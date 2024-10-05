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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9ecce3f-b79d-3e7e-9468-5e98bc2a410e | -18.51682 | -52.86134 | 2024-10-05 05:12:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| f22692aa-b929-3ff1-8f13-e7616c0555ce | -18.51556 | -52.85612 | 2024-10-05 05:12:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 063f348b-4702-392c-b348-7fb4d7e790d7 | -18.50296 | -52.85369 | 2024-10-05 05:12:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 2afe2352-cdee-3f44-86c9-2e47ad901a4e | -18.43836 | -42.2016 | 2024-10-05 05:12:00 | AQUA_M-M | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 28b04c1d-aed2-39e4-bff5-acc58d184dd9 | -18.43788 | -49.76263 | 2024-10-05 05:12:00 | AQUA_M-M | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 12d94f30-3b2d-3e8f-b6a7-456ab6f93ad8 | -18.43578 | -49.77494 | 2024-10-05 05:12:00 | AQUA_M-M | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 56ca3001-cefd-38b5-b15a-f4c2e8a284a7 | -18.04828 | -46.44179 | 2024-10-05 05:12:00 | AQUA_M-M | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9332501c-c198-33e2-b6d1-6070104c3440 | -17.80892 | -50.63664 | 2024-10-05 05:12:00 | AQUA_M-M | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 7397286b-f0c8-30e9-a06c-5928cdd68d17 | -17.76365 | -43.82579 | 2024-10-05 05:12:00 | AQUA_M-M | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 5d159d53-ed8d-3f5a-b0e6-b357a28e1b73 | -17.75424 | -43.82446 | 2024-10-05 05:12:00 | AQUA_M-M | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| bf76d4b0-8668-3c43-90a2-e5e3b37e28c6 | -17.71953 | -43.79766 | 2024-10-05 05:12:00 | AQUA_M-M | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c4b81abe-828d-338f-81d0-6bbb3cc1ea01 | -17.7101 | -43.79641 | 2024-10-05 05:12:00 | AQUA_M-M | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f93373fe-ca6e-3b5e-934d-5a2758db5e15 | -17.64061 | -46.9914 | 2024-10-05 05:12:00 | AQUA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 61f0286a-e44b-398c-8049-76e52f3feec7 | -17.63168 | -46.98981 | 2024-10-05 05:12:00 | AQUA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 08e57654-827e-3be8-83ef-4efe21efbd67 | -17.6295 | -43.25305 | 2024-10-05 05:12:00 | AQUA_M-M | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b94bde84-e31b-3e56-a818-966855c12d07 | -17.62802 | -43.26391 | 2024-10-05 05:12:00 | AQUA_M-M | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 33e39e4a-70f5-391c-b584-aa48e2e2e424 | -17.62275 | -46.98824 | 2024-10-05 05:12:00 | AQUA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| f1f8f5a0-b034-3e7a-b301-8cd3c23ac0bd | -17.59281 | -46.94474 | 2024-10-05 05:12:00 | AQUA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7aca0155-5a7e-3d05-8f10-485fb8f9b020 | -17.1476 | -51.7248 | 2024-10-05 05:12:00 | AQUA_M-M | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 63.3 |
| bc0946a5-f8b5-39f4-82f3-17691defbeb0 | -17.13886 | -51.70479 | 2024-10-05 05:12:00 | AQUA_M-M | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 0655778e-7856-3b9e-bc5b-ade1be2e04b1 | -17.13573 | -51.72251 | 2024-10-05 05:12:00 | AQUA_M-M | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 2b1c5440-6f4b-3bc0-8872-09afa27fdf03 | -16.19069 | -49.25503 | 2024-10-05 05:12:00 | AQUA_M-M | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 2697112f-47d5-32f9-81b6-37ef2ec5d7f4 | -16.18871 | -49.26716 | 2024-10-05 05:12:00 | AQUA_M-M | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 97c4643f-f325-3c3b-8d26-27cc363e7aa7 | -16.1786 | -49.26541 | 2024-10-05 05:12:00 | AQUA_M-M | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 82b133f2-6672-3b21-bfcc-813a2adc11b9 | -16.12019 | -50.25533 | 2024-10-05 05:12:00 | AQUA_M-M | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 184412fa-0bd8-3960-913e-7c81a2f47569 | -16.11919 | -50.24835 | 2024-10-05 05:12:00 | AQUA_M-M | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 73c24ce0-6e92-3814-b6c5-bd67c60fe08e | -16.11773 | -50.46357 | 2024-10-05 05:12:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 209937c6-7810-3eab-b1db-f072773671ea | -16.10962 | -50.44487 | 2024-10-05 05:12:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 8e1d82bb-9ff3-39c6-956e-e642edd977b4 | -16.10841 | -50.24605 | 2024-10-05 05:12:00 | AQUA_M-M | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 965da6f1-3f92-3d37-b8cf-3ef92698be19 | -16.10678 | -50.46119 | 2024-10-05 05:12:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| d23fc2c7-fe76-36ad-9367-2c64c3b7f762 | -16.099 | -50.43551 | 2024-10-05 05:12:00 | AQUA_M-M | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| cfc6d3b3-da81-3cb2-a05b-31abee15a8df | -16.09867 | -50.44258 | 2024-10-05 05:12:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| d8cb5574-d320-378c-9077-5e3f671831ae | -16.09771 | -50.24321 | 2024-10-05 05:12:00 | AQUA_M-M | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 60fbf738-f318-3141-9c64-c0d8f03ebb3e | -15.71838 | -48.32087 | 2024-10-05 05:12:00 | AQUA_M-M | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f3efe3ee-5553-3f46-91dd-9cf94d0148b8 | -15.4528 | -47.67896 | 2024-10-05 05:12:00 | AQUA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e02ad6e6-f918-329a-a9a8-c2940b5b91d8 | -15.44922 | -47.42363 | 2024-10-05 05:12:00 | AQUA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ea1a2a89-817f-3303-97c3-01636cd25fcd | -15.41386 | -47.40812 | 2024-10-05 05:12:00 | AQUA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e88afb68-8c62-3b64-8c8f-50dcfc0cd75d | -15.41236 | -47.41759 | 2024-10-05 05:12:00 | AQUA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| bc3aa71b-d91e-3bab-9e71-b67ab7596e59 | -14.82605 | -48.81166 | 2024-10-05 05:12:00 | AQUA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 390140b7-7cb7-32d7-a13a-03a390797a9b | -14.59684 | -48.82893 | 2024-10-05 05:12:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 58bedce6-db0f-3134-86c4-e2d0f02590ac | -14.58871 | -48.81525 | 2024-10-05 05:12:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 00239d47-c529-3e45-b227-d12a3577101c | -14.58678 | -48.82708 | 2024-10-05 05:12:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a60a1256-6198-3414-b443-8b967c054b87 | -14.58061 | -48.80147 | 2024-10-05 05:12:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 27.8 |
| c61eee43-7794-3419-a658-c04d0217fd99 | -14.57866 | -48.81339 | 2024-10-05 05:12:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 0705e3c1-d3c5-3f2e-aa56-d2a10c283010 | -14.57057 | -48.79965 | 2024-10-05 05:12:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 0bfb7d37-29e4-345f-92b5-4c7fb2086ea6 | -14.28502 | -48.16013 | 2024-10-05 05:12:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 68f9620e-d509-34b9-ac74-0345d0785524 | -14.21961 | -46.47743 | 2024-10-05 05:12:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bb0f22e9-4c8d-3831-9483-3c5902c0ee23 | -14.16159 | -42.47252 | 2024-10-05 05:12:00 | AQUA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| e18d979a-9b35-3c28-977e-5c8d17b9b859 | -14.0295 | -47.27143 | 2024-10-05 05:12:00 | AQUA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 9d63e2a7-c7b0-391b-a0d0-a88f57133d8b | -14.02789 | -47.28151 | 2024-10-05 05:12:00 | AQUA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5e25543a-535f-3f60-a937-cc970a8401d2 | -14.02471 | -47.26379 | 2024-10-05 05:12:00 | AQUA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 35c50fc4-59f2-394a-a3a4-d6fae6db143a | -14.02316 | -47.27372 | 2024-10-05 05:12:00 | AQUA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 83.5 |
| ec74b479-4dcc-39be-967a-025e4b6acb2a | -13.54521 | -48.6039 | 2024-10-05 05:12:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b3590232-037e-381b-ba34-6ab934c315b5 | -13.54323 | -48.61579 | 2024-10-05 05:12:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 46be590d-4796-337a-9e27-c6923158ca34 | -13.53031 | -48.63308 | 2024-10-05 05:12:00 | AQUA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 44f23857-75c6-339b-b5df-8a972042d399 | -13.16746 | -46.35636 | 2024-10-05 05:12:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ced8279c-a4d1-39d0-8390-8dccbfe9c269 | -13.13465 | -46.32593 | 2024-10-05 05:12:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 17.6 |
| e7905c37-92bc-3a3f-b6b6-64d5932520df | -13.1332 | -46.33536 | 2024-10-05 05:12:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1bb5bee6-1b93-337d-ba2f-db7253823b4d | -13.12884 | -46.36369 | 2024-10-05 05:12:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9a30d062-85bf-31a3-9cc9-224ffddc3bfc | -13.12738 | -46.37317 | 2024-10-05 05:12:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 62e98bf5-927b-3d68-9cc9-8e8cf7a931bf | -13.12564 | -46.32436 | 2024-10-05 05:12:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| c951cc26-9efc-3761-a512-f3af8977a43a | -13.12417 | -46.3339 | 2024-10-05 05:12:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 1689739d-cc05-3f96-b773-f1631b4f864a | -13.12126 | -46.35282 | 2024-10-05 05:12:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 09863c61-0c76-3b46-89ee-8567a41a4a11 | -13.11979 | -46.36229 | 2024-10-05 05:12:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b7d8a8de-1867-3fef-a1d1-9173fd000a5f | -12.90355 | -44.62513 | 2024-10-05 05:12:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 44c270e4-8842-32b4-b955-857080c3366d | -12.87829 | -44.61207 | 2024-10-05 05:12:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e1288aff-e156-38d9-98b7-149d571b8f12 | -12.87696 | -44.62112 | 2024-10-05 05:12:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 49f4ed42-0da8-3681-b2e7-b8f933ffc45b | -17.04788 | -56.67386 | 2024-10-05 05:12:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.4 |
| fbf5e1bb-8ad6-34a9-a23c-e7f4969655df | -17.04472 | -56.66842 | 2024-10-05 05:12:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.8 |
| b12a7650-2510-3b0e-b72a-d7f7d18d668c | -17.03693 | -56.7962 | 2024-10-05 05:12:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.5 |
| b0c30883-86fb-38fe-b375-24e96cdc75d3 | -17.03647 | -56.70931 | 2024-10-05 05:12:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.7 |
| b3101a21-6528-3b94-bc96-8b872cddc081 | -17.01971 | -56.79228 | 2024-10-05 05:12:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.7 |
| 55937d9e-1d48-3301-bdbf-9f27ec8f33d1 | -17.01095 | -56.74675 | 2024-10-05 05:12:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.5 |
| be539a7b-fba3-3d14-95d6-7454dd93965d | -17.00249 | -56.78836 | 2024-10-05 05:12:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 145.5 |
| 787143c2-5baa-373e-9dc5-105e1de4e50a | -16.99641 | -56.74828 | 2024-10-05 05:12:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 153.4 |
| 673ee776-d960-365f-a7d9-d3d5052eae08 | -16.99378 | -56.74287 | 2024-10-05 05:12:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.1 |
| 9ac1c3af-6894-3719-896c-a672ce852553 | -16.98764 | -56.78978 | 2024-10-05 05:12:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.4 |
| c84b6fa5-7f30-33a6-a708-7ab1ab97f5a8 | -16.98527 | -56.78444 | 2024-10-05 05:12:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.5 |
| d48653c8-3c3c-3f09-8a5f-1a123bcdddc6 | -21.82819 | -48.74751 | 2024-10-05 05:14:00 | AQUA_M-M | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 20034ec5-b5bf-3f17-af02-7962eb213ec1 | -20.68243 | -47.08574 | 2024-10-05 05:14:00 | AQUA_M-M | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 67d5a18e-1af4-3372-a38f-b0b8c3339b9c | -20.681 | -47.09515 | 2024-10-05 05:14:00 | AQUA_M-M | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 6326b278-3c81-3611-9815-57c347e8e12b | -20.65122 | -51.47049 | 2024-10-05 05:14:00 | AQUA_M-M | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.2 |
| d4dc4818-b5d8-3211-973c-6375876eaf3b | -20.64859 | -51.48515 | 2024-10-05 05:14:00 | AQUA_M-M | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 82.0 |
| aedbcf3e-5f4a-39ca-8523-0359951e03ec | -20.52931 | -44.90137 | 2024-10-05 05:14:00 | AQUA_M-M | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 426b972b-c96b-3618-89fd-7aa15472b436 | -20.24827 | -47.09426 | 2024-10-05 05:14:00 | AQUA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d9892681-a051-3c00-81d4-b8b3b65825ae | -20.10861 | -50.16161 | 2024-10-05 05:14:00 | AQUA_M-M | MACEDÔNIA | SÃO PAULO | Brasil | 3528205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| c3b8a6e5-617e-3b89-bb15-85b2c5d70d7f | -18.69376 | -57.26196 | 2024-10-05 05:14:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.5 |
| 86db47e8-4b05-3d14-96bd-2ad1cf265f4e | -18.67744 | -57.25004 | 2024-10-05 05:14:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.2 |
| 83168526-28d9-3a0c-bf23-db1aec5b30b0 | -18.67659 | -57.25793 | 2024-10-05 05:14:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.9 |
| b5178357-ea3f-33ba-baec-820c46f1c88f | -18.66872 | -57.29208 | 2024-10-05 05:14:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.1 |
| 71ac821e-63e9-315b-993b-a2ef151b8ad0 | -1.05705 | -47.93155 | 2024-10-05 05:27:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 5abb4467-cca6-3774-92e8-061401e45ccb | -1.05612 | -47.93773 | 2024-10-05 05:27:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c5d39385-1a2b-3df3-91d8-9d240c980197 | -1.05596 | -47.92694 | 2024-10-05 05:27:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6402c319-6d18-375c-8ec3-292138bfda45 | -1.05499 | -47.93314 | 2024-10-05 05:27:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 85f42de7-7ec5-30f8-a9ee-54be0c362b6c | -3.27805 | -48.8036 | 2024-10-05 05:27:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dd263e95-3bd8-328b-9cbd-c3d8afd41e7f | -2.91179 | -48.91409 | 2024-10-05 05:27:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d76f05e4-f34e-3945-b573-a191b7832ebf | -2.90523 | -48.91293 | 2024-10-05 05:27:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 62450e94-f388-3511-8c86-432f63fb81d3 | -2.77944 | -48.57983 | 2024-10-05 05:27:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6f1a5e7-d000-3cea-9c51-ca557da5f654 | -2.7786 | -48.58565 | 2024-10-05 05:27:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04395649-0b72-30a8-8781-228eed7b767d | -2.72219 | -48.83809 | 2024-10-05 05:27:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README131.md)
