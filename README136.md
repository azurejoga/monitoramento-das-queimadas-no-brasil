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

## Dados Diários - Página 136

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 203cb0ea-16cb-3ec8-8b72-e8453a6bcce3 | -9.9067 | -48.4211 | 2026-09-23 13:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 2994731f-1387-3429-85d4-ce6e9bbcd6a0 | -8.7735 | -45.6303 | 2026-09-23 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 2e21fbf0-86ef-3fbd-9fe8-e7e067b6eb3c | -9.9064 | -48.443 | 2026-09-23 13:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| e86b19bc-bf08-3d8c-9aaf-6e0b93db5aff | -6.6129 | -43.7317 | 2026-09-23 13:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 436.3 |
| 9b242170-86c6-3c28-bda4-26b9014b511f | -7.9822 | -44.0879 | 2026-09-23 13:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 82.7 |
| a5d855f8-4fdc-3749-8695-0b768977c1c1 | -6.2208 | -41.6651 | 2026-09-23 13:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 87.3 |
| a14dca94-b4b8-390a-953f-f0d924d70aba | -11.4168 | -44.2139 | 2026-09-23 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 621.1 |
| d08d6733-77eb-334f-b03d-b0f06312825a | -11.4009 | -44.029 | 2026-09-23 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 236.9 |
| bb69b356-7d55-3d4b-846f-845a403eb44b | -7.41 | -44.7198 | 2026-09-23 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 3df4aaa5-7d6e-3a4c-8682-8e7509d6dfba | -9.5854 | -48.4549 | 2026-09-23 13:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 213.1 |
| c769e937-b1c3-3564-9225-3eceb216cca2 | -9.9253 | -48.441 | 2026-09-23 13:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 731f2058-bf40-3bec-8841-b75ab5384f85 | -6.9029 | -46.5456 | 2026-09-23 13:30:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 71ec8e62-8627-309e-8626-6074157031a6 | -7.0887 | -52.7369 | 2026-09-23 13:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 8c887b3f-1e24-30a0-b88c-794e102cb8c8 | -7.1395 | -42.0572 | 2026-09-23 13:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 103.6 |
| 4b3b4fba-d3b5-3c38-b512-c59e900381a1 | -9.2796 | -45.9143 | 2026-09-23 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| daf767a0-e609-348a-8456-2c0001e870a2 | -6.9416 | -42.8834 | 2026-09-23 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.2 |
| 48235c32-b62c-37dc-8cd3-08930b4e4fc9 | -8.8105 | -44.2757 | 2026-09-23 13:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 6975aa01-5eb2-34dd-b2b7-e393f4908a4b | -6.6515 | -59.9258 | 2026-09-23 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| f1f5f7f3-ea07-3bf9-9f42-a469d5739011 | -6.2396 | -41.6634 | 2026-09-23 13:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 88.6 |
| 5ad20517-b6cc-35a6-a9eb-03b9de783602 | -9.5665 | -48.4568 | 2026-09-23 13:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 91d29757-532a-3473-88ba-f5a44e01d760 | -9.6043 | -48.4529 | 2026-09-23 13:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 10eb3663-8d05-3174-bace-97469046dbc5 | -6.6148 | -59.908 | 2026-09-23 13:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 100.0 |
| ce1826c8-299a-3434-ac5d-329158a2e931 | -6.5941 | -43.7333 | 2026-09-23 13:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 103bf65b-7964-3f32-ae69-858b4b6af3b5 | -9.9163 | -45.0885 | 2026-09-23 13:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 179.0 |
| 607c3cd5-0542-33cf-8b9c-f9cabb18b913 | -11.4782 | -47.3529 | 2026-09-23 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 118.7 |
| d7ebcac5-843f-33ec-aad5-46f722013157 | -8.3591 | -45.6056 | 2026-09-23 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 028ac85a-1307-3b29-9a1f-4d7d6c66ec42 | -6.6331 | -59.9265 | 2026-09-23 13:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 173.2 |
| 2b84e986-7f2a-3c9d-8dda-a0db09dd71e6 | -11.3054 | -44.0198 | 2026-09-23 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 06255348-1409-3f09-89e1-b1af2a2f0c6e | -9.6108 | -43.9477 | 2026-09-23 13:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 107.7 |
| c2e9261a-4026-3c83-ac65-73379f79aa7c | -6.8841 | -46.5471 | 2026-09-23 13:30:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 3c9faf54-adba-37fc-a855-1e0f3b987da3 | -6.166 | -52.05 | 2026-09-23 13:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 4318fd4d-405b-3fdc-87ec-fdab1cc6d476 | -8.9019 | -45.9104 | 2026-09-23 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 08fa1592-efb4-3e79-9bd6-221ebd20997e | -10.5561 | -46.7095 | 2026-09-23 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| b4a9ca0d-df87-3a32-821f-49a9627dfa47 | -11.1541 | -42.8364 | 2026-09-23 13:30:00 | GOES-19 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 72.7 |
| d2d598da-3f7a-39f7-a6a1-3bde6dd215fe | -8.0921 | -44.3538 | 2026-09-23 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 148.0 |
| e6813b40-42f3-383c-b368-67810e4e1d19 | -7.4288 | -44.718 | 2026-09-23 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 585e152f-08b0-356c-840a-fa48dfb92910 | -8.9013 | -45.9556 | 2026-09-23 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 092fad8d-af3c-3d08-8b53-2f531ed16bc6 | -6.6317 | -43.73 | 2026-09-23 13:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| b6fb511d-8e26-3212-9ba0-9a1081f348cd | -7.9904 | -44.9608 | 2026-09-23 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 694d82e8-96b8-35da-92ea-63dc0cd103d5 | -9.5921 | -43.9267 | 2026-09-23 13:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 77.5 |
| 3d2cabc5-ac2a-37c6-ac88-2d63210c6c6a | -11.6919 | -50.7699 | 2026-09-23 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 3af9f873-be6e-3295-8de6-450b1273b1ed | -11.3596 | -44.1989 | 2026-09-23 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 6b2c3d29-f34c-304e-a792-7727540abb8f | -11.3551 | -43.3764 | 2026-09-23 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 76046c0a-cb3e-3d35-937a-a49aa2f92602 | -6.8839 | -46.5694 | 2026-09-23 13:30:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 103.0 |
| b56f3ba3-c3f3-3812-9567-926a1570a165 | -9.831 | -48.4292 | 2026-09-23 13:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| b81edf14-3d2a-3790-bf9f-a3e30f317b72 | -11.6601 | -43.4714 | 2026-09-23 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 3f685f1e-5304-3f5a-b1fb-e05aebd3ca5c | -9.5329 | -45.3861 | 2026-09-23 13:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 92.3 |
| b5aded66-f4fd-3061-b777-1799c60bd0c8 | -11.3058 | -43.9963 | 2026-09-23 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 185.7 |
| a8439aa1-dcb0-3c7f-b437-e73cfdd9005d | -7.4153 | -42.6479 | 2026-09-23 13:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 103.4 |
| 692b226c-750b-3a93-873c-03b3b548e667 | -8.8264 | -45.9185 | 2026-09-23 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 163.7 |
| bb967c29-820c-3784-92ba-18cc55ecf6d4 | -7.0885 | -52.7575 | 2026-09-23 13:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 89f63d78-ba0c-341d-ae40-12fd477eefae | -12.3573 | -42.2307 | 2026-09-23 13:30:00 | GOES-19 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 118.6 |
| 02a0c662-e185-359e-b9a4-373356d25773 | -9.5668 | -48.435 | 2026-09-23 13:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 907d617f-152f-3789-9868-1977e327018e | -9.5857 | -48.433 | 2026-09-23 13:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 81622e1f-e850-3189-b9c3-f1744152a6aa | -7.1392 | -42.0811 | 2026-09-23 13:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 112.1 |
| 9a03a9f1-a880-3637-91b3-795d7861af43 | -7.1274 | -43.1009 | 2026-09-23 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.7 |
| 786c23c9-bb92-31ff-ba87-4dd926c94251 | -7.1088 | -43.0792 | 2026-09-23 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.2 |
| 2d4b5dbd-08b6-3b73-a6c4-69a15d3d97d9 | -8.449 | -47.4938 | 2026-09-23 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 7b8f7732-2f20-370b-9408-90617cb0da63 | -8.4493 | -47.4718 | 2026-09-23 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 76a0231a-48b4-3b3d-a53a-c710b8152e73 | -9.916 | -45.1115 | 2026-09-23 13:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 3775c420-22a3-332e-98c5-b38ade1ef1c9 | -7.41 | -44.7198 | 2026-09-23 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.1 |
| a340565b-b761-3b60-8460-b15582525801 | -10.0259 | -45.3724 | 2026-09-23 13:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 2d192623-2c4e-33bd-ac61-3f163668d63f | -9.9163 | -45.0885 | 2026-09-23 13:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 138.5 |
| c08b3bf6-541c-30a8-8759-e4d68dbafa80 | -6.6127 | -43.7549 | 2026-09-23 13:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| f9d0dcbc-6407-324f-996d-2634ebecaa6e | -11.2858 | -44.0461 | 2026-09-23 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 124.0 |
| f0171cf7-48b8-3123-8255-55f6acfe63a6 | -11.0048 | -49.7325 | 2026-09-23 13:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 7f0c54dd-180a-3764-8e04-d638cafe738b | -11.3054 | -44.0198 | 2026-09-23 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 197.8 |
| 408197b5-fc2c-35b1-b601-127a72104d76 | -11.3596 | -44.1989 | 2026-09-23 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 8db0dd87-4be1-3ea3-99be-9f541b1a1cc5 | -8.4493 | -47.4718 | 2026-09-23 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 1bfb9699-f706-37c5-b9d3-3ac261f3045c | -10.5561 | -46.7095 | 2026-09-23 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| de0a8a7e-227f-3682-acbf-fff1bd828f88 | -9.916 | -45.1115 | 2026-09-23 13:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 6b552ccc-3b1d-3b5d-b702-79c902c62b32 | -9.6111 | -43.9243 | 2026-09-23 13:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 187.8 |
| 4ca37454-2227-3bb9-82da-b1a4d60962fb | -7.1274 | -43.1009 | 2026-09-23 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.7 |
| 46939064-6849-3913-8f0d-9a9e8fc5a0d4 | -8.0912 | -44.423 | 2026-09-23 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 47c4e2f8-c4b6-3661-8d0c-05868204b086 | -11.3058 | -43.9963 | 2026-09-23 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 341.1 |
| d46e786d-eec6-317d-8d33-f7745a0fae8c | -7.1395 | -42.0572 | 2026-09-23 13:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 89.3 |
| 68456a15-3fd1-3811-bb4d-9e52b91d5351 | -6.8988 | -41.6735 | 2026-09-23 13:40:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 90.2 |
| 8eb06802-e42c-3aa3-bb0a-e324abefbc5c | -7.4288 | -44.718 | 2026-09-23 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 104.7 |
| b71acb6f-d859-3630-9f91-3971158c160e | -9.5735 | -46.5337 | 2026-09-23 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 165.1 |
| b5f6af69-8ef6-3ae6-bb45-e306ad7382c2 | -10.0072 | -45.3518 | 2026-09-23 13:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 3292451d-3870-3e02-8293-a12cf44d5b56 | -7.1277 | -43.0774 | 2026-09-23 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.2 |
| dc94e656-ca25-3a96-813b-6f888b2f5eb7 | -9.8692 | -48.4033 | 2026-09-23 13:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 0bf45a79-d164-3fde-acdf-ebf77491c63f | -11.6793 | -43.4684 | 2026-09-23 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 91a62f1f-71ed-391f-8d53-1e95521764cd | -9.5332 | -45.3633 | 2026-09-23 13:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 56.9 |
| fec22972-dd99-312a-907f-a24a87519ff9 | -10.1148 | -45.7712 | 2026-09-23 13:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 24e057db-4c7e-3611-92dc-1b5692ac63e2 | -6.9135 | -43.7281 | 2026-09-23 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 1d5033d1-a494-30de-8365-2b3c4c4e2f32 | -6.6148 | -59.908 | 2026-09-23 13:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 06f882f8-cbf3-33c9-a0d6-7950c3e7da6e | -9.5329 | -45.3861 | 2026-09-23 13:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 3e4fab1f-b4e0-3acb-9b70-5b213487d6ff | -6.9414 | -42.907 | 2026-09-23 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.9 |
| 757c5029-5a2c-39c9-bbfb-18bc2d92b1a6 | -7.9904 | -44.9608 | 2026-09-23 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 349cde6f-32fb-3c36-b9f8-b5270cd776f0 | -8.8105 | -44.2757 | 2026-09-23 13:40:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 561e678b-9009-3efc-b959-8bc1ec84b857 | -7.4153 | -42.6479 | 2026-09-23 13:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 106.4 |
| fdf39777-5850-3c96-b82c-0be13f3947b3 | -6.6331 | -59.9265 | 2026-09-23 13:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 204.7 |
| 73d4a0ff-36f6-3bf3-80b0-0935177b4c5f | -11.6916 | -50.7913 | 2026-09-23 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 94.8 |
| fe5cb3e3-a41e-3e45-85fc-eb1bd55170ae | -11.4005 | -44.0525 | 2026-09-23 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 252.9 |
| 0abed40d-a2ec-3b15-9529-95c92cc60add | -10.8011 | -50.7604 | 2026-09-23 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 4ab5e45b-07ef-349b-b7de-5bb3e1e23ce0 | -9.8694 | -48.3814 | 2026-09-23 13:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 5a91ec58-ca18-3b3a-85df-7e205c894a28 | -8.7735 | -45.6303 | 2026-09-23 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 69f507db-ce03-3441-801f-9ac7314ecdfb | -6.4486 | -59.9717 | 2026-09-23 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| be600948-16f2-3572-8a09-855e8336fd23 | -7.0349 | -44.6625 | 2026-09-23 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 110.4 |


[Clique aqui para ver as próximas entradas](README137.md)
