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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dcb211f2-0353-337d-b8c7-7acc34965a45 | -3.60461 | -51.53857 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ccb4965d-9ecb-33f2-8048-96fd1760ab6c | -3.97258 | -50.92862 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a51ab63-be18-3935-80a3-7ba1f921fc86 | -0.5773 | -51.69519 | 2024-11-30 04:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 14.1 |
| d6f24edd-63de-32af-8f4a-19bf56d1ebd3 | -1.45574 | -51.50157 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c4cc3be-ac9a-300b-ac2e-d34d0193f6b4 | -2.87931 | -54.1153 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d2cf03ea-620d-35bc-aa1e-31359c011f85 | -3.21999 | -54.17722 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6140c94b-fdcf-3d50-8aff-e159314e2a14 | -6.79534 | -39.45416 | 2024-11-30 04:40:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 71f7de87-af79-31f3-bdad-1b67f176bc42 | -1.28028 | -51.73533 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 388b6432-3880-393f-bd8e-d154cf7a6d29 | -2.84103 | -46.86303 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49d429cf-9581-3642-9370-e6b1a7881814 | -1.20759 | -53.86981 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 46616c5e-563a-3ae8-8c30-6c173a84b8e7 | -2.54845 | -55.22664 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7f052499-b024-347d-9373-2d7248e4d767 | -1.06583 | -53.63206 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f8d5fdb-5f30-3bed-bdbf-80be97752bf0 | -3.03109 | -51.53603 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b73b4372-cec4-36de-aae4-9f4c3964e19e | -4.15351 | -44.26744 | 2024-11-30 04:40:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c42f04a-dc29-387a-8578-dc547da6e1df | -3.28187 | -50.19411 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae2b98a6-9b2a-3044-bbfe-0d90cf376f84 | -2.67238 | -46.14124 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 135932bf-a1ef-32a6-80fb-a959d41e0d32 | -6.41275 | -52.43832 | 2024-11-30 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f43b011-4149-366a-8ab5-6083426a309e | -3.00512 | -49.51015 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 906d877a-80dd-37c4-be57-b2db3ea32096 | -2.61333 | -46.56802 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00f7d222-0728-3519-b3c2-64025ed6939a | -3.99835 | -47.91356 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b3b314f-8d19-3d67-bd72-f4486c2f2ee5 | -3.04766 | -49.36822 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2a3a583e-e39b-38de-8e5e-5be395e05de0 | -2.73608 | -47.98562 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14a2b471-7fba-3f99-bfcd-edaaf9153c7b | -2.91623 | -48.33704 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 854720e6-7e53-3b7e-ab5b-31d08a5d05ff | -4.4738 | -50.42457 | 2024-11-30 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be34ad98-a976-3fa1-afa6-9cd92a183651 | -3.17852 | -54.32875 | 2024-11-30 04:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb0622a2-f740-3dd9-ab9e-23e888e12fd7 | -1.59719 | -51.27329 | 2024-11-30 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1f5eed0c-8e40-3d42-8faa-bc79009c5ef8 | -2.6711 | -46.59938 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7673945c-1673-349b-88c9-632221eac8db | -2.08209 | -48.29853 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b163f04-ae31-3188-8897-50e1932ca625 | -2.72768 | -49.86987 | 2024-11-30 04:40:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 555b9b9f-4b63-3920-ae4b-a00863804b84 | -3.24938 | -50.59582 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41c16fd4-1b34-3e3d-9f18-6f82de24b461 | -2.57514 | -47.01958 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2acbecc1-adea-32e8-8b5e-f1c93a83288d | -2.61616 | -48.1664 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4589bc3-8e3d-35d0-9f73-851f352c6dad | -2.23508 | -46.39867 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6423e9d8-a815-3688-b4d0-f4dc0f223426 | -1.55839 | -51.26408 | 2024-11-30 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a19585cd-e437-39b9-934a-e0566dc4191d | -3.1759 | -51.28448 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c9cb029-79e3-34c6-97fd-43e56cd6ba40 | -3.52673 | -50.32689 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9efd10e-256f-385b-b1b3-daaf3aef4bd3 | -3.26685 | -48.76924 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5430d4f-e580-3bee-b3b1-40621058199c | -2.97937 | -46.94464 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c43d01f9-8179-32d5-9156-dd723ff7f6ce | -3.33422 | -53.5452 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 00ef1e96-ec5d-3572-ada4-704cb65cfeb2 | -3.25374 | -53.86764 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6317b45b-2068-3c3e-ad38-fe1f4f2eef85 | -3.27738 | -48.77088 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a6570e7-5f93-3805-81c7-784d46971fa5 | -4.12514 | -54.2066 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f143fcc-ae24-3875-995e-27a5b1e216d1 | -1.33955 | -54.99639 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45ca8049-6202-372c-8b5b-baace6fe2b41 | -2.29872 | -50.67831 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bfd29ddf-c009-384c-95d1-8318d054f625 | -2.01951 | -48.06638 | 2024-11-30 04:40:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 425d7efd-cd1d-3970-8d70-4b94ead0f8f6 | -4.38548 | -42.15051 | 2024-11-30 04:40:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5153a186-ae5b-3bc1-93c9-b8ccfbd9a84b | -2.09033 | -48.54961 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aabfac6c-1e55-31ab-ba08-8c0312511597 | -1.27738 | -51.62593 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41f1c52b-295e-3744-8aa0-bd531dc16062 | -2.62274 | -46.79989 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5dd8f249-a1f4-3f33-a45b-2f165de18666 | -3.98619 | -46.71504 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fba28bac-e095-333e-bb08-0c4c2a764cf3 | -2.8112 | -54.07153 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 694a7432-5192-340f-ae24-76ad2a919e86 | -2.57036 | -51.84033 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b8da01b5-e0f4-3a31-b2dd-ea60d1600d99 | -3.74468 | -54.68387 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a238711e-abaf-3fcf-b99b-630fe961d1cd | -1.33476 | -55.8479 | 2024-11-30 04:40:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 83aebdbe-65ca-363a-9461-0aceb6d1f292 | -3.25247 | -50.12448 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74a16c22-4c2e-3047-a8c6-e2d4970bd2f7 | -2.91407 | -48.59082 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ab7d066-437b-36d0-93a9-2e5717d76626 | -3.25142 | -50.40807 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 539aa394-b498-366c-b28c-0fb869b92507 | -3.03386 | -50.9806 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 994771a9-562c-3efb-973b-e04da70a1419 | -4.06807 | -46.82076 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| adc66e8a-2f45-37e5-abef-fea4e7ed01cb | -2.80014 | -53.12064 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4430b8bd-f2fb-3154-b51e-ce3cc2f163ec | -0.94205 | -51.6619 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 11aaba00-4ddd-3cc1-9394-0261006e5e2d | -2.56053 | -47.34015 | 2024-11-30 04:40:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 770f16f9-78a2-39d0-96db-2f1a1cbd1c7d | -3.70522 | -45.68738 | 2024-11-30 04:40:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 74b683ef-4e33-3f89-be7e-46f08ab4c49b | -2.83741 | -52.91611 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 29f188da-27df-3238-8092-1c817fbd07da | -1.26022 | -54.55323 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f664995c-ee80-37fb-a6d4-14d7d6093dd1 | -2.60987 | -46.5675 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 634c4388-8480-3092-ac74-c3ba5fb026e1 | -4.9865 | -50.45127 | 2024-11-30 04:40:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 433f7939-73af-362b-ac1f-1337cb587d6b | -3.3047 | -50.75771 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| efd5231a-48f6-3035-8f6e-2f03e503eca4 | -3.44188 | -59.29189 | 2024-11-30 04:40:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ca9aab4d-f89c-357c-a0d6-98bcca2b8a9f | -1.7218 | -46.22479 | 2024-11-30 04:40:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42f624e7-a93b-3ac9-8be0-3e0ba6f57bf0 | -3.33658 | -53.22063 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 81282c1e-145c-3724-8561-2f021d1d1d4d | -1.9663 | -48.38633 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a05c52b0-deab-3245-905d-daf3742ef0bd | -3.0251 | -52.38542 | 2024-11-30 04:40:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38ec47ec-4799-3c88-8f1e-5f848cdcf1c2 | -2.42733 | -54.01906 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5fa472aa-7c32-3244-b064-726a1ed90dc6 | -2.89859 | -51.36859 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1e1efdd9-09df-381a-b14c-1e2227898940 | -2.71555 | -46.21521 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d004d448-bac0-3ef8-a5ce-f800634cce75 | -3.06027 | -53.84723 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba2ccb2c-3ba0-37c9-a948-206b1fcf4315 | -2.5693 | -51.83907 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ccfa35de-26ad-3010-9924-2c04a637a659 | -3.21986 | -49.83217 | 2024-11-30 04:40:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97138cfc-c48d-331a-b8b1-db531530a2fb | -2.36885 | -49.83549 | 2024-11-30 04:40:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04f83823-a81e-3538-904e-f9a016270fe8 | -1.6949 | -52.4581 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f81f9d4-4b96-3351-9da1-e0345d489897 | -2.46963 | -48.47525 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0cb178e-2687-3580-b0e6-edf1d1a2e7e6 | -4.08555 | -47.02446 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba082541-e839-3f3d-9481-3d34d7e5c646 | -2.21851 | -50.40684 | 2024-11-30 04:40:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44d8de15-1bba-39b2-ab95-5849f35c48f7 | -3.61373 | -49.99026 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 654db7e8-ce6d-378d-94bd-343222424348 | -1.58198 | -52.24187 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80d017f6-d246-3aa8-8226-ecbf1639fcbc | -0.96077 | -51.6605 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9786e747-6d1e-320d-89ea-082a1e573f1a | -3.05351 | -48.52427 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0474e5cf-6e33-3364-910e-f98a531ab45b | -3.05619 | -48.50705 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd012593-890e-3c2c-a40d-eca4bb8d9c95 | -2.31609 | -51.95872 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7fbec93-8471-377e-9d6b-af2cbae9be64 | -2.85117 | -54.03001 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 028b1380-3584-38c2-8429-62bccbc7566f | -1.68706 | -45.78707 | 2024-11-30 04:40:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c020d045-8f91-3140-adbb-b81cb6f4e456 | -3.97884 | -46.64641 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c7a6d211-b570-3eff-ac94-6e18103ed41f | -3.32465 | -54.17587 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03e2233b-ac58-3829-bcb3-f2ff32e59634 | -1.72132 | -52.49254 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1b208899-ae5f-3dac-a084-3fbf77255e8e | -4.14634 | -47.8602 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3a2e44f-0ce6-3a7c-b389-f07c306ed810 | -2.71859 | -47.54718 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd19a717-d858-3587-a0d3-e0ecd963018a | -3.20054 | -48.58642 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5f81924-26c4-3428-9ca6-d28c8f79bab9 | -4.1675 | -53.47443 | 2024-11-30 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7b461e2-fee6-37e7-aa21-c81c68276fe5 | -4.31281 | -45.36182 | 2024-11-30 04:40:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README35.md)
