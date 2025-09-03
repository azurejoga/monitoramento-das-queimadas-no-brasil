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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe12dcec-407e-3432-8f0c-89f44b66657f | -7.00059 | -43.25259 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 840f4a44-29db-3072-b49d-a83dd8bc3778 | -6.83774 | -44.27599 | 2025-09-03 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16127790-ea92-3392-bf34-e289df735428 | -7.2874 | -45.2891 | 2025-09-03 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69ae4aed-d73c-3536-b2a9-41fd4d2c57c7 | -5.61579 | -45.01589 | 2025-09-03 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1fe5ba39-030b-3964-a5b7-54322c9b967b | -5.77337 | -45.28474 | 2025-09-03 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d8465d0-14f9-35cc-952d-f444d80849ff | -6.26357 | -42.63577 | 2025-09-03 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e5b9fa91-dc69-3ecb-a9cf-9ceb278c8c4a | -7.71442 | -50.25489 | 2025-09-03 03:53:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dcfdbaa0-ddfc-3132-8e79-b6ddd66e7327 | -8.06318 | -45.36304 | 2025-09-03 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b153e71e-09b6-32c0-ba57-c2a180c670e8 | -6.64689 | -45.90644 | 2025-09-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ccf32266-8722-3d12-804f-03d8aa6629db | -7.01204 | -44.34958 | 2025-09-03 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cec2bb53-46e7-3dec-adad-7e888146fa1f | -7.11655 | -44.75248 | 2025-09-03 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4523d837-0c17-31e5-a537-0627318a5a7f | -6.30687 | -43.54775 | 2025-09-03 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16206542-107c-35b2-a5aa-5b92a68545b3 | -8.01989 | -44.08376 | 2025-09-03 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8daa0ae8-fc26-3f9a-bdc7-a2764bb13ea5 | -6.90104 | -44.33973 | 2025-09-03 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b941b963-f327-3b6f-8659-11723465ad0a | -6.27616 | -44.51662 | 2025-09-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0afd905c-0a34-33d0-a21e-0aa3257b1997 | -8.01902 | -44.11399 | 2025-09-03 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5f577f27-4d26-31ee-aebd-930e481edc2a | -6.24133 | -42.62718 | 2025-09-03 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cfefec2b-187e-3b6c-ad70-5c5e83638ef6 | -7.9423 | -43.82541 | 2025-09-03 03:53:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 84f7464b-b821-3f8d-b8cc-cb44acc3aa20 | -7.00356 | -43.24022 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5df20603-5f74-32b4-ba96-0db162023bc6 | -6.7417 | -45.15145 | 2025-09-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 981a277b-9b57-348d-bb25-21bf73a104da | -7.98329 | -48.42222 | 2025-09-03 03:53:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a716f38-5c02-3aea-8288-d34574129141 | -7.48547 | -44.81117 | 2025-09-03 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| eeed2866-cd5e-3c39-80fc-6ec008514ae1 | -6.76581 | -43.72349 | 2025-09-03 03:53:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4c472740-f3d3-3f52-bc0f-84f3d80893bb | -7.72284 | -50.25116 | 2025-09-03 03:53:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3971e497-3d84-3a4a-b949-4371ff262e8e | -6.42345 | -43.62333 | 2025-09-03 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37d34ea6-a2f5-3c1e-9cd8-ca4ce4612190 | -7.4891 | -44.81615 | 2025-09-03 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 81ecab0c-7be5-375f-9dcc-e5f79d4a8f4f | -7.01366 | -44.366 | 2025-09-03 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7fea2442-8bab-3c3d-a9d1-ea2af3c03b9e | -6.64726 | -45.90816 | 2025-09-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a6a4f07f-b5d7-3640-86c8-d224f8bccea6 | -6.34574 | -42.55859 | 2025-09-03 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b8413277-5b71-322f-8122-ba091e9b44f8 | -5.88321 | -43.01093 | 2025-09-03 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c75d2ed0-8283-3cef-89df-57dbef602928 | -5.92817 | -43.36732 | 2025-09-03 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4182bef3-cbb4-3155-a1eb-bd5fb911728b | -6.974 | -43.27197 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f3b52dab-7911-3c8b-b6a4-4f64ff1444b5 | -7.48475 | -44.81543 | 2025-09-03 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 05be2ca3-520f-310b-8f1a-38d26b86e6f1 | -7.31621 | -44.26928 | 2025-09-03 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 35576af6-bdf5-3fb5-900b-ea0e966efb50 | -6.99878 | -43.24466 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0bc8a514-c984-3860-9534-98651d575e28 | -6.72759 | -42.26707 | 2025-09-03 03:53:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4641464d-4521-3948-823d-24f4b79399ab | -6.72464 | -42.24654 | 2025-09-03 03:53:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 28454fc2-945d-3d56-9f64-3407a962778d | -6.50714 | -42.19285 | 2025-09-03 03:53:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f45c0bce-8d40-343d-abee-d00fdf9ef4a5 | -5.60518 | -45.02364 | 2025-09-03 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ebff8493-3dda-3d5e-8fe0-919568b5e948 | -7.93412 | -46.5301 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 202d3535-bc11-3198-9d64-633f9525a00d | -5.69604 | -45.94793 | 2025-09-03 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 288f454c-19cd-346d-b0aa-44bf3e563573 | -6.64635 | -45.91329 | 2025-09-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9343e21-34d4-3646-9204-70c0a5757857 | -7.90472 | -46.47865 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 57d4b349-94b4-3fbe-a6f9-1544e62fa1bc | -6.27193 | -43.58276 | 2025-09-03 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0077f8c-b249-3829-8190-639a90801f30 | -7.93571 | -46.52938 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1055d24b-a8d2-3cd0-8629-801ab0ae9f6f | -7.93893 | -46.55869 | 2025-09-03 03:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 92d91b74-9abf-389f-b8f4-8cc6659ffb87 | -6.17061 | -43.31437 | 2025-09-03 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 6ffe06e1-96ec-3d95-9e7c-3269bcfc9539 | -6.28764 | -43.58921 | 2025-09-03 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb4cd53e-39e1-37e2-8e2a-1236f91695f3 | -6.24837 | -42.60876 | 2025-09-03 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4e3b5e5b-5d66-3263-b1a3-54a7c330aa0e | -8.88495 | -45.80672 | 2025-09-03 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d44ab36b-0189-3f7d-ba30-df07bc94cfbe | -6.12411 | -44.13523 | 2025-09-03 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 717eccc8-9728-3698-885b-190fec1a4298 | -6.79086 | -44.09225 | 2025-09-03 03:53:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ba0493b4-8c90-3ab1-8be0-6a3a0310421d | -6.37468 | -43.0052 | 2025-09-03 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e684c0d3-0aa3-38f7-ab5d-58e60d91d383 | -6.54334 | -42.9588 | 2025-09-03 03:53:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e697eb54-200c-382c-ac64-cdfe9502c82e | -6.3245 | -43.51772 | 2025-09-03 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52f67279-2ed1-3562-82a1-f0e03055da92 | -7.12269 | -43.76033 | 2025-09-03 03:53:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2c1a539-da5c-33b8-85c7-43744069391b | -6.83253 | -44.77567 | 2025-09-03 03:53:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cba9cdd7-3752-33a1-966b-535ea222eb33 | -8.1904 | -42.29554 | 2025-09-03 03:53:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6634aea7-f8f4-3f18-b88a-b46f03df3364 | -5.84584 | -43.01554 | 2025-09-03 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6a6c7b65-a97c-3d29-9602-26f3478bca43 | -5.8013 | -43.22992 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2fdc5562-7a45-3b08-8180-652d7102c352 | -5.80648 | -43.22373 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59230142-9b1a-3b3c-8b34-46e4a1db6d40 | -6.29932 | -44.75309 | 2025-09-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 165d549d-df41-39b7-953e-e5dbf865b85d | -6.75252 | -45.92032 | 2025-09-03 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d939dc17-4504-3baf-a8e7-2c2aabf1cef6 | -5.60636 | -45.02197 | 2025-09-03 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9679dc3a-7bf1-3d43-90c7-429fb05407f5 | -7.48766 | -44.82475 | 2025-09-03 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd80e073-7541-3278-98e8-bbbc18f9f2b8 | -5.76174 | -45.29752 | 2025-09-03 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8c027d1b-95ee-310b-85a5-fc8c46b8d04e | -6.68934 | -44.1796 | 2025-09-03 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d16afbc4-2a34-3b43-ae99-dd8254716645 | -7.7966 | -45.45201 | 2025-09-03 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fd3ab0dc-1c31-39bb-9c82-ff2f7fdeb8de | -7.71333 | -48.75232 | 2025-09-03 03:53:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b115cafc-7bc5-3c1e-a40e-495066754dce | -7.70208 | -48.75021 | 2025-09-03 03:53:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 89167716-5045-38f0-8531-1fd08f260a88 | -6.50213 | -43.08428 | 2025-09-03 03:53:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 580e5d5e-4bae-32f6-b8ad-6d523ac8e9c4 | -6.25685 | -42.6052 | 2025-09-03 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b2f53197-b167-3a0a-b2d7-a68695cadc1c | -7.01068 | -43.53209 | 2025-09-03 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0202f0de-5748-334e-8454-57a88d2469b9 | -6.72384 | -42.26656 | 2025-09-03 03:53:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 74f7439a-a9a0-372b-97d9-3e5267a6d539 | -6.70593 | -48.39832 | 2025-09-03 03:53:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 807e5771-83e6-39cc-9b8b-9f6e6061a4c3 | -8.02481 | -44.0546 | 2025-09-03 03:53:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63efa369-20a5-3c08-b36c-9e827c84c6e2 | -5.94351 | -43.71886 | 2025-09-03 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 46e6aec1-da08-3a13-9402-ef453da402f2 | -6.45962 | -49.52829 | 2025-09-03 03:53:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 87698204-9946-3063-86b3-5c48cef727a3 | -5.93916 | -43.04143 | 2025-09-03 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8a1c05d8-e888-3245-b7c5-201b1de6829f | -7.47683 | -44.83599 | 2025-09-03 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d7310076-02fb-3447-83d4-87ac5a51250a | -8.4333 | -45.08481 | 2025-09-03 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2aa2d36c-517c-3f8d-885a-9991e1ccdd90 | -6.34492 | -42.56338 | 2025-09-03 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 745c1617-d7dd-3f9a-9004-589c3b78f747 | -7.01127 | -43.52856 | 2025-09-03 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c986faef-dfaf-3794-8267-eeec6491c0ea | -6.95255 | -43.27869 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 84ca82d1-39d6-3a87-aefa-0eadf49a0a1c | -7.25337 | -43.84986 | 2025-09-03 03:53:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 892e236f-d052-3bcf-b6d9-802fd0fee560 | -5.78224 | -46.45832 | 2025-09-03 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| db6f9867-6a29-3216-8659-fe02c8fc3a6a | -7.94572 | -46.5488 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9e791708-8396-3b47-ae13-2073240b93d3 | -6.22291 | -43.40234 | 2025-09-03 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24d562ce-8e42-3bdc-a774-ec74ef90f4cd | -6.97627 | -43.28284 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c53a5551-634b-30cb-bca9-61032e3aa144 | -5.79954 | -43.24029 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1e58956-cc8f-37a7-bc34-7265ffcf0c27 | -7.10986 | -44.3094 | 2025-09-03 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 511342d9-fb41-316c-a0cc-e9a5e348f020 | -6.54708 | -44.56556 | 2025-09-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f598c1f7-23b4-371a-8657-2b69096f36a7 | -7.50348 | -45.3466 | 2025-09-03 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e5ace58-609a-3091-a694-45ef60eddf87 | -5.43217 | -45.97401 | 2025-09-03 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa2091d9-a08c-31c1-970e-817de9a995f0 | -5.61048 | -45.01978 | 2025-09-03 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e101a142-23cf-3c4f-8d41-25f659368e99 | -7.01806 | -44.36229 | 2025-09-03 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e665c211-5b1e-34bc-b828-45b8f2c78682 | -6.25203 | -42.63398 | 2025-09-03 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f29015bd-3e0e-3500-947b-89cd1b371066 | -8.36053 | -48.313 | 2025-09-03 03:53:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 41ee1465-1839-3025-adb6-aba6ad54b24c | -5.80421 | -45.63152 | 2025-09-03 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 747ceee8-2a6b-36df-8ed9-328b1032639a | -5.93538 | -43.03269 | 2025-09-03 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |


[Clique aqui para ver as próximas entradas](README35.md)
