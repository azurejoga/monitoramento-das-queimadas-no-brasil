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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26211c5c-17ee-3f72-a704-ab27b6793e9c | 0.87154 | -60.46818 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a17c7bcb-f39d-39b2-9821-2af353923653 | 0.23426 | -60.51685 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b288f1d4-a5a3-3728-8045-44fae9d9e2bb | 1.51087 | -59.92872 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 998538a6-e334-33c7-9879-7cff0abe9491 | 0.45778 | -60.39253 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3af0e8fe-77fd-3f3c-b086-cb49d800fbef | 1.49828 | -59.91725 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc374930-976c-385f-888e-3da44fee17d0 | 0.17518 | -59.42866 | 2026-03-03 04:53:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b2eb6fc-da8f-3d03-9ddd-cae886bc2fcf | 1.48619 | -59.90898 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 593e0af4-9375-380f-ba32-18565d21dd84 | 1.48771 | -59.91889 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fa3abc14-fafb-3ef4-9b12-4737c2de5554 | 0.63012 | -60.56074 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6f1743d-92f0-3aca-ac73-b602e4161bd0 | 1.36023 | -60.06346 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7bf9644c-7133-33d0-a216-20fb9082be50 | 0.96469 | -60.52993 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95ba73ba-c3af-398d-8662-12c5507b1b16 | 0.06165 | -60.97444 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d1c8a7e4-f3c1-33fb-83b8-73c5214ffafd | 0.091 | -60.62238 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dc717587-4d71-3440-a4d4-2652965324fa | 0.87562 | -60.47107 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25fa148e-6759-3d00-b08e-203cdd7c723b | 1.4925 | -59.91483 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2f05dac-b9a5-3e52-b466-644d76cdcb8a | -0.15603 | -60.74819 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef29836c-3b84-3a94-8841-e1b9d78f0b32 | 1.50148 | -59.90298 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 678f9945-91d3-377e-8a33-0b64ffac2071 | 0.96414 | -60.52638 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 099311d9-ae12-32fd-a87e-aa2589b13c7d | 1.47285 | -59.9278 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd794797-511b-3318-8e45-0e0c6c6bb559 | 1.45813 | -60.0717 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 586b4f89-2cbd-3136-97ac-468e2566d28c | 0.92511 | -59.55853 | 2026-03-03 04:53:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c4b5f3a-3588-3813-823e-d9ab91c7da04 | 1.49776 | -59.91391 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e23c5953-3e7b-3cd7-9d10-aa5900e3f7ea | 1.11501 | -59.19576 | 2026-03-03 04:53:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8fd805af-0b64-3fc3-86ab-445007c2647f | 1.50251 | -59.90965 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7563173f-b5a9-3003-85d4-0e8b45e8a282 | 1.11589 | -59.20154 | 2026-03-03 04:53:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0465499a-0460-3df9-bd2f-a6e628654102 | 0.05607 | -60.97514 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cee36628-1a0e-3a05-bbbc-aa3b75e65bf7 | 0.69889 | -59.96985 | 2026-03-03 04:53:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f9e4ea97-e625-3091-aa44-5c3c2da8f732 | 0.99886 | -60.41674 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 48334a51-e464-3c62-946d-661b143383ae | 0.87452 | -60.46415 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b8f388f-2d2a-369d-8f4e-dce3263b79f4 | 1.12745 | -60.51796 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2c897a26-3284-35ac-aaf6-ead652a2e802 | 0.45241 | -60.39335 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2fcb5673-47b1-3cbc-897e-ce9347017be7 | 0.45831 | -60.39595 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 654ba9ec-74e3-33d3-bf99-faabea0705fb | 0.09155 | -60.62585 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8eb92cc1-e937-3608-8e30-4299f1dd5b06 | 1.55512 | -60.28624 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8575b97-3320-34ef-b6f9-be2b7a102907 | 0.08558 | -60.62323 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 25bf2b2b-8e7b-33f1-9fd8-ee9767ddba82 | 0.76933 | -60.47867 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9948bf2-f4df-3af7-9c9f-66f954b38444 | 0.08612 | -60.62669 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 317b26f5-1e51-397f-a578-a18eae10f74d | 0.49317 | -60.514 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c165248c-e732-3866-bba5-3dff25bb9ebf | 1.50712 | -59.93949 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab1a8d95-dfaa-3bd1-be25-cda1e8983151 | 1.50983 | -59.92202 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2d9deff7-8df0-32dc-8864-88a4436a03ea | 1.54917 | -60.28364 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 742c4a38-f077-3d9f-be6d-e16a31c082b6 | 0.17551 | -59.42985 | 2026-03-03 04:53:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34f59ff2-64c9-34a9-8ff8-e310b6fc1498 | 1.50878 | -59.91524 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cdded735-d317-3d0e-a83d-b68fa9d28815 | 0.69928 | -59.9704 | 2026-03-03 04:53:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d88c7d1-2ef7-340a-a067-4f587f2b9333 | 1.48388 | -59.92916 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e3f25745-354e-34c7-99fd-670a9f78cc27 | 1.50554 | -59.92924 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da2b1f51-df55-3465-a3bd-a8c3504d2309 | 0.49695 | -60.50266 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 631dcfda-7219-3d13-ade4-b32b453205dd | 1.35489 | -60.06421 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c37d408-1e88-3300-a366-ffde54b722ce | 1.50826 | -59.91188 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d0cbf971-827c-30a9-8a93-86bc6a334eaf | 1.54971 | -60.28711 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbab3a10-7db2-3cbe-8435-8b59b516b446 | 0.23175 | -60.51744 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82200d9f-2cb4-3c67-9b30-faf4a7892894 | 0.70452 | -59.96956 | 2026-03-03 04:53:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65dad03b-e03a-3ff0-a2b2-3732157d2c96 | 1.502 | -59.90633 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fb3ba8a4-3fb6-3b81-890b-ac45620cefe1 | 1.35547 | -60.03344 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4232902c-5536-3d4d-9ed3-38cef9e71039 | 1.49725 | -59.91059 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f164372b-35fe-32da-9c4a-254a6181f829 | 0.49155 | -60.50356 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ba41bc6-f564-3978-8ba5-4f18797667a3 | 0.87101 | -60.46471 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b332e6cd-3a78-354a-8717-5f78fa00eb72 | 1.50302 | -59.91298 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 69a04bf8-917b-31d4-8db6-31793c48af63 | 0.05905 | -60.99388 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb295614-2d3c-3a35-a5be-d90b272c254c | 0.49263 | -60.5105 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 68fe280f-9c49-384c-9748-182cd5a19307 | 0.94264 | -60.18069 | 2026-03-03 04:53:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 90407ae1-d7c0-30d2-83c0-3cb3911a8ffd | 1.11094 | -59.56942 | 2026-03-03 04:53:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c8e4225-2ab5-3550-b79b-b6b2b4b9934d | 0.49641 | -60.49918 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3836d0c0-ef75-3cf5-8fd3-abe5340f561a | 1.49198 | -59.9115 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e865fd52-785d-37d2-9d44-a27b7e53cea5 | 0.87507 | -60.4676 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 177d12ac-6326-3f33-a9a0-73ee62d47d52 | 1.47236 | -59.92456 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f90432e-3110-3b1b-a6b5-6dcf332532e1 | -1.51555 | -54.52519 | 2026-03-03 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ebf1d69-cbfa-3a9f-8166-2b2675143c5d | 1.48744 | -59.95244 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ab88dcb1-af20-30c0-bec3-0da36bc6c56f | 1.51455 | -59.91758 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37c3b397-6833-310a-8503-477d940d7eab | 1.50931 | -59.91866 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 84de8f7a-38ba-3a7f-8d04-a54adf254282 | 0.69838 | -59.96668 | 2026-03-03 04:53:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bcf98eed-e2a6-309b-8be1-269f7f9fb043 | 0.49209 | -60.50703 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0806a7c7-2bf4-38f4-9e38-3cd2b83f00d5 | 0.56631 | -59.90836 | 2026-03-03 04:53:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01da7598-0f03-3346-b396-4aaaf80ce935 | 1.51191 | -59.93546 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 667a41bf-51b1-3bf3-8db9-f4326dee275b | 0.76878 | -60.47523 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14116f67-7b4f-389c-91d5-bbfbbdc7a901 | 0.56532 | -59.90928 | 2026-03-03 04:53:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f368f8a9-b02f-3a0e-b985-f4a8ba3c8baa | 0.30602 | -60.44624 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8e04a2cd-9335-37a2-b2b4-c6e85582d2e4 | 1.493 | -59.91811 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a99d81db-3155-384f-be23-604281497535 | 1.47761 | -59.92352 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91372f31-ff59-38b2-a658-da6e3c01db91 | 1.51035 | -59.92535 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 435c2216-20f6-3632-96ee-de1f912b963f | 0.23118 | -60.5139 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9cb6c047-b802-3b30-b3cf-64a365ce02f1 | 1.13292 | -60.51712 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5fea6ed-6c2f-37c2-b233-2d49eee7e225 | 0.6988 | -59.96722 | 2026-03-03 04:53:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4278fb57-b181-3c8d-99a9-6a3f67f5da76 | 1.51139 | -59.93209 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 216fdbdb-db41-3a7e-bce9-9bb1b4841775 | 1.48672 | -59.91241 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 18082334-380b-3834-bb90-adbdd2f44a98 | 1.55459 | -60.28277 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41198583-fe80-3fbe-b687-b4570f0999b6 | 0.77079 | -60.47626 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cacdd3ab-831a-334b-8c08-658cc7caf493 | 1.11529 | -59.20016 | 2026-03-03 04:53:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81f9d983-ffe5-33ef-bf9c-58cc9cbbff18 | 0.49587 | -60.49572 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f97ebaf-8abc-3a00-bed8-c0d642562218 | 0.86964 | -60.46843 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c8ea90d-eb46-3c4f-8950-7008c4f408f3 | 0.31085 | -60.44199 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fadfc648-70e3-3185-8357-d244cce41f55 | 1.50354 | -59.91632 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f9a691da-b79b-370a-a039-c5b1f498a24b | 1.35864 | -60.05345 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41394a96-c070-3e9f-9ae5-4bf0061d7e33 | 1.50406 | -59.91966 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9d9efc03-b51a-3942-a1bf-3e85de5ae3cd | -21.7078 | -48.43189 | 2026-03-03 04:55:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9162a729-ac14-3360-8dea-4c5617611fde | -17.5285 | -53.70091 | 2026-03-03 04:55:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 51be0e53-9d1f-3924-9359-aecfb60dc954 | -18.80469 | -57.64414 | 2026-03-03 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 850911d0-959c-3ca8-bfb0-435d476c222e | -18.8109 | -51.60568 | 2026-03-03 04:55:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f347fad-da0f-326f-a7a6-0fc932c18196 | -21.12459 | -48.65331 | 2026-03-03 04:55:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d87387e5-16d0-315f-b4ea-423434a9f0f7 | -18.8081 | -57.64477 | 2026-03-03 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |


[Clique aqui para ver as próximas entradas](README5.md)
