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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca4b879c-dbec-36ae-b38d-f53cba73f02c | -6.80951 | -52.81738 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e39360e-f7a2-32c8-aa15-a29466326725 | -7.08754 | -49.92158 | 2025-09-01 04:32:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17453177-7542-3741-8f96-784cf5712187 | -5.80928 | -47.8807 | 2025-09-01 04:32:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbd0d7d5-ed62-307a-9aa0-64800e74a9c0 | -8.29866 | -46.32241 | 2025-09-01 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5943283c-86c4-3fd0-840f-f53c90bf2509 | -6.80415 | -45.68388 | 2025-09-01 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1413053-351f-3c7a-82cc-3c1886db440e | -6.19959 | -45.38212 | 2025-09-01 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7058d4ff-ad2c-3514-b520-9a784118693e | -7.38363 | -47.43598 | 2025-09-01 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 937a1805-a993-38cf-97cd-52834cc6411c | -9.00928 | -50.11915 | 2025-09-01 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9457ad3-9846-3627-811c-d307d19c5548 | -6.29804 | -43.62211 | 2025-09-01 04:32:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9249eb36-fddb-3354-8648-87a305ba14ef | -7.08694 | -49.9253 | 2025-09-01 04:32:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ad9d9e6-2969-3b0d-9497-9c117497d9ab | -6.15845 | -43.31891 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9113723a-84f5-3828-96de-4511d0421852 | -7.08191 | -44.35489 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| ca156488-ad64-3313-a4ee-8ebac5a8759a | -9.15208 | -45.22107 | 2025-09-01 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77c3cc8e-c294-36e6-8513-8a282954724f | -7.67361 | -42.65614 | 2025-09-01 04:32:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 368d380d-d2e3-3a55-be4c-ee378a77ff8c | -9.69884 | -48.28519 | 2025-09-01 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7cfc219d-8555-3bcf-ad30-5dda55431a1a | -8.06113 | -48.41978 | 2025-09-01 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29e1028c-1f55-32eb-8578-40755be62351 | -6.42127 | -43.96196 | 2025-09-01 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f5f14ac-35b9-34a2-a0a1-196cc802f92e | -6.28794 | -43.55715 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e058c387-b802-3fcd-b677-9b24aede5346 | -4.15545 | -46.77827 | 2025-09-01 04:32:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 267adeb4-8802-379c-a4c4-2f140e03b85d | -9.22644 | -47.1032 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 787f72df-6555-37fb-92d0-1b2149442c11 | -7.73084 | -50.25666 | 2025-09-01 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 92540416-9d1f-33a3-bd19-df8b7f623b63 | -6.51761 | -43.54657 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c671abef-fc52-36d3-92ce-cd5f2138ef3e | -6.45655 | -43.96101 | 2025-09-01 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 61695dfb-26fe-3e42-9887-4fd8b508e2ab | -6.30709 | -43.61406 | 2025-09-01 04:32:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa918e15-dd83-3b26-b05a-6dc499c23878 | -7.11005 | -44.76426 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0eef93a8-b3fe-35d5-83b8-f0c043442092 | -6.97855 | -43.11327 | 2025-09-01 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a3e07380-7ff4-39d7-a441-c43ce4369a85 | -7.63133 | -42.65428 | 2025-09-01 04:32:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a331a7e4-52ce-3722-b643-9e4074a1edbe | -10.60337 | -44.3245 | 2025-09-01 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 588a8150-ecbf-328c-8498-887c1c3ae77a | -7.06592 | -44.33463 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 5b89b266-66ef-37af-aaff-f848245c1f59 | -6.18131 | -43.35257 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4ac7722-c679-341a-8108-d04c35c03c3b | -11.07791 | -44.73884 | 2025-09-01 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84edb4d9-1bbd-31a9-84d2-97b11296b9cc | -6.76834 | -44.62735 | 2025-09-01 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e00c97cb-64aa-3605-affd-3836336f0cce | -6.70967 | -42.25277 | 2025-09-01 04:32:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 3074cee3-354e-3e19-8337-e3be778bc64a | -7.87686 | -45.17499 | 2025-09-01 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe0c1797-e267-3c6d-a538-9aa76b7ebdb4 | -9.13865 | -47.95963 | 2025-09-01 04:32:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b5cc27d-a279-3152-bd43-aefa09596882 | -8.83626 | -47.50072 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80a68a11-06c5-3146-b11d-df7af857bd6a | -7.50838 | -45.83647 | 2025-09-01 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f63c33c9-af84-3e26-a9d0-a99dd1c0caa9 | -8.29923 | -46.31866 | 2025-09-01 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a92f3877-376e-3144-90ee-3b5a09a39a87 | -6.36882 | -44.45076 | 2025-09-01 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 92f1efc4-18f3-3d6a-8c32-b02764a9c535 | -10.04625 | -48.10291 | 2025-09-01 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c250a0f4-bd69-38d0-9102-e0ef516d36e6 | -4.06791 | -47.95929 | 2025-09-01 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2361025-3148-3170-b5a5-e5afa8ea4199 | -4.15822 | -46.78226 | 2025-09-01 04:32:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0676df6-9168-3da4-9dec-d3659abd33bf | -4.04767 | -48.93674 | 2025-09-01 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87b82c1d-4413-3442-b74b-9738a11a8b14 | -8.85296 | -52.02572 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9db37292-b4d3-3402-adaf-8a96f49cdff6 | -6.63646 | -44.25932 | 2025-09-01 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2aed3a3d-e84e-3d6e-8189-3dab55b8987b | -6.15868 | -43.34405 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| afac8778-8649-3a3f-86b4-e632032362d9 | -6.49662 | -44.07847 | 2025-09-01 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 76f32a6b-77cf-3fc4-8b7d-6ef03afed207 | -5.83518 | -46.12996 | 2025-09-01 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b1ba25f2-751b-3f31-b4ee-112a155165eb | -8.8259 | -47.80935 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35f741cc-13f2-3511-a931-ef9b56b76f54 | -8.19179 | -42.30114 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f832ee14-ef31-3b39-bb4b-3d1ba3c604db | -6.98203 | -43.11736 | 2025-09-01 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b35929bb-d816-3426-94c8-aab701a76391 | -6.82536 | -52.82022 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 755547df-c6f7-3626-98df-7852856f8eb9 | -7.72115 | -50.25552 | 2025-09-01 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c60078c-dc95-38be-b003-685835182932 | -8.05727 | -48.42273 | 2025-09-01 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9bcdaa1a-15fd-3f55-b236-4628ba77fa85 | -10.88766 | -45.80588 | 2025-09-01 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 57b5bc8f-e9fa-3f88-b942-c953c19a4820 | -6.87221 | -45.14684 | 2025-09-01 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 219d846a-8226-3f79-b9f0-93b92abee897 | -5.73081 | -45.53723 | 2025-09-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3fc86452-db98-3129-a5b4-4ca16551b0c7 | -7.55479 | -45.94089 | 2025-09-01 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 490f82ad-b2ea-3962-a573-72419e1499a6 | -6.53578 | -42.96261 | 2025-09-01 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23a44321-2ec5-3568-82b9-a5ca5fba05de | -7.06124 | -46.24076 | 2025-09-01 04:32:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5966da6-10d5-3134-8474-e5b62cb2f6a8 | -11.04453 | -45.13842 | 2025-09-01 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e770577-a42b-3a89-859e-9a3adf9a547b | -6.83415 | -52.81641 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 260de348-05df-35b1-8d8b-a844eec54652 | -7.88314 | -46.99627 | 2025-09-01 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f7beed0-751f-3942-aad3-ee0e696fa30d | -7.70662 | -50.28001 | 2025-09-01 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f0d414f1-f10e-32e4-9410-5dbde2878a70 | -7.69159 | -61.48046 | 2025-09-01 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b9673b94-dab8-3fe7-9445-b6805900f029 | -7.94158 | -46.41375 | 2025-09-01 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b234db8-7df1-347f-a727-8ef34f264942 | -6.33456 | -53.44115 | 2025-09-01 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d52049c-aa99-3aa5-a716-47a625eb31ab | -6.32813 | -53.42826 | 2025-09-01 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f0350d8-946b-301e-ba80-b1f63903db1b | -6.53281 | -42.95491 | 2025-09-01 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b0aa3ea-155c-3ec3-b1d3-1a970057895c | -7.15928 | -44.91305 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b2b9bad-8c65-31d1-b50a-4e4d2e51feba | -6.82932 | -52.82093 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3b8c6f32-70cd-3239-87e7-1107df00f222 | -7.95063 | -46.35444 | 2025-09-01 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79be9092-ed9b-3092-a655-d55c0a7ce24d | -9.64111 | -47.80795 | 2025-09-01 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d97bce15-1d71-304d-918d-b06e5d1bcea3 | -7.10815 | -44.77691 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9cc7ed19-2511-3915-a9f0-9fd92750c7ad | -9.21914 | -47.10577 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6175c35b-b311-31c5-b678-2ec0658afce7 | -6.83965 | -43.34119 | 2025-09-01 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bb0198c9-d060-3304-91d8-ddac05259d52 | -7.08761 | -44.34219 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| c0d7ed38-e49c-316c-b309-7aec8a4e0d96 | -6.75363 | -43.78508 | 2025-09-01 04:32:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 26.3 |
| d0307b65-c552-37a1-b611-6dbc877b9217 | -6.33185 | -44.47351 | 2025-09-01 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9aa7e719-4fda-3667-a31a-b09d5443ca30 | -6.29268 | -43.78955 | 2025-09-01 04:32:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07537763-b9a9-317e-a984-88086a6c7034 | -9.63447 | -47.82863 | 2025-09-01 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3cab3e95-9783-3468-8818-09912e42195c | -7.69192 | -46.71688 | 2025-09-01 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 570100a6-5ff4-3a2a-8d09-1dc841f3d99f | -6.95337 | -44.33723 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d72d5cb7-9197-36a2-9507-7c98d1833c80 | -7.24563 | -44.23969 | 2025-09-01 04:32:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 9229ff69-f476-389a-b01b-3e79cf7ebbaa | -7.57105 | -45.20629 | 2025-09-01 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99e2e920-67b8-3288-854e-8cc720d80aea | -7.39557 | -45.93373 | 2025-09-01 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6cc5ac46-0818-344c-bdd1-6f30c6803647 | -6.82165 | -43.33135 | 2025-09-01 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d9045cca-0a35-37d7-ad58-439c107feabc | -5.40154 | -42.34227 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 588c5a18-6199-3ec4-85ba-2b8ea452d6ba | -8.84348 | -47.49823 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4b6c3919-189d-3e04-972f-b69ef720d1cd | -8.12604 | -45.0154 | 2025-09-01 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d31cffe2-063f-3969-b7f1-c758a4682ab9 | -8.8812 | -47.20851 | 2025-09-01 04:32:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23797d10-aefc-360d-8fae-22833af8a12d | -5.81971 | -43.226 | 2025-09-01 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 49bb730c-03ed-3c33-b9c7-6432aeacd0d4 | -6.27856 | -43.52852 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ffa1d588-802a-3481-bd65-60e4200275f2 | -7.09002 | -44.35151 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 37.9 |
| bd99447b-1847-3f01-9c50-fbeb8f88796d | -6.14915 | -43.32773 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9ee58cd8-7109-3aef-af2a-c0e14d5c782d | -6.18127 | -44.21367 | 2025-09-01 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7e32ca5-3bdb-3ee9-9595-b9cba18ef490 | -8.25393 | -47.18536 | 2025-09-01 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f3c6d72e-739b-34e1-a065-241b9d1f1190 | -7.67382 | -61.09425 | 2025-09-01 04:32:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 26c1a778-a806-39ab-90c6-4c33dce1626b | -9.22871 | -47.11096 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 099855af-fd23-336e-a11d-213629635028 | -5.95708 | -45.17398 | 2025-09-01 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README54.md)
