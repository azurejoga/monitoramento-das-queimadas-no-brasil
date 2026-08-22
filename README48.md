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
| 01f5af45-d0eb-39c0-9c07-b7f09d06a45c | -6.88797 | -56.72511 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b1c4e9f3-275d-3b61-a4ac-b5e83e8751e1 | -6.81351 | -59.42558 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a5454911-2fa3-34af-8fbd-beefc9037bf0 | -12.79456 | -48.45654 | 2026-08-22 05:04:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1dbac942-8713-31b6-bb38-266eb025b379 | -6.88757 | -59.0466 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d72b10ff-3d6f-3d45-b4c8-cc8427cbf710 | -7.23054 | -51.68812 | 2026-08-22 05:04:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4d55f05-2e92-316e-a262-25c0e6b45309 | -6.86003 | -59.45881 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| a6a02bd4-7635-328b-99de-5b17660e6b71 | -6.11366 | -59.9283 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50be2b0e-b1f8-3645-80c0-9f8295f4a40b | -10.65327 | -51.59067 | 2026-08-22 05:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb983915-8215-3eaa-97f4-e95bec1c3264 | -6.86216 | -59.03761 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 74cf473a-d0da-3b47-b180-53bc9f6b3ed0 | -6.88342 | -59.43081 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4262cf10-14ec-3a26-875c-703f0f5f6823 | -6.2704 | -62.52774 | 2026-08-22 05:04:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01e644ba-9be4-3f61-a56c-7763a8a1f11c | -7.53201 | -57.65315 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df696fb5-6a06-312e-8a0a-c25d3cb36cbc | -10.51155 | -57.60115 | 2026-08-22 05:04:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf6944bf-2143-32a0-b40b-c6b83bc66a25 | -10.51605 | -50.77604 | 2026-08-22 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 466825a5-c058-3d46-af68-d975efe56056 | -9.39182 | -55.97876 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2ff1b2f6-4dcc-3d4d-b68d-44eea10c90e0 | -12.71453 | -48.41733 | 2026-08-22 05:04:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f438573f-46cf-3561-a75f-72dc40d4bbc4 | -6.88809 | -59.40411 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8602a24-db46-3efc-a6af-5952b6f67564 | -8.52876 | -54.83759 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1063b6d3-bbf3-3175-a07b-fdf5ca11ca49 | -8.52376 | -54.8255 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 0f006ef3-6b4f-3deb-b623-249ce2a98720 | -6.77514 | -58.66996 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c7c96f15-b485-3f19-aa6d-a3f6f0da6786 | -8.03093 | -54.00445 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b13b67cb-d84f-3ddf-9d81-a1536e8d8274 | -6.64326 | -56.34156 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd170b81-dc4d-3858-a019-205ecb2d1a65 | -7.38185 | -48.08235 | 2026-08-22 05:04:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5df9c2b0-025d-31f3-974b-4cc8aea5854b | -6.68942 | -59.10147 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd55a0ac-ea67-3b13-a333-c4d977247412 | -9.23665 | -60.38924 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b26e8c2-5d00-38e3-9749-d7b65b4da9e1 | -10.52975 | -50.78222 | 2026-08-22 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6db1054a-6e52-3837-9ff3-9daecb9f18dc | -6.88205 | -59.41231 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 62e43105-f314-304a-9cbd-409e4d81acb8 | -8.62999 | -54.73392 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ac0a689-24bc-3767-a734-66c93ed7e429 | -11.62841 | -46.52376 | 2026-08-22 05:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4841508-a05f-3bda-9c3a-c6e7ec3f2112 | -8.6786 | -54.73437 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e44079d1-79d3-385e-98fa-3cd0daec96ce | -8.52995 | -54.83029 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fe2d7dd3-4747-3af9-9ecb-6041df6750f3 | -8.52936 | -54.83394 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4aeafcfc-62d9-3363-bf52-5fecf77c40fd | -8.02697 | -51.80032 | 2026-08-22 05:04:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7de6fc6c-2b4d-3917-ba3e-56c11e85856d | -8.52256 | -54.83283 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ef0913f3-c5c2-3541-a272-6e85ef3e6462 | -11.60134 | -46.54643 | 2026-08-22 05:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 250e17cf-a349-3fcb-aa0c-d88b345eb3b2 | -12.27718 | -43.15976 | 2026-08-22 05:04:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 97eb9a71-92c2-3e90-b26c-d5f380aca187 | -6.09636 | -57.8732 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8f0116f6-654b-30e8-a7fa-fecdcf2264b6 | -8.89908 | -60.54486 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 23.0 |
| e9691f67-501f-3d32-85a2-eb6eadb20a29 | -6.81877 | -59.42183 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| abd931de-5dae-35c5-99af-03c9ed32543f | -6.77231 | -58.70094 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0da1277-fd0c-3df5-9535-981a4b6793ae | -8.58908 | -54.72379 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0c6fc31d-c6ca-3e04-b2ed-2d1f2d00414a | -8.3999 | -62.69395 | 2026-08-22 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b6494f67-4335-31b2-9beb-026a13464222 | -7.02732 | -56.61132 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 70183363-03d1-32a1-87e7-fe15327ed959 | -6.7716 | -58.70501 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6ea0a96-a443-35a2-888b-ef7622cb12bc | -7.33893 | -55.70301 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1967deb8-a0dc-32e5-9e73-0f58e74ecc64 | -8.6275 | -54.72263 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a522f30-3b8a-330f-be99-ab5741d978a2 | -5.79714 | -57.55236 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2d77eb36-91ef-33d5-910d-6bc6b0114dd6 | -6.43976 | -54.95685 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0262b695-cef9-3dbc-bc98-5f5086b6fd43 | -8.90287 | -60.55067 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 72f3482a-b125-3b39-a7cb-8ddd8b7e6e51 | -7.34488 | -55.66675 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dcbdc8c0-4479-3919-93eb-7318db047f24 | -6.81429 | -59.42109 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 322499b8-aa1e-3487-8175-e23782ba5145 | -6.08902 | -57.91675 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9020994-c4f0-3db3-a47f-533dabed5e17 | -8.22202 | -55.02751 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 38b5a85e-c0e2-324f-9000-67fae280800e | -9.1784 | -56.99817 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d64783e0-263b-34ee-804e-fc5236193d7e | -11.2105 | -54.00092 | 2026-08-22 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 447ecb36-eefa-3579-b4f1-d4af3a234e3a | -10.8977 | -50.23939 | 2026-08-22 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 559f6beb-dd91-37fa-aac5-13d71bb4b394 | -10.27712 | -50.38602 | 2026-08-22 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51fa6cf6-cbda-3b1f-a34a-192114654f0d | -6.16057 | -55.44617 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 355d9446-5948-3c56-b72e-3d77ed5b96e6 | -6.86844 | -59.43732 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 756bbe0c-da98-3855-ad63-da296e23e19d | -10.81386 | -50.97591 | 2026-08-22 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 133099d7-1a83-32e9-b2c5-c659a0753a6b | -9.00243 | -50.7384 | 2026-08-22 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d6e74115-4c0b-3e80-a7e0-1265be7f6c93 | -8.52986 | -55.32797 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d582a998-5403-31e6-a030-b88dbd411811 | -8.16869 | -54.98791 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e9402b6-f483-3e68-8ed6-e9436d0f1ff3 | -6.7751 | -58.68494 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 04129ff5-38aa-3ffd-bca5-8ee262e00106 | -6.26974 | -62.53147 | 2026-08-22 05:04:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e63989bf-b0b1-31e8-9469-4db9cbec0af1 | -8.53376 | -54.84974 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06c3ae78-2bab-317d-b75e-ee85bd359b88 | -6.08889 | -59.96013 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 235b18bb-7235-3fe0-9cab-b4eb9208af06 | -11.17613 | -54.02408 | 2026-08-22 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5fbe6694-f556-3a6d-ab8d-27cf70b3779b | -8.53455 | -54.82352 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e6fb640c-f962-3201-9725-49ba28c32a06 | -8.58967 | -54.72014 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 276130c1-3ce3-3159-a39b-c36c47709b73 | -10.2784 | -50.37754 | 2026-08-22 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f59f9be-02df-3ed4-aa09-45a5caedd246 | -6.85241 | -59.41384 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a3720e14-10bb-374e-9aae-e964fd21b9ce | -7.47781 | -45.14724 | 2026-08-22 05:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 00942978-22f4-3fe5-8354-71b7ee6ac870 | -10.98787 | -43.70233 | 2026-08-22 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e09de64-5a31-3140-a600-e0f6ed330aea | -6.65579 | -56.33474 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e94329b4-3f82-3a61-994b-eb56fd5aa6ba | -9.16947 | -57.00593 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4c16e39-94ce-3884-9256-13bcb5d3ebc5 | -9.43825 | -51.60711 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d0b17da7-1c76-32fc-bf9c-113c06f0c75b | -8.55511 | -54.65485 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb1ebf11-573a-3cf5-9a9b-3d6038efd1a0 | -6.53905 | -58.52942 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ffb318af-bf85-3d57-97a6-1cae0532ecb6 | -6.79637 | -59.41799 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.8 |
| c46a185f-c27c-304a-a2ea-990206d56661 | -8.59233 | -54.74669 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 209be206-9df6-330c-b118-a01df33d1f99 | -9.43428 | -51.61017 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fcc1b2bc-0d39-3922-98a7-c6658084b423 | -11.74091 | -45.58623 | 2026-08-22 05:04:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d3bd2183-b47a-35f6-ba93-e248e5a498ef | -6.9385 | -60.0904 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5863ebaf-c88b-3df4-8b24-94da60c79687 | -6.93974 | -59.31791 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb45d929-e49b-388d-8716-1f90140a6edd | -10.29754 | -48.22717 | 2026-08-22 05:04:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91f7ddbd-e840-33b2-9b09-98666be7164f | -7.33802 | -55.68635 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee34af26-7cf2-35b3-bffa-f82810fef822 | -6.76821 | -58.68518 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 97d49928-9544-3f20-b064-a5325d65e681 | -9.11425 | -60.33541 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30919f19-21dd-393b-9773-c4a7455f321f | -6.93897 | -59.32236 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41404284-99db-3dcd-b10d-016c7a1ec847 | -8.99482 | -50.71716 | 2026-08-22 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c9f9b614-9440-3043-b213-71c2930cf512 | -8.61982 | -54.68406 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae173597-f9e3-3ee1-aeec-44090af67df1 | -11.10251 | -49.89072 | 2026-08-22 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b2ceae62-072b-3916-b8c8-150f2255653a | -6.79689 | -58.63528 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c8b45922-39d5-3212-afac-b52204121068 | -8.52615 | -54.81087 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 32e37b75-3c29-3f49-96b2-d59305b90002 | -11.73079 | -45.58487 | 2026-08-22 05:04:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2cf98a30-ca8c-3eb9-909d-7b1a0d7b283b | -9.42856 | -51.64714 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 485c7a86-11e8-3e27-83f4-99ff9756a9ab | -9.20835 | -60.7697 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3c59bd16-12d6-3eca-86d6-b4a14042b2fe | -7.36705 | -55.687 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 52e32004-76e1-371e-8cde-51dff4f6925d | -8.53675 | -54.83139 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |


[Clique aqui para ver as próximas entradas](README49.md)
