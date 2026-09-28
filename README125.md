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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e4c0104-4ce6-3d06-bb48-c052a667b737 | -3.72956 | -50.63987 | 2026-09-28 16:28:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 36af7cf5-b7fd-3918-b7bc-e80543164fd8 | 1.86822 | -55.58804 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 848af161-5397-389c-9f38-056efdd061bb | 1.86368 | -55.57822 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e6b90911-e475-3b35-b027-3c201d21e568 | -1.21607 | -46.49067 | 2026-09-28 16:28:00 | NOAA-20 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 18f35256-29d9-3bdb-af73-2191ec2c3acc | 1.87498 | -55.58435 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 09fa0ecd-a790-350f-9fc3-c80d65a2db05 | -1.36813 | -47.57181 | 2026-09-28 16:28:00 | NOAA-20 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| e2a4e2cf-0b92-3245-8ece-8510dea7f3dd | -1.97451 | -54.25785 | 2026-09-28 16:28:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 47321b90-3da7-3b54-9d1e-d07e9dbd4334 | -1.03095 | -49.23265 | 2026-09-28 16:28:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 61f39950-c73e-3e07-896f-5307984b945b | -1.21088 | -49.21302 | 2026-09-28 16:28:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9ca154fe-a8cb-3d59-83bc-c910b10b1395 | -1.97331 | -54.24981 | 2026-09-28 16:28:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 07dfb895-0d4d-3579-a4cd-6b730c8edc70 | 2.35682 | -50.76577 | 2026-09-28 16:28:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 048c74f6-70b0-3762-bd34-5719263d8d3f | 1.71774 | -50.96268 | 2026-09-28 16:28:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 3ce64942-526c-340f-b117-390100efb2fa | 2.39957 | -50.76302 | 2026-09-28 16:28:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6c06a07c-ef1c-33ff-8d7f-ce8d6800ac15 | 1.72473 | -50.9752 | 2026-09-28 16:28:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 12.2 |
| afab42a7-e7ad-34b9-bbd6-364d04677837 | 0.87721 | -50.77837 | 2026-09-28 16:28:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 691ca78e-2d69-33d8-b6e8-a806d567baf0 | -0.86649 | -48.09372 | 2026-09-28 16:28:00 | NOAA-20 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1604cd28-036a-362f-b63e-064042d9e993 | -1.43515 | -48.90437 | 2026-09-28 16:28:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 6778901c-5add-334c-b92c-57952940ecbe | -1.42854 | -48.88743 | 2026-09-28 16:28:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 36176c45-dcf0-3c54-bb14-2ce6d595655c | -1.89438 | -50.21712 | 2026-09-28 16:28:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 83acf47f-0d36-330b-a5f9-95efac0fcf85 | -2.08855 | -49.55561 | 2026-09-28 16:28:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1fe241b7-5d78-323d-ab69-2b86403203dd | -2.01924 | -49.88752 | 2026-09-28 16:28:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d7097ab5-f49a-3a39-a578-958ab721ee6d | -1.54874 | -50.42423 | 2026-09-28 16:28:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 1b6b50ab-070b-3fa8-8140-e90aaebebcab | -0.52747 | -51.86836 | 2026-09-28 16:28:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 1551908f-f25e-3f67-9d90-92261649b3e4 | -1.4371 | -48.88971 | 2026-09-28 16:28:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| ea02b58a-0d91-3a6e-bf7e-692e8daa69b9 | -2.82071 | -51.33933 | 2026-09-28 16:28:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 0eff67c7-c3eb-300f-a8fc-ee2a5ba74ff5 | 1.89048 | -55.56479 | 2026-09-28 16:28:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a3df7e34-0469-3816-b231-3856a41a8bb7 | -2.06735 | -49.47053 | 2026-09-28 16:28:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 2028fa67-c627-3b53-94ea-3095b7b1eed1 | 2.04179 | -50.9058 | 2026-09-28 16:28:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 234806c7-2e4f-3caf-9df6-1663022871fb | -1.43294 | -48.89845 | 2026-09-28 16:28:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e491ab9e-977a-356e-8f5a-243f150f5577 | 2.04198 | -50.90925 | 2026-09-28 16:28:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a739a106-bdd2-30a5-9639-aa8ba5f4d7db | 1.65803 | -55.91078 | 2026-09-28 16:28:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 73e58f37-057a-3c2a-8564-08d5569286f3 | -2.05529 | -49.53305 | 2026-09-28 16:28:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9de60d7c-a7ad-3514-a39b-d0318d306988 | 1.95772 | -55.6936 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 84eeee2d-0af6-33a2-bf94-de7d693b6321 | -1.97513 | -54.26197 | 2026-09-28 16:28:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| db453576-18d5-3b4d-ae7c-278360597e58 | -2.91599 | -54.12397 | 2026-09-28 16:28:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1a0cef8d-8902-37a8-8af1-d5433de1f526 | 1.72844 | -50.98019 | 2026-09-28 16:28:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 10.8 |
| c541b08f-5a4a-3ed3-a5fc-ae1433970764 | 1.89433 | -55.57893 | 2026-09-28 16:28:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 68a6f83d-bbf0-32ff-a253-8134f1e0918c | -3.07973 | -44.34849 | 2026-09-28 16:28:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 527acf88-accc-3da6-8271-bb8202b7fa8b | 1.648 | -55.89475 | 2026-09-28 16:28:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c9fb9c5d-6b9d-3dc0-8224-72eafa69a2c6 | -2.24704 | -48.74805 | 2026-09-28 16:28:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3825c370-e674-38f9-8668-e518e4c55ae3 | 3.34489 | -51.30112 | 2026-09-28 16:28:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 104156f4-57e5-315b-8a0e-5c340a3d4512 | -2.44953 | -49.21894 | 2026-09-28 16:28:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 0d360992-ccdc-3168-a6f2-ef421cfce174 | -1.20679 | -49.21363 | 2026-09-28 16:28:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e7b49591-e475-30a7-8bb3-eeae5da99128 | 1.95168 | -55.69267 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 7a4ad151-0983-31c8-9883-f7ce9b6ee44f | -1.42201 | -51.40804 | 2026-09-28 16:28:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 10b67021-fa06-3fe7-9f46-8bdfdb855593 | 1.73052 | -50.96727 | 2026-09-28 16:28:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f3632adf-8f67-3f15-9f7b-f886f2619cf6 | -0.50265 | -49.12387 | 2026-09-28 16:28:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| a0d1d7b6-f476-345b-938c-84ae3c844900 | -1.11182 | -48.10565 | 2026-09-28 16:28:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0efef599-78a7-3b03-8515-b825813dfc92 | -3.31364 | -44.70751 | 2026-09-28 16:28:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 69c1ae7f-ba04-3955-a8e4-a9f4efb9587f | 1.8487 | -55.59435 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| ca7ee662-9f5d-387e-afd7-20b68bb0a411 | 1.72983 | -50.97155 | 2026-09-28 16:28:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| adfc9e3e-26d9-3ebf-a665-db16469a7851 | -2.71898 | -43.6277 | 2026-09-28 16:28:00 | NOAA-20 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 478a9271-6165-3afe-ac33-5106bbc0f2d5 | -1.2092 | -51.62144 | 2026-09-28 16:28:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 34ba9b0e-c32b-356a-bae4-a1f9e788cf9f | -3.3865 | -46.45189 | 2026-09-28 16:28:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 5f39e40b-85ab-3607-985e-9998abd1b8e4 | -1.43308 | -48.89033 | 2026-09-28 16:28:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 9d64f7ec-efa1-3524-9594-ba0a0f49f7b3 | -2.06317 | -49.47192 | 2026-09-28 16:28:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 24132496-20d4-3503-a02b-0085e5b233b3 | -1.4397 | -48.90725 | 2026-09-28 16:28:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a365f0c5-2221-351e-bed2-089b1653dd96 | -1.52705 | -50.22828 | 2026-09-28 16:28:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4538da2b-801b-3010-a627-96ef4813586d | -2.49575 | -49.41747 | 2026-09-28 16:28:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 721b21f7-a19d-3902-a8fd-b46c0b4fa215 | 1.88976 | -55.56923 | 2026-09-28 16:28:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| bec766ac-5dc1-36bc-b15a-eca0f8a7c19c | -2.44885 | -49.22283 | 2026-09-28 16:28:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| de7ca6ee-a583-3611-ac57-0e384745bb9d | 1.86218 | -55.5873 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 4357de78-7117-3ab1-a38f-34f9ced66abe | -2.06313 | -49.47115 | 2026-09-28 16:28:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 742448ee-59d2-37ed-b94e-653042086e5a | -3.75852 | -51.34061 | 2026-09-28 16:28:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 90f62fe9-c3b8-300a-84a9-7dc53bde2f4b | -3.73186 | -50.64206 | 2026-09-28 16:28:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| cdc8c06a-30fd-3192-bf73-775bfb96c18e | -2.14763 | -50.25393 | 2026-09-28 16:28:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 4089b917-9a61-3cd3-a810-7a107a27081b | -1.86221 | -47.97743 | 2026-09-28 16:28:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| aa4757c1-3d41-3819-aab8-6c51a1881762 | 2.08413 | -55.88031 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1cec93b3-3bbe-3de4-9e97-64a5b17f3437 | -11.978 | -50.7157 | 2026-09-28 16:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 0e90c030-8feb-37cc-8d27-cdff5548f07d | -11.9399 | -50.7201 | 2026-09-28 16:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 103.5 |
| c7b66049-0a04-3d6f-a90f-01e72a458e85 | -12.1734 | -50.3927 | 2026-09-28 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.8 |
| c8892e2a-536b-352f-bfd9-9d4024268883 | -12.0612 | -50.2558 | 2026-09-28 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| ff270d9a-803a-3e23-aaf8-8caca08a6860 | -11.9968 | -50.7349 | 2026-09-28 16:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| fb7fdb07-3ee6-31d8-ad29-4d9737a8cc67 | -1.2818 | -49.3803 | 2026-09-28 16:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| d0baac0e-ae37-316c-a891-6b2d1390cd1c | -11.8472 | -50.5598 | 2026-09-28 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 2b23be03-132e-355e-b42a-8badef1d7735 | -10.2565 | -50.5185 | 2026-09-28 16:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 73412ad6-ab5d-3ac9-8192-7aa39f6ef7c7 | -11.9586 | -50.7393 | 2026-09-28 16:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 56cc3d46-8ed1-381b-907f-7df5316cf499 | -11.809 | -50.5642 | 2026-09-28 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 9d2b7829-95cd-395e-9b9d-bf8f4eb408a3 | -12.1557 | -50.3089 | 2026-09-28 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 752a155f-4c74-3349-8746-8572f90e08e9 | -10.7624 | -50.8282 | 2026-09-28 16:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 96.6 |
| ce126017-6a2d-3186-82e0-542b6a7008ac | -11.6951 | -50.556 | 2026-09-28 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 65467459-9ddf-33a1-aca9-04e13ef67365 | -10.6928 | -60.7322 | 2026-09-28 16:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| bcd19df7-e2bc-3603-8d8e-cd63ecaefe11 | -12.2254 | -50.7294 | 2026-09-28 16:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 90.8 |
| d50dde1d-c3a9-3c0e-b77f-1bcfc7c716a5 | -12.3088 | -50.2688 | 2026-09-28 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 46cb4bb3-e3ce-3ae1-ad0e-04c760dae364 | -1.3003 | -49.3801 | 2026-09-28 16:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 230b691e-7d8e-387c-bcb3-5c85a4064347 | -11.77 | -50.6329 | 2026-09-28 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 5c479080-f3d0-3b48-b5aa-b608c06ff997 | -12.0609 | -50.2773 | 2026-09-28 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 5b4c5980-5565-3acf-8c76-577606b981c9 | 2.1266 | -50.8788 | 2026-09-28 16:30:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 83.5 |
| f5323f81-8d41-3845-ba85-3afda663e136 | -11.9402 | -50.6987 | 2026-09-28 16:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 96030b59-e37f-3b5c-b1ac-46c4fa8036a4 | -11.8094 | -50.5428 | 2026-09-28 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 6094aec7-486a-3386-bb47-ef5301570a7b | -12.2639 | -50.7034 | 2026-09-28 16:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 89.9 |
| e993bd70-f92c-3e19-9a54-07c35689350c | -11.7329 | -50.573 | 2026-09-28 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 6db81d15-ecab-3bb5-b561-c58d9dfb3931 | -12.1553 | -50.3305 | 2026-09-28 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| ca2cce7c-4ff4-381e-b8b5-59484b9b5c2f | -11.9612 | -50.568 | 2026-09-28 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 0a29196b-0c0c-37aa-ba61-183b04c1947a | -11.7141 | -50.5538 | 2026-09-28 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.4 |
| bcc79579-e73b-3ece-92c5-4024097fc15a | -12.2445 | -50.7271 | 2026-09-28 16:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 92.3 |
| adfd42fc-24f3-3048-998c-24450782f518 | -12.2897 | -50.2712 | 2026-09-28 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 185483f6-9cdc-30ac-9fc0-222ccb5e1eff | -11.9615 | -50.5465 | 2026-09-28 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 581e7af2-5654-3d77-92ec-889f6bb0ab42 | -12.1935 | -50.3259 | 2026-09-28 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| f3a12636-03ae-360e-afce-521df7436fd7 | 3.41677 | -51.52832 | 2026-09-28 16:30:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |


[Clique aqui para ver as próximas entradas](README126.md)
