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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 217e50a1-776d-3cd6-ab52-60289b4e8a4b | -6.8395 | -59.2643 | 2025-08-01 11:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| cdfd1f4b-66b9-3496-82b5-b992c8bc874c | -8.0321 | -43.1257 | 2025-08-01 11:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 122.2 |
| c6057992-7747-3fe8-b8ac-1806bde357d3 | -6.7294 | -59.1723 | 2025-08-01 11:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 107.8 |
| ef3505cc-a3e8-35a2-a320-a2498bf31906 | -8.051 | -43.1237 | 2025-08-01 11:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 156.3 |
| 0c467a44-ea5a-3d69-8e52-b8376f7154e2 | -8.0513 | -43.1001 | 2025-08-01 11:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 119.5 |
| 823a37ca-910e-3ed0-888d-b0cede2518c0 | -6.8211 | -59.2651 | 2025-08-01 11:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 157.8 |
| 046a3608-934d-3240-a872-b9273167f46d | -8.0321 | -43.1257 | 2025-08-01 11:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 174.1 |
| f22b834f-7889-3703-9060-0c631c5cacb0 | -8.0513 | -43.1001 | 2025-08-01 11:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 123.9 |
| dbdd143c-6536-338e-b001-54f2830dccd2 | -6.7294 | -59.1723 | 2025-08-01 11:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 2d30f0a7-15b3-3885-8dc8-b9d9c68efa92 | -6.8211 | -59.2651 | 2025-08-01 11:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 180.8 |
| 470f00cf-ae86-355d-8466-bede7dc68662 | -6.8395 | -59.2643 | 2025-08-01 11:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 256dc5bc-dd34-358e-892b-d7ce5ebd0158 | -8.051 | -43.1237 | 2025-08-01 11:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 155.6 |
| 64327428-5d96-30e5-9311-28c1c5a44606 | -8.0321 | -43.1257 | 2025-08-01 11:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 150.6 |
| 53226749-4cc7-38df-8ea0-c6dc61b59625 | -10.5974 | -45.2767 | 2025-08-01 11:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 189.4 |
| 0040ed3f-153d-3741-97f9-3728b292059f | -10.5978 | -45.2537 | 2025-08-01 11:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 796ba466-2a50-38f3-971c-dcecce368f6b | -8.051 | -43.1237 | 2025-08-01 11:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 199.9 |
| 8333812d-83e6-32b1-a11e-69d22e0bd057 | -6.8395 | -59.2643 | 2025-08-01 11:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.9 |
| cf72e6d6-b018-3dbb-8a0d-a135f08e0486 | -6.8211 | -59.2651 | 2025-08-01 11:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 260.5 |
| 918f1f7a-4996-3ddb-b0a2-8e32f0d5b4bd | -6.7294 | -59.1723 | 2025-08-01 11:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 127.2 |
| bcb35ef3-493d-3f5c-ab8d-48e43977c464 | -8.0321 | -43.1257 | 2025-08-01 11:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 146.4 |
| 80007854-ba2c-3b7c-98d1-adfc8965aad3 | -8.0513 | -43.1001 | 2025-08-01 11:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 148.7 |
| 4eb91ff9-f49e-3a1b-9914-572622868d6c | -8.0513 | -43.1001 | 2025-08-01 11:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 179.8 |
| 8db67e42-8553-3ed3-9bc7-d33d673df492 | -6.821 | -59.2844 | 2025-08-01 11:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 4b00e4a1-1763-3ccd-82da-681693d56a15 | -8.0324 | -43.1022 | 2025-08-01 11:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 132.4 |
| f0352980-8df8-3af9-aa90-688418c39f4c | -6.8395 | -59.2643 | 2025-08-01 11:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 2fe42ecb-5351-3204-a9c6-23643f41cc33 | -8.0321 | -43.1257 | 2025-08-01 11:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 156.7 |
| 38e380fa-3c79-33f7-a93e-1685e3258530 | -6.7294 | -59.1723 | 2025-08-01 11:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 120.3 |
| e4149827-dd26-35e6-95da-bcdb3d6831f2 | -6.8211 | -59.2651 | 2025-08-01 11:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 254.3 |
| e7e96cad-db86-3718-a970-d34c37da7176 | -8.051 | -43.1237 | 2025-08-01 11:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 202.7 |
| f9864b4b-3622-3b75-898c-62706f1e9f88 | -6.7294 | -59.1723 | 2025-08-01 11:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 142.7 |
| 1c0d3994-fe29-3b08-a2cb-0714a499d4f2 | -8.0321 | -43.1257 | 2025-08-01 11:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 190.3 |
| a77836f6-ab17-33a8-849c-e2ae3da2b496 | -8.051 | -43.1237 | 2025-08-01 11:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 156.8 |
| f95aa963-60d4-3a93-be91-cc0510e83023 | -8.0324 | -43.1022 | 2025-08-01 11:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 160.1 |
| 38254a77-ef94-339b-b499-9d4d3273817e | -6.821 | -59.2844 | 2025-08-01 11:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 108.5 |
| fe70b103-703e-3bea-b62c-1fe05216da4f | -6.8211 | -59.2651 | 2025-08-01 11:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 267.8 |
| ec588909-b3da-3a27-9230-20a1d3372cb8 | -6.8395 | -59.2643 | 2025-08-01 11:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 114.3 |
| a9f1f978-36c6-3239-8ff3-09b6fd2d8a63 | -8.0513 | -43.1001 | 2025-08-01 11:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 142.8 |
| 86762503-e696-388d-a89b-b5dee52f573c | -8.0513 | -43.1001 | 2025-08-01 12:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 159.1 |
| bfbc69b5-1a10-3a8c-80d7-692e5fbada43 | -6.656 | -59.0981 | 2025-08-01 12:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.1 |
| ba2b7340-1e5f-32bf-886e-17f3d0fd0e72 | -6.8211 | -59.2651 | 2025-08-01 12:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 406.8 |
| dc2c5165-b5ea-372e-998e-c89dd5f81630 | -6.821 | -59.2844 | 2025-08-01 12:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 7ae292b6-505b-3b4a-8273-ad59bf1b3ee1 | -8.0324 | -43.1022 | 2025-08-01 12:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 127.2 |
| 8f66c667-280e-39bc-be39-96c5d70b797b | -8.051 | -43.1237 | 2025-08-01 12:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 216.8 |
| e2feaeaf-505e-36c5-93e2-a0e512ac5022 | -6.8395 | -59.2643 | 2025-08-01 12:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 120.7 |
| c8f43de1-62d5-3e7f-998b-6c09a8c69910 | -8.0321 | -43.1257 | 2025-08-01 12:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 187.8 |
| 96173a5d-29d2-3ad6-94b8-1f8e1f701403 | -6.7294 | -59.1723 | 2025-08-01 12:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 137.6 |
| ade22b5b-b63e-386c-925e-a5d7bb2f76b0 | -6.8395 | -59.2643 | 2025-08-01 12:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 168.0 |
| 5e7f5e10-370b-3908-8ef3-a968de9f3a7d | -8.0513 | -43.1001 | 2025-08-01 12:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 139.1 |
| 312c32a2-8ad1-3fdf-b25d-695ae2e42b5a | -6.7294 | -59.1723 | 2025-08-01 12:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 158.7 |
| 04147cfb-266a-3fcf-bb45-8e13cf52a8e0 | -9.8119 | -47.0651 | 2025-08-01 12:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 116.5 |
| cbabd85b-1e9b-302b-adf6-a6ecfe960d71 | -8.051 | -43.1237 | 2025-08-01 12:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 158.3 |
| d564e896-99c2-3e62-9575-1c2511b04e7c | -8.0321 | -43.1257 | 2025-08-01 12:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 131.6 |
| 7d1c7063-846c-37b4-8de4-468ed88441d6 | -6.656 | -59.0981 | 2025-08-01 12:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 1837c671-dc2e-33d2-9e8d-4c6a74e3a213 | -6.7478 | -59.1716 | 2025-08-01 12:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.1 |
| bf3e1f26-0920-31bd-adcb-3a835612b6ab | -6.8211 | -59.2651 | 2025-08-01 12:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 432.5 |
| f9da1b04-c3af-3aca-9287-c7713c76b177 | -6.8212 | -59.2458 | 2025-08-01 12:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.2 |
| e864be66-15d2-3cd1-819b-9c64af8e007b | -6.821 | -59.2844 | 2025-08-01 12:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 178.5 |
| 0e5a1566-bd41-3e0e-a9b8-5a29c11d968b | -6.656 | -59.0981 | 2025-08-01 12:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 116.7 |
| cc99a236-e4d2-3476-bd10-bc9f15a8771d | -6.7478 | -59.1716 | 2025-08-01 12:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.0 |
| bbbfa008-806e-3d13-84ca-81b1618ce00f | -8.0321 | -43.1257 | 2025-08-01 12:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 129.5 |
| fe012bb3-3221-3578-af2d-274326f1ebb7 | -8.051 | -43.1237 | 2025-08-01 12:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 160.8 |
| 1ca9e580-94aa-3967-b7f6-029c8c1b07d1 | -6.8211 | -59.2651 | 2025-08-01 12:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 745.9 |
| 38bb4d49-1805-399d-be51-bed347edf288 | -6.8026 | -59.2658 | 2025-08-01 12:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 3bc85361-8358-37ec-b743-6264bff29921 | -6.7293 | -59.1916 | 2025-08-01 12:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.1 |
| bd9c1863-177b-3949-9b36-4305999a93b4 | -6.7294 | -59.1723 | 2025-08-01 12:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 185.0 |
| 685657a7-c263-3e19-b458-189806e91767 | -6.821 | -59.2844 | 2025-08-01 12:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 271.8 |
| c4c8aa4a-3afb-3a15-83f7-eb830be03f07 | -8.0513 | -43.1001 | 2025-08-01 12:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 150.4 |
| 8570d330-45ac-3a3f-9ee9-545a2fc6a476 | -6.8212 | -59.2458 | 2025-08-01 12:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 173.0 |
| 2e993094-561c-3ab4-b7f3-e95ddada5329 | -6.8395 | -59.2643 | 2025-08-01 12:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 240.8 |
| c8169ac2-667d-3f2c-aa85-944b7bc9c6c5 | -8.0321 | -43.1257 | 2025-08-01 12:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 142.9 |
| d17df46e-97fc-3d80-9460-53f7a61b5967 | -6.8211 | -59.2651 | 2025-08-01 12:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1054.4 |
| 0b3206c1-5408-3b0a-a151-e6af25a202af | -6.6376 | -59.0988 | 2025-08-01 12:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 078ebc93-3143-3323-a983-910041f3f1cb | -6.7478 | -59.1716 | 2025-08-01 12:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 990ce653-3e5f-38a1-b1c8-8e4c1a6eb3e8 | -6.821 | -59.2844 | 2025-08-01 12:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 292.4 |
| 1a48bb07-4d31-3c52-acff-7b385c4c53a3 | -6.656 | -59.0981 | 2025-08-01 12:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 158.2 |
| b7b2c105-e20a-376e-bc41-a60caaf35e75 | -8.051 | -43.1237 | 2025-08-01 12:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 178.2 |
| 43ce189d-3c4b-31ee-9028-91d23bd2185d | -6.8026 | -59.2658 | 2025-08-01 12:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 156.8 |
| 6efb8bf6-4933-34e8-a9c3-3ecaaa683ea4 | -6.8395 | -59.2643 | 2025-08-01 12:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 365.0 |
| 70818bfb-165f-3ef4-b94e-3687e4cf47ef | -14.9629 | -49.2902 | 2025-08-01 12:30:00 | GOES-19 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 85.9 |
| d4e392da-ee74-31ae-a145-263b4edc6c8b | -8.0513 | -43.1001 | 2025-08-01 12:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 146.3 |
| 93e8bb32-fad6-378b-88c1-5cbc190e2f99 | -6.7294 | -59.1723 | 2025-08-01 12:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 161.1 |
| 3d4f2b08-f355-3419-964c-c789a45e300f | -6.8212 | -59.2458 | 2025-08-01 12:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 176.8 |
| de38ba68-bef8-3776-9e83-0a295f897d61 | -6.8395 | -59.2643 | 2025-08-01 12:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 470.6 |
| a96bb755-ce87-340f-81d6-13f61fc15f77 | -6.6376 | -59.0988 | 2025-08-01 12:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 255.5 |
| 279c1e81-3b01-3199-9ae1-462a742aacc6 | -6.7478 | -59.1716 | 2025-08-01 12:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 129.3 |
| c01192c9-1166-3326-a9da-d5ffc56a5f48 | -6.8397 | -59.245 | 2025-08-01 12:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.0 |
| dff901b4-667d-3479-918f-c5f6af5b1b2e | -6.8211 | -59.2651 | 2025-08-01 12:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1035.1 |
| a8110595-fe87-328a-a6b5-b4a970211db2 | -8.0321 | -43.1257 | 2025-08-01 12:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 144.6 |
| fa02b9c9-cfef-3a8d-be08-77876a315a13 | -6.7294 | -59.1723 | 2025-08-01 12:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 180.6 |
| 298a3c3e-ef46-340f-9d2f-ad7f5aa2e38f | -6.656 | -59.0981 | 2025-08-01 12:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 201.4 |
| c07e3e2d-aa66-3676-a666-3257045e7d32 | -6.8026 | -59.2658 | 2025-08-01 12:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 296.4 |
| 7d3df6f2-6ac4-3edb-ad65-2c6db3131e21 | -8.0513 | -43.1001 | 2025-08-01 12:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 134.9 |
| 3faf6222-c286-3ebf-a51b-ce422af31498 | -6.8212 | -59.2458 | 2025-08-01 12:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 193.5 |
| 617097f3-222a-3738-8a95-2bdc82ec6b2b | -8.0324 | -43.1022 | 2025-08-01 12:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 114.5 |
| e61f6594-1fd7-3b2c-98e2-01965ec1d3b5 | -8.051 | -43.1237 | 2025-08-01 12:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 140.0 |
| 99a7338b-5917-3970-808a-edbb775a5f37 | -6.7478 | -59.1716 | 2025-08-01 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 122.4 |
| c61a41e3-99e2-308c-97f1-0cee20a2a79f | -6.7294 | -59.1723 | 2025-08-01 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 168.1 |
| 864f78db-00e7-3c10-bd03-897a4c36934f | -6.7293 | -59.1916 | 2025-08-01 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 2735e0f2-4b22-3913-85a5-62863394966f | -8.0513 | -43.1001 | 2025-08-01 12:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 138.4 |
| 86e25e20-f2d6-3594-84a8-ddf00ca16d42 | -8.0321 | -43.1257 | 2025-08-01 12:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 146.8 |


[Clique aqui para ver as próximas entradas](README30.md)
