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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e026d2bb-9a2a-3cc4-82e2-f20ebdf1d00c | -8.07987 | -45.35575 | 2025-09-04 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 99d28c28-36d4-3f66-aa87-2e6d5309e591 | -8.89323 | -45.869 | 2025-09-04 03:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9d335e14-dcfb-3f98-9226-a2fb42ec7f16 | -11.90697 | -46.66447 | 2025-09-04 03:36:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6edc22cd-9800-3a31-94ef-add8a8fa5429 | -6.41417 | -43.26151 | 2025-09-04 03:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd422c39-e234-31dc-bd1e-bb5c937b7dfe | -11.05104 | -45.40571 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f5773ce4-d0b5-3af0-8ad6-43a5de8ad10b | -7.72311 | -44.61568 | 2025-09-04 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d3e61c6-2242-30e3-aa98-aad1b8c29157 | -6.79082 | -44.4895 | 2025-09-04 03:36:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b6b1de6-164b-3cc2-ba2d-e9d9eb72a679 | -6.78445 | -44.45723 | 2025-09-04 03:36:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5ae68b2b-9138-3942-9bbe-edb2e38fdb75 | -6.35258 | -43.76645 | 2025-09-04 03:36:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4395ed35-689d-362d-bb35-f7c53f7ff042 | -9.04211 | -47.02192 | 2025-09-04 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06137c19-f378-379f-beb2-713eb67c4922 | -7.04214 | -43.26729 | 2025-09-04 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 560dfa56-8249-3f75-99d5-c9c2a283edbd | -8.90947 | -45.87452 | 2025-09-04 03:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2a19b7c-0ecd-32e4-a6e2-6d93ec7bf9a5 | -11.03071 | -45.1398 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 8902e5ae-c470-3b3f-a672-b0162f9230c4 | -6.5438 | -42.95533 | 2025-09-04 03:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40448dff-aa63-3503-bd82-3352b43c384d | -7.36378 | -44.32454 | 2025-09-04 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f212760-4311-3f97-83b9-d846babc6984 | -11.92111 | -46.65826 | 2025-09-04 03:36:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e720315f-e74d-34a5-8d3e-5e8ae6a76aa1 | -10.65063 | -44.8428 | 2025-09-04 03:36:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 08d450b8-974a-33de-8b63-20958f0202a7 | -6.78493 | -44.09101 | 2025-09-04 03:36:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 9a92de67-f43f-380d-9311-ede6ab9268aa | -11.05051 | -45.40524 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3e137f9e-bfb1-3dee-b9f3-2e4caea2dc00 | -8.03726 | -45.38005 | 2025-09-04 03:36:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 44ede440-fecf-3a39-8901-8aa6a070e679 | -6.95298 | -44.95515 | 2025-09-04 03:36:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 930604ae-e29f-3615-a969-3acdb4038bd2 | -8.66548 | -36.23054 | 2025-09-04 03:36:00 | NOAA-20 | IBIRAJUBA | PERNAMBUCO | Brasil | 2606705 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 45c53cc2-7f6e-38df-9195-ef6c3b685568 | -11.91511 | -46.65611 | 2025-09-04 03:36:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d7a701a1-7b5e-3a22-b574-1ae60efdc8c1 | -8.07382 | -45.35284 | 2025-09-04 03:36:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3604b0c5-2e40-3712-96ac-7556e30f8233 | -7.04877 | -43.26812 | 2025-09-04 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a7bb9abe-5a71-36e9-8df9-ea1881949aaf | -11.24666 | -44.96113 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2418688a-d994-30e3-8671-f35826738536 | -6.50328 | -43.07601 | 2025-09-04 03:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0592eb4-5441-3188-8eec-9dbeff5fae66 | -11.04621 | -45.15168 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 58b1880b-c120-35c6-ac0b-d1c6fec1b3e7 | -11.24424 | -44.95978 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5260358e-db94-33d5-93b4-9871c0e19510 | -8.023 | -44.12052 | 2025-09-04 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14d7fb8b-f134-3cc9-abf1-ab24a3f1efa1 | -7.50242 | -37.37134 | 2025-09-04 03:36:00 | NOAA-20 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1497cc22-cb31-38d5-8e74-5bec485b5561 | -11.77699 | -47.32946 | 2025-09-04 03:36:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9e5cac8-a802-3ce0-bf3a-fe3f5ce5cace | -6.78276 | -44.09909 | 2025-09-04 03:36:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5f9cfa3c-f751-3fa9-afa2-35bdd17c26c2 | -7.93466 | -44.95192 | 2025-09-04 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 06a928a3-0370-3743-b0d4-00d78f1b7c37 | -6.54855 | -42.95972 | 2025-09-04 03:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bdff7cec-c32f-311a-8add-a3e306e0670a | -6.78989 | -44.09232 | 2025-09-04 03:36:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| d6148602-04ac-3bb6-9722-ed2bd77f3050 | -6.48857 | -44.10829 | 2025-09-04 03:36:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0d3757c8-9ee3-3b05-bdbb-e704da1122af | -6.71918 | -42.24675 | 2025-09-04 03:36:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1cb16fda-3922-37a3-96bb-8361bd268548 | -6.27407 | -44.51358 | 2025-09-04 03:36:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87d58f2e-6863-3de6-b67b-73eb394c6e65 | -7.69113 | -37.5606 | 2025-09-04 03:36:00 | NOAA-20 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9f6b60c1-7840-3435-a274-27e6a0e286e7 | -10.98196 | -46.8349 | 2025-09-04 03:36:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| db3e35be-6f4d-3748-95b2-f06c4f6a1477 | -11.38781 | -43.56423 | 2025-09-04 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 484a7f82-a393-3d83-ac2d-93cf7a5b6325 | -8.09165 | -42.42904 | 2025-09-04 03:36:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 17c543f8-c322-350c-aeb9-3abcc5fa14d9 | -6.03047 | -46.6819 | 2025-09-04 03:36:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 618ec611-9174-3018-97f7-a6e863712911 | -6.54915 | -42.95638 | 2025-09-04 03:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49a23572-3778-3ef0-b694-7426dbab4339 | -7.97182 | -46.3446 | 2025-09-04 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 277739cd-390d-3cc3-bcd1-5bc78a1a1ca0 | -7.93266 | -44.94753 | 2025-09-04 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 584b2472-99ee-3cfd-9dc9-3679c4534042 | -11.04966 | -45.40948 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4c032c91-7cea-3b08-a1c4-d2bacec5abcb | -11.90803 | -46.65927 | 2025-09-04 03:36:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 438b39f2-3bc1-3076-bd30-e53fa62d6d2a | -6.79058 | -44.08839 | 2025-09-04 03:36:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| a88b9610-359c-3110-9843-1924bdb8b6ab | -6.79067 | -44.09214 | 2025-09-04 03:36:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| d52fa3ef-bd52-3fbe-bf8d-60091cfe11ba | -8.03716 | -45.38094 | 2025-09-04 03:36:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9edf0016-6e78-39a1-bda6-5c3c3c141af7 | -6.7868 | -44.44415 | 2025-09-04 03:36:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c92bea19-cd11-3b39-8832-1ac2b9a27707 | -8.02583 | -44.07317 | 2025-09-04 03:36:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49ad74e6-f680-3546-9ca3-ca0696d6cb25 | -6.8388 | -46.39391 | 2025-09-04 03:36:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 829f6dd6-5794-33ec-b013-b6af11c4d2cf | -7.93733 | -44.9377 | 2025-09-04 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 99d230ad-297b-35bd-a8ca-2e203a544a7d | -9.47127 | -47.60884 | 2025-09-04 03:36:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b594030d-b48c-3849-84b0-97463188a1ac | -11.03556 | -45.14536 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f224234f-0b2a-3287-bf92-7a3ff089e4e8 | -11.04444 | -45.40864 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a655001-d4ae-3538-87c7-6e2e6ab60c2c | -8.47009 | -45.06322 | 2025-09-04 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 517fccf7-6051-380f-a3c6-9deda94a5b12 | -8.0363 | -45.38543 | 2025-09-04 03:36:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dfe73158-04df-3bf3-a274-39f5c7784f02 | -11.04779 | -45.14356 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 20e09fa2-ea6a-37f3-b439-fe819d61e4a4 | -9.82328 | -47.8155 | 2025-09-04 03:36:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33617e67-a8a5-39ad-b736-a679ceb4cdc6 | -11.59648 | -47.78129 | 2025-09-04 03:36:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 8399dcaf-9fe2-30a9-8985-87341931d6e2 | -6.7385 | -42.25658 | 2025-09-04 03:36:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d22ad4ad-65d1-32a4-bc78-5b4cab776db2 | -6.33381 | -45.65254 | 2025-09-04 03:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bbb6a6f9-2b9a-39e2-81dd-aaf5263694bb | -11.91013 | -46.6564 | 2025-09-04 03:36:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8b7e4cb9-ef5b-3c59-9cb1-c050fd684237 | -8.60681 | -40.30922 | 2025-09-04 03:36:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3fb36ad4-4fa3-3d02-a230-47a496d2807a | -9.49786 | -43.16783 | 2025-09-04 03:36:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6401a389-0de8-3a28-bf59-85f412ed22e5 | -7.93378 | -44.95664 | 2025-09-04 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7763328c-311d-330a-accd-a54db3a24d06 | -6.3468 | -43.76604 | 2025-09-04 03:36:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8754ab2c-4fbc-31e7-aefa-3e87a83cd71b | -6.40804 | -43.26413 | 2025-09-04 03:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f3be9459-7cf4-3ac3-8d1d-baeeb63577bf | -7.04334 | -43.26714 | 2025-09-04 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7daf4acc-e057-3656-9e7e-098a8ad93ffa | -7.06898 | -46.19882 | 2025-09-04 03:36:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ad0b7bbd-d74a-3900-aa9c-f6948c49728a | -9.04003 | -47.01822 | 2025-09-04 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b6e60f27-616f-30c8-8511-9918477b94f9 | -8.00904 | -44.78304 | 2025-09-04 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b7591e7d-3449-36de-9ff6-f7a4b6b6ae79 | -11.91409 | -46.66111 | 2025-09-04 03:36:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e573b6b8-e9a1-3cd8-9ff5-d0859b391959 | -8.05183 | -44.13751 | 2025-09-04 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a2c9af2b-6acb-34c1-bd61-618e8e401d60 | -11.9664 | -45.78613 | 2025-09-04 03:36:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf04a67d-9311-37f3-80ca-2f37a13eef5c | -6.41355 | -43.26501 | 2025-09-04 03:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a516fd82-4560-392a-baa5-0272c3c66fa7 | -6.77845 | -44.09396 | 2025-09-04 03:36:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 7921fc7f-d631-3b26-b611-57c540d123f4 | -6.78759 | -44.43975 | 2025-09-04 03:36:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 347c1f64-d19e-3327-874b-d784f7baa4f0 | -8.06791 | -45.35222 | 2025-09-04 03:36:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 119a9013-8d06-329b-8a01-80180fd42ef0 | -10.9909 | -45.92149 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d871b4b3-6df6-3249-b26f-6ea8a583a95a | -6.54185 | -42.95056 | 2025-09-04 03:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2be99b2-5c8f-30e9-bd34-ff2f0fbcaf54 | -8.60213 | -39.52951 | 2025-09-04 03:36:00 | NOAA-20 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8981f992-ac78-3e46-9b34-1c9b74e29139 | -6.78484 | -44.08727 | 2025-09-04 03:36:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| e4bd93dc-0ae4-3ada-8803-beac1fd64093 | -6.34203 | -45.67982 | 2025-09-04 03:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a0fb1604-340e-3d28-b0cb-5760d3ad72a7 | -8.89425 | -45.86362 | 2025-09-04 03:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 6d1c718e-c818-3879-b54c-b178639c4b85 | -10.9808 | -46.84078 | 2025-09-04 03:36:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 82d4e72b-7e17-351a-8219-252cb02e5f2e | -7.1557 | -45.22872 | 2025-09-04 03:36:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4183464a-843a-38ea-b1f3-38c7f14d4ccf | -11.76278 | -44.65489 | 2025-09-04 03:36:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1270e99a-2c8f-3b5e-8adc-89c344f5e23a | -8.08457 | -47.5943 | 2025-09-04 03:36:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37caed6c-c573-320b-8106-8d1ae2c19890 | -6.34115 | -45.68465 | 2025-09-04 03:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d21cd868-7869-3b81-b0f8-137e26e11cf4 | -8.05485 | -44.13796 | 2025-09-04 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5e2bd243-3019-3dab-b447-7c2be9e7c9d9 | -6.79165 | -44.48486 | 2025-09-04 03:36:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2973f2ef-c5c7-3746-bdfd-bd2a02b3ffde | -7.97072 | -46.35029 | 2025-09-04 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f912df5-5e13-3831-b4b7-fa0f888995a2 | -8.03656 | -44.14225 | 2025-09-04 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4beee657-0279-3d41-ab09-2615d195dc05 | -6.59504 | -44.31509 | 2025-09-04 03:36:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d5354c1-bf82-31f1-a6b1-cce6591ae73f | -10.05824 | -46.22602 | 2025-09-04 03:36:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README19.md)
