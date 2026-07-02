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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d0b001e-8815-30a8-96e2-79f239966aaa | -10.9593 | -43.0326 | 2026-07-02 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 8f381101-6324-357e-b18c-9a6463a17618 | -5.8058 | -43.7975 | 2026-07-02 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| e5bec378-942a-3c58-b3f1-73f67cdf4a4b | -3.5043 | -48.039 | 2026-07-02 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 2d1ffa4e-8915-36c7-aa66-ad14dd0b7ec6 | -10.9397 | -43.0593 | 2026-07-02 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 0a8dc177-5440-3c8b-96b0-f4d7de34bec9 | -21.7622 | -56.2795 | 2026-07-02 00:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 99.3 |
| ec1ec1d5-6509-3414-b3b5-78056ed9bc3a | -11.8007 | -57.0032 | 2026-07-02 00:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 08903e59-9560-31ab-8588-19f3037b636f | -10.9588 | -43.0565 | 2026-07-02 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 0b434357-e7f7-3de0-85ec-a6af3c691962 | -9.1933 | -45.3114 | 2026-07-02 00:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 49.6 |
| aa1bbcbc-8e8e-3c3f-a878-99f4e18b182b | -4.0046 | -48.0618 | 2026-07-02 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| c9b8e87b-3de9-308e-afb0-d1bb3eed07fb | -9.2123 | -45.3092 | 2026-07-02 00:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 943006fa-a6a6-3e20-af60-e40564af7057 | -12.5135 | -48.2802 | 2026-07-02 00:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 55aa680e-87d6-31dd-a682-2f9e0e88db13 | -10.9401 | -43.0355 | 2026-07-02 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| f57863f4-057c-3218-ad41-12777c27646c | -8.7208 | -48.3441 | 2026-07-02 00:00:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 44f6368b-8f9d-376e-ba88-7e80b81b8872 | -11.4149 | -56.0525 | 2026-07-02 00:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 09282379-53ab-3795-adc9-ce70accc2768 | -11.4147 | -56.0726 | 2026-07-02 00:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| ca8af1cc-933c-3166-a1ed-7a26fb2009a4 | -21.7823 | -56.2976 | 2026-07-02 00:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 8851aa3c-9198-3786-a13d-53a562c04c33 | -21.7827 | -56.2762 | 2026-07-02 00:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 117.4 |
| d14cfe04-c1f6-36c1-9963-55d7e6295e1d | -21.7617 | -56.301 | 2026-07-02 00:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 104.3 |
| f12c45f5-3df0-35b2-ae27-112028af5754 | -3.5228 | -48.0383 | 2026-07-02 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| a417762c-404f-3f60-8b5c-8fe03fccd309 | -7.00722 | -42.76776 | 2026-07-02 00:01:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| c10db391-cf42-3a33-ba92-acb8e9b0a393 | -11.1691 | -50.08807 | 2026-07-02 00:01:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| c0fde67a-d59a-3463-bc90-b6353f2dd0c9 | -9.2017 | -45.32846 | 2026-07-02 00:01:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 99855de2-bec8-31de-b26f-e387c13c458a | -12.52067 | -48.28658 | 2026-07-02 00:01:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 45.7 |
| b1ab5989-c3bb-3133-b802-f73b97b89401 | -7.98243 | -44.54328 | 2026-07-02 00:01:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 8738f91b-c450-3ebf-b4c0-1d2645ee3839 | -13.2934 | -43.55204 | 2026-07-02 00:01:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e398adcc-6b05-3975-9fd9-9e2d1324da45 | -8.65257 | -49.70764 | 2026-07-02 00:01:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| bb828181-9739-3b0d-9694-d648b6867737 | -9.27898 | -50.21422 | 2026-07-02 00:01:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 703f9d48-5d16-3f39-a854-b64ae0cd656d | -7.09342 | -46.50823 | 2026-07-02 00:01:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| b5c356cd-5bc8-3c84-bab7-b150c0773a12 | -9.76059 | -47.87724 | 2026-07-02 00:01:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ecf60ebb-fefb-39dc-a618-417d7ccd62d4 | -10.81007 | -49.33964 | 2026-07-02 00:01:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| e888c8c6-7477-3ece-9299-5fa9f55f7b14 | -12.85033 | -44.36477 | 2026-07-02 00:01:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 96c262af-c3d9-31e1-9460-e5d0f6bb15f3 | -11.00233 | -47.18782 | 2026-07-02 00:01:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 5764c74d-a82c-3898-9f51-8b26c2648bb2 | -10.94251 | -43.0509 | 2026-07-02 00:01:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 220.5 |
| 630576f4-1ac7-34d2-9f2e-042073cf3f8f | -12.74638 | -44.48157 | 2026-07-02 00:01:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 980.1 |
| 005394fc-1d80-3045-b78e-ac91b2beddfd | -11.42298 | -56.04702 | 2026-07-02 00:01:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| e8a2f381-3ac3-3c35-af65-a65b9e999dc1 | -12.74488 | -44.4714 | 2026-07-02 00:01:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7806d35b-d5ae-34d0-b8a7-e85e96672dc9 | -11.41682 | -56.08556 | 2026-07-02 00:01:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| f5405582-dca9-3491-af8a-e6f73285b35a | -12.85823 | -44.353 | 2026-07-02 00:01:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1101.3 |
| 300589c9-646e-313a-a84c-8785dc621139 | -12.76509 | -44.47866 | 2026-07-02 00:01:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| a356127f-6905-3e14-a74d-36c093e8318c | -12.86763 | -44.35151 | 2026-07-02 00:01:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1214.2 |
| dc1a4a8f-72ec-30dc-946b-25a657aa79fc | -9.22035 | -45.32563 | 2026-07-02 00:01:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| bc86af89-4ec7-332e-879a-f832e306cdc1 | -12.75871 | -44.50044 | 2026-07-02 00:01:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 10ae666c-9a0a-37f0-a9f2-d8a7499ea4e4 | -11.50391 | -47.42432 | 2026-07-02 00:01:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6af34614-b91f-3621-a80a-21e94e38c836 | -8.71837 | -48.3363 | 2026-07-02 00:01:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 08069e13-7d39-36b1-bf11-2a1cabc65487 | -11.78859 | -57.00005 | 2026-07-02 00:01:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 15b7625d-2ba3-38a1-b3d2-0eacbd88d752 | -7.54114 | -49.50247 | 2026-07-02 00:01:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 442d93b5-87fc-3748-9e12-44c5873f40c9 | -11.41049 | -49.00847 | 2026-07-02 00:01:00 | TERRA_M-M | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| ba6b6179-f067-35ff-880f-52d166fd749d | -12.51941 | -48.27695 | 2026-07-02 00:01:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 3576426a-dd23-3114-ae5f-e3a00e7f1341 | -9.97471 | -54.43439 | 2026-07-02 00:01:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 080a6f19-22c8-3603-8cc9-29cbe2a1ae66 | -10.51427 | -51.94263 | 2026-07-02 00:01:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 23.4 |
| fc6e7b71-c44c-31c6-b27e-d16258bdb6b3 | -11.41319 | -56.05317 | 2026-07-02 00:01:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 027a7f56-6fd8-3027-b9d7-72fbf8e9ea72 | -12.84543 | -44.397 | 2026-07-02 00:01:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 043cbaac-10f3-3d5b-bedf-f26daadc787f | -9.21102 | -45.32705 | 2026-07-02 00:01:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 33.0 |
| bce2eded-d3fd-30b9-aa88-a009b74ec583 | -10.12165 | -52.09965 | 2026-07-02 00:01:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 62e9f0c9-6e48-3d99-a6c4-d4791668c2fb | -10.38006 | -46.68451 | 2026-07-02 00:01:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 6db08baf-ed6f-3c76-b671-d48d91a71070 | -9.96615 | -47.75638 | 2026-07-02 00:01:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 26c42852-3362-3fe9-adf5-281bedd47ba8 | -12.5103 | -48.27824 | 2026-07-02 00:01:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| fb599033-1baa-39fd-aa98-a0932fa72156 | -8.65006 | -47.77091 | 2026-07-02 00:01:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3f4e1efd-af20-3895-9a84-0f5c2fcaa526 | -9.74228 | -49.03364 | 2026-07-02 00:01:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| f3525720-86f2-357d-95d8-b8fb0c517340 | -10.84124 | -45.06293 | 2026-07-02 00:01:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 29397f2f-dae9-3c69-ae66-2dd8f6cdcae0 | -9.95851 | -47.76664 | 2026-07-02 00:01:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f10032b9-8ccd-3b39-ad77-bdf0290d3a47 | -8.87549 | -50.18863 | 2026-07-02 00:01:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 3fd8e88d-0785-3608-a662-1a6f30e5305f | -10.95501 | -43.06218 | 2026-07-02 00:01:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 39.2 |
| acda8291-56c7-319e-bb3a-0a2753a61584 | -10.78339 | -53.54587 | 2026-07-02 00:01:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| d57753b6-54dc-33a0-8297-9b85a2e266c4 | -11.916 | -43.38322 | 2026-07-02 00:01:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| bed67871-5df5-3c75-ad1e-7aa6281173ff | -12.86613 | -44.34117 | 2026-07-02 00:01:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 632.3 |
| c813e75a-8d05-3063-8f3e-8c0cf21b58c0 | -12.76806 | -44.49898 | 2026-07-02 00:01:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 124.3 |
| da611d0c-4351-31f4-b378-835c26f53ff9 | -12.73852 | -44.49318 | 2026-07-02 00:01:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 0379ff82-e373-3f80-ac31-8e7fcd85ff61 | -12.84092 | -44.36623 | 2026-07-02 00:01:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 3c955af9-6726-31ae-bb42-985d1ce95927 | -7.95278 | -49.27905 | 2026-07-02 00:01:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| f19bc676-2789-3b39-9516-253c63716daa | -10.94049 | -43.03791 | 2026-07-02 00:01:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.5 |
| faa77190-81ce-3e90-8d59-4366cf5e2051 | -9.18333 | -49.66642 | 2026-07-02 00:01:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a71bb9ba-7f4f-3d31-9920-374fe9e50c90 | -12.51155 | -48.28785 | 2026-07-02 00:01:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 3a9637fd-aad7-3b67-bffd-8f3eaa6ede28 | -7.29031 | -49.27499 | 2026-07-02 00:01:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fb5617af-4fc6-3000-b102-8987c4347429 | -9.15842 | -47.23846 | 2026-07-02 00:01:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| fd25a766-afaa-392e-97d3-f10c14fb089f | -7.95153 | -49.26954 | 2026-07-02 00:01:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1ca5db1b-3ac0-389a-9d47-f24441fda49a | -12.84882 | -44.35447 | 2026-07-02 00:01:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 690.2 |
| 9c026601-9804-3b6f-a42a-ccc76756f550 | -12.53106 | -48.29493 | 2026-07-02 00:01:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 68d3b675-3a34-3ff5-a859-668d8a2518af | -10.37881 | -46.67552 | 2026-07-02 00:01:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| b5fce8db-e7f6-3d1f-bd7f-174b85738443 | -7.00951 | -42.7833 | 2026-07-02 00:01:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 19.9 |
| acf8aaa2-cb61-3e63-86bd-9a887a909516 | -8.66326 | -49.71641 | 2026-07-02 00:01:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 484ba2a4-00d1-37ed-a12e-7d946b436856 | -12.61794 | -44.66856 | 2026-07-02 00:01:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 12017876-ff8d-38a6-a744-fce3b6c8a67d | -9.19093 | -45.31985 | 2026-07-02 00:01:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 4bd167fa-c771-330f-a365-031ec259e66e | -12.75573 | -44.48012 | 2026-07-02 00:01:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 372.9 |
| 19e9fba5-b076-3286-bc63-0dbc9da69792 | -11.91782 | -43.3951 | 2026-07-02 00:01:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 529da22e-7129-387c-a3a9-4e55e7ce1b66 | -6.93014 | -43.72126 | 2026-07-02 00:01:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 7db8ba99-809d-396a-847a-8a65dc6a7a6b | -11.4079 | -48.9884 | 2026-07-02 00:01:00 | TERRA_M-M | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a1584880-37a6-3297-82fd-573b1f7274be | -12.84732 | -44.34417 | 2026-07-02 00:01:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 315.0 |
| 4f79d80e-adb4-389a-b62d-46a8f706261b | -8.65389 | -49.71774 | 2026-07-02 00:01:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| feca6ac5-1824-3d3f-bc65-0ff12fc4e79a | -11.40352 | -49.00553 | 2026-07-02 00:01:00 | TERRA_M-M | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 73a71146-a138-3b11-9f2c-08706c857f1d | -10.69979 | -49.60947 | 2026-07-02 00:01:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| edc0310b-0323-3bc8-b53f-d28844238868 | -7.50748 | -45.85607 | 2026-07-02 00:01:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f5e02182-5950-32a9-9a70-8eb623ca533f | -7.10246 | -46.50696 | 2026-07-02 00:01:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 4c77982c-de49-3145-b7df-2f55743cf1db | -8.7196 | -48.34532 | 2026-07-02 00:01:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| e82ae542-f268-334f-9b87-8049749f6387 | -7.09472 | -46.51754 | 2026-07-02 00:01:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a398b793-093c-3e71-9a82-1eaf098aeff3 | -11.40485 | -49.01549 | 2026-07-02 00:01:00 | TERRA_M-M | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 70e6f08d-cab5-3506-b004-fa665adecfa3 | -11.42644 | -56.07976 | 2026-07-02 00:01:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| f9d566e2-9e47-36fb-af55-4a0acc3758b0 | -8.31607 | -45.37756 | 2026-07-02 00:01:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 4dff5788-4094-3196-b917-84518dd40eca | -11.79176 | -56.99268 | 2026-07-02 00:01:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| de97abab-5d23-3b77-b088-4d6555618ca6 | -12.5298 | -48.28531 | 2026-07-02 00:01:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |


[Clique aqui para ver as próximas entradas](README2.md)
