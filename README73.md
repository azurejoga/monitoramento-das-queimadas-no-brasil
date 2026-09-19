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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37639909-5f07-355c-97a9-2bc6256bed7a | -9.02822 | -48.74233 | 2026-09-19 04:57:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e2cb86c3-7310-3840-ada4-8040602682af | -10.64452 | -48.70871 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa713482-86d0-3ad3-9979-ef156781f6ba | -6.44883 | -58.15074 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8fd440be-d164-3e33-9eea-a1ea7dac350b | -11.08519 | -48.27798 | 2026-09-19 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 04451e2a-2830-38e8-b3dd-9e22abe33197 | -4.5388 | -54.93563 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| dbee010d-4c8b-3c2d-b5a0-bf5c6c7c7ce3 | -10.9228 | -48.41421 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d87373ad-7e3b-3ee0-b2d4-985934c72bdf | -6.81439 | -59.19139 | 2026-09-19 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 593a289c-5073-3211-b659-5ac6998815e8 | -3.36931 | -50.45327 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54b600a7-6021-3c5a-8a60-70dfd0fcfcbb | -10.60825 | -50.25077 | 2026-09-19 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b74c6eab-ebce-3cc4-844b-e37a2c9580cc | -9.17072 | -59.41621 | 2026-09-19 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8caa7aa-bfc8-37cd-9571-2a6fbb088be2 | -7.64388 | -46.11172 | 2026-09-19 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 95170a37-f2a7-36ce-9a9d-8f557b4d7fd6 | -9.90102 | -46.55185 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3adb1beb-82aa-3c5c-bf6f-c2c0a6be3326 | -7.58025 | -44.91008 | 2026-09-19 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d44294e0-1a4a-3607-a39f-05b4dc992b41 | -4.68092 | -46.39981 | 2026-09-19 04:57:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf875fa6-59af-3df7-ac7c-6401663fe540 | -7.4979 | -55.01287 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b0dd425-8698-361c-8bc7-b20921da2bb6 | -5.68466 | -47.11935 | 2026-09-19 04:57:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b99689f1-932f-318c-a7f9-11c6ceb82075 | -6.7053 | -59.46416 | 2026-09-19 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8e1f71f8-c5f9-3a66-ade3-5d53d413f9ff | -4.5356 | -54.92765 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3ffe8dc2-f73a-330a-ba2c-cbca567abe3d | -3.03765 | -51.37016 | 2026-09-19 04:57:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f609b2a7-6daf-31a3-be55-8735bc200609 | -3.3341 | -50.12004 | 2026-09-19 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c69aaa74-edcc-3979-991d-5f78f1974aa1 | -4.43274 | -55.52718 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0da40f85-b481-3819-a675-2cb0ee0dcf5e | -7.55509 | -61.33228 | 2026-09-19 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eecbcf7b-dfc8-3fc2-bcbe-37be2224e1e9 | -7.87603 | -47.63718 | 2026-09-19 04:57:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 832b8529-4d09-39f2-aa78-3bc81fb041a9 | -5.74252 | -57.58666 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99614ab8-00d6-332f-ac47-1f966fae2c34 | -7.58902 | -55.69559 | 2026-09-19 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f089b9a-6708-3782-a237-bef1f5c88788 | -10.7951 | -50.8782 | 2026-09-19 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ea5e3350-c74a-3c71-b501-47ec8a0ba357 | -8.76844 | -44.22591 | 2026-09-19 04:57:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3136c898-f02f-3bc5-b9fd-226d9568a70d | -7.40568 | -49.8439 | 2026-09-19 04:57:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cad60cce-0db6-37d0-8dcf-c27ddc36a7d2 | -11.08153 | -48.29545 | 2026-09-19 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 83c74f0a-af09-333c-8299-0be61dbde9c2 | -8.32759 | -50.85564 | 2026-09-19 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a779d9ca-4a5f-3c1a-87a8-7c2c0d591ce3 | -9.02894 | -48.73737 | 2026-09-19 04:57:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 25.9 |
| debbf91c-7e84-395f-a628-c2c0e4d70854 | -8.61191 | -54.59576 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3afb0c68-868b-32f8-b071-ba03ffec2650 | -2.90437 | -54.18678 | 2026-09-19 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8fd6e2e9-30ff-3006-a1b8-f63ea8b12d22 | -8.23241 | -45.60178 | 2026-09-19 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a75bc593-eaed-3a0e-ad43-722aaa1a9142 | -9.58052 | -55.10592 | 2026-09-19 04:57:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ee07d75-7c4c-36d9-8103-38814dc17ff9 | -8.42074 | -54.7312 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 8a763d85-93ac-315c-a6ab-107f9e7e8beb | -6.08956 | -55.55593 | 2026-09-19 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6cf865ef-4758-3f23-8520-49b7eded6311 | -2.96268 | -52.14606 | 2026-09-19 04:57:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4cb4ddc3-9ae6-382c-be80-ac8a430763e9 | -7.58968 | -55.69164 | 2026-09-19 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8081d4b8-3fec-3450-a643-2bcf1a9b64be | -5.85537 | -51.93982 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6473851f-7b3a-39f7-b497-85b40d7d02d1 | -11.30094 | -46.76962 | 2026-09-19 04:57:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ce23a95-9be2-3581-9512-a2322690bd21 | -5.99686 | -51.79707 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32fe0bb7-7d80-3514-bc72-0d16edc4bfad | -10.36181 | -48.89354 | 2026-09-19 04:57:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3c443357-01ab-30a8-acbe-cef83c05b96a | -10.47015 | -51.26293 | 2026-09-19 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78c265c5-a331-3c8e-b782-3fa93869e3fb | -9.47411 | -54.43919 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b349750f-4b8a-3a61-81cc-2d1080aaa2ea | -10.45972 | -51.26091 | 2026-09-19 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ee83f33-0026-31f9-a2b1-3cd0dacbbd5e | -7.86705 | -45.12758 | 2026-09-19 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 401cb20c-db85-3c75-8abe-ac7b83812836 | -10.92228 | -47.85818 | 2026-09-19 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6271c30a-dcad-312d-90a9-b704c7d03099 | -10.20423 | -46.58932 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 83348c55-43c2-3a47-a58e-00ba2589ec19 | -9.78419 | -45.062 | 2026-09-19 04:57:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55542271-90a9-35ff-bc37-3d5168aa2046 | -9.88729 | -46.5491 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5d06adf-a367-3be8-a799-eb663ff798fc | -9.67714 | -48.33179 | 2026-09-19 04:57:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3dc79117-c7a2-37aa-a07e-5c4a18587195 | -3.3761 | -50.45432 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f235eae0-756b-378c-b303-144df8683b84 | -9.32967 | -60.31276 | 2026-09-19 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1467eb09-3174-379c-b61c-b56fa99affdb | -4.54295 | -54.93225 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f7223140-f2d4-3e5d-a703-1f72f2fe3b0e | -4.50705 | -54.97126 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1192357f-52d1-3309-9016-ab2f4364c34b | -7.40867 | -49.84865 | 2026-09-19 04:57:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 758f212c-6543-3280-a26d-167b19583f42 | -11.07989 | -48.28569 | 2026-09-19 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c0cc0196-3584-3fcd-8931-1a2b07ba03d5 | -5.33025 | -48.99048 | 2026-09-19 04:57:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f23dc4bf-0065-39af-b238-f859d2818c88 | -11.07623 | -48.30277 | 2026-09-19 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7756abef-aef4-3605-a0f0-5fa4e8e15f4d | -9.67766 | -48.32802 | 2026-09-19 04:57:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b9ddd3c7-e7e8-392b-ac10-0bde94e1ec46 | -3.36708 | -50.74065 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62ca6463-5e96-334e-a325-12ce8ed36658 | -11.07715 | -48.30597 | 2026-09-19 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 266467c5-b86c-3dcf-b95e-877f843ab0b1 | -9.00039 | -50.82506 | 2026-09-19 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a94d6b56-38b4-3eaa-9dec-d2359d8fe9b1 | -11.06525 | -48.3202 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a0cb8780-a65b-3816-aa41-358109423f8a | -3.15456 | -53.93508 | 2026-09-19 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8cf60b5-ac3b-329f-9215-6dee2ddeaa35 | -10.84935 | -50.18424 | 2026-09-19 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d95dbfb-164b-3ad1-aef8-2eaa0a00a805 | -6.98628 | -42.17215 | 2026-09-19 04:57:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 947d0d30-dd2c-3416-ae87-37c0c32bfd6d | -4.06234 | -56.24451 | 2026-09-19 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 271a9c6b-b826-30e6-8140-96e960a6bbb0 | -3.36261 | -61.31023 | 2026-09-19 04:57:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c011a02c-92f3-376a-99ba-a36045bdbe64 | -10.53899 | -46.6007 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64cc4c10-b6d6-35a5-9715-73801673f59e | -9.2076 | -46.76355 | 2026-09-19 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9938e597-6709-327a-9867-fa4967390605 | -8.61127 | -54.58852 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 986ec6a8-2705-36e9-bf86-92eb7430fcde | -4.49047 | -54.98477 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3f51d44-e4df-37c1-82a4-d9016c8e7a0a | -11.30328 | -46.77646 | 2026-09-19 04:57:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fefcb729-6085-3287-be19-052e60820292 | -8.29309 | -50.81558 | 2026-09-19 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce8ac127-3579-39e2-ac93-d7cb76f154c3 | -9.68757 | -54.3363 | 2026-09-19 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7a7dde74-0027-3974-8bea-5c4485195b63 | -3.36874 | -50.4569 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e01cd7d-d45a-3885-9ebc-fdeb50fc7422 | -8.75793 | -44.22337 | 2026-09-19 04:57:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4669d6ad-4dfa-3ebc-849d-7613e4d75880 | -3.36371 | -50.74014 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c23085da-b2f4-3f04-a979-7bb22fa65190 | -6.32777 | -55.27718 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec716087-48a6-3c5b-b89c-89ab073d942e | -8.88036 | -50.78343 | 2026-09-19 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 12983f00-7b2e-33f5-a9aa-37ee00e48b2e | -6.71124 | -59.45613 | 2026-09-19 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 84218572-091c-3491-ac92-3f16d115a915 | -4.88484 | -56.07099 | 2026-09-19 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 674927a3-9ebf-3260-9d44-819e1d46c24d | -8.31658 | -50.91788 | 2026-09-19 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3bdfec2-29fb-363a-8a51-938eb9c27292 | -7.76899 | -44.87346 | 2026-09-19 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d1473bd2-43ee-3ebf-9264-e7cb72442074 | -10.57975 | -46.54618 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 561c4843-4caf-3fda-b7c2-01229a891098 | -11.05646 | -47.9524 | 2026-09-19 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b66a77f-16cd-3862-a2ae-4eb87dcc1353 | -7.63928 | -46.11103 | 2026-09-19 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3ee27f76-9c67-3915-a5c6-da87328b9645 | -9.89708 | -46.54634 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 27909c29-591c-3c25-ab7d-5f5637eb5319 | -11.37002 | -47.32711 | 2026-09-19 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 849a5b60-965a-3f37-b35b-8ae2f87eb873 | -5.76503 | -57.45367 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 7bcee694-6e6e-37ea-9afc-7b28f30150f1 | -9.71438 | -54.82254 | 2026-09-19 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bef8cca9-f2d7-33ee-8997-9fb05948d129 | -10.53332 | -46.74375 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| eee2a6da-e955-349c-b2c5-052e846214a2 | -6.95047 | -46.97165 | 2026-09-19 04:57:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73158894-a783-3943-94b4-a1e38a8e9ea8 | -8.37111 | -47.2223 | 2026-09-19 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d46a2342-a25d-33f1-b1ab-462e8aaed193 | -9.70825 | -54.81784 | 2026-09-19 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 60c6c8dc-5ca7-37fc-b694-ee4639816010 | -9.80383 | -46.09467 | 2026-09-19 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99efdb86-298e-35a7-8912-04d107a3f058 | -3.33469 | -50.11632 | 2026-09-19 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 109d893a-b72b-386c-987a-713aa857bfcf | -6.6326 | -51.25075 | 2026-09-19 04:57:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README74.md)
