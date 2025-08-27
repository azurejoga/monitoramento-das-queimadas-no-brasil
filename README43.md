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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27c42006-f5d5-3fe8-9b77-fe667ef43267 | -5.75912 | -53.77663 | 2025-08-27 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b6eddff-6ca7-3be3-9cd3-d839ecd908cc | -9.09728 | -49.57907 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c94d9666-e16a-3611-8cc6-6e4fabeef2ef | -9.59089 | -55.37078 | 2025-08-27 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b078ddf7-7f70-37bd-aac8-cf26b8dc5c62 | -11.58519 | -46.39084 | 2025-08-27 04:25:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cdd87ecf-e22b-3ef8-90ca-2fc8646bbafb | -7.43293 | -57.62859 | 2025-08-27 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0137703-5ced-3ee3-9b5c-1b4f3f9c4913 | -6.83675 | -58.97157 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 05897f08-cb7d-3e6d-9b42-a00e0a9e4013 | -9.47396 | -57.82605 | 2025-08-27 04:25:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3037311-e89d-3f3f-9cbd-7b2ba0b7549a | -6.31978 | -43.61075 | 2025-08-27 04:25:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50886306-6f7a-355e-a818-b265490f259d | -10.6629 | -47.17205 | 2025-08-27 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6620d94b-1123-3a8e-91db-6cbc898951e8 | -10.31966 | -46.7838 | 2025-08-27 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24171a82-d88b-39af-a26c-893e380add03 | -8.86661 | -47.16908 | 2025-08-27 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d31de188-51a8-3be4-a4a4-d227b9a1372a | -5.75643 | -53.76205 | 2025-08-27 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca30589c-e8b0-3588-9b4f-8566eae52d99 | -6.12657 | -42.95094 | 2025-08-27 04:25:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 3035e908-b4f4-392f-bd87-87cca6b4a429 | -6.51221 | -42.96934 | 2025-08-27 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3da2ab7-12f1-3211-9147-0e2193528790 | -5.76085 | -43.38796 | 2025-08-27 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0d6bf8b-7b6e-31c1-9bc4-9404313a32c2 | -9.10145 | -49.57568 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ebb26517-fd14-3b4b-9010-95ce36b5ec25 | -9.09222 | -49.56603 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 685d5b08-900c-39e6-867a-033b8af21ae1 | -9.0764 | -49.57259 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f0ac050-bc2a-3536-82ab-0cab5a10a43e | -10.66731 | -47.16558 | 2025-08-27 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eec60316-6912-3a04-a3e1-b031e60488cb | -6.95471 | -44.09418 | 2025-08-27 04:25:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d6e31f39-936c-3bea-8411-caf6d8bc18ec | -5.62309 | -45.72427 | 2025-08-27 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0fde5494-ea6a-3e48-a588-c3e5d3f2007d | -9.10299 | -49.58817 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9f49c2ef-fde4-3776-8c1d-691468ef7a21 | -4.09202 | -55.81022 | 2025-08-27 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dfbdc8cf-6d7c-366f-8c5c-0b22fbce058d | -6.9495 | -60.08197 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 89464e44-5a05-3f0d-9dd1-2d9061cf68e9 | -7.64979 | -42.6667 | 2025-08-27 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 829048bc-0119-3e16-a3e2-4592781a75d2 | -11.57678 | -44.64605 | 2025-08-27 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3335f4a7-8077-3a2f-a3cc-b82bbf7f3ebe | -7.43885 | -42.04446 | 2025-08-27 04:25:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3aa9b08e-b9cc-3e90-ba4b-31bba07af761 | -6.81049 | -58.96663 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fd410535-64c8-3da0-8660-3b22164b1a45 | -8.09157 | -45.01568 | 2025-08-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 865857b5-d96e-38ad-a184-a604374e17a7 | -8.15951 | -45.04873 | 2025-08-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 555a4e3e-cbfa-3a5b-b658-6d23fc0ed0c5 | -9.07816 | -49.56371 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4155f530-9722-351f-8448-f404e13ea105 | -8.47116 | -43.65517 | 2025-08-27 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 793bffe2-5139-37d0-9c37-a5249e96b91a | -8.25713 | -45.12005 | 2025-08-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8455e73e-0686-39c5-a6b9-789d832307db | -6.193 | -43.00674 | 2025-08-27 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| acaa9b4c-8667-31e9-8836-ee6007894479 | -6.79009 | -59.6446 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3b80811e-7f9f-3565-a126-f555fddbd5ce | -9.57887 | -55.38029 | 2025-08-27 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b29fff28-02be-3c17-974f-6b0132841c94 | -9.14674 | -60.78423 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 989ebbf8-6c83-32fe-aa88-f458bb72b458 | -5.22344 | -42.71888 | 2025-08-27 04:25:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1a997c48-177d-32cb-aa73-183ad75609ea | -4.47479 | -47.50564 | 2025-08-27 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d7b8d629-0a0d-3a42-9f2a-64f63015cd26 | -7.2537 | -57.66962 | 2025-08-27 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d6bea281-d3da-3914-872c-b04e6b139c92 | -5.11193 | -43.20914 | 2025-08-27 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d2f80108-0fb9-3c96-a1ab-c1588ce1dedd | -6.67673 | -58.863 | 2025-08-27 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 232bf8e6-7968-3f53-aa21-307201db5c25 | -6.95877 | -44.09093 | 2025-08-27 04:25:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4aa1831f-424b-304b-a6eb-12baddbf25bb | -6.80944 | -58.97228 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2f820f87-9ba1-3f22-b2ea-0df809265a1a | -7.21113 | -44.40851 | 2025-08-27 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 38f1cf4a-905e-3e31-8a14-23f6f69b6ffa | -7.64977 | -42.66392 | 2025-08-27 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 67485587-3870-3682-9066-127fcd88c9a1 | -9.26088 | -50.23565 | 2025-08-27 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3901751c-4fba-3998-80b1-5ead610f874b | -11.2468 | -44.99493 | 2025-08-27 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84b50344-e060-3edd-beee-8df20980bc7b | -7.65423 | -42.66263 | 2025-08-27 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 301b747d-9cff-3ba4-b3f6-8820685da728 | -11.15757 | -44.79244 | 2025-08-27 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da2b0685-ed24-38b2-aef5-7f05ba1248d9 | -3.73528 | -48.94202 | 2025-08-27 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6d6393da-de8b-36c8-bac3-8da14de20c5d | -9.08208 | -49.60518 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9cbf4d4-2dac-3e09-ae0d-545c836d85bd | -8.16716 | -45.04987 | 2025-08-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 257bc011-066d-36f4-b8ce-65d851c34a89 | -19.07797 | -44.33035 | 2025-08-27 04:27:00 | NOAA-20 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4793419f-a463-33d9-bf91-ef5b62c99399 | -17.54899 | -46.62563 | 2025-08-27 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0731eadd-a742-3657-a0c0-62419f0bfb70 | -12.7422 | -48.19815 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7ddbb746-779c-3e07-98a7-c5647ca4a78e | -14.76139 | -47.92641 | 2025-08-27 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a383bd98-be3e-33ee-967c-072c45e578a5 | -12.78386 | -48.10701 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 444f389d-211c-3a00-9e65-39da1ca00806 | -9.39773 | -60.52637 | 2025-08-27 04:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6fee50d8-7efa-3bc0-bed1-ce1e1fb3c7a3 | -13.98145 | -46.3522 | 2025-08-27 04:27:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 798219d2-91df-3dc1-9507-e3d0d88cf407 | -17.70271 | -46.0622 | 2025-08-27 04:27:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb6ee862-f04a-3548-ad59-3b4be3ca502e | -20.06112 | -42.61051 | 2025-08-27 04:27:00 | NOAA-20 | SÃO PEDRO DOS FERROS | MINAS GERAIS | Brasil | 3164001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 17726f6a-a156-3849-8aa7-b66b1ae23182 | -16.84971 | -49.57566 | 2025-08-27 04:27:00 | NOAA-20 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1fa34aa0-9678-368a-ac9b-baf0b8383fc6 | -19.07756 | -48.14258 | 2025-08-27 04:27:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87e955bc-d800-3287-a838-6740cd66d6f6 | -15.66476 | -52.73365 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c3099d31-9818-3f38-b3ff-01ebd1465f73 | -13.42977 | -46.85717 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8dbaf7cf-4560-3449-a081-7983c502b3cd | -15.09211 | -48.56507 | 2025-08-27 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| de6bdd05-b2a1-3002-a9cb-edc146b447d8 | -13.61424 | -48.20359 | 2025-08-27 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ced8ef36-d4f6-399b-96d7-86e0e0e780f1 | -11.52329 | -52.12601 | 2025-08-27 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4715f5e4-2e55-31a4-975d-a4136f08f7c6 | -14.84239 | -49.21122 | 2025-08-27 04:27:00 | NOAA-20 | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 754ac701-3d31-39f8-a0c5-6c5df4b3d297 | -15.61847 | -52.71211 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5cd5e17-2db6-31e0-9645-a586090b7b45 | -15.09542 | -48.56563 | 2025-08-27 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4ab8f51e-b6f7-3657-b5bb-dfe3c63d4d2a | -15.68496 | -52.75274 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1926eba-2a4a-3c94-84bb-8ec619b720d4 | -12.87375 | -48.09645 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 77eac9d9-1ecc-3a73-b2bb-f4ece8e8359a | -13.50566 | -46.87652 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 210d8059-c91a-32a7-b762-8f215bb02779 | -11.52893 | -52.11668 | 2025-08-27 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c186b36d-fe7b-3445-a93d-55901da42dff | -12.41194 | -46.48281 | 2025-08-27 04:27:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20e8e004-ec7d-3630-a085-35ab2977c0c1 | -15.65254 | -52.73611 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9e021e40-bde1-37ec-95cc-54d4876705f2 | -19.07714 | -44.32671 | 2025-08-27 04:27:00 | NOAA-20 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 63f36da9-296b-3742-b4bf-f69f9c429c64 | -9.40164 | -60.50687 | 2025-08-27 04:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 5e41045f-10d4-3f46-b2b8-0be7ba7d3e71 | -12.7649 | -48.18373 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4359a8c0-0097-37d5-b509-0f8952fea8e8 | -12.92706 | -46.31245 | 2025-08-27 04:27:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95692239-bd1c-355a-b51f-c397fa214b02 | -16.38344 | -46.27918 | 2025-08-27 04:27:00 | NOAA-20 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ac53899b-46c5-386a-8a01-cb8de12b0c69 | -15.17195 | -48.1871 | 2025-08-27 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 109acb42-732e-38ae-ad99-39559f41964c | -13.0647 | -46.32632 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e373b65-0099-3848-a2ff-ffd4294eec1f | -12.31467 | -55.30899 | 2025-08-27 04:27:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f5158238-500e-3ca5-984a-577e37578300 | -15.11911 | -48.67197 | 2025-08-27 04:27:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3fd20ad-cfd6-336d-8189-38d634d86738 | -13.50764 | -50.81207 | 2025-08-27 04:27:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5cf5f974-a5cb-330a-acc8-97f1789fccfe | -13.63731 | -46.8743 | 2025-08-27 04:27:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04e71e36-9d0b-3d8a-a666-7f69aa439789 | -15.61772 | -52.75493 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f12f91e9-f922-3c5a-880f-460a6f5897a9 | -9.40295 | -60.50035 | 2025-08-27 04:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 5542058e-3533-3b52-8c44-54e50943bb71 | -12.7599 | -48.19382 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 019a8cb4-2461-3a50-bb90-4d4b9404282c | -15.08338 | -48.53429 | 2025-08-27 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2671f7ae-14c7-33da-b428-3391532a2aff | -11.81769 | -46.79719 | 2025-08-27 04:27:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91f69d90-e9a3-38cb-9d88-24c6b7643684 | -13.53809 | -46.90398 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56ac8a18-2dce-3007-8865-fbc08b423e28 | -11.8144 | -46.8185 | 2025-08-27 04:27:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cb8b3406-7f28-3d74-9f5d-8a3f923b4ed2 | -12.79255 | -48.1156 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8c516484-42bd-3e1b-a9b4-72625bd0b3ed | -12.79048 | -48.1081 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 967aa29c-a86b-3724-ad5d-2fbd50b45d79 | -13.98541 | -46.34902 | 2025-08-27 04:27:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8aaf32a-6726-3c9f-bb80-5de8a8ae9f92 | -16.78787 | -47.5611 | 2025-08-27 04:27:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README44.md)
