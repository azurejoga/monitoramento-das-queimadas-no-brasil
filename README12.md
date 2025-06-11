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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96d9789f-ccf8-3df3-92d8-fad6cb172c7c | -10.3079 | -59.08773 | 2025-06-11 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b098b74-6595-35ab-9331-eacf9f8d9260 | -10.51254 | -53.63008 | 2025-06-11 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ffd7f02-8b12-375b-a1ee-3c8d039bbfc0 | -9.92716 | -59.90395 | 2025-06-11 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f51d56b-0eec-3e09-b4c0-180d82aa8ec1 | -9.40199 | -48.42969 | 2025-06-11 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c39907c3-29c0-3520-9262-a442d8051dec | -10.19284 | -49.59481 | 2025-06-11 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5b855dfe-b387-37ba-bd5d-675a1cc0d3a0 | -10.80676 | -55.86834 | 2025-06-11 05:10:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| eed8002e-66b0-3616-8c4e-0d030fdab0d1 | -10.24105 | -52.23338 | 2025-06-11 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1f6cad1c-9889-3175-ac6a-9d508a733cd1 | -10.19407 | -49.58552 | 2025-06-11 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08262272-057d-3e1b-954a-bc421ff0c456 | -10.36473 | -57.50082 | 2025-06-11 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42f497d7-cba1-3ea6-b953-1c5b0dc2ac88 | -14.04102 | -55.13166 | 2025-06-11 05:10:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa68824d-7f2f-39c4-910d-7ffb64320462 | -9.82302 | -61.40749 | 2025-06-11 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55be0911-694a-384e-81ec-87303d9200f1 | -12.5195 | -57.22845 | 2025-06-11 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aa801b09-fc4d-34ab-85d5-31f92cdcc2f2 | -10.94583 | -55.31443 | 2025-06-11 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| edf05167-1a9f-32a7-b187-820e81fcb5d0 | -10.0508 | -48.66992 | 2025-06-11 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef38f083-f731-3b2d-9da7-4f019737e866 | -9.38147 | -48.41575 | 2025-06-11 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8911526c-5667-301c-8759-c868c58fc7a4 | -12.26562 | -57.60633 | 2025-06-11 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e95bba16-3e37-31aa-b727-db91f565c4c6 | -8.16804 | -46.50692 | 2025-06-11 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 799e9e5f-cd43-30f5-88ce-bd7e0d460e7a | -11.91533 | -54.82458 | 2025-06-11 05:10:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0074b54b-d7b2-3116-91c1-ec10ef6dd6c8 | -10.70028 | -49.51924 | 2025-06-11 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8d15d14c-9771-38b7-9a66-235541e71050 | -11.36691 | -56.56352 | 2025-06-11 05:10:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f9bfbd0-24c9-3733-8358-538b0b2e160f | -11.77437 | -54.37779 | 2025-06-11 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3985dfc-b23d-3c0c-a4dc-f35aaa0bd83d | -9.40056 | -48.44038 | 2025-06-11 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c294a942-ec7b-36ef-8fac-00345e165062 | -10.18853 | -49.58792 | 2025-06-11 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 570da148-5992-37cb-addf-48db41bb9973 | -11.77506 | -54.373 | 2025-06-11 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5a66eab-8c2c-36c5-bed1-1e9e6e9b2e6d | -12.52006 | -57.22476 | 2025-06-11 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 813dbf46-c9c7-3851-83a1-4d4ed1455933 | -9.40151 | -48.43325 | 2025-06-11 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0be5312e-a39a-301f-848d-8f0ee11d6ada | -11.90724 | -54.82797 | 2025-06-11 05:10:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c0c0e2c9-7987-32b4-8473-64ee10146272 | -13.08357 | -47.43526 | 2025-06-11 05:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cceebb26-524d-3ab7-94f8-3a4e71f23a7b | -10.3614 | -57.5003 | 2025-06-11 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ed380cf-c9bd-3aeb-a57a-849edad30d01 | -10.18894 | -49.58483 | 2025-06-11 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 194c52bd-e5c0-39c9-9023-a1cc8b88b48e | -14.25884 | -45.49687 | 2025-06-11 05:10:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43e2f495-adc8-3106-ba10-19d0b827e13d | -10.24048 | -52.23749 | 2025-06-11 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 70e8944e-cb3f-38b2-9c20-145059e44734 | -8.2843 | -47.44801 | 2025-06-11 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73448d00-0648-3405-83d3-b38791de84b6 | -11.90788 | -54.82348 | 2025-06-11 05:10:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 75a10589-6e27-3bb6-853e-f86113408f81 | -10.94882 | -55.31915 | 2025-06-11 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b5435683-9f8a-3fd8-9c79-a59d7a0fb07b | -11.13567 | -53.94207 | 2025-06-11 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 82408ade-b56a-31e2-bb2a-7171a24ff7ed | -10.64783 | -49.42787 | 2025-06-11 05:10:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cfd1a6cc-ddb5-35e9-9f68-e953fdaf5212 | -10.1873 | -49.59721 | 2025-06-11 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1b39e80-71dd-3a45-9ce1-8bc344a6acf3 | -13.64979 | -53.94003 | 2025-06-11 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3d864fd-8b67-3745-aa9c-b528d412b817 | -14.03415 | -55.12591 | 2025-06-11 05:10:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c2c92363-4128-3d05-8566-8c23653f9f4a | -12.13557 | -54.6609 | 2025-06-11 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10a0df1c-815c-39ed-8a57-42e6417a905a | -10.94644 | -55.31024 | 2025-06-11 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a32bc961-cea1-32dc-a4f6-52f752d1b909 | -12.52678 | -57.20317 | 2025-06-11 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 572f810d-68eb-3193-a9b5-acfe06a527c8 | -11.77888 | -54.37352 | 2025-06-11 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65571b6a-24ce-382d-b909-04c758d7a870 | -10.18771 | -49.59413 | 2025-06-11 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 096a106e-48d7-389b-8099-577ce54e9137 | -11.56925 | -47.43599 | 2025-06-11 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4c6a5066-e14d-37b0-968a-cac1638d32b6 | -10.19366 | -49.58862 | 2025-06-11 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f474db48-4ee7-36d1-b74e-218a7c090f0e | -12.78516 | -48.72452 | 2025-06-11 05:10:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a203c5c1-4d76-37cd-838c-3fe04032cee6 | -10.50802 | -53.57781 | 2025-06-11 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cfaa620c-b63f-30a5-9887-6cfdda2facd5 | -10.94523 | -55.31861 | 2025-06-11 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a90f376-b9a5-36ae-bbe4-101007463f2b | -12.78471 | -48.72826 | 2025-06-11 05:10:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| afdec9bd-a8d2-32f8-956f-7808837dd14b | -14.25114 | -45.50313 | 2025-06-11 05:10:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bc31e8bb-4a96-397f-aa29-f4def153f84d | -10.65262 | -49.43189 | 2025-06-11 05:10:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e77998fe-71b7-3c42-b2e2-d8b7160e5b5c | -13.64577 | -53.9394 | 2025-06-11 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a05991c-f249-3102-af50-cb4ed8a2b3e7 | -9.82372 | -61.40326 | 2025-06-11 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12e369cd-9b9f-3b12-82bb-97546dac3c9f | -13.47108 | -56.85395 | 2025-06-11 05:10:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 70aae89c-e418-39b7-b437-18f6d12c733e | -12.52061 | -57.22108 | 2025-06-11 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6c79eb98-2425-3b9b-8d22-24d1a6ea63b1 | -12.08735 | -57.37504 | 2025-06-11 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6343d199-6d30-3c3c-b539-7f2bf65093fa | -13.09247 | -52.28706 | 2025-06-11 05:10:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5d7a82e-edaf-3f1a-882d-0332d54e8b38 | -9.36237 | -57.43976 | 2025-06-11 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f20da2f5-022a-3093-a083-1f4748875f82 | -13.7914 | -54.30805 | 2025-06-11 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 199fd03c-75ae-3cb7-a0cb-7b63dde3722b | -14.04036 | -55.13635 | 2025-06-11 05:10:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f3d7586-89ca-37f5-9b81-cde3d5040e30 | -12.34754 | -57.43061 | 2025-06-11 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 370b1c49-e165-33d6-b183-611df3aec1a8 | -11.05297 | -55.03619 | 2025-06-11 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0928efe-fecd-32f3-9c06-f1cb798a489a | -11.70254 | -54.50212 | 2025-06-11 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d435e477-7517-377d-a14e-88df56c1a281 | -12.20284 | -49.62678 | 2025-06-11 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd20a8e7-b03f-3587-bdea-1f3c7c7dab1a | -10.94451 | -55.31136 | 2025-06-11 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b06211cf-e332-331a-99ce-90026e2720eb | -12.51895 | -57.23213 | 2025-06-11 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ae962b21-2def-37fd-9660-0c11cb4bde77 | -11.7782 | -54.37832 | 2025-06-11 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e458ce1-8207-3b93-a36b-ab84467b179e | -10.18812 | -49.59103 | 2025-06-11 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d74c7a60-dfe6-386f-a372-caa119d85ca5 | -11.37831 | -56.55761 | 2025-06-11 05:10:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c77d4773-d545-3cdb-840a-1abaa7e40400 | -10.65305 | -49.42862 | 2025-06-11 05:10:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 25079f47-68bc-3778-bff8-007e51f127d8 | -11.13926 | -53.91744 | 2025-06-11 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8258da25-e5db-3dd4-9116-43fcbc003c53 | -12.77952 | -48.72386 | 2025-06-11 05:10:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 57670032-5edc-3cfa-89cf-3d05bee09718 | -10.87911 | -54.74588 | 2025-06-11 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2dc2fb2f-2e95-3740-b6c5-352b3e280e71 | -9.8201 | -61.40263 | 2025-06-11 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08b000b6-0347-346c-b7b4-3921ac8fdd8a | -8.9627 | -47.96542 | 2025-06-11 05:10:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d24d9fb5-bc40-3a32-95e5-3efb80bd846d | -10.19325 | -49.59171 | 2025-06-11 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5962619b-1410-3d04-bf8f-491d9a92123d | -14.25183 | -45.49631 | 2025-06-11 05:10:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0b8ec713-424f-389e-ba8d-123b27c5c824 | -12.29418 | -50.10393 | 2025-06-11 05:10:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 682f3c61-7fa2-388d-8c72-c572404f0758 | -10.8828 | -54.74645 | 2025-06-11 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8bd4475-16d3-3851-abd2-3a67cb9188ca | -10.36805 | -57.50135 | 2025-06-11 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a271a87-11a0-349e-bf1c-a716900b7779 | -12.13491 | -54.66558 | 2025-06-11 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4c2dce3-bcc6-3a1b-b4a1-e56b38b97bd5 | -11.76375 | -55.58054 | 2025-06-11 05:10:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e7cf044e-b711-3a30-880b-029522f0fc55 | -12.52733 | -57.19948 | 2025-06-11 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ba9ca91-a07c-3f00-aa23-3a6f8852993a | -10.87126 | -54.32242 | 2025-06-11 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 567cce26-5539-3d11-8dc5-931542af9df6 | -10.87477 | -54.74972 | 2025-06-11 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 513af601-adf4-3b10-8ec1-8056295a60bb | -14.52928 | -48.02361 | 2025-06-11 05:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f759f9d-457d-34e8-b1a5-6819ee22af08 | -9.86021 | -57.64429 | 2025-06-11 05:10:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3bc6fe2-916e-388e-b023-b5682eb9927f | -10.65915 | -49.4227 | 2025-06-11 05:10:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 63756b1b-3da7-3b28-a42c-8e43d9361632 | -11.83716 | -60.92007 | 2025-06-11 05:10:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0339b90-84ab-35a2-98a4-4633c4dba0ef | -10.94462 | -55.32278 | 2025-06-11 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1e2ee6f-2dc1-3a3a-9d2d-8ab7801d8858 | -7.24231 | -49.5335 | 2025-06-11 05:10:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33ddb64b-675a-3b47-b4c7-30ad2a1d3443 | -9.41298 | -48.43112 | 2025-06-11 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e30b9055-6cc3-3927-a626-e2490dc7f8ba | -20.54362 | -54.12529 | 2025-06-11 05:12:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4862cb3-2704-327f-9175-90d511fd2936 | -20.09745 | -50.86841 | 2025-06-11 05:12:00 | NOAA-20 | SANTA CLARA D'OESTE | SÃO PAULO | Brasil | 3546108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9dea65f4-3f41-3975-8c59-f526a11f8a9d | -15.38873 | -47.89764 | 2025-06-11 05:12:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4190379c-289a-3536-b537-b7e35aa0b515 | -20.10003 | -50.86829 | 2025-06-11 05:12:00 | NOAA-20 | SANTA CLARA D'OESTE | SÃO PAULO | Brasil | 3546108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c4b53a92-3daa-3e59-8669-4bf70177cf61 | -20.10282 | -50.86909 | 2025-06-11 05:12:00 | NOAA-20 | SANTA CLARA D'OESTE | SÃO PAULO | Brasil | 3546108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f59e45bd-403b-313a-a0f0-79f50be1dc2f | -20.75475 | -48.53217 | 2025-06-11 05:12:00 | NOAA-20 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README13.md)
