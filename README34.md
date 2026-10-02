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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e2fe339-b254-3c0c-838f-84ab40970f53 | -3.2951 | -53.8395 | 2026-10-02 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| cde342f8-1249-3e8c-8e64-bb446531e271 | -11.1424 | -44.6029 | 2026-10-02 04:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 59d0133e-c638-3392-82e8-1d721810374a | -3.1299 | -53.7431 | 2026-10-02 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 65d0a95e-88f1-3052-91b8-89a75559adff | -2.0394 | -56.8593 | 2026-10-02 04:00:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 6101502b-bfe8-3453-853b-4bf223e6b75a | -2.0577 | -56.8591 | 2026-10-02 04:00:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 02c9450a-bc5a-30bd-be79-4018693dc2a3 | -11.7926 | -43.5689 | 2026-10-02 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| c5fdc2af-c778-3006-962a-40039155f64c | -11.6575 | -43.6136 | 2026-10-02 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 188.5 |
| b8684eb6-9f83-364e-91fb-141bf79d1b0a | -7.3846 | -55.2124 | 2026-10-02 04:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| d03eb313-0f25-36e3-903d-7055b9e45ea7 | -2.0394 | -56.8593 | 2026-10-02 04:10:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| d8b521ac-498e-34de-806d-4840ad836d98 | -11.1611 | -44.6234 | 2026-10-02 04:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 8b5c02a7-7989-39b9-a8fe-f4848cc7e6ce | -11.1424 | -44.6029 | 2026-10-02 04:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 3b21a1c1-d51f-384b-9d85-a192bbcdee66 | -11.142 | -44.6261 | 2026-10-02 04:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| b9a780bf-4cd6-3394-8a6a-e9b68c2fec2b | -11.6771 | -43.587 | 2026-10-02 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 99d7630e-4c06-3ab2-b2f7-304ebedb9b06 | -11.7733 | -43.5719 | 2026-10-02 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 5742765f-18e8-3fea-b2f2-6b9e41a00765 | -3.1299 | -53.7431 | 2026-10-02 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 1a4067a0-bc71-3cf0-8c58-c0d9d8736ae3 | -11.6767 | -43.6106 | 2026-10-02 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| d026826a-dcc4-39b7-8d47-130ec2a6220d | -11.1615 | -44.6002 | 2026-10-02 04:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 122.9 |
| faaed775-8aca-31e8-b364-55053f774f79 | -3.1655 | -54.0844 | 2026-10-02 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 21bb9a42-c323-3c70-8caf-ac6f10751637 | -7.4033 | -55.1913 | 2026-10-02 04:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| beeff448-e3f2-3d87-a764-aeee36cdb5b0 | -4.2676 | -50.7506 | 2026-10-02 04:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 0d0daac4-65f5-3b8a-b9ae-1b545e9a04cb | -7.4031 | -55.2114 | 2026-10-02 04:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 133.0 |
| 0d3f7a36-36f2-3829-a507-7afe8a1288e2 | -4.4507 | -47.9112 | 2026-10-02 04:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| eb2cc3c5-9597-3fe3-a322-24b12e49bcca | -5.7563 | -45.152 | 2026-10-02 04:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 8205f67e-97dc-3c2d-ac83-65d2db66a4fb | -11.6579 | -43.5899 | 2026-10-02 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 309.8 |
| 45288085-7acf-341a-9d9a-17fb192fc29d | -3.1483 | -53.7426 | 2026-10-02 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 67dfb38b-c865-36ed-8f7a-0acfb9b89082 | -11.7541 | -43.5749 | 2026-10-02 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 53712acb-4af5-3614-a073-879b3d885fa1 | -3.1299 | -53.7633 | 2026-10-02 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 8606bcba-f4cb-354c-b98b-13ad820b3680 | -2.0577 | -56.8591 | 2026-10-02 04:10:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 33df43a1-bd42-36fd-8ede-cdc360cab0d6 | -3.2767 | -53.84 | 2026-10-02 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| cfe1593b-50d6-3c8f-b411-81cf843f37ed | -3.2951 | -53.8395 | 2026-10-02 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 7d91a50f-5aff-37fb-aa9e-e21f40e149b7 | -3.295 | -53.8597 | 2026-10-02 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| f3a521d0-8169-3d88-ba38-e96d36d3aedd | -11.7348 | -43.578 | 2026-10-02 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 86647899-6b3c-34b6-b42d-1250c8e32a63 | -1.45335 | -48.91593 | 2026-10-02 04:12:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b972380-8747-34f0-9430-c64c7a5b5423 | 2.55239 | -50.95588 | 2026-10-02 04:12:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 81a9d31f-9ed9-39c3-abc5-4303429d7260 | -1.32929 | -47.96097 | 2026-10-02 04:12:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9c3c6b2-ea30-35be-a5b6-c8de85c64471 | 2.55233 | -50.95895 | 2026-10-02 04:12:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03910248-1f62-3218-b1c1-71cf84d13e70 | 2.35969 | -50.76146 | 2026-10-02 04:12:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 70fe500a-8270-3119-8c54-ec121034b9ee | -1.45936 | -48.91089 | 2026-10-02 04:12:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc07a70b-4d12-3632-859b-d76287930cb3 | 2.55163 | -50.9542 | 2026-10-02 04:12:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 848eefe2-a827-3988-90f4-447e01c7cb47 | -1.16753 | -49.14236 | 2026-10-02 04:12:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3246888e-1267-3ba8-80ce-5c8316e764c3 | -0.9385 | -47.55362 | 2026-10-02 04:12:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 24158eaf-419c-3465-81ba-75487339609c | -1.45383 | -48.91299 | 2026-10-02 04:12:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e9a8d9f-929c-3af6-98c8-94fe770b3757 | -1.16881 | -49.14461 | 2026-10-02 04:12:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a518cd78-7d46-33a6-a1ad-41757d74c6c4 | -0.37863 | -51.75539 | 2026-10-02 04:12:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7d2c3e14-21c3-39ed-8b90-d120a07b4500 | -1.45984 | -48.90795 | 2026-10-02 04:12:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bca8462f-0cd4-386c-a066-4a8e82b1f9c2 | -1.15819 | -49.13451 | 2026-10-02 04:12:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 969ff2bc-84e0-3671-9fa4-7361dd2ac887 | -0.24968 | -48.49149 | 2026-10-02 04:12:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3184cb3-dceb-3123-91a1-033c7b08eb2d | -1.16002 | -49.13373 | 2026-10-02 04:12:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7fd8dbae-3226-3fa5-8364-15dc1ccbfdd2 | -1.15951 | -49.1368 | 2026-10-02 04:12:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 572f7c61-b6ef-37af-9b7c-fe767dc09894 | -0.99666 | -47.65474 | 2026-10-02 04:12:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 96fb6ea7-393e-38ec-a687-166186d8b0e5 | 2.55312 | -50.96062 | 2026-10-02 04:12:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1471d1a3-29f1-366c-aa93-a0a0222cd530 | -1.22109 | -49.01878 | 2026-10-02 04:12:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23c36492-79ed-3518-9eba-48de110eb5ee | -1.28856 | -46.60736 | 2026-10-02 04:12:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 068918cb-8ee0-325d-a160-2473233394af | -0.24468 | -48.49068 | 2026-10-02 04:12:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d7a9b297-aa6f-3466-9575-3c5a8d16eebb | -0.25014 | -48.48863 | 2026-10-02 04:12:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a33a2cc-7cbe-358c-9ac7-7deb7e661e68 | -7.51404 | -47.33407 | 2026-10-02 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1586b297-399f-3dd6-b14e-e0b44e2b5133 | -7.82039 | -55.12252 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0d762ef3-349c-32ea-8e94-c706295e3d0b | -7.59134 | -40.81073 | 2026-10-02 04:14:00 | NOAA-20 | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1fc340cf-0c7f-31cc-b224-f9890f1e878a | -4.25078 | -50.75508 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ece9f3c7-a0d9-3eb0-8f3a-1694a268db15 | -7.19894 | -46.54673 | 2026-10-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ecde3166-89c0-3e8b-8135-9200b91274d1 | -5.7671 | -45.16472 | 2026-10-02 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dbdfc441-92b8-3da7-a2ba-fa4b4992f33d | -9.12405 | -44.73925 | 2026-10-02 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9673ceb-8a6d-3543-9f57-26acbad23768 | -4.27029 | -50.73995 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8622e8ce-5614-345f-865e-4d5e090168ce | -7.05092 | -55.64062 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2de3abeb-1018-307d-aa6c-dd460c5e1de9 | -6.34448 | -43.36971 | 2026-10-02 04:14:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cba094b7-ad25-3104-948d-7756cbaa105b | -3.17003 | -54.10756 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 50ad734c-0aae-39f9-b254-cf1ef4fa4f5a | -8.37386 | -45.37892 | 2026-10-02 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6bd800c1-b816-359f-8712-8e521712e13a | -8.61869 | -45.40004 | 2026-10-02 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c423cc00-b313-3943-9a72-a7e48f3fbd15 | -6.07658 | -53.30526 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc24d726-a81b-3a32-ac9a-1ab6614b9edb | -3.06863 | -49.36784 | 2026-10-02 04:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5eee6928-9ad2-361a-b82d-26296d8bf631 | -7.40816 | -46.61858 | 2026-10-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d40e4fe-b45a-3c4a-b29a-e4f05d14967b | -7.75091 | -54.80683 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cad4df06-de64-3f1f-b644-726b578a952f | -7.04387 | -55.6393 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f692a5fa-1208-393a-aa18-035a27681ff0 | -7.4161 | -55.59277 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 894bf64d-0788-3222-a365-ed1b1dafa144 | -5.1385 | -49.87198 | 2026-10-02 04:14:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3bf01397-b695-3ca9-9430-065f657cc519 | -7.39572 | -55.21379 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 0117092d-74a4-357b-bf14-35505f5f76dd | -6.23747 | -53.15203 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9c9126f7-639f-38b3-bb55-c398e1a548c3 | -9.84488 | -44.85551 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b646acea-00a1-3102-aa98-3c974ada4938 | -4.27815 | -50.75965 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3b893d6-4b36-32cb-8c6f-dcb502250c45 | -8.75064 | -44.80802 | 2026-10-02 04:14:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38df9d19-caf3-35d6-b925-f09e06062199 | -8.16508 | -54.80848 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36c3a601-887b-3faf-9e7b-bfc62f6db886 | -6.44432 | -45.96658 | 2026-10-02 04:14:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 117c0382-4336-31b0-adc2-91a5b365d7be | -9.44164 | -46.1273 | 2026-10-02 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 86bd577c-39ca-379b-aa4a-dabe7a3523df | -9.52025 | -45.32444 | 2026-10-02 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9de52c3b-9df4-32b2-b153-187bde3a8cb5 | -5.76262 | -45.14589 | 2026-10-02 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 61fa14ea-5c0c-3e5b-8ac4-0768e41bcda5 | -3.28541 | -53.84237 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 82f39dbd-05b7-34e7-be95-e73284aace6b | -9.50752 | -45.33484 | 2026-10-02 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4629266-ecd2-3475-8203-4aa59983da2b | -7.50931 | -47.33704 | 2026-10-02 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e7f1cafd-1961-3999-a3b5-15f2012955aa | -5.85978 | -47.42352 | 2026-10-02 04:14:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b6000672-fcfd-3d2b-8212-1af7b0614c16 | -4.24715 | -50.74363 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e339a6e-69eb-3a70-bf0a-c7b9c37b0178 | -6.71606 | -45.57243 | 2026-10-02 04:14:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 523bfa8b-883c-32f1-85d0-9d2ab7a9d518 | -7.74338 | -49.20506 | 2026-10-02 04:14:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 8116f2b1-b9b5-3ee1-b123-7c3cb67d9bd9 | -6.90746 | -43.68136 | 2026-10-02 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ab5b2f2e-9ab6-3c05-91be-6a5839d2a3ad | -8.40986 | -47.63532 | 2026-10-02 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b4673a13-0d21-351b-bdc4-5dce93e4f958 | -7.83265 | -55.13157 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 468047e6-f61c-372c-a6c2-eaf084e9a539 | -4.26721 | -50.75775 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a831926f-37c3-3b87-9296-7cc25f85b632 | -5.74169 | -43.27795 | 2026-10-02 04:14:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7d6792b0-8846-37fa-ab2d-16896331afec | -7.38872 | -55.21333 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| cbbdc330-e89e-3e8e-8fbf-c5cbd45bd4a0 | -6.1849 | -44.34128 | 2026-10-02 04:14:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2ee9bac-0c5b-3a45-9637-48cc329cb741 | -4.29333 | -50.7696 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README35.md)
