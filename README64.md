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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38f90ced-133c-37a9-9bb1-543b905ab4a0 | -3.2789 | -50.52742 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c562bbb-6b06-3701-a31a-f603949a7cc2 | -3.35361 | -50.18818 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fcdef711-589b-3d2a-9fac-4726bffae752 | -3.46322 | -52.7247 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f99f26fe-ff81-3646-ac45-9c4c67d05723 | -2.88441 | -53.96468 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9e3224c-86b6-3b1a-b04d-8208978e0842 | -5.4549 | -46.48671 | 2024-11-21 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45dc89a8-fff7-302b-a207-a1693edfabfd | -3.37176 | -50.19104 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d120031-793d-374d-bcb3-02eacb62865d | -3.37853 | -52.46099 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e01e7db2-7453-3966-acff-9e266159b8c2 | -3.04807 | -54.41078 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3410b02-6757-3e39-9e1f-19ae69df519b | -4.10899 | -51.05379 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d0b565c-7105-30f3-b1e8-6c0f168a65ef | -4.63716 | -49.55013 | 2024-11-21 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e94e665-25c2-3557-a8fd-fc714d64fb4e | -3.74491 | -47.36055 | 2024-11-21 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 99bec3b2-3634-32c0-8b0b-f46e49614db7 | -3.41966 | -49.22988 | 2024-11-21 04:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b06c42e9-6751-3092-81bc-c1e0c1b7516c | -2.60663 | -51.79025 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9bd7976d-26dd-35e1-ba32-f0081360c099 | -2.82003 | -51.79283 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 688a820b-da33-36f9-90cb-be1f6e3caa41 | -3.07782 | -50.35288 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 034bd4d4-a3c4-3ff9-a73f-d37b5bf323bc | -2.41787 | -54.63836 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b1c09ab5-e3e1-33f8-82f3-4200ae0f5fef | -3.22647 | -53.62638 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f9d0357-ae18-3b52-a269-e64cff679908 | -3.11246 | -53.70354 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a11f652-fdb6-34db-ad6e-a931b9ecbc12 | -3.36218 | -50.18089 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 35b46dd1-e548-3666-884a-c6ae60e2ade6 | -3.52587 | -54.68014 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 13f05275-0d88-3c1c-80a5-50b26467b7db | -4.38606 | -47.75739 | 2024-11-21 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 74d82680-7832-34c4-9d87-e22f6ce92835 | -4.07051 | -50.90647 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a64313b7-b90f-3126-98dd-33fe91cfca32 | -4.84846 | -50.85749 | 2024-11-21 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 442f79c2-c63e-3cd7-bdb2-4e414c2afe3c | -2.60506 | -54.05558 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 435760f6-d345-36de-bd4d-10bcf03f3eeb | -3.54699 | -51.53183 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc848f56-afbf-340b-84a5-2e98bc138ce5 | -4.09483 | -51.07546 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5919da25-5852-344c-8d42-596a12bdd49d | -5.00774 | -44.79955 | 2024-11-21 04:55:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5f7ee86a-ba9a-3863-85a3-ce60c80c72c5 | -3.54276 | -50.53243 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8c85cb39-3043-3b4f-9994-aeeb7da31719 | -3.51081 | -54.68867 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2755412c-8f2b-3e84-a896-3560e577b996 | -3.51153 | -53.802 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4c3974ef-974e-3205-8377-2a1d27df7c9a | -3.33823 | -53.30638 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c007a79-9a73-3d8d-8e52-0dc23aa5ff34 | -3.47152 | -47.68526 | 2024-11-21 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 33910526-2fca-3e8a-82a8-b222bb6af6c1 | -3.28834 | -50.53716 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef20a36b-3108-30ca-8f18-42d17654df7f | -2.59782 | -54.01529 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 468c3e6f-d0d5-3972-ad27-6b5484b00057 | -2.96538 | -53.88187 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48ff39a0-8b26-379d-ae55-a2109250d15f | -3.64891 | -54.22305 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ae40209e-f3ff-3674-86e4-20b080738e10 | -3.10546 | -53.9849 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a83ee70d-5ad1-396b-b3b6-6a7ca4d24e5c | -3.99451 | -54.57407 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1c62fce5-e636-3536-a71e-bfbb433b1641 | -4.25521 | -43.8112 | 2024-11-21 04:55:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ceb508c0-bba6-395a-a5a9-87730c2eea3c | -2.71029 | -53.17266 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2bfc308a-67f2-3aa5-89f5-77c119a78717 | -4.3472 | -46.13873 | 2024-11-21 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b40d0bc-0818-31b5-abcd-0dbce1118423 | -2.76416 | -54.05907 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1949287-cb09-3136-8f78-acc07484d5a1 | -3.27752 | -53.84258 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2455a5f6-c46a-35ab-8efd-a881966650a4 | -3.09675 | -53.21923 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4701b64a-d35f-3dc2-8b59-8c26202500b5 | -3.23973 | -51.29891 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c26f3fc8-ba4d-3cce-bf82-8b5777ded2d4 | -2.77409 | -54.06097 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e55b2482-262b-3e39-9c28-221cdaac4634 | -4.39807 | -47.64959 | 2024-11-21 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b174174c-0865-3503-aa59-e310d63e7ec7 | -2.65784 | -51.68356 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1417afd2-a0fa-3bc9-8e09-fe75efdb6f63 | -2.5559 | -54.04399 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8368330d-9406-310b-8b99-47cc63fe8657 | -3.31664 | -54.08923 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c957bb9-9805-3775-b6d5-ea8b9ab8f639 | -2.99456 | -52.37656 | 2024-11-21 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e61a3fa4-4525-3e7a-b8e5-108e85e33533 | -3.29021 | -53.84808 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 17b5b0ce-5653-3fb5-8a9d-245059a3ba0d | -3.42588 | -54.62538 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0c040235-108b-37d8-93bc-af2e0d3ac6f1 | -3.28138 | -53.83965 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6c8f0654-e8e3-3d3c-aabf-a6fc09904718 | -3.00387 | -51.30578 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 2f3c57b1-5b5d-3c69-9900-5028fce0a49f | -3.00616 | -51.31381 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 38ef931b-c609-30c3-852a-5fa53c02bae9 | -4.00805 | -47.96901 | 2024-11-21 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 394c4d59-af0e-355b-831a-ba384f7525a9 | -4.39539 | -45.59513 | 2024-11-21 04:55:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 60a84c77-03ff-37fc-917c-296ba345970f | -3.82405 | -52.25786 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b40fbdb3-6fec-30b3-99d8-88756d94348a | -2.43468 | -55.44344 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d6f7c8f-cd8a-315b-8028-4d7a02f6407d | -3.41335 | -53.216 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73f958a2-865a-3d76-87ff-f6c19619f547 | -3.66288 | -51.57604 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e33e28b-e534-3a4d-bc52-04895348fe86 | -3.29074 | -49.19573 | 2024-11-21 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 519d8ffc-73ce-3e84-84e0-34edcb2f9705 | -2.76139 | -54.05508 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83561fea-52f2-3cf4-ae91-fb9e05b71573 | -4.68746 | -48.97988 | 2024-11-21 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f79eac18-cd0b-3470-9a35-0a3cc074895c | -3.06849 | -51.36552 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 326de2e4-4fc0-3618-acd4-fd13b1b08941 | -3.56649 | -51.4967 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ffe60984-cdcc-390e-9722-fad770c4e08d | -2.946 | -49.44616 | 2024-11-21 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de7f448e-b2b6-3afd-bfad-ce881b8b4175 | -3.18603 | -48.57809 | 2024-11-21 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e80a324-91ab-36d6-a332-091cbbe25652 | -3.55326 | -51.53664 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14172b5c-f85f-3fe6-b7b6-5bedb00f3f6c | -3.4698 | -51.12241 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98b846e9-ebcc-3454-a1ca-dba3dff9a6c4 | -3.60912 | -54.21648 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a0076ea-b0a5-3404-875f-94039f3de136 | -3.37135 | -50.72569 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe2fb317-082d-31ac-b5c1-db6369ba9a35 | -3.11148 | -53.75272 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12da8cc6-830c-3d61-870e-bded053fd048 | -3.68237 | -52.34558 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ac22409-84bb-3882-bf89-e9f17268cfb6 | -2.75257 | -54.06792 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b4a75cd0-dfff-3484-bf50-ca3ac743d7a6 | -3.03429 | -49.47598 | 2024-11-21 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca616a87-008b-389f-8887-eaaefdb2f617 | -2.79781 | -51.79398 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f3e8d20-dd44-3e2a-92b9-ba9f6b1beeb5 | -3.06835 | -53.29225 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 02ae83b3-6d3e-3cbc-b955-bc4eb2efcf69 | -2.76572 | -52.12097 | 2024-11-21 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 934047ed-a479-39a3-b72b-c1286c871670 | -2.86399 | -53.96503 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47db6ee0-7ffc-3450-b881-31735881f085 | -4.38897 | -47.75708 | 2024-11-21 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8aa068f9-ad7d-34cc-aed5-34fdcd3e0d5b | -3.68164 | -50.22072 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 02a956bf-d68e-3273-bbb5-f56dd34cc0f8 | -3.33926 | -54.07508 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08143bdc-09fa-3d62-a06f-74b66cf9bac9 | -2.93814 | -54.41875 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ecb16d5-f269-321e-9f63-c9de72bd2751 | -3.27906 | -53.01129 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61c9902a-b129-3458-b7e2-0ea452763db6 | -4.09117 | -54.04812 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c9780b8-b81f-3b10-882c-bd4e59602d1d | -2.38138 | -53.66293 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f0245c09-a4d8-356c-b623-c5e9b9ae4cd5 | -2.60645 | -54.26278 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5fb98000-034d-3908-9b00-fafdc81f4b97 | -3.72377 | -52.33764 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 906038a1-4243-34a0-9f7c-650a436bb931 | -2.76435 | -53.21624 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0d37f6b-c3ad-3d75-87bf-e746d476a621 | -3.27467 | -53.01767 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 98f32d33-0a63-3e31-94a5-5b3d8f0daa02 | -2.57686 | -54.08326 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ce2a7763-46bc-3e9a-9409-5676683faa1b | -3.09935 | -53.74378 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b3438f6d-3554-35eb-8b26-dffe64c7af62 | -6.20719 | -46.22334 | 2024-11-21 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 778f2b31-e1fe-3dff-9473-3d8e13203e51 | -3.04263 | -54.40641 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2115ca6-ec10-3f34-8ed9-7202ec1e8e09 | -3.28522 | -53.83672 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6459c96a-078d-34fa-b9fd-2749a8e5369e | -3.51953 | -49.94073 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d439f303-adeb-378d-91cd-6f40a634050d | -2.83916 | -53.97179 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e69cdc60-2173-3d5c-a5e2-da08e50e3f32 | -3.10653 | -53.1785 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README65.md)
