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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90cbdf26-7122-37d2-a5ee-c981a5c0d551 | -10.07839 | -50.81519 | 2024-11-07 05:12:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa5f70b7-8258-3580-85c5-2cbb64975554 | -6.07626 | -44.7226 | 2024-11-07 05:12:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9f246d8f-5009-3ce1-aa3b-abaad10c8d5c | -10.01198 | -48.83777 | 2024-11-07 05:12:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7e6d069a-bde3-396e-8609-cd9ac50f9e0d | -6.53933 | -44.46385 | 2024-11-07 05:12:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 087b812d-0e17-376f-8ce1-2b3acc60d557 | -4.99707 | -49.89366 | 2024-11-07 05:12:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 84518fbb-6d6f-33c3-92e4-c60ee6e2565b | -6.04687 | -46.60387 | 2024-11-07 05:12:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7fff7da6-6f9a-359b-b779-ec82a1acf3b4 | -6.50095 | -44.68557 | 2024-11-07 05:12:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f8bf193-9cbd-322a-8dfa-a505ef1c4597 | -5.98627 | -45.36055 | 2024-11-07 05:12:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| ac905189-f6e7-3086-80e1-eb9a15532d1c | -6.08366 | -44.71806 | 2024-11-07 05:12:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 34437c60-327c-3e1c-857d-9cf135e43c5f | -5.97078 | -45.3669 | 2024-11-07 05:12:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 45e4f21f-2504-3f89-bb86-f72adc4e1058 | -9.91806 | -48.56937 | 2024-11-07 05:12:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3be4f07b-16cf-30e2-ac1f-e2ed5389c495 | -10.73028 | -49.82917 | 2024-11-07 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 764125dc-d86f-3c34-a497-f717d12199df | -9.2606 | -50.69039 | 2024-11-07 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 68ee8adf-3b4e-30d9-b3a2-9b90bfd14f5f | -7.0407 | -47.62664 | 2024-11-07 05:12:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59e05737-b29d-3c6f-bfdc-9914aec388f1 | -3.92713 | -56.10862 | 2024-11-07 05:12:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7566617b-bd45-3f02-b07c-c2f4aae0ad81 | -5.97714 | -45.36817 | 2024-11-07 05:12:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fedccb66-1f11-3060-aa35-b916ce8c34e6 | -10.02679 | -44.72582 | 2024-11-07 05:12:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 33b5d472-44b5-3c42-b746-8bd566aee1ad | -5.97846 | -45.37024 | 2024-11-07 05:12:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 1e80a274-5a72-309c-9dd8-9656f2f0be35 | -6.48662 | -44.69019 | 2024-11-07 05:12:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7122f6d7-5e8f-3599-858e-8e0bb1183acc | -9.91762 | -48.57296 | 2024-11-07 05:12:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 74441bcb-983f-3f58-84be-2b9a1ab8e2a9 | -5.37745 | -46.26421 | 2024-11-07 05:12:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b35cd74e-b777-3571-afc0-73617a0bfcc9 | -6.48317 | -44.68781 | 2024-11-07 05:12:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 495dc9cb-3496-3117-bd21-cd588a7a01d0 | -6.53836 | -44.4594 | 2024-11-07 05:12:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 11a2e2be-f260-3f2d-a390-50d15847e591 | -5.70341 | -45.9416 | 2024-11-07 05:12:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c5393b7-f9dd-358f-bf5f-b03b9a910e6c | -6.50169 | -44.68009 | 2024-11-07 05:12:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aaeb1b43-ab5a-339f-afb7-423dab3c6844 | -10.03381 | -44.72666 | 2024-11-07 05:12:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 52a85632-072d-303b-8155-c66c8fb9bb46 | -8.38838 | -49.63771 | 2024-11-07 05:12:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6a14005-7e0b-3157-aefe-34f6d4088ce4 | -5.37204 | -46.25895 | 2024-11-07 05:12:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aa2a09c5-38b8-37d0-9222-93a5756ac22f | -5.62053 | -43.94898 | 2024-11-07 05:12:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| da656d46-6ed7-3062-b316-48f8f1aee83b | -5.61967 | -43.9557 | 2024-11-07 05:12:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 73f77f0c-ecab-38b3-9551-7ea011cd26b1 | -10.45545 | -44.89474 | 2024-11-07 05:12:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4c2888a9-fb58-322c-bf61-54fce09cbf04 | -5.53193 | -48.69691 | 2024-11-07 05:12:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d811ab60-ba5e-3bdc-b33d-f478d4742b2d | -6.08009 | -44.71626 | 2024-11-07 05:12:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8254c2ce-db65-3458-9beb-51bb05a99b51 | -5.45243 | -45.52956 | 2024-11-07 05:12:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| efc7ab0f-5988-35bc-b858-37572715dbaa | -10.02447 | -44.74586 | 2024-11-07 05:12:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ccc5cfea-761b-3259-a11c-ada3bbd7f6be | -5.5362 | -48.70393 | 2024-11-07 05:12:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eaee1277-af04-3624-bbfa-461f5badd121 | -6.48741 | -44.6843 | 2024-11-07 05:12:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b6470cdf-6e7f-39cb-a3b1-22a232994dac | -15.20437 | -60.35844 | 2024-11-07 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92675fdc-b571-3493-ba23-8274b2fc3bb6 | -16.93721 | -57.65633 | 2024-11-07 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 1a1becea-dc76-33ea-8197-1b8c99e617c6 | -16.94124 | -57.65293 | 2024-11-07 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3986ba5f-e221-3d5e-9da9-f8c7d7300898 | -16.94067 | -57.65686 | 2024-11-07 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 542899bf-09aa-3d79-9ab7-8244e1168af9 | -16.94469 | -57.65347 | 2024-11-07 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5e96eda2-c339-3009-aec9-f5f5da70f61a | -20.60135 | -55.90259 | 2024-11-07 05:16:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a5f775bd-a12b-343d-9b98-dc77e2f386e0 | -20.60135 | -55.89927 | 2024-11-07 05:16:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f3d837b4-dac3-392a-b814-c31ff8cc33d3 | -20.64141 | -55.86725 | 2024-11-07 05:16:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56c721e9-0574-3c3d-831a-f6b2967fa238 | -19.19079 | -57.83993 | 2024-11-07 05:16:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7c2b0ba3-e72c-3368-aea6-d873af09c021 | -21.56632 | -57.35457 | 2024-11-07 05:16:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc4e876f-c775-342a-bbc1-935eabab0140 | -20.60528 | -55.89986 | 2024-11-07 05:16:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9fe0df9-2901-31cc-b271-9d34fc189bbc | -19.57836 | -54.88937 | 2024-11-07 05:16:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 05b7bdbb-8202-38c8-ba16-2ab6403e3d36 | -2.2845 | -53.8224 | 2024-11-07 05:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 39f00617-cd3d-3dea-a616-44767c62429f | -2.6228 | -51.3038 | 2024-11-07 05:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 989bdf86-6c48-3838-8523-c7de795e8663 | -5.9975 | -45.3607 | 2024-11-07 05:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 3c2f3d91-af41-3cbf-9288-0343929aab87 | -2.82 | -52.9409 | 2024-11-07 05:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| cc48a92f-c639-3cfb-b357-cd65ac06b75c | -1.1466 | -53.7177 | 2024-11-07 05:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 13f891ce-7795-37ca-bad9-1ba8aca14556 | -3.6048 | -50.2521 | 2024-11-07 05:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 25fb77a3-3847-3406-b943-8ed947abf8ae | -3.5864 | -50.2317 | 2024-11-07 05:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 133.4 |
| 1c083b41-b4b4-3a98-bc1e-c2d150d9762e | -2.82 | -52.9613 | 2024-11-07 05:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 5c122e21-5b11-348d-abc2-588fd0b84b06 | -2.2845 | -53.8023 | 2024-11-07 05:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 62757233-0448-3c4b-bd92-9bcb96eff177 | -3.6049 | -50.2311 | 2024-11-07 05:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 33bb2b90-2723-3d8a-800d-e6090e6a9e27 | -2.8536 | -48.6856 | 2024-11-07 05:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| b183e62b-4ca8-3aee-9bae-3c7a27c18d7f | -3.5863 | -50.2527 | 2024-11-07 05:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 7dd78f65-fcad-33b0-b3d9-3b9959263ce5 | -2.6645 | -49.8814 | 2024-11-07 05:20:00 | GOES-16 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 722f5d5e-d614-32e9-ac12-9c9aeac12a9f | -5.9788 | -45.3621 | 2024-11-07 05:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 41581b4f-b288-3c22-a4b4-1e75a3a717a9 | -2.82 | -52.9409 | 2024-11-07 05:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| ba27b6bb-5059-3058-bbf9-853c3f3ddabc | -5.9975 | -45.3607 | 2024-11-07 05:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 1b8f666a-43c8-3fb6-8a54-eff8c818c8f7 | -3.6602 | -50.2501 | 2024-11-07 05:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 23ad6c13-e44b-3dc2-a677-0ee2f0dafbde | -3.7033 | -48.9986 | 2024-11-07 05:30:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 2052e339-865a-3fcc-ad42-524d0c748ea3 | -3.5863 | -50.2527 | 2024-11-07 05:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| d5f96b42-fe82-3a1c-b4f0-ed91532f5e24 | -2.2845 | -53.8023 | 2024-11-07 05:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| dda8eeab-73bc-3291-9b42-896ffde127dc | -2.82 | -52.9613 | 2024-11-07 05:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 5fd52396-14d5-3d82-92a6-795e6d75fd01 | -2.6645 | -49.8814 | 2024-11-07 05:30:00 | GOES-16 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| ed1d61b5-2855-38ee-b65f-66c16ffa4ada | -2.8537 | -48.6642 | 2024-11-07 05:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| d48fead7-eebb-377a-94c4-eb0c30e76733 | -5.9788 | -45.3621 | 2024-11-07 05:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 164.1 |
| 3c18d2f1-8c7b-32bc-8f37-b0970f0af76b | -2.6228 | -51.3038 | 2024-11-07 05:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 77dd8c1c-f0e2-3102-a54e-8c20156001c8 | -3.6049 | -50.2311 | 2024-11-07 05:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| a0915e29-f1ed-3102-b52f-76f560a1e2be | -3.5864 | -50.2317 | 2024-11-07 05:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 178.3 |
| b9de91be-9c9b-397d-91e7-659172f41415 | -2.2845 | -53.8224 | 2024-11-07 05:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| dcd96ac0-7b2c-3b60-a68a-96948b9f0913 | -2.8536 | -48.6856 | 2024-11-07 05:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| ed982953-7355-3f40-9e18-81cbe0db8267 | -3.6049 | -50.2311 | 2024-11-07 05:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 552abeab-41fe-3c6b-b90a-6ef1bc0b2d07 | -2.2845 | -53.8023 | 2024-11-07 05:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 7f91c223-e093-3ed7-a676-1ed922828daa | -3.6602 | -50.2501 | 2024-11-07 05:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| b91f2307-f996-39c6-9d33-d0259dd0be0b | -2.8537 | -48.6642 | 2024-11-07 05:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 2519d6fd-31ee-34f1-a5bb-2928c2f227ef | -2.82 | -52.9409 | 2024-11-07 05:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 00811f9e-7c70-37aa-9828-35c2fa4071f3 | -3.5865 | -50.2107 | 2024-11-07 05:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 0032922e-e754-3633-aea4-04fa0963037f | -2.6645 | -49.8814 | 2024-11-07 05:40:00 | GOES-16 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| d17cbd43-9ccd-3d87-82f1-a9ce90916cc1 | -3.5864 | -50.2317 | 2024-11-07 05:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 163.9 |
| 08ba2e18-8fda-3355-b0ce-8e4ee849f065 | -5.9788 | -45.3621 | 2024-11-07 05:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 5f78f001-2423-3edd-b1c8-6e35f5e92900 | -2.2845 | -53.8224 | 2024-11-07 05:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 209df50c-02e6-34eb-b06a-0858f92b1cbf | -5.9975 | -45.3607 | 2024-11-07 05:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 635895ef-fa88-323a-af66-ccebe89a9973 | -2.8536 | -48.6856 | 2024-11-07 05:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 63c69c86-e5d8-36be-a803-c9e6bbf8a77c | -3.5863 | -50.2527 | 2024-11-07 05:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 1eab1a24-0e24-3d5f-8bf8-cae7d6b5a874 | -3.6049 | -50.2311 | 2024-11-07 05:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 127.9 |
| b627ba67-556c-3e65-83da-4d3039039eff | -4.8767 | -42.9554 | 2024-11-07 05:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 39723f35-d9fe-371c-bad0-acfe04a777e4 | -2.82 | -52.9409 | 2024-11-07 05:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 07cbb4ca-94c1-3961-beef-cade5dfcc2f5 | -3.605 | -50.21 | 2024-11-07 05:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 7115f0a7-2a70-36b8-a200-7f974a8296d0 | -2.8536 | -48.6856 | 2024-11-07 05:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 4f05f612-fe84-3d31-8fe8-f5970c514625 | -3.5865 | -50.2107 | 2024-11-07 05:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| cc37c2da-e904-320e-8c93-347f59b75800 | -2.2845 | -53.8023 | 2024-11-07 05:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 8814d14d-1666-30b7-b9f6-aa7037734adc | -3.6048 | -50.2521 | 2024-11-07 05:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 97054ebc-6eca-31e7-9152-3e3ea5332a3a | -3.5864 | -50.2317 | 2024-11-07 05:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 161.4 |


[Clique aqui para ver as próximas entradas](README53.md)
