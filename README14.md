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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd99140c-c194-3373-ab5e-60b717b9177e | -1.51831 | -47.45306 | 2024-11-17 01:04:00 | TERRA_M-M | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 7b54d1ad-6470-3462-8970-10fc9d225e5a | -4.56222 | -47.99984 | 2024-11-17 01:04:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| d579b05c-b714-385b-b0b1-21cc33d75ff2 | -2.60628 | -47.56509 | 2024-11-17 01:04:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| dfb38f1c-faa0-3df0-8c10-c7a5bdbd930f | 0.61005 | -51.77451 | 2024-11-17 01:04:00 | TERRA_M-M | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 835d5dd3-b365-3af6-b89c-14e7134c5863 | -2.8749 | -45.39727 | 2024-11-17 01:04:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| bccede78-797a-335f-9ea0-a459045c6e65 | -3.517 | -50.25036 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d62684b7-4b0d-3c44-bed4-fd05b3a0a3ed | -4.47572 | -48.10819 | 2024-11-17 01:04:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 8fe9436b-36e9-3ed4-84c6-a14d59930f22 | -4.65375 | -45.00837 | 2024-11-17 01:04:00 | TERRA_M-M | LAGO DOS RODRIGUES | MARANHÃO | Brasil | 2105948 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 90f3d636-b7cc-3139-9a97-4884e4718519 | -5.88701 | -43.88225 | 2024-11-17 01:04:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| da5ba801-3bc6-38b2-a357-6879b6e46f47 | -1.96721 | -48.38069 | 2024-11-17 01:04:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 7eaf5afe-aa07-368b-a09e-41cf3199fc8a | -2.06711 | -46.5484 | 2024-11-17 01:04:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| e39af60d-10ad-31f7-8ba8-2b28e387a1a7 | -0.94115 | -51.73006 | 2024-11-17 01:04:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| dea55d92-84d5-3681-aa05-0b508c0ebb47 | -3.91576 | -49.03743 | 2024-11-17 01:04:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c89723ea-e7a2-3e43-9677-66bcb58556ea | -2.16589 | -46.11915 | 2024-11-17 01:04:00 | TERRA_M-M | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 23923144-5d3a-3374-800c-bb819c23088f | -3.53551 | -50.51331 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 4c5a472d-db8e-362a-8e1e-c88024cbb4c1 | -4.20308 | -48.71069 | 2024-11-17 01:04:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 20214e02-5c79-3210-9f83-9d0376f44e58 | -4.30056 | -48.10117 | 2024-11-17 01:04:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| bb0c5996-69be-3ae5-a55f-cc29f9604085 | 0.00377 | -51.22507 | 2024-11-17 01:04:00 | TERRA_M-M | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 73cd7773-8d57-31ee-912e-c5319b524d4a | -0.04872 | -53.25831 | 2024-11-17 01:04:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c39e77db-770c-3142-8dfa-b9b6f1d6f985 | -3.1133 | -45.0574 | 2024-11-17 01:04:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 21.0 |
| f53722cf-9aa9-3c32-8fdb-ddaadfd17b84 | -4.40123 | -45.53397 | 2024-11-17 01:04:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 5268810c-1e3a-3c19-a667-787c311f893e | -1.26078 | -47.09563 | 2024-11-17 01:04:00 | TERRA_M-M | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 05b6f4ea-1e39-3d3f-9f5d-fe185cedbaae | -2.38068 | -48.91651 | 2024-11-17 01:04:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a8693bbb-5135-338f-a2ac-d83da665109d | -3.59317 | -49.35757 | 2024-11-17 01:04:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 75fcacbe-e70f-38c4-a9a7-d152563f4750 | -1.58275 | -50.44988 | 2024-11-17 01:04:00 | TERRA_M-M | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a2ff93bd-31fc-39d2-bfe8-a35372da1fd2 | -3.39147 | -50.73645 | 2024-11-17 01:04:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ea7116a0-9f3b-34bc-9340-30a3ce0f521d | -4.63702 | -50.41953 | 2024-11-17 01:04:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a7362620-8bfd-33a0-828c-081f83e6931d | -4.54425 | -45.25532 | 2024-11-17 01:04:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 831e58f9-01db-3d5a-8ccc-fb7a545c661b | -3.33121 | -50.49986 | 2024-11-17 01:04:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 236c0ff3-e63c-3456-8dd3-46a8516006aa | -2.83592 | -45.50032 | 2024-11-17 01:04:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 92.2 |
| d0bcfe15-c3e2-3427-a35f-06f478f191e9 | -2.27822 | -47.9129 | 2024-11-17 01:04:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 9ab75ac1-56a3-346d-9c1b-97d4cedc0700 | -3.18852 | -53.2505 | 2024-11-17 01:04:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| ac4da928-b804-3245-9839-8ef7e9de7bd6 | -0.1114 | -51.59709 | 2024-11-17 01:04:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 334da541-05c5-3412-860b-0b9c3d2d6bc5 | -3.33317 | -52.77227 | 2024-11-17 01:04:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| d2c8f8ce-b4b9-30a0-b0f9-822b0baa2dc2 | -2.22615 | -53.6133 | 2024-11-17 01:04:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 68db2234-431f-385c-8945-11d932984196 | -1.22949 | -47.36161 | 2024-11-17 01:04:00 | TERRA_M-M | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| dbfc49b4-8e0b-3fee-92b1-522ee7aa9d8e | -4.48551 | -48.10678 | 2024-11-17 01:04:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| c849a47d-4c5b-3e88-81ef-21c5b4ac8b20 | -1.56287 | -52.29 | 2024-11-17 01:04:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 705dc4d7-b1bc-3ed0-bd52-09dab0b66a3d | -3.68441 | -49.0179 | 2024-11-17 01:04:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b00e5cfb-60b2-3398-a0d7-ee98fd06bd66 | -3.56568 | -51.65092 | 2024-11-17 01:04:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c955bb1d-32d2-3cfc-a32f-62ac74948c66 | -2.34794 | -47.46504 | 2024-11-17 01:04:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 94b717f4-9492-3826-a284-92a1ab97d700 | -3.84353 | -49.81943 | 2024-11-17 01:04:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 7f17e854-c107-399a-95ac-2e7442a60753 | -0.15449 | -51.50377 | 2024-11-17 01:04:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6050a3aa-bfa2-30d2-9bc8-282768bc85fa | -3.67181 | -50.10506 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| bc050a72-c66b-3160-900b-d7ef15d68c4d | -3.78326 | -46.0316 | 2024-11-17 01:04:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 29ca1dc9-75fa-35c5-9a9b-ad12343e7e62 | -3.86832 | -51.24163 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 37135c21-ce7a-34fe-9d45-9efc4873abda | -3.91371 | -46.5317 | 2024-11-17 01:04:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 38.0 |
| c87d26af-ec5b-373d-832b-ba3877cf544c | -3.82063 | -49.26319 | 2024-11-17 01:04:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4e389df9-4647-3646-b2b2-1c49fd617dcf | -3.95071 | -46.71304 | 2024-11-17 01:04:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 526ebfa8-48fc-3e07-b322-8c385a6a8f4a | -2.16714 | -48.34536 | 2024-11-17 01:04:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7d4802e4-bb86-38c6-bfb7-5be87f20425d | -2.20241 | -49.54558 | 2024-11-17 01:04:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 7b6dcdbd-599e-31e2-9974-7d339a9e7329 | -3.91427 | -46.52592 | 2024-11-17 01:04:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 6f55b7d7-5f38-3b78-bf91-cf140a2bcdb4 | -3.61384 | -47.52854 | 2024-11-17 01:04:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| f662075f-d03f-3435-9176-467b1998fdb4 | -0.80599 | -51.48631 | 2024-11-17 01:04:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bdcfb754-1fc9-340f-ac3d-a2bc43ca7bdb | -0.32533 | -48.70163 | 2024-11-17 01:04:00 | TERRA_M-M | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| ff8a4bb6-680e-377c-941d-92b86ff17cfc | -2.67172 | -46.19598 | 2024-11-17 01:04:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 61aaa529-da8a-3b50-9751-8e2869075f67 | -2.09262 | -48.39645 | 2024-11-17 01:04:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 6f7c4ced-ca3c-3bd7-be9d-b69a846e8290 | -4.74329 | -48.1173 | 2024-11-17 01:04:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 4fe7c40b-b4f6-31b8-ae60-4a444a2b97fa | -3.24477 | -53.51687 | 2024-11-17 01:04:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 198e5dac-3e1c-3a19-8529-9791972bb791 | -0.32322 | -51.52177 | 2024-11-17 01:04:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 592f4fbb-66e4-3456-971e-0819e53e21bd | -5.42711 | -44.30753 | 2024-11-17 01:04:00 | TERRA_M-M | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 60085348-52b6-349a-bf2f-635a85769d2e | -5.4953 | -46.25768 | 2024-11-17 01:04:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c5e04386-0567-31be-a21a-31bbddea2096 | -3.91165 | -46.51726 | 2024-11-17 01:04:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 1ca6c146-9d67-3f19-9317-de5aeaded7fa | -3.95653 | -49.96561 | 2024-11-17 01:04:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 451d1ff7-df8c-308b-b73a-a72be11b430f | -3.51929 | -49.93728 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 1ec788e4-cbd3-306c-be83-e96c2ec82c95 | -3.51826 | -50.25939 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b998e795-a5e6-3a2a-be68-81f6e8266b10 | -3.11608 | -45.07641 | 2024-11-17 01:04:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 2b877dd9-448d-3469-9182-395f7133776b | -4.25567 | -50.19735 | 2024-11-17 01:04:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 890b1fa5-792f-3904-ac00-8f820e12fd81 | -2.69089 | -54.23419 | 2024-11-17 01:04:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| fb14bfd0-ccbe-32ce-8a89-196634f4e99b | -2.83336 | -45.48248 | 2024-11-17 01:04:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 133.4 |
| d0ce816f-c5b5-3dfe-8f5f-2812ff4c59e1 | -0.00513 | -51.22381 | 2024-11-17 01:04:00 | TERRA_M-M | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c087df3d-2143-3684-ab0a-c087313c88da | 0.62012 | -51.76694 | 2024-11-17 01:04:00 | TERRA_M-M | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 13.5 |
| bfa882cc-86ef-3fee-8d7a-6f974a29a4fe | -5.42648 | -45.33955 | 2024-11-17 01:04:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 92a8763f-b2bd-3588-8faa-2a3dc90dba10 | -5.57831 | -44.88028 | 2024-11-17 01:04:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| ed4cb486-5a06-3823-a1fd-d6e66950c800 | -0.95122 | -51.7376 | 2024-11-17 01:04:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f59997a9-2200-36ab-8736-8266b2b380dc | -3.18716 | -53.24075 | 2024-11-17 01:04:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 2957b5df-b80c-3840-b362-745ad397b9af | -3.52469 | -50.24008 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 503938eb-dfbc-3eed-af56-1c3c73d1dd99 | -4.55397 | -48.01234 | 2024-11-17 01:04:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| f0739916-cc7a-38c5-a44d-94c551897060 | -4.66646 | -49.51325 | 2024-11-17 01:04:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9145f0af-7e64-3a6b-a068-3f6c39a3a5f9 | -3.72033 | -51.84032 | 2024-11-17 01:04:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 32c72810-6ecb-38e9-a9a7-6bf9d91edda7 | -3.66785 | -50.20741 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 22ad451a-6623-38fc-964e-8f0275c88475 | -2.20104 | -49.53584 | 2024-11-17 01:04:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 55b972d5-4601-3ac6-b4d7-1df3effd0870 | -3.58549 | -50.53665 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4727d2f8-d56e-36a4-91dc-a8e1ff927380 | -2.25652 | -50.45972 | 2024-11-17 01:04:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 53f72731-cd90-3408-a8d9-644dbed9d345 | -3.45118 | -49.12072 | 2024-11-17 01:04:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c5e4d009-a3ab-3e76-8e82-6ae28d29c97c | -0.78379 | -49.48452 | 2024-11-17 01:04:00 | TERRA_M-M | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 475d72b3-f301-3d4f-a057-94be4f3e2b6f | -2.9976 | -52.60629 | 2024-11-17 01:04:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 81d3bed5-8850-343c-8f11-cda55027caa6 | -0.93776 | -51.6409 | 2024-11-17 01:04:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5efb3749-3fbb-3df8-a363-2b0a0fd2ad36 | -3.71732 | -46.04796 | 2024-11-17 01:04:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 2aad40e6-46d6-3ef7-86bd-bb1d1d4b5639 | -3.58424 | -50.52775 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 0aa50cec-fd73-3797-90e9-1f65bd274740 | -0.90701 | -51.74383 | 2024-11-17 01:04:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 0350767d-6a9c-374c-aa3f-e1e00d4053f4 | -3.28448 | -45.60073 | 2024-11-17 01:04:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 97ea2851-7694-38e1-a0d1-bbc4c8994874 | -4.25205 | -49.19004 | 2024-11-17 01:04:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 415350d5-d513-315b-bfd2-47957b155e79 | -3.92274 | -46.51563 | 2024-11-17 01:04:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 70dcfb7e-246d-3f37-b6f8-0cc31d0499b2 | -3.28429 | -51.16003 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 031bfbf3-3d48-3f01-9c2a-8b89f7715739 | -2.34978 | -47.47783 | 2024-11-17 01:04:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e8b21a8f-fe2c-3226-af95-28fa03c91254 | -1.39352 | -51.99496 | 2024-11-17 01:04:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c42e13c8-8b95-3c83-b44d-a90bdd7f2beb | 0.61889 | -51.77576 | 2024-11-17 01:04:00 | TERRA_M-M | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 6ca90d05-1a62-3015-9b23-abf53816e62b | -4.00283 | -53.74208 | 2024-11-17 01:04:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| de93429b-a86f-39e0-9f01-0105005f28e3 | -5.59175 | -45.21594 | 2024-11-17 01:04:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 38.5 |


[Clique aqui para ver as próximas entradas](README15.md)
