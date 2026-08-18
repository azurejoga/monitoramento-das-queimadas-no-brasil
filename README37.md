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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93445123-659b-385b-8113-9665befb5f01 | -8.19864 | -55.0175 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 37ca4835-5800-31f1-adfb-e834c70f656c | -6.75184 | -59.16608 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ef880fe0-a2c9-3c32-81e8-610ee6df6f6d | -9.99117 | -53.94548 | 2026-08-18 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f1fb1e5-4133-3fd8-95dc-e3cc09461fbd | -8.10757 | -51.65934 | 2026-08-18 04:57:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d3ee151-c566-3ca7-ae30-9d5d2656ffac | -6.85018 | -59.01437 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 706ece34-6c09-3528-a077-e15dd9c7c623 | -6.77518 | -59.45423 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca1d36ca-097f-34fb-86aa-5d521979973f | -8.58648 | -54.72025 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| bc770f96-6da0-3dcc-914f-f19ef56d8c0f | -6.99013 | -59.04851 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 412964b0-a30c-3297-adff-9b87540fa25f | -9.42102 | -60.44439 | 2026-08-18 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f92a557b-9312-3b50-8e5d-f31d58b9685d | -6.71571 | -58.93263 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b433e625-b677-3710-9504-d2b94bd97283 | -6.10627 | -57.73127 | 2026-08-18 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 236abaab-f5b5-3a69-93c1-f3291d825a7c | -9.471 | -51.64761 | 2026-08-18 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea8dd08d-9680-36c2-aee3-a9803b89ddda | -11.82321 | -56.59796 | 2026-08-18 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b7aaf0e-3213-3086-8282-5ffbe9eab9e9 | -8.56639 | -54.69472 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 638b9bd5-069e-3183-a693-492276bd96f8 | -8.56743 | -54.7097 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7c6f15c8-724a-349f-bc12-ba01828709f5 | -12.76768 | -48.4207 | 2026-08-18 04:57:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19495cb4-5264-3387-b3eb-7971b956c0b0 | -6.99445 | -59.04925 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd9314e0-a814-3538-b3f2-e98311890478 | -12.46503 | -54.19779 | 2026-08-18 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| af2e01e4-96f2-36a1-abf6-c9e6c3a6ce21 | -7.87813 | -63.76509 | 2026-08-18 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e62553e6-9d7a-3c23-943a-eca6642c25f3 | -7.37699 | -55.48905 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8596cb6-2454-3420-b5d9-6299ca55e1d3 | -7.82061 | -44.60797 | 2026-08-18 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5fbc6c66-2414-3870-9eed-015a8564efe4 | -12.227 | -47.03409 | 2026-08-18 04:57:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da02db61-c6bd-3c0c-a177-39f69fd9c6a6 | -6.13913 | -57.74026 | 2026-08-18 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9066a33a-ed97-39f2-89cb-9a6d5ee76a6c | -11.20279 | -54.82348 | 2026-08-18 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3dfd3edc-437f-3859-897f-bea0bc6bda41 | -12.45953 | -54.18966 | 2026-08-18 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5729d34-857c-3d95-b4b1-1d0dad52de63 | -9.40285 | -48.25036 | 2026-08-18 04:57:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f61a8af5-1574-341c-b79f-c51543246c6c | -6.10569 | -57.73473 | 2026-08-18 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1972778-e441-3eca-b612-0c7b2ec8d5a3 | -8.64226 | -54.68498 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec021e9d-1758-36d1-9136-f45d93008093 | -6.75842 | -59.15757 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 18a6273d-01b9-3869-99db-64290b4b3b87 | -9.47441 | -51.60254 | 2026-08-18 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ed84a990-bb72-3b8c-a483-77bdded09666 | -10.77107 | -50.36554 | 2026-08-18 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7a46e230-59b3-3dcf-bd5e-26b02bc9718e | -8.5708 | -54.71025 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 107f7be4-34c8-3892-aa77-2f2e1a15f924 | -6.70641 | -58.93513 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13dd9099-da2f-3433-8ec7-a77048bd4d55 | -12.2624 | -45.87016 | 2026-08-18 04:57:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba2459d8-f7b5-32fc-b92a-9bfd14487bc0 | -8.56848 | -54.72469 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 49b0bc2d-afea-3648-ae8b-fef360b2db67 | -11.46266 | -46.56993 | 2026-08-18 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3c9e8ce-3fe5-3549-b5a3-e078553dac65 | -8.58438 | -54.6903 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 27ce8bdf-6b2a-3440-806a-d4edd0f494ff | -6.76474 | -59.4616 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a174ed91-2cc1-3df5-8c1f-3b2c6ef5785f | -9.46585 | -51.61276 | 2026-08-18 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cc9bf587-25ac-36cd-a8b2-fb0ec3bab838 | -10.12132 | -54.27947 | 2026-08-18 04:57:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be768777-e1fd-3bc2-86ae-eb449e20e628 | -8.21638 | -55.03902 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 7e67494e-d098-3b10-8639-a4d6a2de37f7 | -8.61283 | -54.71726 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6448fc41-a28c-3bc7-b0bc-4e86238e496e | -8.21541 | -55.02364 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2f8b7cd1-ab5f-395d-a692-5b7caff24298 | -8.89643 | -60.60615 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 93a3b868-da92-3c1f-90fb-c7140346a71c | -7.38397 | -55.49018 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f82b0e7c-2140-35e1-a548-7f3ce23f2d70 | -8.96218 | -60.53278 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 96fb00b6-9751-3d8e-b0a9-6ddd414d47d0 | -8.59972 | -50.34317 | 2026-08-18 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6cd6e6ab-c1f4-34e1-872e-93825f2b3631 | -8.57092 | -54.68806 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff0d520b-7bee-35eb-ab0a-1c05aa8ffa19 | -11.50571 | -46.60654 | 2026-08-18 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| efcd2df1-7cbe-360f-9427-9838391cb461 | -13.28224 | -48.69418 | 2026-08-18 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a397335d-8fa9-391f-9ef6-346900da3d9e | -8.58879 | -54.70583 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4374bcda-d966-34db-a42e-9340f461445f | -6.67624 | -56.15679 | 2026-08-18 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 19853ba7-36b1-3f76-bc03-3c819395e6b4 | -8.56755 | -54.68751 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4bd24c3d-1196-3737-a942-154bdeae39ba | -8.58264 | -54.70112 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e988baa6-57fe-31ef-a595-eaf33606b69c | -6.03109 | -57.80936 | 2026-08-18 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1880143-2e32-392a-9b28-1af151d05e51 | -8.57753 | -54.71137 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1dbbd78a-57de-3f69-8a68-c35c08e7ac21 | -8.55426 | -55.31211 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19eb323a-c699-33bf-8c98-43d38f998d48 | -8.586 | -54.70168 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf9885ec-cc8b-3d41-a13d-debddf0fc1dc | -7.91332 | -61.73468 | 2026-08-18 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f299449-a794-3c2b-9848-3f11c3b6d75b | -9.06859 | -50.82524 | 2026-08-18 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| aa022554-61b9-3c0f-a665-a0957a43936e | -13.56623 | -51.69551 | 2026-08-18 04:57:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5e22e073-c631-38f2-89c4-c934d070f457 | -6.61035 | -58.96655 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91b6c88f-1ffe-3522-9866-8579c699e583 | -7.90205 | -61.73882 | 2026-08-18 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ec9ada4-0b38-38a6-8021-31ffae8e6250 | -8.73722 | -45.30238 | 2026-08-18 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e84e2734-cf58-30cb-8ad8-b8e213765fe7 | -7.14729 | -47.51231 | 2026-08-18 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7c42826-8268-37df-8e0f-eb6c1c8892cb | -11.20003 | -54.81938 | 2026-08-18 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa685e28-0460-308f-a31c-46a3bae70a7b | -11.12198 | -46.49602 | 2026-08-18 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8daa364a-1b6c-37bd-ae59-d1adc5f3eba0 | -7.5667 | -55.56349 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b41fa243-f671-35fe-9faf-953be4800015 | -9.12453 | -46.04154 | 2026-08-18 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| eee872aa-7d89-33e5-9d6b-32ad9d04ef10 | -8.578 | -54.73001 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 5fcc4a7a-57d9-3214-9943-db6eed3f1ddc | -9.01008 | -60.49866 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| f3f3a001-9a71-344a-b924-145d7dae008e | -8.4866 | -48.80485 | 2026-08-18 04:57:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50f55cb5-3251-345b-8c65-f6b47acb63f4 | -11.20394 | -54.81637 | 2026-08-18 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fdffeca-188a-3040-9784-bd87dc39c1fc | -9.42685 | -60.41146 | 2026-08-18 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e37be003-ed73-3938-82bc-b89517bab010 | -6.7114 | -58.93188 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e026450d-b1c4-3b51-b684-0cd140cffcc6 | -11.46797 | -46.56607 | 2026-08-18 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d10bf626-e28c-3294-8c67-bda5ff1d0801 | -11.21814 | -64.97977 | 2026-08-18 04:57:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 575146ab-6655-3ff6-8d5f-7f554e5eea5e | -10.94133 | -57.18116 | 2026-08-18 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6349945d-1b78-35c0-aba3-38ff0bf4b34d | -11.73602 | -54.59471 | 2026-08-18 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2df2e612-8d74-33a2-ad0d-9734c705c86f | -8.9024 | -60.5544 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff223445-53a5-393f-a731-f13197c65f0b | -7.91224 | -61.7408 | 2026-08-18 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43094615-b7e3-3f95-9e43-4b38049cac9b | -8.59615 | -50.34264 | 2026-08-18 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bba946c8-fcd0-3f1a-a436-47868767e66f | -7.37627 | -55.48544 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eccee1d4-3c36-309c-9bab-15ef6f78bfc3 | -8.56964 | -54.71746 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| cc624a6a-d0ee-3bb2-8504-eead38868005 | -11.11089 | -46.49333 | 2026-08-18 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3b9ea4d0-be5a-3e4b-87fd-4a03e0751f1e | -8.95005 | -60.52066 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd6902ca-50dd-314a-9e06-478385f4c17c | -10.11631 | -54.28948 | 2026-08-18 04:57:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23a383ba-21a9-328b-8430-f2bf5026b876 | -6.24579 | -55.62166 | 2026-08-18 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c56ac79-68ff-3c0f-af43-c45dab410e07 | -8.58101 | -54.68973 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| da338374-177a-3fc8-a79e-591380562229 | -8.02927 | -55.13147 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f722b23-f77d-3706-b183-9b6f556e1389 | -6.74082 | -59.15148 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4bc3b44-6211-3037-a70b-81b92c7df65e | -8.5701 | -54.73611 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea3ed6e0-ce62-3834-9573-1f57fa721a4e | -8.63817 | -54.71022 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e96e890-542e-3c01-8a53-d924d1634c8b | -8.09623 | -61.34474 | 2026-08-18 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 572ed43a-d3f8-3d56-b145-0f077513cf98 | -11.33743 | -55.26936 | 2026-08-18 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c7bec0c-84e6-32da-98de-a6196a243512 | -10.41187 | -61.21067 | 2026-08-18 04:57:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4ae3c4f3-8eee-34f7-8827-e1548ac06e75 | -8.18502 | -55.01524 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c1db0531-47ad-3e20-a61b-aad433e219e9 | -8.32724 | -46.48126 | 2026-08-18 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e946435e-3308-3140-b2bb-08009b5abf8f | -8.89884 | -60.56653 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 129ccfa7-70ff-3d73-9b28-286200d66d65 | -6.95488 | -59.03566 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README38.md)
