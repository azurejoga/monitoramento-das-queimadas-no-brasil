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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3503ec1-b966-3dc5-a76b-763ed0ec4526 | -4.27128 | -42.18813 | 2024-10-31 11:57:00 | TERRA_M-M | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 24.0 |
| 7b6ad04e-cc76-338d-ab3f-72b8f76b06a1 | -3.39653 | -41.6344 | 2024-10-31 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 46.5 |
| c0efc35b-45ca-3b78-a53c-332f66f95787 | -10.84783 | -39.6106 | 2024-10-31 11:57:00 | TERRA_M-M | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| dbc6cfa5-e951-3200-9a0b-79fa2e05ff61 | -17.2733 | -57.5085 | 2024-10-31 12:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 101.2 |
| 76190e8f-2540-3e4b-af84-d0b9ef3e8408 | -19.4874 | -56.6437 | 2024-10-31 12:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.7 |
| e1ab36bc-0083-34d6-b5c7-6aae5c4f0f1c | -19.5087 | -56.5779 | 2024-10-31 12:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.9 |
| 127c22cd-e64d-3568-ab92-53eda2b2395d | -19.6268 | -56.6869 | 2024-10-31 12:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 134.1 |
| 65d384cb-0fe5-3adb-94a0-ef4e93f5efe1 | -19.6264 | -56.7079 | 2024-10-31 12:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 148.6 |
| db795467-f77b-3316-bd1f-54ea5a93a278 | -17.2733 | -57.5085 | 2024-10-31 12:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 113.8 |
| 267da14a-76a2-32e1-a322-73059696ccd3 | -17.7246 | -57.5574 | 2024-10-31 12:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.3 |
| cdeea980-b41d-3d94-a0a0-8e54decbf35e | -19.5457 | -56.7402 | 2024-10-31 12:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 153.4 |
| 48673ad3-cad7-3f00-b83f-c1615f8214cc | -19.4874 | -56.6437 | 2024-10-31 12:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.4 |
| c47be0b7-39fa-3538-8120-da28b52608d9 | -19.5087 | -56.5779 | 2024-10-31 12:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.0 |
| ff64fac8-5871-3f15-a017-230055ea877f | -19.6268 | -56.6869 | 2024-10-31 12:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 125.0 |
| bb0a9ed4-1bac-36bd-9492-62106ad61da7 | -19.6264 | -56.7079 | 2024-10-31 12:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 138.5 |
| 8b34f298-6b4c-3f86-93c5-5dc99bca349d | -2.1695 | -48.7466 | 2024-10-31 12:25:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 693e0de7-bc51-3fc3-a64a-117d2f87b791 | -17.2733 | -57.5085 | 2024-10-31 12:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.2 |
| 2d105851-20f4-3327-99e2-5981b750fbba | -19.5087 | -56.5779 | 2024-10-31 12:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.2 |
| 41729a12-0203-3450-81d4-57a4104e9c4d | -19.5083 | -56.5989 | 2024-10-31 12:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.2 |
| 157626e3-81f6-303c-8cf8-da4f9dbc0a29 | -19.4878 | -56.6227 | 2024-10-31 12:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.9 |
| 8325f359-79c2-3e07-a419-53a7b5b95712 | -19.5457 | -56.7402 | 2024-10-31 12:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 123.5 |
| 126dfcd5-0df4-34d4-a83a-c5771b97bec6 | -19.4874 | -56.6437 | 2024-10-31 12:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.8 |
| ab255bc5-f48a-327a-b41d-b98ff8f84b5c | -19.6056 | -56.7528 | 2024-10-31 12:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 172.6 |
| ec1c4974-7c47-3794-8a11-5827b72da27e | -23.9929 | -54.0882 | 2024-10-31 12:27:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 93.9 |
| 362eeef5-d5fc-3a8a-857d-79f56c7811da | -23.9923 | -54.1106 | 2024-10-31 12:27:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 90.7 |
| 0f5c57a5-b024-3436-96c8-35d4e403ea51 | -3.4076 | -41.6432 | 2024-10-31 12:35:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 89.9 |
| 021b204e-b4ad-3e85-895a-1257d08495c2 | -17.2733 | -57.5085 | 2024-10-31 12:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.2 |
| da583c8a-8553-33c9-a219-d0af53a1fd83 | -17.6667 | -57.4822 | 2024-10-31 12:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.7 |
| 209bcd3a-8220-305d-8b91-54ec920d4607 | -17.7246 | -57.5574 | 2024-10-31 12:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.6 |
| 90b97f7c-876b-3253-84c5-267eaf179875 | -17.7249 | -57.5368 | 2024-10-31 12:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.6 |
| 084e99c3-71b7-3182-bca3-c3fb3d7f6672 | -18.0827 | -57.3696 | 2024-10-31 12:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.4 |
| 73600a06-b2c0-3577-b46a-c24a7b678be4 | -19.5457 | -56.7402 | 2024-10-31 12:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.0 |
| f390bbb2-34df-38eb-ab39-79ee6b19eea4 | -19.5083 | -56.5989 | 2024-10-31 12:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.0 |
| 227ff594-26bc-3ccb-92b7-7dd038fcecdd | -19.5087 | -56.5779 | 2024-10-31 12:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.3 |
| 77acdcee-d372-3d22-aa02-6e18f49ae516 | -19.6056 | -56.7528 | 2024-10-31 12:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 171.8 |
| b45193bf-b4ea-38d4-a56f-e3d05bb9e846 | -23.9929 | -54.0882 | 2024-10-31 12:37:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 110.8 |
| 9daf4bdb-a614-3f0c-a707-46a52af188ca | -3.3889 | -41.6441 | 2024-10-31 12:45:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 88.8 |
| 09e69cb8-8e52-38f6-8f42-980a14d8c2a6 | -3.4076 | -41.6432 | 2024-10-31 12:45:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 86.8 |
| 6f099e06-4b42-3226-b766-214a6933d6e3 | -4.2749 | -43.4357 | 2024-10-31 12:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 15ce2d49-4481-3acd-8df5-ceb1e9c1705e | -17.2733 | -57.5085 | 2024-10-31 12:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.8 |
| 3148f391-516f-3d5b-b49d-b711a8ab32ac | -17.2766 | -57.3032 | 2024-10-31 12:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.1 |
| 295c51b8-2362-3937-9bf8-a23446f4c35f | -17.647 | -57.4846 | 2024-10-31 12:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.2 |
| 074dc70b-808f-3192-a6bb-b1a10c076ce4 | -17.6667 | -57.4822 | 2024-10-31 12:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 144.4 |
| 11dcb664-0660-37f0-a9c3-367978e304b8 | -17.7249 | -57.5368 | 2024-10-31 12:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.0 |
| 8f42cd86-3060-3f2f-aa94-d58bac40b7fd | -17.7443 | -57.555 | 2024-10-31 12:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.2 |
| 9dbc786b-4802-39ed-ba93-5d0cc4d1b1f2 | -17.7246 | -57.5574 | 2024-10-31 12:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.6 |
| f66c66a8-6e50-33d4-8ac5-054f86a32127 | -17.7446 | -57.5344 | 2024-10-31 12:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.6 |
| 3d4d32cd-28bf-3926-924a-719194817ef5 | -19.5457 | -56.7402 | 2024-10-31 12:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.7 |
| 03d23db6-9b9a-353c-a304-f8844d4d6d44 | -19.6067 | -56.6898 | 2024-10-31 12:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 104.1 |
| 60199605-3293-3e05-9ea2-812121dec9f7 | -19.5866 | -56.6926 | 2024-10-31 12:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 96.2 |
| ebd33b1e-49c6-3a1d-9d8e-ce749aca5107 | -19.6268 | -56.6869 | 2024-10-31 12:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 132.4 |
| 1f4dcef3-9961-3a51-96b2-46ed996810bb | -23.9929 | -54.0882 | 2024-10-31 12:47:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 119.3 |
| c9900c09-490e-3b70-b32e-9f618563cb8b | -23.9923 | -54.1106 | 2024-10-31 12:47:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 93.2 |
| faa1bee4-75f3-3474-ae39-778fc97c0dc5 | -3.3891 | -41.6201 | 2024-10-31 12:55:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 79.8 |
| ccb5fd7d-2d7d-3b5c-95c2-1475051e643b | -3.3889 | -41.6441 | 2024-10-31 12:55:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 98.5 |
| 9394657b-f19f-3e74-93a7-2f6a652c6211 | -3.4076 | -41.6432 | 2024-10-31 12:55:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 83.4 |
| 32e59e61-cd39-3350-b80b-540c3bf2a404 | -4.2563 | -43.4368 | 2024-10-31 12:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 6bf9435b-e446-398e-8a50-0749d084ed7d | -4.2749 | -43.4357 | 2024-10-31 12:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 154.5 |
| c49645d5-fdc5-3372-b2e6-01a280a4a64b | -4.843 | -42.4871 | 2024-10-31 12:55:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 110.2 |
| af11604b-0cb8-30a0-908c-ffa3e80075b3 | -4.8432 | -42.4634 | 2024-10-31 12:55:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 131.2 |
| 05001426-fe69-36b6-9c50-3c1a70989556 | -17.2733 | -57.5085 | 2024-10-31 12:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.7 |
| 7bdbac17-3f6c-3507-905b-c658782d4e4b | -17.647 | -57.4846 | 2024-10-31 12:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.4 |
| 43ba30a8-9f87-35c3-9a4f-4a867a6aa08b | -17.6667 | -57.4822 | 2024-10-31 12:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 182.0 |
| 4f4b97cf-32d8-3347-bf33-bd9da2b488fb | -17.6664 | -57.5028 | 2024-10-31 12:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.8 |
| 3e16b7b8-fc40-3142-90e3-a2029db1fca0 | -17.7443 | -57.555 | 2024-10-31 12:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.8 |
| 2905459a-e925-3d47-8fd8-f73714658ebe | -17.7446 | -57.5344 | 2024-10-31 12:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.2 |
| a5eb9054-c74c-3059-b65a-63423d8de9e9 | -17.7249 | -57.5368 | 2024-10-31 12:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.9 |
| 76ad8cc0-72aa-31ca-8af0-16df1af684d6 | -17.7246 | -57.5574 | 2024-10-31 12:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 124.1 |
| 455a8f3c-860c-3d5b-83f1-86f58ee0a285 | -18.0827 | -57.3696 | 2024-10-31 12:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.7 |
| 173be7a4-8795-37f3-8ffe-37912272f1f5 | -19.4878 | -56.6227 | 2024-10-31 12:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.7 |
| 02b75102-9ad4-3f89-b91e-d1757b6901fd | -19.4866 | -56.6857 | 2024-10-31 12:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.0 |
| 81bfbb8a-982a-3b99-9c01-bd835ac191e7 | -19.487 | -56.6647 | 2024-10-31 12:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.2 |
| d2257c8b-7667-39e2-b5cb-2578abda0e7c | -19.5067 | -56.6829 | 2024-10-31 12:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 125.6 |
| 6b895ea8-3dd2-3d1a-be08-70026fb31069 | -19.4874 | -56.6437 | 2024-10-31 12:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.6 |
| f486951a-75f5-3aac-9722-b096ff7b35db | -19.4674 | -56.6466 | 2024-10-31 12:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.1 |
| ee73aecc-24d1-3298-8a59-d93c962a69dc | -19.5866 | -56.6926 | 2024-10-31 12:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 101.2 |
| 3b5cd7bd-7d79-3a28-b238-a9a084e180d7 | -19.6268 | -56.6869 | 2024-10-31 12:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 127.0 |
| d985fc37-ecf5-3fb0-b3f5-7a6846fa841f | -19.6067 | -56.6898 | 2024-10-31 12:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 103.1 |
| a1cbd4a5-9ae6-3c6a-bdfd-c6b3d62bace3 | -23.9929 | -54.0882 | 2024-10-31 12:57:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 123.3 |
| f68b4cdc-bd2c-39c1-aabf-eda27ee527ad | -23.9923 | -54.1106 | 2024-10-31 12:57:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 106.5 |
| 3e29250d-647c-3833-ba34-e9d3298ebe02 | -3.3889 | -41.6441 | 2024-10-31 13:05:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 134.8 |
| 71ef8b33-f983-3ce1-a3a9-93d36391ac56 | -3.3891 | -41.6201 | 2024-10-31 13:05:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 86.0 |
| dcfaf785-3cbc-3a76-9170-6efbea8a4a4d | -4.2563 | -43.4368 | 2024-10-31 13:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 3f6baace-056d-39ae-8b9c-00758dc12006 | -4.2749 | -43.4357 | 2024-10-31 13:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 163.7 |
| 3b8beb34-1b6a-30a9-9aa4-39b76ea6ad3e | -4.8432 | -42.4634 | 2024-10-31 13:05:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 165.5 |
| 82c180d4-7526-303b-b846-ed2525f2e7ed | -17.2733 | -57.5085 | 2024-10-31 13:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.7 |
| 668af98b-6f5a-30ec-a36d-1dd5a2e92c92 | -17.2737 | -57.488 | 2024-10-31 13:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.7 |
| ece43b9a-2d21-315e-a9e1-f2c632729ee7 | -17.647 | -57.4846 | 2024-10-31 13:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 119.1 |
| 7e6b4f0c-568f-3791-9522-f6c7c1657c8f | -17.6667 | -57.4822 | 2024-10-31 13:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 252.9 |
| f9744cbe-e1c5-3a80-8930-e65ac12a1fd5 | -17.6664 | -57.5028 | 2024-10-31 13:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.1 |
| 2328f965-7d0c-32c8-ae14-8c1752a8fd2f | -17.7446 | -57.5344 | 2024-10-31 13:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.4 |
| 29824d96-e43a-3ea6-a02d-9356576732dc | -17.7249 | -57.5368 | 2024-10-31 13:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 168.1 |
| d163a843-a6f9-3d10-95b4-b111ea614471 | -17.7246 | -57.5574 | 2024-10-31 13:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 150.1 |
| 1acc8994-941c-3307-bf60-8930386ea716 | -17.7443 | -57.555 | 2024-10-31 13:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.9 |
| ccaf32dc-ab0d-3615-847b-d7da19752aaf | -18.0827 | -57.3696 | 2024-10-31 13:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.2 |
| c9d207e5-f6f8-3b1f-85f6-dac2fe1df5dc | -23.9929 | -54.0882 | 2024-10-31 13:07:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 118.9 |
| e5a51ba6-b35f-3699-80d6-c3c47b425fd0 | -23.9923 | -54.1106 | 2024-10-31 13:07:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 96.3 |
| 2d34129d-352d-333a-94d7-9ccae53af691 | -0.6641 | -62.9309 | 2024-10-31 13:15:10 | GOES-16 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| a83fad56-e336-3fb3-959a-54182d2fc893 | -1.4761 | -54.2164 | 2024-10-31 13:15:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| fa1ce64d-e879-3c12-ab37-483b2afa482a | -2.8049 | -51.9392 | 2024-10-31 13:15:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |


[Clique aqui para ver as próximas entradas](README55.md)
