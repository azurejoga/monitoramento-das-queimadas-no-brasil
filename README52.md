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
| 28560308-f2a4-3afe-954d-701ae6a71948 | -13.7342 | -60.6471 | 2024-10-07 03:46:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 18b9b217-cc37-38b4-87a9-29bd24888bd6 | -14.0703 | -45.4611 | 2024-10-07 03:46:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 12a1a902-6aa3-321c-af31-c6c8bd175443 | -14.0898 | -45.4577 | 2024-10-07 03:46:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 73.6 |
| c0bf28d2-8e6a-3cc3-b7fd-0b4052b7d140 | -16.4161 | -57.3211 | 2024-10-07 03:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.6 |
| 83d0854c-afd1-3f3f-9779-b951a39292b2 | -16.4164 | -57.3006 | 2024-10-07 03:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.6 |
| 83798ebf-d3d2-3b3d-8b6d-f35c0d5cce33 | -16.4362 | -57.278 | 2024-10-07 03:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.2 |
| 77b2b2d3-eff2-3980-8be1-87e4bec50d67 | -16.4877 | -57.7408 | 2024-10-07 03:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.6 |
| 01a78a66-54f0-3611-ae8a-19187050f4bb | -16.5072 | -57.7387 | 2024-10-07 03:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 127.8 |
| 450960fc-371c-3ac5-9ef4-7465dcbe166c | -16.5075 | -57.7183 | 2024-10-07 03:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.3 |
| 8d798200-2caa-367d-883c-1db3282c0b8e | -16.5267 | -57.7365 | 2024-10-07 03:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 118.9 |
| 5564928d-9b22-3d52-a943-716f10b96dfd | -17.1278 | -56.8074 | 2024-10-07 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 117.3 |
| 5c2f5da7-4d66-3451-895c-c92bbd9c960e | -17.1274 | -56.828 | 2024-10-07 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 122.1 |
| 80cbe5f6-ccb7-390e-9530-171dec5589c5 | -16.9741 | -56.6202 | 2024-10-07 03:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 119.8 |
| 529b21b6-d6ef-336b-b3d3-f9903fda8333 | -16.9744 | -56.5996 | 2024-10-07 03:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 80.4 |
| fb0f8c53-2f35-33f0-a5bc-47c6916e34d2 | -17.0685 | -56.8352 | 2024-10-07 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.9 |
| f8ee303b-f140-3228-98a3-776cdf1dedd6 | -17.1081 | -56.8098 | 2024-10-07 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.6 |
| 2dec45a2-3dc4-3c27-8f59-f66988756e78 | -17.1078 | -56.8304 | 2024-10-07 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.6 |
| e76283bd-1349-3965-a7a6-2365b74bc7d7 | -17.0881 | -56.8328 | 2024-10-07 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.7 |
| ad8b5fe2-9635-3470-a269-ed371676cb76 | -17.1581 | -57.3582 | 2024-10-07 03:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.7 |
| 59159bc4-7afa-3120-bdf5-73f908d2e8cf | -17.1584 | -57.3377 | 2024-10-07 03:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.7 |
| 903c4c0e-95fd-305a-b94b-78d589d9332a | -17.1777 | -57.3559 | 2024-10-07 03:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.1 |
| b2cf6154-830f-3b56-bdf9-aeab3f86a610 | -17.8517 | -53.7799 | 2024-10-07 03:46:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 3e89a3d2-fde2-3a1a-82bb-172720685576 | -17.7922 | -53.7889 | 2024-10-07 03:46:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 162.0 |
| dd1d90cb-3737-3802-b1fd-b6535b5d1185 | -17.7918 | -53.8102 | 2024-10-07 03:46:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 191.8 |
| 3b350895-1762-3c55-b7c2-eea6140a1389 | -17.7724 | -53.7918 | 2024-10-07 03:46:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 82f89052-4e07-3583-9d0d-2c6fe557f422 | -17.772 | -53.8132 | 2024-10-07 03:46:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 79c59894-de5b-38a3-b08c-48e4edf85230 | -17.8319 | -53.7829 | 2024-10-07 03:46:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 125.8 |
| feccac68-051c-30ed-be70-92649cfba7e8 | -17.8314 | -53.8043 | 2024-10-07 03:46:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 1daa4771-2fbc-37d5-b7de-4058073e6773 | -17.8513 | -53.8013 | 2024-10-07 03:46:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 101.4 |
| f20fc9b7-f74e-3947-b095-b46a51d10905 | -18.4718 | -53.5134 | 2024-10-07 03:46:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 1afee446-2001-3b70-ab6d-49e094b923e0 | -18.6391 | -57.2578 | 2024-10-07 03:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.2 |
| 96c60f0f-7c1d-3ed8-9f02-ce5a777d5ee8 | -18.659 | -57.2552 | 2024-10-07 03:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.0 |
| 460be24c-bcb4-3ddf-a76f-35352923f616 | -18.7176 | -57.3097 | 2024-10-07 03:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 133.1 |
| 78ea1441-a97a-320d-9f56-c72c2f8c72b8 | -18.718 | -57.289 | 2024-10-07 03:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.0 |
| 140b4f6e-8baf-305a-8596-013103b9b7cf | -18.7375 | -57.3071 | 2024-10-07 03:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.6 |
| 699ada46-8d20-3422-9e69-1e7a7f7a3baa | -18.7379 | -57.2864 | 2024-10-07 03:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.4 |
| 4d159d54-9106-33c9-bfc7-ec7b8f78b1d4 | -19.8838 | -42.641 | 2024-10-07 03:46:55 | GOES-16 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 67.1 |
| 81c23e9c-841c-3f42-9682-7158b7bccaa2 | -20.4443 | -47.7109 | 2024-10-07 03:46:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 159.1 |
| 0fdd0887-7bdf-352f-9461-42ff12af1543 | -20.4449 | -47.6875 | 2024-10-07 03:46:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 188.4 |
| 64a8dc93-a781-3786-9f2a-8f84eff90dc4 | -20.4655 | -47.6827 | 2024-10-07 03:46:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 147.9 |
| ea31042b-0832-3966-9a25-0b21dd5cbabf | -20.4661 | -47.6592 | 2024-10-07 03:46:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 2762f07d-5b7d-3d9d-b223-f9ae4dbdc90e | -20.5138 | -48.1366 | 2024-10-07 03:46:59 | GOES-16 | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 89a2ab3a-c46e-302f-8c41-cf210a09a28b | -20.5145 | -48.1132 | 2024-10-07 03:46:59 | GOES-16 | SÃO JOAQUIM DA BARRA | SÃO PAULO | Brasil | 3549409 | 35 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 8dfcdb63-2df4-3e17-b264-d70e0f3f0a57 | -20.7621 | -49.4841 | 2024-10-07 03:47:01 | GOES-16 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Cerrado | 88.2 |
| ee46a6fa-98c9-3dcf-ada6-476d3de34c1f | -21.3274 | -47.5939 | 2024-10-07 03:47:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 65.9 |
| afcea741-609b-3596-8dac-eaf496602b15 | -21.5913 | -47.7172 | 2024-10-07 03:47:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 0ac74b63-eb7a-390e-9060-d27786bf2919 | -21.5698 | -47.746 | 2024-10-07 03:47:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 135.3 |
| a29a344b-a81d-3b67-9b74-a2dd85004f31 | -21.5705 | -47.7223 | 2024-10-07 03:47:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 100.1 |
| ad953433-9af5-3bc4-a212-540001a66d15 | -21.5906 | -47.7409 | 2024-10-07 03:47:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 177.8 |
| f95916c0-ec5c-37e7-b8a7-1af584d1ca58 | -21.605 | -47.9485 | 2024-10-07 03:47:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 56.6 |
| b314a2c0-4804-3245-a506-d52ed4ead519 | -2.8753 | -52.9192 | 2024-10-07 03:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 03e55998-5d1a-3bcb-96a3-0e1901ca8943 | -2.857 | -52.8993 | 2024-10-07 03:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 24c57619-5d81-3cc7-978b-c448a015dc8b | -2.8569 | -52.9197 | 2024-10-07 03:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| a7f33915-278e-3125-8878-b8aa1769d980 | -2.8754 | -52.8989 | 2024-10-07 03:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 44ce3d14-52af-3c21-b4fd-78fd49eeac04 | -4.2729 | -43.737 | 2024-10-07 03:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 5ee19c44-5c25-35f9-b155-526af852e0ec | -8.1945 | -43.717 | 2024-10-07 03:55:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 93.6 |
| e5099663-3e53-3e82-a722-b8892e517579 | -8.1942 | -43.7403 | 2024-10-07 03:55:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 69.4 |
| 1fd321be-30b2-3bab-a01b-c678399b50fb | -10.8754 | -63.9169 | 2024-10-07 03:56:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 2fe45e0a-2b4e-3eb0-9187-d55007537124 | -10.8755 | -63.8979 | 2024-10-07 03:56:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 57.6 |
| c1bd471c-b999-3485-a5a3-96e18247a3b5 | -11.285 | -51.3666 | 2024-10-07 03:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| a382771d-049e-39aa-8ee7-a6c0c69297a3 | -11.2847 | -51.3878 | 2024-10-07 03:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 0778b2dd-8308-3b69-80b7-42880ee24e26 | -11.3037 | -51.3858 | 2024-10-07 03:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| af2e3fe2-0940-33ae-8727-d8a38aeeed7a | -11.304 | -51.3646 | 2024-10-07 03:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 60.3 |
| a574c5e7-de25-30c7-9486-47d3186fc78e | -14.6996 | -45.1389 | 2024-10-07 03:56:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| d0018b7f-2de0-3817-8c0d-716703998a2a | -16.4362 | -57.278 | 2024-10-07 03:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.2 |
| 4aeb7734-7ca3-3415-a2a1-483e66cab130 | -16.5072 | -57.7387 | 2024-10-07 03:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 121.0 |
| 2ebb938a-ae0f-3465-807e-eb0b2c8b2729 | -16.5075 | -57.7183 | 2024-10-07 03:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.4 |
| 8f50e360-8358-394a-8e4a-4f35f5ae1581 | -16.5267 | -57.7365 | 2024-10-07 03:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 113.2 |
| 2f1d59c6-8c59-39f8-86ea-06d1d79999ea | -17.1278 | -56.8074 | 2024-10-07 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 151.2 |
| b3ce27b5-9118-3e87-99d6-ece2692c2c24 | -16.9741 | -56.6202 | 2024-10-07 03:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 100.5 |
| a4df4e86-b5c0-318a-af44-6a9c1ae8d2af | -17.012 | -56.698 | 2024-10-07 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.5 |
| d25f59d5-cee6-31c1-a710-1e733596c05c | -17.0123 | -56.6773 | 2024-10-07 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.7 |
| fdf625cd-a824-3ae1-92cd-982c64c18261 | -17.0319 | -56.6749 | 2024-10-07 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.9 |
| 3c13ae43-0085-3800-9d6e-b548483f8732 | -17.0685 | -56.8352 | 2024-10-07 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.2 |
| 06860eab-c962-3cb7-b712-eec2b331dedd | -17.0881 | -56.8328 | 2024-10-07 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.3 |
| 93b747b1-a8fa-3e8e-b01e-e6a157f8c607 | -17.0982 | -57.4267 | 2024-10-07 03:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.9 |
| 5a33a1a7-6725-3afd-b4bb-d08a0a42b3d5 | -17.0985 | -57.4062 | 2024-10-07 03:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.5 |
| a1422e21-a290-3ce9-9dbd-783826346def | -17.0989 | -57.3857 | 2024-10-07 03:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.4 |
| 39e0eff3-3424-313f-a37d-4aaa42b71fbe | -17.1078 | -56.8304 | 2024-10-07 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.1 |
| b675f37a-3866-3a65-90d5-549c2aa25b43 | -17.1081 | -56.8098 | 2024-10-07 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.1 |
| 37060555-9ac7-3550-93ce-1ba3a057ffa8 | -17.1182 | -57.4039 | 2024-10-07 03:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.8 |
| 13b7809b-ecac-3d48-8a16-ce1c438f1f09 | -17.1185 | -57.3834 | 2024-10-07 03:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.4 |
| 4c23c45c-d821-335e-a66b-541945307650 | -17.1274 | -56.828 | 2024-10-07 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 145.7 |
| e665c04c-47be-37a4-8e0a-9c9d74907b11 | -17.1375 | -57.4221 | 2024-10-07 03:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.0 |
| 1a1a826a-8894-3611-a23a-663d5bbe8b88 | -17.1581 | -57.3582 | 2024-10-07 03:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.9 |
| d997db6e-d1a5-3962-973d-0e3c5d8b3bd7 | -17.1584 | -57.3377 | 2024-10-07 03:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.7 |
| 58ecc7f3-8303-392b-9fe1-7ba5b3fed56f | -17.178 | -57.3354 | 2024-10-07 03:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 44.0 |
| 01bf43d6-6e23-3019-904a-622782eaeafc | -17.1777 | -57.3559 | 2024-10-07 03:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.3 |
| 312d4f86-101d-347a-90d0-db9cf1a1062f | -17.8517 | -53.7799 | 2024-10-07 03:56:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 807ba7ae-5cb3-3591-99df-cb746d9fa35b | -17.8319 | -53.7829 | 2024-10-07 03:56:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 136.5 |
| ce5dbcdb-2ba0-3e3d-9f8a-d6cef81788df | -17.8314 | -53.8043 | 2024-10-07 03:56:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 98eb84fa-771c-3a17-b02d-a144df5a781a | -17.7922 | -53.7889 | 2024-10-07 03:56:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 179.7 |
| 2568585f-49bf-3019-82a4-1954e75c2162 | -17.7918 | -53.8102 | 2024-10-07 03:56:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 180.3 |
| fd90a5d0-f6ac-345b-8b29-27cec09c94b3 | -17.7724 | -53.7918 | 2024-10-07 03:56:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 3dbfa9e5-8df9-3bb4-8cd3-aceab066b863 | -17.772 | -53.8132 | 2024-10-07 03:56:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 9e19ba56-1ce6-3102-b94f-20869c54c6b4 | -18.4718 | -53.5134 | 2024-10-07 03:56:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 4d1bdccf-28c7-3950-be32-57a49a7faa77 | -18.7375 | -57.3071 | 2024-10-07 03:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.6 |
| 103ab94b-04a5-3c97-9a07-2082c5a5777d | -18.7379 | -57.2864 | 2024-10-07 03:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 42.3 |
| 11a2a3b0-2606-3f17-9678-7a6c060f0354 | -18.6391 | -57.2578 | 2024-10-07 03:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.2 |
| 6ea7f30f-7f65-3576-a341-ca61a681b284 | -18.659 | -57.2552 | 2024-10-07 03:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.3 |


[Clique aqui para ver as próximas entradas](README53.md)
