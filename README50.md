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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47c731f0-437f-3585-b337-34a74b7c30d9 | -4.65937 | -46.66116 | 2024-10-28 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a0020470-53bb-3147-b699-387a6f2f3dec | -4.61593 | -46.69904 | 2024-10-28 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 48c40c32-0b6c-3eef-8927-fe645e2842bc | -4.54494 | -46.60864 | 2024-10-28 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| cb709c2e-32b5-38fb-9d60-31473c0119f6 | -4.54032 | -46.60775 | 2024-10-28 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cdb1d0c7-9d46-395f-b84f-451b7fa2d9a2 | -4.53798 | -46.39505 | 2024-10-28 04:57:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6084e5c4-3398-34ad-91cc-44ffa080c15c | -4.53726 | -46.39997 | 2024-10-28 04:57:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53e8d52d-456d-36e5-91f8-3c671357d926 | -4.51846 | -46.46347 | 2024-10-28 04:57:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 96a06025-cadd-3a5d-ad26-da0e59252686 | -4.23888 | -46.87181 | 2024-10-28 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70654d78-4f1d-3470-b855-340530242316 | -4.23824 | -46.87621 | 2024-10-28 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 412fc52c-fb46-3f7c-aa45-41c1a2fe45ef | -4.23759 | -46.88065 | 2024-10-28 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d2211e2e-f8b5-3a44-b0a7-1b1cdaca3699 | -4.23435 | -46.87105 | 2024-10-28 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5aef2b67-f502-301a-be8f-3d2bcbb39cf4 | -4.18592 | -46.81491 | 2024-10-28 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11dae82c-dddd-3fae-9d90-6bb3d7bb4da1 | -4.18493 | -46.38513 | 2024-10-28 04:57:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 60faee26-ddc0-37e3-83a5-da8732b67a78 | -4.18303 | -46.38204 | 2024-10-28 04:57:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e8a1cccd-5405-3d6f-b351-7f1f43e5eaf6 | -4.18232 | -46.38694 | 2024-10-28 04:57:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b8c5bbd7-95ab-342d-9d38-f310d03ea194 | -4.18142 | -46.81384 | 2024-10-28 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e8c04332-5e27-3cd5-ba7a-bc478c21daf7 | -4.18022 | -46.38459 | 2024-10-28 04:57:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c4481291-6607-3b55-9e37-0aa4d1af4de2 | -4.12796 | -47.32367 | 2024-10-28 04:57:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ff91e281-8ea0-348a-ab16-536346ecc50a | -4.12769 | -46.89525 | 2024-10-28 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0267cfbb-e60d-3076-9f4d-04911a700fa9 | -4.12732 | -47.32789 | 2024-10-28 04:57:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ea1ee09d-2573-3584-92e7-0b9db0569f38 | -4.12356 | -47.32304 | 2024-10-28 04:57:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 492cbcf7-d46f-3c4b-b514-e9ade9286ca2 | -4.12318 | -46.89448 | 2024-10-28 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fafbf7c5-4b52-3bc4-b359-83dc1ccc1735 | -3.99531 | -46.48503 | 2024-10-28 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf6c42b9-3b30-301b-aa31-5516e1ee34b7 | -3.99141 | -46.47929 | 2024-10-28 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 7a3e761d-3567-3e75-81a1-3949a24afedf | -3.99069 | -46.48417 | 2024-10-28 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 80585463-fe80-31c8-90ab-86bafcf56e41 | -3.98998 | -46.48903 | 2024-10-28 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 2f0f6e7c-8a58-3918-a719-a0b234420c2a | -3.61859 | -47.26368 | 2024-10-28 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eec8c4e5-f6e1-35b5-adfc-744083855c38 | -3.61593 | -47.25675 | 2024-10-28 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8639a784-fb29-3745-b106-02e2e677f84b | -3.61531 | -47.26102 | 2024-10-28 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 851b319b-96b9-3bb0-864e-937769fbf83f | -3.61484 | -47.25888 | 2024-10-28 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8ccca91e-e99e-376b-b4ee-7950684ef002 | -3.6147 | -47.26524 | 2024-10-28 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c0b1f259-2ecb-3c52-81ac-bb78ef184a06 | -3.61419 | -47.26313 | 2024-10-28 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 65f35d8f-dc4a-3850-b114-cc5b04479247 | -3.61332 | -47.29798 | 2024-10-28 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab55ff24-6367-3d26-a004-46ab5e925a30 | -3.61224 | -47.2821 | 2024-10-28 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 34736e0d-f298-3951-979c-334d2f72f901 | -3.61154 | -47.25616 | 2024-10-28 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc21c7d5-8a52-398b-9235-121044999d4d | -3.61097 | -47.28416 | 2024-10-28 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ffa4afc3-7136-3481-9b16-aedf5dd23539 | -3.61045 | -47.25832 | 2024-10-28 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2fc0ee1f-30a6-3495-b5ad-020b490406de | -3.61033 | -47.29531 | 2024-10-28 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 90602919-92a1-3b77-a207-79df5439a140 | -3.60972 | -47.29949 | 2024-10-28 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73aab79c-371f-3960-b2ba-7b6d9be93dc0 | -3.60909 | -47.27304 | 2024-10-28 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0e340b12-f763-31c9-b242-5f3b133e972e | -3.60896 | -47.29729 | 2024-10-28 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 57b427df-61b0-37fb-b269-ea5f56f2c325 | -3.60852 | -47.27093 | 2024-10-28 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 49de9703-9dc0-32d3-b078-a814e21359ba | -3.6066 | -47.28351 | 2024-10-28 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9554d8b9-be39-37dd-a2a0-e3c5a409598a | -3.60597 | -47.29456 | 2024-10-28 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b39ae8be-b5cd-3816-8903-fe0729381f76 | -3.60413 | -47.27041 | 2024-10-28 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fba8e58a-33bd-339c-9436-a275d4fcdde1 | -3.60301 | -47.24837 | 2024-10-28 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c9abcd51-c8a2-36c8-9363-cb162412d184 | -3.59409 | -47.27761 | 2024-10-28 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8984c0fb-b342-3ff3-bfbe-342f76cf36dc | -3.59345 | -47.28181 | 2024-10-28 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a193f3b-ac73-3a1b-a3cf-bd1568cd912d | -3.5897 | -47.27712 | 2024-10-28 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30975bc9-eb24-3522-b15c-addbd293300f | -3.58905 | -47.28134 | 2024-10-28 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3fdf41b9-c128-37c8-a387-302649932e2a | -3.58468 | -47.28069 | 2024-10-28 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c07a2ea-2a4c-3e6e-92e3-6d08e17e6921 | -3.91186 | -46.44773 | 2024-10-28 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ae5c006e-c351-3f91-ad4b-633f511954de | -3.90723 | -46.4469 | 2024-10-28 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a855ab58-84fb-3a7d-92f1-1875f9df9f60 | -3.81576 | -46.93826 | 2024-10-28 04:57:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4666f2a8-9e17-37a9-ab04-8bc20f1ff708 | -3.81513 | -46.94252 | 2024-10-28 04:57:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d8dfc47b-ace3-3d1f-bcc0-b1c2d45740d6 | -3.8119 | -46.93332 | 2024-10-28 04:57:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38adf134-fb96-33d5-91e6-40c6e6856af9 | -6.42094 | -47.28709 | 2024-10-28 04:57:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27e0b701-ecdc-31c8-8649-d75fb27ac86a | -6.41988 | -47.28906 | 2024-10-28 04:57:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3d0819b-2839-3ae7-b4ed-8f5cb30fc938 | -6.36818 | -47.91961 | 2024-10-28 04:57:00 | NOAA-21 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8d575a9c-604b-365a-9b30-0ed25b3fdb42 | -5.78768 | -47.08967 | 2024-10-28 04:57:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ebd40081-58ee-3639-9efd-2024f265e88a | -5.7189 | -47.11308 | 2024-10-28 04:57:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84376492-a227-3c86-8b43-85d16198f123 | -5.71434 | -47.1123 | 2024-10-28 04:57:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05eb6e6e-b036-37b3-8dbf-627c8850d5e6 | -5.24258 | -46.67485 | 2024-10-28 04:57:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f45c4b6-af6c-37e1-bf50-48b8ee9ddf8e | -5.24188 | -46.67978 | 2024-10-28 04:57:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8c74861-cee7-3b2b-8ffe-188b2bd52a91 | -5.15179 | -47.70646 | 2024-10-28 04:57:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2549782-010f-31f0-b77a-037eaf87b70d | -7.63426 | -47.07319 | 2024-10-28 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ef1c9c2-d2a7-3d93-9a7f-551069576cef | -7.63358 | -47.07822 | 2024-10-28 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81855fe1-d5d6-39be-90d7-b0c03e229529 | -7.632 | -47.07693 | 2024-10-28 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d3598b0d-1151-3194-ac93-bc27600e2309 | -7.4762 | -46.90298 | 2024-10-28 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa2621c6-1cfe-325c-a3e7-97f403d2cda9 | -6.69488 | -47.64189 | 2024-10-28 04:57:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cacdb19d-68e2-32e5-a6e4-c22c3bacedf7 | -2.06706 | -48.22038 | 2024-10-28 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df2692f7-b7ce-3182-99d1-f1b22d05cb54 | -2.06533 | -48.22041 | 2024-10-28 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0661b761-1822-3c3d-bc25-2d440c222618 | -2.04548 | -48.02935 | 2024-10-28 04:57:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 13e1cba2-e4fa-3797-9e55-a8e6cf28f6d4 | -1.97499 | -48.43509 | 2024-10-28 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 06ff94f6-10ae-3616-9203-26581a05c620 | -1.97104 | -48.43451 | 2024-10-28 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6b1ba1b4-ec0d-350e-ae23-7b230bc572ad | -1.96523 | -47.95424 | 2024-10-28 04:57:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fb790db8-b07a-3c1a-9067-c7e599c5419d | -1.95099 | -47.91126 | 2024-10-28 04:57:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5513b4df-758a-37f8-966b-11aa8c433eba | -1.93209 | -48.66256 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 359c3e8d-7c87-3f2e-9196-fa3845611223 | -1.78304 | -47.83858 | 2024-10-28 04:57:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17072b7b-16b0-311a-89aa-bbc4a3187eed | -1.78247 | -47.84224 | 2024-10-28 04:57:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7c30b6bd-e7ba-3702-9502-ba5bc6697d1b | -1.77895 | -47.83795 | 2024-10-28 04:57:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3cb7771e-a741-3187-a403-47ed944118bd | -1.57411 | -48.64088 | 2024-10-28 04:57:00 | NOAA-21 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95d6e51f-938d-3dd9-94d9-67a48401ed76 | -1.52716 | -47.20129 | 2024-10-28 04:57:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b869a6cd-0787-379c-8d6f-eb43a6a948a1 | -1.52655 | -47.20524 | 2024-10-28 04:57:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2ea57991-f63f-32ba-b83d-68e4dcaffd80 | -1.52593 | -47.20924 | 2024-10-28 04:57:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 63d022cb-1086-393b-8412-4e2791aa462f | -1.39577 | -47.83506 | 2024-10-28 04:57:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a680570-4710-399d-ab94-91717bc5419a | -2.64317 | -48.55947 | 2024-10-28 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b953385d-6ac6-311e-910c-2fbd3bf38236 | -2.63921 | -48.55887 | 2024-10-28 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed7467f1-3b4a-3ef9-8ebd-dc5b1c648819 | -2.62329 | -48.31609 | 2024-10-28 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d70d692-9f44-31f7-9f00-e65fd5b9cff8 | -2.61928 | -48.31547 | 2024-10-28 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd916cfe-09f0-38dd-bde9-8e977ef3eb32 | -2.61088 | -48.37122 | 2024-10-28 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 925d3448-2e5b-3a28-adf7-5c527da36cad | -2.60091 | -48.2115 | 2024-10-28 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3793846-df99-3af9-a678-68a05f02378b | -2.58543 | -48.15085 | 2024-10-28 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c61b9391-b3bc-3674-942f-c49f66a2ff83 | -2.58137 | -48.15024 | 2024-10-28 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ce69114-06dd-3f93-8325-d4cd7c8d554d | -2.53122 | -47.37258 | 2024-10-28 04:57:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4546a532-0ac0-33c8-9993-2f87ece79056 | -2.52538 | -47.44105 | 2024-10-28 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6e5e8de8-4d73-302f-b11e-3c87ce7f1cee | -2.52479 | -47.445 | 2024-10-28 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ee6b1b7a-8dc0-3142-b363-eb3266c02187 | -2.5242 | -47.44896 | 2024-10-28 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 82e203ad-1051-32d1-9f9e-80430aa766b6 | -2.52112 | -47.44043 | 2024-10-28 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 35a98f2b-5a3a-32d5-88b8-fba88a524d44 | -2.52053 | -47.4444 | 2024-10-28 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README51.md)
