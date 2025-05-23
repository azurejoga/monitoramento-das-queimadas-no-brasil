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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62d31fb6-9d1e-37d5-bd87-6faca2adc108 | -6.22642 | -43.37088 | 2025-05-23 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 29.5 |
| a2e1d21a-8b82-3866-a5c1-87255859cfde | -5.78112 | -43.61013 | 2025-05-23 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba3119da-7479-3b46-a3a9-679c6542634f | -6.23243 | -43.35527 | 2025-05-23 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a171baab-df28-3dca-8a19-b5a3c0dddd72 | -5.76342 | -43.49141 | 2025-05-23 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e61208c-82d9-3e96-b1d5-9759df64ad7a | -5.5809 | -45.20227 | 2025-05-23 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| cd15fcca-8a5d-3639-a021-4f8b62e77a04 | -6.22949 | -43.35068 | 2025-05-23 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 92047f73-ea3f-3848-9457-c9f124644e4c | -6.38397 | -43.66597 | 2025-05-23 04:23:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc8ad326-74d4-3c24-b967-c7e7f19066db | -5.97541 | -43.7575 | 2025-05-23 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc148417-46d4-3410-a081-1b6271ab1798 | -7.21697 | -43.12457 | 2025-05-23 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5ca2f354-1f1c-3dd1-ae69-42315b7f7099 | -6.94495 | -42.79405 | 2025-05-23 04:23:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 94c2c6ab-57db-3e60-956f-0b413edffd14 | -6.22361 | -43.34144 | 2025-05-23 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e4f95f3-e170-3dd5-9f3e-221894ee2b55 | -7.20907 | -43.1277 | 2025-05-23 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| f6964443-8ecd-3e22-becc-5db12a488324 | -11.51383 | -48.55559 | 2025-05-23 04:25:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5a7112be-aa7e-31ca-92c1-1824de938bb2 | -14.0394 | -53.38001 | 2025-05-23 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 805bd631-0e8e-356e-88c7-83b8c298eb31 | -12.07291 | -47.34716 | 2025-05-23 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 821aa411-41f8-3a6a-b27c-97dcbcbe9243 | -14.4387 | -47.87001 | 2025-05-23 04:25:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8d53e34-14ad-37ea-b0e8-a69940fe2fa2 | -10.72507 | -52.47217 | 2025-05-23 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d4e466b-0dd2-3283-86dd-9dafe05ad4be | -14.04074 | -53.37256 | 2025-05-23 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fcef03d6-8118-301a-9ec9-4010d807a9eb | -14.03667 | -53.37179 | 2025-05-23 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84456a80-db59-36ea-88f7-ecd61a638203 | -12.29123 | -52.50089 | 2025-05-23 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a0369aa1-167a-37fa-949e-64fc898e8fb6 | -7.96937 | -49.69203 | 2025-05-23 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eaebd552-ea5a-32f5-90d7-64c61f2b9fdb | -11.27246 | -52.47284 | 2025-05-23 04:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6ae7d31-04a5-3233-8e43-d0bac054d359 | -12.33093 | -49.99193 | 2025-05-23 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f2412faa-519f-3af9-a932-33f41e14d70a | -12.06806 | -47.33563 | 2025-05-23 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cdf064d2-f795-33cd-a80f-9a9355219418 | -12.42127 | -49.97474 | 2025-05-23 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cdf6b054-4922-3ea6-a814-d46957d7f0b7 | -12.29917 | -52.50235 | 2025-05-23 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1d98cfdc-c00b-3bfa-bc3c-288e7c232e7b | -11.80515 | -57.36163 | 2025-05-23 04:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 64f9aee5-5f16-3954-adfc-473f6b3bbeb0 | -12.39677 | -49.98306 | 2025-05-23 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 60f3ba93-e6e9-3029-a231-cd6fabb8ac04 | -11.29436 | -53.9784 | 2025-05-23 04:25:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf9c6411-89a6-3ebd-84aa-bfaa6f09d791 | -12.64346 | -44.24651 | 2025-05-23 04:25:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1120aff1-5909-3785-b80c-45c020863d1d | -12.06971 | -47.34673 | 2025-05-23 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ea6bab75-8f3b-36bd-bfcb-018dfefdfaee | -12.33159 | -49.988 | 2025-05-23 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 64f33830-7d95-375b-9624-4c3ad38d805d | -11.94021 | -43.92933 | 2025-05-23 04:25:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4130cef4-69f5-3edb-936a-ae13fdc30e30 | -15.42183 | -41.40602 | 2025-05-23 04:25:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6473f5a6-4f23-3ed5-a294-fb63f0ddfa89 | -9.04401 | -47.75055 | 2025-05-23 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dec66214-4455-37dc-b9cc-c822dd561f59 | -12.28817 | -52.49493 | 2025-05-23 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9ad2d124-3b2a-3ff5-b69d-a0d7c5dff327 | -13.25041 | -56.54554 | 2025-05-23 04:25:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9da9288-e108-34c2-a9be-d5085e296312 | -11.5702 | -47.45699 | 2025-05-23 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9d02a451-b702-3e14-9d21-05f180737266 | -12.32331 | -49.99466 | 2025-05-23 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9acef15c-c34a-344b-b4d9-c65e2d119458 | -10.46717 | -47.9411 | 2025-05-23 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf2335a9-fb44-3e98-8d93-c3fdf21f008f | -10.64742 | -49.47689 | 2025-05-23 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e69753db-5fc1-3f68-a2a0-b8b4f3f7c285 | -11.65336 | -58.26226 | 2025-05-23 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0af7c31e-4e57-3cb1-83ee-9fe5f9adbac5 | -12.29703 | -52.50364 | 2025-05-23 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| acb7e0b8-de89-3667-b55b-8a9c79505433 | -10.71351 | -48.81984 | 2025-05-23 04:25:00 | NOAA-20 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 137f080e-d6af-3918-8845-e87b557a2549 | -11.56744 | -47.45295 | 2025-05-23 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1b886195-55b6-3a10-93e8-8d2916da68cb | -9.02621 | -47.75492 | 2025-05-23 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99f7eb78-d7cf-3c39-871b-b576bfce2145 | -11.56829 | -54.56987 | 2025-05-23 04:25:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bc026f61-bc9d-30d5-b437-656bf0519977 | -11.57497 | -47.89744 | 2025-05-23 04:25:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c28ddc74-4145-3e08-916c-7dcb2c0e9266 | -7.71624 | -45.66065 | 2025-05-23 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3c8259ff-2a6f-32af-87b9-6ded176c4991 | -7.80187 | -46.22129 | 2025-05-23 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c863e976-6414-3138-b2d3-811374bbb97a | -7.71291 | -45.66013 | 2025-05-23 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dac6c53c-c976-3865-8fbe-6ae69a6481e3 | -14.05363 | -53.37118 | 2025-05-23 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11703041-83d4-3a43-8352-399ec2d3ae19 | -12.06695 | -47.34267 | 2025-05-23 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 788478f5-d05f-3a41-8a0d-83c772220b71 | -14.04414 | -53.37706 | 2025-05-23 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d08595e-57b6-3632-be78-ef2f0467be9b | -15.42577 | -41.4114 | 2025-05-23 04:25:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| be8fae3a-a0f1-3285-ad39-2afdf7977d15 | -13.78709 | -54.31318 | 2025-05-23 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fd4d53d7-08a3-399f-9450-a0ce12c64ec0 | -11.55419 | -47.4508 | 2025-05-23 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 91b3fd0e-52ff-348c-a231-31637d84b92f | -12.33855 | -49.98917 | 2025-05-23 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 575a64ef-99af-3396-80b9-bbc3af0a703e | -9.02067 | -47.74678 | 2025-05-23 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8673d04f-b859-38c2-9179-ceeb0b257ec0 | -8.90021 | -50.02464 | 2025-05-23 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e99b490d-897c-3814-b71a-ebeca907bbb0 | -11.87884 | -52.30055 | 2025-05-23 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 400dce24-3762-3cac-b2e0-9e93085f269d | -11.30927 | -54.02266 | 2025-05-23 04:25:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f41ee3cf-d171-3348-b221-581710884e89 | -13.09652 | -52.28959 | 2025-05-23 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8b09701-6203-3e6a-b687-6445b80f589b | -11.57376 | -54.56596 | 2025-05-23 04:25:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f07ebab2-7cd3-36cd-8a59-390edf8a38cc | -15.42123 | -41.41089 | 2025-05-23 04:25:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 89e8d58e-31d4-3c7c-bfbd-19cadcc86943 | -13.05628 | -44.04637 | 2025-05-23 04:25:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f4a13037-e9aa-3d81-9708-55df775aa315 | -13.7843 | -54.30384 | 2025-05-23 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9dfb292a-8cb5-3f12-ac98-e6ec59dc05f8 | -7.97297 | -49.69264 | 2025-05-23 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d1f8f5b-6f57-3492-8cd3-a93a3363994d | -12.3933 | -49.98246 | 2025-05-23 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e48bb3e-6c39-3301-a1f7-9a6f46b48365 | -12.30007 | -52.49712 | 2025-05-23 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bcc1922c-c746-317a-b6e5-d878f3ce1ed3 | -12.07137 | -47.33617 | 2025-05-23 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac5699d4-c212-369e-82ad-7e302a65a55e | -12.3392 | -49.98525 | 2025-05-23 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd7542b8-13f7-35f2-a6bc-f6949c7733a3 | -12.39961 | -49.98758 | 2025-05-23 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| daf58c75-bb98-3678-a33d-ea7eda3cc7b0 | -12.60604 | -48.37563 | 2025-05-23 04:25:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8022fecc-ece1-3975-9892-11154f2d501c | -7.71678 | -45.65713 | 2025-05-23 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ab3393e6-8fc4-31ab-af7b-b32f871cc280 | -13.78273 | -54.3124 | 2025-05-23 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b6ef38c0-a86e-355c-aa46-2c0431626e0c | -12.29797 | -52.49842 | 2025-05-23 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1de7ec40-3e99-39ee-9826-6c006fc98fe4 | -13.15919 | -56.82313 | 2025-05-23 04:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 332f8c1d-4346-385f-a53f-0e86e2d72bfb | -13.24536 | -56.54433 | 2025-05-23 04:25:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13708670-8164-34ec-ada2-6029c93406b1 | -11.65429 | -58.26455 | 2025-05-23 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb3f3cf7-452c-3387-86ff-b7d82b5ed29d | -12.41714 | -49.97805 | 2025-05-23 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb369ada-dbb0-3800-a12c-a72ae0ff678c | -8.71973 | -50.25559 | 2025-05-23 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6388af0b-f5f9-3e70-9ff9-f93680693dbc | -12.60053 | -48.36745 | 2025-05-23 04:25:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e457c1bf-0c47-3544-b5b7-a2e75ad99b48 | -15.14382 | -43.96413 | 2025-05-23 04:25:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 91b2fd1c-5fbf-3a89-a081-b2ca95bb4035 | -14.04821 | -53.37783 | 2025-05-23 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6dafb6b1-c670-3f84-bf13-29f02b229a70 | -12.30097 | -52.4919 | 2025-05-23 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9decd5de-ac18-3e8f-8dfb-f4e2c4ef94b2 | -11.32561 | -58.62188 | 2025-05-23 04:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0151cff5-2be9-38c6-83b7-5507919778cb | -11.93587 | -43.93316 | 2025-05-23 04:25:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b69ce08-84da-3ea9-9963-f5caf517c378 | -8.48273 | -49.60678 | 2025-05-23 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 484fe41d-ce50-3c3b-82ce-8b8760e89a1d | -14.04889 | -53.37411 | 2025-05-23 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54b65db0-604f-3117-ba42-c9693103ec6c | -12.4763 | -54.47956 | 2025-05-23 04:25:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88c2e99f-9266-3cc7-9fc3-f598baa1e707 | -12.31636 | -49.99347 | 2025-05-23 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9fdf8e04-ee46-3beb-bef7-51ca9e34fc61 | -13.7863 | -54.31752 | 2025-05-23 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6301669a-e5b7-3360-b6af-12e8eb6e0982 | -12.29304 | -52.49043 | 2025-05-23 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4eba2de1-9764-3390-89e6-d266fdc50c07 | -12.13616 | -54.66294 | 2025-05-23 04:25:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3fed287-2460-3697-93b1-a217aacf4f25 | -10.66255 | -49.47152 | 2025-05-23 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 589e6387-c992-34ea-aeba-144e941d846d | -12.85102 | -47.38653 | 2025-05-23 04:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9cc584b0-ac19-3b99-bbe9-a11c4c41c485 | -12.29214 | -52.49565 | 2025-05-23 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4dd3bdd2-756f-3f28-a7e5-69fc28d7d966 | -9.96109 | -49.80701 | 2025-05-23 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 636c9823-85cc-3349-8330-fdaa267de34e | -9.96041 | -49.81104 | 2025-05-23 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README13.md)
