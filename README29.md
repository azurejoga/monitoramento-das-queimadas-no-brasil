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
| 5abb9f38-4747-35a9-904c-e5b65916f293 | -2.63097 | -46.19943 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 47b25a3c-fbd6-3c5c-b728-288085499284 | -2.69232 | -46.15235 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dae0f724-8b86-3ce2-a51b-0ccd9dc6d0fd | -4.06419 | -49.06644 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 643cb194-f3b7-3168-a024-a82730f00cba | -2.3919 | -50.48961 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05e6ac3e-bcfa-3cb5-9ad8-b8bcac9009c0 | -3.93925 | -46.50072 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b561d7da-6bda-3bd3-9732-69331e76ccd1 | -3.38941 | -54.29012 | 2024-11-30 04:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17c53402-4f13-3509-8fb4-cdc0de0a803a | -3.25747 | -48.76428 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 729ae756-5481-3a85-86dc-b4c48656b78f | -1.56719 | -51.85898 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da31b618-c34d-3080-8848-4d0c81cb821a | -4.08667 | -47.02148 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ca0c2214-8d89-3a3a-86ff-e66ec34003f9 | -2.80902 | -53.04713 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 1ab48b71-989f-392f-8fbc-68341ae724a3 | -1.67542 | -48.15769 | 2024-11-30 04:40:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d02a728-2256-3487-997b-61b87e5baf8b | -4.44231 | -46.00932 | 2024-11-30 04:40:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d1008ed-13d8-3250-9c33-84da8e3b6b74 | -2.78531 | -51.66975 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ec0040bc-3952-3e05-8364-719aa7a7b463 | -3.28356 | -50.16178 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05122184-d4d8-3b3c-b1d0-a14c158aa7fb | -1.95277 | -48.68995 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a885ee7-c394-31c6-a8e3-a4db038c5452 | -2.27333 | -47.89936 | 2024-11-30 04:40:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0551c15-26fd-344c-ae1e-3b1dcce39c09 | -3.52987 | -50.75475 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d7b19859-001f-3eb1-83f5-1e91aeda72a2 | -3.30608 | -51.1032 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 64b57697-7306-3007-b813-aec45ec217af | -2.7201 | -48.63413 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4c4b7a5-f7a7-353b-b445-d748fa4b2c10 | -1.32628 | -51.67869 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e75c409e-1d9c-3ba4-8be8-d07b852b2463 | -3.79006 | -58.97586 | 2024-11-30 04:40:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9cb1a775-a1af-3faa-a079-f38202fc4dff | -2.04234 | -54.6973 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 655a21cb-32ea-3192-8581-96783e8cb602 | -2.86088 | -53.99491 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a45165a-f7ae-3d74-9450-a99799377fc4 | -2.72117 | -48.62727 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7bad70f-0c36-3f3d-966a-68cf4ae64afa | -1.68216 | -46.77987 | 2024-11-30 04:40:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8397c9f1-fafd-31e7-a011-d1866336e14d | -3.10846 | -54.04202 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb975faa-a645-3a4a-925d-c6ac3c690063 | -3.20149 | -51.25722 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 527068e4-d90c-3b6c-bb9e-c61748af0d72 | -3.58197 | -53.28244 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be20eb4a-a4ee-35a6-b533-523d64fbd9b0 | -4.02016 | -48.93639 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1451f06-61b5-389d-9cbd-c6fda477ae18 | -3.25136 | -53.63617 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 99465120-cff7-3954-b298-32ae4256151c | -4.88111 | -41.28432 | 2024-11-30 04:40:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 557a6a90-4e29-360d-9f7a-62a63e526b7f | -2.98419 | -53.28986 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 903ddfd4-bea8-34c8-b14b-cfd96b39e8a2 | -2.25179 | -46.45206 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0fb41f34-7936-3105-92a6-0b58a327ffd7 | -2.66706 | -46.60263 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bbf3b59e-4560-39d3-b304-93582aa56656 | -3.12483 | -46.0505 | 2024-11-30 04:40:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 531f5f5b-3684-30e7-999e-f8022b23c45a | -3.18205 | -54.33302 | 2024-11-30 04:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 044a7916-1b7a-3786-9bc0-9182c144ac1c | -0.24852 | -53.7622 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7acd99e0-9e12-319e-8698-fb170eab95e6 | -2.80196 | -51.58686 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5079404-49b0-36f4-aced-2a986a119ce3 | -1.75399 | -50.54913 | 2024-11-30 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 19fb1ed7-7709-3c38-a18e-62b0bd66f9d4 | -3.07507 | -51.09838 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a518ab6-d613-3ff5-84e8-f14accf43b18 | -3.99819 | -43.25368 | 2024-11-30 04:40:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| edda73f2-1d26-31b6-a41a-4a825a6574ba | -1.59782 | -51.26936 | 2024-11-30 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62a811ec-4236-33df-b24f-592dda11c7c1 | -3.61617 | -50.18855 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c8f2630e-0e3f-3c7d-894e-86f878354d7f | -3.94148 | -46.70425 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e82aba0-6b76-399e-9ad7-b416c51ca8d2 | -2.99777 | -53.36343 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f35e6183-1327-3c2a-918a-366281132480 | -3.70909 | -47.14828 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 885b1ea8-4d2a-304f-bbbd-2d8b60e838bb | -3.58242 | -46.34862 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07167572-b8d6-31ce-a4d9-c6f9b81f2093 | -3.01546 | -45.1029 | 2024-11-30 04:40:00 | NOAA-21 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 5662a89c-f93c-32ae-858e-d7c5c15d0749 | -3.22488 | -53.06595 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1187d850-d029-3c7f-ad5c-9142c743bca0 | -3.2594 | -53.6346 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 83d86689-a839-379e-89fb-5cdec4976d24 | -1.62964 | -53.86546 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 828aa5e1-8b6f-32ee-ac30-671e891fe55a | -2.37516 | -50.39783 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 30c07bda-a005-3ba1-9755-4cfbcb737b9f | -2.96091 | -50.57407 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 896d98f7-23f6-380e-b041-d9b243cc87b4 | -1.56787 | -45.64699 | 2024-11-30 04:40:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4152f39-0a71-345a-bbd7-826f440dbdec | -2.75689 | -54.12251 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8c8fd433-8777-389d-80f2-a4fdb4fb8e8b | -4.06424 | -46.68226 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3f11c2df-b51a-3514-8a2f-0aa2a19d6c78 | -3.33153 | -50.50186 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5196bd57-df03-3db6-aee3-1f4cccb6f538 | -4.18037 | -50.66329 | 2024-11-30 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e0e8f3d-5623-3395-9d3c-c21b1b82fe99 | -3.36414 | -50.51424 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22772021-4557-3b84-a122-403bd7029650 | -3.76058 | -49.94206 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 91c5d7d5-3858-3d5d-9b7f-a7327389cb97 | -3.88589 | -46.68413 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 387b280c-8824-3705-84f3-724cfdb7d8f5 | -3.84623 | -52.02011 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d41eeff-788e-347f-b525-916465bf9db4 | -1.71906 | -52.62712 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e42adac0-da11-316e-8817-35ceca099ebe | -1.5221 | -47.37434 | 2024-11-30 04:40:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 942fb4d2-8eb2-37d1-9518-f3c674982a98 | -4.07062 | -46.68728 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0d521dd-235f-3614-ad7c-7e9e22b5d303 | -3.64003 | -54.44676 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4e640263-7529-3403-ad3e-98e6c8b49e4e | -3.20903 | -50.27013 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 278676c8-fade-3216-8981-79c2325bf7d0 | -3.20438 | -48.58348 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09450aee-14ea-362e-9f99-a4a6f3b617c4 | -1.18393 | -51.77314 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d5ff5f85-edd3-3fa2-b43b-db5afc821a79 | -2.59473 | -48.19439 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2ada0be-a3a1-3344-91e2-4534165bd5a4 | -2.82926 | -54.08915 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 21daba47-6be6-3241-a10b-76319b096c10 | -3.67108 | -51.30156 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 691b3bcf-846e-3933-855b-355c220d9b52 | -3.42207 | -50.43142 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b69a9fc8-5dc6-3bd8-856f-0c6983c7799a | -3.70952 | -45.68365 | 2024-11-30 04:40:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 92674afc-4798-3435-bc17-2c06bc80b6e5 | -2.20441 | -45.58203 | 2024-11-30 04:40:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13e7038c-ef1e-36c7-b98b-8717287e5e44 | -1.32039 | -51.66934 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7528b8f0-e724-3610-9fe8-1e720522ae3e | -1.23075 | -51.80613 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a481c89-edb0-36f1-8b5c-f3ac3c6812d9 | -1.08302 | -53.39055 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e786bd6-3940-35dd-9a8c-722d05a23a39 | -3.39745 | -50.30341 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a45849ae-7ac8-3819-81ac-5b6b7a8a9f09 | -7.07922 | -39.648 | 2024-11-30 04:40:00 | NOAA-21 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 05f9e0b1-b538-3813-a563-5ae17c2ba5df | -1.1313 | -51.67657 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 99d94555-9762-3640-8593-3ee757978294 | -2.69019 | -46.28745 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6cd4859-940b-3719-8599-20a8ae5c2de0 | -2.26142 | -50.35411 | 2024-11-30 04:40:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e540b40-7457-3f8b-8bca-4c14d93872a1 | -1.70478 | -52.64372 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| cc14dfaa-e699-365f-932a-553b0dbd02d0 | -2.51529 | -48.46466 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd3713d7-877b-3205-ae4e-c2ccd4836f39 | -3.97867 | -48.1954 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4719e4aa-764c-3248-8e55-79645c4a6c5c | -2.3611 | -55.8723 | 2024-11-30 04:40:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 42ccf66b-5341-339d-ab28-bbdee25e7705 | -2.9891 | -53.35986 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9c681e7-e741-3eb6-be1c-b03c03f50cd9 | -2.66413 | -48.79777 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f5af9315-b67e-3b8e-aacf-72a157a6d46a | -2.31757 | -50.64722 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58ccead9-61c9-3e59-bca6-ad2d88d44936 | -2.72099 | -48.58501 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9dec52ac-5149-3225-a6bb-e0b272cadb03 | -4.61202 | -47.00235 | 2024-11-30 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bec991cf-9ccd-3fa2-be30-f713ded36a3a | -4.9098 | -49.90218 | 2024-11-30 04:40:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72ec122f-3f22-3031-9ee5-3199256f0de4 | -4.38418 | -47.25241 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d33fe740-3cbc-3f1d-b7c3-ba81ab95b6ae | -2.02803 | -52.07618 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c6e26424-5e27-398a-9c64-f7f6d8dbabfc | -3.21809 | -48.82155 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d988e68-38ff-3b16-99e5-a0581510150f | -4.14716 | -48.88549 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 76151a9d-9938-3a57-960f-0c5ea90b74af | -6.12623 | -44.91973 | 2024-11-30 04:40:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8278c4ef-d47b-313b-888b-76b52d03bfb1 | -2.73004 | -46.26159 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d3ee0d7-7a56-3585-aa96-d8014c757cd6 | -1.75174 | -52.76472 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README30.md)
