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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6d3221b-f190-3762-ad1a-95b1cf1f1085 | -2.89089 | -42.84245 | 2025-10-27 03:40:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d999519-438f-3c05-a0ec-6fb0c55d24ff | -5.10135 | -43.19664 | 2025-10-27 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68f7eab1-c142-38ed-a62c-2bbaa9053d91 | -5.49663 | -40.79432 | 2025-10-27 03:40:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3c913c54-9184-372a-826c-9a6ebbc91d03 | -4.77988 | -42.79023 | 2025-10-27 03:40:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 505ad3cb-27a7-3bcf-9971-be79de032d05 | -6.13174 | -41.71888 | 2025-10-27 03:40:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 431328a6-0647-364a-84a8-700462a8ca83 | -5.52912 | -41.7234 | 2025-10-27 03:40:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9cc0964e-c5bb-3526-8ba4-a641dcaf21e4 | -4.45688 | -43.43458 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78fe9167-d603-34ce-ba20-267d80ee18a7 | -4.4543 | -43.42133 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f6db1082-6a10-38b5-8a46-db0428bbdcae | -4.80467 | -43.2998 | 2025-10-27 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 23724849-eeb0-358e-b6b5-a890691fbdba | -6.10345 | -41.77663 | 2025-10-27 03:40:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a9d058f6-3db9-3cfe-8803-f8aeb5c80f20 | -5.58957 | -41.31558 | 2025-10-27 03:40:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2d9a52f3-dd4f-3d11-b1b9-4c11897da1e0 | -5.53575 | -41.3978 | 2025-10-27 03:40:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f9a29778-3b5f-3fd6-bdc6-01ccbc17d0bd | -4.48501 | -43.42969 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d62937be-ca4e-3476-ae3d-6b54cddc6957 | -6.003 | -41.38048 | 2025-10-27 03:40:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e2118589-523c-3803-9d49-4b728270e0ae | -6.13248 | -41.71443 | 2025-10-27 03:40:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ac8aa0b5-6311-3247-977a-ad9168bcbf48 | -4.44179 | -43.42864 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb6f1a6e-610a-3665-8dfc-b7d291d524e9 | -4.26373 | -40.683 | 2025-10-27 03:40:00 | NOAA-20 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c2829a92-4769-39eb-b15a-003477cff455 | -5.42966 | -40.87744 | 2025-10-27 03:40:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| b597ead2-a526-360c-92fc-7756627daf07 | -4.25377 | -40.6896 | 2025-10-27 03:40:00 | NOAA-20 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c93cc179-952f-3d20-8e0e-5ed40fa2cbbf | -4.44382 | -45.45861 | 2025-10-27 03:40:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5185c336-dda2-33cb-bdb6-a2bd7e80cb59 | -4.26307 | -40.68708 | 2025-10-27 03:40:00 | NOAA-20 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2058568f-4b38-37db-8bbb-b8c342748201 | -4.43306 | -45.98698 | 2025-10-27 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5410bfe9-2a41-383a-bc3c-227853ebad63 | -4.45209 | -43.43408 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88a31700-a0dc-3ee7-998b-4f34c1929b00 | -3.70079 | -44.33624 | 2025-10-27 03:40:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ff6ee11-419a-3bb4-b4bf-7286ea451f23 | -5.13936 | -41.20385 | 2025-10-27 03:40:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ba89a8db-7740-3f02-ba10-4645f5ccea91 | -5.60472 | -42.77643 | 2025-10-27 03:40:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 55d57597-3983-34b7-9941-0af90be76dae | -4.45793 | -43.42823 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ede432a3-0246-364a-a7dd-57911dba7b90 | -6.61051 | -38.63724 | 2025-10-27 03:40:00 | NOAA-20 | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c375c523-3652-3db8-91d0-b72ca330c0be | -4.44125 | -43.43184 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c14eda35-d1d8-3587-833b-389f5c6af7b0 | -4.81169 | -38.65143 | 2025-10-27 03:40:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 5003b47b-3ede-3643-a9f6-fd26942afc9b | -2.87712 | -44.38014 | 2025-10-27 03:40:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e70d3a7-0866-3ce2-b9dc-961d0689c435 | -4.86469 | -48.52942 | 2025-10-27 03:40:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e2c8292c-381d-3173-84b4-6fe7379c5edb | -4.48088 | -43.42252 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 864dc0a8-1491-3d28-8976-1edd67b1c384 | -4.7296 | -41.55125 | 2025-10-27 03:40:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 23314a2d-7531-3648-8583-7a2201a5353f | -4.43658 | -43.42776 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ae3ef78-7aa6-3ecd-8ce9-d33b58e328d7 | -6.20797 | -41.52882 | 2025-10-27 03:40:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 714c06ff-1b86-3e6d-b79d-50271aabf9a8 | -4.4486 | -43.41993 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e4acb28-63ed-33ea-a53a-9076c3f8f478 | -3.34067 | -42.88819 | 2025-10-27 03:40:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10e97b58-86c4-3835-90bf-c4f8e1469643 | -4.38515 | -43.32142 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f722530a-fd67-3f59-be37-c13ebee358f8 | -3.70615 | -47.65303 | 2025-10-27 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0798d987-e217-318a-bb3f-460149ae693a | -6.16691 | -41.58075 | 2025-10-27 03:40:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fdffb411-86e6-3093-8475-6d4a8c657baf | -5.07109 | -44.73306 | 2025-10-27 03:40:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 22c8f533-e2c1-32b3-98ae-89c690599727 | -4.44393 | -43.41581 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f53bfbfc-703a-3754-b854-2d9e853af1db | -4.3898 | -43.32538 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e2854d6b-bfe3-3278-855d-446bc105ce3e | -4.47925 | -43.43201 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 60bc717c-97ad-383f-8826-2f28e7076420 | -6.19103 | -41.52099 | 2025-10-27 03:40:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 86137432-4669-372a-9243-d5fcf51cbab2 | -4.4543 | -45.46878 | 2025-10-27 03:40:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0eed96d5-2475-3349-83fe-cc1f36688916 | -3.70732 | -47.64625 | 2025-10-27 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1db9a3e7-0307-333d-a14b-aa1627f7a8a1 | -4.45037 | -43.66304 | 2025-10-27 03:40:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 69f03fc7-29b8-36a1-9d46-f3f941962ae8 | -4.799 | -43.302 | 2025-10-27 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e668fed-042e-3da2-9899-aec3291d0df6 | -5.12315 | -41.19194 | 2025-10-27 03:40:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f2f82242-0599-3521-ac98-d3db89060c11 | -4.47621 | -43.41855 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 679f34ed-af79-3ebc-9de2-60fc7360439f | -4.39087 | -43.31912 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da084eb1-abdb-372f-889e-00dc045eb50d | -4.25803 | -40.69932 | 2025-10-27 03:40:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fc0798af-17ae-33df-95ca-8dcaef12605a | -4.7843 | -42.79008 | 2025-10-27 03:40:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 5ef1031e-66c8-3ae2-989f-9b0c3fcf46be | -4.44223 | -43.42907 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1998244f-d863-3e05-8ef8-4df559d88932 | -4.44286 | -43.42223 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c6d8bcd-359c-35b4-aed0-9866355347ec | -4.0952 | -44.6126 | 2025-10-27 03:40:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 599b8545-b3e3-32fc-bcf1-d8f079c801ec | -5.54195 | -41.40662 | 2025-10-27 03:40:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c8c66cbb-2cff-3cb6-99cb-702fb0ece070 | -4.78522 | -42.78448 | 2025-10-27 03:40:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| db22bbc0-e55d-3745-a7eb-afcdb50fdf9c | -4.47567 | -43.4217 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 5a23180e-aa94-384b-8a58-3d0288d0d0ae | -5.01787 | -41.03865 | 2025-10-27 03:40:00 | NOAA-20 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 680f7e8d-f61b-3cec-88d9-0085f2e69583 | -4.45898 | -43.42186 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57c43641-2473-3cf6-9f1d-9d1a311d19cf | -2.87499 | -44.37983 | 2025-10-27 03:40:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d23ccea8-ee89-37d8-9660-90d5e4785fc5 | -4.44967 | -43.41719 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8394b677-c119-3a5f-bdc7-b534106b2b7f | -5.822 | -40.81894 | 2025-10-27 03:40:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 49e0310b-f518-3f35-9a5d-56d2c0de2746 | -6.09905 | -41.77513 | 2025-10-27 03:40:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b27e2d07-40ad-3541-88ce-6355e867e494 | -4.45379 | -43.42089 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 386fc32c-7e4f-371f-a51d-75b81017e306 | -4.39034 | -43.32226 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0854ad86-2145-39eb-a3ff-242f4ec2d02a | -3.7141 | -47.64802 | 2025-10-27 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6dab2b7c-a459-3338-b766-81f1da0f7a67 | -4.44306 | -45.46295 | 2025-10-27 03:40:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2e3effe0-0def-344d-8575-a4e7c1393a10 | -5.47605 | -37.84567 | 2025-10-27 03:40:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8dd4de8d-a50d-3d38-87cc-548f890f6d09 | -4.36443 | -46.81258 | 2025-10-27 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8b09b87e-59cd-3e22-b51e-1baf21bce66c | -4.4647 | -43.42319 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 14643db5-abd2-3f88-b101-3035fa9e0633 | -4.8289 | -45.34144 | 2025-10-27 03:40:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 38eb5891-e323-34e8-b404-bb9b1d2512d5 | -4.95867 | -44.87665 | 2025-10-27 03:40:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17cab66c-a2c6-3d76-aad5-b060f6a12ce8 | -4.89037 | -43.23003 | 2025-10-27 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f7e2f8e1-10b5-3b2f-aa44-1a648453cd20 | -3.69953 | -44.34363 | 2025-10-27 03:40:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e614ca1-dccb-3e9e-90f1-d35b9cd0d73f | -4.44903 | -45.46387 | 2025-10-27 03:40:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f3e76f49-c00d-3376-8474-04656d1191c7 | -3.61977 | -42.77866 | 2025-10-27 03:40:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 861f61f7-aee7-36de-b56b-c9ae2d77f92e | -4.47349 | -43.43433 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ac7cb0c-08cc-3e5d-b5ae-ef34cae3dbcd | -3.72107 | -47.64943 | 2025-10-27 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ef379553-8246-3339-ba1f-8f3414f779ed | -6.12804 | -41.71329 | 2025-10-27 03:40:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| bd4f5f8f-12fb-3b4d-856c-4669b056cf50 | -5.69768 | -40.80986 | 2025-10-27 03:40:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| abda72d3-e67b-3a27-8338-dd9bbbff296e | -4.73129 | -41.485 | 2025-10-27 03:40:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9b926e23-9533-36c5-ab1a-6a3df010e720 | -4.80359 | -43.306 | 2025-10-27 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ea0a64c-a90a-390e-bf8c-62399efa8882 | -4.43912 | -45.9886 | 2025-10-27 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ac6ce41b-9a16-3fa2-8d3e-fc401d1ad4a5 | -4.447 | -43.42953 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8551df9-fdd6-36ca-9b76-190a64d9adc6 | -4.48034 | -43.42568 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| e8845b6b-0878-37ac-b53d-21cae6e9700d | -5.43028 | -40.87379 | 2025-10-27 03:40:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1aadecc9-0981-3a95-ab82-4d74232a3361 | -4.90416 | -42.99505 | 2025-10-27 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42f77e90-5557-3356-a4eb-4bfa441c415b | -5.11873 | -41.19126 | 2025-10-27 03:40:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| aae2cf20-d50b-3881-ad2e-74765a496c11 | -3.72093 | -47.64944 | 2025-10-27 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 53156174-7c35-3ef0-bfb8-f6bc03eff5a3 | -4.26493 | -40.68486 | 2025-10-27 03:40:00 | NOAA-20 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fe5efc70-9b35-3a09-bb2e-ae94c3dcf7fb | -5.64783 | -42.8024 | 2025-10-27 03:40:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9f4a16fe-da11-3517-8159-9b8937f9096f | -4.45501 | -45.46474 | 2025-10-27 03:40:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ae1fc999-9ade-3aaa-935b-6175957e1676 | -4.78335 | -42.79582 | 2025-10-27 03:40:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 446bbc47-d748-3d3c-b452-5f69e982a5fb | -5.88579 | -41.32565 | 2025-10-27 03:40:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1c73d014-eac1-3f2f-9e46-3b17f14237a9 | -4.95587 | -44.88021 | 2025-10-27 03:40:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62a8aaca-bc70-3cbc-94fc-c3c9ac39b5db | -4.95017 | -44.8793 | 2025-10-27 03:40:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README17.md)
