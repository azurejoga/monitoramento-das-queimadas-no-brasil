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
| 3ef1b67c-99be-3b56-b98a-62d399fde53b | -13.02514 | -46.91432 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9008b539-67be-3fa6-b462-895740847325 | -13.22331 | -46.94164 | 2026-09-20 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7ba3a8c-82e7-32e6-a5e7-e41bf92d06dc | -10.57496 | -46.53713 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56eb8ad2-612a-37c8-8744-d43c9a584177 | -10.26406 | -45.48135 | 2026-09-20 04:40:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 086056f8-a21d-335a-a3a9-350f6a9150ff | -10.57088 | -46.54055 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 36cadf8d-ed22-3060-866f-6dcb0d802952 | -5.84099 | -53.54909 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5aa06984-cfca-3dbf-a057-63aa0e46b8ca | -10.2649 | -50.26625 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 111cc5d3-df22-3d81-af4d-557de06ab8eb | -8.18389 | -54.76646 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1c9ca91-6e19-361d-ad76-89d850b9652c | -11.76882 | -47.46065 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dbfb3859-1a52-3662-847d-98bc6fc178d1 | -5.86151 | -52.03331 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0edb5c4d-4912-3959-b4de-ed70b2c01e43 | -11.00466 | -46.58646 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4c82e9a-a759-3b2c-a7b6-e53cf10c74ba | -9.01827 | -44.92083 | 2026-09-20 04:40:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ab6a312-f338-3870-8133-54ce7107f865 | -9.66656 | -54.32688 | 2026-09-20 04:40:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14f2703d-9053-33fe-9562-96b5d0ec2419 | -10.47753 | -46.29316 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9cfd893e-7da5-3ec3-b113-880d9ee53e8e | -8.13349 | -46.81143 | 2026-09-20 04:40:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7b8906d-28b6-3290-9ba1-17a3d53173e0 | -11.02848 | -48.28349 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60022a77-0494-3ffa-8790-c7c0e911b5d0 | -7.53358 | -45.87849 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cb992363-cbbe-3f53-bfd1-ca9980e32a9f | -9.26193 | -46.20622 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eb81bab8-dee7-3571-9737-bcd8f4a47fc2 | -11.15036 | -42.79575 | 2026-09-20 04:40:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7ce742e0-36e5-3d1e-ba4d-49b8485a599e | -11.79119 | -46.8298 | 2026-09-20 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f59d9e3d-1e72-3ba0-81df-5dbbcdf1a141 | -11.04199 | -54.1776 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5bba08f3-bc2b-3567-af03-c2569c1d6cfe | -11.02293 | -48.34079 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3d5b496e-d9dd-38ab-890c-34ef91470baa | -9.92885 | -60.72932 | 2026-09-20 04:40:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74f56b74-5ec5-3843-b5d3-1818b1460b8c | -9.68728 | -54.33038 | 2026-09-20 04:40:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 981b3832-90e1-3318-8d6d-bbf215880ea5 | -9.17362 | -51.51142 | 2026-09-20 04:40:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fad1cdbd-6bc3-351e-9955-7b2b0a67c0ae | -10.87852 | -54.08937 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ccd75b4-1db4-3a6b-b3fd-61480ccc7306 | -7.83776 | -50.24443 | 2026-09-20 04:40:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0da85b8-d962-3cb8-b65f-fbf55f387e00 | -8.73247 | -52.36306 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 687a2469-9988-3d22-a098-15c888b3f9fa | -12.74256 | -46.18952 | 2026-09-20 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0efdb9b0-ba0f-3182-bc4a-eec9e0fdfed4 | -10.36875 | -50.45419 | 2026-09-20 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b55ace20-e69c-3367-98c9-b99b4d5150f5 | -8.24883 | -50.67302 | 2026-09-20 04:40:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 527cf686-7306-3ec2-a6d9-6344f1b8fce5 | -13.64743 | -46.95346 | 2026-09-20 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3d6bbdba-6a33-331b-99be-00e444325bb2 | -8.16715 | -54.75916 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ed99b4c7-f718-3b7d-8bb7-e57bda5712dc | -12.12073 | -47.02459 | 2026-09-20 04:40:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f61f2916-ea0c-3e72-928e-5e4a97e06155 | -9.01263 | -44.9841 | 2026-09-20 04:40:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e017dff2-8bf2-3e2a-b9a2-2c54ae46bb8d | -6.99283 | -45.68027 | 2026-09-20 04:40:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d54fd58b-aba4-3fcb-bd5b-2215e5453a57 | -7.51675 | -46.24366 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03733645-3ee7-3ccb-af59-48272a6823ed | -7.56604 | -45.40521 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1fa681c7-9347-3278-9ed7-1e14a6469925 | -11.20698 | -54.0763 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5cd15a1e-f3bf-3262-b9c3-26330eede153 | -9.83353 | -46.44495 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 85bd4a84-ccaf-363a-98bc-02d0e8cdd9c9 | -8.47758 | -45.09161 | 2026-09-20 04:40:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea256caf-6517-36c9-8951-44ca98b563af | -8.75521 | -48.66026 | 2026-09-20 04:40:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 523db580-8d5c-3a43-9168-3c3fc36e9c8a | -12.38279 | -47.0073 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 22439efc-862a-3e37-a9ef-f62fe9d96b74 | -10.40843 | -48.92299 | 2026-09-20 04:40:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe0a03d4-17b0-31c9-bba7-c6eb4afb7afa | -11.09218 | -48.28625 | 2026-09-20 04:40:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69bcdd6e-3c1a-3b92-9127-18b96cb718fd | -8.76182 | -48.66132 | 2026-09-20 04:40:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 73bd8825-29a3-3ade-a762-87ef37ffdeab | -8.76679 | -48.67281 | 2026-09-20 04:40:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 4585d40d-3c0d-3433-948b-b40eb0586911 | -10.41009 | -48.93401 | 2026-09-20 04:40:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a557ccb5-17e6-38fc-aeab-cc6b3c1b15a3 | -5.84583 | -53.54595 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b89d7c3-96b4-3e80-8fd7-2e3f312f72a7 | -9.12545 | -45.72422 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 336ba3aa-1fd5-319d-a987-492dd00b094c | -11.86567 | -47.67332 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d0268aa9-4b40-3e31-836a-894c8fce5fbd | -9.57539 | -55.10516 | 2026-09-20 04:40:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0574e4f3-407c-3d7f-93e8-7cf0082459cb | -7.45232 | -44.73249 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5ee149b6-16cc-317c-af1a-6082e80506f0 | -12.59232 | -49.13572 | 2026-09-20 04:40:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e57d4b6-e767-33b9-9992-de10a6ee7b44 | -11.4863 | -47.79905 | 2026-09-20 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8fa8979c-db6b-3ab8-bcf9-6db126e28cd4 | -11.08939 | -48.30419 | 2026-09-20 04:40:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c3162778-00ce-3302-8651-a94213b51a2b | -10.27733 | -50.25346 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| b7f64b31-0160-3e79-ac19-eef968301143 | -8.17299 | -54.75146 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4610ecbf-c05a-35c3-bad6-804af41cb298 | -9.83756 | -46.44183 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b0082b91-be6b-33c1-a5bf-3a1ed98ae738 | -12.01848 | -51.47353 | 2026-09-20 04:40:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b00a5b83-4817-3ee0-a8e6-6a11050c0194 | -9.35345 | -50.11701 | 2026-09-20 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2459a352-4bfc-3f37-b927-908687b1b636 | -11.00903 | -48.32056 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e2d45adc-a56c-393b-8e62-00fc04443aa4 | -8.79904 | -60.79725 | 2026-09-20 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1d0e91ca-e892-3458-9c90-dc6f0c969e42 | -7.76543 | -49.19895 | 2026-09-20 04:40:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 18b8f5d6-9ec9-3e54-80bf-74c112bcd8c9 | -13.23272 | -46.92662 | 2026-09-20 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd578012-95a3-394f-bb68-1cb109521fbf | -11.10656 | -54.02939 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0246fdc8-d8f7-3e33-b77c-cc1198078f62 | -12.75812 | -46.13441 | 2026-09-20 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee06d221-5972-3954-9676-2004728d5dcf | -7.58943 | -46.97637 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 97c95dd9-d536-3c11-a931-d93d26db3b48 | -9.83529 | -46.4332 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c109c83b-9175-30cf-8597-68f44690c045 | -9.9311 | -60.73319 | 2026-09-20 04:40:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4030e02d-5302-3713-8b92-d2c737581980 | -11.99287 | -50.02181 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13c72630-cd98-3870-b32e-8aed56007a7d | -12.53655 | -50.04236 | 2026-09-20 04:40:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 88868a2b-d0d5-38b0-80ed-566f8e9fff21 | -9.14726 | -49.98388 | 2026-09-20 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbb80945-2b08-3ed6-a3ad-17bc7cbcafa5 | -7.16643 | -47.44792 | 2026-09-20 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 422432c4-acda-3e83-8a2f-a0574923b1fd | -8.76403 | -48.6688 | 2026-09-20 04:40:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 3afd0339-3586-3a3d-b54a-51c63d5bd582 | -14.18329 | -47.8723 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 230e5915-27aa-3106-a892-14d07f6465fc | -12.74683 | -46.18573 | 2026-09-20 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d636d757-67ad-32be-b67f-eef57f210c12 | -12.33043 | -50.70734 | 2026-09-20 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 854598b4-dbcd-3f71-8e46-13fdefac892f | -10.88664 | -47.84361 | 2026-09-20 04:40:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54350979-3764-3f60-aef4-95782da3b5b8 | -9.72818 | -48.15348 | 2026-09-20 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a77daef-eae6-375d-b094-dc21818ed0ad | -9.65481 | -54.32082 | 2026-09-20 04:40:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fdf99ae-d73c-3b14-a318-384b8b4a15c3 | -11.99677 | -50.01882 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3eccf4c1-4e74-30ec-8e49-13c11b37775c | -11.01513 | -48.32517 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a014c223-45e9-328b-be2b-233f7fabc916 | -8.38191 | -47.19045 | 2026-09-20 04:40:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bfc0f77d-228a-3de9-b82a-2b92aab8e03d | -7.63008 | -46.1211 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 977ff89d-eff0-3c80-b720-9eb42ac39f7b | -10.31967 | -50.21573 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 544a1ea7-0345-369e-956e-c8dd4c89880a | -12.31283 | -50.73052 | 2026-09-20 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| be67ed4a-24aa-39e9-b038-b5b907a48ed0 | -8.49856 | -47.43923 | 2026-09-20 04:40:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a180a3e-3cdd-370c-a358-58380f470ae3 | -9.76724 | -46.04282 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9d4cd8b-6dd7-3d51-bd8e-5ef4900f0924 | -11.71902 | -54.56433 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2174d2d2-d201-3ea1-9cda-d18d0333a310 | -12.76303 | -46.12636 | 2026-09-20 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 986ebd34-2463-3597-a22c-e7b723a42247 | -9.8071 | -48.32073 | 2026-09-20 04:40:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82fca1e6-4d39-32cd-a3a2-d8325bef75e6 | -11.87361 | -50.00184 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27dd5477-fff8-3152-83e7-29afdab82fed | -7.75334 | -46.70858 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| aadfed82-ebe2-3140-9a92-e476b8f1aca7 | -9.22218 | -43.18064 | 2026-09-20 04:40:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8b0ca945-2756-302b-9b95-d93f7e7010f6 | -8.42835 | -45.86433 | 2026-09-20 04:40:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be2f3e9f-0fcf-3026-b966-ff3dc3104006 | -10.87576 | -54.08165 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fc6d204a-b3ba-36b2-9e92-6d23fe1ed2a5 | -7.29975 | -46.74369 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c6a22f3-d58a-37c4-a57e-6b111a4b9d9d | -12.74792 | -46.20353 | 2026-09-20 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8ea914f9-a2f8-3a4c-9812-60a3e7a05f66 | -5.85773 | -53.55184 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README80.md)
