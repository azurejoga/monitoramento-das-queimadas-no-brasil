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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6e8c54a-7c46-3251-9109-3d42b4491982 | -14.57198 | -48.33025 | 2025-10-03 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7e4d6469-804e-38b5-8fd1-8850b587edd5 | -12.11442 | -43.4411 | 2025-10-03 04:12:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e80b4bd4-f57e-3751-8ed4-7e69251b457e | -12.60658 | -46.9795 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c53d523a-cc2d-3e3a-a2be-b81d462c4a79 | -11.90413 | -46.3002 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a83fcb9a-739c-31b0-984e-889909fc2a41 | -11.80296 | -45.00525 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed2efd96-65f7-3e0c-ad1b-5a82c1930a08 | -11.12065 | -43.39167 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cc249c90-b135-3c7f-b7ec-4a47b9fa5aa1 | -11.42966 | -43.48967 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5cbae905-f1a5-37f2-b039-8abc9b15541c | -13.29042 | -46.98527 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6edd597-1b5e-3b97-b860-feea3c438160 | -11.85013 | -44.95749 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0b90e59e-63b4-3c87-be9d-9a2f8835cdb6 | -11.80513 | -45.01362 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf82b4f5-a512-35df-9b50-c46e0db18e3f | -12.71223 | -48.57847 | 2025-10-03 04:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 62e9bb7c-481e-3b04-a528-6f84e9b5f8e3 | -14.30538 | -47.11573 | 2025-10-03 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 14bdeccf-c9d4-3179-a53c-ded20ae22bc2 | -12.90397 | -46.93945 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e4d1c7b3-12fe-323d-b592-769fbe57ba8c | -10.91068 | -47.04445 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 48a04a2f-db1f-3f56-8538-015721bc16dd | -14.18836 | -46.69105 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17421617-097b-3529-8436-70194827fbdc | -10.86399 | -45.41054 | 2025-10-03 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6fb6b06-9532-3b58-a1ad-8f5fb64b9ec5 | -12.93371 | -48.43526 | 2025-10-03 04:12:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5c6e5172-82c4-3899-9b08-7391c0f0327a | -14.40375 | -46.16851 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29c7dd94-15f7-38bd-a7d4-18c6e1297cc6 | -13.22639 | -46.43844 | 2025-10-03 04:12:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac86cd7c-285f-347d-bb80-ef3362259a8f | -13.05324 | -47.06045 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3126360b-c5ae-31bd-80f6-b0fe7bcb4622 | -8.73405 | -47.34846 | 2025-10-03 04:12:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11cedd82-561f-328d-9975-d0bfaff0bb8d | -11.32322 | -49.01987 | 2025-10-03 04:12:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e458ae0-ffd2-3a3e-834a-61aec2dca536 | -13.63451 | -48.67252 | 2025-10-03 04:12:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 35919456-34b5-34ff-a57c-c74c420ca464 | -12.37891 | -46.52415 | 2025-10-03 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f47c676f-acdd-3ecc-a907-1755913f1194 | -12.85682 | -47.01051 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04d42630-6c6d-3a8b-92e9-f9b4dd4b26b7 | -14.09773 | -45.64614 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fdb546a1-c888-303f-94af-0015f3f9a3c1 | -13.2026 | -47.3373 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dba7565e-6376-342b-85f7-f9b67678204c | -13.96595 | -48.17245 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 1a0742df-834e-38de-be72-c1bf0bf46485 | -13.24077 | -48.49818 | 2025-10-03 04:12:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aed2b65b-fef9-37d1-ae67-8f4079be07ab | -11.83162 | -45.02601 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 791ee97a-ccfd-3c90-8474-d11f11da7ba9 | -11.64122 | -45.06221 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8bd3f4b8-4c3a-3464-b3d9-af6412d1a1c7 | -9.07821 | -48.02766 | 2025-10-03 04:12:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c701e25e-aa65-3a04-9d59-9640b314c00f | -11.6797 | -47.49326 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| efe29916-47d0-355a-b9bd-d17ff05e66d4 | -10.96325 | -44.33881 | 2025-10-03 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7769057d-4609-30cc-a017-4e51cfbfc56e | -11.05797 | -47.79317 | 2025-10-03 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec56153b-cd4f-3ad2-ad1d-67c2979f9438 | -9.04109 | -46.67526 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eb187c11-ec0f-3f09-9ca7-3137f2578a4f | -12.67837 | -46.8542 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff1251ac-c372-352a-8b17-2211f8d781ad | -14.44017 | -46.11877 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ed75418-0131-3978-b1be-67ce56a31dd6 | -14.43519 | -46.10528 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c5995fe-69b4-3280-be5f-d2add1870f02 | -12.76784 | -50.53098 | 2025-10-03 04:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4bdbc026-ed9a-37d9-8654-f7b76916aefb | -13.20239 | -47.89032 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e97fb90-ae87-393a-ab5c-efa9fa6b59b9 | -14.79075 | -42.82959 | 2025-10-03 04:12:00 | NPP-375D | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5bf06b04-7c40-3e34-af6c-1aeabf5ea44c | -11.59678 | -42.87056 | 2025-10-03 04:12:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 57fa404b-9404-3d35-9af6-5f0239ae2581 | -9.95219 | -43.70279 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f7ff95f-3e95-31e8-9a20-1ae1af974cf0 | -12.9943 | -47.7501 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c103b9c-d30c-39bd-8089-b95b2e065cd9 | -8.12848 | -50.23388 | 2025-10-03 04:12:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4fd0abb3-9037-3aa0-bdee-998719e93c73 | -11.57955 | -47.66821 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2a17caf2-0588-31c0-a064-ee3658826664 | -11.4826 | -43.5021 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef4d5f16-c1ef-31e2-ac3d-551ab4ace597 | -10.92471 | -46.72803 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| a1eb0777-92a7-363c-af94-6476a21753e7 | -9.90195 | -43.72798 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3abeb1f7-e520-3942-bfc3-4e8d17aa0f55 | -11.88144 | -45.02703 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0fd4fb9-70f2-39bc-8d42-b2ff7d0a08ce | -13.05245 | -47.06509 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2eb9419d-c4ba-36c1-841d-54f0700695ed | -14.36042 | -46.14403 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b0a9772c-1811-3bec-b76a-a8d567a59a9f | -11.49513 | -45.01052 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 69e16d2d-c4de-3156-b7cd-561b476e88a9 | -10.85381 | -45.39392 | 2025-10-03 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a79cc4db-6ef9-3b1f-a028-2b87b0fa2c3c | -11.83444 | -45.03053 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 93f9a2b0-bfba-3666-8e04-13738e7a4289 | -13.75632 | -48.06509 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0fa51dff-ae77-38b2-b87d-f70aabedee06 | -13.75858 | -48.08569 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 672e832e-3d27-33d2-a8ba-83b79388f25d | -8.80606 | -46.67028 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c3aa32aa-5ee5-3ce6-b0dd-8047f0b00069 | -13.29792 | -46.98653 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6418b8fc-b922-38be-a4a2-971ec5be15f9 | -14.43872 | -46.10594 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c93df8d3-3c38-372d-b507-4d2e1c3d9445 | -13.56767 | -43.5744 | 2025-10-03 04:12:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2a212ba0-db1a-3985-b047-9451a1fac66b | -13.31001 | -47.25325 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cee035bb-0830-361e-8043-16504d4e045c | -8.76343 | -49.92376 | 2025-10-03 04:12:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd500cfc-fda0-3dc1-b6fc-03f748f55ae7 | -11.86207 | -44.97144 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79afe574-0479-3a09-aef5-e3b61e8e8b17 | -12.24568 | -47.83302 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 13143c02-a435-300e-b99a-0d64d59e79f2 | -11.61432 | -45.03015 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 003bf149-cc29-3c65-b491-4a8e40b3e0b2 | -8.61583 | -54.97092 | 2025-10-03 04:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 17dd7bf6-3f37-3ba3-a4d5-01f5c853cc57 | -11.47457 | -44.97606 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5423a3d3-b701-33e5-b2f2-359329d0ce54 | -11.25717 | -47.7961 | 2025-10-03 04:12:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 870328d7-ba1e-3d8f-9193-af24c500524b | -13.57716 | -47.27844 | 2025-10-03 04:12:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a6fe21d-cc0a-342c-ae70-c10d3da5cfdc | -12.93168 | -48.43504 | 2025-10-03 04:12:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce208849-1bf5-3303-9d74-890cf09f731e | -11.11279 | -43.19061 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0a20bed-89e3-373b-b631-e3edfb8700da | -11.49925 | -45.00724 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fe7d5ad8-9141-3b33-b810-5d3a58501a64 | -8.72099 | -47.137 | 2025-10-03 04:12:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1fd18d6-2831-39ce-a4d1-cd06f8fd3b5f | -10.9239 | -46.73275 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 669a47a0-bb2a-3ac0-8b13-5e9f15213ec6 | -11.77364 | -46.82946 | 2025-10-03 04:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e530676-57f3-3f3b-854c-6f7b4f0928b6 | -12.86295 | -46.99726 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b591ad12-0e5b-393e-a6d1-e591d1d49d05 | -13.23979 | -47.30424 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4313fa0-b041-310f-bd75-8eb79e0f4af7 | -12.11832 | -43.43812 | 2025-10-03 04:12:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1b1ab7d1-e261-3b6e-a73a-fbc4376f31f6 | -13.26897 | -47.24159 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d0f973c8-a23e-3928-b36c-cd66dd8f8a6e | -11.46555 | -45.03741 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6fb14066-3c52-31f0-85e7-9533af26fc53 | -11.09923 | -47.81552 | 2025-10-03 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41e943ee-fbb9-3118-90b7-1e654758e0ad | -8.64846 | -47.71803 | 2025-10-03 04:12:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 638c4c17-6494-3c9c-b0ae-79e8b75cc944 | -10.0625 | -48.18623 | 2025-10-03 04:12:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b43a990-13e8-33d6-a59c-56857e776ccd | -13.97596 | -48.12756 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 25820008-fedd-3e4d-a2f4-5367a68ebb2e | -10.96044 | -44.33451 | 2025-10-03 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4cf3003b-dc4d-3087-a25f-f2ad09f5c860 | -13.31319 | -47.57785 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2d20ab7a-7cad-33f4-9886-2bccef38a8d4 | -11.85458 | -45.03831 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb5562a9-6638-31d6-931f-8c7f5235f60d | -11.32063 | -49.01263 | 2025-10-03 04:12:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1dccab41-d3ec-3583-a243-70d1d97f0019 | -13.7595 | -48.08036 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| b025f5c8-ab8b-3ab4-9017-431730d1d9c6 | -11.20146 | -54.0899 | 2025-10-03 04:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7bb9e0c-7d79-3c87-8526-dfb01958b333 | -10.28245 | -44.33187 | 2025-10-03 04:12:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c79ba6d6-8b49-391e-8127-60a21517bae5 | -9.90872 | -43.72908 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 7f0a3988-826f-3f41-a6fa-c67345ca7548 | -11.91079 | -46.28354 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8579619e-cb3f-3579-b25d-ffa6cce5504b | -12.22717 | -43.76678 | 2025-10-03 04:12:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c45a27c9-b0a7-3ea4-a2f9-1f662ecc80d5 | -11.14298 | -43.38081 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a41928ca-4e8c-312f-bcb8-3b83da15c63b | -13.33223 | -48.12516 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4fd515fd-360c-3452-a688-74122339c010 | -13.34419 | -48.12756 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 69ba5309-64bc-3777-9933-ab48d3bd73f7 | -14.37743 | -48.47967 | 2025-10-03 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |


[Clique aqui para ver as próximas entradas](README66.md)
