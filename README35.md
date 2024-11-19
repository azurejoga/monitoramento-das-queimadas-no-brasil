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
| 945cce35-ec02-3eb0-8c75-fb2a91716321 | -5.97974 | -45.36232 | 2024-11-19 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f1a70e52-8d20-3de5-aba2-036ea9104f75 | -1.22484 | -51.7481 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f655eff-2b10-396c-9f24-df66df544093 | -6.20141 | -46.321 | 2024-11-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc51d8b4-bb3a-30b6-964b-d16b72fb8f84 | -1.94267 | -46.95737 | 2024-11-19 04:46:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6fcdeaca-28fb-3cec-a173-bb14b3c86bab | -1.36973 | -47.26239 | 2024-11-19 04:46:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bdef6d43-56df-31c7-ad1f-8235aaa14436 | -1.33724 | -51.85809 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3ab43ba-3357-3c9a-a4d6-80de63dcb515 | -2.31044 | -46.85691 | 2024-11-19 04:46:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 516a4bf9-4c30-3caa-8967-42541d502fe1 | -2.74999 | -54.01472 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 964f4749-188d-3bc5-98e6-c0604ca2c519 | -1.16682 | -53.38074 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6da173fb-f56f-378b-8198-5e18e2afaf13 | -5.9713 | -45.36086 | 2024-11-19 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f284cf99-c670-3258-815b-f515fc73ce60 | -2.93883 | -53.88838 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a019fc34-d363-384e-af27-e65f7871a168 | -3.36443 | -50.82141 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4e2f2ed-a8de-3be5-8319-27f7f9caad77 | -1.78536 | -53.5959 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff487df0-7bbd-31f2-a8ed-9edb719fe306 | -3.32621 | -52.99718 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd192385-d977-3962-8d03-7c4d6fce23b3 | -2.24787 | -50.08706 | 2024-11-19 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b705754-78bf-3b36-a45b-aab1cddb8db2 | -1.43639 | -53.38535 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b2505dc8-7ccf-30f9-9d1b-6e8f93d6d68b | -4.38302 | -47.75656 | 2024-11-19 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ba9f21f5-eda3-3415-be84-4418a7bc0ba5 | -1.95364 | -53.00389 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c389a77e-ce95-35f4-ae37-1b347f4e515d | -2.90352 | -53.05272 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b099004d-7dcc-3dc5-ac48-fb679aba3ae9 | -3.31669 | -54.08249 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2f0e2d23-ef3f-3202-a8d2-df4dfb3a1e67 | -3.88971 | -46.93547 | 2024-11-19 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| c6af9f0c-341e-3e43-aa96-2eade7a009ad | -1.63276 | -52.58416 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72747104-59f9-3616-8964-1204494b8969 | -6.88046 | -44.76657 | 2024-11-19 04:46:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51ce1b4f-94bc-3f5e-85f8-3a0b46d7ecb3 | -8.95452 | -47.63804 | 2024-11-19 04:48:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f14e859c-0399-33a9-9e7d-01aa0188ba08 | -7.66306 | -49.12489 | 2024-11-19 04:48:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e407214-ae34-3cb5-8849-870c530ee268 | -10.85531 | -47.65615 | 2024-11-19 04:48:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5c1e66f-79be-3e94-8915-49c1113d1aff | -11.88698 | -43.81165 | 2024-11-19 04:48:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| abc8ac2f-b8a1-3739-8033-8202a714eb8b | -10.34822 | -47.50099 | 2024-11-19 04:48:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 218b67cc-f298-3e86-948c-e11f2d646e05 | -10.3443 | -47.50039 | 2024-11-19 04:48:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0577b4a3-47db-3324-bead-8fc76dc6ce76 | -11.5584 | -44.02444 | 2024-11-19 04:48:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 059e666a-a077-31c0-94ca-bb9b4a01e3c0 | -9.25014 | -45.00274 | 2024-11-19 04:48:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6ea65bf4-b72b-31fd-b0ea-993c203745af | -9.24623 | -44.99738 | 2024-11-19 04:48:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d518259b-4754-3a31-9379-5897f5636b51 | -8.29396 | -49.98405 | 2024-11-19 04:48:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb5dba63-724a-3d0c-a4b0-268aa5c3d76b | -10.406 | -44.47955 | 2024-11-19 04:48:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8b320dc1-2826-314b-a8ba-e0c520400be8 | -8.67979 | -47.98891 | 2024-11-19 04:48:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32919ace-9608-3eef-9d37-e6797580e37e | -10.97431 | -44.53321 | 2024-11-19 04:48:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 998af220-7663-3277-97f3-eb073d2d8833 | -11.88659 | -43.81473 | 2024-11-19 04:48:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b378b520-5705-34e3-b686-8cef0805eb63 | -10.82051 | -44.36789 | 2024-11-19 04:48:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 3078ada7-fd99-3338-8fe4-9e301ed17630 | -10.46185 | -45.06853 | 2024-11-19 04:48:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| eb32c73d-7403-30e4-9c61-e99ec1ae8bd4 | -10.72824 | -49.51035 | 2024-11-19 04:48:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 5f37563d-3f08-3711-aaca-9cdb2b984314 | -10.34786 | -47.50375 | 2024-11-19 04:48:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| be7cc268-d69a-3043-93b4-7bfa7e409528 | -9.24558 | -45.00208 | 2024-11-19 04:48:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 19fdd687-a638-3025-8b08-032795a6931c | -9.89515 | -44.42968 | 2024-11-19 04:48:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ffb3aba5-ae0d-3478-ba0a-5a98a1972707 | -10.54183 | -44.67231 | 2024-11-19 04:48:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a248d3b4-b271-3810-b7c1-687019d0491f | -10.34175 | -47.51835 | 2024-11-19 04:48:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ec812677-4a8c-3f6d-b1df-9db901f46152 | -11.56395 | -44.02559 | 2024-11-19 04:48:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f1820a7-6626-3a4c-973d-ef20ce6f0a78 | -11.24664 | -44.65588 | 2024-11-19 04:48:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| edd57a3d-868a-3722-ba04-7d093cead66f | -8.5048 | -43.90987 | 2024-11-19 04:48:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 12c68212-e4dd-3fdb-acca-2ab7bf5c423e | -10.44504 | -44.88397 | 2024-11-19 04:48:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5aee58d8-c59a-3dbe-91e3-7d38d477098d | -7.99091 | -49.62395 | 2024-11-19 04:48:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 82fae60a-a60c-3353-9fdf-5b8f978d4fd9 | -8.98242 | -50.01943 | 2024-11-19 04:48:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dbd2b01f-3389-3735-9126-03f4bb21e782 | -8.29056 | -49.98352 | 2024-11-19 04:48:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc5fc25b-1f2b-318c-8a3b-fe0ed49c7301 | -9.26252 | -45.01406 | 2024-11-19 04:48:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f135352b-0ad5-386f-90f1-491ffac53b85 | -13.17163 | -53.28788 | 2024-11-19 04:48:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 64c278dc-32e5-379b-aa47-c6b08b88e1d6 | -10.46287 | -45.06731 | 2024-11-19 04:48:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ce9376e0-eb2e-302a-975b-1c42cef79d0b | -9.07179 | -49.21452 | 2024-11-19 04:48:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b87f5896-9514-3b9f-86e4-510721354f6a | -9.29488 | -43.27688 | 2024-11-19 04:48:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 28b2119d-b2f9-38ff-86d9-ebd9b0fd27f0 | -8.67606 | -47.98832 | 2024-11-19 04:48:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e58799e-ca07-3e52-bd41-8a1479fc23ef | -9.89533 | -44.42887 | 2024-11-19 04:48:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 69493d04-a805-3707-8ad8-f6aadfd703ee | -7.97948 | -48.1791 | 2024-11-19 04:48:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f43841e4-4d5b-3f42-8de5-6b438cc572ba | -9.51101 | -47.24488 | 2024-11-19 04:48:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0651b75b-f736-311d-b7c5-8c04626fc470 | -9.06769 | -49.21794 | 2024-11-19 04:48:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a88c5780-013d-3c16-b230-b28645698a6f | -13.1722 | -53.28434 | 2024-11-19 04:48:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f51b867e-8347-30b3-9ac6-38c2a544c29b | -13.17551 | -53.28489 | 2024-11-19 04:48:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d9f99e5e-632d-32c4-80e6-a7c3d291aaa1 | -10.42042 | -44.48158 | 2024-11-19 04:48:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 57bf1046-e6c5-3785-9046-8ab1764414a7 | -10.52436 | -44.95201 | 2024-11-19 04:48:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0db2790d-bccf-3ee3-b107-d27f3e597da1 | -11.41574 | -51.27744 | 2024-11-19 04:48:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8bbbdfa-4e22-3237-a39a-db81aa604c2e | -10.96948 | -44.53257 | 2024-11-19 04:48:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 83c3e01a-332b-3958-b594-870d2617a72d | -10.83604 | -44.32495 | 2024-11-19 04:48:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47c0f508-6630-3792-9bff-547206889987 | -8.95384 | -47.64278 | 2024-11-19 04:48:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a5074c4-6277-3aeb-9127-3e92b5e489f4 | -10.70841 | -48.81949 | 2024-11-19 04:48:00 | NOAA-21 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e398f536-3bbf-3a6e-9041-26c7a1590c5d | -9.31012 | -46.1841 | 2024-11-19 04:48:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6c385969-652c-333b-9967-5fec24146351 | -11.55891 | -44.02488 | 2024-11-19 04:48:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f7c372a-08e0-31e0-8214-0d27a582be1b | -10.856 | -47.65108 | 2024-11-19 04:48:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f0d97a6d-a1bd-3e7b-9831-bf080c2a9cba | -10.85583 | -47.64975 | 2024-11-19 04:48:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a87aa951-2fb8-3035-838c-31ffab56b2e1 | -10.45759 | -45.07146 | 2024-11-19 04:48:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66ba2a71-57ff-3d8a-b4d9-05334ab55d45 | -10.78569 | -44.32954 | 2024-11-19 04:48:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 65c577e2-8bc0-3e27-8b5a-97e0f956e3c2 | -10.90217 | -44.56617 | 2024-11-19 04:48:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf16d1aa-3d22-3564-a4db-7c67c5ffdcf4 | -11.73421 | -43.84282 | 2024-11-19 04:48:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 42c49110-4a6f-3f4b-ae90-25699bc4204f | -10.97559 | -44.44518 | 2024-11-19 04:48:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d64de472-2bee-3407-bfd1-9c6c0d163068 | -10.40119 | -44.47887 | 2024-11-19 04:48:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 43300767-8825-3f2b-8005-78bc9bc2421b | -9.30646 | -46.1796 | 2024-11-19 04:48:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff957d61-fb42-32ea-b467-bfbbe22faef1 | -10.97054 | -44.53193 | 2024-11-19 04:48:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| d05641d5-7070-3ce2-8d3d-45d5bf37064e | -11.56344 | -44.02516 | 2024-11-19 04:48:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f322639e-64a1-3e4e-9997-bf43fc8fc4e7 | -11.02581 | -41.73668 | 2024-11-19 04:48:00 | NOAA-21 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4ec5265a-2bce-300c-9d06-79b6163c45c8 | -9.25926 | -45.00404 | 2024-11-19 04:48:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 72ea4046-caa4-3ec2-bd1f-8fcbf40658e0 | -13.17882 | -53.28543 | 2024-11-19 04:48:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cec644f7-cbaf-3e76-8eb3-4e83fb674c16 | -9.2547 | -45.00339 | 2024-11-19 04:48:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9cc4a79f-7218-37a3-b1b8-43feb9b29874 | -10.73177 | -49.51087 | 2024-11-19 04:48:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| b039199b-d6fc-3fef-8e79-b3731cdd509a | -10.84962 | -44.25903 | 2024-11-19 04:48:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b738d9a-6100-3a75-9fa3-2dd61c3cc0e9 | -10.70599 | -48.81026 | 2024-11-19 04:48:00 | NOAA-21 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f48832d2-c2f1-33c7-9138-19b5562eb168 | -8.95834 | -47.63863 | 2024-11-19 04:48:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f0f6b569-100d-3a31-920d-8769f0f572cb | -9.25861 | -45.00873 | 2024-11-19 04:48:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 36bd0643-bf40-3450-b692-b74a3ff66c92 | -11.72909 | -43.84212 | 2024-11-19 04:48:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c923a76-6dfa-3b71-ad99-c02843a8bce5 | -9.25535 | -44.9987 | 2024-11-19 04:48:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e2050dea-f537-32fd-883e-1e6550367b2c | -10.01215 | -47.55803 | 2024-11-19 04:48:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd9e81ef-b7b2-37ff-b8e4-3a5a32c1887b | -10.85064 | -44.88679 | 2024-11-19 04:48:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ecf8f56e-fa96-3ce1-aeb5-295ccee19c32 | -9.98431 | -44.72022 | 2024-11-19 04:48:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 324717ca-acd4-3743-ae41-9483a883c4a8 | -8.68416 | -47.98502 | 2024-11-19 04:48:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 674cc8e1-8589-36af-be26-7cd0eb5d15c1 | -7.66538 | -49.10941 | 2024-11-19 04:48:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README36.md)
