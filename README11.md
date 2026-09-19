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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76005fc0-0307-3dd9-8a71-292ec2a93a2a | -18.39581 | -49.16485 | 2026-09-19 00:37:00 | TERRA_M-M | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 47.3 |
| df1a923c-15c1-362a-8821-81c4bdd3721b | -11.93773 | -55.91684 | 2026-09-19 00:39:00 | TERRA_M-M | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c01d1844-f127-37f9-9277-a0ef8b55816e | -15.0738 | -49.59658 | 2026-09-19 00:39:00 | TERRA_M-M | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 36.4 |
| c50d4acb-6cc5-39fa-b41a-6fbf74fc464f | -10.87054 | -56.18773 | 2026-09-19 00:39:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 31.0 |
| e8e68092-125f-3a8a-8bc6-7ba6e67ad98b | -8.16084 | -54.82014 | 2026-09-19 00:39:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d2ed76ae-110f-3214-ab01-e0a1ad48689b | -11.94599 | -50.13705 | 2026-09-19 00:39:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 69610f1c-d9a8-3704-8ebf-a422169fb6f9 | -11.44028 | -51.48113 | 2026-09-19 00:39:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| cfcdb4cc-7316-36d6-8c4d-6c5fb4d3c982 | -10.87499 | -54.09932 | 2026-09-19 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 07347cb5-0b41-3500-a34a-0ff4bb56ed52 | -10.69714 | -60.73693 | 2026-09-19 00:39:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| d0d11fae-1d22-39e8-ab66-8d6137eb4176 | -11.24442 | -54.10256 | 2026-09-19 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 0dc0c94f-97e6-33be-a0b4-98f8a5f87709 | -9.04045 | -48.74437 | 2026-09-19 00:39:00 | TERRA_M-M | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 18f1215d-8d0c-3531-ac44-01ca1cb871e0 | -9.15466 | -59.45668 | 2026-09-19 00:39:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ca815ba7-9961-3b4a-81b2-7beb2f988f05 | -10.2014 | -57.90481 | 2026-09-19 00:39:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 11ea3967-1a31-3519-a87c-2704760140c5 | -9.68713 | -58.18348 | 2026-09-19 00:39:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 387a1f78-07f8-3920-97cc-452accd559ad | -9.88745 | -58.29835 | 2026-09-19 00:39:00 | TERRA_M-M | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2588a937-476b-3729-9b41-2452f2996c99 | -8.77367 | -48.68712 | 2026-09-19 00:39:00 | TERRA_M-M | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 38.6 |
| c0f29c2c-a10e-3778-b652-20a8469ea466 | -11.2999 | -51.72601 | 2026-09-19 00:39:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 9c8e2f3d-0d0f-3da2-908f-d29c47a143be | -10.86402 | -54.10117 | 2026-09-19 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 2dd1ed39-d87d-3453-9a8e-1a4fbd0b30c7 | -10.71565 | -60.73438 | 2026-09-19 00:39:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 7bdb6fae-8103-3efa-ac1d-166472cce164 | -11.13981 | -54.02367 | 2026-09-19 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 8c563568-acf7-3572-9094-63ee827788ab | -11.05575 | -49.77871 | 2026-09-19 00:39:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 27.4 |
| e35856a3-808f-3d34-9180-fc4ded73883a | -16.80457 | -46.98959 | 2026-09-19 00:39:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 39.1 |
| e5a9060e-be6b-3eb9-918c-99e0ceb63934 | -10.86253 | -56.19954 | 2026-09-19 00:39:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 0ea4a679-e8aa-3985-821f-b91bfbc79d92 | -11.91205 | -50.1199 | 2026-09-19 00:39:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| a4acccd7-1ae6-32f5-a8c8-de3f55c4edf7 | -10.02513 | -51.91273 | 2026-09-19 00:39:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 7aa7d455-55e3-3c9c-be11-81d89b37020c | -10.99514 | -57.05878 | 2026-09-19 00:39:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7c582267-8ab2-367e-a763-6fcefb93b611 | -11.67886 | -54.45575 | 2026-09-19 00:39:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| fe4b03a6-db65-36dc-9c5d-4ddd7f0b1005 | -9.37291 | -60.32358 | 2026-09-19 00:39:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ccdc05d4-9c18-3340-bffc-0a201873a96b | -9.69089 | -54.34024 | 2026-09-19 00:39:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| ff5987ef-4815-3d0c-8264-ebfdaf038dfe | -10.70769 | -60.74555 | 2026-09-19 00:39:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 8d42f116-5bff-3126-970c-f4e1b953bb97 | -10.7996 | -50.89863 | 2026-09-19 00:39:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 808bcb1c-203a-3ca6-b8d5-aa59a491a626 | -9.59239 | -60.51945 | 2026-09-19 00:39:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 08cd286f-47cc-3704-af03-946e0ab20c2a | -12.5944 | -49.12512 | 2026-09-19 00:39:00 | TERRA_M-M | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 8586e256-1d52-3362-9b50-3240bdf9862d | -10.87204 | -56.19812 | 2026-09-19 00:39:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 1fe49c51-c528-342b-8036-c21af45a8f6f | -12.14159 | -61.17439 | 2026-09-19 00:39:00 | TERRA_M-M | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9c50b81a-06a8-396f-98e7-6f138c55793d | -10.72621 | -60.74302 | 2026-09-19 00:39:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f3617e66-d1a9-3cec-acc6-031b468a0e9b | -10.69843 | -60.74683 | 2026-09-19 00:39:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 21.6 |
| dbf81425-5905-3476-95c8-7a683d901f47 | -8.48405 | -57.62257 | 2026-09-19 00:39:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f09e9383-d7f9-3e4d-9f21-ba9fdd82cfb9 | -10.86101 | -56.18904 | 2026-09-19 00:39:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 24.9 |
| f76087be-9c33-30fd-91ec-193160a29098 | -12.57921 | -49.10139 | 2026-09-19 00:39:00 | TERRA_M-M | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 33.9 |
| d8de68c6-4b4d-31ed-bd56-a6b92694cdec | -9.25474 | -57.13891 | 2026-09-19 00:39:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5aeb19b4-2a92-3dbc-808b-39fdf492cab6 | -9.39464 | -60.34893 | 2026-09-19 00:39:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 6bea6b86-9bd0-3a36-acee-68d862920bb5 | -15.07219 | -49.60348 | 2026-09-19 00:39:00 | TERRA_M-M | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 44.3 |
| e27bf83b-06fb-3c64-9a02-da42b76028cb | -10.71694 | -60.74427 | 2026-09-19 00:39:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9364faaa-8c63-3dce-9756-d5c3d4f66340 | -10.87355 | -56.2086 | 2026-09-19 00:39:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 7e0fbc0a-a091-3e19-b8c1-a41bfc74496d | -8.49314 | -57.62122 | 2026-09-19 00:39:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 58ced67b-0887-33e4-b917-7cf289c19da4 | -12.33864 | -50.72276 | 2026-09-19 00:39:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 025d53fa-927d-32d2-8841-5ec07d8459af | -16.30357 | -53.85897 | 2026-09-19 00:39:00 | TERRA_M-M | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| addf9fc0-1b92-3390-b79c-fa20adc5e7e1 | -15.58538 | -56.52845 | 2026-09-19 00:39:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 26a81be1-c478-3d94-8e10-a3b7a3431af2 | -8.14786 | -54.80796 | 2026-09-19 00:39:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5adf82c5-0103-3161-ba4f-d6c865acd246 | -11.93927 | -55.92744 | 2026-09-19 00:39:00 | TERRA_M-M | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b70f56a8-3391-3abf-9fe7-784cd7de3d84 | -15.67448 | -52.72974 | 2026-09-19 00:39:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a5d40e96-beee-3685-9187-4fdf4aac33d0 | -10.86406 | -56.21014 | 2026-09-19 00:39:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| e680b213-89d9-3033-9704-224f5b974530 | -10.80272 | -50.89254 | 2026-09-19 00:39:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 52b76c26-f0d9-35b2-8d17-9d60e65d9872 | -11.9796 | -52.45155 | 2026-09-19 00:39:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| edcc3eb1-9ff1-32e7-a562-75676c4741b3 | -11.01663 | -54.12909 | 2026-09-19 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 172ce03e-b1b9-3c99-9d9f-2cb6b41aded6 | -10.22842 | -57.82981 | 2026-09-19 00:39:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 6dc8a6c2-df7a-31d1-b207-2e3e399e0f13 | -9.15587 | -59.46558 | 2026-09-19 00:39:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 23573b6b-93bf-3bfe-a1cb-59a8b0d17f90 | -10.9349 | -53.96505 | 2026-09-19 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 43.5 |
| de6bcf04-87ee-3733-aa39-5124b0c2511a | -10.85948 | -56.1785 | 2026-09-19 00:39:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 52f16434-a670-38a4-b5f5-f2f43d8b1751 | -10.8903 | -54.05234 | 2026-09-19 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 129d3b94-9714-34b0-b390-72748115595f | -11.98241 | -52.44551 | 2026-09-19 00:39:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| ba94c468-5c3b-3b48-b176-55402819ffe0 | -11.98541 | -52.46383 | 2026-09-19 00:39:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 2051318c-c6c6-3032-bd5f-077daa182ac9 | -10.86624 | -54.11536 | 2026-09-19 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 8cbe9125-64e8-3ba3-ba1d-017a3e9666f2 | -11.97315 | -52.46583 | 2026-09-19 00:39:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 19.4 |
| ca7a141f-a0ba-3931-b5ef-d71ea411319b | -11.42311 | -51.46112 | 2026-09-19 00:39:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |
| d1e3e5e1-e073-311b-9594-bd00a50ec5a9 | -11.31314 | -51.74026 | 2026-09-19 00:39:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 237801da-2f6d-3d7a-8296-179a52b4a4ba | -10.92612 | -53.98149 | 2026-09-19 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.6 |
| b89a92c8-83df-3960-b9a6-2f309770572b | -8.49448 | -57.6307 | 2026-09-19 00:39:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 4258980f-f2df-3b4b-9ea7-5c6a5588828c | -10.83543 | -50.18113 | 2026-09-19 00:39:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 5313671d-0e51-3581-9f22-8439fd274f7e | -10.52291 | -56.79659 | 2026-09-19 00:39:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9b433e05-8f33-37d4-8f27-1938320f8ec1 | -11.44183 | -51.46356 | 2026-09-19 00:39:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 921fc056-70c1-3884-ad80-ae85c3a0b844 | -11.43652 | -51.45878 | 2026-09-19 00:39:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 2c34a4a6-cde1-3aa7-991a-e1f679ebef99 | -10.91504 | -53.98325 | 2026-09-19 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 6f5fc6c3-01d1-33da-b859-e62f4262576e | -9.89196 | -57.80068 | 2026-09-19 00:39:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 28252011-7693-3df8-9527-e4f3d4c656f9 | -9.39589 | -60.35824 | 2026-09-19 00:39:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 19602eec-9d75-397e-99d9-6536a6207262 | -9.70625 | -54.82441 | 2026-09-19 00:39:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 9b132ee0-2a67-3665-b08c-6b93ebcfe70b | -11.0188 | -54.14336 | 2026-09-19 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 9b196323-08df-3a6d-bcba-09fd9b2fd86e | -10.72491 | -60.73314 | 2026-09-19 00:39:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 6593949c-b7fe-38a8-bc7c-e83e8af9db39 | -15.66578 | -52.74708 | 2026-09-19 00:39:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 4c2e04c4-5259-316a-abbd-4db7de57150c | -10.92348 | -53.97254 | 2026-09-19 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 28694529-47f7-3f4d-af18-315268130d9d | -10.61906 | -50.26141 | 2026-09-19 00:39:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 82a8d8d0-0b31-3d48-8ea3-97906c08d7e8 | -11.67685 | -54.44268 | 2026-09-19 00:39:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| b7740ba9-9ff2-3a39-806f-d18fbf86ebf0 | -11.94621 | -50.14246 | 2026-09-19 00:39:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 9f3726ed-1813-345a-8acc-570d773346a0 | -10.88153 | -54.06874 | 2026-09-19 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 30.2 |
| c72f607a-9cb7-3015-9501-c4b8d6e953db | -11.05492 | -49.75376 | 2026-09-19 00:39:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 36.0 |
| c156eee7-5d5d-3408-885b-59dc9ebfb125 | -10.93259 | -53.95033 | 2026-09-19 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 3b324075-16ac-32b9-b8d4-4caba16d5e78 | -10.83378 | -50.17589 | 2026-09-19 00:39:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 36.5 |
| e7f45df5-46b1-3ae7-bb15-093171ca8ad3 | -9.54034 | -55.08874 | 2026-09-19 00:39:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d0244e9b-e1a9-339b-b310-7d8633c9c238 | -10.7064 | -60.73565 | 2026-09-19 00:39:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 5d2db3e7-02e4-3b01-b0a7-6f1a4d0770f1 | -10.87506 | -56.21907 | 2026-09-19 00:39:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 52d3eee1-e884-3860-abbe-55e67b02cea9 | -11.06011 | -49.78474 | 2026-09-19 00:39:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 39.8 |
| fc33a5cc-e0a3-3694-9394-d96253320deb | -10.99649 | -57.06833 | 2026-09-19 00:39:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c8e4636f-4f11-3a93-81b2-cc53ab30fafd | -13.68025 | -48.57573 | 2026-09-19 00:39:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 34.9 |
| d4c6fe9e-b1d0-34a5-82b7-a62ea5074f9e | -10.9238 | -53.96678 | 2026-09-19 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 31.6 |
| cac42d9c-7f99-3bea-92fe-149a3107c67f | -10.85303 | -56.2011 | 2026-09-19 00:39:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 94ad801a-ec2f-3d6c-8c95-853b67afaa19 | -11.07112 | -49.77594 | 2026-09-19 00:39:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 91cffa6f-d0eb-3a64-9f66-671998430619 | -9.93672 | -53.99459 | 2026-09-19 00:39:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| d32f9fd9-7d0e-3ede-9ce4-69b5f8cfdc90 | -9.33477 | -60.31643 | 2026-09-19 00:39:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c3e04c44-f600-38a3-91b6-027d65482d12 | -16.07125 | -52.25656 | 2026-09-19 00:39:00 | TERRA_M-M | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |


[Clique aqui para ver as próximas entradas](README12.md)
