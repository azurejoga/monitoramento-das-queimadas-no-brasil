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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32b02eaf-0cab-34ea-b64e-8a77b3b36c78 | -11.6951 | -43.655 | 2026-10-06 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 88484621-e22f-32f6-8a3e-419138ca66bf | -3.0932 | -53.7239 | 2026-10-06 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 166.7 |
| c80f3f92-9709-3c4b-a1b4-7244fb172967 | -2.9449 | -54.13 | 2026-10-06 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| c5bad617-28b8-3be1-9c99-f79a334ef84d | -2.8712 | -54.1719 | 2026-10-06 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| a40689c9-8b3c-3162-a721-5820eed535e6 | -3.0191 | -53.9071 | 2026-10-06 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| f3806409-795c-34c4-bea5-f3754a3f77bb | -2.9265 | -54.1305 | 2026-10-06 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 80e9e3e6-d381-3893-ad7c-6add20cc13dd | -5.8511 | -45.0091 | 2026-10-06 00:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| c3d68e0f-dc02-3659-baa9-2f46469e94ed | -2.9448 | -54.1501 | 2026-10-06 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 283f7372-cced-333e-8a94-270ceda22b9d | 0.4465 | -60.5252 | 2026-10-06 00:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 0769e8f0-d9e0-367b-ad5f-9ab5b653c486 | -3.0932 | -53.7441 | 2026-10-06 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 110.8 |
| f465c04f-b2b6-390c-94d4-c228f90c7ced | -3.1116 | -53.7234 | 2026-10-06 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 6733d451-6443-3448-8b43-08f79e478b77 | -3.3906 | -58.1953 | 2026-10-06 01:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 108.8 |
| f683bda4-472c-30ed-ae2a-f6c1986aeee6 | -11.6946 | -43.6787 | 2026-10-06 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 506d1b3e-71c8-3a2c-9e3c-76935efb0bed | -3.6731 | -55.9622 | 2026-10-06 01:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 0ac58aa8-42ed-3cb2-9c19-f7b113a66d14 | -8.7036 | -45.2061 | 2026-10-06 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 6aa2a7f5-7bb0-3368-b4e9-523778e519b8 | -12.634 | -42.858 | 2026-10-06 01:00:00 | GOES-19 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 80.2 |
| f82dca95-2869-3fab-be0f-6ec8e83a0ba0 | -2.9448 | -54.1501 | 2026-10-06 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| e3e0ac88-7ab9-30ae-9247-d4aaa3f940e1 | -8.7033 | -45.2289 | 2026-10-06 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 17fe13b5-5202-381b-a3cf-a89948713794 | -6.6683 | -43.8196 | 2026-10-06 01:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 1e153dee-3ceb-3906-a8b0-8283f2c8d9ae | -5.8509 | -45.0318 | 2026-10-06 01:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| b79b665b-2da0-3cc4-b89f-a4069dedc4f8 | -4.8766 | -42.9788 | 2026-10-06 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| ea2a397c-1299-3095-b4e2-074ca0a305da | -11.299 | -45.5025 | 2026-10-06 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| b583a753-7198-3d9e-bf83-d3bc1bbf9c02 | -11.6951 | -43.655 | 2026-10-06 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 85afd065-3391-3a04-83f3-8bbe797bf56c | -2.8897 | -54.1514 | 2026-10-06 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| e3531afa-1ec1-3e88-9a68-888bd2b32378 | -3.4955 | -49.8979 | 2026-10-06 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 3471f177-1fe7-339e-8ec6-a0a04dd961d2 | -2.9816 | -54.1291 | 2026-10-06 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 4da5f2f8-9e87-36f7-8277-a643a496ab11 | -2.9265 | -54.1305 | 2026-10-06 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 56365faf-91d0-32f7-aa5c-d06649fbf02c | -3.3905 | -58.2146 | 2026-10-06 01:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 07d78f70-b557-36ac-aa6a-fb5b78fb4de8 | -5.8511 | -45.0091 | 2026-10-06 01:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 7f8918ee-afec-360b-a65e-32b88a6a988b | -5.8323 | -45.0105 | 2026-10-06 01:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 31fffeab-9b4a-3359-8960-1df3692e894f | -3.7409 | -48.8689 | 2026-10-06 01:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 5686c3dd-21bc-3d1f-96f3-0db0b0f3fa54 | -11.2607 | -45.5078 | 2026-10-06 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| f65c4e04-cd66-3b1c-90c6-79fe310d9748 | -2.8897 | -54.1313 | 2026-10-06 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 539a0066-54c8-31c2-9e11-cd72e5c321fb | -2.9265 | -54.1104 | 2026-10-06 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 7492b281-1afb-3f85-af94-94c4a6b45e3d | -4.8578 | -42.9801 | 2026-10-06 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| e29c34a6-a56c-3d56-bd9f-3eda26e44648 | -4.1085 | -49.3871 | 2026-10-06 01:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 567599aa-d119-30b7-89c4-a7c2892340e3 | -2.7879 | -57.6649 | 2026-10-06 01:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| c2617ef7-a610-3472-8ea3-ecc8d15dfb83 | -3.6915 | -55.9618 | 2026-10-06 01:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 2a2100ab-2961-3f7a-86df-98863dd8ae19 | -11.2611 | -45.4849 | 2026-10-06 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 21bbe2f8-fe3e-3ce9-b6ed-0ec4f573be2b | -3.6915 | -55.942 | 2026-10-06 01:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 3be81c47-e06b-3272-b224-edf8e6f77588 | -4.8767 | -42.9554 | 2026-10-06 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 176.8 |
| c7e67b89-8c2d-3d88-bd6e-845272df2393 | -3.0191 | -53.9071 | 2026-10-06 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 5ac61a20-d274-33bd-ac0d-58fa327b45fa | -3.0375 | -53.8865 | 2026-10-06 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 288c1be1-5c37-3b1e-9b7d-8b23a767d006 | -4.858 | -42.9566 | 2026-10-06 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 235.6 |
| e1611592-aeaa-3dae-a0f5-ca3764f57c87 | -11.2798 | -45.5052 | 2026-10-06 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 168.1 |
| 09b9b39a-2f03-33db-955c-9bd7fe80ff6a | -2.8714 | -54.1318 | 2026-10-06 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 124.4 |
| 17f78699-8e8a-38f7-9023-2d57d2bc4a8b | -2.7796 | -54.1138 | 2026-10-06 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 11305ddd-ba98-3ab1-b85c-25cbcff26c0b | -2.7796 | -54.0937 | 2026-10-06 01:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| eb1256b4-3ede-31ca-919a-3896e5a91a4e | -3.3723 | -58.1957 | 2026-10-06 01:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 4390d244-8d00-31e8-8081-3570584dfb3e | -4.1084 | -49.4084 | 2026-10-06 01:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| c2104f52-e6ef-3dcf-8708-575bd50db98c | -3.0001 | -54.1086 | 2026-10-06 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| c1187004-295a-378c-909e-220c4ef88a77 | -11.2993 | -45.4796 | 2026-10-06 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 0c759618-3c7b-32d7-b6c4-7355edbcb919 | -2.9449 | -54.13 | 2026-10-06 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 1c87d815-1525-3779-9ac4-ff75268720c1 | 0.4465 | -60.5252 | 2026-10-06 01:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 45.7 |
| b58ae231-fb8c-3e11-9a20-3bfd63a8c85e | -9.7312 | -65.0944 | 2026-10-06 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.5 |
| dc525569-171a-3511-8e73-aee9801293a0 | -3.6732 | -55.9425 | 2026-10-06 01:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 43653e74-7505-375c-aa64-6e574699981c | -2.7879 | -57.6843 | 2026-10-06 01:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 07af3769-3683-3869-a18a-ea6bc7a864cf | -3.1608 | -50.4347 | 2026-10-06 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| e93ce36c-4f6f-323c-af66-d206d23303d1 | 0.4465 | -60.5442 | 2026-10-06 01:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 821f4a74-310d-3993-aab5-45d06660d9a3 | -2.8713 | -54.1518 | 2026-10-06 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 165.4 |
| 8bf6d111-1540-36e3-a97d-1b14aa3a8683 | -3.0 | -54.1287 | 2026-10-06 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| a7aa5057-7a75-3e85-8e8a-d419be40903c | -11.2802 | -45.4823 | 2026-10-06 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 347.6 |
| 2ff95299-5d77-39dd-af78-5b49613d8fde | -3.0192 | -53.887 | 2026-10-06 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 147.7 |
| c8da3c4e-63f6-3276-a0c9-4094b6c0cf68 | -12.8783 | -62.155998 | 2026-10-06 01:08:00 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2214e1d9-a0ac-3cc9-b964-42141fb20803 | -2.9833 | -54.116699 | 2026-10-06 01:08:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f35bcf43-9443-371c-9c6d-d814f2367a51 | -2.7745 | -54.136902 | 2026-10-06 01:08:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbeb9e0d-c866-323b-8652-b44a68cbf3ed | -9.7316 | -65.088097 | 2026-10-06 01:08:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 956552af-ccfa-37f8-af9f-0ca7ea67304c | -8.9964 | -65.393303 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eb7288ae-8789-3022-ace6-fedf4c71e9cb | -3.6649 | -55.931 | 2026-10-06 01:08:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f63c1719-3408-3b5e-854e-f538f5f5ff5f | -8.5227 | -61.4352 | 2026-10-06 01:08:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 87b0f5e1-6c06-3bff-a3f3-90313957a8b7 | -12.1346 | -63.1572 | 2026-10-06 01:08:00 | METOP-B | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1685c6aa-425a-399f-952b-d093f7764e50 | -1.5601 | -66.633797 | 2026-10-06 01:08:00 | METOP-B | SANTA ISABEL DO RIO NEGRO | AMAZONAS | Brasil | 1303601 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b97ea67b-2440-3a33-be25-5fbea4357892 | -9.5483 | -64.817802 | 2026-10-06 01:08:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 98740c15-9684-3b79-a968-787bf3787318 | -9.4751 | -67.070198 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a91dacf3-39b4-3671-865d-4711c25c8880 | -9.712 | -65.0924 | 2026-10-06 01:08:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cbd2ce0a-20a0-321b-82ba-c0c56f455259 | -3.0188 | -53.926601 | 2026-10-06 01:08:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36a47513-04a7-31a4-b6c4-e784c173e2c9 | -2.916 | -54.1329 | 2026-10-06 01:08:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50f87b16-666b-3474-b912-fb590dc52e61 | -9.4888 | -67.659401 | 2026-10-06 01:08:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d45bb61f-ff0e-3714-8cfc-980f0d101a08 | -8.598 | -66.811897 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| de90835f-1a23-3f7f-9d19-df7c63c6bdf3 | -9.0271 | -65.719299 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b278b8ad-6382-3e42-b434-11f265902329 | -12.8767 | -62.148899 | 2026-10-06 01:08:00 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1e358341-e317-3e7d-8b6c-ed82d5b20c8d | -12.6119 | -60.904202 | 2026-10-06 01:08:00 | METOP-B | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 62a3bde4-f169-33c9-b58e-1e000db85cf0 | -8.6061 | -66.801903 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4b528e90-32cc-3aee-9886-a48aa8f39263 | -9.1653 | -68.256302 | 2026-10-06 01:08:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cc87102e-da62-363f-9581-ebb031dadbf2 | -3.0449 | -54.161098 | 2026-10-06 01:08:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe37eafb-111f-3497-8e22-3f2aef431354 | -9.0255 | -65.711998 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c5facc7d-a27c-3ad3-a1e3-0d2985788080 | -3.0488 | -54.219002 | 2026-10-06 01:08:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64e93266-4f46-3e47-8ce7-5c33de1d20aa | -9.7202 | -65.083199 | 2026-10-06 01:08:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 51d97b36-5ac0-345c-89eb-1f1caa4c0f4f | -2.7679 | -57.674099 | 2026-10-06 01:08:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f8efcba6-1964-3bb8-8a14-1b8855d8f089 | -9.5499 | -64.824799 | 2026-10-06 01:08:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ee46f1e6-bd9f-3f28-8b6d-b9fc22a6ec59 | -2.9323 | -54.158699 | 2026-10-06 01:08:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c21c0fb6-8133-3a99-9f70-166e50e5510c | -9.1633 | -68.246803 | 2026-10-06 01:08:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8d97701a-a0b6-3df5-8d3e-a54fbba5a4d3 | -9.1069 | -67.695099 | 2026-10-06 01:08:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e48a362a-c8a0-33a1-8a6f-9f01a320bcf0 | -2.7677 | -54.108501 | 2026-10-06 01:08:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd602dd5-0606-3e96-b625-32a59a9ae82b | -2.9737 | -54.118999 | 2026-10-06 01:08:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9275a517-d0f1-3a4a-b8ff-6257e1c8e615 | -8.5963 | -66.804001 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 17c16bcb-4394-3a5e-b6c1-56f90607cc0d | -9.0986 | -65.483498 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6deaa6c6-f50a-35fe-8942-f5a42c0612c3 | -8.597 | -63.651299 | 2026-10-06 01:08:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b91e4a1e-2932-3fc7-8660-7256ac9138b4 | -8.6476 | -66.850899 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 98cc5ef7-0580-39e8-a60d-f1ffa35e476b | 0.4491 | -60.538502 | 2026-10-06 01:08:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)
