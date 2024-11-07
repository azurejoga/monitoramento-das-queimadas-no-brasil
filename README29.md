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
| c4573dc8-2dcd-31b8-be71-15716789c360 | -4.18236 | -49.78043 | 2024-11-07 04:18:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a50b7244-6aa6-39d6-bf05-c7bc9c84cdf9 | -4.37856 | -47.24453 | 2024-11-07 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21feba10-b152-32a9-b16e-9f91d3b7dbfd | -5.37239 | -46.26004 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 630fedf9-fe21-316b-82af-175b507e7fb9 | -2.84539 | -51.77402 | 2024-11-07 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c8a402b-d631-3b0f-aa7a-ef3fba565665 | -5.11329 | -43.15144 | 2024-11-07 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e71fe2bc-9cfd-34af-844c-ab235c6cab9b | -1.40178 | -54.49699 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 914de310-6c40-33d5-b912-6f5492693e11 | -3.04316 | -49.53381 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4308386-76a9-3c56-a7a6-e7d1654b0cf7 | -6.04372 | -46.60367 | 2024-11-07 04:18:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 70639baa-f4b6-3494-8d4f-41b632c38b2a | -2.75704 | -53.22344 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0298645-b984-3ba1-9347-448ab5e8c8c1 | -2.72687 | -54.14843 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 20134c5a-1b96-30fc-a33d-d0e7e428422f | -4.708 | -43.79517 | 2024-11-07 04:18:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 43bd5767-86c9-3f2f-821b-02e349500fd2 | -4.67951 | -46.38358 | 2024-11-07 04:18:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c705dde8-229e-3de4-9113-57724fb10cba | -4.92792 | -43.62622 | 2024-11-07 04:18:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83ae8822-f25d-30c0-81c5-3dae37bdb186 | -5.4505 | -45.52907 | 2024-11-07 04:18:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 088bbb6b-54b1-39f5-91fb-3842e1e2f721 | -5.96566 | -45.3665 | 2024-11-07 04:18:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f92864d-6e0d-3db0-abea-1cd98513eca4 | -2.81353 | -52.91806 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 783fb61a-8b55-3a23-937d-ef1d8c69f5b4 | -1.52759 | -52.22529 | 2024-11-07 04:18:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 364a2b65-aa29-32a2-b552-00318081f279 | -2.04704 | -52.08924 | 2024-11-07 04:18:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 279a5daf-589d-318a-910e-47832cfdeb97 | -2.67508 | -51.83288 | 2024-11-07 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f34f616e-88aa-3664-9fee-95304273e338 | -3.70628 | -51.38907 | 2024-11-07 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 58e331e8-b812-3476-92aa-5975c8423743 | -3.6074 | -52.52575 | 2024-11-07 04:18:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 280c621b-d8e0-33d7-8f36-cfb2fc891a88 | -1.14816 | -53.74311 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dbbbfd17-4652-3b63-aff7-344a44ae7a98 | -2.06075 | -48.13751 | 2024-11-07 04:18:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3598d678-474d-368e-990a-63d3c06e8d0a | -3.77772 | -47.73603 | 2024-11-07 04:18:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c6d826f3-bfcc-3ea9-8e0b-8201d86f393c | -3.56744 | -52.69841 | 2024-11-07 04:18:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f647f5d3-7735-35aa-bdfc-eb18d1789a79 | -3.54243 | -47.35985 | 2024-11-07 04:18:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8027463-ec7e-393f-b89e-25c1d70a7540 | -2.12899 | -48.1834 | 2024-11-07 04:18:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb63a44a-34f5-3052-b490-63be385bde03 | -6.55004 | -39.67025 | 2024-11-07 04:18:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f5430761-e4e8-3a92-8bad-9c0709aa8d21 | -4.77149 | -45.56663 | 2024-11-07 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8de46877-36fb-30dd-8d53-22bd744b7f40 | -6.48365 | -44.68892 | 2024-11-07 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bb1354e6-fee9-30da-97f0-cc5d2587e84a | -6.27982 | -44.73463 | 2024-11-07 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 442e0e4e-74c7-321d-9e5d-3aaf9d2be5e5 | -4.73489 | -43.25275 | 2024-11-07 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fac3c8fb-ba21-3667-8fa0-9f61a65b6ed5 | -2.30788 | -48.54511 | 2024-11-07 04:18:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b51e1e17-b7f7-39ee-bbd4-c68a7f1d9478 | -5.06755 | -44.23307 | 2024-11-07 04:18:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 024e571d-ec81-3021-a7e2-093dab840d53 | -5.97562 | -45.36805 | 2024-11-07 04:18:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 528aadbd-ba24-3a83-b159-798e1e471936 | -3.0154 | -53.4393 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54f6fbeb-1f11-3d9b-a375-fb5cb92bc151 | -8.50015 | -42.08691 | 2024-11-07 04:18:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 42855735-919d-31e2-b647-e1c241b60238 | -3.22019 | -50.38041 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7861e07c-ff48-3de1-b03d-4f5c12a71e6b | -2.88542 | -49.38071 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d77222a3-78ce-3d25-91ce-f13b93e8c706 | -2.95022 | -53.28844 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0595103-1b4e-3199-8ac7-8d8c300be1b2 | -2.65716 | -49.88024 | 2024-11-07 04:18:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d3f64532-0a9b-3650-8359-7139ebc6a513 | -3.18226 | -50.58171 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c41eac0e-a710-3f7b-add3-bd96011323e4 | -6.96407 | -39.82334 | 2024-11-07 04:18:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 47960d8e-43a6-3958-89bb-5f9625ce610c | -6.23373 | -45.32644 | 2024-11-07 04:18:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab2d809e-df40-3b6d-af67-80e96af9f4b7 | -2.85066 | -48.44489 | 2024-11-07 04:18:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c030c7c4-ccce-35ca-83c3-bbe795408e10 | -5.37579 | -46.26059 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2d644d7a-800b-3c82-a7db-e5b3a8dbdb18 | -1.14874 | -53.73941 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9d5c0fc4-2dc8-33cc-a6ef-37abd45c7d31 | -2.04858 | -52.08776 | 2024-11-07 04:18:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0bb6c70d-27df-3251-ac0b-90ba50884603 | -3.25294 | -46.46998 | 2024-11-07 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09f2b6a7-4436-361c-9112-9780005e42ec | -6.50936 | -44.67917 | 2024-11-07 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39583929-b2db-34ec-ae5a-efa11e6806b5 | -2.86369 | -50.32944 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b57cbd3-e06a-346a-8711-b65316a61af6 | -2.52821 | -48.20121 | 2024-11-07 04:18:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0b3ecf0-dbb9-32c5-8c87-dd3f85dd37cc | -4.74271 | -44.41768 | 2024-11-07 04:18:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c50ce938-e2d7-3991-8110-952d1e156680 | -5.10964 | -43.96412 | 2024-11-07 04:18:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d6e4f84-e8f5-3a8d-b32f-d2655773a2b6 | -4.22957 | -48.54125 | 2024-11-07 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77d62bc1-9dc3-34e5-b752-0a13aeff86ba | -3.01575 | -53.43235 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42919cd0-e770-30ea-87a9-b1a52499fc04 | -2.40701 | -48.43174 | 2024-11-07 04:18:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf1b4cd2-fc55-3503-b819-6b386a8ff0cb | -7.74184 | -40.47462 | 2024-11-07 04:18:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a1427ae4-e718-3fc6-93c6-12494df1ff92 | -2.83741 | -49.46622 | 2024-11-07 04:18:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f7c6a24-c726-3692-bd4b-68ee0627d33e | -3.0374 | -53.27742 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b499764-4d6a-3c9a-9ff5-b98ea9de516e | -3.20178 | -50.63095 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 562de2ec-a430-3544-a9ec-580f1e456d5c | -3.38403 | -51.24664 | 2024-11-07 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dafe2b11-e268-3899-a141-598aa43bf90d | -4.70812 | -49.60791 | 2024-11-07 04:18:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34cb0dea-995b-3ccd-b79d-85fae3ca797d | -2.92807 | -49.34151 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 367eb422-fba6-3a62-a335-e76c7fe960a1 | -5.07224 | -45.51234 | 2024-11-07 04:18:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 872172f0-dec9-3807-bf54-05c7945c7fb8 | -4.50902 | -42.86531 | 2024-11-07 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 30a9f1bd-8f9e-3dc6-bdd2-44e3da400290 | -2.04811 | -52.09074 | 2024-11-07 04:18:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae56d73b-119c-3127-aa02-6146af4a85f4 | -5.22897 | -44.91138 | 2024-11-07 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e6dbd6d-4eb7-3196-b631-0b546577d39a | -2.60393 | -51.76311 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6e1b44f2-db56-3913-8df7-e3fa1fce5259 | -4.34913 | -48.62954 | 2024-11-07 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 999d1372-6c1f-3ce9-af58-a53f9e5a4041 | -3.76345 | -50.00782 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47cf5e95-7bd0-31a4-a84f-93f340350473 | -6.05056 | -46.60481 | 2024-11-07 04:18:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 70155a61-de11-3099-a4ec-3ef78d0ec66f | -3.80653 | -50.00467 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5003272-7d5d-3c85-b869-24f7ff410237 | -3.47724 | -49.68832 | 2024-11-07 04:18:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8c842cea-8ac0-32ec-9b93-e86f381045e2 | -2.40309 | -48.43109 | 2024-11-07 04:18:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e813e114-6fc5-3ced-b685-e0fb707486b7 | -6.29088 | -47.20556 | 2024-11-07 04:18:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69311b4d-0a51-35ec-99f9-956121cde9d0 | -2.75764 | -53.21985 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c1e60293-7c74-3c4e-95c3-4853a981af72 | -5.44579 | -47.6845 | 2024-11-07 04:18:00 | NOAA-20 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a11ead6d-a4c8-3a1e-b246-7379df74d7b7 | -7.04215 | -47.62494 | 2024-11-07 04:18:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c7deb855-ffcd-3c5e-abf8-a02d5226a8b9 | -1.2806 | -54.13853 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f7cd15c1-30d7-35a6-8a3d-7326a7a4e03d | -3.2913 | -50.08452 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c0a86fb0-c5bd-3693-ac2a-5197ec805a76 | -2.81994 | -52.91221 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f49c51f-a409-30ee-88bf-a7f48ca57419 | -3.21278 | -53.10603 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 910d800c-ccec-378f-a739-c2d1ef21faef | -1.40238 | -54.49335 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 32b54909-c5a4-3138-ab16-92e7d77d1adc | -3.35228 | -45.90895 | 2024-11-07 04:18:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1796e5c3-e2e9-3c10-bda1-797e4963c436 | -2.8453 | -49.44403 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e311b01-5c30-3f13-932b-7f3031a4795e | -3.5269 | -50.35322 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3812945-5bd8-38ea-b825-c42f3dff745f | -3.12731 | -51.11341 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4dd15e00-fb56-39a9-97bd-6b59aa13ac46 | -3.22531 | -50.37687 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cea95398-a71e-3617-af92-8ed74b2dbd89 | -2.59206 | -49.34351 | 2024-11-07 04:18:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 138f9583-a628-352f-9ec8-775d74b3aa40 | -8.31908 | -43.626 | 2024-11-07 04:18:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac67a1cf-3b6e-3a16-809a-39d817651996 | -7.54528 | -42.8454 | 2024-11-07 04:18:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2ccc5e9d-70a1-37f6-be49-e2fb99dfb56f | -3.45035 | -50.38023 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 760af726-f21e-346e-b89f-d473010feb8a | -5.05926 | -44.2212 | 2024-11-07 04:18:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 670ad335-dc44-3ca8-8a5d-d20b964bff44 | -8.30778 | -43.60948 | 2024-11-07 04:18:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e2a8a12d-6419-3122-823c-97fd1bc863dd | -3.24769 | -53.40509 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd399a12-6f21-3d3f-9b99-683399cbdad4 | -5.51101 | -45.31947 | 2024-11-07 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61091005-372e-3d64-bb69-de9c6b559639 | -2.0806 | -52.0434 | 2024-11-07 04:18:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 18075fc2-c7a5-387e-a383-b4c71e285d29 | -5.98669 | -45.36264 | 2024-11-07 04:18:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 44.1 |
| b51ca4c2-e133-3558-9d33-0fe5bcb2a6d1 | -3.28568 | -53.11708 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README30.md)
