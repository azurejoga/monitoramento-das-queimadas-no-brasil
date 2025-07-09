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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06bb1bda-8010-3260-8b05-ab2d2733e0ad | -10.34844 | -49.91821 | 2025-07-09 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba813e22-c475-345f-a690-36e44d6c29aa | -9.45913 | -56.06093 | 2025-07-09 04:46:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e7ec15e-3de6-3e49-8d1b-0e1f751fc2d2 | -11.83906 | -57.7589 | 2025-07-09 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d54a59c6-508d-3a47-9861-80c1e9b64d7d | -10.70158 | -48.43576 | 2025-07-09 04:46:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fbdf1c5b-241d-3278-b4cf-8e8eb6a67eba | -11.43717 | -45.09581 | 2025-07-09 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0021f4ab-f299-3558-8750-bb15d0c34091 | -9.93979 | -50.85397 | 2025-07-09 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d78d7f5-5886-3163-8d6b-9a4127c3cd5e | -10.58333 | -49.12837 | 2025-07-09 04:46:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 470aaaa5-5cdb-3c44-973d-23aec1fee597 | -13.40052 | -47.87838 | 2025-07-09 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb33960f-9dcd-34df-bfa2-84846f9da5a8 | -9.46194 | -62.19511 | 2025-07-09 04:46:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d49460c-4b04-32b8-bce4-fe5ec6ee9dfc | -9.02006 | -61.23061 | 2025-07-09 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f9054695-9ac6-3b65-89fa-db3e25eff48e | -12.98106 | -44.88157 | 2025-07-09 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 892c7ce3-c167-3cb6-840a-18b96a685794 | -9.22499 | -48.59295 | 2025-07-09 04:46:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 5545179b-c3fc-38ba-80b0-a711bae799ad | -11.47142 | -47.92244 | 2025-07-09 04:46:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 732cb7eb-cfaa-3cfa-a624-54689f85fd3a | -16.62441 | -42.20877 | 2025-07-09 04:46:00 | NOAA-20 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1281ff17-daab-3415-b6fa-1d412a67c7ff | -10.63062 | -51.58936 | 2025-07-09 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d12ad420-ce9b-3965-8f52-76fd528e95b5 | -9.47841 | -48.67812 | 2025-07-09 04:46:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 820bd256-11e7-3e06-bfb0-211148a5ffa8 | -8.58072 | -49.87035 | 2025-07-09 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94a46cff-6366-36bc-bced-ee1de99bd684 | -9.01395 | -49.59702 | 2025-07-09 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2fa6eea8-9eeb-3e68-bb1d-5814cd75c292 | -10.29896 | -57.12449 | 2025-07-09 04:46:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c21c9e64-5ad6-369c-bdd4-82ffbc49de7e | -14.05287 | -46.26398 | 2025-07-09 04:46:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d1edfe5-257c-31ba-b16e-2ad650a3ee6c | -16.68062 | -43.88374 | 2025-07-09 04:46:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f240348b-4e32-3bd3-9ec0-cb70e52253de | -10.17907 | -51.15318 | 2025-07-09 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22e4da14-cff7-3ac0-bb6e-3320d07961db | -12.97591 | -47.82861 | 2025-07-09 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8263ea2d-9b94-353c-9810-7d76cbe85bfb | -10.34527 | -56.48844 | 2025-07-09 04:46:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f170341-eb06-371c-a024-d899160f95bd | -11.90399 | -49.19695 | 2025-07-09 04:46:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5b3f809-05a0-30e7-bd67-22889953eaa6 | -8.31345 | -55.10867 | 2025-07-09 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c2995b07-addc-3e5a-bf41-fa396c77562c | -10.17852 | -51.15672 | 2025-07-09 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b7fbfc3a-35d0-33c9-b69f-32c7d7cca6b2 | -8.97199 | -49.85312 | 2025-07-09 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e21ad67f-0928-333d-89d5-c2e6b2676c7b | -9.22861 | -48.59348 | 2025-07-09 04:46:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| dec4f6d1-d94e-3516-97cf-881904775506 | -10.36524 | -57.50738 | 2025-07-09 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cfbd947e-7ebf-361a-81ac-bc3d1ef2f93c | -11.42591 | -45.1093 | 2025-07-09 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 104ed19b-0301-39c1-9355-06ad7712d03e | -13.63576 | -44.41872 | 2025-07-09 04:46:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66d2b826-3c94-3449-8aae-590fc34a38b4 | -11.11095 | -48.8728 | 2025-07-09 04:46:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6568d8c-421d-3293-9598-e0c7ca734117 | -11.33013 | -55.21469 | 2025-07-09 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb02bca7-36a0-32be-88ea-83e756bee7c4 | -12.97126 | -47.83305 | 2025-07-09 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 053f0987-0461-3bba-be84-29565ba08038 | -9.28589 | -44.83892 | 2025-07-09 04:46:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4b2c6fa4-b0f0-3c6b-bf90-0ea1954c8c43 | -10.56844 | -49.13022 | 2025-07-09 04:46:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 56ca9fa6-0603-3ade-bcd8-bb37766a2700 | -8.76166 | -47.67374 | 2025-07-09 04:46:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7cd88cc3-3b29-3c35-9ee2-8180ecf33761 | -12.97195 | -47.82803 | 2025-07-09 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 025a7cac-1b3e-3786-a546-9e89f2f8ee1d | -9.37735 | -48.95116 | 2025-07-09 04:46:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| faf3e312-f07f-3eec-8b1b-340dedd9eb95 | -11.10793 | -48.86792 | 2025-07-09 04:46:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05825f85-cf4f-3b3e-a8a1-a584cfec6576 | -11.41987 | -54.33327 | 2025-07-09 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6a08acdc-aeb4-391b-9cc3-6ca670ce1791 | -11.51006 | -48.95214 | 2025-07-09 04:46:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f0061678-b9e4-3028-af2b-a938f1e451da | -13.3871 | -47.88772 | 2025-07-09 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fc579a06-26f1-35a0-974b-f994cdab3d17 | -14.04327 | -50.51939 | 2025-07-09 04:46:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 043e4df4-24d6-355d-b22c-b07a9552d18d | -10.56067 | -49.13327 | 2025-07-09 04:46:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| edb62010-9d57-3427-a4c0-913433439456 | -15.7626 | -45.05414 | 2025-07-09 04:46:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e65fadc-9105-30fe-8c6c-c6220fbc0fb9 | -13.00078 | -46.29956 | 2025-07-09 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0a0d0dbf-3912-3609-9523-b5f60a26d3c3 | -13.00881 | -46.75267 | 2025-07-09 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c175a629-0772-36db-a73d-a5fcadc01a76 | -9.34966 | -58.83608 | 2025-07-09 04:46:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c099677-5c32-330c-8087-5c295a4d79c6 | -9.2813 | -44.83826 | 2025-07-09 04:46:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b3f4bcf-1ab5-388d-a395-d543bc3a94a0 | -9.00444 | -47.94135 | 2025-07-09 04:46:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64d4aefc-6038-3515-8298-847f5f7f00e6 | -10.56128 | -49.1292 | 2025-07-09 04:46:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 20e2ca29-7a6a-356e-a970-cb0c588a1d24 | -10.46099 | -47.942 | 2025-07-09 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7447943b-378e-3ea2-b5e0-20e5475d83b6 | -11.43651 | -45.10073 | 2025-07-09 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c8a1e2d9-1cc1-32d1-9169-65991c34bb18 | -9.01338 | -49.60081 | 2025-07-09 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d886b82d-02d1-333a-a2c6-90acf53e3b4b | -9.22138 | -48.59241 | 2025-07-09 04:46:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61a35fef-9555-3f77-ac94-be6adf032e65 | -13.39367 | -47.89893 | 2025-07-09 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32f87f5b-e61a-35ba-9000-ea0a9e10a803 | -13.39183 | -47.8827 | 2025-07-09 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4936ef4e-7bd7-3951-9eaf-af0fec2bb2c1 | -10.57915 | -49.13191 | 2025-07-09 04:46:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a8ce6cbc-9614-3f63-913c-92f229c60da5 | -13.01012 | -46.29653 | 2025-07-09 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 12485748-20a0-32b2-bf1c-27c677577cdc | -11.42062 | -45.11353 | 2025-07-09 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23cfa0db-ca12-37e3-aa0a-6e5159ac572f | -9.33871 | -58.84543 | 2025-07-09 04:46:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e0743871-1b40-3d56-bd0d-2ee12ec86443 | -13.38969 | -47.89846 | 2025-07-09 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9bd3348a-18e1-3fe6-bf7e-78bcaf43cc87 | -10.5768 | -49.12316 | 2025-07-09 04:46:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| bf5ff278-6df0-32a9-a04b-5ff3564f8aac | -14.86219 | -45.12711 | 2025-07-09 04:46:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a39ab97-4375-3354-9fcd-5dfe69835ecd | -9.23223 | -48.59402 | 2025-07-09 04:46:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e512be23-32b1-338a-a75e-22a7d1ee6776 | -10.58272 | -49.13247 | 2025-07-09 04:46:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 427ae85f-7585-3da1-a8f7-a02df601bcbb | -10.29554 | -60.54618 | 2025-07-09 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0bd9d80e-84b3-365c-a56c-6aaa872d33b9 | -13.39655 | -47.87774 | 2025-07-09 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab2ee4e5-73b3-342b-bf11-f7fc5a24350d | -10.57201 | -49.13075 | 2025-07-09 04:46:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4343a862-d9e6-32b3-97e7-228a49979ddb | -11.8752 | -58.7157 | 2025-07-09 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cdedc0aa-a90e-3308-9110-b089d8a4ed01 | -13.70148 | -45.61629 | 2025-07-09 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 71274d22-8213-30ca-8028-80e800e56bed | -8.65333 | -48.49696 | 2025-07-09 04:46:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 78cc93cb-cf56-3ea6-a578-afad57298205 | -16.62393 | -42.21329 | 2025-07-09 04:46:00 | NOAA-20 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7ddea4e4-d04f-3278-9bcb-abd9449b900c | -12.97693 | -44.87543 | 2025-07-09 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 450a550c-d099-3915-b149-77ffffa11c7b | -12.97987 | -47.82919 | 2025-07-09 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 78b6d09a-5b70-3885-92be-157a50479c87 | -9.33348 | -58.84785 | 2025-07-09 04:46:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a1170d6-058d-34a4-b3f0-230b4b417b1f | -8.35054 | -49.95584 | 2025-07-09 04:46:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de52f632-b95e-371f-974d-0a2b394fae9b | -13.01069 | -46.29226 | 2025-07-09 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 407718c0-2453-32f1-8671-42a594088af1 | -9.79399 | -47.74945 | 2025-07-09 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40bf9ec7-d34d-36e7-82d1-20e8e5a8ec29 | -12.97763 | -44.86998 | 2025-07-09 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8abd8d1-6824-3611-bff3-07ed48873a47 | -13.40163 | -47.89995 | 2025-07-09 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 579bd42c-1ab6-32ff-b785-6a98a16570dc | -9.02201 | -61.23064 | 2025-07-09 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32cc9d05-6949-3fed-be86-9cc050583a67 | -13.63611 | -44.4158 | 2025-07-09 04:46:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa0319ab-5a7e-3278-b11d-57e711164d2d | -10.13022 | -57.77913 | 2025-07-09 04:46:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8eb0c343-bbed-3a3e-95fc-45a95e668c10 | -9.01942 | -61.23413 | 2025-07-09 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1221935a-617f-3d28-93bd-627ef8ad9325 | -9.79019 | -47.74882 | 2025-07-09 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e744b3b2-2ff1-3e09-9459-72416bbe1cba | -10.63369 | -49.46603 | 2025-07-09 04:46:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a62d31a0-9f2e-3008-aed7-170e67cbd288 | -12.58137 | -56.97579 | 2025-07-09 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91715423-7a38-383c-ae30-f4a2b1eaa06d | -10.57323 | -49.12257 | 2025-07-09 04:46:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| e33aba70-fa42-3462-9022-07a358ecbcde | -13.40231 | -47.89495 | 2025-07-09 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9e091bf-3c03-3187-a603-19a59ac12c12 | -10.63429 | -49.46205 | 2025-07-09 04:46:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 4fd2dff0-a1dd-3e92-bc5b-78baa2caa984 | -10.56486 | -49.12971 | 2025-07-09 04:46:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3557621a-4c65-34e1-a3fa-931e42de9837 | -9.57693 | -48.56262 | 2025-07-09 04:46:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 58867f33-397c-34aa-bd0e-46be7996c4dc | -8.76138 | -47.67645 | 2025-07-09 04:46:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee40fe87-f255-32ef-8191-44fb34e8ff50 | -12.98176 | -44.87611 | 2025-07-09 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 918e561f-a25c-3e31-8761-af0473bc7b01 | -11.67368 | -43.78467 | 2025-07-09 04:46:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a194d694-4fb8-3660-bc33-6ef9dab94457 | -13.01302 | -46.75359 | 2025-07-09 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9496761-e13e-3169-8985-f00f96e89b46 | -11.52401 | -48.95867 | 2025-07-09 04:46:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README22.md)
