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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dfb73854-e9cc-33e3-937a-8a2ef0489e4a | -2.48515 | -49.415 | 2025-12-04 04:48:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b75fb965-6395-32ff-8597-beeca792f81b | -3.8457 | -47.83816 | 2025-12-04 04:48:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41ff8686-62c4-3d74-b14f-e708c1a11876 | -3.22466 | -48.61606 | 2025-12-04 04:48:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d807179c-8996-3d5b-8abb-300ec1b301b7 | -4.0784 | -43.69181 | 2025-12-04 04:48:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99271e4e-a725-3672-ac8f-2f11eea4392b | -2.53894 | -45.36782 | 2025-12-04 04:48:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 01b22d10-7f76-34fc-88d2-a4f3f984376a | -2.14449 | -47.88167 | 2025-12-04 04:48:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 405872e2-2a72-38c9-8a96-0f1e0db0687c | -1.97037 | -46.05165 | 2025-12-04 04:48:00 | NPP-375D | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ced7bb2-33e5-38fc-8b06-482ece6de6f4 | -3.32688 | -44.38058 | 2025-12-04 04:48:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3da2f21-48bf-35f7-9714-1ecd807ddf00 | -3.72107 | -45.58273 | 2025-12-04 04:48:00 | NPP-375D | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 532558ee-3185-3fc0-ae76-65f7126ca535 | -4.54584 | -45.69412 | 2025-12-04 04:48:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab3cadd8-a8cf-3705-b11e-056d1d4efb17 | -2.4224 | -45.79578 | 2025-12-04 04:48:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d361a020-10e6-355b-b548-9221c5e5d97d | -2.82583 | -48.44289 | 2025-12-04 04:48:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0bc96eb1-f32d-3dc4-8841-05989e134f42 | -2.60527 | -49.25071 | 2025-12-04 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e0a1c907-b1af-3936-9eb0-2a60f7503c8a | -3.21826 | -48.6118 | 2025-12-04 04:48:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3d12a893-63a0-3d78-a399-51a0423082cc | -2.53573 | -47.31442 | 2025-12-04 04:48:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bbc23d50-3514-3d95-99cc-2bd442519b6e | -4.389 | -43.12881 | 2025-12-04 04:48:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 46fd74f8-a95e-3bd7-8127-32bed109ca1b | -2.86005 | -45.24475 | 2025-12-04 04:48:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1148e94e-ba9d-3863-8a44-df189edc4411 | -4.07739 | -43.69341 | 2025-12-04 04:48:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6d528776-1c7f-3ee4-9ade-0f6a8f164db5 | -2.54023 | -49.45571 | 2025-12-04 04:48:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f4f8f332-b65f-3784-beac-a3b43667f83c | -2.46911 | -47.82831 | 2025-12-04 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 950959e9-1c2e-311d-82f2-3ace14959fab | -4.07769 | -43.69646 | 2025-12-04 04:48:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5663fc8-18a8-3962-9bc0-d7b4b26642d7 | -2.92591 | -48.23 | 2025-12-04 04:48:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8914ac17-a505-3722-8591-c5e223d0c042 | -3.92188 | -47.68933 | 2025-12-04 04:48:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88c3e05a-a98f-34e0-9b30-4c906a22a7d9 | -2.53356 | -49.45467 | 2025-12-04 04:48:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a7c2204-1c29-3c43-99c1-c13196ca05d5 | -2.70747 | -51.88962 | 2025-12-04 04:48:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1303a51b-919d-3194-9f4a-5f5de9fe1f70 | -3.66264 | -43.60076 | 2025-12-04 04:48:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6212a9e0-f4a0-343e-99f8-e7cbbc78b82b | -3.22167 | -48.61234 | 2025-12-04 04:48:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 93fd9a40-5a1d-3001-aead-fdcf4d98808f | -2.73341 | -51.5472 | 2025-12-04 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a41939aa-29ac-3d22-b26f-f4e6508974bf | -2.60137 | -49.25371 | 2025-12-04 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b4aa02fd-1a30-3380-8a80-32b006288479 | -3.22409 | -48.61972 | 2025-12-04 04:48:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e1322189-d260-3f2e-8d32-5d3b210821c9 | -4.34473 | -45.79113 | 2025-12-04 04:48:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ab3336b7-d8d5-36ab-accc-cd810e058828 | -2.60862 | -49.25124 | 2025-12-04 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 881657c6-7725-3a9b-8c3c-583976ead02c | -2.14668 | -47.88231 | 2025-12-04 04:48:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07d33dc5-24eb-33d9-9279-1417bf1ddb02 | -1.18377 | -49.04081 | 2025-12-04 04:48:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae5b13c3-cdeb-37f3-a72d-db53d1454460 | -4.21291 | -44.24789 | 2025-12-04 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29e52bad-bf5f-3390-8f43-1a6690473186 | -2.33119 | -49.082 | 2025-12-04 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 83e37900-0611-38fb-82b1-1b1216b3355f | -4.55842 | -45.80264 | 2025-12-04 04:48:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f06b0d57-bdc9-31f6-9c51-91556e333ca8 | -3.8317 | -47.50216 | 2025-12-04 04:48:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 094ca5bc-0eb9-3c26-a2cc-85835d2099b3 | -4.06283 | -46.56186 | 2025-12-04 04:48:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4ee9a1fa-f4f9-363e-b607-62f868008ae5 | -3.06762 | -48.03782 | 2025-12-04 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 225e3278-03de-3d75-96d2-55666d20f798 | -4.03014 | -46.97702 | 2025-12-04 04:48:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ebe3bd1-68e5-31b0-8809-66f15830c008 | -3.84631 | -47.83421 | 2025-12-04 04:48:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a823bbc9-1dfc-32f9-8fad-fc36d9bdc565 | -3.32902 | -44.16408 | 2025-12-04 04:48:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63126419-8783-3f3f-8e48-da35e2ff355e | -3.4074 | -47.08139 | 2025-12-04 04:48:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d43e29c9-a7b7-3634-8b5f-48fb8f5b283e | -4.02717 | -47.33972 | 2025-12-04 04:48:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 750215a5-d9b1-30e6-a1b0-4d84ad1fef36 | -3.2171 | -48.61913 | 2025-12-04 04:48:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3662e664-5415-3eea-8d60-ce3cd52c030b | -4.21176 | -44.24649 | 2025-12-04 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 05bbd20a-09d3-3b3b-858a-7e239abcd91e | -4.8262 | -43.19783 | 2025-12-04 04:48:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a784a8b0-6f72-3f51-8a99-ea9f0598afc3 | -4.06593 | -46.56689 | 2025-12-04 04:48:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| bd97a577-4900-307c-9d38-09575739200c | -5.02232 | -41.00609 | 2025-12-04 04:48:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6c01d777-5122-3842-8f03-782e8ea0c3f3 | -4.72511 | -44.71493 | 2025-12-04 04:48:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 721ea433-a0f5-3a25-be40-d79b89440ca1 | -3.23017 | -46.85496 | 2025-12-04 04:48:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92b49f30-65ef-3293-9036-3a71be326c01 | -2.6913 | -48.45695 | 2025-12-04 04:48:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8e88cd40-c37f-3f63-9980-389be7bc99f0 | -4.38777 | -43.13103 | 2025-12-04 04:48:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 477493e7-ab04-3843-bbd6-0cff9ece174b | -2.42164 | -45.80063 | 2025-12-04 04:48:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b4fe5171-91a1-3166-8d4f-5076e7d15337 | -4.5579 | -45.80611 | 2025-12-04 04:48:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| cd23d188-bee0-3b49-83c9-8b8435907767 | -1.13286 | -52.58822 | 2025-12-04 04:48:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 014ddccf-fbe0-3c92-a3da-37060be80155 | -4.80034 | -41.81856 | 2025-12-04 04:48:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5f6b8a5f-3c7e-3ba2-a449-4423429b146f | -3.38099 | -49.24776 | 2025-12-04 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b2856e05-67a1-30a8-9fab-6c93ea769d1b | -3.32696 | -44.38741 | 2025-12-04 04:48:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f591b571-820e-341a-b08e-04dea5655d5b | -4.0908 | -44.9847 | 2025-12-04 04:48:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 329ab528-0883-3b75-934e-bf7089d017ab | -1.42747 | -53.0079 | 2025-12-04 04:48:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 099bad58-2d5a-3e9e-b1be-de5f2b605bbd | -2.52912 | -49.46112 | 2025-12-04 04:48:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bbb74926-3972-333f-a3a9-af65f0aaccc9 | -4.85493 | -42.4758 | 2025-12-04 04:48:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f7e330e5-a8c9-3ac5-ab7b-22073bade00c | -2.53689 | -49.45519 | 2025-12-04 04:48:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3ac6f65f-6c97-3561-a616-1be3e3547f8f | -4.06214 | -46.56631 | 2025-12-04 04:48:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b0c3def5-9718-3631-bb07-8a2a0fffbc0e | -2.70402 | -49.31273 | 2025-12-04 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61f2c2ca-065f-3527-b885-4ee889e41e9d | 0.40809 | -50.75954 | 2025-12-04 04:48:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23e0cae1-3043-3ad1-a5f2-7a9d8da33e2c | -3.22751 | -48.62025 | 2025-12-04 04:48:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a0397f93-0dd6-398c-926a-4955ba7b1edd | -3.34515 | -49.23493 | 2025-12-04 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 851befc9-b0d2-3a16-a20e-c2cac6d3208b | -3.51889 | -47.20515 | 2025-12-04 04:48:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28cdd7c0-5584-3f44-9f62-03d21391cbbe | -2.53301 | -49.45815 | 2025-12-04 04:48:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e614a20-e051-36b1-88b4-1936df9b301f | -4.00276 | -46.54845 | 2025-12-04 04:48:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1c2f84f-4c61-3af8-aca4-6f580b63ea3d | -2.72947 | -51.55023 | 2025-12-04 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 137bc37e-8caa-3907-9b4b-41816ac62820 | -2.57517 | -47.15757 | 2025-12-04 04:48:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2d977c25-05f2-35de-9633-5005592c6dd2 | -2.95348 | -48.58607 | 2025-12-04 04:48:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 630bbca0-c37e-362f-89b2-2e2657f3ba5a | -4.38525 | -46.66745 | 2025-12-04 04:48:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 929d465b-8470-376d-9ef3-01825338bf27 | -4.34378 | -46.14182 | 2025-12-04 04:48:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9899655c-23d5-3917-8fc4-58bec04cae94 | -2.42553 | -45.80124 | 2025-12-04 04:48:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0fd87053-3e72-30ac-9b13-5b58afcc7bdd | -2.17418 | -48.36755 | 2025-12-04 04:48:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d2d483c-be3e-3377-bd9f-940171a7785b | -2.91902 | -48.2289 | 2025-12-04 04:48:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9970024c-9974-35d2-bc77-b3cbc69b4366 | -3.36656 | -44.09566 | 2025-12-04 04:48:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 560c049f-18f8-30b0-85fe-ad96ead50a16 | -2.78729 | -47.43236 | 2025-12-04 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6464d98-c7ee-3232-8ec4-3db1750c5601 | -1.42682 | -53.01202 | 2025-12-04 04:48:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fe9073be-b9ef-3152-9450-f0f7973db42f | -2.53779 | -45.36801 | 2025-12-04 04:48:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 893c68f0-3f64-3cd9-9252-e2979fd53c53 | -1.69927 | -46.15508 | 2025-12-04 04:48:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82a44712-a1ee-32fe-8c52-aa07e7049b5a | -1.46787 | -49.04162 | 2025-12-04 04:48:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5cb7c1bf-2135-3115-9a4c-f8147b742ad4 | -3.93936 | -46.73878 | 2025-12-04 04:48:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc1b3562-c46d-33fe-b16d-388c5142c767 | -3.0418 | -48.42272 | 2025-12-04 04:48:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 73623631-eae7-3417-84d3-2a7339c700ec | -2.14261 | -47.88555 | 2025-12-04 04:48:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b67e14f-1857-3f6d-ae5c-eca831f697eb | -3.32624 | -44.38471 | 2025-12-04 04:48:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80869723-e37a-30a7-b386-e7b917e663f9 | -2.69188 | -48.45328 | 2025-12-04 04:48:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fbd440f9-6eca-3118-90c5-8e7a80389692 | -3.82101 | -46.55271 | 2025-12-04 04:48:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 567ec00b-81ea-3e94-a7e4-210e39a73ecb | -1.67466 | -45.79364 | 2025-12-04 04:48:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d57bc61b-a1bf-35ae-841e-771c9e576e87 | -2.35507 | -50.11054 | 2025-12-04 04:48:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abdee348-17ab-3a0b-bbe7-31283c2e6c6b | -2.34835 | -46.91708 | 2025-12-04 04:48:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef43af54-7237-3aa2-a404-65093bffbf02 | -1.98405 | -46.1319 | 2025-12-04 04:48:00 | NPP-375D | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a62e615-d939-380f-92d8-72e9f33ed463 | -2.92532 | -48.23374 | 2025-12-04 04:48:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 827468e3-d86d-366a-9296-dfb44423cf0d | -2.53744 | -49.45171 | 2025-12-04 04:48:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 69ddaaf3-8b42-37e5-849c-6f76e6c73a52 | -3.21778 | -46.0584 | 2025-12-04 04:48:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README16.md)
