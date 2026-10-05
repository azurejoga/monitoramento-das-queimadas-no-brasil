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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b700146-5880-3504-9cf5-0b5a83b980d8 | -16.03726 | -44.4551 | 2026-10-05 16:35:00 | NOAA-21 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d957ec75-2f48-3a60-8eef-92f0dddb8468 | -14.13074 | -41.19888 | 2026-10-05 16:35:00 | NOAA-21 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 2a989bb2-afb3-3e22-bb48-791272253570 | -15.27077 | -42.18367 | 2026-10-05 16:35:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| 0790c4f3-133c-308d-928a-72d0bb4fb633 | -14.21317 | -40.22604 | 2026-10-05 16:35:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| d67045c5-6caa-36cd-9ec9-46453d66cd9c | -16.34771 | -42.0437 | 2026-10-05 16:35:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 08b9e9cc-7a62-38c3-9dd4-1dafecd0c982 | -21.63683 | -41.24258 | 2026-10-05 16:35:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 273931a3-e97a-3fd0-a192-248c2e889d5c | -17.13138 | -40.06298 | 2026-10-05 16:35:00 | NOAA-21 | VEREDA | BAHIA | Brasil | 2933257 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 8fc1f7e7-d620-3e8f-94b7-0b989459b2f6 | -16.99067 | -44.85991 | 2026-10-05 16:35:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 558c121a-46f2-30db-8b71-63e001f85dc3 | -16.02342 | -45.13301 | 2026-10-05 16:35:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f5d65bbd-cd80-33d1-b0ff-bb145cef713b | -14.22163 | -40.77217 | 2026-10-05 16:35:00 | NOAA-21 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7c0193af-f59d-3a55-82fc-ae4fbba1f768 | -15.68752 | -41.32583 | 2026-10-05 16:35:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| 48c0a30f-9b69-3209-82c8-cfa4a7e56d91 | -16.5853 | -41.53697 | 2026-10-05 16:35:00 | NOAA-21 | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 6125dad6-6d53-30f3-b8fd-24ae5f81eafc | -14.81346 | -41.0201 | 2026-10-05 16:35:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 1d3d34d8-c43c-3f64-b4cb-e7b16937d0a1 | -14.28054 | -43.76235 | 2026-10-05 16:35:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f72b2b7c-0f16-37e1-bb80-fa9e058ebfdd | -15.69254 | -39.77892 | 2026-10-05 16:35:00 | NOAA-21 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 2d58acda-f36c-307e-9a69-125e0a3e1b21 | -15.79546 | -40.79772 | 2026-10-05 16:35:00 | NOAA-21 | DIVISÓPOLIS | MINAS GERAIS | Brasil | 3122454 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| bb6a37e7-8b0c-3d4f-8791-23c846293ef6 | -14.54136 | -40.84827 | 2026-10-05 16:35:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 3ce1fe3a-14c8-3567-b8fa-4cab8a3ede33 | -15.68982 | -39.78754 | 2026-10-05 16:35:00 | NOAA-21 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 7d8f086a-3d61-3155-8fc1-e52dce07a47a | -15.96913 | -44.73734 | 2026-10-05 16:35:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 2f18816c-ee5b-39b5-85af-570e2dea41a6 | -13.93189 | -40.21758 | 2026-10-05 16:35:00 | NOAA-21 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| d7bb854d-6ab1-3750-b907-470c0857b9ba | -15.58138 | -41.50446 | 2026-10-05 16:35:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 89fc07dd-fdc2-34e7-9624-764897c9ea17 | -14.43545 | -39.5963 | 2026-10-05 16:35:00 | NOAA-21 | ITAPITANGA | BAHIA | Brasil | 2916609 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| e791e29e-b028-3c97-9561-444d1f8af6b7 | -16.63418 | -44.50977 | 2026-10-05 16:35:00 | NOAA-21 | SÃO JOÃO DO PACUÍ | MINAS GERAIS | Brasil | 3162658 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 614e9fed-9ac2-3067-b344-5c9edbf2495d | -16.58675 | -41.53988 | 2026-10-05 16:35:00 | NOAA-21 | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 4f94bfbb-84ad-3fc5-8708-b683fbc1bdc9 | -15.8933 | -42.5256 | 2026-10-05 16:35:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ae73b882-93fb-3f67-9d38-dd199a28106f | -16.13527 | -40.70543 | 2026-10-05 16:35:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| e2086662-1d48-32f1-8ee5-b5b2dda0b3d7 | -15.68911 | -39.78363 | 2026-10-05 16:35:00 | NOAA-21 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 491d0dd4-d374-3b6c-904c-d348e8bb1aba | -16.39994 | -39.42385 | 2026-10-05 16:35:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 21.3 |
| fab459e0-338d-3542-bfd8-f7d81a4f282c | -15.68842 | -39.77974 | 2026-10-05 16:35:00 | NOAA-21 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 774ee4bd-7c9b-3984-a925-ac684b3cd231 | -14.55597 | -41.284 | 2026-10-05 16:35:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 0f73b872-4a93-3871-9983-ee776f8133d7 | -14.215 | -40.44793 | 2026-10-05 16:35:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e5be42a9-8285-3250-8644-f81dd6c32d1d | -16.13141 | -40.70622 | 2026-10-05 16:35:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 669b728e-952b-34f1-bb98-cf3fb4297c7f | -14.67189 | -41.32534 | 2026-10-05 16:35:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 1ca9832f-82e2-3822-bc5d-e937becd15b2 | -14.69423 | -41.90749 | 2026-10-05 16:35:00 | NOAA-21 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 8e561b4f-15f8-3f69-ada5-3462d6032483 | -16.43015 | -39.52007 | 2026-10-05 16:35:00 | NOAA-21 | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| a2272b44-a8f1-3f4f-bffe-d3e888cd822e | -15.91284 | -40.98543 | 2026-10-05 16:35:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 4a032269-edc2-3cb8-9e43-752865502fa8 | -16.99123 | -44.8635 | 2026-10-05 16:35:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e703fd36-bf91-37ac-b024-7d9768458901 | -15.36061 | -40.98746 | 2026-10-05 16:35:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 84742ed2-f79c-39d2-9093-ed5db33289e6 | -15.88604 | -40.71484 | 2026-10-05 16:35:00 | NOAA-21 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 3d2fbabe-b2b4-37c8-9990-ca1899a59162 | -15.59082 | -40.31633 | 2026-10-05 16:35:00 | NOAA-21 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| ca0b7aea-d038-35ea-b687-5fd9bcd15ed5 | -13.68131 | -40.84402 | 2026-10-05 16:35:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d8e297d1-2aa0-3530-b264-cf4c79088a7e | -14.89413 | -40.97232 | 2026-10-05 16:35:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 277a9997-5fec-3a6f-959e-8f5c442df7da | -21.63471 | -41.22998 | 2026-10-05 16:35:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 489dc52d-98da-3b48-b60a-27d3173034f6 | -15.88015 | -42.25135 | 2026-10-05 16:35:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| a25fa38c-763a-33a5-89ff-d3ff2b366d65 | -14.07163 | -40.60904 | 2026-10-05 16:35:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 1a25252e-3a1d-3c30-bf1a-ebab052a0b65 | -13.61887 | -39.39727 | 2026-10-05 16:35:00 | NOAA-21 | TEOLÂNDIA | BAHIA | Brasil | 2931608 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| fbfecb06-d36f-3334-981b-af5c553628cc | -14.75588 | -40.92038 | 2026-10-05 16:35:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 150c3161-8809-3c38-9e3f-ba69c068005d | -17.13534 | -40.0622 | 2026-10-05 16:35:00 | NOAA-21 | VEREDA | BAHIA | Brasil | 2933257 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 767f1939-11aa-3ec6-bfc1-417c81461963 | -17.68502 | -42.18185 | 2026-10-05 16:35:00 | NOAA-21 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| dabd621a-e7da-37ab-97e1-cbd5b86de594 | -14.61553 | -41.38621 | 2026-10-05 16:35:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 740a633a-056b-31b4-a93d-8325a68b6d2c | -15.3975 | -43.00034 | 2026-10-05 16:35:00 | NOAA-21 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Caatinga | 4.9 |
| e5d7bfb0-cbb9-34e8-9cab-d58b1f55e377 | -15.69324 | -39.78282 | 2026-10-05 16:35:00 | NOAA-21 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 8f71e7ec-9864-3813-b192-b8bda9a61edb | -14.6916 | -41.90555 | 2026-10-05 16:35:00 | NOAA-21 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 17.9 |
| 812b7da9-e0da-3062-b3ee-5c07fcc06a3c | -16.58307 | -41.54049 | 2026-10-05 16:35:00 | NOAA-21 | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 864bfb36-e3dd-3bdc-b899-d493d9860b53 | -14.63379 | -41.53603 | 2026-10-05 16:35:00 | NOAA-21 | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| d94e86d4-8b12-3cfe-b835-d0ca1831bf0f | -21.63613 | -41.23839 | 2026-10-05 16:35:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| bb96bef9-ec25-3a86-928f-78bb93fe8ce6 | -16.16132 | -41.23071 | 2026-10-05 16:35:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.6 |
| 7ac25f3c-cbed-3772-8917-cdbac2db367e | -15.49687 | -44.41269 | 2026-10-05 16:35:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ea12d3ae-dca6-3874-9875-946a973e3f96 | -14.55519 | -41.50875 | 2026-10-05 16:35:00 | NOAA-21 | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 13.5 |
| b9584f41-cfcb-3751-a03b-c96730e2c2aa | -14.21721 | -41.30666 | 2026-10-05 16:35:00 | NOAA-21 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| b08385d2-2c48-3a61-a099-7048ed691141 | -17.24709 | -39.42815 | 2026-10-05 16:35:00 | NOAA-21 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| cd7dadd7-726a-3b2b-a8b8-0885066a7db1 | -16.55067 | -56.24366 | 2026-10-05 16:35:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 78dfacb5-0b68-3710-9629-275bba4bf0b3 | -15.59147 | -40.32011 | 2026-10-05 16:35:00 | NOAA-21 | MAIQUINIQUE | BAHIA | Brasil | 2920007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 45784084-dda2-3ad0-b422-48aad091290e | -15.79244 | -40.31791 | 2026-10-05 16:35:00 | NOAA-21 | MAIQUINIQUE | BAHIA | Brasil | 2920007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| dbcad61d-42df-32b7-baf3-b8a99a7f8818 | -14.6272 | -43.66856 | 2026-10-05 16:35:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 4b03f977-c232-373f-9739-99fe70d54278 | -15.33498 | -42.77231 | 2026-10-05 16:35:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 02f40eee-ba28-39a0-9912-8a84fde75ad8 | -14.83368 | -41.72753 | 2026-10-05 16:35:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 8326b7dd-ad01-3587-a8ae-fabaa25d3a9b | -14.92844 | -41.43905 | 2026-10-05 16:35:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 2042a242-02d0-39bc-bec7-a749cb46930f | -14.21156 | -41.59338 | 2026-10-05 16:35:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 32aa2aba-8b2b-3bf6-ae13-e560dc6f8d68 | -16.26864 | -41.79348 | 2026-10-05 16:35:00 | NOAA-21 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 36413a0b-957e-3568-8e0d-8e76dd2cf059 | -16.03668 | -45.0868 | 2026-10-05 16:35:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| af035bc9-8408-3a66-ab2b-d6b57fd2ad0c | -15.58556 | -42.86204 | 2026-10-05 16:35:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 5d6f5f47-e137-38aa-b6bb-62c5675280c7 | -16.48708 | -42.14746 | 2026-10-05 16:35:00 | NOAA-21 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 1bba7003-4492-3817-9d35-d38a2402c218 | -17.42894 | -41.12995 | 2026-10-05 16:35:00 | NOAA-21 | PAVÃO | MINAS GERAIS | Brasil | 3148509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.0 |
| f5481b59-ab91-339e-ae47-b5a9a3d73b91 | -16.54897 | -56.24325 | 2026-10-05 16:35:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| cddcb1bb-c815-3c1a-94e6-4562ab17e63b | -14.04996 | -41.26836 | 2026-10-05 16:35:00 | NOAA-21 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 89675100-1cc9-399f-885b-031bf948b19c | -17.43264 | -41.12922 | 2026-10-05 16:35:00 | NOAA-21 | PAVÃO | MINAS GERAIS | Brasil | 3148509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.0 |
| 6d411986-a57b-383b-a8ce-dfbc04b9c640 | -14.12686 | -41.1996 | 2026-10-05 16:35:00 | NOAA-21 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 9bd6d257-c290-3fc2-a1df-f77a2e901628 | -14.39277 | -43.49849 | 2026-10-05 16:35:00 | NOAA-21 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b97b24e0-1aa0-3695-8b40-35f8bdfa0da6 | -15.97245 | -44.73679 | 2026-10-05 16:35:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b3150248-3969-3e2c-a0af-c28f5e833ffc | -17.32157 | -41.44318 | 2026-10-05 16:35:00 | NOAA-21 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| aba3cf69-2b2f-378b-b78f-24d3868c6bc1 | -15.14683 | -42.16004 | 2026-10-05 16:35:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 50.4 |
| e3793e6b-0674-3e85-8509-c0a42cc12dbe | -12.55138 | -43.08501 | 2026-10-05 16:37:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e0ead5ac-726f-36c3-923f-de89f8e3aee2 | -10.39836 | -47.53875 | 2026-10-05 16:37:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 08465c6e-c479-3f42-8fea-f1e3a638c616 | -7.4384 | -40.13809 | 2026-10-05 16:37:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 8b7d8943-58da-3341-9aa7-f1ad87289ad4 | -11.29478 | -42.04814 | 2026-10-05 16:37:00 | NOAA-21 | PRESIDENTE DUTRA | BAHIA | Brasil | 2925600 | 29 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 2471ccc4-b9e4-36c6-8577-7decf802162d | -6.70814 | -45.24117 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 206.8 |
| 7c466e26-b805-3c6c-9388-173dbc5c0912 | -8.66163 | -54.57549 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| af3fb701-9cb2-3678-ab36-45cefae2a1de | -6.34686 | -42.5428 | 2026-10-05 16:37:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| d3b8c282-d316-39a2-9de4-2ed823c16fa0 | -9.82123 | -44.79657 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c162c726-c24e-3619-b1db-c1554e4e2748 | -11.37947 | -47.72285 | 2026-10-05 16:37:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f4cb38c9-392d-3ef9-b27b-47506a11443b | -11.82456 | -43.5454 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| bc73fe09-b3a6-364a-90a1-c690467d8b92 | -13.00626 | -39.72547 | 2026-10-05 16:37:00 | NOAA-21 | AMARGOSA | BAHIA | Brasil | 2901007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| efb4e276-428a-3db8-a11e-0b4d0ed7910b | -11.74448 | -43.43234 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 056697d2-d8d9-3d89-a46c-e2b4f8f6328f | -8.66162 | -54.53889 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| b9977ffe-2d2e-3e38-8dea-1ac65e784c98 | -7.57514 | -46.20719 | 2026-10-05 16:37:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 00382a09-db01-3d8d-ac63-0d13fc57e334 | -9.1543 | -45.13006 | 2026-10-05 16:37:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| cd5fb101-4b82-3930-8ee6-0ca765d9ec86 | -6.88089 | -43.67665 | 2026-10-05 16:37:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 43.0 |
| e16ab931-985b-380f-ad32-459485f7c99e | -9.15489 | -45.13378 | 2026-10-05 16:37:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| b932deeb-e2b5-37fd-88b9-6ec355edc80e | -11.64428 | -43.61943 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |


[Clique aqui para ver as próximas entradas](README80.md)
