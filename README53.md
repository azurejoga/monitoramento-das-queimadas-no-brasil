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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68b3a812-4be1-3864-aa37-5f53dcde7ee5 | -6.6248 | -55.2331 | 2026-09-03 07:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 0aebf1bb-c06c-3905-807b-6d997077d7bf | -8.5917 | -67.1603 | 2026-09-03 07:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 99651d07-265f-38f2-b4d1-a0a9cfc88d37 | -6.6698 | -59.9443 | 2026-09-03 07:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 8c72a184-978c-37bc-b7bf-da316c97534c | -8.0924 | -50.9642 | 2026-09-03 07:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 68509e8a-f316-3b32-817f-7564d2ec9ea2 | -1.01832 | -53.72489 | 2026-09-03 07:03:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c4aade23-aa0d-3a1c-a24a-581c79036621 | -3.24362 | -47.24631 | 2026-09-03 07:03:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 130.8 |
| 75e83280-1a8b-34cd-9b51-2a5c43af0200 | -3.24149 | -47.26098 | 2026-09-03 07:03:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| f7fc03f4-7ea5-3685-9662-6256b730688a | -4.96683 | -55.85158 | 2026-09-03 07:05:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 121207ef-b157-32cc-99eb-b98c568d40c7 | -3.93262 | -49.04946 | 2026-09-03 07:05:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 795a305f-c1b0-3b92-b581-699aa1d097e7 | -4.11714 | -51.02917 | 2026-09-03 07:05:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d91dbbbf-cf13-37b5-aad2-ff212c4f57e1 | -5.20594 | -60.03273 | 2026-09-03 07:05:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 4b18eba6-b20d-32d2-bca2-73051e84645f | -4.08767 | -51.04327 | 2026-09-03 07:05:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f04d9baf-8064-3897-b8d3-85d3e314e897 | -4.10822 | -51.02781 | 2026-09-03 07:05:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| cc3cf22c-463b-36ef-b26c-166cd1317547 | -4.1472 | -51.07699 | 2026-09-03 07:05:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| e9d1981f-c43f-3fa1-91ac-97c3b06673b9 | -4.10959 | -51.01875 | 2026-09-03 07:05:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 948f311d-bab5-3a1d-9e1d-f4e726b2c5fd | -4.14854 | -51.06805 | 2026-09-03 07:05:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| da3c33db-6cf1-3eba-a69c-aa399104f13f | -4.96869 | -55.83987 | 2026-09-03 07:05:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 282427ca-a0d8-3b92-a4a3-fd2891cb033b | -6.67961 | -58.76255 | 2026-09-03 07:07:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 65403311-2fff-34d6-b4f6-1b7fe440a55e | -11.56571 | -50.46618 | 2026-09-03 07:07:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 61719a24-464a-39ea-b06b-5972f2bc8225 | -7.08036 | -56.51429 | 2026-09-03 07:07:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 431ed958-6dfc-313d-bad6-2505b1290733 | -6.42171 | -58.3007 | 2026-09-03 07:07:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 18f959b2-812f-345a-a747-d67956df61f7 | -10.17993 | -50.27485 | 2026-09-03 07:07:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| cd9b0993-fd5b-3f87-9f16-ac94d8ca2ec8 | -5.32304 | -60.1348 | 2026-09-03 07:07:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 22.0 |
| b7e6bc25-d514-3fbc-aef6-2b6001b8be4d | -11.28789 | -54.06425 | 2026-09-03 07:07:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 75e8e035-a41c-3764-ac04-8e621f3d9728 | -11.56737 | -50.45435 | 2026-09-03 07:07:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7e75a109-9c44-3934-a3a2-35a779f81735 | -11.13649 | -51.53145 | 2026-09-03 07:07:00 | AQUA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ecc3ded4-691e-30e1-ba0f-f3121e1416d4 | -8.08139 | -50.96284 | 2026-09-03 07:07:00 | AQUA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 159.1 |
| b787318c-b60e-303f-8d58-4ab4a5ec0941 | -6.68138 | -59.94191 | 2026-09-03 07:07:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 83830a08-d1f3-3f29-9e84-6311819a8bda | -8.44423 | -54.74839 | 2026-09-03 07:07:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 99d9b9bc-fe09-3dc6-9000-39127c9bf205 | -13.5776 | -47.88556 | 2026-09-03 07:07:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 603f416f-35f9-30f0-b735-969b2817630d | -11.31094 | -45.12018 | 2026-09-03 07:07:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 6acbbb17-522a-37b9-aa26-822c3aeb4870 | -11.28924 | -54.05537 | 2026-09-03 07:07:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3fae1c12-f15c-38d3-bcf8-32191683231d | -6.63675 | -59.43541 | 2026-09-03 07:07:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 0b35860b-3848-336b-8c9a-7c86b4d78e28 | -6.41951 | -58.28861 | 2026-09-03 07:07:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 69ec658f-d7c0-3776-9759-fe2f65dae78f | -10.18156 | -50.26325 | 2026-09-03 07:07:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 52d76667-3035-3731-8d99-7de7ccf1050d | -7.55555 | -61.35064 | 2026-09-03 07:07:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 19.3 |
| d1803546-6814-30d9-9d2e-e1e66ac1fe7a | -10.48328 | -51.32216 | 2026-09-03 07:07:00 | AQUA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 806c1e1e-a815-36a7-87c4-a40a6c834729 | -10.56458 | -47.71497 | 2026-09-03 07:07:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 71ff5947-eecb-3f22-be6c-60dbd41cb97c | -8.43519 | -54.74697 | 2026-09-03 07:07:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 9b78a306-3268-336b-a9af-33e65c13562b | -13.57999 | -47.86686 | 2026-09-03 07:07:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| f07742e1-98fa-3398-9bcd-02e09b58e9e4 | -6.68599 | -59.93745 | 2026-09-03 07:07:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 57863778-3cd7-33d6-b767-66568c0df8fc | -6.41671 | -58.30551 | 2026-09-03 07:07:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 80b497b0-878a-3f6b-99c0-f4aa13980991 | -8.07992 | -50.9728 | 2026-09-03 07:07:00 | AQUA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 7a1d5eec-4726-3bf1-88a4-8022b58ea038 | -8.4244 | -54.69721 | 2026-09-03 07:07:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a3f5facd-2dc0-37fd-b91e-269872fae98d | -11.13796 | -51.52129 | 2026-09-03 07:07:00 | AQUA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| cccfd1e8-86f1-31ff-9cb5-8ba87c6daabd | -13.36506 | -51.35194 | 2026-09-03 07:07:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 43834f74-4663-3702-952f-8f8f68a0e8df | -8.4601 | -54.64539 | 2026-09-03 07:07:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 46db5562-6a0c-359e-9ce8-e79c1b134947 | -13.57976 | -47.8737 | 2026-09-03 07:07:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 20.1 |
| b54539f0-c988-3464-90a5-f3a48b9666f1 | -8.43633 | -54.67989 | 2026-09-03 07:07:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c712f69b-5b96-3233-b81d-702b330a3610 | -8.43343 | -54.69858 | 2026-09-03 07:07:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 92dae000-75ee-3baf-ad82-ff4a94b0e274 | -8.0721 | -50.96149 | 2026-09-03 07:07:00 | AQUA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3c6906b5-c461-32f7-a4e5-8cdd0fef02a6 | -8.43488 | -54.68922 | 2026-09-03 07:07:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| f2a90f13-d1a7-3e07-a616-c08ff97f1d18 | -7.56111 | -61.32772 | 2026-09-03 07:07:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 3f01981c-ef10-30d9-ad97-fde0c536c70e | -6.31206 | -56.04712 | 2026-09-03 07:07:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 00ae79f8-26a0-35f6-a99a-167e1dad1012 | -11.31472 | -45.08881 | 2026-09-03 07:07:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 49763fd2-f48e-3a7d-b633-5c6854f881b4 | -11.57574 | -50.46758 | 2026-09-03 07:07:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 9f571bdf-08c6-3ff0-a79a-67fe7ddb53ec | -13.38135 | -51.37682 | 2026-09-03 07:07:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 196c2e19-66a8-3da1-b572-01eb8a219fbe | -18.16025 | -51.80351 | 2026-09-03 07:09:00 | AQUA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 23.4 |
| ae4c0539-cd2a-3d81-8d73-7275b359e398 | -18.16189 | -51.79103 | 2026-09-03 07:09:00 | AQUA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 909822e9-82ec-390c-af9d-0d3d1ab86959 | -18.13851 | -51.81274 | 2026-09-03 07:09:00 | AQUA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 19.7 |
| d87e83a3-a7bc-3ae7-a53c-fec7265ca003 | -8.0737 | -50.9656 | 2026-09-03 07:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 0c6ad7ba-66fd-3fa7-bfa3-549ce29dcac1 | -6.3052 | -56.0442 | 2026-09-03 07:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 680f2b79-0327-350c-a308-811c0a537bb8 | -6.6883 | -59.9436 | 2026-09-03 07:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| b077dc99-d484-3e2a-99b0-00147ab597b4 | -8.0924 | -50.9642 | 2026-09-03 07:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 134c7e2b-8065-3206-8c5a-d65670c91c87 | -8.5916 | -67.1788 | 2026-09-03 07:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| b0807ab0-f378-30d8-8811-c07d7e736e6a | -11.3052 | -45.1344 | 2026-09-03 07:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 0777a5ed-768b-3137-8a0a-6ecb1dce2460 | -8.0737 | -50.9656 | 2026-09-03 07:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| e728be51-9e5e-3f6f-83ca-574b1f9ec95e | -8.0924 | -50.9642 | 2026-09-03 07:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 2198c8de-a1d1-3a81-9297-8935423a909c | -8.5916 | -67.1788 | 2026-09-03 07:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 414eb7ce-774c-35c1-bcbb-8dac59163d63 | -6.6883 | -59.9436 | 2026-09-03 07:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| cbd36b1a-f700-3a0c-b7e9-5e34a0ad1eaf | -8.5917 | -67.1603 | 2026-09-03 07:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| b7e07073-df49-3a73-b443-40a33fb1ca51 | -11.3052 | -45.1344 | 2026-09-03 07:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 98d348b8-94e9-3c0b-b2f3-978b54c8952b | -8.0737 | -50.9656 | 2026-09-03 07:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| c65d0ad0-0cd5-3dae-94c6-ab71b236ea5f | -8.5916 | -67.1788 | 2026-09-03 07:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 93.5 |
| be242b7e-57d2-34ac-a898-65413fc6f31a | -8.0924 | -50.9642 | 2026-09-03 07:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| db9fcd10-ca21-376c-be6c-7d163f9e4d31 | -8.5917 | -67.1603 | 2026-09-03 07:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 84.1 |
| edade385-8ba4-3411-b8f9-6fc8056bb6db | -6.6883 | -59.9436 | 2026-09-03 07:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| d9d5d22e-a9ae-3b88-9646-b9af0dc30dac | -8.0924 | -50.9642 | 2026-09-03 07:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| d25310a1-db6d-3c47-af61-55e6196e4f6c | -8.0737 | -50.9656 | 2026-09-03 07:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 3d9b44d2-ca83-357b-b9f4-b0b99342b0f8 | -8.5916 | -67.1788 | 2026-09-03 07:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 4e3e6411-e72f-3910-9edd-dc11ccd7c7a9 | -6.6883 | -59.9436 | 2026-09-03 07:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 8b01684e-5ac3-3b0f-9fb5-5c613678b181 | -8.5917 | -67.1603 | 2026-09-03 07:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 3eba7fff-f8a2-339a-897e-24069e85a337 | -8.5916 | -67.1788 | 2026-09-03 07:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 76b7711e-487f-3864-ad60-69e90873d8e6 | -6.6883 | -59.9436 | 2026-09-03 07:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| e91f038a-8499-3d6c-b543-c6788451197e | -8.0737 | -50.9656 | 2026-09-03 07:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 487f0e76-134d-315f-a1ed-6d6df8056e33 | -8.0924 | -50.9642 | 2026-09-03 07:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 3782bfbc-15f4-3ced-9d0b-262eae802d54 | -8.5917 | -67.1603 | 2026-09-03 07:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 7118934e-bdff-3304-967a-687ec6354442 | -6.6883 | -59.9436 | 2026-09-03 08:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 01e0f4fd-227f-35d6-b5b4-29fc1d89d5ff | -8.5916 | -67.1788 | 2026-09-03 08:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| c7f7a790-28c1-34bf-9bd9-318d4b092ef0 | -8.5917 | -67.1603 | 2026-09-03 08:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 22db9617-6f98-329c-a47e-27fdc01fbf53 | -6.6698 | -59.9443 | 2026-09-03 08:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 38.9 |
| bd70cfe1-da06-3f11-85bf-76d657935e97 | -6.3237 | -56.0434 | 2026-09-03 08:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 84edb0d9-11f7-3c33-81c2-b3b95644daac | -8.5916 | -67.1788 | 2026-09-03 08:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 37.4 |
| d6288618-af19-3b01-87f3-b94462919437 | -6.6883 | -59.9436 | 2026-09-03 08:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 2f3af84d-8372-3a2d-82dd-fede827202f0 | -6.6883 | -59.9436 | 2026-09-03 08:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| cf322678-24c6-3826-aa3a-8e70e135efe2 | -11.3243 | -45.1317 | 2026-09-03 08:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 7ec29a3f-d1c5-379f-a5b6-f60b7660ea62 | -11.3247 | -45.1086 | 2026-09-03 08:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| b867945a-dee6-3878-8abd-ceee691392c8 | -6.3052 | -56.0442 | 2026-09-03 08:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 05430ee5-a833-3da7-a1c0-b3d79d03ae8c | -6.6883 | -59.9436 | 2026-09-03 08:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 5e929fd7-7182-36f1-a8f1-b2d23047e98d | -6.6883 | -59.9436 | 2026-09-03 08:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.1 |


[Clique aqui para ver as próximas entradas](README54.md)
