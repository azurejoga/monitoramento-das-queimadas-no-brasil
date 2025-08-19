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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2156a8fa-af8e-36f2-bd59-6d80da4898ea | -8.23874 | -47.85793 | 2025-08-19 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c8157bb-3432-3958-8684-385e47b77784 | -13.00902 | -56.84234 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 862bd11a-63da-394f-9c1c-99360c42acc0 | -14.84899 | -48.06598 | 2025-08-19 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0ef1f29-0b6c-30f0-8dea-f1353e55da10 | -12.73347 | -45.05615 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f83e271-0a58-33a8-87ea-6a2d27381dd4 | -12.97742 | -49.35905 | 2025-08-19 04:27:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85aa3e66-9386-3721-b8a9-9c2eedaf7659 | -12.77463 | -41.24953 | 2025-08-19 04:27:00 | NOAA-21 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2efceee8-12f0-39d6-ad57-c9328f2b74b3 | -12.99461 | -45.20047 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b6f72ed1-b299-3962-8c93-e1128425f4bc | -13.14309 | -57.15586 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a518099c-9d9c-3c40-8000-975acc90f059 | -13.59442 | -46.98776 | 2025-08-19 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f16a7616-02ad-3bdb-90f9-fdea7bdd6067 | -8.40253 | -49.50019 | 2025-08-19 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8bcf7be1-724f-3410-ad42-dc797d586b9c | -14.84623 | -48.06189 | 2025-08-19 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e493791a-521d-305a-b1b8-a8a2d3e27e9a | -12.99153 | -56.86739 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb5f49ab-120f-3cf7-b217-d33b369e38c7 | -11.85636 | -51.57863 | 2025-08-19 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c0fa9280-fc33-3971-be25-cdc239bcb21b | -13.60784 | -47.76199 | 2025-08-19 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1500bdd7-d369-3034-89fb-08c6bee028bd | -12.6559 | -45.80193 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| b480202a-cfca-31b5-ae5d-b9455e2d16c5 | -10.43823 | -48.80934 | 2025-08-19 04:27:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bbd2804f-802e-3c74-9d97-26cd4c4ab858 | -13.00269 | -56.84748 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7814dbf5-78c2-3612-8d09-7a27e63ad0e4 | -13.30873 | -50.8175 | 2025-08-19 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eda81164-9806-3c2a-8231-1e1a42dcb47a | -12.99166 | -45.19588 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8f358d11-ff4b-3c55-bb9e-96dcf59160ef | -13.35269 | -54.40796 | 2025-08-19 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 376138ac-1fce-34b3-bdc4-5e17fc2904f9 | -13.07997 | -49.33453 | 2025-08-19 04:27:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87a79432-aa1c-399b-b8a9-546c91ffdc82 | -13.14246 | -57.15917 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c41d128-0247-350c-b768-4a01e3fad290 | -10.61154 | -46.36238 | 2025-08-19 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| c930faa8-acc1-3d13-b2fa-47567402ca89 | -13.06593 | -49.33594 | 2025-08-19 04:27:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d1f2656d-54e2-3d8a-bf77-878f0cbac12b | -12.98673 | -56.84733 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4777c7e-75e0-38ee-8dd1-5afaff34c8ea | -7.68513 | -46.75401 | 2025-08-19 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 429059a6-aded-3624-bc41-ea29361408ac | -13.4817 | -47.07649 | 2025-08-19 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30c84549-0a43-3a03-99b3-2e4255283e04 | -11.86382 | -51.57997 | 2025-08-19 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0cdb66b2-2764-3bfc-a085-60dc34dad7b2 | -8.97143 | -60.49745 | 2025-08-19 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bdc43d73-4cc4-3ba1-9d61-0e9fa7f3c009 | -14.87214 | -48.0698 | 2025-08-19 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a6c3a1c-e0a1-3338-81d9-97f33e4decf7 | -12.10807 | -47.91504 | 2025-08-19 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4cec6a4-595f-3342-9def-07c04ec608b4 | -12.99655 | -45.1857 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0af2802c-5c45-302b-931a-09fe45e804bf | -12.98427 | -56.84933 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6f7ccf1c-48b8-3002-bd7d-43cbe0c451a3 | -13.86935 | -45.54797 | 2025-08-19 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e374ea8d-8ff9-3624-bc62-6e9c49837016 | -13.15328 | -54.91977 | 2025-08-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 789170d0-eac6-3730-9996-27e1a6c69d27 | -9.33435 | -48.5151 | 2025-08-19 04:27:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70565690-3b01-3a47-ab33-a3be97cf274d | -8.77507 | -50.01703 | 2025-08-19 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88b3541c-f791-3f93-ab3b-0ae94f146d7f | -12.12074 | -47.89908 | 2025-08-19 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf5b85ec-4329-318c-8725-21a3d6ab0f30 | -12.99063 | -45.20137 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 329b56da-a5cd-397b-9c85-06493d7c4a14 | -13.73748 | -52.02415 | 2025-08-19 04:27:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87442e54-c0f1-35ba-9865-4f2def5b5b71 | -14.45772 | -48.48201 | 2025-08-19 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f53fc5ba-8ce0-393b-9a8b-b603978cce41 | -12.99058 | -56.84413 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b496f153-39d8-30d3-94ef-e72a99c4ed51 | -11.66845 | -46.87086 | 2025-08-19 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ec59430-d343-3030-8626-f25431e80ff1 | -7.97194 | -55.30179 | 2025-08-19 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a2f478a0-9780-34cb-92b4-8655be3c8341 | -12.98794 | -56.84118 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b38e1671-1abf-3944-83ac-da91e594ffbe | -7.25394 | -50.17747 | 2025-08-19 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bd20d918-0ac7-3b0f-9993-90803f8d1149 | -8.22375 | -47.28804 | 2025-08-19 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 607c25a5-d633-3260-942e-848775eec20a | -13.17686 | -54.94361 | 2025-08-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0bd5d253-8e4b-3632-8388-3117ba67d144 | -12.97913 | -56.8589 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f960f66-58c2-31e5-bbd8-0434f8f74f92 | -13.0933 | -46.83872 | 2025-08-19 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a3391b5-926d-3283-b53f-5d273792b3b6 | -14.87159 | -48.05144 | 2025-08-19 04:27:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b89817ad-e0e2-3fcb-a2e6-bf551040f722 | -12.96464 | -46.15339 | 2025-08-19 04:27:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 66c685a0-4e3f-3c26-8071-61b743004f93 | -12.99819 | -56.84325 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a544a879-fbb4-3a13-9fef-361545c1ce17 | -13.25577 | -50.80833 | 2025-08-19 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 42d02ec9-80ae-3206-a268-3643646e4005 | -13.17235 | -54.94275 | 2025-08-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b99b731-3a56-3132-bccd-eb0d094dd0de | -12.04198 | -44.01773 | 2025-08-19 04:27:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 63dc3922-5e9d-3a66-836a-03aa9182ada2 | -12.99213 | -56.86418 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cdd3ef64-cf0a-3e1a-9b49-33af4a82bb4a | -12.99475 | -45.19786 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2e703ba6-83ce-3694-ad6f-60f5e400db4b | -12.2971 | -50.02023 | 2025-08-19 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1aa8454-ab90-332a-b93e-5e72958887d0 | -12.99326 | -56.86847 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5f6d932-839b-38cd-be0a-40a454c80f18 | -12.46468 | -46.93079 | 2025-08-19 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 432a9546-3967-3730-b7f1-628b3630c908 | -12.92589 | -46.10576 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0061103c-098f-3426-9b3e-b2caee2731b3 | -12.63738 | -46.91082 | 2025-08-19 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70f37e44-f7e1-30db-96d2-593fc6a3a107 | -12.64009 | -46.89301 | 2025-08-19 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b66cee1-2027-3c27-977a-461191334c8a | -12.03827 | -44.01721 | 2025-08-19 04:27:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3c4190c0-dfe5-3c24-a025-fc0dc9f9c051 | -10.6045 | -52.78491 | 2025-08-19 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 992a31f3-2fb0-349a-9208-f5b03a09cc03 | -7.76079 | -49.85519 | 2025-08-19 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c17ec50c-36c2-3e99-88f2-d473094569a1 | -11.86086 | -51.5747 | 2025-08-19 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 709e9772-314d-3f76-b4cf-6e31fb1219b8 | -13.55666 | -47.01088 | 2025-08-19 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f02ffedd-15a9-36be-8df1-5353ca171b75 | -7.27443 | -50.16757 | 2025-08-19 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0320375e-12fe-3084-855b-5dff5e28f13d | -13.29814 | -50.81567 | 2025-08-19 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b8d15f93-24f4-3c85-830e-bddd9808651d | -13.57726 | -47.01048 | 2025-08-19 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59bb5fb9-628c-36af-a51d-1ff8add9a510 | -13.31571 | -50.7975 | 2025-08-19 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e397672-6c6c-3bf6-887d-67a815f7762b | -12.99595 | -45.18976 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d52089d0-1a36-3f98-bb66-ce227d9f5263 | -13.59054 | -46.99076 | 2025-08-19 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a622d3bf-ca00-3e79-b014-88850e90ae39 | -13.13756 | -57.15691 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67fba0b2-622a-371c-996a-b9118a726fa1 | -13.16872 | -54.93717 | 2025-08-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a997c72-18ff-3030-8cbc-ed7b8f2aacc0 | -13.07938 | -49.33818 | 2025-08-19 04:27:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da4660f5-4125-3cd4-9543-a763df52f0a4 | -12.97976 | -56.85571 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee277508-162c-3300-b8c7-ddcfbf9c0182 | -8.0832 | -46.66453 | 2025-08-19 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80c32780-fbe3-3f02-9855-700468def11b | -12.99108 | -45.19994 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f10fc100-0c02-3a46-8163-595b2c1b4566 | -14.18009 | -45.32159 | 2025-08-19 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7711434c-5f35-3686-b349-9d006c82796c | -13.14278 | -57.158 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 608c65ab-2001-370a-a8a8-ba9861dd09fa | -13.40702 | -43.68824 | 2025-08-19 04:27:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b92a066c-bf2a-3df3-88c2-91d5373f00d9 | -8.40316 | -49.49626 | 2025-08-19 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f2e72bf-d047-332f-8edd-ce0eb80a9987 | -9.17098 | -59.62042 | 2025-08-19 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 265ce48c-f4a1-33ef-af58-c0335bdd273f | -11.45232 | -47.32347 | 2025-08-19 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff7aabee-9d0b-306a-957f-1f6f04929863 | -13.31011 | -50.80905 | 2025-08-19 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 44fddbdf-a627-3248-be97-0a09d1470fd1 | -12.7323 | -45.06425 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b25b5f82-c66e-38be-abd2-5ea38a577394 | -7.68567 | -46.75054 | 2025-08-19 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1ad67982-05d9-339d-bd81-7f03494c9a2c | -12.46801 | -46.93132 | 2025-08-19 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f4f6aab-52f2-3450-9410-aeb0f1e710b4 | -9.71811 | -51.97208 | 2025-08-19 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 1f97455c-f650-3186-ad8f-a19ee4f5c5fa | -13.31074 | -50.80531 | 2025-08-19 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7bc65413-322d-3dce-9ac5-d8179f4a22d8 | -13.48116 | -47.08009 | 2025-08-19 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d61f551-1a29-3edd-9c3e-705f97679c4f | -13.19588 | -50.75314 | 2025-08-19 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1fad1001-c49f-3277-b34c-b6b401245920 | -12.64435 | -45.04815 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8c4d336-d4fa-3994-bda2-97f74e7e3f1a | -10.58285 | -49.13366 | 2025-08-19 04:27:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62ab80cf-d900-3260-bc6a-4602499fe0a8 | -13.31639 | -50.79346 | 2025-08-19 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 178f6a10-1849-323f-884f-33fda5d695ed | -9.71333 | -51.97635 | 2025-08-19 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 369cbe1c-1f85-3307-901c-8e6b490cc7e0 | -13.14372 | -57.15257 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README30.md)
