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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66e984d4-5a88-3ea9-aa41-7bcebc78c817 | -16.11222 | -49.86663 | 2026-08-15 05:01:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 80ecb63b-379c-3117-9f35-bbe531b81bb8 | -15.52865 | -53.01074 | 2026-08-15 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d00dbe9-937c-390a-8b13-2f529de9e29d | -15.23525 | -56.47614 | 2026-08-15 05:01:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67c10f96-0aa9-323a-8b3f-44364ff58403 | -20.01532 | -43.89539 | 2026-08-15 05:01:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b8e68fc2-73db-3f81-a066-198671df29aa | -17.89988 | -44.44588 | 2026-08-15 05:01:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f023274-cd28-3c0d-8708-0c4da70ce483 | -20.0204 | -43.89256 | 2026-08-15 05:01:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c2013d8d-110e-3682-a88a-79d34a879356 | -16.88786 | -54.14811 | 2026-08-15 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8a19c7f3-2f8d-3382-a3f0-487f134215e8 | -16.11277 | -49.86206 | 2026-08-15 05:01:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 226ce58a-3bf5-3dbe-9502-d457a7e35aee | -16.88209 | -54.16343 | 2026-08-15 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f73289d5-5098-3d48-8d12-f77d42350a19 | -16.71376 | -46.39994 | 2026-08-15 05:01:00 | NOAA-21 | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1832f2e0-29d9-3180-91b7-70cc8c0150b6 | -16.90249 | -54.17076 | 2026-08-15 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e66d5dc-a97e-371c-b477-3fcc748fca89 | -15.16528 | -52.83353 | 2026-08-15 05:01:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d4fa76d-2cc4-3691-98fd-73b0352f9d65 | -15.29078 | -53.18908 | 2026-08-15 05:01:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 258b77a6-6bb9-353d-8547-328b48506cad | -16.1091 | -49.86437 | 2026-08-15 05:01:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e0af4670-d48e-3536-b330-b518f47bc639 | -18.17707 | -43.98757 | 2026-08-15 05:01:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 02096e28-cafb-328e-908e-87b46c53f2ae | -16.66956 | -49.41346 | 2026-08-15 05:01:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d632d421-8c09-3fb7-8a92-b50bee1718f6 | -17.90591 | -44.45118 | 2026-08-15 05:01:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd452e6e-4691-3433-958c-723f60d9cec1 | -16.89599 | -54.14126 | 2026-08-15 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 283b03a2-5cd4-397a-84b9-5e9ecd3a9bee | -20.33289 | -46.74821 | 2026-08-15 05:01:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1212cbf-f8d6-3ad8-aa01-2fdb3c77cc6f | -16.89372 | -54.15711 | 2026-08-15 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7004d6f1-41ee-349e-86be-c9426448ab3a | -15.1919 | -52.7252 | 2026-08-15 05:01:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26648e50-b3ce-3db1-a924-a1e2641f57ed | -15.52684 | -52.99712 | 2026-08-15 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a284f569-66a9-312e-830e-981d74f4eb07 | -16.89249 | -54.14074 | 2026-08-15 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 51772b6d-297d-38af-8407-d051e8e6330b | -16.10834 | -49.86138 | 2026-08-15 05:01:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9f1dbaf4-bdde-3fd8-a845-515c1fbd6cb6 | -16.90306 | -54.16677 | 2026-08-15 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7ed2ddac-34be-3954-9177-2eeab846c0e5 | -20.3341 | -46.73521 | 2026-08-15 05:01:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7235b88-a0a3-3487-ae7d-b5715a5ca7c9 | -16.18849 | -55.96183 | 2026-08-15 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d19f609a-b57d-3589-9f49-eb43782f976e | -16.90714 | -54.16333 | 2026-08-15 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b7b3d81-f4bf-3253-850c-20faeff39c80 | -15.52562 | -53.00583 | 2026-08-15 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64b269e2-3c1c-34da-a0f5-0daca1250aa3 | -22.99876 | -52.42995 | 2026-08-15 05:04:00 | NOAA-21 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c808370e-5e0d-37f7-99d6-35ebd18a3696 | -23.50601 | -51.72857 | 2026-08-15 05:04:00 | NOAA-21 | MARIALVA | PARANÁ | Brasil | 4114807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 07d7ac7b-c748-3759-9f52-ee60388a2e1a | -22.99658 | -52.4275 | 2026-08-15 05:04:00 | NOAA-21 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 514d351e-0a66-3a6c-b0c8-9410c43d8b84 | -23.50502 | -51.72588 | 2026-08-15 05:04:00 | NOAA-21 | MARIALVA | PARANÁ | Brasil | 4114807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b2b2b99e-4136-39fa-89d8-9be0e829a038 | -22.99923 | -52.42588 | 2026-08-15 05:04:00 | NOAA-21 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 51fd56c4-cb1b-3ab4-a5ff-b5e28651548c | -6.6194 | -59.0609 | 2026-08-15 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| cd4508bc-6579-3fce-9589-7f17c04a6e27 | -14.4495 | -51.9217 | 2026-08-15 05:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 124.9 |
| d7a0830e-7397-31e0-99c5-4664ee706199 | -14.4302 | -51.9243 | 2026-08-15 05:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 144.9 |
| be1745dd-f7a8-37d9-be1d-b15e314285cd | -11.4371 | -46.3707 | 2026-08-15 05:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 87b8fb14-bee8-3878-b203-6a408f931d60 | -14.4499 | -51.9004 | 2026-08-15 05:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 273.9 |
| 5ed6799c-83aa-367c-98d5-e7e36f02ae71 | -14.4306 | -51.9029 | 2026-08-15 05:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 247.1 |
| 0494b03d-6478-3b0c-8124-119dc48943cb | -11.418 | -46.3733 | 2026-08-15 05:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.0 |
| d3e87aa2-85a2-33ca-8b86-4c5e35aa3c70 | -11.4375 | -46.348 | 2026-08-15 05:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.8 |
| d58c4ecd-599c-3d6d-92f3-336aba9b4234 | -11.4184 | -46.3506 | 2026-08-15 05:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 135.4 |
| fdd820dd-d174-36c8-8733-9eb91ebeb403 | -6.6013 | -59.0037 | 2026-08-15 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 09e6ae57-2134-303c-a0a3-f79eac0e78bf | -11.4375 | -46.348 | 2026-08-15 05:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 7b4c0f3d-da01-301c-87e8-c6ef12c90773 | -14.4499 | -51.9004 | 2026-08-15 05:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 127.3 |
| b35a3073-18e3-3da8-b86c-e88186e50678 | -11.4184 | -46.3506 | 2026-08-15 05:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 5d9246e7-63c9-3397-b447-7c07d7f6371d | -10.4047 | -47.9714 | 2026-08-15 05:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 5d7e3dac-0a37-31bb-80d0-8aab7dde5fdb | -14.4306 | -51.9029 | 2026-08-15 05:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 252.0 |
| e5474775-d1f7-30a0-99e7-7d5b60e274b3 | -14.4495 | -51.9217 | 2026-08-15 05:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 3a4677af-0756-3241-a661-8414b58c5080 | -14.4302 | -51.9243 | 2026-08-15 05:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 58462e2d-7d8a-35cf-b405-701c8c1dc43a | -11.4371 | -46.3707 | 2026-08-15 05:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 9f82ed1b-e18e-3074-b316-1c5ec73444de | -6.6194 | -59.0609 | 2026-08-15 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 4b8aecea-6ad5-3916-9fb0-549046626a78 | -11.4371 | -46.3707 | 2026-08-15 05:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 0e357aac-2d6c-3d01-8a10-936795f00b29 | -14.4309 | -51.8816 | 2026-08-15 05:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 8df3c847-2535-3b6d-a551-6adb77b9992b | -6.6194 | -59.0609 | 2026-08-15 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| e72282e2-d617-3fa7-8c52-7ceadfbf6eb4 | -6.6013 | -59.0037 | 2026-08-15 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| c258599c-92d3-3d80-b9a7-8100b0fe36e5 | -14.4495 | -51.9217 | 2026-08-15 05:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 9a1e5939-633e-3e2c-804b-823fdbad0f13 | -11.4184 | -46.3506 | 2026-08-15 05:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 732ff3dc-f64f-315d-a3cd-45a606208b7a | -14.4499 | -51.9004 | 2026-08-15 05:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 2d71299e-2032-3fb2-adb2-efcdc1c4d2f2 | -14.4302 | -51.9243 | 2026-08-15 05:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 189.9 |
| eb6c8734-76eb-3d01-ac93-399d957d2ab8 | -14.4306 | -51.9029 | 2026-08-15 05:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 312.5 |
| bba4a56d-d321-33db-9cae-51557e16c2df | -11.4375 | -46.348 | 2026-08-15 05:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 09e79793-ad62-3797-8624-7866f3222700 | 0.48905 | -60.59473 | 2026-08-15 05:31:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9beaef2-81ac-339e-b365-5b0e3b26280b | 0.89458 | -59.69788 | 2026-08-15 05:31:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e9e5e22-fe10-3039-b365-ef923474a17b | 0.49919 | -60.59313 | 2026-08-15 05:31:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d810267-78c8-3259-9394-1a592acd1ff9 | 0.78355 | -59.70095 | 2026-08-15 05:31:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e8682b5c-bd69-3e3d-a9ef-828a87bcac0d | 0.89125 | -59.6984 | 2026-08-15 05:31:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca91f36d-4b7f-3396-a4ba-fea5562f7b35 | 0.8907 | -59.69493 | 2026-08-15 05:31:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd223387-64e5-3769-ba1f-d7d5e1dd24df | -6.94027 | -62.87416 | 2026-08-15 05:33:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b92f8e1e-971a-3646-bed0-e00001da8955 | -6.84532 | -56.43055 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 39a62cd6-6237-3d16-b6e4-84368cc092a0 | -7.54954 | -55.57047 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d3e7aa8-e44b-38ce-9b79-f052725a3af9 | -6.83831 | -56.42455 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7c89553c-09e9-3d96-9510-a6c9b2e60abd | -6.61776 | -58.99314 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 80b5aa02-2b68-3e8f-9d02-920e134c1c2a | -6.58812 | -56.36324 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 41c7ef9c-b425-3d1c-b2b2-59ae94fee7f5 | -6.61321 | -58.99997 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2385e2ec-7998-3df5-af8c-c08f11edd12a | -3.74009 | -59.33278 | 2026-08-15 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d09b5da6-b67a-3324-949e-7af3f4b454fa | -6.69717 | -58.95182 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97d5ad1d-ddd9-3fed-a20c-3cb12141a405 | -6.85611 | -58.96455 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3e3d8e27-479f-39a6-b9ca-f8b393278c32 | -6.9545 | -59.2951 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dff32f43-2d0f-3e83-ad31-1bc390aaa539 | -6.96413 | -59.278 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4177945c-9193-389e-81fa-5a6761eb19a3 | -6.85068 | -56.42141 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 48bd1201-3f7e-3d8e-8e2c-55deb7d9e08f | -6.79811 | -55.8381 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8e0d6f8-6ab8-3b18-b262-92f5f6f04941 | -3.46683 | -59.62804 | 2026-08-15 05:33:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa8ba906-3bc1-3469-8a2f-759684365255 | -6.85691 | -56.4091 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4d89a5e-7232-3ab0-b18a-9b002891f637 | -8.0178 | -55.1297 | 2026-08-15 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dce48738-6a33-31ff-a21e-d41211bfb939 | -6.93478 | -62.87416 | 2026-08-15 05:33:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 887baa1c-78ad-33f2-8bba-3d041902a40a | -6.84813 | -58.97087 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc688020-f408-3984-9f0e-1ea92c9054a8 | -6.85019 | -56.42809 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 96f78129-a4f4-3c4e-b1b1-acb0a7eb13d9 | -4.3109 | -59.47165 | 2026-08-15 05:33:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0eed04ef-9591-3f21-bc79-788a60aea5c1 | -6.61576 | -56.33763 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c91dd453-ff7c-31c7-8e1f-7c83714b93b2 | -6.85762 | -56.40422 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53a8bfe2-88ac-37b8-aa1a-5b8ac1de87a1 | -6.85306 | -56.4318 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1037a410-1d07-331c-8aaa-a16eecf37904 | -6.85406 | -56.4287 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 430778bc-b7b1-3daa-b4f6-156d72160955 | -6.96156 | -59.2995 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3e486b5a-d287-3a52-b091-9a2f4dd8176d | -6.85726 | -58.95713 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36b3e8a7-a751-3c75-8e6e-e8a9d8af5412 | -6.60651 | -56.34634 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3712b995-9add-3785-b1d8-c0b9304975cd | -3.62741 | -60.32482 | 2026-08-15 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d00b5932-ede9-3352-b427-4cabd133e606 | -7.06004 | -56.51581 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a807234-6b1f-3292-b9c7-5ce344d781d6 | -3.59634 | -58.61885 | 2026-08-15 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README36.md)
