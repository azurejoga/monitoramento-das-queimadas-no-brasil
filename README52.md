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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cab32206-23e8-3051-bd06-18479175cb35 | -3.50005 | -50.46618 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 457802d5-d96a-3ce1-8a5a-3ee286ed7fa2 | -3.95822 | -50.19768 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 46372be0-e528-3cb3-94b7-88c25663890d | -3.32913 | -53.0996 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6ff2906-333e-3d96-b1ea-adea59bf1835 | -6.16508 | -44.42472 | 2024-11-24 04:53:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8b601b1-3f70-3350-943b-a91055d1890c | 0.87733 | -54.63501 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5fc89e9a-9079-390e-8996-50b95772eff3 | -3.21973 | -49.80281 | 2024-11-24 04:53:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 801642aa-f8b7-3553-8f0f-0e05cc4016d5 | -11.04152 | -47.48757 | 2024-11-24 04:53:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 48c9dd77-d245-375a-acd0-5997720195a6 | -3.47932 | -51.9883 | 2024-11-24 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 595806a9-6770-3157-9ddd-bd7b137716ed | -3.52292 | -53.788 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fc75ba3a-afa7-30b7-a513-28b577ae6a65 | -2.11834 | -50.56944 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f34d543a-0b2e-34ce-b5a7-5b417428d7e9 | -2.24366 | -53.61684 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f660530-1682-3dab-af92-a036756ab795 | 1.32497 | -50.62144 | 2024-11-24 04:53:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de518206-379b-3a2e-b218-8dd296d8a753 | -3.15502 | -50.58838 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5e4193fc-7190-3dc9-ba96-a31756bec184 | -2.80275 | -53.00685 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72c587f2-5b23-360c-8426-f7c49cd7709d | -9.24645 | -49.98763 | 2024-11-24 04:53:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bed24388-2dcd-3cfd-a75c-d74324a44638 | -1.69457 | -55.15777 | 2024-11-24 04:53:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0674ca57-a37d-37a2-a474-49136c20cb73 | -1.98962 | -53.13644 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 805b9310-9365-32fa-9b20-dcbe3c42a36e | -2.09187 | -50.49611 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d9b26fe-050d-3ebd-8932-9b0627405a55 | -2.1583 | -50.61524 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22e04711-9586-3a7a-a774-90e65b2ddd8c | -3.24516 | -53.41487 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c68fbbb-f16b-34bf-9ea3-fef40f4d7349 | -2.76945 | -54.06625 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c86dcfbb-ce73-3366-8f58-fe52a5b5c7c4 | -1.29389 | -51.73439 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 67420f84-0e3e-3915-b04a-1ba7bf784fb9 | -1.45383 | -54.96842 | 2024-11-24 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e6899f3-14ba-3c7f-a13b-29ff2ad8d2fc | -3.48412 | -49.90404 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c50b8c11-492c-39dd-9949-5f0dda4dbccb | -3.96114 | -52.23302 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2cd38d6f-7966-3910-8225-ac8efaeba9a2 | -2.28899 | -50.58421 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bbbc5222-15f7-34e3-9cdd-872ff20cb420 | -1.60946 | -54.41159 | 2024-11-24 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 073edbf1-9bf1-3130-8a14-d6de5b2af260 | -1.81584 | -50.98317 | 2024-11-24 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b5b3dcb-9ce2-36b9-aac7-a7f194dcc9df | -2.67216 | -53.03686 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0cdca6e-c590-3d84-b0b5-3d6773b32ca4 | -2.21101 | -50.69587 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c4e9cd8-5676-3731-87a0-9e915aa9acea | -3.57491 | -54.68324 | 2024-11-24 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee3b3dab-cdd1-3e83-b1e5-37a0e2230628 | -2.63989 | -51.89588 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1542fdd8-53e0-3f4b-bc7d-300f7e993ed2 | -3.18487 | -54.76802 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 46d9015e-2bfd-3ed3-a9fa-ed7ec1ede916 | -2.30937 | -51.26603 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09999828-02ad-3ec2-a232-757a6e806349 | -2.21086 | -53.75779 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ddce37f7-e18a-3df5-832f-f6a7f1da8e96 | -4.35752 | -50.81847 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8003b7a-5d1d-3a4a-a46f-635c8d1e7136 | -1.46194 | -51.11625 | 2024-11-24 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 91d6667e-c4b1-3112-a106-46748508a406 | -1.59973 | -52.58662 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 699a3756-b9f1-33f7-b958-355c42609c12 | -3.56739 | -51.114 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 912cd40d-1d1b-3e1f-a3a6-12dc046edf6d | -5.10323 | -43.14436 | 2024-11-24 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 31c43294-ba16-35bc-8bc8-c0a9522d9f46 | -2.67755 | -52.52467 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e43040eb-f1f7-3674-93db-c249d6c49564 | -6.84592 | -44.38663 | 2024-11-24 04:53:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ec4ed7de-7ab1-374a-af02-325716eae110 | -0.27496 | -51.59601 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57c94ea1-b855-3f1e-9872-5ebeea4856e3 | -2.4131 | -51.97609 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef2b096f-ba8a-349f-9239-f4ba290efab1 | -3.31043 | -50.0332 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4990adb7-831f-3923-bb64-55bbcef33e61 | -2.07412 | -51.46595 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5fb83fb4-6d9d-373a-a9af-3b3be0987efa | -5.4133 | -44.77061 | 2024-11-24 04:53:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8e6db33-9dfd-3147-a911-781a704bf6a1 | -0.88399 | -51.72237 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5039d101-e148-36b4-88cb-ff1c39c1ace9 | -3.3884 | -50.32198 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ab3507a0-b9c2-3ebf-a0c7-613abc7ebb09 | -0.95333 | -51.71611 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fd019cc-8f16-3a10-b893-6dba8d47503a | -2.26886 | -50.45705 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b06c1d8-e672-3c13-a3e1-008bbb48241a | -5.06006 | -43.69998 | 2024-11-24 04:53:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05171234-7028-3e2c-9a17-c6cd7194b12d | -1.4045 | -54.46952 | 2024-11-24 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0506ab02-08b7-358f-a8eb-21c1d0a63bc8 | -1.4519 | -53.40166 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 32d9f9c4-afb5-3be4-a668-f7999149c44b | -3.00305 | -51.55106 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7e9f19d9-4452-3bac-a8b9-a850d7a5f5e5 | -1.9658 | -48.38554 | 2024-11-24 04:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4ed1f519-f798-3ef6-807b-e11cd1bc7714 | -5.86297 | -47.19282 | 2024-11-24 04:53:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff4c88c8-472f-3365-9dca-b10bfcbb3a58 | -1.07556 | -53.3658 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a0ce210c-788f-3fec-88b0-5cc23f3417f1 | -3.81971 | -52.22466 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cde8d9d3-dd6a-31ce-8edc-b637b7d982e6 | -2.0703 | -50.31262 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dfb83106-6a99-326a-8e78-546b747b649d | -1.24166 | -51.61406 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ba67c0d-7cdb-34fa-86f5-c60c78839486 | -2.37052 | -49.82814 | 2024-11-24 04:53:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b864fca-a5b9-35f7-9096-cf1e77370c1b | -3.12053 | -53.10671 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0526c403-2a1b-3be5-8b10-a9c755974536 | -1.61466 | -52.42559 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e1d2ac58-469b-364d-a32d-6c3f2c5697c6 | -2.2402 | -46.1518 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 130f5af3-59db-33eb-9b96-7ab87db1c680 | -2.20896 | -50.532 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6adf182a-e589-30b5-8a2e-1765890965aa | -4.09899 | -51.06189 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 100c6574-2ecf-3b4d-a820-6d0f8cbfd209 | -3.10664 | -53.10818 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1789cd7-1cb8-3752-9a4b-ff89f273035c | -3.70724 | -51.79151 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb4c794b-b722-3ad7-ab1f-1449fdc95a89 | -1.42388 | -51.12101 | 2024-11-24 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4b39e386-3b5e-34f2-8898-2ede5ed37978 | -2.62353 | -51.80549 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9db7029e-7378-3449-baad-83b7fb7cb6d9 | -1.45631 | -54.50904 | 2024-11-24 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cb2776e0-81ed-337d-876e-744eaf1db10b | -1.96943 | -53.14008 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c95d51b3-34cc-35fb-b4e2-e4c9fba73b31 | -2.46032 | -50.22357 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e475ee3-bcd2-3aaf-982d-38e51dd95763 | -3.10904 | -53.98195 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f22e5797-d44a-3f97-b86d-f24375ff7da4 | -2.74729 | -54.02856 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8a7cb15b-6658-3c3b-9d37-48a6e631b530 | -1.64097 | -55.25883 | 2024-11-24 04:53:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e18b5877-9945-3a5f-8bd0-a0e836886def | -3.95421 | -50.20087 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3b90f052-1e8e-3d96-909c-d6f9051efecf | -0.83742 | -52.54631 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6d6c9f10-50d5-37b4-b44c-a3792bd62009 | -1.36457 | -52.5461 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11f990db-2be7-33aa-8f09-be7954df2dff | -2.01627 | -51.18147 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af470b45-2800-39a7-99c5-63049bd13743 | -4.24557 | -48.63217 | 2024-11-24 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6bfb435c-976d-3e23-b2df-96452e740a13 | -3.2504 | -54.22063 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce2d46d7-eda7-3f30-a764-7bd557657429 | -1.42773 | -51.11806 | 2024-11-24 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42a698a5-ec28-341c-b242-e56b8205a994 | -1.2886 | -52.4667 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33933589-f0b5-33bd-8f9d-975837f989c1 | -3.5155 | -53.81287 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 6c7ebd33-fab4-303f-891e-7396e13afae9 | -3.31532 | -54.16585 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9220daeb-c966-3a0d-9a0b-17704085e3c5 | -3.26985 | -52.63187 | 2024-11-24 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 718d1998-bc9b-3c68-ae89-bd1d62f4d209 | -2.64557 | -53.98299 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d9d136ef-a1fe-3ab7-8922-5f1fd8c3d01f | -4.63632 | -49.54095 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4998f309-889e-3f11-8916-29119d556b71 | -3.24731 | -50.41714 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fed2d4ef-376a-35b2-831e-0149e0ef011a | -3.49317 | -52.00803 | 2024-11-24 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 484e12b4-e0a1-3907-938a-44fefb502a9a | -3.61986 | -52.46113 | 2024-11-24 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 66bb75c4-e2e9-3cfe-a8cc-c1e9717aa7f1 | -3.85213 | -50.43304 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 19d0bfbe-4f8d-30fb-a066-f926cb1252fa | -3.01221 | -51.38237 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9330a137-6b0a-35a7-86d0-eff90ae63706 | -2.45005 | -49.0616 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e0d2bcb5-fbf2-387b-8d9f-4aad59c1eaaf | -3.4959 | -51.17847 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecee5428-68ad-30c3-af53-d0dd6f719950 | -0.97037 | -51.71522 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 292809f5-5186-3d48-ace5-8c6afd4ef809 | -1.42826 | -51.1146 | 2024-11-24 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6dd03b7d-3a45-3b87-a3fa-664e0112b8d6 | -2.45442 | -53.70464 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README53.md)
