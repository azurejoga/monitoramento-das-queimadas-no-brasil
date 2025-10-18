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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca4cb20c-077b-38b8-b82d-10cc19e5686f | -6.27585 | -44.38197 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 747966b1-4261-3557-b305-0e73c3a6100d | -6.24455 | -46.39033 | 2025-10-18 04:00:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af52bd9e-80d9-3e43-b543-1b8d64256f5c | -4.49809 | -46.49109 | 2025-10-18 04:00:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ded58825-9283-3ace-a773-8dfd1f4f15a7 | -2.36815 | -48.2931 | 2025-10-18 04:00:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db066693-0520-3321-abc3-7d45c4a4bd7b | -5.07962 | -40.95999 | 2025-10-18 04:00:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| de9d9220-2afc-324d-8565-9a5a11b21d54 | -6.47768 | -44.57111 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1351438f-eccb-3cad-9d17-ad85e199e96f | -7.096 | -41.46069 | 2025-10-18 04:00:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b4cb9dc7-57bc-3a2b-acd8-4f2953d331a3 | -6.10493 | -45.84649 | 2025-10-18 04:00:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a875a055-1bae-39e6-b4d3-513681269b5e | -3.29765 | -50.00944 | 2025-10-18 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a90fefe-36f0-30d9-ae19-3f5786bf08b8 | -5.30715 | -41.82974 | 2025-10-18 04:00:00 | NOAA-21 | NOVO SANTO ANTÔNIO | PIAUÍ | Brasil | 2206951 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d78348a8-5748-3894-8199-408240e4c93e | -3.14962 | -50.24525 | 2025-10-18 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| bc5437a3-b2a8-3467-a947-9c60958d7b8f | -6.48039 | -42.16022 | 2025-10-18 04:00:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 83ec7672-471a-3142-ab0c-e148c4403a9b | -3.5936 | -45.97453 | 2025-10-18 04:00:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61ed5ce1-a402-36b2-af30-32fc527933e4 | -4.25205 | -48.56622 | 2025-10-18 04:00:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ee32778-642e-3ae9-ade3-8ca642cff91c | -6.27462 | -44.38341 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d89fcb7-f712-338e-9915-82d915a8ead2 | -7.01382 | -41.83416 | 2025-10-18 04:00:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7bcb7ac9-0456-3ce5-9577-b0b298dca694 | -7.18593 | -41.68602 | 2025-10-18 04:00:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 24a90feb-8bff-3f5b-8425-e8f8050bbc39 | -3.57466 | -49.44383 | 2025-10-18 04:00:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0568b430-ef5a-3336-af98-014dc8f22ed8 | -5.39901 | -40.91898 | 2025-10-18 04:00:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 66aca86d-b01e-387b-b89f-9d5e0fe31719 | -6.73402 | -44.36565 | 2025-10-18 04:00:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b42399a7-2acc-3d2b-ab66-e7eaefbce4b0 | -5.41738 | -40.88942 | 2025-10-18 04:00:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 51445257-9c09-3fee-989c-71b3886b6e7c | -5.53258 | -44.09459 | 2025-10-18 04:00:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0720cd00-aecb-3a27-90d6-5f308823de01 | -2.30623 | -48.57165 | 2025-10-18 04:00:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01424e41-ac9e-3c1a-aee7-963207fe4e9d | -3.52924 | -50.30812 | 2025-10-18 04:00:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f307bbb-0cf3-3ad4-b0cf-0a2015eae35d | -4.00078 | -45.49783 | 2025-10-18 04:00:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2f46a079-0049-34f3-8333-2a819c488242 | -5.84026 | -40.81884 | 2025-10-18 04:00:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 42d6eddc-ee48-3257-a18e-4d3e8df7f424 | -5.57947 | -41.31902 | 2025-10-18 04:00:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f45ac11f-c62d-3d32-8ac8-6292d82c18cf | -7.04317 | -41.8315 | 2025-10-18 04:00:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 1b4eaea2-3067-3fc8-a8a9-5d0deb580eb5 | -6.97697 | -39.69398 | 2025-10-18 04:00:00 | NOAA-21 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 971061a4-88c5-316d-8605-6b865ca472ff | -3.9243 | -41.73351 | 2025-10-18 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 35b35447-4c5a-3b04-a0b5-b39c0bd2d1eb | -3.59433 | -45.97002 | 2025-10-18 04:00:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89f9be59-4172-3dbd-b7e6-2bf1fff9b66d | -5.54731 | -41.33646 | 2025-10-18 04:00:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fffb700c-2824-385f-926b-665096ebe96d | -3.06475 | -43.21324 | 2025-10-18 04:00:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a5a2cb36-5be6-3511-9f10-ea149b1e9e56 | -3.14703 | -50.25115 | 2025-10-18 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| ce934b4c-5b57-3bcf-a12a-b9bacf876bac | -7.01558 | -41.82312 | 2025-10-18 04:00:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8532bd57-64ba-32df-8f4e-d705a64f8a8c | -5.21712 | -45.5195 | 2025-10-18 04:00:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e9dfae1-f2ba-3baa-abab-8c9dca6ca8fd | -5.36525 | -45.56651 | 2025-10-18 04:00:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 50af7846-a25f-377c-bdd0-825a24de088a | -6.00796 | -45.41666 | 2025-10-18 04:00:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8651bc83-747c-352f-bcbb-b692d9228b53 | -7.00203 | -42.79685 | 2025-10-18 04:00:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5cabdf52-526a-3daa-8eb1-27362bfc5cdd | -6.143 | -44.3034 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b50f5404-4091-3227-91a3-2021f0ef941e | -3.14628 | -50.25574 | 2025-10-18 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 90bba4d5-2d49-3711-9a6c-0caca62b1715 | -5.12852 | -45.13364 | 2025-10-18 04:00:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0a187581-ddb6-3b5f-bc4f-89e3fcf7b274 | -6.29645 | -44.7175 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| fa43d44c-b620-34fc-8fe0-280601e925ea | -6.60417 | -44.44316 | 2025-10-18 04:00:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d091a56d-1605-3de5-9d26-7c3838841964 | -6.11112 | -44.85739 | 2025-10-18 04:00:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7b356bea-f0e7-3657-b7d3-6cf31deb5145 | -4.45386 | -43.22479 | 2025-10-18 04:00:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b4a9dd62-5a33-3cdf-95eb-1197f2f6dd64 | -4.83633 | -48.08189 | 2025-10-18 04:00:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f50b41fe-b0c0-3458-94b9-dc381f6a3a01 | -3.23505 | -42.07187 | 2025-10-18 04:00:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 80b988ae-5748-3e4f-acb3-b9bb6e4369b3 | -4.91764 | -45.41032 | 2025-10-18 04:00:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ba9e6cf7-c36a-3883-b6c6-0a2af1592ce4 | -4.37368 | -46.5317 | 2025-10-18 04:00:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8b4484ab-1a74-3e5c-b77e-3184220b877d | -6.27723 | -44.31824 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 83ac588d-55d1-3b59-a481-b30cb7e07d11 | -6.10769 | -44.85324 | 2025-10-18 04:00:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b1f190d9-6a8d-36b9-b055-9686f2533f12 | -6.44501 | -43.81186 | 2025-10-18 04:00:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 30a16222-e69b-3c91-b108-bfa9bcec0594 | -4.30349 | -48.06885 | 2025-10-18 04:00:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| cd53369e-1df6-3d40-bbd7-c7249e903f60 | -3.7826 | -51.76786 | 2025-10-18 04:00:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b99ab8d0-29f3-3ced-a7a3-ccacb9e43d17 | -3.84456 | -40.97557 | 2025-10-18 04:00:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c8dd3b9e-e738-327f-9999-4f2660ddad3d | -3.85384 | -41.58186 | 2025-10-18 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| f8f4b3e8-0aaf-3777-867b-7fdac86aa504 | -3.64772 | -45.26238 | 2025-10-18 04:00:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9069fd45-6e13-3a70-9918-4eb7a745ecf1 | -4.40288 | -44.08404 | 2025-10-18 04:00:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10a6f2f8-0843-36f8-856b-91f0a06570a7 | -4.91405 | -45.4058 | 2025-10-18 04:00:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62c9ad34-291a-31d3-97fd-dcb7e95ff8a8 | -6.13444 | -44.30709 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9c1e049b-d683-3fb8-99ff-df8863b74e2e | -5.84081 | -40.81533 | 2025-10-18 04:00:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6dc8f82a-f131-3338-93d8-fa7230ddf18f | -4.96147 | -45.08745 | 2025-10-18 04:00:00 | NOAA-21 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 709d4a6c-a402-361f-b5df-9886d09bab05 | -5.57515 | -44.18347 | 2025-10-18 04:00:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 87e20a3d-cb17-3787-b5d1-97b3cab8fc30 | -6.31641 | -39.97751 | 2025-10-18 04:00:00 | NOAA-21 | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d180e602-7a49-39f1-85d4-f9102fc7201b | -3.54256 | -49.44799 | 2025-10-18 04:00:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e18aeed-98e1-3140-8bef-49b77e87f2bc | -5.63017 | -50.03155 | 2025-10-18 04:00:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc4e11d2-b202-3846-a872-dabf422094c6 | -2.87097 | -50.73155 | 2025-10-18 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e023be16-bc19-3ead-8960-2c8fabf482f9 | -3.13672 | -50.24795 | 2025-10-18 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| ee2968df-8046-38fe-89c7-836b363db9b6 | -5.30156 | -44.84479 | 2025-10-18 04:00:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bfa0da66-ac39-3064-8124-5aebe7272b64 | -5.456 | -45.41165 | 2025-10-18 04:00:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6305eea6-6181-373e-81ee-160512cc278f | -4.4487 | -43.2331 | 2025-10-18 04:00:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 5b041c6f-8584-3e22-a8dd-e0b6c9714231 | -4.88227 | -46.70218 | 2025-10-18 04:00:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a8d70da-ada3-39ed-a424-7995cd24315e | -4.11886 | -42.90715 | 2025-10-18 04:00:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ec54f65d-c56d-3b6f-8544-d65b815a24bd | -3.85039 | -41.58131 | 2025-10-18 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 3fd23fb9-6bc7-3e4b-b612-a6dc0f4d8893 | -3.14022 | -50.25477 | 2025-10-18 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ae5ca2ce-2539-3c15-84a2-c051675acebb | -4.42351 | -47.75324 | 2025-10-18 04:00:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89a837b5-8db7-3e9d-ab59-a45ae0a502fd | -3.14121 | -50.25801 | 2025-10-18 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| dc5abef6-6a15-3c10-9c09-282cae2f8572 | -4.94257 | -49.76394 | 2025-10-18 04:00:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 36cabe2f-d035-3706-87bb-9920d49a08f3 | -5.87148 | -44.21196 | 2025-10-18 04:00:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cc13dc35-a202-3dff-b0de-bebb0da7ffc9 | -2.30131 | -48.56726 | 2025-10-18 04:00:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e92e02f3-ab1d-3724-a5e6-f370aac888f5 | -6.05035 | -44.52318 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b998b76c-8fcd-3f68-8b93-3f6db062293d | -4.25148 | -48.56961 | 2025-10-18 04:00:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53965efd-6340-3960-b5ff-69c89d3936dd | -5.45664 | -45.40767 | 2025-10-18 04:00:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f39eb8d4-ccf6-3063-930f-f03a0a1d3107 | -6.32403 | -44.30849 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 940f4f3b-edba-3ecb-ab75-3ca140e112f8 | -3.90235 | -43.03557 | 2025-10-18 04:00:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 394a1977-5ac1-3b5d-aba2-33db6ab432d1 | -5.926 | -45.43568 | 2025-10-18 04:00:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c225dca2-3d04-31dd-bad3-1bfaa8ad8541 | -4.53542 | -44.80206 | 2025-10-18 04:00:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7a90dd5-9718-3a1c-a3ff-97efb24bffe1 | -5.57596 | -44.17859 | 2025-10-18 04:00:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7fec280e-80e9-3bdc-9114-c04cdc653450 | -6.02041 | -43.72293 | 2025-10-18 04:00:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| abff0a27-a54f-3b06-a009-c07cfac97fa2 | -3.41175 | -43.01101 | 2025-10-18 04:00:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ee207d4-9e64-3788-95d2-7e93bd51959c | -6.14153 | -44.28811 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1060690c-1e04-3309-b98d-d1c699ff12e7 | -3.53819 | -41.71405 | 2025-10-18 04:00:00 | NOAA-21 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 70647977-ee76-378b-a1dd-6877f3ee11ef | -4.42683 | -40.17667 | 2025-10-18 04:00:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9ec482c5-e709-38c5-914e-0a117e16f947 | -4.91842 | -45.40731 | 2025-10-18 04:00:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7e64a296-d0ee-32ef-87f3-3217cfa14df9 | -3.14854 | -50.24198 | 2025-10-18 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 3116564e-7c38-3261-a397-817ce2229e90 | -5.4518 | -45.4109 | 2025-10-18 04:00:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71aaec1c-812f-3753-a36a-5d0386fbbae9 | -5.53819 | -47.9527 | 2025-10-18 04:00:00 | NOAA-21 | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f65f3f88-788d-3c00-a96d-ecd857562b76 | -7.07645 | -39.29385 | 2025-10-18 04:00:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 13eb4a9a-ef58-32e9-b17e-c83e79767323 | -5.57775 | -41.3191 | 2025-10-18 04:00:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |


[Clique aqui para ver as próximas entradas](README14.md)
