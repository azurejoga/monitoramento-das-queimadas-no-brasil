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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26bdff44-29cc-300b-8dc3-e65a34c618e4 | -10.93274 | -54.08018 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9bf4ce61-ec01-3667-ab70-be25c976f5a6 | -10.59936 | -47.7534 | 2026-09-16 04:59:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eb74acf2-d4de-3d25-886d-9e0714aa4787 | -9.80376 | -46.495 | 2026-09-16 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 41fd1b91-0eed-3098-a01b-75eadd5df5d8 | -15.35338 | -48.11065 | 2026-09-16 04:59:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f661a75f-d5b2-303a-9933-70fa294093e2 | -12.61858 | -50.79136 | 2026-09-16 04:59:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1911e65-796f-3562-a76e-ed1255d512a1 | -12.40915 | -48.47395 | 2026-09-16 04:59:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9f4f0c33-3099-32a7-9adc-9a030e42e623 | -10.77484 | -46.21229 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ddf0e4af-1934-3821-960f-dd5c508016f6 | -11.26924 | -54.12453 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a724ecfe-82b7-3239-813e-d9ab86422927 | -12.38292 | -51.41753 | 2026-09-16 04:59:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa144817-954b-3526-bd42-470f3c65ff74 | -15.04094 | -48.56178 | 2026-09-16 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 56125ae2-f824-3cd7-b2c3-231416b7fdfc | -10.46032 | -44.94754 | 2026-09-16 04:59:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9ec69070-3a5b-395c-b82e-045be74dae8a | -11.3214 | -47.2409 | 2026-09-16 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddfe49e7-7d65-3d0e-8818-fa3ca703c201 | -12.13825 | -57.18381 | 2026-09-16 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 24bb1a1f-eed5-3667-a0f2-b52d35e48080 | -13.39941 | -57.02033 | 2026-09-16 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d4d29d6-9d58-34c8-be0e-1e8acf1ec00c | -12.06159 | -58.04313 | 2026-09-16 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1bd9604-4d7c-3718-9a09-bbaadcd9d5f1 | -9.80257 | -46.50447 | 2026-09-16 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| fd2c8096-43c7-378d-a4d3-2705e754bf01 | -11.20391 | -42.82317 | 2026-09-16 04:59:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 486ef301-d45e-32a7-b44d-6e775b6d5040 | -12.11229 | -57.19459 | 2026-09-16 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0d770116-8143-3c0d-ad94-e789c363f20f | -8.54376 | -54.69949 | 2026-09-16 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c527fa16-4cf0-3e36-8a40-b63242753bbb | -11.31639 | -47.24039 | 2026-09-16 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b81c883-aea8-30a9-bb0f-e2e9ea8f18a8 | -9.81158 | -48.91534 | 2026-09-16 04:59:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 69d7e65c-9763-3ced-a341-1f7830a07f57 | -9.72749 | -64.90311 | 2026-09-16 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2234b0e4-5fe2-3a5c-844a-6271abbb6d25 | -12.77201 | -51.22063 | 2026-09-16 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 24feb899-612f-305f-8d86-b1e9ed001aaa | -10.84844 | -46.1746 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| da4d51b7-9524-3b3e-9347-b46e57e57185 | -12.38745 | -51.41324 | 2026-09-16 04:59:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71eaa5f7-edae-32a4-96ff-8dd43dc38ad3 | -12.41075 | -44.54913 | 2026-09-16 04:59:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9c9981de-bba5-3835-8849-547363e96096 | -10.90387 | -46.2913 | 2026-09-16 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 132d0201-fc08-3b16-a858-5055f71eab7f | -11.98146 | -52.46283 | 2026-09-16 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 57b791b3-7e5e-3e5f-a644-b78789afcd16 | -9.44662 | -56.92693 | 2026-09-16 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c25a7072-6c73-3270-acde-023cac093204 | -10.90259 | -46.29621 | 2026-09-16 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 26ec03dc-d0a6-3c3d-8e3f-eac96215923d | -11.19729 | -42.82228 | 2026-09-16 04:59:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 79a536e2-f560-3215-8492-f54c99f26ec3 | -12.12022 | -57.18836 | 2026-09-16 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 847f37e1-d654-355b-928b-f7f71c8ac532 | -13.55991 | -43.5246 | 2026-09-16 04:59:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b3dce242-bf10-3b67-a9d3-b73afa231e70 | -12.63398 | -50.76828 | 2026-09-16 04:59:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7dfb8dff-5fc5-3cf1-8b09-ea3bccea5a59 | -10.89626 | -54.01195 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d629a6b-fa76-37f5-91d3-3396f668736c | -9.05787 | -65.92935 | 2026-09-16 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0b63db90-5444-38a6-9c46-b2a0aa32f67e | -9.91992 | -60.46491 | 2026-09-16 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f37e0d0-3544-3927-83e2-68499a12e4a9 | -9.59918 | -55.10584 | 2026-09-16 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 64cdb9d1-60d8-3f09-9a96-27349e9bfa0c | -10.40106 | -48.64016 | 2026-09-16 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1b69a09f-b972-34fb-a771-24b1e1330dfd | -9.70426 | -52.0098 | 2026-09-16 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 956274d8-e7ec-35ee-86ac-ad0a975b33fb | -10.80575 | -46.18208 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc1f52ff-f135-31c2-af0a-9d1c529ad285 | -12.77133 | -51.22567 | 2026-09-16 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| cb3a9464-fdb6-305d-ad48-b8f095ba8d47 | -9.76456 | -46.57486 | 2026-09-16 04:59:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5582f40a-f94a-3ff0-b03c-5aa92afabc93 | -9.84789 | -48.35966 | 2026-09-16 04:59:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d3615301-0ec6-391a-a391-17bfe089bd12 | -10.47001 | -57.91365 | 2026-09-16 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 139f27a6-9b71-31db-abb5-959beaa91578 | -13.75498 | -48.79198 | 2026-09-16 04:59:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 9e6f3cd5-c70e-33da-8234-50370357cb3b | -9.80033 | -46.50168 | 2026-09-16 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 02aaebf9-d6e1-390d-9418-cb04e83a9320 | -12.61906 | -50.78782 | 2026-09-16 04:59:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f484f70f-8523-3e2f-8ab7-f039630504e7 | -9.09936 | -65.93695 | 2026-09-16 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c9777099-3d05-3045-bedc-6ffa698782ec | -10.65948 | -58.76621 | 2026-09-16 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 80a11368-f4cc-375f-a416-8f8f44fc5026 | -9.02367 | -61.01567 | 2026-09-16 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ccb65760-a67e-3d59-a905-a42210acb13a | -12.22194 | -47.12988 | 2026-09-16 04:59:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e808ba9-b054-338f-84c6-7deffeb0b759 | -9.72707 | -64.90338 | 2026-09-16 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.2 |
| cfea6563-f167-369b-bbae-751258045518 | -8.85151 | -62.36202 | 2026-09-16 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac8bce6b-a67c-3c86-8e0c-3e62a6b7bee5 | -8.60191 | -64.09692 | 2026-09-16 04:59:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5c851fe7-1c96-3b53-941d-10dd66ff18dd | -11.37218 | -43.94442 | 2026-09-16 04:59:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67613486-a887-36b8-928e-7d3ff0787fa7 | -10.90296 | -46.29317 | 2026-09-16 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 54f46401-9cde-3319-b2dd-dbef19d78344 | -10.4055 | -48.64109 | 2026-09-16 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f0606ccf-5654-3305-9303-7e1cb3101ac9 | -9.72573 | -64.91068 | 2026-09-16 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 35ffb605-cc9c-3895-9626-15967a50b77b | -9.79516 | -48.80964 | 2026-09-16 04:59:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| aaa3368a-7b67-369b-9c47-94c3b39125b8 | -11.79075 | -46.59188 | 2026-09-16 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a34199cd-b465-3c8f-b540-cdf00c7edf6e | -9.85244 | -48.3601 | 2026-09-16 04:59:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e9ee65d4-459b-39d8-95ac-6a142f857608 | -11.16893 | -42.7957 | 2026-09-16 04:59:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6476b841-4edb-33ef-abaa-491df2daf19e | -9.25274 | -60.28189 | 2026-09-16 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1efd5567-54db-31fa-b8ba-d96e91b35712 | -9.3942 | -60.31043 | 2026-09-16 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a85f2d0e-a7db-3cfc-8398-62d3b4f6b7f1 | -9.79048 | -46.49708 | 2026-09-16 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3aa73ba3-5f4e-3347-8c62-17553ac175b8 | -11.24777 | -43.44043 | 2026-09-16 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a3875780-bd70-33bd-9b5d-191f2edd3082 | -10.41209 | -48.66008 | 2026-09-16 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80639cdc-ad74-384c-a745-6924864fa273 | -12.31832 | -47.96264 | 2026-09-16 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 493b23db-0fdb-35d7-8bd3-fe5484210e90 | -11.34707 | -47.31934 | 2026-09-16 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a3c4419e-2c5b-3385-b1fd-4e44a767b2c6 | -10.792 | -46.20491 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d094d919-b557-3d03-aab5-a25dab7db2ba | -9.86217 | -48.35641 | 2026-09-16 04:59:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a7298c5b-9aa1-36ba-a7a0-88d60ad9664b | -12.31767 | -47.96789 | 2026-09-16 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 702a9806-0f2d-3be9-8799-84525e0c47af | -9.13338 | -65.843 | 2026-09-16 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3207199c-f7ff-3dd8-9a50-7663d44382d5 | -11.19128 | -55.03421 | 2026-09-16 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d1cc9fc0-4a11-3f10-a5d6-8270d26d80f8 | -9.06888 | -65.93604 | 2026-09-16 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d12350d2-b740-3b8b-a291-e86f147c12e8 | -9.81735 | -48.91394 | 2026-09-16 04:59:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 007f9f5d-0f6d-30db-9aa9-f60e589dd308 | -10.87553 | -54.01242 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 909efa26-0dea-397e-b1cf-8a2ca4a3e6b9 | -10.59359 | -47.75721 | 2026-09-16 04:59:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4e92943b-66b0-367e-ad10-41082c27979e | -10.37195 | -45.12998 | 2026-09-16 04:59:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 41b035ba-710e-33f4-a888-aa318ed462e7 | -8.36844 | -54.7317 | 2026-09-16 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39a943c8-b8c9-30f2-b13a-5f9ff023fa31 | -9.62931 | -61.82316 | 2026-09-16 04:59:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f18c9223-0366-3173-9ff8-845906d9ce39 | -9.14671 | -51.57253 | 2026-09-16 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8463f0ee-48d8-308c-8c37-b3a4797871de | -9.57367 | -46.59317 | 2026-09-16 04:59:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 26651712-8015-346e-9001-8d098b4d0810 | -13.39259 | -57.04135 | 2026-09-16 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dce125eb-09fc-351d-a461-24c903f9363f | -11.89108 | -43.81807 | 2026-09-16 04:59:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 5f0b2357-6a95-302c-9a12-d24d41aa1f7a | -10.82262 | -46.1773 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 504a9def-c91e-37de-9773-efbfdd0a12bf | -8.37336 | -54.72182 | 2026-09-16 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 033838ee-cea9-353b-94b8-e52463c4d7be | -9.26641 | -48.53901 | 2026-09-16 04:59:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac77e779-186a-3ef9-8ac2-f05771046337 | -11.31602 | -47.24334 | 2026-09-16 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a28b0588-45ad-37e2-9109-8b9479de40cc | -9.7913 | -46.49085 | 2026-09-16 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58b53b50-4d41-3c53-8348-311a32e35ec6 | -13.63255 | -45.97367 | 2026-09-16 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa12a9f0-b556-3102-a62b-e241afe2a548 | -13.37563 | -57.02386 | 2026-09-16 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 88a68388-716c-3833-b797-2db683af8e94 | -9.07291 | -61.01149 | 2026-09-16 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08ed14c0-28d3-3640-b988-a9a252eabb2d | -8.83567 | -62.48004 | 2026-09-16 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 95fec5ef-9c2a-3d1c-94f5-b6ce42ac224b | -9.49264 | -56.74853 | 2026-09-16 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1684e10b-9b62-3c11-bd67-ff3e285ee5f6 | -10.36627 | -45.12926 | 2026-09-16 04:59:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8fdd0744-a084-3bc1-a781-726c528075fb | -12.11844 | -57.19939 | 2026-09-16 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d14d1622-13f7-33c8-bbe2-33b364cf4bc3 | -9.86537 | -49.82179 | 2026-09-16 04:59:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b74352ee-cc91-3b8d-b152-83523afaf5ee | -10.83053 | -46.18805 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README48.md)
