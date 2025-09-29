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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad97ed50-d8d5-39a0-a28e-8f418fb659fa | -12.95265 | -47.18692 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99a3aa3b-e2a3-3300-9ca4-27a3f79f497d | -13.7982 | -47.89057 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0073d7d4-f1dd-3ad7-8ef6-bb2632e55830 | -15.90687 | -46.24038 | 2025-09-29 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9834b0f3-0d17-3a5f-8940-6122041bf342 | -14.59006 | -44.9955 | 2025-09-29 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0cb92917-03d9-3370-b8c4-b7dadc69defb | -12.35743 | -54.14715 | 2025-09-29 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efff3839-cb76-39fa-9ae0-fde8298b05b7 | -13.77992 | -47.91753 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b04788d-3890-3557-8cc0-8cabf264ae68 | -15.42905 | -48.2443 | 2025-09-29 04:59:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 99ae32bc-189b-35d0-9212-33b84b4d5f9b | -11.62976 | -52.84549 | 2025-09-29 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ecb2b404-1adc-33ff-abc2-5797ad926630 | -13.26911 | -48.45713 | 2025-09-29 04:59:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 198aa9a2-e0ab-36a3-aa25-330f3c04fd44 | -17.07582 | -48.56937 | 2025-09-29 04:59:00 | NOAA-21 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cefd384b-a46c-3984-8233-8a124cb2c956 | -13.83242 | -47.48779 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d684a506-497a-3806-bcc8-ff4639ad7f7d | -12.75363 | -46.85752 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5cfd78db-b555-3d01-ba1a-ca504a6d786d | -16.06257 | -51.02283 | 2025-09-29 04:59:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 217ca6c7-45e1-36b6-87ce-3dc550919f3e | -14.52534 | -48.39278 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 17a308fc-ac44-30b8-bc7b-0d45a45ffc01 | -11.37256 | -55.14104 | 2025-09-29 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48bb6b7b-115f-3bba-90b5-8b2aa0845c87 | -11.98937 | -46.59761 | 2025-09-29 04:59:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 200f43b4-534a-3068-bcfa-cd8f283458cf | -15.28219 | -49.50071 | 2025-09-29 04:59:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b92032c9-aaf8-399e-b7aa-6a8c9afefaea | -11.65985 | -45.33522 | 2025-09-29 04:59:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 39cd3c94-67f5-359d-a00c-8fbdb081f756 | -12.00428 | -46.60598 | 2025-09-29 04:59:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d129eed7-5b8d-3c11-b43a-804639f70496 | -14.62453 | -48.30066 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9d93038-386c-381d-b130-5523c8df05ed | -13.80531 | -48.01932 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 594d572d-8d1d-350b-a97f-bc2b294e6ea1 | -13.78957 | -47.87971 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c340f193-1a78-3873-befa-8e24545953bb | -16.40554 | -52.17168 | 2025-09-29 04:59:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13c02c43-3ca9-3cd8-97ed-901b1add4927 | -10.88572 | -53.74548 | 2025-09-29 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fedf093d-3ca1-3aba-8fda-77072c2b1307 | -13.38495 | -48.15435 | 2025-09-29 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 134b20e9-e88a-3afe-9b78-06d887f9cd1f | -15.03554 | -46.97769 | 2025-09-29 04:59:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a57ec038-bb92-359e-92cb-a575be73b18c | -15.9152 | -46.21644 | 2025-09-29 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 46d54a2b-df6f-3bae-b657-da440d29a172 | -13.78476 | -47.91872 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6f3e5ab3-1bd7-3f27-a80d-7d3aae366fa0 | -14.54415 | -48.43871 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1b77f0a9-4594-320f-a785-fa70ed74c163 | -14.5269 | -48.41903 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9cd7706e-dfbf-3bfd-9e64-884e56d2ea38 | -12.01701 | -47.78968 | 2025-09-29 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3fed7756-bd26-3fbf-9c78-4d55834739d2 | -12.02271 | -48.34507 | 2025-09-29 04:59:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ca2c3230-9f41-3eac-ace5-2b833fe8c6b3 | -11.92506 | -48.049 | 2025-09-29 04:59:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 54c52fdb-d35e-3761-ba88-5f1d50b747ec | -13.62251 | -48.04563 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d902f401-a1df-3561-8096-35e61ffe3e9f | -14.28863 | -49.3952 | 2025-09-29 04:59:00 | NOAA-21 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df4e8f75-133c-3779-ab5d-6196433b0095 | -14.46855 | -42.17558 | 2025-09-29 04:59:00 | NOAA-21 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9d2a2016-5a45-3311-9b4c-fe92c9969719 | -11.76809 | -47.55892 | 2025-09-29 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d6eea2da-2076-35a6-a0c3-16775e6e4617 | -11.62917 | -52.84949 | 2025-09-29 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 390d04e8-e4ff-36c3-8629-8150b5c22951 | -15.27716 | -49.50444 | 2025-09-29 04:59:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7abca4f-1a7d-3d4a-989f-2a588f1ef2f6 | -15.21452 | -50.10992 | 2025-09-29 04:59:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| fec9d1f0-6010-3108-bff3-5f7e226376da | -17.08626 | -48.5653 | 2025-09-29 04:59:00 | NOAA-21 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 85ff5ae5-af91-3153-92cb-8c2fd24cf08d | -16.52454 | -46.94883 | 2025-09-29 04:59:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e7f720c2-fac7-3b5f-8398-9703424508fd | -14.57402 | -48.27209 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6c0fac46-9a69-3154-966e-9f0a7a6c3b65 | -15.90656 | -46.24319 | 2025-09-29 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 753b5585-11f4-3957-9003-c494fbef83a6 | -11.7204 | -44.43025 | 2025-09-29 04:59:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7b784cde-acdc-3a02-9c3e-f13310734e2a | -15.54344 | -47.87338 | 2025-09-29 04:59:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb420bcc-1fed-3826-a22c-48ed4949d41e | -14.65087 | -48.15395 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e687bd2f-d835-3e1e-a5eb-1a254f511ce8 | -13.58594 | -48.10416 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e391e5da-a410-3edf-b1ea-b0339c2de1e4 | -13.60131 | -48.05807 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 55685d59-c071-3b5f-a6dd-7b807ecafe45 | -12.94157 | -46.76618 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ab56ab42-952d-36f5-b74a-208db2c55ff6 | -12.66714 | -46.92025 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bc21e6bf-6456-3388-bc45-6650e3663f1b | -14.59465 | -45.00974 | 2025-09-29 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a0b2c626-98ee-375b-9c56-321fe4461c94 | -13.27447 | -48.45246 | 2025-09-29 04:59:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a2e91fb-e2e2-38e8-908e-ef9fc07e1c0f | -15.61308 | -46.25474 | 2025-09-29 04:59:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ca5cb351-fbe8-3328-aa3f-92e8b9657008 | -11.94159 | -43.91979 | 2025-09-29 04:59:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ca8526e2-235b-37a6-bd8e-55108ef69a0f | -16.52914 | -46.9572 | 2025-09-29 04:59:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 666745e6-34cd-3d26-97b7-4cc140093b73 | -13.18516 | -47.44457 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6ce40cdb-c1e2-3789-9f81-1c9393530f70 | -11.44952 | -47.2837 | 2025-09-29 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| da63d017-9950-3344-8e9d-e58eb4099417 | -14.75191 | -48.37165 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 122e423e-a6b1-3a32-8aca-1daf4b069b01 | -15.53155 | -47.93243 | 2025-09-29 04:59:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5253eecc-4b01-38d4-9cc6-44490ad380a5 | -12.95312 | -47.21143 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8379cccb-e19d-3204-87e7-d19029307143 | -15.90091 | -46.24263 | 2025-09-29 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ee34602-9512-3265-a46b-d46e99414852 | -12.98487 | -46.26442 | 2025-09-29 04:59:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3a4abf19-52ab-3287-9a07-ac95f269dfbf | -13.63221 | -48.04689 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| f1cc80b9-1952-3f61-994c-7ca9e796f2a2 | -12.47931 | -54.42311 | 2025-09-29 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1937d8dc-98b9-3bb4-bae1-fb7165891a40 | -15.54882 | -47.87093 | 2025-09-29 04:59:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eda7afdc-85cd-3c73-9a84-b074ee82a08c | -12.96313 | -45.16694 | 2025-09-29 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9197f45-ecad-3585-823d-b33c2fa33d94 | -13.80694 | -48.01926 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 44feca42-360f-3ac7-90b7-a2062d54ad67 | -13.80207 | -48.01865 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 17fbb882-0e20-38d7-9b5d-16521fb6512d | -12.77474 | -46.85745 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65886d3c-c7fb-3443-9abf-3359b7a55698 | -13.02125 | -49.44992 | 2025-09-29 04:59:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7d1c5044-e802-36c1-988d-14ae1b93f39b | -15.06157 | -45.06036 | 2025-09-29 04:59:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0dc6ae9c-a894-346d-94c8-b16d44ec6f96 | -13.75797 | -47.89339 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5f489600-ab2f-3b9c-8a3d-962c090072b3 | -15.25287 | -56.82379 | 2025-09-29 04:59:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86b0a9be-5d08-3e6b-9537-9ecd91193ade | -11.93174 | -48.07185 | 2025-09-29 04:59:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 29709ce2-fddb-3407-a82b-b6e16c3df8bc | -13.65811 | -48.07623 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f770be18-6aea-32c3-8968-71931ffa8232 | -14.64793 | -48.15213 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3759d788-772c-342e-8f1d-5c62f4128504 | -13.49605 | -47.40295 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56879328-6a97-3854-99f6-dec1977825cb | -13.35558 | -47.30681 | 2025-09-29 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bdbe8461-107a-363a-9118-378a64586216 | -12.69516 | -46.90532 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 67966a15-baa2-38d9-93e0-b33c185dae84 | -13.58171 | -48.10317 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a6300a8c-7814-3811-b2e8-116ef61c6c52 | -12.28816 | -44.10013 | 2025-09-29 04:59:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c907fee8-91b5-3364-a7a4-048289a4bac8 | -11.99791 | -47.11194 | 2025-09-29 04:59:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ebfc1408-f417-39fd-b224-099a7a9e18dc | -13.60618 | -48.05838 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4729d86f-4d75-3e4d-a53f-852ad9090fc4 | -13.59532 | -48.06683 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2e7977a6-f21a-3d82-aa21-e70639a65835 | -11.81166 | -48.24272 | 2025-09-29 04:59:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44ed8f9c-0d77-32ef-918b-d8e705a1f6ef | -15.92924 | -49.08721 | 2025-09-29 04:59:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4b1f192-69a4-31ad-9ab0-8322f7adcbe1 | -13.24147 | -48.44944 | 2025-09-29 04:59:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 740663ab-875c-3cc5-89f5-e84ed7d1f455 | -13.59642 | -48.05782 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d230a33a-95c4-368d-92b1-4fcf2b0c2f9d | -13.60582 | -48.06824 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3193dd4d-4d67-307e-a87c-e94cd327c49a | -11.80397 | -51.80388 | 2025-09-29 04:59:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aee99fb1-b1e0-3909-a26a-0280065238ee | -15.22041 | -50.09815 | 2025-09-29 04:59:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d817b2bd-acdc-3770-b432-0d49b84eca35 | -14.59785 | -45.00979 | 2025-09-29 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e4892cc7-66f1-3a89-a8b5-9b75647630c0 | -14.49237 | -48.54801 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fdf003ef-b237-3781-9b2b-6663252febe9 | -15.25973 | -48.7687 | 2025-09-29 04:59:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b262506f-8b2d-3f00-8329-8726ad4a6881 | -11.69754 | -44.44518 | 2025-09-29 04:59:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6fd291c6-8c48-32ad-864e-8951f6d342bc | -13.57927 | -47.29762 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2b09f1de-9214-34c2-ad62-6cc4cb474096 | -13.75567 | -47.9122 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 04691475-6fcd-3397-883f-2b029c8d33f3 | -15.29055 | -49.50696 | 2025-09-29 04:59:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 34140223-7c59-35d4-8b99-78b55d3549ed | -13.60242 | -48.04895 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README66.md)
