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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed6a5174-fe71-3934-a3aa-0c2973b72043 | -3.528 | -52.568901 | 2025-12-16 00:34:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d5a303a-5aa2-358f-8e42-434d62886712 | -20.311899 | -57.2738 | 2025-12-16 00:34:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 072a7841-67f1-31c4-bc93-76cffdbba018 | -16.064501 | -58.982899 | 2025-12-16 00:34:00 | METOP-B | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 07c131d4-04c2-3c7d-91b1-450168f455e3 | -10.7368 | -52.447701 | 2025-12-16 00:34:00 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 475f318c-1b4c-3d61-8001-ececac0e15e7 | -20.3097 | -57.261902 | 2025-12-16 00:34:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8e2aa192-ee78-31f1-9235-75898c33c6e0 | -12.3077 | -57.361801 | 2025-12-16 00:34:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 70c94f27-2064-36b6-ae24-04d41ff77cc2 | -20.319401 | -57.259899 | 2025-12-16 00:34:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b4bb2779-1ceb-37b8-a6a4-25ac4666833d | -2.0221 | -45.820999 | 2025-12-16 00:34:00 | METOP-B | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4251eca0-ac76-3b7d-8bf5-114b7c6f6d51 | -2.3163 | -55.701302 | 2025-12-16 00:34:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b332a340-8e8c-34ea-9de5-2f70af0c4670 | -2.3091 | -55.624001 | 2025-12-16 00:34:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6f2538b-9670-3ead-9297-5cb01a28ecd9 | -17.809999 | -40.1376 | 2025-12-16 00:34:00 | METOP-B | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0f6c8643-d5fb-345e-bad3-eb966dc79a7d | -1.2187 | -53.730099 | 2025-12-16 00:34:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9aef0a8d-54f4-3bc5-8ee4-31af0be6ad31 | -12.3097 | -57.370998 | 2025-12-16 00:34:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a251f02d-e585-397e-8a21-5ea124efef02 | -3.655 | -47.572201 | 2025-12-16 00:34:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25ff8cd4-8573-38c7-82c7-08dbd78c6964 | -1.6625 | -52.068699 | 2025-12-16 00:34:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7024bc68-036e-3c41-8118-ff1e04ba214e | -2.0372 | -45.841202 | 2025-12-16 00:34:00 | METOP-B | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b4099d76-be5a-37ff-8374-9d887c6ff97c | -12.2999 | -57.3731 | 2025-12-16 00:34:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ac75e378-a3ce-3cbc-a570-586767b72ba2 | -2.0318 | -45.818699 | 2025-12-16 00:34:00 | METOP-B | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 64eed396-2357-34ea-985b-4bf9d1f7e612 | -1.6645 | -52.077499 | 2025-12-16 00:34:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbca2bed-1d89-3051-b771-5e16b266d892 | -3.6542 | -44.252 | 2025-12-16 00:40:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 41.5 |
| dc96d073-82ba-3649-ba1f-4d627d17c9c3 | -5.1174 | -43.2898 | 2025-12-16 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| a7df9e5d-f465-305e-aee0-f039d1bee629 | -2.0486 | -45.8231 | 2025-12-16 00:40:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 48.6 |
| ad42c4a4-a5ef-310f-84e1-2c0180ecba20 | -2.0301 | -45.8013 | 2025-12-16 00:40:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 100.1 |
| d9cb5012-9ffc-378f-91c4-53ea867f00e2 | -2.0301 | -45.8236 | 2025-12-16 00:40:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 52b1f462-d89e-3a44-a0c9-cf1050d72f79 | -12.2885 | -57.3624 | 2025-12-16 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| bd84e988-dac8-3730-bbf6-2c15a6b137a0 | -16.0616 | -58.9778 | 2025-12-16 00:40:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 55.4 |
| fee7c0e7-8ae6-3d0c-8381-5f97838908d2 | -12.3072 | -57.3808 | 2025-12-16 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| ffdde10e-f2fb-30fa-804b-93811d17336d | -12.3074 | -57.3608 | 2025-12-16 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 8ea8c37a-1735-3605-b64f-dca8207668c6 | -2.0487 | -45.8008 | 2025-12-16 00:40:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 8d2f04d6-37b0-3430-a71a-0db91c9eff82 | -1.6637 | -52.065 | 2025-12-16 00:50:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| ca17e9c3-5091-3efc-a2bb-81de55cb2cdf | -12.3264 | -57.3592 | 2025-12-16 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| d97a8f0a-77e2-3e67-9df2-a9767a1906c8 | -12.3074 | -57.3608 | 2025-12-16 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 184.6 |
| 8e3e477b-c534-36e1-b6bb-ec20bf7020a4 | -12.3072 | -57.3808 | 2025-12-16 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 115.5 |
| b6a61883-5a26-3b0f-9491-7a0dc06c8f2b | -8.0696 | -43.1452 | 2025-12-16 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 52.3 |
| 0b7b19ea-281d-3fb2-b247-7a2085ec92dc | -3.0822 | -43.1454 | 2025-12-16 00:50:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 47c43235-cc56-32bc-9f57-f101c76866ec | -5.1174 | -43.2898 | 2025-12-16 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 10d37ca3-1033-379a-8cbd-69dff0fe38e6 | -2.0487 | -45.8008 | 2025-12-16 00:50:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 3fdedb71-0cd3-37f8-b400-60e25362efe0 | -12.2885 | -57.3624 | 2025-12-16 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 917278ed-bcd3-3a66-9a8f-e1dde6ba2ec5 | -12.2882 | -57.3824 | 2025-12-16 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 8fd02e2e-acfb-34ed-b36b-f17b52297ca4 | -12.3076 | -57.3408 | 2025-12-16 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 3b7ef46d-05d8-3c74-baf6-868a03d62cd7 | -2.0301 | -45.8236 | 2025-12-16 00:50:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 4fcde77c-adec-36ca-883b-6b5d5b8f918b | -2.0301 | -45.8013 | 2025-12-16 00:50:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 60e73549-7171-36c8-a0bf-b60663f328f5 | -12.2882 | -57.3824 | 2025-12-16 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 91aa9cf7-c84e-3eb3-9a66-9d0aa06b0440 | -12.2885 | -57.3624 | 2025-12-16 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 113.9 |
| aecaa8b6-93f8-3af1-b4ca-a23167599b19 | -2.0301 | -45.8013 | 2025-12-16 01:00:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 0d0d34cf-8bf8-33fd-bb09-aecd63d5f43f | -12.3074 | -57.3608 | 2025-12-16 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 210.9 |
| f6624a2a-87a0-36a4-91ff-0828facf75b2 | -8.0696 | -43.1452 | 2025-12-16 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.5 |
| 15a6c225-5bce-3523-8bba-fed7aaa038da | -12.3072 | -57.3808 | 2025-12-16 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 111.2 |
| a78773f2-9a09-3c1d-88cd-ff1ff8891f7f | -5.1174 | -43.2898 | 2025-12-16 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| e10cdf4f-9303-3381-8d1f-b85dc3303022 | -3.4264 | -41.6423 | 2025-12-16 01:00:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 63.0 |
| 90dc4498-53e1-372d-b1c1-405865c91674 | -2.0301 | -45.8236 | 2025-12-16 01:00:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 67.9 |
| e70e04cb-bcbd-3fcf-be63-3f1d2c12fd36 | -12.3264 | -57.3592 | 2025-12-16 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 7bcb6f7c-6e0f-3156-8fa7-57e71444e953 | -2.0301 | -45.8013 | 2025-12-16 01:10:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 79cfe3e3-f597-3394-943d-3773bed084f8 | -3.4264 | -41.6423 | 2025-12-16 01:10:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 55.9 |
| 6979388f-7a97-3b5a-bc8b-932ef512b806 | -12.3072 | -57.3808 | 2025-12-16 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 9591bb94-2e8f-3771-8805-5a9e80796ad2 | -5.1174 | -43.2898 | 2025-12-16 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 9b3aeb2f-40f0-3b4f-9291-0c524b8896b1 | -12.2882 | -57.3824 | 2025-12-16 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| daf72c04-adf5-3c69-8594-dee7d564b445 | -2.0301 | -45.8236 | 2025-12-16 01:10:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 5021a3e4-fa66-3490-8bd7-8b3f5c283657 | -12.3264 | -57.3592 | 2025-12-16 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 25b60621-d749-3522-a5b7-90026aeff99f | -12.3074 | -57.3608 | 2025-12-16 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 196.9 |
| ab7d36dc-7d75-3cae-8385-9a43ef6e530a | -12.2885 | -57.3624 | 2025-12-16 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 6b765012-937e-301f-8c09-cb1eb54a5f6a | -12.3057 | -57.382301 | 2025-12-16 01:15:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 03d1ad24-caf6-34a2-b6a8-ba068de98750 | 3.8714 | -60.523499 | 2025-12-16 01:15:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7f83ede3-bfd6-301c-9cb7-570d1d25b4a8 | 3.873 | -60.516499 | 2025-12-16 01:15:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0ed9b492-bbe8-3e2f-8e02-1f6f41a40c7d | -12.2959 | -57.384499 | 2025-12-16 01:15:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c6a81a8c-aff5-3977-aa76-97c093adfa15 | -12.2943 | -57.377201 | 2025-12-16 01:15:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 86b5a8f1-2828-3eba-a44d-b433096b3f8c | -12.3155 | -57.3801 | 2025-12-16 01:15:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ce8b009e-9360-39e1-8005-7e142c1f9176 | -12.3139 | -57.372799 | 2025-12-16 01:15:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3a8331a4-5e53-37b1-beaa-85a16ac0fb70 | -12.3025 | -57.367699 | 2025-12-16 01:15:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9d77c072-9d99-3184-b35e-8c6ba17101d6 | -12.3107 | -57.3582 | 2025-12-16 01:15:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3942cc5f-d42d-3f0a-8c7f-1aa418b5c4d6 | -12.3123 | -57.365501 | 2025-12-16 01:15:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dec37a94-7cf2-3dbf-8f13-cf7f85c61ae5 | -12.3041 | -57.375 | 2025-12-16 01:15:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fdbaa050-e9e9-3f61-9f54-0a2e1d12ea03 | -12.2927 | -57.3699 | 2025-12-16 01:15:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8003bed9-e9fd-3a5d-a54d-f03812d4c54f | -6.5738 | -51.117802 | 2025-12-16 01:15:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b2c40d6-f3ff-32b3-9b97-e3a1cf60d6f9 | -12.3009 | -57.360401 | 2025-12-16 01:15:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b50571e0-4768-3925-b75f-d301bb74d3ea | -12.3072 | -57.3808 | 2025-12-16 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 124.4 |
| 569cfabf-b499-3626-be07-372371f5625e | -12.3074 | -57.3608 | 2025-12-16 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 210.9 |
| a210d2f2-759d-33e5-8f03-5b51413f0427 | -5.1174 | -43.2898 | 2025-12-16 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 66bbe448-3ac7-34bf-af88-bbe8c1b636f3 | -12.2885 | -57.3624 | 2025-12-16 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 96.5 |
| e96c8e27-76e0-39bd-a3a3-1db176700e43 | -12.2882 | -57.3824 | 2025-12-16 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 796abf41-d8c6-391b-8057-19a9c310cc36 | -12.3264 | -57.3592 | 2025-12-16 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 16f20a11-92f2-3598-85cd-3ee0b1479e37 | -12.3074 | -57.3608 | 2025-12-16 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 210.4 |
| 5aa047fb-5e1f-30c6-a8fc-cb9fab6691ea | -12.2882 | -57.3824 | 2025-12-16 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| eaddbb5c-3303-3de6-bdb9-1a5a1697eb16 | -12.3072 | -57.3808 | 2025-12-16 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 109.6 |
| cd077f64-05ba-31ad-a183-5d467c6e745d | -12.2885 | -57.3624 | 2025-12-16 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 87.8 |
| c3cd3517-27d2-365a-8c16-5710282b5023 | -12.3076 | -57.3408 | 2025-12-16 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 4993f0fa-8a04-3e59-a96c-97be0c60d40c | -12.3074 | -57.3608 | 2025-12-16 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 190.3 |
| ecab16a5-c9ea-3f36-a787-e8c0cc80bf56 | -12.3072 | -57.3808 | 2025-12-16 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 103.9 |
| ee4afd57-8d8d-3967-97b0-42698630e571 | -12.2882 | -57.3824 | 2025-12-16 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| a1170c35-af1d-3dcb-be75-e762383acc8b | -12.2885 | -57.3624 | 2025-12-16 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 8aad73a2-b990-3075-85c5-87c2b4b58334 | -1.2871 | -46.4156 | 2025-12-16 01:40:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 65ac73b9-9def-32f3-88ee-968931016a32 | -12.2885 | -57.3624 | 2025-12-16 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 72991fdd-aed0-32b0-8cc6-15d225aac80f | -12.2882 | -57.3824 | 2025-12-16 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 1c6cc8ce-87e4-38be-a4e6-edac879161c1 | -12.3072 | -57.3808 | 2025-12-16 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 06c84fb0-51de-3a4c-b051-80c51917c3eb | -12.3074 | -57.3608 | 2025-12-16 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 2ec719f4-6a78-3ae0-aa02-45a1f094f520 | -12.2882 | -57.3824 | 2025-12-16 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| f7a88435-8ae2-325b-90f4-380e14d17075 | -12.3072 | -57.3808 | 2025-12-16 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 9725ecdf-7c2a-3f95-80e4-0564919d71d8 | -12.2885 | -57.3624 | 2025-12-16 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 33a86441-a025-330b-9dfd-466f21d9b655 | -12.3074 | -57.3608 | 2025-12-16 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 156.5 |
| 9671ab4e-dcdf-3aa1-9720-22b12298304a | -1.2871 | -46.4156 | 2025-12-16 02:00:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |


[Clique aqui para ver as próximas entradas](README4.md)
