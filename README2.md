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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 506ba104-d6ed-3379-b4d0-066d1d793820 | -4.37934 | -43.33844 | 2025-12-01 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 88c8f756-fae8-3aba-ac0f-45f97d423233 | -2.74302 | -49.33673 | 2025-12-01 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5259640e-32e5-3ee7-bd85-934c61af516a | -4.19518 | -40.64596 | 2025-12-01 00:13:00 | TERRA_M-M | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 16.2 |
| ced5c0c2-c98d-3b01-b46b-dd001cb723b7 | -2.04389 | -52.09895 | 2025-12-01 00:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| d57fe0c0-d286-38b6-99c2-0fca4e9e9cb5 | -3.30397 | -43.481 | 2025-12-01 00:13:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 41.6 |
| aa148cc8-507e-3ea0-9496-4e7406ad7570 | -2.2848 | -47.40814 | 2025-12-01 00:13:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| ba493d4e-d956-36ee-847f-78ccfe1f1856 | -4.39042 | -43.3476 | 2025-12-01 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 0df9881a-1112-3d39-aa84-edab2a788864 | -2.26953 | -45.70225 | 2025-12-01 00:13:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 16.1 |
| a5c50496-e3c3-332d-b559-fa05a9fc1ae3 | -4.76233 | -40.50808 | 2025-12-01 00:13:00 | TERRA_M-M | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 14.6 |
| cccc20b0-2fb6-3dda-8ae7-bbe5ae7c2098 | -3.35764 | -46.09628 | 2025-12-01 00:13:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 830a835f-65a3-3520-88b1-37e70574b2d1 | -3.20989 | -50.14206 | 2025-12-01 00:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 7fd2f4fd-51e8-3f6a-829d-191cfa69e3e7 | -3.20815 | -50.1292 | 2025-12-01 00:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 4db15eef-d368-3748-9550-318b534e062e | -2.65898 | -46.97731 | 2025-12-01 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 79a0be0d-1dac-3ead-a223-e58ec7efa0cf | -2.04634 | -52.11654 | 2025-12-01 00:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 2b595daa-0176-32d7-85e5-3dcd45225dc6 | -5.70714 | -45.63374 | 2025-12-01 00:13:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8fae66db-5010-3240-b673-f408bc3ed0eb | -2.26065 | -45.7035 | 2025-12-01 00:13:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 51297925-d539-3a43-8d18-4f7f1b54403f | -2.28604 | -47.41721 | 2025-12-01 00:13:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 40b79785-46c6-3bf6-9874-c87dea14cf3a | -2.63377 | -48.53972 | 2025-12-01 00:13:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6916fff8-fcf8-3fb6-8233-1420b7c202d7 | -3.50137 | -43.77804 | 2025-12-01 00:13:00 | TERRA_M-M | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 22457011-3a78-372e-8b76-eefa4b6ed205 | -4.58301 | -45.97018 | 2025-12-01 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 14.6 |
| d3783301-bd52-3558-a2e5-b4d9786e72b1 | -2.05044 | -52.10949 | 2025-12-01 00:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 3649685a-183f-303f-b9d5-93b80edc1d91 | -3.32681 | -42.4962 | 2025-12-01 00:13:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9f531637-106c-31a9-9341-d08bafc1eb4f | -4.03506 | -46.73955 | 2025-12-01 00:13:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ff20451e-4f9c-3590-87e1-c3a6892cc7d3 | -3.23467 | -50.24509 | 2025-12-01 00:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 6ed82721-f816-39ce-bb6d-c97df6471608 | -6.67015 | -39.89709 | 2025-12-01 00:13:00 | TERRA_M-M | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 12.4 |
| c03c3f84-17b8-3bd0-8cb1-b60e6afb892e | -2.25943 | -45.69462 | 2025-12-01 00:13:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5c019c5b-9a2e-3751-a8fc-e6e81e284783 | -3.22047 | -50.14066 | 2025-12-01 00:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 7fecd7dd-efb8-3b76-a570-c9a0e36f6908 | -3.03992 | -50.24374 | 2025-12-01 00:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| fdee9030-ddcc-3e08-81e7-ef23d383df06 | -5.87113 | -44.5007 | 2025-12-01 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cb8dc047-b41f-3def-88b7-3df5dda8eb01 | -4.30703 | -45.37367 | 2025-12-01 00:13:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7ee76468-aa05-3f79-9b18-c7da685661b8 | -4.37443 | -43.16627 | 2025-12-01 00:13:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 0ecb6439-2231-3307-bd55-75644ba63e25 | -2.83734 | -48.8247 | 2025-12-01 00:13:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ecfd463a-ba60-3e2c-ab25-a0d952b2aac6 | -3.70762 | -45.89721 | 2025-12-01 00:13:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 3a72c235-cd19-366f-8dc7-5b436a0eaffe | -3.3606 | -50.49533 | 2025-12-01 00:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 0182c6d9-62b2-3a91-a904-702ceb93e2bd | -2.38645 | -47.61108 | 2025-12-01 00:13:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| f4d0d0d6-65b4-366d-8da1-556c697e0efc | -6.31904 | -43.81956 | 2025-12-01 00:13:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 65cfcd7f-e84b-32a1-bfba-30fd30669b33 | -2.24544 | -46.51938 | 2025-12-01 00:13:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bddd0320-1b71-323a-bde4-65b4bb295453 | -3.42088 | -45.16237 | 2025-12-01 00:13:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 848998c6-b441-377e-8026-cd28df5aa9b8 | -4.38743 | -43.32662 | 2025-12-01 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| a7a363c6-3914-36b1-9ef6-50811b96ba95 | -2.45106 | -49.00518 | 2025-12-01 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 832c7a1a-153a-3e84-95ac-33fde6c64a97 | -3.44437 | -50.15789 | 2025-12-01 00:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 76fca695-fd2f-359c-8e32-9019575daec3 | -2.64459 | -48.54853 | 2025-12-01 00:13:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 32ed5af3-6c35-371a-800e-66a4f7d29fdc | -2.25055 | -45.69587 | 2025-12-01 00:13:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 36.0 |
| be7bafdb-571e-3e75-9f78-496c46ec483c | -3.62838 | -44.34102 | 2025-12-01 00:13:00 | TERRA_M-M | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 109f4257-dd19-3014-ac19-3bdb67ae8287 | -2.95598 | -45.40209 | 2025-12-01 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 21.0 |
| b3b6884b-3707-31b8-816c-192b128dca73 | -4.30827 | -45.38255 | 2025-12-01 00:13:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 7fd4ca81-1411-31e5-a836-10fb4c21d7d1 | -6.30988 | -43.82091 | 2025-12-01 00:13:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 999b55cf-093d-3788-a8b2-040627bb711d | -3.50645 | -43.3309 | 2025-12-01 00:13:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| ab1b421a-3493-37f4-a297-bc66a4cba1ab | -2.60039 | -49.25983 | 2025-12-01 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 5a4a5c17-e5ae-39c6-97c8-6a609aab47ec | -3.27193 | -44.17445 | 2025-12-01 00:13:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3abd9931-38c0-3bb8-a02c-c32b10e4c6c7 | -3.67068 | -48.93898 | 2025-12-01 00:13:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1c21be9a-0cc7-3917-8a80-3f815a9f56b0 | -3.4842 | -45.68036 | 2025-12-01 00:13:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ab144ac0-b2d5-35a3-97aa-5d3d23f2a1c5 | -4.38084 | -43.34898 | 2025-12-01 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 7b6924ce-444f-3197-be4a-b0c352e18c9c | -3.30247 | -43.47043 | 2025-12-01 00:13:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4dd4e0e5-59b7-3041-8d25-65b0a38ba7ff | -3.21515 | -41.57437 | 2025-12-01 00:13:00 | TERRA_M-M | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| e43a148f-2f80-3fcd-87dd-2cc9b038b86a | -2.44209 | -47.08067 | 2025-12-01 00:13:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| d70e951d-427b-397f-8cc9-6c914bf82234 | -3.23645 | -50.25816 | 2025-12-01 00:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| fb48d41c-4d82-32cb-8f53-e661ec488e41 | -2.94272 | -53.29695 | 2025-12-01 00:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| a5a2e3cc-d82c-3f60-96fb-00ef32f83893 | -3.93847 | -45.84354 | 2025-12-01 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 1ff6d05a-d37e-3147-9ae4-579545e9d594 | -4.27183 | -46.71535 | 2025-12-01 00:13:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 804c534a-31d8-3b92-980a-4d6e407f5e13 | -3.44082 | -44.11409 | 2025-12-01 00:13:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| bcabedeb-d8a6-3734-a525-90a40878ecd4 | -2.92071 | -45.27897 | 2025-12-01 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 12.9 |
| e161531d-e08c-384d-b9d1-e4ed54c4412b | -1.99832 | -46.5367 | 2025-12-01 00:13:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8e0fee75-9a79-3bc8-ba21-9748a6ea5081 | -3.50282 | -43.78817 | 2025-12-01 00:13:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 8b448e5c-f8b4-392c-bfa5-4f1032ae4396 | -2.61164 | -47.77559 | 2025-12-01 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2e75f19f-817c-37e2-b3c3-31bdc8fc2f40 | -3.50026 | -44.21882 | 2025-12-01 00:13:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1db0b6c9-d627-3cbc-aa3f-eea3844e9961 | -2.75201 | -45.2599 | 2025-12-01 00:13:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3075491a-0088-38fc-a0ba-4b0d1e2399e1 | -3.66863 | -47.29127 | 2025-12-01 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 297f7a1d-8de1-3c93-b63f-900636d1f987 | -6.31768 | -43.80996 | 2025-12-01 00:13:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| af064846-2867-3825-8285-41c199a5f9ad | -3.60103 | -47.26957 | 2025-12-01 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| b09388b2-384b-383a-82b4-3f11ac1391b7 | -4.25377 | -44.33499 | 2025-12-01 00:13:00 | TERRA_M-M | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5daee646-5b7f-30ec-adf1-0a3aeb708b0e | -2.24834 | -45.61452 | 2025-12-01 00:13:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 82.9 |
| a0651cd0-5c69-3a1b-adea-32bd8ac4767b | -3.59203 | -47.27079 | 2025-12-01 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| ddc54bb4-6900-3070-90bd-bf3128b40b63 | -3.1986 | -45.54925 | 2025-12-01 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f0295754-abf9-3464-a82e-de613837849e | -3.75182 | -42.95787 | 2025-12-01 00:13:00 | TERRA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 4b41d189-14e4-3db0-a27a-e94d57783390 | -4.58422 | -45.97897 | 2025-12-01 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 25.6 |
| abdbcceb-3261-329b-b672-ddd928c318e0 | -1.61594 | -46.90723 | 2025-12-01 00:13:00 | TERRA_M-M | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4cc703ae-9903-3076-b1a6-5cbe1ea2977d | -4.38234 | -43.35946 | 2025-12-01 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4eff3d28-2224-30f6-98fd-6fc90734df8d | -3.44877 | -50.15025 | 2025-12-01 00:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| e03e2ace-1429-34a3-892f-af6d582b365c | -2.49374 | -49.00437 | 2025-12-01 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d901b30c-0aec-3aea-912d-8d972e5994a5 | -3.16001 | -45.47935 | 2025-12-01 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0d5802dd-7dbc-331c-887a-f3e86c40376e | -2.73464 | -49.34935 | 2025-12-01 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e2b4a165-951b-3345-8422-d8c726162903 | -4.39702 | -43.32527 | 2025-12-01 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 625f413b-afc3-3cd5-93da-03c13e9c3afb | -2.1714 | -46.4555 | 2025-12-01 00:13:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1c232b70-d39d-3f45-ae1f-38af9bc25418 | -3.47858 | -44.91663 | 2025-12-01 00:13:00 | TERRA_M-M | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 229487de-0e11-36b5-ba57-e7e8db5cfd3e | -2.44806 | -46.32664 | 2025-12-01 00:13:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 18.7 |
| b545bef5-29a7-3004-a464-8a74f7027873 | -4.14845 | -43.72524 | 2025-12-01 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f75d4e63-e9dd-3f2d-ab20-bc52e79b7d34 | -2.24069 | -45.62469 | 2025-12-01 00:13:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 917ecb58-939e-3411-8cdf-c73866752b38 | -2.44332 | -47.0896 | 2025-12-01 00:13:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 85020d25-1268-32e4-95c8-2b40e1d05e69 | -3.62705 | -44.33147 | 2025-12-01 00:13:00 | TERRA_M-M | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1445a95d-5a8a-390c-83a7-4bdb455c20e0 | -3.18121 | -45.42465 | 2025-12-01 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 102de6e6-ec62-3313-aad8-414c11e20f6d | -4.3985 | -43.33574 | 2025-12-01 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 6f5adc19-a2b8-36b7-a926-9eaf1f9d61b2 | -3.70001 | -45.90725 | 2025-12-01 00:13:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fe0324a5-ff48-31ea-9e89-cc508cf8a786 | -5.48942 | -42.16782 | 2025-12-01 00:13:00 | TERRA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| c5610570-897c-3399-af48-c05fb3c5e252 | -2.44045 | -46.33666 | 2025-12-01 00:13:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5f8ab727-51d8-3541-80fa-f6c7cf8c4e5b | -2.6602 | -46.98623 | 2025-12-01 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 83c09c26-5099-33e9-b9fb-58028f5bfb88 | -3.44265 | -50.14479 | 2025-12-01 00:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c3dcc1c0-79f7-3932-a88e-27dba56cf53d | -4.40936 | -43.99797 | 2025-12-01 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 2769532c-f0a8-3b84-8c48-003163fb90b5 | -2.48951 | -47.82749 | 2025-12-01 00:13:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b54aa0c2-5e3f-3f14-bed4-832526111b06 | -2.93637 | -53.29135 | 2025-12-01 00:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |


[Clique aqui para ver as próximas entradas](README3.md)
