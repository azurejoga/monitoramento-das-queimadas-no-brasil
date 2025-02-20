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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96a3e869-6ac5-3ee1-bdc0-67386f216530 | -22.89315 | -42.43568 | 2025-02-20 04:06:00 | NOAA-21 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 1c716790-334d-311d-98fe-25ba88041525 | -20.85851 | -54.08558 | 2025-02-20 04:06:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8bc66496-2fc5-33b8-9a9a-12b0ec49a5dd | -20.86182 | -54.08564 | 2025-02-20 04:06:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9d8d50f6-ca16-3ec7-85d8-d36f37f66fc7 | -22.67706 | -42.85685 | 2025-02-20 04:06:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f8c5aee9-ec17-3ee9-a093-a0ea99744f6c | -21.3886 | -49.03143 | 2025-02-20 04:06:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e16c7a4a-c3a9-3584-be07-7d67b0b627fd | -22.85904 | -42.86465 | 2025-02-20 04:06:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0112c052-586e-3150-9133-c76225290230 | -22.85533 | -42.98043 | 2025-02-20 04:06:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e4b626ed-d6df-3a64-9011-a8c437e660a6 | -21.20035 | -48.76244 | 2025-02-20 04:06:00 | NOAA-21 | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b0e3b2eb-b567-32f8-a49d-ffab029e6346 | -22.92183 | -45.4146 | 2025-02-20 04:06:00 | NOAA-21 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 048f3c8d-1d80-37cf-b64f-07455f3b73cb | -21.19512 | -44.9394 | 2025-02-20 04:06:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c6d8ac4c-91bd-323f-8e3a-1c752941975e | -22.9172 | -43.19943 | 2025-02-20 04:06:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b1cc7258-ce99-310b-a4b3-b873b50aca98 | -21.62501 | -43.46751 | 2025-02-20 04:06:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2a5b2167-a66e-3071-83db-f12b745d58c6 | -22.67763 | -42.85307 | 2025-02-20 04:06:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3e9f5d58-9994-36ad-9cee-dc79480a38c3 | -21.91376 | -42.26326 | 2025-02-20 04:06:00 | NOAA-21 | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b659032c-48bc-3cc8-9ef2-01123c6fe877 | -20.73241 | -54.6008 | 2025-02-20 04:06:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 362524c3-bb06-38a2-a8fd-a862c0856796 | -21.62832 | -43.4681 | 2025-02-20 04:06:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 618ceef3-18a8-31cb-9e4f-48ab1debb399 | -20.73815 | -54.60233 | 2025-02-20 04:06:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2275a3e-1f4a-30f2-8d54-0617762cefbc | -30.23183 | -54.49025 | 2025-02-20 04:08:00 | NOAA-21 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| d800f7fa-c17b-37c5-8a70-3c69b2c625e3 | -29.89095 | -51.23429 | 2025-02-20 04:08:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| d87c062c-d0c3-33e2-bda3-6299807df386 | -14.41683 | -45.63957 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79219519-f302-365a-97d2-5c21140b26ca | -10.75573 | -37.04882 | 2025-02-20 04:27:00 | NPP-375D | SANTO AMARO DAS BROTAS | SERGIPE | Brasil | 2806602 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1180fb62-1a84-3f35-b5c2-3134aa36bed4 | -14.4256 | -45.65327 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08ce5c36-6d0c-3ac6-8d90-c7ae73eaf7cb | -14.44407 | -45.67551 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c0427ef0-3259-35f5-a0d5-27aa1567e1c8 | -12.80037 | -45.01734 | 2025-02-20 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82f6673d-f71e-38b1-89ec-4fc30571acd0 | -11.57424 | -47.6342 | 2025-02-20 04:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ddb5535-0288-38b7-a266-4c31c96008d2 | -14.42268 | -45.64871 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99fecbd2-3712-3097-99a0-bb056357f3cd | -14.42501 | -45.6573 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95900ff1-87d3-311a-8753-39c2d77fb382 | -10.75622 | -37.04495 | 2025-02-20 04:27:00 | NPP-375D | SANTO AMARO DAS BROTAS | SERGIPE | Brasil | 2806602 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f3cdc335-d0a7-3ace-ab6f-c3b4f269a0c0 | -14.47336 | -45.81892 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbfe93ed-766f-38ea-951a-6feaf591390e | -14.41742 | -45.63555 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8cdbb855-c59f-3fee-8c2e-e2a2bc478af3 | -14.41975 | -45.64415 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b87b227-2bee-398e-b110-fac5d0f1864c | -10.53948 | -45.21822 | 2025-02-20 04:27:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 676978b4-6c3f-3a68-ae62-76258a547e39 | -11.10897 | -45.11681 | 2025-02-20 04:27:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f273f150-2274-3a16-ab49-69b22275359e | -11.57921 | -47.62423 | 2025-02-20 04:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77f0ff04-e21c-36e2-a696-6f8f84681ec4 | -10.54293 | -45.21877 | 2025-02-20 04:27:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1b6764b0-f2ff-36fe-a8c1-9cd5c91b2fe5 | -14.44523 | -45.66747 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da07278f-effe-32a3-83c9-fb35a73a9282 | -14.45284 | -45.66454 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69b299d8-2c13-3da0-aca6-855421cc6290 | -14.42972 | -45.6498 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c7aaf08-3289-3d5f-8538-115d5585e7b7 | -14.43675 | -45.65088 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 607ddcb0-58a7-3e8f-89f6-6f2b125c9b2e | -12.79567 | -44.9999 | 2025-02-20 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc9a3c0a-0313-3640-939a-032486ef6510 | -9.16055 | -43.12119 | 2025-02-20 04:27:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 75f3721f-fc31-324d-b379-255a0cb10037 | -12.79863 | -45.00454 | 2025-02-20 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e88791f-15f9-31db-9af6-b34661d9608f | -11.86221 | -46.94205 | 2025-02-20 04:27:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3bdf4beb-bcb6-3c01-9110-ea2a302265a3 | -14.43437 | -45.66696 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db75f795-6f72-30f5-b62b-355fd9a6b6d5 | -14.47395 | -45.81494 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| adad24a0-a3b3-302b-b324-7d9df2e24b7b | -12.80097 | -45.01325 | 2025-02-20 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1d48efd-133f-3a82-88bc-7fe688b55209 | -14.42208 | -45.65274 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d95a7473-4b48-3b23-a810-e6572072b612 | -11.85777 | -46.94861 | 2025-02-20 04:27:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 929ece9e-471f-3653-bc03-9f28197727aa | -11.8611 | -46.94916 | 2025-02-20 04:27:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 876252d0-9099-3544-afa7-630a6baf3db1 | -11.58033 | -47.6388 | 2025-02-20 04:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0957cb1e-fed9-381b-9c45-1cbbff22ee48 | -10.54005 | -45.2144 | 2025-02-20 04:27:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75f999b1-b1b8-3919-a886-ef91301152e5 | -14.44113 | -45.67095 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d18549c-7234-3e37-8fee-d2072c0b2b79 | -14.44432 | -45.6726 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 64fb7280-f0d3-34d3-970b-a58c8f73d4a6 | -9.87146 | -48.14442 | 2025-02-20 04:27:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fc34c283-c8c2-3aab-b873-90a645555165 | -11.69323 | -47.80136 | 2025-02-20 04:27:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b6e0bcd-38c8-3870-bcc5-3bfd5e40788e | -14.42852 | -45.65784 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3e93491-991c-3cc2-9afc-6067c4b4c563 | -12.79385 | -45.01219 | 2025-02-20 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5de63334-bc84-3431-b73d-34dc4854072d | -8.12587 | -43.13515 | 2025-02-20 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 66904238-74de-3fad-be70-7a66482f6d43 | -14.42912 | -45.65381 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48c3be86-022d-3344-b230-5f03f3c0e939 | -14.44465 | -45.67149 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5df52fea-e923-31e9-bded-ee6e33e105b7 | -14.4414 | -45.66804 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c450a734-eb7a-35a0-b0c4-5e125cb23544 | -14.43788 | -45.6675 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c36bf47c-df6f-3e4c-a0c4-dbd76437a0d2 | -14.42327 | -45.64468 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5941ca5f-708a-39fd-a207-005b1072150f | -14.40627 | -45.63796 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ebf75316-0ea2-3546-82ed-c2d7ddd10e4e | -14.40979 | -45.6385 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f1f6b52-d683-3404-8edc-b032ea09dd86 | -12.79802 | -45.00863 | 2025-02-20 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf550b56-abec-3f53-a04d-cf22676443b5 | -8.12519 | -43.13961 | 2025-02-20 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| db22bcce-2523-3c0f-a9f4-dd241c91890d | -12.79681 | -45.01681 | 2025-02-20 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0436c42-276c-3c84-88c0-550e64e3d9b7 | -12.80332 | -45.02195 | 2025-02-20 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3bd55a32-d929-30d6-9704-3c082bdf5e3b | -12.7909 | -45.00755 | 2025-02-20 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf80bab4-4f8c-3de7-9f24-5f65da1d0bb8 | -8.40114 | -45.09181 | 2025-02-20 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a97f98c0-f143-3b06-8e84-a9738e51e577 | -8.12891 | -43.14015 | 2025-02-20 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a0855fcb-b3d5-34b5-857d-9e52f87b4ee8 | -12.79506 | -45.004 | 2025-02-20 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4626a2d5-cb74-3eb7-9ae3-ccaf84d76324 | -10.7546 | -44.9337 | 2025-02-20 04:27:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 86d262cf-c8e9-3cb5-9187-4cfa5ea2be1e | -11.57092 | -47.63366 | 2025-02-20 04:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a4b59f3-4c5f-3b28-98d6-f50748c5b900 | -14.45226 | -45.66856 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf5036f0-a254-3aaf-9338-1a57790c153a | -14.41038 | -45.63447 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4339de89-24cd-36c9-91c3-14e66f60f92d | -14.41331 | -45.63904 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca5db12a-92bf-3f87-97f9-708678e27a29 | -14.45578 | -45.66911 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80aa4dd3-e0d1-3ae6-8a48-0f721e5bdb22 | -12.79741 | -45.01272 | 2025-02-20 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd82e29f-4a24-3b9c-9f31-c8bcb88c696b | -11.57868 | -47.62771 | 2025-02-20 04:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50c37b96-7536-38e7-abd0-7710d5136f3f | -11.92017 | -43.12136 | 2025-02-20 04:27:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ff01fbde-eb0f-3a4f-ac05-b96c69c2ff08 | -14.4139 | -45.63501 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 909c43e6-8623-310c-a274-ae98dab81c4f | -14.41916 | -45.64817 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52010ec3-b450-3584-b902-54e3fb4bdcde | -14.44874 | -45.66802 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52946b6f-2ca1-3313-8f10-201eb1fd9d16 | -11.85832 | -46.94506 | 2025-02-20 04:27:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 30b89550-30a3-307a-bc4f-52b50e146128 | -14.4262 | -45.64925 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d3ccf87-356b-3de3-ba97-986f7b9c117c | -14.43145 | -45.6624 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b6feea0-1559-3f28-a9e9-579cdee43961 | -8.12725 | -43.13788 | 2025-02-20 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 65f325e3-d44a-3bba-bf73-ceb0274c0a65 | -14.4408 | -45.67206 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a2134bd7-5447-376c-840b-9c5df68ae5b7 | -14.44491 | -45.66858 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e7018a27-2561-3197-a435-4ead92619508 | -11.10839 | -45.12071 | 2025-02-20 04:27:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e7bec09-8128-306c-8590-0e1119f46c90 | -14.42679 | -45.64523 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e4844dd-465d-370d-a4b9-6e083d59f60b | -12.79446 | -45.00809 | 2025-02-20 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01f2f391-478e-343c-96f0-b87d2b3b347c | -10.43373 | -44.8874 | 2025-02-20 04:27:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e90c5e1e-bd73-3d27-9e3b-bd1c775b3f05 | -14.43324 | -45.65034 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50f7ff38-e687-34fc-9120-e30a23447332 | -11.86165 | -46.9456 | 2025-02-20 04:27:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb6f49e7-39b8-3490-aebe-40aac8a90dee | -10.54639 | -45.21931 | 2025-02-20 04:27:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 305e57b2-22b7-32dc-b9d2-bedd23e8ff55 | -11.03103 | -45.0577 | 2025-02-20 04:27:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6cd1385-92f1-3960-b284-477e178ef367 | -14.44932 | -45.66399 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README5.md)
