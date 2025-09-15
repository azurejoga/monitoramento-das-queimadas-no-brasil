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
| 769310a6-ded5-3d26-9f32-3cf2ec6f3c4a | -7.06767 | -43.89407 | 2025-09-15 04:19:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 113e3988-c503-381b-ae73-b37208e8d992 | -6.91399 | -46.16022 | 2025-09-15 04:19:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 369991e5-ca18-325e-8e87-2fe6a97d70a4 | -8.78142 | -46.01548 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4184aac4-8d24-334a-b65f-6fa48845fe91 | -3.64961 | -54.04985 | 2025-09-15 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a9fb548-69dd-3c58-bbfd-007b6544c97b | -1.8972 | -54.61493 | 2025-09-15 04:19:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d9399d3-d9bf-30c1-9665-6d8c245997d3 | -5.95774 | -42.79512 | 2025-09-15 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0186e1af-383c-3633-aae7-1d697002f4e9 | -7.0536 | -44.11875 | 2025-09-15 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89387a15-b73c-3854-be3b-c096713249f0 | -7.53095 | -46.7276 | 2025-09-15 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 982d5a44-bbe2-3827-9041-f77fb476557b | -6.51732 | -43.24592 | 2025-09-15 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79b2e6ec-c7f7-3ee5-9b0d-3441f184660b | -5.93865 | -43.23631 | 2025-09-15 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| dfb8000c-8dfa-339a-ad94-7cee9edbc198 | -8.11984 | -50.16961 | 2025-09-15 04:19:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7207808-5371-37b2-9c84-a06d415eff42 | -4.17532 | -48.57513 | 2025-09-15 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 56f88c54-fca2-39d3-89c3-9be1d8dfb379 | -5.00629 | -39.60769 | 2025-09-15 04:19:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0d0456c6-136f-3ff1-93c5-f540636be849 | -7.89413 | -43.57836 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 88aa8c5e-aed6-31d9-96e0-aac4df32a07c | -7.27305 | -48.67574 | 2025-09-15 04:19:00 | NOAA-21 | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d30ec208-562e-3929-b4db-73160d25afbc | -7.41162 | -42.08746 | 2025-09-15 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b0b75174-e4d8-3774-9ad1-abe22dafcd87 | -8.98212 | -45.82283 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 39912e32-7951-3389-9701-69f26fc8bb15 | -6.89215 | -45.63002 | 2025-09-15 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3133bd63-49e9-3f33-b0f6-29f6ec8f91dd | -8.40548 | -47.25368 | 2025-09-15 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d48a08a-fb4c-351e-b0b1-304f76f574d0 | -6.6834 | -45.50774 | 2025-09-15 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ddb3910-5fad-3ff2-932a-14d3f657b40b | -5.25395 | -42.60217 | 2025-09-15 04:19:00 | NOAA-21 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f67cfb7-3d25-3e89-9d09-79e2a44fff90 | -8.02418 | -44.96637 | 2025-09-15 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3a371db3-0b98-3e9f-8f66-1d1ff9c3c629 | -7.86451 | -43.58097 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 17a533ba-d1aa-36d4-965c-2b1333a1596e | -8.00665 | -44.81811 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d17c03f8-b213-3c20-9a46-e8a64ac48b3f | -7.88793 | -43.57369 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 27.2 |
| ec21eb05-6fc5-3afe-b5f2-6e9ba2eabbf7 | -5.93921 | -43.23269 | 2025-09-15 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f91596c0-169e-333c-bdbb-0d32326818dc | -7.84474 | -43.85794 | 2025-09-15 04:19:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4733f206-7c85-30b7-950a-4e4e51fb11f1 | -9.09974 | -44.80899 | 2025-09-15 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81b5c73d-a005-35af-94d7-f599324e70b0 | -9.04973 | -45.71589 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c98c7305-b05d-335c-83de-85fd235f53cd | -7.68784 | -45.13614 | 2025-09-15 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 42fbb66e-2593-375c-b224-18a2c21b33ee | -8.96614 | -45.77389 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b3abe86-1dfa-3b07-9344-761414c24cea | -8.62981 | -45.7271 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66ddf6ff-22a1-384d-9d14-b7ac950514b2 | -5.9798 | -45.82639 | 2025-09-15 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d76c671-8535-39fd-a971-1568824703f8 | -5.96795 | -43.21458 | 2025-09-15 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c35c64f5-aeb2-32a2-b0f4-ce2f80523b2f | -6.33084 | -43.33629 | 2025-09-15 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1d8b58c8-81dd-3bcc-ae29-145da00dda77 | -9.22482 | -44.50445 | 2025-09-15 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 131bbf1d-eaed-3fc1-b65c-e9d74909e9fa | -6.44597 | -43.31713 | 2025-09-15 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8944666-87e4-31e7-843d-717ed8abfb07 | -8.89419 | -46.20644 | 2025-09-15 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a16d739a-2600-3c47-a21d-79da158004eb | -9.23725 | -45.6716 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f506bd2e-17f7-3483-9f8d-c57905f737d2 | -6.16639 | -41.17866 | 2025-09-15 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4359b9ab-446d-3ba2-b506-7b18efaa0819 | -7.21811 | -44.24157 | 2025-09-15 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed4de36d-b62b-36ee-8bc7-8302ef68fb68 | -6.99213 | -45.62152 | 2025-09-15 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f99c7832-c28a-3775-9520-de9838279e51 | -5.75016 | -43.92672 | 2025-09-15 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8f5512a-f4fe-3d30-bbae-66753c870870 | -4.17916 | -48.5757 | 2025-09-15 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1df8e2d2-167a-3f0d-a23a-3974b8ccb706 | -6.23066 | -43.74326 | 2025-09-15 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7f45026-87ce-38a6-ac5c-0487cf3bc719 | -7.73961 | -45.30709 | 2025-09-15 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2125496e-b06c-3559-b301-3ee933ca9d00 | -8.91397 | -45.49884 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0d5686a5-afe7-3cd3-97d8-a76ab16c14d0 | -7.48687 | -46.15039 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65eeff26-8228-37b8-aee1-fa1e8a61bb4a | -7.298 | -43.94448 | 2025-09-15 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b97c150-c13c-34ad-9caa-c9afeaf6453c | -9.00484 | -47.04641 | 2025-09-15 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8f8eb5a3-db03-37d2-83af-069b2027bd5f | -5.96669 | -43.21106 | 2025-09-15 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 34c60c5e-b2a8-3030-b39c-79ab08ccf200 | -4.18069 | -48.56628 | 2025-09-15 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fe198363-29a5-3c52-be37-c150b5b7f052 | -7.684 | -45.13908 | 2025-09-15 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1407e9b-5823-3710-a715-60f469b4f9f4 | -8.60676 | -46.34451 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e11827ff-0219-397f-bfab-aa23a10ed1e6 | -3.91379 | -47.71336 | 2025-09-15 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| df399556-8268-3b1f-8c8e-086234bb449b | -5.4876 | -48.4867 | 2025-09-15 04:19:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 239d6c96-0094-3bdb-b693-6cd940c92d3f | -6.19587 | -43.484 | 2025-09-15 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 98058f0c-fe54-3f42-8777-cf5e4031da88 | -5.20636 | -44.31575 | 2025-09-15 04:19:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 853264f9-8245-3ae4-9dc7-08823f7ae91c | -6.42513 | -42.60329 | 2025-09-15 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9128db06-1b8a-3718-9a95-54537e060163 | -5.07683 | -44.10157 | 2025-09-15 04:19:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6d0f287-cf83-3731-a20d-9bf275872016 | -6.81761 | -45.60749 | 2025-09-15 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f1eaa08e-d802-37a2-ad21-0a55fbf3eea6 | -5.47517 | -44.68592 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e8f3e6a3-165b-3d99-b59b-62686a62d6bc | -8.40206 | -47.25314 | 2025-09-15 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4cfef258-7749-3d60-9717-70376cb07edb | -7.88738 | -43.57732 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 27.2 |
| b3d35faa-6196-3522-a578-e599287ed520 | -6.73037 | -46.30652 | 2025-09-15 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69b75f07-3a90-33c5-b69e-7d6d07000004 | -6.66077 | -44.63322 | 2025-09-15 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d0a9a88-a3c3-3e29-9bff-1d5656cd4fed | -5.76665 | -52.36653 | 2025-09-15 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c7720c5a-6766-3de4-8992-fbe9a6b72557 | -8.78639 | -46.027 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25fdbe3d-8e56-3722-9745-e635b2b4d476 | -7.67994 | -44.48857 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1bd93734-7734-3d1b-85e4-e6364e6cf78f | -3.83216 | -50.77164 | 2025-09-15 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e585fa9e-124f-3b82-a3cc-1dbd1f48ef3c | -6.30956 | -43.34033 | 2025-09-15 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ed9c4da1-65bd-37dd-94f2-6f49b7cc5701 | -6.97363 | -44.5481 | 2025-09-15 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d309ada4-dae2-38d9-a16e-1d75b26403ef | -6.15439 | -41.18721 | 2025-09-15 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5ed360d5-6865-3955-9b78-d342a78d002a | -6.91677 | -46.16432 | 2025-09-15 04:19:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6dd4e5cb-747e-3231-98b5-c0c21e97e45d | -7.48522 | -46.13926 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d4defd4-41b7-34f4-bcb6-556346dd9960 | -6.32247 | -43.34598 | 2025-09-15 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fdaddcda-c404-3941-a228-31225922d2c7 | -4.10891 | -51.09262 | 2025-09-15 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 70ddcbd1-1fe3-3bf6-9858-084a1e5a00cb | -5.15074 | -46.00927 | 2025-09-15 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 31ee67b0-741b-3eda-b6a9-f2c747409898 | -5.93084 | -44.8638 | 2025-09-15 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8865e893-ee32-3d8d-bb63-7f21eba8a869 | -8.97827 | -45.82578 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| e6f0a0a0-2804-3323-a5e9-251145ea6778 | -5.73731 | -43.19792 | 2025-09-15 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6ab8adfa-53a2-3dda-bc4d-054c1d21e885 | -8.11581 | -50.15727 | 2025-09-15 04:19:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7169398-b3bf-3ae2-bec6-6418ff3ebf32 | -6.96979 | -44.55106 | 2025-09-15 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 8afe845f-b0b6-387d-90b6-1504f5a5c356 | -8.79026 | -46.04555 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3f633d0-98a6-3542-84f4-eb960c981716 | -8.98815 | -45.76313 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fdacefd2-1630-375e-8e3d-cd48d2fc4dc1 | -7.50737 | -44.37258 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b71758ce-3331-32b5-ab51-00ccc03fb5d0 | -5.7722 | -43.91589 | 2025-09-15 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b76f86ee-2d9d-3bb1-9a86-d5d1ba2c3a2e | -7.42794 | -44.86103 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb6dd1e9-25d1-3bb4-9ed3-44598cab00e9 | -6.62035 | -44.08359 | 2025-09-15 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ac00c5b-66a0-3326-bfd9-e8f78cafa9ce | -7.35288 | -44.29443 | 2025-09-15 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 823312d5-f86a-3270-b07a-3b17b5f2defb | -8.08594 | -44.50274 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 17df0cbf-f907-3477-a71e-ad126fe22638 | -9.07238 | -44.82987 | 2025-09-15 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 342407b8-3397-3c3e-a5aa-21b29a96e05c | -7.52869 | -47.63688 | 2025-09-15 04:19:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b753eeb-345e-3b4c-aaa0-0a66d0375c32 | -9.2301 | -45.67403 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30d72c78-2320-3eda-a3c0-68dca9391ab8 | -7.86507 | -43.57735 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4586dbfc-ad99-35ff-b9d1-6423bd2978be | -8.82421 | -44.23539 | 2025-09-15 04:19:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75386c8d-baca-3a87-97af-bf9cd6ae90ad | -5.65112 | -42.59685 | 2025-09-15 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1be43820-54f9-3f56-8547-2fba6ee248bf | -8.64192 | -45.69333 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 656edfbb-8fa0-3ed5-abd2-eb03ecf9d20f | -7.97562 | -45.64326 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7541369d-b585-3801-bfbb-4e60505eeafc | -8.60287 | -46.3475 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README21.md)
