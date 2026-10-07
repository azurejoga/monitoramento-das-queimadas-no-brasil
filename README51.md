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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60d73ea2-ee43-383a-a3a6-6963235c5407 | -3.2797 | -50.14748 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 806e9a81-32aa-3533-b10a-d238b5570253 | -3.27878 | -54.01262 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6ea64364-daf1-3ecf-a746-b85b63329daf | -5.59021 | -47.27885 | 2026-10-07 04:19:00 | NOAA-20 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dc90a750-765a-34f3-a670-c213f88a87ee | -7.81733 | -46.86251 | 2026-10-07 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec2282d6-6f52-3632-95c5-dba42e96a4cc | -3.10577 | -54.17515 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f06b7ac1-234f-3e0b-8d00-9a3236c042eb | -3.52429 | -54.64674 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c47d42ce-8902-3db0-8af1-779ed337d32e | -5.58639 | -47.27825 | 2026-10-07 04:19:00 | NOAA-20 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d1bf2237-3603-34e4-8578-f9b2ea5861ac | -3.47703 | -50.08287 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 82bca4de-9ed6-39c7-b262-536079c539de | -4.24969 | -51.05024 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f836b589-6b48-3524-aa12-2012dd3a9348 | -3.5013 | -54.63372 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d9c50876-2f56-353b-8f75-b89bcc143d62 | -3.5596 | -54.48972 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92000e27-df53-3d51-8e07-18f78c4cd673 | -5.57488 | -48.98726 | 2026-10-07 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 423f105f-67e2-3b3f-91d1-1e916e5c8dc8 | -4.02664 | -42.47698 | 2026-10-07 04:19:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 22c2ca5e-bd55-3aee-8aac-35b99245f9e4 | -7.86669 | -44.16274 | 2026-10-07 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a22ee56-bd39-3177-89af-649775e4dbb2 | -7.82024 | -46.86736 | 2026-10-07 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ac2362a-e9ba-36d0-8b88-3376a15f6e84 | -7.76021 | -43.80675 | 2026-10-07 04:19:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 43a3da9c-2957-3e65-98a3-5148498236ab | -4.15651 | -55.15893 | 2026-10-07 04:19:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 99d76250-5cbc-3d5b-9a5e-7b0442f5332c | -6.87887 | -43.68719 | 2026-10-07 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10f14c0e-1f12-3320-890d-af5a059c087b | -2.58025 | -48.20272 | 2026-10-07 04:19:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf53b994-bb3d-3cab-8a1f-34aa30c8487e | -6.58419 | -53.03614 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17178296-664e-35e2-b679-fc166b79583d | -3.27918 | -54.07614 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| eadff615-b4d1-34f8-b43a-541a0374f448 | -4.08379 | -48.90747 | 2026-10-07 04:19:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d9bbeaa-7cc0-3942-8b2e-39e6215dbb6e | -7.46053 | -42.99468 | 2026-10-07 04:19:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bd61cfd7-dd89-38f8-8157-0b20403087b1 | -2.77308 | -54.09377 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| af7220c4-9d71-3cb4-9820-d6db112dda5f | -3.49675 | -54.65345 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1896ba33-f3bc-3df8-8710-8ce8cf03f988 | -3.83731 | -50.30976 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bba9c98f-0b5e-3796-a778-64890298ce3c | -3.53718 | -50.10348 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1cd99184-9f40-3954-9e81-6e5b43b87b5b | -2.75969 | -54.09661 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| eef1cf63-1c10-31fa-bb7a-af6eb15eee6f | -3.49047 | -50.09019 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a8d08ee-9717-3235-936b-dafeeffbcb03 | -3.50304 | -54.66109 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 22359d61-bafa-34e4-896f-08e43cfb467b | -7.40821 | -44.45564 | 2026-10-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1622554-9abd-39a1-8c9b-1ee0bb1c02c3 | -3.06039 | -54.21336 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fded55e5-3430-3a2c-8557-f219f98fae6c | -3.12223 | -53.71052 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 56334db3-7dad-3711-8a72-68d32369db56 | -8.19872 | -46.35474 | 2026-10-07 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bab80cf9-d956-3c66-82ce-ab21e9fd114c | -2.67066 | -49.13426 | 2026-10-07 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8606d3ff-8848-385f-b46c-223ab56eb803 | -3.03641 | -53.91849 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0759cced-92f8-3549-9850-db62ae08433a | -3.21803 | -53.89002 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b8da2e54-8da6-3836-9291-891e6abce6ed | -7.40877 | -44.45213 | 2026-10-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7594a443-e628-3df5-900b-4457847b928a | -3.0713 | -54.2433 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 802819a1-daaa-389c-b8f6-23f89ae4cf37 | -3.99263 | -56.25237 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6fcdc4f8-dc1e-3bc1-902d-93a33dd9b935 | -3.20815 | -53.87357 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9fa49a08-3cf9-3d75-bc10-1f6d66c1049d | -5.67231 | -53.50222 | 2026-10-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a821ec5d-9f9c-3400-9952-4d4490c06e7b | -6.37433 | -42.53798 | 2026-10-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b6a8a7d6-3b8a-3589-9d28-6af10559210e | -7.10711 | -42.54143 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8fa48aad-7309-3c8b-a9b2-07955c75e429 | -6.21692 | -52.83701 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6795d2b-85ac-351d-82c6-db8f9c882d61 | -2.76982 | -54.09166 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| c0ed6827-bb9a-3450-838f-f22335ec4f63 | -4.28928 | -50.7817 | 2026-10-07 04:19:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b76c9c60-5007-344f-9642-60f5c812e55c | -4.93736 | -45.66555 | 2026-10-07 04:19:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3c2443c-541e-3d56-b326-3a57c0c762e7 | -3.59251 | -54.56384 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2489b8fd-94b8-3dcd-b022-7818dea0caf6 | -2.96939 | -54.13728 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2ca02cd8-c54e-3565-a7ed-870778343919 | -4.55569 | -49.34794 | 2026-10-07 04:19:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c93e836b-6a8f-3639-a3e7-343ef75840a5 | -4.04033 | -50.98353 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dab6678a-a30e-3c36-b631-6feaf9dde89d | -1.50661 | -54.83833 | 2026-10-07 04:19:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eae8ce06-26cd-345e-8ef2-f6c4e37c578f | -3.055 | -54.14772 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fc94508d-c364-31a2-beb2-9020ebce26d1 | -2.98976 | -54.05344 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2aa10505-30d9-3d0a-b89b-d5ee62258735 | -6.91967 | -43.66529 | 2026-10-07 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 86a552d3-69ae-340e-80b2-e3d803a446b8 | -6.99096 | -43.21551 | 2026-10-07 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| edeb5a75-df85-3fba-9bda-30da828b8647 | -5.67302 | -53.49832 | 2026-10-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72b5859b-e511-3aeb-be50-ba0c92477180 | -7.99313 | -45.49701 | 2026-10-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8932c106-819b-3e5a-9b74-a06f0e37f124 | -3.80935 | -47.49997 | 2026-10-07 04:19:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2617674b-c83d-3af0-a2bb-2d077ab8ba16 | -6.4019 | -52.71948 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec15ff71-33a8-3fa3-8d53-1515ef0968a5 | -3.27583 | -50.41452 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bec463fa-03a2-3c36-acec-5aebe3b37094 | -4.18875 | -51.13855 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c5c8b49-3dfc-3abc-81b3-c2078e8a82da | -3.03352 | -53.89836 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46298a82-f15e-320c-a327-c4ef0bf15268 | -5.39986 | -45.65153 | 2026-10-07 04:19:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af0693cb-ebd7-3dd4-8ed0-2ae1d6af3bac | -3.1907 | -50.56421 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| f4c9e3c2-9143-38b1-83cb-f6aca3a23254 | -4.25059 | -51.04713 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e23bdddc-afeb-3d68-b2ac-5f61dd219e62 | -4.83617 | -48.20277 | 2026-10-07 04:19:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5797697-6604-3301-98c0-a2fb16451f52 | -3.13868 | -51.03373 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43b8b5fd-4308-3afb-8c28-d698ad1bb1a4 | -6.37934 | -42.54945 | 2026-10-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0859e294-471e-3f7a-863a-b6462dd96713 | -3.98404 | -56.22863 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33d70c6e-0109-35d6-8fdc-713a31628f2b | -3.09952 | -54.17397 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| abc2c33a-6499-39b3-bf4f-b37ba3627916 | -3.30435 | -42.27539 | 2026-10-07 04:19:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d22cb170-33e6-3e0e-ae47-badaf5b290f1 | -2.75882 | -54.10162 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 347745d7-ce30-3a45-9413-4024a688c635 | -3.6031 | -50.98296 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2d157b7d-59ff-3c28-bcaf-e16c4dabdfda | -3.80926 | -51.03951 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85b9675f-8ba3-3705-82e7-ff6f924b09a4 | -3.0688 | -54.18077 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b46fd57-1889-39a7-a9d9-0c49f10dbd22 | -2.41035 | -51.30417 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fcac5e44-ffbb-3463-8e9d-3f84a5a07ad7 | -4.25012 | -51.04998 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f880126d-69dc-3262-a595-465b8e3f368f | -3.2903 | -54.01979 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 13738444-2d0e-317f-8204-0e0317cf7f19 | -6.56931 | -46.192 | 2026-10-07 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8e2e703-1004-3e96-8993-7ec32262c781 | -3.53696 | -54.65606 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 2fab6ac8-0e12-3df7-9752-ddc0458a11d4 | -1.56798 | -47.74157 | 2026-10-07 04:19:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 474ea0cb-a63b-3fc4-b9fe-8cedfeda1cf4 | -1.81432 | -47.84995 | 2026-10-07 04:19:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fbd9399f-1b0b-3ab3-ad73-e9cc23fd23d2 | -3.53801 | -50.09835 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1959037-642c-302a-bbe9-0bb8fb9cabd8 | -2.76962 | -54.11384 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 50a8bfd4-1ad6-3bc2-92df-95d33ed21a55 | -3.47618 | -50.08794 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d2ee9ba6-74d0-372f-b1c9-c664d31ef3d5 | -6.21211 | -52.83237 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d1b164c-65de-3be5-bde8-365dab1410fc | -3.29485 | -54.03054 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 430e4c3d-51ae-3a75-a2bd-8900d8c727cf | -3.29332 | -54.06843 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 0d38541a-002e-358b-b3a2-178e569a292b | -2.87087 | -54.20366 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4069b9cd-dd04-3cb7-a4ad-d744ecda616e | -2.93367 | -54.1198 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a4ede6e-fba0-3103-9c2e-d012e7b4bbed | -3.08136 | -54.27927 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a1475498-8696-3aa9-8852-42c0a66d5566 | -6.56152 | -46.03817 | 2026-10-07 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79b482f1-a360-3094-aade-4ed0c57d2aa9 | -3.02122 | -53.89611 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b66e9cc8-2cfc-37e9-800a-e593cc749c25 | -5.99429 | -53.50716 | 2026-10-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 77ea8676-2912-367f-aef5-51d204a144ba | -7.83627 | -44.18289 | 2026-10-07 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8667457-303d-3dd3-8c24-9d44dd28dd72 | -2.96473 | -40.39031 | 2026-10-07 04:19:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 876214fb-0359-373a-8062-7a8ed1c45677 | -3.52421 | -54.65343 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 70aef60b-5cea-3332-b102-05548b9f64e7 | -3.0209 | -53.90418 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README52.md)
