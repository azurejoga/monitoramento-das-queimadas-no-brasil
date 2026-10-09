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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db893471-4302-38a0-8f62-165f93ea78ed | -2.08133 | -46.57298 | 2026-10-09 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48436349-5540-3384-878a-eee00440b108 | -3.58615 | -54.68702 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d818e304-6df8-340a-896d-50aa04c227ab | -3.19984 | -50.83097 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 31c420c0-96bc-3908-9441-1000a155e1cd | -4.63118 | -50.95364 | 2026-10-09 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0cd43c28-03e3-3858-960c-e2c621144de0 | -3.16083 | -50.58929 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6dd1f9e7-385c-3750-ae8a-3a4b9b478490 | -3.931 | -56.03252 | 2026-10-09 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 46127ffa-378a-30d2-a519-4679a9475d2a | -3.10644 | -53.95916 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cc33e4e5-f38a-347f-b5af-979c049068be | -6.25007 | -45.32661 | 2026-10-09 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5995bcb5-37a4-3d18-ae0a-0c1921da1637 | -6.8872 | -45.89168 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 583d0f81-e80d-345b-87e1-8a149ccd6a95 | -3.16788 | -50.45013 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08cc75ea-9bb6-3745-9e53-ccb38745274b | -6.00298 | -40.97934 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d35eab09-8dce-337e-b4b4-c3bab0457317 | -3.00572 | -54.76855 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e836611e-1673-3d21-8ad3-d3a573f22713 | -3.42826 | -54.06749 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 780d4929-d533-39eb-8094-79fed6b10b54 | -3.36246 | -50.49105 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d1faa2bf-ab72-31b9-9c8c-f05d352f364b | -4.22322 | -46.93407 | 2026-10-09 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80add581-3fce-3de4-9c98-8e508811f25e | -7.40477 | -35.19446 | 2026-10-09 04:25:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 18fd14d2-9d1d-3d11-a783-144afd0d886b | -3.0783 | -54.29188 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2aabe632-1be4-355d-8bbb-40716cffd05c | -4.6306 | -50.95712 | 2026-10-09 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 281ef85c-f145-3707-aa89-8803a476cb4c | -5.9621 | -40.91176 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 05008885-80b6-3366-865c-33c3c4eb1bfd | -3.16279 | -54.7341 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a36d68f5-d0b4-35ff-a336-3f3bf9dc62ab | -3.08938 | -59.20081 | 2026-10-09 04:25:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a443237e-95f2-3d1f-a6b4-9ab7b968887e | -3.2776 | -53.83076 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 353474fd-0d42-3c22-bb5b-2ea8c33487c7 | 0.94913 | -50.20206 | 2026-10-09 04:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 363049d0-32a7-34b4-83b8-fe6f15f58b12 | -3.17575 | -50.45142 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea1d6d10-c976-3329-9208-07cf7ed71fd2 | -3.66026 | -54.27888 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d8a5efe-9475-3668-898a-ef06a3ec2465 | -5.69428 | -53.47511 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 71806335-685d-3f1d-81fb-07d5941427d4 | -3.07931 | -54.28565 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8493dbce-af52-337f-a0d8-6d2df660d216 | -3.20196 | -50.56159 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 15430c7d-05df-38c9-9f12-eaf1d1d9499f | -3.18813 | -49.24725 | 2026-10-09 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2d702619-7936-3953-ae7d-635a3d35921d | -4.54808 | -54.96796 | 2026-10-09 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d79ac628-541a-3e36-b1e9-b289bc0ada14 | -3.19009 | -58.65113 | 2026-10-09 04:25:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 02664aa4-291c-3784-93db-09bca78a0914 | -2.99335 | -53.8968 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 30fa1744-0490-31fc-a6c8-234e1ba1fd82 | -3.27013 | -51.07199 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eac3a6dd-cb40-3a60-98b8-c5e4c81e0cd9 | -5.34394 | -45.73241 | 2026-10-09 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3bbffcd-620c-3ad1-a019-75016b7f8f94 | -3.10303 | -54.28737 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4093b47-87d2-384a-864f-e60ff2feb026 | -1.15519 | -54.22091 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 991273a9-6a3c-3dea-a2fd-69179a564de4 | -7.18223 | -44.28464 | 2026-10-09 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c319aea9-2afc-307c-bef2-4032b275e05a | -3.87031 | -55.9954 | 2026-10-09 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0aa2b2ee-d18d-3ec3-8e3f-b3849a1f737d | -5.89923 | -43.7687 | 2026-10-09 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c89e0fd5-486b-3466-b0ed-6e496172abd4 | -5.67652 | -49.82569 | 2026-10-09 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5c7392a-2b51-3adc-ba8f-e1e3a85a798e | -3.88225 | -55.99355 | 2026-10-09 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a562b675-04c3-34b1-bbae-90c9ac091d83 | -3.06075 | -53.92508 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4a9d028-cfba-3340-ae68-802c563bf4ea | -2.83724 | -54.12588 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cffc3755-f43f-3335-a86e-b2d31afc9366 | -4.08175 | -44.12072 | 2026-10-09 04:25:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 613592c4-1243-3d84-b5a1-e43dd7f45f79 | -5.2634 | -47.911 | 2026-10-09 04:25:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 36671bc7-1a65-35a8-b094-c93fcff22ded | -5.41542 | -45.86006 | 2026-10-09 04:25:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce9955ce-f920-338e-99c6-c5a138306588 | -7.21964 | -44.16667 | 2026-10-09 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b201926-4056-3845-a77f-a789d66ce98c | -5.95418 | -40.93778 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9a7477f3-2e8b-3cfe-aa94-9dc265f90003 | -1.53222 | -54.54903 | 2026-10-09 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1b658f8-d8a2-338d-a64c-d19783eff4f3 | -6.16337 | -39.4464 | 2026-10-09 04:25:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 502865ff-328a-3c27-b60e-115d93de26fb | -3.09944 | -54.2775 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7af54812-9453-383c-9635-b8f2e8e3dd66 | 0.9276 | -50.2548 | 2026-10-09 04:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| feb4e3ea-ada5-3131-9b0c-2764a8bd9ac0 | -4.55165 | -54.97866 | 2026-10-09 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9367d6ce-6a50-3c3e-b842-c652ef5498e9 | -6.06506 | -44.10963 | 2026-10-09 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8540730e-1507-374d-aca1-48b49d28d64d | -3.32439 | -50.18203 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49c30cd2-0746-341c-ac16-69a26d179524 | -5.70601 | -53.4552 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 84a8acff-9f72-3578-9214-633dbbe4139b | -5.50021 | -42.85812 | 2026-10-09 04:25:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 33f3793a-32f9-37d1-a607-849cdaf33a50 | -3.34912 | -50.4735 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a7a0d50-d21a-314a-b8ed-69dc8fe10758 | -5.38194 | -44.2205 | 2026-10-09 04:25:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 20720a8b-b7aa-3edc-9376-83de13794fc2 | -2.50511 | -56.16573 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| af21682a-99a4-30ca-b2d2-26b3c7117fc3 | -5.69513 | -53.47002 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 60d96ef8-5e14-3407-8751-c650b0181fea | -1.48397 | -54.51974 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 28bbeebe-58ed-3fc7-bd34-61660b4c3dbf | -6.96366 | -45.28338 | 2026-10-09 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3d96c3f9-6958-38ff-ae0e-6a99bfe85a01 | 0.92564 | -50.2588 | 2026-10-09 04:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 317fd22c-32d0-3eef-84d2-98865b35d63b | -5.09505 | -46.21469 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5878828-1fca-389a-87fe-f55b1157b3bd | -1.42072 | -54.62102 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 855fe264-0a2f-33b4-85e2-9d7c26009755 | -4.11924 | -49.07732 | 2026-10-09 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e28bd43-24d9-3528-a7c0-eae210d4419d | -3.57574 | -54.68525 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 94a32bb8-a712-375c-9866-b25a3dee7634 | -3.09572 | -53.93066 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a4eab032-9b8f-32b6-84b1-c33823feaa17 | -5.70493 | -53.48888 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2434ca85-4256-35c6-8140-c6ddec6dd8b8 | -3.11347 | -51.03128 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ed57339-fe9b-34c2-a92e-d3c6e15d9718 | -2.48195 | -56.09096 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e4726358-9bad-3c21-be44-a1a973c62a1a | -6.92261 | -44.56018 | 2026-10-09 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| edc15f8f-e121-3e4e-bb39-44d11f1a1de1 | -3.17895 | -50.57809 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| dc535204-3972-3fd2-a50f-8a28905e3fb3 | -3.49128 | -50.4901 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1422cac6-fddd-3823-bc20-648982287bc5 | -3.73231 | -59.45823 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6cbbced3-97df-3667-9616-60f51f1820f8 | -5.10057 | -46.22258 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8ec983dc-b948-31d6-bc5d-79b4063309b4 | -2.69853 | -49.37289 | 2026-10-09 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e5d7bc5-d782-36c1-8d5f-ec0685d1242f | -5.70747 | -53.45303 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53e7cc6d-c1bf-3d43-b5b1-914ca32fb35b | -2.92302 | -54.1345 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7256f5b4-78c6-382d-a04c-791bd2416afc | -5.71199 | -53.48327 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3e496628-7d31-3b88-878c-dd14928adf85 | -3.57032 | -54.48624 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce44d410-555d-3fa9-8059-12e13bc9ee66 | -3.16621 | -58.62851 | 2026-10-09 04:25:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d67c65e0-d0d1-3458-bbd7-d4e97edc0dec | -4.07426 | -59.84662 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cd52484f-83be-39c2-a8a5-1e88021aad2f | -3.11491 | -54.16219 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 42da9ab4-c766-3f87-a6f5-284cacde5785 | -1.32778 | -52.44854 | 2026-10-09 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9091337-fde1-3cc4-871f-6b3c58804301 | -3.00925 | -54.0843 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3d076f4-5a02-3a2e-bcb3-0a04291f90d8 | -3.01336 | -54.09102 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d23f94e3-6121-3342-9184-60afc630d97a | -4.1097 | -54.62941 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e0cacacc-e2c7-3c54-a39e-b67d76dabaac | -6.16299 | -39.44957 | 2026-10-09 04:25:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| f3f23610-799e-35d8-b5e8-135b27278db4 | -3.09285 | -53.94812 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b85bafcc-0f3c-30b3-808d-4ed01eb6181a | -3.22005 | -54.29607 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cd3ec0ec-fba2-3647-8f6c-d680a939239c | -2.37894 | -48.22522 | 2026-10-09 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57443bd2-9126-3987-80b1-b3f88e14e544 | -3.2528 | -54.03895 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 455c9f89-ef06-386b-9bcd-4f2dfe53eca9 | -7.18816 | -42.00681 | 2026-10-09 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fa40433e-66f5-3f22-95c4-3da0a284385d | -3.18236 | -50.58215 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3ca10f3a-3b7b-39aa-ac8b-f37c0fee743e | -2.84839 | -54.12156 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 510b04ce-90cd-34a4-898a-7e5197a77a04 | -5.70735 | -53.48249 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| bf09d230-8203-3024-b96c-a427583379e5 | -6.82646 | -39.56215 | 2026-10-09 04:25:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 64612aed-59a8-388b-bbba-e4aba6c9b78b | -2.2235 | -53.69832 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README78.md)
