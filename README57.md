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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2f01f0b-11b9-3e8e-9758-999ecfebb604 | -6.32977 | -60.00281 | 2026-09-16 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| decf4199-f1c5-3ab3-8301-6921b986c471 | -9.35879 | -56.93666 | 2026-09-16 05:36:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57d9318c-aee6-3eeb-a145-3e1414a01937 | -10.87093 | -50.82038 | 2026-09-16 05:36:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fd3807ee-c2ca-3bb3-a10b-1f40b7dd9293 | -6.34206 | -62.68378 | 2026-09-16 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a515b9e8-7ebe-3d50-a206-0a1ee0666814 | -6.75433 | -58.8112 | 2026-09-16 05:36:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c9001d4-f840-3ced-a9fa-82e81289d33b | -9.10225 | -65.92818 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32f47288-6563-34ed-b8ae-fbf8991a2ca0 | -10.66212 | -58.76432 | 2026-09-16 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ba565b72-2b88-3a69-882c-88a103722005 | -8.83428 | -62.4788 | 2026-09-16 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 710c3960-955c-3e01-974b-cd1d3ad774a3 | -6.75492 | -58.80748 | 2026-09-16 05:36:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a3a776ce-957d-33f3-b70f-1b6cf468c474 | -6.93061 | -63.13074 | 2026-09-16 05:36:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 501da4c7-edea-3db9-8cf1-6da57aca0e5e | -6.32753 | -59.9953 | 2026-09-16 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5de6f686-1435-3e92-b6d7-cec50e3eec2e | -11.81369 | -60.46575 | 2026-09-16 05:36:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 38b762d2-1fe3-32d3-915b-3f56fb2f865b | -7.65341 | -67.16451 | 2026-09-16 05:36:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a8c7d7ff-71e9-3b2a-9b15-08f6e23cb179 | -10.47648 | -50.95924 | 2026-09-16 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2b773d3-04dd-37b8-b285-61956641a67c | -9.25751 | -60.28187 | 2026-09-16 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b93452d2-f876-3528-9a24-2f9267f9221f | -6.79221 | -58.78991 | 2026-09-16 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d880b1f-f5e8-33e8-b0ba-db8fc28a2d28 | -9.38568 | -60.30922 | 2026-09-16 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1ad3b75d-9850-3916-881a-4026e0a1d82d | -12.75176 | -52.8394 | 2026-09-16 05:36:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c403d773-b267-3145-b4e3-b8221c1cbe9a | -6.72005 | -58.80585 | 2026-09-16 05:36:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1535aefc-02b0-3e73-a587-e70344ccd370 | -9.024 | -61.01703 | 2026-09-16 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2324f51-6660-313d-b4a6-08439adb03c0 | -6.24324 | -57.81282 | 2026-09-16 05:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 638ca2aa-e0f2-3fb0-8cee-e1ff2585ebf9 | -6.32866 | -60.00979 | 2026-09-16 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 41b93e37-eab3-3b8c-91c0-47869fb0d347 | -6.71319 | -58.80479 | 2026-09-16 05:36:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95d8b21d-4b5c-3eaf-98f3-636def45763a | -8.71238 | -62.8421 | 2026-09-16 05:36:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6bc0f81-68fc-3a1c-b496-c76689fa8c05 | -12.61805 | -50.7671 | 2026-09-16 05:36:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 56e57dab-20c5-33ad-8709-f602f549fdd9 | -8.71179 | -62.8458 | 2026-09-16 05:36:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f65ff13-efe4-3bbe-a685-8770aa9bacb7 | -9.09275 | -61.0137 | 2026-09-16 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 234ed7db-6573-3b13-8e85-374a4417a364 | -9.10538 | -65.55743 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37207c9a-5965-3fd4-84a6-9cc78389dd8c | -9.02733 | -61.01756 | 2026-09-16 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b6416fdb-e082-3d0c-bb43-34a4065907ba | -11.8103 | -60.46521 | 2026-09-16 05:36:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cf369810-331c-3ba3-b46b-eaa4bb59a73c | -6.47854 | -62.86973 | 2026-09-16 05:36:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf223167-44a9-3186-9a38-700d956c9ec3 | -10.9491 | -57.18797 | 2026-09-16 05:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3508b558-5951-3398-9861-674e3220f927 | -10.8692 | -50.81292 | 2026-09-16 05:36:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 164b5409-6324-3269-a1a5-9c6c6261d9aa | -6.35184 | -62.68928 | 2026-09-16 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa9cf613-2325-364b-9141-0b00ed3b95ec | -6.76076 | -58.81162 | 2026-09-16 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3672254d-4c70-37dd-bd05-1dd04f1eb0ae | -11.1958 | -54.12819 | 2026-09-16 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ff9bb252-97d9-3200-84a8-9c77357524af | -7.61517 | -67.25545 | 2026-09-16 05:36:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c05dd97-1243-34af-8670-039c633075c2 | -12.1188 | -57.19649 | 2026-09-16 05:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2a1c52ea-a30f-31ec-ab2a-9f6744aca479 | -11.19492 | -54.12907 | 2026-09-16 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5d7a646-5838-308b-baf3-d898b8dba969 | -9.38959 | -60.30619 | 2026-09-16 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1f0c1e4a-5630-3c3e-98a4-f17c4aeafabf | -9.04395 | -65.92142 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98055ebf-5964-37fe-b67c-c1dda497d44e | -7.50959 | -50.15458 | 2026-09-16 05:36:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8cb361c1-3647-3b8b-92cc-6d1f3ea5fc74 | -9.37967 | -58.00163 | 2026-09-16 05:36:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93ff5d2d-a8a4-3871-a7ec-460b920b8647 | -8.36929 | -54.73051 | 2026-09-16 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05dffb3d-8c6d-3143-9341-32a465830693 | -9.25806 | -60.27832 | 2026-09-16 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6dbf5c10-8d60-3b72-9a9f-0b1b2da9c8ca | -6.12779 | -59.88902 | 2026-09-16 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20fa4fb6-33e5-385e-883e-956b65382ee2 | -9.09331 | -61.03172 | 2026-09-16 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23540128-606c-38ba-aeec-1a003c235853 | -6.2913 | -59.92156 | 2026-09-16 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d493aa72-fba1-345d-83b1-9dfd96bb1c12 | -8.70831 | -62.54354 | 2026-09-16 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e84b420-fe14-3ea8-b159-24eed0b960a4 | -9.10533 | -65.934 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ecb9fa3-7deb-3357-aba3-50046e3698b0 | -10.25842 | -57.7014 | 2026-09-16 05:36:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23e53c3e-d8a3-3963-a336-1cc8d62b0d6f | -10.69976 | -54.16851 | 2026-09-16 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6aad0cc1-e17d-3c36-9675-625c9ed968cb | -9.08665 | -61.00914 | 2026-09-16 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a653516f-b1be-3ec9-af48-21349893af8e | -10.13842 | -61.18096 | 2026-09-16 05:36:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d185ea2-9bde-3327-a4b4-2018207484dd | -9.08887 | -61.01666 | 2026-09-16 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 882f007a-acc9-37f0-94e4-ff058143bb73 | -10.70382 | -54.17416 | 2026-09-16 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11c83779-803c-3a0d-91da-ececa39f89c2 | -6.70741 | -56.88078 | 2026-09-16 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 06e0594b-8712-3af3-90c5-46886c95620b | -7.64756 | -67.17227 | 2026-09-16 05:36:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9916eee1-4f08-3981-928f-eb22a0628d45 | -6.32922 | -60.0063 | 2026-09-16 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c51c3cd1-b9ef-3d99-a79d-c3de0ff072b2 | -6.35001 | -62.70067 | 2026-09-16 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bae12f82-8be0-3ead-85b5-22484bf77d16 | -6.34491 | -62.68814 | 2026-09-16 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 96a7e574-e168-33d1-b9c1-df7ef7b7d1a9 | -6.82848 | -58.64598 | 2026-09-16 05:36:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 766a99ae-8445-3835-8cb1-1639782c7194 | -6.28408 | -59.92401 | 2026-09-16 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98df61d2-de49-3c68-bee7-e98823d03646 | -6.12556 | -59.88149 | 2026-09-16 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd6d221f-3ada-3592-81b5-cb9ea3902a83 | -9.22307 | -60.29507 | 2026-09-16 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb30b66f-08f4-36a6-b931-fbc46da66ab3 | -6.35123 | -62.69308 | 2026-09-16 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c7ecf9e6-b224-38bb-abe8-3d92764ed726 | -9.01846 | -61.03049 | 2026-09-16 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd4a1b78-3b05-35d8-bc93-9a3588c19c8f | -10.41966 | -48.65541 | 2026-09-16 05:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8b2f5343-f849-3354-b850-a83f6da3636c | -6.43315 | -55.60362 | 2026-09-16 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c4d9c14-eb74-381d-b326-b40e37844e67 | -6.33798 | -62.68702 | 2026-09-16 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7145f029-9e45-3057-b440-2af73122c138 | -8.64531 | -66.59148 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2be9749-3f58-31e5-9ff8-ffdf15d7a38b | -6.13556 | -57.69429 | 2026-09-16 05:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c21104b-ba75-387b-9454-2eb715d03250 | -7.6578 | -67.16528 | 2026-09-16 05:36:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 421a1c5d-88a0-3d67-8957-0579b00666e5 | -6.32698 | -59.99879 | 2026-09-16 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd795f29-1d93-35c7-8a62-e3342ef67927 | -8.71207 | -62.8422 | 2026-09-16 05:36:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d274380-eb24-35a6-bd5f-aae1e01fa9f1 | -11.98434 | -52.46888 | 2026-09-16 05:36:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ff330e4-b6e0-3cd4-aa48-ff5ba5a506fb | -6.79907 | -58.79098 | 2026-09-16 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9217d6d-e724-3111-880b-342ac08d7a70 | -6.44665 | -60.01462 | 2026-09-16 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e09be0a4-52fc-3d5b-aea0-b9598020105b | -8.66113 | -66.50112 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48a6f6d6-3641-39d4-8ffa-c2ac5b1f7507 | -6.33574 | -62.67886 | 2026-09-16 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a451b403-eef8-339e-bdb6-bb05cdb0c135 | -9.06174 | -65.92648 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff85cf05-37d7-3bdf-a614-9ac96905e8e6 | -6.12501 | -59.88499 | 2026-09-16 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7ded816-87d8-3f6e-9647-902671dd09e8 | -6.28797 | -59.92104 | 2026-09-16 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b050cc21-6aa8-347d-aa7f-8803a133df65 | -9.59036 | -60.5157 | 2026-09-16 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d4f4da3-cd69-3b51-8420-4264db1fa7c5 | -9.03091 | -60.36972 | 2026-09-16 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3a36f39-9195-3110-b5eb-1c118c240b83 | -9.11919 | -59.50835 | 2026-09-16 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ff13dc6-10c2-361f-ab2e-77af91b8de0b | -10.40682 | -48.64799 | 2026-09-16 05:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9e529325-5e38-3c0e-a3ac-e297f13da144 | -8.48958 | -64.03262 | 2026-09-16 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba3eae99-fde3-3e19-8aa9-ec64a6804659 | -10.60302 | -57.31879 | 2026-09-16 05:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c60bc424-29cb-36cb-860d-b0dfbe135323 | -6.80695 | -59.16764 | 2026-09-16 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3fb0f377-89fb-3436-8b6d-c8f03cf025c8 | -9.49425 | -56.74785 | 2026-09-16 05:36:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3959cbd-0e61-368c-bdb0-8b397a600cb7 | -8.83148 | -62.47463 | 2026-09-16 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 328bac83-007d-328d-aa38-564bdfbada26 | -10.90106 | -54.00817 | 2026-09-16 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5b2eb5a-6dca-3219-b93e-2c7d2b1795c8 | -6.34022 | -62.69518 | 2026-09-16 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b11d299d-5710-3c05-849c-17547e90df8b | -6.36458 | -58.28595 | 2026-09-16 05:36:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc856522-9b3f-3d81-8a45-0f9bc4ccb598 | -6.28463 | -59.92051 | 2026-09-16 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b1b1d23-8001-3f56-8d77-c1dbc0c27e25 | -8.83486 | -62.47518 | 2026-09-16 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 271cf1f3-d0bd-39ba-8b0a-2d009e2f2012 | -6.12167 | -59.88447 | 2026-09-16 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3c40889-fb1e-37a6-8ad3-8f144a1b9520 | -11.19195 | -55.02745 | 2026-09-16 05:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 425eb546-191b-3fd2-b2de-9073459bb939 | -7.65579 | -67.17171 | 2026-09-16 05:36:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README58.md)
