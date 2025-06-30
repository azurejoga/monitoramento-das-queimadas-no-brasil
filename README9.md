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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65252147-2bd6-3448-bf81-6acd14660a26 | -12.06242 | -48.46053 | 2025-06-30 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3a02ecbe-1db5-3503-915c-7be895cc7d20 | -12.63038 | -54.21984 | 2025-06-30 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 86f75d93-3f24-3b17-8301-fff2d739f918 | -10.80149 | -55.859 | 2025-06-30 04:14:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1eeae71-1b31-3350-aa9a-4a7937c2b869 | -10.87079 | -53.76439 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a39aaeaf-e2b0-3043-9fb0-f280f38c0c35 | -10.85058 | -53.75275 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06a10d62-dc51-3563-88b3-9e7c7128e3f9 | -10.65078 | -44.48612 | 2025-06-30 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1dcf0ec9-24ca-3cf9-8c0e-95d46b2b2c4c | -9.09792 | -47.95826 | 2025-06-30 04:14:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b290d6a5-dfc2-37da-9e70-1983575230c0 | -10.86396 | -53.74114 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bbaa9a46-f639-3a79-9d91-922eb5191a4d | -11.59066 | -44.66463 | 2025-06-30 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f53a1cc5-f7cc-305d-89c6-94302bf023e5 | -9.4387 | -47.94236 | 2025-06-30 04:14:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 333f148b-3192-3dfb-8208-d9d2f5f5bb73 | -10.84927 | -53.75973 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd91574f-1b6c-3b1a-9dfa-fc7c0d643a59 | -8.08905 | -46.85101 | 2025-06-30 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2eea6369-6652-3e6b-a9f3-1b8c4c894182 | -12.62895 | -54.22705 | 2025-06-30 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 19394d33-9d23-3d5d-a70a-b5d09633077d | -10.87278 | -53.75376 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82e23da0-ab90-32b7-b9f7-7f52bac65de4 | -10.79886 | -44.23812 | 2025-06-30 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 69663fcf-475c-3be1-b128-67e88b607a9d | -10.86879 | -53.7751 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 175fab02-3337-38e8-ab16-9d7ecf519280 | -12.0608 | -48.46978 | 2025-06-30 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0e2dc8d3-4ba8-3409-994c-bcf8981b425e | -10.85123 | -53.74929 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e51bd5c-a584-313d-82d2-264f52cbfa41 | -7.85919 | -47.12937 | 2025-06-30 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0600bd38-c0e3-3024-9ad6-0ef0bc23ba81 | -13.43911 | -47.83376 | 2025-06-30 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b27b9969-194a-3fac-89e4-bf7cfc148f81 | -10.65464 | -44.48316 | 2025-06-30 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e99b2759-e36d-3f89-b05d-710a864b1e2b | -10.87313 | -53.76192 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89f618c5-6b10-3b47-aece-5b1780b86eca | -11.94071 | -57.45497 | 2025-06-30 04:14:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 8ef20eb9-7ea1-3a98-96ac-b82ef4cd09b6 | -11.28359 | -41.86354 | 2025-06-30 04:14:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 27447429-ffb0-3456-af72-b4fe2bbd8d53 | -12.06377 | -48.47226 | 2025-06-30 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f21f3cf3-0aaf-3f66-a829-92fb4d765d5e | -10.62165 | -51.79609 | 2025-06-30 04:14:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd5d3265-48ec-3bba-8bbf-b12c9e104b32 | -10.54844 | -52.0388 | 2025-06-30 04:14:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9ba5d91d-3668-3dc1-99f5-3254ffc32293 | -10.87013 | -53.76794 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca1c6211-e1f7-34c9-8d98-fb913e9691ba | -13.08644 | -54.84965 | 2025-06-30 04:14:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9758baa9-8d26-35fa-ada9-26a33666cbec | -12.06079 | -48.46695 | 2025-06-30 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 98cbfb0d-4ad9-392c-b5b4-b697cdca21a0 | -10.80492 | -44.24268 | 2025-06-30 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9ff9b6bb-612a-37a2-86f3-81fef7d6efe1 | -12.06456 | -48.47043 | 2025-06-30 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 44164998-7f32-360a-8bb3-976d1ceecf6c | -9.69803 | -56.18559 | 2025-06-30 04:14:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f78f8c2b-e39b-30c2-a681-715a2f1a9966 | -11.5868 | -44.6676 | 2025-06-30 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1abf0908-2a0d-3a45-bc85-a22c200cefd9 | -10.87212 | -53.75729 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd15e5a4-9025-3840-8b62-a30933046697 | -17.09504 | -43.80219 | 2025-06-30 04:17:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c29c78c1-ac07-330d-80df-160a7a5cf323 | -22.67274 | -43.04426 | 2025-06-30 04:17:00 | NOAA-20 | MAGÉ | RIO DE JANEIRO | Brasil | 3302502 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c92c1aa7-e0fa-3e39-956c-0490571eeec4 | -20.31198 | -45.58659 | 2025-06-30 04:17:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3e6c947-4c25-33de-9057-8b4ce69b93f4 | -22.67449 | -43.04218 | 2025-06-30 04:17:00 | NOAA-20 | MAGÉ | RIO DE JANEIRO | Brasil | 3302502 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8dba12f6-26aa-35d6-9781-a843b55bd873 | -22.92059 | -43.49379 | 2025-06-30 04:17:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 613a3af5-8cc6-3d2b-87e9-4098a9142a6f | -20.37735 | -45.60153 | 2025-06-30 04:17:00 | NOAA-20 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9828cb1a-17ab-3abb-b316-464b3868e0cb | -15.98669 | -41.98816 | 2025-06-30 04:17:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8c71f8c8-6d77-3da1-95c2-89f8130d86f3 | -21.63329 | -49.84097 | 2025-06-30 04:17:00 | NOAA-20 | GUAIÇARA | SÃO PAULO | Brasil | 3517208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 69ea09f8-8d80-3780-8541-d4a105478c2d | -17.87372 | -53.26093 | 2025-06-30 04:17:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0cba021-b625-3b6b-af6b-cb9a9487ed3d | -17.78049 | -42.80725 | 2025-06-30 04:17:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 851913c6-d1be-31de-bf2f-970aed056f7c | -15.78898 | -48.16399 | 2025-06-30 04:17:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79ea7b31-3fca-3efd-9543-71c8d339477f | -14.03174 | -54.48629 | 2025-06-30 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71692037-84d7-3350-88de-c574ed12a15d | -14.03103 | -54.48982 | 2025-06-30 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e81d2c26-5828-361b-9cc8-049a16f93c7c | -20.30922 | -45.58229 | 2025-06-30 04:17:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa55ed2c-03ac-3d79-a590-66c1f4d901a9 | -16.68079 | -43.8818 | 2025-06-30 04:17:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1303bdc-5ec5-3372-b47e-21ea76931420 | -21.02007 | -50.17393 | 2025-06-30 04:17:00 | NOAA-20 | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 471d395f-5d67-3a99-a2ef-c454e9a4e020 | -15.50915 | -44.75679 | 2025-06-30 04:17:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5e8f3e88-4b49-3499-84f0-0c55678010ac | -15.56943 | -47.85492 | 2025-06-30 04:17:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fbb70f18-5bce-3645-a0ba-db85e58143ff | -21.19671 | -44.93647 | 2025-06-30 04:17:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6e149283-0b55-39d3-8ef5-df0ff40c970b | -21.01688 | -50.17157 | 2025-06-30 04:17:00 | NOAA-20 | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d7cbaa0f-fb49-3960-8c30-f40344f93213 | -20.4154 | -43.55271 | 2025-06-30 04:17:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 9fd720c8-f1b0-3632-87f4-ea32d8ae68eb | -14.86808 | -54.81084 | 2025-06-30 04:17:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49c51c8f-99cb-3b5a-b7e4-6924e7c952ee | -19.71744 | -40.35431 | 2025-06-30 04:17:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7c8c43ae-706a-376a-9a54-7a700047c0f7 | -17.25767 | -48.2802 | 2025-06-30 04:17:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c3c2743-ade6-3633-90d7-cdc6427844a5 | -22.89988 | -43.75224 | 2025-06-30 04:17:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9e5c7b97-6036-37ed-8d71-d58db74e1ef5 | -22.69017 | -44.97824 | 2025-06-30 04:17:00 | NOAA-20 | CACHOEIRA PAULISTA | SÃO PAULO | Brasil | 3508603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3ab1937f-4b14-37cd-ac91-d6ebe93500ff | -21.02051 | -50.17233 | 2025-06-30 04:17:00 | NOAA-20 | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fffbc89a-8c1f-38f8-9d53-53a6f52c92f1 | -17.87272 | -53.26599 | 2025-06-30 04:17:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2cbaea81-db56-3604-a32a-a6f684df7f0f | -19.04619 | -48.48526 | 2025-06-30 04:17:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb630314-b133-3605-b702-e669d6bbf2c4 | -18.68624 | -47.39016 | 2025-06-30 04:17:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76ed82af-a684-30ee-b811-0752d16f1b65 | -15.99032 | -41.98875 | 2025-06-30 04:17:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| efc69978-9dfe-3ce9-bab5-54f925dbd700 | -20.928 | -49.09525 | 2025-06-30 04:17:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3e63fa63-3713-3152-849e-683f1fc92c20 | -17.86813 | -53.265 | 2025-06-30 04:17:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3856136d-f51c-3754-a5bf-cc5f7ac0ec0c | -20.93147 | -49.09594 | 2025-06-30 04:17:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 99403b70-a17b-375a-86f7-9bdfa1070494 | -19.63668 | -45.18979 | 2025-06-30 04:17:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f6a791a-a1b0-3d3d-b36e-939c0dbe89c6 | -22.85524 | -42.97911 | 2025-06-30 04:17:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c364d5e6-9ab1-3df0-a947-c9bb5a6f7d74 | -19.68209 | -45.37914 | 2025-06-30 04:17:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d9dabf9-25c2-396e-b9b8-e53ac0615ac0 | -21.01644 | -50.17317 | 2025-06-30 04:17:00 | NOAA-20 | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9099a195-b997-3326-bfce-f1b9e9bbd7a9 | -19.26667 | -40.00854 | 2025-06-30 04:17:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ddee9d90-7e79-3439-a627-0451730a4b2c | -14.02571 | -54.48859 | 2025-06-30 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 750981f1-f637-3591-9eb9-38e094524111 | -18.05569 | -44.4939 | 2025-06-30 04:17:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 64e718a2-e2b8-3fb5-9012-2a3e35c7db13 | -15.98971 | -41.99306 | 2025-06-30 04:17:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c6c1e451-3a5e-3566-8ae0-a67b6730c5bb | -15.07689 | -48.94572 | 2025-06-30 04:17:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2228cb3a-27bd-3684-b92a-1956d30f1a18 | -16.68022 | -43.88564 | 2025-06-30 04:17:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ce10ede-c0bd-3918-8c0f-e72ebfbf5458 | -22.16094 | -44.38836 | 2025-06-30 04:17:00 | NOAA-20 | BOCAINA DE MINAS | MINAS GERAIS | Brasil | 3107208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ce5e49d1-3669-3518-99ae-075a942c63f5 | -20.90058 | -43.81933 | 2025-06-30 04:17:00 | NOAA-20 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0288e2fc-e36e-36f8-bff4-8027ae54a53e | -21.52304 | -42.62714 | 2025-06-30 04:17:00 | NOAA-20 | LEOPOLDINA | MINAS GERAIS | Brasil | 3138401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 999c5bfe-b44a-3941-8943-a4ad1e60692f | -18.05906 | -44.49444 | 2025-06-30 04:17:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ca937538-c8ee-3955-97f3-4acdfc2a214e | -17.86912 | -53.25998 | 2025-06-30 04:17:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66ec2b34-0ebe-3275-a042-5d9a97719f4d | -22.67551 | -42.85228 | 2025-06-30 04:17:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4b0be1e2-7e95-31e4-8829-0a5ac006b6cd | -17.59503 | -43.19794 | 2025-06-30 04:17:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6782dc25-de37-3b6a-990f-bc39a8b7b5ce | -21.01726 | -50.16868 | 2025-06-30 04:17:00 | NOAA-20 | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c53028e8-1e29-3576-8719-26a7cccff8a3 | -19.4384 | -44.34138 | 2025-06-30 04:17:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80ef5512-5790-3ec9-9ad4-78465413b476 | -17.70599 | -42.72335 | 2025-06-30 04:17:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7bb9f116-a321-3fe2-bab4-9c196a302d97 | -19.31705 | -46.65071 | 2025-06-30 04:17:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cbb070de-6d38-36c8-b87d-d778ac47caaf | -23.40688 | -46.55536 | 2025-06-30 04:19:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 50a650af-deba-3a49-abcb-806278ab7c52 | -23.59514 | -47.43826 | 2025-06-30 04:19:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5a94afb8-e4df-3bea-8086-9d028f6921f2 | -23.7635 | -47.16743 | 2025-06-30 04:19:00 | NOAA-20 | IBIÚNA | SÃO PAULO | Brasil | 3519709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5bb1c9de-e583-3b23-824b-34577fbf7717 | -22.93415 | -45.69373 | 2025-06-30 04:19:00 | NOAA-20 | MONTEIRO LOBATO | SÃO PAULO | Brasil | 3531704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 81819295-544d-33e0-b2e3-736c57e7e6d3 | -22.84842 | -50.23317 | 2025-06-30 04:19:00 | NOAA-20 | PALMITAL | SÃO PAULO | Brasil | 3535309 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7cb6a828-619e-3507-992a-917544262177 | -22.54081 | -48.81213 | 2025-06-30 04:19:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 414129a6-94e3-3564-b9e7-7fe87ab50973 | -10.8046 | -44.2553 | 2025-06-30 04:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 31fcf64c-3552-3690-9ff7-93739dde20a5 | -10.7859 | -44.2346 | 2025-06-30 04:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 68f68f6f-0e56-3de2-97c8-f013016c436a | -12.6319 | -54.2087 | 2025-06-30 04:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| a7d2aa91-a3d5-380c-84a3-b3deac4db9b1 | -10.8241 | -44.2292 | 2025-06-30 04:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 62.2 |


[Clique aqui para ver as próximas entradas](README10.md)
