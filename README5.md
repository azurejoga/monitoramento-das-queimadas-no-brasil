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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b897349-42c1-3509-ba1d-e17070255e41 | 1.9238 | -60.2879 | 2026-03-25 04:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 27ee7cc5-9f99-3243-835b-4f713c36f391 | 2.7065 | -61.3384 | 2026-03-25 04:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 56aa8830-c25b-3222-aace-123ed211f75c | 0.8119 | -59.3438 | 2026-03-25 04:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 7f72072e-efb2-324b-80a8-5654eca5be70 | 0.8301 | -59.3437 | 2026-03-25 04:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 66.9 |
| becbb94c-5799-3bef-a0e7-32d46e2c84e8 | 0.8301 | -59.3628 | 2026-03-25 04:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 54.9 |
| fc8e2f37-0b4c-31c6-820c-5e2527832e7b | 2.7248 | -61.3382 | 2026-03-25 04:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 49.5 |
| f9779f8d-9924-33d5-baf6-da2866da77b1 | 0.8119 | -59.3629 | 2026-03-25 04:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 103a7795-9d44-328c-99d5-b3dafddd9615 | 0.8119 | -59.3246 | 2026-03-25 04:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 7329847f-7b9d-39dc-b529-11c4706d4565 | 1.9238 | -60.2689 | 2026-03-25 04:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 44.9 |
| cfd688a0-b6e4-35ee-8686-7f62ce9007fb | 2.67454 | -60.24178 | 2026-03-25 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7233b14-81a1-345c-be89-c2eba56e24e1 | 0.81734 | -59.35308 | 2026-03-25 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 1708cd87-130f-3cc2-b551-fea917f872ab | 0.80848 | -59.36659 | 2026-03-25 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ded2915e-62ff-3fda-9d16-b32ae9b5dded | 2.6813 | -60.24079 | 2026-03-25 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2684c8bd-2252-3672-8e77-a9f469adbfc9 | 0.97929 | -59.3792 | 2026-03-25 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43d8d420-5591-31ae-b821-52dc736229d9 | 0.81157 | -59.34605 | 2026-03-25 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 8de7a8ad-a756-3644-b62b-4b9713cadf77 | 0.81236 | -59.35095 | 2026-03-25 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 15.9 |
| a30aeabb-c5b1-33a4-946e-28f77c357324 | 0.81552 | -59.37054 | 2026-03-25 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e9bbf833-755b-3637-bb97-a0f4bf1c978a | 0.81394 | -59.36076 | 2026-03-25 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 12.8 |
| ad658809-45a1-3081-8184-d5bc1bddf6ff | 0.81473 | -59.36565 | 2026-03-25 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1cffd184-7158-383e-a4c2-44519807742c | 0.81336 | -59.36876 | 2026-03-25 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 4d560501-2266-33af-81b8-499e41693e3b | 0.98633 | -59.38322 | 2026-03-25 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf84839e-0bef-3fe0-b753-4d61a8e23ce5 | 0.8181 | -59.358 | 2026-03-25 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 8fe91692-54e4-39d2-b9a7-e234b841fda5 | 0.82435 | -59.3571 | 2026-03-25 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 113040fc-0da3-3681-a419-8e394c47bde7 | -1.48565 | -55.27967 | 2026-03-25 04:38:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| baf69e00-7b1a-35df-9988-77808c44aef3 | 0.81583 | -59.34328 | 2026-03-25 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 36266139-4ed8-3e87-b709-7ce42a3ee958 | 0.81961 | -59.36784 | 2026-03-25 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 75de1a1a-8e73-3793-a658-76046c97ab28 | 0.80959 | -59.34424 | 2026-03-25 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 1cde1e2a-4c69-335f-9638-debc1b5b7b62 | 0.82588 | -59.367 | 2026-03-25 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3ab6078b-1059-3659-b6aa-978fb52fb538 | 0.81658 | -59.34817 | 2026-03-25 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 16.1 |
| d0afb2b4-cd0e-38c9-a097-c4221433d6cb | 0.80636 | -59.36483 | 2026-03-25 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 404be216-d14b-3dab-ae32-04cf35991534 | 0.81034 | -59.34915 | 2026-03-25 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 9c4f1223-f513-3e13-be71-a6ecda1d219d | 0.82511 | -59.36203 | 2026-03-25 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3e9a6ac2-69da-34d6-9b9e-f71e07640d08 | 1.92033 | -60.28219 | 2026-03-25 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 12.2 |
| f24c7102-1cb3-3e67-94b8-86221af0c37f | 0.81315 | -59.35585 | 2026-03-25 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 7275a96f-1fd4-3aae-8a86-017f2fce10ef | 0.81885 | -59.36292 | 2026-03-25 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 12.4 |
| f6cd6e3a-87ee-3bbf-a2f3-fa165b8b8e28 | 0.81185 | -59.35897 | 2026-03-25 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 7100dc0e-a983-3235-ae70-317c1dd34b6c | 0.80711 | -59.36975 | 2026-03-25 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f58afa47-e425-3217-a362-9b7969d48e47 | 0.8111 | -59.35407 | 2026-03-25 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 08943efd-791b-31e6-b4f5-10db5c4561e3 | 0.81079 | -59.34118 | 2026-03-25 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 12.0 |
| beab86fa-10cd-3dd3-a391-cf3d5f5ba027 | 0.80927 | -59.37148 | 2026-03-25 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4130f707-7cc3-31e0-a83e-32bb21aaeedf | 0.83138 | -59.36118 | 2026-03-25 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 41c874b9-4a86-3b51-9460-54983c4afb41 | 0.81261 | -59.36388 | 2026-03-25 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 12.4 |
| fb2367bd-eb98-30dc-b3a8-e3a6f8f2ad31 | 2.7247 | -61.3571 | 2026-03-25 04:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 45.8 |
| a777c61d-50a7-3408-8251-d17eb4c88d74 | -3.18711 | -52.88288 | 2026-03-25 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 520bd597-0420-3576-b929-cc0151dfd0b3 | -1.77099 | -54.02803 | 2026-03-25 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 00f2753c-57e2-3108-97a7-acf8a8138240 | -3.48911 | -52.57454 | 2026-03-25 04:40:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6858d5fe-f6e5-3b12-90a4-a3c2727d2a43 | -1.77214 | -54.02762 | 2026-03-25 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b6f92ad-ed43-39a5-bcb5-28f5a09014bb | -16.62635 | -49.19328 | 2026-03-25 04:42:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef125bd7-4f68-3b14-91ad-3929358e9d02 | -16.00007 | -51.20425 | 2026-03-25 04:42:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f0b4323-9b43-31cb-a13e-75a4715e2a7f | -22.06638 | -46.85062 | 2026-03-25 04:44:00 | NOAA-21 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88e5e5fe-bb77-30ed-aaa7-44af1657e183 | -22.06589 | -46.85489 | 2026-03-25 04:44:00 | NOAA-21 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41111c81-5bbb-30c8-85a1-a04d271afe09 | -21.49148 | -48.76855 | 2026-03-25 04:44:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4bbfec37-b36d-38ea-bdea-3772f471c9a6 | -22.33706 | -47.18523 | 2026-03-25 04:44:00 | NOAA-21 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cf5cd269-4e68-3ee0-bfe8-3b22704094e4 | -21.53129 | -48.63852 | 2026-03-25 04:44:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e24e6241-2a94-39e2-8dbb-941e4c736637 | -22.06161 | -46.85431 | 2026-03-25 04:44:00 | NOAA-21 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57302d28-0d83-3383-bb31-3fd25650e4d3 | -21.58756 | -48.85773 | 2026-03-25 04:44:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ebfd4eb0-1c86-3816-ba4f-9dda7473f45e | -22.06316 | -46.85269 | 2026-03-25 04:44:00 | NOAA-21 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2037d550-8a50-349f-9185-5ffb5821de19 | -22.0621 | -46.85005 | 2026-03-25 04:44:00 | NOAA-21 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c3980f4-3e6d-3925-a7df-308e28b7bb9d | -22.34126 | -47.18587 | 2026-03-25 04:44:00 | NOAA-21 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a7094174-b809-3483-b19b-e41f607ce659 | -23.17581 | -46.47031 | 2026-03-25 04:44:00 | NOAA-21 | BOM JESUS DOS PERDÕES | SÃO PAULO | Brasil | 3507100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e85fc9b2-7f95-37f1-81e3-a7107a46aac5 | -22.3361 | -47.18737 | 2026-03-25 04:44:00 | NOAA-21 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b46b5f43-83d9-33bf-a9e8-990e40de6029 | -23.17282 | -46.46842 | 2026-03-25 04:44:00 | NOAA-21 | BOM JESUS DOS PERDÕES | SÃO PAULO | Brasil | 3507100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5f3d5d99-920c-3fd6-a1d4-9b0c44eb51bc | -23.02385 | -48.44759 | 2026-03-25 04:44:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 20299e9d-5687-3826-8b45-8f29846246be | -21.58767 | -48.85955 | 2026-03-25 04:44:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6d6b033c-6bbf-366c-86a4-1aade52c1217 | -22.3403 | -47.188 | 2026-03-25 04:44:00 | NOAA-21 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 513dc166-469c-3235-8701-0b499fb2d7df | -21.49161 | -48.76714 | 2026-03-25 04:44:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2de124d7-b06e-3fd5-8a63-97186de17657 | -27.45741 | -48.45383 | 2026-03-25 04:46:00 | NOAA-21 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6c6e1002-8af7-3cec-b1d7-e081f2eb3220 | 2.71488 | -61.36273 | 2026-03-25 05:08:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f33551c3-3a90-3075-8483-2317136a1a99 | 1.95094 | -60.90993 | 2026-03-25 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4be22993-82f4-36ea-91e4-2c05f7cb5197 | 3.77118 | -60.76431 | 2026-03-25 05:08:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a39d2868-cbc0-3a21-9ce2-2dea7a94ad37 | 2.71407 | -61.35745 | 2026-03-25 05:08:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9a2ea4ca-9b68-3683-b6ff-a453095c5f91 | 2.72457 | -61.3612 | 2026-03-25 05:08:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8167ee28-b9b9-31d4-bba4-284d0f435d2b | 1.94552 | -60.90577 | 2026-03-25 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e31e988b-e61f-3bac-8188-affeb3f529f8 | 1.69167 | -60.35872 | 2026-03-25 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b75965ed-72e8-31ca-92a2-f878dd814edb | 2.11724 | -59.85684 | 2026-03-25 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c50b10eb-1882-382d-9bf0-d772fdc48745 | 3.93045 | -61.29094 | 2026-03-25 05:08:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe25220d-a9b4-3988-94ef-4baadb1d3044 | 1.94164 | -60.91129 | 2026-03-25 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 161bc8d8-5c54-3bd2-8265-dac3bae42ca2 | 1.56359 | -60.46187 | 2026-03-25 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 63e5f739-d463-35d3-bef1-580c10f423a7 | 1.94318 | -60.90431 | 2026-03-25 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6e873714-cbed-3a6a-bbd5-009e541467e5 | -0.31985 | -48.57809 | 2026-03-25 05:08:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1e3168a-baba-3e48-aac0-a109fcb10688 | 3.85397 | -61.29233 | 2026-03-25 05:08:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c160374b-cd2e-3b64-a7d3-6c86df2601ba | 3.85155 | -61.27589 | 2026-03-25 05:08:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4c4a6c36-30c3-3ea5-b8e2-bbaee9890fe5 | 1.65369 | -60.28896 | 2026-03-25 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 58185229-9557-3325-a890-5665879d6b39 | 2.70924 | -61.35827 | 2026-03-25 05:08:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b4b449e8-9595-3657-b91f-3bc1d4e4aeaa | 2.70843 | -61.35296 | 2026-03-25 05:08:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e23a7e8f-8819-3a0a-abdb-ee9db37f8ceb | 2.65136 | -61.30232 | 2026-03-25 05:08:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72e15510-b7d8-35f3-97b7-c2ff2421654e | 1.94088 | -60.90648 | 2026-03-25 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3798a62f-2897-3a8e-a825-d8b8bcaf164c | 3.92033 | -60.19549 | 2026-03-25 05:08:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6466557-4f5e-3d81-9424-6db5478f3fdc | 1.92275 | -60.28536 | 2026-03-25 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 396ae8b3-7202-3ae0-8df8-461968d96260 | 2.72376 | -61.35592 | 2026-03-25 05:08:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e661e968-1791-3be8-a2b7-1c70bf98f8f3 | 3.84995 | -61.26502 | 2026-03-25 05:08:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e3ff4c1-dfa1-3362-baa1-32a318ac72ec | 1.76217 | -60.57539 | 2026-03-25 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 60d183b8-fb1d-36ff-bb52-5bd0077c0dee | 3.85316 | -61.28684 | 2026-03-25 05:08:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8edc800d-2b3e-368d-b944-4bd66f3319f4 | 3.92554 | -61.29168 | 2026-03-25 05:08:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bafe0564-4011-32ae-aea9-8fbd603bfcfe | 1.83343 | -60.84877 | 2026-03-25 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca702b24-4ba2-33cb-b75f-b4efdc6d3664 | 3.85236 | -61.28136 | 2026-03-25 05:08:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8b5268f5-1334-36cd-8cf5-30fe13db38dc | 2.71327 | -61.35217 | 2026-03-25 05:08:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 47bf8064-cb74-3753-86d3-dcbf4e4b4daa | 1.89154 | -61.21459 | 2026-03-25 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 782698b7-dddd-3ed5-bfef-31c4d3139a1c | 1.84578 | -60.4211 | 2026-03-25 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a7c5902-a5bf-3e45-bf60-9736cadec23a | 1.91763 | -60.28172 | 2026-03-25 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README6.md)
