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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83a34c7c-0849-36fa-be5c-8c7e0640126f | -11.1613 | -50.7221 | 2025-09-13 01:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 132abc8d-63ab-3db6-b995-74e9946b9f51 | -20.5946 | -50.4267 | 2025-09-13 01:10:00 | GOES-19 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 108.6 |
| 8abe7fa9-aeff-3a4b-a3ef-f7ae1119f8f0 | -9.2503 | -51.2472 | 2025-09-13 01:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 079b0316-fe47-3828-b835-f71d2eda6884 | -9.2658 | -59.3997 | 2025-09-13 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 208.1 |
| 3d606df1-f4f5-35dd-b9fe-13f48bd48ecc | -11.075 | -51.4942 | 2025-09-13 01:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| dcc69681-7d66-36ce-af73-4df8b6f57f73 | -10.6389 | -46.2718 | 2025-09-13 01:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| e8e4a4e8-92a7-3999-a8ec-4e4af834625b | -9.2844 | -59.3986 | 2025-09-13 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 7ab37c8c-0338-30e2-87db-eb4d844e9f26 | -11.7192 | -46.6257 | 2025-09-13 01:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 0810e186-1f25-3390-837f-797a0f4421f5 | -10.6385 | -46.2944 | 2025-09-13 01:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 73d3fa5b-858b-3cf3-a811-24836fa45ef1 | -11.0945 | -51.45 | 2025-09-13 01:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 151.5 |
| 7c042d27-d072-3927-8320-a2287a1014ac | -9.4807 | -46.4096 | 2025-09-13 01:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| c66e9dca-b0ec-3024-895b-78485ac88f29 | -16.2541 | -50.0745 | 2025-09-13 01:10:00 | GOES-19 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 3a25d5ce-501e-3407-b340-818747836870 | -9.2472 | -59.4007 | 2025-09-13 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 68ef5508-bf52-398d-b1a7-10d1aed2d9ee | -11.0942 | -51.4711 | 2025-09-13 01:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 221cd847-80f5-3781-8466-dae388847b38 | -12.0056 | -47.7728 | 2025-09-13 01:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| cd2a14fa-b587-38e4-9c53-e292ae55492a | -15.1359 | -52.4892 | 2025-09-13 01:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 6f73b4ce-9e6f-35fd-bbf5-02f6182b9abc | -11.7196 | -46.6031 | 2025-09-13 01:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 193.5 |
| b0ee3658-0e4b-30bc-9f4d-1acd6d940ab0 | -11.1519 | -51.4018 | 2025-09-13 01:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| ac3612aa-5cff-32fb-8f93-b6a7712e50b7 | -9.5324 | -54.6277 | 2025-09-13 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 107.4 |
| a603fc03-72c0-319f-a14c-c1eda701a33d | -20.6156 | -50.3998 | 2025-09-13 01:10:00 | GOES-19 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 142.1 |
| 220517d2-fb23-381b-a855-1a201504bcaa | -15.2036 | -56.6803 | 2025-09-13 01:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 2ee725b6-803c-309b-9809-606c5b034c85 | -20.5952 | -50.404 | 2025-09-13 01:10:00 | GOES-19 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 258.4 |
| 979c27af-2624-380f-809c-ac872314e5fa | -9.4996 | -46.4075 | 2025-09-13 01:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| c1de7ec8-1039-34c5-9d7c-1a45322b38a4 | -11.0752 | -51.4731 | 2025-09-13 01:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| e44b064e-7614-3bcc-bce6-69252a80a910 | -20.5952 | -50.404 | 2025-09-13 01:20:00 | GOES-19 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 109.6 |
| ab544974-19cc-38ff-89a1-e669d8250fa0 | -15.1359 | -52.4892 | 2025-09-13 01:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 68.7 |
| e74124c1-6cbc-3eae-af09-ebc6d94763c7 | -13.8983 | -48.2581 | 2025-09-13 01:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 52.7 |
| d95736df-a0e2-36b9-bf70-73ea8eda5aa4 | -13.8979 | -48.2804 | 2025-09-13 01:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 2b674bad-951e-333f-b238-3af71b1a7fc9 | -3.2321 | -46.7836 | 2025-09-13 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 400ba22c-1b7d-3bc2-809a-78513c8d0d7c | -9.5004 | -55.9788 | 2025-09-13 01:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 009f0f10-1510-3c05-984f-1640fc1fd58e | -12.006 | -47.7505 | 2025-09-13 01:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 391b85e3-6cf6-3090-a794-c882d49aceb5 | -9.2844 | -59.3986 | 2025-09-13 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 299b7d5f-16ea-389e-97e4-40ba0f52a9ee | -9.2472 | -59.4007 | 2025-09-13 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.0 |
| b2ac1c00-5d1d-33b7-a78e-556176f45c9b | -9.4807 | -46.4096 | 2025-09-13 01:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 9bc503f9-9fb7-3470-bc4d-0fb21cb19d57 | -12.5603 | -45.662 | 2025-09-13 01:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 5a502c68-c826-3ad4-955f-8e7338e94ad8 | -11.7196 | -46.6031 | 2025-09-13 01:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 265.3 |
| 7fa0bd80-c482-3f53-a4af-b5442e2adc01 | -9.2843 | -59.418 | 2025-09-13 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 126.4 |
| d8f00737-82aa-3553-a4f6-551dd99eae6c | -11.1423 | -50.7242 | 2025-09-13 01:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 7ef3d656-da11-3831-b2d0-5df069ace7c0 | -14.2092 | -46.2439 | 2025-09-13 01:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 5e4640f6-f8c9-3e14-b481-1556433ba4c5 | -11.0945 | -51.45 | 2025-09-13 01:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.7 |
| e949e248-5f50-3fbc-8336-09e005e2ec6a | -14.1898 | -46.2472 | 2025-09-13 01:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 293c6020-d4d0-3abf-82e2-c2d3864bf034 | -9.5137 | -54.6292 | 2025-09-13 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 140.0 |
| 20e95c50-7c0b-3794-97ba-9d1ab1ae5f34 | -9.247 | -59.4201 | 2025-09-13 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.3 |
| da11ea1a-96c3-3b28-8bc4-70ef97150d6b | 0.6904 | -50.6481 | 2025-09-13 01:20:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 6b04d901-5737-335b-9d8d-250c5f54038d | -16.4906 | -55.1276 | 2025-09-13 01:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 73.3 |
| 838b0158-3582-3282-ace3-24efdbf602b9 | -20.6156 | -50.3998 | 2025-09-13 01:20:00 | GOES-19 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 89.7 |
| 154b3907-a6ee-3893-938e-c9f7d88c35bd | -9.2658 | -59.3997 | 2025-09-13 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 209.6 |
| fcea51fb-1608-3013-95ec-fe59dc1900b2 | -9.5324 | -54.6277 | 2025-09-13 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 441afb0d-ef17-3d47-ac31-aa2e3cb79800 | -15.2036 | -56.6803 | 2025-09-13 01:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| c1402371-2ca0-31ae-97d7-4f09af515448 | -9.2503 | -51.2472 | 2025-09-13 01:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 619538dc-1097-3059-8c4f-5cb791697cc1 | -11.7388 | -46.6005 | 2025-09-13 01:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 265.2 |
| 8f452280-ae3f-375b-948d-d8121883be21 | -3.2282 | -47.6371 | 2025-09-13 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 130.3 |
| 83124113-1f03-3cee-89ff-d0f4f1304545 | -9.4993 | -46.4299 | 2025-09-13 01:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 17a44788-ebfe-335d-8d3d-ab60560a5de8 | -19.244 | -46.4201 | 2025-09-13 01:20:00 | GOES-19 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 76.4 |
| a8ad8346-b585-3b3a-a2e9-aa7dd4228463 | -10.6579 | -46.2694 | 2025-09-13 01:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| f23f6d8a-b1c0-338a-941a-d1840543515a | -11.7192 | -46.6257 | 2025-09-13 01:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 9598d8de-1ded-3a04-b829-7e7d87c125eb | -9.5006 | -55.9588 | 2025-09-13 01:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 116.9 |
| d73194ed-27c7-3176-ade0-9497820f52f9 | -15.1748 | -52.4839 | 2025-09-13 01:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 58.7 |
| b750ab18-432b-3c4a-b3df-fa357dcb27d4 | -10.7664 | -50.5299 | 2025-09-13 01:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 2df1442e-9868-30a6-9eff-178a5b947cf9 | -14.1888 | -46.2932 | 2025-09-13 01:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 4913c65f-47c1-371d-a93d-8ce4c6d8d5a0 | -11.1426 | -50.7028 | 2025-09-13 01:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 713fbff4-e719-369f-b5d7-7185e9b91a8c | -16.3422 | -51.5217 | 2025-09-13 01:20:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 67.1 |
| ea1c8ef7-986a-340f-a7d6-05cca305e1c9 | -3.2283 | -47.6154 | 2025-09-13 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 4f7eed00-623e-3a29-b695-2b48dc6f0fd8 | -14.2282 | -46.2636 | 2025-09-13 01:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 23416d15-a5fd-3e01-b2c1-30861bddac57 | -11.5806 | -50.5904 | 2025-09-13 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 18ec9357-c5b1-3efd-86d5-1c7bf6255015 | -9.4996 | -46.4075 | 2025-09-13 01:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 4bbbb3e1-d867-32a7-bb58-58b0cfe70641 | -14.1893 | -46.2702 | 2025-09-13 01:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 166.1 |
| 78a73fbd-696d-3664-91d8-38041e0c196e | -9.2656 | -59.4191 | 2025-09-13 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 242.9 |
| ee323e17-2d25-336f-ad7f-139ada0d8564 | -11.72 | -46.5805 | 2025-09-13 01:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| d147c2db-5651-3fdd-bac3-191caa14c76c | -12.5795 | -45.6591 | 2025-09-13 01:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 35d317d9-e194-37d6-aee0-485174774896 | -12.9292 | -54.7538 | 2025-09-13 01:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| fa5773e0-9142-3667-bdf8-650dde63c5fb | -12.5791 | -45.6821 | 2025-09-13 01:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 64.4 |
| de1b725a-ffa6-3d36-8674-bfc4f60dbd58 | -11.7384 | -46.6231 | 2025-09-13 01:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 76d9fd54-3b30-357a-bec9-d9f53b4ad02c | -16.3418 | -51.5434 | 2025-09-13 01:20:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 68.4 |
| f4de1255-6e12-317e-aeb6-e8b778e7dc42 | -11.7424 | -44.2117 | 2025-09-13 01:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 0c5a05a6-ee9d-3790-a493-108d374fe529 | -16.5666 | -49.2247 | 2025-09-13 01:20:00 | GOES-19 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 5da4f924-f5d3-3ce8-b855-013b1d62e6b0 | -19.2447 | -46.3964 | 2025-09-13 01:20:00 | GOES-19 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 4ab99be2-7b01-3248-9224-332f94b65e99 | -19.265 | -46.3917 | 2025-09-13 01:20:00 | GOES-19 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 118.0 |
| b33314ea-bb0b-358c-9aec-f59544328c58 | -11.3849 | -63.3606 | 2025-09-13 01:20:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 49.0 |
| e1fc1d48-20c5-3d0c-a137-9c12fa0a12ca | -14.2088 | -46.2669 | 2025-09-13 01:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 238.3 |
| b27d1f19-2e07-3ff7-bdd1-2a94b51c45f8 | -9.4819 | -55.9601 | 2025-09-13 01:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 357227a6-2413-3ef6-8d35-748a4988c059 | -10.6575 | -46.292 | 2025-09-13 01:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| a14da719-25ac-3802-834a-fee8a895f1ef | -19.2643 | -46.4154 | 2025-09-13 01:20:00 | GOES-19 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 115.7 |
| dd62e098-dfa0-3c10-b7f5-0c25bf4d27ee | -11.8468 | -50.5813 | 2025-09-13 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 1eacf218-c6b8-358e-bd30-a4e17f9be9c4 | -3.2305 | -47.135 | 2025-09-13 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 16627f21-84cb-33bf-8a4d-ce75d18beca7 | -11.5803 | -50.6118 | 2025-09-13 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 262fd4f0-4ec7-37c7-abaa-258631f8a4f6 | -8.4331 | -47.2527 | 2025-09-13 01:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 7ecadae6-c58c-3274-bd8e-fd221b1157e6 | -16.3422 | -51.5217 | 2025-09-13 01:30:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 69.8 |
| bed1ecfc-ea29-3f46-a281-4efcca96a324 | -9.5137 | -54.6292 | 2025-09-13 01:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 131.5 |
| 44e9e5bc-a872-31fa-9480-b2914e004145 | -9.247 | -59.4201 | 2025-09-13 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 452a6193-104c-3b0e-9a6a-a4489d20e203 | -9.5004 | -55.9788 | 2025-09-13 01:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 9b5f5687-e9d0-3f8c-90cf-97d7f85c423d | -20.5952 | -50.404 | 2025-09-13 01:30:00 | GOES-19 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 92.2 |
| 6f120430-5864-31fb-b779-243293703d7e | -9.5499 | -45.5207 | 2025-09-13 01:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 094dfee6-62f1-3df8-ae00-9ab6e1ef06d5 | -11.7384 | -46.6231 | 2025-09-13 01:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 143.5 |
| bb8062f1-475d-362c-b9fe-b35e7eebec7b | -13.9172 | -48.2775 | 2025-09-13 01:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 84.5 |
| e016a433-0159-36bf-8ec8-b39faef5f1ab | -16.0257 | -47.9294 | 2025-09-13 01:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 114.8 |
| e663025e-c17d-3b8e-8b61-e9af6b85aaca | -9.057 | -47.0355 | 2025-09-13 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 40.7 |
| b1e16d75-cebb-3d83-af18-9e9133a2769b | -3.2283 | -47.6154 | 2025-09-13 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| d8ecd323-974f-3aff-b515-0412290ad778 | -11.8468 | -50.5813 | 2025-09-13 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 753f69c6-0aa7-3dd7-9b5d-1b08b84f23c3 | -12.9292 | -54.7538 | 2025-09-13 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |


[Clique aqui para ver as próximas entradas](README13.md)
