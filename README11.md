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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a28d5ae3-4e41-3ef4-be9b-966e3d855891 | -13.1648 | -45.2665 | 2025-09-01 03:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 18b89fe3-c19f-32dd-bc26-e18cc21544a4 | -15.7112 | -48.9032 | 2025-09-01 03:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 69.3 |
| a006afaf-cc60-3dc0-aeba-90d4cb928047 | -7.0948 | -44.3358 | 2025-09-01 03:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 126.4 |
| cc60ef46-7560-35e3-b3d6-bfdad53fe07a | -9.1165 | -65.5459 | 2025-09-01 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 044ced48-eb39-38d6-8eb9-59e3d8058f85 | -15.6063 | -48.3177 | 2025-09-01 03:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 389518c7-9a60-39ce-a705-1032c088a23b | -10.6128 | -44.3284 | 2025-09-01 03:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 56eeaf41-7a6e-3a38-a6df-413c299d6fbc | -13.1644 | -45.2897 | 2025-09-01 03:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 6650b7f1-978a-39fd-baa7-bb0b75dd3e55 | -11.0572 | -45.123 | 2025-09-01 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 98ddc8b7-4d2a-3483-8f1c-71c049d30634 | -7.0757 | -44.3606 | 2025-09-01 03:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 147.0 |
| 9a1c0b80-d8c5-392d-826f-75d0a88ebb75 | -11.0568 | -45.146 | 2025-09-01 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 0d136486-dcaa-3730-8e56-ca6a08c006f7 | -7.0946 | -44.3589 | 2025-09-01 03:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 06e33980-07cc-3b42-858a-5f539bc0ef95 | -15.6058 | -48.3402 | 2025-09-01 03:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 85db268f-2ae3-38ab-83d3-312556d53e39 | -18.6704 | -52.5973 | 2025-09-01 03:10:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 94f23f2a-06bf-3ba6-9e69-274588238e2e | -15.5867 | -48.321 | 2025-09-01 03:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 3028cbea-beea-35d9-b3e3-e965264be3d9 | -10.5937 | -44.331 | 2025-09-01 03:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 5b496821-7c78-3392-b688-67eb0d202746 | -15.7289 | -48.9892 | 2025-09-01 03:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 080b9654-1c85-3494-8ef5-5db5da4b31b7 | -15.7116 | -48.8809 | 2025-09-01 03:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 56.0 |
| fb00fc7c-4d82-3bb9-9fe5-c0d027e5bdd9 | -10.6131 | -44.3051 | 2025-09-01 03:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 34289b5c-4aab-37d7-9b90-2c1fe5edbe00 | -10.594 | -44.3077 | 2025-09-01 03:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 3cecf791-5ebe-313c-9fdf-75ce44ce98f0 | -7.076 | -44.3376 | 2025-09-01 03:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 163.8 |
| 85358b04-b188-338e-b64b-e6fd59ed20be | -10.0434 | -48.0998 | 2025-09-01 03:10:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 378f4221-6654-37f5-bb0a-da2cd6eb1933 | -11.0377 | -45.1487 | 2025-09-01 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 370.6 |
| c8e7a8b4-2d2e-3a5c-adae-48cef69146b6 | -15.6916 | -48.9065 | 2025-09-01 03:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 1153b2d3-e571-30b6-928d-fda204af5ca1 | -10.2488 | -51.1128 | 2025-09-01 03:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 328d6465-4e43-3de2-b5b1-1072e3ea5ebc | -13.1648 | -45.2665 | 2025-09-01 03:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 56.8 |
| d551a81d-acbd-3842-9c2d-6723925f688a | -11.0381 | -45.1256 | 2025-09-01 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 217.7 |
| 34eb9f85-774a-3bdb-a89e-6be6558ae32e | -6.8466 | -52.8132 | 2025-09-01 03:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 24b19163-f07b-3412-b083-da50473bb418 | -15.5862 | -48.3435 | 2025-09-01 03:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 590f7d0c-3959-31ef-9e06-6f2c1f7e8b52 | -6.8281 | -52.8143 | 2025-09-01 03:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 523fc82b-83b8-3e03-acbb-4757b16b7a72 | -15.774 | -47.7933 | 2025-09-01 03:10:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 57.1 |
| df7afe7f-b78b-3c9a-8a92-66219e038fbd | -9.135 | -65.5453 | 2025-09-01 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 249e244f-ab3e-33f7-842f-3b3cff19b6b4 | -15.5867 | -48.321 | 2025-09-01 03:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 80cceece-fb9f-31ac-b2fb-27507e87cb21 | -15.7289 | -48.9892 | 2025-09-01 03:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 71.4 |
| dd1bbe41-3704-3054-8ec2-d683af5f1aa8 | -6.8466 | -52.8132 | 2025-09-01 03:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| aa5956f7-9d11-395a-b370-f6740224be35 | -13.1648 | -45.2665 | 2025-09-01 03:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 56.1 |
| d3f34301-070d-30e0-9f68-a17cb7fe9522 | -9.1165 | -65.5459 | 2025-09-01 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.9 |
| d4a6faa1-e12f-3a5b-b851-9fcf7685cda1 | -7.0757 | -44.3606 | 2025-09-01 03:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 3d6450bc-257a-33cb-8b24-5cf8d096a784 | -12.5722 | -48.2059 | 2025-09-01 03:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 6be29654-fd8e-3bcc-8b6e-5d0a35cb9ab2 | -6.8281 | -52.8143 | 2025-09-01 03:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 78db08cf-79d8-36c2-acda-8954a2be8061 | -13.1644 | -45.2897 | 2025-09-01 03:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 27ac396e-1995-3c36-a172-8c7c9d0ae807 | -15.774 | -47.7933 | 2025-09-01 03:20:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 55.1 |
| cf971800-8624-3549-aa6f-aa721a9e8c19 | -15.6058 | -48.3402 | 2025-09-01 03:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 80.8 |
| b15d975f-cbb9-363b-b1c4-6dbca23c8904 | -9.135 | -65.5453 | 2025-09-01 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 456114ca-3de7-35fe-b467-06ced3240ab4 | -7.0948 | -44.3358 | 2025-09-01 03:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 6c5a93a8-aba8-3e45-9fa6-b1b4d2909dfd | -8.7684 | -61.4261 | 2025-09-01 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 283188f9-c06b-3b27-8636-2dd308d621f0 | -7.0946 | -44.3589 | 2025-09-01 03:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 21dee374-f1fa-3cec-9519-289993681308 | -10.2488 | -51.1128 | 2025-09-01 03:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| b0f6ebe1-84bb-3719-b809-720b6b7e61f2 | -15.5862 | -48.3435 | 2025-09-01 03:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 90.8 |
| e935bd99-39ec-3596-a677-eda09aedac55 | -7.076 | -44.3376 | 2025-09-01 03:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 167.8 |
| 83e37c6d-1a92-340b-84b8-33acb9008131 | -15.7289 | -48.9892 | 2025-09-01 03:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 68.0 |
| a145e98b-32d9-31a5-a4ac-804eab927d7f | -15.5862 | -48.3435 | 2025-09-01 03:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 81.5 |
| fe1ee9a3-ec88-353e-82eb-be03979d9299 | -12.9197 | -56.9471 | 2025-09-01 03:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 265.7 |
| fa70373f-ec44-32f6-bd04-44c921d0a4d5 | -12.9004 | -56.9689 | 2025-09-01 03:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 95f3cc49-4ab5-362d-a792-c7719de5d18f | -7.076 | -44.3376 | 2025-09-01 03:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 164.9 |
| be8a940c-59a8-3659-82c8-e4d15dd2a0f3 | -12.5526 | -48.2307 | 2025-09-01 03:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 90c15723-6d79-3200-8b8a-3b3f02450767 | -8.7684 | -61.4261 | 2025-09-01 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.7 |
| af831dc2-f083-387e-a89f-35ba05ed4fd0 | -12.5722 | -48.2059 | 2025-09-01 03:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| e84c71ec-b685-3930-a65c-7cab6782a359 | -15.6058 | -48.3402 | 2025-09-01 03:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 72.8 |
| d0328a2a-7217-3536-9336-d07d61bb4f9b | -7.0946 | -44.3589 | 2025-09-01 03:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 110.4 |
| be619db2-3f40-3b8a-93c9-a08284e60c88 | -15.774 | -47.7933 | 2025-09-01 03:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 56.1 |
| a348890b-3525-3944-b35c-6e5120342ec4 | -6.8466 | -52.8132 | 2025-09-01 03:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 5e637711-17ca-3f05-8b5b-3e43b21fe689 | -7.6783 | -61.0908 | 2025-09-01 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 5ab32fb6-77e6-3040-b727-413fea8eb1ea | -7.0948 | -44.3358 | 2025-09-01 03:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 1bba4163-8d99-3cae-8b6e-8f245702fd7c | -6.8281 | -52.8143 | 2025-09-01 03:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 60b53fca-6345-3746-8fe1-33588ab72b14 | -12.9387 | -56.9454 | 2025-09-01 03:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 169.9 |
| 121856e8-57ce-3656-aec9-8961ae243e00 | -12.5718 | -48.228 | 2025-09-01 03:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| cf2e68b9-f2a2-33fe-a8e9-a0b29151cdac | -7.0757 | -44.3606 | 2025-09-01 03:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 153.9 |
| 630d8df0-f841-354a-bdb9-235de8397796 | -9.135 | -65.5453 | 2025-09-01 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 2c7dd80d-9195-365b-a6b0-8dc5c559511f | -12.553 | -48.2085 | 2025-09-01 03:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 8bbf2bda-3bd5-35d8-860b-aa0a6b7d9b2c | -12.9194 | -56.9672 | 2025-09-01 03:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 263.8 |
| f6e4d0c9-5a89-3a49-b6e7-4e7ca1ad3580 | -18.6704 | -52.5973 | 2025-09-01 03:30:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 88f67c73-bda8-3d23-8731-d7ebe7caf262 | -12.9006 | -56.9488 | 2025-09-01 03:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 1938543d-9650-35e1-b353-60d7c93475f4 | -12.9385 | -56.9655 | 2025-09-01 03:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 161.6 |
| 20fda084-d7e7-38a4-a43c-19989f29c382 | -15.774 | -47.7933 | 2025-09-01 03:40:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 8001b9c8-9347-315c-81c3-3531b170a9da | -8.7684 | -61.4261 | 2025-09-01 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| fa17327b-060f-328b-b2cd-ae02fa0da2da | -9.135 | -65.5453 | 2025-09-01 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 7538fa1f-4292-38f6-9ae8-ee6ebfb0adfa | -12.9385 | -56.9655 | 2025-09-01 03:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 189.1 |
| 43d2f47b-4bfd-3d8e-9a06-5a16cf9c5134 | -15.6058 | -48.3402 | 2025-09-01 03:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 66.0 |
| ae84b54d-73cd-3781-96c6-a5ab5eef8794 | -12.9387 | -56.9454 | 2025-09-01 03:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 202.7 |
| e4cb5e86-16e5-32d7-ad74-246908edfdb3 | -7.0946 | -44.3589 | 2025-09-01 03:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 0d1c636b-ddcd-3778-9c06-6b4c61551c59 | -6.8281 | -52.8143 | 2025-09-01 03:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 036c8b68-52b1-3a75-9450-d391f70b2acb | -15.7112 | -48.9032 | 2025-09-01 03:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 67.9 |
| df2c8a65-bc11-31cd-922f-c3f962912677 | -12.9197 | -56.9471 | 2025-09-01 03:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 287.7 |
| aa477d8c-4c39-326e-9d46-d910a0f188f1 | -14.8327 | -47.096 | 2025-09-01 03:40:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 54.4 |
| a3da10e0-534d-3ba1-998b-02f864cde42a | -6.8466 | -52.8132 | 2025-09-01 03:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 135ad3f5-b3ae-38f3-ae5f-6cd18b04aa21 | -15.6906 | -48.9511 | 2025-09-01 03:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 71c9617e-a142-3d81-b468-303d319c7ce4 | -7.076 | -44.3376 | 2025-09-01 03:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 9d2e9530-ae9f-3599-a9d5-dd267979cabd | -7.0948 | -44.3358 | 2025-09-01 03:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 5f4c6c63-3782-3263-a4f0-c4c9103be172 | -15.7102 | -48.9479 | 2025-09-01 03:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 42563622-0196-3f93-b9ce-f6721fefb632 | -18.6704 | -52.5973 | 2025-09-01 03:40:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 47.5 |
| cdec8c10-d0dd-38a7-93a8-0caf5974e10f | -12.9004 | -56.9689 | 2025-09-01 03:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 2e75a8a6-d7de-3d5e-9f0d-85c07b2e8124 | -15.7289 | -48.9892 | 2025-09-01 03:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 83.7 |
| eea78d81-1ff0-30ad-8bc3-db1c2b240aed | -7.0757 | -44.3606 | 2025-09-01 03:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 149.6 |
| a37cd750-2d7e-39cc-b046-8120e358ff0b | -7.6783 | -61.0908 | 2025-09-01 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 4e2a0880-03ec-347d-a6bc-8e1195fc2963 | -14.8522 | -47.0926 | 2025-09-01 03:40:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 106.8 |
| d89772bd-a9bf-3e6a-93d5-3a6bcdcd4db7 | -15.5862 | -48.3435 | 2025-09-01 03:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 666a5018-cf39-3ebf-88d5-49b7d8c3f1da | -12.9194 | -56.9672 | 2025-09-01 03:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 297.5 |
| c2347769-325b-335e-a64c-78bc457a45ea | -12.9006 | -56.9488 | 2025-09-01 03:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| d45e42aa-1ea7-3dba-973f-e18fc1ea57d8 | -6.85975 | -43.49499 | 2025-09-01 03:42:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c59b454e-0bef-368a-b5e9-6c3daa313a65 | -6.4697 | -42.43053 | 2025-09-01 03:42:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |


[Clique aqui para ver as próximas entradas](README12.md)
