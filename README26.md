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
| 7d1eb11e-8f4c-3e8c-b5bf-fcf6f4b714b9 | -4.99716 | -44.35979 | 2025-11-17 04:38:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0ee90be8-7201-31bd-86bd-645ad51d39c5 | -7.43332 | -48.93786 | 2025-11-17 04:38:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b54c49a-2a8e-3a02-bd58-e8ff14d4e320 | -7.66191 | -45.35603 | 2025-11-17 04:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 73e41e9d-7769-3ed0-acc3-5873b8b08375 | -7.06248 | -42.23811 | 2025-11-17 04:38:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cccef202-7e13-3f01-bad1-0e5dcd58a222 | -6.03378 | -48.18461 | 2025-11-17 04:38:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f16230e9-55e5-3e08-8d96-03f3801cabd0 | -4.97276 | -47.81153 | 2025-11-17 04:38:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ba053a2-9990-376e-bf71-93ab4cdd9277 | -3.41047 | -42.47004 | 2025-11-17 04:38:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c7f81956-f5e8-321d-80a1-12f7c147118e | -3.12144 | -50.17556 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b61ddd3-f2ba-377f-8315-cab49e11610c | -4.73742 | -46.37782 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7c6f694-4132-3afc-bd3f-8f352053ff74 | -3.07901 | -51.34262 | 2025-11-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 995136c0-b610-36ca-ac1e-bdf362b3a8a3 | -5.46833 | -40.96594 | 2025-11-17 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fe4c9d65-ee9b-35f6-bbf9-83b0c3949082 | -3.59301 | -43.59824 | 2025-11-17 04:38:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 02864124-fefe-3ccc-8a72-934590facfd6 | -6.41275 | -42.33084 | 2025-11-17 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c44ba810-b8c9-3a55-9713-9850588ed49d | -5.2002 | -46.16838 | 2025-11-17 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a69b2325-cf25-3e2e-b846-908aead2e2a9 | -8.29724 | -43.95684 | 2025-11-17 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42034dc4-deab-3fe5-9b8e-ebf827a0a522 | -3.52967 | -49.10308 | 2025-11-17 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 92c45eb2-5a18-3923-b8a8-9ab04aa14588 | -3.47298 | -54.15293 | 2025-11-17 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b660af1-c3a7-3c41-b1a2-346792e41851 | -3.18986 | -50.64774 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b8a07d2f-ad0a-3de1-8d1b-2306561a2dac | -2.7554 | -49.52503 | 2025-11-17 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 114ca80c-1c43-349b-9193-79ff4461a138 | -3.39542 | -50.19205 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40bb2a92-7c4a-3531-9aae-23b037de0e25 | -2.53437 | -48.96023 | 2025-11-17 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adf5512e-3712-3262-8f80-03ef3048dd87 | -3.77695 | -50.14139 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6dad302a-73ac-349e-90a8-1782dcff652b | -1.05631 | -52.40763 | 2025-11-17 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba29134a-8e18-305d-add3-27b5556430a0 | -3.38511 | -47.19174 | 2025-11-17 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b180148-be42-3aa8-a24b-559a492bc1ba | -3.77581 | -47.74527 | 2025-11-17 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5cb2a163-f051-3a45-a95f-55fa22fc8d90 | -3.81862 | -47.49189 | 2025-11-17 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3e11e65-94a1-3da3-814e-0ce17d0426ba | -4.31209 | -48.16789 | 2025-11-17 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a300e89e-9941-384e-80dd-0a019ecdb4b0 | -3.90038 | -45.18158 | 2025-11-17 04:38:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c1e04601-8ad5-371f-89d3-8214dce9d75c | -3.19329 | -50.64827 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a388d98c-84e1-38b4-8b2d-3af058bc5f3e | -3.01037 | -51.34084 | 2025-11-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a3d1e3df-afa9-3849-a637-4380a3360cbf | -3.16483 | -50.16386 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 23566920-4300-3b6b-b7e9-7b35f02cc47a | -3.95272 | -49.78541 | 2025-11-17 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0c6772e7-effb-3570-a1b5-7e632190dfe9 | -2.89436 | -53.29246 | 2025-11-17 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6ae69174-45da-332a-b6e7-ccf099dbc28d | -4.07639 | -46.20141 | 2025-11-17 04:38:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29e18dc9-2351-371d-95e6-df6d6cb62089 | -0.75678 | -48.64569 | 2025-11-17 04:38:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eb27967a-6467-3309-b9b1-2a80f40ad535 | -5.52628 | -40.99154 | 2025-11-17 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6b602768-3152-3c73-adba-bb843a5f8d9e | -7.86826 | -45.68614 | 2025-11-17 04:38:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 81d81c38-33ad-3d22-b4b1-6e4f4666dccb | -3.30701 | -50.21549 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64a43a8c-af6d-3fa1-b047-68b55beb0a21 | -3.18526 | -50.65461 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bf44d714-dba0-30f6-8bad-39365b82f010 | -3.60089 | -55.53807 | 2025-11-17 04:38:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b79cab39-2c6b-355f-982c-af9c6129f4f0 | -3.3988 | -50.19258 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c89b705-1f1c-3d37-a8fc-64978a7c9922 | -4.25068 | -40.10807 | 2025-11-17 04:38:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a5cbf220-ef0c-36fd-ad87-536dce9ffc1f | -4.61316 | -50.66466 | 2025-11-17 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 21c58dad-c9a5-3064-baf9-4af826bd3670 | -6.67894 | -42.03903 | 2025-11-17 04:38:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 82ef0843-fb32-31eb-8083-22c36e216f55 | -3.7786 | -47.74929 | 2025-11-17 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a70e217-17e4-387c-b08c-8852c6682b7c | -3.13302 | -50.25515 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 482e37cf-47c5-38ac-8144-cc4634fd1562 | -6.06381 | -41.54331 | 2025-11-17 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 7a20327d-ab8e-3f2d-a349-d422ce511fa1 | -6.68728 | -47.38712 | 2025-11-17 04:38:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88ffd315-6216-3151-9df1-cc77be89b4af | -3.91628 | -45.79875 | 2025-11-17 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 68737708-d9d4-3ffd-beff-40a1755741d2 | -3.22043 | -43.3593 | 2025-11-17 04:38:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3f02b37b-af49-3602-865b-6674948698d4 | -3.8381 | -42.01099 | 2025-11-17 04:38:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5991243d-86c0-3c0b-a0e0-d6d701992b73 | -5.46793 | -40.96875 | 2025-11-17 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 60651a24-bda7-3b77-a171-9545db51cc60 | -3.88609 | -47.19084 | 2025-11-17 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97267bef-106b-3745-8fc9-cdf79ec10ba8 | -3.88722 | -47.18357 | 2025-11-17 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7a9d408-b63a-34c2-9201-7e2a10ab3505 | -3.42003 | -50.35133 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8166b22-36fc-36d8-87f9-e8996439c781 | -2.96234 | -53.22044 | 2025-11-17 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6d2e551-cd6b-3c8f-b806-7d5baa532577 | -6.60471 | -44.26236 | 2025-11-17 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f5422645-f05e-33a5-a1b8-84e93e74143c | -7.96444 | -50.00254 | 2025-11-17 04:38:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 39890e61-3a86-39b2-9067-5abd8f10cdbf | -4.7042 | -46.31248 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6a95887-a913-30dc-8845-cfe0e255b141 | -5.04072 | -43.60527 | 2025-11-17 04:38:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4e4e8f59-cdff-3bcf-8394-224a33b9dd63 | -5.79945 | -43.99293 | 2025-11-17 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a516827-f139-30df-9b3c-ccce94849833 | -4.26242 | -46.40779 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88591d89-9a15-3031-988c-3fa3b11836b2 | -4.05171 | -49.0264 | 2025-11-17 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7399253-0ef6-34c2-9c29-48e5d4ec75e1 | -3.2709 | -50.77866 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b293d75a-35a1-32d9-af24-d0bf71e5a41e | -3.38371 | -50.13507 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3cfa2a61-20af-36e4-8066-767e5c414d7b | -3.58637 | -50.71628 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 514f7566-c2cc-32e5-ab44-9753212386e8 | -7.65807 | -45.35548 | 2025-11-17 04:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1892279a-61b2-3303-8d3b-269a8c559e5b | -4.33933 | -46.51008 | 2025-11-17 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9477624-ec67-31d1-902e-02d5a1a2c8ab | -3.23505 | -50.49547 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ccd40adc-0421-3dee-9886-3eabc32add9c | -4.74847 | -46.39943 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7317c096-eecf-3891-9be6-4dd8719bc61f | -6.34829 | -44.22448 | 2025-11-17 04:38:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dcd417e4-03e1-336c-be91-f602ef1b903d | -5.88613 | -46.44527 | 2025-11-17 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bd047f1f-c92f-3cec-8a05-6e09fcecc822 | -1.22476 | -46.2045 | 2025-11-17 04:38:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| afa5c63d-7c06-3ab7-a699-6b83b3642073 | -1.87358 | -46.36628 | 2025-11-17 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b6195f3-1413-366a-8c3b-ef526853fc03 | -8.24813 | -41.425 | 2025-11-17 04:38:00 | NOAA-21 | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a1d4a2d1-bea1-3de4-9f46-4102311dc823 | -3.24503 | -51.34735 | 2025-11-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6ff0836-2af2-3d06-ad39-97e0d1090ba0 | -4.61598 | -50.66882 | 2025-11-17 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41498c29-e1d0-3243-a176-104c7fc200a0 | -3.4077 | -50.26786 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e14c476b-2f2c-3f28-afb2-8a46a5093977 | -4.83995 | -45.42836 | 2025-11-17 04:38:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e7a30b5-019c-33bb-8cd4-75bb7d5cbe54 | -4.69423 | -46.30694 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6da1fed5-6f00-363c-a0bf-4bd9b80a4605 | -7.25761 | -48.01092 | 2025-11-17 04:38:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce35f97e-4c65-307e-a2f5-ba254d068bf5 | -4.99768 | -44.35829 | 2025-11-17 04:38:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 408c3b69-c726-3b71-af44-439859abc2a9 | -3.88723 | -46.45991 | 2025-11-17 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bdcf004d-6121-3945-a077-67865e1604c4 | -3.33381 | -50.27491 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 323703b6-00fa-38da-9de1-4c318f66987d | -7.2199 | -47.98651 | 2025-11-17 04:38:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| dc9f2485-ae9c-396e-a584-074ea5cc3ddd | -8.10224 | -46.05156 | 2025-11-17 04:38:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0443e226-5341-3237-8feb-6f1949b13215 | -3.51153 | -49.92845 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 15ec8754-4c2b-33d3-a4e3-1a4f11b11a0e | -7.43386 | -48.93438 | 2025-11-17 04:38:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 674b7dd5-2e51-39cb-abab-b13ee20b8487 | -6.67753 | -42.04901 | 2025-11-17 04:38:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d40cfbe6-2b49-375a-871f-3df7a8bf10f7 | -3.85659 | -49.14409 | 2025-11-17 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a443500-259d-31d1-b5f9-a6a45ab1d91f | -3.15237 | -49.16367 | 2025-11-17 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b3b745f-1e1d-376c-a1c4-dd1d3f7a704e | -3.53021 | -49.09964 | 2025-11-17 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 84dbedf7-9aae-3628-920e-fd346bedcafc | -3.32927 | -50.28162 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ac1eb28-2e0e-381e-951a-a3ca8a83fd00 | -5.92968 | -44.01261 | 2025-11-17 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 436de84d-a19f-3cc6-a183-8a0984497279 | -6.74311 | -42.94589 | 2025-11-17 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 38f76a95-249d-3fff-8d76-20561972e1ad | -3.38197 | -50.16785 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15c63069-a6c1-3fbf-b9af-d7ee9dfc463b | -3.24129 | -50.5002 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4cbe6038-c16a-3ddc-bdd4-e85efee3a8d4 | -6.68294 | -42.04477 | 2025-11-17 04:38:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 41803faa-1c06-34fa-bb15-2fa2f9992030 | -3.5904 | -50.71308 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc1cbefb-022b-35e4-bc36-006fb0734487 | -3.62411 | -44.44001 | 2025-11-17 04:38:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README27.md)
