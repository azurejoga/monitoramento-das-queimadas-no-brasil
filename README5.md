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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a066b3d-06b6-387d-a357-8b74a3880272 | -17.2578 | -42.66423 | 2025-06-02 04:17:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00ecfa15-c378-3c6f-a1ea-e6a32ae6c79e | -17.67786 | -42.74068 | 2025-06-02 04:17:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 59c00454-3ff2-3884-b72b-5905f93782a0 | -6.73583 | -42.88783 | 2025-06-02 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 873cdabd-2d20-3c02-895e-684a8302a360 | -17.29325 | -42.65504 | 2025-06-02 04:17:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 26.8 |
| dcae5a5e-8ac8-3bf9-a655-5e93252f3fac | -9.39679 | -48.42606 | 2025-06-02 04:17:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3cf3db39-8dc9-3799-ac4f-a688e2800a15 | -9.39581 | -40.36509 | 2025-06-02 04:17:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 648a7277-7f4e-31f2-88ff-8ea034bd800c | -6.73473 | -42.89479 | 2025-06-02 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0e03d2c2-dba2-3ce6-b5ee-59132a38b8a9 | -11.61435 | -47.99788 | 2025-06-02 04:17:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1df96aab-b37b-357c-be4d-859aedde7fea | -6.73141 | -42.89426 | 2025-06-02 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 243d10b7-51d0-31d1-bcab-4f3c44cc5902 | -13.08967 | -45.26607 | 2025-06-02 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 934fa627-64be-3d25-989b-3bd08e78f0a8 | -9.78471 | -36.9985 | 2025-06-02 04:17:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a79ed81f-a91a-385d-b691-23b8c66ba9b0 | -11.9102 | -54.83147 | 2025-06-02 04:17:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ac08c8dd-19c7-3ddd-86f7-fff3938813ce | -11.44332 | -55.01231 | 2025-06-02 04:17:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 46a6dff7-eb68-37cf-9465-9c806814178e | -6.73587 | -42.90923 | 2025-06-02 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| adc403da-8805-3557-a77e-7a29237807bb | -10.4655 | -47.95252 | 2025-06-02 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| d3ee1b45-8c1c-39f4-9c55-b8394bee5fcd | -9.11773 | -47.64612 | 2025-06-02 04:17:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b3df402f-9ae6-3bb8-82fc-42dba51df964 | -13.08159 | -46.74482 | 2025-06-02 04:17:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5216856d-eb6b-323e-8667-2dfba71d2525 | -8.33205 | -47.09164 | 2025-06-02 04:17:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cbbcb544-bab0-3f84-9823-c443f7aec62e | -16.02795 | -43.68172 | 2025-06-02 04:19:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5e50709c-0a6a-3578-bf90-c90ca818971d | -14.03006 | -55.13053 | 2025-06-02 04:19:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d525b0b8-2b3d-36ab-8c36-c7224065e884 | -14.02928 | -55.13432 | 2025-06-02 04:19:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 939b61c1-3724-39ab-bbc1-d136e24bb178 | -27.01328 | -51.27691 | 2025-06-02 04:19:00 | NPP-375D | IOMERÊ | SANTA CATARINA | Brasil | 4207577 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 97b96cd6-3fff-3531-810c-3d051e66731a | -22.15084 | -50.01522 | 2025-06-02 04:19:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d941ee88-d5bc-3162-a73f-419b96008a65 | -20.45088 | -50.01029 | 2025-06-02 04:19:00 | NPP-375D | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 65dfcecf-a8c0-3745-8562-30d6cc1dd674 | -13.69907 | -52.91153 | 2025-06-02 04:19:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c7e47ec-c45d-3a54-9e6a-c2f80b56b5b2 | -20.31166 | -45.58395 | 2025-06-02 04:19:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f185a51-748b-3752-bc6a-2879cd6266a5 | -12.67197 | -58.21732 | 2025-06-02 04:19:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8638039d-060c-3874-8299-c7f2b1d1bab8 | -24.24217 | -50.74088 | 2025-06-02 04:19:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 39138464-b051-3d15-bd18-d7953a235a22 | -16.03145 | -43.67737 | 2025-06-02 04:19:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66a7c7c2-e05f-3ec8-acb5-fb32b8112fc1 | -14.01884 | -55.12826 | 2025-06-02 04:19:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dbf56b79-cbc2-3cc7-81ea-b29b8e4f64a5 | -12.67058 | -58.22381 | 2025-06-02 04:19:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0b0473ad-0060-3a7b-9677-5f7413d7b367 | -20.76541 | -46.76859 | 2025-06-02 04:19:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b746580a-a6f0-3985-b37f-0796f86379d5 | -14.01401 | -55.12335 | 2025-06-02 04:19:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd88b1c5-2b16-3a28-9cb5-f43fe642873b | -20.92043 | -49.09187 | 2025-06-02 04:19:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 70320d2e-3687-3aa1-98a4-54596d5a0161 | -20.99549 | -51.79327 | 2025-06-02 04:19:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ad3f449a-c476-33c1-8285-c43f983ac7f9 | -23.34104 | -46.77189 | 2025-06-02 04:19:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 465150b1-3059-3b79-9c02-88ec634f74f7 | -16.34962 | -43.69548 | 2025-06-02 04:19:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c8bd324-ae9b-3429-a089-2c637c3ed557 | -14.01676 | -55.12616 | 2025-06-02 04:19:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f4389aeb-020f-3594-9701-4e6bd4652360 | -20.5521 | -54.1209 | 2025-06-02 04:19:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 642f054c-3966-3751-87d9-aa3642f3783a | -19.28457 | -55.15757 | 2025-06-02 04:19:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 833f532c-4a62-3aa7-9b4e-38d97c7902c8 | -16.02748 | -43.6806 | 2025-06-02 04:19:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a962d4f-37ec-313a-be0d-c0991293e7e8 | -20.08567 | -50.97651 | 2025-06-02 04:19:00 | NPP-375D | SANTA CLARA D'OESTE | SÃO PAULO | Brasil | 3546108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| f2f779ef-3530-37c0-81b1-046666798475 | -23.4256 | -47.29509 | 2025-06-02 04:19:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 7e8b4ef1-5a8d-3979-a4a4-8aa824c1bd6f | -14.01602 | -55.12991 | 2025-06-02 04:19:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 036b9916-4552-3163-b697-7c16ddd86b34 | -21.19594 | -44.93729 | 2025-06-02 04:19:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 186c8cd9-3510-363b-bc2d-c55bcd6c250f | -14.0175 | -55.12241 | 2025-06-02 04:19:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a73093af-f64d-3f58-b6ad-d0a7e928a2ce | -16.02804 | -43.67681 | 2025-06-02 04:19:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d3adda8-acdc-3970-bdcc-77bb4c774e46 | -13.89185 | -54.63565 | 2025-06-02 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f8c017e-cc70-3a65-97fa-d51b557a9a55 | -12.71904 | -54.97349 | 2025-06-02 04:19:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5096cefb-e1d3-307f-b9d2-b26be0c780a7 | -15.56861 | -47.85466 | 2025-06-02 04:19:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6484f305-2d0c-3004-aa23-d6077ec64462 | -13.36833 | -54.26481 | 2025-06-02 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c15acf22-38b6-3061-a650-8e093456981a | -23.33771 | -46.77128 | 2025-06-02 04:19:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c7e1a032-b809-308d-9477-46ce1aec2db0 | -16.02852 | -43.67795 | 2025-06-02 04:19:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3302371d-793f-3636-8b2e-53f2498569f4 | -19.28969 | -55.15852 | 2025-06-02 04:19:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c703a1b0-4941-39e6-9115-5012dea68cdf | -21.25173 | -48.97548 | 2025-06-02 04:19:00 | NPP-375D | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| dbdb619f-e39a-3f0a-9452-65bc84c4e82e | -14.02236 | -55.12733 | 2025-06-02 04:19:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3188a13d-07e4-3ed7-b169-de9c7b589148 | -14.01961 | -55.12451 | 2025-06-02 04:19:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0be55276-76ca-305d-8bdc-cc17f83c3369 | -15.39619 | -47.52515 | 2025-06-02 04:19:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8decb912-a64e-3715-9c19-b89c41e97345 | -14.02851 | -55.13811 | 2025-06-02 04:19:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d915159c-572e-31fa-af74-ace973e6023b | -13.7024 | -52.91059 | 2025-06-02 04:19:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cd34cd3e-306c-3f39-adfa-5d15fbafe490 | -13.36903 | -54.26127 | 2025-06-02 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| da31bea2-c882-3f99-8018-3731bee7baab | -14.01477 | -55.11963 | 2025-06-02 04:19:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08c1fa45-5369-3e38-838a-8c53bcc61862 | -16.34913 | -43.69527 | 2025-06-02 04:19:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60d1576f-8bc4-3a3c-af0b-d2d7ad10be17 | -13.36296 | -54.26374 | 2025-06-02 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 492a69cf-1d00-35bd-97aa-c1ca86fa2ab9 | -19.28896 | -55.16209 | 2025-06-02 04:19:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5968598f-169d-37d6-b55b-2a72262bbcaf | -14.02038 | -55.12077 | 2025-06-02 04:19:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd7070e9-9b4e-38dd-a581-b84e56a03b35 | -14.0341 | -55.13933 | 2025-06-02 04:19:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77c8f61f-3864-31ad-aef7-d59d4001a85a | -22.54075 | -48.81393 | 2025-06-02 04:19:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8c79287-3261-3172-a5c9-0cc0b9c1414a | -13.70399 | -52.91233 | 2025-06-02 04:19:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b77aa6f7-e99c-32d6-8a74-e4ec6e236dad | -4.55158 | -48.01363 | 2025-06-02 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 098b54c1-4602-3512-86ee-cfe7e6646580 | -4.55103 | -48.01713 | 2025-06-02 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e320fb64-15e2-31dd-a620-428acb0e3bf1 | -2.58497 | -51.92272 | 2025-06-02 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 001c5050-77c2-33ef-b15d-12f599b021bb | -3.98669 | -48.41052 | 2025-06-02 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 434e5175-ed16-3dce-b2d2-a452681e7f51 | -2.58566 | -51.91846 | 2025-06-02 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6baa9b1b-a9de-332f-a9e0-9cd411af2ac1 | -9.33635 | -47.08263 | 2025-06-02 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd71a453-cd9f-3043-a7a6-abc6bd6bd91d | -13.08688 | -45.26376 | 2025-06-02 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 147d7abe-4eef-3414-bade-1586228a654e | -10.82373 | -56.94397 | 2025-06-02 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 595ccf04-0b4b-35fb-9343-c9f8b640e065 | -10.80653 | -56.94207 | 2025-06-02 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 52381b22-5aa0-3bc4-a457-ff5aabe5e097 | -10.81094 | -56.94288 | 2025-06-02 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 02ccff0c-5bbd-33d9-8544-dff9399abcb5 | -10.98251 | -44.62198 | 2025-06-02 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77b5b115-c1c0-35c7-94c7-79b04192acf6 | -6.73541 | -42.8863 | 2025-06-02 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e18c8439-c15d-3ff6-9820-d9cb08395013 | -7.95901 | -45.41765 | 2025-06-02 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24310157-dd92-3fc0-bca1-6dc26486779a | -9.39654 | -40.36324 | 2025-06-02 04:38:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 210912b5-5cde-3204-8491-01502d04aa6a | -7.6281 | -46.11408 | 2025-06-02 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c35b201-8c8e-3975-801c-1eb975307c61 | -11.43973 | -55.00871 | 2025-06-02 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0e9fa18-6001-3e34-941f-7a5c3e0f214f | -7.56641 | -43.28262 | 2025-06-02 04:38:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5e9d7fc-304a-3441-b0e3-d29cbafa5746 | -6.63986 | -43.20251 | 2025-06-02 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 18a8aaaa-aa18-3b33-8bfc-5f4dfb5d1653 | -11.43285 | -55.0025 | 2025-06-02 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9ef2170-3fc2-3e3a-ba0b-b3180cfb69f7 | -9.39639 | -48.4211 | 2025-06-02 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 724936b7-ac34-36f2-bc07-ec7e32f1bdb2 | -8.77815 | -47.24063 | 2025-06-02 04:38:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0cd84014-4876-3cff-a67d-4811536cc834 | -9.56162 | -40.77768 | 2025-06-02 04:38:00 | NOAA-20 | SOBRADINHO | BAHIA | Brasil | 2930774 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 73d2d288-aea9-38c7-ae47-53dcc9b79212 | -11.45131 | -55.01073 | 2025-06-02 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f759b4ca-5aaa-3e84-9d67-406a39e52f85 | -9.3981 | -48.41002 | 2025-06-02 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43ad9e37-534d-39f6-b2e5-00bb3768f408 | -9.40091 | -48.43685 | 2025-06-02 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 45b1839b-208c-3428-88fc-dac28f0b4a37 | -5.92035 | -45.52887 | 2025-06-02 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c0ef2d1-ad30-3dfe-9340-2026b662730a | -8.12891 | -49.58377 | 2025-06-02 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 30a26002-1e32-3c93-b5a6-7f0982211b1f | -7.02412 | -45.41846 | 2025-06-02 04:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0cd5735d-4b1b-3189-9b12-7e6dafe86151 | -7.3431 | -48.31301 | 2025-06-02 04:38:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00bc874b-7f32-36ee-86db-cbba8b177c21 | -9.39701 | -40.35958 | 2025-06-02 04:38:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 03c2082d-4f83-3ee9-8882-26fa569340b0 | -7.08123 | -46.55489 | 2025-06-02 04:38:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README6.md)
