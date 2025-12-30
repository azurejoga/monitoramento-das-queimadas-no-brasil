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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45a2ad15-5d2e-3ed3-8a25-86121819fb8b | -15.13217 | -52.94396 | 2025-12-30 05:05:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6f4a2cd6-adad-30bb-8e86-8b77641ca5a6 | -15.3675 | -53.0392 | 2025-12-30 05:05:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 37bdc085-a54a-32f1-9e9d-cfc232499bff | -15.12055 | -52.94674 | 2025-12-30 05:05:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe9e1dc6-19ba-3ba7-89df-30295258117d | -15.71809 | -58.00035 | 2025-12-30 05:05:00 | NPP-375D | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8634ffb-c3c5-308c-a624-524218f881d4 | -15.67695 | -59.18347 | 2025-12-30 05:05:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7ddd5542-7e9a-3acb-8abf-3e0e7561e044 | -15.71532 | -57.99603 | 2025-12-30 05:05:00 | NPP-375D | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7b0b44c-3027-3936-9f75-010d19d2a381 | -23.26686 | -51.03241 | 2025-12-30 05:08:00 | NPP-375D | IBIPORÃ | PARANÁ | Brasil | 4109807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 837a9d59-a37d-334d-8e14-5f9fd25a2954 | -21.25417 | -48.65432 | 2025-12-30 05:08:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f0a53724-88c1-3e5f-bbd2-c43607b63fc8 | -24.54363 | -50.72844 | 2025-12-30 05:08:00 | NPP-375D | IMBAÚ | PARANÁ | Brasil | 4110078 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 60fd95cc-a258-3b4d-afb4-2da3daf6d94e | -23.6948 | -49.52547 | 2025-12-30 05:08:00 | NPP-375D | ITAPORANGA | SÃO PAULO | Brasil | 3522802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 74e6637d-a4d1-3682-b852-e0672955ec9c | -23.26713 | -51.03069 | 2025-12-30 05:08:00 | NPP-375D | IBIPORÃ | PARANÁ | Brasil | 4109807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f9f3d69c-30b8-3c86-b4ec-1e00ad8e323e | -24.54305 | -50.73389 | 2025-12-30 05:08:00 | NPP-375D | IMBAÚ | PARANÁ | Brasil | 4110078 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| b8037fca-52f6-358b-9025-620a30eb851a | -21.25971 | -48.65177 | 2025-12-30 05:08:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 049d0feb-8047-3a1d-8e07-af5f5e605677 | -10.027 | -36.2699 | 2025-12-30 05:10:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 75.1 |
| c9ae8dd1-d14b-3c4c-a894-bb8384d57196 | -10.0463 | -36.2664 | 2025-12-30 05:10:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 125.8 |
| 806dfef8-6534-3382-af3c-cbb97faf698a | -10.027 | -36.2699 | 2025-12-30 05:20:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 56.0 |
| dd743ce4-868d-31d3-b944-6fff8aaade23 | -10.0463 | -36.2664 | 2025-12-30 05:20:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 80.5 |
| 118ffcf4-b84d-39e9-9f62-de624644b4be | -2.37344 | -55.86726 | 2025-12-30 05:22:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af4a579b-3a16-38fc-a2b7-a6967d524cfc | -1.47945 | -54.20112 | 2025-12-30 05:22:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ba6cee79-ca35-3794-a3e2-9a19b64aaa0d | -7.70645 | -55.21107 | 2025-12-30 05:22:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38659988-ca8a-32ef-9470-d5b4c05c1f50 | -15.72325 | -57.99465 | 2025-12-30 05:25:00 | NOAA-20 | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9d513fa-515e-310f-a070-3582492b9348 | -12.42751 | -64.1384 | 2025-12-30 05:25:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb7781c9-9c1f-3a21-a825-d6d3cd1a8f3e | -15.81523 | -59.23358 | 2025-12-30 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0cde781d-17ab-39bb-8470-3a2b91502c5f | -15.50647 | -59.39246 | 2025-12-30 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8fc57c5c-b9ab-3cbc-a57c-e12350e12743 | -12.36628 | -64.01842 | 2025-12-30 05:25:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb8b34b5-0a19-3515-8938-fcb6870eb9d5 | -12.3671 | -64.01495 | 2025-12-30 05:25:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c7ffdbd7-2c3b-387a-b581-0427fe5438e9 | -13.99757 | -56.57495 | 2025-12-30 05:25:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c042d28a-d0b8-3a71-a417-ac2e766c62ab | -12.36648 | -64.01876 | 2025-12-30 05:25:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 146e58b7-3b3a-3dae-90fb-76b937ce6b6c | -9.87795 | -62.63229 | 2025-12-30 05:25:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 317985db-e567-3c16-8658-faf0fd9712a0 | -16.59225 | -58.21287 | 2025-12-30 05:25:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| bd2c90eb-7851-3ef1-ae81-9907218d7c49 | -12.36692 | -64.01462 | 2025-12-30 05:25:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d40eac40-2c67-3675-bf47-9b59b54671a2 | -15.71858 | -57.99932 | 2025-12-30 05:25:00 | NOAA-20 | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64ad37b3-e541-34f1-aa66-fb4bdcefcb25 | -12.42813 | -64.1346 | 2025-12-30 05:25:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61cf7d69-5b24-3688-a900-d7fa0dbef6d7 | -15.82708 | -58.8091 | 2025-12-30 05:25:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ebcc8bb6-4b83-329a-b94c-995a5059a47d | -18.82074 | -51.61394 | 2025-12-30 05:27:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 29430de8-9bd8-3ee7-afa7-c8dafe7056c4 | -18.82123 | -51.6088 | 2025-12-30 05:27:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 6e517ee4-69bc-32f1-869b-b93b89b3375b | -18.82698 | -51.6146 | 2025-12-30 05:27:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c76368e-8b1b-3b98-b310-c5e6621ee5b5 | -10.027 | -36.2699 | 2025-12-30 05:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 71.0 |
| c2d6debe-49f1-3b2d-91a4-b718335a327f | -10.0463 | -36.2664 | 2025-12-30 05:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 91.3 |
| cc97efd4-37af-3537-8c69-ace0a312d61d | -10.0463 | -36.2664 | 2025-12-30 05:40:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 76.2 |
| aba91f01-bd57-31c4-8364-37491d8fd241 | -6.23199 | -40.2966 | 2025-12-30 05:40:00 | AQUA_M-M | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| fba65f27-f770-396f-8b6e-5aa2061fcf23 | -4.34464 | -44.11766 | 2025-12-30 05:40:00 | AQUA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| a6c6bd06-c823-3d87-bb11-e1d3d4898276 | -10.03655 | -36.27566 | 2025-12-30 05:40:00 | AQUA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 45.9 |
| 902af98f-2ba5-39be-887b-19dbfff34d24 | -3.53824 | -43.60006 | 2025-12-30 05:40:00 | AQUA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 554d567b-1824-3779-8eee-2e0a7014bab7 | -4.89756 | -38.92158 | 2025-12-30 05:40:00 | AQUA_M-M | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 7ff95c0f-73b8-3b0b-b862-6c4ce715c3ed | -4.3434 | -44.12306 | 2025-12-30 05:40:00 | AQUA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b5d9807a-9434-3883-9f55-0d016bd77ba7 | -10.03836 | -36.26274 | 2025-12-30 05:40:00 | AQUA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 142.4 |
| 31fd30c5-a457-3bb7-b38d-8c84f91b0222 | -13.47609 | -44.01955 | 2025-12-30 05:42:00 | AQUA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 63e2b037-88a1-3b60-b6c0-ced159870235 | -15.13019 | -45.27979 | 2025-12-30 05:42:00 | AQUA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ccac6980-00d7-38f2-bf47-cd5b9009da81 | -15.53617 | -42.94038 | 2025-12-30 05:42:00 | AQUA_M-M | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cf1490fb-2952-30ff-9d74-2e1250a5ec26 | -12.66063 | -46.75372 | 2025-12-30 05:42:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| b100af18-6dce-3cee-bfc9-613396665e86 | -13.46818 | -44.00694 | 2025-12-30 05:42:00 | AQUA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 0e4aa94d-7cc4-3d05-aaa2-b508de62fea7 | -13.46638 | -44.01801 | 2025-12-30 05:42:00 | AQUA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e5311d44-d916-3008-88ee-b2cf7aa2121f | -13.47788 | -44.0085 | 2025-12-30 05:42:00 | AQUA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f55a24c3-4ddf-3b42-b0dd-4af1d892386f | -12.37048 | -64.01511 | 2025-12-30 06:16:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92d76ebd-179e-3be4-a91d-ef10d94612b7 | -12.36462 | -64.01433 | 2025-12-30 06:16:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ece274bb-f087-339d-9014-12e6f257c438 | -2.71193 | -42.74763 | 2025-12-30 11:53:00 | TERRA_M-M | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| eac66a36-ecf5-3105-8658-2f69d1cea2bf | -2.42925 | -44.89378 | 2025-12-30 11:53:00 | TERRA_M-M | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 1fe75a69-b5d2-3cb2-8bb7-5cf402058624 | -2.91263 | -41.92532 | 2025-12-30 11:53:00 | TERRA_M-M | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 40.1 |
| ceaf7453-ddba-35a8-a97b-3543ed0d1a94 | -4.67471 | -39.77908 | 2025-12-30 11:55:00 | TERRA_M-M | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 1e4f1885-1098-3776-b627-bf67f7b65c7e | -3.90024 | -42.55661 | 2025-12-30 11:55:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 103.4 |
| 7144451e-906b-3cf4-be35-0afc5abc3ff3 | -3.89897 | -42.56543 | 2025-12-30 11:55:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| ec15aefd-e827-3c87-8ad8-4d803a783e80 | -6.36697 | -38.15852 | 2025-12-30 11:55:00 | TERRA_M-M | MARCELINO VIEIRA | RIO GRANDE DO NORTE | Brasil | 2407302 | 24 | 33 | nan | nan | nan | Caatinga | 22.2 |
| 55259f00-8ea5-3caf-9f85-fd83436bd03a | -6.62989 | -39.29449 | 2025-12-30 11:55:00 | TERRA_M-M | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 22.7 |
| 1669c3a7-b679-3083-a343-a5c6f6653be4 | -4.3492 | -44.12234 | 2025-12-30 11:55:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 9ad247ec-468a-3fa7-844f-159316b7607a | -6.31702 | -39.87769 | 2025-12-30 11:55:00 | TERRA_M-M | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 89e9b420-a1cf-315b-a76a-64f5c167a406 | -6.23762 | -40.29979 | 2025-12-30 11:55:00 | TERRA_M-M | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 10.0 |
| d7d7ce9b-b0d4-3254-aaa9-dc88a0c04fbb | -4.1031 | -40.49177 | 2025-12-30 11:55:00 | TERRA_M-M | VARJOTA | CEARÁ | Brasil | 2313955 | 23 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 36c80852-de20-39c0-a196-3a90bff23b47 | -6.71827 | -38.03559 | 2025-12-30 11:55:00 | TERRA_M-M | APARECIDA | PARAÍBA | Brasil | 2500775 | 25 | 33 | nan | nan | nan | Caatinga | 21.8 |
| 179d3a1d-8ce3-3449-947d-87344c7f6629 | -4.49363 | -40.50135 | 2025-12-30 11:55:00 | TERRA_M-M | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 1671a8bd-7c22-3c6b-ad67-53833216077c | -3.89139 | -42.55538 | 2025-12-30 11:55:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 73.5 |
| 6ec9e69d-c9f6-3f94-84ab-1612f71d14ae | -4.03231 | -45.64683 | 2025-12-30 11:55:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 31.6 |
| a60fcfc2-42c8-33e7-b92b-544d918d8e3c | -3.41532 | -41.88811 | 2025-12-30 11:55:00 | TERRA_M-M | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 179fff9f-9a21-31c4-9b69-135ec2473025 | -6.15777 | -39.06104 | 2025-12-30 11:55:00 | TERRA_M-M | QUIXELÔ | CEARÁ | Brasil | 2311355 | 23 | 33 | nan | nan | nan | Caatinga | 14.5 |
| f2f55994-e77d-3721-ab56-00e12fdd1094 | -3.55665 | -43.60136 | 2025-12-30 11:55:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7d4ef1bf-4341-3416-9286-7a9942df7dcb | -3.53441 | -42.15528 | 2025-12-30 11:55:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| b0d88037-b9eb-3d5b-9ea3-03835d2f2165 | -6.32425 | -39.88444 | 2025-12-30 11:55:00 | TERRA_M-M | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 1e4481a0-4c30-3841-8e35-ad683e9a6b4c | -3.95391 | -42.05494 | 2025-12-30 11:55:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 3ac4f5d0-07da-38b2-83d1-a2102e7f8ebd | -6.64069 | -39.29603 | 2025-12-30 11:55:00 | TERRA_M-M | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 15.3 |
| cd253047-71d2-32b2-9e66-bf30957804ef | -7.4031 | -38.73896 | 2025-12-30 11:55:00 | TERRA_M-M | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 16.5 |
| d03cbf6e-9ffc-3526-ac6f-243d3083a6e6 | -5.8995 | -38.2311 | 2025-12-30 11:55:00 | TERRA_M-M | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 13a2bb6b-6269-3e16-aff8-8c09bc2ffbc5 | -3.96552 | -41.97356 | 2025-12-30 11:55:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| f975a4df-189d-3c5c-84a6-e9b3d55f183a | -6.32587 | -39.8723 | 2025-12-30 11:55:00 | TERRA_M-M | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 9.4 |
| a55d361c-f9fa-317c-8b8e-d88185bb32bb | -4.34025 | -44.12107 | 2025-12-30 11:55:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3249fdaf-17a3-38c9-aba2-652dc0f7bbde | -11.74712 | -43.31685 | 2025-12-30 11:57:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 16d65ece-9bb2-3fbc-96c8-5f2ef6c2ebd0 | -8.30485 | -39.47636 | 2025-12-30 11:57:00 | TERRA_M-M | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 20aea049-639a-3ace-8d32-b1b020229753 | -11.75748 | -43.30869 | 2025-12-30 11:57:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 1b4f6f36-0f6e-3d43-ac11-812c43427b20 | -11.77938 | -44.19928 | 2025-12-30 11:57:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| d0b6dcbc-7392-3635-abf4-b782697f13fc | -10.26538 | -43.96699 | 2025-12-30 11:57:00 | TERRA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e66cedac-1a6e-339c-b471-25b748b1ad3c | -12.08695 | -43.52312 | 2025-12-30 11:57:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 47508641-c82d-36d6-b6b1-eb5040dc1446 | -13.66882 | -43.06387 | 2025-12-30 11:57:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 725334ad-846f-3cc3-8f1d-b7bc9b384a22 | -11.00495 | -44.332 | 2025-12-30 11:57:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 58f07110-064e-3d62-a4bd-39fdefa24671 | -8.15444 | -37.34762 | 2025-12-30 11:57:00 | TERRA_M-M | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 0c4d220c-264e-3c64-968f-ab7ca9877544 | -11.75618 | -43.31812 | 2025-12-30 11:57:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 1f2e7e4a-9245-34df-a1a3-d6ff7dbb4c48 | -13.95938 | -42.88398 | 2025-12-30 11:57:00 | TERRA_M-M | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 8894006e-d08e-3725-a07d-c76c16070139 | -14.35008 | -42.85653 | 2025-12-30 11:57:00 | TERRA_M-M | CANDIBA | BAHIA | Brasil | 2906600 | 29 | 33 | nan | nan | nan | Caatinga | 25.8 |
| 77adf052-acbb-360c-b980-9ee4efa3552e | -11.15631 | -43.45732 | 2025-12-30 11:57:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 3445190c-4638-3155-9212-cec977d407dd | -11.82742 | -46.58534 | 2025-12-30 11:57:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 37ff3a01-1947-3837-a69d-eb7d31d213d6 | -11.76698 | -44.61608 | 2025-12-30 11:57:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| eedd0b1c-bbf5-3549-beea-ffddf93ebc3b | -14.2204 | -43.46692 | 2025-12-30 11:57:00 | TERRA_M-M | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |


[Clique aqui para ver as próximas entradas](README10.md)
