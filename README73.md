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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8755fa3a-b300-39d9-96c1-777b25b9694a | -29.40122 | -50.58846 | 2025-10-17 04:25:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 60c9bb48-fbf1-39da-9e74-b532b70ff03d | -26.99018 | -49.25359 | 2025-10-17 04:25:00 | NOAA-21 | INDAIAL | SANTA CATARINA | Brasil | 4207502 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9c411ed6-097e-305e-8086-9db0e7b9c29d | -31.57062 | -52.32719 | 2025-10-17 04:25:00 | NOAA-21 | PELOTAS | RIO GRANDE DO SUL | Brasil | 4314407 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 1daaf936-7cb4-39ac-88e2-461d49c91f97 | -9.1378 | -46.6261 | 2025-10-17 04:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 339a029e-2240-3304-8dd7-801700f42371 | -12.4264 | -51.3027 | 2025-10-17 04:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 2902846d-5560-36ce-9d63-7bca5756890f | -5.9097 | -44.7317 | 2025-10-17 04:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 637b7666-ce78-3520-879a-d685646bc175 | -10.2939 | -44.0221 | 2025-10-17 04:30:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 4f1ea5b7-697d-3265-b2cc-fe3620055817 | -5.9095 | -44.7545 | 2025-10-17 04:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 7b922fec-c3ed-3d07-84e4-61a3c27b23a1 | -10.5132 | -43.4289 | 2025-10-17 04:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 30aed67e-a9de-3020-ac37-e7a9fb6fdb25 | -12.4073 | -51.3049 | 2025-10-17 04:30:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 0ead91dc-0038-3ea2-af73-4a3e94b43654 | -4.4246 | -43.4038 | 2025-10-17 04:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| e471b1c9-e466-3515-9f9c-21ec3b24fdc5 | -10.2935 | -44.0455 | 2025-10-17 04:30:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 91.7 |
| a78620af-5f39-3f50-a4cc-54ccb94a54ef | -5.3023 | -43.5562 | 2025-10-17 04:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 082bcaaa-e523-36ed-a77e-1de68e799cb5 | -12.4267 | -51.2814 | 2025-10-17 04:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.5 |
| c6521e9d-6a35-35d1-85fa-3570c9e812f4 | -10.4945 | -43.4079 | 2025-10-17 04:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 76e43a81-cde8-3d13-bfcf-54e2fc301b47 | -10.2748 | -44.0247 | 2025-10-17 04:30:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 8a1eb163-bd6b-34f4-954a-5c53da78e5fa | -10.534 | -49.5471 | 2025-10-17 04:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 5c06dd29-f807-3d70-b80c-ea1d6f08957a | -9.1375 | -46.6485 | 2025-10-17 04:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 0a186096-c8d1-3df9-bf6d-ec60a1ad94c9 | -4.4059 | -43.4049 | 2025-10-17 04:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 9963b1de-8269-3313-83b2-bb7c84129918 | -10.4941 | -43.4315 | 2025-10-17 04:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 48.1 |
| c824fa0d-7330-3d4e-9db3-71a3e76a0c30 | -12.4076 | -51.2836 | 2025-10-17 04:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 825c041c-d13a-3185-8d1c-3a2784f637da | -10.5136 | -43.4052 | 2025-10-17 04:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 50.7 |
| fa4ca65e-a138-3255-9510-c61a297c6049 | 1.8402 | -55.7034 | 2025-10-17 04:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 4bcd3667-7e14-37e5-a9b1-8ebbfbfc9713 | -10.9475 | -49.7605 | 2025-10-17 04:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 00e197e4-6e4a-3765-ba2c-c08fe2ad1f42 | -5.9095 | -44.7545 | 2025-10-17 04:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 771619de-732d-36c2-a8aa-9cf4387c650d | -14.342 | -51.4449 | 2025-10-17 04:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 1b58e5c3-dd9b-3e42-baf5-cb742525de13 | 1.8218 | -55.7037 | 2025-10-17 04:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 63b31fa9-c6ba-3d06-8d5c-5221ac0d6ef5 | -12.4069 | -51.3262 | 2025-10-17 04:40:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 010f0557-3dfa-3352-b0f2-c89f5d5467d3 | -14.3424 | -51.4234 | 2025-10-17 04:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 153c010c-007e-3e61-a0a9-66e9948fb5ac | -12.4267 | -51.2814 | 2025-10-17 04:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 110.9 |
| bb3f32d0-2eec-3a27-8ac9-d9abea974a5a | -10.2935 | -44.0455 | 2025-10-17 04:40:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 9e1423c6-4797-38d4-b54c-f1b67ed3758e | -10.4941 | -43.4315 | 2025-10-17 04:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 152bee48-60de-344d-b61e-060f334ed83a | -10.2748 | -44.0247 | 2025-10-17 04:40:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 76.5 |
| d76b2b6e-dc9a-3863-927e-326fa2925264 | -12.4264 | -51.3027 | 2025-10-17 04:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 224.6 |
| 647684fe-ffc4-3751-936d-7fd2b417c63c | -12.426 | -51.324 | 2025-10-17 04:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| bd01c18f-5b26-38cc-88b1-c829d5fc0bbe | -14.3417 | -51.4663 | 2025-10-17 04:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 53.2 |
| aa87555d-c6b7-3d2b-a6d6-a9e61b97a8c8 | -10.5132 | -43.4289 | 2025-10-17 04:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 259d8475-15d7-321e-928a-4243ba54db7a | -10.2939 | -44.0221 | 2025-10-17 04:40:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 2627d676-bf6f-34fe-a235-53b464763362 | -3.236 | -45.9639 | 2025-10-17 04:40:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 6383a14b-4703-319e-93ee-af4c9d936ebe | -6.231 | -44.4096 | 2025-10-17 04:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 01d2bf1e-7318-31e5-b6b7-59a39f96678c | -11.3976 | -44.2167 | 2025-10-17 04:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 48.4 |
| f6d7909f-2c3b-3677-8b44-9964e8e65e1b | -10.4945 | -43.4079 | 2025-10-17 04:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 40.2 |
| c6ba00b9-c398-3a1c-b16f-1e86720549b7 | -6.212 | -44.434 | 2025-10-17 04:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 5d98b559-04ea-3d46-bd5c-536e9bd4cdbe | -6.2308 | -44.4325 | 2025-10-17 04:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| c428c304-eb41-315d-a382-34af8ee1895b | -12.4073 | -51.3049 | 2025-10-17 04:40:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 217.0 |
| 4e3b8fb9-72ea-3f4d-bea9-cd7431b9fea0 | -12.4076 | -51.2836 | 2025-10-17 04:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 114.4 |
| ec421d00-1030-31ce-8e3f-8d4f3c3e7afd | -10.5136 | -43.4052 | 2025-10-17 04:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 2bafe271-68a9-3fd0-adae-4eece7218817 | -10.534 | -49.5471 | 2025-10-17 04:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 522f3bce-5fa9-3fdf-9ff7-880c3a061461 | 1.78534 | -55.92576 | 2025-10-17 04:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e3111d2-a9a5-3909-b6d4-14338f55d1ed | 1.04152 | -51.09568 | 2025-10-17 04:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0b95a994-5780-3b26-8627-4067362d8d93 | 1.82582 | -55.70828 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| f48f0ebd-41d6-3f31-b6a3-7aef3c003b1c | 1.78464 | -55.92117 | 2025-10-17 04:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 22609ad6-8647-38f1-92bc-172930184796 | 1.09673 | -51.11323 | 2025-10-17 04:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78dd9243-d971-3d56-a40f-3d92ef5193fa | 1.8104 | -55.96844 | 2025-10-17 04:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ccae5d8-e5a2-312f-a8e2-9029e12559a1 | 1.10193 | -51.14619 | 2025-10-17 04:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ebff629-40de-3014-b7f4-36919e3a6497 | 1.06154 | -51.22403 | 2025-10-17 04:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 97572109-c0a0-3d3b-a60f-d49fca92dc9c | 1.85465 | -55.67373 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7156b85b-78ed-326e-9cbd-4d1e4596db82 | 1.79235 | -55.91071 | 2025-10-17 04:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c829e5b7-2171-3db9-a9ca-4eb4d917c262 | 1.79653 | -55.72631 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| efe61515-a0a9-37ad-aaa2-21611e7d6ea5 | 1.73519 | -55.78857 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 628351a0-794b-3827-a1b5-504112948fe4 | 1.78801 | -55.91842 | 2025-10-17 04:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 256a459d-eedd-3127-b797-18baf1bc0bac | 1.78258 | -55.90747 | 2025-10-17 04:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01942769-58c2-35cc-9e16-4cc955c16efe | 1.79658 | -55.87741 | 2025-10-17 04:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 853724d0-7dd3-33e7-a79f-d5f200d3e11d | 1.78381 | -55.733 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2471752-6b18-3786-9002-cc776b65fee0 | 1.80515 | -55.96453 | 2025-10-17 04:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70c70261-71c5-3940-9ca9-676d6ec5e30f | 1.78957 | -55.89231 | 2025-10-17 04:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 315eec7d-e8d3-3bd4-adbf-b954d9f5c370 | 1.7885 | -55.91592 | 2025-10-17 04:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df6de6bc-11c3-3e48-a50c-73645f349759 | 1.05226 | -51.00819 | 2025-10-17 04:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35b12860-d332-38aa-bd1b-e832fcfe41b0 | 1.05812 | -51.22456 | 2025-10-17 04:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82c89063-83ac-3f67-b550-84add43f68cd | 1.7338 | -55.77967 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3414b7c-aa23-3ea1-9114-6e4c71fe407d | 1.77239 | -55.74838 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fd93d5d-16ae-373c-8a82-b23ec2e738da | 1.74963 | -55.76344 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 520945b9-5782-3fa9-b6c0-6d0ba2e558fb | 1.79539 | -55.96165 | 2025-10-17 04:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9e34a8a-bc82-3451-b923-cebcde9c788a | 0.87958 | -51.10876 | 2025-10-17 04:46:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a28a9774-a855-3753-9258-9e135f0e6983 | 1.78511 | -55.90014 | 2025-10-17 04:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72728e1e-6f94-31ad-a93b-f049bf79e05b | 1.83718 | -55.69312 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b224c02-6f78-3a4e-892d-e41b0140423b | 1.78057 | -55.90076 | 2025-10-17 04:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8158b5c-774f-3a0e-92e7-34116d8b5d0e | 1.7762 | -55.74328 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17789498-f50c-3406-9799-b475aa77760b | 1.73449 | -55.78411 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 98b0820e-cfa3-333a-bf29-4e1e8ef1f35b | 1.74515 | -55.76415 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c02c59a7-53b2-395f-9ea2-8570fd5072fd | 1.74893 | -55.759 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 02337358-17a4-36e3-9827-fb9ee7dd8c94 | -0.87989 | -48.08065 | 2025-10-17 04:46:00 | NPP-375D | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8cd3aa54-f370-35f3-8480-4cc350f15821 | 1.10072 | -51.11635 | 2025-10-17 04:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f6a4d222-917f-3093-bac6-43fcba82f33c | 0.88356 | -51.11188 | 2025-10-17 04:46:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3f1bd8d-fbab-3158-a299-090578fed055 | 4.38549 | -59.77962 | 2025-10-17 04:46:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f7ccc7b-46a5-3323-8a91-9167303e2d9f | 1.78131 | -55.90545 | 2025-10-17 04:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb99dd7c-7aeb-3f20-87a3-536a9560ea6c | 1.02951 | -51.10837 | 2025-10-17 04:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23b3dc74-98be-38ba-b0bb-a92c0e1c747f | 1.7914 | -55.72272 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30462e64-c49a-3f9d-8dec-f588adc63408 | 1.04241 | -51.21148 | 2025-10-17 04:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 020f9d9c-1b7a-3b97-8f36-5879bdf8f113 | 1.73828 | -55.77892 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 987623e6-fd30-3777-9443-621238b143d0 | 1.7245 | -55.80856 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6a8d8352-ef51-3898-94f0-11bcb80bc908 | 1.80446 | -55.96 | 2025-10-17 04:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00d113d9-0ad9-377a-8a54-d1f8c0d591d5 | 1.79525 | -55.96405 | 2025-10-17 04:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f88436d9-e8e6-3f2d-8ac6-a7126b8ba00f | 1.79993 | -55.96082 | 2025-10-17 04:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28369392-0bc2-375a-bf13-5ce65fac3525 | 1.02667 | -51.11254 | 2025-10-17 04:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59c42b8a-7068-3985-8623-1351d74504c8 | 1.02958 | -51.10876 | 2025-10-17 04:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53433414-8234-3034-a8de-080d02556380 | 1.31023 | -51.25033 | 2025-10-17 04:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 688febd8-37b1-306b-bed4-0b80254c3270 | 1.7808 | -55.92649 | 2025-10-17 04:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df263fec-a409-37ab-8acc-75d0f1789d74 | 1.78887 | -55.88766 | 2025-10-17 04:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2200c9d5-b764-3f87-a673-714b3aef919e | 0.32551 | -51.36227 | 2025-10-17 04:46:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README74.md)
