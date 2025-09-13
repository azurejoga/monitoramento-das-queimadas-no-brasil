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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7943809f-583b-3545-87b8-c9bea055db9e | -11.43519 | -43.55962 | 2025-09-13 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb6a3767-d1a2-3747-bbae-ba96a1259bb0 | -10.42463 | -50.63196 | 2025-09-13 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fc52ab2e-9246-3026-a0b8-8e72e2820982 | -11.17775 | -51.41532 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 906507b5-4aad-3e62-90a3-9b642a3edb9d | -15.13709 | -52.4894 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| aa1dd0af-39cc-36d4-b3f7-8f4a363cc8a2 | -9.32285 | -60.27308 | 2025-09-13 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| daa9660d-f5ba-3ad5-a1c6-b3e96ccb0316 | -10.52869 | -51.54691 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ce248ab7-44b8-3703-8a84-88947a1220e1 | -15.16686 | -52.49406 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08384390-fb4d-3d72-afc7-1d164a1acdfb | -14.19664 | -46.23745 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a5fdb3b4-4d56-3c26-ae56-04fa1d808590 | -11.83439 | -50.55317 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14f01160-94a7-39e0-830e-1bd2e8c5e765 | -14.19129 | -46.2856 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b280a99d-08de-31d3-ae06-9de4677c9d4c | -12.09141 | -44.89653 | 2025-09-13 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2799d6a6-1ab3-3107-81a0-4853e2f13025 | -10.52258 | -51.50989 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 49722d79-3e88-365c-8290-531ee648b83e | -11.44291 | -45.62617 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e92e71e0-26fe-34d6-a58f-cad07816f122 | -12.12012 | -44.8439 | 2025-09-13 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 14b7a002-4716-3482-8cbd-e9a3ebf5d34b | -15.75952 | -53.49882 | 2025-09-13 04:59:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e8e4d9e9-52a0-3236-9ccc-d6a10df4966a | -12.91828 | -54.75105 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2144aec2-5608-309d-840f-1d92fc078593 | -11.77733 | -50.55206 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63caa838-b102-3593-995f-56379fcda291 | -12.95171 | -47.98138 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 06885d37-6e4a-3390-8b47-6224b88f529f | -14.22911 | -46.29817 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 9cb331b4-0d72-395c-88d0-29e17c15e790 | -11.26899 | -51.12449 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4ca14da9-d1ed-38cb-afd0-6c78dcf6da84 | -15.13215 | -52.48556 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1ecfa619-bf5c-333c-872d-93ac2668b8fb | -11.86035 | -50.55616 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5726ae7b-4549-3209-8c31-bc33b83540b3 | -14.28301 | -46.071 | 2025-09-13 04:59:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bff3c9be-26a4-3110-9451-615104a2cf42 | -15.06019 | -48.00025 | 2025-09-13 04:59:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a0634a61-631d-32fd-8aa9-de398f8c8f2b | -9.89006 | -58.33279 | 2025-09-13 04:59:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 30452784-5a56-3a0e-a72b-9e614f9f60b1 | -11.73433 | -46.60489 | 2025-09-13 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6c455d04-aeda-30de-a1de-a741d41b6791 | -16.41104 | -49.23827 | 2025-09-13 04:59:00 | NOAA-21 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e81f33bb-96bb-3cf1-87a2-d0b807603364 | -10.50583 | -51.53279 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cf178a3b-407f-351d-ab36-9410c3ec46a9 | -16.33035 | -43.7564 | 2025-09-13 04:59:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d3d55b0-00fb-3878-853b-bf29d92eacf9 | -11.43178 | -45.62486 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a98df554-c8d0-3911-83b0-2a403ab6c6c7 | -13.40371 | -46.80053 | 2025-09-13 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6819c4e-391e-3541-9cca-7acbc4a91f10 | -11.60503 | -52.22798 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4e3cc6f-7980-373d-90a7-55f074adb871 | -12.56462 | -46.93872 | 2025-09-13 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c74d4114-08df-3cf5-9953-b61517d3d1fb | -12.8638 | -62.14927 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a05a50d7-672a-34aa-9864-d46b5d7cd640 | -15.77219 | -52.24755 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3ec61e99-66fc-3b4b-8564-e9947ab94c1d | -13.91899 | -48.2788 | 2025-09-13 04:59:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| cef48d5a-4ff6-3561-b114-649ed075e692 | -12.12251 | -47.59184 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8016bbba-4527-3e58-860c-503e85d19952 | -11.87044 | -50.5721 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 674cc1f9-ead3-3678-9af0-877d2e0fdb66 | -10.74991 | -50.54412 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7813ad7d-29ff-3fec-9c48-09c378da2bbb | -11.18594 | -51.4118 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| fcc64f04-fba7-3f13-8280-35dcb092355c | -11.27214 | -51.12991 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ceda5e1d-02b9-32cc-933e-d59441331a94 | -9.82678 | -54.53884 | 2025-09-13 04:59:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 51858205-f5f2-31d0-aa65-2a60c8dea515 | -10.7467 | -50.53841 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b7d0f983-72f5-33ee-8c03-23b78ff956df | -15.68886 | -49.90154 | 2025-09-13 04:59:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a0f9ea0-cf4d-31f7-9073-f8f1b2e030f6 | -14.7196 | -55.63993 | 2025-09-13 04:59:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 07547032-2a08-39b3-b486-77bba040d5df | -12.5811 | -45.66771 | 2025-09-13 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 891d675b-2a98-3b2c-82f3-dacac2cad849 | -15.14522 | -52.48542 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fc5dcec9-186b-3de9-b515-78c198ef2396 | -12.58067 | -45.67152 | 2025-09-13 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 099b8046-d19f-383c-a6f6-f3a8622d3cc2 | -15.07323 | -48.01855 | 2025-09-13 04:59:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6b6718f7-e3f6-30bc-9909-813e6d378888 | -14.19949 | -46.26261 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ed587e4d-10a6-39ee-9746-d855d3fd463d | -12.94858 | -48.00666 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 324d8f54-ffc7-395f-a720-2d911d4a2e35 | -10.15449 | -64.72549 | 2025-09-13 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0ed8e9a3-d5e6-3da6-a659-28a2e875cc9e | -15.77534 | -52.25283 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 202f83d5-8981-3d82-b5a7-114e57029d33 | -14.9122 | -55.95568 | 2025-09-13 04:59:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4878a55a-86f8-37c0-98e2-d3ab2de8c912 | -9.50444 | -55.96501 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 1274a36b-68b6-3c99-a37f-ba05ac07b243 | -11.73535 | -46.5966 | 2025-09-13 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 65c86ed0-b044-3dbe-9cc5-83454539b83d | -10.61521 | -52.32719 | 2025-09-13 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b57ee50f-9cec-3b48-b5c9-a84261f79567 | -13.15074 | -47.13678 | 2025-09-13 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c01f638-e720-30f3-99e7-b028b55005eb | -10.76472 | -50.5253 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e0cc1b84-d7a6-3ffa-ac72-a5cb6de93b89 | -13.51157 | -50.80799 | 2025-09-13 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6c09f3d-1842-39df-a4b2-9b2c2a2484bd | -15.87053 | -51.84806 | 2025-09-13 04:59:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 784845ee-825f-37ef-99d5-4b1e6a88c0db | -10.54929 | -57.08413 | 2025-09-13 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3074499f-f4e2-3181-9a2b-5994575d2d5a | -15.13403 | -52.48391 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5740afd6-bda2-3f24-971c-2eba704c0246 | -12.12872 | -44.83432 | 2025-09-13 04:59:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1918e877-7d72-3af2-8cdf-b0853272f69f | -10.46023 | -50.60789 | 2025-09-13 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 168d47a7-f324-34d2-be51-168ea0473b3d | -15.1634 | -50.16221 | 2025-09-13 04:59:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c87a7d1e-d522-323c-b27e-4cc36ea95da5 | -10.36357 | -50.49785 | 2025-09-13 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 576b2517-5628-34c7-a734-8e0226013771 | -12.94 | -48.00441 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a7349e7c-ab97-3433-9e5a-5b698e3b4137 | -14.19294 | -46.27158 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 5ec796d6-f48c-385f-bfdb-08d3d1fc4cea | -12.95464 | -47.99746 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| cb94ee03-ae07-37f9-a865-ff04a061d649 | -11.43365 | -45.60931 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 35e9d819-5400-3b11-98ac-1b1b92250300 | -15.7124 | -50.58551 | 2025-09-13 04:59:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 225d4527-09d3-36aa-a089-e2bac36032c8 | -11.11589 | -51.33268 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 67cedfa6-dc9d-3147-b2bc-5ad03eebf588 | -9.1699 | -60.31006 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f10f1e8-624a-364e-9b94-438b432a22a4 | -10.20425 | -58.22852 | 2025-09-13 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c25c9353-eace-3fab-b43a-09577c6f8e11 | -15.164 | -52.40334 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9040f242-f707-3e4b-be4e-3c6d833cb774 | -11.1915 | -55.08273 | 2025-09-13 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ee2bbed-2500-3704-becd-b3361a7253b6 | -15.15767 | -52.47781 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6105b9ce-c9d3-3712-8bc2-f7dce9cc0fb3 | -10.75185 | -50.50237 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9a7ad67f-eb68-3162-8abe-ed16a610d92e | -10.69369 | -48.66199 | 2025-09-13 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f73bf2ea-301a-3360-a6f5-9b4ddb9a5c71 | -10.25582 | -55.81965 | 2025-09-13 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2548915-f7b0-3012-ad4c-59c50502deb6 | -10.33316 | -54.31958 | 2025-09-13 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45b85ec6-a7cb-38c2-b75b-acf96fd302c8 | -12.93607 | -54.74648 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 352b3e41-81ae-31b0-9640-71506a568cee | -14.20923 | -46.22848 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27423e1d-cddc-3d38-9572-68f8735eda47 | -10.85038 | -48.18083 | 2025-09-13 04:59:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 751bc526-06c3-359a-87a3-beeb70dc2063 | -11.73575 | -46.59332 | 2025-09-13 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4de44484-2620-3c49-aa76-96ce5c98ee68 | -11.23206 | -54.99581 | 2025-09-13 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a1afe1c4-5226-3a03-8eb1-d62968031b72 | -15.16136 | -52.47867 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b3212511-3acd-3e34-8d76-945bd4e7b6e1 | -15.11663 | -52.48776 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 35f20979-61f7-309b-a5d2-c4729919cb40 | -14.19616 | -46.24185 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 41c22592-875e-3102-85ca-b3c0c5dfe7a2 | -12.44577 | -44.74761 | 2025-09-13 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0fc2d4ed-82a2-3da3-9690-1cbd8a2e734e | -12.8318 | -47.92496 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b9a7415b-8cc4-38fc-89c8-946eedc34d7a | -12.06176 | -47.62046 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d25c0160-2a3e-32cb-b09d-f6cd5d167629 | -11.12313 | -51.47111 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c438329c-4830-3a21-88ff-4816e29251d2 | -11.18429 | -55.06364 | 2025-09-13 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df9d7262-d967-326c-83a4-03f2f912c633 | -12.80015 | -47.98931 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 38a79300-5337-3a3e-94b9-0fa1396f283d | -12.99855 | -46.75179 | 2025-09-13 04:59:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8c0df907-8337-39fd-8a03-8431dcb02a6e | -15.18682 | -56.37634 | 2025-09-13 04:59:00 | NOAA-21 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c1c79b9-863a-3b53-9cde-77690c247c0b | -10.71825 | -48.61395 | 2025-09-13 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 62438f19-8daa-3dbd-84e2-04025fd0c6a5 | -14.55242 | -53.2764 | 2025-09-13 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README85.md)
