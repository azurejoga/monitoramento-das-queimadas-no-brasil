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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c0f3ad3-60e9-31f2-9d57-d993cca04b3a | -3.22854 | -46.80349 | 2024-12-20 03:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6a559ba-c873-3abe-a775-050d000fdcd3 | -10.45684 | -37.12464 | 2024-12-20 03:49:00 | NPP-375D | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| dc710185-75da-3ecb-8640-1ffd1084e653 | -2.55429 | -46.93087 | 2024-12-20 03:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59cc7434-a7da-31c2-8065-368b8899aaa4 | -3.95569 | -41.48772 | 2024-12-20 03:49:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| daff6116-efc3-3b76-bf04-7ec285e70fec | -3.23141 | -46.7866 | 2024-12-20 03:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bea32c1a-3af7-31be-a126-38a4d526a19d | -12.4098 | -43.8014 | 2024-12-20 03:49:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35e71a34-04b3-3e59-9b27-88904cc9826c | -10.45351 | -37.12411 | 2024-12-20 03:49:00 | NPP-375D | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 9a26dc89-27de-3b6f-ad08-1b0b0c2a0204 | -2.42656 | -45.68185 | 2024-12-20 03:49:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd71bf9a-d2c5-3e10-9a17-aac62cd245ff | -12.86549 | -43.74367 | 2024-12-20 03:49:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a15ca76f-3477-36b2-83eb-7cbea8f1eba1 | -2.7629 | -45.55657 | 2024-12-20 03:49:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6cc67be8-ba7c-3335-9b5a-8c10d1e9d1d5 | -3.71503 | -41.69626 | 2024-12-20 03:49:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1b081177-50aa-3bc7-a743-e84e93310ff8 | -9.29485 | -40.42607 | 2024-12-20 03:49:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b2a5e3d9-e897-3536-a0e5-00785123d811 | -10.49037 | -36.86419 | 2024-12-20 03:49:00 | NPP-375D | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1f3dde68-9443-397d-92b6-d8f9447e6adb | -3.20483 | -45.51163 | 2024-12-20 03:49:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ddee2e2-9150-3b97-816a-6e9f5da79c36 | -3.7012 | -42.12888 | 2024-12-20 03:49:00 | NPP-375D | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bd742545-e9e1-3d15-85cc-dba798dfad90 | -15.30803 | -43.13283 | 2024-12-20 03:49:00 | NPP-375D | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 5c616563-e593-31b7-a780-af46d2373c89 | -2.56029 | -46.93204 | 2024-12-20 03:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e49b0cb-dcbb-3c47-a3a0-6b93f1464920 | -10.15092 | -42.16658 | 2024-12-20 03:49:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7739555a-a8a7-34c6-9093-c4482c3e6c46 | -3.22997 | -46.7951 | 2024-12-20 03:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 933b915b-7257-3c5f-9814-033470f35d8d | -10.48982 | -36.86775 | 2024-12-20 03:49:00 | NPP-375D | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 6b4dc865-37ca-323e-a4aa-e3c3a0c789bf | -12.33194 | -43.67791 | 2024-12-20 03:49:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea3f41a4-c67d-3b4d-abfb-4adc93cd5985 | -12.15643 | -43.49164 | 2024-12-20 03:49:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7e39f3ed-678e-393b-b92f-4a3bc41d3a04 | -9.90472 | -36.766 | 2024-12-20 03:49:00 | NPP-375D | CAMPO GRANDE | ALAGOAS | Brasil | 2701506 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| de88cd1e-ad08-31da-ba23-852e0aea36a5 | -2.96899 | -40.22733 | 2024-12-20 03:49:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 97e8b50d-da3d-3201-b5e0-5e4ea1689850 | -2.75737 | -45.56024 | 2024-12-20 03:49:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a30d291-be3e-332c-9eca-52377c01040d | -15.30421 | -43.13211 | 2024-12-20 03:49:00 | NPP-375D | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 09a24833-b1ad-3960-8c27-c2b37327b10d | -3.23588 | -46.79616 | 2024-12-20 03:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bdaf85ed-f687-3f0e-b82a-f77a217c5b34 | -10.61473 | -37.0046 | 2024-12-20 03:49:00 | NPP-375D | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0129894e-2d5a-3e77-a88b-acafc1afcf7b | -2.76346 | -45.55754 | 2024-12-20 03:49:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c59892ac-16c6-3a64-a32d-2615e2ac2a0a | -3.23447 | -46.8045 | 2024-12-20 03:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db02e17a-f90f-3494-a893-0abf00edc839 | -12.15233 | -43.49091 | 2024-12-20 03:49:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fd0d3ab7-833f-3ca5-91e1-9a14fd9c6d1a | -14.7198 | -42.64656 | 2024-12-20 03:49:00 | NPP-375D | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a6120a7-ab01-3923-9bbf-fff367db5b7f | -8.45657 | -40.82422 | 2024-12-20 03:49:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 85cf4e8a-4fcb-31d1-bc19-89b8f20a09f8 | -3.22925 | -46.7993 | 2024-12-20 03:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bd3b3b23-6a36-3dcb-a03c-91877d0bfd04 | -9.90138 | -36.76547 | 2024-12-20 03:49:00 | NPP-375D | GIRAU DO PONCIANO | ALAGOAS | Brasil | 2702900 | 27 | 33 | nan | nan | nan | Caatinga | 0.4 |
| aa3d4e9c-0a56-32a5-9edb-ddb24eb69719 | -12.66927 | -43.43725 | 2024-12-20 03:49:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1f9b8b73-2da6-3078-a215-6d138c28bd8f | -11.32901 | -40.46094 | 2024-12-20 03:49:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 177b2efd-1f4a-37e0-b908-8ba014f00217 | -12.41395 | -43.80222 | 2024-12-20 03:49:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2b4cc2c4-2bb0-3866-b11c-6d6dde0f413c | -3.71635 | -41.69588 | 2024-12-20 03:49:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e317822e-e998-3e90-9618-956a789443d1 | -3.23069 | -46.79085 | 2024-12-20 03:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4487565e-6ad5-3a7f-8da4-d5b404febc30 | -3.20543 | -45.50812 | 2024-12-20 03:49:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd136f1b-e1be-3641-b606-6d3a71b041cc | -8.12038 | -43.14143 | 2024-12-20 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7d4c383e-c694-3e7f-bf6d-c2c0ef4eba98 | -10.61139 | -37.00406 | 2024-12-20 03:49:00 | NPP-375D | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4533f51a-e375-31d4-bf1c-e1649901fa07 | -3.2366 | -46.79191 | 2024-12-20 03:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07c9f973-bdd1-36a2-a2db-3c2dffc82c91 | -10.45406 | -37.12056 | 2024-12-20 03:49:00 | NPP-375D | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 359ea57e-6232-3c4b-8fbc-903d6b52e09b | -11.87856 | -40.95436 | 2024-12-20 03:49:00 | NPP-375D | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f8f6c870-8e97-38c0-8eb5-b33bc3fa12b1 | -12.33607 | -43.67868 | 2024-12-20 03:49:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3c440a5-7984-328a-9ca0-34005a9200ce | -2.75795 | -45.55663 | 2024-12-20 03:49:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a185cdb-6108-37aa-8e47-d1bba1ad7fd8 | -2.7623 | -45.56014 | 2024-12-20 03:49:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed1d9639-854a-3171-b5b2-ea87ed88b934 | -3.21086 | -45.50909 | 2024-12-20 03:49:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac4a0185-58f7-33ac-b28d-aa843d2bf8a8 | -12.33672 | -43.67493 | 2024-12-20 03:49:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54fe1089-8eb2-33c8-bf82-acebebb42ed7 | -2.75678 | -45.55927 | 2024-12-20 03:49:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16200f7d-1a1b-3692-8722-1e8029047423 | -3.21027 | -45.51258 | 2024-12-20 03:49:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 508279e3-987f-3d3a-bfee-f22d3993caf6 | -9.1662 | -37.59256 | 2024-12-20 03:49:00 | NPP-375D | CANAPI | ALAGOAS | Brasil | 2701605 | 27 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9e32f926-3d00-37c9-8e0a-f9dc85c10835 | -3.71219 | -41.6952 | 2024-12-20 03:49:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 1d9a1322-db96-3d4b-a8bf-293403c8331e | -3.23518 | -46.80031 | 2024-12-20 03:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7034703d-a7fc-3854-9f96-10b44e714b2e | -10.14229 | -42.17014 | 2024-12-20 03:49:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a58dcfd3-f414-3162-ad05-6eefe1e6e9b0 | -9.9119 | -37.06426 | 2024-12-20 03:49:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 906b37dc-82b2-324c-bbaf-ae0f514aaa23 | -9.2215 | -60.3495 | 2024-12-20 03:50:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| be687333-c025-3543-8747-9b40998cbac5 | -9.2403 | -60.3292 | 2024-12-20 03:50:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 07ffb769-8de3-33cd-b496-d475fe86f895 | -12.5492 | -57.7594 | 2024-12-20 03:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 7925438e-4c4e-3b29-8395-5c80b870287c | -9.2216 | -60.3302 | 2024-12-20 03:50:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.2 |
| f7cd5260-048a-3350-97b2-7c86df41b5a7 | -20.97283 | -49.76091 | 2024-12-20 03:51:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 76a0d1ef-8c84-3ef0-832a-5ad49992e4e5 | -20.53014 | -43.9711 | 2024-12-20 03:51:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 9057f069-2a3e-36ae-91bb-db9cba190973 | -20.53163 | -43.96874 | 2024-12-20 03:51:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 15385305-2864-3d66-a60e-e442da81ed6f | -20.97356 | -49.75756 | 2024-12-20 03:51:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a7dd7eec-14e4-36a0-89a1-499296cb5973 | -22.67304 | -42.85772 | 2024-12-20 03:51:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c62364b6-ab36-371f-83d7-5b54d15f9e0a | -22.67649 | -42.85842 | 2024-12-20 03:51:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a03b7774-8289-300a-9119-a5c8348911dc | -17.75636 | -42.6965 | 2024-12-20 03:51:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ffdf98f1-2b4e-3ffc-8544-94894bd8966a | -20.90076 | -47.37921 | 2024-12-20 03:51:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25e26169-c25c-3144-bd89-2ef22f2477b6 | -19.32131 | -42.39169 | 2024-12-20 03:51:00 | NPP-375D | BELO ORIENTE | MINAS GERAIS | Brasil | 3106309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a1b57bc4-b424-3111-81f3-a7b49208cbc5 | -16.1464 | -40.36753 | 2024-12-20 03:51:00 | NPP-375D | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7d1d8c00-cc28-3468-8984-2e6c10a27a3b | -17.75176 | -42.89409 | 2024-12-20 03:51:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 936f792a-b136-37b3-833c-02c19a991d36 | -20.99092 | -49.0201 | 2024-12-20 03:51:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 74b27a2a-4fa1-3568-8d52-e84651fae781 | -20.99591 | -49.02117 | 2024-12-20 03:51:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 145c9d73-a02b-3a40-ba05-2bdd5b2f59c4 | -20.53383 | -43.97195 | 2024-12-20 03:51:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| dd2af0ac-b559-37a3-aaab-a3eeb39b3cd7 | -16.34878 | -43.69565 | 2024-12-20 03:51:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e379fab1-032a-3af8-8f09-453b873aae11 | -17.75541 | -42.89474 | 2024-12-20 03:51:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41f7fa06-aa43-3f1e-ae4f-fd3460d61738 | -20.90523 | -47.38031 | 2024-12-20 03:51:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4516c35d-5995-3773-b80e-97b169c1ba2d | -20.98963 | -49.02622 | 2024-12-20 03:51:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| a465256e-bd16-39c4-ab7f-0d3615e9258d | -19.28837 | -45.34128 | 2024-12-20 03:51:00 | NPP-375D | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 567e8d2e-6c4d-307b-9769-404a1d143e0c | -19.83931 | -40.08265 | 2024-12-20 03:51:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a4dcbe61-3e93-38ba-ac58-9c108e7961c5 | -20.53077 | -43.97342 | 2024-12-20 03:51:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 5df3dff6-f113-3c90-af7d-e1df68a0ce94 | -23.62254 | -47.05145 | 2024-12-20 03:53:00 | NPP-375D | VARGEM GRANDE PAULISTA | SÃO PAULO | Brasil | 3556453 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4a00a2c6-9f97-35ef-a105-670cf3151dcf | -23.58426 | -46.32026 | 2024-12-20 03:53:00 | NPP-375D | SUZANO | SÃO PAULO | Brasil | 3552502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d29becdb-e0c2-3988-817d-1fbfcf43b697 | -9.2216 | -60.3302 | 2024-12-20 04:00:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| a8e5601b-b392-3f15-911b-6d7ce11e04b6 | -3.232 | -46.8056 | 2024-12-20 04:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| b0c5e66b-442b-332e-adc6-56f03822e8b3 | -12.5682 | -57.7579 | 2024-12-20 04:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| f7856a91-0c9b-3b5e-b41c-6b0464d1992b | -12.5492 | -57.7594 | 2024-12-20 04:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 2670dd95-8ce8-3f13-b50d-a7771a2fda1f | -9.2215 | -60.3495 | 2024-12-20 04:00:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| c329f021-e256-3dc7-acef-9a5fe771d766 | -3.2321 | -46.7836 | 2024-12-20 04:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 68a480a0-38f3-3f01-8964-7726bb8b5a12 | -3.232 | -46.8056 | 2024-12-20 04:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| dca80a74-33b7-3d4c-9454-e40c6fee183d | -12.5492 | -57.7594 | 2024-12-20 04:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 9136bed3-5460-3441-9c71-0ede5f2ee3fd | -9.2215 | -60.3495 | 2024-12-20 04:10:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 607ae6b9-8615-3ae6-89f9-654f589497fa | -9.2401 | -60.3485 | 2024-12-20 04:10:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 0ccba2aa-004f-37ee-b683-acd60d29d1b2 | -9.2216 | -60.3302 | 2024-12-20 04:10:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 714201e7-9f6b-3a7c-beef-420cf243b962 | -12.5682 | -57.7579 | 2024-12-20 04:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| dc6400d0-a2d2-3053-8b32-b96b20b8a3ea | -9.2403 | -60.3292 | 2024-12-20 04:10:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 8c56dd71-43fe-335b-8607-54ebc5bce9d4 | -3.21184 | -45.50873 | 2024-12-20 04:10:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ac2bf24-9d92-3d1a-928b-e53e440610b8 | -3.22833 | -45.49852 | 2024-12-20 04:10:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README6.md)
