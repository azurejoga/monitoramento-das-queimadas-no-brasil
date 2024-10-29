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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df808a14-9df3-3ded-9ef8-37ecef37de1b | -3.80509 | -46.93058 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f3094b9-81f4-34ce-b954-64c0dd31016a | -2.61682 | -49.26985 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d849eb7d-6d87-3d94-97a8-c9682a6574d9 | -1.84063 | -47.45131 | 2024-10-29 04:38:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb1574cc-c438-399d-935e-fee426352bea | -1.67388 | -47.38629 | 2024-10-29 04:38:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a8a92de-ff47-3da7-9069-d3edcfaa35f7 | -1.67334 | -47.38978 | 2024-10-29 04:38:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8cb0f185-f09c-3e65-8e72-8dc524dff1e7 | -1.66138 | -47.46639 | 2024-10-29 04:38:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca5d1d9d-999b-333c-a326-58ecb1beca82 | -1.63443 | -47.24729 | 2024-10-29 04:38:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2cf9138-04cc-304b-a215-fd5d1351e4ed | -1.52592 | -47.20183 | 2024-10-29 04:38:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 299aefb2-26d3-362a-b72e-2307e8538976 | -1.52537 | -47.20534 | 2024-10-29 04:38:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 37f601d0-b82e-3d80-8aa9-c4583c53795e | -1.52482 | -47.20885 | 2024-10-29 04:38:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b515bf2a-d0e2-3701-9709-53bda66f5a29 | -1.52203 | -47.20483 | 2024-10-29 04:38:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6f63c22c-009e-3837-99b0-a99ed79c2f43 | -1.51372 | -47.21431 | 2024-10-29 04:38:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6898e8dd-d234-3fcb-a584-ff5df956d410 | -1.51038 | -47.21379 | 2024-10-29 04:38:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0bb26910-49b6-3e92-8b88-b308604fc4ed | -1.49983 | -47.21574 | 2024-10-29 04:38:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1752a042-73ee-3106-84dd-b69d349a06b2 | -1.27749 | -47.26688 | 2024-10-29 04:38:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3858e0af-c635-3691-bfe3-c9f4516a9808 | -0.99547 | -47.09045 | 2024-10-29 04:38:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 417a132b-70bc-3bfb-afa0-46d0040d2dce | -2.18406 | -47.95168 | 2024-10-29 04:38:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d98802e8-1bb6-3199-a4e7-e28039e0df68 | -2.18352 | -47.95512 | 2024-10-29 04:38:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59cc7772-18be-3e65-9fe5-4e907b974347 | -2.1813 | -47.94773 | 2024-10-29 04:38:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02d62b96-cd75-3b5c-84b8-6e156abd1386 | -2.18076 | -47.95117 | 2024-10-29 04:38:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 335467ec-9afa-3ac3-845b-d940319551f8 | -2.18022 | -47.95461 | 2024-10-29 04:38:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aca444f2-9632-336f-8830-32d40b5810cc | -2.17745 | -47.95066 | 2024-10-29 04:38:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 963387a2-d568-357e-b453-8fdfdbfd6e8b | -2.11142 | -48.11293 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1efb724e-ea0a-3204-87f0-15262339a2a0 | -2.09153 | -47.71813 | 2024-10-29 04:38:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36629258-52e8-3671-8b4f-644465cc167e | -2.09099 | -47.72159 | 2024-10-29 04:38:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed480cd0-dfd5-3cf4-a336-00d506447247 | -2.04621 | -48.02883 | 2024-10-29 04:38:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 17e8a2a6-3c02-3f5c-af91-4ca2755cda0d | -2.04291 | -48.02832 | 2024-10-29 04:38:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 000e831a-8fba-3f2e-b4e7-d7fd9864183c | -2.03081 | -48.648 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 029ba14b-fb2d-3da7-8931-9a0d084042cf | -1.98473 | -48.68303 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b1b17456-c8a7-32ca-9c77-62f56d8b688a | -1.98081 | -48.68224 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb156bd2-af75-34ab-a74f-f12d8d7f3a11 | -1.97698 | -48.68515 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2530d60-8ce8-3001-a07f-6365f78d1327 | -1.87056 | -47.82477 | 2024-10-29 04:38:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b93ed74b-1bb2-3f70-a658-cb6cabda0e62 | -1.86725 | -47.82426 | 2024-10-29 04:38:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55c45511-6386-311e-a07c-e831055245de | -1.79871 | -48.06714 | 2024-10-29 04:38:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1892497-5ab2-337e-ab70-b1ed2f84c4f5 | -1.78022 | -47.83551 | 2024-10-29 04:38:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cbb82b2a-1a2f-3204-87aa-b48cdd41ef2c | -1.77968 | -47.83895 | 2024-10-29 04:38:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 77542bae-051e-3cf6-9570-a64543f59961 | -1.77637 | -47.83844 | 2024-10-29 04:38:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8b052a85-c07f-3b57-8e2d-5d449953410e | -1.52624 | -48.69518 | 2024-10-29 04:38:00 | NOAA-21 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 873e72ce-a013-3936-80f3-39150830620b | -1.31979 | -47.75642 | 2024-10-29 04:38:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 77bebe50-a07a-30de-b0b4-4f0b75b7828b | -1.13229 | -48.38663 | 2024-10-29 04:38:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40938ce8-2b8f-3d63-934f-c6b91b1cc079 | -1.129 | -48.38612 | 2024-10-29 04:38:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b37b8ebb-4b5a-326f-88e3-497b633d1d1e | -1.12785 | -48.37191 | 2024-10-29 04:38:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 372f1098-1d1d-3163-9a3a-c385d9e41b7a | -1.12731 | -48.37534 | 2024-10-29 04:38:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0df3f359-d944-3f7e-b7b9-1d20843bf0cb | -1.12401 | -48.37482 | 2024-10-29 04:38:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f640b21-c73b-3704-a2db-7db4b8c4a37c | -1.05531 | -47.64076 | 2024-10-29 04:38:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 253f3c40-481a-390a-b5bc-6402b0235843 | -3.07353 | -47.48519 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e734086e-4dc9-3749-9b2a-625af66d0679 | -3.07298 | -47.48871 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6661e593-8793-3457-8c29-dde9be28ccb4 | -2.95854 | -48.9599 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 00b0be8f-45bc-33d3-aa5b-c8fe3ff4cb5c | -2.56174 | -47.43075 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 765322ab-22ab-3174-a0f9-eed04a61ac89 | -2.54528 | -47.51437 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 084a11c7-240d-371f-a551-c075214e5350 | -2.54195 | -47.51386 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74201bb8-1dea-3304-9078-b237b96c599b | -2.53861 | -47.51336 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9d4f2dba-9acc-39ae-99ec-684805b37873 | -2.53323 | -47.37239 | 2024-10-29 04:38:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0522fe04-3212-3a5a-9321-31922ba57dbf | -2.53269 | -47.37591 | 2024-10-29 04:38:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d007983-dcfc-3c59-b83f-6a4566864a78 | -2.52456 | -47.45022 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb7139d7-7631-342e-bd82-ab4055f7833b | -2.52402 | -47.45373 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6878aca5-db33-3bdc-8502-895cb964c89b | -2.52286 | -47.43919 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a05cfcc-654d-34fc-9494-41d282c54869 | -2.52232 | -47.4427 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06c8dde6-b9fc-3093-b937-c8c6cd5c7c80 | -2.52177 | -47.44621 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a34c434-9eaf-3a55-9dba-38af82076ec2 | -2.52123 | -47.44972 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8962f57a-e7e9-37fb-b141-fad7b944c4ea | -2.52068 | -47.45322 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 350adcda-c5dd-3ee6-8155-fa8a6a22175e | -2.52014 | -47.45671 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5661e8e2-309d-3b73-a958-4aeb5d2513c5 | -2.51844 | -47.44569 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80c97e48-525c-39cb-bd1d-3912ad14c520 | -2.51789 | -47.4492 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1b81d01-b198-31ed-a0ed-a131e15ca9d4 | -2.51735 | -47.4527 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 301754cd-5386-3afc-8490-b0411d3cc1c3 | -2.51456 | -47.44868 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 6a17aec9-5382-31f0-9363-4c68ad2f9309 | -2.51401 | -47.45218 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| ef3f73fa-e9fd-38b0-9532-ba5e3ed1ad65 | -2.51123 | -47.44815 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 6c0b16c2-614c-3b84-9ff5-d623b5640021 | -2.51068 | -47.45167 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 1f1c7a06-d3e6-34a3-9588-1b36cd6bb540 | -2.25911 | -47.47348 | 2024-10-29 04:38:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1d11e1a6-0575-3750-a7ba-631c119c7694 | -3.16076 | -48.73129 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 901c4039-38e5-3870-8d63-bddfe7daeb44 | -3.16022 | -48.73472 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d67e2f1-4fc7-315b-8fe2-03864fe39e8d | -3.15693 | -48.73421 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4480f983-fc6c-381c-a0fd-27909d18aa43 | -3.11546 | -48.65402 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d76f0810-65eb-3e3d-a303-7e7fcef47ed5 | -3.1127 | -48.65008 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| efeb3b60-cca6-3d98-b932-3e3c04921f62 | -3.1098 | -48.60398 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40e533dd-9850-37ce-82b7-d52f900cb05b | -3.1065 | -48.60347 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9823bb5-a874-3a0c-a205-660156ab9646 | -3.10374 | -48.59953 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cc9a0721-f054-30c8-8b03-f6346a139212 | -3.10065 | -48.66226 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1dfef741-293a-396c-ac77-186290fd2dad | -3.06247 | -48.94802 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 58b6b8a8-f8db-3a59-8f98-6faa6181e7a0 | -2.96448 | -48.63742 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05e3870f-4691-375b-8410-1eb6d057b089 | -2.96172 | -48.63348 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b7ec04d-5279-37b3-92de-9fe23cc36d6d | -2.95896 | -48.62954 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7241e290-a6e8-3339-a379-6359229cc7c0 | -2.94725 | -48.74713 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c52ce7c0-ce21-39cd-807e-f30a667d5439 | -2.9461 | -48.56084 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e2bb39b-853d-34ed-ab53-29ff4d061409 | -2.9443 | -48.98586 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a24368f2-0ab5-36ca-8d32-eff6c85e66bf | -2.9428 | -48.56033 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0fd5022c-cbce-3d85-a46d-54bf7d541b59 | -2.92168 | -48.95771 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0fe6df17-a53e-3ebc-9252-c52bc7e28807 | -2.9127 | -48.94567 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e67e4fe0-c8ed-3cc8-a0a1-01bb5fb7baa0 | -2.91216 | -48.94911 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 563b5ee3-5b8c-3183-b2c2-9ce882135910 | -2.91164 | -48.60817 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6076d633-7abe-391d-a5ab-107996be4df7 | -2.9111 | -48.6116 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 875b31e0-3e09-3365-9d33-2ef37904946e | -2.90888 | -48.60423 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41a18b11-a473-3761-b50c-e48b1a14176a | -2.90834 | -48.60765 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1f578f1-36f6-3d9d-b86c-529dd9dce2b1 | -2.90781 | -48.61108 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6b1e4db-5294-36a8-84cd-b42120850431 | -2.90727 | -48.61451 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e14a383-4a7b-33c4-b85f-e430a92e5ce3 | -2.85674 | -48.45839 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 51a4d34b-a28a-3fde-b7ac-b411f4b1e52e | -2.8562 | -48.46182 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 837d658b-6c62-3d79-a337-186939f84f53 | -2.81992 | -48.4562 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4430d941-e43c-3181-a5c9-61c9143a8666 | -2.81601 | -48.43803 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README40.md)
