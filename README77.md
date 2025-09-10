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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6376afde-ee9c-39f8-abed-8920aff8a3ea | -16.05477 | -49.9706 | 2025-09-10 04:44:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0bbe13c9-ffa6-36d1-9529-d70986184372 | -14.35966 | -47.31164 | 2025-09-10 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27a9ba06-f2a0-313e-bca2-a8006373b605 | -15.47362 | -49.36379 | 2025-09-10 04:44:00 | NPP-375D | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 34a133be-aa68-3f7c-a887-5012ad268105 | -15.81411 | -52.2746 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d1af7ca-19f7-34f1-968a-f411f81e57c1 | -13.9772 | -46.66075 | 2025-09-10 04:44:00 | NPP-375D | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 277dd3ef-758c-3bf3-9ec2-0cd799d711d3 | -15.4759 | -49.37223 | 2025-09-10 04:44:00 | NPP-375D | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d164eb25-189b-3de2-9a1f-39520cdf0f57 | -14.90246 | -50.12616 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 98873ca9-c540-347a-9028-af16816bef47 | -18.33946 | -49.33044 | 2025-09-10 04:44:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ca109a79-8463-3341-88b5-3ea0c157ea0e | -15.10162 | -50.07788 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 98d4bba6-571e-359d-a582-ccbd713f866d | -17.69363 | -44.45988 | 2025-09-10 04:44:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ea60728-d4b9-34a6-8e46-0636391a083a | -12.54517 | -49.10228 | 2025-09-10 04:44:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f334ff8-7efb-32b6-ab89-2f2137063255 | -15.09203 | -50.07258 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bf828fcb-c0d9-3291-8d85-643c0b14f11e | -13.8996 | -47.98151 | 2025-09-10 04:44:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ec8586a-7825-3ade-8fbb-3ae6fc95ccc0 | -12.93515 | -54.80944 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 086ea694-26af-35f9-a7f0-1e8a68d78303 | -16.51298 | -55.1342 | 2025-09-10 04:44:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3b58b40e-8602-38cc-b5be-f3a9a9ad4ad9 | -12.93272 | -54.75674 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9599ef04-e174-30dd-9c9d-77013162396f | -16.45819 | -50.66662 | 2025-09-10 04:44:00 | NPP-375D | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 303083be-9548-3bed-b383-09548f5fe5db | -15.22578 | -44.03742 | 2025-09-10 04:44:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1ed30f4-fe9a-3c1a-a7b5-949e897cd031 | -13.04299 | -47.1657 | 2025-09-10 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8aead7f-1b5d-3c0b-9ef8-2ebc70eb0e52 | -12.04648 | -51.07875 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31407e58-68c6-3c10-b515-55ce0c16e592 | -13.19379 | -45.27471 | 2025-09-10 04:44:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 59aee393-fc58-38fd-9b20-bc9eca9105de | -13.29001 | -51.72618 | 2025-09-10 04:44:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ce1823f3-f02a-3f03-a778-a24e211aa09c | -18.00761 | -47.10591 | 2025-09-10 04:44:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab29be5d-e7df-38c7-9df2-04632e025f74 | -16.14414 | -47.89571 | 2025-09-10 04:44:00 | NPP-375D | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b73c53b1-9b10-363d-8cd0-bf066d6bbddc | -14.46613 | -53.33739 | 2025-09-10 04:44:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63481e70-c991-3328-b963-fd9b09122118 | -15.69303 | -49.89938 | 2025-09-10 04:44:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2118b1ac-8537-33d4-bf14-735b81746ade | -15.09541 | -50.07314 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b92f27cd-065d-34f3-945c-8a3a3392b0b6 | -16.70824 | -47.6573 | 2025-09-10 04:44:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c683e249-30e4-3833-9f85-32a60649993b | -15.76298 | -53.50738 | 2025-09-10 04:44:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 345687bd-7297-31d4-a2eb-5c0fd74f47b1 | -15.0115 | -48.02403 | 2025-09-10 04:44:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a350767a-1aaf-35b5-82e3-ee5378f8bbbc | -15.52146 | -48.37941 | 2025-09-10 04:44:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7de8e9b-494e-35e8-9dfa-7fe91d2d9aae | -13.97349 | -48.21919 | 2025-09-10 04:44:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5577706c-d90c-356e-b4be-58541f40320a | -14.33841 | -47.29852 | 2025-09-10 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d776f32-2eef-31de-8f03-88823f96b111 | -14.92815 | -55.9396 | 2025-09-10 04:44:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d66fb361-2bab-38ff-9afe-6bf9999de2e5 | -12.99809 | -48.01685 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f39624b1-c276-33fe-9fab-74495cd82d35 | -16.52241 | -55.14499 | 2025-09-10 04:44:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9e3ce1b8-670a-3a7f-bc99-e9ef0fa17e95 | -12.87961 | -47.96318 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 311fd2cb-56a3-3afa-96f3-07a0099552d8 | -13.22058 | -51.77347 | 2025-09-10 04:44:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a18c47ba-6555-3580-8fd4-3ff82b12769f | -14.54038 | -48.7462 | 2025-09-10 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 354c422d-ce23-3d73-a72a-d3271c4a0bca | -13.17981 | -47.25332 | 2025-09-10 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f3583153-2013-30ba-918a-595413f8d15a | -17.73341 | -44.48904 | 2025-09-10 04:44:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0a57eb92-f234-3330-b5e2-56a5b0221dfa | -15.90693 | -50.18914 | 2025-09-10 04:44:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4725328e-9fcf-38d4-8528-0a1d05648292 | -15.27566 | -53.78438 | 2025-09-10 04:44:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9f78068d-0fe6-300c-82d6-e6a1f723d9b3 | -12.04658 | -51.03519 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1121bf27-7083-39b5-a5a6-9d6cbb5afe62 | -14.24737 | -46.6932 | 2025-09-10 04:44:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 029c18f4-bde0-380a-b7f0-a1e7738c5a64 | -13.29393 | -51.72316 | 2025-09-10 04:44:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f88a8ce1-a90d-3e5e-976d-0b661b93ce58 | -14.90301 | -50.12251 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| cbf459f6-2c66-314f-8a64-d2955d978add | -13.28332 | -51.72507 | 2025-09-10 04:44:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e7099773-cbfc-3a7d-b744-849e940dc743 | -13.54174 | -44.13587 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ef6cc8a2-fabf-3eac-bf07-f9d848d9a96a | -15.8086 | -52.26614 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03bd0d69-1127-38c1-be6f-c1ee44613f65 | -13.94794 | -48.25502 | 2025-09-10 04:44:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 42c00522-cd4e-3b6b-a9b0-5f0a77e72198 | -17.2519 | -46.08584 | 2025-09-10 04:44:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b80489a-90d4-3101-80a1-223b51758b48 | -15.10618 | -50.09353 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0f134d4c-ddb8-3c5a-a93e-6aa2f56d4e14 | -16.62208 | -49.76679 | 2025-09-10 04:44:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 412f8bac-d45a-3edf-adea-41f4ef9540e4 | -15.09431 | -50.08043 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ae27346a-0f38-32f0-8c0b-9ece9f3a1205 | -19.17054 | -43.06624 | 2025-09-10 04:44:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9ab4b3e3-5f1a-337d-b55c-2d3c6b8aaa19 | -15.10956 | -50.09407 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2101a688-9ec1-37d7-9f70-ff019d834ef9 | -16.51662 | -55.13489 | 2025-09-10 04:44:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ea2b455d-aa40-32e1-9002-26230d110cb6 | -14.90667 | -55.85761 | 2025-09-10 04:44:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a59eca16-63fd-38a2-aed2-db6da56d3d9e | -15.48455 | -49.38554 | 2025-09-10 04:44:00 | NPP-375D | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 03a748a8-ec52-340d-b497-dc3a50fa787a | -15.14833 | -44.03069 | 2025-09-10 04:44:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 306889bf-1fd4-30ed-8f72-baae31e5cf8c | -15.02001 | -50.08788 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 462a3c14-15b2-3dd2-8305-21ef134c25bd | -12.9381 | -54.81474 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 820f34ab-fc17-3d20-9d28-2a24fac3c027 | -12.00756 | -50.98542 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d7e4620c-5c76-3495-9bbe-450e405d9a81 | -14.8633 | -49.53186 | 2025-09-10 04:44:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3b112560-a472-3a34-9608-4a938886b169 | -15.80584 | -52.26189 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2e9db4f-79da-3f0a-b817-cd6dd400555a | -16.04 | -49.97589 | 2025-09-10 04:44:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03058256-f854-3d4c-a8f3-4e59321c1961 | -16.34609 | -52.94059 | 2025-09-10 04:44:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6649a1ca-b909-3e4c-8d7b-3bcf6efe9268 | -14.56678 | -48.76252 | 2025-09-10 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 835403fa-d999-3145-94ec-fcee42ac0fb3 | -12.94553 | -54.74971 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0b340e5f-2a4b-3770-bbcd-e83432484399 | -17.74949 | -44.47528 | 2025-09-10 04:44:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 44e2e630-293a-303e-b8e4-7e004b1ee53c | -15.8786 | -52.20409 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf18152f-ac71-3a32-bd47-4e36942a0b66 | -13.96928 | -48.22299 | 2025-09-10 04:44:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fcf61ce3-07ba-3f37-a919-e99f575f19d0 | -12.02383 | -51.02782 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a77efc6f-8040-3867-84eb-226d3edd29b3 | -15.95048 | -48.10473 | 2025-09-10 04:44:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.1 |
| db6c4f74-3508-3dd5-8c20-631dbb50ac52 | -11.92298 | -51.06591 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13a35dbb-eb67-317f-b218-89d34c11f400 | -16.51514 | -55.14351 | 2025-09-10 04:44:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| fa882ec1-3f0e-3fe3-95c4-8c6b5a253b34 | -17.24475 | -46.07545 | 2025-09-10 04:44:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a1dd6d42-45f2-33f1-8436-1b63c3a43afc | -15.80817 | -52.24738 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 543e623e-f80a-305f-b9e0-a30f3d3e9b14 | -12.17364 | -50.62098 | 2025-09-10 04:44:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 430c8973-1769-32a2-b554-3d2de62b189b | -15.13556 | -52.39112 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c30c6f85-4b8e-3450-b60c-da097ba20be7 | -18.1363 | -51.72495 | 2025-09-10 04:44:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0f12b65-2cb8-355f-99bd-0dfa0268c99f | -13.97647 | -48.22387 | 2025-09-10 04:44:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| da6edd44-bfa5-38e8-889d-3c2f85b0fc89 | -12.98973 | -48.02389 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 765a8803-157f-3d90-b27b-1ffad082fbb3 | -14.92324 | -50.10326 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50bd3feb-23ff-32aa-a2db-9f156ec6b90f | -12.61791 | -56.96444 | 2025-09-10 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 767e6628-320a-384e-a7c9-4c7482a903f3 | -13.15025 | -45.28157 | 2025-09-10 04:44:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc0ee448-11bc-35a2-9bd3-6815485aa887 | -12.92497 | -54.77901 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8d0fac3f-3283-3165-9076-b0e848e4086e | -15.15368 | -44.02628 | 2025-09-10 04:44:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d87559e0-6883-398b-a790-db374c603f0b | -15.17786 | -47.94642 | 2025-09-10 04:44:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0591df5d-e72c-371d-b527-b113043b01d7 | -19.29463 | -47.98404 | 2025-09-10 04:44:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e9258e61-a6a1-3721-abd2-92a9e856db55 | -12.92416 | -54.78362 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e5ef1414-8d08-3983-a43c-1aeb13a38c60 | -13.96453 | -48.23059 | 2025-09-10 04:44:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c911012-db28-31e9-a2d1-16e0a24b5a11 | -18.95852 | -42.38802 | 2025-09-10 04:44:00 | NPP-375D | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8bb02ed2-9ef5-3733-a20a-41e214a083dd | -16.45695 | -51.97498 | 2025-09-10 04:44:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9f422223-b56a-38c8-875d-eaa0decd3b2d | -12.94927 | -54.75037 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 36436b65-4700-33e8-b5c9-40df6118e908 | -17.55709 | -44.54069 | 2025-09-10 04:44:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 68bb358c-08aa-318a-bb7d-4e2a61ccf3c8 | -15.80541 | -52.24321 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| abb45f6f-827c-3b2c-b603-158630d3fedc | -14.88445 | -55.86729 | 2025-09-10 04:44:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 393a552d-5b5d-31f2-9856-95e9e465c45d | -11.21346 | -54.9944 | 2025-09-10 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README78.md)
