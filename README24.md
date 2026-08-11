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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae7b681c-6d60-390f-99e5-56c8aa089d00 | -10.73632 | -50.45067 | 2026-08-11 05:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c183606a-319e-3ea2-86f9-9add3b6e98cb | -13.57673 | -46.26735 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5f667edd-313f-349e-bd9e-5e72e6e0926e | -13.61006 | -46.31572 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 437b776e-e5ff-31f3-99f1-14bffc19a7a4 | -11.45515 | -46.67514 | 2026-08-11 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6d8398af-5705-319e-9f84-a171cbd48115 | -10.73778 | -50.45242 | 2026-08-11 05:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 31ee3d89-0f51-3eff-b575-c0f887bd6900 | -8.64001 | -45.85558 | 2026-08-11 05:10:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63125d2b-c965-39c0-9c37-3b60a1393caa | -8.94685 | -60.50757 | 2026-08-11 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15ae840b-e4e4-39f9-b55e-83386fb1d0b9 | -11.22588 | -54.82765 | 2026-08-11 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0401ba92-c04c-3b1b-b710-6f8f445ae395 | -12.45529 | -45.3148 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 652f8960-73b8-302b-9ccf-10500d40f486 | -12.32295 | -54.11934 | 2026-08-11 05:10:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b5f2f4f-5c4c-3942-8da0-c54f2512a3d4 | -10.73061 | -50.43378 | 2026-08-11 05:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 22264ef0-63d4-31d7-8c89-f64cdb86914b | -12.47974 | -45.31004 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c5c859b4-7cd0-35c9-ba5c-4ac1fb3e588d | -8.24066 | -46.24306 | 2026-08-11 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17246203-90b5-30f9-b17e-ba34495900a3 | -9.14907 | -50.90093 | 2026-08-11 05:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf4a1926-2fc1-3860-9671-c594794c0775 | -13.57629 | -46.27101 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6d0b22c9-d3e9-34f6-9ef0-5851eda4cbb2 | -13.43523 | -57.03715 | 2026-08-11 05:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da94c7f5-1889-3479-8eae-be834800e98d | -14.48157 | -47.98266 | 2026-08-11 05:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 645b321e-6d34-310e-9379-3643ada617ac | -17.13257 | -51.68674 | 2026-08-11 05:12:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5795fde-a08c-3d65-a7bf-d1d63efdc77a | -14.31682 | -54.92621 | 2026-08-11 05:12:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 14a00775-f8c3-34f1-aea0-d5daecd93036 | -15.00551 | -46.59036 | 2026-08-11 05:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de0a4c23-ef9f-3094-8d76-a36b104b50ce | -14.6136 | -47.65894 | 2026-08-11 05:12:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d34e8ece-b003-36c0-84b0-d8f42d806fd2 | -14.45596 | -45.68826 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b009df3f-e2e2-3a4e-bd9b-949bc6c65a82 | -18.02854 | -44.40592 | 2026-08-11 05:12:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 63635a12-88b7-3219-a4c6-183c1e971f79 | -17.56786 | -47.50249 | 2026-08-11 05:12:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3da38c52-0172-3cf6-88d7-300f62fbc07d | -18.01961 | -44.43191 | 2026-08-11 05:12:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| af35e5d3-90e6-36fe-8802-9eebb2da9da6 | -17.9993 | -44.3718 | 2026-08-11 05:12:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 73a59a72-fb96-3535-9ad8-21daa619035f | -14.27872 | -45.30331 | 2026-08-11 05:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0fbd6c6-464d-3799-b82b-28a871528b67 | -14.73351 | -56.35363 | 2026-08-11 05:12:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f572fae3-d88b-3e4b-bd98-6ca57e92f720 | -14.2746 | -45.31151 | 2026-08-11 05:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 286a8b74-61e8-3fa7-8452-0b93240b22b3 | -15.01138 | -46.58786 | 2026-08-11 05:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| feb72e4f-a91c-3f4c-a08a-d411a2051810 | -17.04073 | -45.89691 | 2026-08-11 05:12:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ffff70d-cd51-35b4-8113-c488980dca2e | -14.31064 | -54.92146 | 2026-08-11 05:12:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5056fc59-4643-3973-8863-001941d67e23 | -17.13283 | -51.65313 | 2026-08-11 05:12:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52e139f4-ab8f-32cd-8ad4-066f30f03685 | -15.011 | -46.59122 | 2026-08-11 05:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 44615ed9-4af0-3464-82aa-f87f2ddd659e | -14.28149 | -45.30346 | 2026-08-11 05:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d193420-d4d2-3a50-a811-206e6a8cd823 | -17.44274 | -51.61781 | 2026-08-11 05:12:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9352329f-21c4-3c65-a655-432d116ce3a0 | -18.02599 | -44.43824 | 2026-08-11 05:12:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1aad1c99-b3a5-3b04-b59c-04f5678b7491 | -14.61828 | -47.66298 | 2026-08-11 05:12:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 00223447-cbff-3b73-9e9c-5677ece86318 | -15.04066 | -46.57645 | 2026-08-11 05:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5297695-954d-3510-8bb6-ae1c00ed49ad | -14.73019 | -56.35308 | 2026-08-11 05:12:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 079f4b0f-50a4-314b-811d-925e78ab37a3 | -15.00051 | -46.58519 | 2026-08-11 05:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c7fc880-3439-314d-b21e-bdc98c76c258 | -13.87426 | -53.77316 | 2026-08-11 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0532dfc4-45d8-3e38-a363-d10315263e8f | -14.45642 | -45.68407 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eba87eab-e432-34d0-8a3d-f5549bb0fefb | -13.43464 | -57.04076 | 2026-08-11 05:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 207c6ee5-566a-3875-8f72-8f1c091ed0e5 | -13.87078 | -53.77264 | 2026-08-11 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b519d5b-3d46-3420-b357-76489150a4fc | -14.1279 | -45.63424 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 278ce928-cc6e-36e5-a048-e3c79426cc4b | -18.5075 | -51.66579 | 2026-08-11 05:12:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 14fc91ae-74d2-3ca7-be24-5148af93630e | -18.01997 | -44.43229 | 2026-08-11 05:12:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3be3576e-8d6e-366e-b404-e85e9e3be362 | -18.39597 | -55.54827 | 2026-08-11 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 21c3e123-4dc7-3aec-9d99-773311cd96b7 | -14.12167 | -45.6374 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8b91daac-cd50-37fd-99d5-5563986e6b59 | -14.48236 | -47.9793 | 2026-08-11 05:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3d014c7a-0f6f-3d83-bd49-91493b9d8bbd | -18.42163 | -45.50137 | 2026-08-11 05:12:00 | NPP-375D | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ce5707bb-c372-3dea-a9d2-f3d9e70a0a31 | -13.64164 | -57.92699 | 2026-08-11 05:12:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| dc5f29c6-edc1-3f59-91b3-e1f15885517c | -14.47288 | -45.6946 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96f01758-015f-3b9f-bb50-d79cecc4396d | -15.55145 | -49.96233 | 2026-08-11 05:12:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e03b39e9-857f-3004-8994-76ce47baa7f1 | -17.0403 | -45.90119 | 2026-08-11 05:12:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8629682a-57b1-3d16-82f2-4c7008499ca0 | -15.76914 | -46.78901 | 2026-08-11 05:12:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6ed7ec61-07b8-34ed-a14e-b2c5d8b9cf01 | -14.62056 | -47.66329 | 2026-08-11 05:12:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 35914150-153c-3990-9b87-f635dc7394fd | -14.62132 | -47.65685 | 2026-08-11 05:12:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3d0dca69-74bd-31fc-91cd-c7a0d82cf9fd | -14.48228 | -47.97705 | 2026-08-11 05:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0b26fec9-107a-3f61-b0d5-abdc4649a05d | -14.27718 | -45.31641 | 2026-08-11 05:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 774ed861-0db0-3a61-ab9d-5588baf13cab | -14.99363 | -46.59656 | 2026-08-11 05:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3413fccc-67b8-3cbc-8f24-4080cbde6a35 | -17.14087 | -51.65476 | 2026-08-11 05:12:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15f66bf2-95fa-30e2-b5cf-c2be5b80a935 | -15.04027 | -46.57976 | 2026-08-11 05:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8251ce58-ce70-3f7c-93b7-523d50b5e862 | -15.0343 | -46.58302 | 2026-08-11 05:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 803b8e6f-53dc-3937-827e-f152ba86fddb | -16.66024 | -43.63549 | 2026-08-11 05:12:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 06814fa8-ab41-30a0-a363-3414170c3985 | -13.93448 | -58.10202 | 2026-08-11 05:12:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2e8754e-b74d-3345-b50f-46304f6e0340 | -14.9988 | -46.60019 | 2026-08-11 05:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8851f51-275a-344e-bec9-a8929a23dd32 | -13.86725 | -53.79624 | 2026-08-11 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ddfcd30d-c4c7-3512-a3d4-25dbb6173df9 | -18.02909 | -44.3997 | 2026-08-11 05:12:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 165e238f-58b2-3539-8c27-707d8d6ee9d1 | -13.8742 | -53.79733 | 2026-08-11 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3b3e289c-1090-334f-a128-abd8fd4f41c7 | -14.31008 | -54.92513 | 2026-08-11 05:12:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d08b56d6-55ea-399d-b219-67c0c4798f73 | -14.61908 | -47.65657 | 2026-08-11 05:12:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5a59940-bd4a-335c-a68b-1b3a1036d985 | -14.99956 | -46.59351 | 2026-08-11 05:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6e9d575-8de9-376c-8e0b-be006c5cec41 | -16.48612 | -54.65979 | 2026-08-11 05:12:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8d0c345b-e36d-39af-a90b-06b99c408d75 | -18.49156 | -51.67219 | 2026-08-11 05:12:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88835a00-f897-3b83-80aa-ebabe8dc39e5 | -13.43346 | -57.048 | 2026-08-11 05:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2d1aba2f-9ea9-3d55-9c84-c492a8310202 | -13.87132 | -53.79284 | 2026-08-11 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 94520f95-cc5f-34f1-9b55-0260c079202e | -14.46708 | -45.69386 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 149e68d9-0d33-347f-a911-de726e1f7ef7 | -18.42878 | -45.49197 | 2026-08-11 05:12:00 | NPP-375D | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e12fc332-66ef-3321-b154-b337abaea353 | -14.12151 | -45.63586 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7b7de9c4-dac4-32d3-b9a2-1c199f9a4f00 | -14.28465 | -45.304 | 2026-08-11 05:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21eddea1-aa45-3366-b698-b83467f728a5 | -14.45988 | -45.70568 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a6a3c29-5d5e-372f-b99d-7edc19d275b5 | -14.62415 | -47.65742 | 2026-08-11 05:12:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed6933a4-6388-3573-ab1a-a2d6647e8baa | -14.27556 | -45.30273 | 2026-08-11 05:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f089223-5b40-30dd-a8a3-f6b30e3d50aa | -14.46129 | -45.69315 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 556d5023-6a65-3f1b-b329-a6da0eadd637 | -13.86606 | -53.80417 | 2026-08-11 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2ed30ce9-1c4c-37dc-bc4e-c4a023117680 | -18.01944 | -44.43779 | 2026-08-11 05:12:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96c9ffde-d0ff-3b53-bf3d-485047a83a7f | -17.13585 | -51.66163 | 2026-08-11 05:12:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7ad4a49b-a499-37d1-8d20-51733d187857 | -14.28052 | -45.31225 | 2026-08-11 05:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e137b58-78b7-3544-aa69-226f6a6d83e7 | -17.03649 | -45.89716 | 2026-08-11 05:12:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6222607-8d8a-3ef4-9f27-25932ed2638b | -14.61283 | -47.66515 | 2026-08-11 05:12:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5b93b1b3-50fd-3050-a74f-ec99d7e13991 | -14.63111 | -47.66176 | 2026-08-11 05:12:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54a11991-a6ff-3973-af0e-661ec1532da5 | -15.06952 | -52.69225 | 2026-08-11 05:12:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7950a30b-a439-34e2-831a-67f1847c230c | -18.49105 | -51.67605 | 2026-08-11 05:12:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09119905-b007-33f9-92a3-48e32c13b8c8 | -17.57321 | -47.5032 | 2026-08-11 05:12:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1a4e5114-0076-3961-9757-5abb57572935 | -17.13685 | -51.65394 | 2026-08-11 05:12:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3facbd55-6ec0-3b2a-9406-236b054a5e7e | -14.45455 | -45.70081 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e18f1de0-ee6c-3403-8742-1965380d114d | -14.45092 | -45.6855 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f2829d7-406b-3555-a266-8a79eae0de39 | -14.45109 | -45.67918 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README25.md)
