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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14d71cbf-e403-3eed-81cc-a9028550dde0 | -10.74863 | -45.06866 | 2025-11-14 04:46:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b3d6ee5-aed8-37f8-af2d-dacd6f54a47e | -12.66244 | -46.75678 | 2025-11-14 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 492ea2d2-445a-3211-9942-d5a60bcfadfa | -11.94074 | -44.59796 | 2025-11-14 04:46:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5319c06-ea75-347d-8d15-f163f77c3cfe | -11.17024 | -43.57714 | 2025-11-14 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38de51cb-13ba-34a8-9c07-e77eb097fce3 | -12.66849 | -46.74866 | 2025-11-14 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f41870fb-9b85-39c9-8351-53ef24beb5ae | -7.85381 | -44.29737 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9ba55f01-e225-3629-9b23-ce0da1bdbcf1 | -9.4985 | -47.45501 | 2025-11-14 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b8195bc-16d4-316a-86f0-aab4500b00eb | -10.63658 | -51.76427 | 2025-11-14 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 865deecf-ebc3-3e29-a3b1-45c1d35c5ccb | -7.71716 | -47.19202 | 2025-11-14 04:46:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f45e16b9-dca2-351f-9939-a3fe8020de29 | -12.66354 | -46.74889 | 2025-11-14 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ec35cdfc-7125-338c-9f04-442767dbae98 | -11.25973 | -55.0769 | 2025-11-14 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91c74fef-c1cc-3772-87d1-950fb2406606 | -10.63327 | -51.76374 | 2025-11-14 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 607b2feb-cb9b-329c-ac2e-4c4a1536a51a | -12.62685 | -44.14103 | 2025-11-14 04:46:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35953df3-2d07-3f01-95f9-2d1b411917f2 | -13.68778 | -48.41987 | 2025-11-14 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50b8f7bb-bf92-3d8c-81e4-79e4be7ceb69 | -7.94999 | -54.84214 | 2025-11-14 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 087953fe-e995-3299-bb1d-3ad911a415eb | -10.33773 | -49.92105 | 2025-11-14 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc481c6e-ca61-3461-a480-952db628d8ee | -12.66902 | -46.74472 | 2025-11-14 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 49c52118-bec9-3968-b8ac-3c7a0419bdf1 | -7.38739 | -48.65614 | 2025-11-14 04:46:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef2961a3-44a4-3fbf-8f14-f996bd4739bc | -7.9276 | -44.34207 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7907ca52-2845-3b9d-9d02-24a368affa11 | -12.66663 | -46.7574 | 2025-11-14 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| fd943978-3c73-3a8d-8f03-f66a5f401c91 | -7.8813 | -44.87594 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e00012b-070e-3dba-a0f6-c8d7393cd0a4 | -9.34862 | -46.59143 | 2025-11-14 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 05b3a1cb-3b21-3c7c-98cc-2e77365511d0 | -8.90492 | -41.07391 | 2025-11-14 04:46:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7e359c48-2a1b-3d06-a796-9dd72dabc590 | -8.94623 | -49.81638 | 2025-11-14 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 53c48d86-a194-3554-8d7d-e10455aec69c | -7.93427 | -44.32846 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f6465fd-f2aa-32d0-af57-8472d37b71e3 | -9.00765 | -45.45254 | 2025-11-14 04:46:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09ac2e66-5385-361d-a8c0-a6e19c8f37a1 | -12.6643 | -46.74804 | 2025-11-14 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9bba9a5f-4dcf-31bf-b8ad-ddebf4bf5ff8 | -9.00686 | -44.17972 | 2025-11-14 04:46:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0460a500-18b3-39fa-a8a9-2527504f889d | -12.00542 | -46.76835 | 2025-11-14 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a84c6fb-abd6-3a78-9a6f-adc7f7e36bb2 | -14.98363 | -47.86946 | 2025-11-14 04:48:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ae10fa7-664f-3ba8-b015-94e9a02700ef | -16.96561 | -52.38652 | 2025-11-14 04:48:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87782c7e-99f8-375a-8e27-a0ff285be92f | -15.33415 | -47.35727 | 2025-11-14 04:48:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f774730-712a-35f0-a264-c09df0793ff3 | -15.02355 | -47.1987 | 2025-11-14 04:48:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3c876a8e-9ce7-3c8c-b6a4-02309de20710 | -18.76418 | -45.28799 | 2025-11-14 04:48:00 | NOAA-20 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bfccc683-c81d-3fd1-ae6e-81c5bff1303f | -16.5177 | -43.54663 | 2025-11-14 04:48:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f0382df-16dd-3e15-a6f0-5c7cf7c4c8a7 | -14.6999 | -46.62104 | 2025-11-14 04:48:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 13490f19-1726-309f-8d9f-1a6f4c00edb4 | -14.70039 | -46.61728 | 2025-11-14 04:48:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3318f175-f447-3d2a-a973-d050c4266073 | -14.70088 | -46.61359 | 2025-11-14 04:48:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b1e6fa89-7e22-34fe-9be3-661d74c34b1e | -17.63049 | -46.70876 | 2025-11-14 04:48:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc0de260-8d05-3245-9b6f-826b0a3fd1c6 | -16.47482 | -42.18001 | 2025-11-14 04:48:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7a38e871-ba00-3d92-a80d-77e0c51d89f3 | -14.69939 | -46.6249 | 2025-11-14 04:48:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f2e85283-c8ba-3d68-9c53-aea072abc4e1 | -14.94843 | -48.44404 | 2025-11-14 04:48:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3e6d943-84fa-39f2-8000-e5085e677d63 | -18.76452 | -45.2849 | 2025-11-14 04:48:00 | NOAA-20 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eae20248-dcc9-3bfb-84b1-2ed841dfcb65 | -15.07506 | -46.46008 | 2025-11-14 04:48:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b663db89-4278-393d-85b0-269e0f732ffb | -17.79428 | -44.98087 | 2025-11-14 04:48:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da2fd9c3-3264-3fb9-b345-183b0f210e4f | -16.37203 | -43.03696 | 2025-11-14 04:48:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c848f56b-56f6-30fb-a130-23bc308b5c7e | -15.30081 | -47.38426 | 2025-11-14 04:48:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10e285a5-01ed-3b68-9c87-bab0a561289c | -16.54747 | -49.35145 | 2025-11-14 04:48:00 | NOAA-20 | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1203e9b-18b9-3054-b2ac-ce62c619e18c | -16.03214 | -44.97147 | 2025-11-14 04:48:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f24caa2e-97a9-3c3c-b14e-516dbca2a64c | -14.91578 | -47.36142 | 2025-11-14 04:48:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41b3d84c-1c60-3d44-9e03-ec31711a7351 | -15.24745 | -47.94628 | 2025-11-14 04:48:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3e21fb0-71f9-346b-9926-2900f3022697 | -19.47633 | -46.92265 | 2025-11-14 04:48:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e16401e-d343-3360-b304-dd2188b86a27 | -17.79897 | -44.98481 | 2025-11-14 04:48:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4d47c8a-fb41-3dfd-a9e5-8d66dd14f62f | -16.3074 | -45.09825 | 2025-11-14 04:48:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9597a8dc-6e8d-3f19-9468-901e4e0fc6d1 | -16.3716 | -43.04092 | 2025-11-14 04:48:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c82641a2-a8e8-373d-ae90-a76fdc485e53 | -16.98749 | -51.6077 | 2025-11-14 04:48:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ab87fd7c-af85-3109-9fee-bd0fa046b32c | -17.79933 | -44.98172 | 2025-11-14 04:48:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be6619be-db81-381f-9bbf-04d3354cfbfd | -16.23903 | -45.64176 | 2025-11-14 04:48:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| abc888e8-9f98-3dae-9864-faad8af73e97 | -16.58854 | -42.22078 | 2025-11-14 04:48:00 | NOAA-20 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ebbfede0-6bf8-3616-9701-df0cf33d2c11 | -16.58901 | -42.2163 | 2025-11-14 04:48:00 | NOAA-20 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 22e911f9-940e-3007-9fc8-4c85c42b90a1 | -16.96617 | -52.38285 | 2025-11-14 04:48:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ebe9ef82-a2ba-3514-91ab-13a05193ae3f | -16.47523 | -42.17609 | 2025-11-14 04:48:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ae72fc64-4850-3eb2-8549-35083d9701a9 | -17.79391 | -44.98404 | 2025-11-14 04:48:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f14cc07-d4f7-36f7-9b0d-3fd3cddbf84b | -16.35546 | -46.00796 | 2025-11-14 04:48:00 | NOAA-20 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea9b71d8-be19-3eef-aea0-3af9395f33cb | -14.88527 | -56.73437 | 2025-11-14 04:48:00 | NOAA-20 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d37af0bd-a3b0-3065-8a59-05c29968e847 | -15.07394 | -46.46228 | 2025-11-14 04:48:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d231d20-9b83-3387-a66f-c8cdf23518b5 | -17.29911 | -46.83001 | 2025-11-14 04:48:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d3a0daf-b07a-32c6-9d51-8499c3348464 | -15.61118 | -49.14836 | 2025-11-14 04:48:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dd16d628-2ac1-3a9c-830e-41e8419dc445 | -14.91522 | -47.36555 | 2025-11-14 04:48:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73de744d-4d7e-3074-bf1d-2c3bb763c379 | -14.77378 | -46.67574 | 2025-11-14 04:48:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b31d640-79f4-3a30-98f3-90186e85c20b | -16.54306 | -49.35568 | 2025-11-14 04:48:00 | NOAA-20 | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e8820e37-ee20-3271-9899-aa63814957e5 | 3.1094 | -60.765 | 2025-11-14 04:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 19d5c41e-713e-3763-8377-8cecb5f4e78b | -11.8677 | -49.2195 | 2025-11-14 04:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 2c41734f-ec2c-3780-99ab-db7a6edb0a24 | -11.8486 | -49.2218 | 2025-11-14 04:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 108.3 |
| db1b236c-4d5b-33f9-9bc0-a9387f58b25c | -11.8486 | -49.2218 | 2025-11-14 05:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| c6916f84-1ce2-3bc9-bf83-722488d34b7d | -11.849 | -49.2 | 2025-11-14 05:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| a2112c47-924c-33f5-9ee5-8558680080db | 3.1094 | -60.765 | 2025-11-14 05:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 75.0 |
| c4ffe4a3-cd89-3c7d-8eee-84fb15e6af13 | 3.0911 | -60.7653 | 2025-11-14 05:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 61b7bc2e-c6dc-3e67-a5c9-b564ac5861a4 | 3.1094 | -60.765 | 2025-11-14 05:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 61ecaada-ecb6-3595-9817-e5fbc9e22db8 | -11.8677 | -49.2195 | 2025-11-14 05:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 8159238e-5382-3ab7-a888-7f5706899fc0 | -11.8486 | -49.2218 | 2025-11-14 05:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 177e1957-d88e-3004-b390-39b73a32bed0 | 3.1094 | -60.765 | 2025-11-14 05:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 2ce8099b-0e01-3628-bbf1-f77b6029a885 | 3.0911 | -60.7653 | 2025-11-14 05:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 56.9 |
| e9906882-4afa-36c1-bb2d-719d314ebb83 | -11.8486 | -49.2218 | 2025-11-14 05:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 53d29f1b-73e5-362f-9db3-eae750173170 | -11.8677 | -49.2195 | 2025-11-14 05:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 18631e4a-fda6-330e-896f-ab86c6bc2c37 | 3.1094 | -60.765 | 2025-11-14 05:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 9c61a656-6462-36c2-a2cb-14b4e8ecaa32 | 3.0911 | -60.7653 | 2025-11-14 05:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 9b8055c9-d938-3b35-bac6-c4eb91e1f2c9 | -11.8486 | -49.2218 | 2025-11-14 05:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 7b7d5358-07cb-3d05-8d38-83fed712fdc9 | 3.13628 | -60.71665 | 2025-11-14 05:31:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 20.7 |
| a924626b-7fca-364e-aada-5e35fe6cc03e | 1.52863 | -55.65813 | 2025-11-14 05:31:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14441e72-96ee-31a4-9d69-b3f2b82ab3c6 | 3.10586 | -60.76038 | 2025-11-14 05:31:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7fb7a6bc-73e2-3a62-a588-f5a9cfb1948e | 3.15377 | -61.02136 | 2025-11-14 05:31:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e532f62d-755b-39f7-8e20-5a270198ae15 | 3.10641 | -60.76384 | 2025-11-14 05:31:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d9a6b42f-a23d-3080-b3d0-5a07f83f1cef | 3.16583 | -60.27872 | 2025-11-14 05:31:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9e94b24-e0f7-36b7-b3d1-d24f97e116f2 | 3.16694 | -60.28576 | 2025-11-14 05:31:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ecf31a0-acd4-3648-b96e-da272b128219 | 3.29009 | -60.11486 | 2025-11-14 05:31:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3cc734c-a709-3bd6-9fd6-340199b96025 | 3.16194 | -60.27571 | 2025-11-14 05:31:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e624b49-a9ee-32d8-bc1e-08427b1f6e00 | 4.25836 | -59.84349 | 2025-11-14 05:31:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0fb9e592-19e5-3aa3-a696-d4d443c190f8 | 2.75129 | -60.3693 | 2025-11-14 05:31:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 788d042c-0f8c-30d0-82d5-71b80fba455f | 3.15638 | -60.28379 | 2025-11-14 05:31:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |


[Clique aqui para ver as próximas entradas](README50.md)
