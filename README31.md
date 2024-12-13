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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c2745f7-0c08-301c-b915-4e4ff4a001ae | -6.76713 | -44.82797 | 2024-12-13 05:10:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 918bb7be-35c3-392c-9bea-a5a389c0b3e4 | -4.24421 | -41.92583 | 2024-12-13 05:10:00 | AQUA_M-M | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 73fe0912-d664-3ae7-b1cf-438185510411 | -3.82934 | -41.55584 | 2024-12-13 05:10:00 | AQUA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 0782d0d7-a4fd-3250-aa22-524dbe44478a | -5.21076 | -43.29783 | 2024-12-13 05:10:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 6b19bb2a-34fa-33c3-8b48-c95d7196b10c | -3.82803 | -41.56462 | 2024-12-13 05:10:00 | AQUA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 1aa2ea59-ee42-31fc-b305-65bf4bdf0fea | -3.13864 | -40.0507 | 2024-12-13 05:10:00 | AQUA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| dcb882bb-4494-3370-b2e3-d88e14e0c093 | -4.16727 | -42.43704 | 2024-12-13 05:10:00 | AQUA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| ac75921a-7881-3c01-923f-cce1da8a9174 | -3.142 | -45.58265 | 2024-12-13 05:10:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 8f61ca20-63ef-37ff-9063-2dc0a2e13bd0 | -5.21216 | -43.28869 | 2024-12-13 05:10:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 90abcc47-d0dc-37bc-bccc-4342f5c2669c | -6.12838 | -42.53957 | 2024-12-13 05:10:00 | AQUA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| ff330d1a-95ba-3d59-b19b-7ff081cd9654 | -4.16593 | -42.44591 | 2024-12-13 05:10:00 | AQUA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 592c691c-40d7-3fec-a0b4-0b77e640a423 | -5.45711 | -44.80973 | 2024-12-13 05:10:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ccbe1e84-4c5d-3361-a428-6725d7d024ac | -6.96493 | -42.99756 | 2024-12-13 05:10:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 6b8ae6f7-294d-3a6f-9bfd-471a65bd40af | -6.91545 | -43.50548 | 2024-12-13 05:10:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 07b176ad-edc7-3afe-b358-41dc81e1728b | -8.7149 | -44.00179 | 2024-12-13 05:10:00 | AQUA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0ae16a0c-410b-364d-a929-1639b59733bd | -6.09342 | -44.75576 | 2024-12-13 05:10:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b0e5a22b-b0a9-3a4f-b1a8-d7484d8d05b0 | -5.62776 | -44.83701 | 2024-12-13 05:10:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 523c71e9-3d14-3079-9697-f9904868c701 | -4.54862 | -43.57567 | 2024-12-13 05:10:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0a966eb6-0b06-385b-b856-b232daf7dfc3 | -6.91407 | -43.5146 | 2024-12-13 05:10:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 7be40107-adad-337c-a3b9-cc120823a08f | -6.92303 | -43.51594 | 2024-12-13 05:10:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 5c731d9a-cdbb-3046-a499-4a41eb5c1d10 | -3.03588 | -44.47537 | 2024-12-13 05:10:00 | AQUA_M-M | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 09b87333-c248-3149-a317-9aaf0f4972ca | -3.28228 | -45.59018 | 2024-12-13 05:10:00 | AQUA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 13.2 |
| aa9e444f-6760-3e5d-ad3e-25d593262b75 | -6.05756 | -44.043 | 2024-12-13 05:10:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 233c5497-45fe-3715-8c37-ba174d9f65f7 | -3.28857 | -45.58433 | 2024-12-13 05:10:00 | AQUA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| cfb1082c-1b58-3bf1-b2c0-9e4244918ce7 | -13.06647 | -52.04088 | 2024-12-13 05:12:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 35.6 |
| da2a4e30-f987-3f0f-a8ad-ffeb6b18b06b | -12.5497 | -57.7196 | 2024-12-13 05:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 0efa325a-180b-3cdb-893f-8148d60087d0 | -5.2108 | -43.3067 | 2024-12-13 05:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 14906a08-fbe0-3642-bfe3-af0c69efac6e | -6.9158 | -43.5185 | 2024-12-13 05:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 139.4 |
| e8f22878-1224-3c37-bd18-7b156219ad80 | -6.9156 | -43.5418 | 2024-12-13 05:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| f512e8d6-b6d5-3ac8-8f22-abd8e7c6ab0c | -6.9344 | -43.5401 | 2024-12-13 05:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 61.9 |
| bb15d126-d504-3c7e-8535-e31c0f587bec | -5.211 | -43.2833 | 2024-12-13 05:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 6a14b64d-d0f0-3276-a3c5-604bf5b398aa | -6.9161 | -43.4952 | 2024-12-13 05:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 1b5845ad-32de-365a-8e8a-4685ba6acbe6 | -11.2151 | -53.8125 | 2024-12-13 05:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 880189d2-75ac-3de4-8978-6e450408725e | -6.9346 | -43.5168 | 2024-12-13 05:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 117.2 |
| b449caaa-b29c-3cbe-a12a-66a10922e3f7 | -11.1959 | -53.8348 | 2024-12-13 05:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| ba5a1702-50f2-393b-b0bb-3f0744cf5023 | -11.2148 | -53.833 | 2024-12-13 05:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 7b7502e1-fcbf-3b7f-ab7f-783333255ff4 | -6.9349 | -43.4934 | 2024-12-13 05:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 127d670a-64bb-3e0f-94f1-0c70f4251e9d | -11.1962 | -53.8142 | 2024-12-13 05:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 22779eff-acd9-3370-922b-0fe45679732c | -13.0644 | -52.0326 | 2024-12-13 05:20:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| e4439675-f14a-3227-924c-91e98eb6a3e9 | -2.1173 | -54.6472 | 2024-12-13 05:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 99212574-ba3f-369b-b466-6b023dff38ff | -5.211 | -43.2833 | 2024-12-13 05:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 63f5aa5a-a5df-3bc0-8f98-b1ca215c28ae | -6.9158 | -43.5185 | 2024-12-13 05:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 28f6331d-cedc-3ee2-ae1f-2252e0c9fe41 | -11.1959 | -53.8348 | 2024-12-13 05:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 1af03921-cdde-3cb6-b024-81b60966e75e | -6.9156 | -43.5418 | 2024-12-13 05:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 6e4b547a-de37-3797-8e83-9caebe9efd3c | -11.2148 | -53.833 | 2024-12-13 05:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| c0ceaac3-fa80-3ec6-b07d-167547812263 | 2.74185 | -60.64118 | 2024-12-13 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9c0e4469-4dfb-35cc-a04d-0d6a41b7d080 | 3.26084 | -60.54558 | 2024-12-13 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 00662f3d-0d9d-34ec-8e67-192fcdc4ee82 | 3.19149 | -60.30102 | 2024-12-13 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2d6f333-efb9-3ce6-b474-a357ede49047 | 3.64764 | -60.02706 | 2024-12-13 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 832b7368-5207-3307-801f-1c4a6081a1f2 | 2.74129 | -60.63764 | 2024-12-13 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2b9c3f3b-ce12-32b8-a57c-cb1740f7bc91 | -2.22645 | -53.70992 | 2024-12-13 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4cec1a21-5a61-31a5-a1c6-87fbfa6ecdc2 | -1.70041 | -52.78077 | 2024-12-13 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bb44f1e3-5622-36b5-ba77-fcf7cb38a1f1 | -1.23854 | -54.13908 | 2024-12-13 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b2117cea-cda8-30b5-9b4b-2fb20943bbcc | -1.23809 | -54.14204 | 2024-12-13 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 702c4912-5ddf-3576-b2b4-2f0c764fcd0d | -2.41256 | -53.70095 | 2024-12-13 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1664eb46-ac21-3014-bab2-2711aafc6666 | -2.10796 | -54.65643 | 2024-12-13 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c2a5ea87-360d-3f68-b4e5-fe78f31a7933 | -1.62809 | -54.01897 | 2024-12-13 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ccf165e-e15f-3212-983b-65d62af5728d | -1.60302 | -53.86325 | 2024-12-13 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8001b5cc-a80c-3b50-b7e9-880d70208429 | -2.23207 | -53.43868 | 2024-12-13 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1395e093-1e26-3d51-a81c-68a8bb12940d | -2.23571 | -53.72199 | 2024-12-13 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f5f98783-3c9f-3ed2-93b4-df7bc5acd8f6 | -1.63333 | -54.01973 | 2024-12-13 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db050b1b-7593-38e5-b121-a3e8b291b1d3 | -1.23296 | -54.14105 | 2024-12-13 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b4bda16-01a1-302f-a989-cad58b09f21d | -2.41307 | -53.69756 | 2024-12-13 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 449fe0cd-71d3-3550-b862-9f70ef35f72d | -2.11058 | -54.63881 | 2024-12-13 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 33cabb11-7d54-3854-bd76-ea6963853c07 | -1.68784 | -52.55493 | 2024-12-13 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eca491c5-e685-368b-99a3-155bdea035b8 | -2.22443 | -53.72368 | 2024-12-13 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19a055b4-9346-39c9-930c-5e7e80f77140 | -2.23032 | -53.72113 | 2024-12-13 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c274703f-075d-375c-b56d-aeb5b73ae675 | -2.19405 | -53.6528 | 2024-12-13 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 309b004b-b99d-32fa-b340-1f1a32fc73ca | -2.00657 | -54.51063 | 2024-12-13 05:35:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5978e6c4-e427-38f8-9ee6-df2a2130c761 | -2.2352 | -53.72541 | 2024-12-13 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 49833382-d981-3163-a12e-76e2f1930478 | -2.11014 | -54.64175 | 2024-12-13 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 216b61a4-5fd9-3cac-8098-3ff77991409e | -1.91773 | -52.64625 | 2024-12-13 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 757c7359-5d67-3e6e-b899-60f7ab46b3a3 | -2.11301 | -54.65722 | 2024-12-13 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 518c94bf-2e7f-3e98-9af8-09223d83c9fd | -2.22696 | -53.70645 | 2024-12-13 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5277e876-e96e-3af8-8bd2-92095aecc0ab | -1.63297 | -54.01888 | 2024-12-13 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2bcc5fbc-0295-3c84-9d90-92dce285f10f | -2.22982 | -53.72454 | 2024-12-13 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ced4dc2d-756a-3e99-875b-d39bd42ae0b2 | -2.41847 | -53.6985 | 2024-12-13 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48ff5653-3f11-309c-a465-8498e5ea5e56 | -2.45198 | -53.71033 | 2024-12-13 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0f6cef5-9988-35d4-89c5-4d6381a77e94 | -2.22449 | -53.70692 | 2024-12-13 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 863f6eb1-915c-3b13-9faa-d3334f4bdf15 | -2.31165 | -53.74823 | 2024-12-13 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f562d7d-862b-3d60-aa72-734e49043e24 | -2.36278 | -53.92133 | 2024-12-13 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c02ee28-2a1b-394c-bfa0-2d4b2d0a2ed2 | -1.99633 | -54.50948 | 2024-12-13 05:35:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e31a3c88-3615-3c39-a1bb-2c8c289745fc | -2.001 | -54.5131 | 2024-12-13 05:35:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90283a8c-d056-3ae5-9ac3-08f4c68748b6 | -1.91712 | -52.65025 | 2024-12-13 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6d52eee-0fa4-343f-a6e9-16c79d707a56 | -1.63248 | -54.02208 | 2024-12-13 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17e03909-eb45-3eac-adac-ecf14d95845b | -1.99588 | -54.51251 | 2024-12-13 05:35:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8c65f0e-6e01-3486-84e4-f3e6e1535c25 | -2.45737 | -53.71129 | 2024-12-13 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb19e4ee-43c7-398e-b5a7-1838e08bf566 | -2.00055 | -54.51615 | 2024-12-13 05:35:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bac507f2-83e0-3eed-aa77-8a8e89437a48 | -2.11257 | -54.66016 | 2024-12-13 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bc957b95-d251-3513-82fc-d0abe2ea1d6f | -2.18863 | -53.65205 | 2024-12-13 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37178b5f-40fa-382d-88d0-b9ffcad189dd | -2.31446 | -53.74825 | 2024-12-13 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afac4cfa-40bb-3cc2-adef-ee832adceb06 | -2.45149 | -53.71368 | 2024-12-13 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 20c32765-2a59-3def-b3af-3bd634fb0ca9 | -2.30754 | -54.0002 | 2024-12-13 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a9d1464f-8499-32dc-9e16-7c51bd1b6f18 | -2.36327 | -53.91812 | 2024-12-13 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ccfbc0b-8d88-3159-bc53-583ff9d8eeec | -11.42879 | -55.92339 | 2024-12-13 05:37:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ab1b9f9-d1c4-301e-aa8c-3643db0c8f80 | -11.43942 | -55.92467 | 2024-12-13 05:37:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4168578-d8f5-3943-85b6-6e6b2c6b868e | -13.06571 | -52.03844 | 2024-12-13 05:37:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c61f5123-1528-37df-aa67-594178b25d74 | -11.20669 | -53.83184 | 2024-12-13 05:37:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| e36a4d41-c4c2-3f57-81ca-153dc96ddfbb | -11.2078 | -53.82243 | 2024-12-13 05:37:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e6b731d9-963b-3d04-9307-29c70d44dc52 | -13.05928 | -52.03246 | 2024-12-13 05:37:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README32.md)
