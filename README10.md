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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 433e0102-773a-3581-bd55-cb8ecadf9557 | -14.5691 | -48.0369 | 2025-09-06 01:05:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a7021793-14d6-3e4e-a6e2-376b47d7a089 | -6.4328 | -58.149899 | 2025-09-06 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 313a1ef6-4153-3722-a7da-936edb85d10e | -12.5166 | -53.869701 | 2025-09-06 01:05:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d57acd0b-ec87-360e-8be5-348379f13066 | -9.7924 | -48.3424 | 2025-09-06 01:05:00 | METOP-C | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5f669db9-d836-3d90-af4d-3e8f5361bbf4 | -6.3152 | -58.175499 | 2025-09-06 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b2b18fd-5f6c-33d3-a8d8-c3f7a3e90843 | -5.9431 | -53.798698 | 2025-09-06 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da9795d4-72af-3590-94be-436d058ae34c | -24.1394 | -49.508598 | 2025-09-06 01:05:00 | METOP-C | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | nan |
| e44377ad-c417-3dbd-842b-b91f52628440 | -4.4986 | -42.914799 | 2025-09-06 01:05:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fce94f7b-b8a7-355c-b083-a9898439bcb3 | -12.6938 | -44.9716 | 2025-09-06 01:05:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f88afa05-acc7-32f5-967e-2b9583998389 | -9.7269 | -51.076099 | 2025-09-06 01:05:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d9e9faf-9ee6-30a6-bf4d-dd41ed5be7fc | -5.9464 | -53.812599 | 2025-09-06 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94b8acad-0d99-3d41-bc62-b11f5a6332ed | -22.218201 | -45.876701 | 2025-09-06 01:05:00 | METOP-C | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9f175282-24da-378f-9799-42a944cc327d | -12.9976 | -54.834801 | 2025-09-06 01:05:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0d070d44-70df-3844-b66b-4e7f112df11e | -6.8297 | -52.813599 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22a1fd11-85a4-38cf-bffe-5c98ede8648e | -12.9266 | -48.052299 | 2025-09-06 01:05:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 996d589d-1e96-3dc1-a808-8ebb1ad9ed60 | -12.4923 | -53.8531 | 2025-09-06 01:05:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7e95e2b7-4360-329f-82fa-5e8cb26a4fc9 | -16.3286 | -52.954201 | 2025-09-06 01:05:00 | METOP-C | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 980e88b9-3a4d-3cb1-8d77-7817c8469ded | -15.7183 | -53.5951 | 2025-09-06 01:05:00 | METOP-C | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d39a035a-5ef6-3253-93b2-180648ab11ba | -15.7201 | -53.556599 | 2025-09-06 01:05:00 | METOP-C | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f171c404-8a5b-3a4b-8d98-19a3c32ad25d | -12.9764 | -54.831699 | 2025-09-06 01:05:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 043b0a0a-952c-39c5-a5ae-0b62ea84c808 | -4.3806 | -48.0919 | 2025-09-06 01:05:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16eb8d8d-09ec-34ed-a28d-3b6e15a6502e | -9.6827 | -49.292099 | 2025-09-06 01:05:00 | METOP-C | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 92eab47c-6284-3c5b-b352-22f353b432fc | -2.7822 | -49.628899 | 2025-09-06 01:05:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a82f76ac-b1e7-360e-836b-3f022b87123f | -15.7249 | -53.5784 | 2025-09-06 01:05:00 | METOP-C | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ffe11dce-2ad1-36b7-b0a4-be2483d26b86 | -4.489 | -42.917198 | 2025-09-06 01:05:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7a3b2e4f-e284-319f-a2f0-40cc6be41918 | -8.3488 | -52.555199 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75a60213-2ab7-3ae2-a61a-fb2b5e9bfd18 | -6.3133 | -58.166801 | 2025-09-06 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f52572ad-b975-3a4d-9e12-43bfdd330123 | -2.4689 | -47.785599 | 2025-09-06 01:05:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c4731d3-ee92-3813-b40c-2572652a0346 | -15.6873 | -53.594601 | 2025-09-06 01:05:00 | METOP-C | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b1908e08-d186-38ea-b100-0878beef53f3 | -8.3519 | -52.523998 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a89f7d0-9ccb-3b36-9e34-85e10b9204d0 | -22.839399 | -49.195801 | 2025-09-06 01:05:00 | METOP-C | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4ee62cab-e389-37ce-a0ee-6634b95d8a26 | -11.6377 | -54.5452 | 2025-09-06 01:05:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c4f0c1b4-c527-3fc5-97a5-f131c27b193e | -15.4275 | -52.976601 | 2025-09-06 01:05:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c4b34bdc-52a0-3eb2-ada7-423b6030e24b | -12.9781 | -54.792599 | 2025-09-06 01:05:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8c057cd3-3c7b-3985-b2b4-845628d36655 | -21.375 | -51.748699 | 2025-09-06 01:05:00 | METOP-C | SANTA MERCEDES | SÃO PAULO | Brasil | 3547106 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1f3b134c-a25e-34a6-8952-8c6b70c9c746 | -12.9601 | -54.804298 | 2025-09-06 01:05:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eef914b3-1ede-3467-b87f-e0baed9831be | -4.5162 | -42.944199 | 2025-09-06 01:05:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 07a1cfd8-2fe2-3784-af21-78c93eab3553 | -5.8637 | -51.726501 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b813a91-f394-371d-8416-97bcbba9e5be | -8.3603 | -52.5602 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b0034cf-1766-36e6-8e73-62d847b44da9 | -11.2112 | -55.034 | 2025-09-06 01:05:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bfe3cc15-7429-3def-8988-8939d12c2bc2 | -10.5959 | -44.334202 | 2025-09-06 01:05:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b1984411-49d8-3808-84ba-2c5be97a1b30 | -3.2363 | -50.8153 | 2025-09-06 01:05:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba942c43-2390-3568-9a82-95d10f2ad350 | -10.7683 | -48.276402 | 2025-09-06 01:05:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 229cfb06-2fd3-3862-bb35-436ad1b9d43d | -12.9944 | -54.82 | 2025-09-06 01:05:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cb0633fc-142a-347a-ae98-867c705cd132 | -14.5814 | -48.087002 | 2025-09-06 01:05:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c143a7f8-ad6e-382c-9f26-a2e68920178a | -7.3237 | -48.506302 | 2025-09-06 01:05:00 | METOP-C | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c9a16406-3df1-37ad-943c-27b51615a674 | -9.6981 | -49.483898 | 2025-09-06 01:05:00 | METOP-C | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 39b220f8-b185-3bd4-a423-060d67275fb8 | -24.1411 | -49.516102 | 2025-09-06 01:05:00 | METOP-C | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | nan |
| 11756c24-ada4-30e2-a000-cd16e0bdbbf7 | -24.154301 | -49.528801 | 2025-09-06 01:05:00 | METOP-C | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | nan |
| 5795e32f-880c-3324-873c-2f7319ca1f75 | -12.4742 | -53.864601 | 2025-09-06 01:05:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 142d1c6d-a585-34bc-b062-8bb8d04c36e1 | -6.828 | -52.8064 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3864fd9b-f4c9-36c3-b14d-20d5195a6786 | -16.296 | -50.490799 | 2025-09-06 01:05:00 | METOP-C | CÓRREGO DO OURO | GOIÁS | Brasil | 5205703 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| da97d7d1-6660-3524-b69b-6867e24fbbb8 | -10.4614 | -53.621101 | 2025-09-06 01:05:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bbbdde76-1a85-3f31-9442-5e8a83b18d2a | -9.8404 | -48.8349 | 2025-09-06 01:05:00 | METOP-C | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 20cf503a-463d-30d6-a960-2f13315920e8 | -14.5738 | -48.014198 | 2025-09-06 01:05:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3f030048-98e0-3c4e-bc36-961954d2531c | -6.2626 | -53.439201 | 2025-09-06 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7f19f9f-5b4c-33aa-b9d1-4ad3ba52fd0a | -6.8067 | -52.8036 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebd371db-b620-3783-8de9-c1dad0ef422a | -22.239901 | -48.749699 | 2025-09-06 01:05:00 | METOP-C | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 35261f61-6922-30cb-aeeb-ca5fbfcdff6f | -12.5201 | -53.839298 | 2025-09-06 01:05:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 566ad07a-8fed-3db5-b3b7-d9cfb7f5332f | -14.5666 | -48.026798 | 2025-09-06 01:05:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 77b6fa53-9bfd-3a20-afe2-ef9387d997fd | -7.7301 | -50.3218 | 2025-09-06 01:05:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4a2d12c-b806-3e8e-a925-6f08b7b8b8eb | -5.0984 | -56.147202 | 2025-09-06 01:05:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1544067-b3ec-306d-91de-b2d9b8582168 | -11.6284 | -52.230499 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 00e8ef76-9b27-3339-8d38-bf588ee3dff5 | -5.9781 | -53.592602 | 2025-09-06 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36026fe7-1c1e-3e62-ac73-b94ee34be473 | -3.1584 | -49.479698 | 2025-09-06 01:05:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 262af3ca-76e3-3a5a-9ea1-1ace61d559cf | -15.2066 | -52.358398 | 2025-09-06 01:05:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fe75faba-aa20-3c36-8f6e-1ab11adc0ff8 | -8.7643 | -49.6385 | 2025-09-06 01:05:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0a6bfec-6d15-3440-bb7a-b9f92e69bf99 | -9.2083 | -57.092899 | 2025-09-06 01:05:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7f130720-0d9b-3235-9e3c-4c7d775f02ab | -4.4905 | -42.8829 | 2025-09-06 01:05:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4c0ee0f0-cfff-3c3c-9cbf-b38ea3a1225d | -8.9274 | -48.649502 | 2025-09-06 01:05:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 0aaf8310-3c5d-3cdb-8193-759a0311837f | -22.837601 | -49.188099 | 2025-09-06 01:05:00 | METOP-C | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 264a9026-7a96-35a1-8100-5a4381408f34 | -15.5696 | -52.921101 | 2025-09-06 01:05:00 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dcadcb02-2bad-39db-a496-275dceb7beb7 | -16.3188 | -52.956501 | 2025-09-06 01:05:00 | METOP-C | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7f159568-52a8-39e1-a9ab-0f08ac5d974d | -12.4825 | -53.855301 | 2025-09-06 01:05:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ba7bc6ce-3546-3901-a45f-b15d6d6bfc14 | -15.7329 | -53.6147 | 2025-09-06 01:05:00 | METOP-C | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bded3527-1de1-3546-b09e-08487562e857 | -9.6818 | -51.1036 | 2025-09-06 01:05:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50d3f4a6-6cf5-33d1-a052-7248be06fce0 | -11.2079 | -55.019501 | 2025-09-06 01:05:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 50eb566f-c20e-3ecd-84bc-2a58c133906f | -15.7233 | -53.571098 | 2025-09-06 01:05:00 | METOP-C | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d8cfc71f-44ad-3c06-a3cd-0abbc64ad444 | -15.7297 | -53.600201 | 2025-09-06 01:05:00 | METOP-C | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5184d1fe-b9a1-3106-a28a-aceccdd23334 | -9.678 | -51.0877 | 2025-09-06 01:05:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9d54a4c-c8ce-35ee-b62f-6fdda7bc4c39 | -13.5552 | -48.124199 | 2025-09-06 01:05:00 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7e617572-302f-3d58-86b2-a53192a9787c | -6.1558 | -53.691898 | 2025-09-06 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 604c0e84-5680-377f-9e39-bf2acf4fc565 | -12.6841 | -44.974201 | 2025-09-06 01:05:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fb0c7489-0bbc-3912-905d-8b71cdad951b | -12.7916 | -48.1758 | 2025-09-06 01:05:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 84f6a9e8-b4ee-334d-af79-a7866eb677d7 | -5.9699 | -53.601799 | 2025-09-06 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1860c98d-4446-3cce-9156-965094f0f67a | -10.4598 | -53.614101 | 2025-09-06 01:05:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 26573706-8c76-3b2c-b9d8-9cee93cc876a | -15.7281 | -53.592899 | 2025-09-06 01:05:00 | METOP-C | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 15f40955-0455-35b3-ab89-914cd721ad3e | -12.5005 | -53.8438 | 2025-09-06 01:05:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2a836eaa-f761-3e6f-a0dc-70fe74cf3674 | -12.0123 | -47.785999 | 2025-09-06 01:05:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5fda1162-a609-3dde-bbbf-ae2d43d3076e | -18.4377 | -45.929401 | 2025-09-06 01:05:00 | METOP-C | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c7750143-4b80-3b45-a5b5-5e2f05997e51 | -12.8934 | -48.887501 | 2025-09-06 01:05:00 | METOP-C | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2f01299b-b759-361f-9e4a-c30ad83bafa5 | -20.5345 | -46.456902 | 2025-09-06 01:05:00 | METOP-C | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c88a1442-d7b6-317a-825b-9775e6eec320 | -6.0436 | -51.702 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c5aa429-7e2f-3991-9c57-c72624453a9f | -3.2461 | -50.813099 | 2025-09-06 01:05:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 729e9f43-e274-31da-a427-336d816ca8c9 | -4.5082 | -42.912399 | 2025-09-06 01:05:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| da534215-907e-323d-bece-3efc63e4da55 | -3.9842 | -47.896999 | 2025-09-06 01:05:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dab70d1d-7020-3530-8e86-50f593ed880d | -6.7773 | -52.810398 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| daae82ae-a248-3045-8670-7bba720a0a99 | -6.2642 | -53.446201 | 2025-09-06 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18bb03bb-5141-33d5-8e9d-c3a483f46c10 | -8.1505 | -54.929901 | 2025-09-06 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 918713bb-062b-30d6-8844-9e01cb339c29 | -8.3684 | -52.550701 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README11.md)
