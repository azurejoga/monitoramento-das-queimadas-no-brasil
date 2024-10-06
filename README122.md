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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77e588ac-77b1-34dd-a656-cc6026d117fb | -17.11341 | -56.74812 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ddc1100a-bb47-3db8-9d72-eb7697b0b83b | -17.11336 | -57.38052 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 21.4 |
| bac741d7-3647-3a54-89bf-bfbabef614b7 | -17.11332 | -57.40508 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 3cc76db8-48b4-3a19-8004-aa7b6d68a16c | -17.11288 | -56.80436 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d87fe738-2cb8-3350-a59c-04de40bb8486 | -17.11282 | -56.75237 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 599a1637-d0ec-38a7-89b8-f250f1b43399 | -17.11277 | -57.38452 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 21.4 |
| 1fe830e0-8f11-3a3c-aae9-ab7d3e9eb450 | -17.11274 | -57.40908 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.3 |
| d61603d6-bbcb-3ad2-bbe6-7ddbaa7c4b45 | -17.11223 | -56.75662 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d3489f3e-d108-3a34-a96f-0be5b8e48e81 | -17.11219 | -57.38853 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6c5341f7-9f2e-31b5-af53-84c58e5b4791 | -17.11215 | -57.41307 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 04e68222-1be7-3fd1-9a72-2a4a0820f8fd | -17.11157 | -57.41707 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 2a061bb7-6576-35c7-8c59-ce90b241203e | -17.11102 | -57.39653 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 56e02498-ab47-317b-b2ae-86a181758e19 | -17.11043 | -57.40054 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| d9e3900f-7c1c-365c-8844-4e586d0b4560 | -17.1099 | -56.79958 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 479135b3-4847-3883-9191-097cfa40d69b | -17.10988 | -57.37997 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 29cd39cb-5eef-3d13-81db-0e2e02a8f0c0 | -17.10985 | -57.40453 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 7d564d28-2003-36aa-a961-c7f9d7a1f22f | -17.10929 | -57.38397 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 675d08c0-cd3f-361f-afd2-6df2ba284017 | -17.10926 | -57.40853 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 1e13ef99-2885-3be8-bb42-27a0a6f9fa0f | -17.10872 | -56.80804 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 627340d8-1d95-35f6-9d67-cb3c1ddbe9ee | -17.10868 | -57.41253 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 479a10a8-0913-3509-87ff-e13b1c92fbb4 | -17.10809 | -57.41652 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 147c2864-1e49-3f3b-9884-3a76f8c09648 | -17.10692 | -56.79481 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f40a52b7-52fb-3a49-ae33-75362b446559 | -17.10633 | -56.79904 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 1010cf10-3ceb-35ea-9e7b-59e44a9e726f | -17.1052 | -57.41198 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 953d7284-2708-318b-9141-3e95d8f8e55e | -17.84554 | -57.67996 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| eb7ef5cb-3433-314a-aabc-f6f9901a6f56 | -17.84498 | -57.68393 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 08c6e795-e398-3f1a-a0ee-ba4f38559273 | -17.0281 | -56.71503 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 07ae44a9-8c2a-3172-acb0-a133d70d7840 | -17.02393 | -56.71873 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 36d713b4-83b6-30e5-8d7d-103f8b0817e8 | -17.02333 | -56.72298 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 52502889-8c52-33aa-bc1a-0161ac56055b | -17.02214 | -56.73149 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 6f95e147-6211-3981-a688-3f3bfee876ec | -17.02155 | -56.73574 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| ce649f25-9d8f-335f-92e3-fb50894fa172 | -17.02153 | -56.70966 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 0637dae7-3a78-310f-a32b-e580e1085b38 | -17.02035 | -56.71818 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 02c5870c-4116-3b43-bcab-4ecd765a459b | -17.01795 | -56.70911 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.5 |
| 8854e6b3-353c-3279-a4dc-d0feea244250 | -17.01677 | -56.71762 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 1e9bee43-d1dd-3ff5-8c53-0e8f934d86a6 | -17.01378 | -56.71281 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.5 |
| 89da9a7f-6fb5-360f-ab8d-e901c77f8cc2 | -17.012 | -56.72558 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 2243ea1a-f747-37b1-9718-4593a90050dc | -17.00901 | -56.72077 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 0c06c0e1-8f34-3048-a764-cd39de2fc755 | -17.00366 | -56.73297 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 36142b59-a402-3113-9818-59780b502e33 | -16.99747 | -56.70795 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.8 |
| 14e02ea5-d5da-3d67-8cf3-9f62a73f69e0 | -16.99739 | -56.73398 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.0 |
| d6fdc037-65cb-3b94-b11c-638641f8bac1 | -16.99024 | -56.73288 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 295bb74c-f5d2-3f7c-b328-c4d0277ccbca | -16.85275 | -57.46006 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 57c3b128-e7b3-3ba6-804f-7a2b84b48c23 | -16.84583 | -57.45895 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| dc140c33-83b2-3c2b-92cc-3dcb4ec7e355 | -16.83948 | -57.45391 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 07d85a36-8bad-3eda-9926-4708fd688a5f | -16.83544 | -57.45732 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 10ab6916-9f2d-32ec-b98f-910a1809ae85 | -16.83256 | -57.45282 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| de9b63c6-7523-3307-b586-f5effc1db6e8 | -16.82909 | -57.45227 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 7aa33614-8c3b-3bc2-acb7-51f7741fb627 | -16.82506 | -57.45568 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| e4c17cf5-5bd5-3852-9c52-ba30377f3c2c | -16.82449 | -57.45964 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| a2ee1a23-f71e-3f30-a863-49bd8bbe5e92 | -16.82217 | -57.45118 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| ffb94e98-4907-3b21-8fce-2e61929cc74c | -16.82102 | -57.45909 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| e1127a59-262b-3d99-a32d-cac1a9eb1012 | -16.81927 | -57.44667 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| f6c7c6f0-ba32-339c-896a-1f73d751f7f5 | -16.78924 | -57.43383 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9c273591-4b6a-380e-8d21-7c0b780003fc | -16.78534 | -57.4459 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f518f9f5-5806-388c-9203-56e7179eb758 | -16.77495 | -57.44427 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 1643ddb4-0ecd-3f6b-a891-dfd956f7c391 | -16.77437 | -57.44822 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b6bdbd8c-348c-3b10-bad5-31fb76c5b85b | -16.77321 | -57.45611 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a35475a3-a163-36f0-a472-94e2c75ab869 | -16.77149 | -57.44372 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 97049e77-75cb-366a-b343-a2b2f1c65724 | -16.77147 | -57.46796 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 93659365-f4ac-3f6e-b9a1-397314fd2737 | -16.76803 | -57.44318 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 368c43f8-fe5a-3c5e-86f3-9a228c79a093 | -16.7611 | -57.46632 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2c2860ad-fcb6-3923-9740-ca646401a2bf | -16.72998 | -57.4614 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 8a913eec-ae16-3a94-a4e5-f3351d08a8f7 | -16.71615 | -57.45922 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| dcabec09-79ea-3bbd-8867-dba9f7eb59dd | -16.71326 | -57.45473 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| a5ed86c1-0188-39aa-9828-4108fdf04eb0 | -16.71269 | -57.45867 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3d117b4b-2423-3b0c-bb30-abc1bb6d2588 | -16.70809 | -57.46602 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 8b2ed8ae-eeeb-38e2-a165-cda68d37409c | -16.70805 | -57.44179 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| e289d9fe-26f3-3a27-87dd-969cd9628222 | -16.70463 | -57.46548 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| aac24294-f61a-3f52-927e-53a05623b08f | -18.66265 | -57.26312 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e3a5a2e7-a513-36fe-a4c8-470fdd80dd5d | -16.70061 | -57.46887 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| c31cdc25-a993-35c5-b2a2-b85136618689 | -16.69772 | -57.46438 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 5ee23a02-f646-3010-b268-74ce5541ced1 | -16.69308 | -57.4475 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 7e69f41b-8b73-3ed6-950f-a6a216c7640f | -16.69081 | -57.46329 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c18c3862-f0fe-3876-b0bf-1649c0318858 | -16.69019 | -57.443 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 84efbacb-b5bd-3815-b892-adea0dec7518 | -16.68791 | -57.4588 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 7d82a0c1-7063-37bf-a93c-6f207517827a | -16.68616 | -57.44641 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 9149ef7a-78d6-358b-bdb4-51cf5285156c | -16.68446 | -57.45825 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| f13ff497-3aa6-35d7-be85-6617d271c114 | -16.67777 | -57.46257 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 546ca25f-352d-3681-b59e-2afd2e71ad39 | -16.67719 | -57.4665 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 0644c40f-5e7f-3748-8eb7-59cf6e71f6e3 | -16.67528 | -57.47292 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 185b9de9-2bb9-352b-97b7-556599ffcd00 | -16.67489 | -57.45808 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| e1e81247-5784-32db-8d9c-21e61c0ba657 | -16.67431 | -57.46202 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| fa209fe7-e566-36f0-91e7-14d4b4b98897 | -16.67373 | -57.46595 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 00404846-3fbd-32f1-a7a4-e87522bc2080 | -16.67315 | -57.46989 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| f64f7e81-7f22-3b45-b687-c48feed75b67 | -16.66511 | -57.4525 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5c63b1ce-dbff-3c62-b833-5b00205997d4 | -16.66452 | -57.45644 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2d5b02ad-d7ed-3dd9-90a2-067217d7e376 | -16.92926 | -57.70374 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| e6009728-5c2f-3d77-bc72-957cef6da386 | -16.92583 | -57.70319 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 5747e7e7-4273-3b1a-9a2d-2dbf097c5cd3 | -16.9201 | -57.69431 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 64191039-9095-3f43-bce6-11d0fca569df | -16.91323 | -57.69322 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 94e5fb98-24c3-31fa-a752-ded67e82c0cc | -16.88976 | -57.68552 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c294e6de-92f4-3590-9c3b-28d5c41b17ab | -16.83717 | -57.80505 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 1df159c1-8aab-3547-a568-31122f35f62a | -16.83375 | -57.8045 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| fcbb737d-974e-3162-9603-db06a8acedba | -16.83318 | -57.80835 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| ddf79c99-94ee-3761-bf4c-041de16137a6 | -16.82862 | -57.81551 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f3e994fd-27f1-3f59-9080-cde801b8dea8 | -16.82121 | -57.81827 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e0f720f9-b609-3304-82e8-44c3ffec4cae | -18.65932 | -57.26448 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.4 |
| a31a2457-9a97-3222-90e7-1e4bbd5159b6 | -16.81722 | -57.82158 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| da4dbef1-9c9d-39ae-8519-de8f22719bd4 | -16.81665 | -57.82541 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |


[Clique aqui para ver as próximas entradas](README123.md)
