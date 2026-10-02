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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| edd906d3-8049-369e-9dbd-2add3ab30469 | -11.4691 | -43.4299 | 2026-10-02 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| d5179c19-5755-3d4c-8967-26d464c83737 | -10.8005 | -53.7682 | 2026-10-02 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 23330b97-b3c9-30a9-a4c6-609563e99c0a | -2.0394 | -56.8593 | 2026-10-02 02:50:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 43669297-76c3-3836-93cf-a8a95d029c85 | -3.1483 | -53.7426 | 2026-10-02 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 4656c7fe-fa91-3efc-aea3-df0010068ab4 | -6.2091 | -60.0187 | 2026-10-02 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| fdda2d78-1201-3f8b-b918-3d87851f78c5 | -10.8007 | -53.7476 | 2026-10-02 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 139.7 |
| 7d7bdd1e-b233-35da-be04-4bdf6491b3e9 | -6.209 | -60.0378 | 2026-10-02 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 155b2dea-8d74-34e5-9a24-9ec9a19840ec | -11.1615 | -44.6002 | 2026-10-02 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 6a19a20c-2c8e-3a68-b60e-58653e035613 | -7.4031 | -55.2114 | 2026-10-02 02:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| fd90c39e-b745-3559-9c0a-58d6b98c0f64 | -6.209 | -60.0378 | 2026-10-02 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| bbbe254e-5718-3ca8-85ff-ca9ddc2dc1bc | -11.6575 | -43.6136 | 2026-10-02 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 197.3 |
| 8f707ca5-88dc-39c6-89c9-5f818d2a2d0a | -2.0576 | -56.8786 | 2026-10-02 03:00:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 664f0ee1-7048-3fee-83f9-e1a928b64e99 | -4.4507 | -47.9112 | 2026-10-02 03:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 5a66458c-19c5-3be8-ad8d-ef84fd6337b6 | -10.8007 | -53.7476 | 2026-10-02 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 0a8c5b4a-7d06-352a-82b6-b65d9a2a6d25 | -11.3102 | -50.9187 | 2026-10-02 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 73c77b8c-dc62-3fd8-862c-3d70dcd78045 | -11.1611 | -44.6234 | 2026-10-02 03:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 4b8a4739-3db1-31f9-a7ce-1af58c4f25a3 | -7.0478 | -55.6302 | 2026-10-02 03:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 8bc82b4e-9cb2-3978-9a2d-267042c0442d | -4.2676 | -50.7506 | 2026-10-02 03:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| ac65a17e-048c-3cb3-99d4-826a443a9c1f | -2.0577 | -56.8591 | 2026-10-02 03:00:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 6634bbff-08fb-377b-8fe9-5441bf9b54d9 | -11.1424 | -44.6029 | 2026-10-02 03:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 72a43e33-aa36-3349-802b-26838cf0eb25 | -13.3481 | -43.8538 | 2026-10-02 03:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 59b1a3f3-b72b-3782-b877-b3722affb12e | -4.4693 | -47.9103 | 2026-10-02 03:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| a3ca74a4-8669-37df-b618-3256e1acbfd4 | -2.0394 | -56.8593 | 2026-10-02 03:00:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 4977b021-bd9b-37d4-a654-1cf23f003821 | -4.4506 | -47.9329 | 2026-10-02 03:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 6b24968a-a8ae-3e64-81be-851065ce0729 | -1.2739 | -54.5587 | 2026-10-02 03:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 957bc176-0c6c-3624-b550-6b13edf08927 | -3.1299 | -53.7431 | 2026-10-02 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 129.9 |
| 2aba2c94-a961-3439-95b9-9a0199da0a3a | -11.6771 | -43.587 | 2026-10-02 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 266.4 |
| 6288f5a7-f6a3-3ab1-a317-681dcd79f09d | -2.0393 | -56.8789 | 2026-10-02 03:00:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| fc46e254-fce2-3e71-adad-2fd1fc3371b3 | -3.295 | -53.8597 | 2026-10-02 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 49b61c40-ab02-37b2-adf9-19261805a38e | -11.6579 | -43.5899 | 2026-10-02 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 349.1 |
| 02946637-075f-328b-a18a-0defc5ee8972 | -3.2951 | -53.8395 | 2026-10-02 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 115.3 |
| b02e21e6-a00a-3c82-83ef-8891c9934551 | -6.3952 | -56.4158 | 2026-10-02 03:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| ba1ec665-2af8-3b42-83e5-8e595a864fdd | -3.1483 | -53.7426 | 2026-10-02 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 04073d12-9717-3e55-ab59-293acfe91a4a | -11.4691 | -43.4299 | 2026-10-02 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| c5d435ba-2de7-3170-9d3e-520eb3a6d851 | -3.2767 | -53.84 | 2026-10-02 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| e890c2e2-b462-34b6-aa15-25e188073eb7 | -3.1655 | -54.0844 | 2026-10-02 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| f29d1da0-f72f-3532-905f-ce709c0c9117 | -10.7818 | -53.7493 | 2026-10-02 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 148.2 |
| 0df1fd3a-4afb-33b4-857b-1789cd162a7c | -7.4031 | -55.2114 | 2026-10-02 03:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| b5f9b241-4c2f-38e7-af16-c177a4758357 | -10.7816 | -53.7699 | 2026-10-02 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 560aa08e-3bdc-35cd-996c-efc1dd1292bb | -3.1839 | -54.0839 | 2026-10-02 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 89e246ac-7a95-3de5-bbc6-512669a14600 | -3.1299 | -53.7633 | 2026-10-02 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| c61e50ed-b26f-3d54-84e8-c5620c0d1195 | -11.1615 | -44.6002 | 2026-10-02 03:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 886b1da4-9a23-3397-8c73-f21fd927751d | -5.7563 | -45.152 | 2026-10-02 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| b51100c8-be9c-375c-b920-182a67eceb2b | -11.142 | -44.6261 | 2026-10-02 03:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 0eee72a8-d6f2-3493-90fe-17e95680db60 | -11.6767 | -43.6106 | 2026-10-02 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 209.8 |
| c4dc5d01-ae57-3fb8-a865-5121a574ef7f | -6.2091 | -60.0187 | 2026-10-02 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 0da43120-8401-30b0-9457-fce0fee19657 | -3.1838 | -54.104 | 2026-10-02 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 576d45d3-d3fb-30a3-bbc5-a6656715bfe3 | -10.8005 | -53.7682 | 2026-10-02 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| ad805a9f-6c81-3ef3-b6c3-93ca948342a1 | -11.6579 | -43.5899 | 2026-10-02 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 128.4 |
| a2436171-2562-3d9a-9644-bba47d9a4f02 | -11.6767 | -43.6106 | 2026-10-02 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| a256ad12-f952-32f3-b61a-22ae8d40bc55 | -1.2739 | -54.5587 | 2026-10-02 03:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| ad5eeda3-1667-356e-a3dc-09a6354167a4 | -7.0478 | -55.6302 | 2026-10-02 03:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| dad16d5c-d8ca-3e21-8deb-bd4712de0b22 | -2.0393 | -56.8789 | 2026-10-02 03:10:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| aa3b9dfb-652e-3349-b71e-f90629052cfe | -11.4691 | -43.4299 | 2026-10-02 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| efb7d84f-8e65-3b32-82c5-ce0e78ae4730 | -10.7818 | -53.7493 | 2026-10-02 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 76c3b6d0-6d85-3257-8166-a2bc30a81ac2 | -11.1615 | -44.6002 | 2026-10-02 03:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 6048e856-811c-38c0-a797-e195f06a3684 | -1.2556 | -54.5589 | 2026-10-02 03:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 80bc1ba4-51dc-3238-a26e-6ddcce913988 | -7.4031 | -55.2114 | 2026-10-02 03:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 150.6 |
| df7a5990-aca1-38be-9e12-5090b14fe302 | -3.1299 | -53.7633 | 2026-10-02 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| f5734405-9aba-396e-8dbd-b0495eb82ca3 | -3.1483 | -53.7426 | 2026-10-02 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| adaa521a-46ff-3cf2-94d3-31bbc295a021 | -4.4507 | -47.9112 | 2026-10-02 03:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 15bdee96-e530-3c69-a671-adf4b666de52 | -4.2676 | -50.7506 | 2026-10-02 03:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 7b24e554-daac-340c-8aff-08bd038d40d8 | -11.7926 | -43.5689 | 2026-10-02 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| aa944b09-4309-3dfc-aed5-70aca7872700 | -11.7348 | -43.578 | 2026-10-02 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.9 |
| e6035a14-a00b-34d1-a429-4cf18120bfcc | -6.3952 | -56.4158 | 2026-10-02 03:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| f08d1d12-eb12-309d-ac3e-a7498afefa56 | -11.1611 | -44.6234 | 2026-10-02 03:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| c197b9fe-5704-3e9f-8c0f-7f6c28928e30 | -4.4506 | -47.9329 | 2026-10-02 03:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| efee9645-c906-351f-84c5-bfdec8f3634e | -11.7541 | -43.5749 | 2026-10-02 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 209.7 |
| a26fa130-56e1-3959-b912-4188864a3399 | -2.0394 | -56.8593 | 2026-10-02 03:10:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| d0e92315-875b-3518-a931-24c183d8edaf | -3.1838 | -54.104 | 2026-10-02 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 92610380-06e1-3265-a835-9ec2113f4f4d | -5.7563 | -45.152 | 2026-10-02 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 4e507876-e2b6-35f8-9f48-6dce36e3b6fe | -11.142 | -44.6261 | 2026-10-02 03:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 5231eaf8-57e1-33d3-9bc7-c05ed9d07287 | -2.0577 | -56.8591 | 2026-10-02 03:10:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 584f64eb-9488-3438-b0e8-c3b052539c2f | -11.1424 | -44.6029 | 2026-10-02 03:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| cf160d51-e142-39d0-acea-1da0e06325de | -12.9995 | -51.2976 | 2026-10-02 03:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 5aebc6bc-c7cf-33ea-a044-44e8c88a037c | -11.7733 | -43.5719 | 2026-10-02 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 03a9f5a3-dcb4-3df7-b9ac-d799e4fe6e85 | -6.914 | -43.6816 | 2026-10-02 03:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 565e1d2f-c969-31ea-a3dc-2119d55aee38 | -3.2951 | -53.8395 | 2026-10-02 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| e2981338-c3d7-347f-92dc-2a7ec84ff055 | -10.8007 | -53.7476 | 2026-10-02 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 5cc24234-bba7-3be2-96b8-2e6627db6eec | -10.7816 | -53.7699 | 2026-10-02 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| eab6b7ee-0c50-3560-844e-ed834664fd78 | -3.1655 | -54.0844 | 2026-10-02 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| babfc250-aa81-31da-9c1e-667986e10fae | -2.0576 | -56.8786 | 2026-10-02 03:10:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| b7b59965-de57-3daf-8b3d-a67e02c6fa7e | -3.1839 | -54.0839 | 2026-10-02 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 9557735c-c3b4-30b4-9966-5ae4983a91ce | -3.1299 | -53.7431 | 2026-10-02 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 119.4 |
| ce9d2710-5c89-306c-ade7-02fcb7ead9a9 | -11.7545 | -43.5512 | 2026-10-02 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 1179d603-10dc-363d-9a27-559246caee40 | -11.6771 | -43.587 | 2026-10-02 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.3 |
| b65cfbaf-1f60-3bb4-b069-c5fbbbb874e7 | -11.6575 | -43.6136 | 2026-10-02 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 873fe9de-add4-34e5-8a53-4091455c1587 | -12.9998 | -51.2763 | 2026-10-02 03:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| f6008677-7a1e-3605-bf19-f4bb036ce245 | 1.8221 | -55.5654 | 2026-10-02 03:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 5a27cec7-f1fe-340c-8c9e-937db0017b4d | -7.3846 | -55.2124 | 2026-10-02 03:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| cc108a24-c4df-3d73-af22-aa9f80037bbc | -7.4188 | -55.5902 | 2026-10-02 03:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 31e0eeb9-25f2-3a96-9c89-b713baf6edec | -7.2704 | -55.5983 | 2026-10-02 03:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 590bdb0f-fe7a-32e0-a2fb-cb9f7ca63555 | -11.77 | -43.57 | 2026-10-02 03:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 09e47d08-995d-3f48-8646-9172cf7aac14 | -11.66 | -43.58 | 2026-10-02 03:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b1fb0172-4a70-37d4-8885-ed0510d33057 | -11.66 | -43.63 | 2026-10-02 03:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 242f4b92-96a9-37a9-abc1-aa04053a4044 | -11.74 | -43.6 | 2026-10-02 03:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 041b83cf-d9f9-3903-b313-512d5edc3af2 | -11.69 | -43.64 | 2026-10-02 03:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f6d30f08-f2a2-3c96-8a59-2fef527c7369 | -11.69 | -43.59 | 2026-10-02 03:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1098e1df-47ff-3d77-8b15-433216c5a9c0 | -11.74 | -43.56 | 2026-10-02 03:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aa834fe0-82ab-3915-b354-703ba0f41494 | -11.77 | -43.61 | 2026-10-02 03:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README22.md)
