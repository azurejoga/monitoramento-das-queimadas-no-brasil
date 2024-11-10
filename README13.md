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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50b52709-745c-3ed0-8873-3de47e7fda83 | -1.22918 | -54.18107 | 2024-11-10 01:19:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 101f1c9a-5c05-3d16-804d-156226e390d7 | -2.19969 | -47.73249 | 2024-11-10 01:19:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| b177c0e4-149e-300c-91f2-acf09911935f | -3.95955 | -48.99662 | 2024-11-10 01:19:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 64350595-e5be-34df-a65e-f3e08c98d2a2 | -3.22408 | -50.29926 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 3e69ea95-7858-3ce4-bc7b-cd232a031c88 | -2.85908 | -50.31767 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 4ece366e-a9b5-3031-9474-8dff7524568a | -3.69596 | -54.62017 | 2024-11-10 01:19:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 44546731-7ec4-33af-b46b-6809610bb11c | -2.71271 | -49.29221 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 3fe07fa5-43f7-3518-a64a-ddc2056aac8b | -1.62781 | -52.23822 | 2024-11-10 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 778ffe69-aa34-3cb8-90f8-a4dd628996ea | -3.59415 | -47.35264 | 2024-11-10 01:19:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 329.8 |
| 61ac24c1-db8b-3355-8bb2-2375d093d598 | -2.9485 | -54.67595 | 2024-11-10 01:19:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 08d19faa-1804-3ad7-b509-e9af413cc308 | -1.64316 | -54.43884 | 2024-11-10 01:19:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3f428bac-a905-31eb-91e1-10563d81b703 | -1.24588 | -51.77108 | 2024-11-10 01:19:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 8918effe-67da-3743-a85f-38deeea1b5c8 | -3.08231 | -49.5624 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| c01ae836-9c99-3f80-8ccc-997067bba23e | -2.31245 | -50.6679 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| ec9a0aaf-f3ce-3db2-bbf0-d081d5fe9f10 | -2.87615 | -53.96684 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2e7fb7bd-1a1c-3d5d-b38d-15741240307f | -2.41835 | -53.65893 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 398e4f1b-5c82-3892-bb50-aee40047ee04 | -1.3459 | -54.6244 | 2024-11-10 01:19:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| d792e406-133b-34d7-848c-d9bc0f14f7e8 | -2.64828 | -49.39658 | 2024-11-10 01:19:00 | TERRA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 6558010f-bbd8-370c-a05d-705522117f59 | -2.62408 | -46.77932 | 2024-11-10 01:19:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 628aef28-9ad3-31da-9450-c67984632427 | -2.19554 | -50.8245 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 1e002a79-b9be-32b5-8f15-d35bab1411de | -3.25475 | -51.00876 | 2024-11-10 01:19:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 8b990671-e923-39a3-84eb-5d341e9b89da | 0.86107 | -59.61596 | 2024-11-10 01:19:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c72759cc-3568-32c9-812e-578cfc39eabf | -3.6132 | -55.48081 | 2024-11-10 01:19:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 82f8565a-1e68-3723-b7ba-b4276754f567 | -3.86859 | -52.38296 | 2024-11-10 01:19:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| da5c80bb-5a26-31c4-ba86-ca2b9188e443 | -3.8737 | -49.94361 | 2024-11-10 01:19:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 0a462634-1a29-3053-8cbb-143c468752dc | -3.30395 | -45.64481 | 2024-11-10 01:19:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 30.9 |
| e28c79e8-4aba-3055-9f1b-c3610aebb239 | -2.5716 | -47.34585 | 2024-11-10 01:19:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 93e2e286-958c-33b0-91ae-ee7e1e71df87 | -2.41964 | -53.66825 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 32ed04ac-4a89-3979-9c74-4953b12154a6 | -4.51544 | -56.08188 | 2024-11-10 01:19:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8ba24f07-3ee6-36e2-97d1-ffa276706d66 | -1.51969 | -55.00257 | 2024-11-10 01:19:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d6e5cb8d-d20d-38ca-890d-51bcf9d031f3 | -2.5459 | -45.3872 | 2024-11-10 01:19:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 563e7eda-acf5-3d9c-9fda-7e465335ac47 | -2.04047 | -52.04495 | 2024-11-10 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| da0e7b2b-051c-3428-a28c-d3202476525d | -2.94065 | -52.78115 | 2024-11-10 01:19:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 35317919-5ccb-365a-97ff-f8c6f8e8ff6c | -1.49676 | -51.74111 | 2024-11-10 01:19:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| b4ed0f9c-106d-3ebb-9842-5ba90aaf5bec | -3.1141 | -54.47799 | 2024-11-10 01:19:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 98231d94-77ae-3122-807d-dec7043c1d42 | 0.63317 | -60.09047 | 2024-11-10 01:19:00 | TERRA_M-M | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 24855c08-cb4b-3de0-9336-0a6569db2067 | -3.71239 | -53.75556 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c7b274af-a51f-3330-9aeb-ddaeaef15ba3 | -3.10689 | -45.28938 | 2024-11-10 01:19:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 11a92169-1e86-3706-8603-33e47f147cd2 | -1.9475 | -51.09819 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0e94f391-00e6-3e67-9ef7-c7c64d7e3279 | -3.1163 | -53.70945 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 2aaccbf8-6576-3b9b-aaab-bf69742935e0 | -3.30914 | -45.67844 | 2024-11-10 01:19:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 134.3 |
| 2af6ba9f-157f-3467-9c13-69f0a70fc628 | -4.7288 | -50.37866 | 2024-11-10 01:19:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 0534f43c-c10a-37c8-ba00-b39c24b950be | -4.89848 | -48.6284 | 2024-11-10 01:19:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 867618e7-92af-3f3b-a120-2c72f11e4cb6 | -3.20507 | -50.63208 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 7c0e9a8d-60db-323b-b7a3-08bdfc6f66b0 | -2.90172 | -54.0187 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0f7fa509-e6ac-3f00-8d50-424edea5e056 | -2.75117 | -49.35156 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 320cbb83-534f-32e8-bb66-6c5a98bde94e | -2.19593 | -49.52946 | 2024-11-10 01:19:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 2290ce0c-8935-3b1e-a821-cc18593b5d0e | -2.45421 | -54.04802 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a8d0643d-299e-359b-a99b-00e10017d3c3 | -1.51846 | -54.99375 | 2024-11-10 01:19:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 3bb52050-791c-3fb8-a89d-3173eb1261a2 | -3.76191 | -52.65933 | 2024-11-10 01:19:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| bdbe95cd-e121-33bb-906f-e3d3ec68de2c | -1.44786 | -54.29546 | 2024-11-10 01:19:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b88ff116-acd5-38fa-b599-e588e42423bb | -1.15502 | -53.78088 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| c8e3e6c3-4f4d-3f8b-b59a-04cf806eb0ff | -2.47093 | -50.4138 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| d9038999-3549-3f95-bb8e-d909a842d446 | -3.04426 | -49.55098 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 29d9ef65-393d-3103-a26c-99289a7ddb49 | -2.6511 | -51.87964 | 2024-11-10 01:19:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a1d7bbd8-e2f6-340d-929e-fdbf6248281c | -1.13565 | -54.10673 | 2024-11-10 01:19:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 608d03f5-d2d5-311b-a0ea-823536035068 | -3.3501 | -50.05757 | 2024-11-10 01:19:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| b8bf7d3e-fdc8-3b74-a984-bc5e72f77e73 | -3.56394 | -53.94651 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| d93b4ed7-f974-3813-9c24-d66a6aab5b80 | -3.23532 | -50.29102 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 521b9867-9454-3bba-8810-8fa13edf2c3b | -2.69325 | -49.88144 | 2024-11-10 01:19:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| d18f131b-b8c6-3968-84c2-56c7f6e8062b | -2.86976 | -51.83584 | 2024-11-10 01:19:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 686b22f8-6c16-3487-8cb2-120aecf023ee | -1.51256 | -52.14557 | 2024-11-10 01:19:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| e1a41af3-dc4f-3176-b399-0168c04d6346 | -3.10125 | -49.39863 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| e2d1ad6e-6e1e-37bb-b315-5e62e8e91301 | -2.24324 | -53.79084 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| af9b8b72-c10e-3224-99d5-a5b94d844995 | -2.11342 | -50.56419 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 14f76070-bf94-30d7-ae30-3c5c9cfec736 | -2.25144 | -46.50874 | 2024-11-10 01:19:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 50658b4c-21fe-3ec4-9ec5-8f9aed7ad678 | -3.05012 | -51.09017 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 3e14cb4f-7a97-35c9-bbb7-fb4c6e150882 | -1.14722 | -53.79187 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| dd3db9bd-bc2d-3da3-be4e-fdc6f9f2d709 | -1.71576 | -55.16636 | 2024-11-10 01:19:00 | TERRA_M-M | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5eda9550-f8f6-3cfb-9723-4f2c48faa537 | -3.06855 | -48.04037 | 2024-11-10 01:19:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 1aac8659-7b17-34b2-93c4-c45f0166d5a3 | -3.24432 | -50.28144 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| a70661d8-2fc9-3faa-9580-ea6862ff9cd3 | -2.82376 | -53.98981 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f47209c4-acc3-3ce6-90af-db7aa67a2e3f | -3.11057 | -49.42109 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 0b9c947c-deca-3190-ae04-0f87733e871c | -2.4586 | -53.68507 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 764a014b-568b-3c66-92d6-43361eacaf8e | -2.63399 | -49.46918 | 2024-11-10 01:19:00 | TERRA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 08a82a09-b553-372f-b146-a9682827db0a | -3.35917 | -54.1254 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 431b21b0-99f7-317b-89c3-728d08ed38be | -3.59046 | -47.32798 | 2024-11-10 01:19:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 4a3aa7a6-7d58-3e69-a176-198e9ed41213 | -2.03215 | -52.05772 | 2024-11-10 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| f5aad2d2-b461-3ca8-8b5d-72a6c8e42877 | 1.57821 | -56.06193 | 2024-11-10 01:19:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2aebc715-05da-3494-8c3c-e7f5a388c836 | -2.35748 | -53.75292 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d83dbfdf-164d-3dbf-a359-43e8ffcf2db0 | -3.95611 | -49.00378 | 2024-11-10 01:19:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| b0eb90da-0a51-30e7-84f5-c829532fc98c | -3.91639 | -52.41185 | 2024-11-10 01:19:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5c663bcd-9381-3cd2-9623-b753ec83e0d5 | -1.3585 | -54.64983 | 2024-11-10 01:19:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 64b6b3f7-4c4c-3663-bf55-44ec1e0f0892 | -2.40874 | -50.30266 | 2024-11-10 01:19:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 204e551e-d818-324d-b64f-ef89e483cb7d | -2.93924 | -52.77101 | 2024-11-10 01:19:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 181.2 |
| df3d16e2-6ada-36e3-b4f9-5a39c4f78ac3 | -4.17212 | -48.59695 | 2024-11-10 01:19:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| fe63e1b0-267f-34e4-ae73-70366555a57d | -4.07847 | -50.00732 | 2024-11-10 01:19:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 1a14f808-d959-335c-ae23-421e14022ef3 | -1.59004 | -52.18633 | 2024-11-10 01:19:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 4a9a70b4-4b90-39fc-8c42-6df18d12964c | -3.80292 | -51.99213 | 2024-11-10 01:19:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 48e85284-d189-317d-9b30-3967696f0fdb | -3.32814 | -54.17213 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1038e72d-98ea-34ca-ba29-950c83935c92 | -3.52717 | -51.63896 | 2024-11-10 01:19:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 866b0729-1581-357b-9a3a-4aa437483b3a | -3.18187 | -53.84941 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ed025ff3-3245-3bdb-a84a-7cbc640ebf07 | -3.6197 | -54.79896 | 2024-11-10 01:19:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9c91db3e-55d7-3916-ae15-e10aa461d114 | -4.85196 | -46.96774 | 2024-11-10 01:19:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 238.4 |
| 69d59d77-b0c8-33e8-b4c8-d2a3b604dbda | -3.66315 | -54.65808 | 2024-11-10 01:19:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8f7b6fe9-88c0-3577-96ad-f7ee8f506055 | -2.94412 | -54.45103 | 2024-11-10 01:19:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 515fd48b-c745-3104-b203-8219bead0286 | 0.62687 | -60.08147 | 2024-11-10 01:19:00 | TERRA_M-M | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 11.8 |
| bceaaba4-f52a-3e71-b7ce-a5d3d59dddce | -4.13034 | -55.82673 | 2024-11-10 01:19:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 69905df8-e490-38a9-ae32-69db5c0a95ef | -1.24092 | -51.75288 | 2024-11-10 01:19:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 37c6fc65-c1e0-3cc3-98a9-25d119916ee4 | -1.1773 | -52.08911 | 2024-11-10 01:19:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |


[Clique aqui para ver as próximas entradas](README14.md)
