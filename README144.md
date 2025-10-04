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

## Dados Diários - Página 144

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7104ab1-aaa4-3cfe-97eb-f7d0d868be0a | -9.92341 | -50.20414 | 2025-10-04 12:19:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 682e48f6-d130-3265-92fd-a3fb0857069d | -11.13721 | -47.90965 | 2025-10-04 12:19:00 | TERRA_M-T | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 089a1506-a293-339b-9b37-8ee6cadb8d52 | -13.69201 | -48.02869 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 44c8f001-07cb-3935-b3c4-bba2da938f18 | -14.97669 | -49.97772 | 2025-10-04 12:19:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a1527a97-80b8-3fc2-917c-1d48acbb1907 | -13.24794 | -47.24968 | 2025-10-04 12:19:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 772ee627-610d-346b-a794-ebd3c897916d | -13.31766 | -47.60808 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 21.9 |
| a3d35b86-5ff4-3725-b260-17f245837e7a | -9.32173 | -45.74241 | 2025-10-04 12:19:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 8c56cd67-680c-355d-a66a-afb444cb0efa | -14.65732 | -48.23109 | 2025-10-04 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 455a4002-71c6-3d0e-b40d-fe9570968fa5 | -12.58008 | -48.13488 | 2025-10-04 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| c47a9911-57a1-3f16-adcf-8437b3e22b6b | -14.87074 | -48.35589 | 2025-10-04 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 025ca1d8-8630-3a72-b450-73a4f07e62e1 | -14.75152 | -50.00129 | 2025-10-04 12:19:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 27.2 |
| e2efafcf-7e88-3b16-b7b8-6d3363b63ae6 | -15.61725 | -49.12714 | 2025-10-04 12:19:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 7c927ba4-90a0-37a6-be48-c9fb98b555de | -10.99885 | -46.66796 | 2025-10-04 12:19:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| dfab9878-3d21-3393-b1d3-e8c22d095e01 | -12.92724 | -46.3634 | 2025-10-04 12:19:00 | TERRA_M-T | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8c3836bc-92d0-3267-aaf5-8f26117375c7 | -12.8614 | -47.04879 | 2025-10-04 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 48.9 |
| ca1cfc75-5113-34d1-9f72-d27ecddc515c | -12.72855 | -48.57327 | 2025-10-04 12:19:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 74be31e8-8ff7-3881-b446-e5f307a637d0 | -17.59103 | -44.46479 | 2025-10-04 12:19:00 | TERRA_M-T | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 5c5862c8-2f97-3ba3-bde7-0eccaf4a8c44 | -10.81567 | -47.95719 | 2025-10-04 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 394e8161-0f97-3e95-b1f8-71ae10224334 | -16.39441 | -52.15617 | 2025-10-04 12:19:00 | TERRA_M-T | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 6e87ea03-1cdb-319f-b78b-e87ed8df9229 | -12.24547 | -47.83196 | 2025-10-04 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| c2d67978-641b-36d7-8eb7-50adefb71462 | -9.58975 | -45.26747 | 2025-10-04 12:19:00 | TERRA_M-T | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 03d49b5f-5303-3a18-81eb-adf7db51a8a1 | -17.25264 | -48.11526 | 2025-10-04 12:19:00 | TERRA_M-T | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 6bb333f8-bbd7-38b0-be67-e893a140a0ab | -12.9405 | -50.99964 | 2025-10-04 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| e2500e6b-870a-3f74-9959-8efe1908de57 | -12.09448 | -45.17476 | 2025-10-04 12:19:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |
| a0527081-adc1-381e-a086-e28c437395b0 | -13.305 | -47.5682 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| aab0dde7-5580-3fba-861d-1024cb07f25f | -11.88401 | -44.98883 | 2025-10-04 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| f882207e-d5cb-3d71-ae5f-ce39f58e76a8 | -9.33485 | -45.78403 | 2025-10-04 12:19:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 6b396490-26b8-30fa-b2db-80e0fd47fbbb | -10.77851 | -46.59643 | 2025-10-04 12:19:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 5acb1eaa-ef0c-3423-9a0b-d73ad8686983 | -15.38665 | -47.96233 | 2025-10-04 12:19:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 27.9 |
| a9d822dd-32ee-3e89-8b13-358922e7d6d0 | -13.50287 | -47.26996 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 75c4c9bd-fe65-3b6f-83df-bc59a63c5c69 | -14.68192 | -48.25977 | 2025-10-04 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 5ec29e8b-a027-311d-941f-c19a6347b94e | -13.47583 | -47.26595 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 4e6a7ea6-dcd6-37cf-a023-9f1f35658936 | -16.97655 | -48.38212 | 2025-10-04 12:19:00 | TERRA_M-T | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 4a471882-b17a-374f-88fe-723b1211f7df | -12.535 | -45.9864 | 2025-10-04 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 286.6 |
| 21d1dc91-fe79-370c-ab7f-5be647fbc551 | -13.2938 | -47.5905 | 2025-10-04 12:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 438f3659-dd31-3513-9598-c0a747b64fd2 | -12.031 | -45.2132 | 2025-10-04 12:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 142.7 |
| de638341-bf45-38fa-a033-0b3a124f7d67 | -15.3601 | -47.9554 | 2025-10-04 12:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 56810c10-733b-32f3-b18d-243e39bd84c9 | -11.5683 | -47.6749 | 2025-10-04 12:20:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| dc0ca3ae-f602-3e89-9a7e-7234ce22902a | -8.2314 | -46.8289 | 2025-10-04 12:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 7f477772-7785-3d83-ae42-0151f9d5a218 | -13.3426 | -48.0742 | 2025-10-04 12:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 170.0 |
| 76e279fb-2758-3955-874d-98131a31b404 | -9.3382 | -45.772 | 2025-10-04 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 909379ce-c82f-385a-933a-0bb1088669a6 | -12.8614 | -47.0486 | 2025-10-04 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 2672d761-9e23-3e0f-b757-283f130cecd8 | -12.0699 | -45.1843 | 2025-10-04 12:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 9a0f3b86-569d-3a74-87b9-fecdbc9fb5b5 | -13.343 | -48.0519 | 2025-10-04 12:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 68176220-8c2e-35ea-8f08-b7a5b99240d2 | -12.0314 | -45.1901 | 2025-10-04 12:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 210.1 |
| b064df09-212a-302b-b36f-378b39dcdb0b | -15.5408 | -46.8344 | 2025-10-04 12:20:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 142.9 |
| fbf3662b-024b-3058-bcd6-9e271f75219f | -14.2325 | -46.0563 | 2025-10-04 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 398426de-8402-31fb-ba92-9446110f54e5 | -14.5941 | -52.4976 | 2025-10-04 12:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 60295759-9e1b-3620-8020-78b69bafea76 | -14.2131 | -46.0596 | 2025-10-04 12:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 184.1 |
| cb6b8b41-0da9-363c-9058-06e386f6d785 | -11.1458 | -47.9054 | 2025-10-04 12:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 41fc4c60-9842-37bb-a572-2661532be2a3 | -13.114 | -47.9518 | 2025-10-04 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| d38b51f4-1a2d-3e8c-b7e8-1f5d28f46253 | -14.0509 | -53.9289 | 2025-10-04 12:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 071dcd6e-0029-31c8-8f66-6ebdfeeb0ac1 | -14.2126 | -46.0827 | 2025-10-04 12:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 2cbb2ff9-18bd-31b9-afe9-83ca4f917417 | -13.3619 | -48.0713 | 2025-10-04 12:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 07741847-31f7-36f8-94b3-7a5af73b79d8 | -15.9574 | -43.3423 | 2025-10-04 12:20:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 7e003e54-eef1-3c52-80f9-0bc004091b0e | -10.3346 | -50.3188 | 2025-10-04 12:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| b74423c5-b1a3-3732-bcd8-79dc3e7b7a45 | -8.8534 | -46.7451 | 2025-10-04 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 094b5be2-4306-3e14-9fad-ff767e16409b | -12.6512 | -46.9894 | 2025-10-04 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| d5c51c20-4a52-33d6-97f2-9a9af0c12e38 | -11.5492 | -47.6773 | 2025-10-04 12:20:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 73164d0f-d715-3274-82aa-4b8ed5fb4332 | -7.8593 | -48.2037 | 2025-10-04 12:20:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| db28090f-5e21-35a1-a035-4a6795d34bf0 | -7.7687 | -46.2255 | 2025-10-04 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 02b4bef4-bd27-316c-8297-78ed0f85517b | -10.5835 | -48.7178 | 2025-10-04 12:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 3e4b44b9-7046-3c71-b22b-8c9d4e1d6c9b | -13.3127 | -47.61 | 2025-10-04 12:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 457c78a4-b9fd-39e9-9751-a91d5f547ca6 | -15.958 | -43.318 | 2025-10-04 12:20:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 177.6 |
| f6940e3f-3c2c-3614-9d24-79caafbe9468 | -8.8526 | -46.812 | 2025-10-04 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| cb2fe52e-a7fd-35a8-a83a-b4aeac68fa9c | -12.0891 | -45.1814 | 2025-10-04 12:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 99678db1-5653-362d-9294-cc84640bb75e | -12.7194 | -48.5611 | 2025-10-04 12:20:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 61e6b6ed-595e-3316-8960-af92a5b3c193 | -10.3343 | -50.3402 | 2025-10-04 12:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 6f02356b-b061-3148-908c-c4bd5c03721c | -14.2321 | -46.0794 | 2025-10-04 12:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 5094e295-b828-316a-85ec-767d28a151d8 | -14.5748 | -52.5001 | 2025-10-04 12:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 94.3 |
| d3b6ada2-667c-34f8-98b6-9d877104e4a9 | -13.8283 | -43.1702 | 2025-10-04 12:20:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 117.5 |
| 1f11c7cc-94c0-3daa-9ff6-bd81a7544ac3 | -11.8818 | -44.9815 | 2025-10-04 12:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 3a59c687-fe5c-3c26-a9a7-ce7c81a8a478 | -13.116 | -47.8401 | 2025-10-04 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 99123841-b189-3e8c-b9dc-acd71b9df8c9 | -21.4482 | -46.5494 | 2025-10-04 12:21:00 | TERRA_M-T | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 30.5 |
| d4c5a0e8-c136-3ea1-89d3-aa6589ba7a07 | -20.90297 | -54.42898 | 2025-10-04 12:21:00 | TERRA_M-T | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e2300d28-1b16-3f42-98cf-04852d18dce4 | -22.28727 | -46.7676 | 2025-10-04 12:21:00 | TERRA_M-T | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 9030600b-be8d-31ab-924f-a9bbaafc5fa9 | -22.28881 | -46.75495 | 2025-10-04 12:21:00 | TERRA_M-T | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 34.4 |
| 60a6e2e0-0135-30ff-95bf-0e0862fb0b6b | -19.817 | -46.0625 | 2025-10-04 12:21:00 | TERRA_M-T | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a4e42370-c941-37c4-87ae-841d50162e76 | -21.88317 | -46.90685 | 2025-10-04 12:21:00 | TERRA_M-T | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 78ef761a-39c2-3645-affa-f73ec6f5c3cf | -22.27857 | -46.7537 | 2025-10-04 12:21:00 | TERRA_M-T | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| 1f9ba754-7569-3b0d-b75e-37a046725150 | -20.18395 | -45.73197 | 2025-10-04 12:21:00 | TERRA_M-T | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 789acaf6-8aa7-3505-a7ff-4c23849011c4 | -19.81919 | -46.07001 | 2025-10-04 12:21:00 | TERRA_M-T | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 31d11f08-bebd-3b6c-8395-a9bf7d09da0f | -23.70999 | -51.80184 | 2025-10-04 12:21:00 | TERRA_M-T | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| c4a7497f-f07f-3b0d-bf53-7b6111c59373 | -21.83694 | -46.5349 | 2025-10-04 12:21:00 | TERRA_M-T | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 2b4c1a13-1800-3495-8aba-c592e86f61a8 | -23.95207 | -49.85686 | 2025-10-04 12:21:00 | TERRA_M-T | ARAPOTI | PARANÁ | Brasil | 4101606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 070dccff-3369-3dee-8361-aa20b4cb5c6b | -21.83538 | -46.54785 | 2025-10-04 12:21:00 | TERRA_M-T | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 98835c55-2718-3a66-8e88-b528a3ed6024 | -29.77729 | -51.78858 | 2025-10-04 12:23:00 | TERRA_M-T | TAQUARI | RIO GRANDE DO SUL | Brasil | 4321303 | 43 | 33 | nan | nan | nan | Pampa | 4.6 |
| 5a8c139b-3ade-3039-8cfe-ca5a76b6ff04 | -29.77872 | -51.77833 | 2025-10-04 12:23:00 | TERRA_M-T | TAQUARI | RIO GRANDE DO SUL | Brasil | 4321303 | 43 | 33 | nan | nan | nan | Pampa | 4.1 |
| 9964c04a-3c02-3377-a18d-2cb163188cd4 | -8.2316 | -46.8066 | 2025-10-04 12:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 12522779-28c8-30ee-bf16-efb6e63801e2 | -13.8283 | -43.1702 | 2025-10-04 12:30:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 115.4 |
| a1725dc0-a621-383c-90b0-a5a21d5da71b | -11.5069 | -46.7671 | 2025-10-04 12:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 152.3 |
| c9cf3778-6c0c-367c-b291-57b4bbc47b4f | -14.3171 | -52.9131 | 2025-10-04 12:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 948ada32-48d6-3d17-921a-c41f495bd0aa | -14.5941 | -52.4976 | 2025-10-04 12:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 129f87be-729c-35e5-acaf-361e22585983 | -11.863 | -44.9612 | 2025-10-04 12:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 53bef35f-7dd8-3ec8-a656-3e251e97b2fb | -10.3346 | -50.3188 | 2025-10-04 12:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 1bb1a09d-c28e-3ef4-88ee-ed475dd3b08f | -13.8087 | -43.1739 | 2025-10-04 12:30:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 112.3 |
| 0be87d8f-011e-3ad8-8480-e1f2412600f1 | -11.5683 | -47.6749 | 2025-10-04 12:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 144fc6db-bd68-306d-a7a4-bb881ad0f8a0 | -8.2128 | -46.8084 | 2025-10-04 12:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| fdb189c8-2fc0-31b9-a136-f94a697e732a | -13.3233 | -48.077 | 2025-10-04 12:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 81.7 |
| e7ac7e17-c915-3e94-a885-4acec49525ee | -8.8526 | -46.812 | 2025-10-04 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |


[Clique aqui para ver as próximas entradas](README145.md)
