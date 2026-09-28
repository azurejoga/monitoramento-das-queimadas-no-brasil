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

## Dados Diários - Página 168

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b71ad5f6-d31d-3118-9064-df666bdabfb1 | -3.8866 | -51.96137 | 2026-09-28 17:11:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b233adea-eea2-3b7c-be97-e1038c57f4d7 | -2.08746 | -49.55307 | 2026-09-28 17:11:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dc183c01-26ae-3f7e-bf40-c35b69daec99 | -1.97122 | -54.25826 | 2026-09-28 17:11:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| f8a046d7-ca2f-3380-8071-907c3e4aebeb | -1.42812 | -52.58773 | 2026-09-28 17:11:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b3d8ab35-6737-3995-b595-b4d5607c368b | -1.42153 | -47.90995 | 2026-09-28 17:11:00 | NOAA-21 | INHANGAPI | PARÁ | Brasil | 1503408 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4878d16b-4cca-3c6b-bd86-852c09562d4c | -4.12371 | -51.07696 | 2026-09-28 17:11:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a0e7cb45-2896-38d6-a7da-3f933dbb060d | 0.69866 | -51.43105 | 2026-09-28 17:11:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 74b6e6e3-c02a-3671-8f86-584cdb8244a6 | -3.20715 | -42.45446 | 2026-09-28 17:11:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| a9019ac7-47d4-3ad3-8d4b-f4e0a88742e2 | -1.52173 | -47.9291 | 2026-09-28 17:11:00 | NOAA-21 | INHANGAPI | PARÁ | Brasil | 1503408 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| e9d3fe32-dd87-3828-aa0b-74a622771086 | -3.07257 | -58.00962 | 2026-09-28 17:11:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 197da1c3-b06a-3eb9-bea1-98292021d376 | -3.76009 | -51.33933 | 2026-09-28 17:11:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| b1c6fe85-3f46-3512-8539-fc7c91a3f8ac | 4.27023 | -59.82188 | 2026-09-28 17:13:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 353cd13c-c9ea-3973-af8e-b3f91f59dae6 | 1.73006 | -50.97603 | 2026-09-28 17:13:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 10.2 |
| a9efb45a-066e-3633-b993-706b0a380dad | 3.87895 | -60.88922 | 2026-09-28 17:13:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 30.1 |
| dbdfd267-9a23-3824-a817-9b48ffef4813 | 3.80857 | -51.56478 | 2026-09-28 17:13:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 028154d6-942b-376a-8ee5-9d8c2240429e | 1.85406 | -55.5801 | 2026-09-28 17:13:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2075980d-a51a-3ca4-8601-46f03a077d93 | 3.70215 | -60.20692 | 2026-09-28 17:13:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 48e10de5-eed0-3d99-b3c3-4742c7a05f45 | 4.41711 | -60.55309 | 2026-09-28 17:13:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9e84a124-af74-3721-9fff-60afd9d093a9 | 1.89934 | -55.57941 | 2026-09-28 17:13:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c554eaaa-a1af-3cb6-ba43-668208b63e3c | 1.84058 | -55.60044 | 2026-09-28 17:13:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 21c9d1e7-9d16-3ad9-8c13-2f0b63a955df | 1.7219 | -50.97041 | 2026-09-28 17:13:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 57f13fee-77ce-3b37-b91e-d73d986d5785 | 4.55529 | -60.17955 | 2026-09-28 17:13:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3f5f4b10-a235-3c9e-87af-dd88af0b8e27 | 2.44854 | -59.94258 | 2026-09-28 17:13:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b53cce80-3bd9-33b2-87ff-969b561ecaf7 | 3.69097 | -59.73341 | 2026-09-28 17:13:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e7532b36-e716-3b9a-9a4f-371f15750630 | 3.98438 | -60.12454 | 2026-09-28 17:13:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 22195d1c-570a-3763-ab9c-f815a1f8f588 | 4.102 | -60.90075 | 2026-09-28 17:13:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 1e4e91e9-5925-3531-be7b-19c60737833c | 1.87838 | -55.58009 | 2026-09-28 17:13:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f65df4a8-1d53-320b-a82a-2c60b8bef394 | 3.07617 | -60.4586 | 2026-09-28 17:13:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 2f844366-1b45-3a98-adc6-346416d7100e | 3.53213 | -60.14206 | 2026-09-28 17:13:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 3ac4bcb1-5cd7-38d3-a02e-35283908a923 | 4.49064 | -61.19643 | 2026-09-28 17:13:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7f66f36f-9bab-3220-ac31-6e5cf65fab95 | 2.03781 | -50.90725 | 2026-09-28 17:13:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 4c18518f-cf4a-365c-a677-d4040c41e1e2 | 1.85241 | -55.59105 | 2026-09-28 17:13:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1eb824f0-fb51-3596-ad05-b36bcc88895e | 1.84113 | -55.59679 | 2026-09-28 17:13:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 81962c1a-fd58-3ab9-ab74-6190cf2f08af | 4.06914 | -60.94621 | 2026-09-28 17:13:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 10.4 |
| e504f7e0-26a6-32c2-a07a-179820ad15ef | 1.47928 | -55.71947 | 2026-09-28 17:13:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| c310f7b1-9b57-3a18-a9b8-ce4cb7aa31be | 3.69578 | -60.202 | 2026-09-28 17:13:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 18750fa7-d6d8-39c7-9c67-7bfec85322ac | 4.26118 | -59.72302 | 2026-09-28 17:13:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5d9a274e-a2ea-3489-a9d4-1692429f3506 | 2.87981 | -60.29927 | 2026-09-28 17:13:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 34bcf683-6b81-3ec3-b1bf-cbdfaf716121 | 3.68703 | -51.72962 | 2026-09-28 17:13:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3313aea9-6644-3587-b752-8d2cb8b11f0d | 4.15568 | -60.8379 | 2026-09-28 17:13:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 0703ba53-4501-3944-b212-7a07bba38ba8 | 4.10659 | -60.91825 | 2026-09-28 17:13:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 18.0 |
| b7b37182-9931-30fd-b39c-843d9960afeb | 4.24639 | -60.22648 | 2026-09-28 17:13:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 9631076d-c936-3a7a-9748-afa138bbe521 | 1.90274 | -55.57992 | 2026-09-28 17:13:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| be21abe1-682d-329d-b8a6-5473dd8605da | 1.84167 | -55.59315 | 2026-09-28 17:13:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 5219a619-417c-3ad5-b514-d527bbce6be1 | 3.98841 | -60.12144 | 2026-09-28 17:13:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| feefa8bd-8467-302e-9568-005c82880db7 | 3.48261 | -51.48581 | 2026-09-28 17:13:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0f461b0e-176a-39e6-8dc5-159d3c6efdd2 | 4.26137 | -60.23687 | 2026-09-28 17:13:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 1761c701-ea3f-31c9-ad61-5ea73e32370e | 2.07605 | -50.74474 | 2026-09-28 17:13:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 40dcb582-0d24-336a-88c3-c97ca8edcabe | 1.82197 | -50.81397 | 2026-09-28 17:13:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bee2b881-a701-3ab0-8f07-92f8241bbd02 | 3.86381 | -59.97444 | 2026-09-28 17:13:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 87b154a1-cedf-3151-a65f-4b82b64166de | 2.68397 | -60.41681 | 2026-09-28 17:13:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 2dfdbd94-9623-34de-b06e-ecb722e7d783 | 4.07273 | -60.94676 | 2026-09-28 17:13:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| dc9205b9-e115-35a6-806b-08c909e020b5 | 3.69875 | -60.18273 | 2026-09-28 17:13:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e0c7e2d1-f04c-3fbe-896b-580d12af8ec6 | 1.87443 | -55.58323 | 2026-09-28 17:13:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d8cf94b1-6d9b-3808-9071-bb2548bb08e3 | 3.07555 | -60.46259 | 2026-09-28 17:13:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 914e9aed-904e-3dea-a093-7ef40413ce51 | 1.89427 | -55.58987 | 2026-09-28 17:13:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 58626a32-5954-308a-a1e7-783769936916 | 1.73445 | -50.97678 | 2026-09-28 17:13:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 3e2998eb-c231-3df3-bd9c-f31c8d99a387 | 3.07245 | -52.33363 | 2026-09-28 17:13:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c37887a7-fd3b-3849-b6b1-acd9e9dbff84 | 1.68468 | -55.95935 | 2026-09-28 17:13:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 48c539b7-cfd2-3b74-be21-9786a169df43 | 4.27372 | -60.14085 | 2026-09-28 17:13:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 12.2 |
| b3569afb-cdcb-3719-9cc5-bbc88c2a1b01 | 3.94276 | -64.33378 | 2026-09-28 17:13:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 0b3b0e30-591a-3e3f-9980-e3861b22b5fd | 1.8603 | -55.58478 | 2026-09-28 17:13:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| a1dfad26-972e-3ea7-aa63-15080f04eab4 | 2.45551 | -59.94365 | 2026-09-28 17:13:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 13.1 |
| a8ba4b94-5e51-30ea-ae8f-b73891576a5a | 2.45126 | -51.00279 | 2026-09-28 17:13:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 9411c6fb-9063-3cdc-928b-669d618288a7 | 1.7351 | -50.97251 | 2026-09-28 17:13:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 82752c63-f04f-3835-be10-60eb756954eb | 3.93027 | -60.63134 | 2026-09-28 17:13:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 6caa491f-d8ad-3040-9c4c-3b51e47a54e7 | 3.7063 | -60.17995 | 2026-09-28 17:13:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0ac2d9ec-ad91-327b-8650-0832760cc4ec | 3.69497 | -59.73022 | 2026-09-28 17:13:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d02782ec-85ec-351a-87ff-036f6ab05bae | 4.25104 | -60.21937 | 2026-09-28 17:13:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 42228f3f-16c0-322c-b5d7-abc5c97ee850 | 1.858 | -55.57699 | 2026-09-28 17:13:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| c6c5ceee-daa3-3ba0-a556-d64343d7fcbc | 4.31844 | -60.81495 | 2026-09-28 17:13:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 88c5b9f4-0bf7-338e-9151-c75f511ba14e | 1.87727 | -55.58741 | 2026-09-28 17:13:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| ee448a26-c7b5-3b7a-a3d5-afecb10e5dbe | 1.67044 | -55.91714 | 2026-09-28 17:13:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 89e4c20b-1cc0-3875-b463-bd3252a1b854 | 2.03715 | -50.91163 | 2026-09-28 17:13:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 7b1c3757-21c9-3571-b427-ac681f980a34 | 1.6541 | -55.89647 | 2026-09-28 17:13:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 29a6e0b0-2ed8-3dc0-b9ea-76b24ecdcdc1 | 1.8614 | -55.57751 | 2026-09-28 17:13:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| f32fd26e-8740-36e0-bcdf-a0fe892f7986 | 1.85351 | -55.58374 | 2026-09-28 17:13:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3b23a4dc-d6a6-3f2e-985a-7f96dfa47e05 | 4.27133 | -60.21875 | 2026-09-28 17:13:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 10.6 |
| dffd41cf-4045-38df-b740-8ac377bc936e | 0.64228 | -56.87255 | 2026-09-28 17:13:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 80558d96-26dc-38f1-8745-22482a705ece | 4.41772 | -60.54909 | 2026-09-28 17:13:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6af2916c-0d4e-30e7-adc4-0e086bf69be4 | 4.07632 | -60.9473 | 2026-09-28 17:13:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b1d01b5c-261c-3a9e-96b6-e0f4561c19d8 | 4.08896 | -60.89038 | 2026-09-28 17:13:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f19a7186-d559-3a69-97ef-e4577a37cec2 | 3.48629 | -51.5209 | 2026-09-28 17:13:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 21fcfee1-776f-3446-af80-ac47f3fb0a84 | 2.44681 | -51.00215 | 2026-09-28 17:13:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c7183b99-49ca-3335-8f57-7cf6254ebe01 | 1.83169 | -55.97844 | 2026-09-28 17:13:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fbf62a41-dde3-3b0e-b56d-35f0fb0065cf | 2.45143 | -59.94696 | 2026-09-28 17:13:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 13.1 |
| c9472e26-14a5-303a-8126-35b4bd869e62 | 1.83613 | -55.97184 | 2026-09-28 17:13:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| f64cd0e0-6809-3944-b6c1-bf304664213a | 3.39259 | -51.3032 | 2026-09-28 17:13:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7c87c0df-faef-3615-b242-0c9e4238e5ba | 1.86819 | -55.57853 | 2026-09-28 17:13:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| b1c13f64-fd5f-338a-b8fc-ccdeb2315de1 | 4.10595 | -60.92234 | 2026-09-28 17:13:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 59.7 |
| ded8ee71-0800-3695-b491-a986ddaed8a8 | 1.88005 | -55.56908 | 2026-09-28 17:13:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 63b0314a-bd03-39f1-bb59-c9ef092c1a92 | 4.27296 | -60.1411 | 2026-09-28 17:13:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 8da1d965-c34e-3d69-a442-39d693c42465 | 3.48635 | -51.49068 | 2026-09-28 17:13:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 522f015c-75ad-3157-94c2-efda204bfcb1 | 2.06705 | -50.74339 | 2026-09-28 17:13:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d962d404-2c4e-3225-9557-24d73ac5e0cf | 1.89087 | -55.58938 | 2026-09-28 17:13:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 329a714e-7685-3395-8a26-43f9188adb46 | 3.65064 | -60.17147 | 2026-09-28 17:13:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0b6e6a1f-0e6a-332f-aaaa-353e131475c4 | 3.54604 | -60.14418 | 2026-09-28 17:13:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4dfcfc47-add6-30f2-b622-10e89c76a00c | 3.41847 | -51.52818 | 2026-09-28 17:13:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 7c55e6da-5b63-376e-b5d2-53c2d4e09395 | 2.45306 | -59.94715 | 2026-09-28 17:13:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 3b7cee5c-2ab0-3cec-bc99-eaad870be975 | 1.88345 | -55.56957 | 2026-09-28 17:13:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |


[Clique aqui para ver as próximas entradas](README169.md)
