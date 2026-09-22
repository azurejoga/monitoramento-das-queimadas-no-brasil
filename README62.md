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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4605d095-e787-34ef-8461-505fd98c171a | -7.82928 | -45.25944 | 2026-09-22 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 09cea9f7-17cb-3393-8150-2bf3943336f4 | -10.45491 | -51.33854 | 2026-09-22 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44ec9ee5-c16f-3f3b-9019-ec13ffaf87d3 | -5.87415 | -53.64191 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 462358a5-a847-3417-be26-89bc06dbc2c4 | -3.61043 | -60.5676 | 2026-09-22 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b29ccc9b-10c0-3f42-a8fd-f2bde1def9c8 | -3.89846 | -49.06138 | 2026-09-22 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b5492a2-c892-385b-9870-6d16aa347c35 | -5.87628 | -52.06022 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6dd054cc-2631-3157-943f-a19e9c0f5047 | -7.44892 | -44.74559 | 2026-09-22 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d8b2c78b-6460-3f4d-9f90-774f10eaa457 | -6.2412 | -51.0143 | 2026-09-22 04:46:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69d5917d-3ef1-316d-a879-3affde4fd047 | -7.52686 | -46.21827 | 2026-09-22 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab0825e1-ef2d-3d56-ae83-865a0f4f8ac4 | -6.67774 | -50.94148 | 2026-09-22 04:46:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48f4fe53-3ef1-3ccd-83ce-af0f62ff9cc4 | -7.23469 | -55.58619 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73c66f37-d721-3788-967f-38977a75d7d8 | -6.74081 | -45.45876 | 2026-09-22 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ad42c51-25f9-35fb-ac5e-0b83b0986c5a | -6.03796 | -53.27411 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| eb56ba4a-f76f-3295-8370-067ecbbff313 | -7.32954 | -55.59903 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 067960ec-edf0-3702-a131-fb0cc1d8fe52 | -7.78161 | -44.80963 | 2026-09-22 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e6a1adc0-9823-3290-89b5-6ec888de8e0a | -8.31537 | -44.75468 | 2026-09-22 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9ed5379e-b8ca-3f68-8874-ec5890aa0ae6 | -10.47248 | -46.28732 | 2026-09-22 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52258e0d-2fcf-396e-b0b5-530de718c6e4 | -10.68677 | -48.72647 | 2026-09-22 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af304ea9-fb9b-3324-a4e8-f61e5b5f7217 | -3.55439 | -50.28864 | 2026-09-22 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 244c6348-5caf-30fb-98e0-f60ee3a53f0c | -5.73003 | -53.46031 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e125746d-627b-367f-9a58-ec17e6a9cfe3 | -9.97059 | -45.30966 | 2026-09-22 04:46:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1cf45467-4467-33c8-91c4-17de9fae3d67 | -3.92018 | -56.04877 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e259a2e6-3666-3b51-ae16-7cf0d84ad8ec | -8.76331 | -49.96572 | 2026-09-22 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 588866b8-cf63-322c-b882-ee0e5876ef2c | -6.78031 | -48.66366 | 2026-09-22 04:46:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7bb4b097-cbb8-3240-9a0f-def9b94e2958 | -6.6969 | -59.96048 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 239ff4c0-34e1-30aa-946c-339a8db1ee03 | -5.87795 | -52.04963 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf2388bf-3373-309c-8c4f-207ae78162d5 | -5.26077 | -55.92455 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 89accb4a-2db9-3c21-9abb-221de036b5e4 | -6.66345 | -50.94634 | 2026-09-22 04:46:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90024651-3c98-38dc-a71c-9251a7c35850 | -7.6094 | -55.34427 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ffc6d27-fdfd-35d3-ab2e-7f97c5983b8f | -8.46958 | -50.76471 | 2026-09-22 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 34b3504f-466b-3685-97e1-791e292e48b0 | -9.20957 | -60.28887 | 2026-09-22 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38ff3aa4-1a81-348d-a40e-938748587211 | -9.61614 | -43.9392 | 2026-09-22 04:46:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7ce7b998-ea32-3d63-8332-e9c629fa42a2 | -5.80695 | -49.08847 | 2026-09-22 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01f6f128-4c25-3e21-ae8f-e3d2fdc3f036 | -4.48635 | -55.4922 | 2026-09-22 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a5d1f08-3118-305c-ad67-0838cf714730 | -3.40351 | -59.58512 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 61603594-d6b5-32d2-939e-810d1badd075 | -8.34993 | -50.7464 | 2026-09-22 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c784638-00a6-31fc-90ef-f99397f4b162 | -5.83476 | -53.50846 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5caee21a-debb-3b9d-98a3-507cda7d967b | -6.69993 | -59.95687 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 428089c9-7307-31f1-8897-3dc947fe707e | -6.64527 | -59.92262 | 2026-09-22 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 4853e6f8-d125-3abf-bb97-b64171c11e53 | -6.36204 | -58.28791 | 2026-09-22 04:46:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 68e399df-6afa-376f-a3df-911e1d216f9d | -3.92347 | -60.55742 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ee561c1a-db07-3d90-b824-901476272a73 | -10.45599 | -51.3315 | 2026-09-22 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2432c8f0-60c7-3b3d-9da7-470ef502ff34 | -10.69588 | -48.71494 | 2026-09-22 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4e181556-64ea-3e46-8afa-c39dfb4e1f44 | -9.84918 | -48.31787 | 2026-09-22 04:46:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 512d058f-addb-364d-a26b-6e1aae3791d1 | -4.97024 | -55.83279 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9648faf6-ad25-390e-849f-f8f5a1c4efd8 | -6.38411 | -55.27852 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f8a4f216-bbcc-36b1-9733-7cd725e687e4 | -7.55494 | -42.66063 | 2026-09-22 04:46:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 293cb05e-8bc6-3a36-a82f-2c8b886f7ed6 | -5.82633 | -52.07399 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0431f354-e5d0-38b8-ba69-7f1c4749c054 | -3.16477 | -50.82196 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3eb4604-94c3-33df-99e6-be46270e5231 | -6.89916 | -46.0131 | 2026-09-22 04:46:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dab2d729-d52e-380d-a56f-f65a6798b594 | -8.10706 | -44.43058 | 2026-09-22 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c4db3ad-aaaf-35b7-b575-b5571a6b77dd | -6.91846 | -59.62662 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 28b9af38-ec40-3a50-bc06-a4496b554a5d | -3.30118 | -57.86255 | 2026-09-22 04:46:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ef421000-1a87-3886-ac1c-2d24145abe44 | -5.25591 | -48.90772 | 2026-09-22 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5bd3e5b7-d94c-3f6b-ba9d-1351e7ab7b4e | -2.89767 | -60.05433 | 2026-09-22 04:46:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26b2ee21-751e-3ed5-a4cc-463cbcdd1c49 | -10.93853 | -47.8679 | 2026-09-22 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2180dc83-7217-3740-9da3-953739d45144 | -7.90097 | -49.0129 | 2026-09-22 04:46:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 621c51a1-6230-3118-a209-472a4af4f0fa | -8.79679 | -44.2848 | 2026-09-22 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f97c25c3-48d7-33c4-8de1-86ee8ba69a0f | -3.05267 | -54.40691 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 750bdc5e-eba1-3bd0-8ba4-a51e26daf2f8 | -3.38315 | -50.40652 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f90d12a9-33ea-3f09-943c-89f82b7a5fd1 | -10.47469 | -51.29839 | 2026-09-22 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 560c2a12-14c6-3ddf-a7fb-4631277d2bc8 | -8.83095 | -50.4895 | 2026-09-22 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d7385dd8-90b0-343a-a39c-f4410ec9a7d0 | -7.45275 | -44.75095 | 2026-09-22 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f8fb800e-11cf-30a1-b279-409593e22c25 | -8.60022 | -54.62391 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 807a5231-3e77-3746-93c7-320a817ff6ae | -4.34621 | -55.66199 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d07b771a-798c-36f3-8666-2aa2fc08de0b | -3.41742 | -60.1995 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f7bb2ae2-1042-3331-8ade-86b61d6edaba | -3.24366 | -53.95368 | 2026-09-22 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 01a51f32-b75b-3315-9426-67613d0345f5 | -8.60445 | -54.62043 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce8a31c4-fdcd-324d-b3d3-f746521aead0 | -8.24336 | -55.27853 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 263015ef-0407-3b5d-aada-d77cd0243b78 | -10.74174 | -50.81572 | 2026-09-22 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 79fff6b0-24ea-32f7-8aea-319bfec42803 | -11.146 | -42.83405 | 2026-09-22 04:46:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 83649698-1f43-361b-9d01-18e791487003 | -9.12526 | -58.92117 | 2026-09-22 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9976250-91f9-399b-b6c8-83e1f1ca9b3c | -5.87076 | -52.03044 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 75db7c3a-e1a6-3139-8d14-4c0f990d3189 | -3.0085 | -54.1787 | 2026-09-22 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 654c5ee9-046a-3583-9a47-289b3fe7428d | -10.68551 | -48.709 | 2026-09-22 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cae01b4c-76f0-3b1a-84f5-d88b15b64da0 | -6.78427 | -48.66695 | 2026-09-22 04:46:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0cde86e2-d65f-3f2f-af43-e06c4308efac | -6.62423 | -59.92207 | 2026-09-22 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 49d8d569-55bc-36cd-94fd-7dac4115b2af | -2.87458 | -57.79477 | 2026-09-22 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32809769-bf80-3e42-9565-ced9d085daae | -3.44304 | -50.61251 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0eef321d-0ffa-360b-8731-f8b8d8d15ddd | -3.90591 | -51.88717 | 2026-09-22 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 495868fb-6009-3c8f-ac54-4afe4d1a2a74 | -6.96365 | -44.40111 | 2026-09-22 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b15e3c9f-2ca1-3ef8-a166-815ffaab76e3 | -9.90236 | -48.49055 | 2026-09-22 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eec45c97-b7cf-3339-9c6e-0af82035e896 | -7.5979 | -57.67331 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5d0944dd-a4fd-3cc2-9152-55ed0042576f | -6.35907 | -58.27759 | 2026-09-22 04:46:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e0360d9e-076c-3722-a4a1-bc0d97fc3608 | -5.85422 | -49.78134 | 2026-09-22 04:46:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 04189b8b-2297-3275-a853-d184ea41cefb | -6.70739 | -58.99883 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5c99914e-26b4-3374-9ecc-049367c43e0e | -6.67419 | -47.37438 | 2026-09-22 04:46:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d55681b5-6cac-369b-9385-c648a40b8325 | -6.9169 | -59.63558 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9bfcb9e8-ff8d-3f8c-8fb5-f91bcbf2dc13 | -3.10698 | -60.7218 | 2026-09-22 04:46:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b47011c-6b6e-350e-9e5d-6f1a72d781de | -9.65196 | -49.1391 | 2026-09-22 04:46:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a77470b7-fd46-323e-a18c-389377fc62ae | -6.73668 | -55.06835 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cd7acf21-3ab3-31f5-911f-9cbfbb2c1113 | -3.24053 | -53.95027 | 2026-09-22 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 658dd15d-f52b-379f-b592-fcd878aa5e47 | -6.87002 | -42.86868 | 2026-09-22 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5bf8bcf1-91ea-307c-931f-9e6988a1bf96 | -5.86627 | -52.12354 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| add7c1be-3159-3335-bcbb-dbe8e68e8ada | -5.8707 | -51.94458 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 541870da-84f9-3372-99b8-47415b054082 | -7.4534 | -44.74642 | 2026-09-22 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6c9eb4d0-12be-3913-a892-0b786066e640 | -3.46679 | -59.53165 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83cee617-b77b-353a-8879-6de1459a518f | -5.76081 | -45.09449 | 2026-09-22 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ec510cf2-ebcc-329b-ab65-7fbf5d65b7db | -3.82328 | -59.3362 | 2026-09-22 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f68eef42-6da6-3188-9a86-b2221793c0d8 | -8.30955 | -40.59997 | 2026-09-22 04:46:00 | NOAA-21 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |


[Clique aqui para ver as próximas entradas](README63.md)
