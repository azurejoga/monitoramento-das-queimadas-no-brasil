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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf99bce3-e1f3-347e-b5bb-532236963cc0 | -14.22128 | -45.79773 | 2026-06-06 04:06:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 67e5984d-50fa-3776-9b94-91adbbc0473d | -15.52664 | -42.66838 | 2026-06-06 04:06:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9b473e06-0aa1-3113-9822-1e52165acffb | -13.30597 | -43.77229 | 2026-06-06 04:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a44d0b9c-2ea2-3c8c-b970-d146e28560b4 | -9.07313 | -50.60058 | 2026-06-06 04:06:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 469fffa2-604e-3e6a-ab78-08b077ec55f9 | -11.73724 | -47.45169 | 2026-06-06 04:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f320f468-6e1b-3ae0-8039-2e58e5254da1 | -14.23806 | -47.97937 | 2026-06-06 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 471e980e-67be-348f-aca5-2718a4d617b6 | -8.9409 | -45.67348 | 2026-06-06 04:06:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| edbb9ea6-31f7-3dfb-92fc-fbf847f9bef2 | -10.94382 | -46.93791 | 2026-06-06 04:06:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe2c4192-d328-327e-9db0-03804eec3995 | -15.18231 | -41.81355 | 2026-06-06 04:06:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 343e9943-a28b-30a5-a9d0-c4f19a913fa5 | -13.36214 | -43.20344 | 2026-06-06 04:06:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| f164d022-487f-3a82-a2d9-07cd32f7bf85 | -12.50584 | -46.26941 | 2026-06-06 04:06:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c44d143-9357-3cef-8f66-5dee51dc4b90 | -11.56249 | -52.79545 | 2026-06-06 04:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 81772374-a719-3022-ada1-d98712171ced | -12.0632 | -48.42939 | 2026-06-06 04:06:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35634b84-0013-3e70-85c0-2200e808ffe3 | -11.55459 | -52.79985 | 2026-06-06 04:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c6f33486-0179-394f-ab4e-eb3e82be25e3 | -12.50867 | -46.30338 | 2026-06-06 04:06:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fe4a319d-68a0-371e-bd87-747e4a41bc15 | -9.92356 | -48.00056 | 2026-06-06 04:06:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7f95d86-afb5-3e09-81d8-713b1c48869c | -9.08211 | -50.61302 | 2026-06-06 04:06:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| abb85eef-0952-3405-a451-20943597b74e | -12.07118 | -48.42805 | 2026-06-06 04:06:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd989921-8e14-3b03-a9e4-d06ae2b7c2eb | -13.36286 | -43.19925 | 2026-06-06 04:06:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 1f88999d-c586-33f6-8c2b-01512e750ee3 | -14.22471 | -45.80227 | 2026-06-06 04:06:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 844c5555-76ef-3512-97a3-232d27490805 | -9.07076 | -50.60591 | 2026-06-06 04:06:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d53632a-034a-3700-a9f7-02d1c039c963 | -9.37396 | -50.53945 | 2026-06-06 04:06:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f1797ea-5c4e-3a04-8b11-de856f8ab4ba | -12.51864 | -46.27338 | 2026-06-06 04:06:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 114383ce-067e-3152-9864-760801d6b907 | -21.34756 | -48.62484 | 2026-06-06 04:08:00 | NPP-375D | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ef6310af-8da9-36a1-aa40-2c4ca9c19f98 | -18.60773 | -40.51477 | 2026-06-06 04:08:00 | NPP-375D | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6dcbfb9a-e524-3f52-be8c-f34f9a94fd85 | -19.74441 | -53.54811 | 2026-06-06 04:08:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 619a1afe-49a0-37c9-82b1-6d77243d145f | -18.86611 | -47.64435 | 2026-06-06 04:08:00 | NPP-375D | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d7ad2d16-7c21-3ce2-8318-0f5b705263a5 | -18.02383 | -41.83435 | 2026-06-06 04:08:00 | NPP-375D | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6bb460e5-aca8-30e5-b11d-32f4fc264b70 | -14.7725 | -52.68095 | 2026-06-06 04:08:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f5211788-6abe-3d3d-85ba-c6b7e7661074 | -17.99823 | -51.1451 | 2026-06-06 04:08:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fedb3f1c-eb84-3db7-886b-e19423298b48 | -19.75026 | -53.54819 | 2026-06-06 04:08:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c6d1534-ab62-320a-89ab-9b4799a45d01 | -19.74542 | -53.54163 | 2026-06-06 04:08:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ac2bb96b-62d8-3368-95b0-057f951e8387 | -14.76945 | -52.68383 | 2026-06-06 04:08:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d536f28e-4eab-31bb-b56e-6c6e2145282e | -17.30677 | -42.64431 | 2026-06-06 04:08:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4fda68e0-a546-3946-98a5-a983ad436e2a | -14.77057 | -52.67848 | 2026-06-06 04:08:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f52cf3fb-7ad3-348e-840e-65455f267fea | -19.74432 | -53.54639 | 2026-06-06 04:08:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| eadbb2de-c8da-37ca-bb8a-c2e77ce8281b | -14.4588 | -54.88906 | 2026-06-06 04:08:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 067befe4-546a-39c9-835f-6a19cb18e729 | -18.00202 | -54.28449 | 2026-06-06 04:08:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dd6fe99e-bff9-3261-ae41-00883b4387d1 | -22.37954 | -45.5375 | 2026-06-06 04:08:00 | NPP-375D | PIRANGUINHO | MINAS GERAIS | Brasil | 3151008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7d2565c9-d651-3bba-8530-d054e031f973 | -19.73844 | -53.54645 | 2026-06-06 04:08:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 43a6bf58-9e90-38f8-956b-9023eefbef27 | -19.75034 | -53.54998 | 2026-06-06 04:08:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e5141d15-d0a2-3379-9d0f-a3390a202813 | -19.7455 | -53.54328 | 2026-06-06 04:08:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2acac805-96f4-314e-a660-558cbc6f77e6 | -18.86952 | -47.64963 | 2026-06-06 04:08:00 | NPP-375D | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78308347-808f-32c1-8a4f-8a641679e845 | -22.94049 | -43.64973 | 2026-06-06 04:08:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1f86cd63-1b4e-33d3-8593-4755f5170fdc | -21.34728 | -48.62229 | 2026-06-06 04:08:00 | NPP-375D | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fffd4a22-e269-30e3-a50c-72595ceb3a01 | -19.7395 | -53.54173 | 2026-06-06 04:08:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d75ed5c1-f3d3-3383-9323-e29f7cd56462 | -13.93327 | -53.89366 | 2026-06-06 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03546ba5-4df4-36a5-b4b1-bba231b6dc86 | -17.31477 | -44.92201 | 2026-06-06 04:08:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87005b1c-b314-3644-b33a-409ba4a68320 | -14.45708 | -54.89656 | 2026-06-06 04:08:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66641905-7291-3031-8506-61cad22ecb34 | -21.40859 | -49.23111 | 2026-06-06 04:08:00 | NPP-375D | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9acc98ed-a3e8-37e9-87b9-f4a43a011452 | -19.73942 | -53.54012 | 2026-06-06 04:08:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 725935f2-4723-3c2c-9675-fc3634dfe69f | -19.73833 | -53.54481 | 2026-06-06 04:08:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d3b6c8d1-d4f8-30f5-9d20-7a17536fdf54 | -21.42512 | -48.64307 | 2026-06-06 04:08:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 548b9796-361d-3d07-92ee-d470b9027d9e | -17.30739 | -42.64054 | 2026-06-06 04:08:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e230bfa-c681-3a1b-9bd7-c142a5e28451 | -21.13162 | -44.0729 | 2026-06-06 04:08:00 | NPP-375D | PRADOS | MINAS GERAIS | Brasil | 3152709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e2c2e6af-f3de-35d7-866d-08a2177d8a25 | -17.29997 | -42.64309 | 2026-06-06 04:08:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db465f09-b9d0-3908-a3e7-7d6e2ee35a2e | -18.87035 | -47.64531 | 2026-06-06 04:08:00 | NPP-375D | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4887c5b0-bd3d-32ee-b809-d91d57bcedd6 | -17.30275 | -42.64746 | 2026-06-06 04:08:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 293bef21-7747-349a-9e6a-05ea827bb629 | -17.29935 | -42.64685 | 2026-06-06 04:08:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b32377e4-2c70-39da-a5f0-76f6cb07fab7 | -17.99749 | -51.14864 | 2026-06-06 04:08:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3356934c-b692-3898-a9ef-51022981192d | -17.30337 | -42.6437 | 2026-06-06 04:08:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fc859a05-bf63-3acd-8543-42163edec538 | -17.99835 | -51.14798 | 2026-06-06 04:08:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0a1cfa42-65e1-3a55-a94b-f68f14ffa66c | -17.31016 | -42.64491 | 2026-06-06 04:08:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60bbfe0c-7e54-3353-a942-80e4fa63074d | -17.31559 | -44.91739 | 2026-06-06 04:08:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98b5e395-06cf-30b5-8b36-481595221d81 | -19.75138 | -53.54333 | 2026-06-06 04:08:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d460a872-fe93-3df8-9722-37f58b9ec997 | -18.00328 | -54.279 | 2026-06-06 04:08:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f064b4b-078d-3051-9508-b2bd831c1bc5 | -21.34843 | -48.62053 | 2026-06-06 04:08:00 | NPP-375D | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 25cb9122-a787-327d-8915-77e03e774282 | -19.75145 | -53.54505 | 2026-06-06 04:08:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2d78354c-1bf7-31d2-af98-ec8ba844522b | -17.99687 | -54.27713 | 2026-06-06 04:08:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bb62ac7-be5c-3610-b1a0-fcdf13ea3c7d | -13.93444 | -53.89125 | 2026-06-06 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 237c27da-f671-377d-adea-96cf25593282 | -11.5499 | -52.7867 | 2026-06-06 04:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 2bba39a0-25f6-345a-944a-a736a4b2c189 | -23.82059 | -48.71135 | 2026-06-06 04:10:00 | NPP-375D | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b76f3fd2-6bcd-34c5-8015-f63686644685 | -22.1755 | -50.38342 | 2026-06-06 04:10:00 | NPP-375D | QUINTANA | SÃO PAULO | Brasil | 3542008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4ecb6bc6-1529-32c0-ac24-04f875c6d265 | -23.48538 | -46.55609 | 2026-06-06 04:10:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 45040171-5fba-3fe2-9776-dbe9077a3b3f | -26.54845 | -48.85466 | 2026-06-06 04:10:00 | NPP-375D | SÃO JOÃO DO ITAPERIÚ | SANTA CATARINA | Brasil | 4216354 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 21cb5637-ab8d-3e26-8668-5ba347693bc8 | -22.1708 | -50.38214 | 2026-06-06 04:10:00 | NPP-375D | QUINTANA | SÃO PAULO | Brasil | 3542008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 40f52448-0da6-3a06-8465-2623420ef5cd | -23.25316 | -55.08421 | 2026-06-06 04:10:00 | NPP-375D | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 95c0abea-eba6-3e6b-b1a2-335bd0fbfc0d | -23.25441 | -55.07905 | 2026-06-06 04:10:00 | NPP-375D | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cd7db82e-7558-31b1-b460-12906e807c56 | -22.79671 | -49.35107 | 2026-06-06 04:10:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b95b8c0-de0c-37ee-8015-ee8fee30f29a | -22.99797 | -49.55877 | 2026-06-06 04:10:00 | NPP-375D | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3584222e-154d-3491-92e8-326ec11487ad | -22.17436 | -50.38897 | 2026-06-06 04:10:00 | NPP-375D | QUINTANA | SÃO PAULO | Brasil | 3542008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 96594faa-3b4b-313e-af78-f0008b270a1d | -23.73273 | -54.60661 | 2026-06-06 04:10:00 | NPP-375D | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6977cc91-24c6-3a27-9b6e-245723f4e309 | -22.1748 | -50.38471 | 2026-06-06 04:10:00 | NPP-375D | QUINTANA | SÃO PAULO | Brasil | 3542008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 1f23a817-8288-3ae2-9a62-caaefe23efdf | -23.73163 | -54.61126 | 2026-06-06 04:10:00 | NPP-375D | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 02b5ad3e-3d99-31c0-92c6-798fe806d25d | -22.99546 | -49.55957 | 2026-06-06 04:10:00 | NPP-375D | BERNARDINO DE CAMPOS | SÃO PAULO | Brasil | 3506300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| bd0924f1-ed12-3d48-a445-bb5b051e25fd | -11.5499 | -52.7867 | 2026-06-06 04:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| f72d81d0-8759-3c83-bd22-f1e0f42ff4f4 | -11.5496 | -52.8076 | 2026-06-06 04:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 40.0 |
| b3187e11-1f4b-3b69-8fcb-0282ce5f4a35 | -5.29927 | -47.23992 | 2026-06-06 04:21:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3dc9993b-2f49-35af-bf33-52f5a39d39c9 | -5.92574 | -43.47873 | 2026-06-06 04:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bb915865-d6db-394c-ba76-58f0af5f449d | -5.34761 | -45.18375 | 2026-06-06 04:21:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ba3812f-2713-306c-871b-d62e7359fc12 | -6.1104 | -45.85393 | 2026-06-06 04:21:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a02c0fc-5631-3026-9587-8334319ed88e | -5.80913 | -43.79163 | 2026-06-06 04:21:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2084e520-d370-3e31-968a-2cf4036644e0 | -5.44746 | -44.812 | 2026-06-06 04:21:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6141ecb1-fea9-3307-a1f4-0f14b1908e08 | -5.78843 | -45.12542 | 2026-06-06 04:21:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e83eef61-a0aa-3971-ae33-a88703737a09 | -3.98575 | -47.9316 | 2026-06-06 04:21:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4a72b757-1227-3527-9350-8716994794a3 | -5.81245 | -43.79215 | 2026-06-06 04:21:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77a4a038-36f1-3f03-ab85-1207fe331976 | -5.35038 | -45.18777 | 2026-06-06 04:21:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 665c97bb-1611-302d-895b-6193621652ee | -5.55642 | -43.97276 | 2026-06-06 04:21:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0116426f-5b15-3725-93d2-8e8d9ffd4924 | -3.05797 | -40.84782 | 2026-06-06 04:21:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9a81753b-33ef-3f48-8e5d-41d29de61a31 | -5.41452 | -44.31141 | 2026-06-06 04:21:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README6.md)
