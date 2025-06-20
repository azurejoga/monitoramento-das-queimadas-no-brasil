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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f597e43-a99e-35a7-8d24-cddb9a677bb4 | -16.29622 | -58.27005 | 2025-06-20 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 49bc6f35-8697-3a19-a62e-c53783ade7c4 | -12.51327 | -58.35657 | 2025-06-20 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| aa0d6a42-6479-3428-bdaa-4c6174456612 | -13.95769 | -56.79185 | 2025-06-20 04:53:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80dd4e42-ca27-3266-b29c-8eb87717c890 | -12.50567 | -58.35524 | 2025-06-20 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d652b96a-08c5-3bac-879a-f3ff393b097f | -12.0516 | -63.78065 | 2025-06-20 04:53:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b9945ef6-5adf-33b9-b88c-725e85ab0c78 | -16.30199 | -58.25785 | 2025-06-20 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 2e7cdf9e-d905-3e66-bc13-cb1db7e48960 | -11.95683 | -58.74645 | 2025-06-20 04:53:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 496f4c19-a869-33d3-83af-32b8253bf278 | -16.30054 | -58.26643 | 2025-06-20 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| 0a60b656-7095-3739-abfa-4c0b5ca009d8 | -12.04616 | -63.77958 | 2025-06-20 04:53:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 179dc034-572b-3212-b220-d0d3dae83795 | -16.37047 | -46.46344 | 2025-06-20 04:53:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b1eb875-8512-3dde-87d1-11e38aa75025 | -11.93459 | -48.42365 | 2025-06-20 04:53:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3b03256-7317-3336-a78f-7a21eef2c2c8 | -12.712 | -54.97603 | 2025-06-20 04:53:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 125d0af3-ecd4-3f82-b641-005ae55b7be7 | -14.04548 | -53.36036 | 2025-06-20 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53d68781-2cfa-3b3e-bf00-8cc349cf82c3 | -12.20462 | -49.61732 | 2025-06-20 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da2485ac-aa5d-331f-b0ac-f90c2b88db50 | -13.93145 | -54.49488 | 2025-06-20 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a0e793a0-e825-39c6-a0e9-f551da3c0882 | -16.29336 | -58.26507 | 2025-06-20 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| f0d05547-0ceb-3cb2-abac-9268002d3df5 | -11.98832 | -51.60958 | 2025-06-20 04:53:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f6bf6ca5-2b57-390a-a017-2c48bf57f4ae | -16.07883 | -53.74846 | 2025-06-20 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ab27b3cc-b1ae-384b-82e3-79be5cc00b15 | -12.13121 | -54.6692 | 2025-06-20 04:53:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7d1e069-be41-387d-ab8e-3942bf4d0ee7 | -11.95899 | -58.75747 | 2025-06-20 04:53:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ee7c2063-9e57-3a26-852b-f90c3c71c277 | -12.2271 | -54.2986 | 2025-06-20 04:53:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5013a8b1-ede6-380e-8307-9831a0182af7 | -13.09856 | -52.2963 | 2025-06-20 04:53:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7b032966-b681-3e9d-af76-0367e277eaf2 | -11.62092 | -58.29128 | 2025-06-20 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7621990-e12f-34c7-9e8e-31d3bd675048 | -15.07961 | -48.94442 | 2025-06-20 04:53:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 406f2ae1-f0f5-3c03-a675-0705cb5a99f8 | -10.66902 | -56.54993 | 2025-06-20 04:53:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd5baf89-f1fb-3df0-aa59-a54d16c1cda0 | -11.9618 | -53.51474 | 2025-06-20 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 955ef211-cb73-3b99-9bb2-6cf222ac66b8 | -12.57801 | -56.97658 | 2025-06-20 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4295b169-bf75-378c-8518-4c9c852201b9 | -11.96451 | -53.49714 | 2025-06-20 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c12ba0f7-bb3b-3b04-a989-10728c0bfcd7 | -11.77372 | -54.36868 | 2025-06-20 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2edf883a-d06d-3006-b1d7-a67c692243da | -13.39409 | -48.45345 | 2025-06-20 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2363aa35-7d9e-3ebf-b097-199a75a03f1b | -12.5141 | -58.35178 | 2025-06-20 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 769157da-0db7-3389-b52f-e5ba45886d47 | -14.81869 | -48.46915 | 2025-06-20 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63d31f29-67f8-3f57-b0ad-09a2a54f09a1 | -14.30984 | -59.88773 | 2025-06-20 04:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df94ff7e-299d-3ab8-9df7-156f015d7b0c | -14.43134 | -48.92249 | 2025-06-20 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 41e247ef-6450-3991-b951-d9aedcca9356 | -16.30845 | -58.26347 | 2025-06-20 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| aba6e131-50fa-3e2a-90f3-f169eeaf3237 | -10.67964 | -56.55166 | 2025-06-20 04:53:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 22608f56-eda6-38a1-914b-40601afbeaf8 | -11.94811 | -58.75019 | 2025-06-20 04:53:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e823be35-a153-380b-9ac9-a3ead80a2351 | -14.43602 | -48.91919 | 2025-06-20 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| da13532e-f448-30a4-8978-bc2631a46f94 | -11.95987 | -58.7523 | 2025-06-20 04:53:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e06af8ac-87af-3d07-bcfe-8759be0aff4d | -16.31458 | -58.25865 | 2025-06-20 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5a3e812d-cf81-3de1-be6f-0a514df7e1f7 | -12.34733 | -49.30539 | 2025-06-20 04:53:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6283867a-0c92-3deb-9bce-cf4e66ffc677 | -12.54942 | -57.71029 | 2025-06-20 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8770a70c-981f-3a0a-9a8b-ae78608d9947 | -11.65018 | -54.13968 | 2025-06-20 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b24c26d-d43f-336b-97cb-c6c85b53fb86 | -11.53296 | -56.98771 | 2025-06-20 04:53:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9165e55-0b07-3f22-89b3-303dcb3e5a04 | -16.19949 | -53.07412 | 2025-06-20 04:53:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ec9ceaa-04e3-36b5-880e-f4e28e6bb343 | -16.30486 | -58.26282 | 2025-06-20 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| 6301e739-022b-33ad-bcf5-4e3f967c9f88 | -16.67975 | -43.88778 | 2025-06-20 04:53:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 21ac56dd-97a9-3fef-ad4c-329903b1fca8 | -13.51951 | -56.57548 | 2025-06-20 04:53:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae280834-cdf6-36ef-96bb-1baa38dee6dd | -16.37083 | -46.46041 | 2025-06-20 04:53:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 420a081a-2eb4-3c6e-98c6-0f608cf92b9b | -14.4806 | -50.29223 | 2025-06-20 04:53:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| efdb43d2-c344-3834-b4cd-7411625ea805 | -11.64976 | -54.55005 | 2025-06-20 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8586b100-9db3-36f8-a532-751a341ae782 | -14.04603 | -53.35674 | 2025-06-20 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c88d11b7-2608-3acb-bb44-9af2f0d69cd6 | -14.03769 | -53.36654 | 2025-06-20 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fccfddf7-0dd5-3c4c-9cfd-9f6b22d61a61 | -14.63082 | -48.12045 | 2025-06-20 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84bb6264-910a-3939-a576-3c9e892c7912 | -14.50622 | -58.67681 | 2025-06-20 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8529f1f6-4422-3a0a-a5f4-22aab9201d59 | -16.37012 | -46.46643 | 2025-06-20 04:53:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7096f5e-e832-3c1a-b623-f4addff7af02 | -12.2856 | -57.26904 | 2025-06-20 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 517d0cd2-dc62-3d51-85ac-d9144eac5d42 | -12.75609 | -44.40675 | 2025-06-20 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cae3034d-5ac1-3284-8615-3cc3ac4c3f3d | -11.95204 | -58.75084 | 2025-06-20 04:53:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e4e124ed-106f-3624-994d-01e683ce6965 | -12.3466 | -49.31053 | 2025-06-20 04:53:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4051b31b-0ad6-3c5c-8c17-dc23719803e7 | -12.20569 | -49.62581 | 2025-06-20 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4865effd-0c41-3051-9dbd-60683c019bac | -14.43186 | -48.91864 | 2025-06-20 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 97c8a96a-c7ce-328b-a83b-2ff67f8926d2 | -12.02896 | -57.09049 | 2025-06-20 04:53:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1216873e-f4c3-3db5-96d1-bf3698c72602 | -11.14207 | -55.19556 | 2025-06-20 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6398180-1978-3c0c-83ec-68fed29cb084 | -13.39039 | -48.44888 | 2025-06-20 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0490121e-a8ae-389d-84eb-664865019574 | -11.86308 | -51.72251 | 2025-06-20 04:53:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9418368f-4be7-379f-b0d3-eb4011688dfb | -13.09913 | -52.29251 | 2025-06-20 04:53:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a0945ea3-1c67-3421-ab91-d2563af9aef2 | -16.37004 | -46.46286 | 2025-06-20 04:53:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49450008-e0a0-356b-9d11-8fcda09e7321 | -14.04103 | -53.36708 | 2025-06-20 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f81bfb54-9281-3d9c-87fb-de9ba0ef4f73 | -11.14265 | -55.19194 | 2025-06-20 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95cf2921-2452-3c61-b6cf-b118dbfc500a | -14.04327 | -53.37485 | 2025-06-20 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 176ce601-2b44-3382-81b9-387235b789a6 | -13.77696 | -54.19839 | 2025-06-20 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c860a724-250b-3549-9010-bea8ba14b557 | -16.37038 | -46.45983 | 2025-06-20 04:53:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bbb6370e-3152-3c1f-92ae-2def22be06cc | -12.6495 | -54.12265 | 2025-06-20 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 69c45106-52d7-38e2-a332-51b952d5dfe8 | -12.42543 | -54.87384 | 2025-06-20 04:53:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d31644d-5827-3b72-bf44-5b7f33805d30 | -13.80014 | -54.29247 | 2025-06-20 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c250b4d7-b77d-329f-918b-bdf3e5f70be3 | -12.52547 | -57.20445 | 2025-06-20 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f21c5eff-1ddd-3906-8954-70209ee36e7d | -11.8142 | -54.50135 | 2025-06-20 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a03025a-5f70-350f-afd4-5f0169808448 | -11.53583 | -56.9925 | 2025-06-20 04:53:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 337d4d2c-1120-3ec0-9606-1eeb4dcc9605 | -16.2984 | -58.25719 | 2025-06-20 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 096d1056-552d-38c7-a74d-fd8d45cf93a4 | -11.77647 | -54.37273 | 2025-06-20 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aed1726f-5521-3c32-b996-3a2973aed35b | -12.04686 | -63.776 | 2025-06-20 04:53:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20d626a6-23f8-34a5-87b6-a2fad54b5778 | -13.38935 | -48.45674 | 2025-06-20 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f2b94025-e75f-3320-86fa-43daf5ca065e | -11.95421 | -58.76178 | 2025-06-20 04:53:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 484adea9-3373-3864-9c6e-ad11796215a6 | -12.35127 | -49.30596 | 2025-06-20 04:53:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e14d4f59-82a7-3db6-a014-c54bbd9dc148 | -16.36971 | -46.46587 | 2025-06-20 04:53:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a5b659b0-a5af-3830-a41b-ccc4a8e8dc82 | -11.14499 | -53.93261 | 2025-06-20 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 76f132fe-cbc5-3bf7-be30-370dad202071 | -15.429 | -47.83352 | 2025-06-20 04:53:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10d753bb-ed74-3c0f-b1df-a0297d4679d3 | -16.29695 | -58.26576 | 2025-06-20 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 05d2d04c-342e-3c24-bb60-b624025badc2 | -12.5103 | -58.35111 | 2025-06-20 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8bb99477-b144-36ba-bc4c-acc3c4b6d30d | -15.6262 | -57.31079 | 2025-06-20 04:53:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2e796522-ab80-3707-9806-c8baa69af2f5 | -12.37463 | -54.16053 | 2025-06-20 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 24221871-2c36-3ab9-8208-4108751c4422 | -11.95291 | -58.74575 | 2025-06-20 04:53:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3330a037-1193-3989-8d03-3b6b2a14dc7f | -14.43237 | -48.91478 | 2025-06-20 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a23d8f61-c2ec-38cc-b10b-359857359003 | -16.30739 | -58.25737 | 2025-06-20 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 64dacaa3-edbb-3380-ab57-2c3e2641a2be | -14.03659 | -53.37378 | 2025-06-20 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6751512f-a1bd-3ee6-914a-9f47beb827f0 | -12.97268 | -54.6843 | 2025-06-20 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99236380-0284-3514-bb23-497408919cd7 | -14.03157 | -53.36186 | 2025-06-20 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2abf58a7-1897-3d8d-ac5c-619dcdb10bc1 | -12.19866 | -49.61979 | 2025-06-20 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b32050c7-12a0-3fc0-a17c-105dc3190e90 | -11.84119 | -57.76113 | 2025-06-20 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README22.md)
