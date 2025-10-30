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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38bad44a-7f5c-3211-9e9b-3fca98deeb8b | -6.62102 | -47.17909 | 2025-10-30 04:25:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6fc9b9e2-2250-3a5a-8cbb-5c024acd1a6e | -5.85184 | -47.70181 | 2025-10-30 04:25:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0fbf814a-1682-3a88-a1b7-68ef3c651b52 | -3.446 | -52.81929 | 2025-10-30 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 851d661d-5159-386e-8aee-0a2e8cdbc745 | -7.073 | -44.47075 | 2025-10-30 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 806c98b5-e312-3ceb-8f6e-1f58c90181ba | -6.64469 | -47.28765 | 2025-10-30 04:25:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 423b126f-6957-3ce0-93bc-b7ceec191709 | -4.5367 | -54.96936 | 2025-10-30 04:25:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4ff621b-afd0-332a-b6b1-c0951227a7c7 | -7.38731 | -42.4683 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4b09ba9e-f782-3e3f-ad1d-ae0b659c96b6 | -7.79958 | -46.41162 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 595b5b58-6019-3e3f-9990-d8b00332a4f1 | -9.84631 | -47.69104 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3020fbfa-801e-35af-a8cb-53f147bcab99 | -10.93738 | -47.79643 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0484bc00-bc1d-3db6-af7a-94ef7159ccc2 | -9.89173 | -44.87937 | 2025-10-30 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1a98d04-9601-3c2f-8214-8b5a88b84555 | -10.59285 | -47.9319 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48df432a-f87a-3657-925e-4b063916c349 | -7.38355 | -42.4677 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| df0c34e3-e08c-3b4a-95bd-8e4febd61e9e | -5.31075 | -44.84793 | 2025-10-30 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ef7c1e2a-e025-3386-bb1b-c742eeb0d504 | -7.07796 | -44.94125 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| fb3eeb06-66aa-3c91-805b-b9425a51d13b | -9.83466 | -47.69997 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c8ea03f-bc6c-35f8-8591-75fd967a5f92 | -3.82644 | -51.22203 | 2025-10-30 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b12ec57-679f-31a4-a7cb-f227f478eea2 | -5.03975 | -45.16776 | 2025-10-30 04:25:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7fc53e46-d26f-3afe-9f5a-3f850d85034c | -10.27515 | -44.58481 | 2025-10-30 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eefa0d8c-15f9-3acb-98c1-53bcb9b2995e | -5.86416 | -42.7548 | 2025-10-30 04:25:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ba102a29-ce99-3dc5-aecf-7f6b1e714795 | -11.19266 | -49.78538 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4616b71e-e1cf-3998-95a7-533e83b13010 | -8.15522 | -44.81093 | 2025-10-30 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b32cd2d8-75c4-3ab9-93d0-529e0f55bfcd | -5.4351 | -45.33258 | 2025-10-30 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d9ae967-14c5-3f88-a525-d588a83ebbe7 | -5.57118 | -42.1718 | 2025-10-30 04:25:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3b00a498-b5db-3c67-9181-2a578b429c5e | -6.15798 | -41.59712 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b371e06a-5b2f-3cbd-b9cc-0e7588ccc5ac | -3.77882 | -52.28336 | 2025-10-30 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0f040e7-d382-3e19-b53c-71a8f4cc39a5 | -8.15579 | -44.80727 | 2025-10-30 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b15324ec-2a3c-30b9-b1c9-635cc4de541c | -9.81671 | -47.57808 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e9aa0ee4-a893-3d68-bbd9-f5a1a24576fc | -8.05088 | -49.63305 | 2025-10-30 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad958a35-9b6f-34a0-8c4a-d8fe6c401655 | -7.78642 | -46.45213 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20df2a7f-3e7d-3d3a-8fba-c664cf0f22fc | -9.90551 | -44.90478 | 2025-10-30 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfb59832-71a1-3b5b-bae5-e7720b2237ae | -6.01357 | -41.9811 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| a472d886-e323-3699-a281-3ca9cdee7ee9 | -6.21567 | -41.82588 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9aa4508f-d114-3ca6-9a84-c54f2f66fcfe | -6.14397 | -41.7146 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 659949b9-4598-30b1-87c8-d430cf4f74a3 | -7.15873 | -44.86504 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76aa2d2d-0d2a-3d6c-86c3-a035dc3993cc | -7.79027 | -46.44919 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7971729d-b1cb-3781-8480-b470f0b4fd1b | -10.92611 | -50.20554 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef1637b1-e6b3-34aa-9a78-51f5b488c9a0 | -8.33077 | -47.93771 | 2025-10-30 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 79aea50d-d1dd-3b96-aa0d-4ce35d584c5e | -5.72706 | -44.40285 | 2025-10-30 04:25:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b56b0656-fc46-3059-97a3-7e19fc1c0da6 | -5.5102 | -46.23604 | 2025-10-30 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1231214a-a7b9-3b50-bcd4-88feeaa9443f | -6.1436 | -41.67308 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ea7972c2-8f2c-3f64-9692-b1a2ff152fe8 | -5.05662 | -45.31969 | 2025-10-30 04:25:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55bcf93c-20ad-34c9-a108-85f7b7a1c19a | -7.86986 | -44.22771 | 2025-10-30 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db8558dc-3817-37e6-bfdc-95981efbe156 | -4.98752 | -45.52129 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1bf06d46-8dcb-333d-b167-1be821007c0b | -7.7897 | -46.43135 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 339c73c3-3031-3b0f-affa-5b483c3ba901 | -7.32623 | -42.49163 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a6e566c9-0c11-3e03-b64e-5654687dbb51 | -11.23651 | -49.78077 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c6511d8-89b0-312a-9a96-2b65b36ba9ca | -5.66879 | -43.3154 | 2025-10-30 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b218350-ba1f-332e-9d16-d4075b714437 | -9.60169 | -45.15362 | 2025-10-30 04:25:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9fdf9cbd-d21f-30e9-ae30-a9bcc7a5b0d4 | -7.95525 | -46.75983 | 2025-10-30 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b93dbf0f-44c8-3227-a3e0-21a3e984b15d | -8.02644 | -42.5127 | 2025-10-30 04:25:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f66dec46-60ec-38d0-bc9c-3321132e3c53 | -5.7931 | -40.8234 | 2025-10-30 04:25:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 315f7e64-e449-30a1-9cb5-326057a7a76e | -10.86642 | -47.62244 | 2025-10-30 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c3d1858b-91a3-35bd-a6d4-79654d807f83 | -5.70277 | -43.13919 | 2025-10-30 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f6ee61b5-8a8b-3d52-ab96-0d6fde004a8a | -11.13 | -51.08463 | 2025-10-30 04:25:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| fb05edc4-7b30-358c-a3b2-db3f504f096d | -10.96328 | -50.22472 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4cf6fa8a-55c6-3d14-a2a3-59a8f375be6e | -8.73268 | -50.01543 | 2025-10-30 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cbe60d1f-839e-3dbf-93d1-6a3fc29f4470 | -6.1486 | -41.6063 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ac451e88-b49b-3a1c-834e-4fa5d8991883 | -10.8835 | -44.35413 | 2025-10-30 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da55f448-efc9-3cb0-9b9f-925de3c50f08 | -4.74619 | -45.71591 | 2025-10-30 04:25:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7aca900b-08df-3158-af6d-ff11d0a5e84f | -6.97667 | -47.31553 | 2025-10-30 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8a40cdc9-8564-3ce3-aa2d-cf21ee208ada | -6.46314 | -41.64857 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e0a88deb-0c6b-37f9-8895-01449e6ca3c7 | -7.32381 | -42.48193 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6c452317-9a20-3af1-9aaf-14cd11026a53 | -8.05157 | -45.16785 | 2025-10-30 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 889ce0cc-d302-302d-ba83-d1e8f7031645 | -7.80708 | -46.40961 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0027f303-4a36-3d6b-af7d-0cec1db2ee75 | -11.63801 | -44.046 | 2025-10-30 04:25:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0af5d6a2-b155-3fcf-9ce3-876d03df0b75 | -7.33148 | -45.67284 | 2025-10-30 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8cd9194-00eb-374a-8a72-65572930270a | -10.85698 | -47.8736 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4bade41b-0cef-3b36-adef-e156f2f1bcb6 | -4.31026 | -48.08461 | 2025-10-30 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f62a922f-ff3e-3a46-9c9c-04fd8f3ca968 | -7.87215 | -44.23593 | 2025-10-30 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bfe85e63-6623-3f2f-8e5f-94a7da877f84 | -8.53993 | -48.97899 | 2025-10-30 04:25:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e64ee2ea-8464-36d1-a792-05d2f776a3b9 | -5.30604 | -44.32411 | 2025-10-30 04:25:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25597f8f-e286-3dc7-b06f-b01a9ca24015 | -5.48271 | -44.10685 | 2025-10-30 04:25:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1afb30e4-36f9-390b-a392-b5ed5a3764c9 | -6.20797 | -41.82475 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 021a9fcd-90fd-3a99-9ae5-b8a4ceb49cdd | -6.11753 | -41.70627 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 157f50eb-3f3a-3e2c-b982-c88112d8b356 | -6.16842 | -42.39639 | 2025-10-30 04:25:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 132a148d-e5bc-31b6-b22b-3dfd168d8601 | -5.64547 | -45.98189 | 2025-10-30 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6552b5dd-d0db-3af9-a9f2-a4aad5865c86 | -5.63053 | -41.10643 | 2025-10-30 04:25:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| db9da0cf-3d5a-3de7-9ce5-099b2c96f80b | -5.64877 | -45.98241 | 2025-10-30 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15837750-0bf2-3962-a7a7-3f918bf3af75 | -8.05325 | -45.17924 | 2025-10-30 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5758cb98-c8dd-3628-a9ad-ed5994e64347 | -7.61898 | -43.59253 | 2025-10-30 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4c16936c-285b-38a6-9e4c-fa150ea67e14 | -4.68756 | -45.59392 | 2025-10-30 04:25:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7f275786-6a76-3dd2-ad6b-d8e35985bded | -11.06971 | -47.54076 | 2025-10-30 04:25:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd3a6ec1-acd6-36cf-8d6a-e81a78e2a48e | -5.08297 | -46.08012 | 2025-10-30 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60a54994-35e9-361d-ab58-a6e203d0278c | -7.30105 | -45.67173 | 2025-10-30 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a5103e7-d7aa-39c8-b3ef-fb93f01d49df | -9.90611 | -47.91095 | 2025-10-30 04:25:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a7d2a134-b2d4-3dad-868a-697416ab49ac | -9.71259 | -43.37805 | 2025-10-30 04:25:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 09dfa516-89fc-3ab7-be07-38cba0705be2 | -10.95971 | -50.2241 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e24ceda5-bce8-3728-bac4-6d33c5e45077 | -6.09291 | -46.69763 | 2025-10-30 04:25:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0054e4b7-cff0-336e-b9c5-4dd7df3b76bb | -7.77934 | -46.51845 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d13deaae-54f8-37ad-bc16-a734cd59d85b | -10.76691 | -47.88393 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a395482-a3fb-3336-8410-45c9aa845fb8 | -9.89187 | -49.12122 | 2025-10-30 04:25:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 12fd8f09-a4e7-3551-8e98-e574db9f97c8 | -4.94535 | -45.6171 | 2025-10-30 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 473e46d6-6349-308c-82ad-ac696b5e3bde | -7.65254 | -42.24619 | 2025-10-30 04:25:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 011956d4-a247-36d5-a168-a81f1f1cc692 | -11.00676 | -41.6782 | 2025-10-30 04:25:00 | NOAA-20 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f8bc2e40-6e8f-36df-bcfa-4cc24fb5740d | -7.78967 | -46.41005 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c330ca7-58f8-3cc8-aa4e-35db569f09bd | -10.36043 | -47.27861 | 2025-10-30 04:25:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48f8b7c3-daa5-30de-bb30-b1cabe4cf23a | -10.67694 | -48.04391 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4c1e7ab-291d-3779-b917-ed8b89d0d5b8 | -10.47796 | -45.03266 | 2025-10-30 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f66247ba-e0c1-3653-858f-cbe4133d2165 | -3.66832 | -51.71602 | 2025-10-30 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README45.md)
