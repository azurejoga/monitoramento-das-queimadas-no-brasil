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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d5b4120-6ab0-34f0-bdb0-11e5a61bf4d6 | -3.60623 | -47.26653 | 2024-10-27 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| adda41bd-d5bd-3903-852c-13ad0ae6ebff | -3.60459 | -47.25517 | 2024-10-27 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fefc3d10-460a-371d-b05f-0503c50b9514 | -3.60327 | -47.2549 | 2024-10-27 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b42c2fb1-e786-3848-9d75-b1887f54afa9 | -3.59704 | -47.27241 | 2024-10-27 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2211f287-9f18-3347-b883-9556a1c1dee2 | -3.59647 | -47.27606 | 2024-10-27 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 23bff71b-f86f-372d-92cb-dc64638887d5 | -3.59366 | -47.27185 | 2024-10-27 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 075314e7-6ee7-3753-b2a5-ffd6f3f2271f | -3.59309 | -47.2755 | 2024-10-27 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8b32072-a285-3eae-9d5e-c21c5f9205c1 | -3.59141 | -47.26414 | 2024-10-27 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 837f3a53-160a-3fc5-9ae9-8a7e77c97add | -3.59028 | -47.27131 | 2024-10-27 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86a4bf31-005a-3d1d-8c35-b27b2ef3a8cd | -4.93263 | -47.39289 | 2024-10-27 04:23:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d44427f-35ae-3d94-8bf5-0d02b28187b2 | -4.89523 | -47.47547 | 2024-10-27 04:23:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a055aead-4fd2-3074-b6b5-bdd2561c3035 | -5.36523 | -47.69046 | 2024-10-27 04:23:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd3d027c-31af-3d8f-9c42-3f2f45990514 | -5.74881 | -46.51113 | 2024-10-27 04:23:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3a0ea77-b4dc-3ed3-bde5-87c92111de3f | -5.63851 | -46.69249 | 2024-10-27 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fce73bb6-61e3-3092-bfe1-fc2e65b096bb | -5.55022 | -46.99278 | 2024-10-27 04:23:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 64d93b34-474f-30ed-8784-0891e873f823 | -5.54966 | -46.99627 | 2024-10-27 04:23:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 433b1083-e714-3fae-9fbb-0e2594603dc2 | -5.54689 | -46.99224 | 2024-10-27 04:23:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f12b4d4e-02b4-3305-bf09-37ba9c94e72f | -5.54634 | -46.99575 | 2024-10-27 04:23:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 379974ff-efdd-309a-a85b-4f8d07253bc2 | -5.54356 | -46.99173 | 2024-10-27 04:23:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| dfdb8306-8dc8-348c-9e9f-ca6c32fa8af7 | -5.54301 | -46.99522 | 2024-10-27 04:23:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 13a35ab0-ced5-312a-a46e-ca06b394c372 | -5.34364 | -46.79524 | 2024-10-27 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0c086bb9-1f10-3473-ba36-9433d44bdc2f | -5.34308 | -46.79873 | 2024-10-27 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| d517a513-c035-396c-94f6-6fa9e9bfb2d4 | -5.20391 | -47.86725 | 2024-10-27 04:23:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1adba62c-f763-30d0-9265-f5db3254bd82 | -6.70362 | -47.64272 | 2024-10-27 04:23:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cbfcef1-0406-3a08-8274-aa49b5f4bb83 | -2.17285 | -47.948 | 2024-10-27 04:23:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a57de10-0a2a-3f22-9668-d9af2e6fe6f9 | -2.17223 | -47.95193 | 2024-10-27 04:23:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5389a0d5-a04b-30c0-8177-c2294d21affa | -2.16872 | -47.95138 | 2024-10-27 04:23:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0c48aaf6-e033-3e96-aa2c-f40a2fd1352c | -2.09766 | -48.55238 | 2024-10-27 04:23:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5c342c2b-f357-3690-807d-fe7c0bd02e7f | -2.09698 | -48.55657 | 2024-10-27 04:23:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 311214c3-7af7-3b7a-9fdf-45b50ce48b37 | -2.05018 | -48.61125 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c7298811-7b33-35f0-ae56-94a2b7d3bb8f | -2.04654 | -48.61068 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d3ae3ac-9f01-36e1-b320-69b475bc69c9 | -2.01707 | -48.51571 | 2024-10-27 04:23:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f42a4f2e-6ae1-3f35-93dd-70c3f222815d | -1.9704 | -48.68983 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c9fb9c6-b81d-3b4e-9dd9-c34d23f852bb | -1.96675 | -48.68925 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ada973a-b1cd-39d0-b214-752494e4370c | -1.96656 | -48.6909 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 315a96ce-ea9f-3a4b-ad3f-55dd96c40da3 | -1.9544 | -47.88684 | 2024-10-27 04:23:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ff0cacd1-ac1b-342a-8236-af86470172cb | -1.78976 | -48.43955 | 2024-10-27 04:23:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6bd31e8-9a00-37f6-8121-67c539816bf7 | -1.78905 | -48.43666 | 2024-10-27 04:23:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b29f8ea-6ed9-32c5-838a-45d33829d3a0 | -1.78841 | -48.44083 | 2024-10-27 04:23:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f98fe99c-5ac4-3e0d-9bb5-6d9dfce51131 | -1.78682 | -48.43483 | 2024-10-27 04:23:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4871af6c-c41a-3bbf-934d-1e09da73220a | -1.78615 | -48.43898 | 2024-10-27 04:23:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 792b0049-b939-398e-816a-537116ead43c | -1.31177 | -48.42718 | 2024-10-27 04:23:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a0930d9-70c7-3689-94c0-89d554bf016a | -1.12741 | -48.38428 | 2024-10-27 04:23:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2806f023-8f3b-3049-98ba-ea11efc29d2f | -1.5287 | -47.20601 | 2024-10-27 04:23:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6bc6bb2b-e73c-336a-bc03-4b6df63b680d | -1.52812 | -47.20972 | 2024-10-27 04:23:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08b89644-0b2e-33d0-b7a4-1e2bfdd60579 | -2.92003 | -48.95798 | 2024-10-27 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2da5013-1c1e-386f-9838-8418dadf62f3 | -2.89229 | -48.27796 | 2024-10-27 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31725e4e-f167-3dfe-bd96-910acac3bf19 | -2.89195 | -47.84948 | 2024-10-27 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e699b9a-0e99-316d-8f13-cfb209eac26b | -2.89041 | -48.28992 | 2024-10-27 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2186cadf-a9e0-3ee7-972d-fea109a672cd | -2.87475 | -48.61092 | 2024-10-27 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b1b5de6-2492-3558-a3b9-540f69ec4ac8 | -2.80428 | -48.6734 | 2024-10-27 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f3136d5-ca40-3c4b-a39a-30192023d9a8 | -2.78763 | -48.09161 | 2024-10-27 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24952e82-6ddf-3c89-9095-5c2e96099b0d | -3.46142 | -47.66521 | 2024-10-27 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c2c48e1-c77d-3db8-a097-a31c21d7fd5f | -3.46082 | -47.66896 | 2024-10-27 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b86b813-936a-32c0-a09c-f2271829a802 | -3.45798 | -47.66471 | 2024-10-27 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 866aaad0-3b83-3809-a340-7604b834c700 | -3.45738 | -47.66845 | 2024-10-27 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5926faa-2766-397e-b232-f54fd4e01dc2 | -3.16046 | -48.36689 | 2024-10-27 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea8adcfc-29d1-3ca2-b264-f93ead39e721 | -3.15983 | -48.37086 | 2024-10-27 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4eda1cb1-c1b3-307d-bcb0-e13d0084a63a | -3.08484 | -47.78125 | 2024-10-27 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5701329-b54d-344a-814a-82630d281d01 | -3.08241 | -47.78117 | 2024-10-27 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57056058-c055-3079-a397-29e631599be1 | -3.01243 | -48.08967 | 2024-10-27 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20a4043b-86df-3314-b7ac-5d99a27aedc7 | -2.17725 | -48.8244 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 977154e1-954c-3e6d-a20d-95d965e8c0e1 | -2.16992 | -48.82321 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4272ae04-79eb-3c7a-b0ff-2d5b94cda7d7 | -2.1583 | -48.45127 | 2024-10-27 04:23:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c5528256-7170-326d-966e-a796c2540393 | -2.15764 | -48.45539 | 2024-10-27 04:23:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| eb81e917-ee41-3f24-a761-4aa817eae1fe | -2.10128 | -48.55293 | 2024-10-27 04:23:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f5c3b5e4-a7d9-315c-8152-cb55793b31c9 | -2.1006 | -48.55714 | 2024-10-27 04:23:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7942ec6b-a21b-3312-a535-7d69aea5c715 | -2.49389 | -48.04824 | 2024-10-27 04:23:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6ec2c6ac-5f60-314d-a22d-442c4cd8e7ce | -2.49327 | -48.05218 | 2024-10-27 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b8f8d731-0109-3797-8d8b-a231fde7ce5f | -2.49266 | -48.05612 | 2024-10-27 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8216e1d1-dcaa-3f4e-8ef5-673995223044 | -2.48975 | -48.05164 | 2024-10-27 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 545d522e-17ab-3630-9531-989e31b9bdaa | -2.48913 | -48.05558 | 2024-10-27 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f1e18f11-7820-3adc-aa32-c8465a6429f0 | -2.45671 | -48.50752 | 2024-10-27 04:23:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63de2470-33ee-3ed6-963e-3d44cbdd9a69 | -2.45312 | -48.50695 | 2024-10-27 04:23:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d3690474-ac0c-3843-b067-2f366c556d97 | -2.41617 | -48.59181 | 2024-10-27 04:23:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c7bbc9c-c5d5-3797-9dc2-8ffbb2259f68 | -2.41383 | -48.58997 | 2024-10-27 04:23:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c4755fc-8c47-3ceb-86d1-a1303084d8c0 | -2.36668 | -47.66789 | 2024-10-27 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d4873b98-8c9a-32dc-b7f9-24eb28b9df40 | -2.36607 | -47.6717 | 2024-10-27 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3e4f2f7b-714c-3233-bd2e-08a15f6f9bf4 | -2.36321 | -47.66734 | 2024-10-27 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0b16a868-eb10-3ab5-aaf6-0e70ecf6f8f1 | -2.3626 | -47.67116 | 2024-10-27 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 21e329fd-51c1-3cce-a49d-eb5ee297ccb7 | -2.36199 | -47.67497 | 2024-10-27 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc7627fc-f35e-3d56-ac6d-79c67dce376f | -2.35914 | -47.67062 | 2024-10-27 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 91d689dd-f53a-3d48-b337-00387c463e82 | -3.26419 | -48.79941 | 2024-10-27 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c1188a1-578e-3f6b-88fb-aaeb14b79068 | -3.26351 | -48.8036 | 2024-10-27 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14184027-19fd-38b5-b4c1-36bda0f325cd | -3.26058 | -48.79884 | 2024-10-27 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b073821-0f92-3767-8602-1188634ff41b | -3.15607 | -48.72808 | 2024-10-27 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc2dc7db-c194-3605-a7fa-ee270f811a4c | -3.15539 | -48.73222 | 2024-10-27 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d5112a8-c665-340f-a8ab-406acf18369e | -3.15441 | -48.72956 | 2024-10-27 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8080d1d-a4df-3e25-bcb3-ab12598a7288 | -2.76079 | -48.71358 | 2024-10-27 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 539be774-ee60-3e6d-a8bb-4c6667698328 | -2.76011 | -48.7178 | 2024-10-27 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94cd7c18-7e1d-3746-9e84-a85eedcfbe01 | -2.75783 | -48.70884 | 2024-10-27 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16937728-985f-3e7a-8825-c379c5d38892 | -2.75716 | -48.71301 | 2024-10-27 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 968ab125-6180-37a8-b8e5-37d4997ce3c9 | -2.75354 | -48.71243 | 2024-10-27 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1dec483-7cc1-31fb-b93c-0b302d35a629 | -2.75126 | -48.70354 | 2024-10-27 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c59ab212-0932-3738-9e97-3b72f46d8174 | -2.75059 | -48.70771 | 2024-10-27 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd3b63a7-af63-38fd-95a2-734b097834d1 | -2.74764 | -48.70297 | 2024-10-27 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74b26c8c-3688-39d3-b82f-5ccc3a74969a | -2.72954 | -48.70006 | 2024-10-27 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25b19d80-c11e-39d5-a848-46ff7bea1090 | -2.72592 | -48.69947 | 2024-10-27 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44bdb34c-30bd-3669-94dd-8bdc9e3914db | -2.68563 | -48.6428 | 2024-10-27 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57902f83-db21-38d3-a0d3-4852453d5e66 | -2.68268 | -48.63804 | 2024-10-27 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README46.md)
