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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a015a5f-c2e3-3aa7-ad6f-bb4becc310d4 | -11.13558 | -44.76255 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 152fe7bc-3e64-3467-b13a-db8e3d930164 | -12.78727 | -48.71863 | 2025-08-23 04:02:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 34cd0a22-f08e-3c48-a346-32f7270b4d03 | -13.3751 | -46.21207 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 6f02caed-ab94-3265-b7c7-7207d95db5cd | -13.32807 | -40.34509 | 2025-08-23 04:02:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cac36850-3035-33e4-8b89-7f2e962a51de | -13.37113 | -54.40035 | 2025-08-23 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 783cf52f-86d2-3fef-a0bc-b50d28903d7c | -14.9654 | -48.67435 | 2025-08-23 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 411f4475-386d-3201-80bf-10865326134d | -15.90902 | -42.30568 | 2025-08-23 04:02:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e7ec6d1a-d3b0-3059-8a4c-98fc97b95415 | -13.17019 | -46.91508 | 2025-08-23 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30594b46-d978-3dd0-9c11-5ab2b5c18055 | -14.80707 | -45.45419 | 2025-08-23 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a64d790-25b3-3e21-a1d6-0260eb9460c4 | -9.44086 | -47.6556 | 2025-08-23 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47dfb539-316b-392c-bb16-24a2078afb5c | -8.53391 | -48.86049 | 2025-08-23 04:02:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06b3043b-b0f6-3bc4-b5b9-0d2588a5f813 | -14.93983 | -48.00635 | 2025-08-23 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 630d5705-d347-36c6-b381-3082bd0e05ad | -12.99848 | -45.23164 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c0507770-de7a-3619-b9a1-a774e9eec071 | -13.64811 | -46.88526 | 2025-08-23 04:02:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5147b282-a3d2-320f-a7a2-c7385f617455 | -13.50609 | -47.05136 | 2025-08-23 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aaa94899-a275-3885-a3b7-15d0cbf2c021 | -13.33813 | -40.34669 | 2025-08-23 04:02:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 41ec42da-c0e2-3f77-b8e4-144b55c39910 | -14.37358 | -52.06005 | 2025-08-23 04:02:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 898372bc-bcf3-3ecb-8b39-d38167c4b840 | -12.94907 | -46.29703 | 2025-08-23 04:02:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 14badb77-be83-33f4-aabd-d2362d6955a3 | -14.80784 | -45.44975 | 2025-08-23 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02c06e79-a7d1-3ef1-8667-c12dcf84f4e0 | -13.62497 | -46.87472 | 2025-08-23 04:02:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 72a6ddcc-6393-3bf5-9fca-bd7e14f98665 | -13.37656 | -47.48771 | 2025-08-23 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 26d89c6c-369e-31c5-94ea-1d3786e13805 | -12.93135 | -46.16838 | 2025-08-23 04:02:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e35990c4-af9a-322b-9e74-bdfd6e11e91e | -8.49872 | -44.73746 | 2025-08-23 04:02:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c788dccd-e63a-323b-9f22-8005b63f5b35 | -10.28661 | -46.75266 | 2025-08-23 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e68b3209-c116-3aa2-8225-dece4bfd354b | -15.19225 | -48.24066 | 2025-08-23 04:02:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6a04b41-41d0-370d-be75-2e77290f09a9 | -14.3688 | -52.05494 | 2025-08-23 04:02:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89e8bb4e-fee5-359e-b844-f106b9d9a0c5 | -13.38292 | -46.21326 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| caba5405-931e-3eb9-93e8-a3cecbb67062 | -11.13853 | -44.76764 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 29fd85d4-5d78-36bb-b54f-24f1022e1683 | -10.62627 | -52.34486 | 2025-08-23 04:02:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7fb2567-fb3b-347c-a7ad-31bd2d793727 | -14.96983 | -48.67519 | 2025-08-23 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7313e2e2-2c39-3cbb-8d56-26292b3b4103 | -14.78057 | -45.47634 | 2025-08-23 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ead2710-3efd-3b0c-992d-b3c48c943455 | -12.6744 | -47.81081 | 2025-08-23 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ef1a201-c869-3eb7-b5a8-170fbb0e0474 | -14.93052 | -48.00925 | 2025-08-23 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2574738a-acd7-3a65-b853-c1bd7f8fde6a | -10.27377 | -46.75129 | 2025-08-23 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba3f6058-7699-375a-a36f-457dd1b15141 | -13.13016 | -46.90361 | 2025-08-23 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8cff6c6c-1267-37d0-a2f4-414ffce5238b | -11.19252 | -55.04329 | 2025-08-23 04:02:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 30ed2658-e556-3c8d-99e0-87117e358c06 | -13.46935 | -47.04419 | 2025-08-23 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23175c17-593b-3f19-8094-f05639898d4b | -14.80496 | -45.44468 | 2025-08-23 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8193163-62bb-344b-9e35-c36387b20292 | -14.78344 | -45.48147 | 2025-08-23 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37d0c7fc-6344-372b-9467-55660ed6dbe4 | -11.3235 | -47.84306 | 2025-08-23 04:02:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8c1c511-9d85-3c95-8070-04f2a5515641 | -12.77352 | -48.70789 | 2025-08-23 04:02:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| de2e8bb7-0a7b-3d1b-94d3-676c79ae2cb6 | -9.70505 | -42.17652 | 2025-08-23 04:02:00 | NOAA-20 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1cd04a46-0d9f-32bd-97dc-a5f0cde54cb1 | -8.15828 | -47.30881 | 2025-08-23 04:02:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e4bb877-9d90-3e65-8f0d-ea982bf522f1 | -8.30621 | -47.27332 | 2025-08-23 04:02:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7cc1db9b-0ff7-3c76-ad66-5d1824121038 | -11.12374 | -44.76501 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 392771e1-9ded-3171-9e45-de4cf127ae9d | -10.7527 | -48.25487 | 2025-08-23 04:02:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| becf1461-e225-3c16-a148-33bb995cc7cc | -14.8194 | -47.95067 | 2025-08-23 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2b362e6a-4f72-3e68-b716-31b0ba48de24 | -10.216 | -47.56644 | 2025-08-23 04:02:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 595df8b1-84cb-3ee4-9882-ec2c8cadc2e6 | -14.82361 | -47.95161 | 2025-08-23 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 7e59d684-df46-3dae-a079-153069f33789 | -13.04512 | -46.79541 | 2025-08-23 04:02:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d744dd9-8fe4-3e61-a04d-7b693c093dfd | -14.77343 | -45.23506 | 2025-08-23 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6906a332-fbcc-3a04-88d1-b9642520c376 | -13.36653 | -47.49497 | 2025-08-23 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f10ce8b1-0838-309f-a927-f2668813ca88 | -8.52841 | -48.83661 | 2025-08-23 04:02:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ade09c20-280b-3585-9daf-98e491f35b64 | -14.47213 | -48.35715 | 2025-08-23 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| dd78b18b-0754-34b8-b2a9-2ebc7a0373b5 | -11.98304 | -40.86344 | 2025-08-23 04:02:00 | NOAA-20 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a017dfe9-abcb-3923-88c9-44d500bab6b5 | -11.96949 | -46.77437 | 2025-08-23 04:02:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f8fe5740-0ff1-396d-9dc3-cc4ff30c1be3 | -13.36497 | -54.4042 | 2025-08-23 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f0b9af9d-1e98-396d-aa53-a886e4a8ea9d | -11.61756 | -50.42644 | 2025-08-23 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b522d2ef-e9b2-32f5-9d1e-e3b5c603390f | -13.44972 | -50.67474 | 2025-08-23 04:02:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1b1ec0c-9177-33bd-925c-faa37566f984 | -14.81173 | -47.94473 | 2025-08-23 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6413b004-e60c-3105-96ec-b5edf2f027e4 | -13.64353 | -46.88758 | 2025-08-23 04:02:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8bf02f6-3046-37fb-a935-351e2c6dc9b0 | -11.13785 | -44.74922 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1daf4aeb-becd-376f-976a-f19160171712 | -12.77431 | -48.71107 | 2025-08-23 04:02:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 21d814ab-d7fd-35ea-8c51-721ab2c9fea2 | -13.45868 | -47.03299 | 2025-08-23 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a9d97ce3-a9ab-3421-ba92-c2486c4b11a6 | -13.41747 | -51.79507 | 2025-08-23 04:02:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7cfbd91-7c4b-393a-be6d-eb19c2443ce9 | -13.64869 | -46.88198 | 2025-08-23 04:02:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f56d291-f91a-33fd-844b-ba16c207cc42 | -13.41601 | -46.27677 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 46.0 |
| cbd45399-be66-3b89-9cad-35b48f0ab9ae | -15.18797 | -48.23979 | 2025-08-23 04:02:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ae5da1b-31f3-3a5d-a828-118f0b642bcd | -9.82944 | -46.38055 | 2025-08-23 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 25c6cf18-8fea-31f6-967a-5826d52edae3 | -12.79473 | -48.72219 | 2025-08-23 04:02:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3877e0db-e4f6-3ada-8962-2f7df6fae545 | -13.16475 | -46.92204 | 2025-08-23 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 47c09e5d-6874-3734-9d6f-70185549fbc8 | -11.18839 | -55.02784 | 2025-08-23 04:02:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 82d15273-6daf-3e01-a07c-0e3f6f91bb7f | -8.77437 | -45.43703 | 2025-08-23 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 549cb038-2525-3625-837b-2d5c8d3f791a | -10.20623 | -47.56947 | 2025-08-23 04:02:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 509efabb-8978-3023-bc8e-bded38e46ac8 | -15.55963 | -42.68822 | 2025-08-23 04:02:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| fa5a4a5d-9f62-3f86-91d3-e06dcc7d8381 | -11.14905 | -44.70568 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 500d71af-cf39-357f-bcc9-6d182248cac0 | -14.94338 | -48.01089 | 2025-08-23 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a98493a8-45b0-3573-af3e-42da99144b6c | -12.94629 | -46.31282 | 2025-08-23 04:02:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 90fac6c8-952d-3abb-8f38-2f4be41125d9 | -13.37345 | -47.50485 | 2025-08-23 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 00544dce-a337-30b7-9786-b948b6a7f5d7 | -15.06912 | -48.48611 | 2025-08-23 04:02:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d369dee1-a37c-381f-ad39-b3b4a3d6ef01 | -12.77894 | -48.71188 | 2025-08-23 04:02:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| ff03f710-59e5-3370-a52e-ab376f47d635 | -13.37991 | -46.20757 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5c57a3d3-f97e-343a-a7fb-6bb3f61a9ccc | -8.52892 | -48.83371 | 2025-08-23 04:02:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aef4adba-bc62-37b5-b82c-11b79e200d15 | -13.21786 | -43.37571 | 2025-08-23 04:02:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 15578b0a-2058-3480-b06d-9421fd208eea | -11.11862 | -44.75044 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db80c8f7-255f-39ee-9e9c-b915e44f1c01 | -10.63377 | -50.13809 | 2025-08-23 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ecdb5f2e-e470-35e0-878f-5893e5097737 | -13.46765 | -47.03004 | 2025-08-23 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a131afbf-17d5-3d92-8430-aed2c51ab44e | -14.77417 | -45.23078 | 2025-08-23 04:02:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91f4fb3d-a2e9-3ac3-b634-b3c58553530b | -15.96331 | -43.90271 | 2025-08-23 04:02:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 87aebc1a-9507-3c3f-aea4-15058a9dd6c1 | -13.48436 | -47.03107 | 2025-08-23 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1deee7f-5164-3aa6-9d66-e4fb0bce30e2 | -13.03742 | -46.3204 | 2025-08-23 04:02:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ec1f2d17-a7cc-3d2a-b360-26fd666850a2 | -15.19854 | -48.25457 | 2025-08-23 04:02:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7de6ee70-2d55-342c-8f39-8af069a3ec97 | -8.84749 | -49.86402 | 2025-08-23 04:02:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2ba9a009-7cf0-3ff5-b80c-cffa7666dd8e | -11.32301 | -44.96179 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd021553-44aa-33e2-85a1-76f6cf710758 | -12.78551 | -48.72032 | 2025-08-23 04:02:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7e6f49de-69a7-3f73-ad02-f89e05a7d7fa | -12.47084 | -46.93941 | 2025-08-23 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50e511d1-3676-3396-9ce1-86a675307ee2 | -13.12945 | -46.90753 | 2025-08-23 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 93ffa902-279b-33fd-b352-e318f340cb75 | -15.5298 | -41.6929 | 2025-08-23 04:02:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 673c186a-977c-301e-91d9-fd0ffc99564d | -12.99186 | -45.22582 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 1c8efca9-9b1d-3316-b38a-43aab9f051d2 | -13.39093 | -46.35109 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README29.md)
