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
| 28db0b0b-07b8-30a7-b721-edc0de43b09e | -5.93995 | -44.44317 | 2024-12-26 00:47:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 481510ea-88aa-31b0-ae25-658cc5ae05b5 | -4.34346 | -45.95275 | 2024-12-26 00:47:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0f0b8cec-d100-35f2-a615-cd3cd1647898 | -5.93588 | -44.43931 | 2024-12-26 00:47:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e4e458b1-cb45-3913-85ea-72d6607e25d1 | -2.64331 | -46.11058 | 2024-12-26 00:47:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 81df9db3-abc7-3ad8-bad8-0e87cdd66150 | -3.81659 | -46.72533 | 2024-12-26 00:47:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0c0a0577-7b3f-3e0e-928c-fe26cd33484e | -2.76231 | -44.69827 | 2024-12-26 00:47:00 | TERRA_M-M | BACURITUBA | MARANHÃO | Brasil | 2101350 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0a4b2a11-8f6f-3747-89e2-bb22f813d889 | -5.93739 | -44.4499 | 2024-12-26 00:47:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 5eb1cf27-693a-3edf-a420-c696619c0636 | -4.20123 | -46.11873 | 2024-12-26 00:47:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9889d51c-ed8b-336f-a62e-3d631a2a4231 | -5.21643 | -44.90271 | 2024-12-26 00:47:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| e4b90e57-928f-36fa-86ab-568ff4c959b0 | -3.45319 | -46.30289 | 2024-12-26 00:47:00 | TERRA_M-M | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7db8bdce-59ba-315d-aa64-d15fb97d6c9d | -3.07083 | -40.08364 | 2024-12-26 00:47:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 18.4 |
| aa992bf2-7895-3ed4-9e2e-1b29835fb0c6 | -7.7269 | -55.205898 | 2024-12-26 01:01:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b49f10ab-9abf-319e-b1ae-321f60db6cc5 | -7.7251 | -55.198101 | 2024-12-26 01:01:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a879fe8-b81c-3bc7-ade8-135bcc14b1f1 | -7.7367 | -55.203602 | 2024-12-26 01:01:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf50befb-b7b0-3c60-9cc6-b13b85d47a84 | 1.1169 | -59.4142 | 2024-12-26 01:01:00 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 62d72bc8-1c24-3fd5-8d47-92aacf1682da | -7.82982 | -35.1802 | 2024-12-26 03:12:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 412cc0e1-0a07-34e0-938d-78b3da1c401f | -8.06717 | -35.1567 | 2024-12-26 03:12:00 | NOAA-21 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ea4b5b71-9f3b-3abe-8a7f-120722663b8b | -5.47626 | -39.66733 | 2024-12-26 03:12:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 55cbd952-f954-3a17-8ae6-065a385aa1e0 | -7.83069 | -35.17513 | 2024-12-26 03:12:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| d8bd322d-1add-3ddd-a4b5-0d30c542eb3e | -7.92082 | -35.2241 | 2024-12-26 03:12:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d9fd71a4-b684-37d6-98c2-0ce15dcf97c7 | -7.76541 | -34.95116 | 2024-12-26 03:12:00 | NOAA-21 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 71d83877-ea48-3645-8cda-128bd9afc738 | -7.45993 | -35.24084 | 2024-12-26 03:12:00 | NOAA-21 | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| ab83cb55-799b-392e-a5a4-6502c7a7bb70 | -8.06573 | -35.15282 | 2024-12-26 03:12:00 | NOAA-21 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7363b239-72a1-3f59-b2dd-8fe0f1df9ad6 | -7.75995 | -34.95513 | 2024-12-26 03:12:00 | NOAA-21 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| 3179daf9-4b5e-3350-8df6-0204e68dcc93 | -7.81638 | -35.23001 | 2024-12-26 03:12:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| f61c744c-c3a7-3bc1-b079-69b3f5d5dd2d | -7.90364 | -35.21102 | 2024-12-26 03:12:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 856df9b1-9635-33d5-b701-09ae0bf66e8b | -6.59168 | -35.16331 | 2024-12-26 03:12:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| e24f720a-8670-3c78-9401-edfc53729533 | -7.76077 | -34.9503 | 2024-12-26 03:12:00 | NOAA-21 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 29.8 |
| b87697c9-9b9b-3921-af30-7493a261a421 | -7.90927 | -35.20661 | 2024-12-26 03:12:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 26b002d7-4288-3951-b0de-743920a0e492 | -7.91608 | -35.22338 | 2024-12-26 03:12:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d33cd1f1-6ba1-38aa-862e-7dcc4ba96e5d | -8.80955 | -36.51249 | 2024-12-26 03:12:00 | NOAA-21 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b3a7e5df-b071-30a8-a819-5232cae93321 | -7.90838 | -35.21169 | 2024-12-26 03:12:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| fcf74c52-1643-3f63-b6ff-5b97f46410d6 | -7.90453 | -35.20592 | 2024-12-26 03:12:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| fc1c150a-d5db-3b0e-a456-b9e72efb50dd | -8.1716 | -35.083 | 2024-12-26 03:12:00 | NOAA-21 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 61146f1e-dd03-37a4-b091-716f403825f5 | -6.17576 | -39.28418 | 2024-12-26 03:12:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 531ec212-0b43-377d-9dc9-9a0bab888b05 | -7.15471 | -35.07013 | 2024-12-26 03:12:00 | NOAA-21 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 6b8cf6c3-87dc-3942-b710-fa653c3577cc | -7.46083 | -35.23568 | 2024-12-26 03:12:00 | NOAA-21 | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 6bacc188-2c1f-33a5-baf7-605caed692c0 | -11.45765 | -41.15513 | 2024-12-26 03:14:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| ec5b18fa-4541-3446-9e0a-8c1bf440bb2c | -11.45689 | -41.15701 | 2024-12-26 03:14:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 4106c632-2794-3670-999e-07577087f503 | -11.45804 | -41.1515 | 2024-12-26 03:14:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 442ad588-0994-3368-814e-b954216cd2d6 | -3.06586 | -40.0814 | 2024-12-26 03:34:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c30bd2c2-9eca-3a30-83d8-703ffcf9e768 | -5.22079 | -44.89732 | 2024-12-26 03:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3dd23e87-d6dc-34be-b8fb-9992fcf7cf87 | -5.94734 | -44.44395 | 2024-12-26 03:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 569a8d05-2a12-31be-ada9-35e0a90e64b0 | -7.75848 | -34.94523 | 2024-12-26 03:36:00 | NPP-375D | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| b771d11e-e2db-3f27-b71e-635bdcb98f08 | -6.17807 | -39.28018 | 2024-12-26 03:36:00 | NPP-375D | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 8.2 |
| bea59a0f-0a83-3a2e-a354-8e29f49fd60d | -7.91242 | -35.20747 | 2024-12-26 03:36:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 40a04cf5-9347-3bf2-ba8f-3ea05c8a5b9f | -4.45844 | -46.67661 | 2024-12-26 03:36:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 37fe8b66-0ab1-3b67-a23b-57a911cfd18c | -5.47658 | -39.66528 | 2024-12-26 03:36:00 | NPP-375D | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d1a97bd4-c744-36d6-b476-1dba6cdfcabb | -5.47675 | -39.66344 | 2024-12-26 03:36:00 | NPP-375D | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| acb423f6-d88a-3dc8-81e0-4f465666db98 | -7.76315 | -34.94577 | 2024-12-26 03:36:00 | NPP-375D | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| f4a37977-6438-3019-bfd5-c253ee304674 | -7.81898 | -35.2214 | 2024-12-26 03:36:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 5f314ee6-9b10-39d3-8779-058566d2cc5e | -6.17743 | -39.28404 | 2024-12-26 03:36:00 | NPP-375D | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 1ac321bf-aa1b-309d-b1e5-d378b056efc3 | -7.02066 | -35.02443 | 2024-12-26 03:36:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f80de635-0d68-3ac1-8080-bd6dc2e77c71 | -4.32717 | -43.51111 | 2024-12-26 03:36:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| baffb676-5869-33aa-a928-b8b220940913 | -8.65273 | -35.67537 | 2024-12-26 03:36:00 | NPP-375D | PALMARES | PERNAMBUCO | Brasil | 2610004 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 45ea17f4-a535-33f3-b414-9f176c2fdfd1 | -5.47614 | -39.66712 | 2024-12-26 03:36:00 | NPP-375D | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 924958a5-fde0-36f8-8955-b5f8268f56eb | -7.15603 | -35.07117 | 2024-12-26 03:36:00 | NPP-375D | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ff19b3e7-6a0f-33aa-a3da-681703fab617 | -7.76183 | -34.94576 | 2024-12-26 03:36:00 | NPP-375D | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 4d38b4df-6e12-3486-a36a-dc90f7e599bc | -5.94807 | -44.44788 | 2024-12-26 03:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6af01e57-9a3d-3579-82de-8beda9ea1e99 | -8.07474 | -34.97739 | 2024-12-26 03:36:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 709dbeae-705a-3293-b1da-5060c75c813b | -6.44877 | -38.86412 | 2024-12-26 03:36:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9f8b27f7-23a8-3108-aea1-e1108228068e | -7.0173 | -35.02388 | 2024-12-26 03:36:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 174bfde6-5002-3ee3-b1e6-48ddb91dd0b0 | -7.15883 | -35.07527 | 2024-12-26 03:36:00 | NPP-375D | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 64471e5f-02b6-39f0-9ffa-ba52e9b1c589 | -5.21994 | -44.90201 | 2024-12-26 03:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cf63e005-3fb5-3eca-aea5-09e7c4bff1c3 | -7.01787 | -35.02031 | 2024-12-26 03:36:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d8b2da97-3c51-3236-9da5-703e2501b7f9 | -5.94886 | -44.4435 | 2024-12-26 03:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5fd06e8c-a7c8-3674-8c6d-7ebb8477cccb | -5.94292 | -44.44233 | 2024-12-26 03:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7e0fbf36-c919-349c-9dec-d402c97c5809 | -8.17005 | -35.0801 | 2024-12-26 03:36:00 | NPP-375D | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b1d940fe-3d2b-3f01-8b04-3b12f82a4d39 | -7.7665 | -34.94632 | 2024-12-26 03:36:00 | NPP-375D | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 12396960-0a8f-3048-9003-d9bb4eb53fbd | -4.32788 | -43.50701 | 2024-12-26 03:36:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58f22e71-cd56-3398-aab9-d68dbca07114 | -6.77008 | -35.15592 | 2024-12-26 03:36:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| edb2d555-b20e-3022-be58-9e8333b5bddf | -5.47722 | -39.66152 | 2024-12-26 03:36:00 | NPP-375D | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ac84d601-3562-3d47-9177-6c659c76f8a4 | -7.76259 | -34.94931 | 2024-12-26 03:36:00 | NPP-375D | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 94e15eca-ec24-39ac-9595-819c4f5ec625 | -3.99024 | -43.25666 | 2024-12-26 03:36:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5cb8446d-89d7-34dd-b52c-023216250e71 | -5.94216 | -44.4384 | 2024-12-26 03:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 447058ef-e6e9-352d-bf4f-0bf45dbea034 | -5.93546 | -44.44158 | 2024-12-26 03:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ecbfe813-50b9-3020-9799-8802f8c40b49 | -3.99092 | -43.25275 | 2024-12-26 03:36:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4bb4446c-b9eb-3ba8-8213-fb39c47e7b5f | -7.81503 | -35.22445 | 2024-12-26 03:36:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| bbe80c55-ce29-399d-9e95-bab2d602d889 | -5.52972 | -38.92144 | 2024-12-26 03:36:00 | NPP-375D | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 21250e9c-572f-3eba-bf7c-c5f25aef57d5 | -7.91185 | -35.21104 | 2024-12-26 03:36:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a7cab9d2-ca0f-3ab5-a434-c5256a7b72c0 | -8.51361 | -35.04332 | 2024-12-26 03:36:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 96202670-fed8-33b7-85fc-c6c546fc8c47 | -7.37842 | -34.88359 | 2024-12-26 03:36:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| deb6f324-0c16-304e-b64a-9e0dc0ab4a5d | -5.40591 | -37.03435 | 2024-12-26 03:36:00 | NPP-375D | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b82448fd-fe7f-39d8-af37-031b0b9476ba | -4.4654 | -46.67796 | 2024-12-26 03:36:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4a5b7c1e-bdf0-3f19-986b-4cd3b55f5441 | -6.59473 | -35.1582 | 2024-12-26 03:36:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 24.0 |
| 642ba442-1fc3-3311-81f5-44835e29e5f7 | -7.90848 | -35.21052 | 2024-12-26 03:36:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bd38135b-0f40-3515-892f-27b32dab1dff | -4.79524 | -37.79608 | 2024-12-26 03:36:00 | NPP-375D | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 464eeb82-57df-3cad-bf23-078cca4d202a | -7.92024 | -35.22341 | 2024-12-26 03:36:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 12ee6430-2a54-38d1-847b-41de9937dc3b | -6.76075 | -39.40451 | 2024-12-26 03:36:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a68c1768-6b44-34d1-bdd6-bd2fd4d01a6c | -8.51304 | -35.04686 | 2024-12-26 03:36:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4d939492-b8ca-32e8-b13a-851acf6dde2f | -3.99541 | -43.25488 | 2024-12-26 03:36:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60254917-6750-394a-87b0-08e7064a3ceb | -7.15661 | -35.06758 | 2024-12-26 03:36:00 | NPP-375D | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 29603ad1-d430-3f3b-9603-af3d29261b06 | -7.8184 | -35.22499 | 2024-12-26 03:36:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 457febb3-69da-34e5-b83e-6f79fa3a9850 | -5.21722 | -44.89668 | 2024-12-26 03:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3ac3028a-155c-3d39-89e1-071efe3215f2 | -5.9414 | -44.44277 | 2024-12-26 03:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 73d1769d-35a4-31cb-8f8d-8bc9e1dc4c03 | -7.76127 | -34.9493 | 2024-12-26 03:36:00 | NPP-375D | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ae80f0ea-3f22-3c58-b339-aae8e3e5972a | -7.9135 | -35.22234 | 2024-12-26 03:36:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ebae5082-e134-329c-a983-be3a144bf264 | -7.91744 | -35.21928 | 2024-12-26 03:36:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f86ade26-34bc-37fe-ae13-86febe395a54 | -6.28333 | -35.50969 | 2024-12-26 03:36:00 | NPP-375D | SERRINHA | RIO GRANDE DO NORTE | Brasil | 2413508 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e84040f5-a891-3c61-aefd-fc5fdc7b0c85 | -5.21639 | -44.90147 | 2024-12-26 03:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README3.md)
