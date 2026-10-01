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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d715392b-b6f0-3139-9765-6c894dbefb8a | -4.30275 | -50.77445 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| d6b1c550-f847-3819-8876-a5167e7df388 | -10.45811 | -46.76815 | 2026-10-01 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2cd72922-08a9-366a-adbf-06da0195175a | -7.03079 | -45.27674 | 2026-10-01 04:14:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 16b89c5d-052a-376e-a134-28afd01444dc | -11.44921 | -43.42547 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e249e452-e1b1-34a4-bdf4-91d37b62ee0d | -10.45741 | -46.77214 | 2026-10-01 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0bbe91b0-5fc0-31bc-8582-b6b8ece87f54 | -7.84747 | -45.81456 | 2026-10-01 04:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4c66d54-6e05-37f8-a0b4-1add2000f5bd | -5.10322 | -45.66961 | 2026-10-01 04:14:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d3e63c9b-4a4d-3584-a84f-d33332b11751 | -4.26816 | -50.80179 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 345e2e60-8a5c-3a15-be10-e782d6adcb94 | -4.63305 | -50.61201 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81013fc9-3fe5-37b4-a68b-d357bf697316 | -4.26524 | -50.78168 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 931c93c6-62e6-3c82-9425-708d23bc0877 | -11.3297 | -50.97491 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 206fa9f4-68a8-3900-a706-40fa75ec1ba2 | -11.22831 | -45.19091 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ad8237bd-93c7-34dc-ba0d-b7bd05054e40 | -4.27107 | -50.77335 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 4d02dedc-1504-3b95-aa62-64326f2698a6 | -8.47379 | -44.88597 | 2026-10-01 04:14:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66d21f77-4859-362a-803e-269a17fd27ed | -9.57179 | -37.37938 | 2026-10-01 04:14:00 | NPP-375D | SÃO JOSÉ DA TAPERA | ALAGOAS | Brasil | 2708402 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d9056b9e-6abe-304e-b0b1-42b6e03604b3 | -7.85099 | -45.81914 | 2026-10-01 04:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 29d20a51-f65f-3468-af13-1672367f8086 | -9.81282 | -44.83644 | 2026-10-01 04:14:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b92c0dd-3313-3505-915a-11ac13c9fb7c | -7.02198 | -45.27892 | 2026-10-01 04:14:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cdb20683-bc8f-36aa-805c-46c0a5550932 | -7.57182 | -46.62453 | 2026-10-01 04:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2ee836d2-08ec-379c-afe5-74b4659a0f30 | -4.89146 | -48.37233 | 2026-10-01 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8b09eee2-0318-355c-8761-db0b8ad43ab9 | -11.44287 | -43.42035 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1e811e7f-194e-3651-a364-a1456664d6df | -4.26738 | -50.75844 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| f02e4d6f-ae47-39bc-b8e1-98aef205f7d0 | -4.29765 | -50.80324 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b6c671a6-7772-340e-b630-cfacaae046fa | -11.71746 | -43.44461 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 326c444f-a145-3f4d-a28b-66c499b9652f | -6.70874 | -45.98562 | 2026-10-01 04:14:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ab02ea3-9415-3b38-b974-9b214b25a438 | -11.34905 | -43.3564 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db4770d1-1822-3352-a261-fc7f535db89c | -4.29455 | -50.79666 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bb6e0748-df99-354e-9b4e-e540f8f99158 | -5.7596 | -45.15263 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e93b0805-85d0-3376-99b3-1356de9328ae | -5.75898 | -45.15638 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| fdaaf558-51a3-3a87-9ae8-e11cd565205e | -7.11526 | -43.15093 | 2026-10-01 04:14:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 18f6ffe2-d0ab-3b57-874f-e572253de0d9 | -6.86848 | -44.93055 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 914524ce-6bcf-3074-afdf-fbc9595394cd | -11.44506 | -43.42878 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5b618f8e-1744-38db-a94e-eaa809e71b47 | -5.75835 | -45.16016 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| acc9c315-2a24-3167-8130-5597a83041fa | -11.38372 | -43.36596 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ba02edab-73d1-3353-8060-d55b4a5de12e | -9.06578 | -49.87135 | 2026-10-01 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 298c0fca-46f4-361d-9c86-4ffe2e8daf8f | -4.26565 | -50.7424 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4974c450-2952-320e-8f35-636c5f0a9d70 | -11.20728 | -45.15329 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b3a9b083-8686-3795-8178-ebf7c3a961da | -7.07402 | -42.30901 | 2026-10-01 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 3c29d6ca-ff59-3ead-8d9c-1e34fff796b1 | -4.28219 | -50.79439 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f184afdd-756f-33a9-bd36-b6b1cc5f508f | -8.20314 | -45.49831 | 2026-10-01 04:14:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 87375e10-bdf2-3303-8b92-5b01140b16bb | -9.387 | -49.15229 | 2026-10-01 04:14:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 12787985-7b7a-3abc-b0cc-50d891aa98ff | -4.27611 | -50.74524 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1f59e91d-e39a-34b1-9743-ac6e7c7c9ce2 | -4.26649 | -50.73748 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1321528-4e08-3422-949e-21e7f21b7202 | -10.70885 | -45.31709 | 2026-10-01 04:14:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 38bca7b2-c950-3c5e-b0b8-ffba2417d72d | -10.8564 | -48.69313 | 2026-10-01 04:14:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bb6ec0f4-c978-3df1-99cf-243915a001d0 | -4.25251 | -50.81848 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a13f13f8-1037-3dbb-93e7-31ba5b9e7b54 | -11.44352 | -43.41644 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b6af2c26-c156-339e-a519-cb0fde20337e | -11.42735 | -43.4056 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d2f0625d-c684-3317-abcf-f826b9033bea | -8.20763 | -46.20305 | 2026-10-01 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e3f484c0-09e6-3428-8217-a1f1c1deb28c | -5.76124 | -45.1685 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c61069ee-f278-3d3e-8dca-7c1d62794701 | -4.30554 | -50.79468 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7da4fcd0-e7d6-3b29-8bd4-d1d6804e5bb1 | -4.27081 | -50.73932 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 00632761-55ae-338d-b929-72cb6f2e791b | -4.29571 | -50.7525 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c31d1a55-d977-31aa-9434-408980aa5252 | -4.63741 | -50.62456 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cd231404-9ecc-3420-b64e-4e2b3ffe52b6 | -8.37222 | -45.38264 | 2026-10-01 04:14:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cfec4ecc-3615-3280-9351-ec61e1b4e722 | -9.88256 | -44.96859 | 2026-10-01 04:14:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f9d0b17-4431-385b-bfa5-099cdce8e0cd | -4.27058 | -50.78768 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 88ec4a17-ccb7-37de-bbb2-1f4e627d845c | -5.76312 | -45.15715 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3e841144-0280-3a4a-b10a-f168a793b2ed | -11.42823 | -43.42187 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d92dd87-4784-3141-9e11-f0cfa7ca4ce7 | -8.60891 | -49.46338 | 2026-10-01 04:14:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab911093-b940-32d9-8d90-e3adaa37e505 | -11.41272 | -43.4071 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d4484913-f01b-3f74-89d0-0f1c9203eddf | -5.75647 | -45.17152 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce7f0ea3-6e78-3265-ae5c-dfcfad3c93ab | -5.43035 | -43.44817 | 2026-10-01 04:14:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 09b25978-73d0-37b7-831c-b490d49ef2bb | -12.32452 | -46.39671 | 2026-10-01 04:14:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| aadc9fb1-dc24-30b7-b12e-ca72a759baa0 | -10.29698 | -44.64535 | 2026-10-01 04:14:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a582b66a-2a16-3d1e-b8d9-842f88ecc2b5 | -5.90852 | -53.49483 | 2026-10-01 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61b18fe5-fe93-3c6e-9d5c-ab479d3dd0b8 | -4.26779 | -50.76687 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 6c85700a-52f9-3946-a89e-b165d2a4c0ea | -10.27822 | -44.64367 | 2026-10-01 04:14:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 081bf12b-911b-3437-8769-73f4a920886c | -7.32848 | -42.07598 | 2026-10-01 04:14:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 695e859d-13b8-3f1d-a3bc-04cb3caff938 | -4.26731 | -50.73274 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e351634-26ba-3741-b95f-564b6e48d0b7 | -5.76788 | -45.15421 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9d529537-6f37-3ce3-b00f-4c4b9a3df237 | -4.29703 | -50.78213 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 86a2a34e-9d17-39a6-ba93-c0d9e2965cb4 | -7.6212 | -44.54998 | 2026-10-01 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e349341-ab23-3794-8e49-b3cd6c5dd296 | -11.68516 | -43.50454 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7dbe6024-192f-32e0-ab49-be17e72d2c79 | -4.30611 | -50.75546 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29699a8f-387e-3da1-86d4-17eda736cd77 | -7.50289 | -45.83449 | 2026-10-01 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0fdc73f4-2924-3a6f-ad1d-98e3fbc43325 | -11.1759 | -45.11634 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4a122a02-f5d1-3982-a239-c58222514bef | -10.66376 | -50.76381 | 2026-10-01 04:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32025e80-da65-3aa7-bac5-96a8151b0b86 | -4.27698 | -50.74041 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ed37d6b4-e901-3ca2-9117-44a0d640124a | -11.38787 | -43.36266 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ddfc7b57-daff-3561-8910-3afc3cacb610 | -11.43019 | -43.41012 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2098b5af-36f4-3cec-8b24-66feffee08bd | -9.80759 | -44.82085 | 2026-10-01 04:14:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 398b41a8-25c1-35dc-91b9-02d2e760115e | -4.3044 | -50.76515 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 12aac3fd-6471-369c-8d54-9e6f0548d5a1 | -4.45474 | -47.91704 | 2026-10-01 04:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 958fee99-3567-3427-a680-0f88d4ae6383 | -7.06894 | -42.29632 | 2026-10-01 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| bb0e11bf-5b05-321d-95f4-bd5f8cc978e6 | -4.283 | -50.78961 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 45439143-387d-3e8a-b783-6afaea0c2ffa | -10.78184 | -50.5293 | 2026-10-01 04:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54e3ee1d-2001-3d4c-9e6f-a25ac43a2d39 | -11.70152 | -43.45394 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0fca5d14-96af-355f-9e1a-dc54eba60b20 | -11.41971 | -43.40832 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| edffaf92-9609-3858-b3db-6e15851c1a4e | -10.77708 | -50.52465 | 2026-10-01 04:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a635ab1-2f47-3bb4-833f-19eb73e3d4e2 | -8.53982 | -44.05888 | 2026-10-01 04:14:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 036be4be-b192-3b20-b403-21fa3e49ab2c | -4.26692 | -50.83221 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 45f073a0-a6cb-3add-82fb-b00a5f9f4144 | -8.32523 | -46.75964 | 2026-10-01 04:14:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 946227e5-f63a-3367-b309-1edbb6c47e3a | -5.92741 | -44.11235 | 2026-10-01 04:14:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 878c07b3-5348-3c12-98e6-7d2928179a35 | -10.29618 | -44.64996 | 2026-10-01 04:14:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8c609c7a-b4ed-3ad1-ac82-cf52033fb214 | -10.91885 | -43.85433 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb7ee617-8404-3334-bd09-1ad75bbcfe69 | -4.29166 | -50.77623 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 7d136850-998a-3c43-b183-f34789906065 | -10.514 | -45.37715 | 2026-10-01 04:14:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e3f8ae5-76cc-3f8b-a540-1a29cdcf9971 | -4.29022 | -48.55849 | 2026-10-01 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6bfb2cea-232a-32e6-8801-58f03fc4f061 | -5.70883 | -43.63499 | 2026-10-01 04:14:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |


[Clique aqui para ver as próximas entradas](README33.md)
