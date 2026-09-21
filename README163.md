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

## Dados Diários - Página 163

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a19ed51-66ae-3788-9d2f-e76ef73dd325 | -8.63911 | -47.36553 | 2026-09-21 16:03:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 86333f70-80a3-3d39-9d2d-8d6e081fd22c | -4.20332 | -44.79457 | 2026-09-21 16:03:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 15.1 |
| b5391d72-0450-3107-90b0-78aa196971eb | -4.98654 | -36.89369 | 2026-09-21 16:03:00 | NOAA-21 | PORTO DO MANGUE | RIO GRANDE DO NORTE | Brasil | 2410256 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 94002104-47d4-322a-843e-28d356319bf4 | -3.8885 | -38.64516 | 2026-09-21 16:03:00 | NOAA-21 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| a75794b3-8fd1-3236-8f63-3ff743e2900b | -6.92118 | -38.74002 | 2026-09-21 16:03:00 | NOAA-21 | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 80973a3e-7ddb-3499-87ea-d3eaf12604aa | -6.84727 | -43.72414 | 2026-09-21 16:03:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0babc7d8-1daf-333b-81c3-c87784f83b00 | -4.1983 | -44.79097 | 2026-09-21 16:03:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f0195a2d-388a-37ba-9eef-097ea5f5319a | -7.75466 | -46.72804 | 2026-09-21 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| a9ee99eb-ffe2-301c-b767-6173f2908714 | -6.92579 | -42.9488 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 112.2 |
| d7e7667f-dad5-3dbb-880a-8f37eca85129 | -6.21512 | -35.39013 | 2026-09-21 16:03:00 | NOAA-21 | BREJINHO | RIO GRANDE DO NORTE | Brasil | 2401800 | 24 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 1f97f3eb-899e-3ad0-924b-caa3eb03b5b6 | -6.01838 | -38.43328 | 2026-09-21 16:03:00 | NOAA-21 | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 8bd6593a-1be1-3bc8-80ae-2637ae7ef8bf | -5.65382 | -43.41802 | 2026-09-21 16:03:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| f8e63b8b-7170-340d-9dfe-bb20f71675ba | -1.48501 | -49.96 | 2026-09-21 16:03:00 | NOAA-21 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 7d95e02b-9e08-3d10-8e44-4b6f1dbc8587 | -4.86524 | -43.54868 | 2026-09-21 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 87284a3e-2f9a-3b8d-beeb-8ae76a9d92ce | -6.89233 | -41.70137 | 2026-09-21 16:03:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 72.8 |
| 862edf61-e1a4-38da-9365-7f904dc70eea | -7.06028 | -43.67069 | 2026-09-21 16:03:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 8c78af1f-2e8d-312f-bfa3-80f1113996e2 | -7.40422 | -44.78561 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 31.1 |
| ae115b4b-dbd4-3d4a-bae4-6e36927917a5 | -6.92966 | -42.89076 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| a601c4f4-b00c-3ce2-8b34-c20e20b36d1a | -5.61662 | -43.3902 | 2026-09-21 16:03:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f03e9be3-2386-38cf-85bd-d37d88127852 | -5.66026 | -43.20607 | 2026-09-21 16:03:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 9795e408-0b1d-3df5-9828-9723b3ae0c14 | -3.37914 | -42.96723 | 2026-09-21 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| b7ccbeca-5324-3144-9ea5-f6042f9f6936 | -6.79453 | -43.90232 | 2026-09-21 16:03:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 33d82099-e545-3f82-a220-55b260e262e4 | -5.90073 | -45.29036 | 2026-09-21 16:03:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ba395359-9e99-3a2e-8a70-d326c0a4cacd | -4.17678 | -40.14963 | 2026-09-21 16:03:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 19ba5f56-5284-35a4-ba26-4d9089ef773e | -6.22826 | -43.74509 | 2026-09-21 16:03:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9a996c00-0b76-3cf9-840b-1937aaf4fa05 | -8.36196 | -47.18645 | 2026-09-21 16:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d5586630-7ab3-34a4-91fe-44f2c60226dc | -7.1305 | -43.09848 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| f2350853-a099-3f25-8970-e53b7d9a5231 | -3.44424 | -50.60747 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| f873c867-381d-33c7-8090-e2b3098def7a | -6.5539 | -44.9036 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| e667c9ec-b864-3aef-a84d-7f26f803eded | -4.40121 | -43.04561 | 2026-09-21 16:03:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 5cfb8b04-1a16-37e5-83fa-d1727eb843c7 | -6.37553 | -39.26836 | 2026-09-21 16:03:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 13.4 |
| e6b7ef0f-4ac1-3fec-87bb-37df416ebaca | -3.84876 | -41.70003 | 2026-09-21 16:03:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 35d766f4-3089-3122-9e74-8c4058c6bef8 | -3.33265 | -42.78029 | 2026-09-21 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| e1fc29d6-3ae0-3690-b33e-5ef794cb5db2 | -7.62833 | -46.74614 | 2026-09-21 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9c7b4127-0a70-3b11-a9ce-47a01a12b271 | -4.51306 | -44.96912 | 2026-09-21 16:03:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 57ec0900-6400-3e61-ab0d-94878d3b075d | -3.16703 | -42.9396 | 2026-09-21 16:03:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8eb11547-2348-3e61-8ac9-a5bf8e2498a3 | -5.43031 | -46.61797 | 2026-09-21 16:03:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 681afa24-39e2-3ea3-805d-aac51815511c | -6.92013 | -38.73304 | 2026-09-21 16:03:00 | NOAA-21 | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 24.4 |
| 74ba9771-5d7a-3072-97e7-0989bbdf27f9 | -8.25985 | -45.66572 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| ecb92654-cb79-30f2-8cb9-fd1756bf2768 | -5.98662 | -45.06566 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1d81947b-1b82-32bb-b042-cca16fc5fa71 | -6.55806 | -45.55333 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 948859ce-8a55-3d9f-9d95-2d3e6afd1764 | -1.75113 | -47.72744 | 2026-09-21 16:03:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| ce4020d5-92bd-313d-bbbd-b4432e91f08e | -6.28628 | -47.65771 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fabb9e54-f01a-3046-98dc-a12ba81847a0 | -7.3213 | -46.7723 | 2026-09-21 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64598f2a-8e09-35c5-913b-7565f31f9bff | -2.94815 | -51.03917 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 3a6b0f6d-55b9-30ee-b142-efcefcdb787b | -5.12788 | -42.85707 | 2026-09-21 16:03:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e7efde3c-061a-31ff-8886-b9c43dea00e5 | -5.41215 | -42.96374 | 2026-09-21 16:03:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 10.6 |
| b971d8dc-fb7f-3004-bb38-90c0594d3427 | -4.14129 | -40.61779 | 2026-09-21 16:03:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 6e45f51c-a9a5-3138-877d-e81f2ef30695 | -8.41676 | -46.87542 | 2026-09-21 16:03:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3e608bb4-6b41-34bf-9ce5-6cefc390f448 | -7.16441 | -43.01664 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| b6b7861a-3fba-3943-ab19-c0afbbc1bc83 | -5.85254 | -49.78413 | 2026-09-21 16:03:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 6ec9b465-ada1-39f8-af3b-8a40ea1d9225 | -7.63729 | -44.74354 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3e3c2e7d-d411-3088-a127-c748295bd3bf | -4.58309 | -42.94355 | 2026-09-21 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 620cf8ba-919c-3c76-b1e1-ac11646ee82f | -7.6167 | -46.12324 | 2026-09-21 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3fd2b659-77b8-3cee-aa4f-f500537cfd64 | -3.1657 | -48.0742 | 2026-09-21 16:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 027c7f66-118d-31c5-9e48-371f76e8dc43 | -6.32151 | -43.37426 | 2026-09-21 16:03:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 43ed2a90-99f6-3b17-8f7f-da9302306bcd | -6.98621 | -44.71527 | 2026-09-21 16:03:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 58678ed9-4c46-3934-a18b-ef372cfcbb74 | -6.89168 | -41.69681 | 2026-09-21 16:03:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 72.8 |
| cbd58ac5-3c6d-3533-afcf-849f206b9e68 | -5.75987 | -43.71344 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| c4edb192-a2d9-314a-b825-9b8657ec3c24 | -3.84297 | -41.69963 | 2026-09-21 16:03:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| c0c6513b-b022-3246-bc9e-baf9829ab112 | -8.45212 | -47.65037 | 2026-09-21 16:03:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e95bb7c9-bf05-3049-9f1f-cfd3374c1c70 | -6.24635 | -47.65239 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 215549f8-a573-350f-b0ab-c8dba6bbce0c | -6.8561 | -44.5749 | 2026-09-21 16:03:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 21287a85-74e4-385c-86e1-80919574cf07 | -5.38657 | -48.9574 | 2026-09-21 16:03:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| fe043498-cd9b-34ae-a15d-6af5d08a8b0b | -6.99505 | -43.37001 | 2026-09-21 16:03:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| f496fe4b-5588-3c09-9f27-566bbc716064 | -8.4349 | -45.8249 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d888a4f8-0764-3d7c-b759-f2b4136a9e9a | -6.2284 | -45.42788 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 41209de6-6384-3698-8011-746bdb991bce | -2.32613 | -45.76666 | 2026-09-21 16:03:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e364dd4b-bd02-3009-bd9d-0ac4d988ad23 | -3.84359 | -41.70374 | 2026-09-21 16:03:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 5e85699e-39ca-35b8-955c-942252e52332 | -7.37013 | -44.70883 | 2026-09-21 16:03:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6d198ca6-4559-3aad-b940-fb341382fd88 | -7.25247 | -39.2255 | 2026-09-21 16:03:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 89c9ad33-760d-3bc5-a3bb-5bb1e7438b2d | -6.81337 | -43.72868 | 2026-09-21 16:03:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1c19ba3-e66a-37b9-b842-a813bcdcc3bc | -7.2371 | -48.27165 | 2026-09-21 16:03:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0a34781d-1c72-3875-a380-ac4624a2687c | -5.61245 | -43.39156 | 2026-09-21 16:03:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 954bb71e-42cc-3fe3-a2bc-7248e176f0dd | -3.49254 | -48.95885 | 2026-09-21 16:03:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 12210049-bf19-38ab-a451-1bce1a86a7bf | -7.09632 | -42.0731 | 2026-09-21 16:03:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 19.7 |
| 37bd9e1c-9b73-3609-a075-b4f710dfb701 | -6.50471 | -45.24751 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f07c83a8-764d-3967-821d-d362c704173b | -6.87982 | -41.70611 | 2026-09-21 16:03:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 72e6dc22-3642-36d4-a14e-8442d73a26bd | -1.65721 | -45.0237 | 2026-09-21 16:03:00 | NOAA-21 | BACURI | MARANHÃO | Brasil | 2101301 | 21 | 33 | nan | nan | nan | Amazônia | 15.6 |
| d0dd2c8b-2507-3495-bb46-e13bfe772fdd | -5.82662 | -47.79538 | 2026-09-21 16:03:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 336fc4df-13ca-3085-96f5-fed37f66146d | -4.95353 | -45.15413 | 2026-09-21 16:03:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 479aaa14-f5e4-3544-b5ef-09013bf0845a | -7.40968 | -44.8243 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 75ee7499-53e5-3657-ad51-6241bf79d742 | -5.67829 | -43.41463 | 2026-09-21 16:03:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8194e79c-f90d-377f-bf5a-32a54e11ed6d | -6.2291 | -45.43299 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 5eaf282f-ddea-3b3f-9423-440f74ccbf2d | -8.4853 | -47.01735 | 2026-09-21 16:03:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| c28b8244-a103-3fc7-9721-463a611870af | -6.93623 | -42.90772 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| f85c4367-09d5-36d0-84c8-ffca4984ad64 | -7.06005 | -43.67082 | 2026-09-21 16:03:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 8819f062-75e9-334d-9047-9c9f84322e4f | -6.88048 | -41.71058 | 2026-09-21 16:03:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 689d47d3-2e91-32bc-b553-854c9ad035d1 | -7.81254 | -44.92976 | 2026-09-21 16:03:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1ba70f01-fbf9-3634-b93e-86e5fd0a7c9f | -5.68184 | -43.41044 | 2026-09-21 16:03:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 66bc2b9e-9e8a-347a-9f64-dee6c98f82f7 | -6.16297 | -47.70148 | 2026-09-21 16:03:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f4c990e3-4df5-3833-9d8c-dd19f5da8146 | -7.20623 | -44.08595 | 2026-09-21 16:03:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6f4c1a9e-72e5-3125-bdcd-fbe1a43ae640 | -6.28135 | -47.58206 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 447f65b5-028d-3ffa-a9af-0a08d2736f97 | -7.58171 | -45.38722 | 2026-09-21 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| ac763b96-2717-378f-8c1f-f7df5f706c6b | -8.51226 | -47.42766 | 2026-09-21 16:03:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6d2d709b-e723-3549-bd76-1aa9a4f323bd | -6.36878 | -44.45723 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| df80b45f-ab18-3c79-bd3a-781ddce096f9 | -6.55847 | -44.90301 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 0cfcb98d-21f3-3e7a-aab4-33435b5258cd | -6.84294 | -45.56142 | 2026-09-21 16:03:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fca7df53-8da2-363c-b0e2-601da6f9a872 | -7.16765 | -37.71788 | 2026-09-21 16:03:00 | NOAA-21 | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 21.9 |
| cd223d11-c852-37e1-baeb-aa6c3aa17ca6 | -4.1373 | -40.61456 | 2026-09-21 16:03:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 17.6 |


[Clique aqui para ver as próximas entradas](README164.md)
