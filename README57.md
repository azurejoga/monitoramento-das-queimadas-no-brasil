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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a4d1ed3-0073-372f-9b4b-c2cc69a788b6 | -1.37496 | -52.99082 | 2025-10-29 04:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1cdced1-f1a5-3d71-98cd-296bada4191b | -8.0067 | -46.20817 | 2025-10-29 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 113bcccb-f0d1-39c4-b939-e593fce111dc | -7.74647 | -44.72145 | 2025-10-29 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| afe57420-6162-399a-a77b-b728846f482a | -4.35459 | -43.64361 | 2025-10-29 04:44:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8e4aa7e-cfaf-393f-9625-67940f7c261c | -7.78844 | -46.4743 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 60e5f7dc-568b-3b24-a437-25d63a7128ca | -2.83234 | -49.40297 | 2025-10-29 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 37cf0c31-b920-3cba-be45-1a622b4f384f | -2.99549 | -51.25163 | 2025-10-29 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b1611c02-58aa-3fab-bcc9-7349a65e2539 | -7.00027 | -49.00838 | 2025-10-29 04:44:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e5f12eb-ac81-3752-bd5a-d3d354a03db4 | -7.01969 | -48.65271 | 2025-10-29 04:44:00 | NOAA-20 | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f9ed254f-64dc-3318-8265-b54cad1da7b7 | -5.33634 | -45.5414 | 2025-10-29 04:44:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a87dca80-dbf6-39af-b409-bbf8bd15d155 | -4.43668 | -50.90886 | 2025-10-29 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 757e6f6f-60ef-3258-9f0b-ef6341bad017 | -8.61944 | -44.79835 | 2025-10-29 04:44:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 278f102a-ba95-387c-a68a-77f5dc2c4520 | -5.65478 | -46.45315 | 2025-10-29 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| be47947b-97cb-3e07-880e-f742393b7ece | -4.29158 | -49.65174 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c17c1775-e6c5-31a1-b5a5-ab1e3786b55e | -4.91888 | -47.32314 | 2025-10-29 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0df8b3be-beb7-34ce-8170-410816f4bfb6 | -6.59555 | -46.27752 | 2025-10-29 04:44:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fd5a476d-79f1-3c5e-8524-1acfe140f265 | -3.71373 | -41.57468 | 2025-10-29 04:44:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fb698223-5d4d-33a0-a3ec-d485a60cc281 | -2.9394 | -54.20575 | 2025-10-29 04:44:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 09622af8-6e68-3803-8c78-e2cb94d0c45b | -8.19557 | -46.95044 | 2025-10-29 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 552cd73f-c99f-3915-8e2c-ecfeef01d72a | -6.58516 | -48.58571 | 2025-10-29 04:44:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0681a30-5143-3d4b-ac66-531168fd8c70 | -1.19669 | -54.21623 | 2025-10-29 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30075126-ab6c-3074-8a30-714b955b3c46 | -9.25195 | -45.56092 | 2025-10-29 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9bc1441-e223-3514-a8c2-b2a82ed525f4 | -3.99612 | -43.65804 | 2025-10-29 04:44:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd5a15a0-168e-36bc-88d5-3064c9cac0e0 | -6.1309 | -41.7107 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c2926d6b-094c-3b30-9909-e2e4b3e69bb9 | -7.32261 | -44.7401 | 2025-10-29 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0e5d2f7b-886a-301c-aaeb-f99b52da6b69 | -4.6449 | -47.95488 | 2025-10-29 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b9ac520-4ac2-31b2-9e14-614ccb2d46a1 | -6.11699 | -41.70864 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f1ac0e35-fdde-3444-9583-c18aa826b963 | -6.28122 | -47.87725 | 2025-10-29 04:44:00 | NOAA-20 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1e4cf46-54e0-3b26-8354-c4b4a00a7ebc | -6.48574 | -42.24554 | 2025-10-29 04:44:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a98fb698-9a08-33df-aba4-e3d48f0f704d | -6.10838 | -41.73071 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b77c5780-afdd-3478-b186-eca4f3ddda2a | -6.98587 | -46.23282 | 2025-10-29 04:44:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4b940ad0-35ed-3750-a775-376fab8e47cd | -7.33747 | -42.47432 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e93965ab-2e2e-39b6-ba36-aa99169139c2 | -8.25605 | -46.91527 | 2025-10-29 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b87a20ad-866b-3b5b-b06b-44cb7b71550c | -6.13195 | -41.86044 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e2b6d605-4632-3787-bd15-6a6702733fdd | 0.45507 | -60.48801 | 2025-10-29 04:44:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 44a75db7-2fc7-3052-be1c-86ec64ffce14 | -4.2074 | -50.07847 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| ec6c2c65-71b6-342b-9db5-441366528c04 | -7.98645 | -45.5356 | 2025-10-29 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1afce45e-428e-3334-8a22-238d296d9484 | -6.49655 | -42.23489 | 2025-10-29 04:44:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a772a1d9-4570-3a98-8510-bf44fbbda6ed | -4.29213 | -49.64825 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 70bb623b-baf5-3b42-ba79-d69326b612e2 | -1.27656 | -52.92536 | 2025-10-29 04:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe09c532-4a8b-354f-9407-415cfacee138 | -5.86027 | -47.69667 | 2025-10-29 04:44:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43ab4c86-406a-3675-aece-e93b25ec972a | -5.52266 | -45.4342 | 2025-10-29 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0912572-52df-3e24-9054-be3a6dfe2885 | -4.08807 | -46.93491 | 2025-10-29 04:44:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a3a9b7f4-7372-3361-ba26-d7f35b8cddbf | -7.89121 | -45.68721 | 2025-10-29 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93405cf5-080b-3636-8039-1ebeac2fd5a2 | -8.1903 | -44.44814 | 2025-10-29 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb5a7986-6877-3a4f-a93f-e7c4a9af03d2 | -4.96399 | -48.26182 | 2025-10-29 04:44:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1e4f591-33c0-33ac-bc38-857a84a88c6e | -3.60028 | -48.99044 | 2025-10-29 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65d96b87-f68c-3b94-8d7d-7a8a75739f1b | -2.42272 | -49.30724 | 2025-10-29 04:44:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| fd58be01-997e-3b13-9ad3-83fd05ec5b73 | -4.01802 | -48.98873 | 2025-10-29 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98fa7653-a08f-3994-ac4f-8cc94178a0e4 | -4.21954 | -50.08743 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f76ead80-44b5-3fbf-b46c-3e5c1e2be469 | -4.06499 | -49.36256 | 2025-10-29 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a267542f-de93-335d-9a5d-1a0c3826671d | -3.32291 | -52.62567 | 2025-10-29 04:44:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee84d127-a16a-379a-94a6-0742cbfe5aa6 | -8.72076 | -49.61609 | 2025-10-29 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2098622c-2494-31f1-b5ef-a66e1b59a878 | -6.96539 | -45.51773 | 2025-10-29 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 801da26e-6121-3c20-810a-cb364448361d | -7.07201 | -44.95689 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 90c517e7-f0ed-3a7b-afca-ed1b1763e741 | -2.80905 | -48.66773 | 2025-10-29 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6028b1a8-2228-3934-af77-9ebe2c6d1b3a | -3.0394 | -50.26809 | 2025-10-29 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1cd25b27-9b39-3b34-aaf5-a289b78648c2 | -6.13353 | -41.70741 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 88bb4542-85f1-3d5d-926d-356c783b0351 | -5.57272 | -46.52866 | 2025-10-29 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b02bf57a-3d6d-339a-aa8f-6bc47bc8ac38 | -5.61381 | -45.19143 | 2025-10-29 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 711caaa5-5fd7-373b-8cc9-017e73c5f312 | -7.3438 | -43.91339 | 2025-10-29 04:44:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4435bf3b-aa99-329f-8982-001cb7f30fb5 | -6.48452 | -42.24493 | 2025-10-29 04:44:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a7de9b74-31b2-361c-943a-be12fad49e41 | -7.80332 | -46.45584 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 41b336db-c042-39ef-a4a1-fd36b334b659 | -3.1786 | -45.65124 | 2025-10-29 04:44:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 82992eb6-694f-3462-bd3b-e8902330242a | -5.18528 | -44.36037 | 2025-10-29 04:44:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 45f0c8aa-14be-3ed3-8e65-00500e3988c2 | -7.60145 | -43.57248 | 2025-10-29 04:44:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5d0c050d-00a8-32fa-95fd-c35da46e4306 | -6.11599 | -48.10494 | 2025-10-29 04:44:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b486cb0b-e229-3aa9-95cf-b10e3fa12fa9 | -6.12848 | -41.84649 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| e9e13718-bf0f-3a88-ad5c-fec12db689b6 | -7.0775 | -44.9378 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c364964c-384e-3fdb-8436-7f2f5b55b411 | -8.25977 | -46.34947 | 2025-10-29 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b5d2bf7-5464-38db-899d-a75df897a48d | -4.75467 | -46.97672 | 2025-10-29 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d25537e-929c-3736-b428-ff7a6acad017 | -7.60065 | -43.57402 | 2025-10-29 04:44:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a22e4095-b8f0-3968-9234-5037e991a570 | -5.68032 | -47.82936 | 2025-10-29 04:44:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3fe62c6a-e9ba-34c5-926e-bcb0228a30ae | -4.10421 | -51.07553 | 2025-10-29 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0062bdc2-8129-3ea5-af13-a292a2902279 | -6.12321 | -41.84552 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 0e761bfc-5058-3055-939a-51e910786c4b | -4.22715 | -48.56787 | 2025-10-29 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d4aae37b-6f73-30bd-8140-c7b18ea3bdd9 | -4.70162 | -46.10357 | 2025-10-29 04:44:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a2dd832-d885-304f-bd1c-a70837445136 | -5.16572 | -46.16181 | 2025-10-29 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e40439c5-1c7c-3624-a9b1-4327f37b9922 | -6.9328 | -47.0018 | 2025-10-29 04:44:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9523f7d3-ea11-3d66-9eb2-a466d75ea410 | -5.60987 | -49.12067 | 2025-10-29 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 81bd5fa7-c599-3af8-8398-9bdc243cb82e | -5.4322 | -46.12611 | 2025-10-29 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5abec169-d4a8-3a43-96f2-6c5f4ffa7356 | -8.2128 | -43.80782 | 2025-10-29 04:44:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a257d6fe-2284-32b4-be74-117092fb5eb1 | -8.17622 | -45.71836 | 2025-10-29 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 44b2a23c-40b3-3e22-9c7a-6a4b51628e61 | -6.13588 | -41.71409 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e343d0af-fb7a-323f-bda4-f8809093f982 | -6.80311 | -49.35391 | 2025-10-29 04:44:00 | NOAA-20 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 23054699-1c69-3b20-8e44-1533d44e3674 | -2.96167 | -48.59557 | 2025-10-29 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d39d0b3b-a247-37f6-a2ae-9dd0c17ee16f | -6.11787 | -42.44498 | 2025-10-29 04:44:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 669bfbe0-633b-3fb2-957d-cc9b6fb826c3 | -6.67361 | -44.69399 | 2025-10-29 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6d47e9bd-86a1-3d3b-903e-ed178b61e8e0 | -8.14301 | -49.48014 | 2025-10-29 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4352be90-e001-304e-a6fc-06ca2f2eabbb | -4.25131 | -48.57112 | 2025-10-29 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19f7f560-a848-3da6-9b60-ec702d62b730 | -5.07048 | -47.11354 | 2025-10-29 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 83452303-cc79-3b63-bf9d-dbc6dafda040 | -6.12892 | -41.84327 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 303a94a5-bcb0-360d-ae94-1d965ab2b590 | -7.78354 | -46.45266 | 2025-10-29 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 40546432-c7ba-3556-a8af-f1fd5c7c4df1 | -5.71043 | -49.30626 | 2025-10-29 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| faf08127-2a57-31b4-a8fb-3d8ce5866f76 | -6.14084 | -41.7176 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| aa63d403-be3b-3612-ad27-6151b1de7871 | -5.11692 | -49.26316 | 2025-10-29 04:44:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d1c182b-e08b-3640-9ff7-a6e55406ac41 | -4.25105 | -48.57148 | 2025-10-29 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d97af587-19da-3fd5-aa2a-a6015c9babba | -8.35949 | -47.26363 | 2025-10-29 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 451cb215-7349-3ce5-b627-4df31be01bd9 | -6.49613 | -42.2378 | 2025-10-29 04:44:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b35ec416-f372-3b91-876a-45d7a6e54ec0 | -2.90704 | -40.34407 | 2025-10-29 04:44:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |


[Clique aqui para ver as próximas entradas](README58.md)
