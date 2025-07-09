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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c2b8dd1-2a8e-3607-8f71-50d813b4d52b | -8.51454 | -43.28462 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| eafc7532-d7ed-36cb-9f0b-a4b735ffaf42 | -8.27885 | -42.27655 | 2025-07-09 04:44:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 45c0373a-bc95-3ea9-979c-9586bdec5281 | -7.30986 | -55.30852 | 2025-07-09 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9a7f468-99a8-360a-9723-e44979acd52d | -8.50865 | -43.28395 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.8 |
| 0efd69e5-8423-3b1d-a142-1bc1cce9bfe1 | -6.1448 | -43.96916 | 2025-07-09 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cbd8ac01-ac68-31cd-9e63-5c1272421a63 | -5.23113 | -45.21029 | 2025-07-09 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf3dd296-c424-3a6e-a911-ab76299715b4 | -5.78249 | -43.60915 | 2025-07-09 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7577f6a9-a507-3b69-854f-694be837ce0c | -8.50782 | -43.29586 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 5dd62324-324b-3b2e-b29b-0b992fcf7930 | -6.67859 | -46.30566 | 2025-07-09 04:44:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ef871aa4-fb9b-3ed5-86ba-ed187ee637ad | -5.50372 | -45.492 | 2025-07-09 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b0318db-0688-3480-831c-444915197437 | -8.51117 | -43.27187 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.7 |
| a50306fa-ec25-34a1-bb46-ddce59cb1dff | -7.2471 | -43.07133 | 2025-07-09 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4c298448-20a2-364f-a079-4fecca6cf259 | -6.548 | -43.61885 | 2025-07-09 04:44:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 166f2c2f-3dfa-33ef-b5ce-71a83aba3851 | -8.50906 | -43.28696 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 26.3 |
| 26523e4a-b556-35ca-878f-95e66d924891 | -8.51252 | -43.29359 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 18b7abfe-ab71-3dd2-bbcb-31b639168d50 | -8.51245 | -43.29951 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 3f0ee00c-6825-3b30-afbd-b45167f99f2a | -4.50309 | -47.04726 | 2025-07-09 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66dfd375-b965-3b2e-b34e-87c4618fbe21 | -8.37731 | -43.94455 | 2025-07-09 04:44:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38a9c93b-5686-35c1-a51d-79e345419ee6 | -6.54731 | -43.62379 | 2025-07-09 04:44:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d6fef57b-80ab-3ec5-997c-852f8ae55863 | -5.5884 | -52.08195 | 2025-07-09 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95975741-6460-370b-8015-4b6053fe7f31 | -8.51411 | -43.28159 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 42.9 |
| a7264a25-aa04-3751-b4ac-6234b0715b52 | -5.00908 | -56.17597 | 2025-07-09 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bde48d40-cda0-3bee-ad1b-26f8052b105b | -5.76669 | -45.78635 | 2025-07-09 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3634620-1b9e-3c73-a451-31f421f680f8 | -5.01375 | -56.1732 | 2025-07-09 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f212195a-27d5-3ece-be84-d39eca86116a | -6.97871 | -47.08231 | 2025-07-09 04:44:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4a007c48-629d-38e0-a866-66324cc4b52b | -5.41752 | -47.56857 | 2025-07-09 04:44:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25fb476f-a7d6-375d-b625-d3e2264171f6 | -6.17431 | -48.04941 | 2025-07-09 04:44:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| cdfef839-35b4-30ec-b0fb-58ea8d92ac6b | -8.5061 | -43.27125 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.7 |
| ed6266f5-1186-386f-8380-393af0580d73 | -6.74449 | -43.15768 | 2025-07-09 04:44:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0716a640-4148-3b88-8490-8b9ac55d83e8 | -8.51678 | -43.30024 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 08756d7a-a65b-3664-8841-148f009f336e | -8.37658 | -43.94984 | 2025-07-09 04:44:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| acf452be-aff8-3c3e-ac8f-584ac03a6ed2 | -7.23119 | -43.07495 | 2025-07-09 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5865b813-0caa-3036-8c32-75f9595a305e | -7.81161 | -46.57491 | 2025-07-09 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d55e70da-07cc-3bd1-b3d3-2fbb0b73080c | -8.51213 | -43.29657 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| f92b8142-a26d-3ad4-88e5-a83e2ff207ce | -8.51718 | -43.29726 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2927457a-f7ac-3222-9ae7-fcfbad76e142 | -8.51173 | -43.29954 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 07b4ef13-109a-368a-836c-42764f11d1b0 | -6.67693 | -43.19922 | 2025-07-09 04:44:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8856231b-b0d3-37c1-8282-d44d0b872f44 | -5.9589 | -44.18222 | 2025-07-09 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8440954c-6a1f-32e5-9f15-c4bc923af969 | -5.58953 | -52.07489 | 2025-07-09 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 570f90e3-d511-356f-b01d-46334f27233c | -8.50568 | -43.27428 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.7 |
| 39331406-2d71-3396-9aa3-86b45df5dd90 | -8.50699 | -43.30178 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0c124d8f-1a35-3f15-b6f0-e87230f05a18 | -5.50577 | -45.49079 | 2025-07-09 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f311ee75-56c5-3d74-8c28-711f3a859f3c | -8.51032 | -43.27794 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 40.3 |
| d86dad85-1a73-3206-8164-76bd76fb0a8f | -8.17081 | -46.51231 | 2025-07-09 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 531dfc47-c67c-34b2-9928-ae997da75962 | -7.08545 | -49.16229 | 2025-07-09 04:44:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0194539f-6b36-3e40-9d97-8b6973b41f62 | -6.63367 | -56.27128 | 2025-07-09 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6b070fd-5ba7-36ff-a6ab-eeffa35b598c | -5.12305 | -56.1167 | 2025-07-09 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24e981d5-5510-30e3-8233-3767ea7ebfff | -5.96347 | -44.1829 | 2025-07-09 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be614cec-b4cc-31bc-b190-715aa0857532 | -8.27301 | -42.27911 | 2025-07-09 04:44:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6fc0b8d3-aec8-3ed6-a100-c7cd9c1e144f | -7.65985 | -44.36188 | 2025-07-09 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 61c2c1f9-6bb0-353f-b0d4-64a9a749893c | -7.95642 | -49.64785 | 2025-07-09 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1861929f-1ee2-3f64-a62c-cd0ed9553588 | -6.67911 | -46.30217 | 2025-07-09 04:44:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6e850b39-3e6d-3246-9c16-528117219e11 | -8.50948 | -43.28397 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 26.3 |
| d4b2f68c-f300-3240-8d45-4a17ce5761bf | -8.50864 | -43.28994 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| f3e9db0c-3544-3312-babf-c7892f98eb80 | -5.78572 | -43.61432 | 2025-07-09 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5febc076-550c-3bcf-b556-71c758100e6e | -7.23662 | -43.0728 | 2025-07-09 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c0dfe6e7-41b4-3f3b-b11b-499cfaf2f8c8 | -6.72789 | -44.33636 | 2025-07-09 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9e3e2a26-f714-3ed9-bd6b-d93f4ba0b0fe | -7.54524 | -45.65413 | 2025-07-09 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8e970e37-10ad-37ab-bc09-e4071ee96046 | -5.05941 | -45.11459 | 2025-07-09 04:44:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 084672ef-b59e-306b-adbf-2173f3a43fb0 | -6.88999 | -47.39105 | 2025-07-09 04:44:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cfc685e5-a6cb-3540-9d17-cc5074505ccc | -8.5137 | -43.29061 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 44ab1922-0c01-363a-a609-115e7d8452ee | -8.50483 | -43.28032 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 40.3 |
| 57d2d4ca-de5e-3dcb-af2b-8e2d30e0e40a | -8.51291 | -43.29062 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 9a915090-3462-319d-9cf9-47cb12d0337f | -6.98182 | -47.08762 | 2025-07-09 04:44:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4f967df-cf42-315a-a536-55f379d29a0a | -8.50525 | -43.27731 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 40.3 |
| 22eace55-7680-32c7-8d8a-e697656692be | -7.23242 | -43.0662 | 2025-07-09 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c87f6d0a-0f67-30a5-aac5-5f788818f383 | -5.78176 | -43.61435 | 2025-07-09 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb2305d8-9c68-3aae-95eb-6bd551271b4c | -5.95956 | -44.17762 | 2025-07-09 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4de2b1b7-e0b9-34e9-9c2b-946bf202048a | -6.62523 | -43.35066 | 2025-07-09 04:44:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ae84299d-a790-369b-a805-0110a02e9b90 | -7.95698 | -49.64415 | 2025-07-09 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f439f6cc-b531-3ac8-86c0-2fd1835020f1 | -8.51287 | -43.29655 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 98799e24-5f30-3f28-bb7d-9fdfb9ed5bbf | -7.0889 | -49.16282 | 2025-07-09 04:44:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 210a9546-7e57-39bf-8a5c-8837939c0eb5 | -6.17071 | -48.0489 | 2025-07-09 04:44:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 0ec78362-620b-34a8-9d38-1038c2432c3b | -6.14409 | -43.97399 | 2025-07-09 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c817c3eb-3cc2-3293-96c1-31ca415d33ed | -8.50984 | -43.27487 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 825e0266-3cf1-36b5-a4e1-1b5a62899740 | -8.50944 | -43.27791 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 42.9 |
| 3dd08d75-8682-322e-8479-434b15dd7236 | -12.98657 | -44.8769 | 2025-07-09 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 100f4b59-8fb4-3afe-96dc-2315e183ab9a | -11.42126 | -45.10865 | 2025-07-09 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4fa69bb5-fca6-344b-a5d5-76bb3436374c | -11.32945 | -55.21877 | 2025-07-09 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7723c751-5245-3cfe-826b-6a32a1b3c651 | -9.92172 | -59.9007 | 2025-07-09 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab832900-f099-3ec4-9db2-d3f794ac03d4 | -13.00631 | -46.2916 | 2025-07-09 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c6645e57-3183-3ddf-839b-0f83edc1a7fc | -11.43186 | -45.10011 | 2025-07-09 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 562e3f1e-bdb4-3b48-a26a-2bba329b193a | -12.57754 | -56.97507 | 2025-07-09 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da266395-6c5d-3311-8c37-210d47ae9b93 | -10.22883 | -56.76958 | 2025-07-09 04:46:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e6945766-e336-3dc8-b406-36ccdead5973 | -12.98036 | -44.88701 | 2025-07-09 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 245c0df9-4a51-3d0c-a8f7-905adca771aa | -11.67444 | -43.77856 | 2025-07-09 04:46:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5ded0ade-4a42-38d3-bd48-1ce1c28f483c | -9.4612 | -62.19909 | 2025-07-09 04:46:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90a0aecd-3274-3c5d-ad51-3bf42e2ae531 | -11.67918 | -43.7823 | 2025-07-09 04:46:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ed8aa777-4a20-3c87-add6-e10ec7f4e3ff | -9.40678 | -48.45087 | 2025-07-09 04:46:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 058da7dd-c9e4-36d7-bbd0-dfb8a9095cd6 | -8.64972 | -48.4964 | 2025-07-09 04:46:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a906748c-07b3-3c58-a224-142de6efdfec | -16.63005 | -42.21321 | 2025-07-09 04:46:00 | NOAA-20 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b6bd39f5-6e5d-3185-94be-2f8ccfb71030 | -11.50944 | -48.95644 | 2025-07-09 04:46:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ff4a570a-fb40-3516-99f1-2764c5c8159d | -10.63489 | -49.45807 | 2025-07-09 04:46:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 4e5994df-a529-3e0f-947c-bd7e447b1fe4 | -7.72294 | -55.13948 | 2025-07-09 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97104c5c-32fb-3fcd-8af6-b3d4a5e01e13 | -12.03481 | -48.75803 | 2025-07-09 04:46:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b628eca8-7032-3082-a2e8-534852429034 | -12.05442 | -43.51071 | 2025-07-09 04:46:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cafa9acc-17be-354f-af53-3ca40eaae999 | -10.64485 | -44.48877 | 2025-07-09 04:46:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 24b77b12-c99c-3484-b9c1-edc90a9213e3 | -9.34719 | -58.85034 | 2025-07-09 04:46:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 015f220d-0d14-395a-b5f5-a2efcc47937f | -11.11157 | -48.8685 | 2025-07-09 04:46:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a01a4b2-5d57-39a3-bff8-8638d5fdce2a | -13.38788 | -47.88193 | 2025-07-09 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README21.md)
