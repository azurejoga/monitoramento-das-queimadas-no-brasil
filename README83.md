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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70170e83-aaeb-3651-bf06-f4247dba0fd2 | -18.17067 | -50.38967 | 2025-10-08 04:40:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 456bfd16-a5f1-3fbe-96d7-fd8b18c3edbc | -17.57223 | -46.06082 | 2025-10-08 04:40:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6cf55228-60cc-3f34-96a2-dc75847a2da4 | -11.17428 | -54.87465 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| ee02466b-6b4c-3d00-82d5-123b82c7deef | -12.50727 | -54.71772 | 2025-10-08 04:40:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2d6d9144-dc83-352e-9a5b-30679eb967d6 | -11.77854 | -47.5597 | 2025-10-08 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d31b1e3-7165-3795-a8a0-449d79e098cb | -12.18409 | -57.23833 | 2025-10-08 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2bff0bcf-edbf-3d07-aeda-af571215cec1 | -15.63842 | -52.57651 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d6f6cf44-97af-39de-ab96-12290c0ff1e7 | -14.79473 | -41.63593 | 2025-10-08 04:40:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 78603cee-2898-3867-b1d1-9c222aee693b | -11.12223 | -54.04681 | 2025-10-08 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bc70000c-6b46-3758-a084-e8b3b8e1c696 | -13.01696 | -47.9084 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3bce7678-cf22-3f10-9a62-4f9af4c73932 | -15.3182 | -46.16748 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 72a2e659-5059-3a63-bb39-484d06885b5e | -11.99531 | -47.19457 | 2025-10-08 04:40:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35624648-560a-38bd-aee8-11f00b92c654 | -15.40129 | -48.02363 | 2025-10-08 04:40:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 773a5716-1158-3a4f-ac15-7c3384e69c43 | -13.22246 | -51.70907 | 2025-10-08 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 482e610e-28f0-3ddf-b2f5-4163b76cdddc | -17.69873 | -56.77617 | 2025-10-08 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3ac252e5-5d63-3d25-ba82-2d41642eb441 | -12.30643 | -55.10762 | 2025-10-08 04:40:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6bcabeea-f385-3129-8c53-ddf7cb2dbcbb | -11.15533 | -54.89172 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab210bd1-7d00-3cdd-b897-bae3f3101d47 | -16.275 | -50.98432 | 2025-10-08 04:40:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b4b116d-4e45-3eed-a714-1329f9cd624c | -11.70979 | -50.94952 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 1b559f62-3ea3-3491-b844-00f64f4dfc5e | -16.12952 | -47.9097 | 2025-10-08 04:40:00 | NOAA-20 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b52180ca-6e0d-35e8-b988-a34bd6b724a0 | -15.88303 | -51.14851 | 2025-10-08 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b06d1f0-ce2a-31b2-92e8-ad4c011fff0e | -11.90634 | -46.20456 | 2025-10-08 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8d17f505-e1c8-3142-a93a-ad092986c680 | -12.51479 | -54.71908 | 2025-10-08 04:40:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8600da44-e49d-30d1-a39e-77557e0ec927 | -15.26206 | -46.33146 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dcc158f8-d029-3f50-b7a4-fe2a42c71592 | -10.67668 | -54.69914 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54dd06d5-b4f0-3f55-b948-401f035fc00e | -12.24736 | -47.86086 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e80e0346-33a7-3d52-a0fd-5c8cf00219d0 | -12.2438 | -43.77732 | 2025-10-08 04:40:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cc70b39d-5918-31af-813b-c1940fb5cfe3 | -18.07125 | -44.46455 | 2025-10-08 04:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19844eec-ea20-3504-a024-8b5635ec93c6 | -18.51248 | -42.09965 | 2025-10-08 04:40:00 | NOAA-20 | MARILAC | MINAS GERAIS | Brasil | 3140100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 51b86817-4db3-375b-a861-55f80c1dfe92 | -11.1472 | -54.86341 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d42a760a-7d67-3510-9ade-2370c400a595 | -14.71452 | -46.00247 | 2025-10-08 04:40:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bf5f3ccb-0257-35f7-87a9-f079ffb16887 | -13.05138 | -47.8907 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0c6b47d-06d2-356b-a426-426be698e148 | -17.68694 | -54.21545 | 2025-10-08 04:40:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 863e4bdc-8ff6-35d7-a959-dfecefaccda0 | -15.99378 | -50.96092 | 2025-10-08 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 41a4ded8-c87c-3d8e-b994-ea3e1e31c6f0 | -13.34607 | -48.02337 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2693283d-0ed7-3c85-bfd9-3f07bbeca263 | -16.139 | -48.23856 | 2025-10-08 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2070d1e4-f8c9-3126-b809-fc361bbb7abe | -15.15162 | -52.7662 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f8ef6ca2-94b7-3d5b-93d0-9932b3548648 | -18.49788 | -43.90263 | 2025-10-08 04:40:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6a386818-45a6-3bb7-b96c-278ac4d10da9 | -12.00852 | -48.58808 | 2025-10-08 04:40:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88507700-5f9e-353b-a3b2-704e67b05e0e | -11.14629 | -54.87493 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a35844c-ad0f-3a23-a475-05af1301729e | -13.64287 | -47.28358 | 2025-10-08 04:40:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e17de445-cef3-3527-9a1a-ad8fc0aa8a01 | -18.29125 | -45.44396 | 2025-10-08 04:40:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 67f02073-99ed-3c31-9670-179473d57688 | -15.01916 | -47.55716 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f19cdd11-5b9a-30a7-8be5-4ee685c5c5f4 | -13.2728 | -47.56923 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5671375f-934e-378a-9707-abad0dfd8c60 | -13.26435 | -47.78824 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe74d36b-a04c-3b2b-a9a6-9b72d9feaa41 | -14.70846 | -46.07873 | 2025-10-08 04:40:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 43885265-74c6-3cf8-8c49-e13cc8f6ff0a | -13.58485 | -48.68487 | 2025-10-08 04:40:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 146a430c-6767-3342-96be-f587a87731d8 | -13.7535 | -45.75316 | 2025-10-08 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ab8efcb-668f-3172-a2fa-d17b89fe7f94 | -11.51723 | -51.4931 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c0c749b-a2a0-35fc-8853-db130ea1013a | -13.01925 | -47.91176 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44bd0843-efc1-37b4-b46e-fe8ad216790e | -11.91059 | -52.5418 | 2025-10-08 04:40:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a1414001-8edd-3fc8-96a7-ba7fc2cfa508 | -11.13767 | -54.8785 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 10beece6-1d39-3a60-a1ba-6051abd48bea | -14.38804 | -46.02639 | 2025-10-08 04:40:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c149631e-f093-3a3b-844c-04cbf517742d | -11.67348 | -50.96535 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2be3b041-7497-39eb-8bf9-7a91e7964574 | -14.95752 | -46.83169 | 2025-10-08 04:40:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c2df78ad-c84d-35f6-8ade-7f6cb1421835 | -15.63174 | -52.57529 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0ec1495-f5a0-34a0-9eac-2f8ec2902859 | -14.89562 | -48.08861 | 2025-10-08 04:40:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 03672511-d8bb-325f-b2e8-29830c47e1a4 | -15.98951 | -50.83464 | 2025-10-08 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14d6ae32-7849-3acf-bcad-687af078c2df | -13.07144 | -47.92768 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c25f9660-e15b-3cf0-9044-e4b267209a20 | -15.31057 | -46.16291 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cd90299d-1985-3998-92a0-909ef58c14a6 | -15.60711 | -52.57862 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5262039-4d1f-3be3-a327-260cfe2d49a4 | -11.18417 | -54.8867 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f7d884c1-fb6c-308d-a1b8-b4b94398d6a1 | -15.34745 | -52.81445 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f216694d-1ffd-3b69-a2a3-1e59a6311a0f | -13.70399 | -48.06939 | 2025-10-08 04:40:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1b04f40e-fd73-39ae-a6a5-da43654cf2cb | -16.0056 | -50.81874 | 2025-10-08 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79d3e8bf-af55-37ca-8e80-6743756d8796 | -13.02461 | -47.89978 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c9d6bad4-ec26-3e97-a38a-c29c9a7c1f5f | -16.59224 | -46.55445 | 2025-10-08 04:40:00 | NOAA-20 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d9932e2-5f16-38b6-8205-bb8faf49661e | -12.16579 | -50.96622 | 2025-10-08 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b5021a8e-0a9a-33ac-ba86-0df18be98059 | -13.58598 | -48.67727 | 2025-10-08 04:40:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 20dda942-d34f-3a6b-bab9-20b7f00b7fc7 | -10.9698 | -59.02695 | 2025-10-08 04:40:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1ac05d02-03b7-3688-a49a-1e63ddf3620f | -12.15767 | -51.44107 | 2025-10-08 04:40:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13186d94-7c74-30a5-a470-f54b571a716e | -13.27344 | -47.56491 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f5cf4359-4355-3974-9b02-0eafd21ae68e | -13.28582 | -48.48521 | 2025-10-08 04:40:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e46cb659-d09c-394a-8c93-b5ab5b13a228 | -12.44356 | -50.17381 | 2025-10-08 04:40:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e36fd18b-4f96-3ac2-a2f6-95d949200d8d | -13.07374 | -47.93681 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8935d8ad-fd3f-3d4b-860c-893cd39f56e2 | -15.70769 | -47.51175 | 2025-10-08 04:40:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c1d7189-9ec5-3c7a-8654-31151fe10130 | -17.38245 | -45.0642 | 2025-10-08 04:40:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d4d935ba-770a-38fe-8b73-475a02213773 | -11.14638 | -54.8683 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b624c642-b4f4-3806-b0a0-2da0b1de322a | -17.28483 | -42.65205 | 2025-10-08 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f1270347-dd51-36f5-93de-d70ffb4a6927 | -11.11264 | -54.03606 | 2025-10-08 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5a99e9e0-ead7-3931-989d-9f8f6170548f | -13.28068 | -47.56606 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 742730ce-7fdd-3a94-a916-92e08656ecc4 | -13.20363 | -51.69861 | 2025-10-08 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8b5b7f4-bb5d-3711-8f37-bc2cfb599b79 | -13.32065 | -48.02351 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 44690fb8-7ae0-3bea-8e6e-b0e5f29c8f91 | -13.00818 | -46.78761 | 2025-10-08 04:40:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d0784d3-1ce9-3732-a72b-66eeac82f79f | -11.17901 | -54.87043 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| af3e6e6f-5adc-3597-a994-68fc5588face | -14.65326 | -52.53026 | 2025-10-08 04:40:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d2313aa-ba78-3020-b276-df0f42534c1f | -15.35418 | -47.33391 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 271b6167-9a54-3ad8-aacf-b4308803b6a5 | -14.14381 | -43.17406 | 2025-10-08 04:40:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b5c4d48a-bfb8-359a-82b0-dbe547eeca5a | -12.94569 | -46.84966 | 2025-10-08 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4fb4f80f-3acb-32e2-aa75-93a76c4369ea | -13.29247 | -47.77124 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f380eaff-0b8f-3a32-80b1-122a03425572 | -14.95819 | -46.82687 | 2025-10-08 04:40:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3140954f-1044-3891-8642-268a01158cb5 | -15.11965 | -48.11246 | 2025-10-08 04:40:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 481ba6bc-f095-3833-855c-e0d489f5549b | -14.6499 | -52.52966 | 2025-10-08 04:40:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed6d95dd-9870-387c-966a-d51d4c83f0ee | -15.31333 | -46.16678 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8add03e7-609c-3428-b2e7-a1f31ac86ab9 | -12.34746 | -50.28862 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 23b9d8e0-3f9b-3a04-9012-87a553183334 | -18.45654 | -42.52931 | 2025-10-08 04:40:00 | NOAA-20 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8433ac7f-9873-39f4-bbcd-45e4b9b5faaf | -15.38974 | -46.27673 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a7fd7e13-b488-3637-8edf-5ac0597bdaa5 | -14.70591 | -48.40003 | 2025-10-08 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a52857f4-8789-36b6-90d9-e1e1c3b466de | -13.78821 | -45.80243 | 2025-10-08 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 236262d7-8c5d-3069-b2ca-25f04b969ff5 | -11.98974 | -46.77612 | 2025-10-08 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README84.md)
