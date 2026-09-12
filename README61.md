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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40d21f33-275a-3f40-ac91-0dc63de712d3 | -11.2833 | -44.1868 | 2026-09-12 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 8d44e64f-efd2-3d58-90dc-ec2ba6247bcf | -10.2171 | -45.2799 | 2026-09-12 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 9f6ee5bc-fa3a-3127-960e-d5a55ad94b50 | -11.5026 | -50.7272 | 2026-09-12 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| df106b3a-b352-30ee-8e77-b00c3032019a | -6.6021 | -58.849 | 2026-09-12 14:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 09831290-ee65-364d-8657-807352ebe09b | -11.4218 | -43.9321 | 2026-09-12 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 353.2 |
| adbae9a2-6fb3-30ff-96d9-d901df235685 | -10.2206 | -50.373 | 2026-09-12 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 7bc80804-8455-39ab-b2b9-d974c62c0637 | -7.61 | -46.08 | 2026-09-12 14:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a6e122e6-f7ed-3c4e-95d3-b9087c4a6c31 | -7.0 | -44.57 | 2026-09-12 14:15:00 | MSG-03 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8adb5dd8-7965-3352-b4de-c13f777862a5 | -7.61 | -46.13 | 2026-09-12 14:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9b27690c-b507-3917-a52b-81ce38798448 | -11.3723 | -46.8299 | 2026-09-12 14:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 205.1 |
| 134f5537-c2f7-3c32-9f1b-43b3d0c95afc | -6.2429 | -51.6939 | 2026-09-12 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 55d40d59-6908-3b1d-9dde-15e9575324ff | -7.12 | -42.107 | 2026-09-12 14:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 99.6 |
| 2c233d24-3668-3a67-a2ca-efb4e03f0336 | -8.8132 | -46.9495 | 2026-09-12 14:20:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| ff9a6ecd-bc16-3215-b545-807f6f80b3d5 | -11.383 | -43.9614 | 2026-09-12 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 132.3 |
| e8dbc29f-615a-31dc-b181-7fd3d059ece6 | -10.6827 | -54.1679 | 2026-09-12 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 247.0 |
| 58074acb-87fb-343b-9265-017a73b83142 | -11.4021 | -43.9585 | 2026-09-12 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 155.4 |
| 114c002c-88ac-33c8-a6ac-8575e5f131ff | -6.2243 | -51.6949 | 2026-09-12 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| c11cb776-125e-347f-a11b-3dd01f0bc96d | -11.8193 | -46.3633 | 2026-09-12 14:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| c94df58b-0571-3f17-9262-d10aa0952ba8 | -4.9335 | -42.8813 | 2026-09-12 14:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 133.6 |
| defb5eee-220f-34c8-b438-2be87eaa0a86 | -10.2735 | -45.3185 | 2026-09-12 14:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 99.5 |
| a363a1d7-175b-3501-bcce-9f35db01d5d9 | -8.2203 | -55.2427 | 2026-09-12 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 4c175823-0d3f-3275-9940-e1ba2333df49 | -11.4213 | -43.9556 | 2026-09-12 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 0bdb9cb4-c1b8-3875-aa81-6edb0e2f50f5 | -2.6785 | -57.5115 | 2026-09-12 14:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| df78eedc-f88b-3f5a-90d1-b4bf7e9f20af | -11.3825 | -43.9849 | 2026-09-12 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 0fa73ded-e8f5-35ce-a85a-45f6b077e299 | -13.3384 | -51.6602 | 2026-09-12 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 804515bb-d22f-341b-ae65-10dc239e393c | -12.1579 | -48.9647 | 2026-09-12 14:20:00 | GOES-19 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 0600daa1-268b-3c7d-b0d3-153c99b9ad89 | -11.4026 | -43.935 | 2026-09-12 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 261.2 |
| 71bbf91a-a54f-33bb-a3ad-df8ddeffa99e | -6.5004 | -47.5909 | 2026-09-12 14:20:00 | GOES-19 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 354b06e7-5ed6-35b0-9420-987574a57b8d | -6.8755 | -47.4313 | 2026-09-12 14:20:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 0255ff07-b9e5-393e-b85d-6e8dc6d5fff0 | -6.7648 | -59.4408 | 2026-09-12 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 2b60e767-cdd6-39a9-a24f-7fefc8e4674f | -14.5912 | -52.6673 | 2026-09-12 14:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 167.9 |
| 4323fc39-600b-3ffe-9d78-101c9dff8c63 | -11.0839 | -50.8368 | 2026-09-12 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 91f23d43-043b-35b2-adc9-f2c3e0ed5ad5 | -11.2833 | -44.1868 | 2026-09-12 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 323.2 |
| 2a248f6d-19dc-31ab-9b41-7a2486d90b2d | -2.7331 | -57.6271 | 2026-09-12 14:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| b6b633f0-8e8c-354b-b6cf-dab5b223a101 | -10.9491 | -48.3474 | 2026-09-12 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| ed92b839-0288-3c94-8e07-9adfe0905667 | -11.1032 | -50.8135 | 2026-09-12 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.0 |
| a5ba5778-55a9-3c91-9b00-d95d1e54b19c | -13.3953 | -51.6956 | 2026-09-12 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 25c9d09b-7a2e-3027-a186-9fa42bbb91bc | -11.4836 | -50.7293 | 2026-09-12 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 42a588ae-53ec-3c3c-8017-1ce8f0672b55 | -13.3761 | -51.698 | 2026-09-12 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 174.4 |
| 7221c603-b978-3123-977a-b3fc874586cb | -10.2206 | -50.373 | 2026-09-12 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 7f2cd3f9-7ea2-3829-b3cc-8c9274d81ba8 | -8.043 | -43.7565 | 2026-09-12 14:20:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 121.7 |
| 30056624-d834-3169-82f0-0b2691bd2cfc | -7.0166 | -44.6184 | 2026-09-12 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 352.8 |
| 9a622cd5-ab76-3cc7-8e65-7f12cd725ba8 | -6.8567 | -47.4328 | 2026-09-12 14:20:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 53c83cb1-5f61-38e6-9587-0e4eecdea79f | -10.6829 | -54.1475 | 2026-09-12 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 68f344ee-92fe-3d3d-b1be-586375b9b241 | -11.4218 | -43.9321 | 2026-09-12 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 310.8 |
| eac405cb-2aa4-34bd-96aa-515a19b2f3bc | -9.7141 | -43.3956 | 2026-09-12 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 90.9 |
| b514216b-7b8d-3595-ae65-2e140341df03 | -11.3513 | -45.7922 | 2026-09-12 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 155.6 |
| 1871fcff-236a-304c-8e23-dcc3184c157c | -13.3192 | -51.6626 | 2026-09-12 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 95bea0e1-355f-33cf-b478-f7b0f8b0e86e | -7.9645 | -43.9971 | 2026-09-12 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 95.6 |
| bcb70870-f52b-3c31-bdd6-dd93779c4652 | -12.1388 | -48.9672 | 2026-09-12 14:20:00 | GOES-19 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 139.2 |
| e7634602-4421-34c3-b93d-9e4aa523bf90 | -9.6951 | -43.3981 | 2026-09-12 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 86.6 |
| 2036889d-63e7-357e-80f0-8f0aad9101f8 | -7.6008 | -46.1288 | 2026-09-12 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 289.1 |
| 3d137641-4fb0-3750-9574-67c7a1493814 | -7.2147 | -43.7001 | 2026-09-12 14:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 107.5 |
| df02a211-2043-3f5f-970f-4685c0c0b34a | -10.7018 | -54.1458 | 2026-09-12 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| b20cb1a9-d40f-3986-ae2d-9af3d3880c82 | -7.2147 | -43.7001 | 2026-09-12 14:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 252.6 |
| abc08983-17e0-39d8-8794-d1db7a2c5e69 | -13.3953 | -51.6956 | 2026-09-12 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 7b50fa8a-26ec-3387-ab81-d7b43b548421 | -6.2429 | -51.6939 | 2026-09-12 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| b3acbd3e-5322-3858-b9bd-22b75aeb951a | -10.5664 | -51.356 | 2026-09-12 14:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 139.5 |
| 7637edd2-0713-3a6b-a112-517cc9c336dc | -7.0166 | -44.6184 | 2026-09-12 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 328.2 |
| 839f3205-a01c-3a8d-b4e1-ffca6d3dba20 | -7.6008 | -46.1288 | 2026-09-12 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 09be6a55-8563-3a99-8edf-3edb264d11b1 | -10.2743 | -45.2726 | 2026-09-12 14:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 7a53934e-a83e-31f6-b0fe-905ab6ae82db | -2.7149 | -57.608 | 2026-09-12 14:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| d88ad4f1-9ac3-3eb4-b0b3-8770d10326c7 | -10.2933 | -45.2702 | 2026-09-12 14:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 398.4 |
| c69a2a8f-6f1b-3e3e-8635-a447277d7843 | -11.383 | -43.9614 | 2026-09-12 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 177.5 |
| 63ad7f5c-2c2e-3ed1-96b9-ea4f1eabdb22 | -8.7943 | -46.9514 | 2026-09-12 14:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| e59576ff-7b47-35a4-8dc1-a2e9126e949f | -11.0839 | -50.8368 | 2026-09-12 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 5718a8b1-5271-35f5-8a31-9b75264bb197 | -10.9491 | -48.3474 | 2026-09-12 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 721b73e4-5794-3f55-9907-d4b1de18016b | -2.9395 | -50.3994 | 2026-09-12 14:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 122.6 |
| f3d766d9-d0e7-33a3-8c2e-5b620a300b62 | -3.3504 | -59.4274 | 2026-09-12 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| f0b5a442-0edd-3587-b86f-ddbfbe9d650d | -10.6827 | -54.1679 | 2026-09-12 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 278.8 |
| 2a9875f1-9d8a-3450-84d7-2d958e2f18ed | -10.6413 | -46.1133 | 2026-09-12 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 222.5 |
| a50ede14-7060-3f76-a2da-d2dc78f99802 | -8.8132 | -46.9495 | 2026-09-12 14:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 5d77debe-1707-3f2b-9f1c-60a956f7a804 | -2.7331 | -57.6465 | 2026-09-12 14:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 4d1f4aaf-9615-357a-be00-8b77f7d708b6 | -2.7331 | -57.6271 | 2026-09-12 14:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 8bd693c6-da91-36df-80fb-faf0089f16ff | -10.2206 | -50.373 | 2026-09-12 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 152.4 |
| ad8dcb1d-602e-366d-b57d-66f1d0d8fbad | -9.6755 | -46.0047 | 2026-09-12 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 979eb766-6909-34ee-b04f-8f30d420613b | -11.3731 | -46.7849 | 2026-09-12 14:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 462e904e-db7f-32d5-a299-95c8c7bffc00 | -2.6785 | -57.5115 | 2026-09-12 14:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 672d8d66-150b-3279-b6eb-b56a230fbf13 | -6.5004 | -47.5909 | 2026-09-12 14:30:00 | GOES-19 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 605da9b8-4cac-3196-b8b2-c44ab7f7e847 | -11.4026 | -43.935 | 2026-09-12 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 282.2 |
| 887f4173-e3ef-346b-af48-3305f2ea58b5 | -10.5475 | -51.3578 | 2026-09-12 14:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 101.0 |
| ca26db38-4fef-3bde-8fe8-729931e61342 | -11.4213 | -43.9556 | 2026-09-12 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 153.3 |
| 89af3ba7-8594-335f-a5e4-aa8ccfa544b5 | -12.1388 | -48.9672 | 2026-09-12 14:30:00 | GOES-19 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 8a2ef989-8b6f-36bf-876d-eab01c68e672 | -11.3825 | -43.9849 | 2026-09-12 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 172.8 |
| 79a82dbc-4149-33f4-b794-5e3696bad00d | -8.2203 | -55.2427 | 2026-09-12 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| dd425475-324c-3316-b4f1-c17a46f90e33 | -5.1254 | -55.9748 | 2026-09-12 14:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 172ba965-5137-3a41-8d6d-0c2a1b52bb05 | -11.4021 | -43.9585 | 2026-09-12 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 204.8 |
| 26b0307e-a8cf-33d2-90a3-54c1f22a8563 | -13.3761 | -51.698 | 2026-09-12 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 0462805c-51b5-39d8-ad6b-aac35f0130f5 | -8.5417 | -54.6985 | 2026-09-12 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 1036ec0a-ccc8-38fb-9c13-e152c22d46c6 | -6.8567 | -47.4328 | 2026-09-12 14:30:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| d8e94a40-4796-36db-b251-760b67b3cfcb | -10.6829 | -54.1475 | 2026-09-12 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 169.7 |
| f21d6418-2454-3e15-b2c5-0cee6bd0e780 | -11.2833 | -44.1868 | 2026-09-12 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 179.5 |
| b522a4af-4668-30cd-88dd-2280254380ba | -6.8755 | -47.4313 | 2026-09-12 14:30:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 4db23308-b7df-3b46-8f27-f8c5d27e3ff6 | -7.2571 | -46.6941 | 2026-09-12 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| d74c490b-732d-3c2d-8093-6f5f2cc94e8a | -8.5801 | -54.5747 | 2026-09-12 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| b7ca9e9f-d11e-3b21-82a6-abafb7ff2b7b | -10.2735 | -45.3185 | 2026-09-12 14:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 9383c35e-340e-34e2-a569-2dc35fea7367 | -10.2171 | -45.2799 | 2026-09-12 14:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 4fbdfdaf-fc41-379a-9877-3b001a8041cf | -13.3192 | -51.6626 | 2026-09-12 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 101.3 |
| d541c88e-3c58-39fb-b399-ab78f795cef7 | -8.9913 | -44.8771 | 2026-09-12 14:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 8365f9c0-c1d8-3255-8c68-cbb0a4764215 | -10.7018 | -54.1458 | 2026-09-12 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |


[Clique aqui para ver as próximas entradas](README62.md)
