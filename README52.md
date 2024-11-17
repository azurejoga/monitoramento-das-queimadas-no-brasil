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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1df77406-079e-3a8e-8667-d6037fa64770 | -2.07958 | -48.52349 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 754c4141-b91c-3e76-98c2-bde93d4ad766 | -1.57429 | -47.14548 | 2024-11-17 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6d7977f-b0af-3e65-90f1-d60d37d17d53 | -3.8097 | -46.51868 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4070ada-4f63-3266-843f-64ac9525c4aa | -2.22959 | -53.61388 | 2024-11-17 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 28ec1bf5-c4f4-33ad-932d-98c45ed07c64 | -2.60948 | -46.17898 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cd238bad-8117-3af5-bb82-7d44a6f70aae | -2.19684 | -46.51517 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 84820f72-02a5-3ca4-8797-cfafcb2465c3 | -1.7968 | -48.44654 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94fde724-aff5-3b77-bef3-66e2117e7627 | -2.67423 | -46.22134 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a563ff90-33b9-38fb-8a2f-ab40e4f5526e | -2.30958 | -48.46672 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9040fbc8-4d0c-3415-aaf1-c78850c2de2c | -5.03316 | -44.86329 | 2024-11-17 04:29:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 88c760dd-c3ab-3788-8af2-b32a90f2b846 | -1.75351 | -46.3505 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5e84818-b60a-3467-bb11-bdffbb2aca5d | -2.10903 | -48.29569 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0575632a-156b-3fa0-9a72-45419bd17ce3 | -1.29455 | -51.96363 | 2024-11-17 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| bae485a2-c901-379b-abe0-2bd9ceec791d | -5.67051 | -46.49751 | 2024-11-17 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65accd50-c1b8-38a0-aeaf-4b8b67779865 | -2.35357 | -48.42938 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a54edeb-32d5-3286-ac0e-8dee13886a0d | -2.36803 | -48.53508 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c769d109-0e85-3215-9ef8-1280f7ffa100 | -3.95515 | -46.71861 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 22f475c4-463d-3a3d-8719-47a8d4d68429 | -3.45465 | -45.77217 | 2024-11-17 04:29:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6bee974a-f02d-36b7-b2ec-2de4f0084ebc | -4.37119 | -48.091 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c16de06b-242f-3357-a4c0-6c80acb6fd1e | -4.46791 | -43.77423 | 2024-11-17 04:29:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5746db89-f679-36d9-b7d8-d079be85529d | -1.28132 | -46.69858 | 2024-11-17 04:29:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 45a36f7b-5668-342f-a489-b87a7b53de0a | -3.45851 | -44.53995 | 2024-11-17 04:29:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2930e2cc-a14f-322a-b2c7-0d3e607c94c8 | -4.02304 | -46.54449 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 022842fc-d2f5-3238-a34c-72cce8d973e6 | -1.05009 | -51.74343 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18d59bb2-e462-3235-86b1-aa8da6bf75f8 | -1.12326 | -48.36121 | 2024-11-17 04:29:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 567c6a5a-8e84-3f54-b9f8-2a153fcd500e | -2.00713 | -47.46041 | 2024-11-17 04:29:00 | NOAA-20 | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7c86c427-1147-3e6d-9f13-619e76d86003 | -3.69341 | -43.51458 | 2024-11-17 04:29:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b97086a-f922-3ccb-85bf-e588ae13abb4 | -3.84928 | -46.63503 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7795aec-2c84-324a-bdbc-fb55d2ffba73 | -2.55319 | -45.77923 | 2024-11-17 04:29:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 317cd437-6c2a-3ef2-9754-21e88374aa66 | -2.10167 | -50.36887 | 2024-11-17 04:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef2ca402-7df7-3063-ab8a-9e6113cc8a11 | -2.71092 | -46.07357 | 2024-11-17 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| efac537f-fe39-3162-8c25-08e282ca6646 | -3.61111 | -44.79271 | 2024-11-17 04:29:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f0a8bd4-601a-3852-a024-a895440e00c0 | -3.97388 | -46.70735 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e59c7ca-98c9-3bcf-bbf3-ffbd1793d860 | -4.54083 | -45.25242 | 2024-11-17 04:29:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| bb6566a1-7acc-3d5d-a92f-fa4bdcbccf18 | -3.96231 | -46.71619 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f762413-c1f6-376d-a4bb-efa71eea9021 | -0.83317 | -52.3407 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7783760-1448-3783-bd8e-c0ba46a4457e | -2.63446 | -46.56224 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30d381da-ab60-325a-bd47-42dd6a2a634b | -3.71375 | -51.84183 | 2024-11-17 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 35b9239b-eba9-336b-a4bc-204b82decb0b | -3.98084 | -45.96942 | 2024-11-17 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 169f5c09-2a6f-3839-8677-ebc3ec3a058a | -3.34588 | -53.30874 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 93206d1d-1859-357f-bafb-6a4aec1a3a5e | -2.22628 | -53.61446 | 2024-11-17 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 786c0fd5-8157-3c8b-b119-2a02e7923e6c | -1.56381 | -52.29156 | 2024-11-17 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8b1daad2-eb82-38c5-969d-3d864f98a6b0 | -3.61019 | -44.23407 | 2024-11-17 04:29:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bbd53f11-a3b3-389f-8138-a1be6752d136 | -2.67646 | -47.89238 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9a727d58-0dca-3e84-a174-5d8633f66a9a | -3.50276 | -51.02258 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b6f3fe6-2c06-3ba2-8001-fc3147e2d1fe | -2.60284 | -46.17795 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fc299e4-16e3-3015-9f9e-9eb4ec91164a | -3.10235 | -45.98273 | 2024-11-17 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4063330a-9f70-3957-a5c7-dff3c3bc4005 | -2.13213 | -49.50637 | 2024-11-17 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f708429-a311-38af-9204-4c03c2465271 | -2.63169 | -46.55828 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5f25bed3-32e8-334c-968d-823e293ff07b | -4.13065 | -46.09396 | 2024-11-17 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 552265d2-d99f-3cdc-b08a-87dc4ada5149 | -2.61172 | -46.18644 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e02ef207-e59f-37b0-acc6-493a4d3e5f49 | -4.00745 | -49.01254 | 2024-11-17 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b712240d-d04e-3cdd-8e06-ee5800b014e5 | -5.40484 | -46.35139 | 2024-11-17 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55a181ea-d570-3b33-acc4-c48f982da386 | -2.12182 | -48.78503 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be6755c6-aec9-395e-87a5-9eae6832cc72 | -3.69876 | -51.08267 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c21c1880-8473-37a1-abf3-96fb2b8d1cb2 | -2.90567 | -48.31026 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22b63bf6-64d0-3791-adcd-24baab30d722 | -1.39388 | -51.99451 | 2024-11-17 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 19a40c8c-b538-38b1-83d2-91a38b7e01ad | -2.36603 | -46.43155 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 812fcb27-4b29-3cca-91d2-bb4a6f92c0f8 | -3.01586 | -45.39884 | 2024-11-17 04:29:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ced4b104-d545-3166-965e-b1bc16512a95 | -4.21903 | -47.22259 | 2024-11-17 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a72a814-e972-3412-9b53-591de86f35d6 | -2.43165 | -48.7762 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be4212d7-5a66-3e52-b894-296a08f9a2ba | -4.53671 | -43.28957 | 2024-11-17 04:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0dd0d06-0879-372f-8abc-ab4abc393ec5 | -2.64951 | -49.75754 | 2024-11-17 04:29:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e795ef3-aa46-3596-8416-c8746a591c8f | -3.53024 | -50.25749 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| d9756273-1093-3f01-87f0-2515a51f73b2 | -2.65162 | -46.21397 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 13007d1e-c875-33a4-ae3a-ccc30324ee7f | -1.52926 | -53.5605 | 2024-11-17 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6e66971a-4e4e-3243-8400-ae501e97c88a | -2.39875 | -47.92809 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 813a48bb-5eb7-36d4-a04b-242b3f71f276 | -3.68859 | -50.12188 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf7ae760-5cf7-37b0-8f81-eb597b9c11ee | -4.63298 | -42.91091 | 2024-11-17 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7d1f7b1f-87c1-3c53-843f-ab16f4471509 | -2.63932 | -46.53123 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b353236-48e2-3d81-bbd3-b4b8fe11c94b | -0.9904 | -51.77833 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28a6d04c-bb21-3980-8c4f-99b5800ca589 | -1.66765 | -47.97572 | 2024-11-17 04:29:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 35dae5d9-e58f-3beb-940e-9218bc2dff1a | -3.58055 | -53.72393 | 2024-11-17 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb88269c-bd87-312a-9b3f-ac907fdccf44 | -2.37095 | -47.93424 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8207732-f427-3194-a70f-c08880ef049d | -2.19737 | -46.51173 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 58e4f8ab-c09e-3cbf-9804-1c554ec70b7c | -0.11892 | -51.6244 | 2024-11-17 04:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 142de5a9-1b6e-3627-b5b4-65f3a722295b | -4.06814 | -46.8636 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a81691e-5ce8-398b-89ac-1636b4c5bd21 | -2.21538 | -47.2174 | 2024-11-17 04:29:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 0c3fd8c7-6843-363d-bb6a-1436e028838b | -4.15019 | -50.7647 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7a49413-5322-394d-8f93-c6f49e558677 | -1.21378 | -51.78809 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31358b51-113c-30d8-9547-a1df5e8cd193 | -1.32608 | -51.86843 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f0a9f457-618e-33f8-a2b0-ed0bb1b4d2e4 | -4.249 | -49.19227 | 2024-11-17 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4be2b2fd-9f90-329f-9295-932cf7c570f8 | -3.18171 | -46.53791 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d0613af-22bd-39e3-8d2a-dc35974db5d9 | -4.20287 | -51.03889 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38edb42b-c06f-312f-bd22-6df89a1bcd00 | -4.2746 | -48.20742 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f6ce5ca-e37c-3c7f-9c08-33699f5334c0 | -2.67972 | -46.20794 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ee517e70-57cd-3820-9d40-d861d6e9d7dd | -2.09097 | -48.26708 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 3b1ce140-35aa-3885-bf94-cdc0c9e54788 | -1.81021 | -47.35143 | 2024-11-17 04:29:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 250b2814-4a6a-3337-9c02-71127df3a1ad | -2.53381 | -47.31014 | 2024-11-17 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbffd52c-cecc-3e61-9806-2e159d3053dc | -4.72239 | -50.84002 | 2024-11-17 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6410395-4587-32cc-900a-280883ad9066 | -3.41218 | -45.86784 | 2024-11-17 04:29:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3fb9c60b-78c1-3e24-b1d3-0c33300a9f35 | -3.34085 | -53.3123 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 02d2042e-8ea1-3643-9612-9bf9a8577009 | -4.59338 | -49.62814 | 2024-11-17 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af5cb5db-84a5-3163-b556-cf360d0b108b | -2.8794 | -46.64597 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1fe1df2-c20e-3b86-b590-67b996c41bea | -2.67913 | -46.84044 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5dfdf337-88fc-3af1-8b2b-9c9f2482dad2 | -3.76191 | -54.56727 | 2024-11-17 04:29:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb5447b2-2924-3fc0-bed0-04feb65bb98c | -3.2529 | -46.53833 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b28c563-b13b-3a07-88cc-0063ab774b55 | -2.82602 | -46.66236 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0ca1a787-898f-3bc7-b4db-f01c508e892a | -2.66758 | -46.22031 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 09515218-7fc5-3600-a127-57d78c3ce019 | -2.96265 | -54.31627 | 2024-11-17 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README53.md)
