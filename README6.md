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
| 73c7e3be-5ba4-3d32-be26-e952f56e21ac | -4.661 | -43.7589 | 2024-10-08 00:07:58 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1128ae13-dc72-38c0-b3c0-bed3aa1942d6 | -4.4556 | -42.885601 | 2024-10-08 00:07:58 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 667ef434-7b1e-3518-9d2c-f11026249115 | -4.4443 | -42.880699 | 2024-10-08 00:07:58 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aa85e86a-b90b-3248-87cf-0e2b5ee98dfd | -4.4458 | -42.887699 | 2024-10-08 00:07:58 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1cdcae30-1efc-30e6-b5c6-48fa916b237b | -4.4474 | -42.8946 | 2024-10-08 00:07:58 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8f7263df-e9c0-358f-8258-f28372efd48d | -4.449 | -42.9016 | 2024-10-08 00:07:58 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e6dde83d-8736-397f-acb8-905e38f50600 | -4.428 | -43.038101 | 2024-10-08 00:07:59 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 53b8060a-298b-35eb-a592-afc996f86ad1 | -3.8642 | -40.766701 | 2024-10-08 00:08:00 | METOP-B | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ce510891-35b7-3542-b0cb-b98b0d552806 | -3.8659 | -40.773701 | 2024-10-08 00:08:00 | METOP-B | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 517a128c-2a89-3d06-8895-750eaaa31a3c | -4.6504 | -44.359001 | 2024-10-08 00:08:00 | METOP-B | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0e761913-71cb-305d-8101-1faafa3a3974 | -4.9209 | -45.630699 | 2024-10-08 00:08:00 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b3033c23-0821-36ef-9870-2265469be80a | -4.392 | -43.5215 | 2024-10-08 00:08:01 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5a94ff83-0529-32ee-a241-c5f6520d01cd | -3.9532 | -41.4776 | 2024-10-08 00:08:01 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 11a3c0bf-394e-3f10-a992-2f771f0b737f | -3.9548 | -41.484501 | 2024-10-08 00:08:01 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| eaebaff2-f295-38bf-95f0-769a6033bf99 | -3.9434 | -41.479801 | 2024-10-08 00:08:01 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f001d8bf-0ff1-3c26-b1f0-3d3262657deb | -3.945 | -41.486698 | 2024-10-08 00:08:01 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bd7015b2-2f45-3db5-81de-e4bab74adb67 | -5.4622 | -48.877102 | 2024-10-08 00:08:03 | METOP-B | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac1e2829-0d66-3557-9e4f-5e588f9cfeaf | -5.4525 | -48.8792 | 2024-10-08 00:08:03 | METOP-B | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81bd929d-696c-33c3-b402-6df9ca07c5c3 | -4.919 | -46.744999 | 2024-10-08 00:08:04 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 425fda76-e003-3f6a-9257-c4b065a2ab00 | -4.9212 | -46.755402 | 2024-10-08 00:08:04 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 08ff4e9e-2213-3d17-be94-7333200f0111 | -4.0379 | -43.2272 | 2024-10-08 00:08:06 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9a63866d-a2e6-3a4b-a11f-6fc522b1292b | -4.0395 | -43.2342 | 2024-10-08 00:08:06 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 494826d1-a5a9-36a4-88f2-a86df35763d0 | -4.0265 | -43.222198 | 2024-10-08 00:08:06 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c13b840a-b8f8-372e-bcdf-1eca5a65de5d | -4.0281 | -43.229301 | 2024-10-08 00:08:06 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 65d2f4c5-0b1e-3789-a7aa-13f80f65b692 | -4.0167 | -43.2244 | 2024-10-08 00:08:06 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cdd6afb5-09fc-38df-b2f5-1a4b21466fd2 | -4.133 | -43.7906 | 2024-10-08 00:08:06 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cf6a3d80-36dd-3802-b797-2c558e03ad19 | -4.1347 | -43.797901 | 2024-10-08 00:08:06 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aae12765-d232-313b-99aa-70dbda5a1763 | -5.0552 | -48.4077 | 2024-10-08 00:08:08 | METOP-B | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ac041d4-2ef9-3e5c-86a4-3aef926dc7f2 | -5.0581 | -48.421101 | 2024-10-08 00:08:08 | METOP-B | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a384c302-eef1-3b7a-adc8-ebff330b04fc | -4.4648 | -45.889599 | 2024-10-08 00:08:08 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 105f7236-bfe6-32e1-a7ca-c44e2692c456 | -4.4668 | -45.898701 | 2024-10-08 00:08:08 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ba5abf78-3c5f-3382-a981-2bb562aa08cf | -3.619 | -42.7369 | 2024-10-08 00:08:11 | METOP-B | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 45eaf806-b630-3563-84db-ee7c1d58ddab | -3.6206 | -42.743698 | 2024-10-08 00:08:11 | METOP-B | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4b8e012c-2c72-3cf2-ae61-17ab25be06cd | -3.6092 | -42.739101 | 2024-10-08 00:08:11 | METOP-B | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4aba0c39-ba36-3d55-8a15-6b84657dc3cb | -3.6108 | -42.745899 | 2024-10-08 00:08:11 | METOP-B | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b82b54a4-d90d-3b14-8936-6823bbba8594 | -4.9693 | -48.860199 | 2024-10-08 00:08:11 | METOP-B | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21283e44-ec73-3061-bbbb-9fc3d83d20b1 | -5.0054 | -49.548801 | 2024-10-08 00:08:13 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69d7d70f-4fe8-3b96-a686-e525ee85f505 | -5.0088 | -49.5648 | 2024-10-08 00:08:13 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a51f609-bd2f-35fd-9ea8-8b2926b3d212 | -4.0273 | -45.118401 | 2024-10-08 00:08:13 | METOP-B | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c6cdf33f-dbf1-3827-8955-38048a6047ad | -4.9957 | -49.5508 | 2024-10-08 00:08:13 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ddadd09-8459-38d6-b843-c3910ca370ad | -4.9991 | -49.566799 | 2024-10-08 00:08:13 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7899b86-be6e-3bd6-8b35-c1e564c52093 | -4.2698 | -46.262501 | 2024-10-08 00:08:13 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cf66fc47-e31d-3ef5-b243-3406d00860c2 | -4.2719 | -46.271999 | 2024-10-08 00:08:13 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9b45b0fa-aeef-3319-a2eb-5c0e0dd5699d | -4.4735 | -47.705799 | 2024-10-08 00:08:15 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8dad4980-9524-3084-b233-f6f0eb8df655 | -4.3142 | -47.678699 | 2024-10-08 00:08:17 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cc7dd7e-355c-35c4-8646-0a54090738f1 | -4.3167 | -47.690399 | 2024-10-08 00:08:17 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b150e9ec-9779-3c24-9e5f-eac27a16e953 | -3.6963 | -45.062801 | 2024-10-08 00:08:18 | METOP-B | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7778601b-fce5-3d69-817e-42bb362a72e6 | -3.6981 | -45.0709 | 2024-10-08 00:08:18 | METOP-B | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 14167ef3-a574-3efb-a7e4-6e2403addd39 | -3.6096 | -44.7654 | 2024-10-08 00:08:18 | METOP-B | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 701cec0d-3f38-34f6-bd1c-34e188ef715c | -3.6114 | -44.773201 | 2024-10-08 00:08:18 | METOP-B | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f2ef1584-f1e9-3c2d-a5ca-57a4545db797 | -3.6131 | -44.780998 | 2024-10-08 00:08:18 | METOP-B | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fc505765-0729-3b53-a8e8-a1a8950c7826 | -3.9363 | -46.424702 | 2024-10-08 00:08:19 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1d865893-9dbd-37ab-870c-c4038f7515e6 | -3.9384 | -46.434299 | 2024-10-08 00:08:19 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fc3153ff-b9d5-3a29-80f1-a5f901598a96 | -3.9244 | -46.417198 | 2024-10-08 00:08:19 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a30042ac-f9b8-3dc8-ba7a-a26653dd5bc9 | -3.9265 | -46.4268 | 2024-10-08 00:08:19 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9f1b049b-c73d-3d20-b4d4-9b84af0fd430 | -4.3954 | -48.660999 | 2024-10-08 00:08:19 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7302842-b9c0-3d00-aa50-ae16676f4d5d | -4.3856 | -48.663101 | 2024-10-08 00:08:20 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ddd1c1c-f50f-39d4-9c7c-9abe6b543cad | -4.0975 | -48.231899 | 2024-10-08 00:08:23 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2558cab5-4988-32f2-beae-22ad361cfaa7 | -4.0878 | -48.234001 | 2024-10-08 00:08:23 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddcd6889-6d56-356a-a4d3-4903b934b1fa | -3.9007 | -48.313702 | 2024-10-08 00:08:26 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29a0601f-7c78-3a8c-b600-509556a4b023 | -3.6995 | -47.583302 | 2024-10-08 00:08:27 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d264f07d-b9fb-33c2-a742-6662a44f7e30 | -3.8826 | -49.492901 | 2024-10-08 00:08:31 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4066aa7c-4efc-36e8-b86d-8071084a2290 | -3.8859 | -49.508099 | 2024-10-08 00:08:31 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f294f79-5169-35af-b170-4ac15b36ccc1 | -3.3013 | -46.9865 | 2024-10-08 00:08:31 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7786dbb6-11c6-3508-bf6b-39ea2dd6de06 | -3.2849 | -47.0975 | 2024-10-08 00:08:32 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65a719bd-bf8a-3939-af29-97c636e3f4cc | -3.2872 | -47.1078 | 2024-10-08 00:08:32 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d48f40e8-cf4e-3eae-9b10-a1d7829fb982 | -3.2895 | -47.118198 | 2024-10-08 00:08:32 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc6a8c52-0ba9-3f3b-b3e6-d5b1cd265203 | -3.2185 | -48.8848 | 2024-10-08 00:08:39 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0189a72d-4943-3505-8c9c-56b7a7a43c7b | -3.2214 | -48.8983 | 2024-10-08 00:08:39 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44a7620a-4b4c-3676-9b81-0ede8a2ebadb | -3.2117 | -48.900398 | 2024-10-08 00:08:40 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5fa51d5-1d67-3353-82ab-06357ca835dd | -2.7945 | -48.538898 | 2024-10-08 00:08:45 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a931316-52ab-37b6-93a4-9d6bef1693b5 | -2.7819 | -48.5285 | 2024-10-08 00:08:45 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 241b2517-55e7-3e9c-a653-52ee240bc392 | -2.7847 | -48.541 | 2024-10-08 00:08:45 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c440bc4f-be05-3575-bff3-85be4a759c9b | -2.7875 | -48.553699 | 2024-10-08 00:08:45 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1d5c2ad-33dd-3bd7-831e-986aeb31369d | -2.9855 | -49.496799 | 2024-10-08 00:08:45 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 893b3386-cce5-3b8f-a0d6-5cc55292e169 | -2.9725 | -49.4841 | 2024-10-08 00:08:46 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d467d271-f45d-3612-b75c-cc14acc05cfe | -2.9757 | -49.498901 | 2024-10-08 00:08:46 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 202ba821-64ae-320a-ac11-65c37e69d7a9 | -2.979 | -49.513599 | 2024-10-08 00:08:46 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e13584eb-991e-3d05-8877-5ecc9b6d6036 | -2.3123 | -50.4673 | 2024-10-08 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34d27a3b-49ae-3bfb-9ced-3f3fb617135d | -2.316 | -50.4842 | 2024-10-08 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| edc63307-6c4f-398e-8ffc-352a4be98daa | -1.1745 | -46.702999 | 2024-10-08 00:09:05 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ebf76b3-2ca9-30bf-9492-136e2eab9df6 | -1.1766 | -46.7122 | 2024-10-08 00:09:05 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee0c2d30-6237-3d50-a155-1d08c5079028 | -1.1668 | -46.714298 | 2024-10-08 00:09:05 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ece7f39-e87b-3413-8b64-96ddcc04b728 | 1.2731 | -50.833099 | 2024-10-08 00:10:00 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| c33d8309-5cf5-3838-8e09-1280b05665be | -2.7985 | -48.5801 | 2024-10-08 00:15:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 73fd50c2-ae68-3fdf-9e1d-05a4f30202e6 | -2.7986 | -48.5586 | 2024-10-08 00:15:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 7868ca68-9569-3b95-9fcc-1ca37e86b7da | -2.9797 | -49.5342 | 2024-10-08 00:15:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 2234c80b-8fcc-311f-bf8f-3339865bed36 | -3.2862 | -47.133 | 2024-10-08 00:15:25 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 391d4824-2f87-3a57-8db6-5dceb0889ba7 | -3.2863 | -47.1111 | 2024-10-08 00:15:25 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| a703420b-845b-32f6-b85b-f9e04b3549bc | -4.0962 | -48.2523 | 2024-10-08 00:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 33296817-6a1f-3e76-835e-3510e2e950bf | -4.4468 | -42.9123 | 2024-10-08 00:15:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 505daef2-038a-32c9-9768-ca60aa9bf843 | -4.447 | -42.8889 | 2024-10-08 00:15:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 17efb952-74e6-3505-bee6-2280fa54101b | -4.4655 | -42.9112 | 2024-10-08 00:15:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| bf7e0a69-9729-35bb-bfbc-c546f812067d | -5.4653 | -48.9141 | 2024-10-08 00:15:37 | GOES-16 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 011f29a9-c9ad-3400-8b82-c3e559f04b7b | -5.5716 | -44.8927 | 2024-10-08 00:15:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 66f16cb9-7679-3caf-9ff5-cd4c115c71d9 | -5.5718 | -44.87 | 2024-10-08 00:15:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 117.7 |
| bb7ef88b-2351-359c-b672-f17a8a9fccd0 | -5.8216 | -44.1196 | 2024-10-08 00:15:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 8aaefdb1-7977-3892-8316-be07d80c9d9b | -5.9225 | -45.3888 | 2024-10-08 00:15:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 3a43ac86-ee81-368b-9a31-bf41cc337ea3 | -6.4213 | -38.8347 | 2024-10-08 00:15:42 | GOES-16 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 149.1 |
| ec17ccea-7c45-379c-9093-94071df1507f | -6.4402 | -38.8327 | 2024-10-08 00:15:42 | GOES-16 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 97.7 |


[Clique aqui para ver as próximas entradas](README7.md)
