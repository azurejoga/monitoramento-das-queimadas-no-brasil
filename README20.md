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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef695349-27d3-35e2-8305-c111f1c2d638 | -5.34452 | -41.25426 | 2025-08-19 04:25:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a0f59a94-f2a5-3c45-938e-0c7db579c00b | -6.94043 | -43.58739 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 87104a40-ac21-3725-b6e6-b8a76f656755 | -5.65369 | -43.40636 | 2025-08-19 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24450fec-5817-3cf7-96da-574ab8a8d272 | -6.54542 | -43.00982 | 2025-08-19 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 29f81380-e6bf-3ac8-a3f3-31a0ba61c8bf | -3.36387 | -43.36121 | 2025-08-19 04:25:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ce41a02-aec9-3a6e-8a46-4cf12e772570 | -4.59182 | -43.31588 | 2025-08-19 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8061ca9a-3b52-3895-9e80-52dc5cc1b944 | -7.60009 | -44.40039 | 2025-08-19 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 272a74bc-a490-3187-b690-150cf2e742d1 | -6.58325 | -43.08152 | 2025-08-19 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6d7accda-f3ab-3287-87ef-b0dd45365dc5 | -6.94681 | -43.5867 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| efa5b08f-2aef-3f6d-ae16-cc1335031a30 | -6.94556 | -43.61992 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 27d89f25-092b-3e17-b2fb-02b8b08728b1 | -6.02463 | -44.34612 | 2025-08-19 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d77c0bf-2b8e-3bd2-b93a-3ac6d701c5ab | -4.42798 | -47.76119 | 2025-08-19 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4e3efee-85f1-38a0-b5c3-57dd70a7b912 | -3.12897 | -48.9855 | 2025-08-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34d01a93-bf41-363b-8755-a44311757c19 | -3.64721 | -43.95647 | 2025-08-19 04:25:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8c7574ad-fbb7-3539-947d-5fcf66af804c | -5.9019 | -45.53871 | 2025-08-19 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 608d9d7d-e5aa-3e7a-8aa9-609cad712bf5 | -5.658 | -43.37825 | 2025-08-19 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35b5d766-11c6-3c09-b8fb-9fd8d84b7c27 | -7.13976 | -44.59639 | 2025-08-19 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d9cc4a16-c70d-391f-a9fd-357961099ecb | -6.58303 | -43.08456 | 2025-08-19 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b58dd67-851e-35fc-98a1-d0e2c36c7d28 | -4.34259 | -55.78671 | 2025-08-19 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7630797a-5f3a-34e6-8b3e-fa3cb2392995 | -6.94737 | -43.60764 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bd6bf115-bcd1-3e4a-a460-ca132da02a02 | -6.7463 | -41.5407 | 2025-08-19 04:25:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0e5a704b-a6e8-386f-9ffa-fa6752ba50d5 | -5.65136 | -43.39783 | 2025-08-19 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed73a99e-372a-326a-9677-999c9ddeb1aa | -6.08872 | -44.59135 | 2025-08-19 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 208be844-1c87-373f-b6da-cd89037732f1 | -6.27672 | -43.69079 | 2025-08-19 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6baabca-fdbe-3325-b5ba-41b77c39ed7c | -6.02462 | -44.39201 | 2025-08-19 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80c3a43e-fe36-304d-936a-3483b4e94747 | -7.14994 | -44.20931 | 2025-08-19 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1bfb549b-beec-3b3a-a4af-3485f3d00410 | -3.48392 | -48.43886 | 2025-08-19 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9533c42d-4d78-3313-bb2e-007c19693be4 | -5.66218 | -43.37474 | 2025-08-19 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d00c1faa-8d17-3dab-b2d2-5e5acc0f050a | -4.43254 | -47.75437 | 2025-08-19 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| df8ffc95-98a5-3313-86e0-431d4021fdcf | -6.5997 | -41.40108 | 2025-08-19 04:25:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fa1b26ad-0191-3a2d-aa4e-429472b061c5 | -7.59257 | -44.40321 | 2025-08-19 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b58cfe0-4a3a-3603-8eb0-01aa63921807 | -5.9929 | -44.13718 | 2025-08-19 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2eab0172-3d62-3c2d-9989-36993099856d | -4.92467 | -43.24891 | 2025-08-19 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 405b4c19-aa3a-3d5d-9be5-dba6643a9870 | -6.58367 | -43.08023 | 2025-08-19 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e97756ee-9856-34a6-97d7-d5151297373c | -6.37586 | -43.31903 | 2025-08-19 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 217a5e39-ee1a-3840-b4fd-830474612b52 | -6.92908 | -43.58986 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| a2d80d79-58d4-3eaf-9af1-967f2668950f | -6.93903 | -43.61469 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2d61d1db-b859-333c-8183-88b9bebd95ed | -4.03626 | -38.76875 | 2025-08-19 04:25:00 | NOAA-21 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 410859dd-d839-30c7-aa5e-77bdbfb7cd47 | -4.54287 | -46.6843 | 2025-08-19 04:25:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c392c279-fbe8-3e72-8ddf-b27fce92298d | -3.37682 | -52.71759 | 2025-08-19 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0efa38de-180f-3724-87b0-fdbc7d64139f | -4.40791 | -48.94226 | 2025-08-19 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d527239-8f4b-3492-b4e3-af2bd1e36806 | -6.55164 | -43.9834 | 2025-08-19 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f342b683-a274-3a2d-9d00-58d3edeb1804 | -7.63087 | -46.23005 | 2025-08-19 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a5b1710-8665-3b83-af8b-87f9f19ae284 | -6.92846 | -43.59395 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 819afcf7-d6e1-3d86-b995-effd40085657 | -4.02148 | -48.06719 | 2025-08-19 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b2cea8b-f403-3e22-99ae-7515437a89f9 | -4.27298 | -48.18309 | 2025-08-19 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bbf9a34-2e45-3bd4-8b60-283e35ecd420 | -6.39793 | -44.28628 | 2025-08-19 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3a2e677b-9d7f-3178-8d15-985715b13168 | -6.96826 | -43.58999 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 35.1 |
| f7dd2305-3c58-38d0-8051-5635eca5b17a | -5.78921 | -43.8926 | 2025-08-19 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b8c9a3e-dc06-36e9-b6bb-aa3890f00309 | -4.01803 | -48.06668 | 2025-08-19 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03f1db5e-24d1-3a33-ac4f-361974573cd9 | -6.7498 | -41.54481 | 2025-08-19 04:25:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 38d81978-f8ab-36f3-9402-0b83682b7783 | -6.54966 | -43.98809 | 2025-08-19 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9930375e-d471-318e-864d-a4c111dff0c7 | -7.029 | -44.58767 | 2025-08-19 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3b13de9-dff3-3f02-8de3-512a874d77d3 | -3.03851 | -49.43626 | 2025-08-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e49a7d6f-ad25-35c6-af28-db1bf6ad65f8 | -5.43142 | -42.35329 | 2025-08-19 04:25:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b1375acd-0c2c-3f3b-9564-b6df35fc8c66 | -6.10333 | -44.40421 | 2025-08-19 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e726688-500a-3e8c-9f83-75eac60ea580 | -5.87403 | -48.1198 | 2025-08-19 04:25:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| aff39565-328c-3487-9d93-97cddd8680d4 | -6.93732 | -43.60776 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4db955db-829c-3c23-9197-4b3171d258c8 | -6.68023 | -43.67846 | 2025-08-19 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d1c231b-160d-30be-8c7b-a184ceed4daa | -5.3616 | -41.22134 | 2025-08-19 04:25:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8ecf853f-28e8-3efa-be6a-c89d5da037de | -6.51521 | -44.41558 | 2025-08-19 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ad32bb9-1086-3cc1-9775-08dc3621a5d2 | -6.74579 | -41.54419 | 2025-08-19 04:25:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bb0520ba-cda2-36ce-9944-6952e30fd45e | -3.45464 | -48.96486 | 2025-08-19 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 14d6b167-d460-34e3-8dec-085b31dd29e2 | -7.37986 | -44.27787 | 2025-08-19 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2f2c0c2c-561f-3263-acbd-714d912c8120 | -4.59686 | -48.78154 | 2025-08-19 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f38b5420-1e45-3b0b-a2ca-a9466e1df1ea | -5.98108 | -44.28602 | 2025-08-19 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40a44f3e-43a1-3d61-bf37-26c30831e94a | -3.97346 | -42.52026 | 2025-08-19 04:25:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 71cf60bb-a0ce-3b1c-92c4-b9315e29df32 | -5.55105 | -49.07351 | 2025-08-19 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08302d0e-389d-3b89-9344-673555ce9ab9 | -7.20195 | -46.25515 | 2025-08-19 04:25:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| edcdcd9c-85ef-3d91-99fb-b207dff87fbc | -5.97364 | -44.28872 | 2025-08-19 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| be7bf947-411e-3a97-b3a7-01bc1765f3e6 | -7.29113 | -43.68105 | 2025-08-19 04:25:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44b486d1-5a83-30db-8920-0c9fa03ec6c2 | -5.78573 | -43.89206 | 2025-08-19 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ac376ad-99e3-317a-bfe8-54e96332e45c | -6.66429 | -43.66381 | 2025-08-19 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c1e40ed-c708-34d5-9e8c-53207f957ea5 | -7.00935 | -44.27872 | 2025-08-19 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 46ac8821-0b73-357b-9a76-d2d525ccc979 | -7.1453 | -44.19296 | 2025-08-19 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33956967-836a-3c1e-b3f2-3f04de04f5f8 | -5.75487 | -46.67767 | 2025-08-19 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1c3d1b9d-60ec-33bb-b2e4-fe7904747c5e | -6.9426 | -43.61527 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d0d4a4fa-a73a-3a20-a95d-49480ca6d1a8 | -3.98204 | -42.51289 | 2025-08-19 04:25:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| bcdcc734-e328-3bdb-bffe-5072c2f7feae | -6.55053 | -44.01477 | 2025-08-19 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 760671d6-0d90-320e-8332-b2deaf519a39 | -3.17801 | -52.87283 | 2025-08-19 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 902c5619-2655-3c40-9039-69be6ccd0df5 | -4.72717 | -38.4001 | 2025-08-19 04:25:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ab032bbd-8f4a-3988-b240-8edbaf373938 | -6.03434 | -44.35147 | 2025-08-19 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| deb6d3fe-c4d8-3c4f-aec9-6ab7ca02552e | -4.27867 | -48.19174 | 2025-08-19 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 729a8713-6635-327f-8ed4-ebdbfb2dac26 | -6.51811 | -43.43616 | 2025-08-19 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 66dafcba-5701-3527-a3ae-f89d95bdeaff | -6.95034 | -43.6123 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bf63510d-cd1e-3c5b-b852-b344d0fabb65 | -6.9605 | -43.59298 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef7d3845-6b8b-31f5-b0d7-fe49b7ef15a0 | -3.65016 | -48.32767 | 2025-08-19 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0260bbd-1b0a-354e-82ca-d6098f14e632 | -6.93498 | -43.59912 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c80fe69a-d012-3e65-aee5-0ca39fdd8e02 | -6.95038 | -43.58725 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| addf24f3-e7ee-3253-92b9-3b9aa3e6a130 | -7.35048 | -44.98408 | 2025-08-19 04:25:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51089797-1b88-3ed1-b846-2942bb14709d | -5.65614 | -43.39036 | 2025-08-19 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 913bcf37-5ee6-325a-8d9f-59035dc6fdfc | -7.3054 | -46.28912 | 2025-08-19 04:25:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d9d7d1b-2cb0-33eb-b2bb-33ca6385aa5b | -6.52226 | -43.44859 | 2025-08-19 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 199590ec-3766-30d5-b021-1d79d6a18953 | -4.00192 | -43.26707 | 2025-08-19 04:25:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71abe556-54a5-3f48-b08f-42974b4e75c4 | -5.75927 | -46.67128 | 2025-08-19 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9702f489-fda4-34c9-bd09-5e6ea4d16622 | -6.86589 | -43.11876 | 2025-08-19 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53f54fe5-79cf-35f3-a03c-001ecbd795f0 | -7.50707 | -44.99567 | 2025-08-19 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b96ea736-689f-3a26-8d5f-e7f68a3dc032 | -5.78946 | -43.60837 | 2025-08-19 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 822e7746-6ffa-3641-b252-f9cba8dfc6ac | -6.45072 | -44.56296 | 2025-08-19 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 91b0b963-73ba-36a7-8eda-ae500137037e | -3.45759 | -48.96959 | 2025-08-19 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README21.md)
