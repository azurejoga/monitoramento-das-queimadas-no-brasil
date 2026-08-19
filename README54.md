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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e94d6f6a-3ae8-3386-8c0a-6421c8a0ebed | -6.52805 | -58.60969 | 2026-08-19 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb9808fe-2793-3c6f-b203-bb201c49f3eb | -9.4275 | -60.42728 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 067538cc-dd63-3b43-82f8-8fb883e71261 | -8.55503 | -54.72539 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 13e24e21-afc0-3676-bfeb-6b69296f14ef | -3.10185 | -61.21761 | 2026-08-19 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11a3d3ea-d0d5-3a11-9cba-d3dff8eba8de | -9.39745 | -60.55633 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9ca964a4-23fa-3ef7-9665-fe142365f517 | -5.92714 | -61.31166 | 2026-08-19 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd5eae67-66fc-34e4-b3f7-e4a30e0cf918 | -9.11882 | -61.6062 | 2026-08-19 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4ad9a469-462c-3fe3-b613-5ce13067f3f6 | -8.55133 | -54.75149 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 70d9ae70-ba90-3a4d-b1bb-5c1720ca3498 | -9.01314 | -60.51432 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 987017b9-dcb6-3bf8-86d1-e2eef9c60543 | -8.19212 | -55.00193 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0a72b386-0623-302c-9b57-6328f7bb3cb1 | -9.40913 | -60.56897 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fbe71f3-01a2-3302-a11f-3c67556288ef | -7.60571 | -60.95201 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5e887f2-036c-3a29-bd6c-00e84ca30b28 | -7.61347 | -60.96741 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa98c14d-13c9-385e-8e03-71f840656c89 | -6.85909 | -59.03471 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03f9b0cf-e37f-352c-8551-b7551510691a | -7.06 | -59.84685 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0e2c797b-ac2f-39b5-b260-471e1a66a43c | -9.40085 | -60.57848 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aeeefa75-7647-3ee9-8623-1a131b5e868d | -9.39466 | -60.55229 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e9b6803e-275c-3b89-8891-c43adb1cf105 | -6.60918 | -58.40094 | 2026-08-19 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 931a57ac-0811-32a3-a5ad-a9182bd28ec1 | -9.14106 | -60.61013 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9354c48-116a-3b13-b59e-c0ab8cf99b89 | -6.63536 | -59.07543 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 07e10f10-37fa-3c35-9515-687265fe53e0 | -8.54892 | -54.76852 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a53f5abc-483b-30ed-84ba-8a1fde6bb5e4 | -6.88675 | -59.04205 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b5e876ee-2bec-3ba9-a889-69fd47c40c37 | -6.91363 | -62.905 | 2026-08-19 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77813c93-4f51-3209-a668-28fe58467696 | -6.86636 | -59.03896 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5cbef81c-1ee7-3e85-a7a2-dfe0fd70d51f | -7.6024 | -60.95149 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9bb6bb53-6a68-37c9-9566-47e23284809a | -6.80056 | -59.45102 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36524ecb-9857-339a-9242-67d60d681b95 | -8.56322 | -54.76366 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f3a3b7c8-ff15-3af8-bf12-6026f46f645f | -8.5595 | -54.75725 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 83bba3fe-a90e-3ff4-8f00-78fe27a71a78 | -9.15994 | -59.68035 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e93e1fc-0c7a-3bd7-869a-34bc5d55fd49 | -6.88009 | -56.41993 | 2026-08-19 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 235ea39b-3a7b-3b4c-86e5-0ddb195a1061 | -8.5682 | -54.76006 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0f77b9f0-6bc2-3a3f-965b-fdcc7a805508 | -8.57883 | -54.68114 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6a6c1a8b-e7cc-3855-89b8-8074c25403fb | -7.60739 | -60.96291 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa68652d-1d05-38a4-9acf-7286feb68480 | -9.16781 | -59.67408 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b54a4c0-c5e3-3c53-9f44-98b5c3fee99f | -8.08233 | -61.36209 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 684edf64-6c13-3852-9d34-899183fa96da | -9.42866 | -60.44194 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 270b13d7-47ec-30de-b4cf-6dabbe65b814 | -6.91707 | -62.90554 | 2026-08-19 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5bc4fb89-4a9e-3b6c-9b3a-b02b1bccd5b2 | -6.89265 | -56.44152 | 2026-08-19 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07fa6a61-f73d-3599-9c85-5c7f51c18294 | -4.01166 | -48.06364 | 2026-08-19 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 03821574-1b91-36a4-8615-7140c267abc7 | -7.60962 | -60.97037 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79b0b1d2-818e-353d-8800-dea72698a19a | -9.08251 | -50.80458 | 2026-08-19 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18541c8b-22f4-33ec-b7d3-ca9925091872 | -9.40248 | -60.56792 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6b59e55d-ab62-39c8-8def-ace8e225a214 | -7.43729 | -59.8001 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a512ea7e-cbbb-340c-8d43-fd32d73b7874 | -8.56762 | -54.7643 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 816a7150-33d0-3a6e-97fa-8fd62d0f3623 | -6.85626 | -59.03054 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7480f6a1-6a0e-30ca-a630-6b006e118af7 | -11.09639 | -49.91884 | 2026-08-19 05:23:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8fc35886-02bc-3b4d-84bd-dd505b4368a4 | -8.95673 | -60.52707 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ae13ec5-cdbb-3f37-b39a-1221b0610cf2 | -6.76104 | -59.1541 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf1052b8-4d61-3e95-a052-e754c719907a | -3.09905 | -61.19168 | 2026-08-19 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| baea6780-12e1-3581-a99f-5aa118f2e58d | -6.99407 | -59.05054 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f9c8f44-c789-331e-8bc5-6115932efa08 | -6.88081 | -56.41507 | 2026-08-19 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ed17a03-78bc-32d3-9570-beaa3112d8b9 | -9.17412 | -59.70127 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6acb65c-b86a-39d1-a1c5-231800230831 | -9.01809 | -60.50432 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90af6a83-743a-33d7-a247-130f10efa793 | -6.72331 | -58.59189 | 2026-08-19 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8f760350-abd1-3742-8fb9-68cdd107230d | -8.56614 | -54.74195 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| afcb220c-3609-3823-a237-ecfe325b44ac | -8.56996 | -54.747 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a7676b76-a181-3025-bac4-bc62f46d2b65 | -3.49614 | -59.63042 | 2026-08-19 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1e2b30f-3876-3509-a761-c62fb016118f | -8.54499 | -54.73272 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 837ab75a-a305-32f0-a741-a958757258d5 | -6.79774 | -59.44693 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 457522a9-7589-3765-899d-0cd9ffb2294e | -9.46663 | -51.60503 | 2026-08-19 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 49456f13-4c87-3d64-9782-afae2f84754b | -6.7538 | -59.17907 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cfeefd33-73ca-3a4e-9f64-c183eb4fd079 | -6.84831 | -59.01438 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ea89ae1-188b-34c4-9ed7-ba4f4e88cac9 | -6.63668 | -59.07513 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9693c22b-2b39-3a7a-9f47-69a52890303d | -8.56893 | -54.75414 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 67f91303-de14-3f61-a7a4-551408e92806 | -8.57082 | -54.74092 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7a7bf19d-f477-3fe0-8d33-7d83320f3ec2 | -7.05333 | -59.84584 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bed64339-fbf6-3976-8ce8-29147d08aba6 | -7.91581 | -61.72845 | 2026-08-19 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b21c4a2-ce80-3350-af06-b0f9ef21bd4e | -8.58465 | -54.77112 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 79b70b95-704c-3d98-b32f-63f1f719acf3 | -8.56907 | -54.72019 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ebb4ec95-cd06-3e6a-81b1-d83444812179 | -6.69789 | -58.94616 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 3c9c9b19-5c84-3d87-868b-f548022d799d | -6.7698 | -59.45764 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b400db2c-0860-3d35-ba44-428b10332ea0 | -8.56271 | -54.76628 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 36c66ba7-1286-360a-9a93-ad8bf121f864 | -7.91138 | -61.73494 | 2026-08-19 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0eeab0e4-8c0e-3450-88dd-96829277c6b0 | -7.60625 | -60.94854 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4aa1065-94d0-328a-aa42-8bb0942da161 | -8.57319 | -54.75635 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fb88301c-7c72-3c6f-899f-c4271574e5b0 | -6.8557 | -59.03421 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e477e48c-fbb2-3074-afee-4e43259faf7b | -7.53846 | -55.58418 | 2026-08-19 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d1d63e3-0195-3934-b550-445cd71dae62 | -6.88951 | -56.43616 | 2026-08-19 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c647e672-622b-38c4-8d35-c91661f2010e | -9.02305 | -60.4943 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f701a4a4-d08c-3c8c-99e0-c699ece8077f | -2.77113 | -48.57391 | 2026-08-19 05:23:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c54cc28b-c29d-31e6-9eba-be3df16b4f65 | -9.40194 | -60.57144 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c51dc75a-7010-391e-b252-3ed81486437c | -6.85682 | -59.02688 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b84651fd-9a3e-39e5-abd1-3b1388a9e409 | -9.42742 | -60.40555 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a47850bd-0a36-316e-89bb-ec497bc28d23 | -6.81172 | -59.44544 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2be435e4-7713-348b-a3d7-6fa66c6660cd | -9.42037 | -60.45151 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2dd909f8-c484-3cc5-9af7-3366bef90945 | -6.7428 | -59.03918 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e80f8d28-5a73-3467-b0b2-b7749d7a930c | -8.54316 | -54.74572 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bf5cd921-6d9e-3671-abf6-0a6c91112e71 | -8.95341 | -60.52656 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c0f18da-3213-3054-ab67-692c47842170 | -9.4092 | -60.5906 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 244ba758-fdd2-3518-ad19-a5fb236fe2d2 | -8.56434 | -54.75534 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 80cbf353-a870-3f51-852e-906053e12672 | -8.56888 | -54.72294 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| aa8f584a-f4a3-3add-8400-35bc9ff66562 | -8.50498 | -54.85832 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 83de4224-8bc6-3e6c-9107-32e014563294 | -6.83598 | -56.45273 | 2026-08-19 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c6f5e12-0d10-3c8e-b536-976ee399135f | -9.42091 | -60.44798 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ce16c6d9-26ce-3f4e-8814-be66da061b23 | -8.21842 | -55.01921 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1700283d-6938-3d8c-8fc2-d4fea49cf456 | -6.70923 | -58.94028 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4838c4c7-7681-3e97-9427-269f0b69d122 | -8.54818 | -54.74202 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 63198996-77be-3ca1-81f0-1f64c3d3319a | -3.45899 | -56.80983 | 2026-08-19 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 590cacb1-ee12-385c-9d89-14a1c82de087 | -9.42471 | -60.42323 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 33067d70-9898-392d-bf86-eebc3328375d | -6.86925 | -58.94606 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README55.md)
