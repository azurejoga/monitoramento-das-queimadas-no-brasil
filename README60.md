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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92ca8544-83d5-3c39-a8f9-73736ac7f22c | -6.19794 | -43.55643 | 2025-08-20 12:14:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 20adc665-5679-3b48-bba2-b5b63dfaea01 | -12.90962 | -46.09461 | 2025-08-20 12:14:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 3573cb87-2a90-3f1f-8f64-1d3682171701 | -12.95458 | -46.17225 | 2025-08-20 12:14:00 | TERRA_M-T | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 53a70959-f5cc-3fb5-8110-c98722fbaf7e | -6.08253 | -45.4013 | 2025-08-20 12:14:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ac74c823-eb56-34ee-8130-6d6e6e5202ef | -5.89852 | -45.27314 | 2025-08-20 12:14:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 37bba043-992b-375e-afa8-def664a8ec06 | -4.79194 | -45.33051 | 2025-08-20 12:14:00 | TERRA_M-T | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 675d4558-c9d0-3b48-a9f7-981f98f2e1c8 | -8.03097 | -47.66087 | 2025-08-20 12:14:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 3647ecb1-c95d-33ad-9401-0265c5bca318 | -6.4665 | -43.6121 | 2025-08-20 12:14:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9bec83e3-0f3e-31a0-8b08-0cd48017cfb0 | -6.58428 | -44.47627 | 2025-08-20 12:14:00 | TERRA_M-T | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e734f64a-4fae-30d6-a2d0-7b1fa7b759a8 | -6.52538 | -45.46767 | 2025-08-20 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 24fc243c-d403-3084-95d2-be1cdfc051b4 | -10.71352 | -48.23816 | 2025-08-20 12:14:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 783c16a2-c5e5-31cb-bae5-4ce9c4dbbc5c | -6.08125 | -45.41011 | 2025-08-20 12:14:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d35cf861-e2d4-361a-a4b9-ce830e7b8589 | -8.21344 | -47.30663 | 2025-08-20 12:14:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6706844a-c97f-3876-adab-bdf147f7f76d | -8.54467 | -47.62732 | 2025-08-20 12:14:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d114432c-4c7a-3adf-a6e4-7947273836bf | -6.9555 | -42.87447 | 2025-08-20 12:14:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.2 |
| 30c82340-4e2f-3dcc-a5ea-104669855e0a | -7.58255 | -44.39686 | 2025-08-20 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 4e0aa0a5-7ff0-3030-aeb6-783388bb7b2a | -3.9843 | -43.24136 | 2025-08-20 12:14:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 9c73d13d-5808-3561-838c-2c6d5923ca49 | -12.87046 | -46.05191 | 2025-08-20 12:14:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| b521cbbd-0665-3c7c-b865-6497e9488bc8 | -7.15729 | -43.48429 | 2025-08-20 12:14:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 30.8 |
| f5d541cb-7f01-312d-8192-a1df1f128de7 | -5.78355 | -43.62237 | 2025-08-20 12:14:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 16408dc5-24fc-3697-b168-a5d5ed9eeb81 | -6.44702 | -45.49558 | 2025-08-20 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| db4bfa2c-1714-3081-bdaa-d545d17c2368 | -12.6489 | -45.32904 | 2025-08-20 12:14:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 15fb2965-4104-36a7-9e37-784323533e4c | -5.96776 | -44.14477 | 2025-08-20 12:14:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 48.7 |
| bd76101e-2834-3c5a-a45e-c7d9cffeb76b | -6.46212 | -45.51572 | 2025-08-20 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7265a6bd-7550-3834-84d0-2bee4a302bd9 | -8.8347 | -45.57139 | 2025-08-20 12:14:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 2104e18a-f1f1-38b3-b0f1-ba62cd82d9b7 | -6.12839 | -42.55111 | 2025-08-20 12:14:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 02e0d89d-ed61-37ac-92c2-9ed10023c03d | -5.27987 | -43.59803 | 2025-08-20 12:14:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 95376fb3-2639-3574-ad63-61609ef52358 | -5.79656 | -44.76142 | 2025-08-20 12:14:00 | TERRA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ba3eca02-035c-3a71-808f-be448d07fc75 | -10.43769 | -47.61594 | 2025-08-20 12:14:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5bf76648-1795-394b-aa7a-98e47d0c5337 | -8.02949 | -47.67079 | 2025-08-20 12:14:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 27.3 |
| b867a507-3300-33d6-a853-4c0f508aa447 | -7.23467 | -44.70802 | 2025-08-20 12:14:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| cb3b4346-e3cb-311f-87ac-db172138d7ba | -7.66211 | -45.2614 | 2025-08-20 12:14:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 1bfb0315-1997-3ffa-b4ca-56eb08cbc68b | -10.81341 | -43.28278 | 2025-08-20 12:14:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 13.8 |
| a9857d85-cd3c-34e2-902a-29da23a316c6 | -5.61126 | -43.4712 | 2025-08-20 12:14:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8c604298-ce02-3a19-90d9-3797f696b1d2 | -8.1775 | -47.36011 | 2025-08-20 12:14:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8aa96213-1a68-31c9-b3d1-c28d7733cfa4 | -9.85466 | -44.68878 | 2025-08-20 12:14:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 6a6747a5-fc94-3b4a-b02b-c44ebe0ab44c | -8.29386 | -47.62773 | 2025-08-20 12:14:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 9ff19727-54fc-32d1-96cf-f10d25671a39 | -7.58239 | -45.42447 | 2025-08-20 12:14:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 0245a8e8-4092-39fc-a501-1fdac21fe8a5 | -10.60476 | -48.60169 | 2025-08-20 12:14:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8bb2c3f2-12cb-36e8-9804-49ac2ced7639 | -7.1127 | -44.65104 | 2025-08-20 12:14:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 39646dd6-0b1d-300e-9b73-249241ed88e5 | -12.94701 | -46.16188 | 2025-08-20 12:14:00 | TERRA_M-T | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| dd0845fb-3ff6-393d-a399-7bfb40dc5e35 | -12.99564 | -45.2198 | 2025-08-20 12:14:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a7f362a7-83d3-3588-af3b-7d756019120e | -9.80479 | -47.84172 | 2025-08-20 12:14:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 826c32b2-1b1f-34f8-8ca2-2ea1dcd03696 | -6.01764 | -44.11475 | 2025-08-20 12:14:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 34081677-8a4e-3412-8ec3-0b1b9d252da8 | -10.60638 | -48.59084 | 2025-08-20 12:14:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 28c418e9-e819-3e2f-a4d8-a6aeaaaa8938 | -8.36818 | -47.50894 | 2025-08-20 12:14:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 993d4359-a4a8-3a4a-b082-b8659ca62b66 | -6.60098 | -43.90483 | 2025-08-20 12:14:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| dd00868b-87b2-3ad0-bbfb-58aaa2584160 | -6.03924 | -44.3542 | 2025-08-20 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| b119ec52-ccaa-379b-822a-c54bfa1e03ef | -12.87804 | -46.06226 | 2025-08-20 12:14:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 84e242f9-9247-3006-91ba-36900a13e316 | -12.66263 | -44.96301 | 2025-08-20 12:14:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 115.4 |
| a1a98710-de79-39d8-9b6f-bf3f2acf7be5 | -8.79446 | -45.47515 | 2025-08-20 12:14:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 448ab8e7-4364-3d09-8335-8a2c6b08c8d6 | -12.90834 | -46.10363 | 2025-08-20 12:14:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fde42ba1-5be4-3a56-8fbc-cda937692d76 | -6.08698 | -44.4124 | 2025-08-20 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 916ceeb1-7ba2-3a9e-b363-57ce2282f4bc | -11.1307 | -46.98161 | 2025-08-20 12:14:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| c2b2dbf8-2dc1-36b2-8f08-cbeffef149df | -12.08863 | -44.72183 | 2025-08-20 12:14:00 | TERRA_M-T | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 750ba525-56da-3f8d-a7cd-5c3d0f020771 | -8.30893 | -46.97121 | 2025-08-20 12:14:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 58014771-70b3-39cd-9247-535a79a90be3 | -12.64063 | -46.88591 | 2025-08-20 12:14:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| eba64ce7-0d8c-3cdb-98e8-73f5428a8e47 | -6.43693 | -45.50317 | 2025-08-20 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| d243d41f-217f-39cd-8375-4ece3bd123ef | -12.09259 | -47.90854 | 2025-08-20 12:14:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 1c1e411a-9e7c-3f1a-b40a-2f90f9e173b2 | -9.87139 | -44.70059 | 2025-08-20 12:14:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 6b4e2e54-2108-3c65-9449-249e20b278e0 | -4.86913 | -45.2484 | 2025-08-20 12:14:00 | TERRA_M-T | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 1dc811a0-9d74-3878-9c2c-5dec6eea084a | -8.80837 | -45.44086 | 2025-08-20 12:14:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cc4cac0e-cd07-3614-afdf-4f75f15c474f | -6.09195 | -44.69464 | 2025-08-20 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ef648777-6f4b-34df-8351-5b194408d60a | -13.08103 | -46.82845 | 2025-08-20 12:14:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9425282c-c358-34f7-93ec-6ee5b7ecd414 | -5.89872 | -46.1597 | 2025-08-20 12:14:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 052e534f-9fa7-3577-a69e-ebd7500505de | -6.10079 | -44.69588 | 2025-08-20 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| bae4d348-14f4-350d-978b-f9405c054081 | -7.66338 | -45.25255 | 2025-08-20 12:14:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 43.8 |
| a63dca55-31e2-3a43-ac26-71dd66e946cb | -10.81491 | -43.27172 | 2025-08-20 12:14:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 23.6 |
| 82806e3d-82d2-3ffa-b84f-336a748ca162 | -12.66395 | -44.95337 | 2025-08-20 12:14:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 81e70120-1f7e-3d57-9965-9a6d5190b27d | -12.95331 | -46.18121 | 2025-08-20 12:14:00 | TERRA_M-T | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 363b6e52-c0c3-3ec0-9006-0e979ec26de0 | -7.02835 | -44.59634 | 2025-08-20 12:14:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c3b7fa94-1273-3453-991d-eca8b58f1207 | -6.73417 | -44.33509 | 2025-08-20 12:14:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b89627ff-0696-3f74-ad91-d224389fe0f5 | -12.38262 | -49.98623 | 2025-08-20 12:14:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| c3764b71-1244-3cb9-a48f-70fc32f8f814 | -3.98541 | -42.5158 | 2025-08-20 12:14:00 | TERRA_M-T | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 532b595e-71a1-3ceb-96a3-fb05c83ddbbc | -10.93316 | -42.22982 | 2025-08-20 12:14:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 39382429-7733-3475-b7a6-c7f58f3d8f15 | -8.83642 | -52.04673 | 2025-08-20 12:14:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| d553c1d1-95d9-3c21-b29e-8e4175faa104 | -5.85105 | -39.03993 | 2025-08-20 12:14:00 | TERRA_M-T | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 40.9 |
| 5012c494-73d9-34fe-bf8b-ef2a18502895 | -12.08728 | -44.73154 | 2025-08-20 12:14:00 | TERRA_M-T | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 6d3e1a50-4e2f-3437-8448-c8822ce30778 | -6.95693 | -42.864 | 2025-08-20 12:14:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.6 |
| b643d79d-1176-398b-88b1-7a671e3eddb4 | -6.94597 | -42.87312 | 2025-08-20 12:14:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 34.2 |
| 8ab9241a-0f85-316a-9023-83e072365b59 | -9.51668 | -47.22899 | 2025-08-20 12:14:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 31.0 |
| c06240b7-c5ca-39a3-a19a-8255d911466e | -5.9767 | -44.14603 | 2025-08-20 12:14:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 87a2f9d9-91d4-3e9c-92ea-d5daca50f3d5 | -8.7831 | -45.49167 | 2025-08-20 12:14:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1546e3d1-1d2c-3db5-8859-ec455548bc73 | -7.29644 | -43.67382 | 2025-08-20 12:14:00 | TERRA_M-T | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| c10c9ff2-27d6-3492-92d9-d124570701be | -8.76819 | -44.74511 | 2025-08-20 12:14:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7fe60ad8-d956-34c8-9b46-aed6f8d71705 | -7.58366 | -45.41563 | 2025-08-20 12:14:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 00f14a5e-a333-3823-86a8-ccb6350c0466 | -13.02937 | -46.81163 | 2025-08-20 12:14:00 | TERRA_M-T | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| ab8f5e2c-a5c6-339a-9202-94b01b0b839c | -6.61895 | -39.17521 | 2025-08-20 12:14:00 | TERRA_M-T | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 21.0 |
| 7ee1626d-4e9a-33de-a69e-96c910c27ad2 | -12.6566 | -45.33966 | 2025-08-20 12:14:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 2778386f-0d34-33dc-b82a-410b059991be | -8.02017 | -47.66948 | 2025-08-20 12:14:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| e8cd4da4-0c9e-37b8-b47d-f4d9a53e16b8 | -13.14201 | -42.54972 | 2025-08-20 12:14:00 | TERRA_M-T | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 02f3d8a7-0153-3171-a864-be57eebdca71 | -6.48892 | -45.20481 | 2025-08-20 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e874b993-1f8e-3e79-bf0f-9cfa45f73cee | -6.36015 | -43.65304 | 2025-08-20 12:14:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7bd9ebd8-de89-3afa-ac7f-22236bac8f3b | -19.66694 | -48.67047 | 2025-08-20 12:17:00 | TERRA_M-T | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 40.1 |
| d5e2bc9a-23b2-3ba6-948e-ca2a431c95ca | -15.5489 | -40.71801 | 2025-08-20 12:17:00 | TERRA_M-T | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 23.5 |
| 5e2df648-88f0-3da3-9967-2e2c0cb1ee49 | -13.332 | -54.42601 | 2025-08-20 12:17:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 0f2440af-c361-36bd-8027-8af5b3b3f9c1 | -13.86187 | -45.54879 | 2025-08-20 12:17:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 0d0a1642-513c-38b2-91a5-86204cd98283 | -17.27026 | -46.93355 | 2025-08-20 12:17:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 63949052-1ddf-30f9-b8fb-397f98950dc5 | -18.15872 | -44.55235 | 2025-08-20 12:17:00 | TERRA_M-T | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 120cf5b4-2b90-3664-b8d2-610bb1da3404 | -17.68303 | -44.44778 | 2025-08-20 12:17:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |


[Clique aqui para ver as próximas entradas](README61.md)
