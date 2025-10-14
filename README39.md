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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 082667d6-2f12-3e8e-bf75-e319d9ca12db | -4.73203 | -44.69593 | 2025-10-14 12:17:00 | TERRA_M-T | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 31cf4493-98f6-3622-a154-b29316d3303b | -6.42284 | -44.66856 | 2025-10-14 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e0cb5453-3464-393f-ad14-fd8e3e5321a9 | -6.75986 | -42.80946 | 2025-10-14 12:17:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| ceebb97a-319c-33e8-9f3f-8dc86be2b8f1 | -3.37416 | -43.0591 | 2025-10-14 12:17:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 03c68b68-af39-38c2-bb88-144d091efd5c | -6.76182 | -42.79493 | 2025-10-14 12:17:00 | TERRA_M-T | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 5714e286-a02f-3f08-8b06-9492be9d694c | -6.43388 | -41.82344 | 2025-10-14 12:17:00 | TERRA_M-T | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 24b605f7-6981-34d4-a492-a3a781d19c21 | -4.39162 | -43.53806 | 2025-10-14 12:17:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| ae9cf943-1e33-3104-939f-e01264ae78ba | -4.62606 | -45.77267 | 2025-10-14 12:17:00 | TERRA_M-T | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| a4eb10a0-1427-3d44-93b6-d2115853fe2c | -5.91143 | -43.48599 | 2025-10-14 12:17:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 27.9 |
| faf577a6-9a3e-3d0c-8ee8-9ae34e2161d6 | -4.25582 | -44.87362 | 2025-10-14 12:17:00 | TERRA_M-T | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 62aa3e5c-f11d-3e85-9af9-5833a80e5a75 | -3.37583 | -43.04701 | 2025-10-14 12:17:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| b6c9b3a1-a2b9-30f9-b13e-3ccad7e804bb | -8.5388 | -40.40381 | 2025-10-14 12:17:00 | TERRA_M-T | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 96.7 |
| 9cb941ca-e62e-35b2-8ed8-04762a67bc64 | -5.72291 | -44.54549 | 2025-10-14 12:17:00 | TERRA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f10deabb-5453-3f2a-881b-10c8aa990ad2 | -4.39307 | -43.53176 | 2025-10-14 12:17:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 9849ee28-554e-303f-861e-47343fc69fd1 | -5.75083 | -44.51289 | 2025-10-14 12:17:00 | TERRA_M-T | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| f0f48071-6b2c-310a-b06b-8a912c142af0 | -3.94352 | -44.54272 | 2025-10-14 12:17:00 | TERRA_M-T | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 49a47e62-52a6-3071-a026-774519d73355 | -4.05615 | -47.2481 | 2025-10-14 12:17:00 | TERRA_M-T | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 64368c29-c7c1-3bc2-a422-7b7691c27f0c | -4.39141 | -43.54343 | 2025-10-14 12:17:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 438cfe84-e986-3432-a001-1eaf985f1b56 | -6.08636 | -44.67953 | 2025-10-14 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| a6bd33da-3788-39f0-a8c7-37f0f3a6aea7 | -3.82749 | -47.73911 | 2025-10-14 12:17:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 50318c1c-e8a6-37f7-9087-c2a1ef2873d5 | -7.54848 | -42.66229 | 2025-10-14 12:17:00 | TERRA_M-T | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 30.4 |
| 2cef1683-5156-3431-bf3f-e65e86b42e87 | -3.75654 | -41.68618 | 2025-10-14 12:17:00 | TERRA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| c2181fe9-d6ac-39fd-8ce4-f0db85ac0952 | -7.54725 | -42.66807 | 2025-10-14 12:17:00 | TERRA_M-T | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 65.4 |
| 6d085b37-b7e5-3e12-a92e-8d506000f10a | -2.83641 | -47.44904 | 2025-10-14 12:17:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9d51b307-be8a-33c5-bed6-3b3319afbc66 | -7.53304 | -42.69118 | 2025-10-14 12:17:00 | TERRA_M-T | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 24.4 |
| 0f5e09e5-388a-3c74-851e-9747d0193b80 | -5.72438 | -44.53507 | 2025-10-14 12:17:00 | TERRA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| c2a12fab-674c-30fe-8492-89e6049904f1 | -3.57394 | -43.68506 | 2025-10-14 12:17:00 | TERRA_M-T | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d2538635-b19d-3b06-912c-18407a9348a8 | -7.53509 | -42.67603 | 2025-10-14 12:17:00 | TERRA_M-T | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 68.2 |
| b3125165-ca91-3ebb-8673-6ff34628dd8e | -7.53398 | -42.68187 | 2025-10-14 12:17:00 | TERRA_M-T | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 37.7 |
| 685ffeb6-7b83-3387-bcf0-c30ecd1aabcc | -6.44579 | -41.82495 | 2025-10-14 12:17:00 | TERRA_M-T | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 28.8 |
| 9c629fa3-7023-387d-be28-0a3c46d6983d | -2.02507 | -47.69562 | 2025-10-14 12:17:00 | TERRA_M-T | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 91d61cb2-dfc6-371b-8caa-c4b9a5371f83 | -3.75866 | -41.67057 | 2025-10-14 12:17:00 | TERRA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 8cdd4438-34c9-3998-9378-c6e97fa786d2 | -2.53533 | -47.8044 | 2025-10-14 12:17:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| b649e182-2eaa-3f6a-826b-7093fb61d9bb | -4.11134 | -44.45399 | 2025-10-14 12:17:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3c84c874-54d1-3c42-b6ca-45015ea9046f | -3.0597 | -42.16331 | 2025-10-14 12:17:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 970ad3ea-deda-3f4f-94e1-0a898e2c6498 | -3.48052 | -45.66038 | 2025-10-14 12:17:00 | TERRA_M-T | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4b5e76aa-bcd9-3964-803a-d5ab79601569 | -4.73062 | -44.706 | 2025-10-14 12:17:00 | TERRA_M-T | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5ad8ab3c-7d2e-3373-b3ba-9a7c147a0224 | -7.53519 | -42.04485 | 2025-10-14 12:17:00 | TERRA_M-T | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 1abaac9f-8ffd-3dcf-b390-74cb1003e6b3 | -6.67313 | -41.49678 | 2025-10-14 12:17:00 | TERRA_M-T | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 20.2 |
| a30b8f5d-1504-331b-946b-f8a8815f24ae | -3.57549 | -43.67392 | 2025-10-14 12:17:00 | TERRA_M-T | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| d81b5a7e-7838-3016-8d18-140414d124a2 | -4.04351 | -42.51884 | 2025-10-14 12:17:00 | TERRA_M-T | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 75db97bd-0823-38a5-8f9f-5354e1a9f2e5 | -7.80471 | -38.73915 | 2025-10-14 12:17:00 | TERRA_M-T | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 50.7 |
| 1e2fcd5d-ab2c-3f58-a6fc-b771b65b950b | -6.67631 | -41.50363 | 2025-10-14 12:17:00 | TERRA_M-T | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 27.1 |
| 6ada1c75-22dd-3251-a18a-55f1414fdeea | -6.12647 | -44.94833 | 2025-10-14 12:17:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 94eaee3c-12b0-3c90-947f-fc3a20deebc6 | -7.79887 | -41.09018 | 2025-10-14 12:17:00 | TERRA_M-T | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 46.3 |
| 2cdbb6a9-dd93-3481-9d9f-47a2671a4dc0 | -6.43166 | -41.83996 | 2025-10-14 12:17:00 | TERRA_M-T | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 477c0f90-79ba-3233-b3cc-9491f823ac76 | -4.85631 | -42.54288 | 2025-10-14 12:17:00 | TERRA_M-T | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 28.5 |
| 17d7d5b9-643b-3c77-a695-a9323bb3a8a5 | -7.54642 | -42.67739 | 2025-10-14 12:17:00 | TERRA_M-T | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 72.5 |
| 58605e0c-1d06-3ebb-94ea-566a41f52408 | -5.94908 | -43.73212 | 2025-10-14 12:17:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| dcfa3337-c3b1-3872-8da3-a28d1d07d1b6 | -4.48434 | -47.66456 | 2025-10-14 12:17:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cc95f452-dafa-3c68-90c3-b2eecc35902a | -5.59539 | -45.37719 | 2025-10-14 12:17:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 70b87704-b4f4-34aa-ae3c-2e7a8d1e3144 | -6.21453 | -42.68547 | 2025-10-14 12:17:00 | TERRA_M-T | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 491f438d-13f9-34c9-ae17-b50e3171b8a3 | -6.44354 | -41.84161 | 2025-10-14 12:17:00 | TERRA_M-T | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 31.0 |
| caa00106-8e99-370a-a261-edbb5134dc68 | -2.82379 | -42.30115 | 2025-10-14 12:17:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 99d53146-f204-369e-bf54-e490ac9910e7 | -8.54478 | -40.40999 | 2025-10-14 12:17:00 | TERRA_M-T | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 80.1 |
| 8b27f4cc-ed8a-3b4c-b0e0-73b554f04f49 | -4.85823 | -42.52886 | 2025-10-14 12:17:00 | TERRA_M-T | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| d132636c-d9f6-389f-962a-3df4f3c0aaf6 | -8.92963 | -45.32032 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 589c4071-637f-3d32-b333-7c7023d46d9d | -11.13416 | -45.88018 | 2025-10-14 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 32bbb8d3-50a8-39a8-b8e4-278c333ccf3c | -8.92298 | -45.29808 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1118.0 |
| f552702b-9be9-35e6-a04d-b041a6f1d7d3 | -8.90674 | -45.27451 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 776.0 |
| b0db84fc-f637-348f-bf4b-fb69739699b1 | -12.92956 | -47.0785 | 2025-10-14 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 8ac38296-0099-382a-805d-494341ccbe4f | -10.15678 | -46.88503 | 2025-10-14 12:19:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 329428dd-c8d6-3068-b419-12f389ac17c6 | -13.77288 | -42.25167 | 2025-10-14 12:19:00 | TERRA_M-T | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 26.5 |
| eb6c48b7-415a-36e2-acb4-24734bb72972 | -8.95997 | -45.41577 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 500.1 |
| d502e937-2fa7-33ff-b0cd-e9153b34a0f3 | -12.678 | -42.03315 | 2025-10-14 12:19:00 | TERRA_M-T | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 85.4 |
| 0e824032-31cf-38b6-b22b-e6647849c15d | -9.4835 | -42.31849 | 2025-10-14 12:19:00 | TERRA_M-T | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 6207be1f-68df-38ac-91dc-9d610b810946 | -8.92153 | -45.30854 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 6ee88350-9576-376a-9f3c-5205087ee988 | -8.97091 | -45.40659 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1068.6 |
| c11b6e6c-7a51-3851-9109-e4a0a8c84ba8 | -11.13321 | -46.0273 | 2025-10-14 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 2e4d87bf-482a-3400-8446-63f11528d92e | -12.92762 | -47.03279 | 2025-10-14 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 5f15fc90-22bd-38d9-b862-3afa4cf4bde8 | -8.94129 | -45.33894 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 47cfd469-0f0e-32ca-beba-c193e3614b87 | -8.90004 | -45.25214 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 24bf7021-53a0-3d3a-92de-965fc9f2e119 | -12.59835 | -43.36977 | 2025-10-14 12:19:00 | TERRA_M-T | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| c5c5ec0b-886b-3b1b-9200-2e0ceb11a271 | -8.91719 | -45.33988 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 10ab21d6-5579-354d-a033-8a0d35fe92a3 | -11.33047 | -45.25957 | 2025-10-14 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 3dfff910-bc7c-3be4-b680-4e1cf17825bc | -12.93088 | -47.06875 | 2025-10-14 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| e5b019d7-8b5d-3687-8092-07409a6dc34e | -11.14194 | -46.07616 | 2025-10-14 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 9ed85d05-9986-30b8-8517-c07c17781c2c | -9.52128 | -47.86065 | 2025-10-14 12:19:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| ee820371-6557-3870-a6cd-b1e9201ed6b5 | -12.6756 | -42.05377 | 2025-10-14 12:19:00 | TERRA_M-T | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 28.8 |
| 773edcf1-829d-3df3-b6e9-b12265298b6a | -8.90818 | -45.264 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 58.9 |
| ef050a80-76b6-3b04-a86d-515c773694af | -14.07773 | -41.97899 | 2025-10-14 12:19:00 | TERRA_M-T | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 25.8 |
| c2fa957b-4d58-3f00-bce1-e89488c957b0 | -9.35752 | -48.66793 | 2025-10-14 12:19:00 | TERRA_M-T | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 49b34e26-bf0b-38b9-b622-560f99a3cea7 | -8.95191 | -45.4039 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 6cb9f62d-b74f-3f4c-a75f-16b11697cc0d | -13.83858 | -43.03179 | 2025-10-14 12:19:00 | TERRA_M-T | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 41.0 |
| bdf76d7d-8596-38f5-bf87-763637c27c00 | -12.71464 | -45.14198 | 2025-10-14 12:19:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 64.2 |
| d6ce379c-3bf0-3292-880f-a508477b10fe | -8.91486 | -45.28632 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 828.5 |
| be66b1fc-f6e8-36f3-aef2-b7c0f8f315bb | -8.95333 | -45.39343 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 03a4a0f9-0811-3500-8771-7d6cf8a13351 | -8.95896 | -45.352 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 90654d33-b6aa-3844-ae46-6c5206ef5c88 | -13.34127 | -42.38063 | 2025-10-14 12:19:00 | TERRA_M-T | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 22.3 |
| 9896d38a-fc10-3a18-8e77-6d838ac2cc45 | -8.96141 | -45.40525 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2009.7 |
| 467fa0c0-eea8-30e7-bb9b-6e3ab6a12ec8 | -8.93736 | -45.29574 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 23.6 |
| b877b932-af4b-3b22-a4db-ab86d2085527 | -12.90405 | -47.06845 | 2025-10-14 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| c8052569-c911-3e07-8262-d8395f859937 | -14.89395 | -46.02898 | 2025-10-14 12:19:00 | TERRA_M-T | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 4bde13e7-0d76-331d-92c5-0d5dc5f8f7a8 | -13.75806 | -43.51075 | 2025-10-14 12:19:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| ade67d8c-1ae4-3650-bd44-95e4c4abc0b5 | -13.93629 | -48.7104 | 2025-10-14 12:19:00 | TERRA_M-T | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ca812674-2f94-3cc0-9ebe-678d4f3b513e | -14.37857 | -42.30205 | 2025-10-14 12:19:00 | TERRA_M-T | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 39.8 |
| 4942ed47-0283-3af4-a1d4-284d322892db | -8.95047 | -45.41444 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 41.7 |
| b16b6be4-e1df-32f5-b507-bc5c05a5016e | -11.95026 | -46.97101 | 2025-10-14 12:19:00 | TERRA_M-T | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 10646fad-b512-3fc3-bb86-4597523f5435 | -8.93254 | -45.2994 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 526.6 |
| 3fbae6e7-c256-30af-9546-fcfe169ff467 | -10.81782 | -43.96248 | 2025-10-14 12:19:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |


[Clique aqui para ver as próximas entradas](README40.md)
