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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17c07760-a250-3059-9ca3-4490afe77feb | -10.6598 | -54.5169 | 2026-07-01 06:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 07db1f07-34c8-36fb-8ce1-6ca12dece45c | -12.8359 | -44.3422 | 2026-07-01 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 273.0 |
| 5fa7cf60-e32a-370f-a3d2-3e37e1b5b32d | -10.9205 | -43.0622 | 2026-07-01 06:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| f43c610c-6465-3097-a0e1-6a3f2a9a4fb8 | -12.8548 | -44.3625 | 2026-07-01 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 3a379b19-d370-3e41-ac58-7e1fc3ddbe3a | -12.8359 | -44.3422 | 2026-07-01 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 271.6 |
| be1df986-ca89-3240-a7cb-4eba354dda2e | -12.8363 | -44.3186 | 2026-07-01 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 0621381e-eb60-388f-bee5-7e97c20591b1 | -12.8552 | -44.3389 | 2026-07-01 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| ca9b6874-8b25-3ba2-b2c4-84c06eab9869 | -12.7557 | -44.4959 | 2026-07-01 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 06e1dd7c-92c0-3ee9-9030-d234383cd4a2 | -12.8354 | -44.3657 | 2026-07-01 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 0af679fd-ab73-32ce-98b9-80435cfe9407 | -10.6787 | -54.5153 | 2026-07-01 06:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 8607eaff-ece9-39f2-a562-d1a7c8717530 | -10.6598 | -54.5169 | 2026-07-01 06:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| c4450316-71cf-3d9e-bcdf-6f8f2fbbe1ec | -12.7751 | -44.4927 | 2026-07-01 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 267.0 |
| 0cff3913-47e3-3c88-a9a2-eb82f958c32b | -11.4338 | -56.0509 | 2026-07-01 06:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| b7a247af-aeb6-331e-b536-2483d8fc2f33 | -10.9209 | -43.0384 | 2026-07-01 06:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 8869b4b7-c904-3504-aae0-fa0d0bcceff7 | -10.6784 | -54.5356 | 2026-07-01 06:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| fe2fb7ac-ee0a-30bb-9be3-4ea158ee7401 | -12.7755 | -44.4693 | 2026-07-01 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 146.6 |
| 8e7b1453-1398-361d-bcd5-6ddb9b2f1332 | -11.4336 | -56.0711 | 2026-07-01 06:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| a7db8247-de62-30ec-ba4a-269b72246c49 | -12.7562 | -44.4724 | 2026-07-01 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 78ae76e3-1cf9-3125-b3dd-04310f19e354 | -9.07508 | -65.42386 | 2026-07-01 06:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73e1d0b1-b86c-3d73-8a69-240d8e581730 | -9.09103 | -59.49791 | 2026-07-01 06:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbee3e41-ebe8-38c3-bc36-790e5aefeddb | -9.07971 | -65.42454 | 2026-07-01 06:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31bdf404-6a77-3c19-a5ba-8d9b9faa1878 | -9.03004 | -59.53813 | 2026-07-01 06:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e86b9985-f3c9-3e93-8d5f-56fdb8866b1c | -9.02325 | -59.53713 | 2026-07-01 06:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 66ecde08-6ca5-39d3-981d-734fc842a9e6 | -9.3754 | -65.77638 | 2026-07-01 06:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5908d801-8e04-3025-84bc-93fa5a130938 | -9.08422 | -59.49685 | 2026-07-01 06:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab352b5d-23c2-3678-b8a1-aedb95f40f21 | -9.08402 | -59.49464 | 2026-07-01 06:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c2d70e0-f292-3007-a35f-dd5851adeb56 | -9.08497 | -59.4907 | 2026-07-01 06:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a83d9a6-d9e2-3295-9429-47e52fad619b | -9.02928 | -59.54424 | 2026-07-01 06:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de2aa331-6806-3075-947f-c10df253cd39 | -9.09082 | -59.49569 | 2026-07-01 06:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 063848c7-0621-3509-89ef-918a8451607f | -12.8548 | -44.3625 | 2026-07-01 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 57c589e2-b628-36bb-90b0-ec2050447c9f | -12.8552 | -44.3389 | 2026-07-01 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 4da6fbc9-b72f-33c2-b8df-0a9a77779236 | -10.6596 | -54.5372 | 2026-07-01 06:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| e690cc78-5710-328b-b8c7-1eb84c6cd39d | -12.7557 | -44.4959 | 2026-07-01 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 115.8 |
| d946f16a-8448-30ba-b776-2b47eb433339 | -12.7755 | -44.4693 | 2026-07-01 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 113.4 |
| a1e31150-cb13-3542-bffc-90f0a4d5ae88 | -10.9209 | -43.0384 | 2026-07-01 06:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 5cc10a4b-c858-3bff-a71f-03c788b485d5 | -12.8165 | -44.3454 | 2026-07-01 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 43.4 |
| a2352fc8-3e70-3ab6-89c4-79deb0b8b056 | -12.8359 | -44.3422 | 2026-07-01 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 241.2 |
| 73245e03-f4a5-38a9-8262-3a9cdc62e0ec | -12.8354 | -44.3657 | 2026-07-01 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 57099076-573f-372d-a550-c8ce8496cb6f | -10.6787 | -54.5153 | 2026-07-01 06:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 758e1f63-20fe-3659-beb2-3857c500fb14 | -10.6598 | -54.5169 | 2026-07-01 06:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 9cc08a85-4c51-3213-b859-1544b1f503c2 | -12.7751 | -44.4927 | 2026-07-01 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 182.5 |
| b3229649-9e21-31cd-94fe-91a3dae7b557 | -10.6784 | -54.5356 | 2026-07-01 06:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 149e4308-9c6b-3cb8-8378-d6d3d2a52825 | -10.9205 | -43.0622 | 2026-07-01 06:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| c3400686-fc95-3c99-a411-4bb6f122230d | -12.7562 | -44.4724 | 2026-07-01 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| de3d55d2-8af8-317b-a7ed-6b62573ada8a | -11.62495 | -59.01603 | 2026-07-01 06:20:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6057f38f-c9c5-3237-83cf-3de3e7114bc9 | -11.63218 | -59.01684 | 2026-07-01 06:20:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bc4d0666-869d-3c65-97d0-1a2e665bb233 | -11.62647 | -59.01395 | 2026-07-01 06:20:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fd6d3605-b5a9-3cad-bb8d-1de6584bf4c7 | -11.63295 | -59.02184 | 2026-07-01 06:20:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b4029515-582b-35a6-bdfc-71445941452c | -11.62571 | -59.02107 | 2026-07-01 06:20:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a4539057-0766-3fc2-95b4-ac79323bf2cb | -11.63139 | -59.02385 | 2026-07-01 06:20:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9054e879-cf60-3f0a-8666-c57f23ea9b32 | -11.62416 | -59.02311 | 2026-07-01 06:20:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ac23e301-86e0-3acd-8adb-5faf5b541597 | -11.6337 | -59.01484 | 2026-07-01 06:20:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 83e2b629-bf5d-34f1-99d0-28aed6286d76 | -10.6598 | -54.5169 | 2026-07-01 06:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 500280d3-9d12-375e-8cae-5d7a83d1d0fc | -12.7751 | -44.4927 | 2026-07-01 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 186.5 |
| d488c443-1b99-3ccd-bbdf-26df5356386a | -12.7755 | -44.4693 | 2026-07-01 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| c8bd4c58-ca76-39cb-9b66-df15c2185ee7 | -10.6787 | -54.5153 | 2026-07-01 06:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 31aeae08-7cbc-3a6b-a64d-72d3c5a0b86a | -10.6784 | -54.5356 | 2026-07-01 06:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 7de5febf-e0a1-3af7-bebc-dac6fc7d7fbe | -12.8354 | -44.3657 | 2026-07-01 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| a4738d24-adf6-359a-838d-5114f9729808 | -12.7557 | -44.4959 | 2026-07-01 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 015102f4-4940-3e8f-ae61-50774244136b | -10.9205 | -43.0622 | 2026-07-01 06:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 55a2ecfe-a46a-33b4-90d1-f187304bfc69 | -10.9401 | -43.0355 | 2026-07-01 06:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 429d5c96-f9d8-35ab-a100-752e38976a97 | -12.8359 | -44.3422 | 2026-07-01 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 213.3 |
| 34ff7ebf-2f97-37dc-8bf6-74022cc8b6ea | -12.8548 | -44.3625 | 2026-07-01 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 60.0 |
| e28fd841-8be3-390d-bdf8-a226b07aa12b | -12.7562 | -44.4724 | 2026-07-01 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 2fb41abe-44a3-39f3-b5be-d587b2591509 | -10.9397 | -43.0593 | 2026-07-01 06:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| fe7a11bd-9f5a-387f-b825-614586939c18 | -10.9209 | -43.0384 | 2026-07-01 06:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 986fe98b-4307-3c14-a7fa-f93c3814c15b | -12.8552 | -44.3389 | 2026-07-01 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 3b4ae2a3-826d-3c1e-b34a-19b728667566 | -10.9205 | -43.0622 | 2026-07-01 06:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| d4814fd9-6a9b-3b7d-9288-d7a77c24f81e | -10.6787 | -54.5153 | 2026-07-01 06:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 6a387a1d-b4c9-3298-a327-4c77c3881c40 | -12.8354 | -44.3657 | 2026-07-01 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 652aa629-954f-39eb-a6f4-98bfe2d9855d | -12.7755 | -44.4693 | 2026-07-01 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 48c6bc4d-e09a-3988-87ec-2edd057dcdcc | -12.8548 | -44.3625 | 2026-07-01 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 64efecdf-d995-3dda-9154-0f557515d607 | -12.8359 | -44.3422 | 2026-07-01 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 184.2 |
| a6e6767f-c177-3c35-a19b-5753ed10dccb | -10.6784 | -54.5356 | 2026-07-01 06:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 95561ee1-3116-397f-8f68-eed2674397a1 | -12.8552 | -44.3389 | 2026-07-01 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 123.7 |
| c80a0937-ade8-3e49-8711-c9c442a9dfbd | -12.7751 | -44.4927 | 2026-07-01 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 168.8 |
| 8ed9bc4c-188e-3574-8d86-64706e36a815 | -10.9209 | -43.0384 | 2026-07-01 06:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| f0e5360c-b4c7-3f4b-b076-07c6698e43d9 | -10.9397 | -43.0593 | 2026-07-01 06:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 4e51fe2f-29da-34d4-b3dd-19ec305e44b0 | -12.7557 | -44.4959 | 2026-07-01 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 69346e16-04cd-30cf-83bb-26dd9495f3fb | -12.7562 | -44.4724 | 2026-07-01 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 9c5b44ee-3c2f-34c1-95bb-660ba31c39e4 | -12.8552 | -44.3389 | 2026-07-01 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 91689442-7f7f-3155-89cc-193b59d261ca | -12.8359 | -44.3422 | 2026-07-01 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 199.3 |
| 4847c298-1ba0-38d3-935e-4baad241eead | -10.6784 | -54.5356 | 2026-07-01 06:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 0ae07555-4303-302d-bbce-3f6c44964aac | -12.8354 | -44.3657 | 2026-07-01 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 6b589da1-0a18-3a5b-b8fd-4be77f80f286 | -10.6787 | -54.5153 | 2026-07-01 06:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 693c7108-8bdd-3e84-84cd-8919e56fac6d | -12.8548 | -44.3625 | 2026-07-01 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 6f14d199-e525-3f0b-81be-53d378fc916e | -12.7557 | -44.4959 | 2026-07-01 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 827013b0-db3b-37be-ae66-967a82ebe3dc | -10.9209 | -43.0384 | 2026-07-01 06:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| a262ad61-5d89-38d9-86fb-2760a86bb72c | -12.7755 | -44.4693 | 2026-07-01 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 1439c938-00f4-37de-933f-673d212ca0d6 | -12.7751 | -44.4927 | 2026-07-01 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 158.4 |
| 1811a9e5-789d-3a63-ae31-685861b9e3eb | -10.9205 | -43.0622 | 2026-07-01 06:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 6ed0477b-c041-34e9-a487-fc0614e99fb8 | -12.7562 | -44.4724 | 2026-07-01 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.6 |
| a0a7511b-fd55-373f-89f1-bdf75bb4c23d | -12.7755 | -44.4693 | 2026-07-01 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 333e6290-ebee-3e50-a443-03a848c7fbc4 | -10.6784 | -54.5356 | 2026-07-01 07:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 1426a1fb-e191-3eaa-88ba-243e1b60bfc7 | -12.8354 | -44.3657 | 2026-07-01 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| c2523f4f-747e-35ac-b4c0-dd4e35651836 | -10.9209 | -43.0384 | 2026-07-01 07:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 3d75f1af-8529-39fc-b2bd-e807633014f3 | -12.8548 | -44.3625 | 2026-07-01 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 04f8cedf-5309-3541-8d52-7297aab8443b | -10.9205 | -43.0622 | 2026-07-01 07:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 0f3f81a2-0564-355f-8f93-781b0fc28e11 | -12.7751 | -44.4927 | 2026-07-01 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 163.8 |
| 30f2e2a9-3211-3bd1-b7f3-2182f8384eff | -12.7562 | -44.4724 | 2026-07-01 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 44.7 |


[Clique aqui para ver as próximas entradas](README31.md)
