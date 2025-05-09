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
| 91c6180a-d28c-340d-8389-1b26803211ee | -8.0807 | -43.12147 | 2025-05-09 05:06:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 6983252e-75c2-3fd0-a95d-6cfc583138d1 | -11.56277 | -47.61201 | 2025-05-09 05:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 154f2357-9326-3f10-a474-584b101ea2e9 | -8.07381 | -43.1206 | 2025-05-09 05:06:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 42.2 |
| 7fef67f9-879b-3d67-b332-9d8e353e821d | -11.56189 | -47.61886 | 2025-05-09 05:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6a09f511-1ca9-3587-89ca-30175a3acc6b | -11.91076 | -54.40287 | 2025-05-09 05:06:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49140bc3-d2c9-34e8-819b-b871c6df0f6e | -11.77868 | -48.2012 | 2025-05-09 05:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3490b5ae-0237-3416-bb6d-434fbaaadfa1 | -10.97429 | -44.44094 | 2025-05-09 05:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 540793ae-4a42-31c0-b05d-6ed5a530cc35 | -11.6247 | -54.93859 | 2025-05-09 05:06:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51a1312f-fdd4-3e73-b8a8-9732f6c5c87a | -7.89858 | -61.52232 | 2025-05-09 05:06:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 111fd486-e07a-3327-9695-53b34f91e116 | -11.53536 | -54.36077 | 2025-05-09 05:06:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0cb8c0c-f21f-3d74-9175-93ea885f1d63 | -10.67509 | -44.37754 | 2025-05-09 05:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3ffd18b7-49be-373e-b6f8-34f7ddb848f4 | -11.38439 | -52.93945 | 2025-05-09 05:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 84f7677b-e614-3b8f-b23c-029b4acb6ab8 | -10.97569 | -44.44102 | 2025-05-09 05:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a4377a6b-41c5-378d-b635-253341c43f6f | -11.38799 | -52.93708 | 2025-05-09 05:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d72ed92b-f2d6-3865-99ca-786847e9ac33 | -10.66778 | -44.38273 | 2025-05-09 05:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 1f90498c-ba5d-3d5b-abde-699e8c00ada9 | -10.66847 | -44.37699 | 2025-05-09 05:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3ce6181e-e01c-3809-b0fe-f78a73b4d7c9 | -11.40567 | -52.94924 | 2025-05-09 05:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 7bc50db6-1b4b-3537-b42a-def6ca3cd315 | -11.3816 | -55.11586 | 2025-05-09 05:06:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 215cc7a4-598f-3e1d-a646-46c3d4cd0020 | -11.39939 | -52.93875 | 2025-05-09 05:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 659cdb0e-6a25-381c-b2b4-a9164b0d764c | -10.66617 | -44.3778 | 2025-05-09 05:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| c1cc498b-c91a-3086-b6cb-4ff3f02f45d5 | -11.56302 | -47.61799 | 2025-05-09 05:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5085d184-cbe6-38ff-9445-81538bf57236 | -8.07301 | -43.12687 | 2025-05-09 05:06:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 34.0 |
| 8c3ab2dd-3a71-34b2-8424-8ebbb55e8024 | -8.07989 | -43.12774 | 2025-05-09 05:06:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 1b654360-c6d8-32bf-bdde-6b0331681a6b | -11.91431 | -54.40342 | 2025-05-09 05:06:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38081fb3-f177-39e9-9348-d0b3c64fe1ef | -12.35852 | -52.48746 | 2025-05-09 05:06:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a68e1b96-104b-329d-8049-d5cbc31f2682 | -11.40186 | -52.9487 | 2025-05-09 05:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d53f0e9b-36c3-3a31-891b-0856e6573156 | -11.38733 | -52.94178 | 2025-05-09 05:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 3ad39eb6-7147-3d33-ba67-a8bdc4609dd3 | -8.91113 | -50.01305 | 2025-05-09 05:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a80ecde-a450-3239-a8a2-3d709e90b9c0 | -11.39426 | -52.9476 | 2025-05-09 05:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 366e68b8-a0fa-3820-928e-2eb9b49dac58 | -11.56345 | -47.61452 | 2025-05-09 05:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 54629cd4-009c-3758-b1bc-526086e71897 | -11.77345 | -48.20047 | 2025-05-09 05:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ea0369f-1d18-3ef3-8f00-5f513d1535af | -11.38503 | -55.11639 | 2025-05-09 05:06:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc54c4b6-2328-3ff9-8a3e-8f9805658ef0 | -10.97637 | -44.43534 | 2025-05-09 05:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dc3bc492-7406-3b65-9ac4-83e95cb11777 | -10.48683 | -59.1516 | 2025-05-09 05:06:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 994300a2-0301-32a7-8b3c-5a7e3fd8d03f | -10.67276 | -44.37865 | 2025-05-09 05:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| d33a5300-66cd-37c9-85a1-4f19a296120f | -12.35456 | -52.48689 | 2025-05-09 05:06:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 140af9f8-b2d8-33bb-93f0-59955c3c8cb2 | -11.56819 | -47.61275 | 2025-05-09 05:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd83d191-4e3b-3afb-a060-6e656702df1c | -11.39046 | -52.94704 | 2025-05-09 05:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0aeac5cc-e2f3-329c-9d80-985c5831bacc | -11.56385 | -47.61118 | 2025-05-09 05:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 26fdad47-1f9d-3a7e-9015-9d1776ff94f2 | -10.9691 | -44.44026 | 2025-05-09 05:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff4a6768-5c20-3788-93b5-cb8bdea6b435 | -11.55802 | -47.6138 | 2025-05-09 05:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| df692184-d8fd-38cd-a51e-a7b76b6a5c78 | -13.36468 | -54.25757 | 2025-05-09 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd3204aa-9af3-3990-a6a7-f240f01b45fd | -12.17426 | -54.24219 | 2025-05-09 05:08:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 06e6d59d-39ae-3c7b-b875-20c44f3628d4 | -13.80895 | -52.24226 | 2025-05-09 05:08:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b00a88ca-4567-3ecb-8e52-2568d31067a2 | -12.64507 | -54.06821 | 2025-05-09 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b33c088d-0814-3962-b98d-b06f7b2eccaa | -12.33266 | -55.16095 | 2025-05-09 05:08:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1afecd2-b012-3b5d-92ce-3db411fcd47c | -15.36615 | -60.17013 | 2025-05-09 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3fcad9ba-e9e8-3097-9848-39dff35371a2 | -14.64073 | -45.13182 | 2025-05-09 05:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f6b6fef2-884e-3aac-a186-82a1a9b0c135 | -15.36896 | -60.17466 | 2025-05-09 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4f2b92de-e9c9-37e1-9144-562023e2f00b | -13.37253 | -54.25447 | 2025-05-09 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f781b99-3062-3cbf-a166-12118fa1f3d5 | -19.1572 | -47.81603 | 2025-05-09 05:08:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c72a85f6-b2cb-3032-b7f9-c9da078337c6 | -18.37388 | -55.71807 | 2025-05-09 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 0793630e-7ca1-3b6e-a94b-7de837dd0587 | -12.62995 | -54.07018 | 2025-05-09 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb8a860a-b517-35b4-abd2-32cfb50691a9 | -15.36267 | -60.16951 | 2025-05-09 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6f39f226-6717-3427-85ab-803a7c0b3535 | -13.37554 | -54.25927 | 2025-05-09 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 23fd56c3-c055-3cbc-a760-c4514cc01d3c | -13.36891 | -54.2539 | 2025-05-09 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23d330b6-89ad-38b0-9501-ff19b89206af | -14.64132 | -45.12611 | 2025-05-09 05:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d71baa28-a755-351f-9d1d-5cdc8655e9a1 | -19.845 | -54.22292 | 2025-05-09 05:08:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 03c2641a-ef3a-3946-b90a-963a8d71fff2 | -13.05543 | -53.72344 | 2025-05-09 05:08:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d1da333-670a-39eb-990c-1534343702c1 | -13.37676 | -54.2508 | 2025-05-09 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e63fadc9-c8c3-3723-bac2-6355db35211e | -12.17128 | -54.23749 | 2025-05-09 05:08:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa047a4a-901d-304f-b6ce-1664367a8b6d | -17.52996 | -52.12077 | 2025-05-09 05:08:00 | NPP-375D | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0532a72f-ced8-3fd0-a06f-5f2a16ff38f6 | -14.22578 | -45.46976 | 2025-05-09 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 85383342-9aeb-363a-bbaa-72ae9f9945b4 | -14.30644 | -54.65413 | 2025-05-09 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21019789-e6ed-3ef6-84bb-45bf918d4e3a | -12.17188 | -54.23332 | 2025-05-09 05:08:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 72cb3cc7-88ae-34bc-9aa2-f79be7947533 | -13.03992 | -53.7258 | 2025-05-09 05:08:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bcb821c4-0c7f-3906-b4ef-da3a018f8a9f | -14.2199 | -45.46361 | 2025-05-09 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bdc3eab7-a723-3ded-aff5-3d8fef2f0f21 | -15.07691 | -48.94458 | 2025-05-09 05:08:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f87dedd-2b1f-3e84-8576-7dd2d152e505 | -14.22431 | -45.47205 | 2025-05-09 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4ff1a34c-34f2-3eeb-8ccb-9c0166474922 | -12.63358 | -54.07075 | 2025-05-09 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b2c400e-d087-3e22-b2c7-9512577a2673 | -15.25382 | -47.46772 | 2025-05-09 05:08:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c47292c-2970-327f-9410-7fc1dca21f7e | -13.37494 | -54.2635 | 2025-05-09 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2fc42b8a-ff7c-310a-90d4-7d0fb00b7c75 | -14.21788 | -45.47128 | 2025-05-09 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f000eb7e-cb40-3b60-9b5f-cf8d9b1c2003 | -19.33245 | -56.89463 | 2025-05-09 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| ae6bc0b0-1a96-31be-880a-10e569572b7a | -17.23095 | -47.38639 | 2025-05-09 05:08:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 81557882-6c85-3075-a47c-bd2d610e4eab | -13.2465 | -48.4079 | 2025-05-09 05:08:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76b3eb1e-26a6-3282-b777-a19049a3717b | -13.05236 | -53.71842 | 2025-05-09 05:08:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a07e61c8-b359-3b90-86db-4bda06c7a6aa | -12.32864 | -55.1642 | 2025-05-09 05:08:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0e6490e-6935-3f79-8deb-62e90977fc48 | -16.38268 | -54.57561 | 2025-05-09 05:08:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b2f11aa-4f33-3240-a765-0858d541ad19 | -13.04056 | -53.72132 | 2025-05-09 05:08:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5a4e9f6-39f0-35da-b2d6-a63bc3c2f093 | -20.05841 | -49.36645 | 2025-05-09 05:08:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2f49f60a-3de0-37ea-bc1d-fc7e4bc20ab1 | -13.04364 | -53.72634 | 2025-05-09 05:08:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 663c3c1f-f4b3-3e41-86d0-54a135186102 | -13.37856 | -54.26405 | 2025-05-09 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6521786f-4ad9-3afc-b2a4-bfd94aa84771 | -13.04864 | -53.7179 | 2025-05-09 05:08:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 299fd18a-103e-3b26-938a-803e2a0d229d | -14.20619 | -45.45903 | 2025-05-09 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 31a6ec74-d063-3541-8668-b5169cf8755d | -14.20561 | -45.46437 | 2025-05-09 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2fdab05f-1540-3498-bff9-5d8a44930810 | -12.50534 | -55.19004 | 2025-05-09 05:08:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d1d3763b-a6d4-3573-a7ea-b2e746a9678e | -13.05107 | -53.72739 | 2025-05-09 05:08:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34f18453-9d0f-36ba-aae1-7a2d2c805162 | -20.06038 | -49.36188 | 2025-05-09 05:08:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 899bc851-8655-3e79-978a-9a501be25535 | -13.04428 | -53.72186 | 2025-05-09 05:08:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b7cb75e0-ce08-3dde-9eee-42cce201595b | -11.65933 | -58.26431 | 2025-05-09 05:08:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6ccb5fd7-a411-3fd5-b362-1045f6bb10db | -13.04735 | -53.72687 | 2025-05-09 05:08:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ad209e2-8520-3e5c-b7ba-0b1a1d9eb6a3 | -19.15945 | -47.81703 | 2025-05-09 05:08:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 349064cc-bbcd-30d0-a600-be49736a40bf | -12.64144 | -54.06765 | 2025-05-09 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d84091b-1f38-3d31-be71-372fb4d738e6 | -14.22523 | -45.47512 | 2025-05-09 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c3ef503a-d106-3ae6-bef9-a02a3ab557af | -14.21935 | -45.46897 | 2025-05-09 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1a90af29-418e-3817-a7cb-d6b5a00f22ff | -14.2249 | -45.46671 | 2025-05-09 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52a33531-bc5d-3610-84eb-bfa743a32d88 | -14.21881 | -45.47431 | 2025-05-09 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6f82696c-6e24-318b-a71f-12cbcd0658a5 | -12.64205 | -54.06342 | 2025-05-09 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2d43028-572d-3c39-bed1-93d86d279f07 | -14.64672 | -45.13831 | 2025-05-09 05:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README10.md)
