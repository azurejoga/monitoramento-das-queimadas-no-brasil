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

## Dados Diários - Página 326

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d20bff67-f113-3e0b-9154-44bca3d252ea | -8.35573 | -50.72705 | 2026-10-08 16:37:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe328c19-8277-3bd4-b3e1-796979fdd112 | -12.01448 | -42.07096 | 2026-10-08 16:37:00 | NOAA-20 | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 1d686885-47c8-3771-818e-3f9425e2a37d | -6.0539 | -42.60201 | 2026-10-08 16:37:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 38.4 |
| 5c4bb33f-77f6-3f26-ab41-815f5e8ddd77 | -9.90389 | -44.82183 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 13b1eb96-f448-3614-9ba0-501e393a05f7 | -9.23687 | -41.00434 | 2026-10-08 16:37:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 15.8 |
| b1f82d4f-a97a-3340-9f1d-7cca25b8818b | -8.89402 | -45.3847 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 0ca43625-6997-3066-b3a7-d78ca557a8c7 | -12.846 | -44.62327 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 4a144618-9b80-3705-9108-1c1c0023ae34 | -9.89048 | -44.86685 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 6c71782a-2b84-3c46-8d38-94c77d2866a1 | -6.16266 | -39.42725 | 2026-10-08 16:37:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| ffd1ac80-8d66-3607-a5f7-83187cbebb9d | -8.30122 | -45.72512 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| eb094e0d-047d-3b47-a71d-7da5be229a0a | -10.93318 | -45.38687 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 2b5a6b77-48fb-31aa-9772-6085af819c98 | -7.13197 | -44.08197 | 2026-10-08 16:37:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 8c46eb0a-4e63-3606-9418-f0ac580c6710 | -13.02439 | -41.04889 | 2026-10-08 16:37:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 4f2a7ec8-65aa-3cd0-a82b-1451b4ee834b | -6.41451 | -44.95054 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8370a6a9-fff3-34a8-a27f-40450e6e3b19 | -11.18309 | -47.72545 | 2026-10-08 16:37:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9eadfed1-178f-39cb-9def-b2d95d30eb4f | -11.31991 | -46.6581 | 2026-10-08 16:37:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9b0630da-89cb-385b-8e3a-954a7c2d7d23 | -11.14053 | -46.13347 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 1de801da-2c4d-34cc-9641-8eed4c13bd29 | -11.85609 | -43.53633 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d0b1251f-6753-3a42-a8fe-5ac677547e16 | -13.35917 | -43.87597 | 2026-10-08 16:37:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 3e078b53-4025-3289-b08e-d3045588c85c | -8.86051 | -36.94292 | 2026-10-08 16:37:00 | NOAA-20 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2a0fbb6d-6a04-3447-9ee9-db12319c0486 | -8.78633 | -47.26229 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 8d41f686-77e2-3a15-96f4-a87fcda0d6fa | -6.16744 | -42.58539 | 2026-10-08 16:37:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 64.2 |
| af124761-964b-357f-965c-82574af19f84 | -11.48593 | -51.30661 | 2026-10-08 16:37:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f5a9005c-439a-35d9-9af5-3022831e8339 | -6.22973 | -35.33988 | 2026-10-08 16:37:00 | NOAA-20 | JUNDIÁ | RIO GRANDE DO NORTE | Brasil | 2406155 | 24 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| e994786e-4660-3569-bebd-fabca4620b52 | -8.36394 | -44.76289 | 2026-10-08 16:37:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 802e57b8-a811-30f9-80b0-fc6c060899c6 | -5.99299 | -42.71157 | 2026-10-08 16:37:00 | NOAA-20 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| e7816e0d-caf3-3c75-9fa8-e27205167960 | -10.29611 | -46.61422 | 2026-10-08 16:37:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| ce7b3802-bcae-31e1-97d2-d9a6da7df7b0 | -6.18263 | -44.10419 | 2026-10-08 16:37:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0b1e0a33-84e4-3e60-b265-4b82623a8a53 | -6.0314 | -42.71862 | 2026-10-08 16:37:00 | NOAA-20 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 32.4 |
| 17a23beb-deb4-3e86-b43b-b3dc7620db38 | -9.18352 | -46.70283 | 2026-10-08 16:37:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 87f5c3bc-d8f5-3b96-9d21-210542f7a664 | -6.05591 | -42.92013 | 2026-10-08 16:37:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| f85fb0b9-80af-305c-8169-8dd97e9b05cb | -9.88994 | -44.86335 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 3e66369c-830c-3b33-afcb-aa834062c48c | -9.10498 | -45.12249 | 2026-10-08 16:37:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 3c7d5e48-fc71-3103-897a-a55e5b8ad9a5 | -8.55829 | -40.28166 | 2026-10-08 16:37:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 8.6 |
| ca4fdd65-5d0c-3ddc-851d-45b682710d6d | -8.31099 | -47.6408 | 2026-10-08 16:37:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 352001eb-02db-31ce-9e4a-f017669ebda5 | -12.98958 | -47.0603 | 2026-10-08 16:37:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 23019d23-c8fa-37fe-bf26-de6c020e9f4e | -8.89733 | -45.38419 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.6 |
| e4013749-31b6-35c2-a31a-f1a6f7ca9648 | -8.2852 | -45.73112 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 1636d6f7-1508-345a-baf5-3cd164fc4dfc | -9.88833 | -44.85288 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 5c9cf7b9-c64b-3d24-9f53-d3d73f3e6efe | -12.62088 | -44.54853 | 2026-10-08 16:37:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| a1200e15-8af4-3bef-ba35-ea527c9f393d | -10.45058 | -47.28168 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 31.5 |
| fa1363a3-e5aa-35b6-b8ed-ad4d0435c240 | -6.89433 | -43.70732 | 2026-10-08 16:37:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 9c8cb25b-7ed1-3d51-929b-9c37247479ce | -7.0496 | -44.34072 | 2026-10-08 16:37:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 1b5458bc-6018-39d6-9a03-f8c6521a1e3c | -6.56654 | -44.38429 | 2026-10-08 16:37:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62ba6260-d495-37d8-8d18-8475f664eba0 | -5.81633 | -42.50044 | 2026-10-08 16:37:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| e059e8e9-2ee6-329b-b81e-3cae1c263e7b | -5.98722 | -41.36199 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 9c0dac87-99ef-3bef-ae9b-6ff16d3817e7 | -6.03708 | -37.27765 | 2026-10-08 16:37:00 | NOAA-20 | AUGUSTO SEVERO | RIO GRANDE DO NORTE | Brasil | 2401305 | 24 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 579df721-48be-3b31-9c12-72bb2cc579a2 | -6.52666 | -45.39446 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 122.7 |
| d314d9a1-f6ed-3ea3-bc6e-a53bd75287cd | -6.7082 | -44.98625 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0ffe678d-d726-3791-8dbc-fc4c2011da77 | -5.96753 | -40.9141 | 2026-10-08 16:37:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 22.5 |
| 506512bc-851a-36ca-90eb-2c5c55cd8787 | -8.92594 | -45.19469 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 174.7 |
| 66748ad0-558a-3e3f-92c3-aa9e965feaa4 | -11.84177 | -47.3357 | 2026-10-08 16:37:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| d5378eea-4b71-3d2e-949f-200592e56317 | -13.67732 | -48.64139 | 2026-10-08 16:37:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 82379b6a-c20b-3025-83dd-ec37389cfdba | -11.33119 | -46.68723 | 2026-10-08 16:37:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 9223fa4e-7e8f-365f-ba97-fa22a1b3be25 | -8.30784 | -45.45758 | 2026-10-08 16:37:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 798e22f3-2dcd-39d6-abc6-6bcf5a5bb03c | -8.29738 | -45.72215 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 24ff15ca-01e3-3c7b-8357-4408dbb978b3 | -10.19568 | -36.80434 | 2026-10-08 16:37:00 | NOAA-20 | PORTO REAL DO COLÉGIO | ALAGOAS | Brasil | 2707503 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 1067a850-e441-32ee-93bf-ea19077076c8 | -7.05 | -48.56752 | 2026-10-08 16:37:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 28.9 |
| f983dfc5-53af-31c8-9302-a7a1b58f9d66 | -8.58047 | -45.68835 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5fa92231-8950-35be-baba-8346f065cb51 | -8.1822 | -54.72106 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| d5673ce4-825d-3979-9de5-0a1185775c36 | -8.10187 | -39.88418 | 2026-10-08 16:37:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 7fbda259-fd9a-3643-bba2-c62b17197418 | -7.97583 | -45.48268 | 2026-10-08 16:37:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e844227a-fc6b-3347-b333-2fde858f092a | -10.07721 | -45.69278 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 24deb514-65a0-30f0-bacb-103fd3aedd38 | -6.69006 | -40.91833 | 2026-10-08 16:37:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 720299f6-93df-3fc6-a368-e92488199da2 | -5.74893 | -41.72685 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 38.4 |
| 2f6911c3-cd09-3f80-bcd6-0638c5c79b13 | -6.40483 | -37.79195 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 966bf01e-3b3f-3fb4-8c39-6663036e391a | -7.88688 | -44.96946 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 18181019-9d48-3c94-86d8-35f7476f2025 | -12.22914 | -44.73885 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 349bc7cb-1b31-3163-9700-173bec985367 | -12.77367 | -44.86258 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 660b06cf-f21b-3776-a985-b9a2f2bf6ab1 | -8.88847 | -45.39268 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 34344a6d-b197-39bc-b82e-bcfbc0ef8cbb | -5.74371 | -42.0546 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| e2124b30-b582-3047-aabc-029df8f8e32d | -7.38116 | -46.23465 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 243b12ce-e1d6-3851-8db6-ee542562da24 | -6.15523 | -39.43777 | 2026-10-08 16:37:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 62d6de0d-96a8-36b0-a58f-9ec1c54bf822 | -6.83281 | -47.48605 | 2026-10-08 16:37:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 21412d2a-c827-379b-9c34-39a05e05d4aa | -8.54998 | -46.92263 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f7c481ba-445d-3fca-a95e-c5be115f9a2f | -7.59624 | -42.3886 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 69.3 |
| 86733d6b-4d02-3283-9e27-43b992ab900c | -11.26554 | -47.74271 | 2026-10-08 16:37:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a7e7c169-ebf3-3dab-9f76-65e6031be24f | -6.22307 | -44.8578 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 855c2902-35be-3036-8bde-a0839d25776b | -18.43778 | -40.59275 | 2026-10-08 16:37:00 | NOAA-20 | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| dda881d8-51b5-31dd-b2f1-c9a4570ce267 | -9.74796 | -46.95405 | 2026-10-08 16:37:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 69bc71ac-187b-3dc0-b7a1-25c087eb7415 | -5.71465 | -41.6378 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 756535d7-13f8-3e0e-baa4-8db8cf5e908e | -11.27269 | -45.20954 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 3e8c7e5f-5a73-38ea-8ecf-d71773bb35c6 | -11.39457 | -47.56304 | 2026-10-08 16:37:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| ddf3eac0-aad0-37a0-b005-92ed98717a16 | -11.07418 | -44.02782 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 81ec9609-3575-3f17-afc8-59feeacdd18f | -11.76931 | -45.55767 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 15a41386-3095-3942-960d-402817397fc7 | -12.7107 | -45.82196 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| c7d0de65-e943-3504-b9ca-a3f8746802c1 | -11.20574 | -49.4235 | 2026-10-08 16:37:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| b7e8de39-bc53-33dd-986b-534f99e97ffb | -6.67745 | -45.58032 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c6248950-8a62-346b-a820-23ea6a8249ee | -9.82505 | -44.83839 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 5c503f46-f7ba-3772-a8b9-f0e191ac4955 | -6.07135 | -43.88786 | 2026-10-08 16:37:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a3379236-41a2-3a9d-9985-fa1fbd9dff15 | -13.26626 | -44.00012 | 2026-10-08 16:37:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f37df6e7-bf19-361d-b13a-02f081cb1e6b | -9.88386 | -44.86787 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 8a6730c5-9428-3c25-a064-920ef5cb2945 | -8.19373 | -46.36044 | 2026-10-08 16:37:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 7f2d2a24-d611-3e19-a449-9de8382680e2 | -6.44439 | -45.8083 | 2026-10-08 16:37:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 98e3f195-07a8-329f-a8d2-d504ce9c3631 | -11.8384 | -43.56891 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 2e708a34-3676-3a7b-9cbb-25f0dddab82e | -11.30843 | -46.69859 | 2026-10-08 16:37:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 26.0 |
| cd1ca2b3-da05-3eca-9295-93f8934e0569 | -7.05185 | -44.33296 | 2026-10-08 16:37:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| b2283c54-c0d8-34c6-b7cf-1edf56e8b1b8 | -5.755 | -42.07791 | 2026-10-08 16:37:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| f97d51a4-8657-3134-9415-4863b60d509a | -6.80017 | -45.05443 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 530984b2-22d3-38c1-bd2f-ee5a97c45c47 | -12.22422 | -43.93354 | 2026-10-08 16:37:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 224.7 |


[Clique aqui para ver as próximas entradas](README327.md)
