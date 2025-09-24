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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50b18e83-a42d-3f5f-95e5-35178fa90e10 | -11.6634 | -44.3405 | 2025-09-24 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 7b91b910-f663-39ee-a998-26ac0130378f | -11.6438 | -44.3668 | 2025-09-24 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 211.0 |
| c2ade3d4-386c-3d9a-93cb-7a08805c95de | -3.6241 | -43.0042 | 2025-09-24 14:40:00 | GOES-19 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| dcad430d-e2b0-3551-997b-5ae8b2bcd08f | -11.6442 | -44.3434 | 2025-09-24 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 184.1 |
| 94181dde-4643-3d0d-b7f5-305938698699 | -9.5787 | -47.534 | 2025-09-24 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 774353a4-46f0-3b9b-b843-18cec41867ea | -10.0128 | -46.2583 | 2025-09-24 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| fffc5b95-bcf0-3eb4-8fe8-837270645721 | -11.6446 | -44.32 | 2025-09-24 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 151.7 |
| 62194179-1942-3328-99f8-06fc30495b84 | -20.5648 | -57.1194 | 2025-09-24 14:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 6dba3f2f-9742-3c1a-b9c3-c47eb1918198 | -9.9938 | -46.2606 | 2025-09-24 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| c3eb6bcd-b6ba-3102-9232-5f957fd1e0ac | -20.5652 | -57.0984 | 2025-09-24 14:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 97.7 |
| d43f631e-98d0-323f-92e4-d16fd45010e5 | -17.951 | -55.8522 | 2025-09-24 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.4 |
| 3841a704-445c-3506-8433-60caf53108c4 | -20.5445 | -57.1224 | 2025-09-24 14:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 204.6 |
| 01dd4edc-4a9e-3cfd-9176-74c3ac0c24c4 | -17.9506 | -55.8731 | 2025-09-24 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.0 |
| 89ad9770-7779-3b12-bc6a-93836602c94d | -10.3382 | -46.0609 | 2025-09-24 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| a266135e-be95-3fb9-9088-474c84bdce53 | -6.1992 | -45.7961 | 2025-09-24 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 469f6f5f-bf6f-370b-9f7b-8766ee290597 | -11.6826 | -44.3376 | 2025-09-24 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 3951a986-a2ad-3b30-bbdb-2ddf1911d2d1 | -11.6818 | -44.3844 | 2025-09-24 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 130.5 |
| fe131f6b-bcba-3855-ab3b-7bd24b047710 | -12.1247 | -44.293 | 2025-09-24 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 4b0faa50-d59b-30f7-aa42-d74b0283e884 | -4.7974 | -43.5435 | 2025-09-24 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 03c35a74-7ca5-3828-a735-7bccc60ee55e | -10.9522 | -45.7096 | 2025-09-24 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 807b73ed-8c45-3672-b3d2-412471ce1466 | -3.7814 | -41.7196 | 2025-09-24 14:40:00 | GOES-19 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 286.1 |
| 06eec304-a714-3afb-a789-b25e5c63dbad | -4.8033 | -42.7725 | 2025-09-24 14:40:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 92.2 |
| ed515750-98fb-3ee9-9dfe-93c4ebe65d03 | -8.8417 | -46.187 | 2025-09-24 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| e4ed2c1e-c6ef-35cd-b5fe-07a6869ca706 | -4.7623 | -43.2434 | 2025-09-24 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |


