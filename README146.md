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

## Dados Diários - Página 146

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03ba7256-ec8a-3095-a1a0-146dd450014c | -17.09867 | -56.17747 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| a3d99512-613d-37ab-ab13-427c02c54039 | -17.09812 | -56.18108 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 8a0fdf0a-a9e5-3549-ab22-9f0fc8ac611d | -17.09759 | -56.1625 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 0428edd8-7d7a-355b-94b2-4a5091069a2c | -17.09756 | -56.18468 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| bdd357cb-755c-35af-b68d-632d7d2fdbb5 | -17.09592 | -56.17332 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| b5d28cfb-85e1-30ca-bc61-a811987dafaa | -17.09536 | -56.17692 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 487ecbd9-f494-372c-8a93-42300bfe56ec | -17.0948 | -56.18053 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| cb0b25e6-f6e9-3c74-ad25-1e303e03e780 | -17.09425 | -56.18413 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 2f3d1621-43ab-3fd3-bafe-651a079adc74 | -17.09372 | -56.16555 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| ee5442e4-7a5c-3f46-a33b-573ed9661468 | -17.09316 | -56.16916 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| aebe19b6-c694-38db-807c-d83f57ee417a | -17.09261 | -56.17276 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| cd1cee18-187e-365d-8f79-f66ff39cd5e2 | -17.09205 | -56.17636 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 258ee014-5e03-30e7-a304-a8247d278aac | -17.09149 | -56.17997 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| db39fd27-0d45-3470-82f5-df392a5c95a6 | -17.09094 | -56.18357 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| e7d1a4f1-9d64-3a96-a274-361040928e46 | -17.09041 | -56.165 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 74.8 |
| a490b0fe-e0d8-3341-a2f9-a8194d457464 | -17.08985 | -56.1686 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 74.8 |
| b731cd58-f858-3003-8e85-b46e1855cb2c | -17.12739 | -56.16748 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 69eab80d-f445-355d-a603-5194dfb40f5b | -17.12519 | -56.15971 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| cf52865f-55b0-3092-b742-b341655e52c8 | -17.12352 | -56.17053 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| fab97a73-2563-3a77-ae47-c6e0c0224213 | -17.12188 | -56.15916 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| d49528d8-c6dd-399e-9314-b91dd1028607 | -17.12021 | -56.16998 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 179d46b7-2d8b-3abe-9c66-e0310e85b459 | -17.11965 | -56.17358 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ee88bcfa-5de6-3d68-a228-cde655bdbec3 | -17.11746 | -56.16582 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a66d14e7-d3c6-38b2-abef-d61c59db488f | -17.11526 | -56.15805 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1e4398c0-9043-32d3-930c-cc6ba91860f2 | -17.1147 | -56.16166 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1bf50253-6525-3a86-aacf-23144f58ed35 | -17.11303 | -56.17248 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 0dda62d6-ef7a-3143-b4a7-169f86ba378c | -17.11195 | -56.1575 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 0c32348a-ded8-3b53-9b67-7bf1bf2e8aa5 | -17.11028 | -56.16832 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 6a272b88-c63f-37ea-9889-3fd7d738683d | -17.10864 | -56.15695 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 96a48acc-e5d6-31b6-85c6-98c32eb7ced1 | -17.10808 | -56.16055 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 5b008082-b3ba-30f7-bc6e-00f3651148d2 | -17.10641 | -56.17137 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| facb6d36-336c-3bac-9fcc-b3838eb502c3 | -17.10477 | -56.16 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 0178d5b0-24b1-31db-859b-9041eed22717 | -17.1031 | -56.17082 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 914219bb-6c85-3ab0-8397-755e5b841de4 | -17.10034 | -56.16666 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 48826811-d0f0-330d-844b-2fc22dce0f1c | -17.09923 | -56.17387 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| ef4a4d78-b436-3376-beac-d6b7a8938c2d | -17.09815 | -56.15889 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 47ddfb74-b0b5-30cf-9eea-641fd15591c9 | -17.09703 | -56.1661 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 70a362ba-6111-3a16-9969-8bf2a85dd137 | -17.09647 | -56.16971 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 0a2c5ac1-ed56-3a15-8d97-810442e6d9ec | -17.09483 | -56.15834 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 315f3e94-1b74-32af-815f-0c9ea1273684 | -17.09428 | -56.16195 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| e9fb2486-c421-382f-ad5a-15905d10b674 | -17.09152 | -56.15779 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| a2cbdb6d-261c-3349-9208-3c825b23398e | -17.09097 | -56.1614 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 136cff9a-6a2b-3780-befb-fd14ea780393 | -17.0893 | -56.17221 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 24.3 |
| 646a12fa-836e-3370-9d07-33fad794aed4 | -17.08765 | -56.16084 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 6ae7a8fc-2960-3b78-ad32-04ad0e953e5d | -17.08654 | -56.16805 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 74.8 |
| b4fb130b-43eb-34ab-b220-4d333f616e6d | -17.08599 | -56.17166 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 24.3 |
| c015a79c-181b-302c-ae7a-5f4b5fab681b | -17.08103 | -56.15973 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| bc5a60a5-b307-3571-b182-6a8408bd0620 | -17.08048 | -56.16334 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 61.5 |
| 2fe28fbe-5a24-30e1-b316-932e74f79290 | -17.07992 | -56.16694 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 61.5 |
| 26d070d4-f6e3-327b-85de-d15084019800 | -17.07772 | -56.15918 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 20a132af-0119-30f5-9e7b-1c2d319c56d4 | -17.07717 | -56.16278 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 17.2 |
| 7d6e1c7d-bc9d-30ee-8036-4da7573a5106 | -17.07661 | -56.16639 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 17.2 |
| ec0622bc-7676-3bd7-9705-f2d4509d665c | -17.07549 | -56.1736 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 19778937-8a40-3dd4-8e55-305ee1ba9934 | -17.07441 | -56.15863 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 58b504d2-7d11-3c44-b595-a7066d722fb8 | -17.07274 | -56.16945 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 802f4959-5f4f-3359-8a37-929df91b6815 | -17.07054 | -56.16168 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 0d984a95-d975-3bdc-9a03-81406c4260e5 | -17.06943 | -56.16889 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| b143c5f8-a5a0-335e-9f09-4ccc434a5ecf | -17.06779 | -56.15752 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 49fbc956-da2f-33a5-91d9-ebc47ff18475 | -17.06723 | -56.16113 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 471e23b7-f3c5-30b2-8ccc-1c241be42acc | -17.06336 | -56.16418 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 88ff0bde-1a32-366d-8de4-ac133f8f356c | -17.06281 | -56.16779 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| c378cdcc-15ef-3c4c-bbb2-61b1a7ff43cb | -17.06225 | -56.17139 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 4c7591b1-b99f-3b26-972f-1770dcca0661 | -17.07491 | -56.19938 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 2192f718-3868-3763-926e-45e231b6c91d | -17.07438 | -56.18081 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| cd5f57db-729d-35cc-b1f3-b238be43dd29 | -17.07385 | -56.16223 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 17.2 |
| 65a61246-826f-3752-8124-9ba94cbbddd2 | -17.07383 | -56.18441 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 785c8f6c-a357-3c66-881b-b8e91ed20444 | -17.0733 | -56.16584 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 17.2 |
| c5d04fd0-5cb8-37b6-8460-dba4d7a2c936 | -17.07327 | -56.18801 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| f7430ae1-adb1-3ffc-88ba-c611f233633e | -17.07276 | -56.14734 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 0edf6cef-a586-3184-825e-8576098734ce | -17.07271 | -56.19162 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 6e757dcd-5c4f-31c7-b41c-acd845954b63 | -17.07221 | -56.15094 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3bb6acf1-02aa-391e-a69f-83c3faba40bf | -17.07218 | -56.17305 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| dd2fbfd6-a6c2-3934-8800-90b26af41d9a | -17.07216 | -56.19522 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 96fb0073-f230-3c9a-9aa7-2604921dd5fc | -17.07165 | -56.15455 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| d75a85ee-0619-3147-8775-3ce373e49790 | -17.07163 | -56.17665 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 862c6982-1b88-38ca-bffa-cd804c5ae878 | -17.0716 | -56.19883 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| cefad902-3b93-3564-b3c5-58cabb3aa2d0 | -17.0711 | -56.15807 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 59917158-3714-3469-8332-41b933111efb | -17.07107 | -56.18026 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 7763e2ab-71d8-3a3a-b866-54ac65ce64fa | -17.07056 | -56.13958 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 241500a2-73a9-3eb7-8257-9ec7fcfdd4ca | -17.07052 | -56.18386 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 65ed9956-20f2-3f4e-b0ab-a10357d7fcc1 | -17.06999 | -56.16528 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 0812bdba-7c26-3846-bce0-4bcc1d762955 | -17.06996 | -56.18746 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 3ecb948e-fcca-3c7e-80d7-8a65ac78dce0 | -17.06945 | -56.14679 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f5b0c5cf-9840-3d30-bc88-858a94605037 | -17.0694 | -56.19107 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| e3199009-2d2e-3530-b9e4-dd3f1a138a68 | -17.06937 | -56.21323 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 87c8f275-12ec-32cb-be3e-0a886c7396e5 | -17.0689 | -56.15039 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ad67ad4d-279d-3da9-9a99-300e06bd4350 | -17.06887 | -56.17249 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| ee8ab9bd-a0e5-342d-b53d-357ab4c0c8ce | -17.06885 | -56.19467 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| abd3d975-bbb7-391a-afdf-a3626321331c | -17.06882 | -56.21684 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8d8b3b7b-b490-3fd4-aaac-be333ee82594 | -17.06834 | -56.154 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 8c5e8abd-1aa9-3b31-b716-7ed4c0524175 | -17.06832 | -56.1761 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| f505f0d4-321a-32bf-893a-5e00fa189e97 | -17.06829 | -56.19827 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 837f6caa-bd68-3b7e-9871-c1abfaf7f323 | -17.06776 | -56.1797 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 9e8ca4d1-3d0f-3dfc-9efb-d47ef8188714 | -17.06773 | -56.20188 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| fe1d08f5-6e29-3028-9c45-d1c25d748bc2 | -17.06721 | -56.1833 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3f676819-94e4-3cf2-b067-d6631a800628 | -17.06667 | -56.16473 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 69973db1-d0a0-3441-98f3-f60569a2bfea | -17.06665 | -56.18691 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a43a779a-372d-3132-90b4-0e208633b004 | -17.06614 | -56.14624 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 13e75687-7c9f-3e48-a510-3f727f227a61 | -17.06612 | -56.16834 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| d73aa53c-bc3c-32cf-8932-edbf686b5f59 | -17.06609 | -56.19051 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |


[Clique aqui para ver as próximas entradas](README147.md)
