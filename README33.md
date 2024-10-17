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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 298e961f-20b3-3f16-9ef8-09b9ecf3501e | -15.31775 | -53.30732 | 2024-10-17 04:14:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f805d37-31bc-3478-a7e3-3eae87d39f6e | -15.31671 | -53.31275 | 2024-10-17 04:14:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 124934ba-e4fc-3e8d-bad3-6488fb1d6fdc | -15.31523 | -53.30655 | 2024-10-17 04:14:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 77355212-5ac6-3048-9a78-c227ee102bcf | -15.31415 | -53.31199 | 2024-10-17 04:14:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 05c99570-ba78-3393-aa9d-fe91764bd345 | -11.2291 | -54.18481 | 2024-10-17 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 409b8a34-d3d8-3780-8613-97a2ef72face | -10.12849 | -56.77669 | 2024-10-17 04:14:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 4a3844b5-4609-37eb-a6cd-0cc78339a033 | -10.12188 | -56.77537 | 2024-10-17 04:14:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| d10ddd61-4577-3fbe-bcb0-b19473807be1 | -10.96559 | -37.10675 | 2024-10-17 04:14:00 | NOAA-20 | SÃO CRISTÓVÃO | SERGIPE | Brasil | 2806701 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4326af3c-c05a-38f1-bec2-65a9d0c4ca5b | -17.78237 | -42.80891 | 2024-10-17 04:14:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 115a7125-6921-35fe-a2f5-7f48bf0caf7f | -17.77882 | -42.80835 | 2024-10-17 04:14:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8236e36f-61ac-3d0e-9793-bbff49afb63c | -17.75238 | -42.89336 | 2024-10-17 04:14:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5badc15f-10e0-331e-8dd0-566db784d526 | -17.67641 | -42.74247 | 2024-10-17 04:14:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b95bd99-b32c-3a36-82c2-5e50ad18c2ff | -17.48743 | -43.93406 | 2024-10-17 04:14:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9785af7-8e23-38f1-8eb3-b8314bd704e4 | -3.5086 | -51.1122 | 2024-10-17 04:15:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| c51d14b7-8e61-3769-ae09-4ebae7dc03a4 | -3.7007 | -45.9223 | 2024-10-17 04:15:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 9238d734-9071-30aa-9f35-1394e65fb7e5 | -3.7009 | -45.9 | 2024-10-17 04:15:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 7f6b1954-967f-3693-a99d-e224a732e98a | -3.9078 | -42.4256 | 2024-10-17 04:15:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| 61be0338-1d4a-3d9f-bb2a-48a7acb20f73 | -3.908 | -42.402 | 2024-10-17 04:15:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 205.4 |
| 4cbbc38f-ba27-36b0-92ec-6b675d0cde8f | -3.9081 | -42.3784 | 2024-10-17 04:15:28 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 71.2 |
| 3bb3e214-e62f-39d7-a3fd-97398d1dd67a | -3.9265 | -42.4246 | 2024-10-17 04:15:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 148.8 |
| a3952865-faec-3ac1-9c8a-a96d08f94db3 | -3.9267 | -42.401 | 2024-10-17 04:15:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 314.7 |
| d462268d-7e64-3a42-a1b9-067a88b8ad7f | -3.9268 | -42.3773 | 2024-10-17 04:15:28 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 61.3 |
| 2d9eb610-beab-3578-bd38-76de8e643bc7 | -5.5716 | -44.8927 | 2024-10-17 04:15:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 66e509a6-b1eb-3b98-9018-b4850c8db291 | -5.9788 | -45.3621 | 2024-10-17 04:15:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| b24994b4-1d9c-332d-a994-6b6eabca9c11 | -9.1552 | -61.9047 | 2024-10-17 04:15:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 70.8 |
| ed4bedee-0a6f-355e-9ede-82a31d47064f | -12.2123 | -50.3451 | 2024-10-17 04:16:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 84235a8d-17da-3cf7-bc78-45813eed7c90 | -17.99876 | -45.35587 | 2024-10-17 04:17:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ba6987d2-c296-3f6b-bcdc-26a631ae693c | -19.0229 | -46.29576 | 2024-10-17 04:17:00 | NOAA-20 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 59c72e0d-0186-3016-be63-4ec5df16c984 | -18.93354 | -46.30287 | 2024-10-17 04:17:00 | NOAA-20 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2cedade-871f-359a-af94-a3abcaa32945 | -18.93296 | -46.3065 | 2024-10-17 04:17:00 | NOAA-20 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2dad47dc-82cc-3867-9b32-0771930ecc44 | -18.93023 | -46.30228 | 2024-10-17 04:17:00 | NOAA-20 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b30deeb-2544-3f95-ad1b-3c475a17e101 | -18.92965 | -46.30592 | 2024-10-17 04:17:00 | NOAA-20 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ce2f0358-cd9c-3c37-ae21-e0ef6d530479 | -18.82385 | -44.8871 | 2024-10-17 04:17:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a4c89d0-16e2-3ca6-ac4d-05cd46954ce3 | -18.77862 | -45.60192 | 2024-10-17 04:17:00 | NOAA-20 | BIQUINHAS | MINAS GERAIS | Brasil | 3107000 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ccb29f68-083b-35b6-ae80-b2ffa8d98266 | -18.77531 | -45.60135 | 2024-10-17 04:17:00 | NOAA-20 | BIQUINHAS | MINAS GERAIS | Brasil | 3107000 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01c9d108-3d27-3966-b795-2bcc42f7e368 | -20.44006 | -46.16104 | 2024-10-17 04:17:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 31e5b4d9-6ab2-3d8d-9c13-85446a10fd4f | -20.37657 | -45.60241 | 2024-10-17 04:17:00 | NOAA-20 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 24be22fa-20b8-3686-bfcb-32094248524e | -20.31183 | -45.58412 | 2024-10-17 04:17:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a96b562-6249-33ff-990f-2d5533f7a7c3 | -19.66984 | -45.93928 | 2024-10-17 04:17:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8014fc84-d583-3f6c-b6ee-6484927385a9 | -19.66829 | -46.23132 | 2024-10-17 04:17:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3a32a518-59c2-33a7-a87a-1ccf2a07be69 | -19.66442 | -46.23438 | 2024-10-17 04:17:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3b245e61-2123-3d73-a8d2-c4f59fdc3bba | -21.86167 | -46.09781 | 2024-10-17 04:17:00 | NOAA-20 | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e50d38f5-357e-3069-8875-7b9caa7135fa | -21.44056 | -46.60284 | 2024-10-17 04:17:00 | NOAA-20 | MUZAMBINHO | MINAS GERAIS | Brasil | 3144102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 34bc8387-9dd6-3a7f-8028-3cc14a344bf1 | -22.64757 | -47.13319 | 2024-10-17 04:17:00 | NOAA-20 | COSMÓPOLIS | SÃO PAULO | Brasil | 3512803 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 615a7e45-17b3-3219-b49e-738bf9bd0457 | -23.33931 | -46.77258 | 2024-10-17 04:17:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1111d4b7-7ca1-3e9a-8ae2-30790c3e1d23 | -23.16545 | -46.71086 | 2024-10-17 04:17:00 | NOAA-20 | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 050dd0e6-4dfa-3e35-8304-899681a8d0bf | -23.01008 | -47.18262 | 2024-10-17 04:17:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| fa42eca9-68e3-36d2-ba66-068142a9f3b3 | -22.61612 | -46.70621 | 2024-10-17 04:17:00 | NOAA-20 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 757a5bfe-5aef-3817-8f25-bb1da93b2f3e | -22.61281 | -46.70561 | 2024-10-17 04:17:00 | NOAA-20 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d0b1149e-5ee2-318c-835a-e0fb24b3c5dd | -18.37992 | -47.4086 | 2024-10-17 04:17:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0289aaad-cf70-322e-95c5-42f5e306df46 | -20.80799 | -47.97242 | 2024-10-17 04:17:00 | NOAA-20 | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 696e2866-ba32-3627-9553-fe82fa97ca05 | -20.59213 | -47.55086 | 2024-10-17 04:17:00 | NOAA-20 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab0cebdb-7fb4-30b0-9459-51f908dfbce9 | -20.58879 | -47.55024 | 2024-10-17 04:17:00 | NOAA-20 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41753f86-bda1-34f4-bb83-83058d7d72d3 | -20.58818 | -47.55398 | 2024-10-17 04:17:00 | NOAA-20 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3efaa46d-755a-3ee3-aa57-1ff4931e6ce4 | -20.57816 | -47.55213 | 2024-10-17 04:17:00 | NOAA-20 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| caeca4f9-6cb6-30d0-8388-edca5f360504 | -20.57754 | -47.5559 | 2024-10-17 04:17:00 | NOAA-20 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ecc10707-e71b-3991-ad41-0120111af2fb | -20.47497 | -47.5181 | 2024-10-17 04:17:00 | NOAA-20 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 080231e0-3995-3487-af99-fe5173f62ecb | -20.25061 | -47.28551 | 2024-10-17 04:17:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59938e82-838a-326a-9719-a53c66628fa3 | -20.24728 | -47.28492 | 2024-10-17 04:17:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd66dab6-33a4-339d-8a0c-2030914e2948 | -20.07286 | -48.08183 | 2024-10-17 04:17:00 | NOAA-20 | ÁGUA COMPRIDA | MINAS GERAIS | Brasil | 3100708 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 676172c6-4bb0-3c87-a73f-3e64331d9822 | -19.69925 | -46.78539 | 2024-10-17 04:17:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0fbd916e-b3cf-3509-9ebe-4f6b6633da2f | -19.69866 | -46.78905 | 2024-10-17 04:17:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17454012-9ce3-3633-bd30-662b3e1665cb | -22.30358 | -48.33366 | 2024-10-17 04:17:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f117c9e4-9849-3b81-b6b4-cb625e5a1876 | -22.30294 | -48.33752 | 2024-10-17 04:17:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0343a80f-e918-3b9d-bf61-421d1d3a95a5 | -21.81476 | -48.42327 | 2024-10-17 04:17:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 40bf53b3-c0df-304f-ad3a-0339395bd8e1 | -21.8141 | -48.42719 | 2024-10-17 04:17:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f0a90afa-5f13-3f9f-95cf-d19e7fcec60f | -21.81138 | -48.42261 | 2024-10-17 04:17:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 9f780908-9965-3fbe-ae23-8b6478804b1d | -21.81072 | -48.42651 | 2024-10-17 04:17:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 12ee9419-689d-315f-8884-a6abb0e78f71 | -22.8054 | -48.42278 | 2024-10-17 04:17:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 463c37b2-631f-36ad-8321-3913d8e4d235 | -22.6047 | -47.40186 | 2024-10-17 04:17:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f6ab262-f980-34fa-983b-09e6d33d29d7 | -23.36483 | -47.36551 | 2024-10-17 04:17:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2f8ccbad-2118-35a3-9584-93f3afc357f8 | -23.36423 | -47.36927 | 2024-10-17 04:17:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5b32ddc5-3a1f-3662-bed4-6755f224e5db | -22.94097 | -47.38152 | 2024-10-17 04:17:00 | NOAA-20 | MONTE MOR | SÃO PAULO | Brasil | 3531803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| f0f23a61-9569-398e-a529-a0c7c82b714e | -17.85149 | -56.83809 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 82b71ee9-c486-32a0-a8b7-86a968717a18 | -18.66232 | -47.86359 | 2024-10-17 04:17:00 | NOAA-20 | CASCALHO RICO | MINAS GERAIS | Brasil | 3115003 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| fe9a953c-6448-31e5-bd66-ce58daa9f93f | -19.50823 | -49.48384 | 2024-10-17 04:17:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb541987-2874-385b-8fda-9f2da58d0cd9 | -22.3095 | -49.81301 | 2024-10-17 04:17:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f2d22567-49c1-33d2-9357-ad0e095f8249 | -22.53959 | -48.81334 | 2024-10-17 04:17:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7ca2dba-9ff7-3fc0-9f81-d6351aa1f3b3 | -29.81248 | -51.17654 | 2024-10-17 04:17:00 | NOAA-20 | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| a23f3476-1fb6-3534-aab9-fc44136a3540 | -18.27273 | -50.45595 | 2024-10-17 04:17:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8ea55a6-4129-3928-afa3-37225ac77841 | -23.19297 | -50.67805 | 2024-10-17 04:17:00 | NOAA-20 | CORNÉLIO PROCÓPIO | PARANÁ | Brasil | 4106407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2d9f0e91-0886-36fd-9654-6ca83667f701 | -24.243 | -50.74247 | 2024-10-17 04:17:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 54a21417-894f-36d1-822c-604cb5981b01 | -17.84873 | -56.85103 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| a28d8fec-0f76-3196-8098-e15a6bddb67c | -17.84789 | -56.8509 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5b9602ca-4aab-38b2-92fd-651ebe7e62fb | -16.62204 | -51.49688 | 2024-10-17 04:17:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 413213aa-ccf5-3959-87da-a2b04a946c7c | -20.19429 | -52.14056 | 2024-10-17 04:17:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 334a0e6f-01f8-3534-8fcd-297bcc890d00 | -20.19095 | -52.13557 | 2024-10-17 04:17:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d887166c-3235-356a-972c-94d8aa4db7a4 | -20.19019 | -52.13956 | 2024-10-17 04:17:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29512730-d260-3633-8aed-d99e39c04872 | -20.59646 | -51.61112 | 2024-10-17 04:17:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 88b6fe97-921d-3ba0-9ac7-0acfbf501ea7 | -17.84781 | -56.85535 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 5bc4af12-f5b6-3775-8eb0-5b333ca3585b | -17.87676 | -56.8579 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| f7308404-a8ea-39d2-92b8-56265009857a | -17.87581 | -56.86221 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 12c933e6-8bbb-32bf-ab5b-cdf942f851d1 | -17.87487 | -56.86652 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 073b9019-23f0-3d18-98c6-d22314ced52b | -17.8672 | -56.87377 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| bbcef741-fe47-3813-960a-ac0c5054e22d | -17.86119 | -56.84954 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0563fbfb-e786-3ad1-a49b-96055961b80e | -17.86039 | -56.84938 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e1061a30-ce0d-3586-bc8b-763fb010bc07 | -17.85726 | -56.83949 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 753f391e-8391-3cf7-befe-f6101706a107 | -17.85652 | -56.83939 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 2d85666e-97ef-39bf-9f5d-c4fd078b233d | -17.85634 | -56.8438 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4f276ee3-ea88-33ab-9bea-e64345ee226a | -17.85557 | -56.84368 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |


[Clique aqui para ver as próximas entradas](README34.md)
