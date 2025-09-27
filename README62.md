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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b78c402a-10e9-36b4-8b71-1ef5da0a5978 | -9.14819 | -47.76995 | 2025-09-27 12:36:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| a0a3cefb-e865-35cd-b2d1-aaf9b4c8ac1d | -9.35331 | -47.60201 | 2025-09-27 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| d82cd28b-6643-3518-823d-a69ee6079eca | -6.84093 | -43.17017 | 2025-09-27 12:36:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 41.7 |
| 42ec155a-7d62-388b-81e8-5a667e576716 | -9.85253 | -51.27053 | 2025-09-27 12:36:00 | TERRA_M-T | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 44cb569f-43ab-31e4-9993-1c7e5b731853 | -9.89115 | -46.87872 | 2025-09-27 12:36:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| bde7d970-4849-3edf-9e28-77ea09064216 | -9.88757 | -47.72239 | 2025-09-27 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 79384f3e-e192-3fdd-adc0-cf5c239aff18 | -10.25662 | -52.19803 | 2025-09-27 12:36:00 | TERRA_M-T | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 963bc83b-a87d-3455-b5c0-177dda827b7b | -8.91749 | -46.09687 | 2025-09-27 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 25.2 |
| c1824deb-1f87-3bc1-a459-4948f0f0a28f | -8.64058 | -44.83252 | 2025-09-27 12:36:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 132be740-610c-342a-af67-7608c780badb | -5.50767 | -43.87233 | 2025-09-27 12:36:00 | TERRA_M-T | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 43.3 |
| c4ad1469-dbc7-3404-b345-f65ba94e995c | -7.78841 | -46.95071 | 2025-09-27 12:36:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 870a605f-583d-31a4-a1cd-1ba179b050db | -9.85125 | -51.27976 | 2025-09-27 12:36:00 | TERRA_M-T | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f6d09a57-cc8e-399c-8970-3c0315914648 | -9.14633 | -47.78423 | 2025-09-27 12:36:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 3dbd1cf1-b00e-3c89-af05-4ca249f9dc88 | -9.37032 | -48.87176 | 2025-09-27 12:36:00 | TERRA_M-T | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 776dd2f0-3946-32b1-a400-eb69b3f043c1 | -9.28728 | -48.1927 | 2025-09-27 12:36:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 7516befc-711b-34cc-8d95-f91f9e09c3ab | -4.19022 | -44.2871 | 2025-09-27 12:36:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 5b4b3b9f-d831-34b2-9e20-91948dcffdbe | -8.72601 | -46.68707 | 2025-09-27 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| f87d5615-9efe-3438-8cf8-f7bd6cce7e05 | -11.35835 | -45.01472 | 2025-09-27 12:36:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 00ce38a5-1e9d-3fec-9394-ad7389ac04b7 | -8.632 | -44.84893 | 2025-09-27 12:36:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 46.4 |
| bb2e9e90-35d3-332b-839e-852b16b04818 | -15.90326 | -59.32176 | 2025-09-27 12:38:00 | TERRA_M-T | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 7ba1d902-a87f-3696-9142-cad2b6a4117e | -15.56949 | -51.7197 | 2025-09-27 12:38:00 | TERRA_M-T | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| d52994ce-5719-31ac-a4f4-464852ae94c4 | -13.45155 | -45.89938 | 2025-09-27 12:38:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| fb69a860-2f60-3606-8203-e81b9b511d80 | -15.01209 | -54.9949 | 2025-09-27 12:38:00 | TERRA_M-T | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c6e99a46-05ae-3979-9ef0-3ff372594649 | -13.26496 | -48.44699 | 2025-09-27 12:38:00 | TERRA_M-T | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 2d9f359d-149d-3695-8e06-9407ae15f096 | -15.32444 | -47.88448 | 2025-09-27 12:38:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 68c3c81a-4c8a-3336-9ec3-505da6e7b789 | -14.10274 | -51.14132 | 2025-09-27 12:38:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a5a80301-d1d8-3d6b-af58-4b57cebcb2ee | -17.92713 | -48.628 | 2025-09-27 12:38:00 | TERRA_M-T | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b1c895ec-9509-30e6-ba60-3c74b15683e9 | -13.2937 | -46.44376 | 2025-09-27 12:38:00 | TERRA_M-T | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 36.8 |
| c2505454-1d10-31d4-a2de-3c8e1ee05658 | -14.69774 | -50.8837 | 2025-09-27 12:38:00 | TERRA_M-T | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 5d129047-bada-3d1b-8ec5-62308c794a40 | -15.57082 | -51.70962 | 2025-09-27 12:38:00 | TERRA_M-T | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 8f279b96-7f59-3184-b124-89b27c780b40 | -15.58145 | -51.70086 | 2025-09-27 12:38:00 | TERRA_M-T | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| a36e7b8e-eb57-343f-9dc2-4bd4eebc3af4 | -15.33163 | -47.87299 | 2025-09-27 12:38:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 525c9eb9-6a20-3aa6-b76c-93f569054f33 | -15.43022 | -48.22305 | 2025-09-27 12:38:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 7ea1015c-734c-38f1-8ee4-c397609fd222 | -14.01992 | -56.1009 | 2025-09-27 12:38:00 | TERRA_M-T | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 60.3 |
| b54a61ce-01f3-3bcb-aa9c-27780723a465 | -14.48619 | -48.5599 | 2025-09-27 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 42.5 |
| f0a6f4cc-d06a-3516-8fa7-b0eba5d96ac2 | -14.07521 | -48.82738 | 2025-09-27 12:38:00 | TERRA_M-T | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 328e77a8-b99f-32e1-a650-b42a7fa352dd | -12.28528 | -57.61821 | 2025-09-27 12:38:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| bd98402d-7a38-302a-ab33-6199d024a772 | -11.98095 | -47.91573 | 2025-09-27 12:38:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 1d6aefc5-ce4c-3683-a92e-bfd582913843 | -12.53341 | -56.87038 | 2025-09-27 12:38:00 | TERRA_M-T | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 00811fcd-09fc-39d6-a562-956396509f42 | -12.03385 | -47.05321 | 2025-09-27 12:38:00 | TERRA_M-T | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 252a448e-38b8-36ce-b848-c2e21f0f270b | -12.4851 | -56.39915 | 2025-09-27 12:38:00 | TERRA_M-T | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 807a7898-4a41-39eb-9651-9c6b1e98f02b | -11.94416 | -52.5693 | 2025-09-27 12:38:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0754c540-617b-3b3a-acdb-03b6eade46bb | -11.27307 | -52.7495 | 2025-09-27 12:38:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 3dc8babf-ed1b-39df-8417-a0a0a2d8f2b7 | -11.96762 | -47.92979 | 2025-09-27 12:38:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 52.9 |
| de89a7c6-1418-3803-aaa2-e5ba75bad544 | -11.98481 | -47.88505 | 2025-09-27 12:38:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 4d7f9218-e76e-3fe5-ba8b-ea8caf7ede59 | -11.27436 | -52.74055 | 2025-09-27 12:38:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 87778f1d-cffe-362f-8b43-d18ced2d90c1 | -15.27049 | -56.81744 | 2025-09-27 12:38:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 1a3f0839-25ba-3b8f-b713-62befc86b3e1 | -11.67579 | -54.8481 | 2025-09-27 12:38:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| efe79813-60fb-34cf-acff-18ebd23996b9 | -12.95485 | -48.90597 | 2025-09-27 12:38:00 | TERRA_M-T | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 71567343-508f-345d-9a09-a709c678c806 | -12.4756 | -43.18581 | 2025-09-27 12:38:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 41.8 |
| a2b94e01-c7bc-3458-b005-c09cf74c5b5c | -15.89348 | -46.19988 | 2025-09-27 12:38:00 | TERRA_M-T | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 31.1 |
| fd7808e1-6292-38db-b50f-137536ff8ef4 | -13.19332 | -47.42571 | 2025-09-27 12:38:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 93024e61-8a6a-3639-9814-6b16dac0f4f1 | -13.62002 | -48.0736 | 2025-09-27 12:38:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 26.8 |
| e9eca3af-c060-3e85-9f7a-d166f84a5678 | -13.77254 | -47.86817 | 2025-09-27 12:38:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 2ecf551b-33b7-3a82-bf6c-fa72739290f9 | -12.28694 | -44.06164 | 2025-09-27 12:38:00 | TERRA_M-T | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 293.1 |
| f9e7d754-3114-35de-b783-be5c000ce860 | -11.99233 | -47.91737 | 2025-09-27 12:38:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 404227e2-7443-322e-aad0-1f1877befaa9 | -13.83061 | -47.94595 | 2025-09-27 12:38:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 2c716624-e970-3bfd-b91f-304f91cfba34 | -12.26785 | -44.09113 | 2025-09-27 12:38:00 | TERRA_M-T | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 153f6e3d-d2fd-3750-8828-b49feda901e8 | -14.49856 | -48.5517 | 2025-09-27 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 119f1b1f-ebc9-3e66-9e98-8f5641167aa7 | -15.32959 | -47.89074 | 2025-09-27 12:38:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 8239333b-6e2a-316f-942e-e925abc2728f | -12.26691 | -44.06461 | 2025-09-27 12:38:00 | TERRA_M-T | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 00cf1577-2e62-3e90-a6a1-0809ead6c2ab | -15.57878 | -51.721 | 2025-09-27 12:38:00 | TERRA_M-T | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 010fcce5-c9bc-373a-80fe-f8599613e04d | -14.21504 | -53.38421 | 2025-09-27 12:38:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 81586789-674c-3cac-990c-0b286572ba67 | -11.99966 | -54.59561 | 2025-09-27 12:38:00 | TERRA_M-T | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ea5625ad-94fb-3fd5-a0a5-02e52e6008fd | -10.99377 | -54.16055 | 2025-09-27 12:38:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| d6d5b8f1-9138-31e3-a9a1-be80f0bc6c3d | -15.58012 | -51.71091 | 2025-09-27 12:38:00 | TERRA_M-T | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 542cc741-1be2-34d6-9fb8-52da3f9c843f | -13.33598 | -47.30556 | 2025-09-27 12:38:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 6d5394e5-8d33-3267-896a-da26122ede89 | -13.59774 | -47.30241 | 2025-09-27 12:38:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 7fe6a7e6-ef1e-3126-8abe-844608d87bdb | -14.49555 | -48.57657 | 2025-09-27 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 20.7 |
| a0341882-801c-3c7e-94f3-c49f068bba3b | -14.49675 | -48.56703 | 2025-09-27 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 50b17ffa-c24e-31d7-80dc-78d49b25d7dc | -16.18305 | -45.15088 | 2025-09-27 12:38:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 3903e6f3-1c63-3c74-a73d-96941a1b061a | -12.00558 | -47.90425 | 2025-09-27 12:38:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 42.5 |
| d7c49c4f-330a-34d4-aec7-bc267710f4a3 | -12.27135 | -44.06008 | 2025-09-27 12:38:00 | TERRA_M-T | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 175.7 |
| 46b5789a-5e7b-3a8e-929b-0e9702d1f5f1 | -16.87587 | -49.51149 | 2025-09-27 12:38:00 | TERRA_M-T | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| bcf83446-aaf3-343a-83f1-0f999b0c29bb | -13.29623 | -46.43851 | 2025-09-27 12:38:00 | TERRA_M-T | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 20.4 |
| bd3234a9-f284-3ec7-8cc1-7d586944759a | -16.86982 | -54.66194 | 2025-09-27 12:38:00 | TERRA_M-T | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 38a4c77e-4262-3637-bdf7-c6cfe0230ca1 | -11.80753 | -54.77339 | 2025-09-27 12:38:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 57700b06-a04b-3c5a-8001-5a1a7faed9e0 | -12.96558 | -48.90726 | 2025-09-27 12:38:00 | TERRA_M-T | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 27.9 |
| a48173a7-c419-3bfc-8df2-7022058e6f87 | -12.9896 | -49.43171 | 2025-09-27 12:38:00 | TERRA_M-T | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 951948dd-bb03-32ea-8608-ab98089f3010 | -12.65006 | -51.68097 | 2025-09-27 12:38:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 91a55914-bf61-3862-bb16-96ff692dd5ea | -14.06423 | -48.82614 | 2025-09-27 12:38:00 | TERRA_M-T | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 2a3fcad2-b9cf-377f-a212-2894ce54b605 | -13.28317 | -46.43653 | 2025-09-27 12:38:00 | TERRA_M-T | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 17c41ed5-12d0-3d6e-8389-ab0ab6017c0c | -16.29784 | -52.92693 | 2025-09-27 12:38:00 | TERRA_M-T | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9a9619d1-15d4-3949-861b-d963fe7cfc89 | -12.5376 | -48.49648 | 2025-09-27 12:38:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 2af83f0d-ebe3-3a8b-b8c8-f549342339f9 | -13.68312 | -43.3989 | 2025-09-27 12:38:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 1624028e-5f85-34e9-9795-33310a19b450 | -11.979 | -47.93127 | 2025-09-27 12:38:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 319.6 |
| cbb6ad62-3641-3e38-936c-b97714400066 | -12.29632 | -45.66077 | 2025-09-27 12:38:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| a7b42a35-c39e-35f0-9c51-ffd24af92879 | -12.29197 | -45.64186 | 2025-09-27 12:38:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 32.6 |
| dfd23525-8a4b-3428-a11a-c179600702f4 | -13.61805 | -48.08957 | 2025-09-27 12:38:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 32.8 |
| e45a4785-9b4a-3bc2-8e8f-04179349b62e | -12.65973 | -48.15924 | 2025-09-27 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 1fc5a024-1f3d-3c6a-8902-889902058403 | -13.63147 | -48.07582 | 2025-09-27 12:38:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 0e3d8c66-d5e6-3534-a314-902cd26cab43 | -14.02162 | -56.09005 | 2025-09-27 12:38:00 | TERRA_M-T | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| bad03e3f-fd42-347c-8a44-969f70ebc553 | -15.28255 | -46.43042 | 2025-09-27 12:38:00 | TERRA_M-T | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 25.8 |
| aaa11688-5c51-3765-aa0e-de9f01db1c25 | -12.03741 | -47.06017 | 2025-09-27 12:38:00 | TERRA_M-T | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 00346048-b5b5-34e6-8b5c-484934d86bf3 | -14.49747 | -48.56127 | 2025-09-27 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 3bb28027-6727-3e68-a434-d879486cca96 | -13.33793 | -47.28934 | 2025-09-27 12:38:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 29.1 |
| aa082fe4-d76a-32b5-b66d-f7e01ae3798a | -12.28247 | -44.06647 | 2025-09-27 12:38:00 | TERRA_M-T | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 466.1 |
| cf25df04-ead8-375a-a1e9-503c24371af1 | -7.5568 | -46.7128 | 2025-09-27 12:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 2ae02ce7-3a06-33db-b428-c13723fea9da | -11.3451 | -45.0366 | 2025-09-27 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.3 |
| d88d5d07-4cea-3d9b-915b-2f46143fff06 | -11.4417 | -44.9767 | 2025-09-27 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |


[Clique aqui para ver as próximas entradas](README63.md)
