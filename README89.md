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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2ff7fc5-6d92-32f0-bb4b-8925e18d8952 | -11.61374 | -60.35933 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 69130549-6856-3f52-9de9-040aeab9d5e7 | -11.61033 | -60.3587 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4e283db5-521d-3c9d-9cbb-cc3cd917d9fd | -11.60506 | -60.36958 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8947546a-685e-31a0-bfd9-b34c812e312b | -11.59789 | -60.3488 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5ef84f9b-af83-3e60-ae14-28321266f0b2 | -11.5773 | -60.30294 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 420f76ea-6ff7-3f06-887b-0e9ce19bc2fa | -11.56065 | -60.16964 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a3eba34-9159-34aa-890a-f7f2064582ff | -11.55991 | -60.28065 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71eee1f4-9fde-3ffe-9fba-633349a402bd | -11.55711 | -60.27637 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9575984b-9a22-39b2-959b-ca6a5ccdbe17 | -11.55665 | -60.17274 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2af0a15b-715c-3f22-aecb-781331e042b7 | -11.5565 | -60.28009 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f126afed-3596-3488-9207-63d5aefc029d | -11.55604 | -60.17647 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fbc7fea0-1757-3a42-8055-25845d3d1cd5 | -11.55542 | -60.18019 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 75eba441-a9e0-3646-a82c-cab7234dd411 | -11.55448 | -60.16467 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 12c6ab95-e3dc-30b3-b04a-ac32fd342376 | -11.5517 | -60.16036 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0df3e044-c66c-30d4-876d-ab4de28545a2 | -11.5483 | -60.15978 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a128c85-7a85-355d-b2d3-b537fec5b2bf | -11.54769 | -60.16348 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60c4a2b3-d93a-3243-8f1e-e41df062185b | -11.5443 | -60.16291 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5edbc229-1c7b-3ed3-8e5f-498000c873be | -11.54366 | -60.16298 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92133409-d65f-3b0c-af71-0bd5ad5df275 | -11.54026 | -60.16242 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff37c7dc-5445-3b1b-a1ed-1f05df779b09 | -11.53686 | -60.16187 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e5ed0124-393c-340f-bf22-4c14f103ea4d | -11.53347 | -60.16128 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d6bfa03b-30f4-3784-abc6-46bf01997d51 | -11.53007 | -60.16069 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3fbe9c47-425e-3631-b48d-de22c390862a | -11.52947 | -60.16438 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 18420e99-d702-3407-97e6-1c7a47147b3e | -11.51927 | -60.16271 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ffc5c84-9789-3f8f-a337-131fbaeaf824 | -11.51867 | -60.16643 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 02a2852e-73ad-3988-9c43-673e504c3244 | -11.46873 | -60.45202 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cdc6d4e3-8a1c-3350-9add-ef8a5d4354f9 | -11.37455 | -60.63676 | 2024-09-28 05:10:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 462f601d-81d0-3c53-a093-b3a32142c688 | -11.3711 | -60.63615 | 2024-09-28 05:10:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 581149c7-d5da-31c9-b9dd-141a7b8727f3 | -11.3426 | -60.58064 | 2024-09-28 05:10:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ce7b1c7-7d13-35a8-b57e-017865b5ae4d | -11.3357 | -60.57941 | 2024-09-28 05:10:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4ed9504-e9ef-3a8c-8e53-a18ca5c74716 | -11.33444 | -60.58711 | 2024-09-28 05:10:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c4db279-c9a7-3f79-8cfb-51e243dc8552 | -11.33288 | -60.57497 | 2024-09-28 05:10:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30445a0f-0ae3-3240-b67e-7a9c85e69f9a | -11.33225 | -60.57882 | 2024-09-28 05:10:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 23e8c801-3358-335b-842e-cccf5050434d | -11.33099 | -60.58652 | 2024-09-28 05:10:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac6c33a6-084a-3def-b0cd-8fbe37c5dc6e | -11.33036 | -60.59035 | 2024-09-28 05:10:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 767edc00-365e-389f-870f-8828c9a00227 | -11.33006 | -60.57053 | 2024-09-28 05:10:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e91579dd-3674-37b8-aefa-6adbf45dcfa4 | -11.32943 | -60.57438 | 2024-09-28 05:10:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de85e9ee-ea42-326a-bae7-71875e4f23c6 | -11.3266 | -60.56999 | 2024-09-28 05:10:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d5745767-ad4e-3e89-8051-607269cefcfb | -11.31399 | -60.60355 | 2024-09-28 05:10:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d5b248d-b6ac-3222-9164-bb9337d7fac3 | -11.28851 | -60.60717 | 2024-09-28 05:10:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1952d170-fbbf-33d4-818c-691a057097c9 | -11.28505 | -60.60658 | 2024-09-28 05:10:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d554692b-2238-3efa-b16b-d203d3052cfc | -11.28415 | -60.59058 | 2024-09-28 05:10:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06f804ba-8ac9-3a2b-8121-8971b55a3576 | -11.28289 | -60.59821 | 2024-09-28 05:10:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 135c6dde-b85c-3712-b69c-08f6ae53eee9 | -11.27943 | -60.59761 | 2024-09-28 05:10:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13fd1da4-f393-3682-972a-aaf75ccc9797 | -11.26173 | -60.61856 | 2024-09-28 05:10:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 91845924-cca9-3dda-9a5b-2328a2fed90f | -11.25891 | -60.6141 | 2024-09-28 05:10:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ff9e2556-04ab-388c-9d87-fc7226775fe0 | -11.25825 | -60.61806 | 2024-09-28 05:10:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 29cee350-ed46-30a1-a9a7-94225cdbead0 | -11.2576 | -60.62199 | 2024-09-28 05:10:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae128d4e-b7a8-3599-b8b2-6e0dfc7d8ea5 | -11.25695 | -60.62585 | 2024-09-28 05:10:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d4a9cfb3-3256-33a2-bfff-38b1eea3ce9f | -11.25478 | -60.61757 | 2024-09-28 05:10:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea441b36-9aab-3ff1-92f1-979c43a620ea | -11.25251 | -60.61832 | 2024-09-28 05:10:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a4598d6f-74c8-3a8f-b92c-dadc980d15d1 | -11.25131 | -60.61701 | 2024-09-28 05:10:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2457011-8f55-39ca-a19a-deb65cf6d79e | -11.24904 | -60.61774 | 2024-09-28 05:10:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9fa47fb-9a30-3fed-9724-178e7cc1470d | -11.23587 | -60.48098 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 75bda3c6-8dd7-3f57-916c-8a587dba8b2b | -11.23426 | -60.3829 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9690aa02-2616-35df-aba3-e3a43dceaa11 | -11.23364 | -60.38671 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c310c800-315d-3ef4-86da-66628cba94c7 | -11.23305 | -60.47658 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c2c67793-5dd8-36b4-b972-7610c8b604e6 | -11.23242 | -60.48043 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b2f8af85-2afc-37a3-b546-2eec2b9a4d46 | -11.23174 | -60.6148 | 2024-09-28 05:10:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fd1f890-cfb4-35bb-856e-1c5f8a0601d2 | -11.23111 | -60.61864 | 2024-09-28 05:10:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ec56478-db09-3bcf-85e4-f10837c96610 | -11.23082 | -60.38237 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f94946cb-4c52-39bf-9181-8ae648b590e9 | -11.2302 | -60.38615 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1bbd7baa-6f66-360b-b081-74b708fab0b2 | -11.22739 | -60.3818 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f5c88bc-6a89-389f-aebb-586e08316a91 | -11.20653 | -60.6383 | 2024-09-28 05:10:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c96219e-1fc5-3aa0-8593-44eeb01f7ef9 | -11.19139 | -60.64368 | 2024-09-28 05:10:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f19a1c10-c0b0-3175-afe1-fdef8c1bf280 | -11.19091 | -60.19782 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 468c915c-d2d6-3a05-b55b-fadae2efa1d0 | -11.19075 | -60.64755 | 2024-09-28 05:10:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5a0e52f-7cb6-363d-8fa5-ab24f7bd5eeb | -11.18811 | -60.19352 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5198bbe6-fbdd-3746-8642-451aeb2bf039 | -11.1875 | -60.19724 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6702492-8f92-3767-8b02-cd761fc50a7e | -11.18469 | -60.19297 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7d479f4-5406-32f8-8403-2bdc9e43b1c9 | -11.16635 | -60.6873 | 2024-09-28 05:10:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c6a95b5-e93c-3020-bd16-584a4275fc24 | -11.16353 | -60.6828 | 2024-09-28 05:10:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d626ff3b-0eac-3b61-b37f-7baeef31ab19 | -11.16288 | -60.68672 | 2024-09-28 05:10:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15b75c04-537e-3dbe-bc5c-8f64ac8f580a | -11.1593 | -61.18977 | 2024-09-28 05:10:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61ee12b9-0230-3ed8-ae85-8266443b61ef | -11.15895 | -61.18813 | 2024-09-28 05:10:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ea0c4c7-6bf3-3820-9caa-b524e8fdebd9 | -11.15835 | -60.714 | 2024-09-28 05:10:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 49dc86e4-6c91-355b-9057-91a5b1e31142 | -11.15825 | -61.19224 | 2024-09-28 05:10:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a5b1015-54b6-3882-8b49-0f673aaf7ec9 | -11.1507 | -60.27243 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0ecceaa-ce2e-3833-a006-6f2c00c3d0cd | -10.9185 | -60.93462 | 2024-09-28 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 352d9352-fd86-3b5c-8eb1-1b77f0fa9b6e | -12.01978 | -61.22467 | 2024-09-28 05:10:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0df8e33f-46b6-3af3-ae80-26ddaf5793a4 | -12.01626 | -61.22405 | 2024-09-28 05:10:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a9e76bd-c1f5-3a7d-bb30-49174d401f9d | -12.01274 | -61.22344 | 2024-09-28 05:10:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c7c0474-bd93-320e-a683-7530ad37eae3 | -12.01208 | -61.22743 | 2024-09-28 05:10:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c497b4d0-c9aa-380e-87a1-c487fcffd120 | -12.00987 | -61.21882 | 2024-09-28 05:10:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 661ce50a-c821-3b32-8cbf-ae0d663f2480 | -12.00921 | -61.22283 | 2024-09-28 05:10:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a065e0a-bc08-3e59-97ef-782718cfb7b0 | -12.00635 | -61.21822 | 2024-09-28 05:10:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 559584ec-fd7b-319a-b345-a45cdb0c9af7 | -12.00569 | -61.22223 | 2024-09-28 05:10:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f7631dd-9281-33d1-85c9-fe2e73db5778 | -12.00503 | -61.22624 | 2024-09-28 05:10:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6656c1af-2fe5-3a86-98f2-a3e336dec67e | -12.00437 | -61.23025 | 2024-09-28 05:10:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6b76daef-8c48-3663-b7a8-19540e618e36 | -11.93757 | -60.3737 | 2024-09-28 05:10:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63d3b919-5591-33d6-997b-55d296a79a8d | -11.93696 | -60.37744 | 2024-09-28 05:10:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8bd7f05e-ae91-38bb-92a4-76af556afa1b | -11.93294 | -60.38062 | 2024-09-28 05:10:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b679256-d099-3b99-af96-8a95d3349a13 | -11.93233 | -60.38437 | 2024-09-28 05:10:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ef198d5-8182-37cf-b4e7-007c91695e95 | -11.81277 | -60.25746 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95675c5a-19f7-39d4-bfb5-e828a3a6eab9 | -11.80719 | -60.24881 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 927c9260-234f-3271-9a7e-f83d0b36ee7d | -11.80658 | -60.25256 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65501607-1a63-3cde-9e89-ddd31b5a8979 | -11.80433 | -60.69134 | 2024-09-28 05:10:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e06e3d38-41d9-3603-9394-476d59dfde98 | -11.77201 | -60.29279 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 493b9b13-21b3-3acf-bde5-ae3b1591be21 | -11.74922 | -61.32571 | 2024-09-28 05:10:00 | NOAA-20 | PRIMAVERA DE RONDÔNIA | RONDÔNIA | Brasil | 1101476 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6cefd513-5a1c-3dc8-aa27-2e492ac20eca | -11.67245 | -60.21469 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README90.md)
