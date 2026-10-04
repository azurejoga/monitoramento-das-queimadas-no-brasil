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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 460663f4-ea78-349c-8dea-a09dd5bac26c | -3.47051 | -50.09129 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 22527f87-1d46-3ff7-8aaa-0f39ed5d138d | -2.88974 | -54.1476 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1dcc06eb-b17f-3627-953c-3421aa21edc1 | -6.2093 | -52.79973 | 2026-10-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0170eb7-b22c-3a62-814a-029753d5680c | -3.00701 | -53.87986 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f05f8b7-d06d-3895-8b38-7d9d9412fcc2 | -3.49036 | -59.36972 | 2026-10-04 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56e7597e-2201-3428-866e-90e63e14dedc | 1.76399 | -55.64244 | 2026-10-04 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c649497e-2818-3b7c-8a97-86e4b66e2936 | -3.16288 | -59.09045 | 2026-10-04 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b39153b-b249-3f4f-bc0b-d55fe972ffff | -2.5394 | -58.03405 | 2026-10-04 05:16:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 31920561-919c-3029-bd01-e8afce6c5d16 | -4.26077 | -46.37485 | 2026-10-04 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6b1c7eb3-c963-3698-bafc-de04aea1d776 | -3.12704 | -53.75538 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e915f03-ad64-3580-8b45-925d65b27ae8 | -2.96749 | -54.09055 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92fd45ae-67de-3ec8-84bd-f64814fe4119 | -3.12829 | -53.74715 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef9cf96b-27d6-3b36-a473-07fc0d8d09f7 | -3.17995 | -57.91332 | 2026-10-04 05:16:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ec0c5350-e33b-3bd9-a226-b527738ecc3d | -3.5181 | -54.61587 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fdca2999-0966-348c-adf5-5f83f7345c41 | -2.80023 | -54.09521 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f965d53c-a645-3e98-a855-51b696115d25 | -3.18502 | -57.86002 | 2026-10-04 05:16:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b592628b-6070-36f2-a82b-695fbc9d6122 | -3.87041 | -55.80742 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 40430e2a-9ee5-3e29-b48a-36669879bf3b | -2.21588 | -51.96039 | 2026-10-04 05:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd85b8a8-193e-31ac-8c27-42d9844755d9 | -2.15453 | -59.23027 | 2026-10-04 05:16:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7966c69c-ce61-3678-8eb3-93769497e771 | -1.40266 | -49.26479 | 2026-10-04 05:16:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 704a186f-af93-3b5a-91d9-a949b79f005a | -3.78628 | -59.37873 | 2026-10-04 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a421d17-8c18-36ab-a086-e929db943eb4 | -3.13439 | -53.73124 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b73b96e4-fadb-3505-86ed-ff231130360f | -2.9698 | -54.09898 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6808ac07-931d-32e8-ba84-978b82601193 | -2.92817 | -53.94666 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d18a297f-062e-3372-8594-630e5215172d | -3.13862 | -53.72768 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5ee4ecc7-2ded-328f-9992-e3bb4a30490f | -3.11593 | -53.72129 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 199a043e-ea86-303c-837a-bc1766c0d621 | -1.62267 | -55.00882 | 2026-10-04 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2a236ae-572b-392f-84e0-f5beea52cab8 | -4.46675 | -54.97414 | 2026-10-04 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85b5620e-815a-3cc0-9c58-9d6fce99c501 | -3.13314 | -53.73948 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc89e864-6457-35f7-b383-7551b7c0c169 | -3.30041 | -59.40053 | 2026-10-04 05:16:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d23a8c84-ca7f-3eb9-8c44-d0b9c873e2ca | -3.00639 | -53.88391 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f024ca6f-aa0b-34a4-b4a8-8e67b2a61530 | -6.19743 | -52.79811 | 2026-10-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 109c539b-1497-3467-b639-14a21563d065 | -3.10615 | -53.73664 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0db8b55a-71d1-31e5-ae14-84e253e8ebd1 | -2.24188 | -51.91962 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b08573e9-8a1d-385a-b098-b662a70483f0 | -3.18927 | -54.08294 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 213e5f81-9fb2-3259-ba4d-f8e13e5e2868 | -2.82822 | -54.12365 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 117145a8-a335-3352-8c1e-4e3d8b59d89b | -2.8218 | -54.11864 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 863403d5-5c2e-3a6d-91a5-ab08ff2bac4d | -3.6564 | -55.5013 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c0799991-7658-3cec-9fb2-be3e96bfea82 | 1.75901 | -55.65376 | 2026-10-04 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a4377eb-91bb-3c91-851b-42c8a47f3531 | -2.77417 | -57.68753 | 2026-10-04 05:16:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 69a536ef-7298-30af-9fb1-0158608e3276 | -3.04479 | -54.21917 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ca27d050-9996-3cd5-a487-69edeff4473f | 1.7596 | -55.63609 | 2026-10-04 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e2418d7-994d-3e61-8f3b-09aad4341d90 | -6.20535 | -52.79916 | 2026-10-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf4fd8a7-a4e2-3eb3-b343-be529e2fd3f6 | -3.17572 | -54.07691 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba5fa6d7-d39e-3042-a242-0204c88f9cf9 | -3.00468 | -53.8712 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d2744b94-e679-3f98-92ee-8ce6947c9b80 | -2.87287 | -54.11691 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2322beaf-6fc6-334a-9f77-f686de74b59a | -2.89047 | -54.11965 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6e8753a7-e0e8-34f5-aa80-01c2dfa139ae | -3.42649 | -59.5642 | 2026-10-04 05:16:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7073fda5-b032-34c4-a1e5-2eb2345d94a5 | -5.22588 | -48.4125 | 2026-10-04 05:16:00 | NOAA-20 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd5e7129-72bb-3cf8-b666-10e522cdf67e | -3.7296 | -57.14949 | 2026-10-04 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d293d7e-55e6-36aa-ae0e-b7913a4b97f4 | -1.16649 | -49.27335 | 2026-10-04 05:16:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4050faf-4b10-3a52-afca-7672315ca7d2 | -2.80957 | -54.1047 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2dfd4393-f75b-39c9-bf35-75b9f78b8316 | -6.00461 | -53.55397 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f02cf061-5653-3de0-b242-6c64f909a9fc | -2.45476 | -57.9697 | 2026-10-04 05:16:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16949b10-4d4e-3795-bebc-0e8b3c4f3177 | -1.90436 | -47.01809 | 2026-10-04 05:16:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ed4538f-bcd6-3b24-ab65-8714a7a79cb2 | -3.01031 | -50.47039 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 55ab60dd-0823-3eb3-a5ac-397a2d369497 | -2.48687 | -56.09293 | 2026-10-04 05:16:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3361242-aedf-3093-9308-960258765602 | -2.88804 | -54.13535 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c2931616-9c6a-3893-a77d-8211e601cc18 | -3.84699 | -55.84725 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 88399c1d-9dc3-37f1-a0a8-ca59462ab18c | -2.88331 | -54.14263 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e243e8e-0c43-389f-9490-7c32a3f97a8c | -2.56959 | -54.11273 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0fc604b-39af-3e06-ae18-6e7d26027519 | -2.57262 | -56.15184 | 2026-10-04 05:16:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c41fa432-f8f5-38c5-9759-cb9ae59691dc | -2.58831 | -51.85632 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| fce49274-c04c-3512-a688-d9832b41afc7 | -2.82365 | -54.10687 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 954d430a-0590-3833-941a-ff9ec5eea28a | -2.25217 | -51.93155 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ebb2100-68e8-3bcb-ab34-59bf9236567b | -3.00127 | -57.20001 | 2026-10-04 05:16:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa7a3269-eeb9-3970-92b2-9200651ea6ee | -3.90507 | -55.88514 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 180628c6-9963-3ea0-b45c-692eb86cc3e5 | -4.25699 | -46.37587 | 2026-10-04 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3deb823-9da8-35c5-8bf1-b9cc523315d1 | -3.59986 | -54.23515 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3cf4e7e2-a7cf-3f13-b649-420d4153ec74 | -3.03962 | -54.20634 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66b50532-a771-356a-adb5-45e8416c7096 | -3.06111 | -54.16146 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 720dec6a-270e-3509-b424-f523c8c03078 | -3.12218 | -53.75171 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ed4bb7a7-34f5-38c3-a04e-2892fbaead3d | -4.09552 | -54.32773 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ffa29bd-2cc6-366d-b955-fe001ccc3ac7 | -2.81538 | -54.11364 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 602afbfb-fa5d-3c35-8e79-5acb522fcb13 | -3.50629 | -52.96163 | 2026-10-04 05:16:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0d64379b-e962-3673-a401-d9570ccb285c | -3.12967 | -53.72761 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b15c184c-2bf4-3994-a27e-c27c5d75bdab | -2.99234 | -51.04881 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a8b1a78d-cc35-36ab-96f9-190655fbb1b5 | -2.7486 | -51.54295 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 932aad84-1592-3545-bd5e-0817aee9cd79 | -6.34222 | -51.75833 | 2026-10-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b821cfef-8d80-356d-9e36-214f0a452716 | -3.93701 | -56.05203 | 2026-10-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63955e5a-784f-39fd-8357-12c201bf7556 | -1.27668 | -54.56217 | 2026-10-04 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67b3c1a9-c322-36b3-a656-0d0497e189a3 | -3.13063 | -53.75593 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1061ab6a-6c55-3949-8670-8f959fc8c961 | -2.94744 | -54.12432 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f1aedd50-ffd1-3c6c-8e75-3d91f8b678eb | -3.24153 | -58.75693 | 2026-10-04 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 184d63fb-3452-3d8e-a091-22f145535f7e | -6.23617 | -53.15021 | 2026-10-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 62a3ec9a-cc2b-3c42-8a8b-1c77fb58fbf6 | -4.0579 | -54.31385 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 74eb9c2a-8534-3279-9b7c-3e164180f667 | -3.00527 | -50.47399 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d794f2f8-1188-3259-9489-7a593285a5ab | -3.17557 | -50.53799 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 65f0d5d4-5296-3214-8121-6ef8c4cb7dfa | -2.89386 | -54.14426 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c3a2fdab-475f-38c2-8e79-5f6bfe6e03c7 | -3.18272 | -54.10178 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cb27c8d2-3d05-3d52-80b5-faebfa41d0d2 | -2.59682 | -51.85403 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad6a1f0d-949c-31d5-a1f8-e30fb0fd69e7 | -3.27732 | -54.0063 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd93ab80-e6e0-3445-a39f-865e563da7cc | -4.27421 | -49.97717 | 2026-10-04 05:16:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 860e2299-2d61-3c4b-a3b3-1919d0e6fcc7 | -2.45084 | -57.97276 | 2026-10-04 05:16:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f702f8c-0af9-3395-85d5-89dc843e2146 | -6.08122 | -53.481 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| adfa90d2-0df8-3fc8-bcf1-a29121106dc5 | -3.01584 | -53.89364 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 407ee32e-6684-3ccb-9f15-2b89b2e69daa | -2.79366 | -54.11431 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2676db5f-2974-3dae-9466-34a20d4e2004 | -3.22272 | -54.30891 | 2026-10-04 05:16:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed5c8e82-c9fa-33ae-a6f4-68318d9a32aa | -3.70034 | -50.66543 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| f951f490-16b6-3ddd-b0a0-09d2382a88b7 | -2.97212 | -54.10741 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README57.md)
