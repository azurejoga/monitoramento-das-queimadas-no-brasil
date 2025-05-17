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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4feec2a7-55d9-3711-9c30-bf955d192b84 | -18.38622 | -44.19283 | 2025-05-17 04:17:00 | NPP-375D | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 02d7cbab-900f-3258-8785-8cd3c86408b0 | -7.23404 | -44.7123 | 2025-05-17 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ead1ca5-2efa-3e6a-86fa-859abc128e24 | -6.61927 | -48.01044 | 2025-05-17 04:17:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 809a9f96-9c30-30f9-a022-c31fe334c40d | -17.921 | -45.53182 | 2025-05-17 04:17:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 96417983-fbd6-380d-9c98-135d177ee414 | -12.83755 | -47.40457 | 2025-05-17 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2839163d-8cda-3af5-8cd2-75db51803046 | -11.5785 | -47.61039 | 2025-05-17 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9c1d328b-db14-3f32-85ef-8cb070329bc7 | -12.10547 | -44.74283 | 2025-05-17 04:17:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ae19317-22e3-35ec-ae55-4021d75212ff | -18.38965 | -44.19338 | 2025-05-17 04:17:00 | NPP-375D | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0dff0de-31cb-3a8c-a176-d938339e8806 | -9.66607 | -47.5576 | 2025-05-17 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0c7e134-75be-3210-b4bc-3b54f4f7c7b4 | -18.39022 | -44.18954 | 2025-05-17 04:17:00 | NPP-375D | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cec48b4a-0fe5-39d6-8b7b-3d653a36d2b0 | -13.04858 | -53.72054 | 2025-05-17 04:17:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4166f571-ab9e-3857-bb8d-c44fd8741d2a | -13.39329 | -48.46414 | 2025-05-17 04:17:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1015b76a-1ece-30a3-bd62-58e4e3101cf7 | -11.15791 | -48.67428 | 2025-05-17 04:17:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4cced0a8-84cd-38ea-b25f-b9a97c2351e6 | -13.30504 | -45.37928 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fffca861-a949-3255-a946-f414737483ef | -9.32995 | -44.83812 | 2025-05-17 04:17:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8ce2d95-0cdd-3931-8388-494fad115f5f | -11.42624 | -54.32039 | 2025-05-17 04:17:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3ac665d-3db3-32cd-876d-1220874342d2 | -11.43743 | -44.72583 | 2025-05-17 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a1f39bf-d29b-34e3-9a89-37f6524be3ce | -12.30583 | -52.46864 | 2025-05-17 04:17:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c3fa6cf4-e861-3ed7-88a3-3268773c00e6 | -6.71667 | -47.59219 | 2025-05-17 04:17:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb3aab8e-12cf-3262-a0c4-8b0785b47994 | -13.39598 | -48.45393 | 2025-05-17 04:17:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 16ab1760-996f-397f-b9b3-76afd2c45309 | -11.43133 | -54.29383 | 2025-05-17 04:17:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb907284-6812-30ea-90da-77c3780741a6 | -19.87899 | -44.75842 | 2025-05-17 04:17:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| af53a6b2-c4e0-36f0-aa74-1b701e36c32c | -13.5025 | -47.40153 | 2025-05-17 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d5bca73-10bb-3135-9348-7365d8119d86 | -9.3171 | -44.83236 | 2025-05-17 04:17:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d9854f1-98be-3994-bff6-4e35ca435635 | -11.33963 | -46.50097 | 2025-05-17 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86fbb4c9-b75b-3816-aa0b-f6a1147264f6 | -11.78784 | -47.34561 | 2025-05-17 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9fe9ca34-0cff-3512-98b3-2ed6c3112dcb | -13.06418 | -52.02147 | 2025-05-17 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a16a6e4-d638-3f31-bddb-9ece07e4a5d6 | -8.16323 | -46.49852 | 2025-05-17 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6fc4d308-cab0-3694-bb5b-4b77d09042ea | -11.79309 | -47.40216 | 2025-05-17 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3496352-32f9-3a3a-91fa-7236a9bcae01 | -10.66018 | -44.49081 | 2025-05-17 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 879e5e2b-9998-3398-8a14-f0f67e1d215f | -18.9359 | -40.26232 | 2025-05-17 04:17:00 | NPP-375D | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 1e60be71-1626-3c74-8bad-c2bfc7657a8d | -18.3868 | -44.189 | 2025-05-17 04:17:00 | NPP-375D | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b04320ac-c8df-3db3-9115-d2a69e512186 | -7.95329 | -49.76246 | 2025-05-17 04:17:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08c4cd9f-a37e-3a3a-be88-66efc72f0c94 | -11.35897 | -52.95003 | 2025-05-17 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ce4f482-5332-3a80-ae46-c13661d50d18 | -11.5807 | -47.61964 | 2025-05-17 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 66f08292-bbb2-357f-a496-cfa38d878186 | -13.31281 | -47.46426 | 2025-05-17 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b0566fef-34a6-3650-bfc2-ddf55139c75e | -13.31172 | -45.38039 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d68fce5-d2c1-3167-897f-633c036270e8 | -13.31563 | -45.37737 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6f55fed-34ad-3978-8727-eca07e436cdd | -11.69428 | -44.62243 | 2025-05-17 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86f3ebda-ac16-3f1d-9b1d-796b585ef67d | -10.49889 | -46.18314 | 2025-05-17 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72f1b4ae-ab26-3d9a-a136-2681383ce275 | -11.79212 | -47.34209 | 2025-05-17 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f01b2b55-c78b-3c02-ad06-a6f4bb72a961 | -19.06873 | -53.45797 | 2025-05-17 04:17:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 95476547-0fdf-3088-9541-b83a86f790ed | -17.74838 | -42.89535 | 2025-05-17 04:17:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ab77ce3-0791-3216-ab28-b39ae578c734 | -18.95432 | -52.24678 | 2025-05-17 04:17:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 119f53bc-f90b-3b0e-9f73-26df00571ffe | -11.79142 | -47.34624 | 2025-05-17 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 72fe9ee4-f5cb-3061-983a-94791eccdded | -13.32174 | -45.38207 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1aef5219-b8b8-3f9a-810a-1ab6cbac2366 | -13.47315 | -47.44602 | 2025-05-17 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 015ba016-b78e-3439-ab51-c6a7ae63f3fb | -18.14711 | -47.80233 | 2025-05-17 04:17:00 | NPP-375D | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58663e9c-2bc6-3c6f-b421-58f1739b01b8 | -11.36977 | -52.94895 | 2025-05-17 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2c22278-2fd4-390b-8d81-b7228be9c543 | -11.42696 | -54.31664 | 2025-05-17 04:17:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d6fbedb-b076-3eef-a32c-7bd6c8cc1118 | -8.75135 | -49.75528 | 2025-05-17 04:17:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 95c97b7b-c109-328e-ba20-1f2434611cf3 | -7.23065 | -44.71175 | 2025-05-17 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0a9b087-60ac-31e2-82b3-f751585c0608 | -11.40152 | -52.94901 | 2025-05-17 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9a40aa8-7d82-39a6-814e-a4a67cc3ad8b | -17.78228 | -42.81041 | 2025-05-17 04:17:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4db2f05-0ccb-35af-919b-587d330e7004 | -13.30677 | -45.36855 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36351019-3aa0-358d-a2ce-badf903e6fe3 | -20.3765 | -48.08145 | 2025-05-17 04:17:00 | NPP-375D | IPUÃ | SÃO PAULO | Brasil | 3521309 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc3a07f0-ca84-3012-8e81-2981290d7920 | -14.06614 | -45.41523 | 2025-05-17 04:17:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a65ff95a-f921-3893-ad1c-58f2f1ca5e64 | -10.63495 | -48.09024 | 2025-05-17 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| eaa8b1f9-6efe-3a77-ba47-05c5331fc4b2 | -13.31887 | -45.39995 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b65c0319-1eef-3b65-b69d-9bfacada2cfb | -13.31897 | -45.37794 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a7c5a99-49dc-348b-880d-bc2e646a52b6 | -12.35285 | -49.96797 | 2025-05-17 04:17:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca72c1eb-dec9-3e97-bfab-6c18405b0527 | -12.83824 | -47.40051 | 2025-05-17 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f9488459-10b9-3152-902b-90dfa2950b4b | -13.31725 | -45.38866 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| de0f8198-4909-3286-a2a1-032e046e29ad | -11.31915 | -46.48633 | 2025-05-17 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6221c5e9-d520-3c18-8214-29c002925272 | -11.33872 | -46.49753 | 2025-05-17 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1b490dd-2497-3dae-b6c8-cc1e600bd481 | -11.79499 | -44.28784 | 2025-05-17 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0c88b75-8086-3507-b012-56ef6b9a6956 | -11.10693 | -44.63193 | 2025-05-17 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a504f9c6-9d82-33a2-9abd-c9203c259288 | -13.06976 | -52.01736 | 2025-05-17 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9b41446-140a-3449-abbb-819c629213e7 | -11.16483 | -48.68059 | 2025-05-17 04:17:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 231b79e3-6462-35ed-92a4-f0045525360f | -17.7256 | -54.08964 | 2025-05-17 04:17:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec828d1f-8b3f-33e5-9e8f-32c245cecd2e | -11.96309 | -48.25072 | 2025-05-17 04:17:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f412ca0-3f21-352b-8a19-6b728577ce63 | -12.35632 | -49.97249 | 2025-05-17 04:17:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1eddd8a3-1aa9-3665-8ef2-999ca0425c45 | -13.06571 | -52.02312 | 2025-05-17 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b347428-8338-3a64-b989-873f63669ef0 | -12.99251 | -46.31543 | 2025-05-17 04:17:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 130f2b0a-d387-36ca-94d8-5c6c87c66a41 | -13.3123 | -45.37681 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5b29c1a-9d3e-3c4f-a403-d112470e0449 | -17.5801 | -47.48758 | 2025-05-17 04:17:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ef2f788-f108-3f36-a2e9-05131fcba3eb | -20.97277 | -44.3304 | 2025-05-17 04:17:00 | NPP-375D | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 794f58f9-f103-38f5-b291-6e68d212a4ac | -17.77929 | -42.80564 | 2025-05-17 04:17:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 282f4338-14e6-335c-961a-7051c9eac353 | -13.36557 | -43.08804 | 2025-05-17 04:17:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 58cbeed4-6a0f-37b5-88ff-e5d4ec52e9e7 | -17.227 | -47.48992 | 2025-05-17 04:17:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9cd0051-4a7a-321e-8099-16cf553762e3 | -11.79729 | -47.37714 | 2025-05-17 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85d1d036-b436-342c-95fb-80c2568ad2e2 | -11.97599 | -48.10849 | 2025-05-17 04:17:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1fd64773-e708-3826-a079-268da74299ba | -13.31 | -45.39112 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1de302e3-5e92-3900-94cb-262f8c9891c1 | -20.76594 | -46.76777 | 2025-05-17 04:17:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 974d2284-a336-372c-87f0-7dfa576fe888 | -13.3161 | -45.39582 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e21b9d8c-d206-3e93-8593-85cca43c119f | -13.31944 | -45.39638 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f1cffdb-5486-378a-85be-fd0351c5ecfd | -11.42576 | -54.29271 | 2025-05-17 04:17:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e974646-f978-3818-b1bb-e27e8ea5c159 | -12.99766 | -46.32327 | 2025-05-17 04:17:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f580c22-f70a-350c-a452-a6496a63df23 | -12.45028 | -57.1986 | 2025-05-17 04:17:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc2b6247-d7b7-376c-8a11-31ce6cff6ed3 | -11.4402 | -44.72991 | 2025-05-17 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c96e62c-a7dc-3292-a982-00a56431ab20 | -13.33003 | -45.39447 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b975431f-6dde-3d23-93bf-b8ce933647c7 | -11.16179 | -48.67495 | 2025-05-17 04:17:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 293dcb80-5352-35ef-8ab6-492eef2cb5a5 | -11.58214 | -47.61105 | 2025-05-17 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8cd10028-82e5-35b6-b430-4a64bf0796ab | -7.22727 | -44.71122 | 2025-05-17 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f66f210c-5eaf-38d8-a751-b60eedb4cd3c | -11.42067 | -54.31924 | 2025-05-17 04:17:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 562efeea-0883-3c44-915e-028c02239a33 | -13.05377 | -47.82393 | 2025-05-17 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c446c8ca-3a1d-38ef-8b0b-f9c00150282d | -13.20069 | -47.25153 | 2025-05-17 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d1a00a1d-1d80-38e6-b206-7b6152e5248d | -13.31391 | -45.3881 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 563cfcf2-3bb4-356d-9e9d-943811b95569 | -13.04401 | -53.71616 | 2025-05-17 04:17:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 302352e4-ade3-3a1b-a5a5-b54af81663e0 | -11.15403 | -48.6736 | 2025-05-17 04:17:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |


[Clique aqui para ver as próximas entradas](README8.md)
