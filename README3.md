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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab785ef6-0c20-3efb-9117-a25201714013 | -3.47189 | -50.06682 | 2025-10-23 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 6b633282-0bda-3d0c-9eca-1d14e0eabdea | -2.98364 | -53.99572 | 2025-10-23 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8f6b5a84-97e1-350c-9707-39c9f0afa95f | -6.08509 | -49.37894 | 2025-10-23 00:54:00 | TERRA_M-M | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 842bb370-4964-3998-b423-e59e2fe3b3d5 | -3.01792 | -49.47536 | 2025-10-23 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 231.2 |
| 8605e255-aed5-393b-83b9-3805275edfb9 | -2.80645 | -54.37675 | 2025-10-23 00:54:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 180100d4-6e97-3ac0-9372-f75bd8d72c3b | -3.15745 | -49.17479 | 2025-10-23 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 13b08bdd-cd6b-3f10-973d-0d78180e8491 | -6.28245 | -47.00786 | 2025-10-23 00:54:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 41b97f69-a04d-3e81-9ab1-43cda9ce6871 | -4.19213 | -50.1216 | 2025-10-23 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 99898658-6ad3-33ce-9f7c-f03fbd6b5100 | -2.80772 | -54.38586 | 2025-10-23 00:54:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 54259b28-ae6b-3100-a1e7-1d03cf29c1df | -3.83778 | -51.74078 | 2025-10-23 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| bb75f13a-8177-36f8-b320-f8f2289fcaec | -1.89718 | -54.06997 | 2025-10-23 00:54:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 79f9cc90-c39a-39e6-bd1d-1933ec013d1c | -3.48361 | -50.06525 | 2025-10-23 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 169bc756-8c1b-3fd8-a56c-e0dd091477c9 | -7.28058 | -49.99215 | 2025-10-23 00:54:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 496cfad6-80ed-35f0-962a-7d128108279d | -3.22439 | -49.35097 | 2025-10-23 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 29ce584d-033c-320f-b961-c8c2788060cc | -4.70214 | -48.11452 | 2025-10-23 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| e998aa8c-525a-3281-8892-0977d7a8aed8 | -7.4561 | -49.40431 | 2025-10-23 00:54:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 2ab3d892-09f9-3dec-a46c-f5be3d3377c2 | -2.926 | -48.32095 | 2025-10-23 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| e8cb5677-44c7-368d-9d8d-9d2001bd4fbd | -6.59746 | -44.20559 | 2025-10-23 00:54:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 18c77489-1931-3227-8328-3c8fc5bdf527 | -2.8948 | -49.17242 | 2025-10-23 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 674c7ede-0c92-30b8-93e0-db3ad0b8def2 | -6.08753 | -49.39558 | 2025-10-23 00:54:00 | TERRA_M-M | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 25a421a1-8e31-358a-b954-116e63da18b4 | -6.60419 | -44.2465 | 2025-10-23 00:54:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 42890890-bb01-3cea-b332-580b212f3059 | -6.07976 | -49.3743 | 2025-10-23 00:54:00 | TERRA_M-M | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| f7693523-76a2-3564-a8ad-ac73d641d483 | -6.0941 | -49.38901 | 2025-10-23 00:54:00 | TERRA_M-M | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| df033f80-3083-3e72-a825-0878e012428c | -4.94235 | -48.30621 | 2025-10-23 00:54:00 | TERRA_M-M | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 94c6c3e6-f0c9-31dd-985c-0a80d02fa265 | -2.73144 | -48.29832 | 2025-10-23 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| f985aeef-2965-38c2-951d-c86bf9b01a01 | -3.01526 | -49.45717 | 2025-10-23 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 472fa2b5-01cc-36a8-bd3c-daa7049a12ec | -3.39341 | -51.503 | 2025-10-23 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 176d7ee9-a9c7-3d7f-835e-7f2cfc2d0c57 | -3.48595 | -50.08141 | 2025-10-23 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 2f88d1c5-e9f1-3d42-a33a-e326e9230c6e | -5.69545 | -45.9764 | 2025-10-23 00:54:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 56cebad4-d9ad-3a6f-b0a1-68f9966e15a4 | -5.6852 | -45.98475 | 2025-10-23 00:54:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 0523ba83-8da5-3bf7-a8c1-fba0a8c4b93e | -3.05009 | -48.71957 | 2025-10-23 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| f9e0e9d8-f471-33cd-bb83-7153b7546e78 | -7.00756 | -47.01663 | 2025-10-23 00:54:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| f5a70d1d-6ac2-31af-993f-daca296cb590 | -3.40386 | -51.50147 | 2025-10-23 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 9623a0bb-9ccc-3fd8-8dd5-339a21d8134c | -7.0036 | -46.99211 | 2025-10-23 00:54:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 15f09492-2411-3534-8f32-66c8b224e0a9 | -3.0533 | -48.7249 | 2025-10-23 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 05d8dc57-3891-31f5-aba7-0cf965bff735 | -2.92262 | -48.29826 | 2025-10-23 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| caae076d-4c3d-338a-9e44-7b1a2996d827 | -3.02765 | -49.45532 | 2025-10-23 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 8866117a-31b4-31cb-9b03-dd35d172aa68 | -6.59705 | -44.21017 | 2025-10-23 00:54:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 37f8cfd0-0f32-35d1-ac53-a891645d6569 | -4.70543 | -48.13582 | 2025-10-23 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| e29035c7-6875-3e80-a5bf-4dc01a1c6619 | -3.2272 | -49.36955 | 2025-10-23 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 4dbda770-0df7-3ce8-9863-7722655b3c80 | -3.47425 | -50.08296 | 2025-10-23 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 289252e0-4c83-3712-9281-f53841f8d39c | -4.37575 | -50.35112 | 2025-10-23 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 49805569-7bcb-3c45-a68a-9a9c94626914 | -3.04791 | -49.50812 | 2025-10-23 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 69a2ed47-13cb-314e-8cf1-aff76b3d2e1d | -2.81541 | -54.37549 | 2025-10-23 00:54:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 740f2485-1b82-3e2b-a345-6260768df545 | -2.90297 | -49.40391 | 2025-10-23 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| e476c309-a543-37e2-93a5-515c519ff67c | -6.08232 | -49.39088 | 2025-10-23 00:54:00 | TERRA_M-M | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| e13e5d99-c0c4-39f1-ae17-418bdf167950 | -2.73822 | -48.29083 | 2025-10-23 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 2e804a69-5fed-31e5-8f26-a50e8590c580 | -3.69941 | -49.56839 | 2025-10-23 00:54:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 57b1dc57-bd85-3a35-813c-3746790ff186 | -3.02059 | -49.49361 | 2025-10-23 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 130.7 |
| 9dca3e93-d972-3dec-95a8-7362384f6e94 | -3.03029 | -49.47353 | 2025-10-23 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| ad5ded68-3b42-37af-a23e-f852694bf71c | 1.55596 | -56.02137 | 2025-10-23 00:56:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 140984b5-a8c8-36ad-acbf-223f7c14228a | -10.5249 | -50.2137 | 2025-10-23 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 2f5d2946-4ac0-3d09-938c-2e4fa2d373d5 | -11.3643 | -49.7995 | 2025-10-23 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 924964e6-56d4-314c-a64e-4271c464264f | -5.6933 | -45.9667 | 2025-10-23 01:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 2e7cb1df-d532-313b-af2f-6d8472bacadc | -3.0353 | -49.4901 | 2025-10-23 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| f08408c7-c778-3c55-ba91-2b16dea98d0e | -2.8155 | -54.3736 | 2025-10-23 01:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 42017047-9635-3d90-a97f-53b534c4e532 | -9.0988 | -65.3596 | 2025-10-23 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| f97e5328-7b52-383e-a205-14d2a8caa39a | -10.4834 | -49.0986 | 2025-10-23 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 3ac94343-e6a2-3643-af72-871cd4b50bc5 | -10.4645 | -49.1006 | 2025-10-23 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 8345316e-8d86-397b-a686-864ab0ced026 | -3.0169 | -49.4694 | 2025-10-23 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 177.4 |
| ba643def-2bef-3174-bcf1-713e02001bf6 | -12.0036 | -46.7667 | 2025-10-23 01:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| c7cfe96c-201d-335d-a4bd-13bdf60e1c45 | -3.4763 | -50.0673 | 2025-10-23 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| fcdb2b31-d111-3833-98bb-79efa5a42a52 | -3.0168 | -49.4906 | 2025-10-23 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 170.6 |
| 030b32eb-21d9-3487-b30b-d53beb1112c8 | -11.3453 | -49.8017 | 2025-10-23 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 0bd892c4-66a4-3da4-abbb-2813c2a17bbf | -9.1174 | -65.359 | 2025-10-23 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 7c33b59f-96a7-3c4e-8fad-e7ea4f5639fb | -10.3406 | -62.8401 | 2025-10-23 01:00:00 | GOES-19 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 70b4a6bd-f14e-3127-9c98-f95a2c600a69 | -11.3646 | -49.7779 | 2025-10-23 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 45e2d7a5-d965-3f60-9174-f3b02761140c | -19.7638 | -41.3069 | 2025-10-23 01:00:00 | GOES-19 | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.5 |
| 3e37d14f-bde2-37fd-bf20-633c15f3472e | -3.0354 | -49.4688 | 2025-10-23 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 7fca675b-f4b9-31f2-9083-3b74ceed2cb3 | -3.0353 | -49.4901 | 2025-10-23 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 154.3 |
| cfab5bd4-7bcb-3986-a20a-52c41f6a11ca | -3.4763 | -50.0673 | 2025-10-23 01:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 29507b22-bb83-3a01-a95c-016cb84a2266 | -12.0032 | -46.7892 | 2025-10-23 01:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| a167fd4b-acb2-3dff-8371-49f1d3f1c9d1 | -12.0036 | -46.7667 | 2025-10-23 01:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 327748bf-2aa2-3528-acff-c364ba0e7b80 | -3.0354 | -49.4688 | 2025-10-23 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 128.1 |
| 619e0ec0-7668-3147-8106-98208b453fe0 | -3.0168 | -49.4906 | 2025-10-23 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 135.8 |
| 65f844c3-2425-3810-ab90-92fae1bcbbbc | -2.8155 | -54.3736 | 2025-10-23 01:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 1fc69f7c-5e87-300f-a1df-44658c497344 | -10.3406 | -62.8401 | 2025-10-23 01:10:00 | GOES-19 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 53.6 |
| ec232f0c-ac07-39d2-a783-a7d63e76b063 | -6.6079 | -44.2176 | 2025-10-23 01:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 7e1a9e15-6734-3ce0-b7c7-a816b005fbd4 | -3.0169 | -49.4694 | 2025-10-23 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 60617489-219a-3ff6-8bd1-4ebfd17c2f6d | -10.5249 | -50.2137 | 2025-10-23 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 34053d27-947f-3b6a-9cfd-ac3b5b79ca74 | -3.0168 | -49.4906 | 2025-10-23 01:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 166.5 |
| 49a32f70-26f9-3667-a543-c7478bdbc513 | -10.4834 | -49.0986 | 2025-10-23 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 806e4683-dc40-3e92-bc7f-e4c68e7946b3 | -10.5249 | -50.2137 | 2025-10-23 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| d3880d97-3d77-3c39-8dc0-d2e009bc250f | -3.0354 | -49.4688 | 2025-10-23 01:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 56ab0cb2-36eb-3b91-bc48-9ddc08f2476d | -3.0353 | -49.4901 | 2025-10-23 01:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 125.5 |
| c4768a46-4ffb-3f36-8c53-c0b6322e05dd | -13.8002 | -52.7664 | 2025-10-23 01:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 49.0 |
| a826d318-755f-3365-a156-6623cf2f9663 | -12.0036 | -46.7667 | 2025-10-23 01:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 27d5fc00-1e56-38bb-83c8-7d7d69467ca4 | -3.4763 | -50.0673 | 2025-10-23 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 9661145c-aa47-36f9-abb1-1df6efd4a2c1 | -3.0169 | -49.4694 | 2025-10-23 01:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 141.2 |
| e150c620-aa65-35ff-94e3-7443504e2e27 | -2.8155 | -54.3736 | 2025-10-23 01:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| dc27b983-16d8-3b35-85b1-0b446eb5de49 | -10.5438 | -50.2117 | 2025-10-23 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 76175b80-3808-31be-9507-a06fd7775d8c | -12.0032 | -46.7892 | 2025-10-23 01:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 47657123-7a3c-3b5c-8ca5-a56ebcd928ac | -12.0036 | -46.7667 | 2025-10-23 01:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| b0168e8e-1b74-3b55-a826-cf865b247528 | -6.6079 | -44.2176 | 2025-10-23 01:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 52c4d603-dd11-39d5-bc73-51652ec9f1d3 | -10.4834 | -49.0986 | 2025-10-23 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 949d610c-af68-32e8-a98c-8fb13ec12cee | -9.1174 | -65.359 | 2025-10-23 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| e4907a1d-b628-3030-ad85-ee64ea3c64dd | -3.0169 | -49.4694 | 2025-10-23 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 15b15057-11a5-3330-8f6e-de66c6da2578 | -3.0353 | -49.4901 | 2025-10-23 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 3839186f-983b-3b97-8e01-f7d62dac5257 | -10.4645 | -49.1006 | 2025-10-23 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 3e6d4d83-2000-3d01-b4e0-32100fa7db29 | -10.5249 | -50.2137 | 2025-10-23 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |


[Clique aqui para ver as próximas entradas](README4.md)
