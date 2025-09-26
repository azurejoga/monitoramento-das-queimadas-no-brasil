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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 796c56d1-9255-32de-883a-dce5b7bfcde3 | -22.42816 | -48.5631 | 2025-09-26 04:17:00 | NOAA-21 | BARRA BONITA | SÃO PAULO | Brasil | 3505302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 24ca256f-dcde-3545-9152-c757eccc8fe3 | -15.38512 | -46.11042 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f818436-2846-3c48-9429-ea344552cb2b | -20.9971 | -50.00432 | 2025-09-26 04:17:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| a025a42c-4db7-327e-af06-8a6ea2b9dda1 | -11.25431 | -45.54245 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 810f64dc-be1f-31f6-ab8d-c1f49a758900 | -11.00575 | -44.34422 | 2025-09-26 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bebf576e-c1e5-301b-b59a-5345f4bcabcb | -14.97783 | -44.41182 | 2025-09-26 04:17:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c18d2214-cc2e-35f5-896f-4bf4d0327eee | -13.85163 | -45.6098 | 2025-09-26 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fcff32d5-e020-3f8e-a5b5-9e5dc88f87c7 | -18.58686 | -45.21522 | 2025-09-26 04:17:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1301eee2-866d-322f-9f62-3f727d742772 | -11.68788 | -44.41898 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bac8e72a-3fce-3f26-a576-b30fa35fa79c | -13.24505 | -50.70053 | 2025-09-26 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0f5f3e47-0706-30fd-9568-562614a4ed70 | -15.90674 | -57.49736 | 2025-09-26 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa8b425e-d475-324e-a81c-9a78ce4abab3 | -11.66755 | -44.46233 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b4e10e24-a246-3d9e-8daf-8f35a394fd9d | -21.00393 | -50.02893 | 2025-09-26 04:17:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8db8278c-2856-3f7e-80d5-ff2ab521f7e6 | -14.82409 | -52.92629 | 2025-09-26 04:17:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9850a8f5-dfbf-3326-9193-0841ccc31744 | -11.43394 | -44.93053 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 241a9d1f-cbc8-3ab6-8421-0abe206efd17 | -22.84047 | -47.1971 | 2025-09-26 04:17:00 | NOAA-21 | SUMARÉ | SÃO PAULO | Brasil | 3552403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8cb745c0-aa75-379b-b626-6fbbe52beb22 | -12.06247 | -44.84973 | 2025-09-26 04:17:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e151332-aa99-3054-af35-c3c44ff69e69 | -16.22168 | -48.80367 | 2025-09-26 04:17:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4e60426c-a2df-3d79-8c0f-4c0557d0eac8 | -15.06943 | -44.98592 | 2025-09-26 04:17:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7e9eb9c9-2128-3df9-8a8d-178cecd3fd4b | -11.65609 | -45.35173 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83e61ddc-3669-3835-9d2f-9a42576efaf9 | -13.84444 | -45.61226 | 2025-09-26 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f5be30b-d52e-37aa-ada8-bce1f2549eba | -11.02001 | -44.33941 | 2025-09-26 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8cebdccf-91b5-31f6-ba8b-52f336c83edf | -22.3581 | -49.47038 | 2025-09-26 04:17:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 707076ff-20ad-3067-b09c-e54c031370fa | -14.59812 | -48.25328 | 2025-09-26 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ed720274-1eb7-356b-80c7-6e023c4c17c6 | -15.54062 | -44.33248 | 2025-09-26 04:17:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 4.7 |
| e8ec0e10-00e1-3a63-a85b-7f247a1312cc | -21.22732 | -49.04092 | 2025-09-26 04:17:00 | NOAA-21 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| ce0add5e-80da-3518-ad74-20382e05e28f | -11.00685 | -44.33724 | 2025-09-26 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bcf2d6bb-15b4-366a-b055-a3ba2f22a5fe | -11.22115 | -45.5777 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e274195-24ea-3e96-adde-f0139c8a2fb8 | -12.98367 | -43.20376 | 2025-09-26 04:17:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ba0ca11c-20e7-3790-9c15-c1ccd5c1a393 | -11.78511 | -44.90511 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e520df05-4d8c-3e22-beb0-3bfd9d3d9bb8 | -20.75947 | -57.88878 | 2025-09-26 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c7908cda-8fa1-354a-b3b1-3887a7f95bb5 | -12.73288 | -46.82347 | 2025-09-26 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d92531e-674f-3564-9e4d-82fa9d286fe6 | -11.0162 | -44.34231 | 2025-09-26 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3da97f63-50d2-37c3-9998-6100851dde2b | -10.60518 | -49.64093 | 2025-09-26 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97813573-9cdd-343f-a01b-df263d51a39d | -11.38236 | -44.95452 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3fe24a50-a350-3447-a1a4-84e3201d198b | -11.43338 | -44.93405 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 33972fe7-8e21-3b0f-8a6d-0e8f1dab1b9f | -12.13268 | -47.95544 | 2025-09-26 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 135cb4a7-4432-310a-9639-8dac2a4688b8 | -11.43064 | -44.92997 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0b1cc71-dfb8-3418-992b-465ca27c7c6e | -22.3871 | -47.5441 | 2025-09-26 04:17:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ecf50a79-fcd8-31f5-9467-72692bf2ffa3 | -17.23647 | -52.40609 | 2025-09-26 04:17:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15d0efc6-98e5-305e-805e-657bc3548165 | -15.52079 | -50.43021 | 2025-09-26 04:17:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ffc25aa6-6e15-35bc-a28a-63b3c555b66b | -12.37138 | -44.15907 | 2025-09-26 04:17:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12932870-aa68-3f12-86ca-96140ce5d0b6 | -11.02445 | -44.35436 | 2025-09-26 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 190d930b-aa08-35d1-b696-1fc771a25624 | -12.13784 | -47.94725 | 2025-09-26 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c3b88c2d-5669-30ad-9ef2-52976c81471c | -11.20913 | -47.83609 | 2025-09-26 04:17:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78279822-022b-3dfa-bd7e-bfbbbd204f1b | -11.63012 | -44.39893 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 66b8c147-cdde-3c06-a879-0a271c21ab58 | -14.88349 | -45.54143 | 2025-09-26 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b4eb47d-41af-3867-bc3c-4736e1b7b82a | -15.52212 | -50.42296 | 2025-09-26 04:17:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7715b73-07fe-3792-a9bf-eca1d02bd273 | -12.87501 | -44.70187 | 2025-09-26 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3508aee4-94f1-38d6-bfe3-6d06cf4450be | -11.06892 | -48.36252 | 2025-09-26 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5daa6bb3-bf28-388b-8f05-60d7cae88c44 | -11.6131 | -44.44281 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08e8f040-3a6a-3f4b-a242-23065be54510 | -16.07332 | -45.18071 | 2025-09-26 04:17:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aa2f80f6-961d-37ac-9010-7be6cf6121ce | -11.79007 | -44.91663 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eef94f28-0a65-3617-80b9-0c253f59042a | -11.69667 | -44.40604 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 97966eaa-eeac-3ebc-848a-af8a88bbb7ce | -14.59737 | -48.25758 | 2025-09-26 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3959c547-6f35-3667-9314-ffa4f44c34b6 | -15.51811 | -45.91888 | 2025-09-26 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3dec5745-38b0-3ac3-937c-474afa2f6336 | -15.51355 | -50.42472 | 2025-09-26 04:17:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 81ace800-df53-33fa-b667-a592141676b0 | -15.5373 | -44.33194 | 2025-09-26 04:17:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 7f17e19d-7eac-33a1-a8e5-00fc04079829 | -15.01974 | -46.94167 | 2025-09-26 04:17:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d578ec2b-4fe2-35ca-9c05-578970f95ca9 | -11.21838 | -45.57357 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 0f9d86de-6775-3d3e-ad73-1fda13507f61 | -11.42283 | -44.97913 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48613d47-036b-398a-a468-f27bc4864675 | -15.07383 | -44.97936 | 2025-09-26 04:17:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90255e5a-0a6c-383f-8f25-e4c2a7c574f0 | -11.4842 | -47.32335 | 2025-09-26 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 44ade6b9-09d9-37a4-a1c8-b68053cfe9f8 | -12.06357 | -44.84272 | 2025-09-26 04:17:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1eda0084-e4af-3f17-b059-6b813f306743 | -11.67029 | -44.44484 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| dcf42a96-6c23-3edb-bafb-a775fba62c3d | -12.56023 | -45.85088 | 2025-09-26 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e58b0022-f2ee-3497-843b-b305b7a2f9d4 | -14.33947 | -44.49548 | 2025-09-26 04:17:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1a99906-75e6-302d-8221-b1bee2841087 | -21.01553 | -50.02651 | 2025-09-26 04:17:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 398e6708-72ad-39c6-b44d-129a6fb18d79 | -20.98911 | -50.00745 | 2025-09-26 04:17:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| e155f591-ea4b-33eb-b110-6fe28703cbaa | -14.10838 | -51.15268 | 2025-09-26 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f281a34-abd4-36c2-8b4e-467d65face8b | -13.19681 | -47.40382 | 2025-09-26 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b3b98b42-2fea-3fa2-9382-14d96f31a3d3 | -14.83756 | -46.70033 | 2025-09-26 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56d6873f-318b-3e0d-a17b-a7a7254f9fb9 | -12.0679 | -47.98123 | 2025-09-26 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0cfe9047-2e02-3a70-8902-ac91267f6b2d | -17.99249 | -48.58933 | 2025-09-26 04:17:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c73a81d7-d8d8-3c28-a804-03bbb8f68b25 | -11.06814 | -48.36718 | 2025-09-26 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e9fcb1f8-328a-3680-829c-4cd6ea6fefbe | -11.67965 | -44.44993 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9cc0c8d0-cb03-3480-b843-352ed729162e | -10.62733 | -53.89192 | 2025-09-26 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b775806b-7b19-3852-a539-7b0f3b25123e | -11.43668 | -44.93461 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0f210448-09b7-3a5e-aa32-796dcb1ad7dc | -11.21898 | -45.56994 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 4433c437-f08f-3824-b90e-8f2d9c366622 | -10.44674 | -48.08377 | 2025-09-26 04:17:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de6addce-0427-33cf-890e-ebbf29f3cb01 | -15.03086 | -46.94356 | 2025-09-26 04:17:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b487542e-8f16-33aa-b5e2-a07f6dbee48c | -13.85551 | -45.60678 | 2025-09-26 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b1bbfa5d-8a0a-35fa-b8e2-f31e3c0b877a | -12.34056 | -47.99325 | 2025-09-26 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 236e1c5d-a6bb-3be1-bacf-d45032fef429 | -15.27307 | -46.42601 | 2025-09-26 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 60ba141d-e448-3504-ab19-6d84dcf31544 | -20.97951 | -50.01953 | 2025-09-26 04:17:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| acaa5950-7fea-3789-8851-d8ad3c7bd3d7 | -11.42502 | -44.98669 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f8afccc5-696b-3876-b115-d4a703e8fa7b | -9.51121 | -54.66174 | 2025-09-26 04:17:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e7c9bd7d-b847-3486-933f-a44ab1c95635 | -13.84718 | -45.61637 | 2025-09-26 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25296ab8-b9a8-32c8-9e54-46d08401d702 | -11.24414 | -45.56295 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d261df80-728c-389e-ae7f-4c0bfe5ea46f | -10.45049 | -48.08438 | 2025-09-26 04:17:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 128c52fe-f742-3ae4-be20-34e7ae195765 | -11.6637 | -44.4653 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 76dc0d0a-e6e3-315a-8b44-d157a139eac3 | -22.60649 | -49.02993 | 2025-09-26 04:17:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41d3aad6-e125-3297-bf95-cdd86c4698e5 | -11.667 | -44.46582 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3cf649a1-082b-3b31-b64d-a595b0939645 | -11.6164 | -44.44334 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e861e7f-c348-3a48-9eea-1eac28651405 | -11.43612 | -44.93813 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 975bfb39-8029-3626-9b74-28d5f5b0a770 | -11.02224 | -44.34686 | 2025-09-26 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 47fef0d9-048a-32c5-a70b-b38d18a67b9e | -11.25155 | -45.53831 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 0548f8cd-5017-368b-95ed-888607ac8a86 | -13.28021 | -50.69879 | 2025-09-26 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e0e45219-990a-3c27-8236-033318e08b8d | -16.42528 | -43.51134 | 2025-09-26 04:17:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2fa1c5c8-9a4d-3b1f-9b0b-412a33a8adb5 | -13.84832 | -45.60925 | 2025-09-26 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README24.md)
