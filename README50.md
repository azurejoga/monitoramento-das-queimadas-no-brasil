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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 131d7e43-f630-35bf-a0d0-cb9d9f08af66 | -6.1927 | -50.89016 | 2024-10-14 04:19:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d273e051-76bd-3dc9-bdf1-68268d344a33 | -5.50243 | -50.52614 | 2024-10-14 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ff4292a-9f52-3313-8604-7afc141ede6b | -5.17089 | -50.11678 | 2024-10-14 04:19:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07c2412d-a00b-3ff6-9943-b3f6925b6168 | -6.21422 | -50.90121 | 2024-10-14 04:19:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e3ba6f4-36ed-36f8-a2b0-6e0486a5c9b1 | -6.21379 | -50.89798 | 2024-10-14 04:19:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57eed9c6-bc33-3a67-8b9a-a664f51fd357 | -6.21312 | -50.90203 | 2024-10-14 04:19:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fbf500a2-000b-3605-b998-45339bdb18b7 | -6.19777 | -50.88661 | 2024-10-14 04:19:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ff2b1fb-9021-3725-9a72-890cb73d4e12 | -3.34454 | -51.64274 | 2024-10-14 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8c1756ef-ebea-3b07-922d-262772466205 | -2.92852 | -51.84976 | 2024-10-14 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6451e79f-2fad-3bab-9833-b7cbbd75678e | -2.91054 | -51.93993 | 2024-10-14 04:19:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f75456fb-661a-3803-ad81-8a862af91be6 | -2.6509 | -51.88578 | 2024-10-14 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0c46b74d-b2dc-37d2-a465-06d1f43407f3 | -2.58537 | -51.8525 | 2024-10-14 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d12291c1-36f5-391a-b996-3b7a5be23e36 | -2.58443 | -51.85807 | 2024-10-14 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c68243e-d551-31e5-916a-ca4a271e4aab | -2.58337 | -51.85608 | 2024-10-14 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7a775268-dfae-384f-b0a9-b5d7012e874a | -2.5795 | -51.85721 | 2024-10-14 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6425f22a-b328-3c5b-8af1-0cf1d801db44 | -2.65586 | -51.8865 | 2024-10-14 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7d66318-9d49-30e8-b0d7-35dcfc684095 | -2.64997 | -51.89144 | 2024-10-14 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ea30be40-f3ed-386b-b7b4-b170d0ea3187 | -2.64594 | -51.88507 | 2024-10-14 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 291a004d-e0b8-3dde-a7b1-02d830484a79 | -2.63162 | -51.7575 | 2024-10-14 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41b7017c-d115-312f-990c-fbc50ce03a27 | -2.57754 | -51.86082 | 2024-10-14 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a7d3068-ca63-3daf-ad5e-16299f215638 | -3.07211 | -51.17855 | 2024-10-14 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6bcd943d-4349-3081-8e4c-59eeb68fdee2 | -3.07129 | -51.1835 | 2024-10-14 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 080758f7-20ce-3d64-8549-efe68b2af50e | -2.92644 | -51.8455 | 2024-10-14 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 33a3a423-5d01-3016-9a28-c11d01ee188b | -4.26771 | -50.96072 | 2024-10-14 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf5e498e-0ff6-37de-82d0-9a1d779503c1 | -4.26614 | -50.96115 | 2024-10-14 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e023f017-1f3f-345a-9828-89591eb45f87 | -4.26235 | -50.95587 | 2024-10-14 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e878184e-1f13-3fdb-bb03-089e39deb1d3 | -4.12413 | -51.11324 | 2024-10-14 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d957657f-53de-31b7-a002-af240321415a | -4.08892 | -51.12525 | 2024-10-14 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6160c74-118c-340e-af10-3e281d892410 | -4.07386 | -51.0742 | 2024-10-14 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11c748d6-55ca-3cdc-8f3c-ea18d6616a79 | -4.07309 | -51.07887 | 2024-10-14 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1253764-24b4-3fe6-a08e-6fd0ebc3ba51 | -4.06929 | -51.07345 | 2024-10-14 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8fde7de5-6ac5-3d03-90e1-523fd9fefe14 | -4.06851 | -51.07815 | 2024-10-14 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7ec4c61-d274-3926-8fa0-2822e1b39b62 | -4.63967 | -50.93232 | 2024-10-14 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0791e656-506c-3e8f-ba42-f310975265c1 | -4.64417 | -50.93296 | 2024-10-14 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43a7e792-b7ab-3061-b7c8-e487322d3b48 | -4.61345 | -50.95123 | 2024-10-14 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a8c4a6c6-4c3a-3740-856e-d4d84b46b202 | -4.26397 | -50.95546 | 2024-10-14 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a6122fb-f368-3fe3-bf97-2dbc4f397b5c | -4.12418 | -51.11092 | 2024-10-14 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f346e81-c835-358b-8bae-877cdae08e84 | -3.92023 | -51.23246 | 2024-10-14 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7cdc38a8-c8a7-327d-9b4b-c5399c3f0d3a | -3.86959 | -52.26727 | 2024-10-14 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8590021a-ff52-37bf-b506-fe35827f50fe | -3.83013 | -51.41062 | 2024-10-14 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a69b01f-5a9a-3817-a73d-4029d01a07ee | -3.80863 | -51.54159 | 2024-10-14 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be93996c-0e11-3245-acfc-e3d9d0a28e1f | -3.74894 | -51.33408 | 2024-10-14 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 146819ae-60dc-3f30-ba1d-432d6afd8d61 | -3.7128 | -51.79271 | 2024-10-14 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| adfbec40-5a26-30c1-9db1-9ca344a33ff3 | -3.55433 | -52.01947 | 2024-10-14 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f78595e4-51ea-3753-a33c-1a6a50c8942a | -3.93219 | -51.04887 | 2024-10-14 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a8439c1-c892-3339-a2e4-00eebbf9129a | -3.92103 | -51.22764 | 2024-10-14 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 116ee35b-6b4b-3a1f-90b3-f16e631c055b | -3.89578 | -51.91266 | 2024-10-14 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6141d4f5-a4fb-3dc2-afa9-db2e93158607 | -3.86912 | -52.2701 | 2024-10-14 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8f6f1af-5f27-3a92-8e5f-0b56befb06fb | -3.83096 | -51.40559 | 2024-10-14 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 560b11e7-314b-3702-a6e7-10c2935b2633 | -3.82544 | -51.40981 | 2024-10-14 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48764c1a-6343-3a4f-a640-8c7dc4b159b4 | -3.62274 | -52.01507 | 2024-10-14 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 615f83af-174b-3b59-8234-c2bf3ac98452 | -3.61783 | -52.01425 | 2024-10-14 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ea1ca45f-4ac0-3e71-8769-429d69ffcc0a | -6.40632 | -52.70835 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 17337a88-65f3-3c40-b2a5-7535e358d36d | -6.41123 | -52.70924 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90f0c0f1-5866-3a19-8b59-dcf8128c18f9 | -6.09223 | -51.21588 | 2024-10-14 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac631ab0-7652-33c8-bd5d-067cd6bc6430 | -6.05867 | -51.22411 | 2024-10-14 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e413ecb7-8b8a-38e7-888c-73bf9486698d | -1.93734 | -52.09691 | 2024-10-14 04:19:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90d75868-e1ac-3603-afa3-e19c0efe05dd | -1.93684 | -52.09994 | 2024-10-14 04:19:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 287cfe3b-af22-30c2-b394-1e5659faace7 | -1.93634 | -52.10296 | 2024-10-14 04:19:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2127d98d-ab5f-3071-b13c-3089e5442546 | -1.93176 | -52.09911 | 2024-10-14 04:19:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42fe67ae-ef9e-3e64-b7f2-7fd06b24139a | -1.35592 | -52.94329 | 2024-10-14 04:19:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37c2b68e-fe49-3a33-a3d5-938c3a311907 | -3.42864 | -52.77238 | 2024-10-14 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bd7b29a1-2c48-3b62-bcd6-e419c43f971f | -3.42812 | -52.77549 | 2024-10-14 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 24a0d949-658a-3483-9f23-92f2fb0fe74d | -3.10393 | -53.03368 | 2024-10-14 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01d5edd9-a7e2-3f64-b27b-f6567d363d0e | -3.1034 | -53.0369 | 2024-10-14 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e20b3f26-357d-339d-923c-412db9157bc7 | -3.10286 | -53.04014 | 2024-10-14 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12edf569-2728-3749-9420-5924d9088c75 | -3.10176 | -53.04672 | 2024-10-14 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c104741d-dc1d-3761-8e23-e39ed09b56c9 | -3.1012 | -53.0501 | 2024-10-14 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7df4dc30-9633-3c35-a52a-092edd87895b | -3.10063 | -53.0535 | 2024-10-14 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7d2818e5-0b80-3fc7-aee1-03f877de0aa1 | -3.09861 | -53.03286 | 2024-10-14 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a603a64-ec15-33b3-836d-48795388ed79 | -3.09807 | -53.03613 | 2024-10-14 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee4a7543-5180-3c76-82a5-e21c34566312 | -3.09752 | -53.03943 | 2024-10-14 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aefa91d5-fa4e-31b5-b2a8-8582077beb13 | -3.09697 | -53.04274 | 2024-10-14 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50924ad6-d97a-3a24-b2a9-5395e0cc9fa6 | -3.09641 | -53.04607 | 2024-10-14 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0164f6cd-5ea0-33fb-932d-dbc47b389a68 | -3.09585 | -53.04945 | 2024-10-14 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63e5a1b7-76fe-3322-b62f-f8a221a1336c | -3.09274 | -53.03538 | 2024-10-14 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fed18058-36c6-3189-8b62-0915b2a20e46 | -3.09219 | -53.03868 | 2024-10-14 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b87f190-53db-3ea9-94b1-aca2d3aca3f4 | -3.09162 | -53.04205 | 2024-10-14 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eca440bc-236c-3f4a-8981-82ee766a551d | -3.08741 | -53.03465 | 2024-10-14 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 960a420e-f8e0-3c52-b26e-2e8285603439 | -3.08686 | -53.03793 | 2024-10-14 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d018c5dc-86e6-30ba-aca7-1f5f7a94d554 | -3.08628 | -53.04133 | 2024-10-14 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| def3cfb7-6df7-3657-92c0-cd0b38d601cd | -2.86348 | -52.46887 | 2024-10-14 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f94c4522-3487-37a3-891d-350933fde80e | -3.00743 | -53.44414 | 2024-10-14 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 215f9574-add3-377c-bcc4-3674de969a7d | -3.00682 | -53.44775 | 2024-10-14 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1aba3a32-99f1-35f3-95d0-3b8ae091a60e | -2.66094 | -53.34926 | 2024-10-14 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 639df36b-8b9e-30cf-9332-9207a32b57b7 | -3.8712 | -52.2882 | 2024-10-14 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 55334d4d-b18a-3a48-acc7-25f34505c09a | -3.87025 | -52.29385 | 2024-10-14 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a50a6566-a210-3163-885f-27cf89e4aa96 | -3.87073 | -52.29102 | 2024-10-14 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c951a9d4-bb70-3f8b-83b8-eb2021df9be4 | -4.36538 | -53.66872 | 2024-10-14 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c562497a-ef2d-3296-97d8-88809c5cc16f | -4.35995 | -53.66784 | 2024-10-14 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19bdd4d0-9bd5-374a-acbc-adb1c87f6d1a | -4.17316 | -53.53285 | 2024-10-14 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 976bd897-17ec-397b-92b9-9700efeb8d5c | -5.99188 | -53.35086 | 2024-10-14 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17b1d98d-d8d9-305b-a284-b9ce341718da | -5.99705 | -53.35174 | 2024-10-14 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fe8f607-e457-3697-a3c1-3fdba114760a | -5.99652 | -53.35485 | 2024-10-14 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e401d38-d5c3-3630-ba13-2ee8779cd890 | -5.91575 | -53.29961 | 2024-10-14 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 80d975bf-d5a1-34b0-938f-c586b1e897d8 | -5.90898 | -53.30773 | 2024-10-14 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56f9745f-107f-3d20-9e7d-5fdfed82f523 | -1.69888 | -54.87354 | 2024-10-14 04:19:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31365abc-68d5-34ef-a8df-dbff3c3f780f | -1.42276 | -53.47023 | 2024-10-14 04:19:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0318c365-1b7e-3116-8509-1f6386d545a4 | -1.42214 | -53.47408 | 2024-10-14 04:19:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec00b6c2-ef8b-3ad0-a9c7-9d7d8c3106d4 | -3.62138 | -54.1315 | 2024-10-14 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README51.md)
