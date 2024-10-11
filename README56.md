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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd3f477a-3ec2-37cc-b28d-a6162d503793 | -5.43433 | -45.89614 | 2024-10-11 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76109535-bdc1-3e76-a89b-d6cca4a1f0e7 | -5.41206 | -45.90675 | 2024-10-11 04:23:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8ab49c0-76e5-397c-8529-bf58e14409aa | -5.406 | -45.90227 | 2024-10-11 04:23:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 932397b4-a0ab-34c9-a726-d06ece2edf06 | -5.40546 | -45.90572 | 2024-10-11 04:23:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92cdda79-c6d3-31f2-9361-88e923e5ef53 | -5.34909 | -45.57154 | 2024-10-11 04:23:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4409a4fb-d6a8-32e5-adc6-c7bab3aa4c66 | -5.34633 | -45.56756 | 2024-10-11 04:23:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8d171c09-e2d6-345b-8834-f8d8b4390381 | -5.34578 | -45.57102 | 2024-10-11 04:23:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 489f9f0c-ecdd-3781-94ab-e21ef2e325a1 | -5.26479 | -46.21899 | 2024-10-11 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c12467ee-0864-3c8c-8264-8cd3acee32e4 | -5.26203 | -46.21502 | 2024-10-11 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2f1958c-66a2-3c7a-b87c-9362c8271ea7 | -5.25985 | -46.22882 | 2024-10-11 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f61ee0cd-850e-3e9d-91f3-5ea03ea5ffc5 | -5.25872 | -46.21451 | 2024-10-11 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55fde384-c6a0-33e6-9c68-a5e8b919b79c | -5.25655 | -46.2283 | 2024-10-11 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43a037a1-c83f-3a55-a85c-31af7a25cddc | -5.25287 | -46.22738 | 2024-10-11 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c469733-7f94-350c-b6ab-8445cf55e914 | -5.25233 | -46.23082 | 2024-10-11 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf6bd518-01f5-38bf-952f-45a809b762de | -5.24902 | -46.23031 | 2024-10-11 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e954da8f-74b4-3395-9b52-6cec835c82d5 | -5.2468 | -46.2229 | 2024-10-11 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d30785ed-553a-3a66-b55a-d143ecce42e2 | -5.24626 | -46.22635 | 2024-10-11 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8de7f3ae-eef7-3af1-8f6a-147ad5508d28 | -5.21925 | -45.70684 | 2024-10-11 04:23:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9cb36910-bee2-32f8-a171-ca98c04e37a3 | -5.19438 | -45.95356 | 2024-10-11 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6972c198-3703-34e5-867b-6e957e5baddb | -5.19161 | -45.9496 | 2024-10-11 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 30e43ab7-8b7b-3a9b-88c8-dc34a8570fc2 | -5.19107 | -45.95305 | 2024-10-11 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2728f109-ad42-3d10-8e97-8452816a6d60 | -5.11248 | -46.1065 | 2024-10-11 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e9ecf462-52e7-32d6-9c44-fd3c7328145c | -6.41909 | -45.92028 | 2024-10-11 04:23:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 321e34ac-45ee-376e-86b6-d3132e03944f | -6.41855 | -45.92374 | 2024-10-11 04:23:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2455cb4c-9e83-369d-ba25-fd79f4485dbb | -6.41081 | -46.4921 | 2024-10-11 04:23:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 588e76a1-5515-3280-b3a4-d8b2b771bafa | -6.36416 | -46.16285 | 2024-10-11 04:23:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bea8e1f4-0623-32a6-ba10-9c786231a595 | -6.36139 | -46.15887 | 2024-10-11 04:23:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ae483ac-3cc5-3e50-9e51-51eba7f51c3d | -6.36085 | -46.16233 | 2024-10-11 04:23:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 284b6504-6da1-3da0-b317-cea98667ce13 | -6.33266 | -46.34176 | 2024-10-11 04:23:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3bcfbeb0-2903-3d20-b199-6b745fcbc88c | -6.33211 | -46.34521 | 2024-10-11 04:23:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aec105e6-7af7-3cbd-af5e-c4d50770ed5a | -6.32935 | -46.34124 | 2024-10-11 04:23:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 83ad9fdb-87c4-37e1-b866-67b8cc5f2096 | -6.32881 | -46.34469 | 2024-10-11 04:23:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6cde578-0c54-31dc-8cf8-f552b23b11a4 | -6.32335 | -45.70634 | 2024-10-11 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 95f7cec9-c098-31cd-bdea-dc20cac1676b | -6.3195 | -45.70929 | 2024-10-11 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 46127e24-69f7-37cc-834c-4625e8348e94 | -6.31896 | -45.71275 | 2024-10-11 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b8d3b35-432d-3cad-8148-03f468c42a99 | -6.31517 | -46.10529 | 2024-10-11 04:23:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 77a3d790-43c6-3f49-ae19-6d4a8a70d197 | -7.35491 | -45.62438 | 2024-10-11 04:23:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 332cf063-1059-337e-9bb5-a1a00dc0292f | -7.33018 | -45.51981 | 2024-10-11 04:23:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d396d91-99df-3b81-8413-ce1c1410244b | -7.316 | -45.46029 | 2024-10-11 04:23:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6f9264f-9d6c-39da-9fcc-8fa2a76797f0 | -7.3034 | -45.54121 | 2024-10-11 04:23:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b7ce6b4-3de4-3e8e-b2d1-fdf94f4946ac | -7.27465 | -45.37438 | 2024-10-11 04:23:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d76474fb-746d-3bcd-b374-f6428ccd5e4b | -7.27131 | -45.37387 | 2024-10-11 04:23:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cbac6db7-f003-3ec0-826c-8dcaed175104 | -7.25578 | -45.38592 | 2024-10-11 04:23:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6b2a75fb-ceac-3606-b329-d704384bb852 | -7.23069 | -45.52635 | 2024-10-11 04:23:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| edea91dc-08ba-3327-90ea-ac30f35e82d3 | -7.23015 | -45.52987 | 2024-10-11 04:23:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd90d09d-bbb0-348e-b201-6a0a5edcdd2d | -7.16402 | -45.7169 | 2024-10-11 04:23:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| afb4bca3-20d9-3b62-af2d-2e04acd1923d | -7.10251 | -45.32583 | 2024-10-11 04:23:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45a4dc40-06c3-33b0-b406-5523dfc67d80 | -7.10197 | -45.32936 | 2024-10-11 04:23:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37484681-620e-3213-af99-993029e40c02 | -7.0911 | -45.44322 | 2024-10-11 04:23:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f54d74c-c464-315f-aed1-1a4d6432692c | -7.06531 | -45.56511 | 2024-10-11 04:23:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa9cae25-dce5-3f1a-93b2-28ff1f67e8da | -7.00301 | -45.24543 | 2024-10-11 04:23:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 839b4e87-610a-3d88-92c3-4de385d410ea | -7.00137 | -45.25602 | 2024-10-11 04:23:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9255970-af8f-3de7-b8cf-0159099fb5db | -6.99912 | -45.24844 | 2024-10-11 04:23:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ef76007-6020-37d3-9036-b073694342ae | -6.99858 | -45.25196 | 2024-10-11 04:23:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70f8d230-b717-353d-aa6d-44caf2ed1fa9 | -6.9899 | -45.70014 | 2024-10-11 04:23:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e390ae8e-ffd0-37e7-9c38-2b253a4e2042 | -6.97852 | -45.24886 | 2024-10-11 04:23:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 002dbf98-1c72-3158-83a4-77290d46a174 | -6.95802 | -45.29293 | 2024-10-11 04:23:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5e6a0c6f-5093-35fe-a3cb-06cb34b5ee87 | -6.95522 | -45.28896 | 2024-10-11 04:23:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d03b5a9d-40b1-3d7b-a5da-40a2cce9c97a | -6.95468 | -45.29247 | 2024-10-11 04:23:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b47d33b7-1b75-3ec0-955f-ed79b63a4e19 | -6.94888 | -45.21909 | 2024-10-11 04:23:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 211611e0-ebd7-3410-a715-14b45a958378 | -6.94834 | -45.22263 | 2024-10-11 04:23:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91292a09-4d6f-39f6-b21c-1183ca6f08af | -6.94779 | -45.22616 | 2024-10-11 04:23:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a3ffd6e-fb95-30f7-a210-5961e441d474 | -7.16456 | -45.7134 | 2024-10-11 04:23:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9ae45e20-a86d-3801-a076-f6a629a867ad | -7.06591 | -46.19237 | 2024-10-11 04:23:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74ff58a7-1068-37a4-8ece-a836020dbd95 | -6.98935 | -45.70363 | 2024-10-11 04:23:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e3d85c5a-3d81-3766-b0ba-6094a995f122 | -6.9723 | -45.72596 | 2024-10-11 04:23:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc17c97d-bd37-38d8-bd66-91056bfb3935 | -6.95639 | -46.13227 | 2024-10-11 04:23:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 022b092d-db4d-3415-bc85-e7da6d95ae7c | -6.95585 | -46.13573 | 2024-10-11 04:23:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fdeb8048-4827-3662-95f4-bee490ee08bf | -6.95531 | -46.13918 | 2024-10-11 04:23:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bbc39966-7619-395e-b8fa-d21a7834d61c | -6.94312 | -46.3249 | 2024-10-11 04:23:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e0756ff-0854-3423-83a6-17711027b26b | -6.93651 | -46.32386 | 2024-10-11 04:23:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 23a2a94c-e52c-3322-bbea-1d459f15078d | -6.83074 | -46.17624 | 2024-10-11 04:23:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a811e04-d28e-3f21-bef1-d60601967aa5 | -6.82744 | -46.17572 | 2024-10-11 04:23:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c2814b9-e9dc-3136-bf17-32ae486bccec | -6.80059 | -46.47585 | 2024-10-11 04:23:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9fe492f-04f5-3b87-acc4-a7d515b9a9e2 | -6.79449 | -46.4501 | 2024-10-11 04:23:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed5690f8-0a5c-3dff-8e4c-f67d0de026ba | -6.71656 | -46.23216 | 2024-10-11 04:23:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 56c8d059-6eeb-3d25-8758-d9fb777ee898 | -6.64301 | -46.03 | 2024-10-11 04:23:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63f89301-e2e3-3e76-8fde-f0c075222fbc | -6.60881 | -46.46341 | 2024-10-11 04:23:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a88c139a-cda0-325e-9af6-e5e103b53d78 | -6.55115 | -46.54996 | 2024-10-11 04:23:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c94b4551-cbab-3653-ac8b-8878f30b5089 | -6.55061 | -46.55341 | 2024-10-11 04:23:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36a96797-4e94-33bd-b533-4837762b795d | -6.49931 | -46.16636 | 2024-10-11 04:23:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a89a00aa-f32a-32b8-8e44-1ca07b203bd6 | -6.496 | -46.16584 | 2024-10-11 04:23:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 054304ac-82c5-3232-94b9-2e7ef2dabe4f | -6.49546 | -46.1693 | 2024-10-11 04:23:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39ac28f0-9733-3d5d-a060-219f8226925b | -6.78763 | -45.647 | 2024-10-11 04:23:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6dc1228-b53e-3706-8697-11da08779d0c | -6.78431 | -45.64647 | 2024-10-11 04:23:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c6e131af-f108-399e-bbc1-db732d0dbd78 | -2.05975 | -46.82652 | 2024-10-11 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 633a579b-80a9-313c-b771-0f78157a2dd9 | -2.047 | -46.54607 | 2024-10-11 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63736b58-2d9b-3344-9dfa-09a885a5759f | -3.58697 | -46.40851 | 2024-10-11 04:23:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 937ce4cc-e1ab-336a-82be-040e9ba68508 | -3.35941 | -46.49472 | 2024-10-11 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cbacc7b5-14cc-3d92-abd3-2d6b6476c838 | -3.2995 | -46.07561 | 2024-10-11 04:23:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ce6dff5-96bb-384e-9c7e-d28dec01c8c8 | -3.17999 | -46.46638 | 2024-10-11 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a08a3630-5875-34ca-995a-6f8ef99f3a0e | -3.17943 | -46.46988 | 2024-10-11 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8cd25330-506d-35db-8fd3-d07f72330832 | -3.16832 | -46.47532 | 2024-10-11 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7cfee9aa-3829-3eb4-bd96-c00088666e7b | -3.16777 | -46.47882 | 2024-10-11 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| feac1e73-ba8b-385f-b743-40d38032b961 | -3.06559 | -45.94321 | 2024-10-11 04:23:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e1f07f5-ae29-3397-a668-fb579eaa63c2 | -3.06229 | -45.9427 | 2024-10-11 04:23:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7d7fb1f-0b6e-3b58-bd69-5a5e153bff7c | -3.05843 | -45.94563 | 2024-10-11 04:23:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c753c0ca-ca4e-3374-bf78-f1bd4efe61de | -3.05789 | -45.94908 | 2024-10-11 04:23:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d03117e-28f0-3b1e-80c6-256ebb8c4ac6 | -2.74767 | -46.79734 | 2024-10-11 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bee4696f-5837-335f-aed3-f43a21f8b7bb | -2.74264 | -46.78556 | 2024-10-11 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README57.md)
