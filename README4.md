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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe3d5e3d-c5a1-3511-979a-82ef9d3f2316 | -2.1541 | -54.6066 | 2024-12-05 02:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| f73b89bf-d369-3108-b520-94e2743adcb0 | -2.2668 | -53.5405 | 2024-12-05 02:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 9be8910a-ba66-3f1d-be72-1c1a2eeaca4e | -2.1724 | -54.6263 | 2024-12-05 02:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 764ab6f8-a06e-37cf-acba-eafb9a26bcdf | -6.9346 | -43.5168 | 2024-12-05 02:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 77.7 |
| fb44711b-54fc-37a8-a445-fa3e0c7900d5 | -2.1541 | -54.6266 | 2024-12-05 02:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| df8d411d-089d-3a47-bc09-3575db92c6b0 | -4.0184 | -48.9218 | 2024-12-05 02:30:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 2f675dac-8c7a-326c-bf14-6bcfe710d99a | -2.1724 | -54.6263 | 2024-12-05 02:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 60bb7747-f7ce-3c4a-99e5-0fe2164c6825 | -6.9344 | -43.5401 | 2024-12-05 02:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 163.1 |
| ffa70467-9aef-3930-bda3-61c984a142ff | -3.9999 | -48.9226 | 2024-12-05 02:30:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 5e82d2b0-4f2c-3408-907c-7010f8626c0f | -4.0 | -48.9012 | 2024-12-05 02:30:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 409cd36e-720a-3750-9187-6980ecb534f0 | -2.2668 | -53.5405 | 2024-12-05 02:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| de788d24-68e3-35f7-879d-2fdf0d5dda93 | -2.1725 | -54.6063 | 2024-12-05 02:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 1175627d-99d9-324f-8c6b-485aa26a2ec9 | -6.9344 | -43.5401 | 2024-12-05 02:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 132.5 |
| b351fd20-9866-3035-ab91-65d0b355f328 | -2.1724 | -54.6263 | 2024-12-05 02:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| a39b785e-aece-3d9e-a771-229db0b4a143 | -4.0311 | -46.6619 | 2024-12-05 02:40:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 63.0 |
| b02d753a-7405-3a47-8f1b-74d50e54f08d | -2.1541 | -54.6266 | 2024-12-05 02:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 4447d47a-95b5-3e2a-9fb2-31a699c06356 | -2.1541 | -54.6066 | 2024-12-05 02:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 52ccc21d-7850-3e76-9370-4d9e9284a3ba | -6.9346 | -43.5168 | 2024-12-05 02:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 75.3 |
| b79f4d70-6f51-3a8a-bc86-ddf28d57bfb9 | -9.4782 | -35.7702 | 2024-12-05 02:40:00 | GOES-16 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 103.3 |
| 6013dc7d-65ca-371e-a837-bebbc37b4c15 | -9.4975 | -35.7669 | 2024-12-05 02:40:00 | GOES-16 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 105.4 |
| 54711f46-8975-3239-adfa-977b35e1a69d | -2.1724 | -54.6263 | 2024-12-05 02:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 7f2edd01-6016-38ad-a08c-066a3516001c | -9.7785 | -36.1789 | 2024-12-05 02:50:00 | GOES-16 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 90.0 |
| 8c046383-9f17-3dd4-84ba-d38824a71755 | -6.9344 | -43.5401 | 2024-12-05 02:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 173bd632-b774-3429-a09a-c6df2ce5e49c | -6.9156 | -43.5418 | 2024-12-05 02:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| e8292704-58a8-384d-96f4-3a98bef3e032 | -6.9532 | -43.5384 | 2024-12-05 02:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 3ae20bc6-27d0-3ca2-ab3d-57ece2cdfd52 | -2.1724 | -54.6263 | 2024-12-05 03:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 0e5813f2-8dfa-3e7e-be96-04a0803f9bed | -6.9344 | -43.5401 | 2024-12-05 03:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 3711c382-d98e-3358-8fbb-f50bb9611562 | -2.7543 | -45.7134 | 2024-12-05 03:00:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 56.8 |
| a46587bc-cddd-3bf6-ab7c-7e7aa5956c0a | -6.9346 | -43.5168 | 2024-12-05 03:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 73.3 |
| a3b35000-c5f1-3f06-844f-d78b35f2a771 | -8.18042 | -35.27051 | 2024-12-05 03:06:00 | NOAA-21 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 34eae4ab-6e4c-3eba-91a6-9aa7da99f964 | -6.66062 | -34.97092 | 2024-12-05 03:06:00 | NOAA-21 | BAÍA DA TRAIÇÃO | PARAÍBA | Brasil | 2501401 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| a9d397c4-2bd8-3842-8021-3d2c13ef9aa6 | -7.56969 | -35.23763 | 2024-12-05 03:06:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Caatinga | 16.0 |
| eeeee111-2e2b-37bb-8cd9-632032e38dc3 | -9.98452 | -36.00109 | 2024-12-05 03:06:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 8bf3cee0-f527-3051-8762-69564761eeb9 | -7.5644 | -35.23681 | 2024-12-05 03:06:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Caatinga | 16.0 |
| c1f7dda6-ef93-307b-9430-304b5584c27d | -8.9752 | -35.63261 | 2024-12-05 03:06:00 | NOAA-21 | NOVO LINO | ALAGOAS | Brasil | 2705606 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4cf6682e-1e78-31ba-b26d-49ace855ee4c | -9.98856 | -35.99918 | 2024-12-05 03:06:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 2e05aa9c-ed90-308d-9a50-ea178a2a670d | -6.66589 | -34.97179 | 2024-12-05 03:06:00 | NOAA-21 | BAÍA DA TRAIÇÃO | PARAÍBA | Brasil | 2501401 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 8a502124-907a-3725-96da-94bb2261051d | -9.98513 | -35.99772 | 2024-12-05 03:06:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7e6adede-6cc6-3514-803b-74ec7ef1f795 | -7.42604 | -39.89342 | 2024-12-05 03:06:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 15df5539-fe84-3a14-b360-cfa604d762bf | -7.56323 | -35.24332 | 2024-12-05 03:06:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 8ed42734-54ef-32a7-8807-3301e5dcbc7a | -8.17982 | -35.27274 | 2024-12-05 03:06:00 | NOAA-21 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 7548a43c-c237-37b4-86eb-325e3e6d4181 | -7.42387 | -39.89304 | 2024-12-05 03:06:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 670aa5ae-e2a4-388e-98c6-e51249b94aec | -7.43091 | -39.89425 | 2024-12-05 03:06:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e7de8711-8288-339e-85fb-02dc04187746 | -8.18038 | -35.26956 | 2024-12-05 03:06:00 | NOAA-21 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c4e9bd3d-9ec0-3332-80f5-050d18bbe2b5 | -7.43308 | -39.89468 | 2024-12-05 03:06:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 4.6 |
| e729583c-343b-3174-a34c-f970e1cf4e94 | -7.56381 | -35.24006 | 2024-12-05 03:06:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Caatinga | 16.0 |
| d98db013-72ae-3844-a1de-818c4f556b81 | -10.67591 | -37.20081 | 2024-12-05 03:08:00 | NOAA-21 | SANTA ROSA DE LIMA | SERGIPE | Brasil | 2806503 | 28 | 33 | nan | nan | nan | Mata Atlântica | 24.7 |
| f8a6e4d9-5956-3e95-a62b-698810cc0848 | -10.6745 | -37.20818 | 2024-12-05 03:08:00 | NOAA-21 | SANTA ROSA DE LIMA | SERGIPE | Brasil | 2806503 | 28 | 33 | nan | nan | nan | Mata Atlântica | 19.9 |
| fdff97dc-a440-353a-9a06-0a37765a5c43 | -10.6752 | -37.20451 | 2024-12-05 03:08:00 | NOAA-21 | SANTA ROSA DE LIMA | SERGIPE | Brasil | 2806503 | 28 | 33 | nan | nan | nan | Mata Atlântica | 19.9 |
| bc5f4e64-a5fc-3772-ba5e-95863a5063bf | -10.49763 | -36.70597 | 2024-12-05 03:08:00 | NOAA-21 | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| 61617ab1-a09a-3927-b555-f4d302a86b3e | -13.36171 | -41.34185 | 2024-12-05 03:08:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bef8f2f6-656d-3d1d-a43d-710112e144fa | -10.68091 | -37.20543 | 2024-12-05 03:08:00 | NOAA-21 | RIACHUELO | SERGIPE | Brasil | 2805901 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 127a49be-2e5d-3b99-a385-205065638125 | -10.50379 | -36.7035 | 2024-12-05 03:08:00 | NOAA-21 | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| 2197f6ff-27d3-3c44-b96c-b708b12169aa | -10.68161 | -37.20178 | 2024-12-05 03:08:00 | NOAA-21 | RIACHUELO | SERGIPE | Brasil | 2805901 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| ee80eeca-a964-3987-b4ad-80c9b6a8ea19 | -13.35482 | -41.34032 | 2024-12-05 03:08:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d7d92286-6c7a-3f1d-af31-cc78a750d730 | -10.49832 | -36.70225 | 2024-12-05 03:08:00 | NOAA-21 | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| bb55be46-d883-3fab-9748-4756e451f84c | -10.5031 | -36.70724 | 2024-12-05 03:08:00 | NOAA-21 | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| 6a9799fa-16d2-3a32-b0e4-d4a69c771524 | -10.50265 | -36.70727 | 2024-12-05 03:08:00 | NOAA-21 | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 6884550a-c613-32b1-8a5c-2d1fbd062a1d | -13.36088 | -41.34201 | 2024-12-05 03:08:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cbeb66a0-08e6-3d32-83b0-c7e75a922af7 | -13.35398 | -41.34051 | 2024-12-05 03:08:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ff0ca238-cb11-3be3-9f74-b29cc099d9c4 | -10.50337 | -36.70354 | 2024-12-05 03:08:00 | NOAA-21 | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| feabf6c2-8a08-3d32-83df-f154cd940687 | -6.9344 | -43.5401 | 2024-12-05 03:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 19ae8ef5-ffe2-345e-9895-349feb3b5d4f | -6.9346 | -43.5168 | 2024-12-05 03:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 7575dd7c-57f5-346e-840f-424f0e1506e0 | -19.16875 | -40.139 | 2024-12-05 03:10:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| af36e470-2623-3218-aa2c-a75782351157 | -18.509 | -39.92375 | 2024-12-05 03:10:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 640f972b-190f-329e-b37a-3e723ca84afb | -19.16292 | -40.13772 | 2024-12-05 03:10:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| f4cdab4e-61ce-3654-a77d-307f6315765c | -6.9344 | -43.5401 | 2024-12-05 03:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 123.4 |
| a669e088-d039-3ab6-bce6-732f1c4a423e | -6.9532 | -43.5384 | 2024-12-05 03:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 3d1efc4c-57ea-3581-8f33-c2e7345b8788 | -6.9346 | -43.5168 | 2024-12-05 03:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 4306f053-b348-3354-b6cb-277978827104 | -4.71097 | -38.4345 | 2024-12-05 03:27:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 023529fe-e237-3006-8494-e9b3346412e7 | -4.70997 | -38.43742 | 2024-12-05 03:27:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8faa4026-d8a9-3866-8d96-246e051f20c4 | -5.1802 | -37.59488 | 2024-12-05 03:27:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d350c2e3-559f-36f2-bf5c-694e232276a6 | -6.59895 | -35.25538 | 2024-12-05 03:27:00 | NPP-375D | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 260c1630-5be6-3a0f-afd0-c4ca673b8952 | -7.56185 | -35.23634 | 2024-12-05 03:27:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5509383b-4bdf-3069-976e-caa274b56831 | -7.46889 | -34.81384 | 2024-12-05 03:27:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 402b420c-ca0a-344f-83d0-6a492eccfb86 | -6.49304 | -35.19692 | 2024-12-05 03:27:00 | NPP-375D | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c8b2b576-15d6-33cb-9879-aa8720b579e0 | -5.17592 | -37.59415 | 2024-12-05 03:27:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a152657c-24bc-3061-b0dc-9474c66aa5b8 | -4.70457 | -38.71978 | 2024-12-05 03:27:00 | NPP-375D | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9b96573f-9788-362e-9daa-cb30e7e429e3 | -4.71079 | -38.43266 | 2024-12-05 03:27:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 26fdf91f-b080-32b1-8d8a-c066f630fc7c | -12.23462 | -38.09573 | 2024-12-05 03:29:00 | NPP-375D | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6f3e0d8b-0b4d-34f9-a8a2-8d49dcd35589 | -6.13741 | -43.95037 | 2024-12-05 03:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95e658db-75f9-3b6e-a324-6190193059f9 | -6.93655 | -43.54446 | 2024-12-05 03:29:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 04f2cd4d-680d-357e-a6c4-e3f6d4830008 | -6.13179 | -43.94698 | 2024-12-05 03:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53f7fd3f-1a29-33df-89bb-56815b381e14 | -6.93667 | -43.53707 | 2024-12-05 03:29:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 78f6de2e-17df-3ecb-9d0c-b73e5712afe6 | -10.68545 | -40.48627 | 2024-12-05 03:29:00 | NPP-375D | ANTÔNIO GONÇALVES | BAHIA | Brasil | 2901809 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| aa934450-8fe0-3f5d-b6e5-e9edd26474f7 | -6.93493 | -43.54636 | 2024-12-05 03:29:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 8116f5fe-b985-3f59-ba0f-f7317fb6dde6 | -6.93039 | -43.54327 | 2024-12-05 03:29:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8db4435c-f394-3ba8-b9af-c8015cbcc7a2 | -8.97574 | -35.9896 | 2024-12-05 03:29:00 | NPP-375D | SÃO JOSÉ DA LAJE | ALAGOAS | Brasil | 2708303 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a540ad5e-d1f1-3d13-88d9-c6dce765163a | -6.92877 | -43.5452 | 2024-12-05 03:29:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 006314a0-4cf1-337f-a87d-df8edad0d6a0 | -11.8711 | -38.35575 | 2024-12-05 03:29:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 182d6be4-6454-3eaa-878c-a90212a2783d | -10.49913 | -36.70596 | 2024-12-05 03:29:00 | NPP-375D | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9cecbc47-da18-3964-a66f-53b5be5c6662 | -6.93581 | -43.54169 | 2024-12-05 03:29:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 37b71999-892c-3a76-a140-f14e02f0e7ec | -9.34206 | -41.26733 | 2024-12-05 03:29:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2b81a8a3-e02c-33c4-a8b0-265eb741e9f5 | -8.97549 | -35.63332 | 2024-12-05 03:29:00 | NPP-375D | NOVO LINO | ALAGOAS | Brasil | 2705606 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 432a698e-9c77-368e-b331-3cf62b45a919 | -7.49441 | -37.13382 | 2024-12-05 03:29:00 | NPP-375D | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c64111d7-3c55-3624-9462-4cadc210787e | -7.42652 | -39.89671 | 2024-12-05 03:29:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 4.9 |
| d853666d-fd8c-3c35-9044-cb089d705b7d | -9.89554 | -44.34736 | 2024-12-05 03:29:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f3e5e92d-5b23-3c73-a6df-c1af8ef221a5 | -10.50286 | -36.70667 | 2024-12-05 03:29:00 | NPP-375D | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cc74077b-1629-341f-8d35-302280b7b13d | -10.47171 | -36.98586 | 2024-12-05 03:29:00 | NPP-375D | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b73d34fd-86c7-310c-a6ce-e65c0cde2c4f | -6.92594 | -43.53258 | 2024-12-05 03:29:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |


[Clique aqui para ver as próximas entradas](README5.md)
