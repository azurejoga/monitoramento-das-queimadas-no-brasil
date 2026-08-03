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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e4253f6-6272-33aa-afdc-2094484ac746 | -10.57208 | -46.79029 | 2026-08-03 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ff06ec76-da90-3641-bdaa-645e91cb0eb0 | -5.73796 | -43.2737 | 2026-08-03 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 34bd28a5-7af4-38a0-8e90-041e4fc2e513 | -7.11326 | -46.71804 | 2026-08-03 04:38:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5729d26-f2cb-3a4d-8fdc-853e281a1ed1 | -7.2473 | -59.45069 | 2026-08-03 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 55455184-2243-3966-aba2-7f0edc88778d | -7.34562 | -43.85897 | 2026-08-03 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6a597a0b-1faf-382e-b1dc-069f37de943d | -6.85337 | -44.79675 | 2026-08-03 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39ad7090-0281-3ce5-aa16-a8510d92cd9c | -7.55644 | -45.04353 | 2026-08-03 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8e60e062-0658-390a-b9b2-56db443e81e9 | -7.02419 | -42.8848 | 2026-08-03 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dced9b24-69bc-3344-8c48-5878d938484b | -6.43459 | -47.97316 | 2026-08-03 04:38:00 | NOAA-20 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5152a402-bd3a-38c3-8629-39fd6e8af82a | -7.39137 | -45.06886 | 2026-08-03 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| abd4bdb1-ea4f-3144-a5d3-db82085bec26 | -5.20255 | -46.08936 | 2026-08-03 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b150bb36-b1b0-3c30-aa8a-ce363ad18d4c | -10.62402 | -46.75113 | 2026-08-03 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 134cb514-49cf-37d9-8d12-f6de98bef855 | -6.77341 | -47.02731 | 2026-08-03 04:38:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 561157c7-d2b8-3f54-a55c-f27bb053f786 | -7.20764 | -45.76987 | 2026-08-03 04:38:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e10e5c4f-7455-3638-83c5-bab741412baa | -10.5767 | -46.78315 | 2026-08-03 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d4916e01-b98a-32c6-90e4-6112f01001e8 | -8.54831 | -47.74866 | 2026-08-03 04:38:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5fdbb0ad-811d-36e6-aefc-62d7bed38b34 | -6.5581 | -55.17027 | 2026-08-03 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3fb6247a-075a-3437-a2e9-0e7514c1ac05 | -5.95166 | -46.02932 | 2026-08-03 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 81dc26f8-7bcf-3df6-92a7-acfe528d8420 | -7.62527 | -45.30763 | 2026-08-03 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b52952e2-6724-32a3-88b4-188149034a3f | -6.85069 | -42.90771 | 2026-08-03 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b6974808-040f-3700-b598-188c327847f0 | -4.26902 | -48.19233 | 2026-08-03 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2850fd37-df7a-31be-ac47-53fe909b19ea | -5.26086 | -44.18489 | 2026-08-03 04:38:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 407944a4-b0d9-33cc-a505-632fa7549228 | -10.62035 | -46.82137 | 2026-08-03 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a01d9d1b-705e-3fd2-aa46-0e62389ca837 | -6.06626 | -49.25997 | 2026-08-03 04:38:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 09d6614a-3417-30f0-8cb9-ad68ef668d08 | -7.36178 | -43.85665 | 2026-08-03 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a5225c1b-3ed4-3dae-91bd-476ced456737 | -6.55742 | -55.15243 | 2026-08-03 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36abdfe0-f829-3d5f-84c3-b51afb5ece2f | -6.55518 | -55.15981 | 2026-08-03 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37f3443d-b5da-3949-a4a5-de591fb1fd4d | -7.20944 | -42.98138 | 2026-08-03 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fd474157-e6a4-3b44-9663-e8df997a80d0 | -7.96864 | -44.90947 | 2026-08-03 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd2c54ff-fc26-3c4f-8937-66d031c8f24b | -6.54659 | -55.16034 | 2026-08-03 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8fb6136f-fa4f-33fa-95c4-d2d9d7de4a12 | -10.54471 | -42.5391 | 2026-08-03 04:38:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 76f09fdf-1257-304a-bd7c-eb99a406d504 | -6.5602 | -56.52841 | 2026-08-03 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2326a235-7058-38f8-848d-3193b4e9aaa4 | -9.40706 | -48.57582 | 2026-08-03 04:38:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9510e98a-ef15-3cef-84a0-9f206ce5db73 | -10.56805 | -46.7936 | 2026-08-03 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7f5ca6d2-4ec6-3c41-bd0c-e2578df532bb | -3.57807 | -50.2608 | 2026-08-03 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f1c454a-b97e-394a-87bf-97d15696c6dd | -6.55348 | -55.1695 | 2026-08-03 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ea6d5004-9dcc-3dec-9183-9ae359385e36 | -6.54972 | -55.16378 | 2026-08-03 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d7138551-8ca9-384d-b3ed-96301c07d1b8 | -7.34948 | -43.85959 | 2026-08-03 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 28c57223-c963-3367-9d5a-418ff53bfdff | -7.3243 | -42.99073 | 2026-08-03 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 89c30b7b-921f-3983-9543-77e2df1514c4 | -6.06287 | -45.0546 | 2026-08-03 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13401591-c40c-3384-a1bb-a8dbae6bb024 | -7.3502 | -43.85477 | 2026-08-03 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f329e37a-ba62-3cb6-b965-235c129d5846 | -2.81433 | -52.28904 | 2026-08-03 04:38:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 54ea39ab-4754-31d7-8036-5118e34450d5 | -10.56863 | -46.78975 | 2026-08-03 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d38d5cc4-73b9-37e4-b25f-3799d1cd7aaf | -5.2037 | -46.08892 | 2026-08-03 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d8ea50af-d22d-3961-acba-636297099dba | -10.74915 | -47.26025 | 2026-08-03 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bcd8cac8-59bd-30da-a4c7-65a4141d6eeb | -9.31755 | -47.62628 | 2026-08-03 04:38:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d6340890-32e5-3fcf-b827-676f647257b7 | -5.20201 | -46.07069 | 2026-08-03 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7858f33a-436f-3915-bb7a-3347d5258a25 | -5.98003 | -45.00549 | 2026-08-03 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a682b5a4-df2c-3bc7-bee9-4a80b480b489 | -6.84307 | -42.90284 | 2026-08-03 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 30a6da98-e25a-3353-83b1-6125dc823011 | -6.85765 | -44.79307 | 2026-08-03 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b2991a3-40d0-3883-91fe-e6e860610080 | -4.90598 | -43.47108 | 2026-08-03 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0fce1424-d2c6-3940-82fe-6ce9e6a32fcb | -5.77224 | -50.18774 | 2026-08-03 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 44e5a525-2ae5-379e-b145-02df31071209 | -6.14533 | -51.63649 | 2026-08-03 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21cedca7-aee8-383f-8d29-72b6de6f89a4 | -5.72056 | -44.50286 | 2026-08-03 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 58ec4a91-1b21-36ce-8e16-774746c84235 | -7.32065 | -44.54469 | 2026-08-03 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e658cc25-3271-3bd9-84a6-553b3c0f9879 | -7.15443 | -44.04803 | 2026-08-03 04:38:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95ba141e-82fc-3802-9529-416eb1f2e9c7 | -7.35334 | -43.8602 | 2026-08-03 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2ecd0e90-fb0a-343f-b1c6-162a41fa463d | -8.18019 | -49.19626 | 2026-08-03 04:38:00 | NOAA-20 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8c0b137-9d7a-3573-bb97-9ba812ac05d3 | -8.55163 | -47.7492 | 2026-08-03 04:38:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 416d64fb-97dd-3159-a147-8c4cfa2bab07 | -6.0838 | -43.66413 | 2026-08-03 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f35b333-9a88-353c-bbb2-ac82166c8b51 | -7.56068 | -45.03994 | 2026-08-03 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69e90ee3-f534-358b-bd38-ed9a853d11f7 | -7.47409 | -44.89333 | 2026-08-03 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1a5aeca-2be1-33ce-805f-2fe4696b70fa | -10.14479 | -46.33564 | 2026-08-03 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 357baa56-d1af-3796-9ab8-e8151b974304 | -6.95552 | -52.82487 | 2026-08-03 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b64410bd-b2db-34ed-880f-1295ecdb725f | -2.96019 | -50.34401 | 2026-08-03 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 142dc03e-d107-3d74-901e-a3f808821cc9 | -5.20649 | -46.07077 | 2026-08-03 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9aee939-4915-3767-81fe-719ef388b3a3 | -6.95639 | -52.81974 | 2026-08-03 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8bbe1387-2fd6-3a04-b9f5-d2f9fc12592c | -6.96336 | -52.82626 | 2026-08-03 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 02280cbc-dd34-3cd3-b104-144940ae157c | -6.00972 | -47.41304 | 2026-08-03 04:38:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7c7afc9-459a-3fa5-9efb-7391604317a2 | -7.3695 | -43.85789 | 2026-08-03 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60a2cdc9-7bc2-36ae-b146-3340a064feed | -8.00333 | -46.23921 | 2026-08-03 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 519a534e-8466-3ecb-8a51-7bdf21de412e | -8.34307 | -45.98693 | 2026-08-03 04:38:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| be6999cb-eb55-3fd9-9af8-4629cf6061b8 | -7.392 | -45.06473 | 2026-08-03 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1640b1c5-6406-31a2-a41c-0441190d9445 | -6.56443 | -55.1613 | 2026-08-03 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3baa33b6-3bb2-33c6-b706-ff2d1cfd4a71 | -10.74858 | -47.26395 | 2026-08-03 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fe87ddf6-9661-3717-b055-c1c73f90c23d | -8.23602 | -46.24652 | 2026-08-03 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 68ec1cc0-3cdd-3e5c-8360-02cf4014fce1 | -6.29914 | -44.87879 | 2026-08-03 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3b445d6-ee80-3cb2-aec7-b68487035e48 | -3.53806 | -49.47269 | 2026-08-03 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 667b1f59-92fb-3976-8917-09c1d50a6251 | -6.43735 | -47.97713 | 2026-08-03 04:38:00 | NOAA-20 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 929afdb4-7f3f-3782-b853-490dec27b524 | -3.5415 | -49.47324 | 2026-08-03 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 380958a8-4924-3ff3-a03a-e37c94610fa6 | -7.08145 | -43.34338 | 2026-08-03 04:38:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 214905f9-955a-345c-a558-922227cbeebf | -9.07601 | -44.35466 | 2026-08-03 04:38:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 86ae7a77-8c8b-3574-863f-d15917f23903 | -6.77396 | -47.02378 | 2026-08-03 04:38:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| adb86913-40d3-3107-8868-cbacf512a086 | -9.08158 | -46.05269 | 2026-08-03 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 249b1bd3-5959-3035-90fd-18f8899cbec2 | -3.43598 | -48.83677 | 2026-08-03 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ca8a01e3-43ae-3d0e-8ebb-81429df463a3 | -4.47844 | -47.51459 | 2026-08-03 04:38:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae299a18-08f7-338d-8017-d19d81bb94d2 | -7.3449 | -43.86378 | 2026-08-03 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c098a3cf-89c0-3ef5-97a3-b47b86e1ae47 | -6.96423 | -52.82115 | 2026-08-03 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ab43858-138b-3c2f-8058-852edb375b0b | -3.58098 | -50.26537 | 2026-08-03 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66da01c4-525f-3492-a010-014dd51d5532 | -5.2054 | -46.07121 | 2026-08-03 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1e5506c-50af-30a2-b889-26cbcce07539 | -6.69455 | -47.98278 | 2026-08-03 04:38:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 939a3f27-1ce7-3d59-b960-c3b5b7312a88 | -7.07747 | -43.34283 | 2026-08-03 04:38:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7e9ccf31-20b2-3c39-8f3d-74d506db4678 | -7.83314 | -44.45478 | 2026-08-03 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f6a953e-5563-3882-924c-e4845ae50037 | -6.54678 | -41.83409 | 2026-08-03 04:38:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| efb56e1e-83ba-3a43-ad8d-cb97c7ee04e8 | -5.20144 | -46.07431 | 2026-08-03 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 61f7c2ae-e669-340f-a682-8eb61d9e924e | -4.27289 | -48.18939 | 2026-08-03 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f5edc566-25dd-3eaa-acb7-eea459cc5b30 | -6.55231 | -41.82674 | 2026-08-03 04:38:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 006cd1b2-cde2-308a-876a-ceb9d54365bb | -4.10199 | -50.42671 | 2026-08-03 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 383b9378-9dfd-3cd6-9ad7-07c9a207e7ad | -6.99157 | -42.11942 | 2026-08-03 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fa983ba4-ab66-3d6d-9606-7f8e92a58f0a | -10.57438 | -46.79851 | 2026-08-03 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README6.md)
