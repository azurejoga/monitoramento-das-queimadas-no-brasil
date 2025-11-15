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
| cd92347b-85ce-3b21-a40f-27e24aa11516 | -9.82135 | -49.77213 | 2025-11-15 04:06:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd5bb9d7-fab1-3b54-a304-b57345fd624a | -11.8482 | -49.2183 | 2025-11-15 04:06:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 053265ed-6eb9-33d2-b2cf-1245a8390492 | -9.52066 | -40.59211 | 2025-11-15 04:06:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1c89d8f5-6ee2-3bc4-a427-6c645435cd36 | -11.32107 | -48.52752 | 2025-11-15 04:06:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e7596604-a0b4-3c33-858a-5d31acf10cc7 | -7.21476 | -47.97524 | 2025-11-15 04:06:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8bb7b49a-06d0-3623-8fbd-5f9a8fe0702b | -7.6943 | -47.19268 | 2025-11-15 04:06:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7119f3df-496d-30a6-85cf-a934e4ededbf | -10.04989 | -45.35237 | 2025-11-15 04:06:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37da9939-1f81-3e60-b169-dddd8ecdc831 | -10.11214 | -40.89539 | 2025-11-15 04:06:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 97fb4415-f917-390b-8c41-369077ec18b1 | -12.77035 | -46.95618 | 2025-11-15 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0b8f9ce-723e-3298-937a-ec01371d0984 | -11.32678 | -48.52516 | 2025-11-15 04:06:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e7dc532c-876f-319d-bcdf-b32d727d34f2 | -7.88084 | -48.40921 | 2025-11-15 04:06:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2a325d87-3361-3b0a-84f0-93fdd717536c | -11.91714 | -46.19799 | 2025-11-15 04:06:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2ed03ec-6d1a-371f-b4c1-a5a2c33ef8dd | -12.8421 | -46.43489 | 2025-11-15 04:06:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1948ec10-8e05-39f6-9612-bc0f038a9e69 | -7.69362 | -47.18978 | 2025-11-15 04:06:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 836cccd5-8954-38de-a3f1-cc1858dd7862 | -11.84904 | -49.22085 | 2025-11-15 04:06:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| af45140f-0017-3f65-a0dd-21509b673599 | -10.69126 | -44.51151 | 2025-11-15 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7b1ce126-7f00-31a4-ab85-4ed3f0ddbec8 | -7.5391 | -45.85604 | 2025-11-15 04:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 645316b9-77e7-35da-8bd3-3ac21006bdf4 | -10.875 | -44.68306 | 2025-11-15 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8c176289-58b4-30e3-a6f0-e718f7612d68 | -12.79616 | -46.38648 | 2025-11-15 04:06:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2210161b-761b-3ea0-9095-ad293c07fd77 | -11.84797 | -49.22647 | 2025-11-15 04:06:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c15cae24-8a1c-39de-953f-9bb57523b516 | -18.06632 | -42.34784 | 2025-11-15 04:08:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9704e76a-2230-3a9d-8988-650b2330090e | -17.96962 | -48.06614 | 2025-11-15 04:08:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5a92acc5-1a90-3fdd-9e07-5bb894de47ec | -14.98776 | -42.41432 | 2025-11-15 04:08:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8d0d4b1f-ea16-3fca-8703-3ce25d7e6d4d | -15.46236 | -39.23609 | 2025-11-15 04:08:00 | NPP-375D | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1d787608-8611-300a-a651-f05f0e37a268 | -15.45881 | -39.23553 | 2025-11-15 04:08:00 | NPP-375D | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 0cf840e7-7b7c-3b6d-9270-f2b7b05df165 | -17.5837 | -46.68052 | 2025-11-15 04:08:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 7abbadc1-a43f-3546-b049-29e107997eff | -17.62395 | -49.33745 | 2025-11-15 04:08:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6502d08-7412-3e35-bffd-bc5bb4846eaf | -14.65872 | -46.56337 | 2025-11-15 04:08:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2c281fa1-8476-3700-aa6d-f253f5cbfaf4 | -16.60642 | -43.41203 | 2025-11-15 04:08:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a9bf4c72-05fb-31a8-a5b1-0d88cfcb1eae | -19.249 | -46.45442 | 2025-11-15 04:08:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b760a6b1-84aa-3648-abbb-420e233da52d | -17.26987 | -42.65916 | 2025-11-15 04:08:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e8a52baf-4a5d-38d2-93d2-3802b3c1d872 | -19.19679 | -47.87318 | 2025-11-15 04:08:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7fd9863-4614-3233-a38e-75478a707840 | -18.34048 | -47.19038 | 2025-11-15 04:08:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49ecc72a-83f1-31aa-a385-e55db435ee6a | -14.65669 | -46.57473 | 2025-11-15 04:08:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 61a5368f-ac24-33b6-8f0d-8773b94b7166 | -16.45047 | -45.0109 | 2025-11-15 04:08:00 | NPP-375D | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 914696fd-a96e-3936-8252-66c75943aed9 | -17.15964 | -43.07578 | 2025-11-15 04:08:00 | NPP-375D | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c36f07b2-1765-3b4e-aa28-c4a11821bf4c | -20.53048 | -41.57441 | 2025-11-15 04:08:00 | NPP-375D | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 18c39e14-4b2a-3579-abd3-e7eb3e0d1fb1 | -17.83924 | -50.81445 | 2025-11-15 04:08:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a1811ca5-033b-3075-a116-310fff8e9ca3 | -16.44836 | -45.002 | 2025-11-15 04:08:00 | NPP-375D | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ea0dafd-b16d-3582-bfb4-dad4d47fee0c | -17.58284 | -46.68532 | 2025-11-15 04:08:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 5e327376-c67e-307b-ad24-eb89ac11f73b | -16.56385 | -47.60841 | 2025-11-15 04:08:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efcc2b71-e507-3f20-8572-f46e4ec37779 | -16.44976 | -45.01505 | 2025-11-15 04:08:00 | NPP-375D | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ba16bf7-d358-3936-b3df-3df683275cb6 | -15.95328 | -43.0192 | 2025-11-15 04:08:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d27026c-1ef8-336d-80e9-6e118986a46a | -14.68938 | -46.61927 | 2025-11-15 04:08:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88921af4-e52d-3fce-a4e6-a03fd4e86d7c | -14.68542 | -46.61868 | 2025-11-15 04:08:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c11ac76-35d2-34e4-9ba8-4dab307d00ae | -17.57992 | -46.67979 | 2025-11-15 04:08:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 9028936c-a74c-3c77-9de1-754981a104b7 | -18.33665 | -47.18951 | 2025-11-15 04:08:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4779e755-b8b8-349b-8f43-75c7a26b11d8 | -17.16199 | -43.07581 | 2025-11-15 04:08:00 | NPP-375D | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7aa0cf86-4959-3cdd-b7c2-3bd0d6ddad7c | -15.46426 | -43.14992 | 2025-11-15 04:08:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0e8d905c-71b4-3524-9ff2-5bb2fdd426cd | -18.34887 | -47.25372 | 2025-11-15 04:08:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 018dd02c-be9a-3d09-b548-00452eeb780f | -16.42834 | -42.63167 | 2025-11-15 04:08:00 | NPP-375D | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 33d136d1-7a12-3789-b4dd-d30e2b96f5fb | -15.45821 | -39.23964 | 2025-11-15 04:08:00 | NPP-375D | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 03a42300-6d80-390a-8bcc-5d3570d16a4e | -20.21587 | -47.39557 | 2025-11-15 04:08:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d57830c-d1b7-3cb4-9f90-bb3e512df9b3 | -18.26919 | -43.07626 | 2025-11-15 04:08:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 38d74c6b-1b88-3f95-9665-8901fb356484 | -19.19184 | -47.8778 | 2025-11-15 04:08:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea05ca84-d7ab-38d8-8a08-8777b5bad347 | -17.28148 | -46.46307 | 2025-11-15 04:08:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd0186ee-c64b-3944-aa3a-4c663a2fd5b1 | -16.2777 | -45.61917 | 2025-11-15 04:08:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6ddd503-f6a6-3400-8c91-7136d55707c7 | -17.24821 | -42.66656 | 2025-11-15 04:08:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 939a896b-27da-3951-ba83-7ac0fcc1ee49 | -16.53165 | -43.56734 | 2025-11-15 04:08:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c5f2bb64-9ce0-31b9-b4fe-67ecd2359ace | -15.47507 | -43.18951 | 2025-11-15 04:08:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 22bb4ac0-4365-3096-9679-c292d5af626e | -16.5598 | -47.60764 | 2025-11-15 04:08:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01a2520f-f0ae-3037-9504-4d0c4ad5389d | -15.36892 | -45.63704 | 2025-11-15 04:08:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5720df77-bf87-3fad-87cb-b3e38a0591e0 | -17.83792 | -50.81203 | 2025-11-15 04:08:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| edc8f64e-135b-3d8f-bde4-b6ab544b759f | -13.95276 | -46.19662 | 2025-11-15 04:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a22d7e60-10e0-3ae0-953d-d6238ff05a86 | -15.78972 | -41.47103 | 2025-11-15 04:08:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3b3d8051-bc11-3317-a03b-973ccefeb211 | -15.62655 | -45.25341 | 2025-11-15 04:08:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ebae7ab-bbfb-3fa2-9ab2-897508539bdf | -17.97368 | -48.06699 | 2025-11-15 04:08:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2aac9e2d-5373-3268-9408-3021c198ff5d | -17.48582 | -41.97202 | 2025-11-15 04:08:00 | NPP-375D | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9b567d62-c5c2-30a7-8aa1-b63ccbc10fa8 | -16.333 | -43.94559 | 2025-11-15 04:08:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c433642-66b7-3b35-bc45-83e53d873631 | -14.68726 | -46.60828 | 2025-11-15 04:08:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 01b4943c-828b-37eb-b1d2-b0a77386d037 | -16.15943 | -46.44713 | 2025-11-15 04:08:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 114962c2-0b4e-3b57-a1ba-6d32f5206d59 | -14.68634 | -46.61349 | 2025-11-15 04:08:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a12834b9-8a59-3a29-813c-4650926f14ca | -15.14714 | -43.65273 | 2025-11-15 04:08:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3a1c21a0-931c-3ec2-8192-e56e45064d7f | -15.44211 | -42.93578 | 2025-11-15 04:08:00 | NPP-375D | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa028bba-55dd-3146-a0af-9d5759e5a18e | -14.89978 | -41.5389 | 2025-11-15 04:08:00 | NPP-375D | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 660fa749-5523-376a-9273-a062e1aacf9d | -16.56047 | -47.60392 | 2025-11-15 04:08:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 427dd206-2e0c-3f99-aa0a-56f4970064bf | -14.7197 | -44.23824 | 2025-11-15 04:08:00 | NPP-375D | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 249c0ac6-4231-33ad-842b-81d1fd9f3eef | -17.29338 | -46.82375 | 2025-11-15 04:08:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0870b096-5fba-370e-8a79-0aa09b318020 | -18.69778 | -46.75949 | 2025-11-15 04:08:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a0a2f8a6-b9b1-3524-baed-4ec6843eca6c | -16.56317 | -47.61215 | 2025-11-15 04:08:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 83b7f9e0-bf56-3e4b-a39f-bf548e2e0674 | -20.53128 | -41.57175 | 2025-11-15 04:08:00 | NPP-375D | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5f96091b-dea5-37bf-ae13-ccfd6afb99ae | -15.09484 | -43.24907 | 2025-11-15 04:08:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7859e761-ce79-31b7-b3be-e84f8e853823 | -19.00697 | -41.06879 | 2025-11-15 04:08:00 | NPP-375D | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| faa3e886-ead3-3451-a310-3088c1c2581c | -14.76179 | -42.84685 | 2025-11-15 04:08:00 | NPP-375D | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a60bde5e-2b61-396e-adf3-db0ccea87c64 | -18.59523 | -43.99149 | 2025-11-15 04:08:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 507d9003-7375-3eb1-8a0f-95f329860ca1 | -17.24546 | -42.66237 | 2025-11-15 04:08:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 69e47e9a-de6f-3d8d-9ca2-e81547e0d526 | -15.13038 | -43.66918 | 2025-11-15 04:08:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a2b30c79-6050-38af-941d-bbff23855fa4 | -15.10487 | -41.97205 | 2025-11-15 04:08:00 | NPP-375D | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ebe40351-c6ba-39c7-ab70-cc7780a76e67 | -17.29718 | -46.82465 | 2025-11-15 04:08:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e3fc194b-41b7-3094-9257-10f191782ad8 | -17.88596 | -43.9905 | 2025-11-15 04:08:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e452db48-420f-3436-9d4a-8ea638d66108 | -16.45329 | -45.01569 | 2025-11-15 04:08:00 | NPP-375D | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84df2112-50f6-34cd-ad42-2049e9ef35f6 | -15.38187 | -39.21511 | 2025-11-15 04:08:00 | NPP-375D | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d71ea826-b490-371f-aefa-50194fe3f365 | -14.69032 | -46.61395 | 2025-11-15 04:08:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32854424-1a21-3a69-a181-d8546275a3f7 | -17.24879 | -42.66294 | 2025-11-15 04:08:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 78b45f1b-0925-3cfd-9363-43e4b5713c81 | -18.48612 | -47.51477 | 2025-11-15 04:08:00 | NPP-375D | DOURADOQUARA | MINAS GERAIS | Brasil | 3123502 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5f013ac2-c2e6-3039-ae06-6ba354a96f81 | -14.66072 | -46.57488 | 2025-11-15 04:08:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c24af1c6-0bbe-3135-b1a8-70daeb5e89b4 | -17.57906 | -46.68458 | 2025-11-15 04:08:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0e55be5c-c589-3c3c-93f3-aba9c2f14f9a | -16.81308 | -39.68388 | 2025-11-15 04:08:00 | NPP-375D | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4469c1b6-e504-3a85-821f-59d74f075aab | -16.97616 | -50.60604 | 2025-11-15 04:08:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a78cbf1-7a67-3a57-8a02-aa453bcc108d | -14.05324 | -44.48109 | 2025-11-15 04:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README31.md)
