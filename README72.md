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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2f608f1-3b8a-3ba6-9b5c-910789d51b20 | -13.3009 | -45.2209 | 2025-08-15 10:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 181.9 |
| 4e247200-50ee-35ab-abb7-a5261eaf8ed5 | -13.3203 | -45.2177 | 2025-08-15 10:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 777.2 |
| 2f94b2b4-9879-30ea-b7ee-55ecd3f358ef | -13.3004 | -45.2442 | 2025-08-15 11:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 173.3 |
| fc9457b1-707c-341b-ada1-1eced2ad94bf | -13.3198 | -45.2409 | 2025-08-15 11:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 776.1 |
| 0a34c690-6ea6-3f6d-9a77-bab6ad59dce0 | -13.3203 | -45.2177 | 2025-08-15 11:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 676.0 |
| 9f0c388a-85bf-30d9-8971-8d1e406cbbe9 | -13.3392 | -45.2377 | 2025-08-15 11:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 80d490fe-ef78-301f-9440-3c652a78918b | -13.3009 | -45.2209 | 2025-08-15 11:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 254.1 |
| 936a8bf8-92b0-324a-838b-4890e94904b6 | -13.3203 | -45.2177 | 2025-08-15 11:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 648.7 |
| 3199f39b-1cf3-31fa-ae62-ba1abef1a0e5 | -13.3004 | -45.2442 | 2025-08-15 11:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 201.1 |
| 9d054e0d-b21d-3953-8800-78ebcb40058d | -13.3397 | -45.2145 | 2025-08-15 11:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 158.7 |
| b7ed4282-867d-318a-afc8-c9bbe0af5f04 | -13.3198 | -45.2409 | 2025-08-15 11:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 722.7 |
| d8d53b16-9885-359a-a762-8ed09cf389d2 | -13.3392 | -45.2377 | 2025-08-15 11:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 196.6 |
| 3d69cdd0-2fa2-3cbf-9db1-57ba35e144bd | -13.3009 | -45.2209 | 2025-08-15 11:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 286.1 |
| 9929aae6-cdb8-393c-afdd-d728ca400ed5 | -13.3009 | -45.2209 | 2025-08-15 11:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 192.7 |
| ba89d892-d8b2-37e1-b51a-d0942d1e4665 | -6.8673 | -42.7961 | 2025-08-15 11:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 130.6 |
| 1724fd0d-f4f6-3b25-bb72-7a08a0367a2d | -13.3203 | -45.2177 | 2025-08-15 11:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 793.2 |
| 632bfecd-3aea-3785-8d7c-122cbdd1e56f | -13.3198 | -45.2409 | 2025-08-15 11:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 663.7 |
| a717228b-341d-3448-91f9-b5e0f6af967b | -13.8937 | -45.561 | 2025-08-15 11:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 4a614eec-eec8-3ce7-9b86-0ba6c2b28b90 | -13.3397 | -45.2145 | 2025-08-15 11:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 1cab1369-54fe-3719-af5b-b53c1640ba5c | -13.3004 | -45.2442 | 2025-08-15 11:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 8cb0b0b7-40c6-3390-af67-a7c64956aaed | -13.3397 | -45.2145 | 2025-08-15 11:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 130.2 |
| ccb756c5-b828-30d4-b837-2527d341c038 | -13.3004 | -45.2442 | 2025-08-15 11:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 1504f643-6983-333a-9c6f-cc281617dad8 | -13.3203 | -45.2177 | 2025-08-15 11:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 665.5 |
| 0f41de63-45c0-3b9a-b88b-51c30c7e2c92 | -13.3009 | -45.2209 | 2025-08-15 11:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 209.4 |
| 2d6bb8e7-412c-3891-9582-4faaccd57977 | -7.3894 | -44.8817 | 2025-08-15 11:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 813d7fcb-8982-31e8-a72b-eb10a8ad6a57 | -13.3198 | -45.2409 | 2025-08-15 11:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 626.5 |
| c98c7540-be22-3b17-bac3-bef1746bffa6 | -6.8673 | -42.7961 | 2025-08-15 11:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 173.8 |
| c01e6a0d-cb25-398b-920a-b14068608101 | -13.3392 | -45.2377 | 2025-08-15 11:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 9f73770e-355e-33ee-9a57-a7b6fcd5fd68 | -15.4106 | -55.7769 | 2025-08-15 11:30:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 976d102e-ac18-397e-bfa4-76b88d117e94 | -15.3912 | -55.7791 | 2025-08-15 11:30:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 5db7a6cd-b944-3321-8b0a-ebc4ae4ca060 | -13.8937 | -45.561 | 2025-08-15 11:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 5b6ae6b1-1cbf-355c-ae72-ad848594d86a | -7.4085 | -44.8571 | 2025-08-15 11:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 57840ab5-033e-3c8b-8001-09b587ec5136 | -7.3896 | -44.8589 | 2025-08-15 11:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 157.9 |
| c63d3cdb-8f3a-3ceb-82f3-8056ccadcc8f | -7.3894 | -44.8817 | 2025-08-15 11:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 138.1 |
| b4bae887-57e9-3959-befa-b391c9bf3746 | -13.3004 | -45.2442 | 2025-08-15 11:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 7708f1c7-b2e3-371c-b9ba-bd94706491ae | -13.3203 | -45.2177 | 2025-08-15 11:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 651.3 |
| 8bb88cab-db8e-36bf-9924-9c7c3bf1d647 | -6.8673 | -42.7961 | 2025-08-15 11:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 312.7 |
| 7f70a70d-851a-30fd-9cf9-e99f50e44068 | -13.3392 | -45.2377 | 2025-08-15 11:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 214.3 |
| 8623f1fe-578d-3ecc-a6a9-20880890f3cc | -7.4085 | -44.8571 | 2025-08-15 11:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 08695e61-1f87-305b-baad-f30f816e791d | -13.3198 | -45.2409 | 2025-08-15 11:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 554.6 |
| 8848857f-729b-3a3e-8a60-fed07eba6a0d | -15.3912 | -55.7791 | 2025-08-15 11:40:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 82d672f6-52c4-3fc0-b995-f32fe11dd72b | -13.3009 | -45.2209 | 2025-08-15 11:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 129.7 |
| e59bc18f-1474-331a-9977-216d701e8202 | -13.3397 | -45.2145 | 2025-08-15 11:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 191.7 |
| e34c13ca-9328-3c32-bd4e-c96dcd3c6c42 | -6.8673 | -42.7961 | 2025-08-15 11:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 366.5 |
| bc855c9d-eb66-35fc-a094-c510e6417513 | -7.3896 | -44.8589 | 2025-08-15 11:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 161.8 |
| ac1cfd15-33ef-31c4-b03b-4394a35b6c27 | -13.3198 | -45.2409 | 2025-08-15 11:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 465.9 |
| 932b1820-2944-3e0f-bf1c-3a377c99b8f0 | -7.3894 | -44.8817 | 2025-08-15 11:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 39dc9960-700c-3750-ba27-8174818f6df1 | -13.3397 | -45.2145 | 2025-08-15 11:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 167.2 |
| bb23c440-03f9-3996-89ce-3dab678f2749 | -13.3004 | -45.2442 | 2025-08-15 11:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 2af4e218-2555-38cd-a910-bdbf5759bf01 | -13.3392 | -45.2377 | 2025-08-15 11:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 179.8 |
| 144276ab-e8a9-3cd8-9757-b31e486cf971 | -5.2647 | -43.582 | 2025-08-15 11:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| e7ddb128-0873-37a5-b3cf-736f1cf63937 | -7.4085 | -44.8571 | 2025-08-15 11:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 298.7 |
| 7dbc190d-92d9-32a8-a13d-59d16659a108 | -13.3203 | -45.2177 | 2025-08-15 11:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 493.0 |
| eebba5b2-e6c8-33fc-9e02-820ba745f963 | -13.3009 | -45.2209 | 2025-08-15 11:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 130.9 |
| ce068bcc-c9a4-3518-91e8-2ba546b58936 | -7.4085 | -44.8571 | 2025-08-15 12:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 177.2 |
| 85daef33-0e41-32f3-b41b-5c554be3d89b | -7.3896 | -44.8589 | 2025-08-15 12:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 155.2 |
| b9bcffeb-7c51-323e-b3bb-d11a71c95b2c | -13.3004 | -45.2442 | 2025-08-15 12:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 20509889-4c58-31da-8957-506a1a0177f3 | -13.3203 | -45.2177 | 2025-08-15 12:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 405.5 |
| 653e70ab-da11-3b36-a841-17278cea8c3b | -13.3392 | -45.2377 | 2025-08-15 12:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 225.4 |
| 587bd9cb-fb1b-336d-8705-02cf0010fc78 | -7.3894 | -44.8817 | 2025-08-15 12:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 4c3234ce-3f56-30fe-9015-d48693ecb428 | -13.3397 | -45.2145 | 2025-08-15 12:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 145.2 |
| 75c1def9-4345-3329-a468-1bbffe4c55da | -5.2647 | -43.582 | 2025-08-15 12:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| eaae60d6-fc47-36ba-a557-05b671cf6e0c | -6.8673 | -42.7961 | 2025-08-15 12:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 313.3 |
| 2ec615b3-1eeb-3255-b58c-1a14d0451e28 | -13.3009 | -45.2209 | 2025-08-15 12:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| fef0d5d5-7e7f-3e76-b111-a8a723ce6cb2 | -13.3198 | -45.2409 | 2025-08-15 12:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 471.6 |
| 8e5eba87-afdb-3947-9d22-beb0e12b1f5e | -13.3397 | -45.2145 | 2025-08-15 12:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 184.5 |
| f4d5249e-b580-3819-b391-5322ad758cb8 | -13.8937 | -45.561 | 2025-08-15 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 35df68fa-e9b1-3c1f-9d13-bf348bb439c2 | -6.8673 | -42.7961 | 2025-08-15 12:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 338.2 |
| 448da2e7-83bf-3687-bab0-d3bdd79d235b | -13.3198 | -45.2409 | 2025-08-15 12:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 331.8 |
| ba0ed527-0619-33ec-8111-6ff6404d2694 | -7.4085 | -44.8571 | 2025-08-15 12:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 54ede912-c9be-3eba-9753-d2cc03e34367 | -13.3203 | -45.2177 | 2025-08-15 12:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 407.7 |
| 52c9e9e8-45dd-307c-8559-b9374dfa9e7f | -13.3392 | -45.2377 | 2025-08-15 12:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 177.6 |
| 007d748a-c7d0-302e-a5b8-aee1d6b366ed | -12.5942 | -46.9527 | 2025-08-15 12:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 340181de-2262-312f-a886-0a568f601f15 | -13.3009 | -45.2209 | 2025-08-15 12:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 0b0e3db7-bc87-3576-87cd-477410d6d561 | -5.2647 | -43.582 | 2025-08-15 12:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 4400422b-d8cc-317a-b700-7672ad18176e | -3.46857 | -44.30251 | 2025-08-15 12:12:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 57de99fa-2555-3630-8389-f26e7ccb17ba | -3.40002 | -43.36853 | 2025-08-15 12:12:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 09ad24cb-1138-3616-b8ec-c6327cb67121 | -4.59608 | -43.32601 | 2025-08-15 12:12:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ca09ed7b-f34c-351b-849b-8f8e1ccb43f9 | -4.69097 | -43.24176 | 2025-08-15 12:12:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 948ebffb-5c61-3fe1-8a01-7a12b53e2a61 | -4.59738 | -43.3168 | 2025-08-15 12:12:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 863fcec3-e381-3deb-bd5f-76d956577fab | -4.10169 | -42.45884 | 2025-08-15 12:12:00 | TERRA_M-T | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| e216fc81-d0be-3911-bf95-928c30202768 | -3.95518 | -41.47299 | 2025-08-15 12:12:00 | TERRA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 20b4d893-e33c-3dbe-bcba-34de13e9b1d2 | -4.92336 | -43.22918 | 2025-08-15 12:12:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ff2084cd-307f-35f3-b139-66800ff36eef | -4.92203 | -43.23851 | 2025-08-15 12:12:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f7655a9f-ae73-383f-99e6-a31f3120cf07 | -4.05615 | -42.51274 | 2025-08-15 12:12:00 | TERRA_M-T | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| e1ac6df4-41e2-378f-958a-6d8e0ba43dc9 | -6.32836 | -42.80556 | 2025-08-15 12:14:00 | TERRA_M-T | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 22.8 |
| 385173c0-220c-309d-a9b1-a645511e042d | -9.84254 | -47.80053 | 2025-08-15 12:14:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 488e43d4-7f8f-3734-acd9-451614be1a5b | -13.33446 | -45.22425 | 2025-08-15 12:14:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 3829adb4-5ce0-362a-93e2-d2a95bf127d1 | -6.86084 | -42.81247 | 2025-08-15 12:14:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 330.7 |
| 1c54fcf2-fb25-3422-9938-e40d97327709 | -13.61759 | -46.92432 | 2025-08-15 12:14:00 | TERRA_M-T | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2c532b17-0400-3ca7-bad2-c07d2fb4c3a8 | -6.95996 | -43.82267 | 2025-08-15 12:14:00 | TERRA_M-T | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f04bd8db-34b6-3f2e-b8a3-7fd87b5e658e | -6.86365 | -42.79201 | 2025-08-15 12:14:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 26.9 |
| 2971c22b-546c-3a18-bc80-d046d6a434a9 | -9.11112 | -44.71523 | 2025-08-15 12:14:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6d78249e-e1ed-33f3-b14a-2c90be5abaf0 | -10.36909 | -48.30199 | 2025-08-15 12:14:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| bad0551b-a194-3462-ba95-3821e75d1239 | -13.11366 | -46.84558 | 2025-08-15 12:14:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8d7fe43c-827f-3995-8ebc-0fc42d2c32b4 | -15.2193 | -43.7939 | 2025-08-15 12:14:00 | TERRA_M-T | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 6cb757d0-bc80-3c32-aea8-13fd09a8f2f7 | -11.91903 | -43.43611 | 2025-08-15 12:14:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| d514304b-3bcf-3004-a24f-9522084f7599 | -12.04909 | -43.37082 | 2025-08-15 12:14:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 1cd63832-e2b7-343f-98da-cfa9ac992d20 | -7.23864 | -44.78497 | 2025-08-15 12:14:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 17e9a8bd-ed20-33db-af8c-cdb45d4e9d32 | -14.05905 | -46.2947 | 2025-08-15 12:14:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |


[Clique aqui para ver as próximas entradas](README73.md)
