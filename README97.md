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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a83e511-6640-3ca6-adaa-1c3842107fe5 | -3.54327 | -54.65007 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c557a1cb-003a-3e0a-9a2a-fd64182952b7 | -2.94721 | -54.06888 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 08e34c7c-2693-3d6b-bddd-326b8f128efc | -1.46536 | -54.77184 | 2026-10-07 05:40:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f0eff93-7d8e-38d2-ae08-910aaed17b04 | -3.34952 | -59.50705 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 885c61d9-ac3a-366c-8778-9a0d59380366 | -4.15433 | -55.14499 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 882742f0-ae73-3adc-b89d-9e9707e78d33 | -3.11588 | -53.76275 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 128dd6f7-dc6f-3599-b043-eced2bd14273 | -3.69929 | -58.28811 | 2026-10-07 05:40:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af97bb4e-a9bb-3cac-9bf7-a480e1dd81da | -3.26904 | -54.04451 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| bc5f8d72-e085-3ba2-9e5f-631887d9fa94 | -3.05267 | -57.52142 | 2026-10-07 05:40:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c59e19b1-7407-39c6-bc6e-019d7bcdd18f | -2.46709 | -56.07008 | 2026-10-07 05:40:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 763ed678-b724-3e95-8473-5466e0a4446f | 1.86719 | -55.7351 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8feb7e1-ca89-3d1e-83f8-7c457148864b | -3.10053 | -54.2807 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ad2fe0be-8e0a-3092-831d-a79cc2d6a734 | -3.51908 | -54.65603 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1a528f7e-5e6f-3792-bb7e-3a2f899fe624 | -3.04707 | -53.92765 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04196c1e-77de-37c5-ab35-ce6f39188b50 | -3.54324 | -59.49417 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac76ea80-8ec1-36ed-b72b-62182ba4c1e8 | -3.29515 | -59.49906 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62b351e2-8df3-328c-995e-76275e36f68c | -3.10954 | -53.77231 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 2111e0fd-a603-3024-ae8b-36e0dde8e70c | -3.00245 | -57.74402 | 2026-10-07 05:40:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a65fe16-e6eb-36f0-858c-cb29779d8fcc | -2.9702 | -56.62172 | 2026-10-07 05:40:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 260b8a0f-0f87-362a-9254-df7db74cd69d | -2.78248 | -51.68217 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 381c4aed-4076-36a9-ae3a-ec87849f0c97 | -3.9681 | -56.05667 | 2026-10-07 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db645956-2804-3df0-8995-dd232933ec84 | -2.77081 | -54.11003 | 2026-10-07 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 670a84b3-d4df-35a4-ab44-7135a420ff4a | -3.08905 | -54.29364 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 6bba438f-c1f9-33df-88a5-7d977daf9656 | -3.71268 | -51.14289 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0133de32-0157-3a73-959f-1df27e79e329 | -3.27672 | -54.02525 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e6364149-7c36-3927-8124-43a5adb117f3 | -3.13781 | -54.36555 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| defae52a-7ddc-3a42-8bc0-c24a19b500a9 | -3.26896 | -54.03778 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 5679241e-5763-3b13-9119-f1e59a676018 | -3.52121 | -58.75597 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86af1ee4-a19b-39dd-af83-a676d2197689 | -3.73869 | -55.98106 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ad90b9b-8780-34fe-9090-8045bce7e1a5 | -3.27976 | -50.41517 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d759d18-c3a0-3ec1-b433-0ad816b39886 | -1.46794 | -54.52706 | 2026-10-07 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a757e32-c3f9-33b2-a65d-a2d0eb78bd4f | -3.85479 | -55.98281 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bfb3f17b-e7be-3251-936e-51e0158ff7a9 | -3.29669 | -54.0539 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| af7fae00-5ec6-35a6-be2b-6f1e53d5d903 | -4.10051 | -52.06642 | 2026-10-07 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01ad50aa-7a5d-3116-ae1b-80db387ed41d | -2.48633 | -58.06613 | 2026-10-07 05:40:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 858b8ac7-ee87-30f0-8156-33519582db9b | -3.33413 | -59.4705 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b424db6-1d80-36ba-979a-c179d4cd6343 | -2.4795 | -56.09763 | 2026-10-07 05:40:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 666e1437-8334-3a0d-82e4-27fa6cd1593c | -3.35177 | -54.16766 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54e01d5d-bcbc-3c8c-adf6-3b8399b63f8a | -3.04067 | -53.90587 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f90e6e0e-2375-3bf4-8954-9e9834dd66c6 | -3.0296 | -53.91458 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2177f323-6b5f-3864-97e0-371072eaada9 | -3.02673 | -54.51783 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bcbf38c1-b613-341b-8678-5c52f00deee1 | -3.53991 | -50.09933 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20d0dd54-1cd8-3905-a18d-bff6a5921504 | 2.4551 | -50.82254 | 2026-10-07 05:40:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 469778fb-e6fc-3486-8e1d-a0e8c55c75ed | -3.48423 | -50.09111 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 00486fe4-d86c-3416-8c9d-dcd9333b116e | -3.52108 | -58.75065 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14aeb379-f64d-3525-b0e5-d25e1ca73012 | 3.15198 | -60.59408 | 2026-10-07 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98817e36-dbc2-38d0-9396-da3c4eef0bc7 | -3.38765 | -58.21019 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59d82675-ed0e-37ca-bcc7-250408841a51 | -3.80246 | -51.99263 | 2026-10-07 05:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a26fb2a9-e461-3506-9d15-c523ec725aac | 1.70705 | -55.6362 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67b21102-1afe-330a-b9f5-4eecafe1bc9f | -3.88671 | -55.82656 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 98644bbd-e3f8-3309-80a9-dcf269f07c93 | -3.01904 | -54.14139 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 76cd2555-f961-3d07-be21-48ae24157b52 | -2.8528 | -59.11124 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0acce0d1-4f24-3cd7-9516-150d830afa3e | -3.05273 | -54.21932 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0368cbd2-28a3-354e-847b-12a614da8e0d | -1.12136 | -54.11694 | 2026-10-07 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 940a6ca1-8ae9-3fc6-955b-8110f169bb30 | -3.49041 | -50.09209 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4f2e2254-75e7-3812-a97f-ecf20f322f61 | -3.38402 | -58.20964 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2047b2a0-238a-341b-bdf3-4004d9b9ec55 | -2.94052 | -54.15439 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 157f70ff-f644-346d-a3db-3c592eda9e77 | -2.89541 | -54.15586 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b8bb5e7-196d-3c4e-8a6f-1a739853f0b1 | -3.71435 | -59.69423 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 485c8cbc-0643-3d1f-9573-23385f7bfada | -3.29644 | -54.02298 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| e0cb9f65-63d0-3278-b456-1fb63f16fdb7 | -3.50478 | -54.65834 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8fbe140-280c-363c-b75c-8af083379f97 | -3.27439 | -50.40986 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2b2bc7b1-24b4-3fae-bd2b-509aa4beaeab | -3.57516 | -54.65492 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 84056115-8591-3759-87fd-6f745d5141a6 | -2.48995 | -58.06669 | 2026-10-07 05:40:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bdae0518-662b-34b6-a8be-fc967f04d7e3 | -1.09641 | -54.12726 | 2026-10-07 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98d43b13-b285-3e30-930f-e730ff2e53c9 | -3.05593 | -54.22972 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4120f88-fbd5-33f9-8a9a-1fb01d359756 | -3.05724 | -54.14231 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ee007f12-19e1-324d-91ef-006d25696e72 | -3.12441 | -53.7053 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 01bbf984-7fb0-3faf-9382-648730493ef4 | -3.1327 | -51.03052 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb0b2e99-7d63-36de-8512-edc6a00eba80 | -2.77522 | -54.08096 | 2026-10-07 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 301c38e4-f74d-381f-95c1-24ab1c80a0cf | -3.08241 | -54.2436 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbce766a-6da1-310e-80b9-d60e24d0a7a6 | -2.78906 | -51.67587 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b68c3141-b572-3b41-88c2-01d38da264b5 | -1.6258 | -55.12845 | 2026-10-07 05:40:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be981f77-c3fa-3556-ad69-3ba18261b431 | 1.70724 | -55.63303 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6448ce14-e9c0-3158-b03f-4617de2818d3 | -3.2705 | -54.03459 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| bbc23703-3a6b-3696-8535-dbc46930117f | -3.53923 | -59.49735 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c8ac163-4c68-3b60-a088-38da85d3aa6e | -3.72681 | -51.20916 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ff2e7772-be81-3786-8b62-ad5f1ede2402 | -3.49742 | -54.6457 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3e8da43-5560-303d-a0a9-4ad9761b4c8c | -3.05811 | -54.21519 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d61b03f-1e7f-36bd-a2cf-f72b632de47c | -2.94115 | -55.78753 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a62a907-83aa-3bf5-9f17-cab46c0930da | -1.19571 | -54.21062 | 2026-10-07 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c01618ac-08b6-3bd4-bdd6-ba962d189538 | -3.06392 | -54.17635 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c6417da3-a6ef-343e-8bb2-69da01672bc7 | -3.69566 | -58.28755 | 2026-10-07 05:40:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96be52ae-f842-3389-95e9-b2ea6f05f840 | -4.36799 | -54.75153 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7aa3c5f0-763a-37c5-a80b-e925e5ff95a4 | -3.073 | -54.14771 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3866a231-143b-3b5f-aed7-313111c5a844 | -3.28574 | -54.06248 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7cea91bc-50d8-3d27-85ba-6fe1d317b5ef | -1.10753 | -54.15074 | 2026-10-07 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a57e0d6e-d3c1-3507-a3ac-db48dc04d385 | -2.98948 | -54.05164 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ded5bf63-b49f-36ff-b664-b3e955997edc | -4.4478 | -54.97216 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7f6980f5-b018-3cc4-aab2-de9fcdbc36de | -3.50545 | -54.65379 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79fc56df-700b-369e-b225-42dfce11ca72 | -3.58406 | -54.31405 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ffb64434-6c21-38ce-8833-c241dbacddf9 | -3.96683 | -56.12153 | 2026-10-07 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2bb4825f-a6f7-33f7-b686-c9d408b62b64 | -3.0104 | -54.13526 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3a4d7d46-82cc-32cb-ba2a-dc74208bf40b | -3.01508 | -54.13597 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3200a32a-98e3-331a-96f7-5c16cbe5a5b5 | -3.03837 | -54.26266 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7ae0078-194b-34ab-a83b-a328ec45fe03 | -3.08808 | -54.26889 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3bbb2836-5299-3045-badb-a3020e5d7de3 | -3.12969 | -54.36758 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18a2488e-8a7e-39d9-85a0-ac723e44059d | -3.15025 | -50.44353 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a65885f-b564-3d83-8024-2e899bb590b6 | -3.04949 | -53.94352 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b1667d9b-0c81-3eac-a557-ca0090365ece | -2.7676 | -54.09963 | 2026-10-07 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |


[Clique aqui para ver as próximas entradas](README98.md)
