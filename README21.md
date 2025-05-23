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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec797124-3944-3bc9-93c0-169590beeb5a | -13.9818 | -56.0151 | 2025-05-23 06:40:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 8e705b65-5bd4-3c06-9be9-ca2121b80a38 | -6.2224 | -43.3693 | 2025-05-23 06:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| b13e1fbd-c250-32f4-a700-b663eaeba34f | -13.9818 | -56.0151 | 2025-05-23 06:50:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 48.8 |
| dc429258-b8d8-3993-b8a9-65cbdb92d4e9 | -6.2224 | -43.3693 | 2025-05-23 06:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| dbe0662e-bce0-3663-989a-2e07e87307b0 | -13.9818 | -56.0151 | 2025-05-23 07:00:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 47.0 |
| ffcec75a-52d7-384c-a9a9-2ae8f78d6c63 | -6.2224 | -43.3693 | 2025-05-23 07:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| b89ed44f-26cd-3b75-8b0a-1be121c4afad | -13.9818 | -56.0151 | 2025-05-23 07:10:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 42.7 |
| f7fd3856-655d-378b-9a52-1320646ec702 | -6.2224 | -43.3693 | 2025-05-23 07:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 16d05ab6-eeb1-3a87-ad8d-aaaf553c3afb | -13.9818 | -56.0151 | 2025-05-23 07:20:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 43.4 |
| f8d8bdf2-2689-3839-b65e-fe452b1a11ac | -6.2224 | -43.3693 | 2025-05-23 07:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| edd206a0-0a5b-3dbc-a9b3-c5c843162621 | -13.9818 | -56.0151 | 2025-05-23 07:30:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 40.8 |
| ade44076-c64f-34c1-af99-cabf56951ac1 | -6.2224 | -43.3693 | 2025-05-23 07:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 4d0ea702-1e75-30b6-959b-1253cc24b094 | -13.9818 | -56.0151 | 2025-05-23 07:40:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 342bf931-2074-341a-88ac-dbe12b19592d | -13.9818 | -56.0151 | 2025-05-23 08:00:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 84e2f856-4a0d-301c-bed7-f8aa7efaf77b | -6.2224 | -43.3693 | 2025-05-23 08:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 535eb5a0-cde6-3d82-b90b-896597b92729 | -6.2224 | -43.3693 | 2025-05-23 11:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| c9ab2517-f550-3d27-804e-04f2334f66ac | -12.3898 | -49.9786 | 2025-05-23 11:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 499.3 |
| caeaa4c9-bd3d-35ef-b594-ed511cc51477 | -12.4086 | -49.9978 | 2025-05-23 11:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 161.9 |
| 266aa976-5b84-36cb-872e-6981b46628d5 | -12.4089 | -49.9762 | 2025-05-23 11:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 252.6 |
| 82136662-9f66-3335-ba33-191d1dd3ee4a | -12.3703 | -50.0026 | 2025-05-23 11:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 8b81763c-4249-3f3f-abb8-19f6dc590e56 | -6.2224 | -43.3693 | 2025-05-23 11:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 3ba57fde-e365-381f-bcbe-3d025ec26f8c | -12.4089 | -49.9762 | 2025-05-23 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 273.9 |
| 50f08b08-94d0-3de9-80c6-b2cfaab4b3e7 | -12.3898 | -49.9786 | 2025-05-23 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 849.4 |
| 61b73e8d-f952-33e6-92bc-8b35ce3e0342 | -6.2411 | -43.3677 | 2025-05-23 12:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 32755277-e9fb-3b4a-9569-cab6f5741db7 | -12.4086 | -49.9978 | 2025-05-23 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 171.2 |
| 496b493a-f8b4-3525-a461-5fdd2edd4629 | -12.3706 | -49.981 | 2025-05-23 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 190.2 |
| 58157458-eaf8-3033-b1ab-6d371b283f9c | -6.2409 | -43.3911 | 2025-05-23 12:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 3e7f4c9e-62bb-3cc6-b297-8bef6d82e9fa | -6.2411 | -43.3677 | 2025-05-23 12:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 97.4 |
| caa4dbf6-eeff-363e-857c-f938d5ce18d8 | -6.2224 | -43.3693 | 2025-05-23 12:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 6a8e7c31-6b67-3c10-b2bd-9d3c0e094ec4 | -6.2409 | -43.3911 | 2025-05-23 12:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 2483a0ae-fb94-3d90-a0f1-f23a5024b139 | -12.4089 | -49.9762 | 2025-05-23 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 297.9 |
| 1b2e9d4e-442d-3d55-95b7-53349fa44b15 | -12.3522 | -49.94 | 2025-05-23 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 017e45ad-ad78-33a5-ae5a-2548d47bb7bf | -6.2411 | -43.3677 | 2025-05-23 12:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 3d1ca2cd-8fe7-311a-b5db-cc2ee5041417 | -12.3898 | -49.9786 | 2025-05-23 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 511.2 |
| 53ee5ae4-5745-350c-bceb-35d450f0bedb | -12.4086 | -49.9978 | 2025-05-23 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 239.8 |
| 578727eb-ff90-31d2-96a2-4f4b82471d99 | -12.3703 | -50.0026 | 2025-05-23 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 171.1 |
| 5d55e45c-3492-38b0-8a43-4a04390e0823 | -6.2224 | -43.3693 | 2025-05-23 12:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 123.1 |
| ef5a29ed-5c86-38b3-a241-e7aae9badb03 | -12.3706 | -49.981 | 2025-05-23 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 252.3 |
| 9ff0d184-1b14-3b7d-8694-9207a7c452bc | -12.4089 | -49.9762 | 2025-05-23 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 325.5 |
| e1830af7-bf6b-3d41-a0cc-e2ca44df427f | -6.9427 | -42.789 | 2025-05-23 12:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 82.1 |
| 2ecd2f62-1456-3051-b5fd-b37f3639060a | -6.2224 | -43.3693 | 2025-05-23 12:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 131.6 |
| b961950d-1054-38b8-99c1-1af9092840d2 | -6.2411 | -43.3677 | 2025-05-23 12:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 164.1 |
| c9cddf4a-b270-31c0-8fc5-ed8bd7af1452 | -12.3898 | -49.9786 | 2025-05-23 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 421.6 |
| 5c67d9fa-a091-3a62-9347-259430ba1282 | -6.2409 | -43.3911 | 2025-05-23 12:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 172.5 |
| e0e2af77-f2a9-361f-965c-797be222c1dd | -12.4086 | -49.9978 | 2025-05-23 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 266.4 |
| 2b2a428b-7c80-30ad-a2b4-9ee62a9c3856 | -12.3522 | -49.94 | 2025-05-23 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 632518ee-e5f5-392e-b409-07d099120e79 | -12.3703 | -50.0026 | 2025-05-23 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 99248286-e885-3e3c-8ea2-a71cd86cb9d3 | -10.3293 | -46.6475 | 2025-05-23 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 413a0327-85d0-3dc3-b08a-d2fd6c201989 | -6.2411 | -43.3677 | 2025-05-23 12:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 186.5 |
| 727eadc5-0618-383b-ba0d-46a2170a7241 | -6.2409 | -43.3911 | 2025-05-23 12:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 159.4 |
| 30c6f0aa-ac4c-303b-bd61-9ba1fa80228d | -6.2224 | -43.3693 | 2025-05-23 12:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 05f0f3f2-b664-38a4-93e7-95894dc8f58d | -5.76645 | -43.48814 | 2025-05-23 12:40:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 422c61a6-6d71-3adf-a6a3-1f5f7a3933b2 | -7.45825 | -45.44926 | 2025-05-23 12:40:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 5e7c2471-eda4-3cca-a7ac-741b292fc616 | -6.94278 | -42.78448 | 2025-05-23 12:40:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 37.4 |
| 793ff219-d369-3b2e-a97e-77267efe5abe | -5.97856 | -43.75681 | 2025-05-23 12:40:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| f20cfb5f-dfec-3711-88ad-7eecd7d2e4d4 | -7.31845 | -46.89307 | 2025-05-23 12:40:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d45d451d-ff77-37eb-ab7e-a5937b44eb8f | -7.24284 | -44.70964 | 2025-05-23 12:40:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 799f176e-6750-3316-8c70-3a80bc553612 | -6.62495 | -48.0136 | 2025-05-23 12:40:00 | TERRA_M-T | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 6196650b-15cc-3d58-b47f-2ddd57a5acb0 | -6.23361 | -43.39559 | 2025-05-23 12:40:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 392e3e16-ca4b-37c4-975a-8401c130e518 | -6.22301 | -43.37296 | 2025-05-23 12:40:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| a5d151a3-5bb3-37fd-bf8f-25ad010b3a89 | -6.10842 | -43.96266 | 2025-05-23 12:40:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| a985c921-0844-361f-8a8a-fc70fd0cfea3 | -7.23568 | -44.72073 | 2025-05-23 12:40:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| fb19cd60-be78-3ee8-825d-ba4fcd86e2f1 | -6.46067 | -45.53831 | 2025-05-23 12:40:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 460d3ddd-238f-33fb-9649-1e0dd9d3dacf | -6.24955 | -43.376 | 2025-05-23 12:40:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 3e27fbab-c98d-38b8-96c2-f7e8c43694db | -5.76452 | -43.49352 | 2025-05-23 12:40:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| f81312f9-bbd4-3953-93e3-723a90595b25 | -5.7877 | -43.61935 | 2025-05-23 12:40:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| f5e12ce7-9035-383e-a4cd-1e177a011aad | -5.57794 | -45.19535 | 2025-05-23 12:40:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 0f0eb4b1-495a-362c-8ac9-168746d5ed7a | -7.11675 | -47.8512 | 2025-05-23 12:40:00 | TERRA_M-T | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f11de170-d962-3c94-876c-8294990b890a | -7.24615 | -44.77996 | 2025-05-23 12:40:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 0fac3e27-831d-3199-9e74-2f3feb070fb6 | -7.06765 | -44.9326 | 2025-05-23 12:40:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 616f23f2-84da-3822-bb70-e2be2fabb2d5 | -6.23627 | -43.37454 | 2025-05-23 12:40:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 239.8 |
| 0abc6417-5375-3a28-9b06-8c2aa90ccf4c | -6.23715 | -43.3892 | 2025-05-23 12:40:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 251.6 |
| 69346b60-650e-3294-9b17-57ab3c9fa85b | -6.95687 | -42.78597 | 2025-05-23 12:40:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 93.0 |
| df6bbf9c-5103-3b81-ab5f-03e9fa8c6c58 | -6.24 | -43.36806 | 2025-05-23 12:40:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 161.7 |
| b7adb959-e9d5-3789-b972-7b94f2582b30 | -7.21226 | -46.9211 | 2025-05-23 12:40:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 788db13a-b8d5-3427-9b69-7170c5d78052 | -6.35625 | -42.8677 | 2025-05-23 12:40:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 22.6 |
| ff28e9e5-ff2d-3e9f-9b17-53bafc805eb7 | -6.2296 | -43.34498 | 2025-05-23 12:40:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 4c3c136b-dff4-36a5-8eb3-c6f1d740be60 | -6.62359 | -48.02353 | 2025-05-23 12:40:00 | TERRA_M-T | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 0caf0c93-6280-375b-bc58-c4ba5c6675c0 | -7.11817 | -47.84074 | 2025-05-23 12:40:00 | TERRA_M-T | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 71e90b7e-bb4e-3513-a434-5113cca14041 | -6.22672 | -43.36663 | 2025-05-23 12:40:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 169.6 |
| d75387a7-2897-3b0a-86be-832001b47bb6 | -7.51878 | -43.37258 | 2025-05-23 12:40:00 | TERRA_M-T | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 3929eb28-e42e-3e1c-8306-47e156d0044e | -6.94761 | -42.79064 | 2025-05-23 12:40:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 109.8 |
| 878ae20c-d590-3820-8bf8-e65ab6f1d74d | -7.23801 | -44.7033 | 2025-05-23 12:40:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 7e9cffcc-7731-3933-9128-f7f2976fc427 | -10.32982 | -46.6296 | 2025-05-23 12:42:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| a4d2c331-16a1-3c56-a0a8-3a922ffb43f0 | -12.3828 | -49.98482 | 2025-05-23 12:42:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 176.4 |
| 95a6c99d-ecdf-336a-8c3b-25cd72d3eec4 | -7.58993 | -47.14518 | 2025-05-23 12:42:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| aaf4d6d5-63a6-3e2a-8787-9746a4c5b8c3 | -14.03074 | -55.13094 | 2025-05-23 12:42:00 | TERRA_M-T | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 45513646-ee9e-3b3a-97d4-61742cbbff37 | -9.57133 | -50.5161 | 2025-05-23 12:42:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 629fb2b8-1c9e-3d40-8079-1ba8610ee0ac | -13.79045 | -54.29988 | 2025-05-23 12:42:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| cccdc897-259f-3613-ba35-7f292ed9fd51 | -12.40101 | -49.9874 | 2025-05-23 12:42:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 168.4 |
| 4ac9eb39-0cb6-31ef-b2fb-f9d5bab02452 | -10.3771 | -49.1804 | 2025-05-23 12:42:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| c8bf83bd-08b7-31f7-ae35-4cedeca09a62 | -9.67592 | -49.71744 | 2025-05-23 12:42:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 828ca89b-a898-3aa0-83c1-e9634fa42ba8 | -11.57588 | -54.56784 | 2025-05-23 12:42:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 1a18c768-8ea4-354a-b54d-03537f611056 | -14.3183 | -48.65748 | 2025-05-23 12:42:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| f8ba6cfa-f522-3217-8df3-cf3e071699ae | -11.4557 | -47.85183 | 2025-05-23 12:42:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 439a295a-b0ce-3621-a138-37241ff875d3 | -12.40234 | -49.97784 | 2025-05-23 12:42:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| b687d1e2-9c67-3fa3-857d-3af3d1c70f9b | -10.51092 | -42.38562 | 2025-05-23 12:42:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 304.5 |
| b76d346b-c3ba-33fd-b16c-2bdfbe062be3 | -13.18287 | -53.56593 | 2025-05-23 12:42:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6544ec63-525f-36a3-ac79-0c56a5ead1c8 | -10.65709 | -49.48057 | 2025-05-23 12:42:00 | TERRA_M-T | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 3b15e396-db87-3863-90d2-d491c35dc80f | -7.79306 | -46.22375 | 2025-05-23 12:42:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |


[Clique aqui para ver as próximas entradas](README22.md)
