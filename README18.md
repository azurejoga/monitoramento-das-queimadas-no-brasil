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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5bee6de5-1d19-3146-84a9-387b44bc6f38 | -5.23603 | -45.47791 | 2025-10-31 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f3b3854-315a-31f3-ba79-dac13753bccb | -5.66679 | -44.83508 | 2025-10-31 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71a51596-97fb-37d1-88e6-e062ee79b713 | -3.54041 | -46.431 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 94a80e1c-a1f5-3d04-bca7-ccd053ec04cb | -5.42639 | -43.56943 | 2025-10-31 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c505bb87-2519-3a26-b7e8-cc2d29e442c2 | -7.59555 | -43.56236 | 2025-10-31 04:06:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e363e78b-ab5f-3dad-9df0-607d1581cd2d | -4.7937 | -46.46405 | 2025-10-31 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| efeff5f7-0e81-3b38-8a71-966e9f8ddeda | -3.93923 | -46.97426 | 2025-10-31 04:06:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 764f9811-e8c7-3166-b597-261692118dbd | -6.51272 | -41.34361 | 2025-10-31 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a37582a0-4389-368e-9f8f-05b3a2ea3596 | -2.73486 | -45.21133 | 2025-10-31 04:06:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec7fd6b2-7e32-30e4-96d6-922f817c74ad | -4.48129 | -43.45179 | 2025-10-31 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52f52908-d42b-3cb3-be7f-a12bcfbc89df | -3.14128 | -49.42866 | 2025-10-31 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 79d74c72-95fc-38a5-b452-5affb89980b5 | -4.58757 | -46.44959 | 2025-10-31 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 514100ac-f203-36b7-80df-450069147e73 | -5.54212 | -48.37761 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f0a41d1-945f-38ca-8428-0e16698f57eb | -7.58752 | -43.5687 | 2025-10-31 04:06:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2520718-f58e-3476-b33d-700587085b05 | -5.79148 | -40.80885 | 2025-10-31 04:06:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f8c5dea7-1dc4-3895-8262-de7f33a9278a | -5.94516 | -43.9688 | 2025-10-31 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 33024c6c-d0d6-36c0-a5e1-40a8e8078f0b | -4.42787 | -43.71695 | 2025-10-31 04:06:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ce9d7e4-c9f4-336d-a294-fc3c7411495e | -4.67221 | -46.42484 | 2025-10-31 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc1854be-446a-3a90-b017-b69ff647dde0 | -8.04917 | -39.0712 | 2025-10-31 04:06:00 | NOAA-20 | VERDEJANTE | PERNAMBUCO | Brasil | 2616100 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 01cfa199-399d-3c94-9f4c-d5b8a0309374 | -4.43071 | -48.01553 | 2025-10-31 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 293b8ce4-8ecc-35b0-b4bd-1c169a34e01f | -3.5681 | -45.3526 | 2025-10-31 04:06:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a56209b5-e523-3cae-b35a-1364f2b7df3d | -4.86602 | -45.77325 | 2025-10-31 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1f68c8a-40c3-3d6d-8852-12bea19d0ba5 | -7.58813 | -43.56498 | 2025-10-31 04:06:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57983104-152a-3fce-8ccf-a3857eb1d60e | -7.79046 | -41.57846 | 2025-10-31 04:06:00 | NOAA-20 | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7cfc82fc-3d87-3a1e-8149-326ede1cf53f | -4.35658 | -43.00456 | 2025-10-31 04:06:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 862cd465-401b-3090-9b8f-82f38f0a36a6 | -5.00339 | -41.04459 | 2025-10-31 04:06:00 | NOAA-20 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| baccad6a-c28c-3502-8f00-5b5524fe1e23 | -5.64398 | -45.02177 | 2025-10-31 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ce99a03-f8bf-37da-bd78-ff4051e228d6 | -5.29386 | -41.18571 | 2025-10-31 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6c71b85c-ff1c-39ba-99f8-51eca7f51acb | -5.47081 | -44.318 | 2025-10-31 04:06:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1eed2019-942a-3812-8c90-bccc3ca0a684 | -7.33518 | -42.73421 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1239798a-e672-359f-9c09-91b00bfaa723 | -5.87819 | -44.71053 | 2025-10-31 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 224ae859-6b19-3168-b48c-34453a6119ca | -5.28065 | -45.42157 | 2025-10-31 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f2a6e6da-1458-3e26-b4a1-297696b3d57b | -3.37779 | -44.07179 | 2025-10-31 04:06:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4fefeee-78ac-3e54-aca4-bc2fc36610e9 | -6.10802 | -41.73236 | 2025-10-31 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| ee796264-63c5-3fc7-998d-9116327ef755 | -3.5837 | -50.26356 | 2025-10-31 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4848f5a8-d6e9-3a78-8b21-7a722e173e69 | -5.10172 | -45.18277 | 2025-10-31 04:06:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5167c7fd-d46c-39fc-bf7c-5a2e07369e58 | -4.65059 | -46.40179 | 2025-10-31 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1408c939-6fca-3af0-b881-c06748f391a9 | -3.99393 | -48.32484 | 2025-10-31 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bdd7d1b4-a21c-35c2-86fe-a5fc241efefc | -5.78708 | -40.81525 | 2025-10-31 04:06:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 783a73f2-7f5a-335c-8a0e-b4e4e3515393 | -4.31254 | -41.44026 | 2025-10-31 04:06:00 | NOAA-20 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b117cd30-9e85-37f3-a8a0-e6a57a153d0d | -2.63858 | -48.50149 | 2025-10-31 04:06:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 31c2d0ab-3372-3304-a9e7-4245ab2eafc1 | -6.52669 | -43.70914 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a1e0507f-a02e-3f36-8c39-1bff72ca7ae2 | -6.8499 | -45.13405 | 2025-10-31 04:06:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9dacc291-e5df-3416-98ab-d5dc9c4d327f | -4.87104 | -47.52631 | 2025-10-31 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 532ac2b5-75f3-3341-a87b-942581298df4 | -5.79857 | -35.58529 | 2025-10-31 04:06:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8ec26eba-c5ae-3c3e-957e-e664f5f0c42f | -6.21785 | -43.94258 | 2025-10-31 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4f8bc25d-60c4-30d4-9462-8436faa67d1d | -5.61213 | -42.79026 | 2025-10-31 04:06:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 7e86eab5-f9a9-3048-80dc-0f90788fc865 | -6.07795 | -37.46503 | 2025-10-31 04:06:00 | NOAA-20 | JANDUÍS | RIO GRANDE DO NORTE | Brasil | 2405207 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f859a496-d9ad-3620-82ba-fd85535b7c9c | -2.44615 | -49.01034 | 2025-10-31 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76380ad1-ab44-397a-8e61-64c1e5fe93cf | -4.8654 | -44.65107 | 2025-10-31 04:06:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23ae0b6f-db1d-375f-85c8-9f9e48bc3772 | -5.7457 | -45.5841 | 2025-10-31 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e3bf1f3a-8764-3a9b-a9df-d1f2a84c36b4 | -5.80067 | -44.43105 | 2025-10-31 04:06:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98338bb6-4665-3c3e-931a-46c424a1c3f2 | -4.92006 | -45.3214 | 2025-10-31 04:06:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b84e0ceb-c014-367f-b3df-bd5b4eea40d8 | -2.89495 | -45.48409 | 2025-10-31 04:06:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4d6bce9-768d-3960-ab78-4224d6eb6201 | -5.45023 | -42.72431 | 2025-10-31 04:06:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 29bf3e62-829b-3b49-b8ac-a5bc29130aef | -3.78653 | -43.90219 | 2025-10-31 04:06:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad4d6f2f-677a-3b59-a58e-39526ab01620 | -6.12388 | -41.5897 | 2025-10-31 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| b80c5451-6b1b-3a62-992c-48990f335b89 | -4.67073 | -46.52373 | 2025-10-31 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98a31d25-6040-32b9-9581-81fa2516cf88 | -4.85908 | -45.7416 | 2025-10-31 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 537dafc1-bc32-36c9-beab-d3205735f46a | -5.47883 | -40.89757 | 2025-10-31 04:06:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5dffe2f3-1564-350c-bc4b-ea297176a0d4 | -2.44515 | -49.01638 | 2025-10-31 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa83c2cc-37d9-3e21-8dc7-9eb5b396e698 | -5.28253 | -45.42405 | 2025-10-31 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6806d644-3fbf-3eb1-bf9c-0a03499cc053 | -3.45425 | -45.99147 | 2025-10-31 04:06:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 57465f5d-1bbf-3966-b039-064f3172eaf2 | -7.06709 | -42.0274 | 2025-10-31 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cd3407fb-4508-30d5-b74f-7967057b240c | -5.45139 | -42.71713 | 2025-10-31 04:06:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b6c67e9d-7b65-30bf-ab6b-a8dd738b3c5f | -4.35869 | -46.77972 | 2025-10-31 04:06:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2cdb0a5-0023-31a3-bc8b-06d186a6f9fc | -5.29034 | -45.19304 | 2025-10-31 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d142b185-4550-39d4-be67-cf69911249ae | -2.32081 | -48.58882 | 2025-10-31 04:06:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a0ecadd2-f9d9-3565-bb97-a5f7efe7783b | -7.35965 | -44.63263 | 2025-10-31 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| eb914cc8-8297-326e-aa06-aab4ebd0032e | -4.31397 | -45.75747 | 2025-10-31 04:06:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16944e68-cb08-3e03-95b9-4775a9fc45a6 | -6.66476 | -44.69125 | 2025-10-31 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 458bccfa-01d8-3031-9eeb-696c8236fd98 | -2.63367 | -48.50067 | 2025-10-31 04:06:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3ee87b10-8af3-391a-812e-7587b0b38869 | -6.01642 | -41.96671 | 2025-10-31 04:06:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2b085f8e-7833-352f-b13a-8932c18bd281 | -4.66724 | -45.0901 | 2025-10-31 04:06:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ccce4d4-8bda-3593-9ed9-5849853ad08d | -7.39533 | -43.67257 | 2025-10-31 04:06:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f3ad97ec-d29f-3245-8afa-1bc7aed7b53b | -5.80308 | -40.82128 | 2025-10-31 04:06:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8f2f35f6-2208-3383-8d39-a0308d6b02f5 | -6.95961 | -42.52956 | 2025-10-31 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 55e49782-cfd5-3c06-b2b8-3772e2a6dc42 | -5.79812 | -40.8312 | 2025-10-31 04:06:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 493f0745-1958-3cb8-b244-dc1774d828aa | -5.81106 | -40.83627 | 2025-10-31 04:06:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 98fcdc5f-5cc9-386f-90fa-c0f317c5e26c | -5.759 | -45.8691 | 2025-10-31 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce7e4350-e34f-30b2-af88-4069faaacf13 | -4.90064 | -42.97857 | 2025-10-31 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c2310a9-b625-3d5d-ad7e-e61cf458b0f5 | -1.9554 | -47.85531 | 2025-10-31 04:06:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 913f9a29-9b7a-3a14-97e0-0b74d69847df | -5.03415 | -43.61629 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 3d67e229-ee48-3748-9ce7-6096cab7855a | -4.47232 | -46.56575 | 2025-10-31 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 748a45d3-9b4b-3efb-b3f6-a300dfd778b0 | -5.43264 | -45.34103 | 2025-10-31 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77aa4964-b496-3d62-9b2c-1caf3ebc2a53 | -6.10306 | -41.74223 | 2025-10-31 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 721b2aca-7ac7-3485-89b8-cef65540220a | -4.21524 | -48.09378 | 2025-10-31 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b2eb278-7f44-3d38-97fb-b82bac7aaf88 | -5.41013 | -45.29123 | 2025-10-31 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b74c1d3b-53a8-334c-a440-95e87b6f7f35 | -7.21886 | -39.95386 | 2025-10-31 04:06:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b4699382-2450-3bcd-8139-a400122546cb | -2.92889 | -51.46845 | 2025-10-31 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 76ffb64d-9418-3699-9586-b4d3bb87e758 | -3.54433 | -49.33154 | 2025-10-31 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75d24ca3-4cd8-3822-883a-755d423635c3 | -4.3706 | -46.09905 | 2025-10-31 04:06:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ec1c74c-a5cd-3d8a-96e2-1c7dd7dd9710 | -4.6218 | -42.7916 | 2025-10-31 04:06:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6159448c-f358-3664-ae85-3d84a24d530b | -7.15802 | -39.46173 | 2025-10-31 04:06:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a0db0392-d0fe-3ca0-8ef2-44df13974a80 | -7.22179 | -44.32068 | 2025-10-31 04:06:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f6db636c-5150-36e1-b099-8916ec95cc9f | -5.03826 | -43.61294 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9e956a6e-cc46-3ba7-92d0-ce08d9d43a4d | -3.117 | -44.27085 | 2025-10-31 04:06:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 117f06cf-f2d8-377c-8bb8-2e4b432af3c7 | -3.54482 | -49.32853 | 2025-10-31 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9766e605-462b-3971-80f2-f2a412258eb5 | -4.85176 | -42.73429 | 2025-10-31 04:06:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c6fb44e-720e-3b9f-abdc-1b9ff97862b3 | -5.45857 | -40.87277 | 2025-10-31 04:06:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README19.md)
