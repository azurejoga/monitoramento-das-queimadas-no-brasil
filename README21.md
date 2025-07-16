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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05cbf649-2f80-3920-9ab1-79b426dbbfe8 | -4.30282 | -48.09789 | 2025-07-16 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 490170bb-5f64-3ef2-8fb2-b790781a2c1c | -5.46389 | -45.34298 | 2025-07-16 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c5e2256-5f76-3e47-bd53-18d5b09f3ac0 | -7.34372 | -49.60509 | 2025-07-16 05:04:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 95ae913b-05f6-331b-af74-2797e842dcf6 | -6.73312 | -44.33014 | 2025-07-16 05:04:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| bad6603f-9b8f-30c8-93c5-709b9c098f3e | -4.59161 | -47.25809 | 2025-07-16 05:04:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92a91d02-f09e-374b-9a2a-a30c80915306 | -2.28576 | -48.57629 | 2025-07-16 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a3f6e1f1-98c2-3579-bf7d-7e6889e7613c | -6.73175 | -44.34035 | 2025-07-16 05:04:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 411447fc-fc95-3943-9cbe-71b66600727c | -8.54137 | -47.85099 | 2025-07-16 05:04:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b4ed5ff-4503-3f2e-a34c-73961ca76f33 | -5.78523 | -45.07963 | 2025-07-16 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4cff23db-f4f7-307d-bb67-91623042cadd | -4.10658 | -48.20819 | 2025-07-16 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6cd3b293-c981-301e-8d10-5cae49bd881d | -8.91726 | -47.35239 | 2025-07-16 05:04:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e17568bb-3e7d-3903-8943-d98e31b8c868 | -3.66568 | -50.95245 | 2025-07-16 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 82c5a4f0-8ab6-3b98-a17a-865fef6e7ea4 | -4.59078 | -47.26383 | 2025-07-16 05:04:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23c5deff-8c5f-3464-9259-b47fac023d35 | -2.58382 | -51.9206 | 2025-07-16 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2623a6e-77f4-3916-9e2a-fd96b0f9ad74 | -5.79475 | -45.08175 | 2025-07-16 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e4aeedd9-c218-3cdf-91e0-a43393b07e6e | -3.38497 | -47.48273 | 2025-07-16 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f29f8ab1-5435-3487-a05b-a4d12cf58c96 | -7.20707 | -45.33019 | 2025-07-16 05:04:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b869307-eda9-3e49-83c7-7a5f802dc1a7 | -7.51031 | -46.68748 | 2025-07-16 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a67a5882-93a2-347d-a17c-7d4d9fc74ec7 | -5.78344 | -45.09243 | 2025-07-16 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ccca3624-96c6-3d3f-8135-81fc2489fa98 | -7.18957 | -59.83885 | 2025-07-16 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d454f1fb-6f3e-3d9b-a996-b92394ec8063 | -7.51077 | -46.68395 | 2025-07-16 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fcb083ab-698e-3da4-af42-3de5b1fb7d31 | -8.91239 | -47.34823 | 2025-07-16 05:04:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c8f40d9-fc56-3f99-8fc9-48a7b614a9f3 | -4.02957 | -48.06298 | 2025-07-16 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fba49e0d-160e-3ccf-91de-979fa0b61cd8 | -6.71987 | -44.33341 | 2025-07-16 05:04:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d255339a-f473-3058-b8e3-700ce10669ed | -4.02885 | -48.06797 | 2025-07-16 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 77a18ce1-b9db-3f41-8490-a4568c57d5c3 | -3.38825 | -47.49411 | 2025-07-16 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| abf3ef1a-6884-3c79-bef2-078486d8e2ff | -5.78996 | -45.08903 | 2025-07-16 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1d0450ef-bfd9-36f0-807a-0926f6c217e2 | -8.51037 | -43.30785 | 2025-07-16 05:04:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 4d39b218-19c0-3560-9203-5646fdceccf9 | -6.92365 | -52.85587 | 2025-07-16 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6699a618-8e74-345d-8205-66e5c6de7dfe | -3.85929 | -54.08008 | 2025-07-16 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c05a7e01-6a72-3df3-ae89-a027e607cfa7 | -8.53585 | -47.85334 | 2025-07-16 05:04:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a39124c8-334d-37b5-8b46-6a2a796d84ad | -6.91579 | -52.85901 | 2025-07-16 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36f1baa1-4010-355f-b571-4de4f8adfc80 | -3.39311 | -47.49487 | 2025-07-16 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9e8bb1ef-57b3-33b1-b35e-cba719032409 | -7.50954 | -46.6851 | 2025-07-16 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf681df7-ea11-361d-88c9-351a98c5e0ec | -6.70866 | -44.32133 | 2025-07-16 05:04:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 320accde-25da-3b64-9822-21f6bd545a9b | -7.94389 | -49.65763 | 2025-07-16 05:04:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f7a9b66-fa42-3fcc-8746-b3d3f2c76094 | -7.84537 | -44.19855 | 2025-07-16 05:04:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca6238c2-a5c0-3ceb-ab6b-d8019152a9df | -8.90753 | -47.34401 | 2025-07-16 05:04:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9023d7e2-fdf6-3bc1-b01d-59d4a0749d23 | -7.50906 | -46.68864 | 2025-07-16 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a5ee58d-b5d8-3cb4-ab2f-c8e5b5c6d2d4 | -2.44827 | -47.32779 | 2025-07-16 05:04:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 33e796c5-193a-37d5-8a39-7ace8029947e | -3.03373 | -47.86405 | 2025-07-16 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 999f4e7e-7dd2-3c7a-aaa1-daf80d0831d5 | -4.03503 | -48.05861 | 2025-07-16 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 129ce08b-49ca-3f1a-9bed-724077a0b64a | -7.189 | -43.1264 | 2025-07-16 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| bf7298b8-2d82-3488-81fb-6e176f00edd8 | -6.77662 | -55.48731 | 2025-07-16 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a892d682-6035-3371-8f8f-3a1c28141425 | -6.70797 | -44.32649 | 2025-07-16 05:04:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 9f4c909e-cf92-3216-88cb-15227fb6cd7b | -8.68292 | -51.458 | 2025-07-16 05:04:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d50c6c7-67a5-3003-8a7c-877f93977695 | -3.2172 | -48.97124 | 2025-07-16 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 118d6ea5-6f62-339e-b49a-cc9506f0b698 | -3.21676 | -48.96926 | 2025-07-16 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| ce2f2089-92de-33da-b05b-dc38ef223c47 | -8.91285 | -47.34486 | 2025-07-16 05:04:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19a8930f-9dc3-3bd5-aae2-7871451267e5 | -5.57632 | -46.52567 | 2025-07-16 05:04:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f031e8e8-9950-36be-82b4-a710c9d8c386 | -2.42463 | -48.19453 | 2025-07-16 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8378d215-761d-34d1-9124-80405b1fa810 | -6.72548 | -44.33936 | 2025-07-16 05:04:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 0bff7e79-a91e-301f-adc1-5f2a1acadb1d | -6.73381 | -44.32503 | 2025-07-16 05:04:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2bc94c2a-9605-3eac-ab5d-db1882c52667 | -6.91282 | -52.85419 | 2025-07-16 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c859e805-102a-3e6b-aacb-493ad5ec9307 | -3.84928 | -47.75373 | 2025-07-16 05:04:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9b738924-a283-3c09-9ffc-fdc3630480b0 | -5.79419 | -45.08595 | 2025-07-16 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 992d228a-bf66-3a3d-9c61-4fecad6026c6 | -8.90798 | -47.34064 | 2025-07-16 05:04:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8e0acb3-f1af-3343-948f-f9bf4cd95c8b | -4.78134 | -45.33954 | 2025-07-16 05:04:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d01cf951-43c1-3572-bf84-7af64fe15fa6 | -7.66764 | -56.75018 | 2025-07-16 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9de4954-350a-3c8c-a30f-7c0839dd7788 | -6.91643 | -52.85475 | 2025-07-16 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91967dc1-2645-3bf3-b2d6-c5b034aa9964 | -4.30394 | -48.09946 | 2025-07-16 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c7236175-32d5-35d3-8a60-00204a0885ac | -7.35185 | -45.66793 | 2025-07-16 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02f9773c-dd47-3367-ba3e-250e6f9c2912 | -6.73243 | -44.33527 | 2025-07-16 05:04:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 49859b3a-71e1-3130-b62b-c83bc4c9c629 | -5.78404 | -45.08819 | 2025-07-16 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0757fcc3-12fb-399a-89f0-543dea3ecfc9 | -5.79706 | -45.08141 | 2025-07-16 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f8041fb1-1ab8-3437-bca7-d3b5c9744eef | -4.11153 | -48.72721 | 2025-07-16 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 521efbc8-9e44-3109-aa85-7aee0b999539 | -7.35577 | -49.746 | 2025-07-16 05:04:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8414bbd-0a95-35c6-92ae-90516d022ce6 | -8.92259 | -47.35318 | 2025-07-16 05:04:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 58c25657-1acc-3ea5-8df2-03f69b551fa0 | -4.29393 | -48.06012 | 2025-07-16 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ae5b3ab4-3f14-3d93-96da-0e5ccc56534d | -5.79055 | -45.08479 | 2025-07-16 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a77263ca-fefb-3658-a68c-160e30b7eef3 | -6.26778 | -57.3992 | 2025-07-16 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4da047e3-ca1b-3dab-98fb-9db23b9635f4 | -4.03429 | -48.06372 | 2025-07-16 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e4da1120-598c-3904-8e33-ffa239af80e9 | -5.71934 | -44.82995 | 2025-07-16 05:04:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20ca4089-809e-375e-908a-71097eae64c5 | -7.21899 | -45.33164 | 2025-07-16 05:04:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c15d6939-9d18-3162-bd28-1c06623a0916 | -6.13589 | -44.08105 | 2025-07-16 05:04:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0d116deb-5703-3c67-912d-4887dc1d9ce1 | -4.95962 | -43.22872 | 2025-07-16 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd87fd1e-94d1-3c9e-9dc3-b087e7729451 | -6.63727 | -44.57405 | 2025-07-16 05:04:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8347b479-a584-34ea-8f54-6f4a58b090f9 | -8.75934 | -46.59351 | 2025-07-16 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b5472f5c-a040-3096-b546-dd662e4bfe6f | -3.51707 | -47.21539 | 2025-07-16 05:04:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c7671305-06ba-31a0-b4f8-5c954afd7d16 | -4.96694 | -43.22427 | 2025-07-16 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 98e276bb-2276-3d7a-a6bd-99cb21643288 | -3.33218 | -48.71467 | 2025-07-16 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90e8b6d5-3ff5-3d8d-abae-baab7949e536 | -7.50985 | -46.69104 | 2025-07-16 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2133a503-1c2c-3c35-98c5-6726da3ce2c4 | -2.91604 | -48.23745 | 2025-07-16 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 906eb10d-bfcc-35a0-ad27-17692d77fc5c | -6.72615 | -44.33434 | 2025-07-16 05:04:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 3bacea00-489b-3333-ba8a-c688c3924120 | -7.31469 | -45.76701 | 2025-07-16 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9791794-c893-3614-aee9-4072b8c66939 | -2.9252 | -48.23887 | 2025-07-16 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6a78d06c-16ee-36dd-be3d-bf7198869a7a | -7.20338 | -43.12232 | 2025-07-16 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a6319cbd-761f-3685-9dd0-81b0c0c07e85 | -2.44343 | -47.32702 | 2025-07-16 05:04:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 83ad4c76-f2b2-399f-a20f-eb15596713a4 | -3.38577 | -47.47736 | 2025-07-16 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 83288c81-1762-3586-b6ae-76b95af441b7 | -3.03844 | -47.86478 | 2025-07-16 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 24aa2daf-0d51-3f7c-960b-88f1eea1c301 | -8.65085 | -47.75051 | 2025-07-16 05:04:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1d95d72-c448-3399-a62c-23d247d9c215 | -3.04407 | -48.98267 | 2025-07-16 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15290399-ed81-3efd-b082-b340757d8877 | -9.29969 | -44.84773 | 2025-07-16 05:04:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23023058-75f7-3a6e-866f-7128af5afb4e | -12.48854 | -46.93129 | 2025-07-16 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14eaec58-0359-3d87-bc26-b800c57dd8ab | -10.9547 | -54.37999 | 2025-07-16 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f65e6dcb-fb60-3b13-ab82-b537907b0ceb | -9.01544 | -61.22376 | 2025-07-16 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 954a23da-9fa9-31aa-9a2e-c0bf352aede0 | -11.49694 | -48.07856 | 2025-07-16 05:06:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a791b241-d469-3107-b565-19afb63c36f0 | -13.02242 | -45.05716 | 2025-07-16 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| d3bcc97e-7b87-3f31-bb35-1d7555ad286b | -10.22821 | -55.4558 | 2025-07-16 05:06:00 | NOAA-21 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5de4c37-9e34-35f9-af25-4d1f3400ea61 | -11.87785 | -58.70746 | 2025-07-16 05:06:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README22.md)
