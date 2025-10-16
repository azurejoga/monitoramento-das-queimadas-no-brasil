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
| a09060ed-8076-36da-a6c0-7f8591940198 | -10.65504 | -45.25142 | 2025-10-16 03:47:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 486658e3-6d4f-32a0-9763-a7b90935c565 | -6.33172 | -44.01237 | 2025-10-16 03:47:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 271f3273-768f-3dd8-8a71-633f405a5e61 | -6.15282 | -40.90574 | 2025-10-16 03:47:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 982fe3ce-8e36-38cf-9a72-2cdb0b6e0b44 | -6.76317 | -37.77174 | 2025-10-16 03:47:00 | NOAA-20 | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c202dbd1-6900-334b-9967-e52c6f2a0509 | -10.86238 | -44.41366 | 2025-10-16 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 82a3cdd0-437d-3cfb-ae8d-782855ceeca2 | -9.16035 | -46.87738 | 2025-10-16 03:47:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1af70959-7df4-33da-9450-a39d17906238 | -6.13089 | -44.2911 | 2025-10-16 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07f6f2e2-f555-34c4-b24f-1645b424ba54 | -12.48673 | -45.48473 | 2025-10-16 03:47:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c66ea07f-66bc-30e2-89ae-1e0330ae0cca | -5.43154 | -40.98557 | 2025-10-16 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| d5e155f8-1aa6-3443-8a6c-6ad875eb01e3 | -11.44486 | -44.17023 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2fbdc55-2534-391e-8a57-6f9eaca55dd9 | -3.01045 | -45.38893 | 2025-10-16 03:47:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 9b290de4-dfa3-3324-a160-85be4403fbd5 | -4.38534 | -43.39471 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 45.8 |
| b389aa2f-10fa-3cc6-85f6-a382b278ab96 | -6.14244 | -41.74424 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 26adb8ca-dde7-3731-a761-491c1c50ac61 | -10.50756 | -43.38645 | 2025-10-16 03:47:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c758ad82-c255-3705-bd1b-c0ea9636dbdf | -3.27404 | -45.84041 | 2025-10-16 03:47:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57db1f3b-ff25-363b-b204-9cc0989c265c | -11.59385 | -48.5589 | 2025-10-16 03:47:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bc69233d-a122-3a5e-b380-bf3aad5d7729 | -5.65899 | -45.96149 | 2025-10-16 03:47:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d009ed42-4b4f-3b10-b730-0235047d3fa6 | -1.37834 | -49.31299 | 2025-10-16 03:47:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 08973eda-a4ab-3a17-abb0-6a873fa6b5a2 | -6.23769 | -41.5498 | 2025-10-16 03:47:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ea0ed339-5d5f-3a67-b2a4-38754ec19d23 | -6.0593 | -44.3112 | 2025-10-16 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2431d27c-eaae-3cf6-b409-453fdf3a38a4 | -6.52904 | -42.20784 | 2025-10-16 03:47:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 92a8fd8d-8a2e-3f4e-9c89-6eaed79e72b5 | -10.27702 | -44.02126 | 2025-10-16 03:47:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 001e9dbf-767c-353f-943a-1d7d99b30cc0 | -5.453 | -41.0261 | 2025-10-16 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 80af4a27-69d5-339b-9b81-5fafab1f19bf | -11.13069 | -45.84862 | 2025-10-16 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 70c6f81d-b1a2-3ea5-aede-f0235106874d | -6.38745 | -41.47717 | 2025-10-16 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 16d000df-1981-3e12-bf27-1c0e3d25c45a | -5.86948 | -43.89482 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5351a0ef-46b9-3085-afc9-2338fa4a9214 | -5.88332 | -42.78064 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d39bd3bd-cfcb-3c49-9e0b-bc026b00103a | -5.86532 | -41.23042 | 2025-10-16 03:47:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9ef7606e-a9b7-3793-9ad1-f50c923f5f33 | -11.58873 | -44.0757 | 2025-10-16 03:47:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d638c84c-feaf-311f-9179-f448ac0a2081 | -10.87919 | -48.80378 | 2025-10-16 03:47:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| dc737732-41cd-3568-b7a0-af1711c711ef | -2.26525 | -47.85705 | 2025-10-16 03:47:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c9c83016-bd38-3128-9ccd-d21f598d8096 | -6.64552 | -41.731 | 2025-10-16 03:47:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8c501034-1a3a-3e3e-ba12-fa95f13db8d7 | -4.92576 | -41.55483 | 2025-10-16 03:47:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fc104acc-c2c9-3f4e-8ef6-4e9ccc069d09 | -5.25649 | -35.80895 | 2025-10-16 03:47:00 | NOAA-20 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5b299511-afa5-3739-ade8-1d17bc23125f | -11.47763 | -47.64378 | 2025-10-16 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 003ec94e-a095-3971-bdb8-312f9e2b7e4c | -5.65352 | -45.96054 | 2025-10-16 03:47:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c05d464d-1e33-3fd7-98c4-883f9cf71d71 | -6.44144 | -43.38374 | 2025-10-16 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0d159be8-294a-3f7d-9cf4-c174367f9b36 | -5.91613 | -44.72891 | 2025-10-16 03:47:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a7cb4428-d260-3848-94c5-cd0f609ea652 | -5.29687 | -41.17517 | 2025-10-16 03:47:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d5e14341-68af-3bc9-bec0-4595bae10bfe | -3.83596 | -44.54612 | 2025-10-16 03:47:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f5f69f69-b5fc-3c3b-bda7-63b329b93292 | -6.13832 | -41.76897 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0644be2e-a389-305f-bbf4-af8733ba9773 | -4.37511 | -43.39822 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| e5383ed4-cd39-37fe-92ad-e596ff9cefeb | -2.79522 | -48.94815 | 2025-10-16 03:47:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 865d761e-f29c-3c5f-bca1-38df05c0d9fa | -11.57551 | -48.55956 | 2025-10-16 03:47:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2e3c4a1-7493-395f-ad9a-fee32ae87617 | -6.36911 | -41.48845 | 2025-10-16 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 26.1 |
| 35a10523-39c5-3368-b137-1da271f9fda4 | -6.1269 | -44.28524 | 2025-10-16 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5cccb04c-756c-3041-84d4-555a0a3448c3 | -10.05357 | -43.85574 | 2025-10-16 03:47:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93e8a87e-9c30-390a-b87b-c4e88fea5f56 | -6.39088 | -41.48123 | 2025-10-16 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 13f07714-1e5c-3f1d-bd51-340522a01404 | -6.68868 | -40.87916 | 2025-10-16 03:47:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1d8ed0e9-7ad4-3b08-bdaf-165d3e45c90d | -11.42371 | -44.06089 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1eecaef6-fc8b-3a2f-a106-28a7061f19a6 | -5.89654 | -42.83501 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3966eb84-6e05-3da1-8725-f90b5558d2ec | -5.86315 | -43.84658 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db5a8ddd-e61b-3995-9254-2e3679d35129 | -5.13407 | -43.35424 | 2025-10-16 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13e89ea1-97a8-37d0-9357-3e798ac5a72b | -4.36184 | -43.3908 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 0c920730-ebc5-3d3a-a406-0abc95c7e479 | -5.2446 | -42.00513 | 2025-10-16 03:47:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6f9c0a9a-e7c9-3931-bd1f-fc2714f4358f | -5.57143 | -41.31113 | 2025-10-16 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6693239d-c3f2-344f-8bdc-23f58ef08a5b | -11.42719 | -44.06859 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc3d3672-143e-34f9-bb2d-1cda4376e8a7 | -9.71499 | -44.52813 | 2025-10-16 03:47:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 198c2eca-7a42-3e19-aa96-1759a86ebcbb | -3.07349 | -49.5108 | 2025-10-16 03:47:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e74e4082-ddae-3087-a147-3d065bf71342 | -5.41231 | -40.8848 | 2025-10-16 03:47:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 61d2d1e4-fdfd-32aa-9789-e9a843e32b8d | -5.42371 | -44.2372 | 2025-10-16 03:47:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c04438f-f012-3662-919d-7ea8151cc2f1 | -6.19547 | -41.74942 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8cb9dd4e-8858-3513-ac3b-454198c57e6c | -4.3829 | -43.39096 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| e2cf4a8f-78b6-3597-9a17-7e0d5a06b8b4 | -10.59842 | -47.4257 | 2025-10-16 03:47:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2c812e9e-d259-3c67-8de1-3ba5240ce66d | -6.32385 | -42.76394 | 2025-10-16 03:47:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6898ee7f-746f-3e05-b659-b18df85624d7 | -4.81977 | -46.84451 | 2025-10-16 03:47:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ca7d581b-12b6-3c5c-b847-ee378dac06a5 | -6.16139 | -40.90199 | 2025-10-16 03:47:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| a61a0984-7150-3daa-8b35-06ce24390aca | -5.74235 | -44.98429 | 2025-10-16 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91bdd7a5-91a5-3077-aa2a-9d74886c8198 | -10.12708 | -44.56811 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1089ab9-d2f3-3674-b582-02ba523a26b4 | -10.83666 | -43.95339 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fdadc42d-5c7a-3038-b137-4f6cba506f5e | -6.03712 | -41.92933 | 2025-10-16 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a2554bac-e03c-3657-a504-05b49fa59e11 | -6.10252 | -40.89024 | 2025-10-16 03:47:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| a6f45977-503d-3530-ad93-2defaa43daa9 | -9.71004 | -44.50184 | 2025-10-16 03:47:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 67095949-5c99-3664-89c8-ffd1e681ff32 | -5.46908 | -42.8788 | 2025-10-16 03:47:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f1b365b8-6fdb-37b1-a4bd-8deef44a700d | -12.85264 | -43.81617 | 2025-10-16 03:47:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d68bcdff-25fb-3d49-8c48-264cef8f0696 | -9.37299 | -46.95671 | 2025-10-16 03:47:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 53d79f71-17b9-3e34-9dec-cca2226ac244 | -5.44855 | -41.00442 | 2025-10-16 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 995805c3-37d5-3cda-bb1f-2e214ded6ef4 | -4.95993 | -45.1038 | 2025-10-16 03:47:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7284b6d4-5dd8-3720-a7a5-d14af33dfe9c | -4.85503 | -42.53383 | 2025-10-16 03:47:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fc684e72-0b54-3d98-b3ce-ff2f75600734 | -3.60971 | -41.58704 | 2025-10-16 03:47:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0bcf005d-139c-3566-b837-35b30a748de1 | -9.71656 | -44.51089 | 2025-10-16 03:47:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 61f38486-c5fd-3198-9e63-b8af0d3b3372 | -3.84806 | -41.56347 | 2025-10-16 03:47:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0f111e73-6431-3c63-a2b9-aa883376e655 | -11.54185 | -49.92437 | 2025-10-16 03:47:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 78bbd411-0268-3910-9375-db4718a61bf1 | -5.14605 | -45.214 | 2025-10-16 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0bb40e7-4d55-3dc8-8390-fb2c93d5fa33 | -6.40053 | -43.48746 | 2025-10-16 03:47:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d8ad2621-29ee-3702-884d-f1bfaee2539c | -5.85435 | -44.67117 | 2025-10-16 03:47:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e7e87aa-e29c-3f7e-96c7-826af0e8d69f | -9.3689 | -46.94839 | 2025-10-16 03:47:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9bce3b9b-78d6-303c-b43b-31353a514965 | -6.90583 | -38.25832 | 2025-10-16 03:47:00 | NOAA-20 | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 738c2d6a-fb4d-3cec-b2b3-337f80c77e78 | -5.90395 | -42.81833 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7185f174-58b8-38c2-a128-e6d3c59962c7 | -6.46642 | -41.85371 | 2025-10-16 03:47:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c708dce5-0656-3666-9b4c-6c7a5da7ba93 | -5.85702 | -42.88407 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| bd9abd67-a870-3c35-8bba-dc80dd49d06b | -5.88228 | -43.8771 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3e3eb4ea-c0a8-310d-9eea-aceb7c968ea9 | -4.65385 | -44.11109 | 2025-10-16 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07346c5e-5e1b-3574-b8fc-7c0f9fd9427f | -4.56298 | -44.00885 | 2025-10-16 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 437c21c6-f660-3d09-989a-b655d77cb26b | -5.50757 | -47.31013 | 2025-10-16 03:47:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 451c86d0-9ce9-3ed0-854b-6175a62f7c85 | -10.61471 | -42.31718 | 2025-10-16 03:47:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 28c42418-8399-35fb-a5fe-9b37acadc31b | -4.92747 | -45.90067 | 2025-10-16 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 358bcdfd-8858-3527-8e10-ca56fce457ad | -7.19445 | -39.26937 | 2025-10-16 03:47:00 | NOAA-20 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 59e179d7-b725-3ec5-ae77-e8d373d11cae | -5.47335 | -42.93444 | 2025-10-16 03:47:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 0c24bdda-9751-3dc3-b224-70a9012a8b04 | -5.87033 | -43.88988 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README22.md)
