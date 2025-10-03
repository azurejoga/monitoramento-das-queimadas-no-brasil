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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85f28525-ed7a-3326-aac7-6a64dd69c567 | -10.26325 | -50.36817 | 2025-10-03 00:52:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 30.4 |
| b571f7fe-6e68-384e-9fb0-f67a7253b8cd | -12.6245 | -46.95956 | 2025-10-03 00:52:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 60a7d93d-264a-3871-8ace-afb3ef126da6 | -13.76569 | -51.27882 | 2025-10-03 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7ea08a68-c6f5-3c50-9f4e-246bfed485a3 | -7.75872 | -46.24058 | 2025-10-03 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 36.3 |
| cbd4e1c2-db55-3583-bce2-7a6e5594fde3 | -10.87608 | -47.05291 | 2025-10-03 00:52:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5b6e5ca8-4593-3cbc-9423-cc0faf9d9414 | -13.75018 | -48.01831 | 2025-10-03 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 1815d57f-fd0d-3191-b6e4-00ccf48d5ccb | -11.21586 | -49.95403 | 2025-10-03 00:52:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 005c65de-af66-3474-a2f7-a2703ddc712b | -11.32134 | -49.01638 | 2025-10-03 00:52:00 | TERRA_M-M | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 9e8e2d09-1413-38ba-ae8b-c39b50abf83a | -14.62192 | -48.25182 | 2025-10-03 00:52:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| ddffcf68-f359-3da7-998c-902705538a5f | -13.22783 | -48.50183 | 2025-10-03 00:52:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6b0e6eda-440f-30d2-97a5-e047e1ed838c | -13.13159 | -47.89278 | 2025-10-03 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 4ecc9d73-bd43-3be7-b723-1e4568cc28ac | -12.84822 | -50.50478 | 2025-10-03 00:52:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| eb4a0799-5f01-366a-81cb-99f0fdf3ab24 | -11.07207 | -48.35859 | 2025-10-03 00:52:00 | TERRA_M-M | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 6bce8f01-ccd0-35b0-b974-ee41e0c8c5e6 | -11.81196 | -45.033 | 2025-10-03 00:52:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 5208a64f-a8c4-352a-8f54-a80dd80f138a | -5.65034 | -43.91062 | 2025-10-03 00:54:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 0a7ad095-a02b-38b0-924b-29645272cfe3 | -4.57384 | -46.5191 | 2025-10-03 00:54:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 8e4e39f1-cfcf-3251-b893-62b88c702913 | 1.78817 | -55.82243 | 2025-10-03 00:54:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| bb5c3e21-a83c-3354-8871-822845ab4c7a | -4.64681 | -45.79279 | 2025-10-03 00:54:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 5f3c0888-6302-3095-8214-4d061a144b60 | -6.52353 | -49.56825 | 2025-10-03 00:54:00 | TERRA_M-M | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 7297207e-e071-36fa-b5ac-2e43a724e88c | -4.65174 | -47.55844 | 2025-10-03 00:54:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 17.9 |
| d4a7ab02-3870-3706-a05e-6d1b33f86552 | -4.64263 | -45.78638 | 2025-10-03 00:54:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 20.6 |
| ed1e5084-a7bd-3b0e-b88f-af97fb969c9b | -4.66309 | -45.8156 | 2025-10-03 00:54:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 375.6 |
| a76125c9-c485-3919-aabd-9173b28fcf7e | -1.0762 | -53.67724 | 2025-10-03 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 068f12be-6117-3c11-a1f4-6346874e62a4 | -6.05738 | -44.60892 | 2025-10-03 00:54:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| af7da887-ebe0-3d93-9478-23a011bae1b3 | -1.34298 | -49.25331 | 2025-10-03 00:54:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| f230d1fa-f302-3cd1-a64c-9aa7ab13f453 | 2.12248 | -55.81348 | 2025-10-03 00:54:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a666b623-4c73-3ad0-8b30-37472916e94d | -4.66698 | -45.82166 | 2025-10-03 00:54:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 198.3 |
| c0982f78-6887-3320-94d1-ac9a148fb546 | -2.12611 | -56.53163 | 2025-10-03 00:54:00 | TERRA_M-M | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b2de2944-43d6-3a94-af35-3f022b29d489 | -6.05716 | -44.65021 | 2025-10-03 00:54:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 8652d36e-9be2-3be9-9fac-e29949a81ab4 | -3.93184 | -47.55617 | 2025-10-03 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 27dca197-0935-368a-9814-98a30ccfc167 | -5.00229 | -56.07049 | 2025-10-03 00:54:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ce63cb45-d993-3cfc-bc11-0440f13f7745 | -2.78841 | -51.80191 | 2025-10-03 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| fc3e847c-f125-306f-9745-058b8d4d6e20 | -6.05167 | -44.6149 | 2025-10-03 00:54:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 180.5 |
| 0cda99ba-f7eb-3892-8ee4-4dd02a1747da | 1.51324 | -55.81019 | 2025-10-03 00:54:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 555833cb-9a49-392a-b60e-cfa454bea529 | 1.51082 | -55.82766 | 2025-10-03 00:54:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 50846be5-c74a-3a79-a2c2-ceaa55da3a17 | -5.64068 | -43.94788 | 2025-10-03 00:54:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 108.2 |
| abca12c5-2e6a-3d97-9058-627bf68377e2 | -4.67364 | -45.78234 | 2025-10-03 00:54:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 71.1 |
| a1ca5c4f-e01a-374f-a9a3-3f354839911d | -3.7885 | -52.0594 | 2025-10-03 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d69af6c0-5d99-305f-b8f8-38153a920096 | -4.76874 | -45.33052 | 2025-10-03 00:54:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 9ccc7dba-ea0a-385c-881d-86055e690943 | -2.78684 | -51.79065 | 2025-10-03 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 4a40f8f0-a1eb-3056-b56e-fbf7d053faf1 | -3.09305 | -47.00617 | 2025-10-03 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 3c29dc90-8794-39aa-b0b1-d886859a4b0f | -2.10286 | -56.82792 | 2025-10-03 00:54:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2e86cdc4-a15c-3e35-918e-233c0c5fe50c | 1.51203 | -55.81892 | 2025-10-03 00:54:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 10e7c224-0c16-3a37-a5e3-a44a2574d887 | -4.65153 | -45.82382 | 2025-10-03 00:54:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 09535405-fd25-35a6-bc84-722aef7efec2 | 1.74577 | -55.86991 | 2025-10-03 00:54:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f7ce2079-4cc6-3df3-a43e-dda4f1562489 | -4.56972 | -46.49177 | 2025-10-03 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 22.9 |
| f239362d-0c85-3aec-9116-7ea92b23d97f | -1.0866 | -53.68533 | 2025-10-03 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| b116b2d1-392e-3733-8761-88095c19f153 | -2.92462 | -48.30453 | 2025-10-03 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| f6123bb8-a96f-3bef-a716-7077113c79f2 | -3.09711 | -47.03246 | 2025-10-03 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| dc2a7dca-7ae3-3a48-9bd0-75d3db7bd723 | -6.06312 | -44.64438 | 2025-10-03 00:54:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 38.3 |
| cd6fcb11-856b-306e-b46e-ae98a6b581bb | -5.38292 | -47.20626 | 2025-10-03 00:54:00 | TERRA_M-M | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 126.7 |
| ef3c0b40-a182-36a8-b988-adbcc4132011 | -1.20933 | -49.12037 | 2025-10-03 00:54:00 | TERRA_M-M | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 5004e5c8-b6e8-3c29-84a1-0cd759b6ae95 | -6.03513 | -44.61707 | 2025-10-03 00:54:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| ab40117b-4e89-35d7-bd4b-5520ce066ea7 | -6.24324 | -45.36674 | 2025-10-03 00:54:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 338.5 |
| deaf8dad-22a7-3712-97d3-1daf90198d65 | -6.52575 | -49.58275 | 2025-10-03 00:54:00 | TERRA_M-M | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| c32c929d-2acb-3adc-bf0d-29649435c249 | -1.2083 | -49.12633 | 2025-10-03 00:54:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 0aec4440-eaaa-363e-bf4d-555f4577d06e | -6.23833 | -45.33515 | 2025-10-03 00:54:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 0ca0c671-5ec0-3495-a816-4fece3e95f8d | -2.92701 | -48.30989 | 2025-10-03 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 35fbf48e-3fc6-30f1-8ac4-41aa892ca5fe | 1.50961 | -55.83639 | 2025-10-03 00:54:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c2ae7a6d-e81d-3742-9fe1-be85c3a4cf15 | -4.67859 | -45.81375 | 2025-10-03 00:54:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 0c3cde71-520f-3125-b8b5-248d70e01965 | -5.8335 | -53.66826 | 2025-10-03 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a049c0d3-075a-369a-b499-dc835c1e2f2f | -4.84927 | -45.21567 | 2025-10-03 00:54:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 43d522e8-af58-3424-a383-f07d2f1f3fda | -6.04068 | -44.65255 | 2025-10-03 00:54:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 3af06c52-d992-338d-a3c9-051a63691e7e | -5.48772 | -52.13515 | 2025-10-03 00:54:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 47c254bd-dc77-3c63-a5f3-c8d9d9ee4afd | -3.79003 | -52.07009 | 2025-10-03 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0b328756-1624-3577-8af9-281a3ccd3f48 | -5.36932 | -47.20859 | 2025-10-03 00:54:00 | TERRA_M-M | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 31.9 |
| a1177828-3536-3b98-856f-0bff01d8cc55 | -3.93512 | -47.57872 | 2025-10-03 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| e22ada4c-4352-38ae-9877-3be56b7b7264 | -6.04085 | -44.61125 | 2025-10-03 00:54:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 4cf7e975-1ede-378d-bb10-009c0c2cef26 | -6.04663 | -44.64661 | 2025-10-03 00:54:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 2b6c18fd-35f0-3dd6-be9c-842d20c00454 | -5.63955 | -43.95542 | 2025-10-03 00:54:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 61888293-732d-3376-b14b-ef034019e242 | -3.33711 | -52.0573 | 2025-10-03 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 08bdb851-4721-3ed8-9f83-76e22aa2ecf2 | -3.9388 | -47.54936 | 2025-10-03 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| e669151e-d572-3ce1-b109-c5af485e645b | 0.31586 | -51.12548 | 2025-10-03 00:54:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ef52b594-1f8b-36f9-ab45-ff8324950d9e | -3.94223 | -47.5719 | 2025-10-03 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 1fb19eaa-c22d-3744-b523-976a55817fd8 | -4.66233 | -45.79086 | 2025-10-03 00:54:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 658.1 |
| a9299435-0f46-3371-9c93-d7257782b198 | -5.65122 | -43.9033 | 2025-10-03 00:54:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| fec4f09d-f1a9-3a7e-ad89-00efe785ebcd | -2.25123 | -47.87688 | 2025-10-03 00:54:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| da64c890-1593-3053-86bc-e5797aa72a81 | -1.19306 | -49.10917 | 2025-10-03 00:54:00 | TERRA_M-M | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| c28dd146-bf0a-3982-afed-9eaea320b7d7 | -3.09099 | -47.01216 | 2025-10-03 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| dd008e8b-36e3-38cc-8a89-bdfb06ee0025 | -1.14803 | -54.19328 | 2025-10-03 00:54:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 25375281-9686-3b2b-aedd-3e7ca97a2509 | -1.08529 | -53.67588 | 2025-10-03 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 91d638b1-5094-3002-acf8-06f021bcc454 | -5.61516 | -51.93833 | 2025-10-03 00:54:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3b8128fb-9c87-3e21-af72-d5d97dc1fb7b | -2.2444 | -47.87119 | 2025-10-03 00:54:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 7545a6ce-36a8-34ee-957a-48891cbe9684 | -5.63298 | -43.914 | 2025-10-03 00:54:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 388.0 |
| 2b15da39-1fa1-3578-a84b-dbf873c0d2f2 | -3.09484 | -47.03838 | 2025-10-03 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 41ed82a0-be09-3f6c-8101-5ea83c4ef0bc | -1.20564 | -49.10734 | 2025-10-03 00:54:00 | TERRA_M-M | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 6848978b-d54c-30c5-90b6-370cf5d2e99f | -4.65814 | -45.78437 | 2025-10-03 00:54:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 553.6 |
| 71ae9cbd-5ef5-3c09-97eb-8d72f3327bca | -1.07751 | -53.68667 | 2025-10-03 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1f8c1397-8638-3e48-9a36-fc65cdb7964a | -5.63384 | -43.90649 | 2025-10-03 00:54:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 389.2 |
| 96f6f11e-f703-3c41-a290-007c653d555b | -2.24782 | -47.89416 | 2025-10-03 00:54:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 6dd3d133-8b32-366b-ad56-2e7d323628d5 | -5.37285 | -47.23144 | 2025-10-03 00:54:00 | TERRA_M-M | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 26.6 |
| fd4a1c30-64e6-35ed-a83d-a8d2d28eb130 | -6.52242 | -49.57492 | 2025-10-03 00:54:00 | TERRA_M-M | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| f730ba1a-fd5f-3b1c-af13-2ee2b651b4cb | -5.38644 | -47.22923 | 2025-10-03 00:54:00 | TERRA_M-M | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 7517f13f-90d9-3057-8c48-0ec00379b667 | -4.57469 | -46.51189 | 2025-10-03 00:54:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 28.9 |
| d6d7627d-7140-3a1c-972a-e26ebfd21683 | -10.9291 | -51.0866 | 2025-10-03 01:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 99bf3f17-1376-37d3-b430-387bfffe46d4 | -12.6327 | -46.9471 | 2025-10-03 01:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| c41e3634-c58d-3cb2-a05f-2e99a165a63b | -9.8991 | -43.7237 | 2025-10-03 01:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 68.7 |
| 82428729-1bd5-3205-8f21-52e969e4be6a | -5.655 | -43.9013 | 2025-10-03 01:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| f9f5128f-e06a-33e4-8b76-3b91bf004c9f | -14.7083 | -43.8869 | 2025-10-03 01:00:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 79.2 |
| 916f0e4f-0d1f-3e67-a24d-00ee2e0b308f | -4.6877 | -45.8056 | 2025-10-03 01:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 55.8 |


[Clique aqui para ver as próximas entradas](README10.md)
