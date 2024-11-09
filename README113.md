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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 119fafbb-ed0e-3d4c-a318-3fd370aec3af | -3.59597 | -47.3411 | 2024-11-09 05:20:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 535c0bf0-fac9-3ebe-9cd1-52a7eac64d8b | -2.86696 | -50.32225 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9bcb353-f4ff-3e57-8818-4464583dfcd9 | -3.34578 | -50.36016 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cbe6970c-b0d6-32cd-b2e9-b6a44b5d4960 | -3.29495 | -46.4218 | 2024-11-09 05:20:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 7b2e7191-c946-3b8d-ad62-10d9d1c10bd4 | -4.19696 | -48.55298 | 2024-11-09 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 92ef2685-bf83-38df-ba3d-b44b502c6780 | -2.36846 | -46.85794 | 2024-11-09 05:20:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 80eaa836-80c5-3f6d-8d33-9d522b1bdeb6 | -2.29101 | -48.72857 | 2024-11-09 05:20:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee3553ca-b33f-3aa2-a1cb-2e5b00c00a0a | -2.23249 | -50.52034 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38dac1c8-200d-30ad-9487-8cbc4ccc1ea5 | -0.80816 | -52.4976 | 2024-11-09 05:20:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60948efd-7c14-373a-8bc8-0e40311b9d76 | -1.59888 | -53.32584 | 2024-11-09 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 956889cc-0983-35a7-ab43-c6c902f8b8a9 | -1.5097 | -52.17231 | 2024-11-09 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3810a471-c254-301b-ab3c-d3a1ceccd913 | -1.62118 | -52.24189 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2d7f1f76-c3c1-367e-a412-f5cd3efde4db | -3.15812 | -54.48791 | 2024-11-09 05:20:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4bf5cf01-1ce4-3cb6-9038-eefed8e26b64 | -0.83412 | -53.06072 | 2024-11-09 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f08710d-04e0-3db4-a31f-55d5f3d1d4c4 | -0.81502 | -52.36087 | 2024-11-09 05:20:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 102acc37-8eae-3149-8a93-cf41721f1b21 | -1.24174 | -51.77571 | 2024-11-09 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 193d5840-6cea-323e-b043-e31c1cbaa075 | -3.23906 | -53.39945 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66e1d545-7152-35b8-be3b-bd367926ef28 | -2.37893 | -53.84526 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37b22ec7-c366-34ed-9a40-e231aab55f08 | -3.33978 | -50.36285 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 17f2159f-bc4c-3f16-9fca-fb286edd3bcd | -3.67262 | -54.23718 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fc322550-96e8-312b-98e2-2de6a1a1c058 | -3.02497 | -54.20442 | 2024-11-09 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| af514b52-d251-3e26-a784-8e7fbb89139b | -3.24291 | -50.45272 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 414457b9-5121-3920-938a-042c9087dcd4 | -3.29413 | -46.4146 | 2024-11-09 05:20:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b4a10bdb-12ca-3424-95f3-92393ee68e16 | -3.2083 | -50.63305 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b8de05d-b18e-3a76-9f8c-0ef1ef48f664 | -2.59748 | -48.19653 | 2024-11-09 05:20:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 965302e2-0d7f-3966-a4b9-542b444e0da7 | -2.58504 | -49.132 | 2024-11-09 05:20:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 641d49df-9154-3871-83c7-4f783ade7634 | -2.9272 | -51.67372 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7c0ea38-2916-383d-9738-fa3d6505ba8c | -3.731 | -54.22203 | 2024-11-09 05:20:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 3fb54c6a-8bb7-310b-8781-e27cec97b190 | -3.89891 | -51.9251 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7f88caa4-a64a-30bb-9595-5427df4a5083 | -3.73806 | -50.45299 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d44facd-b183-36e2-ac46-74bb6d88acc6 | -3.03006 | -53.27092 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a6f8ce78-75f7-3969-a6ca-e061f49467f2 | -7.29899 | -55.31636 | 2024-11-09 05:22:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d6bdb7c-0410-31ec-936a-a1f4b923d7e0 | -10.52909 | -49.35924 | 2024-11-09 05:22:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3bdba6c8-a409-38d2-89cc-ebc0d5366c6b | -17.24294 | -57.49662 | 2024-11-09 05:22:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4eca6963-a47e-3131-84c5-cf2df24e4d94 | -16.09724 | -60.10876 | 2024-11-09 05:22:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9033615-0219-3f58-805c-f483de489cfc | -17.29763 | -57.4964 | 2024-11-09 05:22:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 260d2410-8cc2-3ca3-9238-02f20f63af21 | -16.09791 | -60.10729 | 2024-11-09 05:22:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9640dcb3-8bb5-3dfa-9c60-bf670d0c1504 | -14.87933 | -60.06839 | 2024-11-09 05:22:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6eb418a-7b70-3187-acbd-d34f74feb6c3 | -5.13569 | -60.36425 | 2024-11-09 05:22:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4f188772-15bd-33ed-beb7-08bb4084568c | -17.29299 | -57.49969 | 2024-11-09 05:22:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d411b0ce-5290-335a-8639-268dcf0500bc | -17.60966 | -57.44963 | 2024-11-09 05:22:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 9848892b-9455-391b-8176-38778aa5d26d | -8.84523 | -47.67952 | 2024-11-09 05:22:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 169ca47a-fda4-32dc-acb5-3befea24ce26 | -17.40301 | -54.71836 | 2024-11-09 05:22:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a4837a6-f784-39bb-aa13-890c1556df7b | -6.23438 | -47.28909 | 2024-11-09 05:22:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9056184d-1bc2-39f0-87fe-77b85561f537 | -8.84446 | -47.68595 | 2024-11-09 05:22:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 937373cb-4e88-398c-b396-57e76a3763a3 | -5.139 | -60.36476 | 2024-11-09 05:22:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f27fe350-eda4-3a53-b8d0-3f12b2b07fdf | -6.98316 | -59.42548 | 2024-11-09 05:22:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4dd746e8-0565-3529-987e-1f86013f6778 | -6.75447 | -59.06269 | 2024-11-09 05:22:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08e82e9b-ac9c-3f4a-8a1d-2ef10c9ac557 | -8.84609 | -47.68284 | 2024-11-09 05:22:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b4b8643e-1886-36d7-b09e-5df75daf6489 | -6.23528 | -47.28255 | 2024-11-09 05:22:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 494413c8-f397-3777-9683-0134d85dafb5 | -6.62665 | -62.9166 | 2024-11-09 05:22:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39fa4f93-e1ae-3a43-8001-f79f67547212 | -8.85306 | -47.68377 | 2024-11-09 05:22:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0eca89f9-fe0e-3c77-aa0c-deb0049e015b | -10.52846 | -49.35773 | 2024-11-09 05:22:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0e55d6cd-d7ee-35b2-88c9-63eacf5820ca | -8.85143 | -47.68687 | 2024-11-09 05:22:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| caefbe34-ba9c-3e76-8fcc-6182c158b490 | -16.10135 | -60.10521 | 2024-11-09 05:22:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27e525ac-6ded-35f1-be19-2e53a7585a18 | -6.62604 | -62.92043 | 2024-11-09 05:22:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 411b478f-2218-30c0-9020-eee554e0d3eb | -4.73136 | -59.9092 | 2024-11-09 05:22:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a19cbb3-d253-323e-be67-46403a621715 | -4.39332 | -59.91976 | 2024-11-09 05:22:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61019927-e1b8-3a21-806a-4ddd2ad79582 | -7.29485 | -55.31575 | 2024-11-09 05:22:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2aa9967b-63ed-3d27-89a1-43a48c02c028 | -8.84527 | -47.68929 | 2024-11-09 05:22:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 043e9b37-d27a-3659-8890-bba5885f067c | -4.49352 | -60.2136 | 2024-11-09 05:22:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75707bee-a839-3411-b970-1bcc089bc908 | -17.29712 | -57.50026 | 2024-11-09 05:22:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| dda8780b-a26a-3a30-b024-d802fb95ad58 | -17.28886 | -57.49911 | 2024-11-09 05:22:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 44ba3f9a-7884-30a1-a906-06fc0b8f8c7b | -17.28937 | -57.49525 | 2024-11-09 05:22:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 8e6bcedc-e02d-3fa6-892b-6e6ce806bb65 | -6.62951 | -62.92099 | 2024-11-09 05:22:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 08a1cf43-36e6-3679-9891-e65d1a4569cb | -11.56683 | -61.42174 | 2024-11-09 05:22:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5a07639e-706d-3136-afae-d16086d323c4 | -6.63012 | -62.91716 | 2024-11-09 05:22:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 94307740-d23a-39c0-858e-8b9a83904a64 | -17.24392 | -57.4889 | 2024-11-09 05:22:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 320a7239-aee4-3e54-927c-256c2192878b | -4.28945 | -60.15012 | 2024-11-09 05:22:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ce77da1-d14c-3208-b4e9-60e05ebf673c | -17.24343 | -57.49276 | 2024-11-09 05:22:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a9071855-1a7e-37b0-b5c5-cb972ef32d79 | -17.2935 | -57.49583 | 2024-11-09 05:22:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 6710eb56-7f69-3c7d-a526-6711beb3b7c9 | -8.84443 | -47.69584 | 2024-11-09 05:22:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fcf54322-f79f-3525-9245-56043c1fac31 | -8.85388 | -47.67734 | 2024-11-09 05:22:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e1e3788a-3c71-3f0f-9972-ae7b48d8df6c | -10.52777 | -49.36335 | 2024-11-09 05:22:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f986c9d1-8677-3aee-9740-fe7b6bc6caca | -8.8522 | -47.68054 | 2024-11-09 05:22:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 202cb804-332c-3589-9d1a-f0feb03fb2f3 | -6.23551 | -47.28087 | 2024-11-09 05:22:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65150cab-e50c-3025-acaa-0b9ec52f3106 | -6.23466 | -47.28745 | 2024-11-09 05:22:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 001d5ece-481d-3be5-a6af-3fb3f46cee43 | -12.41994 | -64.14021 | 2024-11-09 05:25:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76c8eec7-164a-3ff8-aa67-035f2009063c | -20.60155 | -55.90415 | 2024-11-09 05:25:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3fa4bf7b-77a0-3caa-85aa-5fccac33996e | -23.90748 | -54.06911 | 2024-11-09 05:25:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ccd95c31-1e14-31ab-8e7f-8c890a4a10b8 | -12.42402 | -64.13696 | 2024-11-09 05:25:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22b4a422-b01c-35dd-a257-8df5d9ed6788 | -12.8202 | -62.07059 | 2024-11-09 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e716a6d5-0d3a-3d8a-986e-deebb3adfe40 | -23.91381 | -54.06157 | 2024-11-09 05:25:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 23c56e77-27bd-356a-bcfd-246071ef5a68 | -23.88762 | -54.05949 | 2024-11-09 05:25:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 1c14ec65-2442-373a-968e-09472827b67e | -23.88569 | -54.05859 | 2024-11-09 05:25:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 6e8306f1-9ba3-3c9d-a13f-436b120a4013 | -23.90784 | -54.06504 | 2024-11-09 05:25:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3aeb2bf4-47b2-39e6-8f4f-509769460dc7 | -23.90818 | -54.06097 | 2024-11-09 05:25:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 217507e5-f3e4-3ee4-8a23-274e6128612d | -12.42057 | -64.13636 | 2024-11-09 05:25:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1dcb94d3-b1c7-3386-bb91-ab372c0455e9 | -20.60215 | -55.8988 | 2024-11-09 05:25:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e092951a-64d2-38c0-96f9-1e9a1923aa06 | -1.5347 | -52.1899 | 2024-11-09 05:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| e04b5a81-f96c-33aa-abc4-eb08b5c58cb8 | -3.9854 | -48.1708 | 2024-11-09 05:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 75b0c66c-ac18-32d6-868f-8728b6f4cd9d | -11.1068 | -43.3428 | 2024-11-09 05:30:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 65.6 |
| 291029ee-4d9a-3a8a-9913-c7f9122a3fdc | -11.1073 | -43.319 | 2024-11-09 05:30:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 50.7 |
| f8e3262d-af38-3c00-a73f-3427e7843719 | -11.0877 | -43.3456 | 2024-11-09 05:30:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 1152ad03-96da-37ed-9a37-3eea43b10e15 | -4.2486 | -47.5729 | 2024-11-09 05:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| c99a1f0f-61b7-3d29-a92b-5d2285c29024 | -3.6004 | -47.3395 | 2024-11-09 05:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 633ff338-a10c-3c2b-b2e8-2aaa347dd48e | -3.9668 | -48.1932 | 2024-11-09 05:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 57ee42e0-d6dd-37cb-b5c9-3e488131ad15 | -3.9853 | -48.1924 | 2024-11-09 05:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| c0784e56-d8fd-3605-9060-f19865e8bb2b | -1.5163 | -52.1901 | 2024-11-09 05:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| c935b55e-f4a0-3e3e-9a8a-53c7dc8f064e | -11.0881 | -43.3219 | 2024-11-09 05:30:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |


[Clique aqui para ver as próximas entradas](README114.md)
