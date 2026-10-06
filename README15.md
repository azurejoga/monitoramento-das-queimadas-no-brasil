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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c31aeaf4-6e01-3027-91bc-b8b86ec38b7d | -7.36422 | -72.45988 | 2026-10-06 01:54:00 | TERRA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 772aeab1-b466-3e70-b7c1-a501073824d3 | -5.8511 | -45.0091 | 2026-10-06 02:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 1314c7db-8bd1-35ba-8d53-71463ac9d239 | -9.0231 | -65.7169 | 2026-10-06 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 92320597-de70-3205-9cb2-80eafb14e077 | -11.299 | -45.5025 | 2026-10-06 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 7e1f4890-883d-35aa-9128-0367a2424fee | -2.9816 | -54.1291 | 2026-10-06 02:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| cbff6ce2-3e1c-331d-9e23-1f089d6f714d | -8.7036 | -45.2061 | 2026-10-06 02:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 3fd33644-b89d-3041-a7e5-c75711a93947 | -2.7796 | -54.1138 | 2026-10-06 02:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 8fcc1e0e-7505-34c5-a16e-0696b7ca27d1 | -8.7033 | -45.2289 | 2026-10-06 02:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 60.4 |
| d8dbaf35-b50a-30a0-bb20-7dd4230652cc | -3.6732 | -55.9425 | 2026-10-06 02:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 88b49ad5-454b-3d5c-b3e4-1994f82380f3 | -3.0191 | -53.9071 | 2026-10-06 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 417e9dff-9c0c-3237-b9be-697aac777ca9 | -2.7879 | -57.6649 | 2026-10-06 02:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| ad4f443c-05bd-3757-b0a2-1794e39e99a4 | -3.6731 | -55.9622 | 2026-10-06 02:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 78f031bc-710e-37c3-b58e-b8e2b43b5935 | -9.7126 | -65.0951 | 2026-10-06 02:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| f4363bfd-3bcd-393b-869c-2b81dd5134f7 | -11.2798 | -45.5052 | 2026-10-06 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 379.4 |
| baac3795-e396-3389-be4e-69199f84d439 | 0.4465 | -60.5442 | 2026-10-06 02:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 7d21410d-972f-32a5-9475-90cb4a10c6e3 | -14.9165 | -59.3855 | 2026-10-06 02:00:00 | GOES-19 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 102.0 |
| befcd975-6c04-346f-8442-543f36d89012 | -11.2611 | -45.4849 | 2026-10-06 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 09e83b6f-44cd-350b-9651-ccbf24023fe6 | 0.4465 | -60.5252 | 2026-10-06 02:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 14f377ae-7db7-3b83-927e-e19be4990a8e | -5.8323 | -45.0105 | 2026-10-06 02:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 027d9ad0-0a72-3a18-9b0e-8bd77b5bad86 | -3.0 | -54.1287 | 2026-10-06 02:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| daea494a-68b0-34e7-a5eb-56414f335743 | -3.3723 | -58.1957 | 2026-10-06 02:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 9f49617a-13af-373b-b4b8-9975ab368c4c | -11.2794 | -45.5281 | 2026-10-06 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 720a8c3f-186c-34b2-977b-f23a0f573de9 | -11.2802 | -45.4823 | 2026-10-06 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.6 |
| b190f8f3-c3b6-3bec-9363-89bd60b32725 | -9.7312 | -65.0944 | 2026-10-06 02:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 51337a17-c851-30b4-962c-1506e862f087 | -2.7879 | -57.6843 | 2026-10-06 02:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 34011dcb-4b57-3636-b83f-44131614a1b0 | -9.7313 | -65.0757 | 2026-10-06 02:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.1 |
| eb1b3635-4828-39ba-ba63-6d468f3e6038 | -3.0375 | -53.8865 | 2026-10-06 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 13979ef9-aff4-31ca-b176-4f75b86c70d4 | -3.6915 | -55.9618 | 2026-10-06 02:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 22428079-1891-34fa-beaa-21ad87427f24 | -11.2607 | -45.5078 | 2026-10-06 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 197.0 |
| 6d467a1e-dab5-3d18-921c-1d3593e15f38 | -3.6915 | -55.942 | 2026-10-06 02:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| e59223f2-c167-39e2-b793-b0dee1018739 | -3.0375 | -53.9066 | 2026-10-06 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 16698aad-8748-31ac-bbdd-0953f148cd5e | -3.3906 | -58.1953 | 2026-10-06 02:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 66c41d63-c33b-3cae-b622-dee60b18d5da | -2.7796 | -54.0937 | 2026-10-06 02:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 475af4b1-f69f-3275-a741-c44b62da69de | -3.0192 | -53.887 | 2026-10-06 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 4ee4865f-1596-33f1-8b07-e4bca14e7094 | -9.0045 | -65.7174 | 2026-10-06 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.2 |
| be8bbf16-e44e-3536-af33-c68838056dcc | -9.7312 | -65.0944 | 2026-10-06 02:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 87.9 |
| e52b4a39-c0f7-3ae4-baf9-86c1a3351e0e | -3.6731 | -55.9622 | 2026-10-06 02:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| bc4e3da6-9a6f-3ff0-8319-265d67aaf208 | -3.3723 | -58.1957 | 2026-10-06 02:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 80.0 |
| eb26a37e-6828-3e93-bddd-dcda756658ff | -9.0232 | -65.6982 | 2026-10-06 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 4b963469-ee6d-3f18-8f14-846d49716d97 | 0.4465 | -60.5442 | 2026-10-06 02:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 56.9 |
| b1ef7b56-d967-3531-958a-946a0f361c2f | -2.9265 | -54.1305 | 2026-10-06 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| ed6378f4-0b8c-3e73-938b-329bf74a9dbd | -3.1115 | -53.7637 | 2026-10-06 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 8bee5055-7168-3ac2-99d0-48b3d2d7809a | -2.9448 | -54.1501 | 2026-10-06 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 2dda7b46-05dc-3fe1-96e0-f55d65b02ea4 | -3.6915 | -55.942 | 2026-10-06 02:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 4ce467f2-8079-31d0-bc19-33d7230b0620 | -2.7796 | -54.1138 | 2026-10-06 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| c1c40f82-cd9b-317d-a468-5121d4ef5731 | -2.7879 | -57.6649 | 2026-10-06 02:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 0cc0d5c3-dd3f-3bc2-9e2a-70aa54783018 | -5.8323 | -45.0105 | 2026-10-06 02:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| f7069aad-ce9f-3025-97e4-d392c0ede7fe | -8.7036 | -45.2061 | 2026-10-06 02:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 59.6 |
| b80e9893-efdc-3fee-81b1-17e8eb360299 | -2.8713 | -54.1518 | 2026-10-06 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 136.9 |
| b68bde3b-8a1a-3cfb-9b2b-b0e0007851df | -9.023 | -65.7355 | 2026-10-06 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| a1397b1d-8133-315e-951b-149edc9f120e | -2.7879 | -57.6843 | 2026-10-06 02:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 26910224-babc-368f-9af5-8295d09fa0bd | -2.9816 | -54.1291 | 2026-10-06 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 3e4a16a1-6549-3104-8c40-85cee9f6b557 | -2.9449 | -54.13 | 2026-10-06 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| f3d30b46-0f94-3869-b510-6b63de114bc9 | -9.0231 | -65.7169 | 2026-10-06 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 238.5 |
| 78c4e5a2-0052-3d14-bcb1-d79680693b68 | -3.0933 | -53.7037 | 2026-10-06 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 83261b96-820e-3ab5-80d3-89135c65d9fc | -3.0917 | -54.1867 | 2026-10-06 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 4d14c329-b3ce-3459-aa25-727c3181f3e3 | -11.2607 | -45.5078 | 2026-10-06 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 129.0 |
| ca53992f-fa20-3c99-9fa5-069947524c91 | -8.7033 | -45.2289 | 2026-10-06 02:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 3f02746a-d5fa-3398-a1f6-d27fc0866ee9 | -3.0 | -54.1287 | 2026-10-06 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 93ebb589-e63d-3676-a343-a7336aad2e2d | -3.0932 | -53.7441 | 2026-10-06 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 5fcebb99-036c-3673-9fdf-10f2bbd88202 | -3.0375 | -53.9066 | 2026-10-06 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| a3d167a2-3064-3f86-9b49-7644931a2e0c | -3.1116 | -53.7234 | 2026-10-06 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 4264b1d1-4bc2-36aa-a8ae-72370311ea2d | -2.7796 | -54.0937 | 2026-10-06 02:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 1d83cd6f-d0cd-37ef-b5a2-45eeb320e9db | -3.0192 | -53.887 | 2026-10-06 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 14013a84-ba41-385c-9181-4bf960979f6b | -2.8714 | -54.1318 | 2026-10-06 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 1fa6b23d-c612-3104-9496-017ea90d1c72 | -3.6732 | -55.9425 | 2026-10-06 02:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| ae1718a8-0f2b-37ee-99f4-e2759b1daf20 | -3.0734 | -54.147 | 2026-10-06 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 0a9d0f69-4940-3b90-ba69-85c4efef4e4a | -3.0734 | -54.167 | 2026-10-06 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| a6b577d8-4e99-37af-87b0-8dbcbc1e73cd | -3.0917 | -54.1666 | 2026-10-06 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 130.3 |
| 484ba91f-e750-38dd-9c89-971791806883 | -2.8897 | -54.1514 | 2026-10-06 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| ad7f806d-8ca9-38d7-aadd-096514f5a7ce | -5.8511 | -45.0091 | 2026-10-06 02:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 22919d10-4116-371a-a79d-8c3a0e1843c4 | -2.8712 | -54.1719 | 2026-10-06 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 44c5e00d-c85a-31b0-a755-a26eeac247c5 | -9.7313 | -65.0757 | 2026-10-06 02:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.4 |
| c0c3605f-446c-36e7-95b4-6898f706dcc6 | -11.2802 | -45.4823 | 2026-10-06 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.2 |
| d1edb716-325a-336a-87b7-c3fecea9d421 | -3.6915 | -55.9618 | 2026-10-06 02:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 243e5e6c-acb0-3ad3-adcd-a5a21ff362f9 | -11.2798 | -45.5052 | 2026-10-06 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 243.6 |
| 1c8f96d0-936d-35da-8b18-4b0d804bda30 | -11.2611 | -45.4849 | 2026-10-06 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.1 |
| e3c880a5-db54-3b16-aeb5-d9ae03b30bfb | -3.0932 | -53.7239 | 2026-10-06 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 611e4720-b944-3949-b6fd-f30e64238998 | -3.0191 | -53.9071 | 2026-10-06 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 5d152e1d-3cab-3fe8-9cc2-ead8ecf993f1 | -3.0375 | -53.8865 | 2026-10-06 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| df99863e-609b-3e8f-84c0-87bff6d15bf2 | -11.2794 | -45.5281 | 2026-10-06 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 39.7 |
| d900f8cb-c017-305e-9def-66f1204cc092 | -9.7126 | -65.0951 | 2026-10-06 02:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 7adadc24-2d53-3af4-989c-f39ba2b0224b | -2.9265 | -54.1104 | 2026-10-06 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 48c142a7-7d23-371c-b47b-7645263d3ee2 | -3.1116 | -53.7436 | 2026-10-06 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 619018e4-0a70-30c6-a7e0-dce5c9107ee0 | -11.26 | -45.53 | 2026-10-06 02:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f71cb6dc-1a43-3569-949c-92495e060132 | -11.26 | -45.48 | 2026-10-06 02:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 80e050e3-5d61-36b1-b329-c8b2cbd57e49 | -3.0375 | -53.8865 | 2026-10-06 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| a795426b-e1f4-3379-98bd-755b5bcc4bc9 | -5.8323 | -45.0105 | 2026-10-06 02:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 83b7f372-365e-3c12-baf4-aff729f050a4 | -9.7312 | -65.0944 | 2026-10-06 02:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 96.6 |
| a1bc7ec0-6091-3113-9493-376664f67967 | -3.0191 | -53.9071 | 2026-10-06 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| ec0f79f6-70ef-32e6-b977-db4b71db2633 | -3.6732 | -55.9425 | 2026-10-06 02:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 49912f89-b9da-3e25-95fd-67cdd190155b | -2.8713 | -54.1518 | 2026-10-06 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 2c26f8a9-ad8f-329f-bdc0-04a39b139f91 | -8.7036 | -45.2061 | 2026-10-06 02:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 8fd63768-e8b9-3560-913d-6e587ea5cb1c | -3.0734 | -54.167 | 2026-10-06 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 6cf2630e-ae1b-3e28-810c-471e20ad8118 | -9.0231 | -65.7169 | 2026-10-06 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 174.7 |
| feba33c8-0b16-30c9-861e-fb381b0c63b0 | -3.0917 | -54.1666 | 2026-10-06 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 140.1 |
| 4e6b1085-eeab-37be-aa95-e8bd19f22650 | -3.3723 | -58.1957 | 2026-10-06 02:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 2ae095e8-8cd5-312c-b41a-919dca776745 | -3.6915 | -55.9618 | 2026-10-06 02:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| fc989d02-b254-3f6c-9dda-a5618f034494 | -9.7313 | -65.0757 | 2026-10-06 02:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.7 |
| f04f23e4-a4b2-316c-8291-2a4abcbe3e76 | -11.2607 | -45.5078 | 2026-10-06 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 144.5 |


[Clique aqui para ver as próximas entradas](README16.md)
