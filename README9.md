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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f68e6db-54e5-32fc-974f-ec2a9a92ebb8 | -17.627 | -56.3318 | 2024-10-12 00:26:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.8 |
| f91b20a8-64bd-3057-8b17-2e38f9e2ad7b | -17.6273 | -56.311 | 2024-10-12 00:26:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.1 |
| 9a862111-4417-3770-bd7c-f1d1ca95fcd5 | -17.6467 | -56.3292 | 2024-10-12 00:26:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 138.5 |
| 128047e0-cb32-3401-924a-040517a395d3 | -17.6471 | -56.3084 | 2024-10-12 00:26:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.0 |
| daebe684-d97f-3441-a7ab-6016de8df27b | -17.6675 | -56.2643 | 2024-10-12 00:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.2 |
| 4ad62564-97e0-344c-b63a-5280efe7ed5e | -17.6679 | -56.2435 | 2024-10-12 00:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.6 |
| ea8a94b0-fde8-3a4f-bcf5-4097be93b10e | -17.6873 | -56.2617 | 2024-10-12 00:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.8 |
| 255f6942-fb90-3464-8725-4e26bc3bf339 | -17.6876 | -56.2409 | 2024-10-12 00:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.4 |
| f3604606-4992-3f3c-a423-62a69151aea8 | -17.707 | -56.2592 | 2024-10-12 00:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.9 |
| c413271f-ddb7-31e7-92c7-0321a7d7ff47 | -17.7074 | -56.2383 | 2024-10-12 00:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.2 |
| 4ce76ce3-3354-3d8e-8fc6-3f7deb891a00 | -17.964 | -57.3843 | 2024-10-12 00:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.3 |
| f74b03fc-8acf-36ab-ba60-0e792e501a1a | -17.9643 | -57.3637 | 2024-10-12 00:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.8 |
| 09231ea3-ab3e-374f-964f-697451132e36 | -17.9837 | -57.3819 | 2024-10-12 00:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.8 |
| 39123f2d-4fec-3bb3-b44f-9cca7b2ac11c | -17.9841 | -57.3612 | 2024-10-12 00:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.7 |
| 3449dd72-ab76-388e-97cb-7515a9bc8a7b | 1.9028 | -50.8475 | 2024-10-12 00:26:52 | METOP-B | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 8bf2ca4f-76f8-3d4d-bee2-fa251aa6237a | -1.6169 | -48.0269 | 2024-10-12 00:35:15 | GOES-16 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 5f25ba4f-75fb-3980-a4b8-1dd3660c192d | -2.77 | -51.3829 | 2024-10-12 00:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 265b00e6-db65-3509-92a0-7da8c27e81ab | -2.7701 | -51.3622 | 2024-10-12 00:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| b361d07a-94ed-307b-a19a-2964a1194ef3 | -2.7799 | -54.0133 | 2024-10-12 00:35:22 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 14111ea9-248d-38c5-bad9-3ff8291da279 | -2.7884 | -51.3825 | 2024-10-12 00:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 7bd19db3-f965-328c-bff9-6c57e8041116 | -2.7885 | -51.3618 | 2024-10-12 00:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 1ac60e27-2ab8-3dc6-96ce-1b46ca1f6ed3 | -2.7983 | -54.0129 | 2024-10-12 00:35:22 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| edb4ce59-10f2-317c-a69a-5494d5c91ff3 | -2.8611 | -51.6699 | 2024-10-12 00:35:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| b9034d76-da03-382e-bcae-f3816aa4d247 | -2.8795 | -51.6695 | 2024-10-12 00:35:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 1b527927-63e8-3e06-92ae-0c8d4c1a8a7c | -3.0311 | -50.5642 | 2024-10-12 00:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| ddc21221-9872-3928-9074-b637a0a5a575 | -3.1427 | -50.3514 | 2024-10-12 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| d3c18741-7ec9-3cda-879b-af1791a9f8bd | -3.1611 | -50.3508 | 2024-10-12 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 24e6dd5e-321e-30b7-b885-e61f2e831edf | -3.2136 | -46.7843 | 2024-10-12 00:35:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 7721d18d-7859-30c6-a804-bf4040b65468 | -3.6978 | -50.1225 | 2024-10-12 00:35:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 138.1 |
| 8ddbb271-6cbb-3559-9dd6-23b32ab0657c | -3.6979 | -50.1015 | 2024-10-12 00:35:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| d1280f8d-0019-3904-bdc4-f48a83e80274 | -3.7163 | -50.1219 | 2024-10-12 00:35:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 2af3d4e9-840d-39e3-b9c1-b973a44c6af5 | -3.7844 | -51.3312 | 2024-10-12 00:35:28 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| cc608b57-1beb-38b9-884d-b5686c545686 | -3.7845 | -51.3104 | 2024-10-12 00:35:28 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 7492bd16-0d18-3f8d-8fc2-02e3893c7fe8 | -3.8167 | -52.3403 | 2024-10-12 00:35:28 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 8b4cccdd-e234-3d21-8c66-0d2238c2a637 | -3.9394 | -46.445 | 2024-10-12 00:35:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 104.7 |
| bc2bb455-6a4d-3c90-8367-ed88fd095218 | -3.9396 | -46.4229 | 2024-10-12 00:35:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 762f2ca5-2f61-3b14-9d93-88816cadcb4b | -4.0062 | -60.3869 | 2024-10-12 00:35:29 | GOES-16 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 620c2de3-df40-3a89-8508-a0313d5e4e6f | -4.1148 | -48.2515 | 2024-10-12 00:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 9a484611-0f55-3d96-9855-9d586251b044 | -4.2665 | -50.9594 | 2024-10-12 00:35:31 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 104.2 |
| db06b367-e9d1-3523-abb4-305702316321 | -4.3782 | -50.8087 | 2024-10-12 00:35:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| e90490a8-e860-3ba3-859d-c816bf0b04a1 | -4.7188 | -60.7882 | 2024-10-12 00:35:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 36f4b72d-49ba-3bc5-b172-36a41e14fb3f | -4.7189 | -60.7692 | 2024-10-12 00:35:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| e8cb8dba-3120-3548-a9cc-a944b0034629 | -4.7371 | -60.7877 | 2024-10-12 00:35:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| aa90a608-76b6-3fe5-9236-f856f8c9f222 | -6.0789 | -44.6504 | 2024-10-12 00:35:41 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 6a394a95-5a83-354e-8bc5-b3c5b3408f10 | -6.0791 | -44.6276 | 2024-10-12 00:35:41 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 187da2b1-9be3-3a80-81af-da76b52c28ac | -6.8591 | -59.0705 | 2024-10-12 00:35:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| e85b3cbb-195d-36f0-8060-cd62c679e1dc | -8.2325 | -61.1823 | 2024-10-12 00:35:54 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| e69c8e16-12e3-3a71-ae5c-e0099d247849 | -8.4231 | -55.4704 | 2024-10-12 00:35:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 1746a1d6-d4a5-365a-9911-6d969e7c79cc | -8.9042 | -63.5454 | 2024-10-12 00:35:57 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 7867c465-2533-32fc-9f61-d6e9af3db762 | -8.9376 | -64.2406 | 2024-10-12 00:35:58 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 099a831a-7e3a-3f8e-bed7-dc8386e93153 | -8.9667 | -62.3506 | 2024-10-12 00:35:58 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 2a6f3233-f14a-33ed-99fa-6698ec533195 | -9.5687 | -64.1983 | 2024-10-12 00:36:01 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 003d11b3-b98d-3009-b5ce-1c1652645327 | -9.5878 | -64.1034 | 2024-10-12 00:36:01 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 13db0f72-85af-37be-9fc4-a6e95f3d5c2d | -9.6594 | -56.9635 | 2024-10-12 00:36:01 | GOES-16 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| de4699ae-ef71-3da5-b33c-53e2ce9643d5 | -10.3708 | -61.232 | 2024-10-12 00:36:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 53a28a3a-b293-34b2-a18a-bcbd40d8bcf7 | -10.3895 | -61.231 | 2024-10-12 00:36:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| e85ac671-9706-3963-8648-9cb4ba745ddc | -10.3897 | -61.2118 | 2024-10-12 00:36:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 46e56e31-e715-3608-b018-94490ded26eb | -10.3898 | -61.1925 | 2024-10-12 00:36:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 8f6691c1-a383-3ddb-966c-219c1e9b4679 | -10.4079 | -61.2685 | 2024-10-12 00:36:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 48d13d5e-45d8-3618-9a47-281f74dfb338 | -10.8398 | -44.4365 | 2024-10-12 00:36:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| a3fed4c8-79c3-3187-b849-9690b9a0f317 | -10.9506 | -44.653 | 2024-10-12 00:36:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 85f3caf4-a66f-3f89-bfdf-63e78d31bbc0 | -11.2719 | -50.9441 | 2024-10-12 00:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 63.4 |
| df4054cd-9197-3389-b69a-3def4e847ae6 | -11.2912 | -50.9208 | 2024-10-12 00:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 97b10179-e9a6-3acb-9525-d1108899ea3d | -11.2915 | -50.8995 | 2024-10-12 00:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 35c23297-d99d-3833-b474-a31274cd4329 | -11.3102 | -50.9187 | 2024-10-12 00:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 231.6 |
| c7568c8e-6f05-3074-b76b-9b3ad3c7154c | -11.3105 | -50.8974 | 2024-10-12 00:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 190.3 |
| 8bd22d99-be7a-3da7-b46d-dc5034cebad0 | -11.3292 | -50.9167 | 2024-10-12 00:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 105.9 |
| db71a773-d3e0-3068-a039-9b5a863731ba | -11.3295 | -50.8954 | 2024-10-12 00:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 3eb0573a-c4ad-3c0e-a207-f59a4ef8bbae | -11.2761 | -60.5038 | 2024-10-12 00:36:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 09bbc20a-3fd7-3dde-a276-2aee34712459 | -11.2763 | -60.4844 | 2024-10-12 00:36:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 71.7 |
| c1a61177-9a79-3b29-936e-b7d9ebb2a6db | -11.8188 | -58.8459 | 2024-10-12 00:36:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 51.6 |
| cb170ac8-e391-3a57-9503-d17d54fc68b9 | -11.8375 | -58.8642 | 2024-10-12 00:36:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 9ff6e78c-9209-30a8-a1df-fb78598603f5 | -11.8377 | -58.8445 | 2024-10-12 00:36:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 169.8 |
| d08ee6fa-cf3f-3b6b-bbab-d8522c7cd2e2 | -12.6034 | -48.6209 | 2024-10-12 00:36:17 | GOES-16 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 7120c565-7e6e-30bf-9f33-c650193d3f40 | -12.6038 | -48.5988 | 2024-10-12 00:36:17 | GOES-16 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 9543e04f-5194-3a0d-9686-c2dee541a43f | -12.7871 | -44.8639 | 2024-10-12 00:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 351.7 |
| 7b5b2915-2318-3540-a9ed-f3dec8e7ebbc | -12.7875 | -44.8406 | 2024-10-12 00:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 240.4 |
| 99cad788-3fb5-3577-a154-91d83ecc20bf | -12.8064 | -44.8608 | 2024-10-12 00:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 168.5 |
| de3091e7-ab85-394f-ac3a-31298d423a6f | -12.8069 | -44.8375 | 2024-10-12 00:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 3a9ed102-a6e8-3674-9515-a7502f6ac840 | -13.213 | -51.1216 | 2024-10-12 00:36:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| b599f266-bbe1-3986-8e68-9f2f5d784bc6 | -13.2322 | -51.1192 | 2024-10-12 00:36:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 102.6 |
| b760ab1a-4254-30bb-94aa-6ebeda2771b0 | -13.2325 | -51.0978 | 2024-10-12 00:36:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.7 |
| a2e73552-9cfd-350a-90b7-7393f4a075be | -15.0524 | -45.073 | 2024-10-12 00:36:30 | GOES-16 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 145.3 |
| f7502e45-1008-3cc4-9f6c-e1ce34fbcf07 | -15.0529 | -45.0495 | 2024-10-12 00:36:30 | GOES-16 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 38bf492d-6082-37b2-b9aa-2e2d45037350 | -15.072 | -45.0693 | 2024-10-12 00:36:30 | GOES-16 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 68.2 |
| ccf7df34-7d96-3288-828d-3ecfe8f2a977 | -16.9802 | -57.4609 | 2024-10-12 00:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.7 |
| 0e956059-9353-3c9f-b64b-42ff283b48a5 | -16.9805 | -57.4404 | 2024-10-12 00:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 119.0 |
| 8e218949-1648-3650-bb0c-bb0a34b4fa9a | -16.9998 | -57.4586 | 2024-10-12 00:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.6 |
| d16080e5-bfa2-3a29-8f15-bc062ce03b23 | -17.0001 | -57.4381 | 2024-10-12 00:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.6 |
| ca36925c-aa90-3a02-86da-94dcbe7a52e4 | -17.1758 | -57.479 | 2024-10-12 00:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.5 |
| 97ecab97-725a-3e43-afff-7c12ad8d176b | -17.1761 | -57.4585 | 2024-10-12 00:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 120.5 |
| 860eee9e-cb3d-3100-9af7-ead687ce2e00 | -17.627 | -56.3318 | 2024-10-12 00:36:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 131.5 |
| 29094378-2074-3bcf-b8ad-235fc3000497 | -17.6273 | -56.311 | 2024-10-12 00:36:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.5 |
| 6bba09ff-c543-3c0d-821d-6d2114a628b8 | -17.6467 | -56.3292 | 2024-10-12 00:36:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 158.1 |
| 8aadad63-241d-3d73-b19a-659a8fb5a004 | -17.6471 | -56.3084 | 2024-10-12 00:36:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.2 |
| 7c01f435-e4e7-34f1-a972-5a5dd63847e9 | -17.6675 | -56.2643 | 2024-10-12 00:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.9 |
| 4e0970ae-d095-366a-b471-fec3f4dbf23f | -17.6679 | -56.2435 | 2024-10-12 00:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.6 |
| 3bdac431-0025-37fe-9da3-caeb138cf375 | -17.7074 | -56.2383 | 2024-10-12 00:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.4 |
| fd5a2da8-23e8-32ee-804e-749af22cd4ab | -17.964 | -57.3843 | 2024-10-12 00:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.9 |
| 780efdff-8afb-3e6c-a992-edc34c301b55 | -17.9643 | -57.3637 | 2024-10-12 00:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.1 |


[Clique aqui para ver as próximas entradas](README10.md)
