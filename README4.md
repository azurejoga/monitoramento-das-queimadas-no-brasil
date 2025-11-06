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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 263b6b94-b632-33b5-bd08-96db08e1809c | -4.74583 | -46.59497 | 2025-11-06 00:13:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 521f245a-795f-30a1-9b24-54e27aa3a99b | -5.13826 | -41.26842 | 2025-11-06 00:13:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 3a1aa7dd-868c-305b-bc69-ce65fedfa999 | -5.64887 | -43.02179 | 2025-11-06 00:13:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| b4e96794-36df-305a-95d0-610b675df023 | -4.59005 | -43.35199 | 2025-11-06 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 531a544d-0373-3525-bd14-f940ef69bae3 | -5.68433 | -47.86638 | 2025-11-06 00:13:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 8eab8e5f-5d23-39fe-8da7-a401a9ae4024 | -5.13262 | -41.26213 | 2025-11-06 00:13:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| a8cfa59b-c328-3977-931e-d46c0666158e | -5.3036 | -41.06866 | 2025-11-06 00:13:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 8d70bf53-63d1-31ae-988b-5246e5abc445 | -7.90858 | -44.34609 | 2025-11-06 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9509d5e9-cfbf-32cf-8ebd-39dd91445d6d | -7.54523 | -45.85193 | 2025-11-06 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 311a4a11-a650-313d-be45-bec63cdbca5b | -5.46078 | -44.69718 | 2025-11-06 00:13:00 | TERRA_M-M | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 59f02b4b-544f-388c-9d08-8f258ce97328 | -9.46999 | -40.37995 | 2025-11-06 00:13:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 905c1549-eca2-3f76-9fca-714b7f0cf438 | -7.92381 | -44.3257 | 2025-11-06 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.3 |
| bc845f05-9e48-3524-ac28-2d7662c799d3 | -7.47609 | -44.54747 | 2025-11-06 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 5806e650-a84f-3d81-877c-263592cad538 | -5.36527 | -44.47913 | 2025-11-06 00:13:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0d89656c-75e8-31eb-ac24-dfd159bf61ad | -5.51079 | -41.14926 | 2025-11-06 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| e9be9115-af5a-3106-8516-40f4270c1d7d | -4.70009 | -46.52742 | 2025-11-06 00:13:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| e5ebb136-4513-30e7-9ae1-d898d93ca477 | -5.20636 | -44.00341 | 2025-11-06 00:13:00 | TERRA_M-M | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b0d43c21-184a-3cff-b07e-d03d18144870 | -7.06706 | -45.45563 | 2025-11-06 00:13:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 37061082-a41a-3a87-9c11-dd132ac87212 | -4.60603 | -43.32922 | 2025-11-06 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 8bd3fb44-3703-3470-afe7-5c59c8923f04 | -6.09492 | -41.70269 | 2025-11-06 00:13:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| cb03c2d1-1b18-35cd-8472-255608aee000 | -4.79439 | -45.13944 | 2025-11-06 00:13:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| b87c10b2-d2ae-39e0-ace5-87a38ab79474 | -4.85314 | -43.78045 | 2025-11-06 00:13:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 99b71829-50b6-3fbc-833b-ecdf9831ec1a | -5.53476 | -46.50455 | 2025-11-06 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 5d65a5f1-a5ff-3463-b24a-c45f510f9afb | -5.42877 | -40.67614 | 2025-11-06 00:13:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 32.1 |
| 51172755-cb00-305f-a8e6-4ece5dc5375a | -4.60399 | -46.56505 | 2025-11-06 00:13:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 54c46d73-5f5a-3b72-bca8-224b3966f09d | -5.52577 | -46.50581 | 2025-11-06 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 2fb30757-8901-3995-b3b6-d022b71d4621 | -5.51271 | -41.16218 | 2025-11-06 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| c6efc4e0-6bcc-34f3-ac8a-857fe76932fa | -5.45953 | -44.68824 | 2025-11-06 00:13:00 | TERRA_M-M | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 703ab233-2a08-367c-bc21-1f3a71ae5510 | -4.51902 | -44.42331 | 2025-11-06 00:13:00 | TERRA_M-M | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a653fbab-098c-37e8-a3a1-694a301d9134 | -4.58723 | -43.3319 | 2025-11-06 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 176.4 |
| fdd4021a-5df2-36aa-882b-8b5023635357 | -5.61549 | -41.08703 | 2025-11-06 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| b3bca67c-5a92-3ab2-b47f-8e667bb664e0 | -7.48741 | -44.56395 | 2025-11-06 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 30827308-6d17-3311-a664-45fbb5acf2e2 | -4.7381 | -46.60527 | 2025-11-06 00:13:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 070b07db-b0f3-39bc-bf82-39ee0b4a6419 | -7.83759 | -40.83836 | 2025-11-06 00:13:00 | TERRA_M-M | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 6645196b-205f-3eb7-b06b-0950abf42f13 | -7.17408 | -38.35713 | 2025-11-06 00:13:00 | TERRA_M-M | SERRA GRANDE | PARAÍBA | Brasil | 2515708 | 25 | 33 | nan | nan | nan | Caatinga | 55.2 |
| 6f9ab244-66f8-3ca7-a059-34ec19155685 | -5.15388 | -41.22641 | 2025-11-06 00:13:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| f2846282-f349-3d57-88e2-bd3c2bfbd63b | -3.00906 | -40.24367 | 2025-11-06 00:15:00 | TERRA_M-M | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 19.0 |
| fcb04300-288b-3453-b8b6-ca0f81248cdf | -3.44016 | -43.17195 | 2025-11-06 00:15:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d4d00e64-3f6c-396d-9695-3fb2a46bfc9e | -3.377 | -44.09916 | 2025-11-06 00:15:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 18.6 |
| af6dd5a2-f5bc-35c9-89e4-0f3c09021561 | -2.57265 | -44.93572 | 2025-11-06 00:15:00 | TERRA_M-M | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a7b1b125-c712-31e5-9baa-5ff87f166a52 | -3.98752 | -47.71279 | 2025-11-06 00:15:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| c82ef4c9-beb1-3546-98d8-b67995ad496e | -4.2754 | -45.1231 | 2025-11-06 00:15:00 | TERRA_M-M | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 6ba8c7c8-8450-309d-bb63-9ac3565650cb | -4.37661 | -48.68805 | 2025-11-06 00:15:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 01dbd623-7f99-3bfc-88d4-7174cbb35149 | -2.44916 | -49.01258 | 2025-11-06 00:15:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4401a754-7bea-38e8-a70a-de388900b7f3 | -3.78178 | -49.41774 | 2025-11-06 00:15:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8362b3a7-2cbe-3653-8b94-328f319a1d03 | -3.86201 | -47.40037 | 2025-11-06 00:15:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 0c18b1ec-5d71-3ff4-bb56-a5204f89ce2e | -3.38081 | -44.05967 | 2025-11-06 00:15:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 8e16de5a-bc17-33ab-8d25-89fe2cdec2ac | -1.00645 | -46.80115 | 2025-11-06 00:15:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f25d566a-9478-343d-88b5-20daf80dd4fd | -4.39622 | -45.46019 | 2025-11-06 00:15:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 17537ce0-e0c6-39f3-aee0-8952d9ca35d1 | -2.46855 | -49.23454 | 2025-11-06 00:15:00 | TERRA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| fb189cd4-6dde-36da-b50b-f372f88b0dfb | -3.43226 | -42.53927 | 2025-11-06 00:15:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| f0e186d8-e95e-3cd4-a5b9-e9fe9aa377f2 | -3.47046 | -43.65748 | 2025-11-06 00:15:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1300.7 |
| b4273083-93cc-3a1a-8a70-98282696f369 | -3.42591 | -54.04177 | 2025-11-06 00:15:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| df028c0e-06f1-3d57-a9df-30da04d3eaac | -3.98947 | -48.00865 | 2025-11-06 00:15:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a42bce9a-bf68-36ee-bf6b-e8adf0c20f9b | -4.37489 | -45.43626 | 2025-11-06 00:15:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 914c624a-d10a-3128-8fba-b2e4bd180d11 | -3.13983 | -40.05233 | 2025-11-06 00:15:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 22.4 |
| fe5860c5-274b-3099-ae31-ab16920ca865 | -3.60996 | -43.51939 | 2025-11-06 00:15:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 36.7 |
| daddfc24-92eb-3719-9514-2d40cbdb0e9a | -3.00261 | -49.56014 | 2025-11-06 00:15:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ba393bf4-bbf0-3c37-818b-190d19ff8914 | -4.03756 | -47.00401 | 2025-11-06 00:15:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 68c89d15-92e3-3407-9476-bb3b98b24b5c | -3.48122 | -43.66608 | 2025-11-06 00:15:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 9f540b9b-0de4-30d9-997a-c25ced3bf96f | -2.4485 | -49.01851 | 2025-11-06 00:15:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 39699b41-5a05-398f-8dfc-c43691af8d08 | -4.26655 | -45.12435 | 2025-11-06 00:15:00 | TERRA_M-M | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 8ecc5d41-bab0-3d82-8093-ff7bcdda17e2 | -4.03926 | -46.0795 | 2025-11-06 00:15:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 47952e2e-b7b5-3cb5-90a6-5c281902fd8b | -2.97998 | -45.08319 | 2025-11-06 00:15:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f3d4762a-a935-308e-a607-3d137cda3980 | -3.86332 | -47.40993 | 2025-11-06 00:15:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| b33f444b-2414-3652-829a-fffd8302df93 | -4.87854 | -49.00426 | 2025-11-06 00:15:00 | TERRA_M-M | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 20da6ecb-df68-3e1f-ba70-4b24ad13977d | -4.04661 | -47.00279 | 2025-11-06 00:15:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 1ca92c08-af0c-35a6-ba70-dabc8aea4f82 | -3.41386 | -42.55344 | 2025-11-06 00:15:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d1eb8bb9-c093-3e66-82fb-b26249d2cf00 | -3.37834 | -44.1087 | 2025-11-06 00:15:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8922aca7-3793-3181-a25f-40ef39c7c263 | -2.43419 | -49.35731 | 2025-11-06 00:15:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 92ef293b-2901-3c11-8da4-3f94324aed37 | -4.54191 | -46.45125 | 2025-11-06 00:15:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 7969de5f-3fa7-3369-bb72-1f11c5335075 | -3.39 | -44.05836 | 2025-11-06 00:15:00 | TERRA_M-M | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 16d73fa7-2446-3b1b-a8ce-a0bdaeea4ef6 | -4.42642 | -50.60908 | 2025-11-06 00:15:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| fa4b261c-58be-31f9-9bff-9c147a201d43 | -3.13613 | -40.05937 | 2025-11-06 00:15:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 24.0 |
| c99cdee5-ba27-3c67-8410-d4e06837a2ea | -4.54067 | -46.44221 | 2025-11-06 00:15:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 14198564-cf4e-3989-8ade-445a6f695019 | -4.00745 | -49.28182 | 2025-11-06 00:15:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b148a8d8-e245-3a9d-9466-e8a52402480f | -3.11947 | -51.21615 | 2025-11-06 00:15:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 25fd3315-d2c4-30d0-9495-e5130d4254b6 | -3.83274 | -44.39207 | 2025-11-06 00:15:00 | TERRA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3870024f-b118-3b16-8995-c93f059eca86 | -2.98457 | -52.84178 | 2025-11-06 00:15:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 5eddcee5-14c0-37aa-90ff-5c66e4abb392 | -3.98887 | -47.72262 | 2025-11-06 00:15:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 4b50d700-4f28-35d4-9246-57148bb6b7f5 | -3.32646 | -42.3698 | 2025-11-06 00:15:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 83662d19-ea68-3da1-aa41-b35ae30363a4 | -2.89351 | -50.46699 | 2025-11-06 00:15:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| e2d64f9a-e9e6-3268-a0c5-5f8a33c4afd5 | -3.86886 | -48.33352 | 2025-11-06 00:15:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 32fb9cba-9436-3672-9c58-9da1b73a907c | -3.58448 | -46.05706 | 2025-11-06 00:15:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 9cad48f7-9bf4-35aa-a985-3808aab7094e | -4.1115 | -48.01631 | 2025-11-06 00:15:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 43a274b4-0688-3994-a345-9d0a222854d2 | -2.99285 | -52.8348 | 2025-11-06 00:15:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| bc65d32d-6256-34c7-9b48-b0ed822fccdd | -3.61277 | -43.5395 | 2025-11-06 00:15:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3de939f7-f2ea-3e5a-a03a-2e0508d53f58 | -2.65373 | -48.51094 | 2025-11-06 00:15:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| bd8b933b-7561-301d-8cf1-db015f5321c9 | -3.73994 | -50.70273 | 2025-11-06 00:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 3872ae21-fa8f-381f-87a4-1557cc009d16 | -2.62058 | -49.22487 | 2025-11-06 00:15:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 3fe3924d-cb44-3f0a-8ff6-bfef8b11e351 | -3.42222 | -54.01358 | 2025-11-06 00:15:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| efa8255b-ecec-3534-8a40-5ed562ee4e58 | -3.55586 | -50.01806 | 2025-11-06 00:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| c1ca38ae-e2cb-3bb1-90fd-37d097354875 | -2.89214 | -53.13522 | 2025-11-06 00:15:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 04e75058-4dec-3e8b-af52-372bc7d9d765 | -3.61136 | -43.52941 | 2025-11-06 00:15:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 02af0810-68fb-3932-9408-dd979fda9f01 | -3.92765 | -47.6909 | 2025-11-06 00:15:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 8602ebee-c9d4-36cb-951a-8f40858f109c | -3.12232 | -51.20463 | 2025-11-06 00:15:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 43de556e-a3b9-38fb-b0b2-fb739fb1efe5 | -4.03987 | -46.21487 | 2025-11-06 00:15:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 2518c9b5-c297-3679-8e7c-374d90f98417 | -3.47187 | -43.66737 | 2025-11-06 00:15:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 438.9 |
| a4b86632-2681-35e2-b06e-38c1931a8db1 | -3.48263 | -43.67599 | 2025-11-06 00:15:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 275d6188-07bd-3411-90ae-3d9da10c0eba | -3.91815 | -43.1583 | 2025-11-06 00:15:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |


[Clique aqui para ver as próximas entradas](README5.md)
