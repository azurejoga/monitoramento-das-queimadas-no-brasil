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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67b48268-c2c1-37c5-8d0e-55231fd0d98f | -7.10035 | -44.46638 | 2024-10-03 03:34:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4fdced0a-865b-3c4e-8e6a-770220e6d40c | -7.09448 | -44.46511 | 2024-10-03 03:34:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 753fb3e5-7234-3f16-9ac2-becca0a6135d | -7.00037 | -45.50101 | 2024-10-03 03:34:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ff7ae60e-6398-37dc-aa72-57b121401c68 | -6.99503 | -45.49459 | 2024-10-03 03:34:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 99af3bf6-afc9-3be2-aa6d-83b9014a717f | -6.99409 | -45.49968 | 2024-10-03 03:34:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fb4b143f-7340-38a0-9f94-f15599301e14 | -6.94757 | -47.67128 | 2024-10-03 03:34:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88633b64-5b1e-31e6-ac33-f35f9aa73025 | -6.94613 | -47.67867 | 2024-10-03 03:34:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 79d8b9ea-4090-311b-bbd4-7255091d254b | -6.94366 | -47.67693 | 2024-10-03 03:34:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 33e52717-8c5c-3742-9c24-134955b257db | -6.88725 | -44.28784 | 2024-10-03 03:34:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bcb0ea37-3f7c-3755-949e-6fa5fac46c14 | -6.88651 | -44.29188 | 2024-10-03 03:34:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e0654cd-4098-3f03-a6cf-73109cb32872 | -6.88578 | -44.29591 | 2024-10-03 03:34:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21f1a849-34e4-3006-a044-6d689fea6e82 | -6.88061 | -44.29105 | 2024-10-03 03:34:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c947d28d-a11f-39ae-ac2d-07222bc40c3e | -6.67742 | -44.53181 | 2024-10-03 03:34:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f5aaac3d-217f-3e39-bce8-a08852f77865 | -6.67491 | -44.66037 | 2024-10-03 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a12bcdb6-4a8e-38dd-aedf-16d96c15bb2c | -6.67422 | -44.53011 | 2024-10-03 03:34:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 41535315-abeb-3ff6-b79b-47dce8edecc7 | -6.67406 | -44.66501 | 2024-10-03 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08bf424d-4dc5-3f4b-bc57-720485b8d712 | -6.67335 | -44.53478 | 2024-10-03 03:34:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0cff1b6e-065a-31f8-a328-6e62969b6930 | -6.67144 | -44.53077 | 2024-10-03 03:34:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d3c8ec4-6441-37de-bd8c-2bc31e2c9f23 | -6.6706 | -44.53546 | 2024-10-03 03:34:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04bb1e2c-566d-3b6a-a351-c4be04959693 | -6.66031 | -45.33579 | 2024-10-03 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 16013a3b-7a60-3f89-b508-ca097db6416b | -6.65938 | -45.34098 | 2024-10-03 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 083a7f08-51d5-3caa-9266-6b3cef080e68 | -6.65744 | -45.3338 | 2024-10-03 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 39d44f01-dd70-30e8-b493-2ed67fba8bd1 | -6.65648 | -45.33899 | 2024-10-03 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 6c389fd1-db53-38d1-8138-5a6131a1fc2f | -6.65504 | -45.32898 | 2024-10-03 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 12189dff-697f-3e92-99e6-f840417800ae | -6.65413 | -45.33409 | 2024-10-03 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| e5d3b068-ce40-3936-846c-a6b9869747cf | -6.6532 | -45.3393 | 2024-10-03 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| c0da0fd8-6e9f-3fbe-a7ec-dd29aab8adb5 | -6.65123 | -45.33232 | 2024-10-03 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2e1abd9c-fdf3-368a-bb42-131a08957adb | -6.64882 | -45.32753 | 2024-10-03 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96b0b3e7-f6e6-32d8-a6a6-b7d813d28d20 | -6.64595 | -45.32581 | 2024-10-03 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 157d2c01-edb4-3200-82c1-315e38d6cb36 | -6.645 | -45.33092 | 2024-10-03 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0af0c189-d276-39da-99cf-72fa7a38ae01 | -6.64258 | -45.32617 | 2024-10-03 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1bbe0063-2e9d-3ef5-905f-ff143f833466 | -6.64166 | -45.3313 | 2024-10-03 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79cded32-2095-3fc2-ac75-b22bea4ec802 | -6.63875 | -45.32961 | 2024-10-03 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89f2b8bf-15c3-33ec-a5ac-b1ce77089e02 | -6.58116 | -44.23102 | 2024-10-03 03:34:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98beaf72-018b-3ecc-94ce-87e5b363d1dc | -6.58037 | -44.2354 | 2024-10-03 03:34:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7e1cdeb-faf3-339b-bd71-136499827de2 | -6.57538 | -44.22943 | 2024-10-03 03:34:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2968e39-1a93-3c02-82aa-1cf97cde6a69 | -6.57458 | -44.23386 | 2024-10-03 03:34:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16715742-605b-31ff-8b24-0216b01d4fd8 | -6.54818 | -44.0831 | 2024-10-03 03:34:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39c5399e-bd7b-39f6-8406-6f97164b2cf6 | -6.5478 | -44.08258 | 2024-10-03 03:34:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d3f2ee7d-b1fd-3b52-9c77-8019afe0a18a | -6.54753 | -44.08679 | 2024-10-03 03:34:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| caefa719-f078-3b95-8305-822feb57dbed | -6.54713 | -44.08624 | 2024-10-03 03:34:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a6c46b8b-2838-369b-bfec-e22919b226bb | -6.35553 | -46.51495 | 2024-10-03 03:34:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f826185d-749e-3336-a2d9-defaeb8bf329 | -6.15075 | -44.13259 | 2024-10-03 03:34:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d1ee92d8-b47c-3be1-b764-25f3f65d0206 | -6.14409 | -44.1359 | 2024-10-03 03:34:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01d4fac3-9658-3bfa-88c1-ccdfc2f54e7a | -6.13739 | -44.13937 | 2024-10-03 03:34:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 992074a4-8484-3ba3-9e68-52e4ab10d42c | -6.12399 | -47.2707 | 2024-10-03 03:34:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ef6205b-7ab6-3b68-b6a1-d79664624e70 | -6.12332 | -44.05025 | 2024-10-03 03:34:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4addf56-4775-3cf9-b23f-9b8bc2684166 | -6.12269 | -47.27766 | 2024-10-03 03:34:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fdd095b1-900e-3708-879f-b35bca49ab99 | -6.1191 | -44.04572 | 2024-10-03 03:34:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6fd654e-2c0f-33fd-bd00-d202ede7c84c | -6.1184 | -44.04972 | 2024-10-03 03:34:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d7836453-c553-3d14-8631-9c4c482ff64b | -6.11824 | -44.9411 | 2024-10-03 03:34:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 626523d2-8047-3a63-b2a6-a0287365b0f5 | -6.11747 | -44.04923 | 2024-10-03 03:34:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da2589a5-97bb-3884-8e84-2168ae5ff676 | -6.11737 | -44.94588 | 2024-10-03 03:34:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e887ba0f-fe41-3d5b-96cc-662bdd840492 | -6.11253 | -44.04875 | 2024-10-03 03:34:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 320e89cb-a061-31eb-8d33-7674174014d8 | -6.11203 | -44.94016 | 2024-10-03 03:34:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 09e17edf-576e-3cef-be77-d891d2b9fa2b | -6.11186 | -44.05258 | 2024-10-03 03:34:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0368b827-8578-35a9-b07c-4fd099d765cc | -6.10601 | -44.05154 | 2024-10-03 03:34:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1878a85b-40b1-3fc6-aba0-54e947260366 | -6.10533 | -44.05538 | 2024-10-03 03:34:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e10c260-93d0-3b21-855d-87df7fe2a01b | -6.0886 | -44.04761 | 2024-10-03 03:34:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52e9b0b9-c30c-3fd3-bd0e-96fbb29cffc4 | -6.08794 | -44.0513 | 2024-10-03 03:34:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01407774-cc8a-3e17-9fab-bbbbc3336933 | -6.04578 | -44.15191 | 2024-10-03 03:34:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1cafa1dd-1903-3deb-9938-fb88b7a67ec8 | -6.04501 | -44.15619 | 2024-10-03 03:34:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86bf809a-e115-3f31-98b4-266d596eb272 | -6.01657 | -44.55803 | 2024-10-03 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95f6095b-6ff7-3375-84cf-837df0c0e57d | -6.01578 | -44.56249 | 2024-10-03 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a5ba04a-cb02-32bc-b0fd-7f033f698913 | -6.00971 | -44.5615 | 2024-10-03 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0f282270-c6ce-347a-9f54-6bb35157fe74 | -6.00888 | -44.5662 | 2024-10-03 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f7c884e8-3351-36bb-bc91-3dfc24b5eed4 | -5.96668 | -44.13 | 2024-10-03 03:34:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 26cdea46-caf3-3c06-bb28-295ef0cf18bd | -5.851 | -44.60466 | 2024-10-03 03:34:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 97906230-5082-3d4a-96e4-82bcf673286f | -5.85016 | -44.60933 | 2024-10-03 03:34:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b8ec103d-91f2-3819-abf3-e3f42004467f | -5.84655 | -46.23991 | 2024-10-03 03:34:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a9bae0d5-88ac-315e-b70f-62744171cf92 | -5.84412 | -46.23891 | 2024-10-03 03:34:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d0c376b9-99d8-3bc6-8883-a7049974e6ca | -5.35311 | -46.7224 | 2024-10-03 03:34:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3a5f135c-0938-363f-b963-e4da7afd4eb6 | -5.35188 | -46.7294 | 2024-10-03 03:34:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3dcd36eb-ce66-3969-a408-5935bd5313c7 | -5.35187 | -46.72168 | 2024-10-03 03:34:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6525f041-0fcf-3c77-98a2-60c67eb74383 | -5.35059 | -46.72865 | 2024-10-03 03:34:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 902a342f-0df8-33ce-a956-26709fa2076c | -5.08403 | -46.11995 | 2024-10-03 03:34:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 90bd009b-84da-3687-a4cd-c39f5ec76469 | -5.08286 | -46.1265 | 2024-10-03 03:34:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9f93cc59-70ce-3474-bfc8-b287c3c8f3e1 | -4.67805 | -45.88748 | 2024-10-03 03:34:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 98c3eab4-c081-3c64-a285-eed134e4cf1b | -4.6769 | -45.89395 | 2024-10-03 03:34:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 450182eb-1ff6-324f-b650-ffcce2f92b47 | -4.67132 | -45.88647 | 2024-10-03 03:34:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 90c652b4-c45e-33cb-8fa6-4d3053c2321c | -4.6702 | -45.89281 | 2024-10-03 03:34:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 00a5a1b8-fd77-3419-b0ca-eedd9de8b641 | -4.47105 | -45.93014 | 2024-10-03 03:34:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 167ed7b3-5c69-3005-bbca-e715b88a26cf | -4.46996 | -45.93634 | 2024-10-03 03:34:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c47d7254-29e3-37c4-bb18-78413362ecdf | -3.60836 | -44.7913 | 2024-10-03 03:34:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7cee84b-b731-3859-94df-233f20ffe114 | -3.60748 | -44.79647 | 2024-10-03 03:34:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa4da9de-b95a-3b54-8350-4ec548e47147 | -4.5391 | -43.31305 | 2024-10-03 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| fa02a5ef-470c-3610-bc5f-607cd6a0dcc9 | -4.93581 | -43.7824 | 2024-10-03 03:34:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 437e1b16-d9fa-3513-8c79-52498d7d2ebe | -4.92999 | -43.78113 | 2024-10-03 03:34:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| c202edb1-04b5-3968-867d-f652d0f6288a | -4.92922 | -43.78553 | 2024-10-03 03:34:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| cca61ef0-9ee4-3530-82d2-e667f2d5502b | -4.92489 | -43.77579 | 2024-10-03 03:34:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| bae434e4-f6ec-3523-93a3-80fa91a4ba12 | -4.92413 | -43.78012 | 2024-10-03 03:34:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| a0285cbd-8119-3477-9199-b61e765dffc7 | -4.92335 | -43.78453 | 2024-10-03 03:34:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 969ef6f8-1112-3d1f-aba4-f7871454f114 | -4.86768 | -38.43509 | 2024-10-03 03:34:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2b7a7826-aeda-3d65-9778-7e01b56840d7 | -4.6636 | -43.76451 | 2024-10-03 03:34:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9527c737-3070-3f51-ad42-250bd1d8ca60 | -4.65985 | -43.76015 | 2024-10-03 03:34:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b881afdf-af77-38fc-9007-267f13fda76f | -4.65912 | -43.76441 | 2024-10-03 03:34:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bef04b25-7b00-3dd5-8e87-6ed2ec2eef7e | -4.56189 | -38.84106 | 2024-10-03 03:34:00 | NOAA-20 | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 47dac94a-ff16-302c-a7ce-7271dd1ba7e4 | -4.54481 | -43.3141 | 2024-10-03 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 99c30685-af11-3ac2-a52a-038f22bc6226 | -4.54126 | -43.30912 | 2024-10-03 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| a71065d5-2493-3d89-96bf-fe82cac9d14d | -4.54055 | -43.31311 | 2024-10-03 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |


[Clique aqui para ver as próximas entradas](README63.md)
