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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efac6a20-54a0-3f90-b0e3-5df97272fb24 | -13.58337 | -45.47566 | 2026-09-19 04:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 49729712-076c-32ce-8a43-f0243994c070 | -11.41237 | -47.27962 | 2026-09-19 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4164faa8-d54d-3dce-91cc-d00a60c55aa8 | -11.97794 | -44.93002 | 2026-09-19 04:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8df2fee2-57d4-3d71-b934-d7de478a1bbf | -11.11792 | -45.28794 | 2026-09-19 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85004ef7-bd7e-3d75-857a-faac5271119a | -10.52194 | -44.84843 | 2026-09-19 04:40:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a41fd8ee-af0a-3039-a9b3-9b747aa1ad7f | -10.48811 | -46.29852 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de3c711b-2a5d-3821-99a0-f16dab08b772 | -7.56465 | -57.67397 | 2026-09-19 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0da0fb2a-c18b-385f-b95c-e92e2e25b4f4 | -10.09079 | -45.64856 | 2026-09-19 04:40:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c73cba5f-e99f-3725-bb61-fc44fe0c15a1 | -9.24067 | -46.2039 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59c9cd64-1b49-30be-bce9-cc6b1594f8b2 | -9.95179 | -46.54399 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cb8e9f54-cb00-39f0-a5d6-961929242299 | -11.37639 | -47.03157 | 2026-09-19 04:40:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad111a39-70cb-313b-988c-5f6974a3b2d3 | -10.36063 | -48.89192 | 2026-09-19 04:40:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b69a8a89-7a71-38dc-8392-c1e470eb75a3 | -9.78064 | -45.05772 | 2026-09-19 04:40:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf47204f-ec51-352e-93af-2c00e16510d3 | -13.38564 | -48.03316 | 2026-09-19 04:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 014be62e-20b8-3775-af17-1af3e2178209 | -11.32523 | -47.35575 | 2026-09-19 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5227c0de-6ce6-3d31-ae5f-5b63c42ece69 | -10.91685 | -48.42061 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23b2b66d-d47f-3640-b596-6e9c27119fb5 | -7.56412 | -57.67149 | 2026-09-19 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1dafc8c-b85b-3d0a-942f-5f0aed206ee4 | -14.92299 | -49.92074 | 2026-09-19 04:40:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ed3ee318-b7bd-38a5-b218-fc5455005096 | -11.00434 | -48.32798 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2c9c100b-8822-313b-8ff3-62f418f49311 | -12.99613 | -46.98112 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c11ffa88-e8f2-32a2-851c-07108ddfe097 | -12.86042 | -46.34219 | 2026-09-19 04:40:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 070f536d-6509-33de-bd60-fe9515423269 | -9.92796 | -46.58699 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 87890094-347d-316a-9b6c-70f58f76e7bd | -11.12483 | -45.28905 | 2026-09-19 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 570422f5-f7eb-3137-8373-401db59968e7 | -9.70842 | -54.82068 | 2026-09-19 04:40:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 35c7c695-66b2-3a1b-9030-c888c8ae083a | -16.04818 | -49.98588 | 2026-09-19 04:40:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9c65a841-ba62-3cfd-831a-d063c629d342 | -9.59692 | -45.36646 | 2026-09-19 04:40:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6d02cfe-eade-3165-8ab5-0fd49c2218d5 | -11.3281 | -47.68135 | 2026-09-19 04:40:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0ab45dfb-df07-3f00-a583-156aaf84a55c | -11.22592 | -42.83084 | 2026-09-19 04:40:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 8c8dd5c5-39a2-3e49-845e-7adae2ddd2fc | -11.11153 | -49.44424 | 2026-09-19 04:40:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a7e7b1a-30d9-3688-a357-716b98607e8e | -12.43573 | -49.57651 | 2026-09-19 04:40:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0abdb74-d568-3fcf-a5dc-0a3cd38800de | -11.30382 | -46.75901 | 2026-09-19 04:40:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 583e4e7c-ba67-35da-9a69-f9c31bbda919 | -11.47426 | -47.6512 | 2026-09-19 04:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1c6d7ac-7adf-3c6f-9851-25586a24fb03 | -9.25124 | -46.20197 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 40d52e8e-268b-3b52-b3e1-a41bfca167dc | -7.57017 | -57.67262 | 2026-09-19 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52b70430-efb8-338c-a4f6-a80f3182d6c3 | -13.65095 | -46.94075 | 2026-09-19 04:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a636223c-80eb-327c-9966-90a0c9886cac | -10.85697 | -56.20045 | 2026-09-19 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b023315-f967-3c62-bfe6-d8061e377eeb | -11.086 | -48.27864 | 2026-09-19 04:40:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ff3707b-f9e7-330a-9f29-7d1a31e7e71a | -12.15199 | -46.99989 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 785ea267-2504-3a61-9bc1-c72e50071e4e | -9.7924 | -46.09045 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c34337c9-d959-3709-b658-f335d591aab3 | -14.68976 | -46.66684 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 3b8593a5-47de-3a9c-9b15-1c1283acde1d | -12.57826 | -49.11385 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb82478e-48dc-3fb4-98e2-b99ba943a2a3 | -12.54242 | -47.09499 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 089abf52-3326-3e0f-8475-3c97a03d47ed | -9.94678 | -46.53237 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2db09ba5-71ab-3adf-ac85-c64d14dc023f | -9.56349 | -46.56512 | 2026-09-19 04:40:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9898690b-ef07-3722-8dab-0826c54c21e8 | -12.12411 | -45.15428 | 2026-09-19 04:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ab3e5ba-791f-3a2b-b52c-ca433e345ce4 | -11.04667 | -48.30884 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b2954af8-d428-37d3-a884-ee661422082c | -13.61463 | -48.31902 | 2026-09-19 04:40:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 13e199e4-bd20-3058-9595-1875c42ac40b | -11.1331 | -49.04143 | 2026-09-19 04:40:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d15c38c-53df-3ecc-8275-4058daeaef2a | -11.07979 | -48.29572 | 2026-09-19 04:40:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5911acaa-0dc3-3f80-a25f-cfa0644407c3 | -10.88052 | -54.07138 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2afaf651-a869-38d0-b21a-6ff75e168c5e | -13.00228 | -46.98568 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 541923b9-f253-3bcd-ae96-addeffea0db3 | -11.50074 | -47.72066 | 2026-09-19 04:40:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d82737f-332e-3071-81cb-3ee9a08164a3 | -14.94775 | -49.94061 | 2026-09-19 04:40:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1194591f-5906-33b5-98df-48639fef4ee9 | -11.31327 | -47.2637 | 2026-09-19 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0855bc5-8c5f-3813-bda5-a4c3c8bb4adf | -8.32847 | -50.86105 | 2026-09-19 04:40:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06c28f46-2726-3fac-83b2-989bd14dbbcf | -13.234 | -46.90775 | 2026-09-19 04:40:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a7af966c-d6a0-3e02-bce8-fceb5f6c92e4 | -10.89518 | -50.88624 | 2026-09-19 04:40:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ed3599f-789d-3b16-af22-e970b6893817 | -11.48865 | -47.66802 | 2026-09-19 04:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 69107784-e3b1-3996-b474-43a77d022e09 | -9.56793 | -46.55863 | 2026-09-19 04:40:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0ed008c-5ee2-3b7e-86ff-ee8746a7fe4b | -10.80146 | -48.11522 | 2026-09-19 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 73dd9c0a-6e1d-3a28-8177-e22f7da131c6 | -10.5029 | -46.71814 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 393c3a10-2328-33c1-b231-45beb89b38d9 | -12.13922 | -47.0159 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eda229a5-0de0-3ad3-9196-f06271e87446 | -10.16512 | -45.36917 | 2026-09-19 04:40:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 672e6204-94f3-3d34-a783-c1865063e9a8 | -11.29938 | -46.76553 | 2026-09-19 04:40:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6f1370d-3f31-343b-9ec2-4b7fad0942fc | -11.06646 | -48.27176 | 2026-09-19 04:40:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 88838908-1146-3b03-a92a-c64dab9833a8 | -10.9716 | -49.74327 | 2026-09-19 04:40:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6bbf2cb-2e4a-3b0b-b48c-c5362a77d7ac | -10.70877 | -60.72872 | 2026-09-19 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 412ccc5c-0edd-3631-924f-ab2eb0aa2909 | -13.6291 | -48.31413 | 2026-09-19 04:40:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1a65a0da-c6b2-3643-b594-3072611001bc | -11.0615 | -49.76624 | 2026-09-19 04:40:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c4cdd4a-0e5f-30e8-95ba-f3872ac42bb3 | -8.92295 | -49.99861 | 2026-09-19 04:40:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8cc7db38-34d2-3f3e-9dc3-525ade78a45d | -9.56412 | -45.46672 | 2026-09-19 04:40:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d96d8213-9750-3c1a-b985-6cbd6dd03523 | -11.90887 | -50.12003 | 2026-09-19 04:40:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1f370c3c-592e-3c64-9307-24e0e001ad20 | -10.82087 | -50.17192 | 2026-09-19 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16e21747-cf61-3080-b903-08c3ed34f9f1 | -12.14422 | -46.9839 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 563a408e-4d08-3b32-a07f-84139cd54132 | -8.92016 | -49.99666 | 2026-09-19 04:40:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ba05335-8065-314c-85f1-8f4021f057b7 | -11.51937 | -46.87356 | 2026-09-19 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d6705ac4-50da-35aa-b8cb-4c89026d76bc | -11.30438 | -46.75546 | 2026-09-19 04:40:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b4b5e6f9-85a2-3d34-b415-2cae56d4bfed | -11.05289 | -47.94116 | 2026-09-19 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08d3d99d-704f-353a-a65d-b41f9334e532 | -10.32098 | -45.30849 | 2026-09-19 04:40:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed5613f2-9c0d-3149-a904-6be44a4ab216 | -10.48476 | -46.29799 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da758da8-86bb-35f0-a2ee-b26ac3f5f715 | -6.76634 | -59.42539 | 2026-09-19 04:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 80e7c90c-3574-3fef-bbdb-adbd3467da80 | -10.83515 | -50.1744 | 2026-09-19 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e4dd97c2-c23d-3eb2-9cb4-d649139e21fd | -11.24755 | -54.09911 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee54c115-5719-3f5f-958f-0efeca62ee72 | -11.97182 | -44.99457 | 2026-09-19 04:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78ddb0a7-df73-3647-a7ed-d83ac7d47260 | -11.37583 | -47.0351 | 2026-09-19 04:40:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2fbf10f4-2e0a-3811-a2ab-64afc38da1b2 | -10.7148 | -60.72926 | 2026-09-19 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 70468de6-b8fd-36a0-b97a-3563071d67ee | -12.26621 | -57.1805 | 2026-09-19 04:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a35aa59b-c568-390d-9acd-5c4ae5ee937a | -11.46487 | -45.71112 | 2026-09-19 04:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a34aa440-19e9-3499-ae2e-3e487d9d390d | -10.86274 | -56.19846 | 2026-09-19 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ad5b867-ecab-39ab-9846-16dbb9e48beb | -11.81118 | -46.8288 | 2026-09-19 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee73a0e6-c8c7-3641-8564-7275b5e15038 | -11.24494 | -54.10434 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dfd024d8-9aa4-3521-aab5-bba2af1f01a3 | -11.08036 | -48.2922 | 2026-09-19 04:40:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a4d12293-5d10-3641-a3e9-18243b2c72ee | -9.84091 | -48.39682 | 2026-09-19 04:40:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b84fa604-70f8-3cf6-a34d-a6c9afb2f101 | -11.86062 | -47.60581 | 2026-09-19 04:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a725508-1800-3ffb-9193-c32ae17df9d0 | -9.32517 | -48.19405 | 2026-09-19 04:40:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6909fce0-9517-38e5-90c9-26d6c900efc5 | -12.79825 | -49.09358 | 2026-09-19 04:40:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1eac12e9-6b2c-33ed-855b-85c3b098e485 | -10.94349 | -48.38433 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9eef0011-4534-3107-9382-096865e518ef | -12.39087 | -48.47926 | 2026-09-19 04:40:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eff7631e-7907-32e6-8cfe-fd50a5f2fb00 | -11.06704 | -48.2682 | 2026-09-19 04:40:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f766b243-1198-3be8-bece-5cd228b8b1bd | -14.79377 | -48.57786 | 2026-09-19 04:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README65.md)
