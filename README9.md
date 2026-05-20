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
| 080c2d5d-d12e-3fd2-ae73-c43d31298a9f | -11.45707 | -55.11698 | 2026-05-20 07:03:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a7805743-a6fd-3433-975d-8a9ff1855f1e | -9.88398 | -52.43987 | 2026-05-20 07:03:00 | AQUA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 9a33eaae-2512-3efd-9990-b6b57084ebea | -11.61088 | -55.32713 | 2026-05-20 07:03:00 | AQUA_M-M | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b0274702-cb46-328d-9ce2-770f469f33fb | -14.15503 | -52.88643 | 2026-05-20 07:05:00 | AQUA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e484ba4a-3501-3595-9ffb-13b21ddf4643 | -9.9686 | -52.4793 | 2026-05-20 11:10:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 266b7f4d-8da8-30c6-b9f8-52907581da47 | -9.9688 | -52.4585 | 2026-05-20 11:10:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 54fc9f3b-6fe7-318a-813f-775e39bb9e28 | -9.9688 | -52.4585 | 2026-05-20 11:20:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 119.9 |
| 379a8cfe-7f6f-34cb-a852-53a13ed7fe46 | -9.9686 | -52.4793 | 2026-05-20 11:20:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 93e418ca-663d-329d-8ff5-31a2aa513d45 | -9.9686 | -52.4793 | 2026-05-20 11:30:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 2b28a084-f187-37e0-895e-9baead7809f8 | -9.95 | -52.4602 | 2026-05-20 11:30:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| ebf5bd8c-89d5-3482-b7b9-21e13d5df6e8 | -9.9688 | -52.4585 | 2026-05-20 11:30:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 134.2 |
| 599a10d3-8fa9-3476-906e-38ffcaded578 | -9.9686 | -52.4793 | 2026-05-20 11:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 0f35104b-8603-3684-9190-a6b489e7ab3e | -9.9688 | -52.4585 | 2026-05-20 11:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 101.3 |
| ed237b1b-5d88-335e-8b0e-f44fe63f80bb | -9.95 | -52.4602 | 2026-05-20 11:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 0b22f5f5-de1b-39f0-8ec8-a69245e0ff14 | -9.95 | -52.4602 | 2026-05-20 11:50:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| d07d46f5-cba0-3f7b-a8ea-2d31102939a0 | -9.9688 | -52.4585 | 2026-05-20 11:50:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 33e37a30-b045-3c4d-9ed9-c8ded2a2af5a | -9.9688 | -52.4585 | 2026-05-20 12:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 806fc886-30e0-371c-84b1-1baba561654c | -9.9688 | -52.4585 | 2026-05-20 12:10:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 1ddae7c4-c0d3-354c-9cfb-b782161e2ae4 | -6.81689 | -43.82365 | 2026-05-20 12:14:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 2f46d2ba-28fb-3442-9b1d-9b3055ac7ece | -6.81672 | -43.8302 | 2026-05-20 12:14:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 041c04a5-5653-3694-84fd-be95c9a8afc7 | -6.75344 | -45.02621 | 2026-05-20 12:14:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 2aa0faf3-bb65-3a79-84dd-48f87589ed9c | -6.22052 | -46.89309 | 2026-05-20 12:14:00 | TERRA_M-T | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 63631e27-6bbf-3fcc-9a37-f8d8acc8ce57 | -12.23134 | -44.26254 | 2026-05-20 12:17:00 | TERRA_M-T | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| c87eb471-46c5-3cb8-b553-ee473557ef2c | -9.96581 | -52.45724 | 2026-05-20 12:17:00 | TERRA_M-T | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0881e50b-c448-336b-b228-84fdce6d8f05 | -9.88525 | -52.43937 | 2026-05-20 12:17:00 | TERRA_M-T | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 74f698ea-b1a1-383e-9028-fc64ba8adf3f | -9.15661 | -47.75093 | 2026-05-20 12:17:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| d75122c5-d043-3ae6-911d-851580056c61 | -8.45575 | -51.53109 | 2026-05-20 12:17:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 93fc38ca-27c8-3c82-80f7-5d7046e58240 | -10.09155 | -47.96811 | 2026-05-20 12:17:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 37cd4089-f081-345e-8104-7ea259144f6d | -12.4244 | -47.89548 | 2026-05-20 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 15a5c468-e167-3bf9-86f6-dc3f76325658 | -10.09342 | -47.95331 | 2026-05-20 12:17:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 19247669-688c-3310-a5a8-786d949bdb89 | -9.96454 | -52.46615 | 2026-05-20 12:17:00 | TERRA_M-T | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 3c1c4e27-b29a-3360-b0a6-e6de5592f1b5 | -8.99529 | -46.93219 | 2026-05-20 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 42c00ac4-fb44-3ffb-b563-81ba75d26c89 | -11.47718 | -52.91462 | 2026-05-20 12:17:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 44817fb5-09a7-3396-a91f-23e66d43acb7 | -8.54284 | -51.56758 | 2026-05-20 12:17:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| df83b072-56da-3f06-a9e1-3a43e68a0804 | -8.55032 | -45.97581 | 2026-05-20 12:17:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 85b316a3-ee69-3770-b1ff-3464aa793edd | -9.96327 | -52.47505 | 2026-05-20 12:17:00 | TERRA_M-T | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 896a5dfd-34af-3e29-8913-d0da7fd94238 | -11.15123 | -48.09969 | 2026-05-20 12:17:00 | TERRA_M-T | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 138d9e43-187e-30b0-abd4-b8f0246d57ea | -10.58254 | -46.64905 | 2026-05-20 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 4d5bbf5f-9812-38ac-b6a2-b4e970778e68 | -13.58057 | -52.1774 | 2026-05-20 12:17:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a0265eb4-9e9f-397e-a485-a9f94859b38e | -8.98752 | -46.94196 | 2026-05-20 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 1d2fd221-26ac-3fc3-ba5c-cd2df8826009 | -12.60866 | -44.52236 | 2026-05-20 12:17:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.1 |
| e05394b6-979c-349f-94b5-6e998908b5d4 | -12.06517 | -47.34344 | 2026-05-20 12:17:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 71ddd07d-415b-372b-8ae5-19ae3e14fdfe | -10.11096 | -50.62154 | 2026-05-20 12:17:00 | TERRA_M-T | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 609b620a-07cd-3ca9-ac4e-35759a1ec8cb | -10.1096 | -50.63156 | 2026-05-20 12:17:00 | TERRA_M-T | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 026e83e5-7b7f-3441-a200-f0bcb4f097be | -12.42235 | -47.91197 | 2026-05-20 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| e65bbcfd-f5a6-351d-bc68-5e0c610c297c | -14.15633 | -45.30149 | 2026-05-20 12:17:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 33.9 |
| faba69c6-ac75-311f-a214-5dde33cbef1b | -11.14938 | -48.11469 | 2026-05-20 12:17:00 | TERRA_M-T | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| d95d9dbc-148a-3adc-8157-fb3a81c259ce | -11.91396 | -43.41683 | 2026-05-20 12:17:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 50.2 |
| a2e6957e-9397-3872-a026-79ced461e0e4 | -7.92965 | -48.2892 | 2026-05-20 12:17:00 | TERRA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4af1a2f1-f470-32ec-bc82-af03de079caa | -10.57864 | -46.66204 | 2026-05-20 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 35f76ded-9590-30b4-a000-92e7450c5118 | -10.10464 | -47.95452 | 2026-05-20 12:17:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 08a249cb-0ab9-3b11-8516-4a523a81abce | -9.95571 | -52.4649 | 2026-05-20 12:17:00 | TERRA_M-T | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 43dfb2fa-0166-3489-b208-3ffecd152b19 | -14.15372 | -52.88958 | 2026-05-20 12:17:00 | TERRA_M-T | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 439e8a64-52e6-3377-9181-5487e529b9a7 | -9.15858 | -47.73598 | 2026-05-20 12:17:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 0d61ae89-2531-339b-8f76-9c2c3c61e661 | -11.14987 | -48.10889 | 2026-05-20 12:17:00 | TERRA_M-T | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 57e34b50-6d89-3138-8c11-14bff1c9199f | -10.58097 | -46.64347 | 2026-05-20 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 78ba963c-be63-3889-be55-bd90c6de5459 | -10.10274 | -47.96943 | 2026-05-20 12:17:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 7e18adc8-c6f5-337f-ab12-e73bf2b9c708 | -12.06091 | -47.33621 | 2026-05-20 12:17:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 5b3ebd96-3acd-366f-910d-462e0a78ad70 | -8.98975 | -46.92485 | 2026-05-20 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 7120e3c2-1e56-3e62-9280-68734bbc9d67 | -12.23014 | -44.23767 | 2026-05-20 12:17:00 | TERRA_M-T | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 0dd32bcb-bd7c-3085-81f8-b4d3a80c94a2 | -13.65944 | -43.09173 | 2026-05-20 12:17:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 88.0 |
| 7c8e1671-666e-3961-b8aa-7021ea6cebdd | -12.22687 | -44.26859 | 2026-05-20 12:17:00 | TERRA_M-T | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 7fcf4666-f2bd-3686-90a1-df5a8bd5e3d8 | -8.54157 | -51.57661 | 2026-05-20 12:17:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 019e26e4-bb98-3209-a71b-846d11690a86 | -12.23485 | -44.23154 | 2026-05-20 12:17:00 | TERRA_M-T | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 9ad023bd-04a5-3ab3-ab62-0a0f691330b2 | -9.19286 | -48.61973 | 2026-05-20 12:17:00 | TERRA_M-T | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 50fc08f4-6d29-3ee5-bd92-af6a269e3c42 | -9.95444 | -52.4738 | 2026-05-20 12:17:00 | TERRA_M-T | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0854e6b3-a105-31b8-849d-937894905267 | -14.39126 | -53.87571 | 2026-05-20 12:19:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3a433083-acdc-33dd-8e8e-2f32c2eb4959 | -14.91117 | -47.7358 | 2026-05-20 12:19:00 | TERRA_M-T | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| dee54e66-c83a-340b-920f-fa43fcbe4c73 | -15.91798 | -51.27312 | 2026-05-20 12:19:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 61b3cda8-8fa3-3d71-a5fb-cb86850fe235 | -14.29515 | -54.60017 | 2026-05-20 12:19:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 31b307a2-8f1c-3fab-9d6f-ccad442024f4 | -10.6467 | -42.3141 | 2026-05-20 12:20:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 99.7 |
| ae758191-c48a-39c7-8781-0f5b86d3321a | -31.05254 | -53.0563 | 2026-05-20 12:21:00 | TERRA_M-T | PIRATINI | RIO GRANDE DO SUL | Brasil | 4314605 | 43 | 33 | nan | nan | nan | Pampa | 12.3 |
| 1aaa7272-f1b0-30fd-a4fa-a9ccab1c61aa | -10.6659 | -42.3112 | 2026-05-20 12:30:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 155.0 |
| c94031f7-c580-305a-8990-8966213a77f9 | -11.9301 | -43.405 | 2026-05-20 12:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| c8f686af-e766-3376-92ed-9ca8306b4eb9 | -9.9688 | -52.4585 | 2026-05-20 12:30:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 4f7221cf-c966-35bc-9570-4d56210e390f | -10.6467 | -42.3141 | 2026-05-20 12:30:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 255.6 |
| 5d5de8dc-f177-356c-9b78-cbf745dae76a | -11.9301 | -43.405 | 2026-05-20 12:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| cdeb0510-2da0-3f61-b4e2-35fc88dddf38 | -10.6659 | -42.3112 | 2026-05-20 12:40:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 260.6 |
| 803f1fb0-612a-35a8-9a1b-f23b16d642b1 | -9.9688 | -52.4585 | 2026-05-20 12:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 9932b335-a529-35a4-b8ed-8c9eabb45a88 | -10.6467 | -42.3141 | 2026-05-20 12:40:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 352.8 |
| 61dc8669-5b04-3bd0-8fb7-8adc8e85cd36 | -12.6011 | -44.521 | 2026-05-20 12:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 8cc4d5d3-871e-36bc-9a2a-e37cc284f164 | -12.6011 | -44.521 | 2026-05-20 12:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 0c22dd0c-3a71-36e5-8d45-da6edf09e66b | -10.6659 | -42.3112 | 2026-05-20 12:50:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 261.4 |
| 5598d25e-b0cc-3344-9df9-ac5025bc2af3 | -9.9688 | -52.4585 | 2026-05-20 12:50:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 97b3f9ac-5fff-35b4-a0a3-eeca39cb7c15 | -10.6467 | -42.3141 | 2026-05-20 12:50:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 447.1 |
| a41952d0-43d6-35ab-8e17-1593d1f56f2c | -11.9301 | -43.405 | 2026-05-20 12:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 996ed971-1348-31b3-9a87-44ca38e5cedf | -12.6011 | -44.521 | 2026-05-20 13:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 9f9656f2-a347-3083-8b33-87b6d7b0de23 | -10.6659 | -42.3112 | 2026-05-20 13:00:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 255.8 |
| 44843507-a116-3519-9c09-a1a47310fab4 | -9.9688 | -52.4585 | 2026-05-20 13:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 4c9f7c01-bd71-3dd5-937e-b82eb7569738 | -10.6467 | -42.3141 | 2026-05-20 13:00:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 466.5 |
| 755ffcd5-76e1-3f72-bed2-76ed08976903 | -9.9688 | -52.4585 | 2026-05-20 13:10:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 24ca310a-4df4-351f-897a-8a146bd890b3 | -10.6659 | -42.3112 | 2026-05-20 13:10:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 245.1 |
| d8a71be4-adc3-3d2d-8212-bb1ff6516f3f | -12.6011 | -44.521 | 2026-05-20 13:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 23906dcd-4d55-393d-a6f4-20c2c15fe9fc | -12.2408 | -44.2512 | 2026-05-20 13:10:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| f49d544a-f714-3aa4-9840-8e158e654669 | -10.6467 | -42.3141 | 2026-05-20 13:10:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 446.4 |
| e315d74e-453c-3b0c-aa80-8d157dd7c895 | -10.4346 | -49.9019 | 2026-05-20 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| a780b14f-0cf9-3548-bbb5-71e0f141ce9a | -10.6659 | -42.3112 | 2026-05-20 13:20:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 243.9 |
| cbac161a-dbd6-3239-99c1-9deb621917c9 | -12.2408 | -44.2512 | 2026-05-20 13:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| f634e04d-0acd-3c04-8837-e25a2299afd5 | -10.6467 | -42.3141 | 2026-05-20 13:20:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 529.8 |
| 5fc28a03-5137-3d1f-b6db-2837c6f9a7d8 | -9.9688 | -52.4585 | 2026-05-20 13:20:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |


[Clique aqui para ver as próximas entradas](README10.md)
