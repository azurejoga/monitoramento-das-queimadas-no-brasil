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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| abc1e96f-4dc9-33b3-b0d5-2cc37f3d09e0 | -6.29189 | -43.62891 | 2026-08-11 03:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eabec947-7d0d-3fa8-b726-bae0ee71328f | -14.11717 | -45.63203 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| da8cd17f-4426-39ce-858b-92d6373a9829 | -13.48375 | -43.07853 | 2026-08-11 03:49:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 06d34cd7-71b1-3cca-a954-ac4690003332 | -12.49545 | -45.27953 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 716efb71-e1c0-32ca-be5b-a63c89b05edb | -15.01371 | -46.58149 | 2026-08-11 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40423957-15c8-364b-b418-3e278ac704c9 | -18.02556 | -44.4359 | 2026-08-11 03:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be57a3b3-33ae-340a-85f0-fc836ace4c0d | -7.82839 | -38.1581 | 2026-08-11 03:49:00 | NOAA-20 | SANTA CRUZ DA BAIXA VERDE | PERNAMBUCO | Brasil | 2612471 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cf1ffd54-1a37-3b50-9fbb-90893bba0bd6 | -10.42338 | -46.68267 | 2026-08-11 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| ef8063d6-5db8-311d-8cd0-c135562cbb1d | -13.56445 | -46.28345 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 9fee4038-f14e-3e5b-8c54-32080a12f5d9 | -13.61952 | -46.22549 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1792e6e7-0cac-3a00-8c87-cd642f629d6c | -13.56299 | -46.31839 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a4f5155-21ab-39a9-b0c8-e2373c3bb62a | -13.56579 | -46.27673 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 39654384-4a83-3746-a356-ea4787c0f822 | -13.26005 | -43.53893 | 2026-08-11 03:49:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 491318f8-3db8-302c-b581-c00489503412 | -14.4545 | -45.70539 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d6f478a-6773-3117-8a3a-b6f38537349a | -10.41915 | -46.68172 | 2026-08-11 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| b1c0280a-052f-39bb-813c-511e5946a6c2 | -10.42644 | -46.67476 | 2026-08-11 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 15c139ce-3d9c-319c-92cf-5d163f6077ce | -14.62681 | -47.66492 | 2026-08-11 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8da7dd1a-7c39-3bf9-8106-6437d57e5296 | -18.01542 | -44.37173 | 2026-08-11 03:49:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| edc914a7-0dd5-3757-93aa-6ad25f14a453 | -14.44944 | -45.67847 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0cd18168-49c7-308f-ab7d-0c11023553d7 | -15.00193 | -46.5864 | 2026-08-11 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e295b0f3-4683-3b72-899c-43512a73df2b | -10.42155 | -46.66955 | 2026-08-11 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6c3dc6cd-f89a-39a5-88e4-958159c4baa9 | -11.4682 | -44.57258 | 2026-08-11 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 28b842de-3f03-3366-86af-429f4cb782e5 | -10.41836 | -46.68572 | 2026-08-11 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 74d88d54-6721-3143-81eb-b6256aecd4c5 | -14.49616 | -49.3004 | 2026-08-11 03:49:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1d805da4-5984-30aa-a00e-830ee139cb05 | -13.51742 | -44.14009 | 2026-08-11 03:49:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8fe27ef-b784-3398-8f0e-46d7e7820d82 | -12.46225 | -45.34394 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4cd53530-17fa-35a7-b23e-601fcdbe4ada | -14.45059 | -45.67261 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ade8773d-e1e2-30f1-bfb0-a4f8430377c8 | -11.46114 | -46.65736 | 2026-08-11 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec987c04-c92c-3d7d-ba43-16bc2c8c288c | -14.63243 | -47.66619 | 2026-08-11 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18ac4206-90b3-333f-b623-919c27849e27 | -12.4696 | -45.33291 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 150.8 |
| bbab8971-8e0a-34d0-b17f-15afcc6a5f25 | -18.24987 | -42.38385 | 2026-08-11 03:49:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 2aba34cc-1ecb-3d21-a211-284246f9348c | -17.89339 | -44.46465 | 2026-08-11 03:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 520906de-c494-3a1f-9a4f-c8d7411d086c | -14.4501 | -45.70142 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ebc07a94-bc1f-3299-9220-0abf2f9f89c5 | -14.48968 | -40.48304 | 2026-08-11 03:49:00 | NOAA-20 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 45d9321a-1f8f-3ead-8ca0-09d35ecca087 | -12.46064 | -45.32505 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e61c4cf5-1d26-3810-a819-f9d6a8514db5 | -12.48931 | -45.2844 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a4995225-039b-31a2-9cd6-0f6c728ff5f8 | -14.99384 | -39.52519 | 2026-08-11 03:49:00 | NOAA-20 | ITAPÉ | BAHIA | Brasil | 2916203 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| caa8b4c7-d272-31d4-bd93-f8708a7856fb | -13.64731 | -46.25049 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2aab2053-44be-3275-b29c-6ba32eed2517 | -12.47304 | -45.31493 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 89a542e8-4c10-39a6-a67b-4331c3a60be0 | -12.48472 | -45.33589 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 476b042a-f2d3-3d45-aafc-d46962a500bc | -15.01722 | -46.56424 | 2026-08-11 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bff0e24c-4cce-3a8e-b8b5-b514ef0904a0 | -6.00822 | -47.40155 | 2026-08-11 03:49:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4fcbba1d-a6e3-3bf7-ab62-073fa4bef668 | -11.95651 | -46.33506 | 2026-08-11 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0cfcb9e7-6411-3399-901f-34e3f1456397 | -18.01116 | -44.37076 | 2026-08-11 03:49:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 774b1209-fab9-3433-869c-9fe56d1289c1 | -14.65167 | -47.65805 | 2026-08-11 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 11e5397d-af00-3eb1-906a-6e9da664aceb | -13.6454 | -46.25697 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e56a45d5-64b3-3e75-a1f6-e00e21c78dc0 | -14.45326 | -45.68537 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 88040657-2016-3491-ac99-723e662f93a0 | -14.49087 | -49.2947 | 2026-08-11 03:49:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 107d9c76-e5c4-3ca2-94b7-423e7d9343ba | -10.43786 | -46.63725 | 2026-08-11 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 838cb25d-3815-3744-b3b2-fb56a7de8a72 | -12.47911 | -45.33789 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 52.0 |
| e0122c32-d652-3202-a841-42ef3076fe7d | -12.47739 | -45.3469 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1b6a7367-68f8-37b2-b724-d368582b23f3 | -14.27843 | -45.31273 | 2026-08-11 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e6a8a31-2f97-3bd4-ae27-697d98d78345 | -15.02077 | -47.0411 | 2026-08-11 03:49:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2e59e4a4-952f-39f3-974d-7a4a8d175faa | -12.46122 | -45.32205 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32760808-d9ad-3467-8f48-f6dcfbee527f | -12.46672 | -45.34792 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de409cf9-1dbf-38c6-b13f-c4f8f67438cf | -15.04014 | -46.55825 | 2026-08-11 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47a62559-3ad9-36f6-9332-e5d46846191d | -14.99856 | -46.6036 | 2026-08-11 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4b1f1723-8f22-3e03-9cdd-8a13663b27b6 | -12.47349 | -45.33989 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 1d785d74-c62d-3ad9-a452-7eb3a5592dfa | -12.47865 | -45.3129 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0a9ea371-70e3-3a26-9813-cef4c698bcfd | -18.03213 | -44.40098 | 2026-08-11 03:49:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28ff3b98-7c36-387d-b2ba-88fc90b7fb23 | -15.58168 | -40.98835 | 2026-08-11 03:49:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 650f7b31-31a9-38f2-accb-d332c3a09d75 | -10.42804 | -46.66663 | 2026-08-11 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 74b056a5-f069-3089-813b-fdce98a5a2ae | -15.00762 | -46.58472 | 2026-08-11 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b294cd1f-bee6-3775-b114-192889496012 | -13.65055 | -46.25847 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d4e3b7c-f0dc-392a-9a69-6bfca0333b6a | -14.62271 | -47.65631 | 2026-08-11 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3ee30f14-ee46-3efd-980c-c7aa6fce506d | -14.61705 | -47.65533 | 2026-08-11 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cbffdc0f-0cec-3845-89ee-a95fef0468dc | -5.74029 | -44.50401 | 2026-08-11 03:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ecd2a74f-e2b9-3c03-b2e5-fcda0b373edc | -15.00627 | -46.59135 | 2026-08-11 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 779fe39b-9829-3601-97a1-8cbba687cd4b | -4.26794 | -48.19497 | 2026-08-11 03:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| cb8ea170-9abe-30aa-8142-d3c9f7270c62 | -11.01335 | -45.63916 | 2026-08-11 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6beded69-e6d8-336c-90da-535d183b85c0 | -15.86869 | -43.59924 | 2026-08-11 03:49:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc244a49-c62c-3663-9a88-bdbf23b84ee8 | -11.02305 | -45.64581 | 2026-08-11 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c44409a-3d17-3c8e-a441-57472cb480aa | -12.4641 | -45.30709 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a549b75f-df0b-3d12-8958-06f2c45d1fc1 | -12.46282 | -45.34095 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c1e5751-f295-34bd-ade4-de248b168b64 | -12.49376 | -45.28841 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e8128023-7670-3f38-affe-c4e60241ac56 | -14.45565 | -45.69954 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 868fe67f-88cb-39e7-8c5f-000f9fa25b1d | -13.51281 | -44.13942 | 2026-08-11 03:49:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3d27e47-ec37-3e0e-be97-3b5a260934fa | -15.98586 | -43.00759 | 2026-08-11 03:49:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d471a392-25ec-3eb1-9abd-12b9a1eb407a | -14.45947 | -45.70644 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 76975596-6395-3de7-b255-afb9510e40ca | -11.46038 | -46.66128 | 2026-08-11 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ffd051b-38c9-3508-9dbd-2500761d92c1 | -14.1263 | -45.61202 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4644c047-05d4-35e1-9c42-55166e155b11 | -14.61629 | -47.65902 | 2026-08-11 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 697cd023-3d6c-3a23-81f1-5b07e6634ba4 | -15.52436 | -42.66414 | 2026-08-11 03:49:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| af169c44-a3ef-3364-80c8-9a97e12ffa7e | -10.42487 | -46.68277 | 2026-08-11 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| eaecfe76-d7f4-3c57-af66-83ecbadce5c4 | -11.02125 | -45.65532 | 2026-08-11 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e19b9c2-ae0a-38e6-840b-950484803261 | -15.00725 | -46.58699 | 2026-08-11 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ed71faf-7c1b-3340-8dee-c04622f0810d | -13.60708 | -46.31701 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8abba40-683e-365e-80ee-5f6e1ae9dc63 | -12.45501 | -45.32715 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 726a369b-acda-3abd-9c99-d7bbefffcb00 | -15.01665 | -46.56705 | 2026-08-11 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 63ff3645-8ec0-3900-92cc-ecb9a6aa76dc | -12.45777 | -45.34002 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ea33ed2-3bed-38c9-9146-603ad81be91e | -11.46218 | -44.5649 | 2026-08-11 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e7793174-ceba-3035-835e-7b39f6f8df1b | -15.86612 | -41.97644 | 2026-08-11 03:49:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f322797d-4019-3440-8802-55ea9b312a38 | -14.46062 | -45.7006 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b5f9d315-9d2c-36ca-b617-e16ca247957b | -14.62196 | -47.65994 | 2026-08-11 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| a4a4907d-02b4-3720-b124-f7b1f56f508e | -15.01607 | -46.56988 | 2026-08-11 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e92cdaa-7933-328d-aa01-657b23c7af20 | -12.48875 | -45.28734 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 756b04fb-269f-3141-934a-9639b06aa878 | -14.99307 | -46.60271 | 2026-08-11 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec0bc9e9-f7ad-35f0-b0c6-62591aa302d4 | -13.64673 | -46.25037 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 676bdb8e-b811-329f-b09c-6e37eccbf6b7 | -6.37485 | -37.37457 | 2026-08-11 03:49:00 | NOAA-20 | JARDIM DE PIRANHAS | RIO GRANDE DO NORTE | Brasil | 2405603 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7328ba5f-e511-3bc0-a003-f7944455a1d5 | -14.4632 | -45.68745 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |


[Clique aqui para ver as próximas entradas](README8.md)
