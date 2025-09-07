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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f608d1d-1c9e-3c77-9940-c5f94fc0c229 | -6.2108 | -42.6426 | 2025-09-07 13:40:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 93.1 |
| cacc90ae-4fe9-3748-b8cc-3b656457c7ae | -7.0129 | -44.9613 | 2025-09-07 13:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 2268d945-70cf-3bc8-9ce8-3a4e8aa29fca | -5.8692 | -45.0759 | 2025-09-07 13:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| ba2dbc90-9e29-364e-b500-bef58bf34568 | -12.9289 | -54.7744 | 2025-09-07 13:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 176.3 |
| 103223e0-0897-316a-ae0a-ede353783402 | -10.4632 | -53.6132 | 2025-09-07 13:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 103.7 |
| fcb2124a-7c23-3d34-b89f-462ca6796d47 | -15.124 | -48.0627 | 2025-09-07 13:40:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 235.0 |
| 9707b78c-d24a-3013-8479-f1b7297da672 | -6.8937 | -45.6061 | 2025-09-07 13:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| d7315d91-9c46-39a7-bf99-d58a400c6bd3 | -12.7641 | -52.9498 | 2025-09-07 13:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 4c7eeaf3-2962-36c8-af40-5d2ee53ca940 | -11.4089 | -43.581 | 2025-09-07 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 152.7 |
| 78bcf16b-34f2-37ab-8a46-661a21dc2be0 | -12.9477 | -54.793 | 2025-09-07 13:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 135.0 |
| 0c78e9ad-a91e-3982-bd35-a6c05c7601c1 | -6.1923 | -42.6205 | 2025-09-07 13:40:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 97.1 |
| 17bf7af7-bc8b-38f8-93c4-0ae6856d826b | -11.5669 | -47.7638 | 2025-09-07 13:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 53c32619-c7ae-3248-94c8-810339cbfbb9 | -12.3016 | -47.2416 | 2025-09-07 13:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 126.9 |
| a18f0d90-b1ca-3762-85a4-7e57749cec4c | -7.725 | -50.3386 | 2025-09-07 13:40:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 2ffd4d69-e47e-35f4-8bde-70503f72c68f | -13.0521 | -47.1328 | 2025-09-07 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 1e245651-e7ca-3c6a-aa92-bd8f7818c596 | -11.0245 | -45.9502 | 2025-09-07 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 8da5c382-4078-3ddb-b254-9e3a6f504211 | -8.1814 | -49.6003 | 2025-09-07 13:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| cbbd782a-4ceb-3f1c-ab36-b8bab92eb083 | -11.1575 | -48.3883 | 2025-09-07 13:40:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 859476cc-3be0-31d5-8478-97e213a863aa | -7.8154 | -45.4329 | 2025-09-07 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 126.4 |
| f9c741c4-fae4-3127-a349-960de31c0380 | -13.9342 | -54.0256 | 2025-09-07 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| b3ce3dae-b3da-338c-aaff-a6d3224424ce | -6.5915 | -43.9883 | 2025-09-07 13:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 838c05a2-c2b6-3376-8b47-91d3a460e246 | -6.8281 | -52.8143 | 2025-09-07 13:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |


