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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b037f895-99dc-3133-94ab-0e4f26f855df | 1.94088 | -60.36226 | 2026-02-24 05:52:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0d8a8e6a-e883-30e0-b579-5948fb23d2ce | 4.79496 | -60.28418 | 2026-02-24 05:52:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45c18c4b-0ff1-3fe1-8f33-c0f2b7c7ee24 | 1.94798 | -60.35597 | 2026-02-24 05:52:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cc333d83-f88f-3181-8e33-c5203a4be62c | 3.15834 | -59.97662 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c377308-eed6-3edd-aa55-beb4d7776913 | 3.94289 | -60.53315 | 2026-02-24 05:52:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43afc026-e7f8-3800-af23-e3ab54dfa3df | 3.15989 | -59.97277 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 995462c5-cc84-3096-9f6c-efccdda24d3c | 3.16432 | -60.45135 | 2026-02-24 05:52:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1d7d5a3-404c-3f38-88d5-88bdbeda3ad0 | 4.00545 | -60.35235 | 2026-02-24 05:52:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6dfc624c-9994-3274-8edb-9cc7c065bab1 | 3.26584 | -59.92589 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06362182-0faf-31a2-8547-e6b3c20b3870 | 2.23274 | -60.70413 | 2026-02-24 05:52:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a388ea40-40c1-3dd6-adc9-0df7f458e1cf | 4.28622 | -60.74355 | 2026-02-24 05:52:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03c0bc34-76ee-374e-b29d-d5844a7705ec | 1.94402 | -60.3566 | 2026-02-24 05:52:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 74c679e3-96bb-32ac-8e03-ac30dfc560d8 | 1.92272 | -60.37547 | 2026-02-24 05:52:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf5e2fb1-2d6d-302e-bf9a-6463abbf2929 | 2.71613 | -60.22942 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 28bfacae-2e8b-3bfd-9fd7-27a562c6d1e6 | 1.94169 | -60.36726 | 2026-02-24 05:52:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ddb256ea-b3d9-333c-9862-d83d6d1bcdbc | 3.14721 | -59.99588 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49e7fff5-05dd-381e-8b31-c91822eac8d2 | 3.42688 | -59.89715 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5b754b3-2910-3a6d-a0f9-412831e6d1f8 | 3.16148 | -59.97083 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91e25693-86f4-3feb-8a87-fc0d185e2793 | 3.15672 | -59.97855 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4494e9e7-5231-379c-958c-1de24b172052 | 3.28113 | -60.01816 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| efc529fa-5446-3ae6-b0b7-1f760329b877 | 0.31278 | -60.44295 | 2026-02-24 05:52:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 786628e9-fcbb-3d4f-b045-00185e696e51 | 2.71067 | -60.24575 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 882c19ae-b7d1-367f-988c-f8f6a6185249 | 1.9419 | -60.3637 | 2026-02-24 06:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 49.8 |
| ac74f4e9-e9e9-3a9d-bf5d-565b691b9210 | 1.9419 | -60.3637 | 2026-02-24 06:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 1f560c3e-be4f-3001-986f-3a445241ffd1 | 3.14302 | -59.99638 | 2026-02-24 06:12:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5630235a-38e6-316d-aa68-94a9b2b8bedd | 3.18022 | -59.95648 | 2026-02-24 06:12:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9791b5f1-d6ee-36c2-b55d-7acfbf7aaf5e | 3.43535 | -59.89933 | 2026-02-24 06:12:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5d55b383-08db-31e9-9255-1fd86d5fc011 | 2.72008 | -60.24775 | 2026-02-24 06:12:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88fd4395-4840-3c62-a75e-f251d97220a6 | 2.87382 | -60.26499 | 2026-02-24 06:12:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1a3c3816-e527-395b-9c32-e1b0520d0143 | 3.14912 | -59.99532 | 2026-02-24 06:12:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95b27e54-1350-36be-80fe-4884d7609c36 | 3.15364 | -59.98503 | 2026-02-24 06:12:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 048b0076-81cb-36a8-9d1f-40847d334940 | 3.16426 | -59.97363 | 2026-02-24 06:12:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a68766c5-1153-38f1-a3a2-bb623a5ab3b0 | 2.71088 | -60.23046 | 2026-02-24 06:12:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39044101-7884-37b2-8dfa-a0ef9b892631 | 3.16958 | -59.96793 | 2026-02-24 06:12:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 264b1a17-2a18-3deb-84f0-fe73759a6f64 | 2.70852 | -60.21681 | 2026-02-24 06:12:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b8f4d4b-6cb9-3162-aae2-8a3fe17f6f63 | 2.71402 | -60.24867 | 2026-02-24 06:12:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca10e8c5-c64f-3acf-b2ab-9053f1ac6fe9 | 3.15285 | -59.98038 | 2026-02-24 06:12:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 832e7bd2-c821-39a3-9dad-849a6736995e | 3.16347 | -59.96895 | 2026-02-24 06:12:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d955a7a-21e7-38a6-b90e-178d05c7ca67 | 3.16646 | -60.45385 | 2026-02-24 06:12:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9425d84d-650d-3b17-b70b-e1bd0532bd12 | 2.71244 | -60.24667 | 2026-02-24 06:12:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a782f6e-4759-36c3-a046-c5973261b679 | 3.42842 | -59.89565 | 2026-02-24 06:12:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8dce3512-6d5a-3d81-a6b8-0b6945caede3 | 3.1657 | -60.44952 | 2026-02-24 06:12:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c182f2d-b07d-3dfe-bf23-0dd80e1bf036 | 3.19166 | -59.94968 | 2026-02-24 06:12:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab6f970d-fd4c-30f0-8c3f-ca518e5ce9e9 | 3.168 | -60.44741 | 2026-02-24 06:12:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d36d578-ebbe-38c6-85b6-c0904192c300 | 3.14754 | -59.98608 | 2026-02-24 06:12:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3fc7882b-40bb-3938-98cd-63fd114a7c49 | 3.19223 | -59.95102 | 2026-02-24 06:12:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28477a4b-abb0-3cfc-ba22-4aebbefeeffc | 3.18612 | -59.95205 | 2026-02-24 06:12:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 85de65bd-a32c-3338-b6b6-e6617f601ab9 | 3.1749 | -59.9622 | 2026-02-24 06:12:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b40548c-6211-3bba-9884-5917c0d807a7 | 2.86779 | -60.26597 | 2026-02-24 06:12:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c66b94d9-1152-3b72-96bc-7eac22e64288 | 3.18554 | -59.95074 | 2026-02-24 06:12:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9bc8d1c0-af01-3296-823b-fade82c82d2b | 3.18633 | -59.95541 | 2026-02-24 06:12:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0b1a11a-6ddc-34f4-b6af-1bdca934055b | 2.71849 | -60.24572 | 2026-02-24 06:12:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6a3035d-51a3-308f-89d1-d7083af7a678 | 3.15816 | -59.97466 | 2026-02-24 06:12:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b7c807f-683e-3524-a211-f580038a2622 | 3.16353 | -60.45708 | 2026-02-24 06:12:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5a27d0f-2d21-35ff-b467-8f2361c040f1 | 2.71773 | -60.2411 | 2026-02-24 06:12:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac58bcda-f7af-3628-b944-094638e8a86d | 2.71693 | -60.22945 | 2026-02-24 06:12:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54b2fcca-55de-319b-91fd-fbf2b2a91d97 | 3.15895 | -59.97933 | 2026-02-24 06:12:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 04da07d2-90df-38ef-9c1f-0d188e747473 | 3.16873 | -60.45176 | 2026-02-24 06:12:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e526dbd-c3f0-3554-a431-8deb7eacb06f | 2.71322 | -60.21375 | 2026-02-24 06:12:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 88a80fc1-d452-3589-9baa-786303c7f04c | 3.18082 | -59.95776 | 2026-02-24 06:12:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eafc74c7-8ba3-359f-adbc-dea2490511f3 | 2.85787 | -60.7697 | 2026-02-24 06:12:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e67d6920-2c44-30a5-95f9-93fcac201351 | 3.1628 | -60.45275 | 2026-02-24 06:12:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be17a1e7-c2d7-3fec-aa45-349050966b54 | 2.71458 | -60.21583 | 2026-02-24 06:12:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0741c364-f3c7-38c3-8fff-afa671605965 | 3.16053 | -60.45483 | 2026-02-24 06:12:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9011a373-6db5-3796-a9f7-2bd410d544ff | 2.85857 | -60.77388 | 2026-02-24 06:12:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 561cb69e-bf53-367e-aefd-154f5bec6c02 | 1.92755 | -60.37034 | 2026-02-24 06:14:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45a3fc5f-e751-352b-aeb5-fc8d739c4901 | 2.23384 | -60.70366 | 2026-02-24 06:14:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dfff75c8-a90b-363e-8aeb-2663d54d416d | 1.83662 | -60.6143 | 2026-02-24 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c3ca8cfc-db88-3f4f-b481-fb37eda3abe5 | 0.31056 | -60.44276 | 2026-02-24 06:14:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2967ebdd-8066-3d35-8fa1-ce3617dd02eb | 2.22794 | -60.70473 | 2026-02-24 06:14:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f91e62e-9d8f-3471-a414-6929f44d0f40 | 1.95033 | -60.35717 | 2026-02-24 06:14:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 05b75de4-2453-3576-aa00-dd01660ca27d | 1.94426 | -60.35818 | 2026-02-24 06:14:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7eb42f4a-bd93-3929-b27d-6ee2b6f83696 | 1.94574 | -60.36719 | 2026-02-24 06:14:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 75495e6d-fb49-3f6a-a73d-8534217697ca | 1.9283 | -60.37482 | 2026-02-24 06:14:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 241141d6-d261-3d49-a2f6-8d8b75516c41 | 1.93967 | -60.36818 | 2026-02-24 06:14:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 379d62e8-d72d-36f2-807a-74ea54d54558 | 1.945 | -60.36271 | 2026-02-24 06:14:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cc470a6d-636e-3680-afbf-c8c4c020dfef | 0.31133 | -60.44756 | 2026-02-24 06:14:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f376a0fd-6879-3150-8c48-efc06e4ac8b4 | 1.93361 | -60.36925 | 2026-02-24 06:14:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 711e4b73-d9fa-3221-bf3e-7fba13bafb06 | 1.10545 | -59.59986 | 2026-02-24 06:14:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2252cd1a-3a3c-3a23-89ea-0c51cfaab190 | 1.92678 | -60.3657 | 2026-02-24 06:14:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2d99420-cc38-3be6-badd-e472626b7774 | 1.93209 | -60.36011 | 2026-02-24 06:14:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0eb4188c-6349-30d3-8a7b-acd435df6d99 | 1.93893 | -60.36372 | 2026-02-24 06:14:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 500579ca-27c2-3cb8-a92c-ecdec3b8bf1d | 1.94649 | -60.3717 | 2026-02-24 06:14:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2faf8b71-a5b5-3d07-9399-7d36f1b51a0b | 1.9435 | -60.35361 | 2026-02-24 06:14:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c4f2dd00-9c53-39e0-b560-943b9475e6a6 | 1.95182 | -60.36619 | 2026-02-24 06:14:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c4b56e73-94aa-3bbb-88eb-3ddd1559bb4c | 1.93285 | -60.3647 | 2026-02-24 06:14:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ee5c17c0-acad-33b3-8723-bb3c7cd52fac | 1.93818 | -60.35917 | 2026-02-24 06:14:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3d1f9937-dac0-3329-abe5-9114b7e1db74 | 1.1057 | -59.59828 | 2026-02-24 06:14:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 47d3dcc2-4665-3670-84fd-5fd123d19d5f | 1.92223 | -60.37582 | 2026-02-24 06:14:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| caee88ce-bded-3004-9554-25518cbd38d7 | 1.9419 | -60.3637 | 2026-02-24 06:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 51.8 |
| c1ed4e6f-436f-37ee-8e08-dbe01d2ad8b2 | 1.9419 | -60.3637 | 2026-02-24 06:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 48.2 |
| e615699f-3d42-37de-9a7e-cd335eb9db21 | 1.9419 | -60.3637 | 2026-02-24 06:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 20f7a286-a9bc-3a72-9920-88217336e52f | 1.9419 | -60.3637 | 2026-02-24 06:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 6fe8871a-ee8a-3abb-8e29-ab4b399c0ea9 | 1.9419 | -60.3637 | 2026-02-24 07:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 538dde2e-26a6-3c80-be1a-da5c2e517a32 | 2.7118 | -60.21681 | 2026-02-24 07:01:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| af08755a-5925-36b9-becf-d9073dc90591 | 1.93343 | -60.35964 | 2026-02-24 07:01:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 14.3 |
| ec9fd1a8-1440-3a32-b6db-7608bebe8bea | 1.94324 | -60.36508 | 2026-02-24 07:01:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 9a9a05de-b0ca-38bc-80da-140eaa2f921a | 1.95171 | -60.35114 | 2026-02-24 07:01:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 11.5 |
| bd7c6b06-b299-396e-831f-678fd71338a1 | 1.94145 | -60.35277 | 2026-02-24 07:01:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 26.4 |
| b251b503-c06e-3d7c-9592-e1f13b114098 | 1.95353 | -60.36359 | 2026-02-24 07:01:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.8 |


[Clique aqui para ver as próximas entradas](README6.md)
