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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77b0d28b-2bdb-3f14-b54a-a694d2434a4f | 2.01037 | -61.09152 | 2026-10-06 05:23:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| be86ca1d-a7f8-31b8-8db6-b8f6d271b550 | -3.55158 | -59.4916 | 2026-10-06 05:23:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0d3ef548-a253-3b11-a567-1768077847a5 | 2.26773 | -50.82206 | 2026-10-06 05:23:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 283aec80-e3f2-34f8-8e67-9b4c83d468f9 | -2.95412 | -54.14064 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c50d531c-b0ab-338a-a8cb-2546dc48fc84 | -3.13275 | -53.71477 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f253fb6-0523-3c8d-89ff-36d5bf910841 | -3.12605 | -53.76368 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b882f148-d15b-34e4-a9ca-9603dfab451f | 1.71644 | -55.64651 | 2026-10-06 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b24b9ee1-5f1f-3a79-8e53-a94efa0c3a4e | -3.0247 | -53.89945 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| b3786872-a090-3f45-b850-e027520d52da | -4.28618 | -50.26945 | 2026-10-06 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88133b28-2a73-3f78-b869-bbe1754d5946 | -8.97361 | -65.44113 | 2026-10-06 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7281feb6-4257-39a0-9341-09026a607118 | -3.96994 | -56.12558 | 2026-10-06 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 17d6f2cf-1949-322b-8304-f7f405d32110 | -2.1548 | -60.00064 | 2026-10-06 05:23:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e43fb301-a75f-331d-9ad5-515c01887c82 | -3.10079 | -53.71855 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8d61d7e8-f4e5-3851-931e-cd4e901f831f | -2.93649 | -54.11562 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9dca62a5-9e09-3e15-837f-d52656d7c630 | -3.67039 | -54.53665 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53331d4a-a6d7-370b-804d-c8e5c09c69e9 | -2.87423 | -54.1542 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e6a2de72-ae4f-3d47-9e3b-70b528114c19 | -2.92982 | -54.13085 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ecd70e3-345a-3112-9313-277e8d2c1511 | 0.6618 | -59.55912 | 2026-10-06 05:23:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b9609d27-1837-314f-b29c-22a74819d6e0 | -2.99523 | -56.61061 | 2026-10-06 05:23:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 71e54cdc-1c6a-3297-b028-bbf1dc631b4b | -2.79068 | -54.10579 | 2026-10-06 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 018ee905-b715-3da8-af3f-92f5c7b1afec | -2.95226 | -54.15442 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12411c3a-86df-355b-aec3-659a8eaae0df | -4.77976 | -50.80987 | 2026-10-06 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f1e5ed6-b686-3197-b0bb-daf86ed8ed2a | -4.23764 | -49.9786 | 2026-10-06 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0517c958-0407-3f55-aa0f-0217cfe973a3 | -3.96134 | -56.05503 | 2026-10-06 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d850c88-dff6-35d7-9e75-f5acf0927bdf | -3.49439 | -49.8996 | 2026-10-06 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 18cefc85-f941-379c-a8df-6b94f59a349f | -3.63735 | -59.00173 | 2026-10-06 05:23:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e462f6b-486a-3656-a0d6-9a5714ed8641 | -3.52754 | -54.33042 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75ef365e-371e-33a1-b326-bb3c8620b422 | -2.83451 | -59.24551 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85e548d1-eee5-313d-b1a7-3fff6f026bcd | -3.38076 | -59.42938 | 2026-10-06 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 58bdb0ff-f8aa-3acf-ba30-b259cec249a6 | -8.78162 | -62.87395 | 2026-10-06 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2fceed2-c6bf-3982-b556-584830fe86c9 | -3.05535 | -54.21703 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8ca6cced-ab76-3039-8ed9-49cea68ebb10 | 1.90099 | -55.71904 | 2026-10-06 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 447d60ac-2605-39a5-9ff1-a49ac99d54de | -3.09161 | -54.17677 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52add2f5-0875-399e-96c6-b99ab272f6e1 | -3.08977 | -54.1599 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8b5ab742-6e73-3ff4-a683-ab37f7bb4764 | -2.88075 | -54.13951 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a57846d1-b678-3ce3-a2a0-14f32b2f9522 | -3.04084 | -54.25706 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ce490842-8314-38cb-86e5-2b27dcb0aa6d | 1.60825 | -55.76925 | 2026-10-06 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43be0625-f055-3a95-b896-b1d3872ec534 | -3.61554 | -55.50618 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c03f8506-c5e7-3f1d-add3-2f3af91fe94d | -3.38322 | -58.20639 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a4b16447-93b4-3312-a758-6e89872404a9 | -2.89655 | -59.02029 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9695b73-2282-349f-b53d-f96139a513aa | -2.80771 | -54.13672 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e952f0e-dc2c-3181-b944-ed5e8e739b55 | -3.10069 | -54.17409 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7b779f7a-4e5e-3b35-af0f-424891d75ae6 | -3.11185 | -59.1674 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d6d20dc-ad4a-38b2-99f4-2048febfce21 | -2.96204 | -54.14579 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 996ce0d3-18ef-35fe-a3c1-c005084c6340 | -3.46286 | -54.59201 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fcf7c88a-ae40-3db2-906f-3bd9cadbc6e4 | -2.87787 | -54.15886 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f495e58b-c0d0-3174-b380-92e4f944c1c5 | -3.54786 | -59.49102 | 2026-10-06 05:23:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8733d321-ade7-3887-8b5b-91890f76c21b | 1.72769 | -55.62327 | 2026-10-06 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a47fa78-de96-3aff-9115-a91976691800 | -3.05977 | -54.21629 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 27ed1d3a-fbcb-3201-b32f-65c63ad1fe07 | 0.91453 | -59.54467 | 2026-10-06 05:23:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd974082-ac15-3de5-9018-eefd7d70bbb5 | -2.89535 | -54.15789 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f9437f9-d7d6-32ba-816c-d6be80e45a78 | -3.50094 | -54.62096 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a98b7ab0-ee2e-3663-803a-9e9a6be8cf27 | -3.11418 | -53.75319 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb72f41e-77e1-3064-88ec-f3251a946a5a | -2.76941 | -57.67979 | 2026-10-06 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b5b1844-7049-3844-a697-3a4b2d735c11 | -8.59959 | -66.81049 | 2026-10-06 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b2ad78c-251e-34e4-9c1b-58db7f2ca20d | -3.14101 | -53.72261 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c50d45f-c671-3118-9aa6-d8dfa5f9e4b2 | -2.95295 | -54.14859 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ed2dc6d-b27a-3876-a659-8ad34796bf83 | -3.19125 | -57.85793 | 2026-10-06 05:23:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecb5fed8-532e-3ba3-9b7f-06782047299b | -2.95047 | -54.10956 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9986600-fd07-30f7-94ee-09d795f19dea | 1.86375 | -55.76284 | 2026-10-06 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55ad142b-0ab7-36c7-aec9-6c45dd561de2 | -1.63987 | -54.87189 | 2026-10-06 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81c7bc14-9be6-3ada-837f-f34c74aa31a2 | -3.11173 | -53.77006 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 82b569c5-27ac-3b85-806b-7fe611ba69ca | -2.90607 | -54.08648 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 54ae7890-594f-33d4-b63c-f7c08be7756f | -3.1175 | -53.7558 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4ed9198-8a9e-3b16-b5f5-ba83e5f184d4 | -2.99338 | -54.11026 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8fa2dcfb-c3e5-3791-888a-f8d58e788f32 | -8.34939 | -62.83096 | 2026-10-06 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bdc75883-8efe-3ab5-a138-070fcbfe9b99 | -3.08587 | -54.24445 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 782bd2dc-1d55-3ab7-a1c7-d8d430775051 | -3.38152 | -58.19485 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1472a9af-6956-3d2c-a77c-09aedaaeef56 | -1.61829 | -55.11255 | 2026-10-06 05:23:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9e0dafc-a04f-397b-b225-11b23698e25e | -8.35055 | -62.82365 | 2026-10-06 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2870456-9422-32d7-9a39-d0e8fcadc668 | 1.72603 | -55.62948 | 2026-10-06 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aadc42c2-0d56-34c7-a391-7b03073e09c2 | -2.06253 | -56.87545 | 2026-10-06 05:23:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3eb693e-131e-3def-b1d1-7576c1cceb9c | -8.76426 | -62.61517 | 2026-10-06 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a3da4feb-919a-33f7-9369-bdfbb4d2c378 | -2.86379 | -54.13687 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47d6721b-793c-3ab0-872d-94dfe01d6dc2 | -3.37698 | -58.20168 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 848e144e-801a-38f4-ad5b-37f2a0686319 | 3.21155 | -61.02633 | 2026-10-06 05:23:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| feb0a798-6d02-3e10-a73c-a18f12ea7b18 | -3.0465 | -54.21828 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 06da8500-3098-370e-a495-17d7b84f1c89 | -3.09204 | -53.71721 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 838f5815-0ed9-3620-9f07-9ba6123587c7 | -2.9468 | -54.16174 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 561b703d-4abb-39f3-9a14-993bcff05558 | -1.76352 | -55.03208 | 2026-10-06 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9901891d-6367-3a8f-ab27-9ca98c308c78 | -3.04871 | -54.23209 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac913761-a294-370d-b544-e7237a85b6cd | -2.90128 | -54.11841 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f4b961bc-3a82-369c-b5fa-69a7e89671ac | -3.06147 | -54.14918 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d2c32e23-249f-37c9-88ec-341f234c7f64 | -3.10439 | -53.75379 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09477a91-49fa-3c8e-8e14-0b2dc06f63e8 | -3.49624 | -54.62401 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 330ea2b5-2534-3b10-9ce0-a274ca64b54e | -3.13287 | -53.71702 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40f38e11-d33b-3277-ad11-d89ce128e632 | -3.05709 | -59.27979 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2cb0af7-6804-359c-a16e-920cbff3745e | 2.45685 | -50.82401 | 2026-10-06 05:23:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b0960fe1-0153-32cf-8415-ccc567160bca | -2.94638 | -54.16386 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cc845f0a-ad56-32d0-a1dc-8f68a3bc23b2 | -2.94801 | -54.15382 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e40ea8c1-7767-3343-b146-2f232b55926f | -2.95288 | -54.15045 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5321de27-c1c6-3d37-b0bc-112819048ff9 | -2.80712 | -54.14061 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 59061ab6-ed83-3071-a2b1-d35687402bd5 | -2.99398 | -54.10627 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d583eb6f-cc00-38f6-8b1d-7eff1acf0417 | -3.28104 | -54.18241 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f9d89f63-e69a-37d6-b729-d04e8e16b2b0 | 1.5612 | -55.98234 | 2026-10-06 05:23:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 041197a9-3693-36cd-9d70-31d651ebd736 | -2.78883 | -51.67038 | 2026-10-06 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ad05163a-3218-3997-8597-ecd432f90e79 | -3.06785 | -54.24945 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2e35f5a6-1a69-3294-96c6-4972d4b8ae05 | -3.80685 | -49.11632 | 2026-10-06 05:23:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3dbaa0f9-7517-306b-8f1d-a5fdb6d24329 | -3.04593 | -54.22223 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27709ce9-fb7a-331e-b043-8fe346de2013 | -8.96905 | -65.44517 | 2026-10-06 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README63.md)
