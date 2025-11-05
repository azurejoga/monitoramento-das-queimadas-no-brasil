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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1444c2b0-7c6c-323d-ad6e-c756c61e9b6a | -3.47825 | -43.63145 | 2025-11-05 05:01:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9ce4fa83-f51d-3491-b204-a03192ec7823 | -3.45415 | -50.22288 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1eadd3f4-76bb-3996-9c9a-4d3951ad1a33 | -4.92207 | -46.72149 | 2025-11-05 05:01:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39873f12-c12b-3cdd-b139-7c2c6f3d5bfe | -2.79678 | -50.31348 | 2025-11-05 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6a8cb8a8-c872-30ca-a68a-e6a7752768b0 | -2.39519 | -47.14881 | 2025-11-05 05:01:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0203ec16-3a6e-383f-9eb7-ed13da9ab3aa | -4.23862 | -48.66702 | 2025-11-05 05:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8067bb4a-a75c-3804-9b76-2c2789be2271 | -5.05715 | -45.82862 | 2025-11-05 05:01:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f28f3ee4-3fd5-3ee8-a39a-46ba8cbce68e | -5.43064 | -44.65856 | 2025-11-05 05:01:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 56a790ec-7f31-3471-9a18-03bdc755595a | -2.84553 | -49.40614 | 2025-11-05 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6dfbb0d9-4af5-3b13-92f0-9ebce3f05e14 | -1.27674 | -49.14651 | 2025-11-05 05:01:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 815873da-4c1e-3927-a2d0-e8218e82296f | -2.97045 | -47.36716 | 2025-11-05 05:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06ff0939-fa58-3336-9601-715daf39b4e0 | -2.57994 | -48.40599 | 2025-11-05 05:01:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09dfd6ea-fe54-3574-aedb-4c3dc8751002 | -3.44234 | -50.22097 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b140ed89-9ae4-3487-8e31-b42877c4dc51 | -2.3514 | -48.48699 | 2025-11-05 05:01:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7bc1ee8e-9961-3fa6-8c84-3a6857495530 | -6.07463 | -43.25204 | 2025-11-05 05:01:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 8.8 |
| fa9a28d7-8e73-345c-856e-e43d13947fcc | -2.65451 | -48.51084 | 2025-11-05 05:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| f4ed63ac-365b-392c-aee1-35003a400e8e | -3.4261 | -49.17071 | 2025-11-05 05:01:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5bd9aece-7f43-3f3c-b1a7-3f1787c77197 | -6.42277 | -43.06837 | 2025-11-05 05:01:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f45941bf-1f2b-3b83-ac83-3c8098c40ce6 | -2.45571 | -49.42419 | 2025-11-05 05:01:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86317a21-978e-3dbb-939a-946e254ae7a6 | -3.07283 | -52.62817 | 2025-11-05 05:01:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c5f0941-482a-30d0-85a3-e97371d942e6 | -2.65576 | -48.50243 | 2025-11-05 05:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f0dfc84-3540-33a2-8ae6-601155cb05e2 | -3.48533 | -43.6238 | 2025-11-05 05:01:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 25a6697b-3ca8-3bab-a394-4f8391441668 | -3.47613 | -50.02795 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08488943-8771-32f6-b71a-72c775038361 | -3.3121 | -53.84063 | 2025-11-05 05:01:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee6e612a-8fe6-35d9-adda-e07d29d3d45e | -2.44578 | -49.03476 | 2025-11-05 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 396f009d-0c6d-37e5-b9d5-e0afb3c6f505 | -2.62096 | -46.85528 | 2025-11-05 05:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e612dd19-8ca5-303c-a12b-d739f79f04bc | -4.71117 | -46.43824 | 2025-11-05 05:01:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| de29491c-8a1a-3838-b1a6-f25e2b0cea9d | -5.1113 | -46.22451 | 2025-11-05 05:01:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 533f26cc-4860-3a81-8e34-ada762916257 | -4.41833 | -48.94851 | 2025-11-05 05:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 2b9a2095-1c9d-377d-92c6-bb06131db7d1 | -3.3221 | -53.84217 | 2025-11-05 05:01:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bac515a7-f8f1-399f-880d-f35c20b8a2cc | -3.41616 | -44.43842 | 2025-11-05 05:01:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b12ac099-c31f-3644-bc0b-a544167c3d83 | -1.28083 | -49.14715 | 2025-11-05 05:01:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0367dd02-23b9-3fb8-8c72-66fb41372985 | -3.33351 | -52.0951 | 2025-11-05 05:01:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d417b90-6292-3c56-8845-8a081894157c | -4.86243 | -44.61833 | 2025-11-05 05:01:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 435d0799-7934-3c21-b284-d86234c33a97 | -5.05865 | -45.82749 | 2025-11-05 05:01:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| abec8b83-e2d2-3716-b102-5fe773a08e2d | -3.72329 | -54.21566 | 2025-11-05 05:01:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe2c8cca-06c9-3000-b4d2-c38615b79b9a | -3.4842 | -53.28004 | 2025-11-05 05:01:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c445fcc-5ac2-3480-8387-938d2ca28a50 | -4.18224 | -48.59372 | 2025-11-05 05:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88b824f7-11c5-3811-bdd8-3b82dd274c99 | -4.45721 | -46.63784 | 2025-11-05 05:01:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 32c501c5-42d2-3801-9474-369fc069fb31 | -3.33353 | -44.35565 | 2025-11-05 05:01:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bf463bff-32e9-32b8-820f-486abff7302e | -2.8432 | -49.83245 | 2025-11-05 05:01:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e871dc09-1ecf-3e24-bf69-5030b13907f5 | -6.09837 | -44.44123 | 2025-11-05 05:01:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8a5cdd2-94b3-345c-8274-1b1d3b81de77 | -3.38714 | -54.27685 | 2025-11-05 05:01:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a5f6f31-7dd3-3b9f-a0f5-231c7a0207d8 | -3.2418 | -52.91765 | 2025-11-05 05:01:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e9dec61a-89fb-3c69-8ec0-6c4ecc92e70a | -3.51264 | -55.49749 | 2025-11-05 05:01:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97f6c8e1-4e82-3483-89c1-5ec220e5a948 | -2.83205 | -49.41173 | 2025-11-05 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3cc943be-2e01-3353-b694-e3f7f99df633 | -2.78617 | -50.31338 | 2025-11-05 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8dcf2835-5a5d-3207-8eab-6de3334e897a | -4.28654 | -46.93328 | 2025-11-05 05:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ede1015c-ed0f-3b0f-8d59-5c633d8aba50 | -3.23421 | -46.87522 | 2025-11-05 05:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f62fe4c0-8495-380c-8466-99c48d401bde | -3.36878 | -44.2399 | 2025-11-05 05:01:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8e0289cb-faab-3838-aa0b-fc2389f67e09 | -4.25119 | -48.55902 | 2025-11-05 05:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b09a49c-1f93-3d1d-b12c-832ba47b7fe4 | -6.07429 | -43.25177 | 2025-11-05 05:01:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 8.2 |
| d901f401-be5c-3ee6-9f70-22fc7f574fc0 | -2.98649 | -51.35228 | 2025-11-05 05:01:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc35fbd0-e611-37eb-b0d0-a8393dcae408 | -2.79005 | -50.31397 | 2025-11-05 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 27761524-e941-3dac-8ea7-4f52ea6ca47d | -3.81863 | -52.35914 | 2025-11-05 05:01:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69825c4c-8148-3b74-a9c0-e7f661cc4a85 | -2.84853 | -49.41423 | 2025-11-05 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02031532-e831-38f2-8763-ddad98fc17bb | -3.24 | -46.8702 | 2025-11-05 05:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eebbbbb5-9c5e-32eb-a25c-ef31941f8d30 | -4.20307 | -46.31084 | 2025-11-05 05:01:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a256544-8b96-3c4a-b83b-e55700b3619d | -3.37468 | -44.24085 | 2025-11-05 05:01:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7418ae29-c3c3-3e48-bbea-4c4524fc516e | -2.78306 | -54.02638 | 2025-11-05 05:01:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dc81e3eb-7d67-3f96-893b-c391dd087e1c | -2.817 | -48.44684 | 2025-11-05 05:01:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea80c46a-394e-3dd8-a77d-f3bb431209c2 | -2.84497 | -49.40989 | 2025-11-05 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c57d5ce8-c0ca-3acc-914e-9e00236307ae | -4.67115 | -46.306 | 2025-11-05 05:01:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d7f02ad6-8dcf-3349-ab83-14740de8485f | -3.49826 | -49.55497 | 2025-11-05 05:01:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0dab53a8-62df-34cc-ad93-5d4a3fe05fe4 | -3.60335 | -50.62389 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3a75b85-0864-33b0-920a-104e1699faca | -3.32045 | -53.85269 | 2025-11-05 05:01:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6dcef2d5-3578-3960-ace7-bb1e9db85618 | -2.62386 | -49.22871 | 2025-11-05 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9ce8965e-5fd8-3afb-8208-fae8ff1a62a0 | -3.79479 | -44.04276 | 2025-11-05 05:01:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f692ca00-b1d3-3ce4-b216-7ad78ccf730d | -4.41457 | -48.9437 | 2025-11-05 05:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 9ecfe40e-416c-3ba6-9d61-d9fe54b5bb27 | -3.01808 | -51.09334 | 2025-11-05 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7e7fc47-6800-3528-9d48-4fb79266fd41 | -2.39595 | -47.14576 | 2025-11-05 05:01:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1bf53ac-85c1-351b-b780-581e1a492454 | -4.28154 | -46.93253 | 2025-11-05 05:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a578489-f6cd-325e-9898-45938a56e7c1 | -5.06221 | -45.47784 | 2025-11-05 05:01:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd374158-a517-3268-ae8c-425f7b2ae35d | -4.45298 | -43.21602 | 2025-11-05 05:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| db732350-ac06-303a-aa71-dce410eb7f37 | -3.24429 | -50.80164 | 2025-11-05 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a075844-89e3-3eb3-b63d-4bbbb6ca32cd | -2.73956 | -49.39085 | 2025-11-05 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64639018-cc80-3730-9939-a30121ee398c | -2.38169 | -53.98154 | 2025-11-05 05:01:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7eb3aea2-4884-3bcc-94f7-a3ccb3a23135 | -4.71926 | -49.76655 | 2025-11-05 05:01:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a1703f9-ccb0-34a6-ac84-66077281a497 | -3.82418 | -48.66991 | 2025-11-05 05:01:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 62e83b7f-1b70-3e6d-8ced-bde286d462f0 | -2.79078 | -50.30908 | 2025-11-05 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eb614842-690e-37f5-9753-77515ed67fd3 | -2.78437 | -50.31661 | 2025-11-05 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| e5ef43bc-c7a2-32f9-8b88-f9c0cadc748c | -3.50825 | -55.50027 | 2025-11-05 05:01:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2cdc789b-d27a-322f-9fb4-79b7ce05549a | -3.23829 | -46.88181 | 2025-11-05 05:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0807208f-e2f5-3895-bff4-3cc792cdf051 | -2.25143 | -47.99068 | 2025-11-05 05:01:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 621c90b0-ca5a-3262-9f91-63e3a1328dbd | -3.99165 | -47.72058 | 2025-11-05 05:01:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30da4b8d-cb87-35a5-b6fd-f458ec178d8d | -2.45654 | -57.90795 | 2025-11-05 05:01:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6724de10-085a-35ad-92e3-564e124fc400 | -1.26445 | -49.1446 | 2025-11-05 05:01:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bb232497-cf4b-3eac-86ac-5a8587dfb255 | -3.40956 | -50.83577 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8373dcaf-a725-350f-924d-22488f52edcd | -2.19929 | -48.3588 | 2025-11-05 05:01:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 658fddca-501d-3ca7-8ded-9539154a3346 | -3.24192 | -50.79181 | 2025-11-05 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 731e8ba5-7fe2-3a5a-ad87-ec8fb0dabf3e | -2.89291 | -51.01496 | 2025-11-05 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fff0038c-ac99-3d26-b661-e292529524c6 | -2.98018 | -48.70999 | 2025-11-05 05:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e268abb1-ef0a-3e77-a153-d084b16b00b9 | -3.44781 | -50.21167 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54c008b0-ae03-391a-98b9-a0db99fca8df | -3.91111 | -54.5604 | 2025-11-05 05:01:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 67aa2fc8-2c76-36eb-8efb-3e3564edf2dc | -3.10406 | -49.46389 | 2025-11-05 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00038436-3954-3eb2-bb8f-225782cebe17 | -3.14283 | -50.2888 | 2025-11-05 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e509c05-c052-3700-9cd3-a2f8464dba7b | -3.65539 | -54.58721 | 2025-11-05 05:01:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09dfc793-176f-3c5c-8fe6-cfb17b51bf2a | -4.55691 | -46.76357 | 2025-11-05 05:01:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5de512cb-e638-35cc-80a4-f848ed0a8252 | -3.22514 | -44.40294 | 2025-11-05 05:01:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 12b6f587-f17f-3420-a003-7ef36eb8b62e | -2.80376 | -49.87613 | 2025-11-05 05:01:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README32.md)
