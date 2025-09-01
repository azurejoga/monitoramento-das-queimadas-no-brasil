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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e187dd2-6837-3dcb-a4e3-4eca44680dba | -11.3701 | -43.6104 | 2025-09-01 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 58490add-5944-388d-818c-b7cd243f5bb4 | -4.3197 | -48.0908 | 2025-09-01 13:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 6fdeb701-76d6-3ff0-a4a4-d41ae6f66617 | -10.0434 | -48.0998 | 2025-09-01 13:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 5da1b80a-de21-3846-b1ad-1b5470d4f38b | -7.9729 | -46.4301 | 2025-09-01 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 9e6e0d31-1c31-360a-b2c3-532368223f9a | -11.0568 | -45.146 | 2025-09-01 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 6e8069c3-f955-373d-9434-f547b2eb8527 | -7.9351 | -46.4559 | 2025-09-01 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| f41e9c5d-9b08-3b0e-8337-e03b197a66a1 | -12.793 | -47.6415 | 2025-09-01 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| e9ec011d-d23e-34e2-955e-53f23adef0b7 | -9.2825 | -47.1007 | 2025-09-01 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| f3da2289-8869-369c-ad49-e56b0b2c99ae | -11.3705 | -43.5868 | 2025-09-01 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 189.0 |
| cce5c739-d2fa-3a66-afc1-0d3b0b25cd96 | -8.8248 | -47.5235 | 2025-09-01 13:30:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 02c34d72-0305-3368-a20c-2f56386477dc | -13.3439 | -46.9757 | 2025-09-01 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 14cdef99-29e8-3d61-814d-0e70dd9efebc | -9.6127 | -47.8169 | 2025-09-01 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 67db44bb-a202-3f5d-9beb-f8ce461e4d3a | -8.8936 | -45.1168 | 2025-09-01 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 4aecc409-fa89-38fe-9223-ba1274cefa01 | -9.1567 | -45.2243 | 2025-09-01 13:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 183.1 |
| 4d6397f6-42e5-3752-a66b-7a6b7457c0c5 | -8.8622 | -47.5418 | 2025-09-01 13:30:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| ca340b28-1c7c-39e3-8b30-9fe2265e7476 | -14.6483 | -43.9461 | 2025-09-01 13:30:00 | GOES-19 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 85.6 |
| f0e9d41b-c0aa-3c74-ae1c-1ff285b4ea25 | -11.8185 | -46.4087 | 2025-09-01 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| dca3752d-2480-3a03-9dc0-a8f4af988e3f | -12.9575 | -48.1076 | 2025-09-01 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 75a96ce4-4276-3ada-803b-289d1e45506a | -11.487 | -46.8147 | 2025-09-01 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| a06a5ad5-d83e-39f2-b219-273afb4d3ddc | -12.392 | -46.4626 | 2025-09-01 13:30:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| b66bba85-30e2-39d1-a124-ba904ab7cc20 | -8.8625 | -47.5198 | 2025-09-01 13:30:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 9174c3ee-26b1-3fe2-8b1a-143d4069a979 | -8.8625 | -47.5198 | 2025-09-01 13:40:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 152.8 |
| a9adfd09-68ce-3116-8821-9bf50ae3e08f | -11.0845 | -44.6343 | 2025-09-01 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 301.0 |
| 84ba8dd7-e93e-3b4f-a08c-21a04119c6a8 | -7.9351 | -46.4559 | 2025-09-01 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| dc7f9615-6e49-318a-94a3-3c64b1969704 | -11.7989 | -46.4341 | 2025-09-01 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 18d24366-b9a8-38a6-b56e-5c1ca384b6b3 | -11.8185 | -46.4087 | 2025-09-01 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 405f618b-3429-3445-8f60-b913282be2d4 | -6.8281 | -52.8143 | 2025-09-01 13:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 17ee487a-e26e-3003-b132-c7793aa62375 | -6.8428 | -43.3151 | 2025-09-01 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.5 |
| 7dfdcb34-f9d5-3dd4-b47a-66a542857f0a | -14.6483 | -43.9461 | 2025-09-01 13:40:00 | GOES-19 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 79.3 |
| 10eef357-6c35-3e00-9db6-2decfa86ffe2 | -10.8935 | -45.8084 | 2025-09-01 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 756f5c2c-1fa2-3d0d-9df7-3528a0424a0f | -7.0757 | -44.3606 | 2025-09-01 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 115.3 |
| b6ab846f-1560-3189-ba1d-a769c5bbcef7 | -6.8237 | -43.3402 | 2025-09-01 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 96.0 |
| 892c4708-9568-304d-93f4-99179fed3bb6 | -8.1943 | -46.788 | 2025-09-01 13:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 50c0158e-0d8b-3cfb-956e-c49b4d0b27de | -6.824 | -43.3168 | 2025-09-01 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 121.6 |
| 82b465f0-8d03-397c-a122-6a947fc9430e | -7.076 | -44.3376 | 2025-09-01 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 202.3 |
| 4dc3ad8f-b455-301e-b45a-e55601afb4cc | -9.6127 | -47.8169 | 2025-09-01 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 9292564c-afcf-35b0-9755-524e393b010a | -11.9623 | -45.8428 | 2025-09-01 13:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 59d3008f-dae5-333b-a893-ca2736fd5a71 | -11.0568 | -45.146 | 2025-09-01 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 144.6 |
| ef259470-f0da-3d68-8e93-bfc4d214399f | -6.7038 | -42.2665 | 2025-09-01 13:40:00 | GOES-19 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 78.7 |
| d0ec06b6-096e-3e46-8250-e6084d3c2cb1 | -13.4977 | -46.997 | 2025-09-01 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 7f9f4311-f280-36af-a01d-5ba643fbdc9b | -11.0377 | -45.1487 | 2025-09-01 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 915f9f5a-9a74-3acf-88d9-0dcf83f5aadc | -11.815 | -51.4572 | 2025-09-01 13:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 142.2 |
| e6211ca7-92c8-3f6b-a43f-82483b82be26 | -7.707 | -50.2765 | 2025-09-01 13:40:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| a3311ba3-9297-32bb-ba31-e41f86e97494 | -8.8437 | -47.5217 | 2025-09-01 13:40:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 216.8 |
| cf4a558b-c2e5-34e3-b721-b604184f544a | -6.8426 | -43.3385 | 2025-09-01 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.3 |
| 41c6ecbb-af38-3330-8ffe-59ca812459ff | -9.2825 | -47.1007 | 2025-09-01 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 34d8068e-ccf9-3f40-b78a-f2c5b933332b | -12.9768 | -48.1049 | 2025-09-01 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 3db8dcff-6540-3f6c-83b7-159e63ce057d | -6.9327 | -42.006 | 2025-09-01 13:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 95.6 |
| 5d9d8122-9cb9-3744-8683-55f6ec7802d1 | -12.9575 | -48.1076 | 2025-09-01 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 7a81d3c7-b61b-3e6b-ab62-ed0244b81d0b | -13.3439 | -46.9757 | 2025-09-01 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 0b1538db-163d-3cfe-8f4c-9667cd10e5d5 | -11.8147 | -51.4784 | 2025-09-01 13:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 3de791b3-12b3-356b-9689-ad1980965ecb | -11.3709 | -43.5631 | 2025-09-01 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 123.5 |
| d3bb6244-fea4-374b-9664-d653a29c4a02 | -6.8466 | -52.8132 | 2025-09-01 13:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 9f4d67df-c2e7-3b06-a932-579389e2882a | -7.0572 | -44.3393 | 2025-09-01 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 122.0 |
| b5f64e0a-6a6c-3b17-bd86-52ba8934d7f2 | -6.1665 | -43.3273 | 2025-09-01 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| a1664840-3a5e-35a0-90af-ea0b9f69f5b2 | -8.8936 | -45.1168 | 2025-09-01 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 5875a744-9512-3f02-b630-00585835a409 | -11.3701 | -43.6104 | 2025-09-01 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 4b09932e-b5a6-31d3-bb02-6ae10f5709a7 | -12.9764 | -48.1272 | 2025-09-01 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 65d7a670-f118-370a-aa26-d5f04fa4154a | -6.9314 | -45.5803 | 2025-09-01 13:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 5bb22c6f-53a6-3736-be78-e4dccd22455c | -9.6505 | -47.8128 | 2025-09-01 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| d2234c5b-25ca-3658-b582-a3c17dac2a18 | -6.9317 | -45.5578 | 2025-09-01 13:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 1e2f7b9b-f736-3c92-91c8-2f4e083d863a | -7.9348 | -46.4783 | 2025-09-01 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 439.7 |
| 148bc229-15ff-3b61-8aa2-d6bb415ccf40 | -8.8622 | -47.5418 | 2025-09-01 13:40:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| e5683ab2-8a28-35ee-9f86-ef3e0638ccac | -7.0946 | -44.3589 | 2025-09-01 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 69de394f-634d-3bdf-af89-fdba6be42e43 | -6.204 | -43.3241 | 2025-09-01 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| c4b2c5a9-ef63-35a8-90ca-2bebfff103fd | -13.3245 | -46.9787 | 2025-09-01 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 79.2 |
| bfbe3f26-129b-3469-a076-59d3745b907b | -8.9857 | -48.2096 | 2025-09-01 13:40:00 | GOES-19 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 798868be-c9e7-3752-a6ad-deeaf2c01470 | -16.2953 | -52.9443 | 2025-09-01 13:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| fe468c21-0005-3da1-abee-13bb10e74577 | -7.3992 | -47.4333 | 2025-09-01 13:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 113.0 |
| cb6a2fb9-db94-367c-b042-e876dab9681e | -14.0508 | -44.5543 | 2025-09-01 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 897e3ebd-c094-3496-8e28-0880615e123b | -14.0502 | -44.5779 | 2025-09-01 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| e551e1e1-2817-3453-9359-dfad927dcddd | -11.7798 | -46.4367 | 2025-09-01 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| a4ad2af0-8711-3a55-906a-2b718ef8008a | -7.9536 | -46.4765 | 2025-09-01 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 396.0 |
| 12be883b-e127-39d4-9776-7b842cba216e | -11.0849 | -44.611 | 2025-09-01 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 151.7 |
| 7101d18a-c33b-3659-82b4-7caa00501fe1 | -7.9539 | -46.4542 | 2025-09-01 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 154.0 |
| cfaf2646-a10b-3301-913c-f2e2a6d28cb7 | -11.0654 | -44.637 | 2025-09-01 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| e6d82f81-a53c-3410-99f1-cb0fcb058b6f | -13.5171 | -46.994 | 2025-09-01 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 61918e50-81af-3d28-8486-a4cc557f10ed | -6.9324 | -42.0299 | 2025-09-01 13:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 79.3 |
| 9c7fd927-1992-3712-a3db-c919cd365be3 | -11.3705 | -43.5868 | 2025-09-01 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 252.7 |
| 618a4000-1ee4-3e6f-8bb1-eeb92d8d8720 | -4.3197 | -48.0908 | 2025-09-01 13:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 77a72cf0-ed51-3767-9ee7-b3451fbd59fe | -11.7993 | -46.4114 | 2025-09-01 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 3ddc1d35-8b94-302d-a799-9562c063a267 | -11.8147 | -51.4784 | 2025-09-01 13:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 286c6724-ee0e-3d4e-a20e-788c1ca52302 | -14.6483 | -43.9461 | 2025-09-01 13:50:00 | GOES-19 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 80.5 |
| 5e3c656d-f5e9-3917-9006-5578de6c90da | -4.9122 | -43.2103 | 2025-09-01 13:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 293.4 |
| ad0aa797-c4b8-3188-b4fd-94182d44c007 | -6.744 | -43.7666 | 2025-09-01 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 7dee2232-9d6d-3043-8b10-7cc37846dcad | -5.3976 | -43.3633 | 2025-09-01 13:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| b18d92c6-502e-3bd6-9576-b4da918dc7c7 | -14.0502 | -44.5779 | 2025-09-01 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 83adcc0c-cd7a-3bf4-a671-554c1c1a5008 | -11.815 | -51.4572 | 2025-09-01 13:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 017130a6-25b2-3443-9387-228c2f45207a | -11.0845 | -44.6343 | 2025-09-01 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 175.2 |
| 9b6bce62-a8b6-3edd-a67b-5762c1fc0a60 | -9.6505 | -47.8128 | 2025-09-01 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 0dd9a952-7afb-3b43-b361-ddc0c8ad4bd7 | -6.8237 | -43.3402 | 2025-09-01 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 98.9 |
| 790fc3f9-c0a0-3cfd-9e71-f0d10db4024a | -9.6127 | -47.8169 | 2025-09-01 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 23bfb9e1-9bbc-33f9-9385-171c8bc37e3a | -7.0757 | -44.3606 | 2025-09-01 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 0745c5c5-682d-389d-be44-6c10291818e5 | -11.7989 | -46.4341 | 2025-09-01 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 21d8f62a-f803-3354-8c6a-52542531876f | -11.7985 | -46.4567 | 2025-09-01 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| c62ab60a-82fe-3374-915a-a5caf2167de6 | -6.8466 | -52.8132 | 2025-09-01 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| f8206f31-cb1d-352d-b07c-75c54b5af5bf | -11.3705 | -43.5868 | 2025-09-01 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 232.4 |
| 78177d72-1cd9-3c5d-bb4e-46331514be92 | -6.7628 | -43.7649 | 2025-09-01 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 116.8 |
| dee9fafe-9f16-3cad-a849-ee6d8010c78b | -6.8426 | -43.3385 | 2025-09-01 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 103.5 |
| eece9c1f-3440-38c5-b059-ae1b1e39409d | -9.2825 | -47.1007 | 2025-09-01 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |


[Clique aqui para ver as próximas entradas](README109.md)
