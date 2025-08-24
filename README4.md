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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed929aed-4aa0-3a60-9b29-be0d30942cd6 | -20.084101 | -46.114498 | 2025-08-24 00:34:00 | METOP-C | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9b23509a-5e4c-3843-adfb-74f79c53e681 | -4.5506 | -43.223499 | 2025-08-24 00:34:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 28c2fc7b-9672-3bcb-8f1c-a3cfe7fce819 | -22.126499 | -43.2486 | 2025-08-24 00:34:00 | METOP-C | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 47482c75-216b-3539-b936-c9b16ed71c39 | -3.7943 | -47.569698 | 2025-08-24 00:34:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22ba0f5d-3dd1-3708-84d8-d4ddb16f0155 | -5.8595 | -52.089298 | 2025-08-24 00:34:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de6b94ab-7b79-3b55-a27f-f605d8a0c933 | -23.3297 | -47.843498 | 2025-08-24 00:34:00 | METOP-C | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 986eba7f-cd70-3235-83c0-bb1c087a0c57 | -8.1199 | -47.1441 | 2025-08-24 00:34:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 398dbba9-6802-3a69-b961-4f207536b0e6 | -7.0329 | -44.6562 | 2025-08-24 00:34:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1b1d57a7-0e36-3e92-9531-8b3e2cd4625a | -7.6131 | -45.2435 | 2025-08-24 00:34:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5f5df37d-797b-32a5-9662-3fe70bc7e0bc | -17.4028 | -42.614101 | 2025-08-24 00:34:00 | METOP-C | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a0c7dee1-2cda-3420-ab6f-f18128bd3f2d | -11.2766 | -44.975399 | 2025-08-24 00:34:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4ff63b8d-7ea3-3d35-92ab-d5a762bd7134 | -4.7835 | -45.324902 | 2025-08-24 00:34:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 04ef2ec5-576f-376d-b525-bfabe8c11226 | -9.0262 | -47.6479 | 2025-08-24 00:34:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4db42190-9f3b-3f65-a232-33b727380bcb | -10.6083 | -50.141499 | 2025-08-24 00:34:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 450941e7-135c-36d6-af56-0788d5f00455 | -10.599 | -44.3195 | 2025-08-24 00:34:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 12c7a9b9-7e34-3c1f-b6ad-1da0a688d44b | -19.840599 | -47.536301 | 2025-08-24 00:34:00 | METOP-C | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 96291dee-d15f-3037-9b61-e97044238541 | -11.275 | -44.968399 | 2025-08-24 00:34:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f27e1194-b133-3f7c-9376-23af7be69f17 | -22.0923 | -53.817501 | 2025-08-24 00:34:00 | METOP-C | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a99b49ca-f36c-383f-beec-7a681d060402 | -7.1688 | -44.663601 | 2025-08-24 00:34:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c6bd8bc9-0a60-30b6-be1f-a8dadd0a9c6c | -11.2848 | -44.966202 | 2025-08-24 00:34:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 524a39f1-f8b5-3b97-bf76-a85f0fd5354e | -3.5989 | -47.527401 | 2025-08-24 00:34:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79403540-f99f-32ac-a36e-394d1d55b708 | -8.7685 | -49.972198 | 2025-08-24 00:34:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89630c38-5709-3884-9e9e-fb3662363b57 | -10.4125 | -47.172298 | 2025-08-24 00:34:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dbc66cd0-996d-327a-8145-e735a352abbe | -12.9937 | -45.224201 | 2025-08-24 00:34:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d16936a7-52df-30fb-a26e-45957540062b | -4.2777 | -48.649502 | 2025-08-24 00:34:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cc4561b-4d29-38d8-bbbc-130586c202a4 | -16.7869 | -51.337502 | 2025-08-24 00:34:00 | METOP-C | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a26ec7e8-dcc8-3762-b2ca-de523a4587ee | -2.261 | -47.854801 | 2025-08-24 00:34:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bba807ff-d99f-3405-8d67-8ce7853b9ebd | -4.0185 | -49.5051 | 2025-08-24 00:34:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93e13226-ff47-39ae-83a6-e5582df5bace | -8.7514 | -46.746899 | 2025-08-24 00:34:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bf8a304f-7a65-3db3-9e60-b2f024a82dd5 | -2.9269 | -53.688599 | 2025-08-24 00:34:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abfe6c52-0c7b-39be-81b5-34d1a7cf7ca9 | -19.9284 | -44.216 | 2025-08-24 00:34:00 | METOP-C | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 408c0a05-460c-3e76-95f5-ff39622444df | -4.9539 | -55.7906 | 2025-08-24 00:34:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80ea20e9-0cee-3bfe-84a4-f37b22007db6 | -8.9034 | -47.330101 | 2025-08-24 00:34:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a45ee775-9cff-39fd-b2f7-bee9ddce9318 | -3.4404 | -49.0457 | 2025-08-24 00:34:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39af213a-c378-362d-b028-1bc64dbcdaa4 | -20.368799 | -46.757801 | 2025-08-24 00:34:00 | METOP-C | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d8d81fb6-09c6-3e73-87dd-6c3755d5c375 | -10.5317 | -47.153198 | 2025-08-24 00:34:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b8374802-b1f4-3714-bfc6-bf7b853fb060 | -17.394699 | -42.624001 | 2025-08-24 00:34:00 | METOP-C | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 57f5848e-a700-38b3-9f82-8f0b16d2f082 | -6.6141 | -48.048599 | 2025-08-24 00:34:00 | METOP-C | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| f96dc48c-9baf-3654-9a6f-852b583216bf | -19.7659 | -43.153301 | 2025-08-24 00:34:00 | METOP-C | BELA VISTA DE MINAS | MINAS GERAIS | Brasil | 3106002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 97a103d0-8add-3833-9486-2f8561fff221 | -14.9474 | -48.0042 | 2025-08-24 00:34:00 | METOP-C | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b5d703e2-6984-3ee5-b017-2eebb4c7e484 | -20.3508 | -51.681099 | 2025-08-24 00:34:00 | METOP-C | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d5aaac59-bfaa-3069-ad5b-6e5cdd44666e | -10.4059 | -47.1889 | 2025-08-24 00:34:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 55580cfa-1ab2-3ca6-9138-d5db503872f1 | -11.5198 | -51.91 | 2025-08-24 00:34:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 61a968df-a815-359e-b926-33be661dcf7b | -8.5342 | -48.858601 | 2025-08-24 00:34:00 | METOP-C | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| a651c67b-c206-3772-a028-9f65414aad50 | -11.1043 | -44.764198 | 2025-08-24 00:34:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7175be64-fdf4-3b0f-be59-3b6094350ee9 | -13.3312 | -43.190102 | 2025-08-24 00:34:00 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 54f49b08-51f3-38f6-b04b-9926687e7634 | -23.364599 | -46.9487 | 2025-08-24 00:34:00 | METOP-C | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 899f6cb6-a2c6-31cd-a86e-649dc76773cd | -5.5854 | -45.801998 | 2025-08-24 00:34:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4ccbf644-6121-317b-9f7f-215638dc75a8 | -20.3573 | -46.751202 | 2025-08-24 00:34:00 | METOP-C | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 419a03a8-510b-36c8-a601-f618e3dc5b7b | -10.6006 | -50.153198 | 2025-08-24 00:34:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a22245ff-a455-3380-8044-4e7b2b8bcec5 | -11.1189 | -44.783001 | 2025-08-24 00:34:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e52f0585-e30a-33f0-8cb5-91ba7afc1635 | -12.7377 | -48.1217 | 2025-08-24 00:34:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b846aac0-c1e9-3a97-af92-430769563940 | -16.7896 | -51.351799 | 2025-08-24 00:34:00 | METOP-C | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2fc6d858-939e-33fc-a6cd-ce33f75913f1 | -17.0389 | -47.1838 | 2025-08-24 00:34:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 41dd5fba-337d-3212-aefb-2933a5c527eb | -22.082701 | -53.819099 | 2025-08-24 00:34:00 | METOP-C | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a999a1d2-b0d1-333b-b95c-b05a9ac77ac0 | -6.0549 | -44.0051 | 2025-08-24 00:34:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c25c83e0-fc0f-3fb9-b51b-e8132497b5d7 | -14.8022 | -47.947201 | 2025-08-24 00:34:00 | METOP-C | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| aca031cf-44c3-33f3-9bfd-975faf7550ef | -14.7942 | -47.957699 | 2025-08-24 00:34:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 929f5722-b6df-3de1-87ff-15faf4643bd3 | -5.6545 | -45.1647 | 2025-08-24 00:34:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f188ba59-75a6-366f-afcd-2a8e20e15a0f | -6.1884 | -45.4202 | 2025-08-24 00:34:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0355ce6f-5039-3729-bf15-879c2c7758f9 | -17.5896 | -46.099998 | 2025-08-24 00:34:00 | METOP-C | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6b109948-ef8e-3aed-8929-8afdc81c49ab | -16.7924 | -51.3661 | 2025-08-24 00:34:00 | METOP-C | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c19b0dc3-1006-3fd9-bf31-1f263a12979b | -2.2594 | -47.848 | 2025-08-24 00:34:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6f25690-9c73-3a0a-a080-59e1766c70b6 | -3.0607 | -49.505299 | 2025-08-24 00:34:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 173160dc-820b-3c8d-a16e-843bcda92dbb | -14.8102 | -47.9366 | 2025-08-24 00:34:00 | METOP-C | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| da3d890a-a843-3778-8b64-a6ea56d3b175 | -7.1803 | -44.6688 | 2025-08-24 00:34:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a72397d9-b384-3b34-bd51-2e62fd817851 | -4.2761 | -48.642399 | 2025-08-24 00:34:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0d1a0c3-80eb-35e2-9c6f-3c43d30321a8 | -13.4759 | -47.0266 | 2025-08-24 00:34:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5933b55f-767b-302e-bf63-4b0677b95c37 | -8.7606 | -49.983299 | 2025-08-24 00:34:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1137a8f9-825a-3f18-9a75-69e970365b55 | -11.5092 | -51.858601 | 2025-08-24 00:34:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 657b7dbc-7b07-3f47-90a2-d0966d3546c9 | -8.7587 | -49.9743 | 2025-08-24 00:34:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6a1534e-7eeb-3567-abc8-839feb61b421 | -11.2832 | -44.959202 | 2025-08-24 00:34:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 03415aa9-9411-38f7-951a-253000653756 | -6.588 | -44.563202 | 2025-08-24 00:34:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c87341db-30fa-30cc-b20b-58821e22344c | -6.2565 | -44.3367 | 2025-08-24 00:34:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9000c176-bd40-3d24-b587-6403a5dd8e1c | -4.3067 | -48.097599 | 2025-08-24 00:34:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecec4d32-76b0-32ea-bb00-4231ad6c1911 | -4.6925 | -43.257 | 2025-08-24 00:34:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9e3ed124-9a46-32c4-838d-8f33735bdfb5 | -3.7829 | -47.564999 | 2025-08-24 00:34:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 123c5065-aee1-3d40-8401-c6b8f3302e7a | -4.3051 | -48.090599 | 2025-08-24 00:34:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9fba61a-2246-3cf0-a6ed-d70b54476213 | -13.3295 | -43.182598 | 2025-08-24 00:34:00 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a25b9b61-9264-3628-a06c-810f7f2e0909 | -14.8159 | -55.929798 | 2025-08-24 00:34:00 | METOP-C | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c88cd457-b305-3be9-b4d3-4f89b83c5d38 | -13.5464 | -51.521599 | 2025-08-24 00:34:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f39174cb-b9cf-35c7-b5a7-603dca2ad280 | -23.362801 | -46.9389 | 2025-08-24 00:34:00 | METOP-C | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 560b4d4a-ac5a-3866-81cc-86fb00de9175 | -22.895599 | -45.393902 | 2025-08-24 00:34:00 | METOP-C | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 51075efc-36e7-3896-9d5e-bb56c9bc359e | -12.2102 | -47.114101 | 2025-08-24 00:34:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 71b6c943-e730-3747-8587-77e0d4d3933d | -8.7105 | -51.123299 | 2025-08-24 00:34:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a898d043-cac6-30d9-96f1-ccb3f7d5eda5 | -10.8158 | -46.397701 | 2025-08-24 00:34:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 061fef2a-aa9f-34a3-a02e-0714c12534df | -6.4259 | -53.372299 | 2025-08-24 00:34:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6582b87d-7ba9-37da-b3c3-abe96f9d3c65 | -11.5119 | -51.871399 | 2025-08-24 00:34:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 795305db-5ea7-3be6-a6dd-f2a5578f1edd | -13.0458 | -45.226898 | 2025-08-24 00:34:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 87b51f2a-9e0e-3c71-9810-11c11ef02c10 | -2.9094 | -48.299801 | 2025-08-24 00:34:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d80ff701-6e8e-3d7f-a627-1e25797959be | -6.3666 | -45.520901 | 2025-08-24 00:34:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4ea44442-f3a2-3a1d-8258-0ee57af50a73 | -4.5485 | -43.2145 | 2025-08-24 00:34:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a2561773-a059-3466-94ee-005a87b9a72b | -16.7967 | -51.335499 | 2025-08-24 00:34:00 | METOP-C | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 68bc2b00-c7d8-385f-92b9-03b592b97cab | -23.3577 | -45.812099 | 2025-08-24 00:34:00 | METOP-C | SANTA BRANCA | SÃO PAULO | Brasil | 3546009 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2eb42520-7c49-3cc6-a25e-9c4d4f75ccdd | -3.4457 | -44.142502 | 2025-08-24 00:34:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 17c453d8-af78-347f-92fc-f3231e1feb43 | -18.709299 | -40.008598 | 2025-08-24 00:34:00 | METOP-C | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fe57cefd-7210-3a88-ad97-5da636859e61 | -11.5216 | -51.8694 | 2025-08-24 00:34:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a6eb6d24-b628-3129-995a-efe99d952d40 | -8.7626 | -49.992298 | 2025-08-24 00:34:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70a11453-92d7-3b43-84c4-d8628c4c583b | -20.347799 | -51.664001 | 2025-08-24 00:34:00 | METOP-C | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3be7ffb5-7aa4-389c-81a4-e8b85326c3c8 | -10.8142 | -46.390701 | 2025-08-24 00:34:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README5.md)
