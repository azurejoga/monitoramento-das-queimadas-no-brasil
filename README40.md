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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f636ee9b-4846-31d8-9d2f-2d6b0101d9fe | -3.20765 | -49.22773 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f0ddc46-cdaf-3ef2-b835-52ea580f67a5 | -4.06138 | -50.01792 | 2024-11-06 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d543718-cba5-358b-a25f-07396b933db9 | -3.09708 | -50.2643 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db0ffe81-fa12-3723-9fcc-a02e1b66db41 | -3.71346 | -52.06079 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 981ec040-7fee-3af3-b489-274cb7816ae2 | -3.21096 | -49.22825 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bbce451f-f679-3713-b77f-c4668597c928 | -3.18031 | -50.59832 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8b20ecdd-176d-35bf-8fd3-bb9d8bf9b596 | -5.34365 | -46.46461 | 2024-11-06 04:36:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e68506ad-05d6-383c-870f-9d9fb7a3cbd3 | -4.07112 | -53.94032 | 2024-11-06 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| e1400ebf-0d70-3bce-b449-a6f399e6ee17 | -4.35287 | -46.53428 | 2024-11-06 04:36:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7b121a7-fd34-3dac-94ba-29689d1e0c77 | -4.26489 | -49.16133 | 2024-11-06 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a5752e86-5a9a-3a97-904f-ed2a70b2f5e3 | -2.5761 | -51.33886 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47042ebb-a60b-3544-b41e-2b1ed2f05438 | -3.24962 | -50.18536 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96a49377-b4f9-3890-b5fe-413941a1a697 | -2.52609 | -47.37897 | 2024-11-06 04:36:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c73b987-01fe-32d2-a621-4fd90d012303 | -6.00621 | -38.666 | 2024-11-06 04:36:00 | NOAA-20 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c0437f9c-88a4-327b-85ce-c38f5bd27bfd | -2.81017 | -48.55598 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0ae9d4a-61be-3512-bceb-bb16cb1d5070 | -3.42976 | -49.97297 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54c123ba-6d7b-3bc3-8f21-f53a8b314830 | -2.82845 | -49.43366 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 548f4a82-24c5-3d5e-9914-47c4da93132b | -3.97249 | -48.16515 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 03b83d3b-8dd0-3e05-9ba6-c5c89d6b1e62 | -3.38683 | -54.172 | 2024-11-06 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2766727-0704-3a2f-bcfd-810900641e9e | -3.01702 | -51.4365 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 628c7577-19cb-31b6-b9bf-1a1cbc507be9 | -2.55134 | -49.23071 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4dbad8b4-3704-352c-a209-4dac4bdec56c | -2.82519 | -46.6081 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| faa0c85f-247c-3628-9443-307781c1e317 | -2.43241 | -51.58548 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1baeadc7-d79c-3824-a918-a66717528a65 | -2.82296 | -52.91495 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| af6b3c1d-2a70-37fd-b783-c3af4154f85e | -2.193 | -49.52042 | 2024-11-06 04:36:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c79aa72-e4f2-383f-a325-a068e63729fe | -3.60426 | -42.861 | 2024-11-06 04:36:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 68f8bdf3-54de-38d3-ad37-646313b98213 | -2.60148 | -49.1925 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7920e127-99f0-3114-8aa8-92eb065c2a03 | -3.10579 | -45.93763 | 2024-11-06 04:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de35d860-25a4-33a7-a188-7e2b9ce6fd0e | -4.13012 | -43.58458 | 2024-11-06 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 44490a14-95f8-3e56-b42a-82bad978773b | -3.40156 | -50.2826 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c529222-5c49-3df6-b8ef-e9bb3860d833 | -3.09539 | -53.70977 | 2024-11-06 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a47dac9-2f76-399f-b1b0-ff93e867c1cb | -2.39194 | -46.55493 | 2024-11-06 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 30be060a-17ed-3e13-b166-311ee1bd51ac | -2.844 | -48.45205 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea3c76e7-e309-3285-b3a3-8cdffa1797b2 | -4.58927 | -45.49529 | 2024-11-06 04:36:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2fd7f9d6-4d2d-3740-8dfa-7128e953c8f1 | -3.07788 | -49.57643 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dae19486-5b97-3584-8e12-ebb70893e659 | -4.35584 | -46.5148 | 2024-11-06 04:36:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b0974db-bf01-3f5e-8630-2c9bd37ab552 | -4.65515 | -43.82122 | 2024-11-06 04:36:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 25c4b34f-41bb-3160-a816-9ee70feb6bdb | -4.09684 | -50.50208 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ed9ee309-2c80-36a9-88bc-bfde5d7f3551 | -3.09808 | -45.94054 | 2024-11-06 04:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 368de993-8c67-3754-921b-b83f47bd253a | -3.08357 | -54.51652 | 2024-11-06 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7aefcc4f-082f-36f2-b0a5-d74102146a03 | -2.71926 | -54.14672 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 4dfee397-e6fc-3a5f-9cb9-ee837288eb69 | -3.9547 | -48.14841 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0ee92bc9-0f40-37c4-b4c5-33d5ed9e12f5 | -3.89621 | -48.36992 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e063b0f8-314e-311a-a2fd-8ef9978c5166 | -2.72342 | -51.71227 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fe4b0e09-e40d-37e5-95f3-7b93c3318b18 | -4.02811 | -48.28748 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69991969-5780-38d7-b7a0-fda66c83215e | -3.10441 | -50.26176 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a9bdb6b-adf5-3c28-a979-d0644d8ff7bf | -4.16178 | -46.57402 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4221efdc-04e1-3937-9cf7-fe9f953e4bc1 | -3.76405 | -51.76997 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33a00337-f9ea-3a21-979e-a47e6f47834d | -3.12197 | -48.58369 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6193ef47-2645-38eb-9869-0ec954867115 | -0.96957 | -47.81383 | 2024-11-06 04:36:00 | NOAA-20 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 2c98cd92-3226-3df1-ae2e-45e07ea086fc | -2.72277 | -51.71637 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dd6bc058-b00f-3df0-91e7-a94be0248af0 | -2.34246 | -48.93974 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 662e314f-1e9e-3ed3-8db3-7aa3c44fd1f2 | -3.45689 | -50.38008 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49ed91f4-5fe9-3f8c-8271-f69a5b3d9991 | -2.36252 | -49.54298 | 2024-11-06 04:36:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3221517-7efc-3c60-affc-7249a725aaf6 | -2.63898 | -51.74675 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74c8a055-baf9-3e2f-9d86-d3d4d818ef94 | -3.15798 | -50.20759 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| f99be454-d0b4-31a4-8ed6-23b3c072930b | -2.47002 | -47.93169 | 2024-11-06 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f4cdfc34-6872-39e0-8a88-252ab1299fde | -3.91594 | -46.48256 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e51bdd10-ffb5-37a1-a562-495a8df13bcf | -2.72279 | -54.15123 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 822086c6-4163-3e26-ab23-bcbc3c79cf85 | -3.24472 | -57.56612 | 2024-11-06 04:36:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d9ec242-d365-35bf-a48e-b055d3138646 | -2.51981 | -49.19391 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 323d7b33-4f8d-39bd-98ec-2436af903e00 | -4.06527 | -50.01494 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 38b6f1ce-8a08-30fa-a39a-728c08710286 | -2.97888 | -50.30218 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1213b24d-cb44-3527-ba2f-b978bf78ac72 | -3.33885 | -51.61991 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a5cab2c9-0f33-3e0e-8940-b04046f1e9df | -3.85341 | -46.62265 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| acaa1547-274c-38a2-bc0e-016b36ff3563 | -2.83908 | -52.91255 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| cc05663d-3813-350b-96b0-4119cc506f12 | -2.6749 | -48.51024 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c425eb42-0a67-3e6d-969a-bef0df638cbe | -3.54925 | -47.38947 | 2024-11-06 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| d5e26140-ba68-3500-bf54-70debf5f8998 | -4.34998 | -46.52985 | 2024-11-06 04:36:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d693db8-6b29-3930-b4a0-09a1571af39b | -2.95371 | -51.05665 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc9ab9d9-51cb-3b74-bc08-57ac30436ffa | -4.75133 | -45.90712 | 2024-11-06 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a83b491f-1b85-3ab5-9423-e1d5a12bcc6c | -5.2573 | -46.17199 | 2024-11-06 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8bab1f5-796e-3b63-869f-336d3c2f2685 | -3.10225 | -45.9371 | 2024-11-06 04:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5a92abd-0d45-3c8d-bdf6-25f55d569c1c | -3.52245 | -51.67136 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b74d832-e6b2-355b-a135-9053511990e4 | -2.89399 | -48.6075 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18c9dcf3-fe49-3fe0-a0c0-3c0b8a909570 | -3.30464 | -50.14272 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b11bdc93-d4f7-3b2e-9645-711b977f1226 | -2.8209 | -48.46625 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| daa76854-fa82-358f-883e-3e04023641f4 | -2.29514 | -48.5492 | 2024-11-06 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a50c746d-d888-3c62-9644-f0b8b686a889 | -2.95112 | -48.63406 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9573f7bb-7130-3ce4-9e8a-f2d20fe54711 | -2.83831 | -51.35365 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3ffb6cf9-4e11-3e97-a881-545b4e5667e8 | -3.43253 | -50.25079 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf69c4d4-a804-38f5-b52e-abc532ec3318 | -2.45086 | -49.02723 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| f32570e1-5f04-3141-ae56-ffb970e367aa | -3.09112 | -50.27168 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2bddf675-713b-3cbf-9895-6ba6e23d2d2e | 0.18831 | -51.06908 | 2024-11-06 04:36:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea49e23a-09df-3e6f-8b21-3e031c83dbc8 | -3.11828 | -53.12662 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60e9c750-14e5-3f2d-9310-c8e838e6f737 | -4.21699 | -53.56482 | 2024-11-06 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3774aa77-6625-3f21-b9b7-b7596296d40d | -3.03921 | -53.26771 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c182cce1-e807-3f8e-8976-67911030d339 | -3.18148 | -50.59097 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| faa499df-ac36-3df3-b0fd-6abf6f7660b3 | -2.60352 | -51.30248 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46000904-bc5a-3d51-962e-68d7a0b6eda2 | -3.00956 | -51.3913 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f359fc3-972d-356d-ab0f-075ad7ae36d9 | -4.28056 | -48.649 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0cac2d14-96e8-3f5c-a7db-134357f20916 | -2.45308 | -49.03464 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c03cc01e-54d9-35b1-be99-030c8c99bbc3 | -4.2224 | -50.63611 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1fcd9e3c-c84e-3133-83d1-eb914096562c | -2.48003 | -53.984 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a14557b8-2f85-392a-8c79-b85569bf6ad9 | -2.17455 | -53.70198 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b7686b7-0deb-3bb4-bc69-0b56c54962cc | -3.22485 | -50.38452 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| ee3613dc-0750-37b2-bd27-7a6d5da8b480 | -3.59588 | -51.57657 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0dc5b8ff-9413-3f6e-af14-e5602dfb041c | -2.67322 | -52.52036 | 2024-11-06 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c22b3195-1019-3909-9a03-969b31331998 | -2.77501 | -51.61062 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48db3927-9d6e-3449-beed-0e9d2e41d13b | -3.12143 | -48.58712 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README41.md)
