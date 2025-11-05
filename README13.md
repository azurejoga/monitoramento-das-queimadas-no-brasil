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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 437e740d-4bb4-3375-8453-c5c580ac4324 | -2.61891 | -49.2296 | 2025-11-05 03:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bf9c079b-3d16-3bc1-8a7f-1df132e4216c | -7.72936 | -45.81574 | 2025-11-05 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a69003fa-fa20-30d8-a395-161dc5569b5e | -4.17624 | -40.9818 | 2025-11-05 03:51:00 | NPP-375D | CARNAUBAL | CEARÁ | Brasil | 2303402 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7e3f7165-4f4a-30b7-932f-e8d065c6dd30 | -3.66613 | -44.79829 | 2025-11-05 03:51:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87d65a4c-8fb5-383b-a38e-37f16cda88bc | -5.92187 | -41.29253 | 2025-11-05 03:51:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 90c034d2-13cb-357f-8aa3-49a7071a7536 | -5.02998 | -44.79158 | 2025-11-05 03:51:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86fd1bd0-ffbb-308c-a16e-68a812f8f8bb | -7.33264 | -38.85092 | 2025-11-05 03:51:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 0df96b7f-9f0c-372b-8a6c-12b3d6d42bb1 | -5.10965 | -46.22111 | 2025-11-05 03:51:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74e398d1-763f-36bb-a534-61317b61afc6 | -3.82196 | -48.66924 | 2025-11-05 03:51:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67228f86-518d-3bd9-aaf5-61eb9e7b915c | -6.12029 | -41.63244 | 2025-11-05 03:51:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a293f0d9-355e-37dd-b6eb-21d5b3f5c5d1 | -4.51251 | -45.43279 | 2025-11-05 03:51:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1deb8a92-a861-32d4-987a-57c42abe7210 | -5.51196 | -38.5765 | 2025-11-05 03:51:00 | NPP-375D | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2cc3bad3-63fb-3d6a-a042-84053b457f63 | -4.8941 | -46.85215 | 2025-11-05 03:51:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 12ca8dfb-604f-3381-888a-c59ed49a7db4 | -4.45434 | -43.21387 | 2025-11-05 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9a648c61-a52d-3c2e-b531-0ccdd76a4168 | -6.94968 | -41.13998 | 2025-11-05 03:51:00 | NPP-375D | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ae11b419-5c72-319b-a29f-4a96011e67e8 | -3.88391 | -42.5264 | 2025-11-05 03:51:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 02376996-2a6a-360e-9efc-316ac6e42561 | -4.97306 | -42.86424 | 2025-11-05 03:51:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eac6fa38-9c7f-33e4-adea-7c28a5ab355c | -5.03403 | -43.62329 | 2025-11-05 03:51:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7187fc86-b5df-3622-ab33-990b74f185ad | -5.55344 | -40.75845 | 2025-11-05 03:51:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6b037bd3-9cad-34f0-8124-9c8b42984a71 | -5.63339 | -41.12437 | 2025-11-05 03:51:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d06120c7-2653-3fc7-8a52-3a5ed42c038f | -5.51791 | -41.1438 | 2025-11-05 03:51:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| cc162e05-7d0a-30a6-8fc3-f84ace128f2b | -3.4897 | -43.61754 | 2025-11-05 03:51:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2d33f750-af14-362a-adf9-5a04b6b52854 | -6.27308 | -42.56512 | 2025-11-05 03:51:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0f8ac713-3c92-34f3-96cd-d1e39020e7a8 | -4.92321 | -46.72243 | 2025-11-05 03:51:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 785584e2-fdff-38b6-adff-19aadc6db157 | -4.40873 | -48.9735 | 2025-11-05 03:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f75ff7e5-f7f9-3090-922c-45480926829d | -7.46001 | -46.94827 | 2025-11-05 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b652324f-7681-3bc9-ab06-eec268ed455f | -5.9283 | -41.37683 | 2025-11-05 03:51:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 864d56e1-d809-3479-a87b-f86307fff625 | -5.23621 | -48.50658 | 2025-11-05 03:51:00 | NPP-375D | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 041ae551-0e87-3fe6-b3bc-516038ec3f80 | -7.16528 | -39.15717 | 2025-11-05 03:51:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1e20fed6-689a-3c38-b6e6-0ad62daaa5b0 | -3.47843 | -43.62623 | 2025-11-05 03:51:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b8051d83-315b-3ebe-81d7-c0a3d8bd92d1 | -6.07103 | -43.25514 | 2025-11-05 03:51:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.9 |
| a17752ff-a3d7-35a3-bf4d-330bf024af78 | -4.71695 | -46.43672 | 2025-11-05 03:51:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6deba55-da85-3cb3-99dd-5646b941e107 | -2.82479 | -45.15142 | 2025-11-05 03:51:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 96b6d988-be57-3189-a609-6df84db5d993 | -3.84812 | -49.90571 | 2025-11-05 03:51:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 141a8a0b-0729-3185-a192-ee0664b4618d | -4.91744 | -46.72146 | 2025-11-05 03:51:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4983c19-2e0f-3e2b-8c10-b44c2f3f6d93 | -4.45813 | -43.21928 | 2025-11-05 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 268d3a0a-9440-3934-997c-293fac9da46c | -4.60804 | -42.8498 | 2025-11-05 03:51:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 041c0620-f423-38ef-92cc-74da1ea4a0e8 | -2.26879 | -47.85713 | 2025-11-05 03:51:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98b0e06d-ecdc-3d0b-9cc5-ddc04c0ab46b | -3.48718 | -43.63291 | 2025-11-05 03:51:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 45d95e81-2787-3889-8af6-b6febae6b915 | -2.42136 | -49.30408 | 2025-11-05 03:51:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 729433d7-98c5-3fe3-9c1b-c9b186ced165 | -6.07702 | -43.24708 | 2025-11-05 03:51:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 8251af1e-5938-3a6d-a250-a3b19fb8c65c | -6.85329 | -46.29306 | 2025-11-05 03:51:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3f1215d5-bb22-3351-a967-5d9a6234e400 | -3.41443 | -44.44188 | 2025-11-05 03:51:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 65e2d75a-5f71-3cdf-a8cb-3fb16c417ffe | -4.46492 | -43.23477 | 2025-11-05 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b1e19d93-449f-305d-9345-fd4b88898994 | -5.46931 | -43.58428 | 2025-11-05 03:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| d89dc2cf-96a4-3ac6-93a5-c68623fc603e | -9.78037 | -43.61726 | 2025-11-05 03:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 25536495-6b06-3d88-b204-3cb3fb770a06 | -6.13343 | -41.65219 | 2025-11-05 03:51:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1c6ec06b-3553-3507-89cf-99ffe4486263 | -6.5899 | -35.25181 | 2025-11-05 03:51:00 | NPP-375D | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f2d469c0-12d8-3436-b69f-96a7ad642943 | -7.28793 | -45.44961 | 2025-11-05 03:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8fa643d8-4fd8-3cf8-b3cf-93e6aed69e39 | -4.11521 | -43.8786 | 2025-11-05 03:51:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0053545-05c2-3adc-abb3-3d801c97cb73 | -5.47474 | -43.58034 | 2025-11-05 03:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| d31fabe3-fe42-304d-862a-0711c377f06a | -4.30495 | -45.37346 | 2025-11-05 03:51:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d883081-d5d9-3211-b41c-1edb326c04bf | -3.65526 | -44.79964 | 2025-11-05 03:51:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 476d1341-302a-3d7b-86cf-84b5247aff2e | -2.84282 | -49.41028 | 2025-11-05 03:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3ebaaa82-414d-365e-a3ce-c098dbc085f7 | -6.13403 | -41.64865 | 2025-11-05 03:51:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0f133165-20e3-371a-b8f0-cfe2c9bc8ee3 | -5.49165 | -42.17109 | 2025-11-05 03:51:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f77fdafc-4e24-30b0-a359-b26e312450bf | -5.36078 | -44.73845 | 2025-11-05 03:51:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 46fc5a18-0c69-3ee3-88de-953e84b90280 | -4.28628 | -47.18025 | 2025-11-05 03:51:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7c42a50-c138-3897-9247-d06d6d1912aa | -8.96916 | -44.1075 | 2025-11-05 03:51:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0f05c9a1-5561-38d4-abea-25eaf60b83fb | -6.0986 | -41.70749 | 2025-11-05 03:51:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ee025da0-f7e1-3752-8a48-86e9da24de8c | -7.54655 | -45.84818 | 2025-11-05 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9a1057cc-b742-3de8-8bf9-89aa7f0b2229 | -5.03339 | -44.79093 | 2025-11-05 03:51:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba089afc-69f6-3acc-ad57-96de6f9b1239 | -5.51235 | -41.15313 | 2025-11-05 03:51:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 1c5b90a8-8082-3fbf-806c-2740d63cbdfb | -9.62713 | -45.22594 | 2025-11-05 03:51:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9011f07-86e8-3186-ad98-9cb462f844b0 | -5.92913 | -41.37179 | 2025-11-05 03:51:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f00917e2-e655-3a29-8a26-aa0c055aeb33 | -4.47487 | -43.23167 | 2025-11-05 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 8af10738-ca16-3700-b6e5-9beb65bcffba | -9.84709 | -40.26711 | 2025-11-05 03:51:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d9dc5997-01f4-30e1-912f-deb41e4d9fe8 | -6.06447 | -47.3 | 2025-11-05 03:51:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b7a1d810-8d46-3eb2-a308-f78580592c13 | -4.18592 | -46.41181 | 2025-11-05 03:51:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0f5b8ad-3936-3177-afc0-fcf09a5ba288 | -6.85266 | -46.29652 | 2025-11-05 03:51:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 073bcc6e-6879-336b-ab3b-da727151cb74 | -4.54242 | -40.64276 | 2025-11-05 03:51:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 0b2fb3a5-3c25-3747-b2c8-7a45307c3362 | -4.76119 | -42.65614 | 2025-11-05 03:51:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 34.4 |
| c06b9153-4b5c-3c80-9112-def3beafa2d3 | -3.96985 | -43.78692 | 2025-11-05 03:51:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5efea447-0c09-3b18-b008-cf96c7f3892f | -7.78829 | -42.221 | 2025-11-05 03:51:00 | NPP-375D | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 74ab4a2a-865c-3cbc-9c61-4c60509b1531 | -4.61745 | -45.35466 | 2025-11-05 03:51:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e9f08416-cae4-3558-b63f-a652bbdaabe5 | -6.08238 | -41.78111 | 2025-11-05 03:51:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 940001f9-642b-3c1c-9982-4b22c2f63da9 | -9.77677 | -43.61239 | 2025-11-05 03:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f38ef32e-d7fe-3834-b81c-0522f5326e29 | -5.11023 | -46.21775 | 2025-11-05 03:51:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66aa0361-7150-358a-92c8-eb2f94839a61 | -7.29302 | -45.45045 | 2025-11-05 03:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01c98352-8f16-3dec-880f-a0e0f78b79fa | -2.83332 | -49.41199 | 2025-11-05 03:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b71dbc89-65c2-3065-b7e8-a25a56d851d9 | -2.72522 | -47.39427 | 2025-11-05 03:51:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d5eaa2d-1322-317f-af77-a8dbe0f06485 | -4.67263 | -46.30654 | 2025-11-05 03:51:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c168ffa8-c008-3303-a8cd-f682483269ff | -7.07171 | -41.58159 | 2025-11-05 03:51:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5dd73b29-68ea-3ad1-873a-d93315165076 | -5.99237 | -42.95594 | 2025-11-05 03:51:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| ae92de6d-59fd-3672-8169-6964512b2b08 | -8.858 | -49.88655 | 2025-11-05 03:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| efb68e7b-7796-372f-97f3-4184d9fc4981 | -5.03017 | -43.61763 | 2025-11-05 03:51:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 479d6859-e3b9-3c7a-8c75-5af23f6364b7 | -5.06418 | -44.73358 | 2025-11-05 03:51:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 736c396c-e46e-3923-9384-01138fd9271a | -7.32922 | -38.85037 | 2025-11-05 03:51:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 1b0fecd2-326f-31c2-afea-07f590015a07 | -7.52543 | -47.14892 | 2025-11-05 03:51:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6d43bad-c06a-3eec-b5f0-795698bed32a | -3.22629 | -44.40524 | 2025-11-05 03:51:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e040390-2dc0-3096-a1b5-563360fcd4c5 | -6.68643 | -34.96463 | 2025-11-05 03:51:00 | NPP-375D | BAÍA DA TRAIÇÃO | PARAÍBA | Brasil | 2501401 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7f4f3b61-e288-34e9-b731-dc5670cb3e11 | -6.73753 | -44.1516 | 2025-11-05 03:51:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 85d8734a-f453-363e-8d8c-bc8d37fee2bf | -4.91711 | -46.72332 | 2025-11-05 03:51:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1ceab9d-297d-398e-a99b-4c4d3f61a384 | -4.46571 | -43.23011 | 2025-11-05 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eae4a64b-8ccd-36ae-bbde-c863b07f69f7 | -5.76643 | -40.75522 | 2025-11-05 03:51:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2e555c76-be6f-37e2-9180-9016ae8417bd | -8.79911 | -40.4364 | 2025-11-05 03:51:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b57b7b48-1c67-3351-ad07-c3f75a010a05 | -3.70549 | -45.88935 | 2025-11-05 03:51:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b24f051a-0065-3c21-b79f-40ce69cdcf7e | -4.61871 | -45.35441 | 2025-11-05 03:51:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 815197e7-5c97-3efb-8bb8-28b2986570c9 | -6.7084 | -40.83259 | 2025-11-05 03:51:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 375e0356-c9c6-3695-b4ad-01519bc5cae1 | -6.65822 | -42.66134 | 2025-11-05 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |


[Clique aqui para ver as próximas entradas](README14.md)
