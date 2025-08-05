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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8bae3055-0b05-364b-bc9b-c78904d4b1d7 | -17.205 | -44.8454 | 2025-08-05 01:50:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 1a2cc371-9fd1-3868-998d-5ed2e68e6379 | -9.3985 | -45.5156 | 2025-08-05 01:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 065382cf-071b-35df-b5dd-2b45a67d43d0 | -8.9412 | -60.5559 | 2025-08-05 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.3 |
| ab37dad1-9e30-321c-906d-dee900051554 | -8.9412 | -60.5559 | 2025-08-05 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.0 |
| a11d52bb-4f2b-3748-a495-41e9bc7b46b4 | -8.9227 | -60.5568 | 2025-08-05 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 139.1 |
| 23fb5b4d-ae33-3813-a5ab-8ee971e65159 | -8.9228 | -60.5376 | 2025-08-05 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.4 |
| ff76a11d-e428-31ce-be92-a5e7e7221951 | -7.9943 | -43.1298 | 2025-08-05 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.7 |
| bf635186-6606-3e39-b659-0b12ef085e24 | -8.9478 | -46.7354 | 2025-08-05 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| eb562217-3857-3540-95ac-450711844c93 | -17.225 | -44.841 | 2025-08-05 02:00:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 2fb1092c-c55c-384a-a3a0-c6f2619d4e37 | -8.0129 | -43.1513 | 2025-08-05 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 52.5 |
| 37bd67a0-7dc8-3e49-b30e-75ec72f6dc1e | -17.205 | -44.8454 | 2025-08-05 02:00:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 76.7 |
| a87923de-d571-322d-966e-59f65f1a0864 | -17.2056 | -44.8214 | 2025-08-05 02:00:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 134.0 |
| d0e41e91-3c04-3263-bb81-76599ece3f8f | -10.3311 | -47.8256 | 2025-08-05 02:00:00 | GOES-19 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 9f2a8077-fa04-372f-8e69-13b62d9004b8 | -7.994 | -43.1534 | 2025-08-05 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 132.0 |
| 72f36ef2-ed60-3528-bb79-208ed78efde3 | -8.0132 | -43.1278 | 2025-08-05 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 45.2 |
| e6e0dae7-5520-3f9f-b800-526518865842 | -8.9224 | -60.5953 | 2025-08-05 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 81989290-9da7-3a7c-9da7-538fbbab545a | -8.9225 | -60.576 | 2025-08-05 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 7b2cb3bc-e9b5-3d52-9ed2-1d57e0321566 | -9.3985 | -45.5156 | 2025-08-05 02:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 0861700c-dadd-349a-ab68-670633e602ef | -17.2256 | -44.817 | 2025-08-05 02:00:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 147.0 |
| 5c6eed05-e5eb-36c1-bf81-5e31e4ec3623 | -9.3989 | -45.4928 | 2025-08-05 02:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 1a510371-1bcb-3561-9022-dfaf7eb20a9b | -13.0614 | -56.925301 | 2025-08-05 02:07:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f8899c12-29ed-3e6c-83d0-b86f67ca9c08 | -13.0531 | -56.895802 | 2025-08-05 02:07:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f8eaa4bd-9efd-3e67-8209-36b41f6a4fa9 | -8.8903 | -60.5634 | 2025-08-05 02:07:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9def2034-e06a-3415-8c53-4c1843ee9302 | -13.0519 | -56.928101 | 2025-08-05 02:07:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 08bf8783-6e48-34fc-ae61-1583bfe29895 | -8.9 | -60.560902 | 2025-08-05 02:07:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 49796370-6ffe-3eea-bff7-dd79def7f140 | -13.0423 | -56.930901 | 2025-08-05 02:07:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5b25631e-311a-323c-bf3b-a707a9ec2c3c | -8.8953 | -60.583199 | 2025-08-05 02:07:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1f855cfd-7632-3b03-9c1b-b485d9a643d8 | -13.0246 | -56.904202 | 2025-08-05 02:07:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1802c28a-a78d-3dfa-99ce-440bb3407cfd | -13.0436 | -56.898602 | 2025-08-05 02:07:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 813dc2c7-865d-323e-9dfc-ba10bd83a214 | -13.0341 | -56.901402 | 2025-08-05 02:07:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d5b9d1a4-6808-34df-a8c6-6d2c6b294894 | -8.9228 | -60.5376 | 2025-08-05 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 7b4c7aec-734d-3f7c-a4d3-f3f7094d4949 | -17.2056 | -44.8214 | 2025-08-05 02:10:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 8afe3979-5e24-377d-a4b4-9353b91c7181 | -8.9227 | -60.5568 | 2025-08-05 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 128.0 |
| 4dafe4f1-d4a4-381e-b240-b8cc8244c826 | -17.225 | -44.841 | 2025-08-05 02:10:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 77.9 |
| f9478207-3247-3051-968b-ae077baefb37 | -17.2256 | -44.817 | 2025-08-05 02:10:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 23b3501d-bc3b-3187-a03c-8c34fae6ebaa | -11.9207 | -44.9525 | 2025-08-05 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 9102030b-85a4-3fe7-93b0-4f0391f10f99 | -7.9943 | -43.1298 | 2025-08-05 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.7 |
| 800b83a2-347e-3ee9-b4c6-0dac0d760c8f | -8.9224 | -60.5953 | 2025-08-05 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 17e8d125-f2ff-3776-bd9a-df01c0b6eb5e | -8.9225 | -60.576 | 2025-08-05 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.8 |
| c56e1631-148a-362d-9c96-0092242c4973 | -7.994 | -43.1534 | 2025-08-05 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 111.6 |
| d5321a59-c01d-3c3a-8745-ebca52f69c87 | -8.9478 | -46.7354 | 2025-08-05 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 01ff33a6-cad4-37e4-8fa1-1f87456004e1 | -8.9412 | -60.5559 | 2025-08-05 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 0c1606d6-efed-3b86-b010-56860ca08d83 | -8.9414 | -60.5367 | 2025-08-05 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| ef6bdfac-77bf-3216-98e1-2b6e35da6539 | -9.3985 | -45.5156 | 2025-08-05 02:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 4eeb1743-1f46-3d7e-8dc8-7edc841a8cec | -7.9943 | -43.1298 | 2025-08-05 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 38.6 |
| 580ea931-b6e5-33c8-b264-ba3ad679a66d | -13.0728 | -56.8729 | 2025-08-05 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| b18f22b0-8735-3866-a4cc-9f346c445afd | -10.3311 | -47.8256 | 2025-08-05 02:20:00 | GOES-19 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 409fc93b-489b-31f3-8cca-833e7e68083a | -13.0914 | -56.9114 | 2025-08-05 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 107.5 |
| dbeb9ed8-632f-3dbb-88fd-0f6b049d21af | -8.9478 | -46.7354 | 2025-08-05 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 4875971f-e593-3ef0-8d81-79d7926b8382 | -17.2056 | -44.8214 | 2025-08-05 02:20:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 125.3 |
| bfc06bc1-e4cd-3184-8a01-95e7ad4c50ed | -13.0723 | -56.9131 | 2025-08-05 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 153.2 |
| aa2b3998-98fd-30ed-aed6-52b225840ec7 | -17.205 | -44.8454 | 2025-08-05 02:20:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 08805e78-f289-3ada-8446-89ab33187a96 | -9.3989 | -45.4928 | 2025-08-05 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 0f67938a-ed6e-32fa-891c-9f9c643047bf | -13.0538 | -56.8746 | 2025-08-05 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 4bc6c2e9-cbe7-3eff-9005-cbf07d96c90c | -17.225 | -44.841 | 2025-08-05 02:20:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 8b1b414d-24b2-36bd-9f0d-772f563da812 | -7.994 | -43.1534 | 2025-08-05 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.5 |
| 1347451b-e426-3bc6-8a9c-04ff074db9ee | -13.0726 | -56.893 | 2025-08-05 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| c60b294a-f638-3ef5-905d-b120805ab10d | -11.9207 | -44.9525 | 2025-08-05 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 105.5 |
| dc9c5b21-00d4-3b32-a01a-e2990e5af9a1 | -13.0916 | -56.8913 | 2025-08-05 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| c6f19cc1-7a29-3f4f-b8e9-5658e11b8da8 | -17.2256 | -44.817 | 2025-08-05 02:20:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 115.8 |
| eaa8dcb9-0521-351f-a880-e9bac3b9dfb2 | -17.2256 | -44.817 | 2025-08-05 02:30:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 158.6 |
| 73ccf557-d267-3c0b-a053-b4e38906d551 | -13.0723 | -56.9131 | 2025-08-05 02:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 124.1 |
| a3fc3c24-38d0-325c-8fa2-a7cfe05bae40 | -7.994 | -43.1534 | 2025-08-05 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 39.7 |
| 01870640-ea76-3f0d-86d8-dc20cc2ae8e2 | -17.205 | -44.8454 | 2025-08-05 02:30:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 70.1 |
| c83b9e0f-04fa-35d9-9fa0-504bd45e8f42 | -8.9224 | -60.5953 | 2025-08-05 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 6927b65d-9d7b-318c-bc37-65e07a5a1b46 | -11.9207 | -44.9525 | 2025-08-05 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 704.4 |
| 827a0b5c-3abf-37f4-9847-c1ff5326096d | -11.9399 | -44.9497 | 2025-08-05 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| d746ca5e-6c42-3867-ab0e-2137e7863d89 | -13.0914 | -56.9114 | 2025-08-05 02:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 91.0 |
| b96c114b-70b1-3923-b604-d9669ef84aa9 | -8.9225 | -60.576 | 2025-08-05 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 153.5 |
| 456cccd9-b01a-3088-a3f9-4cffe7119c26 | -13.0728 | -56.8729 | 2025-08-05 02:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 6f7cc435-ea93-35e9-95e6-41e2a15bdce5 | -8.9478 | -46.7354 | 2025-08-05 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 06e68b70-0a37-3faa-b42c-0aa3d3ef8374 | -8.9228 | -60.5376 | 2025-08-05 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 143.2 |
| 1d1d4a6d-3b49-38f1-bae9-a3bd8b675ee6 | -8.9412 | -60.5559 | 2025-08-05 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 99d28705-c78e-3f1c-a795-9999209ff155 | -17.2056 | -44.8214 | 2025-08-05 02:30:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 116.0 |
| fa435fba-2b88-3a99-89ed-409c5af3bea4 | -11.9203 | -44.9757 | 2025-08-05 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 233.9 |
| ffb20337-40c8-3225-b5fc-3da0c7f17c35 | -13.0538 | -56.8746 | 2025-08-05 02:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| f937cc63-09eb-390e-8cc3-58698bd5dbe1 | -11.9211 | -44.9293 | 2025-08-05 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 179.9 |
| c0c6b103-e757-3dce-90ee-43d597ffa8e4 | -13.0916 | -56.8913 | 2025-08-05 02:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 6fefe7cc-14a0-3810-a83d-4e84fa690b6c | -13.0726 | -56.893 | 2025-08-05 02:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 7bad466b-803c-3e89-962e-504d3854a195 | -8.9227 | -60.5568 | 2025-08-05 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 235.5 |
| fd173ec3-0cbe-302f-9a67-fdbc52460246 | -17.225 | -44.841 | 2025-08-05 02:30:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 03af2796-d840-3262-ba31-00f39e518bb8 | -11.9015 | -44.9554 | 2025-08-05 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 47367461-3882-3b2a-a033-9a4435f7c6c0 | -8.9411 | -60.5751 | 2025-08-05 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.5 |
| c6c37f63-7d43-313d-ba6d-d49b9cc88433 | -17.205 | -44.8454 | 2025-08-05 02:40:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 96.7 |
| ad09a28e-5eca-3b38-9fca-011e433d1a0d | -11.9015 | -44.9554 | 2025-08-05 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 367eabd8-5503-3037-93a2-ba0768ada928 | -13.0726 | -56.893 | 2025-08-05 02:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| c9dde6f5-437b-31fe-acc4-de7f6b464b7a | -13.0538 | -56.8746 | 2025-08-05 02:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 47d06fdc-9102-3245-8c82-dc8fe5aface4 | -17.225 | -44.841 | 2025-08-05 02:40:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 432340f7-0ddb-3681-98e9-a8de55fc7b26 | -11.9207 | -44.9525 | 2025-08-05 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 253.0 |
| 1ee6a580-18ab-3d6f-8c1f-b13675bdb8ea | -11.9399 | -44.9497 | 2025-08-05 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| e2ca3e51-0a00-3f2e-aa19-b686ca5652b9 | -8.9478 | -46.7354 | 2025-08-05 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 001fc458-9811-3b62-9044-6273b367e0ac | -10.3311 | -47.8256 | 2025-08-05 02:40:00 | GOES-19 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 46.7 |
| bd5fbb6a-f6de-3275-b7d2-8ba4ca61343a | -11.9203 | -44.9757 | 2025-08-05 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 127.7 |
| a70e743d-06b4-376c-9921-3e093cc3b6ea | -13.0916 | -56.8913 | 2025-08-05 02:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| e68987e5-612c-3cb8-ba57-e78e8990c1b2 | -13.0723 | -56.9131 | 2025-08-05 02:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 4bfc7040-1847-3953-92d6-da90448fac9f | -17.2256 | -44.817 | 2025-08-05 02:40:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 137.4 |
| b7f3040d-2c31-38a3-8b81-73bf23f78032 | -11.9211 | -44.9293 | 2025-08-05 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 7eea665f-8efb-3509-ae21-fdecd336b52b | -17.2056 | -44.8214 | 2025-08-05 02:40:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 152.7 |
| 290fe662-b0f4-3ed3-8b7d-03564da25272 | -13.0914 | -56.9114 | 2025-08-05 02:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 04375d9e-5992-384c-b32c-12b27933cfef | -13.0728 | -56.8729 | 2025-08-05 02:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |


[Clique aqui para ver as próximas entradas](README6.md)
