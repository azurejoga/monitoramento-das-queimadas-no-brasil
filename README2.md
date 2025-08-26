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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 413f79b2-e1d5-3948-908a-93261e206609 | -13.1837 | -45.2865 | 2025-08-26 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 45.3 |
| c626aad5-8391-3f01-9138-380fc03f59e1 | -4.9605 | -55.8226 | 2025-08-26 00:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 140.3 |
| 2481dfd3-8d54-3ef6-8ddc-8edd3c745405 | -10.76 | -47.0424 | 2025-08-26 00:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 220.8 |
| 7127e565-6f7b-3a79-a99e-3c23e27621bc | -6.9127 | -59.3771 | 2025-08-26 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 636825e4-1db1-347e-8144-93f153d1f0b9 | -6.8043 | -58.9761 | 2025-08-26 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.9 |
| f82ff873-a0bd-3e78-8672-49d3a9c26b73 | -7.4737 | -61.3466 | 2025-08-26 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 603bce83-163d-3ab2-8ce0-1ff840d49a81 | -6.8412 | -58.9746 | 2025-08-26 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| fe1061da-59b9-3e48-aba0-ce179c8bd1f4 | -6.246 | -59.9982 | 2025-08-26 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 2d6aed65-e036-3196-8ae4-3c7dddb98aad | -8.9874 | -65.4192 | 2025-08-26 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| fb9cc421-a73f-35da-b798-b42f1eec19ee | -11.559 | -52.117 | 2025-08-26 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 172.0 |
| 7ef3368c-e442-3ae6-aae2-298ea70928dc | -6.2275 | -60.018 | 2025-08-26 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 123.7 |
| 74e3a06e-bdd0-3750-925c-e0ae46f82247 | -10.4241 | -64.3903 | 2025-08-26 00:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 47.1 |
| cc8b6d78-5081-3a74-a9b9-75d32a1338f9 | -6.8228 | -58.9753 | 2025-08-26 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 194.1 |
| ad491797-69ab-3acf-b0f9-592a32273cf5 | -6.766 | -62.8659 | 2025-08-26 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| a2c46093-f627-33b1-8d9e-e990f245b865 | -7.3669 | -64.3667 | 2025-08-26 00:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| cd0a4c54-8ab6-3495-b3d7-a1addf499c98 | -13.1648 | -45.2665 | 2025-08-26 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| a591d9da-7e34-3a43-93f0-3a1bf4a6a493 | -8.3394 | -50.5863 | 2025-08-26 00:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 3de6dd6f-ffa1-3726-bd29-4df5da433143 | -4.9606 | -55.8028 | 2025-08-26 00:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 25c193fd-d87d-3b56-bf7b-f15daa590255 | -11.54 | -52.119 | 2025-08-26 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 257.2 |
| af91cc68-dc52-349b-a81a-1f1424f7c559 | -6.2459 | -60.0174 | 2025-08-26 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 161.7 |
| 6c91924b-ba85-30ba-b09b-c9b0992fe39d | -6.7144 | -58.5732 | 2025-08-26 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 78.9 |
| f81e49fe-6707-3348-82d4-0424864b2ea7 | -9.191 | -59.4425 | 2025-08-26 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 66001b52-3a87-355e-9b04-3374818042ab | -7.4736 | -61.3656 | 2025-08-26 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| c01a6092-904d-39f7-89a1-94c82075e404 | -6.8413 | -58.9552 | 2025-08-26 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 9d11f1d4-2590-3602-9560-5cc364975ed5 | -7.3854 | -64.3662 | 2025-08-26 00:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 159.1 |
| 105180ce-8a84-38d2-b508-2f2fb49f5cc7 | -6.7635 | -59.6718 | 2025-08-26 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 76af4439-66e9-3ae6-8219-d09413900ab7 | -9.0231 | -65.7169 | 2025-08-26 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 7b95cd34-340b-33c7-bceb-df888ff5a1bd | -10.7593 | -47.0871 | 2025-08-26 00:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 364796c4-f206-3b81-943e-dba3f457a8e0 | -9.191 | -59.4425 | 2025-08-26 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 27b63586-3897-379b-bec2-745045fc7f99 | -8.3394 | -50.5863 | 2025-08-26 00:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 398d9672-8e81-3f99-bf95-f833517c1ec7 | -9.2677 | -56.91 | 2025-08-26 00:20:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| f45cc83f-7611-3184-80a6-7d2b81356086 | -7.3669 | -64.3667 | 2025-08-26 00:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 02fd825d-f0c3-39a9-b361-6e46f0d6043f | -6.8044 | -58.9568 | 2025-08-26 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 113.4 |
| c8b72550-8b5e-3f08-80e6-9dfab7d29504 | -9.236 | -60.9256 | 2025-08-26 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 46a160b0-3b57-37e3-872c-a99d8e109953 | -10.4241 | -64.3903 | 2025-08-26 00:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 124974d1-c191-3732-ae0b-abb74e660cd4 | -11.54 | -52.119 | 2025-08-26 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 204.5 |
| 85b7a3a5-a805-346b-8312-71e7e06de66c | -6.766 | -62.8659 | 2025-08-26 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 07f391d2-033d-3af1-b8cd-3221ed71f9f9 | -4.9606 | -55.8028 | 2025-08-26 00:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| cedb03a8-6f85-30ea-b9b0-08cf45502853 | -7.4737 | -61.3466 | 2025-08-26 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| c1b3e586-852a-30bd-841f-1ed4c07c81e7 | -6.9127 | -59.3771 | 2025-08-26 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 17316904-b29e-3c13-8462-6366e77572f7 | -6.7476 | -62.8664 | 2025-08-26 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| cc8e870f-4071-35d9-8b8f-0dbfb9d83344 | -6.7145 | -58.5539 | 2025-08-26 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| ce90697f-3dd6-35fa-8e41-3fcf2d0fcb6b | -6.2275 | -60.018 | 2025-08-26 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 3b30dd02-1f77-3549-a774-a3715e42803a | -6.7144 | -58.5732 | 2025-08-26 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 358b54e0-eda4-33a0-a958-695cca62e206 | -6.6961 | -58.5546 | 2025-08-26 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 92.1 |
| aa9a6e2e-c9ff-38ac-bb54-d44ee46edb22 | -8.9873 | -65.4379 | 2025-08-26 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 4ca89a0d-e0b6-31ab-b88c-71fd148fa38d | -10.76 | -47.0424 | 2025-08-26 00:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 264.5 |
| 1962c57a-01d1-3fc2-803b-971f22f46549 | -10.741 | -47.0448 | 2025-08-26 00:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 213.9 |
| b19fac9b-61ef-308c-ab3d-29717dc4a624 | -6.8229 | -58.956 | 2025-08-26 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 342.9 |
| 2e29aad1-ebab-339b-9d23-2f4b58671c3a | -8.9689 | -65.4198 | 2025-08-26 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 2830c300-b198-37f1-9adc-9cec91b7a862 | -4.9605 | -55.8226 | 2025-08-26 00:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 140.1 |
| 69cbbb70-f59e-375f-924d-7bbcb81dbbaf | -8.3209 | -50.5667 | 2025-08-26 00:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 897e55b6-f894-3651-9ae6-beb8770288b4 | -6.8043 | -58.9761 | 2025-08-26 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 126.4 |
| 52fe83ce-1ae7-3f76-a57d-c6af5af0ccb0 | -11.5587 | -52.138 | 2025-08-26 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 175.2 |
| a2515348-8ab1-30ae-acc3-5fc5e3d234f8 | -6.8412 | -58.9746 | 2025-08-26 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| bf1a4e4e-2463-3358-bfa3-639c281da4bd | -11.5397 | -52.14 | 2025-08-26 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 203.6 |
| ef15fff4-5116-379b-b4ec-6cf8c4a3bdef | -7.8896 | -62.9982 | 2025-08-26 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| e081aabf-7727-3b45-81d2-da3b6509cafc | -11.5592 | -52.096 | 2025-08-26 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 3e39dbc0-3e9d-3bc8-b150-350e51b7d47d | -9.0416 | -65.7163 | 2025-08-26 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 287f9c71-ee89-384a-a847-fbbbcd693c9f | -7.3855 | -64.3288 | 2025-08-26 00:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 3fd1c932-6b8a-3b2a-ac32-8969e361262d | -6.9128 | -59.3578 | 2025-08-26 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.2 |
| df430f17-6919-3699-9376-1520a113787d | -6.246 | -59.9982 | 2025-08-26 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 9326d7f0-f291-3840-8377-7c3c99e612c8 | -11.559 | -52.117 | 2025-08-26 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 185.8 |
| 1b8b01f6-67ef-3976-b00a-cd365332770c | -7.8711 | -63.0177 | 2025-08-26 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 116.3 |
| d7a7026e-2895-32ea-8993-5109b347057a | -6.782 | -59.6519 | 2025-08-26 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.1 |
| da8e5e2b-dd2a-36e1-9ab5-07af4ec8e836 | -7.3854 | -64.3475 | 2025-08-26 00:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 252.9 |
| 8d486590-5899-3c5f-a24a-bcc8ab1a06f1 | -11.6351 | -44.8561 | 2025-08-26 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.0 |
| b9774991-a2f3-36bf-bf74-17a6a553700a | -10.7787 | -47.0624 | 2025-08-26 00:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| aa533188-a560-33f0-935e-6092ad24eb39 | -9.1722 | -59.4629 | 2025-08-26 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 0190017a-8d8b-30dc-a5b8-2eb50f9d6a42 | -13.1644 | -45.2897 | 2025-08-26 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 214.7 |
| caef3f73-1845-3500-82d7-df306d594a75 | -9.1724 | -59.4436 | 2025-08-26 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 8b956040-43fc-3ff1-af9d-3934a8566412 | -7.3541 | -59.6669 | 2025-08-26 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 4fc3047f-36f2-3f21-bdb3-24c19b4f7992 | -11.6277 | -46.3899 | 2025-08-26 00:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| b85d2b82-8482-3ccc-9b59-eecf19c473b4 | -6.2459 | -60.0174 | 2025-08-26 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 9524349c-8ae9-3bb7-a3a9-59077b444b6e | -8.9874 | -65.4192 | 2025-08-26 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 7d3ec910-ac93-389a-88a5-7a75fe0abcf4 | -6.8228 | -58.9753 | 2025-08-26 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 391.3 |
| 84a8ec2e-5ca0-3179-9c85-458cc16254fe | -10.7597 | -47.0648 | 2025-08-26 00:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 419.6 |
| ba373d65-9feb-3c07-873e-1388993f59a8 | -9.1909 | -59.4619 | 2025-08-26 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 3f4fdc6a-f57e-3d16-8531-0b6b80b62072 | -9.1812 | -60.7939 | 2025-08-26 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 044f29ef-2398-33f5-9fed-3b7875b08b13 | -7.4736 | -61.3656 | 2025-08-26 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 4c722c54-e225-387f-974f-c91037bae0cf | -9.023 | -65.7355 | 2025-08-26 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 29aa39f6-ded6-351d-b953-c5f79d98e833 | -13.1648 | -45.2665 | 2025-08-26 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| c45ffc15-ca4f-367c-a4f8-b10e2fabc796 | -17.6748 | -40.2025 | 2025-08-26 00:20:00 | GOES-19 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 108.2 |
| 2f10873c-cfe3-3ae3-8393-509e8b011a72 | -7.8895 | -63.0171 | 2025-08-26 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 102.1 |
| d33361ca-90fe-3864-9048-fbdff189ec7f | -8.2193 | -49.5544 | 2025-08-26 00:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 9219f2f6-ed26-3189-808e-46055bb25ba6 | -7.8712 | -62.9989 | 2025-08-26 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 7c52734c-1181-3aba-bb71-635ae62011f5 | -13.1639 | -45.3129 | 2025-08-26 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 8f1224ee-e15b-3474-a76b-d5ae0e6a087c | -13.1837 | -45.2865 | 2025-08-26 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 4b541d6f-0342-3a99-8e85-9366555aeb88 | -8.3396 | -50.5652 | 2025-08-26 00:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 151.7 |
| be543353-ed2d-3aeb-a9f0-cadd81eee72a | -10.7406 | -47.0671 | 2025-08-26 00:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 316.5 |
| ff3c724a-9427-360f-906f-5060781ef6f3 | -6.7819 | -59.6711 | 2025-08-26 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 23b7c10a-c805-37d9-b8d0-121faae383b2 | -7.367 | -64.348 | 2025-08-26 00:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 95.8 |
| d0993e82-30ee-3fc5-8924-564251562fef | -9.181 | -60.8131 | 2025-08-26 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 6e68b14b-1e28-395f-8581-d1e71b60eb11 | -7.4224 | -60.6236 | 2025-08-26 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 7192b6c9-b0a0-3247-9be8-73918f1b82e2 | -9.0415 | -65.7349 | 2025-08-26 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 596e36c9-1cfc-32ff-8dc3-b06d10b9679f | -6.7636 | -59.6526 | 2025-08-26 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| c617c18b-9d3f-349f-9a74-3d3fb8bbe8ab | -9.81 | -64.2831 | 2025-08-26 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 38.3 |
| e27595ca-7d6c-39bb-90ff-aa9a2cd1b985 | -21.72318 | -46.8173 | 2025-08-26 00:26:00 | TERRA_M-M | SÃO SEBASTIÃO DA GRAMA | SÃO PAULO | Brasil | 3550803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| d7caa6af-815a-3685-ade1-ac6b97167443 | -21.72174 | -46.80611 | 2025-08-26 00:26:00 | TERRA_M-M | SÃO SEBASTIÃO DA GRAMA | SÃO PAULO | Brasil | 3550803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 96b576eb-68e6-3df4-80f5-8849f7f8162c | -17.19866 | -44.31803 | 2025-08-26 00:26:00 | TERRA_M-M | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |


[Clique aqui para ver as próximas entradas](README3.md)
