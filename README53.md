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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88ad6ed4-440e-3191-b39e-1b388dee99ee | -7.44191 | -63.56221 | 2026-10-06 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 508e626b-65e5-39a4-881b-29fd2123a511 | -2.95779 | -54.1452 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fc951bf9-b420-300d-a5b3-2b943ce43e87 | -3.50771 | -59.50959 | 2026-10-06 05:23:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8768576e-ec28-3e7d-b194-1139cb701d75 | 1.86148 | -55.77164 | 2026-10-06 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d6307e1-47b4-3bf4-9f15-df4682d3229d | -2.77429 | -54.09917 | 2026-10-06 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4bb9e5ba-8e76-3f09-9a77-382c6a47dd77 | -3.09951 | -54.18201 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 163eeb9d-bfe2-37eb-a454-58fdd844baa2 | -3.46534 | -50.10277 | 2026-10-06 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71ceec3e-78d0-3394-8e51-a6ed46443644 | -4.26531 | -48.62527 | 2026-10-06 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 351ded4a-9fed-3280-bc72-dddb6fb67fb6 | -3.07771 | -54.18274 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cc28bc95-488d-3eaf-af51-0cbb22ceca35 | -8.6429 | -66.8571 | 2026-10-06 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2268810-f1a6-3506-862f-b651eca958df | 2.4586 | -50.83501 | 2026-10-06 05:23:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 12.6 |
| c380f235-28f2-34fd-8253-7b7801f53282 | -3.049 | -54.23075 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36d7610c-a6b1-34d9-9779-8101ac63a83c | -3.67138 | -55.94439 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2df9358-b727-31f6-b5ec-40b8de048e22 | 0.31498 | -60.43425 | 2026-10-06 05:23:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3847642d-86fb-3470-a092-65206aedbb97 | -3.09526 | -54.18141 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e6666831-3074-3aee-ac14-f9a11efa135d | -3.05842 | -54.16903 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 100becc2-47e7-32bd-bf80-67c2f87cb956 | -3.35404 | -59.49245 | 2026-10-06 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 8bab6264-6245-33ad-b012-ddb874b17cd4 | -2.78301 | -51.67264 | 2026-10-06 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 47155364-d4cb-3824-a76e-036abbcd1e8e | -3.22654 | -53.87677 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9dfd73a4-eebe-36df-b5b3-10a7dd2f025c | -2.98273 | -54.03474 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0d3dee81-3463-304c-b164-39f6ce65a944 | -3.05596 | -54.2131 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f7c07d4d-115b-375a-ab4c-7ef48f600552 | -3.07583 | -54.16601 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f67eea63-9440-39c9-90ab-34b49ae3d3a2 | -3.07642 | -54.16199 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2720e18-fc9b-3a81-b0a0-a3b2972b156c | -2.87304 | -54.16222 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 84f67d4b-bf62-3a50-8f56-0353814c8cfd | -3.9262 | -55.44555 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f1a07fc2-22ab-37e2-8fa1-f2b4f43dc00a | -2.1332 | -56.70321 | 2026-10-06 05:23:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 0a59204d-7940-314e-b805-22ceb61c0e5d | 3.06082 | -60.59756 | 2026-10-06 05:23:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ff6fd7f2-0768-3f47-9d65-949dd9596482 | -2.93709 | -54.11166 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 17af07fb-4345-31cc-bfb3-8764332a6e70 | -3.33342 | -50.05324 | 2026-10-06 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 187f934b-ecc3-351f-80a7-fafdf77c30b0 | -2.95353 | -54.14462 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c362c2d-2def-3bc3-9d86-dfec38a07ad5 | -3.04765 | -54.21038 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ea393ba-143f-3225-9c71-ae2e00da040a | -8.59545 | -66.80977 | 2026-10-06 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 844cb056-2068-32d7-95df-f89134503208 | -3.0469 | -54.21572 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3214c877-d350-30fd-8bc2-39ea87a0c190 | -3.57496 | -53.1298 | 2026-10-06 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c94323e-04d2-32a6-a926-1983144d0a10 | -8.7446 | -64.19149 | 2026-10-06 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3eecca11-c19e-34dd-a7a1-330b4905e893 | -2.88383 | -54.14794 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b448d66-26f0-3a67-be84-39dfdeb6d89a | -3.12623 | -53.75713 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e7de742e-c7ed-31ab-b6ab-025b1619cb8c | -3.0216 | -53.89052 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 4c939df3-cd02-348b-9c57-b813fcd4e2ff | -6.48301 | -62.86106 | 2026-10-06 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 483670af-1379-3705-b0fc-63db477821be | -3.06843 | -54.24555 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 32204aa9-af85-3415-9d66-612c5260c10a | -2.98546 | -54.10496 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5e8a261-d0ae-37f7-b7fd-4ff1abfcc5fe | -3.11149 | -53.70716 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb7660f1-0d91-3560-bb59-3cc8bc38e2c1 | -3.29759 | -59.39521 | 2026-10-06 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3fd91165-5432-3bdc-8c9c-81323d1fe815 | 3.12402 | -60.57663 | 2026-10-06 05:23:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6ac85c2-5f8c-3632-af50-4567a3970e47 | -2.93832 | -54.13211 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 674d3ad0-3c73-3ab3-94b7-40c056ff3cda | -3.0475 | -54.21179 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 185972cf-ded1-3cf8-b842-09fb609f670e | -4.27998 | -50.2725 | 2026-10-06 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4cc009b0-1533-398c-9b63-9a1a6f1ec506 | -3.00034 | -54.18003 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1dd22c6-ae05-3d04-9a86-1ecb63282380 | -2.95301 | -59.16078 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1fb65723-349f-3588-bdec-ae1e28001910 | 0.44326 | -60.53721 | 2026-10-06 05:23:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 44cf8381-1950-32e9-a327-3b9cefcfcd8a | -3.2422 | -58.54846 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cfe665b0-3429-3e99-92c2-68081a59c3fe | -3.32981 | -53.39074 | 2026-10-06 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 07f1cbf9-cbdc-3810-b819-597896c5e1d1 | -3.92696 | -55.4405 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b62e98c5-ab17-3696-afc4-9fb0f945f20d | -7.05363 | -59.23388 | 2026-10-06 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46f2c835-a53b-33c3-b178-73f4e5b51ce2 | -2.87902 | -54.1511 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 21473ca7-d75e-36c1-8cbf-8986791c3f74 | -3.11248 | -53.75935 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2dec9173-13d3-3f9b-9215-64f40b063b5f | -3.50865 | -54.62601 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3cca527c-f61e-3411-8a65-8dcf3ad543e9 | -3.21199 | -53.94577 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1f6eec7b-110a-30f0-abd2-78cac49db52e | -2.95488 | -54.16505 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cb59bca0-7435-3346-9470-01a9a1c9591c | -3.6752 | -55.94498 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 2169ecc5-2a34-3958-85a6-2cc54b0a9687 | -8.27748 | -62.86818 | 2026-10-06 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0534985d-3318-3e47-943a-492177bd0851 | -3.06389 | -54.16173 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 85982c14-54bf-37a5-b39f-a2fac1bc8bc9 | -3.0922 | -54.17277 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff0a502b-9d44-39ff-895a-717a3ec00cb9 | -3.95373 | -56.05386 | 2026-10-06 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6defc7c5-9837-3338-b2f4-d086659eb3db | -3.17347 | -58.63673 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b6708dda-0cc9-3e06-b61c-845d7748e3bb | -2.77795 | -54.10378 | 2026-10-06 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 99de3c0b-fb39-337f-ba91-e342168ad47d | -3.27714 | -54.18351 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 639e3f91-ada1-3aef-a99e-7b546ff3a20f | -3.5565 | -59.48174 | 2026-10-06 05:23:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eadd3963-8fec-39d8-b30a-82799d1cd5fb | -3.88439 | -55.79834 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a470273-39be-3700-83a1-c9c52e41f885 | -2.90286 | -54.02042 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e4f08a6-a9ae-376a-b9d8-3666274ad594 | -3.72282 | -55.46249 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2e9c8dac-54b7-3c56-a28c-9d5d2678ab93 | -3.84568 | -50.3182 | 2026-10-06 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83db4a8d-64fa-39d0-8617-2d1fdf4ab94d | -3.23522 | -53.87814 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b03cdd77-a496-3447-b99a-b3263bc551b3 | -3.07217 | -54.1614 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68921933-0469-3f09-86fb-71e45ef05f8a | -2.92617 | -54.12624 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fd9a1b19-86e7-357d-a6d8-bbdeefe2d5d5 | -2.78803 | -51.67347 | 2026-10-06 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 25b1ff9b-fc21-36b4-8a92-70f5c6ff3a69 | -3.27559 | -50.40335 | 2026-10-06 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ab1c65c-4de9-3460-9b47-6fcb1838e5ba | -2.77547 | -54.09128 | 2026-10-06 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a0631ecf-40f9-3bb1-95a0-df0b6ab1eaa4 | -3.23088 | -53.87746 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43fa916a-05bc-30b8-b01e-f80cdc85e5ee | -3.09822 | -53.73554 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7ddf4cd5-bc5d-38f1-a8ca-5ad83c1ee8f1 | -2.92253 | -54.12164 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e3f1f56a-99df-37df-a79e-c9b4704f643d | -3.32346 | -53.85323 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4aedc080-c342-33c2-9bcd-19d9038a743d | -3.05496 | -54.21959 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c23f4185-e32d-3916-bdaa-fc631879c612 | -3.0538 | -54.22749 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4a55b44f-112d-33b8-934d-494e44a389c9 | -3.5015 | -54.61723 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c6ccb60-dff5-3f75-b4f1-ffa5f1c49c2d | -2.78039 | -57.65429 | 2026-10-06 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8c21c2c6-9846-32dc-937c-d3820681f052 | -3.61637 | -55.50277 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88e007af-b078-3c33-a3a4-bd65bd822cd9 | -8.59834 | -67.19678 | 2026-10-06 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d8c078ea-f082-393e-9dc9-1b030f3fbb75 | -3.09341 | -54.16466 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0f617603-a417-35a3-bdf6-cd85410d50c9 | -2.95165 | -54.15839 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b4d88f9-9cbb-37d5-9e13-8af29ac965bf | -7.43841 | -63.56165 | 2026-10-06 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d31568c-c49d-3adb-9e35-6e75ee564964 | -2.91219 | -54.10372 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 373f95db-b944-35bb-9a82-260c9b274a11 | -4.33635 | -50.40163 | 2026-10-06 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| aec5fce4-45c9-3fe1-affa-384f6f9cb3b9 | -3.90611 | -52.16252 | 2026-10-06 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3b32838-3698-3197-8f23-e207d74f411b | -3.58246 | -54.31087 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 18a4fbb0-8da1-34c9-9c2e-83b3d28eba1a | -2.8717 | -54.14207 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e1e9d82c-305f-3ac7-b76a-235d8bf416b0 | -3.68976 | -55.95202 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 17b97162-dda2-3cd6-866d-9259dc1b32f3 | -3.06541 | -54.14826 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 6313fad7-4f92-3a5e-b188-ba2b7d4bccc5 | -3.24984 | -60.72655 | 2026-10-06 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 590663fb-09ee-329f-89e1-204bc4f926f1 | -2.04999 | -56.88605 | 2026-10-06 05:23:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README54.md)
