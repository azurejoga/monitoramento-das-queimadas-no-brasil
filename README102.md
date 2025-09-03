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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b801193-9ec1-3473-977a-8c3e755f4adb | -6.85654 | -52.79447 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90414612-a688-3e07-959a-74c312e8cd26 | -6.33 | -58.17113 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06b3a2cf-2672-3ced-97c9-647f381431bc | -6.82974 | -52.84497 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab405e30-d3bb-3e9a-95a5-ce27b1b4b2b1 | -6.3431 | -58.16916 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffbd624c-a186-32dd-a617-039a2f097333 | -4.52415 | -54.97135 | 2025-09-03 05:33:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff483698-a186-3218-8426-c30de64eca2f | -5.92493 | -57.7192 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 64951fe8-6111-3438-a6f6-c2df4a63dc43 | -5.91468 | -57.72977 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 96c5c1aa-2ba6-30c1-b1f9-e3d3f3fefbc3 | -5.87039 | -57.77355 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| af3a0f1c-5987-31f5-b2b6-33d93246ef54 | -5.10895 | -56.96397 | 2025-09-03 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05befff5-f40b-3aea-8b1d-37a490295213 | -6.06178 | -57.99769 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ca247c4a-c98e-3437-a434-cc699246ed2d | -6.80863 | -52.8197 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b322d788-198b-3eb9-8435-9e948b2c5034 | -5.86847 | -57.75706 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 8140e7d5-3f04-380e-b457-58b950a35080 | -5.89219 | -57.74419 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 5cef6901-519d-3ca4-8905-6e8871de4b63 | -6.82433 | -52.83966 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b39a6bfd-eebe-3192-9b01-8b116963956f | -3.48293 | -59.25629 | 2025-09-03 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0cbd3b12-7ae1-310d-aed0-4ed25a8c2d8a | -5.89648 | -57.74473 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| f331f732-3748-347b-809a-5fc8f18a6d3d | -6.82944 | -52.81282 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1a5da17-1740-3390-a185-698af8213ca1 | -3.524 | -59.01456 | 2025-09-03 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37cc0568-60a3-3c04-9078-9d6d1bbd3445 | -5.9164 | -57.7177 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| eb5b7483-4648-3f26-8689-21c09a57a179 | -6.83915 | -52.83245 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d81afe07-89bc-3369-a9c9-e8369c0df107 | -6.77299 | -52.8101 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ada1dabe-e6f4-3504-8cba-b98ecc1962a0 | -6.83549 | -52.81365 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a140d1b-f35b-3664-9296-b883fa1bc41e | -6.0045 | -57.85685 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80168231-f87b-3195-8407-2d062761b489 | -6.43589 | -58.12715 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 035052b2-ee2a-39f8-8052-d22e3ee35d27 | -5.92268 | -57.71574 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 3ec64813-0b2c-33b8-ab59-be65d386268e | -6.831 | -52.83593 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6c86dd15-20b0-3f13-86e3-19f8a4888298 | -6.42563 | -55.60897 | 2025-09-03 05:33:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87cfb1c7-c00b-3560-8e48-60f50ea4423d | -6.53519 | -56.20054 | 2025-09-03 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2701ae91-e7fd-365d-a87d-74c671d6cc5b | -5.87525 | -57.77017 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c9ece8fa-d166-3aaa-b1b7-298b8b57f6d1 | -2.2803 | -56.13039 | 2025-09-03 05:33:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a20fa560-281c-38e0-88d6-de3fe8777a66 | -5.92087 | -57.72778 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2d065bf0-5f16-303f-af6b-1d079759ebb3 | -5.92436 | -57.72321 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f24a91b8-7ea5-3a4c-8d5e-255fd88465c8 | -5.89708 | -57.7407 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 8c77fe59-f8c9-38dc-9881-5f48b14b044b | -6.8452 | -52.83327 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4039252f-22dd-322b-98ee-d615b106622c | -3.48224 | -59.26077 | 2025-09-03 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd7882fe-40b6-3b46-8d51-051b1cd7e2a7 | -2.94338 | -54.80093 | 2025-09-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aad87ba9-da78-3126-a580-b44232962fc3 | -6.82336 | -52.81225 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fc6c815-df51-3a9b-9da1-8e282f56e125 | -6.46741 | -55.88858 | 2025-09-03 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ccf81ab-5f0e-31fc-b846-7b553cf09263 | -2.93633 | -49.46268 | 2025-09-03 05:33:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f566f13-86ee-3f94-9233-7a81e9d927f3 | -6.33613 | -58.18759 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9c7c3196-2698-3dd1-9070-4db026470ea5 | -5.86358 | -57.76065 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c21308ce-645a-3250-a3b9-ae2f2c91a129 | -5.90989 | -57.74266 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| bfd9eaa4-2001-3d33-9054-f345fc61dcec | -5.91837 | -57.73448 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6297b895-2179-3869-a638-caf363309db8 | -5.91599 | -57.73111 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f64d14fe-d3ba-3185-a438-9b80f6bbfbe2 | -5.11342 | -56.96449 | 2025-09-03 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00bd3054-f8d1-3f09-834e-1d566d1bc3bf | -5.90073 | -57.74549 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| d68ec25a-41b4-3e96-b64c-6e922be12e76 | -6.33669 | -58.18378 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e0ed5fb2-86ce-3b76-a793-240b9652ff22 | -5.89953 | -57.75352 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9622274d-c98b-37ad-8240-bc555600062d | -5.90499 | -57.71701 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a9ba400a-4ac5-3b0e-9700-b3f728a3deb8 | -6.7736 | -52.80565 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb281283-2235-38ae-84c4-53aba02c932f | -5.87157 | -57.76559 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0ac1da88-9a6d-35bb-8683-af54f418fd48 | -5.9238 | -57.72712 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5980c61-5534-350d-a1eb-9e45da2939b0 | -5.11278 | -56.96886 | 2025-09-03 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88881353-9c1e-31be-87cf-841cb86082e2 | -5.87274 | -57.75762 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aa6f82ba-b00e-3c57-9c14-992f6d815b04 | -6.86264 | -52.79502 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6e0c7fc-b2b3-3a5d-ab3c-83a02fde30ca | -6.82806 | -52.81289 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2945fab5-7157-3122-adfc-39331f71b279 | -6.25751 | -57.89911 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81a4b434-be4a-34b3-919e-157ca12fe760 | -6.83702 | -52.83689 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5dd3879-f62f-3af3-b228-378613f35db6 | -6.83765 | -52.8324 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42584931-59bd-3436-8698-4bc942072553 | -6.43953 | -58.13164 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9c0fa92-1573-341e-bc79-1699a42e64fe | -5.87465 | -57.77421 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6daeaa36-94ea-313b-9e90-4542004582fe | -5.9233 | -57.71164 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 866a3f17-2a3f-311d-96e2-078519ed9ed2 | -6.43533 | -58.13102 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 15bfe0e6-b8e6-3d48-bbe5-dae19495552d | -4.5237 | -54.97442 | 2025-09-03 05:33:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 122d11e5-388b-3386-ad66-459854eeb374 | -6.81007 | -52.81966 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1973c4ad-418a-35ee-8eea-05d9bfdf8401 | -6.33363 | -58.17554 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ed8aced-6b21-3da1-8775-29cfcc7df7e0 | -2.9351 | -49.45716 | 2025-09-03 05:33:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7f4cafe-d7ba-33b2-b9f6-927e7e8c7fb1 | -6.04798 | -58.00377 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7fc99f5b-75b3-3c8f-8437-3d3690a4dd21 | -5.91478 | -57.73916 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7eedd141-8271-3345-b493-8e87e8a86e30 | -6.85051 | -52.79341 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ecfc3361-1f5a-32d7-98c0-1d7f4409d839 | -5.9292 | -57.71992 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 4e781137-5bbe-329c-a435-3cd7995be986 | -4.52919 | -54.97229 | 2025-09-03 05:33:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6c487b4-4aed-377f-9260-06d4d3cadb10 | -6.79229 | -52.8041 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5443bba3-3bd1-35cf-92bc-6d4999812157 | -5.86123 | -57.77662 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 3df62236-6836-3c79-9936-be1fa5ac3a48 | -5.86552 | -57.77707 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 70c1927c-768f-3793-9478-33d3675a473f | -6.26233 | -57.89585 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84e4c0b9-0a98-37ca-b754-c8ec8104af29 | -6.79839 | -52.80455 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 642f5d4e-dbfd-351d-b9fa-1109471b44a4 | -2.94294 | -54.80386 | 2025-09-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78f0fbda-5fad-3ae3-9444-548c04b010fc | -6.8458 | -52.82878 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b47fac99-111b-37be-a735-70d2b2fbed81 | -5.86238 | -57.76878 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| a0273850-25b2-34bb-8959-878c2c228872 | -6.83193 | -52.84053 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 652e78ce-8136-3bfa-8a0d-a5c71ecd22eb | -5.8698 | -57.77755 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ea6e1ed9-58c7-3345-8d46-d8b05314810f | -5.10831 | -56.9683 | 2025-09-03 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee8fb12d-7f02-372e-889f-7c664f2a6155 | -2.93418 | -49.46358 | 2025-09-03 05:33:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d277532-d91b-39a5-a843-f68898a7a53c | -6.84433 | -52.82871 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0e5c01dd-720e-38d9-b351-e50c097b0293 | -6.82136 | -52.81675 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 901c6505-c0cb-38cc-a81e-a5f2de901865 | -5.90681 | -57.73408 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 862185c3-4370-3c5a-9c81-a10b700c4510 | -6.83411 | -52.81367 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca2ad74e-afe7-3b3e-8bb3-512aff400822 | -6.54 | -56.20118 | 2025-09-03 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae4c0094-157c-37da-b439-4948a834b6c3 | -5.89341 | -57.73598 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f4b2017-cf45-357d-8b57-9d7c0550daef | -6.79657 | -52.81782 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 777b663c-c478-3131-bb31-7b3e8d0adbb0 | -5.91111 | -57.73456 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 27e38cda-7d56-3771-8c52-d3addb7d2f24 | -6.82744 | -52.81733 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0af4b6e8-de46-3c34-9273-14dcd1c3cbc1 | -5.90866 | -57.72173 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 068679ba-4ba0-3481-8e48-4c7f595bf3ae | -5.91354 | -57.71836 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2cb72be3-f6e5-34f8-b3d5-99b6e8c60c9e | -6.75672 | -56.39594 | 2025-09-03 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 006644b4-124b-3998-a980-82c53ef0eb6d | -5.9172 | -57.72313 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a45efdb1-3e70-3258-b3f7-569704fd44ac | -5.90926 | -57.71768 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 66a28f27-0a67-3433-bdc4-b2e0dd473979 | -5.86298 | -57.76474 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 32eb15bc-d535-359b-b757-9d8194479d26 | -5.9166 | -57.7271 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |


[Clique aqui para ver as próximas entradas](README103.md)
