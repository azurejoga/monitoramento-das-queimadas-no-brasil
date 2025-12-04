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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 249fd02a-b37e-36e9-b29e-eed81bdb72be | -4.39257 | -43.13175 | 2025-12-04 04:48:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d2987816-79ed-3db0-9771-8c0f0f7ea651 | -1.35565 | -53.22707 | 2025-12-04 04:48:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7c830e43-c0ee-37d7-a7ff-c9328a401a2e | -4.21393 | -46.35777 | 2025-12-04 04:48:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7ee2d95-0daa-3091-8195-d9b59b6f0502 | -3.76792 | -51.19399 | 2025-12-04 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4450e8f-3d55-36e9-b6fb-ddd797411e89 | -1.12551 | -54.19378 | 2025-12-04 04:48:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d66c6a9-8825-399d-bb75-0d40ce2d993b | -2.14728 | -47.87851 | 2025-12-04 04:48:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 310db8d0-a88f-39d4-be65-5114f4607a77 | -4.06663 | -46.56242 | 2025-12-04 04:48:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 3aba1178-1896-3c31-8ce4-86507c850d3b | -4.55388 | -45.80561 | 2025-12-04 04:48:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c1b96003-517a-343e-84e3-21a1fa015e75 | -1.98584 | -47.96651 | 2025-12-04 04:48:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5be844ed-e10e-3046-a244-f1936f21ef92 | -2.06325 | -45.35603 | 2025-12-04 04:48:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7a6553b-7758-364c-9636-ffa34b0384ca | -1.50253 | -52.03698 | 2025-12-04 04:48:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cac32a4f-f826-34e4-b264-62db448a4b52 | -1.42386 | -53.00732 | 2025-12-04 04:48:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8877d8f-b844-3a9f-ac0e-f0bf67a51d97 | -4.48895 | -45.28163 | 2025-12-04 04:48:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86f6e91c-be29-3c81-bb6a-e7ab474dbc9c | -2.14508 | -47.87787 | 2025-12-04 04:48:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 071736e6-f45d-3214-ba30-bf2f7fc8c6df | -2.6351 | -48.036 | 2025-12-04 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9829b065-875d-384f-ae67-71b799d40bbf | -2.70457 | -49.30922 | 2025-12-04 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cabab6fe-b3a6-378e-bffc-833bc311ea16 | -4.38521 | -46.66977 | 2025-12-04 04:48:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 239e5bd2-0f21-36a7-b15b-eb26155fae62 | -4.50406 | -45.77306 | 2025-12-04 04:48:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8a9dcccc-c577-342d-a0be-ed4bc36d6d6a | -2.60752 | -49.25826 | 2025-12-04 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9551f0c4-c58a-3068-8013-359b2f8f271d | -2.47199 | -47.83269 | 2025-12-04 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d26db1f-dc59-3892-ba29-70966112ee5f | -4.85998 | -42.4766 | 2025-12-04 04:48:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ff1d4eb0-0868-33d0-b620-0c7586deb4e5 | -2.07917 | -48.37157 | 2025-12-04 04:48:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0afdd070-b9a0-31ae-b21b-d4f9cf60b85f | -2.24335 | -47.98944 | 2025-12-04 04:48:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69bdef4c-e98a-31b6-9577-d360b2fe77e3 | -2.96966 | -49.62254 | 2025-12-04 04:48:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71d60054-1f02-381a-804e-b21e5b842da8 | -3.37988 | -49.25484 | 2025-12-04 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e8d551b-8b98-372f-8704-6fc7a5baa1b3 | -2.59583 | -49.26723 | 2025-12-04 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70b5fc6b-f3a6-3b8f-ac14-851c568be75c | -0.37048 | -52.04749 | 2025-12-04 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2db39b86-bbb1-33a9-9d9f-bb72cc838931 | -3.3647 | -46.85661 | 2025-12-04 04:48:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20a569b7-d7fb-3aec-b09f-fa2efd394443 | -4.26199 | -44.15178 | 2025-12-04 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6c6cfc50-21e3-3d6d-83a4-e321e6656808 | -2.49198 | -47.82708 | 2025-12-04 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 24f2d73b-e65f-320c-b8ef-84f3ec581ea0 | -3.1882 | -46.60319 | 2025-12-04 04:48:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 915b15a6-b697-3ade-b2eb-a3bc578fccec | -2.82925 | -48.44342 | 2025-12-04 04:48:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab990d5a-00f2-34fb-ad64-47903f13bafb | -4.38903 | -46.66804 | 2025-12-04 04:48:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7a3c5a59-42c7-329d-b29b-2befda1ab9e0 | -4.40216 | -43.13319 | 2025-12-04 04:48:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 1a5a03b2-8caa-396e-bdc8-5ee908b60d2d | -2.49212 | -48.14575 | 2025-12-04 04:48:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 209c1948-bf9f-312b-ad26-11478a37e455 | -4.52318 | -44.65709 | 2025-12-04 04:48:00 | NPP-375D | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc47e4df-5bd3-3a51-acb7-c4f36e115520 | -2.78909 | -48.90174 | 2025-12-04 04:48:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 495756f5-6d25-362c-bfce-3f1c33688059 | -1.75003 | -46.19997 | 2025-12-04 04:48:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7fc9370-2b0a-3ac9-bfc2-3b5b07e915f4 | -2.07633 | -48.36738 | 2025-12-04 04:48:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69b34434-0f16-3393-a9d0-bd17921f5cbb | -2.53634 | -49.45867 | 2025-12-04 04:48:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d6e8150f-8907-3c7f-8ba6-9d38ae197f7b | -0.55225 | -51.78094 | 2025-12-04 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8155c225-f121-3eed-b28b-78ae86d54ca1 | -2.38149 | -49.38411 | 2025-12-04 04:48:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f75e9bf-04e7-3d2d-b676-73eca1def9b8 | -2.13914 | -47.885 | 2025-12-04 04:48:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7469d87-319c-35b5-8af4-cb887862a0b4 | -4.58517 | -45.1032 | 2025-12-04 04:48:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f77cce95-917f-34c5-893c-4629babde394 | -4.00655 | -46.54907 | 2025-12-04 04:48:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f7e812f-6c61-3aad-9a7f-e074c4d9bb17 | -2.42217 | -48.59116 | 2025-12-04 04:48:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1054ba92-3592-3fe5-98a0-38144f1f4a93 | -4.03384 | -46.97758 | 2025-12-04 04:48:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e37de87-6f70-39de-887f-d717178caac8 | -2.94494 | -48.59599 | 2025-12-04 04:48:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 417d3d7a-fd0a-34bd-8526-06a3d343861e | -3.60446 | -45.66653 | 2025-12-04 04:48:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f450fb73-f70f-3b62-9ad8-2492eb7cd079 | -5.02187 | -41.00927 | 2025-12-04 04:48:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4fdf8968-2554-3b03-997e-f3a363914396 | -1.12384 | -53.44323 | 2025-12-04 04:48:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a9d0ce4-8d0c-3da1-82bd-2c8bc6b14670 | -4.2155 | -46.35992 | 2025-12-04 04:48:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f4144c48-74fe-3bfd-9a2c-fec2d529ff68 | -4.05113 | -46.61226 | 2025-12-04 04:48:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4227a035-6bbd-34b7-ae5b-289a4a6ecba7 | -3.33044 | -45.02157 | 2025-12-04 04:48:00 | NPP-375D | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38955f76-af74-30fb-8d85-357f4ba410e7 | -0.41221 | -51.62646 | 2025-12-04 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d7e307a1-310f-3342-b023-e60ea6057520 | 0.32344 | -49.73206 | 2025-12-04 04:48:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd403330-1227-3afe-9f4b-710e9da83ead | -1.83695 | -46.58817 | 2025-12-04 04:48:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d26d2767-e5e5-3c0b-a8e0-8a1182dc7582 | -2.88934 | -45.38179 | 2025-12-04 04:48:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b8266e20-57e0-3d01-912e-d28dadc533d8 | -2.97245 | -49.62654 | 2025-12-04 04:48:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b8d2584-02c5-3661-916f-494a6793d14a | -1.18601 | -49.04832 | 2025-12-04 04:48:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8e53dbe-96fd-3b1b-a3ac-4f80e5afc8b9 | -2.54179 | -45.36862 | 2025-12-04 04:48:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d4286ff7-8291-33a9-9b3a-d51bcecd7a0c | -4.50855 | -46.08074 | 2025-12-04 04:48:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac0ac6c6-4288-3e57-a465-2cfea38f8cd5 | -4.39682 | -45.83342 | 2025-12-04 04:48:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bda5a23a-7d48-3644-8986-ff963885b34d | -2.69728 | -49.1677 | 2025-12-04 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a573fd98-9f47-3817-9fa0-74640cbf6b65 | -2.79247 | -48.90226 | 2025-12-04 04:48:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c52268b4-1a09-3b01-be48-ddb647595431 | -2.56381 | -49.06758 | 2025-12-04 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6db43c56-23a3-38c9-86fd-939f1e41e8a1 | -2.88345 | -48.45553 | 2025-12-04 04:48:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56ac4d19-15a1-398e-93b1-b5be69550b09 | -2.41851 | -45.79518 | 2025-12-04 04:48:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e7fcc8b3-1b7f-3797-baa4-6970b38cd837 | -2.56797 | -47.15641 | 2025-12-04 04:48:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca6ba869-1809-33fd-ab2a-52750b2b60b5 | -4.52946 | -44.10635 | 2025-12-04 04:48:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d86493e0-11d4-3f0d-8e5c-ef50c31d31c8 | -1.35753 | -46.46088 | 2025-12-04 04:48:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aad6a641-0cf3-356f-84b6-02aca0dcc598 | -3.60368 | -45.67167 | 2025-12-04 04:48:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e463331-d13d-3b1a-b798-bda4ba8cbdfc | -2.63009 | -47.31102 | 2025-12-04 04:48:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2f70c1df-6b96-3044-9231-4661260f1e25 | -3.38836 | -47.27622 | 2025-12-04 04:48:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1a8d3db-fe18-3a9f-87c1-1ca45ef638fd | -3.66191 | -43.60552 | 2025-12-04 04:48:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bce0b527-881b-39e8-b688-c897ea61ac74 | -3.22109 | -48.616 | 2025-12-04 04:48:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1052546a-bc92-3108-ac45-427eece35d50 | -4.04735 | -46.61167 | 2025-12-04 04:48:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bab2516c-2c21-3281-a622-55de608d9e49 | -2.47787 | -47.65908 | 2025-12-04 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 27d942a7-3551-33f8-9603-9767d40f3146 | -3.38435 | -49.24828 | 2025-12-04 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c71ad435-7adc-3679-9999-79c93b4fc335 | -1.16353 | -48.86531 | 2025-12-04 04:48:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c3823f48-2784-353e-933e-8651c9b1fc6a | -3.66154 | -43.60234 | 2025-12-04 04:48:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b425e855-df58-3b49-a514-a403df67c9fc | -1.6962 | -46.14996 | 2025-12-04 04:48:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff2e7f69-3136-349d-9a31-450be560638c | -2.59917 | -49.26775 | 2025-12-04 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cda8a1fd-8b9d-3ebf-9222-1f0641e951b4 | -2.49912 | -47.26723 | 2025-12-04 04:48:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d068fc52-4a64-3a58-86f0-87f5c8f14ef8 | -4.11687 | -47.29154 | 2025-12-04 04:48:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fdfad37d-a9e1-381b-bc04-225dc1b1503f | -2.87678 | -46.80212 | 2025-12-04 04:48:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c17c6a48-d5bc-3571-a1ab-483fac993aee | -4.831 | -43.19854 | 2025-12-04 04:48:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff62b516-7f89-3175-9f5e-a99d94c7929f | -3.40926 | -44.99096 | 2025-12-04 04:48:00 | NPP-375D | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 3f2ce564-f694-3086-ba57-3aa9cd7018a4 | -4.40079 | -45.83416 | 2025-12-04 04:48:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6edcc313-6343-3482-b4c3-f8b1e5faca71 | -4.40147 | -45.38542 | 2025-12-04 04:48:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a271790-f768-348a-9028-c6e6690d290e | 0.18475 | -50.03239 | 2025-12-04 04:48:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a560961-3be2-3605-9ffe-6d449e09155b | -3.7251 | -45.58329 | 2025-12-04 04:48:00 | NPP-375D | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61b7c790-1a5c-3602-ba9d-fb349c640ddd | -2.14381 | -47.87796 | 2025-12-04 04:48:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb682368-c25e-33ca-be94-8614b9aea91f | -2.63367 | -47.31157 | 2025-12-04 04:48:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 71776444-cf2f-37d4-8df4-3784f2a3fb06 | -2.57669 | -49.09493 | 2025-12-04 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 11591bc1-064f-37b4-85a3-542f50ccc018 | -2.79085 | -47.43293 | 2025-12-04 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81fad6eb-012d-3510-afd2-6458aa6dc0d7 | -1.1099 | -53.65296 | 2025-12-04 04:48:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af6e4b8b-750e-33ac-a825-a4760a16ba4b | -2.53842 | -45.37126 | 2025-12-04 04:48:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 18.7 |
| adc68115-c0e0-3a85-9e2f-8940e6c9da02 | -4.56948 | -43.80941 | 2025-12-04 04:48:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5a2f649d-9d2a-3038-8747-a4424a17cbc8 | -4.0308 | -47.3403 | 2025-12-04 04:48:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README15.md)
