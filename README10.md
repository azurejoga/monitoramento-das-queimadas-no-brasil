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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75a66f0f-3a6f-3cbe-b40f-3674de58ae2f | -9.9373 | -60.424198 | 2026-08-29 00:52:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3377ded2-0229-3286-9310-10687d76c3fc | -6.7742 | -55.678299 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 517c0b6c-ff3e-3e6c-9e31-1647f6c7f9d6 | -6.8238 | -59.948002 | 2026-08-29 00:52:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fb54f9bf-17db-399e-9cc3-1b231399adec | -10.4957 | -64.487999 | 2026-08-29 00:52:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 308ec1b8-d687-334f-b669-baf35a194ffb | -8.9404 | -50.8064 | 2026-08-29 00:52:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8e38b7c-1dc4-3be0-887f-13b7111a6675 | -10.7425 | -54.0341 | 2026-08-29 00:52:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 225ff68d-07b8-3ce3-ab70-ff98ad706e19 | -9.9291 | -60.433399 | 2026-08-29 00:52:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 68951fe0-8af3-3ed0-88a7-027d104d16c9 | -6.1634 | -57.783199 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 777ac5b4-59ea-3342-8449-6ccc8df456a8 | -9.926 | -60.419399 | 2026-08-29 00:52:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 58a902b0-8f45-3966-9990-bfd329825e1a | -6.7349 | -55.4692 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae1a2811-ce55-371b-a225-c0e283291f45 | -9.1813 | -56.969601 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55b689a5-e92a-355e-b41e-fe9e0411e8fb | -5.997 | -57.821499 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3db4231-f68a-397e-9759-4c8bcb9b830c | -10.5686 | -59.609001 | 2026-08-29 00:52:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 92a3f7af-463c-3308-9bb0-3f8fb5404081 | -7.5891 | -61.338501 | 2026-08-29 00:52:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 07ae30ac-c9bc-31fd-bacb-b151c2a9f5ca | -3.9307 | -59.324699 | 2026-08-29 00:52:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 62fae8ab-0bb9-3a5e-b606-8b28c925e429 | -8.1596 | -63.988701 | 2026-08-29 00:52:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6d0c3178-89da-3138-a85c-44edecbb53a3 | -20.9491 | -57.5942 | 2026-08-29 00:52:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1864f55f-1195-3652-a86a-6931fefe55cc | -14.9487 | -56.2971 | 2026-08-29 00:52:00 | METOP-B | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3daa8b8a-11e5-3529-b21a-25624668f237 | -8.5327 | -55.269501 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76fc444f-89de-33df-9ab1-4fa431d0e000 | -6.7712 | -63.031101 | 2026-08-29 00:52:00 | METOP-B | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9cd47875-6489-3e91-9978-96099986d400 | -8.5303 | -55.259201 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 229b4af6-cefe-39a5-84c0-da211aafa77e | -6.9138 | -59.481899 | 2026-08-29 00:52:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f30dc921-1e8c-3e83-998f-d2e754c8378a | -6.7648 | -63.048901 | 2026-08-29 00:52:00 | METOP-B | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ed264d46-f18a-3c84-9c20-c6dca64752d4 | -11.0353 | -57.223099 | 2026-08-29 00:52:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 35f74f32-09ed-30f0-9fcf-6e453e7d6689 | -14.4629 | -58.5135 | 2026-08-29 00:52:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 00ae53b4-f4a3-3b16-beb5-535930e24bd2 | -11.2192 | -53.998699 | 2026-08-29 00:52:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0e789866-cb10-3918-b0a7-f9b533916b9c | -5.8727 | -57.774101 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60b2d767-7a37-33c6-ba92-dda14b7dbb2b | -2.7492 | -58.168301 | 2026-08-29 00:52:00 | METOP-B | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 60da4bbd-28f2-3c70-a8e0-8a2e0d7be799 | -7.4908 | -55.266998 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70d71071-0c36-325a-8787-e924e32898ad | -14.1647 | -52.824001 | 2026-08-29 00:52:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8e28514c-e48a-38cb-8dc6-fbf995e9a424 | -11.7107 | -54.535099 | 2026-08-29 00:52:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0d97a1f2-43d7-3b03-91f3-cf15765ac908 | -19.2328 | -57.647202 | 2026-08-29 00:52:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 60a5ebea-54b2-3172-85c2-99a52e7d78a0 | -20.933001 | -57.5672 | 2026-08-29 00:52:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6da0a4c2-2540-327a-94fc-bd3b7196b930 | -17.6194 | -51.613602 | 2026-08-29 00:52:00 | METOP-B | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 85eb1cdd-1ff7-3664-aacb-cf79716ebfe6 | -11.2053 | -51.2896 | 2026-08-29 00:52:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6cec7866-6389-3a58-a7da-f8b5484c2da0 | -10.7453 | -54.045399 | 2026-08-29 00:52:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1fcaaa87-5734-36b4-be8a-0555a15b94fe | -6.7669 | -55.647701 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b3557e7-2401-386c-ba29-b4f6b914f0b8 | -5.9989 | -57.829498 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 322fe72f-59ab-32cb-9fec-c2fad3f7d266 | -11.269 | -54.033699 | 2026-08-29 00:52:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0190c11a-58d4-33e2-af71-a83e835eefee | -19.226299 | -57.664001 | 2026-08-29 00:52:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 69b79756-7287-3b7c-838a-804e47f732d7 | -6.1102 | -57.820801 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e85a77a-be24-382f-a3a3-61174977e340 | -10.567 | -59.602001 | 2026-08-29 00:52:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 32eeaffa-9723-3fe7-a56b-e7028cf4a35c | -8.518 | -55.337502 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e4796d2-700c-3224-bccf-f75b63c9f1da | -6.8128 | -59.445801 | 2026-08-29 00:52:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c69bb98a-24ac-3f9c-a9e7-0234fef3980d | -6.8434 | -59.9436 | 2026-08-29 00:52:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 70a712a5-d6dc-3d98-8382-b22133c1fac9 | -20.9573 | -57.584499 | 2026-08-29 00:52:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8558faf4-0318-3220-9c19-f80de32dd4eb | -20.9636 | -57.613998 | 2026-08-29 00:52:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e25ea6f0-9436-322c-a228-ba74ea6e1bdf | -6.762 | -55.670399 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52a82dda-4d1e-3408-85bd-7c82003d7633 | -14.1901 | -52.842999 | 2026-08-29 00:52:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c71ccfed-1863-34aa-b520-8b4d4fb01c64 | -14.8994 | -52.617298 | 2026-08-29 00:52:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 11662371-4b2b-3788-9057-bf6627bbaf95 | -14.939 | -56.2995 | 2026-08-29 00:52:00 | METOP-B | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7c606342-8146-3ee6-b424-bb51f1e702bf | -8.9558 | -63.261002 | 2026-08-29 00:52:00 | METOP-B | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3f7b1611-469b-3b8e-91c0-ca7e80aeb4e5 | -14.1804 | -52.845501 | 2026-08-29 00:52:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0807c520-3195-3c90-bead-3898aba30203 | -9.2566 | -57.0714 | 2026-08-29 00:52:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b84af5b9-7007-3b16-8ceb-8716edcdba11 | -14.1453 | -52.829102 | 2026-08-29 00:52:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fb154c06-7a1d-3c2a-b3b1-553a54163fe4 | -8.5204 | -55.347698 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d6c6fdb-ddbc-3477-9c7f-2a104136186b | -20.9526 | -57.5625 | 2026-08-29 00:52:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7fcc5f96-22a3-323a-91d8-6ce479e0be15 | -20.9475 | -57.586899 | 2026-08-29 00:52:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 711590b2-17c8-3498-af56-35a537aae8ba | -8.9354 | -50.786499 | 2026-08-29 00:52:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 947bfd55-a667-3e38-864b-345aed10f385 | -13.4781 | -57.033699 | 2026-08-29 00:52:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5b678d39-ab14-3b94-a363-4e5ff16606af | -3.9405 | -59.322498 | 2026-08-29 00:52:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3e493de2-07c3-3fc4-9595-5775487353e9 | -20.934601 | -57.574501 | 2026-08-29 00:52:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bb5e344e-362e-3d2d-ae1a-c89e6a482147 | -10.0799 | -62.292702 | 2026-08-29 00:52:00 | METOP-B | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 88a91589-4c75-3a69-ac91-4ccf25a3027c | -6.7766 | -55.688499 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06a86338-958c-3f95-a8d1-e9de0c6876f7 | 3.287 | -60.6008 | 2026-08-29 00:52:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b115145a-0164-36cf-932e-59340ee52da7 | -6.7729 | -63.038898 | 2026-08-29 00:52:00 | METOP-B | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2e3d9b86-498f-3498-8a08-2351611671dc | -20.9412 | -57.5574 | 2026-08-29 00:52:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ee360f47-37a0-3536-bdd8-2939a9d08e20 | -4.053 | -56.281898 | 2026-08-29 00:52:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0576146b-7be2-3777-b51d-d1a0320111f6 | -9.3051 | -56.793098 | 2026-08-29 00:52:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 26939643-9004-3483-93bc-1e01182784f1 | -9.867 | -60.2934 | 2026-08-29 00:52:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4090758d-1c38-35c5-9bb7-492741de7d07 | -4.3037 | -59.4688 | 2026-08-29 00:52:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5d646065-6aba-3ff6-a1b5-83f1844dcd4e | -8.597 | -54.7621 | 2026-08-29 00:52:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8f63648-4e75-3af7-ac5c-367c007706b8 | -20.920099 | -57.554901 | 2026-08-29 00:52:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1aa7da5c-1f67-322a-b62d-47668c1053fb | -6.1573 | -57.801498 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a94ddf6d-394a-3c15-a545-a4ab6d5246b6 | -9.8753 | -60.284199 | 2026-08-29 00:52:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9bc1ec3e-f854-38e6-a396-df38c68e9371 | -6.1554 | -57.793499 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 263f5f39-1c97-34c6-8144-8281a4c0e87b | -6.7499 | -55.662498 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fae12bb-18d5-3a6a-a542-1b4f9548bfe0 | -8.5827 | -54.7887 | 2026-08-29 00:52:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d27cc91-6822-307a-b0a0-18a1d8fe1b6f | -5.9946 | -57.677898 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3aeb3be-098b-33e7-8431-cd9e84f87578 | -5.8806 | -57.763699 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8fabd7e-0124-3fcf-84d1-35ace9da92c0 | -6.7654 | -59.463902 | 2026-08-29 00:52:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1e5d1125-0451-37b5-a93a-783d0390376e | -8.2305 | -54.954102 | 2026-08-29 00:52:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79bdd9f0-1b64-3b6b-919e-ba50343ad2ed | -9.9645 | -53.933201 | 2026-08-29 00:52:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 187cfa3e-d598-3a4e-89e8-621961826bf7 | -5.9811 | -57.663898 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2e6d27d-96e1-3d43-b496-2f8ab8b4b3ff | -22.027599 | -56.027302 | 2026-08-29 00:52:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e891558a-243a-3934-bee2-457c202d7be8 | -3.9422 | -59.3298 | 2026-08-29 00:52:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4e0006d0-2e2a-3e1d-8a4f-03a5e70ea702 | -9.8655 | -60.2864 | 2026-08-29 00:52:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 47aa23d7-1a18-395d-bdda-520aa4b2e7ae | -14.2723 | -57.0327 | 2026-08-29 00:52:00 | METOP-B | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9836cf64-76ba-3efe-8731-1e1913733091 | -7.5031 | -55.275299 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bec183a6-79b2-327b-92e4-88e1d2eaf757 | -11.2261 | -53.985001 | 2026-08-29 00:52:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 737cc600-21cb-3f3f-a0a7-5a1fda9c5bf0 | -6.7694 | -55.657902 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d31ac96-f02c-3753-8557-7e820251dace | -6.1615 | -57.7752 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa4a0766-58c8-389d-b634-415af3474fee | -6.1713 | -57.772999 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15c2b1b7-3aca-3cd5-8b11-7b0c0ee7971b | -5.8847 | -57.737301 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ca71d90-ce43-3abe-8d79-ef4fad6b9b4e | -11.6985 | -54.527199 | 2026-08-29 00:52:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ad3a6ee5-e706-3abe-be8f-bada9ca4280e | -6.3279 | -57.7369 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b03d61b-e239-31d1-947c-7f9a41aa9cff | -6.8864 | -59.407001 | 2026-08-29 00:52:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 40ae1e87-1fe6-3fe2-80fe-b53fbb1c6b96 | -4.3379 | -55.432098 | 2026-08-29 00:52:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f7359a0-497c-3d39-9c3b-fed0ffd8963b | -7.3531 | -55.164799 | 2026-08-29 00:52:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89b2e2b0-d573-34bb-bdf2-90d7f60baa35 | -6.9346 | -58.940399 | 2026-08-29 00:52:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README11.md)
