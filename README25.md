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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92744f88-87a2-3ca4-bcfb-240f80388966 | -15.67583 | -46.63118 | 2025-10-12 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| eccb08fe-5157-3a56-8b0b-ccb515f157a4 | -19.51391 | -43.04589 | 2025-10-12 04:17:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| bc79d1d6-99b7-3850-8d0b-d6a2b3432cdd | -15.68195 | -46.63591 | 2025-10-12 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df8ee152-460d-3043-a1f4-b79155927a98 | -14.93927 | -46.74549 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d906b463-ac6f-3e7a-a04b-d4acfbf3251b | -14.9479 | -46.73511 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2f643a33-aa24-39bc-9146-cc35028a183f | -14.94051 | -46.73785 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1d83ff1c-45ff-377e-b720-11897d7cf5eb | -15.29718 | -46.29893 | 2025-10-12 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11f6b281-6772-3424-8a47-ebcb26966e3d | -18.57082 | -50.59969 | 2025-10-12 04:17:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7adc31be-0e65-328e-a2c0-a279a0d090cf | -15.23232 | -56.87436 | 2025-10-12 04:17:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 45c823f7-922c-3f71-981f-a90f67a9ca9b | -17.3607 | -46.65751 | 2025-10-12 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f1c53b4-bcbb-3ff5-9a48-08a0423086f7 | -17.40848 | -46.86987 | 2025-10-12 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2aec5a47-b5f0-378b-ae1f-1fa57111140e | -12.22067 | -43.79601 | 2025-10-12 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b60f3200-db5d-3d70-8cc0-458d853d6fd7 | -18.46122 | -43.48668 | 2025-10-12 04:17:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f0c8eacb-a8a3-35d3-b2d1-5d515771e8fc | -22.33486 | -49.86696 | 2025-10-12 04:17:00 | NOAA-21 | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 200eb561-1d40-3d72-94f0-80f05320e570 | -14.40314 | -48.01313 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 22.7 |
| c0b010d6-9ba3-3620-98a1-6215bb2fc070 | -15.66794 | -46.63727 | 2025-10-12 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ac962a8e-59e2-3a34-b829-3ab63838d09a | -15.36055 | -44.15807 | 2025-10-12 04:17:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c27b51c3-0850-300e-a2b5-71766f762ea2 | -19.5339 | -43.05194 | 2025-10-12 04:17:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 78c5f101-e7b3-3e1f-bbda-c2cddc952735 | -17.25583 | -52.26811 | 2025-10-12 04:17:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c0fd1394-cb65-38dd-bf54-f1e498800c07 | -19.53175 | -43.04876 | 2025-10-12 04:17:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.0 |
| 00b22414-7440-313b-891c-8f93110b5d41 | -14.8963 | -48.50275 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d58774d1-cc55-34c3-a628-4e081781ff78 | -15.22202 | -46.38747 | 2025-10-12 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| beff9018-67eb-36d3-ad75-e234b49b86f4 | -15.22636 | -56.87058 | 2025-10-12 04:17:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 817e7dbb-8ade-3d84-adce-5ae54fa579be | -18.58612 | -50.58153 | 2025-10-12 04:17:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 165986df-a7b4-37f7-8af6-a5ce0d578198 | -17.18312 | -46.9365 | 2025-10-12 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7cb2a2ef-e267-3a98-9284-81d327b70536 | -18.40519 | -46.38932 | 2025-10-12 04:17:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 714c3d43-7142-3c7a-b954-9989c0fb1f0d | -17.20127 | -45.86787 | 2025-10-12 04:17:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 43c54e37-312c-3309-a2cd-1ee5353138a2 | -14.40668 | -48.01392 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7abb922b-dc79-3146-be89-dff4c5f46507 | -19.53057 | -43.05712 | 2025-10-12 04:17:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| a85ec894-fc19-341a-bce9-3d857be3c193 | -14.90368 | -48.4817 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9cb36bd7-5f9e-3696-bd8c-df38cf6f2993 | -15.46646 | -55.94557 | 2025-10-12 04:17:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 10c8c6b2-3a15-3cb2-830e-ed87b1229cf1 | -11.85893 | -56.86462 | 2025-10-12 04:17:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aa375fb3-d5d1-36a1-9f3e-c410222c8c82 | -14.93312 | -46.74058 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 39b8910e-fe87-3ed1-890b-7cbc92b82f1f | -14.90403 | -48.5229 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7530c51-0cc2-308a-88ce-85a208c154bf | -15.29245 | -46.13764 | 2025-10-12 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e59b2b1-c902-3c35-8402-a93ff8779595 | -16.73641 | -43.97766 | 2025-10-12 04:17:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d21d813-3dec-3702-92cf-f9a3aed5e5a8 | -13.98895 | -54.89966 | 2025-10-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d68a081-4673-3434-9c35-ee101bfe79c2 | -17.21322 | -47.6534 | 2025-10-12 04:17:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5596f48e-5487-32f0-8c64-1c67148d875a | -15.68985 | -46.62976 | 2025-10-12 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d381d6b7-7f2c-334b-9a96-dae8c9409851 | -17.26358 | -46.9009 | 2025-10-12 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b4fe418-b8e4-39c6-8684-89feb1376dfa | -19.7794 | -42.39157 | 2025-10-12 04:17:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 5dc84392-2401-30d7-b1b6-be29e8b621ea | -14.96782 | -46.72748 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 7c0f9f17-91a8-35f9-bf95-6ef23ceb66a9 | -14.41807 | -47.96343 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0e440ad-47f5-3697-828f-ae0350ee4635 | -15.67246 | -46.63068 | 2025-10-12 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 20c45067-921c-31be-ba30-20f1691776f1 | -14.89721 | -48.47598 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2d240f4f-489c-30ab-b48c-c58dba5835d0 | -14.9012 | -48.51765 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7688b279-761c-31f5-a077-bcb5325fd4a1 | -19.53032 | -43.05143 | 2025-10-12 04:17:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| b0797e23-7463-3f91-bf9c-d13629c7808c | -15.6713 | -46.63786 | 2025-10-12 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 83eb2508-d7a4-3681-b2e9-af4fa1743b9b | -16.19395 | -43.66972 | 2025-10-12 04:17:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3608005d-1e17-3fa1-9f2f-c7c1da5d96d5 | -18.07243 | -42.99686 | 2025-10-12 04:17:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 456ba4b2-d5f4-3da0-956a-7b8e7225c0f1 | -15.28303 | -57.08593 | 2025-10-12 04:17:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca3e2430-0501-31ae-a8fa-14588512f5c5 | -14.96995 | -46.7356 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8783a2a4-a80a-3797-8c5d-257c797bb694 | -14.91747 | -46.77268 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fb69709a-4238-3692-8109-39ee14fb83c9 | -12.22122 | -43.79247 | 2025-10-12 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06117624-f071-3c78-9c38-059c1be84f71 | -15.68434 | -46.62127 | 2025-10-12 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26e6c7e4-9fec-345c-888a-f410d537f04d | -14.40236 | -47.97397 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fa05518d-4841-3996-8ab2-d0ab3d4e75cc | -17.87206 | -45.02969 | 2025-10-12 04:17:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2e542e90-05fc-3351-a21a-b874d2ee7a27 | -22.33061 | -49.87034 | 2025-10-12 04:17:00 | NOAA-21 | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 4662a177-18f1-3465-be8b-f210963cdeb9 | -15.23146 | -56.87658 | 2025-10-12 04:17:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ecfb517d-141f-3353-971f-5fc8ee3b579a | -15.2891 | -57.08395 | 2025-10-12 04:17:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4268fc5a-fe23-3d61-a588-4e7e18268461 | -16.83148 | -41.88029 | 2025-10-12 04:17:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f165c878-d16f-3be4-a420-069d81b8ba44 | -14.4066 | -47.97056 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cac067b7-b233-3625-b40f-7e47cef5529e | -14.95772 | -46.7256 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| da45f0da-8072-30be-86e0-bb5256c5d740 | -15.49993 | -47.99781 | 2025-10-12 04:17:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1e5f40fe-9b97-3153-9d7f-50bcc8352741 | -19.78277 | -41.75674 | 2025-10-12 04:17:00 | NOAA-21 | IPANEMA | MINAS GERAIS | Brasil | 3131208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0bdd5736-6917-3398-8b5e-f90c64a7e55e | -14.02185 | -43.48835 | 2025-10-12 04:17:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f275c9d0-32e8-376f-aa20-2bb690f41317 | -17.36343 | -46.66176 | 2025-10-12 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e4e00f74-c3df-32cf-82d9-3037938302ba | -15.19288 | -44.50002 | 2025-10-12 04:17:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d7bfdd3-8402-37ad-9120-afc1e94f5aa0 | -17.25021 | -52.27319 | 2025-10-12 04:17:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 244ce156-f69e-3fde-af86-ae10c59343d0 | -14.96721 | -46.73117 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 77ee3a12-82ea-3f2c-8258-70233f84519c | -13.41632 | -42.71409 | 2025-10-12 04:17:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c0fcf4e2-c610-3576-bc6c-0271c11841b4 | -19.5309 | -43.04718 | 2025-10-12 04:17:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 4bf1c7cc-d736-354d-89c5-2d21a6726310 | -17.19764 | -47.32373 | 2025-10-12 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60c8ede7-6aee-3d5d-a91c-98acc3171831 | -17.40635 | -46.86185 | 2025-10-12 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 137a923f-c6c7-337d-ba93-47b518fd39af | -15.68097 | -46.62078 | 2025-10-12 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2fa33389-1094-3c0b-92aa-a12139332d05 | -18.40188 | -46.38874 | 2025-10-12 04:17:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ec182bd-57fb-33ce-93ca-f2cf3bb0974d | -15.18957 | -44.49948 | 2025-10-12 04:17:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ec06eb6-1d6f-3369-a689-3a16eca45ee9 | -19.52975 | -43.05562 | 2025-10-12 04:17:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 657bc492-1d53-3d4a-8289-c81fa43099b8 | -19.04911 | -57.54649 | 2025-10-12 04:19:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 84561ba2-5182-3547-a4a9-f3299ba1951e | -19.03737 | -57.54367 | 2025-10-12 04:19:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 3a628b7b-838c-3263-9325-0758f8f303e6 | -19.04811 | -57.55101 | 2025-10-12 04:19:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 09f2648a-c88a-3eb8-8abd-47c042685637 | -19.02664 | -57.53635 | 2025-10-12 04:19:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| cc36f5b4-c61a-3087-8257-f4283ef92de2 | -19.03251 | -57.53775 | 2025-10-12 04:19:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| ad5abedf-27a2-36f2-88b7-ee83cb201a44 | -19.0315 | -57.54227 | 2025-10-12 04:19:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 0203e358-9fb0-3815-919c-c84d971e569f | -19.01976 | -57.53944 | 2025-10-12 04:19:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 76bcbf5b-271c-314b-8228-3d617384b231 | -17.94246 | -57.62812 | 2025-10-12 04:19:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 8465a5b4-2f6d-34c1-b785-babd37f990d6 | -17.82462 | -57.66974 | 2025-10-12 04:19:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 94668820-e2c6-32c4-9da3-512151689914 | -19.04324 | -57.54509 | 2025-10-12 04:19:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| cf5d5b16-9fa2-302f-861c-c3a88d142228 | -19.86246 | -45.83785 | 2025-10-12 04:19:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f924276b-2ea4-3a18-94c2-aee649d7d400 | -17.94847 | -57.62967 | 2025-10-12 04:19:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 1dbbe592-f0ae-3f95-a4c3-d478537eeef6 | -17.82101 | -57.62868 | 2025-10-12 04:19:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a2510e77-9b66-353f-bdef-804014f3c2fc | -19.04223 | -57.5496 | 2025-10-12 04:19:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| b46d5356-708a-3a08-b5b7-3a9421165405 | -19.05498 | -57.54791 | 2025-10-12 04:19:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| cf36223b-1d16-3595-a8c3-6f90d611d7e4 | -17.83174 | -57.66635 | 2025-10-12 04:19:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 1bb7912d-4bbe-35c5-ae2e-39a943f7f267 | -21.10297 | -47.10411 | 2025-10-12 04:19:00 | NOAA-21 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9c2bfa24-fd7c-3366-bcd3-cf9f72735853 | -19.03839 | -57.53914 | 2025-10-12 04:19:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| a736e88f-1c0b-38db-b339-08afb32524a4 | -19.02563 | -57.54086 | 2025-10-12 04:19:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 54413206-dbfe-3a62-8096-543dcd5bf216 | -19.02077 | -57.53493 | 2025-10-12 04:19:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| a0e9a5e7-12dc-33af-9cce-d6347c9d6249 | -19.02462 | -57.54537 | 2025-10-12 04:19:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 2feb8fe4-cd6e-3feb-aa1d-a4da18b664d8 | -17.81885 | -57.66703 | 2025-10-12 04:19:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |


[Clique aqui para ver as próximas entradas](README26.md)
