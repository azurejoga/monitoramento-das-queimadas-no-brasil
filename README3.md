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
| 0c762440-7ea5-3b13-a765-0a947209949e | -2.7191 | -45.2208 | 2025-11-28 01:00:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 533.3 |
| eac27ba2-c9bc-348d-9649-11aa0239eb2d | -2.7006 | -45.1988 | 2025-11-28 01:00:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 68.5 |
| f50033df-98bf-3cc5-8ae4-079a90495a64 | -5.5584 | -46.488 | 2025-11-28 01:00:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 906080ae-b232-32bd-bd67-66054a903138 | -2.719 | -45.2433 | 2025-11-28 01:00:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 109.1 |
| e22f8fec-149f-3025-b0bb-b50f926de104 | -2.42 | -45.7462 | 2025-11-28 01:00:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 55.7 |
| a49f53bc-3ddb-3560-9c0d-bfb7a25bacef | -9.4 | -40.3722 | 2025-11-28 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 197.9 |
| 7045921b-4bb4-3752-a7b8-1d6830414f22 | -3.8617 | -47.0657 | 2025-11-28 01:00:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 280.8 |
| 152e9195-c975-3f8b-8028-b573ef057339 | -5.5396 | -46.5115 | 2025-11-28 01:00:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| b33bc252-6638-35ac-8065-6c9677329dc6 | -2.7006 | -45.2214 | 2025-11-28 01:00:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 146.4 |
| 00421685-59b4-324e-8bf7-d2841bd04916 | -2.7104 | -47.4147 | 2025-11-28 01:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 08221409-14cc-3886-89f2-1dcb9cd55411 | -9.4004 | -40.3474 | 2025-11-28 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 150.0 |
| 14e06e1f-9606-37bf-bfb1-796aabb0e1cb | -9.3813 | -40.3501 | 2025-11-28 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 297.7 |
| 9b63c281-83e1-39e4-ab7c-23a2f9deeacd | -9.3805 | -40.3998 | 2025-11-28 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 90.9 |
| 444f6648-bcab-3c23-a717-080adb2a528e | -3.8431 | -47.0666 | 2025-11-28 01:00:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 218.2 |
| bc9001b7-591f-315b-bf5e-ad11c9c64678 | -3.8978 | -47.2395 | 2025-11-28 01:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 715d0eac-6560-3536-86b7-99924547328a | -3.8618 | -47.0438 | 2025-11-28 01:00:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 149.9 |
| 400fa3d8-8ff4-3f15-8bec-6bad667663d3 | -2.7192 | -45.1982 | 2025-11-28 01:00:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 213.1 |
| 6877c1c2-0f49-3ca6-8374-f4670079fd77 | -20.4715 | -47.4711 | 2025-11-28 01:00:00 | GOES-19 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 3b80ceb7-90ff-3b8f-b5d5-f055b5dbd697 | -3.8432 | -47.0446 | 2025-11-28 01:00:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 121.9 |
| cd31de24-648e-38eb-bfb2-771ae9d322cc | -1.8245 | -54.332 | 2025-11-28 01:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 36cba4ab-43c6-3cbe-98bf-e74c844bec70 | -9.3809 | -40.375 | 2025-11-28 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 409.7 |
| 7e51058f-2e28-38da-97c3-5e0e2ba0f18a | -9.3809 | -40.375 | 2025-11-28 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 422.1 |
| 045d315d-7145-3559-9af2-848c776b0ef7 | -9.3813 | -40.3501 | 2025-11-28 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 294.9 |
| 3e2c4a68-4a39-3c17-b151-8e12f1144a59 | -5.5582 | -46.5102 | 2025-11-28 01:10:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 950f2bfb-c2ed-32eb-905b-9041934a1c3b | -9.4004 | -40.3474 | 2025-11-28 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 179.0 |
| c3d3cb88-af0c-368b-b87f-325090ef189a | -3.8432 | -47.0446 | 2025-11-28 01:10:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 722b3d06-ba3c-3635-9485-bfdd9fbda94b | -2.7025 | -49.5634 | 2025-11-28 01:10:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 5ec8bfda-9fda-3d72-bb9d-865a082bfcbc | -17.5756 | -46.669 | 2025-11-28 01:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 6ccab1d4-a8bc-389e-afcf-e61f7d1d0017 | -2.7006 | -45.2214 | 2025-11-28 01:10:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 114.4 |
| cd64e667-43f5-3800-b648-014a629513b5 | -1.8245 | -54.312 | 2025-11-28 01:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 0093dece-3c37-3f20-b90e-64d5e9ea1f58 | -2.719 | -45.2433 | 2025-11-28 01:10:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 69.8 |
| df619aac-af49-3c7f-89ee-04901ce2a1e5 | -5.5398 | -46.4893 | 2025-11-28 01:10:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| bbbb845b-87d5-3413-bde2-0fd289747120 | -9.4 | -40.3722 | 2025-11-28 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 249.2 |
| c62dbe40-81a9-3627-ab35-7ca95620333c | -3.8431 | -47.0666 | 2025-11-28 01:10:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 9b69a4d4-8f7b-347e-ac33-371e722358a9 | -3.8617 | -47.0657 | 2025-11-28 01:10:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 188.4 |
| 73bce383-30e5-3f6b-bf04-d0d33d178619 | -5.5584 | -46.488 | 2025-11-28 01:10:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| bfa4addd-cb67-3740-ab53-08cbf14502dc | -1.8245 | -54.332 | 2025-11-28 01:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| b42133aa-4678-3d0a-ae44-56b2234c5bdf | -9.3805 | -40.3998 | 2025-11-28 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 95.2 |
| 31480989-f473-39de-a65b-0c30788a0995 | -2.7191 | -45.2208 | 2025-11-28 01:10:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 329.3 |
| 9a1c8ed2-15ff-33b2-b17d-655e54f1f235 | -5.5396 | -46.5115 | 2025-11-28 01:10:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 4085ad85-ac01-30bf-9c88-8e16b1c1c843 | -3.8618 | -47.0438 | 2025-11-28 01:10:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 109.9 |
| cc73d8e6-d17c-37a5-976f-8c9259c7b0bc | -2.7006 | -45.1988 | 2025-11-28 01:10:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 0fdeab0e-60d8-3fe1-bcfd-e9c5293a434a | -2.7192 | -45.1982 | 2025-11-28 01:10:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 169.6 |
| 06d7e3f8-5a79-3c9d-81c0-23e437b1615e | -20.4715 | -47.4711 | 2025-11-28 01:10:00 | GOES-19 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 97.9 |
| afa9410a-0f1f-33b9-b640-b7d80f2fd66b | -1.8428 | -54.3317 | 2025-11-28 01:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| ed4165b5-bb98-3e90-a341-7ee0cb2a00ee | -2.7191 | -45.2208 | 2025-11-28 01:20:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 284.0 |
| a82a9525-f563-3669-98c7-8db1da3a12ba | -5.5582 | -46.5102 | 2025-11-28 01:20:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 112d504e-2e19-3681-adb9-e94bb99c184c | -5.5398 | -46.4893 | 2025-11-28 01:20:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| a9664050-48e4-3b51-81a5-f387319984eb | -9.3809 | -40.375 | 2025-11-28 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 452.6 |
| 30493351-16e7-3db6-80b2-732a222d69e8 | -9.3813 | -40.3501 | 2025-11-28 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 282.0 |
| 264e857f-780c-379a-bdb5-36646bdb279a | -9.4004 | -40.3474 | 2025-11-28 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 177.5 |
| 94350c0b-67a8-3674-9ada-4b9217c914d4 | -3.8432 | -47.0446 | 2025-11-28 01:20:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 88.6 |
| d86bc2d8-dc95-3cde-a864-230a92a0185d | -2.7025 | -49.5634 | 2025-11-28 01:20:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| c05db483-b9e1-301e-bb34-24895abdb9b5 | -3.8431 | -47.0666 | 2025-11-28 01:20:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 5e322f64-ac85-330f-971d-956ea3fed0db | -1.8245 | -54.312 | 2025-11-28 01:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| e91cf9a6-07a7-34ef-9c17-a2e517a6e0a7 | -9.4 | -40.3722 | 2025-11-28 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 277.5 |
| 181c6d11-5faa-35a3-95c6-3163a05c7668 | -3.8618 | -47.0438 | 2025-11-28 01:20:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 163.8 |
| 08f83b47-c9bc-3794-8234-9866bed4158e | -2.7192 | -45.1982 | 2025-11-28 01:20:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 7a3c1eae-0e8f-3013-a854-106a53c7e50d | -2.7006 | -45.2214 | 2025-11-28 01:20:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 6283aee2-8e33-35e6-86f4-1c01802efa20 | -20.4715 | -47.4711 | 2025-11-28 01:20:00 | GOES-19 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 5ad42080-e455-3406-9d49-19e461d582f5 | -3.8617 | -47.0657 | 2025-11-28 01:20:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 233.7 |
| 185629a2-98d8-305d-8c7c-7bc097671ff9 | -5.5396 | -46.5115 | 2025-11-28 01:20:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| a4d69b79-6a20-3c8c-9c86-846bd5255483 | -1.8245 | -54.332 | 2025-11-28 01:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 0b54f43d-217b-3597-8f4f-c15fbc4823c5 | -16.14662 | -59.96544 | 2025-11-28 01:28:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bfb415c0-1313-3c8b-a25d-b1748a5f8aad | -15.59917 | -59.93902 | 2025-11-28 01:28:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ec702354-7867-3d57-acfb-fb4ffe51d59d | -16.06343 | -59.29873 | 2025-11-28 01:28:00 | TERRA_M-M | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 77fdd8be-a868-3c5e-b41b-806a8e1090d6 | -1.8428 | -54.3317 | 2025-11-28 01:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| b403036a-5388-3e2d-a5e1-9b9171dcb317 | -1.8245 | -54.332 | 2025-11-28 01:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 276.9 |
| be92e38d-aa15-3400-9055-6d3d52cacf5c | -1.8429 | -54.3117 | 2025-11-28 01:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 3af27a90-749a-3437-a600-846d8cb6114e | -1.8245 | -54.312 | 2025-11-28 01:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 134.2 |
| 66dda142-57b6-3648-afa4-2b7f94c56b12 | -2.7006 | -45.2214 | 2025-11-28 01:30:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 80.1 |
| c76c2de6-376d-3da2-9600-70dec56efdbc | -9.3809 | -40.375 | 2025-11-28 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 414.8 |
| f46761c7-8b76-35dc-b09f-070624d8439b | -3.8617 | -47.0657 | 2025-11-28 01:30:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 58.8 |
| cbeae2fb-b2e1-3d53-9ece-337267a01145 | -9.3813 | -40.3501 | 2025-11-28 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 279.4 |
| 2c0e2f0c-03ba-3d5f-9081-3da74b3f6e2c | -5.5582 | -46.5102 | 2025-11-28 01:30:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 4aa25ea8-2664-3035-bb88-044c0445af4f | -9.4004 | -40.3474 | 2025-11-28 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 152.2 |
| 0ad2609b-7e1c-3ad5-a106-474c771a1c52 | -20.4715 | -47.4711 | 2025-11-28 01:30:00 | GOES-19 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 69.8 |
| b2e67ea5-0964-3295-b953-449f0b68a8a6 | -9.3805 | -40.3998 | 2025-11-28 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 92.6 |
| 0253d081-c82a-32ff-b5fe-5fcdac102eeb | -2.7191 | -45.2208 | 2025-11-28 01:30:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 175.2 |
| ea7ad09b-e0ee-3ea0-8feb-6ebef29ca929 | -3.8618 | -47.0438 | 2025-11-28 01:30:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 52.2 |
| dbed5b72-9b19-3e59-982a-b65837db4312 | -3.8431 | -47.0666 | 2025-11-28 01:30:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 45.3 |
| aa0d62fb-84f1-3162-9cbc-b42946cbf1ba | -5.5396 | -46.5115 | 2025-11-28 01:30:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 2c5c4a7c-a64a-3684-a351-5f563a59841a | -2.7025 | -49.5634 | 2025-11-28 01:30:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 425511a3-33d6-355d-ae6c-33f4396b8b9a | -9.4 | -40.3722 | 2025-11-28 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 217.9 |
| 2b1f872b-d8c0-34e5-9134-020c9a066ead | -2.7192 | -45.1982 | 2025-11-28 01:30:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 25eeab28-9866-3d39-aa31-d1fe8e6cd492 | -14.74705 | -60.1307 | 2025-11-28 01:30:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f426a227-4297-3925-8f30-8540fcb3b370 | 2.87287 | -60.25904 | 2025-11-28 01:34:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 17.4 |
| fab7967d-f1d8-32f8-841b-2054fceb74a0 | -20.4715 | -47.4711 | 2025-11-28 01:40:00 | GOES-19 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 347875f4-0c26-346a-b881-fd517402a098 | -1.8428 | -54.3317 | 2025-11-28 01:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 90efe66f-a41c-35b2-b4c9-511b1ce0f40c | -2.7191 | -45.2208 | 2025-11-28 01:40:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 149.9 |
| 1b2e32e4-d0ba-38f0-889f-3dea1f30bc79 | -3.7508 | -46.9608 | 2025-11-28 01:40:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 0b930b59-0fd1-3ed8-b238-63954b7ca874 | -2.6181 | -47.3521 | 2025-11-28 01:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| a32e0d8e-4893-31ae-a704-dba86193aa6c | -5.5396 | -46.5115 | 2025-11-28 01:40:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 3895fadd-d764-3f96-9af1-f425c4bbdedf | -9.3809 | -40.375 | 2025-11-28 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 407.6 |
| 8be7aa83-b520-333f-aaa9-6b8a2f2db9e1 | -9.3813 | -40.3501 | 2025-11-28 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 223.4 |
| 920e599d-0090-33cf-bc12-59c040245749 | -2.7025 | -49.5634 | 2025-11-28 01:40:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 24d2bc86-94a9-3435-8cf3-fe4f56e18fa2 | -9.4004 | -40.3474 | 2025-11-28 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 130.3 |
| 7b388dfd-75a5-37e8-be0d-0007c829d8c0 | -1.8245 | -54.312 | 2025-11-28 01:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 312d076c-77ca-366c-a64f-ce1074ff7d74 | -5.0631 | -40.8171 | 2025-11-28 01:40:00 | GOES-19 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 73.8 |
| e51ebc74-6eec-3ae6-9b3f-4d78808fab7f | -2.7192 | -45.1982 | 2025-11-28 01:40:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 60.3 |


[Clique aqui para ver as próximas entradas](README4.md)
