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

## Dados Diários - Página 151

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2fbb5e8-49e5-3239-af31-bbc4c790c681 | -3.85934 | -52.25904 | 2024-10-03 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 475ef73d-adc0-3e0e-b44f-d83a6db425b4 | -3.77435 | -52.19256 | 2024-10-03 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e7fb8a98-8596-3700-beac-e3799ed7dc4f | -3.75167 | -52.25655 | 2024-10-03 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9264fc0f-c135-3f24-93e7-bc7a544aa6ad | -4.09785 | -51.11593 | 2024-10-03 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf2c4637-9691-322a-8063-14e3e74a15f4 | -4.09708 | -51.12101 | 2024-10-03 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e39a66cb-5340-3ef2-b3e1-b381e307baf1 | -4.09241 | -51.12024 | 2024-10-03 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3ca25737-88bf-3abc-8d94-9a3eef04e212 | -3.95554 | -50.89228 | 2024-10-03 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52329335-e59d-37a7-ad4f-c30dc2416ffd | -3.95434 | -50.89539 | 2024-10-03 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4caf26c7-f7ed-3252-81fb-aa1a656132c3 | -3.95349 | -51.00587 | 2024-10-03 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 48ff8c60-32b5-3348-9c1e-144ec402d476 | -3.95275 | -51.01097 | 2024-10-03 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 459283a6-6420-3743-9662-60acea3641f7 | -3.94952 | -51.00011 | 2024-10-03 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a897743-154f-312c-a313-fab309ecd33a | -3.94879 | -51.00513 | 2024-10-03 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f514899a-5a5f-39b1-9558-22bf7f32d224 | -3.94687 | -51.24507 | 2024-10-03 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb86b5d9-5976-3b23-a6ea-6949053312cc | -3.94224 | -51.24435 | 2024-10-03 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b4f0caf-0ca3-3558-ba1e-71a7f2d96357 | -3.75296 | -51.13206 | 2024-10-03 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4cee0801-d6c1-3c54-9b47-56cf72e7a271 | -6.38752 | -52.70408 | 2024-10-03 05:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd6f9a64-96ad-301b-a628-4508c29ef4b9 | -6.38317 | -52.70343 | 2024-10-03 05:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eec2cb34-ad3b-33d6-a00f-a8d2fbf9b3a7 | -6.38258 | -52.70758 | 2024-10-03 05:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e402f19-ac09-3a55-abd4-c65f7e25ed1c | -6.37823 | -52.70697 | 2024-10-03 05:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e62331c3-3255-34dd-9124-535e20450f63 | -6.32094 | -52.75527 | 2024-10-03 05:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 55ff7566-9cd2-39c5-bb9a-aeb966fd25f1 | -6.32035 | -52.75931 | 2024-10-03 05:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9a33f24-aeca-363d-980b-3945b8f26928 | -6.47742 | -51.50663 | 2024-10-03 05:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6c8829b-4648-3c93-b8e9-eff87be1fd51 | -1.65815 | -52.58615 | 2024-10-03 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e81023bb-3aef-3bcf-9d6f-448dfd9c9e99 | -1.35072 | -52.30626 | 2024-10-03 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee7fdccb-b97e-38a5-8916-ff582f5fe283 | -3.29732 | -53.70014 | 2024-10-03 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd260f07-e4a3-311b-9058-dead8202f907 | -3.29681 | -53.69882 | 2024-10-03 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f06cd022-a6e8-308f-b7e5-4048b903fe30 | -3.29605 | -53.70369 | 2024-10-03 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68d3e03f-bf8f-33b7-82ef-e04b3593f79b | -3.29292 | -53.69823 | 2024-10-03 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0486a0c1-87f8-3a10-8dcf-c84586efb60c | -3.29216 | -53.7031 | 2024-10-03 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d9e4678-adc1-3ee5-9dbb-8fc6b4113b8f | -2.85393 | -53.31698 | 2024-10-03 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5f957e3-7f6d-3ab6-b67e-d1d51101a423 | -2.84997 | -53.31638 | 2024-10-03 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb78e67b-b3fc-3c82-b247-e914e0785a0a | -3.76607 | -52.33733 | 2024-10-03 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f0fbb7d-3990-3408-8b0b-47c40bc3d9c3 | -3.76547 | -52.34136 | 2024-10-03 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20173140-d8f8-3b34-800e-17f46acb1347 | -3.76179 | -52.33666 | 2024-10-03 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5fb734f5-8c28-3bed-ab1c-f03b312efef1 | -3.76119 | -52.34068 | 2024-10-03 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d6fc1a6-4f14-3e5e-b53a-9779030ea869 | -3.75969 | -52.2619 | 2024-10-03 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97f6dc98-94e1-3aa3-8e3a-3f345d782154 | -3.75897 | -52.41418 | 2024-10-03 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8501b92f-d34d-3aef-b097-334c6cae000c | -3.75535 | -52.26146 | 2024-10-03 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c468c49-0f5f-315e-9c0a-7794ec0eff92 | -3.75475 | -52.26552 | 2024-10-03 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f0dcf686-81b8-3d59-a235-e0629f09dee8 | -3.75471 | -52.41355 | 2024-10-03 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06038956-7607-3ccd-be65-b4ee24412f51 | -3.75105 | -52.26078 | 2024-10-03 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a703963-59fd-308c-a00f-6aad2ab275d7 | -6.40523 | -53.68076 | 2024-10-03 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 656cf277-a6c8-32fc-b290-6ae8e21f8e06 | -6.24473 | -53.33318 | 2024-10-03 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ce2cb1f-6202-3cad-8da4-2a6f4416bd16 | -6.23642 | -53.33192 | 2024-10-03 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7912e0cd-1454-3372-8c3b-e9c36b5353b5 | -6.23226 | -53.33128 | 2024-10-03 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dddc81c7-9614-3a35-8dd8-4b9f4775c6b6 | -6.23172 | -53.33502 | 2024-10-03 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21cc8295-12df-3b23-ac05-af210dabf1de | -6.19291 | -53.28025 | 2024-10-03 05:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9ca47f79-a3a3-3e40-8c1e-b71ebb466051 | -6.19235 | -53.28411 | 2024-10-03 05:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f2fe93ab-30dc-3479-a93b-398e6073509e | -6.10122 | -53.2276 | 2024-10-03 05:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bf1ad244-2870-326f-834e-385397aeaf50 | -6.07062 | -52.87197 | 2024-10-03 05:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e87c0db0-bc13-354f-bc6a-3e4c31e57550 | -6.07012 | -52.87543 | 2024-10-03 05:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7746388c-2d24-3d6a-a6db-8bcd6c59ab8a | -5.87698 | -53.88728 | 2024-10-03 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91f283da-a646-322b-b654-a7c0e0697617 | -5.8743 | -53.89122 | 2024-10-03 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 700609c4-b657-3926-8f50-dcbfbcc3c00d | -5.87249 | -53.89014 | 2024-10-03 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c49705e-0247-37fb-8688-8f8a9235517b | -5.85009 | -53.55664 | 2024-10-03 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49e2e5da-4262-3599-a5fb-fd1a38d258d6 | -1.89766 | -54.70757 | 2024-10-03 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 409514f4-45d0-37b3-abc6-0f2ded3cf083 | -1.76179 | -54.4491 | 2024-10-03 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d6e04bc-147c-3250-9eaf-2c4055b910c6 | -1.75814 | -54.44855 | 2024-10-03 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5093683b-e666-336b-9142-e7c2651ad913 | -1.75748 | -54.45279 | 2024-10-03 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87e15043-55c7-3949-a45a-fbcdf0673995 | -1.75449 | -54.448 | 2024-10-03 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 647b4c44-4be1-317e-ae1f-1eca63d62506 | -1.75383 | -54.45223 | 2024-10-03 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d745479-7e97-39cc-9900-eff1e53e61a3 | -1.75084 | -54.44742 | 2024-10-03 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11a40af1-9a9f-3f6e-b2c7-42dae185c447 | -1.75018 | -54.45166 | 2024-10-03 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a53bd5c-50b4-3eed-b0d8-6b518009dccd | -2.14143 | -53.65283 | 2024-10-03 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eec03e08-40c4-3110-8428-5270622d8c4f | -2.13759 | -53.6522 | 2024-10-03 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 316e5c6a-0482-3d2a-9dd9-f138db6555eb | -1.1412 | -53.64076 | 2024-10-03 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b0b61f81-3ca8-39bb-87ad-39471213671f | -1.14067 | -53.64219 | 2024-10-03 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3b19169f-dfa7-320d-9032-51de556e1a2d | -1.14049 | -53.64524 | 2024-10-03 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c31427c1-bf63-3ca6-85ff-1c015230a9f6 | -1.13817 | -53.63539 | 2024-10-03 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 59bffc20-474b-3fa4-b386-d4667da8999d | -1.13746 | -53.63992 | 2024-10-03 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7a419c2c-0f4a-35d7-bcaa-0a16a5b28d7f | -1.13673 | -53.64448 | 2024-10-03 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e92cdfae-bd09-399f-97f6-0dba401564e4 | -1.1344 | -53.63471 | 2024-10-03 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 54b85b7c-561c-346a-bd9a-b34b58b017be | -1.13368 | -53.63929 | 2024-10-03 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8a55f49c-93f3-325b-bbfa-49c0296204db | -1.12989 | -53.6387 | 2024-10-03 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0aed2ed3-d981-30e2-bf85-e4ce3beb1ea1 | -1.05041 | -53.52852 | 2024-10-03 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2591e1b7-c480-3422-b35c-d62208c14ed3 | -1.05 | -53.52643 | 2024-10-03 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f1164609-f9d8-3f17-a7b7-51620a32fe51 | -1.04968 | -53.53313 | 2024-10-03 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 901824e7-401d-3376-a4b4-924d47afc140 | -1.0493 | -53.53105 | 2024-10-03 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f405fcda-ec65-3492-88c8-09b6e8bf2873 | -1.04733 | -53.52331 | 2024-10-03 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 169c2cdc-f4f5-3437-9c30-53884cabf5ac | -1.04661 | -53.52789 | 2024-10-03 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5b2a20a5-d5b5-3729-b0b8-504339d8eac4 | -1.04588 | -53.5325 | 2024-10-03 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 62caeee3-f5fa-3463-bb67-aa222aafbc05 | -1.04427 | -53.51803 | 2024-10-03 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a2b25854-bb3d-382c-b278-119162ac5eb4 | -1.04353 | -53.52266 | 2024-10-03 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 204bdf0d-c18e-3832-9f33-192b19f46f51 | -1.04281 | -53.52725 | 2024-10-03 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 00ad5ffe-d85f-3d51-8c58-664aa03c8313 | -1.04208 | -53.53189 | 2024-10-03 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5f58ca23-09d7-3f9e-8520-aa22dd46c55f | -1.04121 | -53.5127 | 2024-10-03 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f0a78ac9-ebc7-3429-b31b-d0db0bed0479 | -1.04047 | -53.51735 | 2024-10-03 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 87ec1bc2-0b3d-32d2-a202-f78fb895f864 | -1.03974 | -53.52198 | 2024-10-03 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1f51612d-cfcf-3b19-9d12-f5cecc6de2d3 | -1.0374 | -53.51207 | 2024-10-03 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b6dbe7e6-8c15-3427-be88-9dbd2ad97c65 | -3.5077 | -54.03068 | 2024-10-03 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a1e8ff81-403b-3aae-b4a4-4a6aa58e15c3 | -3.50387 | -54.03012 | 2024-10-03 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c5b78c9b-236e-367a-89af-815368d68d90 | -3.46161 | -53.98277 | 2024-10-03 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d2dd9aa6-a92d-322c-9735-126d37def40e | -3.46088 | -53.98748 | 2024-10-03 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5ee43bea-6d50-3376-90ee-57e573e4980c | -3.45777 | -53.98223 | 2024-10-03 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2eb13181-0c8f-3720-821e-50a974a61237 | -3.45705 | -53.98692 | 2024-10-03 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 22d9c8c7-a2ee-35e1-9c3b-f83b9a3cf386 | -3.45393 | -53.98171 | 2024-10-03 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 62045251-7c3f-31ec-8f81-ddd90908e06e | -3.45321 | -53.98636 | 2024-10-03 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 303b8641-2f07-3417-b09a-ede844dc6291 | -3.45009 | -53.98116 | 2024-10-03 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bbe67091-e551-3756-ae1a-0bc50ec8e71b | -3.3791 | -54.11397 | 2024-10-03 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4d776d11-9083-350c-87da-1e988200b7d9 | -3.37838 | -54.1187 | 2024-10-03 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README152.md)
