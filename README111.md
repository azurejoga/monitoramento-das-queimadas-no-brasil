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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07cbca29-6bd0-3ac1-a16d-121000a952c0 | -19.38525 | -44.24667 | 2025-09-03 11:38:00 | TERRA_M-M | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 80cb0399-6f47-30cc-9a4f-2a7b1aefd07d | -20.2536 | -42.24504 | 2025-09-03 11:38:00 | TERRA_M-M | CAPUTIRA | MINAS GERAIS | Brasil | 3112901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| c203d8b7-fa9f-356c-8144-c26ad746e82c | -12.79228 | -48.13007 | 2025-09-03 11:38:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 7a56f62f-0474-3ad0-ad81-56f39e05f52f | -12.79182 | -48.13847 | 2025-09-03 11:38:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| ce0c010d-67dd-3db6-b839-52222edb9e47 | -20.25558 | -42.2328 | 2025-09-03 11:38:00 | TERRA_M-M | CAPUTIRA | MINAS GERAIS | Brasil | 3112901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 32e6f721-bc8c-37a3-88f3-561d7896c4e7 | -18.06823 | -45.9956 | 2025-09-03 11:38:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 44443dbc-8e10-355f-b0ed-80e5e328f336 | -12.78403 | -48.17485 | 2025-09-03 11:38:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| df8858c2-453a-3563-9cf2-d86996f9d2ae | -15.09102 | -48.12647 | 2025-09-03 11:38:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 8eac59e5-3ad5-3d4f-96e7-0a2e606f8750 | -12.78894 | -47.67106 | 2025-09-03 11:38:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| abea2b1c-a4ea-3907-bd28-90c5668ff790 | -9.7427 | -49.414 | 2025-09-03 11:40:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 0953a97b-3fee-3ed7-bbdd-cf572f20ead2 | -6.7595 | -45.9095 | 2025-09-03 11:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 803587b1-84db-3ef9-a145-c44666af311e | -6.2038 | -43.3475 | 2025-09-03 11:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 211.4 |
| c8b3f237-78cf-350a-910c-4ea01b4b8c32 | -5.7677 | -43.8698 | 2025-09-03 11:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 5b7d87e1-f3f0-380b-ab7e-27320a4067f7 | -6.4648 | -45.4154 | 2025-09-03 11:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 66896d69-3f27-3b4f-8f43-a07ceb3a9623 | -5.8109 | -43.239 | 2025-09-03 11:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 111.4 |
| d7da724f-3c72-36ee-bc22-b4864ef88908 | -9.6229 | -47.0638 | 2025-09-03 11:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 080759df-1af2-39c1-95d1-42d52ffd22f9 | -12.784 | -48.1543 | 2025-09-03 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| f62a93d3-ec0e-3c6c-b6b1-50165afa00ce | -6.8365 | -45.7009 | 2025-09-03 11:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 57223031-dd69-3c81-a649-da5900817d50 | -5.8111 | -43.2156 | 2025-09-03 11:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 0667e5f6-8bc2-3095-a803-bf367f1c64d4 | -6.3502 | -45.6498 | 2025-09-03 11:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 129.1 |
| dba9ae7f-a658-3da2-b026-c551a2339985 | -10.4853 | -50.346 | 2025-09-03 11:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 4316f589-4c8d-3827-b225-f00ef0e4257e | -6.2038 | -43.3475 | 2025-09-03 11:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 131.9 |
| cb9177cb-41f4-3d55-a194-ddd11c67cc55 | -7.7226 | -48.7355 | 2025-09-03 11:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 91.8 |
| a4563448-e41b-36de-8717-8bd79d145fb1 | -5.7677 | -43.8698 | 2025-09-03 11:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 8f7644b9-bbd0-37c6-8bff-6707292dd2a8 | -5.8109 | -43.239 | 2025-09-03 11:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| c0a93a48-a14f-38cc-af58-94b759cb4f78 | -6.4648 | -45.4154 | 2025-09-03 11:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| cc7588fe-3b28-3f6f-8c7d-c1ae127804d5 | -5.8111 | -43.2156 | 2025-09-03 11:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| e34242ec-4552-399a-9189-3d77d19f2023 | -10.4853 | -50.346 | 2025-09-03 11:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 49b1985c-5a0b-3f60-bd4d-fe71a1a1a405 | -7.7036 | -48.7587 | 2025-09-03 11:50:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 199.1 |
| 9eb324b3-411d-32a9-b954-df15bb1d646e | -12.784 | -48.1543 | 2025-09-03 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 0e8ed921-d2bb-38b8-8c02-37262ba11bae | -8.0608 | -45.3636 | 2025-09-03 11:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 82d5fee2-f752-3892-83bf-7af22f280f03 | -15.2675 | -52.7261 | 2025-09-03 11:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 87fa1b3e-b3a7-39eb-a6e2-ac42c7d17b19 | -6.2221 | -43.3927 | 2025-09-03 11:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| cda6afc1-0fdd-354f-81cb-47825c2e26e5 | -6.2224 | -43.3693 | 2025-09-03 11:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 20800c75-f866-37ba-8228-5d6dd2dfbd51 | -9.7427 | -49.414 | 2025-09-03 11:50:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 96e540c6-4ec0-337f-9549-b709c7d9353b | -11.8533 | -51.4318 | 2025-09-03 11:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 4a3d989f-dfae-34e8-aa9e-3c3d53bb4c97 | -7.7224 | -48.7572 | 2025-09-03 11:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 372.7 |
| 7f4fce08-4092-377d-8eb8-05cea0d1bcbd | -6.8365 | -45.7009 | 2025-09-03 12:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 78518734-0228-3faa-a5ab-972d71276b43 | -9.6232 | -47.0416 | 2025-09-03 12:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 146.1 |
| f05f5123-0a08-3ecb-8e9b-0934c11e4c63 | -8.0608 | -45.3636 | 2025-09-03 12:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 90.8 |
| c8733242-3da6-3309-bfa6-7698a024e23a | -11.6165 | -52.0689 | 2025-09-03 12:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 6289cd02-d55c-3db5-bad2-34679072e7f1 | -9.6229 | -47.0638 | 2025-09-03 12:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 06196bb4-f66c-301b-a727-f22040b18e65 | -8.0794 | -45.3844 | 2025-09-03 12:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 9fed0d17-975e-3e30-a481-89d5e347ba7c | -6.7595 | -45.9095 | 2025-09-03 12:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 7b28067b-559d-367d-8afd-55111611b0f6 | -10.5045 | -50.3226 | 2025-09-03 12:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| a87197b4-2a6c-3e9e-9d4b-aec201e49385 | -10.9133 | -50.8549 | 2025-09-03 12:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 1665bbfb-8759-3e1a-a68b-0e7f6c4a26c9 | -5.8111 | -43.2156 | 2025-09-03 12:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 37c53704-a3ca-30b6-bb7a-c2ca6e5eb66a | -9.96 | -51.6244 | 2025-09-03 12:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 8aba893f-d11a-35c7-aad5-9fbf241dd63e | -6.2221 | -43.3927 | 2025-09-03 12:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 673c4040-a540-331c-bb8a-1749bbca810d | -8.0796 | -45.3617 | 2025-09-03 12:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 8415d900-8391-3cb9-b2cd-0960a0381522 | -6.2038 | -43.3475 | 2025-09-03 12:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 4507d68f-ad88-3f6c-ba7f-3d8895209067 | -8.0197 | -44.1072 | 2025-09-03 12:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 134.7 |
| a902ddb5-d3a8-3c47-9462-ce759950df3b | -6.2224 | -43.3693 | 2025-09-03 12:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 150.4 |
| 3b121f09-3a6e-3945-917d-606152f18695 | -6.2411 | -43.3677 | 2025-09-03 12:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 102.7 |
| a6b2ca98-6690-351d-a0fe-0167f9620978 | -9.7427 | -49.414 | 2025-09-03 12:00:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 2f57e10a-654d-3ca4-9fce-2659b716abac | -15.2675 | -52.7261 | 2025-09-03 12:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 7ccd0fea-273a-370f-b3ac-1fbb6a2b71dc | -11.8533 | -51.4318 | 2025-09-03 12:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 74e80a52-98dd-3c2d-8233-1c43512d6483 | -5.908 | -57.7311 | 2025-09-03 12:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 130.3 |
| 82d9bce4-949b-3fdb-8fa7-955b8955dcf2 | -10.0932 | -54.7667 | 2025-09-03 12:00:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 09480a90-250d-3745-8c58-93abc69dbc4d | -10.9323 | -50.8529 | 2025-09-03 12:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 982f156a-4af7-3add-873e-a9ecdc20a60f | -10.4853 | -50.346 | 2025-09-03 12:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 9cf99fed-1ecc-320a-b2ff-f9b4599399ac | -10.4856 | -50.3246 | 2025-09-03 12:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| e7bab2cf-5773-3a6c-a5d2-5385d29c0513 | -7.7036 | -48.7587 | 2025-09-03 12:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 187.7 |
| 1e245812-a53d-3d65-bc08-a3206b34d2c8 | -5.8109 | -43.239 | 2025-09-03 12:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 0ccc5840-ca6e-3c07-840b-200b38b34ec2 | -11.9443 | -45.7769 | 2025-09-03 12:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 5961c62c-1339-379b-9be1-1925fa55cc96 | -9.6229 | -47.0638 | 2025-09-03 12:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 153.1 |
| eed0ac53-439e-3884-a8a1-1673783792f7 | -6.7595 | -45.9095 | 2025-09-03 12:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 076e8fd7-7e74-3f7f-a646-543bfa26a759 | -6.2224 | -43.3693 | 2025-09-03 12:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 277.5 |
| 7f9772f1-c4e6-3e8c-a919-817fd1d2f58d | -5.8455 | -45.6421 | 2025-09-03 12:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 12a4e54c-55e9-3c30-8412-12d3232acca2 | -5.8111 | -43.2156 | 2025-09-03 12:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| fa7c7623-efbc-35b7-99bf-bcf485d918df | -10.4853 | -50.346 | 2025-09-03 12:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 212.6 |
| 54ad4746-8561-346e-a17d-0a6544624e3a | -6.2221 | -43.3927 | 2025-09-03 12:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 237.8 |
| 51cf3482-cf41-37f7-8118-8d8341479746 | -6.2038 | -43.3475 | 2025-09-03 12:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 233.3 |
| 1e0b26f3-2cc5-34a9-93da-24f44652382d | -8.0796 | -45.3617 | 2025-09-03 12:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 959ed483-1a5e-3cd6-a560-ce7cbc73092c | -11.9635 | -45.7741 | 2025-09-03 12:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 159.3 |
| 8ddf2689-05e0-3b07-af4a-13abfe2d2a78 | -6.7782 | -45.908 | 2025-09-03 12:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 3cae5b2a-47b1-3c98-9a56-8625729c6557 | -16.8537 | -49.5973 | 2025-09-03 12:10:00 | GOES-19 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 81.5 |
| ca6b2e73-b0e0-3657-baef-e988816956d6 | -6.2036 | -43.3709 | 2025-09-03 12:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 35d8123f-7c90-3842-aa0b-3089a8fcfb7a | -6.2411 | -43.3677 | 2025-09-03 12:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 750c26c0-1269-3af6-93be-89f09a588e05 | -10.4856 | -50.3246 | 2025-09-03 12:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 426d1645-0fb6-3c3d-ad80-c0d8723712ea | -6.4648 | -45.4154 | 2025-09-03 12:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 140.5 |
| 1e8c99af-f1cd-3c99-badd-f1b21cdc22d9 | -6.3502 | -45.6498 | 2025-09-03 12:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| cae544cd-d535-3f1c-93e7-82dbfe842208 | -8.0608 | -45.3636 | 2025-09-03 12:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 7ab7f477-89eb-362a-8611-9ff1b4def8cf | -6.2409 | -43.3911 | 2025-09-03 12:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 2877c6fb-a900-3e64-aea1-842b8db89823 | -7.5302 | -47.4443 | 2025-09-03 12:10:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| d566ae6f-1820-3c39-a0c4-bc4bb4ec7c8d | -5.8109 | -43.239 | 2025-09-03 12:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 5a153020-565f-3d9e-b5e2-ee17019249d0 | -15.2675 | -52.7261 | 2025-09-03 12:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 11d05784-4a0c-3966-ad08-a9e607fbbe30 | -9.6232 | -47.0416 | 2025-09-03 12:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 8cc40d7c-eb75-33ae-b2db-5c80ea36979a | -10.0932 | -54.7667 | 2025-09-03 12:10:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 3ae99662-7486-369f-8b38-8c9bb16fa626 | -11.6165 | -52.0689 | 2025-09-03 12:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 5cb5ca60-594a-35e7-b1d3-8f572bd3ebc3 | -11.8533 | -51.4318 | 2025-09-03 12:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 4689f8b1-6ad2-3dac-8783-ebf2cc069d58 | -6.8365 | -45.7009 | 2025-09-03 12:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 4fda688c-fb64-30ee-967f-cee077cff45f | -10.5045 | -50.3226 | 2025-09-03 12:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 145.1 |
| d3da2ddc-2c65-3cde-9369-d798c50aa933 | -11.0184 | -51.479 | 2025-09-03 12:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 1e385658-28a2-361d-9b3e-38ce7a1f88b3 | -11.0181 | -51.5001 | 2025-09-03 12:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 106.7 |
| caaf0924-1cac-3ef3-a9a2-46a2c19591a9 | -6.2038 | -43.3475 | 2025-09-03 12:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 283.0 |
| 50b198b1-4d06-384a-85f4-8975ff6410b8 | -11.0181 | -51.5001 | 2025-09-03 12:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| f3ce665c-3d2d-32a7-a6c9-c11ded4789eb | -9.6229 | -47.0638 | 2025-09-03 12:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| fc48a55e-7ffd-36d0-9fa9-92211b6384e4 | -11.8533 | -51.4318 | 2025-09-03 12:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 100.4 |
| efd03694-655b-3e5f-973c-192b57dbe4c4 | -7.53 | -47.4662 | 2025-09-03 12:20:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |


[Clique aqui para ver as próximas entradas](README112.md)
