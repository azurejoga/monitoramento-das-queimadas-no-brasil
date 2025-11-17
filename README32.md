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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e2c1d5b-61b0-343f-b2b3-fdf38933256b | -7.12759 | -41.65996 | 2025-11-17 04:38:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 98724807-fc07-350c-a16f-62bda11d51cd | -8.11653 | -43.53138 | 2025-11-17 04:38:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b4f8db5-3d9f-3d08-bde9-32203645b1c9 | -3.78931 | -46.08803 | 2025-11-17 04:38:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ff2a7a7-ebd2-3521-967c-2e6395b642af | -3.89011 | -46.46423 | 2025-11-17 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6b9ecd7-116f-361e-a443-ae457817fb39 | -4.12731 | -47.29392 | 2025-11-17 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2443de50-9242-3cf6-b587-24da20103334 | -3.53667 | -49.83466 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de2b3fdd-108c-3fe5-8268-8fcd3a18195b | -3.14753 | -51.32389 | 2025-11-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58d01f03-42af-3102-8795-d5252eb04ace | -3.11533 | -51.98201 | 2025-11-17 04:38:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0c2bce30-fb08-3faa-bfd2-ad59b88b6b67 | -3.40331 | -50.18591 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| baacf9e4-b957-3735-b5fd-a09f28aab01c | -4.72277 | -46.3798 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6368ca92-5eec-3027-be88-1a0bea30e2cf | -2.86999 | -51.47118 | 2025-11-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63dea2ac-9600-36c3-b595-06b647331ac4 | -4.83801 | -47.55692 | 2025-11-17 04:38:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 39c1eeda-6778-3e4a-ac31-137d27b1dfd8 | -4.21262 | -49.12969 | 2025-11-17 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6b2155a-962b-3d2d-922f-1ebea8707e07 | -5.46711 | -40.97433 | 2025-11-17 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 350049d7-5666-3298-8db4-d298c939402a | -6.36069 | -46.14895 | 2025-11-17 04:38:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f2f0618d-6946-376b-a5d5-995fc7e71ee1 | -4.13938 | -38.34721 | 2025-11-17 04:38:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ad42fc94-771d-305e-bb6e-8ad356a158f7 | -7.18566 | -44.64452 | 2025-11-17 04:38:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ebf47be7-c54c-3a31-b41d-aef4dafa1ab7 | -3.30496 | -53.85445 | 2025-11-17 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8d32d03-76e3-3cd9-8625-76dfe6c735f8 | -4.01523 | -48.80606 | 2025-11-17 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9c8c21d1-c2d5-3333-a79c-fdb5e17eb729 | -1.69561 | -53.68288 | 2025-11-17 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 99db9f93-3b84-3996-ab1c-86811046eb3a | -5.72303 | -42.9084 | 2025-11-17 04:38:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| fcb8991f-4876-375f-b1d8-de827a6f7821 | -3.78381 | -49.25976 | 2025-11-17 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62c527bd-d6fc-300a-878e-374b48ba3ee5 | -4.1846 | -50.23834 | 2025-11-17 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 705ddada-cc6c-3760-9903-a8f31f584c7b | -3.8588 | -40.7605 | 2025-11-17 04:38:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 688945d2-0acf-3eec-bcf7-dc7e85d7769d | -3.46476 | -50.1145 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a518ef19-7ebc-37f1-b975-e661db0036b3 | -4.87748 | -46.69844 | 2025-11-17 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dbe94c59-2e1f-36f2-987e-655f3e1b5d50 | -2.45471 | -50.28068 | 2025-11-17 04:38:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c102b48a-702e-3c3f-a720-b68dcb497374 | -3.41293 | -50.12488 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e533073e-8ad2-3de1-9262-11cd5528c61d | -4.25327 | -46.06178 | 2025-11-17 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d25535d4-a412-3419-9138-7b8a5d9ff23f | -4.25442 | -46.82995 | 2025-11-17 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 745cea7b-3e74-319d-8ec1-0572e94f3776 | -5.12328 | -56.04221 | 2025-11-17 04:38:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0abfa2bb-b079-3a8f-9cae-04d24acd2cbd | -8.12148 | -43.52777 | 2025-11-17 04:38:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f71c2480-7e10-303a-aa55-bb8b38452ea0 | -7.26099 | -48.01142 | 2025-11-17 04:38:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1f64cb2-2f33-3a96-bb4b-36f86b839edb | -3.30207 | -53.84661 | 2025-11-17 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32e98557-3cbc-36b3-ac41-2efad2cdc385 | -4.83993 | -50.93781 | 2025-11-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 361ec983-477a-345e-b899-ec36fccd1d06 | -3.75237 | -50.42536 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6368f593-4349-38b4-9401-b05a218972c6 | -3.30307 | -50.21859 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92612f00-ac99-3818-bc35-df6a877500d8 | -4.42421 | -49.68788 | 2025-11-17 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eae47259-4677-3a74-8b3c-0ad3e286ef7f | -6.34374 | -44.22737 | 2025-11-17 04:38:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b44351c0-b3e2-31da-ba83-756b34d9e205 | -4.10652 | -47.10578 | 2025-11-17 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d4f17e4-c1e1-3184-8892-09b8e998b024 | -5.47816 | -41.39939 | 2025-11-17 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 46ab1454-893b-3081-8d09-c363141e26d4 | -8.33337 | -45.41202 | 2025-11-17 04:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aee0c228-81cd-3f33-8901-60275a95da8c | -3.79097 | -51.19805 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4b43cc5e-bc60-30e6-aa8b-25a6979800bb | -7.25705 | -48.01453 | 2025-11-17 04:38:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca5ada62-7457-33ec-9229-0fe38b55b880 | -5.67945 | -47.94521 | 2025-11-17 04:38:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48941585-dd21-3317-aaa8-0dddcbfc6a35 | -4.70927 | -45.10494 | 2025-11-17 04:38:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| de85f489-4348-387f-a86a-4dac857b26cb | -3.51837 | -50.32204 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5913988-6aab-386e-96b6-5bbfe5926dd9 | -3.59665 | -50.71789 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 418e1dd8-3664-3daf-8508-83a2582f0dda | -5.72601 | -42.73447 | 2025-11-17 04:38:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1d4a5bf4-e27c-3d59-908a-b62a567ee6ea | -0.75733 | -48.64224 | 2025-11-17 04:38:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb621003-5110-3d4b-b7ef-736bc51fb404 | -8.29721 | -43.95842 | 2025-11-17 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c4693e3-adfa-3eff-be25-088fa7c63b2d | -1.4671 | -53.41816 | 2025-11-17 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb9550f7-755b-3c49-8325-50448eac773b | -4.71822 | -55.72721 | 2025-11-17 04:38:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f6b4620-5ec2-3f76-8a2d-eb98b5311c1f | -2.2374 | -50.52047 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b1b8491e-7fb8-30f1-ade7-081f415f69b7 | -5.73788 | -46.27666 | 2025-11-17 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c9a2844-8ee8-3193-9c83-c321b76d1df9 | -7.47786 | -49.32876 | 2025-11-17 04:38:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3dee6f38-9e5d-3374-93f6-90b7899e308b | -2.99894 | -51.00626 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 94b3a1fd-2c48-3591-898c-0cbb1d03d67a | -3.36029 | -45.21387 | 2025-11-17 04:38:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ffe449a-cd84-3172-9400-4dac2e826efb | -4.76771 | -46.91403 | 2025-11-17 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00218a9a-6fbb-3158-8e03-50aea7f6afaa | -3.08226 | -52.92113 | 2025-11-17 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 898b7c07-8b11-3f8b-a8a6-e1194a4a5d07 | -8.21136 | -43.56044 | 2025-11-17 04:38:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be6762f0-90ef-331a-a99e-0aaec89746c8 | -5.7031 | -49.32354 | 2025-11-17 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 781dfbb1-ec12-325b-a6dc-e990249130f1 | -3.46083 | -50.11755 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 753e312e-19bb-36e5-97ee-94d02e408be6 | -3.15599 | -46.55881 | 2025-11-17 04:38:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3c279093-fa22-30a7-8987-19efce45575b | -5.34102 | -43.03146 | 2025-11-17 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c1cd0537-ad12-3fe9-9a18-460c8c304098 | -4.70068 | -46.31192 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 504f3eed-b81d-30a7-bc72-7a332f1aac0a | -7.22383 | -47.98341 | 2025-11-17 04:38:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 300fbc13-4d58-39bc-bc11-bc8a3ab346e7 | -6.67683 | -42.05392 | 2025-11-17 04:38:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3f1dcebc-b010-3e49-839e-f51513e9efee | -6.41018 | -49.9104 | 2025-11-17 04:38:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4160df00-14ac-3ff1-91eb-d8c42ed08173 | -3.84397 | -48.15842 | 2025-11-17 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e44aa60-e880-3c25-9c5d-cd0f58fe5458 | -2.9135 | -47.84337 | 2025-11-17 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72b84dab-dbd6-3ec0-ad70-0b684460c577 | -3.30614 | -53.84725 | 2025-11-17 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 413620a0-3f17-3241-919d-83ac5c223d9a | -3.40397 | -42.3651 | 2025-11-17 04:38:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 32d158a0-66de-3bca-ae51-0564f1879e67 | -4.06295 | -47.49699 | 2025-11-17 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1863957f-0a4b-3384-9071-df8b038dd8cd | -1.57959 | -48.64782 | 2025-11-17 04:38:00 | NOAA-21 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7440583-1ce9-33fc-9edd-a0ce7fdd4ff4 | -4.95215 | -49.83581 | 2025-11-17 04:38:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8b0183d-4ce4-3634-b550-12f5b18ebb69 | -8.12349 | -43.54471 | 2025-11-17 04:38:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0bd57de8-a786-3a75-90a6-eb7713c3c0b4 | -5.66237 | -48.9743 | 2025-11-17 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a5393f4-c878-308b-bde3-f67d63f728c5 | -5.77609 | -47.38326 | 2025-11-17 04:38:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8e9b07e-39aa-3282-bda9-2f6bf138421f | -5.3361 | -43.03496 | 2025-11-17 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 842db544-1f23-379b-8a8a-604b43fd3622 | -5.73048 | -42.73491 | 2025-11-17 04:38:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 06ec57f8-ef71-34d5-88f9-5b7c380b31cf | -3.49125 | -50.34011 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5843fd90-769d-3adf-bf45-4e343f7ae0c1 | -2.94029 | -51.0724 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c84358c-006a-328b-b003-03dd2fb61493 | -3.08588 | -51.25454 | 2025-11-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b28fca56-b235-3310-b644-eec4c89f67d7 | -3.38034 | -50.13456 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db9796ba-92f5-3cca-baac-77e47b025af3 | -3.61213 | -42.41852 | 2025-11-17 04:38:00 | NOAA-21 | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 69d95ecb-fb47-3e4a-b8dc-b1e41acd6fa5 | -3.24325 | -54.12563 | 2025-11-17 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5bfc15c9-23c9-38f9-b2c8-05096fc84148 | -6.22015 | -46.98151 | 2025-11-17 04:38:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a19854bd-20eb-3f59-b259-7ce189f6cde5 | -5.48452 | -44.83928 | 2025-11-17 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eed4a9fc-603b-3e9c-ac87-83c35ffcf874 | -3.23048 | -50.50224 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1016597-7d44-3208-a0b6-cde4653dce20 | -2.66995 | -51.88249 | 2025-11-17 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 42598cd6-fd29-31e9-a66c-898918ad2b33 | -3.33274 | -51.1396 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 966c6867-2ce4-3502-a231-2e6e93ca9c5f | -4.61822 | -47.26853 | 2025-11-17 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d151dbac-94eb-3650-9feb-b274a46bb516 | -4.40321 | -45.83915 | 2025-11-17 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a1644c06-a52d-349f-a205-6aa81c6880ae | -4.69756 | -46.30456 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9900b952-3f6a-37fe-b75c-c3c36021982c | -4.40447 | -45.83089 | 2025-11-17 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e0e47b9a-cf26-3570-b1d8-37525e8137b7 | -3.43483 | -50.11724 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 591cfee3-6bca-3531-ab1a-672dfd0e2d50 | -2.5163 | -47.81696 | 2025-11-17 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| ae2b839d-1999-3894-962c-ba398891e6b4 | -3.42273 | -50.37787 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 29bebc43-60f4-3aa8-ae89-24d1c43a4ec8 | -2.48174 | -49.36033 | 2025-11-17 04:38:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README33.md)
