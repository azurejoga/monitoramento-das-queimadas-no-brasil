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

## Dados Diários - Página 200

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 41f32a97-ed20-3987-9a9d-b6d2ee59c4e9 | -22.3929 | -49.2727 | 2024-10-02 07:57:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 78.4 |
| fafd32f5-00e2-37ba-b4a3-c57b581ca601 | -22.3713 | -49.3011 | 2024-10-02 07:57:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 134.4 |
| 28571b5f-e950-370a-ad53-ce279edaa1ce | -22.372 | -49.2777 | 2024-10-02 07:57:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 96.5 |
| 3af38237-dcc5-34bf-acaf-d4ee4494e776 | -22.3922 | -49.2961 | 2024-10-02 07:57:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 121.5 |
| caecaaff-fb04-3e6c-8b3e-217bc71fef1b | -11.9293 | -50.164 | 2024-10-02 08:06:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 0ba7cace-1925-3514-89b6-50cdd8030295 | -12.6484 | -63.1214 | 2024-10-02 08:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 4b7b8fe2-b6d9-3a74-b586-c7a6c21a240a | -13.5572 | -51.1846 | 2024-10-02 08:06:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 31bdefc3-e32d-3841-b9a0-7d08d36b2e98 | -15.9003 | -50.1537 | 2024-10-02 08:06:35 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 62857e35-8de0-38f3-bafc-aa52d0bcac12 | -16.5778 | -58.2386 | 2024-10-02 08:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 118.6 |
| a6960393-0da0-3d2b-94ca-74bb994317dd | -16.578 | -58.2183 | 2024-10-02 08:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.5 |
| eab7c103-82f4-3b66-9065-fb8b74b950cc | -16.5973 | -58.2365 | 2024-10-02 08:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 413.3 |
| f58fb2d2-1d92-376f-93b3-59d977485a87 | -16.5976 | -58.2162 | 2024-10-02 08:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 326.2 |
| 57becce5-9ec6-30ca-a69d-a84c1fb5e891 | -16.6124 | -57.2375 | 2024-10-02 08:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.6 |
| 04744bd8-b3ed-3614-9ac1-6e1b7469e42f | -16.6127 | -57.217 | 2024-10-02 08:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.2 |
| 4327f6f5-679b-3638-ac48-77e39adf2cd1 | -16.6168 | -58.2343 | 2024-10-02 08:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.9 |
| 87ca4b32-7d90-3c70-9fe8-854439bf9fbe | -16.6171 | -58.214 | 2024-10-02 08:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.2 |
| 1986a736-01d6-35d2-b81c-252c7e18ae11 | -16.6322 | -57.2147 | 2024-10-02 08:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 153.1 |
| 2c091c8e-8354-37df-b2e5-ee67afc6fcea | -16.6518 | -57.2125 | 2024-10-02 08:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.4 |
| 27ee6467-9f7d-3c15-b60b-f7434beef806 | -16.7461 | -57.4265 | 2024-10-02 08:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.2 |
| 0637f742-17e6-3111-a3d8-d6c3fa81ef3a | -16.8292 | -55.9152 | 2024-10-02 08:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 71.4 |
| 372a9fd8-c3fa-36f5-8a25-6ee8808fb05d | -16.8295 | -55.8945 | 2024-10-02 08:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 81.2 |
| 7164dd9f-a0cb-3daa-b059-8ead0a4ab756 | -17.0892 | -56.7709 | 2024-10-02 08:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.9 |
| 7118031c-2d1f-3d93-8a11-8cc183d60162 | -17.0895 | -56.7503 | 2024-10-02 08:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.9 |
| e3fd7d7f-0b07-3190-a495-d2a8dfdf9b14 | -17.1288 | -56.7455 | 2024-10-02 08:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.4 |
| 0c69ea84-f273-36db-a528-c4c7ecce7b71 | -17.1091 | -56.7479 | 2024-10-02 08:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.1 |
| cd9dd3e9-2f27-38e2-a32d-fb2742f5a2a1 | -17.1088 | -56.7685 | 2024-10-02 08:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.7 |
| 42e880e9-87f4-3fa4-a1d1-dace55bc1ce1 | -22.3713 | -49.3011 | 2024-10-02 08:07:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 119.3 |
| e56ed5d6-d8d2-3856-b665-311f2b2f9223 | -22.372 | -49.2777 | 2024-10-02 08:07:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 92.3 |
| 21a2a25f-36c8-3c45-aaad-86003bf6382f | -22.3922 | -49.2961 | 2024-10-02 08:07:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 115.5 |
| 75dd8a70-37dc-3533-a244-3f96f274edee | -22.3929 | -49.2727 | 2024-10-02 08:07:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.6 |
| 3800bee0-0dae-3a63-bad4-7303ddeada11 | -12.6484 | -63.1214 | 2024-10-02 08:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 9eaa2299-2278-3e19-ac36-b7f7b96d3d42 | -15.5486 | -56.8873 | 2024-10-02 08:16:34 | GOES-16 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 5d566bfb-6dbe-338a-bb4d-cf9b5eb61805 | -15.9003 | -50.1537 | 2024-10-02 08:16:35 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| ecd4b300-484a-37d6-9114-7c7cdff86521 | -16.5778 | -58.2386 | 2024-10-02 08:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 138.4 |
| 7fc54776-88eb-34a9-856f-e426d1e83c01 | -16.578 | -58.2183 | 2024-10-02 08:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.9 |
| 9a473d17-a9d6-3ade-8a82-8a63b9886fa5 | -16.5973 | -58.2365 | 2024-10-02 08:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 352.7 |
| da223e38-a571-3d34-a312-901cc6c766d4 | -16.5976 | -58.2162 | 2024-10-02 08:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 272.7 |
| 57135f3d-7f9c-3eb3-be94-4d945bbeab5e | -16.6168 | -58.2343 | 2024-10-02 08:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.0 |
| 9f11014a-7997-3edc-a694-f0884f17a2cd | -16.6171 | -58.214 | 2024-10-02 08:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 116.3 |
| 03c0e57b-f97e-33b0-a3d1-55070e201c6a | -16.8292 | -55.9152 | 2024-10-02 08:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 74.6 |
| 6ff0dc73-88c8-3599-8e48-c8ea4625dc05 | -16.8295 | -55.8945 | 2024-10-02 08:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 87.3 |
| b3ca914f-a308-39a6-90c7-aefac834c935 | -16.8695 | -55.848 | 2024-10-02 08:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 75.6 |
| aa656f01-b942-305a-8862-f8e8a1fa0c6c | -16.8891 | -55.8455 | 2024-10-02 08:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 110.1 |
| 44948084-e8b9-3a59-a3dd-15542b900309 | -16.8894 | -55.8247 | 2024-10-02 08:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 70.8 |
| 4cdbe806-9184-3890-bb97-10dd25767021 | -17.0892 | -56.7709 | 2024-10-02 08:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.4 |
| 8dc5233d-5afe-3a5d-bfd8-4bf1181e1acb | -17.0895 | -56.7503 | 2024-10-02 08:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.6 |
| a95b22b4-2b19-30fa-984f-bc9f3c4f97ee | -17.1088 | -56.7685 | 2024-10-02 08:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.2 |
| 41fa1848-ae46-37cf-938c-a14575070efd | -17.1091 | -56.7479 | 2024-10-02 08:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.8 |
| 537e780c-331f-315c-a202-2607e8d05513 | -17.1288 | -56.7455 | 2024-10-02 08:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.2 |
| ff53a3c4-b751-3980-bebb-09b483c6c80a | -21.3661 | -55.6807 | 2024-10-02 08:17:05 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 48.5 |
| c585aa14-024f-325a-b78d-77be12b85dbc | -22.3713 | -49.3011 | 2024-10-02 08:17:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 115.9 |
| 462265a8-57b5-336a-a2a4-398b6ee0422c | -22.372 | -49.2777 | 2024-10-02 08:17:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 87.2 |
| 00232bdd-14fb-3de3-8ba7-281ad80d5421 | -22.3922 | -49.2961 | 2024-10-02 08:17:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 105.2 |
| ccdf1016-4b13-38fb-bc62-723223dd8dc2 | -22.3929 | -49.2727 | 2024-10-02 08:17:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.0 |
| f3ffdc1b-602b-3b5b-904e-4c749ea1fe24 | -12.6486 | -63.1022 | 2024-10-02 08:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 7c48b589-0f2e-3c35-b7e4-8e1710fd5b48 | -12.6484 | -63.1214 | 2024-10-02 08:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 40b94c17-e508-3733-91d6-8fb1a52706ec | -13.5572 | -51.1846 | 2024-10-02 08:26:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| d1675650-a83a-3287-9d8d-09aab76ba87b | -13.5569 | -51.2061 | 2024-10-02 08:26:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 57.9 |
| ba4f342a-d543-33cb-937c-d90184a5646d | -15.5486 | -56.8873 | 2024-10-02 08:26:34 | GOES-16 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 59.6 |
| e461ba60-6ab7-37e6-8a52-74055dcca3da | -15.9003 | -50.1537 | 2024-10-02 08:26:35 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 63adf3da-b2f6-3c2b-ba4a-c4580f3744f1 | -16.6171 | -58.214 | 2024-10-02 08:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.2 |
| f3b7ecc4-82d7-3800-828c-248144e4ff36 | -16.6168 | -58.2343 | 2024-10-02 08:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.6 |
| 60764cd4-94c4-3360-86aa-ed84aabe7be6 | -16.5976 | -58.2162 | 2024-10-02 08:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 321.8 |
| ad9af034-42b5-3781-bb47-b29aefa7cf6c | -16.5973 | -58.2365 | 2024-10-02 08:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 374.9 |
| 9e377a41-92b9-3d60-a076-d3836838bf6b | -16.578 | -58.2183 | 2024-10-02 08:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.7 |
| 4ec98797-d782-388c-a6c2-5b5ed714f76c | -16.5778 | -58.2386 | 2024-10-02 08:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 115.3 |
| 18c3c630-1465-3d4d-b657-2775a8e7db10 | -16.8894 | -55.8247 | 2024-10-02 08:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 79.6 |
| 1abc11e5-03fe-3378-8882-57f11c0d145c | -16.8891 | -55.8455 | 2024-10-02 08:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 128.3 |
| 9284752a-8b25-38a6-bdd1-5a4ac7f92a6e | -16.8695 | -55.848 | 2024-10-02 08:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 87.4 |
| b69c54ae-0cad-3624-81ca-7052c6a071b9 | -16.8295 | -55.8945 | 2024-10-02 08:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 84.1 |
| 4bc56af9-5051-3cf6-b034-f16493e0bacd | -16.8292 | -55.9152 | 2024-10-02 08:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 73.6 |
| 2086cd84-2a1f-31dc-9181-09b29836d7df | -12.6484 | -63.1214 | 2024-10-02 08:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 8590ef8d-450c-343c-83b5-d9b09bbb2408 | -13.0211 | -51.1456 | 2024-10-02 08:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.8 |
| b15d7644-0dbf-345e-ae6e-cc13899cbaad | -13.1125 | -51.4115 | 2024-10-02 08:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 607b5537-ade9-3247-b53b-b20a6a5e7ac4 | -15.5486 | -56.8873 | 2024-10-02 08:36:34 | GOES-16 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 60ff6104-6c6c-38ee-9dcd-f88d6aecc405 | -16.514 | -57.2896 | 2024-10-02 08:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.0 |
| 4970a632-4618-3abc-9d43-2be256b435c1 | -16.5778 | -58.2386 | 2024-10-02 08:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 127.2 |
| d937368f-6194-3385-af56-2fd3a85a5972 | -16.578 | -58.2183 | 2024-10-02 08:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.8 |
| 31355f54-e757-3d33-b612-1fb642b0bd78 | -16.5973 | -58.2365 | 2024-10-02 08:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 476.3 |
| 9cda8c24-1e38-3468-96b7-a60654d7f90e | -16.5976 | -58.2162 | 2024-10-02 08:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 341.0 |
| 139ce1b9-acb3-3e3a-a854-ce8ce8506afa | -16.6124 | -57.2375 | 2024-10-02 08:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.5 |
| 1a591993-8a58-3329-9d52-25d9cd73b8a9 | -16.6127 | -57.217 | 2024-10-02 08:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 118.1 |
| 87c0fefd-96e6-3f07-b872-fa709b805789 | -16.6168 | -58.2343 | 2024-10-02 08:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.4 |
| 49cc226b-ec30-33f2-8978-66c8a018dd31 | -16.6171 | -58.214 | 2024-10-02 08:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.9 |
| ba3e5494-f1d7-3712-83ec-f0f667a726a7 | -16.6319 | -57.2352 | 2024-10-02 08:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.6 |
| b3f65eaf-9ab0-3621-a427-560c3f7033c7 | -16.6322 | -57.2147 | 2024-10-02 08:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 334.3 |
| be43f846-05cb-3792-aa90-621b6e972f34 | -16.6326 | -57.1943 | 2024-10-02 08:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.8 |
| 6c7059fb-b5a0-3bc8-9c1b-3e49d5177c5e | -16.6518 | -57.2125 | 2024-10-02 08:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 140.6 |
| 0545fd20-f1a6-3d7e-81d5-2bfa2d4554f8 | -16.8894 | -55.8247 | 2024-10-02 08:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 78.8 |
| 0602cc47-0ea0-3ce8-a833-83fa5a477659 | -16.8292 | -55.9152 | 2024-10-02 08:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 73.0 |
| 44659456-64ca-3b6e-99e4-709ff106e05c | -16.8295 | -55.8945 | 2024-10-02 08:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 83.1 |
| 71391167-8b0c-3fef-a509-6359fb493442 | -16.8695 | -55.848 | 2024-10-02 08:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 80.9 |
| 5fedc8ec-990c-3795-9f1f-e0659d66a55f | -16.8891 | -55.8455 | 2024-10-02 08:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 127.5 |
| b09db1c2-2d0f-304f-b615-faf6f095bc9d | -21.3661 | -55.6807 | 2024-10-02 08:37:05 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 00cb68a7-e866-3c15-b2b9-488e2247622b | -12.6484 | -63.1214 | 2024-10-02 08:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 50.2 |
| d88d812a-e424-3069-b1db-b3c98212e813 | -15.5486 | -56.8873 | 2024-10-02 08:46:34 | GOES-16 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 9b706f3e-3c16-37f0-a0f1-c3276308dbe4 | -16.6124 | -57.2375 | 2024-10-02 08:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.0 |
| 371c0090-fb1f-3d33-831a-9b47dd66583d | -16.6127 | -57.217 | 2024-10-02 08:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.3 |
| bdadded9-c012-38f8-b983-9bc0c3ba9618 | -16.6319 | -57.2352 | 2024-10-02 08:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.1 |
| f603148d-bfb1-33a8-896b-65b8a834e558 | -16.6322 | -57.2147 | 2024-10-02 08:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 242.3 |


[Clique aqui para ver as próximas entradas](README201.md)
