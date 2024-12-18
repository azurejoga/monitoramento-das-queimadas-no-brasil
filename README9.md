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
| 5f1f9702-15d7-3b15-b2c2-444888114322 | -3.02437 | -45.23476 | 2024-12-18 04:01:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| cf74b6f1-7973-34cc-8054-8ee747b30594 | -6.14297 | -43.91741 | 2024-12-18 04:01:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 707d8290-1c51-33fd-94a4-a353004a01e9 | -6.97721 | -43.56022 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 8b64bf25-ed74-38da-8fd7-913658492f13 | -4.52671 | -44.05 | 2024-12-18 04:01:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 67b66823-6f24-3b2f-ab74-ee552849c044 | -7.90524 | -35.23278 | 2024-12-18 04:01:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 30.9 |
| 738f8266-8201-3530-9ca6-b47f76ed01f4 | -6.97118 | -42.82978 | 2024-12-18 04:01:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b8bdaf2d-68df-3b97-9181-8b86033437a0 | -3.07329 | -40.05366 | 2024-12-18 04:01:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 51116d49-97b4-38c5-bf4e-0eda39d0ea6c | -4.18775 | -44.03276 | 2024-12-18 04:01:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b28570ef-0408-3f31-9fe4-5c7925a1407a | -4.00673 | -43.75512 | 2024-12-18 04:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 79d9d496-346a-316f-afbc-b35e4d78c669 | -1.62577 | -45.85376 | 2024-12-18 04:01:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5b1a2fb2-013d-34b3-918d-bd7865a3218e | -5.94476 | -43.77455 | 2024-12-18 04:01:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 81bcce03-9402-3dfc-a04f-d47a6609e90e | -6.66782 | -38.58851 | 2024-12-18 04:01:00 | NOAA-21 | TRIUNFO | PARAÍBA | Brasil | 2516805 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5f111c50-91bb-3629-aa73-18e864026b12 | -5.98994 | -41.56099 | 2024-12-18 04:01:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3e4cc3e6-30dd-3830-81d7-1da7e14513ad | -4.39533 | -44.10284 | 2024-12-18 04:01:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9f0bc8d-f759-3e0f-82ed-052cf0422473 | -3.24712 | -46.87688 | 2024-12-18 04:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9d38e239-26af-3cb9-89ab-de5a7610bdcf | -2.88609 | -40.46795 | 2024-12-18 04:01:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8bcca519-2140-3d76-91db-523fc0446937 | -3.24691 | -42.42005 | 2024-12-18 04:01:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6bbbeb5a-c872-3c1a-a773-7ff1d5fdcc3c | -7.84603 | -35.20944 | 2024-12-18 04:01:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 4cef7456-3ed9-300b-97f9-72d219d9ef8e | -4.54418 | -43.29417 | 2024-12-18 04:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 14c40a09-3ec3-362c-833c-d5d24ed299b8 | -7.78051 | -35.05613 | 2024-12-18 04:01:00 | NOAA-21 | ARAÇOIABA | PERNAMBUCO | Brasil | 2601052 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 8435a27d-4ba4-31e1-a335-dab2beded7f3 | -5.8954 | -42.3292 | 2024-12-18 04:01:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 42fe673d-1ab8-3c25-9c9b-e0d9f3606a5b | -7.16445 | -35.0924 | 2024-12-18 04:01:00 | NOAA-21 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1df53bb0-e023-35f5-a497-26a32461b76e | -7.92682 | -35.19894 | 2024-12-18 04:01:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5a495e7f-f85a-3d74-aed7-cceaa26a429e | -5.9278 | -48.06869 | 2024-12-18 04:01:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ffe71fdb-aeb5-31f6-90c2-07a5e91861d1 | -6.97948 | -43.56924 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 999baf77-4121-369b-9893-85f2e224caa2 | -6.96859 | -43.5675 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 38671288-9715-332c-9ab7-feae0088e2c9 | -6.97818 | -42.83092 | 2024-12-18 04:01:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 36f67b57-003b-3974-a65d-d91178d10d77 | -6.97602 | -40.63464 | 2024-12-18 04:01:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cb09fcfc-de50-3605-a831-87d794eadd7c | -5.33861 | -41.22276 | 2024-12-18 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 43686cec-b302-3760-896d-10d6265c6d71 | -1.70695 | -45.78203 | 2024-12-18 04:01:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| dbf89331-71ba-3bbd-b2b1-a304c7f1c0ce | -4.14923 | -43.56691 | 2024-12-18 04:01:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 992844f0-31e5-3dfc-8abc-f61a99ec8fa3 | -6.97271 | -40.63412 | 2024-12-18 04:01:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 98ac70f5-d470-3b61-b822-a430f4a78ec5 | -4.8535 | -41.38213 | 2024-12-18 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e3f3b322-7cca-375d-af4f-ca923fbc08b1 | -5.94058 | -48.05347 | 2024-12-18 04:01:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36fcb7ad-7307-3908-b91a-65bc23e4e78a | -6.44062 | -40.62094 | 2024-12-18 04:01:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2926fadf-42e0-31cc-b5e2-a2a380baff50 | -2.92332 | -41.4612 | 2024-12-18 04:01:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4009a243-6302-3c40-87c7-7ab08ef1fb5f | -0.75176 | -47.75854 | 2024-12-18 04:01:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d9e5f7db-250d-393a-8bd2-73b42f00146e | -5.5775 | -42.94337 | 2024-12-18 04:01:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 57062398-f3c2-3904-8183-252384c9c4a3 | -5.71684 | -43.4666 | 2024-12-18 04:01:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5fc53bef-4752-3e5f-9aeb-8115dec5d5ea | -7.90063 | -35.23587 | 2024-12-18 04:01:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 2fba310a-8b65-3ae3-8337-f2e64bebcd1b | -6.67177 | -38.58539 | 2024-12-18 04:01:00 | NOAA-21 | TRIUNFO | PARAÍBA | Brasil | 2516805 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2437a23d-e8dd-3af3-b1ad-f9d1d5586e2a | -5.57342 | -45.15853 | 2024-12-18 04:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4074167a-088e-3d5a-9382-911082fd9944 | -7.2541 | -40.16183 | 2024-12-18 04:01:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| aa6d87db-440d-3a0d-befe-97fe6f873951 | -5.94457 | -48.05969 | 2024-12-18 04:01:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 51e8d07d-c9f9-3e38-9014-0ce14e518bba | -6.96633 | -43.55847 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 46251e76-cb93-335c-bbc3-ba2746a86705 | -4.78196 | -42.68249 | 2024-12-18 04:01:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8c523c1d-7d52-30cf-8a4c-29c4db270f6a | -5.9724 | -42.31418 | 2024-12-18 04:01:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f80cdc59-4d31-3888-88a3-9b7895cbabef | -3.66365 | -42.03434 | 2024-12-18 04:01:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b29ec477-de40-33ec-8579-586e7e66167c | -4.4846 | -42.86941 | 2024-12-18 04:01:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e88b8c9-9aaf-33a6-a2b5-57d148a6e73b | -6.97433 | -42.81015 | 2024-12-18 04:01:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7b646a34-35a1-3290-983f-90c221df2312 | -6.98537 | -43.57893 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8c2bad2b-3ca5-3ab7-b051-6f42d8c92575 | -5.9492 | -43.77069 | 2024-12-18 04:01:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa083cfc-7d98-3d30-8472-01e46f07eaef | -6.98515 | -43.55715 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 41665d22-6656-3744-8e09-1c858bb5230e | -4.28312 | -43.05374 | 2024-12-18 04:01:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 326c4109-0b01-36c9-b9bd-1791489b0576 | -4.12217 | -43.5672 | 2024-12-18 04:01:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d31a910-a32c-39c2-b679-3a6fbe8f2e85 | -5.93767 | -48.07023 | 2024-12-18 04:01:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46d5ae75-3dbb-3b17-9a19-0eac3825e9b5 | -6.00174 | -41.57386 | 2024-12-18 04:01:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3dd03f7a-918a-3560-a3b7-47bf31e489a6 | -5.99206 | -43.48172 | 2024-12-18 04:01:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| facdbd54-5df9-31e0-b523-57ac4178f453 | -8.14905 | -38.64995 | 2024-12-18 04:01:00 | NOAA-21 | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 18fed934-ba9e-3b37-9c32-74814d39a8bf | -4.48821 | -42.86998 | 2024-12-18 04:01:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3fb38874-295f-3342-974a-738be80b3a2e | -6.9729 | -43.56387 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 676b0ee1-4fcd-317c-ba95-83533e98cfdd | -4.54347 | -43.29851 | 2024-12-18 04:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 357941e3-6df2-3c04-81f9-84f938887d94 | -4.11432 | -43.22042 | 2024-12-18 04:01:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a8e814c0-aa73-3d50-8b70-47b147688962 | -6.99037 | -43.57099 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7233c299-608d-3fa5-ba32-565d2dfbcd83 | -6.9627 | -43.55789 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3444a432-4c93-3056-95e8-b08d9c954977 | -4.90439 | -42.0748 | 2024-12-18 04:01:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cb5a6ff4-d4d1-3164-8f88-d02dbd46de30 | -5.99499 | -41.57285 | 2024-12-18 04:01:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 20ea72d2-2a6b-30b3-ba5f-f980f12aeda4 | -5.98802 | -41.66098 | 2024-12-18 04:01:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4be53061-475e-3f05-a721-19a7ef888fc8 | -4.16613 | -43.96984 | 2024-12-18 04:01:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a858fe9-adff-3a0b-a83d-d83d63a144c7 | -5.89478 | -42.33303 | 2024-12-18 04:01:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b777f9f6-38f7-36c8-a96a-23bde97b8f03 | -4.83083 | -38.37626 | 2024-12-18 04:01:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cc96f464-6f51-3842-930a-e120c85a8e27 | -1.62962 | -45.85166 | 2024-12-18 04:01:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d5aa809f-baf3-3ecb-9fa6-bfaacb371602 | -1.62294 | -45.86465 | 2024-12-18 04:01:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8985af1d-e1c3-309d-ba62-643a29c1ea34 | -1.62124 | -45.85304 | 2024-12-18 04:01:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92621e28-41fc-3781-b0c9-3204678485ed | -5.73253 | -39.53618 | 2024-12-18 04:01:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 614fb3b7-31bc-3f33-a91b-f4edfca9215f | -6.9884 | -43.56509 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1b9184ff-9a89-35fe-b54d-86b0d73dc101 | -5.70994 | -41.40959 | 2024-12-18 04:01:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d6c85c0a-596b-3be2-adfe-9f363cfe9bfa | -3.07052 | -40.04968 | 2024-12-18 04:01:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4a145755-25e0-310c-8d1f-73b974eea094 | -5.98406 | -41.6641 | 2024-12-18 04:01:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bd2540e4-408c-31ab-ad5e-a97398ff6716 | -5.04428 | -43.21879 | 2024-12-18 04:01:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 269c42a5-5130-3837-b974-06c58f04cc9d | -5.4116 | -36.78207 | 2024-12-18 04:01:00 | NOAA-21 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f87eecdf-84b1-3725-a991-cccaafd2bf19 | -5.93273 | -48.06947 | 2024-12-18 04:01:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fecb5e3d-4988-3620-a569-b2502b59acdc | -6.97811 | -43.57775 | 2024-12-18 04:01:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 789a4a91-3d98-3e87-b27a-71cccff828f8 | -7.15617 | -46.69469 | 2024-12-18 04:01:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 56b5aba6-08d5-3564-85aa-c5c8dba6ec4f | -6.97222 | -43.56808 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| f81ce019-8701-32c4-8293-976de715f1cd | -5.93963 | -48.05894 | 2024-12-18 04:01:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| e1e9c50d-b3ee-3d6e-b1bf-3064f2cf321d | -1.62366 | -45.86008 | 2024-12-18 04:01:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ea07d3a-e446-36e8-95c8-333b9c4d9bda | -6.08329 | -48.20739 | 2024-12-18 04:01:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c629a9c6-e39e-351f-b64a-6c30e1dab80b | -5.99275 | -41.56507 | 2024-12-18 04:01:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 72f220a3-f74c-37f4-8942-e1877f69a7b0 | -6.98488 | -43.58622 | 2024-12-18 04:01:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a5805955-e4c2-3aba-9046-6f6c2994e45a | -1.62508 | -45.85095 | 2024-12-18 04:01:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6b64b753-2838-3bce-bb3e-42e4ca49d335 | -7.15544 | -46.69895 | 2024-12-18 04:01:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d208e64b-aa2d-3b27-912b-cb32664d9c70 | -3.83437 | -46.68296 | 2024-12-18 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a84a7dc5-c62f-3cb4-9af6-cae5e477f1c1 | -4.87382 | -41.38516 | 2024-12-18 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fa852f0a-3b2d-3ee7-9270-dce0e172d331 | -6.98084 | -43.56081 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 79ec48be-1190-34aa-9975-42560aa9d42f | -5.22888 | -36.81008 | 2024-12-18 04:01:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 69d648f9-4115-395e-8514-9a30c304659a | -7.90116 | -35.23217 | 2024-12-18 04:01:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 30.9 |
| 74219a0b-8a8b-305f-a453-0a218770ce45 | -6.97448 | -43.57717 | 2024-12-18 04:01:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0d07d274-ffa3-3495-bd77-c52ee70b4955 | -6.98174 | -43.57834 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ffa2851f-8b69-3233-8cb4-61f5391c0e91 | -2.57426 | -47.94707 | 2024-12-18 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README10.md)
