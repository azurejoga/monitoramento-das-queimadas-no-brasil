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

## Dados Diários - Página 155

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6cdf55d0-8997-3dc0-a10e-52a74d69e464 | -5.11153 | -50.71814 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 882ab625-b24e-3855-bc9c-fdb9722ca49c | -5.111 | -50.71469 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 0010129f-b626-3235-aeaf-50c17a276bd8 | -5.10826 | -50.03469 | 2024-10-25 16:52:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| cb029f47-2cbb-3941-ae20-7f358981b84e | -5.0598 | -50.44737 | 2024-10-25 16:52:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ea873ee3-dc87-339a-9aba-bfca8a69bf75 | -5.00841 | -50.84394 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 419ed65b-f0a7-395f-8931-53a0ee38207f | -5.00564 | -50.84789 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 73101ed9-5e21-3be2-9865-3eaeb13b9e1e | -5.00511 | -50.84445 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d7c2ac16-32a7-3636-8e87-c8f3f865f7b5 | -5.74756 | -51.05588 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 08232cdb-355f-35ca-97f2-0a624fc9b5ec | -5.5506 | -51.07977 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d0757948-facd-3d44-8281-9b5aa7217872 | -5.48925 | -51.03254 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| d2518b0b-03d0-3408-afe8-305043dd8be0 | -5.29166 | -50.98608 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| fbf1f56a-c964-3377-bd56-fb0f1191ecd3 | -6.47658 | -49.86695 | 2024-10-25 16:52:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8bc0f2c7-3331-3f05-a978-f4c9953f34b4 | -6.43753 | -49.90163 | 2024-10-25 16:52:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 31cbac9d-4abc-3db0-a911-c07752896b38 | -6.20676 | -50.85531 | 2024-10-25 16:52:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ab05a2e4-d457-3762-983e-099a566e4f07 | -6.20014 | -50.85632 | 2024-10-25 16:52:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 90c04613-afcf-39b4-8bb2-ab1b018089c0 | -6.19736 | -50.86029 | 2024-10-25 16:52:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a1c06697-eb90-344a-a391-ddb0799149db | -6.19684 | -50.85682 | 2024-10-25 16:52:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| a6a627a0-652e-3411-a44f-7afa8ebcad91 | -6.193 | -50.85387 | 2024-10-25 16:52:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 86430cbe-4137-3342-9a2b-88a380cf5160 | -6.1897 | -50.85438 | 2024-10-25 16:52:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| aef003f2-48cb-3422-947e-decc356b8174 | -6.18639 | -50.85489 | 2024-10-25 16:52:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 646b68da-8d8b-362c-9c60-ba306f8dfc4d | -6.18309 | -50.85539 | 2024-10-25 16:52:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b0b46a16-ed9f-3d37-b56b-95dd4b1bee87 | -7.8002 | -50.85335 | 2024-10-25 16:52:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c2cad494-219f-3293-81b6-75fc245df08b | -7.79741 | -50.85732 | 2024-10-25 16:52:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 35b2e163-fd8f-39ee-901a-e38b47b6aeef | -7.79687 | -50.85383 | 2024-10-25 16:52:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| acb6e733-4005-33dc-8888-6078f372406b | -7.60783 | -50.70531 | 2024-10-25 16:52:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 388a4d22-121c-3684-887c-8bfa5fa39da4 | -7.57036 | -50.70391 | 2024-10-25 16:52:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a3dfd658-2d6e-3fd1-b2a1-050a929aae57 | -7.56676 | -50.70444 | 2024-10-25 16:52:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b36ee5c-1207-3fc4-93ca-0bf580ecafa1 | -7.33341 | -50.66723 | 2024-10-25 16:52:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f4169056-f079-3965-8d8f-da0cc5c10a32 | -7.3301 | -50.66773 | 2024-10-25 16:52:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 52a89e39-e89b-3ea8-9963-6261fcd4b7d7 | -7.32733 | -50.67171 | 2024-10-25 16:52:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3be3b914-6950-3ced-bb13-a813d748a07a | -6.9161 | -51.34304 | 2024-10-25 16:52:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cd6ccf4c-441d-3748-a010-6a52d6d5e653 | -6.91557 | -51.33952 | 2024-10-25 16:52:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f5d17b29-3787-3409-9d15-1c6cf861b371 | -6.91165 | -51.26823 | 2024-10-25 16:52:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| bf58c35f-edf0-3ecb-857f-be73e93e92a7 | -6.86387 | -51.06423 | 2024-10-25 16:52:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e94603d2-de02-32c3-9590-8ea30d736ed4 | -6.81589 | -50.86238 | 2024-10-25 16:52:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7bdfc30c-f7f8-3b50-add3-cbc5e7747f43 | -6.80981 | -50.86686 | 2024-10-25 16:52:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4607901a-c0f6-3a0a-a560-5d8cc3568d3d | -6.80477 | -50.87827 | 2024-10-25 16:52:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 81a2a7fc-4cac-3429-bf37-9d67500785d8 | -7.81898 | -50.24191 | 2024-10-25 16:52:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ec075f03-f7ae-3970-8132-8dad1f9be95e | -7.54628 | -50.3458 | 2024-10-25 16:52:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f4af9e8c-a410-36b0-bada-f520ef681c81 | -7.51441 | -50.33653 | 2024-10-25 16:52:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| d206f912-0b87-3ee4-9e7e-8e497c6537ff | -7.37269 | -50.01112 | 2024-10-25 16:52:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4e79c5c5-34c9-3343-8170-9ef002eeb8ff | -7.37216 | -50.00765 | 2024-10-25 16:52:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| dc091a49-bd75-3d7d-a040-d61afdcdc2ee | -7.36885 | -50.00817 | 2024-10-25 16:52:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c3cc6ce9-93a2-3f37-9ed2-285a8c77a602 | -7.31312 | -49.95732 | 2024-10-25 16:52:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6bde85d2-6f24-3d88-8709-95f0c959bdec | -6.95689 | -50.47168 | 2024-10-25 16:52:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 77a4f162-21c3-37f0-a6ca-69ed83709e8d | -6.90741 | -50.08289 | 2024-10-25 16:52:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| a0540ce6-d48f-3ca2-8bd9-0f7c7d013a7f | -6.90279 | -50.31723 | 2024-10-25 16:52:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3eb768c3-764a-3443-a326-516ede239e14 | -6.90002 | -50.3212 | 2024-10-25 16:52:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ee65e3b4-c941-33ef-af61-fcc793af84c2 | -6.89949 | -50.31774 | 2024-10-25 16:52:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 012ac507-514c-3b50-b4aa-9d8867640d49 | -6.89777 | -50.32862 | 2024-10-25 16:52:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 61c99713-4065-31b0-b3d7-53d003e19466 | -6.89724 | -50.32516 | 2024-10-25 16:52:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 446f6c0a-322f-370d-9d43-5efe54ac8763 | -6.89671 | -50.3217 | 2024-10-25 16:52:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 65aeeb80-8868-34b7-82b7-ed25781cf09a | -6.89447 | -50.32913 | 2024-10-25 16:52:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 136a27c0-abf1-370f-bc15-612b0b6a7a92 | -6.88492 | -49.95863 | 2024-10-25 16:52:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a71f8e7e-950f-331c-b3eb-8cc4e9e0a2cc | -6.83017 | -50.42046 | 2024-10-25 16:52:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ae64508f-0626-3f52-ab5d-f453e11433f2 | -6.82911 | -50.41354 | 2024-10-25 16:52:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 66cdae9b-ee63-3969-8b8c-4824280bb554 | -6.82687 | -50.42097 | 2024-10-25 16:52:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b8206fd0-20e4-337a-a0f7-1165e16a23bf | -6.8192 | -50.50351 | 2024-10-25 16:52:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 453df803-dbba-39c9-9d94-626f09624e87 | -6.68361 | -49.97645 | 2024-10-25 16:52:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| becb73b8-89e5-3ebd-bac2-7abb215d323c | -6.68083 | -49.98042 | 2024-10-25 16:52:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| fc42c283-e8f1-3fb5-8f3e-135595dc0728 | -6.6803 | -49.97696 | 2024-10-25 16:52:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 826e93fd-0322-32a6-84ee-3c0a84b1bb73 | -6.67675 | -50.41657 | 2024-10-25 16:52:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f5b5a595-335b-3e11-9f6d-e718d7c491db | -9.28616 | -50.36818 | 2024-10-25 16:52:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2774564d-96b8-37a7-b68d-a7506491d090 | -9.18493 | -50.55212 | 2024-10-25 16:52:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| e8318ffb-8e44-3a3e-8238-4ec8669c3e02 | -9.1844 | -50.54861 | 2024-10-25 16:52:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 1717deb8-a037-3e8f-8b16-942b574f6347 | -9.14236 | -50.563 | 2024-10-25 16:52:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bb82415d-2d16-38c0-9a6c-edaa9e31df4a | -8.87732 | -50.5398 | 2024-10-25 16:52:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 35b8b376-11cf-38ee-8a84-c0e98499a6b5 | -8.86549 | -50.68561 | 2024-10-25 16:52:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d5b77b15-e2a2-3ad5-9c2b-df2b0fe2dade | -8.74444 | -50.78411 | 2024-10-25 16:52:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| ca67df80-dfd4-3d56-be90-560a34bc67c6 | -8.39361 | -50.42079 | 2024-10-25 16:52:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dbf9a4af-62e1-3cb2-8406-88c49e5d490f | -8.38917 | -50.18964 | 2024-10-25 16:52:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fc55fb6a-962c-33bc-9785-f1285d3286be | -8.38389 | -50.33255 | 2024-10-25 16:52:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5dceed77-3e3b-3e9f-8da4-08ce927607b5 | -8.28946 | -50.33722 | 2024-10-25 16:52:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| d9c9e6ce-3636-3980-8588-c26ac0a5d055 | -8.48894 | -50.80215 | 2024-10-25 16:52:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ed594def-09a2-3ba1-8fbc-738be1d60b07 | -8.48841 | -50.79864 | 2024-10-25 16:52:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cd1b4a5d-6c57-31b8-9247-ce1fe393d676 | -8.39234 | -50.97232 | 2024-10-25 16:52:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a4da8df3-ebb6-30a3-ae0d-8debf7b15fe8 | -8.34836 | -50.86068 | 2024-10-25 16:52:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| fd13c7ea-9cab-392f-a417-8d664a7defe4 | -8.33524 | -50.93112 | 2024-10-25 16:52:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| def2b189-3e65-369d-aba2-da2e4296f821 | -8.2363 | -50.74878 | 2024-10-25 16:52:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| f70878c1-c0b8-3d32-8cdb-14fe0e0c2218 | -7.97668 | -50.91894 | 2024-10-25 16:52:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f85de243-2d57-3a39-80eb-463a11610734 | -10.04885 | -51.44043 | 2024-10-25 16:52:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1ce55851-7c96-3238-b731-7dcbe1dd7390 | -9.63134 | -51.64798 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| f31b6475-4726-3ce8-a5af-faff496df227 | -9.63079 | -51.64426 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1ef390d4-6eec-358d-bc04-87374061e6f5 | -9.62793 | -51.6485 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 860c09ed-3769-328f-93da-6d75a593f73e | -9.62738 | -51.64478 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| bcbfba66-95c8-357b-b66c-30be442107ac | -2.24488 | -50.53765 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 42e44026-2558-34a1-b4e7-4763c4f443a9 | -2.24434 | -50.53416 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| f3428a7c-cf27-39d0-ab14-f05236329f31 | -2.2438 | -50.53067 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 6942a23e-7def-3ea0-9d93-e069f86a740f | -2.24155 | -50.53815 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a8ff230e-4b42-3f13-b052-33b717f6453d | -2.23822 | -50.53866 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6d3c9108-36d7-3f26-b629-64276ba57fdd | -2.23768 | -50.53517 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 1dbfd551-605c-3521-b1ad-d1bf8f5dfef9 | -2.23714 | -50.53168 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| f8805299-f6f7-30ef-b60e-13925176abeb | -2.23592 | -50.67797 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b032752c-be4c-35be-98bb-1b9d4d9dc007 | -2.23538 | -50.6745 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 90ecdc5e-0c38-36e9-8dcf-fb1537362cc7 | -2.23328 | -50.5287 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 47e2b61e-7528-3960-a48b-7ab8ba481968 | -2.2325 | -50.67873 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f431b6da-f4a2-3045-8244-a1c43bcccdca | -2.23197 | -50.67525 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f3c8cf40-522f-35f5-8ed1-a96540f96c99 | -2.23194 | -50.45376 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 57ae86cc-2e39-3abb-96fc-17babbd12c55 | -2.23117 | -50.71447 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 68139064-4bee-3bff-a43f-f5f79beb0f79 | -2.22865 | -50.67576 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README156.md)
