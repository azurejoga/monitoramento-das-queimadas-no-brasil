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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5363839b-7562-3a20-8bde-ad864ff861e4 | -12.6531 | -56.9909 | 2025-09-03 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 45.1 |
| dce23c26-fa52-3692-aa91-f91681702f4c | -6.4462 | -49.5163 | 2025-09-03 00:20:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| fefbf8a9-10f0-38d1-a9ea-8047eaf06d3a | -9.176 | -45.1993 | 2025-09-03 00:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 84.3 |
| afd3d603-ef14-3e82-b194-efd86a568b1b | -3.2305 | -47.135 | 2025-09-03 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 183.0 |
| ff283afa-504a-364a-be9f-d8038b153973 | -5.6081 | -45.0038 | 2025-09-03 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 1a42d188-8698-348b-97a1-03cbfe9eb728 | -20.8886 | -50.0937 | 2025-09-03 00:20:00 | GOES-19 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.7 |
| aa9746eb-5c85-3235-84ea-a59f6c2139a4 | -7.7036 | -48.7587 | 2025-09-03 00:20:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 68c40908-7b44-32bb-b2c6-3781ec68e82d | -3.212 | -47.1357 | 2025-09-03 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 138.5 |
| b4768e20-6a72-33f4-a6b2-cf5237c15ec6 | -7.0964 | -63.0625 | 2025-09-03 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| f66afb1c-9236-3cbb-9f98-77943aa3c7dd | -9.5043 | -48.8978 | 2025-09-03 00:20:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 65660a92-9e08-32ac-9649-ae348059362d | -18.1514 | -51.75 | 2025-09-03 00:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 1378d5c8-034b-3e71-8d72-97f80a63e4ff | -5.6266 | -45.0252 | 2025-09-03 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 42d7247e-f0f5-39cd-b246-99eece4b0db5 | -7.3357 | -59.6484 | 2025-09-03 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| c561db50-13cf-3ec4-99d4-c748fc2e61a3 | -9.3394 | -55.2277 | 2025-09-03 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| f54215c5-24cb-301e-aaf6-2145ecfadce1 | -7.7039 | -48.7371 | 2025-09-03 00:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 27b52bc5-8524-314a-a57c-0512717ec30e | -3.2121 | -47.1138 | 2025-09-03 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 473a4e02-339b-38e9-8b2a-cb4ea8f2a868 | -8.3646 | -48.2899 | 2025-09-03 00:20:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 1f17349b-d0d7-35f1-b9bc-fda5d8ede7fa | -10.0932 | -54.7667 | 2025-09-03 00:20:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 946a1f6d-fa96-3f32-bcd2-d5c4fb5949eb | -12.6341 | -56.9926 | 2025-09-03 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 8196e4ee-1644-3b17-985e-b31438e62e15 | -6.4648 | -49.5151 | 2025-09-03 00:20:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 130.2 |
| 584c96e4-f85d-3b0b-bf74-dcd72935e134 | -17.941 | -47.1718 | 2025-09-03 00:20:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 16e50d54-5daf-31ef-a2f8-e10e081cfba4 | -6.4402 | -58.138 | 2025-09-03 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 0a1ff7d5-9871-3f8f-9fab-407df3dfaeae | -12.6339 | -57.0127 | 2025-09-03 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 5bfeb47b-18ae-3c27-a153-8c585b19392c | -5.6268 | -45.0025 | 2025-09-03 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 866d156d-e99c-3859-acfb-c6cdfddc55f7 | -8.3834 | -48.2882 | 2025-09-03 00:20:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 52d1a839-1ec9-31e9-ab7c-3852d267025e | -11.1224 | -44.6521 | 2025-09-03 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 8bc24801-1edf-3315-b6da-9959c6ea7fe1 | -3.2306 | -47.1131 | 2025-09-03 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 4c4b25ef-35fd-34ec-807c-21292b22f34b | -10.4853 | -50.346 | 2025-09-03 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 22646ef0-a714-3d5e-add2-cd9c82b7df15 | -10.45 | -54.7785 | 2025-09-03 00:20:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 7cde0126-8ea2-33f3-b2c1-9db44677f920 | -9.1949 | -45.1972 | 2025-09-03 00:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 6238241e-14b8-3a5c-b2ac-ba26c2fe119b | -6.4646 | -49.5364 | 2025-09-03 00:20:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| f5bc1d3d-7989-36bf-8886-722169251d21 | -6.2701 | -44.505199 | 2025-09-03 00:24:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1b202be4-3e93-346a-a921-48bab8ca08da | -4.7751 | -45.316799 | 2025-09-03 00:24:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94318604-72a1-33ad-978a-1769bcb677b7 | -12.8652 | -48.026001 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fd252e18-2096-30ba-8847-d0b58761f58f | -6.4072 | -43.757 | 2025-09-03 00:24:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 389b66d8-d9d7-3fb2-9151-b56cc06647d3 | -9.5108 | -48.895401 | 2025-09-03 00:24:00 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 03ba5fbd-433b-3710-a107-751b8779206b | -7.885 | -46.444901 | 2025-09-03 00:24:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fabe0d58-0ad7-3412-adf8-a98680bff8f9 | -7.903 | -46.479401 | 2025-09-03 00:24:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cc899edd-0ffe-36a9-ac69-34a18fa522bf | -4.1607 | -46.780399 | 2025-09-03 00:24:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e4ff1e27-f222-3a56-97ef-73e16b30ba5b | -5.4977 | -42.640999 | 2025-09-03 00:24:00 | METOP-C | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9d0d5e48-d1a0-3abf-8e1a-4db54ee3d42b | -6.9454 | -43.273899 | 2025-09-03 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b587e787-bf44-3838-bb54-fa01e05b037e | -9.6145 | -47.856899 | 2025-09-03 00:24:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 592da080-2cf8-3ac0-b932-3f4bd504b743 | -6.7055 | -48.396999 | 2025-09-03 00:24:00 | METOP-C | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| b19b3419-c19e-31eb-8901-9ed519cbaab9 | -14.5749 | -48.048599 | 2025-09-03 00:24:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 82cb2aca-568c-3b74-962e-d100db51df5c | -15.5445 | -48.359402 | 2025-09-03 00:24:00 | METOP-C | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| eb7204d2-aed1-3eac-a6e3-5a72c8b4654c | -12.5848 | -48.2001 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b509bd92-7eb4-341a-8fa1-b1484910ebdd | -5.6034 | -45.015999 | 2025-09-03 00:24:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 62d1c19c-6906-3a6d-a207-76e2563c3140 | -11.1203 | -45.124599 | 2025-09-03 00:24:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1e551b31-82af-3ec8-94f7-461e24be3e80 | -5.8383 | -42.9953 | 2025-09-03 00:24:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 322094d1-df14-3547-bac9-e3517ac4cbd7 | -8.0058 | -50.079201 | 2025-09-03 00:24:00 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc43d162-5731-3225-aed8-9f265269b9d9 | -15.1215 | -48.180099 | 2025-09-03 00:24:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2a1457be-83dc-3be8-aa05-6e92be7de26a | -9.141 | -49.652599 | 2025-09-03 00:24:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3ceef852-a218-3162-9ef8-4c37d6fae9b0 | -7.1112 | -44.755299 | 2025-09-03 00:24:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d20be3c8-29f6-3c51-9343-a1a8f7af1be5 | -7.7028 | -48.731098 | 2025-09-03 00:24:00 | METOP-C | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| b4fa8be9-210b-3b8e-b5b5-dce0f0476058 | -6.6997 | -44.175499 | 2025-09-03 00:24:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d48a31c5-c6e0-36fc-b9ac-ee3c31020493 | -6.3575 | -43.0093 | 2025-09-03 00:24:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3127cb43-bf88-3450-8ce6-f3e72a03796e | -6.4506 | -49.520401 | 2025-09-03 00:24:00 | METOP-C | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2becb195-8a52-3e1d-ab03-94b1377697cf | -11.3911 | -43.6278 | 2025-09-03 00:24:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 60b983b2-844a-3a02-ad61-bc80845a11ca | -14.6298 | -48.924999 | 2025-09-03 00:24:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6dfc8074-3d5c-3b42-ba39-033a5fe47ef3 | -8.3581 | -48.304501 | 2025-09-03 00:24:00 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0c470bd5-b977-3e8e-8e13-3679f1a40b31 | -3.2202 | -47.1306 | 2025-09-03 00:24:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bde2019c-5b3f-344f-919e-1af5e0227318 | -6.7036 | -48.3885 | 2025-09-03 00:24:00 | METOP-C | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 692f38f6-88d9-3f81-97bb-f9f6dc9ccb73 | -11.1025 | -44.630699 | 2025-09-03 00:24:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bbaf68a3-12cc-3ef6-b738-f267eb573720 | -8.1968 | -44.813499 | 2025-09-03 00:24:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0ffe0b2d-191c-37eb-8c0d-86f06b2ab401 | -11.1041 | -44.637699 | 2025-09-03 00:24:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5af9ef36-bf83-3eac-a638-b037c50be09d | -5.8964 | -46.165699 | 2025-09-03 00:24:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d0be813f-381e-35d8-9d90-b91a800a29f5 | -6.11 | -47.202702 | 2025-09-03 00:24:00 | METOP-C | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e2b25266-fced-3bc9-86ba-546a4a847c5e | -11.5984 | -52.143799 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b1308630-b8e9-3c46-afc5-20eba2790bf6 | -7.5344 | -47.455502 | 2025-09-03 00:24:00 | METOP-C | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ece60d47-a3b0-300f-89b8-3d1ff2a1a68c | -9.7316 | -49.402401 | 2025-09-03 00:24:00 | METOP-C | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f10f0930-3abd-3ccf-8493-6a6581d19bec | -11.5817 | -52.1106 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bd72124e-53de-334d-ab48-fa61935ab1c6 | -6.7947 | -52.8036 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbfdc31d-33b1-3009-b983-d707f4d8e6bc | -12.8533 | -48.0182 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fb3d42ae-9824-3742-9001-8511cb55ce89 | -9.1289 | -49.643799 | 2025-09-03 00:24:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c7fe97ae-f3ce-359d-a682-1ab34f365253 | -8.0062 | -44.7915 | 2025-09-03 00:24:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a5b102ba-2992-3e73-a237-b78b9234ff59 | -5.7643 | -45.403801 | 2025-09-03 00:24:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ede1f4eb-0b4b-3ac2-a144-cdbbd9125939 | -6.5403 | -42.951599 | 2025-09-03 00:24:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9c02de64-6d37-38bf-8e8a-bfa8d613286e | -10.9445 | -50.765999 | 2025-09-03 00:24:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 11b1bf09-1026-325e-a11c-bf5501d15674 | -6.4485 | -49.510502 | 2025-09-03 00:24:00 | METOP-C | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5423441-ea33-333e-bbf5-e53b4cdb49a0 | -7.4775 | -44.8241 | 2025-09-03 00:24:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4ed1ceaf-3ff3-3874-a358-7de99d4f3b4d | -7.9226 | -46.475101 | 2025-09-03 00:24:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f51eb7ec-b2d0-38dc-9105-bcd3402311d2 | -3.3974 | -44.260799 | 2025-09-03 00:24:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a2064232-8768-395b-9692-d2566b766cd5 | -10.1288 | -47.438801 | 2025-09-03 00:24:00 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f5af70bb-8942-356d-8d82-28f8ba9c4420 | -6.9481 | -42.9744 | 2025-09-03 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a369076c-acc0-3163-a40d-375f4fc2c959 | -11.0473 | -45.397701 | 2025-09-03 00:24:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ef0d83d8-9b5c-341f-a812-d1324c063572 | -6.253 | -42.605202 | 2025-09-03 00:24:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cc8f9011-0233-33a3-9e19-baea6a9764ad | -6.8477 | -45.544201 | 2025-09-03 00:24:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2f118469-b2c0-3a20-8db4-a3867abe2ed2 | -7.8883 | -46.459499 | 2025-09-03 00:24:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f640782c-847d-3f58-a5de-4a65713e4336 | -9.7413 | -49.400299 | 2025-09-03 00:24:00 | METOP-C | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c716a5a7-0499-354a-ac00-50e1d8bbbf2b | -8.0222 | -44.0494 | 2025-09-03 00:24:00 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1b01a4b4-43b1-355b-aa51-b1fca818fa34 | -2.1329 | -48.011299 | 2025-09-03 00:24:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a77c6704-4439-3f8c-a4ce-c1dd7bc83248 | -13.0034 | -48.101002 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b804ce88-1a3d-3a5e-8f98-1db02aedaf0a | -4.8404 | -42.742802 | 2025-09-03 00:24:00 | METOP-C | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8b8da249-4549-3f46-8b8b-c7dac36bba65 | -13.5025 | -47.0172 | 2025-09-03 00:24:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c4087b38-76d1-398c-9c48-eb168fbbe636 | -5.8045 | -45.625599 | 2025-09-03 00:24:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 71e5b97c-596b-3060-8bb2-43da95f52df7 | -10.4789 | -50.335201 | 2025-09-03 00:24:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 56648947-353c-392b-9fc8-eca99d8716e8 | -4.8502 | -42.740501 | 2025-09-03 00:24:00 | METOP-C | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 230251a9-de14-3a78-9335-a8527cd3653f | -5.6049 | -45.0228 | 2025-09-03 00:24:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 89d885e6-57bb-3794-95b6-29b2b580cef2 | -11.6304 | -52.100899 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 93807280-c850-3deb-a3b3-8c069fd5e03f | -11.5942 | -52.071701 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
