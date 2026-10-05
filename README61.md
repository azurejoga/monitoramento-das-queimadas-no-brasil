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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10ef325c-d629-3602-bdda-714d6cd80786 | -9.50484 | -68.49779 | 2026-10-05 06:40:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd9853e7-585f-3b72-a9d8-5c979706e019 | -9.40552 | -65.89409 | 2026-10-05 06:40:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0d63445c-77a7-3c22-a187-7731aecc6c7b | -9.16785 | -68.271 | 2026-10-05 06:40:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43f77bc3-92a8-321f-9842-90f16d08acb8 | -8.67025 | -70.04449 | 2026-10-05 06:40:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1acd5b6-d0db-345e-ae63-37006545dd33 | -9.16309 | -68.26191 | 2026-10-05 06:40:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 50a86db1-0230-3585-99fb-829db309a32c | -9.16255 | -68.26604 | 2026-10-05 06:40:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96e54702-e44a-37b2-80a2-f0d08c9b8e2b | -8.04641 | -72.43639 | 2026-10-05 06:40:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8411aa33-fc83-30d0-9c75-354edf52c8b4 | -10.86249 | -68.6926 | 2026-10-05 06:40:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24c16766-fb15-3f88-9345-f8551954a03e | -9.12167 | -68.21343 | 2026-10-05 06:40:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb940bc3-5d78-39ff-b737-fa99670846b1 | -8.66172 | -70.04385 | 2026-10-05 06:40:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f85d8186-9ad5-31ca-8872-02a5f9cde906 | -8.8781 | -66.65226 | 2026-10-05 06:40:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9defbd7-786d-31bc-a366-c846c8557735 | -10.64358 | -68.60255 | 2026-10-05 06:40:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff0d3987-69d8-397b-8c74-f04165176565 | -9.11669 | -68.21435 | 2026-10-05 06:40:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2186ef2-a507-37fd-b3f1-1a4f12a9cee0 | -0.38359 | -51.99706 | 2026-10-05 07:39:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 5ceb9c7d-1421-38f2-8c25-28a2333efb4e | 1.8506 | -55.81971 | 2026-10-05 07:39:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 379e18f2-b559-3c9c-93d4-192f2446abc6 | -0.38513 | -52.02882 | 2026-10-05 07:39:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 26.5 |
| fa8170ca-3389-3ab1-8620-3e3fcc6bdcd0 | -0.38857 | -52.00504 | 2026-10-05 07:39:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 9f5fb48d-3ebc-36bc-9eae-ad9376b57e87 | -1.08828 | -54.106 | 2026-10-05 07:39:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| f591628b-80fd-359b-9c3f-91347c74f618 | -0.40245 | -52.00695 | 2026-10-05 07:39:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 9d481afa-d5c2-35e1-bd17-974343360418 | -0.37997 | -52.02091 | 2026-10-05 07:39:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 32.9 |
| ea5d8d8c-6174-302f-8ad1-a890c56e4e63 | 0.44224 | -60.53764 | 2026-10-05 07:39:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 14.0 |
| d8cbe927-8e61-395a-8ec7-6b90ec7dfea3 | 1.86513 | -55.78339 | 2026-10-05 07:39:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| be8c7a33-c845-3cc9-9b43-9dcda50aee7e | 1.72214 | -55.64919 | 2026-10-05 07:39:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6b7d572a-6370-380c-85a8-ecfcd8ef5a89 | -0.39384 | -52.02273 | 2026-10-05 07:39:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 200.6 |
| 9e43b30e-5214-333d-8c94-c61ac14076f6 | 0.44982 | -60.52721 | 2026-10-05 07:39:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cc25ccbf-182f-3500-aa36-4500f21f37b7 | 1.84888 | -55.8086 | 2026-10-05 07:39:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d91affd8-fbf9-3588-a290-19d2440d94d4 | 1.72391 | -55.66061 | 2026-10-05 07:39:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 852ef6fa-77ce-3f8c-aa03-0fc76eaad737 | -0.39747 | -51.99898 | 2026-10-05 07:39:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 1a951645-5d1e-3ae9-91ce-e23bfd0ea74a | 3.09451 | -60.5878 | 2026-10-05 07:39:00 | AQUA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 01ffc435-979e-386d-aae3-95c5c9efa217 | -0.4077 | -52.02463 | 2026-10-05 07:39:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 25a5c3ee-cce6-3d89-85fb-cb808d188f7d | -0.41285 | -52.0326 | 2026-10-05 07:39:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 18.2 |
| b79c61cc-3455-364c-a27c-ca3cac500e87 | 0.44087 | -60.52851 | 2026-10-05 07:39:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 3424fd2e-610c-34e7-892c-a7536be13528 | 3.10036 | -60.62646 | 2026-10-05 07:39:00 | AQUA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 9.1 |
| a7499b42-433d-3cfd-b2e7-3b82aa1f62ca | 3.10516 | -60.59612 | 2026-10-05 07:39:00 | AQUA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 239421f2-751c-3a39-9e81-b233a2f37ea6 | -0.399 | -52.03069 | 2026-10-05 07:39:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 150.9 |
| a26a4e7e-58d2-3687-9f3c-1a5549dddb1f | -8.34554 | -62.83383 | 2026-10-05 07:41:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c5f34450-3288-3f7d-8e67-33649b17d906 | -8.66999 | -54.585 | 2026-10-05 07:41:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 494aa16d-1d93-3bbf-b761-2f2933dc218d | -3.98219 | -55.80723 | 2026-10-05 07:41:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 8df447c3-798f-3a54-a55e-b06711aeaad4 | -8.65933 | -54.57631 | 2026-10-05 07:41:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 63eb0779-26d1-3e2b-8a90-4bf9f820c809 | -7.43681 | -63.56614 | 2026-10-05 07:41:00 | AQUA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ece4d243-8375-3213-a653-fbdc7615c19b | -3.04853 | -54.20761 | 2026-10-05 07:41:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| f66c8be8-5334-3397-9180-d9f6dce43cc1 | -3.11427 | -53.74857 | 2026-10-05 07:41:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| c857537b-c45c-3012-b101-1efba95cc82e | -3.94988 | -56.03569 | 2026-10-05 07:41:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2607bc62-d240-3e5c-a8f7-4abd66a31da8 | -3.48278 | -59.72276 | 2026-10-05 07:41:00 | AQUA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c0d81827-b18f-342b-9e2f-40e259116b3d | -8.67269 | -54.56424 | 2026-10-05 07:41:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 173.8 |
| 875bd226-f499-3d72-aff0-2a63aadafffe | -8.67516 | -54.55735 | 2026-10-05 07:41:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.3 |
| cee0a622-b42f-3363-a95d-f7bdb9c8837e | -2.95007 | -59.15828 | 2026-10-05 07:41:00 | AQUA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6f98a3f1-a6de-3b4a-90c5-7add4ca7aae2 | -2.15167 | -59.22895 | 2026-10-05 07:41:00 | AQUA_M-M | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 675de46f-ce11-3c1c-84d3-822f7a1c3dd3 | -3.09176 | -53.72575 | 2026-10-05 07:41:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| f1cc1929-67f4-391a-93f0-7a9e1c1460d4 | -2.90736 | -54.08477 | 2026-10-05 07:41:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| a8863bd4-9086-376e-814c-fdbaa1fba823 | -3.10439 | -53.72045 | 2026-10-05 07:41:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 24844a9e-0f20-3f7f-a6a2-4da36edb60fb | -3.04601 | -54.22522 | 2026-10-05 07:41:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 32363d99-3264-3829-a357-70799ed1408a | -2.77709 | -54.09545 | 2026-10-05 07:41:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| f8914f5c-5e0f-3daf-8002-4c56907179f8 | -2.15299 | -59.22018 | 2026-10-05 07:41:00 | AQUA_M-M | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 299b1edc-0831-3c10-af2a-835d5068bf59 | -2.95549 | -54.13293 | 2026-10-05 07:41:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 855b10c3-41c3-3e99-a8da-beb972a5fac7 | -3.30947 | -53.84708 | 2026-10-05 07:41:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 2a5aba5d-1bf9-3517-8786-baf630e1a469 | -3.83536 | -50.32248 | 2026-10-05 07:41:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| c369db22-0471-3e0a-8f73-c3478c6d307c | -3.10731 | -53.70096 | 2026-10-05 07:41:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| cb622928-4963-361f-8a7e-cc926b190262 | -8.67231 | -54.57795 | 2026-10-05 07:41:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 7a3cafa8-fa88-3882-8ced-06dde2345d1f | -3.46796 | -54.57583 | 2026-10-05 07:41:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 5599ee2b-2ba9-321c-bac2-29455e307191 | -3.07793 | -54.17572 | 2026-10-05 07:41:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 7af6277f-9105-3a0c-8a43-a625edfdad9a | -3.98755 | -55.81648 | 2026-10-05 07:41:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| b2de7b0e-b354-31d6-8ef6-c4039e2d51b0 | -1.9834 | -54.41642 | 2026-10-05 07:41:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| b8976093-0bcb-3535-9edb-0fdada1d4ee0 | -3.05615 | -54.15453 | 2026-10-05 07:41:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| ea9c24b4-dd4d-3a63-8a48-f4e4da2e26bc | -3.98023 | -55.82115 | 2026-10-05 07:41:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| f3d6c189-e966-3606-8351-2afc7635d370 | -3.50104 | -54.59766 | 2026-10-05 07:41:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| be5514df-bbd4-3c11-9540-5e5acb236104 | -3.45371 | -54.59092 | 2026-10-05 07:41:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 12aac2bc-4d30-3515-a59d-c702e0883849 | -3.08055 | -54.15773 | 2026-10-05 07:41:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| d37e0532-9ad2-3c0d-980d-eae594c941e1 | -3.51622 | -54.62411 | 2026-10-05 07:41:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| ce0ad7d5-4b31-374e-b2cd-4f80b2953f5c | -7.44445 | -63.55151 | 2026-10-05 07:41:00 | AQUA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| efe3ee74-c70f-366c-961a-e980a830e47b | -3.46554 | -54.59261 | 2026-10-05 07:41:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 157.1 |
| 7de08995-5c5e-3643-9654-73684626fb26 | -2.37119 | -56.11969 | 2026-10-05 07:41:00 | AQUA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 08128fc2-cf43-3937-a7d9-58b7e73300c9 | -3.13243 | -53.71186 | 2026-10-05 07:41:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 96c8b68d-df5d-391b-ad12-762899b0f881 | -7.43844 | -63.55562 | 2026-10-05 07:41:00 | AQUA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 15.1 |
| ad2e2321-69f2-3a26-bd52-6d4eede20e0b | -6.00335 | -53.51251 | 2026-10-05 07:41:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 59ebfef0-f922-3e5d-8e27-6dd4ef44db4a | -3.32327 | -53.39622 | 2026-10-05 07:41:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 9f33d44a-8001-38f6-865d-eaa7a1d54828 | -3.10152 | -53.73966 | 2026-10-05 07:41:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| a77f3762-5077-376d-a7ee-31cad03a2ae5 | -3.32338 | -53.38221 | 2026-10-05 07:41:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 31379a31-220e-38e9-bfdf-2db6d986f702 | -3.11977 | -53.71007 | 2026-10-05 07:41:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| fb26540f-032b-3337-935f-6bc402c87bb4 | -3.87514 | -55.80759 | 2026-10-05 07:41:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| d5a1f116-e24b-3246-a482-0186aeaf2ed8 | -2.94031 | -54.19777 | 2026-10-05 07:41:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| e235130d-c70f-36dd-9eb0-bd703d8f4ad3 | -3.06577 | -54.17401 | 2026-10-05 07:41:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 72812f2d-9ad7-3684-ac5f-0b3d08cfcba4 | -3.84044 | -50.28482 | 2026-10-05 07:41:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| c48f1595-fed2-3ff9-a571-7d39464f9b50 | -3.50675 | -54.60571 | 2026-10-05 07:41:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 3729f1b4-40ec-3bf6-9903-4d7ba3873ffd | -3.10166 | -53.74677 | 2026-10-05 07:41:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| b85f660f-93fb-38ab-a817-4658c2ac1a0e | -3.09008 | -54.17752 | 2026-10-05 07:41:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 2a53f95a-ca5d-387b-b5ee-8e9d6ba5e7e3 | -3.09451 | -53.70618 | 2026-10-05 07:41:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 17c29017-3dfd-3b4e-bf5d-131118506941 | -3.05361 | -54.17223 | 2026-10-05 07:41:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 75bc0268-4035-3c2e-bc3d-023aa9e5fe70 | -3.15864 | -50.44011 | 2026-10-05 07:41:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 355ed501-94ea-3b06-863f-f1bc8d16fb7e | -3.06834 | -54.15619 | 2026-10-05 07:41:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 25c9bc70-c02c-3cb8-b2c3-01570f036394 | -2.98498 | -54.10094 | 2026-10-05 07:41:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| feaa4d10-6d96-3416-9168-9bc3797f4ef1 | -3.948 | -56.04894 | 2026-10-05 07:41:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 0946718c-1e28-39dc-abfa-9c01c5fcbe3b | -3.12965 | -53.73113 | 2026-10-05 07:41:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| b8f9f784-2085-30cd-a34f-4e120326fe49 | -3.09469 | -53.69895 | 2026-10-05 07:41:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 57d84fb4-803d-3e34-8e4c-d90c2f0a1b11 | -3.84663 | -50.31995 | 2026-10-05 07:41:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 59663c28-aeba-34fa-bb96-578a7e678852 | -3.10713 | -53.70818 | 2026-10-05 07:41:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 99db1901-2c95-3085-994d-6efc551a2345 | -3.05811 | -54.22694 | 2026-10-05 07:41:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 3949d9af-7d29-313c-b2a8-ba40fa304fb0 | -8.66216 | -54.55563 | 2026-10-05 07:41:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 2418f3d5-f177-3e8b-a007-88a359f36bcd | -3.10439 | -53.72754 | 2026-10-05 07:41:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 8fe58aa4-4180-3084-bb9f-638da9267489 | -7.4523 | -63.5635 | 2026-10-05 07:41:00 | AQUA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README62.md)
