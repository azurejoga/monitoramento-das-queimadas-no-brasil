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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b60c1397-f3d8-30b3-8dad-9bae639ec022 | -3.70197 | -50.9411 | 2024-12-10 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0fa12aee-dd3b-3b3c-94a1-686d1e765ac4 | -2.98757 | -52.84808 | 2024-12-10 05:16:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84f2cffb-0dcd-3a2a-9b28-56ba09b9f245 | -4.01624 | -54.75163 | 2024-12-10 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5445b246-34c6-3bf7-b1f2-63e28b7c8e6f | -3.0068 | -48.04264 | 2024-12-10 05:16:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2049690a-4b65-3162-8ebd-bf287ae8ff1d | -3.47427 | -52.81644 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d63942f-15c0-3cab-8ee6-47953ccfe26d | -2.95545 | -53.11562 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b81e9871-732e-37e2-9499-b85e3245ed22 | -1.64552 | -54.618 | 2024-12-10 05:16:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5eabc93f-1b88-324f-8e0c-132dc55099a7 | -6.65784 | -54.93967 | 2024-12-10 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 50a4c087-e2e5-3ac7-809a-8b20fc94c504 | -3.71622 | -52.44201 | 2024-12-10 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30ce76e5-41f1-3cf3-94f9-5b9a8c4020e8 | -2.95928 | -53.72142 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7cb30f7-2c94-3849-bc28-4cf9495559d1 | -1.69433 | -55.67197 | 2024-12-10 05:16:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0d7adf8-b207-393d-a7f2-e23c89b007e4 | -4.68187 | -49.50157 | 2024-12-10 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| abaa2a71-df1d-343f-a318-3abb6b56ea7f | -2.94084 | -52.50364 | 2024-12-10 05:16:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b37c22a4-b274-31a1-acfb-f2cb6a0db908 | -3.12174 | -54.0462 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29698ce7-29c6-38b7-a06a-5457a79cd2c6 | -2.81959 | -52.97781 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| e268a454-f8ac-3913-b978-ceb9639bd82f | -3.52015 | -50.9834 | 2024-12-10 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66a38847-321e-3117-86a0-d36f41eb9dcc | -2.61921 | -48.06364 | 2024-12-10 05:16:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| daf5fe95-eb52-3e5f-8ea9-527b09e516d8 | -3.21071 | -46.812 | 2024-12-10 05:16:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 88c5614d-668c-3661-8891-08f037cf1e36 | -2.81808 | -53.04095 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41a78a11-b3e3-34bb-82e1-9c66c3d931ef | -2.03605 | -54.43589 | 2024-12-10 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c24629d0-f1f6-3f9f-ab79-44c2641b3227 | -2.03673 | -54.43153 | 2024-12-10 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fee1a871-e075-34d0-9db1-58fbb7cd94da | -8.13716 | -54.86201 | 2024-12-10 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18160cca-4040-3d82-8408-872f806ce1a5 | -2.78201 | -53.24468 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0c404827-6f8a-3cb2-8192-8a432d89c5c1 | -3.81403 | -51.07502 | 2024-12-10 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7a3eeb18-af26-3a98-8566-eee7d4376fea | -3.23404 | -52.8391 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d1a0739-2737-34fd-970d-d315b86312a7 | -2.76707 | -54.05508 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb707b0a-5841-3444-a7e3-8ccc597bb72b | -2.64904 | -54.29089 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2badfc9c-913e-333d-8d31-681e8d839224 | -3.59868 | -53.74433 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5522457c-ce5b-3648-be1d-84977d31858e | -8.44101 | -49.63046 | 2024-12-10 05:16:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d566b6b-942e-35f3-b962-246bae1cd7e4 | -2.6318 | -48.05751 | 2024-12-10 05:16:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6c37ba7a-ff8c-3640-a287-b9e2a098c4fb | -2.99471 | -52.85689 | 2024-12-10 05:16:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61831ae4-3150-3402-a887-7371dc9d1473 | -2.99477 | -53.02225 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d63aceea-8485-3b63-b9ba-1d4cdd8855c2 | -3.52427 | -54.59121 | 2024-12-10 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2376d28a-2f97-3a71-b45f-deb45f45dd83 | -2.92155 | -52.96318 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2dc42701-5d7b-39ac-a3cf-2640e04af477 | -2.62493 | -48.06448 | 2024-12-10 05:16:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e977c376-8ee4-3b5b-aead-97f4e8929c8b | -2.76495 | -54.05673 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b0155a0-35f6-3f30-a8ee-f346d9ae0207 | -4.03882 | -50.80523 | 2024-12-10 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 0f373f9e-93ef-3802-9069-f2900aef153c | -8.14076 | -54.86437 | 2024-12-10 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b5d2070-7cab-3015-95de-7c66a3cb92db | -3.08607 | -54.07431 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 27fe44cf-c905-381a-a970-67f4883014ee | -3.09013 | -53.21285 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2498661b-b554-3b52-9e75-55a05b95f355 | -3.07091 | -53.79976 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e248871e-1966-3fcf-9518-8e8e067bf92f | -3.92584 | -53.57995 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44936da5-7b45-3472-8c27-f0c8f0cd002a | -3.10539 | -53.24787 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb6fce69-d42d-3bfe-b826-0b4a81dcd25a | -2.3043 | -54.00268 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c52f13c5-8726-305f-99b8-3ce0af6560a8 | -2.95897 | -53.11985 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3de197ab-43d0-315a-825f-2a3c53d0d230 | -3.10484 | -53.2514 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 72c32b75-3fdd-3b27-8948-e462f08ace46 | -3.26928 | -53.6212 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 172a3e60-a086-3999-9ca7-32f89beac7e9 | -3.08991 | -54.0749 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 09af704f-43bc-3162-aa43-cdadaff105ee | -3.1794 | -55.01219 | 2024-12-10 05:16:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6f39a02-ebe4-3bfb-8180-91d48520175a | -3.53245 | -54.58787 | 2024-12-10 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac0ad4ef-0088-3db3-be24-edb55b3c1d20 | -3.3536 | -53.80675 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba2818ad-9772-32bd-ba10-a248e7f625a9 | -2.99124 | -53.01792 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d1897f6-ffef-306a-af76-d8b1c73a9c1c | -2.61332 | -54.24603 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c6620fe8-119f-3997-8507-58000fbf9d17 | -2.57959 | -58.0532 | 2024-12-10 05:16:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 065d9a09-457e-322b-99b2-338f2c6072d3 | -1.42757 | -60.07208 | 2024-12-10 05:16:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e38aa195-edf3-33f0-b722-17aaf3640164 | -3.94573 | -51.03922 | 2024-12-10 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3859cd6a-a6e9-3420-9045-05a897a4b938 | -3.06472 | -54.24266 | 2024-12-10 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77f43296-59a3-390a-88d4-e8149b5ebdca | -2.99639 | -52.84582 | 2024-12-10 05:16:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ef6eca9-c818-33a6-b4e7-c1d8b7f7fde8 | -3.20521 | -46.80609 | 2024-12-10 05:16:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea4a3991-cd44-37a4-b3a2-c88d59bd79ba | -3.79327 | -50.95198 | 2024-12-10 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0b3eecb-4fc4-3d8e-af37-f4eb71c1a6b4 | -7.79443 | -55.01937 | 2024-12-10 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b43b3ea-ca2e-322a-8a06-3e2896e92ef1 | -3.06491 | -54.24507 | 2024-12-10 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 067df7a7-99ae-3dac-b74e-2c75cfa01c4c | -3.06775 | -53.79428 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c85bb031-b6bb-33d0-a169-b01050c91eb4 | -5.91355 | -48.05494 | 2024-12-10 05:16:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 05663be0-f7a6-306a-a06d-4ee98ff9f796 | -4.54487 | -48.02296 | 2024-12-10 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ad7c0c8-d02f-3b75-b898-400974044bc3 | -2.61864 | -48.06129 | 2024-12-10 05:16:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09348e6a-8d98-3671-878d-32fbe0d5ed0b | -2.17049 | -53.65347 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d07ccd89-1054-332e-a6f6-9d4c5d94e10a | -3.78821 | -50.10674 | 2024-12-10 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29744914-a200-3623-a323-2033fdd89081 | -4.3821 | -47.75921 | 2024-12-10 05:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| a437cf3a-85a3-3775-bf11-5128496cfdaa | -3.10525 | -54.07729 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| afb5955a-4cb5-3210-a7d9-25afc4fb18ac | -4.67701 | -49.49733 | 2024-12-10 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c77a2273-bcee-362b-b939-9e7736af81a0 | -3.2084 | -46.8075 | 2024-12-10 05:16:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ba240dc-33ac-394b-969f-f4da96538331 | -4.55313 | -48.00706 | 2024-12-10 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d26c0036-0143-3693-99cf-687224ed3afe | -2.75721 | -54.15993 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6bd8edd7-dc3c-3bed-89dd-619141807f70 | -2.95951 | -53.11631 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 14f85abf-e13b-34ec-ad18-41a51da76a41 | -3.74514 | -52.42565 | 2024-12-10 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60b92e7c-bc43-35d3-a9db-c5c0b7d5eb0b | -3.92842 | -53.58326 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 31c3a2d8-c70a-3ae9-b679-a4f7cf8fafc9 | -3.57722 | -53.27846 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 247e7c38-bbc4-31de-bf4a-9d732427aebc | -2.79066 | -52.86552 | 2024-12-10 05:16:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fdd504d4-afc9-3f6f-b14d-bf85baa6077f | -4.38869 | -47.75583 | 2024-12-10 05:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 4e78a529-0784-3f32-a9d6-78e484632813 | -3.04142 | -54.24626 | 2024-12-10 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f7a0b555-05cc-344b-a6b5-5dff5ff5e755 | -3.62881 | -52.68261 | 2024-12-10 05:16:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 63e5c371-4435-342f-9110-5f9a2f6c9d25 | -4.03959 | -50.79993 | 2024-12-10 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1e82867e-f404-348a-bb7e-236b350126f5 | -3.10594 | -53.24434 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 201a2fb1-526e-308e-a844-5a730f1effc7 | -3.1851 | -54.33777 | 2024-12-10 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76330638-6f59-3fa8-b99a-ca0014999bbf | -3.16073 | -51.47693 | 2024-12-10 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f6faf5a-8016-3b8a-91df-946abe017bde | -2.81471 | -53.06244 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2095d62a-ce68-317a-a176-7749f41994d3 | -3.46312 | -52.72089 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e903844-25c6-3c78-8f5e-b795a65f1470 | -3.08959 | -53.21633 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c7594f1-2616-3a8a-9cd0-29101f2d2713 | -8.13685 | -54.86378 | 2024-12-10 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ca877e3-cf09-3028-a902-03acb8664fab | -1.49815 | -53.42775 | 2024-12-10 05:16:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f354f749-3a3d-3856-aac5-5b1ae501c883 | -3.04902 | -54.24733 | 2024-12-10 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1cc8bf9a-6204-3e1f-950d-a417d62bf232 | -4.63415 | -49.49129 | 2024-12-10 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 149200b6-72e0-326c-83a8-7de0f534232e | -3.57357 | -53.0225 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8133b335-2f28-3b9e-aafa-5fb6578aacf9 | -3.61166 | -53.49424 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8d8bfb0-5a8f-358b-ba84-fa8932774497 | -3.60944 | -54.30853 | 2024-12-10 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ff651a4-5078-3d7b-880e-0e2cec5a2515 | -2.37457 | -53.86303 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 20702272-69ff-323c-a6da-5e138b8d1dcc | -3.08983 | -53.3523 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6c2564f-0f58-3bae-8570-467649e6b005 | -3.66314 | -51.30074 | 2024-12-10 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d74452b-35e6-38d6-bd5a-923ccca6220f | -3.00106 | -48.04172 | 2024-12-10 05:16:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README35.md)
