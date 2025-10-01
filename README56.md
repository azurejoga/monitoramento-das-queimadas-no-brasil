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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88adb043-9dd4-373f-990a-3dd346fbac10 | -16.37134 | -47.03135 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b73ed19a-abb4-3d3c-b07e-ebd9bb5e32ad | -14.06192 | -45.03861 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3505fe13-bdc5-348b-be4c-5bd31f24bdef | -14.78742 | -45.77116 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5974ea7b-47ca-31e7-9c8a-4205171b8f3d | -13.14127 | -47.41412 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d7f28fd5-1a59-362b-a7ff-4cd3fe34fc5a | -13.77656 | -47.95378 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 24e041d0-e86d-3e47-a001-11a86afd9998 | -10.63897 | -48.52766 | 2025-10-01 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a7100523-928b-3c4f-be19-fba7aa6f9ff3 | -11.40643 | -44.8951 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55664051-8860-3f83-8742-626f35f462df | -12.88155 | -46.91201 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| db1b5f27-deb7-38b5-be39-87c869ce0dba | -11.82913 | -44.95411 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2495c2e5-25e9-38c3-9001-c82034302515 | -12.77568 | -46.91327 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45655d26-d16c-3589-92ac-6e4de907bf4d | -11.62413 | -52.24718 | 2025-10-01 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a56096a4-7bdd-3742-941f-538d4e81fb73 | -10.3609 | -48.78199 | 2025-10-01 04:21:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52fbab56-ce53-3e8c-a381-952c4b8a7c2b | -11.91582 | -48.00434 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec184f52-32f4-32fe-bd0d-da2a8a870199 | -11.28108 | -39.22032 | 2025-10-01 04:21:00 | NOAA-21 | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9bcbf876-185a-3c68-8f1c-cde29d2acef1 | -11.84029 | -48.05786 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| a2805f89-0f71-3081-b4e2-f0e67342451d | -15.53328 | -44.34929 | 2025-10-01 04:21:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 207b493e-ffcb-350e-a118-a15a3a986639 | -13.45851 | -47.24216 | 2025-10-01 04:21:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9bd6a26b-a6e8-3ad5-b455-1807d8895634 | -12.87598 | -46.77359 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de29d31d-1663-395e-a005-0930f2fe0536 | -12.82332 | -47.01959 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3ac24128-2d8e-3e81-a006-98f61ad5b427 | -9.5607 | -50.77806 | 2025-10-01 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2c535321-fb24-3ebc-a040-f0bf8384d88a | -12.82214 | -50.55359 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2ede6d0-24c0-3ca9-bc0b-56f13d5189ae | -9.43242 | -54.71973 | 2025-10-01 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25cdce64-279f-3f6f-b5f7-219bc9765b34 | -12.00923 | -46.59443 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9feaf36d-5231-365e-9925-45d99a92adf8 | -14.90708 | -47.2104 | 2025-10-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96bfea36-e08a-3984-a9e2-2a06be11f210 | -14.68941 | -45.27197 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68eef894-785b-3d43-8e0b-5c6cc9539e9c | -11.79978 | -47.59828 | 2025-10-01 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c841e1e-9030-3d80-bd52-087379b04939 | -12.92743 | -54.72554 | 2025-10-01 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8040adaf-df5e-3522-8210-dd7936f51797 | -15.27211 | -47.84278 | 2025-10-01 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d98b392-286f-3d08-bba7-14c0298d3360 | -12.85374 | -47.02094 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9f5cd438-2035-3052-ae93-4f2eedf881c4 | -13.94077 | -48.1143 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f36dea04-e335-3a7e-8741-246cd04f66d8 | -11.83754 | -44.98824 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e8323433-991d-3a81-9c27-838ae1e057be | -11.84093 | -48.05405 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 0e8f336b-da44-3599-be0b-b9a12d7eb96e | -13.41812 | -47.53733 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc5c47be-7a30-3c9c-8796-267f7abc5aab | -12.00083 | -46.64735 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 175492d2-6e86-326f-9be2-bab93ba57f09 | -11.12036 | -49.78383 | 2025-10-01 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6154a7b3-eb05-389f-af97-301d600d13b8 | -14.65807 | -48.14052 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c40b27de-087f-3e74-961f-50245844aad8 | -15.26028 | -49.25739 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 617b83ec-a7a5-3df0-ac81-6700d8b31d4e | -15.3629 | -44.15253 | 2025-10-01 04:21:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8f3b6366-0218-3d64-8b79-460e40a712ef | -9.5139 | -54.74609 | 2025-10-01 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e155b9db-1919-3f2b-bace-e1c44edeb484 | -15.27458 | -56.77679 | 2025-10-01 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4be899ef-c342-3a6b-bb33-fbdc51a30ff5 | -10.73733 | -45.37708 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39d479c6-a3b9-3747-950c-e81bdfd87a77 | -15.41878 | -47.05108 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3b7690ef-d66f-33c2-9232-eb8600408206 | -11.39203 | -44.9001 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a8844de9-022c-3ddf-ad73-79e8b9995975 | -12.95919 | -47.17044 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d7345c6-8340-3aaa-8125-c9b5c4855783 | -13.73106 | -44.24167 | 2025-10-01 04:21:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31faef43-0f01-3554-8934-b9f2662565e9 | -11.63647 | -47.49638 | 2025-10-01 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4095bbe0-e458-3f25-8035-d09428da7d8c | -12.08696 | -47.25766 | 2025-10-01 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0fc82cc1-ae5e-309e-8921-1bd82f4f02d8 | -14.62698 | -46.98107 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0960f7e0-29e5-34c6-a6fc-8dbf8a087a7e | -13.76409 | -47.96674 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3910c9ec-45bf-3677-ba41-fc7ba85ab392 | -14.98903 | -50.76703 | 2025-10-01 04:21:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 45d8d707-3527-36dc-86a6-a1960ec6fb1b | -10.90714 | -46.50422 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0de7cb6b-f10b-37f9-b292-6a8a0182bea1 | -14.68105 | -45.28193 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 479ac749-1822-31f7-b66a-ba3e7e9ba5d0 | -10.80546 | -45.35205 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a05ed9af-63a3-350f-8914-f1e2136935c6 | -13.76721 | -48.40151 | 2025-10-01 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1665c553-fed2-35cb-89dc-51579afc53c2 | -14.91329 | -51.67237 | 2025-10-01 04:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| e0525941-43ac-3c41-a76f-30b6df9e01b1 | -13.94291 | -48.12241 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 3058186a-0f68-35f3-8ad1-b076b5895946 | -14.73246 | -46.82756 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30f13231-fd37-3ba9-ad98-d8428dd22944 | -15.25052 | -56.80872 | 2025-10-01 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 52ca197d-47fb-3eee-b797-f16707f29dcb | -14.19004 | -46.11764 | 2025-10-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 0aeb058f-cfe8-3bcd-bf31-3dd4c7d0ca89 | -15.00594 | -46.97141 | 2025-10-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6edf9fa4-aefd-3b43-b9ef-c30c85a638f7 | -14.72475 | -48.26201 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a95bc0b4-f5e4-3738-9d44-3519d6b4b326 | -12.85487 | -47.01381 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65bc58f2-951d-326a-8a96-b6466afbcd3b | -11.16178 | -47.21201 | 2025-10-01 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c15e97e3-2a58-3a4f-8ed8-5fe5ef160370 | -12.85156 | -47.01323 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c91bcc5-fc4a-3b4b-9038-b10b94359039 | -13.80835 | -47.98243 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2fa49c80-8a93-302e-b531-cfb260fcf025 | -10.83466 | -45.38535 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83558fb3-a58c-38dc-bfc8-fb8b4734624c | -11.83306 | -44.97297 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e52e1d7a-2d37-3823-a8f4-98cf5f31c677 | -13.97708 | -44.87833 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f33ad96d-a529-320c-a4f9-4aa6de3d09f8 | -11.76516 | -46.8449 | 2025-10-01 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e3c4eb6b-8fa0-3b6d-abae-f4ee6cdcc97d | -10.90928 | -46.53349 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c9e5de2a-daf0-3fb3-b170-dab55d80bab5 | -13.67313 | -48.06981 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c1c1e52f-df45-34ff-ae89-9c94b6c9c8d9 | -10.83537 | -46.65578 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f7997e49-c25b-3074-a8b9-57b18cb6e59a | -11.82408 | -48.07075 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 771ac01c-cbec-3168-82ae-827865859d01 | -11.80315 | -47.59885 | 2025-10-01 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3577af6d-3fa4-30e1-8bc0-ed05fc666ce3 | -13.04433 | -47.08559 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b188f5bd-40f4-3315-a0ca-e6b5972e22b9 | -12.82939 | -47.02422 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab182a2d-fbfc-3ecf-80df-0fabc63cbe4d | -14.68721 | -45.28667 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1dc85f01-7aec-3fb3-b14f-f379a177517b | -15.23501 | -46.22173 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9d51810-edad-3fc4-9158-3792c94d058b | -12.91965 | -47.16333 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5ebfefa-53e3-3df8-b551-d351e0d7ac63 | -13.35283 | -48.14242 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e51e6064-9c53-3247-bdf5-1b0e558a1a02 | -13.33746 | -47.33993 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f7c3232-4cae-36f8-86c4-dc0727480db7 | -13.91859 | -48.08029 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 16094d0c-791a-3e69-b1e5-8f695cdc6e10 | -12.69658 | -48.56174 | 2025-10-01 04:21:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c3d2fc7f-ecde-31f6-9fd7-6328058a0b86 | -12.96031 | -48.43051 | 2025-10-01 04:21:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b662009b-5d06-3ffb-8873-184c4a2911b8 | -10.90422 | -46.56525 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e661176-6276-3b77-86b2-ebeb6b4e81bb | -10.48304 | -55.62498 | 2025-10-01 04:21:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f5d48d9-3656-3021-a63f-e84631841ce3 | -12.00414 | -46.64789 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ec14fc59-0e25-37cc-8c94-55b6bce600b2 | -13.11708 | -47.03553 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5dc651ff-b89f-393c-988f-bf1b7f4a3532 | -13.75655 | -47.92805 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 53737a27-ae55-3f79-b8fd-d36a448a9f4f | -12.43026 | -50.17963 | 2025-10-01 04:21:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0cad8c6c-24aa-3792-946c-83e461edc1fa | -14.96441 | -46.86977 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d44d92b9-6128-3e77-9ef8-41046d3b409b | -11.99365 | -46.64981 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 074bc654-e740-35c5-ab03-00d904fa4966 | -14.34985 | -45.92104 | 2025-10-01 04:21:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d5f7d586-a7c0-3363-a7ef-6a619d63cbe1 | -12.21273 | -47.80311 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2c985b00-091f-362a-938d-9c2d5ea7fe0b | -15.36379 | -44.15197 | 2025-10-01 04:21:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 477c1a68-1816-3097-8800-d6089138c6e2 | -11.37862 | -45.07639 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b4068b90-c0c4-3c85-806a-32828e7100d4 | -13.75535 | -47.93542 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4b8c395-17a2-3a92-9f78-0fe5c20ddd28 | -15.36423 | -46.11056 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70a2f3e4-c54c-3f80-aabf-d8bd389f7d44 | -15.16956 | -49.08495 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 75dd6211-6df7-3217-841e-a574aa401eba | -14.18398 | -46.11304 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README57.md)
