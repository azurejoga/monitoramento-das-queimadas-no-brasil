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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 86f25f1c-6824-350b-b8d8-6dea94c715ee | -6.56927 | -58.98161 | 2026-09-12 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5eba7229-4f30-38da-98bd-74b48ba7121a | -6.28314 | -56.02202 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5c1e3c13-d7b5-3f8d-8e9f-4a571edce157 | -6.07035 | -53.4971 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cb243264-9ee1-3e1c-8d98-e50102a45d5c | -6.1998 | -55.27161 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46c35a15-844a-35ab-a49c-5d40d6b6a06b | -6.20035 | -55.2678 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 889303ab-5490-38b9-9e23-072ca90753f1 | -14.58445 | -48.83891 | 2026-09-12 05:31:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 76bfd356-2a97-3757-a529-1f859cbb4a18 | -12.15827 | -64.13519 | 2026-09-12 05:31:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c56a0790-c0cf-35bf-9112-2901840b69a8 | -13.32946 | -51.65968 | 2026-09-12 05:31:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85508659-90b8-3dbe-9945-7bd7baea0b9f | -12.64323 | -51.42751 | 2026-09-12 05:31:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c4a8bcf4-1dda-30e2-99fe-3144e1242b15 | -15.04257 | -48.52309 | 2026-09-12 05:31:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f820de9a-c452-3dc0-9c0a-597aa8fa5533 | -16.6323 | -52.82593 | 2026-09-12 05:31:00 | NOAA-20 | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d528463-7433-39da-85c0-532338ea99c0 | -16.04316 | -52.65842 | 2026-09-12 05:31:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ff8a4dc8-f325-3c7b-ae0e-7024712fd1b0 | -15.05865 | -48.53214 | 2026-09-12 05:31:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8988535b-f7fb-30e5-ad89-eba529522e03 | -12.64375 | -51.42315 | 2026-09-12 05:31:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cdf2b7f9-b823-35f0-88e0-315d231e26e1 | -14.58773 | -52.66913 | 2026-09-12 05:31:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0fbe2d32-c991-306a-ab39-4a5990962ea7 | -12.15764 | -64.13902 | 2026-09-12 05:31:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6903d10f-2903-31c9-9b9e-257a16996d51 | -13.45786 | -48.50756 | 2026-09-12 05:31:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62c43771-f79c-36fc-a094-70d53442fe53 | -15.0177 | -48.50385 | 2026-09-12 05:31:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27e00879-514a-3250-a2b0-dd7a1eb865f1 | -10.27047 | -68.27662 | 2026-09-12 05:31:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9147c1a-6474-3474-9055-3ef2e61ee1ff | -14.58935 | -52.66626 | 2026-09-12 05:31:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3924c74b-b85b-3ce5-9eb6-4a4c9e8bf4f0 | -12.59452 | -53.9865 | 2026-09-12 05:31:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f175efcb-89dc-3bbf-b04a-ae39d5330d7d | -13.32996 | -51.65556 | 2026-09-12 05:31:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 033849fe-4e8c-3624-9467-922a5834be0f | -10.28093 | -68.74939 | 2026-09-12 05:31:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1f6408d-b847-3f94-a677-e2aa53771795 | -12.15294 | -64.14607 | 2026-09-12 05:31:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 2dd8e800-70b0-32cf-8a3f-cf22ce71a63f | -14.58261 | -48.83442 | 2026-09-12 05:31:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 01e0c02d-57df-3641-ae5a-99b459ca0fc5 | -15.04316 | -48.51725 | 2026-09-12 05:31:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6a8c29d2-bfb4-36bb-a1a6-e1fb586381a4 | -14.5896 | -48.83568 | 2026-09-12 05:31:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cf7f479d-5d88-3b54-823f-f0a8b8e7e7e2 | -14.58191 | -48.84147 | 2026-09-12 05:31:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d1a35ea0-e8fd-34fa-a63b-f9c260f47a25 | -16.03179 | -52.65723 | 2026-09-12 05:31:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 417dbb94-6671-34b8-809f-538b04a0af1b | -10.28008 | -68.75414 | 2026-09-12 05:31:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 628fef12-7123-3fb4-a16b-5ed1e0923307 | -10.27872 | -68.86891 | 2026-09-12 05:31:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ae1a79ce-8c34-3b07-8a3a-3d96fc12c0f8 | -10.28553 | -68.75022 | 2026-09-12 05:31:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd9e37bb-b585-3889-9937-1c3604e6313d | -14.58422 | -52.66185 | 2026-09-12 05:31:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f219c135-16a2-3fb0-8812-f68fe39b5619 | -12.15483 | -64.13461 | 2026-09-12 05:31:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6428ad63-8469-3466-8ed3-20c0ff9126f1 | -16.03748 | -52.65779 | 2026-09-12 05:31:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 30e60013-516b-3f61-abdb-0284c7db1343 | -12.63785 | -51.42244 | 2026-09-12 05:31:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 782c39bf-9888-39ef-a247-89ddac73c314 | -12.1542 | -64.13841 | 2026-09-12 05:31:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1980e3fe-4cc8-3a46-a338-fb3fc85e0168 | -17.16924 | -55.93015 | 2026-09-12 05:31:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 387739c9-e9df-395e-a156-bd1b09670a85 | -15.01709 | -48.51028 | 2026-09-12 05:31:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2760bad0-9512-31ec-b42a-27d8abf480da | -14.58816 | -52.66529 | 2026-09-12 05:31:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c1517d3-7fd6-33c7-a06a-7ca714e0d308 | -12.15357 | -64.14224 | 2026-09-12 05:31:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 82f69495-cc37-3762-b6ee-543bbd1edc57 | -12.64964 | -51.42386 | 2026-09-12 05:31:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2e90b1d-6828-3763-88aa-50c23a959397 | -15.05924 | -48.52597 | 2026-09-12 05:31:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6380b31c-16ce-332e-8c0a-c7d48a7e3cd1 | -14.5914 | -48.84047 | 2026-09-12 05:31:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d45bbe65-c1cd-3821-beb3-15b41a49d758 | -10.27667 | -68.87128 | 2026-09-12 05:31:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e0f46391-49aa-39ce-ba03-ca95e46c75b9 | -12.15701 | -64.14284 | 2026-09-12 05:31:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9006a12-94bd-3017-820b-80b56316e740 | -14.58301 | -52.66084 | 2026-09-12 05:31:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a19ba37-9693-3ffb-90f7-01b54885633d | -15.01471 | -48.51086 | 2026-09-12 05:31:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c122559d-d9ee-36e8-851a-fa99be3a628a | -13.45847 | -48.50159 | 2026-09-12 05:31:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 993d3a99-a79f-37ee-94cb-c01155898380 | -15.01534 | -48.50459 | 2026-09-12 05:31:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b600d88-13f5-3448-9fa0-1bc47f90ff2b | -13.45995 | -48.51311 | 2026-09-12 05:31:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0c8f8735-2969-3c16-a50b-9e3c5904886c | -17.17388 | -55.93075 | 2026-09-12 05:31:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 4048327b-7cde-3ad2-b7e0-c40dca1dd93f | -12.15013 | -64.14165 | 2026-09-12 05:31:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 06657890-194f-327b-8d8d-d07d690346fa | -15.045 | -48.52276 | 2026-09-12 05:31:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3a429b60-8f02-33a7-9109-09d79c6c9cbb | -13.32939 | -51.65472 | 2026-09-12 05:31:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d4b4718-570c-3afe-84cf-19eedd41142c | -12.15076 | -64.13783 | 2026-09-12 05:31:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 9e619627-7c7e-3229-8b15-248cc365e00d | -13.32892 | -51.65885 | 2026-09-12 05:31:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d5d73ba-ddb5-3d10-bc56-b56f33cd9875 | -10.26968 | -68.28109 | 2026-09-12 05:31:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb694877-7bb6-392f-b65f-e9edfd97fa0c | -10.28469 | -68.75498 | 2026-09-12 05:31:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ce00b55-40d1-3ff2-9688-9cd3ea027875 | -13.30686 | -51.64397 | 2026-09-12 05:31:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 095a443d-52f2-3f95-8480-f23c66317d1b | -16.62426 | -56.97141 | 2026-09-12 05:31:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 2bb101bc-956a-352e-a46c-7a2b82d6a804 | -13.46059 | -48.50726 | 2026-09-12 05:31:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4605d2e8-18e9-3eca-8d63-1b9530613bdb | -15.04556 | -48.517 | 2026-09-12 05:31:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9d93233b-c307-3c74-8a35-94c9ef03f8eb | -3.7462 | -61.7552 | 2026-09-12 06:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 5e811b0d-8813-33a3-b651-25fea7f9bb0e | -5.77085 | -45.10575 | 2026-09-12 06:14:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 66cc08b3-35e4-387c-b523-cfda8b88ba1e | -7.18081 | -45.89093 | 2026-09-12 06:14:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 415923bc-f432-3a21-9208-0e4dcff55f02 | -5.61102 | -44.83793 | 2026-09-12 06:14:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 2f0c13c1-0ead-3272-888b-a0c139b1e927 | -6.32333 | -43.36214 | 2026-09-12 06:14:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6617c6bc-075a-3c11-85c4-7a6ca1481711 | -5.76176 | -45.08674 | 2026-09-12 06:14:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 750e7f25-5493-3b73-b0d3-2f8ec35cdbb8 | -6.11106 | -38.09947 | 2026-09-12 06:14:00 | AQUA_M-M | FRANCISCO DANTAS | RIO GRANDE DO NORTE | Brasil | 2403905 | 24 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 7d237426-7549-384f-9259-b3d51dbfe809 | -5.75453 | -45.09642 | 2026-09-12 06:14:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 70bd07fe-e920-3c96-b863-cfe788316e74 | -5.77372 | -45.08839 | 2026-09-12 06:14:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 108.2 |
| a9efa194-0499-3424-ba97-2f35dde00532 | -6.32595 | -43.35695 | 2026-09-12 06:14:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 038303b6-a04a-38ae-919d-3095c24db5ab | -5.75888 | -45.10407 | 2026-09-12 06:14:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 73e7341f-4c12-392b-81d4-ea65df8fa760 | -3.22427 | -46.95114 | 2026-09-12 06:14:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 25d4a283-e77d-3943-b7d9-eb32c0033717 | -5.60845 | -44.85416 | 2026-09-12 06:14:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 29.3 |
| d426d5b8-ea1c-301e-b788-e7761c12f596 | -6.96123 | -44.54211 | 2026-09-12 06:14:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 8c5b6043-1bd8-30d8-93e4-6422a78780c0 | -6.96232 | -44.53555 | 2026-09-12 06:14:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 20a86ef5-cabe-3473-b307-ff342fe61932 | -5.76651 | -45.09809 | 2026-09-12 06:14:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 178.5 |
| 0b6b0a63-e99e-3899-941a-67e8eb981e52 | -10.17912 | -36.42135 | 2026-09-12 06:14:00 | AQUA_M-M | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| bfcd867b-a31d-34cc-a256-002fef305220 | -3.32886 | -42.2908 | 2026-09-12 06:14:00 | AQUA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| beb17115-cd73-34a3-b935-592ee3b97d26 | -5.75727 | -45.07918 | 2026-09-12 06:14:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 1a65abdf-12dd-35b5-998e-1160e61a0e2b | -6.96003 | -44.55003 | 2026-09-12 06:14:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| d3d2a403-3011-3ab1-bc3c-2867a37aff1d | -5.76923 | -45.08083 | 2026-09-12 06:14:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 26d23767-2bdc-3afd-872b-b6205780c0af | -7.14154 | -73.11369 | 2026-09-12 06:14:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0d6db5c7-20e7-3b7e-85bb-7e553d7d2acf | -7.36445 | -72.727 | 2026-09-12 06:14:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73c4609c-f795-38c6-a8cd-39269a80b0b1 | -3.74072 | -61.75215 | 2026-09-12 06:14:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 082f64e4-75ab-3144-9cb0-2b2293d94649 | -7.141 | -73.11716 | 2026-09-12 06:14:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52248f32-bf07-3401-af47-8289a9c5b871 | -7.39744 | -72.80038 | 2026-09-12 06:14:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6e536e92-9e74-3fbf-b1ad-e465e6343e27 | -7.36499 | -72.72347 | 2026-09-12 06:14:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b3d6824-709f-310a-9a10-b50c712e224e | -7.42126 | -72.80048 | 2026-09-12 06:14:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f46933a4-3050-318f-97a1-3d3726b6710a | -3.73468 | -61.75124 | 2026-09-12 06:14:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bdc0b52f-5fa2-3af1-91b7-a713bcfad969 | -7.36112 | -72.72648 | 2026-09-12 06:14:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05e9fe42-8345-3013-9619-c44d4a7bb091 | -3.74139 | -61.74757 | 2026-09-12 06:14:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1bf22c32-8589-34d1-bd2f-0265165196cf | -2.97 | -50.4 | 2026-09-12 06:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6f1dc01-c112-3ebb-8dba-9160c0de6559 | -11.79481 | -46.39253 | 2026-09-12 06:16:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| bdb4cbc6-59f7-3356-b75f-f86a6c8ae9a3 | -15.05096 | -48.52152 | 2026-09-12 06:16:00 | AQUA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 27.4 |
| c02ad4d1-1b3b-313a-9cdc-0dff0fd46c41 | -15.05295 | -48.5164 | 2026-09-12 06:16:00 | AQUA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 21.6 |
| b6070483-d2be-3864-99ee-a97811369866 | -11.18309 | -42.79297 | 2026-09-12 06:16:00 | AQUA_M-M | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| ec8720fd-b90e-3189-b64e-e8bb9bf95fb2 | -12.12906 | -48.94991 | 2026-09-12 06:16:00 | AQUA_M-M | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 31.2 |


[Clique aqui para ver as próximas entradas](README54.md)
