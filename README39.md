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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43e4f80e-baf0-3890-8da9-0df4fdbc3897 | -3.0428 | -54.20767 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 62593d88-9506-33a3-97b8-c8e57b1aa333 | -2.99201 | -51.04473 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4e9236df-5ffb-3506-b038-4cc33b3295b8 | -3.70249 | -50.97448 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9735c34e-004f-317c-811b-795b9ad8487c | -2.89071 | -54.11943 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f23419e-df65-3e72-9c7a-066abb4c1821 | -3.10682 | -53.73516 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c4a8a840-e424-3284-85c5-ad2391af57ea | -3.29358 | -53.84731 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d017a100-ecb8-3275-842d-334558087b90 | -3.12676 | -53.7419 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21a296df-da56-387a-9fe8-0815f6560868 | -3.45576 | -50.61485 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7d3dda9-9096-37c0-b720-a53014bc1364 | -2.58755 | -51.8513 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| f38f4705-d6ad-3602-b41c-da15a0c341b2 | -3.10566 | -50.28661 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4695153-4b43-32b9-97f2-dab7b85bf2ce | -3.18619 | -54.08186 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aee5b2aa-69ff-3fe5-83be-bc84ded95d3b | -1.22257 | -54.53651 | 2026-10-04 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2bb6d110-941c-3132-8192-81265f017ccb | -3.15475 | -53.06939 | 2026-10-04 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0595a0fa-8cf7-320f-bfa6-94ed2849ac2b | -3.00725 | -53.8745 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebca42c4-1ced-316e-a279-284eb89adc4c | -2.20921 | -48.22667 | 2026-10-04 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5fd3e37c-b4ba-3404-a808-8260ee92fe2e | -3.13272 | -53.7518 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e2e74e44-658d-3644-9e0e-c371a98d0f3a | -3.1274 | -53.7251 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3faf40f2-1bcf-35f9-92e8-8c4b4534afc3 | -3.18468 | -50.53331 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73bdbc37-f8eb-373e-a92a-c6260911fce0 | -3.82013 | -52.04673 | 2026-10-04 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fe7297c1-18db-3b83-b242-a68d03d9e656 | -3.00518 | -50.4728 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bdbab777-ed0a-33e6-9211-c2028b0a8728 | -3.44049 | -52.88873 | 2026-10-04 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a97fc9b6-02bc-35b3-aad1-ca7e99b2cf2e | -3.4667 | -50.09928 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 791381a0-0ea0-38d0-968d-f56566e3552b | -3.18316 | -54.0791 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c6044406-468b-38bb-a85f-38fdea0f5d5d | -2.97088 | -54.10426 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| db40b62d-0fce-364a-85f8-55e5d4cc2d09 | -2.92921 | -48.75354 | 2026-10-04 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b66f799-ecaa-3d2b-acbf-d1cbb77a37ad | -4.11151 | -49.07132 | 2026-10-04 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 563f5bcb-a19d-349d-87e2-a1db3022edb4 | -2.9617 | -50.31716 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6195597c-7604-3255-b273-6feeb1a6a620 | -0.04539 | -50.82265 | 2026-10-04 04:55:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eb73723b-ac3d-387f-b841-bf59e52b93cd | 1.76111 | -55.63543 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1349850d-eb67-3b51-a898-6d31339f0275 | -2.89741 | -54.07831 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1652e5a-b699-3fe9-a6e9-95ed5ac6cf04 | -3.13435 | -53.75302 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c631470f-0ac6-3a37-958a-825a877d6db1 | -2.94464 | -54.18722 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0929e34c-3f42-3d6c-9612-bd880bacf642 | -2.83287 | -54.21004 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 428395a6-648a-3050-b2d9-f061c38a1fdd | -3.46725 | -50.09582 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 87b1dbbb-585e-35e0-8fd1-14431a0ed31e | -3.01053 | -53.88198 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 319caace-3e16-30f7-a981-03fe605f374c | -0.34632 | -52.05372 | 2026-10-04 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6f26f14-3550-3e80-8875-3178e71f9f86 | -1.40672 | -49.26432 | 2026-10-04 04:55:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ad14cb2f-1ab0-3d3f-86ae-0b65d60ef45c | -4.92793 | -45.69263 | 2026-10-04 04:55:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| af952a8b-9b32-314e-ab4d-e6d205466cd7 | -2.99581 | -49.22288 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 42a8d1e1-0b3e-39e1-9161-5db5b9190760 | -3.88815 | -49.69604 | 2026-10-04 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f6802a00-4321-3e63-bca7-b461558ce815 | -1.98337 | -50.51418 | 2026-10-04 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f2adae9-eca1-3314-991c-1919d1d58a38 | -1.15768 | -49.25406 | 2026-10-04 04:55:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2162ac0d-5ae5-3521-9fbc-8dc38136cd13 | -2.92167 | -54.09629 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 928663ab-8872-3014-b4c8-223d77631197 | -2.85144 | -51.2902 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8804d0a7-8d9e-3fd8-b088-746cab2e9787 | -4.28727 | -50.27835 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| a9818ca7-375d-3e1b-a6e0-c99eb6bd3a04 | -3.36122 | -43.37942 | 2026-10-04 04:55:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf859615-f607-3210-840f-b938f1e007c2 | -3.30683 | -53.83596 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| aacbfb70-76c2-3225-8cd4-169f74a5457b | -1.20816 | -55.86011 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4340b492-2be3-3493-925f-2eaf8be70a6b | -3.29317 | -49.12403 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4fdda2ed-f90f-3664-88b6-64730734ba5b | -2.97233 | -54.0951 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34b69cc4-1ec6-36d5-afc1-ef1d9c95ff90 | -4.27506 | -50.26934 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1431039a-80d2-3bf4-b477-116ac98237ed | -2.88541 | -54.12803 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57544d67-0129-3671-8878-2a7ee0291541 | -2.8945 | -54.12005 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6d7ed4b0-ab51-3097-aacf-974dde556343 | -4.14612 | -49.69301 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd5f3aa2-0526-339e-bc3f-a766d30c3822 | -3.12809 | -53.72075 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d54dbd67-1fdf-3c6b-b514-624bea218438 | -4.47159 | -50.97101 | 2026-10-04 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fae7a37f-ef15-3cba-b951-13f139d4c186 | -3.08617 | -49.53106 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ff43381-ea1e-36cb-9616-fcc65192cc71 | -3.22684 | -54.30985 | 2026-10-04 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d9a5e597-01e4-3714-8556-b961ca9c84b9 | -2.96331 | -54.10302 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4bd3440e-b717-34a1-8f8d-97274c3af0a9 | -3.20805 | -50.74664 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b107f239-7434-3968-836b-e795de66f345 | -3.18148 | -57.9129 | 2026-10-04 04:55:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eb3aa84f-4292-3fd8-87c2-09044de94046 | -3.20527 | -50.74265 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c320395b-daed-39c5-b4bb-93f17eeb7c7c | -4.39055 | -45.9896 | 2026-10-04 04:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 46dc1127-37b2-326c-bb84-dd96ee7ccadc | -4.05177 | -51.07991 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fabaa0fe-c73a-3b47-87ce-a2edcfdd9e54 | -1.01352 | -48.79573 | 2026-10-04 04:55:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e731eb7d-30bf-37ad-abc6-d107a4eb14d0 | -3.1341 | -53.73065 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c5eba11e-759f-3561-8ec4-cbe584d92cf6 | -5.00819 | -45.14229 | 2026-10-04 04:55:00 | NPP-375D | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de6dcf84-a263-3598-af95-a018abc69d67 | -4.25861 | -46.37943 | 2026-10-04 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3954fe5a-3d1c-333c-80cc-78c631e88e19 | -2.22291 | -53.71288 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e9d47dc0-332d-3c72-9343-392077c50dc1 | -3.01171 | -50.47021 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e756e937-f596-314f-9614-098a5e61d6f3 | -4.26462 | -50.7394 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f0f294c-1f5b-3131-b75a-8c54c8b1131f | -3.10347 | -50.30043 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb957d06-47f8-3b98-8f0a-b2a65755fcd3 | -2.21509 | -51.95697 | 2026-10-04 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3605bae7-ecf0-3a81-8f55-81461560b4ab | -3.11631 | -53.72331 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| fac92166-3e25-3601-9e50-54af85150236 | -3.7024 | -50.66141 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| f0eb4d9e-b326-36e1-b9a0-e65d5193bb16 | -3.90205 | -49.69471 | 2026-10-04 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9ab52004-c004-383b-9a58-e0d63d6fb878 | -4.25691 | -46.36509 | 2026-10-04 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 89a0f1fd-bfa0-3b66-a2d1-107dbffa05e7 | 1.93409 | -55.72295 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82ed7103-a69d-3911-826a-c160de5e2520 | -1.264 | -54.55864 | 2026-10-04 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81050436-d9d1-3ab5-b411-f58d09fd91be | -4.45417 | -47.92744 | 2026-10-04 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d39800b4-fa6a-35d8-81e1-f940922f738c | -3.77335 | -51.40259 | 2026-10-04 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2b552eb9-74eb-3c27-a308-2ed1ddccf807 | -3.01061 | -50.47713 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5419552f-b749-3fe2-9513-8cdff6c4e4c2 | -2.79241 | -54.10608 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d8af9f8c-bb26-36e5-ad82-47cd5c140945 | -3.81189 | -50.84556 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0fe6ebfb-1ef8-3390-b34d-5bc56c85935c | -0.24037 | -48.4915 | 2026-10-04 04:55:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a70b9a7-d3db-323f-84ee-0bfa78ad1c0c | -3.13504 | -53.74866 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4450359-6ffa-3f2c-bb65-53e761db853e | -2.81212 | -54.10452 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0b6afb05-046f-3f3c-9a9d-8b03c4d40c70 | -3.11214 | -53.74942 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| fa85400e-1bea-3441-90e3-64ee40d7538e | -4.07967 | -48.95955 | 2026-10-04 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ffefa7e1-79ac-31f0-934e-726f8f6634c6 | -3.12162 | -53.73755 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 101d77c4-616e-30ff-898d-c6d2db294a8e | -2.7535 | -51.55663 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c34748b-194a-3b51-bac1-45e0d16527b5 | -2.81129 | -54.08557 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0f5d2ea-b9eb-3929-a6fd-04fbe9cd7ca0 | -3.13045 | -53.7425 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40af7252-801e-374c-9389-92f838aa13d5 | -5.36473 | -45.03407 | 2026-10-04 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f3203e9-2032-3450-a638-17f04de39f4c | -2.88466 | -54.13262 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96ad1123-6120-3cf5-9833-33e1b9fb8ddc | -2.82887 | -54.12138 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1a6de07b-50d6-36b8-acc1-3d9ede100a98 | -4.45937 | -50.98332 | 2026-10-04 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ca76ca8-8809-3779-8cd4-23a2d33c339e | -4.98157 | -46.04259 | 2026-10-04 04:55:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4e93bd7-4b9c-3752-b1d1-419c5597231a | -4.28449 | -50.27437 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 907d539b-7270-38f4-abc3-92a653e56b95 | -1.85818 | -47.97667 | 2026-10-04 04:55:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README40.md)
