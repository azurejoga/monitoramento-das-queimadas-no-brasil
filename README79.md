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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ec32f21-87f9-3b08-8621-9cc6eeb9acb4 | -10.47516 | -53.6454 | 2025-09-06 05:29:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 195fa455-69d0-3bd0-b8b8-980cf7da5cfe | -8.35782 | -52.55629 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d082e951-4154-33d3-9074-1ea3b10ea5e6 | -7.38651 | -56.69091 | 2025-09-06 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3ad2eab-2687-32e3-8f36-17f3af8f6561 | -7.72145 | -61.51815 | 2025-09-06 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e47c7738-e5a7-3da1-bc35-1e889d58229b | -5.90443 | -57.73433 | 2025-09-06 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ed59bf4c-8b5a-3015-a548-44f432f95ba5 | -5.90905 | -57.72987 | 2025-09-06 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ee0e822-68e1-38b9-ba68-83afe4d70a90 | -9.21353 | -57.08865 | 2025-09-06 05:29:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d362125-c226-31c7-822b-79a75ae61141 | -7.7638 | -50.74461 | 2025-09-06 05:29:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 032985d5-3694-3ea9-84b6-58acf44a9da1 | -6.87005 | -58.93235 | 2025-09-06 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 55c28ece-48ab-3dbc-8ca6-abc156d50469 | -6.84482 | -52.80471 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 92a34367-a487-3f26-a70a-ee58e6ab574d | -6.83934 | -52.8039 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e4eb2856-d560-3432-a165-ce5ea4b432fc | -10.22703 | -50.52549 | 2025-09-06 05:29:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 185b5b56-47c2-3094-b20e-08dfc26848a1 | -9.97566 | -51.65583 | 2025-09-06 05:29:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e040d26a-3587-36f5-9981-baceff5f5baf | -6.53763 | -49.50367 | 2025-09-06 05:29:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a4dbeb1-6db5-3698-b5ce-139696e1a5a4 | -10.14436 | -55.15741 | 2025-09-06 05:29:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 163bf855-2298-3a3d-9bee-9e5631735063 | -9.56126 | -53.58985 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84e1887c-96c9-3efe-b8cc-c2869c89dbbd | -5.94899 | -53.79428 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| edaaa401-ffb0-3120-b2ac-bd4d18c8f5ce | -6.17326 | -53.50525 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f275d2d-4244-3198-b56c-9862d6062400 | -7.7671 | -50.74154 | 2025-09-06 05:29:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e03b5b8a-4039-3cbf-82b3-484f69659dcb | -9.21834 | -57.08522 | 2025-09-06 05:29:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46b8d158-1665-3b62-918c-ba80d5769774 | -7.67707 | -50.29637 | 2025-09-06 05:29:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| db3a8fcd-772f-38b2-aae1-8219170928da | -6.54434 | -49.50475 | 2025-09-06 05:29:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4ec89789-5edd-32ca-802c-84ca77e0a88e | -6.44549 | -58.10192 | 2025-09-06 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 042dc43c-8a0d-3e67-821e-87e50a95f51f | -5.50631 | -60.13439 | 2025-09-06 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b18247a4-e8e1-3ae9-8172-e5414777b683 | -5.76841 | -56.5178 | 2025-09-06 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 877860ce-4c38-3747-8025-cd3da9b89288 | -6.84088 | -52.84047 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8a0f463-f6ec-3269-9280-15eee733c04a | -8.371 | -52.56254 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cdc7be87-017d-3dab-ab99-65958ecbbbd5 | -6.73575 | -51.96312 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f03886c5-0bc5-392f-a801-bf5a8c07ad2c | -5.97804 | -53.59112 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d12da6f3-8185-3b33-9eb4-03e6220feb51 | -9.68278 | -51.09038 | 2025-09-06 05:29:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8cf7a162-fad6-345a-81c5-7fbc032a075a | -5.5103 | -60.1312 | 2025-09-06 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05b5f984-d2b8-3013-bc32-23da5d838648 | -9.11942 | -61.48804 | 2025-09-06 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2073a50b-3824-3700-8e9f-401d696c0f61 | -6.44314 | -58.14485 | 2025-09-06 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3fc68bb2-c0e9-31bd-9650-7ed224e78627 | -8.70519 | -62.38971 | 2025-09-06 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4261ef31-99d8-3033-8aae-ed4c34e398a2 | -9.39628 | -54.75185 | 2025-09-06 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f482541a-70ca-3507-8fe4-c49d5caf91c8 | -5.95828 | -53.80165 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0fdb4b3-2672-3700-a5a4-3fc4aa145a01 | -5.09944 | -56.1239 | 2025-09-06 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 775be4ad-370e-3553-b15b-38ea368efbdf | -5.10682 | -56.13313 | 2025-09-06 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ced48c08-171b-3704-82c9-621eaf6b985c | -6.27323 | -53.44262 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb933af3-a6e3-3060-9d87-a0357b107133 | -9.7107 | -49.49093 | 2025-09-06 05:29:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 1a9eb221-a8b5-3d61-a837-800b95aae2d8 | -5.53546 | -57.24689 | 2025-09-06 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b5be5e1-f86e-38e1-b1fa-f63d3ed2031d | -5.10567 | -56.14109 | 2025-09-06 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7dff5e58-d5bf-3ad8-9485-34c70b76340c | -5.10936 | -56.14568 | 2025-09-06 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 214bfe41-a10c-3621-a50e-b671dacffd24 | -5.72716 | -49.28704 | 2025-09-06 05:29:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 28aebe06-35c9-34f3-8c58-678418222c2e | -4.89772 | -55.99343 | 2025-09-06 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb40bed0-acd8-393e-9240-e8015e12ecbb | -5.9307 | -51.99929 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2844cea8-329b-38c0-aa15-3b93da9af1ab | -8.76411 | -62.40602 | 2025-09-06 05:29:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8908459e-03c0-3a46-a81b-4821457262a9 | -10.22633 | -50.53134 | 2025-09-06 05:29:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a2acb941-1ab4-3183-bae5-e5347b683c7b | -6.28323 | -53.44724 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dfe1284f-f9e3-38e9-993e-2526a5e14abe | -5.48978 | -60.12806 | 2025-09-06 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42c48fb6-2fa6-37f6-b7bf-1be631b7fe82 | -5.98233 | -53.59778 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f57f1d63-6589-3479-bfd4-a31cba475e9b | -9.39703 | -54.74604 | 2025-09-06 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 715b8689-2fde-3b1d-8b68-dd0fb26fe5f9 | -9.68019 | -51.11173 | 2025-09-06 05:29:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d103e2a3-729f-39fc-9950-fa5d2cad9a45 | -7.7331 | -50.3227 | 2025-09-06 05:29:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f8e30d52-c76c-3ff9-9146-dfdc5b1b6c11 | -6.27412 | -53.4362 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9bf562f-6c7e-3810-8ce9-1a17f1bc91b5 | -6.68726 | -63.13194 | 2025-09-06 05:29:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56ca28d0-ce32-30d1-a931-b6cf22196ef1 | -6.19775 | -53.25244 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a115c7d1-fd89-33b7-ab6f-75019f3d4781 | -6.27889 | -53.4402 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 21e73e46-8c92-3b6d-b6cf-80974e062d0b | -8.35257 | -52.5521 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 240d728b-8be8-3779-aca5-8bf725b10a1c | -9.97426 | -51.6649 | 2025-09-06 05:29:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b226aff8-b753-327d-aaf2-1f182b0f39f1 | -5.93013 | -52.00345 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a3f03a7-2d48-381e-8c24-c38727e774c3 | -6.27023 | -53.42583 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b5f7981-4caa-3d25-b29f-7c04c7c6aa36 | -6.87679 | -52.78051 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 431c06f5-7933-31de-aea5-fd5b3efde0ef | -6.81587 | -52.81182 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 885847c8-febb-379c-9f0f-ec5203ecd525 | -6.82232 | -52.80562 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cfd6c016-52e0-3c6a-ae1b-e4698abfba47 | -6.19249 | -53.25159 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 148686cb-6c1d-33bf-b55f-0b145ddc18a4 | -6.19866 | -53.24585 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 92e81f86-fb6b-31cb-967b-7aa627e26e32 | -7.79167 | -52.13289 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 631ee452-f449-3643-beae-7c23b400bddf | -5.1051 | -56.14506 | 2025-09-06 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| deb0336a-2153-381d-b9e1-14b0e514eb97 | -5.94771 | -53.80325 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ff8872a-3193-3321-9e84-1195dfd442bc | -7.75994 | -50.74723 | 2025-09-06 05:29:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 0730a86c-601d-32ae-a04d-80a954f58d03 | -6.18539 | -53.26402 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a91a3b2-89e5-3080-9b71-51ebd36ba5ba | -8.37502 | -52.55784 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9ab3cceb-3938-3aed-baf8-a7ea740cf61d | -5.90979 | -57.72493 | 2025-09-06 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 310a0dbd-6438-3c81-aeb1-2d403e1a5827 | -6.3482 | -53.44593 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd6971fe-b746-397d-9c52-cef0bf1be742 | -6.27192 | -53.45213 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6fec7db-e665-3e34-9f33-9ed610d993f0 | -7.68281 | -50.30324 | 2025-09-06 05:29:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 3aead607-ebd8-3e3e-aa33-df028bac5e2a | -6.1982 | -53.24916 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 959ceebe-9be3-3aa4-a26c-b169cfc864af | -5.97676 | -53.60006 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1dbf79d1-b3c5-3d97-b9e1-cc9adc32204f | -6.63354 | -53.16105 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7771b4b4-15b3-3b0c-ba63-792fe0b15791 | -7.73249 | -50.32756 | 2025-09-06 05:29:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d168af04-6803-3bfa-bfc4-e4d6505dca32 | -7.73372 | -50.31783 | 2025-09-06 05:29:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c2dc0f1b-fea8-3aaf-a2b8-0bd960ffb0f7 | -8.37145 | -52.55896 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 954ccb7b-d958-3515-972c-8db5c9a141a2 | -6.27545 | -53.42659 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| deaaf494-c9fa-3cbf-9814-e4bb14bd8322 | -10.47693 | -53.64062 | 2025-09-06 05:29:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ea26ee4-79a7-3975-8247-0111040a8712 | -5.79037 | -57.55831 | 2025-09-06 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c34e2181-c956-3f08-9232-d7baa5339e05 | -5.10993 | -56.14171 | 2025-09-06 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ebdb79e-21e7-3254-b36b-06dd1e83f45e | -6.43934 | -58.14427 | 2025-09-06 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d792b9e6-1b25-39ac-900c-c2952ca5d3cd | -9.70993 | -49.49772 | 2025-09-06 05:29:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| e6a4f2ba-aaeb-38cb-9686-0f7d10616327 | -6.4403 | -58.11078 | 2025-09-06 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e2a4df91-4764-3641-bcbb-8269672a54bd | -5.78792 | -57.54774 | 2025-09-06 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55f9a343-ce34-34f0-9d86-6c936927bbc2 | -5.50973 | -60.13491 | 2025-09-06 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 791faa1f-8151-355a-badb-b387389cbd56 | -5.4932 | -60.12858 | 2025-09-06 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91cb2647-b4cd-3ecd-abd2-9a2d4b7e73d9 | -5.94942 | -53.7913 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7115b3fc-02f2-3c28-9df9-373c9d147599 | -5.50688 | -60.13068 | 2025-09-06 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d37cee5-2b05-397c-9993-64f0b3edc1cb | -6.634 | -53.1577 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 751bc2ca-92a9-3b41-b05b-f2e69c9dad51 | -6.28544 | -53.4313 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f95f61ca-1c22-39ab-895b-3e0184e52a27 | -5.95278 | -53.80395 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee22eee6-c9ec-375e-a462-ecb4bf1dc969 | -5.10624 | -56.13712 | 2025-09-06 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82bc7bcb-fc89-3a80-909e-014d931f2cfb | -5.09628 | -56.14865 | 2025-09-06 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README80.md)
