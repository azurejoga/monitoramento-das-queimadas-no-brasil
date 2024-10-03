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

## Dados Diários - Página 210

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3dcff0c-ebc1-354d-bcaf-ad1cad8aacb9 | -10.6978 | -46.1514 | 2024-10-03 11:56:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 447923f8-6bbb-3d2d-bbee-b2eaa4dcf09f | -10.7168 | -46.1489 | 2024-10-03 11:56:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 196.6 |
| 3b9c580f-c923-374d-a428-e4193eafa1e2 | -11.0345 | -46.5143 | 2024-10-03 11:56:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 7a603bca-05fd-3d64-8bb3-3d2401f874bb | -11.2758 | -46.9098 | 2024-10-03 11:56:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| df596772-297d-35a3-9290-8957238dad64 | -11.2563 | -46.9348 | 2024-10-03 11:56:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| cb113e10-a111-3014-be54-987dc6f707ab | -13.0017 | -44.7357 | 2024-10-03 11:56:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| d462f36c-668b-3371-981e-48c11bb68505 | -13.0021 | -44.7123 | 2024-10-03 11:56:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| bdf049f5-eab6-3e3a-80e8-dcf59475d786 | -13.1805 | -45.4489 | 2024-10-03 11:56:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| e213ba25-59e2-3716-8b8b-caea3c263ae5 | -13.0594 | -51.1409 | 2024-10-03 11:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 4831765a-7948-36e4-95d2-583c91624a33 | -13.1976 | -48.6489 | 2024-10-03 11:56:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 75.0 |
| a6fb4934-6675-3b70-b244-591b89563f8e | -13.0591 | -51.1623 | 2024-10-03 11:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| a5265e59-f3af-3ed6-a43c-dcd276bb9c08 | -13.0402 | -51.1432 | 2024-10-03 11:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.2 |
| ffc843bd-928f-327f-9c1c-4db8d17e2b70 | -11.27 | -46.95 | 2024-10-03 12:04:21 | MSG-03 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2597fde7-63c5-3e07-b0bb-61626e90cd3e | -8.2399 | -49.3812 | 2024-10-03 12:05:53 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 9000801c-a131-3d50-b480-043bb62547b7 | -8.2587 | -49.3796 | 2024-10-03 12:05:53 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 8a85191d-f6c8-3ce9-a5ca-17aed892c8ed | -8.7225 | -45.204 | 2024-10-03 12:05:55 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 1b44c27e-bbc8-3a35-ab82-d600fac161c4 | -8.6113 | -46.5243 | 2024-10-03 12:05:55 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 9d0cda11-7c0c-3901-9699-b890b5ea6d96 | -8.9244 | -45.6367 | 2024-10-03 12:05:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 255.3 |
| 74d5435b-dafa-32e0-91d2-c7d130212039 | -11.0345 | -46.5143 | 2024-10-03 12:06:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 21b1f958-73ac-31b7-b3da-ff116876e2fd | -13.1805 | -45.4489 | 2024-10-03 12:06:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 02d37928-7ac6-3040-9ff7-de20eab03367 | -13.0594 | -51.1409 | 2024-10-03 12:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 147.7 |
| e5048610-a924-3a3e-85d5-4761432df8f4 | -13.1976 | -48.6489 | 2024-10-03 12:06:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 71.6 |
| adb21ae2-d88a-31b6-b8b3-3cd89c01b667 | -13.0591 | -51.1623 | 2024-10-03 12:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 08aee9ce-b8ef-3491-9ffb-6466b8648bef | -13.0402 | -51.1432 | 2024-10-03 12:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.5 |
| a058611a-0d6c-33a1-a213-62f0c4d28ab6 | -13.1927 | -51.1883 | 2024-10-03 12:06:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 4adf17e7-85b6-3480-9afc-59aa6ad4658b | -13.1924 | -51.2097 | 2024-10-03 12:06:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 922e43df-0e0d-3539-9bbd-54fd8698edd2 | -8.2587 | -49.3796 | 2024-10-03 12:15:53 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 36eff1f2-82ba-3341-96b5-fbfa4989f0a5 | -8.7225 | -45.204 | 2024-10-03 12:15:55 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 148.5 |
| b6966baa-5975-359a-a74c-1a61d15dc3ba | -8.7228 | -45.1812 | 2024-10-03 12:15:55 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 507d1c42-7d70-3061-807c-6d6e4d87ffeb | -8.9055 | -45.6387 | 2024-10-03 12:15:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 0072b98e-4a60-3d6d-b38d-3340a5d38562 | -8.9244 | -45.6367 | 2024-10-03 12:15:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 202.0 |
| a1228974-ba5f-3477-b67b-072fdf9fda7f | -8.9433 | -45.6346 | 2024-10-03 12:15:57 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.4 |
| cacc19d6-66f2-3960-a577-efc44cd4799a | -9.3833 | -68.3256 | 2024-10-03 12:16:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 56.9 |
| d765c3f4-1648-3318-9e5c-c0f7f13c23e4 | -10.2195 | -47.6839 | 2024-10-03 12:16:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| c834f694-c028-3c9e-b7b6-2c1dd2b1c77e | -10.2381 | -47.7038 | 2024-10-03 12:16:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 93844819-1216-3c45-a490-e87f3e9c98d0 | -10.6978 | -46.1514 | 2024-10-03 12:16:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 58151a4b-59f9-351d-a0c4-fb1ed45a9da6 | -10.7165 | -46.1716 | 2024-10-03 12:16:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 840d14a5-4c23-3d3a-ac21-8cd2af891c8a | -10.5736 | -48.0839 | 2024-10-03 12:16:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| b1f05377-ea7b-3853-993e-8060238b464b | -10.7168 | -46.1489 | 2024-10-03 12:16:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 298.6 |
| c6a4b5ab-4bbd-354c-8306-4c03d1cc1ad7 | -10.7459 | -47.9757 | 2024-10-03 12:16:07 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| cf517341-6cee-35d6-aeb9-219adb0b72fd | -10.7352 | -46.1918 | 2024-10-03 12:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 403257f0-4aa9-32c2-ae1a-f2c741ae4951 | -11.0345 | -46.5143 | 2024-10-03 12:16:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| b2c3baa1-37f2-357c-bd9f-c3f357639858 | -11.158 | -49.6289 | 2024-10-03 12:16:09 | GOES-16 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 6751dacd-e18b-355c-946d-49368f53b75a | -11.2783 | -43.388 | 2024-10-03 12:16:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 747320c2-65e1-3810-984b-db8aa145463e | -11.1579 | -45.9551 | 2024-10-03 12:16:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 8bf8a4f4-535a-3afb-afef-fe84d56ff7c7 | -11.2758 | -46.9098 | 2024-10-03 12:16:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| ef7d9b43-89cd-397a-a2a6-3cd3a64331b4 | -12.762 | -50.5997 | 2024-10-03 12:16:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| a17247ba-61a5-3cfa-a670-817b4e76b6f9 | -13.0021 | -44.7123 | 2024-10-03 12:16:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 129.0 |
| e67cef0b-5504-3466-bc92-c62846718788 | -13.0017 | -44.7357 | 2024-10-03 12:16:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 93f36c73-98c3-3e85-a5ed-6f66af2b0479 | -13.1976 | -48.6489 | 2024-10-03 12:16:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 855621dd-65d8-32f6-980c-da9935081ccf | -13.0594 | -51.1409 | 2024-10-03 12:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 157.8 |
| 4a643967-f5b8-34d1-b424-b418d0b4deb1 | -13.1805 | -45.4489 | 2024-10-03 12:16:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 140.0 |
| b131c6ad-ac5b-3134-b71d-46cb5f6dfbe6 | -13.0402 | -51.1432 | 2024-10-03 12:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 58d514d0-190f-32b2-8560-adaf44243958 | -13.0591 | -51.1623 | 2024-10-03 12:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 60c0dd42-81a0-385c-90ac-9877d6e656a0 | -13.1927 | -51.1883 | 2024-10-03 12:16:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| c8581207-f1ab-3798-8766-636fe3775380 | -19.0141 | -43.1998 | 2024-10-03 12:16:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 105.4 |
| 42ce0a9d-5c08-3e00-a353-3f8de196f6ea | -19.0344 | -43.1944 | 2024-10-03 12:16:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 161.6 |
| 7dd70683-247c-3e9e-bf02-9ae7b5f611c3 | -19.0992 | -48.0568 | 2024-10-03 12:16:52 | GOES-16 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 131.9 |
| b38847e8-0c4c-34fd-90c3-f6c946eff91c | -19.2954 | -42.6032 | 2024-10-03 12:16:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 101.4 |
| b419fcc4-8d86-352a-bf0f-0aa29e560ee5 | -19.2962 | -42.5779 | 2024-10-03 12:16:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 103.4 |
| c1ea54f2-bd1c-30c4-9349-97f868ce587f | -19.5104 | -42.8691 | 2024-10-03 12:16:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 139.8 |
| 6a758556-21d6-3e2e-8d65-0d3b192bf297 | -19.4899 | -42.8746 | 2024-10-03 12:16:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 125.5 |
| 7560338d-ed5c-33f0-a854-2a5257292a6d | -8.7414 | -45.202 | 2024-10-03 12:25:55 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 66.0 |
| cda18863-ddac-3486-a342-734014f9a71b | -8.7225 | -45.204 | 2024-10-03 12:25:55 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 149.2 |
| 3a78eb3d-0b21-3145-9fa3-bf17861b520d | -8.7228 | -45.1812 | 2024-10-03 12:25:55 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 68.3 |
| d6629004-93a1-37ef-86f8-b573ab46dacc | -8.9074 | -44.1024 | 2024-10-03 12:25:56 | GOES-16 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 2ee83e93-6ce3-33c7-bfa7-8bd553ee0b32 | -8.9055 | -45.6387 | 2024-10-03 12:25:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| c18070fb-5b58-3141-9c65-f70e35599741 | -8.9244 | -45.6367 | 2024-10-03 12:25:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 337c9f5d-1fae-396b-9429-c5c19604efef | -9.5772 | -46.2639 | 2024-10-03 12:26:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 168.5 |
| 60450a14-11d2-3ba1-a5da-89fad7cc5a15 | -9.5775 | -46.2414 | 2024-10-03 12:26:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 116.5 |
| f8e61410-6fa9-3f1e-8495-18b98f2f00f9 | -10.2195 | -47.6839 | 2024-10-03 12:26:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 06c047cb-b7e1-3298-9fba-56c33fbeaa16 | -10.2381 | -47.7038 | 2024-10-03 12:26:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 1276e15b-2c85-3b50-8c96-04603971975d | -10.4775 | -48.1829 | 2024-10-03 12:26:05 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| eb3b65ae-3772-3c7d-ae3a-4ceb13662f0c | -10.5736 | -48.0839 | 2024-10-03 12:26:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 760398ef-2fa4-3c34-af39-d572c5607818 | -10.7168 | -46.1489 | 2024-10-03 12:26:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 163.6 |
| fede7aa1-48d9-398f-b4cd-96decf9e8f2f | -10.6981 | -46.1287 | 2024-10-03 12:26:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 461e3f87-f592-3fea-b9b4-21ac62954597 | -10.6978 | -46.1514 | 2024-10-03 12:26:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| ef2809c3-9752-31e6-99b7-a819abdb4324 | -10.7459 | -47.9757 | 2024-10-03 12:26:07 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 4955ccd0-2948-36c9-9055-d58b317c6863 | -11.0345 | -46.5143 | 2024-10-03 12:26:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 4fdbf141-562d-3ea4-9e3f-8c913a0c75ab | -11.1579 | -45.9551 | 2024-10-03 12:26:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 32749067-e35f-3ea0-afb8-94801c8bea21 | -11.2783 | -43.388 | 2024-10-03 12:26:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| a5865762-487a-3118-b307-133c3a0958a1 | -13.0591 | -51.1623 | 2024-10-03 12:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.7 |
| f16b20a1-71e4-31a9-8708-07aa9c107ba3 | -13.1976 | -48.6489 | 2024-10-03 12:26:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 1742520d-59da-32cf-9ae2-528db3fa41f7 | -13.0594 | -51.1409 | 2024-10-03 12:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 158.1 |
| 368eb96e-fdfe-3787-a2e7-5e95b34807c8 | -13.1801 | -45.472 | 2024-10-03 12:26:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 733639d2-0a04-34df-8438-629054a44cde | -13.1805 | -45.4489 | 2024-10-03 12:26:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 0bfcb9b9-b520-3e6f-b965-f0660ab6f8e2 | -13.0402 | -51.1432 | 2024-10-03 12:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 115.0 |
| d94184c3-8fc7-32fd-aef9-95e43f41727f | -19.0344 | -43.1944 | 2024-10-03 12:26:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 108.4 |
| f6075a50-2a57-3545-92d0-cc5153b6f77d | -19.2954 | -42.6032 | 2024-10-03 12:26:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 107.0 |
| 3d381468-ed47-3a1c-8b5e-258413501bbd | -19.2962 | -42.5779 | 2024-10-03 12:26:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 105.6 |
| a78a61a1-7de3-3a1f-9eb1-ccec6beea0bb | -7.6486 | -45.2218 | 2024-10-03 12:35:49 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 541c481b-cd7e-31a7-ad7d-62544a06b35c | -7.8626 | -43.0969 | 2024-10-03 12:35:50 | GOES-16 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 73.3 |
| f099b8b3-66f3-31ee-8432-1669fbb5ba9f | -7.8149 | -45.4782 | 2024-10-03 12:35:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 68.5 |
| a6439c9d-5219-3e3e-a486-4f185eaa8fd7 | -7.8629 | -43.0733 | 2024-10-03 12:35:50 | GOES-16 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 78.0 |
| 57e14e49-96a1-3b8a-a119-165b5ac09d5a | -7.8773 | -44.972 | 2024-10-03 12:35:51 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 9142aa03-e2b2-3f29-a681-d785664fd250 | -8.1567 | -43.7211 | 2024-10-03 12:35:52 | GOES-16 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 83.5 |
| 17d4dbe9-d7fa-3335-8b5d-f19d5a190e5a | -8.1756 | -43.719 | 2024-10-03 12:35:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 77.1 |
| 69907f4f-1c4f-3c46-bd47-4d64ad012765 | -8.7225 | -45.204 | 2024-10-03 12:35:55 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 43c151e7-c83f-3111-aae0-5478076f5b2e | -8.9074 | -44.1024 | 2024-10-03 12:35:56 | GOES-16 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 93.1 |
| bbf740ea-db9e-3b21-879c-e5081a458f48 | -8.9055 | -45.6387 | 2024-10-03 12:35:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 110.0 |


[Clique aqui para ver as próximas entradas](README211.md)
