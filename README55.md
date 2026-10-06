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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d7535fe-6502-3bad-91f8-d3788b321667 | -3.06557 | -54.17677 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 2c46f9ea-4b94-3fe8-84d6-0e1720bc9503 | -3.04034 | -54.25837 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c352069b-eb53-3c5a-bd5d-be882eb257e9 | -3.10494 | -54.17472 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1dd2b753-b054-3735-a15e-75af791c1ac1 | -3.11295 | -53.76165 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bd5a90bc-7159-3ff9-83a7-66d43b4e990e | -3.07275 | -54.15743 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 445ce9e9-2fa7-3c86-9285-35cce6257520 | -2.7602 | -57.67061 | 2026-10-06 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f3b5d37-e3e0-373d-af55-21aa2f2b4984 | -3.50395 | -54.62907 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b92c1a0e-e11e-319d-9714-5e5c4661a60a | -3.14477 | -53.72753 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff307bab-49d5-3122-99c2-923a3692fd7f | -3.08831 | -53.71223 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d18174a-4887-34a7-b73b-3aa2b2527eb3 | -2.94196 | -54.13671 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8a973e7d-e6b9-352a-b9a1-1d474cad7738 | -3.10435 | -54.17869 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2035ee7-c7d9-323e-86c2-3bf04b681b4c | -3.50281 | -54.63657 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 9d90ffe3-0566-3f30-9c05-d4af3928cee7 | -3.12122 | -53.7607 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a3b0eb65-04a5-3251-8d13-f307d1577892 | 1.56055 | -55.97829 | 2026-10-06 05:23:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8f18fd64-4a1f-39b6-8afc-ca73e31f0966 | -3.05883 | -54.16354 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aed85435-4950-34f6-a26e-ef20450aa861 | -2.78838 | -51.67331 | 2026-10-06 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 47541a19-6976-3893-8bf1-2bddb43511f7 | -1.76746 | -55.03268 | 2026-10-06 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bcff396b-84b3-34c8-9055-36f61467842f | -3.95444 | -56.04924 | 2026-10-06 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f76d9bb-b607-3422-8cea-e15045d4c40e | -3.50508 | -54.6216 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f1efb25-f2fa-3a5f-911b-9a3b4e6287f4 | -3.32778 | -50.05231 | 2026-10-06 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3377c456-6246-3f37-be74-1dda0c5a6f09 | -3.23494 | -54.34587 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ca21e3b-6b32-3bfa-9fc8-2797fc925190 | -3.54124 | -59.48999 | 2026-10-06 05:23:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4d09341-652a-3f5b-bb3f-6932423b13cb | -2.55531 | -57.3904 | 2026-10-06 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| adbe858a-359f-38b6-974c-9f5d371a71e3 | -4.25635 | -50.79988 | 2026-10-06 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d60b003-d740-31d4-8c14-0fb72d795524 | 3.08076 | -60.56804 | 2026-10-06 05:23:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7858ce83-c9c7-39c5-a728-046682702a9e | -2.87056 | -54.14973 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c4cdd67a-f885-3498-a387-3781f0960850 | -3.2222 | -53.87608 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e4da624-46a3-3ea0-95fd-f8e96a6473fc | -3.68353 | -55.94149 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a8c51a9d-19be-30a8-9ad6-aecfc6e3e3ae | -3.8425 | -50.31176 | 2026-10-06 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0b684ee9-9277-326e-b8cc-7b7163a5b48a | -3.04535 | -54.22617 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba3c770e-0481-3d57-8c1c-6c331a58b06a | -3.84195 | -50.31544 | 2026-10-06 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 058a3e37-24ee-3f9a-b428-27f2df604016 | -3.50751 | -54.63351 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 79f005ae-18c8-352a-be9f-67c49af000fd | -2.7769 | -57.67707 | 2026-10-06 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b29f5a4-fb96-3a62-a413-b83da9c48223 | -2.85597 | -59.10672 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b919fbf9-b6ac-3f01-bd01-d9387a3b3e53 | -3.62982 | -55.28133 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 36b53f65-6a2b-3572-8525-d7f055e61723 | -2.87403 | -54.12634 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7955de26-5209-3a23-b57c-3691da49c98a | -2.78258 | -54.35859 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4c82371e-1e06-3d8b-b30a-b82d5e8d26ba | -2.90493 | -54.12304 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e1557e87-7a81-3a26-b2e1-9d61d444f9ab | -3.07464 | -54.17408 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4bdcaa06-0ecf-3c45-96d2-fc40d049bcba | -1.08953 | -54.12016 | 2026-10-06 05:23:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5fbf71e2-485f-3e50-97b1-9f24ceda17a2 | -3.18987 | -54.09669 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6f44998-218d-3318-a4e6-3fa5d36035cb | -7.05025 | -59.23336 | 2026-10-06 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 000c0157-c6bc-393a-98a5-314d6077923c | -3.51635 | -54.63107 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3cba19e3-8adb-311f-a2a9-8326dd0b65cd | -2.80347 | -54.13608 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c737e284-38db-3336-913f-4076b3c67030 | -3.90089 | -49.71541 | 2026-10-06 05:23:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d16fa58c-8d36-38be-82fa-8af7d4427cc1 | -3.13512 | -59.01745 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e8621cfc-eb9d-33f4-bb67-778b7de342d3 | -2.95876 | -54.10889 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3d376f72-379a-3f6f-abe2-4ff574119c1d | -3.11587 | -53.70784 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee6456e8-3d37-37b1-b6e9-a814d463b0a3 | -3.04958 | -54.22683 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ec00b17-d97b-33b3-b8e7-1677ae83d962 | -3.58731 | -54.30688 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9beead31-6680-3ad3-bb8f-e86316716d72 | -3.58305 | -54.30632 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e6113b55-3ab6-34e8-8516-e0812ec112b4 | -2.87479 | -54.15041 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 769159e9-b417-3cf7-a348-3b305f0f40d1 | -3.31998 | -53.85485 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55a58dd5-4eda-39a2-8603-402b140d70bf | -4.45737 | -47.92654 | 2026-10-06 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| aeb28056-f5e5-376b-96a0-17979488eef1 | -2.93407 | -54.13148 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c18adfa6-c860-3c5d-a263-87eb5bf237cb | -2.78888 | -51.66758 | 2026-10-06 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 064b5fd0-6967-38a3-b66d-6db2dd78d4a0 | -3.3272 | -50.05618 | 2026-10-06 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ca68e234-4f34-3200-98a9-63bee95aee8d | -2.7816 | -54.1084 | 2026-10-06 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dd2eeafb-fb0c-32cb-8e4b-caf7e384da0c | -3.08165 | -54.2438 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 9fab6fff-439e-363a-ad35-44da04d88367 | -1.61853 | -55.11438 | 2026-10-06 05:23:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 973cbdd2-3d4f-35f3-af3e-3d0127429154 | -3.10683 | -53.76707 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| fc4578c1-d9a4-36ce-88b7-05a16637933a | -3.05093 | -54.39271 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1578dcf-04f6-32fc-84b6-e0fe56c3b13f | -3.08737 | -54.17609 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89294578-d150-34ae-a537-070c3f97f37b | -3.06226 | -54.22878 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 93b6d7c8-0466-3c5a-8b7e-f9bdd5193403 | 1.79285 | -55.55854 | 2026-10-06 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 456299a7-2446-3182-9db1-3a612075e64f | -2.05355 | -56.88655 | 2026-10-06 05:23:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 36ede8a3-b3fa-331a-9934-9a7a89b5f1bd | -2.87959 | -54.14732 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c1de9295-8990-3286-bc5f-af8ecb519e2d | -3.49384 | -49.90343 | 2026-10-06 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| dc5488ac-2dd6-3847-a39a-f7398ce360fb | -2.88441 | -54.14406 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd557715-aeaf-396a-ad98-282f471f2479 | -2.95818 | -54.11282 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 37d9c704-e47a-3f68-804d-1cbfd19b1763 | -2.59669 | -57.54926 | 2026-10-06 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aca2861e-da6e-3548-8b47-5278476fd4d7 | -1.61361 | -55.11686 | 2026-10-06 05:23:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2e2c45b-28f9-38a5-896e-c959354746c6 | -8.27409 | -62.86764 | 2026-10-06 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6174659-0fd6-3126-956a-9afa9373b981 | 3.06539 | -60.58172 | 2026-10-06 05:23:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b4824f03-c114-3f12-85d2-43ddaf4eda78 | -4.28563 | -50.27335 | 2026-10-06 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83ddac23-4642-3c71-8cad-37012cc93e75 | -3.1001 | -54.17807 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b4282b73-e766-3e16-a885-6d7cad73139a | 1.72833 | -55.62746 | 2026-10-06 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37d16360-5e90-308d-ba7c-ea1d57946a1b | -3.50037 | -54.62468 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a790d09d-5d6c-3ea0-aa44-b9fb8d209ac0 | -2.93346 | -54.13545 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fadb70ac-6646-34e4-941f-fcc951dcbb5b | -3.01952 | -57.48915 | 2026-10-06 05:23:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b35a632e-8700-3c1d-a219-a048f8969acc | -3.17066 | -58.63265 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0dca6973-3dac-3d0a-b2eb-727401a87888 | -2.95632 | -59.1613 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ab4c3df9-baf8-3941-bc00-3b04e0a9d2fb | -2.57769 | -56.15557 | 2026-10-06 05:23:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0404782d-b3c6-3040-8ae7-c97005c465f0 | -3.09886 | -53.7313 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a62d2762-1511-32e3-97c8-8f7d7bf6987c | -2.33171 | -56.17079 | 2026-10-06 05:23:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b53caed1-25b4-339b-85a1-9f232a60cbc9 | -3.12837 | -53.7141 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2a7aaa66-bcae-35b0-b447-e0618e57b97e | -2.83982 | -54.06863 | 2026-10-06 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f353547d-dfb1-32b6-9eb2-0d84efcea588 | -2.52687 | -58.09224 | 2026-10-06 05:23:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 53fda35a-c51c-3491-836b-634c8c6aea44 | -3.62137 | -55.28343 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2999f35c-df95-3213-8034-d17b41787b51 | -3.58852 | -53.4747 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e8fe2869-5e3d-3d0d-be3f-7eb0901a533d | -2.79864 | -54.13937 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 521404cc-1667-3fc3-88f4-1e0fbdc25b83 | -2.15678 | -59.22497 | 2026-10-06 05:23:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fbe583a7-8cf2-3b24-9409-5a573e35bdde | -2.78343 | -51.66973 | 2026-10-06 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 95715ac0-5553-3363-9140-27a26ddd9676 | -8.59479 | -66.81358 | 2026-10-06 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c317e30-7d22-3c8c-a9a7-b8c49ca1ad7f | -3.36251 | -59.41595 | 2026-10-06 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41a0ecf9-7a58-3bdd-846b-c1dafd1b1723 | -2.95545 | -54.16116 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cf8011d7-78a5-3668-bc2c-6c9b4afb89ec | 1.86082 | -55.76752 | 2026-10-06 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e83dbe44-af36-3853-b2be-2c62ac6558d0 | -4.3358 | -50.40545 | 2026-10-06 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 04866228-9189-3b99-8dcb-b6040be28dd8 | -2.41904 | -56.53408 | 2026-10-06 05:23:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 574f3d3a-ce73-370c-a11f-5e6901488c9e | -3.05611 | -54.21171 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |


[Clique aqui para ver as próximas entradas](README56.md)
