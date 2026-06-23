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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cae58f46-8d3d-3860-8f0e-a858c2528b7e | -12.8543 | -44.386 | 2026-06-23 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 5eb76710-a9ec-3dc4-845e-67b38bc91b57 | -12.4283 | -58.4048 | 2026-06-23 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 989bbcc2-7bee-397c-9780-152224df1592 | -12.8741 | -44.3593 | 2026-06-23 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 282.3 |
| 20376115-85fa-3ebe-96f4-04163c1d0f80 | -6.3703 | -43.5898 | 2026-06-23 00:00:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 07b306ec-fdf0-303c-9f23-b59dfe34072e | -12.8552 | -44.3389 | 2026-06-23 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 478d4332-6739-3f59-ac3e-d92dfa3f7dd9 | -12.8548 | -44.3625 | 2026-06-23 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 301.4 |
| 4c4fd6b2-3f0a-3204-85c2-f262e162f093 | -20.5782 | -47.3053 | 2026-06-23 00:00:00 | GOES-19 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 6a8862ab-cebf-3b6b-b817-c8a9dc97e608 | -12.8736 | -44.3828 | 2026-06-23 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 0328da1b-ab66-3d0b-bbca-ba46c570fc2c | -12.8746 | -44.3357 | 2026-06-23 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 131.8 |
| efa074a6-fc13-3454-a2b1-737a8bf7cfac | -5.8132 | -45.0573 | 2026-06-23 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| a849b207-8927-374a-b329-f95246bec0fb | -20.5987 | -47.3004 | 2026-06-23 00:00:00 | GOES-19 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 3e1bed7b-7830-32ff-ad01-f8ff924e1a63 | -5.8319 | -45.0559 | 2026-06-23 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 52.0 |
| d32f2d74-6dd3-32b7-ae1e-c3ffeb9d1e39 | -12.8746 | -44.3357 | 2026-06-23 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 160.1 |
| 2d97d85f-a6b5-3857-a71e-91bc0ef0c038 | -12.8552 | -44.3389 | 2026-06-23 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 3b082dc0-708b-30b3-b734-222ac706aadc | -12.8741 | -44.3593 | 2026-06-23 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 316.5 |
| 038b50c3-3d0d-3255-a5d2-e584c3e037fe | -12.8548 | -44.3625 | 2026-06-23 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 296.4 |
| 8160351e-f97a-3101-a285-94f725cb65be | -16.0342 | -43.4224 | 2026-06-23 00:10:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 77.6 |
| bb3b5859-f58a-3340-ac1f-f38fcc202b04 | -12.4283 | -58.4048 | 2026-06-23 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 287ceec9-99e8-31e0-8fb9-dccd2fc9a203 | -12.4283 | -58.4048 | 2026-06-23 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| d24923a7-e7ae-381f-a85c-025cbe72c608 | -12.8746 | -44.3357 | 2026-06-23 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 159.5 |
| d246b1c7-61f9-3b8e-a013-6678a658da73 | -12.8741 | -44.3593 | 2026-06-23 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 253.5 |
| 10e357aa-3a1c-33ae-b084-e6de05689a16 | -12.8552 | -44.3389 | 2026-06-23 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 163.7 |
| b5adf86f-df1e-394e-b03a-28cc8de8306f | -12.8548 | -44.3625 | 2026-06-23 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 274.4 |
| d373f8c9-cb98-36bf-a1bd-b96e96e3a323 | -12.4283 | -58.4048 | 2026-06-23 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 42201f44-1683-35d2-a19d-4b067b974e79 | -12.8741 | -44.3593 | 2026-06-23 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 272.6 |
| a4ef0788-e310-3d64-9cf1-f992953c3712 | -12.8548 | -44.3625 | 2026-06-23 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 245.7 |
| 2ef60d38-f1c4-3ca6-b3d5-46482a4b386c | -12.8552 | -44.3389 | 2026-06-23 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 620e17e2-07e7-3d81-b8b4-5d769c410146 | -12.8746 | -44.3357 | 2026-06-23 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 173.7 |
| 8dfd36b4-e487-32b8-b7a1-87f141f38204 | -10.8788 | -49.538502 | 2026-06-23 00:36:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6d1661bc-d26c-3073-b578-0152350ee887 | -12.5505 | -57.179199 | 2026-06-23 00:36:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0d984255-06a9-343a-ba47-7dd86232a7e4 | -11.4881 | -46.670502 | 2026-06-23 00:36:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e67c642d-5bd4-3c4c-a410-be7b357efaac | -11.0536 | -52.449402 | 2026-06-23 00:36:00 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 155aced7-7dca-39e5-a241-27609229a4b1 | -9.4455 | -50.837799 | 2026-06-23 00:36:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c779ba9-fc3c-360b-9133-f4386ef5f73b | -5.8192 | -45.069 | 2026-06-23 00:36:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 41fdbdd9-67eb-3436-a2a1-b882036e5d2b | -12.8576 | -44.354401 | 2026-06-23 00:36:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6b6a24fd-9abd-34d0-8608-2e832e152698 | -9.4496 | -49.821098 | 2026-06-23 00:36:00 | METOP-B | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ba0fa704-6b24-3592-97c6-3b9f12be4898 | -16.0128 | -43.3978 | 2026-06-23 00:36:00 | METOP-B | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f0d1313c-7d5b-3832-85d6-0ace2ba583ce | -12.4297 | -58.403599 | 2026-06-23 00:36:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 99832fbf-bfe6-3e07-ab8c-d671e7bbc612 | -12.9073 | -49.4622 | 2026-06-23 00:36:00 | METOP-B | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9a4425a7-8dab-356f-9f2d-75e9bb893d68 | -11.3118 | -54.711899 | 2026-06-23 00:36:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8dda6f0f-d6ff-3d16-8fa1-9db09a013db9 | -5.8222 | -45.039902 | 2026-06-23 00:36:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 044d791b-0e59-33a1-9aa7-008b25c6b1be | -10.5538 | -46.203602 | 2026-06-23 00:36:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 540202c6-09dd-3d92-8c5f-c78895e6301e | -12.2943 | -57.5658 | 2026-06-23 00:36:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4d7bf87b-5ec1-36f4-950a-a54875c36cc6 | -11.7991 | -47.327099 | 2026-06-23 00:36:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8281cb99-f51f-36db-8012-4a004ce08959 | -10.9704 | -48.144402 | 2026-06-23 00:36:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8144b962-18d5-3a12-8a6a-c0d1488adf27 | -13.5058 | -56.558701 | 2026-06-23 00:36:00 | METOP-B | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8e332db9-14cb-3a9e-821b-d67bada4bf5c | -11.8088 | -47.3246 | 2026-06-23 00:36:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3b058d35-ddb2-37f5-b5bc-759c0d910c54 | -12.8818 | -49.826 | 2026-06-23 00:36:00 | METOP-B | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f031ef16-f852-32c9-b274-207100987518 | -10.3937 | -56.7038 | 2026-06-23 00:36:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d6c8fdc8-b504-3fcf-ba07-a034007b34e6 | -11.302 | -54.7141 | 2026-06-23 00:36:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8997bb21-2dd0-3ec2-beef-eaa47b9871f8 | -6.3515 | -43.580898 | 2026-06-23 00:36:00 | METOP-B | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8ea277d9-9093-3431-a6c0-b184e46e892f | -6.361 | -43.5784 | 2026-06-23 00:36:00 | METOP-B | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9643ea27-c211-301c-8b51-e265cc802ec9 | -10.7724 | -54.102901 | 2026-06-23 00:36:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 63cd6bc9-6397-39ef-84f2-5a8b695ea7db | -11.2817 | -55.782101 | 2026-06-23 00:36:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aeb7b308-2993-363d-9c79-dc88767ecab6 | -11.8036 | -52.521999 | 2026-06-23 00:36:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5c70ba5d-a6c8-3823-bfcb-379371190ae0 | -11.8134 | -52.519699 | 2026-06-23 00:36:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 322d19c1-5933-3580-a4dc-36bba04a2b99 | -8.8621 | -46.93 | 2026-06-23 00:36:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 98d102c5-1686-3a76-abac-68209d9210ae | -12.0314 | -47.799099 | 2026-06-23 00:36:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| df8da00e-4516-3bc4-adaf-60b09d0ba9d7 | -12.6498 | -47.6674 | 2026-06-23 00:36:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 52ad1ca5-55d4-389f-8c96-e53acd0d136c | -16.0224 | -43.395 | 2026-06-23 00:36:00 | METOP-B | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d007febb-b3be-384b-b18a-ca8103630e91 | -5.8126 | -45.042301 | 2026-06-23 00:36:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 53b38534-196b-30ae-835b-228cdfbf655b | -9.1762 | -58.048901 | 2026-06-23 00:36:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a562b04f-9601-367f-b088-f2d061c26733 | -11.8117 | -52.5121 | 2026-06-23 00:36:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5b46fbc6-cbd0-3f0a-abcf-36f463eb559c | -10.9011 | -54.124901 | 2026-06-23 00:36:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| af7d01b8-7b28-3fee-b0bf-973e08d64381 | -12.8479 | -44.356998 | 2026-06-23 00:36:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8a721682-bb36-3b21-ba51-81861991f4e3 | -11.8769 | -57.821301 | 2026-06-23 00:36:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f7ad3f09-ba83-33aa-ac79-4873f9f46aa1 | -12.8611 | -44.328999 | 2026-06-23 00:36:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f2d2bcbb-a4cf-34b7-8f8a-a46aea2f94d9 | -12.8358 | -44.3116 | 2026-06-23 00:36:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ddbbb50a-4b07-397b-9f49-11f11c163c6f | -11.5776 | -47.432098 | 2026-06-23 00:36:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eb29a786-f1ff-3468-8c20-861bf1a74e6c | -12.9098 | -49.472599 | 2026-06-23 00:36:00 | METOP-B | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c2958ab3-6d4a-3841-8d85-1914ea5d5918 | -12.8419 | -44.3344 | 2026-06-23 00:36:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 74f606b1-dc9d-31c3-9d6f-b976c169c173 | -12.2925 | -57.557598 | 2026-06-23 00:36:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 13c9d1cb-b59d-353c-a3f6-9edf28f88530 | -13.5075 | -56.566399 | 2026-06-23 00:36:00 | METOP-B | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| de32ac76-d714-39bf-bf9f-7f0c302f3a16 | -11.0554 | -52.4571 | 2026-06-23 00:36:00 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 971d010b-6268-3639-b556-637038e246d2 | -12.4992 | -48.2654 | 2026-06-23 00:36:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3f163333-c763-3ab0-9cc3-8e34cfbbe77b | -12.8672 | -44.3517 | 2026-06-23 00:36:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f3deb696-be7b-388a-9342-cca3e906e5b6 | -11.5201 | -56.118099 | 2026-06-23 00:36:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8913306a-862d-31a5-b9dc-b26c0619631e | -11.0507 | -49.565498 | 2026-06-23 00:36:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cee22599-7107-3fc9-8301-53588c33e5cd | -10.8761 | -49.5275 | 2026-06-23 00:36:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 22083856-20d0-32df-a6ac-ba4f89fd6a5a | -12.5152 | -48.288101 | 2026-06-23 00:36:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3e5809de-90c5-38e3-910d-b8974dbfe07b | -12.9195 | -49.4702 | 2026-06-23 00:36:00 | METOP-B | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1bbb7bba-a64f-395c-b0d7-5ca530814843 | -10.2752 | -60.523602 | 2026-06-23 00:36:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 84ce9db5-f76a-3f06-bdb4-b3551660a461 | -12.8515 | -44.331699 | 2026-06-23 00:36:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c23368d3-6582-393d-bb4d-fb242251d6a7 | -12.028 | -47.7854 | 2026-06-23 00:36:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 60a2e1e7-293d-384c-b65e-567f2da28290 | -11.8028 | -47.3419 | 2026-06-23 00:36:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dc2f0af3-7a84-3158-a5c1-6f03a379ad0b | -11.2802 | -55.775002 | 2026-06-23 00:36:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8ef388a4-bd33-3600-a535-6ef5fd60631f | -12.4376 | -58.392502 | 2026-06-23 00:36:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 73a38e87-4268-3e84-aafe-6db64bb45292 | -9.4593 | -49.818699 | 2026-06-23 00:36:00 | METOP-B | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f7137eae-c9ca-3591-9100-681f2d90c408 | -11.0456 | -52.4594 | 2026-06-23 00:36:00 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7097d46e-ab5a-33a8-85b2-7ede9d70a58f | -12.5121 | -48.275501 | 2026-06-23 00:36:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f12407a7-6722-384e-a161-5aec2c33fb65 | -10.9372 | -56.8395 | 2026-06-23 00:36:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ffc63a71-8b7e-3658-8f25-fc7a80d6cde8 | -11.8018 | -52.5144 | 2026-06-23 00:36:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 08c6fbce-32ba-392a-a4d6-295965e63dae | -12.8323 | -44.337002 | 2026-06-23 00:36:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b9eb6282-e408-3781-9112-6c0fb42f4630 | -12.4278 | -58.3946 | 2026-06-23 00:36:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 24b15c08-9dc2-3c8c-98e7-02cb4c0b0524 | -12.8455 | -44.308998 | 2026-06-23 00:36:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eae819ee-191f-3569-acd5-190583dd8c48 | -9.1745 | -58.040901 | 2026-06-23 00:36:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fa674fb9-3e89-3abd-867e-9bbbae48383b | -12.917 | -49.459801 | 2026-06-23 00:36:00 | METOP-B | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8e53aa9e-c825-376a-84c2-d477e13c2e22 | -10.2776 | -60.534901 | 2026-06-23 00:36:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d1c06745-df6e-35c9-8d93-f0966f433604 | -12.4357 | -58.3834 | 2026-06-23 00:36:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9128e753-3304-3cfb-a3ae-a0647d1fa4b7 | -11.5739 | -47.417301 | 2026-06-23 00:36:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
