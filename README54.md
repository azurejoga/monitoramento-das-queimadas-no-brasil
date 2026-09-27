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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2b5b518-1f6b-3425-aec5-df9a26ae1646 | -5.27792 | -48.3738 | 2026-09-27 11:45:00 | TERRA_M-M | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 2eca35ab-5a5d-3258-bbf4-ba1e735e1f7d | -5.73625 | -45.01816 | 2026-09-27 11:45:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 04d49a10-770f-32ed-8ddf-fdddc3fcaac4 | -11.42973 | -47.4248 | 2026-09-27 11:45:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 85ab144e-033f-3f80-bcdf-7f1d31234315 | -10.76374 | -52.13182 | 2026-09-27 11:45:00 | TERRA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |
| ddc80abd-b4ca-3f49-89b1-c9a629e04ada | -6.7778 | -48.6585 | 2026-09-27 11:45:00 | TERRA_M-M | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 58f1bdb9-d97b-3a41-8d3e-f03c71f50a18 | -12.12081 | -50.29497 | 2026-09-27 11:45:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| eae4bb9c-9f72-3104-a167-9a16ff59ad0e | -12.11933 | -50.30485 | 2026-09-27 11:45:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| a511ec44-1b14-3e65-84c3-ebbb093acdf5 | -5.73627 | -43.28045 | 2026-09-27 11:45:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 6556a439-4068-3491-a7c5-89d860515b58 | -9.78809 | -44.83037 | 2026-09-27 11:45:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 94e79d19-cc6e-34dd-8252-f01d21a385bf | -12.2352 | -50.40002 | 2026-09-27 11:45:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 71a90862-b5d0-3efd-be0f-8cbef8d646c1 | -14.72415 | -45.5781 | 2026-09-27 11:45:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 63f6de48-e1c5-360d-88da-8f8fc22ac0a4 | -17.91244 | -42.69093 | 2026-09-27 11:47:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.9 |
| 77bb60ff-7733-3440-b004-09a15c24be3c | -19.97568 | -44.15455 | 2026-09-27 11:47:00 | TERRA_M-M | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.4 |
| b1d40553-57c8-3717-8d98-40ec1e498eaf | -20.49331 | -46.20803 | 2026-09-27 11:47:00 | TERRA_M-M | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 5475d5bc-76fa-342f-93dd-b84ddc65129f | -20.19821 | -46.20385 | 2026-09-27 11:47:00 | TERRA_M-M | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 27.3 |
| b93f9800-d341-3566-8b46-0ee6e8299344 | -17.78841 | -47.15817 | 2026-09-27 11:47:00 | TERRA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 59e5fd97-9229-3462-af2c-4b50f8c18fcd | -20.19972 | -46.19101 | 2026-09-27 11:47:00 | TERRA_M-M | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 35.1 |
| b7adc819-4d11-3dd2-bd74-7e18da5a60cc | -16.67845 | -49.61687 | 2026-09-27 11:47:00 | TERRA_M-M | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9c084d7f-c908-314d-9a76-073ad03c939f | -19.9807 | -44.16171 | 2026-09-27 11:47:00 | TERRA_M-M | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| ed5cd230-258a-3ed0-885e-1b6e61f967ae | -22.37553 | -48.78097 | 2026-09-27 11:47:00 | TERRA_M-M | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 3c8b6ad7-6fbe-31de-8c3e-5f4f89b159ec | -26.97979 | -52.18134 | 2026-09-27 11:49:00 | TERRA_M-M | IPUMIRIM | SANTA CATARINA | Brasil | 4207700 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 412d2ddc-aecb-372c-9524-6f8664dc7acd | -23.32309 | -52.30929 | 2026-09-27 11:49:00 | TERRA_M-M | FLORAÍ | PARANÁ | Brasil | 4107801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| decf5a77-a021-3dfd-af08-ba6acb6f06ad | -23.33384 | -52.23911 | 2026-09-27 11:49:00 | TERRA_M-M | SÃO JORGE DO IVAÍ | PARANÁ | Brasil | 4125308 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| afb6ecca-f2bb-3e0c-a4e1-9eadb49df70f | -7.3842 | -42.1039 | 2026-09-27 11:50:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| 6a1588d0-424a-3eb9-93d1-f892a6ff408a | -7.3653 | -42.1058 | 2026-09-27 11:50:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 83.9 |
| 7bc46bc8-ecd5-33d7-b91c-cf2efbb8adde | -8.3589 | -44.1406 | 2026-09-27 11:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 415.1 |
| dfe9ddc1-619d-3f01-a5cb-698bdd297a2c | -14.1105 | -46.3293 | 2026-09-27 11:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 75.0 |
| c9e42858-79df-3145-9903-354f2b0f3b7f | -14.13 | -46.326 | 2026-09-27 11:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 164.2 |
| f141832b-54d1-33be-b357-ddceea72b358 | -8.3778 | -44.1386 | 2026-09-27 11:50:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 6cf4e0e9-aba0-3b7a-a0a1-3cbbcfdd9b7e | -8.3586 | -44.1638 | 2026-09-27 11:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 849.1 |
| 70a5c875-47f3-3d98-9fca-34bcc8c0549c | -7.365 | -42.1298 | 2026-09-27 11:50:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 78.6 |
| 83f4ae93-5b7b-34e3-85bc-c6a9b721b992 | -11.9244 | -50.4866 | 2026-09-27 11:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| e64ea2fd-f42f-3c35-964d-9c6f7dc9b682 | -6.8408 | -43.5021 | 2026-09-27 12:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 173.4 |
| 68a55adc-40ec-31da-a3c3-9a130c636e1d | -12.1366 | -50.3112 | 2026-09-27 12:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.6 |
| d14c9f4c-e31d-34d6-afea-9ac8a034c109 | -12.2307 | -50.3858 | 2026-09-27 12:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| ee593630-cefb-3347-aae7-d62488da8e32 | -10.0162 | -50.1374 | 2026-09-27 12:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 74f859a8-4f1c-3bc8-b87f-9158cec6679c | -14.13 | -46.326 | 2026-09-27 12:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 38b01306-8b18-3b02-8185-2bba52e77715 | -12.1362 | -50.3328 | 2026-09-27 12:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 148b9e68-7b8c-36a6-9f79-a8332cf715e7 | -8.3397 | -44.1658 | 2026-09-27 12:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 4adbafb6-a313-32b9-be84-40125dd973db | -7.3842 | -42.1039 | 2026-09-27 12:00:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 88.8 |
| 9af3bbe5-323a-32dd-a3c9-ac024c40493f | -8.3778 | -44.1386 | 2026-09-27 12:00:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 128.4 |
| c68e3036-b402-38c6-a720-45771f5587a3 | -11.9244 | -50.4866 | 2026-09-27 12:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 1df8e7d0-6367-3c24-a2ce-5cb329cb3261 | -8.3589 | -44.1406 | 2026-09-27 12:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 243.2 |
| dc38319f-5bf8-3b9d-8fb6-4db6c56cc36b | -12.1175 | -50.3135 | 2026-09-27 12:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| a86a136a-c1c9-3ce3-be4c-bd499cd34961 | -8.3586 | -44.1638 | 2026-09-27 12:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 556.9 |
| c0a399da-1fab-3a4c-8324-b484b6c6b3f3 | -6.8405 | -43.5254 | 2026-09-27 12:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 9d9de912-d0c9-360d-91b9-7670b74a599c | -7.365 | -42.1298 | 2026-09-27 12:00:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 191.6 |
| 0c81a1c1-285d-32f4-8e7b-4ade2b7487c9 | -12.2884 | -50.3573 | 2026-09-27 12:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 48518404-48df-3557-946f-cba775b9aa52 | -7.3653 | -42.1058 | 2026-09-27 12:00:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 149.3 |
| a4be900e-c697-36ee-9220-a02c2203380b | -12.288 | -50.3789 | 2026-09-27 12:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 3dcd09e1-9e93-39d7-8467-3acdb98f0d36 | -8.3583 | -44.187 | 2026-09-27 12:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 3b480771-cd58-3372-883f-3d7d288a524c | -7.3653 | -42.1058 | 2026-09-27 12:10:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 138.6 |
| f6c647c8-a5a5-317b-b985-5e0f89eb04ad | -12.2307 | -50.3858 | 2026-09-27 12:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 834b3385-606f-35be-ab25-e13a06fa4507 | -12.1362 | -50.3328 | 2026-09-27 12:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 6bf7e884-ac73-34f6-a3dc-d0d423bb19c5 | -12.1366 | -50.3112 | 2026-09-27 12:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 134.2 |
| a8890224-d98d-36f2-8c83-7e0833f77a73 | -6.8408 | -43.5021 | 2026-09-27 12:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 245.8 |
| 8679ba2b-2af2-3355-9a8c-0dabe25ee6f1 | -7.3842 | -42.1039 | 2026-09-27 12:10:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 80.4 |
| cd026859-160d-372c-a8ad-48e68fb09c08 | -7.365 | -42.1298 | 2026-09-27 12:10:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 146.6 |
| 7a492892-b891-3a17-ba94-1e9d9942a7df | -12.1175 | -50.3135 | 2026-09-27 12:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| efe8d591-658b-3050-b9c7-17fcd0e57738 | -10.0162 | -50.1374 | 2026-09-27 12:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 01d823d2-3da9-3986-8afc-09923f61d054 | -6.8405 | -43.5254 | 2026-09-27 12:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 169.2 |
| bd9daa53-3f2f-36ed-8856-eb4cadb85605 | -11.9244 | -50.4866 | 2026-09-27 12:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 4acdc319-949a-3517-8629-d2ba5632a3c0 | -14.13 | -46.326 | 2026-09-27 12:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 06d10a11-8ddb-30a3-8aea-f8ead7eeb5f1 | -11.924 | -50.5081 | 2026-09-27 12:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 09615fba-7eb8-357c-aa92-8754349f4170 | -8.36 | -44.16 | 2026-09-27 12:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e52b44a7-dfca-3257-9c1c-e96e06c59ab9 | -12.1366 | -50.3112 | 2026-09-27 12:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 9864d9d4-f24e-36c0-83b4-779d16def7f9 | -11.905 | -50.5103 | 2026-09-27 12:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| fef46c80-d069-3633-ae48-2950b942284a | -8.3586 | -44.1638 | 2026-09-27 12:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 614.6 |
| f8883dd5-2130-3613-83d2-22797cd54c6c | -8.3589 | -44.1406 | 2026-09-27 12:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 420.9 |
| 39d45c3e-ee10-36c8-8721-d5a989c5b8d7 | -12.7028 | -47.3189 | 2026-09-27 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| c06c4a1a-f6d4-3a1d-abad-c9f47c8fe4ce | -6.8405 | -43.5254 | 2026-09-27 12:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 161.3 |
| 1cbd67f3-9ab0-3fd2-a940-7a1e33591a47 | -12.1175 | -50.3135 | 2026-09-27 12:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| b1457050-7a99-357e-862e-6273201b46a1 | -11.9244 | -50.4866 | 2026-09-27 12:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| a62387d3-c36f-312a-bc2e-dabc9e59eb0d | -12.2257 | -50.7079 | 2026-09-27 12:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| a82f59f7-d389-302f-a75f-adbf4847d90c | -11.8669 | -50.5147 | 2026-09-27 12:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 561f9bc9-b334-3f16-8995-a952a96ca47b | -10.0162 | -50.1374 | 2026-09-27 12:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 5c349195-8192-3abb-b6e1-27801777b9b7 | -8.3583 | -44.187 | 2026-09-27 12:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 97bdb7e2-e4ed-30bc-8b09-01d63d40d830 | -11.8859 | -50.5125 | 2026-09-27 12:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 803c9a02-c9f9-3e76-b528-f91ff4cb359e | -11.924 | -50.5081 | 2026-09-27 12:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 1b8c2961-e8ff-38ec-aa6a-a0ad5aa57620 | -6.8408 | -43.5021 | 2026-09-27 12:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 164.3 |
| 28bbdc3d-857b-3503-97ca-c3a483d457c5 | -7.3653 | -42.1058 | 2026-09-27 12:20:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 104.2 |
| 15715195-d555-38f5-b633-a2e9ae9797c7 | -14.13 | -46.326 | 2026-09-27 12:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 76.1 |
| effa871e-311b-340d-8bb0-19715bcc8fe5 | -7.3842 | -42.1039 | 2026-09-27 12:20:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 88.5 |
| a0dfdf37-ec7c-32f7-99bd-01ad1a7b9f32 | -11.8862 | -50.4911 | 2026-09-27 12:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 0d06bf34-e6c7-35a4-bbe2-3960ac3294d4 | -8.3778 | -44.1386 | 2026-09-27 12:20:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 171.2 |
| 14428d18-9b73-3edb-9533-c49a8f6e6256 | -11.7643 | -51.0173 | 2026-09-27 12:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 3732c542-c918-34d6-8761-411ccb552ff3 | -12.2448 | -50.7057 | 2026-09-27 12:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| f6876b12-8519-3d6d-858b-9a828a3b677b | -12.2307 | -50.3858 | 2026-09-27 12:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| cc4bd52f-3fc0-3adf-9684-64211263c741 | -12.1362 | -50.3328 | 2026-09-27 12:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| d65a7868-f3ce-3c64-82f1-715c16ab5117 | -7.365 | -42.1298 | 2026-09-27 12:20:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 133.3 |
| e48b6d14-c6b0-3971-95f2-984b995b4fc6 | -12.7221 | -47.3161 | 2026-09-27 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| e8034146-4499-371e-ba8f-c8a85396875d | -10.0159 | -50.1588 | 2026-09-27 12:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| be2acdaf-00b5-3bb6-8b4c-29834b8d56d9 | -11.7647 | -50.996 | 2026-09-27 12:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| ceb47889-e38d-3177-beaa-f7a4bfd790fc | -10.0162 | -50.1374 | 2026-09-27 12:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| e9337536-4b03-3c07-bc7f-a89fc4ba945e | -12.2257 | -50.7079 | 2026-09-27 12:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 74.7 |
| eb872a62-929a-3568-b553-165f127f646a | -14.13 | -46.326 | 2026-09-27 12:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 9597ca36-9747-38bb-96b3-cd560323fef8 | -12.7028 | -47.3189 | 2026-09-27 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 669c09bc-2a60-33da-bea6-cd51807201a0 | -7.365 | -42.1298 | 2026-09-27 12:30:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 127.7 |
| d1960240-e856-3ca2-92f9-3cc787c4fd4a | -12.2448 | -50.7057 | 2026-09-27 12:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| b153dedd-3e88-308a-82dd-f0074c4eef1b | -11.7643 | -51.0173 | 2026-09-27 12:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |


[Clique aqui para ver as próximas entradas](README55.md)
