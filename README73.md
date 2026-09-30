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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1495427-4736-3cef-9dc4-dd7ac4d81114 | -6.7006 | -52.4933 | 2026-09-30 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 0cabac2d-8d66-3fed-9e3a-4f3b0d18bb92 | -9.0652 | -45.0062 | 2026-09-30 15:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| d07d590b-39ef-3fed-b1a1-3bdf51afef33 | -6.1402 | -53.0574 | 2026-09-30 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 120.1 |
| b8f46ee8-eb6f-3b4d-b931-529ba81aec31 | -8.3805 | -45.3994 | 2026-09-30 15:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 117.3 |
| bbe72c6b-9629-3563-929d-eed5d510aa31 | -3.0 | -51.01 | 2026-09-30 15:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7f8f7a3-63ff-3d98-bcb8-b0ecb3f1ea8e | -5.76 | -45.19 | 2026-09-30 15:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7d14d14e-a3a6-3cc3-bda1-f5803e9443f8 | -12.44 | -44.15 | 2026-09-30 15:15:00 | MSG-03 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bda1bb29-b5e4-34a8-b056-c5df407416e4 | -5.76 | -45.14 | 2026-09-30 15:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9a607b08-f58e-3b40-9a17-32db2b836435 | -10.3 | -44.64 | 2026-09-30 15:15:00 | MSG-03 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 583ed2cf-6703-37fc-b4ad-faf20b6a83b9 | -3.7129 | -60.5832 | 2026-09-30 15:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 7c4e67a8-7d57-3ac9-903e-762523129000 | -10.1095 | -50.2135 | 2026-09-30 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 67fca619-76e7-38ef-9700-12e25ee19f60 | 1.6749 | -55.9225 | 2026-09-30 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 1fbfe19e-09ff-366b-bd99-0010f549edfc | -8.2479 | -45.4583 | 2026-09-30 15:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 1556add8-2f7c-3a5e-9faa-d9aa775169fc | 1.6749 | -55.9619 | 2026-09-30 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| f7d43911-df43-3e68-88f5-2667b9e9d3ea | -8.3802 | -45.4221 | 2026-09-30 15:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 9400d847-d39a-339f-9156-6a8c2e23dfa7 | 1.6566 | -55.9424 | 2026-09-30 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| f30bb555-631e-3ddd-b5ce-e1c7113494de | -3.6947 | -60.5455 | 2026-09-30 15:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 6326bad3-9fe1-385a-bedd-0644b54d68b5 | -9.2237 | -45.8527 | 2026-09-30 15:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 53.2 |
| bc5b394d-52a8-331e-ba04-1ebb465465a2 | -1.2085 | -49.0838 | 2026-09-30 15:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 70fea8e3-7ed6-3925-bc43-c6922777af22 | -8.4968 | -36.88573 | 2026-09-30 15:29:00 | NPP-375 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 242994ed-f5c1-3c1d-a8af-846873487538 | -9.32569 | -37.80249 | 2026-09-30 15:29:00 | NPP-375 | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 76e18f7b-9847-386a-9b37-69f2ba1f0bce | -8.73747 | -36.82904 | 2026-09-30 15:29:00 | NPP-375 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 3.9 |
| ff02a85e-4a8f-324f-a0a8-bbeecf2bebbf | -8.97279 | -36.19801 | 2026-09-30 15:29:00 | NPP-375 | CANHOTINHO | PERNAMBUCO | Brasil | 2603702 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| fbb07ebf-2300-37ac-b326-909eddc09338 | -11.94476 | -38.29272 | 2026-09-30 15:29:00 | NPP-375 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| a2106be5-2710-3c69-83a9-48b3f47b4cbc | -11.77332 | -39.08577 | 2026-09-30 15:29:00 | NPP-375 | CANDEAL | BAHIA | Brasil | 2906402 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8505a026-abf5-3ba9-a41d-a51485aec233 | -8.14416 | -36.24675 | 2026-09-30 15:29:00 | NPP-375 | BREJO DA MADRE DE DEUS | PERNAMBUCO | Brasil | 2602605 | 26 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 43f9f053-1e1c-3e6c-ba57-c876406776d9 | -9.32362 | -37.80014 | 2026-09-30 15:29:00 | NPP-375 | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 2424fba6-102a-381f-9568-26d0f28423e6 | -8.35343 | -36.33145 | 2026-09-30 15:29:00 | NPP-375 | TACAIMBÓ | PERNAMBUCO | Brasil | 2614709 | 26 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 004ca7bf-49c2-357d-9f87-ec076f1fc06f | -8.21421 | -35.91272 | 2026-09-30 15:29:00 | NPP-375 | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 065d5526-9be6-3abe-956d-b8dfe49bd713 | -8.30595 | -39.38393 | 2026-09-30 15:29:00 | NPP-375 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 6.4 |
| a67ca8c9-e14e-36b3-a374-f359179f9782 | -10.24918 | -37.4339 | 2026-09-30 15:29:00 | NPP-375 | NOSSA SENHORA DA GLÓRIA | SERGIPE | Brasil | 2804508 | 28 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 2c12652c-e5a3-3a36-9406-08c807d71a68 | -8.14129 | -36.24714 | 2026-09-30 15:29:00 | NPP-375 | BREJO DA MADRE DE DEUS | PERNAMBUCO | Brasil | 2602605 | 26 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 44d65151-2b14-3dd4-9ae9-47b0a431fbff | -7.3462 | -37.3265 | 2026-09-30 15:29:00 | NPP-375 | BREJINHO | PERNAMBUCO | Brasil | 2602506 | 26 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 51a1a56f-e84d-3528-b1c4-3a87d5af0be4 | -7.93474 | -36.29239 | 2026-09-30 15:29:00 | NPP-375 | SANTA CRUZ DO CAPIBARIBE | PERNAMBUCO | Brasil | 2612505 | 26 | 33 | nan | nan | nan | Caatinga | 14.1 |
| cfdff859-263b-3540-8442-ffd9e3f79152 | -8.10367 | -39.44371 | 2026-09-30 15:29:00 | NPP-375 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 10.0 |
| b65fed34-ce17-3584-a0c5-bd56b62d90f3 | -11.77405 | -39.09257 | 2026-09-30 15:29:00 | NPP-375 | CANDEAL | BAHIA | Brasil | 2906402 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1d395797-835e-3f71-8586-af165b80beb6 | -9.38677 | -36.98605 | 2026-09-30 15:29:00 | NPP-375 | CACIMBINHAS | ALAGOAS | Brasil | 2701209 | 27 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 58dc1082-96f6-3c1a-a7ba-6694a236e5ba | -6.69836 | -36.42638 | 2026-09-30 15:29:00 | NPP-375 | NOVA PALMEIRA | PARAÍBA | Brasil | 2510303 | 25 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9a96e1cb-4a06-3af1-8964-3951450ddc28 | -8.14368 | -36.24294 | 2026-09-30 15:29:00 | NPP-375 | BREJO DA MADRE DE DEUS | PERNAMBUCO | Brasil | 2602605 | 26 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 9622ce43-a780-3eb4-88b5-65ad78768a1f | -8.35857 | -36.32642 | 2026-09-30 15:29:00 | NPP-375 | TACAIMBÓ | PERNAMBUCO | Brasil | 2614709 | 26 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 6b0011bd-0fc9-33b5-a2a1-18c1002d5dc5 | -8.0952 | -40.44309 | 2026-09-30 15:29:00 | NPP-375 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 4b971ddf-c7af-3e50-9a08-1b63cc6d570b | -7.93764 | -36.29182 | 2026-09-30 15:29:00 | NPP-375 | SANTA CRUZ DO CAPIBARIBE | PERNAMBUCO | Brasil | 2612505 | 26 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 80b0f52d-048c-3819-90c3-bb7da160f2b6 | -8.02964 | -37.84211 | 2026-09-30 15:29:00 | NPP-375 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 19.4 |
| ea61a5e7-49dd-3914-87fb-97ff8ef61283 | -7.43695 | -37.09682 | 2026-09-30 15:29:00 | NPP-375 | ITAPETIM | PERNAMBUCO | Brasil | 2607703 | 26 | 33 | nan | nan | nan | Caatinga | 3.9 |
| bbc73f54-cff7-3c3a-a96e-5514afad99b4 | -9.87609 | -37.36671 | 2026-09-30 15:29:00 | NPP-375 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 998f6171-e45c-35ee-9c77-6be8d3b49108 | -8.02897 | -37.83702 | 2026-09-30 15:29:00 | NPP-375 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 30.5 |
| f7bad77a-d136-3d8c-86e2-997bd31d1407 | -6.70027 | -36.42622 | 2026-09-30 15:29:00 | NPP-375 | NOVA PALMEIRA | PARAÍBA | Brasil | 2510303 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0c9cb514-d88c-3fd3-821b-867c0858cef1 | -7.44089 | -37.0969 | 2026-09-30 15:29:00 | NPP-375 | ITAPETIM | PERNAMBUCO | Brasil | 2607703 | 26 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 1594e4bd-94ad-30cb-ba67-6cef6cd49bda | -9.28601 | -35.69012 | 2026-09-30 15:29:00 | NPP-375 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 6c00b4c9-b687-3821-b86a-3ddd937dba69 | -8.14078 | -36.24333 | 2026-09-30 15:29:00 | NPP-375 | BREJO DA MADRE DE DEUS | PERNAMBUCO | Brasil | 2602605 | 26 | 33 | nan | nan | nan | Caatinga | 12.1 |
| bf9041bd-d6b4-36e2-af42-6de3e6ca3cda | -7.19152 | -36.99354 | 2026-09-30 15:29:00 | NPP-375 | TAPEROÁ | PARAÍBA | Brasil | 2516508 | 25 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 9830b48b-50cd-3f38-9c91-4fa79bdcde80 | -8.61127 | -36.4945 | 2026-09-30 15:29:00 | NPP-375 | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 9e4ed6ae-1c81-34fa-9de7-74ee61f44590 | -9.38625 | -36.98201 | 2026-09-30 15:29:00 | NPP-375 | CACIMBINHAS | ALAGOAS | Brasil | 2701209 | 27 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 1368ea31-527f-388e-bbe3-21d835e3113a | -8.02627 | -37.83937 | 2026-09-30 15:29:00 | NPP-375 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 34.3 |
| e9de137b-6407-3c6b-b6bc-73fba1779729 | -8.35291 | -36.32748 | 2026-09-30 15:29:00 | NPP-375 | TACAIMBÓ | PERNAMBUCO | Brasil | 2614709 | 26 | 33 | nan | nan | nan | Caatinga | 6.5 |
| b73ddc37-98b8-31cb-b3f4-e836928a8179 | -7.1927 | -36.99519 | 2026-09-30 15:29:00 | NPP-375 | TAPEROÁ | PARAÍBA | Brasil | 2516508 | 25 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 3e508d6c-4fe8-3463-ada0-b965763a2fd6 | -5.91985 | -35.20121 | 2026-09-30 15:29:00 | NPP-375 | PARNAMIRIM | RIO GRANDE DO NORTE | Brasil | 2403251 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 88b7c339-e880-3026-8105-f471556b548d | -8.61075 | -36.49421 | 2026-09-30 15:29:00 | NPP-375 | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 485dc715-6d19-3f24-9e4c-7a5734490703 | -6.3725 | -37.37689 | 2026-09-30 15:29:00 | NPP-375 | JARDIM DE PIRANHAS | RIO GRANDE DO NORTE | Brasil | 2405603 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8571b03f-b5c4-35f4-89ed-4ef244030bc0 | -7.78659 | -37.64876 | 2026-09-30 15:29:00 | NPP-375 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 67f0ff19-a394-3005-832a-892c7ffc2c5e | -7.34437 | -37.32564 | 2026-09-30 15:29:00 | NPP-375 | BREJINHO | PERNAMBUCO | Brasil | 2602506 | 26 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 0b0f1993-48a0-3af9-9517-8826671c6c5d | -8.22485 | -36.55871 | 2026-09-30 15:29:00 | NPP-375 | BELO JARDIM | PERNAMBUCO | Brasil | 2601706 | 26 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 62315011-954f-3e43-8cde-c1ebf28c45ca | -12.17408 | -38.59863 | 2026-09-30 15:29:00 | NPP-375 | PEDRÃO | BAHIA | Brasil | 2924108 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 43aa185c-7913-38ec-8081-4630fc85052a | -9.35622 | -36.01551 | 2026-09-30 15:29:00 | NPP-375 | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| e0e19898-9dc4-3b0d-8d3b-77894d59b784 | -8.62413 | -37.29949 | 2026-09-30 15:29:00 | NPP-375 | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 11656ea2-a7f3-31eb-9854-649ee60faef8 | -9.7925 | -36.89919 | 2026-09-30 15:29:00 | NPP-375 | GIRAU DO PONCIANO | ALAGOAS | Brasil | 2702900 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0d435da9-bc3d-3f49-8046-6009c95cff8b | -8.49954 | -36.76764 | 2026-09-30 15:29:00 | NPP-375 | ALAGOINHA | PERNAMBUCO | Brasil | 2600609 | 26 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f7b0eed0-2e08-31e8-859a-7332382964cc | -8.62433 | -37.30093 | 2026-09-30 15:29:00 | NPP-375 | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1d8a7370-b8ee-3477-a059-6e1b63aae7cf | -8.21342 | -35.91562 | 2026-09-30 15:29:00 | NPP-375 | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| b89e8c4b-16be-36e8-80ea-5b0181e88bf7 | -8.79901 | -36.72108 | 2026-09-30 15:29:00 | NPP-375 | CAETÉS | PERNAMBUCO | Brasil | 2603207 | 26 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 50bbb478-d105-3ce5-ad60-4abe61daadf0 | -11.77659 | -39.08697 | 2026-09-30 15:29:00 | NPP-375 | CANDEAL | BAHIA | Brasil | 2906402 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| a4660a8b-bcc4-3745-8306-1fcb9897cca0 | -1.1901 | -49.084 | 2026-09-30 15:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| b01725d5-240d-334b-b880-032ecb163c8b | -0.8399 | -48.725 | 2026-09-30 15:30:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| b9c05ce7-9760-3230-9186-4e91d6b916cb | 1.6566 | -55.903 | 2026-09-30 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| f4e29e1b-30da-31e2-a672-b1d66212a3e9 | 4.3563 | -59.711 | 2026-09-30 15:30:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 23b79952-f033-3d72-8018-7e6bdff0a8e0 | 1.6565 | -55.9621 | 2026-09-30 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 8377845d-6524-38ab-aecb-47b3d78e5bfb | -8.3805 | -45.3994 | 2026-09-30 15:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 53b719c7-87a3-3bf9-814a-cb750e0f3bff | -1.19 | -49.1053 | 2026-09-30 15:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 372ec567-68b9-3c99-ad83-251d46bb7a36 | -9.0652 | -45.0062 | 2026-09-30 15:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 269.2 |
| f473700b-0b61-33b9-b8b7-50180ddcb4fd | -9.1072 | -67.8326 | 2026-09-30 15:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| c7c91cd4-e44d-3fa7-be61-8443aa82a4f0 | -2.0933 | -49.557 | 2026-09-30 15:30:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 8bf125e9-17c0-31bf-8bf0-e6fa98cd6fc1 | -4.10722 | -38.43603 | 2026-09-30 15:31:00 | NPP-375 | HORIZONTE | CEARÁ | Brasil | 2305233 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| cd16e898-41e6-3b62-8eff-cd53bfa45313 | -4.10245 | -38.43769 | 2026-09-30 15:31:00 | NPP-375 | HORIZONTE | CEARÁ | Brasil | 2305233 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 71362860-8e06-3256-9d61-1215effffe0a | -3.43048 | -39.22757 | 2026-09-30 15:31:00 | NPP-375 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 04e81fb8-9499-3516-abed-5ab9d501425d | -4.61182 | -40.57079 | 2026-09-30 15:31:00 | NPP-375 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 75a853bb-72f2-37ac-9c6b-9e8f4f739c88 | -9.5004 | -66.7831 | 2026-09-30 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| e69fb8d0-899b-390b-a61c-5ca4b6035d45 | 1.6383 | -55.9033 | 2026-09-30 15:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| b2fde8b2-89e0-3bce-aaf5-15fbdaacd778 | -0.8399 | -48.725 | 2026-09-30 15:40:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 0b4a6840-8a57-31a2-a2bd-b2b3dad94a1a | -9.1076 | -67.7215 | 2026-09-30 15:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 94.9 |
| c41457b7-3fa3-3e37-9d3b-443d08e2f214 | 4.3563 | -59.711 | 2026-09-30 15:40:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 9c4380ab-50c4-3d62-943f-8336a21a1fab | -3.6947 | -60.5455 | 2026-09-30 15:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 87.0 |
| d6907085-40e0-3472-b9b1-df224d489825 | 1.6566 | -55.903 | 2026-09-30 15:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 2099d2a1-c064-3362-b475-1fb9bc88404d | -1.1901 | -49.084 | 2026-09-30 15:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| f568d8c7-5162-3b23-9bd6-779474209c18 | 1.675 | -55.9028 | 2026-09-30 15:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| c88fa079-0de7-3b09-8d69-a49b978a3df7 | 1.6565 | -55.9621 | 2026-09-30 15:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 5be4b59d-0639-3cf3-97cb-ac63381a4c34 | -9.4819 | -66.7836 | 2026-09-30 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| ae64061c-e1a4-3eb9-8a61-bf6bae5e8bb9 | -1.2085 | -49.0838 | 2026-09-30 15:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 0149ddd7-e7e7-3cf5-b57f-cb62e8a6f3bb | -9.0987 | -65.3783 | 2026-09-30 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 57996ed8-db9d-352a-aa74-d6c2c699783c | 4.3563 | -59.711 | 2026-09-30 15:50:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 821f783e-96a0-3ad9-8fe7-e7d08b51ed05 | -1.1901 | -49.084 | 2026-09-30 15:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 136.6 |


[Clique aqui para ver as próximas entradas](README74.md)
