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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 004c7273-8ab6-3b4b-aa2e-9a9466cf772c | -13.4872 | -46.95717 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b431ffa-fe3f-3058-89a6-b6001cb5f95d | -11.34739 | -43.52222 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a662c15d-f4b6-31e3-9870-6db1e25c0095 | -11.81218 | -46.43184 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 45466c84-0e51-355d-b06e-84448fc6aa97 | -11.80939 | -46.4498 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| e710c802-baad-3723-8982-663d08530b1b | -12.84816 | -48.08215 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 340d860e-bd72-3a5e-a5f9-19da0188453c | -11.01915 | -46.87347 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d2937ad6-8d29-38c7-be47-ea46fa6fcf3e | -12.45232 | -44.04944 | 2025-08-31 04:29:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18d8ada0-b72e-30f4-9105-2765bb9b8c3b | -11.36532 | -43.60838 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 068016b1-000d-3859-a9ab-0d23e5338b1f | -11.08493 | -52.03645 | 2025-08-31 04:29:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d89d3033-d5d8-3e9d-81b9-10146c95187e | -11.31444 | -43.6962 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a3070787-59ed-36fe-8555-794b58717d44 | -11.36226 | -43.60329 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 86f00bb4-7e47-3fac-9f2f-42a52d339613 | -11.90488 | -46.69867 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0adf8c6b-267c-3cda-a364-74d5453b1ac7 | -11.90906 | -46.39537 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 91c93d36-9e2e-3761-add9-db91977d5c9b | -11.88207 | -46.71335 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| feb9f6b3-7e8f-3713-b9ee-5d9aa233dfd2 | -13.48167 | -46.97081 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74c60c3a-6d3e-3491-8b0c-758ab7e13151 | -11.29516 | -43.59302 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e59b091f-9910-344a-9fee-a24f9d6f9c68 | -13.35708 | -46.95494 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e2e3642-0d49-3d58-af5d-5ce7e66cf1ac | -14.98901 | -46.70647 | 2025-08-31 04:29:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6a05c67f-249c-3b55-b474-22e2b7972b97 | -11.35258 | -43.64315 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| d34ab19c-413c-363f-83f3-15bbe98e7190 | -11.35085 | -43.62902 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cc40efac-576c-3029-8af3-ebd21a311092 | -13.35234 | -51.76206 | 2025-08-31 04:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5950c98a-555a-3f77-97a3-da8e7f5baea5 | -11.34886 | -43.64257 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| a3789631-d45a-3e5b-9e20-d58719f59bca | -13.01564 | -56.88294 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 838675be-11e4-3e09-93b8-58b2d79cb7b0 | -11.86215 | -46.45417 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08546aae-295d-3d9a-a6d7-be984d8a3564 | -11.07293 | -44.62859 | 2025-08-31 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 4f74d5bf-dd15-3fa1-aa0e-490111660e45 | -11.81857 | -46.86741 | 2025-08-31 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 004d2e12-1373-31a2-a754-41b77772d1c0 | -12.80594 | -48.0897 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81481238-c5f4-372c-a0b4-a891263c21d9 | -8.95545 | -50.01117 | 2025-08-31 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e77c1303-9398-32ed-a470-2f8fad6db5c6 | -11.87932 | -46.73111 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ae1f737-7ad2-3c5d-9bb3-8135e2996853 | -10.48185 | -51.62539 | 2025-08-31 04:29:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 536c5c8e-d5d5-39c1-9122-f959d6f69b57 | -13.98695 | -44.53332 | 2025-08-31 04:29:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8199025f-e2d7-3d5a-9fe8-2bd68e996def | -12.63849 | -48.1829 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6e1970c9-527e-3594-abac-008fe7de6c83 | -11.24545 | -44.67691 | 2025-08-31 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3eafcec4-79f2-31ef-b2c6-7481d20bbc11 | -13.38828 | -47.0073 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70bc2d30-63ff-386a-89f0-6a847dea80e1 | -11.82597 | -46.53289 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91ac9484-34aa-310e-bb90-c1ee8fbc2220 | -9.68546 | -47.05244 | 2025-08-31 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3e086f6-47ec-3277-9a1f-9b704cf4333e | -10.24328 | -54.9747 | 2025-08-31 04:29:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6edd9e7a-64a5-3fb2-82d3-bf16ca51101b | -10.01039 | -42.54018 | 2025-08-31 04:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bf3fa9a0-32c3-3e65-832f-1eaec9b07176 | -13.40038 | -46.83963 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9afee4b6-0485-340d-bb77-4ce5c48d46b1 | -13.17449 | -47.18975 | 2025-08-31 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49e5affe-fc25-3f00-885b-85398159bfa3 | -12.63104 | -57.00122 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04a790b4-e357-3f7e-bbd9-19f909cd0d7d | -11.81273 | -46.42826 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2510bf6a-06d6-3783-a80f-5f457691413c | -10.42269 | -50.86063 | 2025-08-31 04:29:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8bc33ff1-a285-3e61-8866-b6d3923b51c0 | -14.81643 | -46.74452 | 2025-08-31 04:29:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8079de5-6c55-3a4b-aaff-afba9c03f8d8 | -13.51404 | -46.98333 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56346ba8-e472-366e-8b0e-ff4872afd610 | -12.91444 | -56.97951 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5706a06b-e26c-39f7-862b-04d7eca1caf6 | -14.03799 | -44.56561 | 2025-08-31 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| db0dd967-8ac4-3e06-81b5-243a6d032f2b | -12.31851 | -45.72524 | 2025-08-31 04:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c78032a-cab4-318a-8d9b-fc79159d19dd | -13.50272 | -46.83369 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e9390e9-26c3-3548-9262-087f79467711 | -12.81707 | -48.08423 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 143aa03d-867a-3784-81b9-65a128d9e969 | -11.88545 | -46.73572 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fae6cf96-6466-3385-8286-bbc245b2a613 | -12.62839 | -48.20317 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a23b8425-f2c5-33dd-afe2-41bfa28b6724 | -11.81498 | -46.43594 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| fece5066-22cf-3274-9bcb-1417b009ceec | -9.67783 | -47.90807 | 2025-08-31 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f932491-bb23-35ee-9173-73fb197b9b6d | -11.07033 | -44.7421 | 2025-08-31 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8b9f6e7-66d0-373c-89d6-6f94974ce9fb | -11.08141 | -52.05692 | 2025-08-31 04:29:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b33b64d-466f-3ab8-bd6a-87886f0b8f5d | -14.98844 | -46.71022 | 2025-08-31 04:29:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0a2d050e-e74d-35fb-a633-6d12d525f393 | -11.81854 | -46.44728 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9825a607-e5d5-3372-8d4b-f9494fbbcac5 | -11.56123 | -47.61815 | 2025-08-31 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ab75842-3f3f-3f67-9ee6-959a99c4f62b | -13.40048 | -46.95049 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69cde5c7-c9ca-3e4e-9261-dc5b8c13d1c6 | -13.68628 | -46.87838 | 2025-08-31 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d485dcb1-0dbb-3e8c-a08a-90dac67d95f9 | -11.81275 | -46.45031 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 8b8cb208-d3a5-3ab2-9bff-0b358af98bfc | -11.21203 | -45.04581 | 2025-08-31 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc3e0e98-b4c5-3a6a-88e1-f9b4fde4e2df | -11.88596 | -46.71029 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f85d282c-2d54-373e-a9dd-6907bd6acdb8 | -13.01966 | -56.89045 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1013dd94-0ebe-3218-98a6-228457142339 | -10.9447 | -50.84098 | 2025-08-31 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1cf40552-771b-3756-99ee-dbf6b4b88116 | -14.80857 | -46.7276 | 2025-08-31 04:29:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f88e1e64-285d-31a8-8ad9-84e47590a53f | -13.37539 | -46.95749 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bec8c404-6005-3d7d-95b6-a3574a016d37 | -8.96333 | -50.00637 | 2025-08-31 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec7ee006-17b4-3807-8efc-2bb585f44b52 | -13.67574 | -46.9244 | 2025-08-31 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44938db9-eadd-3da1-b952-21570a9a1588 | -11.02358 | -46.86696 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 74b8371e-2e45-3e81-b929-95e1d0a6e8d8 | -10.60044 | -44.32341 | 2025-08-31 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d041aac1-4f8c-3e84-83ac-65e57cd85eda | -11.8241 | -46.43347 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3037c2d4-67d3-37f1-8e81-398ad042a3d5 | -13.3543 | -46.95076 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 0a1c0e05-b197-3c7d-8e32-637d5232fd6a | -13.98604 | -46.31205 | 2025-08-31 04:29:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 210d83b6-0119-3a56-8d4b-210494986737 | -10.96764 | -50.8633 | 2025-08-31 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| da7550e0-280a-37f7-9ba0-a661a61bcf64 | -12.64449 | -48.20953 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c06403a0-ce61-3ba5-81f5-70b7d480e222 | -14.27935 | -51.88544 | 2025-08-31 04:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 12622861-bbee-3e06-aa59-0257d8951049 | -13.33078 | -46.85876 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1fe0d022-40b3-3636-828b-299795ac3e4f | -14.15809 | -52.69673 | 2025-08-31 04:29:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8f8a096-65fc-3913-8123-b3c5ea3a64eb | -13.36535 | -46.95591 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6f513e3f-8f26-3a4c-851c-b677133423fa | -13.30517 | -46.89126 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b630cea9-58be-3e80-970f-328627a0fcc7 | -13.02364 | -56.89822 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2565e61c-6587-3d04-aad0-834ffef11d27 | -11.83446 | -51.49947 | 2025-08-31 04:29:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 75029bdc-2f39-3c47-b656-60b4ed512824 | -14.99015 | -46.699 | 2025-08-31 04:29:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 384df952-ec51-3295-a23c-4ebdbaf090fa | -14.35312 | -51.9058 | 2025-08-31 04:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f41b0dbd-10c0-396b-9e0e-09ee80109d20 | -11.8956 | -46.37112 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cb42eadc-4ecc-3c26-af37-626fa8da4460 | -10.94395 | -50.84542 | 2025-08-31 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f31d89f7-5682-3d0c-8411-ee2d22c9fab0 | -14.04471 | -44.54437 | 2025-08-31 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed27bfd1-7ee0-30f7-ac54-d87e5a8b24f7 | -14.9963 | -46.70419 | 2025-08-31 04:29:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4ca32fd3-cade-33e7-afc0-b908fd6c69f5 | -14.03982 | -44.55254 | 2025-08-31 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1d3490e-37aa-301a-81d0-64fcf3869ba7 | -13.35598 | -46.93998 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2361674-3ebf-3e1f-ac49-65ab8a517383 | -8.96405 | -50.00217 | 2025-08-31 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd6d657b-ae99-3b17-831c-0ef160ec3b75 | -11.83245 | -46.42389 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16fa256a-eb44-3391-a5ec-d9944792a752 | -10.03394 | -46.02214 | 2025-08-31 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 54a951be-f14a-3b83-8746-4b0fa0ac5915 | -12.92905 | -56.98932 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fa66f8ac-a670-377d-a832-546477ce8487 | -14.49638 | -52.99184 | 2025-08-31 04:29:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d43b650-fd61-3732-87c1-ef25e2051954 | -13.02688 | -56.90289 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c4c765c-efcd-3552-a0ec-ca8ebbde8b93 | -12.65335 | -48.21832 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa015c12-51c6-3d56-a66c-d81ebd4ac24d | -13.97811 | -46.31836 | 2025-08-31 04:29:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README41.md)
