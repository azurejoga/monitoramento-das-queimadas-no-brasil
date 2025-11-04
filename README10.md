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
| 7d614a33-4571-39ff-8c36-cf1f0c4286f3 | -5.43179 | -46.36351 | 2025-11-04 04:10:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 531af97d-8fca-37d3-b89f-e24c2ec7e0d6 | -6.41859 | -43.07317 | 2025-11-04 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aa289280-beea-36dd-bf92-1eec6e772d7e | -2.31697 | -48.58245 | 2025-11-04 04:10:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c1bf520b-5da0-34d4-b06a-8b7d9a7a4e55 | -2.65267 | -48.50178 | 2025-11-04 04:10:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d609f493-75f4-3e6b-9a63-e89ebc4b60b6 | -4.38318 | -46.27429 | 2025-11-04 04:10:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a0f14114-a14c-3932-ba94-596f648db1b8 | -2.72274 | -48.34879 | 2025-11-04 04:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 957c06aa-2393-3093-98ba-b27cddeed78a | -5.57851 | -43.7944 | 2025-11-04 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 460b2ba6-e325-30dc-bbd1-884103a98f48 | -5.87872 | -44.35006 | 2025-11-04 04:10:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c189168-8d69-3b61-b113-fb8bce0b638c | -3.4889 | -50.31677 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac17fd54-a77d-35f7-bb45-bb82313e649b | -3.24425 | -50.79938 | 2025-11-04 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64f937af-7cb6-301f-aa27-407c1cb86f54 | -6.4836 | -39.42014 | 2025-11-04 04:10:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8385cbc8-7e98-37e9-b9da-630153976fce | -7.22194 | -39.9527 | 2025-11-04 04:10:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2496398d-5cac-3dde-82fd-d814460f592c | -5.23415 | -44.20642 | 2025-11-04 04:10:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3fa232b7-691d-3ec4-affc-fd24d64efb36 | -2.86852 | -45.29247 | 2025-11-04 04:10:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45ed47df-d3e6-3365-8d0f-b5464833bc40 | -5.6141 | -41.10374 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2fe67f45-1adb-32e3-aa51-96d123904061 | -5.23642 | -44.2151 | 2025-11-04 04:10:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb8f5176-7316-3836-b897-98fced10ddd6 | -6.43393 | -43.06846 | 2025-11-04 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33340423-3203-3980-bd1d-87d33989aad7 | -5.03592 | -43.62029 | 2025-11-04 04:10:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 62a4740c-6af6-3aaf-ba31-536912aed47f | -6.34363 | -42.36998 | 2025-11-04 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fbf664a3-c27b-3adb-9ced-668fdd34ad39 | -7.16627 | -40.08675 | 2025-11-04 04:10:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| cea45c51-ffef-3675-b248-bc252c3a2f57 | -2.29209 | -47.86848 | 2025-11-04 04:10:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 622e0f5b-1fec-3f31-bc42-99b7204f74d3 | -5.83218 | -44.66203 | 2025-11-04 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 82761b90-bdd5-352b-8673-288f37627cbe | -2.60943 | -46.91473 | 2025-11-04 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85201ae8-9096-3c70-a10f-4e33b8cb54a0 | -5.83425 | -44.06306 | 2025-11-04 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44677f70-0df8-3bdc-859d-544ed04c9447 | -3.76784 | -42.63531 | 2025-11-04 04:10:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 506a8687-6b05-315f-b9dc-f56fa78e7d3a | -5.19297 | -45.27171 | 2025-11-04 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6d852eb0-b0f5-3efa-a225-42a78dbf3bf9 | -3.38784 | -50.28222 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0520d08-816d-3fc1-bac2-bda7c9c0012d | -6.61108 | -43.61471 | 2025-11-04 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 31f1c5a6-eb7f-3d0a-9a8c-c548b4e919ef | -4.594 | -44.60891 | 2025-11-04 04:10:00 | NPP-375D | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a96dd9f4-bee9-3a78-ae51-d831a1512d28 | -3.0171 | -51.08915 | 2025-11-04 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b43a0c6f-9512-36ee-a105-569f8353320a | -5.41332 | -45.29171 | 2025-11-04 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae4623c3-b350-36d7-90c6-2bf65946ff7e | -3.43891 | -50.24725 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e4799b9e-9c94-3126-861b-e4a4465be136 | -1.22965 | -49.15642 | 2025-11-04 04:10:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de3c4a10-9e4e-332a-92de-cacdd00b405c | -3.01678 | -48.05007 | 2025-11-04 04:10:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c07b541b-9eed-39ef-8b9b-6e790c0b420d | -5.43122 | -46.367 | 2025-11-04 04:10:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79272501-ad9f-3853-866b-96650f0ca20f | -3.6936 | -49.56705 | 2025-11-04 04:10:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7045fcde-03ac-3b73-8f3a-5278058eb15b | -3.49576 | -50.47866 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e3e7b04-85c3-3f98-b234-0b6106cad3c7 | -6.43335 | -43.07206 | 2025-11-04 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b6cd23b0-2b66-3424-80b6-775cbbe9b936 | -5.31473 | -43.52888 | 2025-11-04 04:10:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b65be87-708e-3ab2-845f-ad374e75df73 | -1.84465 | -47.94513 | 2025-11-04 04:10:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8f579994-60a3-3ffa-b0d9-75d983ff2d56 | -4.48522 | -45.8815 | 2025-11-04 04:10:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f6e668f4-2107-37c9-b577-9dc0cdf2ca2f | -3.50187 | -50.47613 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c0ffacd0-6e52-3e84-9151-487fb5ce4cb2 | -5.32164 | -45.37842 | 2025-11-04 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9789a192-e7e0-3495-a0e0-4a7c1d488fa1 | -2.49173 | -45.97178 | 2025-11-04 04:10:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cce42369-5be7-3320-a356-b0a4f8c67d84 | -5.06176 | -45.90851 | 2025-11-04 04:10:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 39387fd9-28a2-30eb-8879-7e98256821a3 | -3.02219 | -51.0943 | 2025-11-04 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7476abb-5903-3245-84e1-805fd8292a08 | -5.22904 | -38.60289 | 2025-11-04 04:10:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8c6a8051-6df6-372a-ad5d-c923ddfe6d90 | -4.87352 | -47.54432 | 2025-11-04 04:10:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b10c96e-8eb5-31ae-aac9-10c634cda0d9 | -3.60101 | -50.62233 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6d8fdbd-f51f-3bfe-adae-5f139c4c4599 | -6.41048 | -42.31587 | 2025-11-04 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b7e02950-64e9-3e18-af92-8548a5f07a99 | -4.05691 | -42.37919 | 2025-11-04 04:10:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cd8de4f6-7330-3b4d-9e1d-4e68e92d2998 | 0.9767 | -51.21696 | 2025-11-04 04:10:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 146584a8-7db3-3b26-82e6-ced3fd516210 | -5.58202 | -43.79496 | 2025-11-04 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d23f37d0-7636-3d45-8f39-65351b272f8b | -4.57201 | -45.86152 | 2025-11-04 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67e039a2-d3e7-3b6b-8d8b-da715c01c233 | -3.70448 | -49.56562 | 2025-11-04 04:10:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| af383559-fd07-342c-9ed0-fe98f303f063 | -6.31647 | -43.8099 | 2025-11-04 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 44022120-c8eb-36ae-926e-1d0d829ba6bf | -4.62308 | -46.40373 | 2025-11-04 04:10:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c571570a-65a7-3faf-8156-4fc071f3d69d | -4.9587 | -44.9082 | 2025-11-04 04:10:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 38a9a717-f8f2-3b95-88dc-3d7062891877 | -6.32533 | -46.32298 | 2025-11-04 04:10:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d623cc30-d174-3b64-a8f7-f9b07d6cb6cd | -5.31191 | -41.23714 | 2025-11-04 04:10:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d36d8508-01b5-3c5b-a255-2826f8449e42 | -2.37457 | -47.72374 | 2025-11-04 04:10:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1895b9b2-2d83-3fe8-920f-99f10ccb5f13 | -3.23861 | -50.79835 | 2025-11-04 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd0c0db4-9ec3-3b19-8077-73437981b789 | -5.57914 | -43.79053 | 2025-11-04 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 783975a0-a90b-34ae-8b2d-4096952d6cce | -5.9222 | -41.31931 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2436b49a-85bc-33c7-9744-b7a5b125d63c | -5.69436 | -43.5415 | 2025-11-04 04:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3df3119f-018a-36a3-83b2-0e96e016e020 | -5.92275 | -41.31585 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1d8d210c-6eb4-3592-a63a-845e07f12ea0 | -4.22262 | -41.77158 | 2025-11-04 04:10:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a3e5d5f4-bff2-3107-b185-3d3872ca7d3b | -5.92498 | -41.32329 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2e841784-ec28-313e-b471-6dc5d887a494 | -3.46231 | -52.87302 | 2025-11-04 04:10:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 662878c8-e6e5-3e0c-bd55-d900c8e2163d | -3.48976 | -50.31653 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4e2dd4ce-eeda-325d-a266-71e6971e971a | -3.15817 | -46.58801 | 2025-11-04 04:10:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9f1c94f-b618-340d-9e43-41597ab2bd1a | -3.49892 | -50.46019 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f81dca0b-91e7-3255-aed8-c5b804f21357 | -3.50376 | -50.46502 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 525d11e8-7e7d-3330-8271-91313fd2dc6f | -3.91373 | -47.7015 | 2025-11-04 04:10:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9e1bebf5-ce3f-3e24-b67a-792cb37ddcc2 | -3.91856 | -45.21574 | 2025-11-04 04:10:00 | NPP-375D | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5940f7ea-d907-3791-980b-c0e96979eccd | -3.98764 | -47.08479 | 2025-11-04 04:10:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00553f9b-2f0b-333a-a6ff-d5fc64ec7b18 | -5.43237 | -46.36001 | 2025-11-04 04:10:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4bdaf9c-c490-3d6d-825c-1f3539e1a307 | -5.07069 | -47.11496 | 2025-11-04 04:10:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48816668-99e0-381c-8921-57125e8fb0b1 | -7.16446 | -39.50973 | 2025-11-04 04:10:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9c4c7587-0944-3954-aa26-087b2a57c7ce | -4.02292 | -51.01492 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e3344e8-1e3a-3b32-99f2-1f0d52ca7615 | -5.18919 | -45.27102 | 2025-11-04 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9180d18-893b-3a6a-bf2a-7a0b8515aee4 | -3.92429 | -47.69382 | 2025-11-04 04:10:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| e3275461-804f-357c-9068-ac6ef91caa36 | -4.91901 | -47.326 | 2025-11-04 04:10:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ca23a44-5d16-35b1-b772-81e7046f6c34 | -5.61132 | -41.09975 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9e98f080-4d45-3f8a-94ce-e2901ac7938e | -3.49278 | -50.46291 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bf43fbc8-16d1-3fd5-a71d-d61f48f1d104 | -5.51094 | -41.11599 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 50fbda5f-f822-38dc-9db0-ee7ddadcab54 | -2.10579 | -48.05392 | 2025-11-04 04:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5888042e-844e-37e8-9b7b-6e982cd719f3 | -3.41659 | -44.43801 | 2025-11-04 04:10:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 738b08d7-b04d-38b4-9c4f-c7624011e7b4 | -2.83873 | -49.82942 | 2025-11-04 04:10:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c25a2b2e-9c78-35db-bd1d-65cae2a0ca04 | -5.65679 | -44.0683 | 2025-11-04 04:10:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 341aad9f-687e-366d-82fe-379664b91f8a | -4.88916 | -45.86512 | 2025-11-04 04:10:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 96906c15-feb7-3e95-950f-ba7f72d888ed | -5.28438 | -44.6106 | 2025-11-04 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3d42ad2c-f8c8-36fe-8fdb-910e9a86094d | -1.97025 | -52.10524 | 2025-11-04 04:10:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31aa1740-9c4e-37fe-9dc4-bef9369a681d | -3.44362 | -50.21951 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d39a33ba-8106-3b25-9461-f79b9ff433be | -6.17493 | -43.06846 | 2025-11-04 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bcbba52a-8900-3b44-8a8f-179adaa707c5 | -1.84453 | -47.94899 | 2025-11-04 04:10:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 03f5ded7-8493-3d2c-a64d-1f212ba7a520 | -4.8728 | -47.54859 | 2025-11-04 04:10:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68665910-0f22-3fc0-bb69-17d784140262 | -5.32546 | -45.379 | 2025-11-04 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e7aedaf-35a3-3176-ac19-bdaa27cd43df | -6.41917 | -43.06954 | 2025-11-04 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ed0377ab-f456-39c8-a8a0-f595b1f45c06 | -3.44552 | -50.24123 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README11.md)
