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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75a5de76-9dfa-3901-965e-d1a6fd80b07c | -8.6817 | -45.4359 | 2026-09-18 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 81ff3fdf-2752-3cd3-8f27-b99c3549382f | -11.3442 | -43.9906 | 2026-09-18 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 176.5 |
| a6b1916d-2c67-3cd8-a323-151742be552e | -11.8937 | -47.6099 | 2026-09-18 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 3b3fd5ab-8c14-3c8e-9383-6c38f2056a14 | -7.8216 | -44.909 | 2026-09-18 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 602610ec-9b43-3345-b223-3b19cf0847f0 | -7.6574 | -46.1013 | 2026-09-18 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 120.0 |
| f6506535-1fba-3243-b1a9-88e20d78aa9a | -6.4667 | -45.2116 | 2026-09-18 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 68dd28d7-4a93-3a4c-abec-60796bbbf945 | -7.6762 | -46.0995 | 2026-09-18 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 9f0eb99f-dd39-3317-bbf3-f918000487ae | -10.5472 | -44.8466 | 2026-09-18 13:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 75.9 |
| d84d2cc3-3eb7-3fab-99b1-106e83573f9e | -11.3437 | -44.0141 | 2026-09-18 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 279.0 |
| 87b5dc84-0cbc-3324-b287-a5a2fb8b61ee | -9.9502 | -45.3589 | 2026-09-18 13:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 129f9e89-b7dc-382c-8d87-68a235b8dc54 | -13.4303 | -51.9036 | 2026-09-18 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 235.6 |
| aa6dd323-e1ef-3d65-a3d4-d5dfad96ab4e | -6.0196 | -51.7893 | 2026-09-18 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| d2496559-fd39-3480-bcb9-ae0f2ad62ef7 | -12.5149 | -47.0991 | 2026-09-18 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 3a527237-3225-3830-a3e1-4639f66f8441 | -12.0461 | -49.9992 | 2026-09-18 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| a2334469-a64b-3378-841d-55bbeca5cefa | -4.5587 | -42.9523 | 2026-09-18 13:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| e05e2d1b-2ea3-3e1b-a887-6d6467458b1d | -10.6758 | -50.2406 | 2026-09-18 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 3b4fa784-483c-388a-8711-515e3546b6e4 | -10.3307 | -45.3112 | 2026-09-18 13:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 185.2 |
| 7c859fac-3b17-3c5f-9c73-b2cf30ed4845 | -7.8033 | -44.8651 | 2026-09-18 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.6 |
| f1871468-09a7-3f32-afe4-e3acac8c0c36 | -10.6944 | -50.26 | 2026-09-18 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| dda552bc-54fa-3f4d-9aea-ae7ac403f198 | -12.5504 | -50.6902 | 2026-09-18 13:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 5c524319-f4c9-319b-843c-f7af3b037e60 | -11.064 | -48.2898 | 2026-09-18 13:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| ffb929f5-069c-38d0-8ac9-1564e0b6d379 | -7.8036 | -44.8422 | 2026-09-18 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 174.3 |
| 0d710e65-8db0-3059-a947-07ace9f3aa61 | -12.5688 | -50.7308 | 2026-09-18 13:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 164.9 |
| 8fe3804d-ffdd-3af2-a230-65f3c7dc443a | -4.9183 | -47.4295 | 2026-09-18 13:50:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 75.2 |
| ae29a139-15f3-3f06-b81f-5673558bc87c | -11.3617 | -44.0817 | 2026-09-18 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| b2b874c4-1b8d-3a73-8b95-f40cc705c468 | -12.5879 | -50.7285 | 2026-09-18 13:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 53285f1b-db99-30b0-999a-2da963a87b23 | -10.6189 | -50.2466 | 2026-09-18 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| fb21b00a-68a2-3fb6-9112-8b7602b7c86d | -12.3954 | -48.4727 | 2026-09-18 13:50:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 0c74c847-3500-30f4-8f0d-5edb030413c1 | -11.8556 | -50.0006 | 2026-09-18 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 8134e9bc-71ad-38d3-ae06-0b586e306f0d | -10.6726 | -50.4758 | 2026-09-18 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 209.9 |
| d6083468-cf92-33ce-9cc8-d966bd6b0af1 | -10.6723 | -50.4972 | 2026-09-18 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 157.7 |
| 49018d5f-0b63-387c-92b2-b9653eac4104 | -12.0672 | -47.5198 | 2026-09-18 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| ad90bfe5-79e6-3367-94b6-0e695b59dc6a | -12.6235 | -50.8953 | 2026-09-18 13:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 63415345-ce0b-3ef1-8a0e-5c9dc76da9ce | -14.8026 | -48.5622 | 2026-09-18 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 25224f73-8eda-39e7-9006-58527026e55b | -10.6536 | -50.4778 | 2026-09-18 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 9a9150ea-d14b-38d7-a924-7217f1a77574 | -12.55 | -50.7117 | 2026-09-18 13:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 144.0 |
| d141d213-412e-3104-adaa-2530075c41e4 | -7.1198 | -42.1309 | 2026-09-18 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 83.7 |
| f23de2b6-2bf7-3348-9a3a-03f9c06d366e | -12.0267 | -50.0231 | 2026-09-18 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| fd1ea432-5982-329b-9d77-f8524280b81d | -14.1737 | -45.1641 | 2026-09-18 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 156.7 |
| 6827fadd-5230-32d5-a2a0-1499cf554d47 | -13.6531 | -45.97 | 2026-09-18 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 0b2df139-6fe0-3093-90d7-05332ccd772a | -11.3838 | -47.2982 | 2026-09-18 13:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 25bb5d07-a085-3d93-9b95-bc5975eb9cb3 | -8.6646 | -45.3013 | 2026-09-18 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 1767ee9d-d394-3dbe-bf6e-27ad79cf45a7 | -19.5539 | -47.6346 | 2026-09-18 13:50:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 4876348c-3131-3168-969f-5fd18cfe32c5 | -9.9505 | -45.336 | 2026-09-18 13:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 47187701-670c-3626-b576-f13b50d09ff6 | -4.5961 | -42.95 | 2026-09-18 13:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 368.2 |
| f6a1571f-972f-32f7-b403-c6c1b887cb03 | -8.4503 | -45.8448 | 2026-09-18 13:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 0b646e12-cd7f-3386-b55b-740767650540 | -8.58 | -44.5552 | 2026-09-18 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 54406bbf-bed5-3007-b0b7-b2f8fe964e71 | -12.0458 | -50.0208 | 2026-09-18 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| fe3610ba-d19e-37b4-b33b-0d9938aa7946 | -14.1732 | -45.1875 | 2026-09-18 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 129.2 |
| ea49cfe2-5520-363b-bd57-55fcd3b5d7f8 | -7.6577 | -46.0788 | 2026-09-18 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 4ef00770-fe5a-3f5b-97ca-450546df600b | -6.3123 | -45.6977 | 2026-09-18 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 6873d62b-3fc9-31fb-a38d-b462bdbc4294 | -11.6423 | -51.5819 | 2026-09-18 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 98.7 |
| de5440ef-dcc4-313d-992c-855768ea7cef | -11.8115 | -46.8158 | 2026-09-18 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 160.3 |
| 3a887707-5efb-34c7-a3b0-c723b1859482 | -6.0194 | -51.81 | 2026-09-18 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 8da2f58d-8718-3a3f-831a-9a72c1b3ed82 | -2.6966 | -57.6084 | 2026-09-18 13:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 3af28633-5b65-304f-9328-4f0c2e9ddb50 | -10.3116 | -45.3136 | 2026-09-18 13:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 7834048d-ae19-3467-a5c6-33ce62cbe6b3 | -7.2257 | -46.1171 | 2026-09-18 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| d4b59cfc-b345-3c2e-877c-ee1feae077ab | -10.5178 | -46.7366 | 2026-09-18 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 168ff20f-6e03-32d1-8337-c7fc1a71648e | -13.6341 | -46.9304 | 2026-09-18 13:50:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 9872ba69-1bf6-3f20-88be-47763f8176ff | -10.6726 | -50.4758 | 2026-09-18 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 172.9 |
| 130ac362-2dec-3bca-a5f1-5f9cd6987603 | -9.9768 | -50.2694 | 2026-09-18 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 52c04d98-209c-3bb8-ac00-d2ebebd87237 | -11.8556 | -50.0006 | 2026-09-18 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 284.7 |
| 8e65b34f-a650-3d11-9d8d-9e27191ec2d8 | -10.6533 | -50.4991 | 2026-09-18 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| a3e81c48-475e-3f92-8fed-0b33744108ed | -13.2485 | -46.9226 | 2026-09-18 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 212efebf-8aa7-3df0-988f-64402d59f05b | -14.1737 | -45.1641 | 2026-09-18 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 170.9 |
| b8ffcc0b-d146-3fd5-8139-c5e130b8554f | -14.1732 | -45.1875 | 2026-09-18 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| cc5c8ccc-73c9-3bee-aad0-9ea64b04c8f5 | -11.064 | -48.2898 | 2026-09-18 14:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 251ce035-4be4-390a-987c-85043fd31725 | -2.4815 | -49.3996 | 2026-09-18 14:00:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 3d02dd90-62d1-3255-9ac0-9b9649b8059b | -12.55 | -50.7117 | 2026-09-18 14:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 136.4 |
| f0f34c5a-bfa4-3775-b3df-bbb6f2aad70b | -11.3442 | -43.9906 | 2026-09-18 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 151.2 |
| 40d18b3d-1cee-35a0-b574-1bba8ceea845 | -11.3621 | -44.0582 | 2026-09-18 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 172.3 |
| 7c404c9c-d4a2-37dd-8a07-41120bc119e4 | -7.375 | -44.4938 | 2026-09-18 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 40b0a060-1f03-3730-853f-46e3bcc58d01 | -7.6577 | -46.0788 | 2026-09-18 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 0b493e08-af37-335c-a3d3-26b67264c419 | -8.6817 | -45.4359 | 2026-09-18 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 8757f245-eb9d-33e8-8810-d4c550046ff3 | -10.5178 | -46.7366 | 2026-09-18 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 9749aaac-b33e-3977-8050-70bc3839dea0 | -2.6966 | -57.6084 | 2026-09-18 14:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 68063bb9-4271-310f-84ef-a4de0baf1db9 | -12.1719 | -46.9906 | 2026-09-18 14:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 8c62523e-9e77-38f2-91ad-5d1a4ea8a535 | -10.3303 | -45.3341 | 2026-09-18 14:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 1365672a-5e09-349d-a260-0a639de8f464 | -12.5688 | -50.7308 | 2026-09-18 14:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 151.9 |
| ac80b088-749a-3e7c-85b8-85d631562fda | -10.6723 | -50.4972 | 2026-09-18 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 019e6247-49f1-3f13-8769-a11efd940963 | -8.4503 | -45.8448 | 2026-09-18 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 0a4eaead-eb94-3cb9-a004-39a9cbf1c8e1 | -9.8313 | -48.4073 | 2026-09-18 14:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 8cc90c7c-ecc9-3bb2-a39b-326690b87a2a | -12.0267 | -50.0231 | 2026-09-18 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 0241ed90-1ce7-30c5-bd22-309c8433e430 | -11.2971 | -43.4088 | 2026-09-18 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 205.2 |
| 043f716d-66c9-3564-b2c0-d7e0c86e6a68 | -13.4303 | -51.9036 | 2026-09-18 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 160.6 |
| cae1a1e3-bfa0-3f98-a5ac-bbdbcf645d75 | -12.5879 | -50.7285 | 2026-09-18 14:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 145.5 |
| efc9fa54-1aa3-3c77-855a-2228e9d686b3 | -7.6574 | -46.1013 | 2026-09-18 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 86d8c834-a6f3-37e9-ac59-f953e0a88184 | -10.5963 | -46.5699 | 2026-09-18 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 19fe3678-4a63-3a74-9cbe-12c86dbc2726 | -10.5472 | -44.8466 | 2026-09-18 14:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 9842a80e-7917-3518-8221-c244bf9a812c | -11.8937 | -47.6099 | 2026-09-18 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 122.6 |
| c6eb97cd-c5f6-3df6-9c17-58746a68c66c | -11.2787 | -43.3643 | 2026-09-18 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 189.7 |
| ef484671-3c3b-3281-9bd1-42af734520fb | -11.3617 | -44.0817 | 2026-09-18 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 299.6 |
| d958b177-8ce8-3617-bfd4-59f07e684a7f | -9.2417 | -45.9185 | 2026-09-18 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 2c107fad-aece-3d3a-8264-9b9345c212a7 | -12.998 | -46.9381 | 2026-09-18 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 3721e807-169c-3bd2-9285-a42f6c91a3fc | -2.8101 | -50.4658 | 2026-09-18 14:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 6f5f0807-d40e-3075-843b-759af426ad94 | -10.3307 | -45.3112 | 2026-09-18 14:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 651eb55e-acc7-3641-b7af-f1b7a4f9ff36 | -7.1675 | -44.5589 | 2026-09-18 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| cd0f42ca-c379-3daa-b8f4-9f639af4f939 | -6.745 | -45.483 | 2026-09-18 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| f7fb0df0-7d8e-30d5-aff4-694afcbe2765 | -7.3752 | -44.4708 | 2026-09-18 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 58.5 |
| e075d401-4e43-3449-b6ed-e873cc0ba9e0 | -15.6557 | -52.7366 | 2026-09-18 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |


[Clique aqui para ver as próximas entradas](README99.md)
