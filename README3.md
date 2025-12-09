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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0a211af-6d81-34f2-a6b5-dcad6404491c | -4.2959 | -45.9161 | 2025-12-09 00:40:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 9be6a092-8b8b-38f8-a789-3d653569e652 | -4.1819 | -46.3004 | 2025-12-09 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 74.3 |
| ab3b4c0a-5494-3ff7-a05e-607eee74e5c9 | -4.1635 | -46.2791 | 2025-12-09 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 78.2 |
| a90e3255-0149-3d50-a93e-c7ebb0ad6102 | -4.2959 | -45.9161 | 2025-12-09 00:50:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 90.6 |
| ed5cb675-dc88-3815-a20a-186c522f75a8 | -5.0026 | -41.3062 | 2025-12-09 00:50:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 51.2 |
| e09e3d0f-0cd0-3817-896f-f389189b213b | -3.4449 | -41.6653 | 2025-12-09 00:50:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 214.1 |
| 7351017b-47a4-3480-a221-39a5d9d0e464 | -4.2772 | -45.9394 | 2025-12-09 00:50:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 100.5 |
| b0b2d276-951a-363a-8acf-26fa9224a9ba | -4.1821 | -46.2782 | 2025-12-09 00:50:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 98aed8bd-69b5-3493-9523-f26e22e6e4c8 | -4.3144 | -45.9375 | 2025-12-09 00:50:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 4e059551-0c37-3052-b617-f4b0d7b92a4f | -4.2958 | -45.9385 | 2025-12-09 00:50:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 209.8 |
| 75a4e137-a58f-38cc-918e-cd906a5e3953 | -3.4262 | -41.6662 | 2025-12-09 00:50:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 157.6 |
| 9a1c7084-ba5a-32a1-a2b4-327e9c4128df | -3.4451 | -41.6413 | 2025-12-09 00:50:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 171.6 |
| 913359c3-074b-36c8-8620-d13e0399c7a6 | -3.4264 | -41.6423 | 2025-12-09 00:50:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 123.7 |
| f347093f-da39-3049-93ad-dfc938e51729 | -5.7093 | -42.0674 | 2025-12-09 01:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 52.7 |
| df25e769-8f21-3680-95e9-3fa0c3177304 | -3.4451 | -41.6413 | 2025-12-09 01:00:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 134.1 |
| 676e3446-44a9-3807-aa36-7957da38c054 | -3.4264 | -41.6423 | 2025-12-09 01:00:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 135.2 |
| 46dbae5a-423e-33d0-9af0-2ecd74310911 | -3.4262 | -41.6662 | 2025-12-09 01:00:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 144.7 |
| 64bc0a5d-a339-3d96-a5e9-ae52824558d9 | -5.0026 | -41.3062 | 2025-12-09 01:00:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 58.4 |
| 44eeeb41-9000-31d0-bba1-d66864dc8d6d | -4.1821 | -46.2782 | 2025-12-09 01:00:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 65cf52fc-ad6c-3e99-81e7-05a5a8fd6f0a | -4.2772 | -45.9394 | 2025-12-09 01:00:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 8dd9169c-0864-3cab-9c16-bcfeac627c7f | -4.2959 | -45.9161 | 2025-12-09 01:00:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 0b0ae525-2c31-3121-bf94-6d12bcd77d0e | -4.3144 | -45.9375 | 2025-12-09 01:00:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 71.3 |
| bd46bb8c-4cc6-37ee-9112-c5797c991403 | -4.2958 | -45.9385 | 2025-12-09 01:00:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 149.5 |
| b0f04cb0-2c2b-3f2f-b7ff-64a7fa8d1411 | -3.4449 | -41.6653 | 2025-12-09 01:00:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 139.6 |
| 45401942-50ed-30c5-ae48-cc272c3ecaf0 | -4.1821 | -46.2782 | 2025-12-09 01:10:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 66.9 |
| ad565913-303a-363d-8b36-906d5c86f0e4 | -2.0651 | -46.5108 | 2025-12-09 01:10:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 60c6f039-cd0d-3a13-91e4-b1971ebed563 | -5.0026 | -41.3062 | 2025-12-09 01:10:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 54.3 |
| 82842125-2d33-383e-a2ff-ee52639eabb0 | -3.4451 | -41.6413 | 2025-12-09 01:10:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 137.3 |
| fddc72b5-5068-38d3-9297-d36e9a5b668b | -4.2772 | -45.9394 | 2025-12-09 01:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 627b8a75-695c-3f85-a950-9a1f67207ddf | -3.4262 | -41.6662 | 2025-12-09 01:10:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 132.4 |
| e15fe7fa-5394-3380-a22b-237f42752677 | -2.3278 | -45.5698 | 2025-12-09 01:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 1ee1a3ec-5e10-3960-b51c-7823891d7e9c | -3.4449 | -41.6653 | 2025-12-09 01:10:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 148.4 |
| aac9a4dc-8129-38d4-a12d-0f6610f0d36d | -3.4264 | -41.6423 | 2025-12-09 01:10:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 115.8 |
| 95f554af-58b8-307c-b344-3249302f117b | -4.3144 | -45.9375 | 2025-12-09 01:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 64.0 |
| a8ae2e07-3270-3e73-9134-85bddf55608e | -4.2959 | -45.9161 | 2025-12-09 01:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 4f163590-df31-3b55-a7bf-832e9314d1f9 | -4.2958 | -45.9385 | 2025-12-09 01:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 90ab084f-d884-306b-91d3-6c5f322b7b69 | -2.3277 | -45.5922 | 2025-12-09 01:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 31693aa3-886a-373e-b00c-bf6c62b736f2 | -3.4264 | -41.6423 | 2025-12-09 01:20:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 91.8 |
| 588d126f-01b3-3c81-a25f-b93146c7bd1b | -3.4262 | -41.6662 | 2025-12-09 01:20:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 102.6 |
| cadabf52-d0f8-301a-bc51-32f33adadb34 | -3.4451 | -41.6413 | 2025-12-09 01:20:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 127.8 |
| c09a97d6-3a96-338e-8210-bead9ab125b2 | -4.2958 | -45.9385 | 2025-12-09 01:20:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 86.7 |
| f3a05b76-c885-3c28-8ecf-13ffe5880fbe | -3.8389 | -47.8305 | 2025-12-09 01:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 109ffa21-52de-3573-b464-f27b723971f5 | -2.3278 | -45.5698 | 2025-12-09 01:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 118.3 |
| fe3408b5-7fc5-3ed0-974f-b4aace766af9 | -3.4449 | -41.6653 | 2025-12-09 01:20:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 140.9 |
| 4ac74bbb-f84f-34bf-841f-fd02c3973950 | -2.3278 | -45.5698 | 2025-12-09 01:30:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 36297cb1-c038-3120-ba8c-5dcd0ca6f090 | -2.0651 | -46.5108 | 2025-12-09 01:30:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 9b756ed6-ba1a-3604-afab-b65e3da6bcc5 | -4.2959 | -45.9161 | 2025-12-09 01:30:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 9307e0e3-f951-357e-b10c-8ae5cf5e13e3 | -4.2958 | -45.9385 | 2025-12-09 01:30:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 85.1 |
| f79cf7a7-e5eb-32a0-9c37-cc8bd0bbc867 | -3.4262 | -41.6662 | 2025-12-09 01:30:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| d632e65c-47d3-3735-8834-ea9ea2fcd3be | -3.4449 | -41.6653 | 2025-12-09 01:30:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 99.3 |
| b4f3594d-9c78-3ea3-a086-027329e2380a | -3.4264 | -41.6423 | 2025-12-09 01:30:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 83.0 |
| 2d6cf851-a302-35d4-bdc4-4ad0275dc599 | -3.4451 | -41.6413 | 2025-12-09 01:30:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 96.3 |
| 93cf9ea4-8e42-388b-a374-5feca3a50b8a | -2.3277 | -45.5922 | 2025-12-09 01:30:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 8a8e1b0e-a3e2-3488-80b9-60ff0391954b | -4.2959 | -45.9161 | 2025-12-09 01:40:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 015702b3-3487-3b1d-b26e-f354470d2abe | -3.4262 | -41.6662 | 2025-12-09 01:40:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 84.8 |
| aacd2cb6-4ac6-3623-8ec0-3cdef52e569e | -10.7983 | -37.2517 | 2025-12-09 01:40:00 | GOES-19 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 88.1 |
| aa2421a4-20b9-3ae2-a99d-97652c05e4d6 | -4.2958 | -45.9385 | 2025-12-09 01:40:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 7836e141-5120-311b-ae70-8cc748cdb799 | -3.4451 | -41.6413 | 2025-12-09 01:40:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 104.4 |
| 0de25570-b615-3d4f-84ec-6dd043572747 | -2.3278 | -45.5698 | 2025-12-09 01:40:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 96125686-bf8c-3948-baf3-33a88f841db9 | -3.4449 | -41.6653 | 2025-12-09 01:40:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 116.6 |
| a501b440-c7ec-3870-a82a-03e82e26c74f | -3.4264 | -41.6423 | 2025-12-09 01:40:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 75.0 |
| 75c5602b-6b76-3c76-89b1-12b9ff8f7b13 | -2.0651 | -46.5108 | 2025-12-09 01:40:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 0303e4d5-ea2e-3607-b04f-a7d8506ca4c9 | -3.4264 | -41.6423 | 2025-12-09 01:50:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 51.1 |
| 2e9eb2f1-2a9b-3493-b756-a2ae224dc4c6 | -2.3278 | -45.5698 | 2025-12-09 01:50:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 60.6 |
| c6911deb-29b1-328d-b578-9326be477cd2 | -2.0651 | -46.5108 | 2025-12-09 01:50:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 9c0d0b24-aa60-3c8c-985a-30c3851d57a7 | -3.4449 | -41.6653 | 2025-12-09 01:50:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 78.2 |
| 150a815e-72f2-32b7-9f16-fe5fdd856063 | -4.2958 | -45.9385 | 2025-12-09 01:50:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 92.6 |
| e9f0fbdc-616b-32f2-88a8-fa06ce83ac5c | -3.4451 | -41.6413 | 2025-12-09 01:50:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 61.7 |
| bfdd573d-5969-327d-85f7-b51941112415 | -3.4262 | -41.6662 | 2025-12-09 01:50:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 66.8 |
| 49b69ed9-c510-38cc-ab2f-fb29e93d92ad | -3.4262 | -41.6662 | 2025-12-09 02:00:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 61.9 |
| a2d2fce5-2494-352f-874c-a750b42d3290 | -3.4449 | -41.6653 | 2025-12-09 02:00:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 67.9 |
| 50023706-9eaf-36c5-8bc8-9115a77dffab | -3.4264 | -41.6423 | 2025-12-09 02:00:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 47.2 |
| 819ef4a5-8ddc-3708-bb9f-538853883301 | -4.2958 | -45.9385 | 2025-12-09 02:00:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 2057a49e-15bf-3b3c-9161-41ddd6c79ed9 | -3.4451 | -41.6413 | 2025-12-09 02:00:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 54.8 |
| 80c2d385-170e-348e-8f9d-117e227f491d | -3.4262 | -41.6662 | 2025-12-09 02:10:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 58.2 |
| 5c44fa18-a42b-3833-a40a-1776f2160cd1 | -3.4264 | -41.6423 | 2025-12-09 02:10:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 50.3 |
| 773e67c5-7cac-331c-84ad-d7fb63c3a123 | -4.2958 | -45.9385 | 2025-12-09 02:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 142.6 |
| 3ca66970-819a-3fb5-8ec6-29dab0c3d87b | -3.4449 | -41.6653 | 2025-12-09 02:10:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 40.7 |
| d9e7409b-a928-3bd5-8c22-79501164b37b | -4.2959 | -45.9161 | 2025-12-09 02:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 869a7405-d861-3341-932b-74bb937f332b | -4.3144 | -45.9375 | 2025-12-09 02:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 724b3255-faf7-3a9d-b446-458213ff3bbd | -3.4451 | -41.6413 | 2025-12-09 02:20:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 40.9 |
| d68c1d14-bf2b-308f-bbe3-b90f6d3e7ec8 | -3.4264 | -41.6423 | 2025-12-09 02:20:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 51.6 |
| 3e16387a-8359-354a-8144-8e8820cea45f | -4.3144 | -45.9375 | 2025-12-09 02:20:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 382f3809-4bfd-3836-87e5-6e3ab713b1c1 | -3.4262 | -41.6662 | 2025-12-09 02:20:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 53.1 |
| ecf0d671-15cc-3d6a-9671-fab7ca214115 | -4.2959 | -45.9161 | 2025-12-09 02:20:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 619eab7a-769a-30c2-ae75-244289811890 | -4.2958 | -45.9385 | 2025-12-09 02:20:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 151.9 |
| 3be0154c-9f76-3baa-9c5e-90ac25e99675 | -3.4264 | -41.6423 | 2025-12-09 02:30:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 47.7 |
| 4416f0ea-27bf-3c53-85de-9eb85c494ab8 | -3.4262 | -41.6662 | 2025-12-09 02:30:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 57.4 |
| 78e8b6ab-49d3-3f76-accd-acfe38408b1b | -7.81541 | -35.24445 | 2025-12-09 02:47:00 | NOAA-21 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 9deb5bc4-8a0b-35c5-ab3a-d8cc3367612d | -7.82258 | -35.24548 | 2025-12-09 02:47:00 | NOAA-21 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| f2737c57-fc0d-369d-a27c-f1bb4d3f0b9e | -4.2958 | -45.9385 | 2025-12-09 03:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 79.1 |
| e22f327a-baef-38eb-9710-14a3efe59cd4 | -5.67703 | -39.59994 | 2025-12-09 03:14:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| eec98ba7-5a48-3d87-b192-34414b93af1e | -5.67193 | -39.60442 | 2025-12-09 03:14:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ea64d4e1-346f-3b6c-86d2-f8e4d17443c8 | -5.67292 | -39.59885 | 2025-12-09 03:14:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 947f242c-e287-3bc5-b0b5-3f4a55a30de7 | -5.08305 | -37.54803 | 2025-12-09 03:14:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0e32ce16-3af6-30d9-84e0-fca416328b33 | -5.22147 | -39.25387 | 2025-12-09 03:14:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ee6d9b6f-224f-3e26-92e2-0b094507457c | -5.08792 | -37.54776 | 2025-12-09 03:14:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 5f22219e-93e9-3d6c-ac07-8940590b2a06 | -7.82045 | -35.24744 | 2025-12-09 03:17:00 | NPP-375D | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9d18bb09-c3f7-387e-948b-674e38461793 | -6.60144 | -39.54171 | 2025-12-09 03:17:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1cb88392-19b8-37db-988f-2b92a9d90e5c | -7.86411 | -38.73088 | 2025-12-09 03:17:00 | NPP-375D | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |


[Clique aqui para ver as próximas entradas](README4.md)
