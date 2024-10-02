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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f984f9e6-f54a-3de8-9852-97c989f31833 | -7.76261 | -43.05063 | 2024-10-02 03:30:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a453eb6e-2f34-3b1c-94cd-ea30cd1b7ab5 | -7.76179 | -43.05499 | 2024-10-02 03:30:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a0731afc-05b7-34db-aa0b-f615ce3824a1 | -7.75991 | -43.04763 | 2024-10-02 03:30:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f3825736-f94c-3ca6-bb09-fcb056c0e725 | -7.75912 | -43.05199 | 2024-10-02 03:30:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ead530af-c92a-3406-92e8-f124a701787d | -7.75669 | -43.04953 | 2024-10-02 03:30:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 78e4276f-c9c2-3dfa-b2c5-856801c8ea01 | -7.70941 | -42.98954 | 2024-10-02 03:30:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 6251c691-63c9-3360-ba35-e19cd5f5f5d3 | -7.70864 | -42.99367 | 2024-10-02 03:30:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 4fc6b63a-952c-3366-975b-3e32669e8371 | -7.70786 | -42.99789 | 2024-10-02 03:30:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 1963c0ac-8a0a-3628-afb0-ebfe990f60af | -7.70275 | -42.9925 | 2024-10-02 03:30:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ca95589a-cced-3d58-8d9d-65ca7d9e66a0 | -7.70193 | -42.9969 | 2024-10-02 03:30:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| fd949b1b-3a77-35b8-a0a6-bac1439705dd | -7.64793 | -42.44945 | 2024-10-02 03:30:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c52735f1-33c5-3838-957c-f0da513a1a8e | -7.64147 | -42.45257 | 2024-10-02 03:30:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| daa398e0-67ba-318a-bea7-e44641098322 | -7.64075 | -42.45655 | 2024-10-02 03:30:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0858253a-3c76-31aa-a3c1-b5aa325c9ff4 | -7.63573 | -42.45163 | 2024-10-02 03:30:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 51a93689-0803-32c2-9176-30008348a2a2 | -7.63501 | -42.45559 | 2024-10-02 03:30:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| eaaed134-7ccd-3c31-b1d3-f797838821b6 | -7.50327 | -43.91995 | 2024-10-02 03:30:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7609e129-63c8-3beb-89e0-7fe16ae63806 | -7.50238 | -43.92462 | 2024-10-02 03:30:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95209b52-5131-3579-9462-cdb709070d59 | -7.44258 | -44.85057 | 2024-10-02 03:30:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b1e7ffe-2b71-3b1c-9ef1-6f70625e0295 | -7.44153 | -44.85625 | 2024-10-02 03:30:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a7b4cf1-7a34-3596-a77f-02050820a949 | -11.25384 | -38.0043 | 2024-10-02 03:30:00 | NPP-375D | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9816b942-7e78-37dd-96a3-5b90a82e4131 | -10.9317 | -38.81466 | 2024-10-02 03:30:00 | NPP-375D | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| baed48dd-79bb-39c3-9d74-6bbc6771a8f2 | -12.44303 | -43.72921 | 2024-10-02 03:30:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c67d30c7-31d6-304f-a637-bf6e83f262b6 | -12.44225 | -43.73321 | 2024-10-02 03:30:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b9b04283-4d21-3a5d-b192-83bb82a65fc7 | -12.43736 | -43.72794 | 2024-10-02 03:30:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d262d84c-fb46-3b3f-95d4-feddaeaa632e | -12.43657 | -43.73195 | 2024-10-02 03:30:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 931c9039-c11a-3c43-bbd4-64e059c7fa09 | -12.14313 | -40.89939 | 2024-10-02 03:30:00 | NPP-375D | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 58cc1b9e-c9ec-3b1c-ac6d-227f7adf6c00 | -12.14218 | -40.90039 | 2024-10-02 03:30:00 | NPP-375D | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dda770f9-a77c-36b3-bab1-cdb782d36609 | -12.1384 | -40.89827 | 2024-10-02 03:30:00 | NPP-375D | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bdaa4600-2f76-32c2-9900-209f93b114a9 | -11.88251 | -43.8128 | 2024-10-02 03:30:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| cc6baf67-f70a-3885-9a8b-d43a7c9ee931 | -11.88169 | -43.81699 | 2024-10-02 03:30:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| cdca8445-26d2-3f27-96bf-3aedb2d84ced | -11.87673 | -43.8116 | 2024-10-02 03:30:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f08457d-10dc-3438-8723-1096becff09a | -11.56083 | -42.18209 | 2024-10-02 03:30:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| aafd8fb8-25ef-3fe4-b825-20f9888919a5 | -11.56023 | -42.18527 | 2024-10-02 03:30:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f20b51ad-e0df-3dc2-8456-149b9bbf5bde | -10.87331 | -45.96753 | 2024-10-02 03:30:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10894146-b9bc-3d50-a75e-3a6356314c5f | -10.86662 | -45.9661 | 2024-10-02 03:30:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db0200d3-f0ec-3517-8145-eadf10b30741 | -10.71199 | -46.1735 | 2024-10-02 03:30:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f6f8c279-2b07-3685-8b50-d4343c87158e | -10.71186 | -46.17556 | 2024-10-02 03:30:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 246accdf-7079-3676-86e9-04c70f90e0cd | -10.70634 | -46.16637 | 2024-10-02 03:30:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3c88ba62-8e30-309b-9f56-f9f83a78c74a | -10.70627 | -46.16836 | 2024-10-02 03:30:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6bf04529-8acc-362b-b233-8084ae275626 | -10.69963 | -46.16455 | 2024-10-02 03:30:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4689526-0226-3bb7-b5ec-abe6b1c74ea0 | -10.69581 | -37.05122 | 2024-10-02 03:30:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e0da5509-642e-327f-becd-618854d1a80e | -10.69409 | -46.15691 | 2024-10-02 03:30:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5383363-04dd-3a28-b37f-c207dcaca05c | -10.69404 | -46.15907 | 2024-10-02 03:30:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea667d49-e35d-3eb1-8370-0ab5e416bfc3 | -10.68851 | -46.1516 | 2024-10-02 03:30:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b492cd60-44a3-33c8-a31b-792e65207f2e | -10.68739 | -46.15508 | 2024-10-02 03:30:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4cc24d5-dd67-3c2e-bb2e-85dfd44a06f6 | -10.68296 | -46.14198 | 2024-10-02 03:30:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0173c013-0666-306e-971f-dacfbfde816d | -10.68295 | -46.14433 | 2024-10-02 03:30:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61d9c36d-3d01-330e-b536-fdf8f8c7680e | -10.67622 | -46.14037 | 2024-10-02 03:30:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc62afa7-0854-3d66-a815-463eb8a18276 | -15.37225 | -47.42756 | 2024-10-02 03:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b10590bd-2fa5-30ee-b02c-db91794e3a4a | -16.68876 | -47.82193 | 2024-10-02 03:32:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bd9117e1-47cf-38b4-8427-9955e60ddc1d | -21.61768 | -42.82694 | 2024-10-02 03:32:00 | NPP-375D | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c48ae4fb-5aec-34ac-845d-2364c368ac2d | -21.61743 | -42.80457 | 2024-10-02 03:32:00 | NPP-375D | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 562bf128-f6f4-3d15-b3bc-623b0b4da62c | -21.61622 | -42.8106 | 2024-10-02 03:32:00 | NPP-375D | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 01395d9d-208b-36b3-a045-730620ba1e70 | -21.61318 | -42.82577 | 2024-10-02 03:32:00 | NPP-375D | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d9935eea-7795-3cd4-9715-c55496bef20a | -21.61275 | -42.80436 | 2024-10-02 03:32:00 | NPP-375D | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ec996e74-0b2c-3c5a-9295-6664dc9acbc6 | -21.61166 | -42.80975 | 2024-10-02 03:32:00 | NPP-375D | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5a432df5-8325-3335-a496-2b0b870343e8 | -21.59818 | -41.30742 | 2024-10-02 03:32:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7a9d8535-d0c3-3111-a6b1-9c724fa59fad | -21.59742 | -41.31141 | 2024-10-02 03:32:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5096d551-4191-3e00-ae67-48eaca7bdab2 | -21.56445 | -41.30389 | 2024-10-02 03:32:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 89a999d9-1f7d-3ef5-ad81-1f7ffe35a070 | -21.48736 | -41.16049 | 2024-10-02 03:32:00 | NPP-375D | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3454fd54-2296-3420-addf-93b4a1bf5104 | -21.32521 | -41.41582 | 2024-10-02 03:32:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| ce044b44-c012-3ad8-8efd-af8f41977a59 | -21.32188 | -41.41054 | 2024-10-02 03:32:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| df7104fc-00cb-3798-9cbd-d7c1cff990ca | -21.32108 | -41.4147 | 2024-10-02 03:32:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| cdb4eae7-7b46-39b2-9c5b-e7b3371169f9 | -21.32021 | -41.41914 | 2024-10-02 03:32:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 84896c91-d8c2-3b0c-8cdb-64fb51b4e5ea | -21.31603 | -41.41827 | 2024-10-02 03:32:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 740f591e-7a1b-38d9-b37c-04f4f17527f3 | -21.15706 | -41.94926 | 2024-10-02 03:32:00 | NPP-375D | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ce954d93-7d41-3a26-8820-afd587d68e12 | -20.97361 | -43.30062 | 2024-10-02 03:32:00 | NPP-375D | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| af9920a0-68ee-3f32-8a7e-c450ec021681 | -20.93348 | -42.93707 | 2024-10-02 03:32:00 | NPP-375D | SÃO GERALDO | MINAS GERAIS | Brasil | 3161502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0993ab4d-a371-3c85-ad8b-a33b7c143360 | -20.92884 | -42.93608 | 2024-10-02 03:32:00 | NPP-375D | SÃO GERALDO | MINAS GERAIS | Brasil | 3161502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| aa1daa5a-fa10-3abf-bd84-bd83448263d8 | -20.92245 | -41.83079 | 2024-10-02 03:32:00 | NPP-375D | VARRE-SAI | RIO DE JANEIRO | Brasil | 3306156 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 31457926-ca85-3854-a9b3-eea3a519a997 | -20.86672 | -45.25457 | 2024-10-02 03:32:00 | NPP-375D | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 01a1da1f-02b6-3c6c-823e-b7e97240a8d6 | -20.8659 | -45.25836 | 2024-10-02 03:32:00 | NPP-375D | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 192adaeb-f9eb-3851-b1e5-40b92cc7f1ca | -20.8622 | -41.67551 | 2024-10-02 03:32:00 | NPP-375D | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 63e5c9f4-e161-34b2-a6ee-f6057967fa31 | -20.86138 | -45.25332 | 2024-10-02 03:32:00 | NPP-375D | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 23837264-8e35-3351-965c-9667eb6696f8 | -20.86134 | -41.67995 | 2024-10-02 03:32:00 | NPP-375D | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3d3c6629-0268-360d-bfac-8b7332f41ec8 | -20.85794 | -41.6745 | 2024-10-02 03:32:00 | NPP-375D | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0298cfa8-be03-316a-8ebc-6d757da66e0c | -20.85708 | -41.67893 | 2024-10-02 03:32:00 | NPP-375D | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| acb14e09-15c5-3006-976f-03fc808a816b | -20.82051 | -42.29993 | 2024-10-02 03:32:00 | NPP-375D | SÃO FRANCISCO DO GLÓRIA | MINAS GERAIS | Brasil | 3161403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9646f49b-b58f-3894-90b4-6054bc6d7ddc | -20.81612 | -42.29867 | 2024-10-02 03:32:00 | NPP-375D | SÃO FRANCISCO DO GLÓRIA | MINAS GERAIS | Brasil | 3161403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 787c84c4-cf45-3369-ba6e-0b17b0473211 | -20.81535 | -42.18698 | 2024-10-02 03:32:00 | NPP-375D | PEDRA DOURADA | MINAS GERAIS | Brasil | 3149002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 37042c3d-8442-3235-9c32-c7923da1deb2 | -20.81173 | -42.29741 | 2024-10-02 03:32:00 | NPP-375D | SÃO FRANCISCO DO GLÓRIA | MINAS GERAIS | Brasil | 3161403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 90f52dba-3597-3bec-a0e7-824f172c0de9 | -20.81071 | -42.30247 | 2024-10-02 03:32:00 | NPP-375D | SÃO FRANCISCO DO GLÓRIA | MINAS GERAIS | Brasil | 3161403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 9c19e750-ada2-3ff2-b9ed-849010f9c5d6 | -20.64655 | -47.04198 | 2024-10-02 03:32:00 | NPP-375D | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 572c6c4f-97da-3793-8c3e-7c2a6008863e | -20.64547 | -47.04665 | 2024-10-02 03:32:00 | NPP-375D | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8d713185-142d-3ee9-addf-2bbe5cfa36a8 | -20.64479 | -47.04499 | 2024-10-02 03:32:00 | NPP-375D | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f9bfa5f3-615f-3def-a0bc-f9d6829888e0 | -20.63018 | -46.77834 | 2024-10-02 03:32:00 | NPP-375D | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5da7a8c4-fff1-3bb9-8025-6c265089365f | -20.53366 | -46.27171 | 2024-10-02 03:32:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f7216e0a-ee84-31fc-aca6-951e6c866eef | -20.53272 | -46.27588 | 2024-10-02 03:32:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 296b3b00-3dd8-33d0-98d6-40c4adde2518 | -20.52805 | -46.26983 | 2024-10-02 03:32:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2b79be7f-d384-30fe-a1b1-3ac107dc0298 | -20.52702 | -46.27447 | 2024-10-02 03:32:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0975a923-9f27-354f-872e-ce88ebce8f7b | -20.52596 | -46.27919 | 2024-10-02 03:32:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fc7c23f6-72c2-3404-8f73-d097df406d4e | -20.52501 | -46.31031 | 2024-10-02 03:32:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d8d0d945-5e23-357e-a684-704795b948b2 | -20.52496 | -46.28363 | 2024-10-02 03:32:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2300b5ea-bb69-3159-94a6-7ec52d2aafac | -20.52413 | -46.31421 | 2024-10-02 03:32:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 65b585fe-57e4-3ba9-899d-0fa78a43abd4 | -20.52333 | -46.31778 | 2024-10-02 03:32:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| f0f29d58-ecfb-3409-b71a-0befb31e5b7e | -20.5225 | -46.32147 | 2024-10-02 03:32:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| fd5a66e8-9c3c-3075-99cc-fc769f6f65b4 | -20.52217 | -46.26921 | 2024-10-02 03:32:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fb17e2a8-8218-3dbf-919e-09bc98f8cdcb | -20.52117 | -46.27368 | 2024-10-02 03:32:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 54504768-fc17-367d-9a93-ba4f858fca3f | -20.52013 | -46.27832 | 2024-10-02 03:32:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f2fd9059-675f-39ad-94d2-2f4ed0037f55 | -20.51913 | -46.28278 | 2024-10-02 03:32:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README53.md)
