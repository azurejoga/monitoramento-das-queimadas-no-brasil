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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13be8e79-132d-3983-8219-3d3f601a8b12 | -12.04716 | -45.84106 | 2025-07-27 03:47:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 872c67be-621b-3dd6-a942-121835984b0b | -16.26197 | -47.81854 | 2025-07-27 03:47:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 411eac2a-fc44-35fc-9599-0fc27912d84a | -12.04783 | -45.83763 | 2025-07-27 03:47:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b7b173f-0fce-3f90-9469-ca0a8f472184 | -12.67692 | -47.0202 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8cf4665e-7997-3272-88e8-50a2381bd8c3 | -13.05312 | -44.07362 | 2025-07-27 03:47:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0fd75057-8db4-3380-9560-9c47924bd4eb | -12.71871 | -46.26645 | 2025-07-27 03:47:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a8a4cf55-1800-3536-9666-e888e16a973c | -11.96437 | -46.71525 | 2025-07-27 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17baafff-428f-3d41-b383-39ea19c15969 | -13.72395 | -45.68626 | 2025-07-27 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 227a03b9-da72-3cfa-8adf-4abf1002e686 | -12.71597 | -47.00294 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0dc5561c-33ab-3bde-98a7-4c48e04912fa | -13.11966 | -47.35136 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9c86f53-f38a-3773-b0e9-e2df0891c460 | -17.21092 | -44.84892 | 2025-07-27 03:47:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb5de649-cf5a-3673-ae99-8a1c93087d95 | -12.0043 | -45.83262 | 2025-07-27 03:47:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0cbd430-d8f7-31a2-b910-1508c429386c | -13.10052 | -47.32655 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60b3a0f1-52af-3801-a79b-35989273b795 | -12.7103 | -47.00162 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9e066e18-dcf8-3aee-ad18-abeba19e1cc5 | -13.48858 | -45.50291 | 2025-07-27 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c344ce69-4eaf-300a-868b-ef74546224e0 | -13.13685 | -47.32529 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3e60a0a3-6c86-31d7-832a-ea6a1e916ccd | -14.21987 | -43.95227 | 2025-07-27 03:47:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| acdb5a32-3638-31a8-a84c-f31ecd70d4c9 | -13.13341 | -47.33866 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6fadf177-2ec9-3072-a243-88ec0d923cd0 | -16.8089 | -49.22699 | 2025-07-27 03:47:00 | NPP-375D | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d782cef2-a7fc-3df5-afec-fda8aa931085 | -11.9664 | -46.71127 | 2025-07-27 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1f4f25e7-53f1-3b61-b580-429d67ac1a01 | -13.13422 | -47.33472 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e8811a08-571a-3dca-a0c3-0c573cd19163 | -13.04844 | -44.07267 | 2025-07-27 03:47:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ac9bb16-88a7-347d-b137-20c4f51d5b28 | -22.43646 | -46.90873 | 2025-07-27 03:47:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5f1c617-5c90-3a7e-a1d1-c86f6f523425 | -14.2155 | -43.94823 | 2025-07-27 03:47:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f929faaa-cb66-300e-a5af-146545b9f1ba | -12.00718 | -45.83322 | 2025-07-27 03:47:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60019359-13f0-397b-9b58-9de6a4500260 | -12.68021 | -47.00375 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bd557c58-5ad1-3ef6-b83c-9e4442dc98b7 | -17.85259 | -40.97145 | 2025-07-27 03:47:00 | NPP-375D | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 54aa9af2-7776-3b30-b33a-47d3f6053202 | -13.71945 | -45.68188 | 2025-07-27 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| accb0955-2181-31ca-aa1a-3065f1d7393b | -12.04114 | -45.84342 | 2025-07-27 03:47:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0464f712-267e-3348-a7ed-bb757a7f1bc9 | -12.68259 | -47.02153 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c268adf0-8189-390c-b6fb-a8ab1b4a93e8 | -13.11883 | -47.35556 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d8cbb65-23de-365f-a0df-fe226a70a12a | -15.18655 | -43.27848 | 2025-07-27 03:47:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 9e9f7365-aac1-3b4d-8528-db230e3c8fe1 | -12.00652 | -45.83668 | 2025-07-27 03:47:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 217a985a-739c-3377-ac53-7092c70376f0 | -12.00117 | -45.83558 | 2025-07-27 03:47:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4560055d-4631-32ce-957c-c8578b814e69 | -12.712 | -45.0307 | 2025-07-27 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4833a81b-27e0-3d72-98dc-3913281aa9e8 | -13.05406 | -44.06861 | 2025-07-27 03:47:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de998092-fc73-3650-bfdf-e25e64ac3cf7 | -12.04047 | -45.84686 | 2025-07-27 03:47:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 648398b0-fd33-3f8e-bc7e-21ad45acd84e | -12.67744 | -46.98803 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2e018d66-cb94-394f-987a-71b355a992a3 | -9.91987 | -48.90315 | 2025-07-27 03:47:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 199e0410-4520-3edb-bf0d-36f0d031ac56 | -13.12451 | -47.35733 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39740e15-5af3-3766-9e45-adeeb6ab20d2 | -14.02387 | -44.61255 | 2025-07-27 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa4744b0-9bc6-30d3-8930-c578948bdf82 | -12.0398 | -45.85031 | 2025-07-27 03:47:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b9290699-e135-3d68-9404-dcd0e96b5c81 | -13.53316 | -45.52834 | 2025-07-27 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9126287-423f-3855-9b16-1b9bcf310c08 | -16.80337 | -49.22411 | 2025-07-27 03:47:00 | NPP-375D | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1038921c-aaba-3669-9a88-592946e4d082 | -13.11928 | -47.34889 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 174de2cf-d09d-32eb-bc8a-4969833ebde2 | -13.08578 | -47.34021 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4c7635e4-944c-3831-88c2-6f7823179eca | -10.84075 | -46.68784 | 2025-07-27 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c751981a-fe4d-38e1-ab57-cefda53a777e | -10.84735 | -46.6847 | 2025-07-27 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80128947-7da0-3149-a086-18a347c8629f | -15.1873 | -43.27438 | 2025-07-27 03:47:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4c2766c6-8c77-3f04-9697-3f68d11a7550 | -13.09273 | -47.33552 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c9dd39fe-f81f-31f7-bd74-143e7185e4e5 | -15.99164 | -42.6528 | 2025-07-27 03:47:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 39f964b1-ed83-3bf7-9e89-a3a39f605d04 | -11.112 | -45.11997 | 2025-07-27 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4155415e-4410-3493-9e4b-be7e73c8aa8d | -12.68908 | -47.01879 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 924cb1bc-df26-3f54-a63c-cc68a8bdc854 | -12.68328 | -46.98844 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f18108b0-4570-3da0-b7c6-8c186b6e82aa | -13.72335 | -45.68934 | 2025-07-27 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2c53910-7e8d-3bb2-ae82-07f74d5ba789 | -14.2162 | -43.94661 | 2025-07-27 03:47:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f56fc28f-0a4f-38ce-bade-251869be7fd0 | -13.1226 | -47.36705 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 70e06e08-3ce9-31f7-8fab-546152b27e37 | -13.72065 | -45.67571 | 2025-07-27 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7cb0f0fe-b259-325b-b0e6-6a892981e0bd | -12.70841 | -47.01118 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6a67233e-afd9-3ccb-ab39-38cdf536b8de | -13.13446 | -47.33744 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d7569c8d-c219-3750-9fe5-4257dddc4a8f | -9.92215 | -48.90435 | 2025-07-27 03:47:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4d8d6e74-7974-332a-82ca-3471092d7959 | -13.14046 | -47.33363 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 7fdb866f-eb6c-3dac-af6f-57f942f05390 | -13.49862 | -45.51488 | 2025-07-27 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f10d6e0-aa6b-3902-bafe-341a5d71efaf | -17.21453 | -44.85475 | 2025-07-27 03:47:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ecdcd4b7-d887-39d3-b17e-b8d49ee0d2d5 | -9.81718 | -47.75678 | 2025-07-27 03:47:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4804f2b-713c-336c-b8a8-4c4fef2994b8 | -13.11845 | -47.35295 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e2440eb-4bf9-3b64-bb50-66770864b28f | -13.71554 | -45.67455 | 2025-07-27 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 84011321-3ec0-34b2-9bb3-e65145575b58 | -10.51789 | -42.55487 | 2025-07-27 03:47:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 2dffdc55-a8bc-38cd-91f4-4ab11727a2c5 | -16.26034 | -47.8162 | 2025-07-27 03:47:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f57d8fc3-dc38-3354-a68a-dec2a4434e9f | -12.67857 | -47.01194 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b66dc506-08f7-30f2-a057-4058cb45df39 | -23.07033 | -49.67305 | 2025-07-27 03:47:00 | NPP-375D | IPAUSSU | SÃO PAULO | Brasil | 3520905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| bae63c8c-3422-39e8-98ed-596d36cdb6c3 | -16.40429 | -48.9257 | 2025-07-27 03:47:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 14dc0382-7e18-3ee2-a978-f3b82391a1d7 | -10.85316 | -46.68568 | 2025-07-27 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8d3941fd-48ad-3ad1-a9e1-d8a629a12282 | -15.99234 | -42.64898 | 2025-07-27 03:47:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0b413504-189f-397f-b078-a4862ef050c1 | -13.09431 | -47.32758 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24b659c5-1353-3efd-9d84-80279a3ef91f | -16.80995 | -49.22226 | 2025-07-27 03:47:00 | NPP-375D | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 314a2df3-9996-316c-97a4-d63629be7032 | -17.04279 | -43.77067 | 2025-07-27 03:47:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4f970d27-43f7-36f0-83fc-201ad15331cd | -12.70654 | -46.2708 | 2025-07-27 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78e7e2a7-6bc1-3d2b-a1db-bb1980a6eeb8 | -13.14132 | -47.32941 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 8ef1713c-15ac-3deb-9efb-b0d22687aa06 | -11.16957 | -43.41992 | 2025-07-27 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f2f388e-e276-3bc5-8f8f-ffeea721a417 | -13.12236 | -47.36327 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9865beb0-5efb-3c17-a20c-755967744aaf | -13.10733 | -47.32256 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 751133b7-c603-39f7-a33b-ec6fa2c5a455 | -16.26521 | -47.82102 | 2025-07-27 03:47:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 369c05c0-dc44-341d-99af-9195cd2be694 | -20.70256 | -46.29615 | 2025-07-27 03:47:00 | NPP-375D | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e70c4d4f-2c71-305e-90c7-368decf92f09 | -12.70747 | -47.01591 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 62691776-2360-3fe6-8200-4a86b894c73e | -13.13503 | -47.33078 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8e3202f3-b109-3b29-a387-f36951646c7d | -17.04706 | -43.77156 | 2025-07-27 03:47:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0961ea72-f899-3087-8529-206e119b6346 | -15.04006 | -49.25249 | 2025-07-27 03:47:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58843ee7-c4cc-3f83-833a-afd2c34c0776 | -13.08659 | -47.33614 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e5130df0-666f-36c9-b2b5-248f897712c2 | -12.0465 | -45.8445 | 2025-07-27 03:47:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5671dba6-6cd8-3c47-8462-20f90650d29a | -17.85335 | -40.96708 | 2025-07-27 03:47:00 | NPP-375D | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bb9fb257-8ae8-3c3f-9235-aeaf4d79f540 | -12.71018 | -46.28102 | 2025-07-27 03:47:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7ec4a285-42be-3439-b407-90294385bda9 | -13.72006 | -45.67878 | 2025-07-27 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 224b82c2-cf65-38e2-9212-63e8df8b0495 | -16.80945 | -49.22533 | 2025-07-27 03:47:00 | NPP-375D | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7319f393-9adb-357e-930f-27ad036d8350 | -13.49802 | -45.51798 | 2025-07-27 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f3f8de62-063b-35ed-9fb5-e79f678364b5 | -13.71614 | -45.67145 | 2025-07-27 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 426351a3-8711-3811-a2ba-c112b6a9297d | -17.24511 | -46.90898 | 2025-07-27 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8f00417-008f-351d-882e-a23b23fc6ed4 | -15.19082 | -43.27937 | 2025-07-27 03:47:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 0dd8afd6-6b73-3502-a505-0a21fabe210d | -13.71674 | -45.66836 | 2025-07-27 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3bb000d-ea02-3ca1-b8d3-febe0a1d066a | -26.02592 | -49.00928 | 2025-07-27 03:49:00 | NPP-375D | GARUVA | SANTA CATARINA | Brasil | 4205803 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |


[Clique aqui para ver as próximas entradas](README7.md)
