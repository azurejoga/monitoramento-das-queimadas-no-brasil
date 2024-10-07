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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4c0a638-9300-3bd3-a990-b590c4e7559f | -17.6283 | -53.088 | 2024-10-07 02:36:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 14255e97-428e-3746-9636-cbc9fdd7d292 | -18.4518 | -53.5165 | 2024-10-07 02:36:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 68fffb64-149b-3e6a-a55d-03a43b07eff6 | -18.4718 | -53.5134 | 2024-10-07 02:36:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 141.4 |
| e9b16a0e-0e7b-3e94-8ccd-77f0b4948ea1 | -18.4722 | -53.4919 | 2024-10-07 02:36:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 61.6 |
| f6e7bf68-d7fe-301b-a125-b160398277ee | -18.6391 | -57.2578 | 2024-10-07 02:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.6 |
| edee33af-c1d0-3bce-bede-64b261091364 | -18.659 | -57.2552 | 2024-10-07 02:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.1 |
| a32bd1f7-68fa-32a1-a6c5-b316a156b2f5 | -19.1963 | -42.5301 | 2024-10-07 02:36:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 69.3 |
| 0ce3a2d4-2d6b-3e62-a94d-8d64d5900165 | -19.2168 | -42.5245 | 2024-10-07 02:36:52 | GOES-16 | BELO ORIENTE | MINAS GERAIS | Brasil | 3106309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 70.2 |
| e1b67380-222c-3ef7-9f9c-6d244992e1b2 | -19.575 | -42.7516 | 2024-10-07 02:36:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 69.2 |
| 672fed78-0fd4-3dc8-9318-67424aacff09 | -20.1223 | -49.0748 | 2024-10-07 02:36:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 96.4 |
| a33591bd-6cff-37e9-b7cb-4d303932255a | -20.1229 | -49.0518 | 2024-10-07 02:36:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 144.9 |
| a8271a01-1e42-3476-bad2-14470f331453 | -20.4449 | -47.6875 | 2024-10-07 02:36:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 171.1 |
| 89b2052f-48e9-3d7e-84d8-b19c073d8812 | -20.4456 | -47.664 | 2024-10-07 02:36:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 150.3 |
| c1bc7bae-748f-31fa-803d-484c9260e045 | -20.4655 | -47.6827 | 2024-10-07 02:36:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 513.1 |
| 733db351-0bde-3129-9a95-8d685cacb754 | -20.4661 | -47.6592 | 2024-10-07 02:36:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 481.4 |
| ad6026b7-1cd9-3798-b082-c9f31e92ec84 | -20.4866 | -47.6544 | 2024-10-07 02:36:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 0a04d9fc-230b-3a78-8f9c-c4ddcf78f3b8 | -20.5848 | -48.5137 | 2024-10-07 02:37:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 7410bd8d-fc66-3a30-b055-e6c1e14a8c75 | -20.5855 | -48.4904 | 2024-10-07 02:37:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 253.6 |
| d385e289-99b5-3799-ba8e-3bf8d4b11405 | -20.6053 | -48.509 | 2024-10-07 02:37:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 125.3 |
| f66e6208-57c2-305e-ba87-8e5e017f6eee | -20.606 | -48.4858 | 2024-10-07 02:37:00 | GOES-16 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 274.0 |
| b3a8cba6-902d-3b4a-8393-677ef9db4ff3 | -21.605 | -47.9485 | 2024-10-07 02:37:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 762a9178-24ed-3887-b71a-c3bd06d3ab21 | -21.5843 | -47.9536 | 2024-10-07 02:37:05 | GOES-16 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 73.4 |
| c9aa9027-745c-30eb-b71b-7e125df2c68e | -1.0365 | -53.7389 | 2024-10-07 02:45:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| e8d9302a-044b-3c2c-a9c3-265ed3e1737e | -2.2297 | -53.7026 | 2024-10-07 02:45:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 77ee4d4b-5771-32a1-b0b0-f828c64b661d | -3.5381 | -65.0229 | 2024-10-07 02:45:26 | GOES-16 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| e37afa2e-2a3c-3a89-af1c-c09192c7001c | -4.2728 | -43.7601 | 2024-10-07 02:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 6eb2eb60-28dc-3e51-8c22-f5988694f9b7 | -4.2729 | -43.737 | 2024-10-07 02:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 87d02d23-641f-3053-a382-a8622089447b | -4.2916 | -43.736 | 2024-10-07 02:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 48.5 |
| af34ef1c-a253-3b4b-b567-5855ce9b2b41 | -10.2707 | -45.5015 | 2024-10-07 02:46:04 | GOES-16 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 95244786-c7c4-3acd-a3fa-776372bb3855 | -10.2711 | -45.4787 | 2024-10-07 02:46:04 | GOES-16 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 62.9 |
| c54c8bbd-e6c8-316f-acb3-33bd8476241a | -10.8337 | -68.3636 | 2024-10-07 02:46:08 | GOES-16 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 3d6a8cfe-5e05-3c7e-8121-6aef235c19c1 | -10.8754 | -63.9169 | 2024-10-07 02:46:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 5323a9f0-bd6c-386d-95e4-ce752e04dac0 | -10.8755 | -63.8979 | 2024-10-07 02:46:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 12b77075-b2f1-3970-bc97-6dcc1da2145a | -11.247 | -51.3706 | 2024-10-07 02:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 93a9204b-0456-380b-950f-291f18256c10 | -11.2657 | -51.3898 | 2024-10-07 02:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 9aeaab15-d008-37e7-8c33-58c81ffb8c79 | -11.266 | -51.3686 | 2024-10-07 02:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 116.7 |
| daa904bb-d44d-3fd6-89cf-3ec952db0361 | -11.2847 | -51.3878 | 2024-10-07 02:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 7fa656c2-e203-3f58-9b41-99e17b1cf8ce | -11.285 | -51.3666 | 2024-10-07 02:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 0eaf295e-95d6-39fa-b594-57eb72a06e8f | -11.3037 | -51.3858 | 2024-10-07 02:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 58.3 |
| ffafb388-c709-3b65-a028-ebad322f7051 | -13.7342 | -60.6471 | 2024-10-07 02:46:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 65b07e30-4a35-3dbc-a758-51f1c2468392 | -16.4161 | -57.3211 | 2024-10-07 02:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.8 |
| 94526bb1-82de-3f25-8c70-c2a4983675be | -16.4164 | -57.3006 | 2024-10-07 02:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.8 |
| 31bfea2b-9a73-3b18-a1f9-b9cfaed5c4a3 | -16.4167 | -57.2802 | 2024-10-07 02:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.9 |
| 74497f3c-9ebb-3904-8c7f-26248fb235f5 | -16.4362 | -57.278 | 2024-10-07 02:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.7 |
| 15d2091d-408a-35f9-90fb-a23e80ab82d5 | -16.4365 | -57.2575 | 2024-10-07 02:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.9 |
| 42b9e78d-e4b3-3dce-8312-6ef658308596 | -16.4948 | -57.2713 | 2024-10-07 02:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.4 |
| ae04747a-1e9d-3b48-9bfb-e5732203cde5 | -16.6335 | -57.1328 | 2024-10-07 02:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.3 |
| fcdbde4f-e721-3a90-aa81-50c60924f681 | -16.6136 | -57.1555 | 2024-10-07 02:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 122.2 |
| cf9c8c2e-efe0-39a8-9937-f0cc0c3b1ef1 | -16.6332 | -57.1533 | 2024-10-07 02:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 155.5 |
| 606991df-8ce5-3994-8112-3c3b0a68c521 | -16.614 | -57.135 | 2024-10-07 02:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.9 |
| 9bfbbbe5-d9de-3065-bb6a-2ff1eeee5661 | -17.02 | -55.0791 | 2024-10-07 02:46:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 83302eb0-cfaa-30c4-ae7a-5ced40db3edf | -17.1278 | -56.8074 | 2024-10-07 02:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 117.0 |
| be7d17ce-f875-3445-9912-7fb1221248db | -17.1274 | -56.828 | 2024-10-07 02:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 132.7 |
| f3662168-2b2d-3ab6-a831-1e2c4ab122b9 | -17.1078 | -56.8304 | 2024-10-07 02:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 122.2 |
| ad1fdbe9-31c1-39a7-a6d2-12990e70ae13 | -17.0985 | -57.4062 | 2024-10-07 02:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 124.5 |
| d1b9b933-90bb-3564-ac0d-7a4d217e48dd | -17.0982 | -57.4267 | 2024-10-07 02:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 135.0 |
| 24f07834-1385-3dac-86db-d5daf50e39f1 | -17.0881 | -56.8328 | 2024-10-07 02:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 129.5 |
| 4e7b28e3-1807-3a11-ae09-6fab2fdaaa2b | -17.0685 | -56.8352 | 2024-10-07 02:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.9 |
| c799058f-b19c-309b-8fe4-158683d2da13 | -17.012 | -56.698 | 2024-10-07 02:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.8 |
| 95166aab-d52b-37da-92ff-361a7377e0ac | -17.1584 | -57.3377 | 2024-10-07 02:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.5 |
| ea15a19a-965d-3d06-8ca5-5325e6150873 | -17.1581 | -57.3582 | 2024-10-07 02:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 123.0 |
| 20427d7f-829f-36cf-b49f-24e12e25545f | -17.1571 | -57.4198 | 2024-10-07 02:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.3 |
| dd279951-54dc-3d30-b592-9f6b97e669fc | -17.1375 | -57.4221 | 2024-10-07 02:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.1 |
| c76e7b3d-7f9a-3891-b6ae-6c4c8337b14d | -17.6279 | -53.1094 | 2024-10-07 02:46:45 | GOES-16 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 229.2 |
| b1703b90-e7fd-3f77-9f61-0bfdc5fbacb0 | -17.6283 | -53.088 | 2024-10-07 02:46:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 188.1 |
| 2b03b752-1325-3384-b575-9bf9bf51e3db | -17.6477 | -53.1064 | 2024-10-07 02:46:45 | GOES-16 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 64.4 |
| c99db7a8-be85-3686-ad46-701aee2ea4b6 | -17.6481 | -53.0849 | 2024-10-07 02:46:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 70.0 |
| bc35d814-f22b-33f7-af83-090c99e78542 | -17.6679 | -53.0819 | 2024-10-07 02:46:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 51.8 |
| ee8f5a7a-8245-3332-bde6-85403e534062 | -18.301 | -47.1425 | 2024-10-07 02:46:48 | GOES-16 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 100.0 |
| ee3a74f6-7282-30b0-ad01-a5bb3688c5cb | -18.4518 | -53.5165 | 2024-10-07 02:46:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 99.8 |
| a377ad5a-67c5-3640-9097-30f06f19106f | -18.4718 | -53.5134 | 2024-10-07 02:46:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 119.3 |
| fd899719-fb59-376a-8369-23930353021d | -18.6387 | -57.2785 | 2024-10-07 02:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.2 |
| 30979103-bc7f-3bdd-b973-0c00e78792aa | -18.6391 | -57.2578 | 2024-10-07 02:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.5 |
| d6aca20e-4056-362c-93e8-2ca8de432b56 | -18.659 | -57.2552 | 2024-10-07 02:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.4 |
| e189b4d6-da46-38a1-8943-5c949abaadca | -18.7176 | -57.3097 | 2024-10-07 02:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.7 |
| 50907cb0-6509-3d2a-a496-3e950de96c6f | -18.718 | -57.289 | 2024-10-07 02:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.4 |
| d8c26f04-dedd-3bd6-99fb-3e866200868e | -18.8886 | -54.5587 | 2024-10-07 02:46:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 7ed0d33f-90f0-35cb-a495-1984647d11c9 | -19.1963 | -42.5301 | 2024-10-07 02:46:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.2 |
| 63653551-5062-3a62-b353-82f75a59dde7 | -19.2168 | -42.5245 | 2024-10-07 02:46:52 | GOES-16 | BELO ORIENTE | MINAS GERAIS | Brasil | 3106309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 94.0 |
| 5b4e8d8c-cc82-38c5-91f8-37b604338fcd | -19.8318 | -42.3542 | 2024-10-07 02:46:55 | GOES-16 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 70.3 |
| 27fae0e9-6c81-3d30-a8a0-e4fa36487574 | -20.1223 | -49.0748 | 2024-10-07 02:46:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 91.8 |
| cc1893bc-bc2e-3a9e-92a1-82026cef0cea | -20.1229 | -49.0518 | 2024-10-07 02:46:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 206.5 |
| e3c555b9-013e-3ea8-b0b0-464592f9c564 | -20.4449 | -47.6875 | 2024-10-07 02:46:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 244.0 |
| a78a0ece-38fa-34e4-a1e6-981f491e7010 | -20.4456 | -47.664 | 2024-10-07 02:46:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 181.5 |
| 937428f9-ee6c-3261-85eb-8f459598b2d8 | -20.4655 | -47.6827 | 2024-10-07 02:46:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 362.2 |
| 64c82c8d-3cfd-3668-9a45-b87119feaace | -20.4661 | -47.6592 | 2024-10-07 02:46:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 365.6 |
| b6e770a4-f4b1-3452-94f2-ad859058a639 | -20.486 | -47.6779 | 2024-10-07 02:46:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 43b09024-7e74-38d1-a059-f9d52f3bc23f | -20.4866 | -47.6544 | 2024-10-07 02:46:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 83bbe54c-928f-31b3-91c8-93fadaf4a888 | -20.5848 | -48.5137 | 2024-10-07 02:47:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 219.3 |
| 9ed74bf7-5ed0-3849-91e0-f972ba50bedd | -20.5855 | -48.4904 | 2024-10-07 02:47:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 399.1 |
| c74fd506-9d47-3b2d-a1a6-781605a2e3a5 | -20.6053 | -48.509 | 2024-10-07 02:47:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 176.1 |
| a9db2d40-27b1-3fef-b4cb-3b22def540d5 | -20.606 | -48.4858 | 2024-10-07 02:47:00 | GOES-16 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 417.0 |
| 9419ca75-db57-3097-aab2-a2358bad2cb0 | -20.6066 | -48.4626 | 2024-10-07 02:47:00 | GOES-16 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 80.0 |
| eab33478-fcc7-380a-8868-52bc1f9a1c0a | -21.5843 | -47.9536 | 2024-10-07 02:47:05 | GOES-16 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 37a58572-c7e5-37c0-ad28-63d58083baef | -21.605 | -47.9485 | 2024-10-07 02:47:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 88b5c395-c467-3fdb-a488-ca255b0e9b94 | -1.0365 | -53.7389 | 2024-10-07 02:55:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 524255b8-8bd2-3934-8492-d65f48bafaef | -4.2728 | -43.7601 | 2024-10-07 02:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| e1a463b2-060b-3c36-816d-8692fe2aaa56 | -4.2729 | -43.737 | 2024-10-07 02:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 039a6192-f295-3cab-b739-60b7573046fb | -4.2916 | -43.736 | 2024-10-07 02:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 76d887e7-0c17-39a5-a263-0989f2b341c8 | -10.8754 | -63.9169 | 2024-10-07 02:56:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.0 |


[Clique aqui para ver as próximas entradas](README37.md)
