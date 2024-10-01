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

## Dados Diários - Página 155

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3ce3b1f-dc54-355d-9d8a-e4f5b283cde2 | -9.27152 | -67.61059 | 2024-10-01 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| daa4dac9-a50e-38de-ab6f-6ed940b13809 | -9.26927 | -67.60284 | 2024-10-01 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42f6f02b-72a4-3edb-9bb6-22cbe7005814 | -9.26871 | -67.60645 | 2024-10-01 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 596980ea-4b22-3b3d-9d09-0829e725a19e | -9.26815 | -67.61007 | 2024-10-01 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9025850f-ccdc-3af6-aa59-ee86f5dc5114 | -9.26585 | -68.73886 | 2024-10-01 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 27a0889b-1d17-315a-a3cf-a9c3f42078ba | -9.26199 | -68.74182 | 2024-10-01 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 454e90f7-fc72-30ae-a361-cdb7ab358596 | -9.20684 | -68.31024 | 2024-10-01 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68b3772c-1256-3655-ad46-3ebc1c2bce02 | -9.20352 | -68.30972 | 2024-10-01 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c64855e6-d152-3891-bb67-f3961ffcb7a7 | -9.19738 | -68.78474 | 2024-10-01 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b8a0cb6-cb05-3b82-b2d1-158e522b58fc | -9.19408 | -68.78423 | 2024-10-01 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b536ad3-443b-3ac1-99cb-1f7223236ee1 | -9.15807 | -68.16634 | 2024-10-01 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 973c3773-eb62-363e-b424-5ae51095df78 | -9.07087 | -68.48682 | 2024-10-01 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d25caa0c-886e-3825-8505-7b0596fffc85 | -9.03779 | -68.50307 | 2024-10-01 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40d83780-d069-3a04-b73d-d50567494da8 | -9.03724 | -68.50657 | 2024-10-01 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44b94961-77de-3800-98f1-c8cf52e710a9 | -9.03393 | -68.50604 | 2024-10-01 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89896c1c-6eb1-3931-94b4-e01cf42c8b89 | -10.68883 | -68.97593 | 2024-10-01 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37a7fb96-8d76-398b-9abe-5676d76ea394 | -10.61005 | -69.04588 | 2024-10-01 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 41fef652-aa98-3523-abf0-5a525fe684a0 | -10.60951 | -69.04938 | 2024-10-01 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 46f039f5-3dba-3037-88f1-ff8b59703db9 | -9.51833 | -68.57877 | 2024-10-01 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad4da7c2-c4d2-3494-b142-19526491982f | -9.51779 | -68.58227 | 2024-10-01 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a93d1e92-dd10-373d-b8b6-959ed29b332f | -9.49275 | -68.50298 | 2024-10-01 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e0d8f03b-7726-3ff1-a180-3696aaa6d16d | -9.42712 | -68.75039 | 2024-10-01 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7b5ff15a-a839-39b2-9b51-92fa25e05d83 | -9.42657 | -68.75388 | 2024-10-01 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7fe1382-3c10-3a40-ba84-a6f24ba837d7 | -9.42326 | -68.75336 | 2024-10-01 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18c19979-d269-39a5-b901-2580de28cf16 | -9.41631 | -68.66618 | 2024-10-01 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4fb27c7-3b82-3289-9d35-5fd601ea7b54 | -9.4151 | -68.60874 | 2024-10-01 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b248b05f-12a3-3318-8f04-dd81ff368955 | -9.40679 | -68.59671 | 2024-10-01 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e837a67c-ac34-35b7-b3fb-617fade95107 | -9.3713 | -68.78056 | 2024-10-01 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3ed58ed-917d-393c-b46f-165f9bc20c34 | -9.36799 | -68.78003 | 2024-10-01 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 025f5131-2ca5-34c4-b7a4-9a8a2c0b3815 | -9.36745 | -68.78352 | 2024-10-01 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6cd0a487-3b29-31db-8bc2-a12dcb5a80c9 | -9.34882 | -68.83762 | 2024-10-01 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d04e2a5c-fa8c-3dbd-b7e6-8c167e9110e0 | -9.34827 | -68.8411 | 2024-10-01 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 720b1d43-3d34-31a5-aa32-b3471cd477a8 | -9.3233 | -68.76224 | 2024-10-01 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3eb20e11-5698-3e97-801f-8aceb4217eee | -9.32053 | -68.75823 | 2024-10-01 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8de8e5c5-9512-36de-8f66-e170fd5e6aca | -9.31999 | -68.76171 | 2024-10-01 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b7431ef-e99d-3925-8ec1-26924c7dcefd | -9.97452 | -67.8913 | 2024-10-01 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 39e385e3-1df8-30b2-9bae-a6c0fd850749 | -10.51625 | -68.3816 | 2024-10-01 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 271447bc-4bae-31c1-b36e-b8263b0e643f | -10.48356 | -67.91034 | 2024-10-01 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8c77c47c-aba6-381a-8cf4-bf36db0e86e2 | -10.483 | -67.91396 | 2024-10-01 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6b26f8ec-b547-3fb1-a6ff-af7dcc9f9262 | -10.48072 | -68.39058 | 2024-10-01 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42cec091-c34a-397c-ba60-d400ff42edf5 | -10.46127 | -68.38389 | 2024-10-01 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fafe8886-175a-3bbd-a158-16bb2b822808 | -10.44873 | -67.89003 | 2024-10-01 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d17e8754-4e28-33d0-9336-abf18255b219 | -10.44818 | -67.89368 | 2024-10-01 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b2f0eb1-9d98-3cea-88e9-0e1bace32aea | -10.42586 | -68.59203 | 2024-10-01 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68b396b7-ddcc-393f-b199-9d7c5f92b504 | -10.42345 | -68.58814 | 2024-10-01 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 496e8d92-be96-34b5-a857-be4247552bb5 | -10.42235 | -68.5952 | 2024-10-01 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af88a76a-89bf-3986-b522-430d4ef15164 | -10.41638 | -67.94431 | 2024-10-01 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2dbd4a23-4345-3f6b-a6a8-d30fed754cf1 | -10.41452 | -67.94398 | 2024-10-01 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c9a79443-03dc-35a8-b07c-938bf0e4b646 | -10.35078 | -68.0006 | 2024-10-01 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9ccb79e3-9df7-3e26-86e7-672fd6f2d8f0 | -10.32007 | -67.76305 | 2024-10-01 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2c08d10-2f77-351e-8db4-b26a49d76862 | -10.27398 | -68.76235 | 2024-10-01 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b46ba702-08fd-319a-afb6-5c36ce9bc565 | -10.27344 | -68.76586 | 2024-10-01 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab9d53c9-f550-3e47-87a8-c01b8e77b15e | -10.27067 | -68.76183 | 2024-10-01 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5b3ab37-c638-35d4-9dd8-db85f543ee1b | -10.27012 | -68.76533 | 2024-10-01 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5b0bbb7-4749-36aa-9881-dc0fc35b1c24 | -10.26736 | -68.7613 | 2024-10-01 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b37534ae-921d-3bb5-8850-d35d2112e2e1 | -10.13227 | -67.89724 | 2024-10-01 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6a58b10-6c16-32d2-a5f1-dc091592d604 | -10.12891 | -67.89671 | 2024-10-01 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47a1d236-f24f-343e-8cb0-22c4a459cbed | -10.12665 | -67.88896 | 2024-10-01 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c542c662-dafe-3f54-9036-2ed4079a17a6 | -10.12274 | -67.89204 | 2024-10-01 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e47f5dc-75d9-3ea5-ae87-2cbe64af8ae2 | -10.11937 | -67.89153 | 2024-10-01 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 308ad0f7-48b7-3063-b5f6-923fafa09fee | -10.97933 | -68.4613 | 2024-10-01 05:53:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fc53d840-8ca3-3b5e-8b70-49d94cc9fd4a | -10.90454 | -68.83362 | 2024-10-01 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c52572ae-9dd6-3cea-bc92-324efd989032 | -10.88777 | -69.09351 | 2024-10-01 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 539fa923-da3d-3eba-be67-cf31aa5dfc2f | -12.27013 | -62.31729 | 2024-10-01 05:53:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8447b495-28a9-374e-995b-4ed9cf16bcaf | -11.85362 | -62.74892 | 2024-10-01 05:53:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f88a6cd0-0fdc-39d4-bbfe-86ee9388a647 | -11.85301 | -62.75352 | 2024-10-01 05:53:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efb3f8e6-0fd9-3d84-bc13-c94121cb3e73 | -11.78438 | -62.66997 | 2024-10-01 05:53:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8ad0539e-e62f-370e-a72f-9434492c01c3 | -12.99692 | -62.71698 | 2024-10-01 05:53:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a7cd3e5d-bbcb-333e-b0de-8957be1c83dd | -12.99559 | -62.71876 | 2024-10-01 05:53:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9cc412ee-fb58-3c01-b214-0c97a4dcdb62 | -12.98563 | -62.69561 | 2024-10-01 05:53:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5a11160a-853a-3c16-bb55-5ba3168195b2 | -12.98498 | -62.70051 | 2024-10-01 05:53:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ec2bdf81-775d-31c6-9336-51935ebd8ef7 | -12.98414 | -62.69735 | 2024-10-01 05:53:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 41c2f0d8-c0eb-3ba9-80b3-3edae3817637 | -12.98369 | -62.71027 | 2024-10-01 05:53:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b0d2e15d-8741-38a5-b58b-7dc79b393b24 | -12.98353 | -62.70226 | 2024-10-01 05:53:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 893a3017-3a98-381d-8100-5646ba6877db | -12.98292 | -62.70714 | 2024-10-01 05:53:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 22bafc8e-d84d-3e77-8dc9-31a90885b485 | -12.98232 | -62.71201 | 2024-10-01 05:53:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bfc9523-aec0-3163-b3e5-53f27a8a9f5d | -12.981 | -62.695 | 2024-10-01 05:53:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| faf04e9b-2a82-31df-9a89-015c833924c6 | -12.98035 | -62.69989 | 2024-10-01 05:53:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 81f25f73-0fbc-37c8-ad8e-0a2d4f78d1e4 | -12.97971 | -62.70479 | 2024-10-01 05:53:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2783c331-aeda-34ad-8919-819bfe37d3c3 | -12.97906 | -62.70966 | 2024-10-01 05:53:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4ecf6fe8-86de-3f21-8e72-45e7186f5757 | -12.9168 | -62.68129 | 2024-10-01 05:53:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 7a5e4bda-8a38-399d-8023-143afc117b92 | -12.91617 | -62.68617 | 2024-10-01 05:53:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 58180088-f78e-335f-9dda-2bc1eb7c9889 | -12.91216 | -62.68066 | 2024-10-01 05:53:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5788bf0a-dd2c-33a8-ba80-86bc372406d4 | -12.91154 | -62.68555 | 2024-10-01 05:53:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8a2397d5-51c8-3abb-a0da-055b117cb52f | -12.91092 | -62.69044 | 2024-10-01 05:53:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 12e6b5d5-b9bb-3eca-8e76-c89caa97944c | -12.85862 | -62.84256 | 2024-10-01 05:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93237ee6-63c5-3a81-834a-22c96ede596a | -12.85858 | -62.84529 | 2024-10-01 05:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 650330b3-84cb-389b-8591-8f235745647c | -12.85799 | -62.8473 | 2024-10-01 05:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dbb05f32-ed90-3673-ab1f-e5dc78c80172 | -12.85798 | -62.85005 | 2024-10-01 05:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f436a376-39fd-3d05-8df0-944558a559ae | -12.85215 | -62.85619 | 2024-10-01 05:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c457e1f6-06be-313c-8048-2927b62a9768 | -12.84884 | -62.84607 | 2024-10-01 05:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0979d33-663b-34a0-bfc6-0d19ed595d5a | -12.84821 | -62.85081 | 2024-10-01 05:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f8a7dd1-36a7-3dd6-856a-ffb707100b79 | -12.84758 | -62.85557 | 2024-10-01 05:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a7b33d82-dad1-3a32-9456-2eb82783af9e | -12.84695 | -62.86032 | 2024-10-01 05:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f8539128-451e-3ab4-865c-142a43b8eda0 | -12.84364 | -62.8502 | 2024-10-01 05:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63a8ee7f-0adc-3f44-a720-d27a0e795b8e | -12.84301 | -62.85495 | 2024-10-01 05:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 09126956-469c-3e5e-8bbe-abccabfbafe7 | -12.83781 | -62.85909 | 2024-10-01 05:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bfa73ae6-40e0-3b09-babd-c9e5d964cde6 | -12.83718 | -62.86382 | 2024-10-01 05:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 33ed9a11-82d7-334d-a95a-1ea9bb5ad6be | -12.8268 | -62.87206 | 2024-10-01 05:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 53fbc7a8-5b80-3522-99c4-c3dc472b7383 | -12.82099 | -62.8809 | 2024-10-01 05:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README156.md)
