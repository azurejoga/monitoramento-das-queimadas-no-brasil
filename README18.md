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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db1235a9-c5a4-366a-b971-070c51fad8f5 | -11.35283 | -46.50763 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 87c9da80-f1d9-35a0-a1d2-80163cc9eaad | -11.48185 | -43.63412 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b67fa4bb-3e21-3b6a-957d-5a92070a6b3b | -6.34981 | -43.415 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2f5a4a16-4bd0-31c6-b822-6ec0809281fa | -13.08615 | -43.5468 | 2025-09-11 03:55:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 14567e85-676d-315c-9a15-f242e5f3aedb | -11.48525 | -43.68248 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d6454bab-6c44-3be7-ace5-ffc4688a8888 | -13.34576 | -44.00352 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 03bc6bf4-6265-3c79-b077-37123ebb3267 | -12.1312 | -44.85305 | 2025-09-11 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e059e610-54ce-307c-aef0-5ca7c2d90a3f | -6.38179 | -44.43305 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2d455ba-55fe-31a3-9824-60de27f6d89f | -6.09878 | -45.93294 | 2025-09-11 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 42426bce-641f-3f1b-8544-c6b24554bc22 | -7.5585 | -48.21305 | 2025-09-11 03:55:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3ac39bf1-d838-334b-8c40-516b2269d117 | -7.84805 | -45.40026 | 2025-09-11 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e00e0893-1dd4-3cf8-8c74-481e79bfaf4a | -6.57095 | -44.21064 | 2025-09-11 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 992260cc-d45d-311f-8e75-fe6a1c7de7ab | -7.80305 | -35.03659 | 2025-09-11 03:55:00 | NOAA-21 | ARAÇOIABA | PERNAMBUCO | Brasil | 2601052 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| af69d5ee-7962-30f6-bed0-316375c6fdda | -8.02175 | -49.04925 | 2025-09-11 03:55:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 78641949-4fe4-3f23-a608-e74f65d5a257 | -6.18107 | -43.49322 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 08ad1c43-42fc-3297-9576-c0d434e852f6 | -6.96039 | -44.81715 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 85c56c66-b680-301c-a8b5-5bb6e023f821 | -9.68123 | -46.76161 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b396b933-3a93-3e65-9318-29e790c0a309 | -6.83822 | -45.60113 | 2025-09-11 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4dd7a96c-91b9-3361-8796-cd392af407c9 | -8.79103 | -48.0888 | 2025-09-11 03:55:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 31aafbdb-f244-3d2a-a8f6-532e04de446d | -11.40028 | -45.59051 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9e5827b-8315-3ec8-bc9f-1c00d876cf18 | -11.40194 | -45.60209 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 581e3585-8db8-30c8-8688-7c210ff5d4d2 | -7.26615 | -39.38713 | 2025-09-11 03:55:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ec05b2b4-87d8-3431-9742-90fbc278ecf2 | -7.47697 | -45.29161 | 2025-09-11 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d4d5e95-8a77-3af8-956c-e7e44c54cc0a | -6.54454 | -42.43949 | 2025-09-11 03:55:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 20f8012f-f4ef-3fc3-bad7-62f8d6b581b5 | -11.95996 | -46.65549 | 2025-09-11 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0887ffa7-6aa6-3c16-9e76-544b307affb0 | -11.16834 | -45.27668 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd0cd2ba-7ba0-34ae-ab73-593b5c192ff4 | -6.35475 | -44.07673 | 2025-09-11 03:55:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6f7c3e34-9842-37ca-95d4-181ffceef403 | -6.40109 | -43.50197 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8dca1f74-77e5-308a-acc3-dbda8feb947f | -12.47282 | -47.48682 | 2025-09-11 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| e2c324a2-9ce4-3374-a4d8-f67490fc60b8 | -11.36339 | -46.56087 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 22583e31-03e9-306c-8530-526547c0290f | -7.39078 | -47.36621 | 2025-09-11 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 424a8dba-da0a-3d92-886e-60f00281d6a8 | -12.48131 | -47.49366 | 2025-09-11 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 63e5e79b-e1ab-3a9f-ad95-a9f4e7ecba4a | -5.97218 | -45.81103 | 2025-09-11 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 67dddfbc-8ff3-3e76-96ca-e425e42c499c | -12.03481 | -47.55323 | 2025-09-11 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ebafca27-a942-3ba9-bfaa-5592ab3996e8 | -12.0561 | -47.59768 | 2025-09-11 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 12749ccc-64c9-3cf9-a36a-1bc767135c39 | -9.08247 | -46.96488 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 37d08deb-83b7-3f97-9c6f-e6aea1631073 | -11.48682 | -43.67319 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f046dc65-1d87-333f-b547-ce3f9685da83 | -7.39424 | -47.37625 | 2025-09-11 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 325b42f9-196d-3a67-9e9f-1caab74b459e | -6.70071 | -44.93757 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ae1f6dd-0217-3bbd-810a-9e0b69701db2 | -11.48402 | -43.64407 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 40638fad-6e91-3f96-8532-60670b7a12ca | -8.02102 | -49.05327 | 2025-09-11 03:55:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6509d19-1130-36ef-b320-29b746a6e008 | -6.41801 | -44.3939 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8b86d0b5-9d81-3b8a-876c-4e83372d2eb6 | -6.55594 | -43.98209 | 2025-09-11 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3af1f8a1-ee31-3264-831e-1a9e931e3753 | -7.20792 | -40.24311 | 2025-09-11 03:55:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 51414b99-22b4-3360-8b65-6498fc084c15 | -7.83386 | -45.40298 | 2025-09-11 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79f1e005-4f2e-341b-9ce4-82ba5aa44db2 | -7.36176 | -47.42701 | 2025-09-11 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d320ed5-cdfa-3560-89f9-17e8e0f185fd | -8.80025 | -48.09759 | 2025-09-11 03:55:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4cf9218f-0ff6-3e72-b1b1-56ac1338d4a5 | -6.73314 | -43.02314 | 2025-09-11 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3a24633-9167-37ce-8e47-c5f9a9404693 | -11.02183 | -45.06625 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 8b338fda-962c-360d-b455-5061990f4a4e | -8.03172 | -44.49392 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aeb85c04-85dd-3816-b5d6-aa182cb1324c | -7.26681 | -44.90472 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa6567e1-0ec0-3936-984d-706b07f1dcb4 | -13.48223 | -42.47883 | 2025-09-11 03:55:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 446a0a12-2769-3173-b97a-ae69c00e19de | -7.47044 | -45.27653 | 2025-09-11 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db178769-0321-30b2-8fc0-1852a9b3151d | -6.83738 | -45.60593 | 2025-09-11 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a323c80b-6214-30e0-b61c-d1c04c03c6d7 | -9.77892 | -51.10135 | 2025-09-11 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b147cd11-f194-32a5-b5b7-a96d1e8b8e3d | -7.18629 | -44.95663 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e113c8b-b69f-3710-b2ea-2a9f365ff12e | -12.13581 | -44.85025 | 2025-09-11 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9723e0c-9878-3832-98af-a6b07bea6d23 | -9.67896 | -47.53193 | 2025-09-11 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| bde1dce0-fedc-37b9-be2a-eef025e8fb29 | -8.06638 | -50.18115 | 2025-09-11 03:55:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7ef8d375-acdd-3ca8-a83b-a8d18f6b7bb4 | -7.38854 | -47.37855 | 2025-09-11 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 536fa5f8-d5c1-3389-872f-81284b75c065 | -8.0232 | -49.04131 | 2025-09-11 03:55:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dfba067b-a77c-3522-bb4e-00b64b63e799 | -8.43077 | -47.26833 | 2025-09-11 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bc786982-d50a-3717-8587-4d3b329525dc | -11.46705 | -43.60769 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 665276a2-3507-30bf-a466-baf9842d10b3 | -11.08915 | -51.33602 | 2025-09-11 03:55:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b14a4b0d-03a7-329a-b2d4-0f6b4b48c85b | -6.44144 | -44.0444 | 2025-09-11 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 81a21fea-5ece-35dd-9e25-2906d5817c51 | -12.0041 | -47.5859 | 2025-09-11 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ea2e09d-4a50-36a1-b352-29bb9820ce44 | -8.5205 | -45.69626 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9ad0244f-f067-3768-b9cb-153283470457 | -11.42855 | -43.69669 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ecacf631-7483-3277-825c-1d452b0375e5 | -5.98752 | -43.70247 | 2025-09-11 03:55:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fafd41b3-5a29-3210-8b43-37a447fb8411 | -6.30361 | -45.66463 | 2025-09-11 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5526184-e54c-3feb-b740-973988ebf02b | -9.02252 | -49.76633 | 2025-09-11 03:55:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4a840fdd-efda-38a1-bf06-7d3fe8588827 | -9.90074 | -49.90987 | 2025-09-11 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c28367a8-26ef-3159-8059-3ed19dce38ce | -6.68459 | -44.54419 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e6b4b61-35b4-33f4-8fd8-bf8a28085b09 | -6.53715 | -44.77935 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5575c045-bc11-39fc-8ca8-41f3c81620c7 | -11.48777 | -43.64474 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e5678562-525f-3d6b-b61a-122bf964d7d2 | -11.16341 | -45.30445 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b17e27b-c430-3045-8f5d-7a51be0a6667 | -12.05712 | -47.59223 | 2025-09-11 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1ff31d2c-9666-3f26-8c91-be9d17ce5d99 | -6.31792 | -42.21601 | 2025-09-11 03:55:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 93289ee9-ccf2-3b3c-8954-b591f1d9bd2e | -8.19637 | -50.10241 | 2025-09-11 03:55:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cbe70ba9-ca23-3b8f-a65d-1f57d6e5390f | -11.45502 | -43.61035 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 95782642-d4ca-3312-a8f8-abfa20854147 | -6.55248 | -47.51154 | 2025-09-11 03:55:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d4a0d9f-4ef2-3102-b960-4a6572727cdf | -10.13896 | -47.8936 | 2025-09-11 03:55:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0fef94bb-a476-3f7b-bd6c-4c8034579f75 | -5.75598 | -43.73608 | 2025-09-11 03:55:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 82c8a5b7-73e8-3e46-ab39-933116a9c6cb | -10.4249 | -43.35125 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2510209-3065-337d-a108-3504fdc32f74 | -11.4782 | -49.25023 | 2025-09-11 03:55:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0e89771b-9890-3f17-97ad-3dc0a2a944dc | -8.04423 | -48.67536 | 2025-09-11 03:55:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f2b2a64-d4fe-39fa-9047-0944c015ba05 | -11.49528 | -43.64607 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 80ce504e-acfa-3594-84ca-dc410cd05e39 | -9.81357 | -46.81947 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ccf5e2a1-279c-3f23-bc1f-c31e6708919c | -11.74557 | -48.12153 | 2025-09-11 03:55:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 79b59fbb-0f3a-3a56-a86e-394d3abaaea1 | -6.86062 | -44.90331 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d39dd793-ec2e-34e3-a28b-32cf97090d4b | -9.20903 | -51.8156 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0241535-0437-3f3a-8711-ce5a037c61de | -11.77426 | -46.51712 | 2025-09-11 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 28f5a783-7335-3da2-bedd-9739554041a8 | -5.69638 | -45.32966 | 2025-09-11 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1431eae2-0ce0-3a93-9ee8-b9f93b51e09d | -7.33161 | -49.60888 | 2025-09-11 03:55:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dd279e2d-7df2-3282-9920-36a761662574 | -9.0167 | -49.76526 | 2025-09-11 03:55:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| a4d0870f-e604-3505-9137-c00cb92b6959 | -7.92991 | -44.8877 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07dd5d38-2c65-3109-a0a9-aa3594f1eb9d | -6.47736 | -41.74893 | 2025-09-11 03:55:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| b44c38e9-c4c2-3fec-8f51-75b5f5de83b6 | -11.82015 | -46.75093 | 2025-09-11 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9f392995-54ec-3824-b5f9-d0733f07b903 | -8.03774 | -48.68249 | 2025-09-11 03:55:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59ac633f-29c4-33c7-b254-869e36a925b9 | -6.21391 | -43.4945 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |


[Clique aqui para ver as próximas entradas](README19.md)
