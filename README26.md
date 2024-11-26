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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 241fcce3-62c3-3413-8df5-eeb930a2f5a9 | -8.26465 | -49.54545 | 2024-11-26 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8831a91-f1b2-393e-bbcd-c98e5774f35e | -1.56965 | -52.01411 | 2024-11-26 04:38:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5b396b67-26de-3f3e-956e-f1124adf6618 | -3.93589 | -48.15446 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d97da15-0121-30e5-a060-f62623966599 | -3.72509 | -50.19041 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f5150ce-9129-378d-a764-e1686c97acef | -3.78354 | -49.36059 | 2024-11-26 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0f4a270-3ae4-39d6-bea5-140c92aad0f9 | -3.17723 | -48.44062 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6ab5a540-d6ab-3ef6-bfe1-e35c2f87d047 | -6.11041 | -46.92686 | 2024-11-26 04:38:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dffbd207-bc89-3df4-b572-1b3d9a674964 | -2.78946 | -53.0068 | 2024-11-26 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac12c5a0-81d7-3ce2-9ee9-2b13590dc7e5 | -3.07677 | -49.50399 | 2024-11-26 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9314345-044b-3534-8bad-d1d5a7eb7596 | -4.41217 | -50.82985 | 2024-11-26 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dda56f61-9328-3524-9318-6a79df843859 | -3.32398 | -50.05482 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 371313a8-f2c6-3de6-b258-fa9106f07e0a | -3.97948 | -48.07206 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 9813bb36-6822-3d85-b112-19be88556dee | -4.16305 | -44.06894 | 2024-11-26 04:38:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b47182a-c1b5-3e2e-a16f-05e542bca961 | -6.18733 | -43.41463 | 2024-11-26 04:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 69f84ad6-c284-35dd-8568-ee793bb6b681 | -3.81018 | -46.60224 | 2024-11-26 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2853f354-0037-3651-8629-afede45a31df | -2.40293 | -53.6829 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c7675436-5c2b-313c-9713-c043c12da7da | -3.057 | -53.28109 | 2024-11-26 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| dbf65722-fd49-3338-aac0-ec0c62ebd7e0 | -4.29939 | -48.23252 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58d136a3-aeea-3fe8-b7f6-74a4abaea794 | -3.27546 | -50.64349 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 162ee5c8-85a5-306d-b8b5-9281be89900d | -5.67511 | -46.49669 | 2024-11-26 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2cd71c8f-3b22-30ec-9466-b64f75e38413 | -5.94735 | -43.79404 | 2024-11-26 04:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d5b077b-804e-38c9-ba62-3eead87f0584 | -8.2652 | -49.54196 | 2024-11-26 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b43f3af6-816d-3a47-b3c4-22d727744f2b | -2.59732 | -46.26065 | 2024-11-26 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac6649f6-c519-38d1-8d24-e374b7566899 | -3.23229 | -53.92249 | 2024-11-26 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 150e2912-970e-31b8-866b-975e59b4e3c2 | -3.17445 | -48.43665 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1acd05d3-9866-35eb-8c94-ad6cad684ed3 | -3.28867 | -50.27534 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ce067172-c78c-323b-8b01-b8280e2c3660 | -3.17832 | -48.43371 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42ebe748-34c9-33f5-a42e-90f30c17d468 | -4.17814 | -48.78819 | 2024-11-26 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b53f3ba-ed98-30e2-b9c6-594d1ca00387 | -3.99129 | -48.32315 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45be2c2b-879e-3efc-ac12-4f70d3d95b31 | -3.38705 | -50.09428 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e781fc5-2ee5-3e2a-b042-d6e841251d8d | -4.72162 | -46.48836 | 2024-11-26 04:38:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e7f5b66-2914-3de8-9323-dc5c4c0957fe | -3.07513 | -49.19621 | 2024-11-26 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b510c220-ea60-32b5-b647-8d54af62a870 | -3.44351 | -50.00729 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59712e16-d5c4-35e1-937a-4449871ecf04 | -3.33143 | -53.71643 | 2024-11-26 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42255dea-943c-3bf8-a446-6ea40d124ed8 | -3.45757 | -50.00586 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fe5d4ce-91b8-3ee4-afbb-090bac6bfd8b | -4.65576 | -47.94374 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9962c2e7-1453-31df-b09b-2c919a6e164a | -4.77658 | -47.83911 | 2024-11-26 04:38:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bac4144f-e7d2-35d4-960a-26bf53157a91 | -3.54689 | -50.18887 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a4e0b30-6421-3205-9221-2261052fde13 | -3.91117 | -42.41698 | 2024-11-26 04:38:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| f372e575-4306-3a5d-8250-f6062889c18b | -4.32148 | -47.53228 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8638a64c-9529-30e5-8ab8-67bb43d0d2e5 | -3.98501 | -48.05856 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 3589bb71-eec2-3f4a-a530-b6ba0674a170 | -2.93721 | -48.82666 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99ab306b-d70d-377c-805d-7282b0279345 | -3.24656 | -50.66962 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 79c63b8f-117b-320d-b110-0067f4aea4c7 | -4.41277 | -50.82614 | 2024-11-26 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a8a40b70-9821-310a-b6e7-5714bb568291 | -3.29453 | -50.36969 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a06223fa-340f-3c60-bf10-3991efc78ba8 | -3.68378 | -50.22865 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 401462dc-0223-375f-97d5-ba9f1a54420c | -3.96057 | -48.06193 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65dd7dcb-0718-393a-ab10-9313f18c8d2e | -3.17777 | -48.43716 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4b90f72a-8b96-319a-a1f9-c46d7b3000da | -3.44237 | -50.01445 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b4d2668-02d0-333d-b72a-d806d6d9aea4 | -3.98282 | -48.07256 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| fb00e399-68af-35fa-8a45-9c3d93f51466 | -3.08626 | -49.21219 | 2024-11-26 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8dd0036c-9250-3b20-92a2-6411cbba7cc4 | -3.29207 | -50.27586 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 488dc794-d76d-34af-8eb2-af7873952255 | -4.05408 | -48.3079 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 237c83fb-e6e8-3f3e-9323-a8ee35894bb6 | -3.8079 | -51.2637 | 2024-11-26 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bde154d-da40-396c-a92c-acba8c22a116 | -1.72475 | -53.24887 | 2024-11-26 04:38:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d4fcd8f-4f0e-3565-9f92-9212018e8638 | -3.32679 | -50.05893 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e956be0d-a073-33e1-8e8a-98702d991fcb | -1.63713 | -53.30349 | 2024-11-26 04:38:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 61c4dd1a-0d9b-3d4b-bfc0-8e7e2fd376e0 | -4.43851 | -48.55257 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe444633-9d78-3bd1-a42f-57920a17c7b8 | -1.47047 | -52.29735 | 2024-11-26 04:38:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 296ca092-e8f7-3a82-a4ff-61f4126c6e83 | -4.02978 | -45.54219 | 2024-11-26 04:38:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c24d06d-1cc0-3997-b2f1-73d8775ae032 | -3.06858 | -50.94922 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f6b06bf-a3a9-3829-9a59-bd6ee4b3ea27 | -3.18038 | -48.57183 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1fb2c8b6-42e5-37eb-87e4-c210eca9f2e1 | -2.77284 | -48.58205 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12544322-8a83-37a3-9d27-ef17159d3f10 | -1.4674 | -52.2921 | 2024-11-26 04:38:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a740cf37-4835-329c-98a4-571350646802 | -3.94848 | -47.99214 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36d04ad2-f13e-3b8f-8f20-d42a69aef5e1 | -3.23308 | -51.61155 | 2024-11-26 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 132d9d5d-c34d-3774-8558-880677663641 | -3.97676 | -48.0895 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| acb45c79-9c7e-3de8-8774-4363cdd9c97c | -3.93806 | -48.14054 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6563f0f-eeab-3a8a-b940-0a288fae6b64 | -8.04925 | -47.08231 | 2024-11-26 04:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24f927c0-5328-3c72-9384-a35b24529047 | -2.98868 | -49.59103 | 2024-11-26 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ef89ab9-56ab-3344-b2c4-f643451219e4 | -3.97894 | -48.07555 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 177baf11-8eaa-3f34-b181-f8641f8a05c3 | -3.93698 | -48.14751 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80b73656-8417-312d-9610-143c55467bb3 | -3.7314 | -49.94974 | 2024-11-26 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a6153cdc-b664-3f06-bc17-b41af83d9ac9 | -3.25325 | -50.41206 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc8e5e65-ae24-37f2-97d4-e2ef8becc1c9 | -3.16624 | -51.10301 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c86d96e-93c6-3e9a-a544-5497e56d6910 | -2.88665 | -48.73746 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 56576ad4-2b60-3639-89f7-35e5ad3708ac | -4.27775 | -48.60907 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c7828e2-c42a-33ba-9b63-aab2be53df41 | -3.48177 | -50.44338 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 599a297d-1342-39e4-8e08-02910c09599a | -2.82275 | -51.79644 | 2024-11-26 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0eb1040e-fdb4-3d9d-ab66-735cfe619dce | -3.05916 | -50.24745 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca3ca7c8-7355-3f9e-94ac-f8e98b3739d5 | -2.98589 | -49.58698 | 2024-11-26 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81946d59-080f-3c21-817a-53a69e48ea2a | -3.98058 | -48.06505 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 1eaf87b9-4a6e-38e5-b3ab-e06a5f04a54c | -3.98949 | -48.07356 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c8cbfdc-fa04-3f1f-9fd1-185240d4910c | -3.16975 | -51.10356 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e701a020-cacc-385c-91eb-3b22e0c8debb | -3.01676 | -48.03979 | 2024-11-26 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 27e49546-5540-3452-bb8e-6ec2ebb160c2 | -3.3893 | -50.10198 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a67529be-3dfa-346e-9fe6-4cc3bee6ad6b | -2.70081 | -51.99817 | 2024-11-26 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ca9cd39a-78a2-30fa-a9c8-64ab27dc6da7 | -3.23338 | -53.93092 | 2024-11-26 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35cea7a8-dd27-3dc2-aa2d-9ae7171ffddd | -2.15968 | -53.77706 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b36dc514-2ab4-33f7-a6e7-44f619adb13c | -2.92605 | -48.34109 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2397cdef-06c9-31a4-b681-14e6cb780b7e | -3.69113 | -50.22614 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e1034b9-6cb7-38eb-8776-15a67f4fce4b | -3.5886 | -50.38852 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b365a587-4ea8-3c04-bf37-9f679ac40fe8 | -4.86953 | -38.38613 | 2024-11-26 04:38:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| aaf039ab-220a-3aff-85b4-e08967af9f4f | -4.31585 | -47.52407 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6523f51c-dec4-36d3-8569-0585c0b0dc93 | -2.88997 | -48.73798 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99ce552f-73c7-36b7-a867-f6f125ed2362 | -3.34915 | -49.21761 | 2024-11-26 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5cde1a26-0022-31cf-b6f2-87c9dd7f8017 | -2.0555 | -53.23454 | 2024-11-26 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e6e5392-e3ea-3f42-be9c-3296d52c2b7c | -4.65801 | -47.9513 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 63cddb18-8983-3b84-b3ed-6c7bbaf0e36d | -3.06283 | -53.22013 | 2024-11-26 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a84b75d-da9b-35a4-8c53-0c79ecc510f8 | -5.75785 | -46.25684 | 2024-11-26 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README27.md)
