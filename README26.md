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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dcad2a3a-686a-3865-ac5a-a27981e504fc | -7.16662 | -45.04629 | 2026-09-15 04:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c25bed2-1904-3049-9dda-3a8d9bd55161 | -9.35593 | -50.18754 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ac9709c9-74c6-381b-938f-5148ca4fa57f | -7.08744 | -42.10574 | 2026-09-15 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fe707626-79bf-3fa4-884e-8bfa2f9ca9a7 | -13.5594 | -43.52914 | 2026-09-15 04:14:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9dbd7046-ff14-3baf-b56c-e903a8370edb | -7.08717 | -41.83058 | 2026-09-15 04:14:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5ed07731-2a23-3fba-b07c-cb365f957573 | -8.37365 | -54.72419 | 2026-09-15 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f323fb1-0ebd-3092-81e3-f0fe2ac72a64 | -10.68028 | -54.18338 | 2026-09-15 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1a090856-911d-39eb-a83e-cf93b6d0cfa8 | -11.24652 | -43.46317 | 2026-09-15 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d4e4bc31-c3bc-3b40-8261-8167e4978cad | -6.05217 | -46.34683 | 2026-09-15 04:14:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61996ede-fb13-3160-beb6-fad0d76a70e7 | -9.4279 | -50.1035 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e655034e-88e1-323f-8a89-317f48b3be75 | -9.36226 | -50.08765 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f09861ca-6b73-3a30-af39-0d5a8d3dda1f | -10.43938 | -42.74056 | 2026-09-15 04:14:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9b76b3b3-449a-348a-a57b-9af9d2f71b47 | -7.93231 | -49.73914 | 2026-09-15 04:14:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4dee8001-86ed-3932-b062-f3367ee6b367 | -8.30345 | -39.52591 | 2026-09-15 04:14:00 | NPP-375D | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1d9cb4ce-2d90-3208-a6fe-21abb7334c4d | -7.29852 | -42.35662 | 2026-09-15 04:14:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f3bf6244-f102-3c73-930b-583754012dd3 | -9.35776 | -50.17389 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f86d9ec5-596c-34de-a663-a7db4fd4f196 | -7.5221 | -47.33472 | 2026-09-15 04:14:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7f5711b-1a0a-32d7-8786-8ae1fdd5f56a | -6.90861 | -43.22846 | 2026-09-15 04:14:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7134ef2b-9127-3b13-b330-f80f7719e97b | -9.35508 | -50.13278 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| de2ae960-bc6a-3025-95b1-ce1354b9b335 | -7.13668 | -42.12923 | 2026-09-15 04:14:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 56ef5750-7540-3ff7-8e16-584cee8f46bd | -7.96155 | -43.98292 | 2026-09-15 04:14:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8a2b568-3c10-31b2-9720-73a3f1d8d266 | -7.09151 | -42.10254 | 2026-09-15 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2fa3ee9b-d6e0-39ca-bfe8-0981fbbe924f | -13.55414 | -43.52422 | 2026-09-15 04:14:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d5c54ec-adce-38d9-87f6-1ebb4bc3cd44 | -7.17632 | -43.59139 | 2026-09-15 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 62bc11f5-740c-3a1d-ac94-6effcb9b3a3a | -8.39445 | -42.21417 | 2026-09-15 04:14:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8548d0f2-d014-3d06-b4b3-750ee5a6b218 | -7.55937 | -41.84977 | 2026-09-15 04:14:00 | NPP-375D | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 99fb8ec7-3f1d-31d6-8ed7-1c6f3881491d | -8.08605 | -50.96811 | 2026-09-15 04:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 236da995-d228-35b8-92fa-9b3a88dd7ee1 | -7.16447 | -43.52723 | 2026-09-15 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2f9ade51-d301-3273-8528-420079ad58fc | -9.0184 | -47.74243 | 2026-09-15 04:14:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1599a1af-b077-36d7-97f2-cd5dbfdcdcc2 | -7.13185 | -42.0937 | 2026-09-15 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ea44c732-4bb7-3c2f-a412-3c102d8c1f8a | -10.98395 | -48.32813 | 2026-09-15 04:14:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e6e608e4-0afe-3352-ae21-18dcd0f567fa | -12.11881 | -44.20759 | 2026-09-15 04:14:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4aac3aa6-4f9c-350f-9af0-a7ac97f68a88 | -7.08028 | -42.1278 | 2026-09-15 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2e6ba61c-e19b-332c-bbe6-0dc2edcd6ccf | -8.09778 | -43.77538 | 2026-09-15 04:14:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4a49c436-160a-301e-a8bb-cd78436ca754 | -11.81471 | -46.58953 | 2026-09-15 04:14:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59419760-0537-3f7d-a789-d5395c2244af | -10.65855 | -54.14561 | 2026-09-15 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25f690d4-67f7-3c05-a8ce-b7b135776ae2 | -9.16029 | -49.99537 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9ce0b91-1f5b-3e2a-bb52-05a1536a34d8 | -8.59371 | -44.47464 | 2026-09-15 04:14:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2c0e670a-3fa3-3a96-b277-a294e05daeb9 | -11.24628 | -43.44299 | 2026-09-15 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8712560-029b-3858-9fc7-cbdafe18fa6f | -7.25386 | -46.16014 | 2026-09-15 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2061b4cb-e85d-3f1e-a8fe-27bcfacc53f5 | -11.18081 | -42.80486 | 2026-09-15 04:14:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5901ace0-0543-3ddf-bd64-08712d9a8541 | -7.29636 | -46.74877 | 2026-09-15 04:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 40bb93bf-9010-345a-a56b-2a352dd6e3de | -7.0762 | -42.13102 | 2026-09-15 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| b2d3bd1a-14fe-378a-b947-a5d18f3744f4 | -7.1705 | -43.5214 | 2026-09-15 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d06dc11a-f069-39a5-9ec3-b2b919a96d98 | -7.09177 | -41.82374 | 2026-09-15 04:14:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4500bd46-132d-3104-b5e4-c3f7be889792 | -7.24251 | -46.17477 | 2026-09-15 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 15a4bae6-b433-3753-bcb5-4e436de5eeff | -6.94905 | -42.57113 | 2026-09-15 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 045af071-5a7f-3af2-877f-ea5b8b495235 | -9.41774 | -50.09791 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 919ca2e2-8f2e-3b99-920b-bb0addf279f5 | -6.29719 | -41.6825 | 2026-09-15 04:14:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8d2e5708-c4c7-349c-bd6a-4785fdc8d32c | -11.47502 | -47.44094 | 2026-09-15 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b43e75c4-021c-3496-9356-86bc4e893ba1 | -6.25944 | -41.97863 | 2026-09-15 04:14:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| bdabfd63-d63a-3fc0-9ffe-ea13cc9699f3 | -10.89391 | -51.5657 | 2026-09-15 04:14:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 136ce082-c7ef-38b7-8f19-431aaf657fa0 | -9.3627 | -50.18157 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9ad6af6c-77b1-3a05-8c03-00917efa274b | -7.6155 | -47.29193 | 2026-09-15 04:14:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d91a4c1-3b95-3e6e-ab25-d6b3d939f5ac | -12.49493 | -44.63667 | 2026-09-15 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de736430-9554-38d9-a83a-399fb22ade0d | -7.61303 | -47.29435 | 2026-09-15 04:14:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 42a19f11-1e3b-308b-a1f8-efab2a0b2c1d | -5.92531 | -47.38328 | 2026-09-15 04:14:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4894b241-2b2d-3741-8665-d716bb3d6c53 | -9.87628 | -47.77317 | 2026-09-15 04:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e03ca8fb-2768-316f-8569-299cf5961d63 | -9.41038 | -50.10733 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 70e65681-5a5e-37fa-b3df-f12ec1cb10f5 | -10.58615 | -47.74214 | 2026-09-15 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1c64737-7ba5-38b4-a6c5-f8ebecb78a97 | -13.55632 | -43.53244 | 2026-09-15 04:14:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e414ccca-aa40-3018-857d-2fd147d7fe22 | -7.17254 | -43.5241 | 2026-09-15 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 40e140f9-9475-3009-9d1f-9547b03160f0 | -11.33799 | -46.79135 | 2026-09-15 04:14:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 436faeaf-6638-3790-ae80-f8fc78891000 | -7.09578 | -43.54001 | 2026-09-15 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| ed8b0f56-91d3-3f2a-b031-403305db7923 | -11.88389 | -43.81844 | 2026-09-15 04:14:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 32e79c8e-b303-38c3-b249-fd18a39d01ca | -12.47988 | -41.39682 | 2026-09-15 04:14:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8aee829f-dfcc-316e-9ec7-66bf090d119c | -11.19322 | -42.81001 | 2026-09-15 04:14:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e424b712-a61e-33cc-99b8-91ca9886b36a | -9.41579 | -50.10838 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c6fbdb01-c1f9-32b1-ab2e-2064a2b10c38 | -12.12169 | -44.21236 | 2026-09-15 04:14:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00e50bfa-c3f5-322f-a2f1-3107be5ae675 | -7.23751 | -46.17809 | 2026-09-15 04:14:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dfde7c5b-6ba0-3661-b83c-8129b928b99b | -6.28572 | -41.68827 | 2026-09-15 04:14:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 02989993-ee07-30aa-b08c-cf658475ade3 | -8.09483 | -43.77672 | 2026-09-15 04:14:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 765afb4d-5a85-321b-adfc-4ceb50b15898 | -12.97799 | -41.07085 | 2026-09-15 04:14:00 | NPP-375D | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6a55d70b-8c96-3a32-b682-7bd19abbed9a | -7.10838 | -41.80763 | 2026-09-15 04:14:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7cae1da1-5512-32c6-a93e-946148b8e5ce | -7.23168 | -46.1601 | 2026-09-15 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1728123b-b8c0-3ae3-be78-3a03314fae74 | -8.59293 | -44.47934 | 2026-09-15 04:14:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b10c5e52-b7e1-38c7-a1a5-80faed0b05c1 | -11.8881 | -43.81504 | 2026-09-15 04:14:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a573836-f15e-3fe4-a132-2050c8f6a8ed | -7.08435 | -41.8263 | 2026-09-15 04:14:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 49407264-7d06-39a1-bb9b-a30422abab0a | -7.10652 | -42.09727 | 2026-09-15 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6121eab5-6728-3622-a67b-9a7d130a73f4 | -10.03526 | -52.09703 | 2026-09-15 04:14:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5667a77f-920c-398b-84aa-55aca7d1062b | -8.48995 | -44.59018 | 2026-09-15 04:14:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 10ed23a4-6ed2-3743-8bb7-115c34725652 | -11.17177 | -42.79566 | 2026-09-15 04:14:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b6d49596-c3c1-3f22-bcb4-d99ed596866e | -11.36084 | -43.96677 | 2026-09-15 04:14:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6100d959-5993-3bf2-bb0d-384abb31d0f7 | -10.57631 | -47.74473 | 2026-09-15 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| da5a07f5-02d9-3c8d-ab12-c102095af14e | -10.75835 | -44.82293 | 2026-09-15 04:14:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 02fb4360-681e-397f-a961-836149e5bd84 | -7.2303 | -46.16822 | 2026-09-15 04:14:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e9771e13-8a09-3f26-a656-604f305871db | -10.75539 | -44.81768 | 2026-09-15 04:14:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 78d35e75-c995-3657-bb75-e63191bfbde6 | -7.77177 | -49.48029 | 2026-09-15 04:14:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e00f5940-2bdd-3a15-86a3-8394c10b4ef7 | -7.29442 | -42.35989 | 2026-09-15 04:14:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 55969dcd-fdb8-3c52-b751-68709aaf0136 | -11.23538 | -43.46528 | 2026-09-15 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f2655660-fd0f-32e6-b542-81dbdb3f7606 | -10.89719 | -51.54928 | 2026-09-15 04:14:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19d518c8-1984-3f7b-97ad-b2b0ed325238 | -8.21552 | -43.78516 | 2026-09-15 04:14:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 77fc0a55-4c1a-32b5-886a-631e7251726b | -12.4743 | -41.41039 | 2026-09-15 04:14:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f8896c56-b2b6-3aad-b22d-406a3e3e26b5 | -11.2297 | -43.45625 | 2026-09-15 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56adeb16-5db7-30f8-b69f-00a4027fea59 | -7.10295 | -47.48519 | 2026-09-15 04:14:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ac2670f6-59b2-3afa-b7c8-e98c3f9ea5fa | -11.97733 | -44.93245 | 2026-09-15 04:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1cc68946-8725-3122-a42f-702c09c7fdfe | -10.97929 | -48.32715 | 2026-09-15 04:14:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 88018e82-aa00-3ccd-a4c6-501eb2e6d5c6 | -10.66951 | -54.16115 | 2026-09-15 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 469a309d-5683-3b6c-b5d6-6a2ac99ab0d3 | -9.88548 | -47.77481 | 2026-09-15 04:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 190ec58e-0521-3752-b8a5-1d14392775e0 | -6.43428 | -43.06971 | 2026-09-15 04:14:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README27.md)
