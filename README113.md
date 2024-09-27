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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c792ace-e046-3e4e-85af-1a5d490b2054 | -10.39766 | -67.86544 | 2024-09-27 05:27:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f8134cd4-a7e7-323e-86f1-37bfa9ac5ca1 | -10.39403 | -67.95948 | 2024-09-27 05:27:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1cec9a7-74fd-341b-b851-f276cace5b5d | -10.39366 | -67.86475 | 2024-09-27 05:27:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e27607e5-493c-3b0e-9631-5af6f0e2f5d9 | -10.39002 | -67.95873 | 2024-09-27 05:27:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ec9f611-d6ef-3f35-ab09-691bc99d3bec | -10.08953 | -67.85893 | 2024-09-27 05:27:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c719d581-746f-3917-b3a7-85837439edfc | -10.08893 | -67.86246 | 2024-09-27 05:27:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b1f943d-3756-3dc7-b488-9a27d2f7eb9b | -7.57452 | -49.19449 | 2024-09-27 05:27:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49d05910-5f5a-3e2e-8e27-24274ed830c7 | -7.57269 | -49.1983 | 2024-09-27 05:27:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 596ad1c7-13fb-3208-b906-1c755b3620e8 | -7.56771 | -49.19333 | 2024-09-27 05:27:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 51948ab8-4343-3894-84f3-c457d5460965 | -7.56695 | -49.19942 | 2024-09-27 05:27:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8293638-1996-3495-885d-330df346dece | -7.56587 | -49.19731 | 2024-09-27 05:27:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4e947ec2-a862-323a-b225-eba1904a233b | -10.64005 | -49.90562 | 2024-09-27 05:27:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 984dd0ad-61a4-33db-b47f-0852eee7f463 | -10.63255 | -49.91101 | 2024-09-27 05:27:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5d7c76dd-d3f9-39ff-a5d3-29ae7e394f18 | -10.14293 | -50.00809 | 2024-09-27 05:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 65d05192-278a-3ea1-a80a-e7734d5a8d10 | -10.1362 | -50.00727 | 2024-09-27 05:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 569e5a99-9251-3971-b01a-fe96a35be113 | -10.13549 | -50.01328 | 2024-09-27 05:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7f611a17-2ec2-3913-84bb-cdd381cc9880 | -10.12878 | -50.01241 | 2024-09-27 05:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 318e4078-d722-3c8d-8343-c90717d6edc8 | -9.58768 | -50.13265 | 2024-09-27 05:27:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e6147369-f938-3196-9c6c-4c03b2517b06 | -9.58295 | -50.1326 | 2024-09-27 05:27:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e70d2bec-6091-3fb0-a0e0-df1028909b16 | -12.18327 | -50.81401 | 2024-09-27 05:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a52ce77a-93eb-30ed-9a4b-8e34dfbe8b53 | -12.18262 | -50.81966 | 2024-09-27 05:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4dd6a4a5-3e15-3461-8852-cd409b34b35e | -12.18198 | -50.8253 | 2024-09-27 05:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4be4f336-0deb-3756-b94e-dc1091d059be | -12.18134 | -50.83093 | 2024-09-27 05:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6d462717-f15e-3ef3-b884-91d2b874bc25 | -12.17606 | -50.8189 | 2024-09-27 05:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 15027100-1435-322d-8f44-d9e069456c1e | -12.17542 | -50.82453 | 2024-09-27 05:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 6b08b67f-3770-3633-91a3-48fc58e33339 | -12.17478 | -50.83017 | 2024-09-27 05:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a95c9e38-c667-3727-9fe1-cfbc2a7f26d6 | -12.17078 | -50.8068 | 2024-09-27 05:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e728aa99-7eca-3c31-b680-b05d96c65624 | -12.16823 | -50.82938 | 2024-09-27 05:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 4b299a84-584c-382d-89ae-1831f67a783e | -12.16759 | -50.83501 | 2024-09-27 05:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1ea343d7-7b6e-3bf5-b235-0eec97f64b8c | -12.16421 | -50.80603 | 2024-09-27 05:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac813b6c-9053-3c2d-afa8-9bbf269a813c | -11.84095 | -49.63041 | 2024-09-27 05:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2f9623c-5999-364d-8452-f796c0f20f00 | -11.83318 | -49.63631 | 2024-09-27 05:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39fa67d7-c22a-3b43-b8f2-5dd93dabcdae | -11.83151 | -49.63562 | 2024-09-27 05:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc5277fb-56e7-3f05-a8f6-472175ac0984 | -11.16366 | -49.731 | 2024-09-27 05:27:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3eeac061-3bbd-3c5e-8630-531883488eeb | -6.12411 | -51.1263 | 2024-09-27 05:27:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ea064eb6-e465-345a-a239-55a610bd9011 | -6.12353 | -51.13047 | 2024-09-27 05:27:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8219e3dd-5407-3f41-ac92-ca2f6f6e91e2 | -6.11816 | -51.12543 | 2024-09-27 05:27:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 07a8d195-d236-3a01-a03e-36dd5624094a | -6.11228 | -51.12405 | 2024-09-27 05:27:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a8af490-8492-36ad-84fe-203ba208f928 | -6.11176 | -51.12778 | 2024-09-27 05:27:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e01c67f2-5f0d-37d5-8923-8f96a1d6eb9c | -6.10756 | -51.11435 | 2024-09-27 05:27:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d53d8cd3-0bf2-3ecb-b94a-f84d4da2852a | -6.107 | -51.11835 | 2024-09-27 05:27:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b184f3b-d4c7-344c-ba07-4393ff6cf07e | -6.10645 | -51.12235 | 2024-09-27 05:27:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 533ddf08-6311-3a12-8b76-755c0c009baa | -10.72318 | -51.07162 | 2024-09-27 05:27:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 58270828-d34b-3b23-a1d8-950aa20a3ea6 | -10.71804 | -51.06049 | 2024-09-27 05:27:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58586812-1092-3989-8c28-197c8949c2f2 | -10.61244 | -51.11341 | 2024-09-27 05:27:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe32ba98-6444-3ade-8a2b-654cfe830915 | -10.60612 | -51.11265 | 2024-09-27 05:27:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 393a7c9c-cd8b-361c-a139-54f96eb21e90 | -10.49486 | -51.23414 | 2024-09-27 05:27:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 886cc7ba-4288-3e9e-bacb-17c57e8ae881 | -10.4932 | -51.22984 | 2024-09-27 05:27:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f37dee34-31ce-3c61-bf9a-b161f3dc02b7 | -10.49264 | -51.23454 | 2024-09-27 05:27:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 12750ade-ba38-38ac-8877-d5b2eaea058d | -10.4891 | -51.22931 | 2024-09-27 05:27:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 26c90913-eba6-385d-a5a6-6b8070af9f79 | -10.48851 | -51.234 | 2024-09-27 05:27:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db118727-ee9c-3bd9-aaee-e90b66c1f385 | -10.48687 | -51.22955 | 2024-09-27 05:27:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6ec241f-d588-3ebd-b69c-1e897be9de6b | -10.46943 | -50.75532 | 2024-09-27 05:27:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 124f60ae-9a5e-336d-80df-4b15b63ace1a | -10.46875 | -50.76102 | 2024-09-27 05:27:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1487eef3-3f15-3870-8166-02625e1f9350 | -11.12639 | -50.83338 | 2024-09-27 05:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5617fb87-0466-3725-aad8-d3c489c1645c | -11.12575 | -50.83882 | 2024-09-27 05:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 723ed58f-6a76-361d-a855-e18ade200d81 | -13.30291 | -51.35248 | 2024-09-27 05:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09af44ba-bb8c-393b-9e01-33117af9f82d | -13.22602 | -51.27068 | 2024-09-27 05:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aed94d05-22f0-324a-975d-401230b18234 | -13.22549 | -51.26794 | 2024-09-27 05:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7dec98b7-ed3f-3f89-9664-6f2d7c053342 | -13.22487 | -51.2734 | 2024-09-27 05:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8800a41-1b27-32e0-af32-dd1593c3f9c1 | -13.22013 | -51.26448 | 2024-09-27 05:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cbc1f1fb-3d38-3131-8575-42e13ce3519a | -13.21955 | -51.26994 | 2024-09-27 05:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ad911608-5952-37ef-b884-8ee3e6a4b3b8 | -13.21903 | -51.26721 | 2024-09-27 05:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f744c097-24e6-36a1-a1ed-856abcaa98cd | -13.21366 | -51.26372 | 2024-09-27 05:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bfb35ef1-c0ce-369c-8b9f-93fe787b2c14 | -13.21317 | -51.26102 | 2024-09-27 05:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cc7147fb-a62e-3bab-8fdb-75aa8b8592db | -13.21251 | -51.27465 | 2024-09-27 05:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 083d9ddd-9559-3dfc-85a6-f5fce1fc4a72 | -13.21195 | -51.27193 | 2024-09-27 05:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 15588911-09ba-3328-a5ab-b40f51a75448 | -7.79389 | -52.40435 | 2024-09-27 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c274ea5-845d-38e7-8d31-75f49967819e | -7.79344 | -52.40762 | 2024-09-27 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e599c1c4-e1f4-367f-8b5e-b624c214594b | -6.59917 | -52.30366 | 2024-09-27 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5d3c04d-5db3-3355-8b1e-5f9aaf5a7f5e | -6.59864 | -52.30743 | 2024-09-27 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9178a641-50ec-3608-bf98-8ef24dd9384d | -9.10571 | -53.30156 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55714d7f-81f5-3d71-adf6-fbb2708b063b | -9.01175 | -52.11695 | 2024-09-27 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c84273aa-18f2-354e-9b49-577cf2a93bc4 | -9.01131 | -52.12039 | 2024-09-27 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 032c9b4b-7d33-36ed-9c65-831cfd134025 | -8.99178 | -52.1347 | 2024-09-27 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9402bd4f-ff68-37f0-a0fd-5bcfd060ee34 | -8.99165 | -52.1363 | 2024-09-27 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71e0f538-b8f5-3ca0-a9c7-d583c6f59655 | -8.99126 | -52.13884 | 2024-09-27 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64c1fcfa-0c0d-3bb9-a9f8-2d94b8bd9032 | -8.99112 | -52.14026 | 2024-09-27 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8cf0df66-9065-3221-a075-ee7ffb80bbdd | -8.98535 | -52.1393 | 2024-09-27 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fb039a4-e192-3ae2-81d8-b1b8f9948f20 | -8.985 | -52.1417 | 2024-09-27 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42300356-e6a7-38f7-ac94-627667eeb9e2 | -8.9796 | -52.13813 | 2024-09-27 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 538b0658-cab8-32f3-b146-1f7e41c613c2 | -8.89567 | -53.02229 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7595062-db2b-379d-844e-1afa39fae2d6 | -8.89432 | -53.03271 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2e7c2e90-dd1b-32cf-af1e-92f44534289a | -8.89389 | -53.03601 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d59f383-e7d9-36da-a735-4ff2199b2bef | -8.89016 | -53.02182 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46988a12-b9b3-3476-b64a-f4eb37ea045b | -8.88881 | -53.0323 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 858b9840-7041-3679-bf45-15959d4324c2 | -8.88425 | -53.02449 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e35cc3d-3107-3f0c-94a4-b9159317438f | -8.88379 | -53.02806 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a8ebe2e-f7dc-3796-a263-828afa260faf | -8.8834 | -53.02458 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73f111d6-b021-36d3-a783-df6c368ad317 | -8.88291 | -53.02814 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 85fb4ca5-5118-3a2c-8d2f-dd90098bfccf | -8.67131 | -53.19067 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a622d18-17eb-3ac4-886d-cbd7c0527791 | -8.6709 | -53.19373 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 63d5baa3-6eb8-3295-aedc-699668d2b13c | -8.66178 | -53.17958 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 225dd56a-75cc-3cc3-9bdc-9b5184facfba | -8.65637 | -53.17903 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3fb27bb9-7ac3-39ec-9784-9c4096389367 | -8.65592 | -53.18248 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bae855e-05ca-343d-a22c-1327594b5292 | -8.65338 | -53.11728 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 640d7e7a-3052-31fc-84a2-a886b4bf0163 | -8.65298 | -53.12038 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1327180-ceba-324a-9bd7-3421ead91656 | -8.65174 | -53.11549 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8d6f5c5-bc1a-3304-9aa9-4348d31ae695 | -8.65132 | -53.11859 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c62dab6-c5a3-305b-9444-60ae4a375fd3 | -8.65053 | -53.18166 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README114.md)
