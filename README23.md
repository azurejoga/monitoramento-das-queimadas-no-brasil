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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ef0ee02-b545-39a9-b2e6-4be55df7d4b3 | -10.81493 | -50.65332 | 2026-08-31 03:55:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a142bdef-74ef-37b6-9c26-12bb59898dd7 | -11.22277 | -45.14701 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34f95361-caa8-3bbf-9941-ecd5bf88f9e0 | -12.098 | -45.05933 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 966a574d-ee84-3348-ba40-122d966be9b0 | -12.94234 | -45.91364 | 2026-08-31 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 989f2f1e-5c4b-32d9-8c9c-9e3616f99df8 | -11.36082 | -45.21165 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 65f13fd5-2821-317a-a9fa-236f44d86eb3 | -12.09916 | -45.05328 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7de975df-f787-3569-be65-16498c9ee6cc | -12.42926 | -42.88198 | 2026-08-31 03:55:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9c11a571-5038-3560-a7ff-558ec918da9c | -14.07699 | -42.45253 | 2026-08-31 03:55:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1cb80fc9-c11e-388f-bfeb-792418e58dc6 | -15.66678 | -45.93773 | 2026-08-31 03:55:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 04fc15cc-1354-37d2-b0e8-2ba95939dd48 | -11.34596 | -45.20538 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2aeeb6e4-051b-358b-a7a8-6da1220a8f33 | -15.18954 | -46.24572 | 2026-08-31 03:55:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4743eca-a0ae-3662-b02d-cff42763378e | -16.28246 | -42.57902 | 2026-08-31 03:55:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f838a066-ba4d-3645-ad44-480c4ca22165 | -11.2226 | -45.09201 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24fafaac-9115-3ba4-8e6e-2b98edf90ab8 | -13.36774 | -46.92575 | 2026-08-31 03:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eca92050-7856-3f33-a4e5-335de35655a2 | -10.15945 | -45.72338 | 2026-08-31 03:55:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d5ebe1bf-54a7-38d1-8950-cc8efe38770f | -12.95173 | -45.94976 | 2026-08-31 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 78b63c24-53e6-350f-b112-cf0ee5900e92 | -11.34653 | -45.20242 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4be1721d-1101-30b7-8d16-93f6544ac531 | -12.39547 | -46.44939 | 2026-08-31 03:55:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 62ef2495-e4fc-377d-9c92-2a5ed4b37f5d | -11.78839 | -47.6643 | 2026-08-31 03:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ad1a3bf-4313-3498-8596-44420b9655a9 | -12.13226 | -45.8382 | 2026-08-31 03:55:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be0ceaef-fe96-3a3d-8e20-1e613c65e143 | -11.34194 | -45.19842 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ac3e420-8093-3401-9176-00dbd78da747 | -12.39476 | -46.45299 | 2026-08-31 03:55:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8d9c9302-35d8-3a1f-bcbd-2b917a2487e3 | -10.15672 | -45.73781 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b6b00d41-37a6-36d9-be14-5f68394058e4 | -10.44532 | -46.75945 | 2026-08-31 03:55:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4cad30c6-446c-3dc2-8f70-1a268faa8571 | -15.19154 | -46.23981 | 2026-08-31 03:55:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 237f17fc-7918-3113-ac47-e571e20f9c0b | -12.9009 | -45.84733 | 2026-08-31 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b29f534-3dca-3664-bc3f-3ad39f5a57df | -12.92054 | -45.85799 | 2026-08-31 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a450860-e1ee-3ad5-bb9f-82cacbabd27d | -18.28726 | -52.68543 | 2026-08-31 03:57:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c05006e8-1b37-35e4-91f4-dd2d9baf78cd | -18.27608 | -52.71117 | 2026-08-31 03:57:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8d416c87-5e42-3739-8ba0-0d679d451c3d | -17.27946 | -46.00371 | 2026-08-31 03:57:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc390496-b828-3072-96d4-e7322112e384 | -17.51206 | -44.23204 | 2026-08-31 03:57:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21615299-7f03-3e30-9771-9f58060b2ca8 | -17.49336 | -44.46837 | 2026-08-31 03:57:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e988e7e-1928-3d4e-a265-7637a5cf6107 | -18.14841 | -46.11183 | 2026-08-31 03:57:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c2f681a3-5bea-39cb-8781-9c07586efd7d | -20.44596 | -47.59437 | 2026-08-31 03:57:00 | NPP-375D | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1d6e0ad-730f-347c-bf96-a4d7bd6456f4 | -17.28431 | -46.00481 | 2026-08-31 03:57:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cbce3da7-f1be-3f62-bdfc-f6deade2a002 | -20.36502 | -47.46212 | 2026-08-31 03:57:00 | NPP-375D | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8a96ce1-2c6b-353c-88ce-dc11b11c9110 | -18.27958 | -52.69693 | 2026-08-31 03:57:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6bd2bba1-a577-3423-9185-0b863a9e8729 | -18.28022 | -52.68357 | 2026-08-31 03:57:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3e4406bf-1620-3710-bba5-1d1dd8241aed | -17.49419 | -44.47083 | 2026-08-31 03:57:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe1a16b8-eecc-32d1-89b6-372eabfd14db | -18.28311 | -52.68264 | 2026-08-31 03:57:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 07950abd-92aa-3660-8198-e052e987404f | -18.27783 | -52.70405 | 2026-08-31 03:57:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4e021bf0-370b-3f9a-b143-63eaa7b9618f | -19.95211 | -42.30721 | 2026-08-31 03:57:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a471b4aa-ff72-3a04-8429-1ea0355d36f4 | -20.36874 | -47.45921 | 2026-08-31 03:57:00 | NPP-375D | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 8.6 |
| af48a358-fe82-304f-844f-ded71b414414 | -17.25415 | -44.86696 | 2026-08-31 03:57:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6923fac1-9a0c-31cb-b7aa-6db8c6ceacb3 | -18.27498 | -52.67423 | 2026-08-31 03:57:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| da12dead-4634-3103-a926-f2001509c97b | -18.68999 | -40.72568 | 2026-08-31 03:57:00 | NPP-375D | BARRA DE SÃO FRANCISCO | ESPÍRITO SANTO | Brasil | 3200904 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6ed2fd02-ac69-3888-897d-b662e5db16a5 | -17.49775 | -44.46928 | 2026-08-31 03:57:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de590e40-17fe-3a7c-8f13-fe5e465dcec1 | -17.25322 | -44.87176 | 2026-08-31 03:57:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1626934c-d1f0-3a2f-9a34-8c2a73d68ecb | -18.69069 | -40.7216 | 2026-08-31 03:57:00 | NPP-375D | BARRA DE SÃO FRANCISCO | ESPÍRITO SANTO | Brasil | 3200904 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 837f76b3-1003-3830-b9ab-37f91f6816a1 | -18.28195 | -52.67636 | 2026-08-31 03:57:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5711235e-6bc9-33d8-9beb-4b9aa39c1d66 | -18.29015 | -52.68445 | 2026-08-31 03:57:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b8cf1f6-0333-326d-bf8e-5d4068d69713 | -17.99441 | -44.31166 | 2026-08-31 03:57:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f19a05df-f5d7-3c4f-bd9e-424eba5794e0 | -19.95373 | -42.30495 | 2026-08-31 03:57:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ed348ac2-140d-3f27-a68e-9dde6becfc0e | -19.08036 | -40.07313 | 2026-08-31 03:57:00 | NPP-375D | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0b1f4491-974f-3849-8eb1-b674faf02804 | -18.27332 | -52.71231 | 2026-08-31 03:57:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| de38db0c-3cfa-3581-b35c-e4fef43c11a7 | -20.46547 | -44.41632 | 2026-08-31 03:57:00 | NPP-375D | PIRACEMA | MINAS GERAIS | Brasil | 3150604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 76bbd62b-e9c6-3bfa-a6ae-915673f3c6d2 | -18.2732 | -52.68166 | 2026-08-31 03:57:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 89d44da1-2754-3b32-8b61-62d582212db6 | -18.28487 | -52.67547 | 2026-08-31 03:57:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b0ed12c9-9eb4-38f8-89f0-000b0d780026 | -20.36805 | -47.46243 | 2026-08-31 03:57:00 | NPP-375D | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4bdb7e42-a6d8-3ce4-abb4-9a96571dd4bb | -20.36569 | -47.45889 | 2026-08-31 03:57:00 | NPP-375D | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f2358f65-5daf-3d7f-ad26-e4ba3a5c4456 | -17.53385 | -52.55958 | 2026-08-31 03:57:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e52efb6a-d4bf-3601-9b33-67f3d9c88de8 | -17.50693 | -44.23545 | 2026-08-31 03:57:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5151d0d-0242-3e3b-922b-2f3a4713ad21 | -18.28386 | -52.69961 | 2026-08-31 03:57:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47e6a00e-19e6-3c7d-b7e1-645a99352bd9 | -17.53896 | -44.61173 | 2026-08-31 03:57:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2452e459-d491-370c-bd6d-b25b3c2c1ca9 | -20.46631 | -44.41201 | 2026-08-31 03:57:00 | NPP-375D | PIRACEMA | MINAS GERAIS | Brasil | 3150604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 615ef11f-04c3-3c11-b0fe-8e1c0ef0e213 | -18.27608 | -52.68078 | 2026-08-31 03:57:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 2c3867b7-4e7f-3104-9921-0ce11f77ac33 | -20.2928 | -40.39254 | 2026-08-31 03:57:00 | NPP-375D | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 32e4321f-177f-3735-bca8-5adb054357e1 | -17.28751 | -46.00434 | 2026-08-31 03:57:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f9ac0da9-753f-3af0-aca0-b5dceb2a902f | -20.46971 | -44.41675 | 2026-08-31 03:57:00 | NPP-375D | PIRACEMA | MINAS GERAIS | Brasil | 3150604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7714fec9-f127-3a79-a610-51bb607fec7e | -18.52409 | -42.84947 | 2026-08-31 03:57:00 | NPP-375D | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f8eb7821-2973-39b5-886a-9784084e972d | -20.36944 | -47.45598 | 2026-08-31 03:57:00 | NPP-375D | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 4c0c401d-2e5c-3429-9fec-13635565bb95 | -17.99011 | -44.31073 | 2026-08-31 03:57:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5bd6d198-3e2d-3dce-9bf0-f0700d811323 | -18.28555 | -52.69255 | 2026-08-31 03:57:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa4afbdd-9523-3ed1-ae18-080d7616dacb | -20.44661 | -47.59125 | 2026-08-31 03:57:00 | NPP-375D | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5d23e4f7-ef09-3de0-a771-a6fc9ae78b1a | -20.44854 | -47.59547 | 2026-08-31 03:57:00 | NPP-375D | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f03bb33-d5bc-388b-82e6-8c0e9e44a115 | -18.27505 | -52.70511 | 2026-08-31 03:57:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d959b8f2-9d7a-3aec-aa8a-fd2f86baa194 | -18.27787 | -52.67351 | 2026-08-31 03:57:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 38fb6a59-d819-3d67-a4b5-21672ab2d47c | -17.53359 | -44.61572 | 2026-08-31 03:57:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 98234069-1fa8-3ece-a1e5-2cf3e692956e | -20.36436 | -47.46531 | 2026-08-31 03:57:00 | NPP-375D | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 923054c2-bbaa-3dbb-b896-8c29423f89ce | -17.28266 | -46.00323 | 2026-08-31 03:57:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc5d7a7e-ee94-3dfa-92f5-10c304d6f09d | -18.14628 | -46.11299 | 2026-08-31 03:57:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 569c2c7a-935c-333a-bad4-8287e1fc6727 | -17.52682 | -52.55748 | 2026-08-31 03:57:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed2b9fa6-a629-3549-bde4-1210148164c2 | -17.49504 | -44.46633 | 2026-08-31 03:57:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4aece6a4-5a4a-3332-aa84-179920dd88c3 | -20.44922 | -47.59234 | 2026-08-31 03:57:00 | NPP-375D | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6d9a4de-285f-3d5f-b3cc-46977532a995 | -20.36305 | -47.46118 | 2026-08-31 03:57:00 | NPP-375D | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cac9ab5e-6e21-3ae8-8d3e-d6e9bf05f2f3 | -17.29023 | -46.00072 | 2026-08-31 03:57:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09f5cbe9-9e41-314c-9a10-b6db5c022df1 | -6.1294 | -57.6833 | 2026-08-31 04:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 3322aba1-88bc-3317-ad3f-dea16a48e7c3 | -5.2548 | -55.8907 | 2026-08-31 04:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 1961c4a2-7797-3fc7-8f91-1da272fc83ad | -5.2363 | -55.8914 | 2026-08-31 04:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 212037d5-6ee7-3ec7-9dfe-c36e8eeb6972 | -6.1295 | -57.6637 | 2026-08-31 04:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 84be379e-60cf-3ea0-8975-9802d6343bf7 | -5.2547 | -55.9105 | 2026-08-31 04:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 143.4 |
| 837a6828-9bf3-3622-8659-9ff9af418879 | -5.2362 | -55.9112 | 2026-08-31 04:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 6ae50f4a-6b2a-3077-96b6-d004f78274aa | -6.6035 | -58.6166 | 2026-08-31 04:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 218c375d-e5f3-3e3b-ac76-4817a7e81abd | -5.2363 | -55.8914 | 2026-08-31 04:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| bf00ff00-9c90-35a9-98fd-f83e33fd5941 | -6.6036 | -58.5972 | 2026-08-31 04:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 125.0 |
| b116e9ae-29bf-3ccb-bf1b-e7c64a8da64a | -6.1295 | -57.6637 | 2026-08-31 04:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 4553d408-658b-38d9-8ebc-d6062fa99aeb | -5.2547 | -55.9105 | 2026-08-31 04:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 149.6 |
| bd682b57-85b6-3075-8f3e-3db853d6b4c7 | -6.1294 | -57.6833 | 2026-08-31 04:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 03724855-17f5-3335-ac42-eebc82bbebb0 | -5.2362 | -55.9112 | 2026-08-31 04:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| db7a3d2f-05a0-30e3-8778-cbe007cc1653 | -7.3119 | -60.5706 | 2026-08-31 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |


[Clique aqui para ver as próximas entradas](README24.md)
