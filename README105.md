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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43c337ab-8fc4-3273-9cd8-9cbf74cd60fd | -12.69554 | -54.07433 | 2024-09-28 12:51:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 28.0 |
| af14bb66-c01b-3785-92c7-b128a1662443 | -14.2822 | -53.39218 | 2024-09-28 12:51:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c1c983a5-3b15-316d-9570-646f184513f3 | -14.27217 | -53.39058 | 2024-09-28 12:51:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 5a794433-7982-324d-a737-0b23d206dc98 | -14.27028 | -53.40232 | 2024-09-28 12:51:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a4b8f078-6a40-30bd-b853-bb8e5f78c745 | -15.67622 | -53.90979 | 2024-09-28 12:51:00 | TERRA_M-T | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 695fdcbd-ee2a-3cba-9028-9c62ab4c74b1 | -15.41494 | -53.29875 | 2024-09-28 12:51:00 | TERRA_M-T | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| c4111221-11e2-3503-84ea-caf4ebdf7386 | -10.37899 | -53.77769 | 2024-09-28 12:51:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 50bc70fc-e77a-3ac2-ab32-23eafe175bf2 | -11.22736 | -53.87018 | 2024-09-28 12:51:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.6 |
| a29d5a34-5558-3792-9f3a-eba4cc7a6069 | -11.22298 | -54.76621 | 2024-09-28 12:51:00 | TERRA_M-T | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 32.0 |
| f5ba6eb0-b20c-3762-9df4-4d92700e10b1 | -11.2203 | -54.78272 | 2024-09-28 12:51:00 | TERRA_M-T | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 2ecd6476-00f4-3d13-a161-e8c4a93a698d | -12.69083 | -54.73756 | 2024-09-28 12:51:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 1a984e4d-4602-3201-bc35-3f4332515827 | -12.67948 | -54.7356 | 2024-09-28 12:51:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 8656e207-1923-33e4-b655-700262b5b854 | -17.91458 | -42.1339 | 2024-09-28 12:53:00 | TERRA_M-T | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 38.0 |
| 2e98e1f5-4827-362e-8184-74968558ad74 | -17.91298 | -42.13915 | 2024-09-28 12:53:00 | TERRA_M-T | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 58.7 |
| b108468e-64b5-3d05-89f7-2faf60212d9c | -18.36338 | -42.76472 | 2024-09-28 12:53:00 | TERRA_M-T | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 34.2 |
| eef2180a-20c9-31e1-97a4-180ffe66e91d | -20.12609 | -43.43685 | 2024-09-28 12:53:00 | TERRA_M-T | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.0 |
| 8c59e11e-ec5d-3133-8069-c43f00b0918e | -20.12183 | -43.42842 | 2024-09-28 12:53:00 | TERRA_M-T | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 39.4 |
| 7776a406-aa79-3983-b719-53515bcee975 | -17.8351 | -44.43475 | 2024-09-28 12:53:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 51e3ffe7-610a-39ea-83f4-b43cca75df83 | -17.78562 | -43.29451 | 2024-09-28 12:53:00 | TERRA_M-T | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 5556a6ab-e27a-3cae-9aa4-8316c7422da9 | -17.77917 | -43.28862 | 2024-09-28 12:53:00 | TERRA_M-T | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 13f519bd-193f-38d3-a3aa-8fb0e682a4de | -18.37805 | -44.00169 | 2024-09-28 12:53:00 | TERRA_M-T | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 45083659-e9f0-3d76-a129-0e3264530ded | -18.37482 | -44.0074 | 2024-09-28 12:53:00 | TERRA_M-T | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 46.4 |
| dea53117-c277-346a-9d89-94c21cdc28db | -18.06303 | -44.37786 | 2024-09-28 12:53:00 | TERRA_M-T | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 5cffec45-e326-32b8-aeb0-0bab24490b6c | -18.00154 | -44.34422 | 2024-09-28 12:53:00 | TERRA_M-T | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 2be52b8c-64da-338d-a918-44562acf4cfa | -17.98877 | -44.3429 | 2024-09-28 12:53:00 | TERRA_M-T | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 63ce8951-d417-3736-8a6a-9fa80b69abca | -19.52217 | -44.09677 | 2024-09-28 12:53:00 | TERRA_M-T | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 298bade0-257c-3857-85be-ff81e5912d09 | -19.51827 | -44.10197 | 2024-09-28 12:53:00 | TERRA_M-T | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 33ebf927-1165-30b2-b186-a67a8cd3f5ef | -20.91826 | -43.89401 | 2024-09-28 12:53:00 | TERRA_M-T | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.8 |
| 2b610b91-1137-38c1-a94a-615a603723b7 | -20.11781 | -44.47274 | 2024-09-28 12:53:00 | TERRA_M-T | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 52.4 |
| 7d332d4a-7c0a-3e54-b0f9-9ca83bb90b47 | -20.1156 | -44.47934 | 2024-09-28 12:53:00 | TERRA_M-T | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 87.3 |
| 25fb027f-a8dc-37e5-8515-e9315167f7b9 | -20.11542 | -44.49501 | 2024-09-28 12:53:00 | TERRA_M-T | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 144.9 |
| 8b1a7c5b-6c50-355d-a9f4-e5792882e2dc | -20.11339 | -44.50145 | 2024-09-28 12:53:00 | TERRA_M-T | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.7 |
| 64b1080b-bb88-3dcc-ae4c-b271c025942c | -22.11424 | -44.71424 | 2024-09-28 12:53:00 | TERRA_M-T | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.9 |
| 3ed4f052-c21b-3529-8383-7b234b0ce991 | -17.8596 | -45.89202 | 2024-09-28 12:53:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 1787c261-88be-328f-8976-40d5881f51bd | -17.85774 | -45.90739 | 2024-09-28 12:53:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 34.1 |
| b43a416b-c68d-39ba-956a-60f67ebb52cb | -17.55411 | -45.29179 | 2024-09-28 12:53:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 494af686-425a-3c1b-8bd8-cae058f6576d | -17.55212 | -45.30865 | 2024-09-28 12:53:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 05bae835-d685-3f8b-bf17-6fb1feceff65 | -20.58629 | -46.28222 | 2024-09-28 12:53:00 | TERRA_M-T | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 53.1 |
| adcc247c-c77d-394f-93ae-f55d9a79532c | -20.58449 | -46.29832 | 2024-09-28 12:53:00 | TERRA_M-T | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 92.8 |
| c2853c86-e03e-3687-a353-1478f403ca52 | -20.04099 | -45.55244 | 2024-09-28 12:53:00 | TERRA_M-T | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| d5d47911-2992-39fa-bfd1-514443bbc71f | -19.67098 | -46.21339 | 2024-09-28 12:53:00 | TERRA_M-T | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| ef0e6115-e5ce-31b9-866a-800e10c6cbbb | -21.47228 | -46.81631 | 2024-09-28 12:53:00 | TERRA_M-T | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| bd0c35cb-6e9d-3542-8495-8f123d4f28d8 | -21.47046 | -46.8321 | 2024-09-28 12:53:00 | TERRA_M-T | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 198d7db7-ab76-314c-9461-3fe1acc57e03 | -15.60842 | -57.47522 | 2024-09-28 12:53:00 | TERRA_M-T | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 9727f46b-24c6-3cc0-9304-f02c6dc2ae88 | -17.74027 | -46.32608 | 2024-09-28 12:53:00 | TERRA_M-T | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 6b3b3917-e787-3740-911e-3877bc9bf279 | -17.73815 | -46.31952 | 2024-09-28 12:53:00 | TERRA_M-T | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 23.8 |
| dbb181b1-82ed-3d0a-b1c4-d41cc2b14e90 | -17.38454 | -47.41391 | 2024-09-28 12:53:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 7108a41f-ffb8-3951-b64e-c72093c959d1 | -17.38296 | -47.42617 | 2024-09-28 12:53:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 9761f150-f0f1-3f60-af80-3da837729347 | -17.01016 | -45.92641 | 2024-09-28 12:53:00 | TERRA_M-T | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 617a0bfb-8fb7-3015-a93a-9b1de99f89ba | -20.50267 | -46.89505 | 2024-09-28 12:53:00 | TERRA_M-T | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 7b83c974-d6a0-3d92-a198-47782e6588f2 | -21.84404 | -48.21306 | 2024-09-28 12:53:00 | TERRA_M-T | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 12.5 |
| c49b562b-003a-30e3-8ace-e2e6796b9ac5 | -21.62444 | -47.75937 | 2024-09-28 12:53:00 | TERRA_M-T | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 818ed98b-90ff-36ad-8e2d-ace086f527e1 | -21.614 | -47.75822 | 2024-09-28 12:53:00 | TERRA_M-T | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 8eb56dc4-5e08-31c4-83f7-9f1b23a42ae2 | -21.61243 | -47.77139 | 2024-09-28 12:53:00 | TERRA_M-T | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 5151e894-9a6e-378a-9287-6d6f4a9c9e2c | -21.60359 | -47.75684 | 2024-09-28 12:53:00 | TERRA_M-T | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 65f0d45a-29bf-38eb-a93a-af7239a5e402 | -21.30934 | -46.93518 | 2024-09-28 12:53:00 | TERRA_M-T | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| df90fefb-e54c-39bd-810a-c697859e7ad9 | -21.65122 | -47.22524 | 2024-09-28 12:53:00 | TERRA_M-T | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| cf50f884-c04c-317e-8753-18e0378089f2 | -21.31227 | -46.92696 | 2024-09-28 12:53:00 | TERRA_M-T | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.9 |
| 9232931d-d175-3cca-a1a1-a201eaa4911e | -21.31108 | -46.92058 | 2024-09-28 12:53:00 | TERRA_M-T | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.3 |
| 90bb19e7-655c-35aa-895a-5c98dbd86581 | -22.51945 | -48.59348 | 2024-09-28 12:53:00 | TERRA_M-T | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 7e8d38e2-0ffb-35f1-98f4-60a591124f21 | -15.82575 | -57.36821 | 2024-09-28 12:53:00 | TERRA_M-T | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| b958ca3c-9bdf-384f-99cf-3a82de915f55 | -18.0305 | -48.09158 | 2024-09-28 12:53:00 | TERRA_M-T | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 9768886c-926a-3634-8c78-5ba0deeac717 | -17.14285 | -47.63157 | 2024-09-28 12:53:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| a2abcc0b-433b-364a-8c23-c355352ab3a4 | -17.13298 | -47.63024 | 2024-09-28 12:53:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 46996604-b0fb-338f-99fb-b8380736da26 | -20.55761 | -49.33321 | 2024-09-28 12:53:00 | TERRA_M-T | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 5e717035-2493-32b5-bba4-26425a1b0ec6 | -21.50643 | -49.84336 | 2024-09-28 12:53:00 | TERRA_M-T | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 0c89bdce-ef34-31f1-96e2-8cbd159728d0 | -21.29796 | -49.21719 | 2024-09-28 12:53:00 | TERRA_M-T | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 46d6ac05-98d1-316a-ad53-e41df09a85f2 | -21.29654 | -49.22801 | 2024-09-28 12:53:00 | TERRA_M-T | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 297ce4b6-b747-333d-b239-85c6adb9c4c4 | -20.57876 | -51.30535 | 2024-09-28 12:53:00 | TERRA_M-T | PEREIRA BARRETO | SÃO PAULO | Brasil | 3537404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 4ded414e-193d-333b-8c5e-be925189d806 | -20.57741 | -51.3148 | 2024-09-28 12:53:00 | TERRA_M-T | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 115f1041-88e8-3eea-828f-4cf294db7d97 | -20.51502 | -51.2984 | 2024-09-28 12:53:00 | TERRA_M-T | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.5 |
| da1e93e5-68b5-3698-9f4f-4c9758004d2f | -16.57038 | -50.73418 | 2024-09-28 12:53:00 | TERRA_M-T | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| aba5c59e-53a8-3f85-b809-5b77adb7a6a8 | -16.56904 | -50.74339 | 2024-09-28 12:53:00 | TERRA_M-T | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| b16e6a36-8da0-376e-acd8-3b336cf7ddf2 | -20.65277 | -55.17141 | 2024-09-28 12:53:00 | TERRA_M-T | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b08be401-b8fe-33f7-add1-5a8e72d51c0c | -15.82921 | -57.34887 | 2024-09-28 12:53:00 | TERRA_M-T | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 2900f143-e9cf-39c4-8488-9969ada50320 | -17.11455 | -56.20546 | 2024-09-28 12:53:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 57.8 |
| 0cecb6b5-d574-3f7c-a5ed-ec7aa33bc6d1 | -17.09319 | -56.21291 | 2024-09-28 12:53:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 75.3 |
| 4fb6ab74-198f-3cce-8bb3-f680b7d9e59e | -16.73089 | -55.55425 | 2024-09-28 12:53:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 15.8 |
| ea40c5f0-e019-3a41-b885-3c3de213bb75 | -16.71807 | -55.84148 | 2024-09-28 12:53:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 16.4 |
| 903be472-e008-3c06-8d6e-025f00372e4d | -15.92414 | -57.19056 | 2024-09-28 12:53:00 | TERRA_M-T | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 26.4 |
| d24743d1-c3ed-3882-ac96-1ecc9a89c4a9 | -15.92197 | -57.19655 | 2024-09-28 12:53:00 | TERRA_M-T | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 48d76439-c97c-3ef5-9659-ec636844f495 | -22.71584 | -53.24141 | 2024-09-28 12:55:00 | TERRA_M-T | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 17740c43-896b-3e8a-8f79-4cfe9e1b3b98 | -23.87034 | -53.53608 | 2024-09-28 12:55:00 | TERRA_M-T | CAFEZAL DO SUL | PARANÁ | Brasil | 4103479 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| bad5c6a3-5805-3961-a041-71eb94ccd9dc | -25.32423 | -53.37654 | 2024-09-28 12:55:00 | TERRA_M-T | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 63170e83-639d-386f-a68b-b87f4c51c16a | -11.15 | -45.6 | 2024-09-28 13:04:20 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b2bf66df-c379-3bf8-979f-a4e7cf2a1336 | -10.69 | -46.01 | 2024-09-28 13:04:22 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8283349e-63cb-3be7-8e39-8119d1c89ffc | -10.69 | -46.06 | 2024-09-28 13:04:22 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c8d44c28-f6b8-36a7-8a45-e602166a9d2d | -10.69 | -46.11 | 2024-09-28 13:04:22 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7c50b367-6c06-3f70-a21a-63b5f32db133 | -10.68 | -45.91 | 2024-09-28 13:04:22 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 01e4c554-1e5d-375f-9be6-16d80beebf46 | -10.68 | -45.96 | 2024-09-28 13:04:22 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cfe1def5-16a7-3bea-a569-c5050e37773e | -10.66 | -46.1 | 2024-09-28 13:04:25 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |


