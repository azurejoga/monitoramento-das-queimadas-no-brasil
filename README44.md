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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ceda41b3-a410-3998-9acf-c67ee8653c48 | -3.364 | -50.4072 | 2026-10-09 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 6e6e896d-b09f-39b8-a755-c3b0afc20a2b | -7.4095 | -44.7656 | 2026-10-09 00:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.9 |
| cc3b0759-c5ef-3910-a4eb-449f00fc45e6 | -3.1285 | -54.1657 | 2026-10-09 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 128.5 |
| a01b248d-97ae-3e88-a4cd-aca5456ac0d2 | -3.0925 | -53.9455 | 2026-10-09 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 2c40f10a-a5f8-324b-b3a8-ad1c763eebd7 | -3.5677 | -54.6746 | 2026-10-09 00:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 20570af8-3385-31ef-84cc-419137419b56 | -6.8907 | -45.8988 | 2026-10-09 00:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 6f6ed051-f024-3de5-8f6a-697d04807d40 | -8.7231 | -45.1583 | 2026-10-09 00:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 23429b2d-5ef3-3d5b-ac4d-02efe95d24d4 | -6.4903 | -62.8554 | 2026-10-09 00:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 510ddffe-3c9f-36c5-bf43-72f07e221ffe | -3.9912 | -59.356 | 2026-10-09 00:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 88ce489b-c9f5-3168-b568-60c88c89bd87 | -11.9865 | -43.4671 | 2026-10-09 00:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 188.2 |
| d639e03c-80b1-3df8-9afb-bb2f6edef62c | -8.8921 | -45.2311 | 2026-10-09 00:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 55.8 |
| a0db7e51-74ba-3898-a8e9-ec62493e2027 | -5.7679 | -43.8467 | 2026-10-09 00:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| a71f9e51-8e16-3a32-bd53-0e3b125bfd02 | -7.2182 | -55.1416 | 2026-10-09 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| f98a6cc2-958d-3988-9531-dd27a5e99e66 | -13.1827 | -54.3571 | 2026-10-09 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 106.9 |
| c62c39fc-0c22-3522-83d9-718683813cc0 | -8.8961 | -44.9336 | 2026-10-09 00:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 63404209-12c9-3f67-bdb0-111560f79586 | -4.6096 | -49.2156 | 2026-10-09 00:40:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 98d88292-0c8a-3cc7-bc11-65d126c8483b | -3.1109 | -53.945 | 2026-10-09 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 95c85683-452a-3c17-b797-94155deb9038 | -5.9833 | -40.961 | 2026-10-09 00:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 136.8 |
| 72e7e4e5-1751-3c49-a90c-940384f2324d | -3.0007 | -53.9075 | 2026-10-09 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| ca5a397a-8222-340d-934d-a6e27665b658 | -6.0207 | -40.982 | 2026-10-09 00:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 62.1 |
| f11f6a38-23bf-321a-b47e-af67b9c62b71 | -3.1101 | -54.1661 | 2026-10-09 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 139.4 |
| 9e3c4abf-f37d-3896-9e11-240a7fdb4ca0 | -5.7119 | -53.4658 | 2026-10-09 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| c38effec-72d9-3e2e-822f-e135f27d3aeb | -7.2187 | -55.0815 | 2026-10-09 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| f7999423-02b4-3c07-9fa6-73d3bc549092 | -12.0251 | -43.4609 | 2026-10-09 00:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 6655b8f6-b621-3b08-b0f7-39e7ef436080 | -3.2759 | -54.0614 | 2026-10-09 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| cda60103-83c6-3d3c-b576-d97f27cece52 | -3.1298 | -53.7834 | 2026-10-09 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 62aaa2be-ba7f-3752-a9cf-3a6ed8caf9db | -15.1063 | -49.9055 | 2026-10-09 00:40:00 | GOES-19 | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 62.5 |
| bfcdc800-0b0a-30ce-b6b9-73ae09e35f04 | -5.7117 | -53.4862 | 2026-10-09 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 126.1 |
| feb303e9-ade4-3d34-952d-6bf4d8ac419a | -7.4442 | -63.5589 | 2026-10-09 00:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 33e50759-f0f2-300c-9600-86aca57e2b7b | -1.1094 | -54.1802 | 2026-10-09 00:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 06c0f9b1-5a2e-3b61-97d0-2aa8a3c2524e | -7.218 | -55.1617 | 2026-10-09 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 124.1 |
| 8323fcb4-01c0-3949-90a8-88203e389758 | -7.5834 | -61.5516 | 2026-10-09 00:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| ccccf919-0fda-3317-819f-78e49d2d41ce | -5.7116 | -53.5065 | 2026-10-09 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 97563517-9375-374f-b2c8-dad99ae7680c | -3.1114 | -53.7839 | 2026-10-09 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| ba0cc42d-64c0-3f90-a650-001b11cc2eb8 | -7.2372 | -55.0805 | 2026-10-09 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 7df6d463-b9ab-38d1-a727-747551e971d0 | -8.742 | -45.1563 | 2026-10-09 00:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 62.5 |
| bdaaac4b-9a87-3ae9-b435-8d54a0b37537 | -11.6562 | -43.6846 | 2026-10-09 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| cd7d7b44-0ca9-3c1e-942d-6748c74a59b4 | -15.4287 | -43.2373 | 2026-10-09 00:40:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 96.3 |
| fe89ce02-252f-3b12-b915-8cd291a45493 | -5.6934 | -53.4667 | 2026-10-09 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| fd4ac378-4c57-305e-a198-5954a0efdab6 | -6.0024 | -40.935 | 2026-10-09 00:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 159.5 |
| ba7430e8-9e91-3db5-9cd4-643c1608fe5a | -3.11 | -54.1862 | 2026-10-09 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 3121456b-8d07-3b24-a3e2-02272e4033d9 | -6.7363 | -55.1675 | 2026-10-09 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 9d7ae6db-8f1e-3b3d-ad5f-e3a76b8de8f0 | -6.0076 | -53.4919 | 2026-10-09 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| e78a30a5-adf8-3f60-8729-7090b38b5c57 | -7.1825 | -52.6283 | 2026-10-09 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 478cd04c-bab8-3f93-b9bf-feffc311062c | -12.2158 | -57.0887 | 2026-10-09 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 314fa2f4-99d8-36fb-812f-3b7ba46190a0 | -3.0186 | -54.068 | 2026-10-09 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| d54aa6f1-ccb9-330b-8141-8e0f29962805 | -6.021 | -40.9577 | 2026-10-09 00:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 110.2 |
| 6e170d15-fb54-3102-84f4-422a5c83f647 | -13.2015 | -54.3757 | 2026-10-09 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| d68517b9-800d-3a21-83dc-bfb5abd73100 | -13.2018 | -54.3551 | 2026-10-09 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| a7ce27ac-ad4b-35e3-bf96-3e61f905d67f | -14.8854 | -50.2883 | 2026-10-09 00:40:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 80c72184-7b6e-3b45-9e26-0530b6e83974 | 4.4435 | -60.9657 | 2026-10-09 00:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 5c23a6cf-5afb-3f61-a1a9-4598c94224db | -11.9861 | -43.4908 | 2026-10-09 00:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 229.2 |
| 5ed01d16-ed4a-3d60-be2d-0ec14806e0c5 | -9.297 | -47.4313 | 2026-10-09 00:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 41adcf77-3712-31fd-b714-7237ec0f018b | -8.9113 | -45.2062 | 2026-10-09 00:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 94.5 |
| dd05dbfc-7f2b-3058-a51a-6a7498ad06bb | -6.0019 | -40.9837 | 2026-10-09 00:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 214.2 |
| 4974cba5-124e-3e14-886d-7e42654724c8 | -5.983 | -40.9854 | 2026-10-09 00:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 59.3 |
| 9f1a1ddc-ad94-3411-964f-157d67707c0c | -3.5493 | -54.6752 | 2026-10-09 00:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 7353ccf1-8daa-3541-ab4b-b493a41ecc5d | -3.2576 | -54.0418 | 2026-10-09 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 2a94beb6-7bed-32c1-b75f-368fc6dcbfa9 | -13.1636 | -54.3591 | 2026-10-09 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 87.8 |
| e74b4e48-7de0-3334-b42c-495fac0d81ae | -2.499 | -56.0675 | 2026-10-09 00:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| b16ed652-7eb0-3e2d-b32a-ec82d9ff36bb | -12.2156 | -57.1087 | 2026-10-09 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 111.2 |
| a38f83f0-21ad-33a0-afe4-e39ecad1f68e | -1.1094 | -54.1601 | 2026-10-09 00:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 3b868a0b-64fc-32bb-bc93-88bb68972cc7 | -10.0253 | -48.036 | 2026-10-09 00:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 1355e6a7-8aeb-3d03-a5b9-4843f93caebd | -12.0054 | -43.4878 | 2026-10-09 00:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 197.4 |
| 4e3d5869-307a-3e29-8bac-f6baea3aa8c1 | -10.0253 | -48.036 | 2026-10-09 00:50:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| b10cf78d-0462-38b8-8b94-dba674f6dd30 | -6.0019 | -40.9837 | 2026-10-09 00:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 130.4 |
| 12631b4f-f1bc-33b9-9f90-6b610280dc14 | -8.742 | -45.1563 | 2026-10-09 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 8317f32a-f69a-385b-a888-954d5c79f544 | -3.3455 | -50.4078 | 2026-10-09 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 243.0 |
| 1a335441-2a8f-3c10-93a1-74983e5f8339 | -7.5834 | -61.5516 | 2026-10-09 00:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 14d4b616-1965-3678-b37b-5866b179ad15 | -19.879 | -48.3251 | 2026-10-09 00:50:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 94d9eba7-bdae-3e85-8a39-6f1dd2c6ff1c | -5.7119 | -53.4658 | 2026-10-09 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 9ededfae-1027-3a05-bc21-031755a941cd | -11.7603 | -61.0549 | 2026-10-09 00:50:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 43.8 |
| b94caa32-ec12-3a48-92ab-76a566777a85 | -3.5493 | -54.6951 | 2026-10-09 00:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 141.4 |
| a62806b3-3e6d-3b78-a097-3abfd244912f | -11.9861 | -43.4908 | 2026-10-09 00:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 87.7 |
| c6e0f231-d89d-3589-b9e6-5391fdc94367 | -12.2156 | -57.1087 | 2026-10-09 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 81336395-543d-3094-9e77-327e052468aa | -3.1971 | -50.5801 | 2026-10-09 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 171d8ba9-3bbd-343d-8c0f-79ca1c76f68b | -3.2057 | -58.8546 | 2026-10-09 00:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 674d5d37-156b-3a92-9cd2-e542d3d049f6 | -12.2346 | -57.1071 | 2026-10-09 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 95.3 |
| ca2625c4-a280-3944-a04e-3f66c4a8c8f7 | -6.8907 | -45.8988 | 2026-10-09 00:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| efee4534-eddb-3b52-84e8-3478eb250f2a | -2.7428 | -54.1146 | 2026-10-09 00:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| baff0407-8773-3080-825e-27a1f68d5c3b | -11.6562 | -43.6846 | 2026-10-09 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 728039a7-f82e-3037-9b94-6420295f28ad | -12.0063 | -43.4402 | 2026-10-09 00:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 66f8bbf0-eb49-3286-97ac-660e9a4c33b0 | -3.1787 | -50.5807 | 2026-10-09 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 8f3b1f9a-d2c4-317a-9ae7-18b0b336a4e7 | -4.6096 | -49.2156 | 2026-10-09 00:50:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 6304d6b4-5722-38bc-aca6-abb759ba0896 | -3.1114 | -53.7839 | 2026-10-09 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 057481c8-49b8-368c-bc21-3a7462eeaf17 | -12.2154 | -57.1287 | 2026-10-09 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| bb4d711b-7663-3598-a310-42b52661ba91 | -13.2015 | -54.3757 | 2026-10-09 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| af31a743-6fa2-33ac-b23e-2a958c463090 | -13.2018 | -54.3551 | 2026-10-09 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| f7f2c4e4-0ab8-3a44-877f-5a42c24cb9db | -6.021 | -40.9577 | 2026-10-09 00:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 115.9 |
| 740a748f-95a3-3c29-8af7-ad42c9e20c27 | -12.2158 | -57.0887 | 2026-10-09 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 487f6bd4-8695-3241-a82e-f037316d2fa0 | -3.5676 | -54.6946 | 2026-10-09 00:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 6b764e86-d066-3f78-ae01-ec1454990e1a | -13.1636 | -54.3591 | 2026-10-09 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 6133f93d-908f-31ac-a526-411dea817f15 | -6.7365 | -55.1474 | 2026-10-09 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 0fae4a5c-aab2-3b22-9fb0-10f13728f324 | -1.1094 | -54.1802 | 2026-10-09 00:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| c7215e0f-95d1-30ec-b680-34d9c4c4e833 | -6.4949 | -55.2995 | 2026-10-09 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| cf9541e2-320c-3373-9287-efcd81e06f77 | -3.1284 | -54.1857 | 2026-10-09 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| ac14ba45-95ee-37a9-b1d1-dee11cb700db | -4.2954 | -49.0807 | 2026-10-09 00:50:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 7558a336-b605-3889-b5a0-6a716b3626ca | -22.6183 | -48.0011 | 2026-10-09 00:50:00 | GOES-19 | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 94.6 |
| e6455c63-f1d4-35d9-a70f-666e3204f5c2 | -3.5677 | -54.6746 | 2026-10-09 00:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| b7b00d31-2161-387e-aadc-466db41b1a76 | -3.0007 | -53.9075 | 2026-10-09 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |


[Clique aqui para ver as próximas entradas](README45.md)
