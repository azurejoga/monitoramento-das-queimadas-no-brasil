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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7250bec8-4275-351e-a953-16aa12498302 | -12.32344 | -63.72312 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6723695c-e658-394f-bcca-9c56c5e7f412 | -12.32331 | -63.72231 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f7b5d3b-43bd-3118-87ac-3c680f9a082c | -11.28736 | -65.2746 | 2024-09-29 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 81c9f9c0-5b55-31fb-a047-7db3a3760846 | -11.28638 | -65.2795 | 2024-09-29 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d4d35407-a485-336e-aef0-fb288ae45bd2 | -20.64784 | -46.28096 | 2024-09-29 04:53:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19594af3-e86a-3c12-82c1-80349e3b4479 | -20.64755 | -46.26816 | 2024-09-29 04:53:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5ac33be6-04a7-3ed2-965f-3156580d6177 | -20.64747 | -46.28441 | 2024-09-29 04:53:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 196ff722-9719-3edf-bf97-756535cf2b5d | -20.64617 | -46.28214 | 2024-09-29 04:53:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07a7520c-cfa1-3cdc-9deb-f3697cd84ba4 | -20.64583 | -46.28558 | 2024-09-29 04:53:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 12a0c419-3c79-33d2-95ae-e01ba724c2c8 | -20.64432 | -46.26326 | 2024-09-29 04:53:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 3e70b94a-b9b5-30da-8df5-b21b5317a564 | -20.64393 | -46.26692 | 2024-09-29 04:53:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8b1e4c15-b66e-3942-9fa9-09e7ed012207 | -20.64355 | -46.27054 | 2024-09-29 04:53:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8a42f414-381e-3a7b-a149-c041ea46ff14 | -20.64286 | -46.26107 | 2024-09-29 04:53:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 500877e0-9127-3b0b-a075-711814b4adf0 | -20.64251 | -46.26464 | 2024-09-29 04:53:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 75f9291c-bac6-3e2f-a46c-c338a16be80a | -20.64216 | -46.26828 | 2024-09-29 04:53:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 021bf7c9-7b2f-3a25-8f34-daba91d7433f | -20.64181 | -46.27182 | 2024-09-29 04:53:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ced46d37-34c7-35c1-9fcb-6a2dfd0ba0a0 | -20.64175 | -46.28765 | 2024-09-29 04:53:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ee7e289-3619-3699-9323-7dc0bfde0878 | -20.64013 | -46.28889 | 2024-09-29 04:53:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e8899ecd-5f4e-3375-8522-4ab57a3d10d9 | -20.6389 | -46.26357 | 2024-09-29 04:53:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e90b6c94-d35d-3e52-8613-c341ac6d5feb | -20.63639 | -46.28751 | 2024-09-29 04:53:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e77a6539-4ce3-3c01-9b8a-d9159bcec525 | -20.63512 | -46.28525 | 2024-09-29 04:53:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 58913028-7fa1-32fe-8a9c-5fce0c22e17c | -20.63387 | -46.26024 | 2024-09-29 04:53:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b871814-9c4c-3002-bb61-365fc1389ea6 | -20.6324 | -46.25803 | 2024-09-29 04:53:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be4dd506-fba5-3a84-8b13-87e84d116638 | -20.63206 | -46.26152 | 2024-09-29 04:53:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f7e024a-fae5-39e2-9b97-f971040a05e1 | -20.63138 | -46.28402 | 2024-09-29 04:53:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e906087b-e5ae-3931-a189-fc33a7e83f09 | -20.63103 | -46.28739 | 2024-09-29 04:53:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6022a392-b7e1-3f06-801d-6fc2df7f747e | -20.63063 | -46.29114 | 2024-09-29 04:53:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e3fbbde0-b551-3ff1-a218-f70493a955be | -20.62976 | -46.28514 | 2024-09-29 04:53:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 42747dae-7ad3-30dd-a547-e55076ef71a8 | -20.62942 | -46.28863 | 2024-09-29 04:53:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca9b4b42-e4fa-38e3-a34a-d8520bd75b18 | -20.62904 | -46.29255 | 2024-09-29 04:53:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5bd70b03-5076-3d98-9a2b-cb13a7265d81 | -20.62846 | -46.26044 | 2024-09-29 04:53:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4203236e-dd1e-3079-ac85-1f260f515880 | -22.29597 | -46.82674 | 2024-09-29 04:53:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4aae1ebd-c489-3843-a976-8df2481ecbd1 | -22.29567 | -46.82985 | 2024-09-29 04:53:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb76c039-f4a3-3f8d-886b-a267431f3f88 | -22.01765 | -46.04671 | 2024-09-29 04:53:00 | NOAA-20 | ESPÍRITO SANTO DO DOURADO | MINAS GERAIS | Brasil | 3124401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 2c893e60-dc42-3785-ab2d-8f02752a1611 | -22.01217 | -46.04612 | 2024-09-29 04:53:00 | NOAA-20 | IPUIÚNA | MINAS GERAIS | Brasil | 3131505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 0633bd16-0c3a-3aa9-b107-4ed8d2b0183c | -21.92133 | -45.59264 | 2024-09-29 04:53:00 | NOAA-20 | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1b16235f-ca13-32bd-ab2d-8db3fcaad92d | -21.87753 | -46.55576 | 2024-09-29 04:53:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 67d8142a-5145-3938-b970-847ade414952 | -21.87634 | -46.55533 | 2024-09-29 04:53:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bbf74735-acb0-3553-9f0d-33b31f5473d4 | -21.47313 | -46.82633 | 2024-09-29 04:53:00 | NOAA-20 | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 284ac859-134d-3b8a-ac14-8bed975cb98a | -22.78126 | -46.80112 | 2024-09-29 04:53:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 30c18aab-dd7d-3b9b-8fa8-994386fab133 | -22.78093 | -46.80453 | 2024-09-29 04:53:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| cdc97220-b8d2-38c7-9574-bf273bcb6ee0 | -21.93664 | -48.45488 | 2024-09-29 04:53:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 734c1819-fa8f-3b27-9cf3-646f861d76e2 | -21.60662 | -47.78453 | 2024-09-29 04:53:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d4408dce-6216-3893-9cd7-c873265e0fc2 | -21.60174 | -47.78392 | 2024-09-29 04:53:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17b9db4a-7499-3ed0-8658-9868b4962292 | -21.60051 | -47.74904 | 2024-09-29 04:53:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 53376fdc-8873-3ab8-b380-ea38a07d363b | -21.59686 | -47.78328 | 2024-09-29 04:53:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f2f9721f-d385-3826-bb29-609291a64dad | -21.59502 | -47.75412 | 2024-09-29 04:53:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6c6331d-3d62-308f-a162-f806b1349c22 | -21.59139 | -47.78827 | 2024-09-29 04:53:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7aa7a34e-a0a8-36c8-b3dd-35a7945e0278 | -21.58465 | -47.75859 | 2024-09-29 04:53:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3a88ed5d-3e03-383e-905c-a50900eaedf3 | -21.58405 | -47.76424 | 2024-09-29 04:53:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 76714051-b8af-3418-8a14-e5d305a07e82 | -21.58225 | -47.78131 | 2024-09-29 04:53:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cabae79b-2036-317a-b27d-5bc0dc4530b8 | -21.57976 | -47.758 | 2024-09-29 04:53:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| abf760e0-712a-3435-90ec-84c2332e21af | -21.57917 | -47.76361 | 2024-09-29 04:53:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 654e28b0-c645-3a3f-bb89-a5dd51056160 | -21.57737 | -47.78069 | 2024-09-29 04:53:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41e47be7-038e-3bdc-8e08-193c4adc4035 | -21.57488 | -47.75737 | 2024-09-29 04:53:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1bbccdfc-bcad-3780-b149-2c032030636d | -21.57429 | -47.76298 | 2024-09-29 04:53:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 36c5068e-ead8-3b71-954c-0ad2c89ae557 | -21.57309 | -47.7744 | 2024-09-29 04:53:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc3f9d87-3582-3988-b96c-27b5c0803ed7 | -21.57249 | -47.78012 | 2024-09-29 04:53:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d159e2d-155b-38ae-b3ed-c2b31cce1ec5 | -21.13326 | -47.03367 | 2024-09-29 04:53:00 | NOAA-20 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 20f1695d-6c02-3d0f-b829-e6658d5d8a8a | -21.13295 | -47.03669 | 2024-09-29 04:53:00 | NOAA-20 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b5956d56-8561-3bbb-b532-1047b0d47c19 | -21.13263 | -47.03976 | 2024-09-29 04:53:00 | NOAA-20 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 50fa6fd1-f89a-380c-a592-7b0d0a965a13 | -21.13231 | -47.04285 | 2024-09-29 04:53:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 825db936-d19b-3b0b-9cf0-9e7459bd0832 | -21.12812 | -47.03345 | 2024-09-29 04:53:00 | NOAA-20 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d82e1a35-d231-36d6-a0e5-617b8bed9978 | -20.8687 | -49.57334 | 2024-09-29 04:53:00 | NOAA-20 | JACI | SÃO PAULO | Brasil | 3524501 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 99fcf911-1d43-3c42-856e-49fb680c9f35 | -20.82367 | -49.5102 | 2024-09-29 04:53:00 | NOAA-20 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| e052c40d-543f-3221-8441-71bcc6160020 | -20.82123 | -49.51239 | 2024-09-29 04:53:00 | NOAA-20 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7e670039-d864-3e41-bf58-20267448d115 | -22.29349 | -49.65094 | 2024-09-29 04:53:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| 6bfb0d80-aa43-3aa6-bee9-1c33e1334a56 | -22.29285 | -49.64797 | 2024-09-29 04:53:00 | NOAA-20 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 66bdf421-25a9-34da-b47b-46fef55023e9 | -22.29232 | -49.65244 | 2024-09-29 04:53:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 4fb23786-a64e-3e18-9a5e-8a97672275a8 | -22.27219 | -48.6619 | 2024-09-29 04:53:00 | NOAA-20 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0da2a814-9b13-3332-9b37-889d73cf0c0d | -22.25105 | -49.66483 | 2024-09-29 04:53:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 23e35deb-fc31-3c7a-854b-d1d09a16ebb0 | -22.25054 | -49.66927 | 2024-09-29 04:53:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| d4af15af-d051-3bd1-bf47-e5873714f3ed | -22.2467 | -49.66422 | 2024-09-29 04:53:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 3b0a0a89-9826-3fbe-81da-b85412186d98 | -22.2462 | -49.66859 | 2024-09-29 04:53:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| 6fa63cde-7bf1-3d58-9766-678f329579c3 | -21.64362 | -49.75574 | 2024-09-29 04:53:00 | NOAA-20 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 29c3e3c0-51e2-36d9-b431-89469a3d7473 | -21.6414 | -49.75223 | 2024-09-29 04:53:00 | NOAA-20 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0fe1d563-5877-3664-b49c-071fa62c40b6 | -21.64086 | -49.75664 | 2024-09-29 04:53:00 | NOAA-20 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fe583091-d915-3a16-b3bb-6319a90219bd | -21.57828 | -49.76979 | 2024-09-29 04:53:00 | NOAA-20 | GUAIÇARA | SÃO PAULO | Brasil | 3517208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 776a1612-ced6-3038-b8dc-97202f5535f3 | -21.15623 | -48.91222 | 2024-09-29 04:53:00 | NOAA-20 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| b82ed3a1-2c4b-3607-854f-b97b93b2bb99 | -21.15171 | -48.91171 | 2024-09-29 04:53:00 | NOAA-20 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d30f0764-fa3e-330b-8250-896767c875a8 | -21.09411 | -49.1375 | 2024-09-29 04:53:00 | NOAA-20 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f6cfb6e3-d3fa-3c1b-bb5e-fbacda01f5f4 | -22.538 | -48.81519 | 2024-09-29 04:53:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18376c99-3812-3697-b31d-0c0e37f4b4a5 | -23.37337 | -50.22214 | 2024-09-29 04:53:00 | NOAA-20 | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 25b58225-1513-35b2-9fe6-84a6f7bc7a7b | -23.37286 | -50.22655 | 2024-09-29 04:53:00 | NOAA-20 | JUNDIAÍ DO SUL | PARANÁ | Brasil | 4112900 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 86e8f43c-1163-335a-96b3-48710170018b | -23.37236 | -50.23081 | 2024-09-29 04:53:00 | NOAA-20 | JUNDIAÍ DO SUL | PARANÁ | Brasil | 4112900 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5f40c02b-3cb5-3186-9a01-c3173fc93751 | -23.3686 | -50.22594 | 2024-09-29 04:53:00 | NOAA-20 | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e65ce7c5-1949-3ade-9b2d-bf52def401c9 | -23.36809 | -50.23024 | 2024-09-29 04:53:00 | NOAA-20 | JUNDIAÍ DO SUL | PARANÁ | Brasil | 4112900 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6dafe882-21a0-353d-87b5-d4470a3d885d | -23.23074 | -49.40205 | 2024-09-29 04:53:00 | NOAA-20 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 120ec7f4-8d36-3e66-8f35-067c8ae2bdf6 | -20.7191 | -50.62072 | 2024-09-29 04:53:00 | NOAA-20 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f4fbac2f-b629-3a7a-af40-16f7b1dc35b4 | -20.71863 | -50.62447 | 2024-09-29 04:53:00 | NOAA-20 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ce6e8c8d-62cc-35be-87d6-89393e6a38dd | -21.2177 | -51.43855 | 2024-09-29 04:53:00 | NOAA-20 | GUARAÇAÍ | SÃO PAULO | Brasil | 3517802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8c9b854b-7556-3f3d-8944-52253cdb2186 | -21.21546 | -51.44115 | 2024-09-29 04:53:00 | NOAA-20 | GUARAÇAÍ | SÃO PAULO | Brasil | 3517802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 98a3bacd-f5cb-36e1-99c2-097b07aa386c | -22.4287 | -51.37551 | 2024-09-29 04:53:00 | NOAA-20 | TACIBA | SÃO PAULO | Brasil | 3552908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| bc8e7cc6-1ba6-3aad-a627-b5e7b32c771b | -22.42478 | -51.37494 | 2024-09-29 04:53:00 | NOAA-20 | TACIBA | SÃO PAULO | Brasil | 3552908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.3 |
| 7183da74-c9f8-33ca-8eff-8603e54dea38 | -23.99774 | -51.5099 | 2024-09-29 04:53:00 | NOAA-20 | CRUZMALTINA | PARANÁ | Brasil | 4106852 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 35a036b8-a62a-38ba-a5ed-a364907e1f73 | -22.68729 | -53.21079 | 2024-09-29 04:53:00 | NOAA-20 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d53eff21-2cb8-3ee3-abc3-20300b11c3c2 | -22.68669 | -53.21516 | 2024-09-29 04:53:00 | NOAA-20 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7ef712a4-ae97-3289-ae1a-24e0f9b334ae | -20.8056 | -53.11165 | 2024-09-29 04:53:00 | NOAA-20 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dfee5534-a917-3b41-a730-4fad248b408e | -20.80502 | -53.11582 | 2024-09-29 04:53:00 | NOAA-20 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95d69cb4-3c09-3986-bd24-65cc1a3b3859 | -20.80266 | -53.1069 | 2024-09-29 04:53:00 | NOAA-20 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README63.md)
