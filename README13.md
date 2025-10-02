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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf382e37-3b69-3ba3-bcf3-d0d66edca9cc | -14.9924 | -46.9091 | 2025-10-02 01:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 43d0ee36-81a6-3975-8e53-da43001f57b5 | -13.3081 | -47.8565 | 2025-10-02 01:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 82b5cd88-488f-37e6-9f19-27306b63f0f1 | -5.9858 | -44.589 | 2025-10-02 01:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 119.9 |
| e6a4d3de-1b4b-38be-8143-dc5efe69e8ac | -6.2411 | -45.3198 | 2025-10-02 01:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 6367a4c4-6e76-3975-b0fa-f26fe97dedcf | -6.0048 | -44.5647 | 2025-10-02 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 44.5 |
| b2535d62-76f7-3e77-bd9a-b1f7a055badd | -14.406 | -46.1184 | 2025-10-02 01:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 0095731a-a39c-30ec-981c-5095bd0ba25f | -14.4065 | -46.0953 | 2025-10-02 01:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 116.5 |
| f6672546-7b57-3006-a8ed-fb531f41aeea | -15.2738 | -49.3073 | 2025-10-02 01:30:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 63d9946f-852a-349b-8110-cbb0b48c0f73 | -14.4255 | -46.115 | 2025-10-02 01:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 411e848e-52cc-3858-a554-17dbb66c4f42 | -15.2547 | -49.2883 | 2025-10-02 01:30:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 63.5 |
| b0297f60-b170-3168-9967-a9e4b83ab375 | -12.4737 | -47.2621 | 2025-10-02 01:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| a24d182c-a0f9-3e59-8532-9f98c325f2d6 | -6.6955 | -48.7062 | 2025-10-02 01:30:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 55.9 |
| ac287092-e7b7-3f37-a442-52dc5688f637 | -5.986 | -44.5661 | 2025-10-02 01:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 6195e930-5338-3b55-8809-945fc2c9c7e8 | -14.4265 | -46.0688 | 2025-10-02 01:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 7fcc5cef-ae77-37eb-bbff-399a7e1b29d8 | -6.2411 | -45.3198 | 2025-10-02 01:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 5be51978-264b-3c74-b805-44dbcba0d253 | -11.0147 | -46.5619 | 2025-10-02 01:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 1e96ab9b-804a-308c-971c-ac8ba876c69b | -15.2547 | -49.2883 | 2025-10-02 01:40:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 5193b3c6-36a6-37d1-9f5e-ec1473de4ff9 | -11.8755 | -51.2173 | 2025-10-02 01:40:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 9e21318f-ad0a-3988-b792-4f2b4d908f5a | -14.3704 | -45.9634 | 2025-10-02 01:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 855ac08f-75b8-371f-a2de-012e33a5f109 | -7.7755 | -42.5152 | 2025-10-02 01:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 93.2 |
| 706d2087-5429-35fe-8b09-d3d03528ef56 | -14.9728 | -46.9125 | 2025-10-02 01:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 81.8 |
| ed036511-0b03-35c2-a663-f56802c3f15f | -15.2738 | -49.3073 | 2025-10-02 01:40:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 74.2 |
| a1b632da-008a-3064-8f50-3d772bafc13f | -14.4065 | -46.0953 | 2025-10-02 01:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 132.5 |
| e620f3e6-8092-3a83-885c-d79932635f44 | -11.8752 | -51.2386 | 2025-10-02 01:40:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 438b9c5b-f9d2-393f-bc3c-2275df14eab7 | -6.6955 | -48.7062 | 2025-10-02 01:40:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 1a8e52b1-adfa-311b-afb1-58b36c1155db | -7.7752 | -42.539 | 2025-10-02 01:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 172.9 |
| 8c8d2aba-4d33-39ef-b942-ce8d1a2675a5 | -13.1546 | -47.8345 | 2025-10-02 01:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 68c0c22c-4c5b-3d7f-8d15-2dbda9aad6d8 | -13.0119 | -45.1988 | 2025-10-02 01:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 50.7 |
| e72e0725-0d73-3e70-8ac3-529fca90aa7c | -14.9924 | -46.9091 | 2025-10-02 01:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 2c6addce-58b7-343f-904c-fe82af8a9111 | -6.7213 | -44.1387 | 2025-10-02 01:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 2b85a522-3026-32e4-9b29-52defcde4b75 | -14.406 | -46.1184 | 2025-10-02 01:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 571e537e-dbf9-3dbb-9c68-0d5c4f7daf6e | -7.7563 | -42.541 | 2025-10-02 01:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| 0a12be5c-567d-332f-9dd2-e9e1c1495114 | -12.4737 | -47.2621 | 2025-10-02 01:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 8b603637-9805-3e71-b0b9-a91fc4ea8507 | -14.426 | -46.0919 | 2025-10-02 01:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 5e73b875-d1af-3c60-8410-828998076a2b | -14.407 | -46.0722 | 2025-10-02 01:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 128.4 |
| a9793c26-3096-3b2e-a077-5856890d80fa | -14.4255 | -46.115 | 2025-10-02 01:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 9fa6ef35-e7a1-37ae-9756-7b1991f7de1b | -13.1739 | -47.8317 | 2025-10-02 01:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| e6905d4f-db06-3c27-ba89-94de4f66fa46 | -6.6955 | -48.7062 | 2025-10-02 01:50:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 67.7 |
| cf971f28-ac85-3cd9-978e-dc2051f49752 | -15.2738 | -49.3073 | 2025-10-02 01:50:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 2ab00410-17d3-30f9-a573-e07e5a5c032f | -11.0144 | -46.5844 | 2025-10-02 01:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 771a59bc-8bed-3523-a74f-cd28dfcb1a4b | -14.4255 | -46.115 | 2025-10-02 01:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 145.1 |
| ad884d53-cc8d-3ac9-a288-79f8700dc84c | -7.7752 | -42.539 | 2025-10-02 01:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 191.9 |
| 57724f46-8496-39b4-beec-93fa0af731de | -14.387 | -46.0987 | 2025-10-02 01:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 91e06b71-daae-3468-a6a1-441eda8764d1 | -10.9956 | -46.5643 | 2025-10-02 01:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| cca628e9-fc72-3585-b4b1-dce93d7f05ea | -10.8237 | -46.6088 | 2025-10-02 01:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| a696bf1b-f362-3c82-b505-a7bd46cb6c4d | -15.2742 | -49.2852 | 2025-10-02 01:50:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 182944c3-1721-3095-8f6f-00cb3149fddf | -14.3119 | -45.9736 | 2025-10-02 01:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 69.8 |
| e626ed4c-24a2-3cb7-9da2-7b98b076bd66 | -6.7213 | -44.1387 | 2025-10-02 01:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| a3fd7f1f-600d-3212-8c18-856f4ddff16c | -15.2547 | -49.2883 | 2025-10-02 01:50:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 91.4 |
| a70127f5-eae8-34d8-aab0-ce916d32d011 | -13.1739 | -47.8317 | 2025-10-02 01:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 01215549-4e81-38d2-9cc1-4dfab3f10ce4 | -14.407 | -46.0722 | 2025-10-02 01:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 68f6b099-2ecb-3f85-8060-47c6b194041e | -7.7563 | -42.541 | 2025-10-02 01:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 89.1 |
| 9e1b397c-bef8-3c0c-8d6e-ab1ecc43abe3 | -9.938 | -43.6718 | 2025-10-02 01:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 36ad4693-35c9-3daa-9fc5-cc6813e8aa85 | -11.0147 | -46.5619 | 2025-10-02 01:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 8bb1b73b-87ab-332e-9005-58c0cc71fa4e | -5.986 | -44.5661 | 2025-10-02 01:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 4ad99a1d-2dc6-3f03-a327-74f9f024ff4d | -6.2411 | -45.3198 | 2025-10-02 01:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 00a91387-2fe4-35ba-8f35-9391e4703ac5 | -5.9858 | -44.589 | 2025-10-02 01:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| b93de2c8-7ea2-37eb-92cd-86acbfc495a5 | -7.7755 | -42.5152 | 2025-10-02 01:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 82.2 |
| 1c9c976f-fc43-30cf-995d-a1a9e1fb18ac | -14.406 | -46.1184 | 2025-10-02 01:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 9069a7be-6d05-3bc8-84bb-9c5bf8d50d76 | -10.9953 | -46.5869 | 2025-10-02 01:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 32a302b9-4bf4-31f9-ba9f-4bf3e262e24a | -13.3085 | -47.8341 | 2025-10-02 01:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 4f46f331-d9be-31f6-bdb6-0cad60c35e29 | -14.426 | -46.0919 | 2025-10-02 01:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 105.2 |
| ad53e8cd-e170-39f4-b4ac-4234724d1ef6 | -10.8433 | -45.3815 | 2025-10-02 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 8a0a33cd-fc56-3124-ad34-e6bb7074c76b | -10.8429 | -45.4044 | 2025-10-02 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 375d11c4-ed50-3fd8-9336-7f4e77dc2533 | -14.4065 | -46.0953 | 2025-10-02 01:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 154.4 |
| e692814a-7258-3180-9cc1-49b4625f6ce2 | -10.9561 | -46.6594 | 2025-10-02 01:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 4ff43c63-e5c2-363c-b087-cad9c07cb600 | -13.1546 | -47.8345 | 2025-10-02 01:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| d17ecd94-7704-37a4-a177-bcb468850dbf | -15.2542 | -49.3104 | 2025-10-02 01:50:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 6435331f-94b0-3ca8-8cc3-7457447ebe93 | -12.3659 | -45.7832 | 2025-10-02 01:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 7e829413-e5e1-32ac-9417-20228a4ed6f8 | -9.49086 | -63.12279 | 2025-10-02 01:52:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 9.5 |
| f6747b81-c69a-34bd-997c-b8a2520cf942 | -9.64517 | -62.85445 | 2025-10-02 01:52:00 | TERRA_M-M | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 35.9 |
| a5d38002-7fd5-3072-a271-8ecd0369365c | -9.49336 | -63.13875 | 2025-10-02 01:52:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 1d56ff27-6621-30f8-952a-5db76ab617dd | -9.40798 | -63.70354 | 2025-10-02 01:52:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 33559d01-3f84-3381-8b6b-7eac7e537c43 | -9.40576 | -63.68909 | 2025-10-02 01:52:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 6b644562-66ba-389f-9a2e-642d43047da4 | -9.64261 | -62.83805 | 2025-10-02 01:52:00 | TERRA_M-M | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 89b9f3cf-02f8-3231-8cf5-32e0830c5cd3 | -10.47305 | -62.45636 | 2025-10-02 01:52:00 | TERRA_M-M | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 9.9 |
| c26c8fa6-1766-30da-957e-751194936beb | -13.1546 | -47.8345 | 2025-10-02 02:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 110.8 |
| ff2e9550-9028-3a1c-9853-cbee81ec42a1 | -6.6955 | -48.7062 | 2025-10-02 02:00:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 124.6 |
| 5e6bc53b-2c38-3b29-8d6d-30af35508c28 | -11.0144 | -46.5844 | 2025-10-02 02:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| e5843536-7820-34cf-b6eb-395be06e09bd | -13.3085 | -47.8341 | 2025-10-02 02:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| e22aee38-8604-345f-bcc4-1f43ee7bdf44 | -15.2738 | -49.3073 | 2025-10-02 02:00:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 7af029bc-f564-3204-b734-c16db1239c97 | -5.9671 | -44.5904 | 2025-10-02 02:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| d73e26a9-1449-36de-9302-67f04c0afd8c | -15.2542 | -49.3104 | 2025-10-02 02:00:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 40fd2ad7-f94a-342f-8fef-22f837705a96 | -13.155 | -47.8121 | 2025-10-02 02:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 544189b8-b129-358a-9851-63a05b84f5be | -5.986 | -44.5661 | 2025-10-02 02:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 3769be39-8a8b-365e-8789-66090424bc81 | -13.3081 | -47.8565 | 2025-10-02 02:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 5846d541-2693-39af-9ab1-0a3c866c5e08 | -10.9953 | -46.5869 | 2025-10-02 02:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| c5684ee4-a0bd-3c75-afa4-c6f3df9f6732 | -10.862 | -45.4019 | 2025-10-02 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 7847f999-c805-376b-9214-62637819b0c4 | -6.6953 | -48.7277 | 2025-10-02 02:00:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 54.1 |
| d8a3d0a9-d1ea-3fa3-96c9-4fed8e57c4a6 | -5.9858 | -44.589 | 2025-10-02 02:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 481107b8-70c3-3591-98a3-d205112b8051 | -14.3119 | -45.9736 | 2025-10-02 02:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 477b6d02-39a7-3dde-9b63-9d2116244b2c | -6.9715 | -45.3283 | 2025-10-02 02:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 094c6c23-b1e7-3b77-a0c2-068c16f0a926 | -10.8433 | -45.3815 | 2025-10-02 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.8 |
| dcebd99a-e2f2-3611-8009-79663665d8ad | -6.7213 | -44.1387 | 2025-10-02 02:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| af220f2c-fc26-38a3-9a66-3e26001cb82f | -7.7563 | -42.541 | 2025-10-02 02:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 79.5 |
| 6d7cf713-55ca-3993-8e1a-252cb6fab31e | -14.3704 | -45.9634 | 2025-10-02 02:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 106.0 |
| d2ca329d-63ef-3b96-881a-fd05f0e54abc | -13.1743 | -47.8093 | 2025-10-02 02:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 1576ef13-dbc4-39f7-bb94-cd75f5d07707 | -7.7755 | -42.5152 | 2025-10-02 02:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 80.4 |
| 3cea4a85-79a2-312b-bc8d-60790565f3b7 | -14.3114 | -45.9967 | 2025-10-02 02:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 133.4 |
| f6d05074-cb26-3e1f-a65c-7d1c9600557e | -13.1739 | -47.8317 | 2025-10-02 02:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |


[Clique aqui para ver as próximas entradas](README14.md)
