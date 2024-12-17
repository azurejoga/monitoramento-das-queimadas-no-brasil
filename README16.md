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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3dd13589-5d2a-37d7-8944-3cbc4087b567 | -4.39999 | -44.88008 | 2024-12-17 04:21:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3da79d8a-29f0-3d58-9c76-6b75114f2d72 | -4.07124 | -47.09199 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 80ae953e-d1c8-31bd-a15e-8b1ae63dd087 | -5.20703 | -43.29821 | 2024-12-17 04:21:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c8ec55b8-ea84-39d1-833f-369bca87a26d | -4.25414 | -47.57544 | 2024-12-17 04:21:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fbf3cd8-37f0-3335-a996-29a8a39a99ab | -4.05073 | -46.92731 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90a82db8-2290-3add-b106-d1a7ba4e2e26 | -4.51688 | -47.94241 | 2024-12-17 04:21:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94774df3-199e-30ec-a1f3-afeb7ac1b841 | -4.7346 | -46.80312 | 2024-12-17 04:21:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67b51e02-7477-3972-acd0-2a03a7088286 | -4.70588 | -44.38105 | 2024-12-17 04:21:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9a2aa5db-1958-39cd-bd9f-77abc0edc31e | -4.10641 | -46.62482 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7767875-11f4-3a11-bc7a-2d1ba5472eb5 | -3.30442 | -53.36794 | 2024-12-17 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| ee59c8b2-e5d6-3250-98d3-291d85ea9c82 | -4.02534 | -47.04014 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58850ef9-f24b-3eca-9238-4350bf37695f | -2.65155 | -42.71756 | 2024-12-17 04:21:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93fac1ff-806a-321d-b791-48b693075aad | -3.91207 | -42.87344 | 2024-12-17 04:21:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b558fe9f-efe1-32f5-8136-d5ec374dc08f | -4.228 | -44.02071 | 2024-12-17 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8a60efe-6973-3fcf-999c-b7376ecd517e | -5.09611 | -46.1199 | 2024-12-17 04:21:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c8602be-d850-30ad-8bee-bd276e9ad730 | -3.15573 | -53.18679 | 2024-12-17 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e473438-c301-3f66-b381-c6b5553d723f | -4.6771 | -44.04124 | 2024-12-17 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 207fdf06-9a59-3670-8613-b2f1434ce495 | -3.77154 | -47.17316 | 2024-12-17 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c4c45352-1401-3ad4-b303-f55c91a0a6bd | -4.93055 | -43.96401 | 2024-12-17 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5fb77da8-dad5-32da-b8f3-9bd7d74dce59 | -3.23628 | -46.80063 | 2024-12-17 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b29acbef-d7f7-346c-880b-7f2e1d4b4111 | -4.02541 | -46.80813 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 410e3310-cb18-3129-8d1c-0a9b12883db4 | -5.98397 | -41.56892 | 2024-12-17 04:21:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c200f43a-0e8f-3321-89c0-5260e21388e6 | -4.01896 | -46.89438 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9fd7ae3a-d031-3af1-9685-691f13c17a53 | -3.92339 | -46.92435 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e90175b6-6a8a-3eb0-9c64-2f3b4631c3be | -2.17906 | -53.74681 | 2024-12-17 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be757aa2-f576-3e5a-acca-ad31aac731c0 | -4.24567 | -45.99079 | 2024-12-17 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a869474-b0ba-30f4-a8ab-03426188ade8 | -4.93109 | -43.96054 | 2024-12-17 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 83c0d5f7-b249-327b-9be5-2f1209fcc12d | -5.06315 | -46.39409 | 2024-12-17 04:21:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 34a5bbe0-c900-3d3b-a0ae-bc57b97e50f8 | -5.09246 | -44.80203 | 2024-12-17 04:21:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9cb1bc1d-3913-35c6-96c3-95c0d0bf2cf6 | -5.13807 | -43.24038 | 2024-12-17 04:21:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a16959e4-76ce-39bb-98bf-3f7c44a8a0bc | -3.08838 | -46.56335 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d07005f3-2461-3c8d-a336-0629e36620e4 | -2.78236 | -42.75264 | 2024-12-17 04:21:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 759a4b65-0cb7-329f-998c-d06fbd09c588 | -3.23979 | -46.80117 | 2024-12-17 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b77d0815-2b2a-3d92-b513-c9b972751b04 | -4.06436 | -46.9095 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec8c4b75-6add-3627-bdb0-e088bdf3e678 | -3.98676 | -48.40049 | 2024-12-17 04:21:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a992aee3-ba27-3745-bf2d-e4287c2807e2 | -4.33508 | -43.55085 | 2024-12-17 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e41def25-3178-3cb2-a08b-742270f3dbe4 | -4.22854 | -44.01727 | 2024-12-17 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb0821af-9c41-3704-b661-111e2994a315 | -4.09752 | -46.72477 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4cb678e8-075e-352a-8e8a-800e9547d435 | -4.05874 | -46.24192 | 2024-12-17 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16c97f3e-a17d-3904-a0b1-9119ad4bd4a3 | -3.80173 | -46.71107 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d69289e1-e361-37c1-a230-27332ccb2c31 | -5.59252 | -43.28425 | 2024-12-17 04:21:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3f61595-66e5-36ae-9124-7d5e9be88eae | -4.07288 | -47.10447 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 30eb0000-e2ce-3002-b181-5bab3c8b461b | -3.20941 | -42.69339 | 2024-12-17 04:21:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4089b48-eb68-3394-842b-3efc328452d5 | -4.17434 | -46.3093 | 2024-12-17 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13d63e54-3d07-33c1-9239-8b562d42e322 | -3.9932 | -44.17413 | 2024-12-17 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 174070de-4fc4-343e-80e7-1cadd4622b1c | -3.79896 | -46.84159 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e32d885-3be2-3f76-b0b9-82c183c40386 | -1.71131 | -46.21388 | 2024-12-17 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2cca1d7-494e-339b-92b4-4584e3a1c33a | -5.45231 | -44.80571 | 2024-12-17 04:21:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98a68945-09eb-3eb7-9e14-88bf51a5e5b1 | -4.87586 | -41.39077 | 2024-12-17 04:21:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e961a714-43c5-36b7-a07c-e1f4e19feb68 | -4.67379 | -44.04073 | 2024-12-17 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8b9bdce-47f1-3608-968a-fb912598eeb0 | -5.11669 | -43.20049 | 2024-12-17 04:21:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4fcdcbb9-1ba9-3870-b3b1-84942974852a | -5.36679 | -44.04612 | 2024-12-17 04:21:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a67089e-518f-319d-a80d-6e18465cc15f | -2.57322 | -49.40835 | 2024-12-17 04:21:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8b498ca-7847-35cf-9957-4c0d322fa10e | -4.12427 | -43.57154 | 2024-12-17 04:21:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 151ad72c-5ddf-3f2c-91f0-0ca4d6ffbc5f | -3.01748 | -48.03015 | 2024-12-17 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c6ea7cd7-1e5d-31a1-99a5-7c9382a60d06 | -3.00997 | -48.02898 | 2024-12-17 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc029eba-66f2-3cc2-a32c-806f489f4bd6 | -4.2061 | -46.48624 | 2024-12-17 04:21:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c466bf1-eef9-3b1f-bb15-34e809002e13 | -4.06149 | -46.90502 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 869fcda7-7ac4-31c8-bc72-762c74c6247d | -5.13862 | -43.23682 | 2024-12-17 04:21:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cdea82be-c971-3c78-a036-1578ed21c8d4 | -4.00699 | -46.92479 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0f7f115-06bb-30c0-a9bb-32288bd89e1f | -15.07297 | -59.6538 | 2024-12-17 04:23:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 5bcaa694-759e-35c1-bc51-5ee8615097ea | -6.92903 | -43.50525 | 2024-12-17 04:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 6ee7a8dc-bffb-321f-bf1d-7dfb099a21c0 | -6.95545 | -42.82857 | 2024-12-17 04:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a51a73a3-48da-397c-98f0-33ffcf522f83 | -6.2119 | -43.92414 | 2024-12-17 04:23:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 48403240-187a-334c-9369-1ed66f916b5a | -6.21589 | -46.21938 | 2024-12-17 04:23:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62a1fded-fca4-3532-9b02-8f667fc4f62e | -6.96721 | -43.00309 | 2024-12-17 04:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 01de4e55-c0f9-3605-92c1-576ca77ef97c | -5.99344 | -43.48444 | 2024-12-17 04:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af8960a6-71f8-3524-a9a6-703ff0578848 | -7.86265 | -43.08603 | 2024-12-17 04:23:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 72d170e1-794f-3303-9fdd-df1c88799877 | -10.48878 | -36.84792 | 2024-12-17 04:23:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 20eafea4-bca4-3c6e-a60b-30d1396a76ff | -6.92511 | -43.50835 | 2024-12-17 04:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d99dbf82-5655-3705-a051-a885ac5b5da2 | -6.97553 | -42.83078 | 2024-12-17 04:23:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 10c9ae45-6da4-3444-9bf0-ab22cb7b9f4b | -6.93186 | -43.50937 | 2024-12-17 04:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 81b5818e-fe9c-377b-b2fe-29d47a1b8df6 | -6.45891 | -46.34191 | 2024-12-17 04:23:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6753f858-1d48-3041-b1ba-d9ca84cbb962 | -7.80088 | -46.20538 | 2024-12-17 04:23:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc5fe58d-9694-3d33-878e-257d93fb7e80 | -5.93403 | -45.48828 | 2024-12-17 04:23:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9aa9f9a7-5001-3478-b228-b4417634b0dd | -15.07416 | -59.64818 | 2024-12-17 04:23:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c72addd7-51de-34ce-954f-63f58e3b1843 | -15.0806 | -59.64967 | 2024-12-17 04:23:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 81c28b00-bf91-383d-b83e-006dd3d15cb7 | -9.2783 | -35.91053 | 2024-12-17 04:23:00 | NOAA-21 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ed14c2cb-9911-3f77-8a59-a782c86ddc57 | -15.07403 | -59.64928 | 2024-12-17 04:23:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 63e47624-9870-3cb8-a987-966ee79a3de8 | -7.90605 | -35.23601 | 2024-12-17 04:23:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| ba58a0b1-8892-351b-95fa-d8a202d758d7 | -7.82091 | -35.22823 | 2024-12-17 04:23:00 | NOAA-21 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 3665ecc2-016e-34c5-a795-b800d77d5af5 | -5.3198 | -46.4831 | 2024-12-17 04:23:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 245638dc-e50f-3842-8fcc-d0cc14fefe17 | -6.98858 | -43.55537 | 2024-12-17 04:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c01267f7-8db7-37fd-aafd-4cc63077ac93 | -6.99085 | -43.56311 | 2024-12-17 04:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 71a14388-3a1f-3769-bfca-af1a4379a774 | -8.65373 | -36.90904 | 2024-12-17 04:23:00 | NOAA-21 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f794dbb5-5a03-3a6d-b71a-0e6ee86897fb | -6.20703 | -46.21818 | 2024-12-17 04:23:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3bde4b07-8753-3447-a870-e7db682d7cf1 | -6.64126 | -47.35358 | 2024-12-17 04:23:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| adca5410-64f9-333e-b5b8-52a7b1ef50d9 | -6.20706 | -44.82939 | 2024-12-17 04:23:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08474f5e-4dcf-3e08-8ee6-e914b939d5d8 | -10.15881 | -42.44748 | 2024-12-17 04:23:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 924c9fb9-e6c5-3352-84f7-66ea29007e31 | -6.2076 | -46.21458 | 2024-12-17 04:23:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 077b455f-7470-398c-bbc8-f9f9286112bc | -6.94408 | -47.79461 | 2024-12-17 04:23:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a0b07bae-0a80-3ba1-ae0d-2692451cf28d | -7.45831 | -34.81436 | 2024-12-17 04:23:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 35364921-c403-3e39-bdbb-aad2b3640d57 | -6.97255 | -40.63412 | 2024-12-17 04:23:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b4522596-2f13-3f3a-b3fd-4d04cf1fcb33 | -8.88136 | -41.10234 | 2024-12-17 04:23:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| baf8f0bb-1807-3653-bff6-d4cf98421642 | -6.03419 | -42.15286 | 2024-12-17 04:23:00 | NOAA-21 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c7272b49-73c8-35e0-a534-709d344bee97 | -6.98297 | -42.80471 | 2024-12-17 04:23:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 59c230bd-e625-3c0f-a79a-5a75d655a59f | -7.45953 | -34.8137 | 2024-12-17 04:23:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 292ea2da-8476-3865-a395-710688ca9adb | -15.07279 | -59.65491 | 2024-12-17 04:23:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 993f27fe-00a7-37bf-9eb5-3cb222330c12 | -7.15396 | -46.69749 | 2024-12-17 04:23:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04510635-6ef6-3488-ae5a-2ea87e526816 | -6.20647 | -46.22178 | 2024-12-17 04:23:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |


[Clique aqui para ver as próximas entradas](README17.md)
