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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3934ea73-d56a-3c1b-bff1-3bc1e625ac5b | -10.9319 | -44.6325 | 2024-10-13 13:56:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| eb6fd89c-34ec-309d-ad30-ed8f65706927 | -11.2637 | -44.213 | 2024-10-13 13:56:10 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 5770c01d-574a-3ce0-9de5-dd003c411f51 | -11.2454 | -44.169 | 2024-10-13 13:56:10 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 122.1 |
| a06bb7f0-22ae-3bac-a6a2-d7dfd702a62c | -11.7373 | -44.4926 | 2024-10-13 13:56:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 89.8 |
| ce54f712-c218-3964-a829-f5aa04d92d8d | -12.011 | -51.0531 | 2024-10-13 13:56:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 0eaf9be6-92b2-3de2-b749-400663de97cb | -12.0114 | -51.0318 | 2024-10-13 13:56:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 4961e4bd-9d60-31fd-b7ea-28acd763bfdb | -12.1073 | -43.1861 | 2024-10-13 13:56:14 | GOES-16 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 69.4 |
| 61b67617-cde6-3190-b5ca-e5bce448fe65 | -12.0737 | -50.6831 | 2024-10-13 13:56:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 210.9 |
| dd799ca9-4999-3842-89fb-1dad4089c817 | -13.3893 | -44.6705 | 2024-10-13 13:56:21 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 6cfefcd7-e024-3e29-976e-460a824b22cf | -13.2514 | -51.1168 | 2024-10-13 13:56:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 8c3038f0-57b9-334d-a8a0-fd6a94d976be | -13.2517 | -51.0953 | 2024-10-13 13:56:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 107.2 |
| b2610efb-d736-3da7-86d1-9041c85fe563 | -13.2329 | -51.0763 | 2024-10-13 13:56:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 4b3f7a7e-0be6-36f1-9616-1e9e8821ca58 | -14.1007 | -44.9438 | 2024-10-13 13:56:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 77c91cbe-278d-319e-aae9-b10749573953 | -17.93 | -57.3 | 2024-10-13 14:03:45 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a163cdec-ebca-3225-8e2e-9301db976fa6 | -17.9 | -57.28 | 2024-10-13 14:03:45 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 55311b89-ba80-3762-bc38-d58f8f7ac53d | -14.35 | -45.33 | 2024-10-13 14:04:00 | MSG-03 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 365bcc31-5f47-37b2-913c-ff105fb96146 | -12.18 | -50.75 | 2024-10-13 14:04:16 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d07a1ea0-526d-380c-b040-16087bf20e6c | -11.74 | -44.57 | 2024-10-13 14:04:16 | MSG-03 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 39fcfeea-d2c2-38ae-bf79-da3b5c49d5f1 | -11.74 | -44.52 | 2024-10-13 14:04:16 | MSG-03 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 30e2a4d7-e917-3e1d-9542-2f5c1fb41e24 | -12.15 | -50.74 | 2024-10-13 14:04:16 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 77e14c37-d085-39a1-a32b-c309ea678f61 | -10.95 | -44.7 | 2024-10-13 14:04:21 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ccdac786-3cb0-308b-b6bb-aa5c385afc54 | -10.95 | -44.65 | 2024-10-13 14:04:21 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a641bbc2-92b6-33b4-a332-a32b3b9de8bd | -10.27 | -47.23 | 2024-10-13 14:04:27 | MSG-03 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 16fd50b0-d13a-3ac6-a5c5-e0d9e542ae55 | -10.05 | -44.17 | 2024-10-13 14:04:27 | MSG-03 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9a423b9a-4c6d-3cd1-b59f-07f87e650b64 | -7.7 | -43.19 | 2024-10-13 14:04:43 | MSG-03 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1f61b625-7051-36fd-ac36-cfb2ce941050 | -6.17 | -41.2 | 2024-10-13 14:04:50 | MSG-03 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 229e1323-f935-347f-a4dc-104d98208d2f | -6.17 | -41.16 | 2024-10-13 14:04:50 | MSG-03 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4181f2fc-6947-3ca1-a4e6-e974d7721500 | -6.14 | -41.2 | 2024-10-13 14:04:50 | MSG-03 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 205bacd1-9936-3798-9a64-de4b937b8b4e | -4.09 | -42.28 | 2024-10-13 14:05:04 | MSG-03 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |


