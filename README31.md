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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb507a0b-0067-3ee9-b3c3-89f9474cb4c4 | -2.30908 | -49.06111 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c5b2760-45cf-3229-9381-09f7ffba5797 | -4.0594 | -46.843 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2a94443-d3c6-342c-b949-3e82bba12f7a | -2.66048 | -46.16346 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 671f54b5-f76c-387f-b177-99775bf71c03 | -1.18434 | -53.72005 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 64ebd95c-97ab-3b17-a21d-b099081c5114 | -2.85549 | -51.27972 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0e6f814b-d96a-3bbf-8909-983985ebcd44 | -1.60274 | -52.41286 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6f41abcb-c440-38a7-a299-18849383aabc | -0.77857 | -51.76649 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38517414-511f-3b66-9faf-76c650506d7a | -2.43176 | -48.63454 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b6b4527-c86e-3915-8241-2f818867d97b | -2.6255 | -51.92296 | 2024-11-21 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 613fdbd3-d8a2-32cd-9d9f-103fccdc010f | -2.21262 | -47.99315 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a66e58e1-8142-32ce-adcb-fa5b62c69792 | -2.00653 | -46.85759 | 2024-11-21 04:29:00 | NPP-375D | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c7d433b2-e7ed-3301-9530-de78d046f546 | -2.61589 | -49.24132 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| deebd155-01a5-31c5-9185-2afe2edfe3d7 | -2.94137 | -48.32928 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b8f6ce2a-c828-3a0b-a813-54779e1843e8 | -1.74569 | -52.05709 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 679146cf-2cfd-3862-9183-23018943d4cc | -2.78745 | -51.71955 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a6242172-660f-389a-971a-9c76cf1fffc1 | -2.74425 | -51.72611 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 829b8911-afea-37b8-a55b-394d00a8f752 | -2.87909 | -52.4492 | 2024-11-21 04:29:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1be9f9a6-5d64-3274-b873-a462a4157dd6 | -3.15028 | -51.50965 | 2024-11-21 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86047a3f-4f74-3226-b428-91717b97cd25 | -3.2874 | -50.54078 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1064e0c2-5739-3190-860b-328cb0383cd5 | -1.24944 | -51.78329 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02145341-cfe8-39ae-9344-8fc9eb4bc5ed | 0.04933 | -49.52088 | 2024-11-21 04:29:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ffcda55-cd48-3c9f-990a-c389cd839f7f | -3.23254 | -46.44085 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf893f17-969a-397f-b8c2-1791ededf774 | -2.65934 | -46.14903 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54b03f9a-da1b-3734-a4a0-b34e3440e2e9 | -1.13033 | -54.17617 | 2024-11-21 04:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59c294e2-0003-3772-85e5-a632eb10fa06 | -3.94679 | -46.69799 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8d43c50-31bf-3f5b-879c-211f0bdc1034 | -1.63813 | -52.60382 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2cf9bb99-d84f-3f99-9444-ce2b3229645b | -2.7005 | -46.23017 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3541f7c8-b5e2-3f49-969b-39ab6c68b9b6 | -1.393 | -55.17776 | 2024-11-21 04:29:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c385afb-5f1e-3f87-a0c1-cc6ebe6a1fd5 | -2.05051 | -47.73577 | 2024-11-21 04:29:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d11d7e95-186b-354b-b734-1e902803d6c8 | -1.20247 | -51.76081 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f5c8a9e-d4ef-3d39-8941-fa490f172cf4 | -3.88958 | -46.65368 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d273920e-dd82-34d8-b22a-363cd2869a2c | -2.6916 | -46.22168 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0e02024-b896-3b90-bbb9-9e353670e6c2 | -3.69143 | -49.96829 | 2024-11-21 04:29:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43ce4c32-b0f3-36a3-ac36-4ade9254929c | -3.06889 | -49.204 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ee5a0084-feb0-3d1e-a3a7-f6838daf7348 | -1.77025 | -54.23853 | 2024-11-21 04:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 44ac49fa-0785-3f6b-b4de-b73465a1da86 | -2.57577 | -49.22313 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30497bb3-453e-3bfd-a653-49667fdaf511 | -2.23601 | -46.81909 | 2024-11-21 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8f9e2d15-c652-3ae1-8cfd-66107525fc30 | -3.08666 | -45.96798 | 2024-11-21 04:29:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c2a7981-a66d-3930-bbbe-fb713b51b6ff | -2.74191 | -54.01086 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ffff459-a2f1-3c8d-a71c-0a7d09ac6a98 | -2.99396 | -52.37437 | 2024-11-21 04:29:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd9d2f7a-f9d9-3bc1-bf86-70a2669d88a6 | -0.04711 | -51.24612 | 2024-11-21 04:29:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2507c6ce-cf4a-3bb1-a82d-2d930292c8d5 | -1.76293 | -50.8552 | 2024-11-21 04:29:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a8d9a65-a93d-3708-88be-c58a87bfe184 | -2.25776 | -48.6986 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a8da7e11-9308-3ab0-a900-41d8b27f0e38 | -3.84521 | -46.63256 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81b9474e-a9b0-3107-828d-c5539902709c | -2.3062 | -49.05674 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8a9972b-de6d-3e00-b3fe-d57902bc9355 | -2.22411 | -48.38153 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b0a87a3-c020-390f-ad60-5d26221403d9 | -4.08374 | -46.8397 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50351a11-8456-3e49-93ed-0f7d165611d9 | -1.34974 | -51.43454 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82c5921f-518b-3124-a1ba-5efaf87ab330 | -1.64255 | -52.6886 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba440d49-6fbd-3694-a06b-897f0bebe731 | 0.8191 | -50.25064 | 2024-11-21 04:29:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7ea73d60-9967-3c5e-ba13-328725a564ab | -2.99447 | -51.46047 | 2024-11-21 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2043204-9c8a-3b7e-b940-0ca3462bad3f | -2.25239 | -48.42275 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54266c07-bc11-3067-b96c-e4a61f3d0fde | -3.55108 | -50.16993 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be40912e-2ae9-3820-947e-84d5647c7e79 | -1.60104 | -46.87164 | 2024-11-21 04:29:00 | NPP-375D | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6ab94f05-0598-39ca-9b57-75c861e8cd40 | -1.6349 | -52.62424 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 37af00a8-d656-36a1-b1f8-a5018e1b0963 | -1.75936 | -52.66757 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e50f219-d041-3d23-a595-df56e01f4ea0 | -3.4998 | -48.22316 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| afce5c49-09df-3bb6-8425-498aaa237f19 | -3.81013 | -47.80341 | 2024-11-21 04:29:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee4d4411-3477-3d90-b2d0-5e1c30b46fac | -2.69746 | -51.3657 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1655903-2ebe-3536-bebb-0fae8de5cad0 | -1.09859 | -47.50473 | 2024-11-21 04:29:00 | NPP-375D | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47b3082e-8b1c-35bc-87d0-7966ae2a6827 | -0.29818 | -51.60556 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b86c9d42-da8d-34fb-91c1-a908939f5dc1 | -2.58679 | -51.72553 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a88b1502-9189-3e57-a904-f604964a2dcb | -3.34186 | -50.49844 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3837474-efa6-362d-8b7e-4815d9877da4 | -1.20773 | -51.7542 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6da3642-c83b-392c-8fe6-7dd34097fb04 | -3.7865 | -49.36783 | 2024-11-21 04:29:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d1ee0e6-0feb-3db6-8196-ab486caa7e21 | -2.39525 | -46.79506 | 2024-11-21 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93479242-fd46-313a-adae-6dbd7a664568 | -3.30025 | -50.22287 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51a7516e-76c9-3a04-a265-164dd1e1b3ec | -2.62639 | -48.07224 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 244d1aaa-7579-332c-8736-9d14c70a1b7c | -3.46827 | -50.01041 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 96e7c029-32fa-31a7-8359-5b754c1c5d19 | -0.97268 | -51.71711 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47120cf6-f696-3e8b-b30a-10c1c1727319 | -1.10761 | -51.75737 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a64a913f-b5a6-3f1f-b2e5-238e9a5c9b91 | -2.60651 | -48.21898 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0bd47119-7525-3703-83f6-efb4e7cf978a | -1.97851 | -53.33079 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7bfb9986-9ac6-3b75-8fbf-712271a1d17f | -3.54967 | -50.27511 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9d22452-fff1-3a92-9cdf-c7d6235f4ad1 | -1.08831 | -48.21053 | 2024-11-21 04:29:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad4bfd69-862d-30c2-8048-0c981c2dcff1 | -4.01071 | -47.97063 | 2024-11-21 04:29:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4aff2633-97a5-30f2-b860-74e2f5f747d5 | -0.95919 | -51.72247 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f4174aa1-7dc7-3fc8-b36b-840991c89b71 | -2.65328 | -49.28209 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88b21de8-ef51-3ed2-859f-5c706db488f9 | -0.78212 | -51.77084 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b63bb52b-1779-38eb-b1d9-97ea26003ca8 | -1.50066 | -51.97334 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd2659fe-6d3b-3d66-900a-623b1c795320 | -1.71173 | -52.38093 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1d43be4-6c2e-34b6-ba06-b96aedd65d88 | -4.154 | -42.02111 | 2024-11-21 04:29:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f2908dc7-0fb1-3427-b64c-c09ebb4be978 | -2.75184 | -52.116 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9b62471f-2051-3231-b46e-721d4f4453d5 | -0.97679 | -51.71775 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0b47cae2-df9e-3fc4-b36f-a71b0e38077f | -2.95208 | -48.32729 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 84912aae-db1b-358d-aa6f-fd925476c6cd | -3.50316 | -48.2237 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e27a4a68-4034-3066-8bb2-c1608a6cb814 | -2.79972 | -51.77018 | 2024-11-21 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 774b677d-d61d-3dbd-bfe0-19f28b9ccb6d | -2.5391 | -46.22667 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9a7a8e0e-f18b-37ea-8d91-46d10b48a6e9 | -1.25191 | -51.78292 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c40c696-c531-3be8-8d59-d32f98ea2596 | -0.95977 | -46.79613 | 2024-11-21 04:29:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79c84e03-78bb-38b9-8518-7b696b02df47 | -2.9408 | -48.33288 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c2b4a2d2-2c87-3d99-8458-6bc5f59ffeef | -3.35481 | -50.18708 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8d4c106a-fb3a-39bc-8dfa-49c676cda0e6 | -2.3825 | -48.92085 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b15ac179-3a79-3081-af87-124b7d015583 | -2.0299 | -50.07317 | 2024-11-21 04:29:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c24cd079-cd8d-353c-96af-55f392f0f975 | -3.0705 | -49.20358 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| e9e27c60-0bbc-3814-951d-21cc52ae8da1 | -2.69098 | -46.20378 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0700007f-2527-3146-a923-c5ec1a3902ed | -4.07878 | -46.84956 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 244779ae-6254-3470-9c34-b47e03f724a6 | -2.02281 | -51.17978 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03eb6c4e-8b2d-330b-8e3d-d52454543c22 | -2.14557 | -50.4906 | 2024-11-21 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e62ef5bd-b548-39f3-9ade-5a81ed227d27 | -1.70043 | -50.20254 | 2024-11-21 04:29:00 | NPP-375D | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README32.md)
