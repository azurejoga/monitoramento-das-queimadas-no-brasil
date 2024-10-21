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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09bdc5fd-5398-3eee-8f6a-02a4f2b0511d | -3.93089 | -52.22678 | 2024-10-21 05:29:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84a9df94-5721-388f-aacb-756ea74ca32a | -3.88739 | -51.1931 | 2024-10-21 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e76896a3-0276-37e2-af6d-7e08898d9146 | -3.88679 | -51.19714 | 2024-10-21 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c9301bb3-3a8f-3b1f-a448-4c5c90a2acba | -3.87605 | -51.19471 | 2024-10-21 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b1eff9e0-f137-3a01-b283-0ae0ace05364 | -3.87521 | -51.19559 | 2024-10-21 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6cd05a9d-ff30-3b62-a815-d6fe6e531a45 | -3.86855 | -52.19979 | 2024-10-21 05:29:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca4f762d-4a94-33df-bcd2-6c99d2dd4d64 | -3.80712 | -51.13517 | 2024-10-21 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11030f12-40bc-3a45-970a-dbe9ee25befb | -3.79571 | -51.8068 | 2024-10-21 05:29:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83f6c951-b8e4-31e1-b921-fa99592e8665 | -3.79531 | -51.80657 | 2024-10-21 05:29:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 141a0910-62fb-3c0b-82ec-159dd2aab161 | -3.79017 | -51.80596 | 2024-10-21 05:29:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85363ba8-54b1-3102-a54e-19aacc156d92 | -3.78976 | -51.80573 | 2024-10-21 05:29:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84cdb54c-69e3-3f7c-8da4-4a12dd7b075d | -3.72491 | -51.33011 | 2024-10-21 05:29:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ea008c8-9f58-3923-b164-6d91d327f110 | -3.68313 | -51.84294 | 2024-10-21 05:29:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d6effbc6-9dba-3255-86d0-34e3d65a4a0f | -3.68264 | -51.84525 | 2024-10-21 05:29:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 710bb845-9e3e-3bcd-93ef-248a8b2ea9e0 | -3.67761 | -51.84209 | 2024-10-21 05:29:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 115d5a27-4a9c-3ee3-8137-30ff3f1b3fa2 | -3.67712 | -51.84436 | 2024-10-21 05:29:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 783b80a8-92f3-3202-acc7-f2228008356d | -3.47514 | -52.21871 | 2024-10-21 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fdfed4a1-6a8b-3d76-9c84-1cfe8c2f307b | -3.46976 | -52.21796 | 2024-10-21 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c19a0402-b187-33b2-bcb7-e5901f8b25af | -3.46925 | -52.22141 | 2024-10-21 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65293207-d879-3cd5-a899-333e39353321 | -3.46437 | -52.2173 | 2024-10-21 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2eb05675-3200-3fbb-8899-08d70b57c117 | -3.54517 | -53.02185 | 2024-10-21 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24de1dfd-d122-317f-9898-6a7f2b6411be | -3.4047 | -53.17677 | 2024-10-21 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36c5cdf4-726b-34a7-94f1-644a92b9d9bc | -3.39966 | -53.17607 | 2024-10-21 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7c4cc22-25d2-3d09-b9b3-d0bd65f252a8 | -3.79302 | -52.32198 | 2024-10-21 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4fe536ca-3edc-3b44-83a2-2d6dca3e0beb | -3.7925 | -52.32547 | 2024-10-21 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40375e89-6b28-313f-af4f-3d6b3385e2b4 | -3.77527 | -53.40577 | 2024-10-21 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a3a0cb2-ca79-37ae-aa67-e1812f33f811 | -3.77171 | -53.4023 | 2024-10-21 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0a3ed09-57c1-38b7-833d-1ee2914d686a | -3.7713 | -53.40514 | 2024-10-21 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3487f49f-4394-3f9d-bd2b-a4a8e207d774 | -3.77075 | -53.40205 | 2024-10-21 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23e57bca-c909-3070-b6d8-de0b2adf25bd | -3.76674 | -53.4015 | 2024-10-21 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ef6deb4-5520-34e5-a50f-73bed99c5556 | -3.77032 | -53.4049 | 2024-10-21 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45db1741-a155-3e60-906e-d02f1f386982 | -3.76715 | -53.39862 | 2024-10-21 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e5e56229-5349-3d05-8385-600ee84a9c80 | -3.7438 | -53.41224 | 2024-10-21 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5b52739f-683d-3a21-bacd-453a7069a058 | -3.56717 | -53.53757 | 2024-10-21 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 22a4306a-1722-34eb-a13b-c9b2c7cbc83d | -4.27331 | -53.72554 | 2024-10-21 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06c5adca-da90-3ff2-a9f9-2dc30c97c5f7 | -4.27098 | -53.72472 | 2024-10-21 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de21d34d-016b-32c0-852f-7ed77d605cce | -3.68475 | -53.80714 | 2024-10-21 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8b26af5d-8157-3914-ae8d-031b5885819a | -3.43773 | -54.12509 | 2024-10-21 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ccc7d091-4b78-37e8-a6c5-f3b48472bf45 | -3.27973 | -54.1577 | 2024-10-21 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8eb24d3-0b13-3fae-b6cd-e4c2b52d7a05 | -3.26651 | -53.78534 | 2024-10-21 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| bcae54d1-bf9b-388f-a66a-9d3db18189e6 | -3.26255 | -53.779 | 2024-10-21 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0884351f-9978-3ef6-8e9f-c9b484771dfd | -3.23511 | -54.15008 | 2024-10-21 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a34fb5ad-676b-3c90-bc1c-13c64faa7dd3 | -3.23286 | -54.15073 | 2024-10-21 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 574cbb8b-77f5-3e5e-ae8a-17482110f19c | -3.21586 | -54.8596 | 2024-10-21 05:29:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18ebedf8-6b3a-3d54-a6e5-af10567dd47a | -3.14161 | -54.35927 | 2024-10-21 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fc5a682-ab2f-3759-ab89-c365011ccef1 | -3.13915 | -54.28064 | 2024-10-21 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bf2f07e-396e-3a9d-810b-8b187b829947 | -3.13699 | -54.35863 | 2024-10-21 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c400740c-562d-33a3-a760-0d553b4a1efe | -3.13379 | -54.28482 | 2024-10-21 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 275909c7-ecf5-3908-bdd0-18888274a577 | -3.13309 | -54.3532 | 2024-10-21 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed0976d2-17e7-315c-9878-ec5af1216cbd | -3.42096 | -54.27459 | 2024-10-21 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 39e048be-97fa-30a2-bb2d-adfe367aeb2c | -3.29875 | -54.69127 | 2024-10-21 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c173f11-1533-322c-a589-44a3515a6bb2 | -3.27507 | -54.15684 | 2024-10-21 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3942a53b-3753-3586-9b2b-f87bcdcab4cb | -3.26173 | -53.78446 | 2024-10-21 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6d310286-fd80-3c44-b190-74cc1573c326 | -3.22033 | -54.8602 | 2024-10-21 05:29:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9e59e60-2d25-385b-bb4c-4ffbc4a2453b | -3.15231 | -54.35082 | 2024-10-21 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d39ed770-7600-3d01-8c64-dec6264e9a21 | -3.14769 | -54.35017 | 2024-10-21 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 163a5f40-8512-38d5-9d84-a024770956fb | -3.13843 | -54.28548 | 2024-10-21 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fb45f4d-d398-3fb2-8b04-776480aba2e3 | -3.1345 | -54.27999 | 2024-10-21 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e65c8e6-ba38-3892-900b-461f6a80dd30 | -3.11332 | -54.24044 | 2024-10-21 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aae65394-7acb-3a4f-a0ac-f88f70e5df56 | -3.10835 | -54.16621 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| da208285-0d0e-3754-beea-5d9534bc5e98 | -3.1083 | -54.18005 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| b8611c5e-850d-39e0-a7b5-c45cb1965bdd | -3.10762 | -54.17126 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 61785067-854b-33ef-bd3f-4f20dc3ebcde | -3.10757 | -54.18481 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 5fc98784-eb22-3463-8f32-bc3275e3ace8 | -3.10691 | -54.17616 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a5729e70-8ab4-30fc-be41-0fa1deecdb1d | -3.10621 | -54.18101 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 12937b6d-df82-3caf-b298-c864eb279acc | -3.10589 | -54.16456 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 90e557ff-ec08-3d61-98c5-52769fed08eb | -3.10552 | -54.18578 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ac48c17-d4dc-3831-aa75-b2da0ccdefe7 | -3.10512 | -54.16963 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| b330cd73-e73f-324c-9be2-bf3fb35a3435 | -3.10436 | -54.17458 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| f04d1ba7-7999-332c-8da3-bc5eaf98b093 | -3.10123 | -54.16382 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9cbd22f9-e14c-33d8-9ce8-41c46ad5165a | -3.10045 | -54.1689 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 00d13625-c288-3e2a-9759-8964ecb68a5d | -3.09821 | -54.18365 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 6a956a4a-8ce5-3cb6-8df2-7f55eba00603 | -3.09747 | -54.1885 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5f0cce5c-41ed-35c2-abab-25078b75d87f | -3.09734 | -54.15798 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8c649c79-f85a-35b8-97ef-3be84ed5b864 | -3.09656 | -54.1631 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 47836c0a-3612-39e6-ad0c-9632d89f7365 | -3.09503 | -54.17317 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 1edcd13d-f986-3197-b1e8-0f141713450d | -3.09343 | -54.15221 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d37324cf-da6e-38b7-88a7-2a9af2acd8c2 | -3.0928 | -54.18786 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 69f4c185-99fd-33e2-abbb-9071570b193e | -3.09206 | -54.19273 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ba502dec-9f5a-3e38-b8a8-3236f931c5a9 | -3.0919 | -54.16231 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 3d5863e6-ae70-394f-b706-95fa7a09c898 | -3.08962 | -54.17736 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| c997a849-715e-3cfe-9761-16bfe9ba4241 | -3.08888 | -54.18228 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| a9ce015f-5b93-34e3-a74c-8e391ab3b486 | -3.08778 | -54.43721 | 2024-10-21 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ee11478-6474-30a3-a784-6bef8b5999e4 | -3.00188 | -54.90376 | 2024-10-21 05:29:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf2512a6-3e7b-3526-9e2f-23619b84d688 | -3.10978 | -54.17035 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| f32cc056-1a66-3b16-b473-368965130e8c | -3.10904 | -54.17522 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| c9af603b-767f-38a9-bc3c-617b306dd6de | -3.10482 | -54.19058 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3aa28e44-3e85-3974-a2e3-dc01be72a895 | -3.10362 | -54.17947 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| a217b6eb-f8e9-372d-9821-39c15ae1aab6 | -3.10289 | -54.18424 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 3f14f082-ab1c-32af-bba1-e0497c9a9a3e | -3.10216 | -54.18903 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 876d22c3-fef3-3169-83d5-df31a02dff6f | -3.102 | -54.15871 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 50098956-e2d9-3af9-8e0e-41b26ab5fffe | -3.0997 | -54.17388 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 6e607356-2a58-3bbd-a342-4bb20580ade3 | -3.09894 | -54.17881 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 66a78819-4e94-3633-9745-eeebb2189be8 | -3.09811 | -54.15288 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a46e1dc4-43aa-34c6-bf82-a27d01c6dc16 | -3.09673 | -54.19337 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 75b85de3-8d4d-3060-83fa-e179075f5451 | -3.09579 | -54.16816 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| d2026393-1eaf-316c-9cb8-34be012e31a7 | -3.09428 | -54.17812 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 15fe6411-11a2-3ab2-a7f4-6bd17c2b7e32 | -3.09354 | -54.183 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 81356a6b-6310-355a-b936-ba53ffbf9e2f | -3.09267 | -54.15724 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 1ab02ed1-0c0b-3265-bc08-f2eda1ee769e | -3.09114 | -54.16737 | 2024-10-21 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |


[Clique aqui para ver as próximas entradas](README55.md)
