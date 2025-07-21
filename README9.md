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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb3ddb93-9bc6-3beb-a56b-be074ba08281 | -10.14549 | -49.65682 | 2025-07-21 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36e43e51-bed2-30fd-b184-f39c6fd7fbcb | -7.41689 | -44.96811 | 2025-07-21 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb79c6c9-51ef-329b-b19e-d5a270eafa25 | -7.95862 | -43.97488 | 2025-07-21 04:19:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f42fe8d8-ef2a-3922-9a04-cd2a04b600bf | -8.51954 | -41.1926 | 2025-07-21 04:19:00 | NOAA-20 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ed7d0f05-c51c-3468-ad32-3143a112a5dd | -11.95557 | -47.02604 | 2025-07-21 04:19:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3d96067-041a-3ff8-aa3d-58fc0ef35b9c | -10.73127 | -52.52309 | 2025-07-21 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b6d2ea3-169d-3caf-a2d6-b747ceafc8f0 | -6.94987 | -44.39354 | 2025-07-21 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f9c7e2f-daa5-33d9-ab42-0c31568477e5 | -5.27949 | -44.94745 | 2025-07-21 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3ba7a85f-1846-38ca-a98c-b2f1b99dc71e | -7.2771 | -60.1889 | 2025-07-21 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 77c75feb-063c-3779-b71e-b19fbf097e67 | -7.2772 | -60.1698 | 2025-07-21 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 5936ba71-044e-3133-b6b0-8e72907a3a49 | -7.2957 | -60.169 | 2025-07-21 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| a3a04d09-0abd-3f68-a75e-aa251dbd9a4c | -7.2402 | -60.1904 | 2025-07-21 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 0fdc2978-c48b-3775-a640-7a94cccaf430 | -16.64385 | -43.89204 | 2025-07-21 04:21:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f83a4bbd-2b60-3bee-a967-bb13410a4ea2 | -15.02617 | -49.25341 | 2025-07-21 04:21:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| afb045a9-e46d-3e32-b759-1e1f206d0da6 | -16.70819 | -49.35509 | 2025-07-21 04:21:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8c58a5c1-1062-3912-8b0e-1cec5681dee7 | -17.64266 | -44.73577 | 2025-07-21 04:21:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b476063-147b-3a13-b640-26ac0adbc21d | -16.07663 | -43.62891 | 2025-07-21 04:21:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b57bd532-3a0a-3437-9a67-d207a0200502 | -15.77491 | -47.79342 | 2025-07-21 04:21:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ddd235a1-4cb2-3a5f-94c1-2009821bd42c | -14.74609 | -48.29106 | 2025-07-21 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2765505d-5981-30e0-ac47-054f40adb5a0 | -15.93118 | -47.75319 | 2025-07-21 04:21:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 133cdcc3-ba23-3edb-a9f7-1f3929495053 | -17.64207 | -44.73989 | 2025-07-21 04:21:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c42d9da2-4328-3d29-959c-6aff16998de3 | -17.64911 | -44.74095 | 2025-07-21 04:21:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 085072d4-980f-359f-9dac-3ab2d17b8446 | -14.77519 | -47.98517 | 2025-07-21 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 019aa627-a223-3997-a9b5-69436dcd0f2f | -13.4893 | -45.50387 | 2025-07-21 04:21:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d6736019-7c0d-32c3-bc06-96e8d5095610 | -13.09291 | -50.57096 | 2025-07-21 04:21:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 68e0a7bf-585d-385d-825f-6dfd3c425f2a | -15.61013 | -45.90022 | 2025-07-21 04:21:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b19d8767-075c-3206-a5e6-65a3497c4213 | -20.02647 | -43.82109 | 2025-07-21 04:21:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 01bf7d36-5d9c-3b55-bf8e-8f09c7020688 | -15.61403 | -45.89714 | 2025-07-21 04:21:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2229cc3d-d80f-369e-a4d4-ca77e25a72f7 | -13.08827 | -50.57502 | 2025-07-21 04:21:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7eef515b-32dd-388b-8102-1780f24659ea | -15.11366 | -43.85935 | 2025-07-21 04:21:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 731c5a7e-a109-3ebe-81ff-506434aae4c4 | -14.76909 | -47.98036 | 2025-07-21 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7d7ee12-96ff-37fa-bcd2-21272d1e780d | -16.64083 | -43.88721 | 2025-07-21 04:21:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 370ad7c1-2dc5-33b6-be82-4230f650cf92 | -17.33761 | -44.89486 | 2025-07-21 04:21:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 91609d47-2a9d-3110-a827-f0050d8392e6 | -16.07965 | -43.63387 | 2025-07-21 04:21:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de189b45-6a40-3bea-8b51-28125e195497 | -14.75404 | -46.67299 | 2025-07-21 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0b17fac8-5cd1-3e5c-9956-806f5b507441 | -12.90066 | -48.9264 | 2025-07-21 04:21:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 05c11cb2-3de7-3411-843d-13dd377aa42b | -15.0255 | -49.25739 | 2025-07-21 04:21:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f78d2108-f524-3743-8b54-9165b8f8f4d3 | -13.09207 | -50.57572 | 2025-07-21 04:21:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d561ff1-63a4-344d-b05a-76febdde339d | -20.05682 | -47.58998 | 2025-07-21 04:21:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d65f2c86-438a-324c-8c32-9c076bee048a | -16.79189 | -49.35707 | 2025-07-21 04:21:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54347ad6-ff68-3af6-b183-5885f39ee433 | -18.05668 | -44.84255 | 2025-07-21 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 759b6a9d-496b-37db-845e-fe50e5966458 | -13.87121 | -46.36815 | 2025-07-21 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f4ccf5b-7b73-399b-939f-41fbde54e010 | -13.09587 | -50.57641 | 2025-07-21 04:21:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5023b570-f868-3ce5-b0cd-0a0811760dc6 | -17.91357 | -47.76488 | 2025-07-21 04:21:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b98989fa-53ce-3a44-af12-e1213f578a31 | -16.64023 | -43.89149 | 2025-07-21 04:21:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c2a139f8-4f87-3645-8e13-03186a86d840 | -19.97594 | -44.8559 | 2025-07-21 04:21:00 | NOAA-20 | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d8b16f5-8b4a-3714-a57b-86bde533eec0 | -13.0112 | -46.93009 | 2025-07-21 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce295749-0617-3637-b76e-63bb44b72c78 | -14.7746 | -47.98881 | 2025-07-21 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 05d68426-f0d7-3bbd-bf51-7ba1d3cfed84 | -17.33412 | -44.89431 | 2025-07-21 04:21:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 76cbb03b-7987-34c7-94b1-b38de04fade7 | -12.98639 | -46.91503 | 2025-07-21 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1bb51fd-de35-301f-9ee8-947b2645ec67 | -14.76574 | -47.97979 | 2025-07-21 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2850a867-ec4a-3e4b-a277-46dd2ff8fccd | -12.62808 | -48.90942 | 2025-07-21 04:21:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 318979be-8547-3bbe-9e0c-a99136575757 | -15.80311 | -43.32119 | 2025-07-21 04:21:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8e963a28-e417-3660-9d5d-a4290c0ce3e0 | -12.64407 | -47.12163 | 2025-07-21 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 194b61af-fce2-319b-9495-776404881323 | -19.75517 | -44.00983 | 2025-07-21 04:21:00 | NOAA-20 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 845f50d9-75c0-37ec-8236-1ddf7f805d4b | -17.91693 | -45.56486 | 2025-07-21 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ac624dca-50fd-37b1-bc37-90c8fee6e2fd | -14.08545 | -49.4981 | 2025-07-21 04:21:00 | NOAA-20 | ALTO HORIZONTE | GOIÁS | Brasil | 5200555 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0744e1ef-76ca-3824-a7fa-125363a4fc30 | -14.74056 | -48.28244 | 2025-07-21 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04a91eed-442c-3b0e-842b-ed9c3db14598 | -14.77735 | -47.99305 | 2025-07-21 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 345b51ec-c33f-3f41-8b11-3f5ad5d7073d | -12.64292 | -47.12878 | 2025-07-21 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9039c1b4-302e-3214-b1fb-cb2710d54f40 | -15.95334 | -48.31062 | 2025-07-21 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7b86997-34d9-3844-9f79-9719e8f98279 | -14.74116 | -48.27876 | 2025-07-21 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f4cc734-05c6-3556-984a-0ad322c173c0 | -14.76515 | -47.98343 | 2025-07-21 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f214a605-b4b9-3d24-a7e8-a834c2acc57a | -11.31533 | -55.21997 | 2025-07-21 04:21:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 030d61f5-39f6-38f3-98b6-5cb9175a0f1a | -11.80673 | -56.96548 | 2025-07-21 04:21:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ec06e169-4cb2-30d1-8e57-ec20dadff5ea | -19.18014 | -45.45831 | 2025-07-21 04:21:00 | NOAA-20 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12c2cbd5-814e-38f8-92bb-43de4835efa2 | -14.76456 | -47.98707 | 2025-07-21 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5413b83c-1972-31ed-a397-1f6ba8a3f3d6 | -13.45745 | -48.0175 | 2025-07-21 04:21:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c36ba686-50de-3999-8631-96ec28574a29 | -13.63478 | -45.53105 | 2025-07-21 04:21:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| af786f71-96b7-3329-b624-268af285d5ed | -15.95274 | -48.3143 | 2025-07-21 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 303fec37-0773-37f7-a7ea-6290c10d6ff0 | -15.61737 | -45.89769 | 2025-07-21 04:21:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 334834f9-f609-3305-8741-826d8a835052 | -12.98695 | -46.9115 | 2025-07-21 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a35ee89-8abf-3c1c-a4dd-f4c35c4088c0 | -14.774 | -47.99247 | 2025-07-21 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ae6143a-0c60-3146-b0a3-6a05666a1c1c | -14.20746 | -43.95723 | 2025-07-21 04:21:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f9ac250-9ccf-3531-8d7b-c44fc9acdddf | -17.24671 | -46.90897 | 2025-07-21 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ae1e3c4-2438-3d30-a7c5-2ee58eec5c42 | -12.64235 | -47.13235 | 2025-07-21 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f6fcff5-ad7f-32fe-9e8c-fe6e3f878428 | -17.25952 | -48.0513 | 2025-07-21 04:21:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 82511dd5-0a90-3052-9fc0-fc277e2f2fa5 | -13.89727 | -48.7353 | 2025-07-21 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d44e17d3-08d2-3ebb-a5f5-1b338284c9f1 | -13.00789 | -46.92949 | 2025-07-21 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d80e3a1-b60b-3586-bc3c-0fdec8792c81 | -11.31596 | -55.21663 | 2025-07-21 04:21:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31cd270b-1770-351a-a509-38aa45204435 | -14.76791 | -47.98763 | 2025-07-21 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24ba0be6-7328-332e-93b9-5b8a9e2db036 | -11.31659 | -55.21331 | 2025-07-21 04:21:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ae3f2e6-1d11-368b-8b40-e58b96a55b41 | -20.26016 | -46.31723 | 2025-07-21 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8f5ec9dc-d93e-3c36-ba1f-7ee5f3ad7403 | -16.64445 | -43.88775 | 2025-07-21 04:21:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b901a72c-ac02-34b2-b0fb-ca832411121a | -15.61069 | -45.8966 | 2025-07-21 04:21:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a2295d62-e310-3bdd-bfb1-4786ad14ff20 | -19.18073 | -45.4543 | 2025-07-21 04:21:00 | NOAA-20 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c76822f-08b9-34b2-a92f-b3af76d72719 | -17.75919 | -50.59486 | 2025-07-21 04:21:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc2b884c-d4c7-3bf2-ab05-2c25dacddca9 | -12.64177 | -47.13593 | 2025-07-21 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1647e878-bfc5-3d7b-9920-fb4da2d377f0 | -12.68017 | -46.83199 | 2025-07-21 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d9ef2fa-3295-3555-af61-472bbc06a1a6 | -15.34436 | -48.6243 | 2025-07-21 04:21:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 73386bcb-9ef3-3ab6-95f2-6f7181f6f126 | -15.61347 | -45.90077 | 2025-07-21 04:21:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4a39d7ca-af33-3bcf-aecb-aad66825c086 | -17.6497 | -44.73684 | 2025-07-21 04:21:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06ebc706-f114-320b-a988-cd378acfded6 | -20.26962 | -54.806 | 2025-07-21 04:23:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2dd21e6b-008c-3ffd-bdbf-de205d693f3d | -23.58135 | -47.22066 | 2025-07-21 04:23:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6347fbab-01df-3609-ba37-0ed1b00cb1b1 | -23.22292 | -45.99513 | 2025-07-21 04:23:00 | NOAA-20 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5c732336-c30d-321a-ac53-a7c1b35daf1d | -23.33792 | -51.90248 | 2025-07-21 04:23:00 | NOAA-20 | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| af94a2f7-c8b3-39d2-b7df-c6994f9a1af6 | -20.27052 | -54.80147 | 2025-07-21 04:23:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 56b67da8-f6e8-32c8-9009-a3c77cb8d678 | -23.27011 | -46.40202 | 2025-07-21 04:23:00 | NOAA-20 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 22272030-2fa4-3b96-9623-42598295f5c6 | -20.19229 | -50.49936 | 2025-07-21 04:23:00 | NOAA-20 | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fff2ece4-d11f-3f25-a2e8-11d9e61c12dd | -23.39289 | -46.14619 | 2025-07-21 04:23:00 | NOAA-20 | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |


[Clique aqui para ver as próximas entradas](README10.md)
