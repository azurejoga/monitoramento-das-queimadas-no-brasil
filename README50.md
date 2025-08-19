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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d463393-c910-3f94-b75c-fe50f9082c2d | -13.14276 | -57.16285 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63fca9a5-0d18-3d88-834e-2f489f8bbd28 | -11.0877 | -58.94298 | 2025-08-19 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d151f7da-c731-3c66-9531-bb915e766a37 | -13.31641 | -50.79208 | 2025-08-19 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 78cd441a-bf05-383e-8c5e-8a88b08d7a16 | -13.34935 | -54.41303 | 2025-08-19 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 81a9e6d6-bbe0-3c8a-8cd4-39f419b37db2 | -12.97714 | -56.85553 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6a293f0e-eccc-37c4-8fd8-fb710b806475 | -11.73577 | -62.1886 | 2025-08-19 05:18:00 | NOAA-20 | NOVO HORIZONTE DO OESTE | RONDÔNIA | Brasil | 1100502 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0240c3f1-442a-339f-a5df-f74c6c45036b | -14.97596 | -54.80864 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 61f6ea58-313e-37ac-805b-01966d800341 | -13.18406 | -54.94459 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af64a120-7616-368c-a5ba-9462f9601514 | -13.47985 | -47.07082 | 2025-08-19 05:18:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2795f1b-3195-3b6f-988a-4bf17ecd9eb7 | -15.38302 | -53.9089 | 2025-08-19 05:18:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98e64ede-9cfe-3d1f-9b1f-ae057df2414d | -13.13735 | -57.14878 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab3dc18e-c3e0-3760-b0ce-10af0bc6d1da | -14.96898 | -54.79493 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5334e44e-f7be-3c2d-8b2a-a10f35dac253 | -14.98165 | -54.81195 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 354218fe-f9fb-3767-bca3-a63c16689d7d | -14.99082 | -54.80904 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4a814af3-c4f8-35a9-9608-93eaa7fd90ee | -11.85466 | -51.57815 | 2025-08-19 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91fdddce-8d7b-34fe-88a6-d73987672167 | -9.64015 | -64.37088 | 2025-08-19 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b7a8b47-f6d6-3859-bd1f-a286f461bebb | -14.86665 | -48.0621 | 2025-08-19 05:18:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4cce692-9eb2-3f2b-8d24-1f919c9bb876 | -12.98052 | -56.84434 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f0712ce4-0af9-3e98-9a0e-c372fdefae58 | -10.11272 | -57.7605 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4397896-b907-3075-8ab9-ca06001ed862 | -13.01307 | -56.84234 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c9c95cfc-2417-3d82-a5d6-a7cafdc04dad | -9.94026 | -60.50128 | 2025-08-19 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a830bc92-9308-300f-81e2-c3adaead2e7b | -15.15341 | -48.77656 | 2025-08-19 05:18:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 67c952ea-9652-32d4-a197-5c1c6ae94dfa | -9.51104 | -60.52942 | 2025-08-19 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f7add51-866a-3bbb-b1e5-6ba2a750cf15 | -11.8602 | -51.57571 | 2025-08-19 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 332e6b0f-caca-3bbd-b38e-17777ffb225e | -14.84667 | -48.05906 | 2025-08-19 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 916e85d3-5639-3337-9c45-caa6d7a2ca03 | -11.86536 | -51.57636 | 2025-08-19 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e58d5fe-617a-39fc-a922-0b5595f4b1d2 | -11.74464 | -58.32824 | 2025-08-19 05:18:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10bbfef8-185b-3b2c-8d01-553205b8b38e | -15.79435 | -48.23039 | 2025-08-19 05:18:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2ec5de9-092d-3fca-9441-c305552f782e | -12.98826 | -56.85715 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08caa94f-2d3c-338b-99bb-3092cb86bf0c | -15.03287 | -57.18811 | 2025-08-19 05:18:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 63c4b3d6-8199-3cbe-9fb5-80ea3608a298 | -14.62496 | -54.92133 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 90b67b3c-257d-3691-95c7-314e0d93038e | -14.9865 | -54.80841 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 09996570-327c-3216-a7eb-9130d508303b | -12.99758 | -56.84474 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4791952f-f5c9-3785-a849-5e2a601bc743 | -11.85825 | -51.57412 | 2025-08-19 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 27db473b-d965-3cf3-b246-42d4bedd7092 | -13.00257 | -56.83624 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2212e2bd-975d-3b09-8042-c738157aea98 | -11.86261 | -51.58084 | 2025-08-19 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60fc1829-a6be-362e-b0fb-6243924e7b57 | -11.85543 | -51.57193 | 2025-08-19 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3662437e-e732-316d-af74-c41e5d31d46a | -13.34991 | -54.40878 | 2025-08-19 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9ff57b6f-f678-3c50-a728-f7bf2e89b711 | -13.16575 | -54.92232 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26e919e9-4ef7-3516-af50-4e891b42463a | -9.51273 | -60.51884 | 2025-08-19 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2d73fba-74b3-3275-a461-272f87da9464 | -14.86792 | -48.0497 | 2025-08-19 05:18:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0d53946f-e199-3526-985f-96cfe6f6258c | -13.159 | -54.941 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a0f15a20-f08e-32bb-a4d2-a96a8273c80c | -15.74358 | -56.0251 | 2025-08-19 05:18:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| cbab146d-7a5a-3a6d-a614-b3ee297c26b8 | -13.37593 | -54.41264 | 2025-08-19 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1be5946-8ab3-3fe3-b6ae-a564ba8b605f | -14.87332 | -48.06301 | 2025-08-19 05:18:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9937896-31b2-3c1b-aa01-db668e808c7e | -12.98211 | -56.84708 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 521a63c4-677a-3e98-99a0-eae41ce40ea5 | -13.14339 | -57.15852 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd695c88-3456-3824-b8a5-8628ef51232a | -13.13608 | -57.15744 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd8c75e5-fa2a-3543-9d50-73c23632ac59 | -8.36757 | -70.1425 | 2025-08-19 05:18:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0cfca8b2-a0e2-3d28-aa22-9207239d7263 | -14.9722 | -54.80385 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 21522e96-7f2e-36f4-8a80-729cf493ae10 | -15.08332 | -55.42134 | 2025-08-19 05:18:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8ad9c55f-b6e0-3d15-af72-361db82b75cd | -14.98461 | -54.80984 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b7469660-36bc-335f-ae2b-ec91af5c2676 | -15.01771 | -54.80538 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 86c357b7-a7ff-3ce6-a35d-0dfa120686ef | -11.85505 | -51.57505 | 2025-08-19 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2dac6888-fbbb-37b6-9bce-4cedf11cf5f3 | -9.53545 | -63.57759 | 2025-08-19 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca9f01bb-e39f-376c-b794-a50ac2c44608 | -11.31357 | -55.22017 | 2025-08-19 05:18:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c51ff0b-ee7f-37c6-868a-0768c75d11a2 | -9.51713 | -60.53403 | 2025-08-19 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d5282e6-532c-395b-8c4d-772a78023f07 | -13.44074 | -56.90226 | 2025-08-19 05:18:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c17aa61-3eab-3398-8b5f-5b66ddad2a8d | -14.97917 | -54.81757 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ccde2825-29c9-3472-847c-ef4d7bfcc550 | -12.98084 | -56.85608 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| be6ff318-6b32-3047-a516-29670689e2b7 | -12.97903 | -56.84199 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a94359f8-0121-36c2-87f4-ab2f8f357578 | -13.00374 | -56.85477 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed5a5827-8a7e-3fc5-81ad-5771dc6e761c | -13.48053 | -47.06427 | 2025-08-19 05:18:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0a1a1fd-743e-38c8-9622-46dae2afc45f | -13.17936 | -54.94785 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e7b3b82-5b9a-3c8b-af84-4daa7758fd50 | -10.16933 | -69.01691 | 2025-08-19 05:18:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7939db8b-b89f-3f10-8cea-f80d38670093 | -15.03332 | -54.82083 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 19a6e23b-2845-38b5-86c1-28209e3e5007 | -15.03435 | -54.81289 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7da60e24-7389-31d2-84eb-bb285df07ad9 | -12.9747 | -56.84592 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d09f80bd-7b22-3fc2-a268-4a055fa84936 | -9.51606 | -60.51937 | 2025-08-19 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc2275e0-94cb-3db3-9209-a699c894e6e1 | -12.98581 | -56.84764 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52b8ecc1-4266-333a-b133-cf39d732a904 | -13.59206 | -46.99675 | 2025-08-19 05:18:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed4cfa9b-f4ab-39fb-8bf3-cb01312ee305 | -12.97099 | -56.84534 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1c83ea51-b5dd-39b0-a18f-bb188ac0c41a | -9.52378 | -60.53511 | 2025-08-19 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 36850341-ed8c-3d8a-aab2-57e0a5c4d091 | -14.97667 | -54.78158 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02a80793-d5b8-334c-bde5-c3829675627b | -9.64491 | -64.3666 | 2025-08-19 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c1c64a9-b5f3-39a8-9f95-6aad5da1ac68 | -13.01807 | -56.83384 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1d457957-2cc4-3a31-8bf0-6ddd0ef05f02 | -14.98702 | -54.8043 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| fada8e9d-8262-3cb0-a319-899bd8b40a0e | -14.62441 | -54.9254 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 189235e4-ded0-32d0-90f8-66e29d24252d | -15.03866 | -54.81362 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 11d499bf-ca59-3347-8e8b-c0d0a232801f | -10.43546 | -60.29355 | 2025-08-19 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31149f39-ece3-3433-ac6a-4b34b776cd85 | -13.16683 | -54.94605 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 070160d8-503d-3780-91ec-026c6965553f | -12.99016 | -56.84367 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc3a42ae-76e9-3824-8d66-dafc5e7a56cb | -13.14469 | -57.14801 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f38b1980-7e8a-3081-b111-73e8fbff37b4 | -13.30952 | -50.80254 | 2025-08-19 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f7063f1-1425-3b3b-a14c-9117709bdb18 | -9.53917 | -63.57823 | 2025-08-19 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8cff4cb7-aa22-3348-bae7-1faff7b18358 | -12.97919 | -56.85336 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 98ce0356-465b-35b0-b3be-325619c9bd87 | -16.6235 | -51.35894 | 2025-08-19 05:18:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ea134b2d-396b-3a3a-8937-c5dc217ba64b | -9.51989 | -60.5381 | 2025-08-19 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 247e854b-547e-353d-a96c-980bc82178a8 | -15.03057 | -54.80812 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5b8cea2-ccca-318c-890c-5687518952d8 | -13.14347 | -57.15672 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da7d8745-6b45-38f5-92c8-db40245c88e5 | -14.97165 | -54.80802 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2f2fd502-790e-3efd-87f0-045d4e1d7266 | -13.14774 | -57.15289 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 447713d5-8bab-38d2-8af2-f9c52b084cc3 | -9.8923 | -64.26208 | 2025-08-19 05:18:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f4ca885-997a-3603-a0f1-76c542146e3e | -14.61969 | -54.89559 | 2025-08-19 05:18:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26dced50-7f44-369d-a9a5-67aebc0a13e5 | -13.29712 | -50.81225 | 2025-08-19 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 181ed857-2f59-311c-8ea1-d28dcf142b51 | -14.97733 | -54.81136 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d1b529a0-ab33-319c-be22-61f33dabc0ed | -10.1087 | -57.76378 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec51f169-68e8-3954-84dc-f7a9f5a2344e | -14.97927 | -54.78384 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f0f111e2-8420-3fff-a8e3-96986e2015b1 | -13.00565 | -56.84128 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 06568e2a-2375-3b97-81cf-5572e4431f35 | -12.98147 | -56.8516 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README51.md)
