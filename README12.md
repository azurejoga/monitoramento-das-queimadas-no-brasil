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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c742323-dda8-3b84-9946-04bc83f31e6c | -7.02014 | -44.60302 | 2025-06-20 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a42090b2-3bf0-3582-afd2-f53f194bb8f2 | -8.72113 | -47.98756 | 2025-06-20 04:00:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed30dc6c-35bc-3e8a-a815-e23a8a7f06fa | -7.13786 | -43.28037 | 2025-06-20 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7e186fe5-4b16-3f84-b24f-ed3104c7b7a0 | -7.71983 | -46.60992 | 2025-06-20 04:00:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0475674d-8968-3b49-9ae5-7f4f77437329 | -9.30215 | -47.79412 | 2025-06-20 04:00:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f81d485-4d9b-392f-b943-ef9f8e65b06f | -7.06697 | -43.39405 | 2025-06-20 04:00:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d2b725a2-5864-3936-afa3-2907bbf36da0 | -8.12376 | -43.1246 | 2025-06-20 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 0cf12e8a-fa14-3c42-9102-09cca6dbd251 | -7.26932 | -45.35815 | 2025-06-20 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5013ea3c-4a9e-361e-bb0d-702c2702bb7f | -7.54329 | -43.81985 | 2025-06-20 04:00:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 906c4bde-4e8f-3031-b104-7010bef88b6d | -9.87517 | -49.33643 | 2025-06-20 04:00:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2875874a-892a-33dd-bcf7-f47200836945 | -7.11659 | -43.14045 | 2025-06-20 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dc9c2f5a-949f-36c1-ba41-d65907257631 | -6.70086 | -43.24846 | 2025-06-20 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6bfd3096-6dde-3961-8ef1-48171afb11db | -6.13032 | -43.95594 | 2025-06-20 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0557d1e6-070b-3008-b4ee-85a82b0568d3 | -6.24333 | -44.65363 | 2025-06-20 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ada56aeb-f220-3613-b54b-045d7ea61da1 | -5.78168 | -43.45934 | 2025-06-20 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a2b98069-9175-32dd-b5c7-4178d2553400 | -7.26751 | -45.36908 | 2025-06-20 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33af14ab-1718-3720-babf-5a7e74f16a73 | -8.64577 | -47.15771 | 2025-06-20 04:00:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7fc473b-d590-38e5-b616-355241cc35a0 | -6.66492 | -44.24502 | 2025-06-20 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 435077ac-ed7d-3153-97a8-8ba0380c6160 | -6.66954 | -44.24084 | 2025-06-20 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4226396f-3169-31fd-9581-6b0ff52a7c7b | -6.59024 | -41.77229 | 2025-06-20 04:00:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 75182009-149b-3713-8953-d173e044a361 | -7.02097 | -44.59803 | 2025-06-20 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a6c39994-fd66-3237-9cfe-0f2a4eee605e | -7.21945 | -43.07312 | 2025-06-20 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| e2d2e72e-f419-3253-8987-d5f7c2bf5361 | -9.10367 | -50.03217 | 2025-06-20 04:00:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea5adf96-59bd-30e3-8fd1-843c8a5350f9 | -7.21719 | -43.06438 | 2025-06-20 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 02137262-230e-31d9-a2e2-8a05b6b7978c | -7.24988 | -43.48882 | 2025-06-20 04:00:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dd1aac9b-e818-3f23-ae37-7e5a802a54be | -4.85129 | -43.19311 | 2025-06-20 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fce8deb8-c179-325e-afcb-4acb1b5f1266 | -8.90987 | -49.85113 | 2025-06-20 04:00:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 20bab41b-30e0-3b40-a039-7449b44ebaf8 | -9.30338 | -44.8283 | 2025-06-20 04:00:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2b279353-02b0-3585-b934-a0e09ffd379f | -9.3093 | -44.72248 | 2025-06-20 04:00:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db502048-9f20-3513-99e2-4b277993fd65 | -7.97183 | -46.21679 | 2025-06-20 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14b1d637-0953-3bf8-aab1-837ab87a15b2 | -9.84665 | -44.69032 | 2025-06-20 04:00:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8be0ab3b-b720-3062-911e-de2577f38e9d | -8.26044 | -44.95602 | 2025-06-20 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 11768d8a-aff0-3cc2-b853-01f25e80c801 | -7.75225 | -47.6146 | 2025-06-20 04:00:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d03fb070-f385-39d5-a089-2bda14b48b5b | -7.06192 | -43.40192 | 2025-06-20 04:00:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2723beab-ead6-3638-be20-d14ec2749638 | -7.06263 | -43.39769 | 2025-06-20 04:00:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7bdd8fca-b525-3a0b-80b7-066080049852 | -9.9547 | -46.62558 | 2025-06-20 04:00:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0241330b-e627-31db-93d2-2630c768a5e9 | -7.2358 | -44.68443 | 2025-06-20 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 31dd165d-2be4-37f9-a896-871a623e208f | -7.24348 | -44.24237 | 2025-06-20 04:00:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 473e30e6-6fdf-359b-9918-d2048f6b7e1a | -9.31769 | -47.78737 | 2025-06-20 04:00:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 507c16a8-2bca-3768-9af1-c79b63fb97a9 | -10.49241 | -47.02238 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0c534c1e-4d97-3c34-83f8-2e8ff02eb605 | -10.48159 | -47.03308 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19729a7a-d9d5-3d4b-a445-f1220c09c95a | -11.31365 | -45.2013 | 2025-06-20 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 861dc5f1-0939-34b7-8889-6b5265456c28 | -11.31655 | -45.20311 | 2025-06-20 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c958cc7d-013b-3b79-8575-641d5012d417 | -12.40253 | -46.36715 | 2025-06-20 04:02:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68b795e7-37cc-30a2-bd29-39620bfd4501 | -11.12831 | -46.67173 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1aaf993e-ffb4-334a-b903-eef201a24d3c | -17.21401 | -44.79854 | 2025-06-20 04:02:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b13fa9f4-0f22-3c05-a31f-095fc45b9dd8 | -14.43508 | -48.9172 | 2025-06-20 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 582452fa-6d34-36aa-8863-4e4eaaf93f01 | -11.9368 | -48.42714 | 2025-06-20 04:02:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a74a79c9-02f4-36a6-9ca1-ee311f1f78c8 | -11.13433 | -46.6375 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af768110-9f4f-38e9-813f-2350abb61b01 | -11.47098 | -47.29198 | 2025-06-20 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2518927-d80a-357b-aaaf-f295189bb248 | -10.83763 | -46.71939 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bdf88f4-4758-3f4f-ba9a-71b294a9b5ae | -16.07452 | -53.7489 | 2025-06-20 04:02:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a5548c7c-af4e-3beb-a0ee-e3ccfea1118b | -11.31573 | -45.20777 | 2025-06-20 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d3a1394-0dfd-3825-b4d1-2c3576ddece5 | -13.38698 | -48.45634 | 2025-06-20 04:02:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f70e0a95-4ca8-34b8-bda7-63b0e9684a4c | -12.63385 | -44.32959 | 2025-06-20 04:02:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9ca6ef34-f30d-348d-9696-2dc63808f508 | -11.14884 | -46.62805 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71b32fcd-0297-3f8e-9cf0-673436036244 | -10.65891 | -49.36538 | 2025-06-20 04:02:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43a8edbf-f822-31ce-b0d6-e8827197b62b | -10.85188 | -53.77386 | 2025-06-20 04:02:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90f6cf0f-ab5a-3982-902f-e54f57888e91 | -12.49286 | -47.47937 | 2025-06-20 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf77b892-cfcc-3734-a697-09345280c219 | -12.22707 | -54.30135 | 2025-06-20 04:02:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb0effde-a4c0-35d9-a769-5e58ddf4541a | -13.2342 | -49.83662 | 2025-06-20 04:02:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6e2ad6bc-4cdf-3994-8774-17ccc981385a | -12.35297 | -49.30747 | 2025-06-20 04:02:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| f15cdce0-b149-3861-9d4f-cb11017a29d5 | -10.46844 | -47.05667 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 34.1 |
| d08890f2-142b-3353-98cf-e1d4221eb446 | -10.84654 | -53.76633 | 2025-06-20 04:02:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3847d1d7-a359-307b-9477-905f30c04bf4 | -13.23914 | -49.83766 | 2025-06-20 04:02:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 83ed8419-b515-3021-84fb-9cbdb4fbe30e | -10.47579 | -47.04059 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f9db1122-3d1b-35aa-ab2c-4d250fd9a56f | -10.48515 | -47.03808 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6479b24c-f3ba-38fc-88b8-d21c39545dc5 | -10.92837 | -49.2749 | 2025-06-20 04:02:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7c376544-3e12-3f36-a6d2-f9310eca8ba0 | -10.46921 | -47.0524 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 34.1 |
| f91ef13a-f131-3b60-93eb-72292aa02fed | -10.0832 | -52.74709 | 2025-06-20 04:02:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2f13283-1265-3a16-b5fc-184f31c99625 | -10.83043 | -54.0168 | 2025-06-20 04:02:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5056f02c-8b67-33df-850b-ffebb0347539 | -16.64156 | -48.4906 | 2025-06-20 04:02:00 | NOAA-20 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1665073d-3fdb-3ae6-ab2b-fe8389abdb1c | -13.25924 | -46.82293 | 2025-06-20 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 701be570-eea2-3de6-8f54-4eec016d463c | -16.00591 | -46.37886 | 2025-06-20 04:02:00 | NOAA-20 | URUANA DE MINAS | MINAS GERAIS | Brasil | 3170479 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 26d480f0-0103-3d44-a483-680d2c6ea46c | -10.51998 | -46.648 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5a68143-1ee2-3d36-a73f-226bcb8ccb2a | -10.66448 | -49.36336 | 2025-06-20 04:02:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f53e652-0533-3eaa-a138-7fcb68dd0081 | -13.39328 | -48.44761 | 2025-06-20 04:02:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c98f9b96-34b6-3ff3-9f82-5f1125832465 | -11.47381 | -47.30121 | 2025-06-20 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48956e20-f6ed-3607-afe5-8995c2e4229b | -10.83795 | -46.71643 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f94c758b-8af3-3a35-bc47-400d7cd38c94 | -10.92844 | -49.27305 | 2025-06-20 04:02:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7ac5e27b-630f-36f9-b723-09eb6855a7ac | -11.14413 | -46.65502 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b2affd5-c7b3-3d91-b031-6e9e16e050e0 | -11.81817 | -54.50374 | 2025-06-20 04:02:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db5ffb1f-3b95-3907-932a-fa0a3ad52a05 | -11.57563 | -47.8721 | 2025-06-20 04:02:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 00079e47-9aca-3b72-9581-82f0782c209d | -10.5249 | -46.6448 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31ff875d-c4c5-3f40-bfd0-52a764bbfde1 | -13.09782 | -52.29278 | 2025-06-20 04:02:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 90d6e34e-4af5-3353-8056-55d0ab8e33fb | -10.16141 | -48.9851 | 2025-06-20 04:02:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 54af6e0a-cd1e-3a5e-8cbb-6db3513815f3 | -10.48738 | -47.02564 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a1836dbb-50e5-3eb8-b079-d5af3672b1bc | -12.21191 | -45.53493 | 2025-06-20 04:02:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e5be05a5-9d29-31b1-937b-9ac2e214de0b | -11.98421 | -51.60715 | 2025-06-20 04:02:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42659ffd-71b3-37ee-a181-ad98c32c7da9 | -11.12346 | -46.67486 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6e312182-1adf-3ebd-99be-c99f1d6a8617 | -11.15448 | -46.64491 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 73393fe3-b879-3c1e-bd96-2682cb30fbfb | -11.98222 | -46.73608 | 2025-06-20 04:02:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 671c6777-fd27-36e7-b19a-8ed07261f372 | -11.80423 | -43.78211 | 2025-06-20 04:02:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2ad8dd47-3176-3f27-8290-3e13620defdb | -10.94001 | -49.43385 | 2025-06-20 04:02:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4bf7f5a5-885d-3453-b1b0-d05076b63522 | -12.20809 | -45.53424 | 2025-06-20 04:02:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aa1e2093-40f9-320c-a6c4-c68e00525b88 | -12.26453 | -44.60793 | 2025-06-20 04:02:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d7c0bb11-bdeb-3402-9fcc-ed4fa016f9cb | -12.19513 | -49.6221 | 2025-06-20 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 23853bf9-be98-319b-9949-768eca9461e0 | -10.85962 | -53.76953 | 2025-06-20 04:02:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ac18209-e732-3ba4-9f7a-1493f8be8873 | -12.76735 | -44.41478 | 2025-06-20 04:02:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f12a8ada-209a-31a3-aa4b-b205b46787b9 | -10.5242 | -47.57863 | 2025-06-20 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README13.md)
