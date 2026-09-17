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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10ea9560-d62b-36cd-bd21-e2c0388fc7d7 | -8.68894 | -44.87286 | 2026-09-17 03:55:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c77f68e-2d98-3f91-a1ba-e7e4833d98cb | -12.44204 | -50.84818 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d3b12edf-9b86-3ecb-9f0e-570ead3a8800 | -11.88369 | -47.58661 | 2026-09-17 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3aa5a24-984a-3b72-954c-0c7805b34d5e | -11.19099 | -42.85846 | 2026-09-17 03:55:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 89b42be1-4390-315b-976c-88271b04ef3e | -9.61725 | -45.35603 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 83473235-524b-3bac-934a-50dd2925b8ca | -9.83897 | -48.37471 | 2026-09-17 03:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| afaffbdb-a65d-3f42-9a18-333ce31827c7 | -11.89042 | -47.60942 | 2026-09-17 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65a63efb-ab97-3dc9-9deb-71497ba4765e | -7.07247 | -47.48858 | 2026-09-17 03:55:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| daeb6929-c67b-3407-8a50-1e13f145dbee | -12.45807 | -50.80047 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 0081f36d-e8f6-358d-8d3c-c3b68f0132cc | -8.86414 | -45.88597 | 2026-09-17 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d3e7422d-ae41-3fe8-8466-dc1301c54c7f | -9.87292 | -48.38586 | 2026-09-17 03:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 2492df6a-829c-38d0-8536-979e61c60c3d | -13.73902 | -39.01183 | 2026-09-17 03:55:00 | NOAA-20 | ITUBERÁ | BAHIA | Brasil | 2917300 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 9ebc1642-e998-338b-861f-48cfc31701b2 | -11.48907 | -45.73964 | 2026-09-17 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 183c6ffd-f5df-375a-bda6-01074e55fba8 | -12.44385 | -50.87152 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3ceb3267-0ca2-3868-9d2a-2d3f717f17e4 | -8.78688 | -46.91005 | 2026-09-17 03:55:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 88e88de0-9aa7-3d8d-b602-142137a61e6d | -9.61766 | -45.35305 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b5b6df09-c492-38b4-8268-7f5e87f9b629 | -7.46389 | -42.10492 | 2026-09-17 03:55:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 64b6ab11-811b-3b5c-84be-80a2690246b1 | -7.58147 | -46.33641 | 2026-09-17 03:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 63faab10-0c05-358f-9917-de22e745dea0 | -8.25062 | -42.16758 | 2026-09-17 03:55:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 96fcd291-a2dd-3845-b343-fcc04672f8db | -9.61049 | -45.36646 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 33e9ad15-d545-35af-aa2a-0ce4affdb360 | -11.32955 | -47.25214 | 2026-09-17 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a5e0623-52a0-3d19-bda3-78c43b2a8276 | -11.48137 | -45.77874 | 2026-09-17 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 713e7dba-5005-3043-b922-de904dc218c2 | -9.86289 | -48.37537 | 2026-09-17 03:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 95efe7a5-7821-33f6-8429-9ae049934111 | -12.47826 | -50.86771 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 21.0 |
| d1327612-ba7d-3761-9fa6-95f98db77bbb | -11.89478 | -43.82502 | 2026-09-17 03:55:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d2bd940-dd64-3fb1-a39e-5e82f97cb214 | -13.60803 | -40.0924 | 2026-09-17 03:55:00 | NOAA-20 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 4dff6bb9-e0fb-3529-b5d8-56d9987c4667 | -12.42675 | -48.48826 | 2026-09-17 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe7775d5-ca63-332e-898c-35fb820691dc | -12.47598 | -50.87869 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 51bb8579-26c4-3d3a-a2f9-5594cc76f6c1 | -8.02026 | -45.48027 | 2026-09-17 03:55:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 17e03848-7b6a-3342-8089-aec354aaa7c0 | -8.60806 | -44.50022 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 84763aed-392c-3237-9b98-50f0c116f200 | -8.46602 | -44.55606 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 12edbea0-05b6-372c-a769-946972552d10 | -12.4606 | -50.82372 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 59.2 |
| b38edc54-63e4-3fcb-a13d-d6426e71838e | -9.56693 | -46.58379 | 2026-09-17 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b4822ebe-6aa3-32ba-9abb-2497c5d0fbb5 | -12.46381 | -50.90477 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| acbca95b-f4ed-362f-99a8-1f1d980cfaec | -11.33664 | -47.2436 | 2026-09-17 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 230c95b5-a382-3f1c-8a5d-b06fc1b06740 | -11.34591 | -44.0028 | 2026-09-17 03:55:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71ae9a58-17ea-3544-8347-90e39bd3e8ed | -12.95414 | -48.61586 | 2026-09-17 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07ccb10d-a6a2-3c50-877a-94d1c86abdd8 | -11.89558 | -47.58212 | 2026-09-17 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 960b50a3-c134-3b76-baac-76adb28dc799 | -12.44893 | -50.87858 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f7249c08-f81f-3c6b-a2a0-31545ce775ed | -9.35808 | -36.94949 | 2026-09-17 03:55:00 | NOAA-20 | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 97e304c8-e1af-396f-9b08-c9896352eac8 | -8.7867 | -46.89865 | 2026-09-17 03:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70575187-ffa7-37a1-b339-4a4c124119a0 | -11.34379 | -43.99 | 2026-09-17 03:55:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2830949-585e-3fcf-9a3d-59cefa2bc3f1 | -9.89035 | -48.38906 | 2026-09-17 03:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3b051ee3-f3e6-3eec-9530-73c9f5a053de | -7.38125 | -44.49482 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d33f29e-7785-3feb-8624-7d0e23002d4f | -7.03148 | -42.03489 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 60067361-1b66-331d-9eb6-1c835da54f92 | -13.22737 | -41.95087 | 2026-09-17 03:55:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 407fb4df-10d7-3e02-9b17-cdae6c853f4d | -11.26792 | -43.46697 | 2026-09-17 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8cf4d0f-d2f6-3a39-826a-c1cce663e302 | -9.4667 | -45.44836 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 54a460a2-6c6c-3a78-b425-411f999f7c1b | -12.43859 | -48.48704 | 2026-09-17 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e43324ab-e032-3ade-b091-8ef2574b2ca3 | -7.96312 | -44.83329 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f0830793-8c2b-3264-a245-b2b59dff5ac3 | -10.36958 | -46.89276 | 2026-09-17 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1fac34b3-143f-38f4-90a7-d5d15b89b83f | -7.36502 | -44.47688 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8d600b3b-bf98-3579-b31d-0ba4eff05df1 | -7.09014 | -43.46956 | 2026-09-17 03:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 64798fac-4620-316f-8c76-fbb004608ff6 | -13.15347 | -43.24403 | 2026-09-17 03:55:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6d33683a-531d-3b6d-ad5e-190ccb7e5d83 | -12.44698 | -50.85513 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 157e6b2e-109c-3661-8e6b-d8bc6929375f | -7.44081 | -44.58128 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d53c4e5-f35e-3bd5-9c4f-9ae88b8968a2 | -11.89131 | -43.82042 | 2026-09-17 03:55:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 353a9b03-c439-3be3-bbc1-a934a075b4c7 | -12.51487 | -50.85299 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c90af57f-6501-3f63-b668-d4ee0e520608 | -12.49411 | -50.88848 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d65a07a4-8a8a-3174-98ff-c0466c7b914c | -10.82845 | -46.14078 | 2026-09-17 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 63ec1cbf-4138-3f9b-8c13-64d86f5539ad | -11.36047 | -40.05848 | 2026-09-17 03:55:00 | NOAA-20 | CAPIM GROSSO | BAHIA | Brasil | 2906873 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a776958f-5e35-340c-acc4-47686d809e67 | -7.03229 | -42.06327 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 869cd3f6-19b6-3c86-9bbb-9b79c5bf6239 | -12.43526 | -50.84674 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1ca4367a-4a83-3a80-bd07-57d6bd443813 | -7.19203 | -41.8144 | 2026-09-17 03:55:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fb3a5f1f-c8a5-30a0-bc0d-92efb2ce3506 | -6.88383 | -45.47028 | 2026-09-17 03:55:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4f44f929-938a-37ae-a3d9-1bde56431d24 | -7.13432 | -42.17421 | 2026-09-17 03:55:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c3f925bb-ab4a-34ac-9e3a-55337d63bcd1 | -12.46427 | -50.87032 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 81d04f0f-7f5f-31a3-bd3b-8cc8495001d2 | -9.94053 | -45.44647 | 2026-09-17 03:55:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 50eb998e-b278-37f5-88ed-fa96f2e51a70 | -9.94891 | -45.28973 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 34f5258a-12e6-3ca9-88b6-8191cbdb1be0 | -9.94836 | -45.29717 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d26cef54-2535-369e-be26-08d7297952cc | -9.04309 | -47.76489 | 2026-09-17 03:55:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38099b92-480d-3501-a12a-5e9a1a7e79ce | -7.6003 | -46.32231 | 2026-09-17 03:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68a97642-2a0c-335e-a3c2-672d3c4df36f | -11.47845 | -45.76986 | 2026-09-17 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 141b6d69-d011-364f-bb54-259735c375ce | -6.88813 | -43.74876 | 2026-09-17 03:55:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 82d08b36-fa67-3bb7-996b-fd7d3a34d54c | -8.85795 | -46.97756 | 2026-09-17 03:55:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f8e1de16-9b3c-3cdb-ad66-e9c43598904b | -9.11339 | -45.73711 | 2026-09-17 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 50.8 |
| b5b72515-9cf6-3e92-9819-e65a92b5c256 | -8.8576 | -45.86752 | 2026-09-17 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| caf46d4d-ff90-3f59-8c38-bdc9c0e2b001 | -12.48395 | -50.84035 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 36.0 |
| d81560ec-7bc3-395b-aed3-f36a1ebb03ca | -9.82687 | -46.50112 | 2026-09-17 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4747b41d-8ccb-3e9a-9cc1-7d61529ea354 | -7.72126 | -42.50336 | 2026-09-17 03:55:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 7df97867-60ee-3c51-b4dc-ebdb4b55e0d6 | -7.72307 | -42.49248 | 2026-09-17 03:55:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c6d7cc14-1da9-3eca-826d-cdfb5395c28c | -11.27147 | -43.49449 | 2026-09-17 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 572a98e7-2d69-320b-9039-c1e85d9ed281 | -7.4448 | -45.29628 | 2026-09-17 03:55:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f4dccfa-1250-35eb-a1df-f43b861d25dc | -11.58953 | -46.87724 | 2026-09-17 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fde63099-d938-3e7b-81f5-11d209faa873 | -12.47227 | -50.83203 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f2599a70-194a-3107-bd37-3870858a894e | -9.8822 | -48.40034 | 2026-09-17 03:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 94b397c8-f44e-3a20-b372-e2470ee4ac3a | -9.95876 | -45.3204 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b133e526-849e-318d-bea6-fa73ae235625 | -8.56381 | -44.48307 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15870f3b-b53f-39b1-b198-47bb522235d2 | -12.47369 | -50.88968 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4395265e-2771-37c2-a616-7670c76d3c5e | -9.769 | -46.09795 | 2026-09-17 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5513be4-e175-3a91-896e-81d34c399b88 | -11.22395 | -43.45898 | 2026-09-17 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9871a02d-0c7e-3d45-befd-bbd57d933962 | -7.18586 | -41.8032 | 2026-09-17 03:55:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5e9528fd-d5d1-3ac4-9d23-459977725100 | -7.35948 | -44.48108 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1829ec65-2dd2-3752-9d03-41885503096e | -12.78526 | -47.56822 | 2026-09-17 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e49e996-8d35-379e-8eb9-2c191fc730cd | -12.4764 | -50.84436 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 36.0 |
| ea531582-9cb5-3432-9629-e8f3c35f8aec | -11.89346 | -47.58162 | 2026-09-17 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 629cd7f5-e205-36d6-88bb-068f582484c5 | -11.9873 | -52.47307 | 2026-09-17 03:55:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a36a9a8-1146-3aaf-bed2-f5b391a5adfd | -12.42322 | -50.87279 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7df77436-48ee-3f52-b800-e8aab567e98e | -9.90405 | -46.51489 | 2026-09-17 03:55:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7148d691-14f3-3a83-9443-dfaa2ee53ef8 | -11.3314 | -47.24254 | 2026-09-17 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README22.md)
