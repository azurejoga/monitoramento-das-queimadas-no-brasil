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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e453e41-3e99-3bcb-81bf-4fbbda104f9c | -7.58946 | -43.45179 | 2026-09-19 11:28:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| c366009a-8c88-3812-94dd-9b3db56a4f3d | -12.50186 | -50.04715 | 2026-09-19 11:28:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 9754c8b3-1984-32f5-aed6-e2c33067ac54 | -11.33858 | -47.36346 | 2026-09-19 11:28:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 77f7c95d-0003-3b25-b1a2-61f0668c5888 | -12.28625 | -49.19358 | 2026-09-19 11:28:00 | TERRA_M-M | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 14d12b1c-c5cb-382c-ad8a-1cc3a087f994 | -6.67619 | -43.63589 | 2026-09-19 11:28:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b0bbaa60-1171-33c5-8320-ca1eee4fa7e5 | -12.60391 | -50.91792 | 2026-09-19 11:28:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 25.4 |
| b59ce90b-d959-324f-94f2-5403ea0edcd3 | -7.76871 | -44.86859 | 2026-09-19 11:28:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 6b4b039b-9dd7-3f49-ab19-1f9110e53c7e | -7.12921 | -43.69426 | 2026-09-19 11:28:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 95c10864-f717-34b2-809d-53497340414c | -8.37943 | -47.20768 | 2026-09-19 11:28:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 09972e01-6616-3f33-b36c-e581f2f7a115 | -9.80836 | -46.10114 | 2026-09-19 11:28:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 92e53592-fbb9-3a81-8e64-f74155c27564 | -12.54966 | -47.08519 | 2026-09-19 11:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| c3795755-1b50-3108-a8c4-562ec99ec864 | -13.15178 | -45.23252 | 2026-09-19 11:28:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| b76c4719-8388-39f1-a7f4-7cc08d46c053 | -7.0266 | -44.65425 | 2026-09-19 11:28:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 07c84821-e432-32a4-8f4c-76fb00d8e340 | -11.03861 | -48.27675 | 2026-09-19 11:28:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 95ba690d-04ad-339a-94a6-7e4ceb5d7ad2 | -7.86116 | -44.86782 | 2026-09-19 11:28:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 329f56c8-9341-372d-8208-782a96caf14c | -12.13524 | -46.98294 | 2026-09-19 11:28:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 1b3bdbdb-76e7-3e19-8b77-0c373bbf9461 | -7.99835 | -44.18844 | 2026-09-19 11:28:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d0a12415-bd72-3806-aacc-5a1d6e21d865 | -11.83946 | -47.63803 | 2026-09-19 11:28:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 1ac57b4a-2548-3c7f-929a-658ecd0fc3d1 | -9.24612 | -45.9393 | 2026-09-19 11:28:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 8ad6ae52-7c8e-3b74-8777-23bb0b38c508 | -9.74994 | -46.07412 | 2026-09-19 11:28:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 06269f01-eaf9-3dd0-a878-e0c59cca5aa3 | -8.6656 | -47.45801 | 2026-09-19 11:28:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d6169c03-5c9f-388d-a4de-28b425f698b2 | -7.78235 | -44.84045 | 2026-09-19 11:28:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 16de4ebc-1fd1-3a17-9f61-d6894bebb040 | -11.55336 | -46.89433 | 2026-09-19 11:28:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 1230b0fd-480b-375c-971d-0b2c283dc6d0 | -12.57656 | -49.11121 | 2026-09-19 11:28:00 | TERRA_M-M | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 0fefe068-66c3-310a-a775-82883d56fb92 | -7.70973 | -44.64478 | 2026-09-19 11:28:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 0ac90cf0-1d2a-3206-ae16-eebd33a8d261 | -7.02802 | -44.64451 | 2026-09-19 11:28:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 6d2b7971-2741-3136-8a13-62cedf58da70 | -12.16851 | -46.96472 | 2026-09-19 11:28:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| b4dae44d-ec37-3c1c-80db-09eb8420f704 | -6.9847 | -42.19207 | 2026-09-19 11:28:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 99231d98-8350-3297-ab8e-3c42a740de05 | -10.18154 | -48.51741 | 2026-09-19 11:28:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| f6d08b4f-6d5c-392c-be65-3a94e271c13d | -6.99354 | -42.19329 | 2026-09-19 11:28:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 1a4f6f50-37bd-3262-b47f-b0a6b392fa87 | -6.90572 | -41.70362 | 2026-09-19 11:28:00 | TERRA_M-M | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| ca2e1e98-a87f-3820-8ea4-79478669383e | -11.07869 | -48.311 | 2026-09-19 11:28:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| efd1d371-22cd-3b0e-bf96-6d7d27a94b09 | -9.34547 | -48.19464 | 2026-09-19 11:28:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| a8fd1449-8f03-38af-9c2d-506aac8c8f68 | -10.50375 | -46.71644 | 2026-09-19 11:28:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4aab0417-a64a-30f6-8ac6-f04beb398629 | -11.1159 | -49.4313 | 2026-09-19 11:28:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 3eabf850-e297-3551-8844-e5946316a850 | -10.45657 | -48.67738 | 2026-09-19 11:28:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 0b376308-3f47-3228-bebc-514661773e20 | -12.12898 | -45.15769 | 2026-09-19 11:28:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| dbcd6a9d-4ca6-3466-910d-defed20affb0 | -9.04452 | -48.71147 | 2026-09-19 11:28:00 | TERRA_M-M | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 37.9 |
| a7c8d80f-80fa-346d-a108-93fafc15df49 | -7.8626 | -44.85816 | 2026-09-19 11:28:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 956d0f93-23c1-3938-b560-11d4d56b77ff | -7.04629 | -42.08923 | 2026-09-19 11:28:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 0ef7f1b5-f9a9-3bf3-9f7b-978c246b4d6d | -13.01615 | -46.92196 | 2026-09-19 11:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c185655a-51c5-39d4-89fd-46d9eca92260 | -11.06121 | -49.76158 | 2026-09-19 11:28:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 0d9b37ca-0fd6-3156-ab17-d7d2fba7dab6 | -11.11294 | -49.44918 | 2026-09-19 11:28:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 8b636d00-45a8-3f58-a0cc-5566d702d74f | -11.31261 | -47.25877 | 2026-09-19 11:28:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c5c34a4f-d2a3-3650-ada7-2824af1f51ce | -12.57945 | -47.08959 | 2026-09-19 11:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e821e188-032e-39cf-a528-6e77a54f25dc | -13.47281 | -43.58794 | 2026-09-19 11:28:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| dc253a0f-fad6-39c7-9375-766ff4615b4e | -11.12217 | -45.28534 | 2026-09-19 11:28:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 15728273-7155-37a1-b61b-9d5e72b9248e | -11.47561 | -47.39783 | 2026-09-19 11:28:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 50e6e383-2a14-35a0-b0af-08973bda5b17 | -7.86007 | -45.13226 | 2026-09-19 11:28:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 198.9 |
| b4e0a03c-9e20-3fcf-93c3-ec2bb3a4e950 | -7.57805 | -44.90919 | 2026-09-19 11:28:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 5202f75c-acf0-3171-a616-750c76207abe | -11.82905 | -47.63632 | 2026-09-19 11:28:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| d5548f9c-e8cb-36dd-8536-e222a0e2a908 | -11.90946 | -50.11865 | 2026-09-19 11:28:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| e92d17c5-fe8a-31f7-9c6f-dbeb2dbc4c80 | -7.78431 | -44.89116 | 2026-09-19 11:28:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 65de943a-4fd6-3339-be60-3d28da7e149e | -7.12506 | -44.0387 | 2026-09-19 11:28:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 66.8 |
| bea1e27a-5d5d-3860-996e-eaaf33f2174e | -10.52508 | -46.71384 | 2026-09-19 11:28:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 4ed1ebe4-14cb-3aac-913f-cbbc4b43ea96 | -11.3096 | -51.72855 | 2026-09-19 11:28:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 87b8baca-f309-367d-ad69-acd459456422 | -8.8695 | -45.92455 | 2026-09-19 11:28:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| d57b3467-c648-3a14-a85d-e33aecb00b45 | -9.29763 | -48.20277 | 2026-09-19 11:28:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 8fdad00f-4471-33ad-8c83-9c1bc265e0da | -10.58861 | -44.7753 | 2026-09-19 11:28:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| a3aafad8-fb3d-3fd7-a734-97dbe4961bc1 | -10.48716 | -46.29769 | 2026-09-19 11:28:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 92704c91-a053-3331-b996-fc5164dddb15 | -10.58153 | -46.54514 | 2026-09-19 11:28:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c57029fa-3550-3744-b35b-8b42962d752a | -9.96365 | -46.55956 | 2026-09-19 11:28:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 9bfe40a0-0958-34c0-842e-6c817e28eeaa | -7.7838 | -44.83066 | 2026-09-19 11:28:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 395919c9-8be9-3201-b152-5e4e431a78b4 | -9.34784 | -48.17924 | 2026-09-19 11:28:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| b4a16dd2-5157-330d-a4de-02bf8dfff30b | -12.5948 | -50.91036 | 2026-09-19 11:28:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 21.2 |
| cacea781-b301-3a86-a7e7-efc64f0d8821 | -10.39841 | -48.31321 | 2026-09-19 11:28:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 2d916f1d-d235-3c9d-8c34-ab8283fb6e31 | -8.46928 | -47.01152 | 2026-09-19 11:28:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a7f6f1da-5e9b-31a8-b635-5f16370c0ffc | -8.7731 | -48.6868 | 2026-09-19 11:30:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 69.6 |
| c14434e5-5c2d-30be-adbb-a8695b862b18 | -12.7085 | -45.96 | 2026-09-19 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| a98e820b-4e92-3544-ae16-595f652e6520 | -9.9702 | -46.578 | 2026-09-19 11:30:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 182.6 |
| 8a68217b-c0f6-3fb6-b7c3-c24608569411 | -13.0173 | -46.9352 | 2026-09-19 11:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 28275a3e-f743-33f5-80f1-b2d06c02b62b | -9.9516 | -46.5577 | 2026-09-19 11:30:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 3d0c2951-9997-3e1b-8a19-3dc076faa576 | -9.9513 | -46.5802 | 2026-09-19 11:30:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 108.3 |
| e94ab98a-79a1-31cf-99f1-9bfbfffb13cd | -11.9112 | -50.1016 | 2026-09-19 11:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 17eb38e5-cfc4-3d95-8cf7-483d371a4272 | -11.9109 | -50.1232 | 2026-09-19 11:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 321c5947-f79c-3eb9-b7de-1bdda78e4fa7 | -11.7823 | -49.8152 | 2026-09-19 11:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 5aa2e5d6-6f9b-38d0-aed8-af8f78187a8e | -12.5952 | -49.1046 | 2026-09-19 11:30:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 98546746-3b70-34f9-ba5c-21671608dcd3 | -20.46319 | -47.62221 | 2026-09-19 11:30:00 | TERRA_M-M | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 4ecb4e82-deac-35ec-b002-175c5c79a35e | -14.68935 | -46.66337 | 2026-09-19 11:30:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 84670cc3-7504-3005-ab86-4559b5e16d8b | -14.139 | -45.16833 | 2026-09-19 11:30:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b8eeae6b-acf2-3dbc-a744-8dc031ee4050 | -15.0285 | -48.55893 | 2026-09-19 11:30:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 0a62b3df-c4fc-3f15-b5c0-1dbd6856906c | -20.46159 | -47.63249 | 2026-09-19 11:30:00 | TERRA_M-M | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 74.8 |
| bd97a7f6-63f8-3e61-b735-1fcb86fd5025 | -15.34073 | -39.97205 | 2026-09-19 11:30:00 | TERRA_M-M | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 202c03d5-03ed-30bc-a62c-0ab7877f1535 | -18.92365 | -44.72514 | 2026-09-19 11:30:00 | TERRA_M-M | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 56bbf4e8-b8d1-3a5e-b365-b1e4e8a18e03 | -16.9939 | -45.46403 | 2026-09-19 11:30:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 24.9 |
| be3f7c9a-3192-3639-909d-72eb35e70416 | -19.02854 | -46.92259 | 2026-09-19 11:30:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 2dbbeeff-3137-39f1-b940-02f7787d5433 | -13.32675 | -51.77386 | 2026-09-19 11:30:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 7c8c8b01-1d4d-3477-9705-7309085f7a09 | -16.99255 | -45.47329 | 2026-09-19 11:30:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 41d66856-3223-33f2-8e5c-b3edc320df00 | -13.88181 | -48.59882 | 2026-09-19 11:30:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a4e2dfb8-1b93-3068-ae8a-15aaad5a1965 | -20.07895 | -45.81599 | 2026-09-19 11:30:00 | TERRA_M-M | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 43b5b7a4-299d-3fb3-87b0-77c8cbd3e39d | -15.90285 | -48.08296 | 2026-09-19 11:30:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 989bc12f-371f-376c-bd66-834494bfdf3b | -14.68775 | -46.67375 | 2026-09-19 11:30:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 4e1cbc02-1af0-3ea7-b496-cd49b0229685 | -19.40801 | -44.82632 | 2026-09-19 11:30:00 | TERRA_M-M | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d39333a6-b77c-3dee-82db-bfa997f079ad | -14.66597 | -46.65315 | 2026-09-19 11:30:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| ddcd7c6a-4cd2-3a85-af2a-329be68a4e66 | -19.49312 | -45.33763 | 2026-09-19 11:30:00 | TERRA_M-M | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 39271333-5e3b-3a31-832f-903e90f603dc | -13.73454 | -48.80132 | 2026-09-19 11:30:00 | TERRA_M-M | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 3af4cf54-6127-3c9d-a34e-351adf7dada4 | -13.73707 | -48.7857 | 2026-09-19 11:30:00 | TERRA_M-M | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 276d078c-dfa2-3ad1-831b-47cbb1db0f77 | -17.57723 | -45.38333 | 2026-09-19 11:30:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d9323a3f-e944-3832-a42a-2f4a1432e0e3 | -19.19753 | -46.84192 | 2026-09-19 11:30:00 | TERRA_M-M | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 401e3d38-495a-3c3c-95d1-e0eb9d871d93 | -19.03004 | -46.9127 | 2026-09-19 11:30:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 27.1 |


[Clique aqui para ver as próximas entradas](README104.md)
