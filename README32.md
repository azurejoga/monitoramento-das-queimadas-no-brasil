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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a66b30f-04dc-39d6-a75b-ed0f7f67502f | -3.26401 | -50.60588 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2bd1aaf7-a504-3169-aff6-39289cb36879 | -0.13771 | -51.45752 | 2024-11-13 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da064b42-4804-32dd-9f9d-89e5f66f79e7 | -3.61369 | -51.53944 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf8e1ffc-aa39-3712-99df-cdd6de0b36a9 | -2.37698 | -48.5141 | 2024-11-13 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dd40532e-5b9e-3b56-b1c6-a295dfcb02ca | -2.57243 | -54.03621 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0e059677-4395-3280-bfdd-398cfffd581b | -3.20014 | -53.85314 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc1cb7a9-1e04-32a0-bcb7-c311f557504a | -1.25638 | -51.62814 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1b7cf9c-d4b8-3f71-9340-5b1a1cbd07e6 | -3.83878 | -52.17168 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa2ca05f-82ba-316d-99fd-0f919b0cb943 | -1.61836 | -52.51972 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1618959e-f31a-3a28-ac5c-511db0f4ad11 | -2.63397 | -46.1711 | 2024-11-13 04:57:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4f921a35-2727-3a9b-b1b2-6af70ff0798d | -0.94678 | -52.39793 | 2024-11-13 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05525de2-7a73-3228-bd92-bc14322a29e3 | -2.44401 | -53.66377 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4699dc3a-fc1e-3656-b66d-3e0a71368918 | -1.41045 | -51.10873 | 2024-11-13 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8db1fa78-37cf-3f3e-92ce-9aa5a761b8df | -2.66291 | -51.72156 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fabd621a-a5de-3780-82f7-b368eb330846 | -3.85733 | -51.91597 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46b88455-4bed-3cb2-bef7-1cc66aeceb8d | -3.87448 | -53.69514 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bbfcfbb4-a010-321e-a1f2-7a0f855a7718 | -3.735 | -54.43501 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e2b916fe-b74b-37f8-833c-d50f127c7521 | -2.37541 | -48.52459 | 2024-11-13 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8bbecba2-b143-3bbc-b17c-abe925593e9d | -2.30912 | -53.9809 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0fb8181-1d4f-385d-a83a-58dbaaa1212e | -2.81999 | -53.997 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6dc7abd3-af6f-3c23-aca0-4f56609d079c | -2.36739 | -52.13869 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9522b5e1-48cc-39dc-957d-e520e729f3f8 | 0.81063 | -50.67639 | 2024-11-13 04:57:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0761f631-6ca9-3a67-8694-30d0b38b82fd | -2.38831 | -53.66922 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0da4767c-76b9-3c06-b354-843315823d38 | -3.04767 | -50.32528 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a5cebe59-e9e7-37ee-99ea-17ac2b74796d | -2.12051 | -50.6958 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5dc247a9-4feb-340b-80dd-81873d4cf05e | -1.77151 | -55.61288 | 2024-11-13 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2b557d82-b80a-33cb-b774-cac812376012 | -2.82022 | -46.65703 | 2024-11-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20f34963-45b3-351e-bb39-5fe283ba451d | -3.70209 | -51.27708 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 584d1736-e07f-30c1-af86-105ed9a7491c | -0.13996 | -51.55326 | 2024-11-13 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67132794-ebfc-34f7-bb78-96a46f09ec4e | -2.32174 | -50.68356 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6701fa4-15b3-3308-96e6-4d3ae5457b30 | -3.34006 | -50.10095 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| be2ea05d-0959-3d44-afb7-8cfaf6cb0315 | -3.02252 | -48.04071 | 2024-11-13 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f100b62e-1ee4-3008-986e-3e0c0592dc47 | -3.09184 | -51.07307 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a806eba-ffce-3e97-bfa9-134d32f50ec6 | -1.613 | -52.4013 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f742d5fd-612a-37d3-b7db-6a56f982c803 | -1.33662 | -51.42434 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57c44f9a-313b-3eeb-8a74-e49329da93c8 | -3.2544 | -43.25854 | 2024-11-13 04:57:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 21fd0d24-1a23-3b7a-8d14-c3d47f73e16a | -3.20233 | -50.63567 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3220b340-89ee-3ffc-acb3-fe65b7b8fb1a | -4.03251 | -55.87827 | 2024-11-13 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fd3c8fd7-65e0-3f8e-a6cc-374a858438a7 | -2.66507 | -46.81676 | 2024-11-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b2605eb-31bb-3274-934f-00e8cf9fd70a | -2.25095 | -52.07719 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf45169d-5ee1-3920-8f7c-874d678b4cb8 | -3.31043 | -54.19075 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61495292-edd3-3773-af9c-8d476a75175d | -4.68961 | -50.75836 | 2024-11-13 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cac97079-48a8-3731-be6c-f26e0666360d | -1.6217 | -52.6516 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d00adcca-ee3f-3bb1-93c6-bc38d221116f | -2.184 | -53.25776 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb3d468d-b2e6-36e6-93f4-b7509e99f419 | -2.9361 | -53.23086 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef11d9d2-4935-3224-92ef-1f4fc9f3c64b | -0.3651 | -51.74078 | 2024-11-13 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e43cb65b-e0fe-3a81-ad06-bb152cfe8e12 | -3.09087 | -53.26588 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b8e9d12-d0d0-3d99-889c-f5f80aa378f9 | -2.05768 | -53.4137 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 127f76ea-efdb-3c88-b138-6efafa1bc95b | -4.32847 | -46.54188 | 2024-11-13 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e1ab4570-1146-33c1-839f-57fd57694bf0 | -3.10726 | -53.70793 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4cc00e83-5140-3e66-af34-9a4035f2a473 | -3.06836 | -50.3404 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 067227f7-f895-32ed-ad53-2cbb0b8a5fb2 | -2.31243 | -53.98141 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6efd5fb5-903e-3748-b39e-0b8633890780 | -4.13634 | -46.70776 | 2024-11-13 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9171f61-2f24-3a00-b4a8-0061a230a742 | -1.41508 | -51.10173 | 2024-11-13 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37c98702-6c77-312a-9301-4a7caed3a8a4 | -1.76459 | -55.61184 | 2024-11-13 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5cb3b8c0-e4b7-3a43-a6ee-9bcd6a297333 | -3.54973 | -51.49474 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19c1589e-f265-3d8d-833f-4a93852eee3e | -2.97884 | -45.15953 | 2024-11-13 04:57:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 55df7041-4fa1-3d8a-b3d8-4825f0df95f1 | -2.47991 | -53.97541 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1d1fc35-0e2f-38b4-9037-55b5184556aa | -2.70996 | -47.72857 | 2024-11-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f34b797-b4a9-3c71-9d1e-1c360e639857 | -2.53406 | -47.09075 | 2024-11-13 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68495ca0-b36e-32de-8f7a-28db33fc30aa | -4.17266 | -55.09429 | 2024-11-13 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ad96ef0-98df-35d2-bf2f-538dcde4aee3 | -3.09418 | -53.26639 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4f13726-2845-3bc6-91f8-58dc14022d1e | -4.37009 | -48.08426 | 2024-11-13 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ea74197-81ea-30c4-82f6-2159d30ba646 | -2.06365 | -53.39707 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 753e7b1d-53cb-38c3-a73f-fbd23c9dc45c | -1.26056 | -52.1319 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84e6af3f-8b36-3ff0-a667-14218ae00f2f | -2.93816 | -49.42515 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f3f49ec-914c-3511-b8a8-bfe7548d8472 | -2.21312 | -53.74758 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6edf93ed-269a-322b-ba8a-d4d640869c10 | -0.91699 | -51.75646 | 2024-11-13 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66eedb1b-cd94-3686-ba47-f8b0056410de | -3.80195 | -52.09529 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8940cca1-7b44-36ae-8b7c-2c9206bb8c5f | -5.90481 | -46.23241 | 2024-11-13 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6552fd95-0019-3f2d-8763-929f83d258ad | -2.64021 | -46.16167 | 2024-11-13 04:57:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bdb9b0c4-c8bc-3a08-bdde-e8e57e0d14b7 | -2.14876 | -46.40635 | 2024-11-13 04:57:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 94c4f241-da53-3f46-8752-be6dec37593c | -3.95587 | -46.40703 | 2024-11-13 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f0c6ecd-de03-3c1b-b675-c50f32b00d9a | -2.56505 | -53.9751 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 677e3691-4478-3da8-a02f-385c76e3bfb8 | -2.73278 | -45.29314 | 2024-11-13 04:57:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| aa142bed-7f4e-3e2a-bc1e-ab8fd3556890 | -2.17962 | -50.59343 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba303a03-4c5d-359f-b9f9-0e120af5f38a | -2.88701 | -54.11381 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a4cb575-9bb9-3c3f-83c1-ede54a996ce2 | -3.52603 | -54.48718 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6b8d09c0-17b7-3c10-b65a-ed16d1accf60 | -2.22398 | -51.99295 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7974e82a-4ba0-3ac9-b95f-033366c2bac2 | -1.62245 | -52.23075 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a78b3e6a-ab80-3364-b188-f998bd9a60b3 | -2.17548 | -48.44033 | 2024-11-13 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d44107c1-7afc-3abe-85b3-0d7688aa8e3a | -2.95328 | -54.21254 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45ebf35a-8d88-3544-889c-eee645c9db20 | -2.21143 | -53.73677 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d1696f9-6694-3a81-a586-a5a7aec2a5c0 | -1.66266 | -52.54078 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9232379e-2a63-369b-9f3f-5929462496de | 1.06576 | -60.60743 | 2024-11-13 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.6 |
| d1f8c904-86f5-39f3-828d-e849e5d81831 | -2.58562 | -51.9227 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc2c9a00-7b52-31eb-b3d4-dc050efb2620 | -4.12762 | -46.86052 | 2024-11-13 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5f3aa89-9065-3091-9a2a-0267df7e503d | -1.60778 | -52.50031 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b2c34159-df0a-3d44-8682-d1a546e76556 | -2.88778 | -54.17402 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b65900b-4018-3949-9f9b-de94b252b8f2 | -2.85939 | -54.09544 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8a08cc89-473d-3dde-b529-2071b0865428 | -4.40312 | -49.9597 | 2024-11-13 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| abd0fced-d50f-3838-8763-41c58c58ee3d | -4.32754 | -48.61342 | 2024-11-13 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f843ce5b-ff73-3682-b713-759113ce30a5 | -2.24285 | -53.75215 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 71680e1b-64b4-3aed-9edd-28707756b03b | -3.09141 | -53.26244 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac2f5a15-13bf-37d0-bb62-6d1a771b357c | -1.47454 | -52.26207 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d636d6ba-599d-3a2e-a34d-07d4944049c0 | -3.06109 | -50.33927 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| da95aa66-1e77-3758-8342-5b47db256b88 | -2.9759 | -45.16526 | 2024-11-13 04:57:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 16.1 |
| e9bf22f2-a9ca-340f-b1e5-16ce91b215b6 | -2.94618 | -54.23625 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0230549d-130d-3f48-b4a4-05ab7ca0076c | -3.06585 | -50.32806 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb3c9a89-fb47-33e0-b524-3c89d619c457 | -4.4745 | -49.63257 | 2024-11-13 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README33.md)
