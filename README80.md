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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b687233-9dc5-31b6-b566-51d437407546 | -2.02431 | -54.32491 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e8adda2-34ef-3b9c-9502-10a51d3a0bba | -4.44889 | -55.0111 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a3c9aa85-a809-3a64-aa7b-b2b4b7c9ddb3 | -3.50834 | -54.60586 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6d13f41-309c-3d8a-b912-f02f15e75c9d | -3.52504 | -54.65101 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2a31e511-bf75-373f-b17a-e549ef200616 | -3.02795 | -54.52361 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99216872-c9d1-3908-9e81-3f2fad3ef7da | -3.99718 | -56.24828 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ab4bc25-340d-3ca3-9a45-5c292d5bf39f | -3.15985 | -50.44453 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d797dff-959d-32c3-a880-cd9dff71f6fd | -3.05547 | -54.14979 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 482ceb8d-645e-342f-9f53-0ce04641e4de | -2.77678 | -54.10302 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 88d49a16-2d17-3778-9522-addfbe71ddba | -2.94687 | -54.14762 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1cb9eb9-82b0-358a-8f16-d49ec89f26f3 | -7.46528 | -47.59743 | 2026-10-07 05:04:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b75ad3a-74ec-3b3a-b09b-84bef3857a3d | -6.15209 | -51.73899 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2dcde4a0-9902-3bf3-a5b7-eaae77646eeb | -3.53159 | -54.65543 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2a6f8cbd-ebbd-3253-a542-658d81ffd172 | -2.99433 | -54.126 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c44daca-2086-395c-9c49-461c9c484c7d | -3.0594 | -54.38632 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c341853d-93cd-36f9-aedc-028a3742fb40 | -3.10072 | -54.18547 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc61090d-e9d3-3dfd-9b41-77b908699a76 | -2.90485 | -54.02243 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d17b39c-ffb5-36a1-a9d8-bc096a544c24 | -2.93633 | -54.1496 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| a8fb3566-a4ed-3e09-bc99-3ba2f170ae66 | -3.83923 | -50.3082 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2bdab43e-0ad1-3468-9433-fde5a82e0c67 | -2.93404 | -54.12053 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62133dde-6fed-3f71-9846-55ab510d2b4e | -2.99736 | -54.04001 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49056ebf-5c90-3c6a-87ff-424f16b70540 | -2.87584 | -54.14388 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5073803-9ec9-3d75-ad1b-10c966911f62 | -2.89707 | -58.45946 | 2026-10-07 05:04:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fbda347-d691-39eb-95f0-555258c0f74d | -3.27276 | -54.04289 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 54b5a365-a7dc-3bd6-983f-2cebefeee373 | -4.15513 | -55.15185 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15edd510-9d2b-3d77-9280-2c04ed64d941 | -8.71502 | -45.20103 | 2026-10-07 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| be9df985-198e-3c5f-8498-34d2accbcd30 | -2.99425 | -54.1044 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02d1bce0-1d43-3065-8650-7238c3ccf646 | -3.77002 | -59.32082 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8d85744-2874-3c29-a35d-e73f9fd0b425 | -4.95544 | -56.25759 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bff5b99f-339c-3941-a60a-1b4c31442c35 | -3.21364 | -53.87725 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 83710ca2-971f-31d8-8da6-e8eea3b90722 | -2.76562 | -54.08695 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| eba24e0a-2c17-3986-a1df-e077c5eee9e1 | -3.39004 | -58.20881 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08911f89-26dc-39ff-85df-3f31e6989126 | -3.6777 | -55.94272 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03849c4f-c8da-38cb-81dc-9421e10065d4 | -3.18552 | -50.56712 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 37909ada-61ab-393b-a549-5f0e6bc05295 | -2.9425 | -54.17564 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 443730c9-2d53-391d-98ea-69aff3c6478d | -3.73595 | -54.65145 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24d6d8ea-9abb-3e35-b497-6da001328d12 | -3.27202 | -50.41945 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 071c213f-f2eb-3909-a4b9-0a9fc2a5a3e4 | -3.29442 | -54.07499 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ae547af1-5d73-39d0-94c3-470360f8b9b9 | -2.78904 | -51.67044 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f47bdf7a-baf7-3a7e-bbb2-0b265dac8f1b | -3.00657 | -54.13509 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5befcefb-4c68-37db-ad00-2c1c44594952 | -3.09772 | -53.72409 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f7341a0-00cf-3f2b-b59e-6cf5068ac33f | -1.48435 | -54.84224 | 2026-10-07 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b4c3a61-2b92-3bc4-b710-5316624c9417 | -3.86129 | -55.98522 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 604d288d-ad47-337b-9cf2-03b4bfd64748 | -3.96591 | -56.05883 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f116cba8-3861-31d4-8a68-fea9b368050e | -3.06381 | -54.24786 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 28fce1ea-c5d6-3b2f-b987-120c3b1f0d1b | -3.42644 | -52.77448 | 2026-10-07 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 312d614c-842a-305f-99cd-f8012bb67bbd | -2.93513 | -54.11351 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79e61765-a5c5-3495-a958-39e94f1aa84d | -3.22154 | -53.88599 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dca58c41-b09b-323f-aec0-d6f67fb75379 | -3.03258 | -53.90051 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 923aaa5b-80db-36a5-9505-0557f232e3b7 | -2.99239 | -54.05007 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ae909a63-e208-368c-912d-5565d371b571 | -3.09165 | -54.28798 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c73d398e-ae2a-320f-9c17-3caf2138a18b | -3.60721 | -55.47672 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9c9e3f33-c710-3877-acfa-cf76bf0b152f | -3.36416 | -58.18827 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08f23ac8-a3bd-3059-9c75-018fd859c934 | -3.02253 | -53.89897 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0cf159e3-b5cd-3794-bd7d-db83ca7890c2 | -6.60885 | -53.0246 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf56c7f3-8e74-3d85-9c02-0440d870863e | -3.04672 | -54.20587 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce1d02bd-20ee-3e43-b89c-37ef626b0d61 | -4.26998 | -54.87318 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f43d054f-95fa-3458-bb1c-b210b3278d4a | -3.09895 | -54.15279 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b35b126b-7914-370f-9b02-469177ec156d | -7.75065 | -49.20503 | 2026-10-07 05:04:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c9148a73-00c5-3f42-9626-fb32fb3a0ad7 | -2.85282 | -59.11124 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8ba40936-a33c-3ca8-bc23-d10b0636f5bb | -3.04127 | -54.24084 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a760424-d504-3a51-9326-313f623b8d46 | -3.99441 | -56.2443 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d83d957c-f096-3827-a6ad-dfd53f09f32e | -3.0099 | -54.1356 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a62ba8c-0d91-3a21-93e8-8aba06da3cb7 | -3.53875 | -54.65298 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 75b5ddc6-1e69-300d-b781-40ceea6d3eff | -5.03532 | -50.01828 | 2026-10-07 05:04:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b851473e-9f79-3a76-951d-975d4e5412d5 | -2.85486 | -51.30371 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 672a8a05-1f3d-3669-b1e9-0fb51ed49a81 | -1.47358 | -54.5384 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 923c45e1-d750-3651-9299-203550f45793 | -3.65369 | -55.5092 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 091620b5-7660-398a-9e6d-bbc4542118e1 | -3.66731 | -60.63133 | 2026-10-07 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0d5dace-9803-38c0-b692-cfdd7e0e6754 | -4.04205 | -50.98474 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa72983f-48bb-36f3-9e88-81f2b1b7621b | -3.10228 | -54.1533 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de280352-8536-3351-b266-4f185cdb816a | -4.76033 | -55.65513 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44319cf7-e723-39e2-b757-acfccefcd006 | -3.48359 | -59.46289 | 2026-10-07 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b2020a5f-59bd-3424-8b01-b1174fb3250a | -4.96879 | -50.90668 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 790fb22c-f601-343d-82d8-aee75e6fa764 | -2.99619 | -54.1801 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 89ce2459-57df-3e84-b79b-aa3084912c09 | -3.0321 | -53.92587 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 048f41d8-5d78-3ef6-acc3-b35b7443eeab | -2.50173 | -56.12751 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ffec7ca5-b5f8-3117-8a81-eeda9e0bc707 | -3.93491 | -54.57582 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c58e41c3-69c0-37f1-845e-77b033309319 | -3.778 | -59.19737 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 822f0ddd-0fd5-381e-8ebb-7c2ed5251d60 | -3.4428 | -56.93724 | 2026-10-07 05:04:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d326eb9-c382-3fa1-9290-0e2409d45da7 | -6.92403 | -43.66135 | 2026-10-07 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 1c682625-853a-3319-a63b-eb4a8e21f4ca | -3.36771 | -58.18883 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 571a2339-ac9c-3694-91ad-5461fd74fdcc | -3.27706 | -50.14013 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 283901d6-b2af-31bb-91e8-cdef323f20d5 | -3.123 | -53.76102 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec544130-17e8-38c0-906b-6b08a6a609b2 | -1.29321 | -54.56322 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 299dca27-a78c-3610-bb45-573da582ef9b | -3.47686 | -50.08498 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 1136ebf5-95b7-3021-9ad4-845ea763a109 | -2.92743 | -54.14106 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8af907d2-250e-3680-9e38-c1fb2d18a32a | -2.49168 | -58.06222 | 2026-10-07 05:04:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c513b62e-2be6-3b63-b2e3-7f0012d672c3 | -3.30954 | -42.27773 | 2026-10-07 05:04:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37e49f0c-3157-3f0e-a1f1-d9a8a0c697c8 | -3.38002 | -58.2031 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d34682b2-f493-3333-9d79-5675356d2cb2 | -3.18165 | -50.56296 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 51e5a8d4-e970-35f1-9a5a-2906efa8e74e | -3.30092 | -53.86168 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 21929f38-3fc2-395a-b752-a63624f1b19e | -3.10395 | -53.77274 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7656f928-96ef-3a34-8cfe-234527c430a9 | -2.95732 | -54.10254 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 593fa809-89dc-3734-84ee-e7c064b0c4f8 | -3.38294 | -58.20768 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ddd002c6-3655-318e-836b-7e9afe403787 | -3.93437 | -54.5793 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50142110-8c3d-3f8f-92c9-6f3281ab1225 | -2.811 | -52.08561 | 2026-10-07 05:04:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 863bff8b-5107-3741-8dcd-737ff20979f4 | -3.46528 | -54.59922 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3166a30-30b9-33ba-ba05-e11d63ec5369 | -2.92295 | -54.12601 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7e70ec6e-5b87-321e-8499-998c8f393127 | -6.20288 | -49.38079 | 2026-10-07 05:04:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README81.md)
