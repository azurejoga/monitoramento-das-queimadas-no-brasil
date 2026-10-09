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

## Dados Diários - Página 287

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1c00aa1-8e50-30e5-9d4c-df6fd277fb97 | -11.3103 | -44.8337 | 2026-10-09 18:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 341.9 |
| eada88ad-7b6d-3c78-b805-2d3f4b3b6a46 | -14.4339 | -43.9396 | 2026-10-09 18:00:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 403.6 |
| 3b808564-ecb4-3cb8-ae12-48e053a986fb | -13.1636 | -54.3591 | 2026-10-09 18:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 329.2 |
| c642ed19-7f7d-3c60-8c6c-513c981e0fd2 | -2.4806 | -56.0678 | 2026-10-09 18:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 899851a0-fa95-3bf3-bf23-0fe8b0359f57 | -3.571 | -59.0777 | 2026-10-09 18:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 9dc7646f-2646-3a3c-9fd1-05a8bd7fccdc | -12.208 | -43.9512 | 2026-10-09 18:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 116.6 |
| e9ed8923-7c4d-3863-9e83-2bac07c70805 | -9.9018 | -44.7917 | 2026-10-09 18:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 107.4 |
| e5f6b8bb-57d7-3bab-b379-d80302a96c95 | -2.4623 | -56.0682 | 2026-10-09 18:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| b30ca6fa-216a-35c3-8fd7-0cec67d2471d | -5.3645 | -42.851 | 2026-10-09 18:00:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 145.3 |
| ac6131af-978c-3fa2-ad26-3d49ca2279b4 | -12.2504 | -44.7631 | 2026-10-09 18:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 6f0652bf-ad91-339a-9862-01d8489f31a4 | -11.1876 | -45.3117 | 2026-10-09 18:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 7b312980-a3ff-3423-931e-5f2076c22f36 | -11.47 | -43.3824 | 2026-10-09 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 133.0 |
| c4727a27-9581-38f6-8656-64c141dd92ba | -2.5171 | -56.1262 | 2026-10-09 18:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 144b2e1a-3f23-35cc-bafc-1554357c8144 | -2.9173 | -57.2151 | 2026-10-09 18:00:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 6a4501a6-6ea4-3344-98fc-7b5527db1dc6 | -15.3832 | -41.9029 | 2026-10-09 18:00:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1005.9 |
| c491c9f3-1846-3f34-a788-f3f2a3fdadca | -11.037 | -44.0589 | 2026-10-09 18:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 744.9 |
| 76d30d02-b446-39ab-9790-cbdde07c847a | -3.5709 | -59.0969 | 2026-10-09 18:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 412828c8-51b2-39b5-bdab-67c56245168e | -3.1541 | -57.6772 | 2026-10-09 18:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 88e7ed39-0ed4-358e-b3ff-2da4fe5f8581 | -11.7943 | -46.7056 | 2026-10-09 18:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 175.2 |
| d9c26007-f37f-309f-bc2c-a312bca4c13d | -2.8997 | -56.9618 | 2026-10-09 18:00:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 38.0 |
| f6e176c5-3fdc-35f5-abb5-ed4bdc39c845 | -11.075 | -44.0768 | 2026-10-09 18:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 95.9 |
| c1ac0b7d-3c35-3600-82be-e02a57d7dd5f | -10.2317 | -46.8382 | 2026-10-09 18:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 202.4 |
| 0cd160ee-7b1f-367b-b5d1-056996478a0a | -12.2145 | -44.6291 | 2026-10-09 18:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 65f49f2c-5a42-3075-8cf4-3bea20cf0d2e | -2.572 | -56.1646 | 2026-10-09 18:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 81e9b05d-0756-31c8-8736-a62393dde847 | -10.4724 | -47.2333 | 2026-10-09 18:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 36ff91f9-d509-3fef-8039-f16bb5d1c41c | -8.9308 | -45.1584 | 2026-10-09 18:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 150.0 |
| 89316f56-ff6c-3334-8b11-50b9f79cb9e8 | -15.4029 | -41.8985 | 2026-10-09 18:00:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 509.2 |
| d5d5fa78-14be-399b-84eb-5b161d91f826 | -12.1952 | -44.6321 | 2026-10-09 18:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 307.9 |
| 12278e44-35bc-3f57-99e5-c3a5acbcb4f7 | -10.2486 | -49.6851 | 2026-10-09 18:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 5f1a472b-9715-3b71-9f66-816d76c8dd90 | -13.3671 | -43.8742 | 2026-10-09 18:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 225.2 |
| 30c1c937-b700-3c2a-90ac-2f72ad06adf3 | -9.9004 | -44.8839 | 2026-10-09 18:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| ac85dc88-a2f5-3a30-a353-e5ab6b8b3f88 | -14.0472 | -43.8222 | 2026-10-09 18:00:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 1e86e4fe-4fcd-3919-a2e2-a353f1e6c2cb | -12.214 | -44.6524 | 2026-10-09 18:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 02f6f2b1-4410-33ae-ada1-26293cdb9636 | -3.4607 | -59.2527 | 2026-10-09 18:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 77f59921-35ec-334a-b7b7-c9f9574d0a01 | -6.6027 | -37.8944 | 2026-10-09 18:00:00 | GOES-19 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 116.5 |
| a5b7059e-611c-3600-8f06-40b6f9c9e793 | -3.4278 | -58.0203 | 2026-10-09 18:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 7591c69e-1f8d-3ea7-ad17-dacffc1a256c | -7.0038 | -47.6843 | 2026-10-09 18:00:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 2995d0cc-4832-3dfd-85ea-b51c3d8c873d | -6.008 | -42.257 | 2026-10-09 18:00:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 103.8 |
| 90c07e66-aa7d-3351-b174-2df0d4ade81b | -11.9115 | -41.3812 | 2026-10-09 18:00:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 110.2 |
| 4d971793-6b2a-3ddf-b0e6-5bc5dfd9c393 | -11.5683 | -45.3959 | 2026-10-09 18:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 200b65c8-d06b-360e-8930-004f66067d23 | -15.0516 | -41.8024 | 2026-10-09 18:00:00 | GOES-19 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 136.1 |
| 6e93bcf0-78ec-38c2-a7b2-c52c6157ac9c | -9.9198 | -44.8585 | 2026-10-09 18:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 377.2 |
| 36dfdbab-a322-3f38-8961-87e271135246 | -7.4974 | -45.3041 | 2026-10-09 18:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| e1a9fea6-aa75-3420-8c19-a3667e429fed | -9.9194 | -44.8815 | 2026-10-09 18:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 370.4 |
| 65abb62c-b556-310e-8eb5-88579f547ede | -6.4611 | -45.7986 | 2026-10-09 18:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 161.9 |
| adf27f6b-abb6-3cc1-8257-a03d919abcdd | -11.055 | -44.1265 | 2026-10-09 18:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 61.9 |
| d4a36655-76fc-346e-8cba-87f2428b238b | -3.6435 | -59.3064 | 2026-10-09 18:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 042f7174-394c-3c34-858c-3c5c22e2fab1 | -1.2175 | -55.6512 | 2026-10-09 18:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 231.6 |
| 25be5900-39bb-3774-950d-ab6a5a55cf1f | -1.4487 | -48.9739 | 2026-10-09 18:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| ad1c79fc-b7a3-347f-9727-2c3477f056f6 | -12.3708 | -46.5789 | 2026-10-09 18:00:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 196.0 |
| 16777668-38b8-3247-98ef-66fa87277a6a | -11.014 | -45.4272 | 2026-10-09 18:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 508aba58-9372-3070-b4aa-4a3dd45f15a4 | -10.472 | -47.2556 | 2026-10-09 18:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 229.0 |
| 19db01a8-2a9f-38c0-a2cf-cd45ea288cce | -8.3014 | -45.7019 | 2026-10-09 18:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 4b8ea22e-afb8-3fbb-9df9-18abbcc810da | -3.5893 | -59.0773 | 2026-10-09 18:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 07fff3ab-2074-3376-829c-85c533ca087b | -12.1627 | -45.3547 | 2026-10-09 18:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 6bd2187d-d4be-3d3a-a27f-ca00cde0731d | -2.0403 | -56.3895 | 2026-10-09 18:00:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| ee6cd22f-b6c0-3fb8-8a3d-acbca30953da | -9.1012 | -45.1393 | 2026-10-09 18:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 123.4 |
| ad762ffd-e440-3740-b1ed-0bd0a70af1e5 | -3.5156 | -59.2324 | 2026-10-09 18:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 2d7008d8-2757-3d86-9e9b-ee64915f1584 | -12.5446 | -47.5875 | 2026-10-09 18:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| e99e9bcc-9a46-377e-bfb8-0f5d6e6e0945 | -1.4486 | -48.9953 | 2026-10-09 18:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| f7ac0ce5-5b1b-3abe-8a72-4fdd288750d5 | -3.9358 | -54.5838 | 2026-10-09 18:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 1500667c-7d15-3c8c-91e3-20a977cab6e5 | -10.4524 | -47.3024 | 2026-10-09 18:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| e1b6a5d0-bfb2-33f6-8e95-48cb14f87748 | -1.383 | -55.1944 | 2026-10-09 18:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 5d25e837-12bb-3190-99f5-1c454df56773 | -9.9398 | -43.5542 | 2026-10-09 18:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 152.7 |
| e3861390-bc15-32bc-a2d0-52b7cc9b45eb | -12.2119 | -44.769 | 2026-10-09 18:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 839412ec-60c8-32e2-8731-785f19e83ab6 | -11.2068 | -45.3091 | 2026-10-09 18:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 7e58bdd9-60c1-3406-8175-14a66acb211b | -4.7404 | -55.6522 | 2026-10-09 18:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 1d21fc1e-51bd-33df-a603-8bb3ac9a769f | -12.2273 | -43.9481 | 2026-10-09 18:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 136.4 |
| dc171cab-4658-3985-a95c-b0f3fd3223c1 | -2.7335 | -57.4717 | 2026-10-09 18:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| d14ec531-8611-3354-9f91-c79f7794d1f5 | -5.2274 | -48.4113 | 2026-10-09 18:00:00 | GOES-19 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 5af40c4a-f841-3a6c-8d34-e5f660160a33 | -15.0713 | -41.7982 | 2026-10-09 18:00:00 | GOES-19 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 854.0 |
| 4314b3e9-2b1f-388e-9835-437c42aaded3 | -9.9007 | -44.8608 | 2026-10-09 18:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 55a61e18-b0e8-3bcd-921d-a41065b36f8f | -13.7447 | -40.8359 | 2026-10-09 18:00:00 | GOES-19 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 107.1 |
| a5cfe5c3-78eb-34f9-a60d-0297e7e1a245 | -10.4334 | -47.3046 | 2026-10-09 18:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 144.6 |
| e8882a1f-c2a4-3849-87b5-6a97aaecd041 | -12.1759 | -44.6351 | 2026-10-09 18:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 288.8 |
| 595dab02-d404-3912-8aa2-4ff127d14486 | -3.2137 | -42.953 | 2026-10-09 18:00:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 882cfff5-a8ee-3dec-84ec-20101ca91fbb | -3.1787 | -50.5807 | 2026-10-09 18:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 110e837a-c0a0-3286-ab06-8628e016c18f | -15.1593 | -48.2361 | 2026-10-09 18:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 80.4 |
| ff963599-7c2e-33ae-af02-de2a8fe1e813 | -15.6777 | -39.6899 | 2026-10-09 18:00:00 | GOES-19 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 132.7 |
| 3366566a-2a44-3832-a3f3-eeb225c43b28 | -13.3865 | -43.8708 | 2026-10-09 18:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 160.6 |
| 7e954ad2-bb91-3672-893d-c9306634cfc2 | -5.7131 | -41.6604 | 2026-10-09 18:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 97.5 |
| f11ac814-f3b3-334f-b91c-1cd3d83374a3 | -3.5193 | -58.0183 | 2026-10-09 18:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 45d81f03-dedc-3e5c-b18d-c8df262c61a7 | -1.8757 | -56.3133 | 2026-10-09 18:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| cdeaf3f6-70a3-303d-a5b0-795794901700 | -11.911 | -41.4058 | 2026-10-09 18:00:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 142.6 |
| 0adc8957-3ec4-3797-93dc-1a32bd6a5873 | -1.3264 | -56.398 | 2026-10-09 18:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 3272466e-6ff8-3003-b9e7-c842a8806fee | -2.4577 | -58.0194 | 2026-10-09 18:00:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 3d0072b4-f50a-3d46-9ab9-564785194478 | -2.5492 | -58.0373 | 2026-10-09 18:00:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 93.0 |
| b50802d8-cdee-3048-95cf-c98bfea6f9e0 | -12.1436 | -43.2992 | 2026-10-09 18:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 220.4 |
| 06a1301a-1459-3622-bd9a-9ee348024072 | -11.0745 | -44.1003 | 2026-10-09 18:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 385.4 |
| c71906d0-43ad-3dfa-ace2-c177602a95b1 | -12.2127 | -44.7224 | 2026-10-09 18:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 0cf000d5-b717-3a36-969a-bca5cd3071fd | -10.9197 | -45.3712 | 2026-10-09 18:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.4 |
| ccd85083-2c18-3591-8351-36f8ed9802e0 | -2.4623 | -56.0879 | 2026-10-09 18:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 6f5d388c-3700-36bf-944c-f916216bc2dd | -10.491 | -47.2533 | 2026-10-09 18:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 191.6 |
| 96ae9ae8-e13b-3e01-ae84-119b335afe43 | -3.5193 | -58.0183 | 2026-10-09 18:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| afb9110b-5952-3759-8eca-b03d10c377c5 | -12.2273 | -43.9481 | 2026-10-09 18:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 570e63b4-e8b9-3b61-80e1-c5ff331d85f9 | -15.4029 | -41.8985 | 2026-10-09 18:10:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 604.3 |
| 8a9c225c-97c2-3ca7-afa7-65f878179626 | -2.5171 | -56.1262 | 2026-10-09 18:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 28bb60d4-f85c-3f4f-a85b-422079ddb63f | -12.1935 | -44.7254 | 2026-10-09 18:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 574c9548-bd41-321a-9dfa-9acf79ec4ee9 | -3.0192 | -53.887 | 2026-10-09 18:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| b94a89af-0282-3c6c-a24b-683ac3803743 | -11.0745 | -44.1003 | 2026-10-09 18:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 209.3 |


[Clique aqui para ver as próximas entradas](README288.md)
