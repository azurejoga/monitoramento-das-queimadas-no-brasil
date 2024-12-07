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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b89e3c1-7fcf-3910-bc8b-daaba70d6ed9 | -8.27542 | -48.02455 | 2024-12-07 04:31:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c83815d-21c5-3822-8878-27b974b4b437 | -4.8817 | -47.23124 | 2024-12-07 04:31:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f2c0f2b1-ee27-37ab-bc02-854a7e4b9de8 | -5.28854 | -44.91323 | 2024-12-07 04:31:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d4b92ac4-edfd-3b46-8fde-ddec74be65c1 | -7.1742 | -44.99662 | 2024-12-07 04:31:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 83926240-7daf-39f9-83b6-f6adec937d4f | -4.32211 | -45.88669 | 2024-12-07 04:31:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc6de03d-767e-3f79-82d5-44f8b2836548 | -8.87748 | -47.27028 | 2024-12-07 04:31:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ee4edd6d-9c2a-31f8-9733-063fba6ee145 | -5.73466 | -46.52026 | 2024-12-07 04:31:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 65b497f6-d56c-31b1-8668-6dd30dc9bb55 | -7.17122 | -44.99201 | 2024-12-07 04:31:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bbbe8b0a-3291-3bcb-8357-6c3a1356783e | -4.42029 | -45.65871 | 2024-12-07 04:31:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e10a4c2-8c05-3053-b963-2480a40b47d2 | -7.17271 | -44.99083 | 2024-12-07 04:31:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9ae5d743-e59b-3803-a497-c2b6b33f80e7 | -6.48917 | -44.68142 | 2024-12-07 04:31:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e15108a-2e62-39d6-a21c-b604fb0211d8 | -9.10338 | -43.19675 | 2024-12-07 04:31:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 6e14083f-843d-3e10-a5d9-e27cf8d9441d | -7.17483 | -44.99253 | 2024-12-07 04:31:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| edace2ac-699e-3ec1-bd4a-98bd81d981bb | -6.00495 | -45.92679 | 2024-12-07 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 538b3255-bb36-3f6b-8ac6-69094b8660f2 | -4.03949 | -46.64814 | 2024-12-07 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 92af4c3b-5516-3264-abe7-a5e6dec67a79 | -6.2073 | -46.06244 | 2024-12-07 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4c4b90b-c1ce-3ffe-89fd-55ece36346ed | -6.00849 | -46.40096 | 2024-12-07 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c14096a1-942f-310a-b9f8-82f6cbd6414d | -4.42939 | -45.82446 | 2024-12-07 04:31:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dada9cd5-f68c-343d-b241-e4e7516bbada | -6.20388 | -46.06193 | 2024-12-07 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3ba539a2-2f10-3f38-b4fd-509b1e47a90d | -8.93587 | -44.24995 | 2024-12-07 04:31:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 32416e22-449d-35c1-9a84-d5856fed33a9 | -8.99375 | -47.42728 | 2024-12-07 04:31:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 029a1070-5a83-3323-af9a-1110ced697c5 | -8.27712 | -48.03547 | 2024-12-07 04:31:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e1c0af8-3905-38b9-8bd4-1cb39d4b3733 | -4.14348 | -46.58907 | 2024-12-07 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cee8c988-b803-3496-a230-3de250b23f56 | -4.17963 | -46.37922 | 2024-12-07 04:31:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be3df51b-bb87-30fd-93bf-65cb3b6bd63b | -6.35371 | -46.08496 | 2024-12-07 04:31:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec462303-3a2e-3184-abbe-7e48ffc7d256 | -8.03028 | -47.68937 | 2024-12-07 04:31:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec52a43a-aac6-387d-a499-9a11e0bcb49e | -6.01187 | -46.40145 | 2024-12-07 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa55f40d-1076-3651-8a93-e3de15d901c8 | -4.21004 | -46.49176 | 2024-12-07 04:31:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e3c7568-e156-3928-afe6-7805a7425280 | -8.27767 | -48.03198 | 2024-12-07 04:31:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bcab2154-42a4-3788-a7d1-84383cd3c754 | -7.3624 | -47.74463 | 2024-12-07 04:31:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd66ad4d-5570-398d-84f3-a2b2e2993a26 | -7.6713 | -47.28399 | 2024-12-07 04:31:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f187e33-958d-3353-93eb-11f15f842fb5 | -6.00838 | -45.92729 | 2024-12-07 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1448fa60-e14a-3ae9-80c7-a0da8b900b05 | -7.79654 | -50.00116 | 2024-12-07 04:31:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff32e4f8-a768-3b61-9bee-7b0e3c2bb8d9 | -8.93655 | -44.24522 | 2024-12-07 04:31:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 760cf00c-20f6-3d5e-aa9e-71c20ffc2131 | -5.77225 | -46.55183 | 2024-12-07 04:31:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 55feac0e-ff59-3b5c-8a8d-df99d30561f9 | -4.32155 | -45.8903 | 2024-12-07 04:31:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9a3fa8a-f496-3877-a094-5f894f58594f | -4.04003 | -46.64465 | 2024-12-07 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f43220ba-4073-3b43-b409-8149c6b0af7d | -5.76889 | -46.55133 | 2024-12-07 04:31:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b0119829-bb26-3391-a2de-008732944bc5 | -5.35252 | -46.86289 | 2024-12-07 04:31:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc0b9e9e-2be0-3d4c-a859-ff1f323e753d | -6.84186 | -44.38596 | 2024-12-07 04:31:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 528266b0-1c67-3f46-be5b-4f70eaac9ea0 | -5.97825 | -46.07725 | 2024-12-07 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c9d2fdc-d2d2-3bc9-833e-6bd90ab8efbc | -6.45759 | -45.74891 | 2024-12-07 04:31:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 13e675c2-fef6-3bb3-a9cb-288026ba6997 | -4.17511 | -47.53074 | 2024-12-07 04:31:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 614f2d75-0ed2-3583-b145-fa299c3855de | -4.42371 | -45.65921 | 2024-12-07 04:31:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 84d57f79-adfe-383a-a6c1-b972ffc712ce | -7.97744 | -55.30617 | 2024-12-07 04:31:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c06e811-0236-3805-9113-37c246005327 | -7.17211 | -44.99491 | 2024-12-07 04:31:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 307ff0b1-f832-3a8b-abdf-fbd32548f67a | -6.92793 | -47.88272 | 2024-12-07 04:31:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51765e92-e20b-3800-af95-8c2aea011f25 | -8.28044 | -48.036 | 2024-12-07 04:31:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 855941c2-6535-3827-b5d2-44dcee79f154 | -6.4472 | -45.74733 | 2024-12-07 04:31:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78fa7724-d355-32c0-908b-421f46a3eace | -5.98166 | -46.07779 | 2024-12-07 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 51a01941-22a8-38ca-8ab2-85efaa234b96 | -8.87412 | -47.26974 | 2024-12-07 04:31:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2647987d-47f4-3752-bd2f-911c9eb077d1 | -6.41062 | -46.19121 | 2024-12-07 04:31:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31574c1f-3108-3833-b7df-db7f1985744c | -6.28915 | -43.85225 | 2024-12-07 04:31:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c49fda59-13d9-3438-8c1f-51f6cb2d0c23 | -8.9397 | -44.25054 | 2024-12-07 04:31:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 18e4d774-29cf-367c-a539-6f2e827b163f | -6.75098 | -46.51826 | 2024-12-07 04:31:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f14b75b1-4f96-3bde-8550-1f1cc9e0494f | -5.58162 | -45.20868 | 2024-12-07 04:31:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eff72c14-ee90-37f8-8957-5eccebdc89a3 | -5.53147 | -46.43479 | 2024-12-07 04:31:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d860e34a-9447-36db-bc8c-50bf38414315 | -6.00793 | -46.40459 | 2024-12-07 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86130b94-bc47-3edb-8a94-a0f394ce3c5e | -6.48553 | -44.6809 | 2024-12-07 04:31:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 12ce0fda-2d3e-309c-b667-d0f750569aa0 | -3.98432 | -46.52882 | 2024-12-07 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a47f784-f128-30ef-ab83-84135a003a2b | -9.19148 | -44.35015 | 2024-12-07 04:31:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff9496e8-c741-3f03-afd9-27fb089efd1a | -5.5101 | -45.48897 | 2024-12-07 04:31:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5deaa598-ec10-3449-8a28-9894699f33f9 | -6.45701 | -45.7527 | 2024-12-07 04:31:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 180d34cb-3652-32f8-b75b-3356c61a03cb | -7.08685 | -45.2089 | 2024-12-07 04:31:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8176190d-a7f7-309e-a196-4790997f45f6 | -6.92738 | -47.88619 | 2024-12-07 04:31:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f855a1e-a145-309c-8069-4fa943bac19c | -5.50663 | -45.48843 | 2024-12-07 04:31:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc9cd757-2e6f-3c0b-910f-046b7878b4d4 | -6.74765 | -44.18777 | 2024-12-07 04:31:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13dc8565-e4ca-3ad4-a979-3922a493feed | -5.34919 | -46.86235 | 2024-12-07 04:31:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 23ad2158-76eb-3aff-a9a9-fb7f6bbb5b7e | -6.75436 | -46.51879 | 2024-12-07 04:31:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3ced1b50-7c1a-356d-bb2e-c024d06d5fdb | -4.17456 | -47.53419 | 2024-12-07 04:31:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| def5923c-0092-3331-805e-5ccc97ce8098 | -6.84251 | -44.38155 | 2024-12-07 04:31:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ef4ef65-8196-32ef-a7eb-4052d35a2edb | -5.75262 | -44.3349 | 2024-12-07 04:31:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f143ced-ee4b-3dcf-afc8-e04f9c8aee13 | -4.43048 | -45.88419 | 2024-12-07 04:31:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e671b5c-7407-3f4e-8113-a71f12967549 | -6.45354 | -45.75217 | 2024-12-07 04:31:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e5694641-d4ff-3821-99da-ac98a6f05005 | -7.79921 | -50.00085 | 2024-12-07 04:31:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| daa6b751-0f39-37e5-834b-17356b8861f5 | -5.58102 | -45.21257 | 2024-12-07 04:31:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da0e7eab-651b-3215-8771-02bfd68124d0 | -8.2782 | -48.02857 | 2024-12-07 04:31:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 345b1630-6b5f-3c0c-83e5-122266f1059e | -8.93272 | -44.24464 | 2024-12-07 04:31:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 17d6d10d-f91a-3f79-8b41-c10fa562e659 | -4.42991 | -45.88779 | 2024-12-07 04:31:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12483497-0b90-380a-ab69-3b645bea7ab3 | -8.27488 | -48.02804 | 2024-12-07 04:31:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d38f3088-013f-3a47-a09f-f43bb3c61eb8 | -4.31872 | -45.88617 | 2024-12-07 04:31:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e37166d-0fb6-399b-a04d-76e3ef8d1371 | -3.98487 | -46.52531 | 2024-12-07 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eda79f70-383c-3fa0-9ea9-aadfd6ed6df0 | -12.28729 | -45.50008 | 2024-12-07 04:33:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9010d369-9438-3638-bca0-b867b28ae8f9 | -10.74651 | -49.51253 | 2024-12-07 04:33:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5aee272a-7811-350d-aa61-2cd3c1d06d12 | -11.73891 | -54.30961 | 2024-12-07 04:33:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 132fb24a-770e-3af3-b5a5-b8243b70d053 | -12.46359 | -46.93703 | 2024-12-07 04:33:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 330586d8-91db-34ee-8372-e1f99d0410f4 | -12.85995 | -51.94088 | 2024-12-07 04:33:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1bfba38d-1ed2-3cf3-b788-255f43cea45b | -12.91203 | -49.68388 | 2024-12-07 04:33:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58fb67b1-2325-3317-9e5b-5d34e5e599f7 | -15.26268 | -53.57102 | 2024-12-07 04:33:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1aa80d78-bbdb-3585-9877-8aed99df1c14 | -10.47331 | -48.28242 | 2024-12-07 04:33:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5cd922a0-19db-3720-8da2-beb6d38d9c4d | -12.86128 | -51.93289 | 2024-12-07 04:33:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 780c387b-8080-3a26-8f7e-8cfd8c0e9c80 | -12.92791 | -48.63174 | 2024-12-07 04:33:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8e0fc8c-2005-3ec6-9ffd-d91730dcfb2a | -13.07577 | -50.26409 | 2024-12-07 04:33:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 87ff89d0-b50d-3d2a-b602-12b090269a78 | -12.6799 | -58.23865 | 2024-12-07 04:33:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64d20fa2-6e6f-30f8-9bad-59b8d7d71bb2 | -12.68174 | -58.22913 | 2024-12-07 04:33:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64ff7a27-775c-399a-964d-de548cf0ff7a | -13.41955 | -48.88194 | 2024-12-07 04:33:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d48905d-9ea6-37d6-b436-cac1371a1727 | -16.32393 | -49.52805 | 2024-12-07 04:33:00 | NPP-375D | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d5f1c20a-82e6-3c8b-aea7-c21ca1421c47 | -12.67536 | -58.2343 | 2024-12-07 04:33:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 004094b6-b8c6-3200-80bf-875238026674 | -12.65731 | -46.57393 | 2024-12-07 04:33:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ddf2359-0067-37b3-9a25-334961898f70 | -9.90975 | -48.58129 | 2024-12-07 04:33:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README8.md)
