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
| 2542908c-5eae-3527-9f1e-2fd2e58aed6a | -17.56078 | -50.44305 | 2026-02-18 04:50:00 | NOAA-20 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47ea7567-4e73-37cc-8fd6-a1dd65fdff47 | -15.47131 | -59.59268 | 2026-02-18 04:50:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13d01efe-d2de-3222-9bea-bf8dcfdaef8e | -20.23886 | -53.01347 | 2026-02-18 04:50:00 | NOAA-20 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ecff5d8-1990-3e32-a0aa-618f32052d34 | -14.51047 | -43.62298 | 2026-02-18 04:50:00 | NOAA-20 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e60a00ee-5f0c-3813-94ad-d18ee8e6b48a | -14.41291 | -44.59532 | 2026-02-18 04:50:00 | NOAA-20 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d4c9efa7-52a1-37e7-b298-a7a7d497b2bb | -18.44449 | -53.91425 | 2026-02-18 04:50:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30f72e7d-314b-3c0b-82a0-3461719ca8bc | -18.97061 | -52.92771 | 2026-02-18 04:50:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bff4da3b-fe01-37a2-a315-003f8e903412 | -15.8503 | -52.94039 | 2026-02-18 04:50:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 83227f38-dbf7-37d8-b71e-4d4a79d61ac2 | -15.1792 | -52.30092 | 2026-02-18 04:50:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1160fbca-3898-359d-a779-ceb2afeaf1dd | -15.85092 | -52.91474 | 2026-02-18 04:50:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f4058ea6-e8e6-3679-a993-8c6953a14f9f | -12.20873 | -57.79646 | 2026-02-18 04:50:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06fea87c-15d9-34d1-a270-f5825bc3a02a | -15.17865 | -52.30452 | 2026-02-18 04:50:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 476358fe-5e4b-3704-b71f-1d0b7af3e378 | -18.97396 | -52.92826 | 2026-02-18 04:50:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 818f4839-c540-3f74-bb1b-3489aa989311 | -14.51007 | -43.62629 | 2026-02-18 04:50:00 | NOAA-20 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7c9f086a-8540-319a-b5fb-55ade8dce7dd | -14.36061 | -44.56316 | 2026-02-18 04:50:00 | NOAA-20 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6463529e-87b8-3d75-8a16-f9bdfaafca47 | -18.80962 | -51.60427 | 2026-02-18 04:50:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e4d3a15e-0fac-3695-ad93-73947c68386d | -18.70404 | -54.98529 | 2026-02-18 04:50:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c743a40f-96bd-3d28-a833-677b97161641 | -13.4888 | -60.38247 | 2026-02-18 04:50:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf022776-c4d0-31a6-9a7d-0f7b44b4fa64 | -18.81252 | -51.60891 | 2026-02-18 04:50:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 56d5a926-5bfa-3126-a991-cf18091cca01 | -16.48221 | -43.76757 | 2026-02-18 04:50:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 924bbae9-93cb-3795-9a97-76aad5a7fe2a | -20.2499 | -52.72887 | 2026-02-18 04:50:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5553b096-f63a-302c-bee2-f02d6a7eef1e | -15.85148 | -52.91115 | 2026-02-18 04:50:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ab40c713-d0f6-3d55-8869-2419e1d53dde | -12.20999 | -57.78921 | 2026-02-18 04:50:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f49edee3-bcb3-3681-ad34-bd0426a961c6 | -26.98772 | -52.35989 | 2026-02-18 04:53:00 | NOAA-20 | XAVANTINA | SANTA CATARINA | Brasil | 4219606 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3d1bf2e9-b1b9-3907-873a-84f06b407de0 | -26.98733 | -52.35745 | 2026-02-18 04:53:00 | NOAA-20 | XAVANTINA | SANTA CATARINA | Brasil | 4219606 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b5e09eb5-9204-39b1-8bf6-f12cf2d338c1 | 2.6724 | -60.1453 | 2026-02-18 05:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 38fe757e-a16e-3808-a84c-bee16058a80f | 2.6724 | -60.1453 | 2026-02-18 05:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 55.7 |
| a30edfad-6b96-388a-96a3-dc4619ae6b3b | 2.6724 | -60.1453 | 2026-02-18 05:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 8e208370-e999-3520-bd3e-0f73f9cd31c3 | 2.6724 | -60.1453 | 2026-02-18 05:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 8e0f5ef7-b512-3504-90a5-e5e7c9bc81d8 | 4.01705 | -59.91293 | 2026-02-18 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00d56e7f-ac4c-347b-ba69-05c7ae969bf0 | 2.68774 | -60.20115 | 2026-02-18 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 598a52dc-49c3-339b-8b9c-df9734126985 | 4.27502 | -60.07801 | 2026-02-18 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a82fbed4-593d-31ed-8864-84aa33acce09 | 3.32109 | -61.06534 | 2026-02-18 05:33:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7afff2d-8662-3876-8910-be2fbdccfc23 | 4.60794 | -60.93269 | 2026-02-18 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2c7d23ca-6691-377e-95c1-45f792927e77 | 2.91451 | -60.82079 | 2026-02-18 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e37d8f5b-7e55-3a67-b7fd-050a8bce0ff4 | 2.66178 | -60.14611 | 2026-02-18 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 475d4072-79b3-31c2-9c18-18df8e0cd41f | 4.19528 | -60.45504 | 2026-02-18 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e584f4b8-bcec-3f04-8ca1-20ddf0728400 | 2.67922 | -60.14707 | 2026-02-18 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ead4e20e-48de-3269-b6bd-8b81426f812f | 2.66796 | -60.14143 | 2026-02-18 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6450cf80-cabd-3abb-85b4-019fcce162e8 | 4.23163 | -59.78329 | 2026-02-18 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1e72f19-11a7-3536-8db2-69aa42ac9643 | 4.27224 | -60.08213 | 2026-02-18 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b10dc55b-2e77-3c72-b7b4-6df6c3519eb3 | 2.68494 | -60.20527 | 2026-02-18 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f5aa419-14c8-3bad-ae16-42d477f02e30 | 4.18543 | -60.04822 | 2026-02-18 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20c1dab4-07a4-35fa-92d2-f83f57eecfa6 | 2.67247 | -60.14814 | 2026-02-18 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 16c4c200-75e0-3550-b170-3aa3a97142c5 | 1.06367 | -60.57073 | 2026-02-18 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d08b3c73-7285-312c-9715-ddcbe0dddcd6 | 2.67699 | -60.15483 | 2026-02-18 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d2cca5cc-438d-32fb-86ac-a4451295b448 | 4.05419 | -61.13988 | 2026-02-18 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ec69a26-704a-3519-a5f1-29fa1b76cf60 | 2.51505 | -60.98732 | 2026-02-18 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d4f01145-a03d-3a83-92fc-1b5896c3ec14 | 2.68327 | -60.21658 | 2026-02-18 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 487c833a-aa52-3bea-8c7c-0d84eaa301d1 | 2.67756 | -60.15844 | 2026-02-18 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c4016348-f881-36fc-9089-00e7d84600d2 | 2.56669 | -61.01082 | 2026-02-18 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f32bb66e-1581-3911-ae1d-311b535f20c7 | 2.66458 | -60.14197 | 2026-02-18 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| accdcb9c-9c5e-37b6-bf28-f12bfab5669c | 2.91397 | -60.8173 | 2026-02-18 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae749dfd-2f44-372b-8a08-5d42a09f4e69 | 4.05802 | -61.1428 | 2026-02-18 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e13b03cd-f862-3ad0-a05e-00b8832705d1 | 2.92392 | -60.81576 | 2026-02-18 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 70ea75e4-ecd0-3a75-9763-b35df82403e6 | 2.67585 | -60.1476 | 2026-02-18 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2eac08fc-278a-3f1f-a6bb-d9f7ee885b94 | 4.24846 | -59.75854 | 2026-02-18 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7d4af68-a71e-3adc-bdeb-764ad020239a | 4.16013 | -60.94309 | 2026-02-18 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2cc27ec4-3638-3259-a0f1-f73c5bf34766 | 2.67979 | -60.15069 | 2026-02-18 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2c8a35b8-3059-37fb-af48-98967264caf9 | 3.99296 | -59.80531 | 2026-02-18 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f904e75-b7e0-38a5-bbbc-993eb33aa6e7 | 2.41305 | -60.70642 | 2026-02-18 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b664d533-93fc-3621-80c5-683b5600d53b | 4.19195 | -60.45551 | 2026-02-18 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bb52f976-43a0-3bf6-9798-b127818ce142 | 4.47007 | -60.77075 | 2026-02-18 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dee3a1ea-c32b-34f4-8440-5e26f20eec6b | 2.6815 | -60.16151 | 2026-02-18 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 51e42530-c5d1-305d-80f7-93020305cc2b | 2.67812 | -60.16203 | 2026-02-18 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3ce2c7e8-95c0-381d-a36c-7a8edf836520 | 4.07942 | -61.12189 | 2026-02-18 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 860cd912-effe-3688-9067-b92120e43f37 | 3.95069 | -60.20181 | 2026-02-18 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee3ddd87-07b6-380e-9212-1b16ae10dda2 | 2.66853 | -60.14505 | 2026-02-18 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 03953747-7bd2-3539-bd31-217e8b896275 | 2.91728 | -60.81678 | 2026-02-18 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9972a078-9350-3b74-8cfa-184e7e144e22 | 4.14807 | -61.08648 | 2026-02-18 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 159ecd11-5cc6-3896-92bd-da04d523ca3e | 4.23105 | -59.77965 | 2026-02-18 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34c47799-4e83-39cc-b828-10166f228266 | 3.7441 | -59.7208 | 2026-02-18 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 06c7fc2f-19ff-37c9-a0b8-8edc4be894f7 | 2.91229 | -60.82827 | 2026-02-18 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7fd6cca1-9223-3899-b176-e7d373132772 | 2.6719 | -60.14452 | 2026-02-18 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 38778619-80fd-3c6e-98eb-afbc09093e46 | 2.67528 | -60.14399 | 2026-02-18 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 31f221f2-8df8-3142-99f3-7c2f48ca172b | 3.6849 | -60.91266 | 2026-02-18 05:33:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84c93dba-2602-3d57-8a4b-176364ccc581 | 4.38498 | -60.49323 | 2026-02-18 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f097b28-b51e-3642-9bb2-48c85af3b3b3 | 2.9112 | -60.8213 | 2026-02-18 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33d56d63-80ce-3ad5-9a62-063535daad58 | 4.05473 | -61.14331 | 2026-02-18 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1562f220-e4c3-38fd-8533-8a34480731da | 3.65388 | -60.30595 | 2026-02-18 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db97605e-2990-3831-9597-98c13241376f | 3.68821 | -60.91215 | 2026-02-18 05:33:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8d9f6a6-9691-304f-9803-672300a32300 | 2.67642 | -60.15122 | 2026-02-18 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 992c8736-2500-30a4-98a8-ac946c0fe4a4 | 3.22942 | -61.1961 | 2026-02-18 05:33:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99069117-45bb-3801-82a0-a8a21ead1560 | 3.95347 | -60.19779 | 2026-02-18 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4ca89c4-44eb-3f85-ae6d-aef9bac3b20f | 4.05365 | -61.13644 | 2026-02-18 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 399b8956-87d8-34be-83e7-7976f9fa64f3 | 4.27281 | -60.08568 | 2026-02-18 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 507db784-2e2c-3a78-832f-69cf524bd33b | 4.33948 | -61.19662 | 2026-02-18 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8537b64b-4fb2-3294-aab6-d2c0b2e18f96 | 2.9206 | -60.81627 | 2026-02-18 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2444f578-fd74-3e89-9a71-4b76e2a3ef0b | 4.01762 | -59.91651 | 2026-02-18 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc460dca-6dde-37b9-9089-485ce799bb08 | 3.11378 | -61.19703 | 2026-02-18 05:33:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dcf0110e-5c02-3da2-89f1-a86dbacc1176 | 2.68036 | -60.1543 | 2026-02-18 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| babbb10d-6854-3ffd-b270-079f49b1de42 | 4.50161 | -60.64923 | 2026-02-18 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2b2fb79c-ba4c-352b-8594-f038dafeef71 | 3.94734 | -60.20231 | 2026-02-18 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a81591c5-a077-3bcd-984c-3ae030a77651 | 4.17747 | -60.4073 | 2026-02-18 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0979e552-4017-345f-b958-25f34ac7a2ff | 4.05754 | -60.27488 | 2026-02-18 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e26a4a84-3507-30a6-8520-14259118a7d9 | -5.1481 | -60.37313 | 2026-02-18 05:35:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3d440da-3b2a-38a9-bcf8-2821e002e0e9 | -10.67048 | -59.37472 | 2026-02-18 05:37:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 43bc57d1-6c50-3f39-8abd-b9ce46efe9b6 | -10.73804 | -59.22164 | 2026-02-18 05:37:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6ce20a62-cdd9-3ea5-acb7-72a4e972412b | -10.74222 | -59.22219 | 2026-02-18 05:37:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4cd45993-71fc-385d-b566-6f065e2c7cac | -10.67459 | -59.37534 | 2026-02-18 05:37:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README7.md)
