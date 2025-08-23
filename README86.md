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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 776fb90b-926a-3d91-98b3-bee7f93ec9a1 | -6.13347 | -43.94843 | 2025-08-23 12:34:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 172.9 |
| cf09d164-3e4c-3d45-875f-22fe7242c713 | -10.22389 | -48.28015 | 2025-08-23 12:34:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1bcf7bfe-9e93-3649-bb09-c64644e515a4 | -13.37271 | -46.21022 | 2025-08-23 12:34:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 262340df-3982-3714-b5c6-e136bd5c5d81 | -5.82569 | -52.06439 | 2025-08-23 12:34:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 080d567a-0a4e-3c87-bf59-b55c3ee267bb | -5.68676 | -41.39522 | 2025-08-23 12:34:00 | TERRA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 53.4 |
| 02aa0462-225a-3c59-86bc-73d8d2c5ad2d | -9.44895 | -47.65462 | 2025-08-23 12:34:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| e47017b9-db85-3c6c-a29f-1d1e96336709 | -6.58718 | -44.55069 | 2025-08-23 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 79c1c5d9-ae4e-3bc8-a5bd-17db2103fb19 | -13.37274 | -47.50854 | 2025-08-23 12:34:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 58fd3077-b3e9-3df8-9ad9-54ee4a6c1392 | -11.65282 | -51.59039 | 2025-08-23 12:34:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 18.8 |
| ea23ca62-1e62-3af2-9891-08244eac1469 | -10.69012 | -50.12869 | 2025-08-23 12:34:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 52979be2-51b3-31e6-8345-a898ceded0b8 | -11.12014 | -44.77272 | 2025-08-23 12:34:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 2a12a400-f227-35a7-a0f9-5e7a35e86962 | -7.63881 | -45.23278 | 2025-08-23 12:34:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 8e9ed4c4-1fd8-3c6a-8d8f-55b0ad841d16 | -11.50816 | -50.47456 | 2025-08-23 12:34:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f8967040-8f8d-3a38-901b-7a99491c7609 | -10.64525 | -50.12242 | 2025-08-23 12:34:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 89b0f0be-5506-3d1a-b2d7-814fa4a13cec | -14.09405 | -43.91825 | 2025-08-23 12:34:00 | TERRA_M-T | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 45.6 |
| de4ccb4b-a9c7-3897-8dbc-36d714041352 | -10.62087 | -50.16597 | 2025-08-23 12:34:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 27a02f9f-4d9d-3c36-94ed-9e4c6da12f93 | -10.47893 | -46.82153 | 2025-08-23 12:34:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| cfb326b9-e470-348a-bec6-ce206a94dbe2 | -10.6337 | -50.1396 | 2025-08-23 12:34:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 26.8 |
| cb29a947-7042-377b-83d8-3c8dc0ccaf66 | -5.83488 | -45.18133 | 2025-08-23 12:34:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 169.6 |
| 449148f0-8e4b-3e5e-b540-c921c4b9f962 | -12.16903 | -44.60495 | 2025-08-23 12:34:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| d7e70f2d-2c8b-3aa5-bb3e-ae19e7127a60 | -12.79879 | -48.7187 | 2025-08-23 12:34:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 4bc4cdb1-95ef-3611-82f5-021e152c2995 | -11.13306 | -44.77437 | 2025-08-23 12:34:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 27d909aa-41ce-3753-86a9-850e56e1275c | -13.4665 | -46.55288 | 2025-08-23 12:34:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 25.4 |
| a1f3edb3-7ae7-3295-b545-57d5ce83e589 | -7.03376 | -44.6379 | 2025-08-23 12:34:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 0db93cfb-0aad-37e9-9e23-07479018a618 | -10.56575 | -47.14603 | 2025-08-23 12:34:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| cdcdd981-1244-36d4-9da3-b64d73370942 | -8.74126 | -45.45384 | 2025-08-23 12:34:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| ff65237e-23f6-31ef-a20e-39a70cb6eca5 | -10.22244 | -48.2911 | 2025-08-23 12:34:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 7ccb4787-19a2-35c0-96bd-b5c801c5a96a | -5.82425 | -52.07405 | 2025-08-23 12:34:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 4af41ce7-5a1e-3fc4-80ae-b389aea7ef03 | -10.64396 | -50.13164 | 2025-08-23 12:34:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0d9ce90a-7f84-3bdf-b530-dad5e8e3d428 | -8.1753 | -47.32787 | 2025-08-23 12:34:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 778b9aa1-7e76-3ebb-b81c-9e563ad065a9 | -8.78878 | -47.31926 | 2025-08-23 12:34:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0ddadb24-0277-349b-abba-a572f57fe3ae | -12.71601 | -48.11437 | 2025-08-23 12:34:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9dc8e4eb-9c68-39c9-9f35-714b8fb726cb | -6.7984 | -44.9851 | 2025-08-23 12:34:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 44072c8f-461c-384d-bc65-29abf4462cc2 | -12.99511 | -45.22514 | 2025-08-23 12:34:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 953e0148-ddcc-3c05-82e2-ecd25d5d07d0 | -11.32144 | -47.85118 | 2025-08-23 12:34:00 | TERRA_M-T | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 118dcb37-d0f7-3c38-bdcb-48c169222531 | -8.74606 | -45.44806 | 2025-08-23 12:34:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 1beaaa0b-519b-33c4-9bcc-d38f4b7e83cd | -7.02737 | -44.6254 | 2025-08-23 12:34:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 6cf56de9-58c8-3ea7-a6fb-bf85208d6b76 | -12.32006 | -44.87246 | 2025-08-23 12:34:00 | TERRA_M-T | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| d5559b0f-28d8-35f0-b79c-e68c7c15ea0f | -13.48879 | -47.03531 | 2025-08-23 12:34:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 6092e436-66f0-342b-8b34-623efcded3f5 | -12.54367 | -45.61511 | 2025-08-23 12:34:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 36.3 |
| c3feec2c-b8e2-3043-844f-601638ba1be6 | -7.62497 | -45.24723 | 2025-08-23 12:34:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 82a8053a-8316-3cab-a467-4f381e26d2de | -6.27599 | -52.82288 | 2025-08-23 12:34:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 983d370c-0597-3f61-86e0-bcb3a63f1113 | -7.02508 | -44.64346 | 2025-08-23 12:34:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 169.2 |
| 9d6609ce-4dce-3302-ae23-140d1a130c5d | -12.99439 | -45.23163 | 2025-08-23 12:34:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| dc9b9b7d-5b32-33d6-aa8c-493fd701c23e | -8.33783 | -44.7855 | 2025-08-23 12:34:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 1a646270-e326-300f-ac1d-fcfc83136232 | -5.10776 | -43.21655 | 2025-08-23 12:34:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 8ad4b786-d4a3-341a-861b-d71ec579fe4a | -9.15037 | -47.5962 | 2025-08-23 12:34:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 0c2b5195-655a-374d-a173-d5b36086f07d | -9.73769 | -47.93983 | 2025-08-23 12:34:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 09bbc433-93ec-3a3a-a0eb-41ebdde6a6f2 | -6.59111 | -44.55685 | 2025-08-23 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 79dd4ceb-0eae-3e76-9b68-007dc7cd7d0e | -12.99672 | -45.21147 | 2025-08-23 12:34:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 8424e114-af11-324a-ba84-17fe83db664b | -7.84419 | -46.97839 | 2025-08-23 12:34:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 45eabce4-e22b-3b6f-83de-33996a199434 | -9.96427 | -54.93337 | 2025-08-23 12:34:00 | TERRA_M-T | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| e482aefc-87b3-3b7b-a2c0-7f0d788d9412 | -11.7068 | -51.66826 | 2025-08-23 12:34:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7200ec8e-ca64-3f1a-964d-b92169803a76 | -7.18708 | -48.42825 | 2025-08-23 12:34:00 | TERRA_M-T | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 83f82192-794a-3c64-b6b5-44075d6f6419 | -6.55217 | -45.47253 | 2025-08-23 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 2b63feaf-f01e-351d-8392-2fa526a9f144 | -9.04459 | -47.6237 | 2025-08-23 12:34:00 | TERRA_M-T | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 5e25736f-3b4c-3b88-90cb-c26668a02b0d | -12.95942 | -46.30636 | 2025-08-23 12:34:00 | TERRA_M-T | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 5cd871bc-9bc0-387f-8404-13e94945b645 | -9.85213 | -44.68817 | 2025-08-23 12:34:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 1787a056-6396-3e8e-8561-9673c238923f | -11.65412 | -51.58143 | 2025-08-23 12:34:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 3473b885-6c52-3adc-aaa8-9bf9f7602738 | -7.63995 | -46.27634 | 2025-08-23 12:34:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 30b45fae-726f-3bd4-b4f3-f567f070e0af | -9.04305 | -47.63524 | 2025-08-23 12:34:00 | TERRA_M-T | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 78664ab4-0a2a-398c-8d30-a5492fa3640e | -10.57634 | -47.14746 | 2025-08-23 12:34:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 8d5c80de-441d-35e2-b04a-b61d3e6b88ce | -11.50945 | -50.46539 | 2025-08-23 12:34:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 5799af2a-b841-3889-b372-dcaba8e9ec4c | -13.48894 | -47.02896 | 2025-08-23 12:34:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 90f46de8-74fd-3dc5-828e-0fc1e1416692 | -6.37133 | -44.74611 | 2025-08-23 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| b32a6f41-bd8f-3d5f-b63a-1bc3d7e1a6a4 | -12.65438 | -47.8081 | 2025-08-23 12:34:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| ec73d23d-faa3-32bd-adf4-73e6d929a070 | -10.56743 | -47.13298 | 2025-08-23 12:34:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 2c0ea21e-523a-3a0e-9969-f9f687ae2212 | -11.13548 | -44.75396 | 2025-08-23 12:34:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 4baefb34-06b3-305f-a5c0-0f425f14dc9f | -8.24695 | -47.40273 | 2025-08-23 12:34:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b9aa7287-0ab4-37a3-ad0e-3767bcf224b9 | -6.9516 | -44.28398 | 2025-08-23 12:34:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 36d3d9de-7a33-3d2b-a2f6-540a8b665eae | -11.89724 | -47.11612 | 2025-08-23 12:34:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 497ff7ed-e1bd-3c4c-b22c-4a18b75404dc | -12.71543 | -48.10782 | 2025-08-23 12:34:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 6722d731-06a3-3ede-b687-2b6889ab1bbe | -6.5235 | -43.86231 | 2025-08-23 12:34:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 1827ae13-ffb8-384d-ae8d-61e51dea87cd | -7.6064 | -44.37265 | 2025-08-23 12:34:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 300a71e2-4dad-3cb8-b6bb-564ba7b5f0d5 | -5.34553 | -45.14853 | 2025-08-23 12:34:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 1499f337-cd16-31ed-ba05-f9ff1e982f3e | -7.02281 | -44.66129 | 2025-08-23 12:34:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| df9dd76f-2fe3-3bf1-9654-60b4e2afa4fd | -8.94384 | -40.61475 | 2025-08-23 12:34:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 59.8 |
| 2bdd8dba-dd7a-3dd6-b73c-5cd3c97dfd66 | -13.46795 | -46.56365 | 2025-08-23 12:34:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| a80b4a6d-0205-3bd2-bec3-e6960bd80615 | -6.37775 | -44.74104 | 2025-08-23 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| f68f7dc2-834f-3601-bba4-a9cd46d39c92 | -6.48267 | -43.47075 | 2025-08-23 12:34:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 43d8489f-76a9-3cc1-ae78-6f5be8d5ae35 | -8.43691 | -48.25375 | 2025-08-23 12:34:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 9b7213ab-6f03-3c12-9d22-e7a52c55b3ec | -11.18944 | -55.02151 | 2025-08-23 12:34:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 67cc10a0-ec90-37e2-b0b2-3cff40c4954e | -11.6258 | -50.42258 | 2025-08-23 12:34:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 82042b4f-2780-33ce-9a8d-f4f12a762102 | -6.19204 | -45.42357 | 2025-08-23 12:34:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 5b89a2c5-6aca-37b5-b0bf-cf1478998271 | -6.55019 | -45.48767 | 2025-08-23 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| a42a9471-783e-3646-a8d3-d3c1bbb89dff | -7.01911 | -44.6544 | 2025-08-23 12:34:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 39e05616-0d88-379b-8b0d-e78222cbce92 | -6.58884 | -44.57447 | 2025-08-23 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 07fb5aa8-9333-3d27-88ed-dc07a9515b81 | -9.32794 | -48.25239 | 2025-08-23 12:34:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| e5e1fed7-b8f5-3e7c-86b7-1bedce9e6e3e | -6.18999 | -45.4384 | 2025-08-23 12:34:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 087f4323-d8ae-39b9-91e4-8453eb42e271 | -13.04871 | -46.32362 | 2025-08-23 12:34:00 | TERRA_M-T | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 558fa440-bd8a-368b-83fe-d048415b4f32 | -4.22492 | -47.21115 | 2025-08-23 12:34:00 | TERRA_M-T | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 88916f75-761c-305a-8813-442e7bdbb36e | -13.37429 | -47.49615 | 2025-08-23 12:34:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5b556315-5a2e-37f1-b31d-23488083dbde | -13.43385 | -46.25969 | 2025-08-23 12:34:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 4d2c8579-e4ae-3b5b-ba2e-345fdfa5f37e | -12.55375 | -45.63497 | 2025-08-23 12:34:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 8bc845c3-d245-3ee4-a2aa-e2aec97305fe | -11.19777 | -55.03545 | 2025-08-23 12:34:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 5ecb3288-3b21-34b5-888e-ecb29af14049 | -14.67427 | -54.90715 | 2025-08-23 12:36:00 | TERRA_M-T | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 3d0c1447-dd99-39e7-a830-fafb4b8d5b12 | -14.37912 | -52.05774 | 2025-08-23 12:36:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 808014f9-935b-33bf-8f2a-632d27e70846 | -13.87983 | -47.38195 | 2025-08-23 12:36:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 6b1fe59b-1772-3c7b-b299-8273a22ef216 | -20.15723 | -47.84278 | 2025-08-23 12:36:00 | TERRA_M-T | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 259.3 |
| 713bb01a-fa79-374e-b726-450b0b0af130 | -14.68393 | -54.90874 | 2025-08-23 12:36:00 | TERRA_M-T | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 44.9 |


[Clique aqui para ver as próximas entradas](README87.md)
