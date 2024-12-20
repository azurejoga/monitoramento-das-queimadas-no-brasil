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
| 1872b75c-5a8d-396d-9e13-c6f35cbfb411 | -7.2573 | -44.708 | 2024-12-20 00:45:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d1ef2697-d404-3fe3-88c7-c070a1483023 | -2.652 | -47.185101 | 2024-12-20 00:45:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1b7df1a-a418-3e87-a00b-03c59de19c17 | -4.9298 | -41.351601 | 2024-12-20 00:45:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f5f6c4eb-9118-3fd0-a885-d9b89d0a5cfe | -3.0077 | -46.719299 | 2024-12-20 00:45:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a391e85-2d47-33a3-b419-f5aeb436a51c | -9.2216 | -60.3302 | 2024-12-20 00:50:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 8e239d2d-3d01-3cf9-b9df-74e5d1bcff69 | -2.7661 | -47.3912 | 2024-12-20 00:50:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 31620cd2-d659-3b62-8c57-3a3b616abc9f | -9.2215 | -60.3495 | 2024-12-20 00:50:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 24821e21-0798-3f74-b363-1a9e41e04bfe | -9.2216 | -60.3302 | 2024-12-20 01:00:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 268cdd7f-c043-3d11-964d-56ed4c092780 | -9.2215 | -60.3495 | 2024-12-20 01:00:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 9dc9165e-6e49-3e69-af15-05e0fe34ee3e | -3.2 | -46.78 | 2024-12-20 01:00:00 | MSG-03 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41b2241b-249b-3e9c-8aed-43bae186077e | -3.23 | -46.78 | 2024-12-20 01:00:00 | MSG-03 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 651a1974-fc77-3e83-b7ac-68831dc916bd | -3.26 | -46.79 | 2024-12-20 01:00:00 | MSG-03 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 11f89b9d-8b8c-310a-8171-11c05390b954 | -3.23 | -46.83 | 2024-12-20 01:00:00 | MSG-03 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf95d4d8-69c3-3d61-b96b-8873d1621683 | -3.232 | -46.8056 | 2024-12-20 01:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 456.7 |
| 09533447-fd0b-36a1-843d-b6d91abc6133 | -9.2216 | -60.3302 | 2024-12-20 01:10:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 08f5c601-a34b-3fd8-b133-3a004a714f71 | -2.7661 | -47.3912 | 2024-12-20 01:10:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 9f4b1d34-8cbe-37ab-9048-83cf06d9bb96 | -3.2321 | -46.7836 | 2024-12-20 01:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 535.0 |
| 494f9305-23b4-30c6-a27d-6d72b56be129 | -3.2135 | -46.8063 | 2024-12-20 01:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| e860fd1b-e771-3507-986e-0da61c46d6f0 | -3.2506 | -46.8049 | 2024-12-20 01:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 119.6 |
| 942cff79-9020-3866-aadc-76e93f0365e2 | -9.2403 | -60.3292 | 2024-12-20 01:10:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 67e88f8d-7033-37b5-acd7-e6861e18fe00 | -2.5887 | -45.3151 | 2024-12-20 01:10:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 896c0b0f-2443-3eb9-844d-ec309d9adb7d | -3.2507 | -46.7829 | 2024-12-20 01:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 135.3 |
| e9dc4fd7-64d1-3cd5-93b0-cc36503ec9db | -9.2215 | -60.3495 | 2024-12-20 01:10:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 7cbaac2a-ffb8-35fc-9bd3-eb5bb42f43a9 | -3.2136 | -46.7843 | 2024-12-20 01:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 32fd962e-345c-36d5-bc38-0d4304dc34c5 | -9.2216 | -60.3302 | 2024-12-20 01:20:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 02e118a9-b5d9-3d8e-b061-cbc127f2f02b | -9.2215 | -60.3495 | 2024-12-20 01:20:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 690ada05-4f79-3c4e-9cae-8d77233d69cd | -2.7661 | -47.3912 | 2024-12-20 01:20:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| b27a41be-9ffd-3f86-a365-121d651912fb | -9.2403 | -60.3292 | 2024-12-20 01:20:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 924b695b-890e-329a-830a-f1e59a26b899 | -20.9737 | -48.992401 | 2024-12-20 01:23:00 | METOP-B | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 82922347-239b-36cc-9632-64393a6e61fd | -9.2252 | -60.321098 | 2024-12-20 01:23:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ec6e8f93-e63b-39db-a65a-73b2eaa5db5d | -9.2154 | -60.323399 | 2024-12-20 01:23:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 24f567f3-950e-37e2-9466-03720d1733b8 | -9.2271 | -60.329201 | 2024-12-20 01:23:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1520e73e-3d77-3624-871c-a314f7cbb9ad | -9.2192 | -60.339699 | 2024-12-20 01:23:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 680928a2-555c-3df2-9cdd-e18e2feca523 | -9.229 | -60.337399 | 2024-12-20 01:23:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a5c479c6-8ff1-3012-b3e6-2f0e77272e9f | -20.9832 | -48.9893 | 2024-12-20 01:23:00 | METOP-B | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| eea0b02f-b631-3fc5-8a0a-6b2caa8ede6a | -9.2173 | -60.331501 | 2024-12-20 01:23:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 778058c9-9cb3-37ee-899a-06cc00466bc5 | -9.2216 | -60.3302 | 2024-12-20 01:30:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| d932ad10-dd41-3498-90a4-054140d60f64 | -3.2506 | -46.8049 | 2024-12-20 01:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 78b9c5ba-f146-3058-9a2c-bc566b097ddc | -3.2136 | -46.7843 | 2024-12-20 01:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| c6fb8d1d-72c1-3e80-a1ce-112c6160a881 | -9.2403 | -60.3292 | 2024-12-20 01:30:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 7411ff18-a18a-3ea4-8d4f-a5a4e12aa749 | -9.2215 | -60.3495 | 2024-12-20 01:30:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| d7ee5065-0fff-349c-af53-6457721845d2 | -3.2321 | -46.7836 | 2024-12-20 01:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 286.4 |
| 2b9669ef-c20a-302d-a9c0-30aa59d0da5c | -3.232 | -46.8056 | 2024-12-20 01:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 286.1 |
| 7e332fbf-fd11-3d83-8bb7-eabee9fc3902 | -20.9995 | -49.0191 | 2024-12-20 01:30:00 | GOES-16 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 82.2 |
| 872be04e-30cf-30f4-ace2-f254ba86e6c5 | -2.7661 | -47.3912 | 2024-12-20 01:30:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 7413f825-97b6-38a1-877e-1cb7ccaff982 | -3.2135 | -46.8063 | 2024-12-20 01:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 3a0be9c0-00a5-33ca-999c-80ed9c12a8bf | -3.2507 | -46.7829 | 2024-12-20 01:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 92c65bf7-23cb-3dba-824d-272061fdc84f | -20.99127 | -49.02381 | 2024-12-20 01:36:00 | TERRA_M-M | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 54.0 |
| 1dedac16-def6-3476-9dec-68a535f29b8d | -19.99181 | -54.74022 | 2024-12-20 01:38:00 | TERRA_M-M | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 50c9520d-9ca6-3397-ba39-ff7d9d71e5b6 | -18.76649 | -55.96102 | 2024-12-20 01:38:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 862437de-1eaf-3868-b17c-13f0cbeb0add | -15.03009 | -57.18391 | 2024-12-20 01:38:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d309a89a-a313-3fc3-85fd-edbd82380b0b | -15.03158 | -57.19387 | 2024-12-20 01:38:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 990fc507-2872-3d5e-a007-9540a8e5597a | -10.85502 | -56.68154 | 2024-12-20 01:38:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 375c72ce-ebe7-3061-962e-8edf1c3a2d22 | -3.232 | -46.8056 | 2024-12-20 01:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 204.2 |
| b5aa0fcd-fe4e-3fb1-abce-e6949bc6cfcb | -2.6245 | -45.6505 | 2024-12-20 01:40:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 60.8 |
| e9309dbd-d674-3551-b69f-8ab5d4cc30de | -3.2321 | -46.7836 | 2024-12-20 01:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 234.6 |
| 9f090755-d4af-321d-9139-c392b645f038 | -3.2506 | -46.8049 | 2024-12-20 01:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 62bab490-b79f-3ebf-8a9e-6e39426efe09 | -3.2507 | -46.7829 | 2024-12-20 01:40:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 425417f9-d205-3937-af3d-854de9c48bcd | -2.7661 | -47.3912 | 2024-12-20 01:40:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| e05b39c8-6987-323f-afee-fc5827e0eb03 | -3.2136 | -46.7843 | 2024-12-20 01:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 7b18eba7-bd37-32fe-aef8-b5238cf0e415 | -12.5682 | -57.7579 | 2024-12-20 01:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 94a03471-d1fd-384e-8914-f1fb9fa80834 | -3.2135 | -46.8063 | 2024-12-20 01:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 9042bb8a-5ecf-33b8-86e3-956de5c66ea4 | -3.2321 | -46.7836 | 2024-12-20 01:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 125.5 |
| 8c228ad5-b9fc-3658-8b43-9b20d5b7cfe3 | -2.6245 | -45.6505 | 2024-12-20 01:50:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 7b0a24eb-c016-37b5-a6b9-df3a8be04641 | -12.5492 | -57.7594 | 2024-12-20 01:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 362ae2b9-cafb-3813-be0a-55b67c554c03 | -3.232 | -46.8056 | 2024-12-20 01:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 126.5 |
| a7ea760a-acdb-3260-b7b8-457796a96d0f | -3.2507 | -46.7829 | 2024-12-20 01:50:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 37.9 |
| f1c319a4-ef8a-3b31-a55b-421f90b3110f | -3.2321 | -46.7836 | 2024-12-20 02:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 6eeee936-d2bd-3fa8-b9bb-9d56dd601282 | -2.6245 | -45.6505 | 2024-12-20 02:00:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 74.6 |
| f39996a6-83ac-3512-82fa-671eb9edc82a | -12.5492 | -57.7594 | 2024-12-20 02:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 060d71e8-ccd6-3efb-beb6-a9d35595afb2 | -3.232 | -46.8056 | 2024-12-20 02:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| f9a9cd8b-2450-3999-a49b-adde6d4172fa | -3.23 | -46.78 | 2024-12-20 02:00:00 | MSG-03 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27ae32c6-8ac0-3783-bc3b-3ee25e1d4eb9 | -9.2216 | -60.3302 | 2024-12-20 02:10:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 1f8876dd-c19d-37b8-a4b9-9945afa73019 | -2.6245 | -45.6505 | 2024-12-20 02:10:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 0159c3c8-ff1e-36e1-b627-2650150e7344 | -9.2403 | -60.3292 | 2024-12-20 02:20:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.8 |
| e71aacb8-71e6-3348-b3fd-ecdb2fcd4d36 | -9.2216 | -60.3302 | 2024-12-20 02:20:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 61b0fd02-e1cf-3478-83da-86d4a5660abb | -4.4662 | -45.5038 | 2024-12-20 02:20:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 7e0b43ca-d5ed-3cbb-93aa-41b0a59f5945 | -3.232 | -46.8056 | 2024-12-20 02:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 6cbc3b3e-61a3-392b-a003-a1d0996a498f | -3.2321 | -46.7836 | 2024-12-20 02:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| a21f8076-c7eb-3816-9956-7906eb27fcda | -9.2215 | -60.3495 | 2024-12-20 02:20:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 7735f3f0-3747-3d22-ac8a-57b48eed3944 | -3.232 | -46.8056 | 2024-12-20 02:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 31f12623-61a0-3963-a70e-9a886529cbc1 | -3.2321 | -46.7836 | 2024-12-20 02:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| e69a6419-407a-3c1b-9762-6dd58c351f95 | -3.2506 | -46.8049 | 2024-12-20 02:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 4b4e586b-2221-35c2-b1b3-caf9cc53cacf | -3.232 | -46.8056 | 2024-12-20 02:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| bc90853f-b56b-336c-bcce-86726ac34301 | -3.2321 | -46.7836 | 2024-12-20 02:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 5f478bfa-25ae-3e11-9295-af28192bb287 | -9.2216 | -60.3302 | 2024-12-20 02:40:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| f5e2a0a3-d9bb-379d-a2a7-aa86299262d3 | -9.2403 | -60.3292 | 2024-12-20 02:40:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 1a056f92-3972-3317-b2d7-70e3bcab0a5a | -3.2321 | -46.7836 | 2024-12-20 02:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| b0d37205-30eb-38af-b580-fc24bb764511 | -9.2215 | -60.3495 | 2024-12-20 02:50:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 0f402c55-ff14-3197-8c91-a799a8168da9 | -9.2216 | -60.3302 | 2024-12-20 02:50:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 9c57402e-8352-317b-bd45-6383520d04ff | -3.232 | -46.8056 | 2024-12-20 02:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 8a788c9a-4d8a-3568-b1f6-3397ef2802c4 | -9.2403 | -60.3292 | 2024-12-20 02:50:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 33a21fba-e62e-329a-bfad-f8761fe3857c | -3.2321 | -46.7836 | 2024-12-20 03:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| f5f096e9-68a7-311e-b4d5-73565e837f61 | -9.2215 | -60.3495 | 2024-12-20 03:00:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| dfad409b-11f7-3a07-b256-28da2621076d | -9.2216 | -60.3302 | 2024-12-20 03:00:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 6dd51f8a-a896-37bb-b6a9-e580884c3b75 | -3.232 | -46.8056 | 2024-12-20 03:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 0f332987-3b84-32fd-942d-c2f9258e8944 | -12.5492 | -57.7594 | 2024-12-20 03:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 2025cccb-95a2-3a2b-bbc0-89b2ab05a588 | -9.2216 | -60.3302 | 2024-12-20 03:10:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 6b2e7e43-59d8-35b8-8472-994de7bee807 | -9.2215 | -60.3495 | 2024-12-20 03:10:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 7a2643a4-542b-37c8-ad86-3f968cefcf24 | -9.2216 | -60.3302 | 2024-12-20 03:20:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 105.9 |


[Clique aqui para ver as próximas entradas](README4.md)
