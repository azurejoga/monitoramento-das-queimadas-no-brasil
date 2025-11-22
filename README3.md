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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1415be8-411f-35be-97e6-2f3b48169e9d | -19.91389 | -42.32395 | 2025-11-22 03:38:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bc7ff463-12f8-3aae-b260-7c4747f9ba97 | -21.37322 | -47.83493 | 2025-11-22 03:38:00 | NPP-375D | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0411cfed-ae38-3428-9cc2-a656452daffb | -19.20711 | -45.83452 | 2025-11-22 03:38:00 | NPP-375D | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| d9e7489e-7ede-3b37-a5f6-ab187ef343d8 | -18.76142 | -45.28705 | 2025-11-22 03:38:00 | NPP-375D | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a87444c0-741d-3152-8300-8748d080438b | -18.76309 | -45.27944 | 2025-11-22 03:38:00 | NPP-375D | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5cb2050a-7011-30b7-b6b8-30e3b0fa0759 | -20.62775 | -47.44416 | 2025-11-22 03:38:00 | NPP-375D | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 241e6c8e-2913-3c3a-93d2-4639ec1dc5f6 | -21.07137 | -43.33288 | 2025-11-22 03:38:00 | NPP-375D | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 62de7067-0a6b-3705-b964-0da02b69aa62 | -20.62408 | -47.43657 | 2025-11-22 03:38:00 | NPP-375D | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ef53e69b-275d-3cee-a3c4-b6c4a806afd6 | -19.62955 | -41.84794 | 2025-11-22 03:38:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| c5c1299c-97fd-3b89-a5ce-85c50734e32d | -20.63022 | -47.43775 | 2025-11-22 03:38:00 | NPP-375D | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 6e4cd9b4-fa3b-3550-bdc2-75fef020bdc8 | -20.62903 | -47.43878 | 2025-11-22 03:38:00 | NPP-375D | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 5bc266e8-0631-351b-8636-57397f86b430 | -19.50193 | -42.08577 | 2025-11-22 03:38:00 | NPP-375D | INHAPIM | MINAS GERAIS | Brasil | 3130903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| cdc23526-8c30-3482-9a17-375713ed129d | -19.91278 | -42.32642 | 2025-11-22 03:38:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dcaea850-ae56-395a-988e-7400886209cc | -18.76225 | -45.28325 | 2025-11-22 03:38:00 | NPP-375D | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1086adfc-3e32-31f0-9b97-ba42a2d37b26 | -20.82257 | -45.1075 | 2025-11-22 03:38:00 | NPP-375D | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b273372b-c998-3ee3-adc7-debe919a96fe | -18.75672 | -45.28192 | 2025-11-22 03:38:00 | NPP-375D | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 326034f6-bf48-395a-8ec3-728deb0157b5 | -21.36712 | -47.83328 | 2025-11-22 03:38:00 | NPP-375D | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7adfeca5-5b73-3178-8e09-2c4d66e09ce1 | -18.75944 | -45.2805 | 2025-11-22 03:38:00 | NPP-375D | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54341e9e-3f1b-31e7-96d6-4210578ab69b | -19.85474 | -46.30583 | 2025-11-22 03:38:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7e8d245-815c-30e2-84cc-b8f1c16e21a6 | -20.629 | -47.44307 | 2025-11-22 03:38:00 | NPP-375D | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 8e716c4c-06f4-3859-aae9-e34263c648ad | -19.85376 | -46.3102 | 2025-11-22 03:38:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7918d089-f4eb-3582-86b9-fe09f6be0f7f | -20.63141 | -47.43258 | 2025-11-22 03:38:00 | NPP-375D | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 00ac07ad-c297-341a-8769-046bf5b3dfc3 | -24.36614 | -49.18551 | 2025-11-22 03:38:00 | NPP-375D | BOM SUCESSO DE ITARARÉ | SÃO PAULO | Brasil | 3507159 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| fc80fda7-c815-3d90-a9bd-12dd34080a9e | -21.04527 | -48.55596 | 2025-11-22 03:38:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c4907ccc-f324-343b-945a-3fcecfa446a9 | -20.62282 | -47.44202 | 2025-11-22 03:38:00 | NPP-375D | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 69ffb1b9-b964-3834-9f9b-2242a9e76d29 | -20.65677 | -43.44547 | 2025-11-22 03:38:00 | NPP-375D | CATAS ALTAS DA NORUEGA | MINAS GERAIS | Brasil | 3115409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d44a94cf-8730-362d-8ccd-a484904561bd | -19.21276 | -45.83601 | 2025-11-22 03:38:00 | NPP-375D | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 755e12d7-a0b2-36e2-889a-de9bf8bb5566 | -18.75755 | -45.27814 | 2025-11-22 03:38:00 | NPP-375D | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d17ac980-7fba-3c61-82f2-f0b9bc8f4d23 | -20.63026 | -47.43359 | 2025-11-22 03:38:00 | NPP-375D | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 1727f5d2-ffd6-337f-9c6e-a4156f77b8be | -18.75863 | -45.28431 | 2025-11-22 03:38:00 | NPP-375D | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e75a66f-93f7-3405-84c2-6239183289fe | -18.96943 | -42.36592 | 2025-11-22 03:38:00 | NPP-375D | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 30ced513-7646-33ca-a8f3-5c05e057368b | -24.37253 | -49.18643 | 2025-11-22 03:38:00 | NPP-375D | BOM SUCESSO DE ITARARÉ | SÃO PAULO | Brasil | 3507159 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f039bfab-e88c-3e6e-b6e7-7b7b11838ab7 | -20.94203 | -42.82892 | 2025-11-22 03:38:00 | NPP-375D | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1001aab7-edf6-3244-a7c4-6846c4e39e0d | -20.8173 | -45.10624 | 2025-11-22 03:38:00 | NPP-375D | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a0e6f5ec-91c9-3527-9241-31806f93cc2a | -20.0062 | -40.20657 | 2025-11-22 03:38:00 | NPP-375D | FUNDÃO | ESPÍRITO SANTO | Brasil | 3202207 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 35f81779-1ace-3610-9f84-f5b5cdd727e8 | -3.85981 | -41.58152 | 2025-11-22 03:53:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ac07f86b-3387-3df4-867a-0f69e385c173 | -6.85834 | -40.15719 | 2025-11-22 03:53:00 | NOAA-20 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a37cfd4b-aa09-30a1-838e-376808c34506 | -2.92396 | -48.24402 | 2025-11-22 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a8427ad-7fcc-3fb9-a548-8693c6ce91b1 | -5.11016 | -40.73261 | 2025-11-22 03:53:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b0f14a8c-e895-3b53-9e26-e5b76d084671 | -2.92266 | -48.22612 | 2025-11-22 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 7cb1e2ee-9a2a-3177-9aa0-678d5d98b7bc | -4.0363 | -42.51924 | 2025-11-22 03:53:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| af525423-b652-3bc9-a6f3-58d41422d588 | -6.79614 | -39.11946 | 2025-11-22 03:53:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 48a4b854-ee38-3eb9-a5e4-84a1221a94b8 | -3.26671 | -42.20922 | 2025-11-22 03:53:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| deb9938a-e9e9-3084-8c19-2f6e684036d8 | -2.91985 | -48.2431 | 2025-11-22 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 6c575d61-c0d1-3179-ac0a-85186b816e4c | -2.92544 | -48.23546 | 2025-11-22 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 8f0ff729-f668-3f2a-b5b9-0f58510e20e4 | -2.6945 | -45.10644 | 2025-11-22 03:53:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 33.1 |
| a323b474-8efa-3a00-b8c7-4864c7604e79 | -4.02408 | -42.47098 | 2025-11-22 03:53:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a04e4324-7053-39c4-a779-974930b53352 | -4.14161 | -43.69458 | 2025-11-22 03:53:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd6af094-25e1-3d66-a412-b5e3f36efb92 | -4.15008 | -43.69603 | 2025-11-22 03:53:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 5af107e5-8772-3f6f-9fac-44c54ef3ca0b | -6.85545 | -39.3653 | 2025-11-22 03:53:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b5a71e2a-becd-3f2a-9ff4-3d3383f2ad51 | -2.46937 | -47.83171 | 2025-11-22 03:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a8ccc6b-0a93-3cb8-9a06-208a8cf0b297 | -3.17305 | -48.61534 | 2025-11-22 03:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7254a4c0-58e4-3f9b-abeb-e90e43f11fc5 | -6.24189 | -44.65525 | 2025-11-22 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 25f8efe8-c5e6-3925-b401-d29d326312a0 | -3.46255 | -40.81858 | 2025-11-22 03:53:00 | NOAA-20 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a75d5c25-8dbc-3faa-9dc3-8b30a7cfa0ba | -2.92029 | -48.2303 | 2025-11-22 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 6d664dd8-4c5c-31d5-acaf-596b3eb0d277 | -3.62229 | -41.99546 | 2025-11-22 03:53:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 180ee47c-1ae3-3152-8a0d-a956c7061f9b | -4.03547 | -42.5243 | 2025-11-22 03:53:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 235678bf-bcf5-30f2-a9be-7c1139b1682a | -4.16675 | -43.67439 | 2025-11-22 03:53:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f297487f-048c-3d76-974e-e0f0597eedff | -4.73684 | -42.8047 | 2025-11-22 03:53:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56d778c9-8e40-3e9b-bd62-b550d6bbfca2 | -2.92056 | -48.23885 | 2025-11-22 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| a7f83075-f528-35bc-8df0-3f3ee197d970 | -2.92503 | -48.24835 | 2025-11-22 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73ef4fc1-14cb-339a-81d8-f467cbe6ebb9 | -4.14651 | -43.69135 | 2025-11-22 03:53:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 766d76d4-2a1f-33b7-99ef-1783f8990ba2 | -2.92101 | -48.22615 | 2025-11-22 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 88eb0483-52d1-3d21-9ebc-7e12a4f06fc1 | -2.69407 | -45.10874 | 2025-11-22 03:53:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 23.6 |
| b6435daf-2444-3bc0-930b-395a46b28f89 | -3.26592 | -42.21417 | 2025-11-22 03:53:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef8d3d31-412c-3dec-8998-1901d91dfa35 | -4.03712 | -42.51421 | 2025-11-22 03:53:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| e8a9a358-7b69-36a8-933a-d23fb07e644f | -6.36519 | -39.49673 | 2025-11-22 03:53:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 193d9bf3-e3e0-3ab3-ae13-13a813a3053d | -4.66768 | -37.8182 | 2025-11-22 03:53:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 04444268-1d89-3ac8-a051-7bd66e7bf39f | -3.26201 | -42.21357 | 2025-11-22 03:53:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6ceb833-ebcd-315b-99dc-ce2a2cf0a01b | -3.29072 | -43.9193 | 2025-11-22 03:53:00 | NOAA-20 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22829381-79d6-3cf1-9c4d-4086b77ccf92 | -5.86414 | -45.28515 | 2025-11-22 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 102fccdc-bf5a-39ab-a0f1-4cec358913ff | -4.36786 | -43.61329 | 2025-11-22 03:53:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e2d9674-c6f7-3d60-884a-bcd936355cb8 | -2.91882 | -48.23875 | 2025-11-22 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| c20acdc3-b9b0-3945-90a9-0b41601e066d | -2.92644 | -48.23981 | 2025-11-22 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 99a531e4-5562-39ac-8bd2-fdacefc95dcb | -5.35232 | -40.6013 | 2025-11-22 03:53:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3512e0f1-b77a-35b0-90ff-e748a9da9d03 | -5.56948 | -39.8402 | 2025-11-22 03:53:00 | NOAA-20 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b9c84645-8e3b-3230-b2d2-1a7cb3cbecd6 | -5.42934 | -40.66504 | 2025-11-22 03:53:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 666a306b-6903-3e94-8047-84376c6954ec | -6.97735 | -39.8343 | 2025-11-22 03:53:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b8ba1687-84af-370c-8ca7-a87a275c37aa | -6.67413 | -39.49894 | 2025-11-22 03:53:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 98e65a7e-6cb6-3df3-b7cb-9c078e704fb0 | -4.04023 | -42.51989 | 2025-11-22 03:53:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 37.3 |
| b24185e9-8a19-393e-b861-a7759523c8a8 | -6.35393 | -39.8461 | 2025-11-22 03:53:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 58ddb84e-7358-31b0-a322-b703f086f0f8 | -6.79227 | -39.12243 | 2025-11-22 03:53:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ceb22a33-7155-33b6-b7a1-30d7f525f68c | -4.03236 | -42.51859 | 2025-11-22 03:53:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 2da2649e-d329-3066-8314-e891022f7fdc | -6.35336 | -39.84968 | 2025-11-22 03:53:00 | NOAA-20 | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8c693f6d-4ae0-3966-ad2f-eea40195aa79 | -2.93206 | -48.23214 | 2025-11-22 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 59e3b72d-f758-3bec-a584-85cbdf968722 | -2.93303 | -48.23655 | 2025-11-22 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9ea9e0b-1cc5-34a6-a08a-3fb9a20fed65 | -4.66478 | -42.60937 | 2025-11-22 03:53:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 04d6f750-822b-3e61-8c4a-c61e443c747c | -2.93133 | -48.23642 | 2025-11-22 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d31fa4ea-e02b-3a7e-80ca-cee34073aa59 | -6.17477 | -44.54763 | 2025-11-22 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8df8966e-1446-3c49-bd91-14afd6bd53b4 | -5.11079 | -40.72867 | 2025-11-22 03:53:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8f6cae79-cc33-3dbf-88c7-1157c04b04cd | -3.96593 | -39.53684 | 2025-11-22 03:53:00 | NOAA-20 | TEJUÇUOCA | CEARÁ | Brasil | 2313351 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| bd58e09d-f04f-378c-8dd3-b6c2a248b45e | -6.30912 | -39.59706 | 2025-11-22 03:53:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f09331e9-9245-3e62-81c5-d0d313b4bbd8 | -6.20848 | -36.43022 | 2025-11-22 03:53:00 | NOAA-20 | CURRAIS NOVOS | RIO GRANDE DO NORTE | Brasil | 2403103 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 98b66d4b-103d-39de-812c-d62232f50c14 | -6.67747 | -39.49948 | 2025-11-22 03:53:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| acafa1d4-d11a-3cb5-9d42-e7fe1b95b240 | -2.46871 | -47.8358 | 2025-11-22 03:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba18af5e-6ac0-392b-859d-1e95084867f9 | -6.67356 | -39.50248 | 2025-11-22 03:53:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 766168f0-9a30-38c8-a1e1-f577936dd027 | -3.6055 | -40.81067 | 2025-11-22 03:53:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 65cc41af-e466-36f7-a826-7481d8512147 | -5.35581 | -40.60186 | 2025-11-22 03:53:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 36de23e6-bcc9-38e1-be06-6ea3cb892b9d | -4.14518 | -43.69928 | 2025-11-22 03:53:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 08aca2e7-9608-32ef-9dcd-14463ad4d63e | -5.72982 | -42.38792 | 2025-11-22 03:53:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README4.md)
