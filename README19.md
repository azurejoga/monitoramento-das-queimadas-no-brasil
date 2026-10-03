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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9aac4c94-5741-3dc1-8cfc-c6899f659442 | -3.1116 | -53.7234 | 2026-10-03 04:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 21ebb360-90c8-3055-8554-948c9ccfbd03 | -3.13 | -53.7229 | 2026-10-03 04:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| b825c6e2-c13c-3e0a-9a6b-ecd6c7aa3e37 | -3.1116 | -53.7436 | 2026-10-03 04:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 089f35d6-5a87-371b-ae76-5a68727232f0 | -3.1299 | -53.7431 | 2026-10-03 04:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 77aba046-c871-39ec-8590-ec0014c02f74 | -3.13 | -53.7229 | 2026-10-03 04:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 1d7d6e66-6086-3b47-a1f9-f22fb907e914 | -3.1116 | -53.7436 | 2026-10-03 04:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 3f131d77-e874-396a-a61c-e675b53224fb | -3.1116 | -53.7234 | 2026-10-03 04:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 48600660-8e1f-3c68-b76a-61367326c529 | -3.1299 | -53.7431 | 2026-10-03 04:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 77495c9b-9fd1-3db4-a189-57d22a238e1b | -2.96443 | -50.31676 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92454e59-5997-326a-8d7a-fcc1ff310583 | -2.86725 | -51.02625 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f84fb8d-5acd-3243-b724-2ba104986853 | -3.30129 | -50.31797 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46b5bb1e-5b6a-37a5-851c-11d405065746 | -3.10935 | -50.29876 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee2e3b0c-4851-3edc-963e-7c4bf4add49d | -3.28839 | -53.83013 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| aabbce40-e6ea-3521-a7b1-7ad846de8c21 | -0.95647 | -52.33012 | 2026-10-03 04:38:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17571489-1b06-3b4b-bd18-3dc255428ef5 | -3.01296 | -53.88636 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 844c0806-199e-3402-af90-853c98a8b39c | -3.88453 | -51.89392 | 2026-10-03 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff69a3ca-6678-330a-a963-283f4c4d3563 | -2.86686 | -49.05201 | 2026-10-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3db735c7-1c57-3de4-b7a3-7845f2ab16ab | -2.49574 | -48.52631 | 2026-10-03 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4fe5f927-56b2-377e-8681-1c8bcad475c4 | -1.76709 | -55.02535 | 2026-10-03 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cd38b432-cdc7-3cf8-95ba-78be6bdd3f74 | -2.97708 | -53.26335 | 2026-10-03 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 30960932-7fe6-389d-aaeb-3150b1d58e10 | -3.51243 | -51.16311 | 2026-10-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91287632-f2ec-3b58-953f-84f61d319984 | -3.92562 | -45.77681 | 2026-10-03 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc438e22-8302-3d58-aec1-531f575b2dda | -3.77974 | -52.14448 | 2026-10-03 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65f46cd6-78bb-3a13-8885-0f46544110ab | -3.35483 | -43.38377 | 2026-10-03 04:38:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 74f1fb6b-d9ed-33c0-9387-48cee84440f2 | -2.88381 | -54.09164 | 2026-10-03 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6f515a8-7c4f-381a-98de-626112c5f89e | -0.35434 | -52.01355 | 2026-10-03 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9feb0ed2-8377-3344-9312-ea9651945dc9 | -3.12316 | -53.75106 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 50b25404-2d6c-382d-8da0-f3938674ce6d | -1.0849 | -54.102 | 2026-10-03 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48435042-4e30-3d09-8d88-f2efa9f45bf6 | -3.32052 | -51.67538 | 2026-10-03 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 525ab372-c780-3b0c-95f8-c18c3397d626 | -2.8116 | -48.66014 | 2026-10-03 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 23bbb7e6-f59e-35ef-bfb2-f5b07e226d0b | -2.90186 | -54.08335 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47c740e2-caca-37af-9230-747e8bcd781d | -1.26438 | -54.55692 | 2026-10-03 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ff02c7f0-aefa-3b29-8491-68052fd7d153 | -2.2462 | -51.9318 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 33d95450-ecaa-354f-9cb2-3a2e7ee9fcd6 | -4.60544 | -46.78791 | 2026-10-03 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54db4ae1-1873-3502-8c5a-0feb743ad0ca | -1.99299 | -49.65425 | 2026-10-03 04:38:00 | NOAA-21 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce66ee4a-c2cf-3a35-b353-68302f595cc4 | -3.51414 | -54.60135 | 2026-10-03 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8334cdc6-737c-3c75-a812-3036cec06e15 | -2.88064 | -51.02784 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c9f81dc-a138-3c23-941f-47f37d9d9493 | -3.2822 | -53.84336 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f784a14b-6c4d-3cb1-a7ce-43d83d531ec1 | -1.26307 | -54.56507 | 2026-10-03 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| afe9c101-6659-387d-96e1-90c1ca6898c5 | -3.00204 | -53.87749 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 821ef21f-9e58-33e2-9d8c-629a0bc4929d | -3.13055 | -53.75573 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40f437fd-b507-3e41-bba5-37a4e56bd6f1 | -1.44897 | -48.90987 | 2026-10-03 04:38:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c92d9ae0-758f-3556-9244-3713df80ea1f | -2.53753 | -54.01139 | 2026-10-03 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e46cb905-e932-31d5-b7f4-24f9de7fd0be | -2.25704 | -51.9335 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e00fcc9e-b2cc-3fd3-aada-a05883d20f12 | -1.08372 | -54.10963 | 2026-10-03 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 72bb005d-914a-3698-9e22-c945a925919a | -1.08731 | -54.11421 | 2026-10-03 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72bbf7a1-00e1-36e5-a911-b7f8d9c57e05 | -2.89198 | -54.14526 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 009e79d0-e3e3-30b1-bed5-cf921608d689 | -2.57553 | -49.99732 | 2026-10-03 04:38:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27639560-f60c-33c1-9a6d-73ef146dd98f | -3.23229 | -54.30968 | 2026-10-03 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac2d4e0c-8e82-305d-8190-e11a2f130928 | -3.16534 | -54.08145 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e0cc8ad-5f48-395e-969d-99efd201d17b | -0.40742 | -51.99021 | 2026-10-03 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f36fc469-eb61-38ad-8049-8b4edc07d3bb | -3.84129 | -47.81427 | 2026-10-03 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e0fb98c-d508-3f17-b4dd-fb0366f0a287 | -3.06935 | -49.36553 | 2026-10-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2959f19a-02ee-3cab-a943-578d78c75f48 | -4.07178 | -50.32937 | 2026-10-03 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 348fd9b1-5fc8-3d7d-858c-cb29be44e327 | -1.61066 | -54.75844 | 2026-10-03 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa3016e0-4ae4-3e37-9bc6-a2b41ba4d862 | -3.29682 | -50.32457 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 512db6d2-aded-30c5-9178-d0fd6ad82a3c | -3.05984 | -54.16479 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87ee8001-2aa9-3c44-a911-5b0b64f4b69d | -2.97354 | -54.20829 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc78a38d-2910-39b4-a6a6-efbecedc72ed | -3.14016 | -53.74672 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c93139f9-faa8-3f45-b6b6-a4b415437c26 | -0.45677 | -52.17381 | 2026-10-03 04:38:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cbbfc3e-b658-3bfd-a633-5931594efa2a | -4.4508 | -47.92282 | 2026-10-03 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| dfebb489-6dfb-3e65-b5fb-cf26622b64b4 | -3.55788 | -52.25134 | 2026-10-03 04:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b418a8e3-6598-3c16-a6e6-e88513dc38cb | -2.92883 | -54.15103 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a6322bf-894d-37fc-8c96-f6888fc20114 | -3.1827 | -54.10264 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70b2fa9f-f489-3c57-b9a8-a255150d7bc2 | 0.98725 | -50.01294 | 2026-10-03 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57e0843d-69fd-362c-816a-f1a31c116bc4 | -0.46051 | -52.17443 | 2026-10-03 04:38:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72ce7347-a321-35d5-a7cf-84b83e5c5113 | -4.90904 | -45.70564 | 2026-10-03 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee38f799-8225-3add-94d0-a945a186b479 | -3.77681 | -52.13974 | 2026-10-03 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58a36981-a7a0-3410-90ff-c3b2c2688ce9 | -2.91184 | -54.12582 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48ff9ad7-9110-34c5-8783-65ed79dfa911 | -3.5128 | -51.16367 | 2026-10-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c421d678-163e-34fa-9bf1-1974e7a08d1d | -3.20876 | -50.40246 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e2023fc2-4986-3f1d-b3f5-6522df2bff06 | -3.1694 | -54.08205 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11f34d8f-512d-3fa1-966c-aabdf2f265ef | -2.97144 | -54.09154 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ecf5965-b44f-36a9-bb86-1dae6a6d4379 | -3.1746 | -54.10121 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f612b020-6383-3117-892c-8c79d4e2ce3a | -3.13 | -53.75916 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 53e739d3-9e95-3d67-93af-c2231ed79bdc | -3.28729 | -53.83703 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 686b85ca-ce26-3998-97e8-b18333551b53 | -3.07275 | -54.37224 | 2026-10-03 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36daedb9-114a-39b9-b916-1746ce08c1ac | -3.00355 | -54.23133 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1b164642-bee2-37d5-8111-d021c0247315 | -3.13277 | -53.74205 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4665dad4-5a07-31d5-a2c1-404cf3fe17ba | -2.97085 | -54.09515 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 960cbe35-bc42-3eef-8074-a87953cfcc70 | -3.71547 | -50.66176 | 2026-10-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04549f02-4696-3690-afd1-2391dd41dc14 | -0.46799 | -52.17564 | 2026-10-03 04:38:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6de782d-eddc-3a85-8bfa-df9f2bbf3b46 | -4.09222 | -50.45592 | 2026-10-03 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d7df6aae-fc76-3339-94c3-269f8f47f0ed | -3.81947 | -52.20876 | 2026-10-03 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2c6d20f-1824-3e7d-b26c-bd2ae6021fe7 | -4.45957 | -47.92747 | 2026-10-03 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 69ecf782-ba2e-34d9-acea-11f54441dbe8 | -2.15057 | -47.75137 | 2026-10-03 04:38:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 81780d66-6f4d-39b2-83c8-2907314611f1 | -2.43958 | -54.83027 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5a97687-35c1-3cdd-bdf4-0434665885f3 | -2.15769 | -47.55173 | 2026-10-03 04:38:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 94b33da1-5c6f-313a-a550-768c472eb4c9 | -3.13111 | -53.75232 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce1517dc-f573-3b96-a624-71ae0933dfba | 1.78558 | -55.59774 | 2026-10-03 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 344f7d0c-2195-3a2b-9b41-9e0d79a4675c | -3.71209 | -50.66122 | 2026-10-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| fea34002-dd2d-33cb-b157-fd9dcfc1e874 | -2.97323 | -53.26269 | 2026-10-03 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 734b0eff-6e46-3a39-b489-56e9af2ad78a | -3.56174 | -53.0597 | 2026-10-03 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| da84d67a-507c-3705-8dbb-71073d79c3a6 | -3.26253 | -49.52274 | 2026-10-03 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c72ca1ad-edbf-35b9-b5f2-8d99d9cfd366 | 1.7509 | -50.8081 | 2026-10-03 04:38:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.2 |
| f4592f06-213f-39b4-8e0b-3af6fd2476df | -4.56859 | -46.58299 | 2026-10-03 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 439cf374-1759-378b-999b-2b622f3e362a | 1.90995 | -55.80811 | 2026-10-03 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a90d647-e9ae-37ee-b313-c7d398b453cc | -2.86783 | -51.0225 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0460a337-c0b5-3108-b14c-afab960739e0 | -2.90128 | -54.08697 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f38d7236-cf79-36ad-b5df-525b5753d403 | -2.04996 | -56.86382 | 2026-10-03 04:38:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README20.md)
