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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ded86fe-1f94-3105-b53f-f4b9bd1d2d0f | -10.63689 | -49.45493 | 2025-07-08 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 78c4c37e-04b5-3a77-8ce1-8c48b1c361b3 | -19.69994 | -52.39204 | 2025-07-08 04:17:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57412539-e53b-3b3d-898d-70478da9a891 | -10.97733 | -45.11562 | 2025-07-08 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| c3441c24-3f86-3a2f-a62b-0f56e571a920 | -11.88766 | -44.93189 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27d5e648-2cfc-3e1e-a669-105da17f3876 | -22.78677 | -43.75587 | 2025-07-08 04:17:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 13ab43e8-d0e1-3b98-baac-9c68930486a0 | -15.963 | -52.2107 | 2025-07-08 04:17:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61b6d44f-6505-3114-b880-70dcab014c65 | -16.07017 | -46.12856 | 2025-07-08 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df6621ed-f54d-3adb-9fdf-15bc7802d14a | -11.81437 | -44.27238 | 2025-07-08 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d22fd42-ce51-3ee7-a695-d605c66387e4 | -12.98268 | -44.89095 | 2025-07-08 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1937188-8bbd-349d-b3d6-63d2f48130d8 | -10.23995 | -47.46057 | 2025-07-08 04:17:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2d17530-2ddc-3b30-aad8-116cabcc55a9 | -17.89028 | -39.78514 | 2025-07-08 04:17:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f5686cc9-67f4-3fee-884e-07f1967043b5 | -15.3109 | -46.90319 | 2025-07-08 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 26d19f90-89e4-3766-83dc-94c511e5b15c | -19.08918 | -56.05082 | 2025-07-08 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b32c51f1-a05a-3ffb-949a-dbe15f1fd9b7 | -10.97457 | -45.11155 | 2025-07-08 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c80e53f2-de8a-3368-98fc-9393206e74fe | -21.1917 | -48.94374 | 2025-07-08 04:17:00 | NOAA-21 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ded25c26-229d-32dc-bdbb-98362e0608b7 | -21.79367 | -52.76491 | 2025-07-08 04:17:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a3e8f7a1-7800-32fb-b625-0e5854c7d677 | -13.0126 | -46.7673 | 2025-07-08 04:17:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b918c5a9-57e5-3df0-a163-26c39f819a09 | -17.01744 | -43.99082 | 2025-07-08 04:17:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1accbb7a-ff57-3300-bdd5-7ffdda5fc562 | -13.41113 | -47.89147 | 2025-07-08 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5f57c5d-cad7-3a4e-a58e-dbae0c1dff28 | -13.36627 | -47.79405 | 2025-07-08 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 344ff04d-5f07-36e8-9178-ca64f25d8dd5 | -11.96884 | -49.57257 | 2025-07-08 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf5f2c52-1abe-32c8-9407-0742b4c19b20 | -20.58182 | -47.49302 | 2025-07-08 04:17:00 | NOAA-21 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dae65044-2298-3214-a9ea-41bf55e33c4b | -13.28884 | -49.15889 | 2025-07-08 04:17:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b64f42a5-d2a4-3ac6-8182-373e572d981f | -17.65262 | -46.829 | 2025-07-08 04:17:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3feb3dd4-b5c4-3989-b16d-9581a41e84b4 | -15.99808 | -41.42535 | 2025-07-08 04:17:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9f29d080-00a1-31f5-b46d-3507b8c91624 | -21.30654 | -49.45459 | 2025-07-08 04:17:00 | NOAA-21 | SALES | SÃO PAULO | Brasil | 3544806 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9633c84b-8cb7-3e6f-9a42-a0bb642e5227 | -11.42367 | -45.11201 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 0ab16cb4-2b8d-34df-95fd-e77991a37f48 | -13.40967 | -47.87852 | 2025-07-08 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 09f7c2f2-0cb3-3701-8783-3c383eddeb81 | -20.99788 | -51.79493 | 2025-07-08 04:17:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5313d05c-ddc6-327d-b7f3-c368f545ec00 | -13.89659 | -42.1335 | 2025-07-08 04:17:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 06c1a28d-08cb-3abe-8c4c-49bff4b1452e | -15.75792 | -48.28495 | 2025-07-08 04:17:00 | NOAA-21 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 96e16ff5-8afe-3e57-8f9b-9cef4d860c85 | -21.07796 | -45.44202 | 2025-07-08 04:17:00 | NOAA-21 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4fd65d5-474e-3396-b913-74949c502c5e | -11.3258 | -55.21791 | 2025-07-08 04:17:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ac2376ed-04a0-3fe0-b988-9b07df29e842 | -11.43305 | -45.11716 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e08739c7-3bd2-31da-bd65-0e9d734e2bc7 | -13.90073 | -42.1299 | 2025-07-08 04:17:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 39feca4a-1cc2-3f72-90bd-2fc4bcbd0ba4 | -14.19125 | -45.5113 | 2025-07-08 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81abcc4a-8204-3783-a98c-ea0952e8a3fc | -11.42147 | -45.1044 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5d321fb2-343a-3dfb-80e5-028a675ec8b5 | -15.07966 | -48.94548 | 2025-07-08 04:17:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a4448c17-c2eb-31aa-9837-774a9351b892 | -11.89153 | -44.92891 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c27ca782-31f1-3267-95b5-7a53a817d0d6 | -13.89422 | -42.12476 | 2025-07-08 04:17:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 630e0ef9-7257-317a-be52-ba61ea8e59b7 | -14.04925 | -46.25041 | 2025-07-08 04:17:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9da1b28a-394f-3f23-9d58-0ccbbbebfb46 | -11.43585 | -45.09949 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c4375fb7-40c0-357f-9569-fcbbb20aa7b5 | -11.47006 | -47.92064 | 2025-07-08 04:17:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2eb0a209-8f1e-3c86-96fc-789213a85e96 | -20.91956 | -43.93031 | 2025-07-08 04:17:00 | NOAA-21 | CASA GRANDE | MINAS GERAIS | Brasil | 3114907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ed8d45bc-4714-3bc7-ad20-080bc96790c3 | -11.88932 | -44.92137 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da68dc09-1956-3544-b5fd-f2238f327e49 | -19.08386 | -56.04958 | 2025-07-08 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e5b2fe03-77da-39c9-922b-a8f476b173f7 | -10.95457 | -48.15577 | 2025-07-08 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db544af9-9b74-3161-bb75-33993aa7d5a1 | -10.63753 | -49.45131 | 2025-07-08 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 21b09292-d6ba-38bf-977d-c2572223d1d9 | -20.92307 | -43.93084 | 2025-07-08 04:17:00 | NOAA-21 | CASA GRANDE | MINAS GERAIS | Brasil | 3114907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 783fb9c3-88fc-3903-868b-3dd53e18e01d | -13.90722 | -42.13507 | 2025-07-08 04:17:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5f217d6b-53b7-3109-98ae-9f92322528b5 | -23.75784 | -45.72912 | 2025-07-08 04:17:00 | NOAA-21 | SÃO SEBASTIÃO | SÃO PAULO | Brasil | 3550704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a39e4bab-97fb-303e-910c-222c4daf3719 | -10.36111 | -48.72198 | 2025-07-08 04:17:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0a144932-f429-3455-87c0-d6183450ddc1 | -10.824 | -54.01812 | 2025-07-08 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7e0f9126-49ab-3466-a63d-c781710e5e4c | -14.15835 | -42.57449 | 2025-07-08 04:17:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fe8374c3-001b-31e7-a25b-216619f99e14 | -10.98065 | -45.11615 | 2025-07-08 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 482e345c-8448-34f7-97f8-0b09468ed1f9 | -11.31038 | -42.1348 | 2025-07-08 04:17:00 | NOAA-21 | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 14ee1372-4b03-3451-9e8a-a406a2a79104 | -10.95164 | -49.25402 | 2025-07-08 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f33e9d1e-12e4-309b-b220-256be6998d92 | -15.2594 | -51.53397 | 2025-07-08 04:17:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 312938cf-066c-36f2-854d-0ab1ef9ad35d | -13.00917 | -46.76682 | 2025-07-08 04:17:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19ac70b2-c769-30b9-8167-db1fa3b4e41c | -21.04034 | -55.99509 | 2025-07-08 04:17:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c617c739-53bd-36fd-bce2-16e79cd1907f | -14.1885 | -45.5072 | 2025-07-08 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a8d16e1-711a-3a11-9698-03b7b7361349 | -10.96321 | -48.2031 | 2025-07-08 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0515ac2-71be-3da3-8008-cbf40587767f | -13.40898 | -47.88254 | 2025-07-08 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b7b7604-9952-3ce7-9a04-2e1d44b149be | -21.30223 | -48.56099 | 2025-07-08 04:17:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 247c03d0-0fb4-391d-a543-bfcb7b69bbd8 | -11.42922 | -45.09842 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 682e28ee-2106-37b9-bd83-3f83468d43c4 | -20.77651 | -49.61673 | 2025-07-08 04:17:00 | NOAA-21 | NEVES PAULISTA | SÃO PAULO | Brasil | 3532504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9a97e041-3f87-366d-a51c-3936d130382b | -17.88976 | -39.78934 | 2025-07-08 04:17:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2a4f1218-733f-3114-b3c9-121c54fbcfa8 | -11.43969 | -45.11824 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 66b905ce-5b18-3c5e-bc0f-a5493a8084d2 | -18.0409 | -39.92642 | 2025-07-08 04:17:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 34d53ff8-e8c6-34c8-8f28-596f49858857 | -11.43142 | -45.10602 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| b98adfee-68b2-3484-b770-bd4066f2a636 | -11.44025 | -45.1147 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 1a21f6b9-ad54-3506-a46a-bd025affa58a | -10.6418 | -49.47461 | 2025-07-08 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| cd25eae4-27db-34c5-963b-dda88083f263 | -11.20124 | -48.99672 | 2025-07-08 04:17:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 404576fd-89c8-3fd6-88c7-72f12a14574c | -10.64031 | -49.45927 | 2025-07-08 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c443ffbf-d74b-3a73-87b3-10bc221b3327 | -12.33095 | -49.322 | 2025-07-08 04:17:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 77a2331a-c42e-351a-b346-a77294d697f9 | -11.42203 | -45.10087 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 831f69cb-573a-3d11-8a11-54ab20f12153 | -14.26824 | -53.23179 | 2025-07-08 04:17:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 638cd4dd-fb4e-3027-8d81-338e78803be4 | -22.85876 | -42.98027 | 2025-07-08 04:17:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ca48fb14-d4c0-3385-a14e-5bf82d690321 | -11.00252 | -42.7849 | 2025-07-08 04:17:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8daecefb-2c33-350f-b294-0964f3aa16fc | -13.02036 | -46.29277 | 2025-07-08 04:17:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 098c9ab8-0945-34d2-8999-3f5b9170bf17 | -10.82539 | -54.01082 | 2025-07-08 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 32994fa1-d0b5-3847-840d-5800eb8466d2 | -10.97401 | -45.11509 | 2025-07-08 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 8149484c-f2ef-352f-8be1-e784bc2accf0 | -12.98819 | -44.8774 | 2025-07-08 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76bd50fd-2e0e-3d96-bc41-4ec1f18fdca4 | -12.76479 | -44.41506 | 2025-07-08 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 49c1604a-5593-315c-9acc-cb9a36ea7c1a | -10.63044 | -46.37567 | 2025-07-08 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 583a46df-d3da-329d-9729-7ba2a98619f4 | -14.84051 | -48.23244 | 2025-07-08 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4bcedb1-dcb9-3f98-b0d1-99e76d386d87 | -21.30562 | -48.56165 | 2025-07-08 04:17:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3274f7eb-2a2e-3d9e-a29b-84acada0667f | -10.41907 | -49.7708 | 2025-07-08 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 26e5febd-bc7a-3ea6-a17b-f69b3ae9a172 | -12.94438 | -46.53886 | 2025-07-08 04:17:00 | NOAA-21 | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 731742ba-2b8a-3c75-9ff1-2fe7c16cc3d2 | -10.22864 | -56.77082 | 2025-07-08 04:17:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e1ffa4d7-8d65-3e5a-9080-a4a11a662d87 | -20.37539 | -45.13712 | 2025-07-08 04:17:00 | NOAA-21 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 36154d01-136b-3501-948f-a3f2a27590fc | -13.65116 | -46.81666 | 2025-07-08 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7a32d678-6434-3984-91c8-0e340688dc72 | -10.63451 | -46.3724 | 2025-07-08 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 30fb855c-b080-3d96-9695-3346e0725f07 | -17.77675 | -42.80858 | 2025-07-08 04:17:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1174549-bfd6-3800-9429-da87d4723762 | -12.289 | -50.11002 | 2025-07-08 04:17:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbf1d607-9ac7-3516-aafb-e4455d3afb9c | -13.3705 | -47.79064 | 2025-07-08 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1dde1246-7bc7-3727-ab52-ccd36b5393b8 | -11.42535 | -45.10141 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| cb3ea6ca-8cef-3971-be9f-f748596c7405 | -14.27104 | -53.23057 | 2025-07-08 04:17:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 06d997a9-d3b8-3e3a-ac9e-2a1bbc6fb78e | -11.89266 | -44.87868 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b56db94c-804d-3ef1-91db-f841394a3147 | -13.89777 | -42.12527 | 2025-07-08 04:17:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README10.md)
