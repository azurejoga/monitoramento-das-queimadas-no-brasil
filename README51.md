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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d485165-71e7-38d0-b0b1-c4e8de229184 | -2.38613 | -50.40869 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7d980444-740e-39c3-aff2-911cb0c6a6a7 | -4.93626 | -43.63876 | 2024-11-06 04:36:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6db1a5d6-a628-3a54-ae72-a22c0f47b56d | -3.85617 | -54.08157 | 2024-11-06 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 06649977-2a4f-376b-a49b-08689b41eb4b | -4.10602 | -48.50492 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f3d6101-d790-310a-91e1-1b075e830d7a | -2.82123 | -48.55402 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 553c42c6-e40b-34f9-b14c-9f364dd2fff7 | -2.51557 | -48.91747 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec5b9ab3-61fe-3ff4-b724-81efe56517e4 | -1.3803 | -52.26615 | 2024-11-06 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28608ce2-cd31-33d8-b7ff-dcdbfb062138 | -3.06911 | -47.7716 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a8151989-90e0-3149-932a-ade265549d0a | -3.38432 | -51.42733 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 595450a6-feb1-37c3-849d-2cc527bc32aa | -2.45196 | -50.39228 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3b62559-3fb0-383b-9aac-e542f2c05c27 | -2.70991 | -46.6746 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0982c622-9538-3fbc-adf9-d472a241353c | -3.88069 | -52.37041 | 2024-11-06 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 82b8b223-dc74-3726-a5a9-389a154ab956 | -2.61999 | -51.72677 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19ecc6b3-aac2-325c-acc9-ed2696148916 | -2.82528 | -48.4599 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8503e640-e6e9-3ce5-baf7-94d449dd4ad6 | -3.32689 | -51.62632 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5dea5b6a-389b-3136-becf-f33c6f547629 | -3.07565 | -49.56894 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3af6fbe1-3a2c-3c58-8397-2a58df6f46b8 | -2.91459 | -49.34089 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 31b8b6de-d6ba-3b0b-b1f8-cb6c1c5c2086 | -2.85672 | -51.28388 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e402b76-7fd9-3439-bf4a-815343871057 | -2.72417 | -46.67299 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3360614a-5dd0-33c9-a122-7cab843c4be5 | -2.84011 | -51.80172 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5fdcd2cd-6b20-3a23-abc3-4803b3d1e320 | -2.34685 | -48.93337 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 508ad101-4928-3c73-947a-ed1c43ac5bb5 | -2.84344 | -49.46806 | 2024-11-06 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c48f7974-dbbc-38d9-8d45-5e9515b81342 | -2.90195 | -49.39892 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfc906d1-f5fc-31a3-8dcf-b330dc5c4bcd | -3.12289 | -51.11308 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e74fb200-7175-34b4-835e-7287366f62bd | -3.2231 | -50.9216 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22627a24-1c55-3aea-9e86-17ba193498f2 | -2.97479 | -50.29777 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e466f45c-2741-3fc8-b381-6e2f2087094d | -2.91957 | -49.35231 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49bee207-e28f-3c9b-a024-14eca3a15209 | -2.71057 | -52.96285 | 2024-11-06 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ee40360-191c-35fe-aff1-86cd1b65dd90 | -4.22879 | -48.54556 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f8b68ad2-725c-3861-8597-2d7ef1beb880 | -2.42732 | -48.5942 | 2024-11-06 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4ce519c-4b62-3618-bc5d-db0b154bd7ad | -4.44513 | -50.69732 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 645082f8-0c0f-3fb3-8cf0-1cec3cd55dc4 | -2.65637 | -48.5636 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fcebfd7c-2e57-3a96-8924-0b5b32ab40e6 | -3.79855 | -49.97996 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 276802ce-0dba-35d7-b584-c451475d584a | -2.87205 | -51.39154 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f596f71-5e0f-32a4-ae94-d16318eba7a1 | -3.73764 | -49.87323 | 2024-11-06 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ce5805c-e0a6-3ef3-ae87-46ef09611ecb | -2.33127 | -49.11806 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c09a5ddf-4b60-3911-916b-1baf3c74394e | -3.7509 | -52.22233 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be99d168-d5c1-3585-9f93-45acc096e6cb | -4.42823 | -45.61808 | 2024-11-06 04:36:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa877501-24aa-322a-9b27-10e6fb41aaf4 | -3.71629 | -41.69037 | 2024-11-06 04:36:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 89411707-3bef-39ae-bea4-27d4e39f0ffd | -2.95579 | -53.71683 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b03fe3e3-e760-3ad6-9b95-07bd2e96c0d9 | -2.34945 | -46.67001 | 2024-11-06 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f567a508-94ac-37c9-9d00-e7827991c242 | -3.53011 | -40.90867 | 2024-11-06 04:36:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f9831648-776d-38c8-acf3-6bb123d03518 | -2.67248 | -52.52498 | 2024-11-06 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f5a5fa2d-eb12-3bd5-a545-597a27d6ea63 | -2.66627 | -48.56514 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d139b8a-2fee-36cf-a593-fc8a5a2b3f65 | -4.09124 | -51.04278 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e3c3b02-1674-304b-a2ba-13945fba1a5c | -2.37815 | -46.33081 | 2024-11-06 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe2eeed6-bac7-3929-ab7c-d5df433c117f | -2.84566 | -49.47554 | 2024-11-06 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| c0e911f6-da0e-3bec-b9e4-b6c3f6563a07 | -2.84016 | -48.45497 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d200cd20-562d-3e19-be0c-9df315de8d5f | -3.59997 | -42.86034 | 2024-11-06 04:36:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fe25c671-1501-34a6-95e1-9dd65aebd46c | -2.91404 | -49.34435 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f089fe39-bdbf-3d0a-b8f8-c425ccdd0a93 | -3.64085 | -49.88353 | 2024-11-06 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1349e1d-5e36-3bc4-a810-ce07e9eb989e | -3.04312 | -53.26836 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 32d8da57-c3f1-365d-893a-c3f753bbd6bc | -3.49198 | -50.2896 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3cc95c5f-49c6-3de1-9c27-dd8ef7c6f782 | -3.15933 | -51.13078 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10e3e757-0b5a-3e18-91c1-e24e3f7b6a53 | -2.64407 | -49.89014 | 2024-11-06 04:36:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4254f516-ffa8-30de-8ab0-bf56281f0e40 | -2.91484 | -48.06438 | 2024-11-06 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1392d1c4-4ed4-38ce-a725-6306480c5c91 | -4.82112 | -48.56055 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96bd8d10-d2fe-3d75-8038-ffd056854505 | -3.41167 | -50.28421 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 463d3da9-2bcc-3841-86d2-ed3031460581 | -3.22204 | -50.38036 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 9e37377c-81c0-3c88-b2fc-afc8b94de136 | -4.35859 | -48.65098 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0f7b003e-003f-3a6f-9205-e11296ceb7c5 | -2.65859 | -48.57098 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d255fc18-57ee-3793-a0af-817d7a7e6bba | -2.72636 | -51.71694 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 583104f8-d1cd-372d-8d98-f7861728ec35 | -2.866 | -49.38974 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae92d486-2283-3c33-a147-d964fdfeebef | -3.20656 | -49.23463 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64a430f6-29c7-3dbc-9803-e839e07e5a17 | -2.83315 | -48.67186 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 732e0c6e-a623-3cc8-be93-352b653e843b | -2.43029 | -49.22207 | 2024-11-06 04:36:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f7503743-8196-3e7f-ad53-33cc80722e70 | -3.99391 | -50.55245 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b83cf68f-b725-329d-9504-0644e9b71b90 | -5.20927 | -47.46022 | 2024-11-06 04:36:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f00d5b7-ce65-3956-a547-afbd2b9b7e9f | -2.65583 | -48.56703 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 381853f7-6ece-39d7-a237-d27c6aabc20f | -2.32314 | -46.1822 | 2024-11-06 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a971707f-31bd-3668-a55a-883f396f3d41 | -2.32833 | -51.98499 | 2024-11-06 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59177436-1cd4-33d1-b36a-9e1836d4ec0c | -3.52523 | -51.31646 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0768fa24-ea0e-39dd-a853-324c44ae57dc | 1.34726 | -50.87971 | 2024-11-06 04:36:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2fb275e0-9cd9-326e-9199-8e5d976ddd56 | -3.97071 | -48.13308 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 418533a8-c52b-3cd4-9bbe-0ff2b434a373 | -4.55547 | -48.01929 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| c0bff298-0f7a-30ab-86a6-984910b0bf99 | -3.11303 | -54.17014 | 2024-11-06 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0b553f6b-fdc4-3804-bf01-c47d22e1c620 | -1.2816 | -46.665 | 2024-11-06 04:36:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb5f7859-c42d-3cd8-aa39-b9a4dd438e74 | -5.14092 | -47.70183 | 2024-11-06 04:36:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31f0a988-ce25-3825-895f-63f032a909f7 | -0.85041 | -52.83661 | 2024-11-06 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1b2ec96-5778-3851-b8d5-4a0d3c8de5f2 | -2.82064 | -52.90493 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 66a33142-218a-3b6e-a080-ff025da782d1 | -2.9392 | -51.05826 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 97c6ccfc-5f04-340e-8228-567c2ab7c3b7 | -2.80591 | -51.48729 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35a134d8-d4ef-39c5-8676-b17e70c3da51 | -2.8207 | -48.55745 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bb0878c2-fef1-3499-a4ae-992493628a15 | -2.8145 | -52.91859 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 020e97fb-691f-3320-8a01-9efb2b1efb95 | -2.50598 | -49.17406 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa763997-0932-3d8e-8d74-944153802b40 | -3.33153 | -50.08123 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0b4c2cea-860e-357a-abc9-3b90439e4941 | -3.32482 | -50.08018 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 840cc871-aac2-373c-abe7-ca7a2db4f30c | 0.18556 | -51.06274 | 2024-11-06 04:36:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 767f53e4-8524-325c-abec-aab949f35a99 | -5.42826 | -45.35677 | 2024-11-06 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be5eb271-4a57-39b2-8c95-9abe4e41a9fc | -5.37742 | -46.43296 | 2024-11-06 04:36:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b816510-ea3c-35ff-956a-6939e6d70fd3 | -2.30159 | -46.73035 | 2024-11-06 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b238a7f1-884e-37aa-9270-bb87d3939877 | -3.19848 | -48.65899 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c84cf279-6b2b-37e5-990e-67754081bdf5 | -2.9119 | -49.42216 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42808688-ba63-3a64-9dbf-a94cebf0e687 | -4.73374 | -48.96713 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f27427f4-5398-355e-b8b5-c0a172c8c564 | -2.74433 | -54.12366 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35da80d1-30b4-3e8f-bfff-75e7238b733e | -4.30336 | -50.74621 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d813021-466f-30bd-ae1e-d0f76bf2e0f9 | -2.79602 | -46.63792 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b790ecc4-60c0-3a64-a074-aa2667c282e9 | -2.64838 | -46.77533 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c72686be-c347-3301-a030-9827981928ab | -2.60219 | -49.27417 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4146d489-84d7-3240-ba34-0d75bd377c69 | -2.83291 | -52.90199 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |


[Clique aqui para ver as próximas entradas](README52.md)
