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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ebdcdf4-ed31-321d-a871-a56261564d0d | -22.36209 | -49.28233 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 51a26afd-cfbc-304d-a2a0-2fbde855f631 | -22.36172 | -49.30721 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 055f4a96-32f7-3e12-b83a-ef11bd36a124 | -22.36131 | -49.33225 | 2024-10-02 03:57:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 040c2632-34e1-3070-8ef0-04efe923c7ae | -22.36073 | -49.31202 | 2024-10-02 03:57:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 5d8fff49-65d9-3d94-a4bf-1bf5dfa8f097 | -22.36016 | -49.29181 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 6a028187-0b13-33c4-92fc-674728b8ed1e | -22.35921 | -49.29647 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 42.0 |
| c2050aee-9e42-3c80-8de8-a295d333631a | -22.35822 | -49.30128 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 42.0 |
| 2edf163e-d07d-348f-8ddb-f8ba2d77830b | -22.35776 | -49.32659 | 2024-10-02 03:57:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| d2f53a4d-ba61-3b73-b1c2-1f8d87c9773c | -22.35724 | -49.30611 | 2024-10-02 03:57:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| d2fa529d-4674-31b5-b982-6e0dba457515 | -22.35679 | -49.33136 | 2024-10-02 03:57:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| c38e0727-188a-35ca-9a0b-4604c08dbbe9 | -22.35624 | -49.31101 | 2024-10-02 03:57:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 7ff450e7-9388-3799-9300-43bd3b5ecd20 | -22.35582 | -49.33612 | 2024-10-02 03:57:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| e5d004e0-5c8e-35d1-9342-0b8ac88e5799 | -22.35474 | -49.29536 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 42.0 |
| 6d13df19-895d-3227-a69b-6b0f91631028 | -22.35375 | -49.30017 | 2024-10-02 03:57:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 42.0 |
| 81af86d0-700f-35fa-ad48-2f8a99dfcf5d | -22.35323 | -49.32573 | 2024-10-02 03:57:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b778360d-9964-3f03-a3bb-c5028504d00e | -22.35275 | -49.30507 | 2024-10-02 03:57:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 999bf15f-019f-31a5-8ef6-42ddad734fbb | -22.35226 | -49.3305 | 2024-10-02 03:57:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 051bab14-7bf6-3e67-9e65-cf70c5aac6e4 | -20.94746 | -49.11376 | 2024-10-02 03:57:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 69820347-13ad-31e5-bcc9-c3d800874807 | -20.94291 | -49.11274 | 2024-10-02 03:57:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ae57e6a2-add7-3837-9f94-2cc02c7a9eb1 | -22.60218 | -48.77043 | 2024-10-02 03:57:00 | NOAA-20 | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c3f76abc-ad43-3ec4-aee5-3e2759be7611 | -22.6013 | -48.77486 | 2024-10-02 03:57:00 | NOAA-20 | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5b871003-f63e-386f-b64b-436060581ad0 | -23.17135 | -49.60186 | 2024-10-02 03:57:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| e184fe40-c3b1-3643-a773-fff5417afa56 | -23.16799 | -49.59528 | 2024-10-02 03:57:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 6d987351-b893-30bc-b2cd-57d7a6c668fe | -23.16692 | -49.6005 | 2024-10-02 03:57:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 0b472b1c-7bd8-3d0f-bd24-6207a65064d9 | -23.16244 | -49.59934 | 2024-10-02 03:57:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e30b8702-846e-3a2f-b1b8-0bf2a0a57d30 | -22.9987 | -49.60794 | 2024-10-02 03:57:00 | NOAA-20 | IPAUSSU | SÃO PAULO | Brasil | 3520905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| f3e39d6d-1720-3f72-a675-ccbb711381fc | -22.40164 | -49.66959 | 2024-10-02 03:57:00 | NOAA-20 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e144ac12-c826-38cf-af56-53dc4e7ce7fc | -25.03131 | -50.72042 | 2024-10-02 03:57:00 | NOAA-20 | IVAÍ | PARANÁ | Brasil | 4111407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 409222cf-9371-3a6c-851a-6c49da85ba45 | -25.03016 | -50.72583 | 2024-10-02 03:57:00 | NOAA-20 | IVAÍ | PARANÁ | Brasil | 4111407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 69eb0ab6-b7b9-32a0-becc-0d5116fd3a96 | -25.02666 | -50.7193 | 2024-10-02 03:57:00 | NOAA-20 | IVAÍ | PARANÁ | Brasil | 4111407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 6e8a3a49-4e6a-3349-9c48-6e61c31c49c5 | -24.60224 | -49.31992 | 2024-10-02 03:57:00 | NOAA-20 | DOUTOR ULYSSES | PARANÁ | Brasil | 4128633 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c5b3215b-3115-3166-a3dd-846ae7597e68 | -24.60065 | -49.32117 | 2024-10-02 03:57:00 | NOAA-20 | DOUTOR ULYSSES | PARANÁ | Brasil | 4128633 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| b8c02c7e-c680-3786-8626-c67b93ee58cc | -25.82381 | -50.25696 | 2024-10-02 03:57:00 | NOAA-20 | SÃO JOÃO DO TRIUNFO | PARANÁ | Brasil | 4125100 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| eb8e2f43-26d3-388c-8671-16a5c63577d0 | -21.6354 | -50.79359 | 2024-10-02 03:57:00 | NOAA-20 | RINÓPOLIS | SÃO PAULO | Brasil | 3543808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 75a8e1ca-321e-3a94-ad3e-9040b0f5b580 | -21.63473 | -50.79678 | 2024-10-02 03:57:00 | NOAA-20 | RINÓPOLIS | SÃO PAULO | Brasil | 3543808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| c5206c86-c851-3dae-8e08-4e9bb771e9d4 | -21.62909 | -50.79862 | 2024-10-02 03:57:00 | NOAA-20 | OSVALDO CRUZ | SÃO PAULO | Brasil | 3534609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| c6e5e0c2-f190-35d8-9757-1defdc2b417d | -21.62845 | -50.80163 | 2024-10-02 03:57:00 | NOAA-20 | OSVALDO CRUZ | SÃO PAULO | Brasil | 3534609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| ddaa384d-5a20-34de-8d3f-5252b8744c78 | -21.62155 | -50.80938 | 2024-10-02 03:57:00 | NOAA-20 | OSVALDO CRUZ | SÃO PAULO | Brasil | 3534609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7f9941f7-e5c1-3137-8b88-69f4bcbf763d | -21.6209 | -50.81247 | 2024-10-02 03:57:00 | NOAA-20 | OSVALDO CRUZ | SÃO PAULO | Brasil | 3534609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 38188002-7fcd-36f5-8f0e-eb40b5225293 | -21.56068 | -50.7551 | 2024-10-02 03:57:00 | NOAA-20 | PIACATU | SÃO PAULO | Brasil | 3537701 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1242677e-d8a3-3715-9793-103002ef7349 | -21.56002 | -50.75825 | 2024-10-02 03:57:00 | NOAA-20 | PIACATU | SÃO PAULO | Brasil | 3537701 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 79deef8e-393d-3134-a7b2-ae1f148f05d2 | -21.55936 | -50.76141 | 2024-10-02 03:57:00 | NOAA-20 | PIACATU | SÃO PAULO | Brasil | 3537701 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2839fd4a-c8f8-3037-b48e-49e55d7f6eca | -21.55508 | -50.75682 | 2024-10-02 03:57:00 | NOAA-20 | PIACATU | SÃO PAULO | Brasil | 3537701 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| efdf4a87-2fdc-3a11-974d-1bcb128a21a3 | -21.55441 | -50.75999 | 2024-10-02 03:57:00 | NOAA-20 | PIACATU | SÃO PAULO | Brasil | 3537701 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6c4bb473-1c27-39eb-a34c-b77f5fdfc698 | -21.54944 | -50.75875 | 2024-10-02 03:57:00 | NOAA-20 | PIACATU | SÃO PAULO | Brasil | 3537701 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8fbe0a11-557d-3b93-9c0d-02b9b8bb8a56 | -21.54876 | -50.76196 | 2024-10-02 03:57:00 | NOAA-20 | PIACATU | SÃO PAULO | Brasil | 3537701 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b8b42978-b48d-3ca6-a82d-812ffbcedb53 | -23.53499 | -51.13389 | 2024-10-02 03:57:00 | NOAA-20 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 37604d60-274c-3287-9e8a-938d0f092292 | -23.53372 | -51.1398 | 2024-10-02 03:57:00 | NOAA-20 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b4053d02-4deb-3cc9-8fba-88ba570d5d08 | -23.5108 | -51.10245 | 2024-10-02 03:57:00 | NOAA-20 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 4823bc71-1516-3087-abb4-80a7030fc064 | -26.49434 | -51.65235 | 2024-10-02 03:57:00 | NOAA-20 | PALMAS | PARANÁ | Brasil | 4117602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5ccdbb11-3c07-3fc3-981b-002814de40cd | -26.48836 | -51.65673 | 2024-10-02 03:57:00 | NOAA-20 | PALMAS | PARANÁ | Brasil | 4117602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| da5a3082-c9b7-3fd8-9acf-3bfa21e17c11 | -25.61325 | -51.35203 | 2024-10-02 03:57:00 | NOAA-20 | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 85c833f9-e5bb-34b5-900c-412e30ff6ccc | -25.6121 | -51.35271 | 2024-10-02 03:57:00 | NOAA-20 | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| b2160599-5dd4-334b-859d-354a068bc535 | -20.79503 | -51.659 | 2024-10-02 03:57:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 6b04d87e-b398-3a53-b634-074a47e82954 | -20.66349 | -51.46527 | 2024-10-02 03:57:00 | NOAA-20 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4ca47828-24e8-3b63-acc5-1347765b8bd6 | -20.66272 | -51.46885 | 2024-10-02 03:57:00 | NOAA-20 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 237af7eb-5589-32b4-bf37-c850f19ffc21 | -20.66149 | -51.46354 | 2024-10-02 03:57:00 | NOAA-20 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f209e3e2-0f71-3417-95f8-d26ea51a411d | -20.6607 | -51.4671 | 2024-10-02 03:57:00 | NOAA-20 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 71505c8d-2915-3565-9b42-f85c12ddeaaa | -21.3456 | -55.6841 | 2024-10-02 03:57:04 | GOES-16 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 958ef04b-ee65-33f6-b894-155b7ab95800 | -21.3656 | -55.7022 | 2024-10-02 03:57:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 757fe4d6-66f8-3541-a28c-6ef0a164d7fe | -21.3661 | -55.6807 | 2024-10-02 03:57:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 95.3 |
| c97beb72-4fba-37af-ad68-3d2d7b53c469 | -22.37 | -49.34 | 2024-10-02 04:03:16 | MSG-03 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 30806390-34b4-30fc-86c0-0e6bba285f9a | -22.37 | -49.28 | 2024-10-02 04:03:16 | MSG-03 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7b2d06bd-69cb-330a-b04b-7c64d0aa363a | -9.9553 | -64.9172 | 2024-10-02 04:06:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.4 |
| fa25608c-e20d-3862-b22a-74bcbbc45526 | -9.9367 | -64.9179 | 2024-10-02 04:06:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 77.6 |
| cab35a11-8997-30fa-b946-f881049c5121 | -11.6931 | -64.9974 | 2024-10-02 04:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 97bcc82e-a932-3aff-87b2-71fae3bc61e5 | -11.6743 | -64.9983 | 2024-10-02 04:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 102.8 |
| e0079997-c2ba-3adf-b3c2-984ee7374d46 | -11.6742 | -65.0172 | 2024-10-02 04:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 260059e8-985f-3b9a-af4c-8cfaf32dbe4b | -11.6555 | -64.9991 | 2024-10-02 04:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 47.3 |
| d274753c-05ba-3822-a167-338ffc634995 | -11.6554 | -65.018 | 2024-10-02 04:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 5e5b8b4b-9298-3e5e-93e2-8f281dcf83e7 | -12.6486 | -63.1022 | 2024-10-02 04:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 7d654f33-48be-3b6f-bad7-80bf4446900f | -12.6484 | -63.1214 | 2024-10-02 04:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 67b0b34d-815f-39a7-b616-fc960b7bff34 | -12.8803 | -62.531 | 2024-10-02 04:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 95a3fd94-ef3e-3146-a1e1-7261f09f9435 | -12.8614 | -62.5321 | 2024-10-02 04:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 155.0 |
| 548b41a0-3eb6-32b3-9c7e-557b834963c2 | -12.8612 | -62.5514 | 2024-10-02 04:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 125.6 |
| 9c0cded1-fb8c-3b99-a87e-c4c0bd312f91 | -12.8424 | -62.5333 | 2024-10-02 04:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 38a46508-6846-3331-99d5-d988d8e25cd8 | -12.8423 | -62.5526 | 2024-10-02 04:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 123e8223-60b4-367b-b06f-15c41e74f2d0 | -13.0742 | -51.4163 | 2024-10-02 04:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 3a31d63e-7ded-377f-8dd7-e504735fd288 | -13.0553 | -51.3973 | 2024-10-02 04:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.3 |
| af14f2df-f812-3a0c-8450-02edc3b92659 | -13.055 | -51.4186 | 2024-10-02 04:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| f01888b0-962e-34e6-a847-c7cde6022667 | -13.2173 | -48.624 | 2024-10-02 04:06:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 42a6de85-38c7-36c7-b8b3-7dca741aa382 | -14.7986 | -48.7628 | 2024-10-02 04:06:29 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 5d4e5368-0558-3ee3-b45a-0702e0373f9f | -16.1094 | -53.5004 | 2024-10-02 04:06:36 | GOES-16 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| e38d694f-023c-3c79-bce6-163f459b76e1 | -16.109 | -53.5215 | 2024-10-02 04:06:36 | GOES-16 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 58f196ac-50d2-36e8-80a2-d4dfcc1254cb | -15.8936 | -57.155 | 2024-10-02 04:06:36 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 42bb5ede-1978-3ee0-aaa4-080355614fb8 | -15.8933 | -57.1754 | 2024-10-02 04:06:36 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 47.7 |
| a42dd03a-8b08-3ed7-8803-328b855a8d26 | -16.6127 | -57.217 | 2024-10-02 04:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.6 |
| e0bd02c9-00db-3536-a57e-e743b3e924b1 | -16.6124 | -57.2375 | 2024-10-02 04:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.7 |
| 6f2555f9-f12c-3891-ba61-bddecb111a34 | -16.514 | -57.2896 | 2024-10-02 04:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.1 |
| 02a0fa0c-3799-3800-9f96-6761780c816f | -16.5137 | -57.31 | 2024-10-02 04:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.8 |
| b1668815-19a5-3648-9981-d851929456bc | -16.4945 | -57.2918 | 2024-10-02 04:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.5 |
| 4320eb6b-4900-36a6-bc53-bf5839bf426f | -16.4942 | -57.3122 | 2024-10-02 04:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.4 |
| ef6c90e1-41fc-36ed-86d7-7bcda431fd7c | -16.475 | -57.294 | 2024-10-02 04:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.8 |
| e1219a39-3a23-357a-a2ef-dd51521c502e | -16.4746 | -57.3144 | 2024-10-02 04:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.9 |
| f4dfa176-c035-355d-a8f9-03aafcf5fa34 | -16.8096 | -55.9177 | 2024-10-02 04:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 72.4 |
| c3f0dff6-e964-3070-a7ac-a0185e68a5ec | -16.7265 | -57.4287 | 2024-10-02 04:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.2 |
| 2651740d-41d3-3674-81dc-64298004beb8 | -16.7108 | -57.1852 | 2024-10-02 04:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.6 |
| 8aac5054-249e-3aed-b128-7e3de9719f4b | -16.7063 | -57.4718 | 2024-10-02 04:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 38.9 |
| 8cc34d4d-5eb1-3f18-adae-0cd0b295dc1b | -16.6916 | -57.167 | 2024-10-02 04:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.3 |
| 256e37e4-4194-3fbb-9660-6b10d49a5148 | -16.6912 | -57.1875 | 2024-10-02 04:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 164.9 |


[Clique aqui para ver as próximas entradas](README80.md)
