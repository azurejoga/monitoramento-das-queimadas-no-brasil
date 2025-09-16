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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 455a96cc-392d-36e4-b3ef-e95e8e37ba47 | -6.12827 | -42.9421 | 2025-09-16 04:49:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a56def07-36ab-38ff-a2e7-ca2479a6f59d | -5.93854 | -45.19115 | 2025-09-16 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f4edfdcc-fcd1-366e-9452-993ba2a10464 | -7.6809 | -46.30528 | 2025-09-16 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8bbe6e54-9019-3cb6-bc05-ef40ec21c1b1 | -5.89031 | -45.7411 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6027e84d-9468-3686-9c98-1cc232eab9a4 | -7.93745 | -47.65428 | 2025-09-16 04:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7121ef63-79df-3c56-9930-dc01bd8540e8 | -6.16103 | -45.11671 | 2025-09-16 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1142f97c-9485-3224-b6b0-fff743d6f2a1 | -5.79155 | -43.93699 | 2025-09-16 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de209848-8836-3f40-9908-df0373cd9603 | -5.79265 | -43.94709 | 2025-09-16 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9a59c3ec-1a7d-3c90-b4cc-d14ccf967254 | -7.08669 | -44.55419 | 2025-09-16 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12313f2c-d7fc-3442-90b9-b7533383a974 | -4.11043 | -51.09059 | 2025-09-16 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fd4ed57-6398-312c-be9f-bf7f8d274d3a | -6.1866 | -41.20071 | 2025-09-16 04:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7446ad67-07e4-3175-b550-ab37acac5a3b | -4.15517 | -46.79115 | 2025-09-16 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2ed0dc0-b472-3566-a672-43a79ca433ec | -4.56922 | -47.24755 | 2025-09-16 04:49:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d08870d1-3bb7-368b-ad08-35129f28e4b5 | -3.90777 | -52.16539 | 2025-09-16 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8490112d-b348-374b-a905-11b01ec78ba4 | -7.38642 | -49.99459 | 2025-09-16 04:49:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2429e8d4-861f-3586-bf82-ab1800771cdb | -7.40954 | -49.98576 | 2025-09-16 04:49:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43c8833d-ec25-31dc-8e5e-77edc19eb4a4 | -7.59692 | -49.33273 | 2025-09-16 04:49:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a5bbc33-4db8-3f78-b316-56815abb5655 | -6.09491 | -46.49956 | 2025-09-16 04:49:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| beceaf63-bc83-3934-b14f-84b0f4779346 | -6.34989 | -44.31213 | 2025-09-16 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e249d71f-7ebd-33c7-af0b-8bb86be24444 | -5.78751 | -43.89301 | 2025-09-16 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 036e199a-ee5b-3550-a925-7aa00aa98f5a | -6.28471 | -42.38639 | 2025-09-16 04:49:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bdfa07c3-72dd-3118-9689-29498e8ffd4f | -5.67517 | -51.1397 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bf7a6b5-617d-3716-a696-2e1a885217d7 | -5.41788 | -43.18821 | 2025-09-16 04:49:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a25dfd73-c2f5-3319-a6a9-2c69678f5b71 | -6.17745 | -41.21599 | 2025-09-16 04:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 11b406a5-c7d8-3623-a1ce-1ddde72c221c | -6.16171 | -45.11188 | 2025-09-16 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3ce8936e-6839-3cc6-9e7f-d5be92c922e9 | -5.89813 | -49.10027 | 2025-09-16 04:49:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 090c2e0a-27d9-329f-8925-750ff26f573a | -3.87725 | -55.35497 | 2025-09-16 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bcd6b266-9c86-3ec2-8410-7de84594c549 | -7.71222 | -45.30007 | 2025-09-16 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83f6776a-0aa2-3e52-906e-c2b0d0be4d4e | -3.41882 | -43.15131 | 2025-09-16 04:49:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb851ff0-24c3-3c39-b359-5a06267eaa3a | -5.55717 | -44.96431 | 2025-09-16 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 7c3cde21-0d44-3fef-9b0b-06f84a5f9f4e | -7.51546 | -44.66662 | 2025-09-16 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45e5b840-0c4d-3010-9e1f-723200b21d94 | -7.66381 | -45.15288 | 2025-09-16 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| adfd6c87-6c75-3c6d-b124-1c93633712cc | -8.00873 | -45.6661 | 2025-09-16 04:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d5538e7d-b12d-3cc4-bd9d-97e5f3105fe9 | -5.78753 | -43.94637 | 2025-09-16 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c6b8540-1e7d-3158-a48b-8665dc2c85c9 | -3.94465 | -56.01663 | 2025-09-16 04:49:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8adb816e-f6a4-3db5-a4e2-56860cb53466 | -6.66732 | -45.54119 | 2025-09-16 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e482d0f8-044f-3e71-86f8-c08c5bbb6293 | -3.55921 | -53.20612 | 2025-09-16 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da476a2e-64eb-378a-835f-361fc214a18a | -7.51001 | -44.66695 | 2025-09-16 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8df60cb4-e32c-3971-9610-659ec0003c10 | -3.65368 | -54.06375 | 2025-09-16 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2968d27a-954d-3df1-ba1f-bfc6a46b730e | -3.07763 | -48.81469 | 2025-09-16 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3701759d-fb99-3123-8fdc-af5586502e02 | -7.9807 | -45.64586 | 2025-09-16 04:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a79b1c9-bf97-3c40-818a-92d1d53af232 | -5.67462 | -51.14324 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3579414-f844-32c3-a4f3-36f55f780a5d | -3.64799 | -54.05516 | 2025-09-16 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba2e48f6-2d20-3f56-9adf-3962e1fccce5 | -3.89078 | -47.60509 | 2025-09-16 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 524cdc8a-8419-3d7b-8676-d75836142857 | -8.33229 | -44.73874 | 2025-09-16 04:49:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 631044e4-d30d-38ec-9c31-3cd9b8eff66a | -7.52943 | -47.65929 | 2025-09-16 04:49:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 07d3801f-5e65-3d7d-8b7b-61dae15de69b | -2.29856 | -48.14675 | 2025-09-16 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c4a8405-7188-3443-a664-d5e92c004c91 | -6.15493 | -45.11829 | 2025-09-16 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4d4326a1-3a85-39c2-8303-3504985e137f | -6.67878 | -46.31237 | 2025-09-16 04:49:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3e126cc9-4535-3579-b5ea-f358c8f62b11 | -2.94453 | -49.34794 | 2025-09-16 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f76b618-4c9b-33c8-89a7-1273f614dd51 | -11.72267 | -46.47965 | 2025-09-16 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c9706514-60aa-3b4a-9ebb-de19ccddf5f2 | -12.49679 | -49.1366 | 2025-09-16 04:51:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1189b6f-7e13-3e1f-be8b-293672cfa707 | -9.05707 | -44.84882 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3061e634-64ca-341b-b828-e20bbf592183 | -11.44639 | -46.94096 | 2025-09-16 04:51:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| adca5c9e-0fa8-3b64-a2f9-d60822ca0f21 | -12.84863 | -47.13926 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| fc66844b-4caf-3ef1-83be-2972b0833f6c | -12.78656 | -47.25918 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f7f24875-ffc2-3eef-b177-0d9750446dcc | -9.73751 | -55.36946 | 2025-09-16 04:51:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 811d6a01-0e4a-3018-bec5-c03987e3dfd4 | -8.66524 | -46.36909 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e6f31f4-0973-3d40-88a9-3c6f90c737bc | -14.84959 | -45.50841 | 2025-09-16 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90071b54-426b-36a9-939f-332f02e73480 | -12.67246 | -48.02085 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 079ac96b-1dd9-3c4f-97a2-042e63992306 | -11.12214 | -45.34251 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5caac163-28d2-3576-851b-9a32357836d7 | -8.76247 | -46.10172 | 2025-09-16 04:51:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d150984b-eaa2-3e6a-9544-824c42c084b4 | -11.13723 | -45.34456 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ba947f5-b347-3230-a70c-944749bccc38 | -9.85882 | -46.45482 | 2025-09-16 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 30f9e70e-a721-34dc-bdf2-6db2c5357868 | -14.80902 | -51.66192 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa3ad26f-0dee-3692-bb22-87f86918d6e4 | -12.85757 | -47.14185 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fe791ac9-6786-30a5-a992-3a746d7f1285 | -12.85329 | -47.14291 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93845506-0516-3d6a-a5e4-cc3ddc23f741 | -9.05202 | -44.84815 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51d6a317-8097-305e-90b7-a9808dda2736 | -14.82679 | -51.66463 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9ecbfbd9-1e22-3d9a-9557-73bbf6f7c482 | -9.09927 | -44.87152 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 41.9 |
| dbd69900-6da9-3b3c-9f8e-6931aafe49a6 | -10.71705 | -44.75297 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e807489-ecdd-3c92-8df7-0bbdc2b477f6 | -12.70096 | -47.73907 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e44930a-8ee2-3a7d-8384-40ea1dcd9ecb | -10.70977 | -44.73537 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 633f8294-41f2-3ec1-818c-ee9fa0b42cf1 | -11.69788 | -46.87564 | 2025-09-16 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fbca4573-ae8d-3aa2-b565-73ab1309ce3e | -9.05544 | -47.02108 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ee34996-e234-35c8-885d-bc179d95dbf8 | -8.4343 | -55.64359 | 2025-09-16 04:51:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 38c53d81-6726-3590-9b20-38b230c02127 | -9.09806 | -44.8501 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd52b7c8-3f3c-343b-bb36-449c1644608f | -14.13878 | -46.26181 | 2025-09-16 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63af8cab-facd-320a-9733-c1393b343f57 | -10.71338 | -44.7488 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1637eaae-448a-3614-8c41-dc381f360400 | -12.67409 | -48.00866 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4b8ad7a8-1e82-354b-afc8-96b1ee78a592 | -12.75737 | -47.97533 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 826d0d05-0776-3708-8c52-d347b51a7031 | -8.95631 | -45.87305 | 2025-09-16 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a744399-7152-3002-aba5-5a26fe9d26f5 | -14.87886 | -51.67548 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f52cbf73-8a66-3ffa-bed6-7934ff714cd5 | -12.75852 | -47.96704 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2716349b-b272-33b2-a094-5b6df4c4a7e9 | -9.15236 | -46.97133 | 2025-09-16 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f989b32b-75e6-3677-afe4-dad892303d86 | -10.71664 | -46.49836 | 2025-09-16 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8094d529-43cd-370c-bbe3-bd62e17111fe | -8.09218 | -50.15743 | 2025-09-16 04:51:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0280e3f6-0751-3341-a9b2-256d20a6aece | -8.88087 | -49.93374 | 2025-09-16 04:51:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eeea9167-9157-3e7c-bcff-6221c8a5f1bf | -13.20012 | -47.30972 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 814eae26-fc67-3843-8aa0-f450ea56e6b9 | -14.61696 | -46.37976 | 2025-09-16 04:51:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3f78f09-24b5-35be-9d81-9ca61ced0a4e | -12.64464 | -48.00012 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2518459f-be55-39f8-911b-2464630d6e20 | -8.95401 | -45.87588 | 2025-09-16 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 43158527-b32e-3d97-99d5-17e46d50a7de | -9.08743 | -44.85251 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e66283f-f624-33ed-868a-14a62fb65059 | -12.76466 | -47.97057 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b4ecc3f5-caf6-30bb-a28a-1617b319c66c | -13.7618 | -48.75869 | 2025-09-16 04:51:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9eec1281-7975-3e72-b748-933da1a7deb2 | -11.4753 | -43.58408 | 2025-09-16 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19504054-23e5-312d-ac7b-1959db6f7e27 | -11.44115 | -46.94564 | 2025-09-16 04:51:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 054869c3-0067-3920-97ec-a0e2e76d29a4 | -12.94791 | -47.96345 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6d61ae97-c042-311f-82bd-7696758e2083 | -8.41652 | -47.21382 | 2025-09-16 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 895e78b8-6986-3e03-ab48-0add71fbfab6 | -12.79678 | -47.25145 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README68.md)
