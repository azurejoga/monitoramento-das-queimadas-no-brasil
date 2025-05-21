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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d826539-17bf-368d-afc5-4da62c9e21c6 | -6.2226 | -43.3459 | 2025-05-21 00:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 32a02ea4-01d6-3822-9686-77f255626a56 | -18.3341 | -49.8413 | 2025-05-21 00:00:00 | GOES-19 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 181f6c9c-aee8-3457-af73-eeaa5879bcdd | -20.9597 | -56.6179 | 2025-05-21 00:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 2b2b42d0-6a20-3bbc-9a8a-34080b1d019a | -18.3335 | -49.8638 | 2025-05-21 00:00:00 | GOES-19 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 80.6 |
| df6cdba1-da4a-3c92-a0fc-a61f9b4b866c | -11.2887 | -53.97 | 2025-05-21 00:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| e203bc72-6128-3d2d-a2cf-0cd64544bed4 | -11.0901 | -54.7852 | 2025-05-21 00:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 3ec41d3a-efa2-38ef-aeff-82c4ad69a1aa | -12.3137 | -52.4764 | 2025-05-21 00:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 43729c6b-68b0-37ab-ac65-220e7ef5503e | -14.1672 | -45.4673 | 2025-05-21 00:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 155d2324-0d5c-3bc2-b1c9-0d2dc82f1f67 | -12.2943 | -52.4995 | 2025-05-21 00:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 127.3 |
| 2335ffc7-3cd2-30c1-a134-5bd464879e72 | -12.2946 | -52.4785 | 2025-05-21 00:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 203.6 |
| 07c3c62b-2278-36bb-8258-c5389b18a7fe | -11.0714 | -54.7664 | 2025-05-21 00:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 5012414d-2b8d-363b-8110-32112dd6e2e3 | -12.424 | -43.7274 | 2025-05-21 00:00:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| e5fa982a-9911-3291-8ff6-835c661c0293 | -11.2884 | -53.9906 | 2025-05-21 00:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 9ad3e277-eec9-3651-ba72-3f568749d04d | -20.9601 | -56.5967 | 2025-05-21 00:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 76.9 |
| d1fd9b4e-1b7b-301c-8809-dcd9a50829e2 | -12.4433 | -43.7242 | 2025-05-21 00:00:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 33e06d4f-d748-3505-9d85-f41ba9b71dee | -13.6671 | -53.9314 | 2025-05-21 00:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 37d18122-d6dc-3b7b-abc1-31208bb83a2f | -9.0291 | -47.7452 | 2025-05-21 00:00:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| e7c437dd-cbf8-319f-981c-5b0b31caf49c | -11.0712 | -54.7868 | 2025-05-21 00:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 136.2 |
| e4d8398c-6f60-3d05-b639-a2f3949cda8d | -11.1531 | -48.6736 | 2025-05-21 00:00:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 38.1 |
| bb040176-231b-31f6-8c65-bcfde4a4a3cf | -11.0903 | -54.7648 | 2025-05-21 00:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 2b4fc380-bf16-3d61-a31a-0bd79bedb4db | -11.7988 | -44.2733 | 2025-05-21 00:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| b49aa25a-19c3-3ddb-aa31-74ee92d370d7 | -12.2756 | -52.4806 | 2025-05-21 00:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| fed5657e-0615-346c-bec7-456e33dcbef2 | -11.818 | -44.2703 | 2025-05-21 00:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| f2290f54-cc97-31f5-a20e-882ff88a0953 | -11.7948 | -44.260899 | 2025-05-21 00:02:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 269f7abe-d9f3-3b28-bf8c-a769a7b6b7f8 | -16.0354 | -43.800201 | 2025-05-21 00:02:00 | METOP-C | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2dc2a7d6-3c40-3c10-8087-0ba3f2c25001 | -6.2347 | -43.366402 | 2025-05-21 00:02:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e55cf65f-2913-307b-b8b3-fdc793ef41a9 | -8.8997 | -46.907299 | 2025-05-21 00:02:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e2d6e84a-4e98-3d35-ad7f-ab032dc66dee | -11.8076 | -44.2743 | 2025-05-21 00:02:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7dc11f01-214e-3f78-9358-7d6d6bbb2d32 | -8.9094 | -46.9053 | 2025-05-21 00:02:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fa92cd66-6910-3832-b4a1-857d99adef23 | -11.801 | -44.291599 | 2025-05-21 00:02:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 00c3a45d-5361-360a-896e-68969c389bf4 | -9.0305 | -47.7491 | 2025-05-21 00:02:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bad41915-0a16-3c9f-939f-a6d23d086720 | -8.8954 | -46.886299 | 2025-05-21 00:02:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1e8cdf4a-3961-3506-bb37-ae59e84c3df9 | -12.4316 | -43.7449 | 2025-05-21 00:02:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 682ce8ee-26a5-3bee-8bdf-dd62eb3016c1 | -11.7979 | -44.276199 | 2025-05-21 00:02:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ed345568-922a-323d-9654-f21cce7971d6 | -6.2299 | -43.344501 | 2025-05-21 00:02:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 13f1b46c-ad5b-3e3e-9c89-8a251e1a87a9 | -6.2056 | -43.3269 | 2025-05-21 00:02:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 534aeda8-0b6e-38d5-b1b0-dbedeac10ba6 | -6.2201 | -43.3466 | 2025-05-21 00:02:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ab074c55-e9aa-3ce4-ba04-db72e10a2c1c | -12.4258 | -43.716 | 2025-05-21 00:02:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c008f301-2ac7-37a2-9055-b7bc9f530807 | -12.4189 | -43.732399 | 2025-05-21 00:02:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2e812570-acdf-3495-9454-d1b9dfd23282 | -11.8045 | -44.258999 | 2025-05-21 00:02:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ba3093bf-796e-31cf-a6a6-092bb762e662 | -6.2249 | -43.3685 | 2025-05-21 00:02:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bd945d5f-3081-3d5c-a57f-34350794dc05 | -12.8658 | -43.1777 | 2025-05-21 00:02:00 | METOP-C | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| cd6a413d-341d-399c-84c2-5e714bd9ea89 | -11.8107 | -44.2897 | 2025-05-21 00:02:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8b6bf1ab-8c74-34e8-aa00-3b9313f10336 | -12.8685 | -43.191101 | 2025-05-21 00:02:00 | METOP-C | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6187200c-906e-32bd-a0b4-8c96b234ee22 | -12.416 | -43.717999 | 2025-05-21 00:02:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9cee9192-0231-3bf4-aacc-9b12bfc0f91a | -12.4287 | -43.7304 | 2025-05-21 00:02:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d188f2da-384e-3c08-9970-6b7dde05e168 | -8.89 | -46.909302 | 2025-05-21 00:02:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b9375b57-44a4-3570-91fb-80788e9e0c32 | -14.1564 | -45.490799 | 2025-05-21 00:02:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2b7b882b-effe-32b3-8401-273b15cc75c0 | -9.016 | -47.726799 | 2025-05-21 00:02:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 35f5ea09-3c91-3a5d-8feb-cde0cae524f5 | -6.2225 | -43.357601 | 2025-05-21 00:02:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3a170f63-e783-3c6b-ad49-992352f544fc | -14.1525 | -45.4706 | 2025-05-21 00:02:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dc676fad-b772-3a00-b73f-eb1a89067e2c | -9.0209 | -47.750999 | 2025-05-21 00:02:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9a47c7d4-10af-3ae8-b899-7add3ad5ddee | -6.2323 | -43.355499 | 2025-05-21 00:02:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9cd7245e-6e4d-3adb-99aa-825b7e5c5345 | -12.8631 | -43.1642 | 2025-05-21 00:02:00 | METOP-C | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7d3febcd-3229-3e09-adad-878f1af315d0 | -6.2177 | -43.335701 | 2025-05-21 00:02:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 09fd9684-8147-3a13-a8ec-3e2d1bf446fb | -6.2414 | -43.3444 | 2025-05-21 00:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 860a3821-8c59-3673-bde1-9490011139eb | -9.0291 | -47.7452 | 2025-05-21 00:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 24b9b777-81a6-3772-a382-b5b229a6156f | -18.3341 | -49.8413 | 2025-05-21 00:10:00 | GOES-19 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 20e067f9-2b9c-3a59-abd4-42c537a13a0f | -6.2411 | -43.3677 | 2025-05-21 00:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 8bb1be9e-8e0c-3b69-b355-1aa288259159 | -11.0712 | -54.7868 | 2025-05-21 00:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 990fb467-865d-37de-8667-4e11986d9563 | -13.6671 | -53.9314 | 2025-05-21 00:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 38.4 |
| a5640179-d49e-3213-af24-8d0335e88c03 | -11.7988 | -44.2733 | 2025-05-21 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 5b318312-2021-33b7-bae7-59bc69e41fec | -12.2943 | -52.4995 | 2025-05-21 00:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| eda78209-0545-309c-b81c-1da9aa9ba8a2 | -12.3137 | -52.4764 | 2025-05-21 00:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| da7ccee2-6086-3e3a-b323-199007096f6b | -11.0903 | -54.7648 | 2025-05-21 00:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 59ac6387-7b18-3972-a5b3-dbd7206ae015 | -20.9601 | -56.5967 | 2025-05-21 00:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 64.3 |
| c58ea32d-af5b-31cb-ba52-bc05460bebfc | -11.818 | -44.2703 | 2025-05-21 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| d5d8a79a-1967-3886-a6d8-0f0ae32b690d | -11.0901 | -54.7852 | 2025-05-21 00:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 120.7 |
| ace3f6d2-2c1f-3b4c-a216-1e2662d95dfb | -11.0714 | -54.7664 | 2025-05-21 00:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 4df4d9e7-44cf-3bcc-a7fc-458b6f0c018f | -12.2946 | -52.4785 | 2025-05-21 00:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 179.9 |
| 4ca199bf-7191-3f2b-9070-0c4580a3efe5 | -18.3335 | -49.8638 | 2025-05-21 00:10:00 | GOES-19 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 67.3 |
| ea839432-8142-3603-9cc4-eaa537f916f1 | -14.1672 | -45.4673 | 2025-05-21 00:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 46.8 |
| b062edf7-a7b8-3a2f-a2e2-cba64c1bf36e | -11.3076 | -53.9683 | 2025-05-21 00:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 2863166c-5dc5-3e31-9425-769a68429694 | -6.2226 | -43.3459 | 2025-05-21 00:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| a6d6ea6a-384c-3ea9-a6cb-dc2d25684246 | -12.4433 | -43.7242 | 2025-05-21 00:10:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| f316ffc9-9871-3d69-949c-87f5dc0ce520 | -12.2756 | -52.4806 | 2025-05-21 00:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| e316857e-08a9-358c-9c4f-09a2f0556e84 | -12.424 | -43.7274 | 2025-05-21 00:10:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 4b3904af-553b-32bf-a55a-bbe0a15cd808 | -12.4433 | -43.7242 | 2025-05-21 00:20:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 3dbea028-b879-3bd2-9116-b8c994dc2c51 | -22.6557 | -47.4702 | 2025-05-21 00:20:00 | GOES-19 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 1742b65e-bc67-3a34-9a0b-7181cf1fef2c | -11.7988 | -44.2733 | 2025-05-21 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 9d178837-8cd3-3d4f-b9c2-c89ee5b6692c | -11.0901 | -54.7852 | 2025-05-21 00:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 0da23f63-f3ed-3bf6-a49c-9b9e7c30de3a | -11.0903 | -54.7648 | 2025-05-21 00:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 96.3 |
| fdf24794-155a-3542-b790-0dcd2d2d9c72 | -6.2414 | -43.3444 | 2025-05-21 00:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| fea9d542-b6a0-3ca9-85a0-986c374c383b | -12.2946 | -52.4785 | 2025-05-21 00:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| d7d06afe-439d-34f1-9b1e-eab37bb05a55 | -11.0712 | -54.7868 | 2025-05-21 00:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| af3b1f37-7abc-374b-8bdd-1951c9b62391 | -6.2226 | -43.3459 | 2025-05-21 00:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 3cb03e5c-4386-3a6a-8d48-3dcb2f0fc943 | -11.818 | -44.2703 | 2025-05-21 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |
| f10886b2-5bee-362c-bdb9-459c4438403e | -12.424 | -43.7274 | 2025-05-21 00:20:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 00f2d5c0-c1c0-30cb-a2b5-75f0a4cb8327 | -9.0291 | -47.7452 | 2025-05-21 00:20:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 97c79857-39db-3222-bc9b-7c208a7173fa | -11.0714 | -54.7664 | 2025-05-21 00:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| c7af82ca-c131-3a2c-bec7-b3e482d16c64 | -14.1672 | -45.4673 | 2025-05-21 00:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 45.6 |
| e57a278f-14e4-37e1-81ef-e960b9b17ca3 | -6.2411 | -43.3677 | 2025-05-21 00:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 278b54ac-d0d7-3258-a8c1-c5fde37cf3f3 | -11.2887 | -53.97 | 2025-05-21 00:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 323b26a8-0f64-3fd3-8027-2736dee3ec45 | -12.4433 | -43.7242 | 2025-05-21 00:30:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| d4c0acec-d583-3a46-8225-edf7a1f928e9 | -12.2946 | -52.4785 | 2025-05-21 00:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 332a48e9-5d82-38ac-bbd5-5dd24c8af225 | -11.0901 | -54.7852 | 2025-05-21 00:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 7192cbc5-3b9c-3da5-ba09-ae6769f3a66c | -12.424 | -43.7274 | 2025-05-21 00:30:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 091115c0-8e85-3b1a-bee2-abeabd7d64f6 | -11.818 | -44.2703 | 2025-05-21 00:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 75.4 |
| e911c308-3d08-3af4-9af7-b0ce2883484f | -14.1672 | -45.4673 | 2025-05-21 00:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 55111020-67a2-3b26-a043-57a3370e7bbc | -11.0714 | -54.7664 | 2025-05-21 00:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 92.5 |


[Clique aqui para ver as próximas entradas](README2.md)
