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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be567123-08dd-397d-ae66-554805535c5a | -1.18224 | -53.51097 | 2024-10-28 05:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a001be7e-12bc-3485-8911-4450dd8bd0ae | -1.18217 | -53.51479 | 2024-10-28 05:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f973e8b0-3406-3485-8c74-de44317f7cbf | -1.17719 | -53.50407 | 2024-10-28 05:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5623e48f-d0e8-3e6d-a6b5-acf19393c411 | -1.17644 | -53.50518 | 2024-10-28 05:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 722c41b7-0fd2-31ed-93d3-6950042872f5 | -1.17643 | -53.50889 | 2024-10-28 05:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a9ceb7f5-ee51-3af4-b419-494a60917ce3 | -1.17574 | -53.50987 | 2024-10-28 05:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 56cc857b-1944-3978-aa15-d0c77e48fa3c | -1.17568 | -53.51365 | 2024-10-28 05:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7a2fbc03-7deb-3611-af9e-f8c49cff5431 | -1.17069 | -53.50293 | 2024-10-28 05:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c9f27541-70d6-39ef-8f82-fae7c7d88f33 | -1.16995 | -53.50402 | 2024-10-28 05:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c5b17900-88bf-3f28-9b8e-0085b95c7b91 | -1.16992 | -53.50785 | 2024-10-28 05:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 27201cf0-1ca3-33d7-83f7-1af83c36a2e6 | -1.08528 | -53.66851 | 2024-10-28 05:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4cc0c968-d9db-38a4-99d4-ff42328635d5 | -1.0845 | -53.6736 | 2024-10-28 05:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 953df71d-9735-3778-9a6a-9631b4531d87 | -1.08027 | -53.65815 | 2024-10-28 05:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| da0d9bad-eb60-3eae-b55d-59432354c2ff | -1.07947 | -53.66341 | 2024-10-28 05:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e6e244ba-344e-3725-b9a7-0db66a56bbde | -1.07886 | -53.66046 | 2024-10-28 05:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7d8ff408-0cb1-3a2a-b138-0247c62a4d64 | -1.07876 | -53.66805 | 2024-10-28 05:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b5a6b0ba-fa56-3370-ba5c-fad3af117994 | -1.07807 | -53.66539 | 2024-10-28 05:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 020ca61e-a788-3293-888a-a0076b313029 | -1.078 | -53.673 | 2024-10-28 05:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2fef986b-7eb2-3cbf-a9b6-04dd0d916828 | -1.07733 | -53.67005 | 2024-10-28 05:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0116e775-ee52-3cbb-a67f-f52513731738 | -1.07649 | -53.6753 | 2024-10-28 05:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cb2d37f4-fc5b-3947-a339-ad948e15ed48 | -0.98673 | -53.70173 | 2024-10-28 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4e484eec-530a-34b6-a90f-92c2caeb4ef1 | -0.98589 | -53.70722 | 2024-10-28 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5c1d4810-8062-3aa6-bd44-1a5e971abb77 | -0.98498 | -53.7131 | 2024-10-28 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 677035a6-e4c7-32e2-bab8-02dd9a0d76b3 | -0.98028 | -53.701 | 2024-10-28 05:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65af6184-38e4-3c04-bb67-36424ffb68c0 | -0.97948 | -53.70612 | 2024-10-28 05:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c960f0ec-2002-31ac-a138-c3843ffa2d77 | -0.97854 | -53.71222 | 2024-10-28 05:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c1eaf856-e9bc-3930-9c02-26a4e0f8e43c | -7.65734 | -63.45699 | 2024-10-28 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8d152f7-66d1-364f-ab75-c6b8ce5f1197 | -7.64179 | -63.44759 | 2024-10-28 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78729c3c-aa6b-36c8-96fe-a6dce9f31fa3 | -7.64112 | -63.45205 | 2024-10-28 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8aaf6cc5-467b-3781-b74c-589c8b70b9ed | -7.64045 | -63.45652 | 2024-10-28 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac02f18b-ea46-378b-aeff-16c868cecebf | -1.9763 | -52.0804 | 2024-10-28 05:55:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| dcd05bfd-929b-384f-ad01-186e1d6ad1ee | -2.2662 | -53.7825 | 2024-10-28 05:55:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| d64b228a-7084-39f4-b7a2-0ef79b8d1039 | -2.5127 | -51.1821 | 2024-10-28 05:55:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 5ac162c6-ffef-3619-b1a1-56a1b348ed78 | -2.833 | -49.2413 | 2024-10-28 05:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 7cfc12bc-748c-3e38-a479-8851fb1c0652 | -2.8699 | -49.2615 | 2024-10-28 05:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 6d2dbf38-1251-32c2-8a36-0b9f57ce6050 | -2.8884 | -49.2609 | 2024-10-28 05:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 956fd2e0-ce8f-350e-9a95-43ac16e5cec4 | -3.0317 | -50.4176 | 2024-10-28 05:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| baaf0fe5-3d19-3d5f-8af6-d0c23e61b1aa | -3.497 | -45.7971 | 2024-10-28 05:55:25 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 873ae9b6-4396-35ae-8fa0-8ee47c3ccf45 | -3.5155 | -45.7964 | 2024-10-28 05:55:25 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 82.3 |
| ae1bf765-8ca2-3d3c-9266-d316d6e61ff1 | -1.9763 | -52.0804 | 2024-10-28 06:05:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| f80db1a7-d880-302c-bc24-695d46af6abf | -2.2662 | -53.7825 | 2024-10-28 06:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 9d98e5ee-2b06-33a4-8e4d-5d1e4cce9aa3 | -2.5127 | -51.1821 | 2024-10-28 06:05:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 12790a0f-420e-3c9d-9d85-eb96ac2c77cf | -2.5311 | -51.1816 | 2024-10-28 06:05:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| f6f784a9-7ce5-339f-8920-109ec21883ac | -2.833 | -49.2413 | 2024-10-28 06:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 044ab7ac-7ce6-3da1-9fe3-b840cea02518 | -2.8699 | -49.2615 | 2024-10-28 06:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| e8354fb7-4a06-3cb4-801a-f4ba26720ca8 | -2.8884 | -49.2609 | 2024-10-28 06:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 36c9c7a7-6e26-3c57-ae03-a0a0174198b1 | -3.0317 | -50.4176 | 2024-10-28 06:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 9cd15f11-652d-3b6d-baa7-662c2e0cf762 | -3.5155 | -45.7964 | 2024-10-28 06:05:25 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 0c756381-ee7d-34e8-ab0e-7d4ea2fa443d | -1.9763 | -52.0804 | 2024-10-28 06:15:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 13cf03c8-5fd0-37c9-b5cf-b7b4b3bc844c | -2.2662 | -53.7825 | 2024-10-28 06:15:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 1a704d11-634a-3c45-b1e9-4b3b278d8204 | -2.5127 | -51.1821 | 2024-10-28 06:15:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 004225bc-c987-3c1e-9b34-880c64228f40 | -2.5311 | -51.1816 | 2024-10-28 06:15:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| f92b81c5-2127-3df9-a38b-d88824a54171 | -2.833 | -49.2413 | 2024-10-28 06:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 6544961f-bb2d-3317-aa8e-c7bd1f725df2 | -2.8699 | -49.2615 | 2024-10-28 06:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 53cba2e4-8dce-35b6-aca8-04149fd7a512 | -2.8884 | -49.2609 | 2024-10-28 06:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| f50e3715-42f7-3882-97c8-19e9c44611f2 | -1.9763 | -52.0804 | 2024-10-28 06:25:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 9c8f6d2a-6a8f-3fbe-a0bc-c5b725bc3966 | -2.2662 | -53.7825 | 2024-10-28 06:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 73cddadb-49d2-392d-811c-0b2e10a67eff | -8.10303 | -38.85557 | 2024-10-28 11:34:00 | TERRA_M-M | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 34.6 |
| 117e7635-680a-3052-b12b-9dc60c19f3e1 | -15.3679 | -40.2002 | 2024-10-28 11:56:33 | GOES-16 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 111.1 |
| d85ee64e-943b-3ab0-900e-d57415753449 | -2.2703 | -46.1068 | 2024-10-28 12:15:19 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 2dc7b91d-f030-379e-a06e-1fa815cb0aee | -2.2702 | -46.1291 | 2024-10-28 12:15:19 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 97583185-9263-382b-8eaa-f247bc24abef | -2.2889 | -46.1063 | 2024-10-28 12:15:19 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 71da1dbf-2cfb-3931-91cb-0587241beced | -2.2888 | -46.1286 | 2024-10-28 12:15:19 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 63.9 |
| f8557e25-9866-380d-85c6-cfd80a39d60d | -2.2888 | -46.1286 | 2024-10-28 12:25:19 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 166b9354-6c16-3071-9b91-98e2a1f47826 | -2.2703 | -46.1068 | 2024-10-28 12:25:19 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 134.5 |
| 202a547d-894b-3872-9c9e-519e95a5764b | -2.2889 | -46.1063 | 2024-10-28 12:25:19 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 5df9bc07-2142-3e5e-9774-f00d27453d1f | -2.2702 | -46.1291 | 2024-10-28 12:25:19 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 169.7 |
| 2c2e19de-6e34-3264-a588-ad7a4ad63307 | -2.2888 | -46.1286 | 2024-10-28 12:35:19 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 69.6 |
| e5679ec9-bd14-38bf-a9c0-1378666cb6f7 | -2.3578 | -47.6641 | 2024-10-28 12:35:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 9554a47e-949a-3f9a-853e-4e8fc0fc006c | -2.2889 | -46.1063 | 2024-10-28 12:35:19 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 2e7df6cd-e17a-3ecb-8ec9-c359c1f79b82 | -2.3763 | -47.6636 | 2024-10-28 12:35:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 133.1 |
| 1be99097-e73d-3dfd-8a31-65b34d8b80c4 | -2.2889 | -46.1063 | 2024-10-28 12:45:19 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 0fbc710d-b9ce-3750-9b95-eed9c9a90611 | -2.3578 | -47.6641 | 2024-10-28 12:45:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| d8242a4b-3c33-3e02-b483-75b414f7ae38 | -2.3919 | -48.5484 | 2024-10-28 12:45:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| eda78bb6-dde6-33f5-b8d5-ab0961326c4b | -2.3762 | -47.6853 | 2024-10-28 12:45:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 23689e34-128f-34d0-bcce-cc81fe6bc238 | -2.3763 | -47.6636 | 2024-10-28 12:45:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 181.0 |
| f72e8ec0-fbe1-3c37-b5de-40b951c2911a | -2.4104 | -48.5479 | 2024-10-28 12:45:20 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 75097168-35af-318e-9426-5babbb673702 | -2.3763 | -47.6636 | 2024-10-28 12:55:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 119.9 |
| 03aa5ce0-916e-326f-82a6-de23856f84e0 | -2.3734 | -48.5489 | 2024-10-28 12:55:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| abf6e227-4b8c-3863-bc99-744f3eb918b2 | -2.3578 | -47.6641 | 2024-10-28 12:55:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 5df87f9c-7207-31f8-a325-fc78e18118ec | -2.3762 | -47.6853 | 2024-10-28 12:55:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 33121173-fa52-33ec-be65-d62a984a353e | -2.4104 | -48.5479 | 2024-10-28 12:55:20 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 58d789f5-1f28-3911-aa04-db127f785126 | -3.8412 | -44.1513 | 2024-10-28 12:55:28 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 84163ca6-86c6-3869-8e0f-961210c65d30 | -2.3578 | -47.6641 | 2024-10-28 13:05:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 50b13df0-94f4-3455-8772-e47f26dfb552 | -2.3762 | -47.6853 | 2024-10-28 13:05:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| c7a1e013-f7a8-35a8-9aae-4d7922155f40 | -2.3763 | -47.6636 | 2024-10-28 13:05:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 141.8 |
| 7ea2a55d-69a6-355c-a4db-c043109da1bd | -2.3919 | -48.5484 | 2024-10-28 13:05:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 8d3ad84b-207f-3b9f-8ed6-9b14720b9708 | -2.4104 | -48.5479 | 2024-10-28 13:05:20 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 174cadd0-84e6-3b59-9c45-789c825b0ea8 | -2.8885 | -49.2397 | 2024-10-28 13:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 265d532f-a0ce-30ab-85eb-090aed6c5ccc | -3.8225 | -44.1522 | 2024-10-28 13:05:27 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 7011110e-8aed-326e-a321-4bc48dcdcce9 | -3.8412 | -44.1513 | 2024-10-28 13:05:28 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 130.3 |
| faae4756-045d-380d-a472-a8384902fbbc | -12.8883 | -44.6143 | 2024-10-28 13:06:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| de7dc1fa-751a-3fc9-b67c-4c28fe4817b1 | -13.1898 | -43.0957 | 2024-10-28 13:06:20 | GOES-16 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 98.9 |
| 2f2767ef-1498-3dc2-b067-b2367a1b9c33 | -2.3578 | -47.6641 | 2024-10-28 13:15:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 3572ea48-437f-321f-9f4a-899ce9f8717b | -2.2513 | -46.2405 | 2024-10-28 13:15:19 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 103.9 |
| fec2de31-21f9-331c-92fd-6600227a18e4 | -2.3919 | -48.5484 | 2024-10-28 13:15:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 5c73cbf1-aa64-375a-9c8e-fdaace2da61e | -2.3763 | -47.6636 | 2024-10-28 13:15:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 134.6 |
| 3fafa1c2-ee25-3084-a55d-72fe68ac8a07 | -2.4104 | -48.5479 | 2024-10-28 13:15:20 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 583adf85-c614-3584-8e98-bc48ccb4d282 | -2.8885 | -49.2397 | 2024-10-28 13:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 127.3 |
| 2ec3a34c-d01a-3881-a86a-832cfbfbc69e | -2.7929 | -45.3533 | 2024-10-28 13:15:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 108.9 |


[Clique aqui para ver as próximas entradas](README86.md)
