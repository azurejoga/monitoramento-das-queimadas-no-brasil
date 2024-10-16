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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc846a79-790a-3b9f-8495-7841a8335894 | -11.20443 | -47.84851 | 2024-10-16 04:08:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39f1d954-aeb4-3d03-8bf7-9b0f4feef9cf | -11.20377 | -47.85226 | 2024-10-16 04:08:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12ad676e-30a6-3d19-9214-763b7448ab6f | -11.15837 | -48.73738 | 2024-10-16 04:08:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5abf890f-be1d-3bbd-8511-9b3abbce9a11 | -8.75179 | -49.77512 | 2024-10-16 04:08:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ccefc552-5372-3239-9b2b-8015f739057b | -8.75083 | -49.78054 | 2024-10-16 04:08:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4694f90c-0e25-372a-b6a4-d42bd02e4ee7 | -8.39889 | -48.93145 | 2024-10-16 04:08:00 | NPP-375D | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ad1c611-dd7c-3efc-86f5-91f85dbb993b | -8.39756 | -48.92799 | 2024-10-16 04:08:00 | NPP-375D | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3837e36d-c7d4-3cd0-9ac1-80d3661eb3ab | -8.39427 | -48.93059 | 2024-10-16 04:08:00 | NPP-375D | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4f85f5b3-9b04-387d-9c03-874919bad339 | -10.8318 | -49.24266 | 2024-10-16 04:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f2bee928-adb7-3481-9b8a-285dc3a4301e | -10.83161 | -49.24018 | 2024-10-16 04:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 422f9092-a0b9-3652-9914-1a37db7668d1 | -10.83096 | -49.24729 | 2024-10-16 04:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| c5444317-1870-3fe1-bbbb-0c784ac79d84 | -10.8308 | -49.24482 | 2024-10-16 04:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9f4bd129-36df-34f9-bd29-0a9a7c05c6f2 | -10.82999 | -49.24946 | 2024-10-16 04:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2164b0ff-2e8e-3b1a-80ed-b2bb810991cb | -10.82728 | -49.24179 | 2024-10-16 04:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bc8a670e-6669-3d3b-b9cb-3e94c9febaf0 | -10.82643 | -49.24645 | 2024-10-16 04:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 28aae8fd-7ae8-33c8-96ba-4cf8a512d0af | -10.82627 | -49.24397 | 2024-10-16 04:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 253eea9e-baa0-36c4-a125-54a770b721f9 | -10.82557 | -49.25114 | 2024-10-16 04:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 218228fd-b70e-3c33-bdfb-6fa37d9ba0d6 | -10.82545 | -49.24866 | 2024-10-16 04:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3f466b3f-9c08-3a98-a26a-c2162451a341 | -10.82462 | -49.25336 | 2024-10-16 04:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7188335c-9b96-3f1f-a709-b6d73c3fbc6d | -10.82189 | -49.24567 | 2024-10-16 04:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1ad5577d-5b7b-3b61-b65f-9cfb0c8c896a | -10.82173 | -49.24318 | 2024-10-16 04:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94737c57-b725-342a-a62e-47d940de2fa5 | -10.8209 | -49.24787 | 2024-10-16 04:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dddc6489-22f0-350f-8b6b-c982c91c1a7b | -10.07045 | -49.55726 | 2024-10-16 04:08:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77ef843d-4639-3c43-8aa1-b85757213339 | -20.99579 | -55.24229 | 2024-10-16 04:10:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9b3f1844-a821-3e52-b803-b3aa1133c944 | -20.99244 | -55.23891 | 2024-10-16 04:10:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dfee0889-77b3-3620-b350-c296d62252f9 | -20.99117 | -55.23706 | 2024-10-16 04:10:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0bfcf74d-ea61-36a6-b866-d3b8959cf2c7 | -20.99031 | -55.24088 | 2024-10-16 04:10:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7063580d-d666-3863-8a77-e3620891bb58 | -17.21299 | -56.68666 | 2024-10-16 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.7 |
| bc63521d-fdb0-3888-9e0a-86ce88267f79 | -17.21219 | -56.68649 | 2024-10-16 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.3 |
| 25d3d2f1-7588-3dc8-8a44-1759a6cfb318 | -17.21175 | -56.69228 | 2024-10-16 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.7 |
| c39fe83c-2bf1-34e2-9e17-f25d778df420 | -17.21091 | -56.6921 | 2024-10-16 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.7 |
| 86d9621a-b721-32c4-84a2-4e54861b871a | -17.20658 | -56.68507 | 2024-10-16 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| b93e3311-7ee7-3c2f-ac96-cce7d4e145af | -17.20577 | -56.68493 | 2024-10-16 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| e43aa8b9-7fb1-3326-af7e-7c7502de4f95 | -17.20409 | -56.69627 | 2024-10-16 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 86f9f166-8974-33dc-a73e-c96b6701721d | -17.20321 | -56.69612 | 2024-10-16 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| cf97d5c7-c24a-3a54-af20-11a2aa4705bb | -17.20017 | -56.68344 | 2024-10-16 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 22dca37c-a200-3e3c-9db7-e1431a22c51b | -18.27252 | -56.59142 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| bfb3ce4b-6de6-352d-82ce-f65f86264b93 | -18.27133 | -56.59669 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 2a946c48-3b1e-3c5a-96e2-6b8238eaa278 | -18.27015 | -56.60196 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 63153bbe-feb5-3dee-9aa0-a3eb8e48d547 | -18.26509 | -56.59508 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| d5bc6979-6929-34eb-8977-3a2caa859cde | -18.26389 | -56.60036 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| b4c20154-4e3b-3617-8598-6e7cf2877890 | -18.26359 | -56.57244 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 83d92feb-69e8-38df-bf31-1d4f6c24007b | -18.2627 | -56.60563 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 9dd05812-c6f4-3a60-9321-66d52b2d6cdf | -18.2624 | -56.57771 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 97f4e44a-38f4-346e-a956-d7a5f000e378 | -18.26122 | -56.58296 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| e88e0295-06f2-35b7-a11a-de184f807eb3 | -18.26003 | -56.58821 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| c2d8616e-7fda-3d6c-adeb-71a27d63d3c7 | -18.25883 | -56.59348 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 6081b451-a761-3603-a82e-3cae63c0d565 | -18.25764 | -56.59874 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 35cf8f30-2c12-35e2-8333-a3250920c22a | -18.25735 | -56.57087 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 9cb9dc00-f346-354d-b885-31dafeab1cc3 | -18.25616 | -56.57612 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| d04c4074-c468-3ab3-8a59-5bf66d847160 | -18.25497 | -56.58137 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 0127c790-c160-3015-9019-1099334f81b4 | -18.25383 | -56.42588 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 95a54df6-8e54-39bd-9508-551c11556d6d | -18.25186 | -56.42151 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4667a7a4-30ff-33c2-8efe-a55c5613de92 | -18.24941 | -56.38681 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 65aec6c2-6239-3a68-9d50-a753777fe170 | -18.24828 | -56.39192 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| ae3d726b-6855-3b0a-b93f-40fa4f756a5c | -18.24764 | -56.42429 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| c3ec3b16-39e9-349d-8680-d475e8755765 | -18.24649 | -56.38772 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 1de9ccc9-6b78-30af-b399-b8bc7bdde1d9 | -18.24536 | -56.4346 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 6347704e-10a7-3c49-bf21-f3467edbe2f1 | -18.24532 | -56.39282 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 79dfb476-4ef6-31df-8e28-f5b784486d3a | -18.24422 | -56.43975 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8c41bac7-baf4-35e3-97fe-e219d8ecd997 | -18.24214 | -56.43534 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 6e274c29-5d26-3c4f-bb1a-5f2fbecd02f6 | -18.24209 | -56.39035 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| f8eb886f-7ad0-3f89-9ff1-d7bcbc005ee5 | -18.23706 | -56.38364 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| f49572c2-2c86-37c2-919b-27ff9d3b921d | -18.23413 | -56.3846 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 9e53083a-73ff-3cf2-8061-afb83fdc8f07 | -18.23088 | -56.38206 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b6dae7aa-ad50-3213-98c9-3ae8bc859439 | -18.22795 | -56.38304 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| e4311b33-2020-3508-b9ba-0d09e6bf52d5 | -18.16735 | -56.84838 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| db604f83-09a0-3374-9445-9eee3b138f61 | -18.161 | -56.84673 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e9ae00bb-34af-3a86-a5ed-90d35859a065 | -19.59335 | -56.98903 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 03c06f4e-e7ad-3838-af09-34be7921304c | -19.59215 | -56.99427 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.3 |
| c223f308-e05c-3d04-aa7d-62c693926d12 | -19.59076 | -56.97161 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 65e120af-e681-38a0-ad4f-ef0f49b8d4a9 | -19.58955 | -56.97686 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| b9d8d117-f595-3bca-95d2-61164377c5a7 | -19.58947 | -56.53365 | 2024-10-16 04:10:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 83219e7d-5a3b-3467-bd25-aaadc4f6e8ea | -19.58834 | -56.98212 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 638a9e01-0a90-3d0a-95e2-0bdbc19abbc9 | -19.58713 | -56.98738 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| b313a9a2-2b34-334d-87ee-042f738fbd40 | -19.58592 | -56.99262 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.3 |
| 0be36296-989b-303a-be03-2d4f28b247f0 | -19.58574 | -56.96472 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| caefc795-313c-3a02-a33f-8bc25d2baf44 | -19.58471 | -56.99788 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.3 |
| c01f8893-e996-3f01-82b5-17b5b5df59b8 | -19.58453 | -56.96997 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| ff5d4f23-4318-3f79-be37-2d5aed85c65a | -19.5834 | -56.53207 | 2024-10-16 04:10:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 20e37f08-5f6a-396d-ba61-86c3e46900c3 | -19.58332 | -56.97522 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 16743056-f73c-3e63-ab84-d62668c98dc7 | -19.58211 | -56.98047 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.3 |
| dc1346e4-ce4e-35c6-9bc4-607761f6dc39 | -19.5809 | -56.98573 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 1a1fce71-3fdd-3ebc-ab95-b13e107fc19e | -19.57969 | -56.99099 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.9 |
| ddfe6b32-c323-3301-8021-760d7de11cf2 | -19.57952 | -56.96307 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 5d00a7c4-f40b-3a48-a37f-95ee673277a0 | -19.57831 | -56.96832 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| aacad7af-a90c-304f-88b0-40f64d9846da | -19.57346 | -56.98934 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.9 |
| 23563df3-d9f1-3165-a89f-6c8be6b4be9f | -19.57331 | -56.96141 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 82a09206-41a9-3484-ab70-efc16affb2a7 | -19.55965 | -56.96338 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 2ac50cd1-3237-370e-9200-f68748a58bd6 | -19.55342 | -56.96175 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 3cce573b-275b-35fb-b339-71d0fc30854d | -19.5472 | -56.96012 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ed3c643b-e2e2-3fb9-aef7-2b693d9d2212 | -19.54597 | -56.96537 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 94219eec-040a-3f8b-9008-100940612bf5 | -17.16496 | -56.84156 | 2024-10-16 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| c4ce3d9f-7db9-3170-a6e2-304cb63cbde3 | -17.16368 | -56.84727 | 2024-10-16 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| df280d2e-2435-329d-b767-ae628cc49dbd | -17.16315 | -56.84102 | 2024-10-16 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.6 |
| 5e809f80-05ff-3c9c-a851-4e241e2b0dca | -17.16184 | -56.84671 | 2024-10-16 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.6 |
| 178022aa-8d6b-3aac-a8e7-e7af541b23b7 | -17.18667 | -57.48098 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| ce3027a9-cfa9-3768-8646-4b6a1d8d20e3 | -17.18523 | -57.48723 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| f401dfd4-a5d3-3c4d-a537-27998171462f | -17.08205 | -57.46656 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 59ada7b6-a5fa-3dda-b9b1-99ae90717b66 | -17.08061 | -57.47285 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |


[Clique aqui para ver as próximas entradas](README38.md)
