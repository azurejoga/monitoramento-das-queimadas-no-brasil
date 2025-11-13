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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec0b5034-5b38-3ee6-a854-1bc734a2bb21 | -4.4595 | -46.551399 | 2025-11-13 00:14:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7edda082-d32b-3f26-91a5-56c3e59f869b | -6.0296 | -43.504799 | 2025-11-13 00:14:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7b75d7ef-87cf-30d5-8bf3-5caa4b41a4be | -2.4547 | -49.266201 | 2025-11-13 00:14:00 | METOP-B | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59699624-96e8-3e02-b914-9541730b9a4f | -7.1064 | -42.7164 | 2025-11-13 00:14:00 | METOP-B | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 109a4235-541f-3449-a19c-e5311276090d | -4.2122 | -48.5667 | 2025-11-13 00:14:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e974f54-1834-3e34-8956-e3a5843e5833 | -4.5218 | -46.420101 | 2025-11-13 00:14:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3afec58e-80ec-36ae-827e-ba6deecc4c94 | -10.7584 | -44.905399 | 2025-11-13 00:14:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a71836e3-2810-3ccf-90cf-1b2fe57f4912 | -3.8484 | -50.0467 | 2025-11-13 00:14:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96268650-4729-3f87-91b0-bb009432bc63 | -5.624 | -46.906101 | 2025-11-13 00:14:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c9e504c2-ffd5-3143-8d14-dc9c0d901271 | -7.1007 | -42.353699 | 2025-11-13 00:14:00 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9b93e591-667a-3109-b5e6-b450907584ba | -20.4569 | -53.018902 | 2025-11-13 00:14:00 | METOP-B | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 55ec7c83-c7a5-3c50-900b-10d5f25ce021 | -2.5221 | -47.8027 | 2025-11-13 00:14:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4e6b8bb-69e2-3e25-b2e3-6d7a426e5546 | -10.5255 | -45.099602 | 2025-11-13 00:14:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3ab7ce8a-5916-3095-a19c-7ab3d6acb22f | -4.6746 | -45.792599 | 2025-11-13 00:14:00 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3101227d-be75-38ba-9666-3201688a45b6 | -9.9342 | -44.479401 | 2025-11-13 00:14:00 | METOP-B | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7fb0216e-5308-32b0-a2b6-49423036b77a | -3.4414 | -45.582802 | 2025-11-13 00:14:00 | METOP-B | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 31cf48c5-143d-3d7f-a63e-ee716b645076 | -4.7197 | -46.428902 | 2025-11-13 00:14:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2ab68ac8-d292-3d42-bf7d-37b4583dc142 | -7.7903 | -42.6059 | 2025-11-13 00:14:00 | METOP-B | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9213c822-db80-3a95-b4ee-a5ffa3d13462 | -2.0196 | -47.318199 | 2025-11-13 00:14:00 | METOP-B | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17644efe-7176-312e-bca3-478e77bc02a0 | -6.4855 | -48.3643 | 2025-11-13 00:14:00 | METOP-B | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 76726701-31fe-37fb-af12-c273e85aad2f | -7.5182 | -40.046902 | 2025-11-13 00:14:00 | METOP-B | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| a04b59de-39c4-39b0-aac5-f796b09a6226 | -8.3947 | -49.605598 | 2025-11-13 00:14:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1c78f71-0ea3-3694-b144-f6a7269f6a12 | -2.6335 | -47.3004 | 2025-11-13 00:14:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9430d47f-4de1-3c8e-aa2e-6cba79109ce2 | -5.0909 | -47.4543 | 2025-11-13 00:14:00 | METOP-B | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1399e736-0d9e-341c-b508-2b3186c777a8 | -8.9452 | -49.811501 | 2025-11-13 00:14:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 644f0a66-d55e-3020-8270-9b060c099b57 | -17.3302 | -46.496799 | 2025-11-13 00:14:00 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f781e2f9-9648-37e6-99f1-8f28f8e60510 | -2.4499 | -49.245201 | 2025-11-13 00:14:00 | METOP-B | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69c54b1e-8720-30a4-b075-b943a7654c3f | -10.687 | -44.996498 | 2025-11-13 00:14:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cfacf2f4-9536-3467-976e-1b83d75e055b | -10.763 | -48.135899 | 2025-11-13 00:14:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2856aa4e-5664-3629-9ec1-5923a03e592f | -3.4018 | -50.167999 | 2025-11-13 00:14:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbbd8a3e-306c-3361-9c09-520e16788a45 | -5.6807 | -45.996799 | 2025-11-13 00:14:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 71cb4a1d-5b54-3ef3-891d-9a7bcaec3908 | -5.3167 | -45.190201 | 2025-11-13 00:14:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c9a28c6f-924f-3d2b-b7db-f45a426e5c9b | -8.2087 | -47.874001 | 2025-11-13 00:14:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b85d0c48-bcc9-378c-9922-746c09c851de | -6.5684 | -48.727501 | 2025-11-13 00:14:00 | METOP-B | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec80a9b4-414e-3fb4-870b-2470f31ced7f | -4.1905 | -50.3293 | 2025-11-13 00:14:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b343c1ba-f64e-3d84-b092-cc39611b5736 | -2.9375 | -45.540501 | 2025-11-13 00:14:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d43405ac-5524-315c-86e8-281339d461a9 | -4.7118 | -46.439602 | 2025-11-13 00:14:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7f39108a-25ca-3554-99d3-25e1d56dbc57 | -7.8258 | -41.7407 | 2025-11-13 00:14:00 | METOP-B | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8cd90834-499f-3dc5-9834-4da57aad36d1 | -6.1428 | -48.038502 | 2025-11-13 00:14:00 | METOP-B | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 43394331-2115-3c96-a4ae-ac1fe9c4ca08 | -3.1561 | -50.2659 | 2025-11-13 00:14:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02e0d404-ac8d-3a62-8eb8-2da06dd31ac3 | -3.1043 | -49.2673 | 2025-11-13 00:14:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0177e151-77aa-3a20-a021-568249e78e5f | -13.3307 | -43.180401 | 2025-11-13 00:14:00 | METOP-B | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 85d17244-4c18-3a63-9a7b-eab9325e35ad | -1.708 | -54.6591 | 2025-11-13 00:14:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c823ba6-8ba2-32f4-90f0-81b2b5dcc9be | -2.8235 | -45.448601 | 2025-11-13 00:14:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4b31f537-3f32-3336-986a-452fb74e9602 | 1.4582 | -55.834702 | 2025-11-13 00:14:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ea66276-c35c-3358-ac82-e5cf4a67dab0 | -3.2246 | -45.580399 | 2025-11-13 00:14:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| aca5128a-9ac6-39f3-85b6-fdda04c76c67 | -7.6643 | -45.8792 | 2025-11-13 00:14:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9ad3a9e7-cb8e-3066-b7c8-e414eb4ff67f | -22.475401 | -44.1903 | 2025-11-13 00:14:00 | METOP-B | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7950f0ad-a1c1-3bea-8191-e41f0b2cbd31 | -3.3553 | -49.826801 | 2025-11-13 00:14:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81711045-e669-3631-a0b2-43b14cbbe4d3 | -10.6205 | -45.239498 | 2025-11-13 00:14:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 372eee76-d956-35e5-88ae-e9d7cd3266a4 | -3.4845 | -44.3578 | 2025-11-13 00:14:00 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c8eeb75c-11f5-3039-a0d4-ef9f75a17579 | -5.3287 | -45.1978 | 2025-11-13 00:14:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5d6e3a1b-2e23-39f4-8048-15d2f2b24f55 | -6.4839 | -48.3573 | 2025-11-13 00:14:00 | METOP-B | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 9f44a6c7-2694-3017-bb66-8038a0eef7f6 | -8.5494 | -48.0116 | 2025-11-13 00:14:00 | METOP-B | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f9df1672-cfc2-3e69-8ee5-c6c0bdafb436 | -5.6769 | -43.536598 | 2025-11-13 00:14:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fbaad4b4-c1bc-3530-853c-411ef3605798 | -7.1255 | -41.865101 | 2025-11-13 00:14:00 | METOP-B | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3cc0db46-d150-35e2-afb4-b6f3fcadf9b7 | -15.4887 | -48.987202 | 2025-11-13 00:14:00 | METOP-B | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 08ca0cc9-079a-3992-a88c-19673694ce18 | -7.5001 | -38.595798 | 2025-11-13 00:14:00 | METOP-B | CONCEIÇÃO | PARAÍBA | Brasil | 2504405 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| ca02a09e-5de9-38cf-9b75-c946ecf79f48 | -5.3622 | -46.754799 | 2025-11-13 00:14:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b64e6cca-f419-34af-af08-1b762edd5b43 | -12.0675 | -48.209702 | 2025-11-13 00:14:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 31d77fd0-22e7-3189-b135-9b957ccd8922 | -16.452299 | -44.999401 | 2025-11-13 00:14:00 | METOP-B | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 61c5b3a9-d6a1-3fa2-a224-9ee4ff6e3982 | -5.3524 | -46.757 | 2025-11-13 00:14:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cf399605-271d-3c87-87a3-133d9c2822d3 | -15.3923 | -43.064098 | 2025-11-13 00:14:00 | METOP-B | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 4230839e-02a6-39a8-91f4-7509c162a83d | -22.6465 | -44.9076 | 2025-11-13 00:14:00 | METOP-B | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 551d5182-803e-32bf-962c-43ee8188f2d4 | -5.3934 | -46.7561 | 2025-11-13 00:14:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 045fd64a-1fe7-38ea-ab5c-097297c5ee46 | -5.7239 | -44.819302 | 2025-11-13 00:14:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bb075ca7-6124-3429-9121-38779b598419 | -2.8212 | -45.4384 | 2025-11-13 00:14:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1beaed07-e778-39bb-a159-94b37d4e5b97 | -12.4355 | -43.7528 | 2025-11-13 00:14:00 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 404264b7-9160-3219-b5a1-a493641fab28 | -7.557 | -47.237 | 2025-11-13 00:14:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9dbf3e77-9e87-3398-8aa5-433fec172693 | -2.8932 | -48.072701 | 2025-11-13 00:14:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6240438d-df45-3b47-986e-dc57a29ac711 | -3.4034 | -50.447399 | 2025-11-13 00:14:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4ff68e1-67b1-3971-a699-743203515e61 | -13.3258 | -43.160099 | 2025-11-13 00:14:00 | METOP-B | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 97663b94-9b1e-3df7-8752-ee84d44bf3f2 | -4.7099 | -46.431099 | 2025-11-13 00:14:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f5a11e26-e78d-3b9c-99e8-df287b217191 | -6.164 | -48.041199 | 2025-11-13 00:14:00 | METOP-B | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 58ef9731-4718-3aab-a8a3-893426c16ac8 | -5.3933 | -48.3218 | 2025-11-13 00:14:00 | METOP-B | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 8084e848-a564-3f5a-a09a-79db6afac263 | -22.648199 | -44.9151 | 2025-11-13 00:14:00 | METOP-B | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8af6dc6e-a2be-309e-ad2b-c4ab9344d6aa | -5.5557 | -47.323898 | 2025-11-13 00:14:00 | METOP-B | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9c952ae3-85cb-36b8-bf72-2701c367a317 | -4.8971 | -45.2463 | 2025-11-13 00:14:00 | METOP-B | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae6e74d8-5a88-3cda-a196-e175f035de2b | -12.0447 | -43.504398 | 2025-11-13 00:14:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ff72620a-330c-349a-b18a-033cf2132d61 | -10.7486 | -44.907799 | 2025-11-13 00:14:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e35eb246-0f2b-310c-8bdd-9de7d6d82ba4 | -4.313 | -48.241299 | 2025-11-13 00:14:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 455aa40e-46a2-39b8-bbda-f858839d6897 | -20.2145 | -41.809399 | 2025-11-13 00:14:00 | METOP-B | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d8a6959e-f7d1-3f68-bc1e-d67c58a79116 | -4.2105 | -48.559502 | 2025-11-13 00:14:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63489a14-4822-346f-90f6-3b9063963955 | -8.3963 | -49.612499 | 2025-11-13 00:14:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c52193b-e8a2-3385-99a9-e888221b8ac1 | -8.2441 | -44.3605 | 2025-11-13 00:14:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 48746eff-920a-3051-a31f-fde397e20204 | -3.0847 | -49.271702 | 2025-11-13 00:14:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54474a2c-f955-3ba0-9baf-ba5d138654b5 | -8.2562 | -44.368198 | 2025-11-13 00:14:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c66c31b2-f5ee-31d4-9443-b3973a7150ca | -4.2066 | -50.081501 | 2025-11-13 00:14:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da90ed28-f40c-3866-8d00-7a7d38603c25 | -5.6222 | -46.898102 | 2025-11-13 00:14:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2b38eeed-259a-3c93-9ce6-5e2ce1bd73a1 | -4.0383 | -46.1129 | 2025-11-13 00:14:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a66d4f0e-ad19-35d5-b6bf-1af9fd64e9e7 | -3.3703 | -48.400799 | 2025-11-13 00:14:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38b1a70c-bf33-3a6b-b99a-382b9529f8a1 | -3.8612 | -49.7855 | 2025-11-13 00:14:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d197560-410c-35ae-9a8d-27cd036930f4 | -3.4297 | -50.4272 | 2025-11-13 00:14:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0be4c1a-f75e-3f54-9723-809431b3907f | -4.2157 | -46.3442 | 2025-11-13 00:14:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 11db1f2b-0a5f-3ae1-b552-7ec809dc442c | -5.0847 | -47.9202 | 2025-11-13 00:14:00 | METOP-B | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0ecb4bab-c97f-3dea-ba22-2b4c0260ef8d | -4.8898 | -48.9608 | 2025-11-13 00:14:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40e2056e-73da-37f3-91b8-a5e097663692 | -3.1618 | -50.609001 | 2025-11-13 00:14:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83c9a22f-fb7a-3a5c-97c2-4994c049503c | -3.8643 | -49.799099 | 2025-11-13 00:14:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b13c34a-ca42-398f-93d2-2d0d03f7b54c | -14.1025 | -44.194302 | 2025-11-13 00:14:00 | METOP-B | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 01a9c969-09be-37d0-a8ab-865eb241dc8b | -3.1447 | -50.2612 | 2025-11-13 00:14:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
