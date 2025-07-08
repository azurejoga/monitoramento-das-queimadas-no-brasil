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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba7710d8-0221-3ded-b218-17e84ff6e40c | -9.22699 | -48.59839 | 2025-07-08 05:04:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d17087b8-4332-37e9-9103-c4afed41803a | -11.20196 | -49.00053 | 2025-07-08 05:04:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 717d9f22-7593-3200-a331-5157cf68ef13 | -10.81732 | -49.49557 | 2025-07-08 05:04:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af5feb40-db55-3fa1-80fc-b944ee62549d | -12.33342 | -49.32475 | 2025-07-08 05:04:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 797640e7-d3c0-30d4-9ac3-9d25afb6ea52 | -10.82957 | -54.0254 | 2025-07-08 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d489f19b-fcf4-3e72-a180-66b1c13afef6 | -9.35164 | -58.84542 | 2025-07-08 05:04:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd893d84-4981-3d33-ac84-99caee9223a9 | -13.02493 | -46.28784 | 2025-07-08 05:04:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a70fa5b-60b0-3baa-803e-c567c952fc36 | -11.84151 | -43.79676 | 2025-07-08 05:04:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 06301116-7bed-389c-91f5-46d22e322b20 | -10.41415 | -49.76526 | 2025-07-08 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 92a41cbb-ba47-3f6a-a571-b331d6f36863 | -10.96302 | -48.20764 | 2025-07-08 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dcb7f9b0-359d-3021-bbf2-ad829c0f5bfc | -10.64474 | -49.46914 | 2025-07-08 05:04:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e20e3e9c-8f2b-3c54-a2b0-d7bf0a408608 | -8.71354 | -50.00532 | 2025-07-08 05:04:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9cb0fe3-baff-39f0-8b7b-fc72100916f8 | -9.37283 | -48.95203 | 2025-07-08 05:04:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca531907-36f4-3a0a-8686-9078c250a532 | -10.62717 | -49.45632 | 2025-07-08 05:04:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7dc26ea2-d2f1-3406-a5f2-fb701e702c08 | -10.83183 | -54.02861 | 2025-07-08 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7c0b7ba-b521-3e63-b15e-b9bf6658a7bf | -12.9867 | -44.88464 | 2025-07-08 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd25cc9e-e624-3b5a-8cf2-33ce393c82c8 | -9.8102 | -48.25644 | 2025-07-08 05:04:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2876474f-4616-38b6-819f-0f315db820ab | -6.34477 | -46.36722 | 2025-07-08 05:04:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee4bf178-c08c-3d5a-94d4-24c3536fb1b0 | -11.43111 | -45.10667 | 2025-07-08 05:04:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 9f0aa440-81e7-3b7b-b0e8-e35e9f69e7bf | -10.63934 | -49.47356 | 2025-07-08 05:04:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d7fe8b51-911a-3c1c-81e0-876c32be18dc | -7.19339 | -43.12833 | 2025-07-08 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 971dffda-028a-3f81-8efa-23da8c2cd517 | -10.66948 | -56.54666 | 2025-07-08 05:04:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4df8f24f-f778-3c2e-b0bf-194d05893863 | -9.57014 | -62.26101 | 2025-07-08 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c3e55d2-6448-3a9d-a8db-609f07d6ae25 | -10.26495 | -46.64781 | 2025-07-08 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9f74f05e-4d89-3dda-9d91-3335b6aa522b | -13.0245 | -46.29179 | 2025-07-08 05:04:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21378436-f7f3-3a3b-901d-4b5fffbc7620 | -13.02169 | -46.29721 | 2025-07-08 05:04:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c84130c7-7853-3cdd-9f4e-9ced908805fb | -7.58238 | -45.22296 | 2025-07-08 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 564b0df3-2c18-30b2-9126-796d5ab7c0da | -10.57873 | -49.11966 | 2025-07-08 05:04:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| a013465f-c884-330c-af4b-28bfa4c26802 | -7.48618 | -43.93626 | 2025-07-08 05:04:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95143dda-6c40-3025-a141-08b31514798d | -6.66778 | -43.76984 | 2025-07-08 05:04:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c68e01d-8897-33d0-9e83-e187724b85ad | -7.19119 | -43.13359 | 2025-07-08 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 87295f63-be7d-3792-8cb5-c3a161abba71 | -6.88718 | -45.24245 | 2025-07-08 05:04:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77144016-3360-375f-8a83-029ffd7ccad2 | -6.33989 | -43.74722 | 2025-07-08 05:04:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7c1ed048-c42d-361f-aa53-5b0c8ce4249c | -7.20098 | -43.12315 | 2025-07-08 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e843c460-25fa-3345-836b-9eded2c6c5d6 | -10.82425 | -49.5533 | 2025-07-08 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac029c09-6246-3e18-8cc5-a2a1bdcbfe55 | -11.41839 | -45.10513 | 2025-07-08 05:04:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 0fdd46c8-65e9-312d-bf39-1d511499ddca | -13.04055 | -46.29277 | 2025-07-08 05:04:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7af608cb-cf27-35ef-95b3-30212c893bd4 | -9.21717 | -48.59699 | 2025-07-08 05:04:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1b3d59a5-ec09-364b-98fb-957c15a8991c | -9.3441 | -58.84811 | 2025-07-08 05:04:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 072bbab3-3b88-3baf-89a9-497b059cae7e | -6.68129 | -43.77015 | 2025-07-08 05:04:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5f12930-fd7e-38d8-8240-afde68d7ad13 | -7.30675 | -55.31013 | 2025-07-08 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 060ead50-c7ac-30a8-8cfd-e781574afc7e | -8.95943 | -47.27419 | 2025-07-08 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 747ead5a-5c83-32e6-a67a-2de125a8298a | -10.63796 | -49.44753 | 2025-07-08 05:04:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 395a8ca4-eae1-3bf2-930f-20a7c2dea242 | -10.94631 | -49.25422 | 2025-07-08 05:04:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d408225-0a61-30c5-bba7-64721498f51d | -11.43687 | -45.11262 | 2025-07-08 05:04:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 92d88fff-8979-3674-b985-db3b7ba52085 | -9.37694 | -48.95773 | 2025-07-08 05:04:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91c82ab3-9879-36e1-988b-1515248714ea | -10.97532 | -45.1139 | 2025-07-08 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 4b8becc8-71d2-3c62-9c1f-50a27a51cf39 | -10.83079 | -54.01727 | 2025-07-08 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 158c41e0-0334-3dd3-8a9b-c5081194e4fa | -10.62784 | -49.45124 | 2025-07-08 05:04:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 2c2cd5ba-66ab-36b4-ad3e-2853a70cfa5d | -11.43234 | -45.09626 | 2025-07-08 05:04:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6ff2297c-ef35-3f7b-9b66-7572fd9233a7 | -10.27061 | -46.64873 | 2025-07-08 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 440c799b-6638-3f05-bfcd-22269975aaf4 | -6.67504 | -43.76498 | 2025-07-08 05:04:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f5939be-c4b5-3ae5-9b6d-4a7069a3597e | -9.33781 | -58.84313 | 2025-07-08 05:04:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a32189a6-1f0b-31cf-9a5e-4ae234b199d0 | -9.22775 | -48.59291 | 2025-07-08 05:04:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 56b4e554-f2dd-395b-a8a3-ee3dfb6209ac | -9.22283 | -48.59229 | 2025-07-08 05:04:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 55ab66d6-1b30-336b-82f3-a6f280349362 | -10.63728 | -49.45267 | 2025-07-08 05:04:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 0cd49cf9-657e-334e-ba3b-61b3835d5201 | -10.64607 | -49.45908 | 2025-07-08 05:04:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| cca7ac8f-bd4c-3a93-972c-53b522a5d4eb | -10.95113 | -49.25483 | 2025-07-08 05:04:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 876e39c2-ee77-3661-9dc7-8ebdacdcc7b6 | -9.92628 | -59.90151 | 2025-07-08 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 521744ab-1025-33df-b878-87af1023641f | -7.91535 | -61.55722 | 2025-07-08 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abf78ae5-4d55-3fc2-8628-70dd98411fd8 | -7.24831 | -43.07909 | 2025-07-08 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| e7b84f3b-6a18-3769-bb85-8fe882bdcb72 | -6.8838 | -45.24363 | 2025-07-08 05:04:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 840f2c78-d274-3a6e-ba4c-b28893dfb817 | -10.23076 | -56.76643 | 2025-07-08 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08dfd2da-48c7-3d81-a7c4-a29452f1b55d | -7.57583 | -45.22617 | 2025-07-08 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 35bc952a-2dc9-3d4d-8f87-dfd4318d4480 | -7.09875 | -44.16233 | 2025-07-08 05:04:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9eecef28-54b8-3759-a8d9-19c93ce389c7 | -11.42475 | -45.10591 | 2025-07-08 05:04:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 8bd72a0e-c275-3dd7-93f7-52cc2c87ddcc | -6.67579 | -43.75924 | 2025-07-08 05:04:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90855cf0-fe8c-3d7d-b058-27d41b5fb794 | -9.22458 | -48.59375 | 2025-07-08 05:04:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| c8009d4a-5363-3df5-8155-496d3532df35 | -13.03732 | -46.28645 | 2025-07-08 05:04:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d74840b-d7f4-3edb-8041-603ef0df8442 | -8.95896 | -47.27767 | 2025-07-08 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7191923-fbc5-32ba-86b6-73e1cfcc2e23 | -6.73212 | -44.33512 | 2025-07-08 05:04:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2e71cea6-66cd-3c52-ac53-e495ed772c74 | -6.66823 | -43.76872 | 2025-07-08 05:04:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2547b47d-4ff9-3d6a-9227-88177a11cfe7 | -7.19038 | -43.13965 | 2025-07-08 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a0fc2678-67e1-33b8-b7b5-08797b9fd646 | -10.36462 | -48.72172 | 2025-07-08 05:04:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 025afe7f-c4c4-34ef-9779-d3e99cba3b65 | -11.20012 | -48.99826 | 2025-07-08 05:04:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2c28fed2-5699-37a7-8897-821b6907d0dc | -6.53283 | -43.54227 | 2025-07-08 05:04:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34667f2c-0fc6-3a62-bc00-07ab6991ef6f | -11.29325 | -45.27211 | 2025-07-08 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7dfce62b-b2c5-3444-8e18-ee43967a2766 | -11.32478 | -55.21482 | 2025-07-08 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf279cd0-ca34-3eee-96ca-8906c8d165e6 | -8.98464 | -49.1837 | 2025-07-08 05:04:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d4ed1fc-6c4c-3ec1-9003-0fb529bd46ad | -9.00925 | -48.72645 | 2025-07-08 05:04:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b314433-8dde-3f8b-9b06-71a25967547f | -9.34536 | -58.84044 | 2025-07-08 05:04:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38b06f73-bd99-38e6-acf1-cc8747d0cc3f | -10.35965 | -48.72115 | 2025-07-08 05:04:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 784a5cd9-3926-39ad-887b-5495b59b2d13 | -6.21173 | -55.62243 | 2025-07-08 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b6732af-63f8-34d6-a8d5-584c0fa5d88d | -9.71363 | -56.18652 | 2025-07-08 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 74e815e3-40b4-3fbc-ba0d-46879a35cade | -12.3341 | -49.31924 | 2025-07-08 05:04:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa14e2b7-4587-34cb-b2b8-7e6fa08c2d50 | -11.42414 | -45.11108 | 2025-07-08 05:04:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| e6702a4a-b5a7-3ee2-b3ce-3630c7b595a1 | -9.34127 | -58.8437 | 2025-07-08 05:04:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f306dd6-b991-3a3e-bd31-89f5348fa979 | -6.34033 | -43.7469 | 2025-07-08 05:04:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0d6b657c-d9e2-33f1-a1fc-affd1d15e677 | -10.04143 | -64.99139 | 2025-07-08 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53f2a9d5-7dff-3f5e-ad77-6792457a9d31 | -8.9585 | -47.28112 | 2025-07-08 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3149ebf1-f2b6-3bcb-8c3d-78542c9af7c2 | -9.21475 | -48.59231 | 2025-07-08 05:04:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d4e30312-eb72-3b5a-8c54-551db5e80796 | -10.83252 | -54.02999 | 2025-07-08 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31a14ec8-5661-3195-9cad-0c8b502419cd | -12.98606 | -44.89034 | 2025-07-08 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b47f8ba-93a9-3730-a603-e62be6955a84 | -10.64067 | -49.46348 | 2025-07-08 05:04:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 83d17cbe-3d2e-3390-a89b-0c2e470a216d | -10.89072 | -56.45655 | 2025-07-08 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7e4d7170-aa47-3a6f-993b-7a1441e06e52 | -7.228 | -49.59717 | 2025-07-08 05:04:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02dce1b5-e879-3550-82a3-104502232bf9 | -11.34825 | -55.40457 | 2025-07-08 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 893a1049-40c0-3eaa-a981-a69a96f939e9 | -10.97273 | -45.11185 | 2025-07-08 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a514b9e7-4d83-3fdc-a39f-081f6be00201 | -10.13094 | -57.77966 | 2025-07-08 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f5465b0-8732-3024-b11a-f24e6405efe4 | -5.73584 | -49.13637 | 2025-07-08 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README18.md)
