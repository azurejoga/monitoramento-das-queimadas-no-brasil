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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 780a3895-bc0d-3017-912b-25a8e2fc6878 | -3.0586 | -54.201302 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fa606bc-42cf-3d3f-b281-147d9410659e | -1.5079 | -54.82 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f23d085-f740-340f-b446-fcc8b3f92f62 | -6.3919 | -52.716 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1e1e247-f79b-37bc-b3a6-f83643147e16 | -2.5 | -56.063801 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 210bc89a-8bff-3d13-9441-4af6984c9fac | -1.2668 | -55.3951 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f644f79-6350-304d-8c71-12ac72279d06 | -3.7371 | -57.125198 | 2026-10-08 00:26:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b92e63c3-e380-3ea2-a04d-7887be8f3e5a | 3.6572 | -60.3936 | 2026-10-08 00:26:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3850b070-b588-3e37-b032-59949d0e3807 | -6.3933 | -55.187801 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61d43f7c-b303-3aea-905f-5e8717cdddeb | -2.5162 | -57.235298 | 2026-10-08 00:26:00 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 63d60211-6077-3dfe-878d-d4956d71d406 | -3.0274 | -54.0634 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 002829af-ddb5-355a-906a-b34af823f791 | -3.295 | -54.0616 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d81b0f8-dd2c-3bca-9d14-faa8f22d520e | -7.1384 | -46.521301 | 2026-10-08 00:26:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 576b7002-1843-3db7-879d-c61d1b47df7b | -6.9224 | -49.619598 | 2026-10-08 00:26:00 | METOP-B | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba525fd4-1ffc-33e2-882a-d68cc0f1e840 | -3.5471 | -54.674198 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4ba97b0-84b2-3fc9-98d9-02db5c042400 | -2.7326 | -57.6036 | 2026-10-08 00:26:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ea96eb42-86bf-37c2-bf88-20c7cfb62e13 | -3.234 | -57.867599 | 2026-10-08 00:26:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3a1a4c2e-ec7f-328b-af5d-349f944e8b40 | -3.0351 | -53.916 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4367d451-ca26-3860-a2e7-59c0cfef8a90 | -6.0956 | -53.498901 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47b20699-4dc8-38ed-83b2-34bcaf846c60 | -10.6274 | -53.855202 | 2026-10-08 00:26:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9814787a-cd92-3e13-9c66-1be0949c81e9 | -3.8738 | -55.987499 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e0781c3-01b0-3349-94fd-6ce50329c034 | -2.4671 | -56.1003 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7492c4a5-0eb0-3af6-aa14-f155d6c02e7a | -11.0057 | -45.447498 | 2026-10-08 00:26:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 76013284-7a0a-3d43-9313-a91c9e549b3f | -4.3006 | -60.9314 | 2026-10-08 00:26:00 | METOP-B | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7fb98dd3-7e04-371b-879d-0cf22a0ea2d3 | -4.0607 | -54.028 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 143814b4-10f7-35cb-b42b-716b52444b89 | -3.1129 | -53.7593 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e47f9ec-9413-3f67-9782-0f8e9d412006 | -3.0758 | -54.276901 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fd0b6f1-682a-3e42-8742-53b840ab76e1 | -2.9598 | -54.129299 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 463592de-8cfd-3e10-8108-cdaabde79444 | -2.4847 | -56.1329 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0149042b-7931-3f74-a708-9abc8ac1e24d | -15.4149 | -43.692402 | 2026-10-08 00:26:00 | METOP-B | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| b73b5648-94a5-3a2d-acb9-24e88fdc7335 | -3.1545 | -54.078499 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| affc8293-bafb-34a7-8991-aff699a24674 | -3.226 | -57.8778 | 2026-10-08 00:26:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b07d091c-afee-3380-853e-84f10896b7d3 | -1.7197 | -55.437401 | 2026-10-08 00:26:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb2e6871-b531-3789-8c0c-0320eb4f6c17 | -3.4815 | -59.582199 | 2026-10-08 00:26:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6dd7053c-cf0a-300b-8d93-dffe00ff7f7b | -6.2153 | -52.846001 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f98518f-5b6c-3234-8221-6bd560caccf1 | 4.283 | -61.029499 | 2026-10-08 00:26:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 73daafa4-8b57-34d7-bbf6-271cc1b5a70b | -1.5306 | -54.556099 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0dc35b03-5a6c-32ca-a4dd-ab6e51c86d7d | -5.8887 | -57.741699 | 2026-10-08 00:26:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e744b596-92e0-30c4-83f8-b1dddddfdf09 | -3.0332 | -53.9529 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da2af2f6-7e41-3f9d-ae2d-17d7295c2f29 | -6.8331 | -55.266998 | 2026-10-08 00:26:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1155089a-9031-3650-89bc-56f80099ca32 | -2.9562 | -54.1591 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f7fa0dc-f2e4-3805-a3bf-13d193bc17f4 | -4.0585 | -59.827202 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2e76ebe8-69b8-3b1a-a5bf-91745396576f | -3.2318 | -54.328499 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c93fb17-3c22-3b47-bab5-69659c0ecdf7 | -5.3713 | -56.053001 | 2026-10-08 00:26:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44196b5b-0f7e-30f6-8a37-8c7d2161c490 | -2.4914 | -56.116798 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a8b5ed6-af9e-32da-a637-672358c20291 | -9.8172 | -44.785099 | 2026-10-08 00:26:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 333a344f-bde6-36d2-ac59-999486774099 | -3.5495 | -50.091801 | 2026-10-08 00:26:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e070e162-c009-3174-a259-e58e6cf84ce7 | -13.2992 | -48.681702 | 2026-10-08 00:26:00 | METOP-B | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fb1be403-b2e6-3567-8584-3a2fc8ea7120 | 1.7791 | -55.556702 | 2026-10-08 00:26:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3e6cfb0-c782-3e93-bec3-a767eaf0d37f | 1.8615 | -55.739601 | 2026-10-08 00:26:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 965edc1b-f418-3e74-a1bd-b906f6a258a5 | -3.0987 | -53.923698 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f30574c2-8dc4-3a7e-be9a-3d2659194b19 | -4.5691 | -54.955101 | 2026-10-08 00:26:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53d4582c-b70b-37cd-bc14-4a17a0a9f1e4 | -4.0522 | -55.3144 | 2026-10-08 00:26:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9ab8efb-e5ed-37b1-a4d6-12321d445061 | -3.567 | -59.4585 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 72b7b03f-149d-3e7a-b8e3-646394121a7e | -1.328 | -56.396 | 2026-10-08 00:26:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c154706-3435-36f6-b8be-a3347c5c12e2 | -5.1102 | -47.108398 | 2026-10-08 00:26:00 | METOP-B | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cdcc1ca0-26b3-3c06-8236-9bb4743d997e | -7.2135 | -55.079498 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a55f4f83-5e71-3aae-91b3-cc764bea600e | -2.7793 | -54.0606 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8becc9b-63c8-364d-bc2e-01625cc8ac9e | -2.045 | -56.376701 | 2026-10-08 00:26:00 | METOP-B | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0258048d-5c78-3ca9-82ad-9804c5b49a46 | -4.1195 | -54.014801 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 840c443e-6b71-35f9-9919-7f4d473d379d | -2.9143 | -54.110401 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15d0d546-da37-32d5-b207-9d1299814862 | -6.3367 | -55.303101 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36a55f32-07d4-3839-ae34-a2e8e00010e6 | -2.7706 | -54.1134 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5207627e-7153-35cc-8e8b-e3e4df8401bc | -3.0367 | -53.923 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 911a15c7-4529-3b26-810f-56c4d52b1821 | -2.4961 | -56.137699 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8f82e4d-b766-3722-b90b-ba31b05ff00f | -10.4262 | -47.274101 | 2026-10-08 00:26:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 455d368b-2dcc-3fd4-999f-891a00c360ac | -2.941 | -54.046398 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26012526-753d-3995-bab4-1d4e478c7041 | -6.8963 | -55.551102 | 2026-10-08 00:26:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 689dc0c5-a8f2-3553-a608-4ef6414cbff4 | 1.9834 | -59.9212 | 2026-10-08 00:26:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 994ab531-294f-3ef4-afde-ffc36b69efdc | -4.0609 | -59.837799 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 08fb9a31-e1ff-3ed9-b179-be9ade5f9d2c | -0.8419 | -51.8409 | 2026-10-08 00:26:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| a9cfd5ac-e960-3d9f-9c7c-7d3d90548eb1 | -7.3952 | -55.202 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bddff04-4fa9-3b01-bc2b-ce517cee7e57 | -6.6265 | -43.705502 | 2026-10-08 00:26:00 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c0721f2e-6801-31b1-a278-ba40f6e52787 | -3.2653 | -54.249001 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40133524-5c05-37b4-b7ca-f8d9384b87ab | -6.2397 | -52.8629 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 150299da-f267-3709-9e1e-35a31dd4c5f8 | -2.8244 | -57.5998 | 2026-10-08 00:26:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7606f2b2-f8a5-30ed-af42-a42d2ed2b402 | -5.99 | -55.365101 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f775c25-8c27-370b-94ee-c21a5871c7a6 | -3.3016 | -53.863701 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e136ca4-d16d-30cc-81d5-f421e361fa8f | -4.1573 | -55.139999 | 2026-10-08 00:26:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e734756-81f9-3609-9d6b-6f1b46ceae49 | -7.8948 | -54.9949 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 600a9691-48bb-306f-b806-18ab2f84aded | -3.2329 | -53.879101 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f97f16d-3894-3162-93b5-c7edf27b887b | -1.8232 | -55.0289 | 2026-10-08 00:26:00 | METOP-B | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08d4fd08-4bfb-398a-a212-9b5b4ec05bd6 | -3.03 | -53.938999 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ecdbd6c-3c7f-347a-8ee4-58d141a0fccc | -3.1765 | -50.4375 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f757b67a-6a9e-3af0-850c-670aabcd4d06 | -5.2545 | -45.4104 | 2026-10-08 00:26:00 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e983a95f-86c2-3a54-b1b5-02b1d485bdc4 | -3.0241 | -53.867298 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 713f82c5-a3ec-33bd-9525-3f6062fc92ba | -4.566 | -54.941502 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3e981a9-cb95-3b43-a6c9-01a7a72bb0d6 | -3.014 | -54.095402 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acdaad3e-9a4f-3afe-881c-d033032a7328 | -3.313 | -53.8685 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f55f01fe-207f-3f0f-b92f-6c9373e93488 | -14.5891 | -54.343102 | 2026-10-08 00:26:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eaa60c42-4a03-358e-a9b7-f22fd0b3cd66 | -2.9645 | -54.150002 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8ba7c65-d741-3df9-b42c-1132ea692c40 | -2.9896 | -54.079102 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ee1ee02-7d6d-3b38-8e0d-7cebba8d04fe | -2.9947 | -54.056099 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8de763b2-086c-3b27-8bbb-4ebd5e5e602e | -3.3114 | -53.8615 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 628ed89f-2c0b-37bb-b32f-3b4cfad3efde | -2.1215 | -54.798199 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a627cc2f-48af-38b4-893c-4bf84fe5b2b2 | -2.5629 | -50.678799 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6351c786-5114-329b-8ddf-3752b990536e | -4.6059 | -55.715302 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ead0ad8-8fbd-39d0-b498-cda13854ce1c | -1.5223 | -54.838299 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e77d36df-13b6-3a1a-8ef7-1fa0ec6da938 | -2.9629 | -54.143101 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de273bb9-1b19-3ef8-a01e-0a4eb275c65b | -5.2387 | -56.104801 | 2026-10-08 00:26:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 772f7da1-dff0-31cc-83dc-d21a54dd4841 | -3.0535 | -54.224098 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README17.md)
