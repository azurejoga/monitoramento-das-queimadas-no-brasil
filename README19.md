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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5eade8a-32f2-3189-afcd-7d3af9488f7c | -13.71271 | -57.47688 | 2025-06-05 05:25:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0bbdf819-c106-3ba1-a448-ece8dd46eb7b | -13.72246 | -58.67524 | 2025-06-05 05:25:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5848ebc2-937a-3f1e-bcb0-c729fa3d13a0 | -12.05618 | -58.12582 | 2025-06-05 05:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5944fa9-6640-3bfa-b4be-43c2ac5c7c0c | -13.14335 | -56.81071 | 2025-06-05 05:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3700fde5-520d-3695-a87f-6145835d787c | -19.40144 | -54.46768 | 2025-06-05 05:25:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a50a6276-2f7d-3ec5-8645-d7baaffa3db0 | -18.83809 | -53.6231 | 2025-06-05 05:25:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d3c09d11-c5ff-3be1-bbb1-167eb6c1a28c | -11.8091 | -58.85167 | 2025-06-05 05:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 54eec354-83be-317e-96b1-3be57b25ac49 | -18.84315 | -53.62738 | 2025-06-05 05:25:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d3acbbd4-6428-3607-b6b2-63fb269f82e9 | -18.84242 | -53.63428 | 2025-06-05 05:25:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34eab1c6-c912-385a-8e03-938181aaec8e | -13.14327 | -56.81164 | 2025-06-05 05:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8232cf55-e94a-391d-9f7c-451c4c3b9919 | -13.5231 | -56.57164 | 2025-06-05 05:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 16.0 |
| bcee3274-2d6d-38c8-8dd7-c84a51fca8b0 | -13.5148 | -56.57037 | 2025-06-05 05:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 69b90dac-fee3-3ac1-a6f4-7ee1ffd19611 | -12.01398 | -63.78856 | 2025-06-05 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8f59ca02-ea81-3a01-bba6-f59fc9454029 | -18.84278 | -53.63084 | 2025-06-05 05:25:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1c3ed37-2519-3ec9-be33-07bcf1b96976 | -13.14787 | -56.80848 | 2025-06-05 05:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b7aebb33-14af-30b6-864d-a9b25a29a394 | -13.51116 | -56.56586 | 2025-06-05 05:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a904f9b-f3b0-37c3-8e93-f6974f8d8cd9 | -13.80953 | -59.68182 | 2025-06-05 05:25:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af05c064-af0e-3fb7-9708-929ff909f33c | -18.84352 | -53.6239 | 2025-06-05 05:25:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| aeb78d8e-5f6d-3ad6-93bd-f0aa4bfb7f1c | -13.51634 | -56.55873 | 2025-06-05 05:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 9cb98265-cc53-3da7-9357-9a824bd32872 | -13.51793 | -56.57868 | 2025-06-05 05:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 40905dd7-e243-338e-88c9-a4201bc3e52d | -13.51531 | -56.56649 | 2025-06-05 05:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| c0297296-1e90-3ba3-824b-ece2ae36f3e5 | -19.3962 | -54.46757 | 2025-06-05 05:25:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1e4690d4-f1d0-3674-a035-7323e578edc9 | -12.6645 | -58.22311 | 2025-06-05 05:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 76c6494d-f68a-3d64-82cb-208a44859ea0 | -13.48506 | -56.55894 | 2025-06-05 05:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 415f3826-0a89-3684-86cc-a8088f7971e1 | -13.51167 | -56.56199 | 2025-06-05 05:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 32fd4985-1ceb-31c8-8fbc-0b7776fcd732 | -13.14742 | -56.81127 | 2025-06-05 05:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b74c952e-1cda-379e-b722-bedbf8982b8d | -21.80145 | -52.76661 | 2025-06-05 05:25:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2424b4f5-0c59-330f-831c-f0e391755100 | -12.66515 | -58.21861 | 2025-06-05 05:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7b27613c-e402-3a09-b979-e3e0b6cbca4f | -11.65433 | -62.76736 | 2025-06-05 05:25:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ab0a7c6-4b95-3e84-a3ee-ce6f6fc4ab69 | -11.83771 | -60.91729 | 2025-06-05 05:25:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 029bb91a-118d-3cca-a9e5-83410b665a46 | -13.52362 | -56.56776 | 2025-06-05 05:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 48e61365-dd85-3207-82d8-dac564774b6c | -21.79551 | -52.76594 | 2025-06-05 05:25:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d68df889-c644-366e-941c-a7ad4b442526 | -13.52049 | -56.55935 | 2025-06-05 05:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 35.8 |
| dedd4fde-3f54-3b8d-9564-4907f2454b8c | -18.84426 | -53.6169 | 2025-06-05 05:25:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3faa61e9-fe23-3673-91d0-8fc2403ae05d | -12.66886 | -58.21913 | 2025-06-05 05:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6fcc7dbc-becf-3705-8477-8b030864ec75 | -11.85984 | -62.75669 | 2025-06-05 05:25:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5528315b-5946-3df0-807f-38d63ba3e90d | -12.66951 | -58.21461 | 2025-06-05 05:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 537536ec-a404-35bf-9e25-6d660a1d9f39 | -13.52101 | -56.55544 | 2025-06-05 05:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f9485df4-d3b3-3c12-a6e2-25cddbc10e77 | -13.52209 | -56.57927 | 2025-06-05 05:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| acd59d3a-e537-31dd-9372-fd5c98c0612c | -18.83846 | -53.61959 | 2025-06-05 05:25:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7385f9f3-f308-3a3d-832a-4a67cf543d45 | -13.71665 | -57.47742 | 2025-06-05 05:25:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0735040d-6df8-3d06-9316-a2d17252e0bb | -12.02425 | -63.79032 | 2025-06-05 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b5c3d5c-0366-3bb9-a3fd-bb210ad6488a | -19.438 | -54.77773 | 2025-06-05 05:25:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd407e11-3926-36d5-a653-0dea7bcf4549 | -13.51844 | -56.57485 | 2025-06-05 05:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 45207692-445b-33f6-bc7a-ddf4750273d7 | -12.66207 | -58.21354 | 2025-06-05 05:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 462e5aba-bf65-37f8-9281-c8036e6c2210 | -13.81304 | -59.68233 | 2025-06-05 05:25:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd877313-2c62-3ca0-8d15-6cb22bc62af6 | -13.51582 | -56.56261 | 2025-06-05 05:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 35.8 |
| b3292a8e-7e20-3fbc-a048-77bcd13b2acf | -13.51998 | -56.56325 | 2025-06-05 05:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 20761789-0d82-34a5-b38e-c1364512befa | -13.51895 | -56.57101 | 2025-06-05 05:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 5b9a8c60-2624-3daa-970b-06084cd3acd9 | -13.14734 | -56.81219 | 2025-06-05 05:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4ce4e96-03a3-3bc1-9c9e-c95af504ac9f | -11.58615 | -61.09521 | 2025-06-05 05:25:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b32aebd-69c3-3897-8c52-6eb7f3604011 | -12.66822 | -58.22364 | 2025-06-05 05:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fb678f95-f8e0-3ccd-860e-3b44eea6a212 | -18.83883 | -53.61609 | 2025-06-05 05:25:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 387ea496-8f12-3763-bd43-b177fcec21f4 | -12.06087 | -64.05504 | 2025-06-05 05:25:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33746bed-3121-34a2-af9b-412e42ad3eec | -18.84388 | -53.62042 | 2025-06-05 05:25:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a8ee461f-c55b-3237-86b5-af77b52ee3f5 | -12.01741 | -63.78915 | 2025-06-05 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3af5c123-5ab6-3fda-9a67-2cd917412920 | -13.51218 | -56.55811 | 2025-06-05 05:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 125b7596-d1a0-3c95-ae2c-438fe075dd00 | -12.01335 | -63.79235 | 2025-06-05 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f80e46ff-950c-3b75-a817-5acbbb57013b | -13.71594 | -57.48262 | 2025-06-05 05:25:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 637e1290-f472-3265-babc-956a8762e372 | -13.51065 | -56.56974 | 2025-06-05 05:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| abeabdff-cd2b-31a8-b3da-7c902ccea913 | -13.5226 | -56.57545 | 2025-06-05 05:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 98f94d62-5bd8-3aa5-94fc-2817d45673a6 | -18.83736 | -53.6301 | 2025-06-05 05:25:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 98227fd4-5e92-3bf2-8b7e-3bd8799438a0 | -18.83772 | -53.6266 | 2025-06-05 05:25:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 93afddf9-ea25-344c-aa98-4eff64b9ff37 | -21.7959 | -52.76155 | 2025-06-05 05:25:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b668f41f-2c5e-30fe-89f0-2368ef882b29 | -13.5155 | -56.5488 | 2025-06-05 05:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 117.6 |
| b9ebebc1-3bef-3419-92d3-7aa0099767b4 | -18.8279 | -53.6283 | 2025-06-05 05:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 7b7e55bb-b7e0-3de0-9147-224488fdf621 | -13.515 | -56.5893 | 2025-06-05 05:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| fcaa17e5-acc3-3312-bd79-5c301cdaca67 | -13.5346 | -56.5469 | 2025-06-05 05:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 5bfbd796-3028-3da5-8fa0-3295b62704da | -13.5152 | -56.569 | 2025-06-05 05:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 285.8 |
| 80f171a4-32f2-33a5-b49d-4e97173687db | -13.5344 | -56.5672 | 2025-06-05 05:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 150.8 |
| a7068685-d04d-390a-839c-8159f1eb7716 | -18.8479 | -53.6251 | 2025-06-05 05:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 95cf59e1-3147-3d35-9b21-7521eabf3807 | -18.8479 | -53.6251 | 2025-06-05 05:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 65.9 |
| db4eaab2-adce-3dc9-a7e4-eedad0bd231a | -13.5152 | -56.569 | 2025-06-05 05:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 268.1 |
| ab5f1739-201d-3338-8343-a13b8abb5d59 | -13.515 | -56.5893 | 2025-06-05 05:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 32778495-ef61-38ea-a480-53cdc8b027fc | -13.5344 | -56.5672 | 2025-06-05 05:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 131.5 |
| efee035a-54ce-3c21-ac00-b3239953c4cd | -13.5155 | -56.5488 | 2025-06-05 05:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 123.1 |
| fe41dcd5-66b5-3270-b1d5-84eb980d8f47 | -13.5346 | -56.5469 | 2025-06-05 05:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 588010a0-f24d-3c50-ac4e-bb1f2c797f1a | -13.5346 | -56.5469 | 2025-06-05 05:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 62.9 |
| f9674a88-9bbb-365d-9c40-8307cc5b9199 | -18.8479 | -53.6251 | 2025-06-05 05:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 4ef335eb-04d9-3772-946f-6aed2521b3be | -13.515 | -56.5893 | 2025-06-05 05:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 280d5532-fe9b-3fd0-800d-663ee9584367 | -13.5152 | -56.569 | 2025-06-05 05:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 256.0 |
| a2a17c51-c9c0-3f57-b1ef-48bf53b31746 | -13.5155 | -56.5488 | 2025-06-05 05:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 96.5 |
| d835255e-b51b-39e5-a292-fc05cc002551 | -13.5344 | -56.5672 | 2025-06-05 05:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 163.2 |
| e7367fab-02bc-3c32-bf28-fa219fa394bf | -7.53708 | -45.82977 | 2025-06-05 05:57:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 1c077c93-ac2a-354e-813d-e46f2be1ee86 | -6.20963 | -43.3329 | 2025-06-05 05:57:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 72189d5f-9b57-3054-81fd-6a1acdc884d5 | -7.90092 | -50.35834 | 2025-06-05 05:57:00 | AQUA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| a7c7ebee-1e23-3148-ba82-378d3e647e78 | -6.96022 | -42.90828 | 2025-06-05 05:57:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 61.7 |
| 7e944397-37f6-335a-8171-1230570c950f | -6.21116 | -43.31979 | 2025-06-05 05:57:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 8bd69afa-863d-37c9-941a-25d67e93b505 | -6.20854 | -43.33964 | 2025-06-05 05:57:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 9e1c6e82-4ced-3b17-bea0-059c8f77fcc4 | -7.5339 | -45.82241 | 2025-06-05 05:57:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| fda5ff6b-7742-3ace-ad4b-c6f187b15f90 | -7.61457 | -45.74477 | 2025-06-05 05:57:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 56fde6bf-9a63-3a03-8c0e-59c456d5aed7 | -8.72845 | -47.98865 | 2025-06-05 05:57:00 | AQUA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2532d2cd-c2c4-378c-bf09-33ddb0851e63 | -9.221 | -48.86137 | 2025-06-05 05:57:00 | AQUA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1423e255-050e-3263-a393-a1c1922dba30 | -10.81654 | -56.9657 | 2025-06-05 05:59:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| d4422bff-0d3c-3bd3-b7e9-30845047e5dc | -18.83896 | -53.6342 | 2025-06-05 05:59:00 | AQUA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 898069d0-c10b-3019-a542-68644567f383 | -11.54593 | -56.4232 | 2025-06-05 05:59:00 | AQUA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 46f254cb-288a-3c73-8fb4-b10084a2f9f9 | -13.50961 | -56.56736 | 2025-06-05 05:59:00 | AQUA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 3942ff28-3e81-3522-906b-11fb94937681 | -11.54306 | -56.43978 | 2025-06-05 05:59:00 | AQUA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 18.0 |
| c5897380-674d-3073-96cd-046e40df5b7e | -12.66951 | -58.2112 | 2025-06-05 05:59:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 26.8 |
| af5f4126-3319-37a9-8950-43bb71f9f81c | -10.49522 | -53.66204 | 2025-06-05 05:59:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |


[Clique aqui para ver as próximas entradas](README20.md)
