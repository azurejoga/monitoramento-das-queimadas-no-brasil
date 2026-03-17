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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a14d3a6-0ee5-3329-a960-f61b02a5a2d9 | -13.66398 | -39.9129 | 2026-03-17 03:51:00 | NOAA-21 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d53f9649-f172-3cdf-9e83-e1725ce6281e | -13.01354 | -40.23186 | 2026-03-17 03:51:00 | NOAA-21 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d45d4ab1-861f-36dc-9c92-b42d67ea7cf9 | -21.85639 | -46.97834 | 2026-03-17 03:53:00 | NOAA-21 | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cac45543-c79e-36f2-9560-e761d1d2d837 | -21.7056 | -48.43063 | 2026-03-17 03:53:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 824dc88d-49ef-3f5c-94d9-0c987df55c2c | -21.71025 | -48.43193 | 2026-03-17 03:53:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8ba29f6d-e3c3-3f97-b56f-17ae55e5f82a | -21.36665 | -47.06068 | 2026-03-17 03:53:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f6f25e7-fc59-30cc-a6a0-972cc30e87b0 | -21.70445 | -48.43606 | 2026-03-17 03:53:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 81e21310-97ad-32f2-8ec8-31454272984b | -21.70392 | -48.43291 | 2026-03-17 03:53:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 77847577-ecf7-34b0-809e-eb189cec9d13 | -21.36139 | -47.06431 | 2026-03-17 03:53:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e1dad8f-8d15-3c73-b1b4-fcfbe057b8b6 | -21.8524 | -50.55662 | 2026-03-17 03:53:00 | NOAA-21 | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 092f83b5-f976-386e-a1cc-ebc8ec9c34fc | -21.70912 | -48.43732 | 2026-03-17 03:53:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 61d3a5d6-c594-3227-bfb8-a66691b803a8 | -26.85714 | -50.96802 | 2026-03-17 03:55:00 | NOAA-21 | CAÇADOR | SANTA CATARINA | Brasil | 4203006 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 00f4296c-aec4-304c-8c68-6aab8997282e | -27.09853 | -50.52374 | 2026-03-17 03:55:00 | NOAA-21 | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e2dc1aa0-b5ad-3a54-86fa-e802851e50cf | 3.1276 | -60.7647 | 2026-03-17 04:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 121.2 |
| a10d6a5d-6748-3d34-981b-d25c271d5fff | 3.1277 | -60.7457 | 2026-03-17 04:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 157.6 |
| 2fdb94e1-810e-3c71-a04d-05694bcdfd65 | 3.1094 | -60.746 | 2026-03-17 04:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 49ce1b80-7cd4-38b8-b18f-db5d964385eb | 3.1094 | -60.765 | 2026-03-17 04:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 50.5 |
| c444016e-cc8e-35bb-a589-f533fd2726bc | 3.1277 | -60.7457 | 2026-03-17 04:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 125.4 |
| 41f610ec-d60a-3c45-b52b-734882c6829e | 3.1276 | -60.7647 | 2026-03-17 04:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 807964c4-0476-3c33-966c-bfcfb3afd0fc | 3.1094 | -60.765 | 2026-03-17 04:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 732edc51-e328-38db-a827-08d49257aad8 | 3.1094 | -60.746 | 2026-03-17 04:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 77.7 |
| dabd1de7-0a06-3db2-98ae-7d35e03ac681 | -9.49742 | -46.10341 | 2026-03-17 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b5c5182-1423-3324-af2c-c0ad2c624db8 | -5.66972 | -45.2019 | 2026-03-17 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fd199c09-1f9b-38bc-8f86-6432d111e5ad | -6.06512 | -43.25848 | 2026-03-17 04:19:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.5 |
| adbbca95-331a-30d0-9d23-8983de122f26 | -6.0671 | -43.26218 | 2026-03-17 04:19:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c9ea623b-6da5-3c97-af60-57b68423b3ae | -5.52897 | -35.52354 | 2026-03-17 04:19:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c4e566a2-1650-3cc9-ac0d-f0205c712ee3 | -5.52423 | -35.52281 | 2026-03-17 04:19:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7ce90798-bf6f-3937-b38d-cf66884d905c | -5.52873 | -35.52226 | 2026-03-17 04:19:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 584f568e-d959-313e-8d4c-f512be15b8e2 | -7.98911 | -42.83699 | 2026-03-17 04:19:00 | NPP-375D | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1353b2d6-7d95-35a0-bcdd-53629285fb84 | -9.49679 | -46.10727 | 2026-03-17 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 718a7c84-31bb-31fe-8f8d-68e83d0b0e51 | -5.66909 | -45.20574 | 2026-03-17 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5620aece-a2ff-3463-bf77-933b35ed3ad1 | -8.3511 | -35.73407 | 2026-03-17 04:19:00 | NPP-375D | SAIRÉ | PERNAMBUCO | Brasil | 2612000 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6c64e573-032a-34bc-a8fa-df45d3d7c4bb | 3.1094 | -60.746 | 2026-03-17 04:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 39a06407-07bf-347b-8f7d-515bd29aa604 | 3.1094 | -60.765 | 2026-03-17 04:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 54898310-a1c9-3b1b-8ed0-c9c6aabbc3e1 | 3.1276 | -60.7647 | 2026-03-17 04:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 6ec60547-2591-3997-94cf-55eeaa1ff6d5 | 3.1277 | -60.7457 | 2026-03-17 04:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 135.5 |
| 67c1d9d2-d010-38f2-9c2d-1eaf16026700 | -13.01059 | -40.23578 | 2026-03-17 04:21:00 | NPP-375D | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 33ca89cc-c3b5-32b8-85d2-c52b90fcd651 | -13.13868 | -39.69382 | 2026-03-17 04:21:00 | NPP-375D | UBAÍRA | BAHIA | Brasil | 2932101 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3948ca13-6d4d-3eda-8bb3-18ff3faa05d4 | -11.73989 | -38.53465 | 2026-03-17 04:21:00 | NPP-375D | SÁTIRO DIAS | BAHIA | Brasil | 2929701 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8347dd31-079c-3ae4-b2d4-7f830729fb51 | -13.01185 | -40.23352 | 2026-03-17 04:21:00 | NPP-375D | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3cd0f33e-815a-31a6-a9b2-4ae4453fbfe6 | -21.35328 | -48.09764 | 2026-03-17 04:23:00 | NPP-375D | PRADÓPOLIS | SÃO PAULO | Brasil | 3540903 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22c5df90-344c-3be3-b39e-c918d0058c6f | -21.7059 | -48.4348 | 2026-03-17 04:23:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 36b9eebc-12d4-3e29-aa18-ec574c740323 | -21.70657 | -48.43088 | 2026-03-17 04:23:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1a179958-a3ae-3d8e-8540-04235c1cecf6 | -16.447 | -58.17924 | 2026-03-17 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 7743368a-c0c2-3c3e-8391-48a53f0f2eca | -21.7093 | -48.43549 | 2026-03-17 04:23:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19fa2b99-8472-3a8f-a5b1-8a883f024932 | -21.35805 | -47.0649 | 2026-03-17 04:23:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c2e72d7-e947-382f-8ef1-43d9948e4b17 | -23.02999 | -52.67673 | 2026-03-17 04:23:00 | NPP-375D | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ec0a9178-b35e-3ef1-90a7-f44b3d17b92c | -21.85573 | -46.97747 | 2026-03-17 04:23:00 | NPP-375D | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bdfa81f2-2e64-33f6-b2f2-f2ce7ca568a8 | -21.3653 | -47.06241 | 2026-03-17 04:23:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2ba00618-08d5-3270-b2a6-94d91e2d1831 | 3.12994 | -60.7449 | 2026-03-17 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 28.2 |
| b83fa5db-4503-35ea-9fd1-23c0b48b7b50 | 3.123 | -60.74604 | 2026-03-17 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 6c748413-a49f-3323-9368-e5ce26514994 | 3.09214 | -60.77068 | 2026-03-17 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d433da2-56b4-32f7-8983-d6e4336bfd7d | 3.13691 | -60.73672 | 2026-03-17 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1ff6034c-d14c-317a-92f4-1abcd0093a65 | 3.12997 | -60.7378 | 2026-03-17 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 409c0c0e-703f-392f-bedd-c76d2bbabda6 | 3.1419 | -60.72255 | 2026-03-17 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06b43a17-a590-3d16-9c5b-7b9970ac169e | 3.14884 | -60.72143 | 2026-03-17 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d4f1519-fa02-3a86-9a4e-c01f4cdf433f | 3.13088 | -60.75147 | 2026-03-17 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 59a00585-5513-3e56-9ed9-b3a55a4f3da7 | 3.12579 | -60.76574 | 2026-03-17 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 971265da-0369-324d-9cdb-5475111e5cc0 | 3.14892 | -60.72847 | 2026-03-17 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a928a0b2-d703-345b-9998-587f2d21a935 | 2.8623 | -60.73978 | 2026-03-17 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd4c2075-242d-3522-9bc9-73ffba1e5ff9 | 3.14289 | -60.72915 | 2026-03-17 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e0646db8-e713-39e2-881f-ffdcb1edb184 | 3.12392 | -60.75259 | 2026-03-17 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 6e418940-8527-33e6-a161-6f41710a915d | 3.19292 | -60.12812 | 2026-03-17 04:38:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7b653ec2-6633-3de4-851f-ed0804fba674 | 3.14983 | -60.72803 | 2026-03-17 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a3777ef9-56d3-32cd-9a60-e9ab9722c78f | 3.19383 | -60.13408 | 2026-03-17 04:38:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fd453fb7-19d9-375d-b442-80a69807cda0 | 3.14797 | -60.72186 | 2026-03-17 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e7f64e1-0816-3465-8b08-e50b6ed2526a | 3.12496 | -60.752 | 2026-03-17 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 8155f173-c19f-3b85-b655-babb07d4bedd | 3.14103 | -60.723 | 2026-03-17 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d4031ea4-34fb-33d6-a463-de58b7a9ace0 | 3.12594 | -60.75854 | 2026-03-17 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 064f673e-988c-324f-b3c1-0e6322d1cf92 | 3.14387 | -60.73568 | 2026-03-17 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b283129a-f385-3859-a77e-aa306a02044c | 3.0931 | -60.77722 | 2026-03-17 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab5e40d6-9ec3-3f99-a132-6f1fb92c5d1f | 3.13094 | -60.74435 | 2026-03-17 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b66e8d59-9598-3f77-9d72-91436e4c847e | 3.12692 | -60.76513 | 2026-03-17 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d6f47a7a-a788-352f-8530-844f161cf8b9 | 3.08613 | -60.77828 | 2026-03-17 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4caa5fce-9117-358d-a6eb-d38a00d79d4d | 3.19741 | -60.13723 | 2026-03-17 04:38:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e1e33250-7760-32df-b0a3-6ac2073d7343 | 2.74684 | -60.44067 | 2026-03-17 04:38:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 18f648fb-136a-3f3f-b28a-f408c0d29cca | 3.12399 | -60.74546 | 2026-03-17 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 38.1 |
| a527aad0-0673-30c6-a5f3-38d91c6939f1 | 3.12485 | -60.75914 | 2026-03-17 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 27.3 |
| f761c621-41f6-3fe5-b21d-0ece992b6157 | 3.19654 | -60.13127 | 2026-03-17 04:38:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6b1151a7-5599-37de-9d05-60751f2f4fb1 | 3.13596 | -60.73722 | 2026-03-17 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 27965025-796b-33d3-81af-291dba18d2fb | 3.13192 | -60.7509 | 2026-03-17 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 83d8d4e7-90c7-3794-bdf5-a6fd578703dd | 3.12901 | -60.73835 | 2026-03-17 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 37cf4ce5-1102-3d2a-b03b-7a257005926f | 3.14291 | -60.73615 | 2026-03-17 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 943df615-452e-3f43-af8e-ce30c7626919 | 0.83985 | -60.33113 | 2026-03-17 04:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ef419f9a-b64d-3ae3-9e2b-9b81770e0010 | 0.84165 | -60.34248 | 2026-03-17 04:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| df6f79d0-a5d9-3ae4-afe2-f08de483cca4 | 0.84059 | -60.34594 | 2026-03-17 04:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b2770e03-6481-3138-a2bd-c3904e4e7185 | 0.83973 | -60.34026 | 2026-03-17 04:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 01122b5a-3306-3172-a4ea-24597fc5c31c | -5.66734 | -45.20418 | 2026-03-17 04:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28b178da-3b02-3984-8823-2f321ae7b12b | 0.83887 | -60.33457 | 2026-03-17 04:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 207e03af-c0d2-375b-be9d-93d88a11dea3 | 0.83327 | -60.33217 | 2026-03-17 04:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da0dab1e-2d7b-3a25-aa58-c4e8c5de3e5f | -5.67116 | -45.20474 | 2026-03-17 04:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f1fffe5b-97cb-30f3-b438-1f6178b0d6d6 | 0.83416 | -60.33784 | 2026-03-17 04:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7ff3005-c7e1-37d3-bbb6-d35c0373fe27 | 1.09078 | -59.8973 | 2026-03-17 04:40:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e9c055e-c736-3a7d-84a5-6f8a0fa57ce5 | 0.84075 | -60.33681 | 2026-03-17 04:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 65659ceb-96a7-3e77-b98b-5d107fd17700 | 0.83506 | -60.3435 | 2026-03-17 04:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef6615e2-1a8f-3604-8018-925606e34ce9 | -9.5004 | -46.10487 | 2026-03-17 04:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6327990f-cc2a-35af-8ca9-2e204f0a160f | -13.66169 | -39.91214 | 2026-03-17 04:42:00 | NOAA-20 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1d6c318c-75c7-38e3-afa6-6b073c1893ef | -7.98756 | -42.83892 | 2026-03-17 04:42:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8d8a055f-c0a4-35f1-8d4c-7db1e33728b9 | -9.49659 | -46.10433 | 2026-03-17 04:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5b7979e-e6cb-3949-bab8-b25f5b441ef6 | -16.44986 | -58.1765 | 2026-03-17 04:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |


[Clique aqui para ver as próximas entradas](README4.md)
