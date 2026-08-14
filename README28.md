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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2feb7867-d860-3a49-8d2d-aa0922055f28 | -3.34188 | -50.14682 | 2026-08-14 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11150d36-d422-3dcd-b122-f4f218718a9b | -2.7922 | -49.52335 | 2026-08-14 05:16:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0434c02e-35be-3f43-ae32-66209254a69a | -1.83176 | -54.50087 | 2026-08-14 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 1e8c6f0a-e3dc-3540-b0d4-7334c8497ff6 | -2.79441 | -49.58109 | 2026-08-14 05:16:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| fe76ed5b-7163-32e5-bfad-8adecd6a26f5 | -2.69312 | -48.22096 | 2026-08-14 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 15213b1d-fbf1-3942-a03f-e04a275145ef | -3.11776 | -59.92891 | 2026-08-14 05:16:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ad2c9c5a-d18b-38a6-bcb3-664ce8dbcc33 | -3.05647 | -48.7443 | 2026-08-14 05:16:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c093c65-9ba0-3554-87e3-89f11ef2499e | -2.6443 | -47.98267 | 2026-08-14 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 40df1272-5ee2-3452-9b53-c30ab45366b9 | -3.33681 | -50.14716 | 2026-08-14 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 12d80ef9-9ac8-35ed-8a11-e29091f3d395 | -1.36947 | -60.26256 | 2026-08-14 05:16:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5660cfff-2eb4-3931-be85-e4f1bbb71d92 | -3.24485 | -60.12788 | 2026-08-14 05:16:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2785adf0-6c94-3b7d-993a-f6209cae8bf3 | -7.49499 | -60.07985 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d755cafd-3e71-3159-9e00-ac412935f89c | -11.85945 | -51.95799 | 2026-08-14 05:18:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fde3d0e8-6d2e-3e59-b51d-c8ad73d83cf7 | -11.06726 | -50.95166 | 2026-08-14 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18908697-9eed-3e14-a2c8-67c1af456066 | -7.40727 | -59.98981 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5870515a-8c88-3f61-8497-772980f50da8 | -8.9506 | -60.53287 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e63d40c-e8c2-3c56-b276-e866468f25e6 | -8.95786 | -60.50867 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| facd118e-9db2-3638-b2ec-e61be8f5fc43 | -11.06765 | -50.94036 | 2026-08-14 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5cf5ec12-d791-38c9-be10-36686498d181 | -6.62447 | -58.99471 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 56aa00bd-d007-3b94-9359-e832785fa0b4 | -6.60768 | -56.33545 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8918fa15-1ca9-36bd-9a18-09a6233293ab | -9.83161 | -65.06265 | 2026-08-14 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2087867a-5c57-3598-9325-a6e492ed1702 | -11.07746 | -50.94849 | 2026-08-14 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0013af2e-aada-3277-ac1f-daee8a8ccdb2 | -7.7098 | -46.23857 | 2026-08-14 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 23a7f0e2-d649-34bd-9720-4feb40a7e35f | -9.60601 | -66.18465 | 2026-08-14 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c71a391-c8db-3158-ba89-8c0a222cc42e | -6.61308 | -59.04604 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 29b7e157-51aa-399f-9297-0cb23c2ea4af | -6.60939 | -56.34814 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c49888f6-fc17-34c1-99a8-6c2c9d90628f | -7.38122 | -59.96078 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd085f66-2356-3f86-869a-2f0dbae5aa2d | -8.55376 | -54.59504 | 2026-08-14 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ec7a280-8ef0-3696-9dd9-6249117852da | -6.86124 | -56.40712 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5ed1b89-9734-3000-9874-ffa03cc20f39 | -7.71096 | -46.23733 | 2026-08-14 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0ed9b967-2e97-33e1-b950-5ece2fbe9d9e | -7.38289 | -59.97177 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62c6a0e2-7c83-310e-8fba-5af037c9e48b | -7.05789 | -56.52061 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20f08465-f7d4-34b0-992d-206332baac4d | -9.07558 | -61.39235 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67f3231e-bf23-34c0-aa8b-2ff022e4b6bb | -6.70566 | -58.95485 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0fa58a6b-fb78-337c-a69b-abf269f9305a | -11.75453 | -50.12959 | 2026-08-14 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ce19192-9939-3c94-b82f-87ea6a403458 | -8.89888 | -60.56094 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 865033c0-6248-3ede-84cb-942e8530887c | -9.75906 | -60.75753 | 2026-08-14 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07e269eb-0af8-3240-8bed-5e7ac89ffd9b | -8.71872 | -54.59824 | 2026-08-14 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 659c409e-e9ec-36c8-94dc-93cdcdc37030 | -11.06856 | -50.94168 | 2026-08-14 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fbc13667-62a2-3a18-85da-1adf88ee07f3 | -11.49671 | -54.63884 | 2026-08-14 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5c16b175-b579-38b8-b356-1c44d5736856 | -9.58244 | -60.49742 | 2026-08-14 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5dc0597f-138a-378e-b83e-f63d6ebabd13 | -7.55241 | -61.16794 | 2026-08-14 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c1acd60b-45b7-3ce9-9bb3-a9c2d1de0ebc | -12.32749 | -50.86212 | 2026-08-14 05:18:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0dcc9f9a-a782-30d3-8abd-00708ad11303 | -6.61531 | -59.05346 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1066b218-8e2d-36ad-a0b0-cf9a43ec9fb4 | -9.19564 | -66.0982 | 2026-08-14 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f54f4fb-6938-3150-872b-7cd54f7d7dd0 | -8.72273 | -54.59882 | 2026-08-14 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 046bbe30-8516-362b-a537-a0aaa99e220d | -11.48162 | -54.62507 | 2026-08-14 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 354512fc-1d0a-36da-9c6b-ce98b531a204 | -11.49985 | -54.61586 | 2026-08-14 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e5c839c0-72eb-3dde-86bf-40ea0c940fcc | -9.98117 | -53.95449 | 2026-08-14 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| b8682c3c-f472-3e2e-a1db-01d877908f54 | -7.38177 | -59.95728 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb60a782-ed48-328a-bc7b-66e6cc205aec | -11.49307 | -54.63445 | 2026-08-14 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 929ee5e1-d2be-3fa4-93f8-ecae563cd77f | -10.97557 | -50.534 | 2026-08-14 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4074928a-aa1f-3b3f-968a-ee082d056dba | -7.37293 | -59.97021 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a71973f-208b-3c6f-a384-cdb9cb1135e9 | -6.623 | -59.04758 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 6da6ca84-9007-3e59-b277-22888ef2c6dc | -7.60187 | -46.46737 | 2026-08-14 05:18:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 48439f20-9a3b-3e5c-802d-e515b0a96a1d | -6.58763 | -59.01376 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43e15c00-e207-3e6e-8baa-31ab82620624 | -11.80749 | -51.80697 | 2026-08-14 05:18:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33d8a813-73ba-3fc4-bf0c-59658fb2e1fb | -7.04146 | -56.50655 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7c62308-b0b9-3dca-993c-d5b4c3ce5fe8 | -10.07888 | -60.49797 | 2026-08-14 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 87f65861-d132-3172-ae50-bdf964a60665 | -7.55181 | -61.17165 | 2026-08-14 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 353212d3-e0ff-33e8-950f-aa3abc7beb83 | -9.96894 | -53.94865 | 2026-08-14 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 862b72bd-3b31-31bc-ae04-df6d7b4886fb | -9.97747 | -53.94982 | 2026-08-14 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 39be9776-2a0a-3f11-b1ed-1894361cad54 | -11.99226 | -53.45428 | 2026-08-14 05:18:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 799e4d4e-a85a-3292-a7e7-821874192f92 | -9.77058 | -60.76727 | 2026-08-14 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9193a15-9450-3e74-b0f4-fd4eaddef58f | -11.49516 | -54.61914 | 2026-08-14 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fd163781-d782-3538-ac6d-31329c7bd6fe | -6.62077 | -59.04015 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cd188148-a328-3d53-bf7e-5988d7e5f241 | -10.94271 | -57.12864 | 2026-08-14 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2bfe81e-ab43-3ae3-9858-f4f18248a9eb | -6.59639 | -56.36245 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09091e3a-98db-3853-bb46-ce4672b5f9c1 | -8.89944 | -60.5574 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0749e517-deaa-3d55-b706-a38a4f5e28cf | -6.62738 | -59.04119 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c18e85f-0ceb-342c-9df6-499e8eed7b77 | -9.75625 | -60.7753 | 2026-08-14 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10ab2651-6675-320a-aea3-6b48b25bb34d | -9.58854 | -60.50201 | 2026-08-14 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b185a3b-4e26-3e58-b1a0-4417a8054399 | -6.11177 | -53.07491 | 2026-08-14 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6187ea37-7a01-3e82-bb10-5ab1e7c73081 | -7.60496 | -46.4659 | 2026-08-14 05:18:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 89b29182-5526-39f8-b3a6-a7802ab151a5 | -8.55327 | -54.59854 | 2026-08-14 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a02a760f-e79b-3ebe-80ed-ed7367291195 | -7.4034 | -59.99279 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62107a76-7d2c-3f7d-b280-72473875c695 | -6.78918 | -58.74459 | 2026-08-14 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 01a857f4-fb36-3567-8251-fbac29de0b97 | -11.47383 | -54.61997 | 2026-08-14 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0e40324c-3082-3770-9b0b-77c7a801be8e | -6.88691 | -59.01147 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ffbbe96d-9e3b-3639-91f2-c3da3be3a8e6 | -6.12416 | -57.90029 | 2026-08-14 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a444275-0e6b-3184-a78d-b7449c18ded9 | -11.62194 | -55.17937 | 2026-08-14 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b785948c-9cb9-3a9a-a669-f47cb07a5d7d | -10.59539 | -55.59529 | 2026-08-14 05:18:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f6869868-b2e6-3c9c-8d2c-da331b99eafe | -7.38012 | -59.96776 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ccbe954-ce13-3cb8-8e1c-6855ff0daded | -9.07677 | -61.38497 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 549e3fb8-4241-3b71-b00b-a93aed210479 | -8.97726 | -60.53711 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96559252-329c-3031-b6dd-8a4f9c2d238a | -6.61915 | -59.05052 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4fa5561c-4142-3ee5-adb0-1e811d8809bb | -7.70488 | -46.23009 | 2026-08-14 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ec413a22-b537-3591-8bd5-387df01dd584 | -7.59426 | -61.21272 | 2026-08-14 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02996bdd-f38d-3f1e-b7a9-d1e963317896 | -6.60998 | -56.34417 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 131df8df-63e0-3298-8692-9dcd0aec6d51 | -6.70343 | -58.94742 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bd4d0a96-b6f9-360f-a330-ceef39e37817 | -8.55229 | -54.6055 | 2026-08-14 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8d55319-1c15-382d-9fe7-588c7c56b14e | -6.96341 | -59.28621 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3417b9be-6732-35c7-a1fd-3fa70294afe1 | -9.83225 | -65.05901 | 2026-08-14 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb6a6877-3f59-3e2b-bfc8-7ae7a2fd1796 | -6.96618 | -59.29019 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c5c8214f-6c9c-316e-bcbf-c80ee8c6e8e6 | -8.77631 | -63.97615 | 2026-08-14 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30b07332-1dbe-3b83-8ef1-750e1b482615 | -10.59608 | -55.59039 | 2026-08-14 05:18:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c05bd5d2-5bb2-3568-959d-ec5f69b13777 | -6.96029 | -52.80614 | 2026-08-14 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 13e58d8b-71cc-3dd9-bd49-10d0f37c8152 | -7.40672 | -59.9933 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b5a1395-68a7-3676-ad5f-87630df6560f | -11.97809 | -48.66069 | 2026-08-14 05:18:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f65d2026-7cc8-3123-8538-47c3c78ad4ee | -11.50507 | -54.60874 | 2026-08-14 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README29.md)
