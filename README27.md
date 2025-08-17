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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3389a56-f4d4-3054-a6f4-b40a363b3ccd | -14.54993 | -52.0336 | 2025-08-17 05:06:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd8cfc2d-ed15-3c1a-8983-665a83dd4ea8 | -10.84184 | -45.36151 | 2025-08-17 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ba5c6fc-3a24-3e1d-a92f-d085baaa0402 | -13.43236 | -45.8916 | 2025-08-17 05:06:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 45c07cdf-7513-33f9-a003-3239bba2a8a3 | -9.00117 | -60.53617 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8bf64337-911d-3063-9fca-bd44d092a4d5 | -10.88401 | -48.49766 | 2025-08-17 05:06:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1fca4549-4c1d-3b31-a224-b4f8ceee3a8b | -9.16715 | -59.61812 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7d77cff-4d5b-3db5-b86b-a60f7a3c5823 | -11.36037 | -55.39673 | 2025-08-17 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 977213f8-ea86-3066-aab6-9a6a3755baf3 | -9.15711 | -59.61223 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 094fd547-21b1-3ab8-8e2b-6ba4902a346a | -9.1374 | -60.74316 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 84b77e59-f55d-3841-8439-ca05f648dc7b | -8.24151 | -61.4704 | 2025-08-17 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 83ff9c87-1a50-3a0f-bf40-a6d69e4401bd | -12.89651 | -46.13046 | 2025-08-17 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05a59ddd-fe68-33ef-8d7c-034f0b8b61ae | -8.80255 | -52.07871 | 2025-08-17 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 46ad8535-9a98-3bab-a459-b1c0363ffbc6 | -10.86318 | -45.32913 | 2025-08-17 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44694419-b3c8-32dd-9340-d21a8cc18a60 | -9.69679 | -46.2624 | 2025-08-17 05:06:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 84ac5ada-9feb-3778-8a8a-3b2c034e3c96 | -13.58954 | -47.77809 | 2025-08-17 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1c80408f-2de7-3323-b5de-9a6a77fe4c31 | -9.51764 | -60.53601 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d479b270-d91e-3b8c-b1b2-b9eb1e79f107 | -9.55439 | -63.65966 | 2025-08-17 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bce5bd93-c375-36c5-8274-d2b97ad893b0 | -9.50719 | -60.52954 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4188acf2-34f6-3f35-a5dc-570ce808b5cb | -8.79867 | -52.07822 | 2025-08-17 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d48c6278-8359-36fd-a63e-05eaca31e181 | -12.57561 | -47.04674 | 2025-08-17 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98224744-13a2-32b5-9305-36ab7a5e0d76 | -12.1443 | -47.91185 | 2025-08-17 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ba44e691-f26b-32a7-8740-5524232659e5 | -10.85693 | -45.32842 | 2025-08-17 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c87c7367-001c-37df-b0a1-38ce7e394958 | -10.12585 | -57.77199 | 2025-08-17 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52eae408-0975-326a-9014-0a95a57a1149 | -13.60119 | -46.89802 | 2025-08-17 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9375e1d-a4a5-32e7-bdf5-3b4e772734d3 | -9.21966 | -59.65643 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0bd4a5d7-d996-3a74-a222-78ec26972b58 | -13.59666 | -47.76508 | 2025-08-17 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c0bc0e15-2652-3472-8225-53f73cece6c2 | -11.36321 | -55.40094 | 2025-08-17 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 64b7f332-3b3d-36ec-a89d-913d9ce54c40 | -9.21676 | -59.65168 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c69e95ca-443d-345a-9f3b-444ff19337d2 | -13.60427 | -47.74791 | 2025-08-17 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61785b2a-7f20-35c5-92fe-eea101fcb143 | -14.58949 | -47.94782 | 2025-08-17 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87f21618-cfb1-3660-9fb1-a22d0dccaf54 | -10.30891 | -54.16108 | 2025-08-17 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b58c568f-6f3f-3b67-8c02-9b5ba00b307a | -12.99859 | -56.86905 | 2025-08-17 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2df8b155-3bfd-30f0-913f-928ff977892e | -12.50352 | -57.77592 | 2025-08-17 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc00aae5-b1cf-3022-bd8a-814248e35188 | -12.13822 | -47.91705 | 2025-08-17 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 49972b87-983e-3b9e-8364-28dab32b01d0 | -13.00964 | -56.86354 | 2025-08-17 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a706fb9-d114-3da8-98c0-2d41a013a5ae | -9.14065 | -58.30129 | 2025-08-17 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea540f5e-9891-3196-87c8-cc594955f7e3 | -9.99591 | -65.28695 | 2025-08-17 05:06:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 707d354e-92db-3d98-990e-4b38ed94f8f0 | -8.99004 | -60.50714 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99b321f7-fa4f-3889-9449-872af646e8a2 | -9.18844 | -59.68947 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| abf4db1b-73dd-39f4-bdd4-71ac1ea0a88a | -8.98475 | -60.53926 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c7fb38e-7750-31ec-af22-b3e691bd25f0 | -12.81847 | -45.9897 | 2025-08-17 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34564d65-44f4-3b85-b641-37c8ef4dfe47 | -8.87541 | -68.50714 | 2025-08-17 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 51a7c00f-07a7-3e09-a8b0-414f05a384ea | -11.36377 | -55.39724 | 2025-08-17 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d38d08bb-0016-3753-9904-ecdddd5db8f2 | -14.55414 | -52.0342 | 2025-08-17 05:06:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ffd37b1-0455-3392-985a-5ab539bb2913 | -9.18813 | -59.64679 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 90194c02-b87d-304a-a570-6f5a067eeb1c | -9.51092 | -60.53019 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| f9b1ae00-a80d-38b4-a035-796ae004a3ee | -13.60691 | -47.77338 | 2025-08-17 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d84b3b9-439e-382d-8ec7-47bfcb493169 | -14.59415 | -47.95716 | 2025-08-17 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5208b27a-10dc-3dd6-9d8b-7b6fad3861e5 | -9.18745 | -59.65092 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 70070281-afec-337a-a594-0c72b26be916 | -12.13933 | -47.90767 | 2025-08-17 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e0b79124-72bd-379b-82d1-dc7df5e81605 | -13.00355 | -56.85893 | 2025-08-17 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31b02c2b-86c3-3706-a2f6-2dc581a46d31 | -14.59967 | -47.95801 | 2025-08-17 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a74f91e8-e451-3d4c-aff1-238fa09f8da3 | -9.14611 | -58.2943 | 2025-08-17 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff7a0805-b1f4-3624-9c1e-540143227da7 | -14.58939 | -47.94997 | 2025-08-17 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 026f95be-a05b-379d-943c-5dbeabfd8a75 | -9.92684 | -60.46394 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 190e509c-e144-30b3-8d7f-6db6e24efaed | -13.42549 | -57.03197 | 2025-08-17 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8844e2f2-0087-3be6-b977-70cd7c21d06a | -13.15963 | -55.71136 | 2025-08-17 05:06:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 389b4a54-e1df-34fe-b0c1-d4faa4a4f06e | -11.3655 | -55.40887 | 2025-08-17 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 692d0717-be9f-3779-8f13-f917d1704d4b | -13.61306 | -46.8981 | 2025-08-17 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 9d489a8c-8b55-3a07-a62e-885b84c1c766 | -14.71922 | -49.45577 | 2025-08-17 05:06:00 | NOAA-21 | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f10a3134-48b1-36d9-b432-a63e2462df63 | -9.63656 | -50.89171 | 2025-08-17 05:06:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57f3a730-4c07-3f6c-8371-619eb4f4081d | -13.87705 | -45.55153 | 2025-08-17 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f0cd9fa9-56c8-3fbe-a9b1-94db967cf2f2 | -10.11032 | -57.76221 | 2025-08-17 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 87b71294-4fc8-356c-85b2-0d281fdc545f | -9.16083 | -59.63396 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eef98068-3542-3ce3-bc58-33e2fe325ca0 | -8.97652 | -60.49546 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| fc565a0e-d715-371f-abad-f3bdfe77905c | -8.99906 | -60.49921 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 150a3f79-efe9-3c95-9299-504910dc6356 | -14.60491 | -47.96064 | 2025-08-17 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 973ab4fc-31a7-3231-b359-66f48da2f764 | -8.97576 | -60.50003 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b3277c7b-e3ed-3bc7-83b3-ef081710003a | -12.93284 | -46.96443 | 2025-08-17 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a45864f9-2a9f-3625-86ba-67d7b7b52eb5 | -8.09165 | -54.9887 | 2025-08-17 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cad2f4b0-2b84-3358-9080-566f58986fff | -9.86113 | -65.26064 | 2025-08-17 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9af5df4f-f239-3a42-826a-a37ce1494500 | -10.83506 | -45.36528 | 2025-08-17 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f384af64-2043-3e0f-b8c0-cedb120ebc65 | -9.50497 | -60.51982 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 776020da-e1de-3e6b-9d31-01568a55c748 | -12.13859 | -47.91399 | 2025-08-17 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 75c7c03f-23d5-35cd-85dc-cc3a4765560a | -11.25805 | -56.71714 | 2025-08-17 05:06:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e166f74a-a369-3f4c-a84c-6f9841fa7c71 | -12.12556 | -47.90749 | 2025-08-17 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 143f11aa-a945-3fe6-acb5-1f03e49efb50 | -12.78903 | -60.15692 | 2025-08-17 05:06:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 8a8f7b02-d253-32e0-a374-3a296e4e4b73 | -9.15931 | -59.62103 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fbc3d0b-ec74-343f-9a91-6798dc17d349 | -13.43267 | -57.02948 | 2025-08-17 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfcde89d-4254-3af6-921d-3b39d1311eb1 | -9.17073 | -59.61872 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0bf678e8-2113-37d6-9e10-857d4ce20bd5 | -14.18906 | -45.32838 | 2025-08-17 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a530289-7604-36de-9527-0d53a4501349 | -9.20334 | -60.83475 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02ce0012-42d3-3d5a-921c-8216b25854dd | -13.43544 | -57.03357 | 2025-08-17 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9e025a1f-b581-3e35-850c-4afd25d922de | -14.58901 | -47.95318 | 2025-08-17 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8aa4f9c6-ec66-3849-aa3f-4559e313afd4 | -10.84303 | -45.35167 | 2025-08-17 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| ff11221c-6dfa-333f-b460-3996bc5dd3ff | -9.39205 | -60.54474 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f30fbe6-8926-353d-966d-e9c050b7d835 | -8.99681 | -60.53651 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76713bfe-a4d5-35de-9607-ec50d9cf9d83 | -11.90003 | -43.43202 | 2025-08-17 05:06:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9b3e7a40-1687-3518-b448-bd66e4c63b05 | -12.89655 | -46.1207 | 2025-08-17 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce0b8b96-8a1e-3c5e-8f5b-3c62f96f10e5 | -10.31655 | -54.15819 | 2025-08-17 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e4c99337-7f60-3aa4-921e-cc12960a8b97 | -12.20674 | -47.24845 | 2025-08-17 05:06:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bf9dd18-ca63-3544-84da-fa03fcfb51a1 | -14.59462 | -47.95224 | 2025-08-17 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53cd7414-d8c5-36a5-9689-242914bf64a5 | -8.79934 | -52.07345 | 2025-08-17 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 712bac7c-acf0-30df-8ea5-f6fde27630a7 | -9.16042 | -59.68059 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c7311d4-58ee-342d-a338-e05ef402292b | -11.35587 | -55.40362 | 2025-08-17 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1cfbfc5-b0a8-3080-bd95-c91733e5a835 | -8.99898 | -60.52634 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae8acf11-435f-3dc0-b262-ceb732408497 | -12.89145 | -46.12029 | 2025-08-17 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2c8d2edf-fde1-3966-9877-53e0aafaa2df | -13.57318 | -46.98888 | 2025-08-17 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2ccbfd3-e465-3774-a2d6-a63e0afe1659 | -10.35795 | -64.50535 | 2025-08-17 05:06:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d4998c2-a508-3a30-9b80-88bb0d302404 | -8.98909 | -60.53893 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README28.md)
