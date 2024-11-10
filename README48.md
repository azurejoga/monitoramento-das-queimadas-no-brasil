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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e65d4f6-22e8-39cf-94a1-d56012be099e | -3.44743 | -50.30554 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1a34103a-13b2-3f4a-a056-ce126cc4d775 | -3.19339 | -48.66029 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aaa5786e-e95f-3f40-bbb1-443c81bcbf83 | -5.72259 | -42.67076 | 2024-11-10 04:14:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 62e41b97-ccd2-3c95-a78e-16950bea51fc | -3.02838 | -49.55238 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eb51d757-42b1-39a2-97ea-f4638030c380 | -4.69253 | -49.62717 | 2024-11-10 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc3dd69b-1601-3fee-8bf8-8480a2a74ee5 | -3.24176 | -50.32411 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1976fb8e-61ff-3e05-b826-50fdcff1e6a8 | -4.05798 | -49.28455 | 2024-11-10 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 70933770-98c3-388f-9aa3-82ccd27af2e7 | -2.67569 | -51.82159 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc796f16-7300-360a-90f9-961e23f2526c | -2.41023 | -46.2965 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ca0ed70-e37c-3d90-8911-3543f9a4eeac | -2.09774 | -46.52981 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ba661a1-1c8a-3b5e-885e-41b4c75b53eb | -2.42456 | -46.30339 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 30.7 |
| cdc520dc-57a5-3408-a16a-0b9b620edeaf | -3.5163 | -44.02628 | 2024-11-10 04:14:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7aa33679-980e-3fa1-94da-582b871b593c | -2.55739 | -45.53785 | 2024-11-10 04:14:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0f76729-56bc-3342-af10-6170167905da | -2.56993 | -46.5346 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16b36abd-715c-3ae3-98c4-66c787106497 | -3.75821 | -41.03158 | 2024-11-10 04:14:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1319bb48-477a-36c8-b2ec-185b99e0c03e | -2.40407 | -48.49068 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4e7a945c-5170-3b08-8da3-b3a0199b20a1 | -5.6901 | -45.17495 | 2024-11-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1e89366d-3ce0-3471-8186-2157a7d12711 | -1.52675 | -52.2042 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 76b545d0-0938-369f-9047-c31f25036f6f | -2.31973 | -53.88183 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fd4dcb50-2640-35ff-a55e-9009965b3ed7 | -3.95147 | -49.00275 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e3c9e1fe-680f-3450-896b-0934805f8e49 | -4.02753 | -44.30142 | 2024-11-10 04:14:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 812c9799-23a4-333a-9c9f-ebad9b1c0d23 | -2.23795 | -53.77125 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a1d967d-d4ca-351d-831d-a6b593d5e978 | -2.37331 | -49.72182 | 2024-11-10 04:14:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c864eb6-2a7d-3ba5-9422-30fa2e507ec0 | -2.97985 | -47.9253 | 2024-11-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be71b4dc-0216-3753-ad6e-433c6c9ea843 | -4.01628 | -43.66236 | 2024-11-10 04:14:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 082014f2-665b-32dc-ac46-67048f7d9a1f | -2.45343 | -47.15936 | 2024-11-10 04:14:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a8e723f4-fe9f-3776-919f-ea7351572deb | -3.11973 | -45.9642 | 2024-11-10 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36a21159-92b7-34ad-bc8e-9cbab116a5ee | -3.51853 | -44.03395 | 2024-11-10 04:14:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 7ffd40c1-a43d-37f4-b8b9-f7e53fe591e3 | -2.03601 | -52.05506 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 78726f96-705b-3745-9401-7197a066d180 | -2.67939 | -46.79821 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 79667676-c89d-334c-ae32-e6baf2dd087b | -4.37007 | -48.14925 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 774fa808-d177-3fd3-8d98-16369759a81d | -3.94892 | -46.40809 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 32fe79d2-f6ff-3f9c-a26f-245b8fe668e3 | -4.28464 | -48.1887 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c1328bf-1168-3e08-b966-6b7f2e6934a3 | -3.35232 | -51.67825 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9fe39e0a-a2cf-3ad2-8719-5df7933316bc | -3.30525 | -45.66872 | 2024-11-10 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7737a43a-f0d2-37a6-865a-bd96db22b52b | -4.68312 | -45.14694 | 2024-11-10 04:14:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7679560-3e3f-3d67-b725-53856c378845 | -3.82674 | -53.77092 | 2024-11-10 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53ad9ae9-d4e7-388d-b8cc-7e3105cb48ca | -2.19062 | -49.53156 | 2024-11-10 04:14:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2721d3b-fb4a-309f-9803-488c8b2f21b7 | -1.52046 | -52.20718 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 910cd15d-5bb6-317c-a914-10e66835dc81 | -3.12774 | -45.96103 | 2024-11-10 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77889476-a2cd-3aac-8c91-a2fe3dff15d0 | -5.60147 | -47.93622 | 2024-11-10 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b1f19ac6-8bbd-35ca-93b3-856da2a258d9 | -3.53631 | -50.33246 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6aa9e1e6-c4cf-3466-acaa-51a899ca69a8 | -2.14593 | -48.83419 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 34fbc5ac-aedc-3be8-a6cc-e5ac8671ba61 | -5.14283 | -48.25352 | 2024-11-10 04:14:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad362701-5f9c-305d-89fe-d39c8823bcc1 | -2.35111 | -46.64054 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c49d9afc-43f7-322d-b587-fc4042f40a02 | -3.24699 | -46.47786 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c8b4e44-cc10-3769-8884-057af4f0f813 | -4.84899 | -48.48358 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 46368bf5-1ee4-37d5-b80b-af83b0f82c6c | -5.89495 | -42.83188 | 2024-11-10 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d3270f96-b157-3556-bc9f-213d5b807c2f | -1.49246 | -51.74257 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ecceb38-ee5f-3267-a1b1-5962b75e0f0c | -2.25911 | -46.51158 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 12a10388-f193-3d46-ac31-c049094acd1c | -4.39028 | -48.57493 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b201f16-1281-395c-8bc4-40412d5355fc | -4.92684 | -40.8411 | 2024-11-10 04:14:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0686b680-a311-394c-8b7d-4d0357c097c7 | -2.00298 | -50.07089 | 2024-11-10 04:14:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e692a62d-69f0-3752-a3b9-bd6f00c3d933 | -0.30539 | -51.70512 | 2024-11-10 04:14:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 926c6fcd-a1cd-3db4-bf53-19e224c2abd3 | -2.90397 | -49.24649 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 266d6c05-34ca-3b1d-9fc4-4e3f9d5e9544 | -2.75858 | -49.35774 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 90572ebe-5f77-3bd2-bb7e-c3236041b479 | -4.6798 | -45.91833 | 2024-11-10 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29820cf4-6336-3a48-891f-1f56ace9f51d | -2.92693 | -48.31615 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d1e268b-fe91-3bf7-8ab4-e02ce167c8f6 | -4.89606 | -48.6146 | 2024-11-10 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 15015164-e67a-30e0-9e8c-a1620777afcb | -3.97618 | -48.18604 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e3889f10-e027-3207-8732-ec026f595378 | -2.56756 | -54.73759 | 2024-11-10 04:14:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f05181d7-6ca7-37ac-a0d3-7f8b564de233 | -3.1127 | -50.15789 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| fa0cc4f2-c542-3799-8d22-71253a0977d0 | -4.19533 | -51.01818 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 320d3f8d-c61f-3f53-8607-c0dbcd2b96f5 | -5.26653 | -44.87949 | 2024-11-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1cf6db4d-a4c1-3640-a1d4-2e4afc8a71d6 | -1.34377 | -51.40956 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a5359bbf-7338-33f2-8218-4779da8376f6 | -4.17089 | -46.60321 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa33b9e0-cfd9-36d6-af4f-d3375a9b1a01 | -3.07852 | -50.42803 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b322cd78-fb09-38ef-a69b-b19ef076b1d0 | -2.08843 | -46.34156 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3de7e4c4-71af-3fb7-9e21-f62a642d51d5 | -2.31365 | -50.67476 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71586483-2d7c-3008-8157-9a02c2ee7802 | -4.05198 | -48.25669 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f78b5bec-8498-359b-b3d7-c8cf10c2db36 | -3.8803 | -49.94845 | 2024-11-10 04:14:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 83d564f8-6c49-36a6-afef-ef1987a3cc7f | -3.23295 | -50.31723 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5cd44ab2-92cd-3cb1-9988-6cd7ce04be60 | -2.42074 | -51.95309 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a124bbf1-e38f-30b1-a348-c7bc03b92e4e | -5.56743 | -43.96795 | 2024-11-10 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 428e4711-bab5-376b-837e-85f84a24124f | -2.66008 | -48.49493 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9f78341-c626-3d22-9ba4-63b3bab29e32 | -4.21806 | -45.69502 | 2024-11-10 04:14:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33c8b109-4c08-313d-a812-e321224ee0c9 | -3.56606 | -45.21426 | 2024-11-10 04:14:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d84aea1-60aa-35de-8ca8-6c03ecf5132b | -3.3517 | -40.70422 | 2024-11-10 04:14:00 | NOAA-21 | URUOCA | CEARÁ | Brasil | 2313906 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 83137746-6ff9-3d22-99b3-04bfd5178662 | -0.4127 | -51.48875 | 2024-11-10 04:14:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 38a9da15-7d8b-3840-8c35-66ffa21890a6 | -3.80219 | -52.26852 | 2024-11-10 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df491b28-ea6e-3c88-9201-e21748e44e5a | -1.18068 | -52.09864 | 2024-11-10 04:14:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 35e9a1ad-bdec-33b3-813c-4c54c7ae3e58 | -3.95268 | -49.40228 | 2024-11-10 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 21ef5fd0-2334-37cb-97f0-6a231fa0c568 | -1.52108 | -52.20331 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f02677e4-ee5e-33a2-8e7e-177570beaebb | -4.01527 | -48.29753 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4864bfb-b0d0-3468-ab40-b2edb81ffe7a | -3.23238 | -50.43936 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23b4cd9b-f45a-39b6-bcc8-e66223c15921 | -3.28741 | -53.2576 | 2024-11-10 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6912e410-7de1-33d2-b995-89d463b0fcfc | -3.90073 | -48.92962 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c47793e-5039-34ea-a6a5-51216ae81ac4 | -2.43089 | -49.87703 | 2024-11-10 04:14:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 074a218d-a918-368d-8328-bd345547ce18 | -3.22719 | -50.68323 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 16b9d6a3-f02b-312a-87b5-1419ae7afa75 | -1.98423 | -46.43661 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e757d85f-1a0e-3148-9993-cb57079f7967 | -3.25908 | -49.89384 | 2024-11-10 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 685df824-9e67-33b8-9b8b-c3d5b4eae84f | -3.2144 | -50.31777 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a7b9ed4-a868-30fd-bb49-115a55ed33d2 | -4.05576 | -48.31185 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ebd5b492-c782-3b86-ab6c-91e1d51379a6 | -5.70633 | -42.73194 | 2024-11-10 04:14:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e93940ce-e773-3452-8b78-dfba96cf2bb5 | -2.61678 | -44.93497 | 2024-11-10 04:14:00 | NOAA-21 | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| accd3028-9db5-3cc4-9b41-f7718397a955 | -3.62471 | -49.61652 | 2024-11-10 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 542a88a4-7a5f-329d-bbd4-edb96f838d84 | -2.67553 | -46.79759 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d1f714c-9cea-3acb-ba1c-b3b5d3fcb1e1 | -2.92316 | -49.50374 | 2024-11-10 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a108c917-c0db-3d3a-beff-638a8ee23636 | -0.0416 | -50.77247 | 2024-11-10 04:14:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c1b90337-df50-3000-90ac-2027c083d11d | -4.10215 | -49.10338 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README49.md)
