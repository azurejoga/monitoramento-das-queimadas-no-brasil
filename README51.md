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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1682c481-498e-3c7c-951b-5039eebea000 | -13.0759 | -57.13306 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a03dfe1d-4396-334b-9407-32a472114718 | -9.20507 | -59.64291 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2aeb1d9a-0bb6-3d99-9bce-facf8b07d48e | -13.14602 | -46.86233 | 2025-08-15 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4bd3198b-78ab-3c7d-9b1e-1ce8c3856bd2 | -7.46149 | -59.88928 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35e615e3-8a3c-3b2a-816f-53f0c61a69cf | -6.66736 | -59.08377 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32c6dbc3-1e66-3fa8-9558-d1777deb2c56 | -6.06461 | -59.96039 | 2025-08-15 04:51:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b2af4e8-6a02-3dad-aa8b-93921956c8af | -9.16845 | -59.69792 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de429912-3d0c-3333-8154-f7a5e66fb45d | -6.87768 | -59.14809 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07390f85-0731-3fbd-a090-a7a3f8ff5cad | -6.89663 | -59.14274 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d44edc8-ce84-3897-bd4c-d84bbbd56f9d | -11.93359 | -63.24627 | 2025-08-15 04:51:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af304659-4833-3c9b-a424-4538eea144b5 | -6.95468 | -60.12788 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9cf3adbd-5b91-3c66-b1bd-cd39aad1af7f | -11.28642 | -49.11532 | 2025-08-15 04:51:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0247359-73a2-3a6b-ae86-bc5210a6787d | -11.34424 | -55.40599 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0acdd363-64a0-3056-b50c-5d0113b55d5b | -14.05385 | -46.2973 | 2025-08-15 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 62e30b70-cf2e-3c11-96a5-340c0bfaa253 | -6.07016 | -59.95622 | 2025-08-15 04:51:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b787c293-25bc-370f-94aa-870f3d9226fa | -7.28733 | -57.6529 | 2025-08-15 04:51:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b65bf8b5-d2b1-37ec-ba8a-7472e6715929 | -7.87315 | -61.81387 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d495da9f-0cdc-38e6-ad0a-e831a3960a07 | -9.50457 | -60.51959 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d225b695-f972-3b0e-bcfb-0c5e1ec7448d | -11.35539 | -55.42296 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0341d8b5-0a51-3c43-a05b-9666fc9c4208 | -8.28962 | -44.99707 | 2025-08-15 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3377ad49-1e06-3a95-9dbe-ad25833aa431 | -7.93478 | -61.76744 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2c6c2dea-6b0b-350d-b6dd-aa1f36c14bf2 | -9.92107 | -60.48224 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a2b648a0-578a-3604-8789-39d088b2f795 | -6.87183 | -59.15586 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57a35b93-d433-309d-b192-e42e3c96806e | -10.0119 | -58.43045 | 2025-08-15 04:51:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 994bc851-cffb-3c9b-92c4-1632c7671267 | -6.90029 | -59.14776 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5f9f909-8f1a-338f-90df-8bd120a8f999 | -9.20211 | -59.65999 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 25017a9b-da60-3024-99b5-a11202cc12ad | -7.07871 | -59.21389 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7829a17a-ccc6-319d-b3c3-82c4e395c48c | -7.23767 | -57.66376 | 2025-08-15 04:51:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a7972d8a-a6b2-3f01-928a-02b8260e7f30 | -10.46844 | -61.33248 | 2025-08-15 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bfd8a620-7a8c-3c81-a87c-81f385fa399a | -6.66545 | -58.8221 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b042aeda-2159-3052-8ab8-7f5eb0b15d3f | -7.81755 | -61.32896 | 2025-08-15 04:51:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ab02670-241d-30ff-9981-579a5b86b606 | -9.78553 | -61.50764 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99c13f17-2490-3970-b151-881c5d1f5f43 | -6.69665 | -58.83411 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2a579fa8-dfda-3005-89cb-d182afcd92c0 | -7.27086 | -60.63194 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c15c65c7-fc71-3e27-983a-a61b04d870aa | -8.29382 | -45.00348 | 2025-08-15 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 033742c3-ba97-3d5e-8f32-6cdeb8121fcf | -8.1024 | -61.19987 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f13d98f-08d8-3780-96ec-1da071281f73 | -11.35658 | -55.4156 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3110cb3-a169-320d-b65f-d222a30e9cf5 | -9.21444 | -59.66676 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c41e13e6-1e10-3196-91c9-76c21fecde3d | -9.60541 | -55.14093 | 2025-08-15 04:51:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8820bd48-10d3-3214-8d60-8e94f583ce4d | -12.42057 | -43.49173 | 2025-08-15 04:51:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52905136-cbf6-3749-9b4a-53c84ab1bff1 | -7.0758 | -59.20452 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af1d09a4-4338-360a-8300-864ae144a65a | -7.88335 | -61.80782 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c735a057-35b6-3574-aa90-dfe00200e8c9 | -13.32643 | -45.23229 | 2025-08-15 04:51:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26fb5567-a1c6-3d21-be5c-34700d94670e | -7.52478 | -61.3799 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3a446f32-bbc4-3016-87e8-b19ca2f6be59 | -6.71662 | -58.82088 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6ab7158a-7c09-36b2-8357-2488238f76de | -6.92968 | -59.53049 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9dfcb9ef-332b-31c1-b424-e3b6fea9d364 | -6.72161 | -58.81754 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 131ca3a3-e7a5-3d2a-9822-e649b3ccaeeb | -7.86974 | -61.82468 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 787365be-ae98-3b89-b230-a62e03479887 | -11.3542 | -55.43034 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 66b7f891-86b2-36aa-b6f1-063c37de613c | -11.31838 | -55.20269 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05383244-665d-310a-8b76-04a0a5ce2dee | -7.95296 | -61.7548 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aecc65d9-4b37-32fa-ba38-6bc5c54f7e81 | -7.09188 | -59.21614 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c14dfb3a-5616-36c6-859d-1998bd8d5dd4 | -7.53572 | -61.34813 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 67cb76d1-f4e8-3e18-a7a9-e7d3878f3110 | -7.61632 | -63.52335 | 2025-08-15 04:51:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f841661-0d19-3813-8a23-6938888e8d0a | -10.36586 | -67.71516 | 2025-08-15 04:51:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 25c0de1e-b681-3166-bff1-277ab5857b9f | -7.08888 | -60.03135 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1caba17b-2d68-3499-9c00-a439e36bb621 | -7.55984 | -61.41694 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a350fc5-b35c-3529-9408-c7bba542d137 | -11.94604 | -62.83808 | 2025-08-15 04:51:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7b1c2845-7310-3608-8dd0-b84d88b8262d | -8.52194 | -43.29474 | 2025-08-15 04:51:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8e8d8e67-d713-3b24-a0d2-eb070a5989c4 | -6.87722 | -59.83633 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5422349-697f-30b4-8535-2f8e87669a6b | -9.39548 | -60.54427 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8b417093-d9fe-320b-b23c-6debb9938012 | -9.17884 | -59.66438 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5eb979b8-187d-3680-b378-9bdaa7277558 | -7.88122 | -61.82813 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 924433db-2e1d-36b0-a300-10443f520ee1 | -7.14714 | -59.63427 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df696c2c-b23e-370e-95b0-6a7e4a62f12b | -9.20572 | -59.66511 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc4b7b1e-b175-3554-85a9-d39411f4278b | -9.18946 | -45.32916 | 2025-08-15 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5880dbc2-a83b-39a2-ada1-a343e8bb876a | -13.12922 | -57.16382 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 964ba3a8-c2a5-3369-aefd-43d7567d29cd | -7.53122 | -61.34428 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2d2f205a-277a-3225-8f23-de9d3c6387b5 | -11.73016 | -64.89748 | 2025-08-15 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0761c8f8-c1b2-316e-b7f8-bd624dcc35c6 | -7.31695 | -60.62371 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 58c46074-5a7c-3350-bf1c-a3bcf862b64e | -7.9559 | -61.76808 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d549065a-f117-3f38-97fb-5a10f4aed545 | -13.47429 | -56.66385 | 2025-08-15 04:51:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 827c717f-f48d-3fff-9dc9-0172e5e1cd2a | -9.49915 | -60.54433 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 43f7f63f-7d58-3851-91d3-cb1fd7b41548 | -13.88951 | -45.55939 | 2025-08-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 367cd88a-db5e-3981-b772-555784725255 | -6.89957 | -59.152 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 699c4194-65ee-3260-89bd-cc93044d41c9 | -6.72092 | -58.82162 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11b4eb34-135f-3688-9419-fbecd85e36c2 | -6.94121 | -59.82005 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b921196-3cfd-36f9-a1a3-d8bb983f2539 | -6.95636 | -60.11805 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| eb958163-500c-32f4-b2a5-b8242dc10982 | -7.58545 | -63.46252 | 2025-08-15 04:51:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa6e8c14-67ee-3eb8-93fd-5a151aa54fef | -7.88002 | -61.80549 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 822c7018-9467-3d6e-83b7-e66b3679a083 | -7.12756 | -59.64002 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 744402b3-5155-3d64-a38e-a052b15f1876 | -7.59817 | -63.52418 | 2025-08-15 04:51:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3d074a7-e6a5-352a-b6eb-b97dbde51af5 | -7.4275 | -60.03362 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45913592-d1cb-39e8-a7f1-dc42e5f4b29d | -11.34922 | -55.41814 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 13c93397-4ef8-3016-b589-b104fe05d07c | -6.68944 | -58.8245 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8071ba0f-558a-38ac-a59e-a9b8122ee094 | -11.77936 | -47.39332 | 2025-08-15 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57226ce9-d786-3864-a51e-9de8c4825cb3 | -10.04851 | -59.35969 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 041a6d4d-1f3d-3e4f-88a3-6588fe2cc05d | -10.58124 | -55.41754 | 2025-08-15 04:51:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb150391-732a-3209-a521-76110997801c | -7.6279 | -63.52556 | 2025-08-15 04:51:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e94fb875-351f-3280-8bb9-7eea214151c1 | -11.35379 | -55.41135 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c87e6105-94a4-3964-946d-f2d8cdcef7d8 | -6.89081 | -59.15044 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8b1d184-4cc9-3014-88be-c64003903644 | -13.12488 | -57.14599 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 997180b8-ee98-3ae3-a9a8-8671fcbc9a5a | -8.31794 | -45.01258 | 2025-08-15 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5dab4786-d07f-3308-86cd-ec8509218894 | -9.50289 | -60.52921 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| cf2a70d0-13a5-3008-bc6c-02d67a7a9c1f | -6.71954 | -58.82971 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9f6aea1d-c6aa-3828-bb64-75e5efce1356 | -6.88715 | -59.14545 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5ea0de3-c60b-3ce2-add5-6b23a92965b3 | -6.92363 | -59.53876 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ae76f152-70d1-3abb-9ca9-dd9518240927 | -6.94658 | -60.14703 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e4fbe2f-0bbc-3345-8e29-b78ce48fa06b | -8.11212 | -61.20853 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6033b09e-12fc-34d1-be86-7ab337b234e7 | -6.71163 | -58.8242 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README52.md)
