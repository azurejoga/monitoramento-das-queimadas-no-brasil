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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64967302-ed2c-3aee-9f81-ea0f37ef0f2c | -3.09233 | -54.16934 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8561b493-b505-3430-b596-23b08860d9d6 | -3.09064 | -54.15837 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f88740d-9333-38a8-8fab-14426ae9e09c | -3.09009 | -54.16185 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 13c22d87-bfeb-3e99-a433-53b06d16303c | -3.08954 | -54.16534 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| caa893e1-70a9-30f2-8588-434a253dc375 | -3.08175 | -54.17127 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3176012-2dcf-3a6a-8faf-3448e950863f | -3.0812 | -54.17476 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 884bfa3a-78bc-367b-971d-d2009580e0d0 | -3.07841 | -54.17075 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 25bad549-e825-34ad-8cb0-f60cd8771200 | -3.07786 | -54.17424 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86e1aa9d-06ca-39ba-aecb-7bca8e04d5e1 | -2.73324 | -54.14918 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44efcbb9-67cd-3d6a-bdec-8e419589b647 | -2.49392 | -54.14079 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 93f95a02-841b-37da-aa9d-35735a3b0f17 | -2.49057 | -54.14027 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 83c9cde8-7e6b-38f2-a697-5bdd0faa02c2 | -2.97444 | -54.01533 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f618b056-589e-335d-b3e2-ba010128ca3c | -2.95718 | -53.86977 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1f387cf-cef4-3ea5-912b-2f827aad4485 | -2.94903 | -53.70528 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc12f131-6522-3d13-841b-f236f255fe02 | -2.9457 | -53.70476 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e65d6708-4a3e-35f5-b65b-5af967c8d260 | -2.94516 | -53.70822 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 317ebb23-c3da-3b0c-9112-305920b5fbe1 | -2.94238 | -53.70425 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 306d2ddb-fc58-35f6-be8a-6f16530575b0 | -2.94184 | -53.7077 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a0225229-a085-3d2a-93f0-bea7d3c62478 | -2.93677 | -53.91279 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3505010c-ed22-3d3e-9942-d5c58ee40191 | -2.93622 | -53.91627 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e900b98b-4a4c-3731-8e9f-30c44b462ec8 | -2.93403 | -53.93016 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2479f94c-c4f2-37ff-8f59-bb56d9a7a3ac | -2.9318 | -53.9227 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9191b9af-f3d4-3d92-9199-fc6f0bb36807 | -2.9307 | -53.92964 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85eb408d-41ed-33c6-a5a9-f15c4fae9c2d | -2.92847 | -53.92218 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e4c760b-8c35-358c-8c24-702ae27d0696 | -2.92737 | -53.92912 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b41e7db0-28c5-3926-9b0e-c7e082d1e18d | -2.92668 | -53.86861 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62ed41f0-ea57-3ad0-b5ff-f984b573c10c | -2.92613 | -53.87208 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 870d4262-731f-3460-b1b8-431d190fcdee | -2.92459 | -53.92512 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49026b5c-8d0e-30f1-9aaa-b9728383cca8 | -2.92016 | -53.93155 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6ca252c-31e1-31d9-bb26-b4eb9cdc2273 | -2.91629 | -53.93449 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25641ce4-f6ef-3cf2-9e63-c669e8730833 | -2.9135 | -53.9305 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d65061a5-0a85-399c-b233-64de6185f9bf | -2.83975 | -53.98667 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9edff496-b574-3407-913f-06d0baa07601 | -2.8381 | -53.98318 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a90472b-82a6-385f-a948-b2e109159667 | -2.80527 | -53.95316 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa07296b-eb6e-3ff9-96bc-6c48548a1a3e | -2.75818 | -54.03494 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2975157e-59c3-3a08-962d-b62d05bb7219 | -2.75484 | -54.03442 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a58f009c-823b-3a11-bc51-3984621835a4 | -2.75151 | -54.03391 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d3ed163f-cce7-3efb-be47-d550a32678b0 | -2.63942 | -53.96997 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97bc3d72-531b-365a-bc74-b4e0a6a55e76 | -2.57847 | -54.0177 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5933ba70-d281-3db7-b30f-5daa7f094276 | -2.57234 | -54.01317 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ad2cd14-790b-3e25-9b0e-f31daa43009c | -2.56845 | -54.01614 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8a4556c-4abe-37cd-b03f-a05a2e10c533 | -2.5679 | -54.01963 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f5a4a85-08fb-3688-a7b3-4d4449838232 | -2.56512 | -54.01561 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7285f565-a4a0-3740-8c93-7c77f591fc23 | -2.56456 | -54.01911 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b4834e2-09ba-3bb6-a5a6-93ab7d8e5a80 | -2.56233 | -54.0116 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 88604a1c-8921-38f7-8dce-bdc37133377e | -2.41904 | -53.80697 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30bda611-c764-31b6-99be-32c7ca2b9bec | -2.41571 | -53.80646 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a067b7b7-be65-34fb-a630-fac0829b1998 | -3.32982 | -54.18845 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e515805-2c2e-3a40-8488-b9823a8baf31 | -3.32927 | -54.19193 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37944463-0105-3755-97c3-e8117d7fb558 | -3.13867 | -54.2806 | 2024-10-24 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41251981-35a6-33be-8f6a-95d99a4df8bd | -3.13811 | -54.2841 | 2024-10-24 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78238159-a718-33b1-aa91-c276e09b2d86 | -3.13644 | -54.27307 | 2024-10-24 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5bbffcad-c116-33f9-aeda-0529c1b121ef | -3.13588 | -54.27657 | 2024-10-24 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0669c7a3-d197-3ec4-8320-4fe451415026 | -3.13533 | -54.28007 | 2024-10-24 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d73fcf15-58f2-3339-9e51-9e633ad4623b | -3.13254 | -54.27604 | 2024-10-24 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fadda776-9e40-3c30-8dfd-ecdc0965640e | -3.10069 | -54.18139 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6212f0e-901c-3e9b-9694-6729c0408348 | -3.09735 | -54.18086 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74d9c998-566b-3dda-b6c8-dd970b836b80 | -3.05085 | -54.85358 | 2024-10-24 04:55:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a6f7278-c41f-3658-a784-8087c051cd6f | -2.88915 | -54.48778 | 2024-10-24 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 33a9da3a-b785-316d-a713-14ebe1c0495e | -2.86147 | -54.59644 | 2024-10-24 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b20297d-5d50-3461-86c1-c2d6faa1c2fc | -2.79226 | -54.54503 | 2024-10-24 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f9d5ca1-03fe-3093-a85f-e18e86e5a6b2 | -2.73728 | -54.53688 | 2024-10-24 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cfddb78b-9e7f-37b9-b429-2d8aa60b5ff3 | -2.62123 | -54.51894 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a03ddba8-db8f-337a-b26c-dcc526437c30 | -2.56986 | -54.22448 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c740a9cf-a8aa-37f3-ac73-3098f8f2d7d3 | -2.55877 | -54.29494 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bfb8ae3e-7fd0-3dba-b251-bb229a22a7da | -2.48127 | -54.69926 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdba43a5-3e0b-3a98-bfe3-c003455040cc | -2.44138 | -54.57903 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 596ab9ff-6024-3eaa-9fe1-722666db22ae | -2.4216 | -54.28099 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0b135f75-c743-3b5b-984e-0a0ab0a2bda9 | -2.13764 | -54.90681 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a2be0c13-8f3a-356d-b801-146398cdd1d4 | -3.70684 | -53.92366 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f54d0343-5892-3979-9c83-91872de095e0 | -3.93105 | -54.53841 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39a39190-fb74-3e53-95f4-72a2d5f7d1b9 | -3.90126 | -54.14296 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e903e871-05a0-352c-a592-f2dbbaa22086 | -3.88906 | -54.1412 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b979fa0f-2f76-35af-9d41-df7539653198 | -3.88851 | -54.14468 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb941188-bfb0-3af9-b414-77284221963e | -3.88693 | -54.51344 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2378594-07d5-3570-8d5f-cf853d58843d | -3.88573 | -54.14068 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32686afd-bc4f-3197-8416-33c93a7707ec | -3.88518 | -54.14416 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9112e955-0aad-3ee3-8b12-5a4ff75ea0c9 | -3.88185 | -54.14364 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 209753f0-4231-3e26-87c2-6ccf4ae1f662 | -3.88022 | -54.55577 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76515dae-4fba-399f-9ad5-40fb31d577da | -3.8206 | -54.55379 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fbe2f11c-89e7-3e71-8dfc-03580ca144e1 | -3.8066 | -54.46856 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c606012-808f-32fb-a5ac-52c5191073c0 | -3.78205 | -54.42867 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d907f257-14be-392d-9b1f-93abbd768441 | -3.67857 | -54.54896 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9bad8388-8879-3a56-9c9b-9d2b5ff532dc | -3.67801 | -54.55249 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ba0ce26-0321-35fd-a96a-c77d8a358106 | -3.67466 | -54.55196 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04c4627a-0681-3458-94f5-3db455216431 | -3.67409 | -54.57724 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 562c53d2-54e0-3457-adf0-730db175a408 | -3.6652 | -54.2661 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e19957be-2e41-3abe-9f40-6d8b062ebf62 | -3.66464 | -54.26961 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| df5806ad-31b6-3321-8bc7-e1ebd86f07f7 | -3.66408 | -54.27311 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f3222d4f-b6b2-3dd4-8479-dfaf7b98e0b8 | -3.6635 | -54.4275 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23bf7404-434c-33ba-9455-25ceadc42f2c | -3.66186 | -54.26557 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c854bbb3-bfbc-363a-8ce5-3eafa274bc31 | -3.6613 | -54.26908 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 794d1b51-7068-35f8-aca2-915a86a31634 | -3.66074 | -54.27258 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7a644174-2654-3476-9109-d0cdd5920e8b | -3.65621 | -54.51657 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32510f85-6a29-307b-a0ef-d3c7ad04642e | -4.09445 | -54.29063 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a551d99e-0e6b-336c-b50a-851a3ed90466 | -4.0939 | -54.29412 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c9f0dfd-8cdd-3b1e-9081-96e6bdd24c2b | -4.09167 | -54.28662 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a2a331c-bb0a-3869-a1f5-d58667a2a23a | -4.09112 | -54.29011 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d986a9b7-2822-3ed1-b776-e15075d1af4b | -4.09056 | -54.2936 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26351469-dcb8-38ba-9d32-fe04392c027c | -4.09003 | -54.26162 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README72.md)
