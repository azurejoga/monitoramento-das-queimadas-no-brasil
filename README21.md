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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab5689be-b094-3807-89af-7b7b1eabffa9 | -4.56418 | -45.14623 | 2024-10-22 04:19:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02cb9921-4b8f-323d-ba3a-4337b61ffb02 | -4.56405 | -45.81092 | 2024-10-22 04:19:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 63812ff6-7e63-3812-9d5a-074de96e5680 | -4.56347 | -45.81457 | 2024-10-22 04:19:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88dc02e3-5482-3f8c-85d0-8ebab15d954a | -4.56125 | -45.80675 | 2024-10-22 04:19:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fcae17f2-8b36-306b-bbc6-086c38b7e5e0 | -4.56068 | -45.81036 | 2024-10-22 04:19:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d13e5acd-0b8c-33a0-a4d0-ec83fb53a10e | -4.55845 | -45.80258 | 2024-10-22 04:19:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c9686d19-ddc9-3663-a741-683d86fedfdd | -4.55788 | -45.80619 | 2024-10-22 04:19:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| f10f9925-3641-3f22-9cbc-4892887b88d0 | -4.55731 | -45.8098 | 2024-10-22 04:19:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 9b022327-7d5d-37bf-9534-25a40a36ab9a | -4.55508 | -45.80202 | 2024-10-22 04:19:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1ab37349-34e3-34c4-9ecd-fa665ccf6942 | -4.55451 | -45.80563 | 2024-10-22 04:19:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| fce15cbb-e122-3c51-a9b4-e32046c23f35 | -4.50821 | -45.73955 | 2024-10-22 04:19:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43f2ee82-cb50-3088-a199-eab9574a5380 | -4.46227 | -45.89888 | 2024-10-22 04:19:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a1b6f60-282c-3c10-bb39-e4199101cb55 | -4.43956 | -45.58558 | 2024-10-22 04:19:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ab230fbe-7dd6-3f8b-bfe0-15079650d8c3 | -4.4243 | -45.63787 | 2024-10-22 04:19:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a4b130f6-1eba-38b9-9212-fbc6aae71c96 | -4.42243 | -45.82224 | 2024-10-22 04:19:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 622c82f8-d7e8-3e32-b833-28b914b80d61 | -4.42036 | -45.64094 | 2024-10-22 04:19:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d5bdaa5-a552-383c-b2b4-d52b15076f8f | -4.41027 | -44.5718 | 2024-10-22 04:19:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1cb8448-a789-3a94-b21f-f8753b4f912a | -4.39538 | -46.16634 | 2024-10-22 04:19:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ebb6b52-f301-3c4a-94ba-bc5c33832e59 | -4.37538 | -45.58625 | 2024-10-22 04:19:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 551695b4-6693-38e1-9cf6-eb8c6f6798d1 | -4.28162 | -46.28594 | 2024-10-22 04:19:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d907234c-7ba8-30cc-bfc8-5f40bab91973 | -4.27878 | -46.2816 | 2024-10-22 04:19:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3c3700c4-396c-35f8-8e8c-c04f3b3048d8 | -4.26585 | -45.59183 | 2024-10-22 04:19:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ca8bda5-b964-3199-a6b9-79ebf5eeb5cc | -4.26249 | -45.59129 | 2024-10-22 04:19:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63199a27-0dfe-3d51-962b-cb7860b8bdfe | -4.25969 | -45.58719 | 2024-10-22 04:19:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1b0ec243-9390-362e-a30a-b5e4b5e80464 | -4.25912 | -45.59076 | 2024-10-22 04:19:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e562b3a9-8968-39d2-914c-8bf916539c76 | -4.21431 | -46.18061 | 2024-10-22 04:19:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 0e03f5b5-cb2b-3718-81e0-71fee3b3aae4 | -4.21088 | -46.18007 | 2024-10-22 04:19:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 48f02b19-68e1-32c2-a8f8-105d60b23394 | -4.19938 | -46.80293 | 2024-10-22 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 722bb9fa-571e-3839-b1c1-fb4acd29b0b0 | -4.18515 | -46.38774 | 2024-10-22 04:19:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2bf21bac-42c9-3ba5-a88f-b1e4aff4acb0 | -4.18171 | -46.38714 | 2024-10-22 04:19:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7435fda7-9c8d-3ede-8ab0-84c2bb18233c | -4.18013 | -44.34799 | 2024-10-22 04:19:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c86646f4-9b47-370f-8ec9-73b54e8d3de5 | -4.17683 | -44.34748 | 2024-10-22 04:19:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8b1a2ac3-c9dc-3fbe-b4e4-d14e9ed6f1b3 | -4.12819 | -46.8643 | 2024-10-22 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abb094ff-e83f-303a-bbea-9e78e29b8a04 | -4.12529 | -46.85992 | 2024-10-22 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31fe4410-9101-3ff1-99e0-69a75daf7702 | -4.12465 | -46.86385 | 2024-10-22 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65e87ae3-952d-3a30-92fd-933cbec5c731 | -4.10699 | -44.59763 | 2024-10-22 04:19:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3efc09aa-341c-36c4-bad3-5ebfa2a7c53f | -4.10482 | -46.14065 | 2024-10-22 04:19:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ad07ebf-287b-3b43-9f2d-f716a625b879 | -4.10334 | -44.23388 | 2024-10-22 04:19:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6aafb935-118c-331e-bcfe-e895c07ee786 | -4.1014 | -46.14011 | 2024-10-22 04:19:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bedcd12b-cf0d-3cbf-88f3-87057eac6ec2 | -4.10081 | -46.14385 | 2024-10-22 04:19:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c71c377-cf20-303e-a3bd-e1fb6cc4f108 | -4.09738 | -46.14335 | 2024-10-22 04:19:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8e5f5c6-ca07-3d6d-a188-ea7273206b15 | -4.07461 | -46.33183 | 2024-10-22 04:19:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1cc3589a-9db0-3921-943c-a3c501dfd559 | -4.07116 | -46.3313 | 2024-10-22 04:19:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1aae3760-dc19-3b00-a69d-613122484a1f | -4.01683 | -46.03228 | 2024-10-22 04:19:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53086a87-93cc-38c6-b35f-ac487e9dac92 | -4.01625 | -46.03596 | 2024-10-22 04:19:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc94b604-3644-3669-9b53-e64905a84ead | -4.01401 | -46.02801 | 2024-10-22 04:19:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0aa23c5b-7358-33a0-b1af-93e4a8537b1e | -4.01343 | -46.03167 | 2024-10-22 04:19:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df453b8f-9d11-39fa-a9e7-06be2632b4bb | -4.01284 | -46.03539 | 2024-10-22 04:19:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e12a670-9b4c-3710-a9cb-25a0c7de775b | -4.0106 | -46.02743 | 2024-10-22 04:19:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a54a81e-3dfa-397c-b6e8-11a95f453456 | -4.01002 | -46.03111 | 2024-10-22 04:19:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0699b59-b609-3b28-aaf1-58e7c4ecd957 | -4.00777 | -46.02321 | 2024-10-22 04:19:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| fd1332af-6757-35bd-86d5-5bb459319f5b | -4.00719 | -46.02687 | 2024-10-22 04:19:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8738f385-db56-3fd4-9106-e24d45766f69 | -4.00661 | -46.03056 | 2024-10-22 04:19:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c82e4d49-235d-3f77-8f15-b8a34e305710 | -4.00495 | -46.01893 | 2024-10-22 04:19:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| cef4dab9-e7d7-39f0-87d9-3e7aae0004a0 | -4.00452 | -47.00182 | 2024-10-22 04:19:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 993abea3-88b1-3a71-9a38-40591db7baec | -4.00437 | -46.02259 | 2024-10-22 04:19:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| aa1dc71c-d031-3d30-a60e-eea8bc6484a4 | -4.00378 | -46.0263 | 2024-10-22 04:19:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 426d2ecd-8005-3f20-a240-906be0b3accc | -4.0032 | -46.03001 | 2024-10-22 04:19:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b99d060a-198b-3691-95d0-0249848eab26 | -4.00096 | -46.02206 | 2024-10-22 04:19:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59439cce-32f5-3a80-a727-7763cd44312f | -4.00037 | -46.02577 | 2024-10-22 04:19:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d46cb7f-8cf0-3e3e-a88c-6a4cff07c822 | -3.97096 | -44.74979 | 2024-10-22 04:19:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 311694fa-2667-31ec-ab17-68be49d6aa14 | -3.93105 | -48.35912 | 2024-10-22 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 983af175-25bc-3e1e-a143-66853cfbd81e | -3.91238 | -46.44622 | 2024-10-22 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9de79a22-a160-387a-a39d-9117e033117d | -3.91195 | -48.33168 | 2024-10-22 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27f14faa-c168-3006-a60f-203f924a28f5 | -3.91177 | -46.45004 | 2024-10-22 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b82aa0b-a160-3a22-adfe-2e8b20d5b413 | -3.9112 | -48.33629 | 2024-10-22 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40d1564c-1ac5-35d2-8ebb-4e90766f8840 | -3.9043 | -48.33049 | 2024-10-22 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5a44bec-52ca-3873-a0d9-5d5af143e4c8 | -3.90354 | -48.33511 | 2024-10-22 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 911cf8e5-4dbc-3fc8-b8da-e432ab306999 | -3.90048 | -48.32987 | 2024-10-22 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8d41d92-6e97-3657-acd8-aa41d61a4f42 | -3.88688 | -46.44995 | 2024-10-22 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a600097-74c6-3911-8935-8cf792d8eb95 | -3.85438 | -46.45288 | 2024-10-22 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6ce786c-c68a-3729-9b76-884eafdb698d | -3.84943 | -46.48346 | 2024-10-22 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6acae24-2206-3e5f-93c5-429ab239cb66 | -3.84754 | -46.48352 | 2024-10-22 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ee2f564-cee8-337a-a698-93f54d29400f | -3.84533 | -46.48674 | 2024-10-22 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29164720-69cc-36dc-b1ef-9bc93cef86df | -3.84407 | -46.48296 | 2024-10-22 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 652cb723-355a-381f-aad9-9786384c5e46 | -3.83808 | -47.54158 | 2024-10-22 04:19:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87b18b4a-a9e4-355e-a278-f1a3dc0f216c | -3.83739 | -47.54588 | 2024-10-22 04:19:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4bef1849-38d8-34a5-bfcf-4a991550ec4d | -3.82844 | -46.92603 | 2024-10-22 04:19:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c89662c5-0363-3338-a9e8-84ce396bb5d3 | -3.82778 | -46.9301 | 2024-10-22 04:19:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfd46c8c-7ff8-3f72-9761-1e07b3328c11 | -3.81845 | -46.92031 | 2024-10-22 04:19:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 548c5b14-eb76-31e7-a69b-8b98862f24ad | -3.80414 | -47.7994 | 2024-10-22 04:19:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 33298be0-1e6c-3175-a61c-1fa36030ebf0 | -3.80342 | -47.80385 | 2024-10-22 04:19:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 9a35637c-122a-3057-968e-0ef2663ad654 | -3.79618 | -46.51508 | 2024-10-22 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c9d5f9e-c51c-3e87-8b11-80aafb851132 | -3.7927 | -46.51452 | 2024-10-22 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b0abda9e-e043-3fc0-a115-6e7ba3a84736 | -3.76714 | -44.51279 | 2024-10-22 04:19:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad027be5-0ebb-3cac-812e-35da305d1485 | -3.76675 | -45.44051 | 2024-10-22 04:19:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2aa350d7-8681-39a3-a932-3a6bd5627a85 | -3.76084 | -44.40242 | 2024-10-22 04:19:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b731bd5-893c-3dca-a7a3-f8b0f21a2cfd | -3.74895 | -45.758 | 2024-10-22 04:19:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6842f232-50bd-3a1f-9828-9f429c9ad759 | -3.74556 | -45.75747 | 2024-10-22 04:19:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 335e06f1-fce3-3073-8736-d0bccc654681 | -3.66211 | -44.79011 | 2024-10-22 04:19:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ff4d68e-c5ee-3a74-84b4-8f8c64a9b752 | -3.63467 | -45.24164 | 2024-10-22 04:19:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0eb4fccf-ee21-3bd6-ac3b-1fdf84a976ee | -3.61238 | -45.72995 | 2024-10-22 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 121af4fb-505d-3bde-a2de-ee4b4923aade | -3.55984 | -47.36163 | 2024-10-22 04:19:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e2f1f80c-a124-362c-a94f-9d9abd0f27dd | -3.54972 | -46.40699 | 2024-10-22 04:19:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6433595-c09f-378b-bba2-bef4d9a46328 | -3.54911 | -46.41082 | 2024-10-22 04:19:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6bfa1c7f-2a0f-3845-850e-8418a66458cb | -3.52412 | -44.84683 | 2024-10-22 04:19:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 143a8a14-5e35-346a-afef-406e3f3a0a1a | -3.46156 | -47.66822 | 2024-10-22 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3717d5d-ba2b-304f-89a6-1d6913ee341d | -2.75888 | -49.33701 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9337963c-33b9-3d0b-9703-f45e8808447d | -3.45673 | -49.15121 | 2024-10-22 04:19:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a31aefe8-93ab-3365-bec7-e4402fc1d0b2 | -3.45268 | -49.15056 | 2024-10-22 04:19:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README22.md)
