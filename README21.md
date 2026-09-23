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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 960de51f-159b-30d0-b69c-98cf094c61fc | -3.4781 | -59.5588 | 2026-09-23 00:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 6c307b60-5099-3d21-88d1-9893c97a7a17 | -6.6332 | -59.9073 | 2026-09-23 00:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 41.9 |
| d9b4ac12-87b9-374a-a4d0-3ee21d36a4cc | -5.7752 | -45.128 | 2026-09-23 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| e2b2d3a6-b69c-30d9-9459-ad1c494b3b6c | -8.4799 | -57.6085 | 2026-09-23 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| b0208dd9-221f-3280-8327-73c0f93b8d2d | -6.6776 | -58.5554 | 2026-09-23 00:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 8ef2a17f-c6bf-3fa6-a379-30a56afb1a64 | -11.8679 | -45.7651 | 2026-09-23 00:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 40.2 |
| b490cfb5-793d-3194-ba25-d9dc03bb9168 | -3.6763 | -60.5839 | 2026-09-23 00:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 8473f3d1-0eb1-39cf-9c54-9180998b7986 | -11.6898 | -50.9193 | 2026-09-23 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |
| de649853-afec-3cfe-b12e-e94319557f3e | -11.7091 | -50.8958 | 2026-09-23 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 59.2 |
| bb250e3e-6d4a-347c-b009-70793fb0ce15 | -11.7784 | -50.0743 | 2026-09-23 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 45116f8a-e468-3b9f-8c3e-196448c759d9 | -5.7754 | -45.1053 | 2026-09-23 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 46dde778-df45-3607-bbfc-b18b59e5a660 | -11.7088 | -50.9172 | 2026-09-23 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 7d871793-e30f-36e6-8e07-1edbc1cadd8e | -12.4404 | -46.9749 | 2026-09-23 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 4e1f4128-0997-3c95-a745-6361257a7635 | -3.6764 | -60.5649 | 2026-09-23 00:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 90b2d014-bcb9-3afe-8a7a-3e9ff1a74eac | -6.7211 | -44.1618 | 2026-09-23 00:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 54eba906-97b5-3912-a55a-3b5aa8a33a86 | -7.1277 | -43.0774 | 2026-09-23 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.5 |
| c8fbbbcc-a035-39b0-bb03-485e7fab9623 | -11.7085 | -50.9385 | 2026-09-23 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 127.2 |
| b86519f2-6f10-3793-8a62-d1d4c5419afb | -6.1111 | -57.6645 | 2026-09-23 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| f48ef3d1-bd75-3815-9798-c8bb2369f091 | -3.478 | -59.5779 | 2026-09-23 00:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 5acf1aa0-a433-327f-b91b-d5ae9db0a886 | -6.6317 | -43.73 | 2026-09-23 00:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| d855e7a2-5cbc-38a5-aaf9-5b3e217fefb8 | -4.0925 | -62.1062 | 2026-09-23 00:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| fec585d7-ef63-3a4e-a809-dad016ade4a3 | -8.4985 | -57.6075 | 2026-09-23 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| b3440f42-e147-3c21-b182-978af56850c1 | -3.2128 | -46.9602 | 2026-09-23 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 73bd2764-ba3c-3dba-97c3-773effe4e1c9 | -3.2129 | -46.9383 | 2026-09-23 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| f2c89fe7-0f9c-346e-aab2-21851badcafe | -6.1109 | -57.684 | 2026-09-23 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 081b31f4-62c4-3bf0-b5c0-0745deafc8c8 | -6.61 | -43.74 | 2026-09-23 00:45:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a2068aff-9120-30a7-970b-92e26730ab63 | -3.23 | -46.93 | 2026-09-23 00:45:00 | MSG-03 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abcf450a-c8ee-36fc-9e2b-fdefdc3fa57e | -6.61 | -43.79 | 2026-09-23 00:45:00 | MSG-03 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dc968a76-942d-3869-8584-8c415f649e06 | -12.79 | -50.91 | 2026-09-23 00:45:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f0125167-d677-3e24-a132-7a3ee9124f24 | -8.5984 | -54.6139 | 2026-09-23 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 580edd33-87fc-36f6-b478-eaa5c505d0a0 | -3.2314 | -46.9376 | 2026-09-23 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 222.3 |
| 225ab945-37f8-3df3-959a-bee30e2fd9d4 | -8.5796 | -54.6354 | 2026-09-23 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| c2bf4444-630e-37e6-9859-ce976ccb5c40 | -11.8675 | -45.788 | 2026-09-23 00:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 126.8 |
| b6f22ab0-719c-3c91-8f32-f8a21670487b | -11.8867 | -45.7852 | 2026-09-23 00:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 476.3 |
| 91efc024-f33c-3428-af40-4eb3ee4a7a0b | -8.8105 | -44.2757 | 2026-09-23 00:50:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 83.8 |
| c62619da-62e1-3278-a7d9-53ab6b86adda | -8.9165 | -61.4767 | 2026-09-23 00:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 291e280e-c886-3351-ae0b-367be6ee02b4 | -9.1025 | -61.4299 | 2026-09-23 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 17208ae9-3f1b-3417-9ab8-f821e0dc0e48 | -12.4216 | -46.9551 | 2026-09-23 00:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 184.6 |
| 15ac56d9-c731-3680-9634-b159ed91f11b | -11.8679 | -45.7651 | 2026-09-23 00:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 027d6990-fed8-3b54-a6b8-273e60115b1a | -5.3453 | -45.1576 | 2026-09-23 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 4f5f89fd-acd3-3f25-a33b-4a575759a641 | -3.6947 | -60.5645 | 2026-09-23 00:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 102.9 |
| b994e7d2-f4c8-32fd-9144-8849fe5f2cdd | -6.1289 | -57.7613 | 2026-09-23 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 830d453a-5791-3c38-ad98-813fcedd49a6 | -7.8811 | -61.1779 | 2026-09-23 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 3998ed62-4b09-34c7-bf6e-ce98220ae290 | -9.5596 | -65.9985 | 2026-09-23 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 4cbb4662-c5d8-3720-8cab-a741554ef604 | -6.6815 | -55.0703 | 2026-09-23 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| ad081c80-2cac-3c81-ad5a-8d61a3c904d9 | -6.1109 | -57.684 | 2026-09-23 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 85916c90-174f-3acf-a887-da4ea01d238c | -9.5596 | -65.9799 | 2026-09-23 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 7f5bf798-2f7e-3b6c-ae7d-35b66c47c369 | -10.6094 | -53.9902 | 2026-09-23 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 27b74a65-203e-3f74-876c-dfa187e17c13 | -4.0925 | -62.0874 | 2026-09-23 00:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 52e28918-5984-384d-bb01-6ecdd2f53486 | -5.7754 | -45.1053 | 2026-09-23 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 3f18fa54-af92-3d0d-bb02-94d3979fb2f1 | -8.1876 | -54.7219 | 2026-09-23 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| f408d154-165d-3f9e-ba8c-d732c17146f5 | -8.2062 | -54.7207 | 2026-09-23 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 6f0183d6-f24b-32a8-951a-80735fcdaccb | -6.6776 | -58.5554 | 2026-09-23 00:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 57d66d24-8c52-3a3e-abbd-f320f099456d | -6.6816 | -55.0502 | 2026-09-23 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| a5342f16-eb44-3007-86d9-8816d574e2b6 | -11.9063 | -45.7595 | 2026-09-23 00:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 52.7 |
| d7ea4605-6eaa-3b1a-b335-0349d084f41a | -3.6764 | -60.5649 | 2026-09-23 00:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| d43ac1a7-58df-3684-95e2-73ae8cde39eb | -10.6283 | -53.9885 | 2026-09-23 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 5a1aa5e1-3c9b-355e-9d66-b3be9b7d036c | -5.7567 | -45.1067 | 2026-09-23 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 134.9 |
| ca5de5a1-3e33-33cc-9bd8-3b50d00a904d | -5.7752 | -45.128 | 2026-09-23 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| d1941bfd-a765-33f6-9a16-8f386905580e | -8.4985 | -57.6075 | 2026-09-23 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 5d8d4302-7da0-3dd5-b2d6-2d3858e22360 | -8.9351 | -61.4759 | 2026-09-23 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 4af7352d-5ed7-37e6-8f1b-fcf541e53f30 | -3.2313 | -46.9596 | 2026-09-23 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 161.7 |
| cdcfb988-c340-3735-beb4-28fbccdb68e2 | -3.2128 | -46.9602 | 2026-09-23 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 1f60508f-cabe-38cf-ade8-9c04afd949f5 | -8.4799 | -57.6085 | 2026-09-23 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| b2017d65-ea00-3e04-aad0-7fe12f257f4a | -11.8871 | -45.7623 | 2026-09-23 00:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 440.9 |
| 8935236a-8307-3daf-9fc3-babb75745ce8 | -3.2129 | -46.9383 | 2026-09-23 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 45edc1f5-5b47-33f4-a668-4735ab0362cd | -6.3293 | -43.9411 | 2026-09-23 00:50:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| b5c22f8f-9448-3c3d-b448-0161fbf6c01c | -6.6775 | -58.5748 | 2026-09-23 00:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 94182709-3827-36c4-b3df-0c6b40527d96 | -3.6763 | -60.5839 | 2026-09-23 00:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| b4d33957-ec9f-37d8-98f9-63f75cf634d2 | -5.7565 | -45.1293 | 2026-09-23 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 757f0a0a-a688-33f1-b61f-46536297eadc | -8.935 | -61.495 | 2026-09-23 00:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 41520562-21fe-3bf6-8cf6-ed43be2475ee | -8.4538 | -48.6944 | 2026-09-23 00:50:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 97.4 |
| be7fe6a9-1d10-3a55-960d-80ff5fd97cd1 | -6.728 | -59.423 | 2026-09-23 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.6 |
| cac49807-b599-385d-95cd-88dde0d65e49 | -11.9059 | -45.7824 | 2026-09-23 00:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| d6429ea4-75c0-360f-8eb5-9cc1c384d0d3 | -6.7211 | -44.1618 | 2026-09-23 00:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 5e375f77-a958-3a1e-9cbe-6d2dc2708c44 | -8.5982 | -54.6341 | 2026-09-23 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 116.0 |
| d0389e4c-d3a4-3e23-8bf1-f165b41ef504 | -3.6946 | -60.5835 | 2026-09-23 00:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 175ad87c-18ee-3df2-b4ab-1babe4247d9f | -8.791 | -60.8127 | 2026-09-23 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 6b3423f4-939c-3828-8cd7-7f470af8d54b | -12.4024 | -46.9579 | 2026-09-23 00:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 87b4913f-ed40-3f4e-82bb-0b7be4ccd222 | -8.9108 | -62.391 | 2026-09-23 00:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 27eb3976-8276-3613-ae3b-62a93d90fafb | -6.3105 | -43.9426 | 2026-09-23 00:50:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| c558df45-f08b-3903-83e5-64b693618fd4 | -4.0925 | -62.1062 | 2026-09-23 00:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 9fa2fe64-1a87-3dc0-91e2-51f60c8dd195 | -8.9164 | -61.4958 | 2026-09-23 00:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 77.4 |
| a54b736a-a004-3572-9351-8480183db000 | -3.6947 | -60.5455 | 2026-09-23 00:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 5a012ce0-cd63-3c53-ab06-4064936c2f49 | -3.6765 | -60.5459 | 2026-09-23 00:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 40.5 |
| ecb98ca5-7f54-3c8b-b4f7-e2227fe7d676 | -8.4726 | -48.6927 | 2026-09-23 00:50:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 0b889456-d141-387e-b939-eb9570d6d05f | -5.2475 | -48.1941 | 2026-09-23 00:50:00 | GOES-19 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 2c9374e3-7420-3fc7-82e6-73de67d7a6ee | -6.0925 | -57.6847 | 2026-09-23 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| eb13bc91-accb-33ec-8286-a8a7b2a44f49 | -8.8108 | -44.2525 | 2026-09-23 00:50:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 65bbdb5d-b8e7-3206-823f-7b9f31f1ad82 | -12.402 | -46.9804 | 2026-09-23 00:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 25a5847d-c70d-3c92-8a64-4c4981243365 | -12.4212 | -46.9777 | 2026-09-23 00:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 197.9 |
| 275e361a-0f3f-3de8-96de-2432602d5a13 | -6.1111 | -57.6645 | 2026-09-23 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 55debd51-60ec-34c7-a68c-f3d4488b9592 | -3.478 | -59.5779 | 2026-09-23 00:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| f073962f-5c0f-3e76-894e-f96352aff3fa | -8.6227 | -54.608601 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73a17aac-0a64-3592-9fe5-49ceca92cb78 | -9.1575 | -51.3559 | 2026-09-23 00:58:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6dd6972e-7e4d-3fbf-bf6a-0b763e44f0ba | -2.8573 | -60.2477 | 2026-09-23 00:58:00 | METOP-C | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 16df99ab-1ec7-3712-9765-db4a79f1b0ff | -6.1233 | -57.740101 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7f7620b-2b6a-3eb4-ade4-bd1b294b7ba4 | -11.3032 | -51.348 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0fcaf12e-7781-3ab5-ab83-efa9cb3b13ef | -5.2443 | -48.176601 | 2026-09-23 00:58:00 | METOP-C | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d3ee055e-b15a-35db-b9ec-4e4e070a9dd3 | -4.4505 | -55.064499 | 2026-09-23 00:58:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README22.md)
