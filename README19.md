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
| d85c59d2-61cb-3b9d-8837-61f55a9eefca | -4.89479 | -49.96687 | 2025-09-05 04:34:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a82c14f-cc7d-3fe1-83de-14c5a9847182 | -6.59386 | -44.5574 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| fb05c255-96a3-3ab6-b4c8-efae8f74a5e5 | -6.98882 | -44.32683 | 2025-09-05 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1257c653-971b-3e3d-a49a-501d24a210ba | -8.0054 | -44.77261 | 2025-09-05 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7fa715b-f9f2-3fa4-ad22-000387c21f50 | -3.67931 | -49.02414 | 2025-09-05 04:34:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c788b45-d178-3851-8b2a-8f06e79b92fc | -3.68393 | -49.01727 | 2025-09-05 04:34:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71d2b622-d6a2-3769-90c7-07a8c6c9eec0 | -6.42651 | -49.74741 | 2025-09-05 04:34:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33bc049b-f0c0-3d3a-afa1-256447927d6b | -6.39779 | -44.69274 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 179fda7d-5301-3efd-b1ee-6954a46dc951 | -6.5506 | -43.7249 | 2025-09-05 04:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32e7da1a-7fd9-3622-b037-a906aad5d73e | -6.22793 | -45.64612 | 2025-09-05 04:34:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3dba829a-3203-3486-87ff-67df7f19002f | -6.27418 | -53.44059 | 2025-09-05 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59994a17-413e-3714-8b21-905fe296c4cf | -6.46314 | -43.56435 | 2025-09-05 04:34:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f095cd0c-2f27-3e63-a497-fd06130f1cf8 | -5.53712 | -46.43385 | 2025-09-05 04:34:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10acc596-54c4-34ea-89e1-7d25611a7026 | -3.32435 | -54.90816 | 2025-09-05 04:34:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5d6facd-c215-30c2-9350-087fb22321b2 | -3.15986 | -48.60216 | 2025-09-05 04:34:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fb1d993-fcbb-32b6-8e2a-6683d83ffa24 | -6.24926 | -43.28481 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 96b109fb-6467-3d7d-bbca-f2c4eb05cd94 | -6.30043 | -43.50164 | 2025-09-05 04:34:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aba015bf-d957-3442-80a6-0202f86956c1 | -4.27317 | -48.18865 | 2025-09-05 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df46c82e-3e2c-3ae6-80f7-134685b76791 | -6.96324 | -43.95636 | 2025-09-05 04:34:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f12ddf49-e78e-30c8-9bc7-c756837714cf | -5.01515 | -48.46896 | 2025-09-05 04:34:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e0b40c26-0fbf-3c6e-b4c8-25cf5d69e10c | -5.20357 | -43.69693 | 2025-09-05 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f490745b-41d6-33f2-9afb-d061796c8a62 | -6.62189 | -43.97325 | 2025-09-05 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e781b2a-951b-352e-a19e-93f0021ef423 | -6.99884 | -44.94979 | 2025-09-05 04:34:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9da9c0ac-c25f-3768-b2a1-30421c5297f4 | -6.26019 | -53.44618 | 2025-09-05 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bed80ac-66e4-3277-b6a9-c3b65bda5b4d | -3.48881 | -48.94897 | 2025-09-05 04:34:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| adc421a9-a674-37a4-bc74-8650c13aea24 | -7.88881 | -45.2443 | 2025-09-05 04:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a096910-ab63-372f-98be-954390e4d0eb | -6.24769 | -43.29232 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31faf408-4d5d-32b6-8797-a5d88832eb9e | -5.45252 | -42.81616 | 2025-09-05 04:34:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3ca383a3-3c2a-3914-900a-83cb8a484545 | -7.29497 | -43.7364 | 2025-09-05 04:34:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 44f4a8b1-ea03-37f2-b089-e2ca56ea71fd | -5.4565 | -42.81679 | 2025-09-05 04:34:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f0ac2361-10f6-36d6-9d43-85a844b5fce1 | -5.20804 | -43.69296 | 2025-09-05 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e091aaec-7552-3bd9-8f37-02daf1788c15 | -6.05242 | -45.99764 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 043eec94-6e7f-3e9a-873e-0852b432203a | -6.42849 | -49.74716 | 2025-09-05 04:34:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 45dbbc66-f9ad-39b4-ba4f-cc485cb5aa63 | -6.16617 | -44.20942 | 2025-09-05 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0ea6f4f8-7c95-31cf-a67a-e802bf2804f4 | -6.37775 | -42.99011 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1c1051a-dd57-341b-a8d7-58164b5a967d | -5.64217 | -43.12625 | 2025-09-05 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b735527c-f04d-31da-90b1-cab9b3360da2 | -5.10754 | -56.13523 | 2025-09-05 04:34:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63622ced-e018-39d8-8167-cc27ae08505e | -6.58955 | -44.56113 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1b17c167-385c-3406-bd52-3b8ae1c95e03 | -6.1252 | -44.15418 | 2025-09-05 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 402a2070-99a1-372d-b4c0-bb54a0424a72 | -7.59885 | -44.67217 | 2025-09-05 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a9473f4-425d-3bb6-b677-6c5eacb60c1f | -5.76936 | -45.43555 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 80933a80-8503-3366-adf5-eb5fec9a0f15 | -6.11778 | -44.15305 | 2025-09-05 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4a8c68c-111a-3288-a372-03aa4c05a953 | -6.84114 | -45.52126 | 2025-09-05 04:34:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6e74455-6aa9-3017-a3ba-6c8a53f9ef93 | -5.53768 | -46.43028 | 2025-09-05 04:34:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed8cc9f9-614f-3424-b0a5-e80d382bca1c | -5.37984 | -45.94497 | 2025-09-05 04:34:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 897e858b-110d-3a81-ba8a-e6a935ec2463 | -6.17452 | -47.28452 | 2025-09-05 04:34:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 70ac415c-0652-3db7-ad7d-59056557eab3 | -6.11472 | -44.14812 | 2025-09-05 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b80bbf6a-d019-322e-936d-5ff8c7acaa5c | -5.2067 | -43.69978 | 2025-09-05 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 00a4b495-270e-3884-abc3-20032049e7a0 | -6.54989 | -42.95028 | 2025-09-05 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 15ba19a6-de13-3c13-b252-cb456669ab73 | -6.54624 | -43.90944 | 2025-09-05 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6a84ebf1-d03b-3289-850c-8bca12bbdd1b | -7.30308 | -44.07383 | 2025-09-05 04:34:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65b8ef75-475c-3ff1-9e78-eed31c2aa724 | -6.65372 | -44.09332 | 2025-09-05 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0778f724-9135-3d4f-8c30-2c07fba32996 | -7.60849 | -43.85332 | 2025-09-05 04:34:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5940ae3-6143-33c3-87c7-ee23cd431c63 | -6.11603 | -44.13929 | 2025-09-05 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36c8fc9b-1770-3230-a5c4-6cb0387c4ff3 | -6.87345 | -45.56642 | 2025-09-05 04:34:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 581bc802-9c28-3814-a377-f63dc6b26cdd | -6.60986 | -43.97638 | 2025-09-05 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76a60912-a520-3407-8068-6ec04b884680 | -6.21317 | -42.45226 | 2025-09-05 04:34:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bda25184-70f5-36e8-b0d8-a622a0cfbfd6 | -6.30343 | -43.58542 | 2025-09-05 04:34:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 220a4b34-e458-3fc1-8af6-14e2af8d678f | -5.54926 | -43.77803 | 2025-09-05 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9cc87087-89c1-3690-9ff1-80ca5898607a | -5.71798 | -43.10204 | 2025-09-05 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b672c6d9-de67-3466-af1b-b80c0a0e64b4 | -6.11537 | -44.14375 | 2025-09-05 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97cdd831-802f-3a71-ad22-9976c4e9e20e | -6.01971 | -46.70061 | 2025-09-05 04:34:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bcb7843c-87bf-3945-9b6f-8190a30bd7e8 | -6.23766 | -42.64751 | 2025-09-05 04:34:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 42f26a77-8edd-31cc-a681-372c9cb5156a | -6.31238 | -47.76893 | 2025-09-05 04:34:00 | NPP-375D | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a15fbb19-ec17-3006-9e5a-411ee46ed9d1 | -6.00124 | -46.68681 | 2025-09-05 04:34:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd40c774-5f9a-3bfb-9283-717ef1bd9c0d | -6.35032 | -47.09388 | 2025-09-05 04:34:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ce8cee8-3375-3991-85e9-594049d98b93 | -5.98845 | -44.73681 | 2025-09-05 04:34:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 283327d9-259f-3184-8bf3-ccc28cfaae67 | -6.38352 | -43.81227 | 2025-09-05 04:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5082bbb-18d0-3890-8d34-22d61c2eb812 | -4.48412 | -47.66826 | 2025-09-05 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d39ecd51-b66f-3143-8544-bba4e836522f | -6.22146 | -42.62124 | 2025-09-05 04:34:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 61c10408-68f0-390d-bdad-afdacb72b57c | -7.89587 | -45.23609 | 2025-09-05 04:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cbd5445d-c503-3c47-9424-b756697c4b36 | -6.51255 | -43.49825 | 2025-09-05 04:34:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 23cc35fa-982d-3900-a82d-50f739ad8c4c | -7.6633 | -46.70305 | 2025-09-05 04:34:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cc30cb34-a933-34c4-8c7d-e5b700146048 | -5.45795 | -42.81997 | 2025-09-05 04:34:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 72a23394-0798-3547-9f1c-ee868836db06 | -5.86807 | -46.10832 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59120f30-3abd-3f9f-bfa2-cd35c2771d46 | -4.78811 | -43.81829 | 2025-09-05 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 15dada96-6e7e-3f09-b736-24a4da53ccdf | -5.86467 | -46.10781 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea7b72d1-c9f1-3eb4-ad5b-bf9cb3aa0260 | -5.88388 | -45.96101 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd0efbff-6abe-365d-83e5-244f652e5943 | -5.39289 | -45.95075 | 2025-09-05 04:34:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0bb51273-3d52-3900-931b-0d4c30d8bc41 | -5.17019 | -45.4508 | 2025-09-05 04:34:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97e92bdf-64d5-3292-b5ff-570d69eda8fa | -6.59732 | -44.55643 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| dd8be5b8-2ad7-394c-9dd4-5d222ea2700c | -7.44366 | -46.13022 | 2025-09-05 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd129dd2-feac-35dc-b972-89be21e527cb | -7.90234 | -44.93708 | 2025-09-05 04:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 48270582-829a-3e3b-8d5e-f8a2eda2fe9c | -6.51709 | -43.57261 | 2025-09-05 04:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df8ddafe-77ee-3e49-8851-5267efe335b7 | -6.01272 | -43.3716 | 2025-09-05 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dc6bc18f-4019-3125-b1d9-e7990f8cb124 | -6.2113 | -43.57121 | 2025-09-05 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65ef7326-11e2-3258-948b-39fbf837ccb0 | -7.89785 | -45.23309 | 2025-09-05 04:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fd305872-3d0c-3bb7-87a5-2cf20295c7e5 | -5.74773 | -45.5526 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f78bdf0-b297-34d6-b7e6-9b13d50f9382 | -5.43508 | -42.86311 | 2025-09-05 04:34:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f4283364-725a-3b12-a7e4-d07d5c31abec | -6.01186 | -46.68485 | 2025-09-05 04:34:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6ae779b1-ea7b-3cb8-9583-0b651a11f0e8 | -5.7306 | -45.36308 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db0e0754-cb40-391e-b3d0-9f292bc31765 | -6.22214 | -43.32899 | 2025-09-05 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 009ccd04-bd9a-367e-bdd2-81cdd47fc01b | -7.27402 | -48.25263 | 2025-09-05 04:34:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83fc4a68-0ff4-37e0-9dba-566e3c08bcc3 | -5.49109 | -45.22949 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2daa1eed-4964-37d8-954e-b03f3a77bd9c | -5.0992 | -56.15287 | 2025-09-05 04:34:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07586443-1c34-338c-9eb7-06d8f91dbd42 | -6.89297 | -45.18287 | 2025-09-05 04:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e74ad21-89b2-3d62-8159-76717997be1d | -5.77966 | -45.27596 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf86e752-31d4-3ca6-9307-1a9fc62e5df4 | -6.90914 | -43.80816 | 2025-09-05 04:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| daa46961-51e9-3385-869f-441da57d82b4 | -5.79296 | -45.63921 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d295608-eb27-3636-9d6b-195378ad717d | -5.86136 | -45.6538 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README20.md)
