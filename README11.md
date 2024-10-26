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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87719c3f-618d-3bb3-b29b-475284de8180 | -3.00138 | -50.50022 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 527f93c3-9bec-3940-8ee4-1904c17ae056 | -3.00005 | -50.49072 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| ed5233cb-929b-3d2c-8731-1d88392cf4ce | -2.99872 | -50.48118 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 211e0d06-b3fb-3841-8f3d-d929b2feb7a2 | -2.99738 | -50.47164 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e1a3d44a-8de7-3a4d-afa2-d21f3df41451 | -2.99089 | -50.49203 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| d51e9107-8b80-378c-9aa8-1965a650faa2 | -2.98954 | -50.48246 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 45c9499f-f6b2-3b9b-90b9-689d79a9b355 | -2.9882 | -50.47288 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 80b17fe4-ddf3-3a56-b1e2-41783ca817d9 | -2.97585 | -54.6333 | 2024-10-26 01:09:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2693ffed-f1c2-33d0-aa8d-79e007a92ae9 | -2.97348 | -53.27117 | 2024-10-26 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| ec7e9761-1181-3bb8-a154-49326c4a7834 | -2.97222 | -53.26204 | 2024-10-26 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| bf476d52-1aca-32aa-a647-c16a582bda12 | -2.97222 | -47.99085 | 2024-10-26 01:09:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| fd618df0-5c55-30bd-a021-e69c4229a7d1 | -2.96311 | -50.42783 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 1d6f6dd7-ef8e-3442-bdbf-5ea77e66d77d | -2.95828 | -50.52578 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0e41bc2f-51fe-3b90-82bc-45db9f4c953f | -2.95392 | -50.42914 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| f97203dc-ddaf-3f25-aa80-ec2adc84416a | -2.95256 | -50.41956 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d211cb6e-3242-3fe4-b694-5297b922b38e | -2.95028 | -52.56781 | 2024-10-26 01:09:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 3f782cbe-662a-3c80-bef8-67924588e108 | -2.94262 | -52.98185 | 2024-10-26 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 456a8152-14be-332f-912f-b548922fffb0 | -2.9391 | -52.56634 | 2024-10-26 01:09:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 06f118e8-b015-386d-9e1c-b070d9765548 | -2.89788 | -53.32521 | 2024-10-26 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| eb22eeaf-4d22-3dfa-a13e-41edb4763c1c | -2.89111 | -48.28868 | 2024-10-26 01:09:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| dda0ea2f-874c-3de5-af46-db14e06a0a40 | -2.89016 | -53.33557 | 2024-10-26 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5f42846b-540a-3399-9367-8abe4269e2fb | -2.8889 | -53.32644 | 2024-10-26 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 36f9da96-c47d-3a27-a268-f30f61261b91 | -2.88764 | -53.31726 | 2024-10-26 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| ffe49181-1fb1-35b1-95ca-ee529f1a8b71 | -2.88639 | -53.30815 | 2024-10-26 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bb1bdaf8-e57a-3523-9fb1-8910d67e9928 | -2.87992 | -53.32766 | 2024-10-26 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| ee19d48a-96d8-3d4d-8318-1d21c071bb2b | -2.87867 | -53.3185 | 2024-10-26 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 4b6f83f8-eb32-3608-8074-9bc0d703df78 | -2.87742 | -53.30941 | 2024-10-26 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| ac7e86a0-6585-3199-b38e-ab40a9928b32 | -2.86427 | -49.45249 | 2024-10-26 01:09:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 2ea51eef-169b-343e-a682-9484580a0672 | -2.84611 | -51.82033 | 2024-10-26 01:09:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e79661c0-93a1-37c2-9061-9f35a1437a67 | -2.84488 | -51.81153 | 2024-10-26 01:09:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 78d52b5a-1773-3fc1-b00b-ff5201682ce8 | -2.83496 | -51.81881 | 2024-10-26 01:09:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9b0c3173-1d20-3c1f-8eeb-6a006b577330 | -2.83373 | -51.80998 | 2024-10-26 01:09:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 987a0ecb-39cc-331d-8d3c-72eec08930e0 | -2.82734 | -52.15186 | 2024-10-26 01:09:00 | TERRA_M-M | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e2f805eb-fab3-3b4c-be40-e909e4a06c76 | -2.8074 | -54.0055 | 2024-10-26 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8b80b330-570f-3bab-8020-925f4fa25e72 | -2.80216 | -54.1044 | 2024-10-26 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| b5ceaacc-a9fd-3e1b-85be-185151d574eb | -2.79131 | -51.36584 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| af19e8d0-69eb-3b62-92fe-5b3a2aa1f102 | -2.78293 | -49.23045 | 2024-10-26 01:09:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b81f4ab8-af1d-3ade-8526-ef94cf6cec0b | -2.77598 | -49.32134 | 2024-10-26 01:09:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a6e0985d-8a7d-33b6-a55a-0c4d34d93c0f | -2.7422 | -53.20233 | 2024-10-26 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a1bb63e9-3841-3202-9a22-bb2be2bee54d | -2.73327 | -53.20365 | 2024-10-26 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 847cc5cc-9235-3e44-9a70-3e260f39d8b6 | -2.72862 | -57.47657 | 2024-10-26 01:09:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 8399deb2-9607-3806-b475-cc748d618e2c | -2.72646 | -57.46059 | 2024-10-26 01:09:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 177e12b8-68f5-32e4-afe9-a3c2ad21deb9 | -2.69376 | -51.7911 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| b81ccfbc-5625-3653-b692-a993c4e99965 | -2.68761 | -48.64098 | 2024-10-26 01:09:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 76f78ce2-323a-3bd2-bb07-43cbd586bdc6 | -2.68528 | -52.06768 | 2024-10-26 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 2711114c-0cc0-3dcf-946b-4988f0e218c1 | -2.68216 | -54.02561 | 2024-10-26 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 5330701c-b023-302d-b7ba-5c15907619a4 | -2.66726 | -47.39963 | 2024-10-26 01:09:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b036e5d3-5e87-3adb-a45c-4200b5d95dae | -2.65936 | -49.51602 | 2024-10-26 01:09:00 | TERRA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4b11da99-6d4e-382a-8ddd-57fccbfdf19a | -2.65784 | -49.5053 | 2024-10-26 01:09:00 | TERRA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1a5287f7-91ff-36b2-b713-f282f7c288fe | -2.65647 | -49.28339 | 2024-10-26 01:09:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 48b2a377-c2d5-3ef2-ac1e-b3c3043a6f8d | -2.65492 | -49.27235 | 2024-10-26 01:09:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 05aaaf48-f5de-36b5-827d-2cf74df31695 | -2.64967 | -49.51743 | 2024-10-26 01:09:00 | TERRA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f10310dd-1da4-3b80-b7f9-58dbbbc83de8 | -2.64815 | -49.50671 | 2024-10-26 01:09:00 | TERRA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f72d23c2-7567-351b-b098-3fa26409dacc | -2.64039 | -54.33843 | 2024-10-26 01:09:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| defc1a31-0401-3a84-9821-833fde1bbc00 | -2.63211 | -49.25301 | 2024-10-26 01:09:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4a297274-4379-36e7-9ae5-9fa474003375 | -2.61938 | -52.45054 | 2024-10-26 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 9518b471-704b-371f-93a0-5122d4aa6495 | -2.5999 | -49.09713 | 2024-10-26 01:09:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 3f8de63f-343a-32d1-ad4b-d4e565287411 | -2.59825 | -51.36881 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| fad16e03-4f1e-3a0f-b35e-99d0cad68b85 | -2.59698 | -51.3598 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 381a0263-c1da-39a5-829f-668a29fdeb67 | -2.58948 | -49.23647 | 2024-10-26 01:09:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c7c6ad4d-d398-33cb-9490-b76ca9224304 | -2.58366 | -51.92051 | 2024-10-26 01:09:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7405a0cb-cddf-3c56-ac84-0dcd587fe9cd | -2.57023 | -54.0176 | 2024-10-26 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2680884a-4055-3ee4-b023-aef82135f3b5 | -2.56974 | -49.23933 | 2024-10-26 01:09:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| ac06d5a4-06f0-3f03-9880-7d026f9ffe57 | -2.56812 | -49.22817 | 2024-10-26 01:09:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d16a8a8e-f979-3554-85ad-7eaaedf5debe | -2.56761 | -49.23455 | 2024-10-26 01:09:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| d73a1c75-d2f0-3c4a-b7a9-bf4b07220e20 | -2.56725 | -47.25629 | 2024-10-26 01:09:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 21a8599a-18b2-33af-aa3f-db1bb30ebb34 | -2.56105 | -54.01889 | 2024-10-26 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1999a36a-a951-340e-8d60-a107a9cfaf03 | -2.55797 | -50.69081 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 27b91f5a-5b28-315a-a51d-640deb7ae7f0 | -2.47898 | -49.10928 | 2024-10-26 01:09:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d59e6a83-c41f-3485-bfa5-7d3587c2d55d | -2.47283 | -54.04758 | 2024-10-26 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1df8a719-ce39-3323-9ca1-a6175a82fb96 | -2.46901 | -49.11071 | 2024-10-26 01:09:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| c78a1e5a-14e9-3067-88b2-200f5dc42268 | -2.46736 | -49.09932 | 2024-10-26 01:09:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| af31e797-83ac-36a0-98fc-b0c827a04608 | -2.45346 | -50.99662 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a06c964a-5d0d-3c64-acb0-7fb480506491 | -2.45215 | -50.98741 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 00dfe445-2af3-319b-995b-2b4447f99b8e | -2.45069 | -50.38034 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 7685cdc0-44ce-3def-a7db-b32cba4e7ebf | -2.44934 | -50.37062 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ad01d419-e5ac-3199-84a2-f86d1dff2ddb | -2.44652 | -48.39659 | 2024-10-26 01:09:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8e4fa889-9cc2-33ed-8500-978ba20f0cd5 | -2.41639 | -50.40506 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2a31a1bc-d4c0-3c92-a6b9-bcd360ab3286 | -2.40063 | -50.42709 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4250acb5-7347-398d-8b87-87d4caab1ca2 | -2.3846 | -49.38613 | 2024-10-26 01:09:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 662f74fe-7af1-3aed-817e-98e2afe5aa73 | -2.37308 | -48.94201 | 2024-10-26 01:09:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 35777031-08ed-33a5-a410-feb41d88c050 | -2.37202 | -48.29584 | 2024-10-26 01:09:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| e3fb9dc8-0f1d-3826-87d6-032d0d408c4f | -2.37013 | -48.28279 | 2024-10-26 01:09:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 99789c82-f47c-3598-881a-c6d3970e4b2b | -2.36142 | -48.29736 | 2024-10-26 01:09:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 1d10d6fb-ce8c-34b8-be65-77d1db3c7c96 | -2.35953 | -48.28434 | 2024-10-26 01:09:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| c4d2609c-fa69-3d33-b617-9ad56c163a57 | -2.34877 | -47.50097 | 2024-10-26 01:09:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 50eac950-9e16-3aeb-bc19-0c14c6f9bf01 | -2.31626 | -46.64964 | 2024-10-26 01:09:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 0b393ac5-6079-36d4-8100-fe80cdb8887a | -2.2684 | -50.66344 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| adf37a3c-a9cc-3ee0-8673-82d02c75bd4f | -2.24251 | -50.74432 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 20a44e39-6d9d-35d5-a1b1-cdbc8af9f172 | -2.19753 | -53.72453 | 2024-10-26 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| b9c0f099-485a-35e6-839f-84541ece2356 | -2.19077 | -46.42008 | 2024-10-26 01:09:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 1b09f8e2-2cea-3cd7-933a-3e904fbe75e9 | -2.18975 | -53.73507 | 2024-10-26 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| df57017a-20a5-3961-888e-5ce222c42519 | -2.18848 | -53.72582 | 2024-10-26 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 8886607c-ce16-3442-81a3-54280e837d15 | -2.17224 | -48.82606 | 2024-10-26 01:09:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| e168557e-69ff-3dfd-99ad-1a6d74675c78 | -2.17052 | -48.81405 | 2024-10-26 01:09:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5cefb501-14e3-3fab-824e-653704709815 | -2.09859 | -54.5989 | 2024-10-26 01:09:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6430f7c9-45e9-3df7-aec9-a9fd7ec597e9 | -2.03603 | -55.76317 | 2024-10-26 01:09:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2d3d4c8f-6f1a-31dd-9385-24696e287e43 | -2.01039 | -48.53516 | 2024-10-26 01:09:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 5bc4ca38-87fc-35ab-b764-d8d7ad0dc761 | -2.00863 | -48.52251 | 2024-10-26 01:09:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| c657d52a-78fe-3075-a8c1-b1ede66c718c | -2.00542 | -48.53008 | 2024-10-26 01:09:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |


[Clique aqui para ver as próximas entradas](README12.md)
