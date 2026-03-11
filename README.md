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
| 9860b3c6-971b-3b2e-8511-20533506f646 | 2.7084 | -60.3919 | 2026-03-11 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 3ed42bd1-771e-3037-acaf-cd90e2bd1c08 | 2.7085 | -60.3539 | 2026-03-11 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 9c8c42d8-c89c-3eb8-a51d-2c2e90d8de86 | 2.7085 | -60.3729 | 2026-03-11 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 94.6 |
| e544c5b1-ef11-3b48-ae69-c14107669ab0 | -23.82956 | -52.9248 | 2026-03-11 00:01:00 | TERRA_M-M | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 38.8 |
| 69ddab05-2707-3f71-9273-d77c58f64f4c | -15.24022 | -42.58808 | 2026-03-11 00:03:00 | TERRA_M-M | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 9969601e-0a72-3047-ae26-cabc02cad926 | -17.11542 | -39.50716 | 2026-03-11 00:03:00 | TERRA_M-M | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| e07ef9e1-66cc-3170-8abc-ac29a3417605 | -15.75854 | -41.41444 | 2026-03-11 00:03:00 | TERRA_M-M | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.3 |
| 2865418f-9afa-3b3b-8f03-6efd9b1b144e | -17.11309 | -39.51504 | 2026-03-11 00:03:00 | TERRA_M-M | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| efeb8980-48a9-309f-8ec1-339b68ba3542 | -15.76008 | -41.42471 | 2026-03-11 00:03:00 | TERRA_M-M | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 066389bf-f87e-3dbc-a429-e18b723adc5e | -12.79044 | -44.8301 | 2026-03-11 00:05:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cc28a9c1-cbff-38f6-b2e0-41e219290794 | -10.62919 | -37.0624 | 2026-03-11 00:05:00 | TERRA_M-M | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 19.7 |
| d21740b5-0bbb-3706-8a26-6d6097dbcca0 | -12.40104 | -48.9822 | 2026-03-11 00:05:00 | TERRA_M-M | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 29.7 |
| eb1b106d-d77d-36c0-bf08-330fc798b783 | -12.40279 | -48.99642 | 2026-03-11 00:05:00 | TERRA_M-M | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 2404375c-6e11-30fe-a923-dd6913d404c9 | 2.7084 | -60.3919 | 2026-03-11 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 1020f392-33a8-34bc-9fb3-16c6d5ac9a0b | 2.7085 | -60.3729 | 2026-03-11 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 92.4 |
| addf8c96-0d70-328d-90bf-37d15bf238ab | 2.7085 | -60.3539 | 2026-03-11 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 53d660a3-6c46-3528-ba91-abea4fda0470 | 2.7084 | -60.3919 | 2026-03-11 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 77.8 |
| bd0a21fd-8dce-3b43-a7f3-c7c98b85f198 | 2.7085 | -60.3729 | 2026-03-11 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 87.0 |
| ae105e7c-50a3-3f41-b021-353337d8b9e5 | -23.8137 | -52.9186 | 2026-03-11 00:30:00 | GOES-19 | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 84.7 |
| 6d23b17f-1065-3f60-b4aa-57aa073c2040 | 2.7084 | -60.3919 | 2026-03-11 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 75.2 |
| e33f5355-1bfc-3d8b-a98c-50a4f5b768ba | 2.7085 | -60.3539 | 2026-03-11 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 59.4 |
| e22084df-24d1-3e78-ac50-abf250941767 | 2.7085 | -60.3729 | 2026-03-11 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 6ece20cd-cef4-3096-8bf9-2145e96bc2c8 | 2.7085 | -60.3539 | 2026-03-11 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 3ffb7690-4ec9-3004-8d88-bb77cc179dd1 | 2.7084 | -60.3919 | 2026-03-11 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 80.2 |
| a2e82974-22c6-36a1-adee-bd5737aa0b97 | 2.7085 | -60.3729 | 2026-03-11 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 92.1 |
| d08dab2b-0878-3ef2-99c2-8c6054fff311 | 2.7084 | -60.3919 | 2026-03-11 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 0056e4be-5cbc-3094-8309-8fde80f24d25 | 2.7085 | -60.3539 | 2026-03-11 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 89ada615-c5c9-3585-af63-88f185fd143e | -23.8348 | -52.9141 | 2026-03-11 00:50:00 | GOES-19 | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 102.6 |
| 9286b4af-09e8-3308-a17e-e889460142aa | -23.8137 | -52.9186 | 2026-03-11 00:50:00 | GOES-19 | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 111.4 |
| 437513ab-4d50-3829-833d-e3be8ca143f5 | 2.7085 | -60.3729 | 2026-03-11 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 87640014-4f9c-38c9-b954-73d12fbab7c2 | 2.7084 | -60.3919 | 2026-03-11 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 1b2b15f5-9af9-3744-af4a-df1365763bbe | -23.8348 | -52.9141 | 2026-03-11 01:00:00 | GOES-19 | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 88.1 |
| 04050bcf-b5a3-38d5-bbe0-837ec0588a88 | 2.7085 | -60.3729 | 2026-03-11 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 77d92704-6536-3675-9176-6c39b16f615c | -23.8137 | -52.9186 | 2026-03-11 01:00:00 | GOES-19 | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 85.5 |
| 71a8c008-a2f8-3557-bce5-118c45e4a611 | 2.7085 | -60.3729 | 2026-03-11 01:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 42f9c2ee-ade1-3554-98fb-99dfe035860f | -23.8137 | -52.9186 | 2026-03-11 01:10:00 | GOES-19 | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 100.3 |
| 1ed071fe-1b4c-381b-bfbb-5ec20a76138f | 2.7084 | -60.3919 | 2026-03-11 01:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 8e75e2f6-71f8-3df3-aaea-a22533f0c98b | -23.8348 | -52.9141 | 2026-03-11 01:10:00 | GOES-19 | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 86.4 |
| 011678e5-a9f0-3d77-8ba4-0fd6c85bdd17 | 2.7084 | -60.3919 | 2026-03-11 01:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 48c1e8e2-d5a1-367e-99fc-955e702cda25 | 2.7085 | -60.3729 | 2026-03-11 01:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 9724b0b3-abae-3e19-a062-eb2cea36fb07 | -23.812201 | -52.915199 | 2026-03-11 01:21:00 | METOP-B | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| aedd6321-451d-35c7-9ce1-db8b84da77eb | -23.821699 | -52.9119 | 2026-03-11 01:21:00 | METOP-B | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4ce349fd-aa92-3eca-95d9-0e0f07b3d610 | 2.7102 | -60.341 | 2026-03-11 01:21:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a93d4126-eeaf-3646-a031-00be424711b8 | 2.7021 | -60.377499 | 2026-03-11 01:21:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7a36f0a9-4949-313c-b3a7-e08aac8c437e | 2.7062 | -60.359299 | 2026-03-11 01:21:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e681ce63-5095-3d9f-853a-632528a10db8 | 2.7159 | -60.361401 | 2026-03-11 01:21:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5e3e9368-fd85-35df-a0a1-71faaad0612a | 2.7119 | -60.379601 | 2026-03-11 01:21:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 4d6534b6-7305-390e-921c-113908109677 | -23.806299 | -52.894402 | 2026-03-11 01:21:00 | METOP-B | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f7168277-c431-3e65-bd84-ca81ce020baf | 2.7085 | -60.3729 | 2026-03-11 01:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 09a7ddce-5450-38dd-a06c-f9378f8f44d0 | 2.7084 | -60.3919 | 2026-03-11 01:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 74afafb9-9d64-3526-bf4e-7bec167d97fc | 2.7085 | -60.3539 | 2026-03-11 01:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 60.6 |
| ac280c8e-dabd-3742-93ec-cc1c9ea3140a | 2.7085 | -60.3729 | 2026-03-11 01:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 85.7 |
| b900a7e8-808f-3f30-8f51-3b944c4b5924 | 2.7084 | -60.3919 | 2026-03-11 01:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 4238bc12-a247-3ba1-814a-39fda59799f7 | 2.7085 | -60.3729 | 2026-03-11 01:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 99869d76-f3d5-3026-a774-b6d2aa4abccf | 2.7084 | -60.3919 | 2026-03-11 01:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 21843044-5ff5-3458-8e8e-eb9498311b38 | 2.7085 | -60.3539 | 2026-03-11 01:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 75.9 |
| a5dbdd0d-8cc7-3d3c-9659-40e774c92463 | 2.7085 | -60.3539 | 2026-03-11 02:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 67.6 |
| ac2b229d-abf2-3f02-a12e-5bc20e8f59dc | 2.7085 | -60.3729 | 2026-03-11 02:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 7085b1f0-6425-3378-959a-a3b1c5ceb1f2 | 2.7084 | -60.3919 | 2026-03-11 02:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 77.8 |
| c037df36-b680-3c8d-9537-410b6246ea09 | 2.7084 | -60.3919 | 2026-03-11 02:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 99b8349b-adf6-31b8-a934-eeb60dfc0d4f | 2.7085 | -60.3729 | 2026-03-11 02:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 1eb3b79a-cb6d-3e44-a0fb-43213f2cd300 | 2.7085 | -60.3729 | 2026-03-11 02:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 621451f0-f2f0-351e-a567-21da00a7e84c | 2.7084 | -60.3919 | 2026-03-11 02:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 69.5 |
| e7e8bf4b-7399-368e-a6dd-e8e7c7d17163 | 2.7085 | -60.3729 | 2026-03-11 02:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 06265c7c-afcd-3d88-a071-12e753fd86e7 | 2.7084 | -60.3919 | 2026-03-11 02:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 64.2 |
| ac2ba2d6-b1d6-363b-8959-f2ded223c314 | 2.7084 | -60.3919 | 2026-03-11 02:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 1aa9be03-2f74-3b89-ad6d-b02a1c747337 | 2.7085 | -60.3539 | 2026-03-11 02:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 61.2 |
| fa9b769b-8a9f-3800-bb39-9600b628063a | 2.7085 | -60.3729 | 2026-03-11 02:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 9876e7e3-f908-37eb-a57d-12812ec2e6fd | 2.7084 | -60.3919 | 2026-03-11 02:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 6c2bb68b-829d-35a8-b5fe-acc543a2fc99 | 2.7085 | -60.3729 | 2026-03-11 02:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 84.0 |
| ce0aeb67-82dd-3df0-96d4-fef2f0055228 | 2.7084 | -60.3919 | 2026-03-11 03:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 02785058-cef2-3ae3-a654-f63fcfe0c401 | 2.7085 | -60.3729 | 2026-03-11 03:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 5e065e91-1f01-3b46-b9ce-d6cbd2972c29 | 2.7084 | -60.3919 | 2026-03-11 03:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 79.7 |
| fb2b91d0-9efe-3b62-b8c8-46af918e3490 | 2.7085 | -60.3729 | 2026-03-11 03:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 86.4 |
| e9fda547-98ea-36d4-9fba-4205a366fb73 | -8.19256 | -36.03598 | 2026-03-11 03:15:00 | NOAA-20 | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 1fce4f3f-5238-3387-ad99-8e30d816bd4f | 2.7084 | -60.3919 | 2026-03-11 03:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 067ff57d-e4e7-3b2f-953f-32e321919b8b | 2.7085 | -60.3729 | 2026-03-11 03:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 474014dd-e1ce-39d9-bcaa-5cd2c775d9ef | 2.7085 | -60.3729 | 2026-03-11 03:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 52ba6d6d-6e6d-39fd-a5f6-61f9a76e6fb8 | 2.7084 | -60.3919 | 2026-03-11 03:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 59.5 |
| a9e57ba2-00c1-30fe-82c7-4d4c99239524 | 2.7085 | -60.3539 | 2026-03-11 03:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 027ef88d-c45f-371c-ae69-6928ecb8b806 | 2.7085 | -60.3729 | 2026-03-11 03:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 977a4871-466f-36be-ab9f-f28077ac932b | 2.7084 | -60.3919 | 2026-03-11 03:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 44ff1d40-c725-3d71-acb7-b553489065bc | 2.6902 | -60.3921 | 2026-03-11 03:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 47.7 |
| a957b7b2-6f80-33d5-93f1-42ed7f4eba95 | 4.0581 | -61.3528 | 2026-03-11 03:50:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 45.2 |
| aea3533c-2fa4-3f6d-84a4-9b6008f2453a | 2.6902 | -60.3731 | 2026-03-11 03:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 51.6 |
| fd3758b3-3d2d-32b8-999f-03c295efa1eb | 2.7085 | -60.3729 | 2026-03-11 03:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 15493205-3d4a-3027-bf82-e4f09329f3fb | 4.0398 | -61.3532 | 2026-03-11 03:50:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 5b785e41-0251-3ff0-a320-0d737257ea1c | 2.7085 | -60.3539 | 2026-03-11 03:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 5200f725-62af-3cfd-aa23-005f04e89e27 | 2.7084 | -60.3919 | 2026-03-11 03:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 53f96af4-479c-36e7-8162-d66a650639e3 | -9.29881 | -38.51189 | 2026-03-11 04:02:00 | NOAA-21 | GLÓRIA | BAHIA | Brasil | 2911402 | 29 | 33 | nan | nan | nan | Caatinga | 0.0 |
| b1aa60d6-d4b7-3e2b-83b1-7b5f3da2bbc1 | -6.51623 | -40.4803 | 2026-03-11 04:02:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 0.1 |
| 819439a9-4e56-31a9-8e9c-421ef7a8536e | -6.89406 | -45.57064 | 2026-03-11 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6daf1576-e6e7-321c-bc5a-327ec1324b4a | -8.52186 | -36.1867 | 2026-03-11 04:02:00 | NOAA-21 | ALTINHO | PERNAMBUCO | Brasil | 2600807 | 26 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 480ca5cb-7b7b-303b-8dad-4201caddf3a5 | -8.19573 | -36.03392 | 2026-03-11 04:02:00 | NOAA-21 | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 062270b9-66df-3361-b3df-66239b817c32 | -9.16113 | -40.08244 | 2026-03-11 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bcdf935e-d791-3ce6-a572-c5ea3cef4638 | -8.52504 | -39.00747 | 2026-03-11 04:02:00 | NOAA-21 | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 0.2 |
| a15c3dd1-8591-3025-a0b9-879ba74755e5 | -6.55147 | -42.0026 | 2026-03-11 04:02:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 0.1 |
| 2ae28425-3c27-367a-a3be-a0a1c4c40694 | -9.86257 | -36.64722 | 2026-03-11 04:02:00 | NOAA-21 | FEIRA GRANDE | ALAGOAS | Brasil | 2702603 | 27 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 91703d8c-c555-3ede-a366-a1f998eff32e | -6.423 | -43.74551 | 2026-03-11 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a9eee9c-539c-3256-9ff9-0d9666e4f847 | -7.54648 | -35.84005 | 2026-03-11 04:02:00 | NOAA-21 | GADO BRAVO | PARAÍBA | Brasil | 2506251 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README2.md)
