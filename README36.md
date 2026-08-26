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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 48f4b19f-7e47-3ecc-9a4b-1d8f5e347d37 | -7.37716 | -55.18762 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a0f5d94-c8b3-3654-ab48-d147e3706e57 | -8.62478 | -54.73835 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e25ceb2c-dd1e-3440-a40f-777670ce4759 | -6.30344 | -53.56495 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edbb2cde-fc44-3c5e-b000-68661e4cff55 | -5.51861 | -44.11428 | 2026-08-26 04:51:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f81b303-5b1b-3cae-96fa-968fcf6d00dc | -6.62864 | -58.4924 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23024139-f4f9-341e-b2a5-085ed46c659e | -8.01902 | -51.81982 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c4364fb-4cb7-3f0f-a48b-1eac667e5a24 | -6.64834 | -58.50363 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 318b1cb4-7f16-34a2-8777-f8860350d4ac | -6.64544 | -58.49524 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 322b07d8-e444-381a-a3a5-63e7071c1cb1 | -8.16477 | -54.9807 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4cecf13c-a769-30a8-9b1b-37b354c3c0bd | -7.87175 | -46.10698 | 2026-08-26 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f943e9c7-d527-38a9-a675-476b9ffe94c4 | -6.33909 | -54.73875 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64c44ab4-2d41-3828-bd81-571b77788b12 | -5.95731 | -53.60344 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b0e2442-97f2-3f7e-88fd-b5962fe32ef0 | -7.03503 | -59.23493 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2b5fa500-f4bf-3db2-95db-03621c4d45e3 | -7.28757 | -44.08085 | 2026-08-26 04:51:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ed0c1314-e1fd-3ced-933e-f88498d10715 | -6.22523 | -55.47667 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba9cb0c1-fa1b-37a9-90a2-b1dccb3cd080 | -7.86201 | -46.10966 | 2026-08-26 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7a352b42-8e3e-3456-8095-d4fe4dc76f85 | -6.63305 | -58.51725 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ae3a4423-7f37-33f0-a2fb-27f393386eb2 | -9.44035 | -51.68522 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5e48bee3-20b3-306c-9e86-25021c51f520 | -7.95173 | -52.43855 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 533e3ff9-c27f-3cfa-95ba-162fa9222577 | -6.95643 | -56.50062 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80d62cd0-09d9-3043-ac11-fb45d153d5f2 | -6.14222 | -57.70926 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1bc3f548-6773-3c02-bee2-46f6014918d8 | -6.2772 | -53.36402 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4d67a37c-4092-3cbc-8356-6391cb661819 | -6.98055 | -59.26269 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eec94b2c-7d42-3b72-bc1e-76ccb047b312 | -10.36949 | -45.0647 | 2026-08-26 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 060ec718-8caa-3886-9005-700f2778d0dd | -8.62651 | -54.72746 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fcdd5fc0-7433-32a5-b418-f38f66b37727 | -6.42414 | -54.93331 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a9b48c0-2946-3a1e-a632-4e20a9f86d63 | -3.42473 | -53.59171 | 2026-08-26 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5d22f87a-c60a-3f32-a97d-da002ee4ded9 | -6.54237 | -55.08851 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2bb5775d-2d78-389a-803b-1f91b717e01f | -6.62804 | -53.18831 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd37b9ef-790f-3407-a24b-85bba0d142a5 | -6.87362 | -43.74201 | 2026-08-26 04:51:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4479e8ee-1c2c-3f2d-abaa-ceaeecf1a50d | -2.98199 | -49.27317 | 2026-08-26 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ff5eef9-1b6b-3645-9e18-cee9453278fc | -4.94708 | -43.1965 | 2026-08-26 04:51:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4dec4da4-2df7-3b16-9124-0a9f68fdb40b | -7.09225 | -56.54358 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3fc8ebc5-e68d-32a9-8bc5-b59521bd15aa | -6.16337 | -57.80721 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e618e9f7-ba33-3282-91c1-3757a12f788a | -6.26836 | -53.37691 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 55c895f1-f043-324d-8996-f8510ac0fc1d | -8.03074 | -51.81049 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9e025c9-5eba-3411-bd36-54beb2d0e60c | -7.79389 | -62.39 | 2026-08-26 04:51:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13f24579-ed14-3fcc-85bf-abc036f074c7 | -7.56445 | -44.47847 | 2026-08-26 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ade0300-846d-31ca-a2a9-c54ee9bbdce6 | -6.74407 | -58.57928 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cfbf1c33-4e5c-3235-9793-d5adcece21ed | -6.63284 | -58.49307 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c9f050e-5506-37a2-a0d4-1e77381af197 | -7.26478 | -49.86266 | 2026-08-26 04:51:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 35bfcd94-2c87-303d-a341-dab909d319eb | -7.02625 | -59.23346 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6359d732-f163-341e-8e1e-d50222f03142 | -7.30422 | -49.54499 | 2026-08-26 04:51:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 16df702b-93b1-3d78-9773-3c7a1f1534bb | -7.52248 | -61.38195 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| eb5a7a1b-3de5-3779-9729-7e99f527d4d4 | -9.01611 | -54.58304 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fb84fec7-c922-3504-9691-037268598d9e | -6.1309 | -57.82756 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9d6ee448-6521-3ece-b454-b1d746af7e97 | -6.87847 | -43.74621 | 2026-08-26 04:51:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aafd6c27-5923-31e4-a5cc-07f2b58da4ef | -6.86596 | -56.57293 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 71e4b734-0b64-332b-83c2-a00911bbf753 | -7.76492 | -44.76012 | 2026-08-26 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b6a77a2b-e38d-3daa-a752-3fca8ba0d4b9 | -8.0125 | -51.80356 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4d9c02c-f258-316f-aa32-09d01273da7b | -5.49205 | -49.10495 | 2026-08-26 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 127e96a8-6653-362d-9897-8c9d5b91ce43 | -7.75989 | -44.75948 | 2026-08-26 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8b74223f-c434-335d-af83-34fbb6980f1e | -6.41053 | -60.06459 | 2026-08-26 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0afb2850-87c5-37dd-9082-5c9679864f3d | -6.63926 | -58.50615 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7cdc26c2-8516-3702-b626-3c8a246d0225 | -7.29836 | -44.08485 | 2026-08-26 04:51:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 525917bd-b12b-3eaa-8725-f8a7b3859874 | -6.64347 | -58.50683 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b75af363-7fe8-3351-938c-079d619b792e | -6.30234 | -53.57196 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8d47c00-53c2-398f-a814-38e4d595b0e9 | -5.63794 | -43.61121 | 2026-08-26 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37607c0a-0b85-31c4-a4ff-f8344c674ed7 | -6.60739 | -58.38169 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b54867b9-6134-3fbd-835d-070c71ac93bb | -8.59114 | -54.71062 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d5148b22-629a-38d4-9a8e-56907fc4e374 | -8.14993 | -54.98606 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5c5a51be-a8f7-32b0-9017-d1e76285883f | -8.16494 | -54.95765 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3197d8e6-6e65-37cd-bcd3-fcbffdf7be9d | -10.3742 | -45.06842 | 2026-08-26 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 18.9 |
| e6d89f56-9dd1-32f2-a514-5e2220d9acd7 | -8.09567 | -47.5636 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 220c0af3-ce97-3853-9597-4e0bb183fe48 | -8.01957 | -51.81622 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b296d71b-2d4f-32c7-b3f2-25aa597911d9 | -6.61959 | -58.49058 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| be9cdf22-8282-3e39-ae6f-c908a8c8d116 | -9.52221 | -51.67879 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4866b799-e5b3-3929-9843-a23c2d62fd7d | -7.02476 | -59.24203 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d1f99f94-1a87-3267-b418-e5f0f850b94c | -7.12824 | -42.78913 | 2026-08-26 04:51:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0f1830ec-082b-3f7f-b779-f0268cc5cde6 | -6.44287 | -54.98644 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4d9eb3d-7f15-32ac-8429-6c4af0ca974a | -8.63935 | -54.75558 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57be25a7-8fca-396f-8759-512072a404af | -8.01194 | -51.80719 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb9ccdd8-41f2-302a-b0a7-e3771b537a6c | -8.08007 | -47.51205 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f24d6b80-6687-3d34-9c4e-aeea58e717ec | -9.4153 | -51.62085 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a0dd3265-aef5-328b-ba7d-0e1e3b6558b2 | -6.45636 | -43.091 | 2026-08-26 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1edb7bde-84d7-3f44-9117-0a616227c822 | -7.06283 | -59.23077 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c859e5e2-4492-3b1c-abf3-642632fa252d | -10.37323 | -45.05994 | 2026-08-26 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1834e4af-3c41-3e71-8aa0-6ae3f8d827c2 | -7.02009 | -59.24267 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50eeb960-527f-3ab9-89d6-3289ea932a56 | -5.62984 | -51.88992 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c038121f-b9b2-3e6b-ba1d-1dbe94a8a3aa | -7.39032 | -55.16582 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7412a582-fe93-384a-9895-1ed91063295a | -8.01752 | -51.7933 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6be219fa-a80c-3fac-947d-1126856a6caf | -7.52734 | -61.38881 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| ef6010ca-06d2-39f3-bf0e-2b4462000751 | -7.0157 | -59.24189 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2df936c-b1cd-3dac-b775-db4420c7e7dc | -6.63084 | -58.50481 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f65b7bab-06c7-30ee-9361-62e1026ee435 | -8.16835 | -54.95818 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd5f7221-0619-3072-8d1d-1a9711e6a38b | -8.21944 | -55.01285 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07d1e3ec-8210-3a1c-94a7-4845ddd154fc | -5.79523 | -57.61163 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bae28c99-e820-318d-b67c-e7976a262506 | -9.41302 | -51.61282 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be157085-1219-3628-8818-7501be228b6f | -6.14069 | -57.84394 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6a522a3e-d92a-321a-8a45-0337c8fd2b31 | -7.51674 | -61.39004 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 24fa8756-b4f4-31a9-adbb-cfa08705b885 | -8.75539 | -49.94966 | 2026-08-26 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c46bf781-4b84-318f-a0bb-71541c4e32b0 | -7.38096 | -55.17977 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6ae656b-b638-3234-9459-f63c35c6a464 | -2.89127 | -48.80208 | 2026-08-26 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d7ddf714-d93b-30c1-8f36-8883c0483c60 | -6.11217 | -53.84924 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2fb346c8-7941-3b1b-b1e9-ab04a1ce0e91 | -7.0252 | -59.2391 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5239beb2-55ca-3b03-81c8-89fb024c9c2b | -9.02075 | -50.77618 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff3562f8-dcc1-3a3f-bf88-0dad1e5276ba | -6.72234 | -59.45157 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 682db9da-e2a4-3be8-a916-99187fa7493e | -7.09277 | -42.17597 | 2026-08-26 04:51:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7b09304f-939d-3601-8660-997e254aae7d | -5.78718 | -57.61038 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe69ae63-6d71-3bfe-9baf-95f534272f33 | -7.02734 | -59.22622 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README37.md)
