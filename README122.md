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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bfd90190-3ba3-3da5-8736-4ec9384a58c5 | -3.45592 | -50.5857 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e630aee-2b44-355e-a786-3e959967e7aa | -3.55133 | -54.69759 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a046795-3302-3ed6-81c8-13fb118d2b1a | -4.58408 | -54.93287 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3ede26e-78c0-34a6-9d3e-9cd6d14bfad7 | -4.50294 | -54.99623 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e30c4077-ea91-35d8-bc6e-d4ae77c5544a | -3.49948 | -49.93782 | 2026-10-10 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e7efe22-d553-3e1f-9009-215fea67fcc1 | -3.22783 | -54.29652 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b839f3da-4a84-37e3-903c-4e8f1c99c72e | -6.47971 | -53.60633 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7632e03f-6d5a-30ca-96d5-dca3ffc1e8e9 | -7.23928 | -55.15999 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64862331-8bca-30d6-9d12-d3f668f49224 | -5.74828 | -45.12589 | 2026-10-10 05:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 32d3de29-293e-3eda-b7f2-9432517e40ae | -8.40852 | -46.90395 | 2026-10-10 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a27b8e2d-d4e3-318d-acfa-4e42dcd9cb59 | -3.00986 | -51.00954 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bceae744-fae9-3864-b3ad-3ab35a89dd15 | -3.62493 | -54.23515 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a99d84e0-4f9f-304d-818b-29f25c236450 | -6.81199 | -55.30313 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a294c80-9582-3c56-9d9a-525fdf93798b | -1.63856 | -54.3968 | 2026-10-10 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0cc3e41d-5f04-398e-8179-9c87aad2c3ff | -1.90823 | -58.24571 | 2026-10-10 05:04:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 468a9123-d85b-3cfd-af13-8bb509898cb2 | -6.74559 | -55.05925 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4a9fe57-3591-3ebe-bb2e-6f258237a27b | -5.97499 | -55.35338 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 984c20e4-4b22-39d0-b927-782ea9dc89fa | -2.93093 | -54.04794 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c3a96ea-b156-3421-9974-3e368b92e3cd | -3.01559 | -54.2207 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f7ebc0c-6efd-3dd7-ac0c-7cba25f7a6b1 | -6.42217 | -51.95874 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 634eab6c-da5f-3960-bee7-59358af5889d | -7.19667 | -55.14997 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5cd898c9-e1cf-3513-ac14-835c2c9aea17 | -4.22299 | -53.82882 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7e1c98e6-f7b2-3916-bb77-b0b469cfdee8 | -3.58078 | -54.70588 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bee6dd6-656d-3986-b87c-11b180c90742 | -3.19971 | -53.85373 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| cf2c2b80-44de-3924-af99-e4e268d3d1b5 | -3.56466 | -54.69971 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42967cf6-ab0e-3419-8110-e59bb37e1493 | -6.3818 | -56.22857 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee3185c7-df7e-38a2-84b7-71c6c02c638e | -3.27146 | -54.30019 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 195108d0-51d6-3fd9-9d4d-117cae8e1060 | -3.10547 | -53.95515 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efa8d413-1cdb-3079-9110-81ec66eb4163 | -2.42219 | -57.99765 | 2026-10-10 05:04:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 242f7566-9324-3c56-ba1e-93b15aecdda0 | -3.57578 | -54.69429 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| edcf4b4a-2276-385d-a524-df8d8fb2fc03 | -4.59374 | -55.72379 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 6bd4eacf-829c-3292-9fc2-feaefb35ac21 | -2.99646 | -53.91355 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a61e7d0-442b-384a-abf3-f29929b275a5 | -2.99617 | -54.1503 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7e4a2fc-63ad-31ac-af88-fd73f0941a67 | -3.25816 | -54.19171 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99acd190-6c84-310a-9394-e3f6ab6fde63 | -5.30671 | -60.08108 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95a2451a-89f9-392b-baaf-fb893e3bc3cc | -6.31768 | -55.33545 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c369d20d-f8a8-39d0-b63e-5d3a1d6c0bd0 | -3.05984 | -53.91997 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a6181ef-fd25-3da0-b5c1-1639f3d48f03 | -5.38425 | -56.06402 | 2026-10-10 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 201cb46e-e671-3c14-a6ed-bfa32150d347 | -7.56425 | -45.64677 | 2026-10-10 05:04:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd9a2977-d2f4-383f-b75f-01746b43465c | -7.09596 | -55.73661 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9e5c094-8b91-3cd2-84f3-bc00cf94c15d | -2.50481 | -56.16735 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 83ed76f7-8d0e-34cc-a8af-8d0ffa73d935 | -6.62542 | -59.99978 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9325bfe8-48a0-3e7c-91c5-c6d235d2c733 | -8.92567 | -45.42059 | 2026-10-10 05:04:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| feb072ab-2cd3-3dae-9347-96c7cc9a0560 | -3.30491 | -54.00462 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6d3f7be7-8fcf-3daf-8b0c-fcaf47a71ffa | -2.93314 | -54.05536 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8766f435-b1e1-34bc-a96b-a087404dcec5 | -3.34896 | -50.40827 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b91443b-2d60-36cb-b07e-b0899bc31ca1 | -3.58746 | -54.57784 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7b488d6-e51d-3266-8cd0-780d51e5cb67 | -6.91722 | -59.28271 | 2026-10-10 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e877196c-08cc-3200-9103-7a7da3690488 | -3.00113 | -54.14044 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 80b77fa1-1db8-3483-b1f5-0a06a94218fd | -1.79313 | -53.48708 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a8c9017-ca17-3bfd-8f05-d6323f80fa85 | -6.22058 | -60.03649 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd3f0dcc-9428-3a8b-84fe-c0b31e00c223 | -3.43369 | -54.53992 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c21169a-1036-3dbf-abaa-d9271c2708a2 | -6.32428 | -58.30825 | 2026-10-10 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 127ba307-3f8b-3bd9-997d-a7ba7b38ce71 | -1.51294 | -54.52531 | 2026-10-10 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 94312566-b44b-393a-8701-0e07d294b64b | -3.01767 | -54.12179 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b30c2eb-c745-3e8d-be8c-9e70d7e8011c | -2.04594 | -56.38279 | 2026-10-10 05:04:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 13c11508-a0ab-3bc9-910a-d36f13375a13 | -2.50673 | -56.15554 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 99dc33a5-ad9b-3d4b-998a-3d912319b833 | -3.12394 | -54.18079 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a0847c99-7da4-3829-a3dc-2466c826c41f | -1.72761 | -49.98337 | 2026-10-10 05:04:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb5a78ae-a7ed-3fc5-b499-38d13a515d90 | -7.56947 | -45.65147 | 2026-10-10 05:04:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60387c7c-baad-3494-aaf4-af64a29b3610 | -6.4909 | -55.31291 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65230b26-f27a-3176-b943-e720997d6a29 | -2.73415 | -51.54634 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0e299cc-f078-3dfd-952a-f383e63476b2 | -6.84651 | -59.30047 | 2026-10-10 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e01220e0-e320-3c2a-b71d-0aaab4f7dae0 | -4.37871 | -55.1577 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc4a5ebb-a2da-3f3a-a06b-3e7f1365c02f | -6.50517 | -55.39465 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6bd54e04-b512-3fdb-a744-40d9279d3ae2 | -6.25082 | -52.85532 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd5628cc-66aa-3b29-8ccf-3d69b0dafd5c | -3.63633 | -59.56695 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71841bac-98c1-3fa7-9074-db513720e40b | -3.86726 | -55.98773 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c2376aef-b61c-3003-9288-3bf7366fa7e5 | -7.50669 | -54.9964 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88d9a7bc-1ad2-38f2-b6d6-b81c7d51c7d0 | -2.57669 | -48.25218 | 2026-10-10 05:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 41239793-c965-3331-b0d8-b53e44c1f11f | -3.00898 | -54.24096 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e990bed-ac33-3683-ae43-c71079ad0b86 | -1.62572 | -54.43444 | 2026-10-10 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11eedfe1-b325-36c6-a106-d4e73d42b60c | -2.5865 | -56.17636 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c79af86-6350-3fb1-a523-f6216de5d982 | -2.61401 | -51.70968 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b714588-ec2c-3696-b38c-2f1fe5e767ec | -3.64239 | -55.48857 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdb50fa1-9c5e-317f-977c-c0f442f0452b | -1.75543 | -55.24889 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c04b084-7ab9-33b2-a7b9-f2eb68ba1bb5 | -3.0576 | -58.79679 | 2026-10-10 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50654450-ce6e-32b9-a840-327a6ad55437 | -2.92324 | -54.07502 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3678a77a-9f65-3317-8a16-7286a94eb8dd | -3.96048 | -55.34501 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 989372df-7e72-3a5d-9ca6-e09de889af1a | -3.08811 | -56.79407 | 2026-10-10 05:04:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7d8e02da-7a4d-301c-97a0-c926edf2e249 | -3.50626 | -49.94347 | 2026-10-10 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5c31334-0640-3d46-8d02-38f61e66c6dd | -4.59282 | -50.97353 | 2026-10-10 05:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1624e60b-09be-3d49-a98c-34461f1e77af | -6.497 | -55.31749 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 254210e6-441a-3b5a-9f44-e39098d69583 | -3.01658 | -54.1287 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9aa85584-1492-3321-8fb9-a4565b49d5eb | -3.50808 | -54.62617 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 14eff2c0-d77d-30a2-8a01-5f5f48b80102 | -3.93095 | -55.76736 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c830df97-c47b-3b78-9a5b-ee026e123a6f | -6.46096 | -55.47816 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 172a3b32-5186-302f-9f0c-cd60898b5d67 | -3.70231 | -54.19817 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69634da1-4eb9-3ff1-a667-81be09f23531 | -4.10952 | -54.62852 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ee6989e-2d68-327c-a31b-131dab790e6a | -3.87315 | -55.84226 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3dcbcdb-4328-36c2-89b2-93e3e803b34d | -2.97399 | -54.03359 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 61dd14f2-dd05-3a59-8cfc-893cb8eef3ca | -3.57355 | -54.70831 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed3424db-53a0-3992-88b1-10e6709a91d3 | -7.23541 | -55.16294 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e94bd382-1805-3ce5-bd77-4e0809c71430 | -3.57775 | -59.08319 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 471b669d-0f43-3a28-af93-04a49e81d7ce | -4.51863 | -54.85492 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a5d0e8f-0335-325f-b5ae-92a4781c9fb3 | -6.06553 | -44.67271 | 2026-10-10 05:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1d720d47-15f6-33cf-a19e-516160af5821 | -2.83907 | -49.87977 | 2026-10-10 05:04:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b1b11d7-7e21-31e2-abdb-6ee5170e5d9b | -2.7287 | -57.47669 | 2026-10-10 05:04:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f96ea92-580b-3607-93c1-1f2af56fd0c1 | -3.31486 | -54.02736 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e338be1-291b-32af-8a69-fd3491ccfda7 | -7.08769 | -52.67911 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README123.md)
