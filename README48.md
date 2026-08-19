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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8cb71da8-7bc1-3b68-89e6-1df2004d910e | -29.13943 | -50.39056 | 2026-08-19 04:44:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| d4363392-802a-392b-bf5a-6b785c43671b | -29.13882 | -50.39518 | 2026-08-19 04:44:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 45c02465-d31c-3e9b-9c3c-8acc9ae25962 | -24.76517 | -49.08923 | 2026-08-19 04:44:00 | NOAA-20 | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 694a40c3-5938-32fc-ac3b-68c2ac9153a1 | -24.7688 | -49.0897 | 2026-08-19 04:44:00 | NOAA-20 | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 45cb7f0a-0de6-39a1-9af8-a0b184cbccb1 | -23.70999 | -46.82395 | 2026-08-19 04:44:00 | NOAA-20 | ITAPECERICA DA SERRA | SÃO PAULO | Brasil | 3522208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 442e7f79-4db3-3dcd-8582-0546f0860772 | -23.75755 | -46.80392 | 2026-08-19 04:44:00 | NOAA-20 | ITAPECERICA DA SERRA | SÃO PAULO | Brasil | 3522208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 1d673f08-c27f-32e6-8510-1ace4ae82424 | -23.21395 | -50.5308 | 2026-08-19 04:44:00 | NOAA-20 | CORNÉLIO PROCÓPIO | PARANÁ | Brasil | 4106407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8caca197-3479-3f16-be15-f5a1f0a078cd | -24.50615 | -50.70458 | 2026-08-19 04:44:00 | NOAA-20 | IMBAÚ | PARANÁ | Brasil | 4110078 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| af32aee7-a6d2-3769-8031-4313a2dd856e | -24.76941 | -49.08529 | 2026-08-19 04:44:00 | NOAA-20 | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| be72df0b-875d-39cd-ad0b-42a864ef8073 | -24.76656 | -49.08763 | 2026-08-19 04:44:00 | NOAA-20 | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 0e0fa9bb-453e-33b0-9a53-8ce2f5e3d523 | -23.43822 | -51.42638 | 2026-08-19 04:44:00 | NOAA-20 | ARAPONGAS | PARANÁ | Brasil | 4101507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cd69e40d-bf99-347e-9c5b-6a24f8096114 | -27.63178 | -51.79623 | 2026-08-19 04:44:00 | NOAA-20 | MAXIMILIANO DE ALMEIDA | RIO GRANDE DO SUL | Brasil | 4312203 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e05f1d4f-67ae-3d0c-88c5-48aeaa873eb5 | -23.75707 | -46.80778 | 2026-08-19 04:44:00 | NOAA-20 | ITAPECERICA DA SERRA | SÃO PAULO | Brasil | 3522208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 832d1c56-9d75-325b-a09f-ca26e37d3c72 | -23.80724 | -47.16655 | 2026-08-19 04:44:00 | NOAA-20 | IBIÚNA | SÃO PAULO | Brasil | 3519709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fef8ef65-2f46-388a-8f24-a4bc515df53a | -5.9995 | -57.8444 | 2026-08-19 04:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 60d2b7dc-757e-301c-99e1-ef00f8e53b3e | -8.5785 | -54.7566 | 2026-08-19 04:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| b3e59006-534e-3f5c-a72c-0d0fe61da0d9 | -9.4061 | -60.5518 | 2026-08-19 04:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 40c77438-bd3b-3e2d-9ad0-061e3065f2a2 | -9.406 | -60.5711 | 2026-08-19 04:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 522165d1-23d9-3de1-b434-4d139eed8426 | -5.9994 | -57.8639 | 2026-08-19 04:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 667d1eb2-45c5-316b-a867-32284b67c5c6 | -5.4319 | -48.3996 | 2026-08-19 04:50:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| db50bbbf-6c8c-3552-9866-481f62965961 | -8.56 | -54.7377 | 2026-08-19 04:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| d1b9083d-b4cc-357d-8e15-2bac5b45c1c3 | -9.4256 | -60.4353 | 2026-08-19 04:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 5389a785-8936-34ba-b74a-56c09a4e41c4 | -8.5598 | -54.7579 | 2026-08-19 04:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| c7858d57-3730-3d1d-8391-7ce28ecaa943 | -5.4317 | -48.4212 | 2026-08-19 04:50:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 6dba67ee-7ed4-38ee-aa16-92f14573c7bd | -8.5413 | -54.7389 | 2026-08-19 04:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 651b916a-9d29-3fc6-a870-db13a8697b3a | -9.4257 | -60.416 | 2026-08-19 04:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 8a16d10c-339c-3850-afb5-f30882ff2c50 | -8.5787 | -54.7364 | 2026-08-19 04:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 72b2b29c-59c0-3577-be34-bbf80cec62ac | -6.0912 | -57.9187 | 2026-08-19 04:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| a4212270-7bd7-3c4d-9bcb-fdbf88cf42e1 | -8.5412 | -54.7591 | 2026-08-19 05:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 7c7c4b7e-2b9a-3ec6-94c1-b4ac6d6b9d0b | -9.406 | -60.5711 | 2026-08-19 05:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 3125dcec-61a3-3e9c-90f2-5ba488ace154 | -9.3875 | -60.5528 | 2026-08-19 05:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 9e424057-2777-372e-bf01-22bdd6187a55 | -6.0913 | -57.8992 | 2026-08-19 05:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 4a8fca8e-4985-3aef-a87f-b51a6029b519 | -8.5598 | -54.7579 | 2026-08-19 05:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| cb0dd094-05b4-38d0-a7d0-85267f118809 | -8.5413 | -54.7389 | 2026-08-19 05:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| b9c658b8-0609-3f82-8622-bd416e89eb8b | -5.9198 | -43.6264 | 2026-08-19 05:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 85299a76-21b3-310e-bc73-1074fcfda60b | -6.0178 | -57.8631 | 2026-08-19 05:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 20a9a4f7-0fdb-32fa-81c8-85ef1cf98294 | -8.56 | -54.7377 | 2026-08-19 05:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| b846807d-f5c6-36e5-894f-3d14b457782d | -5.9994 | -57.8639 | 2026-08-19 05:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 74524c35-da2d-3067-9f38-253bba985aad | -9.4256 | -60.4353 | 2026-08-19 05:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 85bc31bb-85b0-35ae-9893-306f6bc149cb | -9.4257 | -60.416 | 2026-08-19 05:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 664e6f6f-0575-37bb-b342-53833db5b807 | -5.9011 | -43.6279 | 2026-08-19 05:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 8f4bc9bb-1aaa-3802-a7af-24204a98be8b | -8.5787 | -54.7364 | 2026-08-19 05:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 0c611655-275f-34d0-a075-58035358d6e7 | -5.4319 | -48.3996 | 2026-08-19 05:00:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| d750b62d-e7ca-3ffc-b614-b52a84ad6349 | -8.5785 | -54.7566 | 2026-08-19 05:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| bc3769e4-293f-385a-8a1c-816b6d975273 | -6.0912 | -57.9187 | 2026-08-19 05:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 8ceb22dc-999b-37b6-ad2a-a0a115ea27a0 | -9.4061 | -60.5518 | 2026-08-19 05:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 2d053086-2cdb-3158-a8e9-8132c2a5b3bf | -5.92 | -43.6032 | 2026-08-19 05:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| c9c3c429-6944-3587-abbf-2fe4e031eb11 | -5.4317 | -48.4212 | 2026-08-19 05:00:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| af031e6f-3909-365d-80e8-0030713b6b25 | -5.9198 | -43.6264 | 2026-08-19 05:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 1ab5204e-09b8-39d0-bb6b-bbbdcd348d18 | -9.406 | -60.5711 | 2026-08-19 05:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 09e68b60-3533-3a3f-aa61-a0e9c5f435fb | -6.0912 | -57.9187 | 2026-08-19 05:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 2c537daa-0d5a-30b1-9e6f-8e62f2e71027 | -5.4317 | -48.4212 | 2026-08-19 05:10:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 040d25a5-8f37-3d74-aedd-45ac3b3dbbb6 | -8.5413 | -54.7389 | 2026-08-19 05:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 1013f05e-ebcf-37a7-afc2-c6e21260f2f9 | -5.9994 | -57.8639 | 2026-08-19 05:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 32994382-0963-3f62-80d2-ecf865630124 | -8.5598 | -54.7579 | 2026-08-19 05:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 9ef52dc1-64e2-39df-8d08-49bc5ad55bc3 | -5.4319 | -48.3996 | 2026-08-19 05:10:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 75c1037b-73b6-3880-8233-e3192f099225 | -8.5787 | -54.7364 | 2026-08-19 05:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 27beef6d-7daa-3453-937d-430e8a367ef8 | -9.4254 | -60.4545 | 2026-08-19 05:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 6973be26-85c5-3ed7-a57e-36fee8637d7e | -9.3875 | -60.5528 | 2026-08-19 05:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 40.2 |
| ad574e0f-2204-38bc-b0fe-f4fc7acfcfad | -8.5785 | -54.7566 | 2026-08-19 05:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| e7dc7d6c-2535-300b-92b7-7b847b623dbb | -9.4256 | -60.4353 | 2026-08-19 05:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| f9215484-d04f-3333-9a65-70767aa1286a | -8.56 | -54.7377 | 2026-08-19 05:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 340dacd1-f3a9-3585-a922-2e30ec236787 | -19.74 | -57.96 | 2026-08-19 05:15:00 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 98f555d3-de4d-3ac7-b330-a6e73eb69860 | -19.77 | -57.98 | 2026-08-19 05:15:00 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f48fd662-1dde-3896-894f-cc603390f8ce | -9.406 | -60.5711 | 2026-08-19 05:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 12b489c5-679c-3a38-abc1-7dcd271c676d | -9.4256 | -60.4353 | 2026-08-19 05:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 06172326-0634-3edf-b129-ba999f3c3d88 | -5.9198 | -43.6264 | 2026-08-19 05:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 7ed9f6fd-d048-3271-aca7-e1d416bd5784 | -8.56 | -54.7377 | 2026-08-19 05:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| a0d2d088-6e09-34cd-a1df-c6df92d94d6b | -5.9994 | -57.8639 | 2026-08-19 05:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 3cf70e4a-9cf6-3c91-886e-87eedf9c16b3 | -8.5787 | -54.7364 | 2026-08-19 05:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 27ee4ba6-b61b-3b9b-b8f8-f83e2e104dbc | -8.5598 | -54.7579 | 2026-08-19 05:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 41a296f6-d77f-3274-af4b-367c504c1f8b | -8.5785 | -54.7566 | 2026-08-19 05:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 84d29dc2-afd6-3711-a130-35735dda681c | -6.0912 | -57.9187 | 2026-08-19 05:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 4d4a2674-4dea-3d47-82af-04a303c53582 | -5.4317 | -48.4212 | 2026-08-19 05:20:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 55257087-2095-3afd-8c89-afb10463ac89 | -5.9011 | -43.6279 | 2026-08-19 05:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 0c596536-c4c9-3161-834c-a8e1f4a92673 | -5.4319 | -48.3996 | 2026-08-19 05:20:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| c29090fe-993a-33b9-8242-7c06dfbc1745 | 4.50131 | -60.78034 | 2026-08-19 05:21:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9469d34a-0d98-33aa-ba39-c7674ad0d872 | 4.63525 | -60.53875 | 2026-08-19 05:21:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f725666e-7f56-3b8f-a5e5-506bd3eca60c | 4.50068 | -60.7763 | 2026-08-19 05:21:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5e03774-e324-3e1b-8900-725856447157 | 4.63468 | -60.53502 | 2026-08-19 05:21:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 43f70d14-4f44-389d-8018-d095a783ae76 | -7.55397 | -55.56388 | 2026-08-19 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 655f9cb1-88e4-3948-84d7-890db626cfde | -9.39206 | -48.24523 | 2026-08-19 05:23:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ae1cbfb7-7a2b-30a0-aa66-ff9aa0bd9d36 | -6.62746 | -59.08167 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56c19c50-fb2d-34e9-99e2-2e51874f77df | -6.99858 | -59.04373 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 772c5d87-4ffd-3ecd-bda0-a200d7197e0a | -6.70242 | -58.93929 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.5 |
| a7f233a7-21fb-3ef8-b160-cc3ef6da82e7 | -8.53814 | -54.74942 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 015b1239-efa5-3458-9533-54b30e4b7a20 | -6.6348 | -59.07907 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ac99465-fea4-39ff-92b9-597832121b33 | -1.26886 | -55.66505 | 2026-08-19 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cf3de639-15dd-3273-8bfa-e7c619bea6db | -8.49507 | -54.86549 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0667ee83-68a7-3ac7-a01f-7ce079859d17 | -9.39521 | -60.54877 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb1e6b07-1f1e-3227-a10c-8df8b43642c7 | -7.09959 | -55.45393 | 2026-08-19 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3eebfd18-64a6-3f16-995f-804dd1039120 | -7.557 | -55.57189 | 2026-08-19 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f099377-1361-388e-91c0-b2965e9697e4 | -6.74507 | -59.047 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ae3f60c6-c6c2-32f5-b874-513cad288c23 | -6.88849 | -59.05357 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 819a5407-1cc2-3b7b-a041-7e279eae5a82 | -6.90673 | -62.9039 | 2026-08-19 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 214d3375-dd04-323c-9027-67bc2f1596e2 | -8.5679 | -54.72887 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4bdc6719-50af-3c79-9c70-e0f4dfbaf100 | -6.65009 | -56.43049 | 2026-08-19 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4fdb738-a311-333b-8844-f6e8234dfae0 | -9.42757 | -60.44902 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e43c7f7-bc2a-3d7c-9a5f-fcf95fdf2256 | -6.84887 | -59.01072 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6bc04d7-26ea-3fbb-8559-e2067631ddc0 | -8.58085 | -54.70225 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README49.md)
