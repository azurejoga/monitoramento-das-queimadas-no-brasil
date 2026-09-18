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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa585054-b0ea-3877-97af-f0848bc7fe4a | -19.17377 | -48.77514 | 2026-09-18 03:40:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 1e07e300-02f7-3747-b373-aae738098f34 | -21.0493 | -48.4682 | 2026-09-18 03:40:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 61f38e3a-e238-3432-b742-cbfa39dec953 | -21.04803 | -48.47351 | 2026-09-18 03:40:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0c1a762b-1afc-3e0d-9796-53d88661a0bf | -17.77197 | -46.48118 | 2026-09-18 03:40:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b1152880-e9c7-3846-b402-33ea7f116f22 | -19.55335 | -47.63802 | 2026-09-18 03:40:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8f60d577-25c5-35f6-bf3a-f3b2d56a3f82 | -17.76986 | -46.48211 | 2026-09-18 03:40:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 94af477c-9cee-37ec-bf46-d86dd1ec9d7c | -19.18915 | -48.79857 | 2026-09-18 03:40:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 6be4039d-7283-348d-bdcb-f5af99e2e745 | -17.77092 | -46.48585 | 2026-09-18 03:40:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1899cdaa-4302-35b8-9dca-bf4abb194ff4 | -19.18253 | -48.79692 | 2026-09-18 03:40:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 7660997c-412d-3a36-a841-f743f8523c54 | -19.18838 | -48.77264 | 2026-09-18 03:40:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cb453817-7b92-3134-9b6a-e520a43d72fd | -17.83068 | -44.85109 | 2026-09-18 03:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 380dee33-abe9-366d-ba43-f5da201d5896 | -19.18641 | -48.79555 | 2026-09-18 03:40:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 529823ee-a4c9-3fba-a4bb-db4d607c0250 | -19.17226 | -48.78138 | 2026-09-18 03:40:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 24.1 |
| e707e556-1d35-30f4-88d8-cf73f8935bce | -21.46 | -48.68412 | 2026-09-18 03:40:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cd4485ec-18a3-35d2-914e-dcf2ba11fb4b | -19.18267 | -48.78161 | 2026-09-18 03:40:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 3e13ec3a-1f8b-3969-9e01-d18ef37ddbee | -28.18589 | -50.08554 | 2026-09-18 03:42:00 | NOAA-20 | SÃO JOAQUIM | SANTA CATARINA | Brasil | 4216503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d1be753d-678a-3e40-8829-75c7840be8de | -19.2009 | -48.7904 | 2026-09-18 03:50:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 064f0045-b70d-330a-b601-d4e35e25473d | -13.2252 | -42.3414 | 2026-09-18 03:50:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 105.0 |
| 61c41970-fd73-3844-81ea-90bb9b964377 | -9.699 | -54.8176 | 2026-09-18 03:50:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 5143051b-71ae-3ca8-81e1-d303b1490d11 | -13.2446 | -42.3377 | 2026-09-18 03:50:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 144.6 |
| 9103273a-ce9f-36bd-a248-07042c0f1c1d | -9.7179 | -54.796 | 2026-09-18 03:50:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 70ed4338-3f77-35bd-af21-993e77ed791c | -19.2818 | -50.3753 | 2026-09-18 03:50:00 | GOES-19 | UNIÃO DE MINAS | MINAS GERAIS | Brasil | 3170438 | 31 | 33 | nan | nan | nan | Cerrado | 88.9 |
| ab7e3820-e042-3eaf-aff0-b5c275866b18 | -13.2257 | -42.317 | 2026-09-18 03:50:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 67.3 |
| 4de17e82-f21e-3c71-b18a-6945d259ed36 | -8.8922 | -62.4107 | 2026-09-18 03:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 61.9 |
| b80bc3ff-c314-3163-a316-dd17796403ca | -9.7177 | -54.8162 | 2026-09-18 03:50:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 413bb5c5-6910-3ca3-915f-4f3b6af49cb2 | -10.6536 | -50.4778 | 2026-09-18 03:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 0752de64-2af9-3586-ae2e-0be446890d69 | -19.1812 | -48.7717 | 2026-09-18 03:50:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 39e020fa-069e-3d44-9267-649427a20d34 | -10.4057 | -46.6158 | 2026-09-18 03:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 3bc8f9fd-1aab-3876-affe-a839d2367422 | -19.1806 | -48.7946 | 2026-09-18 03:50:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 8c66e4c5-397a-3000-ab90-dbe9cf89d1b5 | -8.8921 | -62.4297 | 2026-09-18 03:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 2f14b092-73db-33da-a774-d4968d0aa3a4 | -8.9107 | -62.41 | 2026-09-18 03:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 24814241-ac0c-31c7-853d-75fcbf1b29ce | -13.2451 | -42.3133 | 2026-09-18 03:50:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 90.1 |
| ef959ffe-1100-3b93-9aef-98608d89fad0 | -19.2015 | -48.7675 | 2026-09-18 03:50:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 64.1 |
| bdec6d4b-f9d7-3374-95f6-5c093e59824f | -19.2824 | -50.3529 | 2026-09-18 03:50:00 | GOES-19 | UNIÃO DE MINAS | MINAS GERAIS | Brasil | 3170438 | 31 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 06a5c143-1bf1-37b2-aec5-00a151ba6d19 | -19.2818 | -50.3753 | 2026-09-18 04:00:00 | GOES-19 | UNIÃO DE MINAS | MINAS GERAIS | Brasil | 3170438 | 31 | 33 | nan | nan | nan | Cerrado | 169.1 |
| cb014ac4-e0bd-3c2b-8859-bf3684fc7114 | -8.9107 | -62.41 | 2026-09-18 04:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 540fceda-a43a-3295-abf4-6c8ccd28dbea | -9.699 | -54.8176 | 2026-09-18 04:00:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| f753951e-e22f-3dc2-a049-f7db9e74a958 | -19.3026 | -50.349 | 2026-09-18 04:00:00 | GOES-19 | UNIÃO DE MINAS | MINAS GERAIS | Brasil | 3170438 | 31 | 33 | nan | nan | nan | Cerrado | 65.6 |
| d6a8568d-dedd-3e13-8095-0a279ff1b643 | -19.1812 | -48.7717 | 2026-09-18 04:00:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 434f02a8-5b55-3a32-826a-5c5dec6d79f2 | -9.7177 | -54.8162 | 2026-09-18 04:00:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 8c7e22b3-b8bc-3b08-8a19-9b0f1d3f390f | -8.8922 | -62.4107 | 2026-09-18 04:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 2d3e07c3-9e8c-3297-863a-1f2869f64595 | -8.8921 | -62.4297 | 2026-09-18 04:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 82c09a93-ca97-31fa-b863-cc39d8b9318e | -19.2824 | -50.3529 | 2026-09-18 04:00:00 | GOES-19 | UNIÃO DE MINAS | MINAS GERAIS | Brasil | 3170438 | 31 | 33 | nan | nan | nan | Cerrado | 120.1 |
| a628edc1-203f-3c29-ba13-0c62b1ee7fc0 | -19.1806 | -48.7946 | 2026-09-18 04:00:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 612115f5-1dc6-3c57-abf5-47ba5ac0fa28 | -19.2009 | -48.7904 | 2026-09-18 04:00:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 41cf4a2d-785a-30e4-9006-d76d90300960 | -11.6798 | -54.446 | 2026-09-18 04:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 1b8a1e41-1f0c-366f-8e11-5934b3889501 | -19.302 | -50.3714 | 2026-09-18 04:00:00 | GOES-19 | UNIÃO DE MINAS | MINAS GERAIS | Brasil | 3170438 | 31 | 33 | nan | nan | nan | Cerrado | 78.6 |
| a878aac9-78e1-3cf5-af8f-31de784e3939 | -19.2015 | -48.7675 | 2026-09-18 04:00:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 380b7ece-a7d2-3a83-a217-5f3337e991f7 | -8.9107 | -62.41 | 2026-09-18 04:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.3 |
| bad8f694-bab9-3a9a-bb12-30e7fae73c7a | -9.7177 | -54.8162 | 2026-09-18 04:10:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 102.5 |
| c9fc6b78-90ec-3da9-a4cb-9c941fc51ca0 | -9.699 | -54.8176 | 2026-09-18 04:10:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| a4dad0d3-61d3-3b83-900e-97941bd55ba6 | -8.8921 | -62.4297 | 2026-09-18 04:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 0a1e9c19-a34e-3638-aee5-1b2d81133840 | -8.8922 | -62.4107 | 2026-09-18 04:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 60c680a6-dd77-3c72-91f3-d9887fbceef3 | -12.663 | -54.7193 | 2026-09-18 04:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 913d09f1-e0ae-3ad8-98fc-50f06f1067ce | -19.2009 | -48.7904 | 2026-09-18 04:10:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 76bf1322-a5be-38ad-b936-ff6a2307dce1 | -12.6633 | -54.6988 | 2026-09-18 04:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 35fea9ec-bd16-319f-8e75-84875802dde2 | -12.6442 | -54.7007 | 2026-09-18 04:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| c13b0d83-5601-355b-a42b-91976ccc23e1 | -19.2015 | -48.7675 | 2026-09-18 04:10:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 5ee295ca-d9bf-3fc0-9494-620352569276 | -19.1812 | -48.7717 | 2026-09-18 04:10:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 89.2 |
| bbb54947-623b-3b13-b0a9-46217bf48816 | -12.644 | -54.7212 | 2026-09-18 04:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 40e3a0c6-f58c-39c1-a0a9-75f974aa94c2 | -19.1806 | -48.7946 | 2026-09-18 04:10:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 8ebe017c-0b97-376b-8667-22b5f78e3c3e | -11.6798 | -54.446 | 2026-09-18 04:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 87.4 |
| ecb213f8-e844-3ec1-9f00-725a08ef630c | 1.33574 | -50.60339 | 2026-09-18 04:17:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0757c287-78a5-3948-957b-c5bae9da6ceb | 1.23419 | -50.9276 | 2026-09-18 04:17:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a53b2a1d-be50-38f7-9ea9-57e17d8a59cc | 1.25048 | -50.7785 | 2026-09-18 04:17:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14867640-98d1-3741-b48c-b7358d24b547 | 1.24949 | -50.77542 | 2026-09-18 04:17:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef8d802e-dc86-35bd-9f11-1b36a911577a | 1.28401 | -50.87321 | 2026-09-18 04:17:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2f99525-f563-314b-b022-6e64d85a0f22 | 1.33097 | -50.6041 | 2026-09-18 04:17:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 61294b0b-2596-38ec-909d-6ab7e9c962e6 | 1.33596 | -50.60103 | 2026-09-18 04:17:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 038b32fe-b440-3c57-a354-513a7b072c25 | 1.20466 | -50.76909 | 2026-09-18 04:17:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ba2ce9a-41e8-33b5-af31-cac79e99d5a6 | 1.33196 | -50.60688 | 2026-09-18 04:17:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 23863d5a-a5eb-3178-b77e-887c655b8870 | 4.00724 | -51.64819 | 2026-09-18 04:17:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e58b66b-6ee1-3555-af2a-dbf924d84023 | 1.33273 | -50.61201 | 2026-09-18 04:17:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 10bdf5f2-c995-3ea1-8d43-c5d4f2973269 | 1.33178 | -50.60922 | 2026-09-18 04:17:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1cafc7a2-d54f-3f6f-bbaf-a835a6c5a3e3 | -2.81983 | -50.486 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b63832a-d7e6-33c7-91f4-26789d7aac01 | -4.88498 | -56.07443 | 2026-09-18 04:19:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a932280b-a6ab-34a0-ad2c-3b507ca5108e | -2.56349 | -54.74415 | 2026-09-18 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ddd733c6-1d0f-3d3a-9300-d25f7850100f | -5.57892 | -42.73589 | 2026-09-18 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e556cc77-a30e-3d60-8053-3735e1859b8f | -4.40948 | -42.31089 | 2026-09-18 04:19:00 | NOAA-21 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4c62d331-cf45-311b-a0ac-6dc5124284b0 | -6.94559 | -43.11057 | 2026-09-18 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 560f0ad3-259c-3551-9456-506ad2a0ed07 | -7.05996 | -42.12901 | 2026-09-18 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 53b81164-6c69-3a48-be8e-1a5694a4b788 | -7.07096 | -43.58068 | 2026-09-18 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df282286-4a48-3a22-b02b-5de29fa96b3c | -6.99795 | -42.15755 | 2026-09-18 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5cae2533-e012-3a79-8734-43f292265309 | -6.78189 | -47.86513 | 2026-09-18 04:19:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d118a3f0-0a06-34ce-b897-7fe995ad55c1 | -7.82266 | -45.10276 | 2026-09-18 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92276945-b9a9-3f9b-b86b-881bb113221a | -6.38258 | -43.86127 | 2026-09-18 04:19:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b762405-e86e-33cc-a9f1-7dd764825d88 | -3.03657 | -51.37343 | 2026-09-18 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| e02cf265-d5e8-3d8e-9b26-cd95959869ed | -6.42195 | -46.20111 | 2026-09-18 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83530db8-46da-345d-8f9b-73659e38b3f9 | -6.66815 | -43.64055 | 2026-09-18 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed1e6baa-3609-3d40-babb-3bdb83ddb8c0 | -6.025 | -51.80823 | 2026-09-18 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eb7c18cd-721a-3bd9-950c-383bd0601048 | -7.29093 | -38.96315 | 2026-09-18 04:19:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 8f8c6f0e-16f8-32f6-85a7-62545f9827a0 | -7.79506 | -44.88557 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2fef65bb-c633-3d47-a988-a94436bf988a | -7.12472 | -42.08509 | 2026-09-18 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e9b331da-ad1c-36d2-809d-e6f7dddce419 | -4.50539 | -54.97824 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48ada4d2-0821-3db5-9096-c5f55e0d4f38 | -5.62064 | -40.86406 | 2026-09-18 04:19:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 841c98ce-4970-3eff-bdd2-634b638f8d68 | -7.14872 | -42.16739 | 2026-09-18 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 12d477d8-6334-3d16-bb8e-2d5629292e75 | -4.95841 | -45.14455 | 2026-09-18 04:19:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7469627f-0ba2-3087-ae0c-6025a42b9c9b | -3.36843 | -50.44754 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| aa6536ae-dae0-311d-9532-d908d6ffd26b | -7.58845 | -44.94498 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 957bd632-66da-3d4a-b4b0-af9dd7c6590d | -5.75644 | -45.0904 | 2026-09-18 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |


[Clique aqui para ver as próximas entradas](README30.md)
