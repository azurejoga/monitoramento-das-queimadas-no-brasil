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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81e0da6a-2c79-3a97-8615-466c6eb459a8 | -6.1047 | -48.0544 | 2024-11-28 00:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 182a4186-cf07-32bb-abc0-1fc02def84d7 | -2.861 | -46.8406 | 2024-11-28 00:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| d31b0bac-2d6b-39c4-aae3-4d0dbf26ffce | -3.1114 | -53.8041 | 2024-11-28 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| d27b4eb1-741a-3c95-a487-e63bf46313c2 | 1.2537 | -55.9664 | 2024-11-28 00:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 9339da31-8c57-3f52-a011-c48f6e450949 | -1.3145 | -51.9259 | 2024-11-28 00:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 6e1de892-fee6-34a4-a3f7-9d5fb0a534a9 | -3.6963 | -43.4199 | 2024-11-28 00:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 0f347601-b6c1-3f64-bafd-7a9fe61cca47 | -6.1735 | -42.6221 | 2024-11-28 00:50:00 | GOES-16 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 90995b33-d559-3f6f-9001-193e64b84bb0 | -1.5713 | -52.2713 | 2024-11-28 00:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 9d42957a-83df-31a9-9460-aad7831f84e3 | -5.979 | -45.3395 | 2024-11-28 00:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| c0d626ca-40f3-3568-b88a-37993bc96985 | -3.3837 | -50.1125 | 2024-11-28 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 001283ed-48dc-3167-949a-9867d6c1d36b | -2.8794 | -46.862 | 2024-11-28 00:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 1bdf8c33-e18f-319b-b297-5070378b2aa9 | -2.8347 | -54.1125 | 2024-11-28 00:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| e2019629-7bac-3ea5-9944-b4a91765bc53 | -6.1039 | -43.9824 | 2024-11-28 00:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| b440bbf8-988d-3a7b-99d9-42c4b8109791 | -18.784 | -55.8416 | 2024-11-28 00:50:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 45.7 |
| 475e9ab5-b61a-3efe-bc3c-fbf5d89243c9 | -3.9562 | -50.1969 | 2024-11-28 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| c9b23bef-22a8-3dd8-892f-d6538fb97a69 | -2.8795 | -46.84 | 2024-11-28 00:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| a9ffc377-138f-35cc-96a9-a728863350c4 | -4.7907 | -44.4423 | 2024-11-28 00:50:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 2f2f8fd6-cf37-36b5-88ff-1a6d1a52446e | -2.8424 | -46.8413 | 2024-11-28 00:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 74afa5ce-f497-301d-8a57-59edc1ca9a52 | -3.4022 | -50.1119 | 2024-11-28 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 7d171c24-dfd1-31bd-819c-4634ed83fb2a | -4.772 | -44.4434 | 2024-11-28 00:50:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 161.7 |
| b4fde43a-0886-377b-bc0e-afb98a65d076 | -3.1113 | -53.8242 | 2024-11-28 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| d88db5c8-971f-3109-b383-89c6bf21fb82 | -5.9788 | -45.3621 | 2024-11-28 00:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 205.5 |
| bc78f91e-c180-35f3-b339-3e395ab5c785 | -2.5963 | -53.9771 | 2024-11-28 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 48dcde0c-c0ad-33a5-a4bf-878530b37e05 | -4.7908 | -44.4194 | 2024-11-28 00:50:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 20bda9be-0eb0-37fb-b8ef-0f4ae301813e | -6.4474 | -35.0386 | 2024-11-28 00:50:00 | GOES-16 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 66.2 |
| 66ff3f01-817f-3664-8331-a6d2ee3c1e73 | -6.086 | -48.0557 | 2024-11-28 00:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| cc83ec6d-254b-3dcf-894b-4a0971e382e1 | -2.8609 | -46.8626 | 2024-11-28 00:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 69270c46-6266-3038-8f8e-10b1b06dec7d | -6.1048 | -48.0327 | 2024-11-28 00:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 188.2 |
| a8bc45d2-7de2-3ab4-a4a1-c9fa4f2bf2e5 | -2.7419 | -48.9029 | 2024-11-28 00:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| e0bb978e-3f02-3fb7-a18e-244dd59eb40c | -2.7234 | -48.9034 | 2024-11-28 00:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 56faa41a-9a30-3a03-aaa8-524bef325720 | -3.715 | -43.419 | 2024-11-28 00:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 6061fed0-0ca5-3e5a-811d-9f62a5e7e8b0 | -2.8423 | -46.8632 | 2024-11-28 00:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 825ce12e-c130-370f-8f63-b736c1a3b88b | -4.7723 | -44.3976 | 2024-11-28 00:50:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 418bd22b-f087-3a5d-86a1-29cf558724cd | -6.1041 | -43.9593 | 2024-11-28 00:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 8c1cd388-e0e1-32a2-bcae-bb43a503a7ea | -1.3329 | -51.9463 | 2024-11-28 00:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| a117ea96-56f5-3648-815c-c7ffbd73d376 | -1.3145 | -51.9259 | 2024-11-28 01:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 75dfa5a0-2416-3c2e-83ad-9a773e43ab5f | -18.784 | -55.8416 | 2024-11-28 01:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 37.0 |
| faa3dfe5-f12a-379f-a921-6f39ff700d3d | 1.2537 | -55.9664 | 2024-11-28 01:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 72d9908e-0d2e-3408-8c87-cb47cc444633 | -9.9086 | -36.4254 | 2024-11-28 01:00:00 | GOES-16 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 66.9 |
| 378f16f0-31ef-3908-b506-0a81efb2c274 | -2.861 | -46.8406 | 2024-11-28 01:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 1a573571-a36b-3787-9372-167c3968f78f | -2.8423 | -46.8632 | 2024-11-28 01:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 776229eb-4444-3792-86c3-b62ee6a2ef12 | -1.5897 | -52.2915 | 2024-11-28 01:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 210a8ea9-73fd-37b2-9068-98ea7cbf9abf | -4.772 | -44.4434 | 2024-11-28 01:00:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 110.2 |
| f7a5b886-e670-3c19-83a5-cc14bb5472e2 | -6.1041 | -43.9593 | 2024-11-28 01:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 1722e796-7e0c-36af-b038-5db72fe57a5c | -5.979 | -45.3395 | 2024-11-28 01:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 119.1 |
| bf5028ea-1ddd-3dd8-b323-d5c3d32bfe41 | -2.8795 | -46.84 | 2024-11-28 01:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 0a482c30-fe8b-39b8-9d64-1553331fdc49 | -3.9674 | -48.0851 | 2024-11-28 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| a2680641-4ba7-3616-8085-1d3e2e246745 | -4.7722 | -44.4205 | 2024-11-28 01:00:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 240.3 |
| 95122418-d3d5-3949-a093-112bec8d9a52 | -3.4022 | -50.1119 | 2024-11-28 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 96c9edc9-527e-3c33-9bb6-47a92141e191 | -2.8794 | -46.862 | 2024-11-28 01:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 149.2 |
| 29d2e434-835a-36cd-b9e1-8aa47f76d654 | -6.1039 | -43.9824 | 2024-11-28 01:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 48d0498b-5728-3ff6-9d2c-63fe1ae51fa1 | -1.5898 | -52.2505 | 2024-11-28 01:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 131.7 |
| da6d66fe-cd95-39ba-b04f-d4319ab6bc23 | -9.9279 | -36.422 | 2024-11-28 01:00:00 | GOES-16 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 66.2 |
| 9595a6d7-2751-3762-a056-94ecbba46b50 | 1.2537 | -55.9467 | 2024-11-28 01:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 8559d167-64d2-33f2-8ccb-a6538b1e2974 | -1.3145 | -51.9465 | 2024-11-28 01:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 832343b1-af04-307c-85ea-ce5ef3dccbd7 | -2.8424 | -46.8413 | 2024-11-28 01:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| e284965e-3af3-3ea8-bcda-058ac14549dd | -3.9562 | -50.1969 | 2024-11-28 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| b48a755c-8b3c-369d-b640-429636cee6fd | -1.3329 | -51.9257 | 2024-11-28 01:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 31710d2a-a996-38b9-bfb5-ed9fee60b637 | -5.9788 | -45.3621 | 2024-11-28 01:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 191.5 |
| 7631b45f-e43e-3c66-b52d-bd8f4bd5b41b | -3.0929 | -53.8247 | 2024-11-28 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 1fcdd1aa-6a5f-3047-9845-49f5cd92a35b | -18.764 | -55.8444 | 2024-11-28 01:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 35.3 |
| ba638de8-39f2-3a12-a23d-883261018723 | -1.5897 | -52.271 | 2024-11-28 01:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 344.1 |
| 312f7300-e35a-35e7-9bba-99a8cc964d71 | -1.5455 | -46.852 | 2024-11-28 01:00:00 | GOES-16 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 8b8abfe2-a10c-390b-8396-975a91aac176 | -3.1113 | -53.8242 | 2024-11-28 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 109.8 |
| d3a6b6f1-32b0-320f-86db-2232e9b9f0ae | -4.7908 | -44.4194 | 2024-11-28 01:00:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| c0158981-dd6d-31ee-af96-e39b370b15b8 | -2.5963 | -53.9771 | 2024-11-28 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 3348246c-07c0-3d07-9ae3-c38077a7fa0c | -6.086 | -48.0557 | 2024-11-28 01:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 3130525a-6c9b-38e0-8346-7c955c115ff4 | -1.3329 | -51.9463 | 2024-11-28 01:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| b33cd194-a435-3f8e-a2a2-8f7402c84df8 | -6.1047 | -48.0544 | 2024-11-28 01:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 555eab19-37a4-3854-9065-0927aa9e48d1 | -3.6963 | -43.4199 | 2024-11-28 01:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| cf8aa299-070a-3852-81a0-b9baf5d145e7 | -4.7723 | -44.3976 | 2024-11-28 01:00:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 2ed5d68c-d3f5-3814-8cc0-9db13342639f | -6.1048 | -48.0327 | 2024-11-28 01:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 215.5 |
| 3e2314c6-43ed-3f6d-b9f2-11785290dd27 | -3.1114 | -53.8041 | 2024-11-28 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| f5fa2ad1-6273-36bf-861b-05236dc4fea6 | -6.0862 | -48.0339 | 2024-11-28 01:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 187.8 |
| 9da89a1d-6680-3b8d-ba4e-441a5f507f7c | -1.5714 | -52.2508 | 2024-11-28 01:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 77811f83-6eb3-3947-a7b7-e6a6fa226136 | -2.8609 | -46.8626 | 2024-11-28 01:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 155.5 |
| e2ff8742-22c6-304c-8f75-6d5567711afe | -1.5456 | -46.83 | 2024-11-28 01:00:00 | GOES-16 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| ea558ff2-0f9e-3de3-9d40-0d447e540f22 | -3.3837 | -50.1125 | 2024-11-28 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 22457eb8-dc60-3960-a146-35d6556b2522 | -1.5713 | -52.2713 | 2024-11-28 01:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 146f682a-93ec-3d4b-8b04-3e7aa49890d9 | -5.97 | -45.35 | 2024-11-28 01:00:00 | MSG-03 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9b6cd4a9-34e8-3630-845b-702ad67848ee | -1.58 | -52.27 | 2024-11-28 01:00:00 | MSG-03 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90bb747c-9041-3de9-a74e-3070a52bc8da | -6.09 | -48.05 | 2024-11-28 01:00:00 | MSG-03 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 852d715a-56c8-3d4b-b1fb-a12b30ba313f | -2.86 | -46.85 | 2024-11-28 01:00:00 | MSG-03 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44f9fac0-51a4-38fe-bfdf-72460390c4f1 | 1.2354 | -55.9666 | 2024-11-28 01:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| b0f2c3e4-2d7c-38b9-b97e-94337a20bf5b | -6.0862 | -48.0339 | 2024-11-28 01:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 249.5 |
| 24007d18-94e5-38ed-8edc-2cb29b67f2f0 | -3.4022 | -50.1119 | 2024-11-28 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| e3b7734d-8421-366a-956b-51f17b600606 | -6.086 | -48.0557 | 2024-11-28 01:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| a2635ac8-9632-36ee-b5b0-9d63b767c93d | -4.7908 | -44.4194 | 2024-11-28 01:10:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 7883a042-de03-3a49-ad94-d1c4e5fa593e | -1.3329 | -51.9257 | 2024-11-28 01:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 0d3d8faf-1111-3349-9bc0-77598002f769 | -3.3837 | -50.1125 | 2024-11-28 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 127.3 |
| 460b44f2-9778-3cee-8e7e-3929343fccba | -1.5897 | -52.271 | 2024-11-28 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 331.3 |
| 8363eee9-5070-3ad1-ba29-c55720d0109c | 1.2537 | -55.9861 | 2024-11-28 01:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 394b86b3-3618-36d3-886b-9d3c83a9d5aa | -4.7722 | -44.4205 | 2024-11-28 01:10:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| b6ccf00d-a053-3a9e-b288-d50f81af5869 | -2.8423 | -46.8632 | 2024-11-28 01:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| fba6006e-f2c7-34c1-97cf-a93ee984ec3e | -3.093 | -53.8045 | 2024-11-28 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| aa4c7d9f-6bcd-3923-bd16-39896af4891a | -1.5714 | -52.2508 | 2024-11-28 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| f4f12293-955d-3527-b9cc-33223308f159 | -3.9674 | -48.0851 | 2024-11-28 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 423b26f0-8986-37e3-ac9a-0c0d2fdc2b65 | -1.5713 | -52.2713 | 2024-11-28 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 154.1 |
| 8d754395-b3f5-3273-b03d-1162fd47c51c | -9.9279 | -36.422 | 2024-11-28 01:10:00 | GOES-16 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 89.8 |
| 3e98d1b0-9268-31a9-b3d7-c68f347aa9c2 | -2.8424 | -46.8413 | 2024-11-28 01:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |


[Clique aqui para ver as próximas entradas](README20.md)
