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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95503171-7a99-343f-9985-7ce416e3a7fd | -19.621 | -57.0016 | 2024-10-18 04:46:52 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.3 |
| 35b1347c-6c10-321f-af31-dee7f3dffe40 | -19.6005 | -57.0253 | 2024-10-18 04:46:52 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.3 |
| f731fea0-115c-3adb-ba43-ac94f9b01c88 | -19.6009 | -57.0044 | 2024-10-18 04:46:52 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.6 |
| a5095b7e-7605-39b7-9968-0dca130acd49 | -19.6206 | -57.0225 | 2024-10-18 04:46:52 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 137.2 |
| f743bda0-b819-303c-a9b1-655f98cdef61 | -3.6823 | -45.9008 | 2024-10-18 04:55:25 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 20c52a03-7d85-351c-a775-6de123cdc268 | -3.7009 | -45.9 | 2024-10-18 04:55:25 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 08b1116f-3501-32aa-8e57-13c5611e9135 | -4.9583 | -47.0325 | 2024-10-18 04:55:33 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 79f439ac-29b4-30f1-8a2b-8230e1b2af9f | -3.7009 | -45.9 | 2024-10-18 05:05:26 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 77.4 |
| a5510eed-0956-397e-961e-e7b7fd39fb09 | -3.908 | -42.402 | 2024-10-18 05:05:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 55.6 |
| 3223f17b-f388-3159-b0da-cfd6f3d8dcf8 | -4.9583 | -47.0325 | 2024-10-18 05:05:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 62.4 |
| f29460e9-8934-3680-b795-b735f7a062ae | -3.7009 | -45.9 | 2024-10-18 05:15:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 83.3 |
| d18af0e0-af20-399a-b6ef-a7b8a9d47b3c | -18.6575 | -57.3382 | 2024-10-18 06:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.3 |
| 33098a7c-788a-3249-9cd3-c488a5f1bc3c | -19.5808 | -57.0071 | 2024-10-18 06:46:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.7 |
| 26343a92-77b0-337d-96ac-b33f929e5d6d | -12.5147 | -63.3014 | 2024-10-18 06:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.2 |
| d8f5ee2e-3908-384d-8b97-618b7b208744 | -17.2373 | -57.3079 | 2024-10-18 06:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 162.6 |
| 40da5165-d8ff-3702-b1e2-df4edfea0732 | -17.237 | -57.3284 | 2024-10-18 06:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.3 |
| 4db63d40-3aa9-3add-ac07-32b0a61422bd | -17.2177 | -57.3102 | 2024-10-18 06:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.0 |
| 53fe5ef1-839f-3d11-9ae0-99cc88cf7054 | -17.9036 | -57.4534 | 2024-10-18 06:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 124.2 |
| 7dedcac2-7b30-3484-b2cd-6dfdc851a11d | -17.9234 | -57.451 | 2024-10-18 06:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 133.7 |
| aee15629-5e89-3a8c-a54f-fd5f4490c267 | -17.9432 | -57.4486 | 2024-10-18 06:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.4 |
| 2486cb6d-1878-3213-8cc6-f3ffa36014eb | -17.9855 | -57.2786 | 2024-10-18 06:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 131.0 |
| 74e226c1-b82a-31cd-8d04-09a0273e87cd | -17.9858 | -57.258 | 2024-10-18 06:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.0 |
| 90c9955b-42ec-3347-b03e-dd5ce1feae51 | -18.0049 | -57.2968 | 2024-10-18 06:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.2 |
| a2714a46-3683-3eb3-88c7-b2bddc658833 | -18.0052 | -57.2762 | 2024-10-18 06:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.0 |
| f81244bc-d245-3a8d-a4fc-6f13c9e9df0a | -18.0056 | -57.2555 | 2024-10-18 06:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.1 |
| d6caad1a-e96a-366f-ad2c-fd92d3615100 | -17.9033 | -57.474 | 2024-10-18 06:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.0 |
| a2ff6359-df5f-3173-8493-3746263e3ac6 | -18.6575 | -57.3382 | 2024-10-18 06:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.6 |
| 9b32116b-375d-3f0f-9960-fb5124833d59 | -19.6009 | -57.0044 | 2024-10-18 06:56:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.6 |
| 12132db8-6c63-3c43-88de-a2ca6bdefb10 | -19.5808 | -57.0071 | 2024-10-18 06:56:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.0 |
| a609d33f-cc8a-3081-9921-a5e423129a79 | -19.5804 | -57.0281 | 2024-10-18 06:56:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.6 |
| 04376e23-215c-3415-bc78-2d443e657ceb | -12.5147 | -63.3014 | 2024-10-18 07:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 8e0163a1-b8d3-3e5b-8336-545ef739da3c | -12.5338 | -63.2812 | 2024-10-18 07:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 9db758ca-d725-3001-b652-2d1601223d92 | -12.5336 | -63.3003 | 2024-10-18 07:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 76503bac-3828-3168-920e-d28ec353ab2c | -12.5149 | -63.2822 | 2024-10-18 07:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 5e823feb-b2ee-35e3-a639-f1bfd6ffff0a | -17.2277 | -56.6922 | 2024-10-18 07:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.9 |
| 2c617e47-e39d-3ff0-b6ce-beec65bb4436 | -17.2081 | -56.6946 | 2024-10-18 07:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.2 |
| 5c218693-49f6-34d8-b8b6-3b9c7cfb808a | -17.844 | -57.4813 | 2024-10-18 07:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.4 |
| c3a3ab7c-a61b-3ec6-9a82-fa897645b1c8 | -17.8243 | -57.4837 | 2024-10-18 07:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.2 |
| 046ea30a-39dc-3a19-b775-d809470c86a2 | -17.9234 | -57.451 | 2024-10-18 07:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 125.0 |
| a3ee3510-2091-372b-a0e4-fc11605fcf37 | -17.9855 | -57.2786 | 2024-10-18 07:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 121.9 |
| 32f6e099-3269-3136-9f3e-8897225e6a78 | -17.9858 | -57.258 | 2024-10-18 07:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.8 |
| 323ac961-6bd9-3409-ab2b-d976b0559bac | -18.0049 | -57.2968 | 2024-10-18 07:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.9 |
| df273f8e-1a95-33dd-bae8-0efcbbfeb390 | -18.0052 | -57.2762 | 2024-10-18 07:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.2 |
| 50108838-eaaf-37e8-b1a2-4d68522b65cc | -17.9033 | -57.474 | 2024-10-18 07:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.7 |
| 6bdc617b-fc2f-35de-a240-6b7f9f970b17 | -17.9036 | -57.4534 | 2024-10-18 07:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.7 |
| 7e264aab-e2a9-3cbe-999a-c1f01e057c73 | -17.923 | -57.4716 | 2024-10-18 07:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.4 |
| b7abac64-a884-316b-8f57-e7ddef5f7644 | -18.6575 | -57.3382 | 2024-10-18 07:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.9 |
| fe852cc2-60d3-3198-80f0-3687fdf7f4d1 | -19.5808 | -57.0071 | 2024-10-18 07:06:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 131.3 |
| 78c16726-09e0-3815-a415-68e9f0ec79e9 | -19.6009 | -57.0044 | 2024-10-18 07:06:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.7 |
| 77666d32-f4b8-3f0a-aaa6-f74218cff136 | -12.5336 | -63.3003 | 2024-10-18 07:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 26a0ed8e-4cab-3703-9a7d-9cbf3108c1c6 | -12.5338 | -63.2812 | 2024-10-18 07:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 49.1 |
| d3d6b46a-9217-387e-b5b6-f5d079676aa9 | -12.4958 | -63.3024 | 2024-10-18 07:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 44.6 |
| bd20e535-fb47-345b-9ad0-f24c5288d1c3 | -12.5147 | -63.3014 | 2024-10-18 07:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 67ba1043-3a26-3626-b1f7-13105b80b3c1 | -12.5149 | -63.2822 | 2024-10-18 07:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.3 |
| effa7340-84a4-30f9-be87-3c430df70803 | -17.2081 | -56.6946 | 2024-10-18 07:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.3 |
| ccec0532-6637-3d4f-b0c2-f09bc5f9054a | -17.237 | -57.3284 | 2024-10-18 07:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.7 |
| 6ec45db3-8280-3ca5-af7b-0491844e0ecb | -17.2177 | -57.3102 | 2024-10-18 07:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.9 |
| db24b2ba-3798-3619-859b-92203907815f | -17.2173 | -57.3307 | 2024-10-18 07:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.1 |
| 52b0c12c-35a8-3bde-9e0f-b2bdb93ac557 | -17.2277 | -56.6922 | 2024-10-18 07:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.8 |
| 0bcd7146-bf76-317c-ad29-883d04053792 | -17.2373 | -57.3079 | 2024-10-18 07:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 118.0 |
| 7242490b-a900-33bc-bb6d-64b8389fa453 | -17.844 | -57.4813 | 2024-10-18 07:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.7 |
| 66320cd8-be8f-38b0-9369-886db16d8cf0 | -17.8243 | -57.4837 | 2024-10-18 07:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.8 |
| aca53575-7de4-3d15-be16-736a69e527bf | -18.0052 | -57.2762 | 2024-10-18 07:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.1 |
| 551521a6-acad-3bda-ae38-4b4fbb5b7e98 | -17.9855 | -57.2786 | 2024-10-18 07:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.5 |
| 8c017438-16cf-3b4e-86b4-7bf6ce18c6e6 | -17.9858 | -57.258 | 2024-10-18 07:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.7 |
| 3727f451-e947-3052-9255-81e96472a54f | -18.0049 | -57.2968 | 2024-10-18 07:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.0 |
| 4a00ac80-e2be-3548-b48c-8230a6938a50 | -17.9036 | -57.4534 | 2024-10-18 07:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.7 |
| 796606b2-a22e-37d8-a79c-f5ee792d4091 | -17.923 | -57.4716 | 2024-10-18 07:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.5 |
| 19823cf3-2fb8-3575-ac6a-098d31b2bce4 | -17.9234 | -57.451 | 2024-10-18 07:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 125.6 |
| d3b47780-dd3a-344a-a52a-29e52af07e7c | -19.6009 | -57.0044 | 2024-10-18 07:16:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.0 |
| 73360c44-2802-3662-b636-46bf8cff7bee | -19.5808 | -57.0071 | 2024-10-18 07:16:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.4 |
| 4cd1eff7-cb00-3cc3-ae10-59a716573e6e | -12.5149 | -63.2822 | 2024-10-18 07:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 27934415-d31e-379b-9ca2-568633009ce6 | -12.5336 | -63.3003 | 2024-10-18 07:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 19735b19-5ed9-3a73-b581-b143da2b3147 | -12.4958 | -63.3024 | 2024-10-18 07:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 671da560-e4bb-396d-bf92-77328b334b0b | -12.496 | -63.2832 | 2024-10-18 07:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 88c4fa3a-78da-3bbc-bbf3-f9cb2ada25f2 | -12.4966 | -63.2066 | 2024-10-18 07:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 9050d036-5c87-3fa2-8439-93b7e3efc9d0 | -12.5147 | -63.3014 | 2024-10-18 07:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 88.3 |
| d5705f6e-42a8-3710-85d9-da897ff82c00 | -12.5338 | -63.2812 | 2024-10-18 07:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 3d52f4ae-6b49-3989-9dfd-8e3223fae5ab | -12.5155 | -63.2055 | 2024-10-18 07:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 7667df7a-5753-313f-b568-a224ce44f736 | -17.2373 | -57.3079 | 2024-10-18 07:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 171.7 |
| 52614b1f-a849-3fdb-95f0-cf4cd27eede2 | -17.237 | -57.3284 | 2024-10-18 07:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.7 |
| 67b66768-9a39-32be-a4f7-57984bbd1711 | -17.2177 | -57.3102 | 2024-10-18 07:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.3 |
| f1d428fb-b6e6-3d65-b2ee-dad1fa89d93c | -18.0052 | -57.2762 | 2024-10-18 07:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.1 |
| 3510ed7b-2423-3929-808b-01e785df3043 | -18.0049 | -57.2968 | 2024-10-18 07:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.6 |
| 90a1ccc6-f143-3851-b6e0-d8e212391292 | -17.9036 | -57.4534 | 2024-10-18 07:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.9 |
| 7bae21d7-dfd5-31e6-9075-bb11e01b897a | -17.9234 | -57.451 | 2024-10-18 07:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.5 |
| cb6c23d7-8143-3e2f-b9a3-ab1a73d7dbd8 | -17.9855 | -57.2786 | 2024-10-18 07:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.8 |
| 633bcd3a-b063-3639-a5f3-7a9015db26a2 | -17.9858 | -57.258 | 2024-10-18 07:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.0 |
| 1be651cf-76c5-3989-acd8-c1a4fe5b4071 | -12.5336 | -63.3003 | 2024-10-18 07:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 46.2 |
| e14fc56c-f851-3807-83a3-9fcc0500fcb1 | -12.4967 | -63.1874 | 2024-10-18 07:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 9328d118-18b8-3655-a82b-5735b5f76fc4 | -12.5338 | -63.2812 | 2024-10-18 07:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 7fbc51be-eb42-3396-b481-ea71b9b3f2a1 | -12.5155 | -63.2055 | 2024-10-18 07:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 9cd00606-726c-33da-8a65-837058cc3499 | -12.4966 | -63.2066 | 2024-10-18 07:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 275e3973-57c5-366b-8e5b-4f0dde75732f | -12.496 | -63.2832 | 2024-10-18 07:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 44.5 |
| eeeafcff-c684-3a4c-b29c-834599338745 | -12.5147 | -63.3014 | 2024-10-18 07:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 709b8fe3-21ba-3a53-94cc-ab3abe0785d0 | -12.5149 | -63.2822 | 2024-10-18 07:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 3e32c7bf-2b10-3b55-9cac-d07dfc0f40cf | -17.237 | -57.3284 | 2024-10-18 07:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.1 |
| f4caae7e-dc3b-3774-bb87-f99049e83b9d | -17.2373 | -57.3079 | 2024-10-18 07:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 132.8 |
| ce986992-12e6-30c7-a7ba-a7bbadadb90f | -17.8049 | -57.4655 | 2024-10-18 07:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.1 |
| b8538b49-7c13-396f-ae4e-485fb5d8308c | -17.8243 | -57.4837 | 2024-10-18 07:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.4 |


[Clique aqui para ver as próximas entradas](README31.md)
