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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 395c101c-c465-3587-b170-9ee93b50ade9 | 0.65458 | -51.54555 | 2025-11-09 00:37:00 | TERRA_M-M | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b6bf6d82-f847-39ef-8453-d06456c3596d | 3.53285 | -51.7789 | 2025-11-09 00:37:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0ab34494-7582-3798-9277-72e28406f86e | 0.66462 | -51.53801 | 2025-11-09 00:37:00 | TERRA_M-M | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 89f195d4-bb52-3594-9c2f-9bb34e1dad8b | 1.92816 | -55.8912 | 2025-11-09 00:37:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c706d07e-fefa-39df-9106-44c4f0421045 | 1.91759 | -55.88967 | 2025-11-09 00:37:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 441b4b18-76bd-30a0-953c-e487eca23cb4 | 0.66341 | -51.54678 | 2025-11-09 00:37:00 | TERRA_M-M | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 87bec372-8c2d-3f32-b630-726c818a4f32 | -5.2908 | -44.9572 | 2025-11-09 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 0109eaf7-369d-3bb8-b693-a3dd8eaee17d | -2.9435 | -49.3443 | 2025-11-09 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| fee0c59e-8451-32d6-9b72-9cf996764163 | -3.5946 | -41.6577 | 2025-11-09 00:40:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 65.1 |
| 628b7285-c50e-3f0b-bab9-24181a82bd09 | -2.738 | -45.1525 | 2025-11-09 00:40:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 52.6 |
| e2a88846-53be-381b-97de-f3449f48f01d | -3.3182 | -44.3814 | 2025-11-09 00:40:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 5ab63246-9226-316e-ba70-78d0a154d281 | -2.5929 | -49.2268 | 2025-11-09 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| a34adccd-ca79-33b6-9263-d84009ebd3f6 | -3.8408 | -51.1215 | 2025-11-09 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 6dc95ef3-dedc-3bf6-861a-51ae438c276b | -2.6113 | -49.2263 | 2025-11-09 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 337aafbe-2de5-36b5-8558-ccf324b4d206 | -2.7379 | -45.1751 | 2025-11-09 00:40:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 57.5 |
| dba00463-e33c-3332-b423-9609dfb77def | -3.3369 | -44.3806 | 2025-11-09 00:40:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 190.6 |
| ad72daf3-a375-301a-b093-3522f34f9b2f | -3.3183 | -44.3585 | 2025-11-09 00:40:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 5d449d27-8ea2-3b6c-bc48-35f660447b64 | -5.291 | -44.9345 | 2025-11-09 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 2cb492b9-eedf-3fdd-8ee7-267acfadf4d2 | -3.4582 | -49.9836 | 2025-11-09 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 650599c7-9e08-3a24-a7f8-e11c1c377d6a | -7.4096 | -40.0563 | 2025-11-09 00:40:00 | GOES-19 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 77.1 |
| 9019b89e-db88-303a-a515-ee160c53bdbf | -3.3555 | -44.3798 | 2025-11-09 00:40:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 50.3 |
| b1318f5f-e96a-3e6f-ad75-27a5841faac0 | -4.6464 | -46.3873 | 2025-11-09 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 52.3 |
| b192443d-cd51-33de-a1e2-588c42b33a30 | -3.4583 | -49.9625 | 2025-11-09 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| db625397-3c89-3c9c-b132-19becb8f4d68 | -4.4534 | -44.6447 | 2025-11-09 00:40:00 | GOES-19 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 67fa4586-c947-3454-838b-98e740eece96 | -2.9434 | -49.3655 | 2025-11-09 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 35ea9300-b24f-3510-b0f3-c6c16f73dbd4 | -3.337 | -44.3577 | 2025-11-09 00:40:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 0da85120-2eb2-35ec-ad3a-2adc325930ac | -2.5929 | -49.2268 | 2025-11-09 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 0f4d0f6c-da4e-3c8a-9e9c-61a1685a1987 | -4.4534 | -44.6447 | 2025-11-09 00:50:00 | GOES-19 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| c966372b-a6b6-3c4c-9ed8-c6d32a059ed4 | -3.8408 | -51.1215 | 2025-11-09 00:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 2ca8414f-6479-3025-9868-f2fd2d8a584b | -3.3369 | -44.3806 | 2025-11-09 00:50:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 181.6 |
| c573ce70-c9dd-37e3-a2c6-d5dfb0abb8a5 | -2.9434 | -49.3655 | 2025-11-09 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| c1124239-77cd-3b31-850d-62f8ce43669e | -5.2908 | -44.9572 | 2025-11-09 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| f98625c3-4a26-3e1c-99bb-2bb79c945167 | -7.4096 | -40.0563 | 2025-11-09 00:50:00 | GOES-19 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 59.7 |
| 57abd1f2-47be-3065-8950-f39c0b6d26bd | -9.553 | -40.3503 | 2025-11-09 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 130.2 |
| a84cf478-42b3-3195-96da-71c65807a674 | -5.2722 | -44.9585 | 2025-11-09 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| efcf7263-0c2a-389c-9310-71d29f914669 | -2.6113 | -49.2263 | 2025-11-09 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 18e76634-887a-34a0-adc1-feec6264864e | -3.3182 | -44.3814 | 2025-11-09 00:50:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| d299b639-4dd9-3045-8851-915205c752db | -9.5725 | -40.3227 | 2025-11-09 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 131.4 |
| 33e48bbf-a96f-34c4-ba18-e529153ce715 | -9.5721 | -40.3475 | 2025-11-09 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 105.6 |
| 63d6701e-2f1d-31cf-a7b2-dd3ad26347af | -3.3183 | -44.3585 | 2025-11-09 00:50:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 43.3 |
| c3afe484-68fc-3a59-93a9-71660383ab8d | -3.337 | -44.3577 | 2025-11-09 00:50:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 105.0 |
| e7b34bc5-2aee-32dd-bdaa-8dfd94fc2c0d | -3.5946 | -41.6577 | 2025-11-09 00:50:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 60.7 |
| 24543266-538b-35ea-b609-9608f32132e3 | -9.5534 | -40.3254 | 2025-11-09 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 143.0 |
| a4220bf7-c7cb-3bc6-ab56-0091446a2a66 | -2.9435 | -49.3443 | 2025-11-09 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 2175d2cf-3bad-3c7e-a4b0-b595c1749779 | -2.9435 | -49.3443 | 2025-11-09 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| e4011d7e-fac1-385c-885d-e4a00846f829 | -9.5725 | -40.3227 | 2025-11-09 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 217.8 |
| 35e81b48-a4fa-3f55-b894-c132d1b3b230 | -9.5721 | -40.3475 | 2025-11-09 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 204.1 |
| 501fd5e4-b47f-340f-8f16-9bc702e17fea | -9.553 | -40.3503 | 2025-11-09 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 200.8 |
| 2ef089e7-1df7-3684-972e-a4d6a4450b27 | -3.8495 | -42.7819 | 2025-11-09 01:00:00 | GOES-19 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 95dd2e4e-61ea-3b17-b994-d1b2ecb4f42e | -2.5929 | -49.2268 | 2025-11-09 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 935e06c1-f38c-3883-9472-7a76b9c4e68f | -5.2722 | -44.9585 | 2025-11-09 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 00506142-72f1-366a-8b49-5cbf82a55a36 | -4.4534 | -44.6447 | 2025-11-09 01:00:00 | GOES-19 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| a5de6a43-3c73-3f8c-a4bb-7db8e3752f92 | -9.5534 | -40.3254 | 2025-11-09 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 227.4 |
| d9fcb543-a726-3329-aced-f3c19c67de1a | -3.3182 | -44.3814 | 2025-11-09 01:00:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 1813454f-0ebf-3354-a766-eaad20738fb4 | -5.2908 | -44.9572 | 2025-11-09 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 1e1e9f67-810d-3430-9c86-6394b1444abd | -2.6113 | -49.2263 | 2025-11-09 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 0af122ee-242e-3945-890e-1113ccaf69db | -3.337 | -44.3577 | 2025-11-09 01:00:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| ee34c13d-758c-3ff2-82e7-3b0a824dd8f7 | -2.9434 | -49.3655 | 2025-11-09 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 134ae2e6-c0b9-3716-85bc-41daa6040015 | -3.5946 | -41.6577 | 2025-11-09 01:00:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 54.6 |
| cf8a4912-d21b-3519-bb9a-f575a7e1405d | -3.3369 | -44.3806 | 2025-11-09 01:00:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 93d29934-750d-3e62-8624-cb7fc6b83c41 | -5.2908 | -44.9572 | 2025-11-09 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 309cad64-4d08-395d-9723-68d3471a562a | -9.553 | -40.3503 | 2025-11-09 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 76.7 |
| 71556e2f-38e5-3e9f-9211-084a5eeba46b | -3.3182 | -44.3814 | 2025-11-09 01:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 43.8 |
| cc4c48fe-31ec-35e8-9274-e0b3d89e42f2 | -3.337 | -44.3577 | 2025-11-09 01:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 0b9b591b-0f55-3f4c-84f2-a09687084fa2 | -2.6113 | -49.2263 | 2025-11-09 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 98fde5d1-334b-3c7a-894c-2beda307d878 | -2.5929 | -49.2268 | 2025-11-09 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 23962cf8-3cf8-30c4-8fcf-b2f0f8b0583c | -5.2722 | -44.9585 | 2025-11-09 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 47361ff7-7b32-344e-ab1a-8b8631738462 | -2.9435 | -49.3443 | 2025-11-09 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 357042a4-74b3-3b59-8062-9f88c877af2c | -9.5725 | -40.3227 | 2025-11-09 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 77.3 |
| a1191745-8f74-3a73-b8db-b20a838da1c8 | -3.5946 | -41.6577 | 2025-11-09 01:10:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 55.3 |
| 71e3e65b-d6f0-3852-ac7c-d87102ec1c3d | -4.4534 | -44.6447 | 2025-11-09 01:10:00 | GOES-19 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| a1dbb177-13c5-37a9-a61f-e6d9983a4f8b | -9.5534 | -40.3254 | 2025-11-09 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 117.7 |
| a15210e5-bf0a-372b-9665-7542008f028e | -2.9434 | -49.3655 | 2025-11-09 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 30304a2a-375d-392e-88bd-cc9770204a6e | -3.3369 | -44.3806 | 2025-11-09 01:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 5583a0bd-1d59-3b2b-ac41-e3c89a410fcc | -4.472 | -44.6436 | 2025-11-09 01:10:00 | GOES-19 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 51.1 |
| a3ffd8ca-0859-3962-9c44-26c26db94b5d | -9.5534 | -40.3254 | 2025-11-09 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 68.5 |
| 2c0db16f-db20-3e6a-9fec-1c2da0c6883c | -3.3369 | -44.3806 | 2025-11-09 01:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 71481e24-c6ca-3ce3-9210-fa20306afa20 | -2.6113 | -49.2263 | 2025-11-09 01:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| ef8dbb47-ac4c-38b5-9bca-8c79ba9686c2 | -2.5929 | -49.2268 | 2025-11-09 01:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| c86209c8-bb10-31ef-818b-6d8d48fc713e | -5.2722 | -44.9585 | 2025-11-09 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 50301f50-fb2a-32a1-b4b7-7c939083bcd0 | -3.5946 | -41.6577 | 2025-11-09 01:20:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 52.7 |
| 77f429e8-54c7-3cb1-889a-335a2ee906dc | -4.472 | -44.6436 | 2025-11-09 01:20:00 | GOES-19 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 550cd43e-489a-3562-8285-dd0857024617 | -5.2908 | -44.9572 | 2025-11-09 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| a3c4e43e-fe20-3728-8c07-dbd87b9e32e1 | -3.3182 | -44.3814 | 2025-11-09 01:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 1a787a0e-4f99-358a-b3a0-ab0f922ada32 | -3.337 | -44.3577 | 2025-11-09 01:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| d277962c-6db9-3efd-9911-748a2285700c | -4.4534 | -44.6447 | 2025-11-09 01:20:00 | GOES-19 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 486f2928-8f18-3712-a11a-14dc87fa148d | -2.9434 | -49.3655 | 2025-11-09 01:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| faf83a18-e55e-35d0-9667-075a073d847b | -3.5946 | -41.6577 | 2025-11-09 01:30:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 49.1 |
| 439ebe89-e393-313c-90e5-06b7d0dce832 | -2.9434 | -49.3655 | 2025-11-09 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| a44de62e-5a99-396e-90b7-78644a690c12 | -2.9435 | -49.3443 | 2025-11-09 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 24d868fd-8bed-3baa-923a-212e46bfa426 | -2.5929 | -49.2268 | 2025-11-09 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| f8a292b1-6185-3e6e-84ec-1783e497a455 | -3.337 | -44.3577 | 2025-11-09 01:30:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 45.7 |
| ad16300a-a9a4-30a2-a73f-d166a8b33fd3 | -4.4534 | -44.6447 | 2025-11-09 01:30:00 | GOES-19 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 6bc6553f-ffaa-37d3-9da0-da1e2cf477bb | -10.3437 | -49.6321 | 2025-11-09 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 5dc261d9-6c1e-399d-bd73-62c0f446c8de | -3.3182 | -44.3814 | 2025-11-09 01:30:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 39.5 |
| f67667f8-e41b-35c5-8fee-5077966fcbea | -5.2722 | -44.9585 | 2025-11-09 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| d05582d9-8e44-358c-9da3-f13aa5469e16 | -10.3434 | -49.6536 | 2025-11-09 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 51.9 |
| ebe65fd2-52f3-3aaa-b2c6-3de917f3ab50 | -3.3369 | -44.3806 | 2025-11-09 01:30:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 6e4b4b07-a151-3aa1-884f-98d181b46465 | -2.6113 | -49.2263 | 2025-11-09 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 63964582-5d8f-3cd4-aebc-b00191c1dc62 | -2.9434 | -49.3655 | 2025-11-09 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |


[Clique aqui para ver as próximas entradas](README7.md)
