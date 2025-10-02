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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f79c6fb8-87f1-3602-ad76-3f0f6d67638d | -11.59873 | -47.22725 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8986ec55-15d6-3550-b568-f4df74855fd9 | -13.21096 | -48.49384 | 2025-10-02 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7e57909b-ecdc-39ca-9658-48f504210328 | -13.80245 | -47.52552 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b4210950-49bc-3e7b-aa57-e1d867c5ffdc | -10.83855 | -46.64408 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5faad522-4e54-35df-b8a8-a69954c7ea37 | -10.82861 | -46.61403 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 046d9f8b-88ed-35ef-8716-4137ad066b83 | -14.645 | -48.26538 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea9e727d-cd30-3cfd-8588-39ad47abe2f7 | -11.17395 | -47.28454 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b4d35240-b80f-3f6c-b9e4-4e31e397d570 | -9.94375 | -43.72805 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 83d84deb-bc6c-3cc1-800d-7f3d7e0518db | -15.39992 | -49.18718 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1177c8a3-9e44-34ac-ab68-8e3822e978ce | -13.30347 | -46.99407 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 873b141f-3010-3f53-bfad-36808a0b3da6 | -11.91603 | -47.88462 | 2025-10-02 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 389620c6-9f50-3288-9c00-8004712b8c78 | -10.20937 | -50.26817 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f7280742-d0e0-38a9-8fbe-88d27cca57ce | -11.61029 | -45.0596 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0c1a3d5-ebed-35a8-b2a7-fad97260da4a | -11.26153 | -47.6615 | 2025-10-02 04:51:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3db0a9d4-afe8-3d16-b0ed-163682e1970a | -16.05536 | -51.03196 | 2025-10-02 04:51:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b01c964-ba62-3743-9813-d8a10dada74c | -13.95461 | -48.10997 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c3bc14e0-2572-3b10-a812-8dfc75f211c6 | -10.81983 | -47.95539 | 2025-10-02 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aec59c8a-12e6-3fb8-a4b6-d1827498eddb | -12.41412 | -45.1722 | 2025-10-02 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cf67ced4-cb2a-38b3-bcc7-36744f2f2287 | -11.27676 | -47.83298 | 2025-10-02 04:51:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 023223af-72a2-3e0e-aa32-4e0583b0e4db | -11.98149 | -51.40447 | 2025-10-02 04:51:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3355163c-a2f7-3498-ab35-76cc3676b7af | -11.81729 | -47.59607 | 2025-10-02 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a490fb4-a8a7-35ba-9ecb-60ed003ab071 | -13.00667 | -45.20483 | 2025-10-02 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bac1d16a-d9b1-39df-a79d-fa704e46f2b4 | -9.93375 | -43.6315 | 2025-10-02 04:51:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a68c8e9-b91e-3287-b5af-2c067a66c6ff | -11.08147 | -47.81176 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19b5080b-a552-3cb0-a3d4-a2b1d2b4b29c | -11.71785 | -44.46681 | 2025-10-02 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23395049-9f26-388d-8d12-629ebc766ac4 | -11.83965 | -49.50817 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8be9f69f-3206-3d2a-b9bf-225ea0ad16dd | -11.59001 | -50.16716 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 32b3307f-f866-3ff0-afbb-edf4ed65771e | -9.93834 | -43.77051 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7585e55c-cecf-343d-b3a8-88328a7517d9 | -11.35875 | -48.33767 | 2025-10-02 04:51:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee8fecbe-896c-3dc7-867c-fb7ef4f681ec | -11.03628 | -47.82702 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a54b65a5-eecc-33ae-866d-ab7c28dec4c1 | -11.1339 | -43.39093 | 2025-10-02 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f77a10b3-270a-3fed-ad9f-3e0e2d99cc35 | -11.38803 | -45.04475 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75e4bd48-4073-3f69-9dcd-9a9a09f661c1 | -11.47079 | -44.98616 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3168ebca-469c-36c6-9cca-465384f1dd26 | -9.80203 | -45.95683 | 2025-10-02 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c98f046-2d42-3077-94cb-892ca1603b6c | -11.46928 | -44.99831 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10fb2f76-b804-3701-b7d0-6d23b986e244 | -15.25001 | -56.7774 | 2025-10-02 04:51:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 571c1600-29e2-3162-b5a2-5fe4d284684c | -13.6926 | -48.63319 | 2025-10-02 04:51:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 3a791639-7510-3e48-b8a1-b0ed5b9c20f1 | -13.65024 | -47.30862 | 2025-10-02 04:51:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4cdf07b-039d-3a74-a84f-3c79152919ac | -10.81723 | -46.62556 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 09b29d61-0eea-3904-b503-ed2a9fc78f95 | -10.26731 | -50.32368 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2249fd85-d33d-3127-96a6-f054a6d30cba | -14.31175 | -46.00006 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 850c2c1d-fd82-3902-99e9-76141459bbf6 | -15.94296 | -43.33932 | 2025-10-02 04:51:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 233f86c8-175f-3b94-8b77-a86a6cac49db | -14.46762 | -48.39893 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa02bbff-bd80-3b9f-9f0f-2f47b8a4f890 | -12.26056 | -47.82309 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 73987027-fc68-38cf-a876-0258abb05b68 | -11.46437 | -45.01893 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd04a23c-3ec3-3456-905d-cc87818fd534 | -12.57566 | -49.89738 | 2025-10-02 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 54dfaa88-ffe6-3725-a654-8bcf98db6d60 | -13.19634 | -47.83871 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 193156ea-9620-3605-853f-a99228c2272b | -13.01026 | -45.21811 | 2025-10-02 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 99b8692a-56d9-35f2-9a61-977986f59b63 | -14.89371 | -48.32588 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 97c704cd-6ced-37a8-9637-30aedd3e1ade | -14.48411 | -48.40548 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19d1f0dc-282b-3c5e-86be-aab471c723ce | -11.60215 | -47.23017 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 04622b9d-916a-337a-9808-6bc573947b84 | -14.43097 | -46.3578 | 2025-10-02 04:51:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6d06dad-11f1-3cb4-86da-0499e9b918dd | -16.03341 | -50.90491 | 2025-10-02 04:51:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9496e890-517d-300c-8cc4-20a1e7cb32b1 | -12.02 | -52.51529 | 2025-10-02 04:51:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79761576-913e-316d-b1a7-6dd1fcb87d01 | -10.70225 | -48.58245 | 2025-10-02 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 1277f31d-45ce-36b2-885a-a494b74e4801 | -12.40931 | -54.36488 | 2025-10-02 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eb04b4db-2157-3845-9f9c-d2fcac7a3074 | -11.47065 | -44.9715 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 395dc2da-0336-356f-babd-d837b63c8205 | -12.68622 | -47.56577 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba1f31d0-70f4-3009-a9f0-5f438f5224d6 | -11.46964 | -44.99538 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ccba2120-662f-3a0e-8b25-8111c99ee0a5 | -12.80278 | -46.86259 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 705b71cf-f9dd-3cc3-9ba5-d8b8aa222591 | -12.8663 | -47.01873 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 03706283-da60-3c60-8d22-c0c65243604e | -14.3261 | -45.9659 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79c2638a-4b3e-35dc-83ff-cd14c7506822 | -10.23079 | -50.32243 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 37fb8159-28f7-39f2-b3de-a9180afc780e | -10.18649 | -52.56182 | 2025-10-02 04:51:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7a54eab-904c-35a0-b35d-c20741cfbb10 | -12.49189 | -54.40015 | 2025-10-02 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b063f4ac-3b65-3769-a26f-4de595a5f1bb | -13.75573 | -48.69641 | 2025-10-02 04:51:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e2228b0-2c8a-3ca2-a13b-692906a8eb08 | -11.12813 | -43.39087 | 2025-10-02 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 325e8084-e2e4-3d4d-bf71-16c5447d404b | -9.9172 | -43.71759 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d0f3ae7b-bbde-3292-9962-7481d2a4cb3a | -11.1415 | -43.37596 | 2025-10-02 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| da42cf4f-0a8c-339b-a428-752620b51c93 | -11.46312 | -45.0284 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9b8a7684-4c5f-3ecb-93c3-f7a84e96b627 | -9.92399 | -50.49281 | 2025-10-02 04:51:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 84a48184-e87a-361b-880f-c8923b989123 | -11.09309 | -47.82128 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2dab12f5-c939-356f-832e-7209232953c9 | -13.30808 | -46.99466 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e4504f6b-9014-3bb6-9ab3-117d075e8e91 | -12.47822 | -47.2754 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0aa09e60-ca2f-3129-849f-7150f8e58826 | -12.26112 | -47.81904 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f5b8700b-d501-3716-b393-b1ca98e642ea | -13.86658 | -47.95765 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e60b9b3-df7d-36cd-a20c-7a41536dcc19 | -15.25231 | -49.29744 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 36fd5eb8-d11d-306e-801f-d88003a7b3a3 | -15.40208 | -47.04543 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8697a4b1-aef2-3fb5-995d-bd85346b29ed | -13.23892 | -48.50604 | 2025-10-02 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cc2ce30c-3722-3f50-ac66-a5b21fb20c1c | -12.76135 | -50.55276 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bf485b6e-ddc3-3644-8ae6-b6a20a06e294 | -12.71028 | -46.89275 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbe69def-5f9c-333a-9346-7e6f89bb8ea1 | -14.36752 | -45.95864 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf568891-670f-3571-bbe1-b0a2d4863e64 | -13.17834 | -47.80779 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c942daa-2b27-32a8-821d-f882b892459c | -12.03271 | -47.91268 | 2025-10-02 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eeaad6db-df90-310e-8617-8f2412c01ceb | -14.88838 | -48.33341 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67a5803d-9f49-372d-a8d6-236be02ddad2 | -11.44062 | -44.96081 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 15e1991e-4cdb-35e1-8d44-c4f1b588a443 | -12.21189 | -47.79536 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0cdc3e16-6030-309d-8319-111ace5d2eb4 | -15.2875 | -56.77976 | 2025-10-02 04:51:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97dbc72c-700c-3573-ba78-57318d55d8e6 | -13.70239 | -48.62312 | 2025-10-02 04:51:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e6e52b5-3760-3169-87d9-300a37b2f7f7 | -10.99481 | -46.59283 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 77d136c2-54d2-3c17-9ed9-8f905402287d | -14.21165 | -46.11523 | 2025-10-02 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 4769c03c-b424-3d6d-9664-dab936905e75 | -13.64159 | -47.19416 | 2025-10-02 04:51:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 668c9519-ddf0-3a04-8aa0-e17a1791cab2 | -14.21594 | -46.12138 | 2025-10-02 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 538ec76c-7758-36ea-8954-5300adc7a0a8 | -11.59886 | -47.22095 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8c657693-23ea-3e2a-8615-e5d89d95f665 | -11.85508 | -48.04575 | 2025-10-02 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b4e1e75d-1fba-3345-9a72-133d4701c1f9 | -11.67331 | -47.49542 | 2025-10-02 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0aa5aa14-d02d-3ae0-bbc7-f1b393034c45 | -12.74921 | -46.91397 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be0cc152-09c6-3ab1-b622-1c7f81ce8a90 | -13.64572 | -47.65935 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28f303d6-8e3d-327b-addf-e80d35cde677 | -13.66132 | -48.08698 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20453d32-48dd-3b1b-ad65-da117cf43671 | -13.21835 | -48.43953 | 2025-10-02 04:51:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README111.md)
