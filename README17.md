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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55b4d46e-57a9-36c9-9d71-3d7bda143347 | -2.83696 | -48.10543 | 2025-11-05 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc405e23-a43f-335f-8b68-6f81e7e48b15 | -5.27004 | -44.1418 | 2025-11-05 04:12:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a7a383e-5ea7-30b4-92b7-09dd3cf3b630 | -2.81741 | -45.14785 | 2025-11-05 04:12:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f187503a-bdaf-3991-b6ec-b95a23a0f51f | -3.48658 | -43.62424 | 2025-11-05 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 62926c9f-6274-3bed-b24b-4d8fea59f643 | -5.24634 | -45.73933 | 2025-11-05 04:12:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c3520df6-c390-3e4f-a111-3918b8361f9e | -4.18344 | -48.59024 | 2025-11-05 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bc44244-d270-3451-8249-570908742324 | -3.06724 | -52.63264 | 2025-11-05 04:12:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd17de69-f515-32d4-984a-735323d0fb48 | -2.82813 | -49.4194 | 2025-11-05 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecaf26de-6a63-3d72-9aa9-3047dffe1e91 | -4.10643 | -48.02555 | 2025-11-05 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 5d9ac8d2-3234-3f3f-bf38-d2ce0cd7d7cf | -3.96654 | -43.78674 | 2025-11-05 04:12:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c1b98b5f-e568-3d3b-9da9-91f47d40b8d3 | -2.81677 | -45.15189 | 2025-11-05 04:12:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1607aba-b53a-3536-a179-18786cd0ab48 | -4.45823 | -43.21767 | 2025-11-05 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 648e9f78-26d6-3cd2-ba06-a07ed2728190 | -3.65466 | -44.79841 | 2025-11-05 04:12:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ab8adec0-ee3d-365e-bb5b-cf2d3a94f118 | -4.59653 | -46.56589 | 2025-11-05 04:12:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a724ea34-d583-390e-8c0e-d6d0555db96c | -3.50251 | -51.55272 | 2025-11-05 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df43f75b-5dae-3c2c-92e4-e16246712561 | -4.11122 | -48.02229 | 2025-11-05 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0ba7d73d-7f51-36dc-b89c-2af5a725f559 | -3.7649 | -51.71656 | 2025-11-05 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c377f729-d653-31c8-b18e-7fda49fb73e4 | -2.48498 | -55.73317 | 2025-11-05 04:12:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a66d1448-f6a6-3a32-ba51-a4f2de69ed7a | -5.0302 | -44.78975 | 2025-11-05 04:12:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d804a76-025f-3e5c-9d1f-ae56b37c3331 | -6.09593 | -41.70766 | 2025-11-05 04:12:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 844e34ee-25ba-3a98-a2b5-9b685c6a2284 | -4.55301 | -45.5928 | 2025-11-05 04:12:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e95579f-802d-39a6-b17f-5c9d75dfb175 | -3.23004 | -43.43874 | 2025-11-05 04:12:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| fc07431a-7474-31c2-b48e-c673137d3d18 | -4.86122 | -44.61833 | 2025-11-05 04:12:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ce7a015f-ed24-3797-a33e-2c38f3c640b8 | -4.81783 | -45.76678 | 2025-11-05 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a07e3b5-f688-3f2a-846d-c5a2b98ddfa1 | -3.05373 | -40.11737 | 2025-11-05 04:12:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d4c21d47-c2e0-31e1-8f97-7fbdc17c53ef | -4.22133 | -46.89011 | 2025-11-05 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2430387f-45af-378f-81b6-8e34336a3ab3 | -3.81552 | -51.28897 | 2025-11-05 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9657e7d-0dd4-387f-97bb-d4a2cc8ad729 | -5.92078 | -41.37182 | 2025-11-05 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 27f4465f-3502-389d-82af-3af9141f21f5 | -3.40845 | -44.44595 | 2025-11-05 04:12:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2ff43055-70e0-3ba3-b795-adb74e810bad | -4.80898 | -38.56835 | 2025-11-05 04:12:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c42de5dc-9d0e-379b-af14-58f115336265 | -3.4043 | -50.84206 | 2025-11-05 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a0954bf-c95d-322a-8202-b274b6a376e8 | -4.04992 | -43.478 | 2025-11-05 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9792a734-4dce-3879-a655-5a5435b81377 | -1.29819 | -49.15845 | 2025-11-05 04:12:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| cbc67e9e-0273-3d73-a98c-0e888f3ad771 | -2.48784 | -44.04123 | 2025-11-05 04:12:00 | NOAA-20 | SÃO JOSÉ DE RIBAMAR | MARANHÃO | Brasil | 2111201 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f01e9691-9304-38c7-994e-6522ac6ad0b3 | -3.87801 | -45.59708 | 2025-11-05 04:12:00 | NOAA-20 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce2079c6-6367-3577-bd0f-908e03e1a518 | -3.98866 | -47.71887 | 2025-11-05 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9fa37578-980a-3258-ada6-df2d667633f6 | -5.62562 | -41.08583 | 2025-11-05 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 568195e1-29fa-374c-8c30-e99236c9f28f | -4.47094 | -43.22322 | 2025-11-05 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 616af457-31b5-3796-82e9-50e47329b6d3 | -4.55554 | -46.76743 | 2025-11-05 04:12:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5ea39fae-b00c-360a-90b0-14dc0f3aa0f2 | -4.41324 | -48.94655 | 2025-11-05 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| ac8f437d-7350-3951-98a4-ca1dcaf02e10 | -3.96883 | -41.81918 | 2025-11-05 04:12:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 292bba67-a4ea-3594-999e-71ed7eae9b64 | -4.40884 | -48.94585 | 2025-11-05 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| ae0eb3db-1baf-3d68-8dd0-afbd8133b33e | -2.83988 | -49.40623 | 2025-11-05 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 208f993d-8003-39ab-aa99-831f68d18728 | -4.41251 | -48.95086 | 2025-11-05 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| b56d1d0a-e557-30d4-9493-98c237da2f48 | -3.24154 | -50.79411 | 2025-11-05 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d8d469b-c3ab-3b43-bd21-58966d125397 | -4.1829 | -46.41453 | 2025-11-05 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8539e719-f965-3296-8f08-568a85baac69 | -4.51513 | -42.08191 | 2025-11-05 04:12:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bde2b5b0-3067-3535-a660-da858521a5c7 | -3.65998 | -44.79886 | 2025-11-05 04:12:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80fba738-83be-3631-99f8-14120e618c0b | -4.8578 | -44.61777 | 2025-11-05 04:12:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c72fc9d-cb97-370c-8560-92a0dbc75d9e | -4.79839 | -45.93023 | 2025-11-05 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4dd31fd5-1bac-349c-b1e9-1abac89094c9 | -4.46102 | -46.6353 | 2025-11-05 04:12:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b496a1e-fcb3-3823-9b33-6ab30964eb4d | -3.99969 | -45.29574 | 2025-11-05 04:12:00 | NOAA-20 | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0cf92f34-6914-3e7d-8aad-8cd6d8434a41 | -3.50817 | -55.50432 | 2025-11-05 04:12:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 12097d22-d849-3c9f-a782-cd7c22a33bbc | -4.46762 | -43.2227 | 2025-11-05 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9f373258-b9c7-3c06-9b67-873d1cd5d99f | -1.24737 | -49.14507 | 2025-11-05 04:12:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a29f7e9-e960-3b5f-a690-1a28bc89b209 | -4.29227 | -43.79066 | 2025-11-05 04:12:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4549aafe-42b5-3a35-ac83-fddb4349235e | -2.41959 | -49.30375 | 2025-11-05 04:12:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f1544c1b-c615-3317-a2da-ff4ac727d85a | -5.02971 | -43.62238 | 2025-11-05 04:12:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f6cbcc90-8866-3934-93e0-2964b570b19f | -5.41456 | -44.84187 | 2025-11-05 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0dcbf963-aa53-3247-9709-d637e16ae717 | -2.72388 | -47.39267 | 2025-11-05 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3c9f51d3-2d4b-3549-bf8f-180cc6cf3e04 | -5.31738 | -37.57816 | 2025-11-05 04:12:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5ea73f43-baf3-31a9-8710-38167d1d5ccd | -4.29619 | -43.78765 | 2025-11-05 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85c65879-4170-3e43-b1fa-5c6d458bf8fd | -5.35769 | -44.73744 | 2025-11-05 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 441be216-eb1c-3889-b5fa-448364cda747 | -4.52042 | -41.96211 | 2025-11-05 04:12:00 | NOAA-20 | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c2ad060d-0042-383e-ba8f-a7de3e05189d | -4.33027 | -45.87856 | 2025-11-05 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b6bc622-a351-3c44-bb71-cec91ee4e294 | -6.4519 | -39.1143 | 2025-11-05 04:12:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 4829b1be-97f1-33b5-a5c1-926397d1bc2f | -6.1557 | -41.64713 | 2025-11-05 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f17a02b8-ba1f-3858-bbc3-aba75ae300ac | -4.46707 | -43.22617 | 2025-11-05 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 96178d47-d4bf-34e3-8d86-9503a1fd4447 | -4.70802 | -48.14158 | 2025-11-05 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11ff98a3-1c96-3f21-84ff-b0f404108601 | -4.17404 | -40.98098 | 2025-11-05 04:12:00 | NOAA-20 | CARNAUBAL | CEARÁ | Brasil | 2303402 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 98924e71-6e42-3dc0-8f00-16b933ad72a3 | -4.75885 | -42.65066 | 2025-11-05 04:12:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| c1fa51b3-277c-329e-80fa-d62cbb270426 | -2.83442 | -49.41029 | 2025-11-05 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ededf1c0-8b32-340e-becd-116c65ea0b01 | -5.92589 | -41.29464 | 2025-11-05 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1815dbd0-39ec-3a44-846d-ccb60de6309d | -5.45344 | -45.4038 | 2025-11-05 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 34.3 |
| b2568b39-981b-3b5c-b10c-5becbcb48736 | -5.61486 | -41.08784 | 2025-11-05 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 08e7d8fd-32b8-3300-b235-95d7c03427e0 | -4.59761 | -49.55482 | 2025-11-05 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fbb59638-b55c-3e73-9b56-525ddbaa951c | -4.10411 | -48.02437 | 2025-11-05 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5a07ec8d-aa90-3e1f-a0f6-287818ca0e5c | -3.06742 | -47.77605 | 2025-11-05 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fae852bc-9960-3bbe-b19a-b12efd4d835b | -3.81905 | -48.66606 | 2025-11-05 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| afce3447-a467-311e-9011-19d3ed21172f | -4.28062 | -46.93948 | 2025-11-05 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| aa171ca2-63a2-3c3c-9333-8e5c3ed8bf18 | -4.37944 | -46.27389 | 2025-11-05 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d90dc5a-35c6-371c-afec-0715873cf96f | -4.32308 | -44.47346 | 2025-11-05 04:12:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8340692c-27ae-3248-9fd0-c741e297b33e | -4.6047 | -43.89839 | 2025-11-05 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 601b0646-f181-3f7a-9e76-ce7018a3e682 | -3.48103 | -49.5966 | 2025-11-05 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff415138-4899-3ff5-a4de-a07d7d88a394 | -3.49607 | -43.62936 | 2025-11-05 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6affe510-bec3-30bf-aac7-8d0fc4aefc79 | -5.91854 | -41.29728 | 2025-11-05 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ae2cb1c0-e581-3891-b1e0-636918bc2983 | -2.68777 | -48.46603 | 2025-11-05 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 17a4a888-5145-3790-8e0d-64f6369ce276 | -3.5883 | -50.1655 | 2025-11-05 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c628a513-7089-3c7b-8d09-38fd6fb2994e | -5.47448 | -43.58191 | 2025-11-05 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 4a78f512-3673-3212-b47c-457911cfa6cf | -5.63013 | -41.12389 | 2025-11-05 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ce2c1f80-f36c-389a-9d7d-f27b5b80c960 | -4.36223 | -50.8856 | 2025-11-05 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a0f4d1f-ad73-3ea0-aba7-922632a7b9d7 | -1.21283 | -49.1369 | 2025-11-05 04:12:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 974a1549-b1b8-3ca7-ba94-eef03f9ab9ff | -4.66949 | -46.30666 | 2025-11-05 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 70810b1c-af2b-3165-8caf-292e4eeb0fa6 | -3.23363 | -44.39974 | 2025-11-05 04:12:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7778e49-acb4-39e7-9e57-f7a143276279 | -3.31557 | -45.33803 | 2025-11-05 04:12:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a35ed7dc-642e-3f02-8b32-2c8a7eba50b5 | -5.64231 | -43.29578 | 2025-11-05 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 65842ffc-02b0-307b-95df-7b61b7473a16 | -3.83717 | -44.55045 | 2025-11-05 04:12:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de547128-e16b-33d2-bfb0-dee62d06caed | -3.21869 | -44.40505 | 2025-11-05 04:12:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8598fa0-8c6e-3688-a975-524093827ca5 | -4.60806 | -43.89892 | 2025-11-05 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da8e05e8-c1c6-3bfc-bcc3-372017c8b6af | -3.48154 | -43.63434 | 2025-11-05 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README18.md)
