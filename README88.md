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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b5d9177-caa0-3ba7-881e-4c6caf5b1619 | -4.3562 | -43.91048 | 2026-10-06 15:35:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 749a48c2-6b40-38c6-96c9-7dabc3dc8848 | -6.89515 | -43.67936 | 2026-10-06 15:35:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 5756586a-88e7-3bce-ae80-4cca7fdeec4d | -5.1305 | -42.97711 | 2026-10-06 15:35:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 47929435-e807-3527-b0e9-4a26bc88c7b0 | -7.42343 | -39.48265 | 2026-10-06 15:35:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 16.8 |
| a70863e6-091c-3625-9ec3-2ba05d6d39d2 | -3.97332 | -41.54469 | 2026-10-06 15:35:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 34c94bd6-2718-319b-baa3-e2f2f88859f0 | -3.27176 | -41.85022 | 2026-10-06 15:35:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 6162ce59-17a4-3b8f-a7a5-6834c8c97c5a | -6.95062 | -41.49419 | 2026-10-06 15:35:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 646c6e51-2d1f-3635-9969-4011ed226a4a | -4.3076 | -41.77769 | 2026-10-06 15:35:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 22.3 |
| 202a403d-0de3-3f29-a946-cccb77ebb941 | -6.84105 | -39.5372 | 2026-10-06 15:35:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 3d54116b-0ce0-32ce-be9b-9332904795e0 | -4.79922 | -42.15556 | 2026-10-06 15:35:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 32.5 |
| 3222e55b-13f9-3dce-9b96-8ff9d6d76d81 | -7.03912 | -42.3054 | 2026-10-06 15:35:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| fa4286a7-ad8b-382e-877b-7ee164be2928 | -3.95532 | -41.5474 | 2026-10-06 15:35:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c500fae8-b598-3f88-a846-5cd9e5e2dea3 | -6.83644 | -39.54459 | 2026-10-06 15:35:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 22.6 |
| a6f8f506-efef-34c1-9834-2fb1a012cd68 | -3.89273 | -42.50114 | 2026-10-06 15:35:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| eef89b8f-ab8e-326c-9978-ebe2a4ba4342 | -3.27108 | -41.8456 | 2026-10-06 15:35:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 8ee4f415-d17a-3d56-b5f2-b9a07f1d5df5 | -3.10505 | -41.16261 | 2026-10-06 15:35:00 | NOAA-20 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| c149cf00-59cc-31d6-99a1-75bec287473c | -3.76964 | -41.69449 | 2026-10-06 15:35:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| f420ec74-bef5-3ff5-8db8-a63e7fabb755 | -3.17022 | -41.40712 | 2026-10-06 15:35:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 66fdb4a1-8800-35eb-a35f-8c304a66d03b | -6.0755 | -43.90215 | 2026-10-06 15:35:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| c299cd4a-0fda-3129-9212-66ec760e2cea | -4.53986 | -43.71888 | 2026-10-06 15:35:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| e0d3e423-2b8b-326a-9d3b-c2d4c06a1089 | -5.94555 | -41.36506 | 2026-10-06 15:35:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 846c79dc-090d-3325-a809-27992972225d | -5.53732 | -40.76102 | 2026-10-06 15:35:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 1e1f29ed-1a91-377d-99b8-dc047459486f | -4.54299 | -37.82494 | 2026-10-06 15:35:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| cebb92f3-ab62-3f52-b2a8-3c48f6046932 | -5.96578 | -41.37641 | 2026-10-06 15:35:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 2d6d08e9-3aa7-36bd-ba57-c515922fd064 | -6.02173 | -42.26621 | 2026-10-06 15:35:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 17.9 |
| 12475403-ae11-37c7-9e96-f071cc97bc00 | -7.70658 | -40.08581 | 2026-10-06 15:35:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 8.0 |
| dcc5d4b6-624d-3797-b96e-c9e551a974b4 | -7.48221 | -42.7971 | 2026-10-06 15:35:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 6eb32eb9-6a56-3105-9bb8-64261c9eb434 | -5.47003 | -41.22355 | 2026-10-06 15:35:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 36.0 |
| 9afdc93a-79fc-3fe9-8383-f38a3137dcca | -6.62191 | -37.88647 | 2026-10-06 15:35:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 10.3 |
| e81c7f85-41bd-3293-9369-ccff421d34da | -3.68216 | -42.92606 | 2026-10-06 15:35:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 72e44d34-33b6-36b1-82f4-aa3e0c9e76a3 | -3.81268 | -41.69316 | 2026-10-06 15:35:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 6728b16e-7bde-3b68-ab4c-b720e415df2f | -5.72512 | -41.63037 | 2026-10-06 15:35:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3083feb7-a074-38df-92a8-c3c97a34f4aa | -6.87391 | -43.68278 | 2026-10-06 15:35:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 9fcc3a31-096c-3c60-bb96-14091a457246 | -6.0289 | -42.27068 | 2026-10-06 15:35:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 5a11c4ad-bb37-3c0b-bb45-4dfc6d5f1671 | -3.13523 | -40.07809 | 2026-10-06 15:35:00 | NOAA-20 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 3163bb01-e188-3c6a-9ab9-a69f22eec8e5 | -4.50763 | -43.69064 | 2026-10-06 15:35:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 02a3f34b-f285-358b-83e2-d0ac00ab0bee | -3.30706 | -43.27216 | 2026-10-06 15:35:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 34d4a7a4-d470-3a75-9a6e-72826672c79c | -5.45484 | -37.51391 | 2026-10-06 15:35:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 1f09c7f0-587b-3d2d-b786-058c1ec3b19d | -6.02314 | -42.27944 | 2026-10-06 15:35:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 28.0 |
| 56f7571e-fbb8-352d-8118-734a5eb6e8f7 | -6.32392 | -43.75298 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| d69a982e-0339-3dac-9c50-972f1f740933 | -4.70513 | -40.27584 | 2026-10-06 15:35:00 | NOAA-20 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| c0622c11-77eb-3e94-9340-ce678b75ccdf | -3.73381 | -38.75778 | 2026-10-06 15:35:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 2add99aa-ce99-3697-b985-50450c93c27b | -3.77635 | -41.69815 | 2026-10-06 15:35:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 428ba1a5-56b6-35c0-98f2-94c80b7fbcd7 | -5.94582 | -41.32164 | 2026-10-06 15:35:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 568177b4-cdaa-36cf-8d29-03bc672ea0c5 | -4.80554 | -42.1547 | 2026-10-06 15:35:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| bab4d761-ce26-3d6c-8271-fd09dd47c837 | -6.93502 | -43.67603 | 2026-10-06 15:35:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b8338dfd-3714-3685-addc-6db4b82a218d | -8.83344 | -41.10047 | 2026-10-06 15:35:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| f785b413-d0d6-3fcc-8ed5-b3f9cda822de | -6.01742 | -42.28346 | 2026-10-06 15:35:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 31.9 |
| eb5d25eb-4fb9-39c1-a84b-142e41824cdd | -4.30692 | -41.77296 | 2026-10-06 15:35:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 7d8ed06d-4ea7-30a9-95f3-79e8c1b7ce8a | -3.88461 | -44.34859 | 2026-10-06 15:35:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 42aa0906-2b61-3b1e-bfa9-6cb1b32a101f | -7.4233 | -35.38319 | 2026-10-06 15:35:00 | NOAA-20 | ITABAIANA | PARAÍBA | Brasil | 2506905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| de9ebccd-78fb-3b59-9200-cbba1be4b287 | -4.5466 | -37.82697 | 2026-10-06 15:35:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 54a4fd71-4cfc-3844-b98c-51253378e0e0 | -3.80533 | -41.81195 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 58.3 |
| 8840ace9-0ece-361b-936e-4f4b786661c6 | -6.9119 | -37.65536 | 2026-10-06 15:35:00 | NOAA-20 | CONDADO | PARAÍBA | Brasil | 2504504 | 25 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 15c4abef-577e-3ab1-8b1e-3f7728d5d29b | -5.7443 | -41.63227 | 2026-10-06 15:35:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c01a7414-dfe5-3982-93ac-c2257e7578fb | -6.32548 | -43.81797 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 03c8535f-459a-3b20-855e-4cab780f9b40 | -3.81359 | -41.69011 | 2026-10-06 15:35:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 74bc74d6-f4d8-35a3-a5f0-75f45bfb400b | -4.29459 | -42.9906 | 2026-10-06 15:35:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| ba4434ce-1bbf-326c-a4f4-0e223791954c | -6.8952 | -43.62428 | 2026-10-06 15:35:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| c9d89583-5994-3762-a101-8f731cd6dd5d | -5.46266 | -41.22966 | 2026-10-06 15:35:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| e78fc5d6-d346-36a4-945d-96f3f2cea666 | -3.7101 | -38.6985 | 2026-10-06 15:35:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 5e249d29-ba35-3e0c-8980-0b846ff1c84d | -7.63556 | -37.98215 | 2026-10-06 15:35:00 | NOAA-20 | PRINCESA ISABEL | PARAÍBA | Brasil | 2512309 | 25 | 33 | nan | nan | nan | Caatinga | 71.6 |
| a99b535b-9be9-31fe-8f4a-485a33690e4e | -4.51515 | -42.05584 | 2026-10-06 15:35:00 | NOAA-20 | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 188f8561-1b13-3793-bce8-c54c32df07cd | -8.83969 | -41.09974 | 2026-10-06 15:35:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 45.3 |
| 1e26380a-cb57-348e-a6a2-7062eb8fcfd2 | -4.29381 | -42.98514 | 2026-10-06 15:35:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 3c9a6130-85c0-3a28-8a3a-bc89a76d7e34 | -4.54677 | -43.71791 | 2026-10-06 15:35:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| d068ec1f-83ed-38a2-bc8a-6716320ec2bb | -4.10459 | -42.49721 | 2026-10-06 15:35:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 18ccf2fa-60fd-36ed-8a2d-e6fb5adc82de | -6.01599 | -42.27266 | 2026-10-06 15:35:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 24.7 |
| 971951d0-3250-3d39-86c2-02ae64d2f772 | -4.92547 | -37.38675 | 2026-10-06 15:35:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 7.3 |
| f3cae2b0-6a39-376c-b828-65fb760f159e | -3.35064 | -39.85759 | 2026-10-06 15:35:00 | NOAA-20 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 43bdf3a8-fe31-3e7e-bfd2-ac3c241561ab | -3.8305 | -41.8105 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2e1fdde2-09b5-3e3c-9600-92c4f702b5b1 | -5.73129 | -41.62929 | 2026-10-06 15:35:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 4dc9bf39-7509-3ad5-9b42-6e523c68a54f | -4.9317 | -38.99298 | 2026-10-06 15:35:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| d842c30f-8714-3e69-9365-a73f711e4f95 | -5.97753 | -41.3265 | 2026-10-06 15:35:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| bb15b44d-3339-3a5f-80c0-3e54c6665d87 | -6.21425 | -41.59251 | 2026-10-06 15:35:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 97e3e9b7-6bf4-3183-bc61-c86beb84ff69 | -4.17734 | -38.43714 | 2026-10-06 15:35:00 | NOAA-20 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 33a184de-b0cc-3d64-8fc9-67a40789dd06 | -6.90318 | -43.6302 | 2026-10-06 15:35:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| f054deb2-c8d6-38a0-bb8c-bc9b85f6e54a | -3.67563 | -42.92694 | 2026-10-06 15:35:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 10b82907-3cf2-366b-99dd-b7e8bc65d697 | -7.00738 | -36.52777 | 2026-10-06 15:35:00 | NOAA-20 | JUAZEIRINHO | PARAÍBA | Brasil | 2507705 | 25 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 189330d6-4651-3611-aea3-9c47adcca655 | -3.78639 | -41.76723 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 292ec680-935d-3194-bca1-e99d0247bf52 | -3.53443 | -40.35115 | 2026-10-06 15:35:00 | NOAA-20 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 87be5704-b42c-3897-87e7-838c574fe022 | -4.53334 | -43.72523 | 2026-10-06 15:35:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 02ac96ff-36a5-30f2-bc5a-ea141edb6c07 | -6.603 | -37.89399 | 2026-10-06 15:35:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 7.3 |
| a108ee1a-a115-3b06-9aeb-9024c53a70b8 | -5.56914 | -41.03532 | 2026-10-06 15:35:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0e024913-ab2a-3f41-9643-ed4e54bef61d | -7.63998 | -40.16321 | 2026-10-06 15:35:00 | NOAA-20 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 79d701dc-3a41-303f-a2cd-f7005d3c0f25 | -7.60878 | -42.36347 | 2026-10-06 15:35:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| b0eab114-8f36-3d72-a85c-4419478b2e7a | -6.42484 | -43.46617 | 2026-10-06 15:35:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6cf9a3e8-ac09-3fd3-8214-229fe402c112 | -7.17102 | -41.99901 | 2026-10-06 15:35:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| d50f2864-9ea6-3117-8b12-29ad9d2a7668 | -6.02162 | -42.2685 | 2026-10-06 15:35:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| f326484e-55d8-392a-8c45-6770d70215b3 | -3.67608 | -42.93177 | 2026-10-06 15:35:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 950f45b1-8694-31b5-8244-fc78baf9627c | -5.47127 | -41.23263 | 2026-10-06 15:35:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 52.0 |
| a17be8c3-175b-30f9-8589-0a7d4161089e | -3.80543 | -41.80914 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 71.4 |
| 9504f066-72c1-3c66-9851-406bb344f27f | -7.64097 | -37.98443 | 2026-10-06 15:35:00 | NOAA-20 | PRINCESA ISABEL | PARAÍBA | Brasil | 2512309 | 25 | 33 | nan | nan | nan | Caatinga | 13.6 |
| f0ee41f8-8a40-3227-89dc-b1e2b824126e | -6.63963 | -43.77802 | 2026-10-06 15:35:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0566946c-a3eb-3b36-a2a2-c593faebd9c1 | -7.81995 | -40.3157 | 2026-10-06 15:35:00 | NOAA-20 | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 448be8af-8cb2-37d3-9f0b-e998c373535d | -4.30117 | -42.98956 | 2026-10-06 15:35:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 9c0d510a-2a90-32ce-a8d4-e1f36b9901dd | -3.81347 | -41.82225 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 50.8 |
| ec10b32e-a408-33f0-90c4-d1e053a5a279 | -6.47809 | -43.61523 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| cf7d663e-bde1-3ba1-9101-9b97c1e443dc | -3.87865 | -42.27077 | 2026-10-06 15:35:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 2d77e688-0a7e-3972-a8c6-7bbfeab3f7b3 | -4.50674 | -43.68438 | 2026-10-06 15:35:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |


[Clique aqui para ver as próximas entradas](README89.md)
