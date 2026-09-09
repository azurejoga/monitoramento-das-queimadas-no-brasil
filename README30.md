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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73fcd87c-5249-3e90-b4ac-b04c3fea8c37 | -9.694 | -43.4688 | 2026-09-09 12:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 75.8 |
| 47ec7301-e80c-3521-8ba9-fc07274f2a2a | -9.6937 | -43.4924 | 2026-09-09 12:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| c95dab63-42bc-37c2-b8cf-d01399bfff1d | -9.6944 | -43.4453 | 2026-09-09 12:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 107.4 |
| cdd7219f-9bd5-3b0e-98d9-2556f89ec99e | -10.7186 | -46.0355 | 2026-09-09 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.2 |
| fed3411b-8cc6-343b-971e-5059488b5885 | -10.7186 | -46.0355 | 2026-09-09 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 418c1797-bfc5-31b9-b42e-5662d4ffe6da | -9.6944 | -43.4453 | 2026-09-09 12:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 103.4 |
| a72d0eb1-8d59-3de6-9e43-48413aebe1ec | -9.694 | -43.4688 | 2026-09-09 12:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 96.8 |
| d5f2b540-39c8-3241-83e1-62da0b52518f | -9.6944 | -43.4453 | 2026-09-09 12:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 112.6 |
| 8036b1d9-600e-3dce-80b3-87c24d1338a4 | -9.694 | -43.4688 | 2026-09-09 12:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 110.9 |
| d4e07322-1353-3373-a8fc-5fdf03949892 | -10.7186 | -46.0355 | 2026-09-09 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 07d64f79-e73f-339f-a165-973a98a4ee48 | -9.6947 | -43.4217 | 2026-09-09 12:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 75.5 |
| d8536dca-e967-3016-9acf-5a39fe51cdf8 | -10.7186 | -46.0355 | 2026-09-09 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 38c8e718-9226-34da-a1bc-585f52851e81 | -10.7182 | -46.0582 | 2026-09-09 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 173.0 |
| ba9f6d2f-079a-3e2a-9763-9d1c3e409824 | -6.8708 | -46.0126 | 2026-09-09 12:30:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| f14cdc7c-a4aa-3bb0-a91b-00ec3b05fcfc | -9.6944 | -43.4453 | 2026-09-09 12:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 102.0 |
| 984945e3-e897-396e-a5c0-d64bbc944dbf | -9.694 | -43.4688 | 2026-09-09 12:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 96.1 |
| af536c1b-8d45-3723-80f9-91afd277cbb6 | -9.6947 | -43.4217 | 2026-09-09 12:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 100.9 |
| f9cad561-fe56-345b-bdbe-09b55f00e2a9 | -3.5406 | -48.1889 | 2026-09-09 12:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| db12c3f1-ae03-3caa-bd24-5030ca5e512b | -9.6937 | -43.4924 | 2026-09-09 12:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| b91b989c-831a-3c08-bbf9-c3801046b54a | -9.7138 | -43.4192 | 2026-09-09 12:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 98.7 |
| 0dff36b6-f8be-3061-9663-5a6c65c31675 | -9.6944 | -43.4453 | 2026-09-09 12:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 108.3 |
| 5565c505-f7ee-3814-9387-abcad218dea1 | -10.7186 | -46.0355 | 2026-09-09 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 157.6 |
| 2b41a865-3984-3918-92a4-192bcf3cc363 | -10.7182 | -46.0582 | 2026-09-09 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 243.1 |
| aff8ad57-1f61-31a3-86db-23cc4ab35223 | -9.7141 | -43.3956 | 2026-09-09 12:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 103.4 |
| b0e8c5ba-256a-3dc1-970b-80e8cf716f38 | -9.6951 | -43.3981 | 2026-09-09 12:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 74.5 |
| a53810fd-237c-3119-a9e6-46d160e2b6d0 | -9.694 | -43.4688 | 2026-09-09 12:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 119.2 |
| 8b82e6b3-32d7-3141-a686-6e5148a1fc2f | -6.1726 | -44.6432 | 2026-09-09 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| b752adcd-6f28-311f-a17d-ec7abd29e76e | -9.6947 | -43.4217 | 2026-09-09 12:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 88.9 |
| d2776aaf-7544-3a14-ab37-dfa5ca719d39 | -10.6995 | -46.038 | 2026-09-09 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 166.4 |
| c88f7964-f8c9-357b-9b6c-7edf338a7cf0 | -9.7138 | -43.4192 | 2026-09-09 12:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 134.2 |
| ac1da782-dfc7-3003-95ce-21d248061303 | -6.852 | -46.0141 | 2026-09-09 12:50:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 5674525c-76e3-30fd-81ff-5899402b3ec2 | -3.5591 | -48.1882 | 2026-09-09 12:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| c3e08df8-45a6-3a59-aa0d-9aefd47495e1 | -9.6944 | -43.4453 | 2026-09-09 12:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 130.0 |
| 908897e2-ed4c-31bf-9031-aa56da63eac5 | -10.7186 | -46.0355 | 2026-09-09 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 3b693543-a715-3c92-94cf-28ab725256d9 | -9.7702 | -43.4589 | 2026-09-09 12:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 1d05c6e1-0752-3580-a13f-594dc3473b9b | -9.694 | -43.4688 | 2026-09-09 12:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 123.1 |
| 6ed629f5-7520-3fd6-9d47-d5fac350ffde | -6.8708 | -46.0126 | 2026-09-09 12:50:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 0f4b5538-3fff-302b-aee8-0af51f882d7f | -9.7141 | -43.3956 | 2026-09-09 12:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 112.8 |
| 6c25ca22-006c-3e13-9d76-52a5c5634724 | -10.7182 | -46.0582 | 2026-09-09 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 68361fd6-d4fc-32e4-9e10-32a6f5b078a0 | -6.1538 | -44.6446 | 2026-09-09 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| d5b23cb1-97b1-3aaa-abbe-b8e59b0e0e4e | -9.6937 | -43.4924 | 2026-09-09 12:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 4dcc17f1-e5f6-3036-8f21-96b9d3bc55a3 | -9.694 | -43.4688 | 2026-09-09 13:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 116.1 |
| 3fd40d0f-7760-3526-9db9-4fe1483c41f2 | -9.6937 | -43.4924 | 2026-09-09 13:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 926c3d9e-5c3e-3556-8950-7fa2937a3689 | -9.7138 | -43.4192 | 2026-09-09 13:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 117.7 |
| cafb5c6d-2f40-3159-a523-2d21978979b1 | -9.7702 | -43.4589 | 2026-09-09 13:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 8b831eeb-caf2-3bea-8590-adfaa167748a | -10.2372 | -45.2087 | 2026-09-09 13:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 9e9973fb-97cf-3b5e-bc47-97de7c275a55 | -10.7182 | -46.0582 | 2026-09-09 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 1d7e326a-4b51-3022-a863-98dc84228f48 | -10.2563 | -45.2062 | 2026-09-09 13:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 110.1 |
| b810c7b2-8006-3a09-8f36-d81601d3bb85 | -10.2559 | -45.2292 | 2026-09-09 13:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 03e53990-cb8a-3ee6-8855-2cdf1b5335ee | -12.5834 | -45.4516 | 2026-09-09 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 969b9603-ccb9-329c-b6af-6e4ceed2a977 | -3.2731 | -50.0741 | 2026-09-09 13:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| b1aa46ae-be09-34f2-bbd4-a5c2c4b3d8f0 | -9.7141 | -43.3956 | 2026-09-09 13:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 120.9 |
| c7c5b897-fff7-3f1e-8050-25528e0850c6 | -9.6944 | -43.4453 | 2026-09-09 13:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 145.5 |
| 3dfbdd4b-8244-32f2-87e8-1b05af08c770 | -10.6995 | -46.038 | 2026-09-09 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 154.9 |
| 15e370c5-5802-37c1-abd1-d05d548a853b | -10.7578 | -45.9624 | 2026-09-09 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 4f47f81f-2591-385f-a3b8-8495703a033c | -6.1726 | -44.6432 | 2026-09-09 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 89e9b526-56ae-39e1-a45d-c80518a53210 | -9.7889 | -43.48 | 2026-09-09 13:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 0a273c29-b6bd-34a3-a32a-42530e48c53b | -9.6947 | -43.4217 | 2026-09-09 13:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 98.1 |
| 038663aa-42ab-3ecf-a6b3-952cb364f744 | -6.3304 | -43.8253 | 2026-09-09 13:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 0f2cafd9-b634-3cc6-8d7f-d0f14c382af5 | -10.7391 | -45.9422 | 2026-09-09 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 89dfa2bb-e088-3c36-bd73-8ce0160e0c35 | -6.8708 | -46.0126 | 2026-09-09 13:00:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 143.4 |
| b02ec87c-30b8-3e2f-af63-ffe03488d00a | 0.65119 | -58.20141 | 2026-09-09 13:04:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 486a05f7-e50c-3abf-a082-4976db323435 | 0.65243 | -58.19582 | 2026-09-09 13:04:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 3425b764-33d3-36ca-bac9-3f8c2b617d31 | -6.89956 | -62.95649 | 2026-09-09 13:06:00 | TERRA_M-T | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 599b5de1-2fc8-370b-ba8b-36e2d0a34761 | -6.56449 | -62.88833 | 2026-09-09 13:06:00 | TERRA_M-T | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 8a039bda-d764-3330-8e92-063152007a84 | -6.56395 | -62.8941 | 2026-09-09 13:06:00 | TERRA_M-T | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 243bea7f-3aef-35f0-ba9d-4f98fc50c195 | -6.56245 | -62.90325 | 2026-09-09 13:06:00 | TERRA_M-T | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 181d49be-770a-3b7f-8360-c5616e5d2055 | -5.77539 | -60.40079 | 2026-09-09 13:06:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 6d55cd6d-82fd-3fd8-8740-31d06aabd089 | -9.23911 | -65.7511 | 2026-09-09 13:08:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a9133ce7-1fa2-3f22-a0a5-2f9aad5af1d0 | -10.12041 | -67.5137 | 2026-09-09 13:08:00 | TERRA_M-T | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f79680a6-b8aa-352a-981f-ff160bc00d9c | -12.5834 | -45.4516 | 2026-09-09 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 722c429a-01ed-3321-9fbe-feb9ae705162 | -9.694 | -43.4688 | 2026-09-09 13:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 117.8 |
| eae07adb-8b5c-338a-a22d-3c3c40a163e3 | -9.6947 | -43.4217 | 2026-09-09 13:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 157.7 |
| ac56a8b4-fbbb-3b2f-9a7e-0d0876e17969 | -9.6937 | -43.4924 | 2026-09-09 13:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 120.4 |
| f810b42f-f640-3293-ad6a-3297d635420e | -9.7141 | -43.3956 | 2026-09-09 13:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 118.2 |
| 252a2314-c650-31fe-88b2-f3e62bb3f8f0 | -6.852 | -46.0141 | 2026-09-09 13:10:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| f216a441-dcb6-35f0-bbe7-7e99286127c9 | -3.2731 | -50.0741 | 2026-09-09 13:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 9444b1f7-ebcc-3eb6-9241-6c557ae635a5 | -10.7391 | -45.9422 | 2026-09-09 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 777aeef4-785d-33af-a824-3cd9bddbf956 | -6.1538 | -44.6446 | 2026-09-09 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| bd72562d-a16c-3dec-91ba-321ece7f5502 | -9.6944 | -43.4453 | 2026-09-09 13:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 212.7 |
| 25b9b358-dc0d-3c5e-95f2-a630231a7d9b | -10.6995 | -46.038 | 2026-09-09 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 174.6 |
| de405447-1e7d-3883-8eca-c459708034d2 | -9.7138 | -43.4192 | 2026-09-09 13:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 147.8 |
| d0d76315-aa1d-3d6d-9f39-1c4108c18d72 | -6.8708 | -46.0126 | 2026-09-09 13:10:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 154.5 |
| beaff1b6-fc8b-380e-b95a-1da422b22ce3 | -3.5591 | -48.1882 | 2026-09-09 13:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| a8cfa1bc-a141-389e-87d0-732c719f9406 | -10.7391 | -45.9422 | 2026-09-09 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 22af8cad-5ee4-3d68-a198-d8b129841999 | -9.7141 | -43.3956 | 2026-09-09 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 112.9 |
| 5545d277-95a3-30a6-a2aa-b50310c8c8b4 | -9.6937 | -43.4924 | 2026-09-09 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 127.2 |
| b1b1aad8-db23-3524-9019-1fd0aed720b9 | -9.6947 | -43.4217 | 2026-09-09 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 112.6 |
| 189f338d-674a-3a08-9673-da3c53d26a95 | -6.1538 | -44.6446 | 2026-09-09 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 932d5238-af24-3c4d-9bae-8376fbb77a65 | -3.2546 | -50.0747 | 2026-09-09 13:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 799207f5-c6a5-3f98-ab1f-3e0bb87e702a | -9.7138 | -43.4192 | 2026-09-09 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 141.3 |
| 6da7b8f3-da82-32a5-ae11-7fcd2974732a | -9.7131 | -43.4664 | 2026-09-09 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 8411bc5f-adeb-3a33-99b7-80ffc1ee23e7 | -9.6944 | -43.4453 | 2026-09-09 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 152.7 |
| ae9e038b-9f94-3b43-a691-adf99d00811f | -10.2563 | -45.2062 | 2026-09-09 13:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 84.9 |
| afaa125a-e2b8-388c-9b78-b9a32fe0d196 | -6.8708 | -46.0126 | 2026-09-09 13:20:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 9c9b8308-c794-3803-b930-eba0ff36efb7 | -10.7578 | -45.9624 | 2026-09-09 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 155.7 |
| 7953312b-970e-3f26-9b92-7b5dc68ee46f | -10.2559 | -45.2292 | 2026-09-09 13:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 4f75ef23-e031-3243-a0e9-14465ac0ffe2 | -6.852 | -46.0141 | 2026-09-09 13:20:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 1d64b513-91b2-30da-a85b-2fe9f4d4da55 | -10.2372 | -45.2087 | 2026-09-09 13:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 119b96de-775c-373f-9eff-e1c593357df3 | -9.694 | -43.4688 | 2026-09-09 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 123.9 |


[Clique aqui para ver as próximas entradas](README31.md)
