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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9dabed26-9186-3ce1-b08b-85f18c261eaf | -8.5214 | -43.2828 | 2025-07-10 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.1 |
| 0fc543cc-5a93-3eb0-b702-04344dfb3ad1 | -8.5028 | -43.2614 | 2025-07-10 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 93.8 |
| f28c87cd-8ede-307b-8c1c-03324eef1c40 | -10.6489 | -49.4483 | 2025-07-10 02:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 0348bb38-32c0-32cb-891f-10ed33f293d4 | -10.6678 | -49.4462 | 2025-07-10 02:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| bf47aadf-c0be-3ae5-b962-7906ca2d4672 | -6.8485 | -42.7979 | 2025-07-10 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.6 |
| f42efd6d-4354-3c34-8d59-37c33e955b6c | -10.5773 | -49.1533 | 2025-07-10 02:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 50e41ddb-0964-350b-8092-5a2999f6ba17 | -10.5776 | -49.1316 | 2025-07-10 02:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 68233c9f-c2b2-3ac1-8d7c-de5fc78b497b | -13.338 | -52.9054 | 2025-07-10 02:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 8c3879d4-a8d8-3280-8281-d75cfb2c63eb | -10.6675 | -49.4679 | 2025-07-10 02:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 95f4f386-62ea-3720-83ea-d13bd5f521d8 | -13.3571 | -52.9032 | 2025-07-10 02:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 05d70098-2ecc-38b6-a969-3573d5d6a38f | -10.6486 | -49.47 | 2025-07-10 02:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 180107d4-feaf-3dea-839f-1ebb4dedd62d | -13.3383 | -52.8844 | 2025-07-10 02:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 43.5 |
| c1265bba-d50f-396e-834d-56378916d7d6 | -10.6675 | -49.4679 | 2025-07-10 02:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 143.4 |
| 1a6acfbc-6af9-30a4-8ec2-7491d2f5c59c | -13.338 | -52.9054 | 2025-07-10 02:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 46.9 |
| e03faf43-71fc-3d84-954f-d55494272200 | -10.5773 | -49.1533 | 2025-07-10 02:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 4d13b2ed-791d-3a7b-ab83-c2f3ab518c6f | -10.6486 | -49.47 | 2025-07-10 02:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 29a24f5b-8620-3d29-8aa5-77ece1fb238c | -10.5776 | -49.1316 | 2025-07-10 02:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 57a8dc74-9a5d-3638-8c72-118775157dba | -10.6678 | -49.4462 | 2025-07-10 02:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 934a8bc6-2426-369b-82ef-73001236a6ff | -10.6489 | -49.4483 | 2025-07-10 02:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| cc93304f-4f6f-34c1-89f6-609398a22e38 | -10.6678 | -49.4462 | 2025-07-10 02:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 148d0eff-d3ac-3813-ae2c-187339c6d9ae | -10.6486 | -49.47 | 2025-07-10 02:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 25d8f2bf-ecc0-3f87-b4c2-33b2f4d700d5 | -10.5773 | -49.1533 | 2025-07-10 02:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 716b651e-39ad-357e-95d6-f2d8c4feadf9 | -10.5586 | -49.1337 | 2025-07-10 02:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 600a7c9d-7989-36be-b4d1-65ad3c4e2d89 | -6.8485 | -42.7979 | 2025-07-10 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.6 |
| 47dab11b-08d5-375b-9e56-9a97c1fff9ed | -10.6675 | -49.4679 | 2025-07-10 02:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 164.4 |
| 4f021fde-4cfc-3fb1-b161-98a82469b3aa | -10.5583 | -49.1554 | 2025-07-10 02:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 1dc8affb-d435-3952-acf5-9eb1c407f6f0 | -10.5776 | -49.1316 | 2025-07-10 02:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| f02f6b1d-e5b7-3b6f-b388-beaf5af30975 | -10.6486 | -49.47 | 2025-07-10 02:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 2d8566b8-8ac6-37e8-acfc-5cdd93c3c6f4 | -10.5773 | -49.1533 | 2025-07-10 02:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| e7d530fb-e123-3b00-96f0-a24b773bdb6f | -6.8485 | -42.7979 | 2025-07-10 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.2 |
| 8089f820-6951-3ca9-9914-af18c9c41650 | -10.5586 | -49.1337 | 2025-07-10 02:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 6ccdfc87-792a-31a5-8053-2dd4bef91bed | -10.6678 | -49.4462 | 2025-07-10 02:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| c637ee86-203f-3e1c-bb42-d802034bc594 | -10.5776 | -49.1316 | 2025-07-10 02:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 1122cc4c-fd1e-33ba-9ed9-2c692fea2447 | -10.6675 | -49.4679 | 2025-07-10 02:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 3e5f9b8c-63c0-31bc-9087-4d92ea58077c | -10.6489 | -49.4483 | 2025-07-10 02:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 43cd3596-4bd4-3aa7-8130-81271027362b | -10.6675 | -49.4679 | 2025-07-10 03:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 16c56991-8d70-32f0-a175-7a5aab2458ac | -10.6678 | -49.4462 | 2025-07-10 03:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 52107776-ac36-3662-abc2-1487317e0f21 | -10.5773 | -49.1533 | 2025-07-10 03:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 72e65018-e673-3dad-b996-e5dbfdc57af4 | -10.5776 | -49.1316 | 2025-07-10 03:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 3ec98e8a-f42b-3949-bc99-2660104430e9 | -10.6675 | -49.4679 | 2025-07-10 03:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 147.4 |
| 193399c1-0c45-332d-900c-9274b9623ce0 | -10.5776 | -49.1316 | 2025-07-10 03:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 822dcf4a-f030-3570-94f9-91fad7ad2f30 | -10.6678 | -49.4462 | 2025-07-10 03:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 103cfc09-93f3-377a-89b0-18ca53399e42 | -10.5773 | -49.1533 | 2025-07-10 03:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 61044db3-c0d7-34c2-9612-501f7df036b1 | -10.5773 | -49.1533 | 2025-07-10 03:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 253c5b44-300c-35ba-b4e0-aeaca0aafe18 | -10.5776 | -49.1316 | 2025-07-10 03:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 88d82040-a891-3a29-9f9f-64a5b303bb68 | -10.6678 | -49.4462 | 2025-07-10 03:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 9f473942-7a7f-39f0-942c-c2479590d5d6 | -10.6675 | -49.4679 | 2025-07-10 03:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 77aa7c51-cb32-34e0-a514-e1533aac8fd5 | -8.5025 | -43.285 | 2025-07-10 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 245.6 |
| e58c9635-9401-3779-a796-d6b64c4afa83 | -10.6678 | -49.4462 | 2025-07-10 03:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| ce923c55-4c67-318a-b513-2fa2e781f38b | -8.5018 | -43.332 | 2025-07-10 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 93.8 |
| b92b2103-2406-33e9-8bac-96fc58702a0c | -8.5211 | -43.3063 | 2025-07-10 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 102.7 |
| b70ae931-2523-328e-8f30-b8935bf308c4 | -10.5773 | -49.1533 | 2025-07-10 03:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| d19e00a9-b633-33e9-8883-6f8f6605839d | -8.5028 | -43.2614 | 2025-07-10 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 102.6 |
| 3b6c37af-5796-3f95-9d83-05812e302b1d | -10.6675 | -49.4679 | 2025-07-10 03:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 47e25eee-f1e3-3de1-abc2-9c4bf0b15090 | -8.5022 | -43.3085 | 2025-07-10 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 263.3 |
| 47f62d12-77c1-3113-bb54-4486c1034cc4 | -8.5208 | -43.3298 | 2025-07-10 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 54.5 |
| 92ce91a9-7a7c-3603-8c88-de439ca8e9f2 | -10.5776 | -49.1316 | 2025-07-10 03:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 107.0 |
| aa2681a7-7a56-3cb3-ad14-43dff758b578 | -6.85186 | -42.80676 | 2025-07-10 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 8a754c65-4784-3898-854c-2957bf4c6d8b | -8.5073 | -43.31567 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 45.8 |
| b5665694-1a5e-3cc7-ac49-4d598b9c99f0 | -3.81566 | -42.54581 | 2025-07-10 03:36:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7194f237-c998-3cb1-8ed9-b2cf8c12d82b | -7.23495 | -43.08242 | 2025-07-10 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c4081092-8946-3ccb-8b3f-bf4f6e0ec048 | -6.99614 | -43.52152 | 2025-07-10 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00a1c92c-d84a-34a4-9cc3-03cdb63f40a0 | -7.48504 | -43.93483 | 2025-07-10 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a4028af9-060d-3136-b74c-cf154c8336f1 | -6.67648 | -46.30438 | 2025-07-10 03:36:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 57bc9821-8fa8-3eb4-b228-9d4e892c1e55 | -7.23085 | -43.07486 | 2025-07-10 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 79605761-2e0d-3158-b10b-578a9c2da0ed | -6.95934 | -42.71996 | 2025-07-10 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 37c5ed8d-1835-3613-870e-af235b30eb94 | -7.22554 | -43.07397 | 2025-07-10 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 25bffd0a-f760-368e-890e-f84979cc4467 | -6.85764 | -42.8046 | 2025-07-10 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| c4eca481-3130-36db-b20a-3ee3360b095c | -7.4757 | -34.84439 | 2025-07-10 03:36:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 51533662-5ad5-3e7d-b3da-8fb25baac019 | -6.85354 | -42.79731 | 2025-07-10 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 09a3c3b2-e759-3b64-86ac-b74806430f06 | -6.95323 | -42.71926 | 2025-07-10 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 74744e44-04e2-37ef-b094-20b4add58d5e | -7.02901 | -43.49493 | 2025-07-10 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 620f3bbc-0e91-3dc0-8952-4a184600c299 | -6.93685 | -43.0272 | 2025-07-10 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9588c54a-c875-348d-bd82-7373270f8c85 | -8.49569 | -43.29 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 862bc4f5-28d2-3f3a-a7e1-2c970ee12c33 | -8.50263 | -43.31147 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 45.8 |
| 0c3d872c-e47d-36c8-8113-2997d2ccbd95 | -7.00899 | -44.42511 | 2025-07-10 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d40d6074-581f-3983-affc-0dd868db5cf6 | -6.93093 | -43.02971 | 2025-07-10 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 86011859-8007-3ace-b546-a6a5adebfa38 | -8.50203 | -43.31473 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 45.8 |
| 1439f749-f67c-32b1-8fbc-ae3ca44e58bf | -6.99677 | -43.51791 | 2025-07-10 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e0dca571-9b42-3fe1-bf56-d1ac9e918aad | -8.50272 | -43.28125 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 46.3 |
| 9d3ad6eb-f54b-3864-b4bd-dd969de20f81 | -8.36271 | -43.95002 | 2025-07-10 03:36:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ca7851d-ab70-3bcc-86e5-ad2eb5c374d6 | -8.50441 | -43.30169 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 2aa30c97-1ee3-30b2-941e-946d5def913c | -7.20627 | -45.35119 | 2025-07-10 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0dc3b4d1-e40a-323d-8760-fa5a5ab1736d | -8.51256 | -43.3166 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 26bd17be-a9c0-364a-b228-192b01f454ce | -6.99566 | -43.4923 | 2025-07-10 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 642e9224-f115-3278-b017-be39453f7367 | -6.9584 | -42.72036 | 2025-07-10 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 21182743-49cb-3374-bf95-1e1fcdb87aa9 | -7.22023 | -43.07311 | 2025-07-10 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 944517fc-7857-3b31-9ee4-456b509e364f | -8.36222 | -43.95218 | 2025-07-10 03:36:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b62765f-d849-3e30-8b85-c1870ad42d5b | -7.00659 | -43.49427 | 2025-07-10 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8005a009-400d-373d-8b06-a34faddfca43 | -7.74477 | -43.59182 | 2025-07-10 03:36:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c1af599d-9a4d-3269-bd9b-40f21a1f8cee | -7.03446 | -43.49603 | 2025-07-10 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1342c96e-84d3-3834-a48b-c3985797a607 | -6.98335 | -41.3674 | 2025-07-10 03:36:00 | NOAA-21 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1a906b8c-943f-3b17-8137-dd4b049674ba | -6.8582 | -42.80146 | 2025-07-10 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| b9e6606b-617b-3422-9ed4-ac624df0faee | -7.48312 | -43.9376 | 2025-07-10 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b0f818fa-e37f-390e-99d4-f815248453e8 | -6.12884 | -42.95808 | 2025-07-10 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| abe0e12a-d7d7-35ab-a154-47c1b1206586 | -6.99319 | -43.50624 | 2025-07-10 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fe7641fe-86f9-33c5-b974-a62dea5c2486 | -6.99504 | -43.49581 | 2025-07-10 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b078c1ca-77d7-358d-9f86-922999f81eec | -8.50551 | -43.32547 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| c84f3e4f-b225-368a-818a-3415a1c5ed9f | -8.5062 | -43.29192 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 13189394-65b8-3904-865f-9a1745db448e | -5.41373 | -46.07127 | 2025-07-10 03:36:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README8.md)
