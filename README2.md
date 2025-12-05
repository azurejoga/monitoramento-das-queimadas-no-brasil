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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9da06fbe-9518-3c2a-ad1b-d48e4f2b2dfc | -3.3332 | -42.1035 | 2025-12-05 00:00:00 | METOP-C | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6d8a093f-848c-3367-ad5e-3c86476d98e2 | -3.4919 | -42.076698 | 2025-12-05 00:00:00 | METOP-C | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d98f5391-6c87-30e7-a9f0-3ca641630dac | -5.221 | -39.254902 | 2025-12-05 00:00:00 | METOP-C | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 176d32bc-7089-3c87-96cb-2538f99f86b9 | -4.7401 | -44.437099 | 2025-12-05 00:00:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a7b88c3e-063b-3f64-9bd1-d25505ee020f | -3.4182 | -39.264301 | 2025-12-05 00:00:00 | METOP-C | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| caa6beb3-fb19-3e7c-845c-0cb56aec895d | -7.5236 | -40.5532 | 2025-12-05 00:00:00 | METOP-C | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| e80abf17-a098-3ca9-b5ad-94c492e84279 | -5.8668 | -39.103001 | 2025-12-05 00:00:00 | METOP-C | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ca0532e3-7175-3b5e-8c35-c6ac15ad4441 | -4.7279 | -44.428398 | 2025-12-05 00:00:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 01290910-2614-3e28-b120-d015605a1af4 | -3.4337 | -45.565102 | 2025-12-05 00:00:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b2503b45-3086-3932-8c7a-b5e9f98b47aa | -2.8503 | -45.7957 | 2025-12-05 00:00:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d81a4d32-c5a3-3756-be13-6fb32f1a5879 | -6.0097 | -41.145401 | 2025-12-05 00:00:00 | METOP-C | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 92c2672b-f782-3e1c-a5b9-c48cc2f0fb76 | -5.8684 | -39.109798 | 2025-12-05 00:00:00 | METOP-C | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2829d8f7-e226-38d1-bdd1-292b411a0926 | -2.8844 | -39.9058 | 2025-12-05 00:00:00 | METOP-C | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ef402b5d-4f46-3542-b665-49adb378a0be | -3.3455 | -42.158001 | 2025-12-05 00:00:00 | METOP-C | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 770d9eaa-ac28-38e9-acc2-f3b9af974280 | -4.159 | -39.2561 | 2025-12-05 00:00:00 | METOP-C | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 93fd45de-8c4d-340b-a5b5-fd3e1c6b3c63 | -5.9177 | -42.992699 | 2025-12-05 00:00:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fdee7f8a-2e69-38a8-8345-c482c57e8166 | -4.7132 | -44.4543 | 2025-12-05 00:00:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3bd4bca1-2678-36c3-8fdd-e5db0cf469cc | -5.4662 | -39.516399 | 2025-12-05 00:00:00 | METOP-C | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 7c7e81df-af32-34fd-87bd-8dc963ba8452 | -4.6163 | -38.6866 | 2025-12-05 00:00:00 | METOP-C | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| b4c9992d-6fe2-387d-ad77-568d795b54d2 | -6.0004 | -41.1295 | 2025-12-05 00:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 130.6 |
| b93c8362-77cc-3691-8e0a-2f90868a80e5 | -1.4532 | -46.7217 | 2025-12-05 00:10:00 | GOES-19 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 0df2fa1d-f9f6-31a1-bfe1-07ee55e5ddfc | -10.5969 | -53.4573 | 2025-12-05 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 361f23c3-f6cc-3ec8-9750-e2fec8d146ff | -2.9049 | -45.2368 | 2025-12-05 00:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 265.6 |
| 673ccd4e-97a2-3198-8a3d-38f53c74ea74 | -2.905 | -45.2143 | 2025-12-05 00:10:00 | GOES-19 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 153.5 |
| fc5dcb1d-bdf6-3389-b1a2-d8fb65648358 | -6.019 | -41.1521 | 2025-12-05 00:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 122.9 |
| ca96068f-3d09-3cda-8ad2-f8feb1fddc5b | -2.7192 | -45.1982 | 2025-12-05 00:10:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 13b77b59-1e4f-3d7e-954c-19dad4803ce7 | -6.0192 | -41.1278 | 2025-12-05 00:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 127.9 |
| d7a5f6c2-f973-365d-b3a3-d14e97659ef2 | -2.9048 | -45.2594 | 2025-12-05 00:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 94d900e8-a59f-3b0b-9035-2a15043267fe | -6.0002 | -41.1538 | 2025-12-05 00:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 119.8 |
| c5da7946-1bad-3450-8b88-55e36d698641 | -6.019 | -41.1521 | 2025-12-05 00:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 90.3 |
| 0757609f-c89a-3bed-9a86-21c5ab7c6617 | -6.0004 | -41.1295 | 2025-12-05 00:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 127.6 |
| 3cc646a0-7225-302a-8a22-e0bb258d21c2 | -1.4532 | -46.7217 | 2025-12-05 00:20:00 | GOES-19 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 2af5f16f-2cf0-31d2-a6a9-dd3812257af9 | -2.9048 | -45.2594 | 2025-12-05 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 84.3 |
| ac4e3049-02d4-3d60-931a-f08fd3700bf5 | -1.4717 | -46.7214 | 2025-12-05 00:20:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 6d41e9c0-e5af-35b8-bc06-31bd50cf4747 | -2.905 | -45.2143 | 2025-12-05 00:20:00 | GOES-19 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 134.0 |
| 8c267e30-b7bd-3f8a-8094-3c8c074f0eb9 | -2.9049 | -45.2368 | 2025-12-05 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 310.1 |
| 1fe94cf9-9aa9-3d2f-8ada-b39a82e10a82 | -2.9235 | -45.2362 | 2025-12-05 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 132.5 |
| c89dbbf4-4708-3e7d-8ebe-769315c98ce3 | -2.8863 | -45.2375 | 2025-12-05 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 136.5 |
| d8ae4340-8ccc-317e-a6ff-205628e6ea26 | -2.7192 | -45.1982 | 2025-12-05 00:20:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 75.7 |
| bc8da979-6452-30fa-9881-7c1ed3581c4c | -6.0002 | -41.1538 | 2025-12-05 00:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 150.1 |
| 713d64fb-9f0e-320a-9989-df8b22f7f13d | -6.0192 | -41.1278 | 2025-12-05 00:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 78.0 |
| 8ae829e7-0e6e-39ab-b2df-79755b796ee9 | -6.019 | -41.1521 | 2025-12-05 00:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 99.0 |
| f1559386-22e2-3c08-bf35-67858eed651e | -6.0192 | -41.1278 | 2025-12-05 00:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 86.6 |
| 21d5e9a0-19a4-3124-9563-44408ce5a923 | -6.0002 | -41.1538 | 2025-12-05 00:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 110.9 |
| 9dd0e07a-6931-3665-861c-8364f5b38ca6 | -2.8863 | -45.2375 | 2025-12-05 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 2e458271-047f-3452-9b79-f30eb413ffad | -2.905 | -45.2143 | 2025-12-05 00:30:00 | GOES-19 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 123.5 |
| fc01b2fd-47a9-3feb-a912-e8726d324151 | -1.4532 | -46.7217 | 2025-12-05 00:30:00 | GOES-19 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 3c03b2e8-4b78-3a20-b032-586eb2199bae | -2.9235 | -45.2362 | 2025-12-05 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 06aa8edb-5bb4-316f-9f18-c539cb3a7c1d | -2.9049 | -45.2368 | 2025-12-05 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 367.8 |
| eb224d0a-7c6c-3f3b-a586-ad82faa8adf8 | -1.4717 | -46.7214 | 2025-12-05 00:30:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 076ef660-f0b5-3d07-9a22-19621c22626a | -2.0266 | -46.9958 | 2025-12-05 00:30:00 | GOES-19 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 73feae7f-410e-3fe6-8a1d-7302a0305a65 | -6.0004 | -41.1295 | 2025-12-05 00:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 98.3 |
| 20cff9cf-48cc-354b-a268-a932afce89b1 | -6.019 | -41.1521 | 2025-12-05 00:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 74.3 |
| a2c35954-9d39-3e95-8591-8e17949e3423 | -2.8863 | -45.2375 | 2025-12-05 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 3e18c800-7ba1-3b75-90d5-30f20585b3f2 | -5.1938 | -43.0977 | 2025-12-05 00:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 68c981a1-57a7-3d70-a868-6c68dd55056a | -6.0192 | -41.1278 | 2025-12-05 00:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 75.7 |
| 38c8f848-eadc-326b-a2b4-e9e15553ced2 | -6.0002 | -41.1538 | 2025-12-05 00:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 108.0 |
| 91cb73a1-faa5-35ea-bac0-34bc02139f73 | -5.194 | -43.0743 | 2025-12-05 00:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 155.4 |
| eb5eab1d-a4d4-3ce2-b437-9b35acce0080 | -2.9049 | -45.2368 | 2025-12-05 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 172.3 |
| 80c9c3f4-8448-3adf-8638-5025a1fe1d27 | -5.1566 | -43.0769 | 2025-12-05 00:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 053ecaaf-318a-3073-9999-0bd08d99ea05 | -5.1751 | -43.099 | 2025-12-05 00:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 252.4 |
| 70729c6c-639d-3315-bf92-a52babd7283d | -2.905 | -45.2143 | 2025-12-05 00:40:00 | GOES-19 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 224fb6f7-a317-355f-badd-7de5a4b1ea9d | -5.1753 | -43.0756 | 2025-12-05 00:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 459.5 |
| 5e89707a-0c5f-3063-8c6b-65b5ca004374 | -2.9235 | -45.2362 | 2025-12-05 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 3561ccbd-f83d-3083-af60-b5e619c3e8d7 | -5.1755 | -43.0522 | 2025-12-05 00:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 0a480221-8360-3fe7-9ed1-947a1212c40c | -6.0004 | -41.1295 | 2025-12-05 00:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 118.8 |
| 7b3be736-ffc5-335e-bd79-98a3647c75a8 | -2.0266 | -46.9958 | 2025-12-05 00:40:00 | GOES-19 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| aa0b000f-e207-3514-a0ac-e7bb3d06ec60 | -5.1751 | -43.099 | 2025-12-05 00:50:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 165.4 |
| 69ea0ce1-479b-3b81-9532-3a313c4a4c17 | -5.194 | -43.0743 | 2025-12-05 00:50:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 9cc1af38-9ed2-3af8-a678-38881006a1bc | -2.9049 | -45.2368 | 2025-12-05 00:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 121.8 |
| 84fbb299-7daf-3165-8a81-a2bfdcbf0aec | -5.1938 | -43.0977 | 2025-12-05 00:50:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 6b6caa69-22b8-3016-a3e9-207c24e4dc6b | -6.0002 | -41.1538 | 2025-12-05 00:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 120.3 |
| ecf50be1-19c7-381d-a0d1-1889f84b2060 | -5.1753 | -43.0756 | 2025-12-05 00:50:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 218.7 |
| cfe153bb-9fdd-35ca-94fa-3426e6f3bdfb | -1.4532 | -46.7217 | 2025-12-05 00:50:00 | GOES-19 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 8483dca0-a501-3dcb-a981-922353ec2142 | -3.641 | -43.3065 | 2025-12-05 00:50:00 | GOES-19 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 935a0114-690a-3d0a-be2e-75db58f6b232 | -5.1755 | -43.0522 | 2025-12-05 00:50:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| ff7368f7-3e6f-3685-a5b2-3214689e3230 | -6.019 | -41.1521 | 2025-12-05 00:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 90.6 |
| cff12a7f-9a45-3fd1-a420-27752ab24bb6 | -6.0192 | -41.1278 | 2025-12-05 00:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 79.3 |
| 384310ca-2dda-3a80-aec1-4e842dd1c4b5 | -6.0004 | -41.1295 | 2025-12-05 00:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 104.2 |
| 9310cc93-2314-3d51-a238-19b070ac4842 | -6.019 | -41.1521 | 2025-12-05 01:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 88.7 |
| 4ff3257d-f88e-3ca1-a96f-50bd82d1f816 | -3.6409 | -43.3297 | 2025-12-05 01:00:00 | GOES-19 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 5b368e33-7831-3ff5-a58e-b63eeb0b3f06 | -6.0004 | -41.1295 | 2025-12-05 01:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 109.3 |
| 4d513f86-da20-3e32-a5e8-793261b3687f | -6.6438 | -40.8751 | 2025-12-05 01:00:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 90.2 |
| eec6b817-76a9-3e54-8fa0-9b05c5710356 | -5.1753 | -43.0756 | 2025-12-05 01:00:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 169.3 |
| a8d8f5c3-a93b-3aee-bd80-7a3f23c40dd8 | -5.194 | -43.0743 | 2025-12-05 01:00:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 4168aa6e-c6e5-3b7d-9de2-84337864850d | -5.1751 | -43.099 | 2025-12-05 01:00:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 2338ad34-2275-37d4-90bc-027725a9cd84 | -3.641 | -43.3065 | 2025-12-05 01:00:00 | GOES-19 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| ef5f7539-b83d-31a7-80bb-7b19180b53e8 | -6.0192 | -41.1278 | 2025-12-05 01:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 95.4 |
| 943a3b04-9dd8-3f6b-9da1-00d7b9d790fc | -2.9049 | -45.2368 | 2025-12-05 01:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 6bbeffdf-dd65-300f-9b07-815cb1f40600 | -6.0002 | -41.1538 | 2025-12-05 01:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 98.7 |
| cc869a7c-2d98-3737-b3c7-b5751fae0f46 | -5.1938 | -43.0977 | 2025-12-05 01:00:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 69a74416-5ca6-3be2-96ba-0be84eac6bc7 | 1.9598 | -55.728699 | 2025-12-05 01:01:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53ed5018-2dba-34f0-9afd-954c78679ff9 | 1.9633 | -55.713001 | 2025-12-05 01:01:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ae5fde3-26a8-33f1-a0c0-82fe3fc0361d | -31.59142 | -53.61723 | 2025-12-05 01:04:00 | TERRA_M-M | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 6.4 |
| b08584ca-2f97-3970-8bc1-e377dc83ae11 | -31.59296 | -53.62778 | 2025-12-05 01:04:00 | TERRA_M-M | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 38.9 |
| ea299c06-ea9d-346b-8939-92c46a62f30f | -30.90042 | -53.49567 | 2025-12-05 01:04:00 | TERRA_M-M | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 10.4 |
| 389d4354-def9-331f-a95f-7cf9af35d819 | -31.34947 | -51.96731 | 2025-12-05 01:04:00 | TERRA_M-M | SÃO LOURENÇO DO SUL | RIO GRANDE DO SUL | Brasil | 4318804 | 43 | 33 | nan | nan | nan | Pampa | 6.7 |
| 414b2c76-b83b-35f2-be16-4fdab2026bde | -30.902 | -53.50624 | 2025-12-05 01:04:00 | TERRA_M-M | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 6.4 |
| 06ca9f56-ebc5-34ae-8db4-94c93fbb0d47 | -21.24897 | -49.25204 | 2025-12-05 01:06:00 | TERRA_M-M | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.1 |
| 797f7325-6708-336b-8985-43a6126d1350 | -23.62327 | -51.65441 | 2025-12-05 01:06:00 | TERRA_M-M | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 19.3 |


[Clique aqui para ver as próximas entradas](README3.md)
