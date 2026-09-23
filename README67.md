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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd76ded0-d57c-3553-a23f-aac84ecadf14 | -14.60923 | -45.63955 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 92f9599c-b294-3723-b3b2-148c96bee2d6 | -12.72629 | -50.88444 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ca09390c-eb5d-3298-b1b0-6b47c21a7203 | -9.27846 | -45.91375 | 2026-09-23 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6483b769-fb4d-31bd-b726-abe81df47f1f | -14.70446 | -45.5822 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c435f224-e0f4-3859-b7b0-5f9ab25d1c91 | -11.47385 | -47.35743 | 2026-09-23 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6cabe7c3-7b38-34c4-bd76-a6a3e88c5954 | -12.76265 | -50.90771 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9eb42fba-f81b-3a19-a2d9-28f9ae3cfc65 | -14.61567 | -45.64468 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7d23e4f2-5cb3-3b3f-b6d0-b301ba504ea6 | -14.70563 | -45.59909 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e99c085-3230-33a9-a1b3-8c5e7c004ee1 | -10.36651 | -50.44644 | 2026-09-23 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 95988b1d-e8ee-348a-a09b-24ebed6162f8 | -8.95999 | -49.05035 | 2026-09-23 04:27:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb864838-8582-3abb-854a-a5591812c421 | -14.61393 | -45.63194 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ca8a23ee-d8b6-3f71-a4b9-39d7ef7b4f2d | -8.78114 | -45.6316 | 2026-09-23 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e147f552-cfc3-3094-ad3b-5bbd13f61192 | -12.72273 | -50.88383 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 067ef2d6-abc4-3a45-b674-43d7fc76bb84 | -10.25446 | -49.98226 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4269e7bf-9db2-34f7-ad79-7eb9dfbfa1ed | -14.70739 | -45.58688 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1b34603e-4050-3a29-bea3-af5bdb0d29ca | -11.28077 | -51.3382 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b96a38b-9408-3cd8-bee6-a70724dd36b2 | -12.04968 | -50.34989 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 5fc4b637-3702-3627-b300-f74977c0c250 | -6.92842 | -46.55847 | 2026-09-23 04:27:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bcf664d0-07d3-3821-be9c-d40f6b3d38a8 | -8.80866 | -44.27866 | 2026-09-23 04:27:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d83312fb-4210-35d6-8d5c-854b2bdd4e64 | -8.81044 | -44.26668 | 2026-09-23 04:27:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1ecac4c3-287e-3bef-908c-0120bb1a4135 | -10.04811 | -50.21819 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 260b524d-1558-3207-99ad-0a5ccf749c3b | -11.35506 | -43.38013 | 2026-09-23 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2bca39fd-37ce-368b-83ec-4a7a59abd424 | -12.80868 | -50.87318 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 322cb003-f95b-315b-8a5f-94b3f97e17b2 | -8.0843 | -44.34945 | 2026-09-23 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a48a7df-0a51-310c-8608-a213e95e348a | -13.44545 | -46.31572 | 2026-09-23 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07d4cff0-1a40-3b2b-9080-c023970ba752 | -13.92611 | -47.83554 | 2026-09-23 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 22d9a386-86fe-31c8-8742-b8388eef1d3e | -6.67576 | -55.05713 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 98fdda63-d2de-397d-802c-30a255392603 | -10.00853 | -45.18316 | 2026-09-23 04:27:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 08f00631-dad4-33c6-8e81-b28e0e8930a4 | -6.66809 | -55.06 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b5d7b6ce-2124-35a2-9c53-127e874d33d1 | -11.88795 | -45.78307 | 2026-09-23 04:27:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 74f0fddd-6a49-3d03-a5c8-43a8f2464c17 | -11.11901 | -51.05001 | 2026-09-23 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b4c09c30-c848-3ac0-a9d0-9cc0ffc512e4 | -6.78542 | -48.67844 | 2026-09-23 04:27:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00694106-2e2a-3623-b8e6-fa94c95e00c7 | -7.49822 | -44.32703 | 2026-09-23 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0fcd575-a763-33f6-ac1f-607b00c58225 | -6.66889 | -58.56784 | 2026-09-23 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 33113056-765f-3b1a-8e26-334733d1a2fe | -6.53328 | -55.35806 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98c86d71-6b50-3c72-a086-d6b5c2efe577 | -6.67378 | -55.06873 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e1972a80-eca0-38f5-a684-d199782bf2e5 | -9.57379 | -46.53912 | 2026-09-23 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9b990ca2-3c93-36da-99d4-cead06d4352d | -7.39848 | -55.21366 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a11a492-810c-3389-a1a7-616b44ef4fb5 | -6.67728 | -55.07895 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c5d0459-ee29-384f-9db3-b4cafa5e27bc | -11.53065 | -45.35598 | 2026-09-23 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| dae1fc35-4e4f-3973-8506-4d8ec94a6a6c | -10.46023 | -44.95057 | 2026-09-23 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95ed295b-8e2a-3b9c-8efe-06128b81d79d | -10.2775 | -49.97385 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36ab2f8a-d801-3dca-ab58-a3173969453f | -8.26115 | -45.43008 | 2026-09-23 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f57c7c5-e5be-30b2-9fc5-deeb0cb94133 | -8.25232 | -54.78312 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2c7c5fb7-bdea-3962-8c65-eede6273ef1f | -6.378 | -55.28514 | 2026-09-23 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95601b19-2426-3886-8861-cbac944ad491 | -12.54537 | -50.0781 | 2026-09-23 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd74d109-9da8-3192-bf93-63a0ec0d994b | -8.55186 | -38.35915 | 2026-09-23 04:27:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c810ba7e-37c7-3254-a5e3-0e74900d1014 | -7.09734 | -52.74956 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f384ef91-7c97-376f-9754-74b731a1d3f2 | -5.92992 | -59.92041 | 2026-09-23 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d5b712e8-8517-31be-8d93-b928aee84a01 | -6.67527 | -55.05996 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8635d9dc-5b0f-37d7-affc-0b29e2070c85 | -13.71275 | -48.78416 | 2026-09-23 04:27:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fffc9f78-7769-38d4-89e0-a5c23de6c86a | -12.80157 | -50.87196 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ca5bfb03-8fe7-3da5-be18-282849f2e18d | -6.67571 | -58.5766 | 2026-09-23 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8fbdffd8-01c6-3291-9e67-c1881f77659d | -10.32607 | -50.51251 | 2026-09-23 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5801dd5b-cc9d-3ca8-90d4-acc6be487bab | -7.54607 | -47.32741 | 2026-09-23 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e8b07e8-5e01-348b-9b8f-c4eda577cb03 | -6.30988 | -59.94641 | 2026-09-23 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1b2b37b1-99a9-3017-b57f-7d10c7773e33 | -12.4102 | -46.97161 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 48eeb4c3-120c-301d-b329-95d30410f4e2 | -11.12193 | -51.055 | 2026-09-23 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9ef999e2-f32d-3b4f-ba68-d9fa4ab59ba4 | -11.69305 | -43.45089 | 2026-09-23 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75779dfa-ba45-3891-b912-913d31f166c1 | -11.39595 | -46.80419 | 2026-09-23 04:27:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b979e8c8-aebf-382d-aa36-a654b7de526e | -8.48551 | -46.86951 | 2026-09-23 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87430984-107a-37de-a0a4-928316197749 | -11.29409 | -51.34972 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6823437a-2e79-3dd5-b1a6-ef8d7d722fb3 | -14.16972 | -47.84275 | 2026-09-23 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42b4ca9e-261e-3db5-9aa0-086590c1da77 | -7.15381 | -48.44191 | 2026-09-23 04:27:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b4a3d0e6-d8b7-3375-922b-457b533f9f98 | -6.93502 | -46.5595 | 2026-09-23 04:27:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 415b1bc3-e1a2-33c6-a321-2e2f5a5156e6 | -14.64805 | -45.59854 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7a953b9f-d030-3599-9c44-b83304f7a5ad | -10.1328 | -45.54613 | 2026-09-23 04:27:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0a60ea75-8c57-3875-9f87-6fe7ae30d2f4 | -9.97363 | -50.2531 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8206b1a2-7493-39d7-9330-25e052dc25ee | -11.71175 | -44.50687 | 2026-09-23 04:27:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2273adb9-f6e7-3082-8a97-cc6dcef92330 | -6.84015 | -55.30773 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2beb6a21-f13c-387f-8dc4-443d279ffddb | -10.71553 | -48.71217 | 2026-09-23 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4902dc73-e380-354d-bff6-83fb65bb57e3 | -10.62184 | -53.98643 | 2026-09-23 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 818bdf34-29cd-35b6-8eec-49159f7a3af5 | -6.68495 | -55.05365 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9dddf5b1-a0ef-3688-975e-8567bd37827c | -6.67776 | -55.06461 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11c562e7-bf21-373c-91cd-cd8befb1f5e1 | -9.5375 | -46.28849 | 2026-09-23 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d6db205-5c3b-3704-b922-52b0df8c496f | -14.69271 | -45.58868 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| c253a9b8-45b2-35d2-bd33-80c61222b6d0 | -12.07702 | -50.35861 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 58090ca8-cdc8-3078-802c-3cb60e04f47a | -11.7 | -50.22013 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6aecd06c-02c7-320c-bfb9-9bb840bce307 | -6.29419 | -57.74152 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c90c7e40-27da-340b-b5e1-117cc664614b | -14.61918 | -45.64521 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 82f6d2b7-6610-3d8c-812c-f5b4f184c5a8 | -7.68554 | -45.46712 | 2026-09-23 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 750de63e-539b-3316-891c-c34e86b2f59f | -10.25039 | -50.00235 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 71b0c533-a4a3-36b9-8263-e2819c4ade5b | -11.12284 | -48.31429 | 2026-09-23 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bd709c1a-c937-3f52-9db9-d66e97a096ea | -14.63093 | -45.63865 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| ce1cbd3f-1f07-305d-989b-d8f7aac13730 | -10.026 | -45.20512 | 2026-09-23 04:27:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4d10453-9dd3-3373-a56c-719f7fda88e4 | -9.96805 | -50.26484 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0df517e8-7a3d-3dd3-ba52-5451ed01056b | -10.32677 | -50.50833 | 2026-09-23 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a9063a63-dce4-3baf-b119-b19de257746e | -8.33908 | -47.23996 | 2026-09-23 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5a6a533-a714-3f4b-813b-7aaae82debc5 | -9.92578 | -48.48129 | 2026-09-23 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac4bbcf0-f4fe-32a6-b511-8c8acce926bc | -12.05251 | -50.35446 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 412b6664-3e15-3eb5-9359-8bfcdce834ff | -10.30021 | -50.51249 | 2026-09-23 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b5b88b2-b9d4-3146-a2ec-7f1538fce3dc | -10.06758 | -46.09038 | 2026-09-23 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c09d8f29-8542-3ada-ba37-7a9b2b686af8 | -12.11864 | -45.64702 | 2026-09-23 04:27:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f401710-1a18-3cab-a1d0-632890487818 | -7.98263 | -47.47197 | 2026-09-23 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 71506257-7a20-38b6-a018-1a61c16e9e83 | -12.87189 | -50.8625 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f4c0fa35-2a6b-3b44-be86-8298f72f8f26 | -8.48873 | -44.75386 | 2026-09-23 04:27:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c4385aa-68a6-38ed-b021-344db6c598f7 | -13.93988 | -47.83415 | 2026-09-23 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cfcb439e-752f-352a-9c8f-fabb525801f2 | -12.365 | -50.15176 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 81b6125b-367b-3876-835d-31f18ff35717 | -6.64057 | -59.92813 | 2026-09-23 04:27:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 4929f140-7c3d-36b6-ad57-03c1218a33ec | -6.09693 | -57.67835 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |


[Clique aqui para ver as próximas entradas](README68.md)
