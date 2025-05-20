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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62564fb7-22b4-3dfa-ba69-2ecfbde6c067 | -13.36753 | -54.25471 | 2025-05-20 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce879f8c-7c81-33e2-b9a9-f68219c583c4 | -14.04604 | -45.51645 | 2025-05-20 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe1fd173-6927-3735-833e-51326b6c1f9d | -14.02255 | -55.14108 | 2025-05-20 05:01:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aed0f66a-6d45-3237-9be6-c02fd1f80bcd | -19.16254 | -47.81754 | 2025-05-20 05:01:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8f88781-93fb-3134-bbca-37b84d349b53 | -14.02535 | -55.12298 | 2025-05-20 05:01:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bb2273b1-dca8-3c7f-b1ee-315442931a2d | -12.68593 | -58.12944 | 2025-05-20 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 51be5a3a-a7cb-3669-9e10-56118c5c5a90 | -20.22203 | -50.756 | 2025-05-20 05:01:00 | NPP-375D | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 979e186f-a98c-35fd-88fe-b84d11839c75 | -12.46565 | -57.18768 | 2025-05-20 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c9f5261-7154-3e3a-96b1-fd5f561df72a | -19.11284 | -52.69097 | 2025-05-20 05:01:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d247bf49-7d03-3d6f-837e-00a891cc3e06 | -19.05803 | -53.4593 | 2025-05-20 05:01:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0eba4d4-328b-30cf-a521-8c3ae9f25934 | -14.01641 | -55.13637 | 2025-05-20 05:01:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2225341-4475-3bfc-b5b2-ece7cf3b9c9a | -15.27328 | -43.07442 | 2025-05-20 05:01:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 1b835381-dce5-3306-9d87-2d73188f60e3 | -12.27808 | -57.26764 | 2025-05-20 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e1176c4a-424d-3275-a796-7cd0977f3c10 | -19.16015 | -47.81656 | 2025-05-20 05:01:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 49d4c4fd-d7cf-3d31-bf96-437f92271df6 | -16.40027 | -58.16745 | 2025-05-20 05:01:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 88bf298c-3a53-32c7-8d01-22237a4bf6f0 | -14.05215 | -45.51534 | 2025-05-20 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 153d4e4b-159a-30b5-889e-929399a4f339 | -13.61539 | -55.45442 | 2025-05-20 05:01:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2872850-98cc-3da6-85c5-c5a3c62a5ae0 | -14.02032 | -55.13329 | 2025-05-20 05:01:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82119dd0-f2cc-3efc-ab98-8eca64a8d9ef | -12.27406 | -57.27079 | 2025-05-20 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 99c31eb0-1772-3289-acb7-8565c9b5353e | -13.48697 | -60.37909 | 2025-05-20 05:01:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 401dc211-f8f3-3485-8c79-9551268158d0 | -14.03667 | -55.12814 | 2025-05-20 05:01:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9d6c7d8-1023-3ec9-bceb-23fab3a67e4d | -13.09384 | -52.28366 | 2025-05-20 05:01:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16a4715c-b9a1-38f2-83c9-b3b966682a34 | -13.71424 | -57.47925 | 2025-05-20 05:01:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99cd1f12-1622-320d-b590-47628ae3e077 | -20.95425 | -56.60921 | 2025-05-20 05:04:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3802e053-a0b7-3dcc-98d4-e12bc4139a74 | -21.46441 | -56.29957 | 2025-05-20 05:04:00 | NPP-375D | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a8cdf2af-e76b-361e-a321-90705d9775a1 | -20.95146 | -56.60482 | 2025-05-20 05:04:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9994dfe9-625d-3cd0-982c-ae6a00fa7c83 | -20.95032 | -56.6124 | 2025-05-20 05:04:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee95995a-928f-392d-aa6e-b26d60b2e033 | -20.95761 | -56.60979 | 2025-05-20 05:04:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c4d97568-cd3a-3488-8324-9b599e622ea1 | -20.94753 | -56.60803 | 2025-05-20 05:04:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e49c03af-b8bf-38ab-b719-8e286e9bb629 | -20.18069 | -55.00628 | 2025-05-20 05:04:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6d646939-a123-326b-be06-b6bc48b78bfe | -20.1842 | -55.00684 | 2025-05-20 05:04:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6b6adc24-316a-33c7-ad15-4e53cf82654d | -23.60821 | -49.01222 | 2025-05-20 05:04:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71089cb4-3c4f-364a-a8fa-be6c1c905b2a | -20.95819 | -56.60598 | 2025-05-20 05:04:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 533f4366-3ba9-371d-b20c-f2a02196167c | -23.60851 | -49.00898 | 2025-05-20 05:04:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9a678e3-20e9-3c9a-9207-693c3e6145b7 | -22.21445 | -56.20099 | 2025-05-20 05:04:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a5400e7-a300-3761-ab45-bbb97cd2b312 | -20.9481 | -56.60424 | 2025-05-20 05:04:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4671032c-0248-3850-8e16-e9efca5b8d98 | -20.95368 | -56.61299 | 2025-05-20 05:04:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a74902a-7128-3394-bbec-417e3f85a667 | -21.783 | -52.74075 | 2025-05-20 05:04:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f87ceed-ced1-311c-895e-8ddea96e3dd9 | -20.95089 | -56.60862 | 2025-05-20 05:04:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d292f389-4827-3d13-8e12-40fd14a85417 | -21.221 | -48.6107 | 2025-05-20 05:04:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e4f67c53-ed2e-360c-bca6-36bd025697b5 | -20.94695 | -56.61182 | 2025-05-20 05:04:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b393fab-6323-356d-aa45-dae4dcd58e71 | -20.3867 | -55.39251 | 2025-05-20 05:04:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 74729788-ae80-3c48-afc7-e6a592bdea0a | -20.17719 | -55.0057 | 2025-05-20 05:04:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 220a39f4-eabc-3253-a712-37a52dc0321c | -21.22133 | -48.60748 | 2025-05-20 05:04:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 90333815-5a41-3c33-8ae2-1ebe263e9e65 | -20.95483 | -56.60541 | 2025-05-20 05:04:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 434e5d3d-0703-3633-90b2-e77849686e38 | -21.78159 | -52.74043 | 2025-05-20 05:04:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d453291a-5662-362f-b574-18061a52ec2c | -20.47966 | -55.83847 | 2025-05-20 05:04:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| db411f50-57cb-3ef0-94f6-fadb10a070fa | -21.21582 | -48.61003 | 2025-05-20 05:04:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| db1a1fc0-4ff3-30a4-98b2-d39d197b5f80 | -2.95409 | -60.01367 | 2025-05-20 05:21:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa5cd70e-f7e8-3815-9b75-be5a244ae93a | -6.22951 | -43.34975 | 2025-05-20 05:23:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 35.7 |
| b7e7a5b1-c0df-3bcc-b311-aa8afec354a5 | -6.2281 | -43.35902 | 2025-05-20 05:23:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 8e1c2c2f-ad30-3056-9f34-9c195166c2f1 | -5.97354 | -43.75487 | 2025-05-20 05:23:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| dd144cd3-7667-3eca-a2de-0f0893026971 | -5.97206 | -43.76451 | 2025-05-20 05:23:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| fe36ad3e-eb56-3e57-a4d8-1122331ed8cd | -6.23091 | -43.34054 | 2025-05-20 05:23:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8b53ddb9-8ec1-3b28-97a1-79377b4be37d | -6.23713 | -43.36042 | 2025-05-20 05:23:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 15cc7340-e3c5-348d-a237-e80af6e18136 | -6.20382 | -43.33649 | 2025-05-20 05:23:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ba5e618f-5d33-31c4-a187-736911cff145 | -6.5518 | -44.48602 | 2025-05-20 05:23:00 | AQUA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cf71f760-1e63-3fce-b72e-97530459ef86 | -6.20526 | -43.32716 | 2025-05-20 05:23:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| f56b8f9b-60f3-3595-a7ee-26acdef1aebb | -11.51369 | -48.58571 | 2025-05-20 05:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c005f26-1b66-349a-9ebf-ea43862a0da3 | -9.41503 | -58.32545 | 2025-05-20 05:23:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8aed49ad-c4b3-394f-a656-8181b104fe13 | -8.75136 | -49.75772 | 2025-05-20 05:23:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb3e7dba-9d43-399c-94f7-2bc52f0408fc | -7.89255 | -61.47544 | 2025-05-20 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a6941449-9115-3aac-a09a-2b08f3b0c324 | -11.51435 | -48.57973 | 2025-05-20 05:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31dc08ea-88dc-3bde-acab-1a937600e388 | -11.23423 | -49.49783 | 2025-05-20 05:23:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c397f82b-d93e-3934-a136-6b0640610ab4 | -19.05755 | -53.45942 | 2025-05-20 05:23:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 688087c6-3f17-37fc-833d-6be251790e69 | -11.66391 | -54.94338 | 2025-05-20 05:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0af02e4f-566f-37e3-a541-5c61a7ce57d2 | -9.65209 | -67.23437 | 2025-05-20 05:23:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4abade99-9cd3-3b00-94cd-65fa09080375 | -11.08753 | -54.77919 | 2025-05-20 05:23:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 532f74e0-f7e4-32ec-b592-1cdbf1848d30 | -11.01027 | -50.75679 | 2025-05-20 05:23:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 651f431e-ab32-370d-8e7a-ddb944628eda | -5.14531 | -60.37674 | 2025-05-20 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f15bf0c-ea8d-3de2-99de-2dba55be5f10 | -11.90507 | -58.24255 | 2025-05-20 05:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbce952b-c9be-3eb1-963f-111ba3357a50 | -12.34076 | -49.97606 | 2025-05-20 05:23:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b85e17d-6770-374a-bac7-035eff0f6c29 | -10.69669 | -59.10947 | 2025-05-20 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 83184afa-478a-3ed0-a2a5-469c8623dac6 | -10.35784 | -47.97669 | 2025-05-20 05:23:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7c2b1316-3c04-3d3d-a96b-b47bdb960d36 | -11.36245 | -55.12348 | 2025-05-20 05:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eeaef93f-5dcb-3f9b-9d49-a73c65bcc44c | -10.07769 | -55.49311 | 2025-05-20 05:23:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7e75200-cae7-3aea-8766-f745c4308bb2 | -11.36213 | -55.11687 | 2025-05-20 05:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b72dafc-9e6a-3b49-9735-6f5e4123d53d | -10.55053 | -55.62439 | 2025-05-20 05:23:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b603ea68-6952-3302-b4bb-214e48e545ae | -12.27326 | -57.26939 | 2025-05-20 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 699760f6-bebd-344d-979c-5eb2dd53228e | -10.36477 | -47.97786 | 2025-05-20 05:23:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6ee77900-a180-37b4-af63-d28a0586e1f3 | -11.23483 | -49.49256 | 2025-05-20 05:23:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af6cbbbf-8ce2-3c75-9d05-1aa678d0c38a | -9.41147 | -58.32492 | 2025-05-20 05:23:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8cc3d4e-cd53-384d-88b7-3cb8bf608b53 | -11.35096 | -55.10838 | 2025-05-20 05:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98c23e25-7ac1-31fa-9d0a-54a8f34fc347 | -12.28817 | -52.47596 | 2025-05-20 05:23:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0007d7ad-8a8a-3055-8404-7a0d60552afc | -11.08468 | -54.77693 | 2025-05-20 05:23:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 922f2f4f-9664-36ff-a6eb-c41c104eb617 | -11.36155 | -55.1213 | 2025-05-20 05:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fd302ee1-33cd-3f89-a278-2f1dbbc9a926 | -9.89587 | -65.10129 | 2025-05-20 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da3f3c6c-e694-395a-8bb0-030e7201969b | -9.41383 | -58.3336 | 2025-05-20 05:23:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60c305c1-951c-3a18-9f7e-32c56666d07c | -10.81692 | -56.9631 | 2025-05-20 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| acdf10a8-83d6-343e-8466-325ce006cf76 | -10.07344 | -55.49253 | 2025-05-20 05:23:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d00b9c11-5219-311a-ab3a-c3425fa151a5 | -10.68458 | -57.58968 | 2025-05-20 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5656777-022e-36de-98dc-e1c4b84cb19c | -12.08455 | -54.58278 | 2025-05-20 05:23:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9b686d78-fd6a-3df1-9ecc-5060176cbbc9 | -12.27717 | -57.26997 | 2025-05-20 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6d164650-520b-3320-aa33-ce73275c048a | -10.05178 | -65.00227 | 2025-05-20 05:23:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 812c728b-0785-34bc-89c4-ae41afaafc62 | -7.3138 | -46.96208 | 2025-05-20 05:23:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e3df630-40c1-3392-bc3d-127ee851f654 | -12.03973 | -54.96647 | 2025-05-20 05:23:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 085ea966-d699-3370-8f8b-96e40e50e83b | -12.08198 | -54.5805 | 2025-05-20 05:23:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09dac352-98a8-3b7a-b389-4f83e1a759e0 | -12.08664 | -54.58115 | 2025-05-20 05:23:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 930d6d50-20d9-306c-b7d5-729fc32a82d3 | -8.74585 | -49.75225 | 2025-05-20 05:23:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fb631e35-aada-39c9-9b19-76d5981d498b | -5.14916 | -60.37381 | 2025-05-20 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README13.md)
