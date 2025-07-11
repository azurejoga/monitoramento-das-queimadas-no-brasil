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
| e563e8db-5425-3af8-8267-603685b24bd8 | -12.9959 | -46.288898 | 2025-07-11 00:41:00 | METOP-C | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2d78accb-280b-3902-aae9-4988e2809685 | -5.7879 | -45.1092 | 2025-07-11 00:41:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1584c79c-fa90-363d-9c27-cbec6fd2c8dd | -7.0844 | -49.613499 | 2025-07-11 00:41:00 | METOP-C | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 596d3eb9-bbb6-306d-8c58-3e1d2ae90b57 | -11.329 | -51.448101 | 2025-07-11 00:41:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 435db1d8-b71a-318d-aceb-446a82acac8e | -9.8625 | -47.872002 | 2025-07-11 00:41:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f90055f1-46c5-3604-840d-fb7453f3beda | -9.9133 | -47.823601 | 2025-07-11 00:41:00 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c1ef03c2-68cc-376c-aaa7-4deb5c1bdc10 | -15.3604 | -49.490501 | 2025-07-11 00:41:00 | METOP-C | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b2a4509d-ba39-3ad2-800d-47d0c88faf02 | -5.564 | -43.9132 | 2025-07-11 00:41:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5e2872ca-a2c0-3d8c-9049-4492dc6447a0 | -8.8944 | -47.344299 | 2025-07-11 00:41:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d60a9770-d036-3944-8661-b9ef151c5a17 | -10.8866 | -46.765301 | 2025-07-11 00:41:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 09f88124-5da9-3d1f-93e7-73d587ed7542 | -8.2319 | -44.926899 | 2025-07-11 00:41:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a997a7e1-ad47-3508-9e37-fcf83ba36845 | -7.2196 | -43.128601 | 2025-07-11 00:41:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5912dd9b-6da3-3d3e-a9f5-9e3b668988cd | -11.272 | -44.8941 | 2025-07-11 00:41:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dd901ecc-bce7-37a8-8a81-754e389e0474 | -11.5786 | -47.437698 | 2025-07-11 00:41:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 41df5516-1689-3a4d-838d-9085d5e20168 | -5.8454 | -48.394001 | 2025-07-11 00:41:00 | METOP-C | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a769dfb-9a6d-36d7-ada9-36ffaec1553c | -11.577 | -47.430698 | 2025-07-11 00:41:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b3e1df17-8e62-36a1-a483-97c8b5ed8af2 | -6.8649 | -42.815701 | 2025-07-11 00:41:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8e489f89-b416-32f0-aa3d-4c02ced912d8 | -5.5585 | -43.890202 | 2025-07-11 00:41:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9d3f5619-c829-3bac-9fb4-3a47159ba93a | -12.0587 | -48.5532 | 2025-07-11 00:41:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9c51de78-dc6b-3e27-9f60-19f23129ca53 | -11.9376 | -49.3013 | 2025-07-11 00:41:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a4369214-b405-323b-a797-5a302f02d7c1 | -12.9942 | -46.281601 | 2025-07-11 00:41:00 | METOP-C | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 41066b4c-1110-3047-97ff-09f79b140565 | -10.6301 | -45.236099 | 2025-07-11 00:41:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 86ce1ee3-dfd9-3f47-953b-f31aeb27a2fd | -7.2099 | -43.131001 | 2025-07-11 00:41:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e75eee79-e783-3732-b2c0-5d1a642e6629 | -10.6836 | -49.493698 | 2025-07-11 00:41:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7353514e-c288-31a8-bb6e-b7025a1d105b | -12.6641 | -47.087399 | 2025-07-11 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4386045b-7e85-3c69-b6f4-5256bda35866 | -5.7901 | -45.118801 | 2025-07-11 00:41:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5fecc7e5-0380-3e5b-bc62-0e4cc5c13bb1 | -4.5519 | -48.021301 | 2025-07-11 00:41:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b123fbe5-d079-36b2-b846-3e869737a842 | -10.6852 | -49.500801 | 2025-07-11 00:41:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8c7d88e5-934c-38ff-a97f-ad6f7303c39d | -11.8426 | -47.509399 | 2025-07-11 00:41:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a1494ba0-f27a-3535-8430-67c030742160 | -4.7911 | -45.342098 | 2025-07-11 00:41:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f525c22-aec7-3fad-8716-732f20235949 | -5.5515 | -43.903999 | 2025-07-11 00:41:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9efde3fb-0c5a-37a8-89cd-6378a31dee5e | -13.1545 | -47.291801 | 2025-07-11 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d3cfab77-a8e0-3082-be10-91f8265c1ed9 | -11.3301 | -45.224602 | 2025-07-11 00:41:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5624397d-1cda-32a0-a293-675a181d9499 | -10.8768 | -46.767502 | 2025-07-11 00:41:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8787476a-c99b-3c8f-a894-c4d010db43b1 | -11.4513 | -45.125599 | 2025-07-11 00:41:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2bf3ef43-f805-32c4-9ac5-7c4d9e374b21 | -9.9165 | -47.837502 | 2025-07-11 00:41:00 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 85b75f46-1570-35c4-a700-afb56ca3bb78 | -10.8559 | -49.113701 | 2025-07-11 00:41:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e7ad3968-1ed8-3bdc-a20b-cae60d8d9c2d | -7.2723 | -49.578499 | 2025-07-11 00:41:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5dd7ddb8-6e6e-36ab-98ac-c1c1e623ef64 | -12.9912 | -44.863701 | 2025-07-11 00:41:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1d28402b-2adf-39fc-95b6-a2058e76522c | -12.4224 | -43.491699 | 2025-07-11 00:41:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 67a82bab-32d4-3137-ae3b-54a95cbd02d0 | -10.8493 | -49.130001 | 2025-07-11 00:41:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bcd953ea-a393-3631-bde5-272cb7606d3f | -2.9319 | -48.242699 | 2025-07-11 00:41:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb9769c9-07fc-3714-bf9f-67013c0c377e | -7.9545 | -44.846401 | 2025-07-11 00:41:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e7c88f33-d3da-3633-bc56-8a27892873b5 | -12.9925 | -46.2742 | 2025-07-11 00:41:00 | METOP-C | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e4a24a7f-f792-3cb9-b962-6b721788173c | -12.0279 | -49.5233 | 2025-07-11 00:41:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 583198b3-1a08-395a-9520-825bc28a8f73 | -21.2752 | -48.5681 | 2025-07-11 00:44:00 | METOP-C | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6a5b9409-b022-3130-a98a-b2dcd107f686 | -22.259701 | -54.929298 | 2025-07-11 00:44:00 | METOP-C | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 32b8f5c5-cdc4-35da-82c9-4ab7a5d81c65 | -23.599501 | -49.006901 | 2025-07-11 00:44:00 | METOP-C | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 23ec175c-547f-3696-ae01-872e1ec574b3 | -22.2759 | -54.967899 | 2025-07-11 00:44:00 | METOP-C | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| eb894979-c39a-32af-b451-0b5950fb601f | -21.267099 | -48.578602 | 2025-07-11 00:44:00 | METOP-C | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f12ddb2f-37ca-3e07-beab-5dbce32eb59c | -21.2654 | -48.570301 | 2025-07-11 00:44:00 | METOP-C | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| db503a8e-cbbc-3ff5-95b6-abcb9d8c2454 | -22.253201 | -54.951199 | 2025-07-11 00:44:00 | METOP-C | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 76c58ccc-86cc-31e6-9401-335b6297b1a1 | -22.262899 | -54.949402 | 2025-07-11 00:44:00 | METOP-C | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0a561d03-abaf-3833-879b-6eb002c27774 | -22.2694 | -54.927502 | 2025-07-11 00:44:00 | METOP-C | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 08304e40-aaf9-361e-8c15-2f9066438515 | -21.688499 | -49.508202 | 2025-07-11 00:44:00 | METOP-C | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 962a50c8-f486-3929-892f-b1a72a43738c | -21.6849 | -49.4897 | 2025-07-11 00:44:00 | METOP-C | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2ccfc6e2-ad93-345f-96d8-44e105819e84 | -19.4471 | -48.543201 | 2025-07-11 00:44:00 | METOP-C | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 494d822e-7fa7-3358-a414-a45927446ab4 | -21.276899 | -48.576401 | 2025-07-11 00:44:00 | METOP-C | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f54fa851-3bee-3133-a97a-b968a3a99b14 | -22.2726 | -54.947701 | 2025-07-11 00:44:00 | METOP-C | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6ff55450-0e01-30d6-ac3b-7b19a669acd5 | -19.4454 | -48.535301 | 2025-07-11 00:44:00 | METOP-C | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1f42adeb-57a8-3aa3-b7e9-afba7e1f26a1 | -19.6066 | -44.8153 | 2025-07-11 00:44:00 | METOP-C | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2de5b76c-e9ed-354c-b37e-30d16fdb45a2 | -16.049299 | -43.723301 | 2025-07-11 00:44:00 | METOP-C | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e26c9c50-0088-3947-b4ff-5d650e94b86f | -21.686701 | -49.498901 | 2025-07-11 00:44:00 | METOP-C | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7b7e8e42-1181-30ba-93c0-ec064f368d47 | -22.266199 | -54.9697 | 2025-07-11 00:44:00 | METOP-C | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5ae2e0b3-4df7-3d4f-8da8-536f96024c35 | -5.5614 | -43.9082 | 2025-07-11 00:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 01b5f27b-fa46-3d9b-950d-1a94db0f8003 | -10.5776 | -49.1316 | 2025-07-11 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 130.4 |
| dc72eb3c-4dd2-322a-b067-386a79c17596 | -7.2025 | -43.1171 | 2025-07-11 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.9 |
| 9d74a8c4-1f05-3b3c-bc0d-0dcb2d495fcd | -10.6859 | -49.509 | 2025-07-11 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 6a74703e-e7aa-3f7b-9f3d-5ef12335e9a3 | -10.6669 | -49.5111 | 2025-07-11 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| eb01a388-c5ff-3ecd-a061-412a45d30445 | -10.8429 | -49.1236 | 2025-07-11 00:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 344a7978-1644-3f56-b5d2-1be48ced2e3c | -9.8958 | -47.8303 | 2025-07-11 00:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 87895a12-38db-394e-80ba-e4eab68c8bba | -10.6862 | -49.4874 | 2025-07-11 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 187.7 |
| 402721de-c178-3cf3-a435-0e9b5806dc85 | -22.2852 | -54.9409 | 2025-07-11 00:50:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 65.2 |
| eb29d2e6-b472-3e4c-bf1b-bbf42fd51efc | -10.8619 | -49.1214 | 2025-07-11 00:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| a6b540c9-89fd-3d3c-9975-2f117c125598 | -9.9148 | -47.8282 | 2025-07-11 00:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 344.7 |
| 1a057fd8-1ea3-3af1-9909-50f50998e5ad | -9.9151 | -47.8062 | 2025-07-11 00:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| e9797926-d5eb-3400-8ba4-2c2aef29f3bb | -9.9145 | -47.8503 | 2025-07-11 00:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 5d39e6e5-48d3-31fa-8b09-623d8a365a80 | -10.5965 | -49.1295 | 2025-07-11 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| ceb4cfe4-8b08-3dc2-a222-c2ca8cbc51f9 | -22.2847 | -54.9627 | 2025-07-11 00:50:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 56.5 |
| f17f8eb6-10c4-33c7-b064-5555934a18a5 | -5.5427 | -43.9096 | 2025-07-11 00:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 6b1c4d0e-bde8-33a9-b7d4-fb56d59498aa | -10.6672 | -49.4895 | 2025-07-11 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 166.8 |
| dd7fea35-8dc6-3fd1-8e2b-a0ac4f1249ab | -5.5616 | -43.8851 | 2025-07-11 00:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 4c81dab7-dc8e-33b0-857f-259007deee61 | -5.5429 | -43.8864 | 2025-07-11 00:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 128.9 |
| cfbd066b-fba1-3fc3-9444-70e64a3192b1 | -7.2025 | -43.1171 | 2025-07-11 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 106.8 |
| e5b6479f-24d3-39b3-bf7e-ab8ac619744b | -10.6669 | -49.5111 | 2025-07-11 01:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| e34c746b-917a-3109-a3fa-9a5e65b10082 | -9.9337 | -47.8261 | 2025-07-11 01:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 9b44946f-fa3c-3810-b3f3-56e68a6e2cf6 | -9.9148 | -47.8282 | 2025-07-11 01:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 280.3 |
| 94bf5a83-461c-3e8f-b3b8-c83bc5c1e12d | -10.6859 | -49.509 | 2025-07-11 01:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 4ad2bb34-540b-3b1d-b200-822eb49a1af6 | -10.6672 | -49.4895 | 2025-07-11 01:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 174.8 |
| 4dc12403-686a-3a23-bc66-956e8ada9bb1 | -10.5776 | -49.1316 | 2025-07-11 01:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 147.4 |
| a06ddee0-e432-3dea-9c35-aa58593c4bdb | -10.6862 | -49.4874 | 2025-07-11 01:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 184.4 |
| 18d31ffd-6fc0-3fdc-a202-8d893cf472ba | -9.8958 | -47.8303 | 2025-07-11 01:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| db49a966-e286-36e1-8424-dacad7482791 | -10.8429 | -49.1236 | 2025-07-11 01:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 1c15cc89-085d-326c-a756-e89e9c8f61f9 | -9.9145 | -47.8503 | 2025-07-11 01:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 2a1e7921-9979-38c0-88f2-281ffeb33016 | -5.5614 | -43.9082 | 2025-07-11 01:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| c692c953-5064-3de2-bd95-18207f32a258 | -5.5429 | -43.8864 | 2025-07-11 01:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 154.2 |
| ca5c8a62-37a7-3abb-8fcf-0abd4da4e784 | -16.956 | -49.4237 | 2025-07-11 01:00:00 | GOES-19 | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 70aa5bf3-e6d1-3ac9-b89c-83a04cd2fc03 | -5.5427 | -43.9096 | 2025-07-11 01:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 217.3 |
| 94cc4cff-3a77-361f-8424-82bac8e192fa | -5.5616 | -43.8851 | 2025-07-11 01:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| f213f2aa-cfa1-3e47-b85f-dd72623984b4 | -9.9145 | -47.8503 | 2025-07-11 01:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |


[Clique aqui para ver as próximas entradas](README4.md)
