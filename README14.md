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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6094eef3-33da-3a6d-a1cc-0e6f843eef3a | -12.56194 | -47.00856 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 320bd848-44c2-313c-824f-52bcf03ed93e | -11.9469 | -43.40838 | 2025-08-12 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa111faa-e5fb-3baf-bdba-ff80d0914765 | -12.54708 | -47.04914 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d20a70b6-da5a-3909-87df-003f94f9eff3 | -10.34099 | -50.82436 | 2025-08-12 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f36e8fb3-3077-37b7-9d1c-ff8ccee1e72a | -11.45476 | -47.32046 | 2025-08-12 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88174f6c-df41-3acc-9624-8db657455048 | -10.3611 | -50.82713 | 2025-08-12 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 88ab0168-ee02-36f0-bc23-0fc5cd888719 | -12.56733 | -46.99983 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f389fba-c197-341a-bc84-75cefaa7f09a | -12.69987 | -46.36403 | 2025-08-12 04:08:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57d56f77-6c0f-3a41-b9ab-a9d12038fb4d | -14.06894 | -44.83253 | 2025-08-12 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6ca2a21-af68-33ca-995d-c3bc17f9f4cc | -8.51968 | -43.31317 | 2025-08-12 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1472dbf1-3194-3b7d-b1b4-abbd624b2bf2 | -14.11944 | -45.38036 | 2025-08-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31469344-bf89-3841-810f-4b263ab0f2bd | -13.34889 | -50.24921 | 2025-08-12 04:08:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 18.1 |
| a81821ff-5423-395d-baff-0d2570c392ad | -13.12574 | -46.87638 | 2025-08-12 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e4970a40-315c-3a64-9711-cf28c12760db | -11.80982 | -44.93194 | 2025-08-12 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f82b52b-44f6-3d36-9c48-ef2c4fcbf5f0 | -12.57121 | -47.06648 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a0493c0-2516-3c5b-bf61-5dcf0498c53d | -11.45547 | -50.1688 | 2025-08-12 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e2391a83-94d7-3464-ad7e-18d019f40897 | -14.11476 | -45.38739 | 2025-08-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76a4427f-ea0b-3913-8e12-f09e2d628473 | -11.72106 | -50.11528 | 2025-08-12 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a238aad8-37c5-3ae3-8523-9e77f64e47e0 | -12.5716 | -47.01969 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f3488104-4dd1-39ff-8ec4-1e051f461de5 | -11.80697 | -44.93217 | 2025-08-12 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 91303961-6a9e-399e-92ba-59b73f48310d | -9.71607 | -49.48859 | 2025-08-12 04:08:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 55e54ad0-1c58-3976-8783-dceb90631cba | -9.71784 | -49.47891 | 2025-08-12 04:08:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 74672c9d-b3bf-3fc1-ab41-20a645b9cdef | -8.56103 | -54.69468 | 2025-08-12 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1b06baf-aa8d-3afd-8612-8eb42100625c | -14.11071 | -45.39061 | 2025-08-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a663573-2727-3e0f-a7ff-ee7ecfc1905a | -8.5654 | -54.70718 | 2025-08-12 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 477a67b0-f663-3b97-b51e-c17a7fdc323b | -9.71235 | -49.48293 | 2025-08-12 04:08:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| eb0c51b1-7ecf-3a0f-a75a-7a6b8ee3136f | -9.07218 | -45.05371 | 2025-08-12 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8fa9e9dc-2f4d-3e65-8081-e201b695e92a | -12.55816 | -47.00805 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 3aa2cc02-5393-30db-a316-1af62041b499 | -12.77583 | -45.46104 | 2025-08-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 11fb6d92-4dd4-33a2-8aff-2c3a830c64b5 | -11.45377 | -50.16587 | 2025-08-12 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 17759aff-3ac5-3c77-b7a3-5cf5f2e7cf04 | -8.21213 | -45.05739 | 2025-08-12 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 87598490-935a-392a-8a43-af366cfbfc9d | -12.56652 | -47.0045 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b25ced6-f077-36b4-8457-f0d540005d48 | -12.56356 | -46.9993 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 21206442-8160-3da2-9fa8-efeefb690469 | -14.02437 | -47.40609 | 2025-08-12 04:08:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d26117b-6fd1-37bc-b865-c6e88baed869 | -11.70351 | -51.60071 | 2025-08-12 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8eff5e90-66dd-37d0-9ba2-2793da39e360 | -12.56491 | -47.01371 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e5fbf789-df09-3d7a-b89f-30e525562a8c | -12.73558 | -45.89643 | 2025-08-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 205d75c6-fb37-36a3-8194-e26d4e12a01e | -10.34488 | -50.8311 | 2025-08-12 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa883e5c-3ec0-3284-a990-221a7b44a41f | -12.64452 | -45.33855 | 2025-08-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb341e91-3f2c-3bd7-b9cc-36cb992efda2 | -14.11819 | -45.38799 | 2025-08-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d9ab68ce-d81f-39ea-b793-48ecdb8ba219 | -13.87954 | -45.57235 | 2025-08-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14cd860d-8d26-3b13-924a-64bdc31a24c3 | -11.95123 | -43.40211 | 2025-08-12 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| caf28340-9737-37ca-b9ca-f49e744ad23a | -12.55085 | -47.04975 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 734d3874-ed50-33e0-a45f-efa26e0dcedf | -12.99687 | -44.88538 | 2025-08-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e9a8360-e1b2-3855-9897-e0375574db82 | -9.06796 | -45.05714 | 2025-08-12 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d513f26-dd74-32f0-82e5-3b5e152bd521 | -10.36419 | -46.63831 | 2025-08-12 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5ee3eb7-8479-33c9-a87b-fcdbbf67f69b | -9.76823 | -48.7536 | 2025-08-12 04:08:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5623f73-8d22-30e6-8667-a3ee2869fdbe | -10.97556 | -49.5692 | 2025-08-12 04:08:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bab0b14b-ebb4-344d-a33c-38c8221d23ac | -11.94358 | -43.40784 | 2025-08-12 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f53be336-c0c6-333a-84b8-3481e866e0f7 | -13.87511 | -45.56448 | 2025-08-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70b3f214-274c-364d-9012-3fad6a9ad782 | -7.80115 | -45.02331 | 2025-08-12 04:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c915810-26aa-33c1-980b-19adb0cc6525 | -14.11664 | -45.37595 | 2025-08-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70b5c8f5-d061-3cf5-81a7-590928991663 | -11.66202 | -50.13312 | 2025-08-12 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e35797f5-cf76-30ab-bcf0-82b0db6ce6d7 | -8.52026 | -43.3096 | 2025-08-12 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 89aa80c0-3015-3fd8-af4e-35e55dbd4f20 | -13.58603 | -46.95275 | 2025-08-12 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d1b8fbe-347f-38c4-8829-68c30913e8af | -14.03002 | -47.44012 | 2025-08-12 04:08:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0c94006-bbfc-3731-bab7-6e6d3ec36c19 | -13.78525 | -43.51181 | 2025-08-12 04:08:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10522100-16e6-3115-9a56-c3d96f5a24a4 | -8.52188 | -43.32086 | 2025-08-12 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07d3b84e-69aa-3572-863c-f400ac850001 | -13.12281 | -46.87133 | 2025-08-12 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07468cc0-3da7-3f49-8cf9-9ca06974085c | -9.32998 | -37.98226 | 2025-08-12 04:08:00 | NOAA-20 | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 72e169be-6b96-3546-9f9d-b0e210575610 | -10.36519 | -50.80424 | 2025-08-12 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 537a12aa-17b5-3dd3-974d-e13de61423e3 | -11.72015 | -50.1202 | 2025-08-12 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 653801a1-4db4-3db7-b841-804b19b42faa | -8.12701 | -47.44034 | 2025-08-12 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be49f2cf-c846-31c9-8f8f-3d08fea0439c | -8.15213 | -49.14391 | 2025-08-12 04:08:00 | NOAA-20 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70795e94-ba43-376c-b7a8-990bc5b05e4e | -8.56649 | -54.70156 | 2025-08-12 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7d9924e0-4008-3188-aeaf-c0c08c89b5ef | -12.5711 | -47.0004 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b44091f3-ff1c-346c-a3da-3b16abac7645 | -13.58298 | -46.94842 | 2025-08-12 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 790306bd-a3f1-3272-a662-249bea8dbc85 | -7.42102 | -43.96416 | 2025-08-12 04:08:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13f0cc75-aeb6-3b77-9ff4-cff92e1e4844 | -9.71412 | -49.47328 | 2025-08-12 04:08:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2443f41-1658-3cc7-827c-b3bfe094ff85 | -14.63655 | -45.85634 | 2025-08-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 12d92e64-d62e-3d7a-a9ad-fe7ae0e8579a | -14.11134 | -45.38679 | 2025-08-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7c74060-6bd9-35f3-938d-8d33bf01473b | -7.6479 | -43.84259 | 2025-08-12 04:08:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8aa093f7-022e-36bc-b510-b0e6f7a429d4 | -9.71905 | -49.47702 | 2025-08-12 04:08:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ac21189d-95d2-3438-a001-1bf1e09b9589 | -8.13113 | -47.44107 | 2025-08-12 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eff4af84-d156-3e23-b106-b15ef81ff0c4 | -11.68694 | -51.60419 | 2025-08-12 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eab4af32-f072-37bc-be9c-8dd03a8159e3 | -7.28544 | -49.27039 | 2025-08-12 04:08:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1285558-2be6-34c3-a15f-d39cde133294 | -11.91446 | -44.8532 | 2025-08-12 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f06d6b2e-e47c-3758-9b00-cc20bfb70005 | -9.70899 | -49.48022 | 2025-08-12 04:08:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 7c91776a-b21e-3937-84fb-c34463978cce | -13.62736 | -46.93332 | 2025-08-12 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fbd03d4b-20e1-368f-941b-67339a933ebe | -8.20924 | -45.05268 | 2025-08-12 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5983c010-6623-3749-896b-66e9c5a70359 | -9.70815 | -49.48504 | 2025-08-12 04:08:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| bb93a145-f9c6-3291-9c98-c30fbff36385 | -9.2065 | -48.52649 | 2025-08-12 04:08:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f9296236-3181-3b24-a0ff-045699bb7be3 | -10.23565 | -48.24988 | 2025-08-12 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac3e52f0-bdea-3d32-a648-566995cca34e | -9.06946 | -45.06987 | 2025-08-12 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d4f4b454-8b96-33d8-b3c5-6d8212166f6f | -12.57778 | -47.07338 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| acdb8118-e218-3c58-bf65-851f2bccfa3d | -12.64318 | -44.86065 | 2025-08-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06288cc4-9cb0-33fa-8013-bc43d685b452 | -12.7743 | -45.44873 | 2025-08-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01b05fda-b001-3ebd-8c69-8775e19daffd | -13.3543 | -50.24538 | 2025-08-12 04:08:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e754422f-0d7b-309a-beec-257471f850f9 | -9.71275 | -49.48589 | 2025-08-12 04:08:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| db980410-e5fe-3391-9e83-ac0c0b712d00 | -10.05983 | -46.39634 | 2025-08-12 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5ec2430-499d-3e4d-8f13-a2e12635f079 | -11.75965 | -45.02685 | 2025-08-12 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46c4d72f-8609-3e87-9ee8-eec960329111 | -9.07015 | -45.06578 | 2025-08-12 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5813b23f-dac3-38d8-be1d-1a5ebfb118d9 | -12.56438 | -46.99457 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 94a820b4-5ea0-3f23-a78f-7bef6b36e8b4 | -10.34208 | -50.81857 | 2025-08-12 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 83d346f2-f328-3796-842a-a16dc2f49cf0 | -8.56284 | -54.69425 | 2025-08-12 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8cb62f7-ba09-3a14-a0d6-8d0891c6e259 | -11.72188 | -48.35002 | 2025-08-12 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4829c704-9e78-382d-bcf7-67c87a9a7e74 | -11.72659 | -50.11125 | 2025-08-12 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8c13a36-a1d1-38f7-8e83-721c312338bb | -9.91382 | -46.17937 | 2025-08-12 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8a07b988-b508-339f-be60-986a66564dae | -8.56494 | -54.68307 | 2025-08-12 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc16dfbe-57ea-3b36-b95b-6af44d3dd361 | -11.95236 | -43.39505 | 2025-08-12 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README15.md)
