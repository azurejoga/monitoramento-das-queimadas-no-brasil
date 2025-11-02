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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1efb6bc9-9fef-3ef1-893e-3c2a4b2f302a | -5.73011 | -44.51083 | 2025-11-02 04:21:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d323f6df-eb8f-305a-bdf0-e6badf6be8a0 | -7.10907 | -38.30429 | 2025-11-02 04:21:00 | NOAA-21 | AGUIAR | PARAÍBA | Brasil | 2500205 | 25 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c63a85eb-7f4b-3e15-b9fe-906162f5b549 | -8.12764 | -42.21195 | 2025-11-02 04:21:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0e02310b-1470-3dd3-b96b-00c39f279ede | -4.50574 | -50.49263 | 2025-11-02 04:21:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| faa466a7-5794-3564-8c79-868c447f7929 | -7.40537 | -40.0701 | 2025-11-02 04:21:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c0d904f3-b5be-3c7f-b29e-d69b4b069295 | -7.95519 | -45.12333 | 2025-11-02 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2e9451f5-d385-3d4f-a2a8-be0eb6e1b3df | -6.12471 | -39.72328 | 2025-11-02 04:21:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cc0609d9-71f6-3b89-a891-58ee46f27cac | -11.27909 | -45.49359 | 2025-11-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1d2be466-0657-36fd-889c-690ca8739bde | -10.63899 | -51.7613 | 2025-11-02 04:21:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bcc8608-02f2-386a-945a-b000470b685b | -10.78365 | -56.81518 | 2025-11-02 04:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e03559eb-e58d-3e31-8b62-34a11fc063b0 | -10.73685 | -46.2348 | 2025-11-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 792b316b-54a3-37a8-a643-e55bc8b9f62c | -7.32669 | -42.50134 | 2025-11-02 04:21:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c1ee4da9-2a69-3019-b77a-d9ac28ff4197 | -11.53146 | -43.15203 | 2025-11-02 04:21:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 81aa8c9e-3ea0-3936-9f20-5cbdb3ed4eef | -11.86771 | -43.81601 | 2025-11-02 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2bf4378-5cbd-38bd-a77c-ca4ba5142450 | -6.71973 | -44.23309 | 2025-11-02 04:21:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 722d971c-56cf-3e88-8542-71da2dc5fb26 | -10.73629 | -46.23832 | 2025-11-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6470a55-16e3-3238-b308-44731a2b9a57 | -13.02518 | -43.61825 | 2025-11-02 04:21:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d5d65605-3251-3b93-8b8a-89c0129b47ae | -10.73292 | -46.25948 | 2025-11-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a528d68b-a511-347d-ae74-4b7719e26647 | -11.86716 | -43.81977 | 2025-11-02 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 829ef5b9-1c38-380d-ad36-1c69ecabb48f | -8.06871 | -40.91874 | 2025-11-02 04:21:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ec1ae2a9-d635-3152-85d2-e7d5883231f8 | -9.7139 | -43.38287 | 2025-11-02 04:21:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 21e87716-92da-3e7a-9218-a2c16f51d760 | -10.7823 | -56.81232 | 2025-11-02 04:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f82689e6-94d8-367b-8c3d-54c741c73a03 | -6.71919 | -44.23655 | 2025-11-02 04:21:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c1d870b4-d8b3-3030-8a5e-5da3aae2e8e0 | -7.29919 | -41.57639 | 2025-11-02 04:21:00 | NOAA-21 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 1003944d-1ea9-39c6-a744-abd27b7537fd | -11.36473 | -54.31223 | 2025-11-02 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2eda950b-b2d7-3380-a805-295af85a88e8 | -7.52991 | -47.292 | 2025-11-02 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 95a7da55-3f94-30ec-8373-6b39bc1f4678 | -3.78321 | -55.44841 | 2025-11-02 04:21:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 44cdab50-195c-38f0-bfc4-bc77719b3562 | -9.15433 | -51.30791 | 2025-11-02 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5f99982-8914-3420-a4e4-c25680571391 | -10.99536 | -53.99763 | 2025-11-02 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8b7bc29-85d5-352f-9ded-1e8655a08d59 | -5.0967 | -46.17036 | 2025-11-02 04:21:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4e46c1c-fb5a-343a-a8d9-9798a631f634 | -9.67663 | -43.88762 | 2025-11-02 04:21:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| deedaf3c-6f68-3f7e-a3a6-537043d28bdd | -7.29981 | -41.57217 | 2025-11-02 04:21:00 | NOAA-21 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 7661e24c-9312-3eb8-add1-7e3c3b6bd014 | -12.64358 | -41.27886 | 2025-11-02 04:21:00 | NOAA-21 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6e83e7c4-6605-345a-bfc7-a701e1a76307 | -10.55708 | -44.53296 | 2025-11-02 04:21:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63beb6d9-5e6d-32b3-be7b-5791a53955f8 | -10.50799 | -51.88298 | 2025-11-02 04:21:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59b5ffb1-9d82-3b4c-bb52-ab2c08497fe7 | -11.94236 | -44.8306 | 2025-11-02 04:21:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dda1e3cd-ee17-3628-9f1f-09af9e39f4b0 | -11.57069 | -47.08309 | 2025-11-02 04:21:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2df182da-1519-3df4-be63-286293e2524a | -5.40865 | -44.93366 | 2025-11-02 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc76c7dd-8e7c-3663-b715-ffa935dd676f | -7.72494 | -44.02432 | 2025-11-02 04:21:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80b86cea-63ff-3873-a079-cc6952576bab | -5.31547 | -44.42057 | 2025-11-02 04:21:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4210d860-ac20-3188-babd-ac5479795adf | -11.02614 | -44.0461 | 2025-11-02 04:21:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c4fc0118-3459-39f9-9487-b568d7ceb7de | -11.02726 | -44.0388 | 2025-11-02 04:21:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a6b15209-1a52-3023-8c63-8097fc90a234 | -7.73989 | -39.8983 | 2025-11-02 04:21:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6f9a5c24-6605-3466-aa9d-5dc5747b8929 | -13.23101 | -39.24192 | 2025-11-02 04:21:00 | NOAA-21 | LAJE | BAHIA | Brasil | 2918803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4d098e94-fd2a-3231-82cb-474fc159d28c | -9.45097 | -43.19844 | 2025-11-02 04:21:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6852067e-79d5-3277-a179-8c7606597f6e | -11.29162 | -53.96127 | 2025-11-02 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51dee56f-78ac-3fb5-8131-932a6325ccd5 | -9.44754 | -43.19794 | 2025-11-02 04:21:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d5b37ff6-35fd-39bb-b2d8-2187ab1a8954 | -5.80455 | -44.51543 | 2025-11-02 04:21:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a48b8184-2c12-3c40-81de-6b06585c540a | -5.11655 | -45.95885 | 2025-11-02 04:21:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10d55da0-95cc-33d4-a2e4-4bbb180486aa | -6.22177 | -46.14048 | 2025-11-02 04:21:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a7c604d5-b00f-3eb8-a02f-013aa6a99853 | -10.42154 | -44.90451 | 2025-11-02 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9a19f73-d9db-3238-9730-f7f39cfa3a1c | -5.12902 | -45.81579 | 2025-11-02 04:21:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 214d8329-0309-3028-8e2f-415531e320d5 | -10.61734 | -52.18409 | 2025-11-02 04:21:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ecca62e4-abb7-3071-8f47-b649dfce5d62 | -6.68009 | -38.18996 | 2025-11-02 04:21:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4521226f-6e8d-3004-bb07-4cc1316b1923 | -7.23232 | -46.03528 | 2025-11-02 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4e1a710-2761-39dc-99fa-1a78dcbe3b0d | -11.56733 | -47.08254 | 2025-11-02 04:21:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8cb14177-f05e-30c1-bcc1-9165317701d0 | -10.73624 | -46.26001 | 2025-11-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8405633f-f51c-3de0-85db-c25921c5322e | -11.36685 | -54.31124 | 2025-11-02 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a8626c8-ca0b-3795-86fa-1565e21aadde | -7.23518 | -44.94109 | 2025-11-02 04:21:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 51f7a367-90d9-38c5-bf3e-8575eae8c819 | -10.41878 | -44.90048 | 2025-11-02 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 922c3553-de64-31f2-9d93-cdaaf3918af4 | -6.80343 | -42.20543 | 2025-11-02 04:21:00 | NOAA-21 | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e7d5f821-58f5-368d-9f88-fbd1bd107b33 | -7.95849 | -45.12384 | 2025-11-02 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6344b3cb-2ad8-3ca0-b617-c63a759897ae | -11.36416 | -54.31521 | 2025-11-02 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ac3bb7f-1ce6-39be-9ee4-ec0bf79805ab | -7.15524 | -41.81551 | 2025-11-02 04:21:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4ad94381-454d-3bfb-bceb-8a049e95469f | -5.55883 | -42.98725 | 2025-11-02 04:21:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b41fbad4-cefe-3b38-aecc-379945485447 | -9.06412 | -48.83625 | 2025-11-02 04:21:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f847b26e-cfe8-30d8-ba4e-a8329dea6d7a | -11.44849 | -43.24489 | 2025-11-02 04:21:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7666b3f1-a1b3-3e98-88a2-4b693978019d | -5.37346 | -45.07058 | 2025-11-02 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b369f280-51ef-3261-bfb3-0ff49e338b54 | -8.59478 | -44.16084 | 2025-11-02 04:21:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a1f1bd5-0a75-39fa-bf82-47fe7b36b02e | -10.73797 | -46.22775 | 2025-11-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 045a08bf-dea6-396c-8a64-d144813111e6 | -11.94569 | -44.83112 | 2025-11-02 04:21:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 679c139c-d2d3-3c96-be32-2ad95ebeda76 | -6.47966 | -39.41021 | 2025-11-02 04:21:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ec2cc86d-f6f5-3695-bf8f-407d0cde4bfe | -10.73853 | -46.22423 | 2025-11-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 329ea35d-1fd9-3125-9c5e-0231366ba178 | -10.74072 | -46.23182 | 2025-11-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 233601ad-a3d9-333b-a48f-cb3938259ea2 | -7.69701 | -43.10588 | 2025-11-02 04:21:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| df68799d-1f86-3fea-b8cc-421016d1e7a0 | -7.07829 | -41.67673 | 2025-11-02 04:21:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| aee82d38-0190-3543-9023-6ade0108c11d | -10.63747 | -51.76125 | 2025-11-02 04:21:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af505fba-a731-3bcd-9e60-83dc98c58c15 | -10.73634 | -46.21665 | 2025-11-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 794feb79-5dff-3662-bd37-e6f3ce3f8c8f | -10.99479 | -54.00062 | 2025-11-02 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b8545c45-e452-340d-8275-41f4143f06b7 | -7.40373 | -42.47715 | 2025-11-02 04:21:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 36e1104b-96c7-3f5d-9297-3763137351fb | -10.74067 | -46.25349 | 2025-11-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 29b7a621-8398-3dac-b800-61f51368f880 | -10.78745 | -56.81799 | 2025-11-02 04:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb6b85c8-242d-31a5-8dca-d971c091e216 | -7.40186 | -40.06796 | 2025-11-02 04:21:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7830b154-c395-3f9b-8dfa-aa0babd9b0ea | -7.15464 | -41.8196 | 2025-11-02 04:21:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7b64c561-0652-316b-8729-59f402c8d61a | -10.99431 | -54.00496 | 2025-11-02 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7cd83185-c93f-3670-802a-b40ff7e47fa3 | -7.40931 | -40.07069 | 2025-11-02 04:21:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 4.8 |
| b296e588-c65c-3f94-bdce-8cfd47305a3e | -9.85423 | -44.1496 | 2025-11-02 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66db4e8e-767a-33d0-bbd8-7cd28735ac5e | -7.5334 | -47.29256 | 2025-11-02 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dec0f9ff-6b91-33d1-91d0-dcbd1bc56347 | -11.36867 | -54.31908 | 2025-11-02 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 64a0bdec-efec-33e0-9c16-839e4db8adeb | -10.7368 | -46.25648 | 2025-11-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eddc5177-b82a-3c10-8e51-a839cc025e5f | -10.73578 | -46.22017 | 2025-11-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88045974-1a58-3800-9eb3-437329474769 | -10.74287 | -46.26109 | 2025-11-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e933467-cbae-319a-9963-caa7bd57e12a | -7.50931 | -42.45004 | 2025-11-02 04:21:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f6a4a658-29b1-3601-9110-7685aced1f79 | -13.63725 | -43.78796 | 2025-11-02 04:23:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99f828eb-bcb7-37e7-9ac7-535687b1dc21 | -13.14423 | -48.44336 | 2025-11-02 04:23:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a07176a-a80f-387a-a403-97dd2fe4d0e6 | -14.01877 | -43.47889 | 2025-11-02 04:23:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| beef4aeb-7587-355a-aff2-b10aa5883c6c | -13.68404 | -47.21884 | 2025-11-02 04:23:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b77dd8c9-a796-327d-864e-5e2a36009835 | -13.88223 | -47.3626 | 2025-11-02 04:23:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e5051f9a-ea6e-37ef-b40b-accd7454cf77 | -11.97936 | -58.06478 | 2025-11-02 04:23:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9bb9ee32-762a-380a-b45e-aa12c5423d9d | -13.8063 | -43.75073 | 2025-11-02 04:23:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README13.md)
