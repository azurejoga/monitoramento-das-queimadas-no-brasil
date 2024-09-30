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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ab79bac-354e-301d-a040-98044b4120ed | -13.57811 | -47.60936 | 2024-09-30 04:32:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 156b66d2-f1d1-383b-961b-ccf33c8d854e | -12.47957 | -46.44572 | 2024-09-30 04:32:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1db9f910-9922-3c20-a97b-6bf1ef33f1fc | -12.47604 | -46.4452 | 2024-09-30 04:32:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 603c034b-e761-32bf-9475-d75c502a6fdf | -12.47252 | -46.44468 | 2024-09-30 04:32:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d93aaed-d95a-3da2-b661-c49e0348ccc4 | -12.46899 | -46.44419 | 2024-09-30 04:32:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c663256-4464-3384-bf63-f1498fba26c7 | -12.81432 | -47.45362 | 2024-09-30 04:32:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db7e49ba-7ab6-3aeb-a67a-e70fed7f8fb5 | -12.81092 | -47.45309 | 2024-09-30 04:32:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4345b2f-7266-3871-bcaf-bf1ac34613b2 | -12.80751 | -47.45257 | 2024-09-30 04:32:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c772249f-627e-3107-b1e0-0a0ad235da96 | -12.68836 | -46.7708 | 2024-09-30 04:32:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de25524b-4597-3a04-bccf-f800fe86a8be | -15.08017 | -48.16276 | 2024-09-30 04:32:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6464c35-02ce-36ef-9365-aeb26775186c | -15.02362 | -47.55641 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57372819-de07-3c57-b293-731af38d84e6 | -15.02078 | -47.55185 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fff7e95c-df11-33b7-9b8c-e561e6a66cde | -15.02019 | -47.55581 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02384ffb-a1e4-316b-a1ec-fe5ab74d925c | -14.76037 | -48.3553 | 2024-09-30 04:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8a701d5-7d79-38eb-b8bf-937f5c60c1d3 | -14.75981 | -48.35899 | 2024-09-30 04:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e9e23c6-2465-3fc3-ad39-b39ac6f9fce0 | -14.75702 | -48.35474 | 2024-09-30 04:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62f690ef-289f-359f-9ea3-e80f59999dc7 | -14.59366 | -48.13712 | 2024-09-30 04:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8dafa223-20de-39c2-8c83-a5d3fb5adf5a | -13.85323 | -48.0561 | 2024-09-30 04:32:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0d7afb9-29ab-3575-acdb-cc3b2c8211c9 | -13.85267 | -48.05978 | 2024-09-30 04:32:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf0468a1-bde1-3b85-84d1-1bbe3a277fb4 | -13.76974 | -48.08406 | 2024-09-30 04:32:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 407240f3-7ca0-3321-9b79-708ccc2855e8 | -13.49195 | -48.59611 | 2024-09-30 04:32:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0de4c07c-b466-358a-a705-7942b6fee37d | -7.80373 | -47.47427 | 2024-09-30 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af2e8cbd-a497-3b76-8a41-02165aa76af9 | -8.17639 | -47.67614 | 2024-09-30 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a4de6fe-0e1e-3d9e-8882-9e10f50980dd | -8.11524 | -47.69859 | 2024-09-30 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9ac3bbf-e0e4-3f36-8b90-75ac1b19b592 | -8.11247 | -47.69459 | 2024-09-30 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d60c86a-490d-357c-a1a6-2d2df08e0161 | -8.11192 | -47.69807 | 2024-09-30 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa4d06da-c87f-3cd2-aea0-cca4237c325e | -9.73158 | -48.1109 | 2024-09-30 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3b18bfc0-ea33-3ea2-a1af-4425994a5f04 | -10.56956 | -48.04922 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 15396605-dd8c-3602-a490-2f22cdde0da4 | -10.56571 | -48.05215 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 710e7bbe-9195-3395-a52a-cb354f0ef5fa | -10.56517 | -48.05563 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0b5d5072-cc14-3801-bc7a-0557295bf9a7 | -10.56293 | -48.04813 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1990f0f3-ed9b-3228-b52f-a3109cda9fcb | -10.55745 | -48.06157 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8512035a-24b2-37f3-a479-f2798a900561 | -10.55468 | -48.05753 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a638c3d1-ffde-368c-abbf-6f419b7f3d55 | -10.54809 | -48.0781 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37940f91-40ab-3adc-92f3-e993fdf13d06 | -10.54689 | -48.04193 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf2465b7-153d-3a81-bfac-a9ed3d10ba3b | -10.54296 | -48.02334 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d777172d-c5fd-3341-9adc-2efe98ca7e83 | -10.53372 | -48.08304 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c644ef5-7530-3bf0-81a4-c0a71019d82d | -10.5304 | -48.08252 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a8e5ea0-535c-3884-9935-feb71bb31b61 | -10.45236 | -48.21418 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a161fa78-d7e7-3105-a561-32cfa76d8f47 | -10.45182 | -48.21769 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5e199f28-5d7e-3c8c-b02c-18708d11b2c3 | -10.45013 | -48.2067 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2bbd8806-9ea7-3b0d-ae22-2de9d8c06a79 | -10.44959 | -48.21018 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9a295767-baae-3c5e-98d2-5df4457d8927 | -10.44905 | -48.21367 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3fdbd498-2f5a-3cba-b46e-7e3f1498854e | -10.4485 | -48.21717 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 301fd26d-b90e-3630-8c95-581922177307 | -10.44844 | -48.19574 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e51975ed-58c6-35bb-9e3c-0c97bedd75b5 | -10.44796 | -48.22067 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 010e32e9-8881-3ee3-89a7-fcc8e411adfd | -10.44681 | -48.2062 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 92730267-0876-3096-8105-c8db29135e7c | -10.44627 | -48.20968 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 13736e42-d3ee-37fd-ab4e-9a49c4fcf304 | -10.44573 | -48.21316 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 18097e22-100b-344b-8d04-f079e6cdea6f | -10.44519 | -48.21666 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1eb44cdf-6019-3c8f-bfb5-2eb9b2fcf93e | -10.44512 | -48.19523 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 430d877b-c240-395d-9d33-d919cf715fa1 | -10.44464 | -48.22015 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ff16038e-be09-33e9-9607-b0297e30a916 | -10.44458 | -48.19872 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1043860e-8781-39ac-aa02-13d765120d79 | -10.44404 | -48.2022 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9c95d852-cdb4-3a1d-a743-32d2e5991998 | -10.4435 | -48.20568 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 15f0e6f2-a216-3c71-b25c-922cadce0eb3 | -10.44296 | -48.20916 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c4a58aa9-2601-3770-9ba2-eaab9ec4b50d | -10.44242 | -48.21264 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c260d99e-4be2-3ad8-9d8b-89418a659f24 | -10.44187 | -48.21613 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| aa6a2711-b85f-33f9-a872-78d9b1c483f8 | -10.44181 | -48.19471 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc4966ba-fa1c-392e-8742-613876baa33c | -10.44133 | -48.21962 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 777f112a-7744-3dc6-ad5f-cfb51c3874cb | -10.44073 | -48.20166 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f3b69cd-acfd-3110-8e2d-283031361528 | -10.44019 | -48.20514 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa28a7c0-814b-31ca-8f60-8adf4d398633 | -10.43965 | -48.20863 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffb2b5ef-a2d3-3253-825a-d0cb2897fa86 | -10.4391 | -48.21212 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff37d372-5322-3318-bf05-4e821a9892a6 | -10.43856 | -48.2156 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d9b3a40a-5d38-380b-a832-5794a9192fa7 | -10.43802 | -48.21908 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 875bb41a-9820-322f-b630-9bb19e6752ec | -10.43742 | -48.20113 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d43a158-59d4-3a81-b3a8-f1b56f8dc4a5 | -10.43634 | -48.20809 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19b9874e-ecfe-39f5-a917-aabdee87a8a9 | -10.43579 | -48.21158 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ad60b81-0d61-3baf-9018-988b73da795d | -10.43525 | -48.21507 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cfea446e-6671-3bdf-8638-f6fc6b99427a | -10.43303 | -48.20754 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e02fff35-ba1c-3744-83f5-3c72a46837cc | -10.43248 | -48.21103 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85385b03-5e11-3f16-90b2-bb4445b187b5 | -10.43194 | -48.21451 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb505a87-9633-3d8a-b32b-0d34813734f8 | -10.43129 | -48.17505 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c8a5105-136b-35e7-b82e-11529e3118b4 | -10.42972 | -48.20699 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c992c977-dd7a-3c03-92be-ef59e2cdf810 | -10.42918 | -48.21048 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5a4d137-4a7b-37f0-81c0-3025235946f8 | -10.42798 | -48.1745 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 612d5e71-5454-3d31-80ac-da0543a7d1ff | -10.42743 | -48.17802 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e85048c-586e-3154-94bf-98ecacf05db0 | -10.42467 | -48.17393 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c17609af-6250-3da9-acab-bb90d96c46e0 | -13.49025 | -48.58496 | 2024-09-30 04:32:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0bdaf210-2f22-3489-adb5-8c15f83a9e40 | -10.42136 | -48.17337 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7eb8a82c-9ca6-3417-9269-91ba293e3edb | -10.42082 | -48.17689 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2057af1f-b633-3a82-b6cc-fcdaf11c2b67 | -10.41751 | -48.17633 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eb887c34-be3a-329b-8de9-a78c6b1ad0d9 | -10.41696 | -48.17984 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5da9d105-9665-3987-aee4-7bc9339eab9b | -10.41642 | -48.18333 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac3730e3-e3a8-3de3-b9eb-048036ca4335 | -10.41533 | -48.19032 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0787a417-0a70-3cce-8931-d49b31b49131 | -10.41366 | -48.17927 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dca79df6-c3a5-30c6-9f47-4d84be2e3e5d | -10.00847 | -48.23012 | 2024-09-30 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bec608f2-fc6a-36da-912f-be25db0b8b69 | -10.76438 | -48.73789 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c340e73b-e4da-3a70-ad0d-cf1991fcbdf7 | -10.76383 | -48.74139 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8ff5bdbe-75fd-3b7f-a7e1-c53f88fb9a00 | -10.76328 | -48.74488 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b65739ee-adc4-3882-a581-98ec0724d807 | -10.76273 | -48.74838 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6ccfc6f3-fd33-38a1-89c7-f1231d1ef530 | -10.76218 | -48.75188 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 58bb5051-6a85-3fa7-8f6e-8ebbf4e45808 | -10.76052 | -48.74086 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e79f42ab-7412-3485-bb6f-b21fd7027e6c | -10.75997 | -48.74435 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e3a03bdb-1682-36bf-a533-aa906bc8b6e5 | -10.75942 | -48.74785 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8415d7a9-c26b-3a98-be84-67d6f1c150a5 | -10.75887 | -48.75135 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 41481cbb-c076-35df-a7d6-60febb00886e | -10.75832 | -48.75484 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8d2e5977-001d-348e-9034-2d36d5b297d8 | -10.75666 | -48.74382 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4799e0b1-f2b8-3370-a0cd-15f9802c8d26 | -10.75557 | -48.75081 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README40.md)
