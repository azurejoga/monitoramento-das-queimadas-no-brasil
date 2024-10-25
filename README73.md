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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0b4c50e-06bc-3e1d-b617-6db0781ca928 | -11.04025 | -49.47066 | 2024-10-25 04:40:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae422ab7-5f15-3136-a5df-de1204506acc | -11.036 | -49.59739 | 2024-10-25 04:40:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 75a29345-4054-3d1b-a169-ad9e4b2d150c | -11.03545 | -49.60095 | 2024-10-25 04:40:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 43ddbc43-19fa-3a9e-a4ca-7bfd21be8241 | -10.98544 | -49.20096 | 2024-10-25 04:40:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25e7806f-a775-370d-b3a7-8a4933d077e0 | -10.98489 | -49.20457 | 2024-10-25 04:40:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f11b0edc-805c-3945-bc0e-68fbb5a75934 | -10.98434 | -49.20817 | 2024-10-25 04:40:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa86f0db-033f-3a40-837b-5aa09443c2fc | -11.16163 | -49.29461 | 2024-10-25 04:40:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1b023cb6-4579-3861-bb40-d08d1dc17439 | -11.15827 | -49.29408 | 2024-10-25 04:40:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46f05c25-8db2-3772-8150-2d8162b337fb | -10.66933 | -51.81702 | 2024-10-25 04:40:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 586237e6-9c8e-36b4-bc20-2dc4cde6d7d0 | -10.66874 | -51.8207 | 2024-10-25 04:40:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cfba8889-b364-31b9-9eef-8b5b5c369d5d | -10.60635 | -51.90469 | 2024-10-25 04:40:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9a6ed57-bf84-3ddf-bd31-a585160ddfb4 | -10.55942 | -51.63067 | 2024-10-25 04:40:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c04fe932-7313-3851-b92f-ea5794a75274 | -10.38649 | -52.11764 | 2024-10-25 04:40:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97258250-9e64-3883-9632-48e61f30d368 | -10.34465 | -51.4691 | 2024-10-25 04:40:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ba98953-d9e9-311f-b93b-6061f1d2e1a2 | -10.32185 | -51.52459 | 2024-10-25 04:40:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b19ace5-b509-3169-94c5-827312903013 | -9.91059 | -50.54294 | 2024-10-25 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1a076ece-c490-3313-96c2-0859d6ec86e6 | -9.91004 | -50.54645 | 2024-10-25 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2abcb43f-13f4-3c19-b870-c28723028bae | -9.90671 | -50.54591 | 2024-10-25 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d1105674-eae3-30ab-8d49-6b6887a2730d | -11.03338 | -51.7714 | 2024-10-25 04:40:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b9bd7d2-b2ce-341f-8f9b-2beb3dbec7b8 | -11.03279 | -51.77504 | 2024-10-25 04:40:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42a4e446-5b9e-3df0-9ceb-bc2be124f6cc | -10.61294 | -52.41728 | 2024-10-25 04:40:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 53a97f31-179f-32c1-b583-8f91ba5c20f0 | -10.61231 | -52.42109 | 2024-10-25 04:40:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 68e19b72-5783-3c55-b870-b5ab46a08ed8 | -10.61056 | -52.82402 | 2024-10-25 04:40:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c40d6ecd-0d30-35ed-a14f-af717814a7c1 | -10.61011 | -52.41289 | 2024-10-25 04:40:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfbd6bcd-918f-3d49-b76e-4bbd90d46254 | -10.60991 | -52.82798 | 2024-10-25 04:40:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4caf7e25-acda-3383-9cb8-84152a7dcfd0 | -10.60948 | -52.41669 | 2024-10-25 04:40:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05235cb1-1051-399b-9209-1899dbaefdc5 | -10.60885 | -52.4205 | 2024-10-25 04:40:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1486148-d72a-3e6a-8ff6-2f0bccc0d1bf | -10.60705 | -52.82343 | 2024-10-25 04:40:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0da5515d-2b7a-3cf0-9d9c-1c0ae8b81c4f | -10.6064 | -52.82739 | 2024-10-25 04:40:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 474fbe35-8ecd-3459-8124-9d9ce29c71f6 | -10.6054 | -52.41992 | 2024-10-25 04:40:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3e3be4b-4352-32f3-8330-6bfb883ef724 | -9.71348 | -52.81107 | 2024-10-25 04:40:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1c0a362-b1a0-3f22-baab-396d2d95c146 | -10.99518 | -52.87806 | 2024-10-25 04:40:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 856dd718-127a-3661-8d23-1ee5ec65c622 | -10.99453 | -52.88201 | 2024-10-25 04:40:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7acfaed3-2d4d-34f2-be26-8ea6b4affe19 | -10.99103 | -52.8814 | 2024-10-25 04:40:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1ed38d1-cfad-3a5b-ba6e-62948c9979a6 | -13.17547 | -53.76987 | 2024-10-25 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16cfe865-3e83-3296-a10e-c02efbfeae9f | -13.17407 | -53.76705 | 2024-10-25 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0a585ad-0f23-36a1-986c-58714a938648 | -13.17339 | -53.77114 | 2024-10-25 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6dbeed19-484d-31bc-8f9c-cc8eaa261f86 | -13.17271 | -53.77524 | 2024-10-25 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8912c857-ee33-3f6c-b6e0-8d1873f07338 | -13.17191 | -53.76925 | 2024-10-25 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 204a1a4d-46b8-37ef-8fea-0f519bb24eaf | -13.17121 | -53.77333 | 2024-10-25 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7361e0c3-1958-317c-acde-377da10921fd | -13.17051 | -53.77743 | 2024-10-25 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d690f25-bd35-3ca1-8dc9-94f4befc0100 | -13.16983 | -53.77051 | 2024-10-25 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4c2224b-91e3-3dc5-849f-de565ec13f24 | -13.16915 | -53.7746 | 2024-10-25 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07762f72-ecab-3b5e-be43-2c1ee8f8ef14 | -10.69965 | -54.56671 | 2024-10-25 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 495c77a4-2905-3a6a-9033-2a06b07a35ae | -10.48618 | -54.87459 | 2024-10-25 04:40:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8adfe211-87ce-3cb9-b895-eac852e22ab6 | -10.48612 | -54.87764 | 2024-10-25 04:40:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70d3c0ef-61f5-36dc-924b-1577a33755c1 | -10.48219 | -54.877 | 2024-10-25 04:40:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f36ed160-cd7c-3b60-9d38-21f8ed02379c | -10.45453 | -55.10081 | 2024-10-25 04:40:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb1871ce-7019-31b0-85dd-812c9131bb82 | -10.45292 | -55.09856 | 2024-10-25 04:40:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6c2002f-9017-381b-91e2-b3a2158077e0 | -10.45204 | -55.10377 | 2024-10-25 04:40:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9eeac7fb-b48c-392a-9da4-40212644855f | -10.45056 | -55.1001 | 2024-10-25 04:40:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a07e815b-7902-3088-8bf1-0a43dc10007d | -10.4374 | -54.45461 | 2024-10-25 04:40:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bec968e2-7a75-366c-9811-b9ff3a4f6c5b | -10.4366 | -54.45942 | 2024-10-25 04:40:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8c42f5c-629d-313a-bfe9-8da2a3238b89 | -10.22597 | -53.87786 | 2024-10-25 04:40:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8362996-e5e8-374e-8ab7-cd7db7d5d07d | -10.18181 | -54.20174 | 2024-10-25 04:40:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29222afa-a25a-32a9-aa69-005fcd337375 | -10.07255 | -54.36428 | 2024-10-25 04:40:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff40bfbb-2628-32d9-97f3-8d4ce8c39411 | -10.07174 | -54.36901 | 2024-10-25 04:40:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02830146-78ad-3475-b113-87979cee98a2 | -10.02762 | -54.33983 | 2024-10-25 04:40:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 272fb01c-844e-3258-945c-11d50c9f548b | -10.02382 | -54.33908 | 2024-10-25 04:40:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ed4c7f17-bc30-3bba-8c59-df831bd74a2b | -12.15536 | -55.42681 | 2024-10-25 04:40:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0306f58f-a6c2-3f68-84b0-4e3041278282 | -12.03568 | -54.65193 | 2024-10-25 04:40:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 150c6f5c-ef99-3835-be25-414f584d7de0 | -12.03489 | -54.65659 | 2024-10-25 04:40:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1ce8dd6-71ba-3cbc-8d43-08b0b818897b | -11.91527 | -55.51239 | 2024-10-25 04:40:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff795892-bb5f-3415-ac9e-3769366944ed | -11.89475 | -54.79961 | 2024-10-25 04:40:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a8411d1-1223-3c93-a9f7-7da87afb3414 | -11.35225 | -54.48272 | 2024-10-25 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89e38508-fa71-3cc3-8221-1a1a4f4d8483 | -11.35145 | -54.48735 | 2024-10-25 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bb3be06-d3fc-3399-b89d-a04e44a56d7e | -11.31649 | -54.33091 | 2024-10-25 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 593a7d0b-d59d-3f7c-8139-d6aa9b976b75 | -11.31274 | -54.33023 | 2024-10-25 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d58aed39-44f9-31db-ad34-c237036f9116 | -12.61708 | -55.22213 | 2024-10-25 04:40:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3667bf74-bfe9-3ecc-b687-c1616833936c | -12.6162 | -55.2271 | 2024-10-25 04:40:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c02a94a5-1b62-3e89-8415-88df115b0588 | -12.50355 | -54.356 | 2024-10-25 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 676399d0-ef9e-3fef-badd-0b03dcc7f34e | -12.5028 | -54.36044 | 2024-10-25 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ababe0fd-a96a-3e10-adfa-e384bdf66716 | -12.47418 | -54.46153 | 2024-10-25 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30f71542-b206-3238-b722-7fb26f7495d6 | -15.67126 | -55.98197 | 2024-10-25 04:40:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 1e0e5d4a-9fba-34e4-bc1b-7d40b66e6898 | -15.66948 | -55.99199 | 2024-10-25 04:40:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 3cde938f-47df-3f8b-8fdb-2633c918e5c5 | -15.66739 | -55.98122 | 2024-10-25 04:40:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| cb800954-39aa-3edd-a4c6-4b07c9776055 | -15.6665 | -55.98622 | 2024-10-25 04:40:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9418c0ec-3d78-380c-b029-f84ebb2621a0 | -15.66561 | -55.99122 | 2024-10-25 04:40:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7213dc1c-7b90-36ec-9bb5-216db4b41721 | -15.66175 | -55.99046 | 2024-10-25 04:40:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e544a12a-a25e-3026-bca6-5141f1bdefdd | -15.65788 | -55.98969 | 2024-10-25 04:40:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 2b091519-ea0a-32ec-82cb-32ac47c4b50f | -15.67037 | -55.98697 | 2024-10-25 04:40:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ad6370a8-eb9c-31c2-8d4b-c04b0432b532 | -15.66353 | -55.98047 | 2024-10-25 04:40:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| d846a3e3-be3b-3d23-ad3d-256808466345 | -15.66264 | -55.98547 | 2024-10-25 04:40:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3d709917-e648-34a2-9d1b-7df074c03b71 | -15.44987 | -56.23581 | 2024-10-25 04:40:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f1a2abd4-2eec-33c8-a044-7ae786438a76 | -15.44829 | -56.23737 | 2024-10-25 04:40:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ea2e9f14-545e-3fba-be98-072008716603 | -16.40626 | -55.92032 | 2024-10-25 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 765236d9-ff56-3898-957d-3f55d2b7f475 | -16.56849 | -56.2466 | 2024-10-25 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 6f13e063-fc6c-34ec-8cea-4e0db52ed5f0 | -16.56553 | -56.24082 | 2024-10-25 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 47aad434-2d19-34e6-8fd2-014ab9c49766 | -16.56462 | -56.24584 | 2024-10-25 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| e6c8e190-7666-3251-a36d-d0942aff6d71 | -16.56371 | -56.25086 | 2024-10-25 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 708c6fbb-d329-3944-8b1c-9b020a241c6b | -16.56075 | -56.24508 | 2024-10-25 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 66930951-baf0-30ae-ae9a-2153225e5bdf | -10.62299 | -55.90627 | 2024-10-25 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ea27cd71-542c-3a61-b22b-995a57ecbd5e | -10.61881 | -55.90554 | 2024-10-25 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 16c02234-64a0-39f1-bcf6-3fd420e22852 | -10.48751 | -55.62146 | 2024-10-25 04:40:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c98d057-53ca-33a8-ae08-094526edc561 | -10.48341 | -55.62069 | 2024-10-25 04:40:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 698fec7c-e9d6-3081-a72d-ac570374e267 | -10.44674 | -55.33357 | 2024-10-25 04:40:00 | NPP-375D | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 112428d2-d024-3b3f-bc72-25ab3d4c2927 | -10.44271 | -55.33284 | 2024-10-25 04:40:00 | NPP-375D | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39b427a6-17b4-36f5-9d8b-60310acc34db | -10.1035 | -55.39071 | 2024-10-25 04:40:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22d005e0-07f8-3f18-95b8-117788d7ae81 | -10.08725 | -55.3877 | 2024-10-25 04:40:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91cda7b5-6d86-3f31-84b3-c0ab9fbf5677 | -10.08208 | -55.48881 | 2024-10-25 04:40:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README74.md)
