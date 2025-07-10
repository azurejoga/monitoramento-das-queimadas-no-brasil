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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6df4054e-ba90-3519-9bd8-142ca110f42e | -7.9545 | -49.64818 | 2025-07-10 05:18:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 176a866f-ebb6-3c18-b272-a5c35a26209d | -12.57145 | -48.88232 | 2025-07-10 05:18:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87216650-b1f2-39cb-bfc7-21165237bea8 | -8.96147 | -49.85321 | 2025-07-10 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b0fc8932-1d56-3d75-8ad7-6d9842c14cf5 | -8.15932 | -62.76984 | 2025-07-10 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a47f5d5-0c21-36c7-b333-95f0802ba016 | -6.62778 | -56.28188 | 2025-07-10 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48b5351f-42c0-3140-a97d-0e88b0cd75e6 | -8.5025 | -43.285 | 2025-07-10 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 188.3 |
| ee0ae3ac-c9d1-3199-bb07-05469d3eda6a | -8.5028 | -43.2614 | 2025-07-10 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.5 |
| 5ae7de9b-92bc-3e71-bfb2-1fc2c0da40e7 | -8.5022 | -43.3085 | 2025-07-10 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 242.5 |
| b7928f88-4946-3983-98fa-c0ca34bf3dbb | -10.5773 | -49.1533 | 2025-07-10 05:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| cfc9712d-c9a9-34ae-b4ce-d37b32a1b998 | -8.5018 | -43.332 | 2025-07-10 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 95.2 |
| 8c8d72d2-47c5-33df-974f-0f568fa0c15e | -10.5776 | -49.1316 | 2025-07-10 05:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| c17f416e-0113-3ce5-8ded-8b3acf90da90 | -8.5214 | -43.2828 | 2025-07-10 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.4 |
| 935909c5-4bed-3765-ad22-b3bc5446930e | -8.5211 | -43.3063 | 2025-07-10 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 0dca7847-f126-3dda-97ee-ee783fe49685 | -15.89159 | -58.56026 | 2025-07-10 05:21:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9c988fee-9912-3c81-b0c5-54e5e5af2903 | -19.45414 | -48.53931 | 2025-07-10 05:21:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 047314ce-0fdb-3675-847a-532a9462c1fc | -14.2486 | -58.42833 | 2025-07-10 05:21:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e7c08746-4665-3a28-b76c-f6714eafc27f | -12.10162 | -64.24051 | 2025-07-10 05:21:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0cf78bc7-659f-35e8-a08f-9a2b60b31965 | -18.64336 | -55.7221 | 2025-07-10 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 24a81bbe-0c3e-37f8-9cd6-b3205e040b66 | -12.09713 | -64.24441 | 2025-07-10 05:21:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6d1023b3-c676-3e16-9770-7a3b7893f591 | -13.3469 | -52.88869 | 2025-07-10 05:21:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2086a9f4-e991-381f-b667-386e428c190b | -13.34139 | -52.89342 | 2025-07-10 05:21:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4a02e72e-0057-386a-9e9f-12aa808dd39d | -12.10458 | -64.24569 | 2025-07-10 05:21:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 99c5078d-e81b-39dc-88d3-f1f32d1a37f3 | -19.0893 | -56.04878 | 2025-07-10 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a1e1624d-3dd4-39b1-b0b2-f285e07128ee | -17.77847 | -52.43655 | 2025-07-10 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 40b2da83-6430-3cfd-8eab-d64444dcb793 | -18.64766 | -55.7227 | 2025-07-10 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| a71632a3-a9fa-3b12-8660-37a3278bbc06 | -18.65195 | -55.72329 | 2025-07-10 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b8858617-a989-3270-be85-e74340f5742a | -18.4229 | -54.56125 | 2025-07-10 05:21:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 555ebc24-ed92-3649-9c68-3562baa264bc | -12.58155 | -56.98769 | 2025-07-10 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51c5768d-7a6c-3da8-b9c6-cfdf517419a0 | -15.08013 | -48.94343 | 2025-07-10 05:21:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9e1e28e1-0337-3ef5-a227-3494d5a93565 | -19.37464 | -51.39724 | 2025-07-10 05:21:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6566f2e-000c-364e-887a-dcd2af17732a | -18.64818 | -55.71844 | 2025-07-10 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| a1d6d8f0-7087-3f41-bac0-ab003fea0b54 | -19.44559 | -48.54165 | 2025-07-10 05:21:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 89a85804-91cc-3182-8c3e-1bc856e2df50 | -15.03238 | -57.1871 | 2025-07-10 05:21:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 117798b9-4215-3e64-a0b3-4bbabc525613 | -12.10822 | -64.02074 | 2025-07-10 05:21:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4fb63e96-e374-3dc6-b6e6-aac5eec4762a | -12.11116 | -64.02578 | 2025-07-10 05:21:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29618a6b-a1e1-31ac-8891-a42dd0b8028b | -19.45245 | -48.54187 | 2025-07-10 05:21:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 21e869c8-3c6a-3084-83ba-4fb4ad87853a | -17.78416 | -52.43353 | 2025-07-10 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 39cf4da9-b2e7-3784-8e0e-b812ef089422 | -11.78587 | -64.98792 | 2025-07-10 05:21:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3fb0721-0661-3644-a78a-3bfb9d1a7e7a | -11.78197 | -64.98722 | 2025-07-10 05:21:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d792bbe2-057e-3280-acd1-e48682f5cf40 | -12.10748 | -64.02513 | 2025-07-10 05:21:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a7347f3-dd25-3333-94fc-98bdf1e77f43 | -16.06522 | -51.56537 | 2025-07-10 05:21:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 988b4bd8-c555-336c-8941-a915f17e2733 | -13.34207 | -52.88802 | 2025-07-10 05:21:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ce803d00-57f4-3412-8815-712052d4205f | -17.78908 | -52.43742 | 2025-07-10 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f92525b-24e4-3be9-bb51-288b1ec4c555 | -13.34414 | -52.91031 | 2025-07-10 05:21:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a13a19c5-3717-35d6-be41-a317e9086255 | -16.06565 | -51.56158 | 2025-07-10 05:21:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a68695ad-7daf-328d-95e7-1558874d1936 | -12.67356 | -60.28778 | 2025-07-10 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8ddce88-b5ca-38f6-8fce-0f9b2b8f3081 | -17.78846 | -52.4393 | 2025-07-10 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 113a5231-42aa-3abc-921d-3852db9f666a | -19.36889 | -51.39654 | 2025-07-10 05:21:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e56d19ad-f865-3e0c-9d45-593d8566edbe | -17.78378 | -52.43695 | 2025-07-10 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f1efb0c-c9e6-3f7b-9c9d-41e94528109e | -12.67686 | -60.28831 | 2025-07-10 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db075d84-bf3e-3479-bf33-324281aa4aaf | -13.3501 | -52.89538 | 2025-07-10 05:21:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| adf735c7-f080-3a98-a4a7-7f09fab40e5a | -11.78285 | -64.98221 | 2025-07-10 05:21:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a895c5ee-d464-3bc7-bdd7-e6f5034e5181 | -14.72599 | -48.40403 | 2025-07-10 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| aed757ca-ad6d-3ba7-a12e-93b5ee1cb3d4 | -17.86691 | -50.71331 | 2025-07-10 05:21:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 339fbc7d-e0ae-32e4-8795-53f19f674b3a | -17.78946 | -52.43401 | 2025-07-10 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1da5573d-a408-37ae-9972-64ef362710d4 | -19.44727 | -48.53903 | 2025-07-10 05:21:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 80391a52-6da2-359a-87fa-3af45b4ccac3 | -17.87072 | -50.71664 | 2025-07-10 05:21:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d921db7c-4741-38b3-ba67-00ffb9d7bc27 | -13.35102 | -52.89489 | 2025-07-10 05:21:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5640175-c956-3947-beed-f6b3bfeaa364 | -12.10381 | -64.25023 | 2025-07-10 05:21:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b262040d-eaef-3d8a-aa8a-e6bdd741a56d | -14.72505 | -48.40341 | 2025-07-10 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c8572467-4377-3657-ae95-a322f22c301e | -17.8648 | -50.7162 | 2025-07-10 05:21:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec6bedcc-27f8-3f77-b9fd-31583977d95f | -17.78881 | -52.43584 | 2025-07-10 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4597582d-9911-31ad-9f11-7dbde79120cc | -14.78825 | -59.56759 | 2025-07-10 05:21:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f7f34072-013a-36fe-82af-ab81513fc4de | -13.33728 | -52.92574 | 2025-07-10 05:21:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b72ce16-c7cd-3271-a0f8-f251e7c2916a | -12.10086 | -64.24504 | 2025-07-10 05:21:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e7fa6e6f-34cb-33f1-9896-4639d4cb5b4f | -12.02995 | -62.52673 | 2025-07-10 05:21:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b54b9b1c-14c0-3df7-9ab8-5d69be3bede9 | -17.77885 | -52.43314 | 2025-07-10 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a44d98c7-22fe-3619-8e0a-2f9f40ff7b56 | -12.10009 | -64.24959 | 2025-07-10 05:21:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 998165ed-7844-39b7-9d48-5d4311437202 | -13.3462 | -52.89415 | 2025-07-10 05:21:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c9fad621-4643-3826-8590-1d02d662d0f7 | -17.86645 | -50.71775 | 2025-07-10 05:21:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de03b975-c336-3fad-ac27-8475f78b22f1 | -13.34551 | -52.89957 | 2025-07-10 05:21:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c7fc2641-464b-349c-9ad0-4679229625c9 | -21.78009 | -52.7586 | 2025-07-10 05:23:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bc5879f3-21fa-3e07-bc5e-612c8f87b4d8 | -20.96206 | -56.59029 | 2025-07-10 05:23:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a7536eb-8405-3a62-8c49-19f9e6aea74c | -20.96332 | -56.58838 | 2025-07-10 05:23:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c37f309-dcd3-3270-9e5e-d2a3475361ff | -21.76755 | -48.129 | 2025-07-10 05:23:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ff30b24c-ec53-3cdd-9606-c32a196eb1cf | -21.96029 | -56.07431 | 2025-07-10 05:23:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2024d73-e0ad-307a-b326-9ab87dd8f5b3 | -20.9997 | -55.60523 | 2025-07-10 05:23:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26312221-7493-3ac4-837a-e5bc7af1f43e | -21.95979 | -56.07858 | 2025-07-10 05:23:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8160829c-d2e3-3d45-b46e-ff28f1022b04 | -21.43871 | -54.56764 | 2025-07-10 05:23:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a26aceab-6739-3ebd-891f-08bd89c1c3bd | -21.04767 | -54.54869 | 2025-07-10 05:23:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9085880c-5227-36e6-aacc-2a559a952986 | -21.77466 | -52.75795 | 2025-07-10 05:23:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 22667596-7aa5-36d1-aef1-a5a543e448e2 | -21.7644 | -48.12531 | 2025-07-10 05:23:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| de657671-5fe2-36a7-9f64-973558e8ca54 | -21.44294 | -54.57378 | 2025-07-10 05:23:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94544bea-95c8-3381-a04a-0a1c78a108f5 | -22.24417 | -49.6111 | 2025-07-10 05:23:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 99f18e9d-4030-34f2-bf9d-0455720f29e0 | -20.86185 | -55.29608 | 2025-07-10 05:23:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7e6d4b3-57db-3ed1-b257-a03ca69ed8f0 | -21.44235 | -54.57935 | 2025-07-10 05:23:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9fd4927c-e402-36f4-b994-54a92d3cbcc8 | -22.21441 | -56.19715 | 2025-07-10 05:23:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b279d0c-08de-361b-9cb8-64d330decf82 | -8.5028 | -43.2614 | 2025-07-10 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.1 |
| dc61a0cf-fdab-3a7a-9453-ab53b9263e8e | -8.5025 | -43.285 | 2025-07-10 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 162.6 |
| def96d12-3798-3467-a864-5f3a0bef2443 | -8.5211 | -43.3063 | 2025-07-10 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 2b385828-a6a1-3c08-92be-841d24ce8beb | -8.5022 | -43.3085 | 2025-07-10 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 209.3 |
| 82aa00de-463e-3d93-a4fd-2e05f632fd57 | -8.5214 | -43.2828 | 2025-07-10 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.3 |
| a050c3d2-1252-392a-a667-ce26d31c7b62 | -8.5018 | -43.332 | 2025-07-10 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.7 |
| 16bea286-cd9a-322b-af30-705d7a412164 | -10.5776 | -49.1316 | 2025-07-10 05:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| e312d29e-aaba-3d77-afe3-e3451a32016a | -10.5773 | -49.1533 | 2025-07-10 05:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 2422c3b6-01e8-3206-890e-48795cb981cf | -8.5028 | -43.2614 | 2025-07-10 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 54.5 |
| 9286b96f-9433-3d44-8830-ae562516ff8f | -8.5211 | -43.3063 | 2025-07-10 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 4d4527bd-daaa-3b65-95a6-5bc3b2637387 | -8.5022 | -43.3085 | 2025-07-10 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 225.3 |
| f1b93e01-50f5-308b-96fb-0e1f1914335f | -8.5214 | -43.2828 | 2025-07-10 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.2 |
| b1a2b92e-9f7c-3f8d-8046-e41e5bbdb71f | -8.5025 | -43.285 | 2025-07-10 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 163.0 |


[Clique aqui para ver as próximas entradas](README26.md)
