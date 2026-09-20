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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fbc46863-8305-3a8c-bfe8-d4d6ca4cf143 | -13.31831 | -51.29546 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6fb6f817-95e4-3033-b111-a8773f3965ec | -9.66436 | -54.31498 | 2026-09-20 04:40:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 925747a9-76f2-3baa-90be-9ff9a3174e0d | -11.08995 | -48.30059 | 2026-09-20 04:40:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8d5d18f6-ecf0-3750-a156-2c5ab153acfd | -6.46385 | -48.4351 | 2026-09-20 04:40:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2d4d36ce-8895-30ea-8506-e9cb512199b8 | -10.28767 | -50.21069 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 29430c56-e133-3479-b363-dcac9b181c62 | -12.1549 | -47.03389 | 2026-09-20 04:40:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f4f7e718-1414-3928-97e4-2678f7d5b0fb | -6.3651 | -58.31438 | 2026-09-20 04:40:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 006f7069-0c10-3aa3-8e99-333471ba4402 | -9.39786 | -40.30939 | 2026-09-20 04:40:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 1ed49120-5af4-357d-be83-4ecac5373f50 | -11.72372 | -54.56142 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70f58cb1-8f30-32e2-8fca-ef41d435f294 | -11.01071 | -48.3098 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1a438b9c-65e0-34cc-bee0-ebf33f0547e6 | -7.86487 | -44.84513 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8b5da336-4230-325c-94bf-225c5004df6d | -7.54774 | -45.38166 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ea3bb989-b801-3130-a672-50e882e5c7cb | -9.54322 | -45.48324 | 2026-09-20 04:40:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a6c8848-b5a4-3f04-a855-8face37a7a32 | -10.27499 | -50.26793 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| a4240202-f47e-301c-8e23-c63df79bd4fa | -12.28988 | -47.11775 | 2026-09-20 04:40:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 77fa9d25-a191-3573-b8bb-3de7eeea6c93 | -8.44537 | -45.87096 | 2026-09-20 04:40:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| feff1eac-a2ed-3785-a1dd-877ee8a28f3a | -7.7523 | -54.7542 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bb094e59-6c49-34a6-af8b-4e37c7f7fa51 | -8.23269 | -61.36677 | 2026-09-20 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 60290f8d-7ef7-3a2a-887a-9ef911c5ac21 | -10.26768 | -49.99372 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| adc952d7-4fec-378d-a516-06e58f20f9f8 | -5.8461 | -53.56958 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb8449c8-3049-3f8b-a037-fec777f3f698 | -8.63476 | -47.61309 | 2026-09-20 04:40:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb840bac-d298-3e0c-9a71-20029fbd69e7 | -9.25629 | -45.93279 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e75da5d-1f49-3d5b-8711-e8fb8966832b | -5.8655 | -52.03735 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b834dc8-82ed-3127-8b15-95162a2f0dc0 | -8.052 | -46.29245 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e324e7aa-b7ec-35e9-aebe-41fa0241be3f | -6.08511 | -56.47104 | 2026-09-20 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bbe1408b-cb96-374e-aa5a-8982213116cf | -6.49104 | -58.38346 | 2026-09-20 04:40:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 73a1a855-fa1c-39ed-ba0a-3f4cccd3310e | -12.75875 | -46.13008 | 2026-09-20 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 20eb3a06-9f00-36c7-ba31-0460f2a44272 | -11.37994 | -51.3881 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eefe6d23-22e5-3503-b527-70e8f758088e | -10.78353 | -50.87494 | 2026-09-20 04:40:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1e9c75d8-03dd-337e-900b-0a1b0f978bfc | -9.58069 | -55.10384 | 2026-09-20 04:40:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2c6114de-5c25-3da6-b0b4-297a54d44d23 | -14.12108 | -45.60465 | 2026-09-20 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4da3c427-3dfc-32d5-a052-516269011a00 | -12.58791 | -49.12051 | 2026-09-20 04:40:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c171adb2-327f-36ed-810b-9476614e0e27 | -11.04778 | -54.17535 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3eff257c-79e1-3a3f-9e78-4c6af2328f00 | -8.61478 | -54.60503 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 874772b7-bc46-3f6c-91c4-fd1910c6c346 | -13.01807 | -46.91339 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b650aa2-daaa-3ee9-867d-7576d766353c | -7.53241 | -45.88622 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec199b11-7b80-3f94-893f-6e2d78a0297b | -11.45415 | -45.71095 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60f12a41-789e-3399-92cb-549589486584 | -8.60986 | -47.31023 | 2026-09-20 04:40:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7087a914-7efb-3c9f-a152-cc268d9eb82a | -6.13275 | -59.94394 | 2026-09-20 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ac05a639-07ef-3c13-81ff-ac1015a61555 | -8.69723 | -49.95908 | 2026-09-20 04:40:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6d01ac3-3943-33d6-a6a3-c450102c4365 | -9.04504 | -48.75994 | 2026-09-20 04:40:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dfff6c7b-5745-34f3-8ecf-fe3d356e8dec | -10.77824 | -46.33526 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4296afad-9ae5-3031-a763-c67b9d1a1909 | -7.15282 | -47.4282 | 2026-09-20 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87187a40-c992-3f65-b777-5a4d9ade819b | -11.3774 | -51.40351 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df8e768b-228b-3abd-88b2-3fdf86e2e2e2 | -10.39075 | -48.99181 | 2026-09-20 04:40:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5680bbf7-953c-3690-a5c4-7ea654587a2c | -7.16698 | -47.44441 | 2026-09-20 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 314acf27-bb68-3360-88f5-fb94276a4455 | -11.38995 | -51.41357 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfdc124b-e0a5-319b-898f-4d8b45dfc993 | -10.4159 | -48.33467 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e5476d3-23ae-3219-afb5-859b4e5246ca | -11.85776 | -47.63415 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87e03deb-62a6-3416-be4d-80f4c8c26f88 | -8.15959 | -54.82839 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8b270958-eb6d-30d9-86ef-03bdcf1b5f13 | -11.86285 | -47.66908 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 566b10f7-ec38-3af8-8041-be590d33ce4a | -12.22706 | -50.15132 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 367a562e-b884-3638-958b-9d7fdca55a7f | -9.79515 | -49.02067 | 2026-09-20 04:40:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 22fe985a-1a32-3517-8ceb-90ff0aa09732 | -8.42092 | -54.72775 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f968baf5-433f-3471-83ca-3b449007c64f | -13.94791 | -47.85581 | 2026-09-20 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72a1a3f8-8287-3d24-a175-02b8a277cdad | -11.74775 | -54.56544 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ce4347c-2370-3ad2-8345-04eb76d2d926 | -6.46163 | -48.42767 | 2026-09-20 04:40:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a1efadc-6095-3b45-8d61-8f312b13a7e2 | -7.62971 | -46.76052 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48167292-03f4-3bc6-a8d5-01eaee64f05e | -6.95108 | -45.61848 | 2026-09-20 04:40:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b74f7a99-0b8b-369b-ad71-2a2ba4045c25 | -8.62698 | -47.61912 | 2026-09-20 04:40:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7be483aa-3407-32c9-9831-b7ab3fa65ea1 | -12.75047 | -46.18624 | 2026-09-20 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 93f851d7-b830-3d55-b26e-f8fa3b47aee9 | -10.13629 | -45.56181 | 2026-09-20 04:40:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a72120ce-5de3-358a-8569-a0abba61ccf4 | -8.85171 | -45.93259 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a799384d-bd36-3668-8d26-d8ef5f23f335 | -8.38838 | -45.62933 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 043e3029-4d36-350b-ab4c-8dead5a9faf0 | -7.3607 | -49.68402 | 2026-09-20 04:40:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b857509-fbd3-3c4c-b5bc-903f6fda066c | -8.66949 | -45.33315 | 2026-09-20 04:40:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ce6d53d-3c02-35b3-85d1-62ecccc65071 | -8.99893 | -44.99975 | 2026-09-20 04:40:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2ac36e9-43b9-3228-b0c3-47039673f6de | -7.54681 | -45.4355 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 13c4a614-3d5d-31ee-acb9-daba69ec8c17 | -10.31042 | -50.25126 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4b0277db-6854-3ef2-8535-423b97809a08 | -9.54809 | -46.58035 | 2026-09-20 04:40:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9d9c1ce-7b55-39e1-baa4-c396a4c2c425 | -11.83684 | -46.84381 | 2026-09-20 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 01f6e30d-56d1-330a-b476-ec6acc8ee4e0 | -11.9586 | -49.79084 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c91c760f-b8be-3709-acda-fd2c82123b58 | -11.23546 | -48.37102 | 2026-09-20 04:40:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e46bb23-4064-3341-b04e-7b1e82b84fb1 | -11.3417 | -47.34689 | 2026-09-20 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c899a711-898c-3cb1-bcdb-85cb0a0870d8 | -10.58901 | -46.53883 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ce2f98d1-73ea-32d3-bc91-9541acc10ad9 | -11.86963 | -47.67017 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d90a5813-b3ed-3a67-a365-b92c864ce85c | -10.87875 | -53.99473 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3342443a-1889-36c4-a32f-b2f49026ed41 | -9.73172 | -46.08738 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 755148fe-1ac8-3561-a951-5fa4cf157bcb | -11.07906 | -54.03296 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a49a2def-191d-3f65-92a6-0f2c25ec0a41 | -13.03103 | -46.92318 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 983ffba4-4b88-3246-b26f-09b8d971b24f | -7.7556 | -46.71642 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 778f6041-c761-3cfb-822c-55d427d0df1a | -11.72842 | -54.55852 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68a768da-8bfa-3792-94c0-86aa70199dae | -9.83698 | -46.44567 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e6b07de7-a680-38b0-8538-3732b41305b3 | -9.57993 | -55.10808 | 2026-09-20 04:40:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb3a38ae-a576-3bca-a5e8-66f9f1bd0ec5 | -10.30647 | -50.25431 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| de9a3589-c315-3af2-ae47-b85809ba3b77 | -6.65319 | -50.92669 | 2026-09-20 04:40:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 201cf9cb-4c46-3236-a76a-1a1a3136f52f | -9.57006 | -46.55259 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a627c89a-27ae-3a3e-b54d-a8b2b282917e | -11.27563 | -54.11802 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2cd0382c-e45c-39e9-9b63-2320d4217070 | -10.59761 | -51.90659 | 2026-09-20 04:40:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 048ae08b-32c7-3e23-b3b3-b5bc7539306c | -8.29841 | -50.81711 | 2026-09-20 04:40:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 44ed139c-d118-3767-b2f1-995606cabd57 | -11.6586 | -43.41733 | 2026-09-20 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa1ab5b3-22cf-3ea3-9d52-8e4332693c74 | -11.27424 | -54.12583 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0367872d-d310-3062-a369-1e65bfd92957 | -10.91508 | -53.97445 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f900435d-060f-3962-ae17-d4ddd3abaa4f | -11.77281 | -47.43436 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d46597da-d6e7-3ede-9822-65948dcd81f1 | -11.71967 | -54.56065 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9ef6ab5-244a-331b-9066-3b40012315db | -10.41367 | -48.32709 | 2026-09-20 04:40:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8faa8f0c-5463-368e-a6db-8f6cb904377b | -10.90622 | -53.97828 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd21e702-aa1d-31d1-8b42-2c1018c468b7 | -7.75713 | -44.8866 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 160bdbe3-7283-377b-8a9b-427d4d27e088 | -9.18615 | -60.77747 | 2026-09-20 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2ee146bc-cf0d-3d53-99fc-8e02a7ceecc4 | -5.8827 | -52.04658 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README60.md)
