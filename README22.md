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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39b8f23c-ce1a-336b-a3bc-88deec6f03a2 | -12.80339 | -46.44175 | 2025-11-17 03:49:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 562bc2fc-2e52-3174-bf83-4d79967b02da | -9.74197 | -43.96995 | 2025-11-17 03:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a71246c-d61a-3f7d-8a96-cae172774324 | -13.81861 | -44.45611 | 2025-11-17 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a041531-4e3f-38b8-b9aa-acfa892f00da | -10.85668 | -44.09007 | 2025-11-17 03:49:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| af928292-b5b9-30d1-aae5-fb126054cd71 | -9.84721 | -44.16327 | 2025-11-17 03:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efb2c8a6-1014-3395-8015-6fd8672dbacd | -10.96457 | -44.5256 | 2025-11-17 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9c07bdb0-81b5-35d1-a714-ed2256ed325a | -2.50182 | -47.81919 | 2025-11-17 03:49:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a58768df-8555-3b0e-bec2-025d25489c98 | -3.88747 | -46.46376 | 2025-11-17 03:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8504fc74-1e5d-31e1-8462-c3264428b6b0 | -9.57494 | -49.11937 | 2025-11-17 03:49:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 57733167-5fe6-3728-a04b-58910e3a1131 | -14.30838 | -47.10727 | 2025-11-17 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8592a9ed-b936-362b-ac28-d495ab299de9 | -3.6618 | -44.73723 | 2025-11-17 03:49:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f45b85b-41fa-30eb-ad07-44e08cfa9d10 | -9.72005 | -43.96577 | 2025-11-17 03:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3b26d8e8-8aea-3d06-85ad-50e9ef94d1e8 | -9.80428 | -48.56358 | 2025-11-17 03:49:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7a3abc82-ea0b-3c9f-b824-c271e5a3b36a | -11.70544 | -48.86735 | 2025-11-17 03:49:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| deaef58a-466e-3145-b074-bd05c955d536 | -14.36651 | -43.56291 | 2025-11-17 03:49:00 | NOAA-20 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83648a44-a193-3c5e-96ae-d0f0725a2110 | -9.84198 | -44.16685 | 2025-11-17 03:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2735608-a929-313b-9859-cc24afea93ef | -10.63524 | -44.60767 | 2025-11-17 03:49:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5996c3fa-603a-382f-83fd-d7d3335885ab | -10.12466 | -43.90557 | 2025-11-17 03:49:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed8048a0-d323-3af1-8518-e5a3e35b054a | -13.83766 | -44.13217 | 2025-11-17 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4d6bb9f-663a-30d3-9b46-e2b638c666fa | -12.41367 | -43.17093 | 2025-11-17 03:49:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4a203de-3584-3bfe-92dc-36c1cdf15043 | -12.40428 | -47.54583 | 2025-11-17 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa6b8cc9-8e29-3dc2-ba4f-6fce3c6bbf9a | -15.13227 | -43.74935 | 2025-11-17 03:49:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d5d3d74e-236d-3d10-a44a-a62a9c4599a9 | -3.38279 | -46.06773 | 2025-11-17 03:49:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 24250d36-d5ba-36f9-9c83-d7cd54ecf13b | -12.3365 | -43.65403 | 2025-11-17 03:49:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c13ff316-2285-396c-906c-393eb5d772d1 | -12.51774 | -47.26794 | 2025-11-17 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e7929f59-ec04-34b5-a256-c84b269e1781 | -11.56711 | -42.42361 | 2025-11-17 03:49:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e8f8e46d-43cb-35d3-b02d-467b72081bae | -11.82119 | -47.58636 | 2025-11-17 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 49f4bc80-0e46-3020-90c8-52a8e70df05c | -11.33676 | -48.90638 | 2025-11-17 03:49:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5bab31ec-25c7-30e9-b8cf-de7088e2ce1d | -9.5759 | -49.11448 | 2025-11-17 03:49:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c7a2e84c-04c4-362b-a6f3-2460cf61a477 | -12.87854 | -46.0504 | 2025-11-17 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0cf56047-6d9a-3614-91c8-b65d0125533d | -11.71209 | -48.86449 | 2025-11-17 03:49:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a14f852b-8cf3-357a-a937-64c57f913168 | -2.06525 | -45.39134 | 2025-11-17 03:49:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c7e8db3-54bb-3a92-be1d-d48221f85ed4 | -3.91525 | -45.80062 | 2025-11-17 03:49:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b312768-6ded-371d-998b-bfd6ee8dde73 | -13.81754 | -44.45931 | 2025-11-17 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7c94cfa-1bc7-3f0e-89b7-84a62004d2e3 | -11.8376 | -49.21149 | 2025-11-17 03:49:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b3e1cfc2-66d6-3888-a09c-081f4cf38719 | -15.38393 | -39.2127 | 2025-11-17 03:49:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1626b88c-2046-3d38-b29f-a6c287190618 | -11.82188 | -47.58286 | 2025-11-17 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 219a77df-049a-3975-9965-7ae200df5ece | -14.9167 | -47.35524 | 2025-11-17 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2856f5db-d119-3cbc-b409-7b316082944d | -12.88813 | -46.45943 | 2025-11-17 03:49:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d748a01-b063-368f-8424-2c2169a51b88 | -11.05928 | -45.15837 | 2025-11-17 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 78512e12-491c-3357-8ef8-afa3a356c536 | -12.84895 | -46.46993 | 2025-11-17 03:49:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8bb814a0-6e33-3b23-9f41-785b82dd78c0 | -2.50584 | -47.82388 | 2025-11-17 03:49:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 24904c98-66e7-30de-b9ed-5c8e0cdf707c | -12.79755 | -46.44559 | 2025-11-17 03:49:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7f74338b-eeac-35eb-b44e-7a931ba0be7e | -12.40907 | -43.17376 | 2025-11-17 03:49:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 037302ad-f0db-3d68-aa49-defe7a16fdfe | -9.33072 | -46.57413 | 2025-11-17 03:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 786d0c96-f6d8-35fa-8660-f3377d40d923 | -8.73301 | -48.32321 | 2025-11-17 03:49:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d31939b-6a76-3914-82e4-ad04b9a9989d | -2.06584 | -45.38767 | 2025-11-17 03:49:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a35132ae-1cff-3c74-8b02-aa007fd15e50 | -3.07441 | -45.19944 | 2025-11-17 03:49:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f564571b-1044-3611-beec-4a4ec43bdf5c | -3.59379 | -43.60406 | 2025-11-17 03:49:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c73fb97-1eb7-3835-a568-41d0b6b876b6 | -9.79841 | -48.5621 | 2025-11-17 03:49:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e8556cd0-55f0-344c-9441-d5d65851eac3 | -3.65668 | -44.73633 | 2025-11-17 03:49:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4048269d-f522-3a35-bc52-028bb23bfaa3 | -9.33011 | -46.57743 | 2025-11-17 03:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 0afa3208-d402-3c4d-b543-867a88799f95 | -14.43464 | -46.48849 | 2025-11-17 03:49:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d95e1ae-b0fa-3857-8224-644aa74d86bb | -14.1603 | -43.40671 | 2025-11-17 03:49:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea9094b3-58df-3523-8968-0b9f45261fd9 | -11.70713 | -48.85884 | 2025-11-17 03:49:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 47f224e3-5476-3bcc-806f-e343405ffa49 | -11.81997 | -47.58274 | 2025-11-17 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 563b0760-f467-3c43-9ef1-ed052e69ad07 | -8.05658 | -45.66409 | 2025-11-17 03:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99b70865-3ba4-3152-b4e0-0c42b4216249 | -13.838 | -41.792 | 2025-11-17 03:49:00 | NOAA-20 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e740a41c-94a0-33ad-b8e7-e453e075a07e | -8.31743 | -45.40937 | 2025-11-17 03:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62f2fbe6-7a2e-3785-aa92-7281fd664029 | -9.15197 | -48.06357 | 2025-11-17 03:49:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f5928e4-effd-3833-a405-6dd09da0939c | -11.57093 | -42.42455 | 2025-11-17 03:49:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2b4da045-8be5-3bb9-b867-24cc284426e0 | -3.67976 | -40.87739 | 2025-11-17 03:49:00 | NOAA-20 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| acdb3f9b-127d-37ab-844d-d299eff4b88c | -9.7515 | -43.96724 | 2025-11-17 03:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dcd63669-b505-3e43-8809-a1002e6f47c1 | -11.67074 | -44.72354 | 2025-11-17 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1c5e6cf9-91ff-3e24-b1ea-6a701d4a8d3f | -3.07976 | -45.20035 | 2025-11-17 03:49:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb6ed39e-ac76-329c-9674-1229bb9bff5e | -13.81828 | -44.45538 | 2025-11-17 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 924e7655-3f75-35f0-af0a-49cefd8983d0 | -10.96595 | -44.53247 | 2025-11-17 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ba1bfa77-c9c6-351e-b27f-35019c088242 | -3.90978 | -45.79961 | 2025-11-17 03:49:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5182115-28f2-30ad-ad55-b106d4d56cfe | -3.37652 | -46.07055 | 2025-11-17 03:49:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71e36125-65cf-32d4-b369-28f2e4b8fbaa | -9.71568 | -43.96488 | 2025-11-17 03:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e72a8030-7be8-320e-9143-b056a363025f | -11.70046 | -48.86179 | 2025-11-17 03:49:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d56cb9b4-942e-3fe0-bad1-37e94c731032 | -12.69836 | -46.77359 | 2025-11-17 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9d7ed9c4-833f-3bef-8090-4aa3007bdf41 | -12.33239 | -43.65326 | 2025-11-17 03:49:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9545dc4b-b044-3e2c-8e99-a2d8a84f6b03 | -4.09238 | -40.51651 | 2025-11-17 03:49:00 | NOAA-20 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 599914ce-071a-3c09-aa72-e3d22e5ea789 | -9.80109 | -48.56365 | 2025-11-17 03:49:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bf0ddfa6-fe1c-3bbf-b57d-d0ac175ac70c | -12.88206 | -46.46443 | 2025-11-17 03:49:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b54a84cf-000c-34a2-8f75-45c22b51aabc | -10.53444 | -47.91396 | 2025-11-17 03:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b117a544-1903-36dd-9db6-3a39c7106e51 | -3.66414 | -44.89053 | 2025-11-17 03:49:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5bfbcc61-0fed-3e93-a0ad-382b152602c3 | -3.07107 | -45.20683 | 2025-11-17 03:49:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4864ca92-b75c-3091-8f6f-78370038eb6e | -12.87969 | -46.46897 | 2025-11-17 03:49:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64295470-de7e-3457-bc3a-8f956d0539a6 | -1.87166 | -46.36804 | 2025-11-17 03:49:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62e122c5-4926-3689-bf49-375bd18f9f7b | -3.35109 | -43.49332 | 2025-11-17 03:49:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 814dc9ee-d266-31d8-b690-6c3ef37b00fa | -12.86651 | -46.03634 | 2025-11-17 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b7f68d6-3825-3361-982f-d8dce6d85c43 | -3.62115 | -41.50195 | 2025-11-17 03:49:00 | NOAA-20 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0d5ecec3-fe1d-3aea-8f61-ff8a4e5131b0 | -10.96298 | -44.5346 | 2025-11-17 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e145207-d46f-3a91-8d7d-03d343eddd55 | -8.52843 | -46.08063 | 2025-11-17 03:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b6c2c366-51fc-379a-bb65-745ec4a60621 | -12.20271 | -49.61548 | 2025-11-17 03:49:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3cdd2fc-b0ca-345a-9fe7-d5ff486307c7 | -10.85152 | -46.74493 | 2025-11-17 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 711e83e5-3284-3862-a96e-d5af10d62416 | -10.38955 | -44.91788 | 2025-11-17 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f33b803a-b78b-3559-a1b6-f3a9c85c2001 | -8.3314 | -45.42013 | 2025-11-17 03:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6466a9d9-b5a7-3d0d-8ac0-b4fb424765da | -2.50821 | -47.82015 | 2025-11-17 03:49:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 35728bed-2c3a-3f21-8791-a8f0cf3f2a10 | -12.40495 | -47.54243 | 2025-11-17 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd2754b7-1fae-391a-9372-d16104092aea | -15.38062 | -39.21214 | 2025-11-17 03:49:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 60eb0130-deab-32e6-ad14-69a5fba7dbb1 | -8.30271 | -44.19426 | 2025-11-17 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3793f184-f7f0-3980-a813-06219bf203de | -10.85613 | -46.74901 | 2025-11-17 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 9fd0d158-fe29-307b-abd9-71da220f34e9 | -15.2662 | -46.56175 | 2025-11-17 03:49:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96a0755e-6f6c-3ea6-a6a4-882cb7328bab | -12.02358 | -47.01672 | 2025-11-17 03:49:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 619c2361-48d6-3028-8d81-c1d139a46fe7 | -3.07387 | -45.20281 | 2025-11-17 03:49:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dbd53c5a-48d5-30f6-8603-501ff4b83e86 | -11.82399 | -47.59103 | 2025-11-17 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1301bf5c-2b6e-3f55-907c-71acd2915e86 | -9.72731 | -43.97602 | 2025-11-17 03:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |


[Clique aqui para ver as próximas entradas](README23.md)
