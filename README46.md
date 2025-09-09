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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90cf31d0-1003-379c-9fd7-d614952a1af5 | -6.54208 | -54.99058 | 2025-09-09 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c4be7dab-97f6-3223-bcd3-b44578638a40 | -13.80628 | -46.28528 | 2025-09-09 04:34:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 66fdbdbe-4ade-3654-bb88-b026371891c6 | -7.46978 | -45.18922 | 2025-09-09 04:34:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 23f9fe1e-3802-389a-9933-26a877851c9d | -7.78867 | -46.08612 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ae07817e-324b-35e6-9f5e-14460e120a06 | -13.00634 | -45.2135 | 2025-09-09 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e9e9e0bf-ddcd-3807-9b68-582901fc3df6 | -13.00997 | -54.81426 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b95c81f5-f8d2-3e58-ae93-f55e9bca058a | -8.04668 | -48.64192 | 2025-09-09 04:34:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8456c76a-a2a4-3e5b-89bd-e87c6d8e3bb0 | -6.86581 | -47.90497 | 2025-09-09 04:34:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 162c1da8-4438-3b61-ba43-848432d38573 | -11.31614 | -55.11817 | 2025-09-09 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47097c39-818b-3d5b-b8b5-3557babd0a60 | -12.63768 | -56.97394 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5bd8f38b-0513-3a19-9e65-4c12d1f912b1 | -8.42959 | -47.29107 | 2025-09-09 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b2d84ea6-c637-3051-957d-f818f944d601 | -10.71765 | -48.57023 | 2025-09-09 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04fd4a63-568a-3bc9-a87c-b10922abb5e8 | -10.9712 | -45.11683 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 90532816-7a3b-363c-8060-db768c05295b | -12.83809 | -52.93648 | 2025-09-09 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c796ebf-c4ee-3bab-8c3c-a3724762b8a1 | -9.55222 | -48.66994 | 2025-09-09 04:34:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 877a7634-fb19-338a-b1ee-aae815fc0500 | -7.65319 | -48.00159 | 2025-09-09 04:34:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 05deec9a-93a3-3d90-9e7f-5649b20941e5 | -9.18613 | -59.37257 | 2025-09-09 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08d4035e-20cf-32c6-95fa-ec0b6f924566 | -10.48083 | -49.77358 | 2025-09-09 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8cc5630-8e10-38e3-afdd-d58e1d672db2 | -9.94358 | -60.12955 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 473f380f-b390-3bb2-ae05-502c608744d6 | -8.06869 | -48.65254 | 2025-09-09 04:34:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 652138ad-0c81-3a71-86c0-441748ba7617 | -10.80914 | -48.28607 | 2025-09-09 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 497b48dc-6b4e-321b-bdd9-b88d96812432 | -8.37395 | -45.02833 | 2025-09-09 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c5ef9af9-18df-3080-9831-d9857404b0b5 | -14.21145 | -42.07978 | 2025-09-09 04:34:00 | NOAA-21 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ae4e1865-a48f-3b3a-bfd1-64177bd7b5f6 | -10.77325 | -47.72282 | 2025-09-09 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b664178e-6ee1-33bd-8a06-7aebf5ae4171 | -12.6189 | -56.97029 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| aada1c65-a6b9-3900-8887-7b23531b7279 | -11.18425 | -48.38913 | 2025-09-09 04:34:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04a1bef3-c5dd-3ed0-9ce4-325bdcc48666 | -10.83872 | -47.26987 | 2025-09-09 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e824c504-f281-39f7-a435-7c88daff1b5e | -10.97571 | -45.12027 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d664eb7-390f-36a9-9edc-491bcce74629 | -6.1828 | -53.26423 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71f7f1d9-c0fa-33b4-b4a8-dd93315554b4 | -9.70643 | -46.80663 | 2025-09-09 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b9886c7-61e0-3b90-b89d-d54ba93290e8 | -11.33346 | -46.55855 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 912fd04f-bcac-3e13-89c3-eb7ac723a48f | -10.09314 | -59.17674 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38638b6b-e0f3-39c1-a06d-0fb4b525ec54 | -14.41436 | -48.46311 | 2025-09-09 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0b5561d2-fa53-3c80-af21-2958fa315c9f | -12.9061 | -47.99635 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0a35381c-88a6-3ead-8905-b851bab9fec0 | -10.96678 | -45.12086 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 914e9b82-4f87-3752-80e9-a505ae09df3d | -11.42818 | -43.6096 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b71501a9-2360-3a57-80ec-3b66752269f4 | -11.84188 | -46.76767 | 2025-09-09 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e26d5bf6-5e40-374a-b846-61aefe7e3d16 | -7.70412 | -45.16158 | 2025-09-09 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9f08f2d-13be-3754-93f7-376a20226c9a | -9.25204 | -57.06716 | 2025-09-09 04:34:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcab272a-5530-369c-9c43-44613ba98f0f | -12.82859 | -52.9482 | 2025-09-09 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8538db68-0329-3263-80bf-3f2f33c892b1 | -11.39339 | -43.53917 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba437704-ad59-38bc-b941-442dc297e242 | -12.51708 | -45.2908 | 2025-09-09 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10451375-8a81-3fd8-b6b1-c557536e4d46 | -11.81452 | -46.75982 | 2025-09-09 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd8e907f-f2e9-3916-ae90-52d51d3d83d9 | -7.99988 | -46.3382 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5d5b6e7f-7242-3e15-b74e-d3922b567080 | -13.54814 | -48.20017 | 2025-09-09 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75952b76-f966-3b9b-97ba-eff956b884aa | -9.43747 | -60.5163 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5256a724-64ff-3908-a8c7-8bda1339a70a | -10.15791 | -46.20856 | 2025-09-09 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0e16edc8-cd3b-3edc-863e-b81c78e56ca3 | -12.19927 | -53.89925 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d70a1413-68ef-31ff-93e6-bf907186c030 | -9.44276 | -60.52243 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c640aeca-8720-3295-87c3-08961822af44 | -13.54478 | -48.19963 | 2025-09-09 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85193530-2a65-305f-b4c9-67bc70b300b8 | -7.71528 | -44.75089 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6bf8b5c7-3599-3189-ba29-87c55359f6ab | -9.01354 | -49.79798 | 2025-09-09 04:34:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ada7c50e-3ed5-3292-af3a-cfff75a3a79f | -7.66256 | -50.29148 | 2025-09-09 04:34:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d7c92b28-2330-3b40-ba8e-71f91eab4fea | -12.61793 | -56.97539 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0270c92-201b-3a88-a688-02e54fd39a80 | -14.3801 | -44.64878 | 2025-09-09 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43a90c67-7398-3cc8-8c15-f353ce5b2d94 | -12.02644 | -51.07877 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3d5ce69-f318-396e-9e75-15feff891552 | -12.96023 | -54.76368 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 368daace-5f44-39e3-9caf-260d43cdda55 | -11.3054 | -46.5052 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8388d757-2889-36b1-bd98-5df0fafe52a6 | -8.46526 | -47.30395 | 2025-09-09 04:34:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 55a56c85-d9d7-34ab-ac78-9af2551be435 | -7.79501 | -46.091 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d81ae1b-e7e0-3fce-a701-720a0c36c9fa | -10.78854 | -49.72237 | 2025-09-09 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7bc16f09-7e2e-3a6b-b263-04fd03aad1b1 | -7.94658 | -44.83148 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8024de1-f819-3492-8b95-08df74b8b127 | -12.9494 | -54.75418 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8c707d7f-0eb7-3ff0-b924-4e7d1380d83f | -13.13067 | -54.91267 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2128ada9-37b9-38b0-81f4-68a44b7d5eea | -8.04329 | -45.48983 | 2025-09-09 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed79cbad-2958-3292-a3f2-8321c62636b2 | -9.5009 | -48.27978 | 2025-09-09 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 730e0089-d888-3ea0-9b9c-8b8f6e570bdc | -12.15503 | -49.08131 | 2025-09-09 04:34:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04d3fecb-14a6-3f04-9ed5-10ddd2ad5543 | -6.26946 | -53.42371 | 2025-09-09 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2103bb04-f492-3bad-a70c-7e1603b3b40c | -9.79523 | -46.23991 | 2025-09-09 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ead8a534-3076-36d3-ac70-133d663ce91b | -11.81272 | -46.76074 | 2025-09-09 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3eab6d47-a4bf-357f-9846-7321303b0ea4 | -11.29267 | -46.48808 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be4acd1e-d700-3392-a4ad-b9c29c57f306 | -12.93599 | -54.75922 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad435e5b-aeed-3d44-bd1a-b60275b19467 | -12.03479 | -51.09165 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae63a3a1-ad12-3a21-9014-d78b360fafc0 | -9.8483 | -47.79115 | 2025-09-09 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ecae454d-6d6a-36d1-a258-0a1846aeb7b2 | -12.94003 | -54.75995 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f82bb01f-6b13-3a6b-ac7f-c862485c5769 | -8.37411 | -45.02535 | 2025-09-09 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| decc223d-d077-3dcd-aea4-4b528abe02ce | -12.8684 | -47.97183 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7fda0dcf-1983-3455-b260-fa17f14acc6f | -14.3371 | -47.308 | 2025-09-09 04:34:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6af9bfe3-a8e1-3340-b2e2-376a9fce65e2 | -9.22515 | -60.8229 | 2025-09-09 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6b5b1e0c-0e6d-3d52-ba8c-1445072dbae1 | -12.54939 | -49.10515 | 2025-09-09 04:34:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57cde44b-926e-3291-97dd-c868054ca7db | -12.93753 | -54.79729 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf9ade7d-3232-3d97-9a74-437b1ac17b7f | -12.83661 | -52.94515 | 2025-09-09 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5ae730c5-f41f-35a2-8ac7-8e3e75358638 | -12.92867 | -54.77673 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e244a888-2e89-387f-ab13-ab44ccbb728f | -8.33482 | -45.06385 | 2025-09-09 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd93e76a-7e2a-3368-a4d6-8de82a688e4a | -7.90846 | -46.85103 | 2025-09-09 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8918dad5-b37e-3110-b64d-35e1dae4ee3e | -10.27866 | -48.81118 | 2025-09-09 04:34:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3b92c2a4-070b-3b7d-b782-9412298468d9 | -13.96271 | -48.24234 | 2025-09-09 04:34:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee7eb12c-be98-36c8-951c-9a69240c0dd6 | -9.87096 | -46.52921 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a67c7f3-b4fa-3b7b-bb71-f212efc1168f | -11.86077 | -47.53771 | 2025-09-09 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 35e47699-956e-3f13-8672-18263e8ea66e | -11.37311 | -43.53231 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28b3e2d5-7982-39a6-a1dd-cd0721a81e13 | -11.98642 | -51.01904 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7f80286-b464-3d0b-9c0c-04c0c3d08c08 | -8.06206 | -48.63016 | 2025-09-09 04:34:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2b45a07-b6b1-3794-9291-4c5fca0a6987 | -11.60305 | -52.20577 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 95748102-12f7-32b9-8104-f63da80ce2ae | -8.03424 | -44.02708 | 2025-09-09 04:34:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3209363d-9f16-370b-8f29-5faf5814fed7 | -13.74855 | -46.91004 | 2025-09-09 04:34:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5d9916f-9087-3a49-a112-6f299be0a0ba | -11.24664 | -49.40781 | 2025-09-09 04:34:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 509f966b-979a-3bd1-9b5b-0872c4b3e257 | -8.20345 | -47.16833 | 2025-09-09 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c1406b84-b26a-32f2-98d9-cdf2640a26c2 | -8.03611 | -48.64029 | 2025-09-09 04:34:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae4f004d-a16b-3fea-8dbb-9e4cca67234f | -11.44373 | -43.65047 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a9fcd09d-f49e-3f47-9a2e-7b22a39d1e07 | -10.96813 | -45.11166 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |


[Clique aqui para ver as próximas entradas](README47.md)
