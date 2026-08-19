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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c7863b5-1d69-36f3-9c1b-b31c36981798 | -6.62966 | -59.08213 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad01dc38-a35b-3818-aa1d-acbb78413cda | -7.05171 | -59.84806 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ae71718d-5e02-35b0-bbf3-4b0fab28f6fa | -3.68429 | -47.65412 | 2026-08-19 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 9aa3cf95-a227-324b-b891-3866eb92fb60 | -6.33705 | -54.91579 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9b59882-037e-3317-ab20-2f66ba2ea2dc | -6.84056 | -44.94495 | 2026-08-19 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2c1a750-3b56-34fe-81d4-e27bdbb9ea3e | -6.33911 | -44.07265 | 2026-08-19 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3d8b5d96-a7b8-3d02-99f3-1d8d64b18548 | -7.17344 | -43.10245 | 2026-08-19 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c36fb3fe-1aa5-36a3-82f9-a432d2eb5b14 | -6.44224 | -52.72849 | 2026-08-19 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b0bf55a-d0b8-3048-9e48-ee01598dd62d | -6.34483 | -54.89814 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 97da8d1a-8988-317f-a69f-35cd34478d66 | -6.03799 | -57.79905 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a210dd3a-05f2-39df-9587-f4247abd49eb | -7.53574 | -55.57346 | 2026-08-19 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6d3d6a77-e05f-3eda-aea3-199eb8e23f00 | -4.46207 | -55.45956 | 2026-08-19 04:38:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c9c1194-42f3-3aa0-a022-c9c15211014f | -6.01711 | -50.19849 | 2026-08-19 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e67207df-c4f9-3f2c-88ef-de2cdc24e9c1 | -7.22033 | -43.28638 | 2026-08-19 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c59de1b0-f20f-33ba-bd7b-261735319b51 | -5.49492 | -60.13132 | 2026-08-19 04:38:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8f9672f6-2daf-3789-85cb-29a21509d8a6 | -5.58172 | -49.15758 | 2026-08-19 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d455db4-4c9b-3763-b479-f3b719bfde78 | -6.34234 | -54.90985 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5e7a6646-c2ab-3038-bf68-72c43a7abd7e | -6.80163 | -59.45517 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07b4349e-08d5-33be-baaf-582a54c765c4 | -7.44442 | -44.85745 | 2026-08-19 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d444fac9-9207-3d99-9738-ec2a7d01fe0a | -6.73839 | -59.04061 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f249bc85-ce99-33f0-ab03-e5abc640d7c7 | -5.05204 | -46.1128 | 2026-08-19 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9081e37-acd6-3256-8bdd-6dfc3c8e9cb7 | -6.83259 | -56.45309 | 2026-08-19 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c2dd523-b8ba-37de-bbc1-ea471c75f41c | -3.28 | -49.46717 | 2026-08-19 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 633a863b-99e1-380e-a7d2-e4f248439c04 | -8.35516 | -46.36308 | 2026-08-19 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 25a7e09d-7039-315b-85a4-b4b1e576743b | -6.85448 | -59.02754 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4cd38423-e1dc-342b-9e0b-b08930916366 | -6.02027 | -57.84251 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8220cf70-4e13-32db-810e-2bdd5f0cce1b | -6.447 | -52.72416 | 2026-08-19 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0d25b81d-698a-3aaf-a8d9-f91ca3df2f88 | -3.68098 | -47.6536 | 2026-08-19 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 96b88e44-7c08-354a-add6-0c34c4ca9a41 | -5.43548 | -48.41712 | 2026-08-19 04:38:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| d850146d-e359-3ae3-82ff-0d1bb5632eda | -8.10548 | -51.65209 | 2026-08-19 04:38:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c71137e-22c6-39ab-aa56-1c333b6c85a0 | -6.16517 | -47.75739 | 2026-08-19 04:38:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3eae6277-7957-36c3-ac03-0a2f5df8402d | -6.80857 | -59.4516 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| adb24cd5-c615-3560-b5ae-9c84bb692f23 | -8.04868 | -50.10713 | 2026-08-19 04:38:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f968fafa-de0b-3b3c-a4dc-9827d7d9c7e8 | -7.01085 | -47.97339 | 2026-08-19 04:38:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3acc5d0c-5213-3184-a905-83aa1e994ccc | -3.9329 | -50.9992 | 2026-08-19 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 125f5415-b98a-366c-a31c-17ec087be15a | -6.69677 | -58.94816 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| afab02e9-b360-3e3a-8875-a7d95ece3754 | -6.45093 | -52.72483 | 2026-08-19 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9c8cb9dd-8647-3ea4-b1fb-be742d8d960b | -6.83333 | -44.94381 | 2026-08-19 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6b5cbe9-1ca9-38f8-ad33-21e88b9f46c9 | -6.68572 | -59.07908 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eea28450-eb64-31e4-a639-4e7e5bdc92d6 | -6.91157 | -42.84943 | 2026-08-19 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 22335790-a26e-392a-abbe-6744703cafb9 | -6.27112 | -43.27747 | 2026-08-19 04:38:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| f46383b8-4b79-3861-a9c1-898b76745539 | -6.40367 | -54.93728 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a8faf91-b9d7-3a72-a1ad-3727019a6735 | -6.34028 | -54.89737 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9a263278-3eef-3eae-a510-4052a27d738d | -7.25726 | -44.21496 | 2026-08-19 04:38:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2824dee-e3ff-341e-bd88-8ef6e110e633 | -5.82096 | -43.39696 | 2026-08-19 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b70ea0fb-5f75-3b0c-8681-c42fa8e95697 | -3.68814 | -47.6512 | 2026-08-19 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90edb03a-92b8-3d66-bb76-28e4ede82dd4 | -6.84344 | -59.02086 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9b5fcef-96f3-3bc2-ac4a-71099b837071 | -5.99472 | -57.85688 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 77da24f7-6616-3e3c-8229-e94944bd5d25 | -6.35393 | -54.89965 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c1b05db4-d1ea-336c-9bb4-1c64c52e759a | -6.03918 | -57.79992 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41f843e5-33ab-3483-8f91-6394dc0066af | -6.2855 | -43.6361 | 2026-08-19 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2805202-53d2-32c1-a9c3-8173c938f9da | -8.02384 | -54.01061 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63f9b7e9-0aed-367c-a2b3-95bea58605b6 | -6.65066 | -56.43252 | 2026-08-19 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d6577f8-1716-3419-8162-c090b38f36b2 | -7.95544 | -44.63997 | 2026-08-19 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d705e5e-adde-3c5e-8a63-8824d449cf0a | -8.35457 | -46.36689 | 2026-08-19 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 18648fe0-da65-3f9d-a39e-28f10fac0a7e | -6.79112 | -59.44366 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 870bd2d6-5fa9-3a25-84ca-0a3e3cb13559 | -6.08125 | -57.91041 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 50513a3b-39ef-3354-8eb5-4c0023fc5778 | -3.4277 | -51.51626 | 2026-08-19 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6e3c279-3268-39ec-8aca-cdd4a1f66a8e | -6.7642 | -59.45305 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df5b6eb1-642e-3608-a5a2-123f0f6b71e0 | -3.51147 | -48.03723 | 2026-08-19 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18f10e68-7c79-3380-a55c-dece2dabc7a2 | -8.36439 | -46.34898 | 2026-08-19 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9fb673d-f2d0-3dda-a802-2226258e2965 | -6.106 | -57.73896 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 886abb65-b741-3c27-85ca-5f972fdefb74 | -5.91097 | -43.62659 | 2026-08-19 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 564c662d-5a98-384a-9a7f-c046f5a9f55d | -7.34903 | -44.37677 | 2026-08-19 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b45dad28-b565-3dfe-93b8-3860b55897f4 | -6.84743 | -58.99908 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 090d568f-3993-3b4b-915f-a2327f726129 | -7.55701 | -55.56195 | 2026-08-19 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9dcab111-7b39-3823-802a-44c2531590ea | -6.13988 | -57.86366 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7a4a3e8b-3875-3651-bbe5-a52f6f0bdc3c | -6.88443 | -59.06545 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 119bc687-cf55-34f1-8278-a85810dc6d2c | -6.33791 | -44.07948 | 2026-08-19 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fdc5e846-22fa-3cd1-a502-f1c6885f2fba | -3.66094 | -48.97237 | 2026-08-19 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c730e6ad-195a-367b-aac5-8bf2299d4332 | -6.34921 | -54.89671 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8ff7a583-1961-35fd-8dcd-0a217eaf97fb | -7.21685 | -43.2823 | 2026-08-19 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d9da9d08-1e56-359b-a418-fb73d82961aa | -7.55149 | -55.56599 | 2026-08-19 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fb09bffb-d1d6-31b0-8441-f60175ae7f99 | -6.69963 | -58.95134 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4e4815f5-8e6e-3b43-a334-723ba2ad5c62 | -6.35768 | -54.905 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e71ddc1-da2b-3ad1-afbc-e66486e58f60 | -6.13512 | -57.88987 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d70089a9-8700-37a7-a698-2dabe9042ce9 | -6.34159 | -54.91665 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3116174-839f-37b9-bca1-af64bfb71bee | -7.95169 | -44.63951 | 2026-08-19 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 66af386a-35ad-307f-9f90-319a33917469 | -9.26916 | -45.64946 | 2026-08-19 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f9379256-32ff-3ce8-ae6c-ade161668dd1 | -7.24757 | -49.89653 | 2026-08-19 04:38:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ca23a75-b113-3187-95c1-70a6114f1a34 | -1.82218 | -47.89182 | 2026-08-19 04:38:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d76f1d7f-985a-3c2f-af8e-ad88ba074d9c | -6.3461 | -54.91535 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 34cc05d3-0e19-3a95-9265-83256e0d1901 | -6.86038 | -59.02884 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5e4430ef-bea8-34d7-a4ca-9eb29d2fb609 | -3.01643 | -51.0603 | 2026-08-19 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5278211a-ee3e-303f-b159-9f603d092acc | -7.62614 | -45.71811 | 2026-08-19 04:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3ed9928b-a58d-3084-a1d7-fe398879aa59 | -8.5393 | -47.38792 | 2026-08-19 04:38:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a8941c7-9b5e-3fef-ba47-8376299fff0f | -8.10118 | -51.65558 | 2026-08-19 04:38:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e36bf74-91ef-3897-af0f-8c0f676d913c | -6.33786 | -54.91116 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09f7969d-7952-38d5-8691-50c94d961679 | -6.23045 | -43.68695 | 2026-08-19 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ce42bde-a438-3853-9bc2-7dfa690c2e5f | -7.56545 | -55.56865 | 2026-08-19 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a6a3e1df-4eb6-3077-beba-37f8e0c30c7d | -5.42995 | -48.40913 | 2026-08-19 04:38:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 9ac7f488-69bf-3ee6-8988-854a029c9371 | -6.09241 | -57.91259 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 87fe6bc5-0192-36f7-bdb2-f7534e59d249 | -4.70772 | -47.15553 | 2026-08-19 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df23284c-9646-32a2-85e8-f9f948d5aacb | -6.14133 | -57.88738 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f74f78bc-fe20-3789-961a-0fc768f3b5b2 | -6.87494 | -59.05003 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f633c297-07c1-3742-ba06-610e5bfcce56 | -8.35353 | -45.97645 | 2026-08-19 04:38:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 39e3127d-4d83-35a0-bfcc-7b2a9eeb174b | -6.33862 | -44.07487 | 2026-08-19 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ffa96386-399c-34c7-b03a-265aa7b90558 | -6.76978 | -59.15296 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ac3dd74-781c-3b1a-9a4b-d43522b7ed05 | -8.1005 | -51.65965 | 2026-08-19 04:38:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e09261fd-2685-3290-82c5-86ed9ac92e34 | -6.77754 | -47.40535 | 2026-08-19 04:38:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README37.md)
