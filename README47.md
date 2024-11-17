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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 18d59f16-a102-3f4b-b8b6-d4e876bb4200 | -4.64936 | -45.00732 | 2024-11-17 04:29:00 | NOAA-20 | LAGO DOS RODRIGUES | MARANHÃO | Brasil | 2105948 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca0e3ecf-dc05-33c9-a933-e77e6559f493 | -3.43358 | -53.32494 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40ea580f-cf8d-3c87-a9f6-84906b7ba6f9 | -2.72831 | -53.19508 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a082e616-f484-32d1-9977-bfa4f66c08b0 | -1.11562 | -48.36036 | 2024-11-17 04:29:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7daf6d2-5995-368d-a7ba-6fab3ae58b80 | -3.99766 | -53.73724 | 2024-11-17 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d316407-124a-3923-8d1c-5c68ccc9c977 | -2.16846 | -48.33433 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8bf359f4-6f0d-3f91-bf21-9685d03957e1 | -4.14881 | -50.77324 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c70e8e6-3706-3d8b-a7c9-1f8f67e18c4f | -2.13528 | -46.49464 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fefb79fc-e173-3e6c-90c2-d78c28c79a7c | -2.90785 | -46.85477 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa786d0a-1022-3561-8d79-cca57358f28f | -1.58338 | -50.44603 | 2024-11-17 04:29:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| baeabd5a-ca68-3d73-a2be-f1f7dc47acfa | -2.86367 | -46.72458 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 77fc9e06-29dd-3140-a811-40e0ca7f6765 | -2.30594 | -47.9564 | 2024-11-17 04:29:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a937f980-9c29-34dc-80c9-d6f65a6b4356 | -4.13972 | -42.12657 | 2024-11-17 04:29:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 98ff7648-b950-32ac-92ee-cf3c2ce747e2 | -2.67643 | -46.85761 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d41dc00c-27c3-3691-a819-10d5eb2fa9be | -2.28173 | -48.41435 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| def37375-6e0d-37bc-ac2c-e556a08a94d5 | -3.52371 | -50.25222 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 1df89aea-ec6a-3376-9dd2-81722ddd699f | -2.47795 | -48.59281 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1ff20bf-19ae-36bb-a4a5-871a75bd3446 | -2.13626 | -48.12496 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18f3a554-5a54-346e-84cf-950c0e67f554 | -4.13423 | -46.94141 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f77d789-ce92-3211-8aa5-5a6674106029 | -2.30255 | -49.13057 | 2024-11-17 04:29:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9e842c40-c3de-31a0-b729-7137db70f3a7 | -3.1955 | -46.53652 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d47f648-baf0-3668-bd2c-95b9906bad46 | -2.13833 | -46.41049 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2231331a-847f-3595-81d5-25d05e970baa | -3.01148 | -47.42736 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4aee0d0-ee16-3553-a36a-1f200b7c5edb | -1.99544 | -46.58553 | 2024-11-17 04:29:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e7a01469-25b1-37aa-8505-252a1b33f21d | -2.22124 | -53.60807 | 2024-11-17 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10d5c1ca-7089-39ee-96d9-69b77c490cc2 | -3.83815 | -51.30128 | 2024-11-17 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7352c9a-6557-3a3d-8e18-0e8a05dd4dd1 | -2.08406 | -48.95815 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9d4726be-c334-3b79-9b91-8d40fd3b89ad | -2.53059 | -47.13718 | 2024-11-17 04:29:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17e2cfa0-f8ea-3050-8dad-811f685b8e31 | -3.52306 | -50.25636 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e2b399d0-0f1a-33f6-9cde-584a38a4db1d | -5.42346 | -45.34373 | 2024-11-17 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b8527a43-c282-3a7f-b7ae-fb2389b7aa6b | -0.92924 | -51.64095 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29b8d10c-3006-3598-ba83-e303356a16d6 | -4.37837 | -48.08857 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c45ccb6b-ffcd-333f-9710-0f28564f36d8 | -3.87246 | -50.44269 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5819a568-fab7-3f1e-a2a1-e077e20bfc33 | -2.27759 | -47.91964 | 2024-11-17 04:29:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2d5c49ed-13d9-3d9c-aaa4-363fe01ae2df | -2.66643 | -46.20589 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a7fc544-f5b7-3baf-a11c-dadd42119607 | -2.61934 | -46.83106 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4171f67-eadc-32c1-b2be-314d4359ebac | -1.92485 | -48.52243 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5af48e33-01a3-36e5-b6b1-7638f31f9a52 | -3.91424 | -46.524 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 464939d9-563a-36b9-b93e-cff005179efb | -3.8139 | -49.25772 | 2024-11-17 04:29:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9ef1795e-6307-3bcb-92c2-5cd0b7a99524 | -2.86383 | -48.72667 | 2024-11-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd1b9a8c-bb0d-3e9e-985d-43bb66569ea1 | -3.23968 | -48.00548 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f05d59ea-9bb8-3b68-ba28-e1a5d3bda550 | -3.82253 | -50.23822 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 935a794e-8de0-3175-8a7b-2c5d9c04cddc | -2.1306 | -48.94958 | 2024-11-17 04:29:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f8012a12-e4d2-3db1-a3ec-7cc0905e828e | -3.57807 | -50.52479 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c1b71b0f-0a83-360f-b720-5457997f02df | -2.58193 | -47.5649 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 733938a5-e1ae-37ac-927b-2c27f407fd04 | -2.68236 | -46.81984 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af619ff8-d16a-3535-89b8-a0077294e917 | -1.39962 | -52.42725 | 2024-11-17 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6780644-9cd1-3f45-b871-f33f9c45c2fe | -2.86751 | -46.72165 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| ddf2a489-6749-396a-92b7-44b3071b8c1b | -3.20695 | -46.67971 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 571a5710-d58a-32b5-ae12-af5d5046495a | -2.07842 | -48.53074 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bf2462ee-6c5e-36ba-8957-c3bdefff724f | -4.36778 | -48.4957 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a13bf9b0-3424-3da3-a1b2-fa1211bd0c57 | -0.0292 | -51.66582 | 2024-11-17 04:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 77407974-dd6d-3c02-83ef-fc66536c69be | -5.31309 | -45.44767 | 2024-11-17 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 75f14213-11e5-31b8-ba75-f4f918578511 | -2.23155 | -53.61061 | 2024-11-17 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 04c88932-de7b-368e-9a1a-09ad5572367a | -4.28403 | -48.21248 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 358fcfe4-c5a7-3bce-8bec-0369e9304baf | -3.56953 | -50.25446 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b93a1edf-39c7-3573-9c64-6f324df3aaa0 | -2.66094 | -46.21929 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5f5b67c1-0548-3778-8178-979c63067bf6 | -2.90511 | -48.31382 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71b60826-c47b-33e0-b405-5a0b44899617 | -3.14558 | -45.98605 | 2024-11-17 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a923578e-7feb-3688-9cd9-354bf0bab7e7 | -2.09695 | -48.39301 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6297cc98-b22a-3bad-b24c-1d9f3cce7178 | -3.08845 | -45.22273 | 2024-11-17 04:29:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7020b61d-3728-3e3e-b880-ca602ddc9c53 | -3.69857 | -47.68014 | 2024-11-17 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a1470e9-daee-30e0-82bb-2a307e70b917 | -4.20611 | -48.70655 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac97eefc-4fd1-32a5-829e-01cdf3509638 | -2.68243 | -46.84095 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d8a572c-51ab-3f61-9c16-a84d3e1ff57a | -1.79223 | -48.0716 | 2024-11-17 04:29:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 252fa56d-50e6-3f0a-9973-44c07e40b012 | -3.20971 | -46.68366 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b2e850c-be58-3156-acfc-151fc5fdd268 | -6.49289 | -47.49841 | 2024-11-17 04:29:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5b0d8527-e12b-3931-827f-f0bba482544e | -3.01247 | -45.39832 | 2024-11-17 04:29:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74f39dfe-5235-393c-88eb-1e036bba9795 | -2.65264 | -46.16426 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 091f5048-6fb0-3643-ac5c-1b1f778d9053 | -1.07295 | -48.19053 | 2024-11-17 04:29:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 11099c1c-e7ca-3737-956a-b848dc27efb7 | -3.83185 | -46.52927 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e7eab73-a997-3c9c-a641-96968eb7f421 | -2.63454 | -48.56093 | 2024-11-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bd4be43e-22ff-33c7-9576-11da619b860d | -2.22295 | -46.41341 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87b87b5b-c61a-3871-8988-fa78c06ecae1 | -2.68195 | -46.2154 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d46b9413-ff63-36fd-80ad-a737a3cbe1b5 | -3.36357 | -51.45157 | 2024-11-17 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d7a4813-b0ba-31d0-8911-61a371a65f42 | -4.20948 | -48.70708 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a763aef-d1ea-384b-a2c4-663985c83b7c | -2.24004 | -48.7014 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b39c25b8-66f6-3dcf-a192-df8d3403ecb7 | -2.17566 | -48.44225 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a33009e5-c961-36f6-ae4c-716df0a0ed5b | -1.21324 | -53.5675 | 2024-11-17 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 098c476f-c7e8-332d-ba27-3fc158aa4e96 | -2.90149 | -53.05056 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52c5ef12-0ea3-3f57-b1f8-b20afecb10b0 | -0.30896 | -51.50437 | 2024-11-17 04:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6e071eb-c02a-3587-adbc-b4cff898d505 | -0.40637 | -51.62415 | 2024-11-17 04:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a0134fa-2cc9-33f0-8cdc-a1ffbf09ce38 | -2.6792 | -46.86156 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce30d61b-d73f-37a1-b102-483af6ba26b5 | -2.6686 | -46.19198 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f263f7ec-a97f-37c0-b5c6-ef5faad5219b | -0.95043 | -52.41971 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8e3b878c-291e-39d1-84ed-3f5b62d0e7e6 | -4.26498 | -48.54476 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 568f8b6c-4c34-3791-82b3-bf9e1a36c41c | -2.85288 | -46.62069 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a7a72f93-0ed7-3e11-9846-2290345a3a97 | -3.91478 | -46.52052 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15dfd6d3-cd25-301e-92e4-6a67bab661df | -2.28489 | -46.90472 | 2024-11-17 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 989a90e8-4e14-3f9c-b17d-bdf7d6270a23 | -2.19903 | -46.34966 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b9c82b4-c0fc-3da1-a119-16faa3cca526 | -2.61988 | -48.56601 | 2024-11-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f1af795-55d9-30ac-a0fc-3fe23ea5ff32 | -4.33076 | -43.04864 | 2024-11-17 04:29:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2aff4fd-5f78-370d-a2df-7dc75a00f0c3 | -2.47508 | -45.4055 | 2024-11-17 04:29:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f6c81ed5-904d-31dd-93e1-930572ebd27b | -3.94203 | -49.48941 | 2024-11-17 04:29:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa6bac2a-49bb-3f7e-9524-214e8d14f3d9 | -0.82738 | -52.29604 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ff48904-807f-3a21-94d7-5e8c0618cf78 | -4.7717 | -48.02979 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e45aa35a-5e39-3404-a98f-66a9f86f9ea0 | -2.90286 | -46.84344 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3b28242-e977-3fe3-8cfa-ce6ece549019 | -2.58084 | -47.5718 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5e88cfa6-8ebe-344e-9ab1-e3f74f795d3b | -6.47473 | -47.5062 | 2024-11-17 04:29:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af986482-80c6-343e-a305-ce2f10e56d47 | -3.21315 | -42.09135 | 2024-11-17 04:29:00 | NOAA-20 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README48.md)
