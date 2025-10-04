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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e036471-7818-3e7c-966c-fb55447ad026 | -17.70419 | -47.0976 | 2025-10-04 03:25:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 44.8 |
| e192dcd1-261a-37b5-bf36-0b6061540f17 | -12.53189 | -45.9777 | 2025-10-04 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| efe94e44-a947-3df2-8097-f2ee80c8bd61 | -17.07712 | -46.24877 | 2025-10-04 03:25:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9026357b-1bfb-3931-b56e-d72cc648ed61 | -17.07935 | -43.35325 | 2025-10-04 03:25:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cf5bb200-1ed9-3d4f-98ad-caf5004a787d | -11.80578 | -45.02732 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9e7bc855-53a1-3d3a-8ef9-436ab8df4da6 | -12.03036 | -45.19526 | 2025-10-04 03:25:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 8bc4f671-4945-30e4-875d-a9b8f93950c2 | -11.801 | -45.02734 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e0ad4b14-0c8a-375c-9654-b99493d3acc6 | -12.87007 | -44.62672 | 2025-10-04 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f34f4f92-33c8-3d95-a948-f7b9d4b4b11a | -15.72412 | -46.29087 | 2025-10-04 03:25:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e869f449-48b7-3c75-98ec-61d359e1d5e9 | -15.79398 | -42.17362 | 2025-10-04 03:25:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 24ee5306-0c4c-3390-bf7c-6483d1e45341 | -17.61614 | -44.46207 | 2025-10-04 03:25:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 507b1679-8ee1-3d11-992f-c81a9fefbea7 | -14.92239 | -46.8872 | 2025-10-04 03:25:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5935b759-dc51-3017-93db-21456a020283 | -16.02499 | -44.28495 | 2025-10-04 03:25:00 | NOAA-21 | JAPONVAR | MINAS GERAIS | Brasil | 3135357 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 62ae7ba0-a428-3dfb-b864-505e1aff7674 | -11.8814 | -45.01269 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10858d6a-36a9-348f-a865-cd297119c189 | -12.87575 | -44.6298 | 2025-10-04 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 449cec4a-32de-3adf-bfe2-6f8cd9077c2d | -19.00296 | -43.01606 | 2025-10-04 03:25:00 | NOAA-21 | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b59b2a3f-c3f5-34d7-b077-3d56290bf544 | -11.87391 | -44.98101 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ecb77f58-be3b-3939-bfe4-96de3678f889 | -12.2973 | -45.35915 | 2025-10-04 03:25:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 634b5e06-a478-39ed-9a32-3080ee45c0ad | -17.08228 | -43.367 | 2025-10-04 03:25:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f589f1be-c898-359d-b66a-f04d04a62125 | -15.65185 | -46.26469 | 2025-10-04 03:25:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5bccaa3-70f5-34c5-9771-3435ea6659c5 | -12.86926 | -44.62851 | 2025-10-04 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d634ebc7-2222-34a4-896a-086c76515113 | -15.5791 | -46.90781 | 2025-10-04 03:25:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 71ca96e6-0450-3ab6-a5ff-fcd3f9c951b6 | -17.98331 | -45.00779 | 2025-10-04 03:25:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d0f2d839-fb1c-3031-8f79-22cd72aab43a | -11.44639 | -45.14077 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08b014ca-c65c-3c40-9a13-cdbb45805e6d | -14.23438 | -46.10068 | 2025-10-04 03:25:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d9b537eb-63ff-3062-9b62-f76af4e38751 | -17.63654 | -44.45334 | 2025-10-04 03:25:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4954c37-eba1-33e3-af3f-6fc4cb245800 | -17.57958 | -44.45985 | 2025-10-04 03:25:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c6cf1d0-25d7-3991-8d62-d653de78e634 | -14.22915 | -46.09059 | 2025-10-04 03:25:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 57a6bf7d-a232-3ede-a2f3-97babc316a4e | -14.23462 | -46.09829 | 2025-10-04 03:25:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c95fca90-a1bd-3798-9168-2aeacbd83085 | -12.52489 | -45.97612 | 2025-10-04 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b3d5ca11-9819-31c8-9c2b-9185b53f7f83 | -17.62193 | -44.46386 | 2025-10-04 03:25:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e8a4f147-793a-32b9-88eb-d8ca4f065c37 | -13.81574 | -43.17591 | 2025-10-04 03:25:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 18e622c7-6d59-3736-aba8-2935f800b09b | -15.79469 | -42.17011 | 2025-10-04 03:25:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db466136-162a-37aa-a4fa-9641f54f952c | -11.45217 | -45.14981 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3a339d15-06bb-3c2a-8018-94454440d42e | -12.52755 | -45.98469 | 2025-10-04 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d9b6db41-ce24-3426-884b-c265f4d06e17 | -11.47487 | -45.03586 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 0bfec485-5bf3-320f-b082-8cdc1fed20ad | -11.49084 | -44.99198 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 770efa0c-d3bd-3682-a82c-e86a9fdc55b9 | -17.69854 | -47.09327 | 2025-10-04 03:25:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 33.5 |
| e438b2fa-4736-39af-8b7c-bbf270802b4e | -16.02398 | -44.28968 | 2025-10-04 03:25:00 | NOAA-21 | JAPONVAR | MINAS GERAIS | Brasil | 3135357 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fd30cb6b-2c0f-3f6a-b700-edd200e1b0a6 | -17.70016 | -47.08649 | 2025-10-04 03:25:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 01f3402e-7e72-32bd-b2d5-5335fbc76b4d | -17.98229 | -45.01232 | 2025-10-04 03:25:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2d0fac62-2151-332a-b966-f14669f3615b | -14.23232 | -46.07716 | 2025-10-04 03:25:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 371a7c2d-0711-324f-831a-2d8b98da53dc | -11.49191 | -44.98672 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7815e6db-d4f5-3f96-80d7-ab4d9162093b | -12.87047 | -44.62278 | 2025-10-04 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a240820b-d496-36f8-b7ea-2b4108883e17 | -18.18156 | -43.56285 | 2025-10-04 03:25:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a32f5151-ecf4-31a5-813b-18abd33ac5b8 | -14.30753 | -45.86817 | 2025-10-04 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c124a48f-655c-33b1-89ba-3111378b1c5a | -15.72867 | -46.27718 | 2025-10-04 03:25:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 362538d4-e276-36fe-af88-4fc3af832041 | -14.38396 | -45.97371 | 2025-10-04 03:25:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e11dcbe7-fe0c-3dff-908f-f275d426e84a | -11.88269 | -45.01716 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 216a7e09-8341-3620-9529-056a32a69e0f | -18.59311 | -46.49936 | 2025-10-04 03:25:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad3f90d0-5ece-31df-b8d5-a70e2b1d7ed1 | -12.03846 | -45.19038 | 2025-10-04 03:25:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 84732898-a3f6-3f6b-a7e2-f7014a384d47 | -14.92068 | -46.89485 | 2025-10-04 03:25:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| af8d5ed7-ad5b-3cc9-8a11-13dd258f6c5d | -14.23267 | -46.07495 | 2025-10-04 03:25:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 24.7 |
| c471fd78-f172-3257-876b-d7243424a6a4 | -14.23983 | -46.10869 | 2025-10-04 03:25:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 07443eaa-b926-3c5a-8424-7f224b67df20 | -17.15354 | -47.04403 | 2025-10-04 03:25:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5502654b-d661-355c-a52f-6ed3169623bb | -15.72004 | -46.28385 | 2025-10-04 03:25:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8ec1349d-ddd1-3815-88b5-a38831fbcbe8 | -14.23952 | -46.0765 | 2025-10-04 03:25:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 1c7fa753-19e6-3b19-ab90-577747e92554 | -14.99384 | -42.01896 | 2025-10-04 03:25:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 198c1ab7-7d9a-355c-b75c-3d18380cbc0f | -11.84157 | -44.93453 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 94e382f3-3bee-30f3-87c6-ad7500142fd6 | -13.30394 | -40.5648 | 2025-10-04 03:25:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 54141f4a-1ad3-3b7f-bad0-8e8332954b63 | -14.92407 | -46.89549 | 2025-10-04 03:25:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fbea77f9-a751-3826-9255-04bff7012d23 | -13.16436 | -44.63831 | 2025-10-04 03:25:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1085cfa2-3a2b-3110-9fc6-491dcb14327e | -16.29185 | -45.24214 | 2025-10-04 03:25:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a211b8ae-efff-3cb7-9c1f-0d8afc277430 | -11.49758 | -45.00104 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 682025f1-e39d-3b0c-9156-e079e1b94b8b | -16.35213 | -43.41657 | 2025-10-04 03:25:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e801702-0ab4-33cc-b80a-b40aa6bbf080 | -15.62024 | -46.94156 | 2025-10-04 03:25:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 062dcf40-381c-3009-9d7a-72a4ea9cdc3a | -17.7053 | -47.0951 | 2025-10-04 03:25:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 4e8f3795-4180-389f-8992-10500907be6b | -16.35779 | -43.41778 | 2025-10-04 03:25:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 004f1b08-8811-376b-8387-78756d0ec50e | -17.69741 | -47.0958 | 2025-10-04 03:25:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 128948df-65a0-3dc3-9c8e-f48389d3081a | -17.07851 | -46.24266 | 2025-10-04 03:25:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ccebad21-e3de-39c2-b36d-611046a524c6 | -17.15524 | -47.03688 | 2025-10-04 03:25:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 29900644-2ecc-3b65-a45e-6b1fd60a73db | -11.47609 | -45.02986 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c3297d91-337f-35a3-ac16-d37fb1f18fd4 | -17.15388 | -47.0437 | 2025-10-04 03:25:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 44973eee-7643-3eeb-b8ee-2631775e7cae | -13.82158 | -43.17718 | 2025-10-04 03:25:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2a9bcfe5-3f3d-3023-85fc-644bd664060c | -17.09159 | -46.24606 | 2025-10-04 03:25:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8537ceb4-9db6-3b5d-a85d-02a6e5db3536 | -14.24342 | -46.09119 | 2025-10-04 03:25:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 3b25e53b-76ef-3422-bc30-9f72779cefba | -16.29383 | -45.2445 | 2025-10-04 03:25:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d99763ec-0fb1-321e-b132-cd5708807f19 | -15.52629 | -46.82657 | 2025-10-04 03:25:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 38be8f33-49c7-3e5b-bd35-fec70c2f1b0a | -18.18877 | -43.55307 | 2025-10-04 03:25:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8243764d-14a7-33eb-a00c-000a5ec5a3af | -13.30449 | -40.5619 | 2025-10-04 03:25:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| fb88eaae-c075-31db-a5ef-a084ac2922f2 | -16.82257 | -46.73069 | 2025-10-04 03:25:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7084aa62-2ad4-305d-8efe-28d8db83587f | -15.53633 | -46.83683 | 2025-10-04 03:25:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3470aba2-4247-38b6-b778-9811ad4c2c00 | -13.15794 | -44.63682 | 2025-10-04 03:25:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2656ea51-8cca-3704-9fd8-12a02971ae21 | -16.82087 | -46.73348 | 2025-10-04 03:25:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f0bdabe7-c4a3-35eb-81c8-365ec6ff1441 | -14.23817 | -46.08249 | 2025-10-04 03:25:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 24bc5ad0-8943-3117-9728-0b5e4e401a1e | -12.02906 | -45.20148 | 2025-10-04 03:25:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 4b9a478a-6853-37fc-8704-bc340241d769 | -14.29767 | -45.87499 | 2025-10-04 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7bee0222-ba05-32cc-9d5e-4eeda9890d08 | -17.70574 | -47.09087 | 2025-10-04 03:25:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 57.3 |
| e3990d5b-6bd8-3dab-adc8-5686f85db268 | -11.88681 | -45.02054 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 735046b8-0c2c-3a45-ba66-d095e93cdc0c | -11.8833 | -44.98138 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2a976e08-0188-39cc-96b0-1396ce443cec | -11.47842 | -45.02498 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5f427c2a-8599-3d7a-b006-4581271323b1 | -11.47976 | -45.0186 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1598a0c2-fb8b-32f1-831d-aaed8c4c15e7 | -16.75742 | -43.96145 | 2025-10-04 03:25:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a0f66724-a61d-3854-a29c-42cf4eb8a728 | -11.45859 | -45.15076 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ecbba7ea-4bcb-3b85-a34d-077b89b2cf61 | -14.23622 | -46.09225 | 2025-10-04 03:25:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 3529da5e-c15b-3fb9-a47c-1b8ce346cfb9 | -15.72771 | -46.27466 | 2025-10-04 03:25:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 68955622-734f-318a-82a9-e0375cbd4911 | -17.58467 | -44.46482 | 2025-10-04 03:25:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a7f6813-e1eb-3722-92e8-80f5d20b0309 | -11.72311 | -44.44128 | 2025-10-04 03:25:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c934d5d-8146-3077-acd1-5c1c86208e8d | -15.60656 | -46.93684 | 2025-10-04 03:25:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f2778951-3954-346e-8964-f12d94a11b35 | -15.60799 | -46.9306 | 2025-10-04 03:25:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README15.md)
