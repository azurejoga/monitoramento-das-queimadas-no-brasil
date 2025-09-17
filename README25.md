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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 784e0114-647d-3acc-b167-a036fcb60fad | -6.6173 | -45.58368 | 2025-09-17 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3f8b74ed-4c3d-3052-984e-1fd91542d5b1 | -7.8598 | -48.1735 | 2025-09-17 04:10:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d55a414-86a7-38fa-9219-070fefab0d72 | -8.9265 | -46.23291 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68b4b756-20c0-375b-883b-bbd0b56476f8 | -6.98125 | -44.45284 | 2025-09-17 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3095baec-76ae-3742-87fc-59f7b1198280 | -6.33679 | -43.32755 | 2025-09-17 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f596ab08-482e-36c9-b143-b29b4267b4b2 | -3.03518 | -43.2458 | 2025-09-17 04:10:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16e3f156-ee50-36a2-b718-1dc9ce1667f3 | -7.47714 | -46.10146 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e12a7fb4-aaf2-3e69-be9b-045677b805ce | -9.07226 | -44.94875 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 838f4d08-00b0-3f79-8b65-6d69f29b1c8f | -8.97182 | -46.33805 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7f6bf96-cb02-3d59-8d63-498096f789c3 | -6.21608 | -43.90035 | 2025-09-17 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5e1547ee-d712-37ad-ad22-5e62788c8f55 | -8.24657 | -44.83747 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f59f073c-19ca-3a56-8b19-7385af42aeb8 | -7.52975 | -44.72198 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 18131474-0e40-3c32-90bd-2cea0a395f2d | -8.68471 | -46.4034 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3493e792-713a-3d3f-9de0-0cc2386f312e | -2.29599 | -48.14332 | 2025-09-17 04:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b9bbf7b4-0b9d-344d-8226-d5378c2ac31d | -5.62719 | -44.33045 | 2025-09-17 04:10:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c5f8cf8-1de7-301c-93cc-53a562a551a8 | -6.22597 | -43.90597 | 2025-09-17 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88479468-d3f8-3e5f-80ed-96ef98921553 | -7.57348 | -44.55685 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 14d42ffc-5830-3c2c-b189-7e3d3f4b649d | -6.68666 | -46.30417 | 2025-09-17 04:10:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b21cb5c-610e-32e7-97a5-5e709172913e | -7.20947 | -44.38155 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a463cd4-235c-3a27-985d-3f9c35386bf5 | -5.78269 | -43.92598 | 2025-09-17 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 3b99a948-be79-33c8-a2e2-7dd6124e9788 | -9.06869 | -44.94817 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b2e1f77-5564-3b4f-a3db-c7ede287f685 | -8.8932 | -47.87296 | 2025-09-17 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2684198e-0c10-3f5f-8255-1e6f53e54bc4 | -7.04154 | -44.30671 | 2025-09-17 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 950c71a2-ce5a-315f-8455-455c4970ab1a | -7.62776 | -44.4712 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1631636b-83b4-3c89-b919-ef761f714928 | -6.41327 | -42.65421 | 2025-09-17 04:10:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f7370703-16c5-3d98-82f4-f70fd14d47b6 | -8.96762 | -46.01493 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d74c43aa-93ad-3138-99c2-77af01607518 | -6.39584 | -43.34774 | 2025-09-17 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 11275cef-4b9a-37b0-b1a5-97abbadcf84b | -9.13859 | -46.93619 | 2025-09-17 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8b248cb4-7846-3409-bb2d-365b4a940ae3 | -6.22305 | -42.02405 | 2025-09-17 04:10:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6b5a6f5f-22e3-3457-809b-d13e55c814f5 | -6.48426 | -46.00376 | 2025-09-17 04:10:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fcfab58a-60a1-392d-b3ba-4dcd12661a66 | -7.25621 | -46.60394 | 2025-09-17 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71b1cf6d-2202-3990-b07f-dd7a8a552d49 | -7.76466 | -44.7318 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d5ff055b-b5b9-3f69-b5a5-27064a823b47 | -5.53055 | -42.1868 | 2025-09-17 04:10:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4e254170-60c3-39e4-91b0-931534c2d770 | -8.25015 | -44.83807 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1be83077-8f8f-31ea-b4d4-97d248e7989a | -6.60892 | -45.58718 | 2025-09-17 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 655bb8a6-4f72-3b6c-98f1-d0db442e72be | -6.39644 | -42.65151 | 2025-09-17 04:10:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| de509bf9-cd9e-3bb1-b391-6dbcf0e1366a | -8.9229 | -46.20806 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 21b5a4dd-f2ad-35f1-acd3-c3222073ef7c | -5.67408 | -45.0461 | 2025-09-17 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4c238253-b9bf-3ac5-86cc-96359ef47a59 | -6.35655 | -43.16034 | 2025-09-17 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1086b2e6-6150-3ddb-a33e-a3fee1956c8b | -5.2167 | -42.32217 | 2025-09-17 04:10:00 | NPP-375D | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9381cffe-1160-39fd-93d0-73c1403dde8f | -8.56202 | -46.36803 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ccab58a2-70db-3915-ac57-cca53f62596f | -9.09158 | -44.89824 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4fa44f7b-979f-3f6c-a9cb-9d9791fe8c62 | -5.50271 | -39.70268 | 2025-09-17 04:10:00 | NPP-375D | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 937f1b42-511a-323e-a44a-b00ed8512ca0 | -4.92379 | -47.86646 | 2025-09-17 04:10:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 843cd45e-f225-351e-9fd3-22d347fa85d2 | -8.95995 | -46.26782 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c41f1d4a-56f3-3d91-9696-d1de336806d5 | -5.34867 | -44.8218 | 2025-09-17 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b8973d3-70d2-39ad-9ffb-60357705aca8 | -6.16142 | -45.10909 | 2025-09-17 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29a2039f-a9a3-3edd-8444-f7b55cc1c44b | -7.65323 | -44.47128 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f2bbd600-89e4-3d8d-84aa-080621ad417a | -6.95678 | -44.55718 | 2025-09-17 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 90407c1e-3f12-3240-82d9-9cdbb0aeb60c | -8.89745 | -47.87365 | 2025-09-17 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7c994c8b-54cc-3754-91b5-e975cb3a5c44 | -9.08748 | -46.93642 | 2025-09-17 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 061a18cc-5172-3fc8-8f27-57a9a7fcb73a | -6.41385 | -42.65063 | 2025-09-17 04:10:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b1797d79-3062-3e6b-801f-358f07050ffa | -6.44753 | -42.63421 | 2025-09-17 04:10:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f953f75a-cc2c-35e9-90ad-741ff04cc968 | -4.51504 | -38.5481 | 2025-09-17 04:10:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 67adb5b7-df40-392a-adfc-98365ad11f2e | -7.72321 | -45.29629 | 2025-09-17 04:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1031a32-5e08-3d4f-b7ba-9c34d3b12d19 | -2.96039 | -48.58729 | 2025-09-17 04:10:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a855246-5591-36c0-a083-f45e1369bbc8 | -6.86892 | -38.43951 | 2025-09-17 04:10:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b5766ea4-0129-33cf-812f-e72b0f6caca4 | -2.26099 | -47.84229 | 2025-09-17 04:10:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c7304ee-c6c4-33a4-b42a-057df6854345 | -8.96604 | -44.1908 | 2025-09-17 04:10:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a90dd4b-6372-3631-b380-c04585d95d66 | -9.75185 | -47.33582 | 2025-09-17 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f4444718-7411-347b-bf00-42e5c585975f | -7.09382 | -44.53718 | 2025-09-17 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bc128e49-4f83-33f0-a6fc-0e53ad6b501e | -6.87755 | -43.95968 | 2025-09-17 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9e32f003-d83b-3c1b-ada7-d442f4d3e10d | -7.5757 | -44.56553 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6d66e2a4-5bf6-3a0a-8ea0-c037bb5f2632 | -4.38879 | -38.69287 | 2025-09-17 04:10:00 | NPP-375D | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 31d45ea6-dbf0-32f6-81c8-a1a9eb246974 | -7.21588 | -44.38691 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f18b2307-b03f-324b-a8d3-961dbb7928bf | -7.26478 | -46.60203 | 2025-09-17 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55e123d6-8110-3231-818b-c431710afdca | -8.78762 | -47.80958 | 2025-09-17 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74c2bbc8-03fa-3964-a454-a54c0a9f90cb | -5.32664 | -44.99958 | 2025-09-17 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e56b39f0-b3da-39ff-8a10-a0d7020e56c8 | -6.39704 | -43.34029 | 2025-09-17 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49c07608-1ccd-39ef-853c-cf984bbca54e | -6.44478 | -44.51262 | 2025-09-17 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15ed1b8d-4528-309f-9dba-8326d6f8372d | -6.17585 | -41.22963 | 2025-09-17 04:10:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fa022873-8fc3-386e-b1e2-44b003fcf136 | -6.159 | -44.52824 | 2025-09-17 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17a922db-a30f-3c5f-9b3e-9295ba2ce283 | -8.56154 | -47.56423 | 2025-09-17 04:10:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1b27fb17-de99-3656-b0dd-aabc4e4d4566 | -5.64003 | -43.89136 | 2025-09-17 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5123c94b-dc27-3bea-99db-4f4f4261fdfa | -8.78831 | -47.80563 | 2025-09-17 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1c6eff1b-c95a-3b81-9c15-654f29238e75 | -3.23328 | -46.78715 | 2025-09-17 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3ed070de-77ad-38ae-8a2c-f4566a980f1a | -5.39926 | -46.52844 | 2025-09-17 04:10:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b52ab362-f3b6-394a-967f-d93b43bd4a0c | -8.91466 | -46.27906 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88c3c3aa-ff14-3e44-bd94-6b8bf127d432 | -7.73804 | -44.82485 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff90abcc-83d5-33a0-b5af-6452ed904d73 | -8.91083 | -46.2784 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 190793ec-46f6-3009-848e-16610b44dc04 | -4.51857 | -38.54863 | 2025-09-17 04:10:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ff0d8d78-f9a0-34f2-9498-7ae688bdb687 | -6.39825 | -43.33285 | 2025-09-17 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 511882e4-e90a-3e35-b280-00d535de5290 | -6.68269 | -46.30353 | 2025-09-17 04:10:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 92af5ca3-1c41-3392-9727-ffe8097d4955 | -6.25203 | -43.45924 | 2025-09-17 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4495fedc-978d-32ee-a47f-b1e0e4aa48b5 | -8.6614 | -46.39977 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c15f4791-825d-33f3-b02d-f26332f602f1 | -9.60055 | -45.65541 | 2025-09-17 04:10:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b34a501-d83f-39c6-8acc-0aeccb3562a0 | -9.06373 | -46.57819 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 952b3ff3-7f62-36ef-a6b8-bff2ddef13dd | -3.39682 | -44.75383 | 2025-09-17 04:10:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 236ba299-6047-3091-aa50-c1b41783e313 | -9.06512 | -44.94762 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cbd39926-014d-3ee4-af3a-89041e60b1af | -7.31745 | -43.96115 | 2025-09-17 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec81a911-8253-30b2-a6a1-93798aaa195f | -8.66071 | -46.40213 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 38ad5589-67e1-3ab1-ac75-8ae17a34e37c | -8.15875 | -46.7541 | 2025-09-17 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 648a4aed-4f6a-32af-8323-b46a98587d68 | -7.89132 | -48.17481 | 2025-09-17 04:10:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2dd4dbb3-ca3b-305c-9e35-f3df3014c14e | -3.64364 | -48.32634 | 2025-09-17 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f59ee21-486e-3f8e-8679-9dd28839b67e | -7.57881 | -44.5909 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cab936d7-460c-336a-b8bd-ea30474acad2 | -2.26329 | -47.88879 | 2025-09-17 04:10:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93ba0ec9-c60a-3883-91fd-5ecdade996fe | -5.20718 | -45.18178 | 2025-09-17 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 26f8bf05-4495-350a-8c1e-1d8704da8e75 | -6.97541 | -44.44383 | 2025-09-17 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cc54c635-ef5b-35ff-971c-259b3ccaa605 | -6.33619 | -43.33129 | 2025-09-17 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5ca9bc3d-fc58-3a91-adbd-7480c3c99888 | -6.45964 | -46.00773 | 2025-09-17 04:10:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README26.md)
