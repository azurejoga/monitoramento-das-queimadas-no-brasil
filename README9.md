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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9debccb-491f-33cd-b7ac-9da98d03d154 | -8.5226 | -46.0851 | 2025-11-17 01:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| d168c627-4999-3567-a5c6-bb3b24230a14 | -3.7652 | -47.7468 | 2025-11-17 01:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| c83a00cc-d464-30a3-8328-3c5ce4512ae3 | -5.0399 | -43.6205 | 2025-11-17 01:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 79d1e8c0-7cd8-3d2b-8a5e-c29d4bcefb01 | -3.2344 | -50.4952 | 2025-11-17 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| fa581a88-17b4-39dc-a223-66e01d9d2bf9 | -11.849 | -49.2 | 2025-11-17 01:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| a633c900-7498-390d-a12f-83dddaefe9cb | -8.5229 | -46.0626 | 2025-11-17 01:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| bc431f9b-c5cd-3cfa-aeff-bd749a951402 | -11.8486 | -49.2218 | 2025-11-17 01:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 9081dece-5608-3614-bae5-3f226c71b92c | -2.5238 | -47.8115 | 2025-11-17 01:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 191f03a1-5d7c-3ca7-9b42-c5f0b8652d71 | -11.7017 | -48.8692 | 2025-11-17 01:30:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| c81adf08-571e-3045-bd3d-a603e0736f65 | -3.7838 | -47.746 | 2025-11-17 01:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 19ee932c-5ce8-3efc-9705-05daa1adf207 | -11.8295 | -49.2242 | 2025-11-17 01:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 6d636f08-8890-3468-ba8b-99c7d7f32377 | -4.7209 | -46.3832 | 2025-11-17 01:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 36130c04-0b48-306b-b04e-7840cb2e6d7f | -5.0401 | -43.5973 | 2025-11-17 01:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| e3678d60-1aeb-3308-9972-8b2fd1787cbe | -3.776 | -49.2517 | 2025-11-17 01:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| fee9b80b-1927-31d6-9ac2-da15bd82928c | -10.6687 | -49.3813 | 2025-11-17 01:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 8686e5ce-4e37-36c8-888a-eb0a3d1386b5 | -2.5238 | -47.8332 | 2025-11-17 01:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 15096c72-578d-3bd9-803d-8bce5be13e2e | -6.6875 | -42.0296 | 2025-11-17 01:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 138.0 |
| 54176318-6b81-3811-a81c-2c63271243bd | -11.8987 | -46.1934 | 2025-11-17 01:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 4eb1c555-0e77-3fed-93ec-cf76ff1aab26 | -11.8991 | -46.1707 | 2025-11-17 01:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 515da73f-3928-3719-affc-776c28e92074 | -2.5053 | -47.8337 | 2025-11-17 01:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 60d3dd04-6584-3062-8214-e1678e70b73c | -3.2344 | -50.4952 | 2025-11-17 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 9d9510e5-3832-34e1-9e17-d5ab27897c14 | -10.6687 | -49.3813 | 2025-11-17 01:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| e3035461-446f-3e4f-a287-e34a9c6d25f6 | -6.6687 | -42.0314 | 2025-11-17 01:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 89.1 |
| 79bb6cea-1df1-3670-bc9b-ea9d8f7acc55 | -3.776 | -49.2517 | 2025-11-17 01:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 0dd5dcec-3211-301e-a9be-1fe7d9df29ed | -11.8486 | -49.2218 | 2025-11-17 01:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| be7925f3-15bd-307d-a800-5440104e97f8 | -5.3254 | -43.0415 | 2025-11-17 01:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 49.8 |
| d9ce9978-f9ca-37fe-a96a-b6b01b3cc985 | -4.7395 | -46.3821 | 2025-11-17 01:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 8fe3b493-9c34-3a95-84d7-f78b60ac0a56 | -4.7209 | -46.3832 | 2025-11-17 01:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 3d7a33a5-7213-3c9a-ad03-d5f3a1b8e348 | -11.8295 | -49.2242 | 2025-11-17 01:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 89acf82c-f750-3ecb-8fce-acf6b9d12198 | -6.6875 | -42.0296 | 2025-11-17 01:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 136.0 |
| 6c4a050d-2443-3e48-9540-104b090e1944 | -2.5053 | -47.8337 | 2025-11-17 01:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 92a7144e-e3b6-3ea2-8b17-e47afaf51d9f | -2.5238 | -47.8332 | 2025-11-17 01:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| fb860f31-ef66-3f8a-83de-a2f76adccadf | -3.7652 | -47.7468 | 2025-11-17 01:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 96db9110-d33e-3364-8c95-e5c4db927b0d | -2.5053 | -47.812 | 2025-11-17 01:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 1b55139c-37db-3b4f-860c-f1b330d853b6 | -4.9967 | -44.3607 | 2025-11-17 01:40:00 | GOES-19 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| d91e4522-a22a-321c-a060-4164bbc0c71d | -5.0401 | -43.5973 | 2025-11-17 01:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| cad423b5-661e-35b3-ad99-3bce75effd25 | -6.6873 | -42.0535 | 2025-11-17 01:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 76.7 |
| 324849f8-cecb-3667-83b1-9f064de6063a | -11.7017 | -48.8692 | 2025-11-17 01:40:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 3817b4ed-059e-3341-98f3-b0036cd9cb27 | -6.6684 | -42.0553 | 2025-11-17 01:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 50.7 |
| 58e71886-a27c-34e8-b7e4-8b33fc9c3f06 | -2.5238 | -47.8115 | 2025-11-17 01:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 3d4afc81-2012-3861-9072-5da9feba5718 | -3.7838 | -47.746 | 2025-11-17 01:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| e442c109-8a14-36db-98f4-7f4bcf9d41b3 | -11.849 | -49.2 | 2025-11-17 01:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 6ccdd185-15a3-35cb-bd8c-b68eaea111d6 | -5.0399 | -43.6205 | 2025-11-17 01:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 45.3 |
| aee121fe-b5c7-38f5-8854-7cb3d67cf0c0 | -6.6873 | -42.0535 | 2025-11-17 01:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 125.8 |
| 61cc531a-1d8d-320e-8d63-2c6802c57ed5 | -2.5238 | -47.8115 | 2025-11-17 01:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 05ec8d74-c22a-37aa-af2f-37c95248a8b5 | -11.8486 | -49.2218 | 2025-11-17 01:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| e98f19f7-d468-3e90-af10-85302a708a86 | -10.6687 | -49.3813 | 2025-11-17 01:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 4634f253-076e-3c94-b542-01df034c0079 | -3.776 | -49.2517 | 2025-11-17 01:50:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| b4cf5664-0f03-3f9e-95f4-85dd851e6e2f | -3.2343 | -50.5162 | 2025-11-17 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 27bcc421-52ec-3cdd-990f-c63ce3a0cd0a | -6.6687 | -42.0314 | 2025-11-17 01:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 78.6 |
| 25d4f173-cdbb-3975-8682-43dc8318b1cb | -3.2344 | -50.4952 | 2025-11-17 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 650c45fa-e136-35fd-9257-c738b3206e67 | -2.5053 | -47.8337 | 2025-11-17 01:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| a7bd1509-90af-3ad8-b77e-0efaa82ebfaf | -11.8295 | -49.2242 | 2025-11-17 01:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 6ee905eb-61c1-38be-ab2c-8c77801802d5 | -5.3254 | -43.0415 | 2025-11-17 01:50:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 9698ecc2-7316-33f6-bc29-2772e68321ac | -4.7395 | -46.3821 | 2025-11-17 01:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 65506187-6c4b-3026-8917-e6a5d18a68b2 | -2.5238 | -47.8332 | 2025-11-17 01:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 89ffce0e-0c80-395d-b681-7a8f03ca0cdc | -11.849 | -49.2 | 2025-11-17 01:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| dcf43d12-f8fe-3f3a-8dfb-1acb99c661a1 | -11.7017 | -48.8692 | 2025-11-17 01:50:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 1f5e0ec7-bd42-35fb-aa5c-d0b2defb9fa4 | -2.5053 | -47.812 | 2025-11-17 01:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 8f98b85c-08f2-3ea6-a339-fc13d43d06d3 | -5.0401 | -43.5973 | 2025-11-17 01:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 3c4cb758-84ba-3f9a-99ae-9df4e2094e16 | -10.669 | -49.3597 | 2025-11-17 01:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 5214f5c8-2332-3a32-81e1-5ebf1619ec3c | -6.6875 | -42.0296 | 2025-11-17 01:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 179.0 |
| 44cfcbc3-a659-3299-ba9e-71131d03e2e7 | -4.7209 | -46.3832 | 2025-11-17 01:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 64aa07fa-ae00-3aef-be76-035264017463 | -4.7209 | -46.3832 | 2025-11-17 02:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| c6f674b0-8a28-3c8b-a8e0-c215633482af | -3.3655 | -46.0702 | 2025-11-17 02:00:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 40cc42b8-00b3-322c-97f1-a2f880338f18 | -3.2344 | -50.4952 | 2025-11-17 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 39d1f800-847c-39be-974f-fdd0fc0ad380 | -11.8295 | -49.2242 | 2025-11-17 02:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| d60f8271-9cd6-3cc5-a742-338d812f5a83 | -3.3841 | -46.0694 | 2025-11-17 02:00:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 0847696d-1213-31b9-8e0c-7abd4f96720f | -4.7395 | -46.3821 | 2025-11-17 02:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 10897efd-be96-33b6-9abd-517b591a1fbc | -11.8486 | -49.2218 | 2025-11-17 02:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| c02a4ab0-0bb6-3ed1-a26c-26fce64331ef | -5.0401 | -43.5973 | 2025-11-17 02:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| a4704936-44b7-39e3-b3b5-8c48075f3ab3 | -2.5053 | -47.8337 | 2025-11-17 02:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 32e77788-7348-3bab-8d21-3ed03162a871 | -2.5238 | -47.8115 | 2025-11-17 02:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 93de79fd-5387-3066-a5b6-d11759b96cd0 | -6.6875 | -42.0296 | 2025-11-17 02:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 47.5 |
| a690def0-2823-3de2-9f1c-c6baa6498519 | -2.5053 | -47.812 | 2025-11-17 02:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 59d5e2fe-4bff-372b-a673-bda40231e3f4 | -11.849 | -49.2 | 2025-11-17 02:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 9917cd11-ece1-3981-9658-ecf10220cf39 | -3.776 | -49.2517 | 2025-11-17 02:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 58685415-68dc-38d9-9880-c6582f2728d9 | -11.7017 | -48.8692 | 2025-11-17 02:10:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 5d3a5991-be74-322d-ac75-bf13914ef14e | -11.8486 | -49.2218 | 2025-11-17 02:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 75220ff9-54d1-3b61-afb6-d7fe0881e109 | -3.3841 | -46.0694 | 2025-11-17 02:10:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 59.8 |
| abb13023-a3ba-3660-956b-a941e6331c3e | -6.6875 | -42.0296 | 2025-11-17 02:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 38.8 |
| ef98d28c-d924-31c9-b76e-b1d935d2d197 | -3.3655 | -46.0702 | 2025-11-17 02:10:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 77.5 |
| d7eb78d7-7940-37fe-a47f-1c4e618b6dbd | -3.776 | -49.2517 | 2025-11-17 02:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| ab189439-9a40-3a3a-896c-5b7cb5747bb8 | -11.8295 | -49.2242 | 2025-11-17 02:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 12546fc5-7346-3d48-88ac-8e1745619da2 | -4.7209 | -46.3832 | 2025-11-17 02:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 53.9 |
| efe521cf-237c-3995-998b-6fbafa1b1444 | -2.5053 | -47.8337 | 2025-11-17 02:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 550e9c18-8f61-3fdf-93be-d94312da345a | -3.2343 | -50.5162 | 2025-11-17 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 6a9b2eda-ddac-3269-86b6-8ac48e76a9cc | -2.5238 | -47.8115 | 2025-11-17 02:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| adfbf195-ff2b-386d-a05b-e55cb19fbd84 | -2.5053 | -47.812 | 2025-11-17 02:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 2294c046-ba9b-3872-9f0f-dfcdf82425af | -3.2344 | -50.4952 | 2025-11-17 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 53a2a7d9-c415-31d0-a55b-c40fb6c19e82 | -11.8486 | -49.2218 | 2025-11-17 02:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 96240874-3bc2-3c40-ad86-925089fdc52f | -2.5238 | -47.8115 | 2025-11-17 02:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 9ba22bfd-121d-3237-91b3-198fc6afc88f | -12.8804 | -46.0249 | 2025-11-17 02:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 4d5d6cbd-f315-3d1c-b615-d6a68df35954 | -5.3254 | -43.0415 | 2025-11-17 02:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 39.9 |
| ea25d4a5-e492-3114-9d36-b967115cf326 | -6.6873 | -42.0535 | 2025-11-17 02:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 48.6 |
| 00ae70d9-8789-3199-bda8-7c02a2ea8226 | -15.8359 | -42.6879 | 2025-11-17 02:20:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.0 |
| 23e2abb0-7b73-3460-b7a8-e07352ed59d8 | -12.8611 | -46.0279 | 2025-11-17 02:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| f60ddafc-1123-3282-9fa2-46b7f2bbea05 | -2.5053 | -47.8337 | 2025-11-17 02:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 0ea7468b-ef48-3112-8e0e-3a3085f13417 | -2.5238 | -47.8332 | 2025-11-17 02:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 7cc7ca2d-460a-34e9-b99b-926556bc02c4 | -11.7017 | -48.8692 | 2025-11-17 02:20:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |


[Clique aqui para ver as próximas entradas](README10.md)
