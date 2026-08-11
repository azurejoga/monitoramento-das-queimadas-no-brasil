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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ff902a0-8094-3326-ae37-e573c40ed503 | -11.17479 | -54.80492 | 2026-08-11 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50798433-cd40-392e-a2a3-92fee7c165da | -12.48799 | -45.28989 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 154cbdbf-043f-3dca-a0f3-518a3bfc64b9 | -13.56946 | -46.28131 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0fbc55c5-9b68-3847-8ed8-05abf263d9b5 | -11.46702 | -46.62262 | 2026-08-11 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5833b9b2-6bd1-3f51-adb4-447f4cfc84dc | -12.48572 | -45.30658 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6d521641-2503-31ff-8f66-16c519346c4a | -9.13383 | -50.89874 | 2026-08-11 05:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89d7a4bc-290b-3d3f-bda4-6ec25779a96e | -12.48898 | -45.28148 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 522fa31e-1397-37d5-87db-453184e3ae2d | -12.45472 | -45.32303 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bcbce9e4-cae9-3c2d-a4a3-f3bbab3d2d80 | -13.57497 | -46.28202 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e78513f2-b688-3e77-9793-cc613dc30569 | -11.22255 | -54.8489 | 2026-08-11 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8987921-42f0-3ad0-afbf-59969bf5ffe4 | -11.2163 | -54.03535 | 2026-08-11 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a74e75cd-67a8-303c-b6fd-a8a0753e2df7 | -13.57075 | -46.27042 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a77f2441-7b89-3906-84d4-cf3873c8f80c | -10.89349 | -50.3703 | 2026-08-11 05:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cf7e9a81-281f-3392-a392-d89af053fe9b | -11.24254 | -54.87382 | 2026-08-11 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73bf8527-1a54-3f0b-aa30-4406a9706714 | -12.45567 | -45.31482 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9a353b54-c99f-3115-a51c-5ee40617c7dd | -11.9549 | -46.33607 | 2026-08-11 05:10:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d7c42e0-2e48-3b46-a4c9-235c6c294d0a | -7.23084 | -43.48184 | 2026-08-11 05:10:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b0d6e835-6d81-3e21-8d8a-f265db0f116c | -10.86546 | -50.24923 | 2026-08-11 05:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c54c2f8-30a1-3e15-886e-1d4b4072e0be | -11.49378 | -54.60763 | 2026-08-11 05:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f2b8e5d-2aed-3d8e-b290-9f0c088cfe73 | -8.89399 | -60.58619 | 2026-08-11 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 976c465e-e127-30a6-98ad-88fc120031ad | -12.2387 | -47.30222 | 2026-08-11 05:10:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f79d4adc-4165-3404-9489-e83cd056bd26 | -13.57454 | -46.28566 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 68a62ee2-02df-3c63-ae41-34e1604bb609 | -11.49044 | -54.6071 | 2026-08-11 05:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb484fb3-0303-310d-81f2-17ec9b5be99e | -13.48204 | -43.07672 | 2026-08-11 05:10:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d9160015-9938-3633-8b0d-0b98d8fee79d | -8.89776 | -60.59031 | 2026-08-11 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 935e82fc-8f57-39ce-aaf8-2e44c5e040aa | -9.47383 | -60.51568 | 2026-08-11 05:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0df00cc-630e-3f0f-9f4e-494412032be6 | -13.62156 | -46.22168 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eee07366-6f50-354c-abd6-5724e8ef4a8d | -9.37062 | -57.36258 | 2026-08-11 05:10:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48068bfa-967a-3942-96d5-a409aafedc6b | -6.7195 | -58.93402 | 2026-08-11 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 786097fd-d696-3a61-b35d-06fb5e1afb9c | -11.19203 | -54.8476 | 2026-08-11 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3223e25-e304-3724-900b-d826fb67384e | -12.48009 | -45.35173 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a58e146d-4698-3a71-8390-fb022c372110 | -8.95887 | -60.53736 | 2026-08-11 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 68e7a7b8-d969-369f-b4cb-dba3479b74f2 | -10.22176 | -45.79642 | 2026-08-11 05:10:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 887b9481-5a5e-3b4e-b139-5a5e2c427c08 | -10.41099 | -46.68115 | 2026-08-11 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 09257d30-3b91-318e-82c2-a4a5cb713119 | -11.19425 | -54.85522 | 2026-08-11 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be005b4e-e02f-393d-85ab-2eb0ea893db8 | -11.45382 | -46.68118 | 2026-08-11 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 37133c04-87e3-3f65-9f89-7847480ce799 | -9.39539 | -47.46511 | 2026-08-11 05:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 03f049f4-9e7b-395b-a077-d675d2634e66 | -6.70834 | -58.9524 | 2026-08-11 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5cb8a34-5535-32d2-bda4-f85463fde796 | -13.58996 | -46.25052 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4804ed91-0d42-373e-9076-3c8a2199022b | -8.23471 | -46.24831 | 2026-08-11 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9badcf98-ec19-3920-bdb9-5a6e23197005 | -10.11167 | -46.20214 | 2026-08-11 05:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eafaf8df-bf06-319c-ba99-055d5a649076 | -10.41614 | -46.68183 | 2026-08-11 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e0774bf0-0fb3-36de-b192-2a904e644158 | -9.47464 | -60.53531 | 2026-08-11 05:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4aa62989-3799-372e-9df5-0b7f84cd37b4 | -8.89356 | -60.58956 | 2026-08-11 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dcc15ef1-a66a-33e9-8ef4-f986c9e2f22b | -8.24107 | -46.24004 | 2026-08-11 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f9d30d6c-f486-3919-abb6-b80661788acc | -11.45903 | -46.68196 | 2026-08-11 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 1c02247e-4c8a-3a1d-a5af-73aa321a8033 | -9.21976 | -51.53968 | 2026-08-11 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a3209c2-2052-33bc-bff1-5e02368751e2 | -10.86498 | -50.24925 | 2026-08-11 05:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab936d0f-e1cf-3993-8aa4-5d5117bf6ede | -7.39914 | -59.99871 | 2026-08-11 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee151ee1-1331-3e5c-8f0c-5349668ca2eb | -12.48832 | -45.28566 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b484b5d7-26e5-38f5-92f6-ebbec936d053 | -11.23365 | -54.84341 | 2026-08-11 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c3628f6-0f05-3f3a-9659-13d9ecf58c53 | -11.46309 | -46.65408 | 2026-08-11 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e1bcfda-4a5f-3c68-a229-8feefac5f678 | -9.38148 | -47.49496 | 2026-08-11 05:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 6aa179a6-b3b6-36a8-b627-18f0248629d9 | -9.47531 | -60.53151 | 2026-08-11 05:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f91b1664-ca08-3293-ac25-9668204a2310 | -8.29459 | -46.40498 | 2026-08-11 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b7c776c1-45d5-3947-8dd9-815df98e00d2 | -7.72062 | -46.22371 | 2026-08-11 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 91265382-698b-3b71-9b9f-2d3fc25d39c6 | -9.72057 | -60.20385 | 2026-08-11 05:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 13be4d3f-f606-3294-97aa-aa40d848b86f | -12.48676 | -45.29825 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6045182d-4ebb-3f23-9135-076ab333b44d | -11.47754 | -46.62374 | 2026-08-11 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e5d9d7be-0c09-3ee6-ac39-0a598407de9b | -13.59598 | -46.24719 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e6a458ae-90f9-3968-9884-9b41f1b71081 | -11.45944 | -46.67885 | 2026-08-11 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 01348c2c-e174-3a66-b35f-5830199f976a | -12.48624 | -45.30242 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6459e5bc-1a30-3176-bd29-970b708ad80a | -10.27888 | -60.53852 | 2026-08-11 05:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3941b2ee-74ad-3bfc-bd43-d037b03626cd | -10.11122 | -46.20553 | 2026-08-11 05:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2e484ea-6cd3-3a15-abaf-e30363263263 | -11.22533 | -54.85297 | 2026-08-11 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bed8f144-fd4f-3818-b27d-dfc6ea997aa4 | -11.46568 | -44.56337 | 2026-08-11 05:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0696e5b5-d60c-3682-81cc-dc334321ecfb | -11.23254 | -54.85049 | 2026-08-11 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69e79610-9790-3f58-b5cf-a10c832c3c24 | -11.45465 | -46.67495 | 2026-08-11 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9ec3487c-0372-3277-981a-8fc326974679 | -11.2492 | -54.83138 | 2026-08-11 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75fcc8b4-b1e5-3bbb-90fe-6b956ce7e06f | -8.95685 | -60.54895 | 2026-08-11 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 82fd1ee1-87fc-3fe7-8461-812a299ddd41 | -11.92577 | -55.90171 | 2026-08-11 05:10:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c56cd761-af8c-311e-8898-41c73e4a243f | -11.02371 | -45.64941 | 2026-08-11 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 83fdec1f-2283-3d87-ade6-f869420ba984 | -12.45853 | -45.33625 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b13bdd08-dd40-32e8-80d5-6cb01a15ec5e | -11.61204 | -54.65178 | 2026-08-11 05:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9360dbe-6a32-362f-82b3-9cbde0cb080b | -10.41534 | -46.68796 | 2026-08-11 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 69e99f25-dbc3-34df-81cc-f95a3319f4a9 | -13.56902 | -46.28492 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 41af6ec1-01b5-3458-9bda-e3ca02b70548 | -10.42108 | -46.64382 | 2026-08-11 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97e90eb6-37ef-3f68-9a89-b7ca4896d607 | -10.73423 | -47.91357 | 2026-08-11 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5da03a49-d9fd-3cce-b289-21e222bcb274 | -11.22532 | -54.8312 | 2026-08-11 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 766fa917-e479-3f36-8dbf-9b429cb0cb1a | -10.94017 | -57.17681 | 2026-08-11 05:10:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1673ae5c-0837-364f-94f7-f412cc19d8eb | -8.95401 | -60.54052 | 2026-08-11 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 06c433d2-1cfd-3c87-a9ff-2591b7765962 | -13.56179 | -46.29863 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 77790a65-0515-34ad-9c1d-39a78b5f29c9 | -8.53363 | -49.69229 | 2026-08-11 05:10:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c24aae6a-0612-309f-a249-a8bca44ba532 | -8.30161 | -46.39128 | 2026-08-11 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee4febb6-85ff-304b-8f5b-6ce01f2c279e | -11.17534 | -54.80138 | 2026-08-11 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23c1bb4c-883f-3946-969e-a3ed0add2766 | -12.45662 | -45.30655 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e00af11f-7b0c-3a7d-87e8-8b7060b43ee2 | -11.45997 | -46.67906 | 2026-08-11 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f1a7a83d-8d63-36ce-846d-8a7c16df73a3 | -8.95468 | -60.53665 | 2026-08-11 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9c36175e-a460-364f-96dd-662a6f47d952 | -8.89982 | -60.57872 | 2026-08-11 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30729ff1-3ceb-3d62-bda1-14e5c8aa973c | -11.65334 | -51.64585 | 2026-08-11 05:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7ab753ad-fbef-3449-a6f5-bdc7ab9635e6 | -11.4582 | -46.68818 | 2026-08-11 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 32.8 |
| a95c2c23-1405-3213-a430-dd800a6b5270 | -13.62115 | -46.22501 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0f8c24db-e888-3952-8c04-f97d98d74201 | -10.71134 | -47.90405 | 2026-08-11 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7311a22f-d5e6-3a81-929e-d1f3259423e6 | -8.30747 | -46.38626 | 2026-08-11 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 24fb2098-7adb-3103-ae91-cca1f5e379d1 | -6.42754 | -54.71626 | 2026-08-11 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f03f029c-9661-3d66-ab6c-6bd704e723d4 | -9.24923 | -60.3311 | 2026-08-11 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9be9279b-b0de-3c11-9477-3dec2dc650c9 | -12.48602 | -45.30664 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b6d99ed1-76af-3b68-ab27-9c338c9c9c45 | -11.48321 | -46.62099 | 2026-08-11 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4fad101b-9101-3f4f-ad8d-1657f2fed229 | -11.95561 | -46.33031 | 2026-08-11 05:10:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea25d839-aa77-3624-a950-52b936fcb9b0 | -10.11214 | -46.19868 | 2026-08-11 05:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README24.md)
