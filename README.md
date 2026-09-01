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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c333fa3-53d5-3ac8-9ee0-2ea17a2647d7 | -6.1844 | -57.7395 | 2026-09-01 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 0ad5105b-2e38-319d-b36f-13cf9ed5edf8 | -11.258 | -50.5836 | 2026-09-01 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| b235e990-654f-3171-954f-3b9b1ef49d81 | -7.4134 | -49.7465 | 2026-09-01 00:00:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 0429149e-62b0-31bb-b81f-13a7d192df49 | -6.6036 | -58.5972 | 2026-09-01 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 77d5ee84-d7db-31a6-8e8e-5fc15b8fbed9 | -14.6925 | -53.5384 | 2026-09-01 00:00:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 064d06b5-ad12-37df-a60a-dab02ed93e00 | -3.1265 | -61.2377 | 2026-09-01 00:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 895a99f8-49db-374c-a9b7-a8fa8f4cc343 | -11.478 | -45.0868 | 2026-09-01 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 52.8 |
| a4d761c3-7cdf-3286-8c74-98b66cb86eac | -17.3713 | -42.3794 | 2026-09-01 00:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 4271fed3-4e53-3e2f-a6b3-a033ff4f893a | -16.1498 | -52.3679 | 2026-09-01 00:00:00 | GOES-19 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 154.8 |
| ca047121-8849-36fa-9dd2-c0818d799e03 | -3.8417 | -44.0594 | 2026-09-01 00:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 873fb34e-9ded-3862-95c6-191fbe230b49 | -3.8603 | -44.0815 | 2026-09-01 00:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| dbdb6c03-78a5-3086-86cd-13b6772a4672 | -11.3236 | -45.1778 | 2026-09-01 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 8d8db037-3f42-3016-aa49-6b883f28e184 | -3.8416 | -44.0824 | 2026-09-01 00:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 9197118f-26a0-313e-b7b0-d6408555d0a3 | -7.3672 | -60.5875 | 2026-09-01 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 2dfa39a6-21d9-39d6-aaf2-25114caea519 | -18.5089 | -50.8974 | 2026-09-01 00:00:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 116566a8-57d5-3b72-bfd0-dd15a6333ab7 | -19.194 | -57.3926 | 2026-09-01 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.0 |
| 0d4ed819-bd30-3229-8ded-41ef8455b09e | -10.0173 | -44.6849 | 2026-09-01 00:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 140.4 |
| a15d9985-c95c-3412-ae68-6d5d93a28abc | -17.3921 | -42.3495 | 2026-09-01 00:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 331.6 |
| a877a819-3775-32a7-a307-56becf620e7c | -17.3914 | -42.3744 | 2026-09-01 00:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 172.6 |
| 7030cafd-3b71-3bd9-9f6c-0d895aca5af7 | -16.1303 | -52.3707 | 2026-09-01 00:00:00 | GOES-19 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 6cefaab1-337c-375b-9f88-69c75d075159 | -3.0612 | -39.9346 | 2026-09-01 00:00:00 | GOES-19 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 25.0 |
| cb2d27c4-af58-3eb8-97e8-fae7f8ad004c | -17.3928 | -42.3245 | 2026-09-01 00:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 138b727c-ddb0-3ed8-bb83-dd55286d5bf5 | -10.7456 | -47.9978 | 2026-09-01 00:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 27a1d339-d3eb-36b8-860d-06763b2eea64 | -19.1943 | -57.3718 | 2026-09-01 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.8 |
| 303f3718-27fd-3664-86cc-dc36233ada60 | -3.8604 | -44.0585 | 2026-09-01 00:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 7d37cc3e-65ef-388b-9c93-bbf478de87da | -7.3488 | -60.5691 | 2026-09-01 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 6b292822-1d87-32ff-b53a-71fb499234bc | -7.3302 | -60.589 | 2026-09-01 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 8279cc60-23e1-3248-968d-c904c7034db7 | -18.4888 | -50.901 | 2026-09-01 00:00:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 117.9 |
| edcb81a5-2eb6-3f71-baa1-996b5539e1cc | -7.182 | -60.6904 | 2026-09-01 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| c30e0760-f5a3-334f-b42a-c41ebd363581 | -6.1183 | -53.5472 | 2026-09-01 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| dba50e3f-d7e7-3c60-813c-f92229abb315 | -16.1494 | -52.3893 | 2026-09-01 00:00:00 | GOES-19 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 138.7 |
| c24b3f6e-8ce4-3b9d-9f01-a261712d7192 | -6.9551 | -55.655 | 2026-09-01 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| f5315094-9f98-3bb3-8c31-044c41175970 | -17.372 | -42.3544 | 2026-09-01 00:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 180.7 |
| f2d311f9-931b-3aa1-96cb-06cb72f9c538 | -7.571 | -60.4643 | 2026-09-01 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| a068900a-b659-3aa0-a312-5512b599cf3f | -11.2577 | -50.605 | 2026-09-01 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 4b4e0c10-cff5-3355-a326-fb84c935d604 | -16.0547 | -54.3908 | 2026-09-01 00:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 26733a41-bdc5-3fcb-82b9-146cb6ee89cb | -16.1299 | -52.3922 | 2026-09-01 00:00:00 | GOES-19 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 8ccaa532-e008-3ebe-a6f9-e8b940db3641 | -3.0425 | -39.9355 | 2026-09-01 00:00:00 | GOES-19 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 51.0 |
| e8c57b01-f830-3f0f-bcf1-684d3d3cf63f | -7.3487 | -60.5883 | 2026-09-01 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 6ebd7442-af14-3d74-bf69-1090279a84f4 | -3.0426 | -39.9108 | 2026-09-01 00:00:00 | GOES-19 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 22.8 |
| 85431255-d0bd-3ace-bada-142c8495a3cf | -8.87 | -66.8935 | 2026-09-01 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 3583b2ca-273e-3159-8267-0f8971abd8d7 | -6.9553 | -55.6151 | 2026-09-01 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 9013e04a-b9b3-394c-a714-a67e33d1afbe | -6.9367 | -55.636 | 2026-09-01 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 113.4 |
| b9211b40-eebf-3c9c-91d4-ca355e23d477 | -10.0364 | -44.6825 | 2026-09-01 00:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 6575e09b-c0e6-331a-92b0-62b9ff6586bd | -6.9552 | -55.635 | 2026-09-01 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 245.7 |
| 4e15de65-09b3-36d6-9a8d-a32411ad4f8d | -19.1347 | -57.3589 | 2026-09-01 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.5 |
| 9b7ac380-f67f-30d0-9236-28b9938f931c | -10.7459 | -47.9757 | 2026-09-01 00:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 4036e78e-7168-3172-b8b9-c494db213be3 | -6.9368 | -55.6161 | 2026-09-01 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 9b73cb68-5eb4-354d-bab7-b283a766e990 | -17.3921 | -42.3495 | 2026-09-01 00:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 307.7 |
| 8d70ab8d-42bc-3447-95f6-66d5b724dd17 | -7.3302 | -60.589 | 2026-09-01 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| e3783a9e-cb88-3b3f-a77b-366e61e6d8ab | -6.6037 | -58.5779 | 2026-09-01 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| c52dec1a-1d12-3a92-88a7-4fac5b88fb21 | -17.4122 | -42.3445 | 2026-09-01 00:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 75.8 |
| fb78a6b4-4ff2-3992-b827-b7839f5e3cd8 | -7.182 | -60.6904 | 2026-09-01 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.7 |
| af2ac0bf-a974-3fc3-8953-3c69268aa111 | -7.2005 | -60.6897 | 2026-09-01 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| e94c5259-0c4e-3556-8f23-e5d73b9963a2 | -7.5709 | -60.4835 | 2026-09-01 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| fc4f2350-055d-3a8f-a97d-7a446fd26fcf | -16.1299 | -52.3922 | 2026-09-01 00:10:00 | GOES-19 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 4d64e874-3b29-3376-9d0c-98a7b578f052 | -14.6922 | -53.5594 | 2026-09-01 00:10:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| c4b859ad-e7d7-35e3-af22-301ba493ceff | -15.8037 | -51.0844 | 2026-09-01 00:10:00 | GOES-19 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 6ba26644-24e4-34aa-9a5d-f43adb65e6e7 | -10.017 | -44.708 | 2026-09-01 00:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 46e1bd13-2b15-333a-ad91-5e9485db336f | -14.1266 | -52.7895 | 2026-09-01 00:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 500b2551-56b7-3c84-9f1c-bfdf9bee8b7b | -11.2577 | -50.605 | 2026-09-01 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| cf5ce474-3ff6-346e-9136-9d38bc3a56f4 | -3.6215 | -60.566 | 2026-09-01 00:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 441efcd7-cbbb-3f5e-8c48-6eed691c8b61 | -16.1494 | -52.3893 | 2026-09-01 00:10:00 | GOES-19 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 121.1 |
| b194d8b2-8d67-334f-a10f-a0f34d477f66 | -11.258 | -50.5836 | 2026-09-01 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| c11d24f2-21ab-3e8d-b3a2-b02a42d4dfe4 | -10.0173 | -44.6849 | 2026-09-01 00:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 163.2 |
| 541a4c2d-745e-3ab3-97d8-98a5b6dc327e | -6.9551 | -55.655 | 2026-09-01 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 88d5c2cc-cfb7-3b6f-89a0-341df4826f15 | -17.3914 | -42.3744 | 2026-09-01 00:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 157.9 |
| 3a62b5d3-0199-3678-a3b5-5f48bcde450f | -7.3487 | -60.5883 | 2026-09-01 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 122.1 |
| 30e4b7bf-4c07-315d-a474-476f9de9821c | -16.0547 | -54.3908 | 2026-09-01 00:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 445cfa2a-09ac-3ba4-a1a5-f75323ba8365 | -7.571 | -60.4643 | 2026-09-01 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 131.8 |
| d9137414-00a0-3d87-a203-ee2e41cb570c | -11.3236 | -45.1778 | 2026-09-01 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.2 |
| f6f5c163-af99-3ad8-bade-300400eb61a3 | -6.9552 | -55.635 | 2026-09-01 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 162.4 |
| 0f80ad6b-3f3f-34c4-a87a-914d4dc2590d | -7.3672 | -60.5875 | 2026-09-01 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 081fb99d-4e6e-34b0-9a7e-89ca585c13dc | -7.6576 | -73.025 | 2026-09-01 00:10:00 | GOES-19 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 609da0e5-2d5c-3b5b-b176-48c30407bdfe | -17.372 | -42.3544 | 2026-09-01 00:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 37d5afd0-8f3f-3bbd-8a01-978a791d2edd | -18.5089 | -50.8974 | 2026-09-01 00:10:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 180.6 |
| fb532b2e-13b9-38cf-88e2-74faea4213f5 | -6.6036 | -58.5972 | 2026-09-01 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 80.7 |
| bb838012-3639-3e3a-94d9-fea100aaa4fb | -7.6576 | -73.0432 | 2026-09-01 00:10:00 | GOES-19 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 83.2 |
| f6c9309f-3e80-3dc4-b533-485ce86550c2 | -16.1303 | -52.3707 | 2026-09-01 00:10:00 | GOES-19 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 60ebe3c2-ee49-3969-a539-ceb3169ad82f | -14.7119 | -53.536 | 2026-09-01 00:10:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 47ae9886-ee95-3470-9dd6-d5f810951e2d | -10.0364 | -44.6825 | 2026-09-01 00:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 6b6cad11-5116-342a-8d3f-14d66531bc3e | -6.9553 | -55.6151 | 2026-09-01 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| cbe61229-7892-35e5-b220-20fcfd212a32 | -18.4888 | -50.901 | 2026-09-01 00:10:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 3df276e6-c1e5-373d-8570-0f4bcc6189f7 | -6.9367 | -55.636 | 2026-09-01 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 127.4 |
| 7c380ea0-7096-32a3-ae9d-0262dc3ee4ea | -6.1844 | -57.7395 | 2026-09-01 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 0f7f79e2-6d72-38a9-8929-cd49f1f18966 | -7.3488 | -60.5691 | 2026-09-01 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 21d7b179-6602-389a-98c6-07aabbdeecdf | -14.6925 | -53.5384 | 2026-09-01 00:10:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 157.7 |
| a6d5eab8-35f3-326d-bd6a-83e30e5c92ff | -7.2006 | -60.6706 | 2026-09-01 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 74a7e838-3fe5-352f-a91b-4c3eff74fccc | -3.0425 | -39.9355 | 2026-09-01 00:10:00 | GOES-19 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 48.1 |
| 71999453-baa2-3bcd-a56e-8433a2720047 | -6.4245 | -52.2005 | 2026-09-01 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| d27a0791-7e6e-334e-9622-6565348d580f | -7.3303 | -60.5699 | 2026-09-01 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 0d329c6e-2ee0-3300-bee6-cee19ffe5f1d | -17.3713 | -42.3794 | 2026-09-01 00:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 164.1 |
| a9ecf2a8-d335-36d6-9c1d-b7a5c5027ceb | -16.1498 | -52.3679 | 2026-09-01 00:10:00 | GOES-19 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 180cdc0e-02f8-37b8-965a-a174017f7ea3 | -3.0612 | -39.9346 | 2026-09-01 00:10:00 | GOES-19 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 46.5 |
| 2015508e-791b-325c-a8c9-37664a1e2833 | -17.36 | -42.4 | 2026-09-01 00:15:00 | MSG-03 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4ea935b3-4ef3-38d7-905b-c73ca9f0a826 | -6.68 | -55.46 | 2026-09-01 00:15:00 | MSG-03 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58f923e9-f9c9-3035-a3f5-6e4c32b752e9 | -6.71 | -55.41 | 2026-09-01 00:15:00 | MSG-03 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7af517cc-d286-38f5-b79a-a68a58ef5a22 | -10.2 | -50.35 | 2026-09-01 00:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 91cb9839-fe55-3c4f-ae8c-7cecc7fbf9cf | -6.71 | -55.47 | 2026-09-01 00:15:00 | MSG-03 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f92496e-4f6f-3065-b5a3-a15b5a34ceda | -17.36 | -42.35 | 2026-09-01 00:15:00 | MSG-03 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
