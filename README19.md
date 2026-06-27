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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6467ac08-cd36-3e5c-9e9a-e0d7ae80095f | -21.77858 | -56.28447 | 2026-06-27 05:23:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a986fcdc-9eef-3336-a5c8-08093d57c870 | -21.77809 | -56.28876 | 2026-06-27 05:23:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c8615176-f288-3927-8ec6-b6d80854d347 | -21.75882 | -56.26908 | 2026-06-27 05:23:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b48b5244-f353-3c41-a59f-4baf45ec7573 | -21.75459 | -56.26844 | 2026-06-27 05:23:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d25d3040-630b-3f56-a8c9-5d5395b5a8ab | -21.75507 | -56.26428 | 2026-06-27 05:23:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 8.8 |
| cfc638ee-4e5a-3161-92a3-fc699592ff3b | -12.4654 | -58.481 | 2026-06-27 05:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 51d0c05b-124f-3589-847b-1bef77bd1f06 | -12.4651 | -58.5009 | 2026-06-27 05:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 55c2065b-60bb-36d9-aa9f-361fc2fa9d2d | -12.6046 | -57.8942 | 2026-06-27 05:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 40.8 |
| eac4325c-a29f-38bc-9d68-db10849c8327 | -12.6236 | -57.8926 | 2026-06-27 05:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| c86a4b6d-1298-3d65-9552-319d1eb794bf | -12.4654 | -58.481 | 2026-06-27 05:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| ef5ddf05-e116-37e1-9973-a89214c7f3d5 | -12.6236 | -57.8926 | 2026-06-27 05:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| ef5bd148-2ca4-380a-8dfc-560210049571 | -12.4651 | -58.5009 | 2026-06-27 05:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 91f0d55a-fb4b-3370-a412-a6f00c1a8419 | -12.4651 | -58.5009 | 2026-06-27 05:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 3b18b216-cf6c-37da-b296-113288a751ca | -12.4654 | -58.481 | 2026-06-27 05:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 8c414802-dbe7-3572-ab1a-5a62af161b35 | -12.6236 | -57.8926 | 2026-06-27 05:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 42c50bbe-a42f-3669-af4d-c4259f6519f5 | -11.91965 | -57.41546 | 2026-06-27 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 89000965-550b-3cc3-aba7-e7773267c806 | -11.90384 | -57.40977 | 2026-06-27 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 626c9459-919f-35ce-8625-cf25c3f373f9 | -13.22421 | -54.42235 | 2026-06-27 05:53:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f161811-09f2-3f52-b0e7-698e62fcce96 | -12.62485 | -57.89363 | 2026-06-27 05:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 91f07bdc-7745-3257-a69f-2044c66569a4 | -13.25934 | -54.4093 | 2026-06-27 05:53:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6fe661fa-49f9-36a6-9ddc-9cb37549f774 | -12.93667 | -56.6451 | 2026-06-27 05:53:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebb9be5d-a2ff-3ecc-9229-a187f037fb49 | -14.87305 | -54.53952 | 2026-06-27 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2df07398-909e-3325-aa17-a50fa76f85a0 | -11.91465 | -57.41136 | 2026-06-27 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f4bf9db-dbab-3b9c-b2ea-a2af0cb81c5e | -12.6049 | -57.8809 | 2026-06-27 05:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 804a384d-df49-3630-9f9d-ca359dc01f5f | -12.4591 | -58.48925 | 2026-06-27 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c334e33e-c2da-3507-af61-73cd693b94e3 | -12.60449 | -57.88418 | 2026-06-27 05:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1aa889a6-e9f7-34e9-8705-dc4e7a5f2165 | -14.87122 | -54.53708 | 2026-06-27 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 72d47581-81d4-39b7-afd3-7ef807c19c5f | -13.24539 | -54.41345 | 2026-06-27 05:53:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3171441b-18db-311e-946d-9767e93daee6 | -14.87185 | -54.53121 | 2026-06-27 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 24d424d2-d6ad-39c0-abfe-1123079b9219 | -11.79372 | -57.34912 | 2026-06-27 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 45aa8a3b-718e-36e1-9121-0574800ff94d | -13.25871 | -54.41496 | 2026-06-27 05:53:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2db670b7-5257-311d-a8de-5f727fba24c2 | -12.93231 | -56.63218 | 2026-06-27 05:53:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d778d33d-f873-35c7-a265-172821fa471f | -2.32275 | -60.06278 | 2026-06-27 05:53:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dea2c82e-fb6c-3328-b814-7e28b476b029 | -13.25205 | -54.41417 | 2026-06-27 05:53:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1125dfc6-7776-36c0-84e1-aaa38805e35d | -12.79493 | -54.87128 | 2026-06-27 05:53:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff31dfa0-d9df-37e8-b558-3dac29857aa7 | -12.45834 | -58.49508 | 2026-06-27 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 28fe344b-0a8a-3a2b-87c8-82a58bd40c73 | -13.26328 | -54.41 | 2026-06-27 05:53:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1512055-85a3-34d9-b977-8d601c3b1bd5 | -12.93261 | -56.63051 | 2026-06-27 05:53:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7342eb37-0f50-3796-a378-37012a497fe9 | -11.90924 | -57.41059 | 2026-06-27 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 653388d4-3b36-3046-b703-929096d53a2b | -12.60897 | -57.89149 | 2026-06-27 05:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7722689c-449e-3b6b-b1e2-017d785e5030 | -11.7927 | -57.34978 | 2026-06-27 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14880841-277e-3d83-9271-283712d0fa4c | -11.87451 | -57.81943 | 2026-06-27 05:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 24ebece3-a0c4-31b1-8dcc-cf6ee8e71099 | -12.45797 | -58.49799 | 2026-06-27 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 16.8 |
| abbaa8e2-afde-3286-ab07-06e5fc9fbe86 | -12.93689 | -56.64338 | 2026-06-27 05:53:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4785ac8-c6e9-3102-8685-4847702ed88a | -13.66696 | -53.93688 | 2026-06-27 05:53:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4f643f92-ca46-3fc5-a661-ae49e4733882 | -12.61426 | -57.89225 | 2026-06-27 05:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8f95f2a8-3f9a-3db7-ab1e-6963543e6fe3 | -12.94215 | -56.6482 | 2026-06-27 05:53:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a01ba637-d3a5-3cf6-b7f1-ce922d0ecd0c | -12.62525 | -57.89038 | 2026-06-27 05:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| d575da25-a5a8-3cf5-8f45-5587d985fe9d | -11.62472 | -59.08214 | 2026-06-27 05:53:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02447ebc-f1fc-36b9-9bb5-be20f7de7d43 | -12.79403 | -54.87066 | 2026-06-27 05:53:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f0ea2f7-a75b-3c99-ba3d-b0b35c16f3e4 | -11.87979 | -57.82 | 2026-06-27 05:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4aef6993-6d21-3bbf-ae13-add7a66de1ec | -14.87424 | -54.52777 | 2026-06-27 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c55f105d-f9f7-3858-b789-cd5df51cf2ea | -11.87492 | -57.81617 | 2026-06-27 05:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e614ae79-c699-3fe9-af64-401f5166f08b | -13.26268 | -54.41572 | 2026-06-27 05:53:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8f2429d-6520-3d8e-9262-3c0daca71739 | -13.65943 | -53.94246 | 2026-06-27 05:53:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dc5913df-6324-3974-b705-9c21246fad4d | -14.87365 | -54.53366 | 2026-06-27 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cf8662eb-5f6a-3681-917d-fdda48d528cc | -11.90882 | -57.41402 | 2026-06-27 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 69b9f4d2-ff0e-3e35-a383-d1cf24f7efcc | -12.45365 | -58.49149 | 2026-06-27 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e3b33ad0-4bdd-32f8-ac43-4bc49e83343d | -12.61874 | -57.89944 | 2026-06-27 05:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9b45849b-79c4-36d9-b11d-0ea6463a5919 | -13.22359 | -54.428 | 2026-06-27 05:53:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5eb23910-2836-334d-ad34-6db1e79c475c | -11.79224 | -57.35334 | 2026-06-27 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f20b7778-926a-351c-899f-438a331761e5 | -12.5992 | -57.88345 | 2026-06-27 05:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b97dab8c-bf53-3632-b2d1-44153a839936 | -13.66646 | -53.94363 | 2026-06-27 05:53:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 779632c5-9b0b-3d9c-9d9b-0b05ab548e97 | -12.61914 | -57.89624 | 2026-06-27 05:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 318ea476-2e2e-33de-99b3-da0e3107b143 | -12.17097 | -59.76039 | 2026-06-27 05:53:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e24f72b1-779d-36cb-9f52-d22c183c5153 | -11.90967 | -57.40712 | 2026-06-27 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cca5c48f-a97e-3d0e-b6b9-5f3c66f0c660 | -12.93212 | -56.63447 | 2026-06-27 05:53:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd0b69cd-8bc4-3e0e-977c-1976db178fe3 | -11.91508 | -57.40791 | 2026-06-27 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 057deb7e-2f99-3fa7-920f-6d47f132f305 | -11.90341 | -57.41323 | 2026-06-27 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f477ffd9-99b5-3e13-bd4d-3ec473ce732a | -12.60409 | -57.88746 | 2026-06-27 05:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4632972e-497a-3420-a656-588b1b87a63f | -12.46379 | -58.49287 | 2026-06-27 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 23.7 |
| f204ab3e-9f92-3bf1-a20d-a8d650465a16 | -12.61507 | -57.8857 | 2026-06-27 05:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c5ad88c4-eb74-3acb-bbb7-f102627ea289 | -12.93639 | -56.64738 | 2026-06-27 05:53:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6cc34b09-e073-3834-a968-aae268a4652a | -12.61954 | -57.893 | 2026-06-27 05:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 3bcd2712-5d53-3bda-b3f6-d1f7b0fdcf4b | -11.91423 | -57.41477 | 2026-06-27 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3a037fb-2ca3-3700-af6d-60f0a2df2ea0 | -12.45402 | -58.48858 | 2026-06-27 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95cced94-df64-336b-bfe4-0577d1efd30d | -12.79551 | -54.86599 | 2026-06-27 05:53:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c7f7ab3-e10c-3e2f-bdac-6199f85057bf | -11.88021 | -57.81674 | 2026-06-27 05:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4561f569-9181-3b6c-a355-34b36bf0f960 | -13.60578 | -56.59671 | 2026-06-27 05:53:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cadaf440-b437-3fee-b42d-b8ef05644301 | -13.64686 | -55.29951 | 2026-06-27 05:53:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2f46bbc-eb5f-3f1c-a627-130fdf12cc1f | -12.9376 | -56.63705 | 2026-06-27 05:53:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c1467f2-ae4b-3bd0-9195-7dca7547b50b | -11.79328 | -57.3527 | 2026-06-27 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ddbc483-29ba-3f42-ab26-f8d25d6d0429 | -13.25268 | -54.40856 | 2026-06-27 05:53:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e1a7cfd9-88ec-3127-99c9-c0cfdaeaf23c | -13.24601 | -54.40783 | 2026-06-27 05:53:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c798d19a-26ec-3f26-a57d-6c4456cf95f8 | -12.19185 | -64.35914 | 2026-06-27 05:53:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| baba2e81-951f-3036-878c-3203b48155a1 | -12.94244 | -56.64592 | 2026-06-27 05:53:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f07a4f45-8d80-3479-b058-e98880a2365a | -12.93277 | -56.62816 | 2026-06-27 05:53:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfc8ebed-24c6-3194-afd8-13d8ecbd64ed | -11.78787 | -57.35184 | 2026-06-27 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c54f362-b6cf-355d-87e0-071d2a727e44 | -12.79464 | -54.86541 | 2026-06-27 05:53:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25172f5c-5198-3b35-9825-3a6dabf1536d | -12.61995 | -57.88975 | 2026-06-27 05:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 0b0e3cf2-cb6f-3fa9-a513-7b0d123ef9ed | -12.60938 | -57.8882 | 2026-06-27 05:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 50d9c093-eda7-3743-b97a-997c6722700c | -11.90798 | -57.42078 | 2026-06-27 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a5a9e88c-ec01-33db-9afc-ea1cab1c0c00 | -12.93738 | -56.63936 | 2026-06-27 05:53:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f1c7d2f-80c2-308e-83cf-4e143f3c8436 | -13.60529 | -56.60094 | 2026-06-27 05:53:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4c13482-0814-3f76-868a-b9c8ad04d87a | -12.46304 | -58.4987 | 2026-06-27 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 16.8 |
| ec48cbc3-a689-35ae-933d-c9c12202056e | -12.45328 | -58.49439 | 2026-06-27 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b772ad48-7ee5-3fff-afe5-e6fefc0d7d2b | -11.91381 | -57.41814 | 2026-06-27 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a47b7862-bf71-35ea-bd9c-1a436c3a4e80 | -12.93714 | -56.64108 | 2026-06-27 05:53:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e560064e-d00f-33b3-b659-acb7c3356afd | -12.46455 | -58.48701 | 2026-06-27 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 10b35bc9-e348-3fbb-86f0-7a73deba407d | -12.61466 | -57.88897 | 2026-06-27 05:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |


[Clique aqui para ver as próximas entradas](README20.md)
