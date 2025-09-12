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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc2aea35-3667-3876-8fc4-dcf945de6b46 | -8.9563 | -46.0849 | 2025-09-12 11:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 4078a080-690c-3aae-bf7e-fb63f025e700 | -6.1935 | -42.5022 | 2025-09-12 11:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 85.4 |
| 616780d1-9787-3e6a-a6c6-8a058f8fc846 | -11.9713 | -51.164 | 2025-09-12 11:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 94781f3f-dced-387a-9fa5-adb75de5cc60 | -10.8785 | -45.5597 | 2025-09-12 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 26a75aae-e436-37d3-9f88-671594ff5b43 | -9.057 | -47.0355 | 2025-09-12 11:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| fa463016-fd78-3775-a8d0-c26e4bdaa7b8 | -8.8901 | -49.9236 | 2025-09-12 11:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| bad3dbb8-b911-3fc7-8dcd-d457f76e19ef | -9.72 | -46.8749 | 2025-09-12 11:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| f92937cd-56ed-30dd-9930-e4148a129f14 | -9.7197 | -46.8972 | 2025-09-12 11:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 1ba898ac-eab3-3bb3-8879-a517bb1121e9 | -11.809 | -50.5642 | 2025-09-12 11:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 19c4703d-f0ce-316a-b097-7e20d3efd18b | -6.8184 | -45.6349 | 2025-09-12 11:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 18be33c3-0875-3e16-b9e8-ac8c95d03e18 | -10.9089 | -47.247 | 2025-09-12 11:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 43077dc1-568b-3286-98d7-76b323d32181 | -11.9713 | -51.164 | 2025-09-12 11:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| d7d93d7b-6ddd-363f-aba7-fa30dd2f8cad | -11.79 | -50.5664 | 2025-09-12 11:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 85802749-81b8-3e84-a594-45aaef2aad72 | -9.057 | -47.0355 | 2025-09-12 11:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 4c64ad48-31cc-3184-910b-fa5498e4fe2a | -14.1907 | -46.2012 | 2025-09-12 11:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 37acd7d8-b1c0-32dd-a925-6b566d2a7d4a | -10.8785 | -45.5597 | 2025-09-12 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| bf637c26-2724-3121-b7fb-7fd4a5705696 | -10.6979 | -48.6612 | 2025-09-12 11:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 0ea11617-d464-3aae-ac7f-d4b1187a1f5d | -10.679 | -48.6633 | 2025-09-12 11:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 4bd990f6-0eb3-340f-ba8f-fc0b316ad218 | -11.9211 | -50.7009 | 2025-09-12 12:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 24052bcb-1bb5-314d-9443-2e87188ff43e | -10.9089 | -47.247 | 2025-09-12 12:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| f36e9dc8-42c8-3af4-94bb-323827e172f2 | -14.1907 | -46.2012 | 2025-09-12 12:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 8e82c93f-3b2c-30a1-85b3-13e544d39062 | -16.2484 | -46.7716 | 2025-09-12 12:00:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 496914fd-6d0a-3c10-836a-42d521d3c491 | -11.9713 | -51.164 | 2025-09-12 12:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 108.0 |
| d8bbbf7a-f3bc-3233-9012-4622071e9bc3 | -9.0376 | -47.0819 | 2025-09-12 12:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| f24d476f-b6bf-373e-a664-1a8330aa1ebb | -9.057 | -47.0355 | 2025-09-12 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 1448f1d0-56aa-35d3-a5c3-b47e4c4bc3eb | -11.4398 | -48.5733 | 2025-09-12 12:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| e8bb8b95-a640-360c-84ae-05a90b34a75c | -8.9563 | -46.0849 | 2025-09-12 12:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 4ac7c22a-c5cd-30db-b56a-c85243c7ef09 | -9.7197 | -46.8972 | 2025-09-12 12:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 6d5a652f-8c57-33cf-b199-9834f8e8bd52 | -10.8785 | -45.5597 | 2025-09-12 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 05c6556e-8dac-3dda-81c0-80eeec1a29f8 | -10.679 | -48.6633 | 2025-09-12 12:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 57d8d845-6142-328c-90be-1da2d9f9dd1e | -16.633 | -49.7905 | 2025-09-12 12:00:00 | GOES-19 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 0f576e1e-ff24-3cfa-b236-1cf70d891b29 | -6.1703 | -41.0901 | 2025-09-12 12:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 157.0 |
| e898db75-f176-3dd1-9f12-0e22cac3d5b3 | -11.9523 | -51.1661 | 2025-09-12 12:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 25fcce1e-4cb5-30b8-80c0-eab1d02f63c4 | -6.1703 | -41.0901 | 2025-09-12 12:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 262.3 |
| 5a19ed11-4956-382c-8832-a6fc6abdb339 | -8.1837 | -46.0965 | 2025-09-12 12:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 49f68942-47c2-32dc-bd82-bfcb84fcbed0 | -9.6727 | -47.568 | 2025-09-12 12:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 22d50134-75f3-32a2-af1a-41201ad56ac6 | -9.6919 | -47.5438 | 2025-09-12 12:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 8083bbd4-09f1-3c37-aeac-8d51ee8a77e4 | -9.0376 | -47.0819 | 2025-09-12 12:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 5aa910ab-a357-38b1-9fe1-e3758277544e | -10.8785 | -45.5597 | 2025-09-12 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 6be39567-d5c3-3321-9bb5-e2dc5302d3b2 | -14.1907 | -46.2012 | 2025-09-12 12:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 5ce561fc-4741-35cd-bf9d-5a1791a187bb | -7.5643 | -44.3838 | 2025-09-12 12:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 1d8c3056-52b0-330f-983f-46d739beece2 | -9.673 | -47.5459 | 2025-09-12 12:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 46c8cb0c-c76f-37e8-a46a-1ff0827aa151 | -9.0379 | -47.0597 | 2025-09-12 12:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 38862c22-97be-333b-873e-7062763d7915 | -7.5641 | -44.4068 | 2025-09-12 12:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.3 |
| c2cb1294-608a-3dae-999d-806d28463ae9 | -9.057 | -47.0355 | 2025-09-12 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| a468b705-5bf7-306e-b7e0-f8e6b843248c | -6.8182 | -45.6574 | 2025-09-12 12:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 1f3bcbb7-e57f-3ef1-9d7b-20264813a5b8 | -11.4398 | -48.5733 | 2025-09-12 12:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 165.3 |
| 12120e4c-52f2-3c85-96e5-4f6db073b1b0 | -11.4402 | -48.5513 | 2025-09-12 12:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 70c49794-19aa-3aef-ab92-b5c8aa70d251 | -10.679 | -48.6633 | 2025-09-12 12:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| a8a3607e-56b6-38ef-b685-0b88650ecf94 | -9.7412 | -48.0887 | 2025-09-12 12:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| c55e73dd-251e-3945-9ed3-f271c4ce95bf | -10.8781 | -45.5826 | 2025-09-12 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 329.9 |
| 0208d07e-faa9-3534-8844-3f98927c021a | -11.9904 | -51.1618 | 2025-09-12 12:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| ae577864-1175-3a96-9cde-580efbc99b24 | -14.1907 | -46.2012 | 2025-09-12 12:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 22ffc146-7e35-355e-8bc5-3e49e8c3a3e9 | -7.5643 | -44.3838 | 2025-09-12 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.7 |
| ab3f650b-f110-3a01-b348-a1b6cd3d2f37 | -8.4705 | -47.2712 | 2025-09-12 12:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| fb6708f0-8e9e-3b42-bece-450a586587ce | -6.1703 | -41.0901 | 2025-09-12 12:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 218.0 |
| 30d84cda-4e47-3aed-ad61-e53802c4d3fa | -8.1837 | -46.0965 | 2025-09-12 12:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 46b8a2f5-6ab5-3174-b7a0-27355c05531e | -9.057 | -47.0355 | 2025-09-12 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 9b2188ef-0498-3a27-bb85-4d79ee2b550e | -11.4398 | -48.5733 | 2025-09-12 12:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 220.0 |
| 342e3317-bb8e-3bd8-8ab1-4bdb352ca2b4 | -16.3127 | -50.0868 | 2025-09-12 12:20:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 38ca463e-4705-36aa-8316-55cead0d0b58 | -10.679 | -48.6633 | 2025-09-12 12:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| fc17df43-52cd-3012-9067-aa864216de12 | -11.9523 | -51.1661 | 2025-09-12 12:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 63b848ce-5949-3410-b208-3960350c7ef5 | -16.2738 | -50.0712 | 2025-09-12 12:20:00 | GOES-19 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 78.3 |
| c0c936d7-6d8c-3095-bb68-a1dc92893024 | -10.8972 | -45.58 | 2025-09-12 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 199.2 |
| be9eabc1-928b-3a31-814f-69c35136926f | -15.2276 | -49.6672 | 2025-09-12 12:20:00 | GOES-19 | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 9f2bf240-e310-30a0-9184-93b0cda9ffa7 | -14.5132 | -53.8949 | 2025-09-12 12:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 106.8 |
| a6d905c6-b84c-3f0d-9507-5bf9e2440cc1 | -21.1574 | -54.9638 | 2025-09-12 12:20:00 | GOES-19 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 8fe2d1fa-8dfb-3723-b322-f1326d61d79c | -10.859 | -45.5851 | 2025-09-12 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| e589daba-9548-38a9-8e2e-aa43d33ee72d | -12.0849 | -47.6065 | 2025-09-12 12:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 5c4c89d2-52ea-3876-8284-e5591bacca4d | -11.9713 | -51.164 | 2025-09-12 12:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 74e7a0c4-2ef1-31b9-8b42-5ac6a4412383 | -11.4402 | -48.5513 | 2025-09-12 12:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| d6a75aeb-d6f8-3331-90e4-2ce83bee4ed0 | -10.8785 | -45.5597 | 2025-09-12 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 318.3 |
| a8c70348-708e-3fe0-8676-7f865967de0b | -10.8594 | -45.5622 | 2025-09-12 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |
| d24ea089-89c9-3b77-b46a-11da403f37cc | -9.0376 | -47.0819 | 2025-09-12 12:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| c73f9fa9-eb33-30e0-a8d1-e6330250c545 | -8.4893 | -47.2694 | 2025-09-12 12:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 45ce5fa9-7ef4-3b4b-a337-b0d255bc4cc5 | -12.9292 | -54.7538 | 2025-09-12 12:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 85833d0d-ca87-31b1-81eb-9a753cb429c8 | -11.9713 | -51.164 | 2025-09-12 12:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 6ee65b90-8852-3f74-a5af-cab3226a596e | -9.0376 | -47.0819 | 2025-09-12 12:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 28c2dd17-5ad5-3cc6-9d43-be9e549638d6 | -10.8972 | -45.58 | 2025-09-12 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 49ffe5f9-1d0a-3111-87b2-91d3d8f18500 | -7.4511 | -44.4177 | 2025-09-12 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 53e88379-faad-32db-b4d0-448c2daf3dbb | -15.1402 | -50.1628 | 2025-09-12 12:30:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 308bb053-b3e9-3a3f-b92e-c78b7a7e56fd | -7.5643 | -44.3838 | 2025-09-12 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 7433bdf7-03fa-3b8e-a3c7-5e76b2c53f6c | -14.1907 | -46.2012 | 2025-09-12 12:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 102.0 |
| dc53d4a3-83ce-3479-b79e-8df658a54ef1 | -11.4285 | -43.5544 | 2025-09-12 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| f91ba9d0-07cb-355b-b6d7-10136334ae30 | -12.9101 | -54.7558 | 2025-09-12 12:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| ff87ab72-0450-3582-b6ed-33d6fc6daf6c | -9.057 | -47.0355 | 2025-09-12 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 72682b3e-82f0-31a1-844b-51b4359a81b3 | -12.0852 | -47.5842 | 2025-09-12 12:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| d2fafcb1-f736-3ce3-8b31-89123dfab2bc | -10.8781 | -45.5826 | 2025-09-12 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 257.3 |
| de7d22a6-0adb-3cd8-af8c-240f12e28bea | -11.4398 | -48.5733 | 2025-09-12 12:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 281.3 |
| 896c0a2b-d215-3f19-a0bd-c409a3b45f54 | -6.1891 | -41.0884 | 2025-09-12 12:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 99.6 |
| a3f236dc-2559-3bea-8c7e-dd8ba3ed68f4 | -8.9563 | -46.0849 | 2025-09-12 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 112.4 |
| a766868f-ee7f-3e57-82fe-2e730f7a9ba4 | -9.6301 | -47.9249 | 2025-09-12 12:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 1aaf8b86-f9ba-36ea-ba8e-50558d9bf74a | -8.956 | -46.1074 | 2025-09-12 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| c715cb2d-c076-3d78-822e-c8b477b900fb | -14.4588 | -47.3174 | 2025-09-12 12:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 863b636d-d1ea-3d3f-bb78-18246892836f | -15.2276 | -49.6672 | 2025-09-12 12:30:00 | GOES-19 | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 6fc54cb7-693d-3c95-8bc1-b6824aedf504 | -10.8785 | -45.5597 | 2025-09-12 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 283.6 |
| 11ac8d98-fc0c-3f13-b160-faaaca691a1a | -8.1837 | -46.0965 | 2025-09-12 12:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 6ff4a928-acf2-35ef-90a0-42706f5a7365 | -14.1717 | -46.1815 | 2025-09-12 12:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 1c8f832c-07fe-387c-a400-a841eb06a0ac | -10.679 | -48.6633 | 2025-09-12 12:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 4ae20609-2bea-36dd-b426-5de7ef0a1afa | -12.0849 | -47.6065 | 2025-09-12 12:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 136.1 |


[Clique aqui para ver as próximas entradas](README122.md)
