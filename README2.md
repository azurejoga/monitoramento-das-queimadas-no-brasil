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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9988a0f5-035a-3782-bcd8-4ad15c79779e | -18.49154 | -55.4968 | 2026-04-10 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 621d0ad4-637a-38e4-9427-9fbbbd8e58ff | -18.49361 | -55.50621 | 2026-04-10 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| b804249d-c0eb-3521-8c0b-0626cb00e0bb | -21.71659 | -48.43402 | 2026-04-10 04:44:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 31cb4915-6ae7-3a29-a3e5-4b540e6f02e8 | -18.49722 | -55.5069 | 2026-04-10 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e00bdda7-0fc3-3c9a-b575-f7af49bf560d | -21.72044 | -48.43456 | 2026-04-10 04:44:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 17262989-eb80-3e09-b2a5-367d39434bfb | -17.9125 | -54.12214 | 2026-04-10 04:44:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 62b5dcb5-423d-3f25-9ffe-71d37c155a15 | -22.88278 | -48.65 | 2026-04-10 04:44:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7522d568-6e71-3225-8bda-2f94846b7e7d | -18.49077 | -55.50116 | 2026-04-10 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 99f4acb9-5697-3063-a70d-662c6e7e556d | -18.49568 | -55.51564 | 2026-04-10 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| c53148f9-239a-3c7a-a8d4-5e317bbb7a15 | -22.88435 | -48.65233 | 2026-04-10 04:44:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d511a0b3-87c2-39c0-bb9c-4151b430fe61 | -21.71515 | -48.43012 | 2026-04-10 04:44:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87fef434-1ce7-3ba3-b57a-5bf1dbdc3f5d | -21.719 | -48.43066 | 2026-04-10 04:44:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5022e95f-d3af-3401-ab87-4800ce53f4cf | -21.71452 | -48.43521 | 2026-04-10 04:44:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c39c7ec5-9507-3e57-bb5a-cbb0f7cd433a | -22.87892 | -48.64948 | 2026-04-10 04:44:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12df6fb6-de95-33e4-ac34-1781ab29c98b | -18.49852 | -55.5207 | 2026-04-10 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 7b4845f0-6f62-30d1-90c5-9a8e8b8b246f | -18.49928 | -55.51633 | 2026-04-10 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 1d364af7-5963-3f7f-8b58-96a6269be528 | -21.71341 | -48.4284 | 2026-04-10 04:44:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |
| dccc0504-2394-3319-b431-c670213e0cc3 | -18.49591 | -55.49313 | 2026-04-10 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 09c9762d-1b46-3c74-836a-f71c71a7a045 | -24.38104 | -53.48331 | 2026-04-10 04:46:00 | NOAA-21 | ASSIS CHATEAUBRIAND | PARANÁ | Brasil | 4102000 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d273ae57-501a-3154-9637-98c4282926e0 | -25.13503 | -50.14054 | 2026-04-10 04:46:00 | NOAA-21 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b2814fd2-5cab-3630-b0f5-96fcaf03d50b | 2.91142 | -60.36995 | 2026-04-10 05:10:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e72043a8-d371-3a70-954e-b6d84fbc12b0 | 2.90169 | -60.36679 | 2026-04-10 05:10:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 955b21e3-6c4b-3d42-b670-1b39bedfbe45 | -1.52032 | -51.41262 | 2026-04-10 05:10:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92adb212-217e-31ef-b0ae-389464f6167f | 2.9069 | -60.3706 | 2026-04-10 05:10:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d972015c-2194-332a-aab2-e008804c9cea | 2.9062 | -60.36607 | 2026-04-10 05:10:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dbad6eb4-ed00-381d-af6e-f98d9dcbbf29 | -18.49322 | -55.51128 | 2026-04-10 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 01c00dd9-fc74-38f3-b38d-cfa4b5e3fcf3 | -18.49622 | -55.51617 | 2026-04-10 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 976d2d99-e517-3a65-b860-8ae05fc91ff8 | -18.49079 | -55.49514 | 2026-04-10 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| bd5bb38d-6a9b-3545-8f72-a9d8f5c3abfb | -13.24377 | -53.2963 | 2026-04-10 05:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a72abaf2-aa5f-3468-adf5-c10ba987d4b0 | -18.49141 | -55.49773 | 2026-04-10 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 61f83d27-6d00-3329-b152-ce98a0a3dec6 | -17.91229 | -54.12115 | 2026-04-10 05:14:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c81c88ba-929e-3dc9-ae2a-081386acea39 | -18.49562 | -55.52049 | 2026-04-10 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| ea497138-9336-3c8b-b6ac-cdc2537379d7 | -18.49924 | -55.49452 | 2026-04-10 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c6d3d246-970b-343e-8187-6ed0b0432d49 | -18.49016 | -55.49947 | 2026-04-10 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 466a417d-b27f-36d0-9565-8013648a775a | -18.49922 | -55.52106 | 2026-04-10 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 682dcdd8-37e1-30ca-88d3-ff46e3181c65 | -18.49863 | -55.49885 | 2026-04-10 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 064afcb2-7e13-388a-a5b3-6746e12841d4 | -18.49382 | -55.50695 | 2026-04-10 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 13850776-eb6d-386b-9c59-1b0bd71feb9a | -18.30981 | -55.33504 | 2026-04-10 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| b4ca00fb-3b66-3fe1-9ea9-6715921d414c | -18.49502 | -55.49829 | 2026-04-10 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 4193c516-e860-34a7-9748-e68e2e2b551a | -18.49803 | -55.50318 | 2026-04-10 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0e1da1ee-b543-35dd-8ca8-2ca0057ed38c | -18.49562 | -55.49396 | 2026-04-10 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| d7d0090f-c881-35c0-9078-7d17f6aa6ed8 | -18.49442 | -55.50262 | 2026-04-10 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| f924e407-f5b3-3490-9d1f-214b27cbf809 | -18.49081 | -55.50206 | 2026-04-10 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 88d4f3c3-a6f2-3d38-b6bd-87b0b99196db | -21.72023 | -48.43719 | 2026-04-10 05:16:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fed5692d-f16b-344b-b77c-ed637b1d752c | -21.20747 | -48.66226 | 2026-04-10 05:16:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 083b4482-a176-30d7-888e-2c7796ad85cd | -21.20787 | -48.65813 | 2026-04-10 05:16:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b2b5a6b7-d446-3779-8bab-0222af5b065d | -21.71477 | -48.4324 | 2026-04-10 05:16:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6504f5af-b44c-3e03-9513-15bedb930108 | -21.20919 | -48.66025 | 2026-04-10 05:16:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ddbe5d0a-2a9c-3536-b06b-11ccad5d43d0 | -21.71437 | -48.43675 | 2026-04-10 05:16:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4e1bf2c7-72b6-3384-9d1d-3dc3f8e8fb97 | 2.90429 | -60.36734 | 2026-04-10 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8ee923ee-10fe-33dc-b390-29eb09ed8558 | 2.90814 | -60.37026 | 2026-04-10 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84ff5432-e7e6-3a7a-a763-440ea657dc55 | 2.9109 | -60.36631 | 2026-04-10 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8459ced-a0cc-35d2-9551-f45c081b9bd0 | 2.90759 | -60.36683 | 2026-04-10 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e5e4f29f-2b24-3783-b0e3-ca5f8dfcc407 | 2.91144 | -60.36975 | 2026-04-10 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d598d048-9dba-3360-9e2a-3680bfb1069f | -18.48961 | -55.49607 | 2026-04-10 05:33:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f6d137d8-5024-3a3e-ad74-c5ea10f1cdd3 | -18.49286 | -55.49864 | 2026-04-10 05:33:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 043f9933-c123-3e94-80bd-ef139156a0e6 | -18.49177 | -55.50911 | 2026-04-10 05:33:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| ba39f518-719b-3cd7-98f4-26eb5556a0db | -17.9137 | -54.12328 | 2026-04-10 05:33:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d534a92-70c6-3b26-9a04-9e1804389e2c | -18.49798 | -55.51818 | 2026-04-10 05:33:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d9bebf9e-0459-3105-9f53-53a4da746a20 | -18.49992 | -55.5008 | 2026-04-10 05:33:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e73bddde-55e6-36b7-ad84-2f9778cc37d2 | -18.49418 | -55.50365 | 2026-04-10 05:33:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| e3805735-cc09-35a2-a5c6-efe9e754e1a8 | -18.49603 | -55.5202 | 2026-04-10 05:33:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 01782be4-ab6e-3133-bec2-e785f6b54302 | -18.49341 | -55.5106 | 2026-04-10 05:33:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| cf97ef13-2211-375f-9e58-54eec7a5d04c | -18.49759 | -55.52165 | 2026-04-10 05:33:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 947a0ecf-73b4-36fb-a665-c35a3ee44a71 | -18.49639 | -55.51671 | 2026-04-10 05:33:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| cd5ceb4c-7a78-3b21-ad82-81a15a344af7 | -17.91394 | -54.12144 | 2026-04-10 05:33:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7a1a3da-a210-3d4c-aabd-68c7af702822 | -18.49457 | -55.50018 | 2026-04-10 05:33:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f8aeff4b-340e-331a-8a2d-099319031543 | -17.90815 | -54.12072 | 2026-04-10 05:33:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52e1b2da-6c3f-3384-ae54-d52065abbf6f | -17.90791 | -54.12256 | 2026-04-10 05:33:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec35d36f-1eff-3091-98bc-a89f6f64359f | -18.49322 | -55.49516 | 2026-04-10 05:33:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 882917d7-8212-30d7-82a3-c40a23783d2e | -18.49712 | -55.50974 | 2026-04-10 05:33:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4f59255b-fa63-3255-8b06-07b31e4f866d | -18.49249 | -55.50213 | 2026-04-10 05:33:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 4e1185bd-6668-3ee7-a692-716d54339c8f | -18.49213 | -55.50562 | 2026-04-10 05:33:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| c6988227-4049-3c6d-8b78-10050b267a86 | -18.4938 | -55.50713 | 2026-04-10 05:33:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 1dea9667-0ecd-37e9-a2f3-a8d7c662199e | -18.49857 | -55.49578 | 2026-04-10 05:33:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b949b75f-ff9f-3906-92e4-98cfd35ef154 | -18.48923 | -55.49954 | 2026-04-10 05:33:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d389718a-175e-347e-acb4-7c8500d34a81 | -18.49821 | -55.49929 | 2026-04-10 05:33:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5e9871a0-e794-368a-ac01-128ed17f61d0 | -18.49784 | -55.50277 | 2026-04-10 05:33:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 660ff95f-7bf3-3b2f-8a36-cb0357a43a11 | -18.49496 | -55.4967 | 2026-04-10 05:33:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| bc697359-d1ce-3781-9ca6-3aba50dfd88e | -15.28182 | -43.07278 | 2026-04-10 06:14:00 | AQUA_M-M | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 1c6d0fc4-e5e6-3702-bd32-c1e599f52c7c | -15.28343 | -43.06104 | 2026-04-10 06:14:00 | AQUA_M-M | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 890d1094-2151-3424-bbe5-26c17937b372 | -21.71105 | -48.43488 | 2026-04-10 06:16:00 | AQUA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ec3ee821-d5ff-3976-9088-a6274c748cbd | -21.7125 | -48.42543 | 2026-04-10 06:16:00 | AQUA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5fa2c05f-381c-307b-ba45-5e9a779b4a65 | -18.49619 | -55.49583 | 2026-04-10 06:16:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.5 |
| bb4ecb7f-cd74-38cc-9019-51e4ed30c112 | 2.90407 | -60.36744 | 2026-04-10 06:18:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 89a77ee5-0b4f-3f08-ba2e-fbeff64c3e8b | 2.90407 | -60.36815 | 2026-04-10 06:18:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c458cae9-0315-31d1-a2c0-8879bca15f8d | 2.91055 | -60.36695 | 2026-04-10 06:18:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a7b49e25-d7e8-38da-a1ed-04475282d00f | -7.08048 | -45.77875 | 2026-04-10 12:23:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 0a547d5e-0848-303d-aeb3-07de89a47c52 | -11.96529 | -43.36332 | 2026-04-10 12:23:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 37579ed2-8e40-3165-a69e-63f63457b990 | -7.07282 | -47.82392 | 2026-04-10 12:23:00 | TERRA_M-T | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 6a3fe1d6-a9bc-31f2-b648-5fc3feac7f6c | -18.49587 | -55.49179 | 2026-04-10 12:27:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 72413c44-45b7-34fd-812e-499fea511cb9 | -18.50957 | -55.5223 | 2026-04-10 12:27:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.0 |
| bbd2aa4a-9d2a-32d4-8563-252bc75965eb | -23.71523 | -53.75341 | 2026-04-10 12:29:00 | TERRA_M-T | ESPERANÇA NOVA | PARANÁ | Brasil | 4107520 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 8ea6a694-fd71-3a56-89e7-f72786ca3b92 | -30.61402 | -52.74163 | 2026-04-10 12:29:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 9.0 |
| 2c1fa30b-6642-3cd2-b9b4-d724f87411a5 | -30.61225 | -52.75878 | 2026-04-10 12:29:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 19.8 |
| b63151e1-8716-385e-9cf2-b22bfcddec77 | -30.61241 | -52.74721 | 2026-04-10 12:29:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 19.4 |


