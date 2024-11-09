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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 30a3100d-8434-3152-97f9-a14b720a50bb | -2.48059 | -54.05416 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| caba695c-8d5e-3182-a97c-c5e21f72d251 | -3.20048 | -46.49203 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e988be9-ae7b-3666-972b-f1cdaa13fc61 | -3.33793 | -50.07984 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9c0dc268-d769-322e-9d5f-0c6239667b14 | -3.64068 | -45.89187 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac1751e4-f5c4-318f-b16d-f7816ae36307 | -2.91987 | -49.36002 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a74b37c-1a3d-3c6c-ab10-9abcb7ef7f04 | -3.53738 | -50.32832 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 24616f8c-625c-3be3-af8e-1f01b8ec049f | -5.4472 | -44.81945 | 2024-11-09 04:33:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| aca32706-40e4-34d2-9b7a-eeac38871300 | -2.73673 | -51.71484 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 437f0d4d-9ccd-3bcd-91a8-25ff604422c3 | -3.77252 | -52.05553 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc2050db-a35f-35d3-9075-04109330cbb4 | -4.0142 | -48.29728 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6184f50-fd32-3b72-beb0-17f805589f12 | -2.83588 | -49.47081 | 2024-11-09 04:33:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b09628e4-ae18-3d39-b029-0d9319ff1497 | -6.44084 | -42.0634 | 2024-11-09 04:33:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| f243ae06-0980-3c65-ae71-99a0dd3e97a6 | -4.36685 | -48.15334 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50dd66ac-ee19-38bb-98d5-8dc62b5a6af5 | -4.24502 | -48.53801 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84c7e420-491d-3334-8ed3-abc13afcff7c | -5.80932 | -44.48348 | 2024-11-09 04:33:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8b6d83e-5488-304e-95bb-757250507fcb | -3.27187 | -46.31749 | 2024-11-09 04:33:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81215323-cb40-3e3e-afe9-de756d32c635 | -2.88854 | -48.29328 | 2024-11-09 04:33:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 29608200-e020-383d-bb98-528a91a73d30 | -6.26797 | -44.54518 | 2024-11-09 04:33:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 425160b0-eeec-3c9d-8528-1e468f348ce3 | -3.02968 | -50.35402 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 761717b2-9d41-3910-8a3a-6469a765fa1d | -6.28833 | -47.34945 | 2024-11-09 04:33:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c8fedb2-ef8b-395d-a293-6138a1595e29 | -3.3563 | -50.12355 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 085f2949-474f-3da8-9eab-1eb43293ed6d | -3.67379 | -50.22444 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a0645565-66ec-3832-9b50-3a986b36c1dd | -4.01876 | -46.54432 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0250ca0-c639-31f3-8fc8-9b688a09dd14 | -8.84813 | -47.68062 | 2024-11-09 04:33:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1d0c1b3b-2cef-3961-82d1-f6dec2ac101f | -4.23049 | -46.88992 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 42dd107e-6a57-3c81-bc92-dbefaebbe03a | -4.41639 | -45.61782 | 2024-11-09 04:33:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1714a57a-229f-34ab-9ff3-5221a9d48985 | -3.50015 | -51.02969 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c3dc352e-5360-3267-9d39-5eaeed106385 | -2.88761 | -49.38956 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac50a4d8-940b-32b8-9889-af413c309833 | -3.87212 | -46.65686 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 372e4d50-f319-334e-9853-cc3be58441dd | -2.86868 | -49.37502 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79cf867e-4df0-3ec5-be48-3fda386011a9 | -5.1383 | -47.70339 | 2024-11-09 04:33:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dec0df78-ee14-308d-be14-e6502fa5e803 | -3.4537 | -49.11526 | 2024-11-09 04:33:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7f7c317-7954-3e31-ba9d-a01d5168d118 | -3.17546 | -46.58763 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1a4f913-7581-357a-b08f-426010666939 | -4.464 | -48.11945 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e82e5b21-3074-33f8-83bb-d923acea31a8 | -3.19589 | -48.65675 | 2024-11-09 04:33:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b47cc8e5-f0dc-3953-a05d-a66e59cc689b | -5.46785 | -50.89405 | 2024-11-09 04:33:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44419bbc-ca15-3fd3-8073-bbd6bb1b4305 | -4.1844 | -48.79667 | 2024-11-09 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7791012d-bfcd-3a00-907e-bc5782f2164a | -2.65969 | -49.87339 | 2024-11-09 04:33:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e11b311e-e699-3815-a67b-37e63da27079 | -2.85681 | -48.45105 | 2024-11-09 04:33:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fb213989-8ea8-374d-b7ea-d46bd21af15e | -4.29624 | -48.64692 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 87abb7c7-351f-33ab-b2d7-ed6d59bf352f | -3.59149 | -47.34743 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 90edf3bb-77fb-30da-979c-95d23c8c7d58 | -3.96462 | -48.99744 | 2024-11-09 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb7090e4-ff81-3064-bcf7-13d8eca56d87 | -3.44489 | -45.98668 | 2024-11-09 04:33:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fafbfa3a-8fbb-331a-841e-5128cc5eb47a | -3.23858 | -53.39657 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67d7ac45-3970-3093-b460-2e96bc483201 | -4.06674 | -48.30961 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f45a8f4e-9bba-30a3-89de-67c483647316 | -4.47894 | -45.66904 | 2024-11-09 04:33:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bf42a253-1ced-34d7-8ac9-011532e5d495 | -3.03394 | -48.04005 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 217a99a6-815a-37eb-b285-615dc91738dc | -3.87537 | -46.63597 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab4c8537-d604-3d3a-9f29-2483243b55ae | -3.34185 | -50.07742 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 393bf442-d59a-36a1-a456-c51ccdc3c2dc | -3.62963 | -43.79701 | 2024-11-09 04:33:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 84a872bc-d1e2-39a6-8cdd-81fd10e23276 | -3.12332 | -50.15091 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| eb81a8de-58f7-36fe-9d1e-f0a6aedffb2c | -3.07885 | -49.55866 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d20970d2-fcb0-3aaa-ac18-9b34bfcdbad4 | -4.39416 | -50.97079 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37acacb3-35d1-3a57-a9fa-c0d599c6b837 | -4.07506 | -48.3216 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 982a03d9-4fa8-3d09-96d5-13ccaff44d05 | -3.59532 | -47.34451 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 1c5863b2-8872-3005-9b38-26b72b7dd946 | -5.5642 | -46.29488 | 2024-11-09 04:33:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e3302a1c-32dd-3af3-85da-34ce4730b8a0 | -3.42602 | -49.24662 | 2024-11-09 04:33:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1833bbc5-6408-3939-98af-0533d135ee5b | -3.27666 | -53.41956 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 032d6bcc-e2d4-3182-857b-da2aff1b12ff | -3.54788 | -51.53953 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| df978d37-bdb2-3fb8-b34b-899781a4dbd4 | -4.02319 | -46.18751 | 2024-11-09 04:33:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 625186e3-ee54-3681-aac9-7c81122fb569 | -2.98808 | -49.53354 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8bd3f8be-3913-31fb-93ae-c3141bbf3180 | -3.97689 | -48.16683 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47a758a9-76c2-3790-a26a-352f186aec9b | -3.79791 | -46.49913 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24c01542-b86f-3d87-b5db-faa6cc79ca95 | -3.60293 | -51.24434 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e7ce1691-d3ce-38b9-9375-d7afc3cf6257 | -3.25162 | -51.13065 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ad48aa69-494b-317a-96df-73033d73e502 | -4.84673 | -48.62922 | 2024-11-09 04:33:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6017dbf5-2223-33e1-971d-66f2055661f2 | -2.87602 | -53.96621 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 703e95c2-e312-32f4-b8c4-4de5044eb1da | -3.75182 | -54.74598 | 2024-11-09 04:33:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8f4a169-1d42-3565-91c3-ba4cfc8a95a9 | -4.61817 | -46.53939 | 2024-11-09 04:33:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff09e4ec-b840-39b2-9422-cdea884f7337 | -3.91225 | -46.44141 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c006d38-41c4-3703-868a-10699cd9f3ad | -2.9346 | -51.04916 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe2fe441-08f0-3d38-86f5-8270f58d9918 | -3.73356 | -54.22078 | 2024-11-09 04:33:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 99791783-8ca1-3dc4-9ae6-7f3ddb5b240c | -3.03326 | -50.3082 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 2f2f9659-4996-39e6-a39e-984297bc5b38 | -2.47625 | -54.05236 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ade6b7e8-5ca6-3c32-85ca-c07fff79cc67 | -3.76306 | -51.02144 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2dab3b44-f07c-37d9-baf2-c9c4de751588 | -4.68445 | -48.77342 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4f09ff6c-e26f-338c-aaf2-6130fc46a00b | -3.04342 | -50.3604 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eed37e76-5980-32eb-97d9-7d2e7aeec897 | -3.30875 | -50.08035 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 10e7e5f7-23ec-3cc9-b543-e715a2ccf6e3 | -3.78158 | -48.88758 | 2024-11-09 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 321a18a9-ac53-38ff-b7c8-d0cd9da5cfb3 | -3.3486 | -50.26269 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f96c33b0-6dbb-34d3-be3a-801fc95ca947 | -2.63567 | -51.7172 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b94fcc21-50f2-36db-b02c-c8061fee193e | -3.12041 | -50.14631 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ab53b1fd-91ff-3b6e-82a8-f4a842fdc14c | -3.47952 | -50.80316 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 07c63879-f989-3461-ac8c-8d927a06db6a | -2.67542 | -51.82257 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 3088a442-3984-3aee-be37-0358ed6ce986 | -2.86072 | -48.44802 | 2024-11-09 04:33:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 11e188a9-c189-3d8a-8a55-2dbb05bfc432 | -3.84755 | -46.44241 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11fa5b18-6094-3dd0-bcea-2eac826e5261 | -3.68208 | -51.30297 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 72318fe0-3507-332d-b2d7-d36121053544 | -3.24591 | -48.74507 | 2024-11-09 04:33:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f5e4833-2f55-35e7-8c3a-6f6d3e825b39 | -2.60731 | -51.30469 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9068cac-76f9-3011-8a5b-3f927b990a8e | -5.16691 | -45.277 | 2024-11-09 04:33:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49c4b7af-838c-3829-ba65-834ab18421df | -6.27653 | -44.53778 | 2024-11-09 04:33:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4154b9eb-9afe-3fe4-8054-bcf11b47fb12 | -4.13877 | -46.91121 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 517a2367-d239-3f10-aae8-2e0f6ff7106f | -2.65679 | -49.86888 | 2024-11-09 04:33:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8c1a62c-ef40-309e-a858-c7ec01f3f7bb | -3.20662 | -50.63293 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 5004316b-057e-346f-9d09-805b4865a5f9 | -4.12655 | -43.595 | 2024-11-09 04:33:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 55ac075f-6615-3e29-aa42-52d17afb36e3 | -4.22531 | -50.64874 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3e8ed05-e760-3687-9c50-7bc5de2d54b7 | -5.13568 | -48.23971 | 2024-11-09 04:33:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ec00aa64-5a65-3d29-a503-fc6306466276 | -3.03816 | -50.30054 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 061bccf0-8aab-30ec-8dca-7d3e13076008 | -3.78877 | -46.14108 | 2024-11-09 04:33:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 34ffd9ff-6f94-33d7-a85c-38beb4d5034d | -10.21355 | -36.23997 | 2024-11-09 04:33:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 24.8 |


[Clique aqui para ver as próximas entradas](README48.md)
