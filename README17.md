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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9d057f7-970f-3733-914b-f0d7bcbee88a | -6.87889 | -43.59828 | 2024-10-03 00:30:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4fc2ecb1-aafc-36bb-95f1-4273779e86cd | -6.87096 | -43.60939 | 2024-10-03 00:30:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 7ecbe43b-3852-3429-826d-3ac8e2f58ce7 | -6.65889 | -43.13821 | 2024-10-03 00:30:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 89997015-4032-37e8-b10b-cf0b23f55d2f | -6.63739 | -42.10866 | 2024-10-03 00:30:00 | TERRA_M-M | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| a7e46647-1cfd-3724-8bfc-53500396a8d6 | -6.60338 | -43.00026 | 2024-10-03 00:30:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ca6328ea-d60f-3ec8-ab71-721927ac5893 | -10.24581 | -47.68809 | 2024-10-03 00:30:00 | TERRA_M-M | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| a7d3b340-91c1-3937-a018-22160589a46e | -10.47482 | -48.18581 | 2024-10-03 00:30:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 884056fe-2365-3ca7-aff7-293812f376a4 | -10.56665 | -48.07589 | 2024-10-03 00:30:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 47.1 |
| ad48282d-c845-3ab4-ab45-ef99b992f7e9 | -10.56847 | -48.0203 | 2024-10-03 00:30:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 1ea60f67-7b12-3116-bafc-942f6392c769 | -10.56948 | -48.09929 | 2024-10-03 00:30:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 5f317560-eb2b-3111-b555-846ee06fa822 | -10.60404 | -48.08937 | 2024-10-03 00:30:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 87f20348-90c6-3853-9193-d6fa5076295f | -10.71786 | -47.70775 | 2024-10-03 00:30:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| d23e71b9-830c-34f7-9287-f6acc55216c3 | -10.72574 | -46.2084 | 2024-10-03 00:30:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 9c99a594-dd4e-3a1f-ab14-1c7d7748c849 | -10.74652 | -47.98676 | 2024-10-03 00:30:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 0af03e87-57e2-33d4-9014-06657d1ebf1b | -10.75243 | -47.99074 | 2024-10-03 00:30:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| f162a878-b36d-3590-87fe-c5513ef68e60 | -10.7236 | -46.19161 | 2024-10-03 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 44e1a5e1-1c8e-3605-bbb2-2ea643bb3a74 | -10.72149 | -46.17505 | 2024-10-03 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 39.0 |
| d1ac1180-6d05-3b3c-b330-2891084494d5 | -10.70775 | -46.16045 | 2024-10-03 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| a2612a63-cc9a-31ef-b284-246c647b91fc | -10.70571 | -46.14433 | 2024-10-03 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 732c72d1-c39b-3e5e-9bf0-155b281c58bd | -10.69401 | -46.14569 | 2024-10-03 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.2 |
| b9cfa686-25ff-39bf-bcd0-a5095e7388fa | -10.692 | -46.12967 | 2024-10-03 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 76168ff1-1299-3200-a6c7-6c3461c38139 | -8.85405 | -48.93613 | 2024-10-03 00:30:00 | TERRA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 08013d56-a3e2-3126-93c1-01336295ae44 | -8.85025 | -48.94188 | 2024-10-03 00:30:00 | TERRA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| be8836fd-af09-3cb6-9cea-b25c016abc38 | -8.72746 | -47.10278 | 2024-10-03 00:30:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| f1da7316-b881-36db-928c-ae7d183bafc6 | -8.5213 | -50.99356 | 2024-10-03 00:30:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 2d693619-e06d-3915-a413-21e60445cda5 | -8.43803 | -46.31818 | 2024-10-03 00:30:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| d6f5ad0c-5f07-397b-90ac-0520afed3527 | -8.43603 | -46.30286 | 2024-10-03 00:30:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| b561db61-805e-3d3a-9de9-6207cea2367a | -8.43451 | -46.38053 | 2024-10-03 00:30:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 89f0b623-29d4-3767-950e-c9d410d1f520 | -8.42304 | -46.38202 | 2024-10-03 00:30:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 66474ad0-da61-3ba1-b9a2-70f8bef9a368 | -8.23865 | -49.76691 | 2024-10-03 00:30:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| ed416aa4-626f-3390-b1dd-be3ccecfaab6 | -8.18133 | -50.50291 | 2024-10-03 00:30:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| ad5725e0-5e87-3772-a550-4bd88c03d1b3 | -7.85773 | -46.26225 | 2024-10-03 00:30:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 8ce48556-1dbc-33ac-a5f0-4e0a6527e45c | -5.40238 | -43.10731 | 2024-10-03 00:33:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| aea36284-9c97-37a7-a376-68d18f61d77f | -6.9692 | -49.43189 | 2024-10-03 00:33:00 | TERRA_M-M | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 51cf1f1b-56ae-309a-aab9-6654c2920b03 | -6.35322 | -46.50393 | 2024-10-03 00:33:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 3cfce84a-994e-34dc-94ef-525e6af24f1b | -6.27878 | -46.98646 | 2024-10-03 00:33:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 7130fadf-403f-3a39-a2a8-1ba1c34dd885 | -6.26763 | -44.73265 | 2024-10-03 00:33:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| c7eaeee0-3fc8-3f34-99e6-980814681d20 | -6.14841 | -44.13375 | 2024-10-03 00:33:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 4510449b-8d96-37ac-b6f2-2c01573623a4 | -6.14387 | -44.1406 | 2024-10-03 00:33:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 92567c5d-ce2c-3fea-9841-6b289a368083 | -6.14246 | -44.13035 | 2024-10-03 00:33:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| d4d57ba7-b8aa-3b28-8c84-20f185f7f0fe | -6.13179 | -47.26655 | 2024-10-03 00:33:00 | TERRA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 6f2f751a-b611-3c87-afdd-2e8aa8eb596a | -6.12249 | -44.94659 | 2024-10-03 00:33:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| fc30fee5-6c66-38be-bd15-49b821b1f641 | -6.12207 | -47.28484 | 2024-10-03 00:33:00 | TERRA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| cc045f57-b864-3ef1-b01e-90863aa80111 | -6.1219 | -44.05083 | 2024-10-03 00:33:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 2630f9db-8f67-3bd9-bd63-b22bfccbb5b4 | -6.12098 | -44.93534 | 2024-10-03 00:33:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 0d82f0ac-0ae5-392d-a357-83d387f8c884 | -6.1205 | -44.0407 | 2024-10-03 00:33:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| fa43bbd0-1c58-3f43-a0f2-e4c6eb4f9a63 | -6.11994 | -47.26822 | 2024-10-03 00:33:00 | TERRA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 7a3d40ce-9f8e-37b0-b33b-3751fed662d9 | -6.11249 | -44.05211 | 2024-10-03 00:33:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 31.5 |
| fe630472-eb96-33c1-9eec-a9f0ac7c5b84 | -6.09364 | -44.05444 | 2024-10-03 00:33:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a82f1742-4456-3cf5-b012-38c247862d84 | -6.02068 | -44.55751 | 2024-10-03 00:33:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 674c531f-654e-3a98-aaec-9c16abee2fc6 | -6.0086 | -44.56554 | 2024-10-03 00:33:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| d7f1afd1-4858-30e2-92bb-e71fa7b265d4 | -6.00714 | -44.55489 | 2024-10-03 00:33:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| c78d35a5-0956-3e70-b280-15eb23e33562 | -5.85417 | -44.61403 | 2024-10-03 00:33:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 220.6 |
| 3120c212-9625-3904-af5d-67eb323ed360 | -5.85274 | -44.60326 | 2024-10-03 00:33:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 369.8 |
| f93b408d-b170-392f-a48f-ab268c271eda | -5.84777 | -46.24092 | 2024-10-03 00:33:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 12ad3f39-8af5-351d-a06f-2e4df9724860 | -5.79568 | -46.45305 | 2024-10-03 00:33:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 8c049859-e6c2-3f6c-9193-0802ad672f24 | -5.50698 | -44.6211 | 2024-10-03 00:33:00 | TERRA_M-M | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 15b0a810-cd4d-3ce9-b96f-4458704c398c | -5.49732 | -44.62235 | 2024-10-03 00:33:00 | TERRA_M-M | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 41ab12b4-b971-300e-b1f5-fd9d44e0db70 | -5.4686 | -47.09851 | 2024-10-03 00:33:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 886dece8-d818-3268-9834-4de92706b516 | -5.46654 | -47.08278 | 2024-10-03 00:33:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| ba422143-476f-32c5-995b-6c3ab21cc82d | -5.35188 | -46.73422 | 2024-10-03 00:33:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 096102c6-3972-340c-9c7c-985274ff3749 | -5.34989 | -46.71934 | 2024-10-03 00:33:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 79a6ba10-d683-3f88-9e8e-fefd724afd9a | -5.242 | -46.76957 | 2024-10-03 00:33:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| de1d620d-7042-3dae-a42e-02298fe41c2c | -5.08569 | -46.11908 | 2024-10-03 00:33:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 1574e31a-ec00-3cbf-b8f0-c6bad104a325 | -5.04435 | -45.81269 | 2024-10-03 00:33:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| db1d5a97-7a51-336b-96b4-dd85d6aa5514 | -4.92466 | -47.14441 | 2024-10-03 00:33:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 17.2 |
| c3785357-9803-36c7-8d14-1573164b7e2c | -4.9226 | -47.12881 | 2024-10-03 00:33:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| f3ea22ed-bee3-3bb8-8311-92ae9f33588e | -4.77748 | -45.95625 | 2024-10-03 00:33:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 54e5661a-9de8-31c3-aa06-55b0ab0c2f2f | -4.75285 | -45.39453 | 2024-10-03 00:33:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| f9432869-41c2-3a65-ac56-d7b55b160bd0 | -4.75192 | -45.3888 | 2024-10-03 00:33:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 497f2bac-0f83-3f18-9806-30ad0c297ef8 | -4.75124 | -45.38292 | 2024-10-03 00:33:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| cedbd3d8-a662-38c0-9fea-342fdfd8a9c8 | -4.68651 | -45.88534 | 2024-10-03 00:33:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f2d8bd50-9a80-3b2f-b76c-845adfd97582 | -4.67785 | -45.89956 | 2024-10-03 00:33:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 98ee14c8-fed9-3d33-a302-8d8f0db234f5 | -4.67616 | -45.88702 | 2024-10-03 00:33:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 36b35935-578d-3ce0-9aad-14f45f669013 | -4.65303 | -47.4421 | 2024-10-03 00:33:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 17.1 |
| f46e78c5-e161-37ee-ba68-f435f346889e | -4.58178 | -48.0189 | 2024-10-03 00:33:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| a5b75dda-bfaa-3b9a-89f3-853ae9171d81 | -4.56949 | -48.02058 | 2024-10-03 00:33:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| ea2fa416-e6ac-3809-8123-13c0345d5407 | -4.56624 | -48.02672 | 2024-10-03 00:33:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| c14bf008-e6aa-38a9-b883-f688ce18096a | -4.56373 | -48.00854 | 2024-10-03 00:33:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 694156cd-707a-36a0-bf4e-5d7e479f04c3 | -4.4903 | -46.39054 | 2024-10-03 00:33:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 91f5815a-5889-3fe3-8467-0ee18c38dfa6 | -4.48964 | -48.11061 | 2024-10-03 00:33:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 56441d13-a47e-335a-aef1-52d8dc5b88b8 | -4.48714 | -48.11752 | 2024-10-03 00:33:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 1b79744e-30a4-37cc-a496-f4966bd64d0a | -4.38314 | -47.48014 | 2024-10-03 00:33:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 62f0df4f-841f-3ba9-a695-8fe2c6f2fbe2 | -4.10853 | -48.49831 | 2024-10-03 00:33:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 1f8a0b9a-fba3-39bd-b314-b80ff692d996 | -4.10593 | -48.47886 | 2024-10-03 00:33:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 9a8a4e07-95cd-3648-8728-467140f4b2aa | -4.10039 | -46.14862 | 2024-10-03 00:33:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 15.8 |
| bd709d31-6c88-30c7-9d3f-f31c888affe7 | -4.09648 | -44.61048 | 2024-10-03 00:33:00 | TERRA_M-M | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2ecd2f04-60a9-3bc0-aaeb-0135ffa57f38 | -4.09585 | -48.50012 | 2024-10-03 00:33:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| e322ad71-e525-3ace-a031-e00065a7c304 | -4.09329 | -48.48073 | 2024-10-03 00:33:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 332967b5-55d4-33f3-a557-2ff7f2f63bf3 | -4.09074 | -48.46143 | 2024-10-03 00:33:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 847fd6bd-f565-323c-ad85-0db6c655cb53 | -3.95474 | -50.99695 | 2024-10-03 00:33:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 5157941d-85ce-3319-ad4f-9e1983161366 | -3.9543 | -51.02068 | 2024-10-03 00:33:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 04ecb92d-4b3d-38ad-9821-d44fd4dc4f1b | -3.93655 | -49.69482 | 2024-10-03 00:33:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| e4397e62-524f-34bd-bfdc-92a944e7ff72 | -3.81003 | -47.81848 | 2024-10-03 00:33:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 82188ef6-bd2d-3b6f-af51-716dacdb26c9 | -3.80778 | -47.80149 | 2024-10-03 00:33:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 120.5 |
| 95730bd3-0d8e-39fc-a6b8-5ff2d17082fe | -3.80209 | -47.80797 | 2024-10-03 00:33:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| ef4d6e93-71e1-3597-a2a0-19446bcc6331 | -3.79974 | -47.79115 | 2024-10-03 00:33:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 6e13d42d-a9b1-33b1-b7fd-bbbab927c878 | -3.70411 | -47.61959 | 2024-10-03 00:33:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 456330e1-eeb1-3e12-86a2-be9318cbc1eb | -3.60705 | -44.7879 | 2024-10-03 00:33:00 | TERRA_M-M | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| ff6cc44a-edc4-32c1-a45f-d889307cafbf | -3.70195 | -47.60343 | 2024-10-03 00:33:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |


[Clique aqui para ver as próximas entradas](README18.md)
