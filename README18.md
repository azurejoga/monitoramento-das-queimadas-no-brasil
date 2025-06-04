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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 653eea34-7160-305a-b992-f6ceb98e942b | -6.40122 | -45.74852 | 2025-06-04 12:23:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 47b7b2ef-07fd-33e8-b414-f395ddd13361 | -10.31961 | -46.7126 | 2025-06-04 12:23:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| e879cd77-33bf-3365-8711-08561c561b57 | -10.51658 | -49.74936 | 2025-06-04 12:23:00 | TERRA_M-T | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 9df04d10-416f-3cd6-8151-5426ebe278f8 | -9.26082 | -47.65368 | 2025-06-04 12:23:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4c115b88-511f-3a9a-960c-8762f76a3e1e | -7.01817 | -44.58803 | 2025-06-04 12:23:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 779bb064-89d7-3b77-ac54-ae6ac9540a5a | -11.47321 | -47.91932 | 2025-06-04 12:23:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b02d9e78-f926-379e-883f-c808d462ada6 | -11.73482 | -45.23475 | 2025-06-04 12:23:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9d81426b-5f22-3375-be42-2ee97ea89613 | -10.68369 | -47.19731 | 2025-06-04 12:23:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6a0d10c3-b7db-37e7-a5b6-c2dc0ca357e1 | -9.12276 | -48.65272 | 2025-06-04 12:23:00 | TERRA_M-T | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 04a55df8-04c4-326e-b391-87d67e7d9292 | -10.25947 | -49.29729 | 2025-06-04 12:23:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 136ef873-4093-3d14-88a7-7cbfb2bbe6ca | -10.06953 | -50.58406 | 2025-06-04 12:23:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 1e8597e3-ed9e-381b-8b98-bdb4bb166126 | -11.55065 | -47.31535 | 2025-06-04 12:23:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e71d6c29-511e-35c3-b2f3-374c00c08205 | -9.25947 | -47.66285 | 2025-06-04 12:23:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 060a7013-7542-3862-a9e2-3045a9ed694f | -7.20553 | -43.55249 | 2025-06-04 12:23:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 5017fb3f-3d0d-397d-a595-3d8969f60164 | -12.37885 | -47.32677 | 2025-06-04 12:23:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| ef143c16-f01d-3ff9-9a99-9dd709751cf0 | -8.74987 | -49.77549 | 2025-06-04 12:23:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| ed71632c-9f15-3302-8f71-19ea47ab393f | -12.23526 | -44.57928 | 2025-06-04 12:23:00 | TERRA_M-T | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f81117c8-388a-3055-ad95-3760b196905f | -8.8052 | -47.1703 | 2025-06-04 12:23:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 87bf33c8-f723-32e0-9f5e-e9dd1af56995 | -8.46043 | -46.50459 | 2025-06-04 12:23:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8baf76e5-6343-33c7-805f-6167d27e5848 | -10.04923 | -49.65781 | 2025-06-04 12:23:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 0748e095-167c-35ab-a62c-c758b2b5db0e | -12.37 | -47.32549 | 2025-06-04 12:23:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 29fc778c-1c05-3f8b-b520-f968d6394dbb | -8.95583 | -47.27811 | 2025-06-04 12:23:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2d823eb8-4441-3747-9d26-d800d35eae55 | -11.91034 | -47.45383 | 2025-06-04 12:23:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| faecbfd0-1757-3c81-9952-7d0e97348586 | -7.02619 | -43.80257 | 2025-06-04 12:23:00 | TERRA_M-T | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2fd1edca-f8ce-3c14-9790-fcca13cd7e01 | -12.72597 | -43.16177 | 2025-06-04 12:23:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 2543cb88-6f98-3dd8-8ba1-33d7093a21c7 | -8.35917 | -45.86065 | 2025-06-04 12:23:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c8b0aa6c-b434-31f4-97e6-fdafe6994780 | -7.58278 | -45.86824 | 2025-06-04 12:23:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 438801ce-d20b-3ab9-ac67-f145e1adbdfe | -8.09287 | -46.29436 | 2025-06-04 12:23:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0ab14863-1743-34dc-b306-a7abf33e1619 | -6.75055 | -44.91817 | 2025-06-04 12:23:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| d13e1f73-7975-3302-a619-d9ef260acaa7 | -6.41006 | -45.74975 | 2025-06-04 12:23:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6f53b76f-e1ed-3a43-92bc-1be78f88127d | -11.80766 | -43.7947 | 2025-06-04 12:23:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 502c81a0-b095-312b-bfca-11389fdd4aba | -8.90076 | -49.32385 | 2025-06-04 12:23:00 | TERRA_M-T | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| b8dc7d94-a80a-38e8-8713-bb1c80b3bded | -6.97628 | -42.9012 | 2025-06-04 12:23:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 19ddc44e-4d8c-315c-82d1-896fe8d85470 | -9.21873 | -50.46634 | 2025-06-04 12:23:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 3e6744e4-a2d7-395d-b38e-ade6a640fbc3 | -7.23957 | -44.78084 | 2025-06-04 12:23:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a1055894-336d-38e9-a399-2e549c3b1a90 | -8.60535 | -51.53823 | 2025-06-04 12:23:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| ecebe9f1-7a92-3c4e-b919-3ef3cbc85546 | -11.80921 | -43.78288 | 2025-06-04 12:23:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 7aaa8d5c-532c-33a9-8683-a1910abbb45a | -9.45124 | -47.24021 | 2025-06-04 12:23:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d23aa2a1-1908-3ea2-8674-2d3f7c1a2218 | -11.83523 | -51.29332 | 2025-06-04 12:23:00 | TERRA_M-T | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| cd989530-1d3c-3951-9903-30d46bbc04e3 | -11.83732 | -51.28007 | 2025-06-04 12:23:00 | TERRA_M-T | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 139d605e-0826-36f6-9d94-f11461d3e8f4 | -7.2632 | -47.12522 | 2025-06-04 12:23:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 40a49e13-0ba3-3c09-8d68-cbfc606282bf | -8.90439 | -50.04035 | 2025-06-04 12:23:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b16ac60b-388e-33ef-af17-890c029980e5 | -7.90148 | -50.35987 | 2025-06-04 12:23:00 | TERRA_M-T | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| c95c2620-bfd8-32c6-af8f-40ae0887f1fe | -8.09414 | -46.2855 | 2025-06-04 12:23:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| e95f6236-c079-3670-a08b-3f8d58f71ab4 | -7.24089 | -44.77145 | 2025-06-04 12:23:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| fb3dd93b-55da-3257-b850-af535a960cc6 | -6.97471 | -42.91266 | 2025-06-04 12:23:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 7a68b077-b08f-3d37-ae38-a74f3185d688 | -12.84973 | -44.8689 | 2025-06-04 12:23:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2eb914b9-fb06-3439-87cd-55461c19e6a7 | -9.03007 | -49.95629 | 2025-06-04 12:23:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 93800499-0d24-329d-bbcf-9128c655bb29 | -7.14902 | -44.0382 | 2025-06-04 12:23:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d9e80863-df9a-3e38-96a6-38b7e483c83e | -9.53148 | -46.75018 | 2025-06-04 12:23:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a0926189-6e3f-346a-8d9e-cf12ab2b64ad | -6.9647 | -42.9114 | 2025-06-04 12:23:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 46.5 |
| 8c0f9e9d-84da-3a2d-8af1-30caa8e6f032 | -6.96628 | -42.89983 | 2025-06-04 12:23:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 38.4 |
| 147bd809-9e94-33ff-9b6d-79e14fae9caf | -10.70743 | -48.78103 | 2025-06-04 12:23:00 | TERRA_M-T | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b4b12f96-c4fe-3e04-b914-d65585428333 | -7.29754 | -43.45623 | 2025-06-04 12:23:00 | TERRA_M-T | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| b4fe2c83-486b-385d-b7b7-61f6269320d6 | -6.62655 | -49.72477 | 2025-06-04 12:23:00 | TERRA_M-T | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 5c6c6b0e-a590-3871-b587-608cd6369898 | -7.43674 | -45.78988 | 2025-06-04 12:23:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| fb03730a-f8a4-3335-b8af-0d269e368d38 | -7.58405 | -45.85936 | 2025-06-04 12:23:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f377b5d3-4675-363e-bb5a-4d7b289a6b08 | -9.56894 | -46.92836 | 2025-06-04 12:23:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| f78f540d-d9e0-32f7-9c1f-7f4e7c2dc987 | -8.03617 | -49.61728 | 2025-06-04 12:23:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 2618e070-d0fb-3d41-ae9e-e902178081eb | -7.89628 | -46.19081 | 2025-06-04 12:23:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b6e42387-17c8-30d6-ba23-997fbdc5f795 | -12.85929 | -44.87016 | 2025-06-04 12:23:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 1772a005-c411-3a5f-b95a-4fa268bdf1af | -9.25316 | -47.83131 | 2025-06-04 12:23:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 1ad61e00-196b-32a0-99f4-e14fa6f82d5b | -7.01418 | -44.61637 | 2025-06-04 12:23:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1b4fb395-7d01-342a-a912-42b03dc0be27 | -7.36628 | -46.85504 | 2025-06-04 12:23:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1b116608-6f27-37df-a7e5-db8411e3033d | -9.52264 | -46.74892 | 2025-06-04 12:23:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3344e03b-148f-3a4a-a86f-ed0419da6fc9 | -7.01551 | -44.60693 | 2025-06-04 12:23:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 5400d295-f8bc-3a3d-9da9-968904ca388d | -8.07131 | -43.11087 | 2025-06-04 12:23:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 4bcfa365-ef84-3679-83c7-e4bd20d825d8 | -16.47262 | -45.01126 | 2025-06-04 12:25:00 | TERRA_M-T | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 12c57a89-5068-3764-86db-6771ad69d8f4 | -16.23202 | -43.59799 | 2025-06-04 12:25:00 | TERRA_M-T | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 87aaa57b-3bac-368d-a337-bc19f4b8e516 | -15.65537 | -43.64428 | 2025-06-04 12:25:00 | TERRA_M-T | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 1ea9beab-660b-3671-9b52-ae92a8dca8e6 | -14.71659 | -45.09274 | 2025-06-04 12:25:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 60d61333-9d38-3c34-9269-592eff4b549a | -16.47414 | -44.99968 | 2025-06-04 12:25:00 | TERRA_M-T | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| a66deb69-9414-3c0d-9296-9ac6f098bc82 | -13.47791 | -46.80272 | 2025-06-04 12:25:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| bc671815-3b8e-3637-aa43-f043a42b9a43 | -16.47431 | -45.00559 | 2025-06-04 12:25:00 | TERRA_M-T | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 29.8 |
| b2f019c4-58e9-3749-b94f-121400d32633 | -13.6503 | -45.42534 | 2025-06-04 12:25:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 36e9ad9c-edeb-3d2e-9450-4f9931bfcb16 | -16.34473 | -43.51595 | 2025-06-04 12:25:00 | TERRA_M-T | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 84702cbd-88b2-36a8-aeef-c6312af89dbf | -13.69621 | -45.27004 | 2025-06-04 12:25:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 24.7 |
| d11498f6-534e-3f4e-82d9-8b679dec90d6 | -16.47286 | -45.01715 | 2025-06-04 12:25:00 | TERRA_M-T | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 4a857326-fa9f-3648-9c98-7d9ae8f553da | -13.69484 | -45.28041 | 2025-06-04 12:25:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cdd309fa-a314-31e8-a3c0-4dfd824a1e1d | -12.35916 | -52.48151 | 2025-06-04 12:25:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| b026e3f0-8f9e-3035-9e29-86b93d5c350c | -13.91445 | -54.65275 | 2025-06-04 12:25:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 785a9fb2-7504-3f62-b58b-ff824f5c7b80 | -15.65368 | -43.65815 | 2025-06-04 12:25:00 | TERRA_M-T | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6fac20a0-c4df-33a2-bc85-b04608255a8b | -14.71913 | -45.0994 | 2025-06-04 12:25:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 79020ce7-fedd-3f9c-bc25-1515ecd109e6 | -15.27239 | -51.47228 | 2025-06-04 12:25:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 521cd48a-8a5e-37da-98c6-feee86296e1d | -13.4792 | -46.79354 | 2025-06-04 12:25:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 01fb9db3-7bd4-3d9c-916e-55c7c367771f | -15.76109 | -48.23835 | 2025-06-04 12:25:00 | TERRA_M-T | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 310c2f31-26dc-3d71-8c7e-10d66e529bcb | -16.02876 | -43.67457 | 2025-06-04 12:25:00 | TERRA_M-T | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 3ad915ef-bf5c-35bc-864b-146a03956d51 | -19.01296 | -53.49333 | 2025-06-04 12:27:00 | TERRA_M-T | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5e0df391-c090-3112-a6ac-89145e754c5b | -17.20625 | -47.65947 | 2025-06-04 12:27:00 | TERRA_M-T | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8561cf83-bf0b-3887-b50a-870a4aca9559 | -17.25973 | -47.07895 | 2025-06-04 12:27:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| bb95d967-8459-37d2-bc73-8a7088b573fb | -17.20756 | -47.65017 | 2025-06-04 12:27:00 | TERRA_M-T | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 67532fe4-9ef5-3368-aa9c-a4d8a901bb1a | -17.25841 | -47.08855 | 2025-06-04 12:27:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 6a3232f5-9775-3546-ad28-148b06a4e7b3 | -19.01549 | -53.47861 | 2025-06-04 12:27:00 | TERRA_M-T | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 004b7d4b-8d92-3fa9-b8ed-75ade3af173b | -17.25069 | -47.07768 | 2025-06-04 12:27:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ee631366-3a76-3a75-92fa-d6f1650e84d6 | -19.78704 | -47.83792 | 2025-06-04 12:27:00 | TERRA_M-T | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 265906c1-7812-31ac-8f65-7260036f44bf | -18.07524 | -44.50836 | 2025-06-04 12:27:00 | TERRA_M-T | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f3674b66-2f8d-3f16-a746-641df2d15813 | -18.0736 | -44.52155 | 2025-06-04 12:27:00 | TERRA_M-T | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f9d46874-32de-3c13-8085-ef8b5104cf06 | -17.24937 | -47.08727 | 2025-06-04 12:27:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 16.8 |
| dddabc47-841f-3ddd-bd95-6fd37989707f | -17.6795 | -46.83667 | 2025-06-04 12:27:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 25.6 |
| b30938d3-138e-370d-aa80-df2be537c1ce | -17.5798 | -50.08843 | 2025-06-04 12:27:00 | TERRA_M-T | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |


[Clique aqui para ver as próximas entradas](README19.md)
