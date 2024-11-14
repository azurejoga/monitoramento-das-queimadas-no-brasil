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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e9ac132-07d0-3058-b40d-50abb22e2526 | -2.36981 | -48.52262 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c44ebcc5-41af-3d1c-8c50-c0d60a149a6a | -3.13356 | -51.12384 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5618b16-33ba-3697-a9c6-d5e175515baf | -2.14873 | -48.8044 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 945f054e-c17d-3681-91ca-adecfcbc6d0e | -2.74828 | -51.62548 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7685ebe7-673a-3485-9b88-1626c21232b8 | -1.13609 | -53.65591 | 2024-11-14 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00be2a49-7d1a-3453-b24f-3621a664bbb5 | -1.85262 | -46.28385 | 2024-11-14 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7114f7f7-966e-3c5f-848d-63e7107e82bc | -1.39347 | -52.07806 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b55d30c-ea3d-319b-94b3-04a98c6b686c | -4.33491 | -48.72392 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ae6dad9-f85f-368f-b4fa-d0d1885d487f | -2.21891 | -48.37612 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 372cb91d-5c24-33cd-9877-2138e8cd4add | -2.83493 | -46.65078 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9b0d189-0340-3c6e-b8fd-be34bb1f1af7 | -3.17382 | -50.44806 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f96c9d9-0cbd-3b60-9903-f84726bcbeee | -1.40701 | -51.11893 | 2024-11-14 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d79f1ada-e448-30a1-bdbf-8fa7c7dc6a61 | -5.95008 | -42.43435 | 2024-11-14 04:40:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5d2cdbfd-cd0c-3ca0-9723-3a08c13f4a5d | -2.66572 | -46.81295 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 63860fbf-cf72-3dae-be4e-a2b5464fcbe4 | -4.59483 | -47.06479 | 2024-11-14 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7bd29f70-3c6e-305c-b06a-a1f18a918ca1 | -1.21789 | -51.765 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a19a481f-584f-3ac9-a5a3-9c7f21528750 | -2.69925 | -51.79508 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c90359ef-7d8d-372c-a2df-d16fc8afb233 | -4.06245 | -50.01028 | 2024-11-14 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e28f18e6-ac6b-3956-9521-8025e497c765 | -4.286 | -46.88334 | 2024-11-14 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 70070124-2588-3ef4-a5c0-3603799668f4 | -1.40468 | -52.39661 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d5e8317-d8ca-3737-b663-04092334e7c7 | -2.34154 | -48.59557 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8190d83-2fc6-317b-9261-9bd3257e4e22 | -0.80859 | -51.48516 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 625fd5d6-24d5-3333-89e9-b33e0cdca021 | -2.14043 | -48.79259 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9512f209-7686-3a0c-8999-46bf25df39e7 | -1.87961 | -47.06116 | 2024-11-14 04:40:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a18eb06f-3f3b-38f2-a780-f2ca763513b3 | -2.89717 | -46.85906 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c5fd41a-d900-34f5-8111-f3452660baef | -4.00818 | -48.8562 | 2024-11-14 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 51586441-6344-315e-8c04-c10b214b9065 | -1.38885 | -51.12014 | 2024-11-14 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c2bdf7a1-b942-3a78-a603-f0f9700d7a57 | -2.67313 | -46.83302 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 231a84de-c11b-3d94-9d86-11b46e4e584c | -2.83089 | -46.65402 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 688773bf-5a14-386a-8783-69dd913fb20f | -1.98333 | -46.5733 | 2024-11-14 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 429f96f3-abd6-3546-95b1-e5df2fcb51c6 | -2.61949 | -46.8172 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e1dc44e-6b0e-36e5-9f4f-bd2542bb8c03 | -2.67485 | -46.82195 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fb807589-003b-307b-a670-3f304568e174 | -3.04537 | -50.33209 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efb384ec-6039-3e13-a08d-c7320b0cbb66 | -0.41473 | -51.57769 | 2024-11-14 04:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c105b08e-00ee-3a3d-93ff-cf277bb7e257 | -0.90194 | -51.7239 | 2024-11-14 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f1fbd82-ac3d-3c8f-ba0d-ca8d221d0e47 | -4.65021 | -44.14561 | 2024-11-14 04:40:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b5fe059-77ea-36de-a18c-b1e24f5fb984 | -1.22185 | -51.7871 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd1777e4-e1d7-3995-9136-0b72d33be8d2 | -4.37314 | -48.0807 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dc29e863-bd37-3dfe-9d62-118398f76cb6 | -1.39647 | -51.43825 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df21dd61-8475-33ef-a14a-0667364915c1 | -2.2698 | -50.81526 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18c7be9d-4b15-34e4-89d8-81c2e792666b | -4.50628 | -48.6944 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 926d29ee-0656-357b-9afc-90cc8fa7baa2 | -2.63439 | -46.17231 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6a59b0b-9d86-3172-84d4-adf45c04e83c | -2.61973 | -46.17408 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f93492df-c68c-372a-9b37-666650a962e3 | -1.39173 | -51.12459 | 2024-11-14 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d1a17648-ec79-3d9b-a194-e4d29d44563f | -4.0903 | -49.16174 | 2024-11-14 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3cfb252-7980-32a9-abb3-a29fa028c99c | -2.64082 | -46.17732 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0dcb998f-2b9a-3426-a9e8-092d515d27da | -3.2852 | -45.36517 | 2024-11-14 04:40:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0fac0fff-e8da-330d-8d4d-b63e05001f70 | -2.89262 | -46.8432 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61cdb32d-6aee-34f3-a72d-ec438a26c29f | -4.45243 | -45.36106 | 2024-11-14 04:40:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ca7ffdf-070e-364c-baff-1fd4abdb0543 | -3.93798 | -46.48138 | 2024-11-14 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41992a10-15c6-326f-a269-1d290c926ee4 | -3.47044 | -50.31102 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22cf9475-f837-36d8-8292-90a1463fe6cb | -1.39009 | -51.11234 | 2024-11-14 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| df46a620-be4c-3724-9b4e-13cedcaa0072 | -2.40742 | -48.93645 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 60b36bc8-221b-31f9-a289-c5032517eb1a | -4.59195 | -47.06052 | 2024-11-14 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 717f3a7a-4021-34d3-bd50-a0cc0146fbf3 | -3.41228 | -50.31612 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 03d3ce6e-28b6-301e-8bdb-fbdf6a512446 | -4.44548 | -46.5742 | 2024-11-14 04:40:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3ff668a-a276-30cf-90c0-ca6f7f3f0b7d | -4.05046 | -47.22861 | 2024-11-14 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d4cf5dca-b755-32ec-bd45-2eb0907788af | -5.69543 | -46.56735 | 2024-11-14 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99f5a6bb-d776-36f2-b8da-d10deab40886 | -3.03539 | -47.96061 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7bba1828-6892-3e25-92c0-ff52ae653cd0 | -1.40164 | -51.13011 | 2024-11-14 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c0e65834-2ca5-3be1-a4b5-dc78d977695d | -2.23715 | -49.00079 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1409e5b2-39fb-3509-b1da-994b51df2012 | -2.05629 | -52.05862 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02145729-129a-3fb3-ba1d-95d1777d6449 | -2.42128 | -46.26082 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6f493fb-7072-353c-9248-19df1b3b8583 | -2.73441 | -49.49925 | 2024-11-14 04:40:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4fe6143b-6e98-3027-9661-06182f47a46a | -1.60575 | -52.40161 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 71f7832c-4cf3-333e-ba12-d52e2785f242 | -3.01712 | -47.96854 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2df02d69-0bc1-3344-ab87-47db79f4ed33 | -2.8014 | -51.49586 | 2024-11-14 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0884f324-90b0-3d51-874c-bcbc48e02b7b | -2.42071 | -48.95958 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8520f130-a507-3c6f-81fc-99d20c606392 | -3.74562 | -50.44848 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b18d4c8-4330-36d3-acfa-5a962e06791a | -4.05671 | -47.23333 | 2024-11-14 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a1df64ae-ec68-3b11-8d7b-1de6eec327ce | -0.6537 | -52.36508 | 2024-11-14 04:40:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c1e14c1-beb2-3930-9de1-a1c002b2a3f9 | -2.25959 | -47.32815 | 2024-11-14 04:40:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 95f0b174-360c-3a8b-a424-a0c07d0c78f8 | -3.3009 | -51.59509 | 2024-11-14 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0104ee06-c6ed-3430-9e6d-e006625a7e7c | -1.1077 | -53.02375 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23e48d98-8161-387d-a0fe-9710ab593e4b | -2.47757 | -45.84812 | 2024-11-14 04:40:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f2f165f-18be-397d-9bcc-0482d64a3f26 | -3.41004 | -50.30849 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3bfdf3a6-ed30-377e-863f-5b9aa0e20a8a | -2.40979 | -48.48306 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c628eac-3547-3de8-94e9-3aa0de73e8fe | -6.27889 | -44.96593 | 2024-11-14 04:40:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c83c822-4139-3a8d-9675-5fc4cc220d8d | -0.90868 | -52.42052 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e72fc1f7-4666-3636-a172-85f35d4ee679 | -2.3062 | -49.08201 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0775b97-15ca-3b02-a20a-07281bd5a0ca | -2.59362 | -48.19809 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61a200b6-0e0e-3793-8ead-122a1cef849a | -3.26987 | -50.57352 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9a00136-8095-3cec-b36f-bbcaf143d472 | -1.84891 | -53.69044 | 2024-11-14 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 121a5536-8f8d-32aa-9162-6c77413bd381 | -3.77778 | -51.3348 | 2024-11-14 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af0687da-40f3-3c86-904a-dd6b36c720f2 | -1.39649 | -51.11732 | 2024-11-14 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3d3857d-acf1-326f-a091-47cb4091d714 | -2.72522 | -53.19902 | 2024-11-14 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4377fce7-493c-33fb-9cf3-aaeb071345de | -2.62324 | -46.17462 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fad25a3c-8b2f-3a23-ba4e-b3754695b68a | -3.43466 | -50.30502 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19ee2c60-b553-38e6-8a6d-8504bea922b5 | -3.1584 | -50.58995 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc7c4c88-177b-3761-8b9b-9861fa1e5a1e | -1.63442 | -52.51968 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1c71917-1d24-3839-8906-663267a5075a | -2.90308 | -45.59214 | 2024-11-14 04:40:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89263812-457a-33d6-9ee1-db9180b96288 | -2.21248 | -53.7118 | 2024-11-14 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1d3130f6-d6b5-3dd9-aeba-b27f5f7bc0a0 | -4.29629 | -48.18422 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5db6c518-f855-3479-944f-d9cc177de31e | -2.6373 | -46.17678 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cb43e94e-b270-3289-b31d-8472dda3bee1 | -1.89376 | -47.99726 | 2024-11-14 04:40:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 33318014-5a47-3f2f-a8f5-0a84b26c6f71 | -2.65487 | -46.83778 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be622074-3266-3be3-bbfd-eb0f8c9307aa | -3.16037 | -48.36075 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8806563b-c551-37a6-8228-3d305c83aa00 | -2.61621 | -46.17355 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa361a1c-ffff-391d-a4fc-7e12ac58ca71 | -2.21239 | -48.39623 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 027d19fc-d487-34ed-a9b9-a3a615449c58 | -1.41064 | -52.39094 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README36.md)
