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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87e6c701-e1d7-3838-b612-b293eeab3dd8 | 2.78894 | -50.92833 | 2024-10-26 05:33:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d8fc5456-5c7e-303b-9bac-ada9680c6602 | 1.00769 | -52.21955 | 2024-10-26 05:33:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bdf88d65-dab7-367c-aabf-1a03cc41698b | -1.59865 | -53.30914 | 2024-10-26 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b18d63b-13f7-3a8f-9095-dc1a2a92458d | -1.59326 | -53.30832 | 2024-10-26 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cda1c98f-ca43-3c5d-96b6-552d14695f03 | -1.58146 | -53.31334 | 2024-10-26 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 840b9b2b-afab-3b4b-b569-41997ad6a757 | -1.57658 | -53.30918 | 2024-10-26 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 878da92f-9844-394c-9fbe-3fe422913094 | -1.58787 | -53.30748 | 2024-10-26 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| efd3b635-2d8b-319f-b4be-a3953f29b550 | -1.57607 | -53.31254 | 2024-10-26 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c271075e-10f5-31f6-ae70-1afd48b9b905 | -1.55803 | -52.05932 | 2024-10-26 05:33:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 300abc02-c0e5-32a4-a4d4-01c061a3318d | -1.55739 | -52.06352 | 2024-10-26 05:33:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09acff57-24dc-38d2-a460-c17286ea4866 | -1.60833 | -54.77615 | 2024-10-26 05:33:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dae9c0d7-661e-3acc-adc8-598667f7ab8f | -1.35308 | -54.60936 | 2024-10-26 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 587591e2-ef02-36ea-ad88-51632e8f048c | -1.34815 | -54.60874 | 2024-10-26 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4186f6a5-e1d1-3b04-9d69-f7d6a2a6b5fb | -1.34728 | -54.61449 | 2024-10-26 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cdd2fe0b-5d62-38b9-a67a-ae7930d6f609 | -1.34236 | -54.6138 | 2024-10-26 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d2af3cee-f25d-3b2b-90e9-ba1461a1761d | -1.34024 | -54.61295 | 2024-10-26 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a92c5e26-b958-3fe1-9412-6bd3012e3e9a | -1.18861 | -54.20387 | 2024-10-26 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4edf9744-1133-32df-bce8-c321a440a987 | -1.18376 | -53.66478 | 2024-10-26 05:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89a8f5e3-1221-3806-942c-95e1a53e2ff0 | -1.18326 | -53.66806 | 2024-10-26 05:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10a3365d-c951-3f00-90a2-128e8e60c66f | -1.18276 | -53.6713 | 2024-10-26 05:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efe7174e-4616-3eb9-8950-49b1860ea90a | -1.18228 | -53.67447 | 2024-10-26 05:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e525801-34b4-3da7-96da-69357090c576 | -1.17962 | -53.8995 | 2024-10-26 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a92f07f-a553-3413-9265-a40582b82629 | -1.17913 | -53.90264 | 2024-10-26 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 397725a9-c7b3-3038-aa85-1033414ec2ea | -1.1377 | -54.10343 | 2024-10-26 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c7e283b9-b821-3049-9f37-9d63dd6af4d9 | -1.13723 | -54.10643 | 2024-10-26 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4930fbdc-a757-380d-aec4-34aaa59a0ba8 | -1.07191 | -53.65719 | 2024-10-26 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b3ef2261-3e6c-339c-8f1a-11d0987b98ad | -1.07138 | -53.66066 | 2024-10-26 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9b055d77-5c7d-31af-81a0-058de2a0133d | -1.07089 | -53.66391 | 2024-10-26 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4266bce9-fdfd-38f5-a6fe-fe1fba83120e | -1.07043 | -53.66694 | 2024-10-26 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 072b091e-7f8f-3daa-bbc3-44659f4f0891 | -1.06522 | -53.66608 | 2024-10-26 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a3b963f-421d-385e-af6a-ac50a8739749 | -1.06475 | -53.66916 | 2024-10-26 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 141230af-0bf9-3247-8aba-3f6db46e208a | -1.04 | -53.51516 | 2024-10-26 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dccafbf4-132b-3402-88fc-d2f758199d67 | -1.0395 | -53.51836 | 2024-10-26 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00999002-ad49-3932-8ec9-bbb2d20c215e | -1.03475 | -53.51421 | 2024-10-26 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fce03b65-469d-32e2-88a8-162c9f4fd743 | -1.03425 | -53.5174 | 2024-10-26 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9245ec7-b666-306a-bace-efa0c42d7123 | 1.57772 | -55.6497 | 2024-10-26 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60d0d7aa-d245-3108-9b8b-e2a1b958c5f6 | 1.57704 | -55.64548 | 2024-10-26 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64a88508-97f7-3533-ac18-789f64be257e | 1.57201 | -55.64198 | 2024-10-26 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 346029eb-182f-3494-926d-9d6965ad4f05 | 1.56765 | -55.6427 | 2024-10-26 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 83de12a8-afbb-31b3-bff2-1630d2917c7f | 1.56261 | -55.63919 | 2024-10-26 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4b8534e1-365e-373b-aacb-9a4a2d9b5494 | -1.71216 | -56.01752 | 2024-10-26 05:33:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce674c09-e5cb-3c03-bffe-379873bbb329 | -1.68408 | -55.30666 | 2024-10-26 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0153d36f-db6d-3f56-bb5d-b9d5298c93ca | -1.52874 | -55.41013 | 2024-10-26 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 856422bd-5b9c-3e0e-adb8-49daf34c3ce9 | -1.52771 | -55.40602 | 2024-10-26 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd568766-02cf-3e4f-b9cd-de0980cbcd40 | -1.5261 | -55.9102 | 2024-10-26 05:33:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ee7637c-a71a-3c46-a0a6-af418b83d717 | -1.52351 | -55.37008 | 2024-10-26 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f6b8873-9575-3d0e-87ee-29d4c6cd3e41 | -1.52091 | -55.3686 | 2024-10-26 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d408d19e-2cc8-3e63-9d74-eace1ada9cf3 | -1.49111 | -55.86766 | 2024-10-26 05:33:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 130d8ea9-88a7-3d81-8173-774ebb1c8122 | -1.4695 | -55.82706 | 2024-10-26 05:33:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fca0b017-5978-3725-97f4-a92d293c573e | -1.38798 | -55.40625 | 2024-10-26 05:33:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c1b07533-479b-35e5-914a-a5ff784e8e82 | -1.38329 | -55.8351 | 2024-10-26 05:33:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a75e117f-4e19-3f4f-916c-681994057d35 | -1.3826 | -55.83966 | 2024-10-26 05:33:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0df965cc-34ef-3bc1-b648-27a36a089fc7 | -1.3819 | -55.84422 | 2024-10-26 05:33:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6fd37565-6ffb-3a5c-95ba-890af261afac | -1.37466 | -55.86157 | 2024-10-26 05:33:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ec1858e-f09f-3271-8d2c-14949bd6d724 | -1.37016 | -55.86081 | 2024-10-26 05:33:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f146d92f-17f3-3aba-824e-16cfbf3a2225 | -1.35531 | -55.49493 | 2024-10-26 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20ebfb98-9a52-38c7-996f-b7165d2a9389 | -1.35069 | -55.49424 | 2024-10-26 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32d8b7b0-e850-35ad-8e1f-a3684f5c4ddc | -1.3458 | -55.73814 | 2024-10-26 05:33:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1448adb0-9ab3-31eb-8e44-c129c925e672 | -1.28885 | -55.71523 | 2024-10-26 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6830cd22-1eec-3d7c-a4be-5b514eaf9831 | -1.28816 | -55.71981 | 2024-10-26 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| db2ba0e9-66a0-316a-a009-4eb1d39a4c6b | -1.21808 | -55.89207 | 2024-10-26 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 06757bff-97b7-3d13-af8f-a55d16001e99 | 1.30067 | -60.4143 | 2024-10-26 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e38728f4-5dad-378e-aba1-899832c34d24 | 1.03814 | -60.05994 | 2024-10-26 05:33:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e2419894-da25-39b8-a656-a191ce2f66cd | 0.71088 | -59.87692 | 2024-10-26 05:33:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2cb45f80-f767-359c-9143-93bf679bc921 | 4.33629 | -60.21983 | 2024-10-26 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 333258ef-09c7-3443-89f8-b5ab628c35eb | 4.33574 | -60.21636 | 2024-10-26 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54936683-9b95-3ded-b0ad-66e34b0621ff | 3.15073 | -60.71017 | 2024-10-26 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 470e0ed7-d6d1-3992-9b58-4c8c7871fac2 | -2.9945 | -50.4816 | 2024-10-26 05:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 99a55c38-826d-3ef1-ab02-c150d1d10c18 | -2.9501 | -52.5708 | 2024-10-26 05:35:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 423d6b7d-701f-3d86-acbf-ea44cf36c564 | -3.013 | -50.481 | 2024-10-26 05:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 9936706c-42b0-3395-9feb-1cd6ca3ed948 | -3.473 | -43.3144 | 2024-10-26 05:35:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| e07167a6-5e29-3b64-9954-67777abdea1a | -3.4729 | -43.3377 | 2024-10-26 05:35:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 178061e3-3bd5-3ad3-a0a4-7172d33fd498 | -4.5614 | -48.0141 | 2024-10-26 05:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 2cc74d88-c0b3-3813-94f3-754e744c8b73 | -4.58 | -48.0132 | 2024-10-26 05:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 200.4 |
| 14ed75c7-0f4a-327f-b153-dfe6bd33db02 | -4.5799 | -48.0349 | 2024-10-26 05:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 152.7 |
| e635d1f1-a77e-3eb9-8c3d-68628407ecc0 | -4.5613 | -48.0358 | 2024-10-26 05:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 50dceef5-bb1f-3561-b1a7-dbeba032d842 | -4.8026 | -42.8665 | 2024-10-26 05:35:32 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 5cfc56d8-3b74-3c68-80bb-5da31a86d562 | -4.8024 | -42.8899 | 2024-10-26 05:35:32 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 91.6 |
| e194467f-9238-39cb-b894-d3b603d54f10 | -4.8213 | -42.8652 | 2024-10-26 05:35:33 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 58.3 |
| d31148e6-5be1-330d-88cb-1c8300567371 | -4.8211 | -42.8887 | 2024-10-26 05:35:33 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 75.7 |
| d14f45e4-5d0f-3ff5-9a3c-0e529840319a | -3.46111 | -64.97392 | 2024-10-26 05:36:00 | NOAA-21 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23efd5b4-cb7f-3024-9eee-60a544b47901 | -3.00671 | -50.48949 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 810331d7-0804-3df8-b173-ae0f82705f11 | -3.23809 | -65.18451 | 2024-10-26 05:36:00 | NOAA-21 | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8828653-4ecb-357b-9986-79d617c7dd2b | -3.19426 | -64.75161 | 2024-10-26 05:36:00 | NOAA-21 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fad3c7e-046d-37a8-b6ba-f0453289b527 | -3.19368 | -64.75527 | 2024-10-26 05:36:00 | NOAA-21 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e72a40ae-0057-3338-973c-aaccf7a3b16c | -3.12321 | -64.78181 | 2024-10-26 05:36:00 | NOAA-21 | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58589773-0f9b-36cc-8b89-e7febd76ec0b | -3.01744 | -65.46089 | 2024-10-26 05:36:00 | NOAA-21 | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c66a16d1-98a5-3e75-b972-0c48423bd23a | -2.60024 | -67.40415 | 2024-10-26 05:36:00 | NOAA-21 | TONANTINS | AMAZONAS | Brasil | 1304237 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| db5988a3-a05b-35cc-bbf6-36f5fca4441a | -2.5846 | -67.40171 | 2024-10-26 05:36:00 | NOAA-21 | TONANTINS | AMAZONAS | Brasil | 1304237 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c37fdc0-6f4b-342b-a427-ae4aed51e9dd | -3.15596 | -50.46181 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3a357590-11f2-3435-af82-1435f5e7a6cd | -3.15169 | -50.45624 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| be54d8fa-e0ed-3bdd-be97-ae98819e1aa1 | -3.15082 | -50.462 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 67dad133-0a68-36e9-9673-374d375d2e84 | -3.15018 | -50.45499 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 71bd5f80-3ded-3bc6-b527-5de898427ab6 | -3.14935 | -50.46077 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9be9f720-c959-3a18-bed3-8d634921106d | -3.14508 | -50.45525 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cc67b756-0b3e-3274-8a19-0536aebb8afb | -3.01972 | -50.48191 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c3f0c1e1-4bd2-3f83-b8bd-dd7955b4bd65 | -3.0189 | -50.48761 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a962b319-bdc9-347d-b61e-fa21c16b5d93 | -3.015 | -50.47912 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| ccd4adc6-0784-3c2f-af19-86f08479ae0f | -3.01414 | -50.48483 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 118a3add-1b0a-38dd-b11e-142c0f8f0247 | -3.0133 | -50.49048 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |


[Clique aqui para ver as próximas entradas](README93.md)
