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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac2e4af6-c823-3b99-9ff6-5afc4d203f16 | 1.78744 | -50.43993 | 2024-11-02 05:01:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6eba6fc1-cc9f-3e05-8fbe-6e3f0a31ba42 | 1.78725 | -50.43782 | 2024-11-02 05:01:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 123c077c-458a-33b7-8527-839c4122a979 | 1.78675 | -50.43564 | 2024-11-02 05:01:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 68209ec8-52ea-326a-b19d-7eb64aebaa7b | 1.78377 | -50.44051 | 2024-11-02 05:01:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 639c26c3-7312-3185-9d01-3f32b5164d80 | 1.78358 | -50.4384 | 2024-11-02 05:01:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 02aabfb2-3888-3241-b383-dede35d8d801 | 1.46434 | -50.86444 | 2024-11-02 05:01:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad2362cc-04e7-396b-b954-bcc065cd9b8a | 3.88843 | -51.74018 | 2024-11-02 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba6a5fde-40c8-3681-b369-e31d1b3fd097 | 3.52073 | -51.27914 | 2024-11-02 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 1d1c1ea0-e72f-3d10-9149-230976009452 | 3.52013 | -51.27535 | 2024-11-02 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7c3ad17e-3000-3862-b8f0-fb044b1e5ea1 | 3.51847 | -51.28728 | 2024-11-02 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40b7b1c9-5ce4-362f-aa09-d03cdad18629 | 3.41134 | -51.27608 | 2024-11-02 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5c678d5-e0f7-39bb-8f51-25e303b1e84d | 3.36819 | -51.29459 | 2024-11-02 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9c3ccf6-bf36-3d3f-af5d-b33acb43d36f | 2.58597 | -50.96224 | 2024-11-02 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52dfe4d9-107d-3e2a-80f1-a2222a992334 | 2.58535 | -50.95825 | 2024-11-02 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27d17867-90a3-3610-adf3-a2bca66c4fc8 | 2.56679 | -50.93255 | 2024-11-02 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be15a490-3db9-31e4-9cc6-775a5e1578ce | 3.31644 | -59.91207 | 2024-11-02 05:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48c25939-a73d-371c-9c52-fca4b56ede14 | 4.38209 | -60.70033 | 2024-11-02 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 35d9ddf4-64eb-3941-81b4-b667e065d672 | 4.38134 | -60.69515 | 2024-11-02 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5f2c7810-e6cd-30ac-821c-8fe3d5c44bf1 | 4.04515 | -60.22142 | 2024-11-02 05:01:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7168051-fdd9-3c17-a8f5-5da8ecfabe22 | 4.04376 | -60.22088 | 2024-11-02 05:01:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2fa1c178-3700-3461-9682-2ffac258778e | 2.98496 | -61.20005 | 2024-11-02 05:01:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d98e6f5c-b1b1-3ecc-8b95-8063ea1898c4 | 2.69658 | -61.39874 | 2024-11-02 05:01:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7303842-2b2d-3187-823c-46a5cb5e001e | 2.58007 | -60.69851 | 2024-11-02 05:01:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c7f6ced2-2d80-3451-9c27-e8a0ae2cc3b0 | -2.57885 | -50.05724 | 2024-11-02 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8b7d6bde-5542-36e8-a989-eab8e225d138 | -2.7405 | -54.12598 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d5a136e-7bd7-3d92-931f-b48668253654 | -2.85426 | -49.38987 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 27eb80db-a1d3-36ab-9476-3899801879a0 | -3.40044 | -41.6422 | 2024-11-02 05:04:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| fa6b069b-4381-3dcf-814c-030f6aa9626d | -3.39896 | -41.64241 | 2024-11-02 05:04:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 08137f97-904a-3e70-9388-92f55b3b4b16 | -5.31678 | -43.07181 | 2024-11-02 05:04:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f40ce80-0e4d-3669-935c-04c279e9d3a6 | -5.31019 | -43.07081 | 2024-11-02 05:04:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6803961c-66db-369b-bc5b-c9edbee9895b | -3.53196 | -43.62075 | 2024-11-02 05:04:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 076e3f04-7018-349f-bc8a-5bd6d5572a2f | -3.22638 | -44.41876 | 2024-11-02 05:04:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 12e3889e-2579-31ec-87e8-bd8b9b7cfcfb | -3.2248 | -44.41912 | 2024-11-02 05:04:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a0754190-d562-3d98-86aa-dc3e2529d596 | -3.22049 | -44.41784 | 2024-11-02 05:04:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8a609655-c348-348c-be52-3ef460c899b8 | -4.60647 | -43.99298 | 2024-11-02 05:04:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 615ab0ff-589f-3fc9-aff7-5e0cf462d2d1 | -4.6058 | -43.9978 | 2024-11-02 05:04:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10c33242-7b00-36ec-8efd-fb1542c852ae | -4.60091 | -43.99183 | 2024-11-02 05:04:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7dcb73c9-3bc8-3552-86e2-217612b94965 | -4.6003 | -43.99198 | 2024-11-02 05:04:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ffc607c7-ce57-3259-8a35-f4ad74235d72 | -4.60021 | -43.99666 | 2024-11-02 05:04:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 186d1482-a19a-37d4-a038-7035489461f7 | -4.59964 | -43.99681 | 2024-11-02 05:04:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e41ebb13-c6e4-3b18-bbe5-5855e9f88df4 | -4.45018 | -43.63176 | 2024-11-02 05:04:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11da2129-7253-31db-80db-f77fde2fd143 | -4.44947 | -43.63683 | 2024-11-02 05:04:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01a28c37-e679-3abe-83f7-c2796451dbd8 | -4.44877 | -43.64186 | 2024-11-02 05:04:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 21ef425c-a266-36be-a623-49a924f737a2 | -4.44808 | -43.64681 | 2024-11-02 05:04:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa1ab045-2fdf-3793-bb72-3ae602e18ce6 | -4.3993 | -43.46563 | 2024-11-02 05:04:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 534b9dc0-6926-392e-8b78-221e35b567db | -4.39369 | -43.45932 | 2024-11-02 05:04:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9fbd7073-e64d-34a1-bcd6-3ba157eb0c6d | -4.39295 | -43.46455 | 2024-11-02 05:04:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 205605ff-8a32-318a-9b5a-d301d67794fd | -3.78114 | -43.548 | 2024-11-02 05:04:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da3903e7-86d0-3281-b718-14aa4182c80a | -3.78041 | -43.55298 | 2024-11-02 05:04:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a314d92b-c65f-323d-b8ed-c0f7f7ae61b7 | -3.77919 | -43.54434 | 2024-11-02 05:04:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c7ebae74-640f-3862-b78b-bc1b043d39d1 | -3.7785 | -43.54939 | 2024-11-02 05:04:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f7620f14-b699-33d2-90b4-d4bd3e654dcf | -3.77781 | -43.55433 | 2024-11-02 05:04:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 3e6b097d-4f6c-3fae-b160-d0d90f1cfccd | -3.77557 | -43.54216 | 2024-11-02 05:04:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9a4ba9d9-c6d3-3d76-b4f9-40d69d7a2ab2 | -3.77483 | -43.54726 | 2024-11-02 05:04:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9975ac71-3911-3f6a-a447-da744166ac80 | -3.77411 | -43.55219 | 2024-11-02 05:04:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 518b204b-31fc-3b2f-8ccd-b9ca68634461 | -3.77339 | -43.55717 | 2024-11-02 05:04:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 458facf6-c4b9-3236-b3cf-02dc89c1a680 | -3.77288 | -43.54367 | 2024-11-02 05:04:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c2b7e3a9-33a0-3f50-b650-24be19d2f80e | -3.77217 | -43.54877 | 2024-11-02 05:04:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 2c4de0b6-6a8d-388f-875f-efabf93be55a | -3.7715 | -43.55362 | 2024-11-02 05:04:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4ccdda7f-de89-3e9f-86d0-dd5b3cb26763 | -3.77081 | -43.55862 | 2024-11-02 05:04:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5d72fac9-7390-3ce4-b754-9ff489d86066 | -3.76928 | -43.54132 | 2024-11-02 05:04:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 183216b3-9be8-36ab-9d6b-6f372c14dffe | -3.76853 | -43.5465 | 2024-11-02 05:04:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ec4eb6f4-86d3-335a-a33b-b64fbfc4ae7d | -3.76781 | -43.55145 | 2024-11-02 05:04:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 9f6ca660-a8ef-31eb-bc1f-e949cf0ec575 | -4.45019 | -44.17208 | 2024-11-02 05:04:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df316d9f-19f0-3301-ba3b-d6c2b54f2d65 | -4.44972 | -44.17091 | 2024-11-02 05:04:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f4b56aa5-0022-3777-904a-f21742ab973f | -4.44476 | -44.16633 | 2024-11-02 05:04:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0cbb3660-deac-33b7-9137-4847423ed994 | -4.44412 | -44.17099 | 2024-11-02 05:04:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d611aa1-26ba-3c6d-9d27-88e7af7b26f1 | -4.44366 | -44.16979 | 2024-11-02 05:04:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 63521f15-7f25-35ea-985e-d20d7dc922f4 | -3.83471 | -44.13467 | 2024-11-02 05:04:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7715f7b3-9517-3383-8526-5eafe224b0b0 | -3.83345 | -44.1335 | 2024-11-02 05:04:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6a12f8d-9c31-3c01-9e55-b005962e77c4 | -3.83278 | -44.13805 | 2024-11-02 05:04:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4541486b-9b30-35c1-bd5f-2ef2d2d87ab1 | -3.82867 | -44.1337 | 2024-11-02 05:04:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e4e0488-efcf-385a-a305-463c2cb857a2 | -5.56596 | -43.87998 | 2024-11-02 05:04:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c8b46bf0-79b9-3468-a6d9-7270a2240457 | -6.19224 | -44.53434 | 2024-11-02 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d5496f7-a156-37e5-a404-ae602e3ffb31 | -5.20188 | -44.30862 | 2024-11-02 05:04:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e522da0-0154-34df-afc0-87a29f94cf89 | -5.0685 | -44.22982 | 2024-11-02 05:04:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e0a38b4-d9ab-34e7-9c98-0624227532cb | -5.0685 | -44.22912 | 2024-11-02 05:04:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0e28d444-860e-336f-a1d5-921662e2b465 | -5.06787 | -44.23458 | 2024-11-02 05:04:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a526f110-8f1d-3242-be9d-293256918628 | -5.06783 | -44.23387 | 2024-11-02 05:04:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3f4af4e8-51fa-302c-bc08-ff702a981279 | -3.40554 | -44.98325 | 2024-11-02 05:04:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e100935-1e93-3640-9d15-74bdcd95f476 | -3.40497 | -44.9872 | 2024-11-02 05:04:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f4c6edb-6000-3715-a1e6-381295a8d51f | -3.37546 | -45.70324 | 2024-11-02 05:04:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 583c318c-794e-3447-b8db-b97aaae3df56 | -3.37496 | -45.70673 | 2024-11-02 05:04:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29fbc2ba-aead-3979-a2ad-338f1cbbb78d | -3.2379 | -45.59479 | 2024-11-02 05:04:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6ef74589-635e-3692-8e2b-8c4d7e106e9d | -3.23297 | -45.59035 | 2024-11-02 05:04:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 30d54a4c-a21f-3926-9987-2489f3f321f2 | -3.22035 | -45.29566 | 2024-11-02 05:04:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c3f881f-e2d9-3ab4-bab1-cb451f65638a | -3.21917 | -45.29581 | 2024-11-02 05:04:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8e909ca-55c0-3f49-8b2a-93e26b925158 | -3.21478 | -45.29483 | 2024-11-02 05:04:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9c15644-9ad2-3e20-b531-be04c8ad612d | -3.21422 | -45.29856 | 2024-11-02 05:04:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1a6d9f0-cbf9-346d-9ef3-bf382899a2e5 | -3.2136 | -45.29496 | 2024-11-02 05:04:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e8de44c-2def-3f6c-8560-7d1b99bef393 | -3.21307 | -45.2987 | 2024-11-02 05:04:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 812698a4-eafb-38ba-9a2f-edcb3c3f379e | -3.07973 | -45.13493 | 2024-11-02 05:04:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 29167049-f73c-36ae-8816-2f4b895a46ec | -3.07467 | -45.13028 | 2024-11-02 05:04:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 17.2 |
| c0abc670-b77f-3307-8a6b-71b18400bbdf | -3.07411 | -45.13409 | 2024-11-02 05:04:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 67630f44-b2dd-39b6-9975-e56b4f84eb10 | -2.64754 | -45.77425 | 2024-11-02 05:04:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc70aeb5-8852-36ba-a981-94190121244a | -2.64704 | -45.77763 | 2024-11-02 05:04:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fdb4e3e-ed16-31e0-9b62-70b914477409 | -2.6422 | -45.7734 | 2024-11-02 05:04:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46df73a8-c4ea-30ea-9f50-2fe5d5c7aac5 | -3.22576 | -44.42292 | 2024-11-02 05:04:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 076598bc-290c-31ad-b243-31737da10c53 | -4.96263 | -45.87698 | 2024-11-02 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 81959f61-784f-30e7-9b9a-a25df18e56d2 | -4.95838 | -45.5505 | 2024-11-02 05:04:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README56.md)
