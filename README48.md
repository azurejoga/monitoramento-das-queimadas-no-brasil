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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e55d205-334c-3267-a555-f729be837983 | -13.62119 | -46.95384 | 2026-09-18 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8080ae62-ebc9-37f9-9869-111d3b2b3383 | -11.16433 | -42.79918 | 2026-09-18 04:21:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b91382a9-677c-3d8a-b10a-0d139f399132 | -15.56541 | -46.45737 | 2026-09-18 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 88c9cc79-7a49-3230-81e5-2bdd2592cf16 | -13.363 | -46.29909 | 2026-09-18 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8db7a27f-05e4-3e86-a324-b8840ad2918f | -10.02105 | -45.50616 | 2026-09-18 04:21:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e0ac9d52-942d-3519-9c73-e8a4aa220dd1 | -9.91198 | -46.50579 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c99188dd-220f-3c55-8c01-56e781cba60d | -11.34008 | -43.97537 | 2026-09-18 04:21:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 775080c0-6568-390c-997d-a88e057601bb | -13.43058 | -51.90284 | 2026-09-18 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b99c5356-f4ab-3c2c-a4c1-ce2952e60903 | -11.98737 | -52.46227 | 2026-09-18 04:21:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d633d00-7b4b-3acd-a776-91dcdb1c1096 | -11.58172 | -46.89761 | 2026-09-18 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3908c37f-6901-3c91-972a-8fdb5d46d5c0 | -9.79588 | -46.09875 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 727aac01-2e8b-3eef-8970-e432cb025be6 | -9.9521 | -45.6879 | 2026-09-18 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 009ed5d2-90e3-3963-b4a9-1507f8a6c9fc | -14.23696 | -48.64074 | 2026-09-18 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 87ca12c6-dd4c-3ac0-b49f-736b9a47c5d3 | -12.39947 | -50.68113 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1cadca47-3e96-319e-800d-351e03cb9bd3 | -10.13337 | -45.57444 | 2026-09-18 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 73de4d1f-cbaf-3cb4-b07b-d62513581297 | -9.10353 | -45.71909 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 51ec4d04-a0b6-3769-9691-6d74e0dc5d83 | -9.91471 | -46.53156 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 500bb6fa-2547-37a4-9e69-5b9e7d2be1a6 | -9.74405 | -46.10477 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7599e69-7a8e-3e37-a531-931cd84903bc | -10.6587 | -50.25402 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c78d5d53-c109-3e9c-a66e-b53411582834 | -10.6026 | -43.32498 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3267edf8-204e-328f-b197-4a0ce3e6c4d8 | -10.54076 | -44.85072 | 2026-09-18 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a14a31be-af17-38d7-aade-8b3753cdfd61 | -8.49553 | -45.65076 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 305fde93-7bc3-33b7-bf38-44957232a621 | -10.66772 | -50.27063 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4f87d0f8-8903-3601-9b65-011633dff8de | -12.53157 | -47.08695 | 2026-09-18 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bbc722e1-5e55-33a0-8a4d-bf7890482e95 | -10.62576 | -50.2509 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| f748c2d1-cc37-35fc-ad6e-db9a5dfc2fec | -9.78981 | -46.0942 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a6befac-68e4-37de-93b0-eaa5dd968fbc | -11.32599 | -43.35051 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 584680e3-659d-323b-bc6d-090c337e165d | -13.61733 | -46.95682 | 2026-09-18 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ce5c0c05-81b4-3a28-ba66-825589a7de6c | -11.52373 | -46.87736 | 2026-09-18 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b52c8011-d6d4-3d8c-bed2-8c5659c33f2d | -8.3034 | -50.96252 | 2026-09-18 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce5a8305-af95-3b46-9a99-7ef851be5573 | -10.51865 | -46.73518 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8af163db-ec64-36eb-962d-032ccfb3b6f7 | -9.72469 | -47.75825 | 2026-09-18 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a3c499f-eeed-307c-b2c2-ba4e25842fc6 | -9.95595 | -45.68494 | 2026-09-18 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dd6d8ada-ed7b-3731-9991-6719d44feab8 | -9.91078 | -46.5563 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 88b180f7-4a3d-3660-8a47-9ad1b4e84047 | -9.60757 | -45.84658 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3574f156-5add-3db9-8456-5f5373734c5f | -12.31246 | -47.96429 | 2026-09-18 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1f99740d-00ee-3440-857f-74f5ba5b7528 | -12.61977 | -50.88094 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb01e4ea-321d-31f3-aab3-23a227f7272d | -11.29699 | -43.39609 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db010ae0-e446-3570-8cfc-bc71be4d2a8b | -10.66585 | -50.4895 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90678174-059e-3ab3-b7a7-aec027cdd9e6 | -13.621 | -48.30407 | 2026-09-18 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8d666b3c-412a-3ab0-bcc3-cc2a2483c084 | -10.11482 | -45.64997 | 2026-09-18 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e3cba8e2-31bf-304f-8021-cdbf046cff59 | -10.83629 | -44.96253 | 2026-09-18 04:21:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d08cbc0-588b-319e-b892-8bf68fee301a | -12.27738 | -50.75809 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d9f269b3-bed3-325b-b51a-07bb26f48d39 | -12.16704 | -46.98306 | 2026-09-18 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3f269765-d142-3274-aec6-f8bf7c73071a | -12.47955 | -50.68755 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e83a607-add0-3a48-84d4-51c053de6bbb | -14.22655 | -48.51003 | 2026-09-18 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0cdebb03-5187-378b-be28-978bca5d1ddd | -10.40192 | -48.67752 | 2026-09-18 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b419ec64-e255-30d3-80cc-7c9afb1bbf32 | -12.25681 | -48.15549 | 2026-09-18 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e8d9036e-2ece-318b-a13c-d444d89c9346 | -8.46543 | -44.53071 | 2026-09-18 04:21:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f253f6f-aa41-3bfa-8ad0-522666644112 | -11.07238 | -48.28682 | 2026-09-18 04:21:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c14626f-2fea-3675-b095-6f0feca58adf | -11.29407 | -43.36736 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46a96196-afc6-3b08-8b9e-fa28ce9d5152 | -8.25627 | -45.63364 | 2026-09-18 04:21:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ea01969-a0a5-3231-8763-a42c32b33122 | -7.74968 | -54.7487 | 2026-09-18 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 851ee34f-b1f4-32d1-9c5f-348fdba21d3a | -13.00154 | -46.93492 | 2026-09-18 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 70ac0031-2829-3f36-b871-21cc6d305489 | -10.40109 | -46.61806 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7d1d483-5aa7-3288-b892-29abaed1d282 | -9.18542 | -45.69704 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 95f7ebf4-a4e2-3d32-b371-826615a8aa1d | -12.62156 | -50.88847 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb977650-188d-3fa2-af51-cc46aa9a1778 | -8.84458 | -45.91717 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 58b6e5d5-8ff0-3a1a-b25d-eed04fd6f8f4 | -11.80768 | -58.177 | 2026-09-18 04:21:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b10b5d97-4f59-3bc7-bf84-e0495266314f | -11.02054 | -54.15103 | 2026-09-18 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81d51458-e2c8-38fe-8f0b-072f4532ee9e | -12.55402 | -50.71592 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 03855841-c842-30dc-bc3c-91b352312734 | -11.30108 | -43.39267 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d6d4169d-81a8-31ee-b64d-7b518217c4d5 | -8.73714 | -45.41154 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 400958a0-3c68-3143-94da-8718ff464546 | -10.38199 | -46.63267 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4826dce7-c3dd-30e2-8915-467dc82c9717 | -13.6295 | -46.94426 | 2026-09-18 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ae0683d2-16de-372c-a257-8985aa4f29cd | -14.80403 | -48.5495 | 2026-09-18 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a283f202-a463-3c8d-b481-3da91e3d393e | -12.12946 | -45.15075 | 2026-09-18 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8751a11d-2b88-3a46-aba7-b335c505cae7 | -12.2993 | -50.74664 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 08086690-d9af-3aec-8eda-709e34e96b2c | -9.73908 | -46.11476 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e075eba-86c8-3d61-8f80-4b17eb9e6ad4 | -8.53799 | -44.5454 | 2026-09-18 04:21:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f033ad5c-10c5-3a54-baa8-ab7902940bd1 | -9.39116 | -46.8457 | 2026-09-18 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 29868fb1-50fc-347e-be2e-11171ddbf962 | -10.71427 | -54.0178 | 2026-09-18 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6db0c37e-71d2-3bac-8bb3-4ea1e7fc9616 | -11.33699 | -44.02038 | 2026-09-18 04:21:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a97cd91-1ef9-371d-94c6-51c4fefd7a6c | -11.30899 | -46.77275 | 2026-09-18 04:21:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 769e7a84-1622-3f2b-8dab-9ae7d93c2335 | -10.48548 | -45.29706 | 2026-09-18 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b67d3aa2-7d45-3798-8ad3-68d7b4f55b66 | -9.90365 | -46.51533 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc30bfc3-b66d-3028-9787-b4f44011cf90 | -9.71544 | -48.15303 | 2026-09-18 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 118d8b47-f5f4-3145-b32b-9549a702879e | -8.49883 | -57.63527 | 2026-09-18 04:21:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 469c8dfb-8ec1-3f5e-a638-5616bcdfc5dd | -9.57206 | -46.56694 | 2026-09-18 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9708c243-d447-36de-b9d1-45f413a4c82b | -11.49409 | -47.65804 | 2026-09-18 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6bd3945-df4f-3250-b7a5-67828b6ec73a | -9.92458 | -46.57677 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bce06a6c-ce4b-3739-bb51-31a1bc2b5b47 | -9.85921 | -48.38003 | 2026-09-18 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7c704bd3-9278-3047-a341-69b78651432a | -10.87757 | -54.00603 | 2026-09-18 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 42e1ad01-83e1-3fba-989c-6dc1d14febd1 | -11.29174 | -43.35891 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 174f20e5-c9d2-35dc-ac69-ce884ad4a5db | -8.87484 | -45.85402 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0cb89a5f-27fc-3f39-8f0d-4a9cc989d267 | -11.21424 | -42.8223 | 2026-09-18 04:21:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0fd5543b-1aa5-313b-98bb-6acd994c0654 | -9.59824 | -45.86292 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 6a166902-351a-3db9-9aef-e84d9d31cc65 | -10.36915 | -50.45659 | 2026-09-18 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0d011cb-8bfe-321c-bc5c-71fd6e28e538 | -8.43958 | -45.70181 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4542c43-4d2a-3a43-92a4-117a7cd969e2 | -10.1625 | -45.36461 | 2026-09-18 04:21:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 79f51655-f5a4-325e-8821-6b7d6e200bc6 | -11.28297 | -43.36971 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6c1095d7-d05f-3900-9ee4-db698fbf2981 | -10.66653 | -50.26799 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 56f3e6ed-33bb-32b7-9426-c3b5c1480048 | -7.75031 | -54.74518 | 2026-09-18 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 474347fb-776e-37d2-8f41-fa0bea69fdce | -11.3212 | -46.76018 | 2026-09-18 04:21:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4e6b4d5f-9e4a-3e17-8fc7-6b7a6069269d | -8.55745 | -44.90274 | 2026-09-18 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e880b71-9ed8-3dc1-9902-fec1ce945c54 | -9.9153 | -46.50631 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c36aaabc-c09d-3d12-b3bf-3e828eae321f | -14.77161 | -47.16625 | 2026-09-18 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f90c3674-8a84-3439-a665-05cb24ca1d4f | -15.45103 | -43.81513 | 2026-09-18 04:21:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c2d52d1-0d32-3cd8-8d1c-9ecd61ccec95 | -9.16015 | -50.00004 | 2026-09-18 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 28a4452e-c491-3407-9462-b6ea4e7213fb | -9.71293 | -54.80983 | 2026-09-18 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README49.md)
