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
| 560de215-3099-3359-9945-468125005d84 | -8.90916 | -41.07315 | 2025-11-14 03:53:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 9b04ca01-555d-3a27-8bff-3c96b824256a | -7.85839 | -44.30595 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed2c3241-0fe0-33b3-83ac-8f87211329bc | -7.94119 | -44.32798 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 402b05d4-5f37-3096-aaa4-7b6a62a00cbd | -7.89069 | -44.31947 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f266fc8-0c56-314a-bb88-68ea54a938ee | -5.42529 | -43.19766 | 2025-11-14 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22de1b10-445d-3afd-8ecb-191fc2deabf4 | -7.00518 | -42.78737 | 2025-11-14 03:53:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 9ea2bfa0-ab3c-3fe9-b97c-2c90f6878697 | -5.42182 | -42.57405 | 2025-11-14 03:53:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6f531080-0dda-3976-80b6-0ce78f381e66 | -7.01828 | -39.1904 | 2025-11-14 03:53:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5ee41fea-21cc-37f5-9894-05139f38932f | -7.46161 | -42.5846 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c3489424-d5b6-30de-8651-63f9b18e9ed3 | -7.85623 | -44.29351 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e376ee11-ee25-3dd2-867b-acf5f2f4fe61 | -6.18668 | -40.87539 | 2025-11-14 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c3c48e94-6edb-322f-a6c3-96d82874ee71 | -6.28222 | -41.74154 | 2025-11-14 03:53:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| aaf9998b-67ec-358a-931c-685a683bae54 | -7.83967 | -44.28618 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 137107ad-64a4-3be4-9674-529acc124653 | -7.93344 | -44.32261 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 36510039-f052-3426-b7b1-2327cca54506 | -5.74974 | -45.10694 | 2025-11-14 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef07cc6b-03be-3633-ba14-a4fa81d12b6c | -5.59646 | -45.17685 | 2025-11-14 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 46398ff3-d332-3218-bd09-f5a8be1f1225 | -5.75373 | -49.26173 | 2025-11-14 03:53:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03efd4cf-2037-31d4-91f1-0415cb936d53 | -5.52223 | -41.75491 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 42937b0a-4727-39e7-8328-eab18805f8c7 | -6.44011 | -45.6664 | 2025-11-14 03:53:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d0534ff9-9646-38a2-a971-fc8c71997eb1 | -5.97752 | -42.60025 | 2025-11-14 03:53:00 | NOAA-21 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ee3a3cd2-5a2c-31c9-90cd-5cc7866b816b | -6.89067 | -42.06195 | 2025-11-14 03:53:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fba9901d-9e36-3314-8f16-127b05c0b011 | -5.36662 | -46.28958 | 2025-11-14 03:53:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 21.0 |
| e964347b-711e-33d5-88b4-dec02de81dbc | -7.28715 | -45.46357 | 2025-11-14 03:53:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 405f81df-f3b5-3d78-9829-2ccaa583d874 | -5.33497 | -41.86037 | 2025-11-14 03:53:00 | NOAA-21 | NOVO SANTO ANTÔNIO | PIAUÍ | Brasil | 2206951 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ba8c6736-c656-30ae-9759-5f1b8ceaf6f8 | -7.26194 | -46.88801 | 2025-11-14 03:53:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc9184e1-52b3-380b-a5c4-743f219c1cb3 | -5.89059 | -42.26207 | 2025-11-14 03:53:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f4c916f4-b6cc-388d-aa9b-07d93ad36e72 | -5.25109 | -46.18136 | 2025-11-14 03:53:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9911d56-ded4-35ab-b8a6-82972d47023a | -7.1492 | -41.2516 | 2025-11-14 03:53:00 | NOAA-21 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 31ad9552-5ee1-3629-8446-1edc404c8029 | -7.06255 | -43.58303 | 2025-11-14 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ccc70b6-e6fd-3360-bba3-35871600ca56 | -5.34859 | -46.76212 | 2025-11-14 03:53:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 67c0036f-2263-3e50-a936-ced35b8076e7 | -6.09863 | -41.53209 | 2025-11-14 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d20c9277-fed0-3ce4-8467-5707cd8adaa2 | -7.45177 | -42.57332 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 4741704d-f3ee-3927-884b-a2caf2b46470 | -6.00523 | -38.98972 | 2025-11-14 03:53:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a6c4ef4e-2665-3b39-ac00-28864ff16a7f | -4.77697 | -46.45017 | 2025-11-14 03:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe136c24-3294-341a-a3e4-fc4328d6a9d0 | -7.45479 | -42.57864 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| cb559bae-69f8-3c1f-b430-50c9e7f1ec84 | -6.83832 | -48.0057 | 2025-11-14 03:53:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a3b23ba-bea5-3e00-98a4-778a83219bbe | -4.71229 | -46.44308 | 2025-11-14 03:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 247340cc-7e5e-3c42-bb07-72b68c6820c3 | -6.98061 | -39.1703 | 2025-11-14 03:53:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d25ad568-c0f3-31a8-825d-bd1beebf14db | -4.7926 | -46.48179 | 2025-11-14 03:53:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0af33e5-3e59-3bd6-895d-6a77d28f067f | -7.66883 | -45.87733 | 2025-11-14 03:53:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 158becfc-d16b-3bc7-8da0-ef6c5464c26d | -7.00131 | -42.78672 | 2025-11-14 03:53:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| dca50c69-1ff7-34c6-a426-3f3646961926 | -4.69591 | -45.67862 | 2025-11-14 03:53:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 560a6aa8-b981-3ea4-b48b-e0ef9203bffb | -5.2568 | -46.18068 | 2025-11-14 03:53:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 50804b30-bbc5-384a-a72f-cbd426c2932c | -7.85097 | -44.29617 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 61ce05b6-80e3-33bb-9ea9-2c6d029cf750 | -7.71851 | -42.36869 | 2025-11-14 03:53:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 36b55d8f-8694-32d0-a9cc-3200f6033259 | -6.09196 | -41.71284 | 2025-11-14 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 408831cd-5a94-3cb3-bd7c-68f4e8750285 | -4.71124 | -46.44923 | 2025-11-14 03:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d4312a35-7dd8-3599-8fb6-f74bc0624fe1 | -4.53785 | -46.41527 | 2025-11-14 03:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b808b979-57e8-31ac-a6e4-44bf5ec28c7d | -6.2917 | -41.72964 | 2025-11-14 03:53:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e672963e-f0d6-3308-abba-1ce861e7e431 | -6.39029 | -42.31824 | 2025-11-14 03:53:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 26314f95-00c6-3d14-92ba-9b866e404f7a | -7.3866 | -48.65653 | 2025-11-14 03:53:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08bb6c3d-38ea-34d6-8eb7-9accbb6c6dd1 | -5.07823 | -42.65669 | 2025-11-14 03:53:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f9edcba-6a15-35c7-9786-b22e4f8dbc86 | -5.56652 | -43.61309 | 2025-11-14 03:53:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4d66544-2317-3ce5-80b1-a1d52179f9c8 | -5.7239 | -42.35315 | 2025-11-14 03:53:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 2b9a8904-f6dd-3878-9c04-10369a5382d3 | -5.65619 | -41.08382 | 2025-11-14 03:53:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 93796811-24ef-310e-aa8f-9f4391b339e6 | -7.14631 | -41.24697 | 2025-11-14 03:53:00 | NOAA-21 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6aa7493d-b113-39a7-a82b-184cd9c99383 | -5.51996 | -41.74541 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7c8f81a1-9897-386b-92df-9736e6aee1f5 | -5.90054 | -42.74729 | 2025-11-14 03:53:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f06ef466-14c4-3478-a910-be5677134f0c | -6.55679 | -44.24585 | 2025-11-14 03:53:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| acd49159-ca7e-3b44-af5a-210d985dace0 | -7.85135 | -44.29671 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 655161f8-ec57-3004-9a4b-c58517662820 | -5.79031 | -43.73596 | 2025-11-14 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7e45325e-d9ab-3f9f-a2b9-a0ee5f4f0cd9 | -7.84676 | -44.29546 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 27614423-d55d-33ac-98d2-4858e4c537ea | -7.26238 | -40.17487 | 2025-11-14 03:53:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 57521092-09df-3175-856a-f0b067f9da10 | -7.6218 | -46.83347 | 2025-11-14 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2b9273e-f292-3b2b-bc26-a7a87a09db83 | -7.46695 | -42.57582 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b0155749-c80a-39f4-aa3f-4ae0db24b0ff | -7.37574 | -42.58741 | 2025-11-14 03:53:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a4bd49c4-f315-3549-ae6c-43082f80b0f2 | -4.71743 | -46.44387 | 2025-11-14 03:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c92843f9-cefc-3c14-a6d1-218f44ff46cb | -5.25159 | -46.17838 | 2025-11-14 03:53:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0d5dc36-3f60-3be9-befc-1afe26606d95 | -8.5026 | -39.61607 | 2025-11-14 03:53:00 | NOAA-21 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4314753a-5c4d-3b3b-a7ab-d4a08b3d634b | -7.84851 | -44.28819 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e03d2348-1edc-3060-8a95-a096a28ca678 | -5.42312 | -43.26075 | 2025-11-14 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 120cabb5-9876-3a33-9c8b-082833bc35c0 | -6.68805 | -47.80182 | 2025-11-14 03:53:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 707684f3-4c38-311c-a729-02125888ebc3 | -6.37986 | -39.50123 | 2025-11-14 03:53:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 34123649-33d9-3b8b-ac63-3ddab14d7755 | -4.11321 | -50.0568 | 2025-11-14 03:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ba13557a-6840-3515-a0cf-b937767dadea | -7.17098 | -38.45723 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f18e0edb-d038-3f31-ab54-d03fd92fb1bd | -7.45781 | -42.58398 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6349b91c-2506-315c-b47b-35e8f9f91d99 | -6.83089 | -43.1627 | 2025-11-14 03:53:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 8eb2805e-4030-3b8a-b5f2-f4f4cdb16029 | -6.10296 | -41.52844 | 2025-11-14 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e324b0e8-e662-3392-9d11-eee4dea958b8 | -7.71862 | -47.18895 | 2025-11-14 03:53:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa906eb9-983d-32b0-acc1-580267a5e76c | -6.99438 | -42.78058 | 2025-11-14 03:53:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| acd4bcbc-d598-3359-9064-31f4e1333d16 | -4.97801 | -43.09787 | 2025-11-14 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2417da30-6bf2-3baa-838b-72e4184815df | -6.10231 | -41.62526 | 2025-11-14 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 694c403e-bdd8-3afb-938e-461a84dd737a | -7.39302 | -48.65339 | 2025-11-14 03:53:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f55d3d2-7437-38af-b742-5b4b06790b9c | -7.6735 | -45.87827 | 2025-11-14 03:53:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7aeb8077-6c4b-33f0-ac39-0737952d91a6 | -5.21223 | -43.9155 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44645150-9fcf-36a6-a754-9e48c35f99ec | -9.05343 | -40.65903 | 2025-11-14 03:53:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7aab64b6-e2dd-3f39-95f9-03454d2e3bac | -4.71072 | -46.45233 | 2025-11-14 03:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 97fc9d24-3523-3d5a-b120-44369ee37317 | -5.49523 | -42.16253 | 2025-11-14 03:53:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3cdd678d-b1dc-38ea-9e0e-21d4d3312c48 | -5.42644 | -46.09103 | 2025-11-14 03:53:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4d75554-f18f-36ba-9bde-4b0af52d9a6f | -4.98351 | -43.88797 | 2025-11-14 03:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54a05f0a-bbb6-38b6-8faf-6f281f021f56 | -5.97772 | -42.76728 | 2025-11-14 03:53:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f45c978a-2d46-371b-9031-2af8c1cf497e | -5.6041 | -45.18809 | 2025-11-14 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2bc64a7-27c7-3cf4-932a-39b6e226f8ad | -6.41283 | -39.74877 | 2025-11-14 03:53:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 91997081-a1c8-3488-a05c-96120bc98f09 | -7.93211 | -44.33049 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6034b08-2c0c-3f0b-b945-ebcd0726d11d | -4.9531 | -43.72665 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a42c496b-cb4c-3012-a877-660f938dea6e | -6.06906 | -41.57582 | 2025-11-14 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 61585057-434a-398e-a5cf-2e050c503466 | -7.72887 | -47.19078 | 2025-11-14 03:53:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d40ee1d-2845-3f02-a21f-383a5b441f57 | -6.45041 | -45.66311 | 2025-11-14 03:53:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 89eab20d-4a31-3948-a582-c776d122709f | -7.93881 | -38.37709 | 2025-11-14 03:53:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bfd12ac8-5a38-3bed-943b-22c0ef9403dc | -7.85271 | -44.28889 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README15.md)
