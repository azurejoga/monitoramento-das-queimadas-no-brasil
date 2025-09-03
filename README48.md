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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 252fa9ce-6f4d-3295-9c4e-52996a0618c4 | -2.94428 | -54.80017 | 2025-09-03 04:44:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1957efe2-eaad-3652-bf16-e065629a09c7 | -2.34628 | -47.58661 | 2025-09-03 04:44:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9f963866-52ee-31e9-b61c-48a6124129a3 | -2.13572 | -48.00633 | 2025-09-03 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa887294-6145-350b-a01b-2ec8dac74213 | -3.79479 | -49.43089 | 2025-09-03 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4f1630a8-763b-3797-933d-a718df71d2e3 | -4.78945 | -43.65623 | 2025-09-03 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6a6a14f6-59b4-3fb8-84f3-b0fea8a376b1 | -3.22739 | -47.12931 | 2025-09-03 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 93ca6533-f5d7-3e1d-a6d9-558d2e9720b5 | -2.94064 | -49.45366 | 2025-09-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 21b24d83-d857-31d6-85a4-8d985898bd01 | -2.04717 | -48.28318 | 2025-09-03 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 359b4968-d648-3a7f-a2f9-6b4000a883a5 | -4.15883 | -46.79046 | 2025-09-03 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 75436f34-7d3e-3912-8b52-08ba89db28b1 | -4.90221 | -43.2079 | 2025-09-03 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| eea3be02-a7a4-3ee8-a4e2-ed3ec7849378 | -4.82908 | -41.80994 | 2025-09-03 04:44:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dec7f243-16cb-3148-990c-ce5910fafea8 | -3.37268 | -47.15781 | 2025-09-03 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 68fd31b8-9599-309a-a6fb-375a8a5627d2 | -3.05096 | -49.3774 | 2025-09-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6dfc4c14-2b14-3ff8-8d6b-9b2706376769 | -3.26185 | -46.92795 | 2025-09-03 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49c385c0-50f0-3440-a70e-06bb50f67d05 | -3.73151 | -49.68343 | 2025-09-03 04:44:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58acc97c-d3dd-3ffb-9264-ab2de6f18691 | -3.48561 | -48.44191 | 2025-09-03 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5a819181-3354-372c-bf0e-c5c0a84d90fb | -3.19754 | -40.74504 | 2025-09-03 04:44:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fd0c32df-af5e-3f4c-b335-ab9c84ae9772 | -3.81683 | -41.06305 | 2025-09-03 04:44:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| c4fca0a8-cd28-3d2d-9688-c6060e30c966 | -2.13858 | -48.01064 | 2025-09-03 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dde82e5d-bc8c-384e-9582-af168f2326bd | -4.56735 | -40.35184 | 2025-09-03 04:44:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 24713bf8-0724-3434-8b2d-3a13878f71dd | -2.88722 | -48.29457 | 2025-09-03 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11ad464a-3485-3bcb-84b0-454129efee90 | -2.65516 | -48.79689 | 2025-09-03 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c786ee3f-2aa9-3c2a-b89a-6b7743f9a22d | -3.68894 | -49.01316 | 2025-09-03 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 243672ad-7f15-3129-beab-c31cf864d6ad | -2.89896 | -51.4825 | 2025-09-03 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b42973e4-7396-3336-8dd4-ff573d669c70 | -4.83039 | -41.80743 | 2025-09-03 04:44:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d86cd607-7dc4-3cd9-ab7a-51961abee165 | -5.02688 | -42.48742 | 2025-09-03 04:44:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6acf61e6-fc6f-39f5-b2f5-10b95159529e | -3.98491 | -47.88449 | 2025-09-03 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c44590cc-9b95-3c0c-a955-170ff2790e45 | -2.13917 | -48.00687 | 2025-09-03 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5121da0-2825-31c3-8e44-9d827b8b0f81 | -4.47893 | -48.11366 | 2025-09-03 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45fbf1fb-2d81-3036-b347-53063105ad1a | -3.37632 | -47.15837 | 2025-09-03 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17ace0ca-a739-363e-a22f-fe8d40ac9761 | -2.34612 | -47.58381 | 2025-09-03 04:44:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 134f33e7-1275-3ab4-9f31-0152f0a8c292 | -3.21947 | -47.1324 | 2025-09-03 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c3dbbb2e-e38f-3978-8b49-4a5dd9e313cf | -1.08404 | -51.14489 | 2025-09-03 04:44:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4867724-f217-307c-9ea2-5bab3cae3150 | -2.20057 | -47.99245 | 2025-09-03 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e749817f-8b4a-351e-8ee1-7ce789df1b7e | -4.1595 | -46.78603 | 2025-09-03 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5c49fd4e-9921-3d71-b43d-17b552cd8c61 | -2.89951 | -51.47899 | 2025-09-03 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f459c410-a97a-3bc0-913f-e0e7e170f03b | -4.16258 | -46.79106 | 2025-09-03 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 1437f055-7ec2-356e-bd07-725e333f3cd8 | -4.15508 | -46.78986 | 2025-09-03 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a91c079e-9db1-3aa5-abde-4b6d2e841244 | -4.48536 | -48.11866 | 2025-09-03 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61cd50b3-c7b7-31b2-934b-9b2ad79222d4 | -3.22311 | -47.13297 | 2025-09-03 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 95920dc2-80af-3a12-951f-860570353d51 | -4.02498 | -49.76479 | 2025-09-03 04:44:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 31c4ca64-4613-305a-8444-22591c4d090d | -1.9624 | -48.69833 | 2025-09-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ee7ba85b-2aec-31c2-9d55-a31726934c5f | -3.81946 | -48.64356 | 2025-09-03 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f103ed37-f70b-3723-9188-9349614f98cd | 0.71369 | -51.37015 | 2025-09-03 04:44:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 300b50c3-09be-3ded-a5fc-4c101eacd49f | -2.94009 | -49.45715 | 2025-09-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2c2b0ed5-0440-3377-9698-bd65a3de0f87 | -4.56784 | -40.34836 | 2025-09-03 04:44:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e4e34dbe-0d3a-3a52-92d7-2676edc3f234 | -3.52796 | -52.9269 | 2025-09-03 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7810255-dee8-3e5f-9b8d-9b3ad076a4de | -4.66907 | -41.95506 | 2025-09-03 04:44:00 | NOAA-21 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ba657340-069a-3ce9-bb1a-f776c7dcd731 | -4.534 | -48.01279 | 2025-09-03 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77218944-6992-3b70-a552-bcf35f1c50ae | -3.20189 | -49.104 | 2025-09-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6507942e-bd28-3a8e-b124-61f4e7cce081 | -3.20134 | -49.10757 | 2025-09-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fed8c180-c3bf-3186-8670-25b1a69548e3 | -2.90155 | -48.29294 | 2025-09-03 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8954833-5f87-3ac0-8e36-8b95121bf1c8 | -3.21648 | -47.12761 | 2025-09-03 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 79f7e758-d61a-3138-94c4-4e6d450bf5e5 | -3.26251 | -46.9236 | 2025-09-03 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c57fcfc5-85f8-3d67-933e-d6e34ab8020f | -2.88779 | -48.29082 | 2025-09-03 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72a87b9d-77aa-34f5-bc0a-f8a30a75888c | -2.93236 | -49.46312 | 2025-09-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8720e8f-e1bd-3cb0-a115-0b5baacaaa1f | -3.79199 | -49.42685 | 2025-09-03 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53039ecc-650c-3d41-a433-770c3bf08a8c | -2.90499 | -48.29346 | 2025-09-03 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d395a71-1651-3052-8326-4f19ac8d041f | -2.28758 | -47.88891 | 2025-09-03 04:44:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d5aba85-6893-39b4-b941-8de0c43f098b | -3.98101 | -46.99796 | 2025-09-03 04:44:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5999f421-a907-3d77-9394-1a2656998d51 | -3.79534 | -49.42736 | 2025-09-03 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| de61ab0b-e517-3554-b93c-6cbca7010797 | -3.60015 | -49.45515 | 2025-09-03 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bcf8061c-f7ca-3ede-b7bc-0a603b1700a4 | -4.31381 | -47.44353 | 2025-09-03 04:44:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6dcfc26-d47b-31ae-a57c-66fb0a92c79b | -2.28195 | -56.13053 | 2025-09-03 04:44:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7fda84a2-4321-31a4-a7c5-f091cb4d612b | -2.60811 | -51.94795 | 2025-09-03 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ad473ec-7469-37bb-925b-c11223367f9e | -3.23168 | -47.12564 | 2025-09-03 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7f19d212-caa9-39ca-b8a3-d4eec4658b60 | -4.19239 | -46.84676 | 2025-09-03 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23a22fb3-96ab-3fd8-b2b4-d51f069163cd | -4.7934 | -43.66186 | 2025-09-03 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f3128864-c1e7-33f0-9b96-d15e75ebfab5 | -3.23103 | -47.12987 | 2025-09-03 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 40b41f59-aa41-336d-afad-6c1e5e4343e4 | -4.47833 | -48.11758 | 2025-09-03 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 99ca32e2-3be2-3894-be1e-81d03dc48aaa | -3.31424 | -48.7113 | 2025-09-03 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c78d29d-fecd-3e8a-881a-25ff92091b36 | -4.31075 | -48.09757 | 2025-09-03 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77a632a7-9813-3e78-a9e3-4c2ff1908c02 | -2.93623 | -49.46014 | 2025-09-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2b16d96-255c-345e-a282-77be325d0945 | -3.79144 | -49.43038 | 2025-09-03 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c0cb8a1-abaa-315b-a69b-b9560c5a4d94 | -4.02444 | -49.76829 | 2025-09-03 04:44:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a4b72076-4afc-3678-9043-a9ec4bcf717f | -2.39092 | -48.53055 | 2025-09-03 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47b934be-c7fa-3651-bfae-6022f5807653 | -3.97373 | -49.96346 | 2025-09-03 04:44:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad01c541-da77-3ed0-b2b0-e28d49942215 | -4.08611 | -48.80126 | 2025-09-03 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88e05024-f00a-36a3-aee3-872ead383a5e | -4.66339 | -41.95743 | 2025-09-03 04:44:00 | NOAA-21 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 5219d7bd-6e0d-3530-8fa5-518a1231e2dd | -2.93568 | -49.46363 | 2025-09-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad857cef-f707-3970-8863-bbc566dfd566 | -3.21713 | -47.12334 | 2025-09-03 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ba534fcf-c5ad-3dd6-b7ac-713015ece12a | -3.4973 | -49.04634 | 2025-09-03 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13c64720-6846-36f9-bea5-44ecbf34ea57 | -3.20025 | -49.11471 | 2025-09-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dbf44e3f-1440-306f-b27e-98aeb64d3c17 | -4.89334 | -43.20122 | 2025-09-03 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10653878-1274-3832-ae4c-111a34ebbfcf | -4.89411 | -43.19587 | 2025-09-03 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 982789cd-da48-31a5-9eef-172c064fc3c3 | -3.22012 | -47.12817 | 2025-09-03 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 29034c30-d214-377f-93ff-941ae5c29586 | -4.1903 | -46.84458 | 2025-09-03 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6447051b-f26b-32c9-bcd8-d78bade33ca9 | -3.23039 | -47.13409 | 2025-09-03 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 4ccc9864-6fbd-3a11-b6b0-40ec995bb506 | -3.16811 | -49.47834 | 2025-09-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb0d59b4-2daa-3856-9e48-bfa5d44d60f0 | -3.22375 | -47.12874 | 2025-09-03 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| fb3618cf-863e-33e0-a615-3d96ee68b932 | -4.79664 | -43.67246 | 2025-09-03 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0dee6752-e1f8-3aec-aad2-29d14bacc403 | -4.6743 | -41.95585 | 2025-09-03 04:44:00 | NOAA-21 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6931982c-5d64-3a18-b4f6-2e2ffc5550a4 | -3.3589 | -43.37525 | 2025-09-03 04:44:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5486cfa-412a-3f04-b6f4-e05ffbc173c7 | -3.75644 | -49.05642 | 2025-09-03 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 47d44d37-0af2-35f7-a9ed-f260c72cb193 | -4.15133 | -46.78925 | 2025-09-03 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c947636c-33a2-3895-a70f-102bbcf47afe | -2.93677 | -49.45664 | 2025-09-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c841020-34f6-3be8-953b-406c642bd74f | -4.89512 | -43.22292 | 2025-09-03 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f2c214c2-9c4e-3468-8103-c164f5befd97 | -2.90441 | -48.29721 | 2025-09-03 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9bd9738e-cffa-37ce-afd4-c30450cf0392 | -3.92556 | -50.1861 | 2025-09-03 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ab86d178-ff7a-3424-85cd-859044eb0d16 | -3.64607 | -48.44666 | 2025-09-03 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README49.md)
