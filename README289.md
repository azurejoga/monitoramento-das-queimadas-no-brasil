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

## Dados Diários - Página 289

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0542a45-9a2d-3f57-97b9-5e204e6becce | -3.7564 | -45.9422 | 2026-10-09 18:10:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 132.3 |
| 668bc048-3664-3e1c-97d7-917c732741fc | -3.4462 | -57.9812 | 2026-10-09 18:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 01ac8d35-af00-3012-9b26-69cef184696b | -12.2504 | -44.7631 | 2026-10-09 18:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 67a10fd3-8bc9-3142-91c9-908fb48b5c9c | -12.3712 | -46.5562 | 2026-10-09 18:10:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 155.7 |
| ed8b6fb6-aa78-34c5-8bef-d16a7992357e | -18.3125 | -42.3901 | 2026-10-09 18:10:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 141.2 |
| 4969e93f-f1a8-33aa-b92f-33dad3fa1870 | -11.037 | -44.0589 | 2026-10-09 18:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 645.3 |
| 824dd43d-ee03-37cb-8ed7-2b34370b900f | -12.2119 | -44.769 | 2026-10-09 18:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 3cefbe5c-6f4a-3433-af0f-1ef8066d759f | -15.2535 | -42.3741 | 2026-10-09 18:10:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 138.3 |
| 42f2a70b-61e4-3711-b709-5ef5c714975b | -5.3645 | -42.851 | 2026-10-09 18:10:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 116.1 |
| 6fa62eb0-c964-3a76-a54c-83304a2bab3a | -10.8598 | -45.5394 | 2026-10-09 18:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 27948271-c339-38bb-a1cf-577d152be24c | -12.0448 | -43.434 | 2026-10-09 18:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 182.9 |
| 55a00d09-12a9-3ae7-9842-f4deeb338f93 | -3.3129 | -54.0001 | 2026-10-09 18:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 8df03638-3690-3bc6-9ed3-26e22200af66 | -2.572 | -56.1646 | 2026-10-09 18:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| a411c1ef-9b7d-3421-bfcd-5abe67bfb893 | -10.4334 | -47.3046 | 2026-10-09 18:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 190.5 |
| fdc8df8e-9062-3969-8b25-ec3acfc9a49b | -12.1759 | -44.6351 | 2026-10-09 18:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 04b8ef0c-4192-3c43-8157-ea90e87f857d | -9.9398 | -43.5542 | 2026-10-09 18:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 138.4 |
| b0d89286-cea3-3da7-8469-2c736325d425 | -9.0533 | -47.3239 | 2026-10-09 18:10:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 16c17c38-a847-3d0c-a141-951fb7fa4858 | -9.0173 | -44.3676 | 2026-10-09 18:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 246007c4-be43-31e7-a48e-8b84d491a140 | -5.6934 | -53.4667 | 2026-10-09 18:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| c0bdfd35-05b0-378b-a71a-25aeede90878 | -3.6252 | -59.3259 | 2026-10-09 18:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| c8918947-e8c3-3d88-a6d0-82920a53ed3a | -12.0453 | -43.4102 | 2026-10-09 18:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 157.0 |
| cf6c520e-8a8b-3f8d-9e9e-6054056ba522 | -14.0667 | -43.8185 | 2026-10-09 18:10:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 331.2 |
| bf842ca4-bb79-3aa6-a554-88afc8125eb7 | -2.8347 | -54.1125 | 2026-10-09 18:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 7ea87e04-a272-3b88-b8d6-2a1a927aac11 | -11.47 | -43.3824 | 2026-10-09 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 48614356-2192-3245-a11e-271ba02d2bb5 | -15.3832 | -41.9029 | 2026-10-09 18:10:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 768.5 |
| d28cc9dd-9304-3b54-9ab0-50fdf29fa3b4 | -3.4463 | -57.9618 | 2026-10-09 18:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 1f1fa23d-d20f-3fb4-8428-67c16930b891 | -1.8757 | -56.3133 | 2026-10-09 18:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 60e06a95-36fd-381f-afdb-f1899928361c | -11.6978 | -46.7638 | 2026-10-09 18:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| dbf9e59e-9103-3a4a-aff6-ca64d3b0db2c | -14.0652 | -44.7863 | 2026-10-09 18:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 2aa7d008-0cf6-333a-9bde-b361275845e5 | -18.3327 | -42.3849 | 2026-10-09 18:10:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 213.3 |
| 2339d6c1-4cad-34cc-aecc-f2cfab820451 | -5.9649 | -40.914 | 2026-10-09 18:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 90.7 |
| d0c3d1b4-585d-38c8-9743-dd1c22265ffd | -12.3708 | -46.5789 | 2026-10-09 18:10:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 340.6 |
| 91e0c3fb-790c-381d-8cbe-3dba0c384d55 | -11.0554 | -44.103 | 2026-10-09 18:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| f5f21821-8e56-3f3a-b6eb-e4e4aeec25aa | -15.1593 | -48.2361 | 2026-10-09 18:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 583cfe55-a57c-33bc-a94a-2bcc80f19ce1 | -12.2123 | -44.7457 | 2026-10-09 18:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 221.2 |
| 5f9ffc6c-6ec0-3a5d-b354-256a3bd56dac | -12.1948 | -44.6554 | 2026-10-09 18:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| f2cd0d91-8578-3df1-a819-5635971ad3ef | -13.7657 | -48.1224 | 2026-10-09 18:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 900426d6-254d-35d6-9606-9ca4360771e9 | -2.5903 | -56.1839 | 2026-10-09 18:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 4bae3902-eb3c-3c50-aa2c-2ffd2d8a806d | -3.5157 | -59.2132 | 2026-10-09 18:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 02fb8235-aede-35f0-ac05-bafa6a135c13 | -14.4535 | -43.9359 | 2026-10-09 18:10:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 527.1 |
| 78de1c33-7933-345d-a07d-c9b0aa3c3f0b | -15.83 | -41.75 | 2026-10-09 18:15:00 | MSG-03 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d46b8018-17fc-3064-bdce-8d9c636d9980 | -5.73 | -45.14 | 2026-10-09 18:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a5515305-44ca-34cd-a759-7f5fa7bede05 | -4.42 | -49.8 | 2026-10-09 18:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da568767-6cec-3140-ac81-91fd64eb5df5 | -7.31 | -40.38 | 2026-10-09 18:15:00 | MSG-03 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 86bd83dd-8c23-3ec9-b0e8-0a4bf586309c | -15.39 | -42.01 | 2026-10-09 18:15:00 | MSG-03 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 464a3453-8dc9-3bbf-8e3c-870037f3e7ec | -15.41 | -41.93 | 2026-10-09 18:15:00 | MSG-03 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8264e2e3-3631-32e1-85d2-4fc93761ff8a | -11.35 | -54.06 | 2026-10-09 18:15:00 | MSG-03 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ade6851c-16cc-3688-be64-89659056fb7c | -14.39 | -54.97 | 2026-10-09 18:15:00 | MSG-03 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9417f815-ff97-338a-86ee-59aa0f53b51e | -9.92 | -44.88 | 2026-10-09 18:15:00 | MSG-03 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 527b3320-0a32-3e42-8428-f265645421e7 | -15.08 | -41.79 | 2026-10-09 18:15:00 | MSG-03 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a7715089-93a0-3952-9f4c-8207f725881e | -14.39 | -55.04 | 2026-10-09 18:15:00 | MSG-03 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1988fb98-d5d1-3ad6-8ab5-35a590052fa0 | -11.35 | -53.99 | 2026-10-09 18:15:00 | MSG-03 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 554d36bf-5ff2-3ad7-a718-977e350bd231 | -15.38 | -41.97 | 2026-10-09 18:15:00 | MSG-03 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cafbfeb9-1ebb-3662-9c71-4f84e1e2ea74 | -11.08 | -44.13 | 2026-10-09 18:15:00 | MSG-03 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7402480c-082c-39bf-be18-42ce1c6cfe94 | -5.76 | -45.09 | 2026-10-09 18:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fa40861a-4c2f-3cb7-9a4d-547e3be57e64 | -7.31 | -40.34 | 2026-10-09 18:15:00 | MSG-03 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| fdd497cf-e919-319e-95ea-78fcddd145e5 | -11.02 | -44.11 | 2026-10-09 18:15:00 | MSG-03 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6299739a-2d2a-3508-b25c-588da0943f86 | -14.45 | -40.74 | 2026-10-09 18:15:00 | MSG-03 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7851be2e-ad6d-38de-9189-a5739f3ddb82 | -5.76 | -45.14 | 2026-10-09 18:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dfaf0072-aa95-32a3-b42f-bc6d25cddbb8 | -15.28 | -42.43 | 2026-10-09 18:15:00 | MSG-03 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 775e38f7-bb6c-321c-a434-3a20e78a5be4 | -15.08 | -41.83 | 2026-10-09 18:15:00 | MSG-03 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 39edeaa9-2777-323d-a9a8-9decf120c367 | -15.41 | -41.98 | 2026-10-09 18:15:00 | MSG-03 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7b2c724f-553e-31b2-ad5b-28642de3fbab | -11.86 | -43.59 | 2026-10-09 18:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fa81633b-d63c-39c8-9c3f-3264b0b0b6a1 | -7.92 | -54.74 | 2026-10-09 18:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39a13fd3-37e2-3442-9040-b506a910683c | -4.42 | -49.74 | 2026-10-09 18:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 118b1a17-768c-3b33-a802-545f3a4c3921 | -15.25 | -42.42 | 2026-10-09 18:15:00 | MSG-03 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c8d4d08a-a1d8-34ef-8fda-ecd208c04edf | -3.0191 | -53.9071 | 2026-10-09 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 2b2e15fb-94a6-33e0-b15b-2d477b8ad2e2 | -10.2486 | -49.6851 | 2026-10-09 18:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 108fc40d-7d19-3098-8339-34d09f2e68dd | -12.2119 | -44.769 | 2026-10-09 18:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 446c4126-6c1e-37cd-a5b3-6f223bebc9bb | -12.3712 | -46.5562 | 2026-10-09 18:20:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 111.6 |
| e67a4c59-3cbb-3c15-9ca9-8a10881a6624 | -7.1825 | -52.6283 | 2026-10-09 18:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 233.1 |
| d0f85d73-778a-3571-9f54-d35a7f18ceb3 | -11.868 | -48.0126 | 2026-10-09 18:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 02409bc7-cdcd-387c-8a38-4f9a3e4c21e7 | -11.8975 | -47.3866 | 2026-10-09 18:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 9b225406-55e5-366d-b377-92b476766877 | -15.0713 | -41.7982 | 2026-10-09 18:20:00 | GOES-19 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 177.9 |
| 0f29ca07-ab39-323f-b127-c0128c3ba0de | -3.1973 | -50.5382 | 2026-10-09 18:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 1647c23f-4725-3c44-9845-230c85890482 | -12.0448 | -43.434 | 2026-10-09 18:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 170.7 |
| c1e1f508-dcf8-3c91-a29f-8a1c2a8b9ba2 | -11.9677 | -43.4464 | 2026-10-09 18:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 570e46b1-a40f-3a7e-94ad-2a4a429516f2 | -3.1697 | -58.6437 | 2026-10-09 18:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 42599fb2-2025-36a6-b45a-142ce7ada5fc | -2.7727 | -56.5142 | 2026-10-09 18:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 9eac794e-251c-3ea0-84bd-51f945278d14 | -13.1447 | -54.3405 | 2026-10-09 18:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 128.1 |
| 433429b9-cbb7-34c2-a794-c6ff537ff29e | -2.5506 | -57.4166 | 2026-10-09 18:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 90d82c92-cc5d-3d1f-a000-27f3b0d976a1 | -2.8712 | -54.192 | 2026-10-09 18:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 6c0ab070-b030-3598-a5af-faf231c626e7 | -2.4031 | -57.9041 | 2026-10-09 18:20:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 79534983-c6b1-3125-ae2c-00a5ea922784 | -6.4611 | -45.7986 | 2026-10-09 18:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| fd5fb823-cf47-3610-9fdb-04fc98b3ab9b | -4.7219 | -55.6727 | 2026-10-09 18:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| c6e75a95-8517-39e1-8be5-8f16be948fcb | -8.3011 | -45.7245 | 2026-10-09 18:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 7b5cec3a-4d89-357d-9e4c-47fb38e15ebf | -3.2357 | -50.1805 | 2026-10-09 18:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 3e33cdf3-0bc9-3b72-9c18-1f91426eefd7 | -8.2061 | -45.8017 | 2026-10-09 18:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 175.9 |
| 833c51e0-8528-339e-959d-6577566d4d82 | -6.4956 | -38.9535 | 2026-10-09 18:20:00 | GOES-19 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 175.0 |
| 43a4f38b-95f2-3eed-8c50-2662962388a9 | -9.9198 | -44.8585 | 2026-10-09 18:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 181.1 |
| 07908e6f-8e59-386a-8001-c46cb6ef08d0 | -3.0375 | -53.8865 | 2026-10-09 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 154.6 |
| caac0ed7-a92b-3387-9ee9-66d32bfbc192 | -15.3832 | -41.9029 | 2026-10-09 18:20:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 909.6 |
| fe99849f-842a-39c6-ae16-917b0f8f912d | -3.188 | -58.6241 | 2026-10-09 18:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 720753dc-25ad-3b7d-8184-f93dae08004f | -1.7296 | -56.0597 | 2026-10-09 18:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| ec504fa7-b9ff-3be4-83a4-3e837a61f609 | -8.0764 | -45.6339 | 2026-10-09 18:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 8e25a7f7-f282-3fec-a057-a5794e04c6df | -7.628 | -45.3826 | 2026-10-09 18:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 32fa3ad4-9fae-37d2-99a5-c43fb9146927 | -3.4462 | -57.9812 | 2026-10-09 18:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| a310a6aa-e8c0-3987-9c6c-df9be5434a8c | -13.6703 | -49.1098 | 2026-10-09 18:20:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 111.8 |
| eb23ba4c-0e80-3ed3-b0e0-fa43fb12d821 | -14.4541 | -43.912 | 2026-10-09 18:20:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 45ae90be-6898-3d0e-b892-4da63836a1af | -2.7335 | -57.4717 | 2026-10-09 18:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |


[Clique aqui para ver as próximas entradas](README290.md)
