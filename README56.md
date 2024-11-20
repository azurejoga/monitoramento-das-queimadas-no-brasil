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
| 9518b550-f264-31fe-a56f-7b4d658b7399 | -1.14502 | -53.51431 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fe0d30b2-f728-31e4-b4b6-d243eb3799c3 | -1.31129 | -47.80328 | 2024-11-20 04:50:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2b0a64da-dff4-30c6-8b61-827d899e9159 | -3.81107 | -52.29141 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7340d1da-ebf5-3f76-a90c-ad201d4a3da2 | -6.94148 | -45.08024 | 2024-11-20 04:50:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dee0b453-9855-3adc-869d-957598d7a1d1 | -0.98308 | -51.7243 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6716728-7e0c-3b10-aec3-94017fd6ddb1 | -0.81177 | -51.60926 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db013dfa-9eaa-36ed-b9be-d7c5f4203345 | -1.86397 | -47.82096 | 2024-11-20 04:50:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f40cce17-7e39-384b-a407-417df702865c | -1.25711 | -51.76738 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 626600e2-9e3a-3b23-bdeb-235600b8f107 | -6.92706 | -41.19469 | 2024-11-20 04:50:00 | NPP-375D | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| ab0e8964-1d28-3918-b7f7-8474351c0a15 | -2.78868 | -48.10269 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04130667-6d42-3437-8a2b-5c9db1937bcc | -3.51296 | -53.79351 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42b4317d-cb02-3d0a-abf0-dab42d9f0931 | -2.69028 | -51.71251 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2bb9affe-52ee-388f-aae4-78eaf39d24a0 | -2.35943 | -49.00516 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37e45cc0-a469-39de-ac6d-ea1e417f8d2e | -1.32737 | -51.87745 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9da7be6-6f30-3fe6-a9cb-edeb1112f749 | -2.28282 | -50.58463 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3812379d-df34-3d66-aff4-e1590eab08e8 | -3.66162 | -54.32393 | 2024-11-20 04:50:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee7f8443-f1ac-305f-ac37-48e0254e561b | -2.68751 | -51.70854 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d1baa7a-897b-3fe9-9625-43f9c03cb916 | -1.6843 | -55.02953 | 2024-11-20 04:50:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0dc4f29-8a32-38ae-9f75-d34de8607047 | -2.92173 | -48.95747 | 2024-11-20 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 846329a7-cd3f-325b-bc53-5322ceafdc15 | -2.21151 | -46.35051 | 2024-11-20 04:50:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44650f3c-c2d6-3a10-9fea-3525a145c3b3 | -0.96646 | -51.72171 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aeb6115e-cbc4-308a-b010-493721abebc8 | -0.94299 | -51.63311 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2dd866c3-a5b8-312e-8008-dee8ee074fd6 | -1.96762 | -46.42767 | 2024-11-20 04:50:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 53685c24-cefd-3dbe-88c2-a47eb377faf5 | -1.45259 | -52.6703 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee015f16-61f7-34c4-817e-0e16cef68fd9 | -2.34143 | -53.61169 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d46c855e-076c-32b6-89b7-beca0d42ae88 | -4.44572 | -46.58928 | 2024-11-20 04:50:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ab3199df-38c6-32b7-97b8-219e67d916d2 | -3.48485 | -50.31766 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f44ccf13-a703-347b-8ae0-eb3e97888b52 | -2.11633 | -48.55109 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ca3cf07-f9d7-3ca3-bb8f-ed55b278b10c | -3.32709 | -43.08151 | 2024-11-20 04:50:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52c4160c-74c4-3617-9fe3-bc6c7224c930 | -1.315 | -51.87566 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb8bbe27-ffd9-3b6c-b845-7532b48ad757 | -3.30395 | -50.36 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6717ba3-7208-39b5-9214-aea8a33550a7 | -1.6022 | -52.41037 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a966ae1-0d10-3341-b49b-ec2ac32c837a | -1.41322 | -51.07866 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d6541e9-2ee1-3d30-9566-95c0fa1292b4 | -2.74329 | -51.82677 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| c57879ec-a2e7-37a4-a6c1-83dbdc995033 | -2.99758 | -51.4602 | 2024-11-20 04:50:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0ce0b94-28b2-3c4d-b565-246f804c3c37 | -2.65212 | -46.14433 | 2024-11-20 04:50:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18289254-ea01-31b7-9224-09b7b7fdde44 | -3.71745 | -52.08903 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7590011-f1b9-34f3-a5f8-15648e009c00 | -2.53941 | -54.30056 | 2024-11-20 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1825a5e-09ba-3c3e-8d59-5101c46ce704 | -3.27335 | -44.48268 | 2024-11-20 04:50:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8476197-a8f6-3df7-a16a-12e687af7328 | -4.30851 | -48.06879 | 2024-11-20 04:50:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c594e84a-ee62-3d0c-b76d-8a9d07ca4a63 | -2.30451 | -48.49339 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 58b3404e-cde1-336e-a8d1-97920704573f | -2.78114 | -53.98095 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 923e6ecd-f05b-3396-b95a-57bf2cf76b11 | -1.09094 | -52.26233 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83f0a399-b6c0-30e2-83c0-96a179531042 | -2.61108 | -48.22046 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 449c8922-7132-3d14-9be3-d95ff930730a | -1.22373 | -51.74446 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6020ecc1-6e7b-3807-bcb2-da361ce1d783 | -2.45606 | -49.14691 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88d49079-341a-36ca-9af6-6edcd064650d | -3.01734 | -51.00925 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bbdacefd-e3e0-3c7e-8b0f-6de84b0161ac | -3.42961 | -53.2891 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70b31517-0673-3b28-9c68-2df82ee631f7 | -1.51392 | -52.08834 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a0326c8-dcbb-3c1d-94b4-cbe6e82b71aa | -1.60834 | -52.41494 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 509b3579-6e89-349e-af05-9df51e50fe37 | -4.14612 | -49.2181 | 2024-11-20 04:50:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c548d1c-ce41-3561-add6-95667bb95de9 | -2.3306 | -51.28907 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 535efb85-a3a0-3a96-8a5f-d842c37cb8b2 | -2.21569 | -46.48668 | 2024-11-20 04:50:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ff6d424e-af77-3799-86fa-75fb1ba9744f | -3.6438 | -52.3611 | 2024-11-20 04:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 367f65de-2cc2-3019-bd06-7c2f0502b099 | -2.77408 | -52.59637 | 2024-11-20 04:50:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 956404fe-0ac0-31a7-847d-fd6e250380a5 | -6.00896 | -38.65683 | 2024-11-20 04:50:00 | NPP-375D | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| b684701b-555c-39d0-ba62-3bc137a58fba | -2.19782 | -53.67788 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ff1fbf67-825a-31cf-9c94-19e44fd91560 | -2.59853 | -48.30122 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66a6774b-ff4a-361d-acfb-f51f8dfd9d60 | -1.64264 | -52.64108 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39235cd9-ed4b-3665-babf-e48515136975 | -2.26398 | -48.41702 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e4649c4-1939-37e7-9898-56059f5fed34 | -1.90045 | -53.32676 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 925f0a64-dcb0-3774-83cf-fbdc1d5ea431 | -5.71527 | -44.80791 | 2024-11-20 04:50:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 06fa230e-36aa-3eed-bdd8-8ae04a8c5b64 | -2.79035 | -48.60072 | 2024-11-20 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8f384c7-26cd-3541-b183-2a47450b19f7 | -2.34478 | -54.77811 | 2024-11-20 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 658f104c-135b-3620-8713-5902dce0b373 | -2.69675 | -46.24301 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f5d4a01-7a84-3354-9c4c-ef5462ebaefd | -2.28763 | -48.40792 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d087ef4-06ff-3d20-b80d-300c006923a6 | -1.24773 | -51.78363 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62cd45d6-121b-3e8c-98b9-720e6acc2987 | -6.82267 | -43.28995 | 2024-11-20 04:50:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2ea52c7b-c5da-3516-b12d-90669ef2848f | -4.03765 | -53.50589 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 730b149b-cbb2-3064-9eea-76870505a5f5 | -3.13205 | -48.58838 | 2024-11-20 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a22413d9-7dea-377d-bdd1-ee184da92127 | -6.47707 | -46.07996 | 2024-11-20 04:50:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d5585f6-e5b8-3529-8792-db77ccba5316 | -1.34344 | -51.39232 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e475c0b6-3f87-3b8e-b96e-7da9a9ff1580 | -2.71091 | -49.86561 | 2024-11-20 04:50:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b4c3183c-15e3-3e7d-b56a-526846d563b5 | -1.24045 | -52.02414 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ab8058f-5338-3b28-9aa6-e2ab90f7060d | -4.38379 | -47.77543 | 2024-11-20 04:50:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 59d9d0d8-7bed-30b1-af69-02c3461f67fb | -2.71091 | -53.17013 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64f9678a-ddc1-391d-b7a4-4a0c65dbdae7 | -3.14117 | -49.1231 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07796ce0-a3e6-3dd9-b535-a016c560ffed | -4.451 | -46.58237 | 2024-11-20 04:50:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d7554f0d-a7ca-3df7-bddd-b7d5f043d450 | -4.13503 | -47.73355 | 2024-11-20 04:50:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 06f8211c-4fb1-3c3c-8caf-947cfa0f903b | -2.13176 | -48.91606 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de1c1957-6603-38db-872d-b8d675e121d3 | -3.10768 | -53.75071 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 91805600-e0ba-326d-8727-962010c48d59 | -0.82913 | -52.83553 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84129946-79f5-339c-b240-0e583f848f0b | -0.92496 | -52.5852 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c19b07d3-1f9a-3261-88f1-0b66108862f5 | -4.24885 | -50.70572 | 2024-11-20 04:50:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6537afd6-a52b-32f8-aaa5-6d079dd11133 | -2.58764 | -51.72137 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8f8667e-1ac5-36a3-9130-27a42433f35e | -4.90014 | -44.00504 | 2024-11-20 04:50:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0cc3604-62e9-3e14-acd4-50a06731bbbc | -2.67015 | -46.16631 | 2024-11-20 04:50:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbdd8451-a9d9-32f9-b4de-31e7a7d5a3c0 | -2.22083 | -49.71628 | 2024-11-20 04:50:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 662f0947-7cb2-3ac4-b773-64f7a2ecd58a | -0.83365 | -52.87342 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24c46920-48db-3ee6-8f57-d38a6f28ed92 | -1.11056 | -51.75534 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48d19a0c-8501-37cd-9c05-108373a0f24d | -9.16998 | -44.72028 | 2024-11-20 04:50:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9eefdfc-a54e-3b0e-9d0e-202c4abeec66 | -1.29301 | -51.73402 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a5f05b7-3d5a-3579-b5e0-284355b5c28d | -1.60433 | -52.24537 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f1ea8f0-ccac-35e0-9fc2-07f136dc297c | -2.84466 | -46.68323 | 2024-11-20 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1d8246b-e627-33ca-98cb-d780d7f03793 | -0.96815 | -51.73261 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6cd5a74-7c4c-3e7a-8a91-a81c0922a409 | -1.96922 | -52.09902 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c56007c5-74ed-3bc9-8ef8-1be4c51ac1e8 | -7.21824 | -45.08436 | 2024-11-20 04:50:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb1fa8f8-2d59-328d-abe6-ff45ad977922 | -3.50718 | -51.01747 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1167bafd-86b0-3ed8-b32f-5b3fc284749b | -1.31274 | -47.80556 | 2024-11-20 04:50:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9688319-bdb8-3378-b41d-0506f676f4f6 | -2.53146 | -54.01007 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README57.md)
