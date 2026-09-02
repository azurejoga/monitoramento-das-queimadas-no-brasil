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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 059bcb45-9f7a-3b57-991b-31acd543141e | -14.32555 | -47.22687 | 2026-09-02 04:57:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 537b157e-6b8e-3725-a57c-d844a12e5326 | -8.21463 | -61.47741 | 2026-09-02 04:57:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5051948b-eaa2-3822-92d0-29ca74a963d9 | -8.26517 | -54.96067 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7abf87d4-bacd-364b-b9b9-d38bacbddd59 | -8.12324 | -54.96011 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 54122f4f-f2e2-3810-9c2d-5f8e94dc89d2 | -6.17964 | -57.73169 | 2026-09-02 04:57:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41aee125-6c88-3119-a81e-5fd3d1cd8e9a | -8.4554 | -54.71435 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b280cb06-65c0-36ca-9ed9-9f7cdc566b7e | -6.14544 | -57.70959 | 2026-09-02 04:57:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e96deb8-f2e8-312e-ab0f-0bfeb1e5e367 | -12.14773 | -47.13473 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4265f008-8ec5-342b-9fa5-1a4698954069 | -7.29199 | -49.81179 | 2026-09-02 04:57:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c07462d5-ff9c-34e0-b109-d2751cc9d51e | -8.45479 | -54.7401 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c5070c73-4680-3de7-8532-fc47e40d1e7b | -12.34947 | -45.66177 | 2026-09-02 04:57:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b134a81-b436-30c5-98ab-44ab78cafadc | -7.60698 | -47.28928 | 2026-09-02 04:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb2f83c5-cf95-303e-88f4-0a13a27576d2 | -11.33975 | -50.58598 | 2026-09-02 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e338bc3e-0dfe-3049-a901-ef60ee707e04 | -6.94327 | -56.46338 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e23ef15b-7be9-3965-8db5-40e6f123c64d | -7.33941 | -60.57737 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 499b83e8-267f-3fb2-ab5e-4dc11d2d1158 | -6.93996 | -59.64515 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4dd2dff7-7d5c-3af5-88f3-838cc73e64f9 | -8.28888 | -54.92702 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eede4266-6474-3585-bbbf-d24890f638c8 | -10.4942 | -59.60889 | 2026-09-02 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f2cf7823-f74a-30f5-b138-31f8e4403106 | -6.94428 | -56.45182 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79f1b3a2-e850-3b77-9a2f-dca93af592c1 | -8.2803 | -54.91446 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 900121af-1b8b-3577-b548-e6cf64da0960 | -10.77287 | -44.74491 | 2026-09-02 04:57:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 65ee0afd-e641-3130-8d8b-fa301cd40567 | -7.35546 | -60.58048 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1a07f90-7d8b-3fe8-a194-f4004266f1b3 | -6.91858 | -59.6478 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 62ba2729-d961-382c-8577-108a9acb4f07 | -12.35153 | -45.68093 | 2026-09-02 04:57:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b67246a3-88ab-35fe-8ee2-7114745e2a30 | -10.46347 | -50.46369 | 2026-09-02 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4ba3e80-7641-3cf2-b3b2-3d0a67e71996 | -6.38736 | -55.21926 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2222f171-a426-3d9b-965f-bf518b92faab | -10.31267 | -50.0363 | 2026-09-02 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 405aa535-fc7f-3c71-a220-6988d2165549 | -11.34723 | -45.40975 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d2f3e9de-8d78-3673-b563-e4d1465f4601 | -9.45831 | -56.74068 | 2026-09-02 04:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b24b3d3e-6c23-3103-b1dd-aa0b5e93e712 | -10.91004 | -45.34058 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 659b08e2-bd7a-32ba-9f8d-fdab9fd3feee | -11.29797 | -45.18603 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9ea9f19-a718-3a40-8a97-8855bbaa5f0d | -6.94047 | -59.64223 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bac8eb3a-2831-3f3c-9771-e6f36d5e71de | -10.34779 | -49.96808 | 2026-09-02 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cef40c42-16ca-3bf5-bd73-e9c7443f3202 | -11.67615 | -58.61776 | 2026-09-02 04:57:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b64a4be6-8635-325d-9959-245cd28c3e47 | -8.45319 | -54.70541 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14b1c82e-cf6d-34e0-b681-90f716a1dfd4 | -7.20318 | -60.67283 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7045d59-2ab7-3f13-8b99-fb2b22e0f03d | -8.47557 | -54.70478 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f0b6bc48-896f-38f5-a1d5-eacb83810aef | -9.00355 | -65.41912 | 2026-09-02 04:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6717f344-d875-35b6-b91e-67989c08c2e6 | -6.69013 | -58.75802 | 2026-09-02 04:57:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0bd266c7-2a79-3e9c-a0e1-4c9d0072a106 | -9.02101 | -65.45882 | 2026-09-02 04:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4ae39d7d-6efd-391d-b984-a697dd0662eb | -12.14877 | -47.12734 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8de7eac2-2fc4-38aa-be7d-17089c4a04dd | -10.4401 | -46.73931 | 2026-09-02 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5aac30f2-c293-3930-bda7-6046cdeb3655 | -6.08035 | -53.66707 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01a43a81-5807-3ee7-9f06-5a3175a7f597 | -11.5359 | -50.94206 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 297dc29a-e151-3910-8b2e-2fd9595af726 | -8.43086 | -54.70325 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 662e1ab8-05f1-3751-9425-7f8eefcae415 | -11.53315 | -45.48491 | 2026-09-02 04:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78679ced-f77c-30c5-a006-8d0371209bbb | -8.4555 | -54.7359 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55d76573-7bdc-3cbc-bb1c-e3de59c9ee43 | -9.94049 | -53.99261 | 2026-09-02 04:57:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 262837a3-6924-39ef-9732-35180d4b8407 | -8.45469 | -54.71856 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 61de1b79-5022-3328-8080-b4220883c2d0 | -9.39347 | -51.68611 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aff8791e-e389-32dd-84a0-a9d2c259ee7c | -8.42655 | -54.70686 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2f147590-6754-3fad-af2d-bddbd59717c3 | -8.75396 | -62.5692 | 2026-09-02 04:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 35c1e18d-26a0-3f7a-8732-dcecb8ef3b7b | -8.76342 | -62.58408 | 2026-09-02 04:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 83ccc53c-8e0b-3802-b29b-609492611e57 | -11.30262 | -45.18651 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c932c5eb-63e6-3d36-a22d-25a138d30fc3 | -11.1528 | -51.57081 | 2026-09-02 04:57:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c5bf7c5f-1c33-34c1-b243-76a771354f8f | -9.4034 | -51.60177 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f3b0163-0bad-377d-844a-4f6378a90f65 | -8.11219 | -54.95844 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b1e51307-4de2-39ba-9f9b-aad96ea02906 | -8.43172 | -54.72073 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 21c73e3d-2ea3-3696-83e4-e8b425b62c8a | -6.76536 | -59.44063 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 68e3f1bf-2b38-3d8a-b39e-6129d7254401 | -7.3501 | -60.57949 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 202dc28f-8fdc-3a10-8aa5-ca38e9d3b1bd | -7.64725 | -45.87803 | 2026-09-02 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f719fe88-d0c4-3b5e-8a07-847cc87536aa | -8.44306 | -54.69934 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2116613d-cd7a-3eb4-8e48-ab9be47bd1d7 | -8.46262 | -54.71559 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| e6c1faa0-012a-345c-9a0a-73d041ec5dd9 | -12.13233 | -47.09476 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18483536-c68b-31f2-8103-b6bc59dc0145 | -12.3744 | -48.14698 | 2026-09-02 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e910c29a-246c-3f7e-8bd4-b8d8ea8f8574 | -12.12461 | -47.08988 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d2539ed-352e-3bee-9fab-5dd006c16fd6 | -5.33875 | -60.15136 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f865f1de-f515-3791-80c8-ba273b51740e | -9.72166 | -48.13909 | 2026-09-02 04:57:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b450b9b-d664-3291-9331-9147db5c1aee | -6.1118 | -53.4509 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52ff0534-ea37-3cf4-b885-e87cfa9e0d28 | -7.52745 | -47.33192 | 2026-09-02 04:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9a580666-2882-39bf-b5e7-e62db33a2b5d | -6.9471 | -56.45984 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 364e1751-4c62-32a1-8397-d31f58d65d82 | -6.05112 | -57.73744 | 2026-09-02 04:57:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0280484f-2a82-337a-8162-31a7253d18be | -6.43192 | -53.56845 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b660b0c5-3828-30a5-a09a-ebc359db0c5e | -11.29533 | -45.17032 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6a9198d0-2396-3566-910b-bec88cae1c52 | -12.12151 | -47.05126 | 2026-09-02 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eac88f9e-ecac-3f89-9b3a-2c7367f78c32 | -8.15559 | -54.94719 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf7bf6d4-cfd5-399d-b31a-a078061b9c5c | -7.28711 | -52.35825 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b26705f1-f88c-3f18-a496-7001da73122c | -12.14722 | -47.13842 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b0140ba-7452-3272-9382-2272b819dc79 | -10.84565 | -54.0409 | 2026-09-02 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 948add38-b3af-3084-a029-90b5ac2288dc | -10.48718 | -64.32429 | 2026-09-02 04:57:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6ab4de8e-b5f0-3638-a01a-ec077e4975e5 | -8.4324 | -54.71653 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d3139f64-cb4a-3874-b5d6-269560dc1782 | -6.11834 | -53.54391 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba97267d-ef39-38e8-ab6d-fdcd11b4ab2a | -9.7115 | -54.33511 | 2026-09-02 04:57:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e18ba1b-5162-3990-a6a9-ec9b4587ac7c | -8.2754 | -54.94428 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67bc1418-7d7b-334e-b37b-df68183994af | -13.41424 | -43.87279 | 2026-09-02 04:57:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33e644fa-9adf-3186-b21d-bc6f9f0ffc88 | -6.9433 | -59.64174 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6714bf28-273c-3be0-b994-7db0a1867e40 | -7.757 | -61.20093 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6e1ccd1-219d-32b6-8d12-f447aad18439 | -9.9474 | -53.99375 | 2026-09-02 04:57:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94cfa2ca-aa2a-3406-9ac9-509b06d7a8d6 | -12.08163 | -47.10993 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e80fa2ba-2108-382d-b101-d6f184cf4d07 | -10.90549 | -45.30618 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5a4a2ae-c3db-3eeb-83c6-164fdb78c1cc | -5.5803 | -60.19833 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58796413-5966-3085-ad0e-d770737ce50c | -7.1893 | -60.68764 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0abb882-25a2-3935-88eb-51de1328f17d | -10.78898 | -44.76794 | 2026-09-02 04:57:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d2d996bb-814e-37c5-af21-1fac7c2c8592 | -11.26969 | -45.12517 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3c3d0d1d-6050-35c3-a5f2-a06d8969e945 | -8.26225 | -54.95551 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 000848b2-cc77-34b3-b885-5aad4f478cee | -7.3495 | -60.58278 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f4c854c-3147-33b1-82ce-3cd1bda8cadf | -11.63471 | -54.56149 | 2026-09-02 04:57:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b4942da6-8680-3f66-ade6-140753cff845 | -8.11816 | -51.66387 | 2026-09-02 04:57:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 354e195d-ca5d-361b-929a-a7b7e1606447 | -6.9275 | -59.6423 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b97384ee-124f-3b59-9911-5d45f29eb479 | -6.1153 | -53.45146 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README39.md)
