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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95f66d7a-91b1-3abe-ad25-bbbc0c32ccbe | -11.9978 | -47.1045 | 2025-09-28 12:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 9bc03300-1451-39ea-bb47-c8c0f8087518 | -7.3659 | -47.0394 | 2025-09-28 12:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 137.2 |
| a32327ab-34f6-32ad-b629-0c7fa8b3b3f2 | -11.3892 | -46.9622 | 2025-09-28 12:00:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| abbdaf8f-927a-396c-becf-8469410849da | -11.3889 | -46.9847 | 2025-09-28 12:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| d6a1448d-5168-34bc-a6ba-680223a9bee8 | -12.0214 | -47.9703 | 2025-09-28 12:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 69a362c1-0644-3588-9d87-a2e603b2faf2 | -14.3816 | -54.9266 | 2025-09-28 12:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 14712a91-a80f-3a89-9530-0a2984aba545 | -14.3813 | -54.9472 | 2025-09-28 12:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 162.6 |
| a4f14efe-ae23-3a0a-95f8-d5696336ed06 | -14.766 | -45.6621 | 2025-09-28 12:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 1ab790f8-cac1-3ccd-a9b9-7a9956d34607 | -11.9794 | -47.0622 | 2025-09-28 12:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 4e9afe4c-1529-3f63-95dd-05bd5f7acf68 | -12.0019 | -47.995 | 2025-09-28 12:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 7593ece7-9de3-3b1a-b0ef-10579412fcb4 | -11.9982 | -47.0821 | 2025-09-28 12:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| de7c6e9c-3631-324a-835f-84e4c1219dd0 | -11.979 | -47.0847 | 2025-09-28 12:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 168.1 |
| 0c8a1bc9-5828-3cc1-8ad6-1b137fff6396 | -14.7655 | -45.6854 | 2025-09-28 12:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 27c0fab2-5cbf-380e-a0a0-b92513721b02 | -7.3847 | -47.0378 | 2025-09-28 12:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 314.4 |
| d1c5d3f4-4f4d-3b06-a62d-c1febeb750b3 | -12.2825 | -44.0804 | 2025-09-28 12:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 127d075a-6b42-32d1-907c-0120cc6cbdaf | -7.8823 | -44.5594 | 2025-09-28 12:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 3800a9c6-1a0f-3db2-96e8-0d740150d469 | -11.9824 | -48.0197 | 2025-09-28 12:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| a64c4141-7158-3566-8c10-305691034a84 | -7.7782 | -47.0479 | 2025-09-28 12:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 284.3 |
| 1eb41ff6-2dba-39b5-8342-acfa5d41ef87 | -7.3659 | -47.0394 | 2025-09-28 12:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 1e44103d-201c-374b-9c0d-0dd708ec8fbe | -12.0214 | -47.9703 | 2025-09-28 12:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 4453d691-c57f-3799-8f18-bfa70a6a9fa0 | -7.3661 | -47.0173 | 2025-09-28 12:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 71dffc7a-0735-351c-872f-09c91d0808fa | -12.9547 | -45.1618 | 2025-09-28 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| febb41a8-f325-322a-924a-c763324422fa | -7.7785 | -47.0258 | 2025-09-28 12:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 225.6 |
| 7febda24-598b-3816-a10f-96d3e6e4c6eb | -13.6122 | -48.0787 | 2025-09-28 12:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 78.5 |
| d52b182b-a938-3ae1-9087-6b583b2beb08 | -12.791 | -47.7533 | 2025-09-28 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 9b082447-1085-3c97-b1b6-584575ba9e59 | -7.7972 | -47.0241 | 2025-09-28 12:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 39224418-0316-313b-b763-d0d2d07eb408 | -14.3813 | -54.9472 | 2025-09-28 12:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 01dbf11c-cdb2-3132-8c79-2fd19a0dd2cc | -11.3889 | -46.9847 | 2025-09-28 12:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 03c9bbab-cddd-33d8-8b59-cf27c341a898 | -11.7002 | -44.4283 | 2025-09-28 12:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| b90dbcfd-c3c5-3a2a-894d-28021f188dcc | -12.2829 | -44.0568 | 2025-09-28 12:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 803265cc-503e-301c-80e8-68a29e98fdbe | -11.9982 | -47.0821 | 2025-09-28 12:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 6be2d83d-ef05-3146-af35-7b7dacb90326 | -7.3849 | -47.0157 | 2025-09-28 12:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 155.6 |
| 68a44847-047e-3b2d-a45b-8328781d1099 | -12.2825 | -44.0804 | 2025-09-28 12:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 182.8 |
| 8107a2aa-fc06-31f4-b93c-211ce87b45e6 | -11.979 | -47.0847 | 2025-09-28 12:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 201.6 |
| ca42c73b-1df3-334e-b7ca-e63382d62f87 | -14.7655 | -45.6854 | 2025-09-28 12:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 86.6 |
| b6d0f254-61c9-3e0f-adfb-2d94018438bb | -11.4083 | -46.9597 | 2025-09-28 12:10:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 155.2 |
| 5c3d7321-ce97-327c-ae93-ab339eb3f63f | -14.7851 | -45.6818 | 2025-09-28 12:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 46042743-e294-3b08-ae90-456f21999407 | -7.3847 | -47.0378 | 2025-09-28 12:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 295.0 |
| f708614c-f32b-388e-a251-5215dccd0efd | -10.4983 | -48.0487 | 2025-09-28 12:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 76f06a38-f2d5-3be8-b5c8-47301e557693 | -13.6073 | -47.3183 | 2025-09-28 12:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 6d705609-c31a-3ef3-be1e-5709581cb8f6 | -11.946 | -47.9138 | 2025-09-28 12:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 096b7705-0e87-31ca-907b-db872debecd4 | -7.3659 | -47.0394 | 2025-09-28 12:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 7fd0ff59-aa1f-3bc9-b307-be6b6c993652 | -11.979 | -47.0847 | 2025-09-28 12:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 161.8 |
| f64eb8df-d56b-31c7-b6f2-21645b2a3a24 | -10.4794 | -48.0508 | 2025-09-28 12:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 131.9 |
| b6c8d1ed-07dd-39d0-be5f-642a3df157a5 | -7.7972 | -47.0241 | 2025-09-28 12:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 111.9 |
| c496c4d2-51dc-3704-87f0-b73c88fbe39a | -13.7893 | -47.8957 | 2025-09-28 12:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 62.1 |
| a85bd8a8-741f-30a2-8d36-caa96734ae74 | -13.2773 | -50.7061 | 2025-09-28 12:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| d2cf4f13-f857-3e3b-870d-ec7d35c1cdd9 | -11.3889 | -46.9847 | 2025-09-28 12:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| dc401490-42d0-3453-b392-eaace6cfa84e | -12.0218 | -47.9481 | 2025-09-28 12:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 08751934-243c-3e0f-afc0-b049d5c50fba | -12.2825 | -44.0804 | 2025-09-28 12:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 107.5 |
| df12887f-58cb-37c9-a16a-01e0461ac2f0 | -7.7785 | -47.0258 | 2025-09-28 12:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 90de6255-0a46-3f2c-b30b-31ea523e5891 | -10.4797 | -48.0288 | 2025-09-28 12:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| cbddbf5a-3458-37aa-9723-81a52e4aa0b8 | -12.9547 | -45.1618 | 2025-09-28 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 727b2ea4-5d1a-3ad0-a208-c7faf3d8dc3a | -7.7782 | -47.0479 | 2025-09-28 12:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 119.9 |
| e6fd7c6b-8745-3bdc-a06c-f231beb2eae2 | -12.0214 | -47.9703 | 2025-09-28 12:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 08b8377e-2a0c-3151-8142-3c64a36f1fe1 | -7.3849 | -47.0157 | 2025-09-28 12:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 128.2 |
| e9ef38e8-a0a7-37db-81e6-7eb2c8303069 | -7.816 | -47.0224 | 2025-09-28 12:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| ef8bfbf1-f581-39bb-a402-81636dc8e54e | -11.3892 | -46.9622 | 2025-09-28 12:20:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| f5015a22-f170-340b-92c4-7fe27cb4e43a | -12.0019 | -47.995 | 2025-09-28 12:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 064a978a-8346-394c-8815-55c44b4f97b5 | -11.9824 | -48.0197 | 2025-09-28 12:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 6e09b4ec-339d-35ce-8016-a16dbe17f08d | -11.9794 | -47.0622 | 2025-09-28 12:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 0b7e9316-6caf-3dc4-9eab-f6bceee93843 | -11.4083 | -46.9597 | 2025-09-28 12:20:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 141.9 |
| f7985683-703f-390b-a379-b9f6be8119dc | -11.9828 | -47.9976 | 2025-09-28 12:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 007d50d9-b6d4-3cd2-829e-c3217f43d7d1 | -7.3847 | -47.0378 | 2025-09-28 12:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 291.1 |
| 4958ca6e-ee8d-3f53-8c85-1684bb21acea | -7.3661 | -47.0173 | 2025-09-28 12:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| aa7fbd9b-7718-3369-b8d5-f6d900e62e80 | -12.0218 | -47.9481 | 2025-09-28 12:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| cb7082a4-7a57-374f-a8e8-f865adeb68ff | -7.7604 | -46.961 | 2025-09-28 12:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 13ea92e8-15a3-3eda-bb61-c52197c3df55 | -12.0214 | -47.9703 | 2025-09-28 12:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 151.4 |
| c957cdbb-2735-35ff-8aad-c7a4b7913d40 | -11.9456 | -47.936 | 2025-09-28 12:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 24a9c003-1c8f-3164-b9c6-115d3381b550 | -11.681 | -44.4312 | 2025-09-28 12:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| a6145636-00da-350c-b1eb-711d8cb627cf | -7.7414 | -46.9848 | 2025-09-28 12:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| af1e7147-ba3d-3292-8564-ca3539b1361c | -7.7785 | -47.0258 | 2025-09-28 12:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 233.5 |
| 61b1df35-bcfe-3949-ae3b-2deb5fc9a634 | -13.6267 | -47.3152 | 2025-09-28 12:30:00 | GOES-19 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 59.6 |
| c3de6c6c-7ff8-35e4-8ea2-7a279787928f | -11.7002 | -44.4283 | 2025-09-28 12:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 3158a8f6-2c56-3b7f-a55b-75a327c48934 | -7.3659 | -47.0394 | 2025-09-28 12:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 6c2ea520-5c86-3186-9a68-6bc57921133e | -7.3847 | -47.0378 | 2025-09-28 12:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 233.7 |
| 350b3ec0-6d8f-3dd2-a1fd-2fd58a1163ef | -11.9982 | -47.0821 | 2025-09-28 12:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| e815c596-2850-3d47-9578-c63a375bd74a | -7.3849 | -47.0157 | 2025-09-28 12:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 145.4 |
| c51cacfd-7cdc-3566-9340-578e0231e8e4 | -7.7602 | -46.9831 | 2025-09-28 12:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| f5c973b9-0525-353a-9e28-cf23e4283a20 | -12.0019 | -47.995 | 2025-09-28 12:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 146883f3-6c18-31e4-a7f7-5829212d6230 | -11.979 | -47.0847 | 2025-09-28 12:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 202.2 |
| f36be2d7-4b5e-3fda-907a-fb8c07cd05d6 | -11.4083 | -46.9597 | 2025-09-28 12:30:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 57e53243-dc1c-377c-8783-17f63d1f6201 | -7.7782 | -47.0479 | 2025-09-28 12:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 294.5 |
| a5b79623-06e5-3850-a427-5f552a3859bd | -11.4413 | -44.9998 | 2025-09-28 12:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.5 |
| b5a08641-3388-3892-a335-09fd40f11db2 | -8.1611 | -46.4122 | 2025-09-28 12:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 01915641-3110-3776-a7ab-d03bdff7b2a6 | -12.9547 | -45.1618 | 2025-09-28 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 36f6d0e4-4d0b-360b-bc6d-d1090c08513f | -11.9986 | -47.0596 | 2025-09-28 12:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 0fd6799d-4d15-30db-9731-ea3fd2b14001 | -11.946 | -47.9138 | 2025-09-28 12:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| dffc3d64-fb04-3efb-be3a-11742263bc39 | -7.7972 | -47.0241 | 2025-09-28 12:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 183.9 |
| 5645d016-7909-38dd-87f2-53fafa3d0e95 | -13.6073 | -47.3183 | 2025-09-28 12:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 86.6 |
| dbe88ea7-6c0b-31b4-8332-41cdb4d81fe7 | -11.9824 | -48.0197 | 2025-09-28 12:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 56c34748-e942-3b82-9404-aff8c39d1a0f | -11.9978 | -47.1045 | 2025-09-28 12:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| a5b92996-18cd-3223-b9c4-36ebc591d417 | -7.3661 | -47.0173 | 2025-09-28 12:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 3f7d3a49-3618-376f-bc27-a182763181af | -7.816 | -47.0224 | 2025-09-28 12:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| e0dffee7-5d8a-3d93-9750-e4ff7aef9174 | -7.8823 | -44.5594 | 2025-09-28 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 821000ca-a37f-3502-9512-8145397a6aa3 | -11.9637 | -48.0001 | 2025-09-28 12:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 6b87e718-0506-312f-b592-1a37f5c81647 | -8.2668 | -45.4564 | 2025-09-28 12:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 58.5 |
| ee744506-f303-36a7-bdeb-0a1d78517c94 | -15.8873 | -46.2409 | 2025-09-28 12:40:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 103.7 |
| fc31604e-a931-3cfb-9ce6-178f160eb1c8 | -7.816 | -47.0224 | 2025-09-28 12:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 93958433-0de1-3d43-bcbd-5e0484234766 | -11.9824 | -48.0197 | 2025-09-28 12:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 142.4 |


[Clique aqui para ver as próximas entradas](README97.md)
