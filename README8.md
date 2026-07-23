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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e8d4b54-aa60-3ccc-a779-38ebe21d663a | -11.80234 | -47.10845 | 2026-07-23 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b809adbf-bef7-3437-8a44-d7edfe5b4654 | -7.89043 | -46.90237 | 2026-07-23 03:49:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c1a4ef8-0703-3a10-a46d-940d7e7f4b80 | -11.94242 | -43.39393 | 2026-07-23 03:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0bf27e98-9f1d-3f0f-9cf5-54e55560c44a | -12.10987 | -44.93772 | 2026-07-23 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46621340-dd98-386a-89e5-2a368395ece5 | -7.88489 | -46.90149 | 2026-07-23 03:49:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0a285b6-e0b9-3a04-ab56-7cccbe30c49b | -12.32396 | -46.73953 | 2026-07-23 03:49:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eba89472-c4d9-3e31-90b2-09bf46cd4d93 | -11.3918 | -47.47831 | 2026-07-23 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 869b299c-80d7-353a-a17d-1f27f229580e | -11.78238 | -47.09982 | 2026-07-23 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 4007e93b-8709-3043-9514-da41696f3bb3 | -6.30905 | -43.65804 | 2026-07-23 03:49:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4c589ae0-646f-3134-bd90-8d206f4a9956 | -7.2126 | -39.00298 | 2026-07-23 03:49:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7483c4bc-c5f9-3566-84e8-f924b17160ff | -12.84523 | -44.38136 | 2026-07-23 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d4d31abf-5198-386d-955d-2bf4d4771d53 | -11.68888 | -50.36412 | 2026-07-23 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b3274a83-9d9c-35ba-9df1-74e46155dc4e | -7.01267 | -45.42058 | 2026-07-23 03:49:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7dd9e68b-b79a-3f1c-a62b-db0dfdc89b64 | -11.69016 | -50.36323 | 2026-07-23 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2f99fbc2-edec-3c3d-b7c2-989fda0cf8c8 | -11.57857 | -48.39841 | 2026-07-23 03:49:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f76ff833-312c-34e9-a105-b71d1b64dbde | -7.68685 | -41.24268 | 2026-07-23 03:49:00 | NOAA-21 | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 1032b55b-a7ef-31f0-8578-75c1c76cb105 | -12.40429 | -50.39388 | 2026-07-23 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 582b3437-0cb0-3b2f-9107-b6083cb7522d | -11.77928 | -47.11634 | 2026-07-23 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0175d053-7f14-32f1-8c8d-6b81bd3bd195 | -11.79841 | -47.10078 | 2026-07-23 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 68fe7092-e4f8-345e-868e-9c7173d2e11e | -7.73251 | -44.55681 | 2026-07-23 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e59f0542-425d-3532-9041-469e29a4fd97 | -12.66313 | -48.21848 | 2026-07-23 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46c267ed-cb96-3698-86f5-e93c26f33912 | -6.49508 | -42.21982 | 2026-07-23 03:49:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 5680ecc0-a0d9-3bd5-8f46-528c22eb3eb3 | -6.3045 | -43.65722 | 2026-07-23 03:49:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5b278ef-dec1-36e1-ae29-959bb2a19a86 | -12.85094 | -44.36502 | 2026-07-23 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef9ad9c4-3907-3ba4-9272-a8023ff577f7 | -7.01391 | -45.85272 | 2026-07-23 03:49:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0bc60d21-c598-3a09-ae81-d32b29890f4d | -11.77716 | -47.09878 | 2026-07-23 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| c55d636c-ff67-3458-b4e5-6beffb318581 | -11.78114 | -47.10643 | 2026-07-23 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 898cb396-68e3-3471-b5ae-8f32dbdbb90d | -11.67715 | -50.35606 | 2026-07-23 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| c7bc5e20-b1ac-3404-bfe8-8b0e26240579 | -6.49856 | -42.22429 | 2026-07-23 03:49:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| aa19ae08-b9da-3301-994a-7be3eb7f7b4e | -9.55935 | -40.34032 | 2026-07-23 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 8a1dea97-c169-3470-82c7-ff931df9d2aa | -11.7968 | -47.10962 | 2026-07-23 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 65a74c30-d440-3ee6-a55b-2e4720b98344 | -10.66164 | -46.60062 | 2026-07-23 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fffc5ad0-0bac-3c10-b3fc-b28849e6066f | -11.6942 | -50.37084 | 2026-07-23 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 47da79e7-6ab7-3e7a-9c76-c7df4f5aa2a1 | -11.69637 | -50.36002 | 2026-07-23 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 51fb1cab-28a5-3eda-8e50-cbc11f66b728 | -11.94361 | -50.37413 | 2026-07-23 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 67fe6fe7-e984-36e5-afbd-04efae9b1c73 | -11.95275 | -40.60093 | 2026-07-23 03:49:00 | NOAA-21 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2d6b3d50-c7dc-302f-ac1b-09dd8ac599b8 | -11.68996 | -50.3587 | 2026-07-23 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2526bb7a-fe5c-33dc-b7d3-659baa0db27b | -12.14179 | -48.25945 | 2026-07-23 03:49:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3e07921-f72e-3fa8-8d16-d3b54709f1b8 | -6.49378 | -42.22749 | 2026-07-23 03:49:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 9b00e798-4f8f-3dd1-b7eb-912ceb44bcd1 | -12.84951 | -44.38213 | 2026-07-23 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 57ec82ca-dbee-37a4-869f-ef1397be1174 | -11.8134 | -47.3348 | 2026-07-23 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 712366f5-c622-32ea-91ad-84dceb55eafb | -9.52592 | -47.13076 | 2026-07-23 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3eb4ab05-421c-3168-acb2-578c7654dc24 | -11.70827 | -50.37251 | 2026-07-23 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c17832ac-cf7a-3cde-9ede-03f43d2bb890 | -6.49443 | -42.22363 | 2026-07-23 03:49:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| d6d35628-1544-3db9-8d85-182237597516 | -11.78176 | -47.10312 | 2026-07-23 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| f740c604-d9b4-3f6a-8907-afa40edabecd | -7.73159 | -44.56197 | 2026-07-23 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6e545789-25fd-3845-80c4-c4a4d3c2fb87 | -11.81872 | -47.33577 | 2026-07-23 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1676b347-016b-33a8-bd05-59f678fff452 | -6.49311 | -42.23137 | 2026-07-23 03:49:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f54662a1-41d2-3d07-9dac-addea692851b | -6.41742 | -43.06811 | 2026-07-23 03:49:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9c5440b-28b2-3a3e-bc07-14a9d28e5178 | -11.59504 | -48.0284 | 2026-07-23 03:49:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b58708d-e735-305f-ad42-919b7c0bb070 | -11.90193 | -50.38248 | 2026-07-23 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 98259ac2-c0b3-34de-bb8b-2e8f77ef83dc | -11.79777 | -47.10405 | 2026-07-23 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 82acf70f-df3d-32f9-88bd-405526220acf | -12.32454 | -46.7365 | 2026-07-23 03:49:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8f4e612-5b98-3add-9d75-aea7d3ef4f67 | -11.78698 | -47.10419 | 2026-07-23 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| c0b0446e-a4ff-348f-9666-a82b618b3a4d | -11.95968 | -50.36066 | 2026-07-23 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b2ec159d-ff47-387a-a89a-22c49a5d5a9f | -11.79712 | -47.10738 | 2026-07-23 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 95addabc-2649-3a80-acea-8a435098de22 | -12.84787 | -44.38165 | 2026-07-23 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e4664bcb-8f08-3b94-8c7a-08d0b4b0ffc6 | -11.80264 | -47.10735 | 2026-07-23 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 597bdd39-fd13-3726-9784-e23ca18ce2c7 | -11.7876 | -47.10089 | 2026-07-23 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 222554d0-9ba6-355a-a2db-5f300d62ab50 | -12.10801 | -44.93832 | 2026-07-23 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7058f224-65a6-3f54-8447-6149facee28d | -7.00761 | -45.41958 | 2026-07-23 03:49:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e518dc7-7114-3fa9-8baf-ce7c1219ddbb | -11.88952 | -43.82958 | 2026-07-23 03:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 760f4472-6b91-3974-a4dd-c8b2dcf41369 | -11.70186 | -50.37121 | 2026-07-23 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0033e95b-fce5-30c7-8b6d-4abb60cd9ed2 | -7.01216 | -45.42358 | 2026-07-23 03:49:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 81f07007-9c8f-3f80-929d-2f94fb96bfdd | -9.464 | -45.64398 | 2026-07-23 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7983678b-06c8-38a4-bac0-7532472517af | -9.5558 | -40.33973 | 2026-07-23 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 037e0cf1-2597-3d14-9c38-ef472c86e005 | -11.68356 | -50.35738 | 2026-07-23 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 86426d24-be27-3675-85da-2717c18cb037 | -11.69528 | -50.36544 | 2026-07-23 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2414d4b4-cf8a-3f16-b19a-0e3a2f7a95cb | -11.70702 | -50.37349 | 2026-07-23 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 49d1570b-f8fc-33f0-80be-733eaecddef5 | -11.79282 | -47.10191 | 2026-07-23 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| e1b0a76e-8ec1-34d4-97aa-542576e93832 | -11.24106 | -41.02114 | 2026-07-23 03:49:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 35d46373-0114-3c07-9736-252b5895e0d5 | -11.94203 | -43.39341 | 2026-07-23 03:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5adcd68b-32ea-3d3a-b8bb-d6495b6613e5 | -12.39903 | -50.38728 | 2026-07-23 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89791784-17f3-32a0-bc79-01d97a96d6d6 | -11.58427 | -48.39954 | 2026-07-23 03:49:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 211c581f-1c3e-39ce-b122-b0fd4a0b1e65 | -11.38707 | -47.47373 | 2026-07-23 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3aa31d7e-6022-312d-a493-e08deb5595fe | -11.79805 | -47.10294 | 2026-07-23 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b4b475f5-b693-3c89-a18c-6a9cf8d70424 | -6.21342 | -49.43123 | 2026-07-23 03:49:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f853f436-9fd6-31b3-87c2-817630713a73 | -6.20677 | -49.4301 | 2026-07-23 03:49:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dc709590-f661-3fd7-9225-f247e637f835 | -11.58348 | -48.40359 | 2026-07-23 03:49:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4d4cc379-7600-343e-9ac3-63bcdb7ec7b8 | -11.9511 | -50.37007 | 2026-07-23 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1a13eb38-c8c4-3c76-b1e4-5f9a8a8f02ce | -11.79221 | -47.10521 | 2026-07-23 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| caa41e17-31da-3a35-b56e-ef3c1d1832a2 | -12.66388 | -48.21479 | 2026-07-23 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f09d681-e517-3fa6-ba0e-ae23f9f663b1 | -5.63851 | -47.10173 | 2026-07-23 03:49:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bbcdcfce-5bc5-3175-b4e6-3e0fc1b2db40 | -7.00813 | -45.41658 | 2026-07-23 03:49:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3221e8cb-b6c7-3820-98e7-3ff0aa4f67f3 | -12.66392 | -48.21889 | 2026-07-23 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4039ad1e-19b2-33fd-bd8e-9329fb92476c | -7.73138 | -47.24761 | 2026-07-23 03:49:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd8038ce-4bd5-3118-8b6f-dc817d65d281 | -6.21038 | -49.43265 | 2026-07-23 03:49:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d2d467de-1721-37ee-83cf-2f9b3e02a515 | -8.80297 | -49.37991 | 2026-07-23 03:49:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a767be7f-8146-388e-9413-f7e46f70a9f0 | -11.57207 | -48.40133 | 2026-07-23 03:49:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9cac0473-6ed6-39df-b1d0-d6afafb5b5f2 | -12.24955 | -43.57174 | 2026-07-23 03:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7c1a3e3-3326-3c21-a464-27c1de6a8dea | -11.79158 | -47.10854 | 2026-07-23 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 9f429343-05dd-3969-909b-0501abbf91ea | -11.67824 | -50.35065 | 2026-07-23 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| b57fca50-037e-38d8-bff6-c58dbcf431d9 | -12.66943 | -48.21577 | 2026-07-23 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc8a7d16-9cf6-3f50-89d0-058bc9e5a588 | -11.77866 | -47.11966 | 2026-07-23 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8e88e09-f79a-3b64-a6ed-3c954df06a23 | -11.80299 | -47.10512 | 2026-07-23 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dfb68419-0f05-3e4e-a917-623fe97802d7 | -11.91333 | -43.84201 | 2026-07-23 03:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f5633f32-e4d8-3bae-9a62-e54153216837 | -6.42249 | -43.06466 | 2026-07-23 03:49:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f2626e6-6b0f-3f26-9ec8-d15a12648658 | -11.70061 | -50.37217 | 2026-07-23 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b40af602-38f5-3c11-b0c9-7ba9c8b9a4e4 | -8.80399 | -49.37467 | 2026-07-23 03:49:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c9eba8b7-76ea-3f7a-ac0c-6a3d1a5e46a5 | -7.01371 | -45.41459 | 2026-07-23 03:49:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README9.md)
