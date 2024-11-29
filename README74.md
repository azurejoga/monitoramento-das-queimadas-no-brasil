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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b15946b7-9c92-36ea-aee2-1175e71a4eca | -1.58251 | -52.1777 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8de93b24-3602-3ba2-8cff-c8ccc1b3a1ab | -3.21586 | -53.83237 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 609da251-a7fa-3fc3-b797-3fc902b137d3 | -3.28702 | -48.76435 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8a05217a-82ce-3b19-9219-a84af7eb1854 | -1.15977 | -53.40781 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9a5a8e0e-1d5d-3965-a4e7-2ecdb74a613c | -0.29463 | -55.87068 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 684fd774-4de4-3c21-baf3-f44f39df95eb | -1.69626 | -52.45367 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| fa9899d7-bb4b-3122-9be9-c7be3efbcdfa | -4.20292 | -50.68651 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72384a0a-d12c-3769-a858-c1860d201ca4 | -1.29137 | -51.72798 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ad18b33-e62a-3ebe-a4e7-e0255524a70b | -2.46105 | -53.69961 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44e2c579-9f3b-32a5-b9a4-b004d8e890ba | -4.48184 | -48.11729 | 2024-11-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a6cb0a81-3fee-30f1-acd0-242f1638927a | -2.72686 | -48.66882 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 272a8b00-504c-3680-a4bd-7bf51cef0345 | -2.90406 | -54.17461 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 796b9389-2fe4-3d91-aaae-b93d68b25eb0 | -0.26385 | -51.49404 | 2024-11-29 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a47d30c2-61bd-3cf6-9955-2c56e2e6b3b8 | -2.8306 | -54.09963 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4a06f1dd-a4e1-3135-8aa6-78590dd297f2 | -1.13991 | -53.79514 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15bd7d98-f050-38db-abad-12c638bc399e | -1.7149 | -52.77002 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| c6b2e327-1ddb-35ff-b5d0-93296735d7cc | 1.23102 | -55.93313 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e3d1c69a-dabd-35b0-a57b-1e122c9b26ec | -1.72204 | -52.48322 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 75a6154d-6ba9-3d69-8350-55a9db288720 | -2.72906 | -48.89953 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bb30a7fc-9459-358e-a702-36b6224372ea | -1.09479 | -53.38716 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 2d03d628-413f-3c1d-ace3-9f1e9b41dc4b | -3.04775 | -54.03809 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9d227a9-36af-3fe1-9913-4b605ea52607 | -2.3397 | -46.87675 | 2024-11-29 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0c75644-8dcd-396f-8178-6204af9643ed | -1.75606 | -52.70198 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7ea7e36-3a7c-32b0-a662-3ce7fd0021b5 | -3.09881 | -53.73285 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5aa180b6-ef00-365f-9579-ec3d3799a812 | -2.13067 | -54.89712 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3799438e-060c-3362-a51d-f9ecc7a9e072 | -1.69789 | -52.44319 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| a4b0b87e-6783-31fc-a467-3e1f48416ed0 | -3.79754 | -51.25823 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 02f50feb-4596-3ce4-a762-33ffb38c544f | -1.07277 | -53.63676 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ad322e3c-9e25-3085-97cb-d65ee8912500 | -3.53025 | -50.75351 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2de11980-c3f6-3bc6-bfaa-bdb3fed07cb0 | -3.05383 | -54.04255 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| df482d65-af24-359b-8110-ad315055297e | -4.04613 | -48.08081 | 2024-11-29 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a498fed-bee0-3450-a81d-24fb39fe5bec | -3.07085 | -50.9886 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 980e41a3-d69e-39a9-ab90-7f7e7eca316f | -0.23927 | -51.60785 | 2024-11-29 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60e16e0d-e898-359e-a684-f2e5ba457558 | -3.26404 | -49.89529 | 2024-11-29 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a9e63f51-f763-35e0-8cef-b2d0b1855ac9 | -3.41666 | -50.16868 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4cbafb54-b39e-375e-97e3-e7280d1c18ff | -2.72388 | -48.66122 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 371ab606-e5a3-3e80-ad48-5878c743f8f8 | -1.47368 | -51.54377 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f15950a-4820-357e-bb6e-936c315a16c6 | -1.29007 | -51.64638 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ab314788-678c-3f1b-b255-f5d71a1b8e68 | -1.45518 | -54.36788 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6774139a-dfb5-303c-bc64-2c5e75532e87 | -1.44803 | -55.19614 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c2afe81-089d-3a31-a884-28c9454e5a02 | -1.6177 | -53.87396 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 236a9b14-5d41-3eb3-a4f9-8e6739e3d29b | -1.13793 | -48.33418 | 2024-11-29 04:57:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 53724ca2-c2dd-3c6d-8fbc-077b69de195b | -3.07123 | -54.41022 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ca71430d-5f80-328f-bd75-7a5b60cdcb6d | -2.99064 | -51.32656 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7859cdce-d9df-36b1-89e1-a45821b5ec0d | -1.15379 | -53.68443 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79aa5e29-e3c1-3320-b99a-5fe938938501 | -2.88643 | -54.00603 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9d128118-0406-3519-9963-6fdec8e5fd57 | -1.28578 | -51.74187 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26eb9f35-57ac-35a3-a242-3eb794005b53 | -2.64804 | -51.77747 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| af8eaa54-63bc-33d3-96b3-1d40d7466eed | -3.08869 | -54.12612 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aff4d36a-1b50-3918-bcb3-176f88d0dc05 | -2.83645 | -54.04057 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aaf5b064-d178-3e00-bde0-8781300d0295 | -1.06103 | -53.21352 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 06e515b3-8da9-31ab-940c-7f13425fd9ff | -3.49056 | -50.4465 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d957009-b121-391d-b7c2-a1f60d6102c0 | -2.6775 | -46.14805 | 2024-11-29 04:57:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 40890a57-ff0c-34fb-af00-317a187cfc76 | -3.98073 | -46.72858 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7f3d71d-c4ee-3bcb-9010-0770a5c5b903 | -3.96715 | -47.94205 | 2024-11-29 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8b52be9a-75af-33cf-9f3e-6b88885ca170 | -2.68145 | -54.2492 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 556faa07-000a-3be1-91f3-3e827a81086b | -2.59892 | -54.25414 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 28708d69-9211-3245-a806-45aff2caecca | -2.53646 | -53.97926 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c5e46c4-106f-331a-9148-5ff7dbf0f54b | -3.25408 | -53.63079 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 27dfd5cc-3db2-3977-9977-b43a212724be | -2.97117 | -53.8537 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e5a4085-a12b-3121-9b63-046032f56d6b | -3.58206 | -50.3364 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d77675bf-82d1-3716-80bf-3db8251e595f | -3.17541 | -46.30049 | 2024-11-29 04:57:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ef514b01-582b-3f9b-969a-00ce64329495 | -1.61882 | -52.64475 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c195369-ae5c-3bf5-a5b7-bdc5d073bdf5 | -1.61698 | -52.45935 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d27bdd3-2310-3117-b447-0137f139d167 | -1.57379 | -51.17168 | 2024-11-29 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6aa8fa79-8d2a-3049-9286-0d5a943171c5 | -1.59616 | -52.2879 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 148eb711-ccb6-3cc3-b60b-4c24b99b5021 | -1.50752 | -52.63832 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ed73a2f-e322-3f71-9cd0-ec82dcd59300 | -1.07445 | -53.38754 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b02ffeb-16de-3504-a404-e25855ff31c0 | -1.25704 | -51.78202 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0d7c119c-7cd9-32cb-948e-2a75a9547595 | -2.98468 | -53.28594 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 658c995d-daa0-3f00-9559-3b61710fe830 | 1.22445 | -55.93842 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 660aa49b-32bd-34dc-9d57-dd14ad77b9b4 | -0.95455 | -51.65115 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c07ae419-635a-3221-a9e8-10b046cb3494 | -2.78501 | -52.86534 | 2024-11-29 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7d0ddcdd-1fe7-39dc-a58d-0d3699596e1b | -1.14793 | -51.92977 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31642609-ab3f-373b-8e7c-74f6f10eed98 | -1.78354 | -52.74511 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 05c830d0-a5e7-3774-8d17-67c241f4b8f4 | -2.5986 | -53.99601 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7dcbe28e-68a0-33b2-93cf-4ac02a57782d | -2.06353 | -46.3804 | 2024-11-29 04:57:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d9776214-3326-3c09-aaac-93dbaf527afb | -1.27718 | -52.69807 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6df8e777-7965-3a99-9db7-e3cc000e2a6a | -1.65176 | -52.73843 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 51326c2c-2daa-37b3-9dae-fb19c3b6b4be | -3.07423 | -53.91195 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6e9eb689-1175-3903-9afd-9e60dcf8723c | -1.67586 | -52.49696 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c54dd73d-c2c7-3071-90a5-8701647ba8ad | -2.55964 | -56.68515 | 2024-11-29 04:57:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d78c774-a511-315e-9c10-e976fd95e233 | -2.61751 | -54.20037 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4c616eb-d3f8-320f-bc92-1637f03e931c | -3.08433 | -53.28015 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c78ba703-3a23-3926-962e-3bf19dbee748 | -2.58679 | -54.09308 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a6a8ba33-5e4e-3aa9-9967-407faf97b3c9 | -1.44359 | -55.15766 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 10a8186d-b9f5-340d-a4ac-2dcf0e57909e | -1.28156 | -52.69167 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9bebf5d2-2637-31fc-a87e-6c7d064375b8 | -1.37763 | -55.03941 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2299d7a-9fcc-30e6-ade6-5bb5b1b1cac1 | -3.26474 | -54.10762 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d164ce40-6f8e-35ad-a624-3f62e21c0c7b | -3.10973 | -53.9919 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e122aff2-9423-37ba-88a9-a788f2fc4d04 | -3.51699 | -51.32096 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5cb45790-748f-330a-9ab1-2eb10c6f36f5 | -2.71154 | -54.16537 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57332afe-e972-3f5e-8f6f-7a61ffd8f053 | -2.53879 | -54.29104 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f11df8ad-e880-34bc-bd5b-e944e6c42a89 | -1.58845 | -53.84124 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b4a4f368-fff6-3064-b27a-98e344768179 | -4.09403 | -48.48827 | 2024-11-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3d55dbfb-6c27-30c6-bded-feacaba797b4 | -2.83406 | -49.84277 | 2024-11-29 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 713ab801-0b2f-375e-9f35-9ca6c9a97ed9 | -3.37052 | -50.82626 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 596ed27e-d01e-3170-a1a1-d7d015522a60 | -1.24443 | -53.38991 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 74e8750e-a6fd-37e3-b956-d7d7cd810687 | -3.35243 | -53.74108 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73df8dbd-2392-39ee-bac5-8efab7e5a827 | -3.0312 | -54.18726 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README75.md)
