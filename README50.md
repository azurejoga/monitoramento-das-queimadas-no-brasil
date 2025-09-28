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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10089efd-dcfb-3a9b-a8bc-7f23a144a619 | -20.92581 | -43.09442 | 2025-09-28 04:08:00 | NPP-375D | SENADOR FIRMINO | MINAS GERAIS | Brasil | 3165701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e04e169d-78d1-37f8-8a78-9e1159f6cb2d | -20.69721 | -50.7093 | 2025-09-28 04:08:00 | NPP-375D | GUZOLÂNDIA | SÃO PAULO | Brasil | 3518909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 23f1d95c-cc41-30c3-8231-8b74e2bfd32e | -19.31259 | -43.81503 | 2025-09-28 04:08:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a310474-e73f-375e-93de-564fcaaf70d5 | -15.60157 | -53.16775 | 2025-09-28 04:08:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ab90348-887c-3c51-b64f-a8a48bdad3f5 | -19.95551 | -43.66588 | 2025-09-28 04:08:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 444d5c89-0741-358f-8e92-159ca1485b72 | -18.19769 | -53.32838 | 2025-09-28 04:08:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cc86c486-c7fc-336b-8bb6-603cc821c0ce | -19.79505 | -44.04942 | 2025-09-28 04:08:00 | NPP-375D | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cfcb6fb9-c38a-369d-b4e3-7ce4960a77e6 | -21.16695 | -45.73829 | 2025-09-28 04:08:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b9cb8d9-74e8-358f-9c1e-8afa4ce2a84f | -19.31534 | -43.81934 | 2025-09-28 04:08:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e80a03fa-36c9-3b36-993f-d5412f7e0d12 | -20.22808 | -47.5155 | 2025-09-28 04:08:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 925025d4-d6c3-3181-8155-05c2ff214b30 | -16.96128 | -53.70417 | 2025-09-28 04:08:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 2ffaa1c9-b767-350d-aedd-19a62a7adad9 | -21.61855 | -46.92641 | 2025-09-28 04:08:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 831112c5-a8ab-3a4c-b0a6-cdb979a87ba5 | -19.24799 | -44.08361 | 2025-09-28 04:08:00 | NPP-375D | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26ecc0f7-d86b-312c-994d-a9a3b989206f | -15.80847 | -56.43326 | 2025-09-28 04:08:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c5694384-981e-3fce-b2cd-20d608975cbc | -19.93874 | -43.62098 | 2025-09-28 04:08:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 35e0e4d0-8162-31ec-a41c-7368e14d143d | -17.75655 | -48.76067 | 2025-09-28 04:08:00 | NPP-375D | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f91d5d7a-69c8-39f4-9ddd-468b44bec633 | -18.19877 | -53.32349 | 2025-09-28 04:08:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ebc8e15c-2f30-32a5-bf5b-72e308f07a95 | -20.20796 | -48.68374 | 2025-09-28 04:08:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27514d1a-ed2b-3de7-8371-d371e95667c4 | -18.29226 | -47.68894 | 2025-09-28 04:08:00 | NPP-375D | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 038b56ad-4e82-3199-8a41-f04e16834bc1 | -19.32384 | -43.80942 | 2025-09-28 04:08:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b36a2483-2983-32e6-a9e3-af0cd434b18e | -22.94345 | -49.88147 | 2025-09-28 04:08:00 | NPP-375D | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| fa9ab9d8-ad6d-3b2b-b968-b8280245ebde | -20.22277 | -42.72361 | 2025-09-28 04:08:00 | NPP-375D | PIEDADE DE PONTE NOVA | MINAS GERAIS | Brasil | 3150208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 98614585-d5ed-3390-a78b-0b46d2ec114a | -18.06103 | -42.39697 | 2025-09-28 04:08:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5d395a53-d583-310a-92fe-bd31fd253fa5 | -15.81007 | -56.42632 | 2025-09-28 04:08:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d18c97a-cb1c-3e26-a0eb-7f09ac9e373e | -22.90903 | -45.38689 | 2025-09-28 04:08:00 | NPP-375D | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2b3503a5-1caf-3207-a47e-68d37d2815c2 | -16.58771 | -50.66216 | 2025-09-28 04:08:00 | NPP-375D | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aa141832-158d-338e-9826-7bd7eccd14db | -19.31868 | -43.81995 | 2025-09-28 04:08:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4dd53974-1788-3200-8f16-7d52acd8dd78 | -17.75817 | -48.7522 | 2025-09-28 04:08:00 | NPP-375D | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26c7a633-dd4a-3c7d-8256-c52569fb6fa1 | -19.31139 | -43.82244 | 2025-09-28 04:08:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6704c094-c0cc-3bf0-ab5b-7447261d1a6d | -18.31795 | -44.87309 | 2025-09-28 04:08:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4c665046-3a34-324f-9525-2361632e58a8 | -20.54352 | -45.10299 | 2025-09-28 04:08:00 | NPP-375D | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 468ee555-42c2-390a-9b0b-a38b1faff208 | -15.81523 | -56.42215 | 2025-09-28 04:08:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8d1a41c5-47ce-3251-a63f-8f80964a0edd | -15.80512 | -56.43417 | 2025-09-28 04:08:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0e8def61-93ac-3ee9-a2a4-de21b7b70b07 | -19.86568 | -43.80565 | 2025-09-28 04:08:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| aad8c3cf-61fb-36eb-9def-e108dc1754cf | -20.09666 | -46.17323 | 2025-09-28 04:08:00 | NPP-375D | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c0cd1787-fe39-30be-b4c6-e4cb302367b8 | -18.1849 | -53.32631 | 2025-09-28 04:08:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b123b9d-898d-3c82-ba0e-e1b0d7efbbe0 | -19.93933 | -43.61728 | 2025-09-28 04:08:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 90eae4db-4fc8-3a98-8781-e444642ee091 | -17.50025 | -43.48743 | 2025-09-28 04:08:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6d7b5e1-348c-3a7a-bc12-43537451e74e | -18.36742 | -47.54589 | 2025-09-28 04:08:00 | NPP-375D | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa131cd4-9633-33c5-ab4e-34e8b60f5feb | -17.17935 | -43.37924 | 2025-09-28 04:08:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 33eb5196-8c61-3d52-91ea-dc3b0c427855 | -20.70073 | -50.71539 | 2025-09-28 04:08:00 | NPP-375D | GUZOLÂNDIA | SÃO PAULO | Brasil | 3518909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 7970770d-eaac-3a8f-acd4-cf16691a2dc9 | -17.71874 | -46.71052 | 2025-09-28 04:08:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 40296723-22b4-38d8-aa01-cb75e187aca8 | -20.87112 | -49.35438 | 2025-09-28 04:08:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b0cda429-6a6d-3a08-8127-7bf7a2a4dbec | -18.90664 | -41.12864 | 2025-09-28 04:08:00 | NPP-375D | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| 461c4504-e5ba-3a16-9c52-b48a5ead26e9 | -20.22611 | -42.72419 | 2025-09-28 04:08:00 | NPP-375D | PIEDADE DE PONTE NOVA | MINAS GERAIS | Brasil | 3150208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5f8125c5-f3cf-3c1d-8053-26d7abb9ca4c | -19.31929 | -43.81623 | 2025-09-28 04:08:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac76aafe-a29d-3323-aaf2-60108bb26482 | -19.78512 | -42.25864 | 2025-09-28 04:08:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4c6f8369-a43a-38eb-b29d-1142c47367fe | -15.81372 | -56.42884 | 2025-09-28 04:08:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f0dc12b8-b4f3-372d-b5cd-2e15df2ed024 | -16.26863 | -50.2204 | 2025-09-28 04:08:00 | NPP-375D | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dee90447-24b4-3f88-bd8a-0c0deb8f9ca7 | -17.18723 | -43.37318 | 2025-09-28 04:08:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bade5c29-1bbf-3db8-bab0-fed0b8289800 | -15.77957 | -50.158 | 2025-09-28 04:08:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 501b1bef-b2c8-320a-bb42-9aaae48a8464 | -22.34665 | -47.33326 | 2025-09-28 04:08:00 | NPP-375D | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f1ae7f6b-c9b5-3d11-bfed-ceeff7eb5f01 | -20.41157 | -46.46944 | 2025-09-28 04:08:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45e8fe6a-802d-3ed0-a6f3-2bf3a8b24a32 | -21.07165 | -48.66668 | 2025-09-28 04:08:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 25bda440-8793-3ac4-ac86-31ccca738c98 | -18.11205 | -42.19156 | 2025-09-28 04:08:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d43eb3c4-fda4-35e1-a385-7cd2d98d5173 | -21.79944 | -45.32957 | 2025-09-28 04:08:00 | NPP-375D | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e5821518-34fe-368d-a4e3-67a5255ee824 | -22.90837 | -45.39079 | 2025-09-28 04:08:00 | NPP-375D | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 95891f4c-19b1-3dd7-9fd6-e18f7586eec2 | -22.52976 | -49.11259 | 2025-09-28 04:08:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81a93bd8-f015-319f-9d99-11230e909546 | -16.58804 | -50.66248 | 2025-09-28 04:08:00 | NPP-375D | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6e16c005-7fc7-3211-8bf6-909407c556c8 | -19.24401 | -44.08675 | 2025-09-28 04:08:00 | NPP-375D | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a232daf-63ef-3b5d-a58d-d5f2d9193b6e | -17.72717 | -46.70713 | 2025-09-28 04:08:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1a2b42d-f73e-379c-971f-043a7d1ffdd3 | -17.72168 | -46.71596 | 2025-09-28 04:08:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6edd20c4-4e8b-3c44-9bf9-9fd864712861 | -21.87455 | -45.29846 | 2025-09-28 04:08:00 | NPP-375D | CAMBUQUIRA | MINAS GERAIS | Brasil | 3110707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ec85d520-474b-38ef-84bc-df5fab0fb4a1 | -19.3281 | -43.82562 | 2025-09-28 04:08:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eff92e56-d09f-334a-a377-0e39d1c220f7 | -19.49811 | -44.26304 | 2025-09-28 04:08:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a767f6a-af2e-3c3a-9607-4d9bed86e63a | -23.20637 | -51.37377 | 2025-09-28 04:08:00 | NPP-375D | ROLÂNDIA | PARANÁ | Brasil | 4122404 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 75601c12-5a40-3661-98d6-b86d46ff30d8 | -17.18328 | -43.37622 | 2025-09-28 04:08:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fec46aa5-c692-32b0-bf79-d1c171aec32b | -19.31989 | -43.81252 | 2025-09-28 04:08:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dbbe35d3-440b-37f6-aac9-acb58c6eb9c1 | -19.86961 | -43.80259 | 2025-09-28 04:08:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 32b13c95-09a9-33f4-8de0-1e3180856d96 | -17.18819 | -43.38844 | 2025-09-28 04:08:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 602ec017-b239-3ffa-8468-d7512821dbf6 | -17.24831 | -43.8718 | 2025-09-28 04:08:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48890ea8-63ab-3036-be30-068b391cd751 | -23.53112 | -47.16417 | 2025-09-28 04:08:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| cdbba07c-6230-3925-b751-d1a93165a6a5 | -21.58437 | -48.84974 | 2025-09-28 04:08:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 20.8 |
| fb2e4289-0cc0-35f1-9cda-ffcc161d66d6 | -22.73736 | -46.13185 | 2025-09-28 04:08:00 | NPP-375D | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2ba61443-207f-3471-9bb9-bea3f1cfd68a | -20.99453 | -50.00931 | 2025-09-28 04:08:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2e1f75f2-be9c-3a62-9ca3-671310598b03 | -17.72046 | -46.70095 | 2025-09-28 04:08:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9a959f30-ee69-38f7-aa70-71bcc171e933 | -18.94442 | -43.88815 | 2025-09-28 04:08:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 61f447b2-4bb9-38aa-8479-be383380b594 | -18.20069 | -53.31475 | 2025-09-28 04:08:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8b6251af-39c9-3832-aeb8-16202f2d1301 | -21.61936 | -46.92181 | 2025-09-28 04:08:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6be263bb-b869-3739-8385-bf554d09bf8e | -19.50576 | -46.34285 | 2025-09-28 04:08:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b5a93a80-1758-320f-b2a3-2c7616eb1986 | -20.69319 | -50.71202 | 2025-09-28 04:08:00 | NPP-375D | GUZOLÂNDIA | SÃO PAULO | Brasil | 3518909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| b1dc822d-606a-362d-8f6b-4be0fbaf5cab | -21.00306 | -50.03502 | 2025-09-28 04:08:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6b823d96-8b45-36e4-bba4-1bfec6e663eb | -16.96226 | -53.69966 | 2025-09-28 04:08:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ae2acb00-b8b7-3526-8cd7-6c62a3074a90 | -18.39252 | -44.53784 | 2025-09-28 04:08:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e1bd380-2f7f-3ba6-8cfe-11720a3c063c | -20.99796 | -50.01489 | 2025-09-28 04:08:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 88202e6a-8e17-3a3d-8f6d-f6cec0b0bf2f | -16.95543 | -53.70255 | 2025-09-28 04:08:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 65fe758d-83cc-3733-963e-d3e26e7f17ef | -20.41235 | -46.46499 | 2025-09-28 04:08:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7e0781f-c0d0-3595-a151-010b8285fb5e | -20.71224 | -45.0129 | 2025-09-28 04:08:00 | NPP-375D | SÃO FRANCISCO DE PAULA | MINAS GERAIS | Brasil | 3161205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9e563bf3-1f15-3d4f-b146-d1f39126a810 | -16.96812 | -53.70123 | 2025-09-28 04:08:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5cf36ecd-e7c9-31db-ac8b-71c3749b1f5a | -19.84725 | -42.59944 | 2025-09-28 04:08:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 07fb0cdd-d147-32b9-9b31-6cb3085ea580 | -22.81977 | -47.32928 | 2025-09-28 04:08:00 | NPP-375D | NOVA ODESSA | SÃO PAULO | Brasil | 3533403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d346354f-df31-3a7a-aee0-3012900ee4ab | -19.32537 | -43.82125 | 2025-09-28 04:08:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48afa2af-6473-310a-849e-39b43f845094 | -18.904 | -41.12884 | 2025-09-28 04:08:00 | NPP-375D | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| b4a3a674-2166-3ce2-8d5e-c09f3bd70b05 | -22.06063 | -43.01398 | 2025-09-28 04:08:00 | NPP-375D | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 92f2ed90-3532-3067-8fb5-e7055857728c | -20.87109 | -49.35418 | 2025-09-28 04:08:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f012eccb-c502-350a-906f-0c3292bf7f9e | -18.19979 | -53.31889 | 2025-09-28 04:08:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0c3a10ad-2b29-3147-bffb-c8e830cb9dc3 | -18.10885 | -41.43802 | 2025-09-28 04:08:00 | NPP-375D | FREI GASPAR | MINAS GERAIS | Brasil | 3126802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5692548b-f11b-3b82-905b-dcc716fee5f4 | -18.2043 | -53.31858 | 2025-09-28 04:08:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2b896db-5fc5-3b65-b8d2-5c5a0f37e334 | -19.3287 | -43.82191 | 2025-09-28 04:08:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2483a203-b7d3-3e95-855d-88f8b864e7ee | -19.50476 | -41.69718 | 2025-09-28 04:08:00 | NPP-375D | INHAPIM | MINAS GERAIS | Brasil | 3130903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |


[Clique aqui para ver as próximas entradas](README51.md)
