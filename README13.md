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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56c96c75-ef52-3b2f-ad25-9801f0b09054 | -20.87823 | -45.89051 | 2025-08-07 04:04:00 | NOAA-20 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2b401a6c-4bcd-3594-b305-a2adc85d6fa3 | -19.77651 | -44.04879 | 2025-08-07 04:04:00 | NOAA-20 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| b2c24ff1-bb22-3e0c-860a-8ff10bfe5322 | -17.11457 | -49.14452 | 2025-08-07 04:04:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d17699f-b888-35b4-80c3-5b1222688eb5 | -16.0412 | -43.72068 | 2025-08-07 04:04:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4416a66e-8689-34fb-8d54-d3ca90fdfb2c | -18.71287 | -47.51224 | 2025-08-07 04:04:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f0693378-b650-3a2e-b81a-103cf1c5a5d3 | -22.33638 | -44.92424 | 2025-08-07 04:04:00 | NOAA-20 | PASSA QUATRO | MINAS GERAIS | Brasil | 3147600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 01d8a79f-bf9f-3b36-b5db-467f2c427a16 | -19.84389 | -49.07415 | 2025-08-07 04:04:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01ba1a93-36b5-3772-aebb-12bc369a3126 | -17.07572 | -48.00374 | 2025-08-07 04:04:00 | NOAA-20 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5fe5790c-648c-38fb-a82c-481b31e911ee | -18.66052 | -46.52532 | 2025-08-07 04:04:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4d4e5fd-51bf-3f93-b31b-2e190083d5e5 | -21.23573 | -49.08257 | 2025-08-07 04:04:00 | NOAA-20 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| 1521b985-c125-3b84-a082-9696b9a71d12 | -18.84672 | -47.05081 | 2025-08-07 04:04:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ab7819f-e2a2-380e-9605-2080ab72a515 | -22.66847 | -47.62036 | 2025-08-07 04:04:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 784993c0-ec92-3d9d-9535-92ec7ecb035e | -18.89559 | -41.00813 | 2025-08-07 04:04:00 | NOAA-20 | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f0177f3e-4079-3b28-9a57-ecd6e0d2741f | -19.43809 | -44.93349 | 2025-08-07 04:04:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d60351e-7c83-3ee7-965a-5ec6c5dc7d67 | -18.73041 | -39.86996 | 2025-08-07 04:04:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 141d2af5-a685-3e38-8c95-a5730604554c | -18.80523 | -46.76553 | 2025-08-07 04:04:00 | NOAA-20 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8569ba7-123f-3efb-b189-1c9d5d84eab6 | -18.84287 | -47.05225 | 2025-08-07 04:04:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e07f4d7f-45ff-3fa1-9b8f-302e51ecdff9 | -18.76424 | -44.4701 | 2025-08-07 04:04:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7129b23d-d703-365c-86f4-2e52cfa4cbe1 | -16.04058 | -43.7244 | 2025-08-07 04:04:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49b14d9f-7fc8-3af9-9e2c-d0e76e4e9bd3 | -18.35785 | -42.74009 | 2025-08-07 04:04:00 | NOAA-20 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 106bfa9b-941a-3ae7-a29e-aa8a173c5349 | -20.54483 | -47.41938 | 2025-08-07 04:04:00 | NOAA-20 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d273a5ed-e395-3d17-a66e-45a123883c6f | -16.08284 | -43.63625 | 2025-08-07 04:04:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70c005f9-a26a-3877-a475-d640d491ee98 | -21.235 | -49.08633 | 2025-08-07 04:04:00 | NOAA-20 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| e6ab1b2b-7df6-3af5-9e75-db3c2b792823 | -19.84314 | -49.07809 | 2025-08-07 04:04:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a7fd6bc0-5b38-324a-86fa-c8e0580a125f | -21.47373 | -49.65707 | 2025-08-07 04:04:00 | NOAA-20 | GUAIÇARA | SÃO PAULO | Brasil | 3517208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| ab54b9d4-36ef-39c4-8d14-af9d061c4ae3 | -21.03167 | -42.83299 | 2025-08-07 04:04:00 | NOAA-20 | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f48c8825-8abe-3236-aa53-9862152fbb9b | -19.24239 | -45.13586 | 2025-08-07 04:04:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 79e79b78-6e3e-378b-84d8-782f3106047b | -16.88443 | -42.0668 | 2025-08-07 04:04:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| aa939e9e-1ab4-39a8-a1e0-eb084245831e | -22.33753 | -47.20482 | 2025-08-07 04:04:00 | NOAA-20 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 09aa1546-41d8-3dc0-a9cb-0128e0810dd0 | -19.84728 | -49.07898 | 2025-08-07 04:04:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c4d9ef3a-fd8f-38cf-994e-570fd604ab51 | -22.82784 | -47.15266 | 2025-08-07 04:04:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2bdd1958-cdea-3314-ae35-3a983c0f6b1a | -20.3341 | -41.44708 | 2025-08-07 04:04:00 | NOAA-20 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| fc51c3c1-34f3-3122-bc55-c0e669ecced9 | -19.84652 | -49.083 | 2025-08-07 04:04:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ee6f30f-7879-3fba-b1b4-2dfdf50285ed | -21.46875 | -49.6603 | 2025-08-07 04:04:00 | NOAA-20 | GUAIÇARA | SÃO PAULO | Brasil | 3517208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 6b366489-2510-3f2b-a6bf-cb461128b0f5 | -21.9765 | -42.88551 | 2025-08-07 04:04:00 | NOAA-20 | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a23bf088-f64f-33f2-9d2b-4fb928238af5 | -20.7566 | -48.04519 | 2025-08-07 04:04:00 | NOAA-20 | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63d7831d-dc7e-35de-989d-3b3b7f87b3ea | -18.84662 | -47.05298 | 2025-08-07 04:04:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f3b70e3-e3ce-3046-bb80-92086479b56e | -21.21219 | -45.62001 | 2025-08-07 04:04:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 897ebe31-124e-3b79-b5fe-fd81431fc5d6 | -17.98744 | -51.26032 | 2025-08-07 04:04:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c22f4fc-231a-351a-9c51-b5f9238bb46a | -21.11393 | -47.04169 | 2025-08-07 04:04:00 | NOAA-20 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9d9920f-afa3-3066-9ae9-aa6c257ee666 | -21.13526 | -43.28035 | 2025-08-07 04:04:00 | NOAA-20 | MERCÊS | MINAS GERAIS | Brasil | 3141603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 74b8e075-73ca-3cdf-be41-72fe023edb4a | -22.03468 | -43.21466 | 2025-08-07 04:04:00 | NOAA-20 | COMENDADOR LEVY GASPARIAN | RIO DE JANEIRO | Brasil | 3300951 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a1f23680-53d6-348d-9093-5b58c85118b8 | -21.11113 | -47.03628 | 2025-08-07 04:04:00 | NOAA-20 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d43acfbc-ff99-348a-a882-6667d543ae96 | -22.73841 | -42.96082 | 2025-08-07 04:04:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| efec88d4-0046-327e-9959-4c45e427f711 | -14.50395 | -52.77342 | 2025-08-07 04:04:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 97b4ee26-f991-31d6-851f-9fc5f39d077d | -22.66533 | -47.62218 | 2025-08-07 04:04:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e5f92de8-682d-38be-b116-d3517d7951c8 | -21.11032 | -47.04087 | 2025-08-07 04:04:00 | NOAA-20 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3bd7cd60-0d94-3c45-ae33-9e7f25205328 | -21.25001 | -49.03003 | 2025-08-07 04:04:00 | NOAA-20 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d58cd421-3f64-373c-b6d1-f9bcf498760d | -16.01398 | -47.30406 | 2025-08-07 04:04:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 417a154e-8e63-3cec-81e2-fd3868b114a7 | -22.34114 | -47.20555 | 2025-08-07 04:04:00 | NOAA-20 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72c0dfe7-a98b-3548-862e-780878e58187 | -19.23832 | -45.01366 | 2025-08-07 04:04:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e845f8ac-e1a1-3c77-8a8a-2d41414d1aef | -14.50487 | -52.769 | 2025-08-07 04:04:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00884f52-b260-332c-9321-31382cf62375 | -21.70907 | -45.27885 | 2025-08-07 04:04:00 | NOAA-20 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| dc0c580a-b834-3d69-9a8e-6ebef2ac223c | -21.46956 | -49.65614 | 2025-08-07 04:04:00 | NOAA-20 | GUAIÇARA | SÃO PAULO | Brasil | 3517208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 39ad2030-245e-3e16-8e7e-cb61f1e5fdba | -21.47293 | -49.66122 | 2025-08-07 04:04:00 | NOAA-20 | GUAIÇARA | SÃO PAULO | Brasil | 3517208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 1dde1007-68f3-34b7-84a7-9e5a2e535fb2 | -22.06781 | -47.32421 | 2025-08-07 04:04:00 | NOAA-20 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0f35ac4b-4cbc-3f4a-99d5-79f7c369c683 | -16.71213 | -50.68983 | 2025-08-07 04:04:00 | NOAA-20 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a9f4ffe-74ca-3583-bbe0-5761d6d17f94 | -23.30973 | -47.48922 | 2025-08-07 04:06:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3a10d765-673e-3407-b851-f831ad5295cb | -23.3033 | -51.17704 | 2025-08-07 04:06:00 | NOAA-20 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c5c8647c-3768-39e5-a3ad-cec1f4b11b00 | -23.53506 | -51.46704 | 2025-08-07 04:06:00 | NOAA-20 | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ca9755b0-1af2-3f45-9d52-e1e9a7e42202 | -23.71832 | -51.73236 | 2025-08-07 04:06:00 | NOAA-20 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 94e2d559-e4db-3c64-a1f6-81dc3fd76bcb | -23.71876 | -51.72976 | 2025-08-07 04:06:00 | NOAA-20 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 89a7114f-da7b-3397-9821-c1fe0429d6c0 | -23.7138 | -51.73115 | 2025-08-07 04:06:00 | NOAA-20 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 096267c3-99ea-3b28-80a3-f09839d7c19c | -23.71767 | -51.73486 | 2025-08-07 04:06:00 | NOAA-20 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| a5d61a03-795b-3de6-8734-5402bf0bcf47 | -25.01406 | -50.10555 | 2025-08-07 04:06:00 | NOAA-20 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 08681a56-9fc0-31a4-8444-bcb365561ce7 | -7.4074 | -60.0108 | 2025-08-07 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 140882d4-e055-3a9f-8021-749a75d376f4 | -10.6247 | -44.767 | 2025-08-07 04:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 5897d4b7-9f96-3848-9560-3880d062d063 | -8.9213 | -60.7489 | 2025-08-07 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 8eaeb77e-dc84-34bd-98c2-ac7200bb3239 | -10.6438 | -44.7645 | 2025-08-07 04:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| fede1810-0b9b-3d38-a593-be1ff7dfa64d | -10.625 | -44.7439 | 2025-08-07 04:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 74.2 |
| a6306fcb-efad-393b-b09f-afe421a6e34d | -8.9028 | -60.7498 | 2025-08-07 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| d33ab2e6-d011-3839-a655-67863a3ffaed | -10.6441 | -44.7413 | 2025-08-07 04:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 58cda124-9697-3a3c-9494-7ce9f5069120 | -8.9215 | -60.7297 | 2025-08-07 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| a00971db-0d55-3af2-b53b-74417d809970 | -10.6441 | -44.7413 | 2025-08-07 04:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 95.9 |
| c1fcfe45-ac40-333c-9912-e34e9fe99d76 | -7.4074 | -60.0108 | 2025-08-07 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| a01fdbbc-7265-32c7-859d-18b3f653c392 | -10.6438 | -44.7645 | 2025-08-07 04:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 859b962e-5f2b-31a3-a17e-5968aba1896e | -8.9213 | -60.7489 | 2025-08-07 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 158.6 |
| 9dc3017a-b1a8-3a79-b54b-098483469e41 | -8.9212 | -60.7681 | 2025-08-07 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| fdd4ba1e-2b86-3326-b337-5490c4bf165b | -8.9215 | -60.7297 | 2025-08-07 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| bba053d7-3ec3-384d-a566-23d8d5d1d893 | -10.625 | -44.7439 | 2025-08-07 04:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 97835cad-b274-3395-8949-efa2e7d8a18e | -10.6441 | -44.7413 | 2025-08-07 04:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 67e313b6-0c37-32d6-ae8b-df8d5cae3a4e | -8.9213 | -60.7489 | 2025-08-07 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 128.0 |
| 4c7a23f2-96f3-32ea-b98c-e89274611c01 | -8.9215 | -60.7297 | 2025-08-07 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 3adad6b0-6e52-3384-8112-daaf37596052 | -8.9399 | -60.7481 | 2025-08-07 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 63679e58-759b-3872-b597-3318d4f42890 | -7.4074 | -60.0108 | 2025-08-07 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 629c6329-fa74-3cca-ba04-4bc1e24ddd04 | -7.4074 | -60.0108 | 2025-08-07 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 013d7fbf-9772-324e-91f7-e81b9b30de31 | -10.6441 | -44.7413 | 2025-08-07 04:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 508af08c-b19e-3288-a5f1-65672dd9b346 | -8.9213 | -60.7489 | 2025-08-07 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 156.6 |
| ebee64a6-091f-3d8b-828e-72e9e69774c0 | -8.9215 | -60.7297 | 2025-08-07 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 5eaae9d9-736d-3c5c-aa5a-acd7b90f7943 | -8.9212 | -60.7681 | 2025-08-07 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| ab92e72e-9b97-35ff-8112-0b697483b32c | -7.4074 | -60.0108 | 2025-08-07 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| af9f7439-7b7d-3537-942e-c56a92f3e3d2 | -8.9213 | -60.7489 | 2025-08-07 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 161.6 |
| 05ec3595-74ef-34e2-8017-b512dc95be05 | -10.6441 | -44.7413 | 2025-08-07 04:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 6e725ae0-3f9f-3c73-a290-5bb4de79352f | -8.9215 | -60.7297 | 2025-08-07 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 7735b644-64f9-39ed-9dc4-872d9600cbd7 | -10.6438 | -44.7645 | 2025-08-07 04:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 6e133fe5-bea2-3741-af8e-636e98e7e4a4 | -8.25458 | -45.08133 | 2025-08-07 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 094da11a-34dc-3405-9434-e5edaaaa7b06 | -10.64085 | -44.7466 | 2025-08-07 04:51:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2c684485-b939-3858-8cbd-b2bfde665f72 | -8.9092 | -60.60175 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1edb0b02-705f-334b-9ead-7954cb96eb82 | -9.08533 | -45.05893 | 2025-08-07 04:51:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f251575a-33dc-3991-9683-922bdb98d3f5 | -8.92073 | -60.58228 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README14.md)
