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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad1b6d47-15cf-3abf-8f09-11fa0f5a75d4 | -5.1529 | -47.960201 | 2024-10-10 00:21:04 | METOP-C | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4d110f99-17cd-33c5-8049-154d5247465e | -5.1557 | -47.972801 | 2024-10-10 00:21:04 | METOP-C | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c8669e4d-2709-3b66-871f-3ddb5bd3ffe6 | -4.8517 | -46.7374 | 2024-10-10 00:21:04 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 55dd429e-a5d0-379e-90b4-dc0a6180d30e | -4.854 | -46.747799 | 2024-10-10 00:21:04 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c330149f-9a66-318c-b27a-8f7385376cce | -4.6173 | -45.824001 | 2024-10-10 00:21:05 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6b62a5d5-eeb2-3c1d-9f03-f10c26d15e4a | -4.2534 | -44.616901 | 2024-10-10 00:21:06 | METOP-C | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5d33cb57-146d-354e-b354-63a36ae43ec4 | -4.2552 | -44.624802 | 2024-10-10 00:21:06 | METOP-C | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 534dc11a-0964-3de2-8f90-c4e9cac1eb84 | -4.2223 | -44.387901 | 2024-10-10 00:21:06 | METOP-C | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b8e77fcf-7432-3640-81bf-8c8859837254 | -4.224 | -44.395599 | 2024-10-10 00:21:06 | METOP-C | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9aed6a1d-97a2-3121-b153-05e2fe59e793 | -4.2125 | -44.390099 | 2024-10-10 00:21:06 | METOP-C | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 753fb2b8-0e8d-3bfc-b794-15eeb960a89d | -4.2142 | -44.397701 | 2024-10-10 00:21:06 | METOP-C | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9508d0f4-bec6-3a12-8f0b-4fa37c412511 | -4.2061 | -44.4076 | 2024-10-10 00:21:06 | METOP-C | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 88845b33-c67d-3860-9ed8-e6f7f76bcc6d | -4.2079 | -44.415298 | 2024-10-10 00:21:06 | METOP-C | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dae2c74c-b56d-39b1-aabf-0647e67f1b06 | -4.7347 | -46.994598 | 2024-10-10 00:21:07 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dcff96e0-d131-37d9-931b-8cd682e43c18 | -4.8566 | -47.591099 | 2024-10-10 00:21:07 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bcebefd4-e4ce-3593-978c-8cab77e34244 | -5.684 | -51.4366 | 2024-10-10 00:21:07 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd312d2c-ac5d-3d26-bec6-7abf9d9473da | -4.4186 | -45.716499 | 2024-10-10 00:21:07 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 884acf23-e8b7-32ae-9c59-a19f1b550544 | -4.3884 | -45.902599 | 2024-10-10 00:21:09 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 89ccb806-87f2-3715-9462-6ed5f207fd24 | -3.9768 | -44.258598 | 2024-10-10 00:21:09 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f73514c5-8326-3e2b-917c-104d6b00bcaa | -3.9785 | -44.266201 | 2024-10-10 00:21:09 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 409308d2-434e-315d-80f1-2bbcae3cc32d | -3.967 | -44.2607 | 2024-10-10 00:21:09 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ca73938b-2ef0-3a5f-9d81-cfd61494762a | -3.9687 | -44.268299 | 2024-10-10 00:21:09 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 075a2ce9-a24a-3e6f-a52d-8c01367d1eeb | -4.2088 | -45.468899 | 2024-10-10 00:21:10 | METOP-C | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f148b24d-77eb-382a-9537-aa6ce691a679 | -4.2107 | -45.477402 | 2024-10-10 00:21:10 | METOP-C | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 40338c84-0cd6-3933-a226-54f6698b6721 | -4.2127 | -45.486099 | 2024-10-10 00:21:10 | METOP-C | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 47209e42-312b-3f5c-81f8-c223dd7c90ba | -4.199 | -45.471001 | 2024-10-10 00:21:10 | METOP-C | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6a98af91-a414-34d5-891e-585b1e174b86 | -4.2009 | -45.4795 | 2024-10-10 00:21:10 | METOP-C | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b002505e-5fd7-3d62-8448-e3dbd4e19707 | -3.544 | -42.7644 | 2024-10-10 00:21:11 | METOP-C | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7bf3578c-a08d-3880-b1a1-dfeebc2a6f16 | -3.5456 | -42.771301 | 2024-10-10 00:21:11 | METOP-C | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b3cf2faf-9594-3776-ad23-0d47a8d5fc8a | -4.4083 | -46.5882 | 2024-10-10 00:21:11 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e71c5d3a-e490-36a2-bec3-2d906b762cc9 | -4.4105 | -46.598202 | 2024-10-10 00:21:11 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 68cc470e-a8fa-3b0d-83ec-6bdb6f63347c | -4.4128 | -46.6082 | 2024-10-10 00:21:11 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 733db69d-951d-3df8-ab51-101c0532e1a7 | -4.3985 | -46.590401 | 2024-10-10 00:21:11 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fac27f07-c99f-3e60-b418-a54b4567339f | -4.4007 | -46.600399 | 2024-10-10 00:21:11 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f1a2c0c8-d00e-341e-982e-0b54e4f7fdcc | -4.403 | -46.610401 | 2024-10-10 00:21:11 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cb567040-d174-3c14-b944-0ee5bcba1b79 | -3.8382 | -44.8741 | 2024-10-10 00:21:14 | METOP-C | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fb398384-36e5-3660-acc1-dcec5d69091f | -3.84 | -44.882099 | 2024-10-10 00:21:14 | METOP-C | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 91419ebe-b4ec-3c79-be30-88fa60d44d17 | -3.7143 | -44.372002 | 2024-10-10 00:21:14 | METOP-C | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6c62d7ab-a5ca-3357-b9b9-e1bf234d84ff | -3.716 | -44.379601 | 2024-10-10 00:21:14 | METOP-C | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 677205ab-cd80-32ca-a979-fd5527e6e62d | -4.5295 | -48.054699 | 2024-10-10 00:21:14 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f441b858-d557-37a9-85b8-670e71a96949 | -4.5323 | -48.0672 | 2024-10-10 00:21:14 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4bb834e-c68f-39fa-8fb2-a7b963ee4860 | -4.5225 | -48.069302 | 2024-10-10 00:21:14 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f43bdc4d-1300-359e-bc24-af20ed94c24c | -4.4079 | -47.737202 | 2024-10-10 00:21:15 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 661d0c6e-fd5e-341b-9593-b24531ac5d1e | -4.3955 | -47.727501 | 2024-10-10 00:21:15 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4709ef35-c815-3394-93d6-7cba460a702b | -4.3981 | -47.7393 | 2024-10-10 00:21:15 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86cce2fb-a10a-3565-b152-80588c83b5e2 | -3.9968 | -45.988201 | 2024-10-10 00:21:15 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7e744843-a961-3ba8-9bd4-56a680d657ba | -3.9988 | -45.997299 | 2024-10-10 00:21:15 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fb80a92b-a95a-3f58-887d-360fa2743889 | -4.2796 | -47.298199 | 2024-10-10 00:21:15 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c2ffd5a1-d35c-3c58-942c-cbaef06cb445 | -4.4081 | -48.107101 | 2024-10-10 00:21:16 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34d541ab-f95d-3135-91e0-8bde4e41688d | -4.4109 | -48.119598 | 2024-10-10 00:21:16 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d99ce550-ba59-348a-9121-ac1a9686e220 | -3.653 | -44.965099 | 2024-10-10 00:21:17 | METOP-C | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ac10d3ce-676d-318c-8e73-dd2cca912e5c | -3.6548 | -44.973099 | 2024-10-10 00:21:17 | METOP-C | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6aacef1d-f933-3f02-9434-0d07684a2c6e | -3.6414 | -44.959301 | 2024-10-10 00:21:17 | METOP-C | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6b0da673-fd60-343c-afb2-e4bc6477b735 | -3.6432 | -44.9673 | 2024-10-10 00:21:17 | METOP-C | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b8d7c0e6-7dd0-3603-bcdf-408a63792479 | -3.645 | -44.9753 | 2024-10-10 00:21:17 | METOP-C | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 196c4349-5b72-3395-b65b-ddb16e82318b | -3.6469 | -44.983299 | 2024-10-10 00:21:17 | METOP-C | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5415eb59-74af-3b45-a38d-7854511d247d | -4.2457 | -47.698299 | 2024-10-10 00:21:17 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82ba5cb9-eed2-3a83-9498-e1e3cdee9f19 | -4.2483 | -47.709999 | 2024-10-10 00:21:17 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82e529a4-840c-3b3e-8c54-9e890fc92e1b | -4.2509 | -47.721699 | 2024-10-10 00:21:17 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f8751a7-4c88-3d21-a96e-b29c41b2aeaf | -3.7428 | -45.499199 | 2024-10-10 00:21:18 | METOP-C | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b240aabf-e5c1-356b-8689-33b3a36738ff | -3.7448 | -45.507702 | 2024-10-10 00:21:18 | METOP-C | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f75236a9-7684-38e2-b156-0109de9a1f49 | -4.2385 | -47.712101 | 2024-10-10 00:21:18 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79bd5c5f-cc2f-3a7f-a4bc-b01c24eaf6ba | -3.7311 | -45.492901 | 2024-10-10 00:21:18 | METOP-C | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4ac28460-4876-3285-90c2-646daa4a044f | -3.733 | -45.5014 | 2024-10-10 00:21:18 | METOP-C | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3a1177de-c498-30c9-8936-760f02324915 | -3.735 | -45.509899 | 2024-10-10 00:21:18 | METOP-C | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 55a418b3-5ee2-3f5c-8ada-665d5afaec7b | -3.7369 | -45.518398 | 2024-10-10 00:21:18 | METOP-C | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 56e55b4e-0ae3-396f-bad6-8ca03c9b0900 | -3.6259 | -45.072399 | 2024-10-10 00:21:18 | METOP-C | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 792c0818-7721-3a5d-9b3a-7f860020f081 | -3.6277 | -45.080502 | 2024-10-10 00:21:18 | METOP-C | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 99c3bfd9-d34b-3a30-ab9e-434576382892 | -3.2308 | -43.514198 | 2024-10-10 00:21:19 | METOP-C | BELÁGUA | MARANHÃO | Brasil | 2101731 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bdbda3c8-cc60-314d-9fbb-3edb551d5fc5 | -3.2325 | -43.521198 | 2024-10-10 00:21:19 | METOP-C | BELÁGUA | MARANHÃO | Brasil | 2101731 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 051df505-7a11-3fe6-be48-45b1c4565c1a | -4.7992 | -50.5345 | 2024-10-10 00:21:19 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d4cb913-0912-3244-8fae-c718a36bbd11 | -4.8033 | -50.5532 | 2024-10-10 00:21:19 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d7c44f6-3a5c-386d-9655-52caf1ead392 | -3.3941 | -44.2771 | 2024-10-10 00:21:19 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 54a7a41b-a05e-3c20-9dfa-3067a69a0e9f | -3.3958 | -44.284599 | 2024-10-10 00:21:19 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 91a915cd-cd2f-33d1-ab87-2ffba05d48e2 | -4.7895 | -50.536499 | 2024-10-10 00:21:19 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11baa2b7-7e21-30fb-becd-8da4a88df630 | -3.3843 | -44.279301 | 2024-10-10 00:21:19 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cd6930b7-6101-3103-81bc-8cce2a396cb1 | -3.386 | -44.2868 | 2024-10-10 00:21:19 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 61f33004-1300-3670-88d6-fb10fae8f74f | -3.3877 | -44.294201 | 2024-10-10 00:21:19 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9cbcadea-89cf-3f8b-9407-bd30696bcc34 | -3.8662 | -46.459 | 2024-10-10 00:21:19 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e6573b7b-7d29-3fef-b64c-f181bcaf7dd7 | -3.8684 | -46.4687 | 2024-10-10 00:21:19 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ff6c3a2a-eb09-3805-bae6-aea6906a4564 | -3.8543 | -46.451599 | 2024-10-10 00:21:19 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 99e50b38-aa57-3a56-a362-7cc1de8cb792 | -3.8564 | -46.461201 | 2024-10-10 00:21:19 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f002dad9-fd0e-3bee-add3-7b69fc1b607e | -3.8586 | -46.470901 | 2024-10-10 00:21:19 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 075e3ba6-dab1-3c32-9bb7-87b08f1a12b2 | -3.8423 | -46.444 | 2024-10-10 00:21:19 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 80ff0675-2924-360f-a272-4c013e9f5c31 | -3.8445 | -46.453701 | 2024-10-10 00:21:19 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3e2b000b-56f6-377a-afe9-98351c2bed63 | -3.8348 | -46.455799 | 2024-10-10 00:21:20 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e28d290d-cd12-3215-ab72-1dc0823acb69 | -3.8369 | -46.465401 | 2024-10-10 00:21:20 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dd28cc8a-e531-39e7-9827-53d88c65f07d | -3.825 | -46.458 | 2024-10-10 00:21:20 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e70b6108-2b50-3124-8d9e-57685272c089 | -3.8271 | -46.467602 | 2024-10-10 00:21:20 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e5ef4110-0c1d-31c2-b38c-307850dd385e | -4.752 | -50.783699 | 2024-10-10 00:21:20 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c874d4ee-4dd4-3542-a372-e4020601233d | -4.7423 | -50.785702 | 2024-10-10 00:21:20 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccb19e3c-649d-36e9-8fac-b34389f70714 | -3.4256 | -44.915001 | 2024-10-10 00:21:21 | METOP-C | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c5d98244-cbdb-313f-996b-ed3bfa8d1a5f | -4.0441 | -48.264702 | 2024-10-10 00:21:23 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 774ac16e-b71e-3532-abf8-112f6d005ba8 | -4.0315 | -48.2542 | 2024-10-10 00:21:23 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 151d8f18-cfe7-3f11-b17f-4d727623a0e6 | -4.0344 | -48.266899 | 2024-10-10 00:21:23 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f22b098-6fe1-356d-9a6a-4592b95814df | -4.0372 | -48.279499 | 2024-10-10 00:21:23 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ab21ced-784e-3baf-87a0-49801b79828d | -4.019 | -48.243698 | 2024-10-10 00:21:23 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7db5b6c4-50de-39c1-97c5-8b302513e7be | -4.0218 | -48.256302 | 2024-10-10 00:21:23 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 068ca96c-e39d-38a3-a7a7-5de096a4afa4 | -4.0246 | -48.269001 | 2024-10-10 00:21:23 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0b6e3a9-db0d-330f-b67b-9e19043da993 | -4.0274 | -48.281601 | 2024-10-10 00:21:23 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README14.md)
