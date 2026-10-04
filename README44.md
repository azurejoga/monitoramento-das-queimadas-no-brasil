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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5109dd8-4c63-300b-938e-c802ad3b1dcc | -4.4677 | -50.97396 | 2026-10-04 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6909338b-4bcf-39a9-9630-0c2a9063aed7 | -3.28315 | -53.84115 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bd91aa9-514c-3b52-96d7-30a688b6cd55 | -2.53715 | -58.03606 | 2026-10-04 04:55:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b010dfd0-5874-340b-a7a4-fa2de228b23f | -2.8099 | -54.11831 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9ad2a535-fc89-3267-b93b-5f7cc41e9e4b | -3.18245 | -54.08356 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ff41cb86-e3f6-3ce6-9987-d9915f635995 | -3.12996 | -53.75677 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 400c24e1-6fd1-3443-b484-a678b39d72c5 | -2.90438 | -54.13108 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9cf78556-e639-3859-8d10-bc7521d1a5b0 | -3.81795 | -51.54026 | 2026-10-04 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 958d7d3f-38c1-3272-b743-dde867a4bcce | -2.83211 | -50.47408 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5217fe53-a65b-3662-9ffb-dd4e0db7212a | -3.20472 | -50.74612 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d51887b0-d822-3608-8b71-2c56b01d5bac | -2.59097 | -51.85186 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| ef1147d7-6d0f-3246-a8fb-994eb6e12b70 | -2.97422 | -54.07899 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e53e79b0-49e6-32b1-bd83-29cbdb626dc8 | -3.11191 | -53.72707 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 30802b89-924c-36e8-b86b-e39da0c4ded8 | -3.22853 | -54.37269 | 2026-10-04 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ca466ad-c879-319f-a30a-299eeb4439ba | -2.14592 | -48.47455 | 2026-10-04 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 08074e4c-1372-39ff-8cf2-31460fdba90d | -3.13849 | -53.7269 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c7df6c7f-24bc-3042-825f-c64f5c3947d9 | -2.27303 | -50.79916 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 28ad84ca-9c1d-345c-8549-ccf8f767573a | -2.24619 | -51.93057 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f8661e1-1549-3a70-b9cf-551d9ea80a63 | -4.4566 | -50.97932 | 2026-10-04 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5393f694-578a-3cf6-a6d7-935c41634b56 | -2.04102 | -48.49937 | 2026-10-04 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 93bc309d-93dc-382c-b65b-ead3b70579d0 | -3.18318 | -54.07671 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5cf73556-7aa2-3bf7-8715-ed84911b0126 | -3.41721 | -48.33712 | 2026-10-04 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 517ea28e-0f82-3620-aa3c-2ff68ce97f57 | -3.01831 | -54.16597 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0945e7d2-8ca0-3e1a-970e-dcb6793535ac | -4.92848 | -45.68908 | 2026-10-04 04:55:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a4fc6f2-9413-3381-b011-ccfb68bf625c | -3.12532 | -53.7506 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c6f586e-82c2-37de-a7bd-5ded8d50c6cd | -4.84645 | -45.9851 | 2026-10-04 04:55:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eca4edae-86f2-3d00-bc51-d6b7f7554c68 | -2.88382 | -54.09018 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fef7f5d-74f3-3d83-bb5f-8f7828ecae05 | -3.18693 | -54.07738 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3bcd93f8-f13d-3079-a2cd-94d787cc86bc | -1.11998 | -54.15267 | 2026-10-04 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98cf9aa3-0afb-3eef-838c-29a89d8992a2 | -3.11283 | -53.74506 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 3addb2d0-01c4-38be-9fa0-3df1f170ed16 | -3.50988 | -54.61567 | 2026-10-04 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5474c853-0c53-391e-b386-af91bfd68cb4 | -3.17189 | -54.07706 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d208bac-61fb-3db3-a88c-5519af0e3b9d | -3.1207 | -51.59599 | 2026-10-04 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d16a1ea-76fe-3778-900d-ffd9fdde4848 | -4.25932 | -46.37486 | 2026-10-04 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2def458-343e-32c0-9e46-79e4d571fc93 | -3.23789 | -50.58074 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 651cd559-87f9-3c90-89c1-af04e5bdfdc1 | -2.97271 | -54.0881 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c588c62d-bd02-33c0-8ee8-82348d3ec3ec | -4.11207 | -49.06773 | 2026-10-04 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e6422a25-df1f-3ace-8a27-8e428f1e2fa9 | -2.82054 | -54.12476 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 592c88e3-7b84-3ec5-a954-4626bf6b13a7 | -2.96782 | -54.09906 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b098c527-de5c-3bf2-80dc-825245e0fca7 | -2.94451 | -54.12351 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c516cd45-5354-3ead-b8f3-f4f67091155c | -2.21989 | -48.02333 | 2026-10-04 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f3db89b-c7cc-34a8-84df-31a2b36b17ed | -2.99917 | -49.22341 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 26d0b9bc-6a73-3191-b36c-26d73edb97ac | -4.48385 | -45.53551 | 2026-10-04 04:55:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bee7c415-41de-3367-afd8-09482fa15c2b | 3.64468 | -60.75742 | 2026-10-04 04:55:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 453a9a03-f83d-353f-81f2-3d92a3671737 | -3.00728 | -50.47661 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 48fe352d-1794-3d0e-8866-c68126d38495 | -3.11954 | -53.75062 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 75557055-bb1b-38e9-83ca-14b722348b19 | -4.26073 | -46.36573 | 2026-10-04 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f6cefdc4-2be5-3574-8798-cd0d2bca38b3 | -1.08336 | -54.10683 | 2026-10-04 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87b4f891-e255-3ccc-a2e6-80552420db26 | -2.96743 | -54.0966 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f92d5d7-c0d9-367c-af7c-1ee04fff21aa | -3.18998 | -54.08487 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8a8afb5f-28e5-3488-9895-80d73c9c27ed | -1.09501 | -54.10869 | 2026-10-04 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6d265a1f-a69e-3b4c-b492-bc007622cf1a | -2.14918 | -59.22701 | 2026-10-04 04:55:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 219958c1-af76-3dae-ab94-c7c6804226e8 | -2.8136 | -54.09534 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 247f384a-af5f-3d5c-9e51-ff1ecab6407d | -3.18699 | -54.10049 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7d6b112e-8a83-3bc4-a7a3-4e074803e2d9 | -1.09968 | -54.10437 | 2026-10-04 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| edf1e9d2-5976-3663-b1db-b9c3b28c2a60 | -1.20882 | -55.85603 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e3e329e-4cab-316c-8ec4-8546287f029a | -2.83001 | -54.21209 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fcdb027a-0203-3589-b0d1-dd34a288d228 | -1.90613 | -47.01578 | 2026-10-04 04:55:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2b179264-2bc4-313b-b782-fcd41e5547cd | -2.84974 | -54.13176 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b9ed4dc5-5cb3-38ef-a3f5-49665b402b70 | -3.20694 | -50.75359 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4c373368-ece9-3489-888f-3c33b65dcda6 | -4.44857 | -49.92295 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6fe8afda-d82d-3cec-b4f6-404160ee1b64 | -2.85088 | -51.29374 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 1664fb97-3865-392d-a9b1-062704859550 | -3.12819 | -53.7332 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb69187d-1d52-3e6a-9383-b70e34b139e9 | -3.13179 | -53.72135 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a8cff85d-186a-3681-8548-a0ab2dc3a5fe | 1.81126 | -55.56206 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5121f540-c55f-3307-b581-7bc9d91808ee | -3.94233 | -48.43501 | 2026-10-04 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08eead8b-9d3a-3ba5-b3b0-e091e08ef8a2 | -3.28639 | -50.04273 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25d552bc-7e43-36cc-b221-dea90a9062fa | -3.81079 | -50.85251 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd2041ba-f311-325c-ba53-99e19a8d53a2 | -3.27261 | -50.08663 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1079bda3-c4ab-3470-9627-559d84c42d33 | -2.81443 | -54.11433 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e7fd8cb0-55fc-3d06-b26f-656ad6dbe2ce | -4.27399 | -49.98153 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77d40b00-dc3b-3788-8b6c-9ca9596c8624 | -3.87906 | -49.69833 | 2026-10-04 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 622e3d3b-2340-3223-b63c-71e43787bd74 | -3.93889 | -48.43447 | 2026-10-04 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6fdf67b-881c-351d-a00c-65169f04ef3b | -3.18413 | -50.53677 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 810ee4e8-c8b3-3bb9-9464-ef02200ed100 | -3.1915 | -54.09662 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6ab4e460-b484-37a8-b668-2c2678669584 | 1.91598 | -55.73289 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7aeb25d1-1bd5-396b-966d-24a9dda48397 | -2.80841 | -54.1275 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 48b350ba-aa90-354b-8d9f-787a3f930a12 | -2.80833 | -54.10391 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aeda9c26-bded-3967-b15e-e622bb8a2ffc | -4.29279 | -50.26503 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 0aac643b-f1e7-38d1-b801-9a0239f5c558 | -3.27552 | -53.81773 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c7a61fd-b3c8-3d7b-8cd4-9a83e35f4287 | -3.76988 | -51.85965 | 2026-10-04 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96d8768f-6204-3206-8073-d910ecf68962 | -4.15739 | -47.54128 | 2026-10-04 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d32a03e9-ee51-3e99-9e0a-5685f7e8d72f | -3.30495 | -49.13676 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39654868-4953-3caf-8053-4745821d7ac6 | -5.04931 | -42.78691 | 2026-10-04 04:55:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c92bc81c-eb16-3d71-88c1-d9b56fbb003d | -3.12695 | -53.75182 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80d0b18f-3162-301c-97c0-2861de799f4e | -2.58235 | -51.86177 | 2026-10-04 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 17a9e575-b544-3d58-a0f7-926e113928bb | -1.41179 | -48.89706 | 2026-10-04 04:55:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cba84b01-3872-3f1d-a85a-17521663cb92 | -2.79315 | -54.10148 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9e36947-5aa3-3446-ba26-d93890a28647 | -3.81244 | -50.84208 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9223393b-cf13-3830-88ac-a61f21df46a9 | -3.18922 | -54.08696 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ca22c181-69e6-3ffd-b3e5-5def7bb18eb3 | -4.26315 | -46.37544 | 2026-10-04 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ba05494-d784-3341-b273-9f2b6f8fcdd0 | -3.04814 | -54.21653 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 29879f2a-3c3c-347a-b1b4-e23b7b86673e | -3.47668 | -50.10084 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2d4ba529-ccd6-3c4a-90a8-b1858ef01aec | -3.5751 | -54.65779 | 2026-10-04 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b292464-a473-345b-bf0d-20dea35439b4 | -4.4577 | -47.92798 | 2026-10-04 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29ea3877-383c-3ebe-931b-95551ab26371 | -3.99334 | -50.55088 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bff79169-9aa2-3730-bed0-f2f7c3875c29 | -2.8 | -54.10728 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bc90655d-6c0e-3511-a8b4-615045b55637 | -4.26839 | -46.36683 | 2026-10-04 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 3c60c13c-e17a-395f-ab99-72324fab4deb | -3.89483 | -49.69709 | 2026-10-04 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae7f609c-2f41-3e02-aa8b-c71124534b15 | -2.44431 | -50.25342 | 2026-10-04 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |


[Clique aqui para ver as próximas entradas](README45.md)
