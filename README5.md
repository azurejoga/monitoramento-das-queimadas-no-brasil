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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13708a75-1346-315b-ba49-3107ff7cd6a8 | 1.11134 | -59.19909 | 2024-12-29 05:59:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e7a332d-a4cb-3966-8b2a-1c0f09c5ad53 | 1.10591 | -59.19995 | 2024-12-29 05:59:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1b37538-acd5-3480-9393-97f05d0a7765 | 3.57859 | -60.2616 | 2024-12-29 05:59:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3f89dc96-111a-3c66-af8e-c5af62029097 | 0.97221 | -60.25093 | 2024-12-29 06:01:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 81658094-6cfe-3205-8773-cbec8b7bb6d0 | 0.65675 | -59.5704 | 2024-12-29 06:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1fd74d7-1754-302a-a55b-3dff85f79747 | 0.65141 | -59.57123 | 2024-12-29 06:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8754179-0f4c-3d66-ab25-5ea47d6fd5c1 | 0.65527 | -59.57279 | 2024-12-29 06:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d159046f-df92-314f-aa26-e3f28ee8617f | 1.03545 | -59.735 | 2024-12-29 06:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f039cef9-723c-3cb9-86e4-0e50cf70696b | 0.65473 | -59.56952 | 2024-12-29 06:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96443d8f-cd43-3d80-be56-636bf5c87403 | 0.96714 | -60.25163 | 2024-12-29 06:01:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d424f75-13cf-3238-8be2-e0e57d95f537 | 0.96667 | -60.24869 | 2024-12-29 06:01:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb007d94-5a0b-3c60-9078-f0eda25f2b4e | -7.0889 | -38.33401 | 2024-12-29 11:51:00 | TERRA_M-M | CARRAPATEIRA | PARAÍBA | Brasil | 2504108 | 25 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 8474bb5c-47a6-3b28-856a-c0b292fbdd22 | -5.24521 | -35.69227 | 2024-12-29 11:51:00 | TERRA_M-M | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 8f2002f1-2dde-3373-848a-62e57122841f | -7.71815 | -37.82611 | 2024-12-29 11:51:00 | TERRA_M-M | QUIXABA | PERNAMBUCO | Brasil | 2611533 | 26 | 33 | nan | nan | nan | Caatinga | 10.8 |
| ab1dba40-c110-35ba-8c5e-f7aefbee8d12 | -5.39656 | -38.13405 | 2024-12-29 11:51:00 | TERRA_M-M | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 424563a4-6a69-3a9d-9406-d87f8b791bf9 | -8.34458 | -36.8959 | 2024-12-29 11:51:00 | TERRA_M-M | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 74bc0151-47c4-3ea6-9724-c3307cdc766f | -8.65769 | -35.51144 | 2024-12-29 11:51:00 | TERRA_M-M | ÁGUA PRETA | PERNAMBUCO | Brasil | 2600401 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 9fe8e37d-ca1e-3225-a306-a4411754b4d1 | -6.89875 | -37.75297 | 2024-12-29 11:51:00 | TERRA_M-M | CAJAZEIRINHAS | PARAÍBA | Brasil | 2503753 | 25 | 33 | nan | nan | nan | Caatinga | 36.1 |
| 38034e6f-a517-3856-b955-0b9f8a12f84e | -8.84289 | -35.63195 | 2024-12-29 11:51:00 | TERRA_M-M | XEXÉU | PERNAMBUCO | Brasil | 2616506 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| ab747642-7240-3375-a157-fc5463dba5d4 | -6.42077 | -37.7349 | 2024-12-29 11:51:00 | TERRA_M-M | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 5c929115-83e4-3c6b-9465-238db03e4e72 | -6.90026 | -37.7428 | 2024-12-29 11:51:00 | TERRA_M-M | SÃO BENTINHO | PARAÍBA | Brasil | 2513927 | 25 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 9f9c2d1e-095c-38aa-8ba1-7794f321695e | -8.34592 | -36.88674 | 2024-12-29 11:51:00 | TERRA_M-M | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 877f5470-6e42-37bc-99b7-8ba141039d7f | -6.58762 | -37.29783 | 2024-12-29 11:51:00 | TERRA_M-M | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 28bafdb1-7ce4-3721-9039-13ff8c5e389c | -8.65642 | -35.52034 | 2024-12-29 11:51:00 | TERRA_M-M | ÁGUA PRETA | PERNAMBUCO | Brasil | 2600401 | 26 | 33 | nan | nan | nan | Mata Atlântica | 43.3 |
| 1251c759-50d9-3a14-bd03-5e6b38e766b2 | -5.7619 | -37.56384 | 2024-12-29 11:51:00 | TERRA_M-M | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 2c2de03c-9516-3d96-91cd-cec6581d1c39 | -9.66234 | -36.21978 | 2024-12-29 11:53:00 | TERRA_M-M | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 43.0 |
| e07bcf40-48eb-3532-9ca5-8fd3e866442b | -10.53657 | -42.4332 | 2024-12-29 11:53:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 45.8 |


