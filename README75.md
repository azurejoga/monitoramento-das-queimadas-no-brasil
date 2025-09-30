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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e9c3b8a-30d7-32b8-bc94-5899fccbce08 | -14.54304 | -48.26033 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 12d72afb-9eb3-33b5-a690-122f89038789 | -14.57904 | -48.28078 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1df03e18-be34-3d5c-86ae-e9efdc75bf94 | -19.59866 | -45.88681 | 2025-09-30 04:42:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4f3f4dd-f785-3e38-a7bf-1669f08b1ab7 | -14.53683 | -48.37922 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2aab73a7-22ed-3edd-95d1-b2d1ff3cf674 | -15.38811 | -47.0789 | 2025-09-30 04:42:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1a9a5d59-4494-3899-8b35-4ee89ec4ec31 | -14.51302 | -48.41811 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9070d790-4d91-3d46-895b-2dae4b019eb1 | -20.61361 | -46.19217 | 2025-09-30 04:42:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ce450a8-0860-380a-b2f4-fd5ddeee03c6 | -15.86277 | -46.2336 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eeb14f3e-4209-3723-a740-a944ec37b90b | -14.66785 | -48.14655 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b3510160-8db0-375c-87af-1932bb4026e5 | -14.78608 | -48.30751 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 539171fb-0983-339c-af6c-74df1160ffc0 | -16.41269 | -52.1734 | 2025-09-30 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ba5f53d1-353f-354f-a802-53a5c77022d7 | -17.50313 | -43.47256 | 2025-09-30 04:42:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8490de4-a524-3baf-88ad-14b0cd3a2313 | -16.42556 | -47.03312 | 2025-09-30 04:42:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d765bf01-578d-3263-bfe4-e262604be2bb | -14.52908 | -48.38249 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c17bba4e-e13a-34d8-ad97-4adca63f0626 | -18.31934 | -41.75013 | 2025-09-30 04:42:00 | NOAA-21 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9c8c16f5-5043-3206-a700-3ff5cebdf8f2 | -15.80534 | -59.51822 | 2025-09-30 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 80ca9560-9869-303e-84fe-9e231ed89123 | -14.58794 | -48.19089 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fc5271fb-4e19-32c7-8e22-b6a154e3ddc4 | -15.25762 | -49.7207 | 2025-09-30 04:42:00 | NOAA-21 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3001f2b8-7353-389e-935e-2b7af8cbb47d | -17.4739 | -46.2033 | 2025-09-30 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 488148fe-d279-3445-b1db-67863bb3b0b4 | -17.10315 | -48.57301 | 2025-09-30 04:42:00 | NOAA-21 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cac00ffe-491a-379b-871b-4db5ae2412ee | -14.52541 | -48.43294 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a342fd0e-74f1-3881-a279-d86313f88fa1 | -15.28246 | -48.02898 | 2025-09-30 04:42:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff25b501-6140-3047-85fc-288b92babfd0 | -14.60948 | -48.29831 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b285161-a031-3480-975c-552ab45f7dcb | -16.7458 | -44.92276 | 2025-09-30 04:42:00 | NOAA-21 | IBIAÍ | MINAS GERAIS | Brasil | 3129608 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 65e2cbda-967e-3c85-96bb-ac122b7136a4 | -14.555 | -48.25359 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4076688d-f1ba-3cd3-aed0-d65a34ff505e | -14.53237 | -48.48485 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dff7431e-0854-3ba4-a1bb-617afa12e180 | -15.33461 | -47.92342 | 2025-09-30 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7bff6533-0460-3da4-84c5-ed959b01c322 | -17.17374 | -42.83606 | 2025-09-30 04:42:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| db6f8657-f483-30ef-a485-9835c64aea01 | -15.77355 | -43.675 | 2025-09-30 04:42:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b54d58aa-bb8e-31b1-9009-1ab806dc8e3b | -15.25098 | -48.74089 | 2025-09-30 04:42:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3bbb8620-c076-30de-9762-048a68982839 | -15.79058 | -46.59982 | 2025-09-30 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6aaceaa5-c1a1-3c15-85a0-9ffec756192a | -14.51482 | -48.40562 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 396a6d72-861f-3cb6-a7cd-393b50a88c5c | -15.27508 | -47.89203 | 2025-09-30 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 25668aaa-2f9e-37f1-a224-0e8e9d02253a | -15.28428 | -47.85226 | 2025-09-30 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0cbcd737-642c-3afb-a8a3-1952219d9eb1 | -15.17271 | -46.40608 | 2025-09-30 04:42:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a2cc304d-9667-3f3a-8faf-0a78c577387c | -15.20907 | -50.11773 | 2025-09-30 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d5ed7f89-f87b-3e18-9392-9261c6936788 | -16.27625 | -52.53791 | 2025-09-30 04:42:00 | NOAA-21 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42fe8c3a-c57a-389d-a2f8-bebb524e0a83 | -15.32822 | -46.26294 | 2025-09-30 04:42:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e09d0c8f-4a38-3ebf-813c-8459b1f2585d | -15.60489 | -47.82469 | 2025-09-30 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98d200bc-6432-32b6-8e8d-0a2b04a3cf63 | -15.33464 | -56.63853 | 2025-09-30 04:42:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7cc3ac2b-2189-3595-9b81-8c6cca000a95 | -14.57557 | -48.21278 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8477f87f-39d9-3a18-91ce-d8820ae0709e | -14.65253 | -46.9684 | 2025-09-30 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd6333cf-bf29-3c46-9cbd-14af552b7b3c | -18.47483 | -44.02296 | 2025-09-30 04:42:00 | NOAA-21 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| d5476f93-70f4-33ac-b703-4329482b7304 | -14.55379 | -48.26198 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ade3f74e-5f05-357a-a89d-a849eb9e2024 | -14.51659 | -48.39334 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 709c3602-3d68-3871-a869-dd8e684cf068 | -15.25146 | -56.79396 | 2025-09-30 04:42:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac24efbc-076e-337d-89af-fc13ba6a9a2f | -17.90147 | -57.59454 | 2025-09-30 04:42:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| eadd773b-9d0b-34b7-a26a-3dee93dbd63d | -18.12315 | -42.19537 | 2025-09-30 04:42:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 98e648c2-500c-3187-a8d7-81d10e3fd314 | -14.52481 | -48.43707 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7d53781a-8903-3108-a3f1-23bca1eb0b08 | -17.39445 | -47.14572 | 2025-09-30 04:42:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6e46b6ae-1a28-33d5-a700-2019fdd47e42 | -14.65151 | -46.96074 | 2025-09-30 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a9118563-1f92-309c-aa7e-11b52d9557ce | -19.59943 | -43.82116 | 2025-09-30 04:42:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 097a10ca-06c0-31b3-94e8-1d580bb9e42b | -15.28415 | -47.85946 | 2025-09-30 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e1206816-a458-3483-b03e-fc093ee7af05 | -15.89302 | -57.49574 | 2025-09-30 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 61a57e90-f9fd-3257-83d9-7a0a48532bb7 | -15.9306 | -48.12003 | 2025-09-30 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 08031df9-f513-338c-bba8-5de100ecd350 | -16.22514 | -52.2819 | 2025-09-30 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4707d22d-39e0-3906-9bff-30cfa56ef7b2 | -15.25542 | -56.79508 | 2025-09-30 04:42:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4ee700c-b076-33e9-ba97-15b8f13cf6ed | -14.5106 | -48.46001 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7cdf21f1-ec6e-3881-9752-a6788b6798c4 | -14.64937 | -46.96291 | 2025-09-30 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| fc606a32-c214-3721-9aa3-047c3cf8e1e3 | -15.79 | -50.32538 | 2025-09-30 04:42:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8cfc3058-37a2-31c8-8cd7-6ba205aa98e2 | -14.64483 | -46.96728 | 2025-09-30 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| abc038b6-039c-3041-b781-508ff4327719 | -14.54357 | -48.48259 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0c9dea43-9b00-3542-b34f-4474d4c4d470 | -16.36693 | -49.12519 | 2025-09-30 04:42:00 | NOAA-21 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a1066ade-8022-3f50-90ac-db6e24b1c624 | -14.79683 | -48.29954 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 124e9741-2f9a-34e5-ae9e-b596f4c1fe66 | -14.2801 | -52.94506 | 2025-09-30 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 70af2731-b8e5-3143-a3e0-62c5d836ca1f | -14.747 | -45.66298 | 2025-09-30 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 830557b1-b509-34ef-a526-974cbc6f7ac5 | -20.06094 | -46.79443 | 2025-09-30 04:42:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73037780-528f-395d-97fa-22046fb2f506 | -14.59935 | -48.29239 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 36da07cb-9703-31f1-ab7c-aefe43740336 | -14.57718 | -48.21545 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 75409497-9917-3014-8476-b3ee1322d654 | -17.72945 | -46.67494 | 2025-09-30 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d878626f-d4cd-3377-8bf2-e230fcb475e3 | -17.91085 | -57.5891 | 2025-09-30 04:42:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| ce476c38-fd51-33e6-91d8-7f67109ea0bf | -14.59153 | -48.19156 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a611dfed-6e2e-34a9-a056-9b285cad4163 | -15.29988 | -46.41569 | 2025-09-30 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a08e6afb-2722-342a-a574-259ad47c07e0 | -15.49841 | -48.55539 | 2025-09-30 04:42:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8f45caa-3844-3efd-9810-75f5d4e61eac | -15.33181 | -47.38639 | 2025-09-30 04:42:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 59cd9bb4-7f21-3384-9218-59406b331e3a | -14.78548 | -48.31165 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d6293bec-092b-3067-aebe-247f726e0c52 | -16.47728 | -46.04208 | 2025-09-30 04:42:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c534984-ad85-3ded-8885-611d16889e66 | -17.75564 | -51.34299 | 2025-09-30 04:42:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df2f9594-7225-3ca8-8ab3-84d7731b21b8 | -15.29503 | -56.78864 | 2025-09-30 04:42:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db9c31dc-3545-34b9-a48b-fd65c74c6503 | -15.23386 | -48.02844 | 2025-09-30 04:42:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8273732-10ad-342e-a6a3-b774f6b5efc8 | -15.37816 | -47.08091 | 2025-09-30 04:42:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17887e82-2573-3ad9-a41d-4ed75c8e0106 | -16.41457 | -43.12153 | 2025-09-30 04:42:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9ce1b1a-d42e-3190-80cb-a7f1dc456ef3 | -15.23252 | -50.09906 | 2025-09-30 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af5ea0b8-39a6-35b8-b203-06623c683e7d | -14.5532 | -48.26606 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f8f885cb-1de5-3263-a203-b202aa072cf7 | -15.92497 | -46.20565 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b0d011b7-d436-304b-8475-70b494a06038 | -15.24852 | -49.71166 | 2025-09-30 04:42:00 | NOAA-21 | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 21a21b15-5c79-32ae-9ed1-2f7c62d2100d | -14.71379 | -48.24925 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 89888d32-d1c1-3bb7-ae8e-a86a32440036 | -16.51919 | -46.02194 | 2025-09-30 04:42:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 04d2e4b8-ec55-349b-b529-e2679c62a54e | -14.79094 | -48.31531 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3af72233-35b5-34bc-a62f-d3139a8e1e0c | -15.28277 | -49.26427 | 2025-09-30 04:42:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d0e081cd-0bd6-3238-a716-55c86a89ba61 | -14.70306 | -48.24723 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| caf6dca1-027c-372c-9c38-a186e1a6d5f1 | -15.2345 | -48.02398 | 2025-09-30 04:42:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e5bfb26-fc4a-3070-bd9e-e817dc5cc0fc | -14.69585 | -48.14069 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cdb027be-696f-3dba-bae3-7bbc9ebe55c8 | -15.32468 | -43.80378 | 2025-09-30 04:42:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3053c726-30ed-3896-baa1-2f335d0719ec | -15.47036 | -47.94145 | 2025-09-30 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 92d1a528-10a0-3c48-ada9-63e91ee1f9b8 | -15.84903 | -46.243 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83fa65ba-5d0d-3828-bf1b-a544e1819ff0 | -20.61911 | -46.18314 | 2025-09-30 04:42:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ed296221-7bbd-30a3-bc67-ba59c4f92d34 | -15.23588 | -50.09964 | 2025-09-30 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56b415a3-346e-37a0-ad76-ccc300851709 | -17.70628 | -46.6652 | 2025-09-30 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f04dad29-0019-39be-9f79-c50abcb8645b | -14.56077 | -48.46204 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README76.md)
