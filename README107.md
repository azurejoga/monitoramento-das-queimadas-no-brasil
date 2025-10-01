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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec7ac728-4d1a-3bff-bb1c-0d1f0cf36e79 | -12.82677 | -47.01988 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9c72e9d3-042c-39c9-acb7-1865ec5852a1 | -10.35255 | -43.73708 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8440b3d-ec96-364b-b93c-536ccacfe6d4 | -13.76918 | -47.97496 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 16d0438e-3bb9-3cfe-ba18-eb4f26ea3935 | -9.95143 | -43.58288 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3929c4be-e63b-31fb-b84c-ef6d26bb79b5 | -11.68565 | -44.29472 | 2025-10-01 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 387631fe-fcf3-397e-a795-4d1937753c64 | -13.88921 | -51.84625 | 2025-10-01 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a668793-6030-3410-a105-dbd6ab49c2da | -10.21102 | -48.19822 | 2025-10-01 04:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9ffbe467-e921-3cae-8e24-43dc4c998551 | -11.60674 | -45.04577 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bef79e94-9f57-387b-8633-60c3777bef5c | -12.70688 | -46.89504 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c68a48d9-be92-338c-aaa3-a78957c2c8ba | -10.4862 | -49.36993 | 2025-10-01 04:51:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a09a77e-46ba-31f7-b875-2256f3cdd4b8 | -13.27874 | -47.22327 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a46f9210-1b02-3541-971c-6863d51bbb97 | -11.4529 | -44.97105 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28a76af8-b904-3483-ac4e-6a92cd24ab46 | -10.06247 | -48.18839 | 2025-10-01 04:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7301c70d-6472-3f3f-aeb9-0aa0e3ac7438 | -13.29551 | -46.389 | 2025-10-01 04:51:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6513d421-8775-3ac3-aa61-7b380ec81b1b | -13.31042 | -47.22322 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 206a5117-8d1d-3c36-9a35-c9ba92e25bc2 | -16.37313 | -47.06196 | 2025-10-01 04:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 453e9e93-7b3e-3270-8c1f-844bd27b0b74 | -10.6223 | -54.94872 | 2025-10-01 04:51:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 09061394-ad36-38ed-8c47-42795db468d1 | -11.83591 | -44.96498 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3f8c1ee4-05b9-311b-9768-fcdeb1240f9c | -14.3529 | -45.92886 | 2025-10-01 04:51:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| a4746ee6-3c81-314d-81fd-08fcc54bc303 | -14.75927 | -45.75414 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 646ba98d-00a6-394d-8cf5-620a43d88779 | -10.57144 | -57.81232 | 2025-10-01 04:51:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83f0d0ab-25fa-3e53-bb9c-080d94c983ce | -12.78136 | -46.88218 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 140b2347-d90c-3497-8bde-90afd926477d | -15.31761 | -46.40635 | 2025-10-01 04:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8a4b76f0-1c90-3143-8922-0d40a334f780 | -12.8847 | -46.9085 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 821a2cb0-c003-3617-8eb7-54320834c264 | -13.29525 | -47.58025 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| acc15d48-7000-3b86-9007-b0faa8334514 | -13.17056 | -47.79127 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24d557c5-b034-3bf6-bee7-244646499073 | -10.28399 | -50.4665 | 2025-10-01 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c44513f8-0ad2-3a5b-ab48-cfb950c36cb8 | -9.42059 | -47.33245 | 2025-10-01 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 625c37a1-9756-3367-b313-3e9af8f33c5f | -16.08477 | -51.04472 | 2025-10-01 04:51:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32a903a0-90d2-3d69-8772-61889bb083a0 | -12.42219 | -44.09433 | 2025-10-01 04:51:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24d4c1c4-4b9b-3f6f-8854-106016f198a3 | -10.62174 | -51.59758 | 2025-10-01 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 573664dc-196a-3d98-8e60-97284c2042fc | -11.63671 | -47.49562 | 2025-10-01 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 51ad0b91-b802-38ed-8c2e-2f187d8435a0 | -16.37104 | -47.04354 | 2025-10-01 04:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ed96932-8ffc-3dbf-91b9-97b024e0a5ba | -9.93999 | -43.59841 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2a83de6b-0565-30ce-b2a9-ff4ff5a5658e | -14.43181 | -46.35773 | 2025-10-01 04:51:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01f6fb1c-30b3-332c-9898-4ad612654124 | -14.92138 | -47.82092 | 2025-10-01 04:51:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0b77c81f-9bec-391c-9771-fc4cba1cd857 | -9.80176 | -45.9377 | 2025-10-01 04:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee04a451-37a8-379f-8077-cf4bc0851c8a | -12.85024 | -47.03451 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 438123e3-510b-3ee9-95f1-e006b6261cfb | -14.40962 | -47.14243 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20d0a029-ef10-3fca-9fa9-8a27af942a02 | -15.20991 | -48.00785 | 2025-10-01 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c074bcd7-dab9-3eee-915c-71c68290ec66 | -15.26268 | -49.2734 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 71f8b489-1536-3ec3-a3be-27defaf0c4c5 | -13.21628 | -47.34118 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2aba357-fd8b-3976-b18b-0f848331029c | -12.80085 | -46.89568 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38e7057b-d70e-351c-a9f1-56948d6ed2b6 | -9.79748 | -45.93705 | 2025-10-01 04:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bbd74aab-7180-3b98-ac6b-097070ec8d73 | -11.46102 | -45.0187 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39e93a94-e19e-37f8-b8e2-2b2b40472cac | -10.98403 | -46.53341 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f58d87b-ca73-3e8b-9e0d-e7b067625862 | -11.13844 | -43.37535 | 2025-10-01 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a7bc7695-9143-357e-8f3e-f316dda4a6f0 | -15.25796 | -47.89341 | 2025-10-01 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a8a49a94-e08a-3e0f-b59a-9eba049da8dd | -11.04786 | -47.82563 | 2025-10-01 04:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6cf2211c-4cf2-3345-8e3b-37885dcc1874 | -12.45808 | -50.23314 | 2025-10-01 04:51:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0757d477-4d61-3e1e-88a2-3c650fc8d62c | -12.24233 | -47.82072 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2682a9e8-02f6-3d6f-a66a-4cc9f56a1bc6 | -14.98325 | -50.76468 | 2025-10-01 04:51:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82f6c969-3294-3261-8d90-a732f62b3364 | -9.92688 | -43.69218 | 2025-10-01 04:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 77c1a48a-aea5-3d0d-a70b-5a3fcaed81e6 | -15.25959 | -49.26829 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da4c98c0-956d-3bd7-bf77-09da240a1535 | -10.21843 | -43.04295 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 977ef4ad-c407-30f6-901e-b7c44ef2d0ab | -12.87265 | -46.77706 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f286db5-2f6a-3e9f-9daf-eabeb23edfde | -13.76941 | -48.40804 | 2025-10-01 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30fa8c79-f3c6-3367-ad83-6ed545bc076d | -11.04678 | -47.82358 | 2025-10-01 04:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3e82532f-bae0-396b-8c5a-1eb5dfa0b1ab | -11.80438 | -46.61998 | 2025-10-01 04:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 8a55b845-003e-3311-8acf-98eff52ec3b2 | -15.61327 | -46.53109 | 2025-10-01 04:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94730faa-c371-344f-b05d-7fab8c46264c | -15.01392 | -56.04403 | 2025-10-01 04:51:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4019ba9c-2ba3-3156-9372-337acaa0acbc | -11.46187 | -51.50627 | 2025-10-01 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c2f9176-7de4-376b-8185-5adeae958917 | -10.90329 | -46.5583 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 12b4e5a2-65c5-3586-8b65-696369d45c93 | -14.69038 | -45.28833 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05007a84-9347-3ccc-9991-176112fc7cf5 | -15.48488 | -48.5474 | 2025-10-01 04:51:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4cbb42a8-f61f-3111-b580-aea4ed46f673 | -11.84606 | -44.99686 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c01fee21-a53b-35e0-9449-f25734505994 | -13.76748 | -47.95791 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c039401b-5593-36be-9cb9-ba8ee68b41a1 | -14.89009 | -48.12014 | 2025-10-01 04:51:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| df1f7aff-e2f6-3d9e-8182-013c9e02559b | -13.33352 | -47.84327 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e14b2642-fce4-350a-89f5-e359e3ba0a56 | -11.83866 | -44.98045 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ddbfed4e-99c5-33fb-a8ad-c2e97ca668b9 | -13.29895 | -50.6694 | 2025-10-01 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a63fd817-4c4d-3d8a-80c3-bb8a8dfd7f1c | -11.0979 | -47.72292 | 2025-10-01 04:51:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ad268415-0dca-3dde-b153-3d8e3ba164ee | -12.86842 | -46.77644 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad2c8679-ca73-32c1-bac0-5bea4347275f | -14.89339 | -48.12587 | 2025-10-01 04:51:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b2660618-dda8-3acd-a82c-5220bcd50134 | -13.69894 | -48.64705 | 2025-10-01 04:51:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 11cf4ca8-071c-323b-90c5-8081c500fc92 | -14.51767 | -48.37816 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 653d4a48-7c8f-3f9c-a92f-cd9cc6d088ab | -10.38881 | -48.14113 | 2025-10-01 04:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c2e2fffa-ad45-3cd1-9208-6dc3c445e776 | -14.7147 | -48.15973 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 91251dda-46f8-3c0f-a838-228768ce8404 | -16.24395 | -44.05609 | 2025-10-01 04:51:00 | NPP-375D | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0aca23c4-bf0a-3423-87de-a3a3cac60543 | -10.4476 | -48.08101 | 2025-10-01 04:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de31545c-d978-3385-910f-3289c70c203a | -14.68144 | -45.28172 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e8ebc77e-ea74-348f-89bd-c7339cea0d63 | -13.33763 | -47.8132 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e453e401-0c32-3b06-be4e-6ab7a7e229a2 | -11.63428 | -47.4965 | 2025-10-01 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 853ea2da-9466-3c35-884a-c3a59d5d79e5 | -11.3669 | -45.06369 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8b0c9591-5e66-33c5-a771-327563d5ea3d | -12.7685 | -50.55864 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f648735e-7221-356b-a9da-d9343c933b92 | -15.36694 | -44.15514 | 2025-10-01 04:51:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75e13bbc-ec09-334d-b6b9-0392478418f7 | -14.34831 | -45.92833 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| adddfcf4-98d5-3411-9adf-9eed6b6d2311 | -12.41716 | -44.09355 | 2025-10-01 04:51:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9beb976e-d8d3-323d-b95f-b0f50c152c39 | -9.94225 | -43.65284 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 45ff7d39-4e21-3909-8985-06f6aeb40359 | -11.4324 | -55.05464 | 2025-10-01 04:51:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57042079-24ef-3389-95cc-7d940f95c2c8 | -12.95683 | -48.43492 | 2025-10-01 04:51:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a07be9b6-8d67-3dff-bfb7-4bdf030d4217 | -13.15271 | -47.4103 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a5688af-6782-39f9-a437-0a5cc479d7fb | -13.13068 | -47.42685 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a80dabb-e92b-3d1d-9845-fa6fb51f955a | -14.68293 | -48.24459 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b430e1f-75fc-30a1-8c8c-b1e393d0d486 | -14.01578 | -44.98031 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd5a240b-3555-34a0-a7a5-ad9837d83f68 | -11.12459 | -49.78831 | 2025-10-01 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ff8cec4a-f22a-3fb1-ba8f-56d0fce5e27e | -10.24159 | -52.69539 | 2025-10-01 04:51:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1719f908-7fbb-30f2-9fe0-93e5a551634d | -13.23117 | -48.44335 | 2025-10-01 04:51:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bd298c66-0140-3987-a5de-a34844d57db0 | -11.20376 | -47.76038 | 2025-10-01 04:51:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6ec2d2d5-dba7-33e3-a33d-695f20ad1c1e | -14.68315 | -48.12306 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |


[Clique aqui para ver as próximas entradas](README108.md)
