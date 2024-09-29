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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20ea7b98-6071-3437-ba26-4dca0fffea3d | -14.28478 | -43.77315 | 2024-09-29 04:04:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1084b32-18bb-3f44-9b67-6fc8c91e808b | -14.18589 | -44.24164 | 2024-09-29 04:04:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 72fa90de-04ed-3a78-ac25-5f50c61c4e7a | -14.18523 | -44.24561 | 2024-09-29 04:04:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 20fa2ebc-741d-3b9e-b9ca-c22a726b4ad7 | -14.02277 | -44.45707 | 2024-09-29 04:04:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 607074fe-2e0f-387c-b63e-43f347721f60 | -13.89617 | -43.95358 | 2024-09-29 04:04:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aefd061f-ec30-3cc2-b3d1-ce6a7ca3c87b | -13.78423 | -44.34208 | 2024-09-29 04:04:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c274add2-27f1-3efc-ba0c-29f62f485074 | -13.78354 | -44.34615 | 2024-09-29 04:04:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d8a3c8b2-f120-3478-bf8d-7e7b8e5413fd | -15.88707 | -45.04056 | 2024-09-29 04:04:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 303d2b51-b749-3fb9-b866-7008c25739f7 | -15.88636 | -45.04471 | 2024-09-29 04:04:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e13c7be-6054-35e3-8a07-4a8e4af7d51f | -15.88566 | -45.04887 | 2024-09-29 04:04:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 75c10630-c60e-3284-9b24-0430c5f18762 | -15.88495 | -45.05302 | 2024-09-29 04:04:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f097710e-c9d3-3cfa-b73c-19ebc8568991 | -16.89054 | -45.31707 | 2024-09-29 04:04:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e23757e7-4982-3cdb-a2e2-38c34e78f08f | -19.4449 | -45.86313 | 2024-09-29 04:04:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e94cc4a9-f47c-3097-8df2-22120e8f32f3 | -19.44416 | -45.86739 | 2024-09-29 04:04:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4dac760c-0cf9-30fd-9017-5059ea5b483f | -19.44343 | -45.87161 | 2024-09-29 04:04:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9ca2ab8-dc4a-3b61-bdf2-07ae4108daaf | -19.44065 | -45.86663 | 2024-09-29 04:04:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5c699b15-2dda-3766-b60f-ea41c44ab5c1 | -19.43992 | -45.87084 | 2024-09-29 04:04:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61274e7b-9474-34b8-a6fe-016542eca413 | -19.68122 | -45.24669 | 2024-09-29 04:04:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d344f52-134e-314d-ae4a-765b942779d7 | -19.59025 | -45.5703 | 2024-09-29 04:04:00 | NOAA-21 | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e547909f-2f12-3a2e-94c6-8f46c07d5397 | -19.58677 | -45.56961 | 2024-09-29 04:04:00 | NOAA-21 | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a950ec9d-f189-330b-9cb3-af387834ecbd | -12.031 | -45.73903 | 2024-09-29 04:04:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee0a2425-cdc3-3d33-938f-fae4c784f4f4 | -14.17076 | -46.45174 | 2024-09-29 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ef032dbb-6e13-3fe3-85dd-7ef5bdf4a819 | -13.17027 | -45.45988 | 2024-09-29 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86119cec-d68b-39d0-97b9-1a733c1729a9 | -13.36027 | -46.30726 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| baba8132-0a43-3daa-a89d-fcfb5bc617bb | -13.35935 | -46.31246 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 51409607-4109-328e-8d0b-b4d22a396bde | -13.35843 | -46.31764 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 66ca79b3-64b8-3779-84e1-4ea08b6856a3 | -13.35637 | -46.30642 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4f17c544-f414-3be6-9fd4-139199f9ead9 | -13.35543 | -46.3117 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b71672e-f318-315b-a6bb-783de4bb9a47 | -13.3545 | -46.31693 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ee707d7-ffb6-3825-9b5e-1668e2bc8641 | -13.3515 | -46.31101 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8b4e584-f823-3638-9588-067047b551ca | -13.3427 | -46.31487 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2a120a05-806b-3deb-9431-ec55a723971d | -13.33714 | -46.34599 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 916d99b9-a4f0-3799-b991-7667467c2050 | -13.33622 | -46.35119 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 69de7dd1-e16c-30c0-9b93-f6ac383fff33 | -13.33528 | -46.35642 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 624bd735-2678-3d5b-b14f-6f0d0a2932ab | -14.1703 | -46.45396 | 2024-09-29 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a86e8fce-b43a-367c-9cf6-ee1a7b15e464 | -13.33228 | -46.35044 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a80f3491-2d40-30ce-8ca5-bfa3219a6137 | -13.25987 | -46.35077 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2e4dfab6-d41c-3d55-be30-b8553fd95855 | -13.25896 | -46.35593 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 968e0e5a-0921-3b89-a37d-220de6ab2e80 | -13.25293 | -46.344 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| be3634cc-2580-3a67-8267-709ed87ca308 | -13.25198 | -46.34935 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5b287367-4ff6-3d69-8023-70ef1d2ad3bc | -13.24804 | -46.34864 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7c5f2d79-b8be-3f41-985f-16bec2ed18f5 | -13.24712 | -46.35383 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b1661d61-77ad-367a-b858-5249d71ff21a | -13.24409 | -46.34792 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7d1f7f84-2885-3de7-a2f9-20642cf682c1 | -13.24317 | -46.3531 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 352e4138-328b-3f7d-896a-679f787f97b5 | -13.2411 | -46.34187 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d0b6e3fb-c0c0-35ae-a838-0a5a5481f93a | -13.24016 | -46.34717 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a4bc7d8e-e04a-3c8b-9c96-6de84550eaec | -13.23912 | -46.33012 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5b496278-9101-3d52-960c-3a03a1e364da | -13.23811 | -46.33582 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c200c834-6604-3a5d-b1d7-38bc56ac4045 | -13.23715 | -46.3412 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6286ea1d-68c9-3c12-bda2-7170061d3656 | -13.23621 | -46.34645 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a4bc2d10-5240-369d-9c63-3e8ee513c3ed | -13.23124 | -46.32873 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7f2ac92c-919b-30be-9d2e-4202057097a8 | -13.22834 | -46.32225 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7cdb0b00-5582-3a77-9b48-4e3aed6582f4 | -13.22729 | -46.32809 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 067ec70e-581c-3278-9af6-9f43aca92683 | -13.22537 | -46.31611 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 65308d65-2d76-3a89-a6cb-42b90d147d97 | -14.58641 | -45.75748 | 2024-09-29 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| b3753035-c49f-356a-b5e1-47e8c165ba81 | -14.58426 | -45.74763 | 2024-09-29 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| af528e86-0556-31d6-8d3e-c51e38fbfd1c | -14.58347 | -45.7522 | 2024-09-29 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e62640af-35a1-3a17-b3d2-289320a01002 | -14.58292 | -45.73315 | 2024-09-29 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c735ceb2-dc77-37fd-a321-575f75bf54da | -14.58268 | -45.75677 | 2024-09-29 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ea215538-cea9-3775-9b4a-beb34ad3e455 | -14.58212 | -45.73778 | 2024-09-29 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 8d739cea-66ed-3af2-a619-e07e5f4db47e | -14.58189 | -45.76134 | 2024-09-29 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7a1d1bdc-ab57-3221-a3c6-9f151437cd10 | -14.58132 | -45.74236 | 2024-09-29 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 62b77779-8fcb-3590-b17a-af1a8f1aa591 | -14.58053 | -45.74692 | 2024-09-29 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 4a8746c8-3bdb-30dd-8ca6-9e0baaebe496 | -14.57974 | -45.75149 | 2024-09-29 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 57e093fd-83e2-3227-be68-c4684c371ef3 | -14.57919 | -45.73248 | 2024-09-29 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d8543f4-f7a4-33f7-9bb5-c0d6271d2352 | -14.57895 | -45.75606 | 2024-09-29 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6afd73ce-6d9a-339d-b8cb-60674720729e | -14.57839 | -45.73709 | 2024-09-29 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9e688381-1e52-33f9-a77f-6ca0f83a04b0 | -14.57816 | -45.76064 | 2024-09-29 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a6fba095-7f45-3ce4-a08f-7cf4cce4df95 | -14.57681 | -45.74622 | 2024-09-29 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e576bdcd-4028-329a-81ac-8eb05be5cdc7 | -14.57626 | -45.72718 | 2024-09-29 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 700fc169-cfae-3d58-81a1-ad029275c98a | -14.57601 | -45.75078 | 2024-09-29 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b110687c-7c45-3d6a-b540-6bfc0755a743 | -14.57522 | -45.75536 | 2024-09-29 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e782821-f802-307a-a158-9d4c1f3e218c | -14.57442 | -45.75995 | 2024-09-29 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c27d0b51-15b3-395f-97a7-80c68dd04c14 | -14.57387 | -45.74096 | 2024-09-29 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dd43c32a-16a2-32b2-9011-9c1bd0055fdf | -14.57334 | -45.7219 | 2024-09-29 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85c7394c-e72f-3344-abdc-1900c9f888e7 | -14.57308 | -45.74552 | 2024-09-29 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba304b1e-ef98-3dcd-9a4e-82e048ce70c7 | -14.57229 | -45.75008 | 2024-09-29 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad6cb5d0-93b2-3ecc-9329-17c744d88538 | -14.57173 | -45.73111 | 2024-09-29 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 62eadf42-8c65-3416-8ad0-3defa0dc59da | -14.57149 | -45.75465 | 2024-09-29 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fadfa17e-6898-3ab0-946c-e5c433cd41dd | -14.57094 | -45.73569 | 2024-09-29 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a77617b3-0906-3f95-8131-22a47315a546 | -14.56642 | -45.73956 | 2024-09-29 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9387acb8-3240-31d1-ba0d-b02fcaac37dd | -14.56562 | -45.74412 | 2024-09-29 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab515344-fe5f-30fd-a8e9-ed721af5f602 | -14.56483 | -45.7487 | 2024-09-29 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8261e313-4537-3462-8ec1-7408bd0df24b | -14.56349 | -45.73428 | 2024-09-29 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00fb01a2-e9d7-365c-8380-78c6a7060af6 | -14.56189 | -45.74343 | 2024-09-29 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b45bc25-e65c-3a41-9e6e-679cf6d17164 | -14.5611 | -45.748 | 2024-09-29 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2a8ed5f4-a3ea-308b-a3bc-1fb16f78f509 | -14.48926 | -46.20286 | 2024-09-29 04:04:00 | NOAA-21 | DAMIANÓPOLIS | GOIÁS | Brasil | 5206701 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9ac0240-83ba-3014-bd2f-1846bdd41ac0 | -14.48542 | -46.20214 | 2024-09-29 04:04:00 | NOAA-21 | DAMIANÓPOLIS | GOIÁS | Brasil | 5206701 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5dd28d57-4e4e-34c1-9ab2-06b423e5bc4a | -14.17997 | -46.44516 | 2024-09-29 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aa165e67-9d8d-3dee-a248-f874697edca6 | -14.17901 | -46.45044 | 2024-09-29 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9ab86674-58f3-3b0e-8ede-e7e2dfdedb82 | -14.17646 | -46.44212 | 2024-09-29 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 11f70ff7-93d0-337c-926b-52236c592fa0 | -14.17607 | -46.44436 | 2024-09-29 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4573817c-1bf4-3664-9b74-5429cb5cef09 | -14.17555 | -46.44736 | 2024-09-29 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7a9b2d8d-71d7-359f-8204-65943ab7b22c | -14.17513 | -46.44958 | 2024-09-29 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ccee001a-4fdb-37da-8bb8-494f0f3ae984 | -14.17465 | -46.45259 | 2024-09-29 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c403baed-c58a-39c0-9b9f-858a922dd2e3 | -14.16985 | -46.45701 | 2024-09-29 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8b466a50-d9e3-3d7c-a811-1c1b083ddfb8 | -14.16684 | -46.45105 | 2024-09-29 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d2f680a1-b796-3f7d-95c2-56867b6233e4 | -14.16638 | -46.45328 | 2024-09-29 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d9ebb601-87f5-3995-8438-cc9d6b741cc8 | -15.2976 | -47.47486 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ae93697b-665c-37a9-b883-46a8d98b261f | -15.297 | -47.47812 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |


[Clique aqui para ver as próximas entradas](README30.md)
