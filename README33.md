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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95c3d9b3-9c58-3485-a688-f9529c8a3d0b | -2.57138 | -46.1842 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5dc877cc-7d92-339f-b1fa-81070859316d | -2.12884 | -50.82534 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 850322e4-db9d-353c-a284-a7c071f8315c | -0.90112 | -51.76192 | 2024-11-09 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76d42ffb-963d-3b00-849a-f1ff56698ce8 | -2.63053 | -46.78847 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7e49c214-b4b1-3da6-8bea-23a605e518f9 | -2.57079 | -47.34491 | 2024-11-09 04:31:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 598b0ee1-223d-3e7e-802f-995208ea6de7 | -2.58438 | -49.12849 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| acfedf77-f98d-328a-b0a7-246dfb3b0024 | -2.37548 | -48.57677 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 17760d50-caac-3f88-9ac1-6224b00312cb | -2.47706 | -48.53434 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce2fbd12-36bc-3030-a2cd-7cae170ca355 | -2.19463 | -46.7698 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea523f9a-ac78-3734-8fe2-7828606e6ad0 | -3.29368 | -43.54041 | 2024-11-09 04:31:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a00b5ea-c7d0-3749-bb87-72dca030c315 | -2.34807 | -46.65694 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b84e267a-72dc-30af-9c4c-8deaf2cc6500 | -2.02818 | -48.01138 | 2024-11-09 04:31:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50c960f0-e1b1-3a8d-bfdc-a4e8c8e49300 | -2.25891 | -46.46611 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c41ad9e-dbdc-3fb5-8000-377c8cb4270a | -2.40103 | -46.79881 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02136a94-7598-3168-91ab-3f51adfe7f97 | 0.04814 | -49.5446 | 2024-11-09 04:31:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 01c33172-ef9e-37fb-af97-89ddf0098158 | -0.3337 | -51.57912 | 2024-11-09 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| daea4fb3-3359-3182-b753-0bb23526029d | -2.30676 | -50.46724 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b718593b-5927-31fe-b2a6-d22746018453 | -2.18567 | -48.37576 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2a8b82e-e654-35af-8e7d-2b42e4ac6834 | -2.29121 | -46.50008 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7ed4ab5-c8b4-3eb7-9f5c-643c25a175fc | -2.11643 | -50.14883 | 2024-11-09 04:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5d1c3f8-729a-3852-a0ed-e749149f4e6c | -2.21907 | -50.61811 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7552b2fd-6724-363c-8316-1f23f0b94cb5 | -2.92971 | -47.02881 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 235c0072-3cb0-3ea6-91e2-0524f9cbc91a | -2.64038 | -46.06934 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| acd69d92-309c-340a-b987-023336cd6964 | -2.22864 | -48.48821 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7fee077-22c8-3802-baf5-316dc761e37f | -2.33221 | -48.58848 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69d8893b-c692-32d6-b8d1-91e6f4356792 | -3.14514 | -45.9481 | 2024-11-09 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53b30965-6f80-3db9-9238-bc2b831cf408 | -0.80977 | -52.49884 | 2024-11-09 04:31:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 79750ab1-83c6-3144-ba33-f2af19a0fc08 | -2.07827 | -48.41045 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd10e974-dad4-3810-a177-bb920e6a4e74 | -2.12456 | -49.01636 | 2024-11-09 04:31:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd52950d-84b0-3a13-a155-3a7c1bd994c1 | -1.14661 | -53.65573 | 2024-11-09 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9a22e096-e313-3b7e-8401-e9020c29df6e | -2.21037 | -48.84841 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2914925a-46fc-3dd8-b1c8-37ebf036c07a | -1.83212 | -53.72547 | 2024-11-09 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0396c901-0c78-3233-b092-f53eec24bdb6 | -2.15158 | -49.13505 | 2024-11-09 04:31:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 64ab6d1a-dfc5-389d-bf4d-747784e1fd11 | -2.235 | -46.55423 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c476e4af-ac41-3691-9342-cb7f36772425 | -2.23608 | -46.54735 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 834ba0df-15c9-31d0-9007-e1ae2eed210a | -2.15578 | -46.6935 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28ca7b25-a407-3bcb-b68b-7cccaec703b2 | -2.56367 | -48.23895 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3d2e9d8-012d-3a71-a701-f68183a0e18d | -1.51852 | -52.18919 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 76eb9099-917b-3e53-ace3-3a8ec51b2d5b | -2.28011 | -50.67961 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9ae08143-be11-3197-b720-a42f9e993b0c | -2.49113 | -47.22725 | 2024-11-09 04:31:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8ad7721-bf8e-3544-b8e6-1823898572f3 | -2.42437 | -48.47502 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25db8c10-14ba-34bb-857a-16a9f657e549 | -2.41031 | -48.52038 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| a250616e-c5a8-3792-b782-ca2c02ff5b67 | -3.55183 | -43.57132 | 2024-11-09 04:31:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 39dd3360-016a-31f3-9eec-352a39cff5ee | 3.74611 | -51.62135 | 2024-11-09 04:31:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a384d515-a072-398f-94e6-7dd5127ac88f | -2.51572 | -46.36802 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec97cb7c-3c7a-3284-8dfe-0b4af0779b76 | -0.04292 | -50.78599 | 2024-11-09 04:31:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bbabd64f-91ff-3e2b-be80-fad012099675 | -2.09002 | -46.52489 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4e426d4-5bc7-33ec-9c59-ba52fcc26ef8 | -2.29546 | -46.71223 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27c9e7f6-a43a-33c6-93b1-71e765ccaee1 | -2.57075 | -46.16623 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72ea42a1-5d16-3e14-9e25-19a9ff35b114 | -1.9539 | -46.30546 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f7940f2-6e81-3679-85df-74364f5d6e54 | -2.15489 | -48.35281 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6933973a-4d4d-3b26-9ee3-ff66a239b2d6 | -2.07473 | -48.79778 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b1adaa5-cc03-3fc8-99fe-538e360a46c6 | -1.52673 | -52.19046 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 6897a108-08a0-30f9-a4e2-c6be423bdb94 | -1.15198 | -53.65537 | 2024-11-09 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 82a6a227-1a31-387e-a5b4-f5ee9a2c5ba1 | 0.02057 | -49.41638 | 2024-11-09 04:31:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b2506893-aab3-3246-9517-d96ee9b6a2c7 | -2.46353 | -46.87879 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1cd2e06-d091-3503-8424-9907a7865199 | -1.57291 | -54.63702 | 2024-11-09 04:31:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34df3097-b54a-3269-9e59-cf2b10c4915e | -1.52444 | -52.63967 | 2024-11-09 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9879208d-7a03-3d5e-917f-6400189dddbb | 1.71779 | -50.81524 | 2024-11-09 04:31:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fac8751f-edf7-3b49-b85d-b48bf978225e | -2.13594 | -48.73999 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f609c0e6-a8e8-3f34-8fb9-3df10a9a7a44 | -2.84004 | -48.47023 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4dfbe8df-ae11-33f8-8b36-28b48ee7d48b | -1.38119 | -51.41323 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f1701615-345d-3a88-b662-6c7a750cc8a3 | -2.56031 | -46.18964 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5e68095-a079-361a-9811-7521433a4d09 | -0.08022 | -51.40432 | 2024-11-09 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37c4615b-23c7-3ab1-b136-204944cc9fdc | -2.39824 | -46.18282 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8275bd5d-a171-3617-b827-ab84b02648b7 | -2.21847 | -46.68202 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4e774e0-39f6-36af-b491-27d029f5d151 | 0.81507 | -51.88412 | 2024-11-09 04:31:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 256e5c99-31fc-3dcc-9f9d-83332e028c1b | -2.05404 | -50.75637 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 210892a6-6b62-3ecc-9890-e588e5e16943 | -2.20405 | -48.36033 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1a00fb4-73fe-3e21-97f6-9ed1c50ab221 | -2.43451 | -46.25602 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bd7576b-632e-34c9-990b-c9ef48e2b032 | -2.36703 | -48.54242 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d31920e-adf6-384d-be82-502d7ca6c9b0 | -2.00288 | -49.00936 | 2024-11-09 04:31:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9d3c3715-6b42-3fa9-a9be-f2c8c5f3105e | -2.13697 | -48.73994 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 88432ed8-e5cb-3a98-ad85-fe3b9bb29182 | -2.53599 | -47.30792 | 2024-11-09 04:31:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 211e25da-8a62-3e22-8d62-7ee84e3bd9b6 | -2.39968 | -48.50045 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60ebbda6-b9af-3405-9e04-32c6fc335e39 | -3.14342 | -45.93693 | 2024-11-09 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff0c8718-7456-368b-9e03-beb3e7458856 | -2.30347 | -48.63935 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 154d16ea-260c-3272-9589-62c2eed0728f | -2.40361 | -48.49739 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01fac7e5-4e31-3ece-8e17-253b284690d6 | -2.80259 | -46.64642 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4baafbbf-4054-3a91-b52f-02bdf01f88a0 | -3.11318 | -45.96108 | 2024-11-09 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c07183d-3257-3b47-8fed-8a53b5a207cd | -2.24414 | -46.49564 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a302d5ca-129c-38e0-a832-9dc06135b17f | -1.24798 | -51.76678 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1edc48c0-453a-3da0-9f33-da9187b4e978 | -2.08671 | -46.52438 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09bbbb4b-a8b7-3108-bee3-93fd86f2a5d4 | -1.32107 | -54.64241 | 2024-11-09 04:31:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e6200270-69ff-38c6-bcb8-e3d611a34530 | -2.19117 | -48.31844 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c94089c2-2a84-3597-96fe-5bd38c7122ef | -2.41828 | -48.93327 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db0cf0de-c0d5-378b-8592-69cdb543ab2f | -2.21633 | -50.77957 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89c3d8f8-cd48-33bb-a7a6-c8c6b04d6ddf | -1.21656 | -51.7723 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3889a3ad-1395-347b-992b-bebcd7dea6c7 | -2.1772 | -48.31991 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c41f1b51-7c63-303a-ac3f-f47c087dad78 | -1.41354 | -55.38005 | 2024-11-09 04:31:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3afd2c3b-c104-3913-a977-4c90f5a0a34c | -2.12186 | -48.56371 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36718615-b330-39c1-a9d2-427d5c05e812 | -2.10131 | -46.21143 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1185240-ba41-3e4c-9869-d3fb12c94faa | -2.18491 | -46.44059 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49b92e35-f303-35ce-89c4-664c1c150a8b | -2.09475 | -46.4727 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a981ec3-909f-314e-85c6-50695ce1acc7 | 2.46159 | -51.06665 | 2024-11-09 04:31:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c58c9a3f-aa6b-3998-b5c7-52b2f97b3601 | -2.23928 | -48.37667 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ffd3b61-2eb3-3557-991e-194f4beb7762 | -2.27737 | -46.85007 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 162ccdbf-77a6-379b-8a9f-7e92f49635f9 | -1.50974 | -52.16539 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fae8b9c2-f5d4-37ab-975d-1911296dc360 | -2.6126 | -46.24772 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06e8efb5-75e7-378e-8f94-e101ed369932 | -2.49496 | -47.22433 | 2024-11-09 04:31:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README34.md)
