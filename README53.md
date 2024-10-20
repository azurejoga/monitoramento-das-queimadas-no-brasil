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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 759b7ef2-2470-3f57-80aa-0cbec9d156c5 | -3.82608 | -54.12594 | 2024-10-20 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9bac70dc-3dde-3d48-b681-3413c2aae422 | -3.69879 | -54.07009 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92510c7d-9c5b-3964-9cb2-3e6922a42479 | -3.68645 | -54.21341 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20def962-9d44-311f-bf35-b83b97b3161b | -3.68369 | -54.20944 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae4e51fd-4830-393e-830e-ddf02d425f94 | -3.68314 | -54.21289 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 164e8424-d0ee-3844-bc6f-a12d05c2d5ec | -4.07906 | -54.11584 | 2024-10-20 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eb04c85c-4ad5-3b1d-808b-87d065305527 | -3.97476 | -53.97965 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b611f6f5-cca3-31f2-b3f5-73dcce027203 | -3.8881 | -54.2491 | 2024-10-20 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a75dc57b-f97e-39a3-b3b4-566cf33d4e3f | -3.88479 | -54.24858 | 2024-10-20 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5c9f5081-2f43-3e7c-b931-2d01e4054003 | -3.85687 | -54.08126 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c20a1496-ea27-3bfe-ab7b-19ea3bdc2f32 | -3.687 | -54.20995 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39128042-b35d-3fba-8eb1-ecb9e271097d | -3.62716 | -54.67252 | 2024-10-20 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1451b08-b90a-3fde-a360-6cdb7442449a | -3.62382 | -54.672 | 2024-10-20 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9649b7a1-cd77-34d9-ac61-c3bbe9855ef6 | -3.61992 | -54.67501 | 2024-10-20 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ddfa1c1c-dc6a-3145-a6e1-60dbbf3447e6 | -3.61714 | -54.67096 | 2024-10-20 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 22ce75f7-eb09-317a-bae1-84b43730bca8 | -3.61658 | -54.67448 | 2024-10-20 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4912d6bc-7891-3377-b6f1-1993362294bd | -4.33148 | -55.44338 | 2024-10-20 04:55:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6756a23-dc18-3aff-bece-171d4dc807b9 | -4.3309 | -55.44701 | 2024-10-20 04:55:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39806206-90a7-384b-9afc-50320e08039e | -4.32976 | -55.45424 | 2024-10-20 04:55:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0ffbb2d-aa89-35ed-90c5-f6927c68c7e7 | -4.32809 | -55.44283 | 2024-10-20 04:55:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0da8ba0-818b-3f01-a6d3-8dbb9c880e79 | -4.32642 | -55.4314 | 2024-10-20 04:55:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 197ff5dc-8e05-31c9-8950-f76b2bb6447b | -4.26841 | -55.08898 | 2024-10-20 04:55:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a2f9ff8-b34d-30e1-aba9-78aa7b7724a1 | -4.26784 | -55.09256 | 2024-10-20 04:55:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d5f64c9-4831-37d7-ac58-e628dca91ac3 | -2.2384 | -55.06356 | 2024-10-20 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2baf3189-9926-32be-98ef-97d279a87b23 | -2.23783 | -55.06722 | 2024-10-20 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef7e235d-f831-3a49-9105-20b9ce8b7219 | -2.13839 | -55.2979 | 2024-10-20 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a5b25cc-13ec-3414-ba25-ebb00931c5e6 | -1.76009 | -55.14066 | 2024-10-20 04:55:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 562d7aa7-c913-3ccc-bc7a-af90f4e5cfcc | -1.75667 | -55.14012 | 2024-10-20 04:55:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e10ec032-d2e3-3462-9d0f-49866cc455c9 | -1.6878 | -54.99759 | 2024-10-20 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 446f3dba-78f3-34dd-86cf-d3ccf106b15d | -1.41341 | -55.00412 | 2024-10-20 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bacb5d22-2992-3668-9283-50ca337ea84e | -1.26276 | -55.9058 | 2024-10-20 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 331c6d7f-2194-3321-a677-dd7df8350ea1 | -1.25921 | -55.90523 | 2024-10-20 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6c2cc03-646f-324e-a348-7cd0527b6443 | -3.62232 | -55.44957 | 2024-10-20 04:55:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49629c32-8b4b-3497-8d9b-36f41bc2d1a4 | -3.59962 | -55.43843 | 2024-10-20 04:55:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2590d281-ad48-33e5-bcbe-dd7d3183b847 | -3.48465 | -55.43211 | 2024-10-20 04:55:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f6aead8-5cea-30a0-a104-62027e949288 | -3.48407 | -55.43579 | 2024-10-20 04:55:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37addd7b-433c-389d-ae4c-274fa556616f | -4.71788 | -56.14129 | 2024-10-20 04:55:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dea7b8b0-4eba-367e-9baf-0197f9ffa769 | -4.7144 | -56.14082 | 2024-10-20 04:55:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 61f4459f-1daa-36fd-bec0-17f9f1d8bb2a | -4.71379 | -56.14464 | 2024-10-20 04:55:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 343afa42-3957-3c1a-91b3-867870d23743 | -4.37415 | -55.68262 | 2024-10-20 04:55:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63569028-3141-3304-8f86-d23f6d51fa65 | -4.28142 | -55.6048 | 2024-10-20 04:55:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac5bdf1b-7cb2-3346-9387-3ad24852439c | -4.27801 | -55.60424 | 2024-10-20 04:55:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c3fe42c-2829-3f61-9f39-fcacc4af7216 | -3.93823 | -55.42645 | 2024-10-20 04:55:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c345eefd-bb74-3723-9bff-b9d20b17f531 | -3.19485 | -56.84743 | 2024-10-20 04:55:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 772745df-1efe-3753-8442-a9363daa7cd7 | -2.46381 | -57.53658 | 2024-10-20 04:55:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f40dbe2e-6a06-3e4a-9dcb-d24017cc7b50 | -2.4569 | -57.53064 | 2024-10-20 04:55:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b9fec705-6f76-3a8f-9a26-3a344e794af3 | -2.27959 | -56.83533 | 2024-10-20 04:55:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b2398ae-346c-3053-ad4d-81e8936565e8 | -3.05538 | -61.67362 | 2024-10-20 04:55:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20abe14e-cb97-36df-afb5-33d66179dac8 | -3.0549 | -61.67652 | 2024-10-20 04:55:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1695f930-b6a1-34ae-a59f-f5a3e6a00ab2 | -3.05442 | -61.67941 | 2024-10-20 04:55:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21ef2280-1562-3eb8-9bad-dd83b277655a | -3.05037 | -61.67276 | 2024-10-20 04:55:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 418ad961-5b6b-3043-889d-2f7507b79660 | -3.04989 | -61.67567 | 2024-10-20 04:55:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bbfff63a-8dd2-38cd-b709-f17da822119e | -3.03487 | -61.67311 | 2024-10-20 04:55:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2677a958-270c-33ba-bfee-c314421c7f06 | -3.01564 | -61.69792 | 2024-10-20 04:55:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a4f4fda-adf4-3b01-b82c-fa67232b8a29 | -3.01518 | -61.7008 | 2024-10-20 04:55:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8bec10c4-6af1-374b-9fdc-a0fffbd2d414 | -1.165 | -53.6571 | 2024-10-20 04:55:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 16144188-66fd-3daa-8e8c-815d1b541102 | -2.7773 | -49.3067 | 2024-10-20 04:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| ecf2a26b-ed7e-3496-903d-c4b1b8904af3 | -2.7958 | -49.3062 | 2024-10-20 04:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| b9915451-73ed-3bc4-b187-c8bbe45244ff | -3.0478 | -51.0226 | 2024-10-20 04:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 91286084-752e-3b64-b5c8-86cff8e42aba | -3.3998 | -50.6573 | 2024-10-20 04:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| d80eb1d2-42fb-3c4f-9d07-54d249aed6f1 | -4.1985 | -46.6318 | 2024-10-20 04:55:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 9f3a4f75-7d5b-3eb2-b7ac-60fd5d58ad33 | -12.07642 | -47.9905 | 2024-10-20 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cda7f5ee-e769-3c07-bc6a-545cd0873e0c | -10.16175 | -49.21442 | 2024-10-20 04:57:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8c8e0388-84ad-3e25-be49-e7e4deeac681 | -12.27475 | -54.54915 | 2024-10-20 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36b04a9c-9f45-35b4-ab88-dc45bdfaa864 | -12.27421 | -54.55273 | 2024-10-20 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0d01d6d-add6-36b9-a1a1-25ff3a95940d | -12.27142 | -54.54863 | 2024-10-20 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d04b45d-6fd5-30e0-b837-98997499e1ea | -12.27087 | -54.55221 | 2024-10-20 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04a6baae-3f98-357a-8f62-f8c84c155319 | -12.26808 | -54.5481 | 2024-10-20 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e43f0a49-6e97-3184-9e10-3f9f96f687d5 | -12.04418 | -55.3565 | 2024-10-20 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f26f2fbd-a452-30f4-a1d3-beff0d08d0f7 | -12.04197 | -55.34894 | 2024-10-20 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 364faca1-0f0b-3d3a-8caf-a18997dca6e3 | -12.03866 | -55.34841 | 2024-10-20 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7663b6f8-b244-3194-9425-70f58d9c3c4c | -12.40433 | -55.00702 | 2024-10-20 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52432594-194c-3bd1-8f70-2db4ff0f4178 | -15.95996 | -54.95726 | 2024-10-20 04:57:00 | NOAA-20 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5d7a14a6-497b-3371-a3e6-5da10989521e | -11.86259 | -56.87535 | 2024-10-20 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 349eb577-4300-3c16-abdf-9adf3c241f1c | -11.85131 | -56.88092 | 2024-10-20 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6435580d-41b5-3b6e-9807-443ced2bd812 | -11.84795 | -56.88036 | 2024-10-20 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62a833ca-205e-3919-92c1-bc70f3a62cb8 | -13.00675 | -55.97477 | 2024-10-20 04:57:00 | NOAA-20 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3d95c770-17ed-39b7-b223-76b6aed2e08e | -13.0062 | -55.97829 | 2024-10-20 04:57:00 | NOAA-20 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa348c0d-2d9e-3578-82d2-aa3a9a124e99 | -13.004 | -55.9707 | 2024-10-20 04:57:00 | NOAA-20 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 063eac87-eece-365c-b3f6-639a3dd4552c | -13.00345 | -55.97423 | 2024-10-20 04:57:00 | NOAA-20 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a7e92e5-cbf2-36f8-828a-ddad794115f9 | -13.00289 | -55.97775 | 2024-10-20 04:57:00 | NOAA-20 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 39275b8f-7fc3-3777-a211-7ed88eebdcac | -12.99958 | -55.97721 | 2024-10-20 04:57:00 | NOAA-20 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0560892e-c357-39ae-ada7-6e0ac13374c5 | -11.81704 | -57.36623 | 2024-10-20 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3e584727-2666-3fd8-8afb-07e5ad3ab82d | -11.81363 | -57.36565 | 2024-10-20 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7a5f44f-5e76-3891-b18a-44510e6a3638 | -11.61499 | -57.22873 | 2024-10-20 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1ed70360-66e3-33c2-88de-e28a61b7fcfe | -12.38756 | -57.63133 | 2024-10-20 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9123b52-5ed0-3e00-a7b0-4500e8ce3949 | -12.38693 | -57.63512 | 2024-10-20 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e499cd9a-26e6-3c71-9861-257007419b65 | -12.3863 | -57.63892 | 2024-10-20 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d388780a-0438-328c-93e8-cce91a465511 | -12.38567 | -57.6427 | 2024-10-20 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2f51d41-e1b5-3172-8d95-43adf096aad1 | -13.32022 | -60.38399 | 2024-10-20 04:57:00 | NOAA-20 | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f7ff086-bed1-3069-98bf-e6e48736477b | -14.28154 | -60.12456 | 2024-10-20 04:57:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52466e9f-7df5-32ca-9fff-f0d74bdd7c5c | -14.27776 | -60.12387 | 2024-10-20 04:57:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a82276f-e50f-349d-8959-5eff41889d0f | -12.28005 | -61.53709 | 2024-10-20 04:57:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e3d9892a-ab7e-3f55-9c24-0da0006eb72c | -12.27654 | -61.53226 | 2024-10-20 04:57:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d000d713-b9af-3b3a-ab73-c4fa69931c6c | -12.27582 | -61.53624 | 2024-10-20 04:57:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 269d7d73-8396-39ed-87ae-ebf2e25577d0 | -9.68677 | -65.2362 | 2024-10-20 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd348e8b-ad7f-3214-9d05-6d6c4c87ea63 | -9.6811 | -65.23507 | 2024-10-20 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 028b72b6-f7f8-3bf8-872d-d02af37a31d1 | -9.5811 | -64.70625 | 2024-10-20 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d701e4f5-c09e-3689-b600-1f806b6e45d8 | -9.58043 | -64.70988 | 2024-10-20 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2d5acda7-0b6c-3e05-8f3c-1476070ee325 | -9.5756 | -64.70522 | 2024-10-20 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README54.md)
