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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 079689e9-16cb-3528-85ab-a8b2092f84d0 | -8.10569 | -43.13124 | 2025-03-25 03:42:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 41a86214-02b7-37b7-b0a2-393d44fc2832 | -7.22594 | -44.77058 | 2025-03-25 03:42:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e32dcb26-d956-3be2-8bea-97a87a77327f | -5.99753 | -44.61194 | 2025-03-25 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b2a6f71e-b87c-3f07-aba4-c18ea29c1ce7 | -3.42252 | -43.16722 | 2025-03-25 03:42:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a5af5c2f-7040-37b6-96ef-c38e873dee60 | -3.78692 | -41.59937 | 2025-03-25 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2e04fd0c-0a2d-3d01-a233-349d86744244 | -6.39427 | -37.39615 | 2025-03-25 03:42:00 | NOAA-21 | SÃO BENTO | PARAÍBA | Brasil | 2513901 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 76787123-b1b1-3b9b-8f7d-254ab2fc708f | -5.63354 | -44.31924 | 2025-03-25 03:42:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d39ea4e4-3900-387a-87bb-854c94fd2695 | -7.2235 | -35.78933 | 2025-03-25 03:42:00 | NOAA-21 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8218e656-e90d-33fa-9ff8-d077354341fa | -7.03856 | -44.37135 | 2025-03-25 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f58407eb-38be-3df8-b492-9d15eedd3acf | -3.78233 | -41.59858 | 2025-03-25 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f2fe498a-0527-30f0-bfe3-5f823a710440 | -7.06984 | -35.05215 | 2025-03-25 03:42:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2894153e-c659-3ead-90c7-7ebc28d1e88e | -7.07261 | -35.05613 | 2025-03-25 03:42:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ca1474c1-f23f-3088-9fe6-b407403f580b | -5.97656 | -39.6718 | 2025-03-25 03:42:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| a2ca3fe5-f87e-38ce-a403-e7c0711fc865 | -9.64418 | -37.89332 | 2025-03-25 03:42:00 | NOAA-21 | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0b7105aa-b94d-3991-9d87-0f8ce350e295 | -8.10658 | -43.12613 | 2025-03-25 03:42:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6fa508b7-3826-3d4b-8371-428c161b8c36 | -7.04379 | -44.37244 | 2025-03-25 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91e13cb8-e2e6-33ef-ae93-f714eb10b201 | -8.36678 | -36.45504 | 2025-03-25 03:42:00 | NOAA-21 | BELO JARDIM | PERNAMBUCO | Brasil | 2601706 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7fdc48a3-1e7d-3e66-937e-472796ca7a4f | -7.26613 | -35.88488 | 2025-03-25 03:42:00 | NOAA-21 | CAMPINA GRANDE | PARAÍBA | Brasil | 2504009 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4adcb7e5-0acf-304f-bdc0-e449e86e6920 | -8.11134 | -43.12691 | 2025-03-25 03:42:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ecfce5ea-b0aa-31d7-871c-a11d41c2bb9b | -4.01391 | -41.79514 | 2025-03-25 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6526a956-67cc-3239-a876-cd6c846030d6 | -8.87884 | -36.53022 | 2025-03-25 03:42:00 | NOAA-21 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c7b12e69-a6da-3e8a-a0bb-ecb47076bd4d | -3.78611 | -41.60421 | 2025-03-25 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e6c3c078-38da-33ce-b5b9-20e780f1054a | -5.63296 | -44.32261 | 2025-03-25 03:42:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 76c119b7-abcb-318e-a558-aadd76b4efac | -3.78152 | -41.60341 | 2025-03-25 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 884e20d7-53f0-34bb-b72c-f1646fb6d04c | -7.07315 | -35.05267 | 2025-03-25 03:42:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1e1510ab-c5f7-33d9-9586-9523b5011925 | -15.51075 | -42.60225 | 2025-03-25 03:45:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b228433a-1eff-36a9-92c8-130cc829aa79 | -15.51011 | -42.60588 | 2025-03-25 03:45:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| aff0aa2d-efbe-3f61-9c1b-a818d4dabd38 | -12.86258 | -38.36698 | 2025-03-25 03:45:00 | NOAA-21 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7fd41f6d-3cee-3af4-8b3a-87355ee9c483 | -16.03862 | -43.72555 | 2025-03-25 03:45:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d6b5e9c-f0ee-3b5d-9419-7d16d96b84e6 | -11.78654 | -40.92772 | 2025-03-25 03:45:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d1cb5f3e-a509-3fef-bd4d-7d7ee1dd1b98 | -11.90333 | -41.61369 | 2025-03-25 03:45:00 | NOAA-21 | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c15da909-ffcc-3bdf-b47d-c309e5dc4aaa | -16.03784 | -43.72976 | 2025-03-25 03:45:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6ace7628-ba3e-3336-97f0-d3ff676bcd50 | -17.05585 | -39.22221 | 2025-03-25 03:45:00 | NOAA-21 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1d9be324-8132-3210-9eff-80d3b429dd04 | -15.08549 | -39.02292 | 2025-03-25 03:45:00 | NOAA-21 | ILHÉUS | BAHIA | Brasil | 2913606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ff90d9fa-9b81-351d-91e1-59bd1408c46e | -17.86435 | -39.86127 | 2025-03-25 03:47:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| 1c1db92d-b75e-311a-8cc1-2bd0e55141c0 | -17.85886 | -39.85307 | 2025-03-25 03:47:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 28.7 |
| b33c9e39-f08c-365c-bbcf-42bcfc31ba58 | -23.33919 | -46.7747 | 2025-03-25 03:47:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8900270e-1b97-3f56-963e-2dee6e4aa6e8 | -23.40434 | -46.5548 | 2025-03-25 03:47:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d5d83324-0d6c-36e5-a075-5960a755c012 | -17.86907 | -39.85416 | 2025-03-25 03:47:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 614bf96e-0e0b-3986-b684-1353526dee44 | -17.86712 | -39.86578 | 2025-03-25 03:47:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 47.5 |
| 040cc109-1b01-3a42-9867-995e286fe9df | -17.865 | -39.8574 | 2025-03-25 03:47:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| ae0479cd-b126-353f-92d0-a87887fb3971 | -17.55662 | -40.64093 | 2025-03-25 03:47:00 | NOAA-21 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| f0f7f422-c6df-3164-9baf-89484338bb68 | -17.85608 | -39.84859 | 2025-03-25 03:47:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| 0fc602ed-7cd4-3f81-aa27-a10ab8a13e64 | -17.55732 | -40.63683 | 2025-03-25 03:47:00 | NOAA-21 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 59c29534-3378-3772-be06-0d5258fe1603 | -17.85822 | -39.85695 | 2025-03-25 03:47:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 3f4836d8-c1f8-3771-bc17-4622bf560453 | -17.8548 | -39.85633 | 2025-03-25 03:47:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 24.7 |
| ceccc4fa-9e9c-35d1-b956-91ae52aa36fd | -17.85544 | -39.85246 | 2025-03-25 03:47:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| 1585aa73-5cc6-3251-acc3-fd8312725e6c | -17.85694 | -39.86471 | 2025-03-25 03:47:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 212b8e5b-1908-3cc5-8f93-da2e82bbdff0 | -17.8637 | -39.86515 | 2025-03-25 03:47:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 3bb6a60e-bcc7-3ff3-82f3-b0bd3b2ee4da | -17.85266 | -39.84798 | 2025-03-25 03:47:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| ba2e6ea6-a4b2-3871-a4d9-7395836bbb86 | -17.87119 | -39.86253 | 2025-03-25 03:47:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 37.2 |
| 4ad19d0c-1695-3906-b9e0-3f0971c93353 | -17.55944 | -40.64573 | 2025-03-25 03:47:00 | NOAA-21 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| be530da5-c1c4-33eb-a5e1-41ffaebea264 | -17.86036 | -39.86533 | 2025-03-25 03:47:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| a36f4453-4b1d-387e-9140-5228a8166072 | -22.78677 | -43.75743 | 2025-03-25 03:47:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| fe766261-d0a6-384a-a15c-28acb6fab9fd | -17.56015 | -40.64161 | 2025-03-25 03:47:00 | NOAA-21 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c9fc4a56-921d-3b9b-a95a-1e2f3deb78f4 | -17.87054 | -39.86641 | 2025-03-25 03:47:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 47.5 |
| 1f6944b4-8925-365d-a167-b4fab75200e9 | -17.86842 | -39.85803 | 2025-03-25 03:47:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 37.2 |
| 857924bc-3909-3d1b-b54f-67da1b504bd9 | -17.85416 | -39.86021 | 2025-03-25 03:47:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 24.7 |
| 0cfc36b6-49ee-3102-8663-9b606911d92e | -16.68083 | -43.88533 | 2025-03-25 03:47:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ced77d1-c4dd-3644-91db-4ff984095c29 | -17.87184 | -39.85866 | 2025-03-25 03:47:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 37.2 |
| cbb9624c-4c51-3e9d-b9f2-fbba96b52821 | -17.86028 | -39.86453 | 2025-03-25 03:47:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 39d2a02d-7fa8-3dc4-9b00-9c0f00a6790c | -17.85202 | -39.85185 | 2025-03-25 03:47:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| 01606227-ceea-3d06-8eea-4e5aa8c9fa59 | -17.85758 | -39.86083 | 2025-03-25 03:47:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 07bb6068-92fe-3b62-a69a-80eadf6fa4aa | -18.0402 | -39.92524 | 2025-03-25 03:47:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 163ab2e0-8f4d-3cea-91b9-2934a252aeef | -22.90102 | -43.75293 | 2025-03-25 03:47:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 5bf099a6-633f-3ca3-a787-fe640c1852b6 | -17.86777 | -39.8619 | 2025-03-25 03:47:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 37.2 |
| 08fee278-0b2d-3265-9217-4db754858b6d | -23.40684 | -46.55696 | 2025-03-25 03:47:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cccff02e-84e6-329d-b31b-5c2554988466 | -17.86566 | -39.85353 | 2025-03-25 03:47:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 38daeb2c-e369-3278-ae23-93831c883f56 | -19.71651 | -40.35295 | 2025-03-25 03:47:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| de2be16e-099c-3a33-b5f4-d3753a8d091a | -23.98386 | -48.91537 | 2025-03-25 03:49:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1e04478-0fed-3c56-a2f7-330b5d5e69df | -23.98313 | -48.9186 | 2025-03-25 03:49:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef10cded-1d9b-3ea1-8e9c-4426a1986844 | -23.98144 | -48.91763 | 2025-03-25 03:49:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d3281fa0-abd3-3cbb-b642-ab2bd500eeed | -23.98655 | -48.91887 | 2025-03-25 03:49:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 31402ef4-387c-3d68-891d-8174b5156f23 | -17.8666 | -39.8386 | 2025-03-25 03:50:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 108.8 |
| eae61aeb-222e-3d92-ac97-48fc3133cb52 | -17.8455 | -39.8705 | 2025-03-25 03:50:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 82.9 |
| 69ed33c4-180c-37cb-b6fd-74d3638edebf | -17.8658 | -39.8648 | 2025-03-25 03:50:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 203.4 |
| 41297c15-d61d-3352-a9d0-219508e6ab6f | -17.8455 | -39.8705 | 2025-03-25 04:00:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 87.2 |
| 1b2b248c-1ff0-3b62-ba98-587e19cb4bca | -17.8658 | -39.8648 | 2025-03-25 04:00:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 186.7 |
| 9c580579-b699-32f7-9dda-ca4a02b0c175 | -17.8666 | -39.8386 | 2025-03-25 04:00:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 111.0 |
| b4b11121-9833-307f-8de1-8b0f31105e9f | 4.6634 | -60.9225 | 2025-03-25 04:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 3305cb4e-8c1d-390c-8282-d6322b5d93fe | -17.8463 | -39.8443 | 2025-03-25 04:00:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 83.6 |
| a649daa6-4a9e-3493-9399-9e5fd0ed348b | -5.97715 | -39.67119 | 2025-03-25 04:06:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 989184e7-eb8c-378d-9426-40aab6c475f8 | -3.78215 | -41.60092 | 2025-03-25 04:06:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 42640f4d-cbd9-32e5-8c5f-560a5d17c077 | -5.97375 | -39.67067 | 2025-03-25 04:06:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1848c8c2-0d1c-30a5-b427-9bc7fe87b2f3 | -3.41918 | -43.16624 | 2025-03-25 04:06:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c30d9ce8-db36-30c0-8a8e-e28a4b21b4a9 | -3.12029 | -40.99194 | 2025-03-25 04:06:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 55112771-7300-31bc-a425-b9a861553a18 | -4.81823 | -42.98813 | 2025-03-25 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c07c327d-adca-3c31-bbdc-43e5b97caf7a | -3.78159 | -41.60442 | 2025-03-25 04:06:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a072b364-8976-3a1d-a744-86f9cd4c45fc | -4.01291 | -41.7923 | 2025-03-25 04:06:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d42d48ef-9d95-33cc-8ba2-c64a8583c977 | -4.81479 | -42.98759 | 2025-03-25 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91c53ad4-ec04-3d12-8c30-666f5ee028bb | -3.78548 | -41.60145 | 2025-03-25 04:06:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3be5d5f3-91e5-32c2-bf44-8f6b4b5b4036 | -3.42269 | -43.1668 | 2025-03-25 04:06:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1d2716d3-f508-3854-9c8e-46c6b4fa1fda | -7.06966 | -35.0539 | 2025-03-25 04:08:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| a93d5259-39a7-382d-8d4b-1fb2c1e510c2 | -8.10421 | -43.13037 | 2025-03-25 04:08:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 93e84fc9-d082-37b6-9b21-cee824f5a1d3 | -8.10084 | -43.12983 | 2025-03-25 04:08:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 799329fb-cb15-3eb5-ac36-391d484e43f0 | -7.22174 | -35.78993 | 2025-03-25 04:08:00 | NPP-375D | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 63462a15-1763-3384-95ce-3c8f935be0c8 | -11.9288 | -40.41259 | 2025-03-25 04:08:00 | NPP-375D | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ba4186c3-abec-3851-9f0a-78014a8a3dd0 | -5.99823 | -44.61473 | 2025-03-25 04:08:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 11b3d968-e706-3161-b2f6-32e0915b4ba2 | -5.42021 | -45.26239 | 2025-03-25 04:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a2cfc14-1c70-3a08-b86d-7d4cb87f615e | -9.64056 | -37.89181 | 2025-03-25 04:08:00 | NPP-375D | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 2.3 |


[Clique aqui para ver as próximas entradas](README4.md)
