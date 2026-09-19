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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f943139e-090a-39dd-8f49-c8cf51a7e64b | -10.5364 | -46.7568 | 2026-09-19 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 3b7e262a-64a8-3b69-83eb-b61481072897 | -11.0611 | -49.7693 | 2026-09-19 13:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 158.0 |
| fb431628-e68c-3936-a052-c5a98544f813 | -10.8282 | -50.1601 | 2026-09-19 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 9438a566-0761-3585-a00f-2868dbdb8737 | -8.4314 | -45.8467 | 2026-09-19 13:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 434a4167-3f09-39a0-ac92-c6eaf82fc74e | -7.8595 | -44.8824 | 2026-09-19 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 3c91915c-9935-31a8-af81-fb1bd016ee46 | -8.45 | -45.8674 | 2026-09-19 13:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 183.2 |
| 2ab5aef2-4e47-3bbb-9ffb-ae4a8120f14b | -12.6896 | -45.94 | 2026-09-19 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 9153360f-76fd-3410-be06-099d55a0fdbf | -8.7919 | -48.6851 | 2026-09-19 13:20:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 241.7 |
| ebf4fa14-c3ac-3979-9117-c4ac73f2f9a3 | -7.0448 | -42.0906 | 2026-09-19 13:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 128.3 |
| 0e14be41-880b-30d4-a623-8aa3c256210a | -9.0358 | -48.727 | 2026-09-19 13:20:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 65c3abb4-c657-3566-92be-0a1748979e12 | -10.5368 | -46.7343 | 2026-09-19 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 170.3 |
| c1eef8af-3166-3cad-b843-3b929e356cb6 | -10.6703 | -50.6465 | 2026-09-19 13:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 135.6 |
| b4a9fc41-d96a-3b8c-ad09-6eb2a0684985 | -6.2582 | -41.6858 | 2026-09-19 13:20:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 160.1 |
| 946776d5-8f00-3602-99aa-94a7d866f87f | -10.8469 | -50.1795 | 2026-09-19 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 144.8 |
| 5707ca7c-25bc-3d60-aae6-59c12f57d922 | -11.155 | -42.7885 | 2026-09-19 13:20:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 118.2 |
| 0881df35-e72b-3f18-94fa-fbe0e84a80d0 | -10.567 | -51.3137 | 2026-09-19 13:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 528256bd-b279-3ccd-82f0-6244bc77e998 | -11.1369 | -54.0251 | 2026-09-19 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 373.1 |
| a9bf0a01-635d-34c7-908d-2cb89162f77c | -7.5203 | -44.938 | 2026-09-19 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 112.5 |
| dd5a7487-a20a-338f-80c0-946f92aec65f | -10.8466 | -50.2009 | 2026-09-19 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 129.7 |
| d8b82ed5-4a66-3bd8-a00f-96aaa09e279f | -11.9487 | -50.1402 | 2026-09-19 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 90b833f4-f48a-3e26-8ed4-8ae34201c242 | -8.7492 | -50.7847 | 2026-09-19 13:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 616fe59d-643e-3bb1-b386-553f628e3f4e | -12.1527 | -46.9933 | 2026-09-19 13:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| d781d6a6-4c50-3522-94da-7fef7e164344 | -11.1035 | -49.4623 | 2026-09-19 13:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 787ae05c-4067-3973-892d-28025e048d1f | -3.3494 | -59.8097 | 2026-09-19 13:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 98.8 |
| a1b59c38-d78f-33dc-9b1e-5c6a4e9d62c7 | -7.6087 | -45.4298 | 2026-09-19 13:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 163.6 |
| 3652841c-9f72-3c4f-9321-b52e3ecf562b | -6.941 | -55.0366 | 2026-09-19 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 73fe1f99-546e-3508-85aa-70de633e9e8e | -12.5032 | -50.0508 | 2026-09-19 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 212.7 |
| 14b50aba-1e4e-3bb2-b1fe-9e44fd831603 | -12.027 | -50.0015 | 2026-09-19 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 203.5 |
| 218eee3e-65f0-32b4-aa1a-f03bc2f99142 | -11.0608 | -49.7909 | 2026-09-19 13:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 118.5 |
| c5f002fd-4630-347b-a9d1-b4bd91092872 | -12.7085 | -45.96 | 2026-09-19 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 217.9 |
| 628aba4e-fb60-3d98-bc91-454cf2cdfb25 | -11.3166 | -42.3313 | 2026-09-19 13:30:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 102.0 |
| e48d10dd-ceec-347f-9a32-f5dc0cf0b715 | -12.1535 | -46.9482 | 2026-09-19 13:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 131.2 |
| ca7ceaa6-3e8a-3dd2-b736-fa023827825c | -11.4673 | -45.7077 | 2026-09-19 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| d85bb22e-b9f7-384e-a4b3-1ebdb360acc3 | -8.4314 | -45.8467 | 2026-09-19 13:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 03df65b9-f682-338a-919c-bd54ed183893 | -9.2603 | -45.939 | 2026-09-19 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 185.0 |
| f735187d-6c77-3436-b0ba-bb7ffaef31a2 | -12.2688 | -49.1907 | 2026-09-19 13:30:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| fd27e19c-2c5b-3397-9895-0fb71918ccd8 | -11.9487 | -50.1402 | 2026-09-19 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 9d234c9e-5fd0-3fca-93b0-884e6dadafd4 | -9.9699 | -46.6004 | 2026-09-19 13:30:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| fdbf5deb-45ab-30e9-b825-0dc33e5f00b8 | -12.2879 | -49.1883 | 2026-09-19 13:30:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 131.8 |
| d5022b60-6747-3eab-aeb3-26c01f0fe30c | -19.1924 | -46.8308 | 2026-09-19 13:30:00 | GOES-19 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 4252d8fc-268e-3fa2-ab1a-43d3daaab2df | -12.1531 | -46.9707 | 2026-09-19 13:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 160.2 |
| c84739ae-4cb6-3dbf-848b-0c08969fadfb | -7.7842 | -44.8898 | 2026-09-19 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 97.4 |
| f2821929-50c8-32f9-b71a-c07c6ca8ff6e | -9.2414 | -45.9411 | 2026-09-19 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 8231a244-c82f-3dfb-a7fe-a879c94a1599 | -12.4841 | -50.0532 | 2026-09-19 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 92cb0d16-c8fc-3d99-93cd-bc574b22b36f | -11.8549 | -50.0437 | 2026-09-19 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 5cf4bec9-352f-349e-bca6-4fff091e72ec | -14.1542 | -45.1675 | 2026-09-19 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 0cf8c85a-db46-3cf9-af90-1663f221fb8e | -10.5667 | -51.3349 | 2026-09-19 13:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 58c82c94-9c21-3e6c-ace2-16877169458d | -9.0096 | -44.9209 | 2026-09-19 13:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 70c83ba6-d1ae-3810-b825-121d3be841f1 | -9.2567 | -46.2098 | 2026-09-19 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 133.6 |
| d0f0a3b2-7b0c-3713-a0fc-43856a98ec27 | -8.45 | -45.8674 | 2026-09-19 13:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 6c2fdeb5-f127-327f-9720-4e12c0469332 | -7.0448 | -42.0906 | 2026-09-19 13:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 130.9 |
| 20aea00a-5e53-30ac-bfd4-5db9579b8d43 | -12.0076 | -50.0254 | 2026-09-19 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 157.6 |
| 6bbe9663-77da-3310-a618-2058e9e6e048 | -11.0611 | -49.7693 | 2026-09-19 13:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 145.6 |
| 4013f962-ed40-3ace-8da1-ae174579a8cc | -12.5952 | -49.1046 | 2026-09-19 13:30:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 157.9 |
| 72e52936-e38c-3d08-a378-b6c1b93d1319 | -3.4455 | -58.2134 | 2026-09-19 13:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 88.1 |
| fcb38d14-7ec4-3a03-bfcf-84c762143228 | -10.9133 | -50.8549 | 2026-09-19 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 9c19490e-c0d8-3df5-97b3-c8fc1cfed3e1 | -5.6408 | -43.392 | 2026-09-19 13:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 62f09c63-335f-341b-82e1-5cacd5c80ec7 | -12.0082 | -49.9822 | 2026-09-19 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 42de5474-629f-3b2c-a493-5ccbbf22f400 | -3.331 | -59.8292 | 2026-09-19 13:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 0c0859ed-f512-39f5-a0a0-2356dfa877c7 | -8.4296 | -54.7262 | 2026-09-19 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 130206e6-3a21-37bf-92c5-4827346f42ae | -10.8469 | -50.1795 | 2026-09-19 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 224.5 |
| 1cca255f-5b91-3099-a532-98ee193aed4f | -10.8466 | -50.2009 | 2026-09-19 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 226.9 |
| 4c402efc-37fd-320c-b39c-a81c88e9809b | -9.0358 | -48.727 | 2026-09-19 13:30:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 76fd6ffb-4ae8-3e73-9c5d-2966e783c110 | -7.8598 | -44.8595 | 2026-09-19 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 6141aeb6-726b-3d57-a953-008e163161db | -10.8279 | -50.1815 | 2026-09-19 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 174.8 |
| 5afca316-e6ec-3272-b3d5-342cb8d95b90 | -6.2585 | -41.6617 | 2026-09-19 13:30:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 206.6 |
| 55b0261f-412b-30c4-9607-745ac8a3d42c | -6.2236 | -45.1853 | 2026-09-19 13:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 77924066-6769-392d-bc7f-e3c6df0774ec | -6.2582 | -41.6858 | 2026-09-19 13:30:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 166.5 |
| ef0aeb57-6625-3889-8e76-326501423661 | -7.6087 | -45.4298 | 2026-09-19 13:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 238.8 |
| 5099707b-951b-35d9-b165-ed7cc2700499 | -12.4844 | -50.0315 | 2026-09-19 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| a1da9b84-2367-3d26-8830-35b477c003e8 | -11.1035 | -49.4623 | 2026-09-19 13:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 129.9 |
| c66ac2d9-6a43-3787-bee4-60117f9bc9d1 | -6.001 | -51.7903 | 2026-09-19 13:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 3a5079b4-3f3c-3376-ab55-67d8b4b7465b | -12.1339 | -46.9734 | 2026-09-19 13:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 149.8 |
| f32e31fe-f7d7-3748-97d1-47732f023c76 | -8.4503 | -45.8448 | 2026-09-19 13:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| fa963a7a-589a-3507-a2c0-9dc1b90d8103 | -4.5585 | -42.9758 | 2026-09-19 13:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| a07d02c0-78f0-3ada-a8e8-189b636d68b1 | -10.8282 | -50.1601 | 2026-09-19 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 0d022135-28de-3b16-9a9b-912bdb66dd26 | -3.4454 | -58.2327 | 2026-09-19 13:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 354368c1-61c8-3b9f-ae82-346d19003992 | -11.8742 | -47.6348 | 2026-09-19 13:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| f439b177-97e0-398b-baff-cd409581a339 | -11.1228 | -49.4384 | 2026-09-19 13:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 142.7 |
| c1a63359-6821-36c3-b208-a60e91503a46 | -10.6703 | -50.6465 | 2026-09-19 13:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 981d452c-ee8a-3830-887d-82030f5fee9f | -11.949 | -50.1186 | 2026-09-19 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 151.0 |
| 55fc67da-4684-3be9-bc7c-9b60fab4c306 | -12.0267 | -50.0231 | 2026-09-19 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| bb0a1d34-0801-33d6-9a42-f9e76c74b671 | -11.9112 | -50.1016 | 2026-09-19 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 535b5df1-ca5b-3ca9-802f-d1a2bc3a6522 | -11.8546 | -50.0653 | 2026-09-19 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 3a087a99-f97a-3c37-8fad-fefbb4e699a2 | -5.6596 | -43.3906 | 2026-09-19 13:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 89b3a181-c7d3-31b7-9a08-0eced7f060fe | -8.7919 | -48.6851 | 2026-09-19 13:30:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 248.8 |
| c96628c3-f833-3325-83a6-d613cd2fac00 | -11.083 | -48.2875 | 2026-09-19 13:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| ec3be702-5fb2-35a8-a2af-94f36220cec3 | -11.1369 | -54.0251 | 2026-09-19 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 676.2 |
| 722376ec-7c40-3249-8d8e-36f0a2142c89 | -8.7731 | -48.6868 | 2026-09-19 13:30:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 145.6 |
| cbe7f64f-aed6-37a6-a285-e5f3565f39bc | -7.7629 | -46.7389 | 2026-09-19 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 121.2 |
| b9c00782-0f40-3271-b727-fb798b72be86 | -10.567 | -51.3137 | 2026-09-19 13:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 109.0 |
| 9171477a-e398-3a30-9b4e-cd6f9ba1e5ef | -6.2773 | -41.66 | 2026-09-19 13:30:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 101.7 |
| 46826ff8-50a1-360a-bbf5-1982161cfb2a | -3.3494 | -59.8097 | 2026-09-19 13:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 3489e66f-0b47-36ab-bec6-feda0ac72491 | -11.234 | -48.3571 | 2026-09-19 13:30:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 7246ad4f-bd4d-3ab3-bc88-6ee7599db1b1 | -5.9344 | -42.0966 | 2026-09-19 13:30:00 | GOES-19 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 110.7 |
| 82c7ab2f-13ff-332a-9916-f1848fba09ea | -12.5761 | -49.1071 | 2026-09-19 13:30:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 1b0b67e7-0f0d-3132-8b0e-93004a8bf72b | -3.3311 | -59.8101 | 2026-09-19 13:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 127.3 |
| 75c5568d-c24c-33c1-a6e7-51d5e4931c4c | -11.4164 | -51.4583 | 2026-09-19 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| a93cac0f-9f74-3091-b9b8-0e7e2eafeff5 | -3.3493 | -59.8288 | 2026-09-19 13:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 42a8246c-7f21-3d06-ab35-2ca5aa387e42 | -11.3355 | -43.403 | 2026-09-19 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.0 |


[Clique aqui para ver as próximas entradas](README110.md)
