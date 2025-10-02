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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d8ea332-b883-37fb-b532-0fe2637c9b42 | -12.50679 | -50.25238 | 2025-10-02 04:04:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ccda0659-dc3c-354f-9777-b0645e8ac564 | -14.36848 | -45.94827 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e333ee38-9d43-34a1-927e-836eab3b6a02 | -19.458 | -44.28032 | 2025-10-02 04:04:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 06a3d773-ae20-356b-82d8-94189d4ddb35 | -16.36565 | -47.07215 | 2025-10-02 04:04:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e34555ef-c8e5-3f98-87db-ef8466c35891 | -18.59179 | -44.51423 | 2025-10-02 04:04:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6a66539-fdbd-30a8-8fa7-fc5ddf795258 | -15.21153 | -47.9984 | 2025-10-02 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 3f0ad3ad-bac5-3272-b046-14aef89c6a99 | -16.00612 | -50.90522 | 2025-10-02 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1ebd88e3-581e-384e-8920-7d0613b7444b | -17.97984 | -45.01746 | 2025-10-02 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e7932f7c-96c1-3828-ac04-4d1eeb35b8e2 | -14.3647 | -45.96877 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6bcfca6c-1979-380a-ab38-9cd9ef148951 | -15.26159 | -49.30497 | 2025-10-02 04:04:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 85873f5f-8e8f-3072-b72a-a1bfb2b2d4db | -15.29649 | -46.38585 | 2025-10-02 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb633a3b-5c3d-341b-a135-753484ad5bef | -14.47263 | -48.39587 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 38fa12f4-2217-3643-bcf1-9650050add2b | -14.22266 | -44.93362 | 2025-10-02 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f720a948-41bb-3261-b2ff-0d11a809c473 | -14.69824 | -49.61249 | 2025-10-02 04:04:00 | NOAA-21 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 484021c0-d900-3c2b-991c-f69d4d44efd6 | -15.54975 | -48.17451 | 2025-10-02 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa68b447-934e-3aae-b500-a1dd49456824 | -13.95453 | -48.10247 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8e1a4fc6-74f5-37d4-9150-e29b8c193369 | -12.76323 | -50.55093 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 83a3f818-71ca-3d00-bc92-1b535f62a130 | -13.76299 | -48.68837 | 2025-10-02 04:04:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b6f9c04a-c6a0-3d66-9b86-03fa958e55f0 | -13.24025 | -48.5129 | 2025-10-02 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36fc89ae-1fab-30e2-b72f-c2ebca8b4ecb | -18.3438 | -42.40744 | 2025-10-02 04:04:00 | NOAA-21 | JOSÉ RAYDAN | MINAS GERAIS | Brasil | 3136553 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 735ce940-f2b0-3a15-98d1-97c014b1d393 | -13.95407 | -48.12965 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dee828ea-513b-342d-b682-9ac2c5e5bd66 | -14.48472 | -48.40533 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 721c07e2-e033-369b-8bc2-3d438eafbf73 | -15.11895 | -48.48941 | 2025-10-02 04:04:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a7f03733-b378-317b-88d9-d5bea8cf5140 | -13.05587 | -47.06373 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5728372-8dc5-33b8-9f6b-bdf64d2556a5 | -15.27886 | -49.31218 | 2025-10-02 04:04:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| abd4f5bb-42e8-393a-87ca-e609ad439bd2 | -17.09015 | -47.10972 | 2025-10-02 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d9a2a93-000f-3f11-afa7-51ea556c3022 | -13.57908 | -48.19487 | 2025-10-02 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33749343-30c4-3070-bac6-df6ead305e1f | -15.29007 | -46.39973 | 2025-10-02 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb8fbace-17df-31e3-9754-c90a15cb59b1 | -13.34293 | -47.33598 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b1fe2b51-99bb-32b9-8a7c-8ef2cc0efde2 | -19.0211 | -49.75065 | 2025-10-02 04:04:00 | NOAA-21 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9863c636-69db-31ab-a6b8-38d1cda144e6 | -14.44277 | -46.34344 | 2025-10-02 04:04:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 964ab26c-7131-3fc6-86ea-c300b6f4fd5e | -13.85913 | -51.25057 | 2025-10-02 04:04:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cf5b4c27-4a9d-31a7-bda1-d5fd81ff9bfc | -15.34923 | -47.08474 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 20.4 |
| a736745f-e0d4-3d1c-ac28-cdc4ad269428 | -13.31525 | -46.99557 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5639ebbf-ddf0-3e10-bdc3-62f845e0f9f8 | -13.12874 | -47.41562 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26cadce1-3940-3d91-8a86-ed64fa81430b | -14.49384 | -48.42921 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a1f4b79a-bc3c-3608-a2c7-f9e00e2b8235 | -16.03504 | -50.86456 | 2025-10-02 04:04:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed06c8d2-5d1e-33c6-a431-a1fb67188042 | -13.16512 | -47.83274 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5e0b8409-0ba6-3f5b-89ec-6f51c76a0479 | -16.04225 | -50.88076 | 2025-10-02 04:04:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12eb5b6e-9d56-3118-9add-860c9d9ad3da | -15.34838 | -46.26997 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9d58f12e-1b0b-3cd7-8200-f81929f3b480 | -14.40725 | -44.90037 | 2025-10-02 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2bb6d43a-516e-32ab-ac32-9e7511198624 | -14.41434 | -46.10875 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 320f290f-edf9-3815-bc23-7efd500dae1e | -12.94251 | -46.94494 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60665ed9-aa1b-39df-b6d4-b76eafea67a7 | -13.21412 | -48.50274 | 2025-10-02 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d1d5eb94-6300-38a3-8f0d-929108731c4c | -13.16944 | -47.80941 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 45637af8-88be-3c45-bce9-bb036045dd24 | -13.42607 | -47.79277 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c6eea817-ff88-3fd7-9ea5-efa30871a28d | -14.79544 | -46.99456 | 2025-10-02 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b39cdb2-9d7a-332c-814e-7eeb13b7da22 | -14.40331 | -46.08222 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a0118995-3818-3ce0-ae21-f9f06b748fd4 | -13.1601 | -47.83576 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 19a3390a-256b-3783-a423-0a503dd69b67 | -14.03097 | -47.98756 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af076d10-25ad-33ab-bb64-4bf60a379b4a | -14.43537 | -46.3627 | 2025-10-02 04:04:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fdf3f834-2148-3f97-b166-b28917eefcb4 | -15.67488 | -46.25232 | 2025-10-02 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d319245-ab51-3276-ba23-ff3680d7b74f | -20.70825 | -43.27845 | 2025-10-02 04:04:00 | NOAA-21 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 754b3309-81eb-34f9-ab62-b602a7b11b81 | -14.08759 | -46.65927 | 2025-10-02 04:04:00 | NOAA-21 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6bc75aca-4ee6-33d5-936f-6aeb2992d280 | -15.12219 | -48.49159 | 2025-10-02 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22d21c33-c2d1-38a7-a78f-2e8119da4460 | -16.40469 | -45.97639 | 2025-10-02 04:04:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 342d6b19-6a6b-3a33-8774-bd802d845b92 | -19.75437 | -44.03152 | 2025-10-02 04:04:00 | NOAA-21 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4adb7d75-e671-324c-9e05-caa41486a5cd | -13.1698 | -47.85563 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 54ca971c-5283-31bb-a785-960a978725ec | -13.30344 | -47.84345 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 60ecf889-b574-3856-bacc-df844424e937 | -13.32282 | -47.20877 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6942dd17-b468-39d8-8861-71bb539dd5e2 | -14.15996 | -46.13632 | 2025-10-02 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f8708f64-a217-3c47-bf96-a5bbc8f57d38 | -13.30366 | -50.67942 | 2025-10-02 04:04:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 05326f0d-e1de-3c7d-a4ec-3526fd5ad11b | -12.49985 | -50.26073 | 2025-10-02 04:04:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ac46a04-7420-34f2-8e06-af17ab01f6ca | -13.30264 | -47.84781 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 42cc6784-4022-3ebc-9e3d-c3137137e419 | -13.7987 | -48.04012 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b3d1e925-e22a-34ad-a468-29b12ee5a14d | -13.68142 | -48.06059 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f7546cc3-0563-3e1a-9d49-a94e29a644a4 | -13.16442 | -47.85112 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 46ee5a9f-5f98-310b-bd29-6119bca005a9 | -13.56735 | -47.27481 | 2025-10-02 04:04:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bb14268c-71d3-3a2a-b1fa-6edb452a5c16 | -13.07907 | -47.0915 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3867fe53-bb19-368e-a9f2-cb0d4b84877b | -20.24102 | -43.88594 | 2025-10-02 04:04:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 9e7b91ab-e1f4-34cf-9fc2-2b03ed2445bf | -14.34028 | -47.14759 | 2025-10-02 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea82dd1e-2ef0-3e45-88ad-172ba4582b76 | -13.08197 | -47.0844 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d929f76-8de1-3e19-be1a-570fcba62178 | -15.22411 | -47.17572 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1efb2952-0c4c-30ab-8993-d2cfb62909eb | -19.57376 | -42.58825 | 2025-10-02 04:04:00 | NOAA-21 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 67cf7051-2ea9-3732-b5c0-58d365879629 | -19.96126 | -43.65549 | 2025-10-02 04:04:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 93a5dadb-2a2a-38db-9529-987fdf7ff44e | -14.62242 | -48.30095 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 08dd6f94-c058-32bf-af8f-1eee6fda0af7 | -14.58628 | -48.32042 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ed2b6721-32eb-32ef-a310-43ce2e9aa2bc | -16.29421 | -45.24248 | 2025-10-02 04:04:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 351107da-f6a2-3fa4-b22a-993c8565f4f7 | -13.18543 | -47.79514 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3efbf19b-c468-3ca2-bd37-2a086988cd27 | -17.68134 | -43.83265 | 2025-10-02 04:04:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a97b0cc1-6fa5-3dad-ada7-21039a7a96fd | -14.65549 | -48.26804 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be7b54cb-c708-30d2-a5a3-d965946a297a | -19.87114 | -42.57814 | 2025-10-02 04:04:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bf605c83-ab02-363e-8c04-ed10081266ae | -13.80833 | -47.53828 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 5f2a84e4-3830-3ad9-91a1-12c65d53a18c | -14.97994 | -46.86775 | 2025-10-02 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 890de520-1c65-3458-b758-1b63f184af60 | -13.47588 | -47.24903 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d43c480-474a-34e0-b451-3873e59d4497 | -14.41936 | -46.0799 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 49751f58-9be1-3071-8e60-8a038948d0e7 | -15.70051 | -46.26106 | 2025-10-02 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9e0d9882-548d-3087-afc9-3f6ff34d5639 | -15.16167 | -52.79672 | 2025-10-02 04:04:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e38db414-826a-39dc-85c6-251f830df4f1 | -12.68451 | -48.57695 | 2025-10-02 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2742e2f4-a106-3d5c-911a-7a2270bf3e35 | -20.03657 | -44.53878 | 2025-10-02 04:04:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 60901b28-9e3c-3e97-91b0-7b7152c3d53b | -14.02043 | -44.96935 | 2025-10-02 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e60617f4-3078-3da3-a498-5aaae3095460 | -18.01121 | -42.85886 | 2025-10-02 04:04:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bc124896-ead2-310f-96a8-0df0fc1c0d0a | -19.45613 | -44.29163 | 2025-10-02 04:04:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24c54fdd-73d7-3a9b-be51-08a0c9dc6c88 | -13.80905 | -47.53433 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c3a0518f-3518-3481-bfb3-baf7b530e618 | -13.81323 | -47.53514 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d4d7c56f-f94d-350c-9bb5-1bc7402d4282 | -12.70561 | -48.59103 | 2025-10-02 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 63fe6923-6968-3569-aea3-c047e489dc15 | -14.3028 | -45.96697 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b2948b88-da64-32f4-ae50-023f061a7dcd | -15.99766 | -50.86926 | 2025-10-02 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 955ae173-22a9-3d43-b750-61eae1aa1ecf | -18.42953 | -46.53402 | 2025-10-02 04:04:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 17153850-c576-32f8-b6b4-d9534d552fda | -16.28081 | -42.54682 | 2025-10-02 04:04:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |


[Clique aqui para ver as próximas entradas](README45.md)
