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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93cddf5a-8ed4-3bf2-9bc3-6337f1e771eb | -5.35106 | -45.26921 | 2025-07-10 04:02:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b8b90a4a-3b7c-39ff-8c6a-4e16d4315c0c | -6.67707 | -46.30262 | 2025-07-10 04:02:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 08f3e888-9ba6-342e-9502-66e428750dc2 | -6.64442 | -43.19376 | 2025-07-10 04:02:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 36621004-25e4-3310-b3df-c11b12850827 | -4.22687 | -47.20951 | 2025-07-10 04:02:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9502de21-5dfa-3755-8ae6-02fee3bd8cbb | -6.93824 | -43.02483 | 2025-07-10 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 18a33868-47fc-3146-a33a-d4c67126ac41 | -6.91604 | -42.83437 | 2025-07-10 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b7ec5400-fc39-39da-a395-c1279b1fbc8b | -2.44502 | -47.33103 | 2025-07-10 04:02:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 650043a9-0803-3ed1-8989-233fdeddb952 | -4.08835 | -39.82511 | 2025-07-10 04:02:00 | NPP-375D | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a7b8a224-df6c-3b52-83df-5031f11ab4f1 | -2.44551 | -47.32809 | 2025-07-10 04:02:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ee8cdb2-7990-310b-bc05-d1f7ebfc6139 | -3.7516 | -47.11826 | 2025-07-10 04:02:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54736ac4-f1ba-3e89-aad5-301505b3596d | -7.22764 | -43.07467 | 2025-07-10 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 01d80b9d-fc29-3fd3-b162-7c9d131aa978 | -7.04482 | -43.2802 | 2025-07-10 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b8065b9b-7587-3c50-b266-b64904f9d48d | -7.15111 | -43.36142 | 2025-07-10 04:02:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f92079f4-7c8e-30e7-a4f9-b73eb1c30b19 | -6.86 | -42.80606 | 2025-07-10 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 89a86870-d9cc-33c6-9500-62f275676bfb | -6.6998 | -43.10453 | 2025-07-10 04:02:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 358b7d0d-ce55-3e01-b83f-341c7cb6ea98 | -4.81876 | -47.32133 | 2025-07-10 04:02:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 18510f70-697e-31d3-9e1f-6d306e1db131 | -6.85192 | -42.78831 | 2025-07-10 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ac44cb3c-d0ef-3d32-9f16-8e6288d23bc7 | -2.44227 | -47.32866 | 2025-07-10 04:02:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10240729-05f8-37f4-8f66-605f320dfafb | -6.69114 | -43.14008 | 2025-07-10 04:02:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a52cf26-9351-3aed-98d3-e8d4285b1a78 | -3.51374 | -47.21545 | 2025-07-10 04:02:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a9911602-22a4-356d-8264-08f56daefc08 | -6.67779 | -43.76899 | 2025-07-10 04:02:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 252124a3-200d-37f3-ba18-d5ae55a5660b | -7.22047 | -43.0735 | 2025-07-10 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.2 |
| e8bc7d34-5ff9-3cb0-b83b-cbc16e0128c0 | -6.94183 | -43.02542 | 2025-07-10 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a3b34bdf-fd3c-3947-80f6-11eca29df8d7 | -6.8529 | -42.80486 | 2025-07-10 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| d8504d97-0780-3b78-8a91-afdee63d8c8e | -7.04412 | -43.28442 | 2025-07-10 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ea152864-87b2-3cbf-ae2b-33c43cec8e91 | -6.14013 | -42.96836 | 2025-07-10 04:02:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 27ce6210-9926-3abd-ae4a-f7caf3e5b335 | -6.99652 | -43.50417 | 2025-07-10 04:02:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7c5ae81-c74e-360d-9847-bb86172f09a6 | -6.45367 | -44.56835 | 2025-07-10 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fba63234-0e5b-35cd-b348-21ea0913abd5 | -6.67405 | -43.76835 | 2025-07-10 04:02:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35f6996f-2551-3e39-bd91-9d89f0fb3cb6 | -6.13067 | -42.95818 | 2025-07-10 04:02:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 47255e94-3583-307c-a58a-53b4d11efd62 | -7.23415 | -43.07995 | 2025-07-10 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| fa7585db-6a4d-3930-9139-8a5de5f2fc9b | -7.01118 | -44.42305 | 2025-07-10 04:02:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b44c7294-8945-32c9-885b-5ed7e5a00efe | -6.9321 | -43.02938 | 2025-07-10 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b33af2ef-8465-3a8a-82de-917d6d697788 | -6.85774 | -42.79748 | 2025-07-10 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| eee8d16c-c2ba-3bf7-bd4f-34b08f88034e | -3.74894 | -47.12297 | 2025-07-10 04:02:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d16b2d48-6521-3e2a-a839-9e0c618d192e | -5.24793 | -44.45424 | 2025-07-10 04:02:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f6d1094c-6f49-3967-a1c7-c92f92c0428b | -6.85537 | -42.80391 | 2025-07-10 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 4b195de1-95bd-36a1-a4df-0be54d960d76 | -6.98329 | -41.36565 | 2025-07-10 04:02:00 | NPP-375D | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ab0dff5a-0e3d-3108-858e-fd321c3d1dab | -2.4418 | -47.33161 | 2025-07-10 04:02:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d02a47d-12e2-3551-a639-bc3334c08f40 | -6.85891 | -42.8045 | 2025-07-10 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 88050b21-be61-3646-91ee-dff3b4b0d190 | -5.60597 | -45.16977 | 2025-07-10 04:02:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1f0dab8b-a860-31a2-ad2c-b7245feb309b | -6.85483 | -42.79289 | 2025-07-10 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b1e5b662-ff35-3a9e-b36e-f2c2140869d2 | -6.98917 | -43.50296 | 2025-07-10 04:02:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a69400fa-456e-35f6-aa6b-17b5c26e0a8f | -6.93328 | -43.03248 | 2025-07-10 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c2a7c575-2b33-3239-99b8-c28c37b9e6f0 | -4.68227 | -42.84521 | 2025-07-10 04:02:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00607228-9374-3c87-a77b-0da7dec637b7 | -2.44687 | -47.33242 | 2025-07-10 04:02:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd85cef0-3065-33b7-a0de-5b229404f578 | -4.25797 | -39.22541 | 2025-07-10 04:02:00 | NPP-375D | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 02b4c39d-92bf-3af5-bb83-4945baa04eab | -7.04049 | -43.28383 | 2025-07-10 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d1c64a69-e0ff-383d-9250-864fc6f5195c | -5.25505 | -44.46068 | 2025-07-10 04:02:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dcbde0ff-981b-3aca-be41-cb4d80654d29 | -6.54706 | -43.62469 | 2025-07-10 04:02:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| af33a9e5-0ace-3475-9c05-5411ceab1cc6 | -6.99497 | -43.49074 | 2025-07-10 04:02:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 898aa81e-f283-3db3-a6c0-869e0949b925 | -2.44734 | -47.32948 | 2025-07-10 04:02:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e13af55a-2191-3767-a2a4-6b45aae16163 | -6.81896 | -41.73005 | 2025-07-10 04:02:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a7786790-22d5-3722-becc-dedb4fccddda | -6.99732 | -43.52205 | 2025-07-10 04:02:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2d7befb9-9bdd-31ed-acc9-907dc28c8e01 | -6.95326 | -42.71744 | 2025-07-10 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cede6202-1d53-3215-b7fb-fd88d07b4934 | -7.22698 | -43.07878 | 2025-07-10 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 10940598-0131-31d2-8aa1-b6f4e5319769 | -6.95743 | -42.71409 | 2025-07-10 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 77279bf3-0e29-33fb-8461-bb42bd7007f9 | -4.87183 | -45.31952 | 2025-07-10 04:02:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| efe994cf-7196-3d5c-b06d-676dc122cc37 | -7.23123 | -43.07525 | 2025-07-10 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 088ee470-067a-30ab-852c-8019f8eb6226 | -6.84773 | -42.79167 | 2025-07-10 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ef24c403-c065-3e21-9a0b-a0c08c628c96 | -6.95262 | -42.7214 | 2025-07-10 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b33f9475-8d09-30cd-a768-0762717cf865 | -6.85958 | -42.80051 | 2025-07-10 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 0704c827-1d21-3f52-ae3b-9b2bce2a88c2 | -6.99437 | -43.51711 | 2025-07-10 04:02:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38d6bb9b-64cc-32ba-a326-eb02405a4753 | -6.99284 | -43.50356 | 2025-07-10 04:02:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ec760a4-3460-3ae3-a848-47a4c50573dd | -6.6994 | -43.13004 | 2025-07-10 04:02:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b71121c-1422-3ac5-a0ea-acd6b04c9a81 | -6.55078 | -43.62531 | 2025-07-10 04:02:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| eaaad54d-a506-3d5a-9532-8faf0b1dfba5 | -4.81692 | -47.31847 | 2025-07-10 04:02:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86d3697f-5997-362e-bca3-4a5067433d86 | -6.24215 | -43.36859 | 2025-07-10 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5de3e3d4-3ea3-39aa-b0aa-db722c11c32f | -6.57339 | -42.89924 | 2025-07-10 04:02:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6807d402-fea0-3600-a57b-40e941535203 | -7.03235 | -43.4927 | 2025-07-10 04:02:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d59d146a-ab1a-3ebf-abbb-d0afab42ad34 | -6.98194 | -41.36564 | 2025-07-10 04:02:00 | NPP-375D | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0a0216f3-8a6d-3d61-9409-1352d2425eb6 | -6.70391 | -43.10812 | 2025-07-10 04:02:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c89be5df-3a4d-3691-be20-ee2dc64a9318 | -7.00728 | -44.42262 | 2025-07-10 04:02:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a09a2336-cc7a-3466-b017-2ef6091cb504 | -6.85603 | -42.79992 | 2025-07-10 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 92613bd1-7b14-3847-bf63-25784235a20c | -7.03165 | -43.49698 | 2025-07-10 04:02:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f40c91e6-ada3-3e19-8898-81272a75ac0a | -6.85128 | -42.79228 | 2025-07-10 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ddc65e1f-68a1-3b53-b1e9-38af1a902afd | -6.86064 | -42.80207 | 2025-07-10 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 63829461-3eaf-3ed9-b8c2-6a0b40111118 | -5.89161 | -45.5753 | 2025-07-10 04:02:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ff70f60-c686-3049-be10-27026d68c669 | -7.00243 | -43.51405 | 2025-07-10 04:02:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f4eb08f3-2815-3d37-9328-9e8cc7bc971c | -6.03144 | -44.05121 | 2025-07-10 04:02:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8f2295c2-a648-3f66-925a-0c7bcbe5c1ff | -6.70341 | -43.10513 | 2025-07-10 04:02:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1234b14-7a8e-3d31-8cea-e2f1bba76c8b | -3.74983 | -47.11753 | 2025-07-10 04:02:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 3219e72b-0792-38e8-b810-edf1d0716572 | -5.41196 | -46.07163 | 2025-07-10 04:02:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 169e4c88-32ee-34df-a756-bcffe5cd4e5f | -6.91538 | -42.83841 | 2025-07-10 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d6c4c752-a23b-3253-9380-0c4d4075b01c | -5.25191 | -44.45487 | 2025-07-10 04:02:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53b7f5e0-664c-326b-9802-d71f5c0273fc | -6.86934 | -42.78563 | 2025-07-10 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ca9b1a6c-2ea3-3fbb-b41e-16ce119cc8ef | -6.55154 | -43.62073 | 2025-07-10 04:02:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0fcc44d7-ea6e-3607-84d8-f988fe3eaa17 | -3.75066 | -47.12371 | 2025-07-10 04:02:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3bf5796b-b65f-3ef2-b1cf-6d18e840df43 | -4.8085 | -39.93912 | 2025-07-10 04:02:00 | NPP-375D | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c2695fbe-87be-3c15-b03e-20aa6bd23a37 | -6.84838 | -42.7877 | 2025-07-10 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f4bb4655-2c48-3a1e-bab0-53350716827c | -4.08585 | -39.82486 | 2025-07-10 04:02:00 | NPP-375D | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| fdb6f6c2-c299-34f7-9798-543988825447 | -7.00006 | -43.4828 | 2025-07-10 04:02:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d0a54092-4446-36e7-9c55-ae77f126dfec | -2.44045 | -47.3273 | 2025-07-10 04:02:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a2c85eb-0b1a-33d2-94f8-212029a9e436 | -7.23348 | -43.08406 | 2025-07-10 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 82da95f3-0314-3a51-aa34-6db7db5473ee | -6.99569 | -43.48645 | 2025-07-10 04:02:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d17ad6c6-2551-3653-bac8-b0bbd5c1cc71 | -7.00965 | -43.49321 | 2025-07-10 04:02:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 442cf82a-b076-35a3-acce-529dd6318032 | -6.84464 | -42.86835 | 2025-07-10 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ebefe568-2383-35b0-9067-291341aedb98 | -7.16109 | -43.70256 | 2025-07-10 04:02:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dd042c38-937e-3461-b102-24e8ab9650a7 | -7.02798 | -43.49635 | 2025-07-10 04:02:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c890814d-8987-3bb8-b597-38fdc8fa525b | -6.64805 | -43.19435 | 2025-07-10 04:02:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README12.md)
