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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ac3956a-0e21-3ad4-8e8d-3c17c06c57cf | -10.53386 | -47.76879 | 2025-10-19 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dcefd600-7f67-310c-b519-a06dd3238c46 | -12.46026 | -45.4294 | 2025-10-19 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 77997dd1-f578-3064-9ec6-fcab2c118841 | -12.98483 | -47.26687 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd48212c-7303-3ca8-a61c-09139771465e | -10.07157 | -49.66809 | 2025-10-19 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de96d4e4-f095-33fa-baf7-bf6871b0e60b | -12.82963 | -41.13178 | 2025-10-19 04:12:00 | NPP-375D | NOVA REDENÇÃO | BAHIA | Brasil | 2922854 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 3bccc094-6061-3433-a145-ee2616494994 | -13.19214 | -46.44428 | 2025-10-19 04:12:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa97185a-ef8d-323f-94d7-97416085dd9c | -10.88896 | -46.08747 | 2025-10-19 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| dba68835-b478-3c53-8000-d22dc51b2d28 | -13.26372 | -46.43848 | 2025-10-19 04:12:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e6872ae-4452-3bf6-ba1d-f6097f3c21e3 | -12.54979 | -45.4762 | 2025-10-19 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 41004152-ab65-39d8-b830-fe33d612fc5b | -10.81701 | -43.925 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9791d2c-bd00-379e-92c2-6ddf82a21182 | -10.42738 | -45.01293 | 2025-10-19 04:12:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7502a59b-2e68-3c49-b15d-e7d0c35ee6c6 | -8.54198 | -45.49205 | 2025-10-19 04:12:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd5bfe7c-ff0f-33ea-bff5-93fde6da07d7 | -10.95479 | -45.46926 | 2025-10-19 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4a0168d-4e2a-31a8-a975-7dbae54167c1 | -9.09984 | -48.9123 | 2025-10-19 04:12:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 74ee8208-5c99-3715-a5af-c5cec458a93b | -11.99953 | -46.77391 | 2025-10-19 04:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 3bc16776-501c-309b-b29e-97ee7a061088 | -10.88974 | -46.09533 | 2025-10-19 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 52d9be45-3444-3788-9dfc-66f63bbfcff0 | -13.18486 | -46.44301 | 2025-10-19 04:12:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0bcda8c2-05bc-39c6-8f2e-ec4dd552a8d7 | -11.77824 | -47.55835 | 2025-10-19 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50cd0fe0-372f-3d4d-912e-8b887c4171da | -9.72366 | -48.9123 | 2025-10-19 04:12:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5f9c7196-773d-34f3-a2cc-ad8c4c63ebd2 | -10.72298 | -44.54086 | 2025-10-19 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38feece8-5a8e-3192-a5eb-c9f0d429f8d9 | -13.90232 | -45.5315 | 2025-10-19 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 564d82b9-812a-38ee-89b7-44139b4e5d2e | -9.90952 | -45.95773 | 2025-10-19 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffc2e34f-89ca-391c-9640-1a3690d54845 | -10.8739 | -43.9415 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d447064d-b2f3-357c-bbbf-fb7e6389c037 | -12.15467 | -45.09751 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 916a32e5-8827-3c45-9258-1937c5591a04 | -11.89795 | -45.44259 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7dd6f302-7361-3992-ac2c-b055f97a6e57 | -9.53027 | -47.91184 | 2025-10-19 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8809960-204b-35f0-9eef-f236a2b3dd02 | -13.01695 | -46.95026 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| edb20cd5-5c17-3d28-aedc-9c185bbe9246 | -8.07857 | -47.09544 | 2025-10-19 04:12:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d4b7543-7565-3755-b920-998eb0e26bd6 | -7.44404 | -46.8404 | 2025-10-19 04:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 17f03791-65f2-32d6-aad2-196a342479e3 | -8.61135 | -40.19659 | 2025-10-19 04:12:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 30d9df37-effc-3061-b84f-a59fb776f3aa | -9.26041 | -44.34064 | 2025-10-19 04:12:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a3f24ff-5d1d-37bc-b626-2f1e2147048e | -10.53332 | -44.50603 | 2025-10-19 04:12:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 615a8bc5-cc58-39d8-87da-16c3e304ed43 | -10.62012 | -48.0134 | 2025-10-19 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 615d3d2d-8c6d-3859-9825-a4021e3a192a | -8.12807 | -47.6671 | 2025-10-19 04:12:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2da7c7b5-25b4-3f68-a936-cf36b4456a46 | -8.12055 | -42.2683 | 2025-10-19 04:12:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b8e4e59b-4cb5-3c2e-b1d8-5caee6a9e3e8 | -10.80967 | -43.92752 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a461bd5-6bcd-35a6-bc59-2fb012e9d400 | -8.24799 | -43.99514 | 2025-10-19 04:12:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d5caf76b-69fc-3ef3-bf8e-ef2b56ae6dbb | -14.27788 | -42.33452 | 2025-10-19 04:12:00 | NPP-375D | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 6f01a7ee-26de-39d5-9355-bae21d662d68 | -8.51527 | -49.50699 | 2025-10-19 04:12:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86b0e824-0778-3399-83d4-b6ada1e4f75f | -11.60709 | -44.05436 | 2025-10-19 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eaaace4e-56ea-3bbf-afc9-4c8da079e14a | -8.43639 | -44.14587 | 2025-10-19 04:12:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 02c6093c-4af6-31db-9ccc-1b4cd01fbc24 | -10.68805 | -44.54731 | 2025-10-19 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3e30595-6939-3377-8ddd-41b953a16351 | -12.15417 | -45.05794 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da046878-e841-3987-97e6-85980e1b04a9 | -13.53639 | -43.01361 | 2025-10-19 04:12:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| f97beb70-e04a-3587-a470-8929755d8fa6 | -13.1885 | -46.44361 | 2025-10-19 04:12:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57dbaf86-970e-39ef-a2ac-806a9eacf8af | -10.36035 | -47.4756 | 2025-10-19 04:12:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a3d29d8-c906-3b1c-960a-66861eda1ce2 | -12.98399 | -47.27163 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6593e40-2958-3607-a130-bf7257c3ce59 | -9.2488 | -43.75224 | 2025-10-19 04:12:00 | NPP-375D | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1ed23cc0-6a8e-3459-80fc-e71039a6ac1a | -8.24959 | -44.007 | 2025-10-19 04:12:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 09c88e24-ddf8-3303-8c79-54380c6fcb23 | -10.15396 | -44.52288 | 2025-10-19 04:12:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6ca5366f-6e64-3b05-a952-f00685bb04b6 | -14.09058 | -43.61807 | 2025-10-19 04:12:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4d89519-3916-34f4-8e78-1d3585426f4f | -8.25144 | -43.99572 | 2025-10-19 04:12:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e386d60e-4e64-3685-974d-b5a8733a70b0 | -11.61046 | -44.05492 | 2025-10-19 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8ad6327d-3007-3cb1-9376-9c7889cd09a2 | -11.13138 | -45.07885 | 2025-10-19 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7501798a-2e35-37dc-a127-b69eab4204d8 | -12.48961 | -45.42624 | 2025-10-19 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7448c371-304d-3bd5-ab25-311d41ffec2f | -13.89449 | -45.51411 | 2025-10-19 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e2790a45-52ab-3a3d-990d-1af3571b4b01 | -10.33782 | -47.77228 | 2025-10-19 04:12:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b3116d2-a806-3662-b131-fcd55ab6dd99 | -10.09738 | -44.56435 | 2025-10-19 04:12:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| abf264fb-8fe7-3b9a-84a6-19c5adaa020f | -11.00939 | -47.88614 | 2025-10-19 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 937ace29-7d30-32f6-af69-c480144991e2 | -9.76553 | -47.87776 | 2025-10-19 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff4d9884-f815-3f42-a15f-12eb6cb8f595 | -10.5367 | -44.0401 | 2025-10-19 04:12:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6d7c64a-3a67-38fe-9432-bcb9739c7b82 | -8.25021 | -44.00324 | 2025-10-19 04:12:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b54e6c21-9fda-36b2-a742-f886d7182f49 | -9.93702 | -47.12529 | 2025-10-19 04:12:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2827760b-56c9-3944-b8b5-2b6c12637ab6 | -12.45893 | -45.43731 | 2025-10-19 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2f57a98-11fe-3694-a31a-e996fd529a9f | -10.57977 | -41.506 | 2025-10-19 04:12:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1816c43a-2727-39a5-90b6-8edcb93c6d02 | -8.56778 | -48.51676 | 2025-10-19 04:12:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0f9f0609-720b-3dc7-882f-76f651b1c0c7 | -8.02567 | -43.92194 | 2025-10-19 04:12:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76395e09-ce77-3ddc-8960-c567455c358b | -12.9823 | -47.28124 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cec1e464-41d9-3003-bd3c-7bd3829edb5b | -11.62657 | -44.08382 | 2025-10-19 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9e515dea-0b53-30fc-9512-9ca14b4e1af7 | -8.44022 | -44.16586 | 2025-10-19 04:12:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e79bea76-cff9-340b-a557-5a58b5bd3ac4 | -7.97669 | -45.88785 | 2025-10-19 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be8110c7-ccb1-3e26-aabf-d18e22ea0d60 | -12.98612 | -47.28193 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b070bb15-8c99-3242-96f7-672ab2e2982c | -10.1256 | -45.5127 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 022b05b7-e09c-36ff-bcfb-494e06ff1f4b | -11.63569 | -44.07037 | 2025-10-19 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 406d2fd3-6414-3824-83a7-00bede1413df | -10.50349 | -44.41655 | 2025-10-19 04:12:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 755b3bdd-5979-39b2-833c-50513574c8be | -12.98315 | -47.27644 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c71c9017-6fec-3679-8c6f-1ffe62e818ab | -7.84031 | -45.52901 | 2025-10-19 04:12:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9bf235a-4746-37aa-9f34-f2709d56c592 | -12.14725 | -45.05673 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 46e00f4b-2fe0-38c5-a2a6-29a2dfa0c34e | -8.21294 | -43.95931 | 2025-10-19 04:12:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ba542f6a-668b-3bdc-b820-d09edf81bc4b | -13.84223 | -43.7279 | 2025-10-19 04:12:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3049075d-25ba-30c4-a4d6-e10642e44c68 | -9.71356 | -43.37872 | 2025-10-19 04:12:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 68cddb8e-d378-3fbd-9be1-46ea4af90994 | -8.07134 | -46.79905 | 2025-10-19 04:12:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a749001d-49b8-3db9-936c-b10b66f60067 | -11.89508 | -45.43814 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88280463-9488-36ea-b620-0f469756505c | -10.86158 | -43.9319 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7f4bd88a-0153-3ebc-9744-25472660eb20 | -7.44748 | -46.84464 | 2025-10-19 04:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 512cd795-27e5-3642-8ccc-8cffa2985021 | -10.85979 | -43.94286 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0ea5e324-d998-3207-9439-5c9ee8907535 | -11.63156 | -44.09589 | 2025-10-19 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd5aa982-6369-354f-80ad-ca3a295f784f | -9.66508 | -44.55827 | 2025-10-19 04:12:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe51e34c-83a8-3c44-9905-8648bf5641a0 | -10.53011 | -44.14503 | 2025-10-19 04:12:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a01ebd3-2b12-3bd1-8f8f-baf70e3c0df6 | -11.28127 | -47.05069 | 2025-10-19 04:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d80f0392-9beb-3e8a-9da8-13fee1457513 | -13.88973 | -45.52132 | 2025-10-19 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 67f2123c-997d-37a4-87b6-3194850d01ab | -12.99162 | -47.27299 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3564f0f3-f548-3a16-bf23-54d5b3dd9015 | -8.3178 | -49.48733 | 2025-10-19 04:12:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6f144e27-e10a-3ccf-bb60-2c46498fbfa2 | -10.63407 | -48.03142 | 2025-10-19 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a13a7765-c120-3148-8752-86e8057d2358 | -12.18654 | -45.09885 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2170b6e9-6398-326e-b10b-65792defd006 | -13.76888 | -42.9749 | 2025-10-19 04:12:00 | NPP-375D | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c7938eb0-d252-3fad-998b-f17dde052df8 | -10.84807 | -43.92966 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3e5d7dc-2e84-3abb-9fac-0972ca1ef75a | -9.95448 | -44.0098 | 2025-10-19 04:12:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26033434-f7ed-32e2-a8b7-3b05df51554c | -12.98567 | -47.26212 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30b3db9c-253d-30ad-91a4-6c8ae1d8854d | -9.18095 | -43.23766 | 2025-10-19 04:12:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README30.md)
