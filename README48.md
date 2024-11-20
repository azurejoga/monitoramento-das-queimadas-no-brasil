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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dbef8c91-eaa7-37d2-99aa-04f9c717a84d | -3.21903 | -53.84141 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 748b4335-fab5-3ea1-bff8-19916a01069c | -6.93325 | -41.19572 | 2024-11-20 04:50:00 | NPP-375D | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 019c393c-5015-3d70-99fd-d58cb0e9fc93 | -3.27731 | -53.83122 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5c4dcf38-8843-3ba3-be80-d3b1c87b67f0 | -2.93653 | -48.33498 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 55299ba2-4154-311c-b100-8b74558a59f1 | -2.54509 | -53.9922 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4377fadf-20a0-3f9a-840e-8c0ae61ba784 | -2.22083 | -46.48019 | 2024-11-20 04:50:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64f307ef-be74-3037-960e-253544d7a8a7 | -1.59922 | -47.14007 | 2024-11-20 04:50:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| b117c3df-5676-3b62-a8ed-6649a51fbe8b | -2.20734 | -50.71627 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86278fb7-a5ce-39e5-8245-584a1919cbcc | -1.13625 | -53.6614 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dafd0ac6-ae53-3f94-af84-63634e61037b | -5.60009 | -46.17164 | 2024-11-20 04:50:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d8423787-7000-3020-bd6c-68c994717aa2 | -1.59411 | -50.44186 | 2024-11-20 04:50:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d038a8f0-767f-3131-a8cd-a9f2f881fd7a | -3.51922 | -53.79842 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 926dddf1-41bc-36b1-bc13-c09b6665409d | -3.66324 | -54.65244 | 2024-11-20 04:50:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2526ff9c-7476-3967-9561-32b81cb269d3 | -2.56942 | -54.08774 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ca6444d9-4ed9-370f-9345-1b5d5f4ef1d4 | -0.91563 | -51.78473 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 092d8c31-75c7-3e91-ae6b-14f9fde3c288 | -3.81 | -47.7971 | 2024-11-20 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 93842128-9068-3bf3-b6b7-91e796760740 | -3.09791 | -51.31721 | 2024-11-20 04:50:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b1b46e6-06ad-3235-9417-1feceae19d5b | -1.25656 | -51.77084 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50c00a3b-2b03-3965-a311-75b8a60d05ed | -2.94723 | -48.07141 | 2024-11-20 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99a201fc-d9ec-3536-bb4d-4aff556334cb | -2.32037 | -46.85181 | 2024-11-20 04:50:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8735b5a9-e180-330b-a7b5-337a9af15784 | -2.91949 | -53.06619 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 39711a11-5c0f-3215-a482-a0571419175c | -2.74965 | -48.57762 | 2024-11-20 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37ae72d7-c8cd-3e2e-a009-c4f0140c398c | -2.88502 | -41.75943 | 2024-11-20 04:50:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5fec5355-e0d2-356b-a3b4-d1ad7a6d8177 | -3.10285 | -53.10167 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b511ea3f-dba5-3ec6-93b3-72768ae889c9 | -4.44267 | -46.58117 | 2024-11-20 04:50:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 23.0 |
| a96db7cd-b05e-33fd-8e54-1bd1e6d939c1 | -4.14989 | -43.97193 | 2024-11-20 04:50:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3f8dce95-4723-38e6-b1f1-21263038b41f | -2.6926 | -46.24239 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59cac510-9582-31e0-84e6-f3b7b3b444d6 | -6.59636 | -46.49467 | 2024-11-20 04:50:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ffe929fc-fbbf-3fd3-ab97-645ba96824b6 | -2.53749 | -54.55619 | 2024-11-20 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 458b5964-a5c5-3082-8d0a-8301db5cd44a | -5.4198 | -44.70011 | 2024-11-20 04:50:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7afe346c-5229-3aed-a0f9-a686c3c2808d | -1.25219 | -53.36434 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9483cf6b-44c6-38de-a7e0-4c9cbcee1140 | -1.32034 | -52.39872 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d6fb3595-48a5-3f30-a37e-08173a4d1d8f | -1.51671 | -52.09234 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bad6d8e8-bde5-3e6d-8916-a45c18aafa1e | -3.0904 | -54.66672 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdca30a5-c840-3405-ad4c-2750d2af8531 | -3.84524 | -50.695 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c62423a7-0b5c-3107-8dfe-2d51b5f9078c | -2.61552 | -51.80341 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c8d7401e-2496-3d2d-a7e5-afca5328cc50 | -6.98466 | -47.08281 | 2024-11-20 04:50:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 329b279c-9f66-313e-acf2-cf35ea008c0b | -1.62696 | -52.62439 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e958bb43-661b-3514-8a0a-81ccb52338be | -3.04673 | -54.40067 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 016074f3-0e02-30da-b176-56a49bdacf5d | -3.54026 | -54.08814 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a8a374d9-ce3c-35ea-becb-54f16a4e6438 | -3.75426 | -51.3413 | 2024-11-20 04:50:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58755f4a-3f60-3fb9-8e3e-d323babb7c92 | -2.21287 | -50.70282 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60ae626d-6574-3018-99f1-1b5947904f6e | -1.70207 | -52.14622 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8deb8167-ea5b-352b-8170-5b0bcdc2daa4 | -2.71838 | -49.34215 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 380c0c15-27f0-369a-8e6f-e2eab7856bce | -3.45895 | -53.30124 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97201556-163d-3398-a521-857fe283c961 | -2.31494 | -46.8482 | 2024-11-20 04:50:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 988a3a0f-084e-3380-8755-f4f105e5f091 | -3.10025 | -54.29139 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09afe9c8-6e11-332a-9cf3-2ff55a63ea36 | -2.02934 | -49.71404 | 2024-11-20 04:50:00 | NPP-375D | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0febdb4e-305e-39cc-a54e-8ace363df1d0 | -3.08323 | -54.66558 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d393234e-4dcc-37c6-8273-31957bc74d4f | -2.56074 | -54.07436 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6de6a9f8-1f47-39d5-b3eb-d8a599464746 | -2.58322 | -51.92207 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 098a4156-20a2-33c8-884a-f6fb84552f66 | -1.4993 | -51.0672 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72810783-5c10-314f-906d-c2abdbcc1214 | -2.18596 | -46.99257 | 2024-11-20 04:50:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74788b14-0665-3277-a21c-43b417c9a9ac | -1.93679 | -52.98794 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c996a4e-6690-32dd-aac1-9c31288ae943 | -2.24503 | -48.44367 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04d387e8-6930-36be-a720-4f2e59262aa0 | -1.66013 | -52.53117 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17627197-d609-3034-9c50-bdac11d5ea2d | -2.06123 | -53.43453 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d3f1e8e4-cdac-3ff5-b077-1bcb8f2e3e02 | -1.39389 | -55.17644 | 2024-11-20 04:50:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b44b69c-7ced-38e8-ad30-f142de590dda | -1.05524 | -52.33605 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adaa8860-4e65-3282-b68a-2bcf19878dc6 | -1.9027 | -53.3347 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8119c7b9-e591-36d6-818b-bc8fdab09d77 | -2.72712 | -47.97424 | 2024-11-20 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb2e749c-2b77-34de-a17b-c6cfebf5e939 | -1.98981 | -53.13709 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a3233bc-aa1a-3a25-a37f-06bd24b04eda | -3.30283 | -50.36719 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b089a493-977d-3266-b62e-443100e9d2a5 | -3.55838 | -51.12193 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ce830de-c2af-310d-8aae-50f9d0f13052 | -1.6764 | -52.0923 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e012ff75-92bb-31b8-acbd-661840fa8eab | -2.7668 | -53.21632 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee56a810-1709-32fe-a575-b4b695a668d8 | -1.68712 | -50.2 | 2024-11-20 04:50:00 | NPP-375D | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 17b7e0a5-ea43-331a-bbc1-bda36ccc50c2 | -4.28181 | -50.58255 | 2024-11-20 04:50:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 605cb408-a783-3058-af74-4e36261e5288 | -2.46864 | -54.7487 | 2024-11-20 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d6b91c95-7554-3099-9e26-75cece7e14cc | -3.8093 | -47.80175 | 2024-11-20 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d4f5544b-b9ac-3ce7-b5c6-dd70cc78479b | -1.21654 | -51.74688 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad53524c-8d6f-36d7-ba72-89089ac85a0f | -2.45968 | -53.69421 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 968bb0e8-094c-3b3b-a901-5dfe5ffb7016 | -1.41858 | -52.81923 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2947533c-953d-3b6d-8222-a4933911aa6f | -2.89697 | -52.44039 | 2024-11-20 04:50:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 08698fc2-6509-3045-971d-3612fd323ccf | -1.5124 | -52.22751 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b121fd75-ab55-381c-a4e5-371ad45a96f6 | -2.67713 | -46.23251 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| afba3496-867c-3f11-bb66-3bc3007956b0 | -2.74229 | -51.72767 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 940330ae-bf6a-360a-9820-c43c5cd237f5 | -3.78434 | -44.06597 | 2024-11-20 04:50:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 48afd617-e034-3b77-8f7f-f926b7899c2b | -0.94264 | -51.72155 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aba41fd2-05e9-3968-97b7-d5cb40fb4707 | -2.85055 | -53.97934 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| de08fe74-209b-3dec-819d-378a03cb92d5 | -4.14551 | -49.22211 | 2024-11-20 04:50:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca0791ce-cc7b-3d74-be2d-ce434dfaa0a1 | -1.33011 | -51.86013 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| abe36b71-453c-31cd-ac81-18697e33ff94 | -2.1992 | -48.45346 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99ac660d-b5ac-3396-ae52-7b853f6806f8 | -1.99776 | -46.6077 | 2024-11-20 04:50:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a3e6746d-b1e4-3da1-8ecb-8c5e377d41d8 | -1.21334 | -51.7889 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ace1372-c522-3a9b-9b6f-79ec1b3a0ef7 | -2.74705 | -54.01508 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5773d552-f67f-3830-8260-aaa824ecb1c6 | -1.19669 | -53.67009 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 9eca1a2b-8153-3562-a2ec-1791e671b563 | -1.41164 | -53.47756 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac80e108-7c40-357f-9a85-b064d1dc3e62 | -2.88934 | -45.83368 | 2024-11-20 04:50:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e39f887f-bf29-3c72-82c2-46273bc9871a | -2.72476 | -49.34705 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 65a298dd-0777-3e5c-9c38-3ada53560175 | -1.79793 | -54.04053 | 2024-11-20 04:50:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7bdd9197-53dd-3071-9490-67fafc97d965 | -2.78337 | -51.72353 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5fb43f3c-e5d5-3666-80e6-d61f814dd83d | -1.60499 | -52.41441 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a827838a-85d8-3bc2-bde7-bd8fe2ac517f | -1.23414 | -52.53025 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 66c11792-ecca-369b-a3ac-8491151095b5 | -2.21974 | -46.4873 | 2024-11-20 04:50:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f3572dd8-d57e-3c23-b857-d6a2fc8ff2f3 | -1.4122 | -51.10674 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4251559a-dbe5-373d-92f5-4e2640a0a77c | -1.23001 | -51.78796 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cd41ea0f-77d7-310d-8638-e20749c3a860 | -2.30388 | -48.49749 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9ff1c628-a7cb-3c19-bf24-412d4a36b9b4 | -1.59121 | -55.84641 | 2024-11-20 04:50:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 28e82e4b-a294-3197-9079-9da360bd6be3 | -2.59513 | -54.01586 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |


[Clique aqui para ver as próximas entradas](README49.md)
