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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2aa0008-cfa8-3e21-ba92-e262ac264de1 | -16.455299 | -53.960701 | 2024-10-07 01:20:50 | METOP-C | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eac206a3-fec4-3d74-b943-ee868183404e | -16.457001 | -53.967899 | 2024-10-07 01:20:50 | METOP-C | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f2aacf10-6929-3d38-b2bd-6f126ecfbe65 | -17.0816 | -56.7967 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a3923fe2-4299-3074-8ca4-603d1fa29a73 | -17.0833 | -56.804501 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6e2a57b2-8b1d-38cc-9604-47890b2faa1b | -17.0849 | -56.812199 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| be9d2a91-44b8-3310-a948-b0fa3593f47e | -17.086599 | -56.819901 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 73fadf0c-0cd7-322a-bdf1-87f8264ddf64 | -17.0882 | -56.827702 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9196683c-c55c-3ade-bf7c-ab5a91ff476d | -17.089899 | -56.8354 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| debefc7b-65c4-3285-bf64-947d4d0f1bd8 | -17.0718 | -56.798901 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e25b52f4-2a30-356e-a473-a177a9c8833b | -17.0735 | -56.806702 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b84cf049-1a21-3ec3-8d23-c9a6de71a4ab | -17.0751 | -56.8144 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c309628e-c20d-35b3-8253-ef7bd57bba19 | -17.076799 | -56.822102 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| aac921df-ef99-3418-8d3c-fd42b8bd605d | -17.0784 | -56.829899 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4a3c0e8f-3d19-37cf-9989-74a8c540b380 | -17.080099 | -56.837601 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ee55bae6-8678-35d0-bdac-e33152d687bd | -16.422501 | -53.907501 | 2024-10-07 01:20:51 | METOP-C | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b54f62e5-b616-31b3-9c90-17e07b7d3f43 | -17.062 | -56.801201 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 460d893a-72f9-3b48-ab0c-574dbd33cd63 | -17.0637 | -56.808899 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c5c90b53-c342-3663-a5c4-c165d3300bc2 | -17.0653 | -56.816601 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b3da9051-2ba7-3079-ae89-7adc121545aa | -17.066999 | -56.824299 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c2bc42db-3387-35a1-be6d-160815ef519c | -17.0686 | -56.8321 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6f36782c-7c66-369e-a5f8-e6179a9ad4d6 | -17.070299 | -56.839802 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5da1beb4-a4e3-3534-b979-26543e1dfd52 | -17.024401 | -56.672798 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 89f02032-e38e-3e54-9f3c-6140c06e3c16 | -17.025999 | -56.6805 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 99882f7b-501f-3941-bdb7-eafd011bae1d | -17.034201 | -56.7188 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a3175e3e-ffa1-36f2-850e-351dde244cb4 | -17.0506 | -56.7957 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1c36c8ec-c269-339f-b40d-b9c342791c0c | -17.052299 | -56.803398 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 505d42f1-b3a4-3a6f-bb83-3aae00890f5c | -17.0539 | -56.811199 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 43880b9f-a6c8-38c6-afc5-280b626fd5ee | -17.055599 | -56.818901 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 86d3f3d0-d687-3d2b-9705-34b3e552cf88 | -17.057199 | -56.826599 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| db2a2f4e-c136-3619-9fe4-2b1482cad127 | -17.0588 | -56.8344 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6b060dfb-750d-3e61-87a2-30d5e3241e62 | -17.165899 | -57.340401 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 265b9282-fb1e-3510-a357-fc05dff8322a | -17.167601 | -57.348499 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9c8ca028-ff8e-37c8-b80b-00e4195b79fd | -17.1693 | -57.356602 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4cb9d820-b1b8-3438-a8be-ca07e8681841 | -17.013 | -56.6674 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f3b15b0c-a81d-36bf-893c-dca1454a991a | -17.014601 | -56.674999 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b335ed6e-4953-3ef6-a671-94a9e79527dc | -17.016199 | -56.682701 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c0d96bda-aff5-341a-a031-0bccbd6c2965 | -17.0425 | -56.805599 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 35e93790-5964-3f7a-ba48-57ec2678a360 | -17.0441 | -56.8134 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 23d2292f-c71d-3b72-93f6-df332dbb45e1 | -17.045799 | -56.821098 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8816923e-10e6-3717-8083-4b4e32aa6d25 | -17.0474 | -56.8288 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bc5d58cd-4dae-3ad0-ac4e-52bc0f8dcd67 | -17.1544 | -57.334499 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| af741478-d6e2-38b5-9df7-3a36675593d1 | -17.156099 | -57.342602 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8c60e46c-06f8-3d7e-b5f2-8445c483ff77 | -17.157801 | -57.3507 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ec5da722-9c02-3e6d-a7d6-39e86fd475ab | -17.004801 | -56.6772 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f6cbd236-4a56-3736-a4a3-2e1bc21a1029 | -17.006399 | -56.684898 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4c5f4b1b-d767-308c-a464-4fa7d4f48aa0 | -17.008101 | -56.692501 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 55f56369-0f2c-3337-9b51-2043e45c8850 | -17.009701 | -56.700199 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 658a96fc-644d-3672-aee9-2da7b8a1de26 | -17.011299 | -56.707802 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 94d38998-d6e0-36c7-8cec-8216df7962af | -17.013 | -56.7155 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 42bfd56b-25ca-3ee2-a870-37a0d8d4629d | -17.0343 | -56.815601 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e1be5fd9-a4b9-3edc-8571-e4a302ead3ab | -17.035999 | -56.823299 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 28ceb4d4-bc4a-3e39-a306-cef79223f265 | -17.0376 | -56.831001 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 378ad5a7-d195-395d-b298-40ecb32e95ca | -17.146299 | -57.344799 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 67bad89e-2b98-36bf-ab45-85a144acfe85 | -17.148001 | -57.352901 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 72eeaeb6-a577-322f-b65b-16fd12a30a85 | -17.1583 | -57.4016 | 2024-10-07 01:20:51 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cee7abcf-7e2f-34dc-af9a-11b3ad21ed2f | -17.16 | -57.409698 | 2024-10-07 01:20:51 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6dd90865-18c1-3267-88ad-6f49b6f43723 | -16.996599 | -56.687099 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 47482057-0c08-3488-bed2-e88826cb1d6a | -16.998301 | -56.694801 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e3e75f51-bb74-305b-b874-ef57b6ddf3a8 | -16.999901 | -56.7024 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b55f06ed-ad33-3fc5-a96f-14280c4a3ae1 | -17.001499 | -56.710098 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c1e10b13-4dd0-36dc-9368-0d7017483a08 | -17.003201 | -56.7178 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 70d62aad-d52f-37f7-8f8b-cf5ca404a5c8 | -17.004801 | -56.725399 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2c3938e9-89e2-3c96-a170-ffbaa1eb53e4 | -17.026199 | -56.8255 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dc338d2d-be52-3f65-936c-db67942f841d | -17.0278 | -56.833199 | 2024-10-07 01:20:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7cd0f2b7-2c69-3e6a-92b8-edc36e01a3a4 | -17.1485 | -57.403801 | 2024-10-07 01:20:51 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 21484ce4-6319-3a9e-9741-be2b7342f484 | -17.1502 | -57.4119 | 2024-10-07 01:20:51 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c740b1f7-2509-397b-b41a-18e7562d07ef | -17.151899 | -57.419998 | 2024-10-07 01:20:51 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 208868ec-ec17-3639-b48e-77e73934d72f | -16.9673 | -56.5979 | 2024-10-07 01:20:52 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3ae7feff-33d5-362a-b20f-cd43ea0265c0 | -16.968901 | -56.605499 | 2024-10-07 01:20:52 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1947138e-ac7d-39a2-aa98-6db9682de135 | -16.970501 | -56.613098 | 2024-10-07 01:20:52 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 094cc76e-0cbf-3cfe-b74b-c6c6d300af14 | -16.986799 | -56.689301 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 60616c71-5349-3d10-a788-e8a206f2355c | -16.988501 | -56.696999 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| befa9cb7-de9c-36d3-9942-c60c72bd4292 | -16.990101 | -56.704601 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0e0a1d92-2c80-3f5c-a40f-17133c152255 | -16.991699 | -56.712299 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d4aa5bcd-3192-3231-a21b-0694ced105d5 | -16.993401 | -56.720001 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e5cf7925-0347-3833-b8f6-5b944f59be12 | -16.995001 | -56.7276 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b6dd7bf6-b8a4-34c7-8ed1-ce2488bed777 | -17.0147 | -56.82 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0d90ee92-1c1c-391a-a677-1e45394b41ae | -17.016399 | -56.827702 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1f2528db-8a14-3c13-a4e9-b346aa70d13c | -17.018 | -56.8354 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4c4c62e2-e3a7-3b6f-97b4-26ac5bc7057b | -17.1301 | -57.365299 | 2024-10-07 01:20:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2c72307f-56bf-384c-8269-3795fde661b7 | -17.1387 | -57.405899 | 2024-10-07 01:20:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e6f92dc2-2abd-381e-99b8-7265752f29d5 | -17.1404 | -57.414001 | 2024-10-07 01:20:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ab9cb732-96d1-3b9c-a4b6-35de8ed24453 | -17.142099 | -57.4221 | 2024-10-07 01:20:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 216fe4b8-71ce-3a3b-a1a9-239bbd4ff053 | -17.143801 | -57.430302 | 2024-10-07 01:20:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 32f1ab32-da55-38af-bbbf-79a6692bb5aa | -16.960699 | -56.615299 | 2024-10-07 01:20:52 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 829ccd1b-1057-3566-92fe-5edd2ca9b589 | -16.983601 | -56.722198 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f644abb4-9874-3068-be9b-dc7ab39bba5d | -16.985201 | -56.729801 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a25b42a4-8653-3fa5-8f0e-7295bcc99c84 | -16.9869 | -56.737499 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e526b16f-3b51-3d45-956b-6845a3faa8d4 | -17.0033 | -56.814499 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bddb9660-ec20-337c-9ff4-adf4faeff296 | -17.004999 | -56.822201 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0b9238bb-7cfd-3cb4-ac62-acce38cf36c3 | -17.006599 | -56.829899 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9bd99432-fbd8-3df4-89c8-e9f3037e2316 | -17.008301 | -56.837601 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ca428bf2-69c0-3577-a9a9-0a2343be6187 | -17.1187 | -57.359402 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 02eccdd2-dc32-3794-ba24-d68acb685acf | -17.120399 | -57.3675 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 11f6d88e-4f9d-3a47-be89-6f8db7b474b1 | -17.129 | -57.4081 | 2024-10-07 01:20:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 288d8496-e0ee-372f-a8a4-7017511a0b2d | -17.130699 | -57.416199 | 2024-10-07 01:20:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 47fb8901-07db-3b46-8598-69fdf59fc888 | -17.132401 | -57.424301 | 2024-10-07 01:20:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 22124044-5fc5-3cc7-96b8-16dca1a7bc55 | -16.978701 | -56.747398 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e4255b47-06dd-342a-9602-5741de6850c6 | -16.991899 | -56.808899 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6f5e6694-c211-3807-8f02-ebd9db53d49e | -16.9935 | -56.8167 | 2024-10-07 01:20:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README21.md)
