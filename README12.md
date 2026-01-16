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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6635a17b-edd6-342d-a43b-f5f2364cb7f3 | 2.69699 | -60.05686 | 2026-01-16 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5de02b3a-39c2-39d7-90bf-45c3fc4c51fb | 2.74828 | -60.23064 | 2026-01-16 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9fcbbc75-9311-3506-8de8-6eeb3a260e9c | 2.75196 | -60.22564 | 2026-01-16 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 461f72dc-d0dd-3d45-b191-3fe55ed4b2bd | 2.94525 | -60.33467 | 2026-01-16 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6541bfb0-b743-36f5-95df-fd1ac981c33f | 2.69474 | -60.0708 | 2026-01-16 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d018beb0-d9bd-3675-a991-dc68c18819a8 | 2.76856 | -60.32717 | 2026-01-16 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4370de6-e64b-3ba3-81c2-e77152e0ec03 | 2.76421 | -60.32789 | 2026-01-16 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d498fcca-855c-30da-9f2e-993d4fba05d9 | 2.75267 | -60.22995 | 2026-01-16 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0163e459-757a-3f95-bd57-1708cad137d2 | 2.70143 | -60.05613 | 2026-01-16 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d297e72-78fe-35ab-a7d5-c82f80784e95 | 2.69793 | -60.05531 | 2026-01-16 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d137f741-3204-300b-bb3e-a855fe4a4005 | 3.00207 | -60.23665 | 2026-01-16 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdc02440-1ea2-32c9-88c6-7f8dad00dd0d | 2.75481 | -60.32515 | 2026-01-16 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9e3b7cd8-3b3c-317e-b3e5-42afc991d3b0 | 2.76283 | -60.31949 | 2026-01-16 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 7bf9e112-d5ab-3802-a58f-fe03a2bdff7d | 2.75847 | -60.32021 | 2026-01-16 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 0add0161-d46b-30d9-9116-ff4702058b0d | 3.22723 | -61.19247 | 2026-01-16 05:54:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3bfda5a-8dad-3038-b938-9df6c6a845aa | 2.74757 | -60.22636 | 2026-01-16 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c4c0be19-6a04-3785-ab98-dc9443c6b137 | 2.75916 | -60.32441 | 2026-01-16 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| e372404e-5b81-36bf-9a78-89ea578a2b6c | 2.75779 | -60.31605 | 2026-01-16 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 12.9 |
| debff649-2f4b-304a-b17e-ca7ed886ed89 | 2.69557 | -60.06929 | 2026-01-16 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3597cdb8-00b9-3d43-b4cb-2e7585673856 | -16.10724 | -56.7589 | 2026-01-16 05:59:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4d8acbbb-65c3-3d09-bfe0-62c846c731c6 | -16.10078 | -56.75129 | 2026-01-16 05:59:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c77b9426-aa8d-34d0-b109-9b51eda71e2f | -15.5896 | -57.34108 | 2026-01-16 05:59:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c1cadb53-8da5-3d38-9c56-34cfd1957a1e | -16.10012 | -56.75819 | 2026-01-16 05:59:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d4beb2e-84ae-3bb8-a1d0-eac8acfcc3bd | -16.11131 | -56.75692 | 2026-01-16 05:59:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7319de1e-e591-3f44-bc01-d88c16d54392 | -16.11193 | -56.74995 | 2026-01-16 05:59:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ec572e3e-3d7e-351b-bf01-b5436137791a | -16.11503 | -56.75256 | 2026-01-16 05:59:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 04d611ae-0f4b-3e4e-9506-6a78db6f9734 | -16.10419 | -56.75624 | 2026-01-16 05:59:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 73a811a2-cf06-37bf-ac53-cb5e19d3c9de | 2.7633 | -60.334 | 2026-01-16 06:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 59583428-d1a9-375e-913b-73d2fde3bc3e | 2.7634 | -60.315 | 2026-01-16 06:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 970cb172-576a-3267-9a18-5288a7660206 | -20.43567 | -57.86576 | 2026-01-16 06:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| b3f6f732-9112-3747-9cea-fa235822913c | -20.43829 | -57.83113 | 2026-01-16 06:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 0a9fa40e-c3da-31be-9dfd-8b0380a4c473 | -20.42922 | -57.85815 | 2026-01-16 06:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 82629203-4bb0-3931-aa97-57122e42aa56 | -20.44474 | -57.83879 | 2026-01-16 06:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 5d2846e6-8348-32e5-a82d-0fe1d571ab97 | 2.7634 | -60.315 | 2026-01-16 06:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 73.1 |
| cf213da6-bd16-3815-ba61-52bb2c60cccf | 2.7633 | -60.334 | 2026-01-16 06:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 53.3 |
| a91a2011-eef8-3702-a445-05a224335ecd | 2.7634 | -60.315 | 2026-01-16 06:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 0b3673a0-bd48-39f2-822c-361a2105e3ae | 2.76902 | -60.32642 | 2026-01-16 06:22:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3ae7dcd8-ff3c-3422-91da-8602f6c81ab0 | 2.76237 | -60.32758 | 2026-01-16 06:22:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 484711e8-fa65-3f17-a46f-d1610f9c4a40 | 2.75728 | -60.32073 | 2026-01-16 06:22:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0e603b6a-44a8-325a-a6a4-08eef7b74a05 | 2.76297 | -60.31381 | 2026-01-16 06:22:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d73caab1-5dda-3ec3-9188-82acee0ad608 | 2.7483 | -60.22648 | 2026-01-16 06:22:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| db22cb57-8e87-38d6-9341-5a4f7aaa4311 | 2.75599 | -60.23128 | 2026-01-16 06:22:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c8bd01a-4905-32ec-aeb2-734692dfcef0 | 4.19105 | -60.58652 | 2026-01-16 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1188c239-56fd-396f-a3a2-bb1119997c0b | 2.75182 | -60.22796 | 2026-01-16 06:22:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0907ab87-dfbe-3b4e-b41c-c52829415f5f | 4.19676 | -60.57992 | 2026-01-16 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0158f7b9-afa7-3bb2-bd02-f3fc0f747bd0 | 4.19129 | -60.58625 | 2026-01-16 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f4de4f22-3a62-3034-a16f-6560abcb1098 | 2.75472 | -60.32301 | 2026-01-16 06:22:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a443af9b-757c-3b8a-8cdb-42fbd0a04435 | 2.76586 | -60.33105 | 2026-01-16 06:22:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| aac296eb-b4ca-395c-a5d9-57e2c773c192 | 2.76037 | -60.31613 | 2026-01-16 06:22:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 80281ffc-c1c2-38c5-b4a8-8b99d4b7bb30 | 3.81643 | -60.98331 | 2026-01-16 06:22:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2eedac85-e8fb-37ae-b20f-d126f1480ac4 | 2.7649 | -60.32529 | 2026-01-16 06:22:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5ff00a57-5ade-30d5-a49f-64ac275e8a07 | 2.75372 | -60.31731 | 2026-01-16 06:22:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d0cb8a9c-e346-3dd3-b6f9-a45988ef705e | 4.19035 | -60.58102 | 2026-01-16 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ba35c885-0db8-3a2d-b825-d56057a95435 | 4.19655 | -60.58014 | 2026-01-16 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 168f99b8-bdc7-3c5c-8f1a-be39103d7d43 | 2.76393 | -60.31952 | 2026-01-16 06:22:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a02ec3ba-c671-3f8e-8d9c-4c5fc9ac8b7e | 2.75499 | -60.22532 | 2026-01-16 06:22:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab3dd958-7f82-3a83-ba4e-492d015fa3e4 | 2.75632 | -60.31504 | 2026-01-16 06:22:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e0677ca5-7674-3a67-bbd5-ddc3fb2ce6d4 | 2.76136 | -60.32181 | 2026-01-16 06:22:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0886fc18-51c4-3183-a48e-19f6d488536a | 4.1977 | -60.58514 | 2026-01-16 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97502f25-7262-3674-8f2d-24c70e3535b8 | 4.19746 | -60.5854 | 2026-01-16 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6816b597-feb3-3955-ad96-060848e98c9c | 4.19014 | -60.58127 | 2026-01-16 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b8f798a8-7370-35e7-ad2f-0d1fa39acca3 | 3.81557 | -60.97849 | 2026-01-16 06:22:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4e15b98c-fe50-3c4a-888d-4b066568c439 | 2.7633 | -60.334 | 2026-01-16 06:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 54.9 |
| f0a0aa4a-5b4a-3f18-ac82-d534cfccbf0d | 2.7634 | -60.315 | 2026-01-16 06:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 24a5dbd1-966b-3517-9340-4c215c7845d6 | 4.19839 | -60.57904 | 2026-01-16 06:39:00 | AQUA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 17.9 |
| abff882e-ce55-3dfc-9297-8d7f61dae0b2 | 2.77225 | -60.31959 | 2026-01-16 06:39:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 5be7d7bd-403e-38e2-a766-4158854c6a2f | 2.7582 | -60.32156 | 2026-01-16 06:39:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 21e9ba4f-c05f-32df-b398-01a989c4e21b | -16.10757 | -56.74842 | 2026-01-16 06:44:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8e267c66-0bd3-3c15-9c1f-d5fedbd6aa41 | -15.43065 | -56.33216 | 2026-01-16 06:44:00 | AQUA_M-M | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 07ddf2d1-d5f7-36b6-b41d-406167bc5a40 | -16.10621 | -56.75751 | 2026-01-16 06:44:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2cff5044-833f-37e1-b033-07732bf234ff | -14.20423 | -57.40232 | 2026-01-16 06:44:00 | AQUA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 698a999d-2c6d-3667-adbb-2c31ba701065 | -15.432 | -56.32306 | 2026-01-16 06:44:00 | AQUA_M-M | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 9f08a016-a13b-31f4-94b6-48c15fbddccd | -20.43752 | -57.861 | 2026-01-16 06:46:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 3e7a3675-a9fb-307f-ade1-af2de1657373 | -18.81267 | -51.61425 | 2026-01-16 06:46:00 | AQUA_M-M | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 69dd8a11-ffcf-3e0a-85a7-2403bde6f73b | -20.44173 | -57.83299 | 2026-01-16 06:46:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 3cc4d55c-8790-3a27-96e9-9016f6c10233 | -18.8247 | -51.61592 | 2026-01-16 06:46:00 | AQUA_M-M | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 896d5ab9-0ac5-3eea-a20a-065ec78e1b10 | -18.82114 | -51.58527 | 2026-01-16 06:46:00 | AQUA_M-M | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| be8f81cd-b8c0-3e8a-9830-697570a651d6 | -18.81903 | -51.60379 | 2026-01-16 06:46:00 | AQUA_M-M | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 03a85e2f-3ada-3242-b71d-e50779c5fefe | -20.43292 | -57.83153 | 2026-01-16 06:46:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| c889ad2c-c944-3faf-b8c9-140c0c45a86c | -18.80699 | -51.60198 | 2026-01-16 06:46:00 | AQUA_M-M | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 19.3 |
| ee0a5dfb-40fc-3bc8-af8e-190c09a36c6f | -18.81489 | -51.59599 | 2026-01-16 06:46:00 | AQUA_M-M | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 94e77460-911c-3a72-a026-84f44e95e46e | -8.14821 | -35.37291 | 2026-01-16 11:34:00 | TERRA_M-M | POMBOS | PERNAMBUCO | Brasil | 2611309 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| a285a69f-520c-3476-b782-00ad5620e39c | -8.24405 | -37.60013 | 2026-01-16 11:34:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 5.1 |
| a7cb8bea-53cf-3dd0-af0e-7810d31740c1 | -7.00194 | -42.86342 | 2026-01-16 11:34:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 34.3 |
| ef2c9ada-0ddd-378a-8ce1-b23e9ff51c2f | -7.24741 | -43.06649 | 2026-01-16 11:34:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 26.9 |
| 165196f3-a7c6-3498-9f37-44e103b8fbc4 | -3.25052 | -41.81135 | 2026-01-16 11:34:00 | TERRA_M-M | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| c3c1341c-a4c6-3b17-9be1-6183a023fdf4 | -9.01419 | -41.024 | 2026-01-16 11:34:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 84a0c2de-c8be-3851-a63c-9a7b433fba68 | -7.58819 | -37.87367 | 2026-01-16 11:34:00 | TERRA_M-M | TAVARES | PARAÍBA | Brasil | 2516607 | 25 | 33 | nan | nan | nan | Caatinga | 8.4 |
| dcc51b55-ecb4-35a5-b4cd-c565e6c4c701 | -7.94937 | -37.46463 | 2026-01-16 11:34:00 | TERRA_M-M | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 54dd30dc-aa75-3261-bfd0-f1e24e07687a | -6.99138 | -42.86182 | 2026-01-16 11:34:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 25.0 |
| 37a07adf-b3fc-3df9-89d2-eeb995d0d52b | -4.58293 | -38.46125 | 2026-01-16 11:34:00 | TERRA_M-M | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 18.1 |
| d7e7b478-8840-365e-a7e4-8c94def5f7cf | -7.50475 | -38.91678 | 2026-01-16 11:34:00 | TERRA_M-M | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 5163c385-f501-3d30-b382-088991aac457 | -6.99996 | -42.87634 | 2026-01-16 11:34:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 24.4 |
| 32250fbd-5fd7-3f8d-a82c-420917a76759 | -6.9894 | -42.87469 | 2026-01-16 11:34:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 29.9 |
| ec2d6873-8b4e-3fa0-9a7e-d006c3bc905e | -3.24014 | -41.80989 | 2026-01-16 11:34:00 | TERRA_M-M | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 38.3 |
| cc306f2a-ffbd-3948-a194-bad293b2794e | -12.51344 | -39.08591 | 2026-01-16 11:36:00 | TERRA_M-M | CABACEIRAS DO PARAGUAÇU | BAHIA | Brasil | 2904852 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 0ee9153a-8024-328a-91c6-1ebf392c6e87 | -19.77871 | -42.15709 | 2026-01-16 11:38:00 | TERRA_M-M | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| e3766737-0f5f-3a51-a47f-0b5719eede54 | -19.37361 | -40.86997 | 2026-01-16 11:38:00 | TERRA_M-M | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| e1c8ba44-30c8-34c8-b8d1-556f034b2d7d | -20.45 | -57.8476 | 2026-01-16 11:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 191.1 |
| 1b248c52-34ab-39e5-ab8d-cafdfd6dd0d1 | -20.4504 | -57.8267 | 2026-01-16 11:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 130.5 |


[Clique aqui para ver as próximas entradas](README13.md)
