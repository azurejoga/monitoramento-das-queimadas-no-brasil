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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4051d37-58df-3349-8f1a-6988e075decb | -4.07678 | -48.04726 | 2025-08-26 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 622f2f2d-a320-346f-8cdb-cfac9efa0fe3 | -2.26592 | -47.85569 | 2025-08-26 03:53:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b14aa1ea-7431-3075-88ba-0b17a32dcc02 | -5.49133 | -42.15372 | 2025-08-26 03:53:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| adb829b1-ea76-3567-a37b-61fb6b32e176 | -2.26472 | -47.85637 | 2025-08-26 03:53:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 341e35d9-f35b-3ad6-bd7f-6a263f6fe885 | -3.34894 | -43.27015 | 2025-08-26 03:53:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48908841-b952-31c0-9c06-1115a9e56efe | -3.34648 | -43.27018 | 2025-08-26 03:53:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a3aab56-3e8c-31a7-8e2b-d4cf88b6fd36 | -3.98882 | -47.88336 | 2025-08-26 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9d256bb5-1f25-3f1e-ac0e-025367823eab | -5.75331 | -40.44738 | 2025-08-26 03:53:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4a73bb7d-c695-333a-b3c2-afa36b8331f6 | -3.16852 | -49.47527 | 2025-08-26 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 35d205d6-70e6-340f-9beb-8ccb357c7b15 | -4.87833 | -37.48446 | 2025-08-26 03:53:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 034e5c97-93b9-32ca-b521-9170858c24b9 | -2.26526 | -47.85962 | 2025-08-26 03:53:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6b0e4287-454d-355b-97e0-f2b8f82bbf2d | -4.41245 | -40.48964 | 2025-08-26 03:53:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 969bdddb-e8d4-3e05-9c2b-f1e02621fd74 | -3.98326 | -47.88219 | 2025-08-26 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a6755d25-1440-3827-b62d-00ed35bfa53c | -4.63217 | -41.39843 | 2025-08-26 03:53:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 12624560-84f3-3643-a182-349d765423c2 | -5.07004 | -37.71641 | 2025-08-26 03:53:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c8d2b67b-139a-3f23-ab4f-7d7a2ee3181e | -3.36295 | -44.19166 | 2025-08-26 03:53:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 787e349e-be7e-3e2d-a341-7ba22082e8d1 | -4.07743 | -48.04335 | 2025-08-26 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3bd5911a-c47f-3969-a669-357664a7f4c4 | -3.97697 | -51.06044 | 2025-08-26 03:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3169ba2b-1a13-37b7-abb4-b4da52d8238c | -3.92096 | -47.68927 | 2025-08-26 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1601e60e-9d7d-3e59-bfd9-d8a4addd73a7 | -3.99001 | -47.88799 | 2025-08-26 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6ae1455-450e-36ec-9601-c282379168db | -2.29 | -47.8882 | 2025-08-26 03:53:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cafeefb7-bdf5-32a4-af9e-157b6f3fe176 | -3.98814 | -47.88728 | 2025-08-26 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2de6fa1e-c34b-30b4-97d2-3e63202bb702 | -4.01547 | -49.50858 | 2025-08-26 03:53:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f03248cc-6bba-320a-9478-f20f7a43810b | -4.66272 | -41.41655 | 2025-08-26 03:53:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a7bdfb5d-23e8-3d55-8b08-d33d57255d02 | -2.64995 | -48.05652 | 2025-08-26 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a7fa668-84f8-3a3e-bc9d-49d773b95ede | -3.49721 | -43.31262 | 2025-08-26 03:53:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a8b12ec-115a-3544-8284-08ec2cf3bae7 | -3.92061 | -47.68876 | 2025-08-26 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a3159b3a-85af-307e-aebe-f7f353017fe6 | -4.08013 | -48.04523 | 2025-08-26 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5388c8b9-5cf4-3a72-91db-b9d86882cd53 | -5.48504 | -41.40728 | 2025-08-26 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ba8a19dc-c66c-3d86-aaca-2ad8aa67b302 | -3.25102 | -46.9121 | 2025-08-26 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c008a65-43fb-3a16-981f-743a0a04dbf9 | -3.36365 | -44.18736 | 2025-08-26 03:53:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a47dd406-c7fc-34c1-b7c2-344ea9d9b923 | -5.48439 | -41.41137 | 2025-08-26 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 304c32d4-aefe-348a-a31d-863f1176c027 | -3.17104 | -49.47605 | 2025-08-26 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7ecf3447-a066-3329-b273-743419d6f50c | -3.1748 | -49.47629 | 2025-08-26 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1288c72c-267c-3595-8d20-7050ac95e1c1 | -3.17395 | -49.48117 | 2025-08-26 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 838eb7bb-a871-3820-997c-5f6869a5df91 | -3.06775 | -40.04822 | 2025-08-26 03:53:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 9ca6b7bd-c730-3d87-bd4c-0bebad03c2bc | -2.64952 | -48.05723 | 2025-08-26 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5b05ff1d-b79a-3f65-85b5-ccdce01c3adb | -5.51073 | -36.66701 | 2025-08-26 03:53:00 | NOAA-21 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 80afdbd9-1a9a-3976-91e6-667a899db3d0 | -6.4703 | -36.23682 | 2025-08-26 03:53:00 | NOAA-21 | PICUÍ | PARAÍBA | Brasil | 2511400 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dc4da955-6bda-3fee-afdd-f96b88dbbfa6 | -2.51431 | -47.71286 | 2025-08-26 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1090c024-86d4-33ed-b61b-e1b31c1405bf | -12.07994 | -46.63375 | 2025-08-26 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 576c436d-9b26-36c6-8c5e-2214007856cc | -8.30484 | -47.23 | 2025-08-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d4906231-5224-373b-a7a8-0932af836017 | -6.50014 | -44.68068 | 2025-08-26 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4bd60acd-963a-369a-aad7-d1ff1ef9f6e4 | -7.66506 | -42.65847 | 2025-08-26 03:55:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9fa21267-e11c-3287-a05c-4ad850f92048 | -7.57868 | -47.48943 | 2025-08-26 03:55:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80629f52-93e1-3099-8df6-531b82b4b03f | -6.8126 | -44.99627 | 2025-08-26 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 41ae0007-3e5e-34c4-bfd3-3600d5fd137f | -11.08937 | -44.77563 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0839a14d-c8cf-3925-95d7-e12d63a96240 | -7.53715 | -44.9416 | 2025-08-26 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 38a8662d-82fa-325b-a5ec-9c48cf9edd42 | -11.44121 | -47.32745 | 2025-08-26 03:55:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cb801044-73d2-3787-a206-fd9ddc4fbf8c | -9.64496 | -40.59664 | 2025-08-26 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 576b0732-864f-3a17-b5bf-76a72f0fe620 | -11.1006 | -44.75882 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f28b2737-7918-3f1d-b71c-acc141111603 | -7.21528 | -44.438 | 2025-08-26 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e802e28d-ebb9-3ec1-be77-fad87ddc874b | -5.8764 | -42.40956 | 2025-08-26 03:55:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3500ed0b-d0d7-3263-bddd-424bf3b7b141 | -12.41148 | -46.5034 | 2025-08-26 03:55:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c25b5135-f462-30f7-85f7-4fe1ddf711b4 | -6.56188 | -44.2177 | 2025-08-26 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f5ffc26c-8fc5-3587-a62f-27a18c1ceb04 | -12.42996 | -45.9672 | 2025-08-26 03:55:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ffe0f4b5-8aef-3b1f-aac8-dce6f95591e3 | -10.8112 | -48.32256 | 2025-08-26 03:55:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a545ec3a-bf7c-3572-b57e-d51b20c56a0c | -7.21795 | -39.22785 | 2025-08-26 03:55:00 | NOAA-21 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 93ee12bf-29f9-3168-80f5-8c7be7f53d0e | -11.16323 | -44.76237 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| f472da3c-89cc-3626-89f2-c9ade69abb68 | -8.47323 | -43.66958 | 2025-08-26 03:55:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8189a789-2ffa-3e4e-b255-3a207f3959af | -8.32498 | -50.57306 | 2025-08-26 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 58592ec7-e8c4-35ff-b640-19505c731bed | -6.62749 | -43.53284 | 2025-08-26 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2b315731-96fd-3595-a22a-e62feccfad28 | -11.1558 | -44.75735 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 727d4971-5ee3-3dce-9f6d-45dbc997f4f0 | -9.81307 | -43.94498 | 2025-08-26 03:55:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27d410b5-b830-3929-b9e5-9552873b0be6 | -5.87581 | -42.41159 | 2025-08-26 03:55:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 145b2706-8c35-38c2-9854-a1554e0359dc | -8.90945 | -44.85231 | 2025-08-26 03:55:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1d81ac0d-7203-3f9d-b745-c96548f23943 | -8.24494 | -45.10815 | 2025-08-26 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b35c2669-f360-3f03-883e-1179e9e1b895 | -7.30062 | -44.52444 | 2025-08-26 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b896930-5a69-3bf1-9c25-a877ea75f207 | -11.94801 | -43.92182 | 2025-08-26 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90f83440-e2e3-36f7-aec4-0110ae1c2c62 | -8.07582 | -44.99492 | 2025-08-26 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d86f95b8-2307-3dd7-b479-a7903ca22c70 | -10.53834 | -46.80224 | 2025-08-26 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 34bc3971-ccb9-33e0-9586-87f0ff6f2c4d | -10.77844 | -46.38382 | 2025-08-26 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d9f07e76-10b8-323f-8ac7-b690da1302a7 | -12.42187 | -43.4883 | 2025-08-26 03:55:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a29dc890-da79-3c45-802d-6e4d642b7f9c | -8.24637 | -45.09967 | 2025-08-26 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41286da6-83b8-38bc-bb3b-fc5474ee5f20 | -7.58786 | -47.49752 | 2025-08-26 03:55:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 49c09a50-98a3-308c-9de9-bf9685f51e43 | -11.16045 | -44.75453 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 603c9e8b-33b7-310b-a943-a7769d3a9365 | -11.08811 | -44.78292 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4061d1f5-d1b8-306c-83bc-ed3d4b4d8a5b | -6.78538 | -44.30819 | 2025-08-26 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4bd1079f-1d50-3421-8957-ca27070ba976 | -9.93418 | -44.01485 | 2025-08-26 03:55:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c65338c-19f4-399c-9ac8-0482a5276925 | -8.31787 | -47.24528 | 2025-08-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35d0a274-51db-3393-af12-27013b0c65ac | -6.31554 | -47.41869 | 2025-08-26 03:55:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f6125dc-c7ef-3bba-b018-9032f841512d | -8.30448 | -47.23393 | 2025-08-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b4ae9a4a-6edf-3b00-88a3-7c639905adfc | -6.28849 | -43.84016 | 2025-08-26 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a7bdef3d-1bfc-3a95-8b44-56bb76f7a258 | -11.15517 | -44.76092 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c05fe34c-ce77-30fb-b989-a09ef0c3c349 | -6.69899 | -48.38479 | 2025-08-26 03:55:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 9e186752-bdc6-394d-9065-4bfea7560145 | -7.6606 | -42.66228 | 2025-08-26 03:55:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| db139326-fec2-301f-ac9c-d72746d87141 | -8.33117 | -50.57416 | 2025-08-26 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| ff57d60c-1668-336e-a1bf-240a10874a1e | -10.53745 | -46.80724 | 2025-08-26 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 74f62eed-7fb4-3d1f-8b3b-e6a8d30a0c31 | -8.32624 | -47.25594 | 2025-08-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9dea8cb1-7047-3f30-aacc-bb957c5af0bb | -8.24417 | -45.08636 | 2025-08-26 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3dc0cdca-633b-3628-9d96-763ec30cea56 | -8.33175 | -50.57716 | 2025-08-26 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 8a4882cf-db4f-31f1-8872-622e1b82c12f | -11.25507 | -44.97811 | 2025-08-26 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cdefaec6-1306-3237-9c5e-1281ae091d1e | -8.26783 | -47.2355 | 2025-08-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d661ae2a-89c3-3e06-b963-a575f08584f9 | -8.11224 | -47.12682 | 2025-08-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 81f85b74-cae2-3db4-82d3-c23b1e18e9a0 | -8.38068 | -48.02873 | 2025-08-26 03:55:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5863e9ef-4c95-3430-b4e2-0fcc230520b6 | -6.44455 | -46.11633 | 2025-08-26 03:55:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ceecd8ea-0c57-3baa-a3fd-341f649251bf | -11.03149 | -49.1412 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5bccae09-297f-31dc-89f8-2ae4e5acd27a | -7.65986 | -42.66676 | 2025-08-26 03:55:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c64b9b29-bc1a-30d7-b254-1fb69e783c4a | -8.38116 | -48.02446 | 2025-08-26 03:55:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c557a42a-280c-3864-89e1-ff9bb5f896a5 | -7.65164 | -42.67002 | 2025-08-26 03:55:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |


[Clique aqui para ver as próximas entradas](README26.md)
