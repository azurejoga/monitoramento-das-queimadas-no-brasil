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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bdc0cb84-d5d1-3450-91e0-e631e5f21439 | -21.72561 | -43.95006 | 2026-09-28 17:05:00 | NOAA-21 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.6 |
| e7378162-cfc3-3509-8f54-dd83a87611ef | -20.77513 | -51.29885 | 2026-09-28 17:05:00 | NOAA-21 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.4 |
| 8645f948-4e78-3fda-9d5e-139aa4f7adac | -19.78746 | -42.02334 | 2026-09-28 17:05:00 | NOAA-21 | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 77e6b3fc-8e3e-3662-b995-18b01ec39915 | -23.14523 | -52.38469 | 2026-09-28 17:05:00 | NOAA-21 | ALTO PARANÁ | PARANÁ | Brasil | 4100608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d3d71e84-7345-3373-8130-fe4c3aadd164 | -19.21379 | -42.61097 | 2026-09-28 17:05:00 | NOAA-21 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 132c6309-bb21-3a14-862d-64f78840e8d1 | -20.8784 | -51.45987 | 2026-09-28 17:05:00 | NOAA-21 | CASTILHO | SÃO PAULO | Brasil | 3511003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 84.2 |
| 4b765654-93fb-39c3-9ce0-21c0ca63765a | -20.87554 | -44.11852 | 2026-09-28 17:05:00 | NOAA-21 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 2b4f72c5-ea0f-3324-9f4c-c33a93f9ece0 | -22.84875 | -49.36523 | 2026-09-28 17:05:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 70b8bbfc-0b6c-399e-ad4c-4d8010f18453 | -21.51769 | -44.05096 | 2026-09-28 17:05:00 | NOAA-21 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 60b01fd0-2fca-3089-a108-4cf984a248f8 | -21.40443 | -45.28674 | 2026-09-28 17:05:00 | NOAA-21 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 904b0f4c-ac76-343b-9fea-58c5a1f8dda3 | -20.84615 | -46.26575 | 2026-09-28 17:05:00 | NOAA-21 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6d257205-7d0f-382b-8899-b0bc62f6d9d0 | -23.02474 | -51.86923 | 2026-09-28 17:05:00 | NOAA-21 | SANTA FÉ | PARANÁ | Brasil | 4123402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b32649d9-e843-3063-ba2e-46053da8fe54 | -21.21561 | -46.70669 | 2026-09-28 17:05:00 | NOAA-21 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| 19482d6a-d50c-3cc7-9939-c2f3f843d68c | -23.14578 | -52.38847 | 2026-09-28 17:05:00 | NOAA-21 | ALTO PARANÁ | PARANÁ | Brasil | 4100608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| b93e803c-91e4-3870-9f4b-6ad7dc22f144 | -22.20692 | -56.03021 | 2026-09-28 17:05:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 90c3fdec-4fa3-3a3a-b95e-4f9cbbfe0ee8 | -21.07148 | -45.88868 | 2026-09-28 17:05:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| f632383e-1516-358b-9fd4-3dc871476443 | -24.25436 | -54.28802 | 2026-09-28 17:05:00 | NOAA-21 | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 9fd53c4c-0b16-354b-afbb-380d83dd0fa8 | -21.23741 | -45.61789 | 2026-09-28 17:05:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| eff66479-fdfd-35a5-983f-7e031ad36cb3 | -22.65782 | -50.08755 | 2026-09-28 17:05:00 | NOAA-21 | CAMPOS NOVOS PAULISTA | SÃO PAULO | Brasil | 3509809 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5f3cb6a7-6091-3c2c-bbd6-3ded24521f81 | -20.76026 | -51.31296 | 2026-09-28 17:05:00 | NOAA-21 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 44.3 |
| 1948816f-8515-3aac-9026-52bb06daa3a8 | -21.04955 | -45.75342 | 2026-09-28 17:05:00 | NOAA-21 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e56a9f87-84b2-3192-bc37-8eeac8fffcf4 | -21.55219 | -46.37613 | 2026-09-28 17:05:00 | NOAA-21 | CABO VERDE | MINAS GERAIS | Brasil | 3109501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 8d063b51-7125-328c-aaa8-adaf43f3e08b | -21.36632 | -43.79624 | 2026-09-28 17:05:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| b70ccf8d-eb98-3544-8f8b-dade32b69617 | -20.04087 | -47.73095 | 2026-09-28 17:05:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f35e90e5-5b65-3bd1-9fa0-6db515011de0 | -23.09993 | -50.92042 | 2026-09-28 17:05:00 | NOAA-21 | RANCHO ALEGRE | PARANÁ | Brasil | 4121307 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| 3a2aaa01-e8ad-32da-933d-c33e8135471b | -20.85712 | -43.29466 | 2026-09-28 17:05:00 | NOAA-21 | BRÁS PIRES | MINAS GERAIS | Brasil | 3108701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| f1527ce2-5f06-3adc-9fb7-1522d7c2e7d1 | -23.3196 | -50.91159 | 2026-09-28 17:05:00 | NOAA-21 | JATAIZINHO | PARANÁ | Brasil | 4112702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 9a7870ec-3321-3a14-8dc0-b86a979619e8 | -21.24119 | -45.38548 | 2026-09-28 17:05:00 | NOAA-21 | COQUEIRAL | MINAS GERAIS | Brasil | 3118700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 463fc6cd-2442-3004-acf2-314d58182867 | -20.79751 | -45.35158 | 2026-09-28 17:05:00 | NOAA-21 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 899b9fe1-413b-3955-8d1a-e7936e7f8f35 | -21.06816 | -45.6209 | 2026-09-28 17:05:00 | NOAA-21 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6d7a1f94-bad2-31f9-bd4e-24fef799b211 | -21.01828 | -44.99438 | 2026-09-28 17:05:00 | NOAA-21 | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| dd26c085-a852-3599-bbfb-6d4bdf75a694 | -20.40226 | -41.20559 | 2026-09-28 17:05:00 | NOAA-21 | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 236213cf-e83a-37d1-8127-7c0037bb666d | -22.63461 | -54.94847 | 2026-09-28 17:05:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 63.6 |
| 1ec258ce-b673-36d7-9ab8-f03d65c29492 | -19.51223 | -42.02224 | 2026-09-28 17:05:00 | NOAA-21 | SÃO DOMINGOS DAS DORES | MINAS GERAIS | Brasil | 3160959 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 27b7506c-2250-307d-a16a-7a6a4edb462e | -21.72441 | -41.26369 | 2026-09-28 17:05:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 8f09368a-a1b3-37e4-abbe-b16475091e2e | -20.04812 | -48.05497 | 2026-09-28 17:05:00 | NOAA-21 | ÁGUA COMPRIDA | MINAS GERAIS | Brasil | 3100708 | 31 | 33 | nan | nan | nan | Cerrado | 44.6 |
| e42ea8f9-1b8b-33d4-935f-a695d263de81 | -21.08957 | -43.26274 | 2026-09-28 17:05:00 | NOAA-21 | MERCÊS | MINAS GERAIS | Brasil | 3141603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 381b5cba-58f9-3b4a-ad79-73d6076eed77 | -21.84169 | -44.4075 | 2026-09-28 17:05:00 | NOAA-21 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| e79c2fab-1ae8-3e8b-a5c3-984bfa133c51 | -20.04395 | -48.05362 | 2026-09-28 17:05:00 | NOAA-21 | ÁGUA COMPRIDA | MINAS GERAIS | Brasil | 3100708 | 31 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 3b412a7e-b7d7-3e3a-9380-8addfbed0f78 | -20.15833 | -41.4388 | 2026-09-28 17:05:00 | NOAA-21 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 7c7e4f43-de27-3fd8-87ca-50783575d61f | -21.82904 | -45.77986 | 2026-09-28 17:05:00 | NOAA-21 | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 9d7cdf60-9e83-3ea4-a9f0-aee4b3e93a47 | -21.48508 | -45.78824 | 2026-09-28 17:05:00 | NOAA-21 | FAMA | MINAS GERAIS | Brasil | 3125200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ec16cb08-2fbd-34fe-831a-912099a6def8 | -19.23316 | -40.26904 | 2026-09-28 17:05:00 | NOAA-21 | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| bf8b2d49-4de1-328a-a974-fe3b6d0b5ef1 | -22.24883 | -44.66763 | 2026-09-28 17:05:00 | NOAA-21 | ITAMONTE | MINAS GERAIS | Brasil | 3133006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| 0a699b2c-34b0-340c-b367-e688e91efafa | -21.23728 | -43.94209 | 2026-09-28 17:05:00 | NOAA-21 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 387462d8-404f-3961-a486-a8611705749d | -19.02336 | -42.34079 | 2026-09-28 17:05:00 | NOAA-21 | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| a7094a2d-3295-39cc-b0a1-930ffc9c3ecc | -21.328 | -43.97037 | 2026-09-28 17:05:00 | NOAA-21 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 81b03b1e-e8ac-3478-b5dc-9fc03806c9e5 | -21.32604 | -42.60546 | 2026-09-28 17:05:00 | NOAA-21 | SANTANA DE CATAGUASES | MINAS GERAIS | Brasil | 3158409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| f5f5196b-0cee-30e2-8752-2771395035cf | -19.58944 | -45.02644 | 2026-09-28 17:05:00 | NOAA-21 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| 7a4fe428-f577-3fbe-b8a2-68a73c912564 | -22.07755 | -45.09706 | 2026-09-28 17:05:00 | NOAA-21 | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 4224f05c-2062-3716-a5ab-9f659f852bad | -21.85935 | -45.46467 | 2026-09-28 17:05:00 | NOAA-21 | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 61e3276b-6b4e-3a90-9c16-f28117e0e267 | -22.63101 | -54.94901 | 2026-09-28 17:05:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 5acbb327-c14e-33b1-be74-8b87f94f8d87 | -22.85219 | -49.36459 | 2026-09-28 17:05:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 52f696c1-e4b0-3b43-b103-e5653c6acc9c | -23.11647 | -52.34686 | 2026-09-28 17:05:00 | NOAA-21 | ALTO PARANÁ | PARANÁ | Brasil | 4100608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 31.7 |
| 68680ee6-5983-33ac-ac2e-ccb145071d87 | -21.61788 | -44.40505 | 2026-09-28 17:05:00 | NOAA-21 | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 35.9 |
| 091c7a64-e6c6-3ea0-842e-8347de6e0b21 | -19.87988 | -44.93385 | 2026-09-28 17:05:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f3bc472c-933b-3578-93fa-2723212afbf5 | -20.77904 | -51.30196 | 2026-09-28 17:05:00 | NOAA-21 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| dec00fe4-6d9d-37d1-9715-c0fc473495df | -20.81653 | -47.07963 | 2026-09-28 17:05:00 | NOAA-21 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 2aa4e3bd-d72e-38ef-aaed-fffc5cd65cfc | -20.04857 | -48.05764 | 2026-09-28 17:05:00 | NOAA-21 | ÁGUA COMPRIDA | MINAS GERAIS | Brasil | 3100708 | 31 | 33 | nan | nan | nan | Cerrado | 46.7 |
| d825ac05-41f1-3b26-8908-7b065b26d0e3 | -20.3718 | -50.27159 | 2026-09-28 17:05:00 | NOAA-21 | FERNANDÓPOLIS | SÃO PAULO | Brasil | 3515509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a0744ed6-3aa5-3ea9-8717-7fbb51bd8dc6 | -20.64966 | -44.38217 | 2026-09-28 17:05:00 | NOAA-21 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 6002135b-4b73-37db-a9de-5eac16377dfb | -23.21058 | -46.82316 | 2026-09-28 17:05:00 | NOAA-21 | VÁRZEA PAULISTA | SÃO PAULO | Brasil | 3556503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 77d2acac-b1b1-3528-89cf-81282c2300e5 | -20.0477 | -48.05282 | 2026-09-28 17:05:00 | NOAA-21 | ÁGUA COMPRIDA | MINAS GERAIS | Brasil | 3100708 | 31 | 33 | nan | nan | nan | Cerrado | 30.1 |
| a8d003fe-3d5f-3165-9ee8-eaf8831c5ca1 | -21.5409 | -47.12432 | 2026-09-28 17:05:00 | NOAA-21 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 88142b84-ffa5-3c07-98b0-946ded628f6a | -21.35289 | -45.49041 | 2026-09-28 17:05:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| c2014b47-1fb2-3be3-9859-77bcd74e1e3a | -22.61106 | -44.77396 | 2026-09-28 17:05:00 | NOAA-21 | AREIAS | SÃO PAULO | Brasil | 3503505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 5562cdfa-0991-322e-887b-3a5d3bb5a06b | -20.04002 | -42.98433 | 2026-09-28 17:05:00 | NOAA-21 | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| fb941a7f-be0d-36b4-b496-2749143ee399 | -19.21149 | -42.61224 | 2026-09-28 17:05:00 | NOAA-21 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| eb0e84ea-a034-365b-81e6-c1b453c1835f | -23.58586 | -51.58127 | 2026-09-28 17:05:00 | NOAA-21 | CAMBIRA | PARANÁ | Brasil | 4103800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 0180415a-f8e8-36b6-a613-4d74193f8ef3 | -19.92478 | -45.06837 | 2026-09-28 17:05:00 | NOAA-21 | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| cb074e1e-8d71-3783-99a5-4ae6cb1f611b | -21.36156 | -43.79729 | 2026-09-28 17:05:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| dc90af21-ef7c-3671-8463-b1606f844be8 | -20.88114 | -51.45557 | 2026-09-28 17:05:00 | NOAA-21 | CASTILHO | SÃO PAULO | Brasil | 3511003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| c79f0a3f-6531-33d5-8e77-3fd86460f30e | -21.90001 | -45.46893 | 2026-09-28 17:05:00 | NOAA-21 | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| ac662d42-71a6-33f5-80eb-cac66a9b5c3a | -21.90808 | -45.3503 | 2026-09-28 17:05:00 | NOAA-21 | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 2c2a8db7-0027-3354-bb32-f495ef807497 | -23.41311 | -49.65107 | 2026-09-28 17:05:00 | NOAA-21 | CARLÓPOLIS | PARANÁ | Brasil | 4104709 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| cb8f99dc-ff58-3ea5-95be-a6ec4db9659e | -20.76416 | -51.31608 | 2026-09-28 17:05:00 | NOAA-21 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 44.3 |
| 9f4e0edd-0e3d-3509-877d-639f662463af | -22.98333 | -52.55182 | 2026-09-28 17:05:00 | NOAA-21 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f67e9d1e-1bdb-3e27-a7a8-cbec2679d9e4 | -21.38163 | -45.33784 | 2026-09-28 17:05:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 4fdcfa67-379d-301f-8805-c83073f0b099 | -18.80478 | -42.23038 | 2026-09-28 17:05:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| eca7137a-8760-3d03-816f-a917d4fea80a | -21.12378 | -46.26222 | 2026-09-28 17:05:00 | NOAA-21 | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| b4ee7a28-5c90-31bb-90ca-b90a4c6c9f7f | -20.39141 | -46.01213 | 2026-09-28 17:05:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2aa71942-05de-3809-b5b9-a9648f4af061 | -23.12145 | -52.33439 | 2026-09-28 17:05:00 | NOAA-21 | ALTO PARANÁ | PARANÁ | Brasil | 4100608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 2d5c6e84-b308-30db-8dfe-90d9e91c0166 | -21.72667 | -43.95529 | 2026-09-28 17:05:00 | NOAA-21 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.6 |
| 54040caa-3d3a-349c-a96c-02aff16fdce7 | -23.60852 | -54.75041 | 2026-09-28 17:05:00 | NOAA-21 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| ff33968e-0958-32da-aeb9-5a55f3022ede | -21.08326 | -45.01885 | 2026-09-28 17:05:00 | NOAA-21 | PERDÕES | MINAS GERAIS | Brasil | 3149903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| ab0e6c00-53f5-362a-83aa-e4f0e395d170 | -21.28405 | -45.74398 | 2026-09-28 17:05:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| cb4deeb4-83ec-3edb-91bc-0230c18d488e | -20.0581 | -45.41142 | 2026-09-28 17:05:00 | NOAA-21 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 670e3e6e-552d-3344-bf38-0e5b5a607479 | -19.03982 | -40.79969 | 2026-09-28 17:05:00 | NOAA-21 | PANCAS | ESPÍRITO SANTO | Brasil | 3204005 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d7e1cb2b-ede3-344e-8d91-aa2f70dcb190 | -21.35007 | -51.042 | 2026-09-28 17:05:00 | NOAA-21 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| ed0c8a9f-96b2-3c7c-9474-72631cf2be55 | -19.65704 | -44.72294 | 2026-09-28 17:05:00 | NOAA-21 | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 25b5b249-cd5d-31d0-bcdf-22b46afc3299 | -21.35067 | -51.04575 | 2026-09-28 17:05:00 | NOAA-21 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 49756887-bc8f-3cd7-8d5c-6e51abd53f6b | -20.43833 | -47.24701 | 2026-09-28 17:05:00 | NOAA-21 | CLARAVAL | MINAS GERAIS | Brasil | 3116407 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 66631f30-1ecd-3f1d-bd39-07434bd68266 | -20.98511 | -45.80319 | 2026-09-28 17:05:00 | NOAA-21 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c8193d04-88a7-3550-8137-f511ee2af5d3 | -21.57826 | -45.81961 | 2026-09-28 17:05:00 | NOAA-21 | PARAGUAÇU | MINAS GERAIS | Brasil | 3147204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| a807a388-bb7e-3f8c-990d-40aebd2711bd | -20.87782 | -51.45616 | 2026-09-28 17:05:00 | NOAA-21 | CASTILHO | SÃO PAULO | Brasil | 3511003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 01c684a2-ffde-3c06-8132-35ab1594d76a | -20.72469 | -46.53406 | 2026-09-28 17:05:00 | NOAA-21 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 825b4786-8a25-376c-bc17-61a9e117f519 | -20.67253 | -42.28669 | 2026-09-28 17:05:00 | NOAA-21 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 01c0017a-bc96-3282-8c86-eb6fe805530e | -20.45972 | -45.57934 | 2026-09-28 17:05:00 | NOAA-21 | CÓRREGO FUNDO | MINAS GERAIS | Brasil | 3119955 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8f2d5636-f7af-3bf0-b31e-f749eb1c6a9b | -23.58917 | -51.58068 | 2026-09-28 17:05:00 | NOAA-21 | CAMBIRA | PARANÁ | Brasil | 4103800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 02eb7c8c-2357-3e1d-b8e9-b2b3f240a681 | -21.48483 | -45.78811 | 2026-09-28 17:05:00 | NOAA-21 | FAMA | MINAS GERAIS | Brasil | 3125200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |


[Clique aqui para ver as próximas entradas](README128.md)
