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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73fd8ea2-d737-3c56-990a-bfdd9be82918 | -8.4737 | -47.0053 | 2026-09-20 14:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| a80fa0c7-b703-3360-a0c0-4efd2afaf18a | -6.737 | -55.0674 | 2026-09-20 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 4d0a6f85-e779-3ab4-9924-65c241a37506 | -10.2787 | -50.2605 | 2026-09-20 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 4e1877d6-3a7a-34cd-85d2-0db2c3366fdf | -12.1715 | -47.0131 | 2026-09-20 14:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 77a30487-c030-3257-8fe9-07e67f3b44f1 | -9.6964 | -45.8666 | 2026-09-20 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 509e7d91-f0bc-381e-a47d-56efd4e18779 | -12.5081 | -50.952 | 2026-09-20 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 0932c4f1-e362-3735-895e-c074aa4dd231 | -11.4736 | -45.3405 | 2026-09-20 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 110.0 |
| ce98b30f-2e49-31b6-830c-0a5259473ee9 | -11.4537 | -45.3892 | 2026-09-20 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 7842b1d8-4ba7-31f3-83ed-38a01c6dd5b7 | -10.8177 | -50.9286 | 2026-09-20 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 116.9 |
| a0115d80-edb2-391c-a3a7-30a92d128c22 | -11.3983 | -51.3968 | 2026-09-20 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 1cfb5f84-686b-3380-8fff-f709b78ee851 | -15.4174 | -53.0236 | 2026-09-20 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 129.5 |
| d0f5501f-35e3-3e05-a8f0-8a14204243e6 | -8.9269 | -49.9843 | 2026-09-20 14:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 334654c7-5713-3406-8717-af2545707f6a | -6.5948 | -45.5179 | 2026-09-20 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 91952b21-bb36-365b-a28e-e1fc7024c21b | -6.7406 | -44.0909 | 2026-09-20 14:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| ee9246d4-19a5-38bf-b4af-0a558feac067 | -9.0096 | -44.9209 | 2026-09-20 14:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 86.3 |
| da4156e7-f883-3d4f-8acc-147204212d38 | -9.2563 | -46.2323 | 2026-09-20 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 1421235c-b557-3d23-9efa-807990daf8dc | -11.0407 | -54.1772 | 2026-09-20 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 103b13bf-0a80-3120-8e30-b22be97a2886 | -11.041 | -54.1567 | 2026-09-20 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 20170451-3711-3f3e-8d77-d3aeb85b0ea1 | -6.1981 | -55.4534 | 2026-09-20 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 4d79b034-4cf1-36d3-97ac-c496a8cfdf55 | -7.5548 | -48.6843 | 2026-09-20 14:30:00 | GOES-19 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 6e1a6a6a-fb13-34d5-a21e-2b500cf3f6e8 | -10.7466 | -50.5959 | 2026-09-20 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 4c42cf60-be82-32b5-8104-c02fb0e76b72 | -14.061 | -52.1 | 2026-09-20 14:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 1cb00281-f6c8-3658-aea6-80d45eaaa957 | -11.0506 | -54.9309 | 2026-09-20 14:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 197.3 |
| 649dc919-05ce-3314-8987-a0eb0da046a5 | -10.5558 | -46.732 | 2026-09-20 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 107.0 |
| ce29193f-8405-31df-8e65-8b37bb8ce1d6 | -6.4485 | -59.9909 | 2026-09-20 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 184.4 |
| 6552bd21-c039-3f83-a384-4929f7cccaca | -7.026 | -42.0924 | 2026-09-20 14:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 106.2 |
| fbca37b3-819a-39ca-a8cb-ad14d125c5ec | -11.3793 | -51.3989 | 2026-09-20 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 143.9 |
| d8ce5039-b49e-3cba-b093-7cd845f7e42a | -11.0596 | -54.1755 | 2026-09-20 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 157.1 |
| c3f0e57e-12a1-3f31-bd0f-590997da6cc9 | -3.3321 | -59.4469 | 2026-09-20 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 7ec9dd8a-d5de-3484-ab56-bc35a34e741c | -11.8747 | -49.9983 | 2026-09-20 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 454.2 |
| 8089c11f-09da-32ed-b9ff-043d551e74e0 | -6.4302 | -59.9724 | 2026-09-20 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| d9d3e027-2bae-3812-b069-abd498d9560a | -2.9143 | -58.3401 | 2026-09-20 14:30:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 35ad5fd5-608e-310d-a010-c23fb771647c | -11.398 | -51.418 | 2026-09-20 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 192.4 |
| a289037b-c7ef-3f4c-97c8-763e51553e95 | -8.2315 | -61.3541 | 2026-09-20 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 6c70a3fd-c4f6-3bda-a55b-bfb842346989 | -11.7823 | -49.8152 | 2026-09-20 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 91a6692d-ed7e-30f7-bd5c-e8bc6b63a6d6 | -8.1688 | -54.7432 | 2026-09-20 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 670f0d54-7e83-3ca0-96fa-2287025080d5 | -10.8553 | -50.9459 | 2026-09-20 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 235.3 |
| dad197e2-86c8-3235-aba4-94e16ad25762 | -3.8814 | -40.7251 | 2026-09-20 14:30:00 | GOES-19 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 188.3 |
| 8919b324-6253-317a-a9d1-7efe5d54e1a2 | -12.2341 | -50.1703 | 2026-09-20 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 668b9630-5624-380b-a632-dc7308f43b64 | -9.2603 | -45.939 | 2026-09-20 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 145.4 |
| f97920d7-7b85-3a67-8489-0058d1e8b0e4 | -6.9174 | -41.6957 | 2026-09-20 14:30:00 | GOES-19 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 96.1 |
| 678894bd-d6a0-3a64-bf32-642428678d3a | -11.0614 | -49.7477 | 2026-09-20 14:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 130.8 |
| e153a972-5a83-3086-b250-e3f54ae0fab8 | -6.9851 | -45.8235 | 2026-09-20 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 4aba6cbd-0fa7-35ea-bc2c-52d7f7b32b9b | -11.7351 | -54.5636 | 2026-09-20 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 93.4 |
| b7b56107-399e-306a-93c9-90713ab28ed7 | -9.2606 | -45.9164 | 2026-09-20 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 3fa48337-ce78-3904-8aac-810b8b76358c | -10.7463 | -50.6172 | 2026-09-20 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 7b87de85-92ad-3734-b396-9eb7b205c80d | -6.3199 | -59.9381 | 2026-09-20 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 3d87e93c-53cd-39e7-86b0-5f8148ebcf84 | -11.9352 | -49.7752 | 2026-09-20 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 6e31cd2b-3108-31c7-99f5-7088a6635a6c | -12.5269 | -50.9711 | 2026-09-20 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 239ef627-565c-3d15-a98c-84ef443b2a6f | -9.2567 | -46.2098 | 2026-09-20 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| b2fe5017-3940-3cc5-b134-42c9e54e2f31 | -8.0279 | -61.3626 | 2026-09-20 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 6bad640e-0f85-33ec-a92f-969a32d17ff7 | -9.8397 | -46.4361 | 2026-09-20 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 194.7 |
| a4e594ca-443e-3e21-b328-bfcd193342d1 | -3.3138 | -59.4472 | 2026-09-20 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 26ffef51-e08d-351e-8a22-3a6eecc66b2e | -3.2955 | -59.4476 | 2026-09-20 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 8bec40f7-11d3-3648-91e8-6944a9b8736a | -9.2865 | -48.2453 | 2026-09-20 14:30:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 59955eb1-7181-317a-9172-72f1a4a971fe | -8.3727 | -47.589 | 2026-09-20 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 1f535087-df85-3d54-8818-8c7709570387 | -10.4103 | -48.9112 | 2026-09-20 14:30:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 2bdcdcc9-072b-3c85-aae0-f2a2c09abe7c | -12.1516 | -47.0608 | 2026-09-20 14:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 116.6 |
| ca45d03f-c567-33e9-9ce3-2e5eb5e43442 | -6.3198 | -59.9572 | 2026-09-20 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 50bb9a31-ad58-3f41-83e4-85b4b777499f | -5.8088 | -55.7095 | 2026-09-20 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 531afe7d-600d-3410-9bcc-0f3e4c89a1f8 | -8.4376 | -46.8757 | 2026-09-20 14:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 25cad270-a137-3b87-8253-2d6e3483e266 | -8.9752 | -44.6722 | 2026-09-20 14:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 6109b7f9-b4c2-3c84-a76b-2a08fb1e5eeb | -11.6621 | -50.2169 | 2026-09-20 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 8dae66f8-e600-3f49-b6e9-e5f8513acfd4 | -12.642 | -50.9359 | 2026-09-20 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 3c781115-3968-35b3-b2c3-544814c5a2a7 | -6.7184 | -55.0884 | 2026-09-20 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 116.1 |
| 18be8e20-32cc-3069-aa0b-47a278dc5a6f | -8.4549 | -47.0072 | 2026-09-20 14:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 3e3eb076-9b23-3b2a-a61a-8e736de7a140 | -7.2519 | -55.5994 | 2026-09-20 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| a69fb9b8-8617-309c-9ce8-f0c2f794b3e6 | -11.6429 | -47.7761 | 2026-09-20 14:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 217.9 |
| 0f36d9f3-860f-3e4c-a5c4-f852e85720b5 | -10.8757 | -57.1554 | 2026-09-20 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 6ce1a4b9-6403-392c-8368-3569dd03b4d8 | -11.4545 | -45.3432 | 2026-09-20 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| e92db9f8-666d-374c-8e99-b252aab70845 | -6.1109 | -57.684 | 2026-09-20 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| e0d59029-a3df-395e-bd51-9ae6cc423c3e | -8.2314 | -61.3732 | 2026-09-20 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 39d101bd-d420-3777-8984-953bfab95ec6 | -8.2499 | -61.3724 | 2026-09-20 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 117.7 |
| b71a5552-7bf7-3992-89e4-71ad8cf880e0 | -9.0541 | -48.7686 | 2026-09-20 14:30:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 598.1 |
| b6300a83-dd2d-3481-9bf9-e8e43127bf9b | -11.0256 | -48.3164 | 2026-09-20 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| ee2892e7-ae7d-3678-a746-5e05ff74e592 | -5.7431 | -57.5814 | 2026-09-20 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 0dce50c9-cfd6-395c-afcb-0c5153bc31a2 | -8.1686 | -54.7634 | 2026-09-20 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| bc28e856-8d97-306f-88ea-30ad434df683 | -7.3289 | -55.2155 | 2026-09-20 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| d4a34556-dde3-3eba-94ef-44076eb1b845 | -6.4301 | -59.9916 | 2026-09-20 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 5efa6787-f3be-3cf2-9140-e47c457a3547 | -6.3382 | -59.9566 | 2026-09-20 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.5 |
| bff655d6-7849-3df5-9cbf-11817d8776b0 | -11.731 | -50.7014 | 2026-09-20 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 91c70f42-7daa-33ed-ab01-a186a30f4433 | -8.4797 | -57.6282 | 2026-09-20 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| f38a59c1-e569-3a03-bad2-eec03415d10e | -6.5953 | -45.4727 | 2026-09-20 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| d083aadb-8aaa-3ea3-8db0-ddfc6f6d2263 | -9.8313 | -48.4073 | 2026-09-20 14:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 3efeb455-5e84-3f64-8423-ff4fa9cb815c | -13.9637 | -47.8688 | 2026-09-20 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 2423d7c5-4d46-3268-be5d-a6ec3a0d9d81 | -8.05 | -46.2663 | 2026-09-20 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 747d854d-3df9-369a-96f4-a98e5e2cc449 | -10.9694 | -57.1881 | 2026-09-20 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 8f3b00f7-99fc-38b4-818f-542168b33600 | -11.155 | -42.7885 | 2026-09-20 14:30:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 112.9 |
| c88bc9bc-7e98-323a-8be2-d48f45dc03cb | -11.1225 | -49.4601 | 2026-09-20 14:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 183f7d9a-cf97-3da0-bc5b-caa6c9923500 | -6.4486 | -59.9717 | 2026-09-20 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 307.3 |
| c1ac712e-6b87-39d3-84ef-4f833ed920ef | -12.0267 | -50.0231 | 2026-09-20 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 54378a09-f5fb-3b57-a953-a25d6bc2c599 | -12.2344 | -50.1488 | 2026-09-20 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 0f385c71-f039-3b8c-883f-d3cff1e8229c | -9.0286 | -44.9187 | 2026-09-20 14:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 69b771b5-5502-31a8-b53c-b3f3bb3ec2e8 | -11.378 | -44.2429 | 2026-09-20 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 509de494-b688-3483-951d-4d3f4931685d | -3.2361 | -61.217 | 2026-09-20 14:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 175f0d33-70f8-3ff3-bc72-8762c862cf06 | -10.7652 | -50.6153 | 2026-09-20 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 171.9 |
| 3ed71747-bc04-3475-a624-2aff918d8a13 | -6.4671 | -59.9711 | 2026-09-20 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 139.6 |
| 06ec8a8b-590d-3350-938c-0931eb96e707 | -9.0355 | -48.7487 | 2026-09-20 14:30:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 0bb8059c-a6ea-38b2-b65f-6b68868904e0 | -13.5907 | -51.4794 | 2026-09-20 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 8a5a57e8-46d2-3725-8fb9-1edcac999baf | -17.5795 | -44.9765 | 2026-09-20 14:30:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 103.0 |


[Clique aqui para ver as próximas entradas](README129.md)
