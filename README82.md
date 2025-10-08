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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 271f986e-f3c9-3acb-b3bf-1e4c662df060 | -13.25528 | -48.05215 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06c44917-03aa-32dc-a7ff-027d99cdadb1 | -14.64811 | -52.54067 | 2025-10-08 04:40:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9070b72d-0883-32f6-a5d6-e47d7d99135d | -12.99438 | -46.77619 | 2025-10-08 04:40:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2aab961e-0bdb-3134-8435-09f2dc6f6a36 | -11.15662 | -54.86155 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c96e49ee-c41b-39d6-b3dd-103a6327c749 | -13.20421 | -51.69503 | 2025-10-08 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a97b686f-4449-35df-a3ff-cc33c7525ed1 | -12.25151 | -47.85728 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1ee66520-d8ee-3c18-b59c-c0503929c0eb | -13.80542 | -45.79728 | 2025-10-08 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6611287-457b-3bcf-bb63-c4b172cf04ce | -11.33488 | -56.20958 | 2025-10-08 04:40:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4ef2b781-512a-337f-b17d-ca90e7c702bc | -15.3504 | -47.33345 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2fa53ff8-6a80-3d4d-a587-a311899aada6 | -14.71088 | -46.06067 | 2025-10-08 04:40:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 868341cc-a1cd-3447-a59c-621efaa51e2a | -12.39229 | -51.14428 | 2025-10-08 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa8e291a-4fe1-395d-80b4-b40d56491f74 | -12.93499 | -46.81328 | 2025-10-08 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ede8f95-2a82-360b-af9e-f115103b8bbd | -15.99269 | -50.94601 | 2025-10-08 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a35658dc-04ba-3947-9e25-c4704cf8a3a9 | -16.32881 | -47.06125 | 2025-10-08 04:40:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 618b70db-7754-3b27-96f9-320c04763342 | -12.38084 | -51.08801 | 2025-10-08 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f720bc46-4e6a-35ea-8f75-20ff38c5f066 | -15.62051 | -52.58089 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cc1ab602-02e7-3148-bd74-d2e1af0a910d | -15.38077 | -46.28246 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 91c8fe32-9278-33c0-a518-e6531406e2e1 | -15.34685 | -52.81812 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2826c0e-20ad-31f3-86a4-0cb9e5bba4bf | -11.16653 | -54.87331 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6e2066c5-6696-39ed-9bac-1db79ce1c45e | -15.38193 | -48.00299 | 2025-10-08 04:40:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1c1736cf-ec24-304e-a055-31c3f77c83e1 | -19.51606 | -44.07005 | 2025-10-08 04:40:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51e7ad01-22d6-3698-afb4-adeee3640217 | -11.33561 | -56.20559 | 2025-10-08 04:40:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6a18896f-aad6-3429-a8a3-be076963011f | -17.29676 | -58.06857 | 2025-10-08 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| f45e38b9-48eb-3015-9f3e-f26fa6f2f8e0 | -12.94022 | -46.85677 | 2025-10-08 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4579134c-2f7f-366a-96d6-671063de91f7 | -13.20638 | -51.70275 | 2025-10-08 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| aa1e1885-2d17-35d7-a9cd-0c59e5689521 | -11.15706 | -54.88183 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b00e96a0-e3c2-3f27-a71e-198e509d90dd | -18.29625 | -45.43989 | 2025-10-08 04:40:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 593fd3e7-6548-315a-8e97-bf053bd69b83 | -14.92777 | -46.7901 | 2025-10-08 04:40:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7ef4569f-86a2-344a-82a4-5164239ba534 | -14.71347 | -46.07199 | 2025-10-08 04:40:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c3e22f0e-3cd2-3a13-85fc-c280768a2209 | -15.15223 | -52.76246 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 426be78b-ed47-30db-89be-834cfa0fed5d | -17.81914 | -45.32098 | 2025-10-08 04:40:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f7a47e1-3526-3317-bf94-2501a19b8f29 | -12.74487 | -44.72361 | 2025-10-08 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 3f871e12-78a6-3a53-b861-455c847e4eac | -13.3242 | -48.02405 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 39981b54-d815-30e3-9178-4fd507af7d41 | -15.63397 | -52.51917 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04372cd7-673a-390a-bae9-ac79f40368cc | -13.38462 | -47.56931 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 40f91771-ce95-3c0c-bfdd-7fb3242ce716 | -11.75073 | -50.92733 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 52.6 |
| d2b8119c-d486-3d37-9fc4-6f0b965fc74b | -18.02828 | -51.14521 | 2025-10-08 04:40:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 240bb47b-a519-39c1-9f46-22c411ba8109 | -10.97546 | -59.02496 | 2025-10-08 04:40:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f385d69b-f049-38ac-9fdd-b11427ee088f | -11.15232 | -54.88609 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8075e79f-3b8a-376a-8b2c-6df9de4d2da5 | -13.39374 | -42.70144 | 2025-10-08 04:40:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ade41b04-093f-3608-b88f-544b5db95f18 | -12.39274 | -50.30318 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16837bd7-6a72-3cff-8f7e-afc1c18df567 | -12.25447 | -47.86172 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e43cf76a-4b92-329b-bef0-a488245317e9 | -18.06071 | -44.47295 | 2025-10-08 04:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b6765441-d6de-30b7-ae2f-aa4c22a5db56 | -14.82317 | -48.41341 | 2025-10-08 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e87dd20-bb04-3370-bcd3-6ce2bb108103 | -14.61408 | -52.4742 | 2025-10-08 04:40:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 03194fb0-a060-388a-b2c3-72aae2a93d7b | -11.73574 | -50.95739 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d13d26c-b184-3c94-a7b8-ba1a30a939c7 | -13.75389 | -45.74987 | 2025-10-08 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ad2b440-3b68-31e7-a24f-fe65b7feaa46 | -13.69588 | -55.01255 | 2025-10-08 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c26ad88-cf39-3b1e-8dad-79e631c7225c | -12.37949 | -50.30104 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ed8f2e16-ba08-3190-8ace-4ad40a50da59 | -10.67754 | -54.69415 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 305d2811-8b3d-3691-9a75-00bce25ee468 | -12.41947 | -45.6247 | 2025-10-08 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 9e28076d-9682-3552-9881-62bd03eb80e0 | -11.7621 | -46.81549 | 2025-10-08 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7838cb9f-938e-3ee3-964f-ff5baf0fa5a9 | -14.70751 | -46.08586 | 2025-10-08 04:40:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a20b0aed-f0f7-3f81-86fe-76e37c5dccb9 | -17.2897 | -42.65608 | 2025-10-08 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ea2f15e-79ee-3099-8e65-12def671d083 | -15.38129 | -47.30785 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef34fc03-66c0-3268-8111-51c356585e82 | -11.3398 | -56.20639 | 2025-10-08 04:40:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c42b469b-ec9d-3c36-a015-d2790acad989 | -12.38842 | -51.14727 | 2025-10-08 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cdc36d19-3b36-330a-84e7-738d661adfbf | -11.72473 | -50.94112 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 19.5 |
| cce07a7c-3334-30ee-a500-eea2c56f38cc | -15.7033 | -47.51587 | 2025-10-08 04:40:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60222453-d37c-3e7d-b7d9-0607a0521f79 | -18.06124 | -44.4685 | 2025-10-08 04:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 63854f59-40d2-3a1d-ad10-ae16b15b57a8 | -16.88567 | -46.95912 | 2025-10-08 04:40:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 026507ff-335b-32b4-b373-33124223b483 | -11.9533 | -51.46553 | 2025-10-08 04:40:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f80ee36f-dc40-3782-8805-14f2edcd1425 | -11.16522 | -54.85796 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8270e84c-4a2a-30da-a718-cb94933a6eeb | -14.68944 | -48.41398 | 2025-10-08 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e03ea494-64ae-337e-83bf-81d62a697772 | -11.44667 | -50.20779 | 2025-10-08 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 54643141-9f98-3495-986c-82c6aec31a52 | -11.66904 | -50.97185 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 601f79c2-b7a3-34f6-8ccd-d5b0fbde06df | -12.9433 | -46.86194 | 2025-10-08 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7f8b34ba-28ed-3271-9530-87c95679550c | -13.06642 | -43.59321 | 2025-10-08 04:40:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a14e98f4-349f-3d96-bb68-8ed478276358 | -12.24548 | -47.87339 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7a8841c8-e3e1-3a09-a4f8-6d415cb8ba48 | -12.94156 | -46.84752 | 2025-10-08 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6a29b78d-0e8a-3e63-b916-d63a2c55bce7 | -14.67427 | -51.89643 | 2025-10-08 04:40:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e4fc0823-5848-3000-bef8-ac13c998461a | -16.06725 | -47.77417 | 2025-10-08 04:40:00 | NOAA-20 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8eb7e42a-773e-3bd4-9010-ee1edf879268 | -18.0226 | -44.94276 | 2025-10-08 04:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7518529a-9d7c-3c86-9ad8-c65715a0c820 | -15.22197 | -49.31614 | 2025-10-08 04:40:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c155f88-6063-3111-b0ac-0907a35969c1 | -13.28594 | -48.04072 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d26e2c9-8051-316e-ad79-b445969eebdd | -13.69507 | -55.01726 | 2025-10-08 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a6cff89-889d-3086-8d4b-27cee3cbbc37 | -15.31729 | -47.93235 | 2025-10-08 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d00bf799-75dd-3cb0-b003-dc784f5f8a05 | -15.9884 | -50.84182 | 2025-10-08 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d56c58c5-eb28-3b8d-8a0c-d2d5987412f1 | -15.94766 | -42.60398 | 2025-10-08 04:40:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 37fc2c1f-d729-376b-9726-69c386e35baa | -14.69687 | -46.01129 | 2025-10-08 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 66dadc1d-b78b-3faa-b0f8-95f33f6e3a31 | -11.13531 | -54.88653 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1799c04d-f241-3f75-8d1f-8ace7ee6bee2 | -13.28133 | -47.56168 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| baf68340-52c4-30ad-bf9c-406a3e3e9b64 | -12.94633 | -46.84502 | 2025-10-08 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b1c08db7-77eb-3c11-8f92-c5a99c62bb51 | -13.29156 | -47.15597 | 2025-10-08 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 449c1a62-07d7-3348-b832-6a40cce3e15e | -11.67679 | -50.9659 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7c206718-fa3f-3db4-88d9-dd77e793ada8 | -18.09802 | -44.70325 | 2025-10-08 04:40:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3adc6b64-e79e-3789-922f-a49f095e62eb | -13.0697 | -48.01359 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 13e38f69-7ceb-37f6-924c-769a79b64af2 | -14.44658 | -48.79155 | 2025-10-08 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4a14949-bd38-348b-9fd9-1d021989f7b6 | -12.39673 | -51.13776 | 2025-10-08 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30cfe93f-6230-3586-ac6a-bb4f4c1cd92d | -12.85933 | -43.81895 | 2025-10-08 04:40:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cec2a1ba-816c-3ff1-8d1e-5f151ade2183 | -12.45618 | -54.72011 | 2025-10-08 04:40:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a244a1cd-21a7-359f-b106-d5adffce687d | -13.26918 | -47.56865 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aad098b4-8011-332a-9554-b0a9babaa96c | -15.38126 | -48.00471 | 2025-10-08 04:40:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eecb03ea-a159-3f9a-9e15-5c91dc2e0358 | -11.45771 | -50.20237 | 2025-10-08 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3393a7ce-f88c-3509-b0c4-bd961b70da62 | -15.37127 | -47.32487 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f15c10ed-e5a5-3a0f-883f-3e61217ed8e9 | -11.69485 | -50.9579 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f7de8f71-94f6-3e02-b509-6a1418cd6fc3 | -13.23241 | -47.79342 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41242c15-8269-3259-ae75-9dfcc0289b3e | -12.24967 | -47.86959 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a5fac2cb-aa10-3f89-9821-80608f06c005 | -15.07403 | -46.62509 | 2025-10-08 04:40:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aebe3525-89f5-35af-9df7-aad77906158f | -12.31415 | -55.109 | 2025-10-08 04:40:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README83.md)
