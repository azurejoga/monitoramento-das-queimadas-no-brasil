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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4b5b050-13ad-3225-a187-251075042f44 | -11.7028 | -54.60332 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9328194b-2d8a-39d7-8ee2-880f2a801d02 | -7.3772 | -55.49208 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2420850b-6a26-304c-ade8-492dc0204780 | -11.81264 | -44.8067 | 2026-08-17 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 6e2b2b5f-84ad-3607-b41c-35d1c1dfe096 | -10.4726 | -50.3726 | 2026-08-17 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 615169eb-d011-3599-b004-31bc54817813 | -7.91049 | -48.52791 | 2026-08-17 04:21:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 01a2ec0c-e7b5-39e8-8000-51e7caf4d0a3 | -14.18958 | -53.06173 | 2026-08-17 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5646a380-8c4b-3d05-8ab8-69fc43584cf4 | -11.14099 | -46.53304 | 2026-08-17 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24829291-4ad9-3615-aeb4-4624d85ea6f4 | -12.6709 | -48.51686 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 2ce81180-958f-384c-8c3b-1b04a9d52dfd | -14.49307 | -45.67823 | 2026-08-17 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3250d5a-3dd6-3087-b904-26eac9d2c237 | -12.69101 | -48.52443 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ac2442e6-361a-39cf-b365-21c0c2399def | -7.39098 | -55.48174 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 060ec16f-d97d-3d89-8e5d-21dc097caff1 | -11.70615 | -54.61333 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffaae195-231c-3cd3-9159-bb43f54fd6f1 | -11.47423 | -46.5765 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7adeb486-f0bf-37d1-a95d-28a8d5e61ecb | -11.39374 | -46.39732 | 2026-08-17 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b894ef0-b04d-3017-9513-c2ab1f91f3f8 | -11.7118 | -54.61118 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b2be830-35de-3a95-bb55-12416e41fa6a | -14.88975 | -46.63235 | 2026-08-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c5bf569-eb9c-39e4-aafa-6dc64e6f9c6a | -11.48419 | -46.57809 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3a5e829f-50da-341e-bce3-db43fd9deb1b | -11.10321 | -47.27615 | 2026-08-17 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0dd7e70d-0f5d-3a35-8322-1b047b84f00c | -11.83545 | -51.7723 | 2026-08-17 04:21:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 64c06fc1-3ee9-3c80-8989-5316538374fe | -11.41402 | -43.97817 | 2026-08-17 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 997082ac-b04f-3632-acda-d9c7ce4dc891 | -10.60595 | -48.37872 | 2026-08-17 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d1ca2b4-6a53-3564-9227-abddfc7ed58b | -8.59851 | -54.69835 | 2026-08-17 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb24655f-5435-34fa-a8be-32fa8d9850dd | -8.7358 | -45.28207 | 2026-08-17 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72ec3812-87ce-347f-9358-719a6c35643b | -14.47251 | -45.67863 | 2026-08-17 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac8b3d25-a7fe-38fb-a2ea-9200282cb89b | -6.12852 | -57.73249 | 2026-08-17 04:21:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2e3c3988-4685-3b5e-a2e8-ad48feaebbb5 | -13.69962 | -46.26319 | 2026-08-17 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90dd1a82-80fb-3a95-98b4-d43ec2171bd1 | -12.24488 | -43.14269 | 2026-08-17 04:21:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d93a3053-1e48-399f-8114-54d34f638804 | -11.79012 | -51.78424 | 2026-08-17 04:21:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6d074073-ff48-35c0-87e2-26d85412aa77 | -15.09395 | -48.7211 | 2026-08-17 04:21:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 582aa936-525b-3963-8c3e-a516364af4e9 | -14.51026 | -53.02074 | 2026-08-17 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 46d9514c-9163-3e18-8244-83a281546b78 | -7.37646 | -55.49623 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7a6a5b86-1f90-37c4-b2d3-1f1ef62228fe | -11.31965 | -46.3055 | 2026-08-17 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c6d6a2ec-c78a-306c-9704-bec4c6d5559f | -14.45264 | -51.83931 | 2026-08-17 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 46963bc0-784d-3094-91b1-0945edbe8367 | -14.73281 | -47.96413 | 2026-08-17 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1af8d501-68aa-316e-82e1-80a2e6ac4dc7 | -11.49634 | -46.58729 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c14bced4-7053-3047-b458-b5a14156f57b | -13.4436 | -43.84432 | 2026-08-17 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 0c3e7bb7-41ef-3704-9787-dfb7faa050a8 | -14.49585 | -45.68237 | 2026-08-17 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 34749f10-f0d8-356b-9d13-45b9b94a0d4e | -11.09511 | -47.30475 | 2026-08-17 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25296717-5e74-389c-bf02-766586449d92 | -10.15807 | -44.01055 | 2026-08-17 04:21:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b912003c-74cf-312e-af66-8a4b35f7288a | -15.60496 | -47.87263 | 2026-08-17 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb196145-587e-36f4-8e28-2d7bfd29b550 | -8.59913 | -54.6949 | 2026-08-17 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f6ff49a-7d89-36f8-bc9d-ca183282758f | -11.10085 | -47.29071 | 2026-08-17 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7223b176-45b0-3264-9c18-9e749d899849 | -9.55908 | -45.36726 | 2026-08-17 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54e7df5a-1a4f-3c52-adda-fd8e5577e5b5 | -11.9951 | -46.4233 | 2026-08-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c641c94-b465-32ef-8e80-68eb49dc9120 | -12.7526 | -48.43026 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7cb41fe6-b419-3224-a00b-2008157b0599 | -14.47973 | -45.67609 | 2026-08-17 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c2c04b3a-a94b-376d-93b0-399342cd86e4 | -6.10301 | -57.73175 | 2026-08-17 04:21:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 01ebf48f-06bb-3950-a9c6-ae6bed10fa32 | -12.24207 | -47.03088 | 2026-08-17 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90b9b77e-c10c-390f-9a2c-3bcba091aff8 | -11.70223 | -54.60635 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb01bbad-d3d0-345d-9247-e77a92e8d111 | -7.53426 | -55.58331 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01ee2bd8-2524-3858-83d0-5c25a0c35575 | -12.65899 | -48.50282 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8203ac17-0e66-3fb7-92c1-e7beb11ac2ad | -14.407 | -51.83857 | 2026-08-17 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60d451cd-9985-3067-8d09-f44ca592e6f9 | -11.48751 | -46.57861 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83dbbee1-9dcb-3747-b5ae-f36808c2e1f7 | -13.68914 | -46.24339 | 2026-08-17 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09521b4d-3cbf-3481-b7c2-4cae8e81784d | -14.30308 | -47.18518 | 2026-08-17 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9edc9797-6074-3d05-beb1-09c93077c874 | -11.9795 | -46.45636 | 2026-08-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5a36367-6ec1-3223-aec9-4c4233be75dc | -8.73532 | -45.3069 | 2026-08-17 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29c06854-8a33-3bee-a547-73069c8089c6 | -9.27324 | -45.64957 | 2026-08-17 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8f38f511-6112-33d3-92c9-a91131f24162 | -8.522 | -54.90386 | 2026-08-17 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5592cc9d-302c-3ce9-92ba-d420b63a5299 | -12.72964 | -48.46235 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f0f94c63-d44e-3b4c-a0ed-bffc1e5b3685 | -7.37794 | -55.48796 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3c7e6f13-20f4-39cc-857c-542aa54bfea1 | -11.45538 | -46.58802 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c0d9aa01-dd16-379a-b918-8a14ae9b7544 | -15.12386 | -48.17491 | 2026-08-17 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48fa77bc-38cd-397e-9518-56cd0a9e40e5 | -9.30113 | -56.81321 | 2026-08-17 04:21:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1321057f-85db-379b-b723-0c17e54e62c0 | -10.3877 | -48.2667 | 2026-08-17 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26fcce6e-2c55-32df-b382-53d0eaacd090 | -11.7073 | -54.60725 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a4f5ef5-12cc-3e2d-b86d-e7fc2c32da67 | -8.58364 | -54.68837 | 2026-08-17 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| dc9053d2-3a5c-3ad7-8039-4b6482b31b8e | -12.00941 | -46.46173 | 2026-08-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9af4dda6-b215-3314-acbf-047d38f89de3 | -13.51551 | -46.24455 | 2026-08-17 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 292b5ae9-1750-3d58-bcf7-3bfd7e257c6f | -6.12439 | -57.7295 | 2026-08-17 04:21:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3c3ad55c-2fcd-353d-906d-2209fa1c6f41 | -12.71605 | -48.48027 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cb380011-33f8-3752-b7b4-3b21350fe62a | -12.56191 | -47.87551 | 2026-08-17 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 459d4280-c8e5-3beb-859d-6467f58e1860 | -7.40251 | -55.48666 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7885c020-0e67-36d6-bcc3-b8473185dd96 | -12.00061 | -46.43141 | 2026-08-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 957183d8-b7a7-35e9-bfbc-453f0ce33d6c | -11.24 | -54.01454 | 2026-08-17 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5c7a300-6952-3d3d-bdf1-5c33632e8ef2 | -11.3965 | -46.40136 | 2026-08-17 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 306aaf59-ef21-3561-b687-3e12d217b2c1 | -13.78635 | -53.80462 | 2026-08-17 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a33a40f5-36d2-3723-b443-f5489ed71604 | -8.5253 | -54.91664 | 2026-08-17 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f8f9546b-8727-32ed-a27b-ae25b6cd80fb | -14.44154 | -51.97393 | 2026-08-17 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c31f4e27-601a-3a26-8831-1205ab326730 | -7.38057 | -55.50829 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc1b0800-5376-38d3-bf2f-4644a4b1e8fc | -14.42341 | -53.17181 | 2026-08-17 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 53480ce2-aa77-3495-92d0-ea124316606c | -14.4691 | -52.0761 | 2026-08-17 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6c3a17fc-ccd0-3188-a4ee-869b8995adb3 | -11.09984 | -47.2756 | 2026-08-17 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf99ee9a-4017-366a-ad2b-a96d40a447cf | -11.71237 | -54.60817 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2190e304-79bc-3ed0-aac7-00ac6149a7a8 | -14.87045 | -46.64735 | 2026-08-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| eb7f1fea-2ca5-35b3-bc72-451533bb8e62 | -8.08688 | -46.89448 | 2026-08-17 04:21:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b63b70e-3350-387a-bea9-8ae096a4e7ae | -15.16968 | -48.66711 | 2026-08-17 04:21:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3ccb0e6-9e1c-3574-96e3-d9d0f087db57 | -12.70962 | -48.51949 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9a427dfa-2f86-39a2-be39-8ab476f64c13 | -10.46395 | -46.29675 | 2026-08-17 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0e642b5-a203-3820-9eb3-22bb23a5c619 | -10.47317 | -50.36959 | 2026-08-17 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7b769bf-9a03-3df6-955a-266e07a0c432 | -12.03866 | -46.49172 | 2026-08-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 192ba614-53cb-3cc0-a408-bd6875670a04 | -15.16526 | -50.08115 | 2026-08-17 04:21:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a211e20-e5e4-3f95-9395-ba5e61729d50 | -11.72137 | -54.61612 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6432d04-263c-31aa-b5d6-c0bbe4ce4471 | -7.36342 | -55.50232 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24f30d88-90b4-307b-955c-f54fe5f95fd2 | -13.4401 | -43.84374 | 2026-08-17 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 6188e242-4651-3269-99f0-ede27c6b954c | -8.50479 | -47.22321 | 2026-08-17 04:21:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b48e09b-23c9-3299-a172-c8d9aa5271da | -14.49029 | -45.67408 | 2026-08-17 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76bdfbd6-22f8-310f-8583-1111cda88f65 | -8.5246 | -54.92045 | 2026-08-17 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6f77f138-ba23-3a9f-9954-05df39ab6d15 | -7.38952 | -55.48993 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e36dcea1-011a-38c8-b2cc-c0b137b9ce52 | -11.14215 | -46.50423 | 2026-08-17 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README22.md)
