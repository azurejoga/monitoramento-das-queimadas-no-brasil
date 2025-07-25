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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d59ba714-c10d-3a60-874f-fed0529dd88c | -20.05282 | -44.61068 | 2025-07-25 03:57:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1157e31-dfe7-3d47-8453-df0675937ad1 | -12.69549 | -46.99415 | 2025-07-25 03:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1c8cb39a-1ae6-31e7-8b1e-add47f05ad20 | -13.09783 | -52.13968 | 2025-07-25 03:57:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62f3f792-10de-3c81-9dfb-7f9fa719cc8a | -13.71751 | -45.68791 | 2025-07-25 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53eeb6b1-8351-397f-8c72-d514ab0505ab | -13.64571 | -45.71001 | 2025-07-25 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d156797a-e566-358a-8303-44be0adbb6d4 | -12.70719 | -46.98151 | 2025-07-25 03:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 619a5392-e2f3-3ef6-b725-f02766312ae5 | -13.40456 | -46.80981 | 2025-07-25 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7835a15-cfab-38d8-8cd6-14e50bafb070 | -13.7011 | -45.6849 | 2025-07-25 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 585b5e80-3766-3066-b81d-bc8c95ad4d9c | -13.21026 | -51.11623 | 2025-07-25 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c97bf674-c3e7-3bd7-bf57-fd94cf676c4b | -13.40357 | -46.8079 | 2025-07-25 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 952e1c88-4f60-3c85-abb8-fe8ded95d6a8 | -15.7125 | -41.08616 | 2025-07-25 03:57:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 47d53ebc-38a4-38e2-9b60-34b1392ff9ed | -14.65665 | -46.8326 | 2025-07-25 03:57:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a7dbfa2-f67a-389e-b40e-0fca7ef31a90 | -17.7039 | -44.31194 | 2025-07-25 03:57:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| be373496-265e-3d4a-8a69-deee41313528 | -13.7113 | -45.67508 | 2025-07-25 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 657cecd7-621b-3f43-9f39-ca9f072f3e06 | -18.72151 | -40.05646 | 2025-07-25 03:57:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1aa0c1dd-c459-39c6-8607-d409f417a6ac | -15.0509 | -47.68653 | 2025-07-25 03:57:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f4d19f72-d3c2-3387-b1aa-3fa9c8d70464 | -15.27872 | -47.1251 | 2025-07-25 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8200f229-1e3e-3ff6-ab82-c89018ab4732 | -13.64433 | -45.71761 | 2025-07-25 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 568b321d-c60e-39e1-88e9-080174507440 | -14.21594 | -43.95323 | 2025-07-25 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86eb591f-5b52-315d-8ae2-0ba04767b874 | -13.71064 | -45.67885 | 2025-07-25 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b55c6492-5c1a-35ee-80d0-6a82fe1d5abb | -14.30967 | -43.80068 | 2025-07-25 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8f879790-fb97-355f-8883-36f76521fa47 | -16.17712 | -40.06795 | 2025-07-25 03:57:00 | NOAA-21 | SALTO DA DIVISA | MINAS GERAIS | Brasil | 3157104 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 65e6c243-9310-3499-a03f-fa83157ff303 | -19.24884 | -46.95582 | 2025-07-25 03:57:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dafa8233-5994-313b-85e3-12fb253cd465 | -18.85395 | -41.99551 | 2025-07-25 03:57:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9746c77d-f69b-3378-bca6-4782b8030eae | -15.6174 | -41.34225 | 2025-07-25 03:57:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 49efd397-0930-30ea-8e5f-8d33f7e22faf | -14.94207 | -46.98249 | 2025-07-25 03:57:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e01475a6-f972-30ab-af01-4faefd0fdd36 | -19.42938 | -44.81189 | 2025-07-25 03:57:00 | NOAA-21 | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a68ebd05-a813-36bf-a7c3-6a6f0cad73c5 | -15.61797 | -41.33865 | 2025-07-25 03:57:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6a07d760-8ccc-38ff-8acb-0cd6775bc652 | -17.68661 | -46.8424 | 2025-07-25 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9000ceb4-9b28-3b7b-aad1-5057915dd40c | -15.60281 | -46.52396 | 2025-07-25 03:57:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d21034e-2721-3234-b3e3-669c69d6fbca | -13.21114 | -51.11186 | 2025-07-25 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8278992b-b146-301b-80c5-3adadbef1c71 | -17.59507 | -43.19975 | 2025-07-25 03:57:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6f1e9cf7-b926-3400-8447-b98efea754e9 | -13.40537 | -46.80535 | 2025-07-25 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f524773b-738a-3cf1-b3c4-00a3bfdcd15c | -16.60809 | -47.96897 | 2025-07-25 03:57:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a492b5ee-fe08-38cf-9421-1866c6020d15 | -15.57134 | -44.76176 | 2025-07-25 03:57:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ef99df6f-1c59-35ba-be79-9e27387c05b6 | -13.2149 | -51.11357 | 2025-07-25 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79bc9df2-bf65-390b-8263-f6444e7e9218 | -18.22572 | -54.55376 | 2025-07-25 03:57:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 16e66e0e-73b6-353e-bd4a-bb9f72e27ebd | -19.28973 | -47.42226 | 2025-07-25 03:57:00 | NOAA-21 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63d83b47-1319-32d9-8a46-6f057936cd1d | -13.70587 | -45.68188 | 2025-07-25 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1bf51915-0f0d-3ecc-83ae-8f441a882342 | -16.09167 | -45.1718 | 2025-07-25 03:57:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ed87e740-ecd0-3918-b839-7f9f68756a7c | -13.70997 | -45.68262 | 2025-07-25 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94cc0ae1-0b20-37da-b769-95ba64c6701b | -18.85454 | -41.99186 | 2025-07-25 03:57:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 79a67a2a-5134-39ec-ac50-5bf7f992f085 | -13.72161 | -45.6887 | 2025-07-25 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 170e25c9-e411-3928-9e5c-fd1d8aedf4e3 | -13.71817 | -45.68415 | 2025-07-25 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 374e51f9-91ce-3649-8864-564eb43cf360 | -16.81962 | -47.60104 | 2025-07-25 03:57:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f41a2501-c9db-3f68-8c36-1308e172a724 | -15.66467 | -39.17301 | 2025-07-25 03:57:00 | NOAA-21 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 52b6c028-cd10-3626-971e-7c6734e091e1 | -13.72059 | -45.68806 | 2025-07-25 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3fb7e64f-72f7-3d50-bc7f-d6b19e7fa74b | -19.52357 | -44.26168 | 2025-07-25 03:57:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ae5537e-7ab6-3190-9768-24878666938c | -14.93765 | -46.98194 | 2025-07-25 03:57:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f8715a8e-b507-36bb-9958-6b945dfceb06 | -20.35247 | -45.5358 | 2025-07-25 03:57:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a0432a46-affe-3da9-8b52-e486e97a0545 | -14.95004 | -46.9883 | 2025-07-25 03:57:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c0f16a9d-4186-32c3-b755-978c0d3ef3b1 | -14.74613 | -46.29861 | 2025-07-25 03:57:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51fb38c0-35f4-38e4-9c4a-c67ab5474803 | -14.9597 | -46.98496 | 2025-07-25 03:57:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e6f7a043-535c-33c8-ad77-d4a404978450 | -13.64693 | -46.81876 | 2025-07-25 03:57:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d6a6102c-61f7-3aa6-8bb7-cd2849101fbf | -15.82624 | -45.77842 | 2025-07-25 03:57:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7bfba7c1-789e-3f26-aab1-bace825a848f | -20.00055 | -45.39562 | 2025-07-25 03:57:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af0c3ffd-f857-39c9-b58e-e0c7bb1d2470 | -12.69711 | -46.98524 | 2025-07-25 03:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d30e8e0a-a085-3461-a326-6b5f61bcba8d | -17.34651 | -45.70621 | 2025-07-25 03:57:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3d6a25e-7b6b-398b-b170-771c8e25928d | -17.30361 | -44.85686 | 2025-07-25 03:57:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec8e6dcf-e22c-39ec-be43-a8614888b424 | -19.28825 | -47.42287 | 2025-07-25 03:57:00 | NOAA-21 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ff0b3e9-b78c-3408-a8e1-80c95e356a50 | -16.56276 | -49.05631 | 2025-07-25 03:57:00 | NOAA-21 | BONFINÓPOLIS | GOIÁS | Brasil | 5203559 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8d9b2ee4-3a45-3dbd-a8d0-05a74ab76d0c | -14.17125 | -45.34956 | 2025-07-25 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4009d0c0-487b-3431-bfd6-197f2f6064fa | -14.30678 | -43.79566 | 2025-07-25 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 687b0ea1-4e04-3d43-bbcf-3fb8836e3752 | -20.49766 | -45.48186 | 2025-07-25 03:57:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11deb42f-9556-3b14-b6bc-45e0ae0f533a | -14.74541 | -46.30254 | 2025-07-25 03:57:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7cf3bcd-7909-345d-b8f2-ef5b2eba832b | -12.70004 | -46.99502 | 2025-07-25 03:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be5438dc-a74d-3bd9-be61-c406e51be492 | -13.40441 | -46.80345 | 2025-07-25 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a97eef8-0bdf-3f1c-aeb6-2ac6f36e1774 | -20.22328 | -43.80302 | 2025-07-25 03:57:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 06edf5b6-8849-3668-ae0d-cce5c906b3c1 | -16.08784 | -45.17104 | 2025-07-25 03:57:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3211d659-00b6-3931-b5dc-25c57aa78684 | -13.64502 | -45.71382 | 2025-07-25 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 27ca32a2-88f1-3060-8d97-09e9a0287228 | -15.27803 | -47.1288 | 2025-07-25 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b6d6525c-1804-3d92-8b54-7e63872429c9 | -18.70341 | -48.25918 | 2025-07-25 03:57:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 270450c0-9528-3e55-9b0f-5d11b9228828 | -13.21399 | -51.11793 | 2025-07-25 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea1e5d1d-22be-3994-a1c6-04c9a4e6daf7 | -14.95644 | -46.9782 | 2025-07-25 03:57:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 94476152-4d47-34ad-b59b-255a24fe4139 | -13.71341 | -45.68716 | 2025-07-25 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc2f6bb2-3edb-37ae-807f-c3f2776abc93 | -17.75446 | -46.17656 | 2025-07-25 03:57:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 47128740-159f-3713-8c66-3b21377dfcf9 | -13.71197 | -45.67132 | 2025-07-25 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76f3c4c8-107a-3904-96cc-520ab3d156e8 | -13.71474 | -45.67962 | 2025-07-25 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1da5fb8a-9c8c-33d1-b2d2-6014dcb32315 | -14.94651 | -46.98294 | 2025-07-25 03:57:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| da176783-7639-3ee3-b675-3ca20335a1ea | -17.70465 | -44.30765 | 2025-07-25 03:57:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 90cfbaeb-9f3b-3419-8f7c-7419915d2fc1 | -15.28316 | -47.1256 | 2025-07-25 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 763dc77d-3615-363c-a936-d733dbebe1eb | -14.17062 | -45.3531 | 2025-07-25 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e89a781a-c9a6-37df-a5bc-eed8fb2cced8 | -13.70043 | -45.68867 | 2025-07-25 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 738065f4-726e-38c3-92ff-521ba61c4a8c | -12.69458 | -46.99914 | 2025-07-25 03:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 84af5902-c095-3402-a8be-d99e3d85221a | -15.59864 | -46.52308 | 2025-07-25 03:57:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 190103fe-27b1-3f7b-8f6d-57400a437a56 | -13.09678 | -52.14475 | 2025-07-25 03:57:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5985a67f-5a8b-3034-b9a4-df951550a872 | -14.30528 | -43.80439 | 2025-07-25 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29163e65-836a-3ff5-8adb-d15d1e3eb2c3 | -12.70089 | -46.99034 | 2025-07-25 03:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b45d192-1d82-365b-9449-c17f95299657 | -16.56419 | -49.05931 | 2025-07-25 03:57:00 | NOAA-21 | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd7bf7fa-54d7-3d15-8d01-efb30f83ac11 | -15.59791 | -46.52705 | 2025-07-25 03:57:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b2785d7-d493-31f5-8f49-2a2fa8830edc | -13.7199 | -45.6918 | 2025-07-25 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e73184fd-d179-300e-b954-23b7bb9f1408 | -13.69767 | -45.68037 | 2025-07-25 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c15e024-ea84-3417-b23e-8bb665196582 | -14.94747 | -46.9778 | 2025-07-25 03:57:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 955817f0-76c6-3369-b9b2-539b82dcc66b | -20.00421 | -45.39635 | 2025-07-25 03:57:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ca39badd-9dd6-301d-a9d6-1e9f12f916fc | -14.95205 | -46.97752 | 2025-07-25 03:57:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b992b29b-d320-3fd7-9be0-92254dbcb81c | -19.16535 | -46.5926 | 2025-07-25 03:57:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef3d34e3-2abb-3474-8465-79da1e0948e2 | -13.64845 | -45.71835 | 2025-07-25 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11800337-cfa8-3abc-bc69-dc55e74bf351 | -13.71606 | -45.67212 | 2025-07-25 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7ed6e1e5-c45d-35da-a72e-1d79b8a14b19 | -14.65231 | -46.83175 | 2025-07-25 03:57:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 590edd75-5b0f-31cb-9324-0c5ab9812794 | -13.71263 | -45.66757 | 2025-07-25 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README11.md)
