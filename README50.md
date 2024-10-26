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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23ce942f-4eb9-331d-9e41-7cd9c1db4d1d | -8.7746 | -44.70762 | 2024-10-26 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a283245-f518-3404-a6a2-5fbf1e121ea2 | -8.77018 | -44.71409 | 2024-10-26 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7437476d-3f59-3faa-b9ae-8da83ca7728c | -8.7674 | -44.71007 | 2024-10-26 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d62fef20-1a04-344f-8897-ad79cec68806 | -8.76686 | -44.71356 | 2024-10-26 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8013e08a-4400-3d4a-b590-98bc3d92d3a5 | -8.76631 | -44.71706 | 2024-10-26 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7dec4fe-f837-3783-965a-db8082ae0436 | -8.76517 | -44.70256 | 2024-10-26 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 998134af-3954-30c6-877f-4648635acdfc | -8.76298 | -44.71653 | 2024-10-26 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89774c11-8082-3019-a01b-eb7bd6a4d5e8 | -8.76244 | -44.72003 | 2024-10-26 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c8a6cc4f-e01c-3246-826c-5adcfbd039dc | -8.76189 | -44.72353 | 2024-10-26 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 54c3b047-b517-345a-9b97-149403fc4313 | -8.65292 | -45.04942 | 2024-10-26 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ff038b6d-942c-3aee-a503-489a00c8e008 | -8.60518 | -45.12064 | 2024-10-26 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89ccad29-40b1-3202-b78a-897d2903c597 | -12.07632 | -45.71857 | 2024-10-26 04:19:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d999846a-16c6-348e-bb58-e8c27d315252 | -12.05695 | -45.7335 | 2024-10-26 04:19:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f8e97ea-7bd0-34fe-b6de-856e7cdbe701 | -6.40571 | -45.82092 | 2024-10-26 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2d909b6-baef-32e5-a5e2-da22e7d3768f | -5.9811 | -45.3689 | 2024-10-26 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 181c9a63-860e-3e2c-96cc-4e4998aa9f26 | -5.97776 | -45.36838 | 2024-10-26 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 80836e73-fee2-3024-9cd0-83225dac4051 | -5.9772 | -45.3719 | 2024-10-26 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 36f384cc-086e-3a11-a93a-54c37a1fbb68 | -5.97442 | -45.36786 | 2024-10-26 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 4d643075-0396-3bba-b45a-726290f841a6 | -5.97386 | -45.37138 | 2024-10-26 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7a8fea44-bd09-30fc-971f-3bddc1888f51 | -5.9123 | -45.5863 | 2024-10-26 04:19:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0974e2c-6444-31e2-825c-d89c92d3f5c4 | -5.90961 | -45.51673 | 2024-10-26 04:19:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c9f6298-fec5-30c0-8358-1a3313789d2d | -5.90894 | -45.58577 | 2024-10-26 04:19:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d960ed01-db97-330a-908a-bd8fc38879c5 | -5.99902 | -45.96009 | 2024-10-26 04:19:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f7d6ff0-0073-3a42-9b20-e4999aee4eb2 | -5.99735 | -45.94871 | 2024-10-26 04:19:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1512f0b-3ac6-3b0d-832d-45e5098538b5 | -5.99564 | -45.95955 | 2024-10-26 04:19:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7940102-34fd-3358-a194-b02e1c2a0d93 | -5.92371 | -45.99652 | 2024-10-26 04:19:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ebf907c8-2cbf-3178-bd63-129223e5333b | -5.86845 | -46.14471 | 2024-10-26 04:19:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 43c1d16b-0e86-384d-98d5-954c7e8fc887 | -5.86504 | -46.14417 | 2024-10-26 04:19:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53cd817e-b08d-3517-bb41-328d497ec645 | -5.84335 | -46.23854 | 2024-10-26 04:19:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| db335e73-26ba-3a79-895e-f0cf3cf21952 | -5.78199 | -46.29315 | 2024-10-26 04:19:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d04195d6-c46f-3c92-bc03-a33cf4e96b03 | -7.41043 | -45.5705 | 2024-10-26 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fe2889b9-c912-3a2d-a886-be1bd160c431 | -7.40987 | -45.57401 | 2024-10-26 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92cdb9a6-ae50-3c0b-9fd7-a32dd7e4df78 | -7.28209 | -45.71628 | 2024-10-26 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 720f110d-63ed-336f-8bd1-a4807a7f4f4b | -7.14046 | -45.43801 | 2024-10-26 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ade8263b-1523-3980-a774-78bd421efdb5 | -7.09712 | -45.4096 | 2024-10-26 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea9b9e7f-1f67-3c9a-b54a-14c4a16b2f5f | -7.08363 | -45.60186 | 2024-10-26 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2eca3e7-e568-37c7-95b8-34d901d0bf09 | -7.07815 | -45.50724 | 2024-10-26 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e25af8ef-b957-34dc-a84d-fa14c5eb1d58 | -6.92795 | -45.62066 | 2024-10-26 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 69d0beb1-616b-37ae-89b1-4b1c962118c9 | -6.86923 | -45.89089 | 2024-10-26 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ccc5d4eb-3d6e-3501-bd0b-afda8db1fde7 | -6.86867 | -45.89442 | 2024-10-26 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f4504ed-3faf-3265-90d5-09d9e3a6d6bd | -6.8681 | -45.89796 | 2024-10-26 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49f94138-28d3-32af-864f-2812afe9ca06 | -6.86754 | -45.90149 | 2024-10-26 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78261956-5c17-3d80-bbcb-a5df8882cedc | -6.86475 | -45.89734 | 2024-10-26 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7961390-c6a5-34de-8fe4-6bc06670dede | -6.86251 | -45.88974 | 2024-10-26 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a1b093d-d04f-3f4d-bcfe-26ee0d9fe00a | -6.85915 | -45.88913 | 2024-10-26 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9fde87b7-4dff-3ff8-8ded-1533e1de284d | -6.853 | -45.88441 | 2024-10-26 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 34.0 |
| e451f295-4c0e-3ad4-9725-e4ed5037e262 | -6.85244 | -45.88792 | 2024-10-26 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 86b4a7a6-2111-3404-8281-d98cc2b307b8 | -6.84964 | -45.88387 | 2024-10-26 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 63b6a468-b985-3dcd-9cb0-bc28b5269de7 | -6.84908 | -45.88737 | 2024-10-26 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 4df42e11-5b65-3483-9cbc-d8414c10aabc | -6.84851 | -45.89096 | 2024-10-26 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| ef41aca8-25c6-3242-be3d-63944b40bcfd | -6.84572 | -45.88683 | 2024-10-26 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 30ddb3d5-4870-3b07-8e5e-7120d44084c9 | -6.84515 | -45.89042 | 2024-10-26 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 6619fd36-6a7a-322a-b519-24fcf52974e8 | -7.80251 | -46.56673 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17daaa7a-2b27-32e1-8330-16aad1d68353 | -7.70063 | -46.63718 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1797304-07a8-3583-a981-6215773ad785 | -7.56387 | -46.79106 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92943ffc-f90e-30e0-aa43-e8196da3a628 | -7.56326 | -46.7948 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 69676309-983f-3883-b119-800cdc9be47d | -7.55983 | -46.79424 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 040be102-4453-3a0d-8784-bc71faa41561 | -7.55922 | -46.79797 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 00f822bf-d0b1-3395-810f-5de95523de9c | -7.55639 | -46.79367 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 409cc6cc-8353-3b83-b775-ca4e9c55aab0 | -7.55579 | -46.79741 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f6d17870-b53a-3fd9-b4ff-01097dadca23 | -7.4777 | -46.48108 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57fe4229-5224-3684-b54f-8c99c886bb30 | -7.47555 | -46.71217 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ff77a81-f9ee-3ae8-b933-1537c3473c4e | -7.47495 | -46.7159 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32c80751-185b-3a78-9ba3-7df85066dd53 | -7.47435 | -46.71964 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9433017-53d1-3ab0-ac3a-4a7b076410d2 | -7.44757 | -46.84222 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ea715ac7-cf5e-3a7a-8086-39f5c678b3dc | -7.44597 | -46.54757 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c8fe2c3-c21c-35b8-ae39-b4f830bc9c86 | -7.44088 | -46.75249 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6299374-194b-3fda-8dfd-cbea50e6de64 | -7.42514 | -46.65422 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ae1948b-8f66-3752-b00a-9707a0ae75c4 | -7.2713 | -46.06504 | 2024-10-26 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9fd6ef3c-ced2-3a39-9097-f4bf29b715b9 | -7.27027 | -46.75153 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7bcf78d2-36a3-34c4-ad81-9f4be0985126 | -7.26233 | -46.05622 | 2024-10-26 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78c7dcda-da38-3be3-8668-54e98de8b793 | -7.25896 | -46.05568 | 2024-10-26 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9b89634-46b4-36ed-96eb-a7689357134e | -7.25648 | -46.33668 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 451a96c3-9a8c-3e26-87a2-a8e548eca07f | -7.17666 | -46.33124 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 56d28f29-4b16-35e8-87ae-852f44923aa3 | -7.17607 | -46.3349 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 248d0fc2-c014-33ba-8055-a9b84637da9f | -7.17384 | -46.32711 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1b19f5b4-1785-36ec-8b4d-4abfa00252f8 | -7.17325 | -46.33075 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 361aa01f-8c91-3c14-bf5c-9eb80ad79fb5 | -7.17044 | -46.32661 | 2024-10-26 04:19:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77c47233-77f3-313e-9f98-f704a9d246a6 | -7.16393 | -46.17315 | 2024-10-26 04:19:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9f11611-9e33-323d-b782-7cfb7574b18d | -7.12811 | -46.45884 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 07d30973-ffa9-38fc-8bd8-7ea35a988ec8 | -7.12351 | -46.46565 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61c2b14c-7ca6-3345-b215-1187a352abe3 | -7.12185 | -46.36825 | 2024-10-26 04:19:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| db168806-6859-3d59-8201-afb29645e6e1 | -7.12127 | -46.37191 | 2024-10-26 04:19:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9ccb9996-d027-3acc-8c96-eb06a8c394c4 | -7.03434 | -46.69591 | 2024-10-26 04:19:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35a3324c-6134-355f-b4f6-8770bd5b50fe | -7.03374 | -46.69965 | 2024-10-26 04:19:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d019ccf-e250-3fe2-bc5d-bd9e8168c699 | -6.99411 | -46.18353 | 2024-10-26 04:19:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc646045-803c-3102-a918-d8ae9b6b5ec3 | -6.96968 | -46.09818 | 2024-10-26 04:19:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7aca97bf-2fba-3bb9-942d-2e7bc2aea5ef | -6.96909 | -46.10181 | 2024-10-26 04:19:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e258a0ce-66c7-39fa-af83-a405599248fb | -6.96314 | -46.63899 | 2024-10-26 04:19:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7fb908a-d16f-3b10-87a8-b38279eb0549 | -6.86277 | -46.35 | 2024-10-26 04:19:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0589d3e2-ea93-3f64-bb0a-ce1ef8e63846 | -6.80166 | -46.46844 | 2024-10-26 04:19:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b257f1e-adaf-3558-a475-3b403471985f | -6.77503 | -46.37329 | 2024-10-26 04:19:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 028c38d8-722a-381a-957d-f9abcd49505c | -7.94648 | -45.68882 | 2024-10-26 04:19:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a64a971b-8042-39db-9c94-4b98caf641b7 | -7.94258 | -45.69181 | 2024-10-26 04:19:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3553bd21-f9ab-321a-a006-97b0f114d43a | -7.71694 | -45.70599 | 2024-10-26 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9354795c-f548-3de5-ad8e-51292c33040d | -7.71637 | -45.70952 | 2024-10-26 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 875ba3a7-e7f6-33a3-9a5c-8f95e1ce46de | -7.71416 | -45.70191 | 2024-10-26 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c8ae3093-6f68-3fc9-96db-cbbd41d3b36b | -7.7136 | -45.70545 | 2024-10-26 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 202cd084-c759-31a7-a561-b013b6e1c48b | -7.58771 | -45.90334 | 2024-10-26 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5dbbb479-fcec-3da2-90e0-a00acba7c017 | -7.56912 | -45.71887 | 2024-10-26 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README51.md)
