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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3310b41d-b3eb-3ced-9db0-8cc5a48f1a13 | -6.00262 | -53.55185 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd6a634f-9a6a-3791-8126-084913b91870 | -5.55468 | -45.26114 | 2026-10-04 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef14247f-93a0-3068-8ae2-08f9eedbd851 | -6.06638 | -53.47294 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65b3015c-851a-30bc-895a-a94ed970b3ac | -4.43206 | -55.23925 | 2026-10-04 04:57:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d16daa49-f9ea-3398-ab0b-8ee7d6922172 | -6.32967 | -51.13783 | 2026-10-04 04:57:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2599afc8-541a-3ab2-be56-e928a58eb1f2 | -6.70819 | -45.97112 | 2026-10-04 04:57:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05064e00-3101-39c6-8582-890d470e9075 | -6.71225 | -45.97171 | 2026-10-04 04:57:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aafcdc2b-75b4-3c86-81ed-5242a867d12e | -6.21558 | -53.26355 | 2026-10-04 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc2219f3-6f0b-3b83-a8b1-98459d27da06 | -3.87032 | -55.8047 | 2026-10-04 04:57:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 32af2483-274f-34a2-b848-3fc12c3fdfb6 | -6.20936 | -52.79988 | 2026-10-04 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36a0cee4-205a-3bb5-9c8d-c3097a2b15a1 | -5.64116 | -51.75993 | 2026-10-04 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 49216476-df07-3f44-87e3-cb4a41954dba | -4.13075 | -54.16301 | 2026-10-04 04:57:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 026214d1-6702-3c24-be57-32dc087cf85c | -5.80634 | -50.12478 | 2026-10-04 04:57:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 93fcae76-0ae4-35f5-a9fd-acfb548ae9a2 | -4.46533 | -54.96672 | 2026-10-04 04:57:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f7501d62-4fb8-3a0e-9fc4-ea517c636be2 | -5.63781 | -51.75939 | 2026-10-04 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1625106d-f577-33ba-b6da-9cc3bab97a18 | -5.86353 | -55.70517 | 2026-10-04 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 770a4fe7-6cd3-3940-bc64-0eee42975ee4 | -5.86703 | -43.59725 | 2026-10-04 04:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73532fb6-c0b5-3d53-a506-813905b01bac | -4.81781 | -49.28622 | 2026-10-04 04:57:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 036dc704-4a74-32d2-9308-c61e0dcfe838 | -10.22114 | -59.09108 | 2026-10-04 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bbc5a12d-b2f3-3a72-9725-a9c19030b688 | -6.2809 | -53.15527 | 2026-10-04 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa761719-d839-3793-9aa1-2945facbaf4d | -6.00196 | -53.55583 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cde72603-1d3c-30de-a333-f0f2c5a47235 | -9.01715 | -65.7043 | 2026-10-04 04:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5a5d1b35-7914-32da-9ee5-694882a11dac | -6.00011 | -53.63354 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 070d582b-89ea-3c5d-9e85-9d555c697e73 | -8.71042 | -61.39313 | 2026-10-04 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8eae1f29-70bf-305e-bd7d-a3569affd19a | -5.73846 | -45.15054 | 2026-10-04 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9e65185d-700b-3afa-a319-7f6dc33397d8 | -9.30535 | -49.64623 | 2026-10-04 04:57:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cb37b193-3d95-38d8-aaca-8e8dcbe5539c | -6.19608 | -52.80215 | 2026-10-04 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55168acb-59b6-3e58-92e7-5dc8f4a9205d | -4.82246 | -49.87066 | 2026-10-04 04:57:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b739098-6ddb-3ecf-bfcb-7438402a5548 | -5.9984 | -53.55534 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24f35fc0-01d1-3173-b047-7d74dab21688 | -5.7421 | -45.15508 | 2026-10-04 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5a7fa8fe-4b97-3421-bb10-ea5d46fb7d6e | -9.08368 | -61.15616 | 2026-10-04 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 380dc8fa-4cc4-3c26-b339-9d73b6917437 | -3.86912 | -55.81216 | 2026-10-04 04:57:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c9742883-fa3e-3ec5-ba25-83737ff99680 | -6.23359 | -53.15214 | 2026-10-04 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a44b7b85-12d6-3748-a54e-0b5100346cdd | -6.57357 | -44.14737 | 2026-10-04 04:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2fa1a742-a7b3-3389-9938-30590180cdfa | -5.99945 | -53.63758 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7af59e1-b2f2-316a-92a7-fa3d4be39f6a | -5.83022 | -53.50514 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 024b9716-beb5-3c93-8db3-58acc846105c | -6.01719 | -53.52962 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c2be6d4-be3e-3f92-8ce1-a2109773e7c9 | -5.82668 | -53.50456 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84fff989-df90-3095-9cd7-a77354922146 | -11.82094 | -43.536 | 2026-10-04 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18b38142-b42c-38ca-8618-32f6695cf936 | -5.57244 | -49.74535 | 2026-10-04 04:57:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6190e571-9edb-3700-8bbf-a55ccc152dbb | -10.24576 | -49.65777 | 2026-10-04 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4632a048-eb7d-3a7b-89a9-c178487bcf30 | -3.84639 | -55.84686 | 2026-10-04 04:57:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a5e386a3-c709-3226-8ff1-7d0d46165248 | -10.22578 | -59.09204 | 2026-10-04 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12eb1d27-16a6-3c1a-9fe7-7016255f912e | -7.19731 | -44.31561 | 2026-10-04 04:57:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 45f6b1c9-2f66-319f-986f-8c02281aae17 | -6.21905 | -53.26425 | 2026-10-04 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc86d4a1-85e1-3211-b6cc-a10067cc3bbe | -10.22316 | -59.09445 | 2026-10-04 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01ec19e8-c039-3303-843a-9444cc345d6e | -6.46465 | -49.91278 | 2026-10-04 04:57:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0f600ea6-721e-337d-a6f1-bdc428e25cf7 | -10.24982 | -49.65445 | 2026-10-04 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29a3bfbc-b98c-3978-a5f8-3fc59a3dd562 | -6.14009 | -52.77775 | 2026-10-04 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3f3371b-07e5-3b01-a0b4-c5ff16bfd99b | -3.94294 | -55.83896 | 2026-10-04 04:57:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4e7e2875-8600-3a08-a70d-0f4ec7e15936 | -5.55049 | -45.26049 | 2026-10-04 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96ff8b8d-8254-3c46-a750-05e9f435aac2 | -6.06927 | -53.47741 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8db73441-4d8f-3274-8972-064b495777b0 | -5.73905 | -45.14657 | 2026-10-04 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b7b9f77a-50ce-3672-86ad-4b308f882221 | -6.30371 | -43.33974 | 2026-10-04 04:57:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e393d484-58c9-320c-9801-97508bb47eb9 | -4.20946 | -53.46584 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2b53e81-081c-3c8d-aba6-5ea64c2fab23 | -6.07924 | -53.48302 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b2b0d8d-db5f-3f55-a398-3caab4f6fe16 | -3.86972 | -55.80843 | 2026-10-04 04:57:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| ff39d535-7968-3b27-9a81-84a35ae97e93 | -5.54992 | -45.26442 | 2026-10-04 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5bd34571-f7e0-3f64-afeb-4ab598dd52c5 | -4.54246 | -55.97422 | 2026-10-04 04:57:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da9ab110-a93d-3fec-a1fe-c5b047ba02d0 | -10.8054 | -55.58064 | 2026-10-04 04:57:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f5e07c1-8045-36b6-9d49-8970885b4509 | -4.81561 | -54.72933 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4bedced8-209b-3175-b9d5-d75296fcf132 | -3.93878 | -55.8383 | 2026-10-04 04:57:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4608f038-680d-39b7-84cf-5ee1d776f86c | -6.32912 | -51.14129 | 2026-10-04 04:57:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0acfb56-3655-3189-84bc-61a4b1948811 | -5.86595 | -50.15925 | 2026-10-04 04:57:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41031c9e-e589-3f67-8765-24526a01a6f4 | -4.54601 | -55.97862 | 2026-10-04 04:57:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe2e1260-08f9-3e99-97d3-4ea3c4967987 | -3.95684 | -55.78004 | 2026-10-04 04:57:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56e50a33-17cd-3107-a715-b04a1e97d5d7 | -5.78314 | -49.84743 | 2026-10-04 04:57:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc60d523-1593-3397-bef1-bf53256dba7d | -5.84237 | -53.8208 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79fb651a-5f20-321a-9bfa-0ad9d663b2b0 | -9.70073 | -57.45697 | 2026-10-04 04:57:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6d76a9e4-0659-3185-9f32-26ee0406c2ad | -4.81776 | -49.28243 | 2026-10-04 04:57:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f88b21db-1e96-3c59-96ed-56f38e3be04c | -12.1939 | -57.12169 | 2026-10-04 04:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a9dae1b-4923-33ce-8d07-3a8e9f40fbfd | -9.91617 | -65.04345 | 2026-10-04 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4f9e871a-caaf-3e10-bc2f-a01052498dde | -14.57274 | -52.88076 | 2026-10-04 04:59:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15d4666a-d3cf-361d-96cd-ed78934e936c | -9.9076 | -65.0154 | 2026-10-04 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3db7201-fe1d-37f1-aff0-58f0f6a75509 | -12.19261 | -57.10549 | 2026-10-04 04:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c8c0a569-9b30-32ba-877c-7abefacdef52 | -9.92609 | -65.0329 | 2026-10-04 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3fc1c0e1-f0f9-35c7-9c72-87b58a94509f | -9.92296 | -65.04498 | 2026-10-04 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a082efe0-35d3-37b7-85a1-0a48a0569117 | -12.19787 | -57.12241 | 2026-10-04 04:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e08c5317-b1f9-3afd-a24e-8f2946c7092f | -9.91063 | -65.03569 | 2026-10-04 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 002cae97-5fe3-330c-b1ac-ae7af2a70165 | -9.91119 | -65.03627 | 2026-10-04 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fdadf88c-f885-38d2-8b72-f150d5cc22f2 | -11.74248 | -58.56607 | 2026-10-04 04:59:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 752e1c4b-58b5-3529-aff9-59f9ee933938 | -10.95707 | -60.91293 | 2026-10-04 04:59:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e100c47-9f91-3d91-a1fe-83a30b5223f5 | -12.19909 | -57.12412 | 2026-10-04 04:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69fd9941-d8d9-344d-8fc5-033e35406dee | -12.8172 | -60.49642 | 2026-10-04 04:59:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e8ca0e5d-af3b-3221-9752-525fea41085d | -15.91332 | -56.34553 | 2026-10-04 04:59:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b44a66ff-fd91-3fba-9da6-b889f342c54d | -12.19089 | -57.10139 | 2026-10-04 04:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c489f06e-9963-3ebc-bc34-58ac9e3212cc | -9.91801 | -65.03767 | 2026-10-04 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8e5e6d3-04e8-3f21-b00e-9b65fb0ed0b9 | -12.20272 | -57.11802 | 2026-10-04 04:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5aafa28c-1269-38dc-aba3-aca66223b29c | -15.91693 | -56.3462 | 2026-10-04 04:59:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eb5d35bc-2d3e-3553-8050-b9ee187aeab1 | -13.50689 | -61.13449 | 2026-10-04 04:59:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a13ddfb2-c138-35ad-8480-696abbbd140b | -9.9193 | -65.0314 | 2026-10-04 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 12256c14-b9f5-3ff9-84d6-9279a247682c | -12.17981 | -57.10852 | 2026-10-04 04:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99c1a3c1-a63b-3b43-b1f3-f6fa6bb7b724 | -12.77361 | -62.04148 | 2026-10-04 04:59:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90333bd2-1994-38bf-978c-2ad1cf157bdd | -12.19605 | -57.11825 | 2026-10-04 04:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f0f2c14-18a6-3f84-8e5e-9754dce85e7b | -12.19964 | -57.11214 | 2026-10-04 04:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce80922e-b713-30bf-aacf-46195cdee937 | -12.19789 | -57.10799 | 2026-10-04 04:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f38a9bfa-3294-3a19-a7f4-637d7f2f920d | -12.15818 | -60.74535 | 2026-10-04 04:59:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e7e5139-ab1e-3014-8186-91348c57381e | -9.91744 | -65.03712 | 2026-10-04 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c4eed04c-d779-3c8d-b7bb-2f7cd8cd7162 | -9.894 | -65.01256 | 2026-10-04 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4fca903a-e458-3f87-82c5-d651fe05d177 | -12.76889 | -62.03681 | 2026-10-04 04:59:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README49.md)
