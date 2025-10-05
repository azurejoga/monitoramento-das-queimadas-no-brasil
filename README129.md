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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f40bd07-ee86-3c42-a649-49a8d8bdf771 | -14.75084 | -54.65897 | 2025-10-05 05:16:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cc273fd8-1c98-3f5b-96e7-3414dfd49a1a | -13.30774 | -48.11552 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0742c056-73f0-3f0e-be2f-876a6422c00c | -16.08351 | -50.91422 | 2025-10-05 05:16:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6c7a8d9f-5686-328e-93c2-9af1cc2fbed9 | -18.2469 | -53.33702 | 2025-10-05 05:16:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6121d803-3fdc-3643-a3a0-cbbb498aca03 | -14.5677 | -52.47345 | 2025-10-05 05:16:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 862e8fbd-8553-301e-ab15-5534795a8556 | -16.35435 | -51.47909 | 2025-10-05 05:16:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f16a2ca9-1609-3c74-937d-5d2ef4d728b0 | -15.98907 | -50.91879 | 2025-10-05 05:16:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9e2f596f-6dfa-31f0-bb8e-505a945877a8 | -13.07717 | -47.91458 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c85510ab-b6c5-33fd-a1de-a5eb3fc0037e | -15.21789 | -56.80527 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 72b178ab-d015-3f30-9f49-b9ccef235ca7 | -12.77237 | -48.82158 | 2025-10-05 05:16:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7d80c27f-fbb5-3a32-949e-8cdf87b909ac | -11.84435 | -63.7222 | 2025-10-05 05:16:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f613e7c-6f60-3738-b006-e3d53e35bde8 | -13.08417 | -47.90662 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64fca1fb-0219-3b7e-a154-8607b892dad2 | -15.7657 | -46.26939 | 2025-10-05 05:16:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e11e4df3-c8e6-3656-b8b2-ae2d29d0c3f6 | -15.30182 | -46.31752 | 2025-10-05 05:16:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5681c0d-e645-36b5-a9c4-644d6c328397 | -12.81268 | -50.53139 | 2025-10-05 05:16:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9473a9aa-6c91-3190-a076-1e74c1cc505a | -10.04752 | -62.45647 | 2025-10-05 05:16:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b64bc62b-a6b4-3644-af64-53d1b94e4852 | -11.91209 | -55.91141 | 2025-10-05 05:16:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3d768c4-45b6-3844-950c-6eefa7e0cb8a | -15.39505 | -47.94957 | 2025-10-05 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d1353f76-e756-3cc3-8e3d-fe8eb281cf26 | -14.6951 | -48.34716 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef422788-6f5c-33a6-ba38-e47e7af21da6 | -13.1559 | -47.97132 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5a92e5b6-2003-3da3-b929-9db6f71f03e4 | -12.30538 | -55.12722 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a8bfc17-bf59-3f29-980b-0b0181fa426a | -15.25244 | -56.76354 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80cb6cce-fe67-3835-b039-936fab277977 | -17.95876 | -57.5773 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 1f955ab9-355d-3b77-af7d-a824bc5658d2 | -14.69643 | -48.35469 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a3f51c94-4486-3d73-b881-47bbd26cc1f3 | -14.40982 | -56.23557 | 2025-10-05 05:16:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6ac0c541-f7c2-38c9-af87-03f3aa667b47 | -16.29101 | -45.24242 | 2025-10-05 05:16:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 688d36ec-5e1a-3f1f-bbe8-308d36ba45e3 | -15.98335 | -50.86068 | 2025-10-05 05:16:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 465ca144-0f6a-3113-a314-932c0bbbbc74 | -15.50974 | -46.85049 | 2025-10-05 05:16:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 93cfcd29-2596-3933-9209-68e881e20aa1 | -12.39099 | -51.09356 | 2025-10-05 05:16:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4a26add-687b-352e-9eb0-e86626f8608c | -13.29838 | -48.0919 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d0b62bac-40b5-3506-a5f9-dd381a8432be | -17.93652 | -57.60686 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 70f79280-ca5a-333f-b239-a2e029a1a549 | -12.88793 | -47.29634 | 2025-10-05 05:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3bd856e-3b4e-35f2-ba09-e63d61943eb5 | -15.75879 | -46.26913 | 2025-10-05 05:16:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7bca5c80-a947-3aa9-b4cf-f01ffde3a54d | -12.91122 | -47.31366 | 2025-10-05 05:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f40a910a-1e8e-35cc-b234-a51954e0f7b8 | -10.83551 | -57.18718 | 2025-10-05 05:16:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2ccdff5-855a-36e8-a31b-88b5c80171a9 | -15.90613 | -48.83122 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8155b4d3-348e-3265-b6a5-6d9c3b24aa9b | -14.33995 | -47.6917 | 2025-10-05 05:16:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b136b5ba-25fe-3074-9f2f-4d19148c0421 | -15.77361 | -46.25974 | 2025-10-05 05:16:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c976fbbd-be58-3022-94b0-5ca1f903673d | -13.20615 | -48.53192 | 2025-10-05 05:16:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a00c701-b610-3687-995a-2ee50a41735b | -11.51048 | -54.47847 | 2025-10-05 05:16:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a13bb011-c4c0-39a0-a29c-189044f1814b | -15.76569 | -46.26901 | 2025-10-05 05:16:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 21dd6120-accb-3097-8544-e72e8855d504 | -12.3115 | -55.13733 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c155ce6-2e35-3522-8713-303fc7b7c72b | -15.97748 | -50.90966 | 2025-10-05 05:16:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 172bffe8-c934-3bfe-938f-0cbbb95f8858 | -12.59495 | -48.14522 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4a06d5dc-06ab-39e1-8b33-3a99d8af690a | -13.26712 | -47.82811 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 648f7e14-de7e-36e6-9ec7-15797ca93214 | -13.267 | -47.61133 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5f7bd6fd-9a7d-3a0c-8a24-aba63be5e2fe | -18.2635 | -53.36648 | 2025-10-05 05:16:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1be9c22d-43a5-370a-bfd5-22d440cef67f | -14.93317 | -46.84379 | 2025-10-05 05:16:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f86e36ce-a925-386f-9e8d-95be7d3af424 | -13.09776 | -47.84082 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 47523d7e-dd2d-3df9-bc89-64275d06d47f | -16.01264 | -50.84938 | 2025-10-05 05:16:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aaa6896f-7d62-366e-a272-c05172c71f42 | -14.67714 | -48.36554 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| aa5060e4-d087-357c-801f-887d11df0b2d | -15.2325 | -49.29922 | 2025-10-05 05:16:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6f49aae-ef59-35bb-a3a2-5734a18d08d7 | -15.54919 | -46.96084 | 2025-10-05 05:16:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ef2aead-8c88-37f2-a3c8-33791c972bf9 | -14.69684 | -48.35084 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7b3acc89-e3d4-339f-a9ce-db927d929c55 | -13.18022 | -50.87311 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 97e40801-3462-37b6-a0f5-26cffa77044e | -15.97675 | -50.91578 | 2025-10-05 05:16:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0a1187a5-2a33-3098-87d6-659b1a8566e2 | -13.2891 | -47.62762 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4fa36cea-b033-3fd1-a92c-f5fd61c86540 | -16.16753 | -57.57802 | 2025-10-05 05:16:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 75c4f5b5-5e10-379b-88ab-0fc20998b66a | -13.45883 | -47.29537 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9eff17ea-6db9-3139-9e48-fda25f019194 | -13.0987 | -47.83259 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 83af1826-3d38-364f-8311-5115385fddba | -12.46083 | -45.50359 | 2025-10-05 05:16:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7bf4f6dc-47f3-3a45-a27c-027ea3f6f6d9 | -14.68696 | -48.36554 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| d5d273a6-5eda-3ffc-9d59-0346e568cac9 | -12.24053 | -47.85013 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0850801f-a1c9-3e48-aed1-45d3f7d701ad | -13.13877 | -47.9839 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7924642e-d248-37b6-aff2-07db6a8231dd | -15.57737 | -52.45675 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d1190ca1-3004-3388-a78f-f19484727d2b | -18.24301 | -53.33145 | 2025-10-05 05:16:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 76e67ff7-24ec-3fbe-9bbc-badeefb6ebdf | -14.68087 | -48.36598 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 5134a037-64ce-3b6a-83c0-cda062cd26d7 | -13.12924 | -50.87782 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| dbbad9c3-93a3-37ec-bbe9-64e0582fe7e8 | -12.77848 | -48.81844 | 2025-10-05 05:16:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6125a9a7-b2dc-39df-acbd-18987b039e08 | -13.30349 | -47.61915 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9d1a2368-b50d-344b-8281-ebe65ab73f35 | -14.56829 | -52.46885 | 2025-10-05 05:16:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f4eff804-cd09-3caf-8408-b4e027403c48 | -14.01121 | -48.21084 | 2025-10-05 05:16:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5dd56dcf-5a1f-3f39-ac3b-3881c5677105 | -14.68854 | -48.29833 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea1b1e2c-5fe0-3fb2-9ad1-aa67fd4761d4 | -14.69137 | -48.34548 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba96e53d-8192-3f11-a8ac-957157100c8f | -18.25957 | -53.36112 | 2025-10-05 05:16:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 8.9 |
| fc3d3467-42d7-391c-b39e-bf137d5fa07c | -10.66122 | -58.77092 | 2025-10-05 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9ac5165-58a8-376d-83b2-49db9d0bfbbc | -12.45879 | -45.52302 | 2025-10-05 05:16:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 362ba766-5251-384f-bd44-c2578cf351c8 | -13.35063 | -47.57925 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3748973a-9edc-3c93-9b9b-24bb282b085b | -11.92397 | -55.90483 | 2025-10-05 05:16:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e59bfb9-d836-320c-933a-912cc4a68fbe | -16.38584 | -52.16429 | 2025-10-05 05:16:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d3ccf0f9-3e16-3e85-abd8-f31ddc231e14 | -15.2389 | -56.857 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4ecde1df-a58b-34be-8c81-8e50bc154878 | -13.25897 | -47.20253 | 2025-10-05 05:16:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19ad54ee-ddf5-3d60-aef8-d046d4d046eb | -13.31723 | -48.0859 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ea5519d-06e3-3b6f-a735-c2882313b7bd | -12.31652 | -55.12893 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5e1b585-6093-37be-a328-1a36c3993ebe | -17.1186 | -48.92909 | 2025-10-05 05:16:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee0fb262-ffd6-32f1-ab1c-f57a255c01d5 | -13.13862 | -47.96301 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 669e618e-af46-37ca-b5ad-d6a794e78200 | -15.54696 | -46.85241 | 2025-10-05 05:16:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9ad0e0a-bb41-37a6-a24b-cbdf9779924d | -13.08821 | -47.92475 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 23cd9586-cb41-34ba-8c7b-d920d389e847 | -11.87207 | -56.88483 | 2025-10-05 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7823a313-a95c-3f16-ae44-e433d2932b9a | -16.15258 | -57.58332 | 2025-10-05 05:16:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d79c258d-5044-35fd-a3cb-a6281b110fd5 | -17.91251 | -57.62415 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| bf2eedb6-0151-3f69-bbe3-faf8a2dce043 | -12.59443 | -54.76936 | 2025-10-05 05:16:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5d32f30-8d43-3517-8632-f5863fd8ad76 | -14.69727 | -48.34686 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 053af9ce-327c-3c1a-bc38-3ec5ae60a3b6 | -15.97822 | -50.85981 | 2025-10-05 05:16:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9dd3c1a-0055-352a-8f13-c0f8319f5c96 | -14.68281 | -48.34881 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 29755233-3023-3ce8-a83d-2bd27d14ffe6 | -15.54844 | -46.83784 | 2025-10-05 05:16:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 96543a4f-9e3a-3b09-a148-bbe12b18985d | -12.23925 | -60.33624 | 2025-10-05 05:16:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62db0744-d055-3a01-8393-16230da83e0c | -15.87168 | -46.25681 | 2025-10-05 05:16:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45a6b4ae-26a0-37c9-a7de-6deea4618742 | -11.4017 | -55.1781 | 2025-10-05 05:16:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a6378819-1f85-3641-99d6-5ea820447887 | -17.86524 | -57.60135 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |


[Clique aqui para ver as próximas entradas](README130.md)
