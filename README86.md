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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52b9e05f-0d1c-304c-8a1b-939e6e4d0974 | -9.4497 | -62.3485 | 2025-08-30 06:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 226.1 |
| d80e8146-6c88-368c-ad12-d12ed5360bde | -9.4432 | -60.5692 | 2025-08-30 06:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 9fc79955-2317-357a-b4d0-858a2f5b864f | -10.0347 | -46.0527 | 2025-08-30 06:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 0f1f4ecb-82ea-3683-8677-85890b9c2c71 | -13.3825 | -46.9697 | 2025-08-30 06:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 1ee81eab-8ea4-3d3d-bf00-0e953f288354 | -13.3821 | -46.9924 | 2025-08-30 06:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 125.2 |
| ad409836-4658-361d-b66f-80166cc052b3 | -13.3623 | -47.018 | 2025-08-30 06:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 151.4 |
| e3f86af0-2448-3692-8eb6-eb22d64a94e6 | -9.4684 | -62.3286 | 2025-08-30 06:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 179.7 |
| f214656c-418e-385d-9b12-5d547ea76c12 | -9.462 | -60.549 | 2025-08-30 06:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 4746e6a1-4b38-3bf5-b597-ad25591a0af8 | -9.4433 | -60.5499 | 2025-08-30 06:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 0bfb59d6-417a-3de9-89e2-87415fd8574d | -6.4253 | -45.6214 | 2025-08-30 06:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 6ca60d26-2566-3aa0-a194-4842e3596c19 | -9.0614 | -65.4355 | 2025-08-30 06:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.9 |
| fa125ec7-2816-3aa7-a0b2-6a7ce49c2bf4 | -11.856 | -46.4487 | 2025-08-30 06:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 0b6e6d0a-c0f2-3a1d-863f-f4296d22e24c | -11.8365 | -46.4741 | 2025-08-30 06:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 139.0 |
| e455e205-b207-3488-94b3-489a69cdc9b2 | -12.0148 | -44.0054 | 2025-08-30 06:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 68fbcf28-3296-343d-822b-ea09d167e4b9 | -9.4497 | -62.3485 | 2025-08-30 06:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 209.7 |
| 41504d86-c47a-307a-88f6-3d55fdd89074 | -9.4433 | -60.5499 | 2025-08-30 06:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 843d75c9-5055-3da9-830e-18ec9830b294 | -9.6193 | -45.966 | 2025-08-30 06:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| a451d66a-c92f-34e5-918b-45dc90a7cec0 | -11.8956 | -46.3753 | 2025-08-30 06:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 6d4a0cd0-d144-3624-b137-a10944290c02 | -11.8948 | -46.4207 | 2025-08-30 06:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 5dd158d7-d585-362a-9935-9b352c1c6de9 | -9.462 | -60.549 | 2025-08-30 06:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 2a4c8048-f845-363a-8480-69124c9e5fe1 | -11.876 | -46.4007 | 2025-08-30 06:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 1d15cc19-ab40-3f6f-bb2d-df9dc5195070 | -6.1853 | -43.3257 | 2025-08-30 06:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 4ea9550a-1236-3886-9ab7-52bba0a135f6 | -10.0351 | -46.03 | 2025-08-30 06:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 3e8f2496-fd6a-3103-95d7-058f0d4c6bab | -11.8952 | -46.398 | 2025-08-30 06:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 286.5 |
| e484c522-ffd2-3f6d-b540-1b5c4a0b3c40 | -9.4684 | -62.3286 | 2025-08-30 06:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 195.8 |
| ef36ffde-cb4c-3f49-af3e-797c86b05e7e | -13.3838 | -46.9017 | 2025-08-30 06:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 373ac481-b65f-3a35-80b8-b6a871ac68be | -13.3645 | -46.9047 | 2025-08-30 06:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 488.9 |
| 5b50f292-1c5d-36f7-9517-69351268e6cb | -11.8764 | -46.378 | 2025-08-30 06:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 3e2907f5-305b-3447-af94-4703d739352a | -9.4498 | -62.3294 | 2025-08-30 06:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 318.6 |
| ea0d296c-3382-3823-9bb2-df8baa4ce546 | -13.3649 | -46.882 | 2025-08-30 06:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 823.4 |
| c25c6c71-0abd-33d0-bfa9-403a94d63d91 | -9.4683 | -62.3476 | 2025-08-30 06:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 125.3 |
| b297713b-fb4e-3c90-b46a-cb803d5c3fdd | -12.0153 | -43.9818 | 2025-08-30 06:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 82afab3b-569b-3601-9239-25aa2e6046ad | -9.4432 | -60.5692 | 2025-08-30 06:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 3e0c0f24-3c51-3bee-9d76-dad7b686056d | -13.3456 | -46.885 | 2025-08-30 06:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 159.6 |
| b8334f46-6469-32a8-9b95-683308bed711 | -13.3843 | -46.879 | 2025-08-30 06:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 0722bfe5-fe90-3da0-84b6-e906f8089d90 | -13.3452 | -46.9077 | 2025-08-30 06:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 05bb7f4f-e2cc-3eab-8d32-0d3de72d0f4f | -9.06826 | -65.44259 | 2025-08-30 06:27:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 94a6b706-8d07-3af3-9e52-98955679b70a | -9.06583 | -65.4483 | 2025-08-30 06:27:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f077d22b-7059-3c4f-bdb9-f6ccc35b78aa | -6.56866 | -69.95774 | 2025-08-30 06:27:00 | NPP-375D | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 099bd71c-18a7-3095-8bf8-44197c30a4e5 | -8.04084 | -70.0649 | 2025-08-30 06:27:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| af923035-f7cb-3254-a7b7-8f4f7657afe0 | -8.44755 | -70.14445 | 2025-08-30 06:27:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61dcd13d-d1f8-3c78-b7bd-2ffc9ce4a87d | -8.64227 | -67.25867 | 2025-08-30 06:27:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d9f96e2-17df-390b-b06c-133399cad7a5 | -8.64273 | -67.25509 | 2025-08-30 06:27:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4f121a9-665d-3bb1-a221-b419e7150dab | -8.96256 | -65.96838 | 2025-08-30 06:27:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4556623-a531-301d-9322-20191ae10fd4 | -8.38852 | -70.23657 | 2025-08-30 06:27:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d63e169-1d2b-319d-abf3-c5b74de02ccb | -8.6276 | -67.24206 | 2025-08-30 06:27:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a10af31a-afe3-3e8c-801b-3ecc92baba43 | -8.54895 | -63.02504 | 2025-08-30 06:27:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30ca3b77-0929-3005-9c6b-d9cc805542cb | -8.62713 | -67.24567 | 2025-08-30 06:27:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4242dd52-20f9-3c80-85da-755f1e31d3ca | -8.56069 | -63.02058 | 2025-08-30 06:27:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8859cb14-f3fb-3c4a-a97f-26f7b549d572 | -8.04608 | -70.09328 | 2025-08-30 06:27:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 901276ee-f55c-3855-bde2-0e04f00bd6d9 | -9.07327 | -65.43929 | 2025-08-30 06:27:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 98a2f787-dc38-31bf-817d-6a4c5f785fa6 | -8.63648 | -67.25865 | 2025-08-30 06:27:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86645fc4-5fb0-3917-bcea-35204b690c35 | -8.55354 | -63.01965 | 2025-08-30 06:27:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e104cb39-7d28-341a-85ef-c5c135674f4f | -8.63697 | -67.25507 | 2025-08-30 06:27:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12a2e7ce-2cb1-3ab0-9a8a-e46a5a7b6303 | -8.5561 | -63.02593 | 2025-08-30 06:27:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0009e351-7002-3b5d-8fa7-3759be3d6697 | -7.99757 | -70.28612 | 2025-08-30 06:27:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3303f2a2-df8b-3fa4-9715-1a1504460369 | -9.06267 | -65.4369 | 2025-08-30 06:27:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0faffe0f-4be2-3078-95be-2ed1c18d1554 | -9.07385 | -65.44832 | 2025-08-30 06:27:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4719e80b-1004-3f00-810e-eef8c3b4b416 | -8.56411 | -63.01989 | 2025-08-30 06:27:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23569a75-4cc8-34a0-83b1-f10c2d0601d1 | -9.06203 | -65.44179 | 2025-08-30 06:27:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c92239d8-1a96-302f-9d1a-e4ec0282841b | -8.44507 | -70.14148 | 2025-08-30 06:27:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 88dbf9d5-b6a4-3083-be17-f2e7b915b869 | -6.56929 | -69.95335 | 2025-08-30 06:27:00 | NPP-375D | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 999b9126-f6db-36e0-9232-bd6b9b2f5af6 | -8.63676 | -67.25792 | 2025-08-30 06:27:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 524ef907-9d78-3274-b87e-0a163fa102e1 | -8.04545 | -70.09776 | 2025-08-30 06:27:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5eac755-addc-35fd-9a9e-256a7a3caff8 | -9.06643 | -65.44339 | 2025-08-30 06:27:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 08230706-c450-3a66-b596-72be103b10fc | -8.44305 | -70.14381 | 2025-08-30 06:27:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1b9042d-1c44-348c-9233-1f82ff8ad578 | -8.55979 | -63.02758 | 2025-08-30 06:27:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 83fac8a1-c6cc-3235-9a7e-6139b205c71a | -8.63722 | -67.25433 | 2025-08-30 06:27:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7954d8bd-e16b-3c96-a5a0-686956446170 | -9.06704 | -65.43847 | 2025-08-30 06:27:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| d3c09891-f577-3ac7-a5e4-43a25186a71c | -9.07145 | -65.45407 | 2025-08-30 06:27:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 08438ff8-8223-3250-8396-b3519aae4096 | -8.04096 | -70.09709 | 2025-08-30 06:27:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69ac4e3a-3f16-3fed-a06c-97be9cb37f57 | -9.06762 | -65.44749 | 2025-08-30 06:27:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 87f18500-33aa-379c-886a-965943e76c6b | -8.95713 | -65.96302 | 2025-08-30 06:27:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fad7e80a-f808-3033-9343-864200ef9fba | -8.55696 | -63.01892 | 2025-08-30 06:27:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c0abb51-b77d-3a04-8e07-4658c2f23eed | -9.07205 | -65.44916 | 2025-08-30 06:27:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 97cac15e-f400-362e-b1ef-74fcff2b0546 | -7.9968 | -70.28411 | 2025-08-30 06:27:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7676a24b-d857-3339-8819-df513ba4193d | -6.56421 | -69.95718 | 2025-08-30 06:27:00 | NPP-375D | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 048326a4-189e-3454-beda-7d29ecd6744d | -8.55264 | -63.02666 | 2025-08-30 06:27:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9e8daf4a-adc5-3fca-a953-f00fc639022a | -9.0689 | -65.43768 | 2025-08-30 06:27:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b9a27e38-9c52-3fc5-b2d7-ebb5b9b836dc | -7.35447 | -70.12421 | 2025-08-30 06:27:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cfc2519d-eee0-3e61-a5bc-df7e9f2f4d39 | -9.07266 | -65.44423 | 2025-08-30 06:27:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b4dd5f41-777f-3b0a-8116-8ac7e835eaac | -8.5498 | -63.01799 | 2025-08-30 06:27:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4e69947-75ae-3ef2-a138-9dfc0f5c4cfc | -8.65595 | -68.68721 | 2025-08-30 06:27:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a6daf8f-5eb6-3276-bda4-a9e3487a093a | -8.62693 | -67.24643 | 2025-08-30 06:27:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bbaf793a-4e69-394c-928d-8b9c4986b186 | -8.53262 | -64.0091 | 2025-08-30 06:27:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7fb03e6-3c9c-3ec3-b556-6a5f0a550f95 | -9.07449 | -65.4434 | 2025-08-30 06:27:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5652990b-8630-302e-8d33-79124d4b2457 | -7.99313 | -70.2855 | 2025-08-30 06:27:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b7647d78-5111-3d8c-ad41-4af8e9b22a5b | -8.04158 | -70.09261 | 2025-08-30 06:27:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6845a83c-9447-36a9-ab4c-8c46334e39b5 | -8.56325 | -63.0269 | 2025-08-30 06:27:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c80bdf88-3c47-3253-bc55-d92c6c6a476e | -8.62743 | -67.24283 | 2025-08-30 06:27:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3882562-9aab-3c74-a029-4fd25a8b4985 | -8.4437 | -70.13928 | 2025-08-30 06:27:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c931b79-2c46-3fb0-b34a-0a12525db202 | -9.06698 | -65.45239 | 2025-08-30 06:27:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1b6b3168-a00d-3222-9914-fe905ec0cacb | -12.42308 | -63.91398 | 2025-08-30 06:29:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c95c69c9-a192-3fbf-a3b0-b67ee86f3a46 | -12.43265 | -63.91964 | 2025-08-30 06:29:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0d1d4bb-bf31-3120-a922-493487286097 | -12.42554 | -63.91889 | 2025-08-30 06:29:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0e2a15f-928b-33ae-ac6f-50bb8184b774 | -12.42944 | -63.92175 | 2025-08-30 06:29:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e20376cb-df4a-3769-b003-91aeada03856 | -12.43655 | -63.92252 | 2025-08-30 06:29:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc50d8ad-32f4-3b03-b9ba-37b763ec2d54 | -12.43019 | -63.91478 | 2025-08-30 06:29:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 574c72a2-537d-30af-9bf2-c396362ca7d3 | -12.42633 | -63.91194 | 2025-08-30 06:29:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc0e534e-a317-3976-9b95-eb12ba7717a0 | -8.92559 | -72.8222 | 2025-08-30 06:29:00 | NPP-375D | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README87.md)
