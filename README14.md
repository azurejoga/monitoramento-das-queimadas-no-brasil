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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf60e9c4-0018-355d-bf57-24eabc415d3c | -9.39104 | -57.52092 | 2025-07-01 05:14:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5dbf91f5-766a-315d-ae72-bfbe9e01a90a | -13.00944 | -53.41478 | 2025-07-01 05:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69c9c2c7-e6a2-3661-8b17-2ca08a2f8e4a | -11.57727 | -54.57208 | 2025-07-01 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48179fbf-52cd-3536-8a06-b8c42d41c731 | -9.25286 | -58.7549 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7461c2e-7b3e-3cd1-ac8d-3143a5ccdab7 | -10.29954 | -57.04672 | 2025-07-01 05:14:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90cf3c70-70ae-3028-9282-6292df1766a6 | -12.62639 | -54.21602 | 2025-07-01 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10c015ab-dc67-3d24-880f-12dcaa23e636 | -11.57912 | -54.56573 | 2025-07-01 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0328ef29-a7db-3fdc-a6ea-f192fb150e02 | -9.28528 | -56.24464 | 2025-07-01 05:14:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7517c7b7-e34a-310f-90bb-7b113ad2939a | -9.92824 | -59.93751 | 2025-07-01 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d844903-ca77-38cc-9491-71e9433cb2ca | -10.88214 | -56.44475 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 17d9abd9-9889-361b-8506-912f0f67c75e | -9.7054 | -56.18868 | 2025-07-01 05:14:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f7033337-af93-34ec-888d-3a599aa5f50d | -9.38771 | -57.52039 | 2025-07-01 05:14:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5945b734-9eca-3d1a-8862-c570a88d94f8 | -9.24953 | -58.75436 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f33fbd34-718b-3003-96b3-fb105e4e95e0 | -10.87601 | -56.44799 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cc2e7aa1-f947-3b0c-9f42-3641268e20cc | -12.62247 | -54.21543 | 2025-07-01 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4709a7e6-d008-3190-8321-83bb40e8ba25 | -9.24229 | -58.75682 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 136f1734-3596-3a29-b5f5-d72aa7a722d3 | -9.24178 | -58.73865 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e460c900-2638-3369-adb3-1bf127fa94f8 | -11.6036 | -65.14464 | 2025-07-01 05:14:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1c92601-bc6a-3cbe-beb9-7f1d903c2ba6 | -9.96952 | -48.24121 | 2025-07-01 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fa13cc3d-1ffe-3cd7-b3dd-2f71c4ece132 | -11.83175 | -62.76838 | 2025-07-01 05:14:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee5e74ce-cbf9-30b7-b217-d63b777e7400 | -10.29738 | -57.12779 | 2025-07-01 05:14:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1dd5a7e9-3487-37ce-9472-14e06fe5fa5e | -12.01252 | -62.82774 | 2025-07-01 05:14:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b584873-053d-3417-8033-82687e5fa8a4 | -13.27337 | -45.09105 | 2025-07-01 05:14:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5363f731-6a76-3240-9609-dd63d958ed4d | -14.40198 | -51.57248 | 2025-07-01 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa8c368f-5112-32db-9af4-9e4613a5e2ec | -10.87927 | -56.44042 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d776c063-83c5-3699-b0dc-e349266b6505 | -10.87643 | -53.77353 | 2025-07-01 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1295708-6c24-31f8-90fb-39efacf88e0c | -10.88902 | -56.44581 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0c94f2a7-5b2b-30ee-bd77-6837f023373f | -12.02339 | -47.77345 | 2025-07-01 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 756b51cb-2f74-3f63-ae5c-b3bf48d48f0c | -10.88502 | -56.44907 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f9fe7ee0-bcff-3061-95c9-b8594c77ca3d | -12.97168 | -54.68602 | 2025-07-01 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c7e9de8-37ed-34a3-b22b-c241b29eff21 | -9.24286 | -58.75329 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fc1fff8a-4bb4-30b7-abb9-e401848a4933 | -9.24399 | -58.74623 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03bc2a45-987e-3c36-97d1-925d1b90ec51 | -12.26722 | -54.53336 | 2025-07-01 05:14:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5420ca7f-6daf-389c-8501-a32c8bd0cb22 | -11.83273 | -47.50302 | 2025-07-01 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59a6ec38-8dce-36d6-9737-3c04fa3a30c3 | -10.67285 | -49.15259 | 2025-07-01 05:14:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5675944-7522-316b-be36-ceeca05c767d | -9.45975 | -57.83679 | 2025-07-01 05:14:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2107d16d-874a-3bdb-b6a7-1b0ded797ba9 | -9.70656 | -56.18116 | 2025-07-01 05:14:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| be260329-30d6-35b0-9f4b-019c4b4a07bf | -9.24727 | -58.76849 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2874f4c0-2962-398f-b6c9-0791484d76a3 | -9.97828 | -48.24134 | 2025-07-01 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 26a4bf34-6057-3242-9800-873363643219 | -9.24455 | -58.74271 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 404068b8-1e06-37a9-a674-32abdff2e127 | -9.28243 | -56.2404 | 2025-07-01 05:14:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af13ad47-d152-3974-9a42-60aba2818548 | -9.97366 | -48.23231 | 2025-07-01 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d72b0f5e-f9eb-3eae-8d61-32c2a41b249b | -11.07224 | -55.37861 | 2025-07-01 05:14:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a63dc608-d003-3370-a584-55d44fa37a34 | -10.54951 | -52.03844 | 2025-07-01 05:14:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e159eccd-3cb6-3289-85a6-7be47daafde2 | -10.87322 | -54.0469 | 2025-07-01 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 789d89e0-f0d9-3bc4-8795-25ba019abaa0 | -10.12771 | -52.34054 | 2025-07-01 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e2bf6b0-a343-39bc-800f-425cdc4d78e7 | -10.87257 | -56.44744 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| db8361e4-f402-34bc-aacc-3cdb84a55bc4 | -9.28514 | -56.24403 | 2025-07-01 05:14:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f90dfbf-6187-3dba-9af6-f8aaaed3a47d | -10.12224 | -57.77655 | 2025-07-01 05:14:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cead5e93-99e5-3ff1-8cd0-5c2f1340bc93 | -10.87283 | -53.74201 | 2025-07-01 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8d2322c-7a95-35af-958c-252c4e88f96a | -10.94824 | -55.31437 | 2025-07-01 05:14:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5fd4c06c-9b6d-33fa-85be-197232a5e9da | -10.87178 | -53.77801 | 2025-07-01 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a82b38f3-2478-379b-b396-96269ff7f718 | -10.08046 | -52.73785 | 2025-07-01 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f9b97b90-7b00-382b-948e-a33d9828b2c1 | -11.12479 | -55.44638 | 2025-07-01 05:14:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e28b0796-62df-37f7-aa5b-76a7935ebfd0 | -11.83218 | -47.5076 | 2025-07-01 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a11f88a-750e-3159-8695-0b8d2781db8c | -10.88323 | -53.75389 | 2025-07-01 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f856e4b-7c78-3380-8053-c2079f21c886 | -10.07992 | -52.74164 | 2025-07-01 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 12a708d6-5dcf-3d57-8fa8-8b413a6125f6 | -14.21007 | -45.51987 | 2025-07-01 05:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a28c861-b9af-3e44-af60-40d32773c5ce | -10.87583 | -56.43988 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9492405a-aa55-356b-bef3-94fda4383c26 | -13.00838 | -53.42241 | 2025-07-01 05:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3173a27e-a2bc-3eb8-8f8a-f4a091b52bf2 | -10.28179 | -52.83429 | 2025-07-01 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bee6ab58-0d5d-3a56-9bde-6f0e6eccd03f | -10.07885 | -52.74919 | 2025-07-01 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 247b9fd2-08cd-344b-9e43-9d772469bafa | -10.17215 | -51.65645 | 2025-07-01 05:14:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0733b247-33a4-3b97-934b-9ca6ce6ffc39 | -9.97566 | -48.23819 | 2025-07-01 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 9931dd98-3539-37c7-846a-360263810c92 | -9.2484 | -58.76142 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47a9ec57-1e28-35f0-b9b2-2230851e7abf | -9.25507 | -58.7625 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e897174c-62eb-3bd3-9a88-e21e7207ad8e | -9.70197 | -56.18814 | 2025-07-01 05:14:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0d5524c0-0ad7-348e-b3d8-0f8e7dcb946d | -12.62316 | -54.21041 | 2025-07-01 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5446afe1-29a0-3099-812d-21ba43214c74 | -9.24789 | -58.74325 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88f0c396-141e-3930-890f-f625d807084d | -10.8732 | -53.76795 | 2025-07-01 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40f7d885-d6e4-3d41-92eb-9cb1df52df03 | -12.97551 | -54.68658 | 2025-07-01 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a5de3d6-4981-32fd-a683-6f0a545277f1 | -9.35633 | -58.8512 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ebd621c6-67ef-3887-905e-0d7b5423f53d | -10.8787 | -56.44421 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9550a411-865f-3222-8be0-4240f10aa9af | -12.97934 | -54.68715 | 2025-07-01 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0013f6d6-e26e-3bf4-9c01-3abc917a5038 | -9.65672 | -50.74307 | 2025-07-01 05:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf7413e4-0372-33da-88df-9318648f8903 | -12.97285 | -54.68907 | 2025-07-01 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 083129da-6130-3d16-8c4a-7575421fa0c3 | -9.97004 | -48.23722 | 2025-07-01 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| be4b2ef3-f797-344f-9dea-1b5d40feeca0 | -9.11072 | -59.05238 | 2025-07-01 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74ab16b5-4a0a-3dab-aff5-6acbb6d22075 | -9.24676 | -58.7503 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 791834fe-255a-3b82-9e39-831ce27a51c8 | -11.60121 | -65.1463 | 2025-07-01 05:14:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11426051-2c4a-3294-b261-070c51b6bc8f | -11.2044 | -55.92155 | 2025-07-01 05:14:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca410155-b0fc-3611-8f24-a29fb29b38c5 | -9.24506 | -58.76088 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8427173a-f0d5-35fb-a0ee-7b509d19af4c | -11.57792 | -54.56743 | 2025-07-01 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df38f570-2098-36b8-919b-da1b4a27f4e9 | -12.01173 | -62.83245 | 2025-07-01 05:14:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67d8a052-6e40-3cd8-b862-9e3fcbc93b8b | -10.03992 | -59.35691 | 2025-07-01 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ebc77d68-eea0-300e-b594-0cfffd15c01e | -10.93499 | -55.32248 | 2025-07-01 05:14:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ed94119-9afc-3512-aefb-ac0371065178 | -10.86854 | -53.77243 | 2025-07-01 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b13e9c6-6b1d-3219-b473-e618117b757a | -9.65607 | -50.74802 | 2025-07-01 05:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3697c9c2-94f9-3827-b436-29ac190c04ad | -10.12557 | -57.77708 | 2025-07-01 05:14:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 13329ca4-88c2-3a00-8167-ac89f6df9049 | -10.87813 | -56.44799 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 97fe3752-c91d-3d8c-93ed-76414da31372 | -10.81464 | -55.85755 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4500b96-b46a-35d9-9e64-f985e6c0616a | -9.96702 | -48.23956 | 2025-07-01 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a05bb28a-53f2-37e3-be40-717b8142819b | -12.2972 | -48.81073 | 2025-07-01 05:14:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c0fad16-f5a3-3eac-bb44-e51a9df243ee | -15.07922 | -48.94602 | 2025-07-01 05:14:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76b3451f-0292-31d8-be49-34120c0c2d0c | -11.02508 | -56.25938 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56045026-ed83-3b3d-9d78-4f3109c471c2 | -9.71344 | -56.18223 | 2025-07-01 05:14:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8aa7b101-5633-387c-9878-b12d58fe802a | -12.01742 | -47.77267 | 2025-07-01 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dc6caf4e-32fb-30ae-bd95-f8a1e7ebbc76 | -9.72032 | -56.18329 | 2025-07-01 05:14:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83e2b996-6260-3074-a765-572793b082a1 | -9.23952 | -58.75275 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4b4863fb-2e78-35d9-8f0f-27d13d799106 | -11.74848 | -54.72352 | 2025-07-01 05:14:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README15.md)
