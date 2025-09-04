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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51bce748-f84e-36ab-add8-c862f8eb0fe7 | -14.37976 | -53.23226 | 2025-09-04 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64ab62e2-d241-3980-b1a3-db9deab57fd4 | -12.49949 | -53.84199 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a17dd0c-bb25-3b95-85b0-e8dce7ecd04a | -12.90074 | -56.93615 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 55a10c5c-5730-3f1e-844f-e1721d5a8129 | -15.98805 | -55.97984 | 2025-09-04 04:55:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4b5ad0cf-30d3-3c6d-8876-13003b88e87f | -14.53408 | -48.06638 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 229acb15-0244-32c0-a582-aaf320b0b3d9 | -10.09817 | -54.79211 | 2025-09-04 04:55:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 682bf7fd-15ce-30d3-a230-89cbc72ba2bb | -15.00727 | -50.06724 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6f60252-1a7a-3447-b3c3-7925c15adcb8 | -11.63369 | -52.20137 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| acec7b81-4909-361a-b1fd-bdfd74e24388 | -12.90004 | -56.94029 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 18f80f0b-3445-3c39-a754-a0dcf214e013 | -10.09671 | -54.75818 | 2025-09-04 04:55:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 455a4351-2b54-35bd-9417-3a673ff6e9bb | -10.46055 | -54.77217 | 2025-09-04 04:55:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 19552e56-b8bb-34e6-b2d1-112fbc4839f3 | -11.78668 | -47.32779 | 2025-09-04 04:55:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d34e8cf-9c3a-3b53-8ef7-1b24ac66a006 | -14.20207 | -48.07861 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd122424-a9fc-3251-a12d-7640bfadad88 | -11.86152 | -51.52054 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| faba75da-1e1e-3a9b-8e96-b24a9941ba2e | -11.59407 | -47.78494 | 2025-09-04 04:55:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1f53f6a2-b668-33df-b395-f4ddb90e38ab | -12.46243 | -48.07812 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39d8f972-b45c-3e94-bd4d-ec28be3b1684 | -12.89935 | -56.94445 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b7d597a6-a593-3dd4-88b4-2fea38308e3d | -11.57751 | -52.15913 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c313e7e8-fb48-32cb-ba01-813ed7489378 | -11.88068 | -51.53545 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5fef50e-12d9-3615-ac33-c3be2f3a7d59 | -11.58487 | -52.15653 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c99a52a-4f28-3840-aa44-55bf46c68fc8 | -13.45013 | -46.93788 | 2025-09-04 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07e3d5e8-3ee4-3f29-9715-ff7c8cde8069 | -12.81171 | -47.66597 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 28fc9020-f970-370a-8522-41e8096423c6 | -10.09097 | -54.77217 | 2025-09-04 04:55:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9957005-03a1-31a0-8de7-021fa24514bd | -15.04694 | -50.03876 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddaa27d5-e218-3a6c-a55b-a5de55848112 | -11.59949 | -47.77743 | 2025-09-04 04:55:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 574f29b1-152b-3b6d-abd2-9dd792f1b024 | -11.86792 | -51.54939 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bafa1161-766b-3b46-a414-9303bcff4940 | -11.84304 | -51.42178 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee05d2cb-57c9-3cb9-9fb0-33864ec8970f | -11.95786 | -45.77071 | 2025-09-04 04:55:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77652d6a-decf-31e0-bef7-75e0ec8e4317 | -15.30408 | -52.76913 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0eb012a3-537a-3673-b531-acd975a19bec | -14.57281 | -48.07768 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c374fd98-870f-3aa3-be12-0d7359e5af2e | -14.58233 | -53.02669 | 2025-09-04 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ed32d49-c528-35d8-b913-4dfaed90900e | -12.2406 | -50.15175 | 2025-09-04 04:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4d97fd43-eff5-3cde-84f3-1edbb9f0d012 | -17.05477 | -46.43847 | 2025-09-04 04:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dde48f83-c499-3621-ae23-dd0b3e0dd82b | -13.28245 | -46.81779 | 2025-09-04 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57428a79-3d6e-38c3-a8a3-fff64866ea57 | -15.7078 | -48.87723 | 2025-09-04 04:55:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ecfc2275-42bf-3e2a-9345-eeec1cc9dac6 | -12.49561 | -53.84499 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 456b3623-6c76-34e5-80b3-c9ea20acd676 | -8.7114 | -62.39979 | 2025-09-04 04:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3983c0eb-a14f-3b8c-8c92-bb7a4778e8e5 | -12.89578 | -56.94383 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a5a36863-27e1-368f-9c32-24bb8b42545d | -12.4571 | -48.08551 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 04431373-e684-3d4c-81ce-824b0aae42f7 | -15.24369 | -53.80578 | 2025-09-04 04:55:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 570aa4c7-aed1-3f30-882b-b86ec1b57d14 | -10.51237 | -50.42829 | 2025-09-04 04:55:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2696b6bc-f7bb-3f68-8546-772bb01167fa | -12.88879 | -48.02801 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b4b59a29-917e-3621-8267-2a16cb0e2d88 | -15.41185 | -55.93411 | 2025-09-04 04:55:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d0093568-4140-3741-97b7-bf8262316318 | -8.70602 | -62.39879 | 2025-09-04 04:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 16b34502-7629-3817-8e18-4655de5b185f | -15.02855 | -50.08532 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c3c254d0-d0e4-30fc-97e9-3b2b0a88f326 | -14.97489 | -50.18772 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c93f646-e475-33a3-827c-cd4ad2663188 | -12.48119 | -53.82812 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 261380f1-a854-33bb-abf1-0ad9ba622796 | -11.03365 | -51.54013 | 2025-09-04 04:55:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a12c0ba4-be61-39a5-9823-6dd9a248f578 | -15.30236 | -52.75724 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ca63bc4-a4ae-3273-8626-0b7517eecd97 | -14.21571 | -48.07636 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 635a1e85-dd53-3074-9091-382c13f9ea27 | -15.30525 | -52.73799 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ee76dcef-517b-399d-bfbd-0efbe0bcad55 | -11.85273 | -51.43512 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f4fdd503-ccad-3c00-ac8e-c971b5ec144b | -13.95841 | -53.98044 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18f4b33c-1019-3837-b8e8-46e64c121c92 | -13.57444 | -48.13321 | 2025-09-04 04:55:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8dbf1f66-17b9-3906-97e5-f50bbaabcebc | -17.04365 | -46.49093 | 2025-09-04 04:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0a31bef9-48e5-3edd-b6b5-b4f3c67b639b | -12.96248 | -48.06601 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 53a32761-9997-3734-abae-e6d663e748fe | -14.20954 | -48.08941 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36833e9b-0199-3429-8f98-e82e558b30a9 | -13.11094 | -56.80227 | 2025-09-04 04:55:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ebc38f90-91f0-3272-be51-3f654abe2dd9 | -12.60651 | -57.00268 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c23c0ad4-03db-3259-8416-17028d20f42e | -10.4639 | -53.62462 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c40f2ec5-f3eb-3d8d-bf85-3e17cf31e3e2 | -10.10009 | -54.75875 | 2025-09-04 04:55:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab842222-57f5-3f9a-8895-a62f8e3a8acb | -12.60363 | -56.99789 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6324b20e-58a3-3404-9631-a470db7eae58 | -10.8983 | -50.83459 | 2025-09-04 04:55:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c3a4735d-af37-3aa7-8bdc-84f1e658bc08 | -12.9786 | -54.78361 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7276f4b8-659c-3176-88bb-5d3b666befee | -12.51448 | -53.83355 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1a6fdead-cad5-315a-bda9-023dddeb0162 | -14.48162 | -53.4833 | 2025-09-04 04:55:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 89af62ea-b78d-3d0e-81a1-1c5b248517bf | -12.17813 | -53.88776 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2f51039-d568-354a-aeb0-f407e58d1751 | -12.50829 | -48.06034 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9ac3e7d-c34b-3982-b5dc-1fc2e570f6a0 | -10.47332 | -53.62974 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28cf3690-6d3c-3298-8380-d13b7d489712 | -14.05523 | -54.01077 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 643fdfd3-1b77-3343-9699-33afaad130b1 | -12.94465 | -48.06836 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b200741-8907-3ca3-986c-2a0b9f624de6 | -11.58544 | -52.15284 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a8633e2-b57d-3aef-a4e8-f52ad6c6b10a | -10.45171 | -53.61545 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a256d735-5eb1-307a-b15b-eaa2c1d4dc4e | -11.60188 | -52.13646 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6878b72d-0313-3f7d-a2a0-ed1550f0665a | -10.88607 | -55.74039 | 2025-09-04 04:55:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a30c3a8-fdc9-3c49-ae23-d099244c5efc | -12.47526 | -48.07954 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aa4bdbca-8a12-3b79-b899-e5bdbdd30c5d | -12.50403 | -48.05967 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d107434-ecf7-3a8e-a844-82d058714e1e | -11.67698 | -57.34322 | 2025-09-04 04:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 8e283e85-dc3b-3a10-95e2-2a5fcdeb46b8 | -12.18479 | -53.88885 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e0eec687-bb94-3457-94e3-517154783c2d | -15.86039 | -52.30068 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 128e2208-8b3d-3a0e-a4a8-fbc0638a386f | -13.95063 | -53.98649 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a7a8b06-fdb0-349b-a202-e4003e7a7f07 | -11.68186 | -52.20511 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35a3d0c8-4750-3ab5-97c3-2955787890e6 | -14.81866 | -48.20519 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8035e6c9-593f-3db8-a07e-1dcdd89ab3e5 | -14.068 | -53.99459 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cd92ad7f-9493-3451-9b0e-05ec12822184 | -11.64618 | -52.21085 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 625f7268-fad9-3327-a537-04ef5660b095 | -10.48052 | -53.6489 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 025a053c-6742-3afd-b06e-5495b1a737dd | -14.53902 | -48.06276 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| de7c155b-bb30-3cfd-b923-2633bd457938 | -15.46699 | -53.00639 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83bd205e-42fb-3d7a-82f8-741c68aa2247 | -14.88075 | -59.50283 | 2025-09-04 04:55:00 | NPP-375D | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| da92cca0-226b-3273-9997-2cd668f7cd52 | -14.48217 | -53.47968 | 2025-09-04 04:55:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2f9a31a2-9999-339e-bd8d-4934d6ee6267 | -12.9324 | -48.062 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f5a45dda-d23a-39a0-9cd0-fb5998936cb3 | -8.6959 | -62.39331 | 2025-09-04 04:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c65d9a1-ff08-3560-bab4-31d0f51e89aa | -12.75107 | -53.9879 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99ae3d97-29e9-3461-9e3c-3d2b9ee1ac8f | -12.18367 | -53.89591 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 10a9bdd4-099e-35c6-9f6e-673d350d39fd | -12.63524 | -57.00776 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2383bb9a-41f6-35ff-8d86-fd4684147bf5 | -14.77942 | -48.1286 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 42fc5456-6a39-3798-9480-514abc4a6706 | -11.78938 | -50.64216 | 2025-09-04 04:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5af570a-063d-311e-8593-a0311a909315 | -10.11229 | -54.79071 | 2025-09-04 04:55:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f295899-3294-3f78-af6e-aefceaa558bf | -13.95508 | -53.97989 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 687688f5-1e83-3044-83b0-90243544abe5 | -10.8529 | -55.74694 | 2025-09-04 04:55:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README67.md)
