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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62540901-6850-3dfb-8903-a83910c83a3c | -12.8552 | -44.3389 | 2026-09-10 10:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 6639d9ea-7a50-3321-8fe9-bb3d1891a20d | -12.8359 | -44.3422 | 2026-09-10 10:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 159c4fca-637a-3601-9c1b-20671c55a988 | -10.6621 | -45.9974 | 2026-09-10 10:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| d05a22cf-f65d-373f-b393-e279dc623a2e | -12.8552 | -44.3389 | 2026-09-10 10:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| fa5a016b-edb3-3a85-97e9-599df7ae823b | -10.6621 | -45.9974 | 2026-09-10 11:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.8 |
| fa59f77b-86c7-305a-886d-ac8b0f99fed8 | -10.6618 | -46.0201 | 2026-09-10 11:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 135.4 |
| be525acc-6074-3cbe-95bd-62c2322a0770 | -12.8552 | -44.3389 | 2026-09-10 11:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 94.6 |
| e99229f9-e90f-31d3-bca0-15e9c50c193b | -12.8359 | -44.3422 | 2026-09-10 11:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 118.1 |
| dfe97354-79ec-305e-b40f-0859845c4d7b | -10.6808 | -46.0177 | 2026-09-10 11:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| b7ba68e9-d645-34da-a520-5347977a8483 | -12.8552 | -44.3389 | 2026-09-10 11:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 11f2febf-dcdc-342c-9c96-97afb7f2509c | -12.8359 | -44.3422 | 2026-09-10 11:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 6470f777-651c-305b-b5e1-d74097ee5aad | -12.8552 | -44.3389 | 2026-09-10 11:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 98.0 |
| a9f119b1-fce7-3275-a210-a7042079cd5c | -12.8359 | -44.3422 | 2026-09-10 11:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 12c216b6-6e5f-3079-8b10-bffc919a1777 | -12.8359 | -44.3422 | 2026-09-10 11:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 145.0 |
| bac0501d-fdfe-3bc0-989b-0f59994e8594 | -12.8552 | -44.3389 | 2026-09-10 11:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 8875ac3f-0801-3795-8fef-1b4327d65a1a | -12.8552 | -44.3389 | 2026-09-10 11:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| aecf42e6-6778-3498-a52d-27473efdbbc4 | -12.8359 | -44.3422 | 2026-09-10 11:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 139.6 |
| c30a9841-602d-343a-aa76-b3f6d7759c49 | -12.8359 | -44.3422 | 2026-09-10 11:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 151.9 |
| 8a61d7e6-6de8-3fcd-9b00-8590627a5a3f | -7.587 | -45.6804 | 2026-09-10 11:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| d1940b56-d405-3d5c-babf-259c5ed272d4 | -12.8552 | -44.3389 | 2026-09-10 11:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 5c68a457-0829-30a5-83b0-37b5f79c784c | -10.5501 | -47.1126 | 2026-09-10 12:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| ade26a8c-e479-31dd-b2ef-aab15ef6b8c1 | -12.8363 | -44.3186 | 2026-09-10 12:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 539d2f89-4e66-365a-81db-bbb9e475d471 | -7.587 | -45.6804 | 2026-09-10 12:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 142.0 |
| d3e1c42a-dd55-360d-9ed3-dab62401248b | -12.8552 | -44.3389 | 2026-09-10 12:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| a9234407-876d-38cd-92bd-1ef94aca7a25 | -12.8359 | -44.3422 | 2026-09-10 12:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 142.5 |
| e832572e-8e9d-394d-8e45-c602b032caf2 | 2.17666 | -50.89561 | 2026-09-10 12:04:00 | TERRA_M-T | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 5672119e-3bf9-3f8c-b603-b9c0f05193ee | 2.22868 | -50.73944 | 2026-09-10 12:04:00 | TERRA_M-T | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 576c8efc-e017-3a3a-bbb2-8253727a58dd | 2.17791 | -50.90436 | 2026-09-10 12:04:00 | TERRA_M-T | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 7d5c05d0-2de9-33dd-9fb0-c8d5303fa352 | 1.51685 | -50.92331 | 2026-09-10 12:04:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 30112612-4434-34e3-b9df-1f6c0cc0745d | 1.36293 | -50.68171 | 2026-09-10 12:04:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 48b6bca5-4c70-3dc7-826e-e312831115ce | 1.79568 | -50.81223 | 2026-09-10 12:04:00 | TERRA_M-T | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 12f86beb-9ef3-3b75-b884-52046ad80397 | 1.25828 | -50.72064 | 2026-09-10 12:04:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| fad059dc-57c8-3e90-985f-265a2900f803 | 2.22743 | -50.73067 | 2026-09-10 12:04:00 | TERRA_M-T | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 10.2 |
| f2f774c5-97cb-341d-a901-dafca54ee3f5 | -5.77574 | -45.08083 | 2026-09-10 12:06:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 48770047-bf92-3fcf-9514-169237152238 | -6.77514 | -45.02076 | 2026-09-10 12:06:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 53217bef-93cd-38db-80da-b5bea3e4e412 | -6.772 | -45.04678 | 2026-09-10 12:06:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 157.1 |
| dea827b7-c39f-3f70-9029-65cdb373c97c | -6.16685 | -44.65159 | 2026-09-10 12:06:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 32.4 |
| d7b4206c-fa95-3160-8122-36ddf144a564 | 0.23536 | -51.45188 | 2026-09-10 12:06:00 | TERRA_M-T | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 0ba47d7e-6d30-3b17-80c5-6e8f7856226e | -7.50331 | -45.26426 | 2026-09-10 12:06:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| d42852dd-81c4-3a69-b227-124323aeea85 | -2.11903 | -54.37474 | 2026-09-10 12:06:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1ffad0e2-9f09-3d42-868d-3f1e957592c3 | -2.9386 | -50.46779 | 2026-09-10 12:06:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 2224728a-bb7d-3495-bf38-b42d882c012b | -6.1703 | -44.62459 | 2026-09-10 12:06:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| d4162324-698a-330d-8f42-345f80211ae9 | -3.37951 | -59.41093 | 2026-09-10 12:06:00 | TERRA_M-T | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 64f81664-dcd4-36ad-8cb3-108a93d7ba85 | -5.76161 | -45.07871 | 2026-09-10 12:06:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 36efaf59-b8a4-3f6a-a01d-10909a041a81 | -5.7658 | -45.08474 | 2026-09-10 12:06:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 4d2a6af8-c9db-3773-a6a2-ec023dce8d56 | -2.11753 | -54.385 | 2026-09-10 12:06:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5e41fddf-88b8-3148-9dd9-9447a46b7507 | -6.77333 | -45.01361 | 2026-09-10 12:06:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 8e261b9e-f372-3129-b834-657b90a6381f | -2.18673 | -54.4749 | 2026-09-10 12:06:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f6603f82-e059-3438-96d6-1e11d0fb5732 | -6.76998 | -45.03983 | 2026-09-10 12:06:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 275.7 |
| 5e67bdfe-1075-3cca-8821-edb762f54230 | -7.49728 | -45.28246 | 2026-09-10 12:06:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| d87c0ff0-a6b5-3388-95e8-999244cdc509 | -3.26934 | -50.0891 | 2026-09-10 12:06:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 11acb7d4-8f52-3c38-93e7-dbb917582eeb | -2.93726 | -50.4772 | 2026-09-10 12:06:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 54214ea2-4a6d-3ceb-903a-cfe93d169404 | 0.23661 | -51.46062 | 2026-09-10 12:06:00 | TERRA_M-T | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 5ec4c4ce-2a70-346b-912a-4c109f65565d | -1.7051 | -55.02815 | 2026-09-10 12:06:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 681a2b94-aef7-3e67-b54a-ebab2798f606 | -3.27075 | -50.07924 | 2026-09-10 12:06:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| df623b5e-7972-3745-8457-518eb4169a44 | -7.50051 | -45.25741 | 2026-09-10 12:06:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 00a03f42-9c70-3324-8143-e76b94b9240b | -7.58585 | -45.68176 | 2026-09-10 12:06:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 4f2b85f4-bec8-3662-b5c3-4576b5c8846d | -3.24694 | -47.25407 | 2026-09-10 12:06:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 2d07b131-3acb-3c37-b845-2b482295b78f | -9.33712 | -45.63655 | 2026-09-10 12:08:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 5c9c2cda-6b5d-307b-a211-fb36bf3e1924 | -12.497 | -45.27077 | 2026-09-10 12:08:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 76f345e8-2db3-3f29-ab90-3d5c3fe20ba8 | -12.50073 | -45.26593 | 2026-09-10 12:08:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 2a7aca5a-80f6-3c04-8ef2-aad7b37d8220 | -8.99201 | -44.98555 | 2026-09-10 12:08:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 845ff700-831c-3d0d-9060-7d3afee33659 | -6.77954 | -58.88408 | 2026-09-10 12:08:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.5 |
| a4e8de46-843f-3c26-8439-6dd083ff5dce | -10.67431 | -45.99067 | 2026-09-10 12:08:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 37b809dd-4093-3112-8bbf-fe480efccf67 | -13.51938 | -50.95342 | 2026-09-10 12:08:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| e7edf628-def7-316b-b16a-abb146361815 | -13.52093 | -50.9415 | 2026-09-10 12:08:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| b723ae86-0b29-347b-ac4f-a941860422dc | -10.55142 | -47.10307 | 2026-09-10 12:08:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 368e5c3d-8380-3e9b-8e3b-15eea42505e3 | -6.79188 | -58.88592 | 2026-09-10 12:08:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 8a6396ce-8d09-3e95-a4e9-65ecadf59221 | -9.34034 | -45.64236 | 2026-09-10 12:08:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 42.0 |
| eeb9642d-5de1-3b6e-a8cb-dd650d22ea3d | -9.78638 | -47.06386 | 2026-09-10 12:08:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 30c71895-1be9-3a52-b752-50937cc9d71e | -14.57171 | -43.83958 | 2026-09-10 12:08:00 | TERRA_M-T | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 40.3 |
| e6fc3579-f5a4-3085-9a77-9b9e245e4b01 | -6.82705 | -58.98553 | 2026-09-10 12:08:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 7c4c1974-5213-3c6e-b81e-2213a1cd19cf | -10.72954 | -45.92565 | 2026-09-10 12:08:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 34.7 |
| a8b12dc7-1d64-38f6-ba2e-88664a572267 | -10.54961 | -47.1096 | 2026-09-10 12:08:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 70a20626-7f1a-39a2-b7f2-84cc082e7572 | -12.84838 | -44.33633 | 2026-09-10 12:08:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 669c9de3-8e94-3fe0-8ad0-727657ae2e8b | -6.76789 | -58.95739 | 2026-09-10 12:08:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| b4ad219f-6d9a-381c-b3f0-1669108b30b9 | -12.84339 | -44.32883 | 2026-09-10 12:08:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 161.2 |
| 49f6b126-6aea-3505-b7d6-5cc47ca580b7 | -13.43727 | -43.82663 | 2026-09-10 12:08:00 | TERRA_M-T | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| c73bbb9b-2062-369d-ac31-57bb367fdf03 | -9.60423 | -46.75275 | 2026-09-10 12:08:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 76056e69-e534-3362-b38e-f81c5c3d2cfd | -8.82497 | -46.92624 | 2026-09-10 12:08:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 4999b1c4-224a-37df-86fb-5563897a730f | -8.99068 | -44.99177 | 2026-09-10 12:08:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 37.5 |
| c815ed3c-7fc1-383f-b5a8-c922cb9eca3b | -11.33914 | -45.7721 | 2026-09-10 12:08:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 32fc708f-034c-39ec-8d0f-b5d11da03c87 | -11.81078 | -52.51445 | 2026-09-10 12:08:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2ae408c4-3ba2-3ebd-9dc5-0070e67e6445 | -6.78899 | -58.90418 | 2026-09-10 12:08:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 0b83fd15-b307-34ab-b100-2235d507df28 | -9.77347 | -47.06256 | 2026-09-10 12:08:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 57c211cf-5c65-33df-aacd-449a2785b6e3 | -6.77155 | -59.43128 | 2026-09-10 12:08:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.0 |
| ffd28094-c8ea-371a-80fe-a32a85340d67 | -11.3346 | -45.7934 | 2026-09-10 12:08:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| a4fef2e6-4d97-3fb2-badf-331fa3190d04 | -10.39681 | -46.54861 | 2026-09-10 12:08:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 38dec36d-2fd9-335b-88f6-70fd0b8c7eef | -6.76577 | -58.95096 | 2026-09-10 12:08:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 694d53cd-07cf-3e33-9cca-77ae72f5002d | -12.83945 | -44.36561 | 2026-09-10 12:08:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.0 |
| a2a939f9-b569-3b1c-82a5-fa7db1f02336 | -13.43843 | -43.83328 | 2026-09-10 12:08:00 | TERRA_M-T | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 44275546-6454-348a-852c-722fbdcc5d18 | -12.50031 | -45.23964 | 2026-09-10 12:08:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 30.7 |
| a6423cf4-84e5-339f-b262-769ecb8d5676 | -12.83171 | -44.33445 | 2026-09-10 12:08:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 170.5 |
| 8d351332-8760-3535-a282-f143d852ec55 | -9.78886 | -47.04377 | 2026-09-10 12:08:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 35a039e7-0eaa-328f-82d1-1fcb4f8715ed | -12.86008 | -44.33042 | 2026-09-10 12:08:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 75f1710c-a96e-3e56-ba8e-e5c271154cc8 | -6.78645 | -58.89775 | 2026-09-10 12:08:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.4 |
| aa83fa90-9775-3661-9c64-63bda1989b2e | -8.82528 | -46.92098 | 2026-09-10 12:08:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 60aa5dfd-2765-3119-b0db-c6769e2a47e8 | -12.8359 | -44.3422 | 2026-09-10 12:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 034e6288-c251-31ae-b44a-cdb53a934ae5 | -7.587 | -45.6804 | 2026-09-10 12:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| d684b759-186f-35f4-a01b-1879b1dbec44 | -7.4979 | -45.2587 | 2026-09-10 12:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |


[Clique aqui para ver as próximas entradas](README47.md)
