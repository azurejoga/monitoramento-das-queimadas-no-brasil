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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57232009-b81e-3587-a432-47f923cfbb58 | -7.30927 | -55.15318 | 2026-06-05 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9b61070b-c324-3123-86e2-d9a4b5f76307 | -10.03321 | -59.35061 | 2026-06-05 00:28:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 509b8fa1-fbe6-3180-9eaf-c245c5cb65e7 | -6.84577 | -47.9416 | 2026-06-05 00:28:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b09b8013-c5a4-3a31-9723-3503fca92832 | -7.34335 | -49.84373 | 2026-06-05 00:28:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 9a8c3f77-7455-3937-b3f2-25f0bf932658 | -7.46296 | -49.74264 | 2026-06-05 00:28:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 209755f3-87f3-3e39-9d38-c4ef58b12220 | -9.37339 | -50.54192 | 2026-06-05 00:28:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 20fc56c9-0fe7-3805-b3d9-441d227438d1 | -7.96049 | -46.84493 | 2026-06-05 00:28:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 99f17206-6a12-3b13-8846-ab541bf302bb | -5.30418 | -47.2355 | 2026-06-05 00:28:00 | TERRA_M-M | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 15.2 |
| cbf7fca0-d5f4-3b57-8be7-112fa596441b | -7.34149 | -49.83127 | 2026-06-05 00:28:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| a7fc7c98-1de6-300d-b2ab-78e3d4a094d7 | -8.72715 | -48.33221 | 2026-06-05 00:28:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 48059cfd-9928-3e5d-ad8c-5cb190592ecf | -8.72482 | -48.3168 | 2026-06-05 00:28:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b9536112-eb2c-3c8c-bbd6-75f52b90ba42 | -8.72946 | -48.34752 | 2026-06-05 00:28:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 1fcf3ab0-0d39-392d-8cb2-53700b47d2e4 | -7.35184 | -49.82972 | 2026-06-05 00:28:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| fc2696f0-2879-37b7-8871-49ff4ff1d9f5 | -12.4464 | -58.4825 | 2026-06-05 00:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |
| b4f909ae-ec74-376b-a103-2bae4f9e4b41 | -12.4466 | -58.4627 | 2026-06-05 00:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 3717c27d-496c-3e95-8352-80c4980461a9 | -8.7208 | -48.3441 | 2026-06-05 00:30:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 44.2 |
| c8f7c5f1-4ab7-39ff-83d1-bcb8e8e12359 | -11.5496 | -52.8076 | 2026-06-05 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 260.8 |
| b3eb53a9-79ef-3749-9918-5bb37862658f | -11.5686 | -52.8057 | 2026-06-05 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 165.4 |
| 6fdaddf8-6f1a-33b7-b9a1-a76f068ad04c | -11.5688 | -52.7848 | 2026-06-05 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 21f3bdc0-8d44-306d-9f9f-aca6419da9b0 | -11.5499 | -52.7867 | 2026-06-05 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 4a9df6bb-31a1-3825-8179-d98794b57bca | -8.7211 | -48.3222 | 2026-06-05 00:30:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| c2e9f0a9-dc01-3bea-8463-78bc832de8ac | -3.9895 | -47.923302 | 2026-06-05 00:32:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87ec98f7-78b5-3d32-bc0e-d45ac8c81dc8 | -7.3445 | -49.8293 | 2026-06-05 00:32:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1e0dbd1-3843-329d-91d9-fcda69f954f7 | -7.3462 | -49.837002 | 2026-06-05 00:32:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 377c62a1-4a14-3ce8-9568-20690906a56c | -3.991 | -47.930099 | 2026-06-05 00:32:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1852182-283d-3dbb-b148-b03ab504e3d1 | -5.307 | -47.238701 | 2026-06-05 00:32:00 | METOP-C | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 26fb22b7-8cd9-3b10-9e88-79a318f4e7ee | -7.3428 | -49.821602 | 2026-06-05 00:32:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3a6a7b3-a139-3f56-aad7-560ed0155254 | -5.3055 | -47.2318 | 2026-06-05 00:32:00 | METOP-C | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 521eb07c-3e76-3ac1-b6cd-a1c65f8b6c6f | -6.848 | -47.938999 | 2026-06-05 00:32:00 | METOP-C | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0d6598e2-f13f-3bda-8ce8-d9b3ad49d82d | -11.5499 | -52.7867 | 2026-06-05 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 114.2 |
| b767d9a9-970e-3953-968a-37450db3732a | -11.5686 | -52.8057 | 2026-06-05 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 126.7 |
| b736bd06-a1a8-3f64-a32e-4cbfbcfd6083 | -12.4274 | -58.484 | 2026-06-05 00:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 9706b444-9561-3213-af1e-29502a75101d | -11.5496 | -52.8076 | 2026-06-05 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 228.1 |
| 10821c51-a044-3090-b0f4-df13ca25a51f | -12.4464 | -58.4825 | 2026-06-05 00:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| a6642cb4-0f14-3e6c-8f45-29b4cb185c6f | -8.7211 | -48.3222 | 2026-06-05 00:40:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 45.9 |
| e24ec1ee-addc-35b2-9c18-b14da2dc7aed | -11.5688 | -52.7848 | 2026-06-05 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| d8e2cbef-4867-3d88-beac-1033f336d264 | -12.4274 | -58.484 | 2026-06-05 00:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 5f0eaa2e-51ee-31ad-ac7e-d47e9dbcb54f | -11.5686 | -52.8057 | 2026-06-05 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 146.8 |
| ef3001c1-75ef-3ba6-a84e-b557fff86ce3 | -12.4464 | -58.4825 | 2026-06-05 00:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 921f15ae-1ab1-3b5c-8c0c-cb4f55d9c105 | -11.5496 | -52.8076 | 2026-06-05 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 149.0 |
| 87016614-62b0-3baa-b45a-4ea9649788a8 | -11.5688 | -52.7848 | 2026-06-05 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 55879227-566d-33b1-85d3-11317298399b | -20.9327 | -49.2178 | 2026-06-05 00:50:00 | GOES-19 | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 86.6 |
| a5067b77-29ca-3f70-be36-81b7dd61ca0b | -11.5499 | -52.7867 | 2026-06-05 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 0ce53c79-85a1-3780-86c4-ca44f538bfc4 | -20.9321 | -49.2408 | 2026-06-05 00:50:00 | GOES-19 | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 61.2 |
| c586901b-fbb9-393d-bb7b-9e12719d44bc | -8.7399 | -48.3205 | 2026-06-05 00:50:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 75a85ce1-47fd-3076-ae18-e6c087c4e25c | -22.2886 | -47.2332 | 2026-06-05 01:00:00 | GOES-19 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Cerrado | 57.2 |
| ed1483df-f1cd-3800-a444-8c2ac5bd4800 | -11.5496 | -52.8076 | 2026-06-05 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 162.0 |
| 96c834c8-13f6-33d9-b43d-a4d3b9e4246a | -22.3103 | -47.2037 | 2026-06-05 01:00:00 | GOES-19 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 05ffaf2a-27c5-3a80-9140-c3d57e67c035 | -22.3096 | -47.2277 | 2026-06-05 01:00:00 | GOES-19 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Cerrado | 135.6 |
| e15f22cf-f4ed-39ae-a173-14d56ca6ed67 | -11.5499 | -52.7867 | 2026-06-05 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| ae3d614b-8c61-31bd-9b56-24deb2d87a6a | -11.5686 | -52.8057 | 2026-06-05 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 118.9 |
| 4bc7f64b-ecfc-3154-98aa-cbae632fe3ed | -12.4464 | -58.4825 | 2026-06-05 01:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 193a22d8-53ed-3695-baa3-002f1f3ba56a | -11.5688 | -52.7848 | 2026-06-05 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 8119fd15-5b7d-3bcd-a006-081c8ea94f2f | -11.5686 | -52.8057 | 2026-06-05 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 9816e9cf-b01c-3b69-9f04-1ec9b0327377 | -12.4466 | -58.4627 | 2026-06-05 01:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 31a30c2b-f590-3a0c-a2cb-65fd3f76d698 | -12.4464 | -58.4825 | 2026-06-05 01:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 02d4f56b-ec90-3711-aba3-c1aa6686ce19 | -11.5688 | -52.7848 | 2026-06-05 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 64639b75-9fef-3973-a3d9-0d566236990e | -11.5499 | -52.7867 | 2026-06-05 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 5d865ff8-4e34-3c31-86b2-be1696f7b1b7 | -12.4274 | -58.484 | 2026-06-05 01:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 47.9 |
| c36b33a9-cc05-3de0-8315-b24088fd3cd8 | -11.5496 | -52.8076 | 2026-06-05 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 150.7 |
| 74cd04fb-56c0-3b7b-b6a5-5f16658f63fd | -11.5686 | -52.8057 | 2026-06-05 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 124.0 |
| 60dd2484-53d1-341c-935c-3820c86ebcea | -11.5496 | -52.8076 | 2026-06-05 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 144.8 |
| 91cd7a89-a371-308c-9e77-394615395191 | -12.4464 | -58.4825 | 2026-06-05 01:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 9b851ff1-fd44-3cdc-9293-966df4c2746e | -11.5499 | -52.7867 | 2026-06-05 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| fc328357-eeab-3fe1-a19d-b75e9f86bc4c | -11.5499 | -52.7867 | 2026-06-05 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 9a17eb14-2087-3f09-86c3-6d36de50612f | -11.5686 | -52.8057 | 2026-06-05 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 5bbb991e-ceae-3e72-a388-4a9da7ddde96 | -12.4464 | -58.4825 | 2026-06-05 01:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| afe412c7-a267-3b0c-a3ae-3703d5788dd5 | -11.5496 | -52.8076 | 2026-06-05 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 147.6 |
| 57d78388-90ad-3234-87b9-5cd9f348687b | -11.5686 | -52.8057 | 2026-06-05 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 2347d5ba-57be-305b-a44d-a673034c1e12 | -11.5688 | -52.7848 | 2026-06-05 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| adfffc36-2317-32bc-9320-e459117724f0 | -11.5499 | -52.7867 | 2026-06-05 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 6650eaba-b3b1-30a9-8c92-2f915a9a039b | -12.4464 | -58.4825 | 2026-06-05 01:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 67.4 |
| cc204ca0-7a57-38f4-9483-abbfcd33c26f | -11.5496 | -52.8076 | 2026-06-05 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 952c852f-d0ed-3575-b4e4-062da8d83443 | -11.5688 | -52.7848 | 2026-06-05 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 46.2 |
| ef144b4c-2972-34ac-bbff-38c1d6bedf52 | -11.5499 | -52.7867 | 2026-06-05 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| ead16591-f56b-34c4-a8ff-7b69fc59c258 | -11.5496 | -52.8076 | 2026-06-05 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 0e7b4dc7-6bd7-3647-af6e-45bfc7e20fe9 | -11.5686 | -52.8057 | 2026-06-05 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 68dad382-8276-35d9-acf0-c5d38b58d80f | -12.4464 | -58.4825 | 2026-06-05 01:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| efc840c1-cab6-376c-a4d5-1c4c72e25424 | -11.5686 | -52.8057 | 2026-06-05 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| bcaea01f-1ac8-3cd5-8bc7-4b48abff73a5 | -11.5688 | -52.7848 | 2026-06-05 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 26880191-817f-3b6c-9e3b-dbefcc6c16c6 | -11.5496 | -52.8076 | 2026-06-05 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 07e12094-deb6-3eaa-8ac6-1256226bf70c | -11.5499 | -52.7867 | 2026-06-05 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| ebff4ceb-d9d7-3f52-bc54-5925e9881446 | -12.4464 | -58.4825 | 2026-06-05 02:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 60a39808-e231-3e9a-a7f9-bcac8cdf28e7 | -11.5496 | -52.8076 | 2026-06-05 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 2263c9ae-4921-359b-96bf-13ab4fb488c6 | -11.5686 | -52.8057 | 2026-06-05 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| f42cdc71-e7ea-34d6-9393-ebea02da3f78 | -12.4464 | -58.4825 | 2026-06-05 02:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 30dc0df6-85b9-3c6e-bf2e-54345bebb97c | -11.5496 | -52.8076 | 2026-06-05 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 90.0 |
| a5de0abc-1dd8-39bf-a8b3-55ed378c8d69 | -11.5686 | -52.8057 | 2026-06-05 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| f9658cdc-5daf-3a5d-8330-9e531db28b8c | -11.5686 | -52.8057 | 2026-06-05 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 50fd02ab-37a2-37cc-9735-93b5485accae | -11.5496 | -52.8076 | 2026-06-05 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 195e87b3-cace-3dad-996c-f75abae537c2 | -11.5496 | -52.8076 | 2026-06-05 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| ce571f08-6d2e-357f-b3f0-1146024cdf0d | -11.5686 | -52.8057 | 2026-06-05 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| c721b1ed-23ed-30e6-90a1-64cb2c64570a | -12.4464 | -58.4825 | 2026-06-05 02:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 7b675bde-f1a1-382e-b665-65fab2c7b83c | -11.5496 | -52.8076 | 2026-06-05 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| f78ec5ba-400c-3438-bea8-a88b63205fd2 | -11.5686 | -52.8057 | 2026-06-05 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| f569e80d-a8c3-36a6-9050-f1dfd814d6e8 | -11.5496 | -52.8076 | 2026-06-05 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 862e5b69-fb4e-3d5e-91f5-cfa5d131ccf2 | -11.5686 | -52.8057 | 2026-06-05 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 299f8f50-59fa-31e5-8749-6497b30b341e | -11.5496 | -52.8076 | 2026-06-05 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 404177a0-dc70-31ef-9fce-151a70f5fd42 | -11.5686 | -52.8057 | 2026-06-05 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 0fb2baec-6650-3db5-9f0b-192eadee3dd0 | -11.5686 | -52.8057 | 2026-06-05 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |


[Clique aqui para ver as próximas entradas](README4.md)
