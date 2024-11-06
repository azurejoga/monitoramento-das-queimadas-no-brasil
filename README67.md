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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ea62ab2-cdfd-3afb-8f57-8bf3859de05d | -3.2297 | -54.86039 | 2024-11-06 05:31:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5e7b70b-1ffa-3f5e-bfd8-92210444eaed | -2.60635 | -51.30692 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e849561-b501-341e-aa3f-58d7530a233b | -3.06779 | -47.77384 | 2024-11-06 05:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d814b189-4b5b-3ba6-b038-c6a2da46acfb | -11.78925 | -64.84483 | 2024-11-06 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6232466-8f00-35e7-8df8-cb619d3b9aa1 | -2.38669 | -50.32365 | 2024-11-06 05:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1aa68ae2-c06e-33a2-a472-88033fc63e72 | -2.7601 | -53.21383 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 167fd791-99b9-359f-b2dd-db8c76cd0701 | -9.58304 | -65.98109 | 2024-11-06 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b091b1af-6d52-38be-b8a3-9fa3a555b010 | -3.17357 | -54.4739 | 2024-11-06 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5dae19ae-f9db-3f4a-aefc-cb5ffd5ff01a | -3.45179 | -50.37238 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 02fb4957-48a3-351e-b380-91f4edd3731e | -3.16811 | -50.20959 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 357a145d-b380-3f0f-b6a5-f1e4fc03d442 | -2.7543 | -53.21851 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bdb46812-739c-3b77-b33e-ff83f5c55fc2 | -2.85826 | -51.77982 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 27dc79d1-d75e-39d1-9ce5-bd742dc1efdd | -1.49138 | -60.37763 | 2024-11-06 05:31:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25e82199-40e3-3998-99e4-bf004682200b | -3.01834 | -53.43621 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| f8d26633-47c4-3cb9-a87c-4225842bb3c0 | -2.81196 | -52.93364 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a9b6d109-49eb-3d9b-9e7a-2932811c536c | -2.8229 | -49.78036 | 2024-11-06 05:31:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bfc5ead4-1d3b-39b7-abd6-75fecda11c77 | -2.977 | -53.27234 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6846e9e9-2feb-3a80-b856-fc168163606b | -11.82513 | -65.01947 | 2024-11-06 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdeb892a-6579-390c-99ae-4f56960635a7 | -2.81523 | -52.94675 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0cf92f2d-ed61-3679-8ca5-824b9564790e | -2.72719 | -51.71204 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7d36b63-2912-3b8c-9941-0ad4d87250c8 | -3.02815 | -53.27193 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 0bf32598-65a4-39d9-8575-0e7b20a1f8de | -3.01337 | -53.43563 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| fdb5af95-3689-33b1-a76b-9d8e9e311310 | -3.10121 | -54.29147 | 2024-11-06 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ab2161f0-cb38-3b86-a17a-4a73e8cf0c92 | -9.74659 | -68.44431 | 2024-11-06 05:31:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a0a481b-2192-3379-9009-835a4959d1b6 | -2.5258 | -51.16474 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbf44782-bf09-35c8-beae-4b5e34200019 | -1.33537 | -60.22177 | 2024-11-06 05:31:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70a8f191-d2d2-3016-aba7-87b1c7d74d0e | -11.78983 | -64.84119 | 2024-11-06 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdbdb12f-579f-3f97-9aff-0d3c51446952 | -2.84705 | -52.90845 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35ba0a10-91f2-3f67-a9a1-6bb67be6b3c1 | -2.81796 | -52.9284 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1a202fbc-ceb0-3085-9055-4676e76cf282 | -3.16269 | -50.20386 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| e356f5ad-b9f5-3d13-aa66-e252c77b7538 | -3.16896 | -54.47321 | 2024-11-06 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee09f301-5801-387e-9566-4750f585a138 | -3.45788 | -50.37333 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ee6b4a71-11a9-31b7-9e72-707b4a546d97 | -1.49192 | -60.37416 | 2024-11-06 05:31:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 29617e23-63f4-33f4-9d77-7ad362ea08b8 | -2.65955 | -48.56244 | 2024-11-06 05:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 102ca805-f0da-3f9a-893d-f94ba744de13 | -3.16196 | -50.20876 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| f180aee8-2ae1-3f45-aac6-ad3bbaf6b4ec | -2.55691 | -54.23724 | 2024-11-06 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b7f554f-955e-3d2d-8e31-76fbdd10e3b0 | -3.01505 | -53.42465 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| ef733d4d-fcb4-3ac6-ae55-312568e8fb8a | -8.76816 | -67.65731 | 2024-11-06 05:31:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc8edbfb-d6ba-3e08-88ce-8ce3f48f635e | -2.91873 | -51.03945 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9860bdfa-dfe9-3ed9-abf0-034718b1af83 | -2.91784 | -49.35158 | 2024-11-06 05:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d5ec0b7-5001-3418-a0af-f07ec90dd550 | -2.77859 | -52.87646 | 2024-11-06 05:31:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3994528d-aeeb-3097-851e-3c67570649d9 | -11.77431 | -64.98129 | 2024-11-06 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 32a5039d-dcc4-3d67-993c-ccf0dc230d4b | -2.93364 | -51.06046 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 876b6804-a637-30f5-9ae7-53fd759ed471 | -2.8009 | -51.47977 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3675ca03-0bfe-38ac-98a5-9f5e76b7cf5b | -3.03744 | -53.27976 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ae12c613-23d6-3435-b1a5-e6b865ad66f2 | -3.10527 | -50.29617 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 49d2c55d-63d3-3112-8d88-84fbe1fa4af5 | -2.75929 | -53.21933 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9a024285-a47f-38dd-87e0-8de2933c76ce | -3.05153 | -51.06732 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6814ea85-953f-3a9f-9f3c-15e8684bbceb | -2.81985 | -52.95064 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 9f97a851-c5f7-34de-95a3-757048040951 | -2.82674 | -52.93944 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 44d7edb4-5c4a-346f-a93c-c356334216ed | -2.84812 | -49.47042 | 2024-11-06 05:31:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| fc20fc16-ad57-3d59-9309-050aa665c598 | -3.12198 | -51.1118 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5482bca2-c279-33c9-a0db-11dbfb36f75f | -2.80482 | -51.49215 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 07700eac-b099-39cf-85b8-b9e583c9dd5b | -11.82453 | -65.02316 | 2024-11-06 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8be1fa5-7032-37c9-9329-757796df7353 | -2.92442 | -51.04218 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d506632d-1db0-3f9f-8c5b-263f965cb3e4 | -3.12246 | -51.11111 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2b628ee4-eba4-3e6f-bcb1-7b8f4e565ba0 | -2.82062 | -52.91052 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3250b63b-0c6a-3672-b665-c4f871a0639a | -2.93942 | -51.05943 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 948deaad-efb1-3f17-9728-e4ea2d08f091 | -2.82213 | -52.93541 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| feda85ed-30c7-3892-ba63-19c54a8cb410 | -3.22578 | -53.39456 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 907185e1-316b-3ff7-8367-97f2ec74597f | -3.19939 | -53.22349 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f25e2f10-4185-3404-84a9-7d8b35b0bcae | -3.73319 | -53.39073 | 2024-11-06 05:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd4a4f8a-cc4b-31a5-8571-e6451f8f4e61 | -3.08368 | -54.50884 | 2024-11-06 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 73ee81dc-448c-3091-b5a9-89f5a7f1259e | -2.96178 | -50.98869 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4271a1e2-0e64-317f-a6a4-fd3204ad2a23 | -9.45407 | -66.63844 | 2024-11-06 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78eb9857-c38f-30b5-9d9a-78288e60dff6 | -2.91283 | -51.04034 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f6b4b2e6-5225-3ac0-b029-5a03ab379cda | -2.71564 | -52.96196 | 2024-11-06 05:31:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97df1d3f-57b6-3f13-b180-886913e51c57 | -2.92267 | -51.05269 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4218942e-6b0c-3003-a993-954f82f05a9e | -3.89614 | -50.25252 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 61395312-0c5a-30e5-b747-6c3c7fabd6d7 | -2.92845 | -51.0536 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 88a433b5-57c3-3f63-b29c-2c23345fad46 | -3.16342 | -50.19899 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 86fdee4e-0a03-3eb7-9e42-dad361eea951 | -3.08437 | -54.50415 | 2024-11-06 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a901fd8-497d-3d11-bd5b-42bd75e2d00a | -4.09251 | -50.49934 | 2024-11-06 05:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38d044b0-35bd-3310-ac0e-c25bc566c4b8 | -3.09039 | -50.2699 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9202a12f-3906-3ee6-8a29-fd763513f9f0 | -3.51849 | -53.14213 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 777dad6c-7543-38b5-b837-e8456ec2129b | -3.33865 | -51.62119 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9da77f0a-59f5-3038-8507-686c2fc36aa7 | -3.21715 | -53.10315 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0dac87e6-badc-3e6e-be06-75e04798093c | -3.0965 | -50.27081 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a91600e1-501b-319b-8ceb-1204c84118ab | -2.87985 | -51.31334 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d779fc7b-e51d-385c-b1d6-7082325dc6a6 | -3.18179 | -50.58672 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d80e21d8-37ad-3f47-8108-2871bc9571b3 | -3.00979 | -53.43581 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 6e3e0fa2-ad15-34ef-9ae0-d6c7fad1329e | -3.00842 | -53.43497 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 88df29f1-e2cd-3b1b-ab3e-ff7d1315dd42 | -2.9293 | -52.54062 | 2024-11-06 05:31:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d5be3ec6-5a2b-35a4-99ec-6d38292c5779 | -2.81151 | -52.93671 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 88a6d0c3-0898-3cf6-98e3-ea61caf9cfe5 | -3.02946 | -53.2633 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 95c45936-cef8-3941-9bc8-1d6c28cc2c6e | -3.14368 | -51.3314 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84a4e71a-57fd-3306-b120-8dac2f709395 | -1.4947 | -60.37814 | 2024-11-06 05:31:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99481709-ba0f-3f8c-90c6-358a1e8fa77e | -1.33623 | -54.60956 | 2024-11-06 05:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 001813a0-8bf7-3c75-96ab-a5105924b114 | -2.75511 | -53.21301 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc2d0cc0-7847-383a-a8c6-d35b1a272df5 | -2.91865 | -49.34604 | 2024-11-06 05:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba02bc83-e637-3fad-89fb-4676b003856e | -3.06685 | -54.78047 | 2024-11-06 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46bf0a76-4dd1-39b5-9e54-f754f509997c | -3.58683 | -50.26464 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c6372f9e-c917-3ee5-b76c-30d19dc0294a | -3.52321 | -51.66673 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7282f745-8275-3ea9-8764-61c9769b27b2 | -2.58595 | -51.86993 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb1f6508-fd6d-3d51-a8e5-2d9a04e558ae | -3.14439 | -51.20521 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a52d8414-a2d3-300e-905b-f5e61db56eb2 | -3.156 | -50.20796 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| f02a250b-f712-3353-a206-1dfdb7e1b90c | -2.91749 | -51.04771 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 8c0ad37a-8737-38e8-8499-8c8f8a9885e7 | -3.16353 | -50.19905 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 4bf5ce2a-552f-30fc-9546-0318bf91053b | -9.51269 | -65.59563 | 2024-11-06 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2676abcf-95b1-3c25-b3d1-0569594b7f7d | -2.77679 | -54.73851 | 2024-11-06 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |


[Clique aqui para ver as próximas entradas](README68.md)
