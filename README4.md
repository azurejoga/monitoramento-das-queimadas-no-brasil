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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68b8deaf-113e-3839-a286-6ef1fe5c0c8d | -3.1422 | -50.4562 | 2024-11-10 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 12d2dd1f-52a2-3239-95e5-cac66186b9cf | -3.0213 | -53.2607 | 2024-11-10 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| df080363-f1bc-34e4-ab9f-587ab605b4c8 | -3.6003 | -47.3614 | 2024-11-10 00:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 149.1 |
| 4bf5425f-da31-3bec-9dae-70e0b5dfb5d6 | -1.5531 | -52.2101 | 2024-11-10 00:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| b71ce9d9-a683-345d-90c3-05090d74f362 | -3.9483 | -48.1724 | 2024-11-10 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 164.9 |
| 62bdeffd-2567-331b-8501-d81dcb05e086 | -4.6922 | -45.153 | 2024-11-10 00:30:00 | GOES-16 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 8c0035ed-f38a-32cc-8533-b6d7282728a5 | -3.2244 | -53.0524 | 2024-11-10 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 205.9 |
| 79f5890a-40a6-3a48-9cec-b09704ed38a5 | -3.5818 | -47.3621 | 2024-11-10 00:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| e5cea7ea-932d-3b0c-b472-c6ca7065a89c | -4.6736 | -45.1541 | 2024-11-10 00:30:00 | GOES-16 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 8a073c7b-bf9b-35f3-a8ae-0590f11ab26e | -2.0954 | -48.8125 | 2024-11-10 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| da38151e-bbee-3404-9a3f-f382fde8f589 | -3.9482 | -48.194 | 2024-11-10 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| b3951377-4fe4-3446-a8dd-7e1a7195a7ea | -3.525 | -44.0286 | 2024-11-10 00:30:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 142.9 |
| e95be130-46c1-3e28-9e16-8eb54ec3274c | -3.8413 | -44.1283 | 2024-11-10 00:30:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| b112f0e3-6951-3086-87cf-7b69aded16b7 | -2.2095 | -47.733 | 2024-11-10 00:30:00 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 106.3 |
| c96a09ac-1c0f-3594-ae98-b77a0033a09c | -17.313 | -57.4834 | 2024-11-10 00:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.8 |
| 2a85e47c-4299-32df-a2f9-c241bea4ce51 | -2.2486 | -47.078 | 2024-11-10 00:30:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 9697b7ca-fb97-308a-af5d-9c03592a743d | -3.619 | -47.3388 | 2024-11-10 00:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 1fae27a8-98c5-3439-9183-1623b9d551fc | -2.6203 | -46.7602 | 2024-11-10 00:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| ded7e152-6663-33ad-8267-be8ba5cc0f23 | -3.6189 | -47.3606 | 2024-11-10 00:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 4f6692c4-cc98-37f5-9ba6-8647088c09bf | -3.9485 | -48.1508 | 2024-11-10 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 7e6f1ba0-e725-314f-afe6-2924e42cb66b | -2.2076 | -48.3596 | 2024-11-10 00:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| adf4897b-ae8f-3aaa-ad6b-fc422f9c2b76 | -3.967 | -48.15 | 2024-11-10 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 08c92b89-5aa1-3484-b2f0-4f2e6feae038 | -3.1423 | -50.4352 | 2024-11-10 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 183.3 |
| bab53f27-c515-3709-bc31-96650c1b1133 | -3.1096 | -49.4029 | 2024-11-10 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 25c8b62d-6da3-3a2b-b805-336066769f49 | -3.035 | -49.5537 | 2024-11-10 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 30c49ce7-4f0f-31bc-9df1-c7e2b5735323 | -3.4383 | -50.2999 | 2024-11-10 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| f1d69b03-f022-3ae2-adf8-5cba1e8411af | -1.5163 | -52.1901 | 2024-11-10 00:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 9e0d1962-f35e-3b98-bf61-bf73f80489ca | -2.2094 | -47.7547 | 2024-11-10 00:30:00 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 03126451-78b0-3ba9-b6ac-eb1d0bda1e98 | -3.1238 | -50.4568 | 2024-11-10 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| cddd7143-f096-34b7-ae19-102c6c022435 | -3.0029 | -53.2612 | 2024-11-10 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| c9973fb3-1f1c-3617-96dd-6e6e6c73353b | -3.6004 | -47.3395 | 2024-11-10 00:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 254.2 |
| 39fb0598-57d6-318a-b6b7-ed207f3a8192 | -2.8802 | -51.4835 | 2024-11-10 00:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 5a502110-2b5f-3033-9558-20572b00055c | -2.9442 | -49.1529 | 2024-11-10 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 989762a2-9ca8-3c8b-8d16-e1f85ff1fa2d | -2.9355 | -51.482 | 2024-11-10 00:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 58a10d7d-afc9-3ccc-9ea3-6d0de359ef26 | -2.7772 | -49.3492 | 2024-11-10 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 141.2 |
| 76e4ea5c-0755-361b-8674-881f6f59ef0f | -3.5249 | -44.0516 | 2024-11-10 00:30:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| c65dc6fd-46da-3883-a06c-e3080ccfa534 | -1.4926 | -55.431 | 2024-11-10 00:30:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 188.1 |
| cd247873-9ef8-3ef3-b813-4fe55e66f721 | 2.8552 | -60.0853 | 2024-11-10 00:30:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 45.1 |
| fe2eefc3-168e-31c6-b58e-e3ef48f17998 | -1.4742 | -55.4312 | 2024-11-10 00:30:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 131.9 |
| cca02aa7-212f-31a0-806c-11a99b90360d | -2.4662 | -48.4391 | 2024-11-10 00:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 566e329c-9d22-303b-a9b6-20a6b141d523 | -3.6923 | -51.2929 | 2024-11-10 00:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 53e3ca0e-b54d-3b26-bd58-b5d9a1ca42bc | -3.5819 | -47.3403 | 2024-11-10 00:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 3c26ee02-78b7-3484-938e-f70718c013f2 | -1.4742 | -55.451 | 2024-11-10 00:30:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 34f4e3fa-d3f8-3072-b004-5ab79a333707 | -1.5347 | -52.1899 | 2024-11-10 00:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 146.9 |
| dee7e362-f2b6-32b8-8660-5d3fb18ae539 | -2.4183 | -51.9484 | 2024-11-10 00:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| bebb6bd7-d7f3-3cd2-a79c-ddf60be6789e | -3.1239 | -50.4358 | 2024-11-10 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 140.8 |
| f664e494-171c-3fbe-8502-d72a914b1f15 | -4.2083 | -48.1176 | 2024-11-10 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| fe58af32-3912-343c-b74c-0d53fb1fba01 | -3.3097 | -50.136 | 2024-11-10 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 9d04f469-2e15-3a19-b7f6-fc5cdd8cf647 | -1.4925 | -55.4508 | 2024-11-10 00:30:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 125.3 |
| 39e2cec7-66ca-30c2-9703-3191f3e878c8 | -3.76 | -52.6695 | 2024-11-10 00:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| b18403bd-0a65-3136-8440-7f204725b789 | -2.9171 | -51.4825 | 2024-11-10 00:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 98858cfb-0906-3a6d-9330-559e07f36214 | -3.5064 | -44.0294 | 2024-11-10 00:30:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 5ed29334-c254-3fa1-9a45-8200c6d8bd5f | -3.4326 | -43.8948 | 2024-11-10 00:30:00 | GOES-16 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 0febed1e-8eaf-3cdc-87d1-0cd92abdc5e1 | -3.9668 | -48.1932 | 2024-11-10 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| b47e78a7-5857-3536-a069-9d39908b9003 | -2.9257 | -49.1534 | 2024-11-10 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 4eb6ea12-ba1b-3d54-9ea2-4c53bfa825c1 | -2.7587 | -49.3497 | 2024-11-10 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 6c29e536-5dba-3216-a862-5bc63dab1cd8 | -2.2671 | -47.0775 | 2024-11-10 00:30:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 160.5 |
| 94477086-4416-33b9-a6c4-db5f5b5816bc | -1.5346 | -52.2308 | 2024-11-10 00:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| f989a721-a42b-3fe4-b234-99b13d910cd0 | -2.0953 | -48.8338 | 2024-11-10 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 120.4 |
| 4fd69638-daeb-34d6-bfac-e32e7725d509 | -1.5347 | -52.2104 | 2024-11-10 00:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 351.3 |
| 16687d5d-7138-37ea-ae5a-3d50888783ca | -2.7771 | -49.3704 | 2024-11-10 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 625084a4-4c92-3d9d-8018-f769e1479cc2 | -17.2933 | -57.4857 | 2024-11-10 00:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 217.4 |
| 7808e4ad-1536-3197-973c-1c05d542d653 | -3.2427 | -53.0722 | 2024-11-10 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 112.5 |
| 11c47de7-9462-39cc-aac6-0a8399d51a89 | -2.2487 | -47.0561 | 2024-11-10 00:30:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 141.2 |
| 9122e8b4-a818-3414-baac-4ed5b904fa8a | -2.2075 | -48.3811 | 2024-11-10 00:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 1b2bb8b8-dcea-3e09-bf03-e781fa5456a3 | -3.2243 | -53.0727 | 2024-11-10 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 162.4 |
| 2904a672-2edd-3398-a9be-4a97aa588055 | -2.2672 | -47.0556 | 2024-11-10 00:30:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 277.4 |
| 977f2dd1-c6a7-32f8-a63b-9eae83828195 | -8.3967 | -44.1365 | 2024-11-10 00:30:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 6e3da846-bf6e-32d1-9335-5d5ecf05e524 | -3.2984 | -52.9486 | 2024-11-10 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 36b3186f-7378-38d6-9f68-f84745f2bd4e | -4.1112 | -45.7018 | 2024-11-10 00:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 1a25d0ac-e363-397a-9fae-56dd95a44be5 | -3.967 | -48.15 | 2024-11-10 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 02aed7c8-f666-3d99-befd-446341528d89 | -3.1423 | -50.4352 | 2024-11-10 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 9ceac7d3-0bd4-31ea-a6aa-645c48a348b4 | -2.8802 | -51.4835 | 2024-11-10 00:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 9fc9fb81-f4f5-3817-9a1f-f0620fc94dc8 | -3.8413 | -44.1283 | 2024-11-10 00:40:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 2cafb4ba-f45f-323e-9bd7-4dcb6d7f22d2 | -17.313 | -57.4834 | 2024-11-10 00:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.4 |
| dc2b0ed6-f543-3050-9a9d-175cf7b3dd6c | -17.2933 | -57.4857 | 2024-11-10 00:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 214.7 |
| d824202f-11cf-300e-b8c8-d2346da8c10b | -1.4926 | -55.431 | 2024-11-10 00:40:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 123.3 |
| 68d35fe9-ba2c-3472-8296-ac7fa65ec8d3 | -2.7771 | -49.3704 | 2024-11-10 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| cd941440-d6c2-3e24-8a6e-1e5785a589eb | -8.4156 | -44.1344 | 2024-11-10 00:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 255a5756-386f-39a8-a3ce-84307758214b | -3.0213 | -53.2607 | 2024-11-10 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| ed3c2d38-8da3-37d9-8661-62bc601001b0 | -2.4662 | -48.4391 | 2024-11-10 00:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| cd973dea-3dc0-36b5-a409-4db58f4c8fbf | -4.2083 | -48.1176 | 2024-11-10 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| a0d51ea1-0362-31bc-9336-acc857f7bf31 | -1.5346 | -52.2308 | 2024-11-10 00:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 142180d3-5d04-3df6-a054-d6fb95af0124 | -3.2984 | -52.9486 | 2024-11-10 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 38bf0cf3-0952-32c8-afd2-228b54b44fee | -4.8916 | -48.6234 | 2024-11-10 00:40:00 | GOES-16 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 9e63d8a3-1832-392e-9c6a-f8f7647b44ee | -3.5819 | -47.3403 | 2024-11-10 00:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| e965c099-7bcf-3e92-a113-a03cc9cc9515 | -3.2427 | -53.0722 | 2024-11-10 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 7c801c5f-affc-34ec-871c-a95304cf41ee | -2.803 | -52.5337 | 2024-11-10 00:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 952ea94d-e19d-380a-a996-5a7b6ac4b24f | -3.9483 | -48.1724 | 2024-11-10 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 138.0 |
| cb95b555-cd5d-37e2-b648-ac288d53df1a | -2.9171 | -51.4825 | 2024-11-10 00:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 9a8fb9ad-8f12-35b4-a371-c75debe260af | -1.4742 | -55.451 | 2024-11-10 00:40:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| f2e8a5ce-e736-30f7-a6a8-f59951a23d4f | -2.2094 | -47.7547 | 2024-11-10 00:40:00 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 9a7481ab-ef1a-3ab3-ad40-152f5d0c11b7 | -3.9485 | -48.1508 | 2024-11-10 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| a11b39b6-0beb-36f3-85af-ca6ae3f353d2 | -8.3778 | -44.1386 | 2024-11-10 00:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 2c728e65-f946-3538-8d9b-51ab25ce1dfe | -1.5347 | -52.1899 | 2024-11-10 00:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 824f6952-eb49-36c8-a5b8-327e0c8b868a | -2.6203 | -46.7602 | 2024-11-10 00:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| e9aaa439-f63e-3986-b7ba-365ed8a0381b | -1.5163 | -52.2106 | 2024-11-10 00:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| e4d178a3-2e0f-3afb-ab1f-f5c8cc08023c | -3.76 | -52.6695 | 2024-11-10 00:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| d4aa715e-842e-3e6c-adfa-ad5ffd6eeba4 | -2.2076 | -48.3596 | 2024-11-10 00:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 410c4075-b404-347c-a831-da67ea40aa91 | -1.4742 | -55.4312 | 2024-11-10 00:40:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |


[Clique aqui para ver as próximas entradas](README5.md)
