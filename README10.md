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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a8c08bc-e559-3c80-9fe1-7703511beb97 | -5.81041 | -40.81561 | 2025-10-28 03:21:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f472b920-9e41-38c7-8d50-62830d5caaba | -6.4183 | -42.33405 | 2025-10-28 03:21:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 3cf78306-c5e8-33a5-9ae8-7eff5dd10273 | -5.48467 | -42.16696 | 2025-10-28 03:21:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ae310d36-d10e-3840-a512-e8facf99297c | -9.04538 | -38.94721 | 2025-10-28 03:21:00 | NOAA-20 | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1695f9f3-7ef9-38ac-98d9-b3e5c44e7d4b | -6.42563 | -42.33009 | 2025-10-28 03:21:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 8b06a17e-01d7-3873-9e2f-5785cd741f63 | -6.42378 | -42.32974 | 2025-10-28 03:21:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 3bd29d57-ddc5-3fad-ae8e-f66b68fb83aa | -6.15524 | -41.53972 | 2025-10-28 03:21:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dee8c4c7-2845-31ae-9f40-a1bcc1453345 | -4.45419 | -43.64382 | 2025-10-28 03:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 6634f229-bb46-3990-bd55-094f157cd594 | -5.65814 | -41.15237 | 2025-10-28 03:21:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0e4d4c49-b5ca-3f33-8d91-46f512c22152 | -6.68897 | -42.04651 | 2025-10-28 03:21:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 827d59e0-0d37-3f5c-8ddc-ecfe095e7df6 | -5.80446 | -40.81511 | 2025-10-28 03:21:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 507677fa-00f5-3271-9be9-9bfcd999a136 | -6.64586 | -43.38383 | 2025-10-28 03:21:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 72b19362-f73a-3b50-86d3-9d208e66537a | -3.57535 | -43.64305 | 2025-10-28 03:21:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d818ddc9-de86-330f-8ce1-6df439e44fd2 | -5.62826 | -39.66004 | 2025-10-28 03:21:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 42ceaf52-9668-35f4-aaed-88f2beb6d13f | -6.68185 | -42.05029 | 2025-10-28 03:21:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 56a43bdb-2b77-32a6-9713-91809fb9b881 | -6.82661 | -41.21077 | 2025-10-28 03:21:00 | NOAA-20 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3839d7b1-9f5f-358e-a775-ea361bc3be84 | -5.66213 | -41.11812 | 2025-10-28 03:21:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d765f821-4d53-3d88-b0f8-bf431a6ab701 | -6.69606 | -42.04292 | 2025-10-28 03:21:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 8b9e9d87-0ded-3343-a77f-4519c4ebf75f | -6.44574 | -42.36364 | 2025-10-28 03:21:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e82b09a1-5c24-399b-b4e5-c0bf0fc5aeb0 | -4.4507 | -43.64503 | 2025-10-28 03:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f5e3cd19-e4c1-3e1d-ba8a-911c13ecbd54 | -8.18692 | -44.4501 | 2025-10-28 03:21:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 70640a04-38d2-38d6-b2fd-e3cf2c0e18e4 | -6.13594 | -41.71658 | 2025-10-28 03:21:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ef4392b4-8c54-3fa4-b2db-645024cbe3ca | -5.65218 | -41.13951 | 2025-10-28 03:21:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d7a55ec6-4131-325f-82f8-504904a6483f | -5.49105 | -42.16825 | 2025-10-28 03:21:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1bf4b37e-1cee-3d01-85d8-0d10a2d7ea28 | -4.45522 | -43.24063 | 2025-10-28 03:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| cab33107-ecc5-3242-bf5b-34c0b2509dfa | -6.69343 | -42.04548 | 2025-10-28 03:21:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 69d8d7c3-4652-3ea2-9f9a-3fb834e51abd | -4.45782 | -43.64613 | 2025-10-28 03:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 49cfff45-de53-3972-9833-42920de4aa51 | -5.21943 | -37.38944 | 2025-10-28 03:21:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 42f435ba-7e9b-357f-b0dc-e44a5f0bde58 | -3.57917 | -43.62137 | 2025-10-28 03:21:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1bf121d4-1020-3d70-bae4-ddb58f623a30 | -6.68814 | -42.03934 | 2025-10-28 03:21:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 0793ac3c-3c02-3f84-b82c-8a6c2a56d27b | -5.65735 | -41.1453 | 2025-10-28 03:21:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 3929b1f2-2884-3f13-9e6a-3b8d447134d4 | -6.42285 | -42.33489 | 2025-10-28 03:21:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| fa4c7451-845f-3d55-85d3-9eff3acd4ac0 | -4.46215 | -43.24184 | 2025-10-28 03:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 9f9e2978-c728-37eb-a1b5-b0bc9b38ede1 | -8.18992 | -44.44566 | 2025-10-28 03:21:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6adbed5a-25f9-3c0b-9384-f6a44fb6dd68 | -3.5838 | -43.63708 | 2025-10-28 03:21:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 25ed18df-2709-3e0c-bf9b-87d16ed396f5 | -5.70038 | -43.53672 | 2025-10-28 03:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a9e2a31d-be7a-3766-b7ad-70602e3666ab | -6.64484 | -43.38938 | 2025-10-28 03:21:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d1d8f9ab-ccd6-3de4-8bc5-36744c428663 | -6.69965 | -42.04671 | 2025-10-28 03:21:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 9eab9ec0-3a17-3081-a5ab-182b62fc6708 | -5.48921 | -42.17221 | 2025-10-28 03:21:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| abf483ab-8859-31fd-a289-e5f12a5dd2b0 | -6.87143 | -43.59155 | 2025-10-28 03:21:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f97f11ff-4f0b-36f5-9faf-c776c48135ee | -8.18822 | -44.44349 | 2025-10-28 03:21:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| eb5f832c-f889-34a8-b828-1e7580b5bde1 | -4.45559 | -43.23364 | 2025-10-28 03:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 441c1056-a29a-3ddf-bc5d-bf649d09527a | -3.58041 | -43.61431 | 2025-10-28 03:21:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b3bf2741-6173-36c1-9bc7-e350dba38f92 | -6.13001 | -41.71419 | 2025-10-28 03:21:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 52dce37a-92e3-3403-9f47-f42114cd75cc | -6.70141 | -42.049 | 2025-10-28 03:21:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| ef5c88ad-b298-3d73-93b3-28bd85689ae6 | -5.79569 | -35.60386 | 2025-10-28 03:21:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 0f0dd3cf-5271-3862-a187-724c4a0b3130 | -5.6505 | -41.14906 | 2025-10-28 03:21:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 8bbd6b42-c31b-3dbf-8673-ef2414cb8cf6 | -3.58246 | -43.64468 | 2025-10-28 03:21:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 241ff9ab-3c3a-351f-b5d2-d0d240284c5a | -3.56946 | -43.63447 | 2025-10-28 03:21:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f1fcc3e4-c7d4-3b37-be93-5ca60d0d31fd | -4.45635 | -43.23413 | 2025-10-28 03:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 0f3d085c-2fb5-36be-bb89-7d344dc1891d | -7.5985 | -43.59288 | 2025-10-28 03:21:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 38d53b2b-b465-3951-8c64-1a45a27e0a7f | -6.1177 | -41.71185 | 2025-10-28 03:21:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1029a546-32f4-380f-99aa-2b044d0a6de4 | -5.66067 | -41.13853 | 2025-10-28 03:21:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6d40fd4a-7b81-3463-afa1-bcf4416bacd3 | -6.70052 | -42.04203 | 2025-10-28 03:21:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 1c5d6832-5a09-3d86-8d92-cbad3157784c | -6.23236 | -43.32059 | 2025-10-28 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 871fa841-deb6-3e01-b078-cc3330d27b86 | -6.12521 | -41.7102 | 2025-10-28 03:21:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 137e8ff2-df24-3210-a617-872c38986c63 | -9.01485 | -43.98022 | 2025-10-28 03:23:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f88894f-affd-35f0-aaba-adc7ecbaaedb | -13.94089 | -43.80435 | 2025-10-28 03:23:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b7cabf2f-50db-337b-89ee-4b3f99f6291f | -11.28088 | -45.50496 | 2025-10-28 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 8f9cdb56-51ac-3536-ace2-5e1ae48fe092 | -11.28129 | -45.52052 | 2025-10-28 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.5 |
| f9532f88-6628-3f15-b8bd-20d865ba10c6 | -11.28273 | -45.51349 | 2025-10-28 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 961dd56b-c847-3187-956f-25c9969422c3 | -11.2794 | -45.51192 | 2025-10-28 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.7 |
| f3e6701a-e2e2-31fc-b8f7-a532710bdc3f | -12.08733 | -45.67717 | 2025-10-28 03:23:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2de1141d-db66-32cc-9633-a46f1320eb63 | -12.61796 | -45.07935 | 2025-10-28 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b557bc81-b466-39e6-9fb4-b51d5a092cf3 | -12.08942 | -45.68232 | 2025-10-28 03:23:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 01c3bb08-22ed-36f1-847f-3e57f1e223d3 | -12.63142 | -45.08235 | 2025-10-28 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 484ba617-b0cc-3225-abec-2b67d792947f | -12.61662 | -45.08552 | 2025-10-28 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ccd5409d-192f-3346-9515-f8ac6e52a38c | -14.70057 | -43.78975 | 2025-10-28 03:23:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 359ee65e-429d-3436-a866-802d5fecea7b | -11.28644 | -45.5135 | 2025-10-28 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 9348c15c-922e-3285-8d70-0774004c79ed | -8.63856 | -44.79078 | 2025-10-28 03:23:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3ae0014-b0b4-3090-9c9a-ff0ea1b38671 | -12.46729 | -44.50082 | 2025-10-28 03:23:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4b07bea-ccaf-3f40-94d7-9ac2672d714a | -12.62311 | -45.0804 | 2025-10-28 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 02d3b88e-b11c-3ca9-9259-63ef387ed559 | -12.54773 | -44.93919 | 2025-10-28 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 59e5c88c-6808-308b-9144-42b202dd0ace | -14.15182 | -44.24873 | 2025-10-28 03:23:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 795f9a21-892e-3052-8008-3eadea71b15f | -12.47383 | -44.50218 | 2025-10-28 03:23:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be34328b-b466-3999-a701-a50f28c95915 | -11.28973 | -45.51527 | 2025-10-28 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c58888b8-5343-3e17-8df9-bbc1ec186bf5 | -13.53949 | -44.14284 | 2025-10-28 03:23:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c1cc75ac-466b-3195-a626-0152d3a61ed3 | -12.08187 | -45.66838 | 2025-10-28 03:23:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f7eed40a-a2cb-358f-bdda-361444c40c4d | -11.27423 | -45.51896 | 2025-10-28 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.5 |
| ad20b316-eefb-3e9b-b9da-3393790ebd7b | -12.55106 | -44.94399 | 2025-10-28 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d28d165-e355-30f2-b420-f37d9022b444 | -13.5406 | -44.13754 | 2025-10-28 03:23:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 954cb9b6-2551-39f7-8fa4-3b3fd7b45d4b | -12.54565 | -44.93637 | 2025-10-28 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3997da55-845f-3b72-b43a-1f26b0dfc9b4 | -10.62327 | -42.31887 | 2025-10-28 03:23:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3764d585-f8f9-3d1b-a6be-ce8ada36b4eb | -14.4389 | -44.79905 | 2025-10-28 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb58b5cb-ae2b-352c-be8e-0e316535eb18 | -13.78525 | -44.34694 | 2025-10-28 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 67ef6fc5-4167-352d-a6b2-e8b20ac1ea10 | -13.55336 | -44.26598 | 2025-10-28 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93d82270-0f7c-39c5-b003-6123818111ca | -11.27714 | -45.50481 | 2025-10-28 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 1cbeaad6-8c2f-3372-8787-dae1a0d31f70 | -9.33746 | -43.09471 | 2025-10-28 03:23:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 179fb209-1e49-3801-90ad-0b21783cdac6 | -12.18694 | -43.58957 | 2025-10-28 03:23:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b660092e-0b97-3a8f-b00c-2178c3cea60f | -11.27791 | -45.51894 | 2025-10-28 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.7 |
| e7e44f4d-bec3-3974-971b-16f2b9eb7134 | -13.63494 | -46.47628 | 2025-10-28 03:23:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2058f6f9-523f-3cb1-a5c7-9033dd172fc8 | -10.62416 | -42.3144 | 2025-10-28 03:23:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c0247a4d-27e7-3496-a671-57c230f0292e | -10.87933 | -44.39972 | 2025-10-28 03:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37fa8057-c1fc-3ce9-8977-5922be886899 | -13.44528 | -44.10946 | 2025-10-28 03:23:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 52009be0-3d03-31aa-b9b9-e878c8938938 | -8.63001 | -44.79661 | 2025-10-28 03:23:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4283ad7d-09e4-3f15-b522-d16fc0852b61 | -10.63232 | -42.32072 | 2025-10-28 03:23:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fa73e024-7c4b-31e4-9a46-b6ad6ed9391f | -10.63009 | -42.31562 | 2025-10-28 03:23:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 1108ede8-091f-3016-b4d8-011ec111391c | -12.62857 | -45.08796 | 2025-10-28 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6e67031f-2fa5-3cb4-a9b4-f0bd36275350 | -14.1456 | -44.24722 | 2025-10-28 03:23:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 21cfc2e1-cae5-3ebe-af05-7e6f2e8dc047 | -12.19003 | -43.58707 | 2025-10-28 03:23:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README11.md)
