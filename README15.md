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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a50badd-3ad1-3433-b741-cecf58729963 | -5.49544 | -39.0734 | 2025-11-09 04:16:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 78282b60-ba78-389d-81bb-28077a2e8db4 | -3.32492 | -49.13064 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35974d98-0387-39f4-96c0-0a233b8c262b | -3.58328 | -41.66065 | 2025-11-09 04:16:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 819280c7-099b-3ce2-8bd4-0415f8524fe1 | -3.13773 | -50.27404 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d787e6ad-30cf-3812-a180-2bd2af43ee7b | -3.68961 | -51.38595 | 2025-11-09 04:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cebd3217-1597-37e9-8062-b8f1a0b05382 | -3.33622 | -44.37108 | 2025-11-09 04:16:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 54d63311-2bef-396c-8903-bd29aadee5b4 | -3.61497 | -49.27645 | 2025-11-09 04:16:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08108b4f-7cf7-39ea-b2a1-90fb13f2d397 | -5.06532 | -40.47324 | 2025-11-09 04:16:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 416d814c-aa06-3c72-9b5e-9a2e0d8ec456 | -3.84713 | -50.74562 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ea50ac2-cc46-3061-9df9-abe8d32ed996 | -3.33219 | -44.37425 | 2025-11-09 04:16:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| abc769d1-26c0-3d64-9435-3a0cfb635b63 | -3.61522 | -50.15719 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e824f9d8-2d7d-36d4-bfc6-7545f557bd8c | -4.24488 | -48.38071 | 2025-11-09 04:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f4fa0a1-1cb2-393a-aee0-e994ea7dca2b | -3.5906 | -49.33876 | 2025-11-09 04:16:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87813295-5ee0-3804-89e1-bdccebd355a7 | -4.9056 | -44.64493 | 2025-11-09 04:16:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd797e00-dfc0-3575-9ca4-6889f57eb753 | -3.31011 | -50.12247 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13d6c63f-8fcc-39d7-8d80-048ecbf11f10 | -4.05646 | -46.43268 | 2025-11-09 04:16:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a645779-b925-363a-b276-054470d60f5f | -4.70948 | -46.45735 | 2025-11-09 04:16:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8fd15ca8-7ac5-3050-889a-c8bcb7e4c6ef | -4.40438 | -49.65818 | 2025-11-09 04:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d3cdd3dd-e3f1-3601-9755-dad4b1dc3bfb | -4.64846 | -44.00827 | 2025-11-09 04:16:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37ea3027-f324-3d6e-b698-2ff9e96d4b7f | -4.68193 | -45.68954 | 2025-11-09 04:16:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04f0d563-a358-3c6d-8527-036dcc566089 | -4.45851 | -44.64392 | 2025-11-09 04:16:00 | NPP-375D | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6e0c07a8-435c-31e5-a879-30f00b53418d | -3.32651 | -44.36568 | 2025-11-09 04:16:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d3b402c9-16ae-3aed-ad60-05d5929ec778 | -2.63802 | -47.30347 | 2025-11-09 04:16:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 37526f41-2cb0-31d0-a368-805075bde537 | -3.49832 | -46.3021 | 2025-11-09 04:16:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 90bd64c5-11d8-36a3-88c2-55176d72eb2d | -6.28714 | -38.87614 | 2025-11-09 04:16:00 | NPP-375D | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c67c0f7c-6de2-3c5e-bb88-048f512c8ebb | -3.09971 | -49.24982 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 306bfedf-4087-3840-b634-83cf1479177d | -3.13278 | -49.10342 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bae8b382-dcc6-31d9-8e05-1939d4168d68 | -4.20558 | -44.75882 | 2025-11-09 04:16:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 67862d26-821c-3357-ab8a-1f4400a2752c | -4.28389 | -49.90608 | 2025-11-09 04:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c31f4c53-92b2-3349-93e2-49165c651917 | -4.28709 | -50.66172 | 2025-11-09 04:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c9d5aebf-4e95-38fa-9a7e-2b9801aed177 | -4.38192 | -45.49549 | 2025-11-09 04:16:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75e03cbf-9da6-37b6-8040-08d69e28428e | -3.46517 | -48.82079 | 2025-11-09 04:16:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ca835d03-9cdc-36ef-8869-691793ad4ecf | -4.1193 | -49.80238 | 2025-11-09 04:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fcf9da8f-999b-3e93-b54c-238ea72cbc21 | -4.71322 | -46.45793 | 2025-11-09 04:16:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| de33d508-93dc-3739-b204-6966b63d47f8 | -3.40997 | -50.45576 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c9ab7bff-1641-3acd-be5b-c4e5793755d0 | -4.31616 | -43.20952 | 2025-11-09 04:16:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60f7dccb-ca0e-3bef-89fa-f7c1e90d1b51 | -4.03343 | -43.17569 | 2025-11-09 04:16:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 16f45fb8-0b6e-3427-a69a-15b72279ad99 | -4.72497 | -42.93331 | 2025-11-09 04:16:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf629b9e-599e-3aea-b561-de75cfd89636 | -4.64124 | -46.39787 | 2025-11-09 04:16:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5097c911-e3ed-3138-be31-adf48f27d603 | -4.40358 | -49.66295 | 2025-11-09 04:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 24eb705a-8a0b-3c51-8b1c-6dc1084345ca | -4.45447 | -44.64709 | 2025-11-09 04:16:00 | NPP-375D | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 6345961f-bcb6-3bf5-96ec-5c1a1d73a9c3 | -3.09666 | -49.26861 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 21b20840-7f50-3020-862f-577443bdbe73 | -4.12402 | -47.2905 | 2025-11-09 04:16:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c55822c1-a30c-37f0-b1ca-49e3e49d4b0e | -3.47727 | -49.93261 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 62150d0f-2dc0-3746-bd35-c7ff1cbf1c5a | -5.38459 | -44.73076 | 2025-11-09 04:16:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a52a26fe-98aa-322e-be96-7facf9a12923 | -2.43202 | -48.04427 | 2025-11-09 04:16:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6bef62c8-e6b6-3375-8a22-db1bb250e313 | -2.70991 | -49.54537 | 2025-11-09 04:16:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf68cd15-5d29-3c52-8ea9-c5b478a4d790 | -3.61573 | -49.27185 | 2025-11-09 04:16:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86e22e6d-7bde-3bf3-8b9f-d92b800b0a08 | -4.46135 | -44.6482 | 2025-11-09 04:16:00 | NPP-375D | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 3de2005d-d15a-327b-ac4d-27ff88b5c498 | -4.12006 | -47.28991 | 2025-11-09 04:16:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b4bb1b0-8cbd-3142-9593-b8d3a623dad0 | -3.51188 | -40.35982 | 2025-11-09 04:16:00 | NPP-375D | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9dbf8d07-0283-35be-98fa-011a0ee2b8a9 | -4.82888 | -45.61271 | 2025-11-09 04:16:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef511e5d-d8ba-3fab-932d-ffd1e94d35b7 | -3.84852 | -47.39973 | 2025-11-09 04:16:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5c8a4bd-5509-3ce7-85b5-5b1c7566c995 | -3.64351 | -49.87303 | 2025-11-09 04:16:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e2ac738-bcf6-3610-968f-961c31cc471e | -2.9473 | -53.28858 | 2025-11-09 04:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dfb8b3af-164d-308d-9462-4a8eb21b31b1 | -3.66042 | -50.27427 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1d2ac320-c755-3550-a0b5-ceee5ff99ea1 | -2.97321 | -41.68348 | 2025-11-09 04:16:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3543500c-4dd5-334a-86ce-b00d202f15f3 | -4.85564 | -45.78775 | 2025-11-09 04:16:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e3754fc-3b77-3ac5-89a1-1938a4ae792b | -3.45118 | -49.97079 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 672ec041-0492-3e5e-87a7-b069039e92e3 | -4.45791 | -44.64765 | 2025-11-09 04:16:00 | NPP-375D | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 208e3737-14ec-3178-9a00-186c214e0c96 | -3.89752 | -47.18598 | 2025-11-09 04:16:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c46abc85-b84a-3206-9987-00b8a6db4668 | -3.53777 | -50.85345 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ca0a8469-6ba6-3262-89d2-e0f9cab17242 | -3.7681 | -44.29039 | 2025-11-09 04:16:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 514009da-b90e-37e0-af9c-906a475f25e1 | -5.37122 | -44.61937 | 2025-11-09 04:16:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 57dbe493-7ed9-3fcb-8493-ef6a84749dae | -2.44372 | -49.2247 | 2025-11-09 04:16:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e38eacb1-5a76-3343-a5c9-6de87594f1a5 | -4.54481 | -44.60756 | 2025-11-09 04:16:00 | NPP-375D | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56793381-37b5-3114-b474-aed01ae354f0 | -2.94218 | -49.35341 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 900f31b7-c5f7-3372-9f59-4229d7db3b7f | -3.84363 | -50.74437 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b339c8e6-077e-3308-a50f-c7b895b29b37 | -3.13732 | -49.10418 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b26c53a-f944-3750-a984-36b456ab8d28 | -3.06971 | -49.37605 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 40bdf7a6-77d9-34ae-809c-e81405969e3d | -4.63823 | -46.39288 | 2025-11-09 04:16:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 521b4a6a-5d13-3e2e-be74-43dbbaf6dd4c | -4.0527 | -46.4321 | 2025-11-09 04:16:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 21af6bd4-b37c-31f0-8698-09c29413e715 | -4.84334 | -42.37789 | 2025-11-09 04:16:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7a6fbe60-930c-3e54-97c8-8bfd78f88660 | -2.61662 | -49.22379 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3607687-51e5-338e-acae-7318928c879b | -2.48792 | -54.19963 | 2025-11-09 04:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 224f0245-1e0f-3336-8558-abd83ba82282 | -3.32994 | -44.36623 | 2025-11-09 04:16:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| bae3597c-02b9-3943-bd9b-4bbb07130a0e | -4.80886 | -38.69374 | 2025-11-09 04:16:00 | NPP-375D | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 618a5203-3038-37a4-87a9-c5b4033ff2b0 | -4.47122 | -46.45042 | 2025-11-09 04:16:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2d02c39-c9e7-3cc9-9513-696013a7d1b2 | -3.32307 | -44.36514 | 2025-11-09 04:16:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3467b258-41bd-31ef-a99a-5cdf191399c8 | -4.5847 | -49.38986 | 2025-11-09 04:16:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7b6c7134-2d57-31d2-a2bc-65e7eb02dbb3 | -2.91803 | -40.00687 | 2025-11-09 04:16:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6e795505-8487-354e-ab83-b99ba724182d | -1.79 | -48.07102 | 2025-11-09 04:16:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d2bdfff-1702-3c1c-9d57-28e98295444c | -4.58594 | -45.61714 | 2025-11-09 04:16:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b9a663d-372a-3b13-a48b-6b1fa49731fa | -3.83367 | -42.51657 | 2025-11-09 04:16:00 | NPP-375D | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e241176-1976-37ba-ab43-a74ebdadf364 | -4.27919 | -49.90526 | 2025-11-09 04:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 351f6bf1-8825-3fb7-b8be-e8a91ed7ecc5 | -3.30617 | -50.01426 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aaa3dda2-51c7-37e1-a8a2-2f4238807d4d | -5.91773 | -42.71055 | 2025-11-09 04:16:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 84101d3f-869e-38de-a90d-70cf894d9a15 | -3.33185 | -53.24958 | 2025-11-09 04:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5084887-89a2-337d-9223-89aba8d9cfec | -3.14577 | -50.28669 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b1664f6-94fc-35a2-877a-5049a5ea7b7b | -3.58339 | -51.24963 | 2025-11-09 04:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e4e83b8-26a3-383b-9146-820d5ab24211 | -3.34854 | -50.20684 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 02689446-506a-32de-ae30-845afd592046 | -3.88918 | -47.18151 | 2025-11-09 04:16:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba77d868-b0ee-3264-9639-a4e26e00408d | -3.50148 | -50.05423 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 34acdb4d-07ea-3939-9fa4-1b5c672701f8 | -2.63437 | -49.52576 | 2025-11-09 04:16:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ae2b1d3-699c-3a84-bd31-fd542138f3c7 | -4.11609 | -47.28933 | 2025-11-09 04:16:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c16e00b5-537c-37d9-9f47-fde9f928d1fc | -3.99283 | -50.4374 | 2025-11-09 04:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4d36210c-9414-3783-9519-06b4813ce677 | -0.81407 | -47.1526 | 2025-11-09 04:16:00 | NPP-375D | SÃO JOÃO DE PIRABAS | PARÁ | Brasil | 1507474 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11e00372-358a-379c-a724-51154cd101a6 | -4.39515 | -49.65659 | 2025-11-09 04:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ab85472d-dc5a-3f21-acce-ddd784a597f2 | -3.83466 | -51.12688 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cb9be9f1-a77f-306e-bf5a-ed01a690b3cb | -3.405 | -50.45496 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |


[Clique aqui para ver as próximas entradas](README16.md)
