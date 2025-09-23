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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ac5527f-b1b2-31b2-bbcd-9d73e364866a | -9.35819 | -66.51184 | 2025-09-23 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb4af534-e1f8-3ee3-b008-154a7ab5209a | -11.92445 | -53.55679 | 2025-09-23 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1a5e2c70-12d9-3fa6-827e-0e64e43274cb | -8.66796 | -66.58801 | 2025-09-23 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 928bfcbe-c16e-344b-85d3-2d03c566b18b | -9.63541 | -57.01379 | 2025-09-23 05:12:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5797b1e4-2543-3778-8bd1-b8c73948b94b | -9.94722 | -64.75613 | 2025-09-23 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 191786e5-86e0-395e-8c21-51087568253a | -9.35372 | -66.508 | 2025-09-23 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be9a8e43-2b60-3ec5-b574-fcb00313cafe | -9.90175 | -67.01192 | 2025-09-23 05:12:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5e9a407-b060-3552-824f-7aaf8bcf19b9 | -8.07847 | -55.04097 | 2025-09-23 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae3956d5-f6d7-3d38-8485-0e9023a6dbb9 | -9.28726 | -67.28752 | 2025-09-23 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 824ae18d-68e1-34f5-8162-2ed3c7eaab74 | -12.76571 | -57.88342 | 2025-09-23 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e5ce485d-9325-3db2-b3d3-67896c71bfbc | -10.05848 | -68.45786 | 2025-09-23 05:12:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 26dd4f14-24a6-34d4-b9bb-8fb7ab3074f3 | -9.45438 | -67.14553 | 2025-09-23 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d651292-b777-3415-84a6-77f97aeba585 | -12.40352 | -63.88389 | 2025-09-23 05:12:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 557ff265-62e6-3d3b-b70e-6ae08b0a935a | -11.92554 | -53.55334 | 2025-09-23 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8c27ecb4-097c-3734-8a10-f307a484f986 | -9.34979 | -66.5012 | 2025-09-23 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 272c300c-4ba8-3c0d-acbe-28164eeb13c7 | -12.76237 | -57.88289 | 2025-09-23 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a5c89714-68a3-3b7c-9b7d-7af3829744e3 | -9.44985 | -68.87891 | 2025-09-23 05:12:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 915f53e2-68eb-32f9-926d-49de244eb6df | -11.86553 | -56.877 | 2025-09-23 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bd0e40e8-125f-3693-841c-29259f2b6846 | -9.88781 | -64.83764 | 2025-09-23 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b56ea9c7-0265-3838-b933-a5434c3fc833 | -9.44905 | -68.88314 | 2025-09-23 05:12:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ea9e653-d440-332f-9b38-bd93b8dfa300 | -14.19689 | -53.29993 | 2025-09-23 05:12:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a62a9b2b-92f7-30aa-8559-425d5c9530c8 | -8.97377 | -68.02247 | 2025-09-23 05:12:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f19b9184-829e-319f-8447-407f030309b1 | -9.34926 | -66.50414 | 2025-09-23 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9c416c4-54e9-32b6-94a6-961202aeddd9 | -9.88858 | -64.83323 | 2025-09-23 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bcc3c218-86bd-3ce0-8862-8726127e931d | -14.18836 | -53.29894 | 2025-09-23 05:12:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 990b4d61-da60-3f1b-8427-7c4352db0382 | -11.8661 | -56.87325 | 2025-09-23 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d0da97d-aca8-39a7-a2a9-98a8c3d63f56 | -9.55967 | -68.55832 | 2025-09-23 05:12:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f22804f9-9395-3327-acdd-b77207e913e6 | -14.19262 | -53.29943 | 2025-09-23 05:12:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9a4cafb-d4f4-3348-a32d-1710d68cfccf | -11.92298 | -55.91186 | 2025-09-23 05:12:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a235addc-89d2-39c8-bcb6-d1e65a52e35d | -6.42144 | -67.91467 | 2025-09-23 05:12:00 | NOAA-21 | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08fefbb3-9581-3e66-b5d0-c31bea155189 | -9.89224 | -64.8384 | 2025-09-23 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2efbc63-cfe7-3bc6-9326-fcccd5150d1e | -9.46018 | -67.14323 | 2025-09-23 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7fc5bd9-bd76-3bd8-9952-327b95148201 | -12.40227 | -63.89093 | 2025-09-23 05:12:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bfb2e54-70f2-3d27-810e-51756133499e | -10.1036 | -59.3087 | 2025-09-23 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb9f2785-c32e-36c9-b2a7-851b7d91a2af | -13.01572 | -48.72557 | 2025-09-23 05:12:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe06672f-71bf-3de0-b857-58bccbc62e14 | -9.90743 | -67.0098 | 2025-09-23 05:12:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24905cbb-4ec4-3e45-82f1-69e171f38407 | -9.7083 | -46.63276 | 2025-09-23 05:12:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 029695f9-9fbe-3909-a226-4df8aa465054 | -10.8178 | -44.80666 | 2025-09-23 05:12:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a4b6727-2a09-3ac7-b277-c08e26a1111d | -12.76626 | -57.87983 | 2025-09-23 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| bb83ec73-f9e6-31ef-b65c-a3e66d3777e5 | -9.35319 | -66.51094 | 2025-09-23 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b845ef79-3cd3-3bdd-ae51-47733644172a | -12.4514 | -54.47223 | 2025-09-23 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0cffc8d1-a0ae-3744-bd9f-c5685b89b4b6 | -9.11692 | -68.32147 | 2025-09-23 05:12:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a41355b-bd3e-3cee-8e0b-d7a911309f29 | -9.44975 | -67.14142 | 2025-09-23 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5f9d014-ae1f-3e50-b0a9-05b8b346c1b9 | -11.92496 | -53.55314 | 2025-09-23 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 209fee3b-11be-301a-839c-1bf312d6c19e | -6.42721 | -67.91564 | 2025-09-23 05:12:00 | NOAA-21 | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1d9803f-e598-3b2f-ba28-8abdacda6cfe | -9.88981 | -66.99066 | 2025-09-23 05:12:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a71164f0-4578-320d-b35b-99b5305ccb59 | -9.35872 | -66.50891 | 2025-09-23 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8e9b9c4-a070-3cde-aa56-034379701e92 | -10.95799 | -45.69736 | 2025-09-23 05:12:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1ce2c9a9-7442-3d38-8c9e-bc5785154ae6 | -9.89301 | -64.83398 | 2025-09-23 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85859e30-0b00-3331-aaa4-a562af9bbce7 | -9.70769 | -46.63788 | 2025-09-23 05:12:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ab3e98c-94df-3027-af84-7693105ffe07 | -9.5899 | -46.43746 | 2025-09-23 05:12:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3fff4207-596a-37bc-9057-832b6f86ca7f | -9.29252 | -67.28853 | 2025-09-23 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb048863-4685-3ebd-9d17-4f00cb6d1225 | -9.47755 | -67.13646 | 2025-09-23 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c47dfb87-572a-362c-bdc0-77063ae63b09 | -11.92505 | -53.55699 | 2025-09-23 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4c8a8cb2-fb5d-3e64-a077-07546d27a557 | -9.46889 | -67.12499 | 2025-09-23 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d3d742d7-843d-3302-ac59-a606a6bef5ba | -9.22228 | -67.57663 | 2025-09-23 05:12:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f1a5b65-b097-3e57-aed9-61a8d086de1f | -12.76292 | -57.87931 | 2025-09-23 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| cff6a3f8-faea-397f-8164-122d52e29bb1 | -9.47235 | -67.13548 | 2025-09-23 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ed2aa2c-866a-3047-acb6-fec4ab4f7c0c | -9.4394 | -68.93398 | 2025-09-23 05:12:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97b1585d-8b87-34a0-b918-0aab2facd83e | -11.91944 | -55.91135 | 2025-09-23 05:12:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42de0353-938b-3d07-a5e5-8aea7e24a8cc | -9.88469 | -66.98975 | 2025-09-23 05:12:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3275da4-5548-3e6f-8b66-1863c579cf88 | -9.27936 | -57.1623 | 2025-09-23 05:12:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2da47b84-b870-363e-b2ea-36c8e38a1e26 | -9.46077 | -67.14001 | 2025-09-23 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eeda2d98-9bc3-35ab-b4fe-b7ea40042472 | -9.19359 | -67.56766 | 2025-09-23 05:12:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 519a9fbd-ae97-37bb-a997-ef0e22859b31 | -9.44019 | -68.92984 | 2025-09-23 05:12:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 751fd469-5931-3db2-bd8a-ab71b76f169e | -9.9304 | -64.74883 | 2025-09-23 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1361bddc-263c-3fa0-8abd-ce82a559da64 | -9.44916 | -67.14463 | 2025-09-23 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66218e46-4bc2-312e-8bf3-a8489e39c5a6 | -12.74959 | -57.8772 | 2025-09-23 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b7200967-01df-3c7b-90f0-34ee8e76482d | -10.81852 | -44.80028 | 2025-09-23 05:12:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae8d0312-7a85-327f-b231-e3c2021195bf | -12.4029 | -63.8874 | 2025-09-23 05:12:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6afb92e-ebe2-367f-a00c-bc5374122447 | -9.19296 | -67.57117 | 2025-09-23 05:12:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db2a9bfe-f54c-3dd6-8009-4d0c981a9f6f | -9.28215 | -57.16637 | 2025-09-23 05:12:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20c01fd5-c480-319b-a5c7-45ee5c4af0c0 | -14.19634 | -53.30404 | 2025-09-23 05:12:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bbbea19e-82fc-3f3f-a5d0-d91163a84c2f | -13.01617 | -48.72174 | 2025-09-23 05:12:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 386f7bf8-c5c6-3ed7-9315-a2ecc7ed5048 | -9.11765 | -68.31755 | 2025-09-23 05:12:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8415d732-73a9-35df-ba35-0985993326ef | -13.01663 | -48.71777 | 2025-09-23 05:12:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e73bf4fa-7d3f-395e-ac6d-08bf86ddee8a | -10.95866 | -45.69131 | 2025-09-23 05:12:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 053c4782-0990-376e-b225-54954da6272f | -9.92151 | -64.74868 | 2025-09-23 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec53de78-8987-3ed1-b62e-a80e3dadfdac | -12.76959 | -57.88036 | 2025-09-23 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 34c7db8d-db06-31a8-8a7c-a8857b922abe | -12.75292 | -57.87772 | 2025-09-23 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 333cf79a-2300-3907-a95c-aef7e789967f | -9.35425 | -66.50508 | 2025-09-23 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 96d3e503-a4a1-32a5-b36d-b7f118810b02 | -9.55757 | -68.55887 | 2025-09-23 05:12:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 891b2bd5-872a-33ba-b792-0824a624edd8 | -9.93031 | -64.7502 | 2025-09-23 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48aeba63-5874-3d13-8c89-1fcf828fd40e | -9.92591 | -64.74944 | 2025-09-23 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5ba6904-7a2c-36a8-b16d-2102392509fa | -9.63766 | -57.02142 | 2025-09-23 05:12:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32a6c473-e141-320c-974a-210ddd870f46 | -9.63821 | -57.01786 | 2025-09-23 05:12:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbf5bc86-f15b-3235-b8e0-ca1a86971d5b | -9.94277 | -64.7568 | 2025-09-23 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d7af4e2-cd42-3d8e-9fa1-2fdc63a6ad23 | -10.96134 | -45.69662 | 2025-09-23 05:12:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1099d421-4423-3b51-85c2-ad590136ec41 | -9.46831 | -67.12815 | 2025-09-23 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 01e42999-5b5f-32a5-b20e-30362372ce58 | -9.27882 | -57.16585 | 2025-09-23 05:12:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b46c97c4-9d8b-317f-8084-8070c5a6a58e | -12.74904 | -57.88078 | 2025-09-23 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4037fa57-aa8b-3d39-bbd4-b5aa1bb15995 | -9.94282 | -64.75539 | 2025-09-23 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1cc708a8-20f4-3e6a-979e-26901a7700ae | -15.9529 | -59.48767 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc2f33ae-037a-332a-9f11-5c2970a8f5eb | -15.31407 | -59.41843 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 984a3a87-4f5c-353a-8d1b-1855a91e5a9d | -15.92602 | -59.37395 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f77f1830-ffe8-3e21-bdda-182b526f69e3 | -15.35272 | -59.19127 | 2025-09-23 05:14:00 | NOAA-21 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 85a09606-c8c4-3d1c-ba69-7d3742c693ca | -15.14625 | -59.46759 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9986648d-2b73-3d6e-a660-5ab6987775e8 | -15.36539 | -59.17508 | 2025-09-23 05:14:00 | NOAA-21 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38410a50-0b12-335f-a8d4-8fd487fbacc9 | -15.94411 | -59.47892 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f82b013-e47b-3103-9106-140f33f1106a | -15.41257 | -58.77925 | 2025-09-23 05:14:00 | NOAA-21 | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README21.md)
