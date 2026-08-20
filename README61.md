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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cbe896e5-b19c-3a63-b017-ce83c410835f | -8.68213 | -54.63999 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5de86a18-12c5-3b36-af41-4728e1a446fd | -9.42449 | -60.4157 | 2026-08-20 05:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cbf08ac9-2c76-3fb5-9100-22eb1d9f2fa2 | -8.67192 | -54.64377 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 35ceb337-83d3-3ece-9a79-17e3eb8e525f | -7.86742 | -63.76469 | 2026-08-20 05:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 601724f6-f983-3cd0-b7e8-bd1ae41aea9e | -7.53265 | -55.57881 | 2026-08-20 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4693c315-8ef3-39f2-8657-c1523aee69f6 | -10.33849 | -57.56789 | 2026-08-20 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 441294af-351d-3cc2-b2f0-0674e6420c54 | -7.01741 | -59.54576 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 572195a4-48e8-3790-b2a6-e7858429a930 | -9.25474 | -59.81556 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e0d6232a-9104-3776-9679-ab86acba23d1 | -7.0131 | -59.59869 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d575b5ec-8b20-3d58-97e1-27b86be0eecf | -11.22049 | -54.00795 | 2026-08-20 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0205e4ab-5fcb-3108-9e23-2b246339f503 | -8.57175 | -54.67004 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82f4c710-f1c8-3009-9914-8dba2bd6b704 | -10.452 | -54.6669 | 2026-08-20 05:42:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 16226627-94db-3ca1-a466-cdb2dbe8fb4c | -7.40406 | -55.53304 | 2026-08-20 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb292a9a-09d6-376c-a28d-a11b76838024 | -12.00843 | -53.43911 | 2026-08-20 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17dab83f-8fba-3964-ac1c-4529c9d376b0 | -13.45185 | -51.42662 | 2026-08-20 05:42:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e8f6473-8a6a-3a91-a4ed-a0553f34b56a | -6.58493 | -58.97693 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| de9bd7b8-1be1-3c30-9b37-a6dc8061793b | -12.00323 | -53.43447 | 2026-08-20 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 01b4fe52-42c3-31e4-92cd-27e9a94301e3 | -8.54001 | -54.78392 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3722ccdb-528e-38fd-b0b5-2fa90f3faaae | -9.20841 | -59.77605 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fc9ec9d2-3cae-3f36-8635-b99fc6c03dd2 | -6.86772 | -59.02927 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a836b6ea-eae3-359f-b3c4-360fc3f2df66 | -6.58731 | -58.98594 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b41e7a4-4e14-3b58-bcd5-fd3eb6043290 | -11.21764 | -54.00339 | 2026-08-20 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e34d3db1-059b-3c7d-ac8f-38e788414879 | -11.20968 | -54.00648 | 2026-08-20 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b663f8d5-1f67-3c68-850b-1f95da90da89 | -6.58986 | -58.96898 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a947d75-3974-3fdf-903b-a06fb62f532f | -7.05338 | -56.52405 | 2026-08-20 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a438f510-557e-319b-8d44-105381e08f19 | -13.65669 | -51.77485 | 2026-08-20 05:42:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 406e3f71-9df1-35f4-b1a8-f9ea19542c6c | -11.19344 | -54.00444 | 2026-08-20 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8e580284-0824-368d-aca1-49efa9235b4d | -6.71695 | -59.09061 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50c7f0eb-2005-3d96-8f80-c18d47f3caf5 | -8.09242 | -51.66858 | 2026-08-20 05:42:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5a0a0a63-3b7b-3d89-a449-15af50e23f64 | -8.52836 | -54.86696 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e1955cfe-7a48-3071-a682-f980dd120984 | -9.21627 | -59.77299 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5717c7c0-4120-3097-a564-b92110b104d6 | -6.85374 | -59.02285 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f679ae8-34f1-315d-b9a5-b9c77b9f19f7 | -8.56878 | -54.76783 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3974ed4b-4e7d-359a-a86f-f97122d68e56 | -8.59236 | -54.74267 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 69204acf-0f8f-35cc-891d-075bbfaebe74 | -8.647 | -62.83406 | 2026-08-20 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b369dc52-6f1e-3677-afe2-49afb4076d02 | -8.58589 | -54.75319 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b24ce642-1e51-3187-8163-e8a30e0b4b7b | -8.67485 | -54.65649 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3012bc01-7dfe-3176-8dec-385fa5857b4c | -8.67529 | -54.65604 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e936d8e5-1fcc-3b08-9348-8710f9052b38 | -6.70538 | -59.09327 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8d213efa-c1d2-33f5-948e-5c5fe3b87902 | -6.59846 | -58.96157 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89ece0c5-0d8c-3c36-9216-ce8acd7e07c4 | -9.22286 | -59.77828 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| df8a46cf-78f6-3e7f-91f0-e38709453526 | -11.19031 | -54.02872 | 2026-08-20 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 42b9121e-3393-3bb7-b2e4-e9769256fcb5 | -13.44834 | -51.81723 | 2026-08-20 05:42:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7fcdde0f-18c4-3de6-be5f-42ff001c7a71 | -13.5489 | -52.23095 | 2026-08-20 05:42:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 73c0287a-de9a-354a-8899-f38a54f77bfd | -10.48564 | -50.31497 | 2026-08-20 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ec42adc-2ede-330a-a688-7fe26b6779fd | -7.86696 | -63.74628 | 2026-08-20 05:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a10b5d9-9b5b-3173-a3f8-0c53d65ed34a | -10.48491 | -50.32102 | 2026-08-20 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4b1a72f-df06-3c5c-9858-ff260240ac60 | -13.40497 | -54.37759 | 2026-08-20 05:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 49f581de-7d71-37a0-89e7-0dbf5699ff50 | -8.56155 | -54.66641 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b014547f-63c9-3c8a-b828-a0a9cceda933 | -8.09899 | -51.66541 | 2026-08-20 05:42:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33bac6f5-d709-3cfb-b7a1-3fa993603f45 | -8.53812 | -54.86869 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de8626ea-2e54-3bcc-b71b-6be698e6a092 | -10.39807 | -61.2127 | 2026-08-20 05:42:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69dcef67-6521-3185-a974-039969588f3c | -7.88265 | -63.29519 | 2026-08-20 05:42:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1da1fe57-accd-3146-bd0b-b48089f09377 | -7.87414 | -63.76577 | 2026-08-20 05:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a769cfb-8f81-33ab-b89e-9ec15b7abafd | -7.83122 | -61.61092 | 2026-08-20 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4897599-b935-3fe9-859b-f22980f848e8 | -8.56074 | -54.67216 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92c01596-6e18-3170-a979-6b00dc54c2fe | -6.67865 | -59.09783 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a28f50e-a65c-3a8a-9964-581aa5d00290 | -6.88703 | -56.43126 | 2026-08-20 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 64ea7655-ec32-32ef-a856-dc4a93989da0 | -11.20382 | -54.00925 | 2026-08-20 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82f6643c-affb-3d81-aa35-3e9511008490 | -6.69682 | -59.10062 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1d83486a-3a77-3e39-a4ee-ed2ed2c1153d | -8.40804 | -62.69601 | 2026-08-20 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2d43438-7322-382a-b82a-385b72638720 | -9.42389 | -60.41965 | 2026-08-20 05:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8fe57bce-02a4-367a-bfd3-a80284af77cd | -6.79223 | -59.58304 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38ffffaf-26bc-306d-a45e-00123adbe56b | -7.81387 | -62.32261 | 2026-08-20 05:42:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b729ef43-d531-32d9-952d-2ac6bf3fbee5 | -9.2235 | -59.77408 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a4da6519-862c-3bde-b2c1-bf723cd83446 | -7.55442 | -55.55804 | 2026-08-20 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b3ad7ac-b9df-3543-a6e0-dc26e64f2319 | -8.6691 | -54.66153 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b58d67ed-efc1-3fa1-b63f-4ddf29c723d4 | -12.00794 | -53.44302 | 2026-08-20 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 417ebfa3-7c97-344a-8db6-cf708a7d6d84 | -7.05286 | -59.83696 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10dfb2f0-94e4-3122-968a-76d5bc5417f1 | -8.57341 | -54.72602 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 593360b8-e4a0-362d-b6d9-c3c2be185e28 | -10.74689 | -50.35547 | 2026-08-20 05:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4153614e-ef4b-3c3b-8c2d-d83508adb783 | -8.56805 | -54.77333 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b475079-96c7-3ebb-a857-faca14946258 | -11.18579 | -54.02119 | 2026-08-20 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14b37c75-05a5-36c3-9fb4-bc761cfe212f | -6.6943 | -58.94399 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6c1683fe-fd22-3a2c-8914-23546f8ac2cd | -7.05225 | -59.8409 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac204bf2-050e-3e09-80f7-c6eb64aed35e | -8.67215 | -54.63847 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4608d08f-79f5-34d4-99a7-64ba58f2494d | -8.95402 | -60.55056 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8afb7ec9-aac4-3c04-a7ae-ddee4091b816 | -10.45241 | -54.66381 | 2026-08-20 05:42:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1d020fa9-208d-3089-bea9-bbca765de27c | -7.34625 | -55.67609 | 2026-08-20 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8c7504ac-78eb-3552-bf25-6b3f84e3bda0 | -10.39521 | -61.20837 | 2026-08-20 05:42:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56b9e426-86e1-3a00-91a3-c0255d5000b2 | -11.21509 | -54.00721 | 2026-08-20 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76d32d47-2984-3ff7-8ee8-aaa6acb86d69 | -8.5874 | -54.74199 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2046107d-bea3-30d9-9f90-7555fbdc3a60 | -7.8591 | -63.7635 | 2026-08-20 05:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a83b8c2-bd96-3a45-bccf-f7f408068974 | -8.52268 | -54.87172 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa3d3325-1575-3150-8ded-9031e1927443 | -8.56986 | -54.72215 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d2de7dbd-f469-3afa-92ea-d6dda7a77d52 | -6.59718 | -58.97005 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3518455e-80dc-3bf8-904a-bb8a03f8c18e | -8.53892 | -54.86305 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b011228-3d6a-3eae-8005-a3c33cd0a867 | -8.67271 | -54.63807 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| a7e3bd62-ca1d-3cb1-8d4e-6b87972adbbf | -7.1099 | -59.76756 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 5746329f-3217-3438-838f-d2959c7ab5b8 | -11.82568 | -58.83455 | 2026-08-20 05:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| e34e2e3c-8e66-3d58-9798-c1fb38c069f9 | -7.604 | -60.96154 | 2026-08-20 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0c1d05a-f9cc-3e5e-a614-2af2e77b1fe2 | -9.21328 | -59.76827 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 92a039c2-9ba6-32cf-9f37-b1171aeed1c8 | -7.54442 | -55.5951 | 2026-08-20 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9587af44-8ac4-3c0e-9c12-ed0c19a32e45 | -7.37971 | -55.53909 | 2026-08-20 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e8126ad-3ef4-33ec-9186-f686fd424d71 | -6.92356 | -59.34537 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 500a1147-25be-39c1-9cc6-425d8e3333e4 | -8.10506 | -51.66606 | 2026-08-20 05:42:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f892803-6497-3ff0-ba38-e77eda90818c | -9.12448 | -51.15208 | 2026-08-20 05:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af6e30b4-b611-30ad-82b1-5fc6bdfbff1f | -8.50304 | -54.86909 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b3577661-461e-3f9e-96a9-f9168b0d4571 | -10.78727 | -50.30474 | 2026-08-20 05:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d6964944-473f-3e91-82af-5c5cfde00b5e | -8.53583 | -54.7778 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README62.md)
