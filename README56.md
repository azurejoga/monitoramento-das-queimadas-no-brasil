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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64f54498-bcd6-3603-948a-3489f11faa88 | -10.59331 | -44.28189 | 2024-10-27 05:06:00 | AQUA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2dc7bc0e-5b50-3917-ab2a-9871118f1741 | -10.56739 | -44.27121 | 2024-10-27 05:06:00 | AQUA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 7b3435a9-803e-3382-8849-dd91b1104857 | -10.566 | -44.28034 | 2024-10-27 05:06:00 | AQUA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 45f839dd-d264-3a14-b858-56143bd3fd14 | -10.55843 | -44.26985 | 2024-10-27 05:06:00 | AQUA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 014f966a-7d09-3d42-b635-b360f791d997 | -10.55704 | -44.27898 | 2024-10-27 05:06:00 | AQUA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| cd525522-5fd9-3926-8e02-bb9fca8eb0c1 | -10.53438 | -45.1395 | 2024-10-27 05:06:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| c72fc7bf-d0d5-32e6-bbe5-6664864afe5a | -10.53284 | -45.14928 | 2024-10-27 05:06:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 27fb3ef3-4a60-3265-9e73-0328214cca61 | -10.43952 | -44.56468 | 2024-10-27 05:06:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ac296188-04e9-36b5-8268-80cb54de9d79 | -10.43807 | -44.57401 | 2024-10-27 05:06:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 506c78ce-611f-3cf2-a81a-d901f526e012 | -10.36827 | -45.08092 | 2024-10-27 05:06:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 32.6 |
| c589648f-c7ac-3134-9b59-6c5edd9fa02a | -7.22805 | -46.04737 | 2024-10-27 05:06:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| dafc7a67-b05c-355f-8390-315777f13a1c | -6.87359 | -44.75584 | 2024-10-27 05:06:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 70995086-7e4d-32aa-bd6f-ab8afaa6ae31 | -6.8062 | -44.47312 | 2024-10-27 05:06:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f8570600-ec29-3c50-b877-ec7866de3cbd | -6.17585 | -45.42977 | 2024-10-27 05:06:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 65bd078e-d89d-34be-b5c4-90422eec59ab | -6.1741 | -45.44098 | 2024-10-27 05:06:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 0243c970-11b3-388e-95b1-260406c8fad6 | -5.80547 | -44.12454 | 2024-10-27 05:06:00 | AQUA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 5b44c68b-823a-33de-a357-ab4202add58e | -5.55001 | -46.98206 | 2024-10-27 05:06:00 | AQUA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 7539e89b-cc9f-3db1-b987-1e278fb53c95 | -5.54766 | -46.99671 | 2024-10-27 05:06:00 | AQUA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| d9edfa33-7127-350f-8872-e170e3e20484 | -5.5388 | -46.98026 | 2024-10-27 05:06:00 | AQUA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0ce96607-e55a-3bcd-bb24-ec93037e3c58 | -5.53822 | -46.98852 | 2024-10-27 05:06:00 | AQUA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 1fa81014-cd8c-397d-a8f5-5b1c0d7bd05d | -5.53641 | -46.99509 | 2024-10-27 05:06:00 | AQUA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| eb7b21c3-4df3-37ad-acda-451ee957d981 | -3.81178 | -48.88847 | 2024-10-27 05:06:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| c899ee44-cca4-3e6b-97f9-cbcc556685fc | -15.19936 | -43.52876 | 2024-10-27 05:08:00 | AQUA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 374aa360-52e8-3760-a743-5dcf1f038de7 | -14.27244 | -43.2507 | 2024-10-27 05:08:00 | AQUA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| d00af3ed-7856-3315-af03-c7434ea1d891 | -13.64807 | -44.11217 | 2024-10-27 05:08:00 | AQUA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fe4cdeb1-56de-374a-b006-d61d0472be93 | -12.89971 | -44.59753 | 2024-10-27 05:08:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 17c827ab-1bfa-3544-8538-f28fd309464d | -12.89831 | -44.6067 | 2024-10-27 05:08:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| d05fa4e5-2d1a-3a70-bbfe-aeb6691e5540 | -12.88939 | -44.60532 | 2024-10-27 05:08:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 53b299df-cbfd-348e-84d3-81283e01e01c | -12.87767 | -44.62226 | 2024-10-27 05:08:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 017c56c6-043c-32b8-8312-65be84935cb7 | -12.65025 | -44.23275 | 2024-10-27 05:08:00 | AQUA_M-M | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b98096f8-723a-393a-9027-fdd8703dbe94 | 2.58948 | -50.88906 | 2024-10-27 05:14:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c0a210e-e07e-302c-88bf-b2f09240b4f9 | 2.33102 | -50.77136 | 2024-10-27 05:14:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2781a1db-dfd6-3f50-bf14-459f6b89968c | 2.29825 | -50.77124 | 2024-10-27 05:14:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fb06df95-0a83-3461-acde-c2b1ddfa860c | 3.62833 | -51.29138 | 2024-10-27 05:14:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2ca48a9-b568-3148-9c6a-068fc008ff1d | 3.62772 | -51.28769 | 2024-10-27 05:14:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8ede27c7-851b-32fe-8be1-c36dbbb66217 | 3.62422 | -51.29205 | 2024-10-27 05:14:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c68826e-db74-3dc7-b6ab-4c13d91df620 | 3.62361 | -51.28836 | 2024-10-27 05:14:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8fcc50c8-0a40-39d4-8ac9-94ea430a43c3 | 3.60597 | -51.28368 | 2024-10-27 05:14:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd7c337b-7fc5-3463-8c5b-880abf0826c5 | 3.60285 | -51.28332 | 2024-10-27 05:14:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2ac74801-5736-3e2f-a7a6-37586a4d706e | 3.60186 | -51.28435 | 2024-10-27 05:14:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3c8d23ee-cc2b-3ffa-aab4-d2ab3a651b72 | 3.60124 | -51.28066 | 2024-10-27 05:14:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e3bff3e3-106f-3985-8081-5b57f4c3138b | 3.59874 | -51.284 | 2024-10-27 05:14:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c3d541e3-0c73-389d-bdd3-f43acef8b7d1 | 3.59815 | -51.2803 | 2024-10-27 05:14:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e9b036a6-9988-3ac6-a88f-fa651e54b818 | 3.59775 | -51.28503 | 2024-10-27 05:14:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 40feb432-c7df-3be7-8bef-4ac47d94751a | 3.59713 | -51.28133 | 2024-10-27 05:14:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 682a3f1a-d3ef-37fa-985a-5227a3d198c9 | 3.44146 | -51.27065 | 2024-10-27 05:14:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4dff8f46-5832-3a71-9b3b-142fc30e71f6 | 3.40329 | -51.29603 | 2024-10-27 05:14:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c2bd9b23-4a4a-3c0d-82a4-2beccff31873 | 3.39856 | -51.29299 | 2024-10-27 05:14:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ca3bcec-f2a1-3420-8f81-f47f80d7f5d8 | 3.39795 | -51.28928 | 2024-10-27 05:14:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2cc2a3cf-e5ca-3bbb-8be7-1040d711f05d | 3.39734 | -51.28557 | 2024-10-27 05:14:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 083eff7b-864f-3ea0-a9e9-f0dca01a15e4 | 3.39673 | -51.28186 | 2024-10-27 05:14:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8bab20ad-2412-35ba-8382-366fdea5819f | 3.39444 | -51.29367 | 2024-10-27 05:14:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 991ce9f7-32bb-369b-b90e-36569e5a76d0 | 3.39383 | -51.28996 | 2024-10-27 05:14:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5ca701f9-bc35-305d-bed4-a762271b10c5 | 3.38909 | -51.28692 | 2024-10-27 05:14:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 310a4943-a789-3ab6-917e-45b9ee46215b | 3.38848 | -51.28321 | 2024-10-27 05:14:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c89e3610-c7fe-3ccf-a92f-b90daad2f5d6 | 2.50925 | -51.08984 | 2024-10-27 05:14:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| babc4ee1-ecee-3fb6-a97b-5110a0ed2776 | 2.50861 | -51.08588 | 2024-10-27 05:14:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ac25b70-1db4-322d-8582-e7aa0ee6f865 | 3.93457 | -59.83865 | 2024-10-27 05:14:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3eb6e91-69af-3718-a749-99c4b9e718fc | 4.93543 | -60.26488 | 2024-10-27 05:14:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54f4b408-4b12-328c-b039-14f40aac1b52 | 4.93171 | -60.26559 | 2024-10-27 05:14:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4acdc002-baf7-39a4-b375-4b4d5771f9dd | -0.9815 | -53.699 | 2024-10-27 05:15:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| d3ade227-a84b-3301-aef2-3d40d3f427f0 | -0.9815 | -53.6789 | 2024-10-27 05:15:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 93a1792f-7041-357b-9bb6-69d14dd52cce | -0.9998 | -53.6989 | 2024-10-27 05:15:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| c5b55562-91b7-3ffa-a205-813fe0f3d0b4 | -2.5311 | -51.1816 | 2024-10-27 05:15:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 126.5 |
| ef56a229-a7e5-3d30-a5d4-ae6d71e876df | -2.5312 | -51.1609 | 2024-10-27 05:15:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| f40d6e51-6d1a-34c8-bcdf-62e2cccd1029 | -2.5495 | -51.1812 | 2024-10-27 05:15:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 8f273bc2-7666-3e9d-bc0b-94dadd1ae289 | -2.5496 | -51.1604 | 2024-10-27 05:15:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 2daccaee-6bd0-38eb-bc18-ecfd9ebc346d | -2.7034 | -49.3088 | 2024-10-27 05:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| ea5e7e87-2595-3c31-887c-ee1e438d9d5d | -2.8329 | -49.2626 | 2024-10-27 05:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 330f1183-17fd-3ed5-82c0-21032f666a08 | -2.833 | -49.2413 | 2024-10-27 05:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 114.9 |
| bdec8482-2550-3cee-86ac-b9fd23917864 | -2.8514 | -49.262 | 2024-10-27 05:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| d26a990c-da73-3f79-9e99-685c33f9d855 | -2.8515 | -49.2408 | 2024-10-27 05:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| f76516ea-bd71-396b-8fcd-6ee92d61b506 | -2.9161 | -51.751 | 2024-10-27 05:15:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| fb6d2c1c-fa45-35fe-95ea-502df3eb956f | -2.9345 | -51.7505 | 2024-10-27 05:15:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 0d2dc904-0aab-3d69-88ca-f1622efc1bd4 | -3.12613 | -45.26854 | 2024-10-27 05:16:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8d6ed5ca-19c2-3bab-9f40-373593f74fa6 | -3.12527 | -45.27464 | 2024-10-27 05:16:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9e81c285-a720-36ba-ab81-e644d7912c6e | -3.12401 | -45.26942 | 2024-10-27 05:16:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 673bfee0-3a56-3431-88e9-f62b44958596 | -3.12311 | -45.27553 | 2024-10-27 05:16:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| dba9b87f-bc64-3db9-b661-42bf17fd5070 | -3.11936 | -45.26748 | 2024-10-27 05:16:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 72f5fc6e-a21f-30d0-be6f-74ce08f8c527 | -3.1185 | -45.27359 | 2024-10-27 05:16:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 64459e05-79ca-3fa6-8f90-a44789e4ff99 | -3.11496 | -45.23671 | 2024-10-27 05:16:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8069f7c2-5d39-3e43-853e-36413017fb3b | -6.1833 | -45.43935 | 2024-10-27 05:16:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 717f36cb-6da0-3d51-8987-8f5d7f592a00 | -6.18264 | -45.43673 | 2024-10-27 05:16:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3c1f03f7-db23-32d6-bc3b-4beb81295dbb | -6.18179 | -45.44331 | 2024-10-27 05:16:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f2e37faa-a70e-3bb6-a675-8d3822d535cb | -6.17632 | -45.43833 | 2024-10-27 05:16:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b042af31-f97d-3f17-a8ba-e5b6c1d8641e | -6.17545 | -45.44478 | 2024-10-27 05:16:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 73118656-aa98-3676-a612-bc5dd7fc7ff1 | -6.17483 | -45.44213 | 2024-10-27 05:16:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5afa3c53-d8aa-3770-8b80-d8b148621e4d | -2.47436 | -45.84008 | 2024-10-27 05:16:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0db6f55a-ae2d-39ad-9053-b5c47b130852 | -2.47355 | -45.84554 | 2024-10-27 05:16:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| aca550f1-70d9-375a-bc3b-3d0af4205a64 | -3.598 | -47.27729 | 2024-10-27 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6f278a20-69d5-3df0-a0b1-8f86ef249592 | -3.59448 | -47.27316 | 2024-10-27 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fc0b5811-498e-3d1b-a487-91b7aea948eb | -3.59387 | -47.27744 | 2024-10-27 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd1f9f40-08ab-30f8-a4d0-ed7f06be77a4 | -3.59255 | -47.27243 | 2024-10-27 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40502923-0d2f-3e07-b370-d1e6af21046d | -1.96856 | -48.68922 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12de6554-6ab4-3676-a233-16fabe710408 | -1.96804 | -48.69258 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf124c49-50d6-3385-82fd-b9d8d4ac58bb | -3.46244 | -47.66326 | 2024-10-27 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 254bdf82-02c5-3db6-a0cc-aacb5392de85 | -3.46183 | -47.6675 | 2024-10-27 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19f8c5d4-51c4-3081-a2de-d709374ec72f | -2.49558 | -48.04782 | 2024-10-27 05:16:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bbbf02d9-6c8e-3ee4-acb8-3d9d6f52b601 | -2.495 | -48.05165 | 2024-10-27 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1883c5ce-630c-3721-84f0-4551553c9e13 | -2.49442 | -48.05547 | 2024-10-27 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |


[Clique aqui para ver as próximas entradas](README57.md)
