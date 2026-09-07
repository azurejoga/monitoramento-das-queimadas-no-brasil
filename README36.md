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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6677533c-2b01-367a-9bb8-bf41a23ce387 | -3.08973 | -61.06958 | 2026-09-07 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c34825bd-2aaa-3641-92c1-43770e332c56 | -3.38837 | -61.31654 | 2026-09-07 06:08:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89a28002-412c-3604-baf6-6c8ac60d8b1a | -5.26608 | -60.1176 | 2026-09-07 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0b7d5179-7d19-3354-9e10-f4b444be6a7e | -8.53041 | -63.88267 | 2026-09-07 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09be5bdd-e300-355a-b580-6e8febb2fd2e | -3.61342 | -60.56775 | 2026-09-07 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7b4f29d4-45ce-30aa-8def-fc271d57baea | -3.77052 | -61.75108 | 2026-09-07 06:08:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 559c959a-06aa-383c-9c62-b9b86433dfa9 | -3.39171 | -61.33228 | 2026-09-07 06:08:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e81789e1-755f-3b0b-bae6-55a1dc7d8250 | -3.18903 | -61.13982 | 2026-09-07 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2d8a8175-489a-396d-ab3c-755018ac19fd | -8.52962 | -63.88861 | 2026-09-07 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9d2a7887-d150-36d2-a2f6-1aa1b241d9a3 | -5.2944 | -60.14159 | 2026-09-07 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 06070813-c296-3208-908b-9ddc8f04637c | -5.26642 | -60.16187 | 2026-09-07 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81ee9696-6e94-3d3f-8a0b-e15d96922443 | -3.41887 | -59.24264 | 2026-09-07 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5f9f7ceb-1f91-3f3a-bb31-26498cf20612 | -3.38183 | -59.4099 | 2026-09-07 06:08:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 169944e2-7a8c-3910-b728-59549f0f2234 | -8.54599 | -63.88187 | 2026-09-07 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80387530-4204-3beb-8296-4f318c2f0bd1 | -8.52185 | -63.86934 | 2026-09-07 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16f61e08-24e1-3b8e-b0e0-019218e940ed | -3.61237 | -60.56472 | 2026-09-07 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dcf749bf-fad6-3295-812e-c2b1ec1e0355 | -3.14829 | -60.65754 | 2026-09-07 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9acf610b-4897-38e1-82bb-328e3b748721 | -3.08522 | -61.53337 | 2026-09-07 06:08:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad2f4b13-2042-3846-9e38-b370eef866af | -3.3934 | -61.31304 | 2026-09-07 06:08:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b2a39b6f-8e18-3770-83a1-29cfe05d5164 | -3.41813 | -59.24779 | 2026-09-07 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| df51d907-c702-32aa-8846-190634615f7b | -5.30256 | -60.12803 | 2026-09-07 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 59f4a1dc-9546-3860-866c-976f33ada7b9 | -5.29084 | -60.12137 | 2026-09-07 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b92b5cf1-d064-3a61-8ada-9207c4d56a1a | -3.14555 | -60.63603 | 2026-09-07 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b66cba0a-5399-3af2-91c7-13910fae5936 | -3.15408 | -60.65854 | 2026-09-07 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9c1a62b-c724-3187-8682-6c9cc5454b7c | -8.87146 | -62.35136 | 2026-09-07 06:08:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb6b0f90-0a32-321d-b036-a1f8631c97eb | -5.29018 | -60.12617 | 2026-09-07 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cef284d5-9fde-3bff-93ca-d23a06654af5 | -8.53199 | -63.87077 | 2026-09-07 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d00924bd-bf51-324a-bfa3-cc0caadadc23 | -3.09249 | -61.06987 | 2026-09-07 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bb713f66-1618-3faf-bf6c-ab5b2a6759a7 | -5.29572 | -60.1319 | 2026-09-07 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 38e84e71-473b-3049-b5e4-a279951f1e2d | -3.3867 | -61.32774 | 2026-09-07 06:08:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da645642-79c2-3aa2-a8b3-c84835af4d20 | -13.2284 | -61.7743 | 2026-09-07 06:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 512ef44b-167a-3bcc-bd96-c31accee3479 | -13.3198 | -45.2409 | 2026-09-07 06:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 105.6 |
| d3711adb-dc82-369a-a36e-381c624546ef | -13.2666 | -61.7524 | 2026-09-07 06:10:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 5acbd4aa-fd32-3e3e-8508-af10dc340dbf | -13.2097 | -61.7367 | 2026-09-07 06:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 53.3 |
| e167703b-73dd-3815-87ec-1079203175cc | -13.3009 | -45.2209 | 2026-09-07 06:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 146.6 |
| 2b561191-39ef-3dcd-b2a1-2200bd8bd773 | -13.2474 | -61.773 | 2026-09-07 06:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 9a3255ea-e099-3317-8859-3c11081e736d | -13.3203 | -45.2177 | 2026-09-07 06:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 677a3062-5cd2-35d3-97a9-9315e7acddc7 | -3.1461 | -60.6696 | 2026-09-07 06:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| c417a81a-6049-33fb-958f-bb353bb7e2a7 | -13.2287 | -61.7355 | 2026-09-07 06:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 6b29f7eb-e1b0-3c67-9060-4893ea9ca336 | -13.3004 | -45.2442 | 2026-09-07 06:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 48421e79-3042-3734-9dfa-eb712f7f89ff | -13.2664 | -61.7718 | 2026-09-07 06:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 54c8b82a-04c0-38f1-a51a-10fe82cf71b4 | -13.21383 | -61.74071 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74ad558d-ea1a-3b22-9cad-6b3152d5397f | -13.24036 | -61.73882 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2c2360e9-1bfe-3430-a1a7-335840449186 | -13.24262 | -61.77384 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 147d31f7-e42d-3757-9d7e-26c53c4cfa5b | -13.2661 | -61.72239 | 2026-09-07 06:10:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| a66d5d19-f65d-3602-9302-585c5bc9bb2e | -13.22121 | -61.74142 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 3409b7a9-a01b-35c2-bfaf-1492b33a1877 | -13.21535 | -61.78554 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f5e856c2-480b-37b4-96f9-2009f5e42469 | -13.23494 | -61.77815 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e8dd35f5-4adc-3651-9c96-65399adcb9cf | -13.23546 | -61.77328 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b8a2d14e-c7c8-3c6c-8326-1165c997282a | -13.22969 | -61.77718 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 865692ff-9c77-33ea-9ba6-be952a5d24af | -11.40668 | -62.12806 | 2026-09-07 06:10:00 | NOAA-21 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8393fdb6-a5ae-3bc4-9a14-1bd4311818d7 | -13.21501 | -61.74067 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 4dc2a2b9-07e1-3f97-8538-812560298c2d | -13.24318 | -61.76896 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e4ea8f19-89e3-3f74-aabf-1c5b227972fa | -13.23348 | -61.7332 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 79f84c67-8d08-3c22-8c66-9769c09eae3d | -13.28526 | -61.71981 | 2026-09-07 06:10:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56ea94fd-7c4e-3417-bce6-2d1aa481fc28 | -13.23472 | -61.73314 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f694b145-24d9-3070-b66b-2c2f3b7c7512 | -13.22205 | -61.78146 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2973e999-6ac3-3e0a-9cf1-e39ba863f290 | -13.22296 | -61.78127 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4c698499-95dd-35f1-a037-e9c297fadd82 | -13.25368 | -61.72079 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ea954a53-576b-3df2-a27a-7d15b8dee6be | -13.24165 | -61.77407 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ce03cc34-80dc-3082-a5cf-e2d70566ae9a | -13.22852 | -61.73238 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5d443728-b6a1-35bd-8438-2d38feaa3133 | -13.22108 | -61.73162 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 0fb97b44-1a19-365f-985d-3e082bedd7f5 | -13.26181 | -61.76173 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 12.5 |
| ff6afe2f-172f-3e29-af7a-3507db41bd4d | -13.22796 | -61.73729 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 12eee073-8e37-34ab-adc5-73db4f35812a | -13.24825 | -61.72485 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fa6a3f7c-fe15-3d08-99d8-2653ef13e0ef | -13.24021 | -61.72906 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 71db7e8d-1959-35ce-a7df-0bfe6d0887b7 | -13.21556 | -61.73576 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 69a667da-10db-3d1e-b902-dd677709bcc5 | -13.23588 | -61.77794 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2f4a20d9-201c-3819-97ac-3b426cbedc3c | -13.27284 | -61.71824 | 2026-09-07 06:10:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dfc884b8-2572-39e0-905d-afdf2fdaf094 | -11.40717 | -62.12387 | 2026-09-07 06:10:00 | NOAA-21 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3647f039-e4e4-3e3c-9938-c900329478d1 | -13.26127 | -61.76664 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 96a78110-0e27-3aaf-8451-39e420819e52 | -13.24218 | -61.76917 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0ed4a487-ce20-3dbe-8e63-da3abb1e2c8a | -13.22728 | -61.73242 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 21.0 |
| f37fc355-b074-301f-837b-0a10d9cdb937 | -13.24769 | -61.72977 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0dbf2d24-8a23-32d7-b659-1e7e6262af61 | -13.23915 | -61.73892 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e96f8a4f-063d-31db-9102-9e1b69f62ead | -13.25989 | -61.7216 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 05fcab34-7226-3794-a353-b529380ee7cd | -13.23401 | -61.72826 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 448d29e7-08d2-3d84-97b5-ec58040d45c4 | -13.25508 | -61.76585 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 06583839-15b1-30c3-bc5c-ce23400caeda | -13.22908 | -61.72745 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 223d7dec-b237-3456-a787-011140f166fb | -13.24695 | -61.72492 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 114af930-920d-32a3-a724-ea4c00d1fd29 | -13.22914 | -61.78205 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 723dccd3-506e-3548-9b9b-790a2dacbfd0 | -13.22176 | -61.73651 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 68470a61-7a91-3721-84b8-fe67fdf3e14c | -13.25315 | -61.72573 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e9f8f58d-7382-3a50-a015-bffe2179e2ca | -13.24642 | -61.72985 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 08b40a63-0f78-3e53-b9df-b44d94d47aec | -13.22056 | -61.73656 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 33.6 |
| ad813fae-196b-380a-a165-0786b65c9732 | -13.24836 | -61.76996 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7a75963d-451b-39cc-b202-6e79e33aafaa | -13.27905 | -61.71904 | 2026-09-07 06:10:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9c3d76f0-9fd8-3332-981e-8696dd3973d4 | -13.24074 | -61.72413 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f647da12-ef0c-35b9-bc2e-ecc3a68df633 | -13.22232 | -61.73161 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 28b51773-54cd-30f1-b6a3-f8614474c74e | -13.23643 | -61.77307 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 62e29721-bd7b-335b-9d79-3c100c3621cb | -13.23528 | -61.72822 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0683d097-3e92-3a9a-ad9b-c2cef198f3a1 | -13.24148 | -61.729 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 802777a4-2425-3786-b71b-f5f35e8d2b8e | -13.22781 | -61.72748 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 21.0 |
| e896cd69-364d-3876-af10-8348a265cf64 | -13.21435 | -61.73579 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7de4f4ea-bf82-33c3-b89c-aea1da6235fc | -13.22875 | -61.77737 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8f2f7120-3dd7-36ce-a3d4-e14e21794db3 | -13.24205 | -61.72408 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 613b4394-d9b0-3e86-b19b-6b7888783a24 | -13.21622 | -61.78537 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12f02f68-5381-371b-a630-b731c0cb447c | -13.22675 | -61.73734 | 2026-09-07 06:10:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 60b6d300-28d0-3c60-b4d8-102dc888f6c2 | -13.3203 | -45.2177 | 2026-09-07 06:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 268.1 |
| a91dcd01-27fe-3051-8891-d5bdd00e54eb | -13.3198 | -45.2409 | 2026-09-07 06:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 195.5 |


[Clique aqui para ver as próximas entradas](README37.md)
