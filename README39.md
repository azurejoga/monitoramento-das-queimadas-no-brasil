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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 205247e2-d79f-369e-accc-ed18f136e9b4 | -12.5384 | -45.8029 | 2025-09-25 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 343.9 |
| 41f5bd66-2cb2-3602-b073-33c8d5536190 | -17.9312 | -55.8548 | 2025-09-25 12:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.2 |
| 1c1c92bf-db29-332c-9a8f-5b632ab7c614 | -15.8029 | -59.4835 | 2025-09-25 12:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 9be188a7-a120-3e6c-920b-73a6a9ee5a75 | -11.6818 | -44.3844 | 2025-09-25 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 117.2 |
| c0ab1aeb-5e61-3cf4-b187-68425752bb9a | -6.4317 | -43.0942 | 2025-09-25 12:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 0134456a-3b63-3776-a5bb-d0b9d54a4fcf | -6.4319 | -43.0707 | 2025-09-25 12:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| e93bef5f-54e3-3417-b5b3-fefb04958eac | -7.3567 | -44.4496 | 2025-09-25 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| ac0509c6-55a5-352f-a00b-83437e429857 | -8.8415 | -46.2095 | 2025-09-25 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 2cb45ecb-9741-321c-9e22-0838cfe42870 | -12.5388 | -45.7799 | 2025-09-25 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 95a9a237-f703-39c9-ba5c-ace62d42c992 | -11.6622 | -44.4107 | 2025-09-25 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| fd2af150-c2e1-3ddb-afa2-833d3970fa60 | -7.198 | -43.5154 | 2025-09-25 12:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 83.3 |
| f3cf1768-0af3-320c-8c91-0788d74fc619 | -17.9506 | -55.8731 | 2025-09-25 12:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.3 |
| d5318ae1-a9d7-38a7-bb6b-a3755ae115aa | -17.9312 | -55.8548 | 2025-09-25 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.2 |
| 38590fb4-f270-36e0-9fe4-4cd4a63d4518 | -12.5388 | -45.7799 | 2025-09-25 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 207d666e-0b3a-3237-8bbf-96c42c0dae29 | -8.8996 | -46.0909 | 2025-09-25 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 8a578791-841a-3985-a87f-4660843e1e19 | -8.8417 | -46.187 | 2025-09-25 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| e375c3a7-9c03-3ad8-b38e-57346543e9d6 | -11.6814 | -44.4078 | 2025-09-25 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 122.0 |
| db77be3c-88d5-398a-ad92-b199826f71ac | -8.8415 | -46.2095 | 2025-09-25 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 6daa7e65-9f42-3c2e-bb23-591720cafec5 | -12.8676 | -44.6878 | 2025-09-25 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 3e3b025a-f1cc-3040-8281-080cafc94be8 | -17.9506 | -55.8731 | 2025-09-25 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.0 |
| b37e5585-1bf0-3dc7-8c94-f7c353a042b1 | -6.4317 | -43.0942 | 2025-09-25 13:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 3bd73b2f-2e81-3d11-a847-ef99cba59cac | -17.9308 | -55.8758 | 2025-09-25 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 128.8 |
| 997fea4b-2953-37ce-823f-69bf54d349d5 | -6.4129 | -43.0958 | 2025-09-25 13:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 6eca9072-bf0a-36d8-8a45-f7e7cf9ebcb0 | -5.1011 | -42.9871 | 2025-09-25 13:00:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 4703d9fe-359b-30c1-b6da-1ad3af57333e | -15.2819 | -59.4321 | 2025-09-25 13:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 90.0 |
| c9bb74ae-89a2-373e-ac51-d48dd1cb2b5d | -6.4319 | -43.0707 | 2025-09-25 13:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 39c2e6c0-6343-3a3a-9528-35734077e595 | -6.4131 | -43.0724 | 2025-09-25 13:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 918ce68f-0627-3219-80b6-151befb323ce | -11.6457 | -45.3388 | 2025-09-25 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 561e6002-f895-3ad7-9aac-d811335287e1 | -8.8415 | -46.2095 | 2025-09-25 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 172.5 |
| 8996230a-7a76-3c74-9305-1a500891318c | -17.9312 | -55.8548 | 2025-09-25 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.1 |
| 001bd94a-1c32-39d1-b823-8d5cc258f239 | -5.0822 | -43.0118 | 2025-09-25 13:10:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| b36f43b0-714f-3fc7-ac71-35f71d23802c | -7.4621 | -41.9041 | 2025-09-25 13:10:00 | GOES-19 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 92.8 |
| 272e2a8e-5e19-386f-a2c5-80659a466706 | -7.6396 | -46.0131 | 2025-09-25 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| eaec7751-a43f-3429-a6ba-6e69774693ed | -7.3567 | -44.4496 | 2025-09-25 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.1 |
| b7daa1a4-f438-3e3a-9a9e-1658d9bb93b5 | -5.1972 | -42.6984 | 2025-09-25 13:10:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 88.6 |
| a4db50f4-db7e-3c07-a911-77f575c1cfa6 | -12.8676 | -44.6878 | 2025-09-25 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 7d9a7828-cc7f-3df1-970e-a2aabc5213ed | -11.6453 | -45.3619 | 2025-09-25 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| c21f51bf-9ed4-3b77-87c2-3c229dd61d26 | -7.6399 | -45.9907 | 2025-09-25 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| ffa7a70a-4ac7-329d-a48d-d530cf5ae0aa | -6.4319 | -43.0707 | 2025-09-25 13:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 7dc66e94-f1df-3d16-9cec-914ede0b6021 | -5.0824 | -42.9884 | 2025-09-25 13:10:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 57151f56-30e8-366e-997f-1427dc6fc850 | -8.682 | -43.9888 | 2025-09-25 13:10:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 2e7531d3-f1c0-3906-9958-70c0d93d7917 | -6.4129 | -43.0958 | 2025-09-25 13:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 1f31b2e4-3b95-3ec0-95d5-618f958804d4 | -12.8483 | -44.6909 | 2025-09-25 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 030c92f5-85da-3b5a-8050-eeb8bbfdd8bf | -8.6631 | -43.991 | 2025-09-25 13:10:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 85.2 |
| c5a23a59-6796-3449-92dc-83349cd439a1 | -17.9308 | -55.8758 | 2025-09-25 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 149.6 |
| 6ec6e4ed-564e-309f-9f7b-a0377c26ebdb | -11.4425 | -44.9303 | 2025-09-25 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 577e5695-986e-3b6b-86f1-de0cc6ad670c | -17.9506 | -55.8731 | 2025-09-25 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.0 |
| c1b88224-6329-3e64-9959-0a59c8fef09b | -11.4421 | -44.9535 | 2025-09-25 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| df3af467-6f8a-3f19-bd98-8bae76d58917 | -8.8417 | -46.187 | 2025-09-25 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| fe9efecb-74c4-3e2a-8d4b-35b925a27853 | -12.8487 | -44.6675 | 2025-09-25 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 4edc768f-e708-349a-8d41-1c44ab849033 | -6.4131 | -43.0724 | 2025-09-25 13:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 6e15086c-73cf-3b46-944c-21ca1397e1b3 | -12.5388 | -45.7799 | 2025-09-25 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 174.4 |
| 1809678e-e2c0-3e60-92b8-e90319b37ce7 | -11.4233 | -44.9331 | 2025-09-25 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 05d5484f-3051-3394-8f4c-3ecb6b2b885e | -11.6814 | -44.4078 | 2025-09-25 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 176.0 |
| a4f5cbbf-b736-36bb-8401-9ba4b0b43b31 | -6.4317 | -43.0942 | 2025-09-25 13:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 0e10e013-26ea-328f-b571-716fe1ec3454 | -11.6818 | -44.3844 | 2025-09-25 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 153.0 |
| b2b2af83-46d4-3eec-a29b-3d4999a0f198 | -11.6622 | -44.4107 | 2025-09-25 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 6efc8fcd-776d-3384-9e96-778ea229b8b4 | -11.4229 | -44.9563 | 2025-09-25 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| c6de220a-dcb0-333b-9c27-022b7de63b68 | -6.4317 | -43.0942 | 2025-09-25 13:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| db7b69b7-431d-33e5-bbc0-5665721d28ca | -11.4225 | -44.9794 | 2025-09-25 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 124.7 |
| df247497-faaf-3edc-b374-dd826b726a06 | -11.6818 | -44.3844 | 2025-09-25 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 7da8701e-9257-36c5-b247-e4699801971d | -11.6814 | -44.4078 | 2025-09-25 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 205.3 |
| 9d433408-7424-35be-8883-770d9c27356a | -6.4319 | -43.0707 | 2025-09-25 13:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| fa448c1d-bc80-3eb1-ad5b-0072b8359fac | -11.6622 | -44.4107 | 2025-09-25 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 131.5 |
| ffa9ef7f-6d2f-393c-bd10-19155e915887 | -15.8029 | -59.4835 | 2025-09-25 13:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 2932851a-389e-3e7e-89dd-d8093699ce20 | -8.6628 | -44.0142 | 2025-09-25 13:20:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 101.2 |
| a80230d5-3dd4-306d-a735-0ec179f25706 | -17.9308 | -55.8758 | 2025-09-25 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 145.8 |
| fff73886-6530-354f-be6b-25d96fe628d9 | -8.4987 | -44.9998 | 2025-09-25 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 0b1f21a6-fbcb-336a-8875-cc496ca2375f | -8.8415 | -46.2095 | 2025-09-25 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 5c3d31e9-1dd4-30da-8311-c28af92dca91 | -11.6453 | -45.3619 | 2025-09-25 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 53bf27d2-6440-3ed9-a86a-20e8029b7b3f | -8.7384 | -45.4299 | 2025-09-25 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| be6fe48a-9661-3dca-a36c-ce99280578b0 | -5.7963 | -42.7946 | 2025-09-25 13:20:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 72.4 |
| 4c6ecf8b-433b-33f7-ad0a-ff28873aaf43 | -8.6631 | -43.991 | 2025-09-25 13:20:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 103.5 |
| afbaf56c-500f-3779-8a7d-3b73e582012e | -10.8051 | -45.3866 | 2025-09-25 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 42b835ca-71c5-35fc-8f5e-c3f56505ee95 | -11.4229 | -44.9563 | 2025-09-25 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 107.8 |
| d44cd359-767a-3f48-b5f9-0145e157c5b8 | -12.8676 | -44.6878 | 2025-09-25 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 166.0 |
| 2f06ca0e-251b-30e7-84ed-78db6190c9a3 | -12.8483 | -44.6909 | 2025-09-25 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| cc62afe0-8fa8-377d-a601-de8c19c9dc60 | -12.5384 | -45.8029 | 2025-09-25 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 406.8 |
| a6c813bd-c8f8-3a39-b867-931cb781c37a | -12.8487 | -44.6675 | 2025-09-25 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 65cf5dc8-88e3-3e68-b874-cbf5a060eb6a | -7.3567 | -44.4496 | 2025-09-25 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 9b2da540-4b21-348a-af6d-e09d60489c7e | -17.9312 | -55.8548 | 2025-09-25 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.5 |
| d86aade5-ee55-3862-8706-07f3ff39e5f3 | -6.4131 | -43.0724 | 2025-09-25 13:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 76ae0b90-259f-38df-8030-d236815d77df | -11.6457 | -45.3388 | 2025-09-25 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 12d9bcf8-bc00-3b4d-9dd3-4744be25f95b | -12.5388 | -45.7799 | 2025-09-25 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 190.7 |
| 1c2afcb5-3fd0-3363-a082-2bff0fba804f | -17.9506 | -55.8731 | 2025-09-25 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.9 |
| 4e0b2f9d-24f1-3fe7-8625-4f34d4ecb887 | -6.4129 | -43.0958 | 2025-09-25 13:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 0d3b95f1-c882-3a2b-a410-de245205d20c | -6.4131 | -43.0724 | 2025-09-25 13:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| ae8baad1-f390-3fd1-9101-d1ed939a4f76 | -5.0822 | -43.0118 | 2025-09-25 13:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 883944c4-de18-31ad-b913-9d9135ae971c | -6.4319 | -43.0707 | 2025-09-25 13:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 98c0b89b-83cc-3d5a-b4a9-d4761e71dc2b | -11.6818 | -44.3844 | 2025-09-25 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 21088ce4-f03b-337e-8a5b-1bca24e6002f | -8.6631 | -43.991 | 2025-09-25 13:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 185.8 |
| 9880da88-e09e-3e98-98b3-10176cb70d31 | -8.682 | -43.9888 | 2025-09-25 13:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 17cf0ca6-2c95-3e23-a3fd-c0c1a3d91aa2 | -8.6628 | -44.0142 | 2025-09-25 13:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 154.5 |
| da18ebf2-0e3a-35d5-898a-95e9ec7c4540 | -8.8415 | -46.2095 | 2025-09-25 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 727b5523-0d43-37d0-ba94-4fd3e56eb010 | -15.7644 | -59.4672 | 2025-09-25 13:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 40a62f97-5d9f-303b-aacf-bc3a6a7deac7 | -12.5384 | -45.8029 | 2025-09-25 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 248.6 |
| e0d3aa0c-da94-34c7-9cfd-d3ee7c8aeabb | -11.6622 | -44.4107 | 2025-09-25 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 450a1d51-7220-35dd-b105-c4f4c96e4ab8 | -6.4129 | -43.0958 | 2025-09-25 13:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 3ebc33fa-5e5d-394b-95b7-f3c3f66e1502 | -5.0824 | -42.9884 | 2025-09-25 13:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| ab0d38b6-72bc-3e6b-8a5f-602f90c58991 | -15.7257 | -59.4708 | 2025-09-25 13:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |


[Clique aqui para ver as próximas entradas](README40.md)
