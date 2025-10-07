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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e72d715-48fb-3003-803c-92aa1d879465 | -11.02538 | -51.15548 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d9884284-695d-3752-8c2a-6e51d110eae4 | -14.92042 | -46.80938 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87b3df2d-1213-3166-8c27-eee920e7bac2 | -10.41612 | -50.31158 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6428eba5-f5a2-3637-a1f7-2f430c61110f | -6.74436 | -63.06029 | 2025-10-07 04:57:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 314e8233-ff40-3c14-aac7-525204da4c88 | -10.74561 | -49.71018 | 2025-10-07 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b99f7135-fe46-3ca0-8884-40d4b7231f29 | -13.22569 | -48.46701 | 2025-10-07 04:57:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 17414b83-a1c8-30b4-a029-efc759625719 | -8.15289 | -49.49442 | 2025-10-07 04:57:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd115466-c5f3-3ec6-a4d3-302b1a556181 | -13.24658 | -51.68504 | 2025-10-07 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 314039b8-cb98-3e19-abbc-103442f6aebd | -10.23237 | -52.70092 | 2025-10-07 04:57:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30f9023d-8f85-38cf-b50f-3ec9b6682417 | -9.98006 | -48.0159 | 2025-10-07 04:57:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b16dd949-2eef-39d5-b5cb-e94a008f52c2 | -11.68125 | -46.34604 | 2025-10-07 04:57:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b28c6c79-8bed-3e6f-945b-e184fcb51c77 | -9.03309 | -50.59137 | 2025-10-07 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4df8121c-625b-32b0-b8ee-22fe50a33bdf | -13.07151 | -47.82938 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| dd87eaf9-b78b-34ca-8f8f-c7bdb76b1c93 | -10.4129 | -50.30595 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| cc4c5e21-e4f9-328b-870d-bec8cd4510ed | -15.88759 | -46.25375 | 2025-10-07 04:57:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74d8dec2-94ad-37e8-a312-d171d1bf0b40 | -10.35399 | -56.33656 | 2025-10-07 04:57:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bcf7b45a-719b-36b3-a24a-a976620ef142 | -15.51284 | -46.84073 | 2025-10-07 04:57:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4496a920-fc89-3e8f-9bcc-fb451c85ff5f | -12.23522 | -47.85584 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7b73f7eb-2392-3bc5-b125-1d503c3ae07e | -8.62315 | -54.96979 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72b4326b-6a98-367c-8c85-aae3d96b05cb | -13.26521 | -48.06151 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d1b56e43-627c-32cb-8126-813f170a25bc | -9.51643 | -54.73462 | 2025-10-07 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca520178-854e-36ec-bc7a-100288275f6a | -10.18789 | -45.53491 | 2025-10-07 04:57:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 08b2ca3f-6ed0-3957-aa79-ff507ec61a76 | -10.59737 | -54.35906 | 2025-10-07 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82b795a5-3a23-35a0-98bf-ad27bf5ab910 | -11.80616 | -45.12821 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf55ffe9-01eb-3c58-9248-91b0dbeb6a29 | -11.02545 | -50.91362 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a8b648f-18b6-3c66-a0b9-455d956361c4 | -13.70613 | -48.07995 | 2025-10-07 04:57:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f3744816-8bc8-3fa6-ab71-f06cfb57342e | -8.49919 | -49.13132 | 2025-10-07 04:57:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| f7dd0737-e9b1-3b62-8f4f-d5c153be1634 | -11.6755 | -46.34404 | 2025-10-07 04:57:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a63b0ebc-cd9d-3547-8c36-feeebe6c59b0 | -14.36543 | -47.72903 | 2025-10-07 04:57:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 816c6580-ee0d-3f5d-873b-c94dacc02f1b | -15.37679 | -47.3121 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c1466d7-6291-3ebc-bbab-2f4779f40b32 | -13.22498 | -48.46434 | 2025-10-07 04:57:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ea78575-1ed1-32b9-a292-dfd2930f78a6 | -11.50984 | -51.4838 | 2025-10-07 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d16abbe-4504-365a-9cd7-45abef0f55a9 | -12.40213 | -51.13963 | 2025-10-07 04:57:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a675f30-c7d5-3fb9-af90-26228736040b | -8.1862 | -50.30743 | 2025-10-07 04:57:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dc9b871b-95d6-3820-ad86-98d036f0331b | -14.91908 | -51.44573 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 9e1750af-661a-3d2a-bfcb-503c158db9b9 | -10.58112 | -51.47461 | 2025-10-07 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b1be3801-a604-3b90-bdd3-2833cd004aea | -10.74697 | -50.48857 | 2025-10-07 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b81874b8-7bd0-3c3f-92db-b2d6807decfa | -13.33075 | -47.55904 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b9d8320d-507d-3932-91e5-b82546b28395 | -12.89568 | -54.7488 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 38.0 |
| cb02fa91-4dba-3417-8206-212badecf7f8 | -12.92673 | -54.72449 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 05a8283d-a2e2-3a65-9c7e-96965cb11d05 | -14.90755 | -46.82706 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a9a85cc-8c48-3e8a-b2be-8fce1fede12e | -9.17085 | -50.83705 | 2025-10-07 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 452f404e-b78f-3e8c-9bcf-63a7104de49e | -10.32937 | -51.23433 | 2025-10-07 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 653404a2-ad2c-33d5-8701-00f9de6f1de9 | -11.77973 | -45.1334 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e513cd81-3de0-3c4d-b425-dbc0181ef905 | -10.88041 | -56.06923 | 2025-10-07 04:57:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 601557cd-2d63-33da-8e14-f1705c2daa93 | -8.61819 | -54.95827 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e9ba2e8-d3bf-316f-a72c-629d262f8d33 | -8.53215 | -54.85879 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d932e1db-d5d9-39f6-9408-afbda432e6d3 | -13.37121 | -48.03635 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5743353-0d5b-3e4e-944b-b3829dcd722a | -14.62295 | -52.4948 | 2025-10-07 04:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b96e3f75-3763-3c09-b281-7c057c752b85 | -7.47893 | -63.5675 | 2025-10-07 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc993bbb-17bb-326c-95ac-d197d27e888e | -13.22096 | -48.45897 | 2025-10-07 04:57:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f42f1e90-e880-330c-9715-1cfd200aa323 | -10.38932 | -50.3025 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e9daa2b5-7f15-3883-aaad-000897debf97 | -13.09212 | -47.85889 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| eafb149c-b9b4-387c-98fc-4bd72dd05c97 | -9.33008 | -54.51601 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d74d2535-b1ff-30c7-865a-cac79361c285 | -9.95739 | -64.21741 | 2025-10-07 04:57:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 58682ba5-60fd-32fc-8aaf-df0c9a20a99b | -8.85219 | -62.36663 | 2025-10-07 04:57:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f5f8f93c-5637-37b3-9dfe-262254f17c04 | -11.65079 | -46.87722 | 2025-10-07 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39fc6021-1c36-398d-8259-3b65de074ce6 | -10.49975 | -51.49551 | 2025-10-07 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3d05a9b5-cf4c-3792-8065-b5b8e8c712e5 | -15.59505 | -47.27113 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77da27b4-22af-3a98-8291-42c6bcadef2a | -12.94426 | -46.78907 | 2025-10-07 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 443f464e-54f9-397d-a279-985662bb9f09 | -13.33221 | -47.5607 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c8b09ae-fe95-39a4-924f-0fb018a16386 | -8.15827 | -62.8313 | 2025-10-07 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92acfcb5-594a-3c78-a849-be6716c6da97 | -12.90454 | -54.73558 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| accea770-7725-3b75-b580-59eca8317361 | -10.37429 | -50.29842 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 215b9ecb-11e8-3b85-8287-d4f5c72d1791 | -13.35617 | -47.56947 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f02a430b-aa79-3140-acf7-8599c870c015 | -13.24313 | -47.24929 | 2025-10-07 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bcbce920-7921-3889-b9c5-a760905d09c2 | -14.90635 | -46.83696 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39e6624d-3e54-33d9-b8d4-e48ca6c55c2f | -15.76333 | -47.77224 | 2025-10-07 04:57:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 252dc7db-a998-3612-a419-d0f43cdffbcc | -10.74593 | -50.46804 | 2025-10-07 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| af515bb3-3455-3df5-aa83-844051d8dd81 | -10.9342 | -51.1439 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66e7b34f-909a-34df-8849-28fcd3e0481c | -13.58858 | -48.686 | 2025-10-07 04:57:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| eb5e6237-030a-314d-845e-78c562b1ae0a | -14.70908 | -48.38631 | 2025-10-07 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9f657594-1e88-3dc3-982b-1d2d6a349847 | -14.93132 | -46.7989 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 05cbaaf6-683d-3c31-a377-dc38b907b9a3 | -12.90399 | -54.73916 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9d7a3840-6ba2-3e2c-bbfd-45e7de517345 | -13.86109 | -44.41872 | 2025-10-07 04:57:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b7ab6ec4-0278-3bc8-9a2b-f2611e2f27b4 | -9.62239 | -54.31898 | 2025-10-07 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02d81362-b6f2-30cd-bf6e-d513f6c98fbd | -9.14572 | -61.2318 | 2025-10-07 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85e82047-c5df-3ea4-a56c-6325c3679c86 | -11.94834 | -51.47151 | 2025-10-07 04:57:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ce716b5-d536-30d2-8cc1-f62f7cd49e7f | -13.58097 | -51.80314 | 2025-10-07 04:57:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8098ae07-b7ac-3d16-85e4-f11c10f62635 | -11.6515 | -46.40599 | 2025-10-07 04:57:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b88d944f-9211-3326-8341-c4df1ed44ccd | -12.17723 | -47.77607 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2575ea2b-00a8-381b-bbb3-b6cf7135cf2f | -15.60308 | -47.29168 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| fd4e1e10-6c23-38c5-9707-c76666db4021 | -10.87739 | -51.02907 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 732205cb-91f7-3bb3-a415-e2714d6665e3 | -13.33019 | -47.24572 | 2025-10-07 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45d9325e-b764-372d-b1f5-c5fac309f6d6 | -14.9059 | -46.83345 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca50fdc9-84b7-39d3-9ac0-716450ec9753 | -8.41013 | -50.70169 | 2025-10-07 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a3832fbe-a347-3580-bdde-aa0982edec65 | -11.84173 | -44.91442 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d7e0c97-50c1-3b81-bf15-7e0e19f2ffbb | -13.24563 | -48.06329 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 912c5fc6-0fe8-338e-89c4-d2e0eedde6b0 | -14.72387 | -46.01425 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd948ba0-55d1-375d-b92e-cbcfb7bac8e9 | -13.25679 | -48.05597 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2dd312e3-1c28-3471-9042-1442675115f4 | -10.3384 | -54.19122 | 2025-10-07 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05008755-7702-34df-8c42-8dd62bda23f2 | -13.26151 | -48.05698 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fdd434e4-8c1a-31d6-a7d7-2f75911aa781 | -11.21233 | -54.98571 | 2025-10-07 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1dbdc1de-7901-352d-a2b3-37e8098e9c6b | -9.69879 | -45.93343 | 2025-10-07 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fffe9bc3-25cb-3777-8167-ac77d97f8a67 | -10.08645 | -57.80529 | 2025-10-07 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03c0e008-1fb9-3507-ba00-1b9bcb9766fe | -12.44707 | -54.40266 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3dbf351-40ff-3772-ac0d-536338f180fe | -11.94323 | -51.48028 | 2025-10-07 04:57:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b71c1b6-4037-359c-a48c-a97519d48d37 | -14.90894 | -46.85396 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 161f6423-8304-3651-a19c-4c159525e0eb | -10.15555 | -61.95056 | 2025-10-07 04:57:00 | NOAA-20 | VALE DO PARAÍSO | RONDÔNIA | Brasil | 1101807 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 34b1359f-8e97-3b49-a3a4-653dac93b241 | -14.93104 | -51.41661 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README88.md)
