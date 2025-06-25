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
| 4467091f-10d8-3ccc-a02c-568fc1186daf | -10.28095 | -48.2046 | 2025-06-25 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3018dc4-1615-3e18-9013-f48c8a888cdb | -14.19313 | -42.772 | 2025-06-25 04:08:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| c608c094-eae0-36d4-beb3-3abc21e3f05f | -12.79587 | -48.73251 | 2025-06-25 04:08:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26259243-c085-32e3-a876-5c9dd1f0dc57 | -10.65171 | -44.49439 | 2025-06-25 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4eeef707-ed4f-3649-954e-65a630cef386 | -10.51821 | -47.57783 | 2025-06-25 04:08:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9b7dc6f-9654-3145-a59e-df90a1bcd144 | -8.92469 | -47.44038 | 2025-06-25 04:08:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b833605-7463-33d2-a858-42bbfabd004b | -10.82804 | -54.04633 | 2025-06-25 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7fa7df7-be7b-346e-be3c-8d30570a6510 | -11.50748 | -48.95587 | 2025-06-25 04:08:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f5707c7-1af9-3034-a768-8a0ae31bdab7 | -12.51119 | -47.43206 | 2025-06-25 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 793996bb-971d-33b9-a3dc-701c872838b6 | -9.50812 | -45.44103 | 2025-06-25 04:08:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b221da4-4718-3df3-9ac4-ea4fe6eee38a | -9.92555 | -52.4364 | 2025-06-25 04:08:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48295359-b60f-39bc-b794-4ce028eba3ae | -9.92138 | -52.42772 | 2025-06-25 04:08:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 65a23c15-0188-37ee-9793-4e85c28b65bd | -9.91996 | -52.43527 | 2025-06-25 04:08:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c1559ef-d3a3-3532-92e3-f3d5c3d3458c | -12.80353 | -48.73793 | 2025-06-25 04:08:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b4f2e26c-d4bf-37e0-ab04-8d8efd676f67 | -11.13766 | -53.92241 | 2025-06-25 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3dae917-4411-38f6-9d5a-46031fb75998 | -15.92335 | -42.57204 | 2025-06-25 04:08:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e6fedbfc-1832-3168-af6c-ae49eb045783 | -11.5797 | -44.63506 | 2025-06-25 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd7b89fe-0b27-3018-a634-008ac21113d9 | -14.71432 | -48.40961 | 2025-06-25 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 62ca3acf-dec1-356b-91ca-e98ea9d0a989 | -8.6739 | -51.466 | 2025-06-25 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c021fc7-64cb-3d26-a80b-c03cd54661f3 | -10.81544 | -54.04492 | 2025-06-25 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed7618c4-8aee-3c86-ab32-0715d659d75f | -11.58187 | -44.64315 | 2025-06-25 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e1be819-b4cb-30a9-ba46-3d636a52363c | -13.04076 | -48.82503 | 2025-06-25 04:08:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 89b52241-a563-31f0-8919-5c053cdc9e95 | -10.83271 | -54.05381 | 2025-06-25 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f0bf868-8a41-3fb7-a9e8-3f4b78320e23 | -17.11016 | -41.57236 | 2025-06-25 04:08:00 | NOAA-20 | PADRE PARAÍSO | MINAS GERAIS | Brasil | 3146305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 654765b9-202d-3f18-8e8b-f74bec7162d0 | -10.44975 | -47.95417 | 2025-06-25 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 19a1d8d0-14f9-3d7b-bb8b-a3d8d1361122 | -8.66854 | -51.46492 | 2025-06-25 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 050fcc2d-5cf6-3e8a-bfda-cbf4a958feac | -10.45221 | -47.95451 | 2025-06-25 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 34.4 |
| f8186f59-4411-3d54-990f-1d359a8e36bd | -11.95605 | -47.01617 | 2025-06-25 04:08:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb9a8867-9591-3690-bcbd-b3f38c658826 | -13.07343 | -48.83536 | 2025-06-25 04:08:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b57e034-8edf-3794-9144-74d0c107b143 | -14.71646 | -48.41228 | 2025-06-25 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0eb4b885-fe11-314a-b9ae-cb5c4f5ed40a | -11.5912 | -47.60875 | 2025-06-25 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a1400f9-ff84-38d7-8700-740d7fcdc702 | -10.17591 | -43.82211 | 2025-06-25 04:08:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a611b19-60a6-3630-8778-5cb832184505 | -10.948 | -47.39064 | 2025-06-25 04:08:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 650f4cd4-15ea-3680-b3c3-8b86c5390028 | -11.08356 | -46.64414 | 2025-06-25 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f2ccee5-045a-3a2f-95db-42e8a63cf964 | -15.03922 | -44.29602 | 2025-06-25 04:08:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c9b25e0d-c4b3-32ed-97b9-9bd330d1dd5a | -11.94976 | -47.02976 | 2025-06-25 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2a3943db-414c-332f-a815-04747d8ec849 | -10.45289 | -47.95071 | 2025-06-25 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 2c44bf00-b816-3484-9910-5b7a0c29c086 | -10.44084 | -47.9566 | 2025-06-25 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 8647cb6e-7eb0-30ca-8694-9051aa8877a6 | -11.59343 | -47.61147 | 2025-06-25 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86999c35-70f4-35e0-bf84-e8ea68892ae5 | -9.92626 | -52.43259 | 2025-06-25 04:08:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0127dd6-d17a-3a76-8000-a1f160f593de | -11.93262 | -47.84005 | 2025-06-25 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4501822-4920-3565-bf17-169dae686435 | -10.5984 | -49.46229 | 2025-06-25 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f125ee8d-c7dd-3575-b632-c028eb870958 | -10.28027 | -48.20853 | 2025-06-25 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0461fc5-78e8-33f1-aaec-1b1286e5e546 | -8.86961 | -47.27707 | 2025-06-25 04:08:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8bca4182-3f13-320a-a94d-854499478ba0 | -9.57171 | -49.10851 | 2025-06-25 04:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 47f17b26-ef46-3c1b-b340-b356183d3236 | -12.03255 | -47.77449 | 2025-06-25 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9e40f9d-899e-37eb-9928-1f5cc789bdac | -15.39988 | -43.19835 | 2025-06-25 04:08:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fb76ca47-5263-376e-856a-9244a08e62b6 | -10.82987 | -54.00328 | 2025-06-25 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d41dc742-2b93-37da-9895-839c0517dae8 | -10.8411 | -42.23277 | 2025-06-25 04:08:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e0538468-15e3-30a8-a9de-70d3c892a6d2 | -13.60975 | -43.97121 | 2025-06-25 04:08:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3a821643-f84a-3929-b38a-5ccbb922feee | -14.40112 | -47.88038 | 2025-06-25 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe37474a-769d-31e0-ae00-c81851c3d0b4 | -10.45388 | -47.95488 | 2025-06-25 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 619884c2-5ab7-384c-aca9-593434c0518a | -13.01435 | -44.10018 | 2025-06-25 04:08:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 484e3c41-5998-3dbb-9fc9-e9d53e96ce76 | -8.71641 | -47.8592 | 2025-06-25 04:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb63f9a5-b66b-31bb-87fd-30ba619c91c7 | -10.44628 | -47.94963 | 2025-06-25 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b4c678d3-5459-3a65-a9ae-3c2dad4a60c6 | -11.57316 | -47.43133 | 2025-06-25 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e1e5c8d3-3bdc-3833-bfe1-74528a7cd002 | -11.92862 | -47.83934 | 2025-06-25 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 807da7af-55b4-39d0-aa61-d4ac327ce6f7 | -10.83315 | -54.05243 | 2025-06-25 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 334e5a47-6597-308a-aa2f-b0b48516d505 | -9.56719 | -49.10768 | 2025-06-25 04:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| aa345496-04ee-3c22-b0b6-7d70a9e66f42 | -14.39809 | -47.87511 | 2025-06-25 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 893c1d21-cb49-393a-b2ae-a33a053f4e16 | -14.38188 | -50.33372 | 2025-06-25 04:08:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb765a1d-c50b-3f47-a228-013f9ef7471b | -13.61307 | -43.97177 | 2025-06-25 04:08:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b7e126ad-ac71-3c3a-a95c-a1f9eba9716f | -11.11017 | -44.52368 | 2025-06-25 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9d087f6a-860f-3bca-a6e9-23ce734edcea | -14.25413 | -50.41307 | 2025-06-25 04:08:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44efdb68-f7bc-3f61-9ed3-6007565d7e69 | -13.04912 | -48.82654 | 2025-06-25 04:08:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b87451c-7b90-3aa6-a2a0-7de31c03a73c | -14.38364 | -50.3321 | 2025-06-25 04:08:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 690ed879-a3ae-3dce-b179-f17a0ab398f4 | -8.67326 | -51.46947 | 2025-06-25 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| caeff159-e96d-3b7e-a6a9-0ebe050588c5 | -16.08791 | -41.98372 | 2025-06-25 04:08:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 743a5aa8-1096-392c-9c96-2f5c6bc6e798 | -11.57013 | -47.42559 | 2025-06-25 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fbbb5619-a616-394e-9967-a57c9d1e3727 | -15.39325 | -43.19725 | 2025-06-25 04:08:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2808bc84-cd05-3b5b-a5d7-657f5712f6f7 | -10.82847 | -54.04302 | 2025-06-25 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94f1fe9e-87ad-31b1-99f4-3f769302f5b2 | -12.12956 | -44.96335 | 2025-06-25 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0668f168-9ee0-350d-b116-629375d6948f | -8.58065 | -48.21124 | 2025-06-25 04:08:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 311f009a-5a00-3681-9de3-a14b5d3c85ee | -16.42998 | -44.5241 | 2025-06-25 04:08:00 | NOAA-20 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91e224fd-fc0d-3fe8-b426-9b24c9c12de4 | -8.98505 | -49.86513 | 2025-06-25 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d0b0f66-0eec-3729-b2c8-2236a5f6f4f3 | -9.50148 | -56.09653 | 2025-06-25 04:08:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 135c7b7e-5a65-3ad3-8f58-28178ba08ad6 | -9.37703 | -47.9832 | 2025-06-25 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da12269f-bc07-3380-ad2f-cc8f55946282 | -10.84772 | -42.23383 | 2025-06-25 04:08:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ded241d3-7b9a-3a07-b62e-82f39e493d24 | -10.44149 | -47.95278 | 2025-06-25 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| df01425e-bfa2-3472-81a8-b0640b9d4ab9 | -9.26183 | -47.64418 | 2025-06-25 04:08:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c481a8c-7e5f-3ed3-ab36-732ea5bd895a | -10.25021 | -47.67959 | 2025-06-25 04:08:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 849debfe-7787-3385-a2f6-94a0885712bf | -10.65232 | -44.49064 | 2025-06-25 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5825e966-0635-3ce2-8359-1503de2636e8 | -8.92878 | -47.44108 | 2025-06-25 04:08:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 476b0e31-eaac-32dc-a63b-664c5b354183 | -10.95193 | -47.39141 | 2025-06-25 04:08:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4259e57f-4750-3b00-9bce-ad98933b9f3e | -13.03932 | -48.83292 | 2025-06-25 04:08:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7543aedd-0461-3488-a567-46157a479852 | -8.47828 | -50.27837 | 2025-06-25 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 3fe0269d-3ab3-31e9-bc04-493cedd4fb37 | -16.42782 | -44.51631 | 2025-06-25 04:08:00 | NOAA-20 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c32a856f-777d-3c88-97c0-d58f55623e69 | -11.58311 | -44.63564 | 2025-06-25 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 25fb87e4-c579-3895-9a7c-6b4b759eb2d8 | -14.71829 | -48.41026 | 2025-06-25 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1fc7c014-d506-304f-ac59-a6af33136324 | -14.13103 | -47.94421 | 2025-06-25 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 377a7689-b721-34e4-9556-505f92e92749 | -13.64486 | -43.79427 | 2025-06-25 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2aad462f-8f91-35e5-80d4-103506ed92a7 | -15.3927 | -43.20083 | 2025-06-25 04:08:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 54b156a7-8a59-3d92-9f8f-3ec26de7da37 | -10.51018 | -47.57636 | 2025-06-25 04:08:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6c7dddd-9b12-3633-83da-eb53ea040388 | -11.11419 | -44.52051 | 2025-06-25 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65008705-e9c6-3476-873a-3a1b9b097c99 | -11.11358 | -44.52426 | 2025-06-25 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8472ef95-6005-3194-af4f-3421f8b43c60 | -10.82872 | -54.0116 | 2025-06-25 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 886a0ce6-6c5f-3295-936a-7f0aabfdea7b | -8.6679 | -51.46841 | 2025-06-25 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e46221b8-667b-30cc-8dd0-da8c7e796677 | -14.37868 | -47.87242 | 2025-06-25 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e1f45906-c8a7-3c9b-b8be-2c2bbfab6043 | -10.82969 | -54.00678 | 2025-06-25 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b29d5ae-a354-3512-a554-31f607e7c2bf | -16.0137 | -43.02612 | 2025-06-25 04:08:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README11.md)
