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
| 5f6be04f-8597-34ca-b27d-7d0caf44835c | -19.6562 | -47.5886 | 2026-07-09 13:50:00 | GOES-19 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 37a85da3-7bdf-3403-a583-2addb48c1801 | -8.6923 | -54.5468 | 2026-07-09 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 73e70bd6-9b10-305c-8a6e-8e65e3aa503b | -17.5896 | -54.0524 | 2026-07-09 13:50:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 125.1 |
| bc873010-1b71-3422-ab45-8da2e09473d1 | -8.711 | -54.5455 | 2026-07-09 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 17aaac4d-d195-372c-bd99-c4ca05592620 | -13.2829 | -45.1543 | 2026-07-09 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 559.6 |
| d1e936e9-5ae5-3a43-bb51-26d8b78f285e | -17.5509 | -54.0157 | 2026-07-09 13:50:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 77.5 |
| e6e8773a-ee97-3061-869e-056705b8b5ac | -11.6664 | -46.362 | 2026-07-09 14:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 194.4 |
| 4ce1fb78-3ff2-357f-aee1-f27d62fa8c25 | -17.5896 | -54.0524 | 2026-07-09 14:00:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 112.0 |
| f0358fd0-e555-335b-8a4a-23c57931ca59 | -17.1209 | -49.9942 | 2026-07-09 14:00:00 | GOES-19 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 87.9 |
| dbc6b617-0c91-36e5-b99f-d4dca6e5e582 | -21.7617 | -56.301 | 2026-07-09 14:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 73.7 |
| d44546d6-8218-3536-92f5-ab5f886884f1 | -13.2978 | -54.3241 | 2026-07-09 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 1987f8d4-f69b-3b38-9a88-896bec019119 | -17.5509 | -54.0157 | 2026-07-09 14:00:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 0f295e7c-9955-3e68-8987-a7d1ad9d479c | -8.6923 | -54.5468 | 2026-07-09 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| e8784d3d-0d78-3d3c-b331-316c2a9f5bc6 | -8.711 | -54.5455 | 2026-07-09 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 804478b8-e9c1-3257-bd19-d3521c38d9a9 | -19.6562 | -47.5886 | 2026-07-09 14:00:00 | GOES-19 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 6a8c1e93-0af4-3b6e-91b7-3d79c8337517 | -11.666 | -46.3846 | 2026-07-09 14:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 122.5 |
| a2d6a879-65b7-3ad0-bdd4-874b2e0e75ba | -11.666 | -46.3846 | 2026-07-09 14:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 522ae4e2-2e5d-3bca-a8ae-85f9a7488d30 | -11.6664 | -46.362 | 2026-07-09 14:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 8bb33c4b-d1fb-3f96-9e2e-374aeb756687 | -19.6562 | -47.5886 | 2026-07-09 14:10:00 | GOES-19 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 77412b08-2de4-3d29-897c-66064c44f34a | -21.7617 | -56.301 | 2026-07-09 14:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 2ad34154-bd16-34a6-ae11-a1b6e693f7a7 | -21.7823 | -56.2976 | 2026-07-09 14:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 039d8f6a-a760-3f4f-817f-f4aaad19906f | -19.6555 | -47.6119 | 2026-07-09 14:10:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 8219e461-f9bf-369a-930c-261ce1a14992 | -8.711 | -54.5455 | 2026-07-09 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| c8ebb4dc-d177-3cac-acd0-66daed43b051 | -8.6923 | -54.5468 | 2026-07-09 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 19b13447-caf0-37c9-b609-334c9f266d7e | -17.1209 | -49.9942 | 2026-07-09 14:10:00 | GOES-19 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 93.1 |
| af9c5557-60bf-3369-ab63-fcc18f2c3aa8 | -8.711 | -54.5455 | 2026-07-09 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 8c2fb5b5-1131-37f8-8f17-1a0123d9a3be | -21.7617 | -56.301 | 2026-07-09 14:20:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 0b5f23a3-324f-37a3-9670-fc35d64f59c2 | -13.2975 | -54.3448 | 2026-07-09 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 120.0 |
| 331ce92e-cec9-39dc-84f5-19eff9310ed2 | -8.5225 | -54.7604 | 2026-07-09 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| ee029841-2ed3-30d4-8601-c88ad78f8f65 | -8.6923 | -54.5468 | 2026-07-09 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| e95a6848-e95e-3052-9c71-efc2c073f146 | -9.0095 | -40.9926 | 2026-07-09 14:20:00 | GOES-19 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 75.9 |
| e4d9cfc2-085a-3059-8f03-c0f727649a5d | -8.6923 | -54.5468 | 2026-07-09 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 2ef26c3b-b6ec-38d8-b1ae-53b73d4eb7df | -17.5699 | -54.0553 | 2026-07-09 14:30:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 74.1 |
| ba288559-4b92-3e77-8960-ea68fa8a56ec | -13.2635 | -45.1575 | 2026-07-09 14:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 343.1 |
| a825cd44-b625-3185-a1d5-1f7a63866600 | -8.711 | -54.5455 | 2026-07-09 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| db2d8e27-42d4-3093-a66b-e5b3583118e3 | -17.5896 | -54.0524 | 2026-07-09 14:30:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 92.4 |
| f8aaa15e-8b75-3355-9647-e952a856905f | -21.7617 | -56.301 | 2026-07-09 14:30:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 283e622b-72a7-3bb1-a46e-ddaa4e10439f | -21.7617 | -56.301 | 2026-07-09 14:40:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 0b465777-c470-344c-a6dc-0e046f32f2ae | -17.5896 | -54.0524 | 2026-07-09 14:40:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 96.0 |
| d706e65e-7761-3048-863a-3298f8e722dc | -9.0095 | -40.9926 | 2026-07-09 14:40:00 | GOES-19 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 79.8 |
| efa4c7b3-e6e4-3a77-8df5-904687ded9a2 | -13.2635 | -45.1575 | 2026-07-09 14:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 297.4 |
| 45cb8f63-c9d2-3e99-9775-1d2bfc17bc13 | -19.6562 | -47.5886 | 2026-07-09 14:40:00 | GOES-19 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 9c69b3c5-42f4-301f-9d07-96aca0a8c04d | -8.6925 | -54.5266 | 2026-07-09 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| cc44f829-1b9c-3fc6-9b36-d2d3278bf32d | -8.6923 | -54.5468 | 2026-07-09 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| c7796dc2-6ac9-39fa-bd78-d0c655cd554d | -21.7823 | -56.2976 | 2026-07-09 14:40:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 73.6 |
| cc5b434b-6f28-38e1-9dfb-e52ea5dab2bb | -8.711 | -54.5455 | 2026-07-09 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 7acf5206-3a3f-30fe-a3ff-16267c8e58a7 | -21.7617 | -56.301 | 2026-07-09 14:50:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 102.4 |
| ec59389e-3ad2-39e9-b215-5d7a4b0f6afb | -17.5896 | -54.0524 | 2026-07-09 14:50:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 73.6 |
| e183df1c-15dc-38f2-bad8-d154ae10789b | -13.2975 | -54.3448 | 2026-07-09 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 117.6 |
| e4e50493-1808-3aa4-a9e9-98e83f3fef44 | -8.711 | -54.5455 | 2026-07-09 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 35080fef-7d52-36d0-a505-6c597802af97 | -8.6923 | -54.5468 | 2026-07-09 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| bde71f13-8b28-3a05-b5e3-50563a1f356d | -13.2635 | -45.1575 | 2026-07-09 14:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 337.6 |
| 7a3612a9-5499-3c23-89ae-dcfb58122f56 | -21.7823 | -56.2976 | 2026-07-09 14:50:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 7c83f275-bb7d-37f7-a0b3-61996d1d651d | -17.5699 | -54.0553 | 2026-07-09 14:50:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 72.3 |
| fa01f6d4-3a46-3451-8df0-528d0fddcc7d | -21.7823 | -56.2976 | 2026-07-09 15:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 81023b1c-fa55-3a8e-88cb-363c4e1b340d | -8.711 | -54.5455 | 2026-07-09 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 11eff2db-580a-3afe-b08e-789f45e9b9dd | -13.2978 | -54.3241 | 2026-07-09 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 91.9 |
| fc5e5158-8a8e-32e0-ab90-9c7e7dc6ac0c | -9.3811 | -48.2138 | 2026-07-09 15:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| f474cf67-39cf-30f7-879e-a15a98c68344 | -13.2635 | -45.1575 | 2026-07-09 15:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 200.2 |
| ed79e019-faa9-3b4b-8759-70c914d00231 | -10.3382 | -50.0405 | 2026-07-09 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 6f35ea05-889c-3958-9dd0-a4a5698f5f45 | -6.9326 | -43.7032 | 2026-07-09 15:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 82505d2a-2ac9-365c-b466-1343ddcff640 | -6.9138 | -43.7049 | 2026-07-09 15:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 1086c609-a235-3a1b-b08b-0e093171ecc9 | -21.7617 | -56.301 | 2026-07-09 15:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 97.9 |
| dfd5fefb-aa53-3303-98b9-44c7387ba974 | -13.2975 | -54.3448 | 2026-07-09 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 119.4 |
| 261de35d-58ab-3cc4-8c5c-81734524f834 | -8.6923 | -54.5468 | 2026-07-09 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 0e862b04-520a-3630-93ce-806755268670 | -17.5896 | -54.0524 | 2026-07-09 15:10:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 67.4 |
| f1d6b498-b097-3def-8d2c-45af319c6555 | -21.7617 | -56.301 | 2026-07-09 15:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 115.7 |
| fab7052a-37ee-33b6-a4b3-c2da776d9745 | -21.7823 | -56.2976 | 2026-07-09 15:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 13f11ea1-3d9b-3687-9681-3fea1e2eba74 | -8.711 | -54.5455 | 2026-07-09 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 129b2f24-26ec-319a-bb32-c2e78524cc4c | -13.2975 | -54.3448 | 2026-07-09 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 172.3 |
| 0d9347f3-7c68-3b31-a8f1-3948e7bcba96 | -13.2978 | -54.3241 | 2026-07-09 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 72b587cf-f9e0-36ae-9f41-897db5ab12ee | -13.2635 | -45.1575 | 2026-07-09 15:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 231.7 |
| ec1a4b48-1b60-3fa6-a819-e4b36918cc1c | -8.6923 | -54.5468 | 2026-07-09 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| e33a0d12-14c4-3962-a654-9c0607269d77 | -6.9138 | -43.7049 | 2026-07-09 15:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 39c2fb35-897e-3da4-a3e8-905b91222eaf | -10.3382 | -50.0405 | 2026-07-09 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 96d9ddb3-b682-32f9-b3a3-b7b6e8291257 | -19.6562 | -47.5886 | 2026-07-09 15:20:00 | GOES-19 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 112.2 |
| c60a5f29-b0a7-3d8f-9830-7d123742cf4e | -13.2978 | -54.3241 | 2026-07-09 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 101.6 |
| a5dfea12-b55c-340d-9dd4-8969bca22f80 | -8.711 | -54.5455 | 2026-07-09 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| f65daa5a-bbcf-3350-8566-1802d5e14b9d | -13.2635 | -45.1575 | 2026-07-09 15:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 193.5 |
| b7048f2f-09ed-3372-928c-fff15c661f4c | -10.3382 | -50.0405 | 2026-07-09 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 880d3d07-e371-307e-a230-324cdb0cbd26 | -8.1096 | -47.6132 | 2026-07-09 15:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 1fdd63b9-d421-386d-ac2e-675a9928eec0 | -8.6923 | -54.5468 | 2026-07-09 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 6eb4c09d-1ded-3045-aa27-9ba9e48f1740 | -21.7617 | -56.301 | 2026-07-09 15:20:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 149.1 |
| 1c78416e-82ce-3db3-a3ba-756bbd58f93d | -13.2975 | -54.3448 | 2026-07-09 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 153.7 |
| 5442d6c6-cb45-3082-9d6d-974d8fc86e8f | -21.7823 | -56.2976 | 2026-07-09 15:20:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 7e42af1f-bc85-3d11-9f7d-3c4e9413083f | -19.6555 | -47.6119 | 2026-07-09 15:20:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 88.9 |
| abcbbc76-8e87-3349-97f2-f8fc39dc9214 | -19.6562 | -47.5886 | 2026-07-09 15:30:00 | GOES-19 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 9d7dd12d-e600-37fc-af1a-d37eec46148d | -13.2978 | -54.3241 | 2026-07-09 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 125.8 |
| 1c83e398-0444-3dc4-be3f-6754005d6cd1 | -19.6365 | -47.5698 | 2026-07-09 15:30:00 | GOES-19 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 79.8 |
| a8f0fcb3-3d8d-31c2-b74c-9aac115de985 | -13.2635 | -45.1575 | 2026-07-09 15:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 2df81bd1-4c19-3261-b8b9-43ea2b21a4df | -13.2975 | -54.3448 | 2026-07-09 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 189.4 |
| c7e31675-2bc5-327a-b73a-8f0043d07c70 | -21.7823 | -56.2976 | 2026-07-09 15:30:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 4239449f-262d-38a9-bee9-48c2b7377455 | -21.7617 | -56.301 | 2026-07-09 15:30:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 795fa2b8-0cc5-38ea-b19d-2eec1b341dc5 | -5.5909 | -42.6929 | 2026-07-09 15:30:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 179.4 |
| 1efe6bfc-57fd-33b1-a0a1-8ccb12bc14ed | -8.711 | -54.5455 | 2026-07-09 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| e198f8ff-c298-3ebf-a9c9-079c5afe8b8d | -10.3382 | -50.0405 | 2026-07-09 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| ab295d5b-76a6-3584-afb7-17424dce9303 | -8.6925 | -54.5266 | 2026-07-09 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 9cae8335-c1ad-3417-8fe6-5180b1acc461 | -8.6923 | -54.5468 | 2026-07-09 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 4d3c997d-e912-3a66-9802-2aa62641ee00 | -19.6562 | -47.5886 | 2026-07-09 15:40:00 | GOES-19 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 94.3 |
| c2e45ca0-9be1-3222-b9b8-0d18d59d68f8 | -19.6365 | -47.5698 | 2026-07-09 15:40:00 | GOES-19 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 119.7 |


[Clique aqui para ver as próximas entradas](README15.md)
