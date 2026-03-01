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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ddb0102-dda8-33b7-809a-0bf93f467ee4 | 3.87564 | -59.63797 | 2026-03-01 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a3091c9-ae4e-3115-9002-0275fe478df6 | 3.08283 | -60.44773 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e66208e-a318-3155-9fc2-dfd414905c77 | 3.08139 | -60.02348 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 96aa3fe8-f1cf-3c54-aa69-eaaa4e6a50cc | 3.93379 | -59.98676 | 2026-03-01 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6049984d-58a7-38ea-ae5b-fd550a19f219 | 1.48232 | -59.92488 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 75e77a29-0a53-3d07-9fb6-07797994149d | 1.50811 | -59.93847 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 932fdd5b-d22e-37f0-9461-4b034e4864fa | 1.0899 | -59.24789 | 2026-03-01 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bce768e1-9b06-35fe-8c26-1b3c3e10bb47 | 1.85188 | -60.8488 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35365373-f80e-3e7f-9280-f02c26a4f663 | 1.72944 | -60.3908 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 308a6046-6caf-34b2-87a4-e8c966e6a05d | 0.94286 | -60.02322 | 2026-03-01 05:29:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e940f0e-c983-3c8f-a611-d25072ba040e | 2.82109 | -60.77763 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d71553d-a715-3a32-8826-a6f7e6a0534b | 0.46975 | -60.39318 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74508c70-e203-3722-b785-326a1e29da68 | 3.45103 | -60.82073 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c79347ed-867d-3649-b1f4-029e0e1aee97 | 2.82494 | -60.78057 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 44079252-3b30-328c-98bc-6e53a2fd2fbb | 0.47028 | -60.39661 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 358ed3ce-2cb2-3919-9179-c8ab6c33cac7 | 1.48838 | -59.92039 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 722c7fc7-3efa-377e-88d6-526aadc63b5b | 1.49714 | -59.93314 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 435ec400-9950-398a-9814-65a5d47c2499 | 0.08058 | -60.64701 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 447a9684-664c-31c8-91ba-37e53946cb48 | 1.02348 | -59.79897 | 2026-03-01 05:29:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8432130-a061-392f-9f61-bc3467b0b038 | 1.4768 | -59.93277 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba5f5fb6-5df9-3c6a-8949-40bd652718c1 | 1.46912 | -59.92689 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| cf32fe56-9e21-3303-a4fa-58d475cac4b2 | 0.1885 | -60.4409 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b65130d-05cb-39e0-9e5b-97deb3394261 | 1.4801 | -59.93227 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b11ba3a1-f7ab-31d4-8ded-3dd369d12f12 | 3.44501 | -60.80389 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e725812-9243-3f38-ac09-8ce2cdcb4ff0 | 3.9354 | -59.997 | 2026-03-01 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f092e83-b6ca-344c-a52f-cf6486f7ab37 | 2.9069 | -60.42987 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b79e8835-031e-3786-b677-67a5f7b2e0a1 | 1.49498 | -59.91937 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.8 |
| e30768bc-9388-39dc-8468-0f463370b221 | 1.20721 | -60.62036 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9162063e-b012-3407-85a4-b82a29371917 | 2.11363 | -60.80043 | 2026-03-01 05:29:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47080f75-04fa-3469-b18e-8f028b03af9e | 1.86032 | -60.40194 | 2026-03-01 05:29:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41c30892-3508-3bf9-8dde-d8a337b0a49a | 0.93992 | -60.26263 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4698ed82-61e3-33af-9e8f-6b9528c27295 | 2.01328 | -60.53173 | 2026-03-01 05:29:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 879764c3-8a4c-31c0-8713-a9f793c2ebe2 | 4.44584 | -60.73959 | 2026-03-01 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 584e2f81-57d0-3937-bc8a-d982fee83b99 | 3.15411 | -59.92102 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 768071db-5fd7-36ca-81b1-f9f8b937567b | 1.5065 | -59.92817 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 50b59968-c701-3308-a2d8-deb7b73487a2 | 3.48589 | -60.78342 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfef4751-5412-36da-804e-ec36086e8bbd | 0.97329 | -60.60419 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f21c3389-0b18-3416-af5e-480db3cb1a0a | 4.08432 | -59.88614 | 2026-03-01 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2d29fe5-f442-3702-b57c-34717f34af2a | 2.62198 | -60.61123 | 2026-03-01 05:29:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de3a75bb-6c7d-3192-84c6-94afd92a3595 | 0.89594 | -60.09033 | 2026-03-01 05:29:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb522775-9fbb-3d1f-9fef-730069a7aaed | 3.05837 | -60.68031 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c0ffb70-eed6-35df-911a-73bf41ad4a47 | 1.50374 | -59.93213 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04bd42d4-54b2-3659-8f01-adb28d901198 | 0.09544 | -60.6342 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d4562bbb-3f0c-333d-a9a3-c38130e2dbbf | 0.96251 | -60.2346 | 2026-03-01 05:29:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b46ee5e0-de2f-31b3-abc6-4ecd4770eeab | 3.44778 | -60.79991 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d71fba20-44c5-38ba-aaea-7e82b005da7f | 3.1574 | -59.92051 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aaf59811-a5f7-3c38-9292-0e0d25f12861 | 4.29618 | -60.06287 | 2026-03-01 05:29:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 21b79e16-b172-3512-ab00-0a11073094f8 | 1.50535 | -59.94241 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d21d231b-bb81-33ba-b725-c2849e46663c | 4.1739 | -60.30744 | 2026-03-01 05:29:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e9a1c84-3c34-3b43-acc3-c4add0f643b9 | 1.07718 | -59.25018 | 2026-03-01 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4b31b78c-6ef8-3fa4-9903-5b7192807888 | 0.99858 | -59.59658 | 2026-03-01 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf348a1d-fe79-37ef-9a67-c75d67404bff | 1.87533 | -60.91209 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ba82d836-86a8-38e5-b0cf-3a1b32b3c21d | 1.08655 | -59.24841 | 2026-03-01 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e298e79-3116-306d-bfa0-55f8f30648b0 | 1.51141 | -59.93795 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 53e3ea9d-c0ca-3551-ac81-4cc5aac33a6a | 1.50158 | -59.91835 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 8226d3d8-d8dc-3bee-a811-e4031922b962 | 2.90575 | -60.4441 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f7c2f21-dfd7-38b6-8007-2db7e31e7fb1 | 3.48975 | -60.78638 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4440e3f-2c7d-3c72-b4aa-a85b0fb66b91 | 3.05507 | -60.68081 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e56a236a-087c-3bde-ac34-feb04a81f22a | 0.6477 | -60.3753 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4bb5dae-fd9f-3e90-a97b-aa034dd2956c | 1.06101 | -59.25632 | 2026-03-01 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3df011f0-4fc5-3725-a0c6-672a6c40c000 | 1.47518 | -59.92244 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 8b585f39-062e-3f0b-8181-9055397df36f | 0.64631 | -59.65151 | 2026-03-01 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79ab3b31-b4aa-306b-81ae-c2237db2ebaf | 3.99473 | -60.11758 | 2026-03-01 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c774826-d258-30f4-a034-3216c7d0b4bd | 1.07439 | -59.25424 | 2026-03-01 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed763c34-ccbe-333a-8e50-12468ca05e8c | 0.5677 | -59.90901 | 2026-03-01 05:29:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 434e5111-f0ab-3289-9781-4b877863daa5 | 1.48892 | -59.92384 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 57ca58d1-f054-3613-88c6-1609321d3840 | 1.02345 | -60.53694 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c5591879-6a65-36dc-b048-f62b55055baf | 1.51033 | -59.93108 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 275ece38-3a0d-32be-9cf2-7a28d2b51bce | 0.87307 | -60.48745 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30cbac85-4216-34f1-aab2-70bd240d8882 | 1.36542 | -60.30453 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 65e052bf-4240-3616-bbd5-cd52f7ba491e | 1.51087 | -59.93451 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5bb03f45-31fe-349b-ad6a-971134adaaed | 0.57432 | -59.90798 | 2026-03-01 05:29:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a31df812-c5c3-3f23-b89e-71fb1d40a288 | 0.8569 | -60.4059 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6891d153-da21-3fd2-a77d-dae162b1558c | 1.47956 | -59.92883 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c67404f1-3371-3010-8fca-2d560a89a6e3 | 2.11466 | -60.19714 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ba71c59-bd2a-3034-9a59-e022f58ee07a | 1.47572 | -59.9259 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.9 |
| d520ea3d-0c1c-3c3c-acc4-67e1ca0e3804 | 1.48448 | -59.93863 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e368bfe-c85f-3dc8-bd58-dd0eed527ccc | 4.12903 | -61.06608 | 2026-03-01 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f91a676-62dc-387f-90db-f7052ddef37e | 3.44278 | -60.81134 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89581ad5-1bbd-3521-8deb-27d8540d1586 | 4.2504 | -60.81747 | 2026-03-01 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| df80b12e-3e61-38e3-993b-98f8574d16fe | 1.49114 | -59.91644 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 90b34d6e-6fe9-3274-8c80-38f67e0d5e31 | 1.03247 | -59.46628 | 2026-03-01 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 95592807-0e68-3879-865c-1e821e8ada70 | 0.55292 | -59.85814 | 2026-03-01 05:29:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04b43ae8-730b-3432-8e6f-609a9e984b98 | 1.49606 | -59.92625 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e186ee6-1ec3-3cc2-9a8f-79c74bb71a3c | 1.69052 | -60.22876 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb460e96-28da-3e41-b78f-b027da3a2c8a | 3.44886 | -60.80685 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5a820e78-5102-3302-b615-e7b6143f8854 | 1.4063 | -60.7431 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48cf449e-9ca9-326c-9d7e-49c325b56bd8 | 1.93407 | -60.80787 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7e26d6c3-3834-3376-b43e-887ce8ffe04d | 1.47788 | -59.93964 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0df43d91-c178-3189-a0db-b0878e202a96 | 2.91073 | -60.43279 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 88077827-af4f-3d8f-ae65-5feef87100cf | 0.07453 | -60.65144 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f788728f-5f6c-30d9-8929-bebd4aea4322 | 1.40354 | -60.74703 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47e67a27-2d4a-3e1e-9e57-9fba5e31672c | 1.4999 | -59.92919 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc5c8dda-779c-3593-9288-1564c3e1284d | 1.06381 | -59.25226 | 2026-03-01 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6f005890-4646-329d-98a0-a4875af300c0 | 0.88898 | -59.78775 | 2026-03-01 05:29:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2e17e8d3-3a33-35f8-819a-98fb49b3a13d | 0.14485 | -60.40562 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb008e62-5bcc-3204-ab9b-488a8ef0ad9e | 0.6973 | -60.0408 | 2026-03-01 05:29:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6801af49-da75-3f4f-8ba8-a3d0c9f3621b | 1.1774 | -60.36588 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d0e6cdce-0ac1-32d4-8e68-7f37bd30aefa | 1.47566 | -59.94703 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b719a4d-cd93-3091-bdd7-7168d0f42be1 | 1.07986 | -59.24944 | 2026-03-01 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README7.md)
