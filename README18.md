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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8608092d-0c48-30e7-8844-83ddf3620eb0 | -4.01772 | -45.96255 | 2024-11-29 03:40:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| bf159378-f8f8-3f0b-ac75-9715335a7c50 | -4.85224 | -41.25815 | 2024-11-29 03:40:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6563d741-1db3-362c-9cb5-df1d08f5d067 | -3.81208 | -44.0425 | 2024-11-29 03:40:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 412d4c15-e763-3a6f-9ff2-96cba903b1e5 | -4.79295 | -43.77835 | 2024-11-29 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 962d834e-f390-3599-b21d-d3a38ebc968d | -2.84044 | -48.09449 | 2024-11-29 03:40:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 73705641-6e66-319d-b908-bbbf6c0d37ce | -3.80995 | -44.0521 | 2024-11-29 03:40:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96051f2f-9c98-37a2-b570-04a37ae9bf5f | -2.83885 | -46.81366 | 2024-11-29 03:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1220d28-6dd2-3cb7-b6fa-34412a109e58 | -4.259 | -42.60651 | 2024-11-29 03:40:00 | NPP-375D | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e81d0e17-5ed7-3005-9875-580348c0d9b3 | -2.94884 | -45.72082 | 2024-11-29 03:40:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f4f4c3e-5629-3f35-afa7-9edd60afdd5d | -3.81606 | -44.04947 | 2024-11-29 03:40:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1fc8084-609a-362e-9c03-17a40cdac5d2 | -5.88642 | -35.42543 | 2024-11-29 03:40:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 55e5256e-16a4-3d3b-9df7-67d50b8ac41a | -3.32814 | -46.6975 | 2024-11-29 03:40:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7224f5f8-9dd1-3272-91bf-a9f5da062026 | -4.4333 | -46.5762 | 2024-11-29 03:40:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 2d6f4a9e-b199-3512-9877-7dae6464f4e7 | -4.43971 | -46.57717 | 2024-11-29 03:40:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b3f93910-1841-3f26-adc6-d6024962ad54 | -5.60117 | -38.78568 | 2024-11-29 03:40:00 | NPP-375D | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f8f954f4-8134-322e-911f-46e695ad85e6 | -2.59957 | -46.83385 | 2024-11-29 03:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 245abc5f-cb09-33a9-876c-fdf9f89c0010 | -4.83876 | -41.25641 | 2024-11-29 03:40:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f89a3a3b-10f0-3ca9-829b-67641cedf072 | -2.87924 | -46.83982 | 2024-11-29 03:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b74bf6c3-aa92-3fe3-b0dc-6f97b7531273 | -3.19902 | -46.59399 | 2024-11-29 03:40:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d5c81a3-5189-30b2-b142-edf285b18e19 | -4.25808 | -42.61209 | 2024-11-29 03:40:00 | NPP-375D | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65bac203-9699-3f27-9bd5-a9920ac3e5c1 | -3.87193 | -48.36798 | 2024-11-29 03:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 038ec3cf-6a8b-3a89-9593-5b69131e2687 | -5.69048 | -39.40966 | 2024-11-29 03:40:00 | NPP-375D | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8ba84861-29de-350e-bbe3-acfc059f1519 | -4.98168 | -41.32005 | 2024-11-29 03:40:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ffd54d45-5392-3cbe-9665-1703c7c423ed | -4.83953 | -41.25185 | 2024-11-29 03:40:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1b679375-dbeb-3330-8bfe-d327d8a90aaf | -2.9828 | -44.96016 | 2024-11-29 03:40:00 | NPP-375D | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 178c6c57-27ec-306a-ba6b-aaf25f2de33f | -2.8398 | -46.80789 | 2024-11-29 03:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6ae2c3f-a4b7-3b2a-93f6-e6d168d15460 | -2.83204 | -48.10041 | 2024-11-29 03:40:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9a53c80f-2e6c-3b17-ae54-2bcc524dc5c7 | -2.06 | -46.38033 | 2024-11-29 03:40:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 613cd1a4-4daf-3af5-8b0c-a9f838bdfa8b | -2.64673 | -47.13209 | 2024-11-29 03:40:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 09fdc336-2b8d-3cf8-840e-8ef55d21bfac | -3.81118 | -44.04498 | 2024-11-29 03:40:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c8282ac5-ecc1-315e-ace2-9c5735d7a0d3 | -4.50373 | -42.07242 | 2024-11-29 03:40:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c83a2fcc-acff-35c2-8041-10aed670d60c | -2.83761 | -48.09429 | 2024-11-29 03:40:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5b7ed508-09e4-3c48-b31b-15133ebc94a9 | -3.69196 | -42.04235 | 2024-11-29 03:40:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 55b3dd79-47a1-3617-b945-1a23d8d4112e | -5.56254 | -35.52804 | 2024-11-29 03:40:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d42756a8-67c2-3e35-a36a-b9e2b45f698a | -1.68452 | -45.80074 | 2024-11-29 03:40:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d40ab675-089f-3922-b66e-5e8ba0c23cbd | -3.96132 | -48.09008 | 2024-11-29 03:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 2030b2c0-2036-36ba-abb8-c3afcc1dfaf0 | -2.86116 | -45.5359 | 2024-11-29 03:40:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28a915a1-489f-3893-9f29-88d7a3b0eded | -2.84794 | -46.82296 | 2024-11-29 03:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e692751-284a-32fc-9649-43a3a1c40790 | -4.92879 | -43.03774 | 2024-11-29 03:40:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bfaee66f-7c8a-3270-8c7f-4a39f207f756 | -3.96253 | -48.0834 | 2024-11-29 03:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 5d3d11e6-2068-3a00-9ce6-41d4fa84e8c0 | -4.07311 | -47.03027 | 2024-11-29 03:40:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 839d64c4-cc86-32c5-9b98-c27fb1f75694 | -4.84403 | -41.25241 | 2024-11-29 03:40:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 752043ca-2fc3-38c7-97b7-aaa202939f1c | -2.83046 | -48.09304 | 2024-11-29 03:40:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 65b43225-6deb-3b38-9d40-84c512315d31 | -4.86415 | -41.26919 | 2024-11-29 03:40:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 92e2b789-95f6-3031-8385-3fcff9139fcb | -2.06653 | -46.38149 | 2024-11-29 03:40:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b208038f-408b-35ec-91a4-cdbced6e9960 | -3.20374 | -46.56664 | 2024-11-29 03:40:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 8d9172b6-6d88-396f-b2c1-6f1de72be200 | -4.1535 | -43.81993 | 2024-11-29 03:40:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db71e6d0-71cb-3b81-8c79-ac589ef8366e | -3.8164 | -44.05057 | 2024-11-29 03:40:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00cfeeb1-f2bc-3041-b954-622de8c48061 | -4.08078 | -47.02537 | 2024-11-29 03:40:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d23d4921-de61-3714-a65b-98b66f99ae84 | -4.07417 | -47.0243 | 2024-11-29 03:40:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ec5f612-3016-3134-a3b8-8c3472d29363 | -2.60625 | -46.8349 | 2024-11-29 03:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0028633-f7ca-3e4f-9448-32fd1fb9a4b2 | -2.64108 | -47.12446 | 2024-11-29 03:40:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ac3cceb7-7c4b-3716-8e2b-4a1ce1301813 | -3.19728 | -46.5653 | 2024-11-29 03:40:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b15880df-0b71-3468-aca4-75d33ee5302c | -3.61316 | -40.49233 | 2024-11-29 03:40:00 | NPP-375D | MERUOCA | CEARÁ | Brasil | 2308203 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7fb49418-19f0-38f4-85f6-592e84554ced | -5.15216 | -37.73972 | 2024-11-29 03:40:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c25fd817-d4ec-3f43-bdfb-59ef1b72b955 | -4.9153 | -44.02695 | 2024-11-29 03:40:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d5dee41-43f5-386c-8c4b-ba866c5b0679 | -4.8164 | -39.94005 | 2024-11-29 03:40:00 | NPP-375D | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6ba72252-7a50-3a8a-befa-08c92ecb7aea | -4.44998 | -44.00322 | 2024-11-29 03:40:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 968a4dae-ab9d-34b3-aed2-7f192980dfee | -3.96537 | -48.08496 | 2024-11-29 03:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31ca0233-8b34-3111-a4ff-78a7de1ec73f | -2.86027 | -46.83076 | 2024-11-29 03:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8f9a780-5fc0-3fc7-a8c6-e7d7998de857 | -4.26628 | -47.61366 | 2024-11-29 03:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c243525-324b-37f0-a18a-bf61e1d0a555 | -4.36558 | -47.25548 | 2024-11-29 03:40:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8c0f4d95-14ae-3ef9-9eec-e3949d5b6d05 | -5.88919 | -35.42942 | 2024-11-29 03:40:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e14f8c3f-1d23-33f2-a035-d137e2443ebd | -3.96649 | -47.94193 | 2024-11-29 03:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc48d73f-c2dc-37e6-a8ac-4a88b9b093f5 | -2.64726 | -47.12311 | 2024-11-29 03:40:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 68d4f106-526b-35f1-aaac-b5a15567bf24 | -1.67899 | -45.7947 | 2024-11-29 03:40:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 340a2c53-77a1-3224-b879-67c06046ae24 | -4.87225 | -41.27568 | 2024-11-29 03:40:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 1dd823b1-2783-3869-a286-f340c298fcd3 | -3.17469 | -46.31131 | 2024-11-29 03:40:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b84a5c8-a80c-3aaf-a514-676f9031c352 | -4.90934 | -44.02931 | 2024-11-29 03:40:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 080fd5ce-d268-36f7-a3da-49c078f6705b | -4.07973 | -47.03133 | 2024-11-29 03:40:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63fe23bf-4c16-32cd-b114-1124999fdaae | -3.19807 | -46.59946 | 2024-11-29 03:40:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96ca4556-a474-307d-b782-8a5093273f47 | -2.88592 | -46.84081 | 2024-11-29 03:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf761744-2965-374c-9aec-6d6f151dbd8d | -4.25928 | -42.60737 | 2024-11-29 03:40:00 | NPP-375D | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e851eda5-68ac-3e56-9771-f239497e26a7 | -3.44079 | -40.83327 | 2024-11-29 03:40:00 | NPP-375D | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2fe3c4de-9024-380c-8ddc-b8ef00b17e83 | -4.8307 | -41.24984 | 2024-11-29 03:40:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3dabf4e1-9e47-3e75-8fd4-9e5259da8de8 | -5.89029 | -35.42248 | 2024-11-29 03:40:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 3.8 |
| db270168-3c34-3cbd-8a15-1daf9c51d744 | -5.20826 | -37.36819 | 2024-11-29 03:40:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0d273d7d-3e69-3877-ad4c-f0631e0f4c4c | -4.43808 | -46.58164 | 2024-11-29 03:40:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 960d0578-28ad-3240-9f2b-e0e6c4acc32f | -5.88587 | -35.42889 | 2024-11-29 03:40:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 26afb446-8abc-3608-9953-fb10e433d19e | -3.95828 | -48.08408 | 2024-11-29 03:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 316afea5-34f6-32ad-b87a-b3017ffb02c4 | -4.84327 | -41.25687 | 2024-11-29 03:40:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0f46c9b5-ca63-3a5a-9cbd-b8c730c03a21 | -3.81667 | -44.0459 | 2024-11-29 03:40:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aafddea1-2738-35b5-b241-bd50e01986f7 | -4.25958 | -47.61184 | 2024-11-29 03:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ecebfe9-394c-3862-b978-382de599eaba | -4.26014 | -47.61122 | 2024-11-29 03:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bf59d1de-51b8-3b13-a9fd-757487b53d6f | -3.19633 | -46.57077 | 2024-11-29 03:40:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 667ec275-bcd2-3cad-9e7f-5be4f77ebcbb | -2.8753 | -46.86308 | 2024-11-29 03:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae3b6b04-e4b5-33b5-bc4d-5193e5d83498 | -4.31561 | -46.04232 | 2024-11-29 03:40:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1cdb1b87-9e53-30ba-a687-16912e809485 | -4.86786 | -41.27445 | 2024-11-29 03:40:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 4318a73c-44e0-3278-b831-8f3dbefb7389 | -2.94802 | -45.72567 | 2024-11-29 03:40:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2449f01c-f0d3-322f-b079-af455085d26b | -2.64005 | -47.13036 | 2024-11-29 03:40:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 551069b7-cd00-3dad-a16b-af47715a8c6c | -2.96846 | -45.23067 | 2024-11-29 03:40:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4d15908-f2dd-35b9-879f-a7e079e4e55d | -2.85341 | -45.54438 | 2024-11-29 03:40:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2bae6e9b-06c2-3a27-9f6c-cb7b766f3530 | -4.36661 | -47.24969 | 2024-11-29 03:40:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 931f9760-88c5-3491-af6c-c6e370e3d111 | -3.96531 | -47.94843 | 2024-11-29 03:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3534ef19-0bd2-3a43-bb1d-160f3890d065 | -2.33647 | -46.87097 | 2024-11-29 03:40:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 19b6de2c-87a1-3538-83fe-6cde188e10e3 | -4.32183 | -46.04326 | 2024-11-29 03:40:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac5e8ef7-f8c6-3e14-b586-9e5c0471cc55 | -5.89307 | -35.42648 | 2024-11-29 03:40:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 3.8 |
| ec61c102-465c-3b7f-8633-1b8e4cbbaf76 | -3.17007 | -46.29977 | 2024-11-29 03:40:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05bf33db-b25a-3e8d-8aa0-db16e834a46e | -2.6478 | -47.12595 | 2024-11-29 03:40:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 56c7b65f-5a01-36a4-865c-5466080c04a6 | -3.81031 | -44.0532 | 2024-11-29 03:40:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README19.md)
