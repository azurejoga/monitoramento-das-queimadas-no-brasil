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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 791edd18-8352-3b93-943d-881716c81d19 | -10.97897 | -46.89689 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 801d15e2-13d1-3f41-ba95-8e34fb4dd4a9 | -11.3254 | -43.56988 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2d7e8a9-aa74-3d65-8c67-1918ab12e154 | -12.92215 | -48.14526 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53295240-a8be-3645-9499-b9a4a9993f75 | -12.82679 | -48.10822 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91bca086-321d-3e36-a405-3ee44577c578 | -11.08591 | -44.76392 | 2025-08-29 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e78b038f-281b-35a1-8e81-f7f7dc9501b0 | -11.03047 | -45.06998 | 2025-08-29 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f2784335-fcb1-32cc-bb56-ce839c7ca27f | -17.54259 | -46.6066 | 2025-08-29 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 320f9e87-86fd-3ac9-a251-cdde16104f8e | -12.82202 | -48.10371 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e918dfd-50c7-38d4-ba51-0d014ba94e32 | -11.58088 | -46.26816 | 2025-08-29 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 157a4412-e342-3679-ad70-44c860bee9fb | -6.25042 | -42.73528 | 2025-08-29 03:49:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8df2816d-2990-31b5-b741-ff1fd65a6b19 | -10.97716 | -46.90658 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 07fffd00-f4c4-3819-bd2d-99adff67237f | -11.59125 | -46.37716 | 2025-08-29 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5598a904-0649-37f8-8562-ffa7a9a77457 | -6.27167 | -43.81626 | 2025-08-29 03:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| afd74ff2-04c1-3740-92ae-06a65e93db82 | -11.08648 | -44.76633 | 2025-08-29 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97ed40b8-f075-3c0e-b42d-dbc62a9b70c7 | -17.7563 | -44.49907 | 2025-08-29 03:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 693c1900-ad9d-35e1-96ee-a129a8402ccd | -11.32819 | -43.57829 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9c97806-66ef-3b61-af50-9ad76f9ae4cb | -12.68579 | -48.18758 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 9646ca5e-a48c-30e8-8bb8-fcda36326b27 | -6.60678 | -43.64467 | 2025-08-29 03:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5b46e120-e88b-3947-8a85-3e5bd4c6490a | -11.58134 | -46.37489 | 2025-08-29 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df9d6ffb-7848-3024-81a3-1cbd7d6f38ad | -15.43698 | -39.82767 | 2025-08-29 03:49:00 | NOAA-20 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bc9610c3-7a48-3c62-b1d5-188d165f2ece | -16.50751 | -45.10402 | 2025-08-29 03:49:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d7c85bb-cf2e-3ed9-9343-461144094e4b | -11.2624 | -45.4959 | 2025-08-29 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da7bcc02-11e8-335c-a3e6-1d816320c641 | -13.54355 | -46.9455 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c7f181d-1dab-3256-9802-fbdbcc82db8c | -13.97101 | -46.33767 | 2025-08-29 03:49:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3481938-bfd0-35cc-b9c7-8829d2cd3d4b | -11.62015 | -47.31057 | 2025-08-29 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb691229-05bd-3302-9eba-f5fa3a3c3901 | -11.32888 | -43.57446 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59d24b81-98a1-3861-8a2c-62819efc09f5 | -5.86307 | -42.94119 | 2025-08-29 03:49:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 58dbc445-ceef-3d72-bd99-f7092eefd83a | -14.24296 | -48.06023 | 2025-08-29 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cd94b5d-019c-3439-a052-5ab500f5c23b | -6.22553 | -42.75195 | 2025-08-29 03:49:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2c9cda88-3c3e-3319-8840-3828899b4fbb | -5.9824 | -43.35723 | 2025-08-29 03:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c324c73b-168b-368a-9854-5a34356fb7c3 | -6.43899 | -44.58168 | 2025-08-29 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 10421f11-f610-33f3-a9e4-c407e5d49ead | -11.55115 | -46.37049 | 2025-08-29 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3c81c150-8c55-3299-ac4b-266dd9dc53ad | -15.49386 | -41.5344 | 2025-08-29 03:49:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b7421581-d0f4-3a06-8b37-3d286d438947 | -5.61982 | -45.00974 | 2025-08-29 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 143f02cc-1288-3d82-b1e0-584bbdc694fb | -12.09112 | -44.97509 | 2025-08-29 03:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5ae49be1-10c4-31fb-a17b-5bc0078a5ab6 | -13.41733 | -46.98388 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| fca41485-7d3a-3f8c-99ee-e83f90771559 | -6.44746 | -44.56108 | 2025-08-29 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85644739-8155-3f05-bdf5-a854eec0cab8 | -11.90231 | -46.71994 | 2025-08-29 03:49:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7155db7-0bd5-3f59-a306-819c9a17350e | -13.4963 | -46.84266 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c763309d-ec79-31f1-9c50-4d01f4f9ed76 | -13.40805 | -47.00484 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8798344b-1936-3476-8dbf-e9018644e9d4 | -16.37034 | -39.26113 | 2025-08-29 03:49:00 | NOAA-20 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 466e79f6-4e7b-33e3-aec4-265161d0998c | -9.6858 | -48.31963 | 2025-08-29 03:49:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2873aed0-7014-33a5-a05e-e3a20ba67883 | -10.0216 | -51.11105 | 2025-08-29 03:49:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| fdd34c4a-4c34-3ffa-9560-9d99614c5762 | -5.78401 | -42.57366 | 2025-08-29 03:49:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 8b9d9e95-a6c0-3036-ab5d-ce716d8e4f0b | -12.8161 | -48.10331 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c08f19f-e144-398c-8def-a337d34b4599 | -11.05797 | -44.76352 | 2025-08-29 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71f12a2f-1dc5-3015-95bf-ed81dcb6ae05 | -10.82732 | -47.49521 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 707794a2-0609-3143-8cea-483174eb5a12 | -17.75961 | -44.48141 | 2025-08-29 03:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 438179d6-9f59-321a-8b22-9f6bf61b0923 | -14.62421 | -41.74218 | 2025-08-29 03:49:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a446f69f-7acc-3f82-834d-4773b6a5d6fc | -12.83152 | -48.11295 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| de3f76f5-b6a9-3578-b071-79cba5c806cc | -9.69173 | -48.32033 | 2025-08-29 03:49:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9f75da6-ac8d-3a92-bfc4-631d8385daab | -4.48625 | -47.68161 | 2025-08-29 03:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 940a2e93-caf9-3633-91a7-16c94d5387e2 | -13.1855 | -45.29283 | 2025-08-29 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 63cc0a7b-d2e0-3f26-bac7-12fd651bd4fa | -11.32124 | -43.56913 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2608f95c-9de5-385f-a068-8216a533dc24 | -5.59374 | -45.5232 | 2025-08-29 03:49:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13e24e68-c667-32ef-9da9-8344446e3149 | -12.91937 | -46.34221 | 2025-08-29 03:49:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 91fe4a82-23b5-383f-b163-4eae1661cc01 | -6.51251 | -43.001 | 2025-08-29 03:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0128435f-0d22-307e-945b-9c5ce85679cf | -6.10794 | -43.30956 | 2025-08-29 03:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 212ea1b4-61c5-3f34-abfc-270e29e787b5 | -14.41051 | -42.87257 | 2025-08-29 03:49:00 | NOAA-20 | CANDIBA | BAHIA | Brasil | 2906600 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6b8c09fc-b9df-32c2-a2d0-50d7045a9cea | -6.26361 | -43.81271 | 2025-08-29 03:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 91f238ca-8011-3e19-8ea6-24e6545215ee | -13.54207 | -46.87274 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| de2cc7fa-b04f-3400-82f7-ee05b5472e75 | -11.55065 | -46.37313 | 2025-08-29 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 94f0e5b5-bffc-382f-b79d-0e2cd35e66c9 | -6.49479 | -44.39772 | 2025-08-29 03:49:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c07c1f2e-1970-3d69-93c5-3d9f7dff2bf6 | -13.56105 | -46.90847 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c91ff796-d31a-3dac-8340-ea9fe5c4a7eb | -10.83684 | -47.50449 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b51d124-b8d3-36b4-a9de-bd9eb70e7699 | -11.35157 | -43.54318 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1444726b-d80d-305a-beb8-182a1d1cf5c6 | -12.70073 | -48.19704 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 9b36adcd-1646-3017-b39e-fa32808d5608 | -6.15865 | -44.17915 | 2025-08-29 03:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1cce837c-2fc7-3abd-a348-99b365f04087 | -11.61421 | -47.31284 | 2025-08-29 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a0b6848-b6bb-3317-8721-4f9cbdc8b2ec | -12.69616 | -48.19306 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f95d10a0-a6dd-3466-a0a1-bb6398a81281 | -13.98261 | -46.32868 | 2025-08-29 03:49:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 877d39d5-b1b1-3993-b3ce-d2948e537e3c | -6.21662 | -43.33381 | 2025-08-29 03:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e37b7885-2af9-308e-ba00-c019ab51ad6b | -5.85722 | -42.94901 | 2025-08-29 03:49:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| e4c4f43f-68dd-3aaa-894f-10cd15a4c9e4 | -11.45916 | -47.30884 | 2025-08-29 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 828f0fc3-db47-3429-b2ea-a1fd157b7c53 | -11.08023 | -44.77489 | 2025-08-29 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b5a03295-67bb-3127-abb1-a4fc0ff61fea | -11.23048 | -44.12494 | 2025-08-29 03:49:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 713e1985-0634-3f4a-b83e-7307225cab05 | -13.66078 | -46.87405 | 2025-08-29 03:49:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1db23a26-dc74-3560-9dc0-502f6ad5ad53 | -10.80965 | -46.36074 | 2025-08-29 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7e21205-a31e-3cfc-9a84-6b1803c247fa | -13.40667 | -46.98507 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3df69c9b-4b8e-35fd-bf2e-7ca0f2798909 | -12.80258 | -48.17311 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4aaecf99-76b1-3bae-9237-4c2f0405a411 | -6.25142 | -44.43896 | 2025-08-29 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1da97320-64c4-3b2b-870d-ec851aa8672e | -13.19538 | -45.28995 | 2025-08-29 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 95b119b6-0fd3-3bf8-9e58-b332faf88238 | -6.84301 | -38.35055 | 2025-08-29 03:49:00 | NOAA-20 | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 74d4b7f0-d941-3a0f-9714-96cff49a82e7 | -13.40522 | -46.96563 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6eced51c-5bba-3bf4-8d4d-3e2eb31f0bc2 | -13.18724 | -45.28353 | 2025-08-29 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 7dc39e44-d005-320b-ac0a-faf54274f423 | -6.68969 | -43.0954 | 2025-08-29 03:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b841e745-99c2-3bd8-be2a-7f0f8695f5a0 | -10.38571 | -45.16626 | 2025-08-29 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf5ff36e-6e88-3772-aed2-f1305a183523 | -12.40001 | -46.49702 | 2025-08-29 03:49:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ac363c63-80e1-354f-8899-7b2f9ac429c6 | -10.82932 | -47.48475 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c62d016-35b2-3c0e-89a5-2b7c71385865 | -6.10648 | -43.31828 | 2025-08-29 03:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5a05af91-f109-3f4d-be6d-0013b5d412d2 | -11.94131 | -46.70854 | 2025-08-29 03:49:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67e7f42c-28ab-3fb6-8dad-1c3c5c3af51e | -13.57399 | -46.8679 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 13a56b18-ee3c-3992-b357-3f16e7309fed | -13.1791 | -45.27712 | 2025-08-29 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 872fff65-b90a-3186-bcf9-6de4a6cbab78 | -16.36731 | -39.26083 | 2025-08-29 03:49:00 | NOAA-20 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d2a99b26-3667-38ef-9afb-0eb2d24e655a | -11.11674 | -45.12109 | 2025-08-29 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e0f3b948-ec82-3036-998f-1ef0218ff751 | -10.98163 | -46.85371 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d119a098-0602-3310-8e29-871189761c62 | -16.51172 | -45.10485 | 2025-08-29 03:49:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d02cfc73-a64d-377c-81bb-87064904ad03 | -13.59382 | -46.87213 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6e498f2-67ab-3a63-8558-a0782cbe0b82 | -12.70077 | -48.19878 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 27.1 |
| a305e85b-3492-3ed5-a504-a81a36529e27 | -11.08454 | -44.75149 | 2025-08-29 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README31.md)
