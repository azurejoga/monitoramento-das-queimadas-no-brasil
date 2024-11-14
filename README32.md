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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 439ca95a-3c60-3d11-8b77-c97fbaf842e1 | -4.15426 | -46.25202 | 2024-11-14 04:40:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9d4dbb3-c028-3e6f-b552-297f57f62e58 | -2.87377 | -51.79623 | 2024-11-14 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 002ce6b5-c21b-31a4-92ff-bde3c1058fb7 | -1.80159 | -52.17541 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e6e9f33b-198d-3402-a807-b614a9729eb8 | -2.89202 | -46.86968 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 46f6e73f-e36e-33f0-bb58-98c672c23132 | -3.77601 | -41.60185 | 2024-11-14 04:40:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 198e1748-4b77-3b30-9956-1fdcd393a417 | -2.17517 | -48.43973 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2586e37a-77ad-3330-ac94-9fae75db9010 | -3.49554 | -50.83643 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 23c33c65-0274-3cf0-b446-646d94cc029f | -3.74002 | -50.44027 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2d434cdb-80fc-38b3-b4a5-dfd5d5b1c8d9 | -3.11005 | -45.87948 | 2024-11-14 04:40:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cbb39239-3ad5-3a1f-a1e2-d0811ec2a7b4 | -3.97353 | -46.70096 | 2024-11-14 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82e27ccf-cebb-3ad5-832f-b6b3d06d4000 | -4.94256 | -44.96076 | 2024-11-14 04:40:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| df09e51f-148f-39a8-bd00-5ac7b17532a7 | -4.21007 | -50.49586 | 2024-11-14 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c230e24-3bc2-31ff-81a6-54b74c5846ff | -4.25557 | -48.53462 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc22b3ea-df5f-3956-9af6-bc42e0e0fc1e | -5.19324 | -44.35738 | 2024-11-14 04:40:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1971debf-dc18-3020-a876-eca1c6b52996 | -2.90483 | -48.29614 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4e967c05-9f40-3edc-aa13-6e7307fadeca | -4.09414 | -49.15881 | 2024-11-14 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbc80042-ec20-3324-a0b0-1799d6c75d61 | -3.40277 | -50.31101 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8e354997-e5fb-366e-8ec8-ad3621492079 | -2.15213 | -48.95599 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3581f0fd-0fab-3355-b014-c267cf437a35 | -4.21954 | -46.81581 | 2024-11-14 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f65ee3c4-b937-316e-b85c-d6f3c7aa378a | -2.21274 | -48.22015 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7570235b-d871-3455-83db-82f70047024f | -2.21837 | -48.37956 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 91b8e3c1-eb86-35d1-9778-26ebe802dd78 | -2.65889 | -46.78898 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4e08767-22ea-3d9a-b956-e844c7e7c321 | -2.1751 | -48.54865 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3661bc43-ae06-37d0-8d21-7702e9486806 | -2.19087 | -48.38236 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab53bbcc-89e6-3951-95aa-122f80173dfe | -2.88326 | -48.28221 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cec9e2db-b108-39ed-bfff-9f095ecb8bca | -2.37019 | -46.49999 | 2024-11-14 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7a8b682-4346-380d-b69e-b20307b93616 | -2.65887 | -46.8346 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e8cc1af-b26d-3fb8-ae58-57baa12f4467 | -3.57055 | -50.33017 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7798da0f-6e74-3c7d-9ea9-74e727bcd271 | -1.33605 | -51.40861 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 612071ae-0289-36b3-b25e-f418d5254b17 | -4.58504 | -47.05953 | 2024-11-14 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce670134-5aae-3cec-9f75-9b82f4cc4087 | -2.37195 | -48.50889 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 462838c5-eb5c-3c83-9aec-eea2054ecbfc | -4.59545 | -47.0377 | 2024-11-14 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e410fa6a-4083-3cae-abe9-de186e514ee5 | -1.13557 | -53.6592 | 2024-11-14 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e891d193-fdac-38a9-82f9-c1e6d24fad2f | -4.74574 | -48.81627 | 2024-11-14 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5306a49-e747-3f2b-b89d-b3f9cc744a23 | -1.80895 | -52.17657 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40f09f31-6806-33cd-94d6-18476759db9f | -3.86852 | -43.9401 | 2024-11-14 04:40:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef2a6231-53df-3f56-816b-6a2b639d3234 | -4.55386 | -48.01415 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 46264430-81a5-3592-8955-6f395eb9051a | -5.193 | -44.79258 | 2024-11-14 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2fd96ef0-123b-35c7-8570-6e701f618c06 | -2.56171 | -47.44012 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6104255b-6099-3d9b-8d6d-073baa5671ca | -3.63373 | -48.92443 | 2024-11-14 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2771adb6-ca11-37ec-8db7-f1fdbbba0d60 | -2.66971 | -46.83248 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ef36ef7-2c51-3b3d-92d2-1c7d5c5fd279 | -2.34715 | -53.75525 | 2024-11-14 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 761b153d-1133-30ea-8106-8e936c386159 | -4.14386 | -43.85049 | 2024-11-14 04:40:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 12723d9c-0c0b-315d-a01b-2d396aca5ac0 | -2.35713 | -48.51715 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc67c58c-5607-3d4b-a36f-fb361a98b57d | -1.22054 | -51.74821 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60f24502-efce-3a36-a8b4-eab13eaadd98 | -4.08523 | -49.14625 | 2024-11-14 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e768989-7890-387e-aea3-6f2ea6e859b0 | -4.5583 | -48.00759 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 14396f1b-d6d4-31b8-b8ff-08a9c85552a6 | -1.47015 | -51.12864 | 2024-11-14 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92960efe-2625-3d02-9cd7-cc5ce0ceea71 | -2.25642 | -48.37838 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| edf0c0d3-9039-3bd4-8243-4d71ded5d95e | -1.68781 | -48.46495 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| df4ae3b1-e798-3a84-889d-1e67d9791efa | -3.48698 | -50.84283 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbf1d3ac-1bf2-38c6-9589-297fe997077a | -3.47156 | -50.30393 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1d2cd25c-d960-33d7-973c-c2d130b60688 | -4.11274 | -48.49081 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35947775-f465-39a4-a1d8-13ffe2e87d39 | -4.29931 | -48.09836 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8bc1021b-77fe-3801-a364-aeb7f79a98fc | -2.31599 | -49.19275 | 2024-11-14 04:40:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 591917cb-75e9-36d2-8a06-e61c9e964ae1 | -2.64202 | -46.16945 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2fbe4df-220a-3f03-bc7c-7a1a2021da76 | -1.39462 | -51.12903 | 2024-11-14 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 45b514c5-d31d-3672-b661-e95546a037d0 | -3.30011 | -43.513 | 2024-11-14 04:40:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e2684ea2-da19-3b06-a976-bec63c2f6432 | -4.29756 | -46.87734 | 2024-11-14 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ccf03cf-1910-3321-87f6-40dc8986a2c7 | -3.0199 | -47.97255 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e149bd8f-63da-3826-a5c6-c2af2c066482 | -1.35856 | -52.34806 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f6a66a1-403e-32b4-8245-5e1fc1577509 | -2.05629 | -51.16449 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd8e3921-89be-3315-8277-c861bdb6ade4 | -1.21458 | -51.78597 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 884890f8-9fb1-3a75-b68b-5e9f6d1b6930 | -2.29752 | -49.11589 | 2024-11-14 04:40:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01298851-8735-35c0-b6a3-680a063bf969 | -2.20686 | -53.74687 | 2024-11-14 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06babf7f-17fe-3f96-a7f9-c58ceef4230a | -2.87734 | -51.79676 | 2024-11-14 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5222dfc1-1d03-38b4-a637-e91af9e059f9 | -2.64974 | -46.82563 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5d6082c-75dd-374f-a144-628b10cb82ec | -1.44906 | -52.24621 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb63526e-ad88-37c5-a9a2-a4c67c9319d2 | -2.15762 | -50.52518 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5509789f-9523-33ee-87e4-acc14a2901f9 | -2.07502 | -46.57214 | 2024-11-14 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e06a6403-83c0-3b97-a357-a9a2d5bbfbb6 | -2.22454 | -48.40513 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bad19948-ae5f-3192-baa6-27ab1a994d78 | -4.16847 | -46.25439 | 2024-11-14 04:40:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1ba69e6-91f5-32c9-8b7f-d1eb0eb503b3 | -2.14927 | -48.80097 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1d14d50-8465-3274-a3a6-fe20f1975498 | -1.37684 | -47.45002 | 2024-11-14 04:40:00 | NOAA-21 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be58dfa7-1d43-33b8-b39b-11cb99c2e6a0 | -2.11245 | -50.69966 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5ee6db8-99a1-3373-9225-ca3959a93c9d | -4.27359 | -48.19868 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e898c4b-d06c-312d-96c8-031f610b8302 | -2.02767 | -46.9427 | 2024-11-14 04:40:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 662e2d63-d07c-3e94-aa05-e42c483b727c | -4.15906 | -45.77465 | 2024-11-14 04:40:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 44940676-0271-3f67-9fe9-6ec2dd3a3062 | -2.64323 | -46.16157 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b705f151-d85c-3b9d-92dd-b0858e79110b | -2.65259 | -46.82985 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d3be4bd-79d6-3c3e-8f1a-9b4a670afe8e | -4.75644 | -46.00777 | 2024-11-14 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 802b915a-af18-3cff-b208-85e3ae87766f | -3.37268 | -46.12777 | 2024-11-14 04:40:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a9147b3-43a7-35f4-9b36-1a980d4ae505 | -4.51809 | -46.47916 | 2024-11-14 04:40:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 86c00aa7-340e-3099-ad5c-c3441bea2b6e | -4.28025 | -48.19971 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 974bf650-92ae-3caf-8e32-463197d3be1d | -3.16315 | -48.36468 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2182a3a0-97f6-3cc6-b40a-8d547d7dd569 | -4.31469 | -46.74258 | 2024-11-14 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d736558-63de-36ec-a78b-1b8d65700add | -3.4134 | -50.30901 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 13b65229-c28d-3500-86ca-8137ccf10e99 | -1.95078 | -52.15783 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae86b5a0-90b3-3dac-9585-34ba3aa48ab4 | -2.37811 | -48.53444 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53dcf8f0-7a38-3270-867f-86986f46870a | -1.6746 | -52.55854 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 00f38960-5555-36a3-b49b-03e3785c9ace | -2.88917 | -46.86543 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c60faba7-b83a-389c-8a44-1d3c5974bd53 | -2.02234 | -46.50253 | 2024-11-14 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 04bef318-8faa-349c-90bc-f395f85e78fb | -3.4106 | -50.30495 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 89b14d9c-efe2-380d-9c2f-62817cc1b867 | -2.36651 | -48.52211 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99dc41ec-a2d4-3379-b27a-044c12bb1c00 | -1.87922 | -52.44354 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17da33ef-2f31-3c28-bd98-e107af2320a4 | -2.59469 | -48.19118 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2200129-53fc-3d64-901e-dae0232e3509 | -5.3544 | -44.36941 | 2024-11-14 04:40:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a74a3b3b-e3fa-3a07-bb4f-9d3773524aad | -3.18859 | -48.66144 | 2024-11-14 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 666d8c31-33c4-3371-bffe-838e222df6e0 | -3.49613 | -50.83274 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ab628819-957c-3094-9927-ab68782cd53b | -3.99363 | -48.33749 | 2024-11-14 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README33.md)
