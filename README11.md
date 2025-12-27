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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e188b5fa-214e-3567-bbcd-02968521fbd7 | -10.49117 | -44.92742 | 2025-12-27 04:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| c394e8b8-8d6d-3f12-85ba-7ef28428beb9 | -3.13275 | -52.84986 | 2025-12-27 04:40:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2cc90886-e77b-380b-9552-ec9e3bd0d7ae | -5.67425 | -47.51531 | 2025-12-27 04:40:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95984e07-2543-3a0c-b392-7a8387c041a7 | -10.49588 | -44.92422 | 2025-12-27 04:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9932fa71-7df9-3e87-91af-14ab4254c88b | -10.49171 | -44.92357 | 2025-12-27 04:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a194e082-fd29-35e7-82d0-b650988e2daa | -10.48284 | -44.92609 | 2025-12-27 04:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ea3fd158-e979-37b0-ac5c-a9517d765ec5 | -10.36357 | -45.16074 | 2025-12-27 04:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21d471ca-554c-3950-b487-c2a847d3dfb4 | -5.4521 | -46.1781 | 2025-12-27 04:40:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 53d3dab9-6471-37cf-8000-e3a40918d998 | -5.44464 | -49.27024 | 2025-12-27 04:40:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| abebec3f-04cd-30ae-9f7b-dd76e1b61215 | -10.36304 | -45.1645 | 2025-12-27 04:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f08bd59b-09c6-3348-874c-1d2bb94c8746 | -11.84612 | -43.79378 | 2025-12-27 04:40:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 16bae013-0265-348e-8ec3-fbc50369c2dc | -4.91757 | -40.66406 | 2025-12-27 04:40:00 | NOAA-20 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a3572999-1fc7-304f-afe7-9ba959fe2fe7 | -5.7521 | -45.11551 | 2025-12-27 04:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| dddb09f7-0d3d-3b06-95b2-8fe04616ff4e | -3.004 | -52.87862 | 2025-12-27 04:40:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dff027ae-1243-35ff-a9b1-2818e0b72793 | -3.74946 | -49.72066 | 2025-12-27 04:40:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3145b83c-8f19-3d35-a831-ad0d2fce1004 | -3.59342 | -49.44009 | 2025-12-27 04:40:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63d70cd6-2455-3191-a862-63a0c033d998 | -4.17028 | -48.58461 | 2025-12-27 04:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93dbaf56-879d-300a-a962-e9a0282a5706 | -10.94041 | -49.42582 | 2025-12-27 04:40:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0272bcf-5c46-3fd9-a2fc-4a4bb1cd6687 | -10.48701 | -44.92675 | 2025-12-27 04:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| ee71e68c-44e5-3c27-9a27-207a9fa3c858 | -8.56351 | -50.01759 | 2025-12-27 04:40:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| faed9c47-bb76-3e39-9749-d08351111975 | -10.54199 | -48.71364 | 2025-12-27 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 226f6f3c-a935-3e8b-b128-f9d4494826a9 | -3.40396 | -51.19316 | 2025-12-27 04:40:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 167de8d9-3673-3820-b3fa-bbdba9355f3f | -11.39219 | -47.99579 | 2025-12-27 04:40:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 081508e2-2cde-372f-945e-62310b8f0d3f | -4.62717 | -47.9426 | 2025-12-27 04:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4383e923-c4e3-3efd-beed-8e2a8f7590e6 | -4.50974 | -43.49168 | 2025-12-27 04:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be899e80-ee72-394a-a5fe-4233f269c13e | -4.75208 | -48.23341 | 2025-12-27 04:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8db6f094-c1ba-31f7-9c8e-ce706b6c7a6d | -3.75169 | -49.72815 | 2025-12-27 04:40:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fa32b7cd-6159-36f5-9958-8087efb9da97 | -11.13045 | -44.28844 | 2025-12-27 04:40:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe724031-d84f-3afd-84f4-74c7d1b36355 | -10.64481 | -49.73402 | 2025-12-27 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a9935338-4954-3571-b15f-b20b9f716a64 | -3.74559 | -49.72361 | 2025-12-27 04:40:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c627e76-8909-3898-a1f0-954f742fb483 | -3.59935 | -49.3596 | 2025-12-27 04:40:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f6a2efb6-0f5a-3e75-af82-4081c6f3ae62 | -4.17305 | -48.58859 | 2025-12-27 04:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5793436-2f23-36c2-ad30-6115e71ceeb0 | -11.01768 | -45.25955 | 2025-12-27 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3eb93152-db9d-3239-a7b0-b8908b95f9c0 | -6.54656 | -43.10601 | 2025-12-27 04:40:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 500c8a53-c91e-3ef5-bb10-5ab8046b9e8a | -11.15771 | -43.32041 | 2025-12-27 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 500b9515-c217-359c-8acf-b6e2a5e1bed5 | -11.84913 | -43.73561 | 2025-12-27 04:40:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c086fea-b6a0-3995-992a-ce03877492ae | -4.42596 | -49.88891 | 2025-12-27 04:40:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c52da75e-ad95-329b-8a41-96572a64043e | -3.8223 | -49.71124 | 2025-12-27 04:40:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7badab1d-5ce9-30ee-ba10-98d02cad56e4 | -3.74891 | -49.72414 | 2025-12-27 04:40:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e228a5ed-4b6f-3102-8903-e0ae45ce83b0 | -3.74836 | -49.72761 | 2025-12-27 04:40:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03a8cb5e-13b7-37d2-bb2b-f83ca490404b | -11.16779 | -43.31669 | 2025-12-27 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 367ff1f8-e5b0-3f05-91c8-563be0b23dae | -6.62241 | -43.86692 | 2025-12-27 04:40:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f6db7753-cb92-38ae-b528-590230882a71 | -4.17359 | -48.58513 | 2025-12-27 04:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fb5adc9-14c7-36cb-89b9-70e7d6c36d90 | -3.80126 | -49.75786 | 2025-12-27 04:40:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58ab2a5e-6efb-33a4-9f94-4f93de9de605 | -6.53638 | -43.11354 | 2025-12-27 04:40:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f172ca72-4f3b-3b0e-a7c3-db3b0a804a17 | -10.53858 | -48.7131 | 2025-12-27 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1ad77af-8dc7-381e-b48d-0179952c10de | -4.89665 | -40.44487 | 2025-12-27 04:40:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c7aa8e7b-a816-32e8-b967-790ca4da2b3f | -4.51031 | -43.49134 | 2025-12-27 04:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8dd25d1f-80d3-3d12-b18a-c84842a21ec4 | -4.63053 | -47.94312 | 2025-12-27 04:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e53736a-975c-3686-a13f-07017b9ee770 | -9.83053 | -49.14701 | 2025-12-27 04:40:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00ead178-ec94-3ff7-863d-a80d0beb2548 | -3.11721 | -52.40245 | 2025-12-27 04:40:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f72f1fb8-df68-3121-b0ac-0e251cafaa12 | -11.85375 | -43.73626 | 2025-12-27 04:40:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 777d159d-d42a-3cbf-9687-2f54d6b1bbef | -11.8485 | -43.74042 | 2025-12-27 04:40:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 669918bc-b0d3-3c03-9cf5-d22114507634 | -9.73294 | -48.51099 | 2025-12-27 04:40:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 621d4dbd-13b4-38c8-8bd1-5a88c0a2382f | -5.01937 | -48.12631 | 2025-12-27 04:40:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ffe733c0-1cd3-31ee-884c-b23f750b2b3d | -5.92656 | -43.51478 | 2025-12-27 04:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7690d829-20d4-35e4-b6b5-20bee986d706 | -7.22381 | -43.08031 | 2025-12-27 04:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 91551ba3-f97f-3544-9bba-7fd1efea5c69 | -3.46568 | -52.80301 | 2025-12-27 04:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdafa179-c905-310e-a514-b8b8c5e500e6 | -3.79794 | -49.75734 | 2025-12-27 04:40:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f214d47b-dc02-3ce0-a490-7199065dc614 | -5.47838 | -46.83343 | 2025-12-27 04:40:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b2a053b-7344-3583-bd54-dab8e7ad1573 | -3.57187 | -52.25571 | 2025-12-27 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40008fb5-e591-30d2-a4fb-1e662ba6e834 | -3.59287 | -49.44355 | 2025-12-27 04:40:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0470e377-a56e-3d69-8977-b61424c1a9c3 | -11.39159 | -47.99979 | 2025-12-27 04:40:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 64602f7c-d761-36fc-8ec6-8c99bcc6ddaf | -3.25502 | -52.43179 | 2025-12-27 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8bfbd1e-92fc-3446-89d4-39b1b3742e63 | -10.14446 | -48.07964 | 2025-12-27 04:40:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab414dd3-5f53-3c5b-9233-3e25695ffd06 | -10.95159 | -49.42018 | 2025-12-27 04:40:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| addd2ddc-a733-3794-91e1-7bcf2993761e | -3.81954 | -49.70719 | 2025-12-27 04:40:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c50cdfa2-e105-3c51-91ac-f990e29ec741 | -10.77246 | -45.01661 | 2025-12-27 04:40:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5e3dc1b0-5059-3826-baa6-a7c397206864 | -3.12897 | -52.84923 | 2025-12-27 04:40:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f2b1725-bfce-38fa-9071-0e239e346aea | -10.48648 | -44.93058 | 2025-12-27 04:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 74a73ecc-ad3d-3bab-bf92-52e324004d25 | -6.17862 | -43.41513 | 2025-12-27 04:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b8cf36ce-5692-3b60-b826-08a40eb83f2f | -6.22149 | -55.65794 | 2025-12-27 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf0c59ca-1b00-320d-a18f-7a224103c01b | -6.54147 | -43.1098 | 2025-12-27 04:40:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72d39114-c660-3812-a809-14f5a699ab0b | -10.14098 | -48.07909 | 2025-12-27 04:40:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a1fb6fb-1091-369b-a21b-e628eae3a894 | -3.74504 | -49.72708 | 2025-12-27 04:40:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01bb9b49-c3b6-3dd1-82f4-a0c36d4abec5 | -11.39279 | -47.99179 | 2025-12-27 04:40:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ade70083-9da1-3659-971b-90672d57ed64 | -8.98019 | -48.07664 | 2025-12-27 04:40:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ef02de73-10d8-361e-abfc-9a2da1043d24 | -10.49065 | -44.93124 | 2025-12-27 04:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 4901ddae-2caf-31d6-a4da-85f3c4e41302 | -3.6032 | -49.35667 | 2025-12-27 04:40:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ddbbc9bc-8416-3636-b616-c284c6b2b326 | -10.94768 | -49.42326 | 2025-12-27 04:40:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc90c297-9d0f-3cc7-9223-0f28c5eae4f1 | -11.01356 | -45.25903 | 2025-12-27 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5f615ce-4b65-3e1c-b2fc-0c4b06fda29e | -3.75224 | -49.72467 | 2025-12-27 04:40:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f7358001-72e8-3017-b167-0133714548da | -10.7708 | -45.01665 | 2025-12-27 04:40:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ebc4a330-97da-3e27-97cd-c1ed43ba34da | -10.87947 | -48.98054 | 2025-12-27 04:40:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c7f8bb7-b22d-3976-9696-b634a78369f2 | -10.81079 | -49.29483 | 2025-12-27 04:40:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba7b1b01-110f-3f2b-bda2-0cf17ac0a89b | -10.49481 | -44.93188 | 2025-12-27 04:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0fe68913-3bde-3e4f-8167-1a7a85d51a98 | -3.60266 | -49.36012 | 2025-12-27 04:40:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 03802706-c79c-3302-ba8f-775c04a89786 | -4.89619 | -40.44807 | 2025-12-27 04:40:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fd7345c3-ff13-39bb-a500-51d9fcc40c70 | -2.98081 | -52.63446 | 2025-12-27 04:40:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb1f78a9-72dc-36bd-a295-45d6c83196ac | -2.98222 | -52.63174 | 2025-12-27 04:40:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f14695a7-9483-3c7f-abf3-1f15df194d24 | -6.18295 | -43.41586 | 2025-12-27 04:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ac49f363-b94c-3d5c-83de-cb2e9ac6c340 | -10.48231 | -44.92991 | 2025-12-27 04:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cc0077a1-871b-319b-9f6e-9023a29f550c | -5.67367 | -47.51905 | 2025-12-27 04:40:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3fe1fa2d-b2b7-3c85-af70-f07224971911 | -11.10581 | -49.10128 | 2025-12-27 04:40:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| da6b1a17-0005-36a2-acce-bca7897affd3 | -11.16846 | -43.31164 | 2025-12-27 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 0ecbc165-5304-396f-a7f1-92fdd4320df7 | -10.94823 | -49.41966 | 2025-12-27 04:40:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7163450c-db43-3dd9-942f-a4123bb4ab26 | -3.25133 | -52.4312 | 2025-12-27 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e51694b-4701-328e-8366-660dacf8af6d | -11.10638 | -49.0976 | 2025-12-27 04:40:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 674255a0-ef8b-32be-a20f-d46696d96c3d | -10.36767 | -45.16135 | 2025-12-27 04:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d9482a7-4d25-3224-8fd4-893e5f037ce5 | -10.94432 | -49.42274 | 2025-12-27 04:40:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README12.md)
