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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 749860be-afa4-3043-9a12-2acf6805a49d | -3.91399 | -46.46228 | 2024-09-30 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8da56187-e63d-3385-ae85-f6ca89fd67e3 | -3.91345 | -46.46574 | 2024-09-30 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 766306da-c7e3-3a0a-896a-398e0d2ae5a8 | -5.72926 | -46.60381 | 2024-09-30 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e2ae3c9-512a-3b9d-a2dc-3519c049b5a1 | -5.72592 | -46.60329 | 2024-09-30 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5e921dbf-a12d-3687-8f21-6b35c5f37fa6 | -5.68834 | -46.69097 | 2024-09-30 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a0c19f2-99f1-3fac-aeb5-325b7caf1bc5 | -6.02559 | -47.4443 | 2024-09-30 04:29:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd2a6ffa-6dfc-3714-828b-78f061ed9bf7 | -6.02228 | -47.44378 | 2024-09-30 04:29:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 822bf4f2-3327-30bf-8805-ddb04c3d18ad | -5.98294 | -47.19677 | 2024-09-30 04:29:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2f504984-a8a2-3770-9e8f-527745930e13 | -5.96998 | -47.27986 | 2024-09-30 04:29:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53493576-5a8d-3c47-a038-1b77155ba6fe | -5.68501 | -46.69046 | 2024-09-30 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16d88eae-533c-3222-a2d4-df18747b4b94 | -5.3328 | -47.8974 | 2024-09-30 04:29:00 | NOAA-20 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d8452d21-446d-3ee1-af3a-5180e9d247f2 | -5.32949 | -47.89688 | 2024-09-30 04:29:00 | NOAA-20 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 89da08e7-7db6-3b59-a8ba-e011dd3d26b9 | -5.32894 | -47.90034 | 2024-09-30 04:29:00 | NOAA-20 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 76622b85-c9f3-3b21-a479-70d12d986c74 | -5.32232 | -47.8993 | 2024-09-30 04:29:00 | NOAA-20 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 65b0ceaf-f809-3132-b504-4d9ace6ad8e3 | -5.31956 | -47.89532 | 2024-09-30 04:29:00 | NOAA-20 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f355ace7-cc48-3012-a547-0a6ca2e14a11 | -5.31901 | -47.89878 | 2024-09-30 04:29:00 | NOAA-20 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 044592cd-b986-33db-b9de-47c0dd6b1334 | -7.14305 | -47.57402 | 2024-09-30 04:29:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cdc89662-b655-39a5-9931-f5bd98c56b2f | -7.09844 | -48.05283 | 2024-09-30 04:29:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c9beb582-fa3c-36db-b2b6-b52d6d31f2c4 | -6.97748 | -47.63291 | 2024-09-30 04:29:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6e17f08-c306-3db8-bf02-46cd6314c4b9 | -6.97585 | -47.64328 | 2024-09-30 04:29:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f03b2071-1b79-31a2-ae7c-8eea891d62f2 | -6.97362 | -47.63585 | 2024-09-30 04:29:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9fd7a208-f23c-3a8b-9e26-78f14a132a75 | -6.97308 | -47.63931 | 2024-09-30 04:29:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e524198-9fad-3cd1-b9a3-aeb9301ba3e7 | -1.97665 | -48.6901 | 2024-09-30 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3c8861aa-c299-36f5-99c0-3ac7c9a7001a | -1.97607 | -48.69381 | 2024-09-30 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8e054a6e-3ab4-30f3-b9ac-a3f2dd9b88f1 | -1.97323 | -48.68956 | 2024-09-30 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 59c49cda-7704-3f9e-8c83-5afba76c9a1b | -1.97264 | -48.69327 | 2024-09-30 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 702ac418-b5f7-37d8-8bb9-ba9906431efc | -2.1686 | -47.94736 | 2024-09-30 04:29:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00fa1b10-13ab-320b-b2ba-89e6d4f79dda | -2.02478 | -47.65505 | 2024-09-30 04:29:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4bdb0b8-9897-3b58-8a40-3cf7f168a0ad | -1.41844 | -47.40681 | 2024-09-30 04:29:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 369b7e4a-5b24-3162-adb2-813d9d6d666f | -1.2498 | -47.74306 | 2024-09-30 04:29:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b3974ae-6a2b-3fd6-8600-380cd80882c8 | -3.45229 | -48.82641 | 2024-09-30 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 472485fd-ea3e-328c-9b43-7267a88e605c | -3.22512 | -48.9311 | 2024-09-30 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0e1a5d93-11b2-3813-8f70-fa3e5dde0273 | -3.2217 | -48.93055 | 2024-09-30 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4ab5b970-0a1a-3737-88c5-4e891468be89 | -2.91945 | -48.89154 | 2024-09-30 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5a2a3cb6-dcc9-3a3f-a190-8cf533b51837 | -2.91388 | -48.30637 | 2024-09-30 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| adaa9d7e-6544-35f1-b98b-4a30b7567979 | -2.73692 | -48.69408 | 2024-09-30 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2ea77b3-8d33-3136-ab8b-b41446cfde36 | -2.64953 | -48.25463 | 2024-09-30 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a2b6e0a7-fdf7-31e2-a12b-00dfe80d3f47 | -2.64778 | -48.25455 | 2024-09-30 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f9aed80-9fca-3d52-9677-e2ba196f9cb6 | -2.64105 | -48.25351 | 2024-09-30 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 656bee5c-ed72-3b7b-81e8-85c7f6dacd6e | -2.41757 | -48.45405 | 2024-09-30 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0abb6b86-280f-358f-8540-cee3c137a96c | -2.20553 | -48.8397 | 2024-09-30 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60fedc4f-b5f4-3b38-9637-2c1272cd19d3 | -3.46717 | -47.66392 | 2024-09-30 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ea5687f-407f-3efd-a057-8c19fe4f6525 | -3.46662 | -47.66737 | 2024-09-30 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ae906d36-952c-366f-a0cd-2188c11ca4e7 | -3.04485 | -47.47672 | 2024-09-30 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7624273-b199-3951-80b1-8bbb848b281d | -2.99099 | -48.07873 | 2024-09-30 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bc9524b0-abc2-3c20-af7e-fe7d53e7cf52 | -2.90525 | -47.88971 | 2024-09-30 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b373c36-31cb-3fb2-8a40-7ceb400e1f73 | -2.90192 | -47.88918 | 2024-09-30 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9050723-7e09-3757-8aa5-ab381489eb86 | -2.89415 | -47.89512 | 2024-09-30 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c540197-e7da-3471-b674-e25d0f77c5b5 | -2.88969 | -47.88009 | 2024-09-30 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7518dda-f881-3da6-8ba6-1c65c04549fd | -2.88636 | -47.87957 | 2024-09-30 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54157e39-252b-3159-8c8a-adb4ec06ea84 | -2.87417 | -47.91354 | 2024-09-30 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 212284cf-467a-3031-a490-a58981bb56e6 | -2.51212 | -47.58133 | 2024-09-30 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b99f7b3a-de8b-32e7-8faa-34c0e91cc23c | -2.51157 | -47.5848 | 2024-09-30 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98302fe5-ba6c-382a-9313-7ec59ada03ff | -2.47849 | -48.04951 | 2024-09-30 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33153963-56fb-3abb-b719-1045687b9f45 | -2.35833 | -47.99855 | 2024-09-30 04:29:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5c68536-f2e4-3b59-b603-5b49939c592f | -2.35504 | -47.60686 | 2024-09-30 04:29:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| af39f909-1603-3a4a-afc7-0ea32994c538 | -2.35449 | -47.61034 | 2024-09-30 04:29:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 53e88ed8-f335-32ff-8ce2-764171223350 | -4.95522 | -49.25161 | 2024-09-30 04:29:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f7ac7f9-66ee-3b3a-aa9b-562b1b78266f | -4.95464 | -49.25529 | 2024-09-30 04:29:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0df4612c-f97e-3894-9a15-1bf3db22da49 | -4.76926 | -48.90121 | 2024-09-30 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cba7a5f0-6bd5-3774-b7fd-d9f84f7df1a2 | -4.76588 | -48.90068 | 2024-09-30 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 34f2bd29-b978-3b6b-91d4-d07c13875167 | -4.73351 | -48.84346 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e06c5794-2ce8-3673-a114-200e6297567f | -4.73013 | -48.84294 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c623213-f451-380b-b913-f542c830cfdc | -4.7287 | -48.84299 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 240cd328-453a-3733-9663-937c5458ec5b | -4.72532 | -48.84249 | 2024-09-30 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74bed03a-7239-3fa4-9c94-ef0cc288e7dd | -4.72475 | -48.84611 | 2024-09-30 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 039a1be7-211f-3dba-b2ad-fa7343efeecf | -4.72137 | -48.84562 | 2024-09-30 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09dbbdba-b88c-351a-bb15-3c3d9470cb70 | -4.36104 | -49.10703 | 2024-09-30 04:29:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3593032-c59e-327e-ba7c-28a90ab4f429 | -4.11699 | -49.09897 | 2024-09-30 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab6d8da1-73c7-3868-a4b2-e89c135876a6 | -4.11475 | -49.09101 | 2024-09-30 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a37d41b0-441e-3601-8d0f-7c6231760115 | -4.11358 | -49.09842 | 2024-09-30 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 379434cd-c8b6-35b5-8e84-9518f95645ff | -3.72562 | -48.86913 | 2024-09-30 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 523df562-4ec1-371f-88f3-e8d510ae0970 | -4.19244 | -47.93407 | 2024-09-30 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f91e229-3596-3a0a-a3cb-91b7c93a50bc | -4.18912 | -47.93356 | 2024-09-30 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ca2365c-989c-3444-87b6-73d7f6e3d758 | -4.18857 | -47.93702 | 2024-09-30 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54f9d96b-5e37-31fd-8bfb-9c4c878db7be | -4.18525 | -47.93651 | 2024-09-30 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c7135c2-ece5-3117-8c87-1a8f99e18453 | -4.91987 | -48.61702 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db271133-dad1-38b6-80ec-9c211e02cf9b | -4.9193 | -48.62057 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5b78438-d9e7-3426-8297-b9f708be2526 | -4.91765 | -48.60939 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 08c1d242-a56a-3e07-8526-f9aeb3829973 | -4.91708 | -48.61293 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8eef9286-de51-3885-81a6-d8b4864e5827 | -4.91652 | -48.61649 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd8872ee-5182-39b8-a134-471b201c4444 | -4.91595 | -48.62004 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 931b1f30-f933-3967-a4f4-ada828052225 | -4.91539 | -48.62359 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7d66b41-e9bf-3c81-9660-82fb7ec55e62 | -4.9143 | -48.60885 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aba5b077-adee-300e-9eef-70bde4c236cb | -4.91317 | -48.61595 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ae9d0a03-4d96-3c13-95fb-bc778cde1c25 | -4.9126 | -48.6195 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c97f5fe3-f310-3f27-8bf1-8ffe165b02dc | -4.91204 | -48.62305 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1bbdc99-98da-3820-99a0-440625f01c41 | -4.63467 | -48.53164 | 2024-09-30 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c33a06e5-7096-387e-9246-28c4f12c5b99 | -4.63411 | -48.5352 | 2024-09-30 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 934eefea-ab23-3cc9-b091-6c19a5db6968 | -4.63132 | -48.53111 | 2024-09-30 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 25323582-dc4f-3854-a530-67891453179c | -4.63076 | -48.53467 | 2024-09-30 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 218db00b-4872-357a-a204-6537a645e71f | -4.49024 | -48.11306 | 2024-09-30 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6456e8d5-7a75-39ca-be82-f92087437db3 | -4.48969 | -48.11655 | 2024-09-30 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 310d67c1-3062-3c19-a433-11d397db0157 | -4.41283 | -48.6468 | 2024-09-30 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa6431e4-da3b-32c8-ad9d-6e0271e7b977 | -4.40501 | -48.63087 | 2024-09-30 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf1ba285-e19e-39a9-8465-6c8649323b97 | -4.40387 | -48.63803 | 2024-09-30 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 22d60932-08e6-3d92-b851-31ee09dbd36a | -4.4033 | -48.64164 | 2024-09-30 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d73d72a5-4495-3908-9eb5-e1e497d5705a | -4.40108 | -48.63393 | 2024-09-30 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d02d408f-ddfe-3347-aed2-00940a7c6f1e | -4.40051 | -48.63752 | 2024-09-30 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79e69530-6f29-3dec-989e-14cdaf973e88 | -4.39994 | -48.64112 | 2024-09-30 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README29.md)
