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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97517636-fa55-31ef-a76e-10438fceb6f1 | -5.39808 | -45.98755 | 2024-10-10 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7c7114b9-303b-3fcf-a556-5eb90b900361 | -5.39717 | -45.99293 | 2024-10-10 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e9979bfc-f77d-3aab-a49e-96c0ef5738d4 | -5.39322 | -45.98667 | 2024-10-10 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c22359f4-0d44-300d-a37a-65099671df9d | -5.3923 | -45.99209 | 2024-10-10 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f426b64b-92af-3a91-8094-e47790e7949e | -5.37045 | -45.19735 | 2024-10-10 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27858d18-5745-3395-92d2-e92accfcd2a6 | -5.19893 | -44.93124 | 2024-10-10 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| c329086d-3504-3913-abdb-f504ba306876 | -5.19814 | -44.93588 | 2024-10-10 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 57550cf1-0f64-3acb-812a-801713c81a77 | -5.14661 | -45.10173 | 2024-10-10 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1e4bc12e-f9f3-3f8e-a939-db545e872fe0 | -5.14643 | -45.1005 | 2024-10-10 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ef31b66f-4407-3e53-b599-182d0f7a94aa | -5.0997 | -46.11256 | 2024-10-10 03:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5a9c5695-1091-3202-9ac1-0dc21863a4c1 | -5.0514 | -45.79415 | 2024-10-10 03:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8894968-c872-364f-bf7c-5e3b9aa726af | -5.04656 | -45.79338 | 2024-10-10 03:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b9509c5-d5b4-3ff4-9833-4e6ad5f4f26f | -6.34355 | -46.30531 | 2024-10-10 03:55:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7dd22d2d-80e0-3970-b0f0-3ba4698e7342 | -6.34032 | -46.30801 | 2024-10-10 03:55:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2cb8912a-ad24-374c-967d-b2cada6f8719 | -6.32678 | -45.71664 | 2024-10-10 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5d0d324-ff91-3d43-a950-762ba748a1d4 | -6.31672 | -46.40372 | 2024-10-10 03:55:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| de863439-4700-318e-a411-3408302bf967 | -5.98635 | -46.34721 | 2024-10-10 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| eccb5685-5687-3c8b-99e3-d2087e78e132 | -5.85238 | -46.43829 | 2024-10-10 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9bb9f5f-9be3-330a-aea4-912a86e97070 | -5.84444 | -46.45465 | 2024-10-10 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 348e4794-f49f-3d1f-a7fd-70a682baeb9c | -5.84391 | -46.45775 | 2024-10-10 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0a592a2-7f44-343d-a14f-92e493eabb34 | -5.75895 | -46.50257 | 2024-10-10 03:55:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75bbcbf3-1fcb-31e5-bc0a-2b281282419f | -6.22339 | -45.31192 | 2024-10-10 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4f6acd72-fd66-3ec7-81d9-027a2b8423ed | -5.91163 | -45.42601 | 2024-10-10 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 156ee531-3689-32d2-b30b-7d7c7e2c5788 | -5.90865 | -45.4154 | 2024-10-10 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| cbc77afc-41f7-3243-a387-5840d7e41acf | -5.90315 | -45.41964 | 2024-10-10 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 460a6f40-3552-349b-a6b1-3ddacd99d3e1 | -6.34523 | -46.30877 | 2024-10-10 03:55:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7040489d-6315-3234-9d8d-45c7f81e245e | -6.33771 | -46.07582 | 2024-10-10 03:55:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac5a0929-1522-3037-a28b-578dd91056ea | -6.3137 | -46.40063 | 2024-10-10 03:55:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 53d8e24b-e5bc-30bc-a20a-7100f9592187 | -6.31269 | -46.40631 | 2024-10-10 03:55:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4947a3a1-5ce9-3b1e-8e93-759d3bc7140b | -6.30448 | -46.32719 | 2024-10-10 03:55:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 95981cc9-74d4-37cb-9d0a-7f5e7de5c475 | -6.22801 | -45.31251 | 2024-10-10 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8a08c34-1006-30d1-950c-e91a6e8fccc1 | -6.02176 | -45.41616 | 2024-10-10 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1855f9f2-c854-3d15-a601-5c062dba7f97 | -5.91247 | -45.42105 | 2024-10-10 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 48b0b80d-a741-3c6a-a9f6-802986298690 | -5.90781 | -45.42035 | 2024-10-10 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 18356530-7f64-3acb-aa97-d4ed4f1448a1 | -5.90697 | -45.42531 | 2024-10-10 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 603002e7-9985-3ae2-a28b-5550b296763b | -5.8479 | -46.43454 | 2024-10-10 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 634e739e-cd5c-3da9-b664-86d5c1db2f9f | -5.84738 | -46.43752 | 2024-10-10 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57645821-7d61-3739-92b5-f0dcf3f80e7f | -5.84656 | -46.23571 | 2024-10-10 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3a8dfb5-bed5-3726-b128-28b044329c03 | -5.83043 | -46.12611 | 2024-10-10 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6078bf8a-9b73-3bb7-bdf6-2489ddb3e21c | -5.70127 | -46.44818 | 2024-10-10 03:55:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7683e548-66af-3981-9eb1-81aff1eced4d | -5.58505 | -46.31216 | 2024-10-10 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 312c4be2-e88e-394f-96c0-936e7634d18f | -5.58006 | -46.31148 | 2024-10-10 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 13483d7e-2241-384b-9030-c7d30f6625ad | -5.53768 | -46.20156 | 2024-10-10 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6a4dce2e-9333-3359-9b0b-4752cb071546 | -5.31724 | -45.47969 | 2024-10-10 03:55:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ce54c55-42f0-335f-bc7e-71845165da5d | -5.31639 | -45.48463 | 2024-10-10 03:55:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0eef0157-0e2c-317b-95ea-a6571d4b2697 | -5.31169 | -45.48378 | 2024-10-10 03:55:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c08139c5-9d45-332e-ad62-c5494ad04146 | -5.0987 | -46.11838 | 2024-10-10 03:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 97602d77-9bba-3b49-bdb4-8f76d4d5785d | -5.09275 | -46.11545 | 2024-10-10 03:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e65a56a6-c9b9-303d-9882-a88e2e71f19f | -5.05051 | -45.79936 | 2024-10-10 03:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78eda184-2512-3188-8f98-68fd915ab67e | -7.82369 | -46.47665 | 2024-10-10 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7454a11-7f28-3407-ad66-3811d91f3051 | -7.81946 | -46.47949 | 2024-10-10 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c1755055-ed09-323f-8ebe-3f4403d4d159 | -7.81887 | -46.47577 | 2024-10-10 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e48c7448-967e-3304-8dd0-70d4eeb1ba23 | -7.58752 | -46.80839 | 2024-10-10 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0ac8aece-d4da-3ebb-b7d5-c1724b5e19df | -7.58333 | -46.80324 | 2024-10-10 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e9db6b59-e91c-3361-934f-e59fee8d666e | -7.58256 | -46.80751 | 2024-10-10 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5883ca5e-519b-3fc1-b187-09c8036190b1 | -7.58205 | -46.81036 | 2024-10-10 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 32ee4a09-ae27-3e5a-9804-d7e28e0b8a20 | -7.4484 | -46.68653 | 2024-10-10 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fa078f7c-97b8-31a0-9ce3-586ffe1abb78 | -7.42542 | -45.61843 | 2024-10-10 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 09fe2d4f-b96b-3375-8020-38ec1b0c5451 | -7.39608 | -46.13729 | 2024-10-10 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 540830fa-2f73-3d53-9909-014fe2732bd5 | -7.39516 | -46.14253 | 2024-10-10 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3d53c1b5-7f16-30fe-96e8-237ce2f126bf | -7.38856 | -46.15219 | 2024-10-10 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a3205f71-c670-31e5-b14e-7b919a5af5e2 | -7.3847 | -46.14625 | 2024-10-10 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7dcccbe2-7ce5-3821-b7ec-3efc958a1360 | -7.38085 | -46.14022 | 2024-10-10 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 16cb7968-0bfb-38cd-9200-ac65c0c46f30 | -7.37993 | -46.14547 | 2024-10-10 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8b4343f1-feb8-34ea-bed5-c780e6d425ec | -7.35453 | -46.37389 | 2024-10-10 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e1864be-34da-3767-993d-e79c8d11cfe2 | -7.33843 | -46.73152 | 2024-10-10 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1d8abf8b-1283-32af-b204-4b59e9672b24 | -7.33781 | -46.72977 | 2024-10-10 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1ec215f8-8058-3065-84b8-87adcaec118e | -7.33683 | -46.73544 | 2024-10-10 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fd4c6ce6-d297-3acb-a9c8-e49d18336c12 | -7.24642 | -46.45771 | 2024-10-10 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6b178d6a-7e52-3723-b058-417b3db28951 | -7.112 | -45.3292 | 2024-10-10 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0b4da2ec-3a46-362f-b111-6dc0f30c299d | -7.01491 | -45.45377 | 2024-10-10 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 219b069a-5e76-32c3-996c-e18aa6f45d50 | -7.01033 | -45.37054 | 2024-10-10 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36937f8d-d43c-3c0a-a2a3-5d8c50096888 | -7.00659 | -45.36506 | 2024-10-10 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee06d1b1-abb3-310b-a1d3-aa118becf477 | -7.0058 | -45.36969 | 2024-10-10 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a205955-72be-3b84-9885-599f9781377e | -6.99188 | -45.23447 | 2024-10-10 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6da7494e-00c7-3ba2-850a-ae9f39acc584 | -6.98736 | -45.23379 | 2024-10-10 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cb98f018-68ca-36f7-8099-c74e4403cffc | -6.98518 | -45.38068 | 2024-10-10 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8fb2a430-1e62-39f5-b3bc-eb7a7b283b78 | -6.98142 | -45.99988 | 2024-10-10 03:55:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5c85bad8-53fc-3780-97ea-8eadba55bf9d | -6.96486 | -45.79086 | 2024-10-10 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4f19769d-94e0-3094-99d2-aa17fff0a412 | -6.96432 | -45.28591 | 2024-10-10 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf314a47-7282-30bf-8b12-da5c23ed3fef | -6.96308 | -45.64636 | 2024-10-10 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4d8bb4f1-a35f-34c7-ba6b-af6cbc51c031 | -6.96269 | -45.28745 | 2024-10-10 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f4a6279e-0984-3109-aecd-7a273b68f169 | -6.95986 | -45.28481 | 2024-10-10 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 85895ec4-a6d6-3654-a23f-1b5bc818ce67 | -6.95969 | -45.27756 | 2024-10-10 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fd43fc26-308c-3543-9a7f-f2162f0b799b | -6.95896 | -45.28191 | 2024-10-10 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9aece988-8632-3b3e-ba09-459c14ca1e28 | -6.95823 | -45.28624 | 2024-10-10 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e53d5c2e-46f2-3192-a1ec-6ad18f982335 | -6.95612 | -45.27959 | 2024-10-10 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 27ee93b4-9096-3149-ace4-55c332abd03d | -6.95538 | -45.28379 | 2024-10-10 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0eaace14-d79d-3a8f-96c1-ea0136aa01dd | -6.95446 | -45.28104 | 2024-10-10 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b9135fd7-a5e0-3870-8af1-c6765d883097 | -6.95376 | -45.28519 | 2024-10-10 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 51c50234-c281-3b9b-88b1-004413a87ae6 | -6.84409 | -46.22193 | 2024-10-10 03:55:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 614673a6-b3f2-3b6f-9aa8-aaab49af2871 | -6.83923 | -46.22127 | 2024-10-10 03:55:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 89292ea5-906d-3eab-97a8-3b2041851a37 | -6.81454 | -45.96592 | 2024-10-10 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6a4fd4b5-9f18-3a27-8f4b-3db6827d7c41 | -6.79634 | -46.12694 | 2024-10-10 03:55:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 04506abd-483a-3108-8b00-0d4b7bc964ec | -6.79632 | -46.13018 | 2024-10-10 03:55:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| cb9a533b-3dac-30db-b845-ceedd23922ff | -6.7954 | -46.13219 | 2024-10-10 03:55:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6a16f52d-aba8-3640-9c4c-a0a22b7b8f0c | -6.74262 | -46.2981 | 2024-10-10 03:55:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 202215e6-619c-3c82-bbcf-4b6cf22d0e82 | -6.66578 | -46.33553 | 2024-10-10 03:55:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cec69c24-f7f6-338f-8c38-a34b9016e180 | -6.66282 | -46.3661 | 2024-10-10 03:55:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a695c4a1-4961-3a22-b161-5a593d144adc | -6.65792 | -46.36531 | 2024-10-10 03:55:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README48.md)
