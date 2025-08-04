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
| efdcc2e4-7e0c-3d93-b551-a331ce5d3f4d | -7.56012 | -44.91073 | 2025-08-04 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48aa8a06-8cf5-3c4a-9cb0-3bfaf5bde0dc | -8.13206 | -49.58742 | 2025-08-04 04:34:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 8e3eba9e-008c-3f29-b59a-6e0e820831ae | -6.21968 | -44.34321 | 2025-08-04 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 046ec613-6ab8-37e3-a54a-c2c9318fcd9c | -7.01798 | -59.83232 | 2025-08-04 04:34:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c755847-de1a-334c-a603-2944bef05c5d | -7.56135 | -44.90256 | 2025-08-04 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85a98a5a-b10c-3e57-b6d8-822ca4187198 | -6.62261 | -59.95218 | 2025-08-04 04:34:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c6e6b7b-18ec-32a6-953f-d2e8f8446131 | -6.15531 | -57.91756 | 2025-08-04 04:34:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dc8215fd-62ab-39e1-b1f8-0ecb1c2314bc | -8.73732 | -46.40247 | 2025-08-04 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8985adb0-0cf0-3b73-8396-1088caec9272 | -8.00621 | -43.1457 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 29.5 |
| 6b90e465-9e24-3a6d-9849-c943075c7b3e | -4.73432 | -44.43306 | 2025-08-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d38437d3-bd78-3231-a158-1ba695d28dd3 | -8.7419 | -46.39552 | 2025-08-04 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ce2e019-1f3e-344a-ac6e-48a29f05dfd8 | -4.74022 | -44.44233 | 2025-08-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a9b22db7-d87e-3165-a473-9f240a6b518e | -8.0006 | -43.21272 | 2025-08-04 04:34:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c89f3faa-1b1d-3814-ad7d-ae1dc3356e93 | -4.73664 | -44.44176 | 2025-08-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 45aab25e-3676-34b1-bbd3-f95b4008d0f9 | -7.64404 | -45.30191 | 2025-08-04 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 94171b5a-38db-3cdd-b498-394a507c1ba4 | -7.43988 | -48.93705 | 2025-08-04 04:34:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a95fb2ee-e698-32ba-be44-bc64f426d540 | -7.27059 | -46.16397 | 2025-08-04 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 539b934f-bd35-39f2-a72f-85c7a28cb105 | -7.41289 | -45.28634 | 2025-08-04 04:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bcc9f71b-470a-32e4-a142-ce6e32c7b9c9 | -7.40887 | -45.26525 | 2025-08-04 04:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0969a332-3eb2-31b0-8fee-f548924de1fc | -8.73902 | -46.41424 | 2025-08-04 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aafe7b81-ebc4-3425-8532-2a7b016a9eec | -8.27105 | -47.36432 | 2025-08-04 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc43ddc6-28bd-37c1-a772-fc7e88bb9a18 | -7.01378 | -59.82698 | 2025-08-04 04:34:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 622aada3-d451-3eb6-84db-894282895d41 | -6.19711 | -43.75192 | 2025-08-04 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8cbabe91-5891-3221-b80e-16a5535c48e7 | -9.49966 | -43.17136 | 2025-08-04 04:34:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e1ede0ae-c024-3605-9d7e-2e63d3614658 | -7.44323 | -48.9376 | 2025-08-04 04:34:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 127a1047-122b-31b7-9f39-eea30d30e8b8 | -5.98654 | -45.52437 | 2025-08-04 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12524802-e801-3105-ba44-5effd6d839f3 | -6.32699 | -45.65263 | 2025-08-04 04:34:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10ccb20a-628b-364f-ad49-54f2e2f185f8 | -5.28754 | -44.88472 | 2025-08-04 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 22b418af-5751-3354-aa58-7fbe93394570 | -8.00569 | -43.14923 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 29.5 |
| be4e5f5d-4ecb-3d3f-9201-7fbe1675d8e1 | -5.87548 | -50.14951 | 2025-08-04 04:34:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9bf2069-b980-3297-9ae9-fdb2dd7024a9 | -8.26995 | -47.37138 | 2025-08-04 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67765a09-c9b9-3813-b7f7-950cc556ef48 | -8.03558 | -43.11392 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| b3d65395-07fd-376d-a64c-c978f73400d6 | -4.7464 | -44.43776 | 2025-08-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58702d29-bd1d-3068-9da6-66d32d1f14a8 | -9.46066 | -46.3205 | 2025-08-04 04:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d9fab06c-5d05-3e16-8c68-94006aa6bf3c | -6.14886 | -57.92064 | 2025-08-04 04:34:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3681de2e-bb0f-3f1c-8568-c3325cae2527 | -6.72616 | -46.29995 | 2025-08-04 04:34:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 56bf523a-20a0-34fc-874b-f3ceea38c54c | -6.17585 | -44.77762 | 2025-08-04 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 90d77f25-c18b-38eb-8e38-2069f32fdcf7 | -3.39556 | -46.90792 | 2025-08-04 04:34:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f3597c0-07a9-326b-9e77-8ad02568bc93 | -6.52564 | -44.53796 | 2025-08-04 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47d2915b-0743-3612-b952-84dfd3ac7b23 | -8.35774 | -46.9404 | 2025-08-04 04:34:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41184f7b-2989-388e-b1bc-cb80b945841a | -7.55176 | -44.89255 | 2025-08-04 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1353adaa-a982-3d94-ab67-673863d78504 | -6.32351 | -45.62913 | 2025-08-04 04:34:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3f49cc6-0c67-31c0-9fd4-2e861cbc45cb | -8.25819 | -47.33698 | 2025-08-04 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66b48419-1fe1-3be9-8f15-9e10ee14981b | -7.44266 | -48.94114 | 2025-08-04 04:34:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7937dec-9c27-39e2-980b-90317682f752 | -6.64185 | -51.4527 | 2025-08-04 04:34:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e523acc8-9df9-3c3d-a748-2be42365c74d | -7.9916 | -43.16127 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.7 |
| dd36a7ce-b700-35bc-a66c-812efc8e6b48 | -7.55113 | -44.89674 | 2025-08-04 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a149500b-2091-3a0a-bd99-a3f2032b8d9d | -4.74444 | -44.43884 | 2025-08-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fdb81821-776d-3d63-a016-2eac8bf186b8 | -7.54279 | -44.87838 | 2025-08-04 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46409102-da90-3982-b956-302acac588c0 | -4.12475 | -47.65232 | 2025-08-04 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9c8c9c6c-b382-359c-893c-726e4e8e7094 | -7.99709 | -43.20863 | 2025-08-04 04:34:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 5b99758f-5278-3f79-9ba6-57f2a8b5d262 | -6.06251 | -44.66933 | 2025-08-04 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8bb0d592-d2df-30c4-a1e6-5799eb817cec | -8.37722 | -46.54538 | 2025-08-04 04:34:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8f001ce-bbd9-3106-8bcf-ff8218fd5b0c | -4.1361 | -46.45844 | 2025-08-04 04:34:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c1105001-7872-3690-82dc-c42ec3f127ad | -4.21289 | -46.14253 | 2025-08-04 04:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b0162ae-d2c8-36fc-ac8f-c81ae5587ba3 | -4.17076 | -47.2102 | 2025-08-04 04:34:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e30459a4-e97c-3cbe-a494-2d601e108c3f | -3.3961 | -46.90447 | 2025-08-04 04:34:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1eddcedf-aeef-3935-aa93-a84053798991 | -7.33771 | -44.68201 | 2025-08-04 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68de9ca3-a15d-3d97-b1d3-41df919875c7 | -8.54945 | -47.46219 | 2025-08-04 04:34:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f73b424-bd75-3f43-a569-89c77c34b067 | -6.62702 | -59.96429 | 2025-08-04 04:34:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9a9c9180-8b44-3dbb-abef-039c3dfb3ae1 | -8.74588 | -46.41531 | 2025-08-04 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 660c1ad8-d5d1-3a7b-ab7a-12655eedba8a | -7.01817 | -59.83846 | 2025-08-04 04:34:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 45da5acb-5400-3665-9f7c-9debe3980ec7 | -6.65308 | -59.10661 | 2025-08-04 04:34:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 147a6999-c75e-338c-8dee-3b82db857ebb | -7.5579 | -44.87646 | 2025-08-04 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 855af275-a19d-3f54-9b01-bff98bb1f2d2 | -4.73727 | -44.43771 | 2025-08-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 28d5d635-e646-3366-9326-83845ee642c5 | -6.69114 | -44.35526 | 2025-08-04 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cac3973a-08d9-387d-9a54-87e2fcec6522 | -8.00317 | -43.1667 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a0d460fc-7c1b-3b14-93da-243df3e54b63 | -7.05604 | -44.39825 | 2025-08-04 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 884bdd49-3517-34fd-a518-439f1e386d41 | -7.21092 | -41.85559 | 2025-08-04 04:34:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2bf387ce-db80-3f18-849d-0a0233f4bfcf | -7.7687 | -45.10474 | 2025-08-04 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce5753d4-c085-34c5-8186-a41f32cb3a56 | -8.0579 | -43.10268 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| d8de6eb2-e3fb-3aae-a663-1fd501a9919d | -6.14671 | -43.77936 | 2025-08-04 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7a47e4e-c6c0-3b86-9e06-777988e1dc19 | -8.01928 | -43.16907 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c399d178-6298-3d6e-ba87-0bc2eb219aa8 | -8.36053 | -46.92246 | 2025-08-04 04:34:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24d45bcc-53bd-3c74-b989-c4c484672465 | -5.87611 | -50.14563 | 2025-08-04 04:34:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 389ae403-39dc-3023-82b6-f74612748e42 | -7.41242 | -45.26577 | 2025-08-04 04:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b96724dd-f4f3-3fe3-ab54-af913311f5d5 | -7.55128 | -44.8712 | 2025-08-04 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6a0eea04-d1eb-3cba-8526-c3affdf0091a | -6.6331 | -43.66891 | 2025-08-04 04:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12e0e284-3691-367b-9eb2-490c20959942 | -4.12529 | -47.64885 | 2025-08-04 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f947aafc-559c-362a-9b41-b5b1c3e2db24 | -7.26774 | -46.15974 | 2025-08-04 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4cf8dad2-5af4-3d25-828b-ba01565f3231 | -6.61963 | -59.96822 | 2025-08-04 04:34:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 478d55d2-7d5c-3bcc-b720-e66c82648b79 | -8.74645 | -46.4116 | 2025-08-04 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dfb7d6d8-1368-398c-ad4c-30ce49569026 | -6.55803 | -43.9146 | 2025-08-04 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8daea351-01ae-3058-b46f-381056170b19 | -7.446 | -48.94168 | 2025-08-04 04:34:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc3e9deb-6ab9-3dc6-bc42-14f0b626d96f | -6.55736 | -43.9192 | 2025-08-04 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6bd563f-a7a2-3478-9afa-659985539cf1 | -8.36446 | -46.9194 | 2025-08-04 04:34:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ca3a4e1-e4a7-32f5-9f18-53e2af96974b | -4.74149 | -44.4342 | 2025-08-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df3aa7bc-53da-3249-b06f-cc2a54d64290 | -7.03415 | -59.85826 | 2025-08-04 04:34:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ae6a91b-2e27-3b4f-9c4d-ba6dbb3f300f | -8.51562 | -44.73973 | 2025-08-04 04:34:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4f83e45-c36e-3e1a-9284-2e623f7967df | -8.35884 | -46.91112 | 2025-08-04 04:34:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4f565fa5-7512-3736-bf2b-8bd2c8339112 | -8.00816 | -43.18897 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c31db6a1-eaa5-3a49-8225-2677f42f34b3 | -6.85213 | -41.70406 | 2025-08-04 04:34:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1f81ee53-33da-3b02-a91e-548e9d3d13a9 | -4.12143 | -47.65178 | 2025-08-04 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7a83b53c-2af9-3c40-8c92-5ee5dfaa4d3a | -4.21657 | -46.35983 | 2025-08-04 04:34:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 041191a4-49c3-3519-b412-116b889771e1 | -4.73791 | -44.43364 | 2025-08-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc154487-42e3-3215-9bcb-9596b77333f3 | -7.34136 | -44.68254 | 2025-08-04 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b9dd672-e3a2-369a-804d-46610ba30dc6 | -8.26208 | -47.334 | 2025-08-04 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19af39c4-e479-38ad-9e20-f4727b491456 | -7.40409 | -45.27274 | 2025-08-04 04:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55f64113-8d6a-3e2f-a87d-cc4a7a87a422 | -8.05385 | -43.10207 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| cb43de41-a5a2-3781-a5e0-057cd9aadccc | -6.62504 | -59.97503 | 2025-08-04 04:34:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 19.9 |


[Clique aqui para ver as próximas entradas](README15.md)
