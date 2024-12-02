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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72423cd3-014a-3907-a85b-b47f8a267b75 | -3.74793 | -54.51056 | 2024-12-02 04:25:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c713de98-385a-3312-bbcb-3433741b7cc2 | -3.55528 | -46.02531 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74ab06e8-e48b-3afa-a96c-ee47193a08ec | -3.53589 | -53.51146 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c96c3684-af32-39d1-824f-0689483dca37 | -3.26855 | -51.10547 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6abd1c4f-f92a-3e71-af41-852822f40efe | -3.28639 | -50.6293 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc31a200-6c35-3068-bbd0-20960417e794 | -3.77447 | -46.69702 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10e27372-bd60-38e1-9d41-693801b32868 | -4.34945 | -45.75384 | 2024-12-02 04:25:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd1ea9ae-0a3e-3027-b157-9542c9ddfc1f | -4.55403 | -45.72197 | 2024-12-02 04:25:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 232a4b91-9835-3e3b-b2fd-84d6961e1dd5 | -4.07163 | -46.69678 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46557256-8a7b-3fc8-823e-cc349696d2a3 | -3.74218 | -52.26557 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02114fbf-d14d-3bd3-b43f-c8c89e178a5d | -4.07051 | -46.68218 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ecafa00-cec8-3f08-8200-713e90a6bf53 | -5.58715 | -45.14902 | 2024-12-02 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 1ae529ab-2816-3954-9462-6db032e2be27 | 1.937 | -55.7077 | 2024-12-02 04:25:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c214482-044a-3454-aecf-f90bc6196253 | -3.82685 | -46.5932 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d3d686d-d692-3581-8fad-615cfb8a2339 | -3.95993 | -46.50324 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| def7b637-6c9e-3c44-b360-8a874e9660a4 | -3.99422 | -46.30848 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 227d96cf-b21e-3a73-a400-f67089a35c50 | -3.81404 | -46.54441 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33d2f1b0-68cc-33d9-9de4-00104c126225 | -3.21469 | -54.23375 | 2024-12-02 04:25:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e59a0b2-b332-386a-a7b2-1f82c87688c5 | -3.07088 | -53.69121 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd299495-6e14-31b4-9a18-b6410b5022a1 | -3.91763 | -47.09616 | 2024-12-02 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43378cb2-83a5-3edb-9d3f-5c28d65cf5bf | -11.13548 | -37.21974 | 2024-12-02 04:25:00 | NPP-375D | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 62abf8ca-a8a8-3585-91ae-6131179074ed | -5.15168 | -44.92342 | 2024-12-02 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77ef2105-e6d1-3d05-8497-9bb76b4081e3 | -3.96847 | -46.89087 | 2024-12-02 04:25:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ceb71531-4f19-36cd-9f4c-7b5167a451e5 | -2.81726 | -53.05701 | 2024-12-02 04:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 28cd9928-8ddc-3009-83f2-4c95082d2665 | -3.17696 | -54.33425 | 2024-12-02 04:25:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4819af4c-2e4d-3543-9a37-a7d016254283 | -4.52753 | -45.73907 | 2024-12-02 04:25:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f1c8522-99cd-35d7-905f-d94239c2846c | -4.18785 | -50.68041 | 2024-12-02 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a072ffd2-5f87-3254-a5b1-fd80ed0c98cf | -4.02206 | -49.94394 | 2024-12-02 04:25:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b3403a56-6962-3ee2-8fdf-fbdeeb82911c | -3.74383 | -51.83645 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f377c984-d1ba-36c8-b13a-764f77f802bd | -6.81697 | -46.77211 | 2024-12-02 04:25:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a6f2f74-d68b-3e0d-a91e-e0933072bd77 | -3.95703 | -46.3062 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6f8ae0b-f389-371a-9ca0-fda0e4b7bbd3 | -11.13597 | -37.2158 | 2024-12-02 04:25:00 | NPP-375D | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 8317fd9c-95fb-3f76-93d1-ea098ef3483e | -4.17078 | -46.56123 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 223d93f8-ff76-3b46-9638-0e1c6cae5a64 | -4.09448 | -46.12117 | 2024-12-02 04:25:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2f0f3e6-01d8-3333-b98d-19f22e011fdd | -3.1875 | -54.33574 | 2024-12-02 04:25:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dcbb268a-cc41-36c1-a944-1f7033bf875b | -3.93261 | -46.71852 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 75d7e0f4-07dc-3785-bc83-a8e228f3d580 | -3.28589 | -50.55629 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98790da1-1b95-377b-8077-581f811ef8ea | -4.08723 | -51.11674 | 2024-12-02 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79cb16b6-449e-34c5-834f-5d789d711e2c | -2.30556 | -53.89523 | 2024-12-02 04:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 967b20ff-e0c3-354c-820c-5bdf253e79f9 | -5.12547 | -43.21373 | 2024-12-02 04:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f4f86fa0-0238-3e50-835f-6b72381182f9 | -3.10761 | -49.50539 | 2024-12-02 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2f83865c-4575-30dc-ab91-41ca13d6a510 | -3.1021 | -53.75192 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e19754d6-c6db-3256-8b27-2ce7c8a27106 | -3.83354 | -46.61588 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8c56207-667a-3a6d-8e3f-90def3574894 | -6.36697 | -47.35291 | 2024-12-02 04:25:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a8ba792d-5cdd-39e3-b51a-7cd3f1942edc | -2.92213 | -54.12438 | 2024-12-02 04:25:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f21dd1e8-72c1-3c0a-9f18-b8da84522afe | -2.71156 | -52.00736 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 803a6b7b-7bcd-351b-8116-56fbd99d1159 | -3.94818 | -46.92464 | 2024-12-02 04:25:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4649f5de-6fee-33b5-96ea-ea0b96ea3e85 | -3.8486 | -46.52101 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 253e2e8c-2caa-34ce-b7b9-c395738b98c6 | -3.95824 | -49.75444 | 2024-12-02 04:25:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b498fb6f-20a2-345c-8b94-be6cf33b49fd | -4.917 | -41.34029 | 2024-12-02 04:25:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 630e41c0-5b2c-389d-9c92-01303401e444 | -3.97676 | -46.72184 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56951475-40fd-3a62-803e-50d8e0d56300 | -3.88889 | -49.9294 | 2024-12-02 04:25:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4638b5dd-c7f0-3c74-91ba-8214e75375e2 | -4.25993 | -50.84875 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a2d9dede-9dda-3613-91bc-93f75fc74741 | -3.90024 | -46.66288 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7896d88-2a19-3c62-b8f3-f9d7870cd589 | -3.03965 | -49.37213 | 2024-12-02 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e2c055b-cd84-309c-a498-b5f6285f49ae | -3.98231 | -46.66496 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c11091ab-447a-3ebb-a84b-ea927d176a43 | -4.53085 | -45.73959 | 2024-12-02 04:25:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91a1547e-2d07-324c-b022-642b578a1dba | -3.7563 | -50.75573 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b03f1f29-799c-36d4-a1fa-b6d620702f8e | -3.88813 | -49.93414 | 2024-12-02 04:25:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f7104e0-ddda-3c85-a4d3-163fb9f5b52f | -6.08021 | -48.0555 | 2024-12-02 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d7459d5e-e5d4-3e09-b7f9-50b544e9afad | -5.18441 | -45.38799 | 2024-12-02 04:25:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3abc55da-7b35-37f5-aa1f-f7defd9a5be7 | -4.90435 | -41.34421 | 2024-12-02 04:25:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| eb415dab-4d07-3eb4-a6e7-55a53f702965 | -3.25203 | -53.92026 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 005b1b7f-6cee-375c-bb76-9c4cec516f52 | -5.12315 | -43.20515 | 2024-12-02 04:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 9bed7ba4-fecf-35a6-a7ff-f11891a9e62d | -4.14415 | -48.24055 | 2024-12-02 04:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bdc32ed-4b15-3fe4-91b4-91ebe1b5fdab | -6.82029 | -46.77264 | 2024-12-02 04:25:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0185b245-8c4f-375f-a328-f81db0c01797 | -3.26851 | -53.64609 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b87aedbb-f4ca-3b61-93d3-c253e3c26013 | -4.87269 | -45.84641 | 2024-12-02 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 674022a7-48c3-369c-b7a5-a1523df4499f | -6.08364 | -48.05604 | 2024-12-02 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e7c2deae-0aa9-30ca-ada8-f2dc54f3a889 | -5.91146 | -46.25172 | 2024-12-02 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 04562efd-986c-343c-872a-696cf16fa0b8 | -3.54389 | -50.18005 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7cbe5989-baf0-3e8d-90d3-6269cebd1738 | -4.17619 | -48.19766 | 2024-12-02 04:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1361353c-ce5d-36f5-8c3d-8b9462815fb1 | -3.8525 | -46.53961 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8803f76-699d-3cc7-8d7b-2c041338d447 | -5.36791 | -44.902 | 2024-12-02 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0fd1af46-fd47-3f7f-afcd-a30632b5b178 | -4.90437 | -41.31767 | 2024-12-02 04:25:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8f9304b8-4586-382f-a122-992685555382 | -3.15409 | -51.11824 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb1234d0-0bc1-35ff-bed2-37fa1edb76cf | -3.77918 | -52.0358 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 4c99937e-fcb4-3145-9d26-8c66d7229ff1 | -3.25877 | -48.89876 | 2024-12-02 04:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 965368b3-5cc9-315d-ab7e-c306fd2226ea | -2.72558 | -54.17612 | 2024-12-02 04:25:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b54be69-7178-3a2d-a00b-7dc1cc69fc97 | -2.99405 | -51.3357 | 2024-12-02 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 00c2aac2-d566-332d-aa71-9b8b0882b7c6 | -10.66285 | -44.49429 | 2024-12-02 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d44caa2e-2070-3bca-ac93-587e38c6ad72 | -4.27432 | -50.68441 | 2024-12-02 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0c9f438e-3e9e-3cf6-9a30-db0e77125548 | -4.65586 | -45.65336 | 2024-12-02 04:25:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9dadc5a-49df-3035-99b7-439c85217b27 | -3.79329 | -46.69611 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bfd20435-b870-3b96-991e-2092e43fb5c2 | -3.33961 | -53.37513 | 2024-12-02 04:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa2505f0-823a-36ea-b8a1-915854e876f7 | -6.14918 | -52.04684 | 2024-12-02 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a761ff6c-0967-3496-ab77-7b3ac52c8c6c | -4.65533 | -45.65676 | 2024-12-02 04:25:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6b0912a-d6b7-3765-aae2-9ae88c142dc8 | -3.02884 | -54.19032 | 2024-12-02 04:25:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4027834-e2fa-38b6-990f-d23bd7899547 | -5.00965 | -44.17268 | 2024-12-02 04:25:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5877a92-abed-3076-bc1c-2b275ab50a9f | -5.58101 | -45.14447 | 2024-12-02 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8b8f9e5f-e412-3439-944e-8dc4fbd4d85e | -3.74528 | -49.68659 | 2024-12-02 04:25:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 00659533-60cb-3aed-90a8-f0583958d8ca | -4.26136 | -47.61616 | 2024-12-02 04:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5e07d65c-dcdd-389e-9070-c90fecb3b54a | -4.07048 | -51.06373 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72d6e792-a03c-3a25-a5ae-7212a2961e9f | -3.7481 | -52.26385 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 13c4f9d2-e8e9-391d-b8e9-eba313bc1ffc | -2.89876 | -54.16504 | 2024-12-02 04:25:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77663a41-cef0-305c-999a-ed81a3b74507 | -3.69049 | -47.11947 | 2024-12-02 04:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e68615ea-f273-3821-b8fa-9ac2607fef6e | -4.04422 | -46.82642 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fff4e0f2-73ef-3f1e-808b-5253d07ac6c0 | -3.7505 | -52.27143 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2718362a-e9d1-3900-ae2e-9d2a79cfb7cd | -2.70408 | -52.00354 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c9d50d6-e77c-3c8d-b162-92b4bca11dde | -6.81641 | -46.7756 | 2024-12-02 04:25:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README43.md)
