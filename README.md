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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb779095-c60e-3e7b-a90c-b6c14ce93f6f | -16.4349 | -52.7963 | 2026-05-08 00:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 604837ca-953b-388d-8f54-07b57e5d6cba | -21.4329 | -47.0562 | 2026-05-08 00:09:00 | TERRA_M-M | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 116d6fa3-bad1-3227-9fcf-1df96a819c84 | -21.43418 | -47.06576 | 2026-05-08 00:09:00 | TERRA_M-M | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d78620d5-8dfc-391d-8fc0-a5e6a3168fbb | -23.14314 | -47.54482 | 2026-05-08 00:09:00 | TERRA_M-M | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| ce33471d-036f-3fd3-bce5-3eca15e360a0 | -21.4253 | -47.06714 | 2026-05-08 00:09:00 | TERRA_M-M | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 400b0658-aa58-3f9a-9a3a-5b9273f2d0e3 | -22.93715 | -48.91674 | 2026-05-08 00:09:00 | TERRA_M-M | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 43b029a4-5e91-36ea-8d38-d187dff5ef4e | -21.70133 | -48.41059 | 2026-05-08 00:09:00 | TERRA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 30.2 |
| a1d9397a-7758-3eb2-b385-4385749f5bd8 | -21.70265 | -48.42107 | 2026-05-08 00:09:00 | TERRA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 97620e6b-fbfa-3534-a6ae-45912b6ce01d | -22.93578 | -48.90532 | 2026-05-08 00:09:00 | TERRA_M-M | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1f8c9877-9046-3455-9e41-28ecc74b8769 | -13.78893 | -44.08349 | 2026-05-08 00:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 09112a94-699b-337c-b6c1-786d934acd21 | -12.86532 | -43.76783 | 2026-05-08 00:11:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 184405c5-bd66-3a04-ae7d-ef557fcb6426 | -12.8545 | -43.76959 | 2026-05-08 00:11:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 9f0fb32f-3877-330b-8dd3-df5aaa838447 | -16.42241 | -52.78775 | 2026-05-08 00:11:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 27505090-bce1-3e34-975c-ec36aaf2defe | -18.51129 | -55.51381 | 2026-05-08 00:11:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.7 |
| 95834a64-896d-3928-81ee-13429b05d20c | -17.81225 | -46.71497 | 2026-05-08 00:11:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 59f0c132-8f61-340e-8f30-9fef558d1c46 | -21.37709 | -48.55163 | 2026-05-08 00:11:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.6 |
| c76006ec-ef6e-3a23-9697-16d9e2480c35 | -12.84972 | -43.76252 | 2026-05-08 00:11:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 20514d2a-c37c-3bc0-b2a5-cd59468a48d0 | -20.22382 | -46.83234 | 2026-05-08 00:11:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 17287d35-1aac-31f6-96a7-b058f5f8260b | -12.86055 | -43.76074 | 2026-05-08 00:11:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 5d58c2e3-5c6c-379f-a7a4-395fb83032b3 | -21.37579 | -48.54101 | 2026-05-08 00:11:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 3bd6f3b3-28c8-3b47-8ac4-de41a60ae018 | -19.18082 | -47.35339 | 2026-05-08 00:11:00 | TERRA_M-M | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d0bd0aae-6e6e-34f0-83c1-51b5af14bfbe | -14.13526 | -45.34253 | 2026-05-08 00:11:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9f243245-f05b-360d-949e-b0f75795f9b6 | -12.85226 | -43.75556 | 2026-05-08 00:11:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 310396ce-cc77-3c0c-867b-0281343b9d02 | -16.42426 | -52.80407 | 2026-05-08 00:11:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 06e5f380-ab29-3c05-9f67-499c400c5b68 | -12.86308 | -43.75379 | 2026-05-08 00:11:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 448b620f-2d1d-3dba-b97c-2d4fea1409ac | -21.38641 | -48.55015 | 2026-05-08 00:11:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| b641e56c-4f25-397d-a692-994d424b88e5 | -18.51119 | -55.51936 | 2026-05-08 00:11:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.3 |
| 4ac97a55-3e2d-3557-ab74-ed8fd8d368c9 | -11.06936 | -49.47294 | 2026-05-08 00:13:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 4f69e318-6708-3ab1-9bcb-ce3c15bda7a3 | -12.34944 | -50.02386 | 2026-05-08 00:13:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 33227c73-d358-3f1d-873c-103e5f6a0f2d | -11.47394 | -52.91359 | 2026-05-08 00:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| ffec5cd0-4d40-3e33-9523-c8e10ea30e14 | -11.12678 | -45.11724 | 2026-05-08 00:13:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 547d4740-b59f-3d39-9696-d45691e5d117 | -9.40874 | -50.68116 | 2026-05-08 00:13:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| b076662e-1df5-37ee-b3af-c27a4f739621 | -9.307 | -48.58731 | 2026-05-08 00:13:00 | TERRA_M-M | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| c68fa24c-1fc8-30d1-89f2-c8dd6e241208 | -10.95716 | -48.84726 | 2026-05-08 00:13:00 | TERRA_M-M | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a332bc6f-0e6f-348b-aa2d-95e1080ef5fc | -11.42131 | -47.09338 | 2026-05-08 00:13:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2c67bf73-6bd9-3570-8111-55244f5f7317 | -8.68633 | -49.08951 | 2026-05-08 00:13:00 | TERRA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1ddede73-050c-3721-828f-61e883e90bdd | -9.47595 | -46.14624 | 2026-05-08 00:13:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f15f5403-18af-351e-bd6f-090af0f78a51 | -9.29819 | -48.58858 | 2026-05-08 00:13:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 37.4 |
| df026c30-4dc7-396f-adfa-10d1bd0fce3e | -12.35073 | -50.03355 | 2026-05-08 00:13:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| acd14b29-ad1d-3563-88a0-d7e9ed90d798 | -9.41004 | -50.69077 | 2026-05-08 00:13:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| e29311de-0b41-3622-9791-2bb31622c5df | -8.78317 | -44.83982 | 2026-05-08 00:13:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c33051c3-65df-307b-b38e-ef1097241db9 | -9.31581 | -48.58603 | 2026-05-08 00:13:00 | TERRA_M-M | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 2eb67852-2570-34f8-aa1b-e4389a4f63c7 | -11.62736 | -47.89171 | 2026-05-08 00:13:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 3ec4dfeb-9417-3dc3-9fda-89b6e560cdd9 | -10.05442 | -51.67874 | 2026-05-08 00:13:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b9b4b9c2-c9f5-3761-9a51-93d22d0d27f5 | -8.7027 | -49.07816 | 2026-05-08 00:13:00 | TERRA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f9c32daa-f5e2-3171-acb4-99bebcd37e66 | -11.1266 | -45.11081 | 2026-05-08 00:13:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 20fb07c6-5be7-3944-bef3-0c1af30fa00b | -11.63494 | -47.88139 | 2026-05-08 00:13:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| cbbb5bb6-5090-31c4-b30b-28a1fd6668ec | -10.66803 | -49.70871 | 2026-05-08 00:13:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 1270e1a0-bebe-3c88-ba55-ed9c9889ec8a | -8.71149 | -49.0769 | 2026-05-08 00:13:00 | TERRA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4f089165-44a8-3cf3-94c1-88aaa5a2dbcd | -11.80154 | -47.10749 | 2026-05-08 00:13:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4ae64850-bbac-3839-8399-16efd7a71b8e | -10.67609 | -49.69242 | 2026-05-08 00:13:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 6870a5e1-a498-3c31-9b1c-499c278eed1b | -7.29445 | -49.62769 | 2026-05-08 00:13:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 65ff85fe-6e8d-3a6e-9ba9-c1a571398869 | -13.18933 | -52.7068 | 2026-05-08 00:13:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 561fc9a5-c06f-39cf-b977-149b042c2201 | -8.69512 | -49.08825 | 2026-05-08 00:13:00 | TERRA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| bd3adb3a-f818-3e87-95eb-ef2bcc44cbb4 | -8.68755 | -49.09835 | 2026-05-08 00:13:00 | TERRA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a2617061-48b5-3ab9-a7ce-c9bbb8ae7e8c | -8.71271 | -49.08574 | 2026-05-08 00:13:00 | TERRA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 2d4802cd-323c-3887-a4d9-bf0c2ffa9f2a | -10.93693 | -49.442 | 2026-05-08 00:13:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 4e6bd2cf-1c0f-3a38-935d-55a6607ec398 | -13.18763 | -52.69254 | 2026-05-08 00:13:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 6764a07f-5d53-3feb-b8fd-ffbbb1ced456 | -10.93816 | -49.45108 | 2026-05-08 00:13:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 0c54c694-339b-38c9-ba14-cfb2572fe4ac | -12.40649 | -46.75979 | 2026-05-08 00:13:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 9ebea743-9381-3e7f-ac41-d970e5fc29d4 | -9.5627 | -44.57763 | 2026-05-08 00:13:00 | TERRA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 7909f6e4-9c2a-31d0-9fc4-e0feac3a9e02 | -8.69634 | -49.0971 | 2026-05-08 00:13:00 | TERRA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 52.0 |
| a52408e2-623d-30cc-a287-9f9e1ce8f0e1 | -11.80019 | -47.09813 | 2026-05-08 00:13:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 36.6 |
| e00332e6-be16-3094-9554-f139b79609c9 | -11.12838 | -45.12294 | 2026-05-08 00:13:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f971187f-fb88-3071-97f1-8b374b098605 | -11.94997 | -43.37951 | 2026-05-08 00:13:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f31c8b2c-1bf1-3a10-91e3-606f7a11d755 | -10.05301 | -51.66783 | 2026-05-08 00:13:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 10ae0bec-e87b-3f41-9cdc-dce3f63c62e1 | -12.1539 | -46.66971 | 2026-05-08 00:13:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 2349071d-597e-3b53-8f9e-9a4fe676a322 | -10.04329 | -51.66909 | 2026-05-08 00:13:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 40.5 |
| db46ce56-dd22-3533-a195-25cce0cae39e | -13.4811 | -48.91751 | 2026-05-08 00:13:00 | TERRA_M-M | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bd8243da-99ce-33b9-99e0-f46cd8bb7d15 | -11.81562 | -47.33941 | 2026-05-08 00:13:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| df9de229-6b3a-3273-8db6-fe0f043bd8fb | -10.23759 | -52.22795 | 2026-05-08 00:13:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| d1c326b6-c12e-3870-89d1-61f1b145033b | -9.56564 | -44.57148 | 2026-05-08 00:13:00 | TERRA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 22.2 |
| a185033b-e17a-3e30-9160-e43f8094d59f | -12.15251 | -46.66002 | 2026-05-08 00:13:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 94a33630-eb0c-30bf-ae5d-5900f906a340 | -11.13049 | -45.14138 | 2026-05-08 00:13:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 30a3fae7-3105-3f85-b46a-3e3732d3efea | -8.37025 | -48.08011 | 2026-05-08 00:13:00 | TERRA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fed870f8-5521-367e-a37e-c001299e6130 | -9.56776 | -44.5851 | 2026-05-08 00:13:00 | TERRA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 1f29b50c-cf47-3bb4-88b8-6825b7521c4b | -11.61401 | -54.1868 | 2026-05-08 00:13:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 03984e5c-525d-32ca-9ce4-27a8999c70fe | -11.82593 | -47.3414 | 2026-05-08 00:13:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 30.5 |
| eabe5f70-afb3-3dd2-9afa-cb2fe1fb9c9f | -11.79884 | -47.08873 | 2026-05-08 00:13:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 939799cd-538f-3a12-9212-a2009e16a054 | -9.29696 | -48.57969 | 2026-05-08 00:13:00 | TERRA_M-M | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 9fc67e4c-1ace-3b76-89ec-105300c83750 | -7.34389 | -49.79183 | 2026-05-08 00:13:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 98315cec-0f6d-327e-99f7-447e658ce5db | -8.69268 | -49.07057 | 2026-05-08 00:13:00 | TERRA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 88f6efe1-6aca-3541-b713-f1ddfcdef7df | -11.47564 | -52.9275 | 2026-05-08 00:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 5036d095-36fc-3892-9fe1-e9dedfe6b141 | -11.79119 | -47.09949 | 2026-05-08 00:13:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 5405a4ca-3565-3509-af2e-d2d07f71acee | -11.97707 | -46.78774 | 2026-05-08 00:13:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 04e785bc-ce68-3685-8ad8-e364b878fb79 | -8.7868 | -44.833 | 2026-05-08 00:13:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 7dd0ab00-b47e-39f1-859a-c8c73a4662a2 | -8.6939 | -49.07941 | 2026-05-08 00:13:00 | TERRA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5ac4db48-6c46-37a2-b51e-415f8739011a | -11.1253 | -45.123299 | 2026-05-08 00:16:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e798d568-1443-3d1e-a0f0-194c827f30d2 | -9.3011 | -48.5825 | 2026-05-08 00:16:00 | METOP-C | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6c75a4b1-b155-3ac6-bff0-fbae96c83b71 | -11.7925 | -47.0905 | 2026-05-08 00:16:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7321acc7-3322-35f4-94ba-892868b01b23 | -10.039 | -51.663101 | 2026-05-08 00:16:00 | METOP-C | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1eef7f8f-e1e3-315c-907c-450d911a032b | -9.2914 | -48.584499 | 2026-05-08 00:16:00 | METOP-C | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4ef4d042-11a3-38a9-ab3d-86a547d56c3d | -11.814 | -47.344601 | 2026-05-08 00:16:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9d0bf6c0-d8be-37a1-af5b-00978883896f | -12.8518 | -43.755199 | 2026-05-08 00:16:00 | METOP-C | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9f6f5e58-3db2-305c-b1b5-0104701683d5 | -8.7849 | -44.828499 | 2026-05-08 00:16:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 08ab59e5-d002-3d9a-bdc7-2bd54f3ff6b2 | -18.0844 | -50.421902 | 2026-05-08 00:16:00 | METOP-C | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 10bfcfb5-64bb-3bd6-939f-a8ad0bcaaeae | -9.4009 | -50.695202 | 2026-05-08 00:16:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d0ac3e0-46e2-3a19-b957-a3070f5600a5 | -5.7813 | -45.1395 | 2026-05-08 00:16:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0a28444a-f4f4-3f2c-afa0-8d1494f8d5f0 | -9.3969 | -50.675598 | 2026-05-08 00:16:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbc4a593-fa6e-39df-9825-b6b53fe1db9f | -8.7867 | -44.836601 | 2026-05-08 00:16:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
