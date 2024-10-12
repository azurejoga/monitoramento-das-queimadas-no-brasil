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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ce0488c-8a53-3a65-ac09-1f33fc63b254 | -2.65281 | -53.35369 | 2024-10-12 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6bd8263e-5a6d-39f7-970f-7a7d3a64b90b | -2.8319 | -49.5385 | 2024-10-12 04:05:22 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 5d542357-66f8-30fa-b708-092f4259619f | -2.8254 | -51.3401 | 2024-10-12 04:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 1032786e-0eb7-37fd-87fe-51104c8c72a6 | -2.8253 | -51.3608 | 2024-10-12 04:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 42f4e486-d307-3d58-aa35-49e8af2cc016 | -2.7885 | -51.3618 | 2024-10-12 04:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 0389269e-7a52-34ab-837e-2ff1562600ae | -2.7884 | -51.3825 | 2024-10-12 04:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| ca85f067-f300-3761-9c71-4335fb239c8c | -2.7701 | -51.3622 | 2024-10-12 04:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 01ef8d81-e45c-3e32-9965-a4a7e89423ce | -2.77 | -51.3829 | 2024-10-12 04:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 01977e33-204a-3fbd-92ff-7765f2006f73 | -3.6979 | -50.1015 | 2024-10-12 04:05:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 9ad03461-3c52-376d-8266-2596b572eecd | -3.6978 | -50.1225 | 2024-10-12 04:05:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| f72f87de-a8f2-3943-b30b-0f9e57989b03 | -3.7845 | -51.3104 | 2024-10-12 04:05:28 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| eaff9e86-9ecc-3eb7-97b5-02279d5bb832 | -3.7844 | -51.3312 | 2024-10-12 04:05:28 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| a8bdf8ca-f3c7-3053-bd4c-c38610bd8d1e | -3.9396 | -46.4229 | 2024-10-12 04:05:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 3f815786-9cd3-301f-b274-e4e959179d73 | -3.9394 | -46.445 | 2024-10-12 04:05:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 07995625-fef9-367c-bcca-d9ddb4dcf722 | -4.4538 | -44.5763 | 2024-10-12 04:05:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| c6fece10-4218-3900-84b5-b6da7cdb0399 | -4.5859 | -47.0968 | 2024-10-12 04:05:32 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 74.5 |
| f4548620-1fed-361c-a9b9-8b1edca47cfa | -4.5673 | -47.0977 | 2024-10-12 04:05:32 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 44.4 |
| bd1d4888-0753-309f-96c4-92e01bede472 | -5.2486 | -48.0424 | 2024-10-12 04:05:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 405bfbe9-b6e8-3501-946d-b71f646240cf | -5.3997 | -45.3574 | 2024-10-12 04:05:37 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 0fff657c-1822-37a6-95b5-5b5ad9ff2d6c | -5.381 | -45.3586 | 2024-10-12 04:05:37 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 4df67223-ba41-3880-b19c-3d5a20572bb3 | -6.747 | -59.3259 | 2024-10-12 04:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 4098d1e1-3aa4-333c-ad73-d7273ea1162b | -6.7469 | -59.3452 | 2024-10-12 04:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 029f712e-a462-3967-a4b0-6cd8f38ce360 | -7.8901 | -54.7004 | 2024-10-12 04:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 6558790b-6470-3f48-9cf8-aaa69b8202be | -7.8717 | -54.6814 | 2024-10-12 04:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 81d442cc-3eba-3f48-a70e-77839efea8ec | -7.8715 | -54.7016 | 2024-10-12 04:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 129.6 |
| 6f563bde-cfd9-356a-b950-d3f6c66d5a15 | -7.8713 | -54.7217 | 2024-10-12 04:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 993efba6-a8c9-307a-bb38-74edd28e8104 | -7.8529 | -54.7027 | 2024-10-12 04:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 731a9cfc-ccbc-32aa-9173-4b6bb8c6164a | -8.4231 | -55.4704 | 2024-10-12 04:05:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 77b77443-0008-3a96-a51c-58910de110a4 | -7.09912 | -35.86306 | 2024-10-12 04:06:00 | NOAA-20 | SÃO SEBASTIÃO DE LAGOA DE ROÇA | PARAÍBA | Brasil | 2515104 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 75a885f3-0bcb-3dea-8242-ce44ff999911 | -7.09853 | -35.86707 | 2024-10-12 04:06:00 | NOAA-20 | SÃO SEBASTIÃO DE LAGOA DE ROÇA | PARAÍBA | Brasil | 2515104 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 44c09217-e78a-3379-b8d5-1fb7602fce72 | -6.87434 | -38.56614 | 2024-10-12 04:06:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2e3a4045-821a-34e2-9c67-b16f32047f3f | -7.13957 | -40.0723 | 2024-10-12 04:06:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 910cb0b5-9c55-30bb-a22e-d6c16a494bfb | -7.13831 | -40.07239 | 2024-10-12 04:06:00 | NOAA-20 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 92f328d2-4628-3a73-a13a-d818ccbd268b | -7.13775 | -40.076 | 2024-10-12 04:06:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 66b9907c-b030-3ec3-8406-d13d07a613a6 | -7.13494 | -40.07185 | 2024-10-12 04:06:00 | NOAA-20 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 524b7a28-ff60-3cad-9862-a00385ade413 | -7.13438 | -40.07546 | 2024-10-12 04:06:00 | NOAA-20 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dd2f08f4-1816-35f3-86af-10207141de2d | -7.09027 | -39.93431 | 2024-10-12 04:06:00 | NOAA-20 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 3af3fa7a-b668-356c-99e4-361d10bdce7e | -7.08744 | -39.93011 | 2024-10-12 04:06:00 | NOAA-20 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e185dfe8-1ddd-3a52-ae8c-4f51d4021c3c | -7.08688 | -39.93377 | 2024-10-12 04:06:00 | NOAA-20 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| cbb97e81-57cf-3054-87e9-fb7245ab30ad | -7.0633 | -39.71976 | 2024-10-12 04:06:00 | NOAA-20 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8acd00b4-d130-33b3-bce7-57fa853ca8f2 | -6.97128 | -39.79667 | 2024-10-12 04:06:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7a890ac7-df50-3461-92a2-1bd0d4e1fc4e | -6.96531 | -40.17549 | 2024-10-12 04:06:00 | NOAA-20 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fc25c7d1-49ec-31c2-843e-249f1363e4bb | -9.25326 | -44.56254 | 2024-10-12 04:06:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 66afd054-ce5c-3f05-9bc0-8001a7eacfc8 | -9.25178 | -44.56318 | 2024-10-12 04:06:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d996ad21-9995-39db-9632-0309caef5f35 | -7.21473 | -44.14204 | 2024-10-12 04:06:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31c10853-8615-3e41-936d-21570f334cbb | -7.15262 | -43.87607 | 2024-10-12 04:06:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| becc328d-48ef-3ca6-a3be-f1d8894aff50 | -7.15077 | -43.88752 | 2024-10-12 04:06:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 801e97d4-9672-3d9e-86c8-42afbd02f343 | -6.63669 | -43.85834 | 2024-10-12 04:06:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3f0a380c-0bd0-36a6-ac7f-168cec2bd1ad | -6.63607 | -43.86216 | 2024-10-12 04:06:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 298f0c71-0d0f-3120-9f9b-084348ce543a | -6.6326 | -43.8616 | 2024-10-12 04:06:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6eab5ce0-d0c4-37b3-8f33-93d49bcf5d89 | -6.48573 | -43.8778 | 2024-10-12 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c6fae0e9-4a34-3f87-b650-1de06ce0f24e | -8.07133 | -34.9784 | 2024-10-12 04:06:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bb6529f3-32a3-3f8b-a9e7-f79997a23dfd | -9.42184 | -35.96476 | 2024-10-12 04:06:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4986632b-3906-38a1-b9a6-70b290ed866e | -6.23265 | -43.12021 | 2024-10-12 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b33e3478-bef2-3b91-9633-1917cd385f0e | -6.17229 | -43.45152 | 2024-10-12 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24cad941-0fc3-3875-b691-5f608de98ff6 | -6.17198 | -43.45095 | 2024-10-12 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 764146f3-6aa1-3d48-874a-517cb4f6073a | -5.93369 | -43.34197 | 2024-10-12 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8395c49-3fea-31a8-b0e4-8328a6ff66d4 | -6.44218 | -38.81824 | 2024-10-12 04:06:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1e43637b-99c6-3f08-b98b-a749815ff2b0 | -9.84208 | -39.59743 | 2024-10-12 04:06:00 | NOAA-20 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 13a6fec1-2b17-3f21-b274-18ec2d21025e | -11.11023 | -43.33397 | 2024-10-12 04:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 859590ff-3e32-30e8-a0cb-f0a18c42e959 | -11.10634 | -43.33696 | 2024-10-12 04:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 63b74cc4-4463-39f6-be67-1ec2329cebfa | -5.9934 | -37.9615 | 2024-10-12 04:06:00 | NOAA-20 | VIÇOSA | RIO GRANDE DO NORTE | Brasil | 2414902 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 915950cd-45bf-3a1b-9460-5469b5abe98b | -6.62627 | -43.8567 | 2024-10-12 04:06:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d088d083-1e34-36b0-8077-cf1027b77e32 | -8.82406 | -45.37621 | 2024-10-12 04:06:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8226cbeb-d984-3ad7-8f1f-226df0dc5fe7 | -8.1341 | -44.46285 | 2024-10-12 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8252ee8-9d21-3560-afac-671de9093987 | -8.13346 | -44.46677 | 2024-10-12 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 426b7443-dea4-37b9-a2d9-f09506765019 | -8.1306 | -44.46227 | 2024-10-12 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5079cfd-8028-31d9-8bcf-10a8f36efc1e | -9.10157 | -45.82526 | 2024-10-12 04:06:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1eced77a-675f-3191-803d-5baa0890832e | -6.48511 | -43.88167 | 2024-10-12 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 01982d1a-4153-3730-b970-9eb08445b2de | -6.48226 | -43.87722 | 2024-10-12 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a8cef4d-1ac6-39a3-acad-edc31258f7a8 | -7.21619 | -38.98477 | 2024-10-12 04:06:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fedcd422-fdc5-3034-b5bb-c72a055e4210 | -7.2156 | -38.98871 | 2024-10-12 04:06:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 985c5b17-2b62-37ad-92cf-f3eba3f4aac1 | -6.71617 | -38.46938 | 2024-10-12 04:06:00 | NOAA-20 | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a84add46-69b5-3896-8bd5-d8bc0b8936a4 | -6.65996 | -37.46377 | 2024-10-12 04:06:00 | NOAA-20 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 61fee426-f45f-3c7d-a35b-06fb295bb1c0 | -6.60487 | -37.94253 | 2024-10-12 04:06:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 153e805a-c6a4-3480-8689-863f8b532a0d | -6.60056 | -37.94617 | 2024-10-12 04:06:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 812109ff-fde5-3767-9356-ce1dc28e422c | -6.44922 | -38.81934 | 2024-10-12 04:06:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| aa0d95bd-37c3-3267-8a11-507e24cbf186 | -6.4457 | -38.81879 | 2024-10-12 04:06:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cf1b9396-0586-3292-ab6a-5ea91d239182 | -9.56644 | -38.3075 | 2024-10-12 04:06:00 | NOAA-20 | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f3b6de0e-417d-3281-a928-37aad909ad43 | -5.69318 | -39.0621 | 2024-10-12 04:06:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5c718c72-5445-3470-a033-e8142a9b2b29 | -7.46997 | -40.22337 | 2024-10-12 04:06:00 | NOAA-20 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 560df471-15af-310b-8d82-215ad28f6c47 | -7.4666 | -40.22286 | 2024-10-12 04:06:00 | NOAA-20 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 03537308-24c7-307a-8d3a-d8608b7cfb9d | -7.46322 | -40.22235 | 2024-10-12 04:06:00 | NOAA-20 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b726095b-2a57-3481-bcf2-175e2e30adc8 | -7.41798 | -40.45064 | 2024-10-12 04:06:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6690187e-cd05-37aa-b73b-c9cff23f8441 | -6.51456 | -39.69018 | 2024-10-12 04:06:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5f094000-3741-3a5c-b73a-8218b4da72cc | -6.51399 | -39.69387 | 2024-10-12 04:06:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9057fd0e-2fd9-3092-a999-d1715199bb42 | -6.51116 | -39.68966 | 2024-10-12 04:06:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ed679c2d-eb89-395c-ba16-6f6292b7c12f | -8.77713 | -40.35293 | 2024-10-12 04:06:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8264b57f-d499-34b3-924d-b0d02483acee | -8.34856 | -40.68763 | 2024-10-12 04:06:00 | NOAA-20 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cd02f15c-94fe-3cad-abdb-e652a67a3106 | -8.32397 | -40.61074 | 2024-10-12 04:06:00 | NOAA-20 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3634fb80-b942-370f-af29-877b38ad045a | -8.14798 | -39.70288 | 2024-10-12 04:06:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1c5725bb-8446-3f47-950a-a2cf59473e32 | -8.14741 | -39.70666 | 2024-10-12 04:06:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 483828de-bcc9-3889-aa1d-60730e694f5e | -6.37261 | -40.47422 | 2024-10-12 04:06:00 | NOAA-20 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c5d5b09f-144d-37ad-9d23-e7c4db10953b | -5.64131 | -40.70034 | 2024-10-12 04:06:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 137a530c-a49e-3f79-bfb6-5bb63bd28698 | -5.638 | -40.69983 | 2024-10-12 04:06:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5ff954fb-ec80-3f3b-b2f8-16f6db1c359c | -5.61505 | -40.93405 | 2024-10-12 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dcd17208-8669-3db0-8e9c-8b9366908f3b | -5.40011 | -41.2424 | 2024-10-12 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bd7b318e-eea5-3bfa-bcdb-a6d0f6cc6aee | -5.3968 | -41.24189 | 2024-10-12 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 474f0618-5b97-32ac-94f9-ecb7a7a7672e | -5.39626 | -41.24533 | 2024-10-12 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8954306a-2ad0-3117-a36e-d52a42fae982 | -5.3935 | -41.24137 | 2024-10-12 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |


[Clique aqui para ver as próximas entradas](README44.md)
