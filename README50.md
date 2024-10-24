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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a064a928-428d-3d77-8661-75e42559c8be | -15.898 | -43.95024 | 2024-10-24 04:36:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 23a96100-767b-3099-9524-6b7beb52bff3 | -15.41664 | -43.08337 | 2024-10-24 04:36:00 | NOAA-21 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 2a16d7ae-3a78-3592-b0f9-763cfb557406 | -15.8913 | -43.03199 | 2024-10-24 04:36:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2cb20f8d-e082-3770-be67-f6367d96c7ed | -15.86158 | -43.52812 | 2024-10-24 04:36:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1566db46-29ce-37a1-90ae-89ecb08e46a8 | -15.50046 | -42.86872 | 2024-10-24 04:36:00 | NOAA-21 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9707f78a-52b9-3c82-8ae9-4d93f3a5fa81 | -17.89819 | -44.00094 | 2024-10-24 04:36:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ec4079e-60d4-3ddf-84a1-70a8c754f74f | -16.69322 | -44.23048 | 2024-10-24 04:36:00 | NOAA-21 | SÃO JOÃO DA LAGOA | MINAS GERAIS | Brasil | 3162252 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3aff3689-5c63-3ea1-9ac0-a1dcf766b077 | -16.68145 | -43.88392 | 2024-10-24 04:36:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4933b292-420f-3c9f-b81d-d44b1ff6630f | -13.73179 | -44.28579 | 2024-10-24 04:36:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e4e25009-5948-39a2-b2a1-32ca9e1227b0 | -14.92693 | -45.1134 | 2024-10-24 04:36:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a6da6a2-57c0-3293-8ce9-03438c85fee2 | -14.92622 | -45.11856 | 2024-10-24 04:36:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b1c4f300-0d9f-3398-9223-99d799447634 | -14.92231 | -45.11801 | 2024-10-24 04:36:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1d08c553-aac0-3196-a1d8-4cd3641629e1 | -14.92161 | -45.12315 | 2024-10-24 04:36:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7fa75118-d6cc-3f35-8405-1866b6ca751e | -14.9184 | -45.11745 | 2024-10-24 04:36:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 36174749-f4ce-35df-b348-c89e77439dcd | -14.9177 | -45.12258 | 2024-10-24 04:36:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7eae9e6e-6c2e-300d-93c3-250afce74be8 | -14.91379 | -45.122 | 2024-10-24 04:36:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ca3923eb-79c1-33e0-9daa-14b5d3485e6b | -14.9131 | -45.12708 | 2024-10-24 04:36:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b262d6c4-a773-3770-8d77-bc280cb7fae3 | -14.90919 | -45.1265 | 2024-10-24 04:36:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 072d912e-1915-3b65-a878-b9bffe7a7c5b | -14.84439 | -45.19438 | 2024-10-24 04:36:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 017d8d25-62a1-39f0-b02e-6e26632c08d1 | -14.71706 | -44.18201 | 2024-10-24 04:36:00 | NOAA-21 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5e1edaf-b3ee-3588-9ab6-015857b4eb4b | -14.27287 | -44.55894 | 2024-10-24 04:36:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e6145ab-94f9-31dc-a268-992675772210 | -14.2724 | -44.56253 | 2024-10-24 04:36:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94d287cd-be34-35e1-bb76-f0d6153a95a5 | -14.27094 | -44.56219 | 2024-10-24 04:36:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 16bb2e27-e9cb-3972-a137-ae61295cfd57 | -17.19999 | -45.33416 | 2024-10-24 04:36:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 583e0520-34e7-30c6-82bc-5a82e05a8753 | -13.56082 | -46.52512 | 2024-10-24 04:36:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e17f3bf7-4874-3386-bfbb-3c3c2fce5b4a | -13.56029 | -46.52341 | 2024-10-24 04:36:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5e11ab2-f322-3eeb-b2bf-21bc57076c24 | -13.55971 | -46.52753 | 2024-10-24 04:36:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 649d1704-3abd-330c-8684-f19fec47ff66 | -13.55666 | -46.5287 | 2024-10-24 04:36:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 335f0764-19f1-38cd-a997-117ca748e350 | -15.05054 | -46.2023 | 2024-10-24 04:36:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0f811fae-2e84-38d7-9c1b-9962ad613ad6 | -15.04686 | -46.20173 | 2024-10-24 04:36:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2e7ba97f-b778-3e18-93b7-c35e61461568 | -15.27956 | -46.6132 | 2024-10-24 04:36:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e295dac-30c5-3e97-9bea-a051c5fe1d7f | -18.92786 | -47.51748 | 2024-10-24 04:36:00 | NOAA-21 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 231025a6-6731-3e67-85b3-04e45cf6ea60 | -18.37843 | -47.39178 | 2024-10-24 04:36:00 | NOAA-21 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7871ee7a-12ab-36d2-a48e-13fb78242d0f | -18.37783 | -47.39607 | 2024-10-24 04:36:00 | NOAA-21 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e3fa551-2de7-38c3-b913-9a8a1730e220 | -13.86357 | -50.35188 | 2024-10-24 04:36:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5e1729b-e693-38bf-bf3e-1537903bd969 | -15.87356 | -50.5327 | 2024-10-24 04:36:00 | NOAA-21 | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a9db758-b12d-34b7-ab7c-48c0324897e1 | -15.78748 | -50.51816 | 2024-10-24 04:36:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dcc8b658-85e7-3130-9885-0404f235b950 | -14.00727 | -47.97621 | 2024-10-24 04:36:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6486ee0a-a687-3d02-ae3b-f7d9890c5346 | -14.00389 | -47.97567 | 2024-10-24 04:36:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b178702-e21d-3652-8b27-3184490d62b0 | -13.93736 | -48.15527 | 2024-10-24 04:36:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c8e83bc-4899-3bcc-be87-c56ae8b4ad3a | -13.9301 | -48.1577 | 2024-10-24 04:36:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bff4716b-b434-3ae6-ad91-87b9bc803def | -18.26387 | -48.24638 | 2024-10-24 04:36:00 | NOAA-21 | CUMARI | GOIÁS | Brasil | 5206602 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 13e469dd-53a9-370d-a4bf-810a8e36d6ff | -13.00503 | -48.8931 | 2024-10-24 04:36:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81baa218-a30e-3200-9a9e-43b0a68d3575 | -15.6875 | -51.38913 | 2024-10-24 04:36:00 | NOAA-21 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3511e35-a37b-3a1c-a0b2-523dc3958618 | -13.00226 | -48.88903 | 2024-10-24 04:36:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 191fa835-d0b9-32f7-8fb1-77abcd8cfdce | -14.1923 | -49.82675 | 2024-10-24 04:36:00 | NOAA-21 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ae4257c-df7c-3910-848e-2b9963d2ab3d | -17.29156 | -51.87296 | 2024-10-24 04:36:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c532254a-34ec-3b07-acc9-2cb7f92f12ef | -16.75829 | -50.70515 | 2024-10-24 04:36:00 | NOAA-21 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 267c5ba7-0cbd-301d-8e2a-768115b36c84 | -13.07065 | -48.88556 | 2024-10-24 04:36:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af52e0ad-f09f-368a-907f-93aa36340a64 | -13.00172 | -48.89257 | 2024-10-24 04:36:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3decd17c-9f69-37d0-9237-99a8cf75e440 | -12.96906 | -48.94834 | 2024-10-24 04:36:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d749b19-a6f1-34d0-baa0-ad0388f5dbe6 | -12.96851 | -48.95188 | 2024-10-24 04:36:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e2f313c-5a9a-3eb8-9886-d1db1283d0d0 | -12.96075 | -48.87097 | 2024-10-24 04:36:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5cd197a1-f7c2-3c20-921a-0f177876a73a | -12.9602 | -48.8745 | 2024-10-24 04:36:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a1c9e006-ef20-3a46-8872-5d53552d5c9f | -12.95744 | -48.87043 | 2024-10-24 04:36:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3514c327-adc5-3481-ab87-f0a5f7be5f98 | -12.95689 | -48.87397 | 2024-10-24 04:36:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b52effbb-a43a-3cea-a4a9-aad71f8002a4 | -16.75771 | -50.70875 | 2024-10-24 04:36:00 | NOAA-21 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 612033a9-23e8-3ee8-999d-b32a36e49a17 | -13.27302 | -49.24779 | 2024-10-24 04:36:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 667de56e-8316-3bf7-83a8-fc28525f4ed5 | -13.27247 | -49.25132 | 2024-10-24 04:36:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 063d7768-ccd8-3548-b4c9-38fd5af1a3c7 | -13.25716 | -49.21583 | 2024-10-24 04:36:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d249d579-2fbe-339e-bdca-5edd7cb745e8 | -13.10535 | -49.12261 | 2024-10-24 04:36:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4daee6a-e100-3556-9630-2e93db74fafc | -13.10205 | -49.12207 | 2024-10-24 04:36:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1bf0bb4-c114-36ee-8cd8-ea3a8375ee56 | -13.01316 | -49.55898 | 2024-10-24 04:36:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d2382c6a-3964-3f5e-b71d-5ef8ae6013a8 | -13.0126 | -49.5625 | 2024-10-24 04:36:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| feba9201-33b8-3f94-abe1-5e82b5cd4b08 | -13.0093 | -49.56195 | 2024-10-24 04:36:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4c4ea06-9a92-34e5-b65e-e6fd520c0df3 | -14.40385 | -48.57191 | 2024-10-24 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7358c772-9211-3698-8570-013165d7acad | -14.04354 | -48.77264 | 2024-10-24 04:36:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7fc0a4c5-c895-3cc9-9a8f-910500063e84 | -13.86051 | -48.6368 | 2024-10-24 04:36:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 216fe310-7f08-33e8-9160-c0e2d45e7db2 | -14.55833 | -49.72755 | 2024-10-24 04:36:00 | NOAA-21 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8b0cde93-8095-3880-9d4a-acef2082a03f | -14.55503 | -49.72701 | 2024-10-24 04:36:00 | NOAA-21 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a0b0191b-b49a-3444-b568-6f52ab79c9a3 | -14.55184 | -49.941 | 2024-10-24 04:36:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9767a0f0-cbcb-335d-aefd-3262f0ce3b03 | -14.20226 | -49.80659 | 2024-10-24 04:36:00 | NOAA-21 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a5b2269-2183-3d1a-9e57-1a796cbef151 | -14.189 | -49.8262 | 2024-10-24 04:36:00 | NOAA-21 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 83c53ed1-515c-3e0a-896b-36457c58e808 | -16.75325 | -50.71539 | 2024-10-24 04:36:00 | NOAA-21 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e1d4b467-eda1-3ff9-84f6-626b17f7fd56 | -13.54918 | -49.89056 | 2024-10-24 04:36:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4cc90d3d-d77d-3537-8791-87b371892b7a | -13.54587 | -49.89001 | 2024-10-24 04:36:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91a92ce6-0494-3f13-be23-9abc6837619a | -12.90759 | -50.19938 | 2024-10-24 04:36:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8314c843-0950-3861-a882-91818583b252 | -13.89515 | -50.74531 | 2024-10-24 04:36:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 88f20824-9bb6-30e6-bee7-f6ce84a3eb20 | -14.26781 | -51.13195 | 2024-10-24 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a276151e-863d-35e1-8764-1a6e7dda9f8d | -14.26672 | -51.12773 | 2024-10-24 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1efd8ee4-f113-3a0b-921a-ba7751963c6e | -14.26612 | -51.13143 | 2024-10-24 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 202d7320-4c9c-3f47-b4e7-5eef7fde8160 | -14.26395 | -51.12347 | 2024-10-24 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 21bbf21b-6a6e-3b65-8560-9d7b6a8fe42f | -14.26335 | -51.12717 | 2024-10-24 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 642eb5c2-df1c-3c8e-ac57-1d119f5252fb | -14.26275 | -51.13087 | 2024-10-24 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| ecdeedf3-3819-316a-a74d-385e1c673c1f | -14.26118 | -51.11922 | 2024-10-24 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c3ac60c-1954-3b3d-8615-f7d9f515541e | -14.26058 | -51.12291 | 2024-10-24 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| affddd4d-efca-3a6f-8ba9-8749164e546e | -14.25998 | -51.12661 | 2024-10-24 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b9fe2054-6574-3ed6-a64a-53b43ba8b51b | -14.30054 | -49.91715 | 2024-10-24 04:36:00 | NOAA-21 | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8dd122c-5971-37f2-8508-2ea1aa2c47a4 | -16.74994 | -50.71482 | 2024-10-24 04:36:00 | NOAA-21 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8820b13d-95df-30be-adc2-d2abdd86195f | -16.74936 | -50.71843 | 2024-10-24 04:36:00 | NOAA-21 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e8c0d697-24fa-3675-b85e-046c0b79c088 | -16.74664 | -50.71425 | 2024-10-24 04:36:00 | NOAA-21 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 08f078ef-68fd-3cca-ac01-fbd67e1363ce | -18.29969 | -54.61335 | 2024-10-24 04:36:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bf6bd38d-333c-3f36-b4fd-e6e8278a8b2a | -14.82253 | -52.86665 | 2024-10-24 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b53b5d6d-6d1a-30cd-96cb-96ac7c2090ed | -14.72358 | -52.78555 | 2024-10-24 04:36:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5bd0039-7e60-34d6-a417-3e0ed8a62ddb | -14.45513 | -52.88667 | 2024-10-24 04:36:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d46a2515-f6f7-3ea4-87a7-be802697ecdd | -14.45226 | -52.88177 | 2024-10-24 04:36:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bbbfadca-e831-363a-8d3d-5ea86307ce90 | -15.87258 | -53.26614 | 2024-10-24 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2a1e7c8f-969e-32c5-82e6-69510fa34584 | -15.87154 | -53.26228 | 2024-10-24 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| efc37149-779a-3d9b-b5e9-13378b78051b | -15.8708 | -53.26662 | 2024-10-24 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d1c65e79-52c7-3a65-92f7-5ccd84f2a32f | -15.86974 | -53.26119 | 2024-10-24 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README51.md)
