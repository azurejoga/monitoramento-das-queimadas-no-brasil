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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 351f47a9-7258-3cdb-863b-c6323b342c2c | -10.858 | -46.8513 | 2025-06-05 01:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| dfb21d23-fb6b-3987-8bff-dba14e631edc | -10.8386 | -46.8761 | 2025-06-05 01:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 6e32bb68-5f6d-31d2-b557-3bb21a07d2bb | -10.8576 | -46.8737 | 2025-06-05 01:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| de55f1f2-849a-3321-8da5-1bca237c571e | -7.9118 | -50.3454 | 2025-06-05 01:20:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 2c4fb6b8-1df2-30a3-a7f5-396615756709 | -11.5428 | -56.4237 | 2025-06-05 01:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 451cd03b-ae33-3237-8cbc-fc4670c2a571 | -18.8479 | -53.6251 | 2025-06-05 01:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 89.1 |
| e52f3b13-ba67-35d2-a916-9d9824eb3fdb | -10.8389 | -46.8537 | 2025-06-05 01:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| b105488e-d459-3252-bced-897864e70e1d | -18.8479 | -53.6251 | 2025-06-05 01:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 70.9 |
| eb854297-8b3a-34c6-a021-11057d0098c1 | -11.5426 | -56.4438 | 2025-06-05 01:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 5d897b93-89a7-371e-8887-b02c87940a5d | -10.8386 | -46.8761 | 2025-06-05 01:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 5d1b158c-1acb-3245-9a04-db3e3dfe066d | -7.9116 | -50.3666 | 2025-06-05 01:30:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| a350a1f3-0927-3477-9f0d-d230ec05e4f6 | -10.8576 | -46.8737 | 2025-06-05 01:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| e4155d11-9a44-32fc-ad92-21b61488cc47 | -7.9118 | -50.3454 | 2025-06-05 01:30:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 0d3d8ab6-f579-3fd2-a722-82e55cb60249 | -11.5428 | -56.4237 | 2025-06-05 01:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 43.9 |
| f93ebfb2-304a-3698-b27e-750903d17c81 | -11.5426 | -56.4438 | 2025-06-05 01:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 81914741-0b3b-30ed-b3a0-50b92afff591 | -7.9116 | -50.3666 | 2025-06-05 01:40:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 106.4 |
| d8483c41-6fb0-3f0e-8ed4-904bc60d14ed | -18.8479 | -53.6251 | 2025-06-05 01:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 0de9d224-61b7-3155-afef-3339e18c00cf | -10.8386 | -46.8761 | 2025-06-05 01:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 9840af60-04c1-3cf6-a0e3-aaaf86abbad5 | -7.8929 | -50.368 | 2025-06-05 01:40:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 69157dbc-0a7a-33b5-ae6b-7987a816b330 | -7.9118 | -50.3454 | 2025-06-05 01:40:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 3da94dff-7cd0-3e60-8e8c-19d0bb201376 | -18.8479 | -53.6251 | 2025-06-05 01:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 6efafb44-f162-34ad-9346-f9f842321bfd | -7.9118 | -50.3454 | 2025-06-05 01:50:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| f9dbea56-83cd-3ade-b787-ef307827b246 | -7.9116 | -50.3666 | 2025-06-05 01:50:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 4cb743cd-c744-3eca-a8fa-54beb0f63169 | -11.5426 | -56.4438 | 2025-06-05 01:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 3c0ac48a-b8ed-348a-80ff-7c5a9387d24e | -18.8479 | -53.6251 | 2025-06-05 02:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 48.7 |
| aa1cb569-9792-3099-a68c-de831be9c4ab | -11.5426 | -56.4438 | 2025-06-05 02:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 42.7 |
| ba5178fc-1d73-39a0-b47b-325f9f502965 | -7.9118 | -50.3454 | 2025-06-05 02:00:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 158662fe-e506-3d19-9113-4d61ca3c49f0 | -7.9116 | -50.3666 | 2025-06-05 02:00:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| b5c3d870-f55b-33e8-93a5-bd95ce8ae502 | -11.5428 | -56.4237 | 2025-06-05 02:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 29.0 |
| c247edfa-6f73-3897-bbd9-56c1277be2fd | -18.8479 | -53.6251 | 2025-06-05 02:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 51.2 |
| ac18979b-938a-3292-b535-519e5d1d5d39 | -11.5426 | -56.4438 | 2025-06-05 02:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 37.2 |
| d9c44ee1-d36f-3bda-98ae-58dea95a2b53 | -11.5428 | -56.4237 | 2025-06-05 02:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 28.3 |
| da902d05-8b2d-30f4-b0c9-64f48b689998 | -7.9116 | -50.3666 | 2025-06-05 02:10:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 126.1 |
| ad3f7547-bb6e-3fc3-b803-8a4a87daa8f7 | -7.9118 | -50.3454 | 2025-06-05 02:10:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| db19d090-898d-3d36-889b-01cb0dda0801 | -18.8479 | -53.6251 | 2025-06-05 02:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 9cc0fc76-3c52-3cc8-a96a-27b70baa3c3c | -7.9116 | -50.3666 | 2025-06-05 02:20:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 36f7d8e2-3c29-3601-9125-61d9c58bf571 | -7.9118 | -50.3454 | 2025-06-05 02:20:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| ec58278e-58ad-38ac-b703-d53ef4528c84 | -11.5428 | -56.4237 | 2025-06-05 02:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 26ca47a5-1ac8-384f-a464-393d4c7d8527 | -11.5426 | -56.4438 | 2025-06-05 02:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 39.1 |
| a419f897-0440-3717-9dfb-901506f4c85a | -11.5426 | -56.4438 | 2025-06-05 02:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 899b628e-1f5d-35af-b151-f85cd21c3ba7 | -7.8929 | -50.368 | 2025-06-05 02:30:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 663ecaa7-37d8-3f96-a581-87cee1ad64f6 | -7.9116 | -50.3666 | 2025-06-05 02:30:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| ad0a3348-da15-3c1a-9e03-e14e984ff4b0 | -7.8929 | -50.368 | 2025-06-05 02:40:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 7b7ad34c-e9c2-3592-9594-eeed5508c595 | -7.9116 | -50.3666 | 2025-06-05 02:40:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| d1a2775a-be78-3d30-b066-ed55f3b797a3 | -7.9116 | -50.3666 | 2025-06-05 02:50:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 28c19344-9db6-3149-8c22-75063153dc29 | -11.5428 | -56.4237 | 2025-06-05 02:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 3ad22c78-6e72-3773-985d-124383881438 | -7.8929 | -50.368 | 2025-06-05 02:50:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| a216e6ef-26d5-39aa-9251-16340364dc2a | -11.5426 | -56.4438 | 2025-06-05 02:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 3b0d4f8e-9965-3f2a-94f5-9e196620f88e | -7.9116 | -50.3666 | 2025-06-05 03:00:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| bed154fb-1542-3e6f-8f2a-9c34a5efccb4 | -11.5426 | -56.4438 | 2025-06-05 03:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 6928fb56-d558-3a26-a1aa-98a7c3416464 | -13.5152 | -56.569 | 2025-06-05 03:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 298.0 |
| 528abf7e-18f7-3406-bbd9-3752aa4c94e3 | -13.5155 | -56.5488 | 2025-06-05 03:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 01fe5bd0-1fc6-329c-a84a-4e906ecec8f4 | -13.5344 | -56.5672 | 2025-06-05 03:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 8a09f377-4b78-38a4-9498-73002894e800 | -13.5346 | -56.5469 | 2025-06-05 03:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 9f81e9d9-86ce-3edb-a204-4363b5903af0 | -13.5341 | -56.5874 | 2025-06-05 03:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 37.1 |
| b994a01b-624b-30c9-bf04-3470dc0726f0 | -13.515 | -56.5893 | 2025-06-05 03:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 726e7b0e-95cd-3f6a-a84d-5a5d9caa0c48 | -7.9116 | -50.3666 | 2025-06-05 03:10:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 6aaaef40-3f2b-38f8-b744-fabd126a7641 | -4.8789 | -37.50019 | 2025-06-05 03:17:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 746b4cf8-50bd-37d0-988b-839334e03f8f | -4.39455 | -38.06514 | 2025-06-05 03:17:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a4f0712f-1113-312f-83db-1b4df5409995 | -6.96804 | -42.90889 | 2025-06-05 03:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 185232c1-60a3-38e4-804f-0f616324856a | -4.8842 | -37.50105 | 2025-06-05 03:17:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c5a6df0f-6403-30b6-8d89-124e4bd42f71 | -6.96549 | -42.91044 | 2025-06-05 03:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f74fd2e4-dbdc-3102-bb14-768fbb11be66 | -6.9668 | -42.90349 | 2025-06-05 03:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1b8179d6-fb8c-3ff8-85d3-c6ae78922f62 | -4.88298 | -37.50125 | 2025-06-05 03:17:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 76188982-6551-36ee-b027-9ac8191b6190 | -6.9694 | -42.90197 | 2025-06-05 03:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 2c6cf3ce-bb58-3c92-aa8e-0757e84bf64b | -12.2911 | -43.5479 | 2025-06-05 03:19:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cda1ffe2-6779-3ccb-a68a-a6924d2e17a1 | -12.03321 | -43.72376 | 2025-06-05 03:19:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e20479e0-62b1-3866-8c07-3d0648088e1d | -13.515 | -56.5893 | 2025-06-05 03:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| fcfa1fd0-430d-3332-b79b-f4de43f9e8fa | -13.5155 | -56.5488 | 2025-06-05 03:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 8a232564-119b-3c15-a0fd-7d98bcb7f94a | -13.5346 | -56.5469 | 2025-06-05 03:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 95f053fc-1819-32a1-b7c4-201eb1806261 | -13.5344 | -56.5672 | 2025-06-05 03:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 17de813e-e929-38f1-8e32-f6b9c3547bd5 | -7.9116 | -50.3666 | 2025-06-05 03:20:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 7714dffa-06f3-339e-8723-3ae4b4715147 | -13.5341 | -56.5874 | 2025-06-05 03:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 36.1 |
| ddf02060-3cd1-33d9-90ce-cd1363788c20 | -13.5152 | -56.569 | 2025-06-05 03:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 284.9 |
| a1969bc4-2300-31d6-9218-8af9bd9267eb | -14.721 | -45.09672 | 2025-06-05 03:21:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ceea43af-7410-3fe7-865a-c1a6ed1b48cb | -14.72456 | -45.09811 | 2025-06-05 03:21:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b29f7b80-1250-36c1-aee4-00e3d550804f | -17.74966 | -42.89726 | 2025-06-05 03:21:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd42aa49-efa4-32e8-bdd6-d739e15da9dc | -22.67759 | -42.85432 | 2025-06-05 03:21:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| dfd5078c-df5b-3df2-83d5-da389f3be89f | -14.73851 | -45.1022 | 2025-06-05 03:21:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6af06de0-f359-3dc2-a099-4414f5818112 | -14.73153 | -45.10018 | 2025-06-05 03:21:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eaa703b4-e847-3806-960c-629dbf767b03 | -14.73495 | -45.10075 | 2025-06-05 03:21:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 218f6e76-902d-391a-9bae-b0b05c34a82d | -14.72798 | -45.09874 | 2025-06-05 03:21:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c37b2848-3fa3-37e6-b4ea-d5d638e204e7 | -22.67678 | -42.85796 | 2025-06-05 03:21:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fc4917b4-4517-3b52-815c-8fd62ddb5016 | -13.5346 | -56.5469 | 2025-06-05 03:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 0188d62e-bc19-38c4-96f7-5397406e0a83 | -13.5344 | -56.5672 | 2025-06-05 03:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 63d5262f-8151-398c-b1be-9c701b01df8f | -13.5152 | -56.569 | 2025-06-05 03:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 229.6 |
| ad975e1c-63cd-37cb-a484-32854cb32079 | -13.515 | -56.5893 | 2025-06-05 03:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 763c823d-8fbe-36c7-8bfe-aaa01e208a75 | -13.5341 | -56.5874 | 2025-06-05 03:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 92f1b959-ca9d-39fd-ae4a-0da760a8c0d5 | -13.5155 | -56.5488 | 2025-06-05 03:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| a122c0f5-57e1-34d9-b90d-b51e1d5c7131 | -13.5155 | -56.5488 | 2025-06-05 03:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 7de3d44a-8ad5-39e1-8c0a-523599c428ae | -13.5344 | -56.5672 | 2025-06-05 03:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 92.6 |
| d5b889b0-13ca-34bd-9b0d-8959b0b27cdc | -13.5346 | -56.5469 | 2025-06-05 03:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 40.4 |
| c0b7e017-8188-37a2-9cbb-b982479353bc | -13.515 | -56.5893 | 2025-06-05 03:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 367639b4-f387-382b-a808-6d45e724c8a5 | -13.5152 | -56.569 | 2025-06-05 03:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 186.4 |
| 764f6ab2-610e-3763-98fe-18e970d7492c | -7.54015 | -45.82628 | 2025-06-05 03:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1b682777-7ede-33d6-87c5-b5eaef616c21 | -3.9426 | -41.51543 | 2025-06-05 03:40:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a6e9e6ea-4068-32b3-9987-a82b40fe1967 | -4.81619 | -44.35635 | 2025-06-05 03:40:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac3493a7-f918-3218-bbe9-3a9b7530b260 | -7.59947 | -46.43594 | 2025-06-05 03:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 05e46051-9590-3061-a39a-6e402b999c63 | -7.69808 | -45.7788 | 2025-06-05 03:40:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 957c3861-dad7-3931-a0d2-e1eeb6e4256d | -6.20848 | -43.33632 | 2025-06-05 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README4.md)
