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
| bc8b73c3-3579-3e53-ac12-639f52132661 | -8.52533 | -44.16038 | 2024-10-14 04:21:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 971e9efe-5a7a-33be-9d40-5d25906f307e | -9.45545 | -44.14895 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b9220b05-57d0-309c-a87c-1293724a2140 | -10.52737 | -44.20733 | 2024-10-14 04:21:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17f69a06-40cd-3f48-a2e5-e13d76b8ed03 | -10.524 | -44.20681 | 2024-10-14 04:21:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36c46746-ec28-390e-a661-2c25a3362b5c | -10.29898 | -43.42204 | 2024-10-14 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 726c3635-d525-3241-9bcc-99c1ea90bf31 | -10.08463 | -44.23504 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f6bd3ca8-33c2-314a-adf8-e91df583d591 | -10.08408 | -44.23863 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5478cb0f-f834-3f07-b3ae-4db6cbcd9943 | -10.08347 | -44.22016 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d107d32-80dc-3da4-abda-9d64ae41f23b | -10.08292 | -44.22375 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9bf63efe-6a56-3d6b-8b87-f55a4e7a3360 | -10.08128 | -44.23452 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 783f8553-aba4-3311-aea4-e54bb4b5eaad | -13.38149 | -44.69591 | 2024-10-14 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| adb16da8-89a5-34f4-83d7-b2316a028c48 | -10.82105 | -44.95127 | 2024-10-14 04:21:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 22166a30-cf8a-3f6f-9e51-2a986ff82d27 | -10.81774 | -44.95074 | 2024-10-14 04:21:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b37aa7e-030c-3e0c-b519-660f07c00cdd | -10.81719 | -44.95427 | 2024-10-14 04:21:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd5726f7-b41e-3aad-af5b-a171bf13f6d1 | -8.50111 | -44.16412 | 2024-10-14 04:21:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1e959d3-b451-35d8-9ac9-b639e27a75ac | -8.4959 | -44.89665 | 2024-10-14 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 56a3d0b3-f509-3cfa-a3de-30b185b3cee1 | -8.40597 | -44.83987 | 2024-10-14 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9b6ecb6-93ee-3c34-b5ef-8c9cff93a42a | -8.40573 | -44.73321 | 2024-10-14 04:21:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43191a6b-0d57-3947-9ee2-da3cac32fba6 | -11.17812 | -39.901 | 2024-10-14 04:21:00 | NOAA-21 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 22599070-5adc-33d0-adbb-c5845e0e8116 | -11.17756 | -39.90502 | 2024-10-14 04:21:00 | NOAA-21 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ad38d9bb-8746-3bc0-b74d-29b8cb577060 | -11.177 | -39.90905 | 2024-10-14 04:21:00 | NOAA-21 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 47d5db18-4af9-38b6-b858-ed5adf4a8060 | -11.17333 | -39.90443 | 2024-10-14 04:21:00 | NOAA-21 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 85890f6f-4805-3f3f-a8f7-0d3126a0c9e5 | -11.17277 | -39.90845 | 2024-10-14 04:21:00 | NOAA-21 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 392bfc1e-466d-3939-aa1e-b2fe0b1af491 | -9.31766 | -40.62136 | 2024-10-14 04:21:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 17b410a4-0a60-30a3-bea8-1473de5382b4 | -9.3476 | -40.86225 | 2024-10-14 04:21:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cf223d9a-7f88-32bb-9d18-1dd741c15afd | -13.28183 | -41.91317 | 2024-10-14 04:21:00 | NOAA-21 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| bc728950-5f36-377d-bde5-eb7f2b015934 | -13.28122 | -41.91747 | 2024-10-14 04:21:00 | NOAA-21 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 0b5fcc99-bb2a-37eb-a8e9-fcb92014ff9a | -13.27797 | -41.91282 | 2024-10-14 04:21:00 | NOAA-21 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c9b57c42-c84b-3b5b-889c-1390443861bf | -13.27735 | -41.91715 | 2024-10-14 04:21:00 | NOAA-21 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 056bf165-4545-35c3-a04c-845718f2500d | -10.4918 | -42.4406 | 2024-10-14 04:21:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 8eac8563-c8d1-3fa5-91b0-138fbbec7458 | -10.49117 | -42.44482 | 2024-10-14 04:21:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 9b5f1c5a-15b0-3fe1-afa9-4b5d944e163c | -10.48883 | -42.43581 | 2024-10-14 04:21:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 0969de0e-5200-3831-a038-25cec627d221 | -10.4882 | -42.44004 | 2024-10-14 04:21:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 7bc3d219-452b-34fe-9d4b-e6fb89e600ad | -10.48758 | -42.44425 | 2024-10-14 04:21:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 5f86426a-6247-3231-9319-6b132365e3bd | -10.48523 | -42.43525 | 2024-10-14 04:21:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| dc840c87-aff4-341f-8c8c-4b00686a8f40 | -10.4846 | -42.43947 | 2024-10-14 04:21:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 1725a162-9ae1-3f8f-a311-9b1593f3c50a | -10.18303 | -42.40224 | 2024-10-14 04:21:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b15d4319-57d9-3495-9c88-2b6acb41496e | -12.10569 | -43.19503 | 2024-10-14 04:21:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7225f107-f2f6-3b3a-9175-f7d099e69817 | -12.10215 | -43.19458 | 2024-10-14 04:21:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| bbeed7ba-caab-3069-95f1-a360a109fd66 | -12.0998 | -43.186 | 2024-10-14 04:21:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 119ddaad-4e98-3de7-ab6f-93976801c0df | -12.09802 | -43.19811 | 2024-10-14 04:21:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f9e4e3d7-38f4-33d3-a780-2c8db96a2f1f | -12.09688 | -43.18132 | 2024-10-14 04:21:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 64335964-4b49-3fff-bad2-560020709839 | -12.09626 | -43.18547 | 2024-10-14 04:21:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1b881e44-ff63-3677-8cb0-2dd16e06a2ed | -12.09566 | -43.18958 | 2024-10-14 04:21:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| eb6bc5ee-2b46-31c0-9068-7da8555fc179 | -14.55329 | -43.13329 | 2024-10-14 04:21:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| da5fca15-4f7f-3e86-b105-e83e7383b43a | -8.45544 | -42.50687 | 2024-10-14 04:21:00 | NOAA-21 | JOÃO COSTA | PIAUÍ | Brasil | 2205359 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 748a1a7c-e8fe-332b-995f-6d766a2abfde | -8.45134 | -42.51029 | 2024-10-14 04:21:00 | NOAA-21 | JOÃO COSTA | PIAUÍ | Brasil | 2205359 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 01db0d35-18a3-3fc6-8170-741b4a0902d6 | -8.45075 | -42.51425 | 2024-10-14 04:21:00 | NOAA-21 | JOÃO COSTA | PIAUÍ | Brasil | 2205359 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2838a17b-d220-3439-8f4c-5af9190cffd8 | -8.44313 | -42.4685 | 2024-10-14 04:21:00 | NOAA-21 | JOÃO COSTA | PIAUÍ | Brasil | 2205359 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 239acdef-8911-3336-b271-3e6609b7145b | -8.44233 | -42.46965 | 2024-10-14 04:21:00 | NOAA-21 | JOÃO COSTA | PIAUÍ | Brasil | 2205359 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| eb51b3bd-0d22-35c6-82af-be244272ca73 | -9.42371 | -44.15494 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 092b1207-0530-3b22-ac92-557365bb28a9 | -10.29841 | -43.42581 | 2024-10-14 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80f0185e-d098-3a35-871f-f6adeff50cdf | -10.29554 | -43.42151 | 2024-10-14 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9048fe8d-a5ba-3df1-86ef-ad1ab2634911 | -10.29497 | -43.42528 | 2024-10-14 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0097c66e-d37b-3596-b0e1-4bcb9fddc3f8 | -10.29441 | -43.42905 | 2024-10-14 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9dffcc15-5f01-38f9-b2b8-5f259afd37cf | -10.11817 | -43.94729 | 2024-10-14 04:21:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| da6d3ad9-7830-35fe-a317-d17ee6076a95 | -10.11761 | -43.95094 | 2024-10-14 04:21:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04cf1d13-14f6-3d9c-98b6-e4c96c4181cf | -10.11706 | -43.95459 | 2024-10-14 04:21:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99ce8287-1f55-3d58-89ae-049392e2c38f | -10.11651 | -43.95823 | 2024-10-14 04:21:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0f6d3358-4a63-300b-9e1e-d7d130324d5c | -10.1159 | -43.93944 | 2024-10-14 04:21:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bef737d8-d218-355c-bd5b-9adef0904997 | -10.11535 | -43.9431 | 2024-10-14 04:21:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 49cb31d2-7b8a-3dbd-ac16-5ef1bce58f95 | -10.11368 | -43.95407 | 2024-10-14 04:21:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9892b28-0f92-3eda-b077-41abb22764f3 | -10.11313 | -43.95771 | 2024-10-14 04:21:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3922ecaa-4a7a-3fbd-9423-5f393a4c77d0 | -10.11258 | -43.96135 | 2024-10-14 04:21:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40735022-b695-379e-8589-18e21564440f | -10.11197 | -43.94257 | 2024-10-14 04:21:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 585bca0b-a60f-348c-a621-7d0fc0182d17 | -10.11142 | -43.94624 | 2024-10-14 04:21:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 56795df3-c618-3413-bdfb-cb812f789a5b | -10.11086 | -43.94989 | 2024-10-14 04:21:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01879a99-bd1c-36b8-89e4-38c8a8622efc | -10.11031 | -43.95355 | 2024-10-14 04:21:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6a8a5b5-ce84-37b9-b989-182e35feae78 | -10.10975 | -43.95719 | 2024-10-14 04:21:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b76ed3d5-fa7c-3eea-ada0-1560252c4398 | -9.45266 | -44.14484 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 239773ae-353b-3611-a9a4-3f2cb26d0975 | -9.45215 | -44.17043 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e4c0174c-b14b-3a32-a825-2d99b02175b1 | -9.45211 | -44.14841 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 24597c9b-582a-3c16-b8d2-1b51cdb110e4 | -9.45046 | -44.15916 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5336966c-c858-3452-8b04-d3633ba4afa5 | -9.44991 | -44.16275 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4f1affb9-4ba3-31ed-8107-f98ee2b81206 | -9.44987 | -44.14071 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8231fc89-a414-34f2-91e3-6d03aea9cc44 | -9.44932 | -44.14429 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e926d7ea-36df-31d1-9357-861128f2828d | -9.44881 | -44.1699 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 03fdcce3-4ce8-383b-b89a-15be6bd7302f | -9.44877 | -44.14787 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9581f68d-3e78-3976-8ddd-62de83df1394 | -9.44822 | -44.15146 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 64fcb8cd-883c-34a7-a1e4-e01db51daaaf | -9.44767 | -44.15505 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9e23961c-e5f0-37e1-8088-d9f331c47149 | -9.44602 | -44.16579 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 05450ee5-eab4-3adf-b175-67984edaf2f5 | -9.44492 | -44.17294 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7fc2ed47-8919-3e77-9f5c-1d62da922c35 | -9.44487 | -44.15093 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d5ab1aae-b190-3b5f-a82e-7761cdd129d8 | -9.44427 | -44.13256 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b7a5e854-1dbd-3576-99c5-1b3dc60a6256 | -9.44213 | -44.16883 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b235270e-5d87-316b-bc10-c358aefc0ecd | -9.44147 | -44.12847 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ad6e481-dda9-3056-b773-0b6dbe3668e8 | -9.44092 | -44.13203 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e011d0a9-cdec-3a06-bd6a-dfe419df71be | -9.44038 | -44.13559 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5c86127f-67d5-33f5-ab37-69ec387ca238 | -9.43654 | -44.16062 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f5e5121a-fc51-3856-b8b2-2638f55772f8 | -9.43429 | -44.15294 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6b8fe8c7-1f4a-37fe-9e57-e038c3e5cd45 | -9.43095 | -44.15242 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 41b51cfa-b12f-3e57-8d0b-8e51bb7726a2 | -9.4293 | -44.16315 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b352f06e-90f2-3f0f-996d-b18646a548ea | -9.42875 | -44.16674 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8001caaa-3986-3428-b8fa-7fc422db7a02 | -9.4282 | -44.17033 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8e6f9bd5-fb43-35cb-8194-3cb8047bd91d | -9.4248 | -44.14782 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 08c30c02-e16b-3394-855f-a2dfddea6581 | -9.42431 | -44.17338 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6b7dee77-1a3b-33d2-a40e-2bf984870bba | -9.42426 | -44.15138 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4a62b27f-96ed-35b1-b8c4-4ddf7739ca7e | -9.42377 | -44.17693 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7402a2d6-bfe8-36c9-b47d-1e64255f51a7 | -9.42316 | -44.15853 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f8e55664-e312-32e4-8aff-2056166bbf79 | -9.42097 | -44.17286 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README53.md)
