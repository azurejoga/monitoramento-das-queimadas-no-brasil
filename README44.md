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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e389267-2342-3557-97d0-841dc88b6c1f | -11.73006 | -51.76179 | 2025-08-31 04:29:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 221e1a0e-97be-3f16-82b6-0f637e0d9f71 | -10.95211 | -50.84227 | 2025-08-31 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 327b1d49-00b2-382c-8f4a-bdca75056c10 | -11.9277 | -46.68407 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ede1aac0-4d48-33f4-aa2d-42fefea668b0 | -13.46403 | -46.9389 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb662e10-67d8-3913-8ebb-511677b5a226 | -14.54931 | -51.98019 | 2025-08-31 04:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e60d53d-17c2-3317-9fdc-1102704f2474 | -11.88986 | -46.70723 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 726f5d92-f7e7-3c02-8a11-7afcc4a6d04f | -10.604 | -44.32394 | 2025-08-31 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b1cd3599-234d-371f-93f6-9f2403d98bf1 | -13.02559 | -56.90938 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df78d7ec-dc7a-3766-8ab5-4a15e8f38544 | -11.79989 | -46.46671 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e9c2ab1d-c3ec-3f39-a2b8-6cf7a1c05d08 | -13.47552 | -46.96621 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb47ca8e-852c-3343-9193-e9d788492bee | -10.03249 | -48.08594 | 2025-08-31 04:29:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f0890e6c-ea93-3678-8b3f-01f2b039cd20 | -12.30879 | -45.69674 | 2025-08-31 04:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a910359-f4e2-3de8-a5e1-7f3ba6e7333d | -10.94915 | -50.83719 | 2025-08-31 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dba6ea80-f5ea-30cb-812d-28af6053d902 | -11.08849 | -44.74089 | 2025-08-31 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1267f7a2-41a7-3c2e-a11c-74442456a25d | -14.27977 | -51.883 | 2025-08-31 04:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4babb2c6-6fd4-3a48-82e5-2e9b86c9420e | -13.34705 | -46.97537 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4419e901-b9ba-396d-bd3a-9fb17900582d | -15.71795 | -42.59986 | 2025-08-31 04:29:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4eaefda2-fcde-31c1-9d4b-c22ebb4497a4 | -14.27521 | -51.88694 | 2025-08-31 04:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b9926aff-f15f-3ede-b1fb-0f1ec94478f4 | -13.39367 | -46.83857 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a7ab0936-38e0-3462-aa07-99f4ca0307b2 | -12.87048 | -48.08634 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c3a984a7-0430-3c40-8c4c-0e0a65e7cf8f | -12.3988 | -46.47895 | 2025-08-31 04:29:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38d93ec3-d362-3dd3-83b9-6ae2d132d581 | -11.84285 | -51.4961 | 2025-08-31 04:29:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d0d1c1c2-088a-37d7-b220-a036583090b2 | -9.68765 | -47.03849 | 2025-08-31 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01213b13-cdf9-3085-9357-ec41e6818699 | -11.90065 | -46.38297 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94d2b043-4b25-38bd-8946-0801d5de5a18 | -13.59027 | -46.89931 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c455fbbb-debf-3126-925b-529907f9428d | -14.98958 | -46.70273 | 2025-08-31 04:29:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 130190dd-bbb8-3d5e-b787-8e8de262f3ad | -13.51739 | -46.98384 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8742e60b-1123-377d-a007-605abce8d3f8 | -13.48215 | -46.94544 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea9be533-81aa-3199-bd6b-47947dcf652f | -13.35153 | -51.7667 | 2025-08-31 04:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba1970a5-b94f-37b4-8095-47faccd51bd8 | -14.35174 | -51.8914 | 2025-08-31 04:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f921fff8-93a7-3806-8e03-08c9781df09e | -14.35685 | -51.90655 | 2025-08-31 04:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 72b665a6-2f46-35e1-8726-d8365a96e481 | -12.64058 | -48.21253 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b16348b-e75b-3406-9bf5-1cc95ed2b13d | -13.47936 | -46.94127 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 61be8ae0-b92a-328f-8732-d25ea0472afd | -12.41502 | -46.46302 | 2025-08-31 04:29:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf99074a-b074-3e0a-a30d-07e4683694d3 | -13.35374 | -46.95436 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73ae1b2a-ac80-365a-b4a8-ee5b2bd0b7b5 | -14.03737 | -44.56995 | 2025-08-31 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b41abb3c-31c8-3fc0-b8b2-f5e92e4394b3 | -12.92372 | -56.98838 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| de186a1a-544c-3016-b64b-a881cafa69fd | -13.01651 | -56.90685 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8523ae59-d35a-37cc-af50-615bcddff360 | -12.91698 | -56.98018 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 56c8fcf3-2167-3ea9-9d0d-77ee01554f6e | -13.3045 | -44.27302 | 2025-08-31 04:29:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7da49276-a409-3629-b57b-b145a70c81b1 | -11.86332 | -46.49109 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61b44318-554a-3106-af8f-c235f3f24be3 | -11.82239 | -46.4222 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a7fac9e8-afa2-384b-beb2-21dd094cbfec | -11.90346 | -46.3871 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 626053fe-16b7-3132-a081-8243c9c26778 | -11.29617 | -43.63895 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21af464e-4953-3da6-a0dd-26678ba7aba2 | -11.89738 | -46.47078 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd57f2c3-4e0d-32ab-8a31-ad58c8b0770a | -11.88989 | -46.72915 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 04323c44-3e74-35be-8ec3-ccfd927c133e | -11.88211 | -46.73518 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 721ae0d6-edb5-38b6-af41-a06ffcac1b23 | -11.8252 | -46.42632 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 59c6d18a-7d19-3cc1-a509-666c42897d00 | -13.3659 | -46.9523 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63e6019e-6fa8-3ee6-8f0d-04201ba1556e | -14.0387 | -44.56327 | 2025-08-31 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| aa7b6cf3-fddc-351f-8ad4-27695f5279de | -11.90598 | -46.69158 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 87ceefae-fac7-3cd3-b529-8cf41921edf8 | -10.96393 | -50.86266 | 2025-08-31 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d101c6b9-b7a6-30b2-93a3-e61f2f45bff4 | -11.89379 | -46.72609 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bc6f6c5a-fd3e-3b5f-95f8-8f44d434ffe6 | -11.30344 | -43.66749 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e787ce4c-72b2-393d-93af-65eb244b268a | -15.07183 | -48.62304 | 2025-08-31 04:29:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e68b02c-11b2-3acd-a6a1-15d04e7bfc30 | -11.05845 | -52.04782 | 2025-08-31 04:29:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27dcd23e-e9ee-3f5f-8367-e294562dbe4a | -14.33623 | -51.86958 | 2025-08-31 04:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e4793bba-6d1f-3b3c-ac61-3fd8900b8dea | -13.33413 | -46.85931 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45d4b4bc-87ab-3754-9a01-58b26a2555f7 | -11.35588 | -43.6207 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff27cd29-4762-399c-b88b-8dfd6310d19c | -11.8258 | -46.44474 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 122c7c10-7d57-3e68-9b0a-3c0b26147793 | -11.32573 | -43.67077 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 287ab187-bfa2-328e-82df-b7adbab336f2 | -11.24192 | -44.67638 | 2025-08-31 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 24b54c35-6120-34b9-bfc6-435881a887ad | -10.47621 | -51.63481 | 2025-08-31 04:29:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 39ad7537-0f0b-39ef-b023-bd27306259d1 | -12.56545 | -44.7993 | 2025-08-31 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c4f54f0e-e016-3986-bf10-2198dd2a7cb9 | -11.3652 | -43.55736 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b8668ef-edf2-3ea7-8869-51984c58fecb | -9.50489 | -49.10174 | 2025-08-31 04:29:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aca75309-ab96-3915-95af-29baa296f3f1 | -14.41185 | -53.44314 | 2025-08-31 04:29:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a889b4a-40c8-3a82-ae07-a06698e9e67e | -12.80261 | -48.08916 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 652a0f0a-57e9-3bf6-a07b-c0d18b210784 | -15.07574 | -48.62 | 2025-08-31 04:29:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 802d838b-5e1c-3073-8413-839b24400a5e | -11.31137 | -43.69123 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b684bb14-2220-3e04-a3d5-79b037448447 | -13.36925 | -46.95288 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d5992ad-b954-3e3f-b42e-13250d274c1d | -13.54249 | -46.95466 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2a137073-a313-3897-9556-dba9d0a1520e | -13.02427 | -56.89495 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6e6bb37-8130-3210-bcfb-ca4648eafd23 | -11.89223 | -46.37067 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5d8bc88a-8147-3e43-ad7c-da73e91d0ff6 | -12.86326 | -48.08876 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d5692de0-2482-3c6c-82aa-5f302c166ccd | -9.65995 | -48.34126 | 2025-08-31 04:29:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75ac0bee-1321-35d2-9fc8-c48a877a4518 | -13.34984 | -46.95741 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a1dbf56-3c11-36ce-9303-2651e7dca75e | -9.66218 | -48.349 | 2025-08-31 04:29:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b49c3a1-9954-3451-8a52-575458241949 | -13.67798 | -46.93212 | 2025-08-31 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13756c21-7ce2-35d9-a0e8-9a1e0a06e8b8 | -13.31019 | -46.88102 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 71190516-746c-34bf-a3aa-3395e3864c4c | -12.63344 | -48.19303 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7016a3ed-8149-341e-a2f5-23d14d297716 | -13.03084 | -56.91054 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| caa0e229-eae6-3690-9e4a-783922baef70 | -14.83059 | -46.74253 | 2025-08-31 04:29:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a3f3bcf-3ee0-39b9-bd4e-1f299a5eee1f | -11.00636 | -46.84614 | 2025-08-31 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 54b20fd2-a49c-3622-a401-9f295a5d61c0 | -13.02295 | -56.89516 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab7be8da-00b3-3d95-8781-662f1b98e48f | -11.34364 | -43.52166 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f621a87-5bf4-3b09-b291-30e1f46de37f | -11.29925 | -43.64394 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12c2a293-71ac-38d0-97af-d6433e1ac40a | -10.93042 | -46.83789 | 2025-08-31 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f653b99a-ae3e-3e03-a069-45dd75fc00de | -11.80233 | -51.43634 | 2025-08-31 04:29:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd54da41-197e-3ab4-81fd-d633120b6298 | -13.47546 | -46.94433 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2cc92361-c1b7-31ab-87ad-fe6381efbe9c | -11.56067 | -47.62168 | 2025-08-31 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8bf303dd-bba9-38f4-b727-5707ec6e5c07 | -11.83915 | -46.425 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5f5a3059-df3a-3533-bce8-fcb4060847ea | -10.03808 | -48.09406 | 2025-08-31 04:29:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b95487ba-3546-3da4-9215-6782be5dbd4b | -13.68848 | -46.8863 | 2025-08-31 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f556e3a3-74dd-3c50-9ffe-22f1c77c766b | -10.71087 | -49.01173 | 2025-08-31 04:29:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a2f8673-e178-31c5-aaf7-958b5d4e4c2c | -10.93708 | -46.83895 | 2025-08-31 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 296e581f-2ae5-3f91-88fa-f83759377d14 | -11.34713 | -43.62843 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d241e03-0099-374d-9c75-a3439d9d480f | -14.99967 | -46.70482 | 2025-08-31 04:29:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 1aa675e1-da56-355e-96ff-9dd2be3a9860 | -11.88321 | -46.72809 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe739c12-806c-329c-b088-51622ece545b | -10.01298 | -48.36474 | 2025-08-31 04:29:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README45.md)
