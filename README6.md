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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 839d7904-6d09-3f5a-820e-64d69b0d7860 | -5.82348 | -44.11345 | 2024-11-28 00:11:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| aa90f329-a748-33b0-af71-811c184afa86 | -1.4425 | -47.12261 | 2024-11-28 00:11:00 | TERRA_M-M | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| b1af9129-3636-3db4-bc6e-74f20afa05a3 | -3.46051 | -43.5361 | 2024-11-28 00:11:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| edaa0e5e-667d-36de-bd45-edcb2490aacc | -4.66378 | -42.40517 | 2024-11-28 00:11:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 27.4 |
| 1c83f7c2-e0e6-3035-b40c-9023c1656bb6 | -5.31618 | -43.08332 | 2024-11-28 00:11:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 20704195-f22c-3cc4-9763-dc2383fce3c9 | -2.47864 | -47.03223 | 2024-11-28 00:11:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| a35ee17a-b757-3cf5-8d84-a546074e2077 | -3.33246 | -44.04432 | 2024-11-28 00:11:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| ca8ed7a9-8e54-31b0-89d9-c5a7acda78dc | -2.29336 | -47.10596 | 2024-11-28 00:11:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| b8f2a306-2e11-323f-ae03-8e2614d6c128 | -5.82376 | -44.11885 | 2024-11-28 00:11:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| c25b331d-c7cc-3f58-b492-0551702297ed | -5.98466 | -45.38916 | 2024-11-28 00:11:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 9d3190ce-188e-3a89-8f0d-32c3768b1570 | -6.17846 | -42.60287 | 2024-11-28 00:11:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 17.5 |
| a1f3ff56-9482-34b9-8c2d-91ae6d87c223 | -2.71168 | -45.94443 | 2024-11-28 00:11:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 14.7 |
| a702b290-ae03-3ae0-8a82-84d2f54dab3a | -2.15619 | -48.71113 | 2024-11-28 00:11:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 23d89693-d2f5-3a73-a771-d099adcc898b | -4.67518 | -44.61498 | 2024-11-28 00:11:00 | TERRA_M-M | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 29adcacb-9059-3bf1-a3cf-c32c53c6cc49 | -6.09461 | -48.04614 | 2024-11-28 00:11:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 343.4 |
| 018d035b-6b78-31a9-b18d-cef0ef631495 | -3.66431 | -45.77654 | 2024-11-28 00:11:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 131.6 |
| 7c61ff4a-9010-37ad-87b1-674b2c66b7f4 | -3.66489 | -44.48659 | 2024-11-28 00:11:00 | TERRA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 67f97e03-b6f9-3396-a3ae-8011ee89f4c5 | -4.76966 | -44.4463 | 2024-11-28 00:11:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 7c830f8b-fba4-32ae-8654-ace557ed1592 | -6.1062 | -43.97832 | 2024-11-28 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 117.6 |
| bbb11d2a-506b-35ae-bf0d-e6e143d5c049 | -3.68166 | -45.79915 | 2024-11-28 00:11:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 9180bb86-b205-3eae-8d34-bd4dd34d0a44 | -4.55493 | -38.2516 | 2024-11-28 00:11:00 | TERRA_M-M | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 85507259-158a-3388-9199-5d9593909e23 | -3.62946 | -42.41212 | 2024-11-28 00:11:00 | TERRA_M-M | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 589d3cba-9d44-356c-b3d8-67a35ad37dd4 | -3.32665 | -45.50159 | 2024-11-28 00:11:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 5a624bf8-6a72-3e60-b37e-2566feab49b1 | -6.15947 | -42.62679 | 2024-11-28 00:11:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 40.2 |
| f23e9833-359d-33e0-a3b1-1b1a306db8e5 | -2.87625 | -46.83156 | 2024-11-28 00:11:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 54f6db5f-b635-3f99-ab2d-e4f5c134b8e9 | -5.31234 | -43.07822 | 2024-11-28 00:11:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 211af3b0-a428-3abd-b819-6a5d8c9a57dd | -5.22299 | -44.91703 | 2024-11-28 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| d38ba8a8-f7f6-32a5-97c6-086517925e34 | -2.85197 | -46.86955 | 2024-11-28 00:11:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| b54bb636-5f75-376f-9ddf-4bcb581c2a91 | -6.11737 | -46.58699 | 2024-11-28 00:11:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| ab4f4c2d-3afd-326c-88f1-02e808142b51 | -5.00257 | -38.01635 | 2024-11-28 00:11:00 | TERRA_M-M | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 26c99b9f-894b-32c4-b56e-1b493be954ad | -2.88003 | -46.86052 | 2024-11-28 00:11:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 263.6 |
| c3556a83-b598-3532-af89-5f42db381230 | -2.15824 | -48.70416 | 2024-11-28 00:11:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 1752b445-469d-384b-9940-4b0c0ae8d07b | -6.12252 | -46.59163 | 2024-11-28 00:11:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| eb4455e0-152e-3011-b288-fcee3e55d61e | -2.86317 | -46.83842 | 2024-11-28 00:11:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 214.0 |
| a69a56fe-5d96-31d5-93d8-f6ac02c9f9b9 | -4.00275 | -44.28707 | 2024-11-28 00:11:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| d51bdd68-02f7-3968-bd3d-c5bb5922e10e | -6.15742 | -42.61163 | 2024-11-28 00:11:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 6d0d6b68-df7b-3399-a533-c203cb33c4d5 | -3.97036 | -46.97666 | 2024-11-28 00:11:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 48fb2215-29b7-3479-80f8-71ee05c81d55 | -2.72557 | -48.88705 | 2024-11-28 00:11:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 183678f2-f2f5-31cd-bdb9-9989dd9f5e87 | -3.3286 | -44.05135 | 2024-11-28 00:11:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 203e4b48-8a0e-370d-80da-22a05a9eeee0 | -3.9562 | -48.06948 | 2024-11-28 00:11:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| db5091e5-c558-3c6d-83a5-a11301a55d09 | -6.36888 | -45.68443 | 2024-11-28 00:11:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 291826c1-aeb3-3f9d-be40-650c99a86598 | -3.96004 | -48.06392 | 2024-11-28 00:11:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| e436cd7f-1e36-3d3e-9b60-dfb69bbad110 | -4.66019 | -42.3776 | 2024-11-28 00:11:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 40.7 |
| 4e268a55-f3f3-335b-ac12-8481b528ff2a | -6.19206 | -44.43616 | 2024-11-28 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| a304f303-85dd-3217-855d-2ebff8ad4d8a | -2.33365 | -46.17012 | 2024-11-28 00:11:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 8b2bb349-e599-36cf-ad36-0a716bd3ef3a | -4.73449 | -46.54745 | 2024-11-28 00:11:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 32.0 |
| d980c08a-517f-3f98-a764-d7accb45e48d | -6.09174 | -41.93533 | 2024-11-28 00:11:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 36.2 |
| a960712c-5c0e-3e7e-9534-1bde541e0999 | -3.62765 | -42.39893 | 2024-11-28 00:11:00 | TERRA_M-M | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| b365dc2b-7990-31a2-b21a-93ca14180abb | -3.70036 | -43.42661 | 2024-11-28 00:11:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 116.4 |
| f1c30626-6a7c-39ae-99df-42b5d690ff1e | -2.41964 | -45.50766 | 2024-11-28 00:11:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 0a46d271-7f23-3cbc-ad02-96d52ef02f7a | -3.33476 | -44.06179 | 2024-11-28 00:11:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 50.2 |
| d6e2ff8b-f0e1-369f-90b1-ace61c3dae4f | -2.27806 | -47.10818 | 2024-11-28 00:11:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 86ce5ffc-ba95-3c44-ac3a-99228ddd8928 | -2.23959 | -48.53493 | 2024-11-28 00:11:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 3b75bf32-c68e-31cc-8973-e19c8a6132d5 | -4.77082 | -44.45167 | 2024-11-28 00:11:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| e21bd9fe-9ce2-37fc-9f9a-08178bea7c9c | -3.20973 | -46.59493 | 2024-11-28 00:11:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 53ad1b63-6fe7-36f9-899d-8a265e124801 | -4.76705 | -44.42618 | 2024-11-28 00:11:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 346.6 |
| 29900dc7-c799-3bec-88d9-63cea9e1b646 | -2.89629 | -45.38422 | 2024-11-28 00:11:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 43.3 |
| ec42f234-cb18-38a8-84bb-f4b5d03178bc | -3.67421 | -45.78048 | 2024-11-28 00:11:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 248.3 |
| 655601bb-a657-3088-a03a-1942e6c1a086 | -6.16879 | -42.61013 | 2024-11-28 00:11:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 105.3 |
| a0a840d7-a4ed-33b4-af33-ad6e5d54b015 | -5.98151 | -45.36398 | 2024-11-28 00:11:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 330.0 |
| 89908388-504d-3cdc-a934-ad72cf523422 | -2.87832 | -46.83644 | 2024-11-28 00:11:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 7574cb7f-5c3d-3706-9cdb-ffb28b795f2f | -3.66468 | -44.49212 | 2024-11-28 00:11:00 | TERRA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 1d110b0a-4b45-3dee-9a62-91c6b339d527 | -6.18042 | -42.61802 | 2024-11-28 00:11:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 39.5 |
| 22b96479-0358-31bd-899b-3bfdde9f7951 | -5.97442 | -45.34552 | 2024-11-28 00:11:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 155.6 |
| ce19f612-007f-3c4e-b55e-377c4ef87cd0 | -6.10369 | -43.95885 | 2024-11-28 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 151.2 |
| 39fb43fa-093f-3808-8861-cf9ed9db3d35 | -4.67274 | -44.60885 | 2024-11-28 00:11:00 | TERRA_M-M | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 16a8dd22-e2d9-39a2-8047-1cd35be4582a | -2.72537 | -48.88 | 2024-11-28 00:11:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 412cdaac-88a4-3ff9-804d-0c657a8cda71 | -3.66204 | -44.47303 | 2024-11-28 00:11:00 | TERRA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 5b3af3ef-22ec-3030-b7d0-13be9f962970 | -5.76021 | -46.25994 | 2024-11-28 00:11:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 7a4e132b-4f23-3962-8db1-44dd1f9d98ac | -6.1577 | -42.62127 | 2024-11-28 00:11:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 29.6 |
| 811617cc-0545-3fe8-9fa0-5fc1b4feb0e0 | -4.79543 | -44.44265 | 2024-11-28 00:11:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 1bcb177e-e09a-345a-bea5-9c3bef528498 | -2.54042 | -46.92945 | 2024-11-28 00:11:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 3c97a460-85ed-3271-9587-90630c21f974 | -5.99184 | -45.36813 | 2024-11-28 00:11:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| e7a4f80c-9c1a-317a-b3c7-0ec7a8b148e1 | -2.519 | -45.19653 | 2024-11-28 00:11:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 0a374c3a-c4fa-3d7a-a1dc-600b713eaea7 | -4.67532 | -44.62916 | 2024-11-28 00:11:00 | TERRA_M-M | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 27.9 |
| ecbeed1e-1fba-3de2-a8ab-260a75c2878c | -1.95896 | -46.57186 | 2024-11-28 00:11:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| bcc89c2d-b14d-3782-9fd0-875d9b146995 | -3.69856 | -43.4375 | 2024-11-28 00:11:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 3404c962-8ad0-3ad1-b32f-8aad6c4b9694 | -2.15375 | -46.0814 | 2024-11-28 00:11:00 | TERRA_M-M | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 21.8 |
| e6c3a9af-0e7f-371e-9cea-b1b879935e16 | -3.49733 | -44.60589 | 2024-11-28 00:11:00 | TERRA_M-M | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 5db20570-9053-3619-a524-23bc7a35e338 | -3.75015 | -40.97543 | 2024-11-28 00:11:00 | TERRA_M-M | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 2f34f9cf-6ac8-3be6-8b97-a3eea48ff0ff | -6.17084 | -42.62523 | 2024-11-28 00:11:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 79.6 |
| 2d2c5464-3cb0-3596-8dc2-4106ccf40527 | -3.54824 | -44.39178 | 2024-11-28 00:11:00 | TERRA_M-M | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 6f42b3f9-ab2b-3456-a9dc-51a5663072cd | -2.54282 | -46.9346 | 2024-11-28 00:11:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| c6546e5b-1f45-329a-9a3b-d4cb9494f766 | -4.77991 | -44.42427 | 2024-11-28 00:11:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 709.3 |
| c9d2efcd-1c90-3c21-893c-5d179badad37 | -5.68653 | -39.50983 | 2024-11-28 00:11:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 3e6c0a03-ba40-3625-ac01-1f73d3e4df9e | -4.6689 | -42.38226 | 2024-11-28 00:11:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| ad1225d7-6572-3ec1-a69b-f1b2807f8a1f | -2.5373 | -46.00479 | 2024-11-28 00:11:00 | TERRA_M-M | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 31.4 |
| e6019358-6a6f-3e39-8796-5483eff5c61f | -2.24262 | -48.52919 | 2024-11-28 00:11:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 42db11ca-9dcc-3b13-ae12-97a0338feeea | -4.13412 | -46.1283 | 2024-11-28 00:11:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 69efdbe2-d3b5-3c11-8b26-4bccce93a356 | -4.78516 | -44.46449 | 2024-11-28 00:11:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| be0513cb-ad6a-39f7-a1d0-314cab2ba5cf | -4.13061 | -46.10209 | 2024-11-28 00:11:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 1d13dfdd-8ddc-3373-9fe6-bd2415ab1319 | -3.71199 | -43.42493 | 2024-11-28 00:11:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ed3a4296-9b8f-36dd-91b0-4340f544628f | -3.33102 | -44.0688 | 2024-11-28 00:11:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 17f942cf-7ba7-3505-80c6-659488dec93a | -2.14956 | -46.08828 | 2024-11-28 00:11:00 | TERRA_M-M | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 594fd0ab-6aec-3dda-879d-2fddf6922a9d | -4.03645 | -46.53785 | 2024-11-28 00:11:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 21.0 |
| a6781de9-2c12-3a77-92f1-4dbb120cf7d9 | -1.54027 | -46.06132 | 2024-11-28 00:11:00 | TERRA_M-M | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 26.0 |
| c7928d62-687f-3a4e-9c39-d3e257357830 | -6.0935 | -41.94884 | 2024-11-28 00:11:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 42.0 |
| f33b74c5-c763-3134-a9fa-fdca1a8c5686 | -2.86111 | -46.83366 | 2024-11-28 00:11:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 313966fd-9409-3c00-af06-8c1fae279df7 | -2.55139 | -46.0028 | 2024-11-28 00:11:00 | TERRA_M-M | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 65.7 |
| f0efb571-b593-3c87-a5ed-c3af051b543b | -2.02492 | -45.69887 | 2024-11-28 00:11:00 | TERRA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 19.0 |


[Clique aqui para ver as próximas entradas](README7.md)
