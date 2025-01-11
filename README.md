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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a802dc27-196b-3b67-9c0a-1a837a8a3fba | 1.9419 | -60.4017 | 2025-01-11 00:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 1e02e09e-83bf-3a8b-840c-39a898c50c04 | 1.3034 | -60.4263 | 2025-01-11 00:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 28.5 |
| ad828cc4-5c97-3ceb-a4fd-adc7e0318c9e | 1.3217 | -60.4262 | 2025-01-11 00:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 59f5b752-f283-326f-ab18-038ccb1a714e | -6.0785 | -37.3271 | 2025-01-11 00:00:00 | GOES-16 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 72.4 |
| 4c451fe3-98df-3fb3-8072-203462d2edc3 | 2.6886 | -61.1688 | 2025-01-11 00:00:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 52ef9d67-35b2-3d67-9227-a6a8173bed58 | -6.0788 | -37.301 | 2025-01-11 00:00:00 | GOES-16 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 80.7 |
| eda71910-cd6f-3f04-abff-e0b9fa6f94c7 | 1.3217 | -60.4452 | 2025-01-11 00:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 44.9 |
| cd4ea50d-8399-3eb1-bd64-f8cf5b9cad60 | 2.6703 | -61.169 | 2025-01-11 00:00:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 91.2 |
| d9a74a89-fb2c-3d78-a39b-cca703e13cfe | 1.3034 | -60.4453 | 2025-01-11 00:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 2a41c814-1c0b-3868-b1f1-e747ada26f04 | 1.3034 | -60.4453 | 2025-01-11 00:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 259aee92-b31c-374e-9b45-6beb5e70d4ff | 1.3217 | -60.4262 | 2025-01-11 00:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 337271f0-4842-3bdf-8d33-a6bd7017339a | 1.3217 | -60.4452 | 2025-01-11 00:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 42.9 |
| f53e7626-9786-32d8-bc77-0e74d0767d19 | 2.6703 | -61.169 | 2025-01-11 00:10:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 75.5 |
| a0348242-2925-3c9a-97bc-b9a35ca1d6f4 | 1.9418 | -60.4207 | 2025-01-11 00:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 42dbed21-780c-33f9-bb0d-8eab8cf90956 | 2.6886 | -61.1688 | 2025-01-11 00:10:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 13f41179-fbb5-3474-b7b1-42450fb60228 | 1.9419 | -60.4017 | 2025-01-11 00:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 0a068c23-9cd1-3c99-b7ea-1f25470add83 | 1.9419 | -60.4017 | 2025-01-11 00:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 0e7454ad-f429-35ae-bd80-033f695991ec | 1.3034 | -60.4263 | 2025-01-11 00:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 32.4 |
| b475443d-eb44-3b66-8280-aab81ba5f754 | 2.6703 | -61.169 | 2025-01-11 00:20:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 4b3270f0-eac9-3ad1-bcbb-d720645cc207 | 1.3034 | -60.4453 | 2025-01-11 00:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 0afdd905-3147-3a69-b3d2-f7ecfd007e91 | 1.3217 | -60.4262 | 2025-01-11 00:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 4198ec13-086e-3a84-b60e-6cdde05b6899 | 2.6886 | -61.1688 | 2025-01-11 00:20:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 67.1 |
| b8eb90a3-2977-36a5-af3e-b2deec36368e | 1.3217 | -60.4452 | 2025-01-11 00:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 80ae4c9f-e2f4-360e-b256-d01465bafa6f | 2.6886 | -61.1688 | 2025-01-11 00:30:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 56c390dc-659a-36b0-87e4-fcd6847eaa02 | 1.3034 | -60.4453 | 2025-01-11 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 457fca77-cde5-3414-b24e-5ef9bf3d6afc | 1.3217 | -60.4452 | 2025-01-11 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 41.0 |
| fecc1523-eae0-38b5-8a34-39a03d205a02 | 2.6703 | -61.169 | 2025-01-11 00:30:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 3a2d95fd-950e-3243-a002-5dc41108af93 | 1.9419 | -60.4017 | 2025-01-11 00:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 64.2 |
| b1c95013-7579-3b28-a0f2-e2a88dbebf47 | 1.3217 | -60.4262 | 2025-01-11 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 30.7 |
| cb7c7c64-11f2-311d-9a3b-c2f520a395e3 | 2.683 | -61.1675 | 2025-01-11 00:32:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5c1c60d1-71b1-3ea7-bea8-2a14b81651ef | -19.309999 | -48.3978 | 2025-01-11 00:32:00 | METOP-B | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 79a5d2dd-b170-358d-ba27-3a3266212a27 | 1.3235 | -60.456799 | 2025-01-11 00:32:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 959e2fde-ab9a-36a7-81a1-16b79e0974fc | -3.3556 | -53.257301 | 2025-01-11 00:32:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e51e1918-fb92-34b8-98bf-a26b9ee2f798 | 3.3654 | -60.268799 | 2025-01-11 00:32:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c6fe2ecf-7fb9-33fb-ba2c-cdf03e545645 | 1.9357 | -60.4212 | 2025-01-11 00:32:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| af971cec-6332-3275-8f69-80bdd0935c40 | 1.3177 | -60.437901 | 2025-01-11 00:32:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 292a681f-03d3-3dbe-8109-d8ce97c567b0 | 3.3689 | -60.2537 | 2025-01-11 00:32:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 27b4ed6f-16eb-37f1-b591-4841c30fe15e | 2.6927 | -61.169701 | 2025-01-11 00:32:00 | METOP-B | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 091c1edc-7935-31c3-b83f-648f97ba4c39 | 3.3716 | -60.286098 | 2025-01-11 00:32:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 22bdaeb8-4d2a-3cb0-afb1-b95d8dbdabc9 | -21.5704 | -54.208401 | 2025-01-11 00:32:00 | METOP-B | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 33b727d8-352d-3c36-b6f2-340001d57bcb | -20.2593 | -40.266899 | 2025-01-11 00:32:00 | METOP-B | VITÓRIA | ESPÍRITO SANTO | Brasil | 3205309 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 71bd237f-8cbb-3764-8972-61499a9684b1 | 1.3274 | -60.440102 | 2025-01-11 00:32:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| eba5c20b-609b-3830-a784-1ea22fd673c4 | 2.6788 | -61.185398 | 2025-01-11 00:32:00 | METOP-B | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a4250bdd-81c7-3b73-abb9-968441cd02e9 | 3.3172 | -59.9925 | 2025-01-11 00:32:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2a8a32f4-c3ab-35c8-b2e2-f93cf18e24ea | 1.3138 | -60.454601 | 2025-01-11 00:32:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0a1d663f-252e-3d4d-92fd-0c72991311ff | 3.3751 | -60.271 | 2025-01-11 00:32:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 022097f1-a157-38a1-baa9-04bd2fd13c77 | 1.9395 | -60.404999 | 2025-01-11 00:32:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 77910dc0-e59d-3510-99fa-8fb79166d5aa | -1.7098 | -54.501999 | 2025-01-11 00:32:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44e46586-cd32-3137-a273-5f1ef529e82e | -21.2932 | -48.995998 | 2025-01-11 00:32:00 | METOP-B | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8a2fe802-976f-3d3e-b027-be0b81d78e31 | -21.5606 | -54.2103 | 2025-01-11 00:32:00 | METOP-B | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e47fa728-e1ec-33e8-8b4a-bc0e4a887282 | -21.2948 | -49.0037 | 2025-01-11 00:32:00 | METOP-B | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e1cee864-0e0e-3809-ac42-e357ed276aa6 | -22.016001 | -49.1245 | 2025-01-11 00:32:00 | METOP-B | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 46ee9a88-4893-3d4a-b03a-b99e489a82d8 | 3.3787 | -60.255901 | 2025-01-11 00:32:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 998d646c-3f84-3ce2-831b-3a360dee91e2 | 2.6885 | -61.187599 | 2025-01-11 00:32:00 | METOP-B | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d28a2716-7f5a-39a0-ac3e-3fd4f6e8317f | 1.9454 | -60.423401 | 2025-01-11 00:32:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 026caa26-6b5c-3d2b-a7ea-e20be573e0f7 | 2.6886 | -61.1688 | 2025-01-11 00:40:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 5711fb58-a996-3fc0-bcf0-0b5cabc314ee | 3.3665 | -60.2477 | 2025-01-11 00:40:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 92dd9d93-03bc-3858-a890-4e0967e7a4eb | 1.9236 | -60.4019 | 2025-01-11 00:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 43.1 |
| f4b8f2e6-d6bf-3a21-9cac-afcd7fef74c2 | 3.3664 | -60.2668 | 2025-01-11 00:40:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 52c2eb1c-4b6f-317e-bb30-61133d0d22e5 | 3.3847 | -60.2664 | 2025-01-11 00:40:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 395cd5db-1cdf-38e3-b56e-37ad537e162e | 1.9419 | -60.4017 | 2025-01-11 00:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 2969db2a-9f9d-38b0-9d64-5d574d9e5ede | 3.3848 | -60.2474 | 2025-01-11 00:40:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 2f17a0c4-12fd-3afb-9978-4e0439ed23ab | 2.6703 | -61.169 | 2025-01-11 00:40:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 78358a4f-2fcc-3e24-8ccf-5352b7363c96 | -9.259 | -60.309 | 2025-01-11 00:50:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| a0facb07-8060-3f55-af3c-046102d9568a | 3.3664 | -60.2668 | 2025-01-11 00:50:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 447c3472-9774-30a2-86d9-368c28a528b3 | 1.9236 | -60.4019 | 2025-01-11 00:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 39.1 |
| e145a643-957e-37b8-a4f1-7e0261c8413b | 2.6703 | -61.169 | 2025-01-11 00:50:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 744a8000-f053-3ce5-beb0-47aed6d71681 | 1.9418 | -60.4207 | 2025-01-11 00:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 37d433ac-4c43-3eaf-a278-214cd0c1f1e2 | 1.9419 | -60.4017 | 2025-01-11 00:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 355219f5-c3a7-34fc-842f-54093b191bb5 | 2.6886 | -61.1688 | 2025-01-11 00:50:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 53.9 |
| d87092a6-0010-3030-9c01-0aedc04b7ed5 | 1.9419 | -60.4017 | 2025-01-11 01:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 72459809-e24c-3c99-80d7-66b1a7eb6145 | 2.6886 | -61.1688 | 2025-01-11 01:00:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 50.1 |
| eeb14f32-96c4-3205-af01-7ab6cdc9c0e3 | 1.9418 | -60.4207 | 2025-01-11 01:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 7e0415dc-a698-3c1e-a707-5e9a75760a44 | 1.9236 | -60.4019 | 2025-01-11 01:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 3a0e9a40-cb65-32d4-9063-9b10055e9dc8 | 2.6703 | -61.169 | 2025-01-11 01:00:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 77.2 |
| b0563349-70fd-3684-a572-89b975de7154 | 1.3217 | -60.4452 | 2025-01-11 01:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 29.1 |
| ba3ef423-6d63-34ad-b128-c163b7568f0e | 1.9236 | -60.4019 | 2025-01-11 01:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 34.4 |
| a11c37c8-0b74-37f4-bffe-68824d1acae6 | 2.6886 | -61.1688 | 2025-01-11 01:10:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 4641a27e-ca18-3bd6-86bc-7626a6f0f7b7 | 1.9419 | -60.4017 | 2025-01-11 01:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 3a4749fe-37e3-3839-8ffa-0bdff6df7edb | 2.6703 | -61.169 | 2025-01-11 01:10:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 509c53da-95f6-3ced-bd82-f9e2cffe271f | 1.9418 | -60.4207 | 2025-01-11 01:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 226c58e2-ea81-3f76-8d7e-85f57d33456d | 2.6703 | -61.169 | 2025-01-11 01:20:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 56c9d197-ddb6-3a00-84df-72f7d13633ed | 1.9419 | -60.4017 | 2025-01-11 01:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 1f883a39-76a5-36f3-b9eb-2ebc40f8f608 | 1.9236 | -60.4019 | 2025-01-11 01:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 274f2903-4e03-3937-bd8d-fc934efcbd3c | -30.83247 | -55.3952 | 2025-01-11 01:26:00 | TERRA_M-M | SANT'ANA DO LIVRAMENTO | RIO GRANDE DO SUL | Brasil | 4317103 | 43 | 33 | nan | nan | nan | Pampa | 8.2 |
| 4b255cf2-fe63-32e4-9fb6-2dd736a28380 | -30.38799 | -56.16487 | 2025-01-11 01:26:00 | TERRA_M-M | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 5.5 |
| 2fda7cbb-3237-3cf1-a090-6071371b19a2 | -21.960501 | -57.2724 | 2025-01-11 01:28:00 | METOP-C | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a2bc1642-ab10-3977-8686-4fd91a77be34 | 3.0274 | -61.225498 | 2025-01-11 01:28:00 | METOP-C | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b7f723bc-3a61-3262-acf7-bfb292d18b9a | -30.0334 | -56.2243 | 2025-01-11 01:28:00 | METOP-C | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 94609f8c-feb6-3da8-a2ff-2e44a06c3a05 | 2.2924 | -60.471901 | 2025-01-11 01:28:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 36c3a4d7-3d6e-3895-9459-b1e245d7c70b | 1.5308 | -60.558498 | 2025-01-11 01:28:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8a567d78-dec2-3e21-8e78-b0454d13b5c0 | 3.9374 | -60.574902 | 2025-01-11 01:28:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e76b4bd5-20ee-3f4a-8091-f6010aa886dd | 2.2826 | -60.4697 | 2025-01-11 01:28:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8c6e2fc6-98e2-3fbb-aa9c-1b4b8b3f51eb | 3.7279 | -60.317799 | 2025-01-11 01:28:00 | METOP-C | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8e7a0c4f-9dde-3c51-8b92-0bbedc750832 | 1.672 | -60.481998 | 2025-01-11 01:28:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0ee8b6fc-a064-3c64-bcdb-2bf8af78ff3b | -19.315201 | -54.473099 | 2025-01-11 01:28:00 | METOP-C | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 07d8d723-a60d-35e4-927a-e46db5ab917a | -21.99 | -57.171902 | 2025-01-11 01:28:00 | METOP-C | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c01ab215-3ad9-356d-a0f5-f54fdffa3556 | 3.0258 | -61.232601 | 2025-01-11 01:28:00 | METOP-C | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 444bd165-e32d-3282-89a1-3fe2de801e56 | 3.0356 | -61.234699 | 2025-01-11 01:28:00 | METOP-C | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 60d1c0b1-81c4-3461-80df-407f06b013af | 3.7297 | -60.310001 | 2025-01-11 01:28:00 | METOP-C | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
