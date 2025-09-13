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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1dbf739c-3bfe-3f24-9a15-f5a4cdd2c3b5 | -6.1698 | -41.1387 | 2025-09-13 00:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 74.9 |
| 67191bb8-0a3f-3070-a624-b1714ab65293 | -9.2472 | -59.4007 | 2025-09-13 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 1e5a8eaf-e71f-3745-ac3f-4cdab9d8cec3 | -3.2306 | -47.1131 | 2025-09-13 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 409a2948-5ba1-32fc-ae74-a686671e227e | -10.7661 | -50.5513 | 2025-09-13 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 140.3 |
| cd522db7-89fe-3a41-971a-923fee693dbc | -9.2656 | -59.4191 | 2025-09-13 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 137.3 |
| acdc8bba-c94c-3a67-a545-52e5abf93634 | -15.2226 | -56.6986 | 2025-09-13 00:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 3e450c29-d276-35ae-9622-f8a56f068b06 | -16.5469 | -49.2282 | 2025-09-13 00:10:00 | GOES-19 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 8a834420-79d4-3651-8ea8-90cf72e232bf | -10.6385 | -46.2944 | 2025-09-13 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| fb9ef604-33af-3c47-a888-0a7710dde1c4 | -11.4477 | -43.5514 | 2025-09-13 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 150.8 |
| 1910724d-3e45-3af8-8886-d407b9460ff7 | -11.7424 | -44.2117 | 2025-09-13 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 98.7 |
| ec10c408-6c8a-3a6e-b30d-3499cca54f6e | -10.7664 | -50.5299 | 2025-09-13 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 481.9 |
| 29eeb116-6ed1-367d-96cd-31e5e1df3768 | -11.4285 | -43.5544 | 2025-09-13 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 8c66134b-647b-3820-ba7d-fd947556fba9 | -16.534 | -51.7299 | 2025-09-13 00:10:00 | GOES-19 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 68.0 |
| dd88c89b-3a91-31fc-9bf4-45f7f54bb2e2 | -9.247 | -59.4201 | 2025-09-13 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| cbfa66a3-f6a8-3530-ad5d-9c7fa96174b0 | -16.0061 | -47.9329 | 2025-09-13 00:10:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 103.8 |
| dc7b07c4-5f5c-3578-b295-261dded718e3 | -12.9294 | -54.7333 | 2025-09-13 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 225e29ca-48a1-369e-a1ca-5441af959c62 | -9.5324 | -54.6277 | 2025-09-13 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 159.1 |
| 992a51b3-f96e-3392-a59b-7d99b908434c | -9.2843 | -59.418 | 2025-09-13 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 785f88fc-d8ea-3fa6-be4b-01bcfdc4a2e0 | -16.0257 | -47.9294 | 2025-09-13 00:10:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 275.8 |
| 2a73a533-738c-39a0-b2de-1f84275423b3 | -16.2541 | -50.0745 | 2025-09-13 00:10:00 | GOES-19 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 26f0b3d6-e38e-3bec-96c3-9bc4059fd2ad | -16.0252 | -47.952 | 2025-09-13 00:10:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 1ac29c9a-5fb4-3757-9ae3-45ab33490e79 | -15.1135 | -42.4774 | 2025-09-13 00:10:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 57.1 |
| 34778718-e029-351f-8432-6c06dadfa730 | -8.9493 | -62.1613 | 2025-09-13 00:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 78.3 |
| f6a5a020-8dee-3c77-bb61-ea5444f8e1b9 | -17.3622 | -42.7029 | 2025-09-13 00:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 261d66a0-6a65-3b5d-814d-47170d401850 | -16.4906 | -55.1276 | 2025-09-13 00:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 63.8 |
| 3d858ce8-132a-339b-a735-ce8dfda02294 | -5.2027 | -44.3014 | 2025-09-13 00:10:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| c257602b-55bd-3c48-adba-7f817a71a16d | -9.2658 | -59.3997 | 2025-09-13 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 131.1 |
| 737d91c0-d1ec-358a-b73d-949035c4cf74 | -15.1359 | -52.4892 | 2025-09-13 00:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 9c4b441f-0486-345f-955c-b43673285de3 | -17.3629 | -42.6781 | 2025-09-13 00:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 87a18f7d-5283-35e8-a986-39d828001376 | -9.2505 | -51.2261 | 2025-09-13 00:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| e13d734c-11c9-31e1-83c4-5a214071bf99 | -12.006 | -47.7505 | 2025-09-13 00:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 353d1ed5-6058-3b7c-9a06-30c545e2778b | -9.5137 | -54.6292 | 2025-09-13 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 209.4 |
| 9708863b-c9af-3a1c-aca0-1652626e461b | -9.4807 | -46.4096 | 2025-09-13 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| a9769c25-09c9-381e-8dd5-e1367c0f5be7 | -16.4903 | -55.1484 | 2025-09-13 00:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 77.2 |
| 5b0e4a6d-4086-3574-82e4-6138153f3c48 | -16.2546 | -50.0524 | 2025-09-13 00:10:00 | GOES-19 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 60.5 |
| a3784dde-c492-3dc3-b307-70e9c4d51a68 | -10.6389 | -46.2718 | 2025-09-13 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| f64e0c60-1c7e-351b-a432-0379c7bfb08a | -15.1141 | -42.4528 | 2025-09-13 00:10:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 60.6 |
| 4f8f24aa-9cd5-3018-b879-266a78d66629 | -6.17 | -41.1144 | 2025-09-13 00:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 56.3 |
| f6d2c370-f791-3918-9f45-6131c4ae1981 | -12.9292 | -54.7538 | 2025-09-13 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 86.7 |
| ae063981-5db7-3271-b887-f2c398e6e2dd | -17.3643 | -42.6284 | 2025-09-13 00:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 43.4 |
| dcf91373-5dcd-3757-a2d0-17a1756c8cbb | -15.2229 | -56.6782 | 2025-09-13 00:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 114.3 |
| a103977a-410e-3f86-8479-77d067158747 | -10.0885 | -59.1575 | 2025-09-13 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 0b859426-f843-32fa-a75b-1e48fa7efeb8 | -10.7477 | -50.5106 | 2025-09-13 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 221.6 |
| 27e1a7be-56cf-322d-8055-9a554eb1e8fe | -16.5666 | -49.2247 | 2025-09-13 00:10:00 | GOES-19 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 94.7 |
| caac81e9-f11b-359c-959e-c0fb6232c1ea | -16.5336 | -51.7515 | 2025-09-13 00:10:00 | GOES-19 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 63.6 |
| e1e84142-3ccb-3af9-b989-50c989df4fac | -22.2473 | -48.5869 | 2025-09-13 00:10:00 | GOES-19 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 79.3 |
| ada835c3-87f1-359e-8ea5-93f9322f7ad8 | -16.0449 | -47.9485 | 2025-09-13 00:20:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 210c1714-00a4-34da-8535-7ff1f289cf3d | -3.2321 | -46.7836 | 2025-09-13 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 5c5849be-438e-3196-89b5-5de070eb7849 | -16.08 | -49.9709 | 2025-09-13 00:20:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 6aef07ea-8a71-3af8-b5fb-61732b9fe6b7 | -9.4993 | -46.4299 | 2025-09-13 00:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 164.0 |
| f3e86421-eb32-3bc9-808a-a54b7b7f52ca | -9.2472 | -59.4007 | 2025-09-13 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 910c1d34-af25-3867-a3b4-160043749d4d | -16.5666 | -49.2247 | 2025-09-13 00:20:00 | GOES-19 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 08910621-9437-38ed-966c-32eee70b85b0 | -21.6187 | -46.8115 | 2025-09-13 00:20:00 | GOES-19 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 81.5 |
| 2009de23-3bc7-3848-8f95-ecb0aeb7f96a | -14.1893 | -46.2702 | 2025-09-13 00:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 194.6 |
| dc8fbb76-bb1e-3901-b919-55d8c730ca5b | -8.7785 | -62.8324 | 2025-09-13 00:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 20e88e57-4b0e-3823-8fa7-81deb06796b4 | -9.7297 | -47.5397 | 2025-09-13 00:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 67893d17-63ba-3514-8bab-978e6e6c73c3 | -17.2831 | -47.2594 | 2025-09-13 00:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 35996999-1c16-3d96-95dd-c29183ccb40f | -9.2843 | -59.418 | 2025-09-13 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| f7d22f77-594c-342b-a711-123a79448560 | -11.7196 | -46.6031 | 2025-09-13 00:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| d07871fa-6432-3d82-92ce-12740bffa23f | -20.0192 | -47.6459 | 2025-09-13 00:20:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 95.7 |
| a6562039-2179-3ee1-b5e7-df7cc9f0e646 | -11.7424 | -44.2117 | 2025-09-13 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| aa1af38b-cb59-3ca6-97e6-750d1d08656c | -22.2264 | -48.592 | 2025-09-13 00:20:00 | GOES-19 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 145.8 |
| 03786808-16bb-3ce5-a4c8-4d444b2ff4d6 | -16.4132 | -49.0508 | 2025-09-13 00:20:00 | GOES-19 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 58.4 |
| ffbe8626-443a-341e-846d-83c5990053b0 | -22.2271 | -48.5684 | 2025-09-13 00:20:00 | GOES-19 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.1 |
| 10d88431-236e-376e-91ed-6913cce2421f | -17.3622 | -42.7029 | 2025-09-13 00:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 7c6264f6-d969-3246-86c2-c1e478bb4f18 | -9.2656 | -59.4191 | 2025-09-13 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 133.1 |
| 6537fcbc-a3cb-33da-bda2-494be39c8576 | -17.8434 | -50.4201 | 2025-09-13 00:20:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 011ad3c3-1608-31b4-b7e9-491d11b0a480 | -9.5137 | -54.6292 | 2025-09-13 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 161.0 |
| b8cf6c5b-f707-37be-8e66-ded9cc474d77 | -10.7477 | -50.5106 | 2025-09-13 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 8b1cf407-96ef-3158-81f3-5622dc9cfcfc | -15.2036 | -56.6803 | 2025-09-13 00:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 98119b12-fb89-3d97-b179-15ee2dae808a | -18.4353 | -49.7775 | 2025-09-13 00:20:00 | GOES-19 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 7cffeee4-f61b-354d-918b-39bb394883ec | -11.4477 | -43.5514 | 2025-09-13 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 4a7d4fad-8967-3a49-baf0-2fb42d593939 | -9.2658 | -59.3997 | 2025-09-13 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 40dec446-cafc-3405-97be-259f6b86c0ea | -12.0056 | -47.7728 | 2025-09-13 00:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| a53727af-e800-3478-b832-5bd31d96ef41 | -10.7474 | -50.5319 | 2025-09-13 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 195.0 |
| b23c03a4-e97d-3503-a70f-5c3070a58747 | -3.2306 | -47.1131 | 2025-09-13 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| af52e105-437a-33e8-a093-a129332b3a4f | -10.8972 | -45.58 | 2025-09-13 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 1a69c272-2441-3541-9f77-580b92b19df2 | -9.4804 | -46.4321 | 2025-09-13 00:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| f7000201-7daa-3ba3-b0e2-a7ed366226a4 | -16.5102 | -55.125 | 2025-09-13 00:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 60.5 |
| d1afbb7e-d255-3e29-8426-74f3ccba6bab | -3.2305 | -47.135 | 2025-09-13 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 114.2 |
| fbbf7b70-9ab0-3c31-88c6-a3994de4b17f | -9.2505 | -51.2261 | 2025-09-13 00:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 9e034f8b-4303-3a5e-8ab8-967082ab95df | -11.4285 | -43.5544 | 2025-09-13 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.0 |
| d96d9dbd-c66d-3d87-9126-d1a6b8cc0d2b | -3.2282 | -47.6371 | 2025-09-13 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 171.2 |
| 3a371141-9651-3a61-bd37-65abc47e1fb7 | -17.3643 | -42.6284 | 2025-09-13 00:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 47.6 |
| f4cbb891-338c-3cbe-809c-d2759d914595 | -3.2283 | -47.6154 | 2025-09-13 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 264a72a6-f765-36dc-929b-d549f414a693 | -10.7661 | -50.5513 | 2025-09-13 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 165.6 |
| 16b926e6-7409-3849-ab97-8d56b38aced6 | -10.7664 | -50.5299 | 2025-09-13 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 502.3 |
| 9e729852-9f4e-3e98-8576-1d1c517a4645 | -16.0997 | -49.9677 | 2025-09-13 00:20:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 4d82cbd7-628d-3401-ae0f-bf866fc4abc7 | -10.7667 | -50.5086 | 2025-09-13 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 129.0 |
| d5142dfc-accc-3607-90f5-8b8c2f22786f | -14.2092 | -46.2439 | 2025-09-13 00:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 200.2 |
| eed694f2-6fac-3e85-86bd-b760dcf4474f | -15.6966 | -50.5793 | 2025-09-13 00:20:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 7347f430-70a1-3201-8450-a4174bf30bce | -22.2257 | -48.6155 | 2025-09-13 00:20:00 | GOES-19 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.8 |
| b39895f7-7d1e-3360-869a-d17bc538ecf7 | -9.2844 | -59.3986 | 2025-09-13 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| c2029c3c-8886-379c-85c5-49ef48007190 | -16.0061 | -47.9329 | 2025-09-13 00:20:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 594f18ee-425c-39aa-93fc-b7dbe5bacf02 | -10.1072 | -59.1564 | 2025-09-13 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 4b726731-d2fe-3e21-b346-40d42d241ec7 | -16.0262 | -47.9067 | 2025-09-13 00:20:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 9d6b3303-b976-32d9-87f7-948f79bb1db9 | -11.9869 | -47.7531 | 2025-09-13 00:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 7f045aa4-cf72-331d-9fbc-e5573cbc1a62 | -16.0257 | -47.9294 | 2025-09-13 00:20:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 188.4 |
| 368ceed3-77e7-3d8d-80eb-c6dc5124679d | -9.4617 | -46.4117 | 2025-09-13 00:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 68de1c3b-640d-3f0e-b510-977d61cdb522 | -14.1888 | -46.2932 | 2025-09-13 00:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 99.8 |


[Clique aqui para ver as próximas entradas](README3.md)
