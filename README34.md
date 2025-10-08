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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70dcd5f9-2cf1-3411-a2fe-d6fe2abf132d | -12.21599 | -44.25772 | 2025-10-08 04:17:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ac992019-3f95-3acf-a31a-14958139fa92 | -2.78971 | -49.61977 | 2025-10-08 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c60f7619-f339-33c6-a862-391193202bbc | -11.17834 | -54.88193 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 559199ea-b7a1-366d-9cc2-6e3f00ff31d0 | -0.90496 | -47.54715 | 2025-10-08 04:17:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3c60abaa-9753-33ea-bb3c-c88919b2e7e3 | -7.44643 | -43.15157 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e47c0f09-59f0-33ec-b2ed-c46e6a20df98 | -3.10867 | -47.79442 | 2025-10-08 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1a55680a-ed5a-3d95-84fc-09801fe08468 | -10.42579 | -45.38432 | 2025-10-08 04:17:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd593f78-3f0d-39ff-8737-d9cb812f350d | -5.40398 | -46.22575 | 2025-10-08 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 30811368-597a-3fec-96ec-971d1d66224d | -4.68615 | -45.84824 | 2025-10-08 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7221faae-826c-3d9f-a810-6eeb60994d61 | -7.02396 | -42.88854 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| da55fa43-33da-3eb4-a20f-4dddc8541fd7 | -5.03583 | -43.60843 | 2025-10-08 04:17:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9dc447a7-e431-3e29-a6ba-344f5a47e1c9 | -4.01703 | -48.96717 | 2025-10-08 04:17:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d595151-65c4-359f-9be6-9a9c90a6b612 | -11.16921 | -54.86721 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ede7006b-d6ff-3345-b7bd-5b4a38d99d95 | -7.00786 | -42.88241 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 9c01cb87-eb03-3cfc-9399-d261e88ef279 | -6.42287 | -47.23648 | 2025-10-08 04:17:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ea40e92b-f83f-302f-a705-092534637c9c | -10.61112 | -48.67785 | 2025-10-08 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fa78baf6-b1d2-3bbf-ac3b-c13f486cd3fd | -11.17502 | -54.86832 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f44a58a6-1eb4-331d-8378-0903a51aa44a | -11.88438 | -44.96152 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cff9b69b-dd9b-3048-aec2-2d504cba1648 | -12.15639 | -51.4433 | 2025-10-08 04:17:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 591d2e80-314f-3baa-8bce-08668014add5 | -13.23433 | -47.79082 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20695b3f-3082-358e-9c89-eaad8aaec0fe | -2.51625 | -51.92881 | 2025-10-08 04:17:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83c30105-5410-35c0-bd68-5f88b5dff604 | -4.05163 | -42.52071 | 2025-10-08 04:17:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 68a2856f-9a04-3605-ab53-bf158eabe627 | -4.68684 | -45.84404 | 2025-10-08 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1c9f2dcc-a122-3f4a-9351-e70302ea1e55 | -3.12221 | -48.78572 | 2025-10-08 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a66f19d9-1618-321d-9ff8-3bce85cad82a | -9.7899 | -47.74474 | 2025-10-08 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9114699c-a268-3b7d-a554-ada245ac94c5 | -11.85753 | -44.92471 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da6fda0d-95a2-3495-b615-bb4f52905293 | -12.23662 | -43.78498 | 2025-10-08 04:17:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4a910b8c-4053-3494-b3da-88c3648d9af9 | -2.87454 | -48.70322 | 2025-10-08 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1a3751d-9f89-35cb-869c-8ef42d44a4b2 | -12.91797 | -46.82745 | 2025-10-08 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8fd47316-e07d-3cd1-8cc7-33f1d4eb7bad | -13.29182 | -47.56985 | 2025-10-08 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35321d32-6afe-338d-8b68-65bc284dc5e4 | -10.88546 | -47.10172 | 2025-10-08 04:17:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9b3c9e8-d455-31f1-9360-4483424a0da6 | -4.50926 | -46.35567 | 2025-10-08 04:17:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 62664899-23a4-37da-bad4-d53a1d9d6e64 | -11.1591 | -54.86336 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01d88b66-ebcb-3bc1-ad63-da91cb326831 | -5.45738 | -44.17535 | 2025-10-08 04:17:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cbb4d6da-26ac-34d4-a6fa-0ee47d6e6142 | -3.86932 | -41.54984 | 2025-10-08 04:17:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 480aadfd-0752-31f2-986a-8e57b11ccc89 | -5.15329 | -46.0939 | 2025-10-08 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 24dd340c-06c4-34fb-91ff-150d12db9ebb | -11.16674 | -54.87957 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| de968a58-1c69-3083-b59c-2de4ca23a7f6 | -5.02589 | -43.65714 | 2025-10-08 04:17:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 794675a4-e98c-3917-b34e-ef47473c7fde | -13.07185 | -47.93684 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57e0539d-6b81-3310-b0a9-a64d6e984b47 | -10.3571 | -50.28865 | 2025-10-08 04:17:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c516145e-a6f0-327c-8eed-7908c76a9fff | -5.81247 | -45.85052 | 2025-10-08 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 62d47cdb-8441-3c9c-83af-fe4408a0446a | -4.84576 | -45.7585 | 2025-10-08 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aab6defd-e02d-366d-8a0e-f09dd149e129 | -13.25361 | -47.79311 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 385ce936-8ebb-366b-8456-69209d1ce734 | -6.99951 | -42.87038 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 6b385bc9-6b7b-3380-94d0-c610a2375f39 | -11.68483 | -46.37964 | 2025-10-08 04:17:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7984ba79-ae86-3b36-92ec-0f351e8091b8 | -4.93385 | -38.75279 | 2025-10-08 04:17:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d15c110a-41b3-3060-a77a-37868ddbfe7c | -11.79349 | -45.111 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6cf3b3c3-bfa7-330e-b88b-038e8ed88a3a | -13.36366 | -47.55641 | 2025-10-08 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9b018876-c6d3-37ba-b676-8871472e8e55 | -12.93438 | -46.81446 | 2025-10-08 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5f57076-7001-3c90-8ec7-9e89e46146b9 | -10.64372 | -47.79794 | 2025-10-08 04:17:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1c6fa87a-86bc-3ad4-b6a3-28fd53e78178 | -13.22938 | -47.17007 | 2025-10-08 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1597be91-1cba-35e7-98fb-bd1a8fe32420 | -5.26009 | -44.14102 | 2025-10-08 04:17:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 33b6470d-fa3c-354f-ba20-626e74db1773 | -7.4442 | -43.14408 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b169fdda-5240-33da-a1dd-28c3b97b3ccc | -5.73724 | -44.97945 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 339a8140-298b-3545-a003-f25675591aff | -7.15998 | -46.2147 | 2025-10-08 04:17:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72632af5-ea74-30fe-a269-207fd357504b | -5.41235 | -45.29479 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b156388e-d5d5-3c53-a523-269fdd741f6d | -4.47999 | -49.70946 | 2025-10-08 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 871f6c7e-970d-39e9-8548-9b7dbbd57fb0 | -11.45843 | -50.20332 | 2025-10-08 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 178570b2-e4d8-3298-a5ab-ca3466c1b08d | -12.23107 | -43.77665 | 2025-10-08 04:17:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40dafb89-ede7-3532-a0fb-81d9dc328de0 | -11.70072 | -50.96968 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ea2cc3b-b0e4-3264-9fd8-4bfd0c2563ff | -10.86995 | -53.73994 | 2025-10-08 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9721f1b4-9b8b-31ce-803a-46e45d9a93a6 | -11.42191 | -56.29056 | 2025-10-08 04:17:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2e8f9014-e59d-35ae-9015-585ec718e845 | -5.40325 | -46.23015 | 2025-10-08 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 878cca2e-1a26-348e-8445-ad057c6d59ed | -5.41131 | -45.29541 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2fd02d1d-74ff-3203-afd0-80dd99baf4c4 | -5.63888 | -43.60644 | 2025-10-08 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bf50d287-d898-3150-9d6d-836165771077 | -11.873 | -45.74488 | 2025-10-08 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 102b95bb-b087-3db2-a5e0-136baf2670e4 | -7.47734 | -43.06361 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 64e32049-f29d-357f-83e2-b38b02785321 | -7.00677 | -42.88939 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 072d83ef-b38a-31b5-85a8-c11b505298b6 | -3.08085 | -50.5759 | 2025-10-08 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f38d10b7-9349-3110-bfd3-b12f56788a69 | -12.99501 | -46.78124 | 2025-10-08 04:17:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1f4f3f31-816b-3cd8-b789-341767f8e7b1 | -13.0769 | -47.92905 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bedd8a05-8fcd-3b2f-bb22-fb198bebfeaa | -11.17172 | -54.88489 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 56f5b667-785e-34b9-ab22-abeb6598870b | -2.89213 | -50.73359 | 2025-10-08 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7c0ad00-f76d-38a8-907b-3a8e1a5fd80c | -7.02173 | -42.88103 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 49b5c491-abed-31ad-80ce-71dcd1bdcf8b | -11.46737 | -43.48698 | 2025-10-08 04:17:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ad30c60d-475e-3446-906c-2b7749a26302 | -11.18155 | -54.87193 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1750c9d0-40c2-34f1-ae93-c05a3d1b7fd4 | -11.27967 | -49.99158 | 2025-10-08 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 40609413-104d-3d5e-b4a5-ef79f012d607 | -10.86833 | -53.74357 | 2025-10-08 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 15626ab5-fcf2-301f-b937-37b3b0dc78b8 | -11.16175 | -54.88086 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 944c6e83-930f-33b6-88fd-cafd03a82af9 | -12.94787 | -46.84068 | 2025-10-08 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49dfecaf-5d1d-33d4-b3d7-485c95e6c219 | -7.51785 | -42.71871 | 2025-10-08 04:17:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 289619f1-e0d8-3c6f-a9bf-385bd8aa6a0d | -7.35119 | -43.8612 | 2025-10-08 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 566ef661-bc77-3463-81da-5eb891c9c5ff | -7.44366 | -43.14756 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ff0258b8-3dff-3ea9-922d-72ce030fe39b | -11.18073 | -54.9003 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddf72994-7a69-32e2-aac4-9b1d7854e2a8 | -12.72879 | -44.37309 | 2025-10-08 04:17:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5439c9fd-f777-32b3-bfdd-e9555e2641cf | -11.64301 | -44.26656 | 2025-10-08 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 600168be-5eb8-3cb0-b9fe-f68043a8e611 | -11.11553 | -54.04963 | 2025-10-08 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 79785f3f-3a7d-3f80-825a-d36bfe067efa | -7.78557 | -42.41248 | 2025-10-08 04:17:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1d379ee6-7e7c-35e8-a714-06a1bab5f15a | -11.69271 | -50.99905 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25d2bd54-361d-3274-8549-1c51615a168f | -6.50196 | -41.49232 | 2025-10-08 04:17:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 1c783221-5c65-397b-a7ac-dc90a99a6a88 | -5.74413 | -44.98059 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db67bedd-9a87-324f-bdca-b51f2494b89c | -8.01728 | -41.36253 | 2025-10-08 04:17:00 | NPP-375D | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3bcb9203-09b0-3781-9ce3-30f980cc6533 | -5.4873 | -44.62101 | 2025-10-08 04:17:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4fc092f3-2fb0-3d8a-a176-f47e4d19d6f0 | -1.97469 | -50.24467 | 2025-10-08 04:17:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40ad1d7b-f4bb-3b8f-949c-50fb892cc521 | -7.35396 | -43.86523 | 2025-10-08 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 1e467dbe-df4f-3daa-bf26-aa16914c79af | -11.32007 | -42.30589 | 2025-10-08 04:17:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0477199b-778c-3800-b81c-570c7cb09ac2 | -11.12586 | -47.15803 | 2025-10-08 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 130a60e3-1831-35df-9af1-1f97d0cbcc66 | -11.99526 | -46.77224 | 2025-10-08 04:17:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 49ddef58-0b6a-327b-b667-ca4a722cd2d6 | -11.74584 | -50.93536 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 0e1268d0-98eb-34a9-8d2c-50a985b309b9 | -2.89309 | -50.72766 | 2025-10-08 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README35.md)
