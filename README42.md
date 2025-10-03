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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe0c1617-ffa9-368e-b4f1-491508da2322 | -18.80681 | -43.66199 | 2025-10-03 03:47:00 | NOAA-21 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d3018772-ad9b-30ca-9024-1d905bfd17e0 | -18.44921 | -43.70776 | 2025-10-03 03:47:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1a526184-bb1c-3ab0-a594-e7b21d253fe0 | -21.5893 | -45.28035 | 2025-10-03 03:47:00 | NOAA-21 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 754d9eae-f350-3de1-a651-59ecce73e8e4 | -20.06111 | -45.10568 | 2025-10-03 03:47:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 960644af-c736-37b2-ba52-f3529f371073 | -18.65311 | -43.87592 | 2025-10-03 03:47:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b0c9547-ad9a-342a-9175-839f726c8f1e | -19.90153 | -44.5073 | 2025-10-03 03:47:00 | NOAA-21 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| c11d2bf2-5f3f-3c95-989e-90d0f8af4ac5 | -19.72307 | -45.92171 | 2025-10-03 03:47:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a40aa1f4-f620-3df9-94b0-457a58060bf9 | -20.11506 | -44.39447 | 2025-10-03 03:47:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fbad9544-562c-3159-8856-2269085cf26f | -19.85491 | -46.1928 | 2025-10-03 03:47:00 | NOAA-21 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04f4c52a-f9cf-3803-9f67-576bba246a9e | -20.37919 | -44.13038 | 2025-10-03 03:47:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 89342688-d343-3ce1-8aea-8020614b6c12 | -19.84152 | -44.03895 | 2025-10-03 03:47:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e59474c6-0cc1-344e-9fa6-ff0448e99333 | -19.87242 | -43.65261 | 2025-10-03 03:47:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e6cd5fa3-9e8e-3c6a-bd66-9f5c8ba9deac | -16.29759 | -45.24261 | 2025-10-03 03:47:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d9500f35-7ecf-37a0-94ec-dcd7594108bc | -12.6323 | -46.9697 | 2025-10-03 03:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 2f9b0f7d-1163-3e01-847f-a8ac51f2700c | -10.931 | -47.0434 | 2025-10-03 03:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 635671ad-d12a-39f0-bd16-f3f48d994c4b | -7.7496 | -46.2496 | 2025-10-03 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 414.0 |
| c3aa5f7b-d228-38ce-b9a3-21a6956acdc8 | -13.7764 | -47.5617 | 2025-10-03 03:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 83.0 |
| b6f1e2ad-3989-33cb-90e0-522f4198a4c0 | -12.6319 | -46.9923 | 2025-10-03 03:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 59547b64-2604-3d02-a2f1-08eb9df85746 | -14.9342 | -46.8965 | 2025-10-03 03:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 5895f1ae-eb86-378c-bb17-5685bfbb9f82 | -13.776 | -47.5843 | 2025-10-03 03:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 29089757-5ed2-399a-b437-ea54797b6047 | -7.7746 | -47.3792 | 2025-10-03 03:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| cc3f87d9-93d2-34d4-82d1-f85c5af10736 | -8.6138 | -54.976 | 2025-10-03 03:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 19c484b3-a11b-33ac-94f0-8bc2b1a60c40 | -9.0808 | -46.6545 | 2025-10-03 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 7b976e1d-d557-3066-a9bc-a7ddfbd9e296 | -7.7494 | -46.272 | 2025-10-03 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 219.3 |
| 14c87f0b-7b05-34f2-a70c-d5b7271877ce | -7.7749 | -42.5628 | 2025-10-03 03:50:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 78.1 |
| 964ec207-1cc8-3118-b7ee-b0223e99665d | -7.7563 | -42.541 | 2025-10-03 03:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 94.5 |
| 7d92871f-aa7b-3a3d-a775-a92ff1836471 | -10.8982 | -46.7117 | 2025-10-03 03:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 0bb04a58-e44b-3b0d-b84b-3809ab71fa57 | -7.7746 | -42.5865 | 2025-10-03 03:50:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 120.7 |
| 0a51448c-7643-3161-822f-4405ca571a25 | -4.669 | -45.8066 | 2025-10-03 03:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 366.8 |
| 81d88c57-9bb2-3787-8bcd-b5042c3e7cd7 | -7.756 | -42.5648 | 2025-10-03 03:50:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 173.8 |
| 4446c31b-52f5-36fd-9f8d-84643767cfb1 | -7.7499 | -46.2272 | 2025-10-03 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 73a0213d-d336-3828-b9ae-451cf33edc14 | -9.062 | -46.6565 | 2025-10-03 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 08a22115-4107-32c9-95fa-bbdf7f9d61a9 | -7.7557 | -42.5885 | 2025-10-03 03:50:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 94.0 |
| ce5b6d44-05cd-3f9d-899e-3c647352d206 | -10.0148 | -50.2443 | 2025-10-03 03:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 780d1585-694f-316e-97e0-f8dd2b277b4a | -10.9314 | -47.021 | 2025-10-03 03:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 43f63580-33ce-347b-850f-e19a0c660669 | -10.9123 | -47.0234 | 2025-10-03 03:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 181.3 |
| b773484d-3558-3d0b-88e7-809870bc0d40 | -7.7682 | -46.2703 | 2025-10-03 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 011ac736-4850-3d15-b02f-0b383c86e2bb | -4.6692 | -45.7842 | 2025-10-03 03:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 265.5 |
| a7c13d77-33cd-35e4-a450-af5fc195f185 | -12.6127 | -46.9951 | 2025-10-03 03:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 970b8e21-1365-360b-8667-a1e4f2008877 | -10.912 | -47.0458 | 2025-10-03 03:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 183.3 |
| a4efb2da-7ce4-3c26-a001-9f30baef3f99 | -12.6131 | -46.9725 | 2025-10-03 03:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| c3849a45-1dd2-32fa-b49c-bf2f716884a8 | -11.9163 | -46.2817 | 2025-10-03 03:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| ec12eb96-69ef-3966-9a6e-1b7a057148e6 | -4.6504 | -45.8077 | 2025-10-03 03:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 197.9 |
| 253a4ccc-9c8f-3ab8-ab4a-68ab9b0fe0dc | -4.6505 | -45.7853 | 2025-10-03 03:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 171.9 |
| 0212b298-15fc-32d7-bd25-bcaed77ee0d3 | -7.7684 | -46.2479 | 2025-10-03 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 228.1 |
| 02295ca8-1488-35d5-9f7e-d5c3604027c3 | -7.7496 | -46.2496 | 2025-10-03 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 5211af47-7690-3dca-a192-ad0515020319 | -10.1569 | -45.493 | 2025-10-03 04:00:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 338cef29-89f4-3c8a-aa04-53cbed0513ef | -7.7749 | -42.5628 | 2025-10-03 04:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 105.8 |
| 632498a6-b814-3ff6-95a2-5a09b60c179b | -4.6505 | -45.7853 | 2025-10-03 04:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 88.6 |
| fc26a6ad-63eb-3ca4-8811-000cbdc87e17 | -9.062 | -46.6565 | 2025-10-03 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| c343a2c7-8c0c-3034-ab15-4e4d892b5a6c | -12.6131 | -46.9725 | 2025-10-03 04:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 155.1 |
| d4cd61a1-d139-3658-8a35-c15eccf8ca3f | -7.7563 | -42.541 | 2025-10-03 04:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 80.9 |
| 50074dcc-85d6-3688-b299-2b09aac3e16d | -7.7746 | -42.5865 | 2025-10-03 04:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 143.5 |
| aaa55f0f-dbf8-3e7d-9930-5cf424c022b6 | -12.6319 | -46.9923 | 2025-10-03 04:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 40162e35-06ae-39a1-a610-fcc4671bf26d | -7.7684 | -46.2479 | 2025-10-03 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 119.8 |
| ab8279f7-d175-36c0-9f14-7909b9f7781a | -10.912 | -47.0458 | 2025-10-03 04:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 173.6 |
| cc2d2dbc-4690-3211-ac90-aecaa8719c52 | -12.6127 | -46.9951 | 2025-10-03 04:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 659bae89-5629-367f-be49-f69d692aa101 | -10.9314 | -47.021 | 2025-10-03 04:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 29af02db-784a-3870-aea6-875cea29c5d4 | -7.7557 | -42.5885 | 2025-10-03 04:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 81.4 |
| d282cdcf-c927-34a8-88b1-b6e6b4e03f7e | -7.756 | -42.5648 | 2025-10-03 04:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 183.8 |
| 97f3bf47-ea38-3795-a8b0-48cf1e716174 | -14.9342 | -46.8965 | 2025-10-03 04:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 5554ad8f-833e-3d85-b06c-6c76424da54c | -4.6504 | -45.8077 | 2025-10-03 04:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 68.3 |
| c3955de0-f9ba-3f0c-b797-b87aac3cdda0 | -4.6692 | -45.7842 | 2025-10-03 04:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 2a0d15a6-352d-3aed-a679-2bf84069fb3c | -4.669 | -45.8066 | 2025-10-03 04:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 84.7 |
| f6822be7-4bb1-3dbb-9644-9344a7b37f95 | -10.9123 | -47.0234 | 2025-10-03 04:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 168.8 |
| c6ed4fbd-469a-3735-b442-4589d54051dd | -7.7371 | -42.5668 | 2025-10-03 04:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 79.8 |
| 6dad04ff-bd60-3286-ad2a-20194e21d8f1 | -12.6323 | -46.9697 | 2025-10-03 04:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 2cf0a36a-3989-3a00-ab60-23ec7ff29657 | -10.931 | -47.0434 | 2025-10-03 04:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 978df909-a281-3141-8e4f-683e5f49ff6c | -11.9163 | -46.2817 | 2025-10-03 04:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| f57e2f56-41c1-3bdc-84a9-a2f47978f58d | -9.0808 | -46.6545 | 2025-10-03 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 6cd27283-0a69-31c4-bedb-4c6404e1b880 | -13.1345 | -47.882 | 2025-10-03 04:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| e4a31365-4123-3ef6-98d1-f69f27af225a | -14.7083 | -43.8869 | 2025-10-03 04:00:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 72.5 |
| 77117c7a-fa95-3001-9f62-28201088ec0a | -10.9363 | -46.7068 | 2025-10-03 04:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| c44a0135-496d-3950-a216-c205ade0806c | -11.9163 | -46.2817 | 2025-10-03 04:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 7e453095-03f9-3d4c-82bd-f4bdb3b7eca4 | -14.9342 | -46.8965 | 2025-10-03 04:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 26066751-0a33-3889-be67-76b3836bb530 | -7.756 | -42.5648 | 2025-10-03 04:10:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 197.9 |
| 8dd41800-ad90-3ece-b1a6-cb437686053d | -10.931 | -47.0434 | 2025-10-03 04:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 46e27695-0c97-36ba-a3ac-ef1672f00c6c | -10.9123 | -47.0234 | 2025-10-03 04:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 48.8 |
| aa094b69-ee4e-36b8-b8b2-9ddd0cd9d462 | -10.9169 | -46.7317 | 2025-10-03 04:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 49666d84-20a1-3b46-b5cf-7525ad327ab4 | -7.7557 | -42.5885 | 2025-10-03 04:10:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 92.4 |
| e9d945e4-716b-3ddc-9e12-d6405f789aaf | -7.7563 | -42.541 | 2025-10-03 04:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 124.6 |
| 904170df-98b7-30a8-b6d8-5e5a8818e9c9 | -10.912 | -47.0458 | 2025-10-03 04:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 4b0ef004-b190-3018-ade9-4f9e7a26e26a | -9.9182 | -43.7212 | 2025-10-03 04:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 72.0 |
| 25daadfe-f4bc-3bec-9944-eacb18fd3d75 | -14.2135 | -46.0366 | 2025-10-03 04:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 8197fad1-c550-3ef8-b7fd-f55c2a60ab9b | -5.6363 | -43.9027 | 2025-10-03 04:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 04200da4-ecc4-3bd2-a97c-f1b90d6284ad | -7.7749 | -42.5628 | 2025-10-03 04:10:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 84.5 |
| 37f772a5-396b-3f95-bfa0-a957a82890c9 | -10.9172 | -46.7092 | 2025-10-03 04:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 31.6 |
| adc3e147-cd02-3a45-a853-6444119c6d0d | -6.0416 | -44.6304 | 2025-10-03 04:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 39.9 |
| c10ec34f-6b56-34ae-80cf-1c3cc3ccd730 | -7.7746 | -42.5865 | 2025-10-03 04:10:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 125.6 |
| 5143260e-f220-3f0e-8341-b4b5784a8574 | -7.7684 | -46.2479 | 2025-10-03 04:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| e82d6690-fcea-3b05-9990-b6cffd42f37b | -9.9959 | -50.2462 | 2025-10-03 04:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 2936bac0-81e2-33ff-8c6d-b5e92e50a2cd | -13.1341 | -47.9043 | 2025-10-03 04:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 524ec188-faca-34ef-ac08-5ef7de2dcf96 | -10.9314 | -47.021 | 2025-10-03 04:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 37.6 |
| cafe14d9-4052-3bd5-b602-c8061022397a | -12.6131 | -46.9725 | 2025-10-03 04:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 8480306a-c80a-3d86-9d03-efbbb961f204 | -7.7496 | -46.2496 | 2025-10-03 04:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| a1d12300-4ee0-3c96-be24-92fbf174d85c | -4.6692 | -45.7842 | 2025-10-03 04:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 57.4 |
| cd2f2829-d87a-3699-9f7a-1227d00cc37b | -13.1345 | -47.882 | 2025-10-03 04:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 162.3 |
| 58dee2db-b8f4-3934-98c4-6d0837cb4bc0 | -10.0148 | -50.2443 | 2025-10-03 04:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 33.4 |
| f3e2adf0-25f1-33b8-8711-16051f0449bb | -12.6323 | -46.9697 | 2025-10-03 04:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 6a14dfeb-5efa-3efc-830f-f00f8b1f1aa1 | -14.1936 | -46.063 | 2025-10-03 04:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |


[Clique aqui para ver as próximas entradas](README43.md)
