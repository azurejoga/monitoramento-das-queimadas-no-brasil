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

## Dados Diários - Página 227

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 753e12f1-b454-31f4-9320-5d55f48c20e8 | -14.66865 | -40.49561 | 2026-10-08 15:39:00 | NOAA-21 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| c794928d-5042-393b-bc0a-206396886b75 | -14.76363 | -39.81252 | 2026-10-08 15:39:00 | NOAA-21 | SANTA CRUZ DA VITÓRIA | BAHIA | Brasil | 2927804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 24.4 |
| 5eda2572-f145-398e-86e6-9328d9c00855 | -14.14327 | -40.79101 | 2026-10-08 15:39:00 | NOAA-21 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 33e88052-16e3-3eed-83b4-2ab90feeadcd | -14.59728 | -41.02321 | 2026-10-08 15:39:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 33.5 |
| d5e86551-a851-3f7c-ad4c-8fa7605af558 | -11.61378 | -43.62207 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 07b42176-160d-3547-89e5-65d3586f8585 | -14.67243 | -42.48288 | 2026-10-08 15:39:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 1f7d005b-e859-3c52-a9cf-3bbd2ca3fc0a | -12.18917 | -44.80748 | 2026-10-08 15:39:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 0f4b1b76-1f7b-335f-838f-795a0fb7da24 | -17.43158 | -40.41827 | 2026-10-08 15:39:00 | NOAA-21 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 2054016b-e2ab-3649-9823-e3e152a7bfc4 | -11.10643 | -39.42255 | 2026-10-08 15:39:00 | NOAA-21 | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 139bf33a-402c-3358-90c7-a73dc1d5b77b | -12.22967 | -44.70987 | 2026-10-08 15:39:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7699e549-cb5c-3231-8ae6-92672519c70f | -14.41812 | -41.51004 | 2026-10-08 15:39:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| a9e98f9e-5d46-3f7e-97d6-c646b3cc988b | -11.58918 | -43.67542 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 202.8 |
| e995b8e6-da77-3de3-ace7-bba372fadcc4 | -14.25831 | -42.4418 | 2026-10-08 15:39:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 72.0 |
| fef7053b-5e25-3c53-bd7a-0a58a105c163 | -14.64637 | -41.25297 | 2026-10-08 15:39:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9bd7606b-e59c-3926-a0db-a7958ca634e8 | -14.8219 | -39.40788 | 2026-10-08 15:39:00 | NOAA-21 | BARRO PRETO | BAHIA | Brasil | 2903300 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| d73f20b9-1ff1-348b-a205-425356bcb8e2 | -15.10508 | -43.63332 | 2026-10-08 15:39:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 23.7 |
| b7ea0c6a-1b4c-3b99-b042-862ffad360c2 | -14.00013 | -40.1601 | 2026-10-08 15:39:00 | NOAA-21 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 03ba0df1-a63b-3fae-b7cf-761ac03ab539 | -11.6195 | -43.6137 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.1 |
| f51740a0-6380-33bb-adba-5aeffb4eff3c | -14.0354 | -40.55478 | 2026-10-08 15:39:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| bf19d2df-91f1-360d-9659-f27ba851bea7 | -11.6354 | -43.7023 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 2dea3586-ff03-3a41-80ff-ac8e50b76715 | -11.62917 | -43.69426 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 5526fa76-9704-33bf-bedf-38d78b4024ec | -13.92677 | -40.63214 | 2026-10-08 15:39:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4f8f4561-2710-3b0e-ae20-ce9c92e383f6 | -11.28909 | -41.12547 | 2026-10-08 15:39:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 29.8 |
| c5cb016a-6ac6-3374-ae57-6990a8a125a0 | -14.47179 | -40.72609 | 2026-10-08 15:39:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 26.5 |
| 0226c465-dcc2-34a4-a2ef-600e97a5c88f | -14.85824 | -42.06763 | 2026-10-08 15:39:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 48.5 |
| 734cd71d-1e44-39b9-bc45-09c15858fcdb | -17.1152 | -41.34026 | 2026-10-08 15:39:00 | NOAA-21 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.8 |
| f0a71f1c-4408-3904-9256-d6bd4af8a278 | -12.15952 | -42.26416 | 2026-10-08 15:39:00 | NOAA-21 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 67.2 |
| 2fa5ffea-1c35-30e5-a002-205bf473bab1 | -15.01104 | -40.8219 | 2026-10-08 15:39:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 605da846-4694-3798-92b0-ab2f14c421fd | -12.1899 | -44.65425 | 2026-10-08 15:39:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 87922a28-f13b-32f5-b5af-e5febada55ed | -11.61621 | -43.63853 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 35.4 |
| d3a2c368-7e2d-3269-9b28-acbffd360ebd | -10.77102 | -38.49736 | 2026-10-08 15:39:00 | NOAA-21 | RIBEIRA DO POMBAL | BAHIA | Brasil | 2926608 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 2170f868-85c4-3539-b166-e28f14f79dbc | -14.95789 | -41.79173 | 2026-10-08 15:39:00 | NOAA-21 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d6144d50-8f58-3345-a81e-b0b9b905e4e1 | -13.739 | -43.51988 | 2026-10-08 15:39:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 7fce6485-8bc8-380f-ae53-86b753366ebb | -14.42371 | -41.50933 | 2026-10-08 15:39:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 10.6 |
| c400ae19-be5e-37b5-a877-817c98a9a78a | -11.60153 | -43.67352 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| c270dba4-2dc7-39b0-a449-a5676eb944da | -13.57507 | -40.46515 | 2026-10-08 15:39:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| a47d548e-e7a7-307d-b37f-59c5846540db | -15.56325 | -44.53663 | 2026-10-08 15:39:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 78bc8127-8b0b-30d7-a43b-cc9a334b111c | -16.84771 | -40.5966 | 2026-10-08 15:39:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 78ac314c-d55d-3fb8-bdf8-68c089d32700 | -15.31422 | -40.64842 | 2026-10-08 15:39:00 | NOAA-21 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 85343b73-23e7-38da-892a-50a1cae74f30 | -11.46081 | -43.38129 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 37.3 |
| add3f83a-7050-3ffe-85c9-d652c0e08a68 | -17.92294 | -42.2847 | 2026-10-08 15:39:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.9 |
| 4a594ceb-8c71-3fff-9c15-ed8be24937d9 | -11.54628 | -37.96908 | 2026-10-08 15:39:00 | NOAA-21 | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Caatinga | 20.4 |
| 14df9fb9-84a4-3803-b138-2e6bccd90ef3 | -11.76952 | -45.55465 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 828eab1b-f2cb-317a-9bfb-99a1da7ff431 | -12.2191 | -44.67538 | 2026-10-08 15:39:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 523a05a7-c789-3928-8d71-f1f4675465ea | -17.06774 | -40.02418 | 2026-10-08 15:39:00 | NOAA-21 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| c11babd3-e436-33da-9bd6-81261ba74545 | -14.26423 | -42.44112 | 2026-10-08 15:39:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 72.0 |
| b65908db-3862-3a34-ac15-1ed2f1866ec4 | -13.47834 | -42.48434 | 2026-10-08 15:39:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| e27b05f4-d60b-369d-a3dc-01ed741cd494 | -13.29834 | -41.51738 | 2026-10-08 15:39:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 34.0 |
| 670a0f36-caef-3850-970f-8be851ebd43e | -13.83506 | -39.58595 | 2026-10-08 15:39:00 | NOAA-21 | NOVA IBIÁ | BAHIA | Brasil | 2922755 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 4f2db628-b85e-3aec-989b-b6da03204ee1 | -12.04142 | -43.43909 | 2026-10-08 15:39:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 0c9dd87c-ecab-3cf3-9f60-e15f0aa2f555 | -14.11204 | -40.27093 | 2026-10-08 15:39:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 13.0 |
| d0bb38c8-0422-3d02-86e2-7dd0e3949c34 | -11.62161 | -43.6838 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 1619bc2c-c7d7-32be-881c-510dd3993ea3 | -16.15923 | -43.63884 | 2026-10-08 15:39:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 0d73b58d-401b-361d-ba34-ee4c0ba8ce2f | -11.77332 | -45.58747 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| c296ac44-b317-39d0-a71f-3559a7570e52 | -11.75453 | -45.48716 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 8a79c0f5-f419-3f88-9504-e67bd9a511c4 | -17.12102 | -39.51543 | 2026-10-08 15:39:00 | NOAA-21 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| be9261c4-47e8-33f6-8dd7-fe0db047a03f | -13.95622 | -44.85199 | 2026-10-08 15:39:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 7c62b50d-0bab-339d-90e3-6c5c92dc66f9 | -14.47112 | -40.73009 | 2026-10-08 15:39:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 121.7 |
| 17e52139-a1e4-3cc9-a9d9-8575cae1c37c | -11.76658 | -45.52916 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 3f61e965-897e-33f5-bb1f-85e436edc6eb | -11.58862 | -43.67071 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 346.9 |
| 9075e389-2429-3460-8b9f-1679f96a5ec2 | -13.96369 | -44.85732 | 2026-10-08 15:39:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 63.5 |
| c1babec5-5004-3e55-b2f9-63ca39ad0ec3 | -15.96899 | -40.69694 | 2026-10-08 15:39:00 | NOAA-21 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0ee199a0-4976-317b-bd34-aefef0f4027d | -18.06142 | -41.50197 | 2026-10-08 15:39:00 | NOAA-21 | FREI GASPAR | MINAS GERAIS | Brasil | 3126802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 88db51c6-05a6-3f82-8d31-593a7a8c66eb | -12.18385 | -44.82023 | 2026-10-08 15:39:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 199.0 |
| 4f81321e-5229-3c43-907f-9b51d2c934d5 | -12.71264 | -45.8197 | 2026-10-08 15:39:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 132.5 |
| f70261b8-42c8-3186-a30e-f93d727b927f | -11.62915 | -43.70275 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 057b48d0-eccf-3a7d-8512-d7169376c896 | -12.18727 | -44.8162 | 2026-10-08 15:39:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| f164194b-0f51-35b0-a231-0f954334f59a | -11.97773 | -39.04903 | 2026-10-08 15:39:00 | NOAA-21 | SANTA BÁRBARA | BAHIA | Brasil | 2927507 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 0c21559c-37c7-38f4-8b1e-f86f2c312110 | -17.10857 | -41.35073 | 2026-10-08 15:39:00 | NOAA-21 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| 41cef883-6e4c-3aba-869a-9a1d59ee7539 | -11.71801 | -43.65482 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| a5415f82-d0bb-3002-b5a1-5c0934ef14cd | -12.15636 | -44.71698 | 2026-10-08 15:39:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 41.5 |
| b5c36dee-31a3-3c36-9f3d-84fafb95a12d | -12.01256 | -42.07044 | 2026-10-08 15:39:00 | NOAA-21 | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 4593c56c-4af3-35b9-8724-2c36b769f554 | -14.76151 | -41.32789 | 2026-10-08 15:39:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| acb4b152-dda8-32f0-850d-f2d7f68ab2c2 | -13.74531 | -43.51924 | 2026-10-08 15:39:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 37e1964a-e574-3784-986d-c6341fa54210 | -11.6466 | -43.6822 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 01341bbc-f61e-3db4-ba5c-a3e6c9aa3fb1 | -14.45417 | -41.23704 | 2026-10-08 15:39:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| dbd87b19-559e-33b0-82c9-c1a0a5d46e9e | -17.7042 | -43.29117 | 2026-10-08 15:39:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 258c1fdd-ca9f-3fe5-a042-0308b169de1f | -14.53672 | -41.27509 | 2026-10-08 15:39:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 2268c36f-5299-3d73-b5fa-d794395414ca | -15.40445 | -44.33382 | 2026-10-08 15:39:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 23.8 |
| a5d57c73-7728-3db0-8a07-86d1d73683bb | -11.83343 | -43.52626 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 3e78af3e-3e65-3b4c-828f-22b4b9b83e3d | -17.94439 | -42.31564 | 2026-10-08 15:39:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| d00f0895-a278-3976-95fe-82d72cc51f6c | -16.45541 | -41.25766 | 2026-10-08 15:39:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| dfa66a57-320a-3373-8355-df6603dbab47 | -14.59686 | -41.01964 | 2026-10-08 15:39:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 48.2 |
| ea4fd13a-9955-34b8-9b9e-d1e89f6681ed | -13.96304 | -44.85117 | 2026-10-08 15:39:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 25547146-7287-347b-a0cb-3b7c2f634e81 | -14.41855 | -41.51381 | 2026-10-08 15:39:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 20.2 |
| 872cda94-fa6f-3e06-8b6b-355fa82385f8 | -16.23376 | -40.14657 | 2026-10-08 15:39:00 | NOAA-21 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| b6ab2ede-c49e-339e-a230-98c481432822 | -11.60944 | -43.63439 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 83bd18a3-90f9-32f6-b21e-ee759b197325 | -17.96123 | -42.77574 | 2026-10-08 15:39:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 55b09a82-8339-326f-b315-f4faa53f87fa | -15.56949 | -44.5299 | 2026-10-08 15:39:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 0f7b10af-a2b8-3379-978a-6d50ee8762a7 | -15.56737 | -42.90163 | 2026-10-08 15:39:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e8bb5495-6880-3883-b6aa-d6934846fca2 | -12.18856 | -44.82818 | 2026-10-08 15:39:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 0961e79c-fef0-347a-8e92-dd8d371845a0 | -12.22762 | -44.75215 | 2026-10-08 15:39:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 245048f4-91d5-30ba-a17c-7b9af2277e4c | -12.98923 | -41.00377 | 2026-10-08 15:39:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 7d568255-642d-3d14-aa21-e80ad3e5740b | -11.71697 | -43.65604 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| c2c9c966-7369-3e13-840c-c69b38878680 | -11.30158 | -44.83698 | 2026-10-08 15:39:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 37.7 |
| c25d38d1-7feb-3e53-bdde-d03972ecd13c | -14.45377 | -41.23347 | 2026-10-08 15:39:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 50ddec16-0dfb-3491-9ac8-407ce84d563e | -14.1547 | -42.10407 | 2026-10-08 15:39:00 | NOAA-21 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 031c51cb-bf33-338c-8bfe-bab670b14b48 | -15.9669 | -40.69958 | 2026-10-08 15:39:00 | NOAA-21 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 066ad854-de09-3398-a6ea-3fe808a08aad | -11.73165 | -43.50762 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 35.0 |
| d559475c-4604-3280-9b41-c3ec7d693f76 | -14.35698 | -40.47597 | 2026-10-08 15:39:00 | NOAA-21 | BOM JESUS DA SERRA | BAHIA | Brasil | 2903953 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |


[Clique aqui para ver as próximas entradas](README228.md)
