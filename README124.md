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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1dfce78f-9c26-3430-a583-4eb8b1dd634c | -12.74075 | -54.09278 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b808641-58cf-322b-a8c3-ba222d33fc7c | -12.7402 | -54.09645 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc2b9708-3b04-3caa-aaab-b109224b64ea | -12.73904 | -54.08125 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4c9b7e83-4211-31f2-8cfc-2e3723488183 | -12.73893 | -54.03604 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 011bad07-fda8-3f01-b634-bc769bf6eca7 | -12.73566 | -54.08072 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 338b1bea-79d8-30d6-8a64-b98ab0d658ee | -12.73556 | -54.0355 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39a3beb8-b8a8-3c3d-a317-99c55bb3b54c | -12.73511 | -54.08439 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d799c81-8e68-3460-aac5-9df839c61a8b | -12.73174 | -54.08385 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4cadfe50-d41b-3ab8-90c0-e7e32baaf744 | -12.72892 | -54.07965 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8cea18c5-8234-3760-acc8-7e6c296e29f3 | -12.72837 | -54.08332 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04f0ff23-b2af-3737-afc1-6bd00f9530bd | -12.72555 | -54.07912 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7d84bb0-5104-3b61-82ce-608f26f332bc | -12.72218 | -54.0786 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c27dc831-596e-3826-bb1b-f09da477eedc | -12.71936 | -54.07441 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7e9ab4b2-4601-37ae-87a9-a701fd53ba0b | -12.7188 | -54.07808 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f72cb881-eb53-3b45-b479-936d5b2cd996 | -12.71598 | -54.07388 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0809c5d8-2220-3157-b956-61af00397edd | -12.71261 | -54.07335 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 39a76083-ace9-3995-b9be-e6800be4dc11 | -12.71144 | -54.05809 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6ce3305e-f5f0-3b2e-914c-5b71db79919a | -12.71089 | -54.06178 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f695663e-3720-37c8-b92a-7ffa6f13a308 | -12.70979 | -54.06914 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cc002811-4d32-3425-9fdf-f214d9b7cf37 | -12.70924 | -54.07282 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d57eda84-3160-380f-b613-a2ba75970e60 | -12.70807 | -54.05756 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e506a6b7-fbff-3882-b4e8-9e3a5ea7563e | -12.70752 | -54.06125 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3538cc2-a853-3ba1-b9a0-ef7d6bd596e2 | -12.70697 | -54.06493 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da9f885d-cbfe-35ef-9bcd-d41403da5869 | -12.70642 | -54.06861 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9fb9886f-c8d2-3dd6-9875-00554248a28f | -12.7047 | -54.05703 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d828f11-d138-3fb0-a40f-170c2f55c4f8 | -12.70345 | -54.01908 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b84c9928-3e8f-3e95-a649-2d7e0d038292 | -12.70304 | -54.06808 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3a99cf2d-7d19-3c73-97d9-6043b810e828 | -12.69561 | -54.03735 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2bc0eb9f-8677-30f7-8719-6ee76389918c | -12.69505 | -54.04103 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7770c19-e6a8-3f75-8357-412f22146df9 | -12.69448 | -54.04472 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c602873a-323e-3d64-894c-ef471145975a | -12.54583 | -53.16614 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d38b4fcc-4a2b-3c78-8737-584fe18eb3c3 | -12.54294 | -53.16169 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c0a880c5-a36b-36ee-bfd2-6e8bbfac66ff | -12.54236 | -53.1656 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d31c34f8-9e03-34f0-8017-e87d06807472 | -12.54195 | -53.50093 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| f7714815-0a51-3866-84ae-e7537bc0e262 | -12.54179 | -53.16951 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c04d50f-3eab-3eb3-8a96-14cec287e3b1 | -12.54064 | -53.17733 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75c39acf-ba21-3e79-b51a-669d03837b25 | -12.53946 | -53.16115 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4e9fe173-6360-37a0-bb1c-ce5a51b6f3ae | -12.53909 | -53.49659 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6cedb6de-6b95-3305-b8a8-e2fbdc1744ce | -12.53889 | -53.16505 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ffa843f3-c600-367b-a378-2c3f5d4993bf | -12.53852 | -53.50039 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 524ef113-4d72-33d4-876b-dedcc1b4d2db | -12.53831 | -53.16897 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da1348d7-e7c1-338f-938e-04cf9293ea87 | -12.53795 | -53.50419 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 2aaf8808-123c-3395-9bfb-1231cc036836 | -12.53774 | -53.17288 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1481af2d-982c-362d-b6dd-1fafea829fc0 | -12.53738 | -53.508 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d67eef8c-89af-3622-baf8-8d587e02b940 | -12.53717 | -53.17679 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 616fe0c5-d9e1-3066-8eed-ed934866ac07 | -12.53566 | -53.49606 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c3bf0c39-e2c0-327c-905a-1061a00291c5 | -12.53542 | -53.16452 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e1204db-bd30-3aee-91c4-2fbd2adad822 | -12.5351 | -53.49986 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a5f318f7-023e-3abc-8fb8-30a2bc612263 | -12.53484 | -53.16843 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 44ce2347-c646-3505-b671-c93b29145724 | -12.53452 | -53.50366 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 97b0806b-40a1-3892-a393-bdf6f7578c49 | -12.53427 | -53.17234 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a2ce1692-68fc-3c0d-b98e-421c961c1d17 | -12.53395 | -53.50748 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 21ababa0-72ec-3574-a0f2-508bbd1b59b6 | -12.5328 | -53.49174 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0cae335a-6567-39aa-a1b6-e2b93732b7f9 | -12.53224 | -53.49552 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5a03eed7-8354-316e-a7d0-4545339a1677 | -12.5311 | -53.50313 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dde2f454-e3c8-3717-88fd-14ca2b656b2a | -12.53052 | -53.50695 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d9eb8149-3f90-37c9-98ba-d9b001193fe6 | -12.52937 | -53.4912 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6db459aa-eeea-3c09-be22-5c66b43789be | -12.52908 | -53.18353 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd87060c-599e-38f5-9fc6-30b31a5c8792 | -12.52767 | -53.5026 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3dc5fd0-39b6-32fe-bec4-f8639b23e313 | -12.5271 | -53.50642 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c3937f3-3728-3682-8ec5-f2bc8cfb1029 | -12.52561 | -53.18299 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 411f1402-fb07-3a5a-a092-a88a72abf7d0 | -12.52481 | -53.49826 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33ff44d5-4705-36f1-a6e0-43e5453af597 | -12.52424 | -53.50207 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bdcca598-a483-3553-8ec8-ac73b086201d | -12.52367 | -53.50589 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e708ec8-3b1f-3412-b432-536f5cdf3c78 | -12.52308 | -53.48632 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 820f0955-a9d0-3f17-96cf-f07766df656c | -12.52271 | -53.17854 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ea7ff97-3d51-37b9-9bb2-044cd6324761 | -12.52252 | -53.49012 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb5ec411-5a03-3ecc-bab7-0f4de112db38 | -12.52214 | -53.18245 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 247d8101-a462-3c9e-974d-34883019f9de | -12.52157 | -53.18635 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 774b7add-f719-3abe-9bae-cc8d92c8ba8b | -12.52081 | -53.50154 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ff7863ee-ffd2-34a5-8e9e-ddde2da3c425 | -12.52043 | -53.19412 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27413634-fecb-38fa-b575-2204d1587adb | -12.52024 | -53.50536 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e29d42dd-018c-3cae-aa9c-98d94f4321ed | -12.52022 | -53.48198 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1fc6cc7e-145d-3fe0-b645-c9ba9a5d38c6 | -12.51965 | -53.48578 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 634a8046-1408-32ab-b95e-a0869215c0cb | -12.51867 | -53.18191 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 422add27-eec7-3c19-b2aa-b87c4c2b6b4b | -12.5181 | -53.18581 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60f4079e-ef30-3a13-9d17-24b5c75e5442 | -12.51753 | -53.1897 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c813bc7-0e21-3e42-bc32-354879287678 | -12.51738 | -53.50101 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 51a966d2-9275-389d-9a45-2d21027f7734 | -12.51696 | -53.19359 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2763f077-3040-3138-b726-3fe1200591b5 | -12.51679 | -53.48146 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2dea6d18-dc3c-3822-92d1-31e66af193ca | -12.51622 | -53.48525 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fc506ccf-167f-36fd-9e61-389d3213e5f5 | -12.51395 | -53.50048 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 717de8e2-f09c-34ff-a66b-f82fedf1be54 | -12.51279 | -53.48472 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fcd3ecc9-175b-3e80-82b6-f4885a770bb4 | -12.50936 | -53.48418 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5fdc4650-f5a5-3c7a-94a2-1c83efd4228a | -12.50593 | -53.48365 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b60b8380-dacb-3353-90fe-f08ded121f72 | -12.50423 | -53.49507 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8467e31d-951f-3b0c-a3a0-f3be385d0bd9 | -12.50367 | -53.49888 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7e61ebd-55b2-33ec-9ccf-781b6804fc16 | -12.50307 | -53.47932 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fbad7b23-1035-3401-9c3d-37e87773d936 | -12.5025 | -53.48312 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd9cff96-a211-390d-9360-0203ff8ccb15 | -12.50024 | -53.49834 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ad1a0a0b-2708-3a1e-8a44-fcbadae5c241 | -12.49964 | -53.47878 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d85e94db-5d4f-3737-a1ec-9022df9c21da | -12.28303 | -53.45088 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 234dcc77-f1a4-3fb1-bc41-1b85a168cdfb | -12.81625 | -54.03704 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c108b24-399d-368a-b1fb-d579d8da121c | -12.81618 | -54.01433 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3d36899-5b96-354e-9c13-09709d2bac92 | -12.81563 | -54.01803 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9152d6cf-6e88-3a3a-94d6-c7c547b401ed | -12.81508 | -54.02173 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da19cf64-de18-35f0-b368-5209a7c614e3 | -12.81453 | -54.02543 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d225517f-0076-331e-a087-0a5b3c95be16 | -12.81288 | -54.03651 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7365c0be-0077-3b53-a67d-75da18b7d2e2 | -12.81233 | -54.0402 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c19ddbcf-7c54-375f-9aa2-c62a160222c0 | -12.8117 | -54.02119 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README125.md)
