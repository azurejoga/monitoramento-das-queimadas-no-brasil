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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89d8b008-1979-37bb-bfc1-51ea53e48ebc | -9.0799 | -65.4349 | 2025-08-31 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| ec29185e-798e-347b-a459-1da4ff4a5222 | -9.4431 | -60.5884 | 2025-08-31 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 7f4564ae-3807-3409-87b7-ceec2d7c4a26 | -16.2217 | -52.6992 | 2025-08-31 03:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 2b06c27a-61c9-35e3-ae98-67529020904e | -6.1665 | -43.3273 | 2025-08-31 03:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| b9fe48cf-18b8-3438-a73c-49fdede3e619 | -9.4431 | -60.5884 | 2025-08-31 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| efc8168e-572c-3221-9b82-744356221272 | -6.7093 | -51.4165 | 2025-08-31 03:50:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 2168ebae-64c0-322a-945f-7ead08e6c72d | -16.2221 | -52.6778 | 2025-08-31 03:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 85db2133-62cf-3c95-90cb-572dcfc09d7e | -11.3293 | -63.2681 | 2025-08-31 03:50:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 13e80dc5-eb65-322c-8ede-509ef30f0580 | -6.1853 | -43.3257 | 2025-08-31 03:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| fc67eb86-c3ca-3386-91e1-1f7312e7d8c1 | -9.4432 | -60.5692 | 2025-08-31 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 304a9a3a-6c3b-3630-9f0b-f9164486bd9b | -9.4433 | -60.5499 | 2025-08-31 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 718c5b0a-9eca-3412-b0fc-2fc2a4e1f715 | -9.0613 | -65.4542 | 2025-08-31 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| e150eab8-364b-3272-8b6a-1ff70eae6e01 | -11.3106 | -63.2691 | 2025-08-31 03:50:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 1ea73ae6-205a-3c92-b4ed-81f82607db58 | -9.0614 | -65.4355 | 2025-08-31 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| a4ad35c6-d385-3725-8f8e-13b0f03f7a98 | -9.4431 | -60.5884 | 2025-08-31 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| c177720e-93b7-3448-95c3-a04012cd5054 | -6.1667 | -43.3039 | 2025-08-31 04:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 48.1 |
| d82a8c13-8cee-3c88-9d10-4e9723379650 | -6.1665 | -43.3273 | 2025-08-31 04:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 7873a4fb-de09-3c63-b15f-2c58455e1751 | -6.7093 | -51.4165 | 2025-08-31 04:00:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 347c0a17-8f7c-3e19-90a0-6310c8ba63bc | -9.0613 | -65.4542 | 2025-08-31 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| a74b18da-44a8-327b-9f76-f88b480c269c | -7.0951 | -44.3128 | 2025-08-31 04:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| a2255324-b961-3058-b04a-8505cdf46cb0 | -9.4432 | -60.5692 | 2025-08-31 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 59d3bb54-ba69-32ca-a94f-6fc213e8020d | -9.0614 | -65.4355 | 2025-08-31 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 45509557-6825-344e-9e08-2e5221606587 | -2.26327 | -47.85668 | 2025-08-31 04:00:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f3f28f6-54dc-344b-86c9-fac9a480475d | -5.12217 | -38.03568 | 2025-08-31 04:00:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 013eda90-589a-3dce-a942-768d66e64f9a | -3.81697 | -41.55318 | 2025-08-31 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| b722cdc9-5c19-3936-887e-b7af6512533f | -3.4866 | -40.67236 | 2025-08-31 04:00:00 | NOAA-21 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| faa7b76b-1c97-30be-871a-4d70729fbb55 | -4.40558 | -40.69389 | 2025-08-31 04:00:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 808199f0-910e-3790-81b5-edcda7c61972 | -3.81744 | -41.57239 | 2025-08-31 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 72ebaffd-3b5c-3ba9-8812-584f077e85ac | -3.21575 | -46.83303 | 2025-08-31 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a16c1cd-1f5b-3db2-83bc-945f3ab263e0 | -3.51362 | -47.20158 | 2025-08-31 04:00:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d33104db-ae75-31c7-870c-3cc7af8338a6 | -2.44195 | -47.32811 | 2025-08-31 04:00:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ddbd58fa-0efc-3e47-aedd-837760cb7e93 | -2.82853 | -40.3598 | 2025-08-31 04:00:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 05d06fd8-42b4-315b-b19a-dd216cbca472 | -4.26875 | -40.93638 | 2025-08-31 04:00:00 | NOAA-21 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7f56b473-ee64-3271-a485-7bbd5479efac | -3.51274 | -47.20681 | 2025-08-31 04:00:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e9491d0f-4acf-373f-931b-3e37010a12ad | -4.16915 | -42.03098 | 2025-08-31 04:00:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 373b242b-ee7d-3e5e-8661-41676a8caf16 | -4.27546 | -40.93746 | 2025-08-31 04:00:00 | NOAA-21 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 77415a31-c4c9-3e75-91a3-aecd5d644cb7 | -4.82082 | -37.80555 | 2025-08-31 04:00:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3c53df40-bbf8-30ce-a168-5636b09f1779 | -4.59795 | -40.61664 | 2025-08-31 04:00:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fb64150e-d1c8-38ce-885f-72a69b40639c | -3.48604 | -40.6759 | 2025-08-31 04:00:00 | NOAA-21 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9b6f4626-6c98-34b8-ab1d-67ecc91ca3bd | -3.22158 | -46.8323 | 2025-08-31 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b04a0a87-787d-3ea1-a16b-2a9b8a5bbd6d | -4.2721 | -40.93693 | 2025-08-31 04:00:00 | NOAA-21 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 32f43ac2-6fc1-3ac5-9da5-f9743e80db38 | -3.05955 | -39.92902 | 2025-08-31 04:00:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e37eb07b-e0ad-307d-899b-829777714533 | -2.34379 | -47.5858 | 2025-08-31 04:00:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf1f00d8-6941-3550-ae26-d83caf91edec | -4.40613 | -40.69038 | 2025-08-31 04:00:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a2ee9523-a53d-32a3-bad2-364ec3019829 | -3.602 | -41.4473 | 2025-08-31 04:00:00 | NOAA-21 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| edd4794c-7c11-3608-a207-5f9e828bc28d | -3.22051 | -46.83376 | 2025-08-31 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 535ea6e9-0700-3e83-b4c0-66dfdffb8f75 | -3.51849 | -47.20223 | 2025-08-31 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2a5f0c2d-fe7d-3fde-86b4-602cd291bade | -2.26844 | -47.85758 | 2025-08-31 04:00:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73e7df0d-d330-3af9-a825-a1976469bc91 | -4.17263 | -42.03152 | 2025-08-31 04:00:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 78793260-7ca9-3355-b0bd-9482041a571d | -2.26377 | -47.85364 | 2025-08-31 04:00:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11d1d83a-3e46-3be7-bc32-7ea043c944c4 | -4.62489 | -41.39495 | 2025-08-31 04:00:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dd775d40-5e1c-3289-93ea-59f2be7cc72a | -2.44242 | -47.32528 | 2025-08-31 04:00:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 768fa9a5-320e-353f-bc17-788f05deed34 | -3.28674 | -43.41412 | 2025-08-31 04:00:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 233654f8-88e5-32b1-b052-f68ec4e054fc | -3.26571 | -42.66089 | 2025-08-31 04:00:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c0a47c8-07a3-36b6-9728-05b4b12c09a7 | -2.26893 | -47.85455 | 2025-08-31 04:00:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1967d4d0-a13e-307c-8268-6b3bc0a5d0f4 | -4.50712 | -37.95038 | 2025-08-31 04:00:00 | NOAA-21 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2ba27be5-03ab-30b6-874f-70509cc3f3ef | -3.059 | -39.93248 | 2025-08-31 04:00:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8cb3d737-f943-39f0-b433-29219d75d5e7 | -3.5176 | -47.2075 | 2025-08-31 04:00:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b325562a-02a3-382e-b7ff-ecccd27756c9 | -4.39225 | -41.90825 | 2025-08-31 04:00:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 969ff2da-3422-3ca4-9ef4-e12f40830539 | -4.94201 | -37.36067 | 2025-08-31 04:00:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e2e73094-b6a0-3056-a805-3e914bf0a754 | -4.50216 | -42.8993 | 2025-08-31 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ddc97e8-72b1-39b0-8704-09987c6240f0 | -7.2125 | -43.7046 | 2025-08-31 04:02:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 725bcbd8-51b8-3654-b9da-f2ca4bf042ef | -10.78412 | -48.81366 | 2025-08-31 04:02:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cae08c58-b8d2-3a9a-a83c-863c7f07458e | -6.17869 | -43.32225 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| b1c16e43-c3d6-3ed8-8804-81f756f9c0d0 | -11.33052 | -43.64386 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f83cc2e9-51e8-38a9-a5b4-9f98826cc062 | -11.31709 | -43.682 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5e2d20b-4989-3557-a98b-346507ad0e31 | -11.08073 | -44.60616 | 2025-08-31 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 86ec6439-c458-3f94-a37c-21788b542bbf | -11.0195 | -46.86604 | 2025-08-31 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e42adc51-fb81-3f0b-b5ec-8c1a5362daae | -11.21754 | -45.02225 | 2025-08-31 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ace2630a-fa25-3b16-bed1-1b8e3fda90da | -8.96461 | -50.00543 | 2025-08-31 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7fe44948-d743-33ea-a158-983974d06f81 | -9.93817 | -46.34538 | 2025-08-31 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8bda749e-0d95-3864-8911-4ffccc95d215 | -6.17592 | -43.5701 | 2025-08-31 04:02:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c7589417-b774-3512-8126-4bc5d0251385 | -11.34698 | -43.63058 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 27e611b5-c91f-3868-80cb-98aeb76dec69 | -7.17221 | -39.42577 | 2025-08-31 04:02:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0975c86e-ccff-316e-9fb4-6bcb6a4e2475 | -9.5954 | -40.35453 | 2025-08-31 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 28.1 |
| d57c5e85-6f65-3f18-aa8d-fca4b439282e | -7.41472 | -42.05274 | 2025-08-31 04:02:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fb53ad57-131d-34ef-a012-8fedb8acd320 | -6.24233 | -42.4136 | 2025-08-31 04:02:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d870595a-896e-36c1-b0ef-8fe52f565f0e | -8.49702 | -44.73619 | 2025-08-31 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d24d0db6-3ef1-33b3-a92b-fa6275d49ea5 | -7.58803 | -42.72366 | 2025-08-31 04:02:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 540bc4ca-900d-388e-b79e-4b5d0ed41e5a | -10.02152 | -48.36937 | 2025-08-31 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 86e1e64c-1c2c-3abe-8814-cd7abd381b4b | -6.42416 | -43.96613 | 2025-08-31 04:02:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac24d74e-7957-3fe5-a484-478732ea9713 | -6.48811 | -44.07694 | 2025-08-31 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 029aa006-c317-3d58-b93c-7516ee061d94 | -6.3112 | -43.61616 | 2025-08-31 04:02:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1e90232-e20e-37e8-8526-6cac158bce2c | -7.64821 | -42.65033 | 2025-08-31 04:02:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fb372829-55d2-3663-971a-a20d87a4cf9c | -7.44597 | -44.8213 | 2025-08-31 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ff116ffe-0078-3fea-8bbf-8ea6a918caf8 | -7.58148 | -45.12051 | 2025-08-31 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7cd23aa9-893a-3758-a177-891e3709cb1e | -6.58144 | -43.64029 | 2025-08-31 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7a63aac-3af8-32f2-b368-b568324c19c2 | -7.5864 | -42.71156 | 2025-08-31 04:02:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8937f793-1bff-3aed-be15-267f1eb57695 | -7.22877 | -44.22756 | 2025-08-31 04:02:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d269d58d-2806-396a-b7ec-7e1eee45986d | -6.4648 | -42.42874 | 2025-08-31 04:02:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 20129b43-afce-3d89-ad65-45f409c41c65 | -10.48235 | -51.62686 | 2025-08-31 04:02:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 17c4557a-03a4-32eb-9494-5b550e0d9c85 | -10.60116 | -44.32693 | 2025-08-31 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| cba028aa-24bd-3b53-a80b-363b204f2030 | -6.9465 | -44.3142 | 2025-08-31 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53e5cf80-fad8-3a31-9807-05637dfe1c1a | -10.48811 | -51.62798 | 2025-08-31 04:02:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 48b132cb-64fb-3af0-a20c-f2a219f7c4c0 | -6.65094 | -43.94295 | 2025-08-31 04:02:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5605970-7bfb-3110-884a-1249937a9480 | -6.42781 | -42.76598 | 2025-08-31 04:02:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| db97c90b-ec78-3a07-aade-9d2c18962264 | -11.31774 | -43.67807 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fde44983-80d2-3771-879d-a83f9c57f607 | -6.56123 | -43.67224 | 2025-08-31 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 49d7cf83-d59d-3ff4-beb5-7e5aa1f786fa | -11.28013 | -43.30728 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bfb5bc93-f9c2-37b4-865a-1c2af986d7a7 | -7.71389 | -50.30238 | 2025-08-31 04:02:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README15.md)
