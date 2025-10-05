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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 627f0e9a-374c-3af6-9bc4-983447c1d202 | -9.04244 | -61.64202 | 2025-10-05 04:46:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4bd75c37-1c2f-3f61-a267-c9931ada7a90 | -13.48087 | -47.28598 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 6126a940-9fd9-36fc-989e-7f51a174a812 | -8.63594 | -44.90419 | 2025-10-05 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 256a0c65-3456-33d0-84a6-2e9661b3184e | -11.1302 | -47.90606 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 68160990-555d-3e28-b45e-8ddd51e1549f | -10.623 | -48.668 | 2025-10-05 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 55af8d1e-7f47-320c-aa69-e87928932b24 | -11.67157 | -43.9025 | 2025-10-05 04:46:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 3f19d313-7b54-3c3a-b91a-9dbf95c2396b | -9.28294 | -45.66916 | 2025-10-05 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40467600-5f0c-324a-8015-9b9673c1f14f | -11.78571 | -47.92155 | 2025-10-05 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63744a5e-359d-3375-b255-2f7e27102954 | -10.3626 | -48.16277 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9bef6484-28a9-3c14-b686-f343a568bf40 | -12.31932 | -55.14296 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e58f140d-abcf-39e4-a8f5-3155689ee56f | -9.06475 | -47.01765 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2391ef90-68f6-356a-9f5c-def9a75af23b | -13.43674 | -47.78216 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4348fcde-b5b7-3da1-ad32-cc9ac9077879 | -13.27824 | -47.58752 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ff9b4d97-490e-3775-8c01-3a1603dbd3f0 | -12.5906 | -48.13076 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 015c964a-7bc1-3c78-90cc-836271c9658e | -10.18356 | -48.90902 | 2025-10-05 04:46:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ffa2d5b-2c05-3559-8114-1a386c69b797 | -8.8619 | -46.83903 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4433227-e14c-3faa-a9c2-8a465f0c6e3e | -12.98901 | -46.84203 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58773cd5-f5c4-3acc-856e-b3fbe56ef7fa | -9.32632 | -45.65916 | 2025-10-05 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7e0b14fd-da8b-3f0a-b5fe-41886a5afcb4 | -7.65928 | -45.44682 | 2025-10-05 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8e6a26af-84f7-3b45-a335-76ccad668e35 | -13.58895 | -48.16151 | 2025-10-05 04:46:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3aeeafa6-6958-3642-86a6-5888967cf48a | -10.84392 | -47.98603 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 27995d87-3314-3fff-874d-eb4190ba43dd | -8.75253 | -47.20164 | 2025-10-05 04:46:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bd776287-1804-3dcb-98c5-a4614ea07c61 | -11.11561 | -47.13837 | 2025-10-05 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 53082bf1-1c3f-3ca5-bea0-21cdb4259b84 | -8.62383 | -55.00239 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f0406c4-db0b-35f7-8c85-7a4eaa876fe4 | -6.42904 | -47.17275 | 2025-10-05 04:46:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f96b865c-af4e-3b31-91c8-5d752c548a65 | -11.80371 | -46.8255 | 2025-10-05 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1f626d08-f62a-3eb1-9489-06482a459268 | -12.30086 | -55.14073 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c8d1de4-7cf4-3036-a64d-808aa54330d6 | -12.31376 | -55.15447 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06e54654-5169-3e63-8f34-113cc48fc78d | -12.70014 | -45.84926 | 2025-10-05 04:46:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d3734f57-4fcb-3ae4-a068-18ab2b76c606 | -13.70373 | -47.35421 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6102f61-a9d1-329d-9779-abd00a69800d | -11.11162 | -47.1377 | 2025-10-05 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 499728ee-1461-39df-9624-d8e33a60d7f2 | -7.69652 | -42.87193 | 2025-10-05 04:46:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 072200b2-920d-3608-a85c-3c44dceb85b0 | -7.15893 | -46.08955 | 2025-10-05 04:46:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a841a575-3db3-31ea-9fa0-3f6ae0187b7e | -8.60481 | -46.27839 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 3a148031-15e6-3a17-ac41-4507991cc533 | -13.35368 | -47.58612 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dcec79a0-7293-349d-a921-a407b1c245cc | -12.30655 | -55.15001 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26881efd-66b3-31a8-b460-1c27e3ce6ad8 | -12.92405 | -45.07355 | 2025-10-05 04:46:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8f92d2e2-9d23-331f-836e-b574b1baf492 | -10.39481 | -45.40316 | 2025-10-05 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a5f90465-8402-3a2f-bad0-2ac8bf6d254b | -11.46529 | -51.52044 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac39df49-fee4-3326-903e-d4850141e39c | -13.08682 | -47.90606 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5e3e93a-5c46-3e1c-96e5-b2c4997a7fbd | -10.35992 | -55.38591 | 2025-10-05 04:46:00 | NOAA-21 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d87af2d6-b0f0-3f58-a195-2d4e2d0e9d9a | -7.81216 | -42.53706 | 2025-10-05 04:46:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| dc022763-fa62-33b2-8f07-6d6afc8483c7 | -13.20701 | -48.52978 | 2025-10-05 04:46:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64677bde-9ff4-3786-be3a-bc76e75f212f | -13.25332 | -48.47483 | 2025-10-05 04:46:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7f9868db-f174-3ec2-92cf-76c800bb7a58 | -13.20321 | -48.52936 | 2025-10-05 04:46:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87aadf14-b2a7-3dff-b1d7-2ef3f9271d82 | -11.91695 | -46.24437 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 07be195f-06eb-34cd-9b46-d21cb1c8b085 | -10.57094 | -48.68903 | 2025-10-05 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 41c1386d-0505-3d95-91f6-f8d2a6e9050b | -8.57828 | -46.31881 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| fda92bd7-9d89-3997-9708-c0d14e884049 | -8.93584 | -48.66084 | 2025-10-05 04:46:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 51488300-8427-35fb-a800-c20a09af9aed | -13.14587 | -50.92826 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ef5b8ab-915e-35b9-a8bf-abfd28c9d6e0 | -11.79025 | -47.91729 | 2025-10-05 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 864da55a-9670-3d4b-883f-a21aabe80461 | -13.29853 | -47.61858 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a189285-1094-36be-8704-7005dd9325a6 | -8.16136 | -47.2166 | 2025-10-05 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4533238c-780b-330b-9128-f29c441d497a | -13.58409 | -48.15921 | 2025-10-05 04:46:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 816a7a6d-d728-33b6-b13d-a5aea1c4df79 | -13.27445 | -47.61566 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e981ab32-5774-3158-bd43-de861bae1bcf | -6.99056 | -44.21052 | 2025-10-05 04:46:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 50d5684f-57e7-32ca-9c0a-cda32c448c12 | -12.31445 | -55.15042 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3dd2d84-bb47-3f2e-be28-dbd7d11f77b7 | -10.50145 | -48.10874 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| be78558d-be8d-35cb-9952-811494944810 | -12.89202 | -47.30997 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| faf7d3ee-386a-3b00-83d5-bdb1fc3660ae | -6.84581 | -45.48527 | 2025-10-05 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 62022b5f-4a75-392b-b561-ff03feabaee5 | -10.59674 | -54.35706 | 2025-10-05 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6cd79644-682d-374b-8339-02160e95e1cb | -13.10623 | -47.94064 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0507d7e4-a3d5-38ff-bc3f-63479bab38fa | -13.10165 | -47.85782 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4cddd46f-e8a1-3387-a384-175ddd4eeac0 | -12.98482 | -46.84145 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6102985a-7629-355d-8cf7-a25edfca94ff | -7.52529 | -41.27389 | 2025-10-05 04:46:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 87b27e27-589a-3640-840a-2223e8ef4f27 | -13.26439 | -47.59938 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 52dd063e-2833-3ef8-8896-14374da8b645 | -9.91718 | -50.19912 | 2025-10-05 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a23229c-ea3e-3510-a6ad-d231c34e4271 | -12.58992 | -48.13564 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d926a67-a7d5-3e3c-b528-152baa8e0bbe | -7.52256 | -41.27338 | 2025-10-05 04:46:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 2d2147f3-be97-31b2-a305-115c06a349ca | -7.64145 | -45.41903 | 2025-10-05 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cc183b1b-5ce3-302a-8fe0-eac51ed00405 | -10.74422 | -47.89767 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5169d7c-3998-3d30-b592-dba1d1856a31 | -12.40981 | -51.09693 | 2025-10-05 04:46:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 679dfb65-3cf9-3da8-84dd-d49a9cdedbf8 | -9.99307 | -48.29458 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9d4cb8e4-7cbc-35ec-a8bc-392325d7f51c | -12.98992 | -51.0136 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85809ab9-2568-346e-918a-9dcb9cecb9c3 | -13.26363 | -47.81458 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 24b24867-74d4-32db-a3c6-25f64083c58b | -8.59869 | -46.2921 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 61bc04a5-6c0f-39da-bfb7-2f98cf9bcdd7 | -7.06134 | -49.95246 | 2025-10-05 04:46:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 273b824c-d28d-33cf-84a8-dde0009bdeda | -8.56497 | -46.26499 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 885ae445-2dbd-3915-b31a-a9759a76ed7c | -7.03641 | -42.76156 | 2025-10-05 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 52b6446c-52e1-3397-ad4f-b7f785e300e4 | -11.31597 | -53.96254 | 2025-10-05 04:46:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11fb187d-4fa0-3df6-8d9f-7fc6314d51d3 | -11.22761 | -49.92615 | 2025-10-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| efde1d26-299d-3a07-823f-05a62db02942 | -13.28961 | -47.62412 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 82f5d803-2d5b-36d0-a1c3-756ae18f2d11 | -11.43748 | -43.48957 | 2025-10-05 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a4fc28a-0807-34f7-a53e-7a7ec29e5fd2 | -13.38587 | -47.55942 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80c3a66d-7427-3001-b750-2625bdbfafca | -9.62397 | -46.63025 | 2025-10-05 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf786843-b0f6-3cb9-bc7e-6c6fb4c24a11 | -9.65434 | -45.85066 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8abf38ee-46c4-36a3-9e26-e147cc54b33c | -10.35032 | -48.15573 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d803e88a-23d3-3de5-bb2d-eb4329c6e6f9 | -11.0823 | -47.91401 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d910d74c-e3e6-3b89-b1ef-efbb5125f718 | -8.58442 | -46.3047 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 597e2c8c-de7b-3afd-b603-8ae292b57c32 | -12.08107 | -45.15071 | 2025-10-05 04:46:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1a54d5a4-fabc-37ce-a2a5-97605ba73b69 | -10.8414 | -47.97658 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| be78b011-f6e4-3641-a8c6-e7026f423fb3 | -11.7568 | -44.74229 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ac0f3f3f-ef15-39d8-9235-b3d1cd2b95fd | -11.87282 | -56.88349 | 2025-10-05 04:46:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 2466d7a4-3d98-31d7-baf2-13c10330657e | -13.08676 | -47.90759 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8e960b00-6656-316e-8aa9-fea18baaab56 | -11.81382 | -45.0888 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2a98c9f3-b539-37ed-92e4-bf28f5c17937 | -11.12706 | -47.9008 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7849be77-8340-3db7-b777-4d377ae9828e | -11.81251 | -46.85295 | 2025-10-05 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 605af8a9-fce2-3e92-a32d-2cc48a6ac9bb | -13.33505 | -47.59071 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 76d81067-1d74-3b30-ad56-01b18a53c616 | -10.1926 | -46.72528 | 2025-10-05 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce8ad2d9-215e-39ca-8802-7703443c99ba | -8.54977 | -46.31517 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README93.md)
