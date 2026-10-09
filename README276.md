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

## Dados Diários - Página 276

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1054050c-3dfe-3fb5-b500-4972e69284e8 | -10.91171 | -45.51997 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.5 |
| bc20024a-62ac-32ac-b6e7-448c329d6508 | -6.04982 | -35.24582 | 2026-10-09 16:01:00 | NPP-375 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 2c9c1d08-bdd5-3e0f-976d-c6c30bdbad68 | -9.54245 | -46.84597 | 2026-10-09 16:01:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 6a7313fe-6ea9-3a8d-bde3-3814a1b6c829 | -10.32812 | -46.24512 | 2026-10-09 16:01:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 26d4cadb-78de-3f83-be7f-7e52d9046ab6 | -10.49316 | -47.34121 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 0cf1a203-c9f3-3349-8fa7-005fc333e1d2 | -7.01012 | -47.68599 | 2026-10-09 16:01:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 1dc4c0c3-1041-34d9-93ab-7f719028bca3 | -7.06859 | -40.95502 | 2026-10-09 16:01:00 | NPP-375 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 997d409c-9919-3777-94a4-4ca25187b0a2 | -6.5975 | -37.88734 | 2026-10-09 16:01:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 255c6d49-ab15-3726-b8ea-1be32fe1ba07 | -11.24817 | -44.85231 | 2026-10-09 16:01:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| b0118125-0840-31b2-88e4-36cfa875c1af | -9.9155 | -44.87423 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 19.2 |
| ab74a373-5213-3279-970f-325dfd5b3ae9 | -10.29603 | -46.60487 | 2026-10-09 16:01:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| bedfe24e-ec0b-307a-8312-2d5daac4d80d | -11.20946 | -45.26065 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 39.6 |
| f301cb67-db43-35dc-8e3c-ff11bddad118 | -10.32014 | -46.25633 | 2026-10-09 16:01:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 6c2a095b-9e08-35bc-b521-12ddee321a0d | -11.08926 | -44.05749 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f2342893-2402-30ed-b645-a66d8bcca187 | -6.86604 | -41.74459 | 2026-10-09 16:01:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 25.0 |
| 92629a72-65d2-362b-a026-d23f7549aa36 | -9.84214 | -44.78592 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| f7df69bc-f762-3e4d-9b0c-832047124c91 | -6.81987 | -39.55331 | 2026-10-09 16:01:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a6c74995-adb1-3f81-8ff1-7ffd646e6b5f | -6.96844 | -43.86067 | 2026-10-09 16:01:00 | NPP-375 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 472f65e9-87e1-37d8-a2f0-3f5ff1593765 | -9.87245 | -44.87584 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 0f2ec5bc-a080-3153-af40-89b7c04feb5e | -10.45671 | -39.54095 | 2026-10-09 16:01:00 | NPP-375 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| f00bb6d8-bea1-3055-b1ee-19c49edc6c69 | -4.57559 | -40.66626 | 2026-10-09 16:01:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 27.7 |
| 2bc06d2e-6583-3b5b-ab42-036446164e46 | -7.12175 | -42.54525 | 2026-10-09 16:01:00 | NPP-375 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| de9f5fac-788b-3483-98a7-3e53e07de971 | -11.1192 | -44.01138 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| e0fa8f54-0c1c-36b1-aead-226d9a4b0cca | -9.72618 | -45.53107 | 2026-10-09 16:01:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a4d3ca42-64ee-3e0d-bb25-07bdc8a44d2a | -7.47579 | -42.83645 | 2026-10-09 16:01:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 15c01a92-c0a2-39e7-8b22-ad2171fe7bbf | -5.60792 | -44.11972 | 2026-10-09 16:01:00 | NPP-375 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| cc2614e8-de71-3f4c-be91-de9e7e16aa5b | -11.06579 | -44.06026 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| aa79a804-7953-37b1-b387-7fce6748e64c | -11.08476 | -44.118 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e07abe8e-70b1-30a8-b8f8-679f95dc2f57 | -5.12156 | -42.76697 | 2026-10-09 16:01:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a06480e5-86df-3a4e-ae86-470a1bf36d53 | -11.49209 | -47.60611 | 2026-10-09 16:01:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| bf658080-4fdd-32dc-953c-46b1ee6c3a98 | -7.08282 | -44.04499 | 2026-10-09 16:01:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07587329-6520-3d5d-80d5-dde33cb051fa | -6.86092 | -41.74825 | 2026-10-09 16:01:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 30.2 |
| 32ee073e-7e19-3094-9b62-b8e834fe3ac9 | -10.47337 | -47.33086 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 28279a4a-8bdf-3394-9cab-57db6501161e | -10.88845 | -44.79899 | 2026-10-09 16:01:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 4259bdd9-c23d-37b6-8755-dd5e77569ce1 | -7.03451 | -44.31381 | 2026-10-09 16:01:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 890636c6-758e-371c-a402-3e2a85b0329f | -7.59041 | -47.03969 | 2026-10-09 16:01:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ed8558cf-fd55-3a2e-bcb6-05bc3f5f9df2 | -9.75349 | -45.68537 | 2026-10-09 16:01:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 34.6 |
| e6fd0fdb-3768-3b7f-b153-4568b98acc92 | -7.49084 | -42.83159 | 2026-10-09 16:01:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 47535801-3218-30a3-83dd-ed4ac967c7ae | -10.84331 | -47.35066 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| f78a327a-991d-3c1b-8c76-c22fdeb15c72 | -10.97242 | -45.19927 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| e45a9137-b91d-3078-9319-834b69b15779 | -9.05819 | -42.79427 | 2026-10-09 16:01:00 | NPP-375 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| fa4eaf90-d885-3c4c-a305-14dfa35bdbc0 | -8.90046 | -45.40172 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 45f87d1f-7309-393d-b456-20a3887e1e79 | -5.1135 | -42.85485 | 2026-10-09 16:01:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e6abe411-78cf-35ec-9cee-4c73813ff6bb | -6.80645 | -41.23865 | 2026-10-09 16:01:00 | NPP-375 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 59a73669-1c45-3340-849a-0c2e15ea3e3d | -11.1181 | -44.00797 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 7fd522a9-c067-388f-b22e-8b9a4b3b1226 | -9.72203 | -45.70275 | 2026-10-09 16:01:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 04275f51-7058-3783-a54a-873abb03584e | -10.48355 | -47.25711 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 9b6a4cc7-f530-347f-9579-a260982652a4 | -5.75582 | -35.31339 | 2026-10-09 16:01:00 | NPP-375 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 8.8 |
| ca2c64a1-5d75-3756-ad9b-010ac1b020e4 | -10.88715 | -44.79365 | 2026-10-09 16:01:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 62834e21-2e73-32d0-a963-05abb7a6ead2 | -7.10862 | -34.96119 | 2026-10-09 16:01:00 | NPP-375 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 24.8 |
| bca05703-74fa-30b4-933a-00d42e62cff6 | -9.17861 | -43.38798 | 2026-10-09 16:01:00 | NPP-375 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 19.9 |
| 87c7e454-1e1d-3c2e-af12-cfa28e4bb839 | -11.25463 | -45.18114 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 5fc972f9-ab4f-388b-8c7d-0c91580f4ac1 | -11.11512 | -45.6885 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 3a9252b8-f9d1-3764-a416-0e23d856f065 | -5.63785 | -43.2131 | 2026-10-09 16:01:00 | NPP-375 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 0b4770d3-aa27-37f6-8967-d178303413ee | -10.85776 | -45.5719 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 242210d2-b333-34de-bfbf-627fab407772 | -8.98007 | -45.14336 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4e686a3d-67e9-3da2-983b-192496899768 | -6.13283 | -43.04321 | 2026-10-09 16:01:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49c4e33f-0ada-394e-bdde-dab6b68bb0d2 | -6.85692 | -41.75397 | 2026-10-09 16:01:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 22.5 |
| 7ea6ae52-9582-3e73-b727-69571761d63f | -11.25106 | -45.17951 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| c9452e1c-13ad-3eb4-9504-eed9c970e9fc | -7.47783 | -42.85163 | 2026-10-09 16:01:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 6d14a6c5-dbd0-38d4-a7aa-2a8f0dfab71f | -9.93749 | -43.55485 | 2026-10-09 16:01:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 654385fa-74b4-3f7b-b323-c7969523553c | -7.05905 | -40.95224 | 2026-10-09 16:01:00 | NPP-375 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 004c0797-4f84-3842-a52f-ef24f6e994b6 | -6.05484 | -42.62914 | 2026-10-09 16:01:00 | NPP-375 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 704621a1-f61e-32b0-ab33-6bd24633cae7 | -6.49512 | -38.95794 | 2026-10-09 16:01:00 | NPP-375 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 36.4 |
| 5fc3c29f-252c-3915-9b29-008a091703bd | -5.7668 | -42.09747 | 2026-10-09 16:01:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 59421cfd-d151-3be8-8623-06a1c87b7be8 | -7.31375 | -44.01289 | 2026-10-09 16:01:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3e49379d-0786-34d8-a098-91fdbba6a65e | -8.34748 | -45.01538 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bfff1700-bc80-383a-89c9-d18e70c582a0 | -10.96887 | -45.38934 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 923da6f6-f6ee-3ac1-ac50-35e9b45d45cb | -7.46698 | -42.80974 | 2026-10-09 16:01:00 | NPP-375 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 9c118d0e-5bf3-3ffe-94b5-36598887f4e1 | -7.5438 | -42.10402 | 2026-10-09 16:01:00 | NPP-375 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 1740604e-13b8-374e-9a48-6d4cfe45f84a | -10.28885 | -46.61133 | 2026-10-09 16:01:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ca7e9ca0-5323-3c3e-8928-5c2d66a2a3a8 | -10.85071 | -45.56744 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| da0917a7-1c76-39fc-ac3e-b334029efdd2 | -10.62577 | -45.23956 | 2026-10-09 16:01:00 | NPP-375 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 10f5eed2-657d-3e0b-a00f-d6fe31b7f4fe | -9.72252 | -45.55287 | 2026-10-09 16:01:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 60690cd3-1837-3672-ac89-fae53230e710 | -9.15801 | -44.78305 | 2026-10-09 16:01:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 9b86b360-a7f7-35c6-9151-adc7d50500cc | -11.01899 | -45.43086 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 066924fa-01fd-3a47-80aa-4cc35ebcc56c | -6.49194 | -41.82173 | 2026-10-09 16:01:00 | NPP-375 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| bf70e839-622c-3a78-b341-a3f55196b434 | -5.44134 | -43.44599 | 2026-10-09 16:01:00 | NPP-375 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1444e2da-f4ad-39a6-b8ac-dc5f0b81c7a0 | -6.57331 | -38.84205 | 2026-10-09 16:01:00 | NPP-375 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 1298ecff-d455-3b02-8401-6e48215d6752 | -10.91095 | -45.51351 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 7f002c53-0510-3d8c-8b6d-38b1b6b075d9 | -9.09468 | -45.11921 | 2026-10-09 16:01:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 483f011f-27b9-3fae-b240-7bf4d3525584 | -10.93377 | -45.3785 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d3f1f691-cd4a-376f-bc9d-3c7a79432bb6 | -8.89871 | -45.23967 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 1ebe75da-0e0d-3e8e-ad1c-36befefc074b | -9.89764 | -44.83006 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 0293806a-e841-3d0d-9ca3-2e4c1cfcfcdd | -10.48623 | -47.21807 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 18ead507-99dc-3c59-a8de-ae1db086958b | -9.71578 | -45.69537 | 2026-10-09 16:01:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 73204fe1-3b3c-3062-a0f8-a26169a0811e | -7.28494 | -35.87889 | 2026-10-09 16:01:00 | NPP-375 | CAMPINA GRANDE | PARAÍBA | Brasil | 2504009 | 25 | 33 | nan | nan | nan | Caatinga | 43.0 |
| 49c5a1bd-26cb-37c2-9881-f1b289fd104a | -11.09956 | -43.99674 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 0de4c04f-5587-3757-b2a0-623dd365b3ad | -6.57558 | -43.04325 | 2026-10-09 16:01:00 | NPP-375 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5dad06b5-a31c-309a-921e-02a28c615091 | -6.94249 | -43.66679 | 2026-10-09 16:01:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 70822cb3-cb85-3ae6-aabf-87df7712e1b8 | -10.40244 | -39.86742 | 2026-10-09 16:01:00 | NPP-375 | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1acb43c2-0231-3c2b-93f7-6aeee2fa2a54 | -6.01026 | -40.96751 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 39.4 |
| 432ed434-bfd3-3007-8d5f-247830fbedfa | -6.01535 | -40.97146 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 28a45671-a81b-3561-907d-8d643bfc8464 | -10.91816 | -45.5195 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 758c03e0-d672-32f7-b2b6-341a22f47163 | -9.89821 | -44.83462 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 129.1 |
| e390c2d5-c3db-3ea5-8eaf-403fd05707be | -5.07432 | -36.94243 | 2026-10-09 16:01:00 | NPP-375 | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 282.5 |
| 705a6c92-7556-33fb-ab03-11199f17c521 | -7.26907 | -43.51347 | 2026-10-09 16:01:00 | NPP-375 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| a45f4c4c-9b6d-3ae3-8768-0c80f03cdc5c | -11.25673 | -45.17353 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| a4460f1b-f4b0-3fe1-abc2-ce347aeaa843 | -11.09617 | -44.06519 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 22abaa09-4731-32a9-83c3-712251f7f261 | -5.98376 | -41.38762 | 2026-10-09 16:01:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |


[Clique aqui para ver as próximas entradas](README277.md)
