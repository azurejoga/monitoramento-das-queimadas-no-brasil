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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0cda9e3-88b6-3a08-8129-912caea1e2df | -1.92249 | -45.7704 | 2024-11-20 04:25:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3475c114-3e25-3c78-a26f-317d3b467bf9 | -2.17519 | -48.45821 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33d54fd7-028c-35bd-8735-ed672cba3f6b | -1.15061 | -53.51158 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 834e03f7-4df7-3d2d-9616-36c39c705bb6 | -3.19314 | -46.28004 | 2024-11-20 04:25:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23734d8c-f485-3173-a25c-c2db8ab7433f | -2.72698 | -47.97174 | 2024-11-20 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c16c7c3-1b26-3307-ae8b-3ba072cb09b2 | -2.59653 | -48.29297 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56098ae7-e62a-3714-8ce1-255cf762f071 | -2.6109 | -48.24695 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ba0422bf-d9ec-31b0-aab7-e29e1a7ccd85 | -2.22409 | -48.37934 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d2a463a-2c7d-3107-8b52-19cf16bbf17b | -2.68227 | -46.17479 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c743507-a04f-3c05-8455-3543210d790b | -1.14558 | -53.51093 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fea1b74e-2173-37d0-a64c-22b39d42fa82 | -1.70471 | -52.14854 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dd4893a5-16e9-3972-a366-8f647d3c864b | 0.63695 | -50.57475 | 2024-11-20 04:25:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e451a879-59b6-3636-9feb-ccb594f6a528 | -1.29798 | -52.24793 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e67c59b-3982-3053-81fe-0ce8287e1d73 | -1.3956 | -52.43483 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf0fb584-fe9b-326b-9d6e-ce7efc8b7ae1 | -2.78541 | -45.95114 | 2024-11-20 04:25:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5d5ee34-94aa-3b77-a295-50b2dc2ae85b | -2.57602 | -46.54906 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c01dcabb-c864-36e4-9dc3-14821e5eb142 | -1.85436 | -47.82759 | 2024-11-20 04:25:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 24dab053-0467-37f3-8ef0-047c93928219 | -2.91846 | -46.83951 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff7c2177-19fd-3684-8410-248c2428d444 | -1.98429 | -48.68579 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37ebdeec-b3ea-3b7a-9dfe-473fdc424944 | -1.66517 | -52.09351 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ef9a1f2-1e9c-3f9d-bd51-74b4a10a8531 | -2.12835 | -48.53001 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d69684ed-0411-3191-ab8e-b03fac032f49 | -0.77616 | -51.74787 | 2024-11-20 04:25:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bf3b3a8c-05f0-3ab6-ab68-395009a9782a | -1.90254 | -53.3345 | 2024-11-20 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 060a42e3-0c87-3e12-b5cb-dac58ecbdb32 | -2.41459 | -45.81906 | 2024-11-20 04:25:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aea02c1e-c03c-3f61-a62f-4e431a07e8f7 | -2.1098 | -48.96242 | 2024-11-20 04:25:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68c40092-8a83-36f9-b1c6-7a661144364d | -1.92295 | -47.05298 | 2024-11-20 04:25:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb2444d7-50d2-3234-8003-6dbf9019c8ca | -1.19593 | -53.68036 | 2024-11-20 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f6710f35-be99-3e0f-b0cb-e83cc6a73cd7 | -2.59403 | -47.78885 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bfab8c3-bcc2-3b64-9f52-dc8f430d6fff | -1.20373 | -46.53653 | 2024-11-20 04:25:00 | NOAA-21 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6906cf5-8b1f-3d59-a302-84af3939cdf2 | -3.32911 | -43.0822 | 2024-11-20 04:25:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e855bf4-09a9-3fa0-939c-46509984f680 | -1.70938 | -47.04931 | 2024-11-20 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec977754-04f5-3f6f-8d51-75cd20e39b54 | -0.27903 | -51.44188 | 2024-11-20 04:25:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7420e777-d3f2-34bf-ade6-601599869c29 | -0.18716 | -51.62487 | 2024-11-20 04:25:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 89be062d-8516-3238-ac1d-8ed7b38cb3e3 | -2.78686 | -48.60228 | 2024-11-20 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff8fd313-944c-3bbb-9f69-fecfe557ee36 | -2.82437 | -45.1335 | 2024-11-20 04:25:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c100bb40-5115-3ab1-902d-2992a6367ff3 | -2.13379 | -49.12073 | 2024-11-20 04:25:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cebe1a3d-4a28-37d2-a257-155d8463a2ff | -2.69173 | -46.04927 | 2024-11-20 04:25:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 14e6a11c-a648-32d5-8f77-7dc6c88926d8 | -0.18784 | -51.62048 | 2024-11-20 04:25:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b8d98f34-37dc-3102-ae62-48f64c332384 | -1.64673 | -52.68731 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4c56470-b4cc-3d11-8399-de7e56a4b4b5 | -2.68635 | -46.23552 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3f93b408-779c-3f96-a58c-9d16517c4690 | -3.00155 | -46.96075 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac82284a-56b9-3a44-8ced-c917f66a4e78 | -1.31447 | -47.80164 | 2024-11-20 04:25:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 829f7bcc-3994-3b4b-b231-7df44a6b4278 | -1.23895 | -52.02335 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 721dd170-047e-3b70-a537-9510e1145aea | -1.33218 | -52.23885 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aa6b9462-eddb-3bab-8133-c793f17fb900 | -2.71004 | -46.08382 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3cc617a1-d2fc-335f-8cdc-e499415de374 | -2.64329 | -46.22887 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4d83ebb-bc3b-3d1f-8a12-7b66369f47d8 | -2.53905 | -47.33352 | 2024-11-20 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1440596f-1f04-3e37-8933-ed8d6ffa65d4 | -1.54229 | -51.18898 | 2024-11-20 04:25:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82f4a615-9b3d-30b9-8f53-cf771e71c478 | -2.62912 | -46.83744 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47610fb0-2e44-3ab2-9533-3349a611a650 | -2.1993 | -49.54775 | 2024-11-20 04:25:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6e2dada-db65-3db4-93ea-c931b0fad950 | -3.77783 | -46.67279 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b2e4b164-ba28-38bc-bedf-0acf94e1991a | -3.01007 | -51.01334 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92fd5d7c-8c63-326c-b279-f8067823a45c | -9.1958 | -44.72779 | 2024-11-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b0c6c6cb-385a-3b43-ad26-ffeec43e0b26 | -4.05986 | -54.05013 | 2024-11-20 04:27:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a57534bb-ceb7-3666-98c9-22db7c831240 | -5.45185 | -44.8261 | 2024-11-20 04:27:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c29bf7c-e92c-34ef-90bb-265e33ce4267 | -2.94598 | -54.79926 | 2024-11-20 04:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0db83db-6057-3780-8311-6172d62ccbce | -3.08629 | -54.66627 | 2024-11-20 04:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 45aeb771-65c6-3305-9851-41632f1e5e0c | -4.06414 | -46.84274 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b0c385ca-b88a-3bb7-bd90-073c2011b70e | -2.4688 | -54.74841 | 2024-11-20 04:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c869b16e-9973-3e0c-83ff-ac6bc2887e93 | -2.62217 | -51.80711 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2540ea9d-d55b-3fe8-86e6-74257a46e4cb | -3.4192 | -50.70867 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f239b5ea-0658-3623-899d-8c4ec83f37fc | -4.99027 | -46.92459 | 2024-11-20 04:27:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d81de58-5040-3f68-a41f-583c5a4d12f2 | -4.02703 | -46.40729 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 717c8635-559d-3ab5-bf01-a70db9048e57 | -2.71309 | -53.17675 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e44f8e3-8944-3bbd-a059-6e7b0d01f23b | -7.15161 | -48.31972 | 2024-11-20 04:27:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2186170e-1c4d-3c7e-9a9d-441e801cd993 | -8.00091 | -44.37192 | 2024-11-20 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17ae4716-2858-3095-af54-ec456d4f3457 | -4.77844 | -46.49712 | 2024-11-20 04:27:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0cac9cf-bc1c-3e64-8557-c8d00d1c58f2 | -10.42448 | -44.49028 | 2024-11-20 04:27:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2c845086-65dc-3985-a45a-ccd522adcade | -5.46606 | -46.47145 | 2024-11-20 04:27:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bdb33dc4-66c2-395b-93cc-2e8fdcbdad5d | -3.94329 | -46.70256 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3e3323a-4d22-3a81-aaae-0977825495d0 | -6.31147 | -41.51512 | 2024-11-20 04:27:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ee3247d2-0301-3394-8336-ace85a1370b3 | -2.94665 | -48.07181 | 2024-11-20 04:27:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 067d0dbe-6c64-3d16-bcb5-c320a0626ebd | -7.17556 | -45.04253 | 2024-11-20 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e71672a-285f-3734-9352-dca3dd56d6a1 | -3.29113 | -53.84762 | 2024-11-20 04:27:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f4e434ee-6397-3a64-85d3-a8dc787d1fc2 | -4.09517 | -44.85498 | 2024-11-20 04:27:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2fc4168c-f48c-30ce-bf8d-8492e1d1a2e8 | -4.16384 | -45.50846 | 2024-11-20 04:27:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed0c84fb-c9c0-38a1-88dd-8b9915b5be13 | -3.36818 | -54.09921 | 2024-11-20 04:27:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5aeee0b4-58f5-3394-92ed-c3d000c9e28b | -4.25023 | -53.66284 | 2024-11-20 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f07ca564-6f32-31e0-860c-1789a7cd97c2 | -4.19456 | -46.81363 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c46b0eb-c5f3-375a-a0eb-ec5822a8f151 | -5.44615 | -43.23452 | 2024-11-20 04:27:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3cca5a19-17e7-3470-8a99-13f529e21421 | -4.77898 | -46.49367 | 2024-11-20 04:27:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 696f1760-0c70-3098-8b0a-c1c8dad82e1e | -8.00007 | -44.36883 | 2024-11-20 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13524e20-55f5-3e42-9eb4-8e564603f440 | -5.73296 | -46.19947 | 2024-11-20 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d54c10a0-eaf0-3ff9-8965-d647f3ada9a6 | -3.21195 | -46.46354 | 2024-11-20 04:27:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a3c7b21-a77a-30e8-9243-d721c970e188 | -2.9144 | -53.06322 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 948d2067-3e65-3bb4-81b6-942f6b130690 | -4.65343 | -49.02176 | 2024-11-20 04:27:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7301b714-d372-3761-ba51-01b3ee6c5898 | -3.48493 | -54.70069 | 2024-11-20 04:27:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d83bcdd-2bc0-3dc4-9d0c-220f00f9535a | -10.45372 | -44.88383 | 2024-11-20 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49b79368-538e-3a20-9e07-3f9cd5358522 | -11.24736 | -44.44221 | 2024-11-20 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f786cf4b-3c40-346b-a826-9961f8378771 | -3.99888 | -46.39233 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fbf255d-5643-3134-91ec-617762d5f6ff | -5.9785 | -45.3619 | 2024-11-20 04:27:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3047e946-d02a-3a5a-9bb5-73f2e2e459d0 | -3.51179 | -45.35017 | 2024-11-20 04:27:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c6e6395-8636-3c05-9b5a-f9e1b83c51b0 | -3.76835 | -53.84957 | 2024-11-20 04:27:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1bb2be40-b508-3c6d-a337-d66955173cc9 | -7.22135 | -45.08307 | 2024-11-20 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae1ed182-f7dc-34db-8785-df5de0a23218 | -3.77737 | -53.95974 | 2024-11-20 04:27:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 44298f90-86f9-3b61-aa7e-ff10dfcec667 | -5.48711 | -46.20654 | 2024-11-20 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 32858154-f3db-31b8-a6c5-f53a7dda8316 | -11.03783 | -44.57092 | 2024-11-20 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 30.4 |
| cc5cb76b-5ef5-3f8a-8b6e-bd4d4e6004e6 | -5.63948 | -46.36498 | 2024-11-20 04:27:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b9fafc55-afd5-3461-8c01-cdedfa43918f | -3.79332 | -46.94367 | 2024-11-20 04:27:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f72f561-6e05-3931-bd8a-4a64cc7bf473 | -11.06328 | -41.61663 | 2024-11-20 04:27:00 | NOAA-21 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |


[Clique aqui para ver as próximas entradas](README31.md)
