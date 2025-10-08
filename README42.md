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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f15a93f6-142f-31b3-ab27-a2b1cdf30041 | -11.14429 | -54.87758 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0051e7bb-0bbe-3dba-bc18-86bb50be7f88 | -5.17148 | -45.12859 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 743f7a58-5bca-38cc-b3a6-0b4f1a437553 | -13.05724 | -47.89097 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 370ea1df-09df-3512-931d-3a02a36e20eb | -3.24114 | -46.78595 | 2025-10-08 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9c66c343-3445-3ff3-a595-f23007c90ecd | -11.2575 | -47.61914 | 2025-10-08 04:17:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fdff9162-7535-3c59-9088-a115da16bf30 | -11.6964 | -46.3739 | 2025-10-08 04:17:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cf156885-4099-3777-a73f-d710f834c405 | -10.88188 | -47.1011 | 2025-10-08 04:17:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 157dcbf7-4a66-386f-8740-5ebe0f7b4acd | -11.17083 | -54.85908 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4615a0a-085d-3539-bb94-a7586ea1cd8d | -7.47411 | -43.12739 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c0781ae4-c948-3fd2-abc9-ca4957d960c7 | -11.69341 | -50.95906 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bdf8e523-5a1a-3157-af71-1dc542174729 | -10.36221 | -50.28523 | 2025-10-08 04:17:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| de7c6a6f-0937-3963-a87e-3a0932ef5bf5 | -2.78888 | -49.62478 | 2025-10-08 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4636c84b-df80-346e-9379-140fe9af79ff | -5.14013 | -44.96083 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 7a847aca-7611-3924-af89-cc72d4e66438 | -5.454 | -44.17482 | 2025-10-08 04:17:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 28a7835c-ba31-31f9-aaf2-e7b3dfcd0e58 | -11.16174 | -54.87439 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6dde6a4e-71b1-3fa0-8471-3f8e2c84a4fc | -11.12177 | -54.04698 | 2025-10-08 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6afd0eaa-db57-357b-b4b1-d472388a120d | -3.23955 | -46.79561 | 2025-10-08 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2dc13d1a-99e1-3193-8f2f-6ce1d36d69ce | -7.69857 | -42.38839 | 2025-10-08 04:17:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 453022ec-d25f-36c2-839f-bdcd628a6a20 | -11.38106 | -54.34531 | 2025-10-08 04:17:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33c3dd95-5600-33c9-a566-3a00cac9b768 | -7.09784 | -39.75568 | 2025-10-08 04:17:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7ca83845-4078-3d96-93b7-592ed07ced04 | -3.57776 | -49.44162 | 2025-10-08 04:17:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 17c8e468-d756-3662-8b53-27e7989c9b76 | -11.17497 | -54.87479 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 96a45649-2a0b-3137-9694-5ba8f10e096d | -7.15646 | -39.31295 | 2025-10-08 04:17:00 | NPP-375D | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dc756315-6fe0-3a86-bd02-0b72a29d77ba | -3.14726 | -50.29834 | 2025-10-08 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9552bfe1-85ee-32e3-9088-e3e87d40a483 | -9.44675 | -56.65392 | 2025-10-08 04:17:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e45330d-8f1c-3f03-a66d-7c2f8621f47d | -11.52132 | -51.49378 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2510ae2c-1cbd-3c01-99b5-fa1dcf7e0708 | -11.44424 | -50.20901 | 2025-10-08 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eda31438-93f6-3cdc-8921-e06b73724636 | -7.6259 | -43.06168 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2ed8e515-9dd2-3497-9cb4-68b765659489 | -11.3392 | -44.8799 | 2025-10-08 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| de2c03ee-7c47-3f44-a350-51045e58ca67 | -12.93502 | -46.81061 | 2025-10-08 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2b3b59d-6c5d-3273-b5a7-b71a40fca7f1 | -12.94724 | -46.84454 | 2025-10-08 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe2e565e-5fe9-3460-b65e-842520e7f8db | -13.07369 | -48.01484 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0ab4d0d1-4c4d-352b-a471-39475d77336c | -4.05327 | -42.51034 | 2025-10-08 04:17:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 09877b19-4fa7-3d50-a32a-7204cda39a1e | -7.51117 | -42.71766 | 2025-10-08 04:17:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ab84f28d-8392-3016-882b-1ffcb259dc4d | -7.00006 | -42.86689 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b2ce6e98-4937-34ec-ab1a-7969025a46ba | -7.70585 | -42.38588 | 2025-10-08 04:17:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 63b633cb-d3c9-34dc-b3c9-c8342fba67af | -5.1571 | -46.9252 | 2025-10-08 04:17:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81a6b9f4-d44f-3ba7-ae44-a2dbf1734f60 | -4.42721 | -47.75667 | 2025-10-08 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1c5f5fa-5efa-3330-9468-2795fb1d5df2 | -11.86836 | -44.93338 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76ee0c2f-59c2-3080-81a6-5781ac77394a | -13.245 | -47.16348 | 2025-10-08 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b04ff6d-6bee-321b-879f-f275fe02368f | -5.45125 | -45.87041 | 2025-10-08 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59dfcbca-8481-35b3-9747-7784a0ee34eb | -13.29694 | -47.17582 | 2025-10-08 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f5d02d73-7c10-3c35-8f88-d6c703c015aa | -11.18327 | -54.8875 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 11c6a587-8c48-3559-a274-e71d6fb41a65 | -7.00011 | -42.88834 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1c14602e-a409-32ce-89b1-fb73e177774e | -11.45131 | -50.21864 | 2025-10-08 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 528d1df5-cb92-32bc-8d75-dff288b345fd | -10.61928 | -48.65414 | 2025-10-08 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b26ce9d0-be1e-38c8-929c-6106e5c639e9 | -10.94312 | -51.03318 | 2025-10-08 04:17:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dff7f5a5-7de1-302b-b96b-0772a7984f61 | -11.78088 | -45.06142 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 614c388b-f41f-3ae9-b4c5-d28dc947653c | -12.2405 | -47.8776 | 2025-10-08 04:17:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb67be00-8d08-36f2-a3f4-ce2740fa6177 | -12.24847 | -47.85877 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 79384d23-16f2-3ee3-a6b8-7e84bf9ddda5 | -4.25432 | -48.56713 | 2025-10-08 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0b10fe1-e472-3ace-9868-38ed8472425f | -7.35674 | -43.86926 | 2025-10-08 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24d7ce99-5d6d-3062-a84c-cf551ff93458 | -10.38014 | -47.97992 | 2025-10-08 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3805156-bc85-33aa-9768-2587749c77e8 | -3.94594 | -39.01905 | 2025-10-08 04:17:00 | NPP-375D | PENTECOSTE | CEARÁ | Brasil | 2310704 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| b736165c-80b0-32b4-b380-21444394f937 | -11.76609 | -45.13215 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 850cb086-b492-3b88-8386-91fa157835b5 | -13.27168 | -47.56701 | 2025-10-08 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b5993c77-47ef-37ff-b1e3-bd276a194130 | -3.73867 | -44.26571 | 2025-10-08 04:17:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7978ce33-c906-38fb-8f40-529b2093ab2f | -4.48208 | -49.71667 | 2025-10-08 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7c339a6-3eee-30d8-9c8e-4c701a13db87 | -11.8202 | -45.11563 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0fea10e-a0d7-3729-bdca-e0080e8b8f2f | -4.50334 | -46.3684 | 2025-10-08 04:17:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28e3dd57-73c4-3e42-815b-bf6856fdf00a | -11.17918 | -54.87773 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 00abb621-348e-3900-a606-906f180246d9 | -7.4392 | -43.13258 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 661740ef-a348-399e-a12a-827f5ad3f0d4 | -3.19994 | -51.02145 | 2025-10-08 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3238f05b-96ab-365c-a70d-2e534ec520b6 | -11.77161 | -45.14046 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2f666ec2-a52f-3bfc-944b-685b733a2821 | -6.32311 | -41.61086 | 2025-10-08 04:17:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| e72a1e61-7c7b-33f8-a3d2-0a0a1eca8eb4 | -11.14239 | -47.74979 | 2025-10-08 04:17:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c679944a-3294-334e-b723-04bd90cc0658 | -7.02506 | -42.88156 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 52062e3d-a103-32bd-83b6-4d1b891ab4d3 | -11.79292 | -45.11457 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b0c42ed-e319-3f8e-8529-ff66482ddcaa | -10.94036 | -49.48489 | 2025-10-08 04:17:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 617ae3bd-81cc-3411-815b-2f9560441c9e | -6.42512 | -47.24649 | 2025-10-08 04:17:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55cbe0fd-e489-3d0e-a000-eaf008b501ed | -5.76922 | -45.74183 | 2025-10-08 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| af60f3b9-cf94-3b8b-9147-39841e20cc76 | -11.11617 | -54.05316 | 2025-10-08 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 99c86cb4-1d51-397e-9e17-df5864016bdc | -11.70774 | -50.99263 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5bee494-2eae-34fe-bec8-be187f1dab03 | -4.85492 | -45.79298 | 2025-10-08 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4dcd52df-72a3-336e-990a-baa1b88e43fb | -11.16339 | -54.86619 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 479592b4-63ca-3d32-a789-f2662156458f | -3.38294 | -50.14231 | 2025-10-08 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8b41734e-49ec-33ca-bc67-10ba94f89737 | -13.29024 | -47.77368 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4b0fc821-b60f-3a84-a7eb-7ea2150b3f72 | -2.14619 | -47.50547 | 2025-10-08 04:17:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2604ac43-ae0c-3956-8a60-a5642467ed45 | -3.83426 | -50.97105 | 2025-10-08 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 73a91506-c5ba-3ed1-80d4-cc8f8582fec8 | -11.17833 | -54.88871 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 463309b4-05f3-3c90-9115-b468be0e95b4 | -13.27827 | -47.56334 | 2025-10-08 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e9d6234-1a01-34f0-b359-0184319d5c3b | -13.49683 | -43.67043 | 2025-10-08 04:17:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6ced135-6da3-3f25-8a30-7b0d087b8e7b | -6.5675 | -44.15385 | 2025-10-08 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b303cbf-7af6-39f5-8664-5c858c30aa2a | -7.47799 | -43.12443 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d7db42a2-74ac-3e62-a4ae-bf09c38b3927 | -10.04586 | -48.28235 | 2025-10-08 04:17:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a44d9d4-57a3-3aa1-a1bb-9d7c1af67f5b | -5.16751 | -48.96444 | 2025-10-08 04:17:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 850f86e2-b855-320f-97fb-f502455c531a | -5.14123 | -44.96395 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 2050d2e0-534c-3dfb-81fc-7929ec36b4ed | -11.29801 | -54.88634 | 2025-10-08 04:17:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0081de7-387e-3290-a84f-3e7f0c07343c | -12.40287 | -51.14491 | 2025-10-08 04:17:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bba50256-d4ca-3ad7-ba4b-7c84f1bac9b6 | -10.34037 | -51.55657 | 2025-10-08 04:17:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4103b8bb-38d1-3b13-ba40-103670b9cb1b | -13.23061 | -47.79754 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 284aa2b0-dcf2-3e93-9353-7c8a062b8a44 | -11.17418 | -54.87893 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 493279b8-76fd-35f9-bf01-20328224e7d7 | -11.99934 | -46.77253 | 2025-10-08 04:17:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| fe7e597c-7d4e-369c-9efe-627c849d0600 | -11.67241 | -50.97353 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a6c9633-bf0f-38e2-811c-5db692d90873 | -11.70856 | -50.98816 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 05cf4be1-1a13-32ec-bd61-3720008ffcae | -3.45071 | -45.59727 | 2025-10-08 04:17:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 531fcb2a-011c-3228-b3da-d74ab27c91db | -13.372 | -47.2253 | 2025-10-08 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15935bec-4835-3e79-91f4-674a20d56351 | -10.38859 | -48.13404 | 2025-10-08 04:17:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 05d27888-7703-3b1c-b32c-36b271aaa4f3 | -10.86928 | -53.74338 | 2025-10-08 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1acdfc94-88b9-37c3-9dd7-03a3d12087af | -5.74008 | -44.98378 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README43.md)
