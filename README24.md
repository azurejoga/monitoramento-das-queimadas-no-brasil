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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a545872-176e-3b53-93bb-fa00b22dc91b | -11.4201 | -45.1181 | 2025-07-29 07:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |
| e778c142-7ced-37d3-867a-23cf7610933d | -14.3988 | -59.3316 | 2025-07-29 07:00:00 | GOES-19 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 3f43d00f-726e-387a-9146-8c22b00e3a17 | -5.0577 | -43.7352 | 2025-07-29 07:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 0ac3ae81-04bc-31df-aefc-509240f32991 | -5.0579 | -43.712 | 2025-07-29 07:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| c836fe62-9011-346b-9cf7-318ef69df156 | -5.0766 | -43.7108 | 2025-07-29 07:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| f0e874ff-b1de-35b0-afa9-567b69a3db76 | -11.4393 | -45.1154 | 2025-07-29 07:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 44c15745-6ece-3c6b-8a75-7a37356acf90 | -11.4389 | -45.1385 | 2025-07-29 07:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 95cdb47c-4242-3198-b6fb-5eb56d9d0477 | -5.0764 | -43.7339 | 2025-07-29 07:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 391dc5ae-0553-32c1-8a01-f5ef3dc16701 | -5.0764 | -43.7339 | 2025-07-29 07:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 6785f8c6-bd00-39fc-a7ff-7e627ef8d8ea | -5.0766 | -43.7108 | 2025-07-29 07:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 70336ce0-a2f8-3827-9f9d-9fac59c9f30a | -11.4389 | -45.1385 | 2025-07-29 07:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 46.5 |
| cc162b6a-44fd-3d51-abdb-134011d7f0c6 | -11.4201 | -45.1181 | 2025-07-29 07:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 0b4e9077-8db0-3cdd-88cc-f24c8069608e | -5.0577 | -43.7352 | 2025-07-29 07:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 56a62bca-6d0c-3283-b9b6-fc7be3313faa | -11.4393 | -45.1154 | 2025-07-29 07:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 2c74b22b-3136-3cc2-9869-a5061d5ba6ff | -5.0579 | -43.712 | 2025-07-29 07:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 123.0 |
| cf457679-48e2-348c-ab36-e380565e2b9b | -11.4393 | -45.1154 | 2025-07-29 07:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| de4ca622-9333-32c7-9378-3055f24b2f48 | -5.0577 | -43.7352 | 2025-07-29 07:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| f56f41dd-ab0a-3c8b-ae43-5de2d482799e | -11.4201 | -45.1181 | 2025-07-29 07:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 51.7 |
| c194c7b0-36db-352f-a47f-811dbbf1d648 | -5.0764 | -43.7339 | 2025-07-29 07:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 7ca436b3-076b-3db6-9fbb-dfc65be4c614 | -5.0579 | -43.712 | 2025-07-29 07:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 342b0dbf-6057-34e1-a86b-f583b02df546 | -5.0766 | -43.7108 | 2025-07-29 07:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 6271ddd1-a01f-3c2b-ab84-c66340772c5a | -14.3988 | -59.3316 | 2025-07-29 07:30:00 | GOES-19 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| d8645bc6-8efb-3c39-a33b-82b5d2428b11 | -5.0766 | -43.7108 | 2025-07-29 07:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| f5ad409e-3274-335d-93b7-c8ecdaf82667 | -11.4201 | -45.1181 | 2025-07-29 07:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 45bdf56a-0a99-364f-95f9-f318d5a81daa | -5.0764 | -43.7339 | 2025-07-29 07:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| a7dabadf-cc4c-3fff-92b7-cc4f68353047 | -5.0577 | -43.7352 | 2025-07-29 07:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 1ef00a40-4402-3e19-8905-5f5330d390b3 | -5.0579 | -43.712 | 2025-07-29 07:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 125.4 |
| e9c83cba-9506-32f2-a2fe-d9190a1a0f03 | -11.4393 | -45.1154 | 2025-07-29 07:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| d7ba3d58-ec0c-3c84-b3d2-71a8bedbdcfd | -5.0764 | -43.7339 | 2025-07-29 07:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 16626ea4-0385-3377-a2cd-988c4efb2503 | -5.0579 | -43.712 | 2025-07-29 07:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 052a9e58-b1c4-3289-b0fb-505f72893dfc | -11.4393 | -45.1154 | 2025-07-29 07:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 6793086f-d7eb-3311-abe2-f48a800ee46c | -5.0577 | -43.7352 | 2025-07-29 07:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 176.3 |
| c7142eb3-24b9-3bfc-b5ec-3a5032f9ef14 | -5.0766 | -43.7108 | 2025-07-29 07:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| b6fc1102-373e-3cd9-8868-7089685b25f9 | -11.4201 | -45.1181 | 2025-07-29 07:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 9536d792-b93d-3906-ba86-9bbc6066c271 | -5.0577 | -43.7352 | 2025-07-29 08:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 51070c9a-3c10-370d-a977-86197e7e88c1 | -11.4393 | -45.1154 | 2025-07-29 08:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 2129aee3-3381-36b1-90af-cf35a35bf4b7 | -11.4201 | -45.1181 | 2025-07-29 08:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 32a35661-d8fe-3744-b265-15264a37f1cc | -5.0764 | -43.7339 | 2025-07-29 08:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 9788da26-6be8-347e-8bf6-e2bba997e065 | -11.4389 | -45.1385 | 2025-07-29 08:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 46.9 |
| d122f212-edf0-3efb-a968-4fb555aba9bd | -5.0766 | -43.7108 | 2025-07-29 08:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 294b8772-7455-3e42-b9c1-24a3d2ab2d27 | -5.0579 | -43.712 | 2025-07-29 08:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 6966a274-4446-3c4a-b1ee-f2bf9e89d1ba | -11.4389 | -45.1385 | 2025-07-29 08:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 3c16c381-3f64-3071-bec9-36da4e9a7de8 | -11.4393 | -45.1154 | 2025-07-29 08:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| c5587c9f-a3f5-32d5-8374-fb3b3b6d6aed | -11.4389 | -45.1385 | 2025-07-29 08:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| c55c8c8b-bcd1-3373-80e3-7e6314953155 | -5.0579 | -43.712 | 2025-07-29 08:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| e47ce986-45e8-33f4-bdcd-e892d6ae6234 | -11.4393 | -45.1154 | 2025-07-29 08:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 026ac992-e6b8-3b0f-9c4b-4ebf7549f8d3 | -5.0764 | -43.7339 | 2025-07-29 08:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 9d0b71d7-d9e2-3ffe-9d9c-80344ad03fa3 | -5.0766 | -43.7108 | 2025-07-29 08:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 387a766e-250b-3c4e-bfde-ddd4837488bb | -5.0577 | -43.7352 | 2025-07-29 08:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| bd1a1dd0-2812-331f-9cd8-a7ce09727101 | -11.4389 | -45.1385 | 2025-07-29 08:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 9ef26b60-fcb0-3217-8d37-426df5d3cba1 | -11.4393 | -45.1154 | 2025-07-29 08:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| e6039352-2e14-36b5-8a9f-cd9abc1ed6f0 | -11.4389 | -45.1385 | 2025-07-29 08:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 4f3944d8-8860-3560-abbc-93c722f604f9 | -11.4393 | -45.1154 | 2025-07-29 08:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 0c71946d-22f7-3936-ad44-cb083c389f3c | -5.0577 | -43.7352 | 2025-07-29 09:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| bdd960ee-6410-3584-b0ab-fbbd28c324da | -13.5053 | -45.6263 | 2025-07-29 12:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 378e68b5-801b-3144-be1f-32803f15d143 | -13.5053 | -45.6263 | 2025-07-29 12:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 0dc55b96-07da-3020-9c1d-664ceb1f40b0 | -13.5058 | -45.6032 | 2025-07-29 12:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| af8811bc-63f5-312e-a0c6-3bfc40a82247 | -6.9456 | -44.2342 | 2025-07-29 12:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 8ec1a6f6-2c41-3177-947d-3bb3098b650d | -13.5053 | -45.6263 | 2025-07-29 12:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 181.8 |
| e1c24473-f3a5-3bf3-a216-7190009ba780 | -5.85721 | -44.22469 | 2025-07-29 12:29:00 | TERRA_M-T | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 799af64b-6b96-3b9d-a145-9db19a0cf1c9 | -3.4253 | -43.28207 | 2025-07-29 12:29:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 82436ecc-dcca-3de2-98d5-3acf8ed702de | -3.89369 | -43.21099 | 2025-07-29 12:29:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 31c199b6-a50c-3ce5-9a1f-3ba1df60f5a4 | -4.32691 | -48.38247 | 2025-07-29 12:29:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 24b5d11d-d565-3750-adb2-ba5e4d57c57a | -2.5143 | -47.71032 | 2025-07-29 12:29:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 4631c74f-fa76-390b-b70c-64b9e417b109 | -5.06492 | -43.72339 | 2025-07-29 12:29:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 119.5 |
| dd026cd1-4d0d-30e1-8a1f-ce071e7def52 | -4.32565 | -48.39125 | 2025-07-29 12:29:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 6dd09667-50b4-38f5-8c3c-2ee775f00188 | -3.10784 | -47.49434 | 2025-07-29 12:29:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| c0f25291-a182-3827-9390-cd877477acf8 | -3.11438 | -46.79662 | 2025-07-29 12:29:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 2de9b9d2-6e6b-3876-a7fa-bed6a175adbf | -4.54039 | -42.95226 | 2025-07-29 12:29:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| fb1fea7e-eda2-3cba-91c0-7b503bceffbd | -2.81558 | -49.19901 | 2025-07-29 12:29:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 26c184ac-55e0-30fc-a803-a330064d0c10 | -5.85705 | -44.23063 | 2025-07-29 12:29:00 | TERRA_M-T | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 6b7101e4-2b6c-3d4c-bca0-340263e5a436 | -3.00098 | -49.31955 | 2025-07-29 12:29:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 15854649-2024-379b-9c0d-17b90deb0c8b | -13.5053 | -45.6263 | 2025-07-29 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 038cd9f5-3c9c-32cf-8afe-00cd8cbeb76f | -6.5033 | -45.2992 | 2025-07-29 12:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 132.3 |
| b8f361a2-5152-3bcc-995a-6ddd68bc9d3e | -6.9456 | -44.2342 | 2025-07-29 12:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 6ecbbf58-5db7-3650-b275-d31e7c90d61d | -14.4943 | -46.5387 | 2025-07-29 12:30:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 77.1 |
| e952f111-9cf4-3c8f-a172-082d9b636090 | -13.5058 | -45.6032 | 2025-07-29 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 61c0c5cc-e0ae-33c2-ab35-cb6cc0cddc6a | -7.60437 | -44.8186 | 2025-07-29 12:32:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7297a644-3a43-3f6b-ae13-d82fb2144781 | -7.79241 | -44.95618 | 2025-07-29 12:32:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 744c9ea7-0377-3cb1-9681-f829dbd386ab | -13.49718 | -45.59632 | 2025-07-29 12:32:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 792786f7-b291-3aff-bfe6-6c57f0a79f86 | -12.27069 | -47.00227 | 2025-07-29 12:32:00 | TERRA_M-T | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 49e12d30-9798-3f4d-b0cb-6d399382a475 | -6.91441 | -44.73652 | 2025-07-29 12:32:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 505a0260-5dc2-3daf-a819-0c1379997054 | -12.36688 | -49.9773 | 2025-07-29 12:32:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 80b436f9-7e12-3cdb-aea7-546ad9c59d41 | -12.02442 | -46.93326 | 2025-07-29 12:32:00 | TERRA_M-T | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 4a458e9d-b8fc-35f4-8140-fe719f6592c7 | -6.50073 | -45.31992 | 2025-07-29 12:32:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 5b31c25a-6eec-3cb1-a936-ad72bca68977 | -12.9573 | -46.89879 | 2025-07-29 12:32:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 353d28b4-24c9-3265-be7b-7c94698690ee | -7.31049 | -46.7188 | 2025-07-29 12:32:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 087f1043-003b-3610-82a0-245ea08791df | -8.63582 | -45.52743 | 2025-07-29 12:32:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 3746c810-dc8d-35ae-95ff-0551ac0e0bac | -10.18051 | -47.66905 | 2025-07-29 12:32:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 86996470-20da-3156-a5e1-7ac46c9461a4 | -6.94796 | -44.22607 | 2025-07-29 12:32:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 6aa8f8df-02bc-3946-ab69-f9f8027cab41 | -7.30902 | -46.72941 | 2025-07-29 12:32:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f67deba1-1bb1-3511-9ee7-beb92da0cfd0 | -13.14402 | -47.34671 | 2025-07-29 12:32:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0fb03d0f-5f7e-3f2b-9a54-8a27a0090d9a | -9.64974 | -47.92426 | 2025-07-29 12:32:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 05be1177-f92a-3863-bb43-582a2f5906bb | -6.12813 | -47.72675 | 2025-07-29 12:32:00 | TERRA_M-T | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 7e3ee809-ef44-375a-8c26-3884fbe04700 | -6.54167 | -49.86793 | 2025-07-29 12:32:00 | TERRA_M-T | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1d067ced-bab6-3156-bda6-53ced57337cc | -10.93964 | -45.79248 | 2025-07-29 12:32:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 14eeb948-4f07-31ef-94ba-0ccc6a6daa34 | -9.92062 | -47.75874 | 2025-07-29 12:32:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| ecfa2d35-aa2a-302e-9371-8bbfda5162c3 | -9.82727 | -41.7877 | 2025-07-29 12:32:00 | TERRA_M-T | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 24.7 |
| e79aae87-3ae8-3828-b405-b5e024b24900 | -9.65111 | -47.91442 | 2025-07-29 12:32:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 1d663292-2477-3b67-923e-64e4c2d1369e | -7.8591 | -47.87364 | 2025-07-29 12:32:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |


[Clique aqui para ver as próximas entradas](README25.md)
