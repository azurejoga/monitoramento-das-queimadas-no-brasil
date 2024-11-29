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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a0c3a11-e96e-3470-9f29-c76dae89e1c0 | -2.03436 | -53.49815 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 31451428-47ba-3740-9c65-a19a9c067b1c | -3.79343 | -51.25671 | 2024-11-29 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a3f21db-89e9-30e1-8d1a-7c4b42fab96e | -4.07303 | -54.56508 | 2024-11-29 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23d24abd-be6b-3fe9-b3e6-631268721153 | -1.91357 | -52.88878 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 808b7122-1e33-3ec4-8e14-c2b116ad9ac6 | -3.03686 | -54.03623 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5bad3684-a336-3e53-82df-98176dae0c97 | -3.10086 | -54.04075 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 313b7de6-a782-3683-8c69-4ae2bfc8200a | -8.12573 | -47.99133 | 2024-11-29 05:22:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 408e9437-5270-3b1f-afb5-e8f084faebdf | -1.30014 | -55.74209 | 2024-11-29 05:22:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 094a8231-8785-3416-9fc9-32e6ccae92bc | -2.80194 | -53.04688 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92e26bce-d593-3996-8c59-f45e59cbc3af | -1.71041 | -52.47732 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4e5e11b3-d9e0-3dca-9a72-5863e2cdc54f | -3.3301 | -46.69874 | 2024-11-29 05:22:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8667951c-06fa-368c-848c-02b28e5ff7b6 | -3.48766 | -50.44807 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93a2635c-3b4d-3f77-a029-b27bbabeb4ef | -4.78377 | -46.12207 | 2024-11-29 05:22:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 9316b8e1-3efb-3775-9eee-d27ec1975c27 | -1.88408 | -52.65917 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd7b9eb2-9b88-360f-a439-f8dd2b885d4d | -2.30167 | -51.99111 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8072a589-3e25-301a-8810-9c7582d88fdd | -3.05776 | -51.05935 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1b7fb43-e9f1-32b9-9baf-82eed6b6802a | -2.69645 | -51.99084 | 2024-11-29 05:22:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9d7ed254-1006-3bad-8d6b-ef255f5478b0 | -2.87298 | -53.98062 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a249653-4c7a-3eca-8752-66560da6a38f | -3.53924 | -50.18207 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9754444-4a39-3483-bea3-93d64c650484 | -2.86875 | -53.97997 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 822fc104-9162-3fcd-8f91-04e5ec6b1e97 | -3.2785 | -50.15796 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13338b21-2150-3262-b5be-176bfc7b1753 | -1.70224 | -52.4488 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 712d5b4c-7435-3b04-9bf5-6b2616f03647 | -2.76746 | -54.07944 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a0715d8c-aab9-3789-a25b-e9216b09ed52 | -2.83957 | -54.11783 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3a6548e2-a68f-3b28-94af-6242ec74413e | -3.29634 | -53.69109 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b868028a-6348-330e-81e1-c4dd9afc53a5 | -3.43367 | -54.11628 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a035c2fe-fd2a-3c31-a86e-411da6be285f | -1.6534 | -53.81649 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb03a813-ec16-38ab-9755-06a0956dc44e | -3.09944 | -53.8166 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f9804685-bf65-392f-b5cf-bc8d1b789689 | -2.86393 | -53.98322 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5da904ff-a9cb-3c6b-8186-d6be17f6f531 | -3.91394 | -53.66669 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e608391e-bea3-379c-bd3e-476023f36ccd | -1.6581 | -52.72704 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e669295c-b1e0-3260-af18-d2a50b49e14c | -1.71668 | -52.77163 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5ce7d037-c381-3301-8d96-5e9ce4b90661 | -2.25764 | -53.75066 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 645dca39-bc71-3b5c-a92b-737add1f7a70 | -3.11204 | -53.76137 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa77dae0-f3dc-31b8-a0db-05ac385f5b13 | -3.46912 | -50.53393 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0ff83066-1858-3622-9ec2-0be55661417c | -1.65738 | -52.73157 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ebea14ef-46a3-3f17-be4d-ca50aaac02a1 | -3.38571 | -50.11304 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b74e2392-02c5-3fd2-8d98-bd3e5f1fef50 | -2.58359 | -49.99851 | 2024-11-29 05:22:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ef79642-92b9-3489-b9ce-2af48b926179 | -2.59492 | -53.96851 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c1c7c12-d3fa-3019-8dae-49799e4d6e67 | -3.2499 | -50.77095 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8f8bb50-e2e8-38b9-8c78-6a1f9e41902a | -3.23852 | -53.63115 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e58a2294-c45a-38cc-9337-328dadd4b846 | -3.10508 | -54.04147 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4080eba7-57d2-378d-ab2e-34b4427cbf20 | -3.24726 | -53.6324 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a8da15a-ef24-3a73-8371-19ed4727b36b | -2.7438 | -54.03638 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6ca77c29-3e13-3655-9b1d-e0165adaa08f | -2.31705 | -51.95598 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 53aec44c-11fa-31ab-ad53-9c549a079f46 | -4.17181 | -48.62104 | 2024-11-29 05:22:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad5f7a8d-50d4-3ab3-adac-24e9bbd0602c | -3.24984 | -50.6211 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03d80c71-21e1-316e-b3cc-1562844fef5e | -1.68033 | -52.52758 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c8b99cfd-af05-3a60-8dbd-0e1840271a0a | -2.10288 | -50.34569 | 2024-11-29 05:22:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cfe3ea77-beb6-3775-a754-39e3de7e4ad8 | -3.52592 | -50.19505 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b666b7df-e263-3cf5-9bd8-5bede969b315 | -2.65856 | -48.78122 | 2024-11-29 05:22:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 64afd45e-2ecd-3b80-ad0f-dba4e6a29db4 | -2.70533 | -51.9976 | 2024-11-29 05:22:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7b8a3007-b6c1-390a-9b11-1d295734ae9b | -3.09703 | -53.73136 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 061c127e-a37f-3eaa-af52-08f29ff47c45 | -1.68912 | -52.43027 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 65e2567a-655a-3a3c-a6c8-72d6e4e0e23b | -2.59735 | -53.98078 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24156e7c-06da-3684-abec-0ab5cddc12fa | -1.43489 | -55.24501 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fc37bcf-d93d-3794-9044-274cb3f6cd1d | -1.61804 | -53.87867 | 2024-11-29 05:22:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6716e37-c829-3152-b29d-c44963c047ca | -2.83574 | -48.08852 | 2024-11-29 05:22:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ced55ae0-dad6-31af-94c8-808d1ed5fab0 | -2.73314 | -54.13661 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e775b751-8c57-3fcb-934e-ed9c38261a75 | -3.093 | -54.03543 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 31b0e5f7-c4ac-3b2d-87cf-e15243f4b745 | -3.66444 | -52.2892 | 2024-11-29 05:22:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ffe466b8-906e-3b34-be55-767f6e31685f | -2.58674 | -54.24292 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b58e0d8-eddd-3f0a-b055-3ecb11633d31 | -1.58565 | -53.83796 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 9114e473-2c48-38cb-8322-0e49a7564970 | -3.17654 | -48.43776 | 2024-11-29 05:22:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba539340-f3ad-3316-bf2a-92a9b9a7cc41 | -3.87459 | -48.36083 | 2024-11-29 05:22:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b348f1d9-3047-3482-9ccf-f3579f26aed6 | -2.10341 | -50.3423 | 2024-11-29 05:22:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78797b04-c32f-3e75-9ba1-7ba21f01e0aa | -4.20122 | -48.56548 | 2024-11-29 05:22:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f724fbc-1e5b-3d85-ad5e-03c68a956393 | -1.69836 | -52.44335 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 996a9a83-29ed-3fc9-908d-672a094c6c7e | -3.5387 | -50.18563 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49dd2c2e-682e-3c4e-8f28-f41e346faa20 | -2.83426 | -48.09842 | 2024-11-29 05:22:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 20660263-475c-3a48-a92b-27f4317a6c5c | -2.66243 | -48.78724 | 2024-11-29 05:22:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| fb4bf0d8-317c-3a4d-8797-63c1fcddbc40 | -1.58359 | -53.84649 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2ef67032-c1e5-3e5d-9562-b195d6bb2941 | -1.58507 | -53.84181 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 78279375-9284-3d23-bddf-4a0a5ad81751 | -1.94111 | -52.96333 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a449e3e5-13d8-36f9-82b6-942e8b0ac3c9 | -2.98 | -53.89476 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fae53d39-0aa1-3cd7-af83-e7900c96ada1 | -1.30318 | -55.74702 | 2024-11-29 05:22:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f9dc8e0-3e10-34e3-890b-84cfd0b7743e | -4.78561 | -46.1133 | 2024-11-29 05:22:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 0cef9153-6ec7-39e2-aa36-9ee8a7222bba | -3.02536 | -54.02651 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e236c8c2-7b3b-3985-bd91-be48ef447b08 | -2.01193 | -51.19139 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a0c7b64-759d-38a2-8800-5f542eba6e52 | -3.30657 | -50.75578 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 36b4ce6f-c2c3-3326-a0f2-9ac55a765699 | -3.46371 | -50.53302 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e9e3164c-c34d-3926-ab25-84a9a228bd58 | -1.89205 | -54.54649 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27ac89c8-e9dd-383e-8480-af893f87b28a | -3.22572 | -54.18117 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a6736db2-6f71-3b57-aa22-ba56188a460d | -3.41225 | -54.17218 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b498fb5c-e776-320f-9c34-7498ba5348bd | -1.71285 | -52.76643 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ee73c0eb-9d9c-36b0-ba3d-93e758c88b18 | -2.00443 | -51.17213 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2211898d-535b-34eb-9a5c-b88897d80240 | -2.82416 | -55.58787 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f068696-02b4-3b08-9e28-76da6f292712 | -1.57043 | -55.78426 | 2024-11-29 05:22:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f7f3ae6-82a2-3393-88a3-8abe44a4b712 | -3.87389 | -48.36563 | 2024-11-29 05:22:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9d6f172d-42eb-38d9-9237-eb796a93738a | -2.16329 | -54.48629 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2f46bcd-2753-3bce-b88b-4778e6c75a80 | -2.98464 | -53.29297 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| c697bc00-c55b-3f75-b7f0-3341fae9e64a | -1.92187 | -52.89464 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8f2a0d4b-863b-38bd-8baa-3239460fb628 | -2.3696 | -55.70599 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eee6309d-158f-359b-83e0-a3eeb1d686b1 | -2.83171 | -54.10876 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0050bf77-2fb5-3ad6-9223-9fd2a36c16f0 | -3.42011 | -53.88655 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6582445-07c7-3bd4-bc11-dd70c815ca09 | -3.09515 | -53.8159 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b128cefe-6128-31c4-9347-b6079d9e42dc | -4.17267 | -48.62993 | 2024-11-29 05:22:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5fe02ffb-04a9-33ad-9bd2-38c295ba5838 | -4.17337 | -48.62518 | 2024-11-29 05:22:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1fcfc3b6-8e6f-3f76-ae60-30d061300904 | -3.22113 | -53.42155 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 587d5eb6-599d-379b-bffc-b528d2407110 | -3.33048 | -46.69818 | 2024-11-29 05:22:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README92.md)
