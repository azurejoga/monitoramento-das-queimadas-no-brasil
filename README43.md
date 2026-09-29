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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d2a4c1d-d7c1-36c6-bd99-f28dfb924125 | -11.62659 | -41.83404 | 2026-09-29 04:51:00 | NPP-375D | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f5a34d65-b68d-3c17-8733-676ea78b6faa | -12.77756 | -54.02849 | 2026-09-29 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7a116447-c44e-305a-9f9a-75a92de47757 | -11.98777 | -50.94242 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fce9a049-97d5-3798-b942-0a2db6fcb30d | -10.41755 | -53.78187 | 2026-09-29 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb22d28f-2453-3bfb-9cff-84f9e5786a06 | -11.99663 | -50.95107 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 531fd8be-3fbe-3534-a770-5599968ac816 | -12.71433 | -46.9996 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b9c41378-b86c-3ec2-99cf-cc5839f6c3b4 | -11.43611 | -43.45008 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8482d260-127c-361f-8cc9-9dfb8f6a1d53 | -12.05584 | -50.93898 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3434e90d-6ec0-345b-9628-188d211ca151 | -11.41417 | -43.43712 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4f504545-0c66-3025-b7ee-51d820387262 | -13.06438 | -47.44892 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6991b2de-07b2-350b-aac5-fbf08c026090 | -11.128 | -50.07204 | 2026-09-29 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab49c700-2ade-3474-b3a2-914ac9c241a9 | -11.35667 | -54.03847 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c984de18-da7d-3b63-bd35-2c76e0c988d6 | -11.35211 | -54.11024 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03c4f30e-457a-3301-866d-9be5578bea61 | -6.31833 | -52.61843 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72d15ca5-a5aa-3f73-aa55-ba92126d6620 | -11.90141 | -50.61276 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b2971634-59d3-38fd-854e-8431fbbb91e1 | -11.38207 | -43.39265 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52554c07-e2bd-3c85-a694-623791b14e4b | -13.45669 | -48.58373 | 2026-09-29 04:51:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e81d3f4c-d9ac-34e7-8001-1618909d3350 | -11.44409 | -43.46115 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c1fcbcad-6a51-35bc-876f-10e273c876ea | -9.95357 | -50.14296 | 2026-09-29 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9be5dfdd-5e09-3e7d-97e4-6fea7bde290e | -11.83476 | -45.02131 | 2026-09-29 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75bbbefd-8b95-3bd2-8263-6f7de43d7cad | -9.82379 | -44.93872 | 2026-09-29 04:51:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 713e62ad-db35-3a5d-bf07-8dd38ffba47b | -12.77181 | -50.67067 | 2026-09-29 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47d4a494-6e77-378c-a278-eae91633ce95 | -9.168 | -61.40798 | 2026-09-29 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e90defa1-d49d-39a3-92ba-7e0b31e6591c | -9.79323 | -48.19812 | 2026-09-29 04:51:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d266d542-1b56-3df6-a1d3-75b0e2ce49ab | -9.76122 | -44.83217 | 2026-09-29 04:51:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f23216ef-2271-3720-9cae-ee5444904c51 | -11.39473 | -43.45275 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 88fec58f-58c3-3dd3-a0e7-5956e3b8c84c | -9.80073 | -44.83361 | 2026-09-29 04:51:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47bd84d9-fd19-383e-bad5-76577b78ed79 | -12.00888 | -50.93864 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 87461e91-1ff6-3487-ba73-645310581faa | -12.63125 | -47.2561 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 636339c6-1a97-34d1-b123-3078c4b61d25 | -9.76428 | -36.97367 | 2026-09-29 04:51:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 6.6 |
| bafe2c62-bb41-38ca-903a-bee567ae9164 | -11.71302 | -43.45435 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac688364-d50a-3652-9f7c-3ec8a9d77b79 | -10.71502 | -44.42261 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 108d1112-67f5-3477-a770-8765ef288331 | -14.12546 | -46.29035 | 2026-09-29 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 638a0289-e27d-33ad-8faf-cd40e01d141d | -13.06373 | -47.45333 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15ec2e9b-9cbc-346a-bfc0-4ec1baaec46b | -12.05566 | -46.46875 | 2026-09-29 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 77b2372b-f1c5-3a47-ade5-7decb4d04d74 | -11.43277 | -43.43967 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8163415a-2d7f-3fb2-a530-8bf72037205b | -8.21494 | -45.45928 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bdb3cba6-a78f-3862-96a0-e59907b9cfad | -11.14078 | -50.07772 | 2026-09-29 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| be17a43f-8f11-3a6a-b118-e3108bf9d9e9 | -13.38414 | -51.32483 | 2026-09-29 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 947bd6ea-e5e5-3520-b6db-fe4fff32814d | -6.15587 | -52.90764 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50fba8fa-a40e-38ac-9d7d-f8aaa618fdff | -11.13134 | -50.07257 | 2026-09-29 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89adf474-59c2-3bff-997e-dd0948a8be2d | -11.67787 | -44.53194 | 2026-09-29 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 651ff540-9b19-3e17-9400-2dd89b3907f4 | -9.14403 | -49.97751 | 2026-09-29 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0bff518d-54d0-32e0-a2af-cdbbd30136b1 | -12.17557 | -50.69345 | 2026-09-29 04:51:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 53979de9-3eed-3abf-85ea-80678dfe12d7 | -12.01643 | -50.92886 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3e5b51e7-f5a0-30db-b98e-b12c20a0571a | -12.79416 | -54.01837 | 2026-09-29 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 215c2309-6cfe-3de2-adcc-86d2f0aff9d1 | -9.16674 | -61.40947 | 2026-09-29 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2e8ebb20-d274-317e-8d11-6a963e279cb3 | -12.68984 | -47.25341 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 488e9528-5d40-3519-817c-7b252f69e8c2 | -8.7208 | -47.60571 | 2026-09-29 04:51:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a52c1bdd-47e9-37fb-a655-73116907680e | -14.12218 | -46.2845 | 2026-09-29 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 25.1 |
| e37f3817-6adf-3049-ac79-74013b75f99f | -13.45319 | -48.58312 | 2026-09-29 04:51:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6af1901-f88d-369b-b394-412cc7ff7da4 | -9.85657 | -44.94384 | 2026-09-29 04:51:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6a909f0-2803-37ed-8dd8-6174d4d5acce | -11.16691 | -50.04207 | 2026-09-29 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dcec520b-02de-38bc-8afa-df36028d034f | -11.05511 | -54.19997 | 2026-09-29 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a415073-6d1c-3c02-bb7c-d5f69a866a7f | -11.96834 | -50.93559 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1738800e-25b6-32da-8211-a16d6899ac0f | -10.81811 | -48.74347 | 2026-09-29 04:51:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bfffcd74-5b7c-390b-b332-250c8b879a24 | -11.38538 | -54.04804 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9074c28f-ce8b-320e-bafd-a1957e458bde | -10.48098 | -46.77089 | 2026-09-29 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dcd89d4c-b931-391d-97f6-6178a6640186 | -9.77057 | -36.97982 | 2026-09-29 04:51:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c3738820-b08c-3cd2-9372-e2ed349dd1e7 | -11.42412 | -43.4335 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4e6db6fd-c52d-3006-8495-ba591ff42f0a | -11.37432 | -54.04614 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d935399e-6cb7-3499-bc89-1117ced31528 | -11.12356 | -50.05683 | 2026-09-29 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 045a6302-b34f-3689-9934-ac1472c504d0 | -12.62256 | -47.26385 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42b006be-9673-3046-8422-34724ecb2641 | -9.958 | -50.15805 | 2026-09-29 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f23fe9f-f0e9-35ae-b952-610b7d7bca55 | -7.52354 | -45.08994 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 467d3ade-5dd9-3844-84f6-6e117dc855cc | -12.71685 | -46.98169 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5edcbee9-99d3-34e3-a1c0-aedc895a5eb7 | -10.51953 | -45.36695 | 2026-09-29 04:51:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d1ad83ed-05ba-308d-97c3-34a5077cbc42 | -7.46261 | -45.81931 | 2026-09-29 04:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62e999e3-9135-3f87-9861-9ff2c4197716 | -12.67657 | -46.99607 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7461ca80-7263-3b93-9583-04add88fe6df | -8.21815 | -45.46449 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| be51b51b-069c-351d-a592-a00138e9c2cb | -12.59178 | -51.96607 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef7b354c-84c6-3c13-9a1c-a1e6a6e8a484 | -11.36277 | -47.43861 | 2026-09-29 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39aa46ae-ca18-33e0-b626-b20304867283 | -14.4309 | -42.3115 | 2026-09-29 04:51:00 | NPP-375D | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9ca81409-8c08-3dd0-a962-bf887708771b | -12.05138 | -50.94551 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74fff1a9-c9ab-38dd-bd3b-be1a2bb4c3b7 | -11.37801 | -54.04678 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fda792c-ae41-3763-83fd-b29169dc27a5 | -12.03918 | -50.93624 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 35f669c2-4b2a-398a-9c2b-e9bd95189d0e | -8.43111 | -44.84949 | 2026-09-29 04:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee1ce51d-e7d7-3694-8085-23099f8b71ef | -11.13467 | -50.07311 | 2026-09-29 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e5ff960-4bab-3010-86bd-fcdc60903479 | -12.04471 | -50.94441 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2a8b43ef-abf8-317c-b74d-a7f7b6eef710 | -5.3053 | -55.8324 | 2026-09-29 04:51:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba282dfa-2036-3a91-8de1-f2e6a2cffa9d | -7.41012 | -40.21912 | 2026-09-29 04:51:00 | NPP-375D | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f88a851b-8815-3959-9f84-f0cc4fc22dd7 | -12.69291 | -47.25845 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82871835-8150-3818-b9a2-9256993d07be | -7.26032 | -45.33635 | 2026-09-29 04:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 886f8b93-4772-33b6-ab21-83a97a99b8e6 | -13.17128 | -48.56668 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eba8eb14-2f78-349c-b453-2b7a41f6783f | -12.70493 | -47.3328 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2192cc5-f1c8-3754-b4a7-e2f76f0409f1 | -12.14119 | -45.00415 | 2026-09-29 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b7245875-ebdc-3e9d-bc3a-e67a6d4c4b4c | -11.39812 | -43.42831 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 459ef226-f6db-31f3-97c8-407b2597a924 | -13.20746 | -48.56438 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a7d9b884-3df0-3e05-9329-61ac6f112318 | -11.50191 | -47.40559 | 2026-09-29 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e79f8bd6-d3c8-3e11-9216-4cbbc11ab8ff | -7.43186 | -46.87568 | 2026-09-29 04:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ec0cb3c-a3d1-310c-be05-06db89abe6e0 | -12.17224 | -50.69291 | 2026-09-29 04:51:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93f3329c-fdc7-315c-9246-22b48b6ddac2 | -7.69515 | -48.86683 | 2026-09-29 04:51:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 926edf23-15ce-347d-ace9-4b74a01932ea | -12.94024 | -46.65983 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc0b79d3-ec47-39a1-b620-716fdfdf95ea | -12.15869 | -50.82125 | 2026-09-29 04:51:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 26989920-a528-3f34-a600-644bd5a97e68 | -7.52035 | -45.08424 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4565ab7b-6600-3134-9dca-bbdee8eeab69 | -7.47591 | -45.80769 | 2026-09-29 04:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7352f65f-aef7-31c9-b020-1f619e6b08ce | -11.87103 | -50.45927 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3be4bd07-fc10-3757-93e8-e71e0f5b3e5d | -11.30172 | -43.54758 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa6cb558-bc76-3e77-b116-c6724d105cbe | -7.67597 | -44.89222 | 2026-09-29 04:51:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5c5f3e04-a664-32f6-b440-58a27046fdce | -12.90426 | -52.04057 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README44.md)
