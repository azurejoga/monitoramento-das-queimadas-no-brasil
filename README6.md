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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28aaab98-b2cf-37cf-8ccf-3a103a5b795b | -7.34448 | -48.82834 | 2025-07-17 00:26:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 43e0c16e-380f-30c8-b1b6-14b8d700bd32 | -3.38314 | -47.47634 | 2025-07-17 00:26:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 420e1fa1-21ca-3f40-9339-01b757832bfa | -11.1125 | -48.8531 | 2025-07-17 00:30:00 | GOES-19 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| b2ef2bf4-b221-3ec6-b012-5cbea8a4be28 | -8.1072 | -43.1646 | 2025-07-17 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 139.3 |
| 74291e33-013a-3a9b-b919-2d243766d02a | -8.1264 | -43.139 | 2025-07-17 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.4 |
| f96a94a3-e4fb-3e40-a280-59f1a15ef1ac | -11.1121 | -48.875 | 2025-07-17 00:30:00 | GOES-19 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 08ced07f-cfd8-39c6-8b5e-618cfd11ddbf | -9.2638 | -48.5527 | 2025-07-17 00:30:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 48410bf5-e34d-3534-afd0-9ba0a42e9cf1 | -9.2447 | -48.5764 | 2025-07-17 00:30:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 107.8 |
| bce63290-f300-3f15-9bc2-0373f5352540 | -6.7192 | -44.3461 | 2025-07-17 00:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 19371e48-b677-3e3a-9ace-ebcb8676602d | -5.6569 | -43.6929 | 2025-07-17 00:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| d2436c59-5e19-3c38-8a44-b5e38a965270 | -3.3771 | -47.501 | 2025-07-17 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| e3a1ff7f-d869-3dd4-9942-a6b2db9d019c | -9.2449 | -48.5546 | 2025-07-17 00:30:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 192.2 |
| 6579f6bc-a932-39a4-8cd7-f9e52415a4a8 | -5.6567 | -43.7161 | 2025-07-17 00:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 430.6 |
| 384dab16-7ea6-3490-9f36-62aafdc2cdc4 | -6.7379 | -44.3445 | 2025-07-17 00:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 42.6 |
| d2bc2470-01d9-3e44-a72e-8d307582cfca | -8.0886 | -43.1431 | 2025-07-17 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 89.0 |
| 1ca05de0-2982-36e4-8b88-75979b6c42dd | -6.7194 | -44.3231 | 2025-07-17 00:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 1c447a52-838e-3a39-8ddd-8d3f52f55f6b | -3.3958 | -47.4785 | 2025-07-17 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| d16f6942-c9e2-36ae-800c-cd24af85100d | -22.3989 | -49.7795 | 2025-07-17 00:30:00 | GOES-19 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 68.7 |
| df4db5c7-816b-3e83-bc67-c945c02d50c7 | -11.9376 | -48.4228 | 2025-07-17 00:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 86c45953-50e4-3bda-8786-e32da112642b | -5.5241 | -43.8878 | 2025-07-17 00:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 292a0e11-6a84-3826-b2ff-b46ee932aa6c | -3.3772 | -47.4792 | 2025-07-17 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| ba31bf0a-af66-36aa-8e70-d7c53d6a7bd9 | -6.7006 | -44.3247 | 2025-07-17 00:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 46a52233-9b38-3ea4-a5a6-97baab795700 | -9.2261 | -48.5565 | 2025-07-17 00:30:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 07a6b302-fb4d-3b20-bd5d-9e90b7039db4 | -6.7382 | -44.3215 | 2025-07-17 00:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| d6f497ac-57fe-3a8c-af51-33b988b7638f | -8.1075 | -43.1411 | 2025-07-17 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 324.9 |
| 4bb9cf15-be7f-3b04-b383-df4df2207931 | -12.7122 | -46.8001 | 2025-07-17 00:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| c1a4535d-fbbd-3d00-9b8c-310b6b2bc318 | -12.427 | -50.0387 | 2025-07-17 00:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| ad97c5f4-f0d8-30cf-86df-cfaac431e752 | -5.6565 | -43.7393 | 2025-07-17 00:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 31523ab3-be2f-3a31-b073-49c7f4efcabf | -5.6754 | -43.7147 | 2025-07-17 00:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 47697c27-160d-3133-958c-a857fc6c8573 | -3.3957 | -47.5003 | 2025-07-17 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| c0d9535e-da29-3378-ae4b-4b458f3a60bd | -8.1072 | -43.1646 | 2025-07-17 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 117.5 |
| 30a7db72-12a2-3c54-bbc1-91b07aef5509 | -12.7122 | -46.8001 | 2025-07-17 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 92210da8-2aa7-36e4-9329-495c59cb40c1 | -8.1264 | -43.139 | 2025-07-17 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.5 |
| a0f2ab46-de50-3003-8fac-bd656413a1f6 | -9.2449 | -48.5546 | 2025-07-17 00:40:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 201.1 |
| 5cf5c3b9-be94-3a0d-b23e-73e9ad46d37c | -22.3989 | -49.7795 | 2025-07-17 00:40:00 | GOES-19 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 50.9 |
| dbeb1ec5-60d2-3ad6-970a-3bad6dc44c13 | -3.3772 | -47.4792 | 2025-07-17 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| f91d1100-ecc8-3a46-a211-719ba75b4ec6 | -8.1075 | -43.1411 | 2025-07-17 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 258.4 |
| 1b2fc708-6555-34f2-b2d5-14095497df4f | -8.0886 | -43.1431 | 2025-07-17 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 89.6 |
| fa85c144-1176-3a08-b9a9-9c6a3ef39583 | -3.3958 | -47.4785 | 2025-07-17 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 5d5b60c0-e6ad-377a-854c-e5d083d45717 | -6.7194 | -44.3231 | 2025-07-17 00:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 57355046-97e4-3722-8953-16cf86a70164 | -5.6565 | -43.7393 | 2025-07-17 00:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 18100ec1-4b33-3108-b6f3-b7dd8e6b2c0f | -11.1125 | -48.8531 | 2025-07-17 00:40:00 | GOES-19 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 04f90d74-c61d-3f00-bce8-81f4bbb0418d | -5.6379 | -43.7175 | 2025-07-17 00:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 518318f6-1dff-3666-ab84-e796b48f9ef1 | -5.6569 | -43.6929 | 2025-07-17 00:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| bb176f62-705b-31ff-85e4-9d63f5b798a4 | -12.427 | -50.0387 | 2025-07-17 00:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 6b6ba289-f569-3ce3-a385-26baaa0a1f0a | -5.6567 | -43.7161 | 2025-07-17 00:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 314.8 |
| 932dd7ae-e01c-34fd-a1d1-ea0a1e8ac5b4 | -3.3957 | -47.5003 | 2025-07-17 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| a099dad7-dce9-3441-b302-a08f476baa14 | -21.2908 | -48.8605 | 2025-07-17 00:40:00 | GOES-19 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 111.9 |
| da0f6216-f8b4-368c-883e-1ce96ccbfacb | -11.9568 | -48.4203 | 2025-07-17 00:40:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 57aeae31-b317-3ef7-b745-5d26a9649c38 | -11.1121 | -48.875 | 2025-07-17 00:40:00 | GOES-19 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 092a64ab-d476-3132-98ee-04750cfa1495 | -5.6754 | -43.7147 | 2025-07-17 00:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 240.1 |
| b71ebed8-60c8-38e4-a055-06074f20cc99 | -9.2447 | -48.5764 | 2025-07-17 00:40:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| fe46ca5c-2855-3f4a-b9a5-658fdd3a8c4b | -3.3957 | -47.5003 | 2025-07-17 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 297755e8-6b65-3cfa-bf95-434ec8901720 | -8.1075 | -43.1411 | 2025-07-17 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 267.4 |
| e26c9d1e-4ede-36bc-bed1-979f02c49cd1 | -9.2449 | -48.5546 | 2025-07-17 00:50:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 161.2 |
| 46b2e236-69ec-319b-ab2e-7877775f4847 | -5.6565 | -43.7393 | 2025-07-17 00:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 55ecfbe1-2396-3068-bcda-885d2ee9ab7f | -3.3772 | -47.4792 | 2025-07-17 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 2f98eb66-6dae-3b95-8153-8c6a5aa24bb6 | -12.7122 | -46.8001 | 2025-07-17 00:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 5b0dea9f-0152-38ca-8ecc-9742596049b1 | -8.1072 | -43.1646 | 2025-07-17 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 92.3 |
| fe0d45e3-1560-392b-ae1d-0051d98954fa | -8.1264 | -43.139 | 2025-07-17 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.3 |
| 1e62b686-f62d-3774-85cf-83d7d36742b9 | -8.0886 | -43.1431 | 2025-07-17 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.0 |
| 742064d4-9759-3ffe-9cde-0381321511f7 | -6.7194 | -44.3231 | 2025-07-17 00:50:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| d6ed4261-1431-3af8-8058-5ca0065b3939 | -9.2447 | -48.5764 | 2025-07-17 00:50:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| ca9fae38-1e47-3289-ab15-99c2b244a1ac | -5.6567 | -43.7161 | 2025-07-17 00:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 312.2 |
| 2f2f4e46-9e51-3c61-8b45-5cfe9c2b308e | -5.6569 | -43.6929 | 2025-07-17 00:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| ad2a6e44-d059-3e5b-9b18-2d1992917654 | -3.3958 | -47.4785 | 2025-07-17 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| ceb4675e-8682-3421-98d1-9283b219c0e5 | -5.6756 | -43.6915 | 2025-07-17 00:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| c44afe95-fa87-3397-aea9-1e2ff71933c4 | -11.1125 | -48.8531 | 2025-07-17 00:50:00 | GOES-19 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| a02cb661-e9f0-3fd7-86e4-5dee244d11be | -6.7382 | -44.3215 | 2025-07-17 00:50:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 696ee498-3d19-32a6-9f39-89b1fdd2f646 | -11.1121 | -48.875 | 2025-07-17 00:50:00 | GOES-19 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 130.2 |
| c0e5e5fb-5b15-364c-a7e1-c3899f918c8a | -5.6754 | -43.7147 | 2025-07-17 00:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 204.9 |
| b7733347-81a1-3956-ae2f-daf3dc808174 | -6.7382 | -44.3215 | 2025-07-17 01:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 0adae2b6-0938-354e-b790-814a529cea20 | -5.6754 | -43.7147 | 2025-07-17 01:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 159.6 |
| af8ce4fa-6bea-3aac-a106-d177b537f69c | -9.2449 | -48.5546 | 2025-07-17 01:00:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 8b1e5717-0221-3be2-a61f-714c42013470 | -3.3958 | -47.4785 | 2025-07-17 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 393e1c95-55a1-31a9-95ef-60265fd83f6e | -11.1121 | -48.875 | 2025-07-17 01:00:00 | GOES-19 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 105.2 |
| fb600425-ed3b-3a7f-9e3e-f6d4743dbcff | -9.2447 | -48.5764 | 2025-07-17 01:00:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 56283f93-a4bf-3bcf-b72a-6e104a24a705 | -5.6569 | -43.6929 | 2025-07-17 01:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| f568f986-5fdc-35ca-bd0a-3630b58766f2 | -5.5241 | -43.8878 | 2025-07-17 01:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 37ac64d9-8612-3324-ad2a-f90ea572e54f | -12.7122 | -46.8001 | 2025-07-17 01:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 69441f4c-b999-38fc-930f-d12b0652099a | -8.1072 | -43.1646 | 2025-07-17 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 112.9 |
| 3eec725e-9404-3047-be66-e31704e8a5c5 | -3.3772 | -47.4792 | 2025-07-17 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 1f0d3f93-a5b8-3452-9578-1934e7494145 | -5.6567 | -43.7161 | 2025-07-17 01:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 388.9 |
| 225b76ff-db97-3327-9e57-808d167bf8c7 | -8.1075 | -43.1411 | 2025-07-17 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 205.9 |
| b5d5b587-c8aa-30f0-b48b-ceb21c24b601 | -6.7194 | -44.3231 | 2025-07-17 01:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 0c061d91-875d-3187-a05b-2876a0d4e6cd | -3.3957 | -47.5003 | 2025-07-17 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 3dc9b261-5694-355a-9a4f-cd1f772a9764 | -5.6565 | -43.7393 | 2025-07-17 01:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 09afb986-1cca-3178-a067-105bda59d892 | -12.3983 | -50.0131 | 2025-07-17 01:09:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4dfcefe0-8976-3f57-b2ea-49f12a812b58 | -23.2668 | -52.108601 | 2025-07-17 01:09:00 | METOP-B | PRESIDENTE CASTELO BRANCO | PARANÁ | Brasil | 4120408 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 922a9b2d-167c-3a7a-b503-e5a9ac560575 | -18.651899 | -55.715599 | 2025-07-17 01:09:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7038afeb-8c64-3fbd-ade8-5004eb549016 | -11.9521 | -63.8293 | 2025-07-17 01:09:00 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e5fbc3bd-df6b-3993-a936-27fc097b005e | -12.4079 | -50.010399 | 2025-07-17 01:09:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9b0fc89c-0656-34f8-8d28-1d26d80f4f44 | -10.6715 | -56.5424 | 2025-07-17 01:09:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 53de5d48-bf85-39fb-83e1-a79fae213c61 | -11.0825 | -48.834999 | 2025-07-17 01:09:00 | METOP-B | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 05b9b098-c24a-3052-8011-12c2780b8a79 | -22.3797 | -49.761501 | 2025-07-17 01:09:00 | METOP-B | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6939709d-10c3-39a1-a215-3bb58f4db45b | -18.6542 | -55.724998 | 2025-07-17 01:09:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 963326ea-70cd-38d5-89c8-16e81f3e5d18 | -11.0917 | -48.868698 | 2025-07-17 01:09:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 355bfea6-c0cf-39e4-ad61-32bd2490f8ae | -23.276501 | -52.105701 | 2025-07-17 01:09:00 | METOP-B | PRESIDENTE CASTELO BRANCO | PARANÁ | Brasil | 4120408 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b219a1c9-b58c-3a74-8962-91c6985c109b | -11.0921 | -48.832298 | 2025-07-17 01:09:00 | METOP-B | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 70270c15-126d-33d1-b1c5-596d479c256e | -9.4599 | -63.131699 | 2025-07-17 01:09:00 | METOP-B | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
