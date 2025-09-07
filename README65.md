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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0fa4e0c4-8f6d-3eac-92b8-c203ede476a1 | -3.9001 | -55.83833 | 2025-09-07 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f454227-9b8e-3f50-b221-3b4fd15aa775 | -7.75077 | -48.81714 | 2025-09-07 05:10:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fdc87780-945d-3a5c-835a-cf1c02b3e8e3 | -5.68977 | -48.14074 | 2025-09-07 05:10:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7e4dae33-3959-3cfc-b7f7-ebde31a36298 | -6.09074 | -57.71746 | 2025-09-07 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4be6eab8-78a9-37f9-b28a-c5fcdf3647e7 | -3.24688 | -50.79913 | 2025-09-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 67007c41-25a5-32a3-9d34-53cef763977f | -4.2733 | -48.18408 | 2025-09-07 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 67013c36-0db4-33ee-9975-aa787644ba66 | -5.09951 | -56.15343 | 2025-09-07 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bce7a6ef-932a-37b9-afa2-9468035aec2b | -8.1134 | -45.31444 | 2025-09-07 05:10:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f52840d9-d755-34fd-94ee-12d36dce49bf | -5.22118 | -43.69418 | 2025-09-07 05:10:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8ea157a8-2a4a-3994-b1d4-23f30c2df1ef | -6.81517 | -52.81015 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 01a7933d-eeda-3746-ae5f-e64b36adf9df | -3.34803 | -47.6126 | 2025-09-07 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 236eaf5d-83b3-3e99-b1d6-babe6b01fb97 | -3.90623 | -54.68303 | 2025-09-07 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 92c3ec0f-4435-397f-a0b5-02e112b1c9d3 | -3.24568 | -50.80722 | 2025-09-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 3371f864-5e37-35e9-8d55-619f8018c9e3 | -4.89904 | -49.92957 | 2025-09-07 05:10:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e253d069-f07b-3591-9138-1c5db41b5507 | -7.74899 | -48.83041 | 2025-09-07 05:10:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1137f5d4-510d-3085-a15e-b8ccafa8aca0 | -7.81429 | -45.43343 | 2025-09-07 05:10:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 81236067-9239-32a8-bd24-cacabf51d752 | -7.68111 | -47.33181 | 2025-09-07 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c589d7c2-59ce-33dd-ab77-380c7b4042e2 | -5.79216 | -57.5605 | 2025-09-07 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 075f9f56-496b-3942-b1dd-3d8c1722698c | -5.04227 | -45.45235 | 2025-09-07 05:10:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ed88bea-70e6-36c1-9d16-b5405ad6fa62 | -3.37823 | -50.85048 | 2025-09-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13b37141-a173-307c-82fe-de12bb36e030 | -7.81472 | -45.42066 | 2025-09-07 05:10:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 32c5724d-2251-3d13-8ada-8197117b585b | -5.96902 | -53.5819 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee8dc061-084b-3cc8-81c7-d55d322e7231 | -2.6281 | -46.83339 | 2025-09-07 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2772e894-1455-3786-b11c-7ad509c51d99 | -3.58879 | -47.5122 | 2025-09-07 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| e419ab6c-5846-36fb-87d0-a5f2b57383c6 | -6.29928 | -55.19878 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a5264c06-ca9b-3c8a-9162-6c4b5ecccc83 | -6.82053 | -52.8095 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 583d44ef-968c-33b3-ab1f-b4fa9d19b9fd | -2.78763 | -49.61907 | 2025-09-07 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3ada2afa-9758-3bcd-8bfb-bba6a6d94f0e | -8.34212 | -46.94042 | 2025-09-07 05:10:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4bbf13a-544c-30c9-9c50-f575982e084e | -6.44112 | -53.39844 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a645ce8b-7397-3cce-9566-f79ffdfaccce | -7.97798 | -44.95049 | 2025-09-07 05:10:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cd06b9d9-0c55-3088-afee-9b863302d475 | -7.73667 | -50.31879 | 2025-09-07 05:10:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e45df82d-b3ee-3474-921f-fb395bad0512 | -2.43649 | -49.30592 | 2025-09-07 05:10:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 852a2954-74f4-3141-ab93-3870b0b744b9 | -5.06424 | -56.07216 | 2025-09-07 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 07da26d1-65af-30d5-807f-80bab20643a9 | -6.60824 | -48.05584 | 2025-09-07 05:10:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 65cece93-ed34-35d8-8e4d-154ea4cf9feb | -6.30449 | -55.18782 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ddc7d4bb-19f3-3317-a581-9a672595c33d | -6.29986 | -55.19495 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a691da61-6014-333e-a3e1-e0c60f3e4189 | -6.26925 | -53.43534 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be15ad67-adc8-3e71-b953-0c50bed9f236 | -2.43572 | -49.31095 | 2025-09-07 05:10:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c9d05a02-dce0-3cdd-800e-26360da14a09 | -6.82526 | -52.80497 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 572faebe-7d28-3ae5-ba9e-6fc577ff96f5 | -5.21919 | -43.69468 | 2025-09-07 05:10:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 7f4a439d-df64-386e-86fb-db560a442155 | -5.64288 | -51.7981 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4200d1d-338a-3ba3-b4b0-391df5a05976 | -3.59473 | -47.50954 | 2025-09-07 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f2b572fc-5fd8-3b2e-9248-2a5e316a92c0 | -6.14945 | -57.95034 | 2025-09-07 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71a67451-0a68-347c-986c-8d367eb59c52 | -4.25826 | -48.54549 | 2025-09-07 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2b55ae49-b405-3859-8c23-ff847e37f870 | -4.48196 | -48.11602 | 2025-09-07 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e4341fa-eadc-34ce-b7f5-3fdfe16cae19 | -6.20174 | -53.26621 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd891619-d234-3608-ba0b-0d6244761dca | -5.57777 | -49.08706 | 2025-09-07 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 26bd0bd4-db54-37a9-afd5-5ecd9434e133 | -6.8112 | -52.80956 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 85fb3a82-b212-341a-a3f7-e73ede8f9a39 | -6.09404 | -57.71798 | 2025-09-07 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d67d169a-89de-3c08-bfc9-cde5c270b7ad | -5.19436 | -56.02315 | 2025-09-07 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4f43cc19-b657-307a-86e5-67968dc1433e | -6.27822 | -53.42719 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ea93e7b4-0a81-337e-a790-0f73c042f69f | -7.815 | -45.42797 | 2025-09-07 05:10:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c6c2a4a0-bee4-331a-ad72-ac4bf5f10216 | -3.39452 | -52.84243 | 2025-09-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2533f9b7-2978-3cc3-93e9-8087e2eae7a3 | -2.62755 | -46.83713 | 2025-09-07 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1e58e88-79ba-30ce-a6b5-3f79e317b8f9 | -5.97891 | -53.59255 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| baf78f84-e696-3d6f-ac84-ed4187ed32fa | -6.78088 | -52.80359 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 08b6bfc1-1618-3bed-aa1f-b187fb52334a | -5.78609 | -57.55603 | 2025-09-07 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3602255f-ca00-30d8-9840-26f7f91b9c2e | -7.68808 | -50.313 | 2025-09-07 05:10:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 25b7ed83-d65f-38f7-85db-91de228e6a7f | -6.28061 | -53.43707 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ac50397-93b6-3ab4-b913-6b8e3f64646a | -6.27542 | -53.44578 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| baa6ab57-e399-3fbe-bab3-a739a2fe58c9 | -5.87448 | -45.07907 | 2025-09-07 05:10:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e9173766-008a-3af7-b73b-b8c55ae2a0e7 | -3.59503 | -47.52205 | 2025-09-07 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 821e9156-1154-3deb-9f7d-265da0d09279 | -6.26995 | -53.43071 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4db97c2-8848-3a76-a9f5-7fe8fbf33f8c | -3.90343 | -55.83884 | 2025-09-07 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9df9fd44-795c-303b-b67d-df17561c94d0 | -6.27991 | -53.4417 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e949c1fd-9534-3625-8a34-0269b1350590 | -4.32996 | -48.39275 | 2025-09-07 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dfad595c-b45a-3fd5-bae9-5efc4549eda4 | -2.79155 | -49.62458 | 2025-09-07 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9bb8683e-e34b-3781-9410-cebcf39e08eb | -7.68403 | -50.30731 | 2025-09-07 05:10:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8ab3326a-6628-37b1-a316-2ab4b58eae4b | -7.81581 | -45.42178 | 2025-09-07 05:10:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9a3a13a0-bc34-3cbb-b990-166f66e85b63 | -5.482 | -45.90953 | 2025-09-07 05:10:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4fbbbd4-a23c-3e24-890d-064675bbe958 | -6.27373 | -53.43127 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e7cdd5b-a9d5-3350-966b-dec31c0472e8 | -6.27043 | -52.80879 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5a1575e1-ee19-3ad5-8e38-b5b10cd2c2df | -5.98954 | -44.14597 | 2025-09-07 05:10:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 2158d223-6afb-3e2d-954f-2c832d931944 | -3.82549 | -54.1258 | 2025-09-07 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81f7f62a-d182-34ee-b4f5-60b9523b2496 | -6.84175 | -52.85054 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 814595b4-1266-3aea-a244-2435704cb6f2 | -6.2851 | -53.43298 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfb2f116-1ac6-3408-871c-b3452535a8dd | -6.83727 | -46.39606 | 2025-09-07 05:10:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 010b2bef-a164-391a-bed3-02eb51edd5f2 | -7.68181 | -47.32669 | 2025-09-07 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c5254de0-5265-3681-bebb-10a443daacf0 | -6.20058 | -53.26791 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9f2a9f5e-724d-33c7-8923-05f0a48eb1c1 | -6.82058 | -52.80062 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 60017af6-21e7-393a-bb0d-cc7f14af1d01 | -5.9954 | -44.15518 | 2025-09-07 05:10:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 0b6cffde-0d5f-399c-9cd0-d22f84de867c | -7.67927 | -50.30663 | 2025-09-07 05:10:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a54209f6-d7ed-330b-bbdb-f67edae6ba50 | -7.74988 | -48.82377 | 2025-09-07 05:10:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 31ae9feb-251f-3794-a63d-630da40da923 | -7.63554 | -46.55547 | 2025-09-07 05:10:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 84a1211c-1c74-3fa4-9ee7-ea1a2afb3e56 | -3.45142 | -52.72382 | 2025-09-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf02f6ce-d068-3982-a600-738470d8a7d9 | -7.71388 | -50.33639 | 2025-09-07 05:10:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 317479c9-0467-3199-b685-cb5d47645ee7 | -6.20824 | -53.26898 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d8034f96-d00b-346d-8030-ee6754851086 | -6.72995 | -50.4583 | 2025-09-07 05:10:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9b85d43a-656f-39b9-9f60-8bbeb1dd2561 | -8.14682 | -44.88383 | 2025-09-07 05:10:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 11099036-3b05-3dc1-8c94-4be868b86055 | -6.81445 | -52.81524 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ca1e868-12c8-3463-8354-cd8f9791e923 | -7.97576 | -44.94866 | 2025-09-07 05:10:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c4def791-3b41-3d1c-96bb-f1d91db666ab | -4.27284 | -48.18729 | 2025-09-07 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a67abdd7-e1a0-32a3-9cfe-36e374f485fc | -5.78939 | -57.55655 | 2025-09-07 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3067d5be-730f-3aa2-9043-16a1c842c7be | -3.72977 | -53.78465 | 2025-09-07 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a5e5dde-670f-3b62-80e0-763bc2aa47e6 | -3.78922 | -48.91355 | 2025-09-07 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7add7b36-9111-3773-b6d4-2046afabdac5 | -6.91745 | -45.19828 | 2025-09-07 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 47b51e40-9962-37f5-ba99-be7628457dea | -6.27752 | -53.43184 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2febe407-f82e-3dfc-9474-74930f4a4128 | -2.42707 | -49.30449 | 2025-09-07 05:10:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2589198d-ca3b-3474-ad83-6d4ff1d86434 | -5.58775 | -51.91331 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09693c6b-2f79-394b-8e54-4be79db6a3ea | -5.9561 | -53.79742 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README66.md)
