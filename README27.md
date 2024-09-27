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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1b80010-2625-3b4f-9415-6f19393ea34c | -7.18905 | -55.02673 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 61b02d39-c359-300a-b9d8-d573ffc27dca | -7.18782 | -55.01787 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c8f81ddf-0eff-32ca-b6f2-09d61e4b09fb | -7.18268 | -55.04571 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 41a1a87c-1624-359a-9bc4-029cebe68691 | -7.18145 | -55.03685 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 00179173-b5f2-3065-9ed7-4e9afa8dcce6 | -7.18021 | -55.028 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| a5ce3a1c-c0cf-34ad-8149-a70e83832e3a | -7.17898 | -55.01914 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4a7b0fe7-cd2f-39f5-ac5d-bb5dbe461227 | -7.17384 | -55.04698 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ee9d26f7-9e15-3d15-81bf-24e8cd8fb5e2 | -7.17261 | -55.03812 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 72a9f40d-a37a-37a6-a067-bb7538119c82 | -7.14865 | -55.07493 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b6bcdc12-a5ed-3c39-a6be-5c7448317450 | -8.40967 | -55.06235 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3e235d25-79da-31a7-9ffa-d3d74d00f733 | -8.40844 | -55.05345 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6a8ba8fb-84a2-3437-a306-5b699eaa34e3 | -8.40472 | -55.02674 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 251de7b8-6040-3f95-a18b-e60f21bb3274 | -8.3578 | -55.07887 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| d8fc0ae0-dbd7-3fca-a9e3-88e7e4b771f9 | -8.3541 | -55.05216 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2b7ded87-0fa1-356b-a5e3-172f385a907c | -8.34676 | -55.07722 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 228a7c40-010f-3771-b174-4561e2e05c0b | -8.34552 | -55.06833 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| a146b2de-e71b-31cb-a0fc-7055f222d0c8 | -8.32164 | -55.02639 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 5a308de5-cbc4-3447-8c09-a1245bc11289 | -8.3204 | -55.01749 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b49d5772-6c21-3c6b-bf0e-093f8137ff29 | -8.31916 | -55.0086 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| ad42a804-955f-32a5-930e-3e64806ced01 | -8.31793 | -54.99971 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 857d3557-5c05-3b86-85c5-4325ce5ec1b5 | -8.30908 | -55.00098 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| ed474593-90b1-3149-9867-cfcbb7740e6b | -8.74991 | -54.98906 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| cac73e33-f338-3f13-8de3-0b53fca39047 | -8.74868 | -54.98015 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| aa7186d9-c66a-30d1-99f6-52a205aee439 | -8.70205 | -55.04726 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7d0e9bb2-82a5-3fdc-9cb1-0767e307e1db | -8.52021 | -55.1947 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 59e07353-1a27-3903-a0dc-bec740344d0a | -8.51897 | -55.18576 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 3f56c7ef-b0c3-3b5d-a52c-13bff66c4f52 | -8.50125 | -55.1883 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5afdc0d3-d391-3d5c-a6a2-5f9afa5f93b5 | -8.40596 | -55.03564 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| fea893f2-db23-3e94-99c7-d3ea89495933 | -8.38475 | -54.94798 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8f07c738-4ce1-3b8b-988a-bc6d8df0610f | -8.38352 | -54.93909 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 338af3d2-472d-3dfb-b1f6-b6fc49b74cd3 | -8.31032 | -55.00987 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| ebdfd1a0-4a6a-3cc8-a083-4c4156f68876 | -8.12012 | -55.35823 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c1733c86-e5dd-300e-8195-4442c0e1375e | -8.11734 | -55.0769 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 0bfe10c6-9b00-3567-814d-f8e8ed4c3290 | -8.11561 | -54.8054 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 838ae4ea-95de-3b4c-99af-44dffb5c34b8 | -8.11437 | -54.79652 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f733960d-52fb-3689-a50d-f4340551c322 | -8.11314 | -54.78764 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d9e7b72c-2858-3009-afc0-64e218b11477 | -8.10973 | -55.08705 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4c90d913-92a8-3f05-8de9-fe09ebec8127 | -8.10849 | -55.07816 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 45b87cfa-a1e2-321d-998b-2ff503830d09 | -8.10726 | -55.06928 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 62b1d10f-a9fd-32e3-bb80-a962e2654348 | -8.1053 | -55.39402 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ec2d60da-82aa-3f0b-b2f3-00acd411953b | -8.09642 | -55.39528 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e75fc786-6e98-3735-b3af-9a721a456417 | -8.01101 | -55.70648 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 37e48211-6912-380a-bb79-96914975c929 | -7.93661 | -55.76952 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 832f27ac-b09f-35ec-9ef5-63ec1db93fc4 | -8.3233 | -56.51146 | 2024-09-27 01:24:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 215d3188-1852-39ec-9d5e-9fdf618d6a5a | -7.93536 | -55.76044 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 53174e74-d880-3097-82a6-52594ab54460 | -10.82218 | -53.7377 | 2024-09-27 01:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3d049553-07df-3d2b-9327-1940818193bf | -6.09531 | -44.69425 | 2024-09-27 01:24:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 39fb8c1f-5dff-3de5-acca-7eb178772931 | -7.25126 | -44.96296 | 2024-09-27 01:24:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 4c8534f2-a334-3a67-83f2-0286f69e99b2 | -7.25414 | -44.95541 | 2024-09-27 01:24:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| dbf55715-a8eb-361a-8c9f-e5ccbc1f1138 | -10.65702 | -45.90464 | 2024-09-27 01:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 54862719-e4c7-368d-bf6a-7a4158de6b55 | -10.65336 | -45.88174 | 2024-09-27 01:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 49fba9fb-0690-3744-b6a3-59561703b648 | -10.65216 | -45.87629 | 2024-09-27 01:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 16639e25-7148-399c-aae8-9f024ccd5f7c | -10.64857 | -45.85251 | 2024-09-27 01:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 32.4 |
| afa5293b-94d8-300d-ad02-fefab7dc7176 | -10.63761 | -45.97135 | 2024-09-27 01:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| a45a7c97-aedc-3e6b-a67c-416ff1f75145 | -12.24179 | -45.50578 | 2024-09-27 01:24:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 25.3 |
| c00cd59c-4e6f-3d58-85ff-e63f14f2a77f | -11.27547 | -46.12327 | 2024-09-27 01:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |
| bd327418-0b06-3db6-abcb-59e947f4d407 | -4.61019 | -45.77771 | 2024-09-27 01:24:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 0609ae6a-0b45-3823-851c-2671f8cb96e2 | -5.23351 | -45.43581 | 2024-09-27 01:24:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 3b111a2b-996d-3f97-94c5-06d27fa11514 | -7.27325 | -46.60723 | 2024-09-27 01:24:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 35017fb1-28c2-353f-a1be-6858fea2cf13 | -7.09706 | -46.46517 | 2024-09-27 01:24:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| f2e46c76-1236-3c88-bd7a-658a0654ec20 | -7.09239 | -46.43632 | 2024-09-27 01:24:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| c54db5e5-a734-3ec2-b308-19cf43ab245c | -9.54879 | -46.31858 | 2024-09-27 01:24:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 025290a1-3fba-3c7d-ad9e-1e6849317931 | -11.09929 | -46.16743 | 2024-09-27 01:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 76ea8b3a-9cdb-3f9b-97cd-f944ae8fa428 | -12.18216 | -46.75767 | 2024-09-27 01:24:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 66afe61a-cf21-3969-82dc-875db9ca4a13 | -3.21859 | -46.80653 | 2024-09-27 01:24:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| c93478ba-9827-3a17-8f72-9a8bb2b3309a | -3.21361 | -46.7739 | 2024-09-27 01:24:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 788ad0fe-6d24-3b33-b968-c8214643f3e6 | -4.48814 | -46.32196 | 2024-09-27 01:24:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 188f2cae-904c-313e-8fea-7010a62f5bdd | -4.47947 | -46.31774 | 2024-09-27 01:24:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 9f0135d4-45c4-3e57-b6cb-07c454bbaa73 | -4.14139 | -46.69561 | 2024-09-27 01:24:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 23.9 |
| d2c2c9fc-8754-3c4b-a9a6-e9acd6b1d119 | -3.91811 | -46.4435 | 2024-09-27 01:24:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 35.2 |
| a1fa0a16-61f0-3b5f-b25b-4e5b76bfde6e | -3.9105 | -46.4498 | 2024-09-27 01:24:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 4e8e7b7b-9b50-3551-a476-086962a9a0b8 | -4.13197 | -46.70288 | 2024-09-27 01:24:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 10a66fa8-8ef4-34c1-9d98-f84ed4e7afc2 | -9.88282 | -47.47849 | 2024-09-27 01:24:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 35bb949f-9afb-3966-aaaf-f8f3a4f6e90f | -10.53334 | -48.06927 | 2024-09-27 01:24:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 402e253a-0347-380a-ae6d-54bde8c87d12 | -11.52023 | -47.83199 | 2024-09-27 01:24:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| f801294b-102f-3aba-b207-d752c4e51004 | -11.51964 | -47.83762 | 2024-09-27 01:24:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| b3d7f573-6650-38c9-9b9f-5b9337d04c9f | -12.46501 | -47.97135 | 2024-09-27 01:24:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 6a4e718f-6612-3875-a9a3-20b6d656e3a1 | -4.63036 | -48.53513 | 2024-09-27 01:24:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 89983aeb-d060-3f5d-920c-be0f9eebffe4 | -4.56034 | -47.99508 | 2024-09-27 01:24:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 535f247e-4c5e-3c4d-886d-b04e0e8c2491 | -4.56023 | -48.0255 | 2024-09-27 01:24:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 237219ff-ecc3-39a2-aa40-1dae92008312 | -4.55661 | -48.00111 | 2024-09-27 01:24:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 8fd08535-d5de-35aa-9f52-63cb4d62e7eb | -4.18924 | -48.6161 | 2024-09-27 01:24:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| ac0ce488-8f19-3b2e-b290-041e2d2f48f3 | -4.1867 | -48.63272 | 2024-09-27 01:24:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 90652032-fbf1-3cd2-a5db-3e2e67cae179 | -4.63631 | -48.53961 | 2024-09-27 01:24:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 73996a8a-9c28-34af-97ed-30ecab674196 | -4.56415 | -48.01956 | 2024-09-27 01:24:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 9dce6dfa-5e5b-3c79-9205-854b431de50b | -4.20019 | -48.63049 | 2024-09-27 01:24:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| b543fe0a-481a-3c9d-bd18-e3079ec4fc6b | -4.19245 | -48.63802 | 2024-09-27 01:24:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 1797933b-f87c-3837-9181-90ccb9ceb870 | -5.87756 | -48.11398 | 2024-09-27 01:24:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 29.2 |
| bb7f32dd-de2f-349c-b893-009be1b15002 | -5.87389 | -48.0906 | 2024-09-27 01:24:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 15d1b52f-5da7-32d9-876d-723493509d60 | -5.8675 | -48.09727 | 2024-09-27 01:24:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 32ef5898-0936-353c-b6f7-8be229b3590d | -5.62181 | -49.089 | 2024-09-27 01:24:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 1236e37e-7907-3a6a-b729-8babcecfc46b | -5.25102 | -48.88646 | 2024-09-27 01:24:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 765df193-8709-3d5a-b055-121b5fbc16f5 | -5.62471 | -49.10838 | 2024-09-27 01:24:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 5b8d9775-8bc6-37f8-9073-8b7354a8b0fa | -5.62465 | -49.10271 | 2024-09-27 01:24:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 88a964c8-1b2d-3045-b15c-0b3a9753f10f | -5.23651 | -48.53778 | 2024-09-27 01:24:00 | TERRA_M-M | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 230298ed-f882-3fa1-98fa-59c594f604e4 | -8.57016 | -49.60502 | 2024-09-27 01:24:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| fefcb03b-d4a2-3824-9202-0b39a5571c84 | -8.55956 | -49.59704 | 2024-09-27 01:24:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| b1f47908-ad1e-332e-895c-9149af90bf2d | -8.08828 | -49.52161 | 2024-09-27 01:24:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 0fa17ef8-494b-3a3e-bbe7-4098f992af47 | -7.89713 | -50.01327 | 2024-09-27 01:24:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 23e556d1-9318-3c0d-b700-69edaa804331 | -8.78565 | -49.65408 | 2024-09-27 01:24:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |


[Clique aqui para ver as próximas entradas](README28.md)
