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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4134cff-1fa9-35b6-98bf-15ee8c0a94dc | -5.49853 | -42.74342 | 2025-09-30 03:47:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fbd39f9e-8eaa-3f87-baf0-62d1e0526989 | -4.39998 | -44.0815 | 2025-09-30 03:47:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c98ed306-889b-3e75-b576-9d5ab930c8e1 | -9.37347 | -47.59634 | 2025-09-30 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8e976db-3e88-3bdc-bb60-55d66d587651 | -8.8021 | -44.94593 | 2025-09-30 03:47:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 007f6f2c-7825-379e-adb1-af0e05cc79c5 | -3.25148 | -49.1304 | 2025-09-30 03:47:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 46d88c60-f572-3a82-b078-38663f17c73b | -4.79278 | -40.54934 | 2025-09-30 03:47:00 | NOAA-20 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 972f701e-d326-372c-8b64-b2369708bce5 | -9.12876 | -47.63421 | 2025-09-30 03:47:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f471cd75-affc-368a-b60c-1f8b673f1674 | -6.74417 | -34.98314 | 2025-09-30 03:47:00 | NOAA-20 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c5e27b27-c65c-3957-abbc-67c8e86f1b3e | -5.4199 | -42.28908 | 2025-09-30 03:47:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8992fb76-73b3-3d6e-af29-aadc9501a9be | -9.05734 | -47.62981 | 2025-09-30 03:47:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce3ab71d-304d-3270-ad30-19b8e65f5506 | -9.03102 | -46.71094 | 2025-09-30 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea493e7b-f0d8-3502-b622-2109160ab190 | -8.06727 | -42.9437 | 2025-09-30 03:47:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5e65946b-f2c6-3391-9038-8596d103d67f | -8.22682 | -45.51052 | 2025-09-30 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cd0efc54-ae4d-3fa4-a6b8-42e6d3abc33b | -7.66515 | -47.42231 | 2025-09-30 03:47:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e8c89a6-3034-3fd1-a430-da3ea6d4d7a3 | -8.96044 | -47.44759 | 2025-09-30 03:47:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 15421482-25ad-3e87-8810-96d08196a3d2 | -4.81427 | -42.76422 | 2025-09-30 03:47:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a5e8db31-0e05-394a-80fc-6b51d164a4cb | -8.64951 | -43.98053 | 2025-09-30 03:47:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30362caf-4bc9-3e73-80b8-bd009223cb0a | -7.82025 | -46.99666 | 2025-09-30 03:47:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d7f0d97a-5899-3b1c-a3c1-8e34ad20d920 | -4.86887 | -45.05852 | 2025-09-30 03:47:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 83cba2de-5592-325b-b664-85d8324a1b63 | -8.15803 | -46.38309 | 2025-09-30 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 031d8fce-f02e-38ab-846e-0ef699c922e5 | -10.03441 | -50.20061 | 2025-09-30 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3cd6b8f-3e03-30f7-a87b-324d07bc29dc | -10.64938 | -48.54497 | 2025-09-30 03:47:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6e3d79be-9be3-38b6-b7fc-269f08cad414 | -11.67729 | -44.29878 | 2025-09-30 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| feeea4ab-d439-34f4-a82a-77e47488fc0e | -5.89419 | -38.48095 | 2025-09-30 03:47:00 | NOAA-20 | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2bba6eb2-40d6-3f15-9851-777434025c86 | -5.02728 | -42.99388 | 2025-09-30 03:47:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 29d853e2-8078-35ce-930f-2e8330f5094a | -5.42415 | -42.28983 | 2025-09-30 03:47:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c402edd3-8aa4-3236-a3e7-df1fa83f3145 | -11.36279 | -44.94272 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1a1ca2a-15d2-3472-9626-958e40bc7361 | -5.25702 | -40.70359 | 2025-09-30 03:47:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 59779d6d-86ec-34b2-8830-403d3a2da0f9 | -5.04547 | -45.31352 | 2025-09-30 03:47:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1a13df2b-0838-35ba-bd8d-5e565616bc0d | -10.19478 | -44.90394 | 2025-09-30 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 248a32b8-9e12-376f-9389-c0e1e247883e | -8.24024 | -45.51512 | 2025-09-30 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75e778a6-0724-3ca2-9edb-d427c96a0764 | -11.49398 | -43.51757 | 2025-09-30 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13a05275-d325-3cbb-b704-e054fa79c235 | -8.26109 | -45.51508 | 2025-09-30 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ae278075-fcd9-3888-b0b5-b97ce6bd55fc | -4.86944 | -45.05525 | 2025-09-30 03:47:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1a47c1dc-5af5-3ead-8c6d-92bb19106799 | -3.67957 | -38.93821 | 2025-09-30 03:47:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7f24ba45-8c3b-33b7-8a23-2681e22dec69 | -9.95813 | -48.80941 | 2025-09-30 03:47:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05ac7cb5-47bc-30b2-b14a-e3fb50ed997c | -7.77041 | -45.7405 | 2025-09-30 03:47:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79815d1d-8821-3e53-8bac-9ae12ab9d1aa | -4.40245 | -44.39759 | 2025-09-30 03:47:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0cc1516-00ae-3dcd-9c43-afc70d70adb0 | -11.43699 | -44.95282 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dcbf53ef-fc9f-3245-8439-68dc3074d205 | -8.25342 | -45.52858 | 2025-09-30 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e1f0f2b-0dc2-3208-80f2-3247f826b845 | -10.11162 | -47.79042 | 2025-09-30 03:47:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1fac2eb-4276-30f0-ba37-0bc74b2439b1 | -4.45728 | -40.98082 | 2025-09-30 03:47:00 | NOAA-20 | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2431b3ed-73bb-32d6-b90c-f5192fd13082 | -11.37259 | -45.06977 | 2025-09-30 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| db7e6cae-1415-337a-af95-47af2bd111c5 | -8.15138 | -46.38931 | 2025-09-30 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 879542c8-4e90-3f9f-a5c2-0ffefb8af9d0 | -10.993 | -42.74437 | 2025-09-30 03:47:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fa0243aa-94c1-3f45-ba96-4cbea814b095 | -10.83234 | -47.97244 | 2025-09-30 03:47:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e57479cc-dfa0-3825-80da-60663b67e48d | -9.887 | -45.95772 | 2025-09-30 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 797231f6-bdd6-39c5-aa51-3cc9728ab74f | -11.43613 | -44.95751 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74d5d672-2ccb-3f21-b5cb-0ed830bf0ee8 | -10.8708 | -41.61509 | 2025-09-30 03:47:00 | NOAA-20 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 96d1beb3-b9df-3206-8cb9-3a0902f9c416 | -10.03728 | -50.19543 | 2025-09-30 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5fa02938-48f7-31b9-8b2e-7892a52e03b1 | -8.67047 | -47.71196 | 2025-09-30 03:47:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3c6fd167-083f-319b-924b-254280c2177e | -8.25391 | -45.52591 | 2025-09-30 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8f2ca70-2c7b-3f00-beb3-16c6a9c4516c | -4.392 | -44.39867 | 2025-09-30 03:47:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30c43201-a284-3ceb-86fa-e934c884dfdb | -4.86379 | -45.05085 | 2025-09-30 03:47:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c16f29b-4976-365f-b8b2-71ceb760b140 | -7.91348 | -44.63057 | 2025-09-30 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 64f4069a-ab43-3d73-a41f-1e1c91febe12 | -8.24723 | -45.53394 | 2025-09-30 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be72c22a-191c-3402-a050-cc7143d654c5 | -7.91131 | -44.61492 | 2025-09-30 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 59ffe3dc-6c52-3ec3-94f1-ec68292c894e | -7.36794 | -47.05081 | 2025-09-30 03:47:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 81428fe1-427c-3dec-ba45-4d3948851f55 | -5.35345 | -42.29419 | 2025-09-30 03:47:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3616f9e3-4a50-315d-ba4d-cfee433b2aee | -4.89662 | -43.46496 | 2025-09-30 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 4fdf12d3-1403-33a9-9344-6d5ea424a9f2 | -8.24834 | -45.52785 | 2025-09-30 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83a3b598-bdbc-3ad0-a16f-0da613d1eeff | -4.6727 | -45.69255 | 2025-09-30 03:47:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24fad102-fa0b-3be2-925e-cffee20ed94d | -7.845 | -47.25915 | 2025-09-30 03:47:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4509f566-d599-3909-8a4b-dd4c4c617821 | -10.19103 | -44.89807 | 2025-09-30 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 04d922aa-06ab-3df3-a703-338964c3b651 | -5.0449 | -45.31679 | 2025-09-30 03:47:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 06abec28-b7b5-38b6-af28-c44d98bce34f | -8.23344 | -45.50249 | 2025-09-30 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89336743-03fe-37a8-b7e7-1f20a3eb3e52 | -6.7436 | -34.98681 | 2025-09-30 03:47:00 | NOAA-20 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 11969460-e65c-36b6-91d3-8f0d1853d8c8 | -10.18938 | -44.89511 | 2025-09-30 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 53.5 |
| d29a9f0c-8e42-3288-8a23-6b2757013143 | -11.43983 | -44.96332 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 241652ac-2005-380c-9ddd-b6eaca7879d9 | -8.24532 | -45.51582 | 2025-09-30 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd76fa9e-deff-3f22-ae34-8c8b91f39221 | -10.42801 | -46.14894 | 2025-09-30 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e57e4d51-d4af-3887-81fd-4ddb05a3f9a9 | -10.5468 | -43.63795 | 2025-09-30 03:47:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fec35f04-330d-311f-8664-dec5b318d46f | -13.22923 | -43.37376 | 2025-09-30 03:49:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 43f7d8b8-76ee-3d85-82a8-d8f1b9cb35ed | -6.08669 | -42.44754 | 2025-09-30 03:49:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ff050c52-f9b8-3c42-8192-9ec972e48f8b | -12.84583 | -46.87714 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2faba62-2d77-36da-b01d-3f5dc122aa8e | -15.04688 | -46.98446 | 2025-09-30 03:49:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 04b46ba3-b9dc-397f-90af-a4770752d766 | -12.84704 | -46.96697 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6c64af3-97cc-33a4-8afb-4fb945fe8d87 | -13.0275 | -42.80555 | 2025-09-30 03:49:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 755e8171-d9fb-344d-bb97-14c50bede8a1 | -16.42332 | -47.0211 | 2025-09-30 03:49:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1821f5b8-3537-334a-a2d9-ee4c52f62469 | -15.32542 | -47.38356 | 2025-09-30 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70d8d928-a1a2-3a2c-babb-f9024c1abc04 | -6.10423 | -43.46885 | 2025-09-30 03:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dc6d0cd3-36ca-3048-b949-7718f7ea395b | -14.54155 | -48.26277 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e6d274d0-bd2e-375a-a63d-cff967693bcf | -13.36072 | -47.91466 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8c36e9e-82b7-352f-9d5e-91bc88348352 | -11.89196 | -48.05196 | 2025-09-30 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b57d02aa-bdfb-37f3-817c-28e98fd63c69 | -12.69228 | -45.28929 | 2025-09-30 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 323c3f05-f039-39d5-a0a6-9a17ce2c0a9e | -17.02746 | -44.99334 | 2025-09-30 03:49:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce1a9bc6-5b20-35be-81b0-10f1e59ac78a | -16.83111 | -39.33331 | 2025-09-30 03:49:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 98a257dd-a4f6-3775-be20-e4e56746a440 | -15.26705 | -49.49791 | 2025-09-30 03:49:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba6d9385-b38a-3754-b8f1-25ecb9b7329e | -12.83308 | -47.0011 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76a73c52-a70b-3522-a12d-a7ec8fcb26a5 | -12.83828 | -47.00176 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 316de476-2b59-37e9-ad32-8c9925dea8c8 | -6.05983 | -42.45112 | 2025-09-30 03:49:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e7d7b2f3-1fd1-33a0-97a0-b766c2fe0fe2 | -15.77153 | -43.67488 | 2025-09-30 03:49:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a56c6ed0-072d-33bf-a302-23803c70fbfd | -15.00272 | -42.42464 | 2025-09-30 03:49:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| acf90048-3450-3d66-aa61-56fcc3fcb73e | -14.38 | -47.14125 | 2025-09-30 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99402f06-5ff9-3914-bd84-34f6c9b7e299 | -14.71336 | -45.67399 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3363d46-e03f-366f-8f9e-ad6465c8c3c9 | -11.26081 | -47.23421 | 2025-09-30 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2ad75cf-c398-3c8a-af44-27f7a6c06aac | -13.78185 | -47.94874 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| de9b1242-9db7-3489-9d0a-0648cf0fde17 | -5.51094 | -43.88 | 2025-09-30 03:49:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 52e2b4c1-8abf-3a4d-835c-e848ac8f6269 | -14.69226 | -48.24776 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9349be4a-7b32-3942-88cc-2b4d59f9f123 | -14.52036 | -48.44989 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |


[Clique aqui para ver as próximas entradas](README28.md)
