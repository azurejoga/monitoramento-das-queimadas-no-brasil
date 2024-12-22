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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81a87d99-8bdb-392b-8702-13675e787acd | -2.64676 | -46.91654 | 2024-12-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dc2274eb-3878-3a19-a889-8374967763c4 | -3.93569 | -46.44128 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c2d792c-e776-3d3c-933b-c57fe425ef48 | -2.64841 | -46.10101 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c232d57-ce73-37cc-a803-8fcb4dcc15f8 | -2.37943 | -47.66144 | 2024-12-22 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e53064dc-7053-34fc-994c-a107e59a10ef | -2.67991 | -54.84284 | 2024-12-22 04:25:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f3aa8a4-c3ba-3c2e-9a91-14f8c0ed0d92 | -3.08615 | -46.56394 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbb8210e-cdb7-302b-9045-eceb6ec92ef6 | -4.72862 | -43.25462 | 2024-12-22 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1e3c0a8f-4ba8-3117-add9-a5eda0a01ef5 | -3.92486 | -46.89913 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a14e215a-37b1-317b-b135-fcb0e1f7e515 | -1.91165 | -45.54931 | 2024-12-22 04:25:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4db8496-0cf5-3395-b4ef-244f8cebb5d5 | -1.37483 | -53.7057 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 08cb316e-d796-3f42-9a4d-8f453ee4ad4e | -3.78596 | -47.11231 | 2024-12-22 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 487afb9c-d52a-3c1b-b809-9bd6d26480e1 | -3.49892 | -42.33236 | 2024-12-22 04:25:00 | NOAA-21 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 8921e739-02da-3f15-bb62-2649d40e5299 | -3.67908 | -47.16494 | 2024-12-22 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e369b967-4889-3457-adc8-4ae92f977e12 | -3.08337 | -46.55996 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf55f594-157b-337b-8758-287198bee66f | -2.55448 | -46.93498 | 2024-12-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5ef5101-6897-33fc-8251-61b98084cbc0 | -4.0836 | -46.79887 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 57d7242d-4b08-30b7-be86-27caf8d579a3 | -3.99334 | -46.54944 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b2ea2c0-5b10-3d9a-a5c6-a9508412cd32 | -3.92655 | -46.91014 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca329347-a3d4-31b9-8462-b24e3de57b3b | -3.881 | -47.02568 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59501bb3-add6-3288-8346-96669c590314 | -2.49334 | -49.05048 | 2024-12-22 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ec476f1-ba3b-3205-a0db-03dedbeafb16 | -2.39159 | -45.45922 | 2024-12-22 04:25:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4610bbc1-f894-31c6-8d57-0bcc2df027cb | -2.57667 | -49.47723 | 2024-12-22 04:25:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14192627-3708-38d2-a5d8-1344ddd74a0a | -4.03651 | -46.79514 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae5b568e-63cb-3bf9-bbb6-3dccdb083c4d | -4.03802 | -46.69904 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 57a1f4b1-f339-3959-ae88-66aa529dd125 | -3.91749 | -46.36058 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe591ce0-b795-377b-af24-28d456efa3d3 | -1.15596 | -46.75079 | 2024-12-22 04:25:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f044df27-90b3-3c70-afb4-b298144d6e9d | -2.61741 | -47.46635 | 2024-12-22 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 123d3951-3b93-365e-a8d5-7a62715840a6 | -3.87126 | -46.59077 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc8b9ae4-93f4-3313-a1b2-07d860595d1f | -3.99053 | -46.74109 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 366e0909-289a-3901-8715-a69a60edcb51 | -4.08305 | -46.80238 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3eebf430-1680-38f3-9faf-5c5a56e28033 | -3.98114 | -46.90839 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a357a092-199c-3479-832d-a68509248ed0 | -2.65064 | -46.10841 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7770de3-df4c-3ae9-b96f-6ad1429b7d58 | -1.41146 | -46.48528 | 2024-12-22 04:25:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b0811aab-bc4d-3017-b70b-649b7e04b268 | -3.9821 | -46.68627 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8960197-cae0-3f18-a642-22fa2345af58 | -2.68179 | -54.8446 | 2024-12-22 04:25:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9bde5b41-e485-3012-a359-18f05d63473b | -1.71513 | -46.21753 | 2024-12-22 04:25:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b57bb98a-0cdd-332d-bf80-4b8cfe925413 | -4.10282 | -46.74127 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| abdf7dbd-62f7-3c42-851d-9059b89d8826 | -3.17536 | -46.25474 | 2024-12-22 04:25:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 51c4fa85-8c2f-32a7-91ff-713ac9264328 | -1.7129 | -46.21007 | 2024-12-22 04:25:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c53a9595-b028-34bd-a5ec-fab2ca8b9ba5 | -4.01279 | -46.90251 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cdb18620-a958-3b6a-b01d-46db9ece5c98 | -2.04952 | -46.34102 | 2024-12-22 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6dbf0c85-6efc-39dc-a10f-9a2b53951d86 | -2.68715 | -54.84543 | 2024-12-22 04:25:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7a3c77e7-b8e4-3eba-97b4-99e3089276bb | -4.0149 | -38.81331 | 2024-12-22 04:25:00 | NOAA-21 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 06a1e32a-dc61-3bf2-aad5-6df641ef5e8b | -2.97305 | -48.08177 | 2024-12-22 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e645503-0d36-3288-a46c-ea84c470ee25 | -2.66615 | -54.87319 | 2024-12-22 04:25:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d9e40306-b5b4-3052-8b01-6feb1784e0fb | -4.20045 | -47.54016 | 2024-12-22 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a500405-945b-3ef9-bbec-1199b8f9a093 | -2.64733 | -46.10789 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 569c6b83-8720-3a6b-97c6-d02779f19c8c | -4.56241 | -43.30009 | 2024-12-22 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ad1a747e-1ae3-32d3-b774-1ead18199498 | -1.82481 | -46.53863 | 2024-12-22 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 109b0658-c424-3ba8-8fa3-c7dd7278f0ff | -4.00274 | -46.55442 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f39d00a-66e9-3465-8475-44130a5c2732 | -4.39717 | -39.90701 | 2024-12-22 04:25:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e7ab3ef2-a24f-3b5b-8542-f46721699a72 | -4.09084 | -46.81796 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbebae06-3520-358a-933d-869acb0da474 | -4.02403 | -47.04828 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 083ef1d6-4ed8-3066-8592-55cc25d8c69b | -3.99665 | -46.54995 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 033b4629-53b5-3c8a-ac39-d5e6a3638377 | -3.90885 | -47.001 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa646ae5-683e-3d20-b6a3-e5a6e3c29107 | -3.7854 | -47.11585 | 2024-12-22 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b750ce5c-3daf-3d9d-92fb-1b30a0564c19 | -3.90829 | -47.00454 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8990af28-0db7-3659-b975-28f5bc8fa8b0 | -4.05204 | -46.80467 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1457bc5c-5f6c-38a1-aada-64cd58a6b6b5 | -2.16088 | -48.44833 | 2024-12-22 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22b15a26-84c3-3d43-8077-4ee7206d6229 | -1.41189 | -52.03764 | 2024-12-22 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1f1baeff-7284-36da-a900-4900d53f7dd5 | -4.01624 | -47.05428 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9607f868-64cc-3de0-afb4-77a6b3a0352b | -4.0995 | -46.74075 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 611dce37-d10e-3297-bf8a-d9a45751f6ac | -4.1023 | -45.30663 | 2024-12-22 04:25:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d1c7398-46d3-3564-a06b-008e1618d986 | -4.0205 | -46.09466 | 2024-12-22 04:25:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5e53b7d-7bb4-3b85-a976-183e637e6b9a | -1.36797 | -53.69021 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 75f0471c-4868-3c9d-bb57-e0efe21ac70e | -2.00371 | -46.43756 | 2024-12-22 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e2d4a48-00af-3bfb-90a8-2d5a84baf0d4 | -3.92652 | -46.88862 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 826eede2-1df7-36de-a37e-c4a86583bf36 | -3.9271 | -46.90664 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f81eff3-0a95-37dd-b204-ba55f03b503c | -2.64769 | -46.77902 | 2024-12-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f068339c-c117-33b1-83ff-c722e03ab233 | -3.76248 | -47.19595 | 2024-12-22 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74224cfc-587d-373f-9e76-2a86a5354004 | -2.58172 | -49.47621 | 2024-12-22 04:25:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f26d1ed-f905-3059-8513-8702c7130f5a | -3.91347 | -46.66854 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf8fd75e-58a1-3584-bd56-9b9fdcb6c9d6 | -3.92026 | -46.36453 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45d8b9bb-1bc3-32df-88a6-6c3eae804f14 | -2.8073 | -46.71361 | 2024-12-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a93442f4-ca38-3d6e-9280-f87e81c087ee | -4.02278 | -46.90404 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dcabd523-79dc-39db-8950-eb516e61eeff | -2.22522 | -46.50047 | 2024-12-22 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2593f37-ef8f-3cf2-88e5-351fe48cecaf | -3.91052 | -47.01213 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 30d03db4-4021-38bb-9318-5d0386acb3a9 | -2.44528 | -51.79387 | 2024-12-22 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 3cd14d61-fd53-33f1-a28d-bc818c51b841 | -3.9282 | -46.89964 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f85e06c-87d1-35b8-942b-395c135733d9 | -2.19739 | -48.42499 | 2024-12-22 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ce732019-08a5-3e76-bccb-3c11069e302a | -3.94538 | -46.87715 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a586d5bd-821f-33d1-a21c-8706f3b508fb | -1.15203 | -46.75386 | 2024-12-22 04:25:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20928d51-3a79-3d99-b699-fc370d0cfe71 | -2.79812 | -54.18816 | 2024-12-22 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 728ff8df-8136-3367-a456-6844189a8f03 | -2.7984 | -46.74823 | 2024-12-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56c5283d-cf89-3471-9dc5-98ebb22417da | -2.70941 | -46.14647 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9e1e87b-a770-3407-903e-168f7ead9b02 | -4.00279 | -46.92257 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da51dcf2-1f73-3ede-b07b-d1ca104edda6 | -3.88368 | -46.68512 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12cf6da8-279b-3391-af0a-7768e74edbb9 | -2.50987 | -48.05518 | 2024-12-22 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 382b3ad6-c429-3067-8967-eeea30aa244d | -3.9798 | -48.39234 | 2024-12-22 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 76985503-e76d-3cbf-af48-a4cb16fb5af4 | -3.99386 | -46.74159 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58174cd5-556c-3c55-a4c0-d2bdc38c437f | -2.77345 | -54.35266 | 2024-12-22 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1d318e15-a99b-3ce1-b924-2ffee0d87ba5 | -3.91878 | -46.91614 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f822709-d557-364c-8e2d-548167bbc91c | -3.91767 | -46.92315 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b13142a6-d261-3d0b-bbbb-dd624c79016f | -2.56917 | -49.47604 | 2024-12-22 04:25:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d460b84d-4544-3bf3-9666-b17cf7d15389 | -2.44665 | -51.78552 | 2024-12-22 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10388ba4-5e37-3cc2-b8f2-e7be09b0f547 | -4.56301 | -43.2961 | 2024-12-22 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3e39d5a3-6669-34b1-abe0-abedfd6fbd97 | -2.6667 | -54.8698 | 2024-12-22 04:25:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 74ff4001-136c-3298-bef9-4215484f0451 | -4.0089 | -46.9055 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe905301-7276-375a-8da9-a3ee8224bd72 | -2.87116 | -45.93888 | 2024-12-22 04:25:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a9847b0-9c3d-397f-85d0-af275bedd769 | -2.51311 | -47.50344 | 2024-12-22 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README6.md)
