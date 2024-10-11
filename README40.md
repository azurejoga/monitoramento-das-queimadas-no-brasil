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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e292148-095d-3b88-a05c-6dae5e329ea5 | -4.11457 | -48.26817 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d5a43bf7-b678-3874-a280-9f158bb50efc | -4.114 | -48.2716 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 44bbaa59-2c6f-3d06-8dfc-714a12c82af1 | -4.11377 | -48.24071 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| deb7928b-cb65-3957-b7c0-2432dabc5c06 | -4.11342 | -48.27498 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eb7f0279-d490-374b-a088-86c2fc981913 | -4.11323 | -48.24387 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 15e89fb5-5594-37c4-915b-baea2d9ad834 | -4.11285 | -48.27838 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 713e8ff4-802c-39b9-b393-385979e004ef | -4.11269 | -48.24709 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 25160bfc-9e71-38cd-8ef9-618f2eebb59b | -4.11213 | -48.25037 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| d448b969-6e17-37fc-a489-1dd415ad6ec7 | -4.11158 | -48.25364 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 0e7f4441-f45c-37f9-8cac-3f0aff673c2d | -4.11101 | -48.25701 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| e4240c5e-dd0b-3039-a1f8-55b6fbf59136 | -4.11043 | -48.26039 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f4316a2f-c650-3ca7-b3e4-c9ce382c8cdc | -4.10986 | -48.26381 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e4eb7f4b-b2e8-3e58-a9b7-b23587078d5a | -4.10927 | -48.26724 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e6b519d-1d97-3245-a292-39899bca9bef | -4.10869 | -48.27067 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d916f7d-5f5b-33a2-82b5-04da28a9de68 | -4.10847 | -48.23983 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 7ad082d4-c075-3f3d-80ce-9c216574c797 | -4.10793 | -48.24301 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| e27cdada-21b8-3b30-8f72-b77555548261 | -4.10739 | -48.24622 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| dad4ee32-f632-32bf-a100-fd13752b4cb5 | -4.10683 | -48.24949 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| c007c472-9254-3efb-a3f5-d6afea30eb00 | -4.10627 | -48.25277 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| c0931dea-97d0-3360-8ec1-fc44513d84a4 | -4.10571 | -48.25611 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| a4b00447-c32e-31d6-9247-7ba33050c726 | -4.10512 | -48.25954 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| df7249fa-d31d-38c6-a664-3b0efc5be836 | -4.10455 | -48.26296 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 85fba4e5-b13f-3199-928e-f2eeec10ac40 | -4.10397 | -48.26635 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d12d357f-dcf8-3d63-8b73-fdd2aa632b3d | -4.10339 | -48.26974 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c4148a8d-c1e4-3f08-9ea6-6e014a257944 | -4.10283 | -48.27306 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7117d8dd-43e1-3a36-a40f-d339e9a33c1a | -4.10261 | -48.24224 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bfdedc68-6324-3830-b247-a28844768f3b | -4.10207 | -48.24545 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 55e9fb20-c829-3c3c-8839-367174778c94 | -4.10152 | -48.24868 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f7358740-bc4f-3b77-83e0-74d2d8a704e8 | -4.10097 | -48.2519 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ebbdef80-9161-34ba-a61f-31ec3c38ce7a | -4.10042 | -48.25516 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6dfe4e96-6dbe-3023-8c71-12138cf9dbbd | -4.09984 | -48.25853 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 980b26f9-8dd0-3d7e-a640-3a693b27f51f | -4.09927 | -48.26189 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8fe5608a-e198-3e22-8f5b-2f8add09fe80 | -4.09871 | -48.26521 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd67ad85-f60c-3262-b0e5-617671583bd1 | -4.09815 | -48.26851 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ef31cb0-4632-3919-9e83-8a231432114d | -4.09759 | -48.2718 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08572db6-6e95-3c96-8089-07fd692d54e5 | -4.09702 | -48.2751 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f910cdf-7a62-39c3-bc1e-0397660b13ff | -4.09673 | -48.24481 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 35506784-84f9-357a-82a1-015e71e8a87f | -4.09646 | -48.27842 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1676860e-f2db-35fa-8f49-5fcd37b6b2d9 | -4.09619 | -48.24797 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 547c32ad-b9b0-3ec3-9b49-15df8008d4be | -4.09565 | -48.2511 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 56c3438d-0cb2-3bf0-b16b-e11a01b52784 | -4.09343 | -48.26414 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3e8aed2-8acb-30ba-bb5e-4c5f4f00afba | -4.09287 | -48.26743 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 383d324a-9e17-3d43-b31f-6169603dda16 | -6.08428 | -49.32187 | 2024-10-11 04:00:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d5b9a06-3d43-3704-862f-660abe23426d | -6.08365 | -49.32543 | 2024-10-11 04:00:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 125548fa-1a1b-3b93-807b-c5ea352bddba | -5.78287 | -49.04509 | 2024-10-11 04:00:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6e32065-ce8f-3937-a78d-c561cd508e37 | -5.78226 | -49.04856 | 2024-10-11 04:00:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c898fde-1248-3271-bb72-1e9b55392aba | -5.71339 | -49.31565 | 2024-10-11 04:00:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87664f2b-6a2d-3261-ac59-8e505f07efa2 | -5.70787 | -49.31461 | 2024-10-11 04:00:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8d9aa81-a732-3094-ae32-a4a18d70918e | -5.49344 | -48.82608 | 2024-10-11 04:00:00 | NPP-375D | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51c4ba4d-6dea-3b0e-bac5-0548b4f0a3f2 | -5.49284 | -48.82948 | 2024-10-11 04:00:00 | NPP-375D | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 05fca04d-c2fc-35a0-973d-69d06aba2f15 | -5.2475 | -48.04354 | 2024-10-11 04:00:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 3db17fa0-e8f7-38e0-b9ac-97b75d10bca1 | -5.24698 | -48.04658 | 2024-10-11 04:00:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 123c6193-7fdd-3368-ade2-5e225016a1c8 | -5.24647 | -48.04961 | 2024-10-11 04:00:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 87af536e-8d19-3fd9-bc25-e225be3473ee | -5.24185 | -48.04569 | 2024-10-11 04:00:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 968c1456-7bd8-3533-95f4-14ea487d394e | -5.17469 | -48.28246 | 2024-10-11 04:00:00 | NPP-375D | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3f1294b-b7c0-3f0d-b3f3-2be4026dd3bd | -5.16948 | -48.28151 | 2024-10-11 04:00:00 | NPP-375D | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b4ef6a29-0a53-3230-a21e-9ef5b0f7bea9 | -5.16894 | -48.28468 | 2024-10-11 04:00:00 | NPP-375D | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 155d8caa-8faa-38a0-bb74-83dad6c54de9 | -7.73098 | -49.02828 | 2024-10-11 04:00:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d278b2a7-f73d-3e9c-af9c-a3cdced1fb74 | -7.7304 | -49.03152 | 2024-10-11 04:00:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 84ef561c-5d5a-3b5d-af52-4165fc7caf35 | -7.69191 | -49.83771 | 2024-10-11 04:00:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0f968e5-353f-3b1f-816c-c02aaffdc8d7 | -7.68839 | -49.8256 | 2024-10-11 04:00:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 998ab768-7586-35bd-b47c-0c9c538671d2 | -7.68772 | -49.82928 | 2024-10-11 04:00:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4326c941-9d77-366f-b32c-9f382bd51a39 | -7.68637 | -49.83668 | 2024-10-11 04:00:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 84c4ae92-4343-3488-b1ed-70983a200112 | -7.68084 | -49.83561 | 2024-10-11 04:00:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 834504c7-f69a-32dd-861f-ad93226daab0 | -7.3347 | -48.59196 | 2024-10-11 04:00:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 707d3df2-e833-34ae-b619-27f104bc93eb | -7.33185 | -48.58904 | 2024-10-11 04:00:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8643eef4-9f77-3a73-8ff0-7ac7614b02fd | -7.33129 | -48.59214 | 2024-10-11 04:00:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffc1877a-f153-3cb6-b77c-695d8f82ba4f | -7.32957 | -48.591 | 2024-10-11 04:00:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0cc378b9-b027-38cf-a660-8adbd387276a | -8.83785 | -50.06615 | 2024-10-11 04:00:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1aa78e7-91b3-3eca-89a3-8922b8b24270 | -8.83717 | -50.0698 | 2024-10-11 04:00:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df9c5b85-77e4-3902-8930-9079f4c67af5 | -8.83166 | -50.06873 | 2024-10-11 04:00:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28e12039-0c68-33c3-aad9-5298ad003491 | -8.79179 | -49.79208 | 2024-10-11 04:00:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e497aba4-1d4c-3200-9ac5-d0e4afd6e5e1 | -8.78639 | -49.79098 | 2024-10-11 04:00:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0f067920-39a0-3961-bff1-5cd80f22a442 | -8.77227 | -48.8591 | 2024-10-11 04:00:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 817668f9-a7ee-3093-a489-e039dd548b27 | -8.70682 | -49.98117 | 2024-10-11 04:00:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b4a01448-107f-3486-bfec-3dd6a9e069b3 | -8.70655 | -49.97813 | 2024-10-11 04:00:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea7ed581-0802-38f2-976e-da7804e3f9de | -8.70618 | -49.98475 | 2024-10-11 04:00:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0dae5cd1-49c3-33ef-aaca-7930290edc75 | -8.70588 | -49.98173 | 2024-10-11 04:00:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a526f49-3369-306f-a24c-924c77e783f7 | -8.70521 | -49.98531 | 2024-10-11 04:00:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c891643a-7ad5-3c08-a376-4406d2a97d5e | -8.69904 | -49.98786 | 2024-10-11 04:00:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24e0c6bd-3004-3432-bf13-df61aff62d43 | -8.69875 | -49.99446 | 2024-10-11 04:00:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbf7bb6b-f21a-3734-894d-b5681314ca85 | -8.6981 | -49.99806 | 2024-10-11 04:00:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf2050f8-0c81-30dd-af99-acbbc7d5fcdf | -8.6977 | -49.99503 | 2024-10-11 04:00:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e692449-16fe-3866-bf3f-dcac2ac120b4 | -8.69703 | -49.99862 | 2024-10-11 04:00:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1a7dc07-1076-3550-bf64-c6c4c645b86a | -8.69196 | -50.0006 | 2024-10-11 04:00:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3300979-caac-363e-b1d8-b9897ee92c1a | -8.4372 | -48.66472 | 2024-10-11 04:00:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e9dd9da7-f50f-313b-aca4-486d8f1d672b | -8.33559 | -49.96856 | 2024-10-11 04:00:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1a512f5d-810d-3ce2-b930-205fa03e1e16 | -8.33492 | -49.97222 | 2024-10-11 04:00:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 97a50211-2fe1-31d4-976c-17ab4385989f | -8.1793 | -49.20103 | 2024-10-11 04:00:00 | NPP-375D | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 77a58e6c-08f6-361e-bc87-a70a20db30ac | -8.17403 | -49.20004 | 2024-10-11 04:00:00 | NPP-375D | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d5828769-3f14-3dd6-90ce-da68049b1629 | -2.96423 | -49.20284 | 2024-10-11 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca20c3d0-7c5a-33f6-92fc-5c2db761ae56 | -2.95849 | -49.20183 | 2024-10-11 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e855e27-bde1-3abd-b2dd-2ad277ba3c7f | -2.95782 | -49.2058 | 2024-10-11 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03c35f2c-4229-33f9-9d48-5b27f37c8fc2 | -2.90042 | -50.39179 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd372c33-6474-372f-924f-aa3c2b8d3033 | -2.89962 | -50.39658 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79f1dfbb-9c30-3ac2-b011-df32f7ecdba4 | -2.89342 | -50.39548 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b0a5685-4ddc-3b2b-81f3-65c9fc27a7b4 | -2.8451 | -49.86864 | 2024-10-11 04:00:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7683b722-ef84-37d3-81e9-8845528c23da | -2.84376 | -49.86616 | 2024-10-11 04:00:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e04795a8-6948-3aeb-aa0d-c0a3d3445d09 | -2.84304 | -49.87059 | 2024-10-11 04:00:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 591b5b0f-3e18-3011-b6d0-8bfabd5ed1a6 | -2.83908 | -49.86768 | 2024-10-11 04:00:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README41.md)
