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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 290da201-97d6-3d20-88e2-f049e20f6fc2 | -16.75985 | -57.56196 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7067dcb3-a1aa-3679-9751-f7e5659815a4 | -16.75926 | -57.5656 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5afc8309-5258-31b5-a153-520b37894997 | -16.69647 | -57.44627 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 499d1c0b-3749-327b-96b4-d8c71ada175e | -16.57212 | -57.70987 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 6ee93b3b-b6b3-3190-912b-d9324bb85685 | -14.63115 | -57.94211 | 2024-10-12 05:01:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0712e90a-12b0-3b49-92af-057c89e5f105 | -14.63053 | -57.94587 | 2024-10-12 05:01:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1604db7-0311-3939-860c-a870642ab8ac | -14.95523 | -57.9164 | 2024-10-12 05:01:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7240df8-8fa4-30aa-b521-0e6a92c817c9 | -14.95184 | -57.9158 | 2024-10-12 05:01:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c2e9c73-2225-3a1f-be7c-dbabc003a381 | -14.94784 | -57.91893 | 2024-10-12 05:01:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e62cd81-2d09-3ae4-aa6e-b5d32c98da5c | -14.94445 | -57.91834 | 2024-10-12 05:01:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2eeb18f-d51c-30ad-adfd-e91483d61106 | -14.94106 | -57.91774 | 2024-10-12 05:01:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c15f455-637c-39c0-a70c-2c6d64833c6d | -14.94045 | -57.92147 | 2024-10-12 05:01:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80a9ba6e-14e9-38a5-9100-1392c1385d07 | -14.87774 | -57.98413 | 2024-10-12 05:01:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24403cc6-4545-3487-a25f-e49b23cd0106 | -13.73979 | -60.59481 | 2024-10-12 05:01:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| b9776e25-c790-31e4-9fe9-c185dab89ce5 | -13.7389 | -60.5999 | 2024-10-12 05:01:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 80c53a89-945c-3c86-b636-e4e13ee55df2 | -13.735 | -60.59919 | 2024-10-12 05:01:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| ab06160c-dbac-3396-8359-f2cb6f0d28c6 | -13.76845 | -60.56867 | 2024-10-12 05:01:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6e8679a7-0aaa-3d33-adee-fec7eb7cdf3e | -13.76551 | -60.56521 | 2024-10-12 05:01:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5d6a2a2b-0a53-3758-bd5f-0cc49ff22bbc | -13.76455 | -60.56796 | 2024-10-12 05:01:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c0a18c37-eae0-3d6e-a3a5-de19038bd5ec | -13.7559 | -60.57389 | 2024-10-12 05:01:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 364c0ef0-db27-30e7-ae9e-94967d729115 | -13.75501 | -60.57666 | 2024-10-12 05:01:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f1b459da-f74a-3102-aaef-4d6967aa20cb | -13.74545 | -60.58539 | 2024-10-12 05:01:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2a374959-13fd-3eca-b461-db559ac13ed5 | -13.74369 | -60.59553 | 2024-10-12 05:01:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7f557323-2fd6-3f2f-964f-0b25f8571f37 | -13.74281 | -60.60062 | 2024-10-12 05:01:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b5cfa33d-df58-3539-bc26-f587bf2452fd | -15.63033 | -59.96375 | 2024-10-12 05:01:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2360069b-1f39-37ca-96db-fe42e2da015f | -15.62667 | -59.96309 | 2024-10-12 05:01:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42aa512a-204f-3f13-9297-51c17831658f | -15.62432 | -59.97645 | 2024-10-12 05:01:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11813bbb-04fb-33e4-b35a-85cb5bdaeb67 | -15.623 | -59.96241 | 2024-10-12 05:01:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cbc3dd4b-6637-33aa-a7c1-19ce2e3ae48a | -15.62222 | -59.96688 | 2024-10-12 05:01:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 99a2791e-e74d-3461-9fa2-5121b2bcef89 | -13.73411 | -60.60429 | 2024-10-12 05:01:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 9b499c49-092c-3553-b5f8-dedaf78f4db6 | -13.72789 | -60.63998 | 2024-10-12 05:01:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2ce639b2-4908-34f7-a305-87b9534c35d3 | -17.98763 | -57.37857 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 454463e2-ff37-358c-bceb-59f3273f2fd8 | -17.98604 | -57.36712 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 7b4830e3-ff81-3f97-baf1-945e62c0578c | -17.98432 | -57.37799 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 51fe4fac-8072-3eac-9877-6a8155f23e71 | -17.98273 | -57.36655 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 279abf03-b05d-322e-ae11-661a82d7ce25 | -17.98158 | -57.37379 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 7c4b79f6-349a-38c1-88f9-bc2f395b071d | -17.97439 | -57.37627 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| a31794c1-d6b3-3250-996d-20cce20cc724 | -17.97381 | -57.37989 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 938f9efe-a30f-35d0-8404-7930010be974 | -17.97165 | -57.37207 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.1 |
| f25f7bc7-7659-3112-aab5-e3f08323028d | -17.97108 | -57.37569 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| b91c4469-4f4f-308e-a38c-2ecdcc99f529 | -17.9705 | -57.37932 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 37f2175d-2b99-321b-a989-1eefe4b53773 | -17.96834 | -57.37149 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.1 |
| 784b0d3f-4027-3de5-abc4-aa69deb5c441 | -17.96776 | -57.37512 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 7d36dfa9-56b9-3cd3-a530-047322aaa1ee | -17.96719 | -57.37874 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 389d4cc1-ca2d-3ded-89f5-490b8b50ce9b | -17.96661 | -57.38237 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b6f08969-d1aa-3346-9a72-ae4a12c73dfe | -17.89721 | -57.326 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 191ce47a-8ff8-379d-a702-0b0f0ec327c6 | -17.89663 | -57.32962 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 8e051a41-8f86-3a46-a7d3-c52e6c8bb31e | -17.89605 | -57.33324 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.9 |
| 9411f653-29c4-3bf7-a0b4-07e0f455ed36 | -17.89505 | -57.31819 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.7 |
| f174cfc1-74e8-391f-a30b-6849b7257f99 | -17.73984 | -56.24648 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 62edef77-e7ab-3252-83a8-77720488ed00 | -17.6414 | -56.31164 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 131d9563-7cda-3dce-9b5d-1492c62446f6 | -17.63586 | -56.32556 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| a83e5db3-be39-3be4-bbf8-7f21d11ddb83 | -17.64249 | -56.32667 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| d47db711-e713-3760-a38e-4476c2e9a13a | -17.64085 | -56.31526 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 3ed93bd0-aa56-3d94-b105-6aa3baa32c5b | -17.64029 | -56.31887 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1f46b6c8-4ec9-3915-bc29-ea8224e7eb9a | -17.63918 | -56.32611 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| b1c7d1e1-8029-301b-aa14-90d71ee89e52 | -17.63862 | -56.32973 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 7ff6496d-9012-3031-bd08-45c497ed577e | -17.73153 | -56.25624 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 779f912a-863a-3daf-853a-622523b2bdf1 | -17.71276 | -56.24566 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 49ebd9e7-8a32-37e9-881f-1c6bcd2dd4bf | -17.71056 | -56.23785 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| cf125cf6-13c4-360f-9326-64f611208c58 | -17.70665 | -56.26323 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f99a26b3-909f-35fc-b085-975b70f718ad | -17.70613 | -56.24455 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 2bfc96b5-90b1-3524-ad76-ab4647149303 | -18.22718 | -56.52456 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 3f299fe3-7738-3c29-9130-8e3a774b9354 | -18.22556 | -56.51311 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 56643d78-706c-39d0-96e7-dab75b4628f3 | -18.22337 | -56.50529 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 22f7dd8c-5048-3740-b893-5d4599e6021e | -17.84378 | -57.38373 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| fec99b71-7885-308e-9f71-a32991b4b43f | -17.84294 | -57.34636 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 49004d12-6834-38b8-a903-6a4482cdc9a0 | -17.84237 | -57.34998 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| d2f9b185-5646-3954-8868-d1f3b40a8986 | -17.84163 | -57.3759 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.7 |
| 11cffd5a-6dab-3a58-9ab3-39da139067bf | -17.84121 | -57.35722 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 33bc2378-a44c-37ca-8a1b-e7bea498939a | -17.84105 | -57.37953 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.7 |
| 1d925090-405a-37a2-b0eb-f63af10dc0fb | -17.84063 | -57.36084 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.7 |
| 339abcdf-ea56-3a13-a8bd-50fd59f7f75c | -15.69177 | -52.50193 | 2024-10-12 05:01:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff6c2103-165f-3b95-8b9b-6a9390f99522 | -15.68955 | -52.5037 | 2024-10-12 05:01:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7653d771-8ec0-3e26-b84b-b568cf7bcd4a | -15.68805 | -52.50138 | 2024-10-12 05:01:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ddf935c-1f06-3618-bbc3-7d0a9a677fbf | -15.68584 | -52.50314 | 2024-10-12 05:01:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a7841b6-1498-386a-a5ad-a64dd5a8af1c | -15.68434 | -52.50081 | 2024-10-12 05:01:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a7d8acc-b723-3c1d-b901-0d8312b4bfbf | -2.807 | -51.3406 | 2024-10-12 05:05:21 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| da611b2a-eab8-318a-a649-418b1b9c0fa2 | -2.7701 | -51.3622 | 2024-10-12 05:05:21 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 44cdcf9d-09ee-3aae-905a-1b5f726d5020 | -2.7885 | -51.3618 | 2024-10-12 05:05:21 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| adccd9a0-71c5-35f2-9fc7-2cab50645b65 | -2.8254 | -51.3401 | 2024-10-12 05:05:21 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 3d231a2e-d232-378f-90fc-fb2268b1fd73 | -2.8255 | -51.3194 | 2024-10-12 05:05:21 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| d887a5f1-3f92-34fe-ae0c-a373dc15e340 | -3.1611 | -50.3508 | 2024-10-12 05:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| de7a4957-8317-3959-849b-5b2875fefedf | -3.161 | -50.3718 | 2024-10-12 05:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| e8f62e45-9013-367e-8e1a-ab30075b8646 | -3.1427 | -50.3514 | 2024-10-12 05:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| afef4a40-2372-3c37-a9c3-e74f8fca73b5 | -3.1426 | -50.3724 | 2024-10-12 05:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 41f12863-d514-34d6-9bcc-cdf763ecc066 | -6.747 | -59.3259 | 2024-10-12 05:05:44 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 7f2e6300-205b-355e-86e7-a3381bacb41c | -3.21473 | -46.77893 | 2024-10-12 05:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ec45eb76-54fd-30b1-aff8-d8e343f9bea1 | -3.21385 | -46.78506 | 2024-10-12 05:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 63bf4cbf-8efb-384c-824c-eb4fe010d9ed | -3.21374 | -46.7761 | 2024-10-12 05:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e510109b-7b6a-31d3-adfc-cc6607e76477 | -3.21281 | -46.78226 | 2024-10-12 05:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| efe3f283-c950-3085-b4ae-0472d838d0e3 | -2.61339 | -47.34349 | 2024-10-12 05:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 541bb43d-1976-3049-8f5e-a6dd4cec287f | -2.61175 | -47.3419 | 2024-10-12 05:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4da091d0-52f7-3260-8fdb-8c54b2ab22ec | -2.61096 | -47.34732 | 2024-10-12 05:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8b6b559c-3e70-359c-9c1d-e56656fe22be | -2.60685 | -47.34248 | 2024-10-12 05:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9304b1a-accd-3cd5-b4b8-bd5081a55ba5 | -3.93781 | -46.43451 | 2024-10-12 05:21:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f97a3f80-a045-3a4f-867f-d847cb859df1 | -1.62077 | -48.02673 | 2024-10-12 05:21:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c66a8cf-1d74-3a5b-be8d-49bcf2d788c6 | -3.45839 | -47.65667 | 2024-10-12 05:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e67b5295-e0c6-3416-b299-c897587ed154 | -3.45755 | -47.66242 | 2024-10-12 05:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 486200c9-6e77-325e-90fe-a60bbbeeb3e1 | -3.7047 | -47.92115 | 2024-10-12 05:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README96.md)
