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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70ab1c6a-c44c-3c67-85a0-f7059270fa7b | -13.79012 | -45.86694 | 2025-10-09 05:12:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3ce0939e-1766-3ca7-8845-852bec3c6a60 | -15.75115 | -49.03117 | 2025-10-09 05:12:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a801f880-5330-39a1-ba42-80aef18ba352 | -10.85017 | -49.94059 | 2025-10-09 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d0635ca-a067-3713-b210-c308f153f424 | -11.99133 | -45.18822 | 2025-10-09 05:12:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d4dcc2f6-67eb-3792-acce-3a219d380be9 | -10.35415 | -50.21299 | 2025-10-09 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 26109753-1f7b-350d-aeb6-246ddd0f7276 | -12.26216 | -47.88585 | 2025-10-09 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 105f0fb0-5e25-33b4-a263-a65d5e4d4982 | -10.52768 | -50.02697 | 2025-10-09 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75162b7f-f922-3d7a-ac87-9353255bcb63 | -15.01177 | -47.53668 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb02a85d-268c-3797-b449-cab157cfe238 | -11.00173 | -62.64216 | 2025-10-09 05:12:00 | NOAA-21 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea15bbbe-443d-36fa-b1e9-07caa9e7b66b | -11.7789 | -45.14523 | 2025-10-09 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b80861a4-5d7d-3f08-8277-508938d09be7 | -15.00411 | -47.5301 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2db361da-6243-3c66-9a03-ea4827f4de9d | -12.09172 | -64.22595 | 2025-10-09 05:12:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecf19ca8-ec7b-3201-9cc9-95bdd78fb080 | -15.39335 | -48.04974 | 2025-10-09 05:12:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0d1df04-e55c-317a-b84c-f88a3c3a6d06 | -12.26157 | -47.89097 | 2025-10-09 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b72b9c8d-f739-3b38-930b-9b0cb23c03e3 | -12.25735 | -47.87542 | 2025-10-09 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d66f8198-4a5f-3a22-aeff-bc86298ea9dc | -11.79277 | -45.14327 | 2025-10-09 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5a88bf72-13c9-37da-8bbf-b78f7956c98a | -10.60072 | -45.01928 | 2025-10-09 05:12:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6f756fe0-c74b-3213-b632-1d106140f61b | -15.39338 | -48.04001 | 2025-10-09 05:12:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 068d61ee-6796-36f2-95ce-80b6a10f870c | -11.87543 | -62.76867 | 2025-10-09 05:12:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3aa4d58-fb79-39cd-8b19-8b24541e1c2a | -9.62509 | -67.5165 | 2025-10-09 05:12:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5291d162-6326-376f-b23e-b27ff7df2d5b | -13.8251 | -45.81013 | 2025-10-09 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c8ab1813-d500-3048-9522-df71cac0caff | -10.84434 | -49.94588 | 2025-10-09 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 37fa1312-ceff-3a30-a292-d6628eff3f68 | -14.63686 | -49.25495 | 2025-10-09 05:12:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97803a8b-935b-3051-8999-6439e708402b | -15.2285 | -46.36524 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 70889ff5-ee27-35b2-8134-51dd60f5d3b9 | -13.8065 | -45.84208 | 2025-10-09 05:12:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6bf435e3-13bb-3580-9333-c2af7296e0c8 | -9.86487 | -65.17152 | 2025-10-09 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98ba840a-346b-30f7-ae47-3afca336e21e | -10.85523 | -49.94129 | 2025-10-09 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c861ef1-27f2-31f6-9723-5b79025b043d | -11.77753 | -45.15437 | 2025-10-09 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 032a3aca-fd61-3746-b326-7ebded5f9710 | -15.22694 | -46.38187 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 34e4279d-7c20-3a8c-9888-b1e82a2d6d78 | -14.72513 | -48.3689 | 2025-10-09 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f248a007-42fd-34c3-8f5e-d1681547dd4f | -10.85908 | -49.91125 | 2025-10-09 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3a04532a-c5bf-30ff-b532-548f35a565e3 | -15.49475 | -47.96528 | 2025-10-09 05:12:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7937d20-2ce7-3cd2-892f-feb3d14324b1 | -15.39288 | -48.05434 | 2025-10-09 05:12:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e28ea4e4-b414-3bc2-b6c9-f9c7b63b157d | -14.83994 | -48.3608 | 2025-10-09 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c72b3c9-03c9-3996-ab20-f45abb33489e | -15.23284 | -46.3563 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 42f459f3-c4db-3fe4-b6d7-7d8e2a19f94d | -13.68021 | -48.74985 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 306b1be1-b1dc-3fcc-a763-ebda318bf66d | -15.75411 | -49.00339 | 2025-10-09 05:12:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4abc956d-76ab-3527-b66a-583477cba4c1 | -15.38677 | -48.0539 | 2025-10-09 05:12:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8be78aa4-2fa9-3e6e-ac69-7274f76a1f0f | -15.5612 | -45.32495 | 2025-10-09 05:12:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c6a27047-b7e8-3bde-832f-9f4ddc102655 | -10.35581 | -50.21478 | 2025-10-09 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| babdc35c-6b91-3ffe-9c38-8836a69e6f22 | -15.55799 | -45.32095 | 2025-10-09 05:12:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9e631fbc-82c1-37ec-a13d-3fbdb24361f1 | -11.99831 | -45.18634 | 2025-10-09 05:12:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ad394882-fec7-307e-b78e-68992124453b | -15.74291 | -48.99913 | 2025-10-09 05:12:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2669bf6a-06f3-3ee3-915d-0377aba82886 | -15.74948 | -48.99219 | 2025-10-09 05:12:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 60d213a2-cb8a-3532-bad0-2374a99c5ecf | -15.29433 | -46.15413 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e1a6e374-1a0d-3915-8136-1b471af81db1 | -11.77826 | -45.15096 | 2025-10-09 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f223815c-8033-3907-8384-b27611d273ab | -10.73474 | -49.33295 | 2025-10-09 05:12:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f350143a-6e31-323f-a245-38f7be8826b8 | -15.7545 | -48.99974 | 2025-10-09 05:12:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52eb1aec-892b-3577-a130-60c0169241ba | -14.72741 | -48.3653 | 2025-10-09 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9a7605a6-7491-3e22-9495-7004f4c5ec3f | -15.22441 | -46.37262 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5b35f644-f2d8-3dab-9a64-29d58be83e6d | -12.08694 | -64.229 | 2025-10-09 05:12:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 426bdbe6-564c-3edc-845a-786f7297f739 | -11.99901 | -45.18246 | 2025-10-09 05:12:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c4592e3-16f7-3f99-bfba-faa798f4e586 | -10.07941 | -64.69383 | 2025-10-09 05:12:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a96ffb2-b89c-377e-be1f-30cd8d691b04 | -10.52343 | -50.02042 | 2025-10-09 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 84763ee4-2522-3b9a-9a7b-bf2da9e49222 | -15.22332 | -46.38348 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a4702a5-1406-3477-9936-236fd1ba0e9b | -14.83817 | -48.36089 | 2025-10-09 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b572fb8-0db9-312e-a71d-1966ce8ede4f | -13.8215 | -45.83069 | 2025-10-09 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cec08c68-d30b-30c5-ad54-99da57d858fe | -14.72564 | -48.36401 | 2025-10-09 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7a252939-d27c-3f27-a137-59f015ac4d90 | -9.29643 | -68.24882 | 2025-10-09 05:12:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f2ee0a85-79d4-3153-8ebb-b72bed215de4 | -15.38531 | -48.0577 | 2025-10-09 05:12:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0cf60a0c-1552-3ac6-b380-344e9cf38bbb | -14.7982 | -46.08709 | 2025-10-09 05:12:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5b9938f4-3535-3d9f-bda1-3b23dc735fe5 | -15.47586 | -47.9682 | 2025-10-09 05:12:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1e0f2e45-1e21-3bc8-826f-3589b98d54ed | -9.79985 | -59.96684 | 2025-10-09 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da0fd63b-8b83-3f75-98cf-5768cf82bce2 | -14.84409 | -48.36164 | 2025-10-09 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cf801041-5cdb-3202-bce3-2f5cac4147cc | -17.52339 | -46.74484 | 2025-10-09 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 996312e2-b237-3e56-8707-b12107d241bc | -19.47093 | -55.47842 | 2025-10-09 05:14:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 3819c992-41ae-3b11-8680-487b863ed9d5 | -16.28609 | -47.14089 | 2025-10-09 05:14:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 73f48cbd-4b8b-336d-b76b-2ac0773f7071 | -19.19124 | -46.49218 | 2025-10-09 05:14:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4b55787a-3c6f-34b8-8cc4-984f495f3ec9 | -18.03466 | -57.56483 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d22f2ed0-26bd-3995-919c-7e3706d16bf5 | -16.02171 | -59.53162 | 2025-10-09 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f5cffae-d3f3-3d6f-b838-1c266820d5ae | -17.53577 | -46.75873 | 2025-10-09 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1620ef6a-335b-35c4-9078-f87fa5678a83 | -18.06482 | -57.52865 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 63b6dc74-c8f1-3e16-a0a3-d45e6bbdabeb | -17.92529 | -57.52094 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| bd35d1c7-2b22-3c7c-97a3-adcdb767f085 | -15.99968 | -59.54255 | 2025-10-09 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08b0a34f-0160-39c9-be93-c6c691242270 | -18.01245 | -57.49505 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 7a49d5fb-52d9-3f1e-98d7-4cb7608307da | -17.26763 | -46.96411 | 2025-10-09 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0aa8fe8a-5aa3-35a7-a4aa-6a56644aa8e1 | -17.4198 | -46.5495 | 2025-10-09 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2a45ce27-73e5-3890-9db8-90813e471074 | -18.02637 | -57.54809 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| db368f46-316e-3dac-958c-6793e07ab3de | -18.00839 | -57.4985 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 6329ae07-d894-389f-88f2-7c0b5a33e81d | -18.02768 | -57.56377 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| b9573907-4a6f-3d43-9afb-b93031b6bd1c | -17.99557 | -57.48803 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e3c9e359-861a-39c7-bea5-8a2521e06bbf | -16.70162 | -47.59633 | 2025-10-09 05:14:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 971eafee-4e8f-390c-871d-8870a0c77a14 | -17.91482 | -57.51937 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 9e1eaa5f-127c-3998-b034-a8337a008146 | -17.92821 | -57.52548 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 23a3fff2-6702-30ef-a5ab-425d2dde4637 | -16.01511 | -59.53052 | 2025-10-09 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5175aeb3-ef12-37d1-8070-e5b861791c5a | -15.97715 | -59.53518 | 2025-10-09 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86ff1376-c322-3cf0-9d3b-0abe51bc6aea | -17.91603 | -57.51075 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c875f01a-3275-33c0-a95f-e81f5b776c87 | -15.99912 | -59.54612 | 2025-10-09 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1503370b-31c7-3dd4-9530-c0e6ad7dc08c | -17.53267 | -46.75765 | 2025-10-09 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 1dfde0a9-0014-3562-a802-b53d7ea80a6b | -17.98068 | -57.50799 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 09aff6e5-88b7-38a8-b9fc-39a3bfc6c4be | -18.06302 | -57.54116 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| b55d08bf-383d-3696-b8c7-374d3afabbf8 | -16.60022 | -58.16167 | 2025-10-09 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 04c14bb3-9cd0-3af3-9fa8-90b510119cfa | -20.12152 | -49.53938 | 2025-10-09 05:14:00 | NOAA-21 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2c524f84-787f-3e7c-b98f-190a2c0109d5 | -17.91434 | -57.49747 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 3524241c-3a6d-3287-9fd1-ee0286205eed | -18.02644 | -57.52243 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| cbc71c58-0fde-3f3b-895b-321c20c312c6 | -15.97933 | -59.54285 | 2025-10-09 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dbd83b36-d8e5-3790-b116-253fc1e6958a | -15.99582 | -59.54557 | 2025-10-09 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6bba08b2-c06e-3a24-9bf8-7627109f94b3 | -17.97489 | -57.49865 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c9eb6fef-f7f0-39bd-ad59-b91b06901f20 | -18.05778 | -57.55279 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| c23c1df3-366f-369a-8be5-2db8529ce0fe | -15.97659 | -59.53874 | 2025-10-09 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README56.md)
