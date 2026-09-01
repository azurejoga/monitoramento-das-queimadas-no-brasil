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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 827283c0-cb44-3641-b537-bd484f7231c8 | -10.80707 | -50.70864 | 2026-09-01 05:16:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 729b6126-9fcd-3cb7-a1ec-4915aeb9ac18 | -6.94076 | -55.63594 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7cf0b056-559b-3593-927e-d5a6842ad97e | -6.93188 | -55.62741 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb577889-0066-3119-b822-f0da7fcf2317 | -7.58037 | -61.3341 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21b159e0-43eb-348e-951b-d61309ebbc70 | -9.15046 | -59.53892 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01a2e879-b3a5-3b52-b3c7-d11fa9be283c | -6.18866 | -57.73769 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed49668b-b3f7-32db-8af1-f3d0f3c70049 | -6.18643 | -57.72972 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3c978d3f-03ee-318d-8fe3-ecfbd1c56fce | -9.40981 | -51.67545 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 252c0530-22a3-36dc-a411-aedb6f36c177 | -8.61607 | -54.78685 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1261c99-a770-3947-af7f-1b7d8436135c | -5.97076 | -57.68008 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4d169327-e861-346d-ba07-d9b49356b370 | -6.55571 | -55.13528 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c78559ad-4743-3f99-8cd6-0b091cf7181e | -6.63024 | -53.17377 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e0db7f0-8f42-3946-b6f9-5f67b96180c2 | -7.55855 | -54.9943 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1009394-81b0-3246-9548-2fa4fee5435c | -10.99001 | -48.39505 | 2026-09-01 05:16:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 23128a37-8718-317f-abb4-d57a5784e3a1 | -6.11889 | -53.54876 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b4f83b29-2b7b-34e8-a293-6ce920ca39c8 | -6.25726 | -55.4247 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 139045db-31dd-3036-b16d-b1b41dce3303 | -9.41381 | -51.67606 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 692de648-1f06-32cf-8ec8-68902f6ad985 | -4.96206 | -55.84452 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39039d06-b6ab-3b3c-9814-97610a6a9f96 | -8.84789 | -47.07975 | 2026-09-01 05:16:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 955e1f8b-f2fd-35db-b7f3-6d25df315133 | -9.46648 | -57.01524 | 2026-09-01 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f1eba4a-2425-3ee7-b1d3-1e968357ade2 | -6.2639 | -55.42575 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 30644d64-f6d7-328e-8c60-d8cbe1a58a7c | -5.25636 | -55.9087 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24933b8b-d379-3a7e-8a6e-76a089fdc243 | -7.57692 | -61.32978 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5064f3c3-a835-3d60-92d9-be0313246cc7 | -11.31246 | -45.1897 | 2026-09-01 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 220c8171-6869-358e-ac74-3a263ccabc12 | -7.56742 | -61.36588 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c34330b1-ea72-3e10-bf9a-7a27bdbb8ed6 | -10.35297 | -50.01254 | 2026-09-01 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 4b2b628b-b4d9-38fd-819d-ffee446918bd | -7.3574 | -60.58287 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| d6628891-fc21-345e-8891-51172dac7bc8 | -6.75563 | -56.3365 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b4b22b5-1797-32eb-8cbc-1895d136e2ef | -5.34524 | -45.15979 | 2026-09-01 05:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aa319cc9-e867-3c7a-9c5b-b45db832e916 | -6.80043 | -59.43747 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dde49475-7bd8-3741-9d29-f5678f86a418 | -6.41645 | -52.20058 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4d1eaf44-0a33-319e-9183-3c899034cd8d | -6.27505 | -53.33371 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f88857dc-8915-3100-997d-4a677ca755ba | -7.58371 | -60.47551 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| f6c30344-4285-3c4e-9a27-e637b6177b01 | -6.59212 | -58.58931 | 2026-09-01 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3cb0c6b7-cfa6-3b4a-83d7-af7c23c9a033 | -6.25671 | -55.42818 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 840d00d0-4d09-302b-a7dd-b6ade2181207 | -8.50548 | -55.29824 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30c801d1-1a99-3999-9e73-754f3116afaf | -6.89333 | -59.05584 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3234b8b8-0b5b-348a-9484-92ffff49e5d6 | -8.41872 | -44.99666 | 2026-09-01 05:16:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d887ed83-e1a9-32e8-8701-5a4c3015b798 | -4.76904 | -41.80444 | 2026-09-01 05:16:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3b272ceb-9cc5-33fd-97c0-9ebe46b208cd | -6.10759 | -57.86674 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c553a48e-5c7d-35f1-a53f-c90aa3b1073f | -7.34096 | -60.58516 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e42f6c46-6825-3be5-8c7f-a68a1da4c044 | -9.17957 | -51.55333 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7579a506-b3d3-379a-b42c-b0bf89fadc3f | -7.68449 | -55.34052 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3dfa76ca-7465-3c47-9af3-7befa91add8d | -6.93911 | -55.64638 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4317839-7b98-390b-9ff9-dee7b8ba098e | -8.78193 | -62.49807 | 2026-09-01 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82bf4f8d-3e6c-3480-8099-eee49e7f28d7 | -4.76642 | -41.79826 | 2026-09-01 05:16:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5a2a112a-e25d-390e-8d25-0109717acaf6 | -10.83322 | -50.71237 | 2026-09-01 05:16:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f068c4ff-7d86-3645-a9ae-d2f4171f49ae | -7.69118 | -55.34157 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4f11614-b86d-3b40-9727-dbfe29d0657e | -6.95406 | -55.63805 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6cc50710-f4c8-3406-a38e-e8612a7ef655 | -10.83381 | -50.70816 | 2026-09-01 05:16:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 683c7ade-10f0-3ae0-b1d5-84d47fdc5272 | -7.34651 | -60.57599 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 01e7986c-e281-369c-b219-1db55b6a5399 | -5.88158 | -52.0709 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69c158c9-5ca7-314e-b115-b9ff0f84d059 | -6.25338 | -55.42764 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40d0055b-7a64-3a3d-a3dc-d8eb21cfc416 | -5.94552 | -57.68362 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7ff4e7b1-84be-3afa-b2f4-6719425fab6e | -11.31314 | -45.18403 | 2026-09-01 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4e00aed3-71d1-3241-9d7c-8d9f963b6eb6 | -9.17315 | -59.60982 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b768a32-ffd7-3356-8ce1-0b83b957bbd5 | -10.99514 | -48.3957 | 2026-09-01 05:16:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 89298166-fbcd-3ed3-9cb9-70d17ce0f8f0 | -7.53164 | -61.37839 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4c601c2-e8ba-33a6-8cbc-27021d66471a | -6.8378 | -59.45535 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f47c5d3b-e11f-3748-8127-a3874c955403 | -7.56212 | -60.46211 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8cc00fcb-b091-367a-97e8-39a9cb951d46 | -7.56932 | -61.37341 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23054c43-5fd1-36c7-832f-0e0536876938 | -6.81587 | -59.67777 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40a64b82-b504-3f13-80ad-0b1b5ef3c339 | -10.3536 | -50.00793 | 2026-09-01 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ddacb851-8568-3f6a-ab5b-d2c64fba49f6 | -8.61833 | -54.79473 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b147b9a-2fa6-33c8-95c1-4afb4f0f97b4 | -6.08726 | -57.71812 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de9388a1-d9b2-3194-b3a3-3c124543c8c9 | -8.79276 | -62.48727 | 2026-09-01 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a21de3b0-3cc7-3669-ab23-819a61a216d9 | -4.3838 | -55.15749 | 2026-09-01 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9bc6a818-dd6f-3ae2-8c0f-348f81036c6e | -10.82274 | -50.72376 | 2026-09-01 05:16:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d7f16d4-965f-338d-938d-061cdd78f404 | -6.8106 | -59.57231 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f0193b3d-e200-33bc-9538-22db15a0c886 | -6.69365 | -55.40414 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f80a7c23-f370-3f24-8308-1042efe68276 | -11.49318 | -45.09799 | 2026-09-01 05:16:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f39f9c7-2898-3eb3-abe6-c1ddada353e9 | -10.34451 | -50.00664 | 2026-09-01 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1e86dee0-6a0d-320a-8b2d-0aa577e32e8c | -10.2086 | -50.31953 | 2026-09-01 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c6c04fad-b0ba-3a66-8cd5-279f14f624d8 | -9.6695 | -50.85968 | 2026-09-01 05:16:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a62f5bd0-e17c-31bf-979a-b12921870666 | -10.20258 | -50.36318 | 2026-09-01 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b539e7aa-573a-3236-924e-adc6647e7c8c | -6.67824 | -58.7461 | 2026-09-01 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06053b9b-2cd7-352a-98f9-b003cd1879d0 | -7.48221 | -61.39613 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af7e9e9c-64e5-3292-a474-9bf260a72c88 | -7.56868 | -61.37706 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28f25dcd-9790-365f-8861-75cfdd4a4f65 | -6.93356 | -55.63837 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea315bb5-3e2c-3aa1-a0c3-f325b8df14b2 | -7.02827 | -55.63896 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e45b682-c1fd-3077-b81d-746c9fbc9e47 | -11.48877 | -45.09823 | 2026-09-01 05:16:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 339d2040-b6df-3cf4-92a4-670db68a05f8 | -11.48236 | -45.0805 | 2026-09-01 05:16:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fe08c578-6019-3d4a-8643-574ecd58ba78 | -6.95351 | -55.64153 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 933deee2-1e0b-37e1-8138-d2c405fe9954 | -7.02439 | -55.64193 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 067f33c4-8a9c-3608-8b59-7d3d5f0fe7f9 | -8.6268 | -54.85216 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d7bd5386-a36f-36dc-962e-24e488a357ef | -3.09532 | -61.22065 | 2026-09-01 05:16:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5b78952-d82b-380f-8794-98aa9500a169 | -10.03542 | -44.69967 | 2026-09-01 05:16:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b94ead9-0892-3d3a-92e1-3b79e872d52e | -6.12532 | -57.67855 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 664f9a15-708d-3d13-9357-646ed7289d0a | -5.89155 | -57.7637 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71b77bc1-bcca-309f-a885-1bedaeb52959 | -5.4833 | -57.15171 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d98bd266-cf54-3ffe-822a-08230363229f | -7.92206 | -44.22977 | 2026-09-01 05:16:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7bff0b21-8ea0-3f8e-b10f-7c4b38a43a05 | -9.14822 | -60.94306 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2ab6c0f1-f72b-3b55-a82f-9b4da73e14c5 | -8.61604 | -54.85421 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 11171868-6ee4-3383-a075-1b68842b4af1 | -9.15225 | -60.946 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 55c27958-bcb7-3ad6-9537-aff7068a445f | -6.15675 | -57.78226 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87832b19-b874-3c91-a954-067c7c9b9441 | -7.57902 | -60.4798 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 64ad91f9-17c2-3943-a719-03343889b5e5 | -7.58105 | -61.3345 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b3ce92f-eb16-3ced-9f14-2a116829ae7c | -6.96025 | -56.43311 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9f5cd380-a0ed-31b3-b71e-d532b1066ed4 | -8.04566 | -61.73735 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 179e59c0-f1a2-357f-8db4-dfe0a0d030e0 | -5.4861 | -57.15588 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README60.md)
