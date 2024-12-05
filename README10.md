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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76b9f575-2331-3548-8f6b-967cc8459d09 | -3.26754 | -53.86642 | 2024-12-05 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 340f7c3c-af7a-3df9-a952-f997a51be19f | -2.8212 | -53.0649 | 2024-12-05 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb5e5f7d-57db-38ce-968d-5c4939d57f8b | -1.57256 | -46.03484 | 2024-12-05 04:46:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef1f2dc7-c596-35e9-98cc-3ed262d9ba3a | -3.25821 | -53.66841 | 2024-12-05 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f86498ba-7c36-3427-9277-b0f0acf91a6e | -1.8803 | -53.30292 | 2024-12-05 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c6175998-e073-35ea-861d-f4eede0d76c3 | -2.82533 | -53.06153 | 2024-12-05 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e8ee702b-43bd-3613-b216-163ee2fef4d7 | -3.09689 | -51.31532 | 2024-12-05 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8736073-27de-3a0b-99b9-a99c7d36b86f | -2.32035 | -53.90435 | 2024-12-05 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 819b89fc-66b6-31ed-8e5c-7e07ec52535f | -4.49231 | -50.24157 | 2024-12-05 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df99760d-184d-3362-9629-711b48ee5041 | -4.08334 | -50.74939 | 2024-12-05 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c1c76d5-fa5b-3257-8e7e-223920a5d1f7 | -4.00577 | -53.43752 | 2024-12-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a60c8c23-d576-36ac-8b9f-12ddbcca453a | -1.71141 | -52.44533 | 2024-12-05 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09372eee-1fa7-3190-b8ea-bd82755025a0 | -5.57558 | -45.15423 | 2024-12-05 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea17d1e5-bf1d-3f2b-a7a6-e85891a07127 | -3.45344 | -54.34409 | 2024-12-05 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9eeeec3-1878-3066-918c-c1ae2703d426 | 0.70312 | -59.87416 | 2024-12-05 04:46:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a3b73d5-e5e3-32d2-a155-9f34f507bff2 | -0.85691 | -52.71226 | 2024-12-05 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0a6cd576-2774-350d-a092-93c7214c14f1 | -2.80715 | -53.06274 | 2024-12-05 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 50d50513-18b4-3d4b-bf96-80c4d6fc685b | -1.6812 | -54.44917 | 2024-12-05 04:46:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 376486ec-e5af-3161-be52-8c6450b18803 | -6.94601 | -43.52578 | 2024-12-05 04:46:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee7a01a1-a556-3b80-8cff-db8326655ca8 | -1.03734 | -53.55845 | 2024-12-05 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 02914726-93bb-3bda-8217-c890ae79e407 | -3.57505 | -54.69569 | 2024-12-05 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6fc5fbd4-e9cf-3f3a-90b0-2d3ab2fd22c3 | -4.07333 | -50.02735 | 2024-12-05 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51952913-9c6a-3343-acc1-33b089e938fa | -1.18063 | -53.43078 | 2024-12-05 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 51c79f17-6ae5-319f-a8af-4b2d98aebd19 | -3.1892 | -54.51321 | 2024-12-05 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 51a3cef4-ae2b-3cd5-a2e7-85b631321aaf | -2.8183 | -53.06045 | 2024-12-05 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5899750a-fd5b-3dda-85b6-f788a1984b9f | -2.98255 | -51.4369 | 2024-12-05 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32fb7890-b306-3cb7-a2d2-0f1f994765da | -1.63316 | -52.3866 | 2024-12-05 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7646e658-d3b1-30bf-8631-1ae984693dac | -1.15713 | -53.41415 | 2024-12-05 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3b1859c-c19c-3857-8d18-ff0a5dd8d0ac | 0.16664 | -60.59233 | 2024-12-05 04:46:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b7eb3be3-4383-3148-b04c-20a86bd4d5f5 | -1.08474 | -53.22918 | 2024-12-05 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f9935a3-5891-3c75-bdb3-98e7f0627c77 | -5.58354 | -45.15953 | 2024-12-05 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ff084e6-1fb0-3b75-abdc-7061ed583c93 | -6.11608 | -46.5957 | 2024-12-05 04:46:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| efb1b009-f85e-3ae8-9d46-76e6f2800011 | -2.00023 | -53.27865 | 2024-12-05 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf5fa539-d152-3574-8d37-9bbca9e4703a | -2.48459 | -54.03169 | 2024-12-05 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f9bf027-7fbd-3eee-afb5-2c649cd4f711 | -4.67263 | -47.92089 | 2024-12-05 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 428d6629-de49-36b2-bdc9-e6f8173414d5 | -1.16757 | -54.19118 | 2024-12-05 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e33f81be-4faf-3164-b53a-395e1b31b4dd | -4.7258 | -45.6936 | 2024-12-05 04:46:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb542a4e-6da1-3027-8973-e6048c281a88 | -1.71892 | -45.78191 | 2024-12-05 04:46:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8b6e7f8-9bb0-3753-aea2-e1a14f6a5065 | -4.07279 | -50.03083 | 2024-12-05 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e4893808-2482-3036-ab83-fe72e11d96b7 | -4.40302 | -45.9264 | 2024-12-05 04:46:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6094cc5e-4e5d-35e0-8235-f13fc7f585a1 | -1.54759 | -45.53263 | 2024-12-05 04:46:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d2613f9c-b712-34fc-b5e0-c7363d08a689 | -1.69508 | -52.57146 | 2024-12-05 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 32b85741-5af5-3f29-8970-ae2836372ebf | -2.82058 | -53.06882 | 2024-12-05 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54b87356-98e1-3589-8795-6769ee35ee4e | -2.52599 | -53.97816 | 2024-12-05 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6cafc5a-04d6-3d50-8da3-04e0850e88f3 | -2.83235 | -53.06262 | 2024-12-05 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 72d29e46-12f8-389c-adea-1f3983d39109 | -1.7107 | -52.79164 | 2024-12-05 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98cc52d4-5641-3e35-913f-c7ef241bd8de | -1.14814 | -53.75508 | 2024-12-05 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf906c96-76be-3098-839f-5a62c0ec477c | -4.67202 | -47.92494 | 2024-12-05 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e7f842e5-faca-32a8-9b0a-d5197c04a1a1 | -3.57125 | -54.69509 | 2024-12-05 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| abc12c0a-f717-3044-b5f9-629f5d3a36c5 | -2.1637 | -54.61786 | 2024-12-05 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 068a821c-6a18-30f8-8fd0-779d7f2794df | -2.81355 | -53.06773 | 2024-12-05 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c1426932-c584-3cf6-aec0-c60d2f970546 | -2.57171 | -53.97593 | 2024-12-05 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7aa88549-06ac-3f06-a5b9-85675593794c | -2.1668 | -54.62323 | 2024-12-05 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 616c4ecd-34f5-3668-a0a8-4a99617ffbc2 | -1.62963 | -53.53406 | 2024-12-05 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a8b2ca0-ce02-3bbb-8c79-c165e9ec9bdb | 0.75012 | -59.65873 | 2024-12-05 04:46:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 611be984-6ca5-3808-81b2-d6d41a01265c | -1.87998 | -46.38522 | 2024-12-05 04:46:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c3a8c907-03f6-3e10-99ef-4d6a98b12df2 | -1.92713 | -51.46668 | 2024-12-05 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e7ec9c92-0cd6-3ca2-b347-5e8e1b2c7a78 | -1.69754 | -52.64657 | 2024-12-05 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02e7dd22-4e1d-3338-a4c6-e3f061001de7 | -2.3514 | -54.50759 | 2024-12-05 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d61fbbf-4868-3e71-8305-e8b8354e811a | -6.93922 | -42.82793 | 2024-12-05 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a148d663-9e7c-3930-b9d2-0eb4575201dd | -1.62599 | -53.53347 | 2024-12-05 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b39a60c5-b4bb-3725-987a-89e3463c563a | -3.46112 | -54.65602 | 2024-12-05 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41e86872-ff27-3269-9399-77fdec7aae47 | -11.94753 | -55.14867 | 2024-12-05 04:48:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5bde54bb-6f4b-3c40-ab8c-9bca8e91c126 | -11.20476 | -53.8226 | 2024-12-05 04:48:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d7806590-8556-3661-8f69-a7751bb89c60 | -11.4903 | -54.03492 | 2024-12-05 04:48:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ecad53d6-4c91-3282-9e84-6c25c882b981 | -11.20755 | -53.82678 | 2024-12-05 04:48:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9a45a12b-ceb8-3526-9289-c6c8a7ff3272 | -11.94687 | -55.15265 | 2024-12-05 04:48:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 572d6ae6-0889-3be4-8d08-11d51d0b3e52 | -13.35781 | -41.34195 | 2024-12-05 04:48:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b74523c2-6d83-3cf9-9fb3-83a9442aa643 | -12.15056 | -55.17321 | 2024-12-05 04:48:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 962296c6-2fa1-3292-949c-b65fc4c0d013 | -13.36396 | -41.34275 | 2024-12-05 04:48:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| afcf70e5-a021-3cde-a5c9-07cb67922c73 | -11.32216 | -54.33595 | 2024-12-05 04:48:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b686be88-12f1-3140-91bd-806f991af494 | -11.36076 | -54.4857 | 2024-12-05 04:48:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b04fe7b1-0134-3f6e-888a-ecca94cd33fc | -11.94819 | -55.14469 | 2024-12-05 04:48:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c23500e6-da12-3b0f-96c8-04245192dd0d | -10.82084 | -44.36764 | 2024-12-05 04:48:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49909e16-943a-3ff6-8514-14ad848807fd | -12.15756 | -55.17441 | 2024-12-05 04:48:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3ca053d-bd22-3c6e-b9c1-d165d8f007f0 | -11.48443 | -54.85028 | 2024-12-05 04:48:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 008aa303-5efd-3626-be1d-aca283d911d7 | -11.31875 | -54.33538 | 2024-12-05 04:48:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 632de2fe-54d8-351a-a509-feca713f67b2 | -11.20813 | -53.82314 | 2024-12-05 04:48:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 369891d2-48c7-3c95-a4cb-6b06f71ab610 | -12.15406 | -55.17381 | 2024-12-05 04:48:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31b0684a-9192-307c-b587-bf4fa42ebf1b | -9.8967 | -44.34875 | 2024-12-05 04:48:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b79c79d-fd3a-3c1e-88d2-cc3c59b77f2d | -11.36013 | -54.48949 | 2024-12-05 04:48:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7673d305-70e2-30d7-97e7-c6087ef33195 | -15.07839 | -59.64769 | 2024-12-05 04:50:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 38b06aee-0ddd-38e6-9f05-0db52e55dc2d | -15.09102 | -59.62793 | 2024-12-05 04:50:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b503132d-a307-34db-85be-d6a71822d01d | -15.08192 | -59.65284 | 2024-12-05 04:50:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b616b8b-6f19-3c23-82eb-db53d7fb87c5 | -15.07645 | -59.63402 | 2024-12-05 04:50:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b20665fa-7b59-3d63-99a7-6acf0a989bda | -19.16529 | -40.13958 | 2024-12-05 04:50:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| f5add512-fda5-3ce4-9d47-3be348437298 | -19.17653 | -54.99589 | 2024-12-05 04:50:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 49139150-c7e5-3721-9d5a-1e034c8bdd22 | -19.16723 | -40.14211 | 2024-12-05 04:50:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 258d0100-519b-351c-ae7b-ee533c111595 | -15.07326 | -59.65113 | 2024-12-05 04:50:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc278a52-bf2f-3c33-b4fa-939ebac59952 | -15.06893 | -59.65032 | 2024-12-05 04:50:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f46c0ceb-6d78-35bf-85c5-edb2a3987612 | -15.06812 | -59.65462 | 2024-12-05 04:50:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88ca79ac-fc15-346e-b577-8f5e23583616 | -15.07759 | -59.65198 | 2024-12-05 04:50:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a51d404-0b40-3f86-b4e2-b9282d25cbb9 | -15.08078 | -59.63483 | 2024-12-05 04:50:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7893c62-125a-346a-ae1a-27767d4bc32e | -19.16781 | -40.13514 | 2024-12-05 04:50:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 60e6609a-8303-3e8c-9adb-6497fe49ca45 | -15.09454 | -59.63308 | 2024-12-05 04:50:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ab0a69c0-9f29-3c68-9c61-42becbc7a964 | -15.07725 | -59.62972 | 2024-12-05 04:50:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3229d31-88d6-3904-905f-206d05e97479 | -15.09023 | -59.63219 | 2024-12-05 04:50:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f4d04c37-b3c4-399f-b41b-294d2543d69f | -19.16556 | -40.13711 | 2024-12-05 04:53:00 | AQUA_M-M | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 6041846b-e16f-39d6-8dc5-e00c2ea8da19 | -25.19399 | -49.32602 | 2024-12-05 04:53:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fb1723a9-ec9e-33ea-87fe-3f58ecccd70c | -23.2707 | -51.20701 | 2024-12-05 04:53:00 | NOAA-21 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README11.md)
