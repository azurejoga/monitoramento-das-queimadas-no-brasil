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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92f2a231-83f6-3a88-8407-d044799ceac9 | -2.88045 | -51.03236 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99e19b7a-8588-3cd2-96fa-5c6aa83de74e | -2.86028 | -53.91737 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4eaa2d7-a9b1-326a-81d1-069924303096 | -1.05693 | -53.58995 | 2026-10-07 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b34c436-2f4a-3fd0-a2fe-cbcb71650d9b | -3.06398 | -54.15827 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd1e4e1f-f2a1-3656-8dd8-6aceed53344b | -2.55322 | -57.3909 | 2026-10-07 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cc869719-b303-3708-ad12-12cc655e9b27 | -3.0505 | -57.15332 | 2026-10-07 05:04:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2fe00838-a878-34b5-a538-89dc7386a641 | -3.34441 | -59.4817 | 2026-10-07 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c684ddb6-17c0-36b5-a04e-f6f313fe4484 | -3.86352 | -55.99264 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 190cd9bd-54f4-3380-9b1a-ad5f7202f005 | -3.91038 | -55.89115 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5233b1f-dbc0-3e42-be30-0cace38d6e8f | -3.04599 | -53.90257 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1d5ab03d-ff77-37f1-b6bf-452886ea079c | -3.74676 | -59.44387 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 070ad5a7-94ce-3570-b058-9b3ef001dc8b | -3.65985 | -60.62673 | 2026-10-07 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4d14b0a6-8927-3e3c-8e05-0710f6e00312 | -3.56889 | -54.47982 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08b269ef-af4f-3842-b691-8cc9319ce792 | -3.03593 | -53.90102 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1ea0cf0e-6d1e-364f-bf5d-4f185d4f4e27 | -3.35998 | -50.47461 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7d378e1-fc2a-36ac-a813-002839d5fac7 | -3.51504 | -54.62819 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f27f002-df1c-3fca-832f-fe290764736a | -4.75757 | -55.65118 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1d81b344-409a-346b-87e2-78ad2dcddc34 | -3.08873 | -53.71535 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9d12216-b02b-3b29-8087-0a706508be5b | -4.24378 | -49.97761 | 2026-10-07 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 870b1f1d-9888-38f0-921f-c6ae892efe15 | -3.54206 | -54.65349 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a227a6b8-b8f5-36b5-9474-76eb18d9c915 | -3.11062 | -53.70769 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7cc13353-fc63-3255-90e9-2313cc46657e | -3.11123 | -53.77021 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4416be9a-ee11-30a5-943e-dd9ece1c418a | -4.76256 | -55.6625 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be3ab8a3-634b-38af-af4f-8e46fcd7cdd5 | -2.99951 | -54.18062 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fe1f69d-d57b-38d3-aff2-678c2d668f3b | -3.80831 | -51.53587 | 2026-10-07 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3e3a0a4-2c75-3611-8d03-c5fb815104a9 | -2.38595 | -56.12762 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e2f6821-9067-3fa3-9648-8b44bdc0d15f | -2.87429 | -54.17591 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| abb028a3-9bca-3b63-bba3-a0eeb0a40fa7 | -4.7631 | -55.65907 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04a879c3-7276-3050-b70e-4c55cf54c734 | -2.98991 | -54.13251 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5122d710-2de8-3410-a589-4b5552d48567 | -3.4687 | -50.08371 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e647f927-162c-355d-a5b4-b5d97a3af72f | -3.11571 | -53.76357 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2eca8c2-ca88-36cb-addf-72a39a0511f6 | -3.04104 | -53.93452 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25a0b9cc-b773-3b72-8101-e6ba438cb152 | -3.49502 | -59.27126 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d68be5ce-18af-30c8-bc75-b7b1b81db6cd | -2.93638 | -54.17114 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d252974-5589-370d-b1fb-18b4ceb0ab8a | -3.06236 | -54.16881 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ae9a1e91-3330-3ff0-adf9-b097742dd9bf | -3.53212 | -54.65197 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90e5102e-4ded-3c59-b922-e498e7b6bdc6 | -3.67938 | -55.95359 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41ad70f7-786a-398b-9be7-9af00d276bfd | -6.92251 | -43.67284 | 2026-10-07 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 29b27502-4704-31a9-b169-aa013e6a67f4 | -3.78919 | -50.87429 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57a172e2-ad57-3ca4-b24b-f902b049847f | -6.40522 | -52.71618 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 713338d4-bb6f-37d8-ac56-d86ff5388449 | -2.44987 | -50.25496 | 2026-10-07 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 857c8861-c25d-3783-9d34-56e53ca24eef | -5.98856 | -55.37179 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 642a4dbf-16b2-3e2f-82d0-4c2307c2499c | -6.15387 | -51.73199 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a36e53bc-0abd-3eb3-bedf-9521b7b01149 | -3.46901 | -50.08365 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5c947e9f-7380-3d15-aa37-c4c65104c60f | -3.24285 | -56.80257 | 2026-10-07 05:04:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7afff7ac-085a-318d-b6e6-9d27f60ba7c7 | -2.78837 | -51.67476 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 77e470ea-b770-33f4-b950-1129fe41a011 | 1.03359 | -59.44874 | 2026-10-07 05:04:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a7d8a70-8a57-310e-bf77-ba0313587d2d | -3.28283 | -54.06614 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bfe65535-7a06-38ac-8558-a6ec02e2346f | -3.14772 | -51.62428 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bd055525-6cf0-3da2-a66d-0e29497e6579 | -2.93458 | -54.11702 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 897358d2-7beb-3aa8-8edb-71310ee103b1 | -3.28157 | -50.41027 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a3d4331-5e0a-3efd-946f-c0822cf35c62 | -7.24895 | -45.25813 | 2026-10-07 05:04:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 97b14074-d2e1-357d-b0d5-8da7e282ab5f | -3.60858 | -54.59633 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d9ae5a34-185d-387a-aa49-b99a8c1c34c2 | -5.03589 | -50.0144 | 2026-10-07 05:04:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa2ab7d4-b04a-3db4-ad02-b47f16cfc129 | -3.35752 | -43.39154 | 2026-10-07 05:04:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a20ead1-d3ff-3665-ae05-c3f5cdfc488f | -3.04547 | -54.14826 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d5eb86a6-0725-3fe5-b551-d0a3a9047a82 | -3.68465 | -45.83749 | 2026-10-07 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a15951da-9207-3edf-87d0-4e0fc12734a3 | -3.68599 | -55.95461 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| efa7f04d-3883-3ccc-8ef2-278f6597ac6e | -3.38839 | -54.1721 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82022f48-04d5-37c3-98ee-48641376e29b | -3.09883 | -53.71692 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9df01a7c-ec11-37cd-9dff-3c1d0a8d689a | -3.06713 | -54.24839 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5205571a-1db1-3adc-b223-6bbd6d1aa0a5 | -3.05975 | -54.20789 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f1583828-d700-38da-84dd-71ecdba6571f | -4.06443 | -59.83352 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fceeaf3e-190a-3b26-b479-254ef2fec176 | -2.99647 | -51.00906 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5acc38f2-62c1-3ca5-ae5b-a6035a1974f1 | -3.02588 | -53.89948 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ce3ddd6e-fbdb-3d72-a0a2-91ea08580dc4 | -4.11755 | -50.83006 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6768432-b652-3f79-a0f4-d17c32dd7af2 | -3.50849 | -54.64845 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de912e4b-f724-3f3a-83b1-238dcf7b9191 | -4.16012 | -55.16317 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8a63eb3a-5521-36b7-8f98-3475db526c71 | -3.83316 | -55.97026 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a12ca4b-0a09-3f7d-80c7-0c449a87cda9 | -2.96951 | -57.84079 | 2026-10-07 05:04:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31f08628-dc3d-365e-b89e-3b6715af8d89 | -3.04439 | -53.93504 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffb2b47d-d421-39dc-9f8c-3103fc6c3775 | -3.2844 | -54.01207 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3dca84b9-f62e-3f47-8c8d-041dd86fe9ec | -3.63113 | -55.28028 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 542ed25e-f9b6-3c13-9777-eb50904059e8 | -4.06204 | -56.33335 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a97bd55-7bcf-35e5-90b6-0513dcc5e349 | -1.54117 | -54.78091 | 2026-10-07 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e29952ef-3981-30e9-aedd-5636aa4a021d | -3.2872 | -54.01612 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 32acb79b-c150-36a4-949e-00103c6acb00 | -3.28169 | -54.05151 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a19f0300-4bda-37da-aa94-b0c72335cb28 | -3.0843 | -54.2475 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 95296b2b-cfa8-38c0-9de0-711bdb38c618 | -3.27331 | -54.03936 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 8a921161-cf04-3058-9829-a1a823dabad8 | -3.73846 | -59.4473 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4ed6f063-bc1e-3817-abf4-f1b9e38c2773 | -4.11458 | -54.42513 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff32b6ee-efde-34d3-b057-f17d3f4e772f | -3.01657 | -54.13662 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eb2e1893-5a16-30d6-8713-5248fe62afc5 | -3.85083 | -55.98714 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| cf7d1b44-e3c7-3bfb-bf0f-7f6b21787768 | -3.15588 | -50.44393 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d7bac45-cc48-3b30-bd58-f449599b1ce6 | -3.10282 | -54.14978 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0425786-3303-38b5-8814-3334c1f76cca | -4.44766 | -54.97557 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a2accc47-ece9-330d-a4b8-9993e9741e8b | -4.23905 | -49.98074 | 2026-10-07 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c73d0e2-c91f-330e-8ca0-a50737ebdee2 | -3.02269 | -54.14114 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e86e6e09-16f0-33e7-a21c-f27ae77edd94 | -2.03367 | -55.63843 | 2026-10-07 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 897e2b0b-74f6-3efc-8a61-6bffd7955bff | -4.15736 | -55.15923 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b3e3040-c18a-3f62-b9b4-f19e393b844b | -2.10296 | -52.06784 | 2026-10-07 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 26f57e0e-b0a5-383c-8684-5c63df866a7b | -2.86996 | -54.20391 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ecfcf102-cdef-3a38-9f30-7483e4253d2f | -4.92241 | -55.86037 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d3baaad-7a14-351a-b6dd-7192dc1179c7 | -3.18081 | -50.57151 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 2dbf95c5-1f50-3c52-9e58-677f3c4ae05f | -2.85355 | -59.10669 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4fd8f08c-8abc-35b6-b7d7-9c2fd8add6bd | -1.72874 | -57.26979 | 2026-10-07 05:04:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6379bfdd-5769-3289-8348-e3f31d467a89 | -3.64868 | -55.27596 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42050a13-c7a4-3b47-8525-4ac65e497d2c | -3.50511 | -54.62665 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da357bde-71cd-359e-9ffe-3ee189883ad1 | -3.53982 | -54.64605 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 9928cb85-e498-3ea8-9b80-df8a0562613b | -8.70886 | -45.20047 | 2026-10-07 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |


[Clique aqui para ver as próximas entradas](README85.md)
