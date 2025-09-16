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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6bc6420-fcf8-3dcc-84b2-57c35f9ddd50 | -16.51882 | -43.55171 | 2025-09-16 04:32:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5de3bacd-0234-3996-9a18-99a5063d1d79 | -15.80932 | -53.46244 | 2025-09-16 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2cac2bdc-81b3-3923-a4cb-391ee9ecc41d | -15.99664 | -59.44077 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47980501-c204-3946-9495-93e448d7cbd6 | -18.61259 | -48.20388 | 2025-09-16 04:32:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 78e5715f-854e-30a5-8692-bb2dfbabf504 | -18.01046 | -43.93338 | 2025-09-16 04:32:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| adc290ee-8ad5-31ee-8a9d-4321930bb0e0 | -14.80763 | -51.66776 | 2025-09-16 04:32:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d3598986-197d-3c7b-a57b-c0d77e59dd90 | -16.78539 | -40.94516 | 2025-09-16 04:32:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5a5a4bb9-1a27-3d57-9b6e-5bacdc975350 | -16.05097 | -59.43358 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 70e05da1-d699-3f83-9bb6-49fe64c69ff9 | -14.61859 | -46.374 | 2025-09-16 04:32:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46ec0147-6e4b-3f6b-9949-61aaa303c729 | -16.02964 | -59.45761 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8111ebf7-b956-3a32-bc5e-6691e4b4574e | -18.61202 | -48.20758 | 2025-09-16 04:32:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 047a2004-0941-347d-9692-c2ff37f27b0e | -17.82959 | -50.42387 | 2025-09-16 04:32:00 | NPP-375D | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 975c8c1a-af24-3ed4-98ba-550accbb78fe | -18.86516 | -43.35291 | 2025-09-16 04:32:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| dc1149f5-a8e2-3af8-9f9b-cb78693812b9 | -15.98873 | -47.95119 | 2025-09-16 04:32:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e94b2e0-6f65-3830-a254-8179b43e90fd | -17.86648 | -44.44085 | 2025-09-16 04:32:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b2e1c763-285a-3d77-abf1-83d6e0caac80 | -14.52042 | -47.33643 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51055da4-70ab-3212-a28d-bd20428bc4b8 | -14.35819 | -52.92179 | 2025-09-16 04:32:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d620ae9a-1233-34ea-959b-d9a6bccf5b80 | -18.77612 | -47.63538 | 2025-09-16 04:32:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9064cb5-c4ea-31a6-a1d4-cd4fd80746f4 | -15.91866 | -56.27356 | 2025-09-16 04:32:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 0cee6e8e-f380-3f9e-b1c4-4310afc66e8f | -15.99855 | -59.43166 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19419c39-6233-3c24-8f18-55723c7c141f | -14.62203 | -46.32752 | 2025-09-16 04:32:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9c3b3a3-cdd7-360d-9190-d564be865faf | -20.86499 | -46.21309 | 2025-09-16 04:32:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a8fa08c4-afd0-3d4c-a6bd-3a83a2e895c5 | -14.962 | -46.56887 | 2025-09-16 04:32:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68d58ab6-6a9d-32f2-9974-7ba837ee1424 | -15.99889 | -59.25787 | 2025-09-16 04:32:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7101c44c-489e-3c79-8b18-9fa267eebfc5 | -17.08093 | -45.83331 | 2025-09-16 04:32:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 39.6 |
| e369b791-aef9-3f60-91e2-13674508151e | -14.92573 | -51.65598 | 2025-09-16 04:32:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cfe16ad6-c556-3116-b58d-9ebbd55256c2 | -15.80234 | -53.45547 | 2025-09-16 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 610b2c58-cf11-3620-92af-d2d83697752e | -16.03657 | -59.44401 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c3ec6f7-a187-335d-bc78-5b560770174b | -16.69595 | -49.77651 | 2025-09-16 04:32:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2123a1d8-00d1-3ea6-968d-dea6d42a8bda | -14.52597 | -47.34484 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5c6d6028-b090-3ea8-93cb-adec28839679 | -16.59406 | -42.90621 | 2025-09-16 04:32:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 469102fc-a1fa-3f0b-974e-fa5febc3cd3a | -15.41893 | -47.34944 | 2025-09-16 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d6644505-968e-3a8e-b99c-d6bf1a62f5c5 | -20.96603 | -44.50195 | 2025-09-16 04:32:00 | NPP-375D | SÃO TIAGO | MINAS GERAIS | Brasil | 3165008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 67b7142d-70a9-37ad-928e-c2571ca68063 | -15.78748 | -53.43932 | 2025-09-16 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a41985b8-6c63-3aad-86a4-8589481e7563 | -17.32995 | -46.79688 | 2025-09-16 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf6cc025-759a-3390-88a6-97cfd58ec622 | -17.60793 | -46.68627 | 2025-09-16 04:32:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e9e3acdf-74da-381c-8818-4fb6460f949c | -21.26449 | -47.01218 | 2025-09-16 04:32:00 | NPP-375D | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80b26f6b-cfb5-35b3-973f-bf5810751ac0 | -15.87652 | -59.41113 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53bf2d9f-6ba3-3d29-a5de-fb56e49d308c | -14.27402 | -46.14297 | 2025-09-16 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0d31cbf-91ed-3bf4-b758-ed6ba558f867 | -15.86836 | -59.3922 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6984d408-01d4-39b7-9a05-e8652822c45f | -16.06356 | -59.43155 | 2025-09-16 04:32:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 35331cc4-577c-3404-935b-572d84ec7c13 | -18.90467 | -49.57704 | 2025-09-16 04:32:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1e1e72bd-f617-3941-b7e2-0aaacd001d8c | -19.84426 | -46.45367 | 2025-09-16 04:32:00 | NPP-375D | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 62b86b85-484e-3f28-926b-481b92a61c2f | -14.81054 | -51.67285 | 2025-09-16 04:32:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43efbff3-4dc3-3e08-b364-ed193a73705a | -14.51529 | -47.39149 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b0c3fd3-05b3-3045-8d70-8c3ed8529985 | -14.8187 | -51.66349 | 2025-09-16 04:32:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75ec2237-0c9f-3a02-be19-89fafce58cda | -14.60037 | -46.37867 | 2025-09-16 04:32:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31fa16cf-cf3c-3b29-a372-c9ea66702f01 | -14.53823 | -47.35428 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e548a6fe-dad4-3185-a5ee-8bd3308a2914 | -19.84485 | -46.44949 | 2025-09-16 04:32:00 | NPP-375D | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0606cc23-ffe1-3018-aaa0-cd5483c238c9 | -15.77166 | -53.45849 | 2025-09-16 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 44e20146-423f-3c9d-8d46-7f91d16e56af | -14.45625 | -47.2851 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31ca651c-2776-385c-8b80-2bc41797e67a | -19.19284 | -47.20057 | 2025-09-16 04:32:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a08411a7-b9b6-3c42-bc1b-d26c4d8fb46f | -15.40941 | -47.34417 | 2025-09-16 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 800012a5-62e5-39ad-af09-338bfb703353 | -15.87331 | -59.39756 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c0861c52-8a0f-3ab6-9b0c-e0c78804fd40 | -16.04243 | -59.44507 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49060b8a-07bc-3144-a4c7-6dff794723a6 | -15.78657 | -53.4444 | 2025-09-16 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b635b217-fb54-3928-9a30-6352fec15da3 | -15.82732 | -53.47705 | 2025-09-16 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dbb6e803-2161-3eb2-bd6a-fa3c9846b716 | -17.73179 | -46.76975 | 2025-09-16 04:32:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1b0c6f1-d35e-3351-bf3a-1795c8defb01 | -18.86937 | -43.3535 | 2025-09-16 04:32:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 8f52d750-6d0d-337d-bf5a-e68ab88abc6a | -16.5148 | -43.55113 | 2025-09-16 04:32:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 66517056-0100-3224-b99c-75db8cad4273 | -15.80461 | -53.45906 | 2025-09-16 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3a09c5d9-8f1a-3417-8eeb-e55a27772e01 | -15.8133 | -53.46328 | 2025-09-16 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a491c43a-f27a-3508-81da-47cbb74779f3 | -16.70488 | -54.9749 | 2025-09-16 04:32:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 99930d8d-a996-3509-ae9f-4ef2ed21fbdf | -14.80397 | -51.66708 | 2025-09-16 04:32:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 820493b7-33e7-3251-bba4-c8d26d72c04b | -16.02287 | -59.46087 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e06dec04-bdc9-35b2-be27-9135fe34a6d6 | -14.61292 | -46.38848 | 2025-09-16 04:32:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d6b07859-6f9a-37c6-8af0-cc145790ec21 | -14.80838 | -51.66335 | 2025-09-16 04:32:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fc1027bb-9f84-3293-bcf3-c98066814e78 | -16.01306 | -59.24776 | 2025-09-16 04:32:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67d1120d-d358-37b0-baa7-82d7a65b0ae4 | -15.40886 | -47.34781 | 2025-09-16 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bc7e3166-cc7b-3f6b-99be-642a0f2460ee | -16.43938 | -49.5886 | 2025-09-16 04:32:00 | NPP-375D | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dbfb3f5b-a540-3023-bb76-a2f2c96851ba | -15.80449 | -53.4887 | 2025-09-16 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6cc7c7d0-4b05-35ea-8247-092be5703352 | -17.08033 | -45.83748 | 2025-09-16 04:32:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 4e70ecf9-17aa-3cc9-aefe-6bed03512193 | -16.87195 | -49.35827 | 2025-09-16 04:32:00 | NPP-375D | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee5dc628-360b-3688-88b1-41c0b10113fc | -14.52866 | -47.39364 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 89e2aa40-4aee-3b58-8243-a47650ac19d1 | -15.40997 | -47.34048 | 2025-09-16 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 930bc2d9-d4a8-3e93-8ebd-994eb22c8ee4 | -18.17293 | -45.19589 | 2025-09-16 04:32:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25cb5e11-55e2-3017-9d59-229abd4fda57 | -18.97771 | -46.68042 | 2025-09-16 04:32:00 | NPP-375D | CRUZEIRO DA FORTALEZA | MINAS GERAIS | Brasil | 3120706 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8cdd96cc-6645-33af-932f-74f2f4c7dfdd | -14.83258 | -51.67057 | 2025-09-16 04:32:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c5842f9-d75d-3d7f-acaa-2d1f40a62fd8 | -16.53071 | -43.73795 | 2025-09-16 04:32:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 191de54d-177c-3dee-aa6e-b3c49ff4de94 | -13.61764 | -47.6424 | 2025-09-16 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01276c21-a4a0-39a3-a70c-6b13a2b23a9b | -16.13177 | -42.3312 | 2025-09-16 04:32:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2a6a12c6-6444-37d8-a63c-10e9004e101c | -18.01447 | -43.93395 | 2025-09-16 04:32:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f2c0d432-d79b-3453-a55e-505726b7cd7f | -21.26804 | -47.01273 | 2025-09-16 04:32:00 | NPP-375D | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a74e69d-119d-3db2-9ab5-bffd9601c9a1 | -16.69794 | -54.96395 | 2025-09-16 04:32:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7008034a-d337-3099-92d2-5969f4ec37f7 | -16.87253 | -49.35464 | 2025-09-16 04:32:00 | NPP-375D | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 48bb48c3-7d22-34a8-b4b3-beef8fc5f93e | -15.78119 | -47.72852 | 2025-09-16 04:32:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0768913-b25d-33a0-a787-00e859d65daf | -20.86172 | -46.21452 | 2025-09-16 04:32:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 45aa0e44-d883-3bb4-b93b-acc8a1d4a8bb | -19.15998 | -48.72931 | 2025-09-16 04:32:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 30ff080a-ec58-3caf-a643-401dcf440eb3 | -17.72774 | -46.77317 | 2025-09-16 04:32:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 78b3e544-83eb-368b-a5c7-9f19e96be7e4 | -14.47479 | -46.35965 | 2025-09-16 04:32:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ec66026b-8980-3409-928d-af9b20e64577 | -14.80616 | -51.67027 | 2025-09-16 04:32:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 971ff1e9-a96c-33e7-9a0a-6180fbda2377 | -14.53312 | -47.38703 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 43b26ae2-500d-372f-b0f8-b38cae8febd0 | -17.23639 | -43.42752 | 2025-09-16 04:32:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b05c0b5c-3693-32f6-97f7-037cceb1ad89 | -15.41222 | -47.34837 | 2025-09-16 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 21e137fd-6052-389d-864e-615e2e772017 | -16.04339 | -59.44057 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7085d8c-797a-3568-8eb2-1cdd3b4a51aa | -18.55366 | -49.25386 | 2025-09-16 04:32:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.6 |
| 19007b6b-3c1b-3c5a-bf4a-7d0cafd11dba | -14.80983 | -51.67094 | 2025-09-16 04:32:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 40e94c2a-1d08-3487-be26-b6b745f945bf | -14.50872 | -47.32333 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd57b08f-c77c-3c0c-913c-5f8efd93f5fb | -14.60951 | -46.38789 | 2025-09-16 04:32:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86d1232f-4e86-3e7e-af33-8ae2cd1348b5 | -14.34522 | -47.09278 | 2025-09-16 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README57.md)
