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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a32df5f-86b6-35f6-9141-1fcabc31bade | -9.82174 | -67.06702 | 2024-11-01 05:48:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ae8f590-5d7f-30bf-9918-89592fba2316 | -10.85719 | -68.22916 | 2024-11-01 05:50:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4726577-09c2-320f-beb2-ffcc474a9662 | -10.85386 | -68.22862 | 2024-11-01 05:50:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb845022-b084-3a3f-89b4-5c914cb9f910 | -10.79072 | -68.26543 | 2024-11-01 05:50:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b261b12c-9edc-3b7c-8d62-d9aa84310981 | -10.77322 | -68.77543 | 2024-11-01 05:50:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b06625dc-f847-3e37-a378-bae3999656b8 | -10.77264 | -68.77899 | 2024-11-01 05:50:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| eedbbc74-d3d3-34aa-aefc-b885d390c66f | -10.73268 | -68.80202 | 2024-11-01 05:50:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8214239-2e78-353f-8649-3040a9fd232e | -10.72928 | -68.65125 | 2024-11-01 05:50:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e0c8e2b-7627-3eca-be36-52bb69d63ebd | -10.71094 | -68.78741 | 2024-11-01 05:50:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d5d09a86-aa68-3910-9e04-d3a334952174 | -10.70767 | -68.76486 | 2024-11-01 05:50:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5180d95a-42e1-353e-babc-e06328ce69b8 | -10.69952 | -68.70854 | 2024-11-01 05:50:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b197319f-4bf1-3bb4-8dab-3fccd16ea4c9 | -10.69837 | -68.71568 | 2024-11-01 05:50:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 933ad872-2936-382e-88fa-71fa4a2c7b11 | -10.69617 | -68.70798 | 2024-11-01 05:50:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ec371f8c-2e31-30db-ad61-22c256a60359 | -10.67951 | -68.81171 | 2024-11-01 05:50:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 687826bb-672b-3328-871e-148e2f0c4d61 | -10.63579 | -69.01871 | 2024-11-01 05:50:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6bab3d94-2c1c-34c0-895d-46d9fa125920 | -10.51141 | -67.78463 | 2024-11-01 05:50:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e468af0e-4f74-3bb0-9e71-dd5dc0b3d0b8 | -10.41886 | -68.38976 | 2024-11-01 05:50:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27dce5ec-44fa-3d77-8678-866c2dd9615c | -10.4183 | -68.39329 | 2024-11-01 05:50:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 674b3de6-4608-3b6f-a944-f1f50b666190 | -10.13247 | -68.40485 | 2024-11-01 05:50:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1db86f5e-1930-3723-950c-274395577155 | -10.12913 | -68.40431 | 2024-11-01 05:50:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 50fd7a56-ed87-382a-b32d-c117d6679cd5 | -10.12222 | -67.59293 | 2024-11-01 05:50:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a669a8f-303c-31fa-8e83-674da9d573e5 | -10.12167 | -67.59642 | 2024-11-01 05:50:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75a08a88-6597-3305-a3d2-b1b46ec3ea1a | -10.1189 | -67.59239 | 2024-11-01 05:50:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d98c88a-258b-36d3-b226-904165d8bcf9 | -10.11835 | -67.59589 | 2024-11-01 05:50:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53edbd7f-ba21-3cb2-a331-7aa35baba99e | -9.98293 | -68.44991 | 2024-11-01 05:50:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef2ce6fb-9d25-3faf-a852-8e7abc895bc3 | -10.09914 | -68.37763 | 2024-11-01 05:50:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1f5a8e9e-05b7-345a-b903-022b5ccd5a0f | -10.09858 | -68.38117 | 2024-11-01 05:50:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac9e70c2-2cd1-33f7-b153-9b0ade946bf3 | -10.09806 | -68.36293 | 2024-11-01 05:50:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9fc710fa-bb96-3ff9-99fe-371a4714cd61 | -10.09801 | -68.38471 | 2024-11-01 05:50:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c48a7e1-21f8-346d-9bb5-f32ebdcd5e88 | -10.0975 | -68.36647 | 2024-11-01 05:50:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 2c2862d6-b602-3d43-b1ea-ad1302393792 | -10.09637 | -68.37355 | 2024-11-01 05:50:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0f8fd0c7-ba14-33c7-a459-5b08003ca52f | -10.0958 | -68.37708 | 2024-11-01 05:50:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 04dba1b3-b429-31aa-83df-e15be79f1aec | -10.09524 | -68.38063 | 2024-11-01 05:50:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ab79419-6aa7-308f-8ca6-493f61027ee8 | -10.09303 | -68.373 | 2024-11-01 05:50:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87e15e61-0c3c-3600-9fa6-10912e8edaa2 | -10.09247 | -68.37655 | 2024-11-01 05:50:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d84a8fc-f013-312e-bbbf-a4b0d9f12f73 | -10.0919 | -68.38008 | 2024-11-01 05:50:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5693e02c-c342-3a28-90bd-328c0327d06e | -10.08969 | -68.37247 | 2024-11-01 05:50:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a6af26e-9d87-3f31-b84d-bb4fd1b6e7b9 | -10.08913 | -68.37601 | 2024-11-01 05:50:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1a0ede4-abd0-348e-aa28-1256e41ee036 | -10.08544 | -68.29203 | 2024-11-01 05:50:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 252172d5-e235-3d14-a3bd-7c5ec08d28ee | -10.0782 | -68.29448 | 2024-11-01 05:50:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e07119f-433d-3f89-a7a4-b1b655a1b952 | -10.01865 | -68.41939 | 2024-11-01 05:50:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6bc22efc-6112-3ac1-892d-316b10e6c36a | -10.86103 | -68.73083 | 2024-11-01 05:50:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7640afd1-8eb2-32e8-bcbc-e7ae7e38b071 | -10.825 | -68.66677 | 2024-11-01 05:50:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 77f2e6f7-275d-376c-8306-31de3846abbf | -13.81486 | -60.26686 | 2024-11-01 05:50:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6eb99b0d-b001-328e-8282-01d9d02c9441 | -12.13391 | -63.60765 | 2024-11-01 05:50:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3cc71210-77df-30b5-a5c1-324c40080fda | -10.88913 | -69.52589 | 2024-11-01 05:50:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe60ea8f-bc6c-3633-9c9d-b144d7727703 | -10.83356 | -69.35 | 2024-11-01 05:50:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c06c1a9f-b3d8-34dc-b986-6600e2da5b78 | -10.62626 | -69.679 | 2024-11-01 05:50:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8300982-7203-3684-abab-365824ab9e00 | -10.57519 | -69.6943 | 2024-11-01 05:50:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b5cb4aa-3046-3ef3-a8ac-66610477a5fb | -10.45264 | -69.19785 | 2024-11-01 05:50:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa0f639a-c795-3236-b0a3-8163d9ceeca2 | -9.98627 | -68.45047 | 2024-11-01 05:50:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44aa9b31-d906-334e-bf0a-4cb164544417 | -19.4642 | -56.61316 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8e75111f-979e-3aea-ad9c-39e6a95a1fbf | -19.45961 | -56.61176 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a332cfb0-08e3-3728-a9b5-3be5a4e22189 | -19.4834 | -56.73138 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 39b6aea9-6820-3265-92d1-9affe9daa649 | -19.48289 | -56.73744 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 102677e9-489a-3d74-bde8-3d925a164fcf | -19.48238 | -56.74347 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| a79ad358-79fb-34ab-8e0d-b5ccb32b5cc8 | -19.47775 | -56.71857 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b8384613-a359-3dfe-a1b2-c56433640a54 | -19.47724 | -56.72464 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| a46a77b7-240f-3019-9082-1913784eedba | -19.59097 | -56.61819 | 2024-11-01 05:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2d3f1935-7dfb-374a-b2f4-030828034f87 | -19.59045 | -56.62437 | 2024-11-01 05:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 9aba8f5f-29a9-3c4a-9743-2bdbf9ee853b | -19.54571 | -56.713 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 89509e45-4043-36f6-b370-d2d495704bf0 | -19.54517 | -56.71909 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c11dca59-7c96-3777-adca-f4a9e8c35417 | -19.54463 | -56.72514 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0f719a4f-c259-3b15-8502-038bcfb12e3e | -19.54409 | -56.73121 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| fa1b1586-ce31-3076-bad4-bb86b4d345b8 | -19.54256 | -56.71246 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8fb20941-ec8c-3c01-9b2f-31367a77a647 | -19.54206 | -56.71855 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| afd079aa-cbd2-3daf-bfbc-c3d726559388 | -19.54156 | -56.72464 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b4cca017-d0d7-3797-a4a3-a789e557c79f | -19.54106 | -56.73072 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a04b5c9c-d6e2-3fe7-bd10-914737880e47 | -19.53848 | -56.71841 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 7358eef7-81bf-3d27-bd25-3c98a81d072f | -19.53794 | -56.72449 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f7b9bf4f-f75b-32ac-8df8-8309aeedaccd | -19.53741 | -56.73056 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 0f421934-8afa-3500-8e95-9d0603a3469c | -19.53537 | -56.71786 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 71e495be-c48c-34b9-9157-91154272aa08 | -19.53487 | -56.72396 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 81e11116-1e19-36b3-9b60-609f7698825c | -19.53437 | -56.73004 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 09938439-5f09-3ac7-a5ae-4c4e186cc642 | -19.53232 | -56.71168 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| e8a09bd7-d082-355f-b00d-5d5384778a40 | -19.53179 | -56.71776 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 611a5e79-f449-38fe-a421-d2ed90a14b4c | -19.53126 | -56.72382 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 916e17eb-9768-342c-a7d7-2515f43a324f | -19.53072 | -56.72989 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3f15418f-e8b9-3965-949b-42cfb36b9151 | -19.52917 | -56.71109 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 20d1634a-2e46-344d-9893-86b8e9591095 | -19.52867 | -56.71717 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 520d6df4-7eb0-3ba3-b928-7f0cbb61e67a | -19.52818 | -56.72326 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 22c1e7e2-6cf8-34ed-ae12-cd948e3017c4 | -19.5251 | -56.71711 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 9590d468-8053-3d3e-879f-c2339d55c455 | -19.51382 | -56.69144 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 0a0c640a-5dab-3fd5-b8f0-f9af45ad7808 | -19.51276 | -56.70365 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2e4b9d8f-ec7d-3559-b4de-67a2305ab00d | -19.51224 | -56.70972 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5a05de45-54b9-3833-a604-6bc24a28f90e | -19.51171 | -56.71581 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 64910360-1a94-3af7-8525-00ae5b811538 | -19.51119 | -56.7219 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 304c6611-4e4a-3bfc-bfd8-401d8fa2c644 | -19.50882 | -56.59169 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 2beb9b55-b6ff-31e6-b092-f38273a8dc50 | -19.50607 | -56.70301 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4b6bfcc6-5423-30e4-8b39-fd2e7c3498cc | -19.50555 | -56.70908 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 61f9b63a-cd22-3dea-b467-258f993e70be | -19.50502 | -56.71516 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| d5fea4cf-fb10-3788-bc97-f65036bf21b9 | -19.5045 | -56.72126 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 9915c30b-f5e2-33f1-85ce-5a467ad1e151 | -19.50398 | -56.7273 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 7959a29a-198e-359e-9956-b2e0bf94cb39 | -19.50365 | -56.57242 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d69909e6-4cf9-3612-b001-6cba3b41499c | -19.50313 | -56.57862 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| f8123266-8aa1-37f3-9546-7650129fbd70 | -19.50103 | -56.60343 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| c9de494f-7fac-359e-bde9-f0b287cd60e5 | -19.49946 | -56.62198 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 59771e21-a908-3376-a030-d6a13894e074 | -19.49885 | -56.70846 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 70d0b0f9-0a02-3010-90e0-32124a97199e | -19.49833 | -56.71454 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 731c33ba-b5c1-3fac-a5f2-c3ed250012ba | -19.49781 | -56.7206 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |


[Clique aqui para ver as próximas entradas](README54.md)
