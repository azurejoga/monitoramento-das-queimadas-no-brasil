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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66a22bde-8f05-3ae1-8197-9c3a3a75e225 | -6.31604 | -43.44211 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 75f183dc-7418-3565-9b63-034a625d2fcc | -6.64512 | -42.96527 | 2025-09-11 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1882380-abce-3a22-a7ef-acd5b35edbd0 | -3.24464 | -50.803 | 2025-09-11 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 54001dec-a56c-3d3c-b8aa-49c6df79b54d | -6.44079 | -43.65402 | 2025-09-11 04:21:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8ba52b9-bd65-3e19-8f7e-9c3fa27226a3 | -8.16697 | -46.06739 | 2025-09-11 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7d72a358-a9b5-365e-acef-4d57808ea559 | -7.84308 | -45.40166 | 2025-09-11 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1a64641d-4ba5-3a8d-988e-1f84e553c858 | -6.80601 | -52.80381 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52d26fc1-9983-3bfd-b372-fff93333f51f | -6.73709 | -43.98919 | 2025-09-11 04:21:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a7276fca-cf80-3c55-8c3a-47269b48243f | -7.03506 | -42.1316 | 2025-09-11 04:21:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e13308d4-0d00-3129-850a-555e93dbe4b8 | -8.09966 | -49.2505 | 2025-09-11 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e345262-892c-3f70-955f-779a9c2efbf3 | -6.85401 | -47.86776 | 2025-09-11 04:21:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9ff6549-7793-3db9-926f-56f46936a7dc | -8.65503 | -45.72197 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01d2306c-d313-3f6f-8e66-a7fcaa87e1f7 | -6.83766 | -45.597 | 2025-09-11 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ce608ce-8562-35e1-a9e3-80844522b0e2 | -8.52766 | -45.69011 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5bb04fc-d2f8-3ff4-adb7-c6dcd456cc98 | -7.53633 | -48.23521 | 2025-09-11 04:21:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e68d98f3-3990-3466-a0f5-3141dd986a2d | -5.66554 | -43.33585 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8fbe909d-1c14-3c1c-a014-78595399c4b8 | -8.6478 | -45.72441 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c48d4149-043a-3912-ba5c-5a6af619d017 | -8.01595 | -48.64914 | 2025-09-11 04:21:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7d9235f1-f1b4-3677-8271-523cb3d5dafa | -6.36311 | -44.49816 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f7959fa-e605-3b5d-8ecf-a80f5037202b | -8.02324 | -49.04207 | 2025-09-11 04:21:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d447bf94-42db-3631-b327-401de0390387 | -5.76779 | -45.52088 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5dd5ae29-8e87-3693-8564-7f663adfb990 | -5.72627 | -43.89309 | 2025-09-11 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 528835a9-da8f-358a-a6e9-6ea9f666b5fd | -4.77295 | -45.32414 | 2025-09-11 04:21:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d04ded0b-2a74-37d7-968b-cbcaf33df702 | -8.73412 | -47.10012 | 2025-09-11 04:21:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 749bd7d7-64ec-3295-a9b1-500677f33af7 | -7.2053 | -44.81114 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 538c1b57-aa69-3eff-8da2-48f585705059 | -7.3829 | -50.88811 | 2025-09-11 04:21:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2c120940-5096-32da-a821-ef4fe1d24632 | -8.02383 | -49.04371 | 2025-09-11 04:21:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 40f49131-1ba7-3775-bd9d-469fdc2f04d1 | -5.22991 | -46.08952 | 2025-09-11 04:21:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f945a8da-01fc-30fe-8408-9e5f91e629e9 | -2.4396 | -47.33059 | 2025-09-11 04:21:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b9c47c21-e409-3fcd-8c16-e037c5f973fb | -7.71448 | -44.80226 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ec71664-55ce-3db5-ba22-a3f22f945d9a | -6.40069 | -43.50616 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 04ff62e3-3b28-333c-9b24-3203886a38f2 | -5.52994 | -44.35043 | 2025-09-11 04:21:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4f370755-8a86-3055-a2f8-870b56111508 | -7.18221 | -44.95722 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2f4a172-c0d1-395f-bffd-f1b19396c623 | -8.07296 | -50.17955 | 2025-09-11 04:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a8e2b851-6e72-3924-806a-0732dc4dfd1c | -6.36257 | -44.50163 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32b33ef5-8695-33dd-9bbe-4ab895567fe3 | -7.23725 | -55.06334 | 2025-09-11 04:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7eceb26c-7b13-3a36-ae68-01813d62cf57 | -5.45384 | -43.99667 | 2025-09-11 04:21:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5a446888-4b22-3b1d-aa0a-50288890ba0d | -7.87155 | -46.72976 | 2025-09-11 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5163a38d-ff94-35fa-bd1e-914968be538f | -6.19979 | -43.53767 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc2258f7-67e3-33b6-bdcf-6d45d6763e76 | -7.20327 | -44.95343 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| dfa6f584-b9be-3ced-821d-429b438f43a6 | -6.0196 | -45.89623 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe5ce29f-1d72-395a-bf1c-c860207f40aa | -6.44436 | -44.77122 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d127ef62-904d-3606-855f-e68a394055de | -4.92978 | -55.78498 | 2025-09-11 04:21:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fa74c7a5-f594-3d55-91d9-fa4eaf35a7ff | -6.82278 | -52.79688 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 80dc2366-4dcc-3577-b4d9-a9e681cfad67 | -7.993 | -45.79957 | 2025-09-11 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd1e12e0-89eb-34b8-a022-0c83a59f39c4 | -7.41922 | -45.87127 | 2025-09-11 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 94bb60e5-0a0d-3ce4-8e07-632692c991c5 | -5.65815 | -43.90047 | 2025-09-11 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ad82634-3ba6-3e65-8383-6a32865766e1 | -6.09144 | -44.78274 | 2025-09-11 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d582e55-9327-33fa-a9c5-9209d7cb518b | -6.61011 | -43.9552 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5eccdabd-3d19-3765-b16a-060f788c9beb | -8.02185 | -48.65946 | 2025-09-11 04:21:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6bbed6b9-8565-3755-a298-0cf4112ef1ac | -6.61345 | -43.95571 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 697ed005-571c-3c8c-b57b-177eb6ce97cd | -5.73171 | -43.09605 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 9694cfcf-da3c-3fc1-91e6-6b194ca84580 | -6.66557 | -44.0966 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d2acad2-7f91-32c2-8c11-8793a96789f6 | -5.62469 | -43.10947 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c7217673-8625-357f-becf-0c8a1411794d | -6.39003 | -43.50816 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76ea5eea-e996-3011-85f4-6e190bcd3d01 | -6.44381 | -44.77469 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df2f0e35-3ea4-3b4c-871a-741b4cdc5729 | -5.5439 | -45.70406 | 2025-09-11 04:21:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73874269-e64b-3b52-b662-42e0a604a1ae | -5.69852 | -45.31818 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e98f2149-3605-3ffb-a604-72336244c370 | -8.96719 | -46.07235 | 2025-09-11 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ada18a50-b88e-38b2-9fef-aa2caa4a1035 | -8.01927 | -49.04772 | 2025-09-11 04:21:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dceeb0cf-092a-3c0b-8506-2aec39a541a5 | -7.87571 | -46.01682 | 2025-09-11 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7d81966-3aa6-3cbd-b1b7-aea90cacb8b4 | -8.5071 | -45.69041 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d08052ed-075e-3ea7-9eea-6cd8035e4943 | -8.16299 | -46.09226 | 2025-09-11 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9b1e47b3-6028-3c65-ab03-8cb278664f2d | -6.53953 | -43.10659 | 2025-09-11 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f56a966e-9f7c-3c9a-a312-474f798af70c | -6.99383 | -44.78069 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b8e45e96-7718-361f-93d7-28f871ffe045 | -6.9141 | -44.55453 | 2025-09-11 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9b341014-7139-30ca-b01b-b9617819d5e2 | -7.03152 | -42.13105 | 2025-09-11 04:21:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7d7dd61f-8f15-3cb0-b337-8b7f2fbef693 | -8.43995 | -47.27042 | 2025-09-11 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1817df3-b9ac-33de-9cf3-2a4cb4fa3fea | -6.64598 | -44.0756 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5fc0de9a-7553-379e-8c13-c919f122cfc9 | -8.64503 | -45.72036 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ac916730-4ea8-37b2-9673-5b0564628e18 | -7.86906 | -47.98241 | 2025-09-11 04:21:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c070c28-0287-3e6c-91ea-c0b39b63845b | -9.50085 | -43.16851 | 2025-09-11 04:21:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2575a30c-ebf7-38f7-ac04-9b86114f6bee | -5.95294 | -45.69871 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f137531a-46b5-30fb-819a-955a41cf065c | -5.74842 | -51.6965 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 491668e0-163d-3b26-9ccf-d96a5634ca07 | -5.43709 | -43.41287 | 2025-09-11 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f9edf7b5-2614-3fb3-a1c8-0db2acaaa324 | -8.73229 | -47.11138 | 2025-09-11 04:21:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ad27584-e026-3bba-b968-28c9dc03d62e | -7.04412 | -44.69957 | 2025-09-11 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 53c10021-de2d-38b1-b241-3d30e31ef33b | -6.49638 | -42.40857 | 2025-09-11 04:21:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2655472b-7dea-3ab4-a47a-15d79df56d5e | -6.2897 | -42.19827 | 2025-09-11 04:21:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2997b29a-7e2b-31ee-b208-ca8bba4d8663 | -5.76387 | -45.5239 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5041d66-ba12-33a1-9feb-06b7d2e723cf | -6.8547 | -47.86357 | 2025-09-11 04:21:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ece9bcf1-061f-3ddf-8bc6-d63d39b47ebd | -6.16754 | -53.50494 | 2025-09-11 04:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f597fb59-3644-3d49-83b2-91d5a500d1ec | -5.79287 | -44.84648 | 2025-09-11 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 355351ff-9385-36b0-95ea-78967b5710e8 | -5.73084 | -49.22012 | 2025-09-11 04:21:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 571c5347-a029-3ebd-9837-0129083d115b | -6.83822 | -45.59346 | 2025-09-11 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4339174d-0717-3fec-875b-1b2114401404 | -6.44203 | -44.77095 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5e94cc85-af99-384b-a2de-b414e9817ead | -7.18609 | -44.95427 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26c28d25-c7fa-32e2-8769-516a02b65c60 | -6.38457 | -44.42686 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f78ffb1c-44d4-30cb-af0a-baef3ed38cd1 | -9.03907 | -45.79444 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 77caa153-bc45-353c-952f-5c3dde66b0c1 | -5.48428 | -45.61438 | 2025-09-11 04:21:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2f3f59a2-5a53-3c48-b848-125541a420f3 | -7.54137 | -44.67152 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6ee157e-c7d6-31e2-a40b-f82b51d1f319 | -8.96913 | -44.93305 | 2025-09-11 04:21:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2adcc14-7b9a-332c-9514-294c7225d824 | -5.51492 | -42.69046 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 42ed193c-fa51-30dc-a834-17e0dc8fec83 | -6.33245 | -42.59904 | 2025-09-11 04:21:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 426a2bf9-2323-3bff-a369-25b9d2c5c54c | -9.16295 | -45.58753 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fbb01c73-771a-3c4e-8317-d70b4b876241 | -5.74375 | -51.69564 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e87f2b47-476c-3ac4-9339-bc69dfcaab2e | -5.17434 | -42.84128 | 2025-09-11 04:21:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b96661f-b6eb-376a-819c-c31fa94e6eab | -4.55698 | -43.73905 | 2025-09-11 04:21:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9211520b-342d-39f3-b1a8-559bd3c7a081 | -7.73096 | -50.73396 | 2025-09-11 04:21:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c426936-ba68-384f-98b1-68db0476c963 | -7.48232 | -47.05679 | 2025-09-11 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README48.md)
