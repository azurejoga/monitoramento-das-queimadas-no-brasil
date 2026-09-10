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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6365861-d5bd-3311-bde4-d6fb1b99dbea | -14.91532 | -44.67187 | 2026-09-10 04:27:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6cf66380-ab19-303d-8720-4d1fe867be54 | -16.61656 | -43.32158 | 2026-09-10 04:27:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06de6040-82b5-3e73-b5d7-4f9ec69a4251 | -10.67246 | -45.99829 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ec0dbf4e-84b6-3209-82c4-ca807645b975 | -12.63863 | -47.08807 | 2026-09-10 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4f405697-bd2c-370b-a349-9aec54739619 | -10.72092 | -48.96168 | 2026-09-10 04:27:00 | NOAA-20 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15c431a7-4aa5-3268-9dce-3918b57b24be | -12.84939 | -44.34412 | 2026-09-10 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 50a65169-ec57-39f7-8f2c-6eea16d54c87 | -12.82593 | -44.33654 | 2026-09-10 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| d2311a85-07e5-37d0-8ecd-3b707178f915 | -11.85696 | -44.86754 | 2026-09-10 04:27:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26cde014-2132-3c9b-9701-4cc00181b5bd | -12.20212 | -49.39354 | 2026-09-10 04:27:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 921055a6-b2f2-3303-bd2a-5c4a43d78cc9 | -10.26467 | -45.20445 | 2026-09-10 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41fdbf31-b13f-31a8-989b-9c7009c8eb1a | -12.64861 | -47.08974 | 2026-09-10 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2d361e8-c6f9-3b21-9912-efaafc9b2c8e | -12.85054 | -44.3365 | 2026-09-10 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 4c0293d3-14ae-3b7a-b39f-f12e6b4fb0be | -12.83909 | -44.34251 | 2026-09-10 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| c446cc96-d843-349a-a459-551d54e13cb2 | -2.7332 | -57.6077 | 2026-09-10 04:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 21761e53-753a-3a38-a55b-6fc273878044 | -3.4242 | -59.2151 | 2026-09-10 04:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 54e2438d-3eb2-3bc3-99fa-cca768679d08 | -2.7331 | -57.6271 | 2026-09-10 04:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 452ce8cf-c6cc-3ba7-974c-c02e2e73535d | -29.72938 | -53.87167 | 2026-09-10 04:32:00 | NOAA-20 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 6796dea1-16d6-337a-9e39-9f7636b52f29 | -2.7331 | -57.6271 | 2026-09-10 04:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 361c918a-2ceb-33f2-b7cd-61c1a356504a | -3.4058 | -59.2347 | 2026-09-10 04:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 600d8878-b906-3df5-8752-270a3d5c0227 | -3.4241 | -59.2343 | 2026-09-10 04:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 57791a44-d5fb-327c-80f9-533488f30fbe | -3.4058 | -59.2347 | 2026-09-10 04:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 566aed9f-ca73-3a8a-8e06-cc5922872d0f | -6.5453 | -62.8914 | 2026-09-10 04:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| cdffeaf2-f131-38ce-b60f-ac0065d050a7 | -2.7331 | -57.6271 | 2026-09-10 04:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 3b863aed-7913-34fe-b083-7284ea21e67e | -3.4241 | -59.2343 | 2026-09-10 04:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 55b9a25e-dd70-35c6-bc58-4b2eab19daca | -2.7331 | -57.6271 | 2026-09-10 05:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| cf356c6d-d369-3515-b9a5-34fd341daedf | -6.5637 | -62.8908 | 2026-09-10 05:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| fd050055-48e3-3a37-a4eb-460f8adaed84 | -3.4241 | -59.2343 | 2026-09-10 05:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 2eab9e49-1a45-3e64-ab90-027615517a7f | -3.4058 | -59.2347 | 2026-09-10 05:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| f519a8af-ecce-374d-a3ac-028258e3b2d8 | -12.83 | -44.3 | 2026-09-10 05:00:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2f3b1c1f-7cdf-3d4b-a797-2a2058303557 | -12.83 | -44.35 | 2026-09-10 05:00:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 030d0689-7989-30bc-aa05-b3226f290e96 | -12.86 | -44.36 | 2026-09-10 05:00:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| de670bd4-6bd9-3987-82d1-47babbbb9abf | 1.00572 | -51.10618 | 2026-09-10 05:08:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 31169016-1527-3192-9bc4-d3665be8eef3 | 1.36932 | -50.68392 | 2026-09-10 05:08:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e322bef1-42bc-33e3-a7ad-4ac13ed3a11f | 2.50962 | -50.85175 | 2026-09-10 05:08:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f1c18cb6-d788-3237-ac4b-c8ceafe7abac | 2.51435 | -50.85617 | 2026-09-10 05:08:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c54002e8-13b1-3f52-b628-fb622c8e2028 | 1.00967 | -51.1055 | 2026-09-10 05:08:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 29f6b28b-bb42-3f64-9154-5eff1f0a42ba | 2.51042 | -50.85678 | 2026-09-10 05:08:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ceab851f-ced2-3d2a-a7f3-070f945126b3 | 1.36527 | -50.68457 | 2026-09-10 05:08:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7419a59f-25c2-390c-b882-4c22d14c7602 | 1.00652 | -51.11127 | 2026-09-10 05:08:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 070192c3-39d7-3d5a-9274-976de287237c | 2.49954 | -50.99108 | 2026-09-10 05:08:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fd6a89f-42ac-305d-bc1c-bc9d4dace2a6 | 1.26226 | -50.71863 | 2026-09-10 05:08:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ffdfc62-7c71-3d06-801a-3adbc17450e0 | 2.49564 | -50.99171 | 2026-09-10 05:08:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e86160e-3055-31ef-bb27-0088726e2722 | 1.36583 | -50.68812 | 2026-09-10 05:08:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f3330fe-8a6e-35d7-9ec0-c8b8de6e5aaa | -3.4241 | -59.2343 | 2026-09-10 05:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| e7bfb9ee-3f5f-34ef-92cf-fa7953002362 | -3.4058 | -59.2347 | 2026-09-10 05:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 2f7004bd-3fbd-366c-99af-92f81f75ec67 | -6.5453 | -62.8914 | 2026-09-10 05:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| f7b18e4a-4ae5-32d5-848f-5cc0bd67c19a | -5.36977 | -56.02397 | 2026-09-10 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4656a272-b11c-3e0b-b95c-eedba0659782 | -5.75879 | -45.08743 | 2026-09-10 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 48b8b2d6-5fee-3897-b084-bca756b0b603 | -3.43689 | -59.25223 | 2026-09-10 05:10:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 362e43f3-fcc8-3a67-9db2-942307df9262 | -3.35373 | -58.18224 | 2026-09-10 05:10:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bfa2a231-90e7-3568-a20c-782f759e1df4 | -3.54373 | -48.18175 | 2026-09-10 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a914b7b-2dce-3930-b166-69a658b67491 | -4.00644 | -51.02724 | 2026-09-10 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7ab5c52-6370-369a-9607-01031f02558f | -7.50294 | -45.26816 | 2026-09-10 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a4c0ee9-5743-360a-b54e-e3181dad449c | -1.70612 | -55.02555 | 2026-09-10 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0a78681-176b-3cbe-9986-f82eb5117a6e | -3.40439 | -58.28879 | 2026-09-10 05:10:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f609802-da26-30d2-8949-f2189b86ec7b | -2.94873 | -50.4776 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dfc1eaed-8504-3d16-8626-aee4b12e2532 | -2.94589 | -50.47026 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e6bde62e-00ad-3490-9923-cad179e56903 | -5.28121 | -55.959 | 2026-09-10 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12f80e89-e070-3342-bfe1-9bbb39df2f01 | 0.2453 | -51.45978 | 2026-09-10 05:10:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ef476577-9ced-34fe-9926-4640ba458011 | 0.26566 | -51.43633 | 2026-09-10 05:10:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ac89aa6f-1941-3d67-8f1b-bd3890252e91 | -5.28012 | -55.96613 | 2026-09-10 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26433778-5acf-34ca-a59d-d7592390a996 | -4.38195 | -55.04884 | 2026-09-10 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1858a51-0b79-393a-826b-a05dc448f6db | -5.27395 | -55.96153 | 2026-09-10 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2042c91-f569-3344-bda8-0cbf585e51d6 | -3.67202 | -53.84082 | 2026-09-10 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 480e4d25-8a72-38af-850b-3460b956bff6 | -6.24189 | -51.67249 | 2026-09-10 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f03ab6f0-6bd7-376c-82b5-bd662e3579a1 | -5.60495 | -44.85331 | 2026-09-10 05:10:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| abd11eb9-c0b7-3823-baf3-5e8bc2656e49 | -6.76267 | -44.56708 | 2026-09-10 05:10:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d07527ec-8d63-3c9a-bb5c-8d25928a52ed | -2.73375 | -57.62318 | 2026-09-10 05:10:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 0a6fc990-3a76-3ace-a602-2b7e2a5e575f | -6.10242 | -51.74183 | 2026-09-10 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0330ce83-6af8-3fee-be98-fe491f334a40 | -5.76824 | -45.07256 | 2026-09-10 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 90482def-db3d-3c5e-8540-9b031e2ce9e1 | -1.47501 | -47.27536 | 2026-09-10 05:10:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fb9b37b-32f1-3980-97a0-acd5cff336a3 | -5.77242 | -45.09042 | 2026-09-10 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 91c02857-b731-3784-a778-2d78d50bcc9b | -5.37812 | -46.30048 | 2026-09-10 05:10:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d1e3253-9e08-3656-b4bf-da1884d30bfd | -4.85773 | -56.01819 | 2026-09-10 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| c5faa371-496d-315f-91ea-f584d3ae0f79 | -4.8291 | -55.76615 | 2026-09-10 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3e952f1-bc1f-3e44-a64a-8c9f4ac5ce26 | -4.3791 | -55.04456 | 2026-09-10 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1af2a1ec-e1a1-39a0-98cf-0dbe425b89ed | -3.37819 | -50.40476 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 97e9d447-41d4-3b46-9028-dc8e118865f5 | -6.2504 | -51.67365 | 2026-09-10 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5267e044-f615-3efd-957f-8345217ed5f4 | -2.94256 | -50.45934 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a9dc2984-6882-3847-a600-2f5cfb0cc042 | 0.27505 | -51.41948 | 2026-09-10 05:10:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe3d05ad-c8a4-3aef-a1d6-de730fd4aa4f | -2.9365 | -50.47318 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb1c27a4-2b7f-385b-b7ed-f2eadce81f83 | -2.93377 | -57.9092 | 2026-09-10 05:10:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a8c8e0b7-b5e2-38e6-83c4-504c711df422 | -4.36898 | -47.78176 | 2026-09-10 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 8652fbae-febb-34eb-9f99-97a33a2c55cf | -2.73152 | -57.61568 | 2026-09-10 05:10:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7afb9365-a5e1-34eb-801f-ce28d1ef7507 | -3.43517 | -59.25179 | 2026-09-10 05:10:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4abe435-351b-3117-a25f-2bc6de98302e | -3.95792 | -59.36332 | 2026-09-10 05:10:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 924dba44-7efa-367d-ac2d-b05eb39e4313 | -6.18903 | -55.26978 | 2026-09-10 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a529a00-253e-3c4d-8e6c-68c337a4a08e | -3.9614 | -59.36386 | 2026-09-10 05:10:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80f9bcd4-440c-3ec6-9bc7-1c271638de28 | -6.26299 | -53.11715 | 2026-09-10 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f51b70e3-953c-3d24-9218-c66ad8b21394 | -6.14772 | -51.75638 | 2026-09-10 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2cedf62-d1dd-365b-bf75-796e4aeb2885 | -2.91732 | -54.1106 | 2026-09-10 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 73ee8d20-531a-3c08-b411-857030bb8635 | -2.94903 | -50.47946 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 77e71870-fba8-388c-8456-fa09f131b925 | -3.03648 | -59.16733 | 2026-09-10 05:10:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab3d9600-9382-3bc6-ba69-99c912db29ef | -4.86758 | -47.41035 | 2026-09-10 05:10:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e5e8a68-6a0d-312c-b8be-43535a8635eb | -6.25465 | -51.67424 | 2026-09-10 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7fb05866-aacf-3e49-b4d4-0234c3798e78 | 0.28595 | -51.48893 | 2026-09-10 05:10:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9bf4ebef-a6a0-3e56-93dd-ac8110d4b32a | -5.37032 | -56.02041 | 2026-09-10 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d584bbe8-b61f-32a2-b6c6-6a510e659744 | -6.75339 | -45.47979 | 2026-09-10 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9c07cc8c-1f6e-3f59-a811-4f392c11c86a | -6.14406 | -51.75189 | 2026-09-10 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b472b4d-394c-303e-a569-4b6c60ad3de8 | -6.75389 | -45.48001 | 2026-09-10 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README30.md)
