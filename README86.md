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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ff2a353-3e91-34ac-9dfe-8ed8fa7b91ee | -6.80039 | -46.88981 | 2025-10-17 04:49:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d922d9d5-b2dd-3e95-9981-dea11f0f51da | -7.45766 | -42.68267 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a82c5c1b-a4b6-3bb1-9e6f-71cc459f605c | -3.90427 | -52.27262 | 2025-10-17 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ccb8afca-a26a-3613-9a28-3cc3b4154ba0 | -4.41978 | -40.17827 | 2025-10-17 04:49:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5ba95537-2f5a-3b88-975c-53bcab1ab281 | -5.6581 | -46.80951 | 2025-10-17 04:49:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43a7a530-71e3-3704-b5e2-11777496fb01 | -2.99001 | -44.31701 | 2025-10-17 04:49:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 448c2d5f-ca96-3ae5-b8aa-8ea19864a33c | -6.20265 | -41.75595 | 2025-10-17 04:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ee1452e9-08ad-37a9-aabf-9b5195892df5 | -7.35919 | -41.90882 | 2025-10-17 04:49:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f260703f-6201-31d2-b377-0cdb05d19461 | -4.95477 | -44.95987 | 2025-10-17 04:49:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a050e4c7-df97-3b53-9fe7-ebf758361f5b | -8.16275 | -43.30801 | 2025-10-17 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ff66aeac-13b9-3c91-bb4e-939854379584 | -7.3353 | -44.15335 | 2025-10-17 04:49:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f94b8e1c-7e13-319f-b42c-0263b5c75d77 | -1.49516 | -47.81133 | 2025-10-17 04:49:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 944f6ed3-973c-3008-89b3-1e12ddd8e04b | -4.56135 | -46.62125 | 2025-10-17 04:49:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86b5b515-28e8-360d-a6b4-2a939efdeb64 | -6.35822 | -41.4878 | 2025-10-17 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a1299026-39d2-3702-a025-4e4ac0c2581f | -7.0394 | -42.73201 | 2025-10-17 04:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 701e12c3-b275-3bfb-bec1-35f064e664cf | -5.23714 | -49.23021 | 2025-10-17 04:49:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 17006243-06ec-3f35-9ef4-99fba2063c22 | -6.94849 | -47.72345 | 2025-10-17 04:49:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6eec7961-c49b-3495-812a-6577f0ef19c5 | -8.25827 | -44.0293 | 2025-10-17 04:49:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0222f1cd-3dbc-30f6-9add-cdbfe662e380 | -6.56022 | -48.04649 | 2025-10-17 04:49:00 | NPP-375D | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 32ae49bd-8197-39c0-9b9b-6aa057cecf83 | -5.81561 | -42.33598 | 2025-10-17 04:49:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cc5a2f65-e261-393f-89a8-89cde18dccae | -6.5451 | -43.92319 | 2025-10-17 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 35a62db6-7d4c-3ea7-b3f9-00232d853795 | -7.95415 | -44.15276 | 2025-10-17 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 86d8c41c-d07d-3ba1-a42f-3dd987015853 | -4.55265 | -50.60696 | 2025-10-17 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16277397-dfd7-335c-b00b-a6a65f3a0892 | -7.05355 | -46.68715 | 2025-10-17 04:49:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| da453b45-8e02-3c58-9d2e-f9f9cf718886 | -2.68859 | -48.70246 | 2025-10-17 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9dc6b2dc-8ef6-364e-92bc-4de8b8ef5198 | -5.51198 | -43.87066 | 2025-10-17 04:49:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d25a2580-5622-3d0c-a5c3-f56ca5f1b124 | -6.29391 | -45.49943 | 2025-10-17 04:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5d1a2ff-27e8-32f4-8957-985fef9e8b00 | -5.52697 | -44.60095 | 2025-10-17 04:49:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7ed936f-b330-3e02-98fb-6fd9419d70b1 | -3.77504 | -43.44452 | 2025-10-17 04:49:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ea2a36f-a07c-3839-bb99-cbfbaed933ea | -3.53049 | -50.31182 | 2025-10-17 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 482a60f8-0615-3d47-8073-66a60509e856 | -7.17969 | -42.18952 | 2025-10-17 04:49:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fc8de7b8-342b-3fcd-8a5a-cc554852c3d8 | -5.22448 | -46.19407 | 2025-10-17 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5724442f-a0e5-39b9-8c77-fbb15e4467db | -5.2573 | -44.21319 | 2025-10-17 04:49:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec2b07ae-69a6-3280-b313-780110437739 | -6.30575 | -46.06023 | 2025-10-17 04:49:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| accdd76d-7879-3890-a5de-734c0df7277f | -4.60883 | -50.91349 | 2025-10-17 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ea96f17-84bb-3bf1-a071-dbeb14b02eb3 | -7.0543 | -46.68208 | 2025-10-17 04:49:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fa26364f-904c-3338-b95c-80bd1adc80cb | -2.86743 | -50.73529 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 90b1fee7-9e07-3ce2-9e05-d0cec21898ff | -7.29216 | -41.94916 | 2025-10-17 04:49:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 080dea2d-3b1b-3598-bcc5-9b9f5cddff3f | -5.83411 | -42.24119 | 2025-10-17 04:49:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a2a30911-4e38-3199-ac9c-4d6ac8ff78dc | -7.40297 | -44.75023 | 2025-10-17 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 87773f71-0039-3022-825b-02a2b503c234 | -6.28919 | -45.50229 | 2025-10-17 04:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e731690-212d-3e1f-968d-beeb4ca68c0a | -5.60658 | -49.03025 | 2025-10-17 04:49:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e948e61f-5521-3686-b70a-6027591b2150 | -5.86791 | -44.84116 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f1ab062-a06c-31ad-80e5-a00f806fee27 | -7.20068 | -45.49987 | 2025-10-17 04:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cab0d23a-02e5-3ba1-aa73-f2ac090842ad | -6.77261 | -46.94458 | 2025-10-17 04:49:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72fb7670-7091-3f62-a2e9-ad199ee23ba6 | -5.21262 | -46.19242 | 2025-10-17 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3974ec4-ef0f-310d-8065-0e5a269c1a38 | -4.26622 | -49.21597 | 2025-10-17 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abd39c08-8f43-3ae5-887c-73d769fb2d99 | -8.28401 | -43.38515 | 2025-10-17 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 635a6504-34c9-3a8a-bf81-3394972dcbff | -8.20739 | -43.97477 | 2025-10-17 04:49:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 631fcbaf-8a4c-351f-a1a6-26ebfd8405e8 | -6.70368 | -44.39737 | 2025-10-17 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69fe4eda-ba30-3b42-9725-baf3e3d4f3a9 | -6.51633 | -46.51477 | 2025-10-17 04:49:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 115c437b-6cb5-31ce-b862-28db3d04d047 | -6.74468 | -42.36625 | 2025-10-17 04:49:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 176260ad-ab91-37b1-ba7d-a79bfdc65df4 | -5.16059 | -46.27077 | 2025-10-17 04:49:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15e15bf6-bc2a-3237-a5a8-727ab6d89e91 | -5.91281 | -44.74742 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| c4d6c3c5-54b8-3457-b532-49a0cff519fe | -6.83425 | -42.41457 | 2025-10-17 04:49:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 90c3174d-9846-3c38-8129-4fd85765aed9 | -8.18705 | -43.31733 | 2025-10-17 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0c2d16f2-74e6-3f44-bacc-6840bc15e54d | -2.95453 | -51.96795 | 2025-10-17 04:49:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 490c4c1c-1d6b-3aab-ab18-2dde87ae0d5a | -6.22709 | -47.04222 | 2025-10-17 04:49:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa63d933-628b-3949-af08-296f9ab65cb6 | -3.97867 | -42.48846 | 2025-10-17 04:49:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e596eb86-5812-3f02-844b-e89fbfc9bd76 | -8.289 | -43.38594 | 2025-10-17 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4da3f31f-dc3e-3ec6-a497-90386ecb17ee | -7.84038 | -45.45622 | 2025-10-17 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb7539f5-7c77-358f-84b2-a40fb51bc25d | -1.48359 | -55.68041 | 2025-10-17 04:49:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 299ec3cc-7d20-34dc-be7f-fe479d5e0c7d | -3.65801 | -50.27153 | 2025-10-17 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6470e4b8-12e1-3529-aeda-7eb451ec7bed | -7.20607 | -45.49249 | 2025-10-17 04:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 192e9684-7356-30d0-9032-10b654b87f2d | -3.87225 | -51.95042 | 2025-10-17 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d9d29f7-42ba-3979-9054-a12d85e4a244 | -7.46679 | -42.65548 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1537ef52-1d84-3c7f-a443-d66a3cceba51 | -5.28971 | -47.92707 | 2025-10-17 04:49:00 | NPP-375D | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2df6a85a-2045-3d56-85b7-7867b8e873ac | -7.47968 | -42.75766 | 2025-10-17 04:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ec44aa6c-a64b-3be9-a618-9ded5973364b | -5.79071 | -42.5008 | 2025-10-17 04:49:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 86a9602d-a0e1-31ba-bfff-fc1b1b24340a | -6.30657 | -45.58622 | 2025-10-17 04:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b71077f-931c-3d4d-a66d-6b6c7655edff | -7.20238 | -45.48793 | 2025-10-17 04:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4bc40ec8-6eeb-3726-97b1-78e90b88964f | -6.34403 | -41.51566 | 2025-10-17 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3380d68f-b094-3ca4-bbb7-6ad215189fcd | -3.27769 | -50.04575 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb0a8410-7c9f-3aba-be06-8298a88e8a77 | -5.49409 | -43.07058 | 2025-10-17 04:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7885841f-87fb-3252-9e64-11c3f5d98c4f | -2.79824 | -48.93991 | 2025-10-17 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1b6f6825-40a6-39ef-bd52-69b3cd103c75 | -4.8405 | -42.7625 | 2025-10-17 04:49:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5d1fd49a-5bdd-362b-9499-7129dfc3f88e | -2.74471 | -49.39184 | 2025-10-17 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 9e46bbe2-49ff-3a3b-a6d9-5c5f0598d719 | -7.46094 | -42.15202 | 2025-10-17 04:49:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bd8f8f27-0679-32e9-8ba8-47472111840f | -7.73741 | -42.507 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7feab097-387d-3c54-8eb4-de3d48539e26 | -5.50734 | -43.86993 | 2025-10-17 04:49:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6c9d2d6c-6fa0-39dc-9e5c-6c8948a1ca0a | -7.20124 | -45.49588 | 2025-10-17 04:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 14b4cd2d-b5e4-377f-8bad-3ad3be7f7b34 | -7.95507 | -44.11155 | 2025-10-17 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 333237d8-5432-39ac-82d8-2ebd4e4e59ce | -4.87933 | -50.89254 | 2025-10-17 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8ee56abc-8ce0-3f34-9fd9-197689f03ea7 | -2.86633 | -50.74223 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efc37843-79d5-31e0-9ee4-700c2050af9b | -7.74269 | -42.50768 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 01d0f6cc-c0c3-3b62-84d9-661acf4c6340 | -5.81518 | -42.33904 | 2025-10-17 04:49:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3dc32012-f766-31d6-b40b-9f953cf6b843 | -5.88681 | -43.89458 | 2025-10-17 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b1207f11-b6d7-3f1a-8c36-a9b9446464e4 | -5.87207 | -41.23874 | 2025-10-17 04:49:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4bcaaaa9-0c66-3df5-8628-71c59ab0180b | -8.60889 | -40.20088 | 2025-10-17 04:49:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ac292412-2bf1-3a89-a3e8-48d52bba9437 | -8.60951 | -40.1961 | 2025-10-17 04:49:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4c67c648-6346-37fe-8e7f-1f4511d3974c | -6.27069 | -52.62907 | 2025-10-17 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b808b25f-634b-3ca6-9697-552256a9c01c | -7.09166 | -44.26022 | 2025-10-17 04:49:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7378fbe6-ebcb-3534-9e6a-15813d5a0caa | -6.53838 | -55.05285 | 2025-10-17 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d43ecf79-4ef6-3998-95f2-b67cfa0e2be2 | -6.58908 | -43.93171 | 2025-10-17 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9eef32f6-fb16-3a4e-8a92-2fce77766046 | -6.34834 | -41.51909 | 2025-10-17 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9e9165b8-f1d4-3938-a691-236d4999e8ea | -3.97689 | -42.49752 | 2025-10-17 04:49:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 188b3789-6235-3391-a34e-549350599f75 | -6.69592 | -40.8637 | 2025-10-17 04:49:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 80f14a97-b7ae-35b1-abe0-e0c18a4c0576 | -3.41726 | -48.88371 | 2025-10-17 04:49:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 48adde12-3e82-35e2-b4f6-80606bc08b88 | -3.13251 | -50.21375 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 44c881d9-e5c8-34f9-996f-479382428007 | -6.47129 | -41.84764 | 2025-10-17 04:49:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README87.md)
