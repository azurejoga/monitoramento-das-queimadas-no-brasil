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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7194e3ed-a776-38f2-9304-0a475a058db3 | -10.7715 | -46.3001 | 2026-09-14 14:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| b85b550b-3403-3fbb-93d1-3214a9272c92 | -10.5484 | -51.2945 | 2026-09-14 14:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 6ad02718-db38-36c7-ba3f-4ed0d2d7dea2 | -2.9025 | -50.4004 | 2026-09-14 14:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 149.3 |
| c59a1f7c-8257-307e-baae-3dc3c228a995 | -3.1697 | -58.6437 | 2026-09-14 14:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 114.0 |
| e25afa98-c3e6-32c8-8386-5febf7377903 | -14.205 | -47.4039 | 2026-09-14 14:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 3dfe1145-34d8-34f1-93e8-9e3b35640c14 | -2.6602 | -57.5119 | 2026-09-14 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| b4f41827-9bd9-3de5-b1cd-ddcbc0de99bd | -3.8957 | -60.5984 | 2026-09-14 14:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| b41716c7-79c4-3285-a15b-9a0929b99471 | -9.7036 | -54.371 | 2026-09-14 14:50:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 2fe7364f-7fad-35a4-83d6-37ac0efcd82d | -10.5667 | -51.3349 | 2026-09-14 14:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 1a129f3b-54f2-30c6-bd03-03af43c72e65 | -6.1108 | -57.7035 | 2026-09-14 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 4f927cbe-6ac8-346a-8d02-cf6b88dbfbcf | -6.1111 | -57.6645 | 2026-09-14 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 156.7 |
| aeb3ea04-5945-36fa-b378-4549d237ce82 | -12.1265 | -44.199 | 2026-09-14 14:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| d55b380d-0dbd-33e1-accb-45c2569ce7bf | -7.207 | -46.1187 | 2026-09-14 14:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 924a523a-55bf-343a-9e55-1b29cb05b457 | -12.177 | -48.9623 | 2026-09-14 14:50:00 | GOES-19 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| cbaa1a80-b8f2-3cc6-80b3-6bbb5494d016 | -4.1151 | -60.6696 | 2026-09-14 14:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 89ab5262-e154-3b98-900b-649e5d407fdd | -8.5809 | -44.486 | 2026-09-14 14:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 120.3 |
| cfc0e84a-5682-348d-82f0-02d7c97f9545 | -10.7722 | -46.2549 | 2026-09-14 14:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 338ebef1-22f8-329a-909e-9abee4d91973 | -3.4089 | -58.2142 | 2026-09-14 14:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 202.4 |
| 4e1a8389-9ad3-3e83-9280-6d3690ba91cb | -7.1048 | -41.7971 | 2026-09-14 14:50:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 197.5 |
| f3f9fc19-0b00-30a5-9a2c-a2bd26eb8408 | -8.6194 | -44.4357 | 2026-09-14 14:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 189.2 |
| 2370018e-57bc-32d5-bba2-682b4384da91 | -7.1051 | -41.7731 | 2026-09-14 14:50:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 225.0 |
| 9f9c915d-f56d-3bae-85fa-af293c052744 | -10.6832 | -54.127 | 2026-09-14 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 180.8 |
| d5858ab0-bb5f-3216-8bef-d3623caf2da4 | -15.5768 | -48.792 | 2026-09-14 14:50:00 | GOES-19 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 164.0 |
| 3dec30be-5f41-36a9-9975-9cc77bdb914b | -8.8081 | -45.8753 | 2026-09-14 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 234.2 |
| 117198a6-3131-3318-a49a-763c5b60701a | -10.81 | -46.2726 | 2026-09-14 14:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 172.0 |
| 38eddf3d-79fa-331b-ab2d-d0918fc66408 | -2.6785 | -57.531 | 2026-09-14 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 864a63ce-e57e-3aa6-85c9-4882fb8e1aa9 | -3.3493 | -59.8288 | 2026-09-14 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 157.4 |
| d2f22f17-3dec-3b8b-b493-6d38d5cf4d1e | -6.1422 | -52.7711 | 2026-09-14 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 857d8ea2-48be-3d76-8715-40b7a920defd | -3.728 | -61.7367 | 2026-09-14 14:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 12aff450-8cf8-3b0b-bb98-5d926860f412 | -3.728 | -61.7555 | 2026-09-14 14:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 33d9f3b6-1bc6-3878-911f-9d5d3acfd8bd | -3.4272 | -58.1945 | 2026-09-14 14:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 123.8 |
| d8ce80c1-8173-3d11-ac18-efb72cd9c421 | -4.1334 | -60.6692 | 2026-09-14 14:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| a620b83b-f8fb-3b13-8d95-585128baa81c | -3.4089 | -58.1949 | 2026-09-14 14:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 869aaa2b-1d28-377a-88cd-4901c6bb89c2 | -3.3677 | -59.8094 | 2026-09-14 14:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 7c3410d2-b0e3-3177-b5c7-8d49393cb826 | -2.6785 | -57.5115 | 2026-09-14 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| e32c1347-c2d9-390e-b4ff-398513ccb7c2 | -6.3436 | -55.8243 | 2026-09-14 14:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 6ff6c29f-78af-385f-a79c-eb35c23fff52 | -6.8446 | -55.5611 | 2026-09-14 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 922bae55-fa2a-3904-8472-2cfe20bd3126 | -8.5415 | -54.7187 | 2026-09-14 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| d5292d46-ce8d-319e-963b-e69599ec6ed5 | -11.8362 | -50.0244 | 2026-09-14 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 54d39935-530c-3fcd-b3a1-5e3979156036 | -7.0859 | -41.799 | 2026-09-14 14:50:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 161.3 |
| 041aa7b0-3511-35aa-951a-2461c85d387a | -6.1109 | -57.684 | 2026-09-14 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 518.5 |
| 7ae41cd6-328e-3d23-a2ca-e39b2d2cb56c | -4.115 | -60.6886 | 2026-09-14 14:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 17f56b21-abdd-36ae-b6dc-da6a32d18297 | -13.5526 | -51.4629 | 2026-09-14 14:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 9dff852d-186f-3e9b-986a-3757707e4846 | -12.4901 | -41.4012 | 2026-09-14 14:50:00 | GOES-19 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 90.1 |
| 04aabae2-936e-32b8-82d4-e5c98bbfd15d | -3.3141 | -59.3515 | 2026-09-14 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 3cdc0a83-cd8c-3962-ade2-db725345733b | -14.1852 | -47.4296 | 2026-09-14 14:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 79.5 |
| c60c3b62-7790-3224-bec0-e6f949be4646 | -3.3494 | -59.8097 | 2026-09-14 14:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 4f6e9c26-25de-3826-91c3-2f2110570dc9 | -3.4449 | -58.4066 | 2026-09-14 14:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| c574521c-0055-3ddc-b436-d001e346ebcc | -2.6601 | -57.5702 | 2026-09-14 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 84.8 |
| ee2143e3-4557-339a-aed6-99ee2e34abab | -2.6602 | -57.5313 | 2026-09-14 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 103.6 |
| a4e8389e-77d9-3b30-87f6-5b58ef4c32f0 | -9.5126 | -45.4796 | 2026-09-14 14:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 2e35adb6-98d1-33da-a886-f38acf583f94 | -5.2023 | -49.3348 | 2026-09-14 14:50:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 17e7a0ac-9f72-3204-a932-34032ac4443a | -13.3251 | -51.2997 | 2026-09-14 14:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 792e071a-f905-305e-b0cc-93cf1400b9c8 | -10.7726 | -46.2322 | 2026-09-14 14:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 124.9 |
| b94190b4-b81f-35aa-90d7-a0c87d486893 | -15.5567 | -48.8176 | 2026-09-14 14:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 105.1 |
| ce58f8c7-e499-3113-ac5d-bda12bc93897 | -3.3871 | -59.4075 | 2026-09-14 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 88.9 |
| d2a785d7-1194-334f-afc0-e496f44fb792 | -10.3116 | -45.3136 | 2026-09-14 14:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 2756e331-ba22-34f1-9398-f3a9bbb92574 | -7.3017 | -51.7525 | 2026-09-14 14:50:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 52610dde-c9f5-3027-87b4-223b9bfcbdad | -9.4936 | -45.4818 | 2026-09-14 14:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 144.4 |
| d2d187fb-094d-3d87-8e14-646c35305356 | -10.6829 | -54.1475 | 2026-09-14 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 271.4 |
| 96ec06b9-4447-3065-9147-82d99a0c6dbe | -10.7274 | -50.6192 | 2026-09-14 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 98.9 |
| abfb5c48-1930-3226-9e1c-dfe9d6aa8483 | -6.8445 | -55.581 | 2026-09-14 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| d1742a11-0613-3344-afeb-0800db1d715f | -2.6601 | -57.5507 | 2026-09-14 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 231.8 |
| b178b833-3d65-321c-9c20-3dfca52dfbc6 | -15.5121 | -43.8455 | 2026-09-14 14:50:00 | GOES-19 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 98.9 |
| bc57da4c-d74b-31d6-8439-6fe566898f5c | -3.1514 | -58.644 | 2026-09-14 15:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 49d4d104-f2fb-3ef3-bc8e-a0d922bcd83f | -8.5812 | -44.4629 | 2026-09-14 15:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 97c60cc1-36e0-3078-85ac-4551fd3b6041 | -3.3494 | -59.8097 | 2026-09-14 15:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 59a2d9a9-076b-3713-952f-533d1f8159c2 | -6.3436 | -55.8243 | 2026-09-14 15:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| d686a106-227c-36e0-9836-15de41f6a266 | -10.3116 | -45.3136 | 2026-09-14 15:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 79.9 |
| b1f7edde-e706-30e7-a034-2ec1a255d7ce | -12.177 | -48.9623 | 2026-09-14 15:00:00 | GOES-19 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| debcb89d-7a9f-3a3a-9b3b-aae3cb706abc | -4.1334 | -60.6692 | 2026-09-14 15:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 48da8fdf-c046-32e2-a3c0-07661d68b3c9 | -14.205 | -47.4039 | 2026-09-14 15:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 227.3 |
| d32b89a5-154a-31c5-bbe6-899153c162ef | -9.6275 | -46.729 | 2026-09-14 15:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 589fbb80-319b-3f63-9a7d-9de55419586b | -3.3505 | -59.3891 | 2026-09-14 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| cb98b373-3f30-3835-aefa-e1807b075a5f | -3.3871 | -59.4075 | 2026-09-14 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 02a88bb8-d2a0-3ac5-b3e3-b80133c2ed83 | -13.2867 | -51.3046 | 2026-09-14 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 209a0447-1c62-3f80-9551-fb89572d9863 | -11.2199 | -43.4441 | 2026-09-14 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.1 |
| b5f34dcb-6877-325f-8046-2467ad857610 | -11.8154 | -46.5899 | 2026-09-14 15:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 48.8 |
| bd3e249d-83c8-3420-8a9b-9ced9d7c3d7c | -9.7036 | -54.371 | 2026-09-14 15:00:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 9f02cdf8-bcf2-312b-9163-385abdef097b | -3.314 | -59.3706 | 2026-09-14 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 149.5 |
| d94bc313-b3de-3a47-accb-db64a3b1ef01 | -9.4936 | -45.4818 | 2026-09-14 15:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 138.4 |
| dedb7cbf-ae14-379c-9842-76d3816c1f9f | -3.1814 | -61.1802 | 2026-09-14 15:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| e7129bc8-7bb5-3cdf-ac0e-66cdd941b136 | -3.1816 | -61.1235 | 2026-09-14 15:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| cb0c1068-516d-3bed-b364-be6271731406 | -3.332 | -59.466 | 2026-09-14 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 1aeda229-6e66-332b-93c8-2aa34aab4e1a | -10.7274 | -50.6192 | 2026-09-14 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 117.7 |
| cc209035-22cf-3ffc-be52-fbfe3eb28df0 | -3.9594 | -43.1271 | 2026-09-14 15:00:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 8c64c577-6114-3068-b745-a48a684434c4 | -3.728 | -61.7367 | 2026-09-14 15:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| dcd20c5f-6a43-3124-a999-14926f7a2fc4 | -10.6829 | -54.1475 | 2026-09-14 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 240.0 |
| ab1cb7f4-2385-376b-8721-68b55116adf7 | -8.6194 | -44.4357 | 2026-09-14 15:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 230.9 |
| 2a9ba2c5-ade9-307d-9080-12bb749a8cfc | -9.9956 | -50.2675 | 2026-09-14 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 2a6c93f3-8e32-3f1f-9852-32bfcb2f694c | -7.7824 | -46.6705 | 2026-09-14 15:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| aa606ce2-0672-3964-aa13-ef38bcbfe4bd | -13.5526 | -51.4629 | 2026-09-14 15:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 302.9 |
| ceaadc5d-81c6-3dec-8a6f-371c5a6d5bab | -11.5984 | -47.0018 | 2026-09-14 15:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 943dfbf3-72fe-3d2e-ba21-32319467e0bb | -8.8081 | -45.8753 | 2026-09-14 15:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 195.1 |
| 9ccb3ac6-0196-359e-826a-3ff11debb4ef | -1.7133 | -54.9521 | 2026-09-14 15:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| a3437712-ae55-3624-a629-d6107db3291e | -13.5719 | -51.4605 | 2026-09-14 15:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 159.5 |
| 6cee068f-551c-3f26-bf62-a17ec9ac5d0e | -10.6522 | -50.5845 | 2026-09-14 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| cd8915bf-57ed-347c-8775-49816b26cfac | -3.8957 | -60.5984 | 2026-09-14 15:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| c582ac1e-3bfc-33e0-971d-e8770a9d0d68 | -10.6525 | -50.5631 | 2026-09-14 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 572acdc8-4a4e-34be-8272-5e55f314a5a7 | -3.3305 | -54.2005 | 2026-09-14 15:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 164.6 |


[Clique aqui para ver as próximas entradas](README77.md)
