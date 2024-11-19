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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 58e40938-9274-392b-b54a-58ebe765f8fd | -10.6986 | -48.803902 | 2024-11-19 00:28:00 | METOP-B | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 816d8d26-384c-30ee-81f0-f548fcec0c55 | -2.7825 | -51.716702 | 2024-11-19 00:28:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef3768c1-6e1e-34b7-ad55-7fbe356b0516 | -2.7808 | -51.7094 | 2024-11-19 00:28:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d26b2eb-fcb0-3f34-ab65-baf41f00248c | -3.8402 | -50.6922 | 2024-11-19 00:28:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8767380-3576-348c-a398-2cdd770d1562 | -2.6078 | -54.528801 | 2024-11-19 00:28:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83d82e0b-0bcd-3780-b47e-3a82b55673ea | -1.7552 | -46.310299 | 2024-11-19 00:28:00 | METOP-B | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e8b2b80f-c496-38ad-940b-f639f9c0109f | -5.1484 | -48.175499 | 2024-11-19 00:28:00 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ebbe30e8-7746-38a6-a21e-e12f05906276 | -9.2578 | -45.011501 | 2024-11-19 00:28:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 08e32c96-8b2d-3adf-b831-3adbe6e5d396 | -6.0365 | -44.032501 | 2024-11-19 00:28:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff284bb7-5894-393d-b2ee-406ad6c56133 | -13.2367 | -56.768398 | 2024-11-19 00:28:00 | METOP-B | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5d8d145b-1e83-36c4-9569-de5ba5a4a4ad | -3.7685 | -51.983898 | 2024-11-19 00:28:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4e3a92a-9097-30a6-999c-7a21188d7ee7 | -5.4476 | -49.684299 | 2024-11-19 00:28:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22b2b6c1-3ad3-3f2d-9ad8-cd7e25c0e4a6 | -1.4086 | -52.430801 | 2024-11-19 00:28:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a2ee324-189f-359e-a94e-a782e8abc573 | -6.036 | -46.5998 | 2024-11-19 00:28:00 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f3f07916-d169-3e44-b2c7-cb91a4837ec8 | -0.9948 | -47.993599 | 2024-11-19 00:28:00 | METOP-B | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c3af47c-2ca6-38c4-82f2-ede4d654ef86 | -3.3922 | -50.3484 | 2024-11-19 00:28:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03739d11-38be-3318-897b-75855d764622 | -2.7152 | -45.9618 | 2024-11-19 00:28:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b1854931-239a-39e3-9b7d-dd19908791d0 | -7.9922 | -44.368599 | 2024-11-19 00:28:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c05e8147-b03b-3848-b8e1-bed329b1c0ce | -10.9928 | -49.0186 | 2024-11-19 00:28:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a2ca6cde-850c-3267-a4bc-edbc5501975b | -2.6723 | -46.223999 | 2024-11-19 00:28:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d25cfd2c-5851-3905-82af-d44b756d02be | -6.2777 | -46.127201 | 2024-11-19 00:28:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 58a96a11-075f-329c-9740-df559863dd41 | -8.2597 | -44.016499 | 2024-11-19 00:28:00 | METOP-B | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2d21073e-b95d-3cc2-8651-f3c2ba58ce51 | -6.478 | -47.494301 | 2024-11-19 00:28:00 | METOP-B | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1749954c-8726-340b-afa3-2ea10c3c799b | -11.8737 | -43.800201 | 2024-11-19 00:28:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c8b6e03a-10fd-3139-958d-6ef8e7683293 | -4.1596 | -48.7701 | 2024-11-19 00:28:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa9d32e9-4699-384c-98a1-f7625082797a | -2.0158 | -52.062401 | 2024-11-19 00:28:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46cf6007-ab18-31d6-a5d9-70976efd655b | -3.6602 | -50.4408 | 2024-11-19 00:28:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a33ca757-23ab-31cc-aa9c-ed25dc000c3c | -2.9483 | -51.399799 | 2024-11-19 00:28:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ca04094-bb56-3a1f-b8e9-700de88fc42c | -4.1035 | -51.040699 | 2024-11-19 00:28:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43649900-1bea-3153-817e-19884f15cc7a | -22.3009 | -49.7472 | 2024-11-19 00:28:00 | METOP-B | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4e5199f6-0671-38b0-9eac-439e898c64d8 | -1.9344 | -46.509201 | 2024-11-19 00:28:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2dd0d6d-be82-3137-81cd-4aa07129aba3 | -3.3317 | -50.491699 | 2024-11-19 00:28:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a83a781-8bd1-3b4c-8135-6e5dc9c57ce2 | -2.8594 | -51.784302 | 2024-11-19 00:28:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9a4727d-8e24-3cbc-a83a-3e8a6a1b144d | -3.3332 | -50.4986 | 2024-11-19 00:28:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e4dd1d1-cc02-3561-b6ac-48d43e10bee9 | -2.3148 | -45.652401 | 2024-11-19 00:28:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 46d529bb-eb14-3ddf-aebe-a86966ea0881 | -3.0829 | -51.0354 | 2024-11-19 00:28:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf76191c-eb74-396f-8187-d9c2ce913f86 | -13.2541 | -56.8074 | 2024-11-19 00:28:00 | METOP-B | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 42d7a4f3-b714-3f3c-a2de-ea64928bcc7d | -3.5064 | -50.215099 | 2024-11-19 00:28:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60db2746-de16-320b-be89-4728e4ae3e66 | -2.6056 | -54.518902 | 2024-11-19 00:28:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 122ecdad-b7a2-30f9-bcf4-b9eb7fdd0419 | -12.2728 | -43.523998 | 2024-11-19 00:28:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5d299194-0284-36f4-96a5-31bdd3d55f74 | -3.3058 | -51.525299 | 2024-11-19 00:28:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06e66a60-7fc7-3952-94cd-dc52aa11b246 | -4.2142 | -50.6609 | 2024-11-19 00:28:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99ec8845-0291-37e4-a2d6-eeadf3a532cf | -2.6762 | -51.793701 | 2024-11-19 00:28:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b701d3f-8d0f-3daa-ad4d-07bd17a1cedf | -5.5765 | -46.440201 | 2024-11-19 00:28:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6b5998c9-26d3-3669-8c24-bb345bcfb54e | -3.4966 | -50.2173 | 2024-11-19 00:28:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68a928f2-c265-3aae-ab1f-15087867df7e | -4.9015 | -44.023499 | 2024-11-19 00:28:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1e13914e-cff7-3d77-b9cf-b5e41e27c8e5 | -7.9727 | -48.174999 | 2024-11-19 00:28:00 | METOP-B | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4b3925cd-decd-33c9-9626-fe913e372684 | -8.9527 | -47.6311 | 2024-11-19 00:28:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 057963cd-90ef-3a1f-b86c-cdea9f251c95 | -2.3448 | -48.9491 | 2024-11-19 00:28:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce1523f5-2623-38b1-ac09-472ce5d9558b | -3.7415 | -44.566002 | 2024-11-19 00:28:00 | METOP-B | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1202c000-1516-3f28-9d30-598b8f0dc87e | -3.1898 | -52.4338 | 2024-11-19 00:28:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81ed86c8-80e7-328f-8b8c-d9bec55774ed | -8.6611 | -47.9828 | 2024-11-19 00:28:00 | METOP-B | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e817a28d-ed44-388c-8ab6-28c9dd9602f2 | -2.7815 | -48.6021 | 2024-11-19 00:28:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c818cff-dd0b-3166-aae1-45b5076940b0 | -21.1933 | -48.555302 | 2024-11-19 00:28:00 | METOP-B | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e5069051-f01a-3c86-b4ff-eef65b430c49 | -1.0596 | -52.389702 | 2024-11-19 00:28:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c48a3b5-4011-39c3-99a6-f8b8977e61dd | -6.3053 | -45.2239 | 2024-11-19 00:28:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3782a164-19bf-30d7-919c-8b31943f1afd | -1.2403 | -52.048599 | 2024-11-19 00:28:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70d51f33-e7d8-3f7a-9b06-5152d3b868d1 | -3.3713 | -52.787399 | 2024-11-19 00:28:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bc3ef35-b870-3561-966d-b0df298e52c3 | -2.9499 | -51.406898 | 2024-11-19 00:28:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d236efc2-7e8b-39a7-a020-34d31dbba2ad | -3.4756 | -48.2537 | 2024-11-19 00:28:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| febba28c-0e7d-30d8-8619-0c5cd2d302db | -3.5398 | -50.409599 | 2024-11-19 00:28:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41040522-1700-3179-81d2-84da07fd367e | -3.3301 | -50.484798 | 2024-11-19 00:28:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e52bb41f-2896-3901-8d3a-fe18e5049acc | -2.2814 | -53.6171 | 2024-11-19 00:28:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28458a06-17a9-31ee-8b4b-ca5e015cce6d | -8.6725 | -47.987499 | 2024-11-19 00:28:00 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d894003d-7625-35f4-a1a5-3b94d5084d51 | -9.9725 | -44.714199 | 2024-11-19 00:28:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 55e9ebaa-f5ad-35f3-b5d3-80711d62d95b | -5.9755 | -45.356998 | 2024-11-19 00:28:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 31d05690-0d51-3670-88dc-aacc7c4ea6bd | -2.9716 | -45.330898 | 2024-11-19 00:28:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d63cf439-42d8-3280-a588-ff9ffe46ca69 | -1.8294 | -46.274899 | 2024-11-19 00:28:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| caddccad-e455-3677-b854-7456c6eb0cad | -4.2158 | -50.6679 | 2024-11-19 00:28:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40369ed8-3ee0-3e06-b927-a99c278b4af2 | -3.3203 | -50.4869 | 2024-11-19 00:28:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a05427ac-3300-30f7-939f-fd7e55884aaf | -2.9149 | -48.054298 | 2024-11-19 00:28:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc1cd995-5222-37f1-bd31-2b46098a1f6c | -3.4982 | -50.224201 | 2024-11-19 00:28:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96fe2fdb-fd68-39f9-b295-57a57fe114a3 | -11.1302 | -45.3386 | 2024-11-19 00:28:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 881431b1-5734-33d9-a023-b4979800de97 | -5.1499 | -48.182499 | 2024-11-19 00:28:00 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5563c5e0-3eba-3ca6-9051-15cb6c661142 | -9.246 | -45.005199 | 2024-11-19 00:28:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2dfaf121-8ecf-3e63-a230-e82e97cd53a5 | -3.508 | -50.222 | 2024-11-19 00:28:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b680dc5-0237-3c9e-9c5a-20f0e9156022 | -4.5447 | -48.013802 | 2024-11-19 00:28:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1ec47b9-57ff-304d-bf96-4eb8996c2f4e | -10.9612 | -44.440102 | 2024-11-19 00:28:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5c540577-3148-3ed2-a312-32eaf636dd22 | -2.5863 | -51.714001 | 2024-11-19 00:28:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a6a68fd-936a-3c99-a570-37c7fa1c2b9a | -2.7172 | -45.970798 | 2024-11-19 00:28:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7bd880c3-2280-30a3-807b-1c33b2beeaa6 | -5.9657 | -45.359299 | 2024-11-19 00:28:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 24172964-e9e7-31c4-8526-45206b84bc9d | -9.7128 | -48.122601 | 2024-11-19 00:28:00 | METOP-B | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 96a53319-56b2-30e5-8e8b-af84f799dbb9 | -3.7954 | -52.244099 | 2024-11-19 00:28:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c8614fa-a4a5-37fa-be8e-bc1bd1acf0e4 | -3.1108 | -53.696301 | 2024-11-19 00:28:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff2529e6-c832-3b75-bf60-d86e47e0627d | -2.4754 | -49.116501 | 2024-11-19 00:28:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df41339c-15e0-38e4-8c6d-bfe377ec7e22 | -2.9264 | -48.059299 | 2024-11-19 00:28:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86d97191-854a-319b-8b4a-04e0fe7ef552 | -3.1915 | -52.441601 | 2024-11-19 00:28:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9910ae37-3da0-363c-b2b7-713d9b05bff5 | -1.8314 | -46.283798 | 2024-11-19 00:28:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b61606b-733e-394d-8ddd-dc66ebb9a2c6 | -5.9417 | -39.6661 | 2024-11-19 00:28:00 | METOP-B | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 9fae365f-61d7-3c15-a9dc-932aa048ec3e | -3.0374 | -49.459801 | 2024-11-19 00:28:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea0da63b-5872-3756-b2c0-9aed9ac9a2ec | -2.9263 | -48.331501 | 2024-11-19 00:28:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 662e31ad-4345-3fbd-abff-51e046a63481 | -4.371 | -50.487301 | 2024-11-19 00:28:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b48effeb-de13-3689-bedd-b6a627390746 | -3.5527 | -51.524502 | 2024-11-19 00:28:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a365d121-7187-30ec-a436-36df06e8c7a2 | -3.7037 | -51.8321 | 2024-11-19 00:28:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d5d52df-7c1c-3759-83f9-9901ecdf2cb9 | -0.1083 | -51.414101 | 2024-11-19 00:28:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| a653e7d9-33b5-394a-afdf-158cd144ac22 | -4.8537 | -50.527199 | 2024-11-19 00:28:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b0643af-9428-36a6-9253-41213c69be9c | -3.1088 | -53.687199 | 2024-11-19 00:28:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbaafd0f-d9d1-3bed-8256-4347053ce53d | -9.248 | -45.013802 | 2024-11-19 00:28:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6c2f476d-5e19-39bb-8522-85d2c71dc322 | -1.6856 | -52.747398 | 2024-11-19 00:28:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4dced2a1-16ee-3273-8c9e-cca2016439d5 | -2.7543 | -52.603199 | 2024-11-19 00:28:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README5.md)
