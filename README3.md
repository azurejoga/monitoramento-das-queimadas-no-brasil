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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa28b18c-57c8-383f-9638-378b71c3c63e | 2.6905 | -60.2591 | 2026-02-21 02:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 33.4 |
| b79cd983-d9c0-3393-b590-f8d87768c114 | 2.6905 | -60.2401 | 2026-02-21 02:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 40c8425c-f766-3ff8-ad98-1cafe6709741 | 2.5617 | -60.7354 | 2026-02-21 02:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 67dd5938-299c-3103-b87e-e35d0307ecb8 | 2.6905 | -60.2401 | 2026-02-21 02:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 3edb783c-eeef-3842-b4d4-60a077f50678 | 2.5434 | -60.7357 | 2026-02-21 02:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 106.7 |
| bde519cc-6876-3f88-af63-1ab6a5d50d41 | 2.5617 | -60.7354 | 2026-02-21 02:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 75.6 |
| b8cdd4e6-4381-3a3d-ac8e-5f641c71447f | 2.6905 | -60.2211 | 2026-02-21 02:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 2cc12804-78f2-322b-af5f-f0a122d67308 | 2.7088 | -60.2208 | 2026-02-21 02:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 9dd998ee-5945-3b26-a0eb-cd1580f5357c | 2.7088 | -60.2398 | 2026-02-21 02:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 8a6750de-6d08-334d-9e44-deba3390e9c7 | 2.6905 | -60.2401 | 2026-02-21 02:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 52.2 |
| dcedefd8-a776-3c6e-91b7-f85aaa371c83 | 2.5617 | -60.7354 | 2026-02-21 02:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 97.1 |
| eca77d6b-ddef-3aed-b9f6-0a3354f0f732 | 2.7088 | -60.2398 | 2026-02-21 02:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 52.9 |
| fb73f5c0-7abf-38a9-9bee-2b18a7cd268c | 2.5434 | -60.7357 | 2026-02-21 02:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 3969344e-7c06-3149-a17a-99d354b8ee62 | 2.6905 | -60.2211 | 2026-02-21 03:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 97dc2c4b-99fe-315a-99fb-f809e22988e0 | 2.8906 | -60.5789 | 2026-02-21 03:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 6403a85c-6b16-3dcc-bf5c-11166c326b3e | 2.7088 | -60.2208 | 2026-02-21 03:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 62969211-1125-32d7-80ff-3bfd84511b41 | 2.5617 | -60.7354 | 2026-02-21 03:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 164215cf-3cbc-3e40-b671-ecfee9f08baa | 2.6905 | -60.2401 | 2026-02-21 03:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 13a8c5ab-9546-37e2-b8e1-6b3a36755196 | 2.7088 | -60.2398 | 2026-02-21 03:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 53e55bc6-eb03-3a35-9216-dab69f278f2e | 2.8906 | -60.5979 | 2026-02-21 03:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 51.5 |
| c2d5c0b7-a100-3df8-aad0-8e4eee22220d | 2.5434 | -60.7357 | 2026-02-21 03:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 42356257-6d2a-39f8-a4f4-cf1d7056cdca | -16.49526 | -39.86559 | 2026-02-21 03:02:00 | NOAA-21 | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 0f3d51a3-14f0-30f8-8df9-2f6e746ed7be | -16.49331 | -39.8607 | 2026-02-21 03:02:00 | NOAA-21 | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 453d895f-2056-37e5-ba22-4f2903a1159e | -16.49645 | -39.86023 | 2026-02-21 03:02:00 | NOAA-21 | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 7e159835-91ac-34b2-a1e2-ac836cd105e4 | -16.49209 | -39.86605 | 2026-02-21 03:02:00 | NOAA-21 | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| ce4661cb-c9a9-3c49-91b9-aed4e397cd2f | 2.5434 | -60.7357 | 2026-02-21 03:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 8f672f47-c751-3d41-90a0-febb6ff3394b | 2.562 | -60.5648 | 2026-02-21 03:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 9ee9b3ed-ba22-3164-ac89-6087aa86a3f9 | 2.6905 | -60.2401 | 2026-02-21 03:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 31bb9674-e45c-3cd7-bb2c-f7d43d447a5c | 2.7088 | -60.2208 | 2026-02-21 03:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 43.6 |
| b3db99d7-6987-3f13-bed5-53285d866841 | 2.7088 | -60.2398 | 2026-02-21 03:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 22323922-5033-33fb-a476-36238dd30d5a | 2.5617 | -60.7354 | 2026-02-21 03:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 18ca1b88-9748-3c5a-b837-da474bb5f4ef | 2.6905 | -60.2211 | 2026-02-21 03:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 46.6 |
| e0197b79-9284-37e6-82ef-00bbaed8af4a | 2.5617 | -60.7354 | 2026-02-21 03:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 58.4 |
| b8938fdf-081b-3c47-8b23-283afbeced56 | 2.562 | -60.5648 | 2026-02-21 03:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 94096907-0189-35e1-8d50-24a038195d12 | 2.5434 | -60.7357 | 2026-02-21 03:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 4fce56d5-3b1f-3b3f-9155-dbb7d908b1db | 2.6905 | -60.2401 | 2026-02-21 03:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 40.1 |
| de49870c-d8ef-3fdb-b6a9-722e95d51c6d | 2.7088 | -60.2398 | 2026-02-21 03:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 2fc6c745-010e-3c24-9160-05bdeaba2151 | 2.6905 | -60.2211 | 2026-02-21 03:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 1314fd50-759e-32a8-a85c-0300ecb1607a | 2.5438 | -60.5651 | 2026-02-21 03:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 58543819-7138-36f2-8a3c-18736e1c8f43 | -4.57722 | -37.98351 | 2026-02-21 03:27:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c8475110-2172-3812-bb20-b9297bdde8ac | -4.58214 | -37.98436 | 2026-02-21 03:27:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a31a2402-14e9-3b67-9ae7-72fe2b1e0306 | -9.34325 | -36.81818 | 2026-02-21 03:29:00 | NPP-375D | MINADOR DO NEGRÃO | ALAGOAS | Brasil | 2705309 | 27 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0c574ba2-36b1-3aa7-8bb3-d382027d665f | -6.23408 | -35.64008 | 2026-02-21 03:29:00 | NPP-375D | SERRINHA | RIO GRANDE DO NORTE | Brasil | 2413508 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9cb356eb-4a59-31cf-828a-f261444cd6eb | -9.34257 | -36.82209 | 2026-02-21 03:29:00 | NPP-375D | MINADOR DO NEGRÃO | ALAGOAS | Brasil | 2705309 | 27 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1c6f5e89-2240-3238-ab98-f5d08c1b1e68 | -6.23493 | -35.64062 | 2026-02-21 03:29:00 | NPP-375D | SERRINHA | RIO GRANDE DO NORTE | Brasil | 2413508 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a8fcc139-84a1-3dfe-8deb-b5a05f06cc5a | 2.6905 | -60.2401 | 2026-02-21 03:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 89d56246-0e08-3375-b9fd-e384df26991c | 2.5434 | -60.7357 | 2026-02-21 03:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 25fb0500-1782-3de1-bb57-004e07f8e818 | 2.562 | -60.5648 | 2026-02-21 03:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 26de4ffb-4bd6-3f9f-aa97-f5b565fd06b6 | 2.6905 | -60.2211 | 2026-02-21 03:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 034079c1-d5f6-374b-a720-005f2bc65c27 | 2.7088 | -60.2208 | 2026-02-21 03:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 2a5685ff-29c8-3dd1-9b61-6574973670f0 | 2.5617 | -60.7354 | 2026-02-21 03:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 53.3 |
| c4b4a83e-ff9a-36c5-98ec-36dc208ab3dc | 2.5438 | -60.5651 | 2026-02-21 03:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 63.1 |
| eedba275-0947-34ab-bd58-edcb9ff2347e | 2.7088 | -60.2398 | 2026-02-21 03:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 50.5 |
| ec08afd1-6190-3973-9f5a-6e2a919052af | -16.49762 | -39.86393 | 2026-02-21 03:32:00 | NPP-375D | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 30783c6d-9379-30c1-8898-d30486037b5e | -16.49312 | -39.86286 | 2026-02-21 03:32:00 | NPP-375D | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 373d479e-e20d-396b-baee-791f8c07d9c6 | -16.35071 | -40.65023 | 2026-02-21 03:32:00 | NPP-375D | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 13495296-6f6d-3de2-9592-63ccee0b2fd8 | -17.23587 | -39.23425 | 2026-02-21 03:32:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ef831ed0-a7bf-3464-b704-72e6f20693ec | -21.69328 | -41.98713 | 2026-02-21 03:34:00 | NPP-375D | ITAOCARA | RIO DE JANEIRO | Brasil | 3302106 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8543546b-b03e-390c-afb5-c0151782d65c | 2.5434 | -60.7357 | 2026-02-21 03:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 49.8 |
| b3a9496d-0fd1-343b-8a0b-336517f0b578 | 2.7088 | -60.2398 | 2026-02-21 03:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 966c63fe-a3a8-320d-9853-d3e156cd9be1 | 2.562 | -60.5648 | 2026-02-21 03:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 889f55a0-cb1b-3f64-a905-f7cec095ca7c | 2.5617 | -60.7354 | 2026-02-21 03:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 8e089010-666e-390e-8022-3d4467ae4f67 | 2.6905 | -60.2401 | 2026-02-21 03:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 37.8 |
| ce48fe1e-2be1-3414-85a8-1369c95546a6 | -4.58108 | -37.98326 | 2026-02-21 03:49:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 94de5446-6856-35ee-a31a-516b0c56562a | -6.23231 | -35.64011 | 2026-02-21 03:49:00 | NOAA-20 | SERRINHA | RIO GRANDE DO NORTE | Brasil | 2413508 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5b3962ea-60ad-3913-b8f3-c8484f5aba89 | -4.57771 | -37.98272 | 2026-02-21 03:49:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cb6bb218-87ba-31f7-85c8-5c974efbe7f6 | -6.23566 | -35.64063 | 2026-02-21 03:49:00 | NOAA-20 | SERRINHA | RIO GRANDE DO NORTE | Brasil | 2413508 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8dfe2440-34cf-3854-bb15-fdf0ad2cdfc7 | -6.23621 | -35.63708 | 2026-02-21 03:49:00 | NOAA-20 | SERRINHA | RIO GRANDE DO NORTE | Brasil | 2413508 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| afc2eb51-1e49-3d47-8438-af641a8db985 | 2.562 | -60.5648 | 2026-02-21 03:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 53.8 |
| a7312eaf-78b6-3a5f-a227-1e7e4c9446d0 | 2.7088 | -60.2398 | 2026-02-21 03:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 41.2 |
| cc0152bc-087b-3a0c-be44-8dc8eb991399 | 2.5617 | -60.7354 | 2026-02-21 03:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 257769bb-5000-3d6b-94cc-f49e69bf5aab | -17.23683 | -39.23048 | 2026-02-21 03:51:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5135e5dc-bd66-3d64-9414-02639d627e6d | -15.27429 | -39.41526 | 2026-02-21 03:51:00 | NOAA-20 | ARATACA | BAHIA | Brasil | 2902252 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 69b956e8-113e-36f1-a8b9-d214e58b4d68 | -17.24563 | -39.23938 | 2026-02-21 03:51:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 10140221-2e59-383b-b970-92c155ee36a9 | -16.49373 | -39.86599 | 2026-02-21 03:51:00 | NOAA-20 | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 09be3e76-c74f-3949-9e7a-48a9d0245e52 | -16.49431 | -39.8624 | 2026-02-21 03:51:00 | NOAA-20 | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| f08242af-300b-39d0-84f2-05989038a898 | -16.34954 | -40.64917 | 2026-02-21 03:51:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 686cc440-6003-3729-a783-06000538294e | -16.34618 | -40.64861 | 2026-02-21 03:51:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| de5ccd2d-0e94-395b-8aab-1968014d5ac0 | -17.23627 | -39.23409 | 2026-02-21 03:51:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 50b26002-3239-3e1d-ac65-0c8347e8ccd0 | -20.2232 | -50.66386 | 2026-02-21 03:53:00 | NOAA-20 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5b080519-ccc1-3011-ad7c-398544fb884b | -21.69354 | -41.98792 | 2026-02-21 03:53:00 | NOAA-20 | ITAOCARA | RIO DE JANEIRO | Brasil | 3302106 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 82e559be-9a31-38a1-9418-40bffdc86d5a | -20.22955 | -50.66137 | 2026-02-21 03:53:00 | NOAA-20 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a8060ace-3002-3b30-b019-2865850cfb59 | -20.69059 | -40.52283 | 2026-02-21 03:53:00 | NOAA-20 | GUARAPARI | ESPÍRITO SANTO | Brasil | 3202405 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b12acf8d-0cc6-33aa-90b6-e6255d8e054c | -20.2275 | -50.66499 | 2026-02-21 03:53:00 | NOAA-20 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b9973482-c2be-328a-ad95-1b4712f94398 | -19.18621 | -40.30417 | 2026-02-21 03:53:00 | NOAA-20 | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ddee1469-cf04-3696-9aab-8aa11a99080c | -20.22837 | -50.6611 | 2026-02-21 03:53:00 | NOAA-20 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 23172eb0-ed0b-3d81-b57a-9ef0f24fd5da | -20.22405 | -50.65998 | 2026-02-21 03:53:00 | NOAA-20 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 42c54d96-39e3-3f35-83c6-f34e05487bf1 | -20.2287 | -50.66526 | 2026-02-21 03:53:00 | NOAA-20 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 40423354-f70e-3c04-8f6e-60a6d51d8d1a | 2.5434 | -60.7357 | 2026-02-21 04:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 1eadbd7d-a896-3a39-839b-1b2b4666dce1 | 2.562 | -60.5648 | 2026-02-21 04:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 2eb77fe5-be0d-3e79-b95e-07c832d02759 | 2.5617 | -60.7354 | 2026-02-21 04:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 4b9a7eba-99ad-3c45-9a10-f728e7772ad4 | 2.6905 | -60.2401 | 2026-02-21 04:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 46.3 |
| ebb127b0-6ddb-32cf-9424-bec67d1daf9b | 2.7088 | -60.2398 | 2026-02-21 04:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 830ad9ee-ab50-369d-b1a4-92dd127e53ba | 2.5617 | -60.7354 | 2026-02-21 04:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 12a3dcd3-11f6-31ea-859d-634a7828a781 | 2.7088 | -60.2398 | 2026-02-21 04:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 47.7 |
| b0c7dc8b-4ac4-3172-8c38-c832306b144a | 2.5617 | -60.7354 | 2026-02-21 04:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 50.8 |
| cf981d8f-6d27-3af0-bcab-6ec9ae512490 | 2.54796 | -60.56699 | 2026-02-21 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 071ddbb6-8b21-39ef-8336-e2a0413bcc4a | 2.55042 | -60.72878 | 2026-02-21 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 12.4 |
| e924b532-e054-3943-b234-019499feca7b | 1.05373 | -59.49573 | 2026-02-21 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a576dfde-f537-3bb0-896b-d2eeb52f5df0 | 2.70435 | -60.23549 | 2026-02-21 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 13.3 |


[Clique aqui para ver as próximas entradas](README4.md)
