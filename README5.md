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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 21f3e150-78f4-3b2f-a424-335df737addc | -7.8741 | -49.978298 | 2024-09-30 00:27:37 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a370f7e-3ac0-3430-b02b-d4e7858524ae | -6.5768 | -44.168701 | 2024-09-30 00:27:38 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 36c8d929-5cfc-3413-9158-30dd3641c2bf | -5.9804 | -45.3564 | 2024-09-30 00:27:52 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9296ce39-c085-3254-bc68-13aed3c19b2b | -5.982 | -45.3638 | 2024-09-30 00:27:52 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d2648c6b-d39a-30e7-942b-4119eeeb5788 | -5.9837 | -45.371201 | 2024-09-30 00:27:52 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 78e4b63f-5be3-3876-9c22-cee1416ef7d7 | -5.9706 | -45.358601 | 2024-09-30 00:27:52 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a5e944af-39c4-389a-b9cf-aa1aacb864eb | -5.9722 | -45.366001 | 2024-09-30 00:27:52 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 69e8c159-5045-3fe5-94ce-164c0768272c | -5.9739 | -45.373402 | 2024-09-30 00:27:52 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 21908957-6ff9-36da-b2b3-0c7dc2d127c0 | -5.3275 | -45.1091 | 2024-09-30 00:28:01 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 183bbd5e-6784-3930-8d04-f5bb1aabe095 | -5.0552 | -44.544498 | 2024-09-30 00:28:04 | METOP-C | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e00d4e44-9b0d-3034-8920-5371a5b032e7 | -5.0568 | -44.551498 | 2024-09-30 00:28:04 | METOP-C | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3f60dc0f-c58f-3418-934a-4f4a683779b4 | -5.6442 | -48.409302 | 2024-09-30 00:28:08 | METOP-C | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b7126a2-c828-321f-a27c-46daa78d2ee4 | -5.0912 | -46.159302 | 2024-09-30 00:28:09 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0764c7a9-1d12-3537-a545-8697ec2be4da | -5.0929 | -46.167099 | 2024-09-30 00:28:09 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c010c071-876b-3068-ac86-4ce0c7cae8a8 | -5.6615 | -48.812801 | 2024-09-30 00:28:09 | METOP-C | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 788123dc-2456-3296-8415-c3cb5a513603 | -5.6639 | -48.823898 | 2024-09-30 00:28:09 | METOP-C | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82f0d52f-513d-3b84-b413-2fe59dcb824b | -3.9577 | -41.477798 | 2024-09-30 00:28:10 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d97df68f-79e9-376f-a17c-feea0d53c742 | -3.9595 | -41.485401 | 2024-09-30 00:28:10 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 89c43259-5b69-3ef2-81a7-807313a2169d | -4.9301 | -45.627399 | 2024-09-30 00:28:10 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a36f5b2f-57a5-35cc-9da7-0a4a844b8115 | -4.9317 | -45.6348 | 2024-09-30 00:28:10 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c7b2b03f-e0da-317b-a609-ffe1875d7a37 | -5.7328 | -49.230598 | 2024-09-30 00:28:10 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aafa7920-ed15-39dd-874c-4827f8433070 | -4.412 | -43.8484 | 2024-09-30 00:28:12 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 83882b43-f50d-3715-9962-0a56ebcf8088 | -5.3217 | -47.8792 | 2024-09-30 00:28:12 | METOP-C | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f8fbafd3-8902-3f22-94ec-4df09cf874ad | -5.3238 | -47.888802 | 2024-09-30 00:28:12 | METOP-C | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d9bde0e8-ee9e-32b1-b72d-cc1f4ef3aabb | -5.3097 | -47.8717 | 2024-09-30 00:28:12 | METOP-C | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 980b4919-b7b1-3755-941e-f20091ecd2d4 | -5.3119 | -47.881302 | 2024-09-30 00:28:12 | METOP-C | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2ec75d4d-c379-393f-9606-2cf643498f35 | -5.5398 | -49.004002 | 2024-09-30 00:28:12 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14553a8b-a660-369a-b0e0-fac78ce0838b | -5.5125 | -48.9268 | 2024-09-30 00:28:12 | METOP-C | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7ad6a16-7960-39aa-876e-04a6d0416293 | -4.6016 | -46.634201 | 2024-09-30 00:28:19 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 73e5e99a-ad91-388e-b427-41cac5b3730c | -4.6034 | -46.6423 | 2024-09-30 00:28:19 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f530ea24-5d06-329d-bd00-b153950ef531 | -5.2857 | -50.034302 | 2024-09-30 00:28:20 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 725f6dfc-746e-33bd-9825-562455d962c7 | -5.2886 | -50.0476 | 2024-09-30 00:28:20 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c9ea7dc-f3c7-34aa-b8c2-5aa31c7c2649 | -5.2915 | -50.060902 | 2024-09-30 00:28:20 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a8f8db8-3aea-392a-94a4-775e9dbe2542 | -4.3212 | -45.8479 | 2024-09-30 00:28:20 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fd0601e8-2b44-322b-bb9b-1b76e660bb45 | -4.3229 | -45.8554 | 2024-09-30 00:28:20 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b757ca88-cc7f-3170-9ba4-a3b2c0e277a8 | -4.3742 | -46.0821 | 2024-09-30 00:28:20 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f7252046-974a-31f0-94f7-2cf721e46b52 | -4.3759 | -46.089699 | 2024-09-30 00:28:20 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b8b35510-6bbb-3571-8120-8c0abaf69432 | -4.6476 | -47.433899 | 2024-09-30 00:28:21 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4151dda0-a44f-31d8-a062-328c7466bccb | -4.9079 | -48.601398 | 2024-09-30 00:28:21 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77f6407a-353d-36a1-861a-8e9e195202fd | -4.6333 | -48.519001 | 2024-09-30 00:28:25 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7fe6798-862a-3153-b50c-0c3b6532075f | -4.6235 | -48.521099 | 2024-09-30 00:28:25 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1888fa91-f0e1-3eb4-983b-68e2a78edc48 | -3.6316 | -44.2672 | 2024-09-30 00:28:26 | METOP-C | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 663aa513-5f31-3607-b091-13112ad5b8dd | -4.4887 | -48.1007 | 2024-09-30 00:28:26 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 858933ad-3fbf-3275-8b6d-d04ad8d9b6f3 | -4.1748 | -46.839199 | 2024-09-30 00:28:26 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 997604fb-8a14-3be0-a6d0-05e9ad73a71d | -4.1766 | -46.847401 | 2024-09-30 00:28:26 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d08da65c-0e54-310b-948d-f248955f04e3 | -4.1785 | -46.855598 | 2024-09-30 00:28:26 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| aa4ea947-6aed-3eaa-930f-e60e3a64caee | -4.1668 | -46.849499 | 2024-09-30 00:28:27 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1697befd-a8c6-31d8-951a-e13cf2c8700d | -3.6211 | -44.536499 | 2024-09-30 00:28:27 | METOP-C | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b453a50d-1cf7-3e64-8ad8-a3fa4145581f | -3.5869 | -44.5224 | 2024-09-30 00:28:27 | METOP-C | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cd23f86e-aed7-34f5-8505-bcd8149ccd44 | -3.5885 | -44.529301 | 2024-09-30 00:28:27 | METOP-C | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 103d6873-b6ea-354c-a0a0-9fc998b5cde4 | -3.5901 | -44.536201 | 2024-09-30 00:28:27 | METOP-C | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4a42c058-5ad9-375a-b7e1-94ab7adb7e74 | -3.5771 | -44.524601 | 2024-09-30 00:28:28 | METOP-C | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4124f846-c785-39a2-ab98-e0af4faf229a | -3.5787 | -44.531502 | 2024-09-30 00:28:28 | METOP-C | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 38c70905-1a14-3872-b790-c2ce72296e54 | -3.5803 | -44.538399 | 2024-09-30 00:28:28 | METOP-C | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e9e0bc4c-bdea-3704-908a-ef27d096c9c3 | -4.1811 | -47.9184 | 2024-09-30 00:28:30 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fdd4a0f-4a33-324d-b271-a6a2ad1e558d | -4.2784 | -48.628502 | 2024-09-30 00:28:31 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e7c2e2a-1722-3946-beb7-a0aaa34b871f | -4.2807 | -48.638802 | 2024-09-30 00:28:31 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 451ee2d4-1463-3073-9014-ae4a7312c0ef | -4.2663 | -48.6203 | 2024-09-30 00:28:31 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba4820ff-b392-3994-be13-2fffe18e2028 | -4.2686 | -48.630699 | 2024-09-30 00:28:31 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17d21479-7a7f-3c98-8cc6-d3274192a7b6 | -4.2709 | -48.640999 | 2024-09-30 00:28:31 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b621fcd0-6a09-3214-bacf-7280007f536e | -4.2134 | -48.5672 | 2024-09-30 00:28:32 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e18aa392-412d-3fe3-992c-0bfa1e6a825c | -4.2157 | -48.5774 | 2024-09-30 00:28:32 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5710963d-b17e-3235-aad5-f709c53bfc5c | -3.7699 | -47.551601 | 2024-09-30 00:28:36 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23b87b27-e8af-3ea3-bc36-0ea4815ac211 | -4.1121 | -49.077801 | 2024-09-30 00:28:36 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0720e24d-2526-36d0-9594-6b0cacfe73ae | -2.715 | -46.707699 | 2024-09-30 00:28:50 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e500f880-4b49-384a-9c56-344b19eb6e3d | -2.7167 | -46.7155 | 2024-09-30 00:28:50 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52575965-1d4b-3ccb-9a47-d737dad0e7c1 | -3.1007 | -49.367298 | 2024-09-30 00:28:53 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51f0b878-d852-33cb-8208-02adedba785a | -3.1031 | -49.3783 | 2024-09-30 00:28:53 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3a3ded2-5f7d-31be-85d6-736407879c34 | -3.1056 | -49.3894 | 2024-09-30 00:28:53 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e93ea86-78eb-3356-bd5a-7e72d402df0a | -3.1081 | -49.4006 | 2024-09-30 00:28:53 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70a42d0f-d0cf-3014-8834-3f6a31cf0672 | -3.0933 | -49.380501 | 2024-09-30 00:28:53 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2233630c-757f-386a-95c9-56a83abaed48 | -3.0958 | -49.391602 | 2024-09-30 00:28:53 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1386b604-3e2d-3fd1-919c-c2c9c5de9a0c | -3.0983 | -49.402699 | 2024-09-30 00:28:53 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2682f5e4-e001-3b34-ab66-50245583d3d3 | -3.2952 | -50.645199 | 2024-09-30 00:28:55 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0d0e316-5be1-30db-9341-b5aab7b52ba8 | -3.0884 | -50.452801 | 2024-09-30 00:28:57 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3a7e2d8-6c0e-3e75-9582-23df9e8f0a72 | -3.0914 | -50.4659 | 2024-09-30 00:28:57 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87caea57-536e-33b8-b4e5-dda05d394f3d | -3.0757 | -50.441898 | 2024-09-30 00:28:57 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4030a9ad-9870-33ff-99c7-e836d8d34eca | -3.0786 | -50.454899 | 2024-09-30 00:28:57 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81dc4ff2-210f-3a13-8c7a-ea4832e2e4a3 | -3.0816 | -50.467999 | 2024-09-30 00:28:57 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f994125-534d-3993-bafd-01f29fcbf2bf | -3.0614 | -51.198799 | 2024-09-30 00:29:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b3cd908-c826-3eb7-a1d6-be619a13b367 | -3.0337 | -51.440102 | 2024-09-30 00:29:02 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45092b01-f701-3f47-ab82-d3b58388af6e | -3.0269 | -51.409698 | 2024-09-30 00:29:02 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5264d21f-ce84-3996-a92f-38a9aa34ef84 | -3.0303 | -51.4249 | 2024-09-30 00:29:02 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6bfbfc8-4c1b-3175-a72e-56528da12eea | -3.0205 | -51.426998 | 2024-09-30 00:29:02 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66979dc0-6c6c-3bad-812e-9248e95ff5f7 | -1.6495 | -46.145302 | 2024-09-30 00:29:05 | METOP-C | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f2a01e29-b5d7-30ed-bdb0-c16622762e96 | -1.7254 | -47.108601 | 2024-09-30 00:29:07 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4c1aa10-8edf-3a22-8f97-6b005ef5bf3b | -1.7272 | -47.116501 | 2024-09-30 00:29:07 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a120a70f-2ea9-3bb6-a8e9-deadef357dfe | -2.701 | -51.323502 | 2024-09-30 00:29:07 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 570795d1-1dad-3e7b-b614-4cf969ee3f0d | -2.688 | -51.310902 | 2024-09-30 00:29:07 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a04dab51-10ef-38a2-b5c3-c801c2cbd0ae | -2.6913 | -51.3256 | 2024-09-30 00:29:07 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8deafb90-8a98-338c-b67a-a7ceb0e8eb71 | -3.0721 | -53.0257 | 2024-09-30 00:29:07 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8c6f393-afc9-3570-8378-63b550e39651 | -3.0765 | -53.045399 | 2024-09-30 00:29:07 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ccc39e5-99be-3c28-8daa-36eb72733db6 | -3.0624 | -53.027802 | 2024-09-30 00:29:07 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1197c81d-dabb-33b6-a322-c423218e73af | -3.0668 | -53.047501 | 2024-09-30 00:29:07 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ed84d2f-46b2-3e00-97b0-de9d94dfb4c4 | -3.1187 | -53.691101 | 2024-09-30 00:29:09 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fa827af-a2ad-3717-9674-0b00b400c233 | -3.1236 | -53.7132 | 2024-09-30 00:29:09 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f557aa7-650d-3c01-9755-dd231040dddf | -3.1091 | -53.693199 | 2024-09-30 00:29:09 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 621aeb79-3042-38be-b286-525ab5cf5e4e | -3.114 | -53.715302 | 2024-09-30 00:29:09 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e2c4078-0a1d-366b-82bf-2516761d2d92 | -2.1937 | -52.0187 | 2024-09-30 00:29:18 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9fdcafe-86a1-3c07-8f0f-c87d820b397b | -1.3854 | -49.360401 | 2024-09-30 00:29:21 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
