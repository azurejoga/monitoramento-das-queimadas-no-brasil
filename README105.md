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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3142c969-57ed-348d-a93c-306d43e7302e | -1.49652 | -47.81152 | 2025-10-17 05:08:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3c2367b-a141-30df-8393-bc0ffc9af6d3 | -2.86739 | -50.72954 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8d34736-7098-33b7-a259-0938e829360a | -3.2452 | -45.97432 | 2025-10-17 05:08:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| edb2a9da-613e-3ac9-a922-c2d1157abf29 | -6.29111 | -44.01638 | 2025-10-17 05:08:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 92711571-c1cf-3e52-a0ac-43f844efbb48 | -2.64773 | -48.38965 | 2025-10-17 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f2d09c1c-c341-3cc2-a42f-1fcedb638473 | -3.8417 | -47.0674 | 2025-10-17 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9a232f2-383c-3420-af6d-49d5193d197f | -1.60794 | -55.72587 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 862024f5-05f9-3a5d-b862-95330670e60e | -2.87947 | -50.73848 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 435776b4-eef6-3a17-8297-2c7a7cf87f26 | -2.92687 | -48.30395 | 2025-10-17 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3df7a9ab-5194-3ac4-b2e8-4b44065b5061 | -3.47209 | -50.02421 | 2025-10-17 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9aecd923-b58f-3590-b7aa-e2d92ca6bce9 | 1.87385 | -55.84747 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 01c1aafd-0da3-3543-870e-09ca0f8d298a | -3.774 | -58.52483 | 2025-10-17 05:08:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c29eedec-1672-34c1-bfd1-d6f458568983 | 1.81772 | -55.72923 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94c8587e-45e5-3bbb-a580-04f1d1872d66 | -3.5044 | -52.49405 | 2025-10-17 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| a6169aec-8f7e-30c8-be2a-61ca59a99596 | 1.73719 | -55.77702 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31e4e985-2a2d-34e3-848c-a90e45a7353f | -5.87962 | -44.83862 | 2025-10-17 05:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 428f51da-17d4-33a0-8dcc-80f9c732e51e | 1.02325 | -51.11368 | 2025-10-17 05:08:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 17b17bfc-14d9-38ee-86fa-1f4bc4c9b60a | -4.4239 | -47.75725 | 2025-10-17 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb3c17a6-9f1b-3b9c-8211-251313cc0787 | -3.52813 | -50.30843 | 2025-10-17 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4d15a212-a717-36e7-81d8-262e9bbe8784 | -2.87223 | -50.72945 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e70ebbc-4fd3-310c-bb56-46dc7ac2af56 | -3.66031 | -50.26622 | 2025-10-17 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd4f94e1-a3f1-3722-be4a-c063acf70c9b | 0.8758 | -51.12654 | 2025-10-17 05:08:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1148f6e3-0d87-315f-88c5-953da46a65ad | -4.41987 | -43.40111 | 2025-10-17 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 00eef703-deab-3b08-b064-fcfccb0e5dde | -2.86917 | -50.7456 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb90b3b7-0bf5-3d29-bb4d-e70cc364e5b4 | -5.24356 | -50.96241 | 2025-10-17 05:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 448bf0e1-39f8-3c8c-8287-6ba8ce1440ab | 1.82298 | -55.71778 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8941168d-a93c-3a71-8d7d-437a4dea4f10 | -2.68889 | -51.84564 | 2025-10-17 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70b3ae2e-c202-30d7-9c36-461e90cf14f6 | -3.53773 | -49.00685 | 2025-10-17 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9efa875f-b1d4-36f1-baf8-f6e07faffb69 | -3.5152 | -50.21546 | 2025-10-17 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f0ccdfe-8d50-3e85-85e3-563be4d7c1ad | -1.6041 | -55.72879 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fa5b84a-e36b-3537-802c-7129701ef307 | -4.39893 | -43.39862 | 2025-10-17 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b9ddb599-cf12-3832-9131-85f5a7e7818f | -5.87788 | -43.84972 | 2025-10-17 05:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9bba506a-85da-34e2-bd78-7bb116e54127 | -4.41197 | -43.40676 | 2025-10-17 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4fd4d375-175f-33f1-9146-ac2432971447 | -4.21872 | -48.36104 | 2025-10-17 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80fd5699-1456-3769-877a-1f736a618c7c | -3.50582 | -52.48472 | 2025-10-17 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 194205fb-9dc5-3544-b8f0-afc3f4f1b3e4 | -5.98936 | -44.15802 | 2025-10-17 05:08:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0ec7407b-70d6-3b4f-a00c-8e8f16957e09 | -6.32184 | -43.62096 | 2025-10-17 05:08:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8eb1e7e6-d0ff-3af6-8349-ce9c8a30db13 | 1.78743 | -55.73042 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9bb14aa-f280-32e1-92ac-61ee6addc7f8 | -5.03743 | -49.22058 | 2025-10-17 05:08:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4835231-d49b-37cd-8f57-a8b4de33d3e1 | -3.54712 | -54.69553 | 2025-10-17 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c73c7cb-7c48-3477-a233-efb55d189015 | -1.43831 | -55.24955 | 2025-10-17 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1be2f6d-5a06-3df3-9861-339ca9322e91 | 1.78869 | -55.88898 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4f02a7c-a72f-3a7a-83db-6122fb35de98 | -4.61154 | -50.82705 | 2025-10-17 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5f6bf48-2bb5-358f-b9fa-07f93f0b2e64 | 1.09959 | -51.14616 | 2025-10-17 05:08:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a6deea4-241f-3559-ad83-7ba63947e2ff | 1.77529 | -55.73936 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b84cc67e-92d9-3e7b-8fee-0017e3208933 | 1.80183 | -55.92939 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7768c7a-591f-3e8e-a231-2d88d6e9e7c2 | -2.73832 | -49.38904 | 2025-10-17 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3e7216ce-2230-31b1-84be-4d20f928c59f | 1.31296 | -51.24971 | 2025-10-17 05:08:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be4b1b45-101a-3383-abb9-ec2d4c66b9f8 | -5.29347 | -47.93335 | 2025-10-17 05:08:00 | NOAA-20 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 07c027fa-9844-3258-b612-57585c5e55b0 | 1.79906 | -55.93335 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72b38d34-e0f7-33b9-9b37-ef6fa5e03ee7 | -1.18243 | -55.66631 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6b76c19-38f9-35b9-9514-b80945f2d510 | -3.12822 | -50.21507 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e156730-6848-3234-b93c-875eba1a0205 | -3.27184 | -53.25742 | 2025-10-17 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8b76619-db32-38e1-81b7-f4aa795bf879 | -5.88536 | -44.75087 | 2025-10-17 05:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2df9daf8-9b57-36a4-9924-c3aa98fdb04b | -2.9608 | -52.50611 | 2025-10-17 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da5e981a-5a1e-3a5a-a254-989ed0fe7c98 | 1.7322 | -55.78837 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| aa437f21-0414-3801-934c-9cc38f9b3e3f | -1.422 | -57.85596 | 2025-10-17 05:08:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8fa3308-0084-3c85-97d9-d0e18311d14f | -4.26294 | -49.69311 | 2025-10-17 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bd3c0cbe-1dd3-3d11-8e4c-0b481e03e868 | -5.50016 | -51.1578 | 2025-10-17 05:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b27370d2-5caa-3b3a-8b57-9adbb8fb0b9c | -3.47016 | -51.66953 | 2025-10-17 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 512c9fea-747c-347a-926c-3dee32372290 | -3.41395 | -50.13974 | 2025-10-17 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14acb72c-9fa9-3f2c-9506-9b9a1293c392 | -4.40411 | -43.41874 | 2025-10-17 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fc833888-c3d1-3dda-a11c-0d225f4c3bf3 | -2.71147 | -49.41219 | 2025-10-17 05:08:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4d855a7d-f660-34b1-b71b-2161b1e8ca36 | -4.40408 | -43.41246 | 2025-10-17 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 93d38bd9-48fb-303d-b236-a5413b9ae0b3 | -7.10921 | -44.74506 | 2025-10-17 05:08:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 28cad270-d223-39d3-a463-0662b15f0119 | -6.29075 | -45.50307 | 2025-10-17 05:08:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd3ff5dc-da56-3b93-aabb-8543625c2f3c | -2.73879 | -49.3875 | 2025-10-17 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73f0efd0-4074-34a0-a7b0-d0165056c719 | -6.29303 | -45.53263 | 2025-10-17 05:08:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e77574d1-0b01-38b2-a107-ab35ad76f744 | -3.82386 | -52.07983 | 2025-10-17 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dfbba91c-2e80-3c5b-bbcf-bb3d7f9292ad | -1.69252 | -54.71614 | 2025-10-17 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5698e8b5-5d76-3a28-a77e-db8d5a4918a9 | -2.87159 | -50.73018 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab6a558b-b3da-3a67-b0eb-6982ed97269d | -7.34421 | -43.86759 | 2025-10-17 05:08:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b85fb418-a9b0-3330-9957-e41e420e37d3 | -1.49105 | -47.81364 | 2025-10-17 05:08:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dceeb7dd-cd2f-3c2b-ad4d-b09472c814ab | -7.35206 | -43.86227 | 2025-10-17 05:08:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bdc0f739-be48-3136-93eb-8d7e539ef206 | -3.78939 | -51.78559 | 2025-10-17 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c0a7f6d6-3f81-34a6-b34e-000d95571847 | -2.97801 | -49.22363 | 2025-10-17 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aab72e23-7d31-3c0b-a869-48e5b4a569c3 | -4.72367 | -46.1593 | 2025-10-17 05:08:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b500def-20dd-356b-9000-fcfdec62dbdc | -1.46432 | -54.95287 | 2025-10-17 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6bfaaa3-cae7-36c7-ab4a-4ebd1676f522 | -2.31215 | -57.16056 | 2025-10-17 05:08:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c64d5116-385d-3759-963a-b3446f12b48e | -3.82094 | -52.34399 | 2025-10-17 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eda28d2e-63d0-3dcc-9cdd-b7bd90b906f1 | 1.10167 | -51.14856 | 2025-10-17 05:08:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e3acf56-146e-37dc-8b72-bef1a7572996 | -0.89705 | -47.54549 | 2025-10-17 05:08:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86831262-2dc6-3438-ac88-4952e6d4f388 | -5.8846 | -44.7563 | 2025-10-17 05:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 137bf97b-a86e-3213-9084-7635538cc2f7 | -1.89401 | -51.01448 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b2c02cf-e2db-3990-8ffd-6cab33e5e42c | -3.68115 | -47.63152 | 2025-10-17 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 625252e2-fa6f-32c1-abc0-aa89ceac2a59 | -4.60758 | -50.9129 | 2025-10-17 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fec99ac3-f27a-3099-90df-3f02bbc4055e | -2.73902 | -49.38428 | 2025-10-17 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a27ec15-5b0b-350f-ab86-469bb20cfee1 | 1.06082 | -51.22563 | 2025-10-17 05:08:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 562cfd77-e1f4-3368-9e2e-e95ac089063c | 1.90353 | -55.64887 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb157fc0-f65d-3da6-9d08-9b477a3a170c | 1.77583 | -55.7428 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 585687a7-7cd5-3f93-bc52-05637e9f8fe0 | -4.39711 | -43.4116 | 2025-10-17 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 17445dc7-3919-3d29-bac4-f4fd19d7a537 | -3.84117 | -47.07094 | 2025-10-17 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 270e0282-62cd-319f-bd0e-701d6f1a4a00 | -5.03629 | -49.22203 | 2025-10-17 05:08:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 023709b7-3f6b-313a-86bc-cd82e12e4f4a | -5.85272 | -43.87804 | 2025-10-17 05:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd5f1b43-9f83-3fd5-9de6-72bad439c5a9 | -5.29394 | -47.93008 | 2025-10-17 05:08:00 | NOAA-20 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 741576ca-efb4-3f6f-ad68-68e5596ccbf0 | 1.78419 | -55.92507 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7d94738f-b6bf-3552-a387-8628fee6d46c | 1.78814 | -55.88551 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c7d808eb-c6a1-3d7a-805d-7423d9939364 | -1.11545 | -54.06454 | 2025-10-17 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ebbefbf-9cd9-3683-a555-2948054deadc | -0.8966 | -47.54847 | 2025-10-17 05:08:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6771ca17-5931-3164-9a61-7f38fed24327 | -4.42438 | -47.75393 | 2025-10-17 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README106.md)
