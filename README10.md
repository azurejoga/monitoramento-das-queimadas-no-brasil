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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4eb9ddf1-2f47-3882-8300-f0ec3aad1bf8 | -3.477 | -46.0656 | 2024-11-05 01:50:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 39.8 |
| a6fb4789-8c9b-3a15-b20f-1406527d3066 | -4.408 | -43.1018 | 2024-11-05 01:50:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 0d87ede7-d50e-30f2-8a91-d9b9ecba8e40 | -4.0667 | -46.9246 | 2024-11-05 01:50:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 546417e7-46db-3c15-b886-c8c1f623d341 | -10.0891 | -68.352997 | 2024-11-05 01:59:00 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| c5c44cca-999a-3a7f-b087-d5fb4af22755 | -9.2086 | -71.921097 | 2024-11-05 01:59:00 | METOP-B | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 284a8903-9b81-376b-8b3e-b95564459c69 | -9.2071 | -71.9142 | 2024-11-05 01:59:00 | METOP-B | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| e8c168a5-8a6d-34a6-8fdc-d01288af5e0a | -4.2429 | -48.5474 | 2024-11-05 02:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 8ddea884-89cc-3bf5-8e59-84b9d76a2b29 | -3.967 | -48.15 | 2024-11-05 02:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 61fbceeb-8c50-3f90-8b5b-59abda1b7731 | -3.9669 | -48.1716 | 2024-11-05 02:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| bab62146-3d8d-3251-b4c9-2ec65309f118 | -4.606 | -46.8758 | 2024-11-05 02:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 40aecb1f-c546-3895-ad78-51dbe3467175 | -4.408 | -43.1018 | 2024-11-05 02:00:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 7c8f7ed1-0a00-38e1-b751-94a33bae3dec | -4.4266 | -43.1241 | 2024-11-05 02:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 48.6 |
| fda8f0bc-2130-37a0-9157-4c125b102fed | -4.4268 | -43.1007 | 2024-11-05 02:00:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 741e5e4b-98a0-3ecf-8cbe-c989cdc67e2d | -4.4079 | -43.1252 | 2024-11-05 02:00:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| c2ac4059-4dd9-3429-953a-6bd0ee5ae117 | -4.6061 | -46.8537 | 2024-11-05 02:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 56.7 |
| a2fef052-f6b1-3bf7-9371-fbd187795506 | -3.56 | -47.4 | 2024-11-05 02:00:00 | MSG-03 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6d145aa-d7bf-3136-b3b3-c3217150fff9 | -3.55 | -47.35 | 2024-11-05 02:00:00 | MSG-03 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 375f900e-7509-344c-832a-87bb79965014 | -4.4266 | -43.1241 | 2024-11-05 02:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 39ca5ca5-12bb-3f6c-88df-49196a0745c7 | -3.967 | -48.15 | 2024-11-05 02:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 47ded6f6-d683-3013-a396-52c1850d0ff0 | -4.4268 | -43.1007 | 2024-11-05 02:10:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| a675b916-07ba-3015-8930-a71252b1699a | -4.408 | -43.1018 | 2024-11-05 02:10:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 173.0 |
| 594308d8-a5e4-3551-a4d7-5621647a22a1 | -4.4079 | -43.1252 | 2024-11-05 02:10:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 143.6 |
| b55a4807-385f-3c6b-90fa-3680a906823b | -4.0667 | -46.9246 | 2024-11-05 02:10:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 9426fe4b-7568-3ca2-896f-b4a2a5f8d8fb | -6.1041 | -43.9593 | 2024-11-05 02:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 28b19971-ea6a-3c0e-a4ac-b3a91514056d | -4.4079 | -43.1252 | 2024-11-05 02:20:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 7bd43d78-a60a-33c1-b18f-0d2fc78b56b1 | -4.4268 | -43.1007 | 2024-11-05 02:20:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 1581527a-1eba-38ba-b2d2-b13e596f8227 | -6.1043 | -43.9362 | 2024-11-05 02:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 77bc5553-d3d2-3086-bbeb-965d2a53f182 | -4.0667 | -46.9246 | 2024-11-05 02:20:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 6363f38f-a940-3542-9ed7-b612c50e233c | -6.1039 | -43.9824 | 2024-11-05 02:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 43.9 |
| a1bf5d90-0d6e-3c8f-9d27-f7416b850275 | -6.0853 | -43.9608 | 2024-11-05 02:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 2c08213b-cb1b-3381-902e-2d08c64253e6 | -4.408 | -43.1018 | 2024-11-05 02:20:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 4f75c829-243a-3bbc-a46c-2ecbf5890e11 | -6.1041 | -43.9593 | 2024-11-05 02:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 148.2 |
| d8533317-92b6-3464-a08a-fe65f80181a5 | -6.1229 | -43.9578 | 2024-11-05 02:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 0433721a-5431-30bd-9fc1-054e01ca025f | -4.4266 | -43.1241 | 2024-11-05 02:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| cf36f957-4d53-3a43-a59c-eca177ea51e3 | -4.408 | -43.1018 | 2024-11-05 02:30:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 82b72b81-c985-3c14-8b30-545c201f9317 | -6.1041 | -43.9593 | 2024-11-05 02:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| b426d1e9-2242-38b6-afc3-1c0ea5b7a054 | -4.4079 | -43.1252 | 2024-11-05 02:30:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 74e4992d-8832-35e5-9838-a9466f7e1c78 | -3.967 | -48.15 | 2024-11-05 02:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 063a09c2-6c17-3069-bd47-23eda3eb7c09 | -1.514 | -53.512 | 2024-11-05 02:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| b60b4020-bb49-390f-93d8-3cda65e6221a | -6.1041 | -43.9593 | 2024-11-05 02:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 4d52ae5c-8805-391b-b189-9e45306e57cd | -1.514 | -53.512 | 2024-11-05 02:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 0eff1651-5a41-33ed-a8d9-4d6e5a8d9029 | -4.4079 | -43.1252 | 2024-11-05 02:40:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 48.4 |
| f3a5a565-c9c5-34f8-8bd8-de71e5dbd8a9 | -4.408 | -43.1018 | 2024-11-05 02:40:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 47.7 |
| b64e26cf-380a-3295-8725-e4cfcab47aeb | -9.6598 | -36.361 | 2024-11-05 02:40:00 | GOES-16 | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | 66.9 |
| 6c08d633-82f9-3c93-b197-30a0da5ab317 | -10.2111 | -36.7201 | 2024-11-05 02:40:00 | GOES-16 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 124.1 |
| 3a81996a-6ae2-3c28-9021-bbec3f91d217 | -6.1043 | -43.9362 | 2024-11-05 02:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 1863a67e-aa76-3f42-875b-aa3795aad653 | -6.1039 | -43.9824 | 2024-11-05 02:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 03b613b8-b08e-39ad-bacc-2538fd1b2d3a | -4.606 | -46.8758 | 2024-11-05 02:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 168528b4-5555-3b67-9668-3fc19c13c3eb | -2.82 | -52.9409 | 2024-11-05 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 4e0f376e-4a06-33fc-bdb6-422e6ee629fc | -9.6598 | -36.361 | 2024-11-05 02:50:00 | GOES-16 | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | 92.0 |
| c194aa88-ad10-303a-8285-3e9d02105c10 | -6.1041 | -43.9593 | 2024-11-05 02:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 88ef198f-57f4-3523-9e74-5c2110befc8d | -2.8065 | -51.4855 | 2024-11-05 02:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| fdb9da0d-da58-3930-8d1e-11212137ade7 | -6.1043 | -43.9362 | 2024-11-05 03:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 48.6 |
| eabd6852-37dd-3a42-b346-9113d9d735b4 | -4.6061 | -46.8537 | 2024-11-05 03:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 45.5 |
| af938c60-4571-334f-9fe0-55bfe12d757f | -6.1041 | -43.9593 | 2024-11-05 03:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 106.0 |
| e168ab13-760f-3f4e-8471-e1526db9964c | -6.1039 | -43.9824 | 2024-11-05 03:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 5cd6db6a-29a2-333b-a322-a7e0695d05d0 | -4.606 | -46.8758 | 2024-11-05 03:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 82b08c18-c492-34dd-9269-bf35ce276432 | -2.82 | -52.9409 | 2024-11-05 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| e687b6c5-db40-3e05-bc0a-0b18fd63c952 | -2.6507 | -48.5629 | 2024-11-05 03:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 20ee893f-e7aa-37b9-b3c0-453e461b7ac5 | -3.55 | -47.35 | 2024-11-05 03:00:00 | MSG-03 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a944627d-6ab5-3fdf-8fdb-457be519cafe | -3.56 | -47.4 | 2024-11-05 03:00:00 | MSG-03 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb5e8e1e-c1c3-3c4e-8a5f-d106a54c07dd | -4.606 | -46.8758 | 2024-11-05 03:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 45.7 |
| ed10f7e1-0641-3850-a5a6-48d96e06a147 | -6.1039 | -43.9824 | 2024-11-05 03:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| cea38640-1b66-34bb-a663-d40f11fbfd62 | -6.447 | -35.066 | 2024-11-05 03:10:00 | GOES-16 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 67.4 |
| 56d086a9-7f4e-3cd1-8926-a1fc2210f679 | -3.5632 | -47.3629 | 2024-11-05 03:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 117.9 |
| f1e6c358-2083-364f-b579-0dd6202b0663 | -3.5446 | -47.3855 | 2024-11-05 03:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 372.2 |
| c5f6e3fa-a2f3-3c92-a354-8628b4a430b9 | -6.1043 | -43.9362 | 2024-11-05 03:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 46.7 |
| addfbd42-d09f-3eaf-9bb2-74bbcb28002b | -3.5447 | -47.3636 | 2024-11-05 03:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 114.5 |
| b6fca676-ee61-3efe-9bc3-2159297e312c | -6.1041 | -43.9593 | 2024-11-05 03:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 131.9 |
| b476f92c-b2af-3c60-95b4-7ad1d4ece682 | -3.563 | -47.4066 | 2024-11-05 03:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 119.3 |
| 940bc8f8-d96d-3618-aa35-5cc77e0fb180 | -2.6506 | -48.5844 | 2024-11-05 03:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| f839bb83-1e5d-3153-a5e5-ce0c62fcf360 | -3.5631 | -47.3847 | 2024-11-05 03:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 372.1 |
| a8f15efc-a49e-3691-b619-b44db6059094 | -3.967 | -48.15 | 2024-11-05 03:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 821d2dde-c31f-3848-a71f-2b3a08e49ee8 | -3.5444 | -47.4073 | 2024-11-05 03:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 128.0 |
| 9e82f463-1050-3d08-8af1-48114ff33310 | -2.6507 | -48.5629 | 2024-11-05 03:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| e2f51200-8c21-3fc1-a3c8-fc601e40fe31 | -2.6691 | -48.5624 | 2024-11-05 03:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 28486a18-d3b2-3365-81bd-1574dfaacadf | -6.1229 | -43.9578 | 2024-11-05 03:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 4afdc132-884b-3795-8d9d-7ccc5124f798 | -3.78388 | -41.61238 | 2024-11-05 03:14:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1df87395-2ab7-3065-8e11-f189dad23388 | -3.31104 | -40.03906 | 2024-11-05 03:14:00 | NOAA-20 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fef71b5f-ff34-328c-bef7-0e0ee3fdac60 | -3.31823 | -40.0353 | 2024-11-05 03:14:00 | NOAA-20 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ec66e5d4-223d-3f1c-b436-baaa7ccbab3b | -3.79079 | -41.61372 | 2024-11-05 03:14:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 606d263a-4d47-3a83-a473-730944317eb4 | -3.31737 | -40.04032 | 2024-11-05 03:14:00 | NOAA-20 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0dabc6bb-d26b-3ef4-bc10-56c2f73bf1ab | -8.94111 | -40.78186 | 2024-11-05 03:17:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b4a0bf12-188e-3f2d-a4f7-fb5c575933cd | -5.8563 | -42.66975 | 2024-11-05 03:17:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1a601059-eef9-3e44-a211-ccaca163fe3b | -10.11194 | -36.21164 | 2024-11-05 03:17:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| e563eaf5-b499-30ce-8c16-cd916739e126 | -5.85428 | -39.43079 | 2024-11-05 03:17:00 | NOAA-20 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 7c0fe7aa-e327-3c10-ba57-86898c8c1c77 | -7.48867 | -37.30441 | 2024-11-05 03:17:00 | NOAA-20 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 665f783a-b1f1-3a86-b37c-9d2ef27ba470 | -12.29602 | -40.9146 | 2024-11-05 03:17:00 | NOAA-20 | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0cb8b72a-5dbd-3742-93fa-3e725dcc2e2e | -5.85319 | -39.42763 | 2024-11-05 03:17:00 | NOAA-20 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 8ee335fe-e066-3709-b364-93a225d0a1e9 | -6.69219 | -37.47649 | 2024-11-05 03:17:00 | NOAA-20 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 0.2 |
| bd5b7fe6-7e82-36a2-b941-88f188280a45 | -10.27323 | -36.3261 | 2024-11-05 03:17:00 | NOAA-20 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 192573ea-b9e5-3b50-8762-57e4bc187a19 | -11.86155 | -43.88147 | 2024-11-05 03:17:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7ed93f07-990f-37ad-af6a-653bdf38a731 | -6.19316 | -39.23273 | 2024-11-05 03:17:00 | NOAA-20 | QUIXELÔ | CEARÁ | Brasil | 2311355 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ab191ee2-41cf-3d56-abe6-951811f78721 | -6.70179 | -37.48179 | 2024-11-05 03:17:00 | NOAA-20 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 38ff94b6-73c0-3c18-8550-245b3340ed56 | -7.54171 | -35.12918 | 2024-11-05 03:17:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| fae0f05e-af63-3790-ac33-dabb0d1dcd08 | -11.9869 | -42.90653 | 2024-11-05 03:17:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3eacc8c6-9f6c-3a76-afeb-b0e13e821d21 | -7.0518 | -35.2239 | 2024-11-05 03:17:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 760f7de9-08de-3232-b1bc-5bb0c120c92e | -10.11115 | -36.21603 | 2024-11-05 03:17:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 27.5 |
| e8852f36-2c26-3c39-9600-796210b49def | -7.53741 | -35.1285 | 2024-11-05 03:17:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e787b39f-9b30-3040-8f4b-93d0c437d885 | -5.94016 | -42.67292 | 2024-11-05 03:17:00 | NOAA-20 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |


[Clique aqui para ver as próximas entradas](README11.md)
