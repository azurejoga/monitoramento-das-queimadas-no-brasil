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
| bda753ad-a9d9-36b5-9a9f-6b64bd9fee0b | -6.04813 | -37.51295 | 2025-03-26 12:06:00 | TERRA_M-T | JANDUÍS | RIO GRANDE DO NORTE | Brasil | 2405207 | 24 | 33 | nan | nan | nan | Caatinga | 25.4 |
| a0c53ffe-131c-337e-846a-9faec6b39003 | -9.52413 | -37.31611 | 2025-03-26 12:08:00 | TERRA_M-T | OLHO D'ÁGUA DAS FLORES | ALAGOAS | Brasil | 2705705 | 27 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 489e124b-6cfa-3ecd-81ad-54fcaf2530a1 | -10.6208 | -40.21378 | 2025-03-26 12:08:00 | TERRA_M-T | FILADÉLFIA | BAHIA | Brasil | 2910859 | 29 | 33 | nan | nan | nan | Caatinga | 21.9 |
| 718b008f-e168-3f4f-a964-dfe67dbadd16 | -9.23063 | -40.52983 | 2025-03-26 12:08:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 14.5 |
| df493aa5-47a0-32e7-a25f-9db7fe07cc75 | -10.70797 | -38.88823 | 2025-03-26 12:08:00 | TERRA_M-T | QUIJINGUE | BAHIA | Brasil | 2925907 | 29 | 33 | nan | nan | nan | Caatinga | 20.9 |
| cf6f44c4-0584-338d-bf0a-9002295e05a9 | -9.2741 | -36.92413 | 2025-03-26 12:08:00 | TERRA_M-T | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 49.3 |
| d842e5b4-c7bd-358a-94ad-633b1d79f62e | -10.69823 | -38.88706 | 2025-03-26 12:08:00 | TERRA_M-T | QUIJINGUE | BAHIA | Brasil | 2925907 | 29 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 0da57390-80f0-3099-b1a3-ccd1c982a473 | -9.02095 | -40.24967 | 2025-03-26 12:08:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 6.0 |
| e0eda794-9583-397e-962b-4f9201c15fff | -9.47103 | -40.78487 | 2025-03-26 12:08:00 | TERRA_M-T | SOBRADINHO | BAHIA | Brasil | 2930774 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 45335112-dfc5-39c8-8e3f-2fe7b9bfaf29 | -10.79211 | -40.30757 | 2025-03-26 12:08:00 | TERRA_M-T | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| c732e347-8ed4-3f0a-9b30-eae1e8afb714 | -9.60595 | -41.64905 | 2025-03-26 12:08:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 15.5 |
| f5fced46-58b1-3ece-8fd4-33b45161bba1 | -13.47906 | -42.48997 | 2025-03-26 12:08:00 | TERRA_M-T | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 9eb2d570-dd5e-334d-bd82-d1e1e1d043e5 | -8.8499 | -44.18126 | 2025-03-26 12:08:00 | TERRA_M-T | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 068a6b45-ba3a-36ea-b391-ce1bb6df9d4d | -9.11781 | -40.73783 | 2025-03-26 12:08:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 6d820235-9516-38a4-9c2f-ac90c31e2b25 | -10.1314 | -37.99714 | 2025-03-26 12:08:00 | TERRA_M-T | CORONEL JOÃO SÁ | BAHIA | Brasil | 2909208 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 1e90d5d1-7ec5-3c10-95f5-6121448312a5 | -10.7908 | -40.31704 | 2025-03-26 12:08:00 | TERRA_M-T | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| f3a7ed8c-7a6b-3c85-bbc3-5434fbc38cde | -14.01449 | -41.31951 | 2025-03-26 12:08:00 | TERRA_M-T | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| c7e311a1-ad5f-32f5-af3a-f67de35188d4 | -9.5203 | -37.30934 | 2025-03-26 12:08:00 | TERRA_M-T | OLHO D'ÁGUA DAS FLORES | ALAGOAS | Brasil | 2705705 | 27 | 33 | nan | nan | nan | Caatinga | 10.3 |
| b9191969-4ead-392a-a8d6-9054daf7cb09 | -9.2368 | -40.02775 | 2025-03-26 12:08:00 | TERRA_M-T | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 7e2c56ce-d8da-3921-8104-99dd25ac5b8a | -10.59383 | -39.05497 | 2025-03-26 12:08:00 | TERRA_M-T | EUCLIDES DA CUNHA | BAHIA | Brasil | 2910701 | 29 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 6bce744f-822b-39b8-a560-ac9db9a2ead8 | -12.20591 | -39.30593 | 2025-03-26 12:08:00 | TERRA_M-T | IPECAETÁ | BAHIA | Brasil | 2913804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 443e6783-b8fc-3f5a-bcdd-5b3c3f22e81a | -8.56084 | -36.95894 | 2025-03-26 12:08:00 | TERRA_M-T | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 12.0 |
| fc66cbf7-d9fa-3e6a-8344-c5919c07dc3e | -12.20449 | -39.31678 | 2025-03-26 12:08:00 | TERRA_M-T | IPECAETÁ | BAHIA | Brasil | 2913804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 359f15f5-00e1-3dbf-85b6-1e6508351147 | -10.6626 | -40.11259 | 2025-03-26 12:08:00 | TERRA_M-T | FILADÉLFIA | BAHIA | Brasil | 2910859 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 11a81aff-31b7-3647-b1c8-7125202221e9 | -17.07081 | -39.55343 | 2025-03-26 12:10:00 | TERRA_M-T | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| c94d549b-4317-3a85-b5db-5fe7970d2fff | -14.81234 | -39.27224 | 2025-03-26 12:10:00 | TERRA_M-T | ITABUNA | BAHIA | Brasil | 2914802 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| ac7e3995-da08-3163-86c2-8102f310fbe5 | -17.32335 | -39.56788 | 2025-03-26 12:10:00 | TERRA_M-T | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| ab64963b-ecf5-3623-8d88-f6e6ddaee323 | -17.07235 | -39.54107 | 2025-03-26 12:10:00 | TERRA_M-T | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 669a0696-54aa-3198-b1f1-1722ad456273 | -15.34299 | -42.10215 | 2025-03-26 12:10:00 | TERRA_M-T | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 39.2 |
| 24035c58-3ca1-307f-ab68-c94b69209e5f | -17.93601 | -39.80489 | 2025-03-26 12:10:00 | TERRA_M-T | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| edb46992-a229-39bd-902c-26a195bae905 | -15.52492 | -41.25672 | 2025-03-26 12:10:00 | TERRA_M-T | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| d63c0bc2-6a27-3904-abe9-bf02516befe0 | -15.34428 | -42.09297 | 2025-03-26 12:10:00 | TERRA_M-T | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 3c26741d-3dd6-35f4-9942-84f8f4f03c34 | -9.1113 | -38.162 | 2025-03-26 13:00:00 | GOES-16 | TACARATU | PERNAMBUCO | Brasil | 2614808 | 26 | 33 | nan | nan | nan | Caatinga | 150.4 |
| fab26499-e836-34b4-9862-9c8034c34a98 | 3.9662 | -61.5246 | 2025-03-26 13:10:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 55be2078-86c5-3289-b622-320e1ae7f345 | 3.9662 | -61.5246 | 2025-03-26 13:50:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 82.7 |
| e31062e0-0dac-3baf-baa5-0bb54a00e9c3 | 3.9662 | -61.5246 | 2025-03-26 14:00:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 58b77322-42f5-36c1-8625-98e01b23ca6f | 3.9662 | -61.5246 | 2025-03-26 14:10:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 01349874-f329-3f8e-a8fe-88405431beef | 3.9662 | -61.5058 | 2025-03-26 14:10:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 67.0 |
| a10744a5-154d-347a-8b41-3766edbbed31 | 3.9662 | -61.5058 | 2025-03-26 14:20:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 6943eee8-c14b-3d26-9f42-21c5125042be | 3.9662 | -61.5058 | 2025-03-26 14:30:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 69.3 |


