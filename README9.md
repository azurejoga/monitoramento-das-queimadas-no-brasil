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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38411e0f-4282-34bc-8c73-9b6d6a5a75c2 | 1.5047 | -59.9116 | 2026-03-05 05:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.6 |
| fb00b5bc-3194-3f32-80a5-46c3567443d6 | 2.7816 | -60.3338 | 2026-03-05 05:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 154.3 |
| 35323d47-3746-3b29-bf37-369679921bbc | 2.7816 | -60.3528 | 2026-03-05 05:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 91.3 |
| fe09e82c-fd41-3219-84e4-b7482da32bd1 | 2.7999 | -60.3335 | 2026-03-05 05:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 8dbec70f-34e8-3119-946d-7fe63e4acf7c | 2.7816 | -60.3528 | 2026-03-05 05:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 7ae80252-1573-30f3-b8df-1b01df45f2b7 | 1.5047 | -59.9116 | 2026-03-05 05:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.1 |
| f9b52940-fc8e-390c-8bf6-ad51c9639c48 | 2.7816 | -60.3338 | 2026-03-05 05:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 137.2 |
| 85d857d3-8812-38e7-b67c-4496e01bd803 | 2.7816 | -60.3338 | 2026-03-05 05:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 136.2 |
| b650668f-e713-3e79-a3ff-d4d2031fd9a3 | 2.7633 | -60.334 | 2026-03-05 05:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 54.9 |
| cb5f3a88-88ee-3284-8c74-b32c4b4d7b85 | 1.5047 | -59.9116 | 2026-03-05 05:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 581abf8f-4515-39da-a5a0-c96b3a287752 | 2.7999 | -60.3335 | 2026-03-05 05:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 9120f82c-8dd8-3bf7-be81-fda4abf04d1d | 2.7816 | -60.3528 | 2026-03-05 05:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 3b388b13-cb94-33a6-a5c9-f5ebe85bd314 | 2.7633 | -60.334 | 2026-03-05 05:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 49.0 |
| e9c19bf9-7b76-379d-b22f-401127bfd7f5 | 2.7816 | -60.3528 | 2026-03-05 05:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 127eef14-8d73-3d7a-8709-f2dcd7aad3e4 | 1.5047 | -59.9116 | 2026-03-05 05:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 3496d70c-38fd-3f44-a3d9-f6a6e4e12846 | 2.7816 | -60.3338 | 2026-03-05 05:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 123.3 |
| 562b78ea-3ea3-3ce6-8aca-f3a39f34ebf8 | 4.53676 | -60.59425 | 2026-03-05 05:52:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2a9610b5-0185-38c0-97c7-761d9e178d4b | 4.949 | -60.27952 | 2026-03-05 05:52:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19ab87a5-df1a-3f3b-beb7-b3aeed64875a | 4.96408 | -60.26661 | 2026-03-05 05:52:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6d6ec728-6961-3a08-976c-510363234214 | 4.17878 | -60.37791 | 2026-03-05 05:52:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 824cda88-3cd2-38d5-9f91-93c8cbd2e144 | 4.96277 | -60.25871 | 2026-03-05 05:52:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ed0a458e-08a6-3f7b-865f-2aabe0bde128 | 5.00697 | -60.37063 | 2026-03-05 05:52:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a147e4a-fb50-39a7-bcb1-e992fb1f6982 | 4.96341 | -60.26257 | 2026-03-05 05:52:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 909c8ab1-cf63-36d7-a63d-9d9c6e3c315f | 4.95325 | -60.27921 | 2026-03-05 05:52:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d41b5bf7-8310-3a2d-abfe-1d24211985a3 | 4.18188 | -60.39646 | 2026-03-05 05:52:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36811862-38e5-3ad6-b76e-628ef830d89d | 4.81618 | -60.68772 | 2026-03-05 05:52:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fec3d1c2-7415-3d70-b0ad-7bf52eed1230 | 3.87692 | -59.98681 | 2026-03-05 05:52:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70ccc25f-4486-361f-a828-ad917cb87cf7 | 4.95856 | -60.2593 | 2026-03-05 05:52:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5cb3ee75-dbc0-3afe-ac68-d152c3091bc5 | 4.51631 | -60.58777 | 2026-03-05 05:52:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5189a8f-70d4-311b-aeb5-fbbc4639d409 | 5.00283 | -60.37148 | 2026-03-05 05:52:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd9d3a96-90d6-3e48-8a97-92d055da5fc7 | 4.81071 | -60.68003 | 2026-03-05 05:52:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c51f3db-cd98-3822-b507-ad54212e786b | 0.03957 | -60.99327 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e5c40f5-1d73-3b86-9441-7dfad77004ac | 3.16795 | -60.24276 | 2026-03-05 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd6ee82e-9ac6-3503-8101-f975792923cf | 0.48957 | -60.51651 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4eb00b37-c0a4-30fc-81d5-7249e0ac95f7 | 2.97241 | -61.03687 | 2026-03-05 05:54:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 22530d0c-342d-3a8a-9968-31ed1adba4ba | 1.93758 | -60.36966 | 2026-03-05 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 929771c7-efa9-3f8c-a9dd-aa29718307b5 | 2.69707 | -60.69304 | 2026-03-05 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d1e4ffd5-1639-362b-a76c-78fc3b19fdc7 | 0.47174 | -60.32666 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03ca52df-d730-3b87-af7f-4be55594c771 | 3.03025 | -60.82378 | 2026-03-05 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| af2a2d7f-ac0a-3604-91f0-68f3cf5bcc21 | 1.00857 | -59.51209 | 2026-03-05 05:54:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98e95cad-d28b-37d7-9447-1404d5d3fa06 | 1.10947 | -59.19311 | 2026-03-05 05:54:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 661e477e-9fca-38b5-8358-5e38b1200170 | 3.28304 | -60.71806 | 2026-03-05 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e03c9a2d-940a-3013-b1fa-a686a1b8ccda | 3.03381 | -60.81926 | 2026-03-05 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e56f45d-d61e-386b-adf1-b41a1108b89b | 1.50699 | -59.91499 | 2026-03-05 05:54:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cebb31b3-09f6-38dd-bd00-05ecc80264c0 | 2.78186 | -60.33545 | 2026-03-05 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 13be5d9e-eedc-37aa-bbdf-68548d0adc5d | 0.03673 | -60.99137 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4a2f0704-ccba-3460-9b30-1e58ed2c8a9a | 0.03843 | -60.97428 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 548e515a-49b4-33d8-b063-7d9a35d2d729 | 2.69302 | -60.66784 | 2026-03-05 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2653533-42dc-3217-9dfb-1e45e04e2e52 | 0.47875 | -60.32715 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c12e3f82-b2f4-368f-a5f3-b78508943362 | 0.47806 | -60.32263 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe85104c-5749-3f51-9d3e-98bf66f37008 | 0.49669 | -60.50922 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 483f7391-6fec-3441-b5be-3615259d2bea | 3.03259 | -60.81159 | 2026-03-05 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1e2049ec-2e4f-3c8f-b924-8cd70dd073fd | 1.14553 | -60.89546 | 2026-03-05 05:54:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f01c0f0-b5c1-30cc-9439-61eea2334394 | 3.02264 | -60.63912 | 2026-03-05 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 43c978a5-18e9-3d5b-842d-03e9c3b3c10c | 0.03975 | -60.98255 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7d02398-5629-3196-84ea-d07a43c53995 | 2.96534 | -61.04562 | 2026-03-05 05:54:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ddf9a2ac-4d59-348d-bc09-78b55a81b361 | 0.07456 | -60.54332 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 858d2a6c-ceab-3d35-88b3-4bd3da86a5c4 | 0.04474 | -60.98598 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e41bbf10-9792-3141-b3a8-fbccf0079515 | 2.69664 | -60.66317 | 2026-03-05 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16f742e7-b490-36b4-bad3-53df66a157ac | 2.69615 | -60.68763 | 2026-03-05 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5327e798-4ee9-3d5f-bd5e-2f8f9fc01e48 | 0.0727 | -60.45407 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d62c9c22-68a3-36e6-a4be-95c6de9e5135 | 2.96417 | -61.09139 | 2026-03-05 05:54:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9108ea12-eeae-3f56-ab07-de9ad980baa0 | 3.28264 | -60.74185 | 2026-03-05 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a95525a6-7bc2-3821-92e3-cc0ec352bf53 | 0.07356 | -60.54523 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7bf5b2c-c87c-33b1-852d-c8aaa147c3e3 | 0.05342 | -60.98481 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38747e83-9683-34f5-9568-817a4888b958 | 0.47552 | -60.32146 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 46d68203-a564-35c4-9247-8b67462b89ae | 0.28406 | -60.61691 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 649cfba9-ce38-33b8-8e39-1459c954c7f3 | 0.7688 | -59.89204 | 2026-03-05 05:54:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a5a21cd6-a278-36b9-9008-638cb2d6818a | 0.72896 | -59.90501 | 2026-03-05 05:54:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b364330-411c-3b40-b2a0-939477ff456d | 0.47102 | -60.32219 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| dd147df4-605c-3cb0-bf8d-9b46192faef8 | 0.0701 | -60.54403 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e323e01e-1a64-3e19-9a49-4be6e16eff64 | 1.50625 | -59.91043 | 2026-03-05 05:54:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 5aeb3fcd-736f-32fd-8b7d-b1c250d35329 | 3.05513 | -60.62569 | 2026-03-05 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f98bc90-255e-3f2a-82da-e8ded468863c | 3.04808 | -60.80116 | 2026-03-05 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df62581c-ff65-38c6-89db-c5906ead049a | 2.69771 | -60.69695 | 2026-03-05 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| aa23f509-674d-3925-9fa3-8f9ea8afafaa | 0.04265 | -60.98442 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a25b5973-270e-3240-815b-33c5a4254c44 | 3.03466 | -60.63311 | 2026-03-05 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2fc1e663-816e-39a9-add3-23df730102c8 | 1.11031 | -59.19836 | 2026-03-05 05:54:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c1827765-9312-3233-a3d2-e2828fc9155a | 2.78322 | -60.34374 | 2026-03-05 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 41.0 |
| d5365e4a-f259-3102-b802-82479e6ada75 | 1.07943 | -59.25175 | 2026-03-05 05:54:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 416a92c4-74ee-39fb-8755-7b5477b9aabb | 3.03198 | -60.80774 | 2026-03-05 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2d0adfdf-0d2d-3f8a-88ea-332d804773df | 0.31078 | -60.44429 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 51f56bc0-e7b2-3855-8de3-b7c1a1a68d1d | 2.70064 | -60.68842 | 2026-03-05 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8c23222d-1864-3d36-8caf-2f7a6fdeca8d | 0.73357 | -59.90424 | 2026-03-05 05:54:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f01377cf-adf1-3ae5-b376-9203a81825fc | 0.66443 | -60.30749 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ca481c02-121e-30c5-b5aa-680d684ac8c4 | 0.47247 | -60.33118 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1262504d-57b5-3245-bd0c-12c63dd4d244 | 2.90759 | -60.59996 | 2026-03-05 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab1815b9-bdba-3506-8cdd-6216384f0458 | 0.03909 | -60.97844 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12b110a4-ce42-3076-a78d-580dd32d890e | 2.69999 | -60.68447 | 2026-03-05 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 074512a2-4c12-38cc-b3ad-c976e1eec7a7 | 3.50875 | -61.90873 | 2026-03-05 05:54:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9346be7-a31f-3780-ae48-dd44693a8b1b | 2.69601 | -60.6592 | 2026-03-05 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4818a7b-1d5a-3ed4-804e-4638d32fc31b | 1.5055 | -59.90583 | 2026-03-05 05:54:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 15.1 |
| b61c6b2d-bca4-3f58-975b-2fcc2eac4311 | 1.49559 | -59.93095 | 2026-03-05 05:54:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e666c105-bc47-35ff-b6c1-b8c0851158d7 | 0.03895 | -60.98919 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e46aa4f2-9a2d-38fa-ac14-2f93465b2c71 | 0.04106 | -60.99072 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a48da1eb-6afb-3ab4-b4ca-7661acb367d4 | 0.49402 | -60.51585 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c51a1646-86a1-3202-b6fc-b19f72af25c3 | 2.77753 | -60.33615 | 2026-03-05 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 14.9 |
| df157912-590e-38d4-99c8-a221b7da0c0f | 0.31596 | -60.44802 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5e5e76b6-3eae-3208-ba6e-f081e12b9c5b | 2.66086 | -60.40764 | 2026-03-05 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 18f00425-9a7d-3726-a05c-4e4f9d0f4b9e | 0.03525 | -60.99397 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README10.md)
