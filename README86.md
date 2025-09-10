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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64cd3464-49c2-3fce-8800-25bd92c8e72f | -12.02168 | -51.00117 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 8183fe32-166f-36ef-81c2-4f513059367a | -9.66728 | -46.64186 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c07742d3-4761-3790-92f9-7e8a39c08c81 | -5.0278 | -56.19329 | 2025-09-10 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 8069d978-f120-3752-a08a-6cdf3279af35 | -7.73724 | -50.7321 | 2025-09-10 05:04:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 046e1337-a946-3966-89e4-86f7283a3cdc | -12.98812 | -48.02449 | 2025-09-10 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ecaa0a80-0072-3180-98d7-fad8bb413275 | -9.69178 | -46.76249 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0120ed8d-81ea-3905-9c4e-56e7547439c6 | -9.08127 | -50.46379 | 2025-09-10 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 67ea9782-5e69-3622-8a01-dcc9a092db8d | -9.06204 | -45.73105 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dcd2ea55-442e-38a4-a0fe-04b0998139df | -9.02831 | -49.78534 | 2025-09-10 05:04:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| cfe29887-9a0a-3539-961f-9ea1fb289bec | -9.75707 | -51.05702 | 2025-09-10 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a5356474-ae4f-37a5-b77b-d4a0d9a5ae2d | -11.45093 | -43.61618 | 2025-09-10 05:04:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 63645bb8-d0a3-3578-82b1-1a700b04a438 | -9.01254 | -46.05694 | 2025-09-10 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d6708cb-3281-34b8-961a-d22c1f4d0455 | -12.00545 | -50.97439 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 7ed07364-acaf-3b86-aac7-a4d24f95f933 | -7.99304 | -46.33101 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5444b976-52df-38a4-b0a8-92cc00094232 | -13.02526 | -48.01599 | 2025-09-10 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b749cc3b-9400-306f-9c12-990a5b94d124 | -12.04249 | -51.04202 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 0dbbe0d4-d3d9-315a-9cca-27a044d08d67 | -6.86201 | -47.93565 | 2025-09-10 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b49cc6f8-8f9f-322e-93c6-6f1e7589fb8d | -8.78677 | -44.40778 | 2025-09-10 05:04:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce93279b-8599-36b9-9d50-d632b9a85e5f | -12.1819 | -53.86474 | 2025-09-10 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7776dd7b-fae3-3ddd-b042-574f03e6fe0f | -10.01666 | -51.68845 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 24c99d3c-5368-3239-9f9b-a0bd50ddb1b1 | -9.04773 | -50.49291 | 2025-09-10 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a78240d8-996a-390b-8a1d-6bb5ce8fa079 | -9.07464 | -50.4801 | 2025-09-10 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0bf31eb4-284c-3770-9907-139c2344dbfa | -9.1592 | -45.57337 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7accc524-05da-398d-89e3-8d560ff6332a | -9.35567 | -46.50663 | 2025-09-10 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e53a9d55-8481-3a95-900d-fecad19da8ca | -9.66775 | -46.63811 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8cfd550-b4a3-3a29-83c2-db90ef8a8d84 | -8.63385 | -53.11145 | 2025-09-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b69536c3-2a51-327e-b480-3c718b3cfeb7 | -11.10807 | -48.37253 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5f1ad00-a2d3-3d75-858f-4dbfa0b8be02 | -8.74884 | -47.09529 | 2025-09-10 05:04:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 40e480f6-6dc1-3e2c-96c9-453777b9629a | -5.73063 | -51.68586 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ba48000-560e-3097-90d4-c11ed076e24d | -9.03726 | -49.78661 | 2025-09-10 05:04:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 37f8596d-8791-320a-9d84-880f2d945141 | -9.79507 | -61.52149 | 2025-09-10 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23b7ddfa-98e2-33e6-af4b-95ed0992a829 | -11.21018 | -54.99791 | 2025-09-10 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 217f9fa9-6c65-389e-9cd7-eb278e7d878b | -8.66375 | -45.74399 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5d7c02a-8eb7-3766-977f-4c89d9725bb4 | -12.03931 | -51.03315 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 658d7359-a440-3e7b-8aef-266ac8c28884 | -8.74303 | -47.09787 | 2025-09-10 05:04:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 967730aa-c2bb-362f-93d3-cc8adf41fc2d | -5.79022 | -50.16068 | 2025-09-10 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57cb817a-9dc7-366d-9dda-ebcf6dc38599 | -6.84897 | -44.90233 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9766bad9-dd12-3ac1-8485-8b24419871ca | -7.10629 | -50.76213 | 2025-09-10 05:04:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 64130970-545e-3f32-a0f4-68d1577447c9 | -10.86496 | -55.71725 | 2025-09-10 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a5356aeb-bde6-34ab-b571-ef7494b1727d | -6.53317 | -44.7866 | 2025-09-10 05:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37c1f1b9-6afa-3e24-8025-657d6fb8c400 | -9.08245 | -47.05585 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 606252c9-d8b7-3423-b3cc-077eb90327ba | -10.47254 | -47.94893 | 2025-09-10 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| fe68a87a-205e-3df2-8218-1400f23e59d7 | -10.56705 | -49.4439 | 2025-09-10 05:04:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71b59425-22d4-3b87-a121-c5d0e77a89cd | -8.04286 | -48.67306 | 2025-09-10 05:04:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 143d7ed4-cc3b-3268-9d8a-4bdb406bd93b | -7.86945 | -46.02894 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f3a9570e-c665-31ec-aa6b-bf24b1540219 | -8.03932 | -48.66344 | 2025-09-10 05:04:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 46738d15-75e4-32f8-86b8-7a4b5c847928 | -8.09369 | -54.74856 | 2025-09-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a88fabe-56cd-3181-b7c9-3fd603ab0670 | -9.06819 | -45.71852 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 38f533f2-f646-354b-a9d2-59bccae51ea5 | -12.99428 | -48.0186 | 2025-09-10 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 718a6cda-634e-3def-b12e-ba0c51c3140e | -9.04632 | -50.49594 | 2025-09-10 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 830ee4c0-5c24-39fe-9d0e-0cba6fa226e9 | -8.15531 | -46.09137 | 2025-09-10 05:04:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bce83517-0fc5-39df-9e2c-bacd9dc8e967 | -9.97807 | -50.30246 | 2025-09-10 05:04:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a160f31b-a4a1-34df-81b6-2b06658564a3 | -7.86207 | -46.25676 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c7015e5-46af-3a96-8bcb-daff1b357921 | -11.10757 | -48.45597 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2faa84d8-7cd8-36d5-a36c-8921ee185104 | -5.90988 | -52.46719 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad428cf7-a996-3505-ac8d-b111e2068e65 | -10.0137 | -51.70918 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9fff019d-4214-3fe6-860d-e68cf8959ba4 | -6.41073 | -53.65413 | 2025-09-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2feee58-3cba-3c3c-8454-adff41bb080d | -11.11883 | -48.4486 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95907a45-7f37-3c6f-84b7-9886897b7519 | -6.84696 | -47.92211 | 2025-09-10 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 46c5147e-7600-3a13-af12-a43a1f74cbdd | -9.21511 | -50.52547 | 2025-09-10 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3ae8a33-b38f-3824-81e0-214009fbdf1b | -9.10401 | -46.97364 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dfd79291-8e0f-3ece-9fb8-b31d3b293a0b | -7.5531 | -48.22278 | 2025-09-10 05:04:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| afa82f3d-9ceb-3cf2-95a3-8be0705867c2 | -12.04734 | -51.03848 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 7a81085e-83d6-34c7-a166-bd54771a4acc | -9.51337 | -54.64907 | 2025-09-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e03293d5-8b5c-304a-9ef0-8267f4958abb | -13.79429 | -46.29071 | 2025-09-10 05:04:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f44a91d4-72df-3b1a-980e-07829cd2ef72 | -9.09659 | -46.97452 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 70afb1e5-b69a-3011-b54a-6cb30f3def71 | -11.12181 | -45.12106 | 2025-09-10 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eccb8134-8520-3c73-aefa-047f98ed89df | -11.43561 | -43.62732 | 2025-09-10 05:04:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ec5d7af4-a30b-3579-a4cf-335d589a90eb | -6.34008 | -47.10379 | 2025-09-10 05:04:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d5da9660-f1ba-3fe7-be72-0c35260c9c0a | -11.47338 | -49.26442 | 2025-09-10 05:04:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9688bd71-7af8-3a85-90a3-a9870c029594 | -11.50074 | -55.50451 | 2025-09-10 05:04:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 04a4c9ee-a825-32fd-b766-1906bc8e5127 | -8.05033 | -48.68931 | 2025-09-10 05:04:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4c7fbb93-4028-3e5f-a4fb-f29a90d973de | -8.85393 | -47.26643 | 2025-09-10 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f337d3b-4c72-31ce-8c00-ddd89eaa306d | -13.00039 | -48.01313 | 2025-09-10 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd1b3a59-ee62-3c7b-abf7-43f48850b979 | -8.85184 | -47.27374 | 2025-09-10 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84c6ebc9-62c5-3d5e-8000-4ba00ac37dbd | -8.41879 | -47.27716 | 2025-09-10 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f04437c-e7e0-3d87-b35a-f0f17c744725 | -6.81137 | -51.87845 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91976f8c-a14d-3958-900a-26f4018c16b4 | -10.94989 | -46.80083 | 2025-09-10 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5ba1d952-177f-3c52-9a1c-5d6bcf0da40e | -10.84558 | -47.7529 | 2025-09-10 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5714f31e-6a0a-3865-ae33-f192a3a0b436 | -9.10069 | -46.98509 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 072edc56-bd16-332b-99cf-b7116d6a27ae | -12.02223 | -50.99703 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 410deac1-f673-3db5-af94-f88cace1ad6d | -11.53951 | -47.31751 | 2025-09-10 05:04:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89e4743f-9383-3423-9e88-86731539a6e2 | -9.05215 | -50.48515 | 2025-09-10 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 44c415c0-70a4-3079-960e-cd9fc2ad96ec | -6.55715 | -47.48975 | 2025-09-10 05:04:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5498801-89d9-3501-9e6e-8b2880935c36 | -11.31352 | -55.12447 | 2025-09-10 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60e4f716-50f8-36f8-b016-ad0c15a501c9 | -12.81882 | -52.94348 | 2025-09-10 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c47e5ec4-74a4-3587-a58e-5f1ff5c90284 | -10.55197 | -51.51226 | 2025-09-10 05:04:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa9677f5-64b8-38da-9c3f-c96cedd0f612 | -8.06496 | -50.18537 | 2025-09-10 05:04:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7e566ffc-648e-3125-977a-2b5da701d64d | -7.76905 | -50.77395 | 2025-09-10 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41241727-3228-3a88-a588-1381a71ac7c1 | -6.38896 | -53.61199 | 2025-09-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 07d3e399-9e36-334d-aa52-ad2628a8c2d2 | -12.00985 | -50.99106 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| e5d7a9a1-46d4-31a5-a1cc-8213c9ff613b | -8.06652 | -52.32952 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 027a36df-02a5-3976-a477-2c1d7dcad165 | -12.01848 | -50.99227 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 36a38832-9d95-3672-b8d5-43798d9f39e7 | -10.52965 | -57.09919 | 2025-09-10 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb36e9e8-70a0-32b9-9733-a66226a3e442 | -8.08357 | -54.74698 | 2025-09-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f8fe0146-9bc3-3674-bee4-0636f103ac10 | -7.86789 | -46.04075 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 469a5c8b-76d9-3ffa-bced-a7da4f433119 | -8.08245 | -54.75421 | 2025-09-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 20b81bd1-6118-3c92-ab45-5cae0a20125b | -9.32038 | -46.73046 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7d049d0-c055-3bfd-ad9d-ea469768c48d | -12.00429 | -50.98269 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 2e972888-7ecc-3966-bf47-bb244967055c | -10.01067 | -51.67313 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README87.md)
