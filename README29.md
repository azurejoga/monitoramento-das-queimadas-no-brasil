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
| 3b33ed72-7a77-3fdc-a639-d748c4d41df7 | -9.48446 | -48.17376 | 2026-09-12 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 558f97b6-7996-340a-92f4-0ff9889c3437 | -12.64341 | -47.09491 | 2026-09-12 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5b9d752e-591c-37b3-a5e7-74c03d5ccff0 | -12.13829 | -48.97286 | 2026-09-12 04:34:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cc5943f6-6548-310b-941e-9e59d4d65203 | -10.7121 | -46.06259 | 2026-09-12 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 401182cc-ec99-3075-b920-e1b11d1d2fd4 | -12.208 | -49.39808 | 2026-09-12 04:34:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6068d008-00b3-30c0-8d47-1d0f5177755b | -4.86434 | -56.00322 | 2026-09-12 04:34:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6a82628-3f69-343f-93aa-909155ad114c | -16.75808 | -50.00428 | 2026-09-12 04:36:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18e01b8d-ad3e-3944-97c2-e8fd90a8c968 | -15.13492 | -48.17238 | 2026-09-12 04:36:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0453eae3-973c-30a5-8dad-f1aded53870e | -14.58747 | -52.66134 | 2026-09-12 04:36:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0f26f352-84ec-3663-af0a-55ccc5162479 | -14.80331 | -48.79025 | 2026-09-12 04:36:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 73a8d827-0127-3cd4-937d-f3b3d9383fd9 | -19.27365 | -46.84323 | 2026-09-12 04:36:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c2219ed-92fb-3765-9a96-cec8f89dce32 | -17.71565 | -42.35046 | 2026-09-12 04:36:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e8ffa791-b64e-3c4d-921a-69e66ba4671b | -18.65877 | -41.99295 | 2026-09-12 04:36:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| dc9f0a39-f4e6-355d-b64b-ea8b9753ff68 | -13.33046 | -51.65498 | 2026-09-12 04:36:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eea6d331-f1bf-3659-a609-05c85b56a118 | -18.61876 | -46.32027 | 2026-09-12 04:36:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e1465d4e-47b0-37ef-813b-f03f440019c2 | -14.57624 | -52.66347 | 2026-09-12 04:36:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1a74abd7-73de-33d2-abb5-8ff63eac7a55 | -14.58119 | -48.84394 | 2026-09-12 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9f2755b-4f1f-3b31-aec9-a2ec8d757a94 | -17.10965 | -51.25305 | 2026-09-12 04:36:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 62dc358e-ceb4-3e43-ba6e-5c5431c70845 | -16.63479 | -52.82383 | 2026-09-12 04:36:00 | NOAA-21 | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 55fb1acb-6b33-3fe1-a6a6-ce641454f307 | -18.6595 | -41.98611 | 2026-09-12 04:36:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 860442b2-f257-3ac9-bc91-4470d19fc855 | -13.4596 | -48.50844 | 2026-09-12 04:36:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cd2404ea-8905-32a5-b2ce-450362c13e14 | -16.63412 | -52.82783 | 2026-09-12 04:36:00 | NOAA-21 | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d5a22abf-c29e-331d-a5d0-e355e6b2b517 | -18.93695 | -46.82315 | 2026-09-12 04:36:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 42885336-2291-3afc-848c-96823f92eb09 | -18.86443 | -44.08067 | 2026-09-12 04:36:00 | NOAA-21 | PRESIDENTE JUSCELINO | MINAS GERAIS | Brasil | 3153202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 989a2e51-3cd5-3ffa-97f1-801d8bf2af91 | -18.64628 | -47.29314 | 2026-09-12 04:36:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a9f90c5d-3425-32ed-b93f-7e0653186668 | -15.50914 | -45.88643 | 2026-09-12 04:36:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b92b438e-e046-30bf-9f8c-788d339cbcb3 | -14.58753 | -48.84154 | 2026-09-12 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e44ff750-e9eb-3762-afc9-2cdb4b03cc0f | -18.94007 | -46.82854 | 2026-09-12 04:36:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e63ccd36-7f97-332e-aa75-8e08dc5285ed | -19.74257 | -46.04202 | 2026-09-12 04:36:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e03387c-c191-3159-9177-ba54f279a162 | -13.35353 | -51.7729 | 2026-09-12 04:36:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3e83594-3711-344e-993e-a1ed9d176f1f | -18.48268 | -51.71183 | 2026-09-12 04:36:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08cc3178-238a-3860-9150-da2f88ffeff9 | -16.03051 | -52.65443 | 2026-09-12 04:36:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4da11b8-4ec5-3c6b-aa78-20ab13f7d584 | -13.61869 | -47.90803 | 2026-09-12 04:36:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 89f9874e-4805-3bab-bf82-d67b0bd16a9c | -18.93632 | -46.82793 | 2026-09-12 04:36:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9ea5d63f-93a6-35bb-b7ac-6d1bce30a67d | -13.72612 | -51.83501 | 2026-09-12 04:36:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7a9d563-65f2-37d5-b5c0-98a0e457926f | -13.46402 | -48.5018 | 2026-09-12 04:36:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5a33f2e-5c4d-3d30-8961-33a5a3fa523f | -16.0309 | -47.90417 | 2026-09-12 04:36:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b9ea6cd0-0e67-3cdd-85d0-4905f6e9639b | -14.57976 | -52.66409 | 2026-09-12 04:36:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a672aa52-6d3d-3d0e-a30b-0f51bcc35388 | -13.82526 | -53.93776 | 2026-09-12 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 935171d7-03ef-3e31-b815-96349a377f0a | -18.99002 | -46.26862 | 2026-09-12 04:36:00 | NOAA-21 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7440310a-56e7-3d31-8003-7cd714cc413a | -14.58563 | -48.83723 | 2026-09-12 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e8e1d7fb-7364-3aa6-a44b-88eb0c1739b6 | -16.04091 | -52.65631 | 2026-09-12 04:36:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6c1b9775-45dc-39a5-aac7-76a9ae89d589 | -16.91288 | -48.84329 | 2026-09-12 04:36:00 | NOAA-21 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 58796873-8da8-39aa-8f15-db2582946703 | -16.73745 | -52.31155 | 2026-09-12 04:36:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 47f40c63-5160-3c41-9dda-44b4f41d22f1 | -13.37437 | -48.01913 | 2026-09-12 04:36:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 766982ce-e106-3240-876f-666f49400997 | -13.36029 | -48.02067 | 2026-09-12 04:36:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 320fe2a7-ae2f-3596-8290-114620fd8d2e | -18.48524 | -51.67451 | 2026-09-12 04:36:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0582abb-5e4e-334d-a002-5c1ef04ee531 | -14.58612 | -52.66942 | 2026-09-12 04:36:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f7c0c1f-cf7d-3946-8776-7f8657632949 | -14.5868 | -52.66537 | 2026-09-12 04:36:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a355987d-e2de-32d4-b80d-a244c2e4ea68 | -16.02917 | -52.6625 | 2026-09-12 04:36:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0de159c9-cc43-3d4d-bef8-ba7554e081d5 | -16.63132 | -52.8232 | 2026-09-12 04:36:00 | NOAA-21 | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4068dfd5-86fe-302e-9358-6620c34c0467 | -16.02782 | -52.6706 | 2026-09-12 04:36:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e7a0fb4-bd4c-328c-ac65-8e2d67ab2629 | -15.44497 | -41.38556 | 2026-09-12 04:36:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| efa6a1ce-c70b-36f5-93bb-8acf1d0cf42e | -17.5317 | -45.35052 | 2026-09-12 04:36:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ada8c740-e3cf-3b54-aa19-03b3986634e6 | -17.82387 | -44.5434 | 2026-09-12 04:36:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20f40959-5892-3e33-a038-00882eaa43ff | -18.95282 | -43.02607 | 2026-09-12 04:36:00 | NOAA-21 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c625fc20-b1ad-345a-a11a-ea680a2668db | -13.37382 | -48.02277 | 2026-09-12 04:36:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d7015e7f-9e3b-3817-8713-752b3f7098f2 | -16.01209 | -52.70065 | 2026-09-12 04:36:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0758c75-c2b1-35cb-8246-824896bc46dd | -14.98217 | -53.95805 | 2026-09-12 04:36:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d61d1925-bdcb-3b8b-b83b-dd50963836b1 | -18.94383 | -46.82913 | 2026-09-12 04:36:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 863b21cf-e6d0-3557-a39d-6fa3b0792880 | -20.38115 | -40.59657 | 2026-09-12 04:36:00 | NOAA-21 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 99f5b66d-b93e-3971-b803-afa240924d95 | -18.88868 | -46.84003 | 2026-09-12 04:36:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 074c57c0-44b2-3743-bb84-90df3c2ebd46 | -16.52596 | -48.73378 | 2026-09-12 04:36:00 | NOAA-21 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7057fe7d-237b-3526-a588-756b339aadca | -13.32983 | -51.65882 | 2026-09-12 04:36:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3b309e99-ec6d-32fd-a6da-aa678cd779d2 | -15.32163 | -47.25036 | 2026-09-12 04:36:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6840d95e-1a96-3146-9fd5-723fc4632238 | -14.83747 | -48.17098 | 2026-09-12 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5981212-d7a4-30e7-b6c6-fa15a4897f42 | -16.01623 | -52.69734 | 2026-09-12 04:36:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca917fba-70a0-3006-9a87-47df23af9058 | -13.48129 | -48.50079 | 2026-09-12 04:36:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 91e83bcd-5618-3c68-ab24-279d91093e7f | -14.58395 | -52.6607 | 2026-09-12 04:36:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a35ba03e-89b4-3f76-9409-597ca5bd2948 | -14.58808 | -48.83788 | 2026-09-12 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 89481f05-419e-386a-a781-a42664a223a5 | -13.69829 | -49.89453 | 2026-09-12 04:36:00 | NOAA-21 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7732492-d73e-394b-ae84-a12dded3b6b3 | -18.41398 | -46.05767 | 2026-09-12 04:36:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 031840a0-cbcf-3ab1-8ded-d9e5b7053691 | -18.65914 | -41.98952 | 2026-09-12 04:36:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e938d83e-40fe-3c32-8d5e-3cf2db28ee3b | -13.37263 | -48.00766 | 2026-09-12 04:36:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0259084c-99f8-39ff-8018-f4e9795bbb15 | -18.73661 | -45.02478 | 2026-09-12 04:36:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 03027712-748e-3331-b4fc-01092a56802b | -14.39092 | -43.78975 | 2026-09-12 04:36:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d3623583-daff-334f-b370-c44c6c60cfa6 | -13.73534 | -48.97456 | 2026-09-12 04:36:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 44bec7bb-d2c5-39f5-a1de-f358b333c935 | -16.926 | -49.66197 | 2026-09-12 04:36:00 | NOAA-21 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 344b5780-b5cd-39d6-8951-1fbdff079d61 | -13.35973 | -48.02438 | 2026-09-12 04:36:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 421a4f93-4ce1-35b3-95b9-e0e80a7cbd9e | -14.91249 | -44.67519 | 2026-09-12 04:36:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8e4aebc7-a7c8-32bd-845d-1ea47fa4d013 | -16.03196 | -52.66718 | 2026-09-12 04:36:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14f44ded-91ac-3efb-85f0-c2c0319004b6 | -14.11903 | -44.21696 | 2026-09-12 04:36:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 347fefde-12d9-3241-b816-11703ee99dee | -13.46014 | -48.50488 | 2026-09-12 04:36:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3ad52f71-1cc3-35f5-9d80-9b05945c3bf7 | -16.51001 | -43.79686 | 2026-09-12 04:36:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e133daac-c621-3dd8-ba24-9cb90a6229a2 | -18.66753 | -42.00782 | 2026-09-12 04:36:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 5c6dda13-9f25-365f-a450-6dcc19365770 | -19.74063 | -46.04265 | 2026-09-12 04:36:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c6cd3ea-9829-3b8c-b07b-2fef3552179a | -15.61631 | -48.2546 | 2026-09-12 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52b2ab67-b274-3eb4-acf6-00132f4d0d82 | -16.33862 | -43.44135 | 2026-09-12 04:36:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6d05f97d-ee85-3297-8e18-0d3439afe227 | -14.67975 | -42.85077 | 2026-09-12 04:36:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e3a28205-e158-3121-b074-894239369497 | -13.37829 | -48.01605 | 2026-09-12 04:36:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 012e1596-ed5b-325b-aa82-60869c1aa718 | -18.62066 | -46.31775 | 2026-09-12 04:36:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec9e995a-7f49-33d1-ac6f-743c5121dd21 | -14.58229 | -48.83667 | 2026-09-12 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6b0e375f-10c6-3f93-975d-3b356617d755 | -17.71383 | -42.3505 | 2026-09-12 04:36:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 18037416-234d-3b6b-9fa8-d01a29259a07 | -15.2505 | -53.89015 | 2026-09-12 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6012de0-d835-3219-b0de-7b537e7a5c73 | -14.58174 | -48.8403 | 2026-09-12 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62d443f0-8250-373f-9f81-6068f14f60cc | -14.07092 | -45.61818 | 2026-09-12 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9523c2fd-b06b-32ad-b9ad-b504f337e273 | -19.77182 | -43.97343 | 2026-09-12 04:36:00 | NOAA-21 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4b0aa60-0aa9-3fac-a971-435136d3eb1d | -18.88768 | -46.84216 | 2026-09-12 04:36:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c4a714a4-9f21-3a83-ae3a-b971df66a83c | -18.87766 | -46.98199 | 2026-09-12 04:36:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 0e1372e8-51ba-310a-aeff-46b9a52525c6 | -17.38174 | -48.24796 | 2026-09-12 04:36:00 | NOAA-21 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README30.md)
