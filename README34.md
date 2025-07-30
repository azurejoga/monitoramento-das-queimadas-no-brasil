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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac3a3cf8-b34b-3a90-b4cf-53c316752375 | -6.12542 | -42.54339 | 2025-07-30 11:32:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 99.3 |
| 7de9ac13-5f88-3721-bd56-c3496d6886b1 | -7.33157 | -38.2611 | 2025-07-30 11:32:00 | TERRA_M-M | ITAPORANGA | PARAÍBA | Brasil | 2507002 | 25 | 33 | nan | nan | nan | Caatinga | 11.5 |
| ceb63762-1617-3f8d-bb52-3d808a26d507 | -7.69927 | -37.52399 | 2025-07-30 11:32:00 | TERRA_M-M | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 21.1 |
| 2f7cafd4-8296-3b0d-af6e-4648c68c4a8c | -6.12541 | -42.53742 | 2025-07-30 11:32:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 76.7 |
| 48cee59e-377d-35e8-b3b5-7a4101ceef99 | -14.27704 | -41.44148 | 2025-07-30 11:34:00 | TERRA_M-M | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 10.6 |
| c8578575-3f5a-385c-90fd-1185cc98a23e | -15.73695 | -42.6478 | 2025-07-30 11:34:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| a4bf8dea-62a1-365a-bd34-25431a61e804 | -9.74922 | -37.01019 | 2025-07-30 11:34:00 | TERRA_M-M | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 51e2cb24-5b2a-3856-a129-cad91d5e2edb | -13.59479 | -41.51472 | 2025-07-30 11:34:00 | TERRA_M-M | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 17.0 |
| b59224c3-ab36-3640-8494-332dd64073b5 | -17.50509 | -42.35624 | 2025-07-30 11:34:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 239b0cd7-f9d2-34a7-8f6b-14b9f4cad2b5 | -13.52845 | -45.63533 | 2025-07-30 11:34:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| b3b7b3a8-bf0d-383d-924e-e5a46ebefa4f | -13.53187 | -45.66505 | 2025-07-30 11:34:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 33.1 |
| e979edcd-ad89-36d8-9bd0-57704d209e90 | -9.08379 | -40.24635 | 2025-07-30 11:34:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 13.5 |
| c2b30760-0820-39e3-bcbb-8530ba5e6601 | -8.86627 | -44.16491 | 2025-07-30 11:34:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 8d9ebb11-3c30-3466-b482-d116a6a85302 | -13.53835 | -45.62944 | 2025-07-30 11:34:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 90b285aa-b3f2-3636-bc0d-654ee49bfe98 | -20.17105 | -41.78599 | 2025-07-30 11:36:00 | TERRA_M-M | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 87c1153d-4bfd-35f9-a11e-16b8397e75c4 | -13.5243 | -45.6462 | 2025-07-30 11:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 7d5aa579-e723-35c5-99fc-04ccca3c29db | -13.5243 | -45.6462 | 2025-07-30 12:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 4d162a03-3f58-3afd-8711-3093c8fc8d9c | -7.3646 | -43.7555 | 2025-07-30 12:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 112.1 |
| b907b175-ebe5-320e-b42a-a5e76d188109 | -13.5437 | -45.643 | 2025-07-30 12:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 9c2468a9-1b9c-3159-a0b2-9b09b8659e0c | -13.5243 | -45.6462 | 2025-07-30 12:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 241.2 |
| 4c0b6675-ffb7-3a80-9726-3eed9388d80d | -13.5243 | -45.6462 | 2025-07-30 12:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 405.0 |
| bca827f4-1480-375b-9539-738532acdc70 | -13.5437 | -45.643 | 2025-07-30 12:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 128.5 |
| bea509f4-d312-3541-b202-13935511eabf | -13.5238 | -45.6693 | 2025-07-30 12:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| a439ecd1-abe5-3207-b855-a67b757a1074 | -13.5238 | -45.6693 | 2025-07-30 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| c1549e3e-b1c4-3fce-bd58-aea88269c628 | -13.0869 | -47.3299 | 2025-07-30 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 970f627c-1b50-3dfe-b4f9-15e5afebcc56 | -13.5243 | -45.6462 | 2025-07-30 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 277.2 |
| f513de35-edd7-3046-9d10-e1e604bec8b5 | -11.5307 | -44.267 | 2025-07-30 12:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 67f9a3c9-91f9-3b19-b779-c047183338d9 | -13.5437 | -45.643 | 2025-07-30 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 172.0 |
| 3aec0ca6-49af-314b-9af6-487231bb0b70 | -13.5243 | -45.6462 | 2025-07-30 12:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 169.9 |
| f6114286-3ba6-3ddf-b6d8-f862613b97db | -13.5243 | -45.6462 | 2025-07-30 12:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 238.8 |
| ec65506f-590c-3834-bc95-0f7457f2c6c6 | -13.5238 | -45.6693 | 2025-07-30 12:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 53f1e076-27c5-3ef9-b0cb-3565bc254af6 | -8.605 | -45.5348 | 2025-07-30 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| cfb0f7fd-d526-3704-9752-bea84491456a | -12.6129 | -48.0673 | 2025-07-30 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 149c6517-3848-33dd-afc8-03f57d78e9c3 | -8.0425 | -46.9132 | 2025-07-30 12:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| cf13d573-829a-3d7d-a669-1c2e95db2836 | -13.5437 | -45.643 | 2025-07-30 12:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 75.6 |
| bb7dbdf1-a5a1-3f9e-a84f-07c636c5fae0 | -8.3565 | -47.3704 | 2025-07-30 13:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| c68d5c8e-13cf-3162-868b-6556d11e3698 | -8.3377 | -47.3721 | 2025-07-30 13:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 52afdd43-f338-338e-88da-aa3cf3ae61b2 | -8.6431 | -45.5081 | 2025-07-30 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 15df7287-03bb-32cf-a5c9-c9c58f4cd20f | -8.3753 | -47.3686 | 2025-07-30 13:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 173.5 |
| 78b45774-6f12-3ed8-a5b1-7d29f9055f00 | -8.3568 | -47.3483 | 2025-07-30 13:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| e9818940-2e07-392b-bd36-1c2fe0cede9b | -13.5243 | -45.6462 | 2025-07-30 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 48db923c-b897-3200-9f48-a3c6edbb0d59 | -12.6129 | -48.0673 | 2025-07-30 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 50b60fb9-c2e7-3179-a697-78068021f003 | -13.5243 | -45.6462 | 2025-07-30 13:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 06489ed4-336d-30a1-8a29-99e134f6aa78 | -8.3565 | -47.3704 | 2025-07-30 13:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 783a6394-c5ec-3581-b0cc-d495dcddbef9 | -8.6431 | -45.5081 | 2025-07-30 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.9 |
| b129b063-7074-35e0-a9e1-e9b29d503faf | -8.3753 | -47.3686 | 2025-07-30 13:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 94d4b7c4-d913-3b9d-b77c-9a99f8ca879d | -8.3568 | -47.3483 | 2025-07-30 13:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 2f9184d3-fa9e-39d4-9085-9eef35da2a87 | -13.5243 | -45.6462 | 2025-07-30 13:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 9cc17da1-bb49-3bc9-9637-260cbb6ca59b | -13.5437 | -45.643 | 2025-07-30 13:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 19231a92-7132-35de-a495-c58a6e49f401 | -8.3753 | -47.3686 | 2025-07-30 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 142.8 |
| 73fc5dec-c5b0-3906-aca1-3c10f29ed278 | -8.0425 | -46.9132 | 2025-07-30 13:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 2b7e287d-d509-36c8-9620-0f4f6434bbd9 | -12.8225 | -43.0889 | 2025-07-30 13:20:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 130.3 |
| 330924d2-9841-357d-9262-24169a57deae | -7.1131 | -44.3802 | 2025-07-30 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| c9dbd478-1683-30c8-9d64-46cdd6d158a6 | -8.6431 | -45.5081 | 2025-07-30 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 337.7 |
| 28eec268-7a6c-3a93-ba0f-c12bfaa30fd5 | -6.1229 | -43.9578 | 2025-07-30 13:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 16cc2d0a-5f69-3fe4-8fe7-9e3a01995232 | -13.5238 | -45.6693 | 2025-07-30 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 156.2 |
| f888ce99-bb03-3eda-9db9-83817a2e9ba9 | -13.5247 | -45.6231 | 2025-07-30 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 67489e12-5bfd-39b1-b133-c2aead765993 | -13.2237 | -47.2195 | 2025-07-30 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 730561b3-6bc1-3cee-952d-5cf37d8957ad | -8.6431 | -45.5081 | 2025-07-30 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 244.6 |
| 134b3d83-f23a-35cb-b563-1471a5fd5818 | -11.315 | -50.5774 | 2025-07-30 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| eeb8e44c-72c4-3a7c-bff9-72873a2f726e | -8.3753 | -47.3686 | 2025-07-30 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 192.5 |
| 1fd31529-20ed-328c-9100-2dba890ef0da | -13.5437 | -45.643 | 2025-07-30 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 107.2 |
| fedfd43e-d120-3504-a98c-e2b009a7a797 | -12.6129 | -48.0673 | 2025-07-30 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 5ab079bb-946f-390a-8561-98e93322bf94 | -13.5243 | -45.6462 | 2025-07-30 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 354.2 |
| 92106b4d-302e-3eef-988c-14adf0866c3e | -13.5053 | -45.6263 | 2025-07-30 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 15125129-4f09-31d5-8692-249d831dd066 | -11.315 | -50.5774 | 2025-07-30 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 55820a0f-9f9f-3c33-8d06-760d8fc898a3 | -13.5238 | -45.6693 | 2025-07-30 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 170.2 |
| 1b9e04e2-d3a7-3b84-b3f4-847e763eee19 | -11.3153 | -50.556 | 2025-07-30 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| d226acf4-2e5c-3bde-a8c4-ca8cef5e2593 | -13.5243 | -45.6462 | 2025-07-30 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 517.1 |
| 2a710963-78b5-3c96-8cfa-c30eb9bc51fc | -13.5247 | -45.6231 | 2025-07-30 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 334e0654-d7fe-3c47-8524-d0ce45a0dbdc | -8.3753 | -47.3686 | 2025-07-30 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 913f3dd6-5d1a-34c3-b6d9-23b6bb36b693 | -12.6129 | -48.0673 | 2025-07-30 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 297.4 |
| 1320cd9f-30d4-3c00-9942-43bf58a91582 | -13.5437 | -45.643 | 2025-07-30 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 2907dc54-b390-3eb8-9690-4c7b2658bd74 | -8.6431 | -45.5081 | 2025-07-30 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 143.4 |
| 23a92f48-eea6-3818-8053-1683bd6f0179 | -8.0425 | -46.9132 | 2025-07-30 13:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 36fe888d-e30a-33db-bc02-523546fdc23c | -12.8225 | -43.0889 | 2025-07-30 13:40:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 234.8 |
| 5449da34-468a-3910-ade0-5a1abc2c2492 | -13.5437 | -45.643 | 2025-07-30 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 1e4f1296-b61d-366a-b60f-8efd45afe13b | -7.6527 | -46.5263 | 2025-07-30 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| a074951f-fece-3809-a60b-5be7df719f2a | -9.6312 | -43.8518 | 2025-07-30 13:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 65.0 |
| 9b624042-2f95-3011-aa64-425f74790914 | -6.9946 | -52.8863 | 2025-07-30 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 47155aa3-719e-38e2-8fec-2654bfb0f949 | -12.6129 | -48.0673 | 2025-07-30 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 370.4 |
| 823e0ad8-18ac-3c00-a062-4193f3ecab06 | -11.315 | -50.5774 | 2025-07-30 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| ec4005dc-0a55-3ef5-b711-b455f5d7e322 | -12.8225 | -43.0889 | 2025-07-30 13:50:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 177.5 |
| 9fd40bca-62a4-3b63-b3d4-bd2f2db0e3ec | -8.6431 | -45.5081 | 2025-07-30 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 221.2 |
| 68292272-f836-3776-bfc3-9674f5a85b07 | -13.5243 | -45.6462 | 2025-07-30 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 217.0 |
| 306a2fdf-8dcf-33a2-82ff-6b53683dc50e | -8.0425 | -46.9132 | 2025-07-30 13:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 596b5902-9299-3e3e-a1a8-62b0bcd6261f | -8.3753 | -47.3686 | 2025-07-30 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 3d3a0ca8-cb1e-3db3-9b35-674ca02e821e | -13.5238 | -45.6693 | 2025-07-30 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 103.6 |
| a7529be5-a468-3305-ae48-9cf68070177b | -8.0425 | -46.9132 | 2025-07-30 14:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| e9191006-00a2-3ad2-92ae-8ee63397fe53 | -7.1131 | -44.3802 | 2025-07-30 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 80ca72a0-8935-3d24-b595-382da3de3eb8 | -13.5243 | -45.6462 | 2025-07-30 14:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 190.3 |
| 24d66fc6-3c5c-3f7b-9944-1663e487c296 | -8.6431 | -45.5081 | 2025-07-30 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 4467742c-e8b9-3218-98fa-3f7e4409db2f | -13.5238 | -45.6693 | 2025-07-30 14:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 3830d82c-f1df-36d4-97ae-ccd8c03452e1 | -8.3753 | -47.3686 | 2025-07-30 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 131.1 |
| cb1a8ce9-b09f-3655-b9d3-471b6ece1539 | -13.5437 | -45.643 | 2025-07-30 14:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 451ffdd8-bf05-3c92-9459-e3f20f1c113c | -13.2237 | -47.2195 | 2025-07-30 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 62.1 |
| e8bbcb5e-34ad-3ca7-951a-e111fb2010af | -7.0943 | -44.3819 | 2025-07-30 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 8ca4d260-6489-3227-8d74-f88886fc9b12 | -12.8225 | -43.0889 | 2025-07-30 14:00:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 284.3 |
| e11f5ea6-4184-3b81-ab2a-e24d32ee073b | -7.6527 | -46.5263 | 2025-07-30 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 1e893552-0627-3840-bd84-4b667854bc89 | -7.0946 | -44.3589 | 2025-07-30 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |


[Clique aqui para ver as próximas entradas](README35.md)
