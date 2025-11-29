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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81a35a83-010a-3c31-85a8-57fd156e3782 | -3.97515 | -45.81133 | 2025-11-29 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ef6d815-3920-34bc-abcb-b965a209bebf | -5.40954 | -44.81639 | 2025-11-29 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf544fd0-c118-31a4-be3d-8eb6cdd8f4d2 | -6.71861 | -40.81163 | 2025-11-29 04:14:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0015d586-ba6e-3d9c-b7f3-b92a681ab27a | -3.03749 | -50.9796 | 2025-11-29 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 412dc183-e875-3d11-b1f0-8f83b5f2a0f9 | -4.52816 | -44.72849 | 2025-11-29 04:14:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86925d76-8eda-37e7-91e0-7e6dc76a3f82 | -4.93243 | -43.46806 | 2025-11-29 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b69222d7-c09c-3005-b8c3-023f823dd590 | -9.89982 | -36.14208 | 2025-11-29 04:14:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| b4233595-fff3-348e-88c3-ab969a362bd3 | -8.04701 | -43.12905 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 67c71b6b-38c0-3a10-a9ac-7b8ecf7e7b4a | -5.49588 | -39.16756 | 2025-11-29 04:14:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d4210b61-7927-3ad8-aabf-57c45754cb35 | -8.18211 | -43.19991 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2287a538-5b92-3ec5-a32d-b00d7678da61 | -8.04039 | -43.12801 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 73a93d9d-f87d-3258-9b04-b79e72942f19 | -3.97101 | -48.99707 | 2025-11-29 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d21ab4c1-1447-3598-ab69-ad9fa3390341 | -8.17165 | -43.20182 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 292f8eb8-c0e0-3a7b-95d2-b454f11f066e | -3.94955 | -44.76628 | 2025-11-29 04:14:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e047398e-8c45-374a-aad5-eb5beeb2bee5 | -3.84105 | -44.12724 | 2025-11-29 04:14:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6298b001-02ff-34f1-9813-7a9075388b6c | -4.6286 | -43.9893 | 2025-11-29 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ebbbc12f-74ec-3c9a-b79e-ab1c8eb7dc17 | -8.22288 | -41.20312 | 2025-11-29 04:14:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 88a6a035-5e3b-3990-b777-2ae1a3965475 | -2.83999 | -51.81038 | 2025-11-29 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e806df08-4f83-3af1-92e9-572a0ff50640 | -4.81434 | -43.09402 | 2025-11-29 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28845896-11a9-3ec4-8125-4f8e972288d8 | -8.17603 | -43.1954 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 096fb07b-5f0f-3d4f-a686-7b22bc86b44f | -4.90559 | -42.68481 | 2025-11-29 04:14:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f5f168a-aeae-3f68-9db5-e7c65b8d09ee | -8.16335 | -43.18985 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7e76d568-6c72-3e40-8481-450091020c56 | -7.76404 | -37.62952 | 2025-11-29 04:14:00 | NOAA-21 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3fbc7bb4-8164-3152-9cbf-98825983821c | -6.30767 | -43.78618 | 2025-11-29 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70713edd-7be1-3128-acf6-2e72673736ff | -5.94141 | -45.3962 | 2025-11-29 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e1c349b7-6084-3dd4-a18d-6e5f447add00 | -6.72946 | -39.30468 | 2025-11-29 04:14:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| becf23d8-1845-3105-afc1-32dc35bb677f | -8.17441 | -43.20581 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9f1cd56e-6e9f-3b82-8ff9-5d125af847b7 | -5.30829 | -40.89265 | 2025-11-29 04:14:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a49c0304-005e-304c-ad26-76023ddd5c08 | -6.24471 | -40.29945 | 2025-11-29 04:14:00 | NOAA-21 | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 64599b63-58cc-37cc-a34b-0fe0e2fe00c7 | -4.72288 | -46.43677 | 2025-11-29 04:14:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08cd1cec-24b9-3e90-8bd8-6c2bd16dd59b | -11.17366 | -43.57486 | 2025-11-29 04:14:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab3b8f5b-3f66-3d58-bb08-858d6317584d | -8.17826 | -43.20285 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9872cacc-551f-3c27-bf77-9141a81c4e74 | -2.8394 | -51.81395 | 2025-11-29 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8bcef32e-e458-384f-b278-e0360e840ff3 | -8.5902 | -39.44611 | 2025-11-29 04:14:00 | NOAA-21 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c95b567e-cbd5-3bcd-8c54-b1babd274822 | -5.00551 | -38.54081 | 2025-11-29 04:14:00 | NOAA-21 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 2e75bed7-98a9-3546-91db-787818b9211c | -3.84047 | -44.13087 | 2025-11-29 04:14:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34f7a3ba-cbb3-38a5-8cea-c2335de7345b | -4.2235 | -46.50299 | 2025-11-29 04:14:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 156d400f-73a5-3f6a-87c8-4739d8fb5cd4 | -5.01238 | -43.11149 | 2025-11-29 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e033d5ac-6b62-37ce-a47c-5d0328131ace | -2.91042 | -53.06623 | 2025-11-29 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c17089e4-5ce6-3a32-b64a-2e31d1a31fe0 | -4.52264 | -46.47294 | 2025-11-29 04:14:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55cb2e59-aea4-33eb-a209-e905eaec75d2 | -6.73329 | -41.22675 | 2025-11-29 04:14:00 | NOAA-21 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bec2ca6e-cfd2-3136-8927-592b6cfe08b4 | -5.67199 | -38.97173 | 2025-11-29 04:14:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 060eab6c-4723-3efc-8688-402cfaf053bd | -6.69933 | -41.47045 | 2025-11-29 04:14:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7bf15d0e-4916-3dc9-b3f0-f86e763045d5 | -4.72217 | -46.44123 | 2025-11-29 04:14:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9fe3033f-2f39-3534-9e29-af9c8cc3d102 | -4.72588 | -46.44185 | 2025-11-29 04:14:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d4e1c8b7-2408-3806-a56d-ca5cc98448c0 | -11.16371 | -43.57328 | 2025-11-29 04:14:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 154a78b3-60b5-35f0-bd0a-e97571307dbf | -5.25387 | -46.18952 | 2025-11-29 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9d8be130-56c7-3da4-9075-e584fccef241 | -8.03324 | -43.13044 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 279eb4b1-ee5d-371f-a7a6-a5e7b945e1fe | -7.229 | -40.279 | 2025-11-29 04:14:00 | NOAA-21 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 66176d8f-b391-3a30-856f-d00c569961ff | -4.81488 | -43.09057 | 2025-11-29 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6102a71b-d337-3295-9959-e53e69017135 | -3.95016 | -44.7625 | 2025-11-29 04:14:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e7116bd-6de1-30db-8a66-8da2e7261ed5 | -8.16557 | -43.19731 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 365e672c-1e69-3851-9636-fc0f720ba5ed | -8.17387 | -43.20928 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c6b788c7-9007-3f2c-953a-c830c8a80001 | -8.18156 | -43.20337 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5620fc2b-08bb-310f-bbff-dfce20a0cbad | -5.57365 | -44.97561 | 2025-11-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 944e0988-9eb0-3321-ab6c-1382c1be5de5 | -8.16666 | -43.19037 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| eb65d9a4-6a59-3b26-b753-8e9e60f91bc0 | -8.03215 | -43.13739 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 115c4da5-9f9a-3ec4-9555-31ab4ab842c8 | -6.78103 | -41.71275 | 2025-11-29 04:14:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8dcc0647-dce3-3a33-ac0a-ba22a53acf53 | -3.61817 | -50.36884 | 2025-11-29 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49eb1518-c943-3a11-af3a-50844c63f40e | -8.17333 | -43.21275 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4b76c8c8-5887-397e-b32b-679f214b857d | -8.16118 | -43.20373 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 7f17f7a0-3fe2-3710-9b8b-8580a31f9896 | -4.9363 | -43.46511 | 2025-11-29 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c25eb1d-d606-3d68-a469-cc826a8011db | -9.32161 | -43.08762 | 2025-11-29 04:14:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9f72bdbe-f1fb-3d03-8f32-74a7e3c72428 | -5.36651 | -43.0227 | 2025-11-29 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2a6fc0e2-206a-306f-aa98-d68be473a815 | -4.93852 | -43.47259 | 2025-11-29 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7c1d332-3755-3296-b40f-1e934dacdb3d | -8.18265 | -43.19643 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4d407c4a-56f1-3565-a737-1939ccf33968 | -3.87726 | -54.20171 | 2025-11-29 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b35da7b0-96a4-3cfb-b323-268cfab53546 | -4.92967 | -45.98685 | 2025-11-29 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 754bae08-ccd3-3e0c-952a-2ad57e77c069 | -5.2407 | -41.24544 | 2025-11-29 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7e8f60fd-6433-3932-ac71-690f40e3bc26 | -4.88869 | -41.02107 | 2025-11-29 04:14:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f876d7ad-65e8-3e7d-98fe-4d2454e50833 | -8.62828 | -37.00875 | 2025-11-29 04:14:00 | NOAA-21 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 330a367a-4cfc-3de6-af62-faaf4634fa87 | -4.16982 | -43.75292 | 2025-11-29 04:14:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6a8bc7b3-b3f4-3bba-9991-3241a3e87854 | -8.17934 | -43.19592 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 048f13c7-2a33-3c23-a8a4-91263cde3734 | -8.17219 | -43.19835 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7a2928ef-5711-3824-9a18-4ffd3aee1b69 | -10.14417 | -36.32483 | 2025-11-29 04:14:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 487f27dd-1a2f-3d92-8c3f-4bd1c6c0c3f9 | -2.93086 | -53.2722 | 2025-11-29 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b239013f-aba3-3282-8668-4b45b904cf82 | -3.32712 | -53.32063 | 2025-11-29 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7af33ce3-ff65-3351-bbd6-c4acf295a39d | -4.86404 | -50.82669 | 2025-11-29 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b099827-bacf-34b1-98c8-9395739ebe11 | -9.28763 | -43.15353 | 2025-11-29 04:14:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 15afeb40-5f7c-3622-93c4-70f84af9e28b | -8.17717 | -43.2098 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3167ceab-41cc-3034-83a6-97e22eedcc49 | -6.2441 | -40.30342 | 2025-11-29 04:14:00 | NOAA-21 | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 60c75de8-18e3-36a5-8902-aa80e5bf99e7 | -6.4875 | -41.96033 | 2025-11-29 04:14:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 413619fa-3d52-343f-90e8-1da2bba43b32 | -4.0536 | -49.50029 | 2025-11-29 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad465aac-06ec-3fbc-b896-0d00fd06aab4 | -4.35832 | -43.16017 | 2025-11-29 04:14:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7e1c9616-fa3e-3c4a-8b6a-8b68766a797f | -4.00883 | -46.50904 | 2025-11-29 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f50dcc9-dea1-3555-b8aa-f1003947e89c | -5.23429 | -41.25525 | 2025-11-29 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 445f0b39-936b-3794-b1c4-c132f80e2735 | -5.3775 | -43.01735 | 2025-11-29 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.5 |
| eabb4cd2-78b5-3188-bb48-66a1a22f2f81 | -11.55824 | -42.18286 | 2025-11-29 04:14:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e459732f-0d5c-348d-9769-cb389074ce5c | -4.40054 | -41.45381 | 2025-11-29 04:14:00 | NOAA-21 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 59802f0a-9eb9-33a1-ad19-366053ec85ee | -5.23597 | -41.24445 | 2025-11-29 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 00d94c7f-e163-307d-b6c2-1b05e391436f | -3.88068 | -54.20436 | 2025-11-29 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f952aec1-8bd1-3184-a909-4ba0635555b5 | -3.88354 | -54.20273 | 2025-11-29 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ef750c1-4f2e-31b1-a523-6e7a57c2bf26 | -4.95977 | -41.19871 | 2025-11-29 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3d07af84-8b05-33ae-8425-defd89c1d394 | -5.11226 | -40.72878 | 2025-11-29 04:14:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 43ee53f6-9cfb-36c3-b0d2-83e3d3d85077 | -4.34107 | -43.57108 | 2025-11-29 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bb07a272-dd76-326c-b32f-22fcfba6e664 | -4.74016 | -44.43153 | 2025-11-29 04:14:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6c578550-1e3d-3766-b1d1-5ec93ad2109f | -6.46637 | -41.72696 | 2025-11-29 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 213c47d1-fa14-3020-9c00-c3713e667a93 | -4.85013 | -38.74459 | 2025-11-29 04:14:00 | NOAA-21 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4e9038fd-1b42-36ab-b116-bf4577cd7461 | -6.717 | -42.52047 | 2025-11-29 04:14:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c56524e2-c9ab-3db8-82da-6789d3f9c065 | -4.7266 | -46.43737 | 2025-11-29 04:14:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README16.md)
