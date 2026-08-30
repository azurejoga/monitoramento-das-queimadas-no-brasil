# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9afbb02b-9672-314f-83f7-e0f41390e1c2 | -5.95988 | -57.6814 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 631c99d0-0255-3ccf-8ce1-77d30c791bc1 | -9.89385 | -64.98589 | 2026-08-30 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b304acf-2ee3-3792-a0a0-42087b0ca082 | -4.96737 | -55.83442 | 2026-08-30 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c200e920-5616-3e7e-a6d7-b5a3f02936ae | -14.03559 | -54.0151 | 2026-08-30 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ec5417b-0ad4-3e2c-844f-fbeaa5f131ed | -5.88213 | -57.77705 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 82fbaf27-52f2-3ca6-8ee0-0aa401300e49 | -8.73709 | -69.56805 | 2026-08-30 05:55:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 454f81a5-8761-3213-a1d7-45df9d157ba2 | -9.03791 | -67.62131 | 2026-08-30 05:55:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70eb32e1-b1f2-3a8a-99dc-02af238962ad | -10.48013 | -64.5051 | 2026-08-30 05:55:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e958524e-0ee3-30b8-bee5-feaa4f4bbc51 | -9.44955 | -66.73436 | 2026-08-30 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bfd65af-c32d-3a03-90cc-70da3d68a5ee | -8.86484 | -71.46099 | 2026-08-30 05:55:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbdfa181-c4f6-317c-be3d-09ca05b41687 | -11.71021 | -54.53202 | 2026-08-30 05:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3f5f7512-917b-3063-98ac-c47c69f866df | -4.15102 | -60.69466 | 2026-08-30 05:55:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d744b8fa-7ea4-3a0e-bc6f-03a6ae420e79 | -10.73564 | -54.04361 | 2026-08-30 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e89d23cd-c59d-3eec-91cd-93fbaa4bb5fa | -9.93839 | -60.52851 | 2026-08-30 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a892a7de-4cd5-3779-be10-e1ae8c729dd1 | -3.94091 | -59.33389 | 2026-08-30 05:55:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8266abbb-9ca3-34b4-95f6-4865391476c1 | -9.38634 | -66.51499 | 2026-08-30 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6894f5a-50a1-3c52-8329-688d9ae6e773 | -5.97357 | -57.68893 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 56cbefff-efaa-3f41-ab71-0f5b6836f7c1 | -8.91335 | -66.94855 | 2026-08-30 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2028821-c260-39c5-bbf3-6f13361bb3c8 | -4.9664 | -55.84128 | 2026-08-30 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2dee1224-6786-3f0b-a90e-9f23c7423599 | -6.16255 | -57.79411 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8096f5df-ce8e-3e70-84c6-5a45a05e2787 | -5.88362 | -57.76665 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 65eb6aef-b787-3abd-9f0f-6c53a9f0fb22 | -15.21285 | -56.38243 | 2026-08-30 05:55:00 | NPP-375D | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93aefdd1-dcf0-39ba-acae-ee28e51f5566 | -10.48792 | -59.60651 | 2026-08-30 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 483b3147-b8bf-3101-a954-c0150aee76ad | -5.48269 | -57.1496 | 2026-08-30 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b0650de8-bdca-3eca-b7d3-63f329735f95 | -9.98062 | -60.26235 | 2026-08-30 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3591b919-3e9f-37dc-a6e9-1d2193cf3181 | -5.88137 | -57.78238 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1ff3cf44-f9d5-3ba2-9625-5451a0d3224c | -5.48768 | -57.15022 | 2026-08-30 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4cc54745-8a93-3193-bc97-595f480ee07b | -11.44695 | -61.48536 | 2026-08-30 05:55:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af1b4b5c-5431-318d-bffd-5bff2250989c | -8.89462 | -71.4117 | 2026-08-30 05:55:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ac5ff46-4d4c-320e-9eae-adcc8e23e0eb | -4.92487 | -55.77011 | 2026-08-30 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4133111-ef06-3ec0-8a31-e92efde6cf10 | -10.48278 | -59.61032 | 2026-08-30 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 593fa676-0ab7-35ad-b198-2121d8fd51ac | -11.23856 | -54.00032 | 2026-08-30 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9a70ba6b-f687-3c29-a513-2bc4310664ca | -6.07504 | -57.8921 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 000d9498-a247-3ce1-8041-5cede280eef6 | -5.96752 | -57.68914 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e7de62aa-0a4c-3771-9077-76b40f2a863f | -10.47887 | -59.60524 | 2026-08-30 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 49aea570-ecab-3d5f-aa43-65de1f68ff2c | -8.60591 | -70.20528 | 2026-08-30 05:55:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ad97d629-3f08-3979-81fc-85f9b9d9a8ab | -4.15514 | -60.71944 | 2026-08-30 05:55:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| afafa2f6-973c-350b-940e-fceb25c27140 | -9.89329 | -64.98949 | 2026-08-30 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ccb1439b-efd5-3a54-bd70-4cc250d4a506 | -10.4873 | -59.61101 | 2026-08-30 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c4211032-fa15-3ad0-a628-71037e700281 | -14.02811 | -54.02055 | 2026-08-30 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37df8601-1793-3256-b9ea-c4b33c319362 | -6.1133 | -53.56034 | 2026-08-30 05:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d80eec23-0f1f-39a6-9030-5e0b3b0af659 | -5.96976 | -57.67306 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 91b6373f-ab4c-3ab5-84ec-2cc724010fa9 | -6.61612 | -55.45051 | 2026-08-30 05:55:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d2e9e4c0-5683-38d8-9b4c-dc608264bb99 | -9.03571 | -67.61342 | 2026-08-30 05:55:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8c461f5-6d27-386a-a183-021a50070a0b | -11.24058 | -54.00646 | 2026-08-30 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 575e77b5-f8c1-36ec-b717-05b1a221b324 | -9.94316 | -60.52522 | 2026-08-30 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 69a122c4-1023-353b-9e2c-8fae3a47aa62 | -14.4504 | -58.47989 | 2026-08-30 05:55:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 653dfc97-93ad-3493-b787-302bb3900ad0 | -14.42522 | -56.26405 | 2026-08-30 05:55:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0a40a320-5685-3921-b0d2-c4e3655d73da | -13.84718 | -54.0311 | 2026-08-30 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 594f3295-aa54-336b-900d-8f7ae4eddac9 | -6.1672 | -57.79199 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a731a64-ee38-3b2e-b12f-da372a1004dd | -15.12366 | -53.58393 | 2026-08-30 05:55:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| de8e1423-a2a2-3d13-b0ac-fdaf7951a606 | -11.71521 | -54.53456 | 2026-08-30 05:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1da419a-dded-3c41-8941-ad95d87d33dd | -9.04411 | -67.62611 | 2026-08-30 05:55:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f78ca2a-a6e9-3bac-b001-9dbc1fecdb2b | -9.5144 | -65.57756 | 2026-08-30 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 70053705-977b-3c13-969f-df6662b8399d | -14.93904 | -56.33218 | 2026-08-30 05:55:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 13f2792b-19ef-3f1b-a326-07ba32d2705f | -9.9343 | -60.43559 | 2026-08-30 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d561bc51-87ec-30a1-b998-14cc9a791e7e | -5.87734 | -57.77634 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5eae3207-41db-3c65-8639-e74e841f8515 | -5.97033 | -57.67751 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 76f6d6ef-d65d-3f6a-a021-bf53fca2590a | -10.57106 | -59.61059 | 2026-08-30 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7e48bb8d-d9f5-3bd4-86d7-fb6f86472bce | -8.60894 | -70.21077 | 2026-08-30 05:55:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87974b98-69f2-339c-b749-c3b2196182d5 | -8.93185 | -67.37179 | 2026-08-30 05:55:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cc5b0b8-6100-3ecb-b584-5bc0d5176d8d | -8.88237 | -71.26013 | 2026-08-30 05:55:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9c3e2f85-19a7-3b9c-9a55-c70f0bfd4b4e | -4.15629 | -60.68579 | 2026-08-30 05:55:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2affa263-d418-3b87-ba22-8aa9306c0219 | -3.62054 | -60.54753 | 2026-08-30 05:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a31afa74-602c-3a88-8575-49c7d178bbf4 | -3.6228 | -60.54508 | 2026-08-30 05:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d61f69be-0517-3d8f-83a0-f4d823827045 | -4.96288 | -55.84984 | 2026-08-30 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| e36a6f3c-02cd-3b4c-bfd0-a8df294cf3e6 | -11.95813 | -63.28974 | 2026-08-30 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e381430b-7487-3d22-b70b-5361addbb8d8 | -4.9546 | -55.84679 | 2026-08-30 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 7be852b0-262b-3a6d-bfac-1ce6c98dcca7 | -5.8884 | -57.76746 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c93e2724-ad4d-36fb-90a4-e4c02a5e417a | -3.94148 | -59.33008 | 2026-08-30 05:55:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb7a4e68-00a3-3361-afcc-0c1b13cd01ba | -5.95912 | -57.68658 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb2f4526-f5d6-3332-b348-5f215f58f3b7 | -9.9426 | -60.52914 | 2026-08-30 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46f8ca13-f6ba-3248-8121-0c6daa1c4d9c | -6.07979 | -57.89289 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3de6f174-1def-336a-89f0-0c5fae3ed9d2 | -11.18562 | -55.1068 | 2026-08-30 05:55:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 35b6118c-4dc2-3ed4-909f-f05ed8f09cec | -10.75527 | -54.04636 | 2026-08-30 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 10051786-e962-3889-b0f6-4d5f4cd9b3ec | -4.15558 | -60.69053 | 2026-08-30 05:55:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 04d151cf-abb6-3334-b8e9-fd7c27c08892 | -3.62522 | -60.55518 | 2026-08-30 05:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ed3cf588-f927-3258-8fef-f2679688cf5a | -13.86899 | -54.12834 | 2026-08-30 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f5c66608-92d3-32a8-b377-0dd37afff3bb | -15.21334 | -56.37787 | 2026-08-30 05:55:00 | NPP-375D | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c3043d9b-7749-3dc7-825e-ce6f4be2826a | -9.04131 | -67.62188 | 2026-08-30 05:55:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 940b22a8-d23d-3ace-b889-e17e81534869 | -10.5898 | -69.36991 | 2026-08-30 05:55:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3debff29-0bb7-3437-9f71-3b8f7033784a | -13.87152 | -54.12771 | 2026-08-30 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1048b3f6-4fc5-3c23-af5e-616a3ce60105 | -13.86475 | -54.12698 | 2026-08-30 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c5a8166-4a17-3092-8685-c266fa524724 | -4.96339 | -55.8464 | 2026-08-30 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| d8b2d970-556a-35b7-9f8d-21547a5495ee | -6.16334 | -57.78878 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f49ee67-2e1d-3a8e-bb26-ded1a55f2147 | -11.03591 | -57.22494 | 2026-08-30 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b680dfe-5f5d-3067-ad7f-8f1f1935799a | -9.73381 | -67.70382 | 2026-08-30 05:55:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19fdc0e8-6897-344f-b871-78240124889f | -5.85733 | -57.55122 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f03df9ed-cf28-34a3-a536-a4134caad9e2 | -5.88433 | -57.76164 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 834106cf-378f-3d38-9b51-1bcfdc412751 | -8.90131 | -71.3974 | 2026-08-30 05:55:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efdfb0f1-0b7b-323e-b6ec-4f57894994ac | -8.93363 | -67.36092 | 2026-08-30 05:55:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d7ad235c-79f5-38d6-ad5d-eb22fa1c5627 | -5.86222 | -57.55182 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4dc6aa46-a4eb-3eea-9f54-ae28bfde8ddb | -5.90023 | -57.75331 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c7cc784-61b0-364d-b304-e00741717045 | -4.15942 | -60.69111 | 2026-08-30 05:55:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| bd45073e-fb8b-3224-a325-8c9b6ff0a969 | -5.97716 | -57.69069 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2eb3a9d1-0388-3f36-b3fe-44ef5fd6db65 | -9.75337 | -66.75844 | 2026-08-30 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 514e1986-03e2-3248-a03d-e814e734e927 | -3.63291 | -60.55634 | 2026-08-30 05:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 664e1199-e9b8-3fb2-aa49-606c75eeb774 | -8.93244 | -67.36816 | 2026-08-30 05:55:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 478b42b5-8f1e-3da4-8941-ac26702965ea | -4.15585 | -60.71473 | 2026-08-30 05:55:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19d1ad36-3170-3a89-a0d4-76336abb1470 | -5.88984 | -57.75739 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README70.md)
