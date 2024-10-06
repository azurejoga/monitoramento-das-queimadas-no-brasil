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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31ad0842-e75c-3973-97a5-3def53500448 | -7.96206 | -54.76794 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21c16a31-3fbf-304f-acd9-5b98d0af2b2b | -12.1497 | -56.70002 | 2024-10-06 04:19:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e8ea6ec1-60ad-3ddc-ab18-ef6418cf59b9 | -12.14847 | -56.70208 | 2024-10-06 04:19:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8ac8934b-87ae-3468-924f-0a5a042a9a45 | -12.14389 | -56.69883 | 2024-10-06 04:19:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c3ad99f8-06a3-37b5-b1ac-f1c1e945f9c3 | -12.14308 | -56.70303 | 2024-10-06 04:19:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f6b21003-5f1d-36da-8d64-39263dbe657b | -12.14227 | -56.70723 | 2024-10-06 04:19:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1d635c31-6375-31cd-b3fe-763913e69ddd | -12.14182 | -56.70512 | 2024-10-06 04:19:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e34eca9b-eecc-3685-acf1-2829699499b5 | -12.14763 | -56.70629 | 2024-10-06 04:19:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 293502a0-9d15-30bf-8dad-a4aff50b08ab | -12.1435 | -56.69674 | 2024-10-06 04:19:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bf4d7c9c-7f5c-3e64-ba47-9f6d28c01249 | -12.14266 | -56.70093 | 2024-10-06 04:19:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 191adcc7-1ac7-3cb7-ac3e-3ab54ab9c4d3 | -11.91775 | -56.92805 | 2024-10-06 04:19:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ce851da-7771-3643-b7d9-5e38b3a9ca4f | -11.91689 | -56.93238 | 2024-10-06 04:19:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9168d6ad-fad2-3440-bb2d-f1cf059d8218 | -11.91185 | -56.92679 | 2024-10-06 04:19:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 112fb814-8dd6-32ad-9dc6-2d655ac96192 | -11.91099 | -56.93113 | 2024-10-06 04:19:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a43f08e7-c1ec-3b46-8be2-79a1b2ed2f68 | -11.91012 | -56.93548 | 2024-10-06 04:19:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 143639b7-e039-3c14-84e7-49af1bcb30b4 | -11.90592 | -56.92569 | 2024-10-06 04:19:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1ddeab2-cb55-3f87-95bf-b056e70ed013 | -11.90506 | -56.93002 | 2024-10-06 04:19:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73226dc9-ebab-39b3-84a2-2fc97194d2e7 | -11.90419 | -56.93435 | 2024-10-06 04:19:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 283ad282-e080-3c45-a203-0ba635c5fc65 | -11.56194 | -55.66837 | 2024-10-06 04:19:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 083769c0-1ef6-31c1-a38a-d52ad24676e8 | -11.48575 | -56.78822 | 2024-10-06 04:19:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0aa64ba7-e092-3baf-bc04-74831e7f2858 | -11.4849 | -56.79262 | 2024-10-06 04:19:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f6d6d33f-c757-3587-8c7b-c63767f38bea | -12.34385 | -57.37018 | 2024-10-06 04:19:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b7c16fac-b434-3b4f-998f-3d3a8723a2f3 | -12.34326 | -57.36666 | 2024-10-06 04:19:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7751720d-5a99-3e88-a843-82ff2301436f | -12.34236 | -57.37124 | 2024-10-06 04:19:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d35a2b41-3e99-30c4-8710-f30c6f0fa5b8 | -10.21334 | -59.40467 | 2024-10-06 04:19:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8233790-6c1c-38c8-a155-36347cb85b22 | -10.21174 | -59.41246 | 2024-10-06 04:19:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44c790f1-c705-3773-abe5-b8ebf6a43db4 | -12.87461 | -60.52164 | 2024-10-06 04:19:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cf2a05b5-887b-37a9-a876-bdf1471f1b71 | -12.87054 | -60.51657 | 2024-10-06 04:19:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 120bca59-00b4-3923-98ac-5bb4c261336f | -12.86916 | -60.52289 | 2024-10-06 04:19:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 65e9a71e-61af-3535-8a95-481e1bd2478d | -4.94802 | -37.45451 | 2024-10-06 04:19:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 847325e4-4b24-35ea-b678-9bb45e3b9012 | -12.71559 | -40.21758 | 2024-10-06 04:19:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0dcdfcd0-8884-3222-894b-b7afc5b4a66b | -12.71136 | -40.21695 | 2024-10-06 04:19:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 98ff8f0d-6b64-325e-b8e6-91f178a075cd | -13.29264 | -39.91591 | 2024-10-06 04:19:00 | NOAA-20 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a46bcc80-a2d1-31ce-8542-d1d53a48ecbc | -12.25776 | -41.10176 | 2024-10-06 04:19:00 | NOAA-20 | WAGNER | BAHIA | Brasil | 2933406 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6121f53a-1c73-3e2d-b07b-8d93fd8c58ad | -12.25449 | -41.096 | 2024-10-06 04:19:00 | NOAA-20 | WAGNER | BAHIA | Brasil | 2933406 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 11882265-e2f0-34c3-a3a5-a8dcc71dc8cc | -12.25379 | -41.10118 | 2024-10-06 04:19:00 | NOAA-20 | WAGNER | BAHIA | Brasil | 2933406 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 6bc14d5d-d548-3d25-83e8-03acffd273ce | -12.25535 | -41.09922 | 2024-10-06 04:19:00 | NOAA-20 | WAGNER | BAHIA | Brasil | 2933406 | 29 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 4a950cee-e4fc-35df-8ec0-45df75682c78 | -12.25139 | -41.09865 | 2024-10-06 04:19:00 | NOAA-20 | WAGNER | BAHIA | Brasil | 2933406 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ce1a7946-7153-3ab2-9e69-61f6022e5fc4 | -12.24982 | -41.10062 | 2024-10-06 04:19:00 | NOAA-20 | WAGNER | BAHIA | Brasil | 2933406 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 6e9a5fd1-0fab-3b35-88f6-21debb515da3 | -11.99207 | -41.34598 | 2024-10-06 04:19:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a589f75e-abaa-3389-8fe0-52b5ae2eecff | -13.04908 | -40.52319 | 2024-10-06 04:19:00 | NOAA-20 | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8dbeb77b-9aa6-37c1-a639-77fc52863a07 | -14.65711 | -41.96449 | 2024-10-06 04:19:00 | NOAA-20 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 374cdf78-e602-3c8e-bd96-bfd7ea5fada0 | -4.75039 | -40.22113 | 2024-10-06 04:19:00 | NOAA-20 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b4b20862-bc26-37c5-9d0e-0d8d04b03f8a | -10.76735 | -42.68908 | 2024-10-06 04:19:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8de0b713-99df-3115-b01e-a03394fd92a3 | -10.23064 | -42.39317 | 2024-10-06 04:19:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| cbece3e1-8d8b-39cc-a505-cea3bc805a18 | -10.22705 | -42.39263 | 2024-10-06 04:19:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f1fd1faa-23d7-3b54-93b6-47163328bb04 | -10.13059 | -42.42484 | 2024-10-06 04:19:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2bd71cc0-a456-3407-a187-a3a6aacf03e8 | -10.12999 | -42.42898 | 2024-10-06 04:19:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 382039d3-4e68-3664-a424-bb0d6508aa9f | -10.82791 | -42.69826 | 2024-10-06 04:19:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e47e8c6a-861f-3fba-97af-fc49f3e07fff | -10.84071 | -42.85273 | 2024-10-06 04:19:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d538c0f-5722-310a-8c07-427336f219f3 | -10.84012 | -42.85677 | 2024-10-06 04:19:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d64391f-0aa9-332d-aca8-a674efa4fb79 | -10.83776 | -42.84815 | 2024-10-06 04:19:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5dc6f9f-f008-3732-87b4-767ad66ffff4 | -10.83717 | -42.85219 | 2024-10-06 04:19:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24788359-9e9f-3355-9ce9-d8082a2d091d | -10.83304 | -42.85569 | 2024-10-06 04:19:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd772145-01e8-3134-a50e-636fb96334f7 | -10.82951 | -42.85516 | 2024-10-06 04:19:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4bd9def0-cb1f-3c56-821b-31a6f0dc1072 | -13.08965 | -42.41962 | 2024-10-06 04:19:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 4736d4f3-a35c-31f1-b3e2-73557fffd344 | -14.39261 | -42.62035 | 2024-10-06 04:19:00 | NOAA-20 | PINDAÍ | BAHIA | Brasil | 2924504 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 407f5db5-220f-32f6-b5ba-85fe527b9d00 | -16.3471 | -43.69555 | 2024-10-06 04:19:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff43dd10-6839-35d3-a142-07585f6c0a20 | -16.29453 | -43.69377 | 2024-10-06 04:19:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6779914e-c8f4-3a7f-9cdf-cc99ee1168b7 | -16.48252 | -43.81533 | 2024-10-06 04:19:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ca56565-c76a-37dc-8672-f75965a2be69 | -16.68149 | -43.88596 | 2024-10-06 04:19:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25e2c9e9-9a03-3898-8f99-ab21a0b76353 | -5.18183 | -42.80691 | 2024-10-06 04:19:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 366661ec-00bb-34f4-a06a-9a77662598f1 | -3.50004 | -42.33373 | 2024-10-06 04:19:00 | NOAA-20 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 90b3d49c-d7de-3a8b-a02b-0c1f352cfe7a | -3.80383 | -41.59662 | 2024-10-06 04:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e538b05f-46ab-3eb5-8997-bd2237f0b8f5 | -3.80324 | -41.60047 | 2024-10-06 04:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ff97a47e-a62e-3639-baa4-621d0517b562 | -3.80094 | -41.59224 | 2024-10-06 04:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 4a3abff0-00e7-385e-8928-61ef913e1399 | -3.80034 | -41.5961 | 2024-10-06 04:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| aceebfe7-ee72-3595-8344-84185a2b84a7 | -3.79975 | -41.59995 | 2024-10-06 04:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 8aaf8bbb-b89f-3988-ac08-0af3ca7202e9 | -3.79804 | -41.58786 | 2024-10-06 04:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 25c88ebb-16a3-3baf-9a9f-5283354802be | -3.79745 | -41.59172 | 2024-10-06 04:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 63937ef5-4d0a-3dc7-9a0c-4fc973caa3b3 | -3.79685 | -41.59558 | 2024-10-06 04:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 10163a55-2af3-3770-a1d9-5476b204520a | -3.71752 | -41.6819 | 2024-10-06 04:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 951caa19-6873-3fac-9001-283494a093f0 | -3.71405 | -41.68138 | 2024-10-06 04:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 6e30328d-d7e5-3322-8a53-b45354a2c599 | -3.71345 | -41.68519 | 2024-10-06 04:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 1e80d9b6-5c68-356c-a3ce-4fd1b9e17789 | -3.71057 | -41.68085 | 2024-10-06 04:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| f5166526-52a6-3672-839c-868c8636ffd2 | -3.70998 | -41.68466 | 2024-10-06 04:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 1cab2860-6dbc-3108-8d5a-385c9abe70e5 | -4.85198 | -43.17611 | 2024-10-06 04:19:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7017ccd7-e783-312a-89e5-5292dfe3aac1 | -4.85144 | -43.17964 | 2024-10-06 04:19:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9631680-6e8e-38e1-be1c-8b4eb65aff49 | -4.85029 | -43.16499 | 2024-10-06 04:19:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37068e3e-8c4f-32f8-9897-46a9263a9b57 | -4.84974 | -43.16853 | 2024-10-06 04:19:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 935ef37c-9b79-3d8f-80f5-ffc521fd1e58 | -4.84919 | -43.17207 | 2024-10-06 04:19:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c32feef-0124-3fca-941b-fe61396275ff | -4.80931 | -42.77261 | 2024-10-06 04:19:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b295bab2-5ea4-3524-a0ca-53df1407ff24 | -4.80594 | -42.77208 | 2024-10-06 04:19:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 04d71277-5ca1-3c2e-a16a-f9174d60ff75 | -4.80479 | -42.75716 | 2024-10-06 04:19:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cac5c334-b9db-3845-8873-113d2664ab19 | -4.80424 | -42.76075 | 2024-10-06 04:19:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6be79c47-29a5-341a-80e6-d8599279d9d7 | -4.80142 | -42.75665 | 2024-10-06 04:19:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| d0a5cb41-b796-3a57-993f-5a8b94cb2ca7 | -3.55104 | -42.6575 | 2024-10-06 04:19:00 | NOAA-20 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ebd3f63-b250-30bd-9d0e-a197f00f2885 | -5.54991 | -42.78843 | 2024-10-06 04:19:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a0d449f5-4006-30c2-90ea-3746c80d7438 | -5.54936 | -42.79206 | 2024-10-06 04:19:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8af82fca-dc1c-3c73-a5e6-290c340d75b4 | -5.53808 | -42.79776 | 2024-10-06 04:19:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9fe768a7-e2f4-3079-95c9-75628fe0a945 | -5.53469 | -42.79724 | 2024-10-06 04:19:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b16905c6-82f1-3078-bf94-f72ee55ca002 | -5.51093 | -42.78614 | 2024-10-06 04:19:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1210559b-2258-305b-a0c7-02beb7ccb383 | -5.51037 | -42.78976 | 2024-10-06 04:19:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 9d883624-4a46-3003-90c7-626ef0b0bbac | -5.50755 | -42.78562 | 2024-10-06 04:19:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a6cba862-c1ee-3ed6-97e1-f3a75397489a | -5.5036 | -42.78872 | 2024-10-06 04:19:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 75fb3a74-6e6d-3424-b517-272b29169a09 | -5.50021 | -42.78819 | 2024-10-06 04:19:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e2822eaa-e6a2-3fc3-b938-b125bc86830d | -5.49739 | -42.78403 | 2024-10-06 04:19:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 28254b5a-6442-3c87-b45b-3a004420ec36 | -5.49569 | -42.77264 | 2024-10-06 04:19:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 752fa1c2-e1d4-3fb9-b2f0-86e0bdd69303 | -5.40634 | -42.92526 | 2024-10-06 04:19:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b237bab6-8037-3db6-9ac6-becc03ff1d18 | -5.41621 | -43.10662 | 2024-10-06 04:19:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README69.md)
