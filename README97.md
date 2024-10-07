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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| baa055d6-9b21-30c0-bc51-25b8656a84ee | -17.19387 | -56.172 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| f8f0ed02-64be-3395-9e7e-39959ba93429 | -17.1976 | -56.29741 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 6dea674d-2117-3b8b-9ea8-12745e31efa5 | -17.19426 | -56.29683 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8a3810b0-8742-32d8-a423-38f46a9c45b5 | -17.1541 | -56.14243 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 7b8ea2f3-44b9-3a7f-9fd2-0262cc149d9e | -17.15351 | -56.1461 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b60251b0-bcf8-3acd-896e-5af32624f671 | -17.15291 | -56.14976 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c2ec9a8a-6f7f-315e-9754-d1c29d53db53 | -17.15052 | -56.16442 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 0d121fae-688d-374e-bf8c-d43fd3d99132 | -17.15017 | -56.14552 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 32e27c40-93ea-3b18-a8d0-0de56f79817c | -17.14898 | -56.15284 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2a6e99ff-23e2-31f8-9e2a-d910269f8b48 | -17.14839 | -56.15651 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 67fae856-970e-3ecc-8742-1fb89f02fdb8 | -17.14779 | -56.16018 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 90f67eab-52bc-3db5-94ea-1d534c27a70b | -17.14719 | -56.16384 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b8ad4eb1-99fc-326f-a1f0-396ae7e635df | -17.14505 | -56.15593 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 636a1c0a-fe74-3135-85c3-18ec980e301e | -17.10739 | -56.09686 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 11783509-e925-373e-8588-ae492013621c | -17.084 | -56.4029 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b769491c-8edd-39b4-9b67-9cb0ee489085 | -17.0686 | -56.08258 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 9245fd89-40d0-3876-9e37-d23151976c87 | -17.0561 | -56.05411 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| fe352dce-49e3-352d-b614-098f548b7247 | -17.05277 | -56.05353 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| b3fbc12d-164a-3e90-bdcb-fcfc5c303660 | -17.05217 | -56.05718 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 8d3280b1-5113-32a5-9b21-e49b74576225 | -17.04944 | -56.05295 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 552e0603-0d87-3fa7-9a0b-50792f078304 | -17.04884 | -56.05661 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 8dd4d3a1-0f33-3526-a21c-0133711079a4 | -16.97479 | -56.61401 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 2647c293-b0dc-3dca-92af-8d31252b052f | -16.97266 | -56.60592 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 2f5904b1-7abd-327a-b4dd-02a439dbb3f0 | -16.97204 | -56.60966 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 9f2d4c28-dabe-3b67-aab5-a76fe0586fb4 | -16.97142 | -56.61341 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| c01f7b94-d59a-34fe-948e-08847e80aa5b | -16.9708 | -56.61716 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| b8183e51-92f0-3a35-b37b-b2e58100f326 | -16.96788 | -56.13692 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 273f7ef5-b911-3e43-9137-ccd97ee8b584 | -16.96729 | -56.14059 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 81d2b227-e4c8-3823-9781-b278f2a0cbe1 | -16.96681 | -56.62032 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 6b86d8f4-055a-3962-8b28-125e18677fee | -16.96395 | -56.14 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f860a5d0-591e-35e0-bbdf-3218f2d82ce1 | -16.94321 | -56.61615 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| fe85644d-04e4-3b91-b8a1-a96477d14be5 | -16.93984 | -56.61555 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 989b0812-4d32-3b28-b2bf-d3fd7352c2df | -16.93922 | -56.6193 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 5144f7e6-7255-3761-aa4d-25324e12b5a6 | -16.9346 | -56.62621 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6445bfad-b636-30d9-bd65-acc3c05e5adb | -16.93447 | -55.83839 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 73d28f55-e9d0-36c6-b6d0-992596871f50 | -16.93016 | -55.82273 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| eaae0fec-4df9-3791-8938-c60321b7a77f | -16.92958 | -55.82636 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 535741fb-c582-35ca-8e37-651d16b8810f | -16.929 | -55.82999 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e95c02ba-9138-3538-8a13-6e73fae93cdd | -16.92876 | -56.61026 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| aec80f2e-d72b-3991-9246-d682e660b322 | -16.9251 | -55.83304 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 6f351002-bb08-3601-a74d-a186c7e17a95 | -16.91985 | -55.86571 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 73a6bd03-ce4c-3c88-956c-a8e745d250f0 | -16.91962 | -55.82464 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 4e41bb57-d4cf-3bd8-9592-7503f3d501b9 | -16.91927 | -55.86934 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| bc7fb3a6-7680-3ec7-b4d8-0cdaec7abec2 | -16.91572 | -55.82769 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 5ae33545-fc25-375f-848e-b6b18f23b25f | -16.89153 | -55.872 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2f81a4af-9b6d-347e-991a-4ffea3af6623 | -16.89094 | -55.87563 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 0635a10d-775b-31b8-9389-a7936b7b844b | -16.8708 | -55.83112 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e401f902-6383-3b23-a168-2638863fb1c7 | -16.86103 | -55.80708 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 15ce1510-c5a8-3829-a8d4-98406e99e2c3 | -16.85713 | -55.81012 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ae889bb3-becf-32b8-9698-e0c7ee1c9760 | -16.80906 | -55.8768 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a45d654f-a527-3de4-98e5-50d37fc36f62 | -16.79833 | -55.96471 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| cab85259-e896-38ef-a069-347908508749 | -16.65938 | -55.55726 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 358f7234-15c2-381b-af7a-3c55d82d8c21 | -16.65225 | -55.89848 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 85af5d56-6f7e-327d-8d4b-1dd474c5c5b6 | -16.65166 | -55.90211 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 005753d2-efd0-3d99-9da8-e7e994f3bd7e | -16.64892 | -55.8979 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 41bc8d25-6b92-3310-ada1-5ffa8dd37148 | -16.64833 | -55.90154 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| e01af4a8-b4c4-38d8-9482-f88d63d3ed9f | -16.64501 | -55.90097 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 2c69df62-047d-3e26-b6bd-fbb903f80ac0 | -16.64168 | -55.90039 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 94cc7750-192e-3d35-9974-c73bb41e80e5 | -16.64109 | -55.90403 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| db9ec72d-7ba1-392a-9c54-417f8d3a8e79 | -16.6405 | -55.90767 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| f765035d-d635-36b2-814b-83c1314329cf | -16.63717 | -55.90709 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3bf279aa-b5ae-309c-af04-b9d914f1a848 | -16.63326 | -55.91016 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| daa1651e-1f3c-35ce-bee4-26bc12e6276f | -16.62993 | -55.90958 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 7959db90-3e54-3600-bc66-5c3bb444beb0 | -16.62778 | -55.90173 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| ed92219f-8edb-3ec3-a711-23cbe22a0360 | -16.62719 | -55.90537 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 134f903b-11e4-3f60-a2a2-d11115b4047a | -16.62446 | -55.90116 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| c2125fd5-f9c9-3538-81a2-326cff97401c | -16.62387 | -55.90479 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 8479329d-2e8a-3162-ba0d-3fc483590f06 | -16.6221 | -55.91571 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c89e3c9d-33c9-325a-9149-0e60c88caf93 | -16.62151 | -55.91935 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 10df5c22-3c60-3dd5-bc83-4f5e877716c5 | -16.62113 | -55.90059 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 301e5c5b-9f70-3296-b4f0-1b28e5126792 | -16.62054 | -55.90422 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| e77c75c2-82e4-318e-9900-6397b2ff89d3 | -16.61818 | -55.91877 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 68cb2141-f062-3627-a7ef-0a6f9e01f948 | -16.6178 | -55.90001 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 4cc0cdad-107c-34ea-be58-7e27ef21b3a2 | -16.61721 | -55.90364 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| ef094c3b-5ff3-3b12-b81d-3591ef89827c | -16.61662 | -55.90728 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| cf78d4ac-97be-3bc6-88c7-dcd3776afcb1 | -16.61544 | -55.91456 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8f1201e2-e494-3f67-aa13-72e44cf6d396 | -16.61485 | -55.9182 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| bc1a0bda-7451-353d-803d-0f6cb2463636 | -16.61389 | -55.90307 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 855487d9-9f1f-3aa4-aeb3-6cd3c0df0d52 | -16.61329 | -55.90671 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1fd0276c-15b8-3d59-b4fa-ecfb29ea9298 | -16.6127 | -55.91035 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 89fd0dc9-ca23-3ca1-b2da-3e3839cb372e | -16.61211 | -55.91399 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e976a4bf-30f3-36db-b508-df7fbb6eabc3 | -16.59501 | -56.06107 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5cbf4f13-1410-33ac-9ae5-d4788585b692 | -16.58518 | -56.06285 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 9d03faed-f63d-3047-8fc5-b97cce02b0f3 | -16.70312 | -55.92224 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| b6817d3e-9bfc-39dd-af4c-3ef1e625c472 | -16.70235 | -55.94831 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c6b914fa-59ad-3cff-9219-4f1453c4d024 | -16.69961 | -55.94409 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e8997a6d-fb4e-30a7-8534-c7424b702fdb | -16.69902 | -55.94773 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 220966be-e321-3eac-975b-9ad80055a005 | -16.69844 | -55.95138 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 12e264fe-0c5d-34d0-a535-72fc10ff741b | -16.69511 | -55.9508 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6fca19aa-2c66-3080-b96b-c0ac3c41967f | -16.69452 | -55.95444 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 50d13de7-5abd-3637-aaef-8e6416304e6e | -16.6945 | -55.89084 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 73fd7f69-6e5d-306a-b154-a28a8fa95de0 | -16.69393 | -55.95809 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 9997f8c5-f211-3942-be43-3451c804fe3b | -16.69392 | -55.89447 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8ffe963e-135f-354a-92e4-86261e4f9633 | -16.69216 | -55.90538 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| cfb50f8b-7868-3dd5-affb-605a475f7454 | -16.69178 | -55.95022 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| bc2d2489-ba11-3166-a91e-9890177526e8 | -16.69119 | -55.95387 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d0822cf2-b95a-3f41-b808-ef70172e173f | -16.6906 | -55.95751 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7e736786-7044-305b-a62a-f44230430d1f | -16.68786 | -55.95329 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 74c9782c-3413-3f03-adaf-b7e5550c3696 | -16.68727 | -55.95694 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| fe18dddf-d8c6-3e5f-b364-35eb43853210 | -16.67514 | -55.88375 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |


[Clique aqui para ver as próximas entradas](README98.md)
