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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c660f82-cd45-3492-a4f5-6dcdfa109fb6 | -16.33247 | -51.53369 | 2025-09-13 06:48:00 | AQUA_M-M | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 86dbf1ab-9bf7-36d3-987e-14e4eed69fd0 | -9.5324 | -54.6277 | 2025-09-13 06:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 9bd28040-d523-35b4-a03c-0e2f2339ba97 | -18.0502 | -50.935 | 2025-09-13 06:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 40ae0e95-4ab1-3a9d-84e0-1d26e980fcb5 | -14.1898 | -46.2472 | 2025-09-13 06:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 197ceda8-e111-3ab3-a199-0d9a1ebd10fc | -14.1703 | -46.2505 | 2025-09-13 06:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 85a3b042-d3ee-35d5-8977-19ae547db0ac | -18.0298 | -50.9606 | 2025-09-13 06:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 72.8 |
| cd83aded-e137-3f5f-9358-498282c7f9ff | -9.2844 | -59.3986 | 2025-09-13 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.2 |
| cef1392e-557c-3a47-a0a8-5a2e70c2e47d | -11.114 | -51.4057 | 2025-09-13 06:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 102.6 |
| e0a3f9c2-a20d-33a9-8038-d9795095f7b1 | -9.2315 | -51.2488 | 2025-09-13 06:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| e0bef307-c2b0-3639-bbde-483eb13615e3 | -11.0948 | -51.4289 | 2025-09-13 06:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 108.6 |
| c1d7b066-0df1-3033-ae4f-749a4f0fafc6 | -9.5137 | -54.6292 | 2025-09-13 06:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 6f6fa4d8-36a3-3c3b-8d21-c4906b0e9179 | -14.4584 | -47.34 | 2025-09-13 06:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 4e537f36-0de5-32fb-b51c-d548be2b57a4 | -15.7815 | -52.25 | 2025-09-13 06:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 7f837077-e009-3b17-988a-5cf487c2aab6 | -11.1426 | -50.7028 | 2025-09-13 06:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 38e1e691-9f7e-3626-b145-cd4782b0ac4d | -15.4517 | -47.3291 | 2025-09-13 06:50:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 60.4 |
| fad56f53-7112-33bc-b37f-90e2c84b2c27 | -14.1698 | -46.2735 | 2025-09-13 06:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 165.2 |
| a371c97e-708c-3086-a210-42a3fc948534 | -9.2658 | -59.3997 | 2025-09-13 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 135.3 |
| ebc00c6c-6775-3589-8268-d9ad8874d2fb | -11.1616 | -50.7008 | 2025-09-13 06:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 226.3 |
| eaf82576-8cb8-37f2-9ad4-d9376d473f9c | -9.2656 | -59.4191 | 2025-09-13 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 117.9 |
| 38216c89-dea2-3b74-a65c-430719e78292 | -15.4713 | -47.3256 | 2025-09-13 06:50:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 38d9d28a-425f-3749-bdf9-d74407c3dca1 | -12.006 | -47.7505 | 2025-09-13 06:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 95746c47-9f61-3438-b04a-c52d54a42213 | -14.2088 | -46.2669 | 2025-09-13 06:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 64.5 |
| df678bfe-e664-3e5a-9bb3-307888879013 | -9.2843 | -59.418 | 2025-09-13 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 6fade56e-7b86-3997-a8d6-e50a8c8fab45 | -14.1893 | -46.2702 | 2025-09-13 06:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 0ff552f1-0411-34ef-b2f2-39bda25b725f | -11.095 | -51.4077 | 2025-09-13 06:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 149.7 |
| 825bbd88-1658-3ccb-8755-39de7c73a095 | -11.885 | -50.5768 | 2025-09-13 06:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| d8b8226a-2e99-3274-8dc6-7b0b5fb19dbf | -18.0303 | -50.9385 | 2025-09-13 06:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 172.8 |
| 0b3515ac-53c9-3d8a-b946-991451a8185f | -11.1806 | -50.6987 | 2025-09-13 06:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| ceb5bdd2-a0e7-3380-94f0-3f7247ebf8bd | -9.2844 | -59.3986 | 2025-09-13 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 277b9ed8-751a-3a37-ae9f-1185f22b02ac | -18.0303 | -50.9385 | 2025-09-13 07:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 230.1 |
| b8e80438-2cc8-38d2-88ea-be9782cfd609 | -14.1893 | -46.2702 | 2025-09-13 07:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 62f13dd4-6a60-3d76-9435-440144c38300 | -14.4584 | -47.34 | 2025-09-13 07:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 018d9df9-9e87-3fa1-8b51-34fee99c34ef | -11.7575 | -46.6205 | 2025-09-13 07:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 30f3f495-8fee-3155-919f-b78b37de71d0 | -9.2656 | -59.4191 | 2025-09-13 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 102.0 |
| edc051fa-6d8d-3d3a-9cf8-a90bc1612b1a | -14.1698 | -46.2735 | 2025-09-13 07:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 83505f1c-75c7-35a7-bbe9-25192b7571a6 | -9.5324 | -54.6277 | 2025-09-13 07:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 302f17b7-087e-3f14-91ad-31f044f5156b | -14.1898 | -46.2472 | 2025-09-13 07:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 9e1bc409-a467-3bef-9525-183174bb01a9 | -9.2315 | -51.2488 | 2025-09-13 07:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 94a554aa-b6c8-378c-85db-1e44254553ec | -11.0948 | -51.4289 | 2025-09-13 07:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 1d3ca7a9-92ff-3123-b953-fc58f8a48fc1 | -11.114 | -51.4057 | 2025-09-13 07:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 1edc1c56-8e53-379d-a718-81754f7b95c3 | -9.2658 | -59.3997 | 2025-09-13 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 132.1 |
| fb9e52fa-e2be-3158-bae7-a554aba46004 | -18.0502 | -50.935 | 2025-09-13 07:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 1bc5d32a-1293-3d01-8375-55c615ede092 | -9.5137 | -54.6292 | 2025-09-13 07:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| b9102e7f-f060-30a8-8525-2553f74efe55 | -9.2843 | -59.418 | 2025-09-13 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 377a1785-fb9e-3bfe-bcfa-634460b86dd2 | -9.2503 | -51.2472 | 2025-09-13 07:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 8340034f-7782-3276-bf78-4436f59d0864 | -14.2088 | -46.2669 | 2025-09-13 07:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 08062dd5-0309-3ebe-b463-522957b67b48 | -15.4713 | -47.3256 | 2025-09-13 07:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 77.7 |
| d91d47f8-5bbc-38cb-94e8-16a75741b1af | -18.0298 | -50.9606 | 2025-09-13 07:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 106.9 |
| cacf17f6-155c-3d2d-8cd3-d4470a6dc7c0 | -9.5006 | -55.9588 | 2025-09-13 07:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 1083b940-2aac-3ab7-aed2-bf6939ded3ba | -11.1616 | -50.7008 | 2025-09-13 07:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 128.5 |
| f5ef9e77-3488-305b-bdc9-149bb2ac74b0 | -14.1703 | -46.2505 | 2025-09-13 07:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 9cf3d73e-be36-3b70-a6f3-1ff75f65f0df | -11.7571 | -46.6431 | 2025-09-13 07:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 76da7aaa-613f-3aea-a473-fb6a854c658f | -15.4517 | -47.3291 | 2025-09-13 07:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 689b7299-68fc-39ce-b479-006a8199a0ff | -11.095 | -51.4077 | 2025-09-13 07:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 159.9 |
| 62847d1e-4d93-317b-bf98-82de367308f4 | -9.5006 | -55.9588 | 2025-09-13 07:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 3e56587a-4a13-3b59-b8af-a77dd3c4312b | -11.114 | -51.4057 | 2025-09-13 07:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 150.9 |
| 3f2b8377-8ed7-3983-bf82-5c17a5cfde47 | -11.0948 | -51.4289 | 2025-09-13 07:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 685c9081-7332-31c3-b984-6b866e6a34a3 | -9.2658 | -59.3997 | 2025-09-13 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 7b4049b3-9048-37d5-ae8e-e8bd5b0e6153 | -18.0298 | -50.9606 | 2025-09-13 07:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 200.5 |
| 9a7939ae-9a9f-3c96-8f51-7a909d468909 | -14.2088 | -46.2669 | 2025-09-13 07:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 6d833293-92ea-355c-bdbd-7ce85111ce9f | -9.2503 | -51.2472 | 2025-09-13 07:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 466aef25-ae81-3f1b-8d0f-601eed746ee6 | -9.5137 | -54.6292 | 2025-09-13 07:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| f59dd374-9749-34df-af6d-7a823d855899 | -9.2317 | -51.2278 | 2025-09-13 07:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| e168489a-c55a-3496-a4a2-756b243a447a | -14.4394 | -47.3206 | 2025-09-13 07:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 2bfa11c7-72cf-3d06-922e-708861b0eed8 | -15.4713 | -47.3256 | 2025-09-13 07:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 57.8 |
| f5e7e281-4efc-336a-af78-1d96ec37b69a | -9.2315 | -51.2488 | 2025-09-13 07:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 05709e34-9097-3eca-8851-20ae88001803 | -11.7571 | -46.6431 | 2025-09-13 07:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 12bef707-89a8-3ddb-ae3a-4148507e5d0f | -18.0303 | -50.9385 | 2025-09-13 07:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 427.8 |
| 3bca1b93-54ca-3f0a-bc0f-623b1d88ac87 | -11.095 | -51.4077 | 2025-09-13 07:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 225.1 |
| 81bc57c4-b39a-35fe-8908-6d869a0f17e6 | -9.2656 | -59.4191 | 2025-09-13 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 21927daa-1f47-36d0-b349-24d1f8b423d6 | -11.7391 | -46.5779 | 2025-09-13 07:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 0b3936c1-18fb-3232-9520-a3cb82c29bbe | -14.1893 | -46.2702 | 2025-09-13 07:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 154.5 |
| a6042852-b69e-352d-8b4a-a24d7fab5735 | -15.4517 | -47.3291 | 2025-09-13 07:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 0d67848d-50e2-38ed-984e-699f4e031cba | -14.1898 | -46.2472 | 2025-09-13 07:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 57162b60-2d56-3672-8afd-1bd5c72a64b4 | -18.0497 | -50.9571 | 2025-09-13 07:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 81.1 |
| fd8d40d1-b33a-34d1-9d01-ade23d0ee1d8 | -18.0502 | -50.935 | 2025-09-13 07:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 154.3 |
| ebb8e7e8-8978-3a92-b388-aeb69eda6611 | -14.1703 | -46.2505 | 2025-09-13 07:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 171.3 |
| e8178b1f-922a-3ce7-a103-3f26f23d6c96 | -14.1698 | -46.2735 | 2025-09-13 07:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 182.5 |
| 6bb331f4-c7f8-3c8f-be83-c4ccdc349ea6 | -18.0308 | -50.9164 | 2025-09-13 07:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 64.0 |
| b9589a9e-dd3d-36f0-8f4e-029791697044 | -9.5324 | -54.6277 | 2025-09-13 07:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 9848b7c4-51dc-3e79-b575-4cc17a5d612d | -11.1616 | -50.7008 | 2025-09-13 07:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 53461ee8-0635-3d73-b614-c8107ae621c5 | -18.0502 | -50.935 | 2025-09-13 07:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 202.9 |
| 4865d0fe-d96c-3b0a-9cfa-93b1feff2b99 | -11.095 | -51.4077 | 2025-09-13 07:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 229.1 |
| 1e0ab294-bb9b-3c49-9885-a6eb4c8316cb | -9.2656 | -59.4191 | 2025-09-13 07:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| fc02eb95-00bd-3ea1-bb5a-e59677c3273c | -9.2658 | -59.3997 | 2025-09-13 07:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 93c0bc3a-42f4-3fe5-9a72-dbbed7c10cb4 | -9.5137 | -54.6292 | 2025-09-13 07:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 14cdba3f-2d71-3ab7-94d5-c1fa65a3d3a0 | -18.0303 | -50.9385 | 2025-09-13 07:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 597.9 |
| 79c76dbc-7e85-3d9d-8ed0-3987e107cbda | -11.0953 | -51.3866 | 2025-09-13 07:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| e0c0488a-9d5b-32bd-8df7-427db3147b2e | -9.5324 | -54.6277 | 2025-09-13 07:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| da30ae47-b279-391a-b2a1-141deafee5b6 | -11.0948 | -51.4289 | 2025-09-13 07:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 80b6e43f-bb70-3f60-899f-fe133da161c7 | -18.0308 | -50.9164 | 2025-09-13 07:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 94.1 |
| dd40d980-58ab-3925-8d55-c9ef07047550 | -11.114 | -51.4057 | 2025-09-13 07:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 259.5 |
| 56307e28-c847-3b62-a4a9-4cdafbf35140 | -14.1698 | -46.2735 | 2025-09-13 07:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 93e245eb-16b2-3c99-b617-a18845da8cb5 | -9.2315 | -51.2488 | 2025-09-13 07:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| cc297f1c-9c86-3165-8dc1-ef404c5e3af1 | -14.4394 | -47.3206 | 2025-09-13 07:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 58.4 |
| e091d165-1108-35ea-9914-b05f6b5f8f4f | -18.0497 | -50.9571 | 2025-09-13 07:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 126.9 |
| a73527c1-aaa9-3ac0-bccd-b8c2e07419fc | -18.0298 | -50.9606 | 2025-09-13 07:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 352.7 |
| 56c4ea6b-7dc0-36b2-b9c5-01dda26e875f | -15.7815 | -52.25 | 2025-09-13 07:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 490873c5-266d-3fa6-9f7e-1ecb7c7cc108 | -12.006 | -47.7505 | 2025-09-13 07:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| a74bc165-1e12-36f1-9274-8521dcccd7ee | -14.1703 | -46.2505 | 2025-09-13 07:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 195.9 |


[Clique aqui para ver as próximas entradas](README118.md)
