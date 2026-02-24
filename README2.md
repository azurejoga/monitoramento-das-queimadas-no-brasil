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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d175490-c3e2-33de-b99f-fbd4cac4a265 | -10.07332 | -37.61581 | 2026-02-24 03:44:00 | NOAA-21 | MONTE ALEGRE DE SERGIPE | SERGIPE | Brasil | 2804201 | 28 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c51df225-77cf-3d22-9a5b-6aebf8248b47 | -10.24827 | -36.30214 | 2026-02-24 03:44:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7285f26c-f60f-3428-b4f2-b88b0fb420f4 | -10.24442 | -36.30509 | 2026-02-24 03:44:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| da9d8807-d84d-36c2-b11a-8d4de498b4ed | -10.25487 | -36.30319 | 2026-02-24 03:44:00 | NOAA-21 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| d3c9deeb-0271-3f54-bd0d-4b61d83cec93 | -10.61744 | -37.04422 | 2026-02-24 03:44:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d67407f9-e79f-3415-8bdf-f222c6355ee3 | -8.79977 | -36.9551 | 2026-02-24 03:44:00 | NOAA-21 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c564eda4-1ee9-3e4c-a4c4-fd3a70edcb6d | -9.71045 | -37.26766 | 2026-02-24 03:44:00 | NOAA-21 | PALESTINA | ALAGOAS | Brasil | 2706208 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f371ab61-aacd-3718-b941-60d7b4ecd4c6 | -10.24497 | -36.30161 | 2026-02-24 03:44:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 73124127-26eb-3cd5-b451-1c703f7438d5 | -10.12998 | -36.14705 | 2026-02-24 03:44:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3b561486-5e5e-3e15-b47c-467fa26e15fb | 1.9419 | -60.3637 | 2026-02-24 03:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 57.8 |
| c5e1406a-6da9-3c67-adcd-98fd220ce292 | 1.9419 | -60.3637 | 2026-02-24 04:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 61.4 |
| c9dd32bf-0668-3841-b8ff-c6c8f7602dbc | 1.9419 | -60.3637 | 2026-02-24 04:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 1d3aec02-2273-3be9-8dc7-22d0e6cc95c1 | -4.15409 | -40.37856 | 2026-02-24 04:12:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fa8f8de3-18f1-3f83-a292-b7cdeaa22bb7 | -6.23626 | -37.4738 | 2026-02-24 04:14:00 | NPP-375D | SÃO JOSÉ DO BREJO DO CRUZ | PARAÍBA | Brasil | 2514651 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f855385b-0235-336f-a1c0-fea61ac24d33 | -10.24588 | -36.30456 | 2026-02-24 04:14:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 23d4a91e-f1b9-3752-8840-943eaecde2ba | -10.6157 | -37.04546 | 2026-02-24 04:14:00 | NPP-375D | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dfebfd11-0c94-3311-a332-1b244d57251d | -5.40641 | -37.33401 | 2026-02-24 04:14:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6d52be79-e5f6-3e21-88e3-1cff6f76bcdf | -10.85105 | -37.54089 | 2026-02-24 04:14:00 | NPP-375D | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 094a935c-5d48-324e-8017-b90a27febd98 | -10.24646 | -36.30034 | 2026-02-24 04:14:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b9c906bf-4dc4-3bb4-bf7f-46f5a4726fb0 | -10.07184 | -37.61724 | 2026-02-24 04:14:00 | NPP-375D | MONTE ALEGRE DE SERGIPE | SERGIPE | Brasil | 2804201 | 28 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a2f78428-fdc2-3ba1-98a0-9dca5f57f546 | -12.4214 | -44.44733 | 2026-02-24 04:16:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 686eb48c-7a32-3672-907a-080171463224 | -22.02295 | -49.50291 | 2026-02-24 04:18:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9e820883-1ca5-3212-be6b-0d51f5d4b755 | 1.9419 | -60.3637 | 2026-02-24 04:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 4ea1b979-a32f-3b2d-8d2d-af7b5ec3f5d0 | 1.9419 | -60.3637 | 2026-02-24 04:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 57.9 |
| b5e9195c-d167-3e67-8448-647fbcfb1004 | 1.20494 | -59.97432 | 2026-02-24 04:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7942927a-ee5e-3b38-bce3-3c0bbf04b173 | 1.19791 | -59.97588 | 2026-02-24 04:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3314ff6-d9c6-3ef2-8194-7d5b8d93ad90 | -10.24904 | -36.30319 | 2026-02-24 04:33:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4f7a249c-4409-398b-943b-7d0bed9e1ee7 | -10.25082 | -36.30393 | 2026-02-24 04:33:00 | NOAA-20 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 6e3bfe25-1d4e-3c6b-bc54-0267ea88017b | -10.24834 | -36.30906 | 2026-02-24 04:33:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 204b8426-0d3c-366e-b9f5-cfa50b470b6c | -6.99996 | -46.38965 | 2026-02-24 04:33:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d56873f-bdbe-3267-abad-bee82d32394b | -18.9732 | -52.92706 | 2026-02-24 04:38:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3e62fcb-6000-3e85-b8c8-9c2727fc106a | 1.9419 | -60.3637 | 2026-02-24 04:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 61.3 |
| cb86163a-49c4-31c1-9e56-739a126e17fc | 1.9419 | -60.3637 | 2026-02-24 04:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.1 |
| e3e790e5-8782-3ae2-bfd4-352be406e59f | 1.9419 | -60.3637 | 2026-02-24 05:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 52.3 |
| f4f75a64-629c-3550-b714-745509fb4c82 | 1.9419 | -60.3637 | 2026-02-24 05:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.4 |
| ed22919e-42cc-3fe0-b538-ea68a3cecc51 | 1.9419 | -60.3637 | 2026-02-24 05:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 55.9 |
| d5d464d0-388e-39ca-a02d-feaac0de12ab | 1.01635 | -59.76468 | 2026-02-24 05:22:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9b407756-f45c-36c5-91d0-d7c91564c992 | 4.13059 | -61.07889 | 2026-02-24 05:22:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c2fa2fe-3dcf-345a-8d5e-34cac1ee374b | 3.93712 | -60.0561 | 2026-02-24 05:22:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 485e7006-16fb-3bab-909e-c0e808778995 | 1.20214 | -59.97459 | 2026-02-24 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23cac4b0-e8d2-3f89-86ef-8305cd602f1f | 2.86092 | -60.771 | 2026-02-24 05:22:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce27eb55-f995-3f67-90f0-fcb97288c2e5 | 3.95045 | -59.59418 | 2026-02-24 05:22:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e76fed05-5cb1-303d-8fe3-651ad5f7ba3c | 0.31212 | -60.44092 | 2026-02-24 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f69b73a-a2c6-390a-a5b4-d79aef46b4a6 | 2.2841 | -60.5165 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2baaa19-adb8-3d52-aefc-173498187e63 | 3.14169 | -59.99652 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9999a034-6de2-33ac-bced-ebd9c7212ca4 | 2.71607 | -60.22773 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c0f427c4-8ddd-3574-99c2-40b0c6118d31 | 3.18038 | -59.95764 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e731ff13-c0ac-3322-8987-83b5c08e64d7 | 4.79424 | -60.28723 | 2026-02-24 05:22:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 936f724c-071e-36cf-bf0d-b86a2c24b11e | 1.52246 | -60.38835 | 2026-02-24 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8d74ae7-cd6b-37ad-9c87-29dac0cdbd1b | 0.63872 | -60.66077 | 2026-02-24 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 94c60a82-1ad4-3b79-bbc9-b26e9e37e2d8 | 0.16164 | -60.48217 | 2026-02-24 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9379231-f32f-327f-8619-68095b5f6e81 | 2.71778 | -60.23856 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2aafd068-67b6-3885-817e-eaf8bf5bc4cc | 3.1445 | -59.99243 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99c790bb-c706-36d6-bc98-99facb51cf16 | 2.22914 | -60.70535 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bd3dee48-40d1-31cd-b959-1bca06ac6966 | 0.86196 | -59.69374 | 2026-02-24 05:22:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6484904e-5b49-3037-8206-41f87bf40c20 | 1.83949 | -60.61404 | 2026-02-24 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bdb5eb8d-ae40-3404-a388-8ffb824da0d9 | 3.17142 | -59.96633 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0d21a61-7c02-3f28-8a3c-efd762d14f88 | 1.93442 | -60.36935 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 705510f9-130c-37be-812c-6f8492824e0c | 1.20492 | -59.9706 | 2026-02-24 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 680b94bb-fadd-346f-ab6a-e45f22220ac9 | 1.94341 | -60.3606 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0c2afc37-b298-3b00-a4fb-2f8a3838b865 | 3.16525 | -59.97094 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8cc78f3c-6e65-3971-8a36-39fddece2f79 | 1.75766 | -60.76594 | 2026-02-24 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7adf0817-2b59-3ee9-a667-5f77cae0ad60 | 4.7908 | -60.2877 | 2026-02-24 05:22:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2437cb31-7ee1-3627-a119-b9c663ee6050 | 1.9333 | -60.36214 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fba2f8d8-cf87-3d66-9043-8a42d5d51d8e | 3.16572 | -60.45029 | 2026-02-24 05:22:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 16cbe03a-8c31-39be-932d-87a2848d9937 | 2.2354 | -60.70062 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8a5298e7-67f8-3e15-80ad-080069670689 | 3.93656 | -60.05246 | 2026-02-24 05:22:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d7678ab-7ac1-376c-ab3e-fac87dcd8a1e | 1.2016 | -59.97112 | 2026-02-24 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 719b12b4-65e8-3767-8dff-dfb7e9402d8c | 3.18654 | -59.95304 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 61e8f67b-a556-3251-939b-2b01be9b48f5 | 1.94848 | -60.37091 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6dca0dce-e63e-3d2f-9865-a536a5d80409 | 1.09721 | -59.63197 | 2026-02-24 05:22:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0a1c066c-f6fb-3b06-9df5-47db7701066f | 3.16189 | -59.97145 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d36418bf-cde0-3b10-be30-35ff51e39327 | 3.4357 | -59.89642 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4763b8cb-b2dc-34fe-af6f-a8e1e007bc53 | 3.42608 | -59.89402 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08acdace-ded5-35a8-9cf7-9976dcdcdfac | 1.94959 | -60.35596 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 333b8c4b-7ba8-3d6c-a2ce-90b25e93275d | 1.83028 | -60.8497 | 2026-02-24 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bebc3d49-a52f-32c6-9d87-c6ad255b9590 | 2.5152 | -60.98952 | 2026-02-24 05:22:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9fbcc202-d949-3b1a-a3d4-c2ef702b41d8 | 1.92712 | -60.36677 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f912c2c9-2abe-350b-9237-cc0752d46295 | 3.17422 | -59.96225 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b1d87b37-2a17-3065-9e87-57438e92561a | 1.93611 | -60.35802 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 04a1c063-fb49-3682-92cc-bffa90a2455c | 3.2667 | -59.92268 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eaff8aab-8fd9-3a55-bd83-96b10f6ab71d | 1.33829 | -60.06126 | 2026-02-24 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b0db08cc-1a89-3c09-a9bf-c14ff45bb768 | 0.30933 | -60.44498 | 2026-02-24 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 249ddf37-899f-35a1-91fd-ddf1ac5e53ee | 3.16288 | -60.4545 | 2026-02-24 05:22:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5b60e2a6-a63b-3872-86cd-804e129c7b22 | 2.85748 | -60.77153 | 2026-02-24 05:22:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d7def36-458d-3294-814a-45fdd1196752 | 1.93049 | -60.36626 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcca8d06-55b3-3631-a9be-06daf6d12dd2 | 1.93105 | -60.36986 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d88690d7-dcab-33de-8dec-141b0b479812 | 3.42816 | -61.9909 | 2026-02-24 05:22:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 724241a6-0bc2-39a6-bd9c-c45ea3293d31 | 1.10277 | -59.59909 | 2026-02-24 05:22:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 44b9cbfa-5a42-364c-9dd4-e8d3cfa289a8 | 0.10503 | -60.7287 | 2026-02-24 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96f3ce41-e6f7-3a7c-9ab0-943a8e3fd7bf | 1.94792 | -60.36729 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ca0e6169-c7d8-30b0-bbba-e59cdf40ee17 | 1.09947 | -59.59959 | 2026-02-24 05:22:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5625c2b-6004-3cdf-9085-7ae4de2d9b96 | 2.71986 | -60.24139 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bcc2f69-b5e6-3aa5-ac18-273de8f3a381 | 3.16806 | -59.96684 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 646169da-56a0-3aaf-8f48-2d64cc2af4ca | 3.94398 | -60.53214 | 2026-02-24 05:22:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81425dcd-8068-3cfd-81f2-0ab8c7172aa8 | 3.43625 | -59.89998 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0725dc1a-ecb0-3c6b-941b-e76ae8d199df | 1.93386 | -60.36575 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7449319a-fa8f-3957-acd5-193300672b4e | 4.33258 | -60.20889 | 2026-02-24 05:22:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a975403-507e-3308-a17f-deb9925686aa | 4.33316 | -60.21261 | 2026-02-24 05:22:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e676cdc5-ba53-3674-8f30-b88923a2e272 | 2.23598 | -60.70433 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README3.md)
