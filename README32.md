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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f390d2a5-2582-3e02-94f4-65d5d83fa0fe | -14.74367 | -48.13542 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1b370a9c-9eb9-3a79-9764-9587b9346e19 | -14.72995 | -48.11394 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 970208d0-9d7d-3fee-9b3f-4d3a4c6d7f33 | -15.57447 | -46.95505 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 115ab1ee-7532-3332-a075-257e728aa2e9 | -11.01393 | -46.55035 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a2acfad2-d319-33a3-b840-d95ef82de9e1 | -11.81318 | -45.03199 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02a0872f-18d5-34bd-8e9d-6dcdc0790ea3 | -13.97407 | -48.12725 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ca2618f6-f477-35c4-9411-64a43d1e47d3 | -14.90316 | -48.30203 | 2025-10-03 03:45:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b378966b-aa6e-3be3-8f0f-334349d4d49e | -11.04324 | -46.65668 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68dc413e-489a-3e1e-ac6a-8a81caf3f200 | -13.27022 | -47.24181 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6b789726-55c2-3b65-b397-dbb0a7335f32 | -15.91879 | -43.33966 | 2025-10-03 03:45:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0b0ac633-2f44-3dbd-bf44-b6306627ec67 | -14.29203 | -45.96839 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0d6f8ba-aa2c-379a-a431-a7a33d54529a | -14.59181 | -48.34368 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4fd2fbb3-a3bd-3b32-b684-2f455586a707 | -10.84446 | -46.59616 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96f41229-8d5a-3cf0-ab2b-12f1f17958d6 | -12.75186 | -44.91285 | 2025-10-03 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0c606ec2-27ba-3dff-855f-d2d4bd5c17b4 | -11.59974 | -42.8734 | 2025-10-03 03:45:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1af81327-e2c3-34ef-839b-daa59b70502d | -13.48274 | -47.24932 | 2025-10-03 03:45:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f0a711c8-894b-3463-8c0f-a47845c36214 | -11.86082 | -44.97129 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c025412c-0b24-32f4-a4a0-d1af97103ae9 | -13.69076 | -48.63046 | 2025-10-03 03:45:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6f9b6dda-a853-344c-9f7f-1633d044d6f0 | -15.25339 | -47.91564 | 2025-10-03 03:45:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 35cfbb37-4d6d-31a9-aa89-745430dc72bf | -10.65755 | -48.48396 | 2025-10-03 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 90f3bbde-a68a-304e-b0ca-f09979c088e7 | -10.27874 | -44.32928 | 2025-10-03 03:45:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 868a8027-5a3f-301e-83af-4bc0f3d50d60 | -13.20461 | -47.83206 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e07ccee-7de1-38dc-9034-347b4f0593b9 | -13.1982 | -47.89412 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e43fccb4-77bb-345c-9682-8263f5d43be8 | -11.14584 | -43.38598 | 2025-10-03 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| d540004b-d478-3ec0-8c55-c5b76bade36c | -13.84765 | -47.9257 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67619e74-69b2-3ecb-912c-46a0b35df968 | -13.52034 | -47.25207 | 2025-10-03 03:45:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 711a9f16-4b8c-3f8c-a2c0-654d835000e9 | -13.33141 | -47.59085 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cd4a7f15-8c3a-394b-b707-497beada97d1 | -14.22837 | -46.09343 | 2025-10-03 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e673e901-966b-3727-8b64-90d61259faf5 | -11.58931 | -47.66981 | 2025-10-03 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e9f6a2b2-39da-3ffc-95d5-ed011cfd908c | -14.88075 | -48.3418 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6b9023e-e80c-3a64-beb3-857f99820831 | -12.86487 | -46.9961 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84237df9-a67b-3033-859a-c7a86783114a | -12.89759 | -46.93771 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a2e8fd5-997c-3cd9-9051-c22af01ce39d | -11.45346 | -44.96195 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7b7beb42-10c0-3e73-baad-8fd8cce026fc | -13.75703 | -48.06911 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 466a1c21-24d4-3775-a775-2c8642a6561c | -12.29347 | -45.36455 | 2025-10-03 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54fa73bb-b83e-38b0-a346-802426aec181 | -14.66795 | -48.09473 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 08a65ef3-0225-30d6-a86e-08944108c268 | -15.30652 | -46.28519 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a81c3ec-c11b-39c2-b19d-471cb59fc045 | -13.86256 | -47.94221 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d088fe7f-6ab2-34b8-961f-3c79b56a54e3 | -14.91035 | -48.34694 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d632b316-9499-3628-9512-d6d596403ec8 | -13.77412 | -47.54712 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| db9d96e3-ad91-318d-82e0-1c32ef5ffcc2 | -13.7366 | -47.99924 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05e497e7-2794-307c-815b-31792d2d5649 | -14.37711 | -45.94054 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6e937ff-ff38-3a66-b8ce-f0d658b04f85 | -14.70364 | -43.88875 | 2025-10-03 03:45:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 20.6 |
| 60fed15d-01d5-3c55-96b2-f1a08412a884 | -11.4897 | -44.99171 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 756d4709-8b31-3c36-acef-87b5954bb5a3 | -11.55449 | -47.65736 | 2025-10-03 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0caac0d9-5856-3629-8203-51e8ccb5310f | -13.34068 | -47.2128 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c20831a5-5833-3b7c-b1f1-53f3afc40c4a | -13.32506 | -47.20288 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 87b08c6d-fc1a-3565-9edd-a440a0644635 | -11.85555 | -44.96879 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 48ab79f8-96f0-3a6f-bced-4b59a1219a5d | -13.31003 | -47.57727 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6109b99d-ff0c-36bc-b750-3480d179c3ef | -12.62982 | -46.97035 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1e08e070-15ad-3683-8676-e925de23b798 | -15.51171 | -45.91027 | 2025-10-03 03:45:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c8a1170-8606-3afa-93e4-b25ff65c8f78 | -10.89367 | -46.71704 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 79d741cb-d9af-3560-9413-da4b44847483 | -13.57273 | -47.28346 | 2025-10-03 03:45:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bb45e35a-a399-35cb-985e-e01e2d3b1dee | -12.80628 | -46.85188 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8345942d-b8f6-3fbd-9e23-45b8c2a36f9c | -12.62076 | -46.9867 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d1b34a28-090c-3e09-90c3-4c969783d4c9 | -11.84136 | -45.04267 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3977aeb8-3fbe-34ae-b139-7cacecdaf0b3 | -15.94694 | -46.22877 | 2025-10-03 03:45:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 90c0230e-c374-3b81-8eb8-86c2cd699b4e | -15.21941 | -47.63769 | 2025-10-03 03:45:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ef0eec05-8bcf-36b5-a311-7f01b1ea2874 | -11.00892 | -46.63909 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba0a1f18-8cb7-3a1a-9283-950fad331303 | -11.61214 | -45.0303 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2f2fec05-970b-3e8e-817d-6e23db7fa6e9 | -14.41377 | -47.86452 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c469efb-0021-3f38-a69f-4a45c37eb91e | -14.6854 | -48.0983 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 15912e3c-1edd-36fe-9963-e8a7bc3706fd | -10.86711 | -46.66257 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b125b35d-b2fe-3503-900c-31941acc46ae | -13.75798 | -48.0645 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3bec973a-7d53-347e-8392-3421afbd51d6 | -12.91971 | -46.36749 | 2025-10-03 03:45:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 58d83287-ac4d-37ed-a317-ee16790c5ae8 | -14.94235 | -46.88311 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c30a25a-3354-3c75-a343-810409186a30 | -13.14218 | -47.83811 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5517eefa-44f8-30ae-ba51-6f2341f6a2f4 | -14.87769 | -48.29853 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3537b843-4041-3c3a-9b96-8f22a71b9e2a | -15.70789 | -46.25702 | 2025-10-03 03:45:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c13af087-007e-39cf-b467-8bafcd30a275 | -15.11762 | -46.68534 | 2025-10-03 03:45:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 748cc0e9-411d-3cb6-b612-5dc167124051 | -14.95107 | -47.5176 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2bfe2551-3a7d-3c94-9912-724ce4188d1d | -11.63043 | -45.0643 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5d513004-cd81-3e23-b564-0c25a865aaf1 | -13.2664 | -47.26059 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 78937cce-6343-303b-be5e-829bd46dc74e | -13.12261 | -47.88409 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ae9752d2-1782-30a8-b7df-8c4de9907fce | -13.47871 | -47.25486 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4e5641a8-170d-3e68-9e0e-62963fe03e70 | -12.23091 | -43.764 | 2025-10-03 03:45:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ec0d117-ba69-36df-b33b-3e8ac52652fc | -15.66042 | -44.49331 | 2025-10-03 03:45:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5079c783-7208-3a68-8130-13f5b983edd2 | -13.26673 | -47.24647 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 7383632a-8c90-373d-af38-b26839993f42 | -13.45738 | -47.22935 | 2025-10-03 03:45:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7381f9b1-04c4-3d3e-9030-4d7094c4d8f5 | -8.45874 | -46.84519 | 2025-10-03 03:45:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c1ee334f-ca90-3477-879f-76b5d58b7dc2 | -15.30691 | -46.38953 | 2025-10-03 03:45:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cee9f9e8-f03d-3bab-8253-d2a281b1ffac | -12.68376 | -48.54355 | 2025-10-03 03:45:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b41c537c-f7c2-31a0-b61e-2983676e9496 | -15.08521 | -42.12354 | 2025-10-03 03:45:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 28236ee8-6afe-3c75-bbfe-92ba4cdd5312 | -12.8074 | -46.85402 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b78c5bd4-d6e7-32a1-8e2b-a8ab67c890fe | -11.90499 | -46.29708 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9275d867-fa7f-3878-9bcd-1e2e9e9fcf7a | -12.67947 | -46.85661 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d3b7ed7c-c0d8-3440-a260-9f929d865e18 | -15.22409 | -47.97111 | 2025-10-03 03:45:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3d006581-a1cd-3694-bb50-27c0fd18afab | -13.7905 | -47.58369 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 94308c3d-7be0-3866-bec8-c8d3431873d9 | -14.89489 | -46.98042 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5daf934b-7c94-3596-b352-24898cb698d4 | -15.29943 | -46.29384 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d1f41d1-f685-3c03-9e69-de2e473e6ba9 | -15.28647 | -49.31055 | 2025-10-03 03:45:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7349f98e-2f6c-3939-8bc2-3207346cf3a7 | -11.83206 | -47.69227 | 2025-10-03 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a291a9e6-d021-313c-88fd-8bc5cc8e480d | -14.90389 | -47.82982 | 2025-10-03 03:45:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df3aae9b-93d5-3822-b867-d95e8e4454ce | -11.12062 | -43.39506 | 2025-10-03 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4cba9350-0b13-3282-a02d-0f2273d73e41 | -11.42486 | -43.49066 | 2025-10-03 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bc8e3846-997d-3ec6-a104-ab4c86ac90dd | -15.32715 | -47.3319 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 331213e0-6669-3e64-a85b-df99a4adf16d | -14.97889 | -46.85347 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f322c70c-85b2-3257-a135-f5ea5c3cb56b | -13.48137 | -47.25631 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6a34f1d0-ebde-3db2-96e0-0c7cf50fb73d | -11.87511 | -45.00239 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce814848-e320-3f44-81b3-fa65f538b168 | -8.33272 | -46.22792 | 2025-10-03 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README33.md)
