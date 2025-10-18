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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e8503cc-e2b3-3201-ad04-632a96083bf7 | -4.1525 | -42.1989 | 2025-10-18 14:40:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 97.4 |
| 7e72ca0a-594f-34a2-bee2-aa834fc32ad2 | -13.6373 | -43.9208 | 2025-10-18 14:40:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 5aa67df7-067e-31ef-a032-25361bf03485 | -6.823 | -41.705 | 2025-10-18 14:40:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 78.9 |
| 3270f61c-0c4e-3258-a64d-14f993735788 | -6.4637 | -41.8351 | 2025-10-18 14:40:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 78.2 |
| 864616e0-29ce-3148-82cc-e068d54c87f7 | -11.3996 | -44.0995 | 2025-10-18 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 259.5 |
| 6d5a9e2d-1522-38db-b75d-1a6f8aa7dc6c | -13.6363 | -43.9684 | 2025-10-18 14:40:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 8b5056dd-7c6a-3a1a-bcc9-f22c68eca317 | -5.9518 | -42.2379 | 2025-10-18 14:40:00 | GOES-19 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 68.1 |
| 50bb2994-4370-3b56-96fa-e0a25064e649 | -12.7251 | -50.5184 | 2025-10-18 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 198597de-00e0-3018-80cc-1f135ae10e07 | -8.2098 | -43.9944 | 2025-10-18 14:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 6a32e50e-bd1c-3f47-8ee3-1ba8c7c33096 | -10.514 | -43.3815 | 2025-10-18 14:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 253.1 |
| bd197fc6-1895-3036-9dfa-eb8bc2a338db | -12.5059 | -45.4866 | 2025-10-18 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 144.9 |
| d16dfcbf-8fe2-38b0-ac7e-d1e504f2ab62 | -10.1147 | -44.5338 | 2025-10-18 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 73f7a420-b054-3f27-abfd-5f6a963e8600 | -11.3767 | -44.3131 | 2025-10-18 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 4013a44f-bd1f-342d-a793-a64f64f710f8 | -5.7035 | -42.6841 | 2025-10-18 14:40:00 | GOES-19 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 63.9 |
| cd6a9e3f-b653-3158-8298-72f64c32e483 | -6.0644 | -42.2522 | 2025-10-18 14:40:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 62.9 |
| abcb4bd9-a94e-36d7-98fb-e5b7b841fe82 | -9.8167 | -63.1489 | 2025-10-18 14:40:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 4eb5f031-5a7b-3af8-ae78-55d4252e8aac | -6.1737 | -42.5985 | 2025-10-18 14:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 78.2 |
| 994604c4-53d0-3c79-b129-2b604cb8edbe | -4.4845 | -42.8631 | 2025-10-18 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| b01e43d6-740b-3bcf-b74b-70fcd614dd7c | -6.333 | -45.4934 | 2025-10-18 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 2249584f-80cc-37d2-88ba-1fb457ead484 | -8.1909 | -43.9964 | 2025-10-18 14:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 114.8 |
| d2e93119-93e9-366b-bed7-d765af3fe17b | -10.1337 | -44.5313 | 2025-10-18 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 54e32b93-59e7-367b-865f-066f1ae4215a | -7.9817 | -44.1342 | 2025-10-18 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 76d065d1-9eca-3de8-8caf-d5b7fab822ed | -12.487 | -45.4664 | 2025-10-18 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 338.9 |
| c6921350-5c2d-30ce-9084-aef2726c6aca | -6.4257 | -41.8625 | 2025-10-18 14:40:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 68.7 |
| 86917f3e-6f39-3eb3-807f-7715c8182f23 | -8.5419 | -44.5824 | 2025-10-18 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 3aca7c22-3282-3147-bc65-15e431746a28 | -4.5033 | -42.862 | 2025-10-18 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 31f3b12a-a32f-380a-a955-32c0ba0ce7fc | -8.2092 | -44.0409 | 2025-10-18 14:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 8b893756-a25c-3615-ba31-ab3b070ed58c | -6.4634 | -41.8591 | 2025-10-18 14:40:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 90.9 |
| 958d69e8-0af5-31ed-bb78-a0f83ae65b2e | -6.2012 | -41.7389 | 2025-10-18 14:40:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 72.8 |
| f0e17e07-3506-3976-b16a-3f2e80e36919 | -5.7784 | -42.7018 | 2025-10-18 14:40:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 77.0 |
| b3c817b7-857b-392a-88d5-df0e2a285ced | -8.2278 | -44.062 | 2025-10-18 14:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 81.9 |
| d0ddbaa9-3e74-3aaf-a5c6-c8234b9a0eeb | -5.3837 | -42.8026 | 2025-10-18 14:40:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 71.1 |
| 706335c1-90b8-3496-bf4d-3d19d0c390e8 | -8.1912 | -43.9732 | 2025-10-18 14:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| b6ee0374-034a-375c-a413-f6d60b150046 | -12.7063 | -50.4993 | 2025-10-18 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 147.8 |
| b3b004ee-1365-3824-8e26-9beefcfeceb6 | -4.171 | -42.2215 | 2025-10-18 14:40:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 107.9 |
| 72d8f811-766a-36ea-b4bd-ddc946fb41b4 | -5.8907 | -44.7559 | 2025-10-18 14:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 51.5 |
| d1afc094-89ef-352a-a8bb-5158f1bcf81e | -6.5959 | -45.4049 | 2025-10-18 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 978c2814-6f0d-3f78-b2e5-8519ddf1742b | -5.854 | -42.6486 | 2025-10-18 14:40:00 | GOES-19 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 80.7 |
| 5d8f43d6-6711-3a08-a805-a8737ecb436c | -6.314 | -45.5174 | 2025-10-18 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 4f6c4b53-cc5f-3d6f-b209-689958b827f9 | -8.2467 | -44.06 | 2025-10-18 14:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 70.0 |
| bfacebeb-ca42-308b-a760-c841497bcf24 | -10.1143 | -44.557 | 2025-10-18 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 8495edf4-501f-31af-8d28-9911a3161c8a | -6.3328 | -45.516 | 2025-10-18 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| ab60d343-4a94-3e45-a1e8-813759532da8 | -6.3138 | -45.54 | 2025-10-18 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 907d6ec4-4171-3f33-9402-c9830740e5b4 | -10.236 | -44.0766 | 2025-10-18 14:40:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 21c835b9-f995-3397-a288-059844d69bf1 | -6.3679 | -45.7609 | 2025-10-18 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| e8e26de5-ea5d-31b2-883a-3144a0d1a0dd | -6.3492 | -45.7623 | 2025-10-18 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 3c314875-09a3-34c3-89c9-0d691b2f9baf | -8.2101 | -43.9712 | 2025-10-18 14:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 123.5 |
| b3fa3f18-2b0f-36d4-9946-abff83e5d601 | -15.8019 | -43.2548 | 2025-10-18 14:40:00 | GOES-19 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 192.1 |
| 0dbf0d09-0a6c-34de-99f7-552ec90db227 | -6.4443 | -41.8848 | 2025-10-18 14:40:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 89.9 |
| 7bca1dce-3a23-3ccb-9ce2-8da2154a5d1b | -8.3698 | -44.7616 | 2025-10-18 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 04576430-8c07-3199-ad6c-1feeb2b3d61f | -10.255 | -44.074 | 2025-10-18 14:40:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 58.3 |
| b8e931bf-b2bc-3247-b76c-f86fca6d8083 | -8.2464 | -44.0832 | 2025-10-18 14:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 96.6 |
| ec4244b8-801b-37bd-b37f-94f65dc64bca | -6.3517 | -45.4919 | 2025-10-18 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |


