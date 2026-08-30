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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cdfcda5b-67d1-33eb-b84f-471ca7f8e21f | -12.9221 | -45.8582 | 2026-08-30 15:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 161.4 |
| 84ad6a43-d40c-3677-baeb-fd789446c96e | -10.9556 | -50.5311 | 2026-08-30 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 6a046be9-65f9-312b-bcb2-83559f246779 | -11.0627 | -47.1385 | 2026-08-30 15:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 7dcac751-8d62-3a28-aa27-23163993d910 | -11.6205 | -50.4575 | 2026-08-30 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| bae317e8-07bd-33b8-988d-4a3d28b6eb65 | -7.9169 | -61.3671 | 2026-08-30 15:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| dedc2bff-5293-334b-8f7f-876e7d8851d9 | -8.1534 | -45.4904 | 2026-08-30 15:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 20d4a0e8-9910-3922-8978-81051b6b2922 | -14.36 | -49.08 | 2026-08-30 15:15:00 | MSG-03 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4f33b1a5-e0ad-350a-97e1-5ffc14a27755 | -8.0 | -46.54 | 2026-08-30 15:15:00 | MSG-03 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4af4c5d4-2642-34c2-b612-16034b92874e | -14.39 | -49.09 | 2026-08-30 15:15:00 | MSG-03 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4f4d614f-942b-3bdd-8570-48e9c3e38873 | -4.96 | -55.84 | 2026-08-30 15:15:00 | MSG-03 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abfa0507-d911-3f64-a8fd-52fc4af39922 | -11.1631 | -50.594 | 2026-08-30 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 34a25630-00dd-3cec-affa-2c3b0b9b68fb | -12.3229 | -50.5892 | 2026-08-30 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 6aca3a75-8f03-3b90-b0a0-3ff158d96c31 | -21.0172 | -57.8313 | 2026-08-30 15:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 68.2 |
| b124f51d-3e9c-38b7-9147-95afa2e478d9 | -10.7867 | -45.3433 | 2026-08-30 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 287.0 |
| 0ac40489-60d3-3c40-b199-ab55eb7f57ca | -6.0 | -45.0889 | 2026-08-30 15:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| a5280798-c597-3aba-a1d3-66b13ce8cb62 | -8.231 | -61.4304 | 2026-08-30 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 3baec059-01c5-3238-844c-32aabff07994 | -15.3655 | -52.6703 | 2026-08-30 15:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 86d9e91f-33a5-3869-b5b1-f7c84ff2839a | -3.913 | -60.9395 | 2026-08-30 15:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| d95f3ed5-9655-377d-bedf-79c8be87210d | -10.5601 | -50.4022 | 2026-08-30 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 69e82a37-2364-39dd-b89b-e949d688845f | -7.3479 | -55.1544 | 2026-08-30 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 61c058d7-f9ce-3dba-9419-24629ef6ef15 | -10.7405 | -54.0606 | 2026-08-30 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| b2c17452-e3ee-39cf-adab-405298bcd7a1 | -10.7647 | -50.6579 | 2026-08-30 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 85b0c04c-dc82-3aa5-906f-d8ba12219d11 | -11.1349 | -49.9117 | 2026-08-30 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| e894f404-2b1e-3f9b-89fd-9066429de5da | -9.9281 | -60.5242 | 2026-08-30 15:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 879b9377-5d40-3a1e-81a5-baf024ff222b | -3.2361 | -61.2548 | 2026-08-30 15:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 5f7973ce-9c61-3ec3-adcf-19cfc559d2be | -11.1995 | -55.1008 | 2026-08-30 15:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 0d438ca1-b4b2-3645-aac3-dcdf51a45257 | -14.1456 | -52.8082 | 2026-08-30 15:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 155.8 |
| 7257a514-58b5-3d1a-89e7-f92024a2112b | -14.5627 | -52.077 | 2026-08-30 15:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| ef9a3cab-4ab6-34b7-b190-3a1d524ed215 | -12.0921 | -47.1812 | 2026-08-30 15:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 7276c500-7ec9-3d18-8978-e43b482428d5 | -7.2932 | -60.6096 | 2026-08-30 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 92c4b576-cd9d-3d7a-82b1-50831c4aadf6 | -11.3431 | -45.1521 | 2026-08-30 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| c24d52c2-bf04-3912-80ad-f48ab240b746 | -9.1711 | -59.618 | 2026-08-30 15:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 9bf71fa6-f07c-39c8-91ac-5c52bfc30dd5 | -5.8788 | -46.1103 | 2026-08-30 15:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| a270c733-75a9-379a-ac58-acede267bbf1 | -11.0244 | -49.6872 | 2026-08-30 15:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 47b50c49-926c-314e-9ae0-d9ad8f0c3545 | -14.7601 | -48.7467 | 2026-08-30 15:20:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 68d146b6-2311-3968-8697-0e50b141cd02 | -10.8804 | -50.4965 | 2026-08-30 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| cf35beb8-8001-3727-b287-a2f66f0440c3 | -8.574 | -66.9569 | 2026-08-30 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 34e73101-f140-3aed-8b17-d7593316f8b4 | -13.856 | -54.1175 | 2026-08-30 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 26e0ce84-b2da-31e9-bc8f-fdeb2b01b899 | -8.1345 | -45.4923 | 2026-08-30 15:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 8d13659c-650b-362a-9de3-91e38d73c447 | -11.2294 | -45.099 | 2026-08-30 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 698.3 |
| 9042f224-c80e-3c10-939b-d8a889f01d0d | -6.861 | -41.6772 | 2026-08-30 15:20:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 352.2 |
| 62de10fd-8bd0-3df9-9895-58fdb652123f | -7.9907 | -46.5177 | 2026-08-30 15:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 165.1 |
| 628683ed-3f26-3f58-887e-175a64c2527a | -7.1312 | -42.7708 | 2026-08-30 15:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 125.0 |
| 24adf017-e2fc-3c50-962f-ad976096a516 | -10.8253 | -45.3152 | 2026-08-30 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 1b95af24-d078-37a8-8cc0-81dd753af9a9 | -12.3803 | -50.5823 | 2026-08-30 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 16ec06d4-7d4b-395d-8ce8-3ebd62347256 | -10.7644 | -50.6792 | 2026-08-30 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 100.8 |
| e63fc34e-2657-3701-ba65-99e97c23cf6d | -10.1348 | -45.7006 | 2026-08-30 15:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 3a655ead-a4d1-36b3-80e4-3b848d95bcae | -11.3619 | -45.1724 | 2026-08-30 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 185.7 |
| 8354917c-4a27-3eef-b452-b3dd2afd2d0d | -3.4943 | -54.6567 | 2026-08-30 15:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 3f78445d-ed86-3bee-be6d-4a2b1c16b7b7 | -8.1534 | -45.4904 | 2026-08-30 15:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 157.6 |
| 029aed38-749f-3adc-83be-2c0751ba70de | -11.2503 | -54.0146 | 2026-08-30 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 220.9 |
| d84c271f-793e-36b1-8462-76a6938de86b | -7.5272 | -44.3413 | 2026-08-30 15:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 114.6 |
| ab82cc40-ab9d-329b-8a26-c0ebbb705e7e | -11.2443 | -45.3497 | 2026-08-30 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 324.2 |
| 666231af-a2d3-35de-b610-470694049269 | -3.1998 | -61.161 | 2026-08-30 15:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| ac95b6f7-befb-3144-8d98-46d7a2a2f988 | -13.4187 | -51.4372 | 2026-08-30 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 13c9d598-26a4-3ae8-b0e3-816fb0e7b1dc | -14.4838 | -52.1725 | 2026-08-30 15:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 8aba0f62-f77c-31b0-8543-b164a2d412ae | -7.917 | -61.3481 | 2026-08-30 15:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 6c355678-1a06-35e1-9636-8b811af29d2c | -10.9559 | -50.5098 | 2026-08-30 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| a679281d-30a9-3976-9e40-470513ecd268 | -11.2298 | -45.0759 | 2026-08-30 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 78c23b4d-ec70-37dc-9ffa-3f8386774af6 | -9.9284 | -60.4856 | 2026-08-30 15:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| e2b8adca-7d6c-3bd8-afdc-c429e5f3dc37 | -11.0054 | -49.6893 | 2026-08-30 15:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 813340f0-340d-3aa1-95dc-ba841633b114 | -11.0627 | -47.1385 | 2026-08-30 15:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 6c979f1d-d43e-3a98-9f09-d5b55ce60f64 | -10.3226 | -58.0847 | 2026-08-30 15:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 0a41fdf5-9c5d-38c2-a551-087013a47943 | -3.9363 | -59.3381 | 2026-08-30 15:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 72bdb952-30b4-3c8a-ac70-cb8ab3888d3d | -5.8893 | -57.7902 | 2026-08-30 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| b8d743ca-ad4c-3bb9-b740-cf4e551cb982 | -5.2547 | -55.9105 | 2026-08-30 15:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 7c0403b3-6b2a-3a5a-8e6e-ca86ca1a13de | -11.1807 | -55.1024 | 2026-08-30 15:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| cfad4bf9-3311-3496-bf2c-d0b78bf0030b | -8.078 | -45.4979 | 2026-08-30 15:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| db1a7a68-91c2-3124-9b94-5e28bf1c446e | -9.1712 | -59.5987 | 2026-08-30 15:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| fccb8c22-269a-3a62-9a69-ab64b74f4f42 | -5.4876 | -57.1416 | 2026-08-30 15:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 125.7 |
| c5ee0539-b41d-384d-8d57-1279f1661d8d | -5.9636 | -57.6704 | 2026-08-30 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 0dd934db-202e-32b1-a67a-6cf192e336bc | -10.1538 | -45.6982 | 2026-08-30 15:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 222.1 |
| fb492de2-b2a6-32de-aa08-117afd2083dc | -9.1662 | -60.2752 | 2026-08-30 15:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 132.2 |
| f9d33bcc-e26b-3add-9052-2e6ac9ffcae3 | -2.9488 | -43.7536 | 2026-08-30 15:20:00 | GOES-19 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| ae615526-4671-3291-b579-b6ef7f2d9f65 | -9.043 | -65.4175 | 2026-08-30 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 9e15b639-4934-3cec-a171-43763fa32a01 | -14.5631 | -52.0557 | 2026-08-30 15:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 427e00ec-5f15-3bf0-9e59-13e76dd3f7df | -5.9635 | -57.6899 | 2026-08-30 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 5dec6612-2e55-3ab2-9062-0c037514e989 | -12.9216 | -45.8812 | 2026-08-30 15:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 107.7 |
| ad28b4e0-bdff-33fc-992e-0478faacfa98 | -6.641 | -58.4987 | 2026-08-30 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| b587da6e-9cc4-3f07-a813-f22e9eb8de91 | -11.1821 | -50.592 | 2026-08-30 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 119.2 |
| e332253c-05b0-3fb1-a758-0128d6dc5c66 | -10.4794 | -64.5012 | 2026-08-30 15:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 56989843-7fc4-32a8-bb6c-61893c9b9c18 | -15.2283 | -57.6517 | 2026-08-30 15:20:00 | GOES-19 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| ed5d715f-ce4a-3abc-aa33-a92390d9d4e0 | -12.2086 | -50.5815 | 2026-08-30 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 63f8246f-4473-3371-9fe6-4ac4a40914f2 | -14.4842 | -52.1512 | 2026-08-30 15:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 20fa9fec-6008-3230-b55f-441a518e39e3 | -7.3294 | -55.1555 | 2026-08-30 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| e29f2dd4-0873-3db7-bb66-7c5f2c6eb63a | -5.4875 | -57.1611 | 2026-08-30 15:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| d9e1b5b9-05cf-305c-b712-50434ce4b9e9 | -10.937 | -50.5118 | 2026-08-30 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 6fdd91ea-0770-33ce-93c7-66f4c96c926b | -9.9468 | -60.5232 | 2026-08-30 15:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| c1cb3d2d-9fda-34f5-8a14-627fc371fb5a | -9.9282 | -60.5049 | 2026-08-30 15:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 209.5 |
| 83651883-5c09-301d-9c59-8917c099117a | -14.1645 | -52.8269 | 2026-08-30 15:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 6473ee0c-7c1c-3a4d-8b81-b1943d789d08 | -8.5925 | -66.9564 | 2026-08-30 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 142.2 |
| db536e79-8848-3005-a55d-952ad00eee2b | -14.4846 | -52.1299 | 2026-08-30 15:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 188.6 |
| bd973ccc-2432-3ce5-8a7f-a3f39712bd3c | -10.7409 | -54.0196 | 2026-08-30 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 2a484300-575d-3e05-8393-ee5c53813be9 | -12.209 | -50.5601 | 2026-08-30 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 80484bda-7ab5-3000-89dd-0111227cf377 | -9.2071 | -59.771 | 2026-08-30 15:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| b51b7edc-597c-3d2a-9ee3-75a9597014bd | -12.9221 | -45.8582 | 2026-08-30 15:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 79f7f8f4-242f-3128-a121-4907d5629f9c | -9.0614 | -65.4355 | 2026-08-30 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| e1c4c0d1-502b-338a-871b-41d9a048fd26 | -10.8801 | -50.5179 | 2026-08-30 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| f74c0549-a853-3bfb-837a-df79c7ce9301 | -16.2735 | -42.5653 | 2026-08-30 15:20:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 193.5 |
| 62002fd7-fe9b-3a8f-ba02-704ff33981d2 | -3.6399 | -60.5466 | 2026-08-30 15:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 97.3 |


[Clique aqui para ver as próximas entradas](README92.md)
