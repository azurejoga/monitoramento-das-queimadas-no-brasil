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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9b5e85f-45bd-35cf-96f1-620fb8da250d | -10.7262 | -50.7044 | 2026-09-21 02:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 8608bceb-4d94-3875-826e-6c8dc5254044 | -10.0903 | -50.2368 | 2026-09-21 02:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 3758bb3a-9190-36cc-affc-28d1708df4ce | -7.5889 | -57.6757 | 2026-09-21 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| ec79d8c5-7469-3244-a996-83565c539808 | -3.0534 | -61.2767 | 2026-09-21 02:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 624652f0-5bbc-3c6f-9c88-f5a4bb2431b6 | -11.8014 | -49.8129 | 2026-09-21 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| bc8d72a2-85e7-3fbc-8c16-d6586bc61033 | -10.09 | -50.2581 | 2026-09-21 02:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 46c4060f-177b-3a6a-9d8d-65a250a3b3ba | -3.0717 | -61.2764 | 2026-09-21 02:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 9a4009a1-00a8-348c-a486-bdba96a470f9 | -3.424 | -59.2726 | 2026-09-21 02:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| e2aa846b-a1c1-3e04-9ec2-d5138a957ab8 | -14.8703 | -47.1576 | 2026-09-21 02:40:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 96.9 |
| cc27f4fd-7d4f-396b-911b-d474cdac6672 | -10.7262 | -50.7044 | 2026-09-21 02:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.9 |
| f4b391f7-592e-31a9-b44f-8eaf14f65780 | -10.09 | -50.2581 | 2026-09-21 02:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 2b229b9c-4398-3b3f-a5f4-81ccfd49e413 | -11.8014 | -49.8129 | 2026-09-21 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| fe1e7ad7-ccd1-37ca-990b-f098b9a354b0 | -14.8508 | -47.161 | 2026-09-21 02:40:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 52.8 |
| e8807b67-97d5-30f5-9de5-9d70487ec778 | -10.0712 | -50.26 | 2026-09-21 02:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 86b35864-2fd4-3746-aabc-944164d4747e | -10.7451 | -50.7025 | 2026-09-21 02:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 7858c737-a21e-314b-ab98-751d49f3edf7 | -7.5889 | -57.6757 | 2026-09-21 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 35a69540-c6af-32f5-952d-e3032bed39d9 | -7.5888 | -57.6953 | 2026-09-21 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 3c1a2697-4b70-394c-880a-327da44776d3 | -7.5703 | -57.6962 | 2026-09-21 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| e6fc42d4-b47d-3342-a87f-194fb5b15b4d | -15.4667 | -48.4533 | 2026-09-21 02:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 57a01e72-9f88-3345-a763-32cbe22f02fd | -3.4241 | -59.2535 | 2026-09-21 02:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| b4e372b7-b98c-3016-bd57-05643966d07c | -14.8708 | -47.1349 | 2026-09-21 02:40:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 170.6 |
| 5513e781-4a88-30c9-ac94-f7ac1db713ea | -10.7448 | -50.7238 | 2026-09-21 02:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 2d1bb9df-6e2f-3519-aa79-fde180e6e963 | -6.4486 | -59.9717 | 2026-09-21 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 06f8c135-97f2-37f2-b9ba-254820a2ccb5 | -10.7259 | -50.7257 | 2026-09-21 02:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 38d5b7fd-c17d-3f30-96b4-dbfe39e8551b | -15.4663 | -48.4757 | 2026-09-21 02:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 64096cfd-398d-3082-a867-1512b12e19a7 | -14.8512 | -47.1382 | 2026-09-21 02:40:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 1729c8ca-d9ee-3550-9950-46bc03572a79 | -3.0717 | -61.2764 | 2026-09-21 02:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 84.1 |
| c4af4b0c-9dd1-3420-9759-d5b742004e90 | -3.0534 | -61.2767 | 2026-09-21 02:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| dc1e6efc-8dd9-3b1c-87f7-b832df7d5377 | -7.5704 | -57.6766 | 2026-09-21 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| fbd0c7df-9a65-3d8e-8e52-d9e3bf82f987 | -7.5888 | -57.6953 | 2026-09-21 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| e4bf1021-3430-370f-8ebb-479e2f820863 | -7.5704 | -57.6766 | 2026-09-21 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 4c0ea950-6ecd-36e3-ab40-214f4bc94601 | -3.0717 | -61.2764 | 2026-09-21 02:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| c27272f7-3d7f-322e-97f1-0f1e6c05b6bb | -11.8014 | -49.8129 | 2026-09-21 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 03a2e2fd-aa15-33c8-b09a-5d83c88372da | -10.0712 | -50.26 | 2026-09-21 02:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 43051d56-d4cf-37dc-8cdb-f172456f27c4 | -15.4667 | -48.4533 | 2026-09-21 02:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 72a1eb82-e66d-352b-9af9-b2a3be36c3f9 | -6.7464 | -59.4223 | 2026-09-21 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| a8d5e27b-c3e4-3e6e-98e6-8c80b56772cb | -3.4241 | -59.2535 | 2026-09-21 02:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 72da1d92-cad3-3afd-ae76-b73bc168b60c | -7.5703 | -57.6962 | 2026-09-21 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 9d611fd7-e943-3c90-8422-f6f7f70338b2 | -15.4663 | -48.4757 | 2026-09-21 02:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 81.3 |
| a2362ce8-f715-37b7-8d3d-2ece8658bdff | -3.0534 | -61.2767 | 2026-09-21 02:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 4026ec3c-a952-3875-919b-28a13702d2a1 | -10.09 | -50.2581 | 2026-09-21 02:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 8e584f45-f6b4-3d27-bc9f-4536c0f2cab9 | -4.3541 | -55.6653 | 2026-09-21 02:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 4f3ca287-21a3-376c-b621-c9f8ac005601 | -7.5889 | -57.6757 | 2026-09-21 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| e19e375f-0471-369e-9a4d-1eb63da02987 | -6.2026 | -57.7778 | 2026-09-21 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 47255379-3331-317e-bb8e-87ff1577ed6c | -7.5704 | -57.6766 | 2026-09-21 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 792fb1a9-79ea-3238-95eb-2e1f851f68c6 | -7.4283 | -44.7639 | 2026-09-21 03:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 90eb2878-5ac9-3948-936c-3a065be97f3a | -7.5888 | -57.6953 | 2026-09-21 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 502d9c4e-1f3a-3a92-9a85-7db27b20cd27 | -6.4486 | -59.9717 | 2026-09-21 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| eb7b034d-fb57-3d80-8d42-d03e249329af | -11.8014 | -49.8129 | 2026-09-21 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 827eea8d-2dba-3781-8319-e3ec5509d4be | -6.2026 | -57.7778 | 2026-09-21 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| b6e1dc6a-600c-3659-96f4-25798b6b25df | -15.0738 | -49.5813 | 2026-09-21 03:00:00 | GOES-19 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 89.1 |
| e08faa09-0eb3-3257-9d10-40cf8d5bf8f6 | -7.5703 | -57.6962 | 2026-09-21 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 310f08f7-736e-3e08-95d3-91473b07f17f | -3.4241 | -59.2535 | 2026-09-21 03:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 12ef0100-eef5-34ea-b873-90d43485cb85 | -16.1769 | -50.0211 | 2026-09-21 03:00:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 1ba3981c-59dc-3f3b-a50d-712adffb1589 | -3.0534 | -61.2767 | 2026-09-21 03:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 8ee7a7cb-345d-3e91-95a4-28f926cb42c7 | -10.09 | -50.2581 | 2026-09-21 03:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 0d81bac7-f2e9-3c0b-b567-c19b9f493d55 | -3.0717 | -61.2764 | 2026-09-21 03:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| dc382245-37cc-3ffd-bf3d-89d69b30179c | -7.4095 | -44.7656 | 2026-09-21 03:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |
| df5d28bf-5ad8-36fe-aa7b-8d8f1a333287 | -10.0712 | -50.26 | 2026-09-21 03:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 2d707d07-71ce-3be1-8b4b-b43f229f300b | -7.5889 | -57.6757 | 2026-09-21 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| cdad063c-b5c3-3733-baef-6b2306f5b0c6 | -3.424 | -59.2726 | 2026-09-21 03:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 64bcf526-26ed-3e83-b20e-d150b9f14154 | -15.0547 | -49.5623 | 2026-09-21 03:10:00 | GOES-19 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 30767a97-5251-3c07-a404-bd645c4d29f9 | -7.5888 | -57.6953 | 2026-09-21 03:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 73fbff4c-818b-358a-a34b-8c59e4b3d394 | -10.4862 | -50.2818 | 2026-09-21 03:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 364df022-8183-3f62-8373-7e2b077e139a | -10.4486 | -50.2644 | 2026-09-21 03:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| ffce430d-54ba-3da2-82b9-2001419fa721 | -7.5704 | -57.6766 | 2026-09-21 03:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| c659e255-105f-3697-8bce-0135c26f12bd | -3.0534 | -61.2767 | 2026-09-21 03:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 36.1 |
| e8fbcf08-9aa9-3bf4-bc94-67edc1cf3d0a | -15.0937 | -49.5562 | 2026-09-21 03:10:00 | GOES-19 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 115.8 |
| c790ccd3-ee5a-3e5e-8a16-c51d3825cc8d | -15.0933 | -49.5783 | 2026-09-21 03:10:00 | GOES-19 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 6377c64f-ba5c-33dd-9f81-4c6316460931 | -7.5703 | -57.6962 | 2026-09-21 03:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| a586beb1-caba-365c-bd2c-dce7bb320467 | -15.0742 | -49.5592 | 2026-09-21 03:10:00 | GOES-19 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 247.4 |
| f4424916-3616-3b00-a5a2-8dec77be2475 | -11.8014 | -49.8129 | 2026-09-21 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 8358d5a0-5cb0-31ce-b84c-e01b012a2191 | -3.4241 | -59.2535 | 2026-09-21 03:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 30a0af75-ace0-3033-9b72-448927a7b9c3 | -13.1798 | -43.5749 | 2026-09-21 03:10:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 30007604-82db-3e56-806d-37292f7d594e | -10.4483 | -50.2858 | 2026-09-21 03:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| e24e26ef-3915-3654-a5a0-54f552a7b80b | -7.4283 | -44.7639 | 2026-09-21 03:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.3 |
| d7b9c1e2-5a33-349f-9e71-0efefa6d090e | -3.0717 | -61.2764 | 2026-09-21 03:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| a3d07269-1d42-3d91-8d79-0c506bd4bb95 | -3.424 | -59.2726 | 2026-09-21 03:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 42.1 |
| bb2f9635-57b2-32e0-a358-86a23ee31448 | -9.4381 | -45.3972 | 2026-09-21 03:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 9b3ad4c8-8ee2-3c6a-b3ed-a5abe4be45ba | -15.0738 | -49.5813 | 2026-09-21 03:10:00 | GOES-19 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 275.7 |
| 4b839380-5868-37d4-bc60-06160b3a2906 | -6.4486 | -59.9717 | 2026-09-21 03:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| c1b77aff-b308-3db5-ae49-c2ef9f5c1d0f | -10.467 | -50.3052 | 2026-09-21 03:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| a74066d7-54aa-3cd0-bd30-5cdb2d6ee49c | -7.5889 | -57.6757 | 2026-09-21 03:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| d0305264-bb05-3e06-b9c3-1dc107732a37 | -15.0543 | -49.5843 | 2026-09-21 03:10:00 | GOES-19 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 59272d30-c81e-3b74-bf8a-a26b05fd5210 | -4.3541 | -55.6653 | 2026-09-21 03:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 1f3dac6c-d225-347f-84f6-51c15f3c6a3e | -10.09 | -50.2581 | 2026-09-21 03:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| b3ba0ad3-4a4d-3670-a5b1-41e040562c1d | -9.457 | -45.395 | 2026-09-21 03:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 81fd9787-a9b5-39a4-8d23-a1908178ec48 | -7.4095 | -44.7656 | 2026-09-21 03:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 16748844-4dad-3e75-9d77-cb8a2655778d | -10.4675 | -50.2624 | 2026-09-21 03:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 88005656-5125-3a79-b086-7aaba3415a0d | -10.4672 | -50.2838 | 2026-09-21 03:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 190.5 |
| 9009a35a-ed9a-35ca-88a5-c37d54ee20ca | -7.4283 | -44.7639 | 2026-09-21 03:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 64.1 |
| db2f6ded-92d1-309c-ab53-852ddb916ea4 | -11.8014 | -49.8129 | 2026-09-21 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| a375addd-6e1f-3a9d-b9c5-7c7134dd0519 | -7.4095 | -44.7656 | 2026-09-21 03:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 56ea7b58-2b96-329b-bb27-12b79b2d0e33 | -6.4486 | -59.9717 | 2026-09-21 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 6b8a7a07-1e72-3435-8cdc-9ad06c7eb993 | -9.4567 | -45.4178 | 2026-09-21 03:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 7cf8f70e-1388-3863-ad2c-f2aa86c60a77 | -7.5889 | -57.6757 | 2026-09-21 03:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 48a1253d-28c3-3657-97f2-ae5d2a7b4020 | -3.0717 | -61.2764 | 2026-09-21 03:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 075682c9-e1d8-3ceb-b8fa-ce65e6075c4d | -7.5704 | -57.6766 | 2026-09-21 03:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 1ce89a1b-641d-37d6-b8bb-6e08207f1862 | -9.476 | -45.3928 | 2026-09-21 03:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 7f455028-2f56-3ba5-85b8-eaaef52248bc | -9.457 | -45.395 | 2026-09-21 03:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 125.3 |


[Clique aqui para ver as próximas entradas](README18.md)
