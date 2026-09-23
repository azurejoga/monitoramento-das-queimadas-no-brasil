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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0eb1d08b-0409-3f10-adcb-73cf4457abff | -3.6764 | -60.5649 | 2026-09-23 01:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 5a9fb4dc-6fff-31ba-9240-28145f58e73b | -6.6816 | -55.0502 | 2026-09-23 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 2b82ef81-ac52-385c-9705-a8b31b924de8 | -14.6497 | -45.6367 | 2026-09-23 01:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 66.5 |
| b789683e-00ee-3007-be0e-0afb57455be3 | -1.9271 | -58.2587 | 2026-09-23 01:40:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| b6e12a19-4eca-3ebc-a7a2-b017e0faf96a | -6.0925 | -57.6847 | 2026-09-23 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 96f34c4f-19e3-3433-9078-f2d670beb518 | -6.6145 | -59.9464 | 2026-09-23 01:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| e3d49cb9-a96e-32a0-aa6b-f73ebef750d5 | -8.935 | -61.495 | 2026-09-23 01:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 1360e64d-4c7b-37db-aa30-9dced763458e | -11.5311 | -45.3323 | 2026-09-23 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 749429da-fd0f-3d91-9b09-243ef8d30167 | -11.6919 | -50.7699 | 2026-09-23 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| f58ce268-23ec-3993-9e6d-a20b380a8d86 | -3.2129 | -46.9383 | 2026-09-23 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| c5d70b65-47da-3cab-8d8d-20d5b8823538 | -12.4216 | -46.9551 | 2026-09-23 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 111.6 |
| c2306e65-dc9d-3d09-b3f8-85fadfc136e6 | -6.6815 | -55.0703 | 2026-09-23 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 36fe9d4f-6d7b-3de3-9053-fe723f330089 | -6.6148 | -59.908 | 2026-09-23 01:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 537862d4-583b-3953-9c44-ede8b58c579e | -3.6763 | -60.5839 | 2026-09-23 01:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 6e8ede3a-bff9-3685-addb-d9949bc88f43 | -6.61 | -43.83 | 2026-09-23 01:45:00 | MSG-03 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c9c828e1-edf2-323b-a27e-4e8e032b6d1b | -6.61 | -43.79 | 2026-09-23 01:45:00 | MSG-03 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 23c100a6-6f2b-3609-8cec-b71e1728b844 | -8.8 | -44.28 | 2026-09-23 01:45:00 | MSG-03 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6dd57d92-1058-3cc2-b351-ada3d074ca1e | -6.61 | -43.92 | 2026-09-23 01:45:00 | MSG-03 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26d3b86c-c3d5-31ec-b161-6b75c8fdab5f | -8.83 | -44.29 | 2026-09-23 01:45:00 | MSG-03 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3fd30a07-6345-3bd5-a7c7-0022b2c8335e | -6.61 | -43.88 | 2026-09-23 01:45:00 | MSG-03 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 43929332-d811-38f0-bb91-08ba29162978 | -6.61 | -43.7 | 2026-09-23 01:45:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2073ee71-82ea-380d-85ea-e9f3a3341d77 | -6.58 | -43.74 | 2026-09-23 01:45:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fd847b97-7e2a-365a-9e89-8bd6a7f1524e | -6.58 | -43.69 | 2026-09-23 01:45:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 76fa4368-576a-3413-9aa4-3d6ad174602e | -8.8 | -44.24 | 2026-09-23 01:45:00 | MSG-03 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cc5d1e00-0e96-3807-a5b1-5d4cc513522f | -3.23 | -46.93 | 2026-09-23 01:45:00 | MSG-03 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6017f56c-218e-35f3-a7b6-faa18ca0f0c0 | -6.58 | -43.83 | 2026-09-23 01:45:00 | MSG-03 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ba903979-cbca-33ef-a171-677171206f7d | -6.58 | -43.78 | 2026-09-23 01:45:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4818f4fa-f8c4-395a-9904-3318dcee8b6b | -6.61 | -43.74 | 2026-09-23 01:45:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e12906a8-ee6f-3d63-8861-880edec2621d | -6.64 | -43.75 | 2026-09-23 01:45:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6e577cc0-3ae6-396e-a846-62ddfe2257ce | -11.5311 | -45.3323 | 2026-09-23 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| b7662f8c-1d6e-3338-b4a9-fac1ff02d022 | -9.1025 | -61.4299 | 2026-09-23 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 94d28451-b8b0-3bca-9f2e-e48d2872dfd2 | -12.1192 | -45.6368 | 2026-09-23 01:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 20c16064-58b5-3fdf-b6aa-e1352d6c774f | -3.2129 | -46.9383 | 2026-09-23 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 44fa7e3a-cd9a-3aec-9331-bc617e9b0a55 | -1.9271 | -58.2587 | 2026-09-23 01:50:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 83.1 |
| b74d72f9-7553-328b-9d2d-b32c371c0c4f | -6.6315 | -43.7533 | 2026-09-23 01:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 190.5 |
| c0521109-2a62-3df3-a68a-89016fb6a234 | -5.7567 | -45.1067 | 2026-09-23 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 5a148fbd-a151-332b-a7b4-77d2eb6c3ddc | -6.5939 | -43.7565 | 2026-09-23 01:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 28.6 |
| efcdb3ad-3fb4-37e5-a0ef-7ac0bfa3b619 | -12.129 | -50.8049 | 2026-09-23 01:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 153.5 |
| aea659c6-fc4d-31ce-94b5-db334ec24716 | -3.8648 | -58.8211 | 2026-09-23 01:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 18ea46ce-ce6d-384d-93c3-73ad6af8c5d3 | -11.8871 | -45.7623 | 2026-09-23 01:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 180.9 |
| c038bbda-1415-3b7a-8e5a-733115ae02a3 | -12.1478 | -50.824 | 2026-09-23 01:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |
| f901e0dc-f49d-3fb9-902a-3204da64f28d | -6.6127 | -43.7549 | 2026-09-23 01:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 269.2 |
| 04aeef22-265e-3335-b678-3a0a30aa4262 | -6.0925 | -57.6847 | 2026-09-23 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 734cda2e-4e95-3265-a1cc-3630ecd90193 | -5.6246 | -45.2518 | 2026-09-23 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 502a3839-7ee4-3e21-b0fc-023663f3b243 | -3.6764 | -60.5649 | 2026-09-23 01:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 9127c7c6-9676-330c-bd47-6d11ec8b7b07 | -11.5307 | -45.3553 | 2026-09-23 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 4f895139-3bf6-3e09-8ee3-1b3c32f82edc | -9.1024 | -61.4491 | 2026-09-23 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 9879728e-c85b-3577-a57c-9cebea135448 | -6.6815 | -55.0703 | 2026-09-23 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| d2b8da91-f0ab-322d-afe6-03ba5d627029 | -11.9059 | -45.7824 | 2026-09-23 01:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 54.0 |
| c4692878-d2ad-32a4-b65a-cda13d3a20d4 | -8.9165 | -61.4767 | 2026-09-23 01:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 57.3 |
| fe3fb346-74aa-3959-8466-85d2c8eeda16 | -3.6946 | -60.5835 | 2026-09-23 01:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 88f55baf-25c7-347a-bac1-5e566880879a | -6.6145 | -59.9464 | 2026-09-23 01:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 13b03a23-0384-30ef-8c9c-ae351c7313c2 | -12.1385 | -45.6339 | 2026-09-23 01:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 64.4 |
| f169290e-9afb-37a4-9ad4-351002965f04 | -6.6129 | -43.7317 | 2026-09-23 01:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 219.9 |
| d024fe55-c437-3ff4-b2d4-a96d535946d3 | -8.2616 | -54.7776 | 2026-09-23 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| c7158e55-1449-3db9-a874-8ecef528aebb | -8.8105 | -44.2757 | 2026-09-23 01:50:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 57.2 |
| e5fadb34-b930-30f5-9e66-f27763ed61d3 | -6.3293 | -43.9411 | 2026-09-23 01:50:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| a84aa319-c6fa-306d-96b3-0d9cfdbdd601 | -6.1109 | -57.684 | 2026-09-23 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 38f94e7c-22e7-3049-a332-57504dd2a8e0 | -3.2128 | -46.9602 | 2026-09-23 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 7873c50a-61ed-3209-abdf-808b32d10fa7 | -8.9164 | -61.4958 | 2026-09-23 01:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 56.5 |
| aa71632d-e107-3c3f-b6b5-590936179ccd | -12.1099 | -50.8071 | 2026-09-23 01:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| b5f47595-9b17-38fc-b715-89f9d5c1168e | -3.6947 | -60.5645 | 2026-09-23 01:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 9d6dc2f3-3f28-3e3a-b263-e7f95891294b | -6.6331 | -59.9265 | 2026-09-23 01:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 142.7 |
| 49a689f2-d687-3d6c-b7d2-23f965fb1bf8 | -6.6317 | -43.73 | 2026-09-23 01:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 148.4 |
| c6c2b821-aefd-3f6a-8cfc-235bf4652640 | -11.8867 | -45.7852 | 2026-09-23 01:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 1b7ca9d8-4a02-3099-9c3a-794bf4b89b82 | -12.4216 | -46.9551 | 2026-09-23 01:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 0f99efb6-a1ce-3990-b141-b153ee8fd4e0 | -6.6332 | -59.9073 | 2026-09-23 01:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 57affe81-bb40-3763-a9b1-a6d58b83ce80 | -11.8875 | -45.7394 | 2026-09-23 01:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 5c90c695-8890-363d-8cac-97bd6977c182 | -6.0926 | -57.6652 | 2026-09-23 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 90acdf23-f408-38ea-8dab-481eb8f926fa | -8.9351 | -61.4759 | 2026-09-23 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| feeb0058-fc7e-38a8-ac84-b5ffff20a340 | -12.1481 | -50.8026 | 2026-09-23 01:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 76976664-c1db-3d9c-b94e-390866510c53 | -5.7754 | -45.1053 | 2026-09-23 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| acc1c737-daf3-39a7-a056-c12ff696bbde | -6.6816 | -55.0502 | 2026-09-23 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| a624bc6e-587c-3f3a-9a88-5cba777fae86 | -12.4212 | -46.9777 | 2026-09-23 01:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 120.0 |
| bf267762-6804-399a-9c77-e88dd03f3bd8 | -3.2313 | -46.9596 | 2026-09-23 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 0828f535-eaac-3ac2-838e-87fa8ab47bf4 | -11.9063 | -45.7595 | 2026-09-23 01:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 45d3066d-4a21-3598-88d3-8175a85dae1e | -6.6148 | -59.908 | 2026-09-23 01:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 2700133b-c50d-3784-816c-99c108f215a8 | -3.2314 | -46.9376 | 2026-09-23 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 143.6 |
| d0857984-724c-3ae5-ac5c-22ca5c8b2f9d | -6.6124 | -43.7781 | 2026-09-23 01:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| b28d2735-8002-3bc8-a6bb-a34058889e2d | -8.4726 | -48.6927 | 2026-09-23 01:50:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 66.2 |
| a3cfa9e9-7a45-3abe-ba73-6cbd456d2440 | -8.8108 | -44.2525 | 2026-09-23 01:50:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 26724955-e23f-30c5-8b7e-a4a69a126331 | -8.4538 | -48.6944 | 2026-09-23 01:50:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 50bed3f1-e60d-3ceb-80fc-f4db48059af7 | -6.1111 | -57.6645 | 2026-09-23 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| d9951ece-7f11-34cd-bdb0-0fd5fd0dc99f | -8.935 | -61.495 | 2026-09-23 01:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 7abca8d5-58b4-3322-9d60-9acf7250258b | -6.6146 | -59.9272 | 2026-09-23 01:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 223.5 |
| 7b719de1-a61d-32b0-af30-299ff5b2552c | -4.2951 | -49.1234 | 2026-09-23 01:50:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 80b66fe7-352f-32ab-9318-4f2413a40a22 | -3.6763 | -60.5839 | 2026-09-23 01:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 8d64630a-d115-3085-bf23-a3171e1f5083 | -14.6302 | -45.6403 | 2026-09-23 01:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| c29dc5c4-f1b0-39b3-acc6-b0690bd21725 | -6.633 | -59.9457 | 2026-09-23 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| d8e84c24-bfbd-33c9-a752-1c63c05ab6e1 | -11.8679 | -45.7651 | 2026-09-23 01:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 48.7 |
| a3bc7227-c921-3d21-8e54-6a86948deb64 | -8.4985 | -57.6075 | 2026-09-23 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 9ed6f1de-e942-3ebf-ba9c-28599040bad9 | -12.4212 | -46.9777 | 2026-09-23 02:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 443dd7e7-7449-38e5-89eb-7aff9bdb416c | -12.3867 | -50.1731 | 2026-09-23 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 7b7bfd49-0ec4-33b8-a013-732e7a1c45a2 | -6.6815 | -55.0703 | 2026-09-23 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 211c5892-4145-34dc-b2a6-e750d4d4b7ce | -10.3134 | -50.4915 | 2026-09-23 02:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 847c3bae-c85a-3493-af73-5c7af812eebe | -3.2314 | -46.9376 | 2026-09-23 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 176.1 |
| c42ac24b-658d-3a5e-8609-2210ab6f3b4b | -8.4985 | -57.6075 | 2026-09-23 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 751141ba-276a-3b04-9e92-951d525abfac | -9.1024 | -61.4491 | 2026-09-23 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 3225de50-cb48-389d-9c1a-91bbc440c688 | -10.2942 | -50.5147 | 2026-09-23 02:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 131.0 |
| f6616c7d-1e1a-3446-a392-f16f043c4a92 | -10.332 | -50.5109 | 2026-09-23 02:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 113.4 |


[Clique aqui para ver as próximas entradas](README35.md)
