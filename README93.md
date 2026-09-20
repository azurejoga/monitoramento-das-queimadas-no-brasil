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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da65e309-2c4e-3d9c-b529-9135ca660a8e | -4.49329 | -55.56546 | 2026-09-20 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e7d048f-d136-34fe-80bb-88ee72777523 | -4.21027 | -56.33948 | 2026-09-20 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3efba992-260c-3e46-9ed1-b5fddd301def | -11.71286 | -54.56283 | 2026-09-20 05:25:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6845926e-1823-3208-baec-cac0a49d63ff | -11.13419 | -54.01602 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c3c02f34-3826-38a8-aa4f-c9dbc6b72af6 | -3.5341 | -59.60556 | 2026-09-20 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7ab594c-fb52-374a-8a53-b20a76cc87db | -12.88398 | -51.00328 | 2026-09-20 05:25:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 103c30ab-2bff-33f8-acf5-8bff50830cbe | -6.16527 | -57.70979 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2932589a-fd75-3ae5-93f3-747e3eaec420 | -11.04941 | -54.1765 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 38ef09e1-e5b2-3281-9ccf-958bcc770014 | -10.87768 | -54.07123 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7dceb05e-d2bf-3953-9452-a6e5d6c6a422 | -11.03641 | -54.16415 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 15e0758f-b4c5-3cc4-a498-ebbdbcf6005d | -7.16716 | -47.48322 | 2026-09-20 05:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| bfd57d4e-1b67-30e2-b010-c0598d81d202 | -7.17214 | -47.45378 | 2026-09-20 05:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3f6270f9-575a-3777-972e-6e7d10be9728 | -5.87307 | -52.03754 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57922d8e-c596-3030-bfd3-450e7d53cef5 | -3.72911 | -60.62239 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f2e329f1-de6e-3311-bae8-4340d8c1cd9b | -5.84644 | -53.50691 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10dda667-4677-38be-ba61-c05ca731384d | -11.6826 | -54.44759 | 2026-09-20 05:25:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 66fc609b-1ff0-3650-a08b-e38bd6debf0a | -4.49306 | -54.97923 | 2026-09-20 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14e4bf75-82fe-392f-a884-d915eb698e25 | -3.88412 | -58.94938 | 2026-09-20 05:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9eaf784-1bf0-345f-8bed-a731cb7b660b | -10.57253 | -68.66776 | 2026-09-20 05:25:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 29d2535e-91b0-334a-8e58-7e691c556559 | -6.39708 | -55.24717 | 2026-09-20 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c4ceb08d-0a8b-3dea-85c2-c59caf89686f | -3.47858 | -59.58977 | 2026-09-20 05:25:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15366c5e-39df-3026-bb59-98df5caab0fd | -10.87887 | -56.22865 | 2026-09-20 05:25:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b25ef29-31b2-3d01-9b31-35cdec7a4b16 | -7.16255 | -47.46321 | 2026-09-20 05:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f1ad809e-5fe3-303e-ae1f-476e303490be | -11.11177 | -54.03093 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9735b7ce-edbd-3630-a3f6-cf76f0b234e7 | -6.15937 | -57.70054 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5f3a1de-cb99-3b88-9666-7ead3a152bd7 | -14.05671 | -52.09161 | 2026-09-20 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 19404ac8-4fcf-3d68-8ef7-7ef5f45902e8 | -10.92673 | -53.9535 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0faa0aab-922e-35fb-9a46-9afb17b70af4 | -3.36577 | -61.33181 | 2026-09-20 05:25:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 32f1e311-f21d-3080-8ae0-a67f6e4b610d | -5.88169 | -52.05055 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2bf6508d-cf26-3f6d-813e-3440b4493bf0 | -3.48242 | -59.58683 | 2026-09-20 05:25:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 13ad89f7-0109-3438-aafd-3ae6bfa5045d | -10.89546 | -54.08456 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6505e16d-fdf8-3c90-a448-65b943d5db7f | -4.56004 | -56.15192 | 2026-09-20 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c6c39dad-c2e3-31a7-aa0f-ef4797e3755c | -4.48803 | -55.49186 | 2026-09-20 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 200d443e-5360-3341-ba4a-7c856c940056 | -3.68827 | -60.60194 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b6ce9fd4-de94-3313-92ef-771eb3390195 | -5.72876 | -53.45197 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9764f97-5e6f-3d4b-a9d8-38bab5ce145e | -12.34693 | -50.68987 | 2026-09-20 05:25:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 127e7ec6-15a0-3b32-a385-a80212551e05 | -9.93691 | -60.72771 | 2026-09-20 05:25:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 580cfb2d-04d7-3255-bb25-7a672ca2de89 | -10.75007 | -55.9993 | 2026-09-20 05:25:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fdcb6f4a-4bd4-31de-8e5d-ad882283a73f | -3.83064 | -57.5117 | 2026-09-20 05:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7a6a1f26-ba5f-31c6-9053-760cff1baa34 | -5.85227 | -53.53256 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 649d62f5-2bae-3df2-950c-e5e6676c1d13 | -5.22652 | -47.58568 | 2026-09-20 05:25:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 449f8eaf-d6bf-3cd0-bf64-981a39f3f8bf | -11.22252 | -54.08012 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 64216f61-6d43-371d-8546-d69cecc9b98d | -11.22486 | -54.06844 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 17aa1983-0c8d-36a8-a98d-e25d10fc8357 | -5.85814 | -52.03197 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d0504e3-d0fe-3ae4-9ad6-410bdcf66558 | -6.06708 | -57.7323 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| accb2f0f-b69d-3c3e-a124-e24841e11347 | -11.74639 | -54.56234 | 2026-09-20 05:25:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ae1dbee7-b769-3f7d-814c-1dfd31de539f | -6.00261 | -53.69365 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19a96c68-5163-30a6-92c2-99cb299df278 | -10.87077 | -54.0866 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| abe922f9-9ac3-30b1-bad2-e51e685313b5 | -6.33579 | -55.29114 | 2026-09-20 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eabb89b1-babd-392f-862b-ea6ccfe341a5 | -5.98006 | -55.36548 | 2026-09-20 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b7418da3-c2f7-3bac-aea0-82d426939c3e | -11.94754 | -55.92311 | 2026-09-20 05:25:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0e13f587-437d-366e-b093-a61dc18493a2 | -6.09345 | -56.46649 | 2026-09-20 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3f88d130-01cd-3cf2-ab56-5a1d5fe86ec6 | -9.93359 | -60.72719 | 2026-09-20 05:25:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a23addfc-03cc-3b9f-b8d4-973a16bbc497 | -3.37417 | -61.30041 | 2026-09-20 05:25:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02a1bd07-bc90-3ff4-871d-45e53f79dcd7 | -3.6324 | -59.56471 | 2026-09-20 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9dda28a-4be3-3b98-8803-282e1e3139ce | -11.22413 | -54.0739 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 0ad9d92a-b567-31d6-bdac-5429790ed0f8 | -11.08792 | -54.03108 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fb052cac-b7d5-3525-8045-e1851f55362b | -12.77092 | -52.85817 | 2026-09-20 05:25:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6fc66eb3-95c7-3c69-b6da-dea4e37d73dd | -6.19247 | -55.45092 | 2026-09-20 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 609ce1d1-8e6c-38b5-9b79-de13ddf1a56e | -7.52567 | -47.33231 | 2026-09-20 05:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 48f7b267-b67d-306e-893e-28570ef1f93f | -4.36658 | -55.04574 | 2026-09-20 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d103a495-0e2b-315f-a64d-b1d1f6d5bfc5 | -10.88106 | -54.08267 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cb407078-5eb6-350f-a1a9-2c060c58ac63 | -6.15751 | -57.71281 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b6c60f5-129c-3bfd-91d2-4da7b4b6b32c | -11.7182 | -54.55844 | 2026-09-20 05:25:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ddab7d42-311c-3081-be26-0ca50459573d | -11.13793 | -54.01842 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fc3d68d3-37a5-3c41-9770-f094b303b698 | -3.68279 | -60.61523 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ed149bd5-8b1b-3041-8c4c-da36c632fa7d | -11.13726 | -54.02372 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2b5b4f0a-0628-3b1e-b537-e8b04a235eba | -10.75427 | -55.9999 | 2026-09-20 05:25:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3bd8551-8889-3811-b348-9d6fc22d7f34 | -13.73361 | -48.78933 | 2026-09-20 05:25:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0abfc147-9c8c-382c-93e9-31ffdf79e387 | -12.33251 | -50.70728 | 2026-09-20 05:25:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 659ec9f4-9889-358d-ba2f-3027bd6801d6 | -7.1658 | -47.43694 | 2026-09-20 05:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ce5465d2-5936-3938-b108-20d539bdd6dc | -11.37877 | -51.39711 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 967e5eb9-c52b-340d-b1ea-ec1d910a2a9a | -3.85344 | -58.60139 | 2026-09-20 05:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a8136a2-de0d-362a-a7bf-c6f4a6658402 | -5.80533 | -57.74182 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| afd4c2c6-443c-37fb-b92a-63e81b52f384 | -3.68989 | -60.59159 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 330162dc-5f13-3ea1-8577-3003bf0e24d9 | -5.97629 | -55.36495 | 2026-09-20 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 890d905c-98c0-3300-b70c-a056c69a7d24 | -3.37864 | -61.29384 | 2026-09-20 05:25:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbeb281d-5bda-3b28-ac61-d059f8f17516 | -11.37154 | -51.40856 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3e4cb474-72d5-3ee7-81fd-f3e0db630648 | -6.11868 | -57.75264 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9500e813-63f7-36e7-a4c4-6b7b6cebb55f | -11.22734 | -54.08078 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6c61d611-1d56-3f7b-8a33-17e35817dd12 | -11.02751 | -54.15769 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 086fa349-ecd0-3ee5-9a7e-c4bd313cf8fb | -5.85851 | -49.78862 | 2026-09-20 05:25:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bfa81dc8-5267-316e-977b-09fe613d6a0c | -5.84884 | -53.55679 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ce644a34-59b3-34db-93a2-32a47961cbed | -3.37752 | -61.30093 | 2026-09-20 05:25:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe5337e9-920c-38b8-b569-238c69a774f6 | -3.68664 | -60.61229 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0cd4592c-98b0-3e72-8ef2-4e6b727c849a | -7.1556 | -47.46196 | 2026-09-20 05:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0304b867-8e9b-3eb6-97ae-a741bed73f20 | -7.16043 | -47.42285 | 2026-09-20 05:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 994a5439-9507-3e11-98d4-2eb29de045d2 | -10.92633 | -53.96397 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6d2f86e0-f777-3839-9f6b-85f00ba107e5 | -9.93304 | -60.73072 | 2026-09-20 05:25:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4eb3dfde-5aa3-3a1e-a82d-396b28f23d7a | -6.07065 | -57.73283 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cf871d76-7c5f-319c-853f-4615d16d7f8b | -10.91916 | -53.97446 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d024263c-34dd-381f-a6c9-b39f3f034776 | -7.16349 | -47.46562 | 2026-09-20 05:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e787a0fb-fcda-3e13-8aa2-49d1d7c798c6 | -5.2863 | -49.3458 | 2026-09-20 05:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 41736892-94e9-3ab2-b59b-334d018a3507 | -5.81011 | -57.73423 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1743f8f6-e985-369c-a032-6f6fa1066359 | -14.05718 | -52.08737 | 2026-09-20 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d23d93b4-8cdc-3404-a647-08f9e211c0b8 | -11.28108 | -54.12066 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1bbb3bdd-0659-3440-91f3-c012dc81a170 | -3.59368 | -59.06682 | 2026-09-20 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59714e71-aab4-35ed-872f-63a1e915fa2d | -3.75677 | -59.31057 | 2026-09-20 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f1083962-2cc6-3066-8bcc-2f8a04ae2668 | -3.66034 | -59.27434 | 2026-09-20 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d8954a1-8d56-3214-ae53-0468f3215b37 | -11.04394 | -54.18114 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README94.md)
