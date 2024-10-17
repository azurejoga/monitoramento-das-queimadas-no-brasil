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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1596c0ca-1fdb-3ae0-8add-266bccb27c49 | -4.35719 | -50.97483 | 2024-10-17 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80af6e9e-7638-375d-9b66-30a8b4bb0531 | -4.35575 | -50.98352 | 2024-10-17 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe8ecadf-8e4d-359a-8217-cf7e77b41a47 | -4.35262 | -50.97112 | 2024-10-17 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e7a0aa3-f63d-365b-897b-4edf8f17ac03 | -4.35214 | -50.974 | 2024-10-17 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad93d2ed-3633-3225-881d-7c0d76d8122e | -4.35167 | -50.97688 | 2024-10-17 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12c63f5a-819a-36ec-b359-ea446a6a12ff | -4.35118 | -50.97979 | 2024-10-17 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdc4dfcc-3440-3ec9-8471-8efd39904eb1 | -4.35069 | -50.98275 | 2024-10-17 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 521e73aa-ec2b-3bf0-83b1-47afad88f754 | -4.35019 | -50.98574 | 2024-10-17 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 616e4797-bea1-3e8b-b6b0-7c79cb1ce79e | -4.28701 | -50.96016 | 2024-10-17 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7ff7d841-9d79-3bce-9383-60bb2150507e | -4.2865 | -50.9631 | 2024-10-17 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 134d00bf-7732-37db-b753-3e62cd366d8d | -4.07026 | -51.11979 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af36b5c3-f116-3a8d-8f91-ce273e9ee382 | -4.06975 | -51.12281 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dfa70ebd-3797-3e0d-87ba-dc676e4fa6d1 | -3.35858 | -53.21759 | 2024-10-17 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dfd10483-e9a8-39bf-afb3-4ddda82d4aea | -3.35197 | -53.22054 | 2024-10-17 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ced6507f-e839-3e5e-8fe9-410341fc4c95 | -3.35008 | -53.21489 | 2024-10-17 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 2ef24782-78a3-309e-a5f7-f653fb71b653 | -3.34934 | -53.2192 | 2024-10-17 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| f3781121-f756-3586-b920-835b0f4a02fb | -3.34678 | -53.21494 | 2024-10-17 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| c3e30698-7c46-39fa-ab73-e2e24c4e8e97 | -3.34605 | -53.21936 | 2024-10-17 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 6249fc26-7931-38c2-ad32-39c26e93adef | -2.7828 | -52.10323 | 2024-10-17 04:12:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12b77f7c-2912-33e6-b523-4c24773ddaaf | -2.77904 | -52.10152 | 2024-10-17 04:12:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| aa7718d7-ee50-3bc7-8ad7-927fdb3957e4 | -2.77843 | -52.10527 | 2024-10-17 04:12:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d5dbca2b-8eac-3783-aa79-7652cd5b0755 | -2.77785 | -52.09857 | 2024-10-17 04:12:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6214ea28-8181-3990-9f4c-d2e563823f47 | -2.77721 | -52.1023 | 2024-10-17 04:12:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c162516-f7e2-3c5b-ab4a-4160c79861c0 | -2.77657 | -52.10605 | 2024-10-17 04:12:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ecf8ef65-6f52-3071-99e7-fe22f4bb1cb2 | -2.77344 | -52.10072 | 2024-10-17 04:12:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cfc70924-26a1-3fd9-a4ce-2d27a61c411d | -3.90289 | -52.37959 | 2024-10-17 04:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2bd6472-5604-34ae-94d4-b552dca168de | -3.89484 | -52.39342 | 2024-10-17 04:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c19a0ab4-ca61-33ff-9734-e3f1137f3058 | -3.89422 | -52.39709 | 2024-10-17 04:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8839fa42-eaa0-3ffa-87f0-970f955800c4 | -3.775 | -52.39941 | 2024-10-17 04:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 55bce199-beab-370b-b4b0-1315b49cbe22 | -3.1137 | -53.74698 | 2024-10-17 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47c35940-607e-3ab4-8771-a6eaad398fbb | -3.11289 | -53.75177 | 2024-10-17 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6db3a425-c75d-373d-b061-e5afd3d5e35d | -3.10914 | -53.73632 | 2024-10-17 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e6096526-c698-38b5-bfb4-668f8f6f1120 | -2.32896 | -54.40774 | 2024-10-17 04:12:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f63cd42f-52f2-335c-8735-7728d0eea7e6 | -2.32339 | -54.40115 | 2024-10-17 04:12:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7ea51812-1ee1-3fa6-8ea5-23bd6410cc29 | -2.32247 | -54.40661 | 2024-10-17 04:12:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 74c08db1-de3d-333f-8dd3-9cdbd76a3d9f | -5.14019 | -42.8827 | 2024-10-17 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db827419-7ad1-362a-9179-bdfa1382470d | -6.74387 | -35.25635 | 2024-10-17 04:12:00 | NOAA-20 | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 660282be-5f32-332b-93dd-e8018ccbb44f | -6.75324 | -34.96754 | 2024-10-17 04:12:00 | NOAA-20 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7e83f94a-5e12-3d60-88de-6d4577fddbcc | -9.74276 | -37.84323 | 2024-10-17 04:12:00 | NOAA-20 | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4457ba95-a991-3044-97af-60e42c250738 | -10.961 | -37.1061 | 2024-10-17 04:12:00 | NOAA-20 | SÃO CRISTÓVÃO | SERGIPE | Brasil | 2806701 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 24f8ed71-b49e-3eaa-a8ca-e6432ae0b172 | -4.83306 | -38.3732 | 2024-10-17 04:12:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 35570a74-6f01-3f5b-9d29-6c4fb44c60a2 | -5.22842 | -37.7146 | 2024-10-17 04:12:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 479ba1ab-6b2e-3bed-b040-d974c17fa063 | -5.95025 | -39.6769 | 2024-10-17 04:12:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 251f9626-7d75-3922-8960-bf382506022b | -7.15312 | -40.2265 | 2024-10-17 04:12:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bbc395e4-c97c-3435-90d9-6fc5e3272483 | -7.15374 | -40.22242 | 2024-10-17 04:12:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c038ee39-7d4d-34f5-97c1-0fa24db89b37 | -7.8166 | -40.76392 | 2024-10-17 04:12:00 | NOAA-20 | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 71dc38c6-7656-38db-a17f-eefcf9bcbe2a | -9.18744 | -40.24327 | 2024-10-17 04:12:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fdd00b5d-41bd-3927-870a-3c00bba129df | -8.72592 | -40.58223 | 2024-10-17 04:12:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9873a106-226a-369d-a47b-bd0b792f4ba4 | -8.50488 | -39.93582 | 2024-10-17 04:12:00 | NOAA-20 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b16afb32-275e-3c6f-b41b-c2eda85e692a | -8.50422 | -39.94024 | 2024-10-17 04:12:00 | NOAA-20 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f8bbd271-f175-358d-abb9-92295e05c62f | -8.7253 | -40.58632 | 2024-10-17 04:12:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a40acce6-278d-3cf7-b734-fb7f7b037851 | -8.50857 | -39.93637 | 2024-10-17 04:12:00 | NOAA-20 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a18fb7c3-6ff3-3827-9aa6-cfd6cc87a69d | -8.50791 | -39.94079 | 2024-10-17 04:12:00 | NOAA-20 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8e960bc5-7bff-30a7-b822-d18d0f28a00e | -5.49645 | -40.78041 | 2024-10-17 04:12:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e66e0475-8324-389c-8f2a-335fc1cd6793 | -7.99128 | -40.97266 | 2024-10-17 04:12:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5339fc83-a6f5-32a9-9940-b66ed4620cda | -7.50642 | -41.2388 | 2024-10-17 04:12:00 | NOAA-20 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d18151c6-ead3-3dd9-bae3-f3936f2752fc | -7.99187 | -40.96877 | 2024-10-17 04:12:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c502f955-2dd3-3097-98c4-9240bdd8c4bc | -8.71085 | -41.16441 | 2024-10-17 04:12:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b79e98a3-3888-3223-a82a-67cf991dfed9 | -8.70736 | -41.16388 | 2024-10-17 04:12:00 | NOAA-20 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e6012d25-1549-33da-bf93-3f98979ba709 | -8.14319 | -41.14485 | 2024-10-17 04:12:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 06c79c8a-7bee-3dca-b14f-8717c7d17892 | -8.08389 | -41.07723 | 2024-10-17 04:12:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3384fe22-58bf-34f2-bd63-a0eaf6f67a15 | -8.70677 | -41.16782 | 2024-10-17 04:12:00 | NOAA-20 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c4dd9eea-9376-354b-93f7-244bfc00a0ca | -8.19332 | -41.30523 | 2024-10-17 04:12:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5d132e96-f625-3562-86cb-43d3c10dc5fa | -8.08331 | -41.08107 | 2024-10-17 04:12:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2bcf5616-6754-349d-85c0-c7db957d32b4 | -7.96555 | -41.60443 | 2024-10-17 04:12:00 | NOAA-20 | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5b3a12d2-322f-3948-b173-89051d06826d | -8.82107 | -41.27172 | 2024-10-17 04:12:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 0557ca2d-443b-352e-b66a-02170e19be72 | -8.71026 | -41.16835 | 2024-10-17 04:12:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8e9dbdb0-7c95-3a70-b264-e02697128f17 | -8.08737 | -41.07776 | 2024-10-17 04:12:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7a3269d4-e9bd-3c63-b310-d313c90172c0 | -9.90268 | -42.10279 | 2024-10-17 04:12:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dd77b988-03a7-3196-b000-34f722f45a67 | -9.90212 | -42.10648 | 2024-10-17 04:12:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b795fa3c-41aa-34f3-971c-7dd0b4e6dcd3 | -3.93594 | -42.41822 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 390b09de-c83a-342f-8e05-7d68186788ad | -3.93264 | -42.41771 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0745583c-4acb-3b52-b503-cf1ef66b1a6b | -3.9321 | -42.42115 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bd21580b-9225-324c-8ed0-79a3a2aadd69 | -3.92988 | -42.41376 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5725c41f-97a7-3ff8-be73-f33a3876cc6f | -13.42477 | -48.06487 | 2024-10-17 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8a2be27-f850-3028-969b-13313eac0287 | -13.12026 | -48.24325 | 2024-10-17 04:14:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13ff123d-81af-331d-a590-e911576737e1 | -12.22234 | -50.34618 | 2024-10-17 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4daee315-ad60-30eb-8c2a-33f7d68af14e | -12.21883 | -50.34137 | 2024-10-17 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 25eb7a48-2009-3282-b574-ee8e02cd66d4 | -12.21811 | -50.34539 | 2024-10-17 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c8ee6c5a-bbaf-3b3e-8703-aae7223c9159 | -12.21739 | -50.34941 | 2024-10-17 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf5d8b39-45a9-3fed-9348-a5278eec4865 | -12.18242 | -50.32855 | 2024-10-17 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76f97b36-710c-3553-bb2f-4ccc524047fa | -11.15353 | -49.70327 | 2024-10-17 04:14:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2346fe67-da00-3f84-b9df-d8594c0cbe14 | -10.99534 | -49.78925 | 2024-10-17 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 95bcf680-cc8a-3708-a341-7226154aa6e4 | -16.35222 | -50.58701 | 2024-10-17 04:14:00 | NOAA-20 | CÓRREGO DO OURO | GOIÁS | Brasil | 5205703 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9324df15-a847-3821-b2b6-95f632e50962 | -16.15442 | -51.40945 | 2024-10-17 04:14:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 610ef32c-a195-3417-83ad-a538b126f8cf | -15.68414 | -51.39096 | 2024-10-17 04:14:00 | NOAA-20 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f769cdb7-f203-3897-ad87-9fd5441bf445 | -15.68296 | -51.38803 | 2024-10-17 04:14:00 | NOAA-20 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5dab08b9-e072-3a89-9006-e629d46cfecd | -10.67359 | -51.56892 | 2024-10-17 04:14:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fecb7a3d-dd1e-3903-b606-c5955f9ab5f5 | -11.59059 | -51.01662 | 2024-10-17 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5465c7e-e2d9-3f2c-861b-40b7538dadf1 | -11.58613 | -51.01576 | 2024-10-17 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc380d2c-2c30-3860-9aa4-e984067401d7 | -10.19798 | -52.32652 | 2024-10-17 04:14:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fd5d4f2e-f3e8-37cf-be54-495aaf78504c | -10.19329 | -52.32528 | 2024-10-17 04:14:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 43bb36d6-fbc8-38bf-a77c-76a411a7d3e1 | -10.19299 | -52.32553 | 2024-10-17 04:14:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6a58a475-df8e-32b7-889c-1ad516940b65 | -10.19276 | -52.3282 | 2024-10-17 04:14:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 21625178-058c-37a2-9063-5360c73525e0 | -10.19245 | -52.32843 | 2024-10-17 04:14:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 64badafd-2a68-3539-95ac-bd1422add23b | -10.19224 | -52.33111 | 2024-10-17 04:14:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a4a6df79-d28d-350e-990c-fac9e7ea9da2 | -12.36776 | -53.14174 | 2024-10-17 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a810c085-6a24-3638-984f-6ed1f8c39498 | -12.36269 | -53.14071 | 2024-10-17 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 490691c9-3cc8-38e1-9156-71c4cee28857 | -15.32261 | -53.30831 | 2024-10-17 04:14:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f5775b21-7981-32fc-9529-dfa95c9f07bc | -15.32011 | -53.30748 | 2024-10-17 04:14:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README33.md)
