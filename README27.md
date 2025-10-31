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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88d02daa-91f6-3f31-bea5-9424cd5e6a91 | -8.55593 | -40.7404 | 2025-10-31 04:08:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f7f4c4bf-e0cc-35ac-92cd-ee2e90e2ee55 | -12.69334 | -45.11524 | 2025-10-31 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a27b185f-03c2-3e96-8628-606065f1f196 | -12.28603 | -48.064 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a1e7f519-d802-37ca-b46b-58c490a8c073 | -9.42103 | -46.89194 | 2025-10-31 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7de8e6bf-3c76-3a9c-b811-b006808c6c1a | -13.41216 | -54.35828 | 2025-10-31 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e7d20ac-f347-3882-a818-f2f1ff8287de | -10.72197 | -46.2628 | 2025-10-31 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f7fe5c4-aa91-3688-a869-14d83bbfc145 | -13.68355 | -44.73254 | 2025-10-31 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 383bc5a1-562e-371e-90f3-05962d15a07d | -8.47578 | -45.78237 | 2025-10-31 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66940e7f-fccc-3195-89ec-071d203f8524 | -10.88621 | -44.32261 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4282f370-9e3d-3695-90ac-c52bc53c676f | -13.65352 | -47.04733 | 2025-10-31 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 17aaf750-8650-3f2c-bdef-080e6207be32 | -12.10444 | -47.12395 | 2025-10-31 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ac45484-36a1-3cd8-92b1-8bf0ba349e95 | -7.95123 | -46.73313 | 2025-10-31 04:08:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9267601c-d447-3f7a-81ae-2bd162f84b4d | -9.21728 | -46.31592 | 2025-10-31 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c0fa87a-6f46-3157-89dd-ce85edd57a6b | -10.09337 | -36.19776 | 2025-10-31 04:08:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 23.9 |
| 5903f122-6f7f-339e-adf7-cbe42227c416 | -8.2095 | -42.85281 | 2025-10-31 04:08:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8295e28c-905e-3145-89e3-6deaa22027d4 | -11.56076 | -47.07531 | 2025-10-31 04:08:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 49.3 |
| a821b123-ac3a-3944-9a37-f3d46b0110aa | -10.95439 | -44.67984 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae0d51ff-e247-3061-9abc-56bab07b48f7 | -12.93861 | -47.92519 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5489c6d-69fc-3197-b061-ec083d487f09 | -11.4637 | -42.75667 | 2025-10-31 04:08:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2f4e2624-0905-3f7d-b043-15facc9e66ac | -7.66457 | -43.59214 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f6fc9f14-0d2b-3693-b113-19b0049489eb | -10.92676 | -44.76207 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f80fdd92-1848-3896-9c4f-0210da160f8c | -11.79276 | -44.59458 | 2025-10-31 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2507776a-43b3-37cd-8ea2-161c15668270 | -10.92634 | -44.16133 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4e4799b7-d66a-3365-bc59-eea2d32877d2 | -9.72709 | -48.03023 | 2025-10-31 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6debe0d-23c7-3377-9379-2ea3a54c51ba | -10.87757 | -44.22538 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0fa5659-6aa9-394e-8358-78f7ec7dce38 | -8.16494 | -45.50481 | 2025-10-31 04:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c23d913d-92e3-36f2-ad96-4eec6b57fba0 | -9.24502 | -45.54809 | 2025-10-31 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a7c4a41f-d7bd-33af-a682-16718518f56e | -13.88319 | -47.3374 | 2025-10-31 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d090f5c8-7e93-3bc7-898c-51da7c624c69 | -8.08308 | -45.14018 | 2025-10-31 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc0a6bba-9fe0-3c93-8b12-386add45b128 | -7.90881 | -45.71474 | 2025-10-31 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 05132a49-0413-37da-9e09-fa4f27f6658a | -8.55407 | -47.78254 | 2025-10-31 04:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a599ba5-ddac-3cd6-9f8d-56dc1c8a8fcd | -13.78209 | -44.36399 | 2025-10-31 04:08:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b37ac3d-e09a-3b0a-9cf2-8b09883dc1ca | -8.32831 | -47.93745 | 2025-10-31 04:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4566161f-34a1-393f-be68-f16afc994dd2 | -7.65093 | -43.5899 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 205bc9d5-3528-307d-8b4a-8c3974e51066 | -13.68755 | -44.72943 | 2025-10-31 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 787adff1-6f62-3f3d-aed6-8ee703bb96ba | -13.36784 | -42.26609 | 2025-10-31 04:08:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 47a822d1-9821-335a-b5f4-a8ec7ac5e3d9 | -11.64921 | -43.90859 | 2025-10-31 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea597845-e15d-37ff-94e2-4b1ceac8ec35 | -8.31409 | -45.3752 | 2025-10-31 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f6380794-ee8f-324b-ac39-bf219f6a849c | -11.01232 | -43.87416 | 2025-10-31 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0d6608a-21ed-36f5-83fe-153a4321d3c8 | -8.15684 | -45.46215 | 2025-10-31 04:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c705fa7-3574-3c2f-b6d5-d3763c69f5b3 | -9.85337 | -45.36087 | 2025-10-31 04:08:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7adfe64b-8c29-3f4c-a710-49b79739f80e | -7.44055 | -46.88737 | 2025-10-31 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 39cd0bb3-5c40-3c5c-b4e5-afb0049cea7e | -10.17662 | -47.64554 | 2025-10-31 04:08:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83736081-e0d9-324d-943b-eee42f626c68 | -10.88934 | -45.07822 | 2025-10-31 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0401f8d1-78f6-3760-a0fc-7d42deb34c02 | -7.80776 | -46.39127 | 2025-10-31 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 49723401-6126-359d-800e-3d02a59f0140 | -9.73199 | -48.02705 | 2025-10-31 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1e7714e-4143-3715-a886-375e044202ef | -10.86876 | -44.40828 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d94e4bef-8232-35f0-8e01-167aea6e9cba | -10.97737 | -44.77036 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c69e56a-c6cf-3743-ae9d-8d2eb4cc08b6 | -10.53665 | -45.04163 | 2025-10-31 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 068a708f-5a1c-3edd-9e2e-410ea7d6326c | -12.19038 | -47.00687 | 2025-10-31 04:08:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a478c2f6-da55-382c-a89b-7e41e13fe4b0 | -8.09327 | -45.14626 | 2025-10-31 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5eb6f57c-aff7-3d97-9f1b-fdfbc8882f03 | -7.65001 | -43.59368 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 3860bea0-a0e8-314b-a4fc-5b98d909f94e | -8.0838 | -45.13589 | 2025-10-31 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fa45b7cd-39ea-34de-925f-9a87a6eea790 | -11.65256 | -43.90915 | 2025-10-31 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05131bf8-1c26-353a-bd6e-2b3bf9c19062 | -13.54939 | -47.37338 | 2025-10-31 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 90353cc2-ebea-3437-8611-8dfc72ed49ef | -10.54348 | -44.78325 | 2025-10-31 04:08:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5cfeb0ff-3b62-34de-abce-f43ffc9b2586 | -10.8873 | -45.0731 | 2025-10-31 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e4eb59d-61de-3817-8510-5b431b0d5c1c | -8.14777 | -44.79572 | 2025-10-31 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c5f7d31-4a0f-334f-8c0d-c7ae234161df | -9.73131 | -48.03101 | 2025-10-31 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eec30c7a-653b-3176-9f18-260501f54b38 | -8.34388 | -46.15145 | 2025-10-31 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad667ca1-40c1-3681-ae57-8c0b0101bced | -9.52156 | -47.20303 | 2025-10-31 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d06df64-9511-3e6d-8e79-1c78d2357b59 | -12.15744 | -48.01102 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a040799-6ec2-3b07-9477-3f02a7dbbf03 | -7.37723 | -46.22352 | 2025-10-31 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 41af70af-c4be-3bed-a0af-54a6a310de9f | -10.87724 | -44.03564 | 2025-10-31 04:08:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08646fea-36fe-3252-a2ad-8822802b5910 | -12.28874 | -48.07242 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36ddf421-473c-3f34-a8a7-9db6727d6fd6 | -12.06334 | -47.33606 | 2025-10-31 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 70fed1f1-0e63-38ad-8317-fd417f3aaccd | -8.33067 | -47.93647 | 2025-10-31 04:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55c106c7-60d4-3a1f-94e7-234206d42155 | -11.7135 | -43.91562 | 2025-10-31 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c6508cd-4353-3267-a1f5-71871bfbf8c8 | -9.89184 | -47.45672 | 2025-10-31 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fbd4ce70-b917-3c5a-b766-b8a3e61eceec | -12.84237 | -43.46747 | 2025-10-31 04:08:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 411d8d45-594f-3554-86fa-e0453534b488 | -10.52704 | -53.71169 | 2025-10-31 04:08:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab3ed8d6-2931-397d-8b80-17a80281a5d6 | -12.84463 | -43.4533 | 2025-10-31 04:08:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 19011cf6-6e89-325d-ac7e-48faa5b6d206 | -10.09712 | -36.20251 | 2025-10-31 04:08:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 23.9 |
| a1eed5ac-8448-3614-8c43-ee8d317af336 | -11.44223 | -45.13802 | 2025-10-31 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ae1abcd-1d07-3689-a107-348300922cd3 | -7.30431 | -45.66255 | 2025-10-31 04:08:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60c33d8f-3edf-3274-8144-019c6ed5a83a | -11.05278 | -44.2925 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0167df0-16fd-30be-baf5-7ff40d6a1882 | -10.64034 | -45.24812 | 2025-10-31 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ffeed4df-be30-3282-a3f1-86b9ba074520 | -12.52992 | -47.54898 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7bbf74ef-c6ae-31b3-8842-cc9111ae4657 | -12.93737 | -47.93219 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9d285786-24cc-30ab-8af4-82d2e5a81358 | -8.06856 | -45.13771 | 2025-10-31 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b7a9aea3-2947-3c19-9f3b-b2f895794e56 | -8.17771 | -45.6896 | 2025-10-31 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be65fcf6-6599-392b-bddd-aebfd36e763c | -8.33106 | -45.38657 | 2025-10-31 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e5b7156-472d-3fa4-a45d-0c4c0be22f93 | -10.88999 | -45.07426 | 2025-10-31 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 275f109f-b37c-324a-b033-bf8fe5d06f88 | -12.28534 | -48.06791 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3156b6e-b034-32f9-b3d4-e00a00dd3042 | -7.93369 | -42.24066 | 2025-10-31 04:08:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cb6415bb-8ac1-3700-b67f-7757059ebe80 | -14.21006 | -44.38752 | 2025-10-31 04:08:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39f56bba-fd69-3b76-ad96-27f4dc9955ac | -14.65423 | -44.26881 | 2025-10-31 04:08:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee7b795f-41b2-3b09-ae40-bd165af4f64c | -7.95805 | -43.79261 | 2025-10-31 04:08:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b310b3c7-70bd-3e93-85f6-4e515619ff83 | -7.60707 | -46.48081 | 2025-10-31 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d76006e1-3d6a-357e-86b3-fe8ddd457950 | -13.67925 | -44.71654 | 2025-10-31 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a317790f-f756-3cee-a2b7-d15d5c647da1 | -8.95598 | -47.52237 | 2025-10-31 04:08:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| daa2eda0-51d5-3e15-924b-317fa4112abb | -8.51255 | -39.64512 | 2025-10-31 04:08:00 | NOAA-20 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6354c71e-b89a-3d63-a504-db3e8a649fef | -7.65995 | -43.599 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 1b0c51cc-1cce-32d3-b51b-fb937c796cdc | -12.49358 | -46.85277 | 2025-10-31 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e18cb8f4-fd7c-3c64-9b40-a13f572f2133 | -13.53289 | -47.43088 | 2025-10-31 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3cc47f20-9b6c-3baa-9470-928dfbaeafaf | -12.09886 | -47.13322 | 2025-10-31 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 57ef9334-189c-3573-abb6-ac4fccbf17bf | -10.63459 | -45.2388 | 2025-10-31 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45947831-3383-3fb6-bbad-6d47a0b10eea | -10.88663 | -45.07705 | 2025-10-31 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5e5edfc-f6a6-3f1e-b197-a9f87dd88e52 | -8.09992 | -45.1737 | 2025-10-31 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f213d1f1-2055-36e6-9e24-cf490aa190b1 | -14.21493 | -44.81105 | 2025-10-31 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README28.md)
