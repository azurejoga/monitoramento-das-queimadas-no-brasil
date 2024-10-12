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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f2b1afe-00ef-3d19-9a69-e94e64c4e162 | -12.89054 | -53.52118 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c24eca6-2d01-3aa8-908f-a9876e893e68 | -12.88701 | -53.50858 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99aff9e8-4da9-34dc-9650-20253d633ed2 | -12.88625 | -53.51454 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 277a29b0-0a73-3283-b842-f4b85f2a26c0 | -12.8855 | -53.52047 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 15573448-563f-3467-aa27-6407630cc8f1 | -12.88121 | -53.51378 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df0438e8-5589-360e-a439-d14a5c9d3a8e | -12.88046 | -53.51973 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ee7d1bd7-4d2b-3faa-83bd-c311574c3f90 | -12.87617 | -53.51303 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4927c4b-9d28-3b2b-b81c-4c986bb91aa8 | -12.86607 | -53.51172 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c295723-3379-30a0-babc-d9a9a28525bc | -12.86534 | -53.51758 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5001ec9-471f-30ab-8b6e-bc72be5bdee2 | -12.86101 | -53.51114 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6a3cd31-b9f8-32ac-9b79-2ab325217ba9 | -12.86028 | -53.51697 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8628cc1a-7f9e-384a-8a69-f83333127747 | -12.85596 | -53.51051 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8385959-a7f6-38d5-84e8-f225778c0354 | -12.85522 | -53.51637 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c79f4bc1-47eb-365a-8205-aca4483b94e9 | -12.85091 | -53.50985 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| addc32c6-60b8-32c2-8695-5e6fe2256adf | -12.85018 | -53.51571 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 698776a7-2cfe-3f20-860f-7e340ae3f76f | -12.84945 | -53.52154 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 825902e0-13e4-37d7-914e-2ea862ccbdab | -12.84586 | -53.50917 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f82bd5d-e493-387c-ac10-bb91c7fcbe30 | -12.84513 | -53.51503 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6675bceb-4b85-39d9-905f-359a5523bcf1 | -12.84441 | -53.52086 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 900c0c6d-f28d-35c1-81a9-777a115884c0 | -12.84081 | -53.50848 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 783b6e88-e162-313f-a843-861475c81986 | -12.84009 | -53.51435 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bc8878b6-82a4-3cd8-8ec6-4f982e0d0e6f | -12.83936 | -53.52017 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 194a8872-0750-36bb-a367-20ef3e0050df | -12.83504 | -53.51366 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d424ef34-4a70-308c-86e9-52b284dd8c74 | -12.83432 | -53.51947 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a9d9140c-497d-35b5-801f-8a5bd69755cf | -12.83 | -53.51296 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e5dbc59c-ca50-3894-948a-c1bfdde05314 | -12.82928 | -53.51878 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cc81fd3d-2309-3479-814d-3da22696c756 | -12.82495 | -53.51225 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f31bd45b-95bc-3713-9b61-bef9459a44e9 | -12.82424 | -53.51806 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1e9da695-b9d5-3a2e-a785-9f05cf9d0097 | -12.82146 | -53.5115 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 76175fa1-d4f9-36f6-a60a-c3226c733866 | -12.82071 | -53.5173 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 49b0af77-9fa6-36b6-b69e-a59ce371ed6e | -12.81991 | -53.51153 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ed4755d6-6e94-3c52-816f-35e907b3e441 | -12.8192 | -53.51734 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 25ba0add-c780-3886-99d0-96cb2cfc6b55 | -12.81643 | -53.51078 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8f3c2262-0c26-3f0a-9e1c-eb42d654ab4a | -12.81567 | -53.51657 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c1e24e0d-b616-3a66-af37-c2649a2995c5 | -12.81487 | -53.5108 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 2387f75f-ec4a-3e08-934f-af55018007ca | -12.81416 | -53.5166 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9da5c21d-a474-3192-a317-6b43e5a6091d | -12.81139 | -53.51006 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 991c4121-0327-39bf-98a4-20a08600b496 | -12.81064 | -53.51585 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 31203c8e-41b5-3a71-a86f-40ddf75751a1 | -12.80983 | -53.51006 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a978a4f0-1fae-3bf9-972c-6f15c587c019 | -12.80912 | -53.51587 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 90551b70-f170-3d82-b140-386fb8c1e1ba | -12.80635 | -53.50932 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| d5b02ab3-3a27-3479-855f-40532e120b84 | -12.8048 | -53.5093 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 2579ab87-583d-3e70-b2d5-5dc66c7bf85c | -18.13602 | -56.33862 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 4d7298c0-e31d-3efe-8ef1-532b5af7f193 | -11.72614 | -54.7881 | 2024-10-12 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f9fdecb-9f91-3d10-b5f6-29faa8633288 | -11.72551 | -54.7928 | 2024-10-12 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37ab3d96-7881-3a4b-9fed-fd74b1a202b6 | -11.2761 | -54.21969 | 2024-10-12 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb072123-0a4c-3497-bfb5-8192fb3bf5d8 | -11.27543 | -54.22472 | 2024-10-12 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 19cc306e-8809-31d4-a58e-223d930852e2 | -12.61456 | -55.21118 | 2024-10-12 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c722e614-45c1-36d5-8457-a60fc5159cfc | -12.61398 | -55.21569 | 2024-10-12 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab058ced-6efb-33c9-a67a-4f81643b6bad | -12.60386 | -55.22335 | 2024-10-12 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dcda7b8d-b5ee-365c-abae-3bbe89a7173e | -12.45112 | -54.56469 | 2024-10-12 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| d5529e05-eb87-3534-bb7c-cb68074ca50f | -12.45049 | -54.56969 | 2024-10-12 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 36bf7742-3d10-3ce1-bfb0-37804a25ceee | -12.45028 | -54.55689 | 2024-10-12 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3e31cbe1-8182-3446-89d5-445db456da06 | -12.4496 | -54.56194 | 2024-10-12 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 5d1e88d9-6419-39d9-9bf1-f64220140f88 | -12.44894 | -54.56694 | 2024-10-12 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 2e72c22f-800e-3e6c-a453-7d4804c74c1b | -12.44827 | -54.57192 | 2024-10-12 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 3f2f6172-9b1e-3920-a35f-99aed439a0d2 | -12.44707 | -54.55906 | 2024-10-12 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 9c816921-3740-3b82-bb55-a0c74a9df71d | -12.44644 | -54.5641 | 2024-10-12 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 2f400fc1-1eb2-308c-8317-54cd4881de8e | -12.44581 | -54.56912 | 2024-10-12 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| e2f12313-8e03-3f76-9326-534702a2673c | -12.4456 | -54.55629 | 2024-10-12 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cbb1bcee-aaa9-38fb-9dd4-949a269150d3 | -12.44518 | -54.57411 | 2024-10-12 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 6bfc5f44-f998-3e01-a46a-7d989deeb3a8 | -12.44493 | -54.56133 | 2024-10-12 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 12d32cb6-fb0e-33e1-a0a5-a67e4b50f88d | -12.44426 | -54.56635 | 2024-10-12 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| bc251d3f-2bf3-3d91-9046-16292b2b6dd1 | -12.44359 | -54.57136 | 2024-10-12 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 47fb7636-468c-320a-aa47-b2a830f4887f | -12.44293 | -54.57633 | 2024-10-12 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 7b1c16e5-2fcc-3d4f-aa78-1c044e282ea7 | -12.44026 | -54.56071 | 2024-10-12 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe5fcae5-e9dc-3cbc-a142-d83126761edb | -12.43959 | -54.56574 | 2024-10-12 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de688193-c721-37b1-873f-4f2936aa5226 | -12.43892 | -54.57079 | 2024-10-12 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a804a0ce-376c-376a-8295-74f6d6693c1b | -12.43825 | -54.57578 | 2024-10-12 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bd98f250-06f3-3c17-a78f-10dd4794794b | -12.43358 | -54.57516 | 2024-10-12 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d701336-a5db-342c-952d-d44aff50c56a | -12.39236 | -54.45245 | 2024-10-12 05:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7dc2009c-e9da-3c73-9b35-ece68c094acb | -12.38766 | -54.45176 | 2024-10-12 05:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff598c64-246d-3e53-b483-521d084e19b0 | -12.38702 | -54.45679 | 2024-10-12 05:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 77f5d3fb-93a7-3aa6-b1f6-1916d5676d62 | -12.38638 | -54.46182 | 2024-10-12 05:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6349d582-5853-3a41-8c56-b18f43ac7ed5 | -12.38104 | -54.46614 | 2024-10-12 05:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 988bdf6b-49d2-3f05-b288-538db9ff583a | -17.27226 | -56.73726 | 2024-10-12 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| b9e98227-910d-3484-9506-f6c56c29ab4b | -17.06689 | -56.00167 | 2024-10-12 05:25:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 612916d4-efa4-3e0d-98ac-773911a2b534 | -17.0663 | -56.00634 | 2024-10-12 05:25:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d7f3c2e1-cbe8-3a2a-bafd-15c09f7ef60d | -17.06277 | -56.03437 | 2024-10-12 05:25:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| d9f7068a-e9e8-300d-90bf-f991ef3cac09 | -17.06219 | -56.03901 | 2024-10-12 05:25:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| f2d8e9bd-3eda-3260-a64e-0612b3738274 | -17.06178 | -56.00573 | 2024-10-12 05:25:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 93c465da-5ec5-3e83-8bc1-e2df44b5d4cf | -17.05826 | -56.03376 | 2024-10-12 05:25:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 77db674e-e1f9-3cef-87b4-8bf6907b955f | -17.05768 | -56.0384 | 2024-10-12 05:25:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3aed4ac7-cb0a-3c00-98ed-7d98cbe89c46 | -17.04705 | -56.01328 | 2024-10-12 05:25:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 603dc00c-edc7-3136-a648-aaa2a0728c1a | -17.04253 | -56.01267 | 2024-10-12 05:25:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ba27d8a2-ab8f-3c03-be2f-f59a70aea4c7 | -17.03119 | -56.03014 | 2024-10-12 05:25:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| df9870ec-ec82-3f78-bccd-ac67cfcb32ee | -17.03061 | -56.03479 | 2024-10-12 05:25:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e8c3153d-0467-38f1-a892-662b34d5f942 | -17.03004 | -56.03943 | 2024-10-12 05:25:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 0f098cc3-434a-33e6-995d-83d5cb813f43 | -17.02668 | -56.02953 | 2024-10-12 05:25:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 7558e6d0-0474-3a79-9412-216f13dfc2cb | -17.0261 | -56.03418 | 2024-10-12 05:25:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3c8516d9-1d59-3aa0-b708-489730a84df6 | -18.20575 | -56.53092 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| b2a0a6d8-72b2-373d-803f-4e2332d16a8e | -18.20521 | -56.53543 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| db3b3138-e91d-3d6f-90b7-01fb09b50f8d | -18.20467 | -56.53995 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 60f5bdb1-273e-3946-8d16-466b831c4ba4 | -18.20023 | -56.53934 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 5d111b73-3c4b-39df-81b3-f34968f55d88 | -18.19997 | -56.5192 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 99598917-6471-302b-8d00-6d6abd7c5219 | -18.1997 | -56.54384 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.5 |
| a0574976-6a72-3eaa-9152-dc3d4cdb3255 | -18.19849 | -56.51614 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 9f524da8-c846-3c78-bc28-0a606b72579c | -18.19712 | -56.54172 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.5 |
| fc07eeec-e5bd-3c28-9316-8cbd4d856cc3 | -18.19655 | -56.54622 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 6f9290b1-adea-3223-a132-0035904a8f58 | -18.19554 | -56.5186 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |


[Clique aqui para ver as próximas entradas](README121.md)
