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
| 2a67346b-f509-3a20-86f9-75d614a2b8dd | -16.96016 | -57.43517 | 2024-10-11 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ac506a29-4384-327a-849e-2e32a8451164 | -16.95954 | -57.43822 | 2024-10-11 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ec013b80-4f91-3a90-9450-9cce20fdb2eb | -16.95452 | -57.4371 | 2024-10-11 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 99945adb-6781-3e4f-9781-42d2783dcac5 | -16.9533 | -57.44321 | 2024-10-11 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| bdd0919c-1325-34b2-8e6f-cc0a0d55fc83 | -16.94705 | -57.4482 | 2024-10-11 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 780a32b5-aa22-379e-8057-9af5e36bd62f | -15.71132 | -59.35253 | 2024-10-11 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52c2df7a-0f43-34ad-905c-cf79d5143ac0 | -15.70559 | -59.35091 | 2024-10-11 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 43c990d1-f96f-3866-b73d-470b85615c6e | -15.70057 | -59.34594 | 2024-10-11 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 68c4e774-9067-38cf-b3f2-f5ca638d61b5 | -15.67109 | -59.34191 | 2024-10-11 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12cfa289-e48e-3550-b843-c51de79342b1 | -15.67028 | -59.34575 | 2024-10-11 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09f48032-bd68-3e22-9362-f148f873dfa8 | -15.6683 | -59.32643 | 2024-10-11 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 004edd59-3040-3afc-8681-3848c7dbfaf0 | -15.66749 | -59.33027 | 2024-10-11 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4edf759-cfa2-37c7-8dac-e43bea98029f | -15.66253 | -59.35371 | 2024-10-11 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7e560e97-eff7-3828-bbad-245c1db55863 | -15.6616 | -59.35815 | 2024-10-11 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1271d61e-6274-3433-8f4f-438456af4208 | -15.66064 | -59.36271 | 2024-10-11 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54a857d2-a1bd-3fff-9055-bbe27be2e912 | -15.65973 | -59.36701 | 2024-10-11 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 981f5e65-21d5-38bc-8f05-57601e9b001f | -15.65031 | -59.38281 | 2024-10-11 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6cb5142-6cf2-31dc-b007-7c8a42ede574 | -15.6445 | -59.38152 | 2024-10-11 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09f78ba0-7eac-3cb0-ad03-f4afddbad7b1 | -15.64009 | -59.40227 | 2024-10-11 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80e57262-80fb-3ef7-869d-d297feb7481e | -15.63947 | -59.38246 | 2024-10-11 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f979df75-7b8f-3a66-808e-c7efd891c2d6 | -15.63921 | -59.40643 | 2024-10-11 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07804579-5783-3495-8af8-83fb512a4eb4 | -15.63875 | -59.38595 | 2024-10-11 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 413de846-e611-360c-b61f-1dacf72779d2 | -15.63792 | -59.39001 | 2024-10-11 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e11103e5-7fb6-3783-9aeb-c85d16e21d64 | -15.63788 | -59.38403 | 2024-10-11 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 624a2766-a6ef-312e-9c1a-92ca689c604b | -15.63709 | -59.38771 | 2024-10-11 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f477b3c5-a373-306d-8574-4f92b5edfa64 | -15.63699 | -59.39452 | 2024-10-11 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e41ddb5-0f0c-32fb-9bcb-1d0faec69e39 | -15.63616 | -59.3921 | 2024-10-11 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24390582-d23b-3254-b418-a54a590e167f | -15.63603 | -59.39923 | 2024-10-11 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1e5e83de-f07b-3345-ab01-dd1f119d6d12 | -15.63518 | -59.39671 | 2024-10-11 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb1af839-e99c-351a-b654-22fe9a061196 | -15.63508 | -59.40384 | 2024-10-11 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| efaf0097-c1dd-3f49-a4af-8093c1fb16f7 | -15.63428 | -59.40775 | 2024-10-11 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dc330b70-4d76-3b7f-bddd-8e62b421ae8b | -15.63344 | -59.41181 | 2024-10-11 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e19679d7-63df-3352-8e23-c95180a54f3f | -15.63253 | -59.41628 | 2024-10-11 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| edd7ea31-d625-360f-af53-2fc17a16e5f2 | -15.63244 | -59.40961 | 2024-10-11 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c1abde6-2cb4-3423-9fe2-6a35a6301eac | -15.63152 | -59.41393 | 2024-10-11 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2f27af4-cefb-392e-9138-0a6f2f37d29c | -15.62973 | -59.42237 | 2024-10-11 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 210734b4-a2b4-3d75-96e6-dc5ba9b650e1 | -15.62922 | -59.43237 | 2024-10-11 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b5a83e3-82b0-3ae7-a447-9ba0844e1a15 | -15.62892 | -59.42615 | 2024-10-11 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf4461ca-a0d7-36fc-b275-8bd76c28492d | -15.6281 | -59.42999 | 2024-10-11 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aeb24216-9f30-356c-8304-3f84a18b7698 | -15.62725 | -59.434 | 2024-10-11 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57d43fdd-1f53-3a7f-813c-b75f1587d993 | -15.43262 | -60.01559 | 2024-10-11 04:27:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57440e20-e1dc-3a07-b4fa-012f7da32357 | -15.4316 | -60.02038 | 2024-10-11 04:27:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8a0db85-2a57-3bdc-88c1-c413579fc3fe | -15.42657 | -60.01418 | 2024-10-11 04:27:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 440c1cdb-689f-34d2-b5fe-54cd8a5db2f4 | -15.42154 | -60.00801 | 2024-10-11 04:27:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6712846f-35ee-33d7-8d54-b62efbcb6dc9 | -15.41447 | -60.01138 | 2024-10-11 04:27:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 48645fe2-01ca-3c9d-b0f1-16ecf8c4a294 | -2.6716 | -53.3502 | 2024-10-11 04:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| e3fa42aa-6350-3b83-b14a-ca82a0a9f081 | -2.6533 | -53.3506 | 2024-10-11 04:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| ac06465d-ce48-39cf-8b28-2c57f08cb330 | -2.8081 | -51.0084 | 2024-10-11 04:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 6e8dc07d-7816-39c2-8c27-8b1dd05727aa | -2.9857 | -52.8961 | 2024-10-11 04:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| a34e4c42-5961-347f-8d0c-4eb9b4bba58d | -2.9857 | -52.9164 | 2024-10-11 04:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 975b5b90-0bd8-372b-af44-f03df1f0c47c | -2.9673 | -52.8966 | 2024-10-11 04:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 48858dcf-e2b9-36a0-b682-ba036fd21941 | -3.1608 | -50.4347 | 2024-10-11 04:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 112.9 |
| c836ae22-21d1-3e85-be78-58b02131a3d4 | -3.1423 | -50.4352 | 2024-10-11 04:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| ee3d0e4a-c99d-30d7-a359-7b6181f97eb2 | -4.0963 | -48.2307 | 2024-10-11 04:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 131.5 |
| b8b8fe18-1bb3-3fe7-9378-f6964263b9ca | -4.0962 | -48.2523 | 2024-10-11 04:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 186.0 |
| af95f8e6-f32f-3198-9d08-65ef3cf211f0 | -4.1149 | -48.2299 | 2024-10-11 04:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 236.0 |
| 0359ba1d-0ad3-39d1-9d76-e82cfba46365 | -4.1148 | -48.2515 | 2024-10-11 04:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 315.6 |
| 0d226bcc-9bc9-3a70-bb52-b043ab58aaf1 | -4.1334 | -48.2291 | 2024-10-11 04:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| d641b966-73c1-3745-b55b-3b43e6551506 | -4.1333 | -48.2507 | 2024-10-11 04:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 221ef087-5322-37b7-89e0-77ff9b81cf22 | -8.4419 | -55.4491 | 2024-10-11 04:35:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| e469c6bd-965f-3045-8734-ff048775668c | -8.4417 | -55.4692 | 2024-10-11 04:35:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 5287f7f6-9d6e-30c7-846e-7dcd29be48dc | -10.7059 | -64.1138 | 2024-10-11 04:36:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 1c297d19-ab82-3be2-a3b0-a85056f9391d | -12.4182 | -53.1544 | 2024-10-11 04:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 11281ea7-3656-3668-a691-e20b511aeccd | -12.9852 | -53.4881 | 2024-10-11 04:36:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 56fa7aa4-11e7-3b24-a156-cbfc7aca4427 | -12.9661 | -53.4902 | 2024-10-11 04:36:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| a2ceda43-0599-36b9-9ffa-dbaecee0086c | -12.9855 | -53.4673 | 2024-10-11 04:36:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| cc5bc91d-ce6b-3551-bffa-a905ff3967f7 | -12.9658 | -53.511 | 2024-10-11 04:36:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 9db9e3f5-dd46-383d-ad39-380c9a3cc1e3 | -13.7346 | -60.6079 | 2024-10-11 04:36:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 6b7743e7-2919-3fb7-9088-2cd85abadceb | -13.9663 | -45.8025 | 2024-10-11 04:36:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 3d6c9a9f-951f-3f8b-b346-c8d59ae09ee5 | -2.6716 | -53.3502 | 2024-10-11 04:45:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 8200f2f3-91c0-361a-9154-a1d8e5097b51 | -2.6533 | -53.3506 | 2024-10-11 04:45:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 936064b1-eda3-35cc-9860-c60ed8152a33 | -2.9673 | -52.8966 | 2024-10-11 04:45:20 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 4d9ec503-1454-3a27-867f-cca45b5f3783 | -2.9673 | -52.9169 | 2024-10-11 04:45:20 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| f408746f-08a4-3a77-88ad-1c9a07eb2526 | -2.8081 | -51.0084 | 2024-10-11 04:45:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 78d8f0c0-216f-3303-8d46-ec375a7eaa17 | -3.1423 | -50.4352 | 2024-10-11 04:45:21 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| bbdacebb-21e3-3f54-8f8c-f8afd4043015 | -2.9857 | -52.8961 | 2024-10-11 04:45:21 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| abda0cbd-4f78-3433-ba56-36168937968b | -2.9857 | -52.9164 | 2024-10-11 04:45:21 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 2e4f2568-dc73-3561-beef-ef1be94a88fb | -3.1608 | -50.4347 | 2024-10-11 04:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 27e7634a-7795-39b8-86f9-58c49d4eb7dd | -3.1607 | -50.4556 | 2024-10-11 04:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| d964888e-0fa3-320e-8780-3dde9510ac99 | -8.4231 | -55.4704 | 2024-10-11 04:45:51 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 3e1afa60-dcb4-3582-aa08-7aa73d4c7f38 | -8.4417 | -55.4692 | 2024-10-11 04:45:52 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| e486f65e-9093-313f-8de6-6d7272cdfe37 | -8.4419 | -55.4491 | 2024-10-11 04:45:52 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 8e3dbdf2-4d16-3c25-9c7d-13fd1a143a8d | -11.2912 | -50.9208 | 2024-10-11 04:46:07 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 9b8f149a-90bb-351c-922e-1659075a7715 | -12.4182 | -53.1544 | 2024-10-11 04:46:13 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| aff94f97-e80e-337f-9502-949013216d17 | -12.9658 | -53.511 | 2024-10-11 04:46:16 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| dff43500-86cf-3f9a-abf0-09cd9c7727f1 | -12.9661 | -53.4902 | 2024-10-11 04:46:16 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 799ff440-f742-3816-997b-95bea3e1117f | -12.9855 | -53.4673 | 2024-10-11 04:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| b0028979-54e8-3fc4-abbc-d81fa0655109 | -12.9852 | -53.4881 | 2024-10-11 04:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 0e7f8458-0a59-3c1d-ad40-a94d7339c4b7 | -12.9849 | -53.5089 | 2024-10-11 04:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| c3c4f88e-51f5-3c34-bad0-29bc85214d9a | -13.7348 | -60.5883 | 2024-10-11 04:46:21 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| b1622656-da54-3800-8f0f-5e1938d9b6ff | -13.7346 | -60.6079 | 2024-10-11 04:46:21 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 875bf42d-e53b-3bb2-a1d1-d022374c088c | -2.6716 | -53.3502 | 2024-10-11 04:55:20 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 06603c03-c0af-3ef9-82fe-3dc1e940e42e | -2.6533 | -53.3506 | 2024-10-11 04:55:20 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 0f3532cb-2be8-3b5c-add7-cfd1ca1f9b9e | -2.9673 | -52.8966 | 2024-10-11 04:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 83226b36-49a5-3619-8a7c-84c9dfd79585 | -2.9857 | -52.9164 | 2024-10-11 04:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 63f7307c-81ce-3f7b-909c-48a280b269da | -2.9857 | -52.8961 | 2024-10-11 04:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| d866786d-fa71-3a85-a666-56ca3ab4750d | -2.9673 | -52.9169 | 2024-10-11 04:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| a59893c3-b325-33eb-80e7-2274eb896548 | -3.1423 | -50.4352 | 2024-10-11 04:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 6a5d5aa6-fdc7-39ef-aebc-51bf551e4e72 | -3.1607 | -50.4556 | 2024-10-11 04:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| b8bbedb9-d4b7-3294-a282-987eff47d5a0 | -3.1608 | -50.4347 | 2024-10-11 04:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |


[Clique aqui para ver as próximas entradas](README74.md)
