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
| c080ca7a-897e-39f7-b7c3-65aa40dc8c4a | -5.36791 | -42.79975 | 2025-10-20 04:12:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2a3f9b5d-718c-3632-81bd-e8bcbf77f3c4 | -7.06373 | -45.52382 | 2025-10-20 04:12:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39b6d690-7396-31ae-a0c7-c5b2992e4cf7 | -2.24955 | -51.91717 | 2025-10-20 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| a4eeaecb-470b-30a3-86b7-ada07a77e073 | -2.65623 | -49.37507 | 2025-10-20 04:12:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1325c131-d04b-3c35-a99a-6d11f0c5b707 | -7.14259 | -44.90361 | 2025-10-20 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2908dd6d-3cb1-3478-820a-038e27659525 | -7.65111 | -46.86077 | 2025-10-20 04:12:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3148f3a8-33d0-3f33-b05c-7fe4b592e5ca | -2.24453 | -51.91245 | 2025-10-20 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 6f2c54e3-90ad-3023-8b35-32e154d5ac3d | -5.08761 | -42.95997 | 2025-10-20 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2bac8431-a541-3367-9e0b-998082a4fa2b | -6.54659 | -41.67091 | 2025-10-20 04:12:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 04fdb7bc-dd25-3740-a1af-7ccbeaa5ef5b | -5.28801 | -41.20289 | 2025-10-20 04:12:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 42a6c46e-5f3d-3d8a-bf3a-bb26c0d2dcb6 | -6.49473 | -43.17333 | 2025-10-20 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 66c284af-6f01-3249-9cfc-ebdab11c6d5f | -6.71601 | -47.39165 | 2025-10-20 04:12:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66942247-0531-3c93-9a37-d4bd78c4ea73 | -3.09456 | -51.29406 | 2025-10-20 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e2f8c51-e066-3b28-8383-9466f8193907 | -5.62828 | -43.64425 | 2025-10-20 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c27c7a41-1e58-3042-a036-8ec0720c5cc8 | -6.5516 | -41.66079 | 2025-10-20 04:12:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b68f9d7f-61df-384a-9065-4d3477464976 | -5.53512 | -44.60439 | 2025-10-20 04:12:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f2f42f0-bbe7-3274-9253-da89014af23d | -4.11108 | -42.27983 | 2025-10-20 04:12:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b5e2cc0e-2ac5-344f-a1a6-d82fba6ce5f7 | -1.44264 | -48.8894 | 2025-10-20 04:12:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e88e5e50-17f0-3709-9beb-35f16d793cc4 | -4.1827 | -42.1924 | 2025-10-20 04:12:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 94b3bd4f-da72-3f1a-a136-de3ac5fbcf2f | -4.83098 | -45.80035 | 2025-10-20 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7e043262-d198-3612-be34-8cb9eaff3bb2 | -6.96348 | -46.97891 | 2025-10-20 04:12:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 490e1033-67fc-33b2-b288-1623c6c1945c | -4.86133 | -45.11433 | 2025-10-20 04:12:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9e2c246-77fd-3c4f-8a26-020fedb22517 | -1.44092 | -48.89182 | 2025-10-20 04:12:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98d0b724-f5e8-3dcc-9e48-c00ccf8de7f7 | -6.46723 | -43.73127 | 2025-10-20 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ca6d6c48-a44b-34e9-af97-336088a475e9 | -7.1101 | -46.48553 | 2025-10-20 04:12:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c72c6637-6e28-32e3-8908-5c486ff7db14 | -6.87657 | -43.59299 | 2025-10-20 04:12:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86e3796f-cca5-3636-b00b-cc346e3b183e | -5.16262 | -44.54283 | 2025-10-20 04:12:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3943a07a-0228-3939-951a-07f714708bb7 | -5.91612 | -45.4086 | 2025-10-20 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c35c3de-e9d3-333c-826d-3866dd87899d | -7.13931 | -44.2465 | 2025-10-20 04:12:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b084f9b-ca2b-349f-8336-de486e257f5a | -4.88754 | -42.93571 | 2025-10-20 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d31acbc8-ece1-31a5-a5ba-ccec839bfc10 | -4.88826 | -42.95354 | 2025-10-20 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 017f9108-fde6-33c6-9c6d-8b948649b7e7 | -4.46075 | -43.75988 | 2025-10-20 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32cc6529-dbfb-3429-b724-fa3f4743f436 | -4.39885 | -43.31656 | 2025-10-20 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b2fc4c6f-1955-3de1-aa89-46fd402f6911 | -5.36338 | -45.50665 | 2025-10-20 04:12:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 788a8541-5221-3ddd-8cf6-cbd92bcd2759 | -4.82883 | -42.74984 | 2025-10-20 04:12:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 9c98f80e-8617-38c7-b082-95420d537d2f | -6.20735 | -41.5346 | 2025-10-20 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| eb124f48-6734-39af-971b-cbb7cf12a63e | -5.4543 | -43.73153 | 2025-10-20 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63267928-222b-3f1b-8292-75e9db772dd3 | -7.02308 | -48.61354 | 2025-10-20 04:12:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0da9ce19-7c0c-37f8-b65e-413ad9720ea5 | -2.65767 | -49.37777 | 2025-10-20 04:12:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f34e1dcb-f2fc-33da-88bf-280ee3175eb5 | -2.24894 | -51.92096 | 2025-10-20 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 34c9e93f-e699-3cc2-a2bf-f16cf3a9614a | -6.21449 | -40.96304 | 2025-10-20 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 01a6ee31-ce16-37eb-94be-538bda1a0344 | -5.16293 | -45.99619 | 2025-10-20 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d13c49b6-b7fe-39a3-95bc-32984d73ce27 | -7.07184 | -45.21042 | 2025-10-20 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f49c35dd-63ce-3505-83b5-9538eff4d63e | -4.38966 | -45.79609 | 2025-10-20 04:12:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d064d736-83d8-3f48-ac29-53d651eb5e43 | -5.54241 | -41.34135 | 2025-10-20 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 47f6f18d-3a35-399e-add6-16fafa7af2e0 | -6.09473 | -44.02145 | 2025-10-20 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50f23b50-96af-3540-a633-d3b51f8974d9 | -5.62106 | -43.6467 | 2025-10-20 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2509f653-051f-3230-a5dc-9c9fed75c129 | -5.65203 | -46.81283 | 2025-10-20 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35ad7b91-053c-3914-b4e9-cb0757bae9fe | -4.8408 | -43.01686 | 2025-10-20 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3475d30d-e9ba-3c82-8af4-b5977782c353 | -4.68237 | -46.07105 | 2025-10-20 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a110e03-cfe1-365e-8ec9-5d31e25ca76a | -7.21311 | -45.41624 | 2025-10-20 04:12:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca6d9b15-e72c-35e5-bd7b-958de35e77b7 | -4.95555 | -45.09298 | 2025-10-20 04:12:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 00d56458-e46c-36db-a4b1-a5152ab88ced | -7.9988 | -39.62332 | 2025-10-20 04:12:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7e798c3a-2017-378d-9158-eb88dfc04b8e | -7.41591 | -40.07269 | 2025-10-20 04:12:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 54b13aa1-086e-3563-828c-0945caad0ac4 | -4.89611 | -45.53254 | 2025-10-20 04:12:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 982f00c3-1233-3145-85dc-35dc9a03a40f | -2.24666 | -51.92048 | 2025-10-20 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| cf67c70d-24db-322d-9d56-8f43a76f3320 | -5.77795 | -42.71962 | 2025-10-20 04:12:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9c6451cd-2293-3410-aa04-9fbc1a3620d9 | -5.62772 | -43.64776 | 2025-10-20 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f08ed5a-a435-3860-9898-390132b5222d | -7.30261 | -39.27032 | 2025-10-20 04:12:00 | NOAA-20 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 968bcde2-d082-3c91-8274-21f54cdb90c2 | -6.31137 | -40.90128 | 2025-10-20 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6e467e3a-c02e-3e76-bcdd-ccacfd08f034 | -5.08598 | -45.89362 | 2025-10-20 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75dbe72c-3769-3d45-a25f-13347e5503b8 | -7.13596 | -44.24597 | 2025-10-20 04:12:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c86e714-f958-3cf2-b039-6a38cdcb672e | -2.44625 | -49.01138 | 2025-10-20 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04576889-b270-3327-b51a-1cd03cbb8da8 | -7.53951 | -46.09391 | 2025-10-20 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a5c84ee-90e6-3d9e-b946-4dd97750e31c | -7.06689 | -46.1976 | 2025-10-20 04:12:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 071c0caf-13a4-3fe0-a28e-4db0d2161822 | -4.86071 | -45.11825 | 2025-10-20 04:12:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1259c87b-d004-3004-94b6-e1c2de53bc9d | -6.39721 | -38.28048 | 2025-10-20 04:12:00 | NOAA-20 | PARANÁ | RIO GRANDE DO NORTE | Brasil | 2408607 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a143b2e0-c554-39fb-970d-d74ca45dbedc | -8.00115 | -39.63274 | 2025-10-20 04:12:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a0d71f35-76ea-34e9-bb31-32df14cf114d | -5.54185 | -41.34492 | 2025-10-20 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| be6a9b61-394b-35f3-9a0d-8d6922a551c8 | -5.11112 | -43.19767 | 2025-10-20 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d2c619fb-1c6a-36fe-8e96-8747a5d8b407 | -3.58409 | -41.65655 | 2025-10-20 04:12:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a1792dda-bd19-320c-8e45-7f4aa62ef76c | -5.91262 | -45.408 | 2025-10-20 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a1b014ac-21a9-3607-89f1-015a40bdb6d5 | -2.43455 | -48.61657 | 2025-10-20 04:12:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0eba1a84-cf2a-3205-b7ee-fb8de433a50d | -7.21246 | -45.42014 | 2025-10-20 04:12:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a5106ed-091e-3173-8e7b-3c5247a856a8 | -3.4869 | -46.00657 | 2025-10-20 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4cd75cde-0caf-3770-83e7-0314b8072ecd | -6.21563 | -40.97835 | 2025-10-20 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 9d6398d7-7d5f-3f95-8957-c9f38b8c30c3 | -5.4504 | -43.73453 | 2025-10-20 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 774bf823-e019-3fcf-b039-66c25bda2704 | -6.55585 | -47.11929 | 2025-10-20 04:12:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63862d03-fda2-3eb4-9954-0a8924ceb4de | -7.23996 | -44.21191 | 2025-10-20 04:12:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6f19364-a4d0-3deb-b0c6-11a83b68f0ba | -5.16462 | -43.13863 | 2025-10-20 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ead1db7a-a1d9-3834-b4c3-8602ce914568 | -5.3756 | -43.15816 | 2025-10-20 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2c3cbe78-0900-3eaa-93d3-fad9439905ec | -3.32749 | -50.74547 | 2025-10-20 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8489a200-a32b-3b50-8e45-d2ac1d08df98 | -5.48914 | -44.19342 | 2025-10-20 04:12:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5ab20f5-e3d3-3ea9-b5e7-c8a16a7e2c09 | -6.20824 | -40.98098 | 2025-10-20 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 89e86cda-8e44-3def-92bb-baa54908d59c | -4.86607 | -44.44639 | 2025-10-20 04:12:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d64ed60-f685-368f-b217-c287f7983cb8 | -5.28745 | -41.20648 | 2025-10-20 04:12:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 47b37bc4-5fff-3e00-8837-29a43f7d5630 | -2.2473 | -51.91671 | 2025-10-20 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 0adcad6e-1647-3d08-91c0-94225ef48b75 | -4.82937 | -42.7464 | 2025-10-20 04:12:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 00a6e319-4aba-3a81-a7e7-b205e6df2aff | -6.09808 | -44.02201 | 2025-10-20 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47415934-4123-31a7-a796-71d4fb5f5d38 | -5.5845 | -45.75283 | 2025-10-20 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f32263e-27da-306d-bb74-5b0ec47fe4cb | -5.53571 | -44.60069 | 2025-10-20 04:12:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b11c7f1c-e1ec-3e00-8373-562443f2adaa | -3.32698 | -50.74852 | 2025-10-20 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| baacf3ea-b9ea-32d5-8e7b-e719f799ffb8 | -6.14743 | -44.28642 | 2025-10-20 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8db576aa-0aef-3483-ba1f-88a9307ab5d2 | -4.84817 | -44.59978 | 2025-10-20 04:12:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e55e03fb-3003-353e-b103-39b0e22df86e | -7.01485 | -35.22556 | 2025-10-20 04:12:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 1fb6817f-a289-306e-8899-511e81c1f7be | -4.39496 | -43.31952 | 2025-10-20 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1684ef70-e292-30e3-a22e-5b277d128469 | -7.20696 | -45.41968 | 2025-10-20 04:12:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4067929c-be3e-3558-91c9-b7f2b2108708 | -7.69031 | -47.36584 | 2025-10-20 04:12:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd7c82e3-5579-3c99-b04a-d51c4cecd2b1 | -4.88792 | -43.40507 | 2025-10-20 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dbee538b-e1cc-38ae-8fad-7456e98b5724 | -2.93398 | -39.86657 | 2025-10-20 04:12:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |


[Clique aqui para ver as próximas entradas](README12.md)
