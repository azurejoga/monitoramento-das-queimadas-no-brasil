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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f7713c2-6d36-39fa-bd5b-37e4a554a5f0 | -4.7722 | -44.4205 | 2024-11-28 01:30:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 70fa6d4f-7b90-36d2-a9ec-8b621de808c4 | -2.5963 | -53.9771 | 2024-11-28 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| b06047d3-c88d-3351-be48-444942d071da | -3.3837 | -50.1125 | 2024-11-28 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 6c77ef86-562f-3182-9f94-9f3c683ac819 | -2.8424 | -46.8413 | 2024-11-28 01:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 9e1fa485-6455-3054-9c31-505d54897c37 | -6.0862 | -48.0339 | 2024-11-28 01:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 6f4eed53-0ee6-35e4-8e71-610ee5df5f7f | -1.3329 | -51.9463 | 2024-11-28 01:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| c926b92f-8dc8-3c28-93cc-5e67fe51382e | -3.093 | -53.8045 | 2024-11-28 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 2be6395d-2e5c-3a0f-b35b-d87b8d2d1622 | -4.772 | -44.4434 | 2024-11-28 01:30:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 9fc942ea-972e-356a-85cb-4572da8d4b08 | -21.0803 | -49.8023 | 2024-11-28 01:30:00 | GOES-16 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 53.3 |
| be368c62-45ec-387e-9fc3-1bbfed9864b0 | -1.5897 | -52.271 | 2024-11-28 01:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 166.1 |
| 180bb7de-5631-3ecd-b0c0-dc4f83977c4d | -5.9788 | -45.3621 | 2024-11-28 01:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 183.5 |
| 3a769efd-8028-375c-a7ac-9766dd9224e7 | -3.9747 | -50.1962 | 2024-11-28 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 9d2cb623-158b-3198-a97f-463ede9310c2 | -3.0929 | -53.8247 | 2024-11-28 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 7fea12b2-6c90-39c9-b07b-e3ca984bca75 | -1.6812 | -52.4946 | 2024-11-28 01:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| e347ad71-88aa-3dfc-b920-1e3d6a835b56 | -2.7419 | -48.9029 | 2024-11-28 01:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 084d08a1-c6f8-3a70-808b-1ab80bfcd94a | -2.8795 | -46.84 | 2024-11-28 01:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| d65a0087-6315-3e3c-82f9-74fe41fa5525 | -2.861 | -46.8406 | 2024-11-28 01:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 39d8d11a-1f18-3fbf-8c64-13bbc0ae2721 | -6.086 | -48.0557 | 2024-11-28 01:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| e2034690-3a3c-3e40-a91f-4dae665f0d10 | -1.2812 | -51.951801 | 2024-11-28 01:39:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ebf93cc-b981-30cc-9e0d-cd5a5060cc98 | -17.5938 | -57.579601 | 2024-11-28 01:39:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5ddeba88-532b-37cb-bbf9-79edb8a30cae | -1.5502 | -52.311298 | 2024-11-28 01:39:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13c5822c-4d19-3595-93d0-693da123359c | -16.1201 | -59.624001 | 2024-11-28 01:39:00 | METOP-C | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7112a610-085c-33d9-864e-554b4fe1ea8a | -1.6154 | -52.497398 | 2024-11-28 01:39:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1025e531-7c11-37ac-9742-a222fa760881 | -17.5979 | -57.5966 | 2024-11-28 01:39:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 28fc97d5-1105-3141-93dd-0c41e8dfcdfb | -18.7283 | -55.8563 | 2024-11-28 01:39:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7d747d1a-f2c0-31ad-bae7-ccaced928728 | 1.3038 | -55.965401 | 2024-11-28 01:39:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ba31249-87e9-37da-8912-8d9cc92c4b52 | -1.5407 | -52.313599 | 2024-11-28 01:39:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 313fdf17-a0f2-337a-8b0b-4ffeaa723467 | -18.730801 | -55.866299 | 2024-11-28 01:39:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 47438ad9-a14e-3761-a15a-0200148c25a9 | -17.586201 | -57.590698 | 2024-11-28 01:39:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7e419448-3260-3bfd-9967-21a97bc293ad | -18.7258 | -55.846199 | 2024-11-28 01:39:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 44eede41-7947-34e3-a6f2-9dec70f3bbf9 | -21.5625 | -57.502399 | 2024-11-28 01:39:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e23e72c8-50e8-3640-9e70-77a2526f61b3 | -17.5882 | -57.599201 | 2024-11-28 01:39:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f6c8e2bf-20ff-396f-ba20-97b57d796e72 | -3.0577 | -53.827301 | 2024-11-28 01:39:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30875db1-eb0d-303f-92e4-54bc3493b5af | -16.0383 | -60.121498 | 2024-11-28 01:39:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c6cf7b3f-3d57-35d7-a473-5f2449396184 | 1.2891 | -55.941101 | 2024-11-28 01:39:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7871873-6950-32f7-9ea7-7060249a5b0d | -1.5329 | -52.2813 | 2024-11-28 01:39:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e835cc3d-340b-3a7c-878e-3e6a7892d57a | -16.035 | -60.107101 | 2024-11-28 01:39:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6ca10721-a1e7-39a7-95bb-32099562221e | 1.3618 | -60.416698 | 2024-11-28 01:39:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9eb27c6f-dad2-3af5-908b-78d02f19105c | 1.2895 | -55.983101 | 2024-11-28 01:39:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d24ad4cc-018e-340b-82a4-fb88ae883a37 | -16.118401 | -59.6166 | 2024-11-28 01:39:00 | METOP-C | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6941aa07-d9a3-3e48-90f3-fe28a5d55b6d | -16.082701 | -59.6409 | 2024-11-28 01:39:00 | METOP-C | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 124d5124-60da-31d9-b97d-ac137aae3cfe | -2.7961 | -54.138302 | 2024-11-28 01:39:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56d78fd5-c023-33c0-85ff-bb6c6e24654d | -3.8701 | -53.6819 | 2024-11-28 01:39:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4608089-07aa-31e0-8c1d-957d40346fb4 | -1.6346 | -52.492802 | 2024-11-28 01:39:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14ad9aba-42d3-3924-ba12-2a28ee1f551f | -16.0296 | -59.7239 | 2024-11-28 01:39:00 | METOP-C | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7f681d24-3b70-3f55-819c-6f9fa501d68c | 1.3089 | -55.987499 | 2024-11-28 01:39:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e69b3bbf-1566-313a-b904-0408898c4058 | -18.7381 | -55.8536 | 2024-11-28 01:39:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9a42a5e8-de83-370b-a1e4-58ebe0eb8435 | -1.5424 | -52.278999 | 2024-11-28 01:39:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27345425-9f08-3d3c-97d4-ae5526178d36 | 1.2941 | -55.9632 | 2024-11-28 01:39:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0c27fc6-68f5-3f3c-ba11-f86b434bd12b | 1.941 | -55.762001 | 2024-11-28 01:39:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67f9d5af-71d0-3c84-bf8a-686cca5ab29e | 1.2987 | -55.943199 | 2024-11-28 01:39:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1329261-6d3e-383f-b521-9ccfbad33e29 | -16.027901 | -59.716599 | 2024-11-28 01:39:00 | METOP-C | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 170b94c0-c77c-3125-82ee-0a7fb8995e93 | -1.625 | -52.495098 | 2024-11-28 01:39:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 716fba3e-3f9f-3533-a135-b389b60e83d2 | -2.5577 | -53.997101 | 2024-11-28 01:39:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ad4e23a-a46e-3175-8597-4510a112df2b | -16.0844 | -59.6483 | 2024-11-28 01:39:00 | METOP-C | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e7b7e2f9-0753-3a9f-b6a9-b202c889e5d1 | -3.0635 | -53.8512 | 2024-11-28 01:39:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e12e7fc4-9901-3891-9e9b-fedc5ed1d2b9 | -3.048 | -53.829601 | 2024-11-28 01:39:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0750ee20-c89e-3a0f-9c5b-466853f61893 | 1.2992 | -55.985298 | 2024-11-28 01:39:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e201c46-09cb-371e-a957-9964b40b1bf4 | -2.5481 | -53.999401 | 2024-11-28 01:39:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7085d530-0082-35ef-89ac-6d1913aa58a0 | -21.5644 | -57.510399 | 2024-11-28 01:39:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 8aeb6744-e1b8-3895-9804-0812bb96b834 | -2.7864 | -54.140598 | 2024-11-28 01:39:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33fdd2d4-1b45-31fe-9bd5-d4b54ae04493 | -2.1015 | -54.8606 | 2024-11-28 01:39:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48311730-5595-3429-8584-441fbf8cf6e3 | -16.036699 | -60.1143 | 2024-11-28 01:39:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e27c8707-1112-3cd8-bdc7-c11aeee4bf25 | -2.0965 | -54.8395 | 2024-11-28 01:39:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b72c11cf-64e4-37f8-93e7-2602ed4be7f3 | -17.5959 | -57.5881 | 2024-11-28 01:39:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fe510f24-9701-3275-8956-d4b164a6871a | -3.9674 | -48.0851 | 2024-11-28 01:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 0f53fe44-a786-3aa3-a29c-3f2e4636f6f4 | 1.2537 | -55.9467 | 2024-11-28 01:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 3b3fbc57-3339-3103-98b6-9d22b929b69f | 1.2538 | -55.927 | 2024-11-28 01:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 719f2b34-6e54-3739-a21b-af249bcd2fb7 | -5.9788 | -45.3621 | 2024-11-28 01:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 202.5 |
| 3ed329a6-65bd-3c36-b5bc-cb3fc18bf2e6 | -6.0862 | -48.0339 | 2024-11-28 01:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 9ebed797-69e3-30cf-8d48-52ba37ad7e0f | -3.3837 | -50.1125 | 2024-11-28 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| f313ddd9-020b-31b4-ada6-85ff438ab453 | -1.6812 | -52.4742 | 2024-11-28 01:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 12eefd45-ccae-3509-9814-3929120699b4 | 1.2354 | -55.9666 | 2024-11-28 01:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 1284e2ea-7f58-3fd0-ba32-a00e375e8a5d | -2.7419 | -48.9029 | 2024-11-28 01:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 7eba0c33-dd03-3188-bd74-0409eae9d14a | -1.6445 | -52.4543 | 2024-11-28 01:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| bcdb078f-5acb-3d4a-bd70-ef3d73e4c86e | 1.2537 | -55.9664 | 2024-11-28 01:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| a7cc0f40-79e2-313f-bc8e-6270abc320c7 | -4.7722 | -44.4205 | 2024-11-28 01:40:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 140.6 |
| eb2a517f-ce49-3238-9cad-d4a56fbe7e5d | 1.2354 | -55.9469 | 2024-11-28 01:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 31fe38d0-b1c1-3abc-9e5a-a05b577f3f11 | -6.1039 | -43.9824 | 2024-11-28 01:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 1b40dae8-4fb1-3847-bc64-82cbc07c55a5 | -4.772 | -44.4434 | 2024-11-28 01:40:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 4c793a06-6412-3637-8989-2bfd80b63bac | 1.2355 | -55.9272 | 2024-11-28 01:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| a6a286cb-f0aa-3227-b599-cf2cbe81da8e | -2.8794 | -46.862 | 2024-11-28 01:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| dc790872-d91a-3fc9-99f3-babf9b61dc01 | -5.979 | -45.3395 | 2024-11-28 01:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 86f27060-c862-3398-b2f1-f3b74c7a389f | -3.4022 | -50.1119 | 2024-11-28 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| b5995458-ca28-390d-948a-c098c047cc14 | -6.1048 | -48.0327 | 2024-11-28 01:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| caf99434-4329-360f-bdfa-0d12a91ad7e6 | -1.5713 | -52.2713 | 2024-11-28 01:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 84989b18-33df-3f11-9e08-d7a7dfa5f163 | -3.1113 | -53.8242 | 2024-11-28 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 7386dc78-607a-373c-a553-dbde40ce2068 | -3.3311 | -45.5129 | 2024-11-28 01:40:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 50.7 |
| db984878-f2de-34ce-9346-5e7783232609 | -2.8609 | -46.8626 | 2024-11-28 01:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| b03ba8f0-061d-384b-b95b-d91a258b43e6 | -2.861 | -46.8406 | 2024-11-28 01:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| ef9d5368-4d6e-316c-beb3-cae61221a1d2 | -3.1114 | -53.8041 | 2024-11-28 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 6c069e5c-a336-30b2-9055-bf71224b2cf2 | -1.6445 | -52.4747 | 2024-11-28 01:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 57027909-b417-3935-9ace-c7f6574fd1f1 | -1.5898 | -52.2505 | 2024-11-28 01:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 1afe769b-baa3-3848-9e3b-f6b4c9a0ed0e | -2.7234 | -48.9034 | 2024-11-28 01:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 2df3d8b1-c1b8-340c-8c82-678849baa487 | -1.5897 | -52.271 | 2024-11-28 01:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 173.6 |
| ee3c6999-9bbf-397b-977e-db760ff90a43 | -6.1041 | -43.9593 | 2024-11-28 01:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| fa8c92c2-75cb-3ba9-9db6-e3f4422520b2 | -2.8795 | -46.84 | 2024-11-28 01:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 3ae10c41-0dfe-3c30-9fee-1dafe458dadf | -1.6812 | -52.4946 | 2024-11-28 01:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 43ba6d0b-6971-3a9a-9676-18491195f626 | -3.3312 | -45.4904 | 2024-11-28 01:40:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 5652392c-f154-3218-855d-a37f355144f0 | -1.3329 | -51.9463 | 2024-11-28 01:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |


[Clique aqui para ver as próximas entradas](README22.md)
