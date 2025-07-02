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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53133674-b102-3cf1-a168-87bfe88dc452 | -7.21534 | -43.08868 | 2025-07-02 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| aef6a17c-a7b0-3e7c-8698-4627fcd0f6c3 | -7.79852 | -44.02353 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5eba5912-1c86-380d-92f4-4b6395831f06 | -7.79581 | -44.01883 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4c3ea1a7-9fad-3175-b161-04b2522265a7 | -9.84681 | -44.70007 | 2025-07-02 03:36:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6dca723d-411c-3545-8d99-c41e0c870b82 | -7.60718 | -45.77654 | 2025-07-02 03:36:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0ed060ee-8e1d-3650-a33e-bbfb15bab426 | -7.21153 | -43.09154 | 2025-07-02 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| a4a276ee-c0a8-3ac8-a9f4-f1baac6fe926 | -7.20816 | -43.09779 | 2025-07-02 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d33737f3-dcc3-3fbd-88ac-c258c2cc4a40 | -7.21568 | -43.09922 | 2025-07-02 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9a7400e8-f961-3817-8a3d-1e826560a098 | -7.81196 | -44.02575 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4587994c-1a85-3098-aed0-31d8bc66e6cd | -8.10166 | -42.99947 | 2025-07-02 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5b4c41b0-efc3-3f2c-8ec8-d126f9555e79 | -7.21945 | -43.09629 | 2025-07-02 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 48ed4298-8095-3631-87ea-e7c5675b637c | -7.81128 | -44.02958 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d3295220-2049-363c-816e-56b49cd7e6ee | -7.77899 | -44.01572 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 33e58baa-4696-3ecb-82ca-7e027b97363b | -8.53931 | -46.34225 | 2025-07-02 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a376faee-196d-31d9-8904-901892d5cf30 | -11.88023 | -40.95423 | 2025-07-02 03:36:00 | NOAA-20 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 73ce7fdd-d045-35dc-881f-d6bdfef71d63 | -10.64355 | -44.4913 | 2025-07-02 03:36:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a2a30fe-d198-37c6-93f9-35bdada8d4da | -10.69368 | -44.49765 | 2025-07-02 03:36:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f053c226-e706-3ea9-8bd3-5185d5a56694 | -7.21062 | -43.08439 | 2025-07-02 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 64b68f16-fc3d-380f-965b-8e1bbb4a6ee6 | -7.81263 | -44.02194 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ce485e5b-bf74-3a2f-b60f-3387c9880f9d | -9.79399 | -47.75294 | 2025-07-02 03:36:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b726440c-58ff-3090-87db-0a0040b20b9f | -7.80635 | -44.02472 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 25.7 |
| c6854021-d8fc-3f9a-b3bf-fc2b9c692fd2 | -7.80073 | -44.0237 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 4a4f74ce-ea00-3547-8194-c57eecc2d528 | -7.2127 | -43.08487 | 2025-07-02 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| df980ac0-a96d-3f13-a987-77c97bb37fc6 | -7.59992 | -45.78054 | 2025-07-02 03:36:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0bb81f8f-bbc4-3817-8da2-627539d1c300 | -9.79528 | -47.74633 | 2025-07-02 03:36:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 718ca75b-81df-3ba6-8eca-a7d2011d83d4 | -12.10546 | -43.65226 | 2025-07-02 03:36:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aafa0d9c-fa5d-35b3-9e17-688bdcbbdd5a | -7.79781 | -44.02736 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8557cfb7-a69d-3626-9d4e-ed42254c3dab | -7.81045 | -44.02174 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 3fd2fcc3-13e8-3697-873f-36692747a7a1 | -7.20264 | -43.07952 | 2025-07-02 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 1a690108-2182-33fe-8e61-122ce1ff3ff2 | -11.14478 | -43.33357 | 2025-07-02 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d013ede0-a7a9-3dbd-be66-1fe2c5a97255 | -7.21035 | -43.09827 | 2025-07-02 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| de6b5c46-4ce6-32f3-9f2c-7d2da99e67ed | -10.64426 | -44.48767 | 2025-07-02 03:36:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1b04d86-d7e3-3baf-9535-376c488f8bbc | -7.79924 | -44.0197 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 29.2 |
| ef716bdd-b91e-37bd-a9e4-626dad4db787 | -7.2135 | -43.09873 | 2025-07-02 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7bbf5626-c6f1-36d8-8b87-9ac6421f3b99 | -7.80903 | -44.02936 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 0e2a9e16-f26b-3426-b322-73f9a78e06da | -7.20796 | -43.08052 | 2025-07-02 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 31755aa5-fd00-36f5-8cef-7fe120cfdc93 | -7.79995 | -44.01589 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 4e210801-1b16-3318-9407-c420b5334be1 | -11.31121 | -46.19535 | 2025-07-02 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2288422d-3819-3a7d-82d1-378587d30ed3 | -11.13972 | -43.3326 | 2025-07-02 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ba542537-2e67-38ca-a50d-fbcc07a48e37 | -7.21883 | -43.09968 | 2025-07-02 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 408abfbe-5332-3c9a-8ee3-5d3bd2448eb0 | -7.22161 | -43.09679 | 2025-07-02 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e8bc619c-c207-3a8b-835c-9d8996801722 | -11.30409 | -46.19949 | 2025-07-02 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| aeaa15ee-fd94-393e-9e88-fd8d9932ee7c | -7.21686 | -43.09248 | 2025-07-02 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 4080d592-0059-3122-b9dd-5bda42699cf8 | -12.11112 | -43.6502 | 2025-07-02 03:36:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbabb3b4-6522-3221-aa78-38f389d026bb | -7.20205 | -43.08286 | 2025-07-02 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 3fe42911-8368-3d1c-b196-487831f3e3b7 | -7.79363 | -44.01869 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 1c1290e6-3943-3f7b-88d6-68074f33b141 | -7.8021 | -44.01604 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 99752da0-f845-3a23-9f61-944aa7191461 | -11.83856 | -43.80077 | 2025-07-02 03:36:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1bb7384c-4b72-395e-afac-940d0dfa8c49 | -7.2094 | -43.09106 | 2025-07-02 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 2db1be53-a062-3a89-a37a-5d299ce376e8 | -10.69298 | -44.50134 | 2025-07-02 03:36:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7532c606-9a4b-3904-8287-0b98d0cc37a6 | -7.78391 | -44.0206 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b187b984-d6cf-3f01-a7c7-64d43825e99a | -7.80005 | -44.02753 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 00554a92-e5fe-36f8-84a5-13db23bdec0d | -7.80484 | -44.02072 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 0ea1de82-28b3-312b-b92b-2906b67bf55c | -7.21094 | -43.09489 | 2025-07-02 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| b65a9c0d-04b4-35f2-bb6b-81a6808ec8cc | -7.21412 | -43.09536 | 2025-07-02 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| c1579880-c89c-3155-a679-a346ed614351 | -7.81465 | -44.03038 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 62be53f7-0b49-3876-a4eb-5b1084302634 | -7.80342 | -44.02836 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 54d14654-c38d-3e0c-abfa-620efcc8211f | -9.79616 | -47.74667 | 2025-07-02 03:36:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a09c3294-4ef9-3317-a30e-ebc032f84813 | -7.22006 | -43.09294 | 2025-07-02 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7ee851a6-fe5b-3d2f-bba0-d8881e5019da | -7.7965 | -44.01501 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ef244437-42e8-3369-8e9b-dc1e322abd57 | -11.8431 | -43.80492 | 2025-07-02 03:36:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5700f20c-a391-3940-b61c-0f92fc1d5ca1 | -7.7846 | -44.01676 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1c8fb9a1-113e-34cf-84dc-397db12a3865 | -7.80066 | -44.01208 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| ae2d74e8-2408-3e5c-98fb-f35f406c150a | -7.59363 | -45.77939 | 2025-07-02 03:36:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e46a4ae-5bbb-30f0-a7df-a50bc78c2b02 | -11.83668 | -43.8032 | 2025-07-02 03:36:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e9e5289-2e4f-385e-8567-5670141e9cc3 | -15.92605 | -43.51891 | 2025-07-02 03:38:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2a7d39f1-9729-36ab-89b3-e308282ba5c9 | -17.48969 | -46.74333 | 2025-07-02 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5542e265-b102-3394-a394-c0f17e692070 | -15.92399 | -43.52146 | 2025-07-02 03:38:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f1dc9415-1a7d-31f6-92cf-46a51d3f6ce8 | -15.92707 | -43.51371 | 2025-07-02 03:38:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c78d6bc-1b8d-3ff0-b5ad-75d100fed50a | -20.23446 | -41.88487 | 2025-07-02 03:38:00 | NOAA-20 | MARTINS SOARES | MINAS GERAIS | Brasil | 3140530 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f60ac23e-e827-313d-a63b-9a55755240c7 | -18.96319 | -39.91683 | 2025-07-02 03:38:00 | NOAA-20 | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1db23461-9c29-312b-8bd7-3a174a44ed8d | -16.7727 | -42.78984 | 2025-07-02 03:38:00 | NOAA-20 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2735f636-9a51-339e-a6b3-e679226694e1 | -13.40926 | -47.82508 | 2025-07-02 03:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fd3d4e44-8c97-39f2-9961-f5f5aeeb44da | -17.09252 | -43.80243 | 2025-07-02 03:38:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba039772-d9ac-3cae-9e27-208070d6644b | -13.36385 | -46.19242 | 2025-07-02 03:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c860fb66-812f-386c-addc-0e6ce42f5a97 | -16.77709 | -42.79082 | 2025-07-02 03:38:00 | NOAA-20 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9836d2bc-0635-3720-9455-af61ce67a8c7 | -13.40931 | -47.82637 | 2025-07-02 03:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2f65d93b-7149-3eb7-8c07-52d22f0eaacd | -19.4348 | -48.54726 | 2025-07-02 03:38:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 14909c28-e423-3551-ac08-a961092d1f7b | -17.91836 | -45.55803 | 2025-07-02 03:38:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e098fc56-de32-3617-938c-00455505cf81 | -14.44573 | -48.86973 | 2025-07-02 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cb6c0233-17ad-36d0-a11a-a74f2d50700d | -16.42061 | -46.55123 | 2025-07-02 03:38:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11a75650-6900-38f2-aa26-07d985e4b689 | -15.52908 | -50.00027 | 2025-07-02 03:38:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 197a8a20-3766-3644-a93c-c67f4d93e0e9 | -16.42488 | -44.5245 | 2025-07-02 03:38:00 | NOAA-20 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85fd7b5e-6ee5-3000-b6d6-1c328a73774f | -16.4211 | -44.51757 | 2025-07-02 03:38:00 | NOAA-20 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59f1e810-19ae-3e77-a990-9b5b1e3949a2 | -17.21842 | -44.80459 | 2025-07-02 03:38:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c93897b7-387b-366e-bee1-de5334ba98eb | -15.92136 | -43.51794 | 2025-07-02 03:38:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b2e651fd-f00d-39b1-bc1b-9044ebe049dc | -16.6023 | -44.51567 | 2025-07-02 03:38:00 | NOAA-20 | SÃO JOÃO DO PACUÍ | MINAS GERAIS | Brasil | 3162658 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a425ba92-9222-38e6-a3d4-1ff2d08e9983 | -13.35801 | -46.19121 | 2025-07-02 03:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 045da407-8aa4-371e-9484-45b357c5b835 | -19.43793 | -48.55464 | 2025-07-02 03:38:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5f390d7a-ab5e-3e3e-b7a3-95698057f94a | -19.52163 | -43.60426 | 2025-07-02 03:38:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f1a29d9a-b8c7-3b6a-8d3b-6b6f9a27ca7e | -14.90518 | -45.14142 | 2025-07-02 03:38:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2b877d3-e218-3600-b85f-51a206433a68 | -15.92498 | -43.51625 | 2025-07-02 03:38:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| bd9c34b7-422a-3c7f-b88c-b96279922880 | -14.8992 | -45.14369 | 2025-07-02 03:38:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47f3e7b5-9107-3781-ae2c-de0815e5b1e0 | -19.43192 | -48.55324 | 2025-07-02 03:38:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 00146a22-c171-3a41-87eb-06423d88035b | -13.36294 | -46.19685 | 2025-07-02 03:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5de23c1c-ffdf-3cf9-9473-ea470f1666a8 | -19.43369 | -48.55209 | 2025-07-02 03:38:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fadcd7d4-8321-3467-8f06-5ada2d3d4c5e | -19.5226 | -43.59938 | 2025-07-02 03:38:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8b0e69a0-c7b3-3dac-a163-202bee971fe0 | -16.60267 | -44.5175 | 2025-07-02 03:38:00 | NOAA-20 | SÃO JOÃO DO PACUÍ | MINAS GERAIS | Brasil | 3162658 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db00e451-ce0d-39c9-8a1b-696258f9fd02 | -19.44072 | -48.549 | 2025-07-02 03:38:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 93292975-ef2e-3528-9080-1cc8c61810d4 | -19.51822 | -43.59827 | 2025-07-02 03:38:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README7.md)
