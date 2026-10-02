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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6a3221b-3fc3-3609-b3ef-f82fb07b8619 | -11.72503 | -43.57935 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| a9cfe0a2-6a8c-3ba1-90c6-62182dff36d4 | -11.16256 | -44.60538 | 2026-10-02 15:54:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| a2c0e5bf-8a2e-3f3b-a14f-dadf3a4da8aa | -11.16748 | -44.60149 | 2026-10-02 15:54:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4e647679-d47f-300a-8ce0-9e65ded52065 | -11.47179 | -43.42738 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 26840f31-0e29-389e-99e4-1ea3283fa9df | -13.36077 | -43.84391 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 96.4 |
| a2542c94-3d4c-3e8e-aa8b-dfb19ed3e24d | -7.60375 | -43.97614 | 2026-10-02 15:54:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| e3242313-0ffb-3b19-907e-634afe9f7075 | -10.86108 | -42.361 | 2026-10-02 15:54:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 8337eccf-c22b-3ee1-b058-b5c91df5947c | -11.36859 | -43.43209 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d373a818-2bbd-3d12-acc1-35ea4e2cf827 | -12.41845 | -38.39965 | 2026-10-02 15:54:00 | NOAA-21 | CATU | BAHIA | Brasil | 2907509 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| f7b8d531-2111-342a-8ed0-8e3e08a00953 | -11.47394 | -43.40416 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 153.5 |
| b8ad49d6-86c2-3e85-9ffb-8fa5f622d09d | -11.13829 | -44.58465 | 2026-10-02 15:54:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4384b609-81d9-36f9-9d18-98c8e53eb532 | -12.5248 | -44.1783 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| bce882cb-dde7-3dc0-ab2b-14e09c0e5489 | -11.74323 | -43.52124 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 31.3 |
| eb43dea1-b89a-3424-a209-ab305dc954cb | -11.71776 | -43.60306 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1410bb14-07a9-33db-86ca-8f305174c75c | -11.44632 | -43.39732 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 5cf2a40e-eb9e-37c9-ae11-47a1d7bd438d | -11.71282 | -43.60293 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| a65c7f08-7fe4-355c-8eab-9be29e29b087 | -11.1568 | -44.60267 | 2026-10-02 15:54:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8a3f9d9e-df10-3b53-894a-bade38e0a848 | -11.65864 | -43.61843 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 90638035-84da-3b4a-b483-39b7fc9317ec | -7.04412 | -36.89888 | 2026-10-02 15:54:00 | NOAA-21 | SANTA LUZIA | PARAÍBA | Brasil | 2513406 | 25 | 33 | nan | nan | nan | Caatinga | 5.4 |
| da1810e8-9a60-378e-889a-33854d0db2d6 | -9.09726 | -44.977 | 2026-10-02 15:54:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| d417695f-22b1-38df-b18d-b12abc79ba74 | -13.3391 | -43.8399 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 8abe29ff-ce45-350d-a8b2-6d7990a07703 | -8.8056 | -45.82416 | 2026-10-02 15:54:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 04c4d93c-85a3-30e4-86c0-b79955f0c2f3 | -11.67875 | -43.49717 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8310e534-6390-3b2e-9ed9-381486b13fac | -11.45416 | -43.40656 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 677ab2ac-57ce-3024-8405-75d0f770e6e1 | -11.27835 | -44.25044 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e1c77472-348b-30d0-b5f0-d9ba9eca744f | -13.33553 | -43.86197 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 11339909-6e75-3d85-a56f-b7cd803af900 | -11.77731 | -43.54945 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 321758b4-adda-3705-a5cc-722e7db889dd | -11.24187 | -44.30449 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| a7050c5a-1377-37ef-a58e-105c1e673c4f | -12.49507 | -44.1523 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 184.0 |
| 57cb50c1-f966-3b3d-99d2-ce2f01176c3f | -12.47765 | -44.14109 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8dadfb20-00f5-3b72-a025-941b5261849c | -11.12477 | -44.60648 | 2026-10-02 15:54:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cd8fb2d9-b7f6-3179-994b-866828e49139 | -9.93685 | -43.45781 | 2026-10-02 15:54:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 29.4 |
| a067d935-616f-377b-86c3-ede5bf673426 | -11.6068 | -43.52956 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 26d6ffab-dfa9-3473-b7d8-0c881db85d69 | -11.16214 | -44.60207 | 2026-10-02 15:54:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 89266e2f-f9d1-39ef-9d57-0282355b732a | -9.79152 | -44.7975 | 2026-10-02 15:54:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| bbeb2156-98cc-3932-9348-bf4adb34b945 | -11.70131 | -43.59293 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 922cb627-681f-33a5-8c06-f4dfc84cebc5 | -9.94315 | -43.468 | 2026-10-02 15:54:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 7919ce30-0f32-3950-a10a-c31ea64046ec | -11.62813 | -43.57847 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| cc58c6f8-e1f4-3e33-86f2-df724719df19 | -10.90596 | -43.83918 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| cb75e048-b226-3ad4-8345-8fb1c93ed666 | -12.48939 | -44.14964 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 351.5 |
| 1a16c920-e2e4-3ea9-bfd4-0012ebbf4c1c | -13.34475 | -43.85076 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| a68bb19d-cbdf-341f-9d99-8c73ce7cee62 | -11.72134 | -43.59075 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| c37a8a57-fd14-37db-abbf-0f86c8604c5e | -11.78232 | -43.54882 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 19094cd9-b421-3b17-b78a-85f3bc8ad89d | -11.67226 | -43.60511 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 01eb0a5d-d02a-3321-8d21-7402f61558d0 | -12.49994 | -44.14837 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 184.0 |
| 99623d50-0bd3-3786-82cd-428b14420207 | -11.6975 | -43.52099 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| d5076ff2-d3f0-3719-9089-b08d54b4f4c0 | -13.35107 | -43.85162 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 35.2 |
| e601eb4f-4ea4-3689-909b-cee92b28989c | -11.46545 | -43.41667 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| ad91e484-a90e-3a96-9909-92977884ad20 | -11.75811 | -43.43879 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 9ed47361-058a-33a0-94ab-4d50c5016851 | -7.08424 | -42.89709 | 2026-10-02 15:54:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| fb712408-4cbb-3a10-81e8-a036dccc01ac | -11.85425 | -44.7463 | 2026-10-02 15:54:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 0e1e2b11-89ea-3365-857f-f621cfcc23d9 | -11.64634 | -43.56138 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5b9a20b8-c0f2-33ad-8b24-6f825f22dde7 | -12.5276 | -43.10033 | 2026-10-02 15:54:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 16.9 |
| b8af33cc-a50a-394e-ac8f-cff5bfac9111 | -13.34215 | -43.86617 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1e479630-a0fb-3969-81b8-9b413ea26c87 | -11.81428 | -43.55953 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.3 |
| fefd83dc-a0f2-3835-a8a6-b1246fdbf3b6 | -10.9324 | -43.84533 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 51871400-b733-30dc-bccb-316b579532a2 | -11.72309 | -43.60493 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 127c9358-3025-369f-b66c-3bf2f51f10e0 | -11.14937 | -44.58673 | 2026-10-02 15:54:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| aabb0d06-dcf7-3f23-9238-7ec5f0201429 | -10.25742 | -42.53515 | 2026-10-02 15:54:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ce8d1b93-dcd9-31be-9bd4-2004c00e6308 | -11.26333 | -43.51442 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 5a4f6db4-523a-3722-bc30-8cc3bd28965d | -11.14445 | -44.59065 | 2026-10-02 15:54:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 3a2f6163-4661-3f5f-8b1d-ed6eabea8e9e | -12.81455 | -43.36227 | 2026-10-02 15:54:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| bac358b1-9f0d-3774-b0a8-61e449d8aaf1 | -7.48923 | -42.80687 | 2026-10-02 15:54:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 851d8ab0-ea33-308e-82fe-95412fe6d073 | -11.70496 | -43.62112 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 612780d2-7d17-3c55-8d45-2f41f3f77bc0 | -11.40254 | -43.36858 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c15e83b5-fcf8-393f-b317-ac59d499fdd8 | -8.21902 | -39.08213 | 2026-10-02 15:54:00 | NOAA-21 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 1d217b1c-8898-38c8-893c-75e81683ecbd | -11.65721 | -43.60711 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 82af7146-c15f-351e-9915-f45010f5fe3e | -11.26097 | -44.24682 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c6b913d4-f606-3f56-a59d-3538875eaa73 | -8.37155 | -36.96037 | 2026-10-02 15:54:00 | NOAA-21 | ARCOVERDE | PERNAMBUCO | Brasil | 2601201 | 26 | 33 | nan | nan | nan | Caatinga | 70.7 |
| 855240d3-c789-3c6f-b67d-9075141363df | -12.53176 | -43.09367 | 2026-10-02 15:54:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 41.2 |
| 573b40d9-afd6-3e5b-b3ff-3e08b63c2fdb | -11.47669 | -43.51448 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 977e4085-9710-3147-849d-70d1def50594 | -11.715 | -43.58065 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 802de61a-f8ac-37b7-bcc3-2f96e18255a8 | -11.73751 | -43.43567 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 53.8 |
| fcfa4d9a-3a20-36a8-b9ca-89e47998129e | -11.72635 | -43.59003 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| c124d6db-e02f-3620-9ecb-c2fa6da12f27 | -10.70207 | -45.32103 | 2026-10-02 15:54:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 58a17e94-936c-353e-aa78-5e4d6d336823 | -12.5048 | -44.14444 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 124.3 |
| bbd124d5-6f62-34fa-9109-49d96583a0bc | -11.14978 | -44.59003 | 2026-10-02 15:54:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 735f5836-7e06-3de3-ab82-91d5f3880f4f | -11.27382 | -44.29995 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dea01827-5406-3e75-8ed0-d776a8cf3c5d | -11.47889 | -43.40354 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 153.5 |
| fc3c62a7-f882-3131-bf14-e7064545320e | -11.81465 | -43.56244 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 503a9589-e85b-3bf0-ac97-9f83c8930609 | -11.4704 | -43.41608 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 8a0e892c-3d0c-3bc1-a40b-a01069ace565 | -7.48538 | -42.81186 | 2026-10-02 15:54:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 18dff35d-d588-3892-8bb4-7194e3794aae | -11.74705 | -43.59233 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6a6ea10d-e9c4-3237-b64b-7d5731a410eb | -8.36822 | -36.96088 | 2026-10-02 15:54:00 | NOAA-21 | ARCOVERDE | PERNAMBUCO | Brasil | 2601201 | 26 | 33 | nan | nan | nan | Caatinga | 70.7 |
| 4479fd2d-5988-3d01-8b31-a67d4572644b | -10.91643 | -43.84083 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ae218f58-c91a-3ba5-b5a0-ca5971aafc7e | -11.50439 | -43.52743 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 29011f00-c41e-3f7c-87fb-05224c6d3ee9 | -9.85381 | -44.82703 | 2026-10-02 15:54:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 002b50ca-fd8b-3acc-b79d-f7020dfe57e7 | -11.61109 | -44.13458 | 2026-10-02 15:54:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 35b32587-8431-3db9-9cc4-574f46a1e66a | -11.65502 | -43.58981 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 82828109-e06f-3180-bc3a-201f04471cd7 | -10.52687 | -43.50231 | 2026-10-02 15:54:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 4c14ac1b-7f6a-32ac-a1a6-576d95b0ed5a | -11.47744 | -43.40498 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 4f223d13-143b-3105-a22b-50cb73e8d8a6 | -11.11733 | -40.93722 | 2026-10-02 15:54:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 99e8d4d7-1d6d-3713-98f4-38513c37833f | -11.80922 | -43.55854 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 3a31daac-1cc0-33ff-aa89-884221a7df28 | -11.72572 | -43.58488 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e1336562-536b-3801-8ccf-76ed22185521 | -11.79845 | -43.5554 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| fe54be15-2582-34a7-b7da-2cbd0a4ccefb | -8.86544 | -40.87056 | 2026-10-02 15:54:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 30a895a3-41a5-37c5-9c89-cc1522cfdd36 | -11.72037 | -43.58282 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e78bef5d-914b-3098-90ef-3cc98de64a83 | -11.74195 | -43.5111 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.6 |
| b22b753a-94c5-35b1-9d25-2777377bd4f1 | -11.27465 | -43.56509 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| f8df2ff6-1eed-3c3a-8dcb-32c4e31a609e | -11.48233 | -43.51273 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |


[Clique aqui para ver as próximas entradas](README102.md)
