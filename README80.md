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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85cb7dcb-cf05-361c-a782-d5597d8df4a4 | -6.42202 | -38.38129 | 2026-09-14 15:29:00 | NPP-375 | LUÍS GOMES | RIO GRANDE DO NORTE | Brasil | 2407005 | 24 | 33 | nan | nan | nan | Caatinga | 13.6 |
| f018cef7-dcbf-3b92-9f29-f2d77f6a1759 | -9.12191 | -39.99583 | 2026-09-14 15:29:00 | NPP-375 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 750f2375-0c19-30a5-ad61-506fa5efb3bd | -6.22279 | -35.38643 | 2026-09-14 15:29:00 | NPP-375 | BREJINHO | RIO GRANDE DO NORTE | Brasil | 2401800 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 89a7a0d2-5c6b-3c77-b667-4e9dfc19529a | -10.41913 | -39.31593 | 2026-09-14 15:29:00 | NPP-375 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| d73d9ccd-5d56-356c-81cc-58861e1c4404 | -8.58197 | -39.49576 | 2026-09-14 15:29:00 | NPP-375 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 2caf90fa-ea5c-3c75-859f-020e00671bd7 | -7.52066 | -36.25892 | 2026-09-14 15:29:00 | NPP-375 | CABACEIRAS | PARAÍBA | Brasil | 2503100 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d1fb1d9d-d709-3234-b413-7aadf2a5f43d | -8.70783 | -39.60718 | 2026-09-14 15:29:00 | NPP-375 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 820b57b1-6ae2-3a42-a11f-2fd2ac156da4 | -11.20386 | -39.69668 | 2026-09-14 15:29:00 | NPP-375 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| e1e8c572-75dd-3cb8-a738-62434b20b02f | -7.88148 | -36.98989 | 2026-09-14 15:29:00 | NPP-375 | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 60fb88b1-51a1-3386-8b41-f323f56cef54 | -6.87138 | -38.74219 | 2026-09-14 15:29:00 | NPP-375 | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 11.2 |
| ec700d20-15c6-3288-bf61-75f3a6e0a935 | -6.33576 | -38.97594 | 2026-09-14 15:29:00 | NPP-375 | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| a96f2c38-99b8-303e-8ea6-4b22e003fb23 | -10.42341 | -39.31385 | 2026-09-14 15:29:00 | NPP-375 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 6de5b15b-ef39-3173-b57b-f521236db6b3 | -6.16048 | -35.14552 | 2026-09-14 15:29:00 | NPP-375 | SENADOR GEORGINO AVELINO | RIO GRANDE DO NORTE | Brasil | 2413201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 3318e3b9-8157-367f-90c5-39d42a6dcde4 | -6.8706 | -38.74016 | 2026-09-14 15:29:00 | NPP-375 | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 8c5d4468-5eba-347e-a904-6919a7b25e57 | -6.42494 | -38.3794 | 2026-09-14 15:29:00 | NPP-375 | LUÍS GOMES | RIO GRANDE DO NORTE | Brasil | 2407005 | 24 | 33 | nan | nan | nan | Caatinga | 27.3 |
| b3c6ec1b-8b08-31c7-97c7-9d767d04be4d | -5.81205 | -38.32175 | 2026-09-14 15:29:00 | NPP-375 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8a638b0a-04a7-37b0-b0ec-f4a14230795e | -8.23335 | -36.66499 | 2026-09-14 15:29:00 | NPP-375 | POÇÃO | PERNAMBUCO | Brasil | 2611200 | 26 | 33 | nan | nan | nan | Caatinga | 5.0 |
| cb0498c8-a945-3924-9527-2fb4af53ef87 | -9.12272 | -40.00289 | 2026-09-14 15:29:00 | NPP-375 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 70f4b6cb-4c6b-3acd-9c5c-7949e7682775 | -10.0447 | -39.66158 | 2026-09-14 15:29:00 | NPP-375 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 37da7be1-57e2-30b4-bf27-1b05c693e859 | -8.70873 | -39.60529 | 2026-09-14 15:29:00 | NPP-375 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| b7667acc-bc19-3077-815d-87c243ddbd95 | -6.33058 | -37.46087 | 2026-09-14 15:29:00 | NPP-375 | BREJO DO CRUZ | PARAÍBA | Brasil | 2502805 | 25 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4a2aa887-eb84-3756-91d7-4fae2d88aa06 | -9.11907 | -39.99715 | 2026-09-14 15:29:00 | NPP-375 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| c1d1d940-1dd8-3370-939f-7cef2b16c76b | -6.05464 | -36.3826 | 2026-09-14 15:29:00 | NPP-375 | CERRO CORÁ | RIO GRANDE DO NORTE | Brasil | 2402709 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d9eac657-41b5-3db8-a407-71d17cc74fd8 | -8.3641 | -35.26313 | 2026-09-14 15:29:00 | NPP-375 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| e0a1a0db-f3ae-3943-b6de-3495906409c4 | -11.20095 | -39.69176 | 2026-09-14 15:29:00 | NPP-375 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 0bad55aa-d9e9-31c7-8858-395e8b83e937 | -4.4549 | -39.35219 | 2026-09-14 15:29:00 | NPP-375 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 87.3 |
| 0a6f5483-6fd8-3e3e-a4ea-03e7fb7588ed | -9.35882 | -36.9514 | 2026-09-14 15:29:00 | NPP-375 | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 618e5357-f0fc-3d4f-b9fc-fd240ff4461d | -4.45637 | -39.36273 | 2026-09-14 15:29:00 | NPP-375 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 55.2 |
| 2d1b7bde-4a7d-36c6-8e6c-05c9629b7ef3 | -7.85085 | -38.07667 | 2026-09-14 15:29:00 | NPP-375 | TRIUNFO | PERNAMBUCO | Brasil | 2615706 | 26 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 7c30ee9f-6359-3061-b16c-3febb742190b | -10.33998 | -40.03816 | 2026-09-14 15:29:00 | NPP-375 | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9012b900-ae9e-3ccb-80fd-30792d224dbc | -6.42142 | -38.37669 | 2026-09-14 15:29:00 | NPP-375 | LUÍS GOMES | RIO GRANDE DO NORTE | Brasil | 2407005 | 24 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 16c9a50c-4720-3f74-9fdf-c6ea0329c49a | -7.8539 | -38.07438 | 2026-09-14 15:29:00 | NPP-375 | TRIUNFO | PERNAMBUCO | Brasil | 2615706 | 26 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 07238c80-7702-39a2-9c7f-b62fb06eab99 | -4.73547 | -40.31961 | 2026-09-14 15:29:00 | NPP-375 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e209e16f-cc67-3234-b3a4-c40d87fc4f8a | -4.98191 | -37.38573 | 2026-09-14 15:29:00 | NPP-375 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 66ce67e5-8d5a-3973-9d7f-9e0719947293 | -6.87127 | -38.74512 | 2026-09-14 15:29:00 | NPP-375 | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 3cad58f7-1591-39d2-a076-3b5db296f93e | -7.73381 | -37.66661 | 2026-09-14 15:29:00 | NPP-375 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 60fbf1a4-abd4-321b-8ef3-8c8127fe2619 | -2.6601 | -57.5702 | 2026-09-14 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 3fe46484-50f9-3f97-a87d-9a3eacd947df | -3.6457 | -58.6143 | 2026-09-14 15:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 0bd65dda-b3cd-3c14-a244-f14042d01de9 | -3.3306 | -54.1805 | 2026-09-14 15:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 06b8f24a-cdd3-37c5-9751-0de2912bcd00 | -10.6824 | -54.1884 | 2026-09-14 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 151.5 |
| ba7b9a53-4ff2-3730-9928-0ff9808e7430 | -3.1514 | -58.644 | 2026-09-14 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 9c0d252a-8903-36c0-b48e-78869f0f92bf | -10.312 | -45.2907 | 2026-09-14 15:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 247.1 |
| 1edc8e7c-58eb-33c0-99c5-c9be539d0d67 | -2.6601 | -57.5507 | 2026-09-14 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 98.2 |
| b6a7a4cf-f52f-3255-8135-2dd9f1b5e687 | -9.4134 | -50.153 | 2026-09-14 15:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| ee77815b-89d3-35a1-bbc7-bea4238ee553 | -8.5812 | -44.4629 | 2026-09-14 15:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 102.8 |
| bc4c2811-6c94-3bd6-95d4-2da9701a0be7 | -6.67 | -43.657 | 2026-09-14 15:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 161.5 |
| 2dbb5e80-bf7c-32d8-9957-e308d28c9b11 | -9.1711 | -49.9835 | 2026-09-14 15:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| ddfb864a-a876-3420-9e34-4cd5930b9baf | -6.3436 | -55.8243 | 2026-09-14 15:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| b00cbea8-918f-38de-b2dc-69acccf7473f | -3.3305 | -54.2005 | 2026-09-14 15:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 4d1863a0-00d2-3ccf-9feb-1f569cf7f483 | -10.5667 | -51.3349 | 2026-09-14 15:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 64353a1e-ad47-339d-ab04-e9c32f29527f | -7.7636 | -46.6722 | 2026-09-14 15:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 9b868711-9be4-3066-8c6d-415a9d56a4e1 | -11.3349 | -46.7899 | 2026-09-14 15:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 42b8d9c8-8bfe-3782-bd05-2caac9f7037f | -6.2916 | -55.2895 | 2026-09-14 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 8c386a60-24a8-3e4c-8f28-4fa79fb68143 | -11.4905 | -50.2581 | 2026-09-14 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 0b0966d4-7c02-3611-ad7d-2be8052afd8a | -10.5484 | -51.2945 | 2026-09-14 15:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 156964a4-034e-37ab-a51b-510b54615e9b | -11.4908 | -50.2366 | 2026-09-14 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 898842af-3f62-3606-825f-51e0687f4c81 | -11.8362 | -50.0244 | 2026-09-14 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| ca431102-881c-3d59-82f3-e30cdd4ff73f | -13.5526 | -51.4629 | 2026-09-14 15:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 314.0 |
| ebb88253-2678-3830-a867-86fd30a82987 | -8.4112 | -54.7073 | 2026-09-14 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| a88b64bb-542a-3cbb-809b-f5fc0804a745 | -8.8081 | -45.8753 | 2026-09-14 15:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 133.6 |
| dcc33924-053c-336d-814c-36b26bcaab29 | -13.5719 | -51.4605 | 2026-09-14 15:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 194.0 |
| 4d32508a-6f6e-331e-b11b-dca2acfce32c | -10.661 | -51.3465 | 2026-09-14 15:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| a2abbbbe-2615-3834-b994-acb9a847ebc0 | -5.2023 | -49.3348 | 2026-09-14 15:30:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 8cf16c95-8f20-3c3c-b76a-5f932b7ee03d | -3.1816 | -61.1045 | 2026-09-14 15:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 8d1771eb-b8c9-3754-bc85-99ffa599eb36 | -10.2926 | -45.3161 | 2026-09-14 15:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 1e25fbbe-7788-339e-b30b-b97eae8abe58 | -4.5382 | -55.6196 | 2026-09-14 15:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 1cd633bc-326a-3748-9916-7488a8e472b5 | -2.6602 | -57.5313 | 2026-09-14 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 84f4863e-43d1-3aa1-a930-6742a0bc3b9d | -12.1265 | -44.199 | 2026-09-14 15:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| ca649065-86f6-387e-86e7-c4cecdb9cceb | -13.5523 | -51.4843 | 2026-09-14 15:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 56bb441c-a4dc-39e9-bdcb-b90e91059abb | -9.3572 | -50.137 | 2026-09-14 15:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 4b91bf07-cc46-3eb3-8726-bd747a4e553b | -3.6077 | -59.0577 | 2026-09-14 15:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 045517c6-fed0-391a-bd5c-34fd4c89dfab | -10.7722 | -46.2549 | 2026-09-14 15:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 252.7 |
| 5ccc87cf-789e-3bed-84ac-97ac8673e2ee | -3.4632 | -58.4062 | 2026-09-14 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 6d04b094-80f5-3da2-9d6f-df807217097c | -9.3753 | -50.1992 | 2026-09-14 15:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| bc0929e2-7630-3d66-a948-04373766b818 | -1.7316 | -54.9518 | 2026-09-14 15:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 19387892-9d77-3202-bf97-132b39c11e43 | -10.7015 | -54.1663 | 2026-09-14 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 814bd736-4d15-342f-8630-94db98652bad | -10.7532 | -46.2573 | 2026-09-14 15:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 11e6f629-accd-335b-964e-84f661643614 | -7.7824 | -46.6705 | 2026-09-14 15:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 2f046895-7e57-327c-badd-4bbdc1b9c4f8 | -9.3758 | -50.1565 | 2026-09-14 15:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 131.0 |
| 5473f767-0b37-3bd4-b4bd-e54933dccef2 | -11.8365 | -50.0028 | 2026-09-14 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 2ebf1ad7-fa43-38ab-aa29-7027d376ce32 | -10.7906 | -46.2977 | 2026-09-14 15:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| eb5ecbcf-ee7c-3c48-a6f3-18833cbe7b90 | -5.221 | -49.3125 | 2026-09-14 15:30:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| ff377349-e176-3f6c-aa04-7de80a971835 | -3.4279 | -57.9816 | 2026-09-14 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| a56a3aae-fe85-3823-a0b8-c134098e728c | -3.314 | -59.3706 | 2026-09-14 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 148.0 |
| b990f238-baec-3484-990e-63b7b8ac9b45 | -9.3948 | -50.1334 | 2026-09-14 15:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 538194a3-105a-3e02-af62-3c52ef162ef0 | -8.5417 | -54.6985 | 2026-09-14 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| f5ce2364-8ac9-38c6-a888-c95d7788348b | -11.5095 | -50.2559 | 2026-09-14 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 0595aaa4-82d5-3cac-8537-11dfb07300b5 | -7.1048 | -41.7971 | 2026-09-14 15:30:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 230.6 |
| 02a91e06-0609-3a40-b518-4f258b1dbf84 | -10.7719 | -46.2775 | 2026-09-14 15:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 9e2f57ec-2c16-30e3-b4b4-b04c54e4d349 | -2.6785 | -57.5115 | 2026-09-14 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 38a4ce8e-f774-3197-bf91-70db86ee1564 | -10.7715 | -46.3001 | 2026-09-14 15:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 343e298d-b070-3d2b-90fa-403a2cdccb09 | -10.6335 | -50.5651 | 2026-09-14 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 0b0ad3a9-8900-30a4-b4fe-e763393afd0e | -10.2929 | -45.2932 | 2026-09-14 15:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 106.1 |
| c243cec3-67ff-34e7-932c-c09368ade828 | -6.6512 | -43.6587 | 2026-09-14 15:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 320.9 |
| 5deb24d3-2ce5-3037-87db-c8cc6a347f22 | -6.1608 | -52.7701 | 2026-09-14 15:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| ca0de9a7-7420-3a1d-8d25-1a86edd9e4a2 | -9.376 | -50.1352 | 2026-09-14 15:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| c6e9ad69-9a6d-3c5c-a76b-731931efacde | -3.1462 | -60.6317 | 2026-09-14 15:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| f550b6c2-8cd9-31dc-b605-f89dd3616ea8 | -10.6525 | -50.5631 | 2026-09-14 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 34c13a15-28cd-3c19-8e4b-a9fbc5718d5f | -3.3141 | -59.3515 | 2026-09-14 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 69807a83-7b4f-39c8-af5b-2c00281b27c6 | -3.7181 | -58.8823 | 2026-09-14 15:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |


[Clique aqui para ver as próximas entradas](README81.md)
