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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d88d01c-23bd-3f60-9c08-155d5b2a84bb | -13.85147 | -42.44597 | 2025-10-19 04:12:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 519aa218-302c-3cde-abf1-dcfbb05a7195 | -9.75671 | -43.95842 | 2025-10-19 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78be9015-3d8a-36ef-95be-d76736606d82 | -9.26733 | -44.34178 | 2025-10-19 04:12:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb9ab4ad-d606-320e-b260-30e4adef3b99 | -12.14266 | -45.07678 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a26ae29f-2708-3bd7-8adb-1db6e78d09f0 | -10.88749 | -46.09625 | 2025-10-19 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 081c1a49-4fe8-3e99-b576-c54aca6302a4 | -13.88979 | -43.45069 | 2025-10-19 04:12:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f7fadd23-868d-3b7e-98e9-ca56b9da604c | -12.1837 | -45.09449 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 92243753-598a-3bd0-ac5e-2e86d8acffd8 | -8.53926 | -48.26957 | 2025-10-19 04:12:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72225ba9-53d7-3348-a1cf-d66b93b14aaf | -11.68693 | -47.30056 | 2025-10-19 04:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3c1bf79b-65fa-3886-ab76-2b43e80ff343 | -8.60792 | -40.19607 | 2025-10-19 04:12:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 38.3 |
| 0981fce0-e678-31f8-b320-321f6b2bebf6 | -12.69456 | -46.95874 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb3b5a1c-2fac-37bb-a2d8-0efb39e7d3e5 | -12.2366 | -49.39271 | 2025-10-19 04:12:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1dca1d7d-d4fd-3ba8-af18-9614f5f66c5f | -10.86993 | -43.94458 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 819e411e-081e-36d4-96a7-eeb949776b92 | -10.12383 | -44.53331 | 2025-10-19 04:12:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2cf72e04-6d18-31b4-b3c6-de851b814c6d | -8.36101 | -46.20258 | 2025-10-19 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5bc699f9-8d24-3867-93d4-f9ba9cee70de | -10.88968 | -46.0831 | 2025-10-19 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 52c2184d-d528-347c-88e5-5a8087fdd298 | -13.26868 | -46.49716 | 2025-10-19 04:12:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30b41974-0e52-3317-bb41-0e28345ca41d | -12.15183 | -45.09314 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95d1a440-e6d2-351e-bd5c-413e5fe6d6b2 | -13.88364 | -45.47213 | 2025-10-19 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| baec237a-6a83-36ae-bcb8-b9807f8c0c0b | -12.14533 | -45.06818 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6cb80d4e-0b50-3dce-b51f-7ee35ec59a1c | -9.21834 | -46.068 | 2025-10-19 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b6595d9-63b0-3008-8a64-79939e4b56dd | -10.87449 | -43.93784 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4386266-22e6-3bae-8ff2-4e56af6f4170 | -8.21505 | -43.95882 | 2025-10-19 04:12:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3588c6d3-618a-3c4b-8781-d872332314d7 | -14.10758 | -44.08328 | 2025-10-19 04:12:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 669a0642-bb40-3611-8073-c2995d1e44e2 | -12.97933 | -47.27575 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| efd6f92a-8ec8-3f93-b07d-34b5186ff679 | -11.65203 | -47.31703 | 2025-10-19 04:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c8111a51-e3c0-3421-8e7c-967e9744143d | -13.01995 | -46.95533 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5619046e-2b2b-337d-a64b-a0eb976e93aa | -12.01184 | -46.48199 | 2025-10-19 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 127a03a5-8819-372e-97d4-0d65626334bd | -8.21443 | -43.96256 | 2025-10-19 04:12:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7390196b-a005-378f-8b31-af126b0562ae | -8.43294 | -44.14524 | 2025-10-19 04:12:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dc81b82f-a07e-3b55-b188-b71328916a91 | -8.41629 | -44.13848 | 2025-10-19 04:12:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8a887520-4912-3894-9a4e-dd65d0d5c197 | -12.01477 | -46.48706 | 2025-10-19 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cdcd50e1-f501-3f0d-8759-3e1cccc1f14a | -12.98909 | -47.2874 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1d2cca5d-beed-39b3-b795-2dfb81f56cd7 | -10.22683 | -44.05348 | 2025-10-19 04:12:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 563459e7-d2d2-3051-822b-c7f4e2583e1c | -10.1598 | -42.20795 | 2025-10-19 04:12:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 91cafd7d-e2a4-311d-bf44-10af89f0ff62 | -8.21234 | -43.96306 | 2025-10-19 04:12:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b0b65dde-4f0a-3b3a-88a8-7f7d9b787bd2 | -12.98696 | -47.27713 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a0aef9b6-36b2-393b-810f-00ed9d26100e | -12.68999 | -46.9626 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c7d83c6a-fec0-316c-8857-0623eedc00db | -12.69472 | -46.9611 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b44d7052-f8a1-312e-bc86-019bff30c3f0 | -13.89038 | -45.51741 | 2025-10-19 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b6498308-362a-3c63-b508-176c4fcfbb23 | -12.98865 | -47.26756 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 94cf2234-039f-3095-acf3-d73f6fa3fa31 | -8.3013 | -43.38724 | 2025-10-19 04:12:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9fe6ac13-beac-3ddc-85cd-9a0914747561 | -10.42394 | -45.01358 | 2025-10-19 04:12:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 655b87de-8a40-3db2-ac78-34f1c5c5d3bc | -13.17392 | -46.44119 | 2025-10-19 04:12:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d4ce522c-5527-3c64-8d69-5e9f2372f625 | -10.886 | -46.08254 | 2025-10-19 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8777e7e0-f162-320d-8c92-005de46c8eca | -8.35947 | -46.21183 | 2025-10-19 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ddedddd7-5928-37a3-964f-a20a4d580c7d | -13.01546 | -46.959 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e4940328-a3a8-3f2a-9e73-ba5ad8ded4a4 | -9.91324 | -47.65269 | 2025-10-19 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 47842147-3e12-3bff-b9cd-b8143a0da8cf | -8.47192 | -43.88578 | 2025-10-19 04:12:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3d345ad8-3499-3233-b30b-c92b0f480261 | -10.53738 | -44.50285 | 2025-10-19 04:12:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 57940cd4-0284-317a-83a6-ac0081961d1a | -9.23037 | -46.0654 | 2025-10-19 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eca3f668-48b0-3833-87a3-c9452613ca31 | -11.63628 | -44.06673 | 2025-10-19 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1f4c408-d4d1-3867-bb4d-6db8b6af3478 | -8.42603 | -44.14402 | 2025-10-19 04:12:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49f13577-92e8-3d75-b1ff-2f05ba7ce01a | -8.23483 | -43.98907 | 2025-10-19 04:12:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb88502f-2b7e-3933-b00c-0b915f5fa1f4 | -7.95701 | -48.1216 | 2025-10-19 04:12:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db6c2446-c408-30f4-874a-3e8ad8a64a80 | -10.68054 | -44.54994 | 2025-10-19 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a253660f-9ce9-34be-abcc-71feb20d0d98 | -7.96994 | -43.88246 | 2025-10-19 04:12:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 85b2ee16-585c-368f-a40d-f832f3cb577e | -8.60038 | -45.43542 | 2025-10-19 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7da8fe58-069e-39c6-b695-f054e76b50b4 | -8.43108 | -44.15655 | 2025-10-19 04:12:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 707625c5-eeec-37aa-a58c-e51dad64cb74 | -11.60649 | -44.058 | 2025-10-19 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ee3b0ee-9c5b-3576-b062-675533517b4a | -9.93715 | -47.6608 | 2025-10-19 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 90544cbe-8cc2-354b-80b8-2436ba26a008 | -10.87052 | -43.94092 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76a7f59a-bc5f-36da-a353-8612df677d33 | -8.62486 | -44.00246 | 2025-10-19 04:12:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 598a24fe-5325-3195-adbe-6ddc96973e3a | -10.87787 | -43.93841 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c87d460c-08b6-3f14-b5d7-c033caddf326 | -8.64793 | -39.93166 | 2025-10-19 04:12:00 | NPP-375D | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 179b3d62-682d-36ed-886f-36e2d4835e25 | -12.14402 | -45.07595 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8c66d0f3-3d13-3c88-b46e-57069fe2db9c | -8.43232 | -44.149 | 2025-10-19 04:12:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9e66c6e6-2836-324a-b67c-a3cf139c9def | -11.1532 | -43.25525 | 2025-10-19 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 484b5b5f-8df4-3b04-b23e-1e2477c00fc2 | -13.89588 | -43.45535 | 2025-10-19 04:12:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b97779f-10e5-3f90-931f-96e45c4f49a4 | -12.15814 | -45.09806 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e5c1b38-9c48-3456-b324-b84cc9995d29 | -12.14683 | -45.08044 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3e24008-7c0c-37c9-83ac-bf50573523a5 | -8.24919 | -43.32309 | 2025-10-19 04:12:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| beca6259-ce0e-3fc5-bdc1-76dac45688e5 | -12.33821 | -41.20047 | 2025-10-19 04:12:00 | NPP-375D | WAGNER | BAHIA | Brasil | 2933406 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d9beacbb-6e2b-3367-a21e-99223da05278 | -10.72642 | -44.54147 | 2025-10-19 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 908d6ad2-63c5-3d4a-baf5-514c836376c8 | -7.95991 | -45.94195 | 2025-10-19 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f31ab0c8-f0a0-36ed-91b0-4fe88f9e68e9 | -7.66596 | -46.66364 | 2025-10-19 04:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c831f78-d3a5-3288-91f7-9d54947ba983 | -8.24676 | -44.00267 | 2025-10-19 04:12:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4cdd632b-ebc8-3f8c-91bc-d0feb97f6f27 | -11.41534 | -41.42207 | 2025-10-19 04:12:00 | NPP-375D | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 39bc1c3c-0841-3043-992a-159144dc3dfb | -10.23019 | -44.89647 | 2025-10-19 04:12:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| af7f1f2d-38d3-3a74-90d2-98ee31e7bc65 | -10.85145 | -43.93021 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| debb024d-ba20-3902-8ec5-402d9be94259 | -12.18717 | -45.09509 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 66cc7abb-f487-3168-9e82-a9983b54386c | -10.68907 | -47.94737 | 2025-10-19 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5dcc48d0-b191-3dac-949f-94e545183fb8 | -10.6153 | -48.01656 | 2025-10-19 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f4d5034-14a5-3b8f-bb76-d13791f1b839 | -10.16312 | -42.20848 | 2025-10-19 04:12:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ae8d76e8-59e6-3804-a608-4949f5a91b82 | -11.62936 | -44.08803 | 2025-10-19 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a2bab5c3-f3fa-38e8-ac61-e9aa65ef8660 | -12.14456 | -45.06517 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f040d17-5674-363e-bede-0c561515fac8 | -11.61265 | -44.06277 | 2025-10-19 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bf952047-3955-3a37-be36-31321f44305c | -11.34953 | -44.28336 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db64991b-4223-3e54-91aa-16bdb8fc45bf | -10.68179 | -44.54235 | 2025-10-19 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c82429f6-46e0-35ac-bbe0-9607d70375b7 | -11.36416 | -49.25623 | 2025-10-19 04:12:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| de8229e3-f0d9-34c0-8371-3e0fe1b873a1 | -12.45543 | -45.43671 | 2025-10-19 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4ff5603e-dc7c-35ec-ac0b-c20b5b41f7af | -12.9449 | -47.32652 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7121c4c5-c2a1-3498-986b-ae92072fe7a2 | -13.26578 | -46.49216 | 2025-10-19 04:12:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7609a545-9efc-3d84-9b48-2807ce3ed570 | -12.1864 | -40.62053 | 2025-10-19 04:12:00 | NPP-375D | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7440b5cd-eae2-3a12-b304-954c5349e857 | -8.87948 | -47.9716 | 2025-10-19 04:12:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6cb5c66e-0739-3ff1-afda-f39f06a8e348 | -10.13483 | -44.53126 | 2025-10-19 04:12:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c2a5484-9439-32e6-bff2-4c504d175693 | -12.33732 | -41.3911 | 2025-10-19 04:12:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| cf957e2a-abb9-3f91-ac21-c5a57f65e11d | -12.99246 | -47.26823 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f2bf3966-1048-340b-a8c0-a6bf34be1349 | -9.90789 | -47.65917 | 2025-10-19 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b20b92c-97dd-3248-9f89-f5648af2259a | -8.23828 | -43.98965 | 2025-10-19 04:12:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README29.md)
