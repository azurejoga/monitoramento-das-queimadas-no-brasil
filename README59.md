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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8b2046c-1ede-3714-9f0f-c9a1cf5c197a | -2.7244 | -54.1351 | 2024-11-06 05:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 9c1f1b91-c70c-328b-970d-9c181ffcea34 | -3.0213 | -53.2607 | 2024-11-06 05:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 239da133-fbdb-36cd-b1c9-effa4f75d57d | -2.937 | -51.0673 | 2024-11-06 05:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| dd6ca34c-1ee5-3c81-8d8e-5c52a35d13ec | -1.3579 | -51.94791 | 2024-11-06 05:29:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b140d65-ed11-3663-8b2f-cbae41875c4f | -3.74068 | -58.52752 | 2024-11-06 05:29:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df965e6e-fd93-3092-b4df-4517d175d85c | 0.1407 | -62.56035 | 2024-11-06 05:29:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23266ace-5535-3b44-b56b-3e9cc16b5298 | 1.34883 | -50.87718 | 2024-11-06 05:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bfe39971-2cff-3952-b71b-96281403b596 | -3.59837 | -58.60292 | 2024-11-06 05:29:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c18d7e4c-95ac-3ba3-bedf-8ae53201f0ca | -4.22119 | -53.55871 | 2024-11-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a3b4987b-a44f-34ec-8856-22fc45538ac7 | 1.60389 | -61.02684 | 2024-11-06 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f04aebd7-95a3-3cda-8a1e-e63e20ac9f10 | 1.13236 | -59.44318 | 2024-11-06 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37b35caf-97d7-37e3-ad3c-180734a9a8ce | -3.06932 | -59.21545 | 2024-11-06 05:29:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 465799d2-edcb-3a31-99d1-f60dbdb2bf5f | 0.18468 | -51.06263 | 2024-11-06 05:29:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3560394a-91fa-3c48-a14b-4dbe12ee575d | 1.34939 | -50.87834 | 2024-11-06 05:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce18cd75-82f5-30ab-8dc3-40f562f4e181 | 1.3439 | -50.87922 | 2024-11-06 05:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1abe130a-1f17-3f54-a9d0-88bcbf1ac135 | -4.30209 | -50.74552 | 2024-11-06 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2057015a-2953-3a01-b291-d6fd4a1cd698 | -4.66308 | -50.97398 | 2024-11-06 05:29:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ac94e2f-d5ea-318e-a259-e856db084b9e | -4.22078 | -53.5616 | 2024-11-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f60bb366-8b43-388e-b3a0-27438b9e1857 | 0.1786 | -51.05994 | 2024-11-06 05:29:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ea07b02-a131-33cc-a85a-ccfa81fd4e31 | -3.74363 | -58.53222 | 2024-11-06 05:29:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f593558a-4e18-35f8-adfe-6afdd428befe | -4.41011 | -59.52869 | 2024-11-06 05:29:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a22003b-bea9-380e-a09e-894041c08d85 | -3.74004 | -58.53166 | 2024-11-06 05:29:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5efbe9a-a69f-37d3-8a7a-d9f82581c1ee | -3.44669 | -56.93359 | 2024-11-06 05:29:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 545bcb64-4a16-39f0-ba04-6a4da8e578e3 | -3.97724 | -59.20027 | 2024-11-06 05:29:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6c6ca38-3f3a-3300-9042-db0370f703ea | -3.44672 | -56.93502 | 2024-11-06 05:29:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ba14b2f-d86a-396f-8903-7e5f7755a825 | 1.77639 | -50.43528 | 2024-11-06 05:29:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e097800-6d42-3e79-9c50-a4ec793fb537 | -4.40608 | -59.53196 | 2024-11-06 05:29:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 19ca1a65-3353-3485-8cf7-8bec47e08e7b | 0.17916 | -51.06351 | 2024-11-06 05:29:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c1b23bf7-f3c3-3176-b6f6-1e9ee744092b | 0.1742 | -51.06814 | 2024-11-06 05:29:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db94c76d-c6a0-348a-b616-7acfc1dbd76a | -4.30474 | -52.68443 | 2024-11-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42c1e9a3-4738-3fba-9dfa-715fef6a22d5 | 2.638 | -61.44175 | 2024-11-06 05:29:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac7292bf-8500-39c4-9458-2fd7a17ef8ac | -4.04363 | -54.68113 | 2024-11-06 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1f7af085-03db-3e7d-88c0-794db0854ed1 | -1.39125 | -52.18839 | 2024-11-06 05:29:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca21afb7-af35-3042-b72c-b575f5389867 | -3.24567 | -57.56425 | 2024-11-06 05:29:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8108b42c-3524-3f6c-8d35-b62059298a6b | -3.59185 | -58.59777 | 2024-11-06 05:29:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e4206bab-712c-3edc-9274-0d4ffb0d40b1 | 0.17857 | -51.05986 | 2024-11-06 05:29:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9a86aa51-7cd3-3741-a562-3defed25805e | -3.118 | -59.9282 | 2024-11-06 05:29:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b9bc753-8eb3-3f07-a86d-69d09d3ab475 | 2.63466 | -61.44226 | 2024-11-06 05:29:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ea2a077-58c2-3603-9416-e37db39db76e | -4.27516 | -50.71812 | 2024-11-06 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 882e8db7-6b8d-3341-9910-777f01e157b8 | 0.81918 | -59.79133 | 2024-11-06 05:29:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d2220d3-467c-37e9-9529-0e57099072fa | -3.59542 | -58.59831 | 2024-11-06 05:29:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 12eddc86-d68f-3010-af67-5a72da348063 | -4.40953 | -59.53248 | 2024-11-06 05:29:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9e13ba9e-40c5-3f45-b9ce-8c9ffd722072 | 1.34334 | -50.87809 | 2024-11-06 05:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da70cbcd-c677-3cea-b1ea-c920b0957da1 | 0.63824 | -60.24722 | 2024-11-06 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4787b16-bd2a-3fd0-a3ae-b9494bd94d87 | -0.34658 | -51.5704 | 2024-11-06 05:29:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18ab2fc6-d6ad-3dfa-9e80-89fc24fd77a1 | 1.35371 | -50.87027 | 2024-11-06 05:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b13acc6e-3076-3f26-8c3d-0f564f9e0993 | 3.6062 | -51.32299 | 2024-11-06 05:29:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1d71e3cb-ffaa-3340-8ff3-e4bd9f676c1a | -0.39902 | -51.9934 | 2024-11-06 05:29:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db455ebd-5a8b-3394-8afc-97938c73763e | -4.21578 | -53.56089 | 2024-11-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b6c18c4-ae3f-30f9-afca-18bb09484c83 | 3.61235 | -51.32819 | 2024-11-06 05:29:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 646dab7d-fe94-3e3b-b8b1-077fcf1dfb01 | 1.12848 | -59.4402 | 2024-11-06 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0aa65309-d68d-3358-8b2e-1ad941e85b01 | 3.61184 | -51.32513 | 2024-11-06 05:29:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fa6dde60-7ee1-3597-9bf3-0774940859b6 | 1.12127 | -59.43773 | 2024-11-06 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b475b347-a76c-3ae4-b44d-61ba437891c5 | -1.35206 | -51.95036 | 2024-11-06 05:29:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c14a6dbe-c3f7-369e-bba7-bf29416d9fb2 | -4.73471 | -48.97161 | 2024-11-06 05:29:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 196daa22-c15c-3594-a42f-9f72ee198ce0 | 3.60518 | -51.31688 | 2024-11-06 05:29:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0156ff28-d6c1-3739-a787-496a4bc6be1e | 3.51691 | -51.2426 | 2024-11-06 05:29:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a51d552-95f3-33b3-84bc-2a4c2a4eb74c | -4.27453 | -50.72264 | 2024-11-06 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 143cc527-af9b-341f-b02b-9e7e6db055a7 | -3.74427 | -58.52808 | 2024-11-06 05:29:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95fc4240-de77-3a60-b797-9a75b14bf283 | -4.39905 | -50.50172 | 2024-11-06 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cbc3ad0c-6b55-3de0-ad25-c078945b8dea | -0.40325 | -52.00061 | 2024-11-06 05:29:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7ddcdf3-54d5-39af-bf8b-6c609c5b6943 | 3.60569 | -51.31992 | 2024-11-06 05:29:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.3 |
| df02b812-22bf-3d27-8753-be9ce7ebdf44 | -0.38754 | -51.99825 | 2024-11-06 05:29:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3262d1ea-1953-319b-9ddc-85e6c97f32a1 | -3.96389 | -59.19426 | 2024-11-06 05:29:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7cf24c6-95f3-3980-90d1-b2eda7d9bbff | -4.38302 | -59.4974 | 2024-11-06 05:29:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce8962b0-a8de-3212-a583-7729e926d126 | 1.05508 | -59.5588 | 2024-11-06 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2f26ad93-1abd-3a39-9af4-93b194e5aead | -4.21537 | -53.56376 | 2024-11-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 73a3316a-847c-3e04-8e4f-0a0d9aa1065f | -3.39239 | -60.48986 | 2024-11-06 05:29:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46daac5a-b441-322a-ad38-04f3e2b75fce | 0.18525 | -51.06639 | 2024-11-06 05:29:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6550fbf4-190b-3b9b-bcb2-a8206108425e | 3.55197 | -51.48846 | 2024-11-06 05:29:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c9eb085-764a-396f-8eb9-a488ffc9f564 | 0.64155 | -60.2467 | 2024-11-06 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 241415b0-25c0-3dce-a17c-4763c2990249 | -4.66244 | -50.97836 | 2024-11-06 05:29:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e660f52f-ed19-39b3-8260-0d1e688fd68a | 0.18527 | -51.0663 | 2024-11-06 05:29:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db97f0fd-aa4e-3bed-9801-fb6af11ae2be | 3.60672 | -51.32608 | 2024-11-06 05:29:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| aa9b397c-854b-305f-999b-fbd7487023f1 | 3.55148 | -51.48544 | 2024-11-06 05:29:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98d2e9bc-e0d2-3be1-8c3d-3369e197da3c | 0.17422 | -51.06802 | 2024-11-06 05:29:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 75b8e6fd-0add-343a-87e8-b421d0b3a5ed | -4.21121 | -53.55727 | 2024-11-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69772c25-4ccb-3378-952b-e0160a1b00a3 | -4.51827 | -50.31828 | 2024-11-06 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c301cf33-2f22-39aa-9d6a-58a7caadc63b | -1.06202 | -53.65607 | 2024-11-06 05:29:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8d6faa68-caff-3eeb-9822-4024e88ceaf1 | 0.18413 | -51.05904 | 2024-11-06 05:29:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fb3ea267-a338-3daf-b632-6ffc42569462 | -0.39328 | -51.99583 | 2024-11-06 05:29:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 01d5f133-9c0e-3242-ae84-f050b13eb71b | 0.64208 | -60.25014 | 2024-11-06 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fc6a45c-8b14-3abe-9f3f-49e7e12c7813 | 0.18469 | -51.0627 | 2024-11-06 05:29:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b39197e0-b4c9-3bce-a42b-e3ae307f45ce | 3.61133 | -51.32206 | 2024-11-06 05:29:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c56d964e-c7ac-3ba4-8ebe-1057f683db01 | -4.51387 | -50.31476 | 2024-11-06 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b451b3a5-1926-3459-9ffb-4f3be479b7d6 | -4.4465 | -50.6981 | 2024-11-06 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c971547-b24f-30cd-b055-8fb4793f52bf | -3.5948 | -58.60238 | 2024-11-06 05:29:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3fb2ea53-ada0-37db-86b8-558f818d63b3 | -1.3898 | -52.19802 | 2024-11-06 05:29:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 59bb8b72-b612-3ff7-aed0-27ef5de78689 | 3.3469 | -51.28571 | 2024-11-06 05:29:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| adf0adc9-454d-3e14-9916-d6033231665d | 1.3488 | -50.87473 | 2024-11-06 05:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 774863b1-d571-3e13-bc77-9ef72e0feb5a | -4.51891 | -50.31359 | 2024-11-06 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c3aa2c3a-b9db-38c8-af78-1647e2802c15 | 1.782 | -50.43434 | 2024-11-06 05:29:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1fc56e14-9b78-327f-b4c9-93ff113ef6b3 | 1.12903 | -59.4437 | 2024-11-06 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e1f29a9-4e29-39c7-8316-6cc7fb338ea8 | -3.2813 | -61.50971 | 2024-11-06 05:29:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0bbaf244-2ae4-3c92-930a-5b59c3083f1a | -4.52012 | -50.31534 | 2024-11-06 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 93c59252-4109-3350-881e-da1c37813e12 | -4.65989 | -50.97472 | 2024-11-06 05:29:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da75308d-8f2a-3e91-8f5f-c327946ec1ae | 3.61031 | -51.31592 | 2024-11-06 05:29:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 84cff496-261a-31e7-99a3-659b469f6298 | -1.35739 | -51.95121 | 2024-11-06 05:29:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8523f80-97b0-3dd3-8223-d75f20dafc07 | 0.38286 | -62.67432 | 2024-11-06 05:29:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 365dc043-50dd-3569-b6c4-cb885d24cd6a | 1.13182 | -59.43968 | 2024-11-06 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README60.md)
