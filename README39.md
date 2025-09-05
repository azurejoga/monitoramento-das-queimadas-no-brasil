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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00899b9b-8a99-31b6-bef6-fc24f40f36af | -15.54834 | -48.4197 | 2025-09-05 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d716116d-26e2-3960-8600-7cfa67dd50ef | -19.68687 | -54.81065 | 2025-09-05 04:38:00 | NPP-375D | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9acbe0b-70f8-351f-b36b-651048422ac1 | -12.96788 | -54.78354 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cbfe8020-bbee-3a76-a59a-8c78ea339427 | -12.9054 | -57.00443 | 2025-09-05 04:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8050f27c-0bee-3270-92b7-1a368d339b77 | -15.5937 | -52.92207 | 2025-09-05 04:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3dff221f-4015-30e2-9777-9ac663ef82e6 | -14.73391 | -47.48439 | 2025-09-05 04:38:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8f4090fc-5ebf-3e8e-8b9b-8303fd2775dd | -12.98443 | -54.81012 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 58970166-8313-30b7-9c91-09876f1a24be | -15.04996 | -50.04294 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d776d16-84c8-3c45-ab7c-29e4d00f5371 | -15.62378 | -52.89725 | 2025-09-05 04:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d669f63d-96be-3b54-a5f9-ed8c84d1cdea | -15.58518 | -52.88589 | 2025-09-05 04:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d76db083-96b9-322b-92b3-4d371cc08688 | -20.39418 | -51.34271 | 2025-09-05 04:38:00 | NPP-375D | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 758320ea-9af8-3246-8e90-9de765fa4801 | -15.71259 | -53.61862 | 2025-09-05 04:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36844d42-af19-3bea-8d99-755cca1cd299 | -14.28559 | -45.21424 | 2025-09-05 04:38:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8dc50b0a-62c8-36e6-ae23-f738dc287641 | -21.27591 | -44.92112 | 2025-09-05 04:38:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ca39dd09-119a-37a3-b775-751069080f4a | -15.15657 | -52.3909 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1db7aa42-074f-3bc1-baf3-a132929d487b | -14.37693 | -53.12582 | 2025-09-05 04:38:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd2aae93-92da-305e-a421-45e363eb06db | -15.06099 | -50.0595 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b002f1a-f0bd-39b0-ad1d-b33f5efa7d8f | -15.55173 | -48.42024 | 2025-09-05 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9f67774-17ad-3685-83f8-1b8598b6956f | -14.7368 | -47.48887 | 2025-09-05 04:38:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4deb11b-907b-34a3-b07d-dee9e09aad9e | -14.55334 | -48.08543 | 2025-09-05 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34563420-f5d3-35fb-89d5-79923d6320c6 | -14.74028 | -47.4894 | 2025-09-05 04:38:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33942a16-417f-3946-b3c8-4fbbc6fd284b | -12.96927 | -54.79943 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e851c1ec-4c5d-3d4d-9142-a0a031a850f8 | -12.98374 | -54.81393 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6d7f1f6b-7d3f-32d8-80e6-435ec5c15e09 | -15.01107 | -50.08111 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be471ac4-c246-3be4-b334-6d1dc92f8e24 | -16.49945 | -43.73109 | 2025-09-05 04:38:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2cb235f5-2f3e-367e-8b09-eeed57ec027c | -23.39169 | -46.8444 | 2025-09-05 04:40:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5bcd0a6f-c57e-3568-a948-ab6182fb48e5 | -23.3601 | -46.32514 | 2025-09-05 04:40:00 | NPP-375D | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f04f0900-42c6-3214-9af0-ef4359d76432 | -23.36056 | -46.32128 | 2025-09-05 04:40:00 | NPP-375D | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 4f8172d5-ed3d-3ca8-ad99-df4f23e24e56 | -22.65719 | -46.81803 | 2025-09-05 04:40:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 6704c223-9c74-341f-b8d7-6ac892bc3991 | -24.91844 | -49.7376 | 2025-09-05 04:40:00 | NPP-375D | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c5fe2753-0411-300c-9c89-bed8a16122f1 | -21.79948 | -46.7921 | 2025-09-05 04:40:00 | NPP-375D | SÃO SEBASTIÃO DA GRAMA | SÃO PAULO | Brasil | 3550803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 1b4f86c4-7081-3e97-b3a5-a0008fed3e16 | -23.09124 | -49.85997 | 2025-09-05 04:40:00 | NPP-375D | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b951ee8d-ef3f-3a59-b997-783517461cfb | -24.37968 | -50.68786 | 2025-09-05 04:40:00 | NPP-375D | TELÊMACO BORBA | PARANÁ | Brasil | 4127106 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| db989578-1e57-3ac1-9f56-82193d345a12 | -22.92271 | -49.60693 | 2025-09-05 04:40:00 | NPP-375D | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| fd01e9e6-d100-3e47-8b5d-941ef6e17cbb | -22.5095 | -47.69765 | 2025-09-05 04:40:00 | NPP-375D | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ba4883f8-3fa6-3c46-b79c-29384ca4c6c5 | -23.08153 | -48.91875 | 2025-09-05 04:40:00 | NPP-375D | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 96008573-2ff3-33fe-917b-4cf17e78924f | -23.12806 | -45.76474 | 2025-09-05 04:40:00 | NPP-375D | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| cb56d44b-4bb3-3b61-8a6d-429ff3cdbedb | -22.29647 | -54.81969 | 2025-09-05 04:40:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c87b848d-633d-3677-87bf-cfb550b5bca9 | -22.4629 | -49.40339 | 2025-09-05 04:40:00 | NPP-375D | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 202f028c-de18-3197-bebe-da179960f4c7 | -23.12385 | -45.7641 | 2025-09-05 04:40:00 | NPP-375D | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 98669564-a3bf-3971-8f5e-fb14c6579e40 | -21.80337 | -46.79272 | 2025-09-05 04:40:00 | NPP-375D | SÃO SEBASTIÃO DA GRAMA | SÃO PAULO | Brasil | 3550803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6b4423b2-a8d0-3a65-81ed-7b2590e5c2b0 | -23.35968 | -47.16511 | 2025-09-05 04:40:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4f2624d2-bce0-3115-bc7e-c55dccbb587e | -22.27107 | -49.56685 | 2025-09-05 04:40:00 | NPP-375D | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3bae4f71-5689-3cad-81fc-d7bf56d9b3b7 | -20.85761 | -54.98859 | 2025-09-05 04:40:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b6dfb347-a49f-36d4-9e45-94e08ff13238 | -22.66892 | -46.82018 | 2025-09-05 04:40:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 80d90d00-285a-3ca7-9d91-dc252ec7c7e3 | -22.26419 | -49.56573 | 2025-09-05 04:40:00 | NPP-375D | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5d21374a-824b-36e7-acb2-aef22557fb69 | -23.83772 | -50.01638 | 2025-09-05 04:40:00 | NPP-375D | TOMAZINA | PARANÁ | Brasil | 4127809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a90e80c8-f4bc-3be1-b4c4-d36f58ef6106 | -22.6611 | -46.81879 | 2025-09-05 04:40:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| dd0fe25c-d975-3d11-bc95-6aeb1dc036c5 | -21.80207 | -46.80285 | 2025-09-05 04:40:00 | NPP-375D | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cd68643e-385d-337c-b90e-7c442bc30267 | -22.27699 | -47.62659 | 2025-09-05 04:40:00 | NPP-375D | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 82fe968c-9418-3f1b-8430-6fe0cf4c9944 | -22.75996 | -46.45277 | 2025-09-05 04:40:00 | NPP-375D | PEDRA BELA | SÃO PAULO | Brasil | 3536802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5cb7bf81-fbec-374f-a648-c2043521b4d1 | -21.79819 | -46.80217 | 2025-09-05 04:40:00 | NPP-375D | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| f31ff76d-93c0-3155-879e-6e95e6cc4e96 | -24.91853 | -49.74101 | 2025-09-05 04:40:00 | NPP-375D | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 388013ef-0e97-34b2-b09e-a746ad82e04f | -22.27164 | -49.56292 | 2025-09-05 04:40:00 | NPP-375D | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 44fcce98-8d66-3f29-bab6-1aa454ae23a5 | -23.41951 | -46.97527 | 2025-09-05 04:40:00 | NPP-375D | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4485b706-3dda-3ab8-a274-55c5f3fb8300 | -22.66501 | -46.8195 | 2025-09-05 04:40:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 4f689986-de9a-3da0-a1f7-ce02e9ba191c | -22.67342 | -46.22645 | 2025-09-05 04:40:00 | NPP-375D | ITAPEVA | MINAS GERAIS | Brasil | 3133600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8ec52ceb-9073-3552-8689-ef3f0b41f58a | -22.48949 | -52.76571 | 2025-09-05 04:40:00 | NPP-375D | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 922187f5-4de1-34a5-a960-b7c567c00eb8 | -25.09302 | -49.79863 | 2025-09-05 04:40:00 | NPP-375D | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 532c833a-f571-3c1e-9df3-f84a9ceb7511 | -22.68558 | -47.13128 | 2025-09-05 04:40:00 | NPP-375D | COSMÓPOLIS | SÃO PAULO | Brasil | 3512803 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d99b98b-373b-3965-8a9b-6294c201c434 | -22.33309 | -54.78162 | 2025-09-05 04:40:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b7929e3-4591-3211-bb04-4e34e96c81c7 | -21.79884 | -46.79712 | 2025-09-05 04:40:00 | NPP-375D | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 7660ede6-cb3d-3422-8215-6b2b98e54662 | -23.04512 | -47.82458 | 2025-09-05 04:40:00 | NPP-375D | LARANJAL PAULISTA | SÃO PAULO | Brasil | 3526407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f644d48c-d951-3545-b5c3-c7a5f5250950 | -22.27797 | -49.56794 | 2025-09-05 04:40:00 | NPP-375D | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 23e01b0d-3dc5-3dab-a60a-aa12b0385794 | -21.80272 | -46.79779 | 2025-09-05 04:40:00 | NPP-375D | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a5df4d7d-8782-34a5-a1dd-cbd63fc33603 | -23.37385 | -47.17822 | 2025-09-05 04:40:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fe57651d-ab6c-3e5c-9a09-94a521a156d9 | -22.49286 | -52.76636 | 2025-09-05 04:40:00 | NPP-375D | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b2116eb5-11ae-3548-aa1c-d8bbd7add5c5 | -22.49274 | -47.44698 | 2025-09-05 04:40:00 | NPP-375D | CORDEIRÓPOLIS | SÃO PAULO | Brasil | 3512407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4bfb1a4f-fba5-3f32-9e6e-45693de13e72 | -21.26119 | -50.29636 | 2025-09-05 04:40:00 | NPP-375D | BIRIGUI | SÃO PAULO | Brasil | 3506508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4a667b6c-0a35-389c-a630-df9097f91e54 | -23.37451 | -47.17302 | 2025-09-05 04:40:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4443fa43-9ccf-3fd0-b2f1-c8cd97b3ec6c | -22.04972 | -47.90023 | 2025-09-05 04:40:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 88c1face-4185-357f-bc05-9706796cb532 | -24.20119 | -50.15031 | 2025-09-05 04:40:00 | NPP-375D | ARAPOTI | PARANÁ | Brasil | 4101606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 956f8319-5ee6-3212-979e-03efc63a2606 | -23.43881 | -47.04313 | 2025-09-05 04:40:00 | NPP-375D | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bb89f878-9a8a-32f6-b4f0-b361bbccf64f | -23.17725 | -46.81492 | 2025-09-05 04:40:00 | NPP-375D | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 77d32ed9-2d67-3689-8aa2-ecb6280c1b4a | -20.88878 | -54.9857 | 2025-09-05 04:40:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 598e3633-4c5e-3887-aa9c-9f9cd1b766bd | -22.91926 | -49.60636 | 2025-09-05 04:40:00 | NPP-375D | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 1a95d535-3bc7-31ab-88ed-34e372af9128 | -22.51387 | -47.69341 | 2025-09-05 04:40:00 | NPP-375D | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 592ad209-901f-37f2-844c-023c8f15bb90 | -22.26075 | -47.6339 | 2025-09-05 04:40:00 | NPP-375D | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1f8af894-5e2e-3795-a292-c24c67de41b6 | -22.26691 | -47.64477 | 2025-09-05 04:40:00 | NPP-375D | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5f745e1-15eb-3881-8a8c-43b5a5887e1b | -22.51988 | -47.0883 | 2025-09-05 04:40:00 | NPP-375D | ARTUR NOGUEIRA | SÃO PAULO | Brasil | 3503802 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b98047ab-897a-3fcd-a177-06433e5937e8 | -25.62603 | -49.73699 | 2025-09-05 04:40:00 | NPP-375D | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d994978d-c6da-3ecc-b805-2679ff12e91f | -23.39102 | -46.84979 | 2025-09-05 04:40:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 3259642f-7b70-3184-a1e1-51dec5c59c5c | -23.39499 | -46.85031 | 2025-09-05 04:40:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 446d5416-74e9-3cb3-981a-1bcb696888d5 | -22.50996 | -47.6909 | 2025-09-05 04:40:00 | NPP-375D | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 052bb10f-5c57-3c55-9e2c-2a9929839206 | -23.12855 | -45.76062 | 2025-09-05 04:40:00 | NPP-375D | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 61e94fd9-ae0b-35bd-894f-9f828eede9d4 | -22.28072 | -47.6272 | 2025-09-05 04:40:00 | NPP-375D | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 3b198861-f19c-369b-9df9-19916249c774 | -22.68449 | -47.1297 | 2025-09-05 04:40:00 | NPP-375D | COSMÓPOLIS | SÃO PAULO | Brasil | 3512803 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a74ad45-0da4-3bb1-9076-d932354482f9 | -23.10976 | -51.51387 | 2025-09-05 04:40:00 | NPP-375D | JAGUAPITÃ | PARANÁ | Brasil | 4111902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d9866f9e-a48c-370f-b654-1add75d37bdd | -23.04139 | -47.82399 | 2025-09-05 04:40:00 | NPP-375D | LARANJAL PAULISTA | SÃO PAULO | Brasil | 3526407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2fcc4c99-e8a7-3b1d-b514-6d3e7475a046 | -22.44599 | -47.56861 | 2025-09-05 04:40:00 | NPP-375D | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 75e8632e-a5b5-3e7b-a41f-d0a3db2d70af | -22.27452 | -49.56739 | 2025-09-05 04:40:00 | NPP-375D | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5a599a28-5252-33c8-af3b-d81baea22f21 | -22.67995 | -47.13428 | 2025-09-05 04:40:00 | NPP-375D | COSMÓPOLIS | SÃO PAULO | Brasil | 3512803 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa81357d-0fb7-3659-ac9c-84cacceb25aa | -23.07799 | -48.91816 | 2025-09-05 04:40:00 | NPP-375D | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a3abf9f-b5a7-3b8e-9b44-0e0bbd57cb29 | -22.51014 | -47.69279 | 2025-09-05 04:40:00 | NPP-375D | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9720daba-c4f1-3eee-80a4-5e2f72cd5d78 | -23.47265 | -46.82417 | 2025-09-05 04:40:00 | NPP-375D | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 678b88a9-1d2e-375a-820a-569e97b77241 | -22.68062 | -47.12918 | 2025-09-05 04:40:00 | NPP-375D | COSMÓPOLIS | SÃO PAULO | Brasil | 3512803 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 180ccf83-9b43-33d4-9fb3-2d82816a506c | -23.1131 | -51.51448 | 2025-09-05 04:40:00 | NPP-375D | JAGUAPITÃ | PARANÁ | Brasil | 4111902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 669020af-581b-39ea-b569-ae21e0ee13e0 | -22.5137 | -47.6915 | 2025-09-05 04:40:00 | NPP-375D | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0f140754-391c-3a34-8f05-d26116895865 | -22.26763 | -49.56629 | 2025-09-05 04:40:00 | NPP-375D | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ef4913d1-8b95-3860-ae8c-c133863b3d3d | -22.19039 | -54.91084 | 2025-09-05 04:40:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |


[Clique aqui para ver as próximas entradas](README40.md)
