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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38fa7d73-5213-355c-a4d6-86f905f20932 | -7.03636 | -49.28432 | 2024-10-26 04:44:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 331469df-876e-32fb-9388-5b6495b80b1f | -7.0358 | -49.28796 | 2024-10-26 04:44:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a49af68-94a2-3980-be98-bdd3f1b99f22 | -7.03183 | -49.29111 | 2024-10-26 04:44:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0eab1ced-75ff-3bcf-b354-cad93a04ddb7 | -7.02664 | -49.27924 | 2024-10-26 04:44:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb82bd47-b80f-3e16-bf8e-161cdea23913 | -6.68641 | -48.75398 | 2024-10-26 04:44:00 | NOAA-20 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5be64c9d-8bfe-3727-a6de-300e74f3d819 | -7.29481 | -49.28881 | 2024-10-26 04:44:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5dfec3cb-eab0-331b-a484-ccd56b16531c | -7.13272 | -49.27182 | 2024-10-26 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eee19bc9-2bae-3d00-9233-430fcf8f0a52 | -7.11809 | -49.14 | 2024-10-26 04:44:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 559a7277-f961-34ad-aa5a-628de15217f3 | -7.11632 | -49.17422 | 2024-10-26 04:44:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed7d4a63-7ab9-3b14-b3fe-63a00f12a942 | -7.10888 | -49.1769 | 2024-10-26 04:44:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 49c2c1be-6178-3475-a578-06d72e7e8903 | -7.10377 | -49.14165 | 2024-10-26 04:44:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e6ed8594-c7ca-31a2-9b11-06a1f1942b83 | -7.10264 | -49.12614 | 2024-10-26 04:44:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ed35d033-9e87-3d4a-be91-42097040a88b | -7.09632 | -49.14438 | 2024-10-26 04:44:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b501907-c90f-3fe7-959c-adb10ee7b9ac | -7.09346 | -49.14011 | 2024-10-26 04:44:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09bdf5d0-d164-3f06-a925-f1955c4d5b46 | -7.09003 | -49.13957 | 2024-10-26 04:44:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98a4d8b9-b896-3ac0-9273-98ec02e77d25 | -7.03691 | -49.28068 | 2024-10-26 04:44:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98f36ae8-a18a-3517-bb51-5c56e4a37c87 | -7.03348 | -49.28025 | 2024-10-26 04:44:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0d97408-a114-3249-93d9-b07613d4a139 | -6.75714 | -48.76799 | 2024-10-26 04:44:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1c9f6ea-a905-3879-ac31-9ebf62ede8fd | -9.05144 | -50.00461 | 2024-10-26 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9fc77d3c-0a8c-3541-9315-c12e70d89a4c | -8.81966 | -49.6904 | 2024-10-26 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 096e050f-fa0d-360a-be29-b314569a6a09 | -8.81625 | -49.68988 | 2024-10-26 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8ae2aada-b007-3ce8-83ff-b332b87abdc4 | -8.81339 | -49.68563 | 2024-10-26 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee959f71-9bfd-3eca-b7e5-4bdce46a723e | -8.80885 | -49.69258 | 2024-10-26 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a41a175-f1c6-3dc2-b715-bff8b96550e1 | -8.70699 | -48.99742 | 2024-10-26 04:44:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1685d978-cac9-346b-bd9e-122a38badc03 | -8.7029 | -49.00082 | 2024-10-26 04:44:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 835567f6-8599-39f7-bc69-77de6299a403 | -8.60727 | -49.03543 | 2024-10-26 04:44:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9018ecbb-f093-37dd-a654-38d5ad25ffe1 | -8.60668 | -49.03934 | 2024-10-26 04:44:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eecefa83-8a4c-3078-b726-683e7c2bf4f5 | -8.60377 | -49.0349 | 2024-10-26 04:44:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd53f2d2-0fcf-3f36-9dd4-e15d17dc64fd | -8.56358 | -49.20752 | 2024-10-26 04:44:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31d520a3-f179-3949-9a6c-dc066182e9b3 | -8.56069 | -49.20314 | 2024-10-26 04:44:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4c6fb38-425a-36cf-bbe0-7785280fd25a | -8.56012 | -49.20699 | 2024-10-26 04:44:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a369ac1d-9770-3c7d-8dbb-616aa832a56e | -8.54236 | -49.55753 | 2024-10-26 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9991c4f8-bf16-3fb5-89db-dc7798f336c4 | -8.39281 | -50.04976 | 2024-10-26 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c87b960f-1fc2-3a02-ba98-720d4e20a1a8 | -9.1689 | -50.06727 | 2024-10-26 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 063738f0-4480-3a6b-80f9-75e8569d6c9f | -8.81681 | -49.68615 | 2024-10-26 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 32659198-2574-3b93-89c1-b0a70bf2c5b7 | -8.81568 | -49.69361 | 2024-10-26 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dee94870-1111-37d2-af9c-e83925ffc95b | -8.81455 | -49.70107 | 2024-10-26 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0d6e435-99bd-31e3-92ce-cde6242993ae | -8.81283 | -49.68936 | 2024-10-26 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72abf837-eaf1-3de8-ba53-d51cfd9eb316 | -8.8117 | -49.69683 | 2024-10-26 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95643aff-3d27-387d-b741-b40ee6860324 | -8.80941 | -49.68885 | 2024-10-26 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a3dfa6c-39ac-319e-9359-ccb4130552cf | -8.67514 | -50.04126 | 2024-10-26 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ee2162b-df92-337b-9876-27ae4f79ac7c | -8.56474 | -49.19983 | 2024-10-26 04:44:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1db5e482-03f5-37bf-bffc-00c83d500754 | -8.54578 | -49.55805 | 2024-10-26 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e67fd9b6-807a-32de-aeaf-36c014b2a9f3 | -8.54179 | -49.56126 | 2024-10-26 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4fe06074-6ae7-36c7-8cfc-3e4189a61243 | -7.98497 | -49.69767 | 2024-10-26 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a8e56815-ebd8-3c88-b616-af0c80920c94 | -7.98362 | -50.00983 | 2024-10-26 04:44:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b9c3a99-f7a6-3088-9e4c-4ba86cb3a171 | -7.98214 | -49.69347 | 2024-10-26 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e2696804-10b2-30ab-991f-71cec3a6253a | -7.97535 | -49.69243 | 2024-10-26 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 533251b2-abb9-3e55-b2b9-6ac3d377cc04 | -7.97479 | -49.6961 | 2024-10-26 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e3ae4c2b-12e4-367c-8ff6-54774043beac | -7.97139 | -49.69559 | 2024-10-26 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ccb3c769-b496-3de7-9273-750687b272bf | -8.18675 | -49.50083 | 2024-10-26 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cd57093b-abce-306d-8ea1-2ba948d64490 | -8.18333 | -49.5003 | 2024-10-26 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e51d864-d5d2-3027-ade2-5f065f5cd246 | -8.06186 | -49.3792 | 2024-10-26 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b18a2c3a-505b-3964-b736-2f64a7c335cd | -7.98892 | -49.69454 | 2024-10-26 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a28e289d-c095-3fdf-a021-cdfcaa5111cb | -7.98553 | -49.69401 | 2024-10-26 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d6e4ef15-dc68-3b0e-882e-0a795be62274 | -7.98157 | -49.69714 | 2024-10-26 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 34333930-002b-3896-bfd6-840382f7d514 | -7.97591 | -49.68877 | 2024-10-26 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ae434717-ed67-3a2d-acca-1a93fcf11321 | -10.61408 | -49.48753 | 2024-10-26 04:44:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0065e982-56f7-39f4-8a65-32f1141be0fa | -10.19914 | -49.14431 | 2024-10-26 04:44:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec4576f0-07b5-32d8-95fb-2a56dd023b0d | -10.19854 | -49.14833 | 2024-10-26 04:44:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb846876-519f-3c27-9981-0f8e55112372 | -10.19501 | -49.1478 | 2024-10-26 04:44:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3337963-2678-3234-9ef5-ca6281e8e4fc | -9.9454 | -48.95718 | 2024-10-26 04:44:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a445925d-f356-3d03-b927-1fdd18eedb21 | -9.78701 | -49.31327 | 2024-10-26 04:44:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 894e7f4a-763c-35f9-b51a-1011d4ddafde | -9.57047 | -49.6554 | 2024-10-26 04:44:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96d1df35-a0aa-3219-b17d-0c1e1b93565c | -9.56526 | -49.61958 | 2024-10-26 04:44:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 27ac35e5-fbbc-3bfd-9e8a-c38b249d7e84 | -9.51708 | -49.1892 | 2024-10-26 04:44:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e79ae70-d091-3363-961c-dc78396b3605 | -10.61758 | -49.48806 | 2024-10-26 04:44:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75742b45-1593-33a4-813a-fe3c0dcd8809 | -4.97475 | -49.77667 | 2024-10-26 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 09c22351-1078-3b2e-b64b-6f54549189b3 | -4.91205 | -49.83115 | 2024-10-26 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 036ca3bd-deb1-3cd3-9de0-37b8a01b97d5 | -4.84047 | -49.87737 | 2024-10-26 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5014aa0-4000-3724-b652-655389fd6d75 | -4.83992 | -49.88086 | 2024-10-26 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9023fd1-d508-3abe-88f5-7cd06619a51b | -4.73323 | -50.69227 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 772b7111-6c2e-398a-9a94-75ee3234a86f | -4.72745 | -50.79357 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce4f685e-d1de-31ba-8089-a03d3c9f09b9 | -4.72414 | -50.79306 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efe295af-fbf9-3162-b639-cb3ae7aa9359 | -4.64165 | -49.36428 | 2024-10-26 04:44:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd177962-187e-3bea-8c39-dd2e351beccb | -4.63294 | -50.76817 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 622fae50-243f-36c4-96bb-ab5e641e8b6c | -4.55338 | -50.43116 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f4474ee3-df4e-3e1d-afe4-1cacc4f42046 | -4.43718 | -50.13079 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6fea45fc-0c18-3545-bfab-857e4c030656 | -4.40417 | -50.73252 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f31c5d04-2c9e-3659-90e9-bac41fc59d62 | -4.40033 | -50.73544 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65a930f2-18c8-31e8-8a0e-086405c8557c | -4.39764 | -50.53381 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30e31b9d-2db2-340e-88e6-cce43bc640f5 | -4.39596 | -50.52298 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 791852a6-fc11-33a1-b593-55ca96dab768 | -4.39542 | -50.52642 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dd78a0a5-520f-32c4-928c-407b28fd48ee | -4.37639 | -50.84444 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4fb3e5bd-f1ab-3f3e-98b3-a1c2fe122785 | -4.29478 | -50.73613 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9a36d9d-c74e-3be3-bf95-6929a77691a0 | -4.29424 | -50.73957 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb037f5a-e8ef-377c-b8c9-0037561fad73 | -4.21668 | -50.47735 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 582d2ccd-1384-3e63-a2ba-f237b1275362 | -4.00573 | -49.41493 | 2024-10-26 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c984ade6-7b9a-33c5-a8d3-b75ec3cb434b | -3.96083 | -49.89724 | 2024-10-26 04:44:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1101980a-4f84-35c5-9c28-8a2d251468d5 | -3.93791 | -49.39348 | 2024-10-26 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df2acf27-d4c0-306e-a5b0-4545da81ebf9 | -3.93457 | -49.39296 | 2024-10-26 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8fa67159-cca3-3fcf-ad76-1d05dc5ef489 | -3.92081 | -50.17371 | 2024-10-26 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20dc2a86-3239-39ee-af6f-3eccfa5c9de5 | -3.91509 | -49.38634 | 2024-10-26 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7102dd0f-6540-3303-b564-1f92ee6f760a | -3.88298 | -50.04787 | 2024-10-26 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc234900-4e02-39bc-81d3-1dba053ac951 | -3.81973 | -50.23555 | 2024-10-26 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2564c5ea-ef39-3d96-b36a-db181489a532 | -3.81919 | -50.23899 | 2024-10-26 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 901689e3-6013-3752-8311-ab4c65237c65 | -3.78665 | -49.838 | 2024-10-26 04:44:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5580a7b3-2cb2-39ea-a56e-0d82ffeaf3fb | -3.77448 | -49.82901 | 2024-10-26 04:44:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 03782d93-ec2a-3c4e-9b2d-3ec8ccaf7459 | -3.74617 | -50.66056 | 2024-10-26 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78bfd829-7575-3c43-950a-8f092ec73c2c | -4.65147 | -49.54335 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README81.md)
