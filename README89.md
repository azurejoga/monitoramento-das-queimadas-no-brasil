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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f835a5b-2fb3-3927-b48b-a6a930e8c7f9 | -3.05869 | -46.50858 | 2024-10-05 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 807bd8e6-f614-3bac-b306-91023c4429f7 | -3.05575 | -46.50834 | 2024-10-05 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a5ab43f-984b-3002-a7b3-e9eee5834e9b | -3.04743 | -45.9407 | 2024-10-05 04:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 959b8575-d788-30f4-aa14-aaf279515193 | -2.76684 | -45.95325 | 2024-10-05 04:36:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79153d6b-d9ae-30c2-a589-e3f192f4884e | -2.74531 | -46.79064 | 2024-10-05 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b69b638-8b58-3930-8858-c4ead4314c52 | -2.74249 | -46.764 | 2024-10-05 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 008506e8-c291-3316-933f-2db37ac02731 | -2.74191 | -46.79013 | 2024-10-05 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e722aa72-126b-3b97-abe1-91f8fbe27588 | -2.74134 | -46.79378 | 2024-10-05 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3824f28e-17f7-39cb-aa23-befc44842c01 | -2.73965 | -46.75983 | 2024-10-05 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0eb84bfb-7065-39d3-ba66-87ad6037eaad | -2.73794 | -46.79327 | 2024-10-05 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3b96f95-9984-37ad-8bc3-b878a0b9b3a7 | -2.73625 | -46.75932 | 2024-10-05 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1bd7c140-9ce9-381a-8cf9-139494e37de0 | -2.72944 | -46.80318 | 2024-10-05 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 007c759e-c9d0-3c8e-af9f-478b40a3889a | -2.72604 | -46.80267 | 2024-10-05 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed90fb49-3afc-355e-824a-51ffa2b8f3ab | -2.72548 | -46.80631 | 2024-10-05 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fc79457-48b8-37da-bc4c-e9b02ae93e7b | -2.72208 | -46.8058 | 2024-10-05 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44d865f7-47f5-370c-b955-cf6c25fab331 | -2.71013 | -46.7253 | 2024-10-05 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 154da74a-54cc-322a-a87d-dd6e5fea343f | -2.62439 | -46.91458 | 2024-10-05 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be4bdc44-a327-35dc-bc96-0d522d903e58 | -2.62157 | -46.91045 | 2024-10-05 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97b84a8a-91aa-3c98-b655-718d28506338 | -2.55744 | -47.29926 | 2024-10-05 04:36:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f5574d2-50ee-363a-a527-19a0e6d27059 | -2.55689 | -47.30279 | 2024-10-05 04:36:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 27ecc3e7-73eb-3b13-9893-b323c7b8e456 | -2.36434 | -46.12671 | 2024-10-05 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b456bbad-101f-3f7b-bbb3-817c73c4885e | -2.36087 | -46.12617 | 2024-10-05 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4efca84c-1421-39cb-afd7-56a00747e4e1 | -2.23388 | -46.74348 | 2024-10-05 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7238993-aa45-3020-b542-b1be63d36aab | -2.23275 | -46.75074 | 2024-10-05 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5b25e4e-5e20-3862-9109-bd8ff22e8ef3 | -2.2322 | -46.73206 | 2024-10-05 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16e4c797-1238-3d95-9a22-ca8930cf6eac | -2.23218 | -46.75436 | 2024-10-05 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d31135b7-1da6-30f2-a574-97fee9f9eeef | -2.23049 | -46.74296 | 2024-10-05 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3bb3f4ba-114d-3093-9177-9aaa2438f65a | -2.22995 | -46.72425 | 2024-10-05 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa0c760a-462d-3b33-a1a9-3d7338314d87 | -2.22881 | -46.73154 | 2024-10-05 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52dfa739-04bf-3f6e-9715-9ef6620fcf6b | -2.22824 | -46.73517 | 2024-10-05 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6dfeeaf5-3942-3967-8fd2-939fbfc593d9 | -2.22767 | -46.73881 | 2024-10-05 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a05fdcf9-835d-33e8-a21e-e3ed7beece69 | -2.22598 | -46.72738 | 2024-10-05 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fe7c90e-4391-368c-b5eb-2433f8ec43f1 | -2.21066 | -46.86955 | 2024-10-05 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87d13f86-a887-3c76-a58d-ad20b1e931bd | -2.21009 | -46.87317 | 2024-10-05 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd72b6ba-d794-32b4-a1d7-a0877c1713d2 | -3.31991 | -47.019 | 2024-10-05 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a42cbb84-80ae-3fb2-94ca-451188501048 | -3.3176 | -46.98889 | 2024-10-05 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d057a8fe-c54e-3239-880f-8498eda3a947 | -3.31704 | -46.99252 | 2024-10-05 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07ca7d06-14fd-366a-aabd-9e72e95735e2 | -3.31257 | -47.0216 | 2024-10-05 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de6d5c77-47f1-3700-8b37-3e166482f365 | -5.0383 | -46.56916 | 2024-10-05 04:36:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e70bd594-d788-3eff-83ca-f54a430e472d | -5.0377 | -46.57307 | 2024-10-05 04:36:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 360cda3d-fc12-3a35-82f7-5a73769303d2 | -4.84591 | -46.52507 | 2024-10-05 04:36:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9c950867-fa81-33c6-ad0f-8afb477e1cb9 | -4.7674 | -46.67608 | 2024-10-05 04:36:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 586ce0d8-b954-3066-a21f-d44388c5f62c | -4.76453 | -46.67165 | 2024-10-05 04:36:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82ce964d-063b-33fe-9959-38daa94fa2d7 | -4.32337 | -46.71508 | 2024-10-05 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f10766b-d1b6-3096-9771-e0f4dc73e943 | -4.16171 | -46.83017 | 2024-10-05 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ab738b4-b3d6-32b4-a1a1-efc05bb7718d | -4.15828 | -46.82964 | 2024-10-05 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 247303c7-81e7-3d8b-9eec-23579694acdc | -4.13436 | -46.71051 | 2024-10-05 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 54765499-69cb-3092-a352-820ff480a0ea | -4.768 | -46.67223 | 2024-10-05 04:36:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa974cbb-cebe-389b-8c8a-6b04c03cf658 | -4.76393 | -46.6755 | 2024-10-05 04:36:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb1ac454-8834-386a-96ec-8b551a53e33d | -4.55261 | -46.40749 | 2024-10-05 04:36:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fe7630de-a86b-385c-8262-55d84636c279 | -4.53363 | -46.82333 | 2024-10-05 04:36:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86ab14af-6d69-3ca4-915e-4ad5cd21b139 | -4.32396 | -46.71128 | 2024-10-05 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0895849d-03d1-3c12-aad3-6cf87462dfb5 | -4.16458 | -46.8344 | 2024-10-05 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 610d9a51-98bc-3d20-a050-e5988c9c151a | -4.15886 | -46.82592 | 2024-10-05 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cce0202a-3cb8-33e4-a993-67f5d8a7b2b7 | -4.15543 | -46.82539 | 2024-10-05 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23c1336f-dfaa-3d40-9255-2ad5be8ac975 | -4.13034 | -46.71376 | 2024-10-05 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 611fdaa3-4f31-3539-8e47-3c1d035c5cdc | -4.12746 | -46.70948 | 2024-10-05 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46f44045-21ba-35ab-834b-dc843f2f79d8 | -3.92492 | -46.43896 | 2024-10-05 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 810a4788-1a0b-37b4-b03b-689ab79dcb83 | -3.92144 | -46.43843 | 2024-10-05 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0adc27f6-cf40-3440-8f0b-4b3afce9b94b | -3.90754 | -46.43626 | 2024-10-05 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60dd99f6-05b3-3270-aa42-da89a5a7f7c2 | -3.90635 | -46.44394 | 2024-10-05 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f51c143-4b71-3488-8730-e4bb7fdd6124 | -3.90575 | -46.44778 | 2024-10-05 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 005847e6-cdef-306e-b9e6-09ee999a4329 | -3.90287 | -46.44338 | 2024-10-05 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c4729b4-abc9-3ca7-8f3c-29c8b43fea07 | -3.90228 | -46.44723 | 2024-10-05 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ed58418-8f72-336b-a5b7-d8e90d230294 | -5.04264 | -47.15867 | 2024-10-05 04:36:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 74ef4640-1523-3cc5-8639-40b08423dad8 | -4.93777 | -47.13524 | 2024-10-05 04:36:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24b25863-5222-38fa-8141-987629f26812 | -4.9372 | -47.13892 | 2024-10-05 04:36:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5a79ebf5-2acb-306c-ad3f-46cc56adaadd | -4.34406 | -47.3007 | 2024-10-05 04:36:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 612ecfcc-2fb6-3bf7-bc7d-ddf69c1e08bc | -4.34349 | -47.30433 | 2024-10-05 04:36:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 52ca49cf-bdb3-31a6-acb3-ab63a96743b5 | -4.34182 | -47.29287 | 2024-10-05 04:36:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98b026bc-1466-3c99-a0c5-83a9c1cedc4b | -4.34125 | -47.29652 | 2024-10-05 04:36:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d22c1cb2-d9b6-356b-b54c-6b9b0d97c641 | -5.04606 | -47.1592 | 2024-10-05 04:36:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1cb0be02-87bd-3b92-bcf6-e8e1c22fbe36 | -4.3137 | -47.70615 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dfc010cb-e478-3b5e-965c-0487e23493cc | -4.24317 | -47.57168 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f95ae4a-f4c1-3d6d-8d2d-3bb4c3971ec2 | -4.23981 | -47.57117 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb0845de-607f-36ed-a722-f8986b45546f | -3.82479 | -47.48959 | 2024-10-05 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84c04987-33fc-341a-8335-cf4df21ba31a | -3.82424 | -47.49316 | 2024-10-05 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68addbe9-f3bf-32f7-8eb6-3a3026052605 | -3.82088 | -47.49264 | 2024-10-05 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83f24ac5-8747-3209-b949-922dca59db7f | -3.77203 | -47.60851 | 2024-10-05 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7571b31-488a-3e25-8349-8d2fe2fdcf00 | -3.76923 | -47.60446 | 2024-10-05 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b83e600-cb2b-36ee-b389-f6737d18c7e8 | -3.76814 | -47.61152 | 2024-10-05 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c825db35-2e7f-371b-ada4-49d83c4021fc | -3.69932 | -47.59711 | 2024-10-05 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8066a58a-adfc-32b7-a5bf-9cbfdc52f284 | -3.61659 | -47.51932 | 2024-10-05 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 087117f3-0a72-34d0-ac70-243ad64eeadb | -3.61604 | -47.52285 | 2024-10-05 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 78fbef60-2d2f-3482-a592-8b68de386196 | -3.61549 | -47.52639 | 2024-10-05 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| a3a0e395-d35c-3ffa-b466-2e030c721d55 | -3.61324 | -47.5188 | 2024-10-05 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb618ba9-5929-310e-99c6-c283366b2d94 | -3.61269 | -47.52234 | 2024-10-05 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 764c9b70-aa21-3f07-8e62-2cc194dc3f7a | -3.61214 | -47.52588 | 2024-10-05 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2d228fc3-fbf0-388c-8474-59b5a03a7c04 | -5.98382 | -46.653 | 2024-10-05 04:36:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 741c1b98-b875-3280-97f4-4937e7f5adbe | -5.98323 | -46.65692 | 2024-10-05 04:36:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ba3fea0-ab30-3548-b7b2-028214b1eeeb | -5.9803 | -46.65248 | 2024-10-05 04:36:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b2686af-b22e-3840-a371-bcca62c8ae91 | -5.38476 | -46.43016 | 2024-10-05 04:36:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 359eac7e-e520-3395-bb0c-b1077e451ada | -5.38122 | -46.42968 | 2024-10-05 04:36:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6bf23815-9e69-387d-b64c-3905bc17498b | -5.37769 | -46.42916 | 2024-10-05 04:36:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ef2802a3-33e0-327e-ae5e-c90bf9792693 | -5.97971 | -46.6564 | 2024-10-05 04:36:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f0322746-3410-35ca-b1b8-32b6038f77bd | -5.3983 | -46.57733 | 2024-10-05 04:36:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 071283f0-bece-3687-8ee2-39a3de995ccd | -5.43882 | -47.61034 | 2024-10-05 04:36:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cd0a3617-4f32-3822-873f-7b4e0de9d6ec | -5.43489 | -47.61343 | 2024-10-05 04:36:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5517add9-433f-3e4a-bc29-45b30a5369cd | -5.3655 | -47.71722 | 2024-10-05 04:36:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a2661b28-fe5e-3523-b854-45fb4ca9ab39 | -5.28684 | -47.32317 | 2024-10-05 04:36:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README90.md)
