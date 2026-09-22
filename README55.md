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
| 4296d2bf-fd73-30e6-8cbc-0e33b3da7162 | -9.89575 | -48.4584 | 2026-09-22 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3799040a-372c-378f-a133-04fe5afd5797 | -6.77894 | -58.60931 | 2026-09-22 04:46:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2082798-8df7-372d-b67f-1ce05b6260ed | -7.53828 | -45.41223 | 2026-09-22 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a8456703-79df-33d8-a432-f09383035ed7 | -3.7884 | -60.75233 | 2026-09-22 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6fc9f707-68da-33f8-b0a8-c487ef45f6bc | -7.3303 | -55.59451 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dac049aa-e541-3c40-90e9-c4a489f0bec9 | -3.28705 | -57.86023 | 2026-09-22 04:46:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 90539c7e-e063-3ac1-8cc1-4bf09b5dcd0e | -6.19546 | -57.77878 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| fd72e5b3-b3b2-3290-a5e4-3aac5f6af31e | -6.00255 | -53.65359 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21417286-56ca-3ddd-b252-e7f2425e6266 | -2.91361 | -54.18764 | 2026-09-22 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98d0d03a-f237-3f7e-804e-fda25ae67907 | -3.64534 | -58.77025 | 2026-09-22 04:46:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b9b71b7-6468-3d58-b121-4a469b1e2b3a | -5.26882 | -45.4118 | 2026-09-22 04:46:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51e94493-fb9c-3c3f-bba1-144af83345d7 | -7.08975 | -42.07132 | 2026-09-22 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 23c819ee-be79-3173-ae37-2de302247f53 | -4.53041 | -54.97442 | 2026-09-22 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8da12c5-630d-3bd0-b0c1-28f54c1b1c1c | -9.8781 | -48.4243 | 2026-09-22 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f14435e-c399-3fa4-862f-902ca0dead96 | -6.57185 | -44.90301 | 2026-09-22 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aff4c2aa-b7e9-3672-8e50-3a2979a793e2 | -4.44522 | -55.59598 | 2026-09-22 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95ac2628-32c9-39ee-95c2-d929068d20d1 | -6.11394 | -44.31776 | 2026-09-22 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00c62bd9-2fd8-3fec-ad9c-620ab3fc3404 | -3.06429 | -54.41135 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 43a3f56a-f2f3-3b7d-bd66-d556edba5fa6 | -8.61279 | -54.74782 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c60185c6-5bf9-3ece-a95d-27c51b0e1a08 | -7.1402 | -48.4412 | 2026-09-22 04:46:00 | NOAA-21 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ad2989fe-a2bf-39bb-9d34-eb7239e51d54 | -8.48514 | -44.74357 | 2026-09-22 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0e865f45-091d-3230-a360-f4defdd2ee99 | -10.09852 | -46.08443 | 2026-09-22 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 66325cb7-9cdd-322c-887b-a351a5d0b30b | -9.65827 | -54.32719 | 2026-09-22 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2bdf7be-d8c5-3b92-ad46-afb8712a8079 | -8.08417 | -55.33758 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8204d881-994e-30b8-ad46-4f0a70c7a12b | -5.85688 | -52.03193 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e9d3165c-850f-3a39-85b8-b8e49c8f88c7 | -6.74248 | -59.42258 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 324b88be-c4a7-35b4-bf44-13c5e844e049 | -4.43277 | -55.34859 | 2026-09-22 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56116e3f-2ae7-3191-83a4-bd12ea800866 | -3.06501 | -54.40689 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0969c20a-bad0-30d9-96c4-31249befb054 | -7.36205 | -55.42886 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5141cb8d-5308-3de3-ad6d-58dd34f6426f | -2.8834 | -54.0761 | 2026-09-22 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c513ba0-5321-3964-b30a-d9e2f428866b | -4.65661 | -42.09426 | 2026-09-22 04:46:00 | NOAA-21 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1799124e-a269-3a76-8731-153599cf2754 | -2.95236 | -57.7171 | 2026-09-22 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 92ee90ee-5dd4-3b0b-8bf1-62b6bea95ebf | -8.33803 | -47.53583 | 2026-09-22 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d9ce77dd-3309-3f05-abe2-f1e4383ade7c | -10.68307 | -50.75878 | 2026-09-22 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fce5b869-88ee-3f65-befe-371a4f1c4ed0 | -8.78454 | -44.30359 | 2026-09-22 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ba961fee-ce13-3701-b23e-0bbcba613e97 | -4.1339 | -54.25071 | 2026-09-22 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 892e18a2-ffb8-3dbb-9d4d-ce1ed9514a53 | -6.72855 | -55.09492 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e34ce6f1-0443-3b85-8c66-7f34b9439d86 | -3.00922 | -54.17427 | 2026-09-22 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec804d70-ed23-314a-a6ee-da1d26df82fa | -6.78662 | -48.6754 | 2026-09-22 04:46:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f3a68571-6da2-390b-ad01-91e99cb87080 | -6.08571 | -57.63185 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 664d9b32-a9e8-3729-b6e6-f999e2ca7ba9 | -9.27415 | -46.17882 | 2026-09-22 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1efdf783-dfd1-39da-a044-ae9233f25297 | -8.45232 | -46.83646 | 2026-09-22 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 37c01184-dbe1-36bf-b535-0b444f80945a | -11.10667 | -48.32228 | 2026-09-22 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c2637e8b-2b24-3d78-a35e-a3f876fd8fb8 | -2.78894 | -59.88807 | 2026-09-22 04:46:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 16e57c8a-bbec-3200-aba3-0144c866e670 | -2.56806 | -57.50964 | 2026-09-22 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 77f8edd1-5ec8-3769-b755-f36239a369c3 | -8.80462 | -48.75585 | 2026-09-22 04:46:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5410a991-ce48-3597-ab68-8995512200a9 | -3.47152 | -59.53572 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f140fc0c-58cc-336f-a3bd-2467c8d66a7d | -5.64953 | -43.35915 | 2026-09-22 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ed3fe2d-accd-316e-8a89-a71ef1af687f | -5.83081 | -52.04583 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b81a5380-e9a9-37ad-a1a5-4205c91ed79d | -5.20666 | -46.21115 | 2026-09-22 04:46:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d0b9d97-e43c-3fe4-a2a8-6bc5bac890a8 | -3.23566 | -53.95676 | 2026-09-22 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| f5c024d7-e2d0-3f98-b43b-39f97613cb55 | -9.88841 | -48.45721 | 2026-09-22 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 21cb02e0-f23d-3aab-8f58-4c812ad40bbf | -6.78613 | -48.67263 | 2026-09-22 04:46:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f72b7adb-7bd0-32b6-b404-6a81af2d987f | -3.22523 | -53.95218 | 2026-09-22 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 10b1a82c-7477-3948-95cd-e0b2a616c0a4 | -6.92795 | -59.63135 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d1bf54e-997e-37ac-abdc-fdfb01f37e39 | -7.6079 | -55.35331 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bfb209f4-3467-3cca-9c7a-17c59fc2eb7b | -7.32694 | -55.59591 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 22fcd0a8-bf0b-3402-ad92-83d0bee761c6 | -6.59695 | -39.14051 | 2026-09-22 04:46:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 12.6 |
| b6676a8d-4e2e-3993-a1d3-f013c408f642 | -5.9796 | -57.78352 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c8d4ce41-55ae-3949-81ee-c725539711a4 | -5.61347 | -44.84678 | 2026-09-22 04:46:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 88a1d6e0-c80e-36f1-a0e3-1996a482d742 | -4.34961 | -55.66634 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9406f767-3e7d-3021-86cd-3f6f13799775 | -3.17386 | -51.35168 | 2026-09-22 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aa4e2561-7450-3413-827f-1b93878d681b | -8.33872 | -47.53111 | 2026-09-22 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 84acd68f-c75e-3c42-97c9-061dae0fd629 | -5.45571 | -60.15088 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c435fe48-6fa2-3275-9db8-59fe3773f1fa | -6.4625 | -59.98568 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9a216283-abab-3e13-afc7-403066b1b6b2 | -3.85349 | -54.21889 | 2026-09-22 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ffe6440-e24d-3e1d-8221-17530573a997 | -5.97942 | -57.77229 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8834f5e6-0aa0-3169-8b08-07b7448364a6 | -6.42981 | -55.61911 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 57e2e124-aeb6-3a3f-9549-c175d7475b72 | -4.64221 | -50.99148 | 2026-09-22 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5e57a71-bfe5-32b2-92e5-db6fb447cacf | -3.01452 | -54.18863 | 2026-09-22 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 923064aa-36ff-3775-9cc6-9c6b30249255 | -5.98532 | -44.72722 | 2026-09-22 04:46:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d1db39be-a996-316e-841a-47dc281f5d98 | -7.58862 | -57.70179 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 87dad7ac-a27d-37bc-b8c5-a28a8cd5d164 | -9.59137 | -47.77684 | 2026-09-22 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 606df904-c164-3600-a5a6-ffc4cd0b43ef | -7.5116 | -45.44563 | 2026-09-22 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f3df117-9b6f-3e67-9c51-9ef49a48e30a | -3.13522 | -61.39718 | 2026-09-22 04:46:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3c7f1dc2-fb72-3926-9e6a-f299149bf362 | -6.22799 | -55.62137 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 886c53f8-00d3-3366-8418-c5309d8e65f9 | -8.44397 | -45.81643 | 2026-09-22 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 755f40a0-99d7-3083-8091-84870acfc7de | -8.92514 | -50.89742 | 2026-09-22 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d745e862-31b9-391e-81d5-f706873c82aa | -6.45169 | -59.97673 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08ef3f10-583f-3677-80a0-1b71868ef261 | -4.12655 | -50.65663 | 2026-09-22 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97c127c9-bf27-3c58-97a6-a74ecabd88af | -9.55064 | -47.95179 | 2026-09-22 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fed4dba9-bf13-352e-99bb-c0316746645b | -8.60357 | -54.60362 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e5dda6b-be23-3172-8fef-84ac4bee4d65 | -5.98592 | -44.72297 | 2026-09-22 04:46:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1ffdcac6-3c07-3693-b782-cfa41184b6ae | -6.63341 | -59.93 | 2026-09-22 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| caccbf15-3686-3965-8a9f-e3cf9cef2169 | -7.59286 | -57.67674 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2dc736f5-4a60-33de-9160-dd534919a726 | -4.29751 | -56.26651 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 789a5b99-038c-365f-b00e-3921d1c6b453 | -6.63855 | -59.93085 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| abe86bb4-63e7-3b17-a134-31c8eb2c3108 | -6.73974 | -55.09672 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a551f9aa-ff51-35e3-878f-c6df50618253 | -3.68921 | -60.56669 | 2026-09-22 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d8c0adb6-59d1-31da-bb41-3bed64b3f189 | -10.84222 | -50.14518 | 2026-09-22 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 054438a4-09a5-33ee-9ce4-d7c82dce3848 | -8.53849 | -54.69369 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10b108d6-6d9e-3f06-b5d5-824bdc624b86 | -7.41818 | -49.83883 | 2026-09-22 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9d56419d-aff8-3ef1-ada9-fd0a2bca1471 | -3.06125 | -54.40628 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2b58659a-2e7b-3c21-ad63-626b6cf85a88 | -10.45375 | -51.32395 | 2026-09-22 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b361b270-2c4a-3dd6-928a-c588411912ef | -3.36745 | -50.46386 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ede899f7-28a3-3277-818b-0f57961d5beb | -6.10832 | -55.6892 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b964e85a-65a7-3e2c-99f3-a98ccdbb1731 | -8.89747 | -62.37601 | 2026-09-22 04:46:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3ab77b58-541c-3471-9bb7-1a2312b12331 | -4.12986 | -50.65714 | 2026-09-22 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4766d4ca-4e69-3bbb-a4ed-5ed6ea65245d | -6.67846 | -59.10907 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 01023e8f-5aff-3e10-8b89-bd869fe26916 | -3.52322 | -59.93904 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README56.md)
