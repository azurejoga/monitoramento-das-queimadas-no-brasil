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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e78c8b6-58c3-3f91-80b7-721289171a29 | -18.88875 | -41.13514 | 2025-09-07 04:21:00 | NOAA-20 | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9da13648-cdaa-3558-b35b-2d9dbd71e27a | -12.92799 | -54.77209 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 69b165de-e5bf-3790-b9c6-eecb1e5c598a | -17.67203 | -43.52843 | 2025-09-07 04:21:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4b0b4e1-e3f7-3fa7-8c85-86e912749f06 | -14.75389 | -47.51541 | 2025-09-07 04:21:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a24208c9-05f4-3d2a-b7e5-4459ecbc71a3 | -16.33094 | -58.11689 | 2025-09-07 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 28d0fdd8-bc2d-36b2-8a45-d5e09ddc68c3 | -13.00063 | -54.82295 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c99a639f-ad55-327a-bec6-93e9490a12fd | -14.58479 | -48.09875 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dd73fbb1-3b06-305b-b37b-bc19e411e2cd | -20.01906 | -44.59741 | 2025-09-07 04:21:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4aa1c08b-5a0c-3dd3-9643-e944005d221f | -19.06984 | -46.77411 | 2025-09-07 04:21:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b27ce9ef-ee6c-3fdf-a9b4-55b845a1ee4b | -14.58166 | -48.0754 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8fc6da32-e82f-3280-a650-c007edb95838 | -20.40659 | -43.76965 | 2025-09-07 04:21:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ad604359-feaa-3f5d-8ff6-4f1a587966ee | -13.91535 | -53.99283 | 2025-09-07 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca5a4832-d14d-3a73-a110-4dcfe2322aab | -17.55782 | -44.40575 | 2025-09-07 04:21:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24e83cb0-b333-3f37-8c16-da821080879a | -13.89453 | -53.99971 | 2025-09-07 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9eebb000-91b7-3344-9ce8-c81644258017 | -11.15711 | -59.16141 | 2025-09-07 04:21:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70d9950d-20e3-3d0c-998e-bc8469e0378f | -20.54632 | -46.44379 | 2025-09-07 04:21:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cfc2c039-c9b7-3bbe-b751-30e190ca2920 | -16.93535 | -45.75751 | 2025-09-07 04:21:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b5c56d89-a960-341e-b2d4-2693254c4a1f | -13.73696 | -46.90799 | 2025-09-07 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a921d9b-e452-39c3-a4b4-07138c728bd1 | -18.07873 | -47.98956 | 2025-09-07 04:21:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c3dd5af1-044a-37ab-8a64-63f73dc84565 | -13.91748 | -48.03994 | 2025-09-07 04:21:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1b98022-6de7-3c7b-b059-cd91d6eac820 | -12.94798 | -54.80436 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34796594-eb32-315d-8985-0bb638065326 | -16.28355 | -45.68533 | 2025-09-07 04:21:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a4d6ed57-8ff6-347b-a762-27f48355a2bf | -15.83694 | -52.27722 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b58ae14d-9f71-3e5f-9fb9-425445c152ca | -17.40303 | -49.30972 | 2025-09-07 04:21:00 | NOAA-20 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6a2ac8d3-1568-3a4a-9ad0-e2c635cf533a | -19.47105 | -47.75514 | 2025-09-07 04:21:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 1aea518f-2714-3c34-aec9-01e8428bc47e | -16.94098 | -45.766 | 2025-09-07 04:21:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2d496983-6c9e-32fa-a59a-25e57bd0a0ad | -15.53775 | -42.65474 | 2025-09-07 04:21:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 42aa6ed6-be4a-3c4f-a280-b1c0b972c3b6 | -19.37034 | -43.65603 | 2025-09-07 04:21:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c27909c3-2222-359e-84b1-c054def76797 | -16.32903 | -52.94911 | 2025-09-07 04:21:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff98fc85-2f35-36b5-9c4a-109e54bc11cc | -17.22241 | -46.70131 | 2025-09-07 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f7f2090-feda-3e5c-90ad-357696d04f05 | -13.46109 | -48.14832 | 2025-09-07 04:21:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6b7353d-4f6a-32cd-b157-8aee80ba9bdf | -15.1399 | -52.35847 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0dac26a7-10b8-350e-b45e-f7903a7d27a8 | -19.7109 | -44.56364 | 2025-09-07 04:21:00 | NOAA-20 | SÃO JOSÉ DA VARGINHA | MINAS GERAIS | Brasil | 3163102 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4620cc28-e030-36ce-b85d-3d0eff75fb15 | -12.61477 | -56.98927 | 2025-09-07 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92b9aa7b-80c4-3015-a8c2-657638498c3e | -16.94153 | -45.76228 | 2025-09-07 04:21:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e6d05a6d-e136-3b7a-b7cc-f7ac313d8c04 | -13.78202 | -52.77818 | 2025-09-07 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be722a84-304a-32ed-8469-9d528b37cbb1 | -15.53708 | -42.65972 | 2025-09-07 04:21:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 9aa4ed3c-7bd8-3bdf-9b0f-fea65f0ce90b | -16.92527 | -45.77871 | 2025-09-07 04:21:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e76becaa-b8f6-3037-b6a4-4c22e08b134e | -13.55586 | -48.10641 | 2025-09-07 04:21:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6a1f2c5d-5b06-3336-8e7a-3d3076d11997 | -20.53614 | -46.44232 | 2025-09-07 04:21:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 5ee3b029-2325-327d-854f-25cf03a67c91 | -13.05494 | -48.05734 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c456a55-cb6b-31a5-bee3-a5c3ed2c845f | -12.77085 | -52.94701 | 2025-09-07 04:21:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a34c9648-e464-328c-bd6a-74a6a50addaf | -14.44333 | -48.44826 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f179913-f28b-3552-a286-dc3f20a3cc8f | -15.11129 | -48.07829 | 2025-09-07 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9f75c84a-47a9-381d-82f2-505722d692f9 | -14.45167 | -48.4614 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e823707d-83d5-314a-bfea-7cffe81b3b7e | -12.18913 | -53.90493 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3fc589ac-beb1-3b51-b642-195ef1de0f0e | -15.69879 | -53.55922 | 2025-09-07 04:21:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0be804f3-36dd-35b0-ab62-83dd05d5b4cd | -15.84878 | -52.27936 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 68eda8a7-5ac4-33df-b9c7-2b2d5410bfab | -17.2429 | -46.70101 | 2025-09-07 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54445a5f-ade7-3bc6-a86f-5170c933fdab | -19.42289 | -42.328 | 2025-09-07 04:21:00 | NOAA-20 | IPABA | MINAS GERAIS | Brasil | 3131158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 336e1930-67bd-3bc7-9cb8-04b3282a4e74 | -19.46716 | -47.75822 | 2025-09-07 04:21:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 857e4a6f-20ad-3040-ac57-d932e27a3537 | -16.96572 | -45.83088 | 2025-09-07 04:21:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47f78e88-db85-3ef8-986f-f8f643a01b01 | -14.4529 | -48.45402 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5df22476-f7d6-358e-9eb9-c495c2de9547 | -16.93316 | -45.79515 | 2025-09-07 04:21:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d22f736a-f3b2-30e0-ba3a-f3282ba0f9e4 | -12.9503 | -54.79212 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e249668-3e75-3dc3-b4b2-a6326be0b679 | -16.28411 | -45.68163 | 2025-09-07 04:21:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3c3a420b-31aa-3c39-8624-ecd9ae4bbea7 | -13.45912 | -46.83968 | 2025-09-07 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7a53f4fb-fb86-328c-867b-7df9e6263d66 | -15.09022 | -44.0064 | 2025-09-07 04:21:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f12b9ed1-6fb4-3efa-8fa4-03924eb30c71 | -14.58754 | -48.10318 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb986a06-22dc-3768-a4ee-1d9ee54406b7 | -15.49895 | -52.77617 | 2025-09-07 04:21:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 60a16cef-79dd-31e8-afc0-02aa4e1dd144 | -13.89921 | -53.99382 | 2025-09-07 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a52e8906-76c3-3cb3-9c4a-b5abe798bdb1 | -16.92314 | -45.78233 | 2025-09-07 04:21:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 84c85ab7-b67c-3196-b051-85f5013c7321 | -13.82862 | -46.28691 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 27203a60-07f4-3d67-bdfe-247708bab1d8 | -16.33326 | -52.94979 | 2025-09-07 04:21:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 02dbfb61-7afc-3ace-a374-ba51758c2973 | -12.77657 | -52.95518 | 2025-09-07 04:21:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2924886e-aa70-3994-bf9d-7c85d7fe2b4e | -18.49582 | -49.51549 | 2025-09-07 04:21:00 | NOAA-20 | CACHOEIRA DOURADA | MINAS GERAIS | Brasil | 3109808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 8c6aee84-d334-30ef-8102-891e09007e38 | -17.68429 | -43.54899 | 2025-09-07 04:21:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04b15ddb-41d6-3ef3-b90a-b1630fe5ed49 | -14.66177 | -46.81723 | 2025-09-07 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e67672b0-4306-31f9-9fbf-748d3fa6db25 | -13.90588 | -53.99137 | 2025-09-07 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01a1d0db-a5a4-3652-a74c-c3e563f1ec79 | -15.57061 | -43.85614 | 2025-09-07 04:21:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 04fe2288-3912-309e-b42b-e030176c4bed | -13.05433 | -48.06105 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91d8af6f-1099-3850-8c70-f077dbdfd8f6 | -13.04257 | -48.04727 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6e4e924-2a59-3748-b14a-7eb0d22bcf41 | -19.47653 | -47.76361 | 2025-09-07 04:21:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f829a18-83ad-3603-a028-836220537d8f | -13.02091 | -48.0512 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 855f0553-4546-3751-965c-be5cecce0400 | -15.70149 | -53.56217 | 2025-09-07 04:21:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7d2d2d07-1ab5-32ea-b610-99e6f21c0a7c | -16.63319 | -51.85756 | 2025-09-07 04:21:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fec0374b-e017-36fb-9245-42908839d923 | -17.86326 | -44.33706 | 2025-09-07 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b7fb6976-7b78-3d7c-967f-5d39c2c8294a | -17.48962 | -44.77505 | 2025-09-07 04:21:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 49524bea-7f34-3090-a4a6-8ed1a677171f | -15.70938 | -47.51001 | 2025-09-07 04:21:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe02aff7-562d-3e3f-b9fa-244a9e505611 | -16.93646 | -45.75003 | 2025-09-07 04:21:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb74cda7-59e7-3ddb-9328-0fc3e3d72c71 | -16.30834 | -45.69238 | 2025-09-07 04:21:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e8c15e8c-9230-3b4d-9090-9019f19c58f8 | -13.71382 | -46.88231 | 2025-09-07 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5f1d1eb1-3d37-315b-aa72-858dae630b67 | -18.35406 | -43.92381 | 2025-09-07 04:21:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb285e13-eb6c-3067-b127-a50277fadae6 | -15.83747 | -52.29787 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d58d1958-9040-3235-b2bf-68baefc98466 | -15.85402 | -48.12862 | 2025-09-07 04:21:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e4697c52-ad64-339c-b00f-6c9d57b82aa4 | -12.94368 | -54.77197 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 30.7 |
| a83f403d-4038-3782-a3b3-e38cd3634ae8 | -15.70167 | -53.56838 | 2025-09-07 04:21:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52b13b90-78ba-3c5f-bc57-b7a46dd2a804 | -19.89304 | -41.44013 | 2025-09-07 04:21:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 70a13436-4c2a-3092-9f13-ad3936e639de | -14.8486 | -46.68781 | 2025-09-07 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2ce9d9de-d931-3388-876d-dcb4a64f0965 | -14.78139 | -48.12081 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24ef5585-7360-3231-8e97-da749f9e690f | -13.0072 | -54.84316 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4486404a-f954-356c-858f-74455b60b470 | -13.91687 | -48.04368 | 2025-09-07 04:21:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a8f0cc4-5fc6-3fff-9f5d-02d301ee5ce3 | -14.49414 | -48.77305 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d0a6b35-bcf8-3cfd-aec0-dbbaf67d2251 | -19.48201 | -47.77208 | 2025-09-07 04:21:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 93204f51-176f-3587-a7cb-0e888bdca336 | -16.69098 | -46.80194 | 2025-09-07 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 590835cf-2fbe-3003-8227-6dd46b7428b0 | -14.81201 | -48.10308 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d80dd46c-1885-3dc7-9919-7f9e052a6fa9 | -14.55733 | -48.03339 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43b70b0b-1cf1-34f2-a3dc-d6b9d5725066 | -16.44847 | -49.28826 | 2025-09-07 04:21:00 | NOAA-20 | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21935f2a-88ce-39b6-90ac-8508c1a0cc8e | -13.05927 | -48.07365 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 64b7ef27-1086-3f77-8af7-dc05007a4475 | -15.35952 | -43.66797 | 2025-09-07 04:21:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README61.md)
