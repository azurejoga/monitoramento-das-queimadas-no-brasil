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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 226e5142-182d-37f4-aaf5-7d0cd7683f03 | 1.0212 | -51.1654 | 2024-10-21 00:05:00 | GOES-16 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 62545364-b99d-3195-a1c4-fb44e7d94d4c | -1.1834 | -53.6368 | 2024-10-21 00:05:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 5595f945-9c42-397f-8355-2dbd76c8cdcd | -1.2018 | -53.6366 | 2024-10-21 00:05:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| a03d45a7-78ef-3eb2-8f0c-5459e9888bb4 | -1.9211 | -52.1019 | 2024-10-21 00:05:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 8b162c8b-cf5b-333d-816a-f011b09ecf07 | -1.9395 | -52.1016 | 2024-10-21 00:05:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 584ec678-49bb-31dd-b222-93de09acf137 | -2.2199 | -50.4594 | 2024-10-21 00:05:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| b9dc76e5-aff0-3ab0-878f-5ff950b13f7e | -2.2671 | -47.0775 | 2024-10-21 00:05:19 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| d906c01c-d75b-33ce-b7b6-4638874bc71e | -2.4233 | -50.2871 | 2024-10-21 00:05:20 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| a425d9e7-2400-38ef-ae41-bbd3738cc506 | -2.4824 | -49.1233 | 2024-10-21 00:05:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 9e2250ee-c49c-3e1e-aac3-f79be9e7ece9 | -2.4824 | -49.102 | 2024-10-21 00:05:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 4858169d-f7a5-3e68-8f0e-abaff7ae4a61 | -2.5134 | -45.5868 | 2024-10-21 00:05:20 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 91d12cb7-c8f1-3363-9181-51be90a47c98 | -2.532 | -45.5862 | 2024-10-21 00:05:20 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 34.8 |
| c2f1d1fb-14df-3df7-bdd2-34d9ba490b99 | -2.7773 | -49.3067 | 2024-10-21 00:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| c696ed91-6cbd-3e7e-a4d1-573418633a04 | -2.7774 | -49.2854 | 2024-10-21 00:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| c5230097-b873-37dd-86c5-e09d2d5f5d38 | -2.7885 | -51.3618 | 2024-10-21 00:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| b026de4c-588b-3980-8fca-38162b7f5374 | -2.8069 | -51.3613 | 2024-10-21 00:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| efeb7417-ba6e-3a31-b404-a37ec2873670 | -2.8198 | -53.0019 | 2024-10-21 00:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 86d8b12d-a134-3ae0-afb4-9390d1c9a33e | -2.8481 | -45.4862 | 2024-10-21 00:05:22 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 56.9 |
| d5fa8e2f-e976-3872-a4d3-8a12fd803ef3 | -2.8482 | -45.4637 | 2024-10-21 00:05:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 75e14a28-7f55-3061-8c0b-3b76b3dcb605 | -2.8371 | -53.3463 | 2024-10-21 00:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 152f6e9d-6532-3155-9b9d-048432c03600 | -2.8372 | -53.3261 | 2024-10-21 00:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 10889d5a-d992-327f-aef6-c4a4ec96da42 | -2.8667 | -45.4855 | 2024-10-21 00:05:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 9bcfe8a4-8c69-3d9d-a0d0-b33eb8df13cd | -2.8668 | -45.4631 | 2024-10-21 00:05:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 293bbbe4-ef8d-3ab9-89ba-043e2f28d422 | -2.8864 | -45.215 | 2024-10-21 00:05:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 59.2 |
| de3e93e5-b580-309b-9a63-98e09a8c3709 | -2.8865 | -45.1924 | 2024-10-21 00:05:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 23b22cdd-7998-3ff6-9405-561c55d963b2 | -2.905 | -45.2143 | 2024-10-21 00:05:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 146.9 |
| a97a8050-d057-3be0-aa46-b19b552ea9d0 | -2.9051 | -45.1918 | 2024-10-21 00:05:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 106.4 |
| e2757ab4-4f66-30ee-a8dc-b3c70078aa2a | -2.9674 | -47.9931 | 2024-10-21 00:05:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 57cad90e-1a6e-3a39-922e-aa27c1fd144e | -2.9852 | -53.0587 | 2024-10-21 00:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| fe3e09de-bb20-3bb9-8c8b-4806a22be593 | -2.9853 | -53.0384 | 2024-10-21 00:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 5c2dfc57-6035-3f78-9612-8b60082d42ff | -3.0036 | -53.0583 | 2024-10-21 00:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 123.7 |
| bf669640-b16a-34e2-947e-8886903f65c1 | -3.0037 | -53.038 | 2024-10-21 00:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 127.8 |
| 4fb16444-0b84-368e-938b-a3b62777eccc | -3.0581 | -53.2395 | 2024-10-21 00:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 8b6efe3d-180d-3bce-9e11-3154bc70ed47 | -3.1137 | -53.1366 | 2024-10-21 00:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 368cad12-a6a4-3ae2-8e1b-2177e23277ef | -3.1138 | -53.1163 | 2024-10-21 00:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 95b93dc7-baa6-37bc-a60c-83f63d8484d8 | -3.1962 | -50.8099 | 2024-10-21 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 3bce6840-019e-346a-8396-6eeefa8dc4ec | -3.2146 | -50.8093 | 2024-10-21 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| cd92176c-7dc6-31f1-b6e5-aa0788645006 | -3.2147 | -50.7884 | 2024-10-21 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 24274975-d6dc-3100-9128-6b45f5ae8eb3 | -3.2585 | -53.78 | 2024-10-21 00:05:25 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| df386b1e-53a6-3e96-bc17-4528414414f2 | -4.0899 | -46.1493 | 2024-10-21 00:05:29 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 76.1 |
| deb70167-9f19-3c06-b7df-04070a472480 | -4.1085 | -46.1484 | 2024-10-21 00:05:29 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 70.6 |
| ca6388d7-f87d-35e7-a7e3-fb0d61ae903e | -4.4414 | -46.4425 | 2024-10-21 00:05:31 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 128.4 |
| 22905747-f57a-361c-a65a-8b0d8ce6c830 | -4.46 | -46.4416 | 2024-10-21 00:05:31 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 76.4 |
| b50c0677-06b8-3cf5-99f0-934fc7c83e08 | -4.6299 | -46.0768 | 2024-10-21 00:05:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 94796853-09c3-3b2c-a311-d12b5a305173 | -4.6301 | -46.0545 | 2024-10-21 00:05:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 63.3 |
| a6c205b2-e4d4-3a30-9c21-2bc14b38c0e1 | -4.8289 | -46.9078 | 2024-10-21 00:05:33 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 64.3 |
| d1032751-1e20-3d22-8479-b20b3ca8145b | -4.8291 | -46.8857 | 2024-10-21 00:05:33 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 129.4 |
| 3f039d3e-0be2-3b53-8805-3c3e7418d1de | -4.8477 | -46.8847 | 2024-10-21 00:05:33 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 64a8cbd3-651a-3e5c-9935-27c6210bd86c | -4.8924 | -45.8386 | 2024-10-21 00:05:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 5c16c4cf-31d5-35c1-8499-685136a8f2a1 | -4.911 | -45.8374 | 2024-10-21 00:05:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 93db6e03-3ec6-3e55-b14c-c56340396bad | -5.0098 | -47.6427 | 2024-10-21 00:05:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 0281a5c0-9e4a-39f6-8dd7-453efc29bb35 | -5.6707 | -46.4363 | 2024-10-21 00:05:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 8140e99a-51fa-3989-87eb-7c02f54b4438 | -5.6709 | -46.414 | 2024-10-21 00:05:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 451b4bc1-d165-38eb-bec7-b32a05ae5773 | -5.6894 | -46.435 | 2024-10-21 00:05:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 155.7 |
| 580fd237-e50f-381d-b706-369ba89768c5 | -5.6896 | -46.4128 | 2024-10-21 00:05:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 116.9 |
| a0d1da90-f2a6-3388-a041-e51567300804 | -5.7081 | -46.4338 | 2024-10-21 00:05:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| e08fea1a-f66a-3b17-8d75-2ba0cdfc98c1 | -9.3718 | -66.4891 | 2024-10-21 00:06:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 1b9e0dae-5cc5-3668-8049-1f4ac0740e7d | -12.4778 | -63.1885 | 2024-10-21 00:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 22bd453a-8112-3bce-a89a-60eb4379269d | -12.5147 | -63.3014 | 2024-10-21 00:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 764b9081-3309-3b35-96e3-1839fd492d22 | -18.263 | -56.1021 | 2024-10-21 00:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.5 |
| af34725b-3d0d-30c6-8b14-520e192e3c82 | -18.2828 | -56.0994 | 2024-10-21 00:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 154.7 |
| 0fc5ffc2-1d2a-3acf-836d-51668bc686f2 | -18.2832 | -56.0785 | 2024-10-21 00:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.3 |
| a49e55a8-7213-3b85-b972-224fde70b3ae | -18.3015 | -56.1595 | 2024-10-21 00:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.1 |
| b6261b7a-1301-325a-b5cc-d8d01cab2d3e | 1.0212 | -51.1654 | 2024-10-21 00:15:00 | GOES-16 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 65.0 |
| a00e57e3-fa7b-3694-b21b-dc6d23e6ab6d | 1.0028 | -51.1656 | 2024-10-21 00:15:00 | GOES-16 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 151a6d34-93e6-36aa-9117-f361be07bb68 | -1.1834 | -53.6368 | 2024-10-21 00:15:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 2774ab53-661c-392e-bd5b-3c9641b13c46 | -1.1835 | -53.6166 | 2024-10-21 00:15:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 065aecc0-c87b-33fe-b055-194f957cdd3a | -1.2018 | -53.6366 | 2024-10-21 00:15:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 1ded0067-6571-3055-a9af-f2edf938c020 | -1.9211 | -52.1019 | 2024-10-21 00:15:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| ce661bdf-d301-370c-a9dd-6860201fc9c0 | -1.9395 | -52.1016 | 2024-10-21 00:15:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 2dc6634d-b42a-3b6e-9774-98b729973b2c | -2.2199 | -50.4594 | 2024-10-21 00:15:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| fc56f811-b705-3b8f-91d8-731ef9d694e1 | -2.2671 | -47.0775 | 2024-10-21 00:15:19 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 3d8a9488-5028-3258-9938-647685a71da8 | -2.4233 | -50.2871 | 2024-10-21 00:15:20 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 28ad3bc1-0981-30df-b86c-4bb17eda9da6 | -2.4824 | -49.102 | 2024-10-21 00:15:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 9278eecd-1c19-3c98-9fe9-876ec7758aa4 | -2.7773 | -49.3067 | 2024-10-21 00:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| b1e0f128-db3c-3d1f-88d3-1abd4605564e | -2.7774 | -49.2854 | 2024-10-21 00:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| ad712fc1-67e7-3a53-a960-0cd18bebbdc7 | -2.7885 | -51.3618 | 2024-10-21 00:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 303a7368-dd93-3ee5-9d4f-75cea4db5c62 | -2.8097 | -45.7786 | 2024-10-21 00:15:22 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 41.6 |
| f5d840ba-a76b-3616-a7ca-1911941d6e85 | -2.8069 | -51.3613 | 2024-10-21 00:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 3d915570-167a-3e8d-900c-b81d3a163120 | -2.8198 | -53.0019 | 2024-10-21 00:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| aa0f5ab2-4360-38ec-b2c4-c36be163986a | -2.8481 | -45.4862 | 2024-10-21 00:15:22 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 51.2 |
| dcd0379b-015a-38bf-935f-078c15233a13 | -2.8482 | -45.4637 | 2024-10-21 00:15:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 6785107a-a751-31e9-8adf-7d06d628d929 | -2.8372 | -53.3261 | 2024-10-21 00:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 5c38a6be-0173-369e-bb0d-1c8f84050d4a | -2.8668 | -45.4631 | 2024-10-21 00:15:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 78.0 |
| d551e0c8-4fb6-3876-9ffa-cbccac2cc757 | -2.8556 | -53.3256 | 2024-10-21 00:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 80a7fe8d-35fe-3419-82fa-99600e31f07f | -2.8864 | -45.215 | 2024-10-21 00:15:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 4c003d56-f774-3134-a994-3a6a107d1dff | -2.8865 | -45.1924 | 2024-10-21 00:15:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 48.2 |
| cb8746c7-4330-3736-a07b-a3205cfa503d | -2.905 | -45.2143 | 2024-10-21 00:15:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 147.8 |
| 24474a24-6e0d-381a-ad22-2685849243aa | -2.9051 | -45.1918 | 2024-10-21 00:15:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 138.0 |
| f400d93b-71cf-3d77-8e56-93256c6bcdb5 | -2.9674 | -47.9931 | 2024-10-21 00:15:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 222754ee-547e-38ef-b215-0c11379a2a33 | -2.9852 | -53.0587 | 2024-10-21 00:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 12426558-6318-33da-aaa8-30e3f7f76787 | -2.9853 | -53.0384 | 2024-10-21 00:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| a916e019-62a5-3fb0-b380-37259a1719db | -3.0036 | -53.0583 | 2024-10-21 00:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 5a7fdf91-086b-3f65-8310-0da407986011 | -3.0037 | -53.038 | 2024-10-21 00:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 34cf12b0-6bea-38eb-807d-e4d2b6ad0b6b | -3.0176 | -54.3489 | 2024-10-21 00:15:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 296eaf9c-b97f-3467-98ca-fc79689a857a | -3.0581 | -53.2395 | 2024-10-21 00:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| b0c12fbe-55ed-35ca-a000-09b36e13f4d0 | -3.0765 | -53.239 | 2024-10-21 00:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 5328cc77-92ee-3e20-a5cd-98092f467896 | -3.1138 | -53.1163 | 2024-10-21 00:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 49b219c8-b032-3129-ad46-cfcad1a4a01a | -3.1962 | -50.8099 | 2024-10-21 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 78f6c44b-e95f-3652-9f6d-31eed6533e89 | -3.2146 | -50.8093 | 2024-10-21 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |


[Clique aqui para ver as próximas entradas](README2.md)
