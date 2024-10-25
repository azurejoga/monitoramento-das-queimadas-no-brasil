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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c97d85d8-5725-3d85-bcca-f0ee687be6c1 | -11.71326 | -43.9095 | 2024-10-25 04:40:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad56df0b-a8ed-381b-8c11-04b76fb3431b | -11.71265 | -43.91402 | 2024-10-25 04:40:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6a38eaf8-8bac-3242-b40e-d7dcf8177d3f | -11.69396 | -43.81388 | 2024-10-25 04:40:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b42b63f-1dfd-36f3-b92b-1cc49b1f6660 | -11.58304 | -43.98113 | 2024-10-25 04:40:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1cdb75ae-021d-3cc5-9d68-421b4eb8e7a1 | -11.57918 | -43.97604 | 2024-10-25 04:40:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| d65e3a0b-8844-3ea8-9b32-36fdbf07a709 | -11.57857 | -43.9805 | 2024-10-25 04:40:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 508d71cb-ba55-3e16-ab54-2b6496b4f46f | -11.53663 | -43.98825 | 2024-10-25 04:40:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c7674fe7-551d-34ad-8795-abfda86d7dcc | -10.90651 | -43.99755 | 2024-10-25 04:40:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 437902e6-9d49-3df2-8d20-566c4e6e3915 | -13.70473 | -43.65907 | 2024-10-25 04:40:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f6f0915-c8eb-36a7-9a97-f3d9fe1903dd | -13.64461 | -44.29868 | 2024-10-25 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0e9079f9-92c6-3ab0-bda1-914ceeac8b22 | -13.62468 | -44.34724 | 2024-10-25 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fb3eae4c-b9b2-3d08-b38d-dc6d29b4cb63 | -13.6225 | -44.31218 | 2024-10-25 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 246b0194-9559-3f2e-90c0-a67d885f16eb | -13.4963 | -44.42234 | 2024-10-25 04:40:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 16c83f52-bd82-3033-ba82-ed6bfdb3dbb6 | -13.49402 | -44.4239 | 2024-10-25 04:40:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 39cabfa3-8c24-3ed1-8468-cfdcf04fa2fd | -13.49186 | -44.42162 | 2024-10-25 04:40:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d88469ac-adfa-36bd-9f40-dad5ed89e5a2 | -13.48958 | -44.42319 | 2024-10-25 04:40:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7924cf32-fdd7-35c9-af9c-2bc62755623b | -13.45515 | -44.07193 | 2024-10-25 04:40:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e27c9f08-f65f-3500-a959-a57e835539b5 | -13.43278 | -44.35307 | 2024-10-25 04:40:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3a26cec-0e0f-34d3-8c63-7052355d634e | -13.41839 | -43.77899 | 2024-10-25 04:40:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f8928bd-653e-31e6-92a2-415657506e09 | -13.29294 | -43.96153 | 2024-10-25 04:40:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 91421096-5f2c-3e63-94ec-694d17d08c2b | -13.28835 | -43.96096 | 2024-10-25 04:40:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3d652dfa-cb45-39b0-a685-349b7be16feb | -12.67192 | -43.43758 | 2024-10-25 04:40:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39330590-c2f8-3255-ab42-8a35784e0064 | -12.5843 | -43.83183 | 2024-10-25 04:40:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b82a0892-94a9-3553-93fa-bf49c0b1c19d | -12.58367 | -43.83652 | 2024-10-25 04:40:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| e89e1afa-6828-3263-ad93-da4685fb7665 | -12.5791 | -43.83585 | 2024-10-25 04:40:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6205a7c6-5eeb-396b-8ed4-b60cb0edca35 | -12.4688 | -43.79375 | 2024-10-25 04:40:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a98dd5c2-a8e1-3b96-a152-d5e2d91249bd | -12.4442 | -44.4079 | 2024-10-25 04:40:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| da7849ff-1b4e-3824-abb5-2929ad324247 | -14.16241 | -44.17403 | 2024-10-25 04:40:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14050658-fbd1-323c-a128-45ea4f2b5e6e | -14.16178 | -44.17561 | 2024-10-25 04:40:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95ef6253-7d50-3ddd-9413-dbf801dd46c0 | -14.15369 | -44.24022 | 2024-10-25 04:40:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4ad412a-eece-35a2-aebc-4d5995570a7a | -14.15355 | -44.24195 | 2024-10-25 04:40:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b3245df-8bd8-3ecf-bfdd-e5c00131bef4 | -14.14914 | -44.2396 | 2024-10-25 04:40:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1de5c1f3-e300-3016-9e49-a92552e508d6 | -14.149 | -44.24134 | 2024-10-25 04:40:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15008f0e-0d47-3cd2-9a22-422bdc22ecdf | -14.12175 | -44.3076 | 2024-10-25 04:40:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b6cf8669-ea3e-33a4-88ef-c0fc61501d86 | -14.12114 | -44.31226 | 2024-10-25 04:40:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 50b00d35-c76d-37bb-8800-1e35402d6a27 | -14.11722 | -44.30698 | 2024-10-25 04:40:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 13414a0e-6912-3f6e-bd72-f945a9343915 | -14.11662 | -44.31163 | 2024-10-25 04:40:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 516f54f7-aec8-362b-a58e-d630ea6e889c | -14.10604 | -44.21471 | 2024-10-25 04:40:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25956c98-8cd0-3039-af17-396813ad86b9 | -10.88038 | -44.54104 | 2024-10-25 04:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f6234cea-6de8-3f66-8e4f-5ad515195db3 | -10.87722 | -44.68602 | 2024-10-25 04:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 27d43e8a-a00d-3887-b046-f98873a42792 | -10.87477 | -44.79348 | 2024-10-25 04:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9db98618-d135-3df9-90fb-258af2c138f8 | -10.87169 | -44.78511 | 2024-10-25 04:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 94850517-e31a-3665-9b37-10c3a2c89678 | -10.87164 | -44.78796 | 2024-10-25 04:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7e3a00f6-af55-36a6-9af0-caee792f94f8 | -10.87113 | -44.78905 | 2024-10-25 04:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 316cd8ea-082a-3d90-bab8-75165f85ca6f | -10.87111 | -44.79184 | 2024-10-25 04:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 952fcf59-d7d6-382d-9d3d-1f31f22e81be | -10.87058 | -44.79292 | 2024-10-25 04:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 133db090-3b02-31b2-b796-fceed78ee1f1 | -10.86751 | -44.78455 | 2024-10-25 04:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| db28b54d-78e0-3eaf-816d-2bdd601a1aa1 | -10.86745 | -44.78736 | 2024-10-25 04:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 97c7ef48-6970-31a7-adde-1a1feb9e6903 | -10.86695 | -44.78846 | 2024-10-25 04:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cac922b8-e4b5-3cce-b7b2-318fdd57ced2 | -10.86693 | -44.79124 | 2024-10-25 04:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b11c8778-9c0a-3643-ad83-16b39a4d6803 | -10.8664 | -44.79232 | 2024-10-25 04:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 62319416-f865-3f0d-8f9f-c62ede9bb045 | -11.31195 | -45.01859 | 2024-10-25 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4ba0fc8-8666-3bc8-9fc8-80b2096315e1 | -11.27311 | -45.02448 | 2024-10-25 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11963a56-f27c-3daf-84dd-b407f82ca9a1 | -11.27206 | -45.02153 | 2024-10-25 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09e9d864-6a94-383f-b6f5-e997989aaf4d | -11.27151 | -45.02532 | 2024-10-25 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d0ae74f-eb15-3e92-85c1-ea8c503495a9 | -11.26897 | -45.02384 | 2024-10-25 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0405778a-4bc9-350b-a265-d17531fee76c | -13.57421 | -46.16005 | 2024-10-25 04:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0ab0dff-e198-3e7c-9429-dd83ce41dbfd | -13.57218 | -46.16216 | 2024-10-25 04:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 569afd97-ff44-313a-8b32-ca66365ed5b6 | -13.55891 | -46.52589 | 2024-10-25 04:40:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c43b7f3-6e27-3baa-b4bd-b6ef09343ba7 | -13.55502 | -46.52531 | 2024-10-25 04:40:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| beec0792-5aaf-320f-8ff5-84c5f24fcde2 | -12.90501 | -45.07514 | 2024-10-25 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b47d680-7530-30dd-96ba-2ef326fdbd3e | -12.90448 | -45.0791 | 2024-10-25 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7297f40-fd2d-30ed-95ac-0ce8322befbd | -12.90131 | -45.07058 | 2024-10-25 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4096922e-12d6-36dd-b44b-b564f3d00368 | -12.90079 | -45.07454 | 2024-10-25 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c02f4fd-99ee-3cdf-86b0-7b8495bcc4f0 | -12.90026 | -45.0785 | 2024-10-25 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3cc834d4-df9a-3f20-8dea-c0838dca31f1 | -12.89656 | -45.07394 | 2024-10-25 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5f3a4c53-5874-389a-a150-1f8979b0d76e | -12.46501 | -46.33939 | 2024-10-25 04:40:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e46476fb-914b-3bba-8998-d382eb23b874 | -10.46486 | -47.33648 | 2024-10-25 04:40:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b93e5e2a-b5da-3994-b859-e12124837ea8 | -10.46189 | -47.33181 | 2024-10-25 04:40:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a258a243-6d48-3058-b696-9bf2c0a325ed | -10.43988 | -47.3072 | 2024-10-25 04:40:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| abd1ed0a-3571-3f9b-b072-20a4a490cf2d | -12.33235 | -46.75191 | 2024-10-25 04:40:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54cbcd76-7426-3b76-a1ac-95c009f88297 | -12.19749 | -46.72806 | 2024-10-25 04:40:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0bfbd69-878c-3d09-9933-607fdec56538 | -12.18015 | -46.98888 | 2024-10-25 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ea14d09c-f844-3bbf-913f-5378eb6f38ee | -12.17818 | -46.99098 | 2024-10-25 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3a21f9dd-8e5b-3ad1-81a8-2c37eecf489c | -12.17707 | -46.9838 | 2024-10-25 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ecd1ac40-be21-3758-90f2-ea134cabad14 | -12.17512 | -46.98595 | 2024-10-25 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a5c5b7e7-0fc4-3ae2-8ede-28b865b81512 | -12.17376 | -46.99517 | 2024-10-25 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b6fbbe2f-f5db-30ac-83ff-58f6f1c82632 | -12.17334 | -46.98338 | 2024-10-25 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 481b1fbb-5366-3f9f-8a73-991fb36c4d47 | -12.17268 | -46.98808 | 2024-10-25 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a09ad6b-0eb0-3e58-bff1-a97ea4fa1f41 | -12.17138 | -46.98554 | 2024-10-25 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8ae17a6c-9e8b-383a-93ac-47aa63879844 | -12.16894 | -46.98765 | 2024-10-25 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7c7ac26-c0f8-3a12-be46-92101c484592 | -12.16696 | -46.98977 | 2024-10-25 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0b36b644-1661-389a-bafe-6f37748edd7d | -12.06546 | -46.89703 | 2024-10-25 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f7ca272-b5c5-3629-9949-892d70b4d978 | -12.0593 | -46.88696 | 2024-10-25 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb09be85-2267-3978-88c4-6d4150990a56 | -12.05864 | -46.89147 | 2024-10-25 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 904850c4-d531-3225-9204-1cafe944f245 | -11.94466 | -46.58619 | 2024-10-25 04:40:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6f7f0180-5665-316d-be80-ef3a126ea913 | -11.93457 | -46.57544 | 2024-10-25 04:40:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be21d260-5003-3341-8108-5e4c40203516 | -11.93392 | -46.58002 | 2024-10-25 04:40:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a569030f-06cb-321a-8ac8-1167bed33256 | -11.93327 | -46.58462 | 2024-10-25 04:40:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6673439e-3117-3c2d-bcdc-430219be3438 | -11.94161 | -47.48814 | 2024-10-25 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a40a6f01-2f6a-367b-bcf2-c756da647c73 | -11.87889 | -47.71666 | 2024-10-25 04:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 015e5f06-02d3-3a1d-a22c-31652599885e | -11.87592 | -47.71204 | 2024-10-25 04:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 805efc90-2c75-3382-888a-0ec597bab0ad | -11.87532 | -47.71614 | 2024-10-25 04:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d3e19be-4312-34b4-ba99-7789d65dbf45 | -11.62681 | -47.57775 | 2024-10-25 04:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60bc2a6e-f8f3-38ab-8230-2e02db5c0f10 | -11.43116 | -47.67996 | 2024-10-25 04:40:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7641dbc8-1165-3d79-89de-70e2a77d3ecf | -11.43057 | -47.68406 | 2024-10-25 04:40:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d581624-a533-38c7-99fb-d6bb5fe18253 | -11.4286 | -47.68017 | 2024-10-25 04:40:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a37b2407-07fa-31b1-80e7-3f00b3d23a20 | -11.34996 | -47.31387 | 2024-10-25 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4457226b-0161-3504-8663-fce16c39c2ad | -11.27759 | -47.5798 | 2024-10-25 04:40:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b2fab6f-5fa2-31cb-806b-91515c56f271 | -11.19651 | -47.56871 | 2024-10-25 04:40:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README71.md)
