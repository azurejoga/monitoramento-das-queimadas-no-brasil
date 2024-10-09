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

## Dados Diários - Página 204

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20e76c60-eafc-3049-ae1b-8787ecced688 | -3.01238 | -59.11127 | 2024-10-09 05:53:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c6a3bd00-6dcf-39bb-9946-2bf1e29537b6 | -2.68557 | -59.57727 | 2024-10-09 05:53:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e31c153-c73d-3731-b975-e52f450c9b12 | -4.38008 | -59.94132 | 2024-10-09 05:53:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3f63cada-c55e-3def-9169-88fb5f2f74ec | -4.29795 | -60.02034 | 2024-10-09 05:53:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 965a24e4-06e0-3a14-a7bf-18425906eef8 | -4.29621 | -60.01927 | 2024-10-09 05:53:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c93b3dc3-51f5-3d78-95f9-d603c494be6e | -4.29381 | -60.01403 | 2024-10-09 05:53:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8de14019-3b7d-306d-bd35-6f88dfe852fa | -4.29302 | -60.0196 | 2024-10-09 05:53:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e5a6ca82-5202-31c8-b525-743e4d5e7fe2 | -4.29212 | -60.01297 | 2024-10-09 05:53:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| fd4fb90a-f55b-33ea-8ef7-c9e9f88b61e1 | -4.29128 | -60.01853 | 2024-10-09 05:53:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bfe2ff29-6b60-3a08-8497-6d58e1dea84f | -4.28889 | -60.01326 | 2024-10-09 05:53:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f22e9243-91a0-3329-9201-f09a3f505f12 | -4.2872 | -60.0122 | 2024-10-09 05:53:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 17aa448f-46ba-3f01-8e9f-70c98b3694ed | -4.28397 | -60.01249 | 2024-10-09 05:53:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b3906c2-7c13-3c61-b094-7466d614482e | -4.27817 | -60.00517 | 2024-10-09 05:53:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce3a5893-52df-3828-b491-e75d6dcae3d9 | -4.27325 | -60.00441 | 2024-10-09 05:53:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc4fed35-b2a2-3a89-88fe-e2658c07d588 | -4.11336 | -59.87686 | 2024-10-09 05:53:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 879d1bde-0ec5-3959-83a3-3ce029d468f9 | -4.11256 | -59.87497 | 2024-10-09 05:53:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b45e29a2-3741-39f7-9d34-9d26cca6e0b8 | -4.10759 | -59.88172 | 2024-10-09 05:53:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8b418d22-db64-3b7a-8a05-db59eefc855c | -4.10675 | -59.87983 | 2024-10-09 05:53:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 94506c08-cf01-395d-8229-df0e1f66c5c0 | -4.10591 | -59.88545 | 2024-10-09 05:53:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6984641e-1a8f-377a-8854-ace47cebee29 | -4.10264 | -59.88094 | 2024-10-09 05:53:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 54f773cd-5bf6-3ec5-bb39-3b1eb9e3887b | -4.10096 | -59.88465 | 2024-10-09 05:53:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3a0b8128-6206-3586-be1c-8060cbfd65fa | -3.08343 | -61.05972 | 2024-10-09 05:53:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 34b7542f-e349-35aa-b9c4-4a643d22b2ed | -3.07826 | -61.06358 | 2024-10-09 05:53:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee93227c-20aa-3501-8de1-d7b483689d6c | -4.72038 | -60.81762 | 2024-10-09 05:53:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1e088759-cd7e-3ee9-a8fc-2835ec391a4d | -4.71964 | -60.82257 | 2024-10-09 05:53:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| df471e2b-e098-34b5-8eea-715978c36488 | -4.71853 | -60.81447 | 2024-10-09 05:53:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1a41defa-9da2-3835-92b2-a77b8b4a5f88 | -4.71783 | -60.81942 | 2024-10-09 05:53:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 45e44e8c-a048-3820-a2dd-332cf3b31426 | -4.71569 | -60.81694 | 2024-10-09 05:53:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e10602ed-4665-38d6-87d2-56787df406eb | -4.11967 | -60.7796 | 2024-10-09 05:53:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bce3c251-29f3-3e28-a764-82f92a00cbf7 | -4.11896 | -60.78448 | 2024-10-09 05:53:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2a93e60-b0c9-32fa-92c4-e9b154232826 | -3.88791 | -60.59434 | 2024-10-09 05:53:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61e49fa7-c278-321e-bb27-752ca0dfe072 | 2.31157 | -61.28592 | 2024-10-09 05:53:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db3ec673-c6ba-33a9-bf4f-fb5249ce62c8 | 1.609 | -61.02342 | 2024-10-09 05:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ecfb90ab-e95b-33d3-a489-7ec0a3c9900d | -3.29164 | -61.59355 | 2024-10-09 05:53:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58648088-5b28-3fb2-9847-45533a32ebf2 | -3.0435 | -61.6851 | 2024-10-09 05:53:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aec31135-f5fa-3ca2-b939-2b03b87b86c9 | -3.0392 | -61.68445 | 2024-10-09 05:53:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8365a5e5-73d2-3c3a-84e5-c0bafff271ef | -5.89027 | -63.90294 | 2024-10-09 05:55:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca68f19e-db28-375e-926b-467dc49abdac | -7.35945 | -64.66551 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 34f7dfab-7554-3738-955b-42135a228ae4 | -10.89268 | -64.16027 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b18d2b35-5626-359c-83d8-c2f1984ff97e | -10.8385 | -64.22089 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2daddc5f-05e4-3612-b28d-c8e58e0d1da8 | -10.83596 | -64.1785 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f59c0578-e269-36f1-b7c2-237fa57fec70 | -10.8319 | -64.17768 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39785959-0972-3864-aff6-61fa9d33b0f7 | -5.89187 | -63.90082 | 2024-10-09 05:55:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7c0062b2-cab9-3a11-8dfc-0f2d40857c96 | -5.89116 | -63.9057 | 2024-10-09 05:55:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4b2b7cc-25a1-3e18-8809-60d8702157af | -5.89101 | -63.89807 | 2024-10-09 05:55:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6029892-c34e-3f82-9069-5e36545a04f1 | -7.35877 | -64.67013 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eb730404-801d-3785-a7fe-4391725a5892 | -7.35808 | -64.67474 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ccf4caa9-7ce1-3951-a6db-43862e6d16e0 | -7.3574 | -64.67936 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 56369fb7-d6db-3d5d-bbd9-96c4c92f066d | -7.35568 | -64.66495 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 52cbf18f-7cb2-3116-be6d-e5b5afcc22bf | -7.35499 | -64.66957 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9114d1a3-883d-3afb-aaee-719e0d36155f | -7.35431 | -64.67418 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a4d8326b-7d49-3d52-bdd6-07d16fbf5e40 | -7.35122 | -64.66899 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4de3deaf-a016-3c7a-9b56-c75c89fb68cb | -7.35054 | -64.67361 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 014b3450-1a4f-337b-a80b-1521b31a6be7 | -7.30148 | -64.6662 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a97516fc-5570-3d8e-860d-7aca481b8b72 | -6.82484 | -64.32551 | 2024-10-09 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 39e7d2c3-16fe-3746-9329-70a7ee903d51 | -6.82415 | -64.33025 | 2024-10-09 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ada65ce-fbf4-372b-8c34-f9175f327264 | -6.82032 | -64.32968 | 2024-10-09 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54bdd04e-5492-3bbd-8180-4b88237f8ccb | -9.43091 | -64.29903 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06415433-4366-3969-b2ee-d972103d7514 | -9.99304 | -64.77463 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ac8ba82-1d07-3a3d-aff5-7678addf96a8 | -9.99235 | -64.77959 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d67870e-5c54-3de0-ab6c-64045747c4f3 | -9.98916 | -64.77402 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2085c7c1-de0c-3045-a615-3a39337f9443 | -9.98846 | -64.779 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 118f404c-d862-362f-9fd5-b9c5af0bfb1e | -9.9882 | -64.7724 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 480e2886-560e-3d1b-a7ae-e9eb57a348d5 | -9.98777 | -64.78394 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 698851e7-1541-3386-a6cb-6edd3594562f | -9.98747 | -64.77737 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 813a6436-c46a-3998-bd9a-064970da6ec4 | -9.98674 | -64.78231 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec3378f3-0290-3d3a-92b2-389365b65889 | -9.98458 | -64.7784 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4851fb95-511d-30ae-bdec-2b7d40260be7 | -9.9695 | -64.76452 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38f06424-a692-3d1f-b21e-1f48af31e4d4 | -9.96274 | -64.78376 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75e1ee6e-35fb-399c-a650-64e255122142 | -9.92401 | -65.04966 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec4fad56-2eb8-3612-800d-321e4a84a134 | -9.92019 | -65.04911 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 19d1729e-0b79-3059-bc64-2bf9e3fa37f8 | -9.91935 | -64.78229 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86c8fd9c-25fe-3bff-8934-ca937c905245 | -9.91618 | -64.77677 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 625330d2-6b45-3739-80b8-3f0795bb62c7 | -9.91548 | -64.78168 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49be39b6-d00d-3e78-97e8-10e0ebc55a57 | -9.89918 | -64.92363 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c8a26e2-a7c3-3c5f-9936-bdf1ef97608a | -9.89533 | -64.92305 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3efaba83-1b60-39c5-b802-41af3d7b761a | -9.89149 | -64.92246 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1649e6f0-0e43-3b5a-b2da-70de133aabc0 | -9.88764 | -64.92188 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4922a0dd-0a11-3549-b9e9-dca9d504a210 | -9.79585 | -65.05273 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24bc280a-4d0e-3f86-8ee5-7ec0166e4db3 | -9.7377 | -64.91242 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7062f4f4-7013-3c16-b7a0-5bce08c0daa2 | -9.7294 | -64.8988 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 66ace5cf-94da-3b50-a5c9-27d7755f5540 | -9.58569 | -65.24501 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6cc9ef73-a3bd-3ada-a992-727f545ce899 | -9.58554 | -65.25175 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98ad11fd-f68b-32a4-a3ec-678653ed57f6 | -9.58501 | -65.2496 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 445c1d69-1497-383c-ae3e-d16249f80826 | -9.58434 | -65.25417 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ff1c81b5-df2a-3df9-b3ac-22e97040a039 | -9.58308 | -65.24199 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3e253ca6-ef35-3b08-b30a-54b9e18b5b1b | -9.58243 | -65.24657 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 808b1e55-5bf4-3ce1-a2f3-28d94142b76f | -9.58194 | -65.24445 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 165b0ee5-69e2-3850-b640-b6688f9f2262 | -9.58178 | -65.25117 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84fa45e4-325e-3be2-a5cf-113e7134b033 | -9.58126 | -65.24903 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc829f03-3af7-3323-a517-619bffc10754 | -9.58058 | -65.25361 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21de92fd-53db-31fa-a484-765c1b40d1d0 | -9.5775 | -65.24846 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 353eae1b-f997-34d4-af97-f0b88cde4747 | -9.57683 | -65.25304 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65353eef-1df9-3c7e-9cbf-4314ef1806cf | -9.49427 | -64.67145 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5ac38006-e051-3186-8e26-687f560f7d54 | -10.80252 | -65.175 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b573e8de-e18c-3caf-88ed-57a3980010a6 | -10.62693 | -65.2172 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 36c5b045-2998-30b9-8dc5-0384d35d4dc3 | -10.62379 | -65.21189 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b8e65826-d1b3-36c4-84b6-1512410b56f9 | -10.46512 | -65.29268 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b0a96af-0044-31dd-b8b3-4b6efa921ac3 | -10.0963 | -64.83759 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c16c70c-28fa-3572-bb69-f07a83f9ac13 | -10.09561 | -64.84245 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README205.md)
