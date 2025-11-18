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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c0d273a-5368-3a9c-be71-3ee8004417f0 | -3.66391 | -50.214 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f4d063bc-8759-3d90-aa2d-a97f44eaa754 | -3.84829 | -51.0578 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a00de696-c58a-3c1b-9938-90bb443152b4 | -6.15689 | -46.10413 | 2025-11-18 04:48:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6814f0d8-467b-364d-ad7c-dc3b8a501a33 | -4.13781 | -52.12027 | 2025-11-18 04:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1e31dfb-bfda-3593-a54b-134127c43fa2 | -3.51465 | -50.34247 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 719dd0e1-7d7c-366b-898e-9901b6cad0e0 | -1.34347 | -49.32286 | 2025-11-18 04:48:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 7364cb1c-be91-3500-9724-c23499fba141 | -2.29502 | -47.22875 | 2025-11-18 04:48:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1eec5498-32b9-3d58-b307-b754f4e438ad | -3.07521 | -50.2308 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d1f79a52-541f-3528-b0a3-6809e88a3b36 | -3.68933 | -50.54297 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c47e036b-8d35-3914-9701-918c5df7fa52 | -2.52825 | -51.1869 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84c65f46-e024-3eaf-8416-dcea7d9bf9f8 | -2.49222 | -49.33811 | 2025-11-18 04:48:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63012159-2283-3026-b706-98c6093f540f | -4.67484 | -50.71252 | 2025-11-18 04:48:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1827a138-b006-397d-9a30-488f72f58055 | -4.19427 | -44.23343 | 2025-11-18 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| df3becfb-c073-3afc-9da4-92bdd2639563 | -4.135 | -52.1161 | 2025-11-18 04:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e9002072-fb5f-3c11-a2a5-6f6bf1396110 | -4.01619 | -47.4149 | 2025-11-18 04:48:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d05a839-e223-36d0-9557-9b32723c9781 | -3.72024 | -50.51955 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0653848b-5d63-3c71-973b-34d1df238319 | -2.51563 | -47.81903 | 2025-11-18 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 295965bf-e180-3971-b641-56a84605d431 | -4.22466 | -53.50601 | 2025-11-18 04:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ec94758-0345-345d-843d-342b76392e26 | -2.52546 | -51.18284 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7d0028d-0e29-33bd-ba73-de82bca7e308 | -6.6677 | -42.03135 | 2025-11-18 04:48:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| c7a029a9-348d-3132-af88-942b70fc4878 | -3.78434 | -45.589 | 2025-11-18 04:48:00 | NPP-375D | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fecf359b-16be-3ad0-9691-70e22fc365e9 | -3.47538 | -46.07168 | 2025-11-18 04:48:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98ea49ad-aff1-3fcc-b044-7bb630360b9c | -3.32609 | -51.51131 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae8019ee-c11f-3a55-937f-eb8746897dc9 | -3.2379 | -50.50709 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 222e32cb-c468-325a-af89-01ca1c6c9e8c | -1.43322 | -48.90486 | 2025-11-18 04:48:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52bd460b-f807-3015-a6ea-0682b4be835e | 0.27574 | -51.07286 | 2025-11-18 04:48:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e38fbf2c-a8cf-3dfa-af92-ac6bef6aa4e9 | -5.25156 | -50.68005 | 2025-11-18 04:48:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1229b3c-a419-334b-866c-567137416b49 | -3.30041 | -53.85387 | 2025-11-18 04:48:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d705575b-95eb-36a4-a06e-5be5c34de50b | -6.4022 | -42.32824 | 2025-11-18 04:48:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| adf1d0dd-0b9c-37bf-a3e2-c5bd0637a8dd | -6.54975 | -46.63381 | 2025-11-18 04:48:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e5d1ccb-eead-3092-a9d2-887ec946bb79 | -6.40773 | -44.19424 | 2025-11-18 04:48:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7435486-4d27-3230-b93c-772ccaa06083 | -2.95075 | -45.34471 | 2025-11-18 04:48:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 97006f42-a8d7-38e3-b2c6-8dab31e3116d | -5.47872 | -44.69076 | 2025-11-18 04:48:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c00f1e2-5370-36de-96d1-c22a31d2162b | -4.19868 | -44.23406 | 2025-11-18 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4b6889f6-fddc-3e4c-a8ef-152694c14fb8 | -2.47128 | -48.22758 | 2025-11-18 04:48:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 384c5b89-dea5-31a1-89ab-0cd26c79b3ff | -6.29068 | -43.80759 | 2025-11-18 04:48:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5cf05a4-7f97-3e19-9f74-d3517c5eeb7a | -3.23127 | -50.50605 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4cb724a-6f78-343f-94cb-beccbf2aee8d | -3.10616 | -53.13814 | 2025-11-18 04:48:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 917e1c7e-abe0-3e57-a145-f3cd5c67a40e | -1.3396 | -49.32581 | 2025-11-18 04:48:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef6075c8-b0e4-353f-876e-85e2386e948b | -6.22052 | -46.8798 | 2025-11-18 04:48:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0438fe6e-6368-3dc9-b5cb-c49b2dc6616e | -4.17665 | -44.23072 | 2025-11-18 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| a60d52e8-c203-3e1e-a845-e85568c8cfe7 | -5.18769 | -50.61274 | 2025-11-18 04:48:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ad7e758-2297-3d88-967c-69aa66747c02 | -6.67834 | -40.89092 | 2025-11-18 04:48:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 08c9d6bc-214e-32fe-9ab0-62714d507e99 | -1.09141 | -54.20967 | 2025-11-18 04:48:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb1936a3-5b27-3d6b-96d6-15fae7a05063 | -3.33001 | -51.50829 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6cad2f34-9db2-353f-99ed-c92448d68e9f | -1.9107 | -48.795 | 2025-11-18 04:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| f0ca0d5a-b4a8-3f28-bef9-008e30278bc9 | -11.6755 | -44.7342 | 2025-11-18 04:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 9d28da66-adbd-3cd0-896e-717573139a4b | -4.1764 | -44.2257 | 2025-11-18 04:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 8d1d2833-6d77-394c-a08e-a080b546cc38 | -9.3969 | -48.4523 | 2025-11-18 04:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| d04114bb-e8f7-3420-81cc-c2016e69300e | -11.6563 | -44.7371 | 2025-11-18 04:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 74eb692b-829e-35d5-809c-b6d6ba5e79d3 | -4.6361 | -47.9453 | 2025-11-18 04:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 32df1c11-6861-3557-82a1-a7c0359a5227 | -1.3373 | -49.3159 | 2025-11-18 04:50:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 65697f24-ee3f-387c-ba0c-a7c5afc4df67 | -7.3387 | -44.43357 | 2025-11-18 04:50:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f4b44ee-27f2-3b64-9ea3-505f942ee46b | -9.06083 | -45.42167 | 2025-11-18 04:50:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 820d3f70-de44-3c3c-a49c-e6eb523a41ae | -10.37831 | -49.91696 | 2025-11-18 04:50:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ddc746d6-81ee-336c-a7bc-e38a29c9b1b4 | -6.92877 | -45.34727 | 2025-11-18 04:50:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 02c10892-c8da-3637-a6d3-7136e56b22b5 | -13.89965 | -47.49191 | 2025-11-18 04:50:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 31e28ebe-9246-3067-8a06-98989ce901e0 | -12.69995 | -46.79278 | 2025-11-18 04:50:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f23535f7-7d32-3764-ae37-6d086740a2d6 | -9.88584 | -44.18572 | 2025-11-18 04:50:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7827e5d7-f546-31dd-a526-056877a1e810 | -11.39579 | -43.3158 | 2025-11-18 04:50:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d189ec0-dcea-3759-8f07-6c649424685c | -10.85848 | -44.09653 | 2025-11-18 04:50:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5fc7715a-ffb8-3fb5-8794-be1abbc3c751 | -12.636 | -48.86604 | 2025-11-18 04:50:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85442608-3bad-3d6c-b5b6-7efef2bc2133 | -12.89085 | -54.75212 | 2025-11-18 04:50:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c1f93890-9fa3-31bd-a669-0d51def94c2b | -11.88443 | -44.21109 | 2025-11-18 04:50:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b813c0be-4b14-30b0-93bc-1a67ddbc072c | -13.90281 | -47.49539 | 2025-11-18 04:50:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3d08dcdd-1e1d-32b1-a298-2d1c2aaa1f85 | -8.01121 | -46.57854 | 2025-11-18 04:50:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e8740c6-4ad3-3b20-b749-88f5e0ff243c | -10.61136 | -42.31811 | 2025-11-18 04:50:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a291f2fe-a56f-3e3f-9f6c-9e4820eafb30 | -12.1607 | -47.42395 | 2025-11-18 04:50:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2d5ab0d-6d79-3bc7-9a9f-591b2123a6a3 | -8.93102 | -49.84558 | 2025-11-18 04:50:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69e2933c-5d4a-3e7c-a875-53c29d9ea822 | -11.01668 | -49.03811 | 2025-11-18 04:50:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9872c4c-e228-38e9-8012-13b018466c08 | -10.34076 | -49.63795 | 2025-11-18 04:50:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08c56158-e17d-3114-8bad-5d03213227f9 | -8.7978 | -44.39371 | 2025-11-18 04:50:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d7e9057d-6669-350b-bbc7-abbb2523151d | -10.35589 | -48.9229 | 2025-11-18 04:50:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 87743aa4-3c07-3a2a-ac06-379b9198ed72 | -7.33481 | -46.17074 | 2025-11-18 04:50:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f032a609-303d-39f4-84a6-29ac94b1bafb | -8.93444 | -49.84611 | 2025-11-18 04:50:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab9163a4-5ea6-3a73-9095-64ac208bfcb5 | -11.20577 | -43.17903 | 2025-11-18 04:50:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 63f0e037-e2c5-35ff-8b93-cdeecca64791 | -7.45631 | -42.76089 | 2025-11-18 04:50:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e5fe2850-27bd-3e18-9892-1b5cc57edac3 | -10.37991 | -47.2864 | 2025-11-18 04:50:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ba196a4-ff0a-3686-9238-6b85298b4663 | -10.35167 | -48.92648 | 2025-11-18 04:50:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cc533294-0170-3e8b-910d-5a2e9164bf37 | -7.42 | -42.75876 | 2025-11-18 04:50:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4bb8424b-2a55-3dc9-ae50-a0cda8f918e0 | -10.02745 | -44.07137 | 2025-11-18 04:50:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9a454344-7118-3fc1-abe6-8bfa2dfd3a20 | -8.47184 | -47.98134 | 2025-11-18 04:50:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fab0ae2e-fbfe-30c8-a7ba-c617e119c3ac | -9.20846 | -48.88628 | 2025-11-18 04:50:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d13450cb-82d7-30df-8644-9e9cb6b36682 | -6.64693 | -52.44169 | 2025-11-18 04:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 82ab4381-5d25-3eb7-a2ab-26fe872d16bc | -10.64807 | -49.72666 | 2025-11-18 04:50:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df9578fd-f85f-3cd0-b6d3-bfd20a6cfd6b | -7.41016 | -42.7543 | 2025-11-18 04:50:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 09d0c60f-5c36-3ccb-a84d-b01b1149ec4e | -8.86326 | -47.32278 | 2025-11-18 04:50:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 596c95d0-493e-3d9b-9e36-5dda75bf03ee | -5.09564 | -56.16426 | 2025-11-18 04:50:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5a7dbf9-c8ec-3557-9da2-84ef57723956 | -10.85565 | -44.89338 | 2025-11-18 04:50:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 701f043b-56c1-3f6e-9b2b-73985fefec73 | -10.51663 | -43.95715 | 2025-11-18 04:50:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 400d8624-acd4-32a2-8ff8-47f184434033 | -7.30752 | -45.76188 | 2025-11-18 04:50:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2aef6522-61f8-3e28-89cc-8ea247971cd3 | -7.85961 | -46.87012 | 2025-11-18 04:50:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a92a8a6c-690a-3db0-a784-e11d191ff396 | -11.51911 | -48.95747 | 2025-11-18 04:50:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 970198b7-9702-3f5d-92f6-449e51468077 | -6.32197 | -55.16347 | 2025-11-18 04:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f3f3801-5bdb-3ab3-b6cb-59ac46966c97 | -11.20619 | -43.17579 | 2025-11-18 04:50:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 906f46b7-f2da-36d0-963c-f84b9f476d33 | -9.39172 | -48.45169 | 2025-11-18 04:50:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 6e041bee-bc96-387a-89a8-f30edd9fa7f0 | -6.20519 | -54.72166 | 2025-11-18 04:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a1d414f-3551-3f81-92d5-08664a805f78 | -6.94284 | -49.66483 | 2025-11-18 04:50:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98b3b70c-8624-3781-b709-37b2746ca0ad | -6.72516 | -46.31389 | 2025-11-18 04:50:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed2e6f5d-abfa-3536-a541-5848ae24c1e0 | -10.50747 | -43.95013 | 2025-11-18 04:50:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README43.md)
