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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2aad5880-e58c-34c0-917d-057144561fef | -12.93806 | -46.32936 | 2025-08-26 04:23:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2809b04b-8c35-3dba-8250-8b399dc255f7 | -15.13144 | -48.68346 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1bc3c4e-0b9c-318c-880e-45378ef7580e | -14.3606 | -51.91165 | 2025-08-26 04:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 09bab406-1622-332d-bb8f-24920bd924a3 | -12.67771 | -47.85935 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 558ac276-e55a-3872-8ef3-e98f883deba2 | -13.47876 | -47.01132 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 24c571d6-b1a7-3881-9a00-b0db49c07414 | -14.28829 | -60.35922 | 2025-08-26 04:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dde15f1f-9d4e-3b5a-9287-f12b0666fdde | -14.34897 | -51.95266 | 2025-08-26 04:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e143b2a-cc1d-385e-b56a-71c091534362 | -15.13682 | -48.67247 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4eadd4b3-98e5-330f-9ba6-8d56f0c60aa8 | -15.04444 | -48.5133 | 2025-08-26 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6e13b74-d6de-3fb2-9e68-2759ae0c0150 | -11.03118 | -49.13885 | 2025-08-26 04:23:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fea7d7aa-2025-39dc-b985-24073739720a | -11.5251 | -52.1338 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| d9ff4900-a40e-387b-8656-f382e8d34ea4 | -12.37671 | -46.55394 | 2025-08-26 04:23:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19921811-e122-3d0b-9e0a-8d2cd26de467 | -12.77556 | -48.12871 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 831c568d-9d32-3010-b920-859a3ce819eb | -9.15748 | -59.56181 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| db8e1179-5653-37f2-9981-8123a828b041 | -13.52001 | -46.89643 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d8e6de5-d7d5-33d3-aa19-3c58cd990a5d | -15.18096 | -48.19372 | 2025-08-26 04:23:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82f78da2-50a9-30bd-84c1-083fb14e5b0d | -15.63016 | -52.7285 | 2025-08-26 04:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c24f651-2c68-3acd-a5c0-4ce9d34a4aed | -13.51826 | -46.90723 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 34906803-a8e5-3c38-a1ee-3e9b1d1b2f8e | -12.70084 | -47.88586 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a789c1f7-2aa6-3073-a34c-feed569ac3fa | -14.8505 | -47.15204 | 2025-08-26 04:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 470dbb7f-d9a4-37e2-b4ed-d202ee84286d | -12.73213 | -48.14551 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 33d40bd6-d933-3089-b605-34e98d659364 | -9.1887 | -59.44544 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 37cc57ec-4091-3b7a-9ce8-209139c7693c | -12.42257 | -43.48714 | 2025-08-26 04:23:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ecc3e216-d1bd-3044-b3b3-8c704072162c | -13.44375 | -46.99412 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b21af48e-dfd0-3a52-9fd0-beb88fd5f3a0 | -12.66557 | -47.86897 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc744817-d9bb-3635-9245-74fa21a9d8f1 | -11.6345 | -46.2065 | 2025-08-26 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22fc91e1-e63d-37a4-b8f5-67a0c2f6d3ad | -12.75131 | -48.09372 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b7b7adcf-2218-3fd3-95d5-f7473b992a6c | -15.03246 | -48.67089 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a3a631f-398b-37f0-bcb3-b5040b4286ac | -16.1554 | -40.35209 | 2025-08-26 04:23:00 | NPP-375D | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 04b7aa25-f9b3-3788-8720-209d9573872e | -14.30609 | -53.07446 | 2025-08-26 04:23:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a21b7c83-317b-34d1-bb20-ace9579d20f3 | -13.59135 | -48.19086 | 2025-08-26 04:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e28f1d7-0d6e-3947-ab4a-da7ba1c09768 | -14.36404 | -51.91631 | 2025-08-26 04:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5356aece-8062-3ebc-a388-ce0e7c99ea23 | -9.15689 | -59.564 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| d64a0c05-644c-3348-b369-e40338a148fd | -13.5277 | -46.91254 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8502da97-0be6-3b7d-9031-b9a26d7e2b96 | -11.30642 | -55.10572 | 2025-08-26 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| de5b06f5-1637-3f95-87ed-e99bc42f15cd | -13.16874 | -45.28835 | 2025-08-26 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ef63d526-5593-35cf-88d0-2b5597b93062 | -13.40866 | -46.8926 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| a9d3b35b-f891-38ab-9b07-09c928d03220 | -15.5722 | -43.85881 | 2025-08-26 04:23:00 | NPP-375D | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 3c6476bb-9dc4-3482-839d-df67e7d761d5 | -12.73024 | -48.15698 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c65c8ec-915d-3f88-9fec-ebf7b2686709 | -15.02507 | -48.50232 | 2025-08-26 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 652d30d6-9c9c-3a17-b6a8-fb1574359211 | -11.63673 | -44.8586 | 2025-08-26 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb299688-b218-3841-bf2b-4ff3bd7ecbf6 | -14.64302 | -49.07686 | 2025-08-26 04:23:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1b26fa00-b7e9-3035-802a-40ae77e5683a | -13.06107 | -46.31637 | 2025-08-26 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c104500a-ea88-3db2-8237-2faf2a1c2da1 | -12.94026 | -46.33702 | 2025-08-26 04:23:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1a839736-0c0f-3f16-aa26-99c833d72088 | -15.62112 | -52.70578 | 2025-08-26 04:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62d12046-cb6e-3dbe-a283-3ff8d1ab8401 | -9.16285 | -59.45765 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5bf7c7df-b86c-3f91-bce4-a92b3c7665cd | -12.77 | -48.11951 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ef07451-e65f-3c1b-a97f-910fc527f0cf | -11.6217 | -46.22255 | 2025-08-26 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 78739116-a465-3be1-b04e-54ce65f2e88c | -12.94138 | -46.32992 | 2025-08-26 04:23:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db130308-8529-3d6f-ae6a-091dbc04cf95 | -15.03881 | -48.50468 | 2025-08-26 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ab462d6b-e2a2-3ea7-95cf-832c25aee821 | -11.63461 | -46.41356 | 2025-08-26 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 74d7b89e-531a-3f81-985d-78409a5ebd7b | -12.74123 | -48.155 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7ecf80f-7b8b-3804-a379-6f7b4cbb7e6e | -13.60857 | -48.15061 | 2025-08-26 04:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 00ff7f03-410d-3001-94cd-f5efce03978d | -14.2529 | -48.03662 | 2025-08-26 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f7d3b8dc-b24a-314a-a787-6e76ed246b8a | -15.07084 | -48.5461 | 2025-08-26 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1f0b647-820a-3730-a876-178790e5a5d9 | -14.28255 | -49.13691 | 2025-08-26 04:23:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d08bd471-3fb6-3251-a913-2b890ba4a368 | -14.28325 | -49.13282 | 2025-08-26 04:23:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 78fb6f46-1588-37da-b6a9-619af4588fe4 | -11.05353 | -52.02175 | 2025-08-26 04:23:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90ee2f44-6d0e-3885-a68b-d46007f41004 | -12.75917 | -48.14164 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 113a1a51-43e6-30fc-acbe-9c5159b51f6f | -12.69238 | -47.87738 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93bcc0f8-68ef-3de3-a1c2-7757139bf142 | -12.95181 | -46.32405 | 2025-08-26 04:23:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfcb783a-9eaf-3f57-8e3b-304ee34e0314 | -9.18101 | -59.52036 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fab5dafc-d2ce-301c-ae3d-3b08d8accf4d | -11.63729 | -44.85503 | 2025-08-26 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74792d39-c901-3867-95c9-b5cbf174c192 | -12.38876 | -45.00312 | 2025-08-26 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04e859c8-1469-3551-9027-2ff015a42e26 | -11.3049 | -55.1044 | 2025-08-26 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3c98fad5-6c7e-3020-8c30-9101e6a7db85 | -13.42623 | -46.93247 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9286fb01-80c0-37be-a89b-4dbee949ad00 | -11.5502 | -50.46306 | 2025-08-26 04:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22a157e8-98e1-3e59-8f4b-69bd12cb9a73 | -12.70301 | -47.89399 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 79655e05-61cc-38d6-b6ff-b7428abc2a55 | -12.37223 | -46.5605 | 2025-08-26 04:23:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f1923125-61bf-3afc-a9ea-dfcb5c18d456 | -12.93089 | -46.30995 | 2025-08-26 04:23:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5fc5b4cd-2eb5-3670-ac45-f5f51a62e73b | -13.45769 | -46.99281 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14fa430c-aeb4-3c88-b870-eeb096e873d2 | -15.06475 | -48.69948 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f43e16dc-3e1d-3904-b198-251bdddea6f1 | -14.27832 | -49.14037 | 2025-08-26 04:23:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 688cce96-6376-3c13-a14a-056e19ba27c3 | -13.50221 | -46.88641 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3ad0c1b0-da1f-322e-9c81-3f9acfca80d9 | -15.11937 | -48.64929 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63d6719e-b413-34dd-9e35-ee9c346aad25 | -12.98661 | -45.22244 | 2025-08-26 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19841171-d575-3547-8b20-a7c8d0b591f9 | -13.42096 | -46.88004 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d207471c-a9cc-3973-8c4d-87343d1f00a9 | -14.28694 | -60.36518 | 2025-08-26 04:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e73fda46-ac05-3e33-a3c3-546d96b84f81 | -12.66962 | -47.86577 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe26a247-1e52-30c8-b20f-bd8fe38cc6cc | -9.17801 | -59.53514 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9fd143ca-75a2-3413-bae1-3e387f8fe0b4 | -14.40031 | -51.93845 | 2025-08-26 04:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4dd98fa9-df82-3c35-8031-8692dcbc971f | -9.18594 | -59.45478 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 394bd2ac-24a5-3157-b8ba-d5dda017f267 | -11.29466 | -53.96157 | 2025-08-26 04:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9392880-b6b2-368a-95b2-3473cd6c70ce | -11.30838 | -55.11559 | 2025-08-26 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| b458ac97-2d8a-3f65-a953-95419244e2c5 | -13.45435 | -46.99223 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b26dccdb-f1f0-395f-b0aa-9ab14f51c828 | -14.96988 | -52.88289 | 2025-08-26 04:23:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c27a38ad-9109-3a6d-8a0f-fa16492b1789 | -15.10684 | -48.63937 | 2025-08-26 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca612109-73e7-3788-9c02-5f727aa2616a | -11.55961 | -52.11618 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c77fe9f-ade4-3a17-9dfd-20dc9d344e42 | -10.74468 | -50.54745 | 2025-08-26 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| caaa3b0c-ca87-31cb-9e41-b6dc41f5d5dc | -12.75476 | -48.09431 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9e1c5579-65a6-33d1-a362-3f21c7df1c33 | -14.71697 | -45.38484 | 2025-08-26 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf32fd61-322a-36e7-988a-04652b04bdfb | -11.56678 | -52.12659 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| eb3f0082-48cd-370d-af22-6d4a43b3b3b6 | -13.39813 | -51.77246 | 2025-08-26 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| afcb8b7a-40a0-3e27-a661-e77a89af9613 | -9.18574 | -59.46003 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d5738c6c-1056-31d3-8fdf-faff44097ba6 | -12.41253 | -46.50139 | 2025-08-26 04:23:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b52d9707-7a2a-3ba5-8c55-364bf1f93a91 | -11.53453 | -52.12933 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 200b772d-caa3-3659-9a0e-306b8b375936 | -9.17226 | -59.52631 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| efb7efc4-5833-3201-a006-c5e31f4e9611 | -13.40294 | -51.76955 | 2025-08-26 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2fbd1ddf-fd66-3664-98dd-a13853020bfe | -12.76226 | -48.13524 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8f592bb5-d085-3620-b703-f9230968762a | -15.02926 | -48.69016 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README44.md)
