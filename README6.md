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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6da8ae14-478b-353c-bd51-6a374f56f51b | -11.4393 | -45.1154 | 2025-07-29 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 116.1 |
| fa83d52f-900f-35f5-8e2c-7b3c7754dfa5 | -11.4389 | -45.1385 | 2025-07-29 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 3e61bd43-7ace-3736-9092-ad003a6604e0 | -11.7508 | -48.1825 | 2025-07-29 01:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 44a6b75a-0a1f-337f-82fa-e2bcf5d038d6 | -11.7317 | -48.1849 | 2025-07-29 01:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 5e5f3923-bdf7-3d45-bed4-3dd11364431c | -2.8921 | -48.2977 | 2025-07-29 01:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 3cbf4f7b-2918-3b4b-a4ff-bcf642975828 | -7.9445 | -44.0918 | 2025-07-29 01:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 7eee72dc-15f6-3058-a491-34c4bcdd6460 | -2.8921 | -48.2977 | 2025-07-29 02:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| b05d47c0-c707-36fe-8f46-743c16cee6e8 | -11.7508 | -48.1825 | 2025-07-29 02:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| cbf740a1-913a-3d5b-bd38-8c8f47d5f740 | -7.9445 | -44.0918 | 2025-07-29 02:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 66.3 |
| df27403f-8d3a-3043-93b4-521a7922e391 | -11.7317 | -48.1849 | 2025-07-29 02:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| e00715bd-812f-38bb-8e0b-edf790504cfb | -7.9256 | -44.0937 | 2025-07-29 02:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 5c5fda8f-3a74-3ff8-bd18-59ca81120cbe | -14.3988 | -59.3316 | 2025-07-29 02:00:00 | GOES-19 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 791d6b01-3c04-3bf0-92db-3fd304bf753a | -11.4389 | -45.1385 | 2025-07-29 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 2c27df04-d0b9-3084-92a3-9a148fead55f | -11.4393 | -45.1154 | 2025-07-29 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 1f17a091-c7ab-3365-a291-51febc645f47 | -11.7317 | -48.1849 | 2025-07-29 02:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 41c30034-5f69-3ef9-b6c8-9381b4f49214 | -11.7508 | -48.1825 | 2025-07-29 02:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| e5258bd8-0ae5-397a-b276-faf0e6c9776b | -14.3988 | -59.3316 | 2025-07-29 02:10:00 | GOES-19 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 301953cf-cf80-33ca-bd91-e8900a2572f2 | -11.4201 | -45.1181 | 2025-07-29 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 0b7a46f3-14b5-31e7-869b-500af6ccb939 | -11.4389 | -45.1385 | 2025-07-29 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 0ad9f59d-da5a-318d-9fcd-5068845efbd8 | -11.4393 | -45.1154 | 2025-07-29 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 077a0920-623a-3127-9a97-a240d628596c | -2.8921 | -48.2977 | 2025-07-29 02:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 103aa730-a44a-37c9-bf89-4acbab7a455d | -14.3988 | -59.3316 | 2025-07-29 02:20:00 | GOES-19 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 39.1 |
| eb0db756-e88c-395a-8597-e3d408b7e0de | -11.4201 | -45.1181 | 2025-07-29 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 45.1 |
| d4079a46-c94e-36fd-bda3-3238c0cf022e | -11.4389 | -45.1385 | 2025-07-29 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 710830fc-babe-3391-b67b-ce79107b94e8 | -11.4393 | -45.1154 | 2025-07-29 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 4b099581-d537-3f8b-b317-73d25dcce163 | -11.7508 | -48.1825 | 2025-07-29 02:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 6261f72e-f1ff-315f-ab19-650e8e7234aa | -2.9106 | -48.2971 | 2025-07-29 02:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 6e5c9e98-9c72-3926-9737-bf73011cc64c | -11.4393 | -45.1154 | 2025-07-29 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 388cb4c9-22f6-34a3-9173-de23c42e5643 | -11.7317 | -48.1849 | 2025-07-29 02:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 22feb83e-3c65-320d-9b91-9ed3d9ba9ecc | -11.7508 | -48.1825 | 2025-07-29 02:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 5a59fc7f-8969-3dd8-916e-e8deb5eda023 | -2.9106 | -48.2971 | 2025-07-29 02:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| b258896e-8e85-33ea-af29-dc644075bf12 | -11.4389 | -45.1385 | 2025-07-29 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 67728dc3-0154-3cbe-8adb-488273fd6b79 | -11.4201 | -45.1181 | 2025-07-29 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 630ddce2-d06d-3746-aa4f-2c3c0c6b2bcf | -11.7317 | -48.1849 | 2025-07-29 02:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| fcfdbfac-231b-3b3a-ac7f-be9da3272d64 | -11.4389 | -45.1385 | 2025-07-29 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| b9cd7182-3723-3785-9c96-9b3e3906f141 | -18.4486 | -54.6674 | 2025-07-29 02:40:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 74.4 |
| b252f0fe-eb74-3263-becf-054fa74fd6fd | -11.4201 | -45.1181 | 2025-07-29 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 2c504309-593c-3827-9fb2-bfca7d7fc089 | -11.7508 | -48.1825 | 2025-07-29 02:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| abf8818e-5fd7-3ab7-a26e-185a460c1b62 | -11.4393 | -45.1154 | 2025-07-29 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 98.0 |
| cdf0f5b8-07b7-3d42-8a6b-2291511eb889 | -18.4486 | -54.6674 | 2025-07-29 02:50:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 46.8 |
| c6678ac8-8989-3960-a9de-8fcb66f7f7d3 | -11.7508 | -48.1825 | 2025-07-29 02:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| da11ed31-5908-3ca2-ac58-aab55a8787f4 | -11.4197 | -45.1412 | 2025-07-29 02:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 52.2 |
| f1020603-aafd-3992-b594-992d3bee6541 | -8.9475 | -46.7577 | 2025-07-29 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| ebe9c0f6-1b9b-3981-8cb0-039b8686d972 | -11.4393 | -45.1154 | 2025-07-29 02:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 44aa3a70-ec80-3be9-9ed4-9c9d91a13f6b | -11.4201 | -45.1181 | 2025-07-29 02:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 7da1e82d-5d3f-3317-bbef-16be0b66b2db | -18.4486 | -54.6674 | 2025-07-29 03:00:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 943413c3-b250-3457-85e4-992d74e619e1 | -11.4201 | -45.1181 | 2025-07-29 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.6 |
| ec2067c9-f955-3f43-a944-47b4e9289412 | -11.7508 | -48.1825 | 2025-07-29 03:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 57bb77dd-6ef8-3c69-b8cf-b63cfc397651 | -11.4393 | -45.1154 | 2025-07-29 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 5107e0cc-e351-3eed-91cc-56a5014d06ae | -7.2408 | -43.0664 | 2025-07-29 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 40.2 |
| 404307f3-9cb7-3695-8173-7f6a8fe03c33 | -8.9475 | -46.7577 | 2025-07-29 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 8a8f4718-f0e3-3c85-a4c2-fa58ab79e425 | -14.3988 | -59.3316 | 2025-07-29 03:00:00 | GOES-19 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 53.6 |
| d64ea6d3-e7c7-3b07-92e8-d34276832812 | -2.8921 | -48.2977 | 2025-07-29 03:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 8e897d2f-93e0-3fef-bfef-4c03d9956a2b | -11.4389 | -45.1385 | 2025-07-29 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 54.1 |
| af9cbb25-ae62-350d-99e6-58038b3f402f | -9.33369 | -37.98403 | 2025-07-29 03:08:00 | NPP-375D | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e8446a24-7069-3432-9b86-ae5e497b066f | -9.33104 | -37.98063 | 2025-07-29 03:08:00 | NPP-375D | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| be599160-a887-3ea4-9f52-6ee987f3fefc | -9.33012 | -37.98551 | 2025-07-29 03:08:00 | NPP-375D | PARICONHA | ALAGOAS | Brasil | 2706422 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4c20fe47-6ed0-32a7-baee-f4eb901c3177 | -9.65446 | -40.58941 | 2025-07-29 03:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| abcba044-af78-3842-94b5-663dff2bfa5b | -9.64728 | -40.58786 | 2025-07-29 03:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5ed5ea84-2251-3f92-9ad4-fac796334565 | -9.64872 | -40.58619 | 2025-07-29 03:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5da9bbba-8d6c-301e-bc88-36e29fbda614 | -9.65591 | -40.58769 | 2025-07-29 03:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5554c47d-788f-36cb-972c-d64bb59962b2 | -14.399 | -59.3118 | 2025-07-29 03:10:00 | GOES-19 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 40.5 |
| f44c95cb-1e63-3a21-8fc2-935ccabb42b0 | -11.4389 | -45.1385 | 2025-07-29 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 82015ec0-9946-35f4-945e-4f3eb7c32d1b | -2.8921 | -48.2977 | 2025-07-29 03:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| ee293c51-5c74-364b-a99c-faa5094abc51 | -11.4393 | -45.1154 | 2025-07-29 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 2c9197d8-4e26-3e3a-bd88-f23d0c334a5f | -14.3988 | -59.3316 | 2025-07-29 03:10:00 | GOES-19 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 9abe9022-1b72-39eb-a8fe-1009800f7807 | -18.4287 | -54.6704 | 2025-07-29 03:10:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 63.3 |
| e9f3cacc-928a-323f-9a14-f9bb9d767e42 | -11.4201 | -45.1181 | 2025-07-29 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 97a76dc0-7b7d-3984-bb46-3bd1dace7fef | -18.4486 | -54.6674 | 2025-07-29 03:10:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 98.3 |
| d5e40c32-ac6e-34c7-80f6-0396f4b61fd5 | -14.3796 | -59.3333 | 2025-07-29 03:10:00 | GOES-19 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 3b293926-a76b-3a38-8cfa-8be80514fd42 | -11.7508 | -48.1825 | 2025-07-29 03:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 50.0 |
| adc24ade-3d32-34e9-a5a0-f63e0ce5c2c6 | -18.449 | -54.6462 | 2025-07-29 03:10:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 46.1 |
| a2b17f27-858f-35b5-b61d-b7407c2b0414 | -16.55575 | -40.50967 | 2025-07-29 03:10:00 | NPP-375D | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| af4434ef-2688-3ee9-a096-d1bfe0d54420 | -16.54938 | -40.50821 | 2025-07-29 03:10:00 | NPP-375D | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0f687ebf-bb96-3302-81fe-b77ae25fda08 | -11.4201 | -45.1181 | 2025-07-29 03:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| da7c9c50-8e5d-32e5-a00d-2f3ff903acb5 | -11.7508 | -48.1825 | 2025-07-29 03:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 2b688e6d-d218-34b2-91fc-8ad457f773cc | -14.3988 | -59.3316 | 2025-07-29 03:20:00 | GOES-19 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 08ccccc9-78e6-3ca3-b482-a296af7809d4 | -18.4486 | -54.6674 | 2025-07-29 03:20:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 757f2cd2-ff88-303f-8f61-0e12f5af3a41 | -7.2408 | -43.0664 | 2025-07-29 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 49.0 |
| 7d70101e-4142-3fd2-ac14-aab24c884a6b | -11.4389 | -45.1385 | 2025-07-29 03:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 4cb8b4b8-5d82-3a4c-8e72-f12a0d48831e | -7.9256 | -44.0937 | 2025-07-29 03:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 6fb5d175-903e-31b6-8dab-9b5786c851c6 | -11.4393 | -45.1154 | 2025-07-29 03:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 6f7a3eb4-0766-3003-ad5f-c16d8c3772e2 | -14.3796 | -59.3333 | 2025-07-29 03:20:00 | GOES-19 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 95.6 |
| c0b344c3-ca92-3844-8b08-51af29ebce4c | -11.4197 | -45.1412 | 2025-07-29 03:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 49.5 |
| b176664d-d9e1-3b7e-86ff-71b3abb9897d | -3.82685 | -41.55761 | 2025-07-29 03:28:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bb109a22-0dc3-3bcd-b303-732bd016a017 | -3.82185 | -41.55286 | 2025-07-29 03:28:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ceb3b4f5-5154-310c-a433-05f7b49c2b1c | -5.64657 | -44.35561 | 2025-07-29 03:28:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 95200c97-6c95-3681-9b7c-e4c89c298b75 | -5.64632 | -44.35246 | 2025-07-29 03:28:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e01aafa1-b72d-309d-8b90-3cf68cfefc9e | -3.82554 | -41.56528 | 2025-07-29 03:28:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| db147152-8eef-3e7f-8ab8-132da9577a9f | -5.18468 | -44.9567 | 2025-07-29 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6889967d-eb1b-3003-9249-52c01fd69f70 | -5.47858 | -42.15533 | 2025-07-29 03:28:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 075a7aee-77d6-390b-92aa-20fe23f9e944 | -5.35448 | -45.27616 | 2025-07-29 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5eb92574-ccfb-3917-87cc-5010025492d5 | -4.60121 | -43.31636 | 2025-07-29 03:28:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f09050ab-5bb9-3f19-b5c7-4993717b5ca3 | -5.64531 | -44.35794 | 2025-07-29 03:28:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad8e3b00-4759-32d3-a16d-691fca75d6ea | -5.34755 | -45.27499 | 2025-07-29 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de49c7fc-71a6-38a9-8e23-867cace773b1 | -4.59669 | -43.30554 | 2025-07-29 03:28:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 89bb8e7e-5580-3511-bd7a-4b0d9bb84d70 | -4.59583 | -43.31042 | 2025-07-29 03:28:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 799f7597-28da-3fcd-ad25-c3b664348b69 | -5.40782 | -45.29287 | 2025-07-29 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aa472e92-ea43-39d3-b0eb-67943136453c | -5.34681 | -45.27483 | 2025-07-29 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 983b9af0-0edd-3a43-b7ec-38a1af23f6cb | -5.35374 | -45.27598 | 2025-07-29 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README7.md)
