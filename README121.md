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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08dec715-fadb-35bf-8c0e-79e04d0d07e9 | -12.10947 | -45.02642 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 409928dc-a668-3851-b2c1-79e8fce63200 | -11.18486 | -50.56843 | 2026-08-31 16:30:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e432cb94-5bd5-30dc-84d5-a1335a813992 | -8.92412 | -45.04002 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 4a7f12f3-8a6d-3988-8272-33df45dde30d | -12.07292 | -47.20426 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 48.3 |
| aea2b909-f38d-3dbb-8cd6-6ed265074595 | -10.92151 | -50.62388 | 2026-08-31 16:30:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 08c6d185-537c-3ace-8d87-a6928156f141 | -11.3811 | -45.17617 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.8 |
| c0b31da3-686c-39fa-938e-979d4f9749f7 | -11.3708 | -45.42684 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| c16b9224-0f91-3a6f-95e5-a436594a0828 | -9.16387 | -49.989 | 2026-08-31 16:30:00 | NPP-375 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 460af318-a83a-3cb8-8684-a338dc4fe782 | -13.4248 | -51.38554 | 2026-08-31 16:30:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1deb6a08-3384-353e-a518-7567199ec5c2 | -11.24531 | -54.00752 | 2026-08-31 16:30:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 54881b95-7a28-3e93-9a24-3b610baca0da | -12.91829 | -45.85477 | 2026-08-31 16:30:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 8e97feb4-192f-31db-b169-eca9916698cf | -10.30739 | -49.99898 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| c6e7ca65-1c3f-3d15-95a7-a46a1b7a2e61 | -11.19098 | -45.04485 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2281a656-2ca9-31ee-82ff-4a9934465272 | -10.85255 | -45.32185 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0812e825-10ec-32af-8217-6f774abfcc2a | -11.35144 | -45.23475 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| d467cda4-4d49-3fbb-82a9-f2c9e3c6477e | -10.74278 | -54.0428 | 2026-08-31 16:30:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 931bbc54-3cfa-334d-b45a-6c9bba20d272 | -9.64939 | -46.05184 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| be8efa8e-1065-3116-9e8f-e2fc192edd22 | -11.20187 | -46.10078 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| fec9d996-8f37-31f2-809b-95ee3ad0b288 | -13.41904 | -51.38618 | 2026-08-31 16:30:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3cea578a-a774-307c-9f40-ee9bbfeeaf8c | -10.3978 | -45.08043 | 2026-08-31 16:30:00 | NPP-375 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d7a2ada4-38dc-3792-a988-f022d0ee15c4 | -11.2316 | -45.09253 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 03dd5f9a-297c-35b6-b347-9252e566c9ce | -10.19342 | -40.08289 | 2026-08-31 16:30:00 | NPP-375 | JAGUARARI | BAHIA | Brasil | 2917706 | 29 | 33 | nan | nan | nan | Caatinga | 12.9 |
| c5ef800f-590e-3e2b-a7b6-903dc40af37c | -9.41927 | -45.68273 | 2026-08-31 16:30:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.4 |
| ee7a24a9-0831-3a98-900a-8c817ccd1dbb | -9.43835 | -45.6777 | 2026-08-31 16:30:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 81e4b6f2-fd85-34ff-9b6d-381a60e5646b | -14.96267 | -54.58458 | 2026-08-31 16:30:00 | NPP-375 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7f12d5d2-26b7-3639-a68a-a7c00db7175d | -11.20449 | -45.06063 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ee619514-6ac3-3c9a-8f6d-ef4830f16905 | -11.66988 | -47.62088 | 2026-08-31 16:30:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e4595a2b-3859-3001-a518-fb4da656d978 | -12.97835 | -40.71489 | 2026-08-31 16:30:00 | NPP-375 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 3460c877-db3b-3b7d-9339-f08c2c1c93b9 | -13.46424 | -51.4159 | 2026-08-31 16:30:00 | NPP-375 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| efdbec2e-c4e8-30a8-b115-791e1b493185 | -13.26834 | -51.60472 | 2026-08-31 16:30:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7e67fbf0-5a85-3311-9e89-6ca288efdc22 | -12.07341 | -44.98601 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f81c8501-65ca-3fb8-aeed-1e71436daab0 | -8.76315 | -45.39408 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 8f9681cf-8582-3fcf-b1d6-359486affc5d | -11.91669 | -45.07883 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 1ec83612-2417-344e-b6d9-428d6317aa52 | -10.02055 | -46.16321 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0627aa8f-6ea3-3907-ab86-9a75b46d835c | -11.2242 | -45.09351 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9efbce82-8ddb-3fe7-b098-215b53667725 | -9.20174 | -47.99823 | 2026-08-31 16:30:00 | NPP-375 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9c1836e5-f2b2-3a5b-9c88-0919ff309750 | -8.92294 | -45.03181 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 8f453def-d47c-3ce6-b63d-663c8c69cfd3 | -11.19405 | -46.10199 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 2eb22d9b-15c1-3efb-9fe1-2fc04f7f42f6 | -11.3199 | -46.37387 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 63f90cd7-4d97-3138-85b8-84c2b3a20d6b | -8.74418 | -46.46936 | 2026-08-31 16:30:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1d4eb0d7-49bf-3eb4-95c8-48d4185673c6 | -11.03817 | -47.12446 | 2026-08-31 16:30:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f3445114-2bff-3ba9-8374-e9f566acdccb | -11.24775 | -51.2625 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 43.0 |
| d6542a32-4376-36cc-ad41-cbc06df0fb3f | -8.88463 | -46.02942 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 176cc322-c521-358f-8fbb-7a401fc7fd33 | -11.91411 | -45.08057 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 92a9a824-c0a2-3171-84f1-999e393bd8a9 | -8.73994 | -39.00543 | 2026-08-31 16:30:00 | NPP-375 | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 32.7 |
| 5ae37910-377c-306b-a1ed-abf6a64eb818 | -12.17527 | -50.53812 | 2026-08-31 16:30:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a1731b1f-b0d1-3deb-a847-69be0568bdd5 | -9.67202 | -47.93227 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 2aabe88f-331b-3674-91ef-75d04ecb3cd6 | -13.07928 | -45.17342 | 2026-08-31 16:30:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 17cdfdda-180d-3780-b288-4c8f39dbddba | -12.11197 | -40.47707 | 2026-08-31 16:30:00 | NPP-375 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 81faccfb-9c06-34c3-85d8-9176a7bad1b2 | -10.1301 | -45.89688 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 26d24d62-f03e-3d69-afdc-7418445ea6ce | -14.41614 | -53.0965 | 2026-08-31 16:30:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3556fda3-441d-3385-b2ce-ccf9e9149c5b | -10.45062 | -46.74908 | 2026-08-31 16:30:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 49e3153b-038e-394f-b5df-7b0dab71c56a | -8.38893 | -44.99013 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6a90506c-4bf1-3f4a-bcee-cd2cc4c7078e | -9.30217 | -45.39494 | 2026-08-31 16:30:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 34.0 |
| b70501b7-3992-3890-9d94-559e1c4d2512 | -11.22296 | -45.11139 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 3855abe6-2a57-3733-9c6d-04a1b4a7227e | -11.20392 | -46.11594 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.9 |
| b381b3bb-bae8-3ede-8a35-18bcc97932a9 | -14.44431 | -52.5148 | 2026-08-31 16:30:00 | NPP-375 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 6ab20520-3b2f-358f-b071-8746524ae4d1 | -9.67688 | -47.93567 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 5bfe5414-66d6-3000-9202-47ff6e6fb4d0 | -13.08754 | -45.17706 | 2026-08-31 16:30:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 59737d40-4fa0-3860-ada3-b2bacaa63c83 | -8.85729 | -47.08862 | 2026-08-31 16:30:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 611df5d4-52e8-375b-b86e-9b3f87d2ded6 | -14.58664 | -53.60832 | 2026-08-31 16:30:00 | NPP-375 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 31.1 |
| e1353e70-16e1-3978-b581-a2d4b0115c4b | -14.48168 | -49.0396 | 2026-08-31 16:30:00 | NPP-375 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 263a18ec-a8cc-3af4-b58e-51477d20b5fd | -11.23788 | -45.13668 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 3ea11293-f95f-3cac-827a-0018a8a95d2c | -9.6748 | -47.95264 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 168.5 |
| 862abd51-c212-352b-a892-f44eec7f8b7a | -11.67362 | -47.61565 | 2026-08-31 16:30:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| be26c13f-f828-3843-9a2c-cb34d7239953 | -14.95914 | -54.58963 | 2026-08-31 16:30:00 | NPP-375 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 284ddd31-c885-38a3-86fe-9e30bdfc90bd | -11.21222 | -46.08884 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| e0417845-9342-3b2d-bca1-2fe953d9b6f2 | -9.20398 | -47.99841 | 2026-08-31 16:30:00 | NPP-375 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| cd1552ed-2887-3899-bd40-923e5ea3221e | -10.10252 | -50.29795 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f5adf6e2-321a-3746-a979-dc2282870ec3 | -8.88085 | -46.02993 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 62e79cac-49f2-36a5-aaa1-0b4e8f62bc26 | -11.63205 | -50.18234 | 2026-08-31 16:30:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4674fd4b-3965-3c96-b204-30fcd8e7dd95 | -10.38794 | -48.24019 | 2026-08-31 16:30:00 | NPP-375 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 031d213f-0cba-311f-9b64-c8228b457996 | -10.98445 | -48.38731 | 2026-08-31 16:30:00 | NPP-375 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cf56af00-092a-36e5-bc93-66b112eb7aff | -12.09256 | -44.98757 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| db286592-5110-35c9-a69d-fed87759fd41 | -10.30663 | -49.99317 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| f60fdeab-3936-3b62-9c00-63a6a218cbf9 | -11.22791 | -45.09304 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 014f2c9d-bc07-34aa-9f78-75d447ff714f | -11.32164 | -45.18484 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 63678041-d507-32e0-9035-08ab90a2859d | -10.75251 | -44.85852 | 2026-08-31 16:30:00 | NPP-375 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 74a306d9-3da0-3780-8c89-1ecb2a04d7e1 | -10.78466 | -50.72569 | 2026-08-31 16:30:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a9dc1a41-c753-37a3-a663-7d7521d7f689 | -11.20775 | -46.08219 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 1ead0974-2f2c-3629-970a-b49a397284df | -11.93571 | -45.07194 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 55ad6438-a071-39cd-89f1-cb22fe4cf10a | -14.21372 | -48.64207 | 2026-08-31 16:30:00 | NPP-375 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 11d0d5d4-151f-3472-8501-b5ddd2a2062c | -11.5417 | -45.47173 | 2026-08-31 16:30:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 6102e108-c6cd-392c-946f-437adb3e2c03 | -10.86027 | -45.37577 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 474bf733-a0aa-334b-a49d-cabf8bc46bd2 | -9.1688 | -49.98835 | 2026-08-31 16:30:00 | NPP-375 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 36f7adf1-692d-3555-8ed5-b7a291818c8d | -11.19403 | -45.03982 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 469e0477-eff8-3460-984f-0f54bf084553 | -10.39843 | -45.08473 | 2026-08-31 16:30:00 | NPP-375 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 394da113-2b4b-3bcf-bcdd-bb8bf6601645 | -11.33357 | -40.44322 | 2026-08-31 16:30:00 | NPP-375 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| fb0e7966-0f84-3066-a301-1962a582a205 | -11.91845 | -50.81555 | 2026-08-31 16:30:00 | NPP-375 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fe9a07f0-7c55-320e-affd-2fa01b3b5bc9 | -9.67908 | -46.54417 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| e97dbc8e-2af7-3f71-9e44-3e609d53cf34 | -14.5782 | -53.59158 | 2026-08-31 16:30:00 | NPP-375 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 29.5 |
| eb223a28-6187-3177-acd6-e037cd2b7c2a | -11.04364 | -49.68613 | 2026-08-31 16:30:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| eca58330-d119-3954-b501-09d92c641fd8 | -12.07501 | -47.1877 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b6f52727-9ff5-34fb-87a5-a7494ec46a2c | -11.16192 | -45.0435 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 507ab321-8731-3007-a5dd-cacbfabb630d | -8.75191 | -46.46816 | 2026-08-31 16:30:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| f2033c6a-4a3a-31fe-9046-2ceaf85a6240 | -13.07169 | -45.1745 | 2026-08-31 16:30:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 8c21f889-9966-3671-96fa-be42f0fc44e0 | -11.25091 | -54.01048 | 2026-08-31 16:30:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| b4870fd2-800e-37cf-9105-2d3c580699f1 | -11.24896 | -51.26283 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 3ea201c6-7269-3b77-ba7c-1ba557bc004e | -12.08571 | -44.99265 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 1d35fb07-7939-32db-aa31-381aae04805d | -14.09278 | -52.19331 | 2026-08-31 16:30:00 | NPP-375 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README122.md)
