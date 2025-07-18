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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6e25ce1-d258-3468-843b-0c956d0569b9 | -10.71761 | -49.49371 | 2025-07-18 01:05:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 93a6ed23-d21d-395d-a1ed-f650225cc5b1 | -8.88762 | -50.16179 | 2025-07-18 01:05:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 401d0435-0f6d-3bbe-a731-89f17d3c3e84 | -10.81968 | -49.27927 | 2025-07-18 01:05:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 4be966e6-e7a6-37ec-a0d5-6df71b2963af | -5.99696 | -52.19557 | 2025-07-18 01:05:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 48fcdcc1-93a8-3801-9d00-ed58827ce937 | -12.03791 | -48.76014 | 2025-07-18 01:05:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| a251d3d8-6936-30fb-9224-037ad9c361f3 | -5.99995 | -52.20126 | 2025-07-18 01:05:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 5e73e9f2-5f91-3982-a5dd-25feb7847abe | -9.86588 | -60.30123 | 2025-07-18 01:05:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 61341731-99b1-34e7-b279-d4ea40ff23d4 | -9.77609 | -48.76962 | 2025-07-18 01:05:00 | TERRA_M-M | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 2664f6b2-b627-3726-9c3b-4571077ce53b | -11.57283 | -47.06895 | 2025-07-18 01:05:00 | TERRA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 0aef5aee-a27e-31ae-a17f-28c0fc0d6044 | -11.73553 | -48.19815 | 2025-07-18 01:05:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 8bbaaa27-03fd-3f69-bdd2-eb0e6fee5f0d | -10.71508 | -49.47749 | 2025-07-18 01:05:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 2ad70468-f22e-3c91-8b3c-904d042955b9 | -7.36135 | -49.61043 | 2025-07-18 01:05:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 267a1017-2647-3e31-b42b-827f83e227b7 | -5.99875 | -52.20751 | 2025-07-18 01:05:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2947c5e4-3413-3f3c-97a5-df3cdd5633e0 | -7.35563 | -49.59834 | 2025-07-18 01:05:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 49a3c8e1-7341-313b-aa62-258fe62b8bef | -11.55898 | -47.07153 | 2025-07-18 01:05:00 | TERRA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| a3870f24-df37-3730-b7c3-cf99e0aecb2d | -9.89173 | -65.17588 | 2025-07-18 01:05:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.7 |
| c1418c84-dca8-3b29-938a-f6f0870f63c0 | -7.3585 | -49.59238 | 2025-07-18 01:05:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 85545ff1-37bd-3088-a94b-f39af7e1d45e | -11.56314 | -47.09589 | 2025-07-18 01:05:00 | TERRA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 7f46146f-10e4-3882-a85d-9077849ece9b | -9.49003 | -64.11488 | 2025-07-18 01:05:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.3 |
| aeaca4a1-b87e-3849-a2bc-bdf317a851f6 | -11.73238 | -48.18397 | 2025-07-18 01:05:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 001432b5-89bf-3c33-940c-8b0be16d95a8 | -6.56867 | -51.1153 | 2025-07-18 01:05:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 0a859e67-165f-39a0-b2fd-bf6e764d1e84 | -9.77313 | -48.75082 | 2025-07-18 01:05:00 | TERRA_M-M | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 29.3 |
| c05255de-ed5f-3385-ab44-e6e2161373ea | -8.88527 | -50.14639 | 2025-07-18 01:05:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 64433183-61a0-3d9e-ac12-a5c9fd9d0d51 | -10.68477 | -56.54552 | 2025-07-18 01:05:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 6ee4e397-f5a9-3145-9fea-a53190ae1b89 | -4.3052 | -48.0987 | 2025-07-18 01:07:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 03f3931e-8653-34e0-8306-02e0dce42242 | -3.72883 | -53.99463 | 2025-07-18 01:07:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 7ffcbaf1-1d33-35e4-a05c-2610aebcb2ea | -4.31007 | -48.11847 | 2025-07-18 01:07:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 360ed654-49ef-3580-b911-9056636bbf14 | -3.40593 | -47.48769 | 2025-07-18 01:07:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| f800a8d2-1746-3435-b132-6e8408f5aad9 | -3.39559 | -47.49445 | 2025-07-18 01:07:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 147.1 |
| 9161cd32-ecbe-3261-be92-58f55bc44a0e | -3.12707 | -47.01398 | 2025-07-18 01:07:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| dc5918ca-f543-3f08-ac76-2eae0bd7cfab | -3.37998 | -47.49678 | 2025-07-18 01:07:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 1eaa0526-d16d-3ac4-97a1-e6b86a509ab5 | -4.30911 | -48.12537 | 2025-07-18 01:07:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 2e30585b-64e0-3498-ad7a-40767b1d7ab9 | -3.11087 | -47.01677 | 2025-07-18 01:07:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 73572691-d662-3002-a122-e1243af88dd6 | -3.39035 | -47.49024 | 2025-07-18 01:07:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 234.3 |
| 509946b0-4f7d-364a-92cd-f4ca89d480ff | -3.39105 | -47.4632 | 2025-07-18 01:07:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 4ea5a353-0485-3d6f-b8f4-82fffd341898 | -3.73826 | -53.99323 | 2025-07-18 01:07:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 2d4c7286-84f6-307c-9432-c55721d80bdb | -3.11759 | -47.01026 | 2025-07-18 01:07:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| bdde0ab8-e62e-391a-a8b0-2dbc09e5cd6a | -4.30596 | -48.09175 | 2025-07-18 01:07:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 051b15b3-77fa-34b9-a418-4b7f9bb2ca59 | -5.6565 | -43.7393 | 2025-07-18 01:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| c9a443f1-367e-38e6-9ba7-78fc7c9bbf0e | -8.0883 | -43.1667 | 2025-07-18 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 170.6 |
| 0c1a3d54-3ff9-36bb-9945-e152a669332b | -8.0696 | -43.1452 | 2025-07-18 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 130.6 |
| 19f9fa41-4de9-3f5c-93c1-1a04c8292632 | -8.0886 | -43.1431 | 2025-07-18 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 330.4 |
| a46b643d-4d4b-308a-9c13-e30ecd0b2acb | -5.6379 | -43.7175 | 2025-07-18 01:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 2ffd1a32-3846-342d-b63d-c07e0f9e7094 | -3.3772 | -47.4792 | 2025-07-18 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| d81967c8-4c6a-30cc-8f5c-c931f4640fac | -8.0693 | -43.1687 | 2025-07-18 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.5 |
| 277669cc-cb15-3760-917b-874578e6ba89 | -5.6567 | -43.7161 | 2025-07-18 01:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 302.9 |
| e1a0bdd7-0a4f-3700-b75e-f7127a0a5dfa | -3.3958 | -47.4785 | 2025-07-18 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 133.4 |
| 752a7e73-ea34-300c-a878-fd7ca99258a4 | -11.7317 | -48.1849 | 2025-07-18 01:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| c38bceba-f02c-3d2f-9594-cd8f32f01a36 | -4.301 | -48.1133 | 2025-07-18 01:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 819459cd-a07c-33ec-add7-d278d4a3dee4 | -11.559 | -47.0742 | 2025-07-18 01:10:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 00252655-f961-3bda-9621-a431845b5452 | -5.6569 | -43.6929 | 2025-07-18 01:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 117.8 |
| d2d42380-1054-30c8-97fc-c06430b4d62f | -3.1198 | -47.0075 | 2025-07-18 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 9a90ca2f-6fa7-3b1d-b5e9-097fb34d636d | -8.1075 | -43.1411 | 2025-07-18 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 97.9 |
| 34d4a8e8-b4d4-361e-b0ba-c15556a896ce | -3.3957 | -47.5003 | 2025-07-18 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 97d375b8-141d-36a0-a241-69358e377c36 | -15.0959 | -49.4458 | 2025-07-18 01:20:00 | GOES-19 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 53.0 |
| b180807d-de7e-352f-9c6a-b192c38de047 | -5.6567 | -43.7161 | 2025-07-18 01:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 321.9 |
| dab35e4a-2154-31b0-a5f4-712feb30ead0 | -11.559 | -47.0742 | 2025-07-18 01:20:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 67c46a3c-35d3-355e-a76e-3e129fbc68e2 | -5.6569 | -43.6929 | 2025-07-18 01:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| d7aeb940-6465-3f51-bac5-ece962ff2a93 | -8.0696 | -43.1452 | 2025-07-18 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 124.8 |
| 0950dbab-8963-3156-8721-df002e938a57 | -8.0883 | -43.1667 | 2025-07-18 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 195.7 |
| c129ca4b-5c7f-3e03-9c5d-886a7a1bd9d9 | -3.3772 | -47.4792 | 2025-07-18 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 796e4684-4fc8-37e0-ad91-91da91306b6d | -8.1072 | -43.1646 | 2025-07-18 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.7 |
| 9d056cc6-01b1-3b14-89f6-d194da64cfdf | -11.7317 | -48.1849 | 2025-07-18 01:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 5a8978aa-4fa7-3f32-bcd6-9e0e3089252a | -3.3958 | -47.4785 | 2025-07-18 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 148.8 |
| 22f38db5-4e57-338c-8624-f614e2b4b0f1 | -3.1198 | -47.0075 | 2025-07-18 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| ecdcd97a-a8e4-3698-8444-b7ee44377263 | -8.0693 | -43.1687 | 2025-07-18 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |
| 96e39a43-a28e-399d-9ce9-aa4124861f26 | -8.0886 | -43.1431 | 2025-07-18 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 309.3 |
| d6a2659e-9abf-342c-974c-fd18bd21e14c | -5.6379 | -43.7175 | 2025-07-18 01:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| b38a0333-e83f-3cfb-bade-e76177134ffd | -8.1075 | -43.1411 | 2025-07-18 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 107.8 |
| 32329522-c238-3a09-a5b3-70a53e00a33d | -5.6754 | -43.7147 | 2025-07-18 01:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 159211d9-8b7f-3f4b-ae48-8a3b9dc61891 | -3.3957 | -47.5003 | 2025-07-18 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 478ebfb4-528d-3fdf-a7aa-96badd8e6c9f | -5.6567 | -43.7161 | 2025-07-18 01:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 329.9 |
| bc9a5376-8c4a-386c-91b3-0b3dbe279009 | -3.3772 | -47.4792 | 2025-07-18 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 74ddb48f-3501-33b0-afb8-6c2da35f37f0 | -11.5778 | -47.0941 | 2025-07-18 01:30:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 26442fef-10be-3f1a-8119-2b84e1a83b23 | -3.1198 | -47.0075 | 2025-07-18 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 4436a322-b594-3b2a-8e79-9911d00fc455 | -8.0696 | -43.1452 | 2025-07-18 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 98.0 |
| b7f3403d-2913-33f3-8786-0431ca725071 | -8.0886 | -43.1431 | 2025-07-18 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 324.4 |
| 04206bcb-411b-375e-8921-a4728ca77796 | -3.3957 | -47.5003 | 2025-07-18 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| c2b1be3d-5690-36ef-a13e-48bc2275629b | -8.1075 | -43.1411 | 2025-07-18 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.7 |
| f3491555-e22a-3b88-abc1-8b9db6029cf3 | -11.7317 | -48.1849 | 2025-07-18 01:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 1e845e5e-8371-3400-a7ef-b23209fd5f64 | -8.0883 | -43.1667 | 2025-07-18 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 186.6 |
| 3499e371-2a73-32d9-b586-5443a48f332c | -8.0693 | -43.1687 | 2025-07-18 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.4 |
| 29f22006-3e64-30eb-8062-b99f91742508 | -11.7508 | -48.1825 | 2025-07-18 01:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| c25f2ca9-07b9-323b-8540-2f64eb01f212 | -5.6569 | -43.6929 | 2025-07-18 01:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 714e0e30-a4bb-36d2-85e5-bb705504d297 | -3.3958 | -47.4785 | 2025-07-18 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 147.4 |
| f7c72d1d-3fc5-3a36-9c72-8f3ef22f9209 | -5.6379 | -43.7175 | 2025-07-18 01:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| a5274bc3-bc18-3e54-9d9d-84a8e37aae06 | -7.4925 | -63.817101 | 2025-07-18 01:39:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c51acefd-ebf3-3398-b992-c9a455a98cfb | -9.8819 | -65.161903 | 2025-07-18 01:39:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 323db398-f169-3f2c-a759-6fff1eb4ab5b | -10.2989 | -60.540298 | 2025-07-18 01:39:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 648285a1-a011-34af-bd8f-85e8cfd35dac | -21.0389 | -55.9818 | 2025-07-18 01:39:00 | METOP-C | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 8bae5545-44af-3543-a059-bed0c2b38294 | -9.8836 | -65.1698 | 2025-07-18 01:39:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 142d7796-a676-3136-ac8d-6582991f373e | -9.0227 | -61.223301 | 2025-07-18 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 97feef3a-7a73-3bc6-9e0e-412eac8f164a | -9.4934 | -64.104301 | 2025-07-18 01:39:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7d172d1e-cdef-36d2-932d-bc6c04697f54 | -9.021 | -61.216099 | 2025-07-18 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3adcc80e-d65a-3abc-82b6-632fcdd53567 | -7.491 | -63.8102 | 2025-07-18 01:39:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8fe5b113-67bd-31b2-8fc5-94030d60729c | -9.8801 | -65.153999 | 2025-07-18 01:39:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6763f490-4a04-3763-bced-ebfccd2890cc | -18.659901 | -55.719501 | 2025-07-18 01:39:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d2b2a214-1ac6-3dd9-9420-cf5ac55ef22d | -5.6569 | -43.6929 | 2025-07-18 01:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| b187da3a-c4a4-3612-a6cd-e7c60fa7f8dd | -3.3957 | -47.5003 | 2025-07-18 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 3f734cc6-f553-381a-a743-d2d325fbba54 | -8.1075 | -43.1411 | 2025-07-18 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 99.6 |


[Clique aqui para ver as próximas entradas](README5.md)
