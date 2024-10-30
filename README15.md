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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8e7d8e5-2dc8-3517-af87-66045f544478 | -3.2798 | -50.3451 | 2024-10-30 00:52:04 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4c4c995-4ddd-3a5c-9e6f-0201b694c42c | -4.3588 | -55.1171 | 2024-10-30 00:52:04 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4ea31c9-65eb-38d2-8b98-f4193cd9398a | -3.2662 | -50.330799 | 2024-10-30 00:52:04 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e947957-4704-3939-9b30-1cc4f05e5d59 | -3.2681 | -50.339001 | 2024-10-30 00:52:04 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e389555e-f4d5-3bf5-b134-2c6625651070 | -3.27 | -50.347301 | 2024-10-30 00:52:04 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57f72bed-cfc5-3e20-adc6-8796b2ec4f9f | -3.6959 | -52.2603 | 2024-10-30 00:52:05 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d98840b7-3b61-3e13-8332-baf702bbce0d | -3.9735 | -53.626202 | 2024-10-30 00:52:05 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94229af3-5f56-3113-88c1-47546e24c887 | -3.0213 | -49.577999 | 2024-10-30 00:52:06 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74806408-6d7a-3cb2-bfe6-c16816bffbb1 | -3.248 | -50.565899 | 2024-10-30 00:52:06 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87b3d728-2825-3d1e-96ce-1e9165d9557b | -3.2498 | -50.574001 | 2024-10-30 00:52:06 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1704be57-5812-37ea-9886-a9725a61aec8 | -3.2516 | -50.582001 | 2024-10-30 00:52:06 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad9c8dbb-5763-3ff1-9c51-03d7c14c9ea6 | -3.2626 | -50.630001 | 2024-10-30 00:52:06 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcd278cb-0130-38ea-bf4b-4121fed16be1 | -3.2644 | -50.637901 | 2024-10-30 00:52:06 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 273d8bda-55ff-366f-b5e1-0ee68c849bfc | -3.6417 | -52.294399 | 2024-10-30 00:52:06 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06c75b19-1b45-329a-b156-890c6de851b5 | -3.1936 | -50.373199 | 2024-10-30 00:52:06 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cb30823-aca2-3894-aa35-71fb7687aa47 | -3.1954 | -50.381401 | 2024-10-30 00:52:06 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f3c32dd-c2f0-3e5b-b5e6-b578e16075fb | -3.24 | -50.576199 | 2024-10-30 00:52:06 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e2b1abb-1548-3a3f-8d13-fc824152538a | -3.2514 | -50.716 | 2024-10-30 00:52:06 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4896c74-8a30-3fbb-a416-4698bb3a2a02 | -3.2532 | -50.7239 | 2024-10-30 00:52:06 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d96f9d1-e622-3974-9edd-066454bc2c5a | -2.9718 | -49.541302 | 2024-10-30 00:52:06 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9000ffa5-9a5a-3d01-ab3c-9b1ce43e0d97 | -3.1874 | -50.571201 | 2024-10-30 00:52:07 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4af9d1d-be40-39ec-ade2-43e8c60ac1f0 | -3.1892 | -50.579201 | 2024-10-30 00:52:07 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 054df645-4ed4-3624-b264-5ec59eaec666 | -3.191 | -50.5872 | 2024-10-30 00:52:07 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64d87f14-484e-3c8f-9d0a-bd0f2b01ee9d | -3.1929 | -50.5952 | 2024-10-30 00:52:07 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e40746bd-baaa-3c03-acda-f1bbdd637ca7 | -3.1776 | -50.573399 | 2024-10-30 00:52:07 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e886ddf-85a8-37ae-9a43-4a1b4980c623 | -3.1794 | -50.581402 | 2024-10-30 00:52:07 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65e3ebb0-0c67-3361-a356-19fafd4d4f8c | -3.1812 | -50.5895 | 2024-10-30 00:52:07 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43c0bd00-f2cc-374f-92e4-5ac7e26b6561 | -3.2763 | -51.005501 | 2024-10-30 00:52:07 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89b49bda-c4f3-34f3-8bcc-4d1bdfdae2fe | -3.278 | -51.013199 | 2024-10-30 00:52:07 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33942be5-7304-32d3-9718-19f4df27ebca | -3.9849 | -54.135502 | 2024-10-30 00:52:07 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04189657-ab75-31a6-99f2-ddea3d95876e | -2.8574 | -49.223301 | 2024-10-30 00:52:07 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee99535c-932c-386f-8c7b-3ad500bc1def | -2.8596 | -49.232899 | 2024-10-30 00:52:07 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6adbc140-e207-3fb7-a5d9-a6925193b160 | -3.1678 | -50.5756 | 2024-10-30 00:52:07 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1092aaaa-3ee3-37c5-9c45-678419774b0d | -3.1696 | -50.583599 | 2024-10-30 00:52:07 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4037668a-1445-3036-a3df-bb6e3d3d8385 | -3.1751 | -50.6077 | 2024-10-30 00:52:07 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73dc0ce3-7616-304b-a9e7-99284f6a38f9 | -3.1769 | -50.6157 | 2024-10-30 00:52:07 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cca59ae-3e23-3cea-ab57-ebf813af913f | -2.6202 | -48.240002 | 2024-10-30 00:52:07 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fd1f8ae-535f-3002-b948-3327351b4c08 | -2.6228 | -48.251099 | 2024-10-30 00:52:07 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9abe197-ebfd-3631-9d3e-bbf7ad632894 | -2.8454 | -49.216 | 2024-10-30 00:52:07 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0414a09-9d5d-3e39-b5ac-9375c76b4786 | -2.8476 | -49.225498 | 2024-10-30 00:52:07 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a9f5fc2-15cc-3652-be89-0f18ad5e3c20 | -2.8498 | -49.2351 | 2024-10-30 00:52:07 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c7f7ba9-b5d2-3a47-adfa-fce655e89f2f | -2.9017 | -49.460499 | 2024-10-30 00:52:07 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55d7f78a-814a-30a7-ac92-c8aa061ff8a8 | -2.8357 | -49.2183 | 2024-10-30 00:52:07 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8694a3c-a119-31b2-86b8-8781f217e61e | -2.8379 | -49.227798 | 2024-10-30 00:52:07 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc7556a4-c951-3709-b2a7-c9a4b8b7c3dc | -2.8215 | -49.201302 | 2024-10-30 00:52:07 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 021cf410-51a3-3e68-b91e-565e0b85341b | -2.8237 | -49.210899 | 2024-10-30 00:52:07 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89d9252e-d62c-3c48-88e0-e2cf575830ba | -3.2388 | -51.021999 | 2024-10-30 00:52:07 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f055744-490a-3e78-b06c-882c3ef469af | -3.2238 | -51.001202 | 2024-10-30 00:52:08 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 729dbad5-f673-3b60-97aa-0149dd2c8fd7 | -3.2255 | -51.0089 | 2024-10-30 00:52:08 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8d5eb67-80f0-3bac-a5d7-5fe02dc7884e | -3.0662 | -50.402 | 2024-10-30 00:52:08 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12d31de1-b1f0-3180-995f-a7bf527b428f | -2.592 | -48.384899 | 2024-10-30 00:52:08 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12a8f9bb-f079-353d-8a23-bb324aa2542a | -3.0564 | -50.404202 | 2024-10-30 00:52:08 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e52f6644-6ae9-3cc5-9c0e-aaaf9a62c95a | -3.512 | -52.403999 | 2024-10-30 00:52:08 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ef27d67-03b9-3045-870a-1ba2e21db6bd | -3.5136 | -52.410999 | 2024-10-30 00:52:08 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c51dea8f-a5d6-3d0d-86c9-066d4e3fd354 | -4.166 | -55.313999 | 2024-10-30 00:52:08 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0833d3ea-8bee-385c-ab9b-4eb8baf86a72 | -4.1677 | -55.3214 | 2024-10-30 00:52:08 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92bdd59a-0182-3e93-8a7f-43e0e42ca75d | -4.0379 | -54.785999 | 2024-10-30 00:52:08 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 099bf8b9-d939-3a82-aece-3c57627eabf0 | -4.0395 | -54.793098 | 2024-10-30 00:52:08 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cf58f21-38c9-3a00-b26f-96b3aef6ee6b | -4.0411 | -54.800201 | 2024-10-30 00:52:08 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02bf6ed8-1ef8-3ab6-aaee-4c1a89fabfab | -2.8017 | -49.473499 | 2024-10-30 00:52:09 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32061741-7b67-39a3-bbe2-d395c4633872 | -3.1987 | -51.207298 | 2024-10-30 00:52:09 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be62a8e3-1d90-3fc0-9e4b-b7f32819cf20 | -3.2214 | -51.3522 | 2024-10-30 00:52:09 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 981f4645-aca3-3f25-9470-3f2c5dac957f | -3.2231 | -51.3596 | 2024-10-30 00:52:09 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 510c1cbc-6dfc-3c0b-b855-03b5cdba527a | -3.2248 | -51.3671 | 2024-10-30 00:52:09 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34124149-3eab-3bdd-87f7-1c52789713e5 | -2.9795 | -50.473202 | 2024-10-30 00:52:10 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54dae53b-b4b2-319a-a0f0-f2942af39117 | -3.1202 | -51.089001 | 2024-10-30 00:52:10 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5eecfd4-f497-3f8f-a597-6f84cd11b013 | -3.1219 | -51.0966 | 2024-10-30 00:52:10 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f1769bf-81a1-3d9e-8a3a-d309b88d91e1 | -3.4685 | -52.849201 | 2024-10-30 00:52:10 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c23cb0a1-9bc5-304b-a204-91676a33e849 | -3.47 | -52.855999 | 2024-10-30 00:52:10 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e329c494-8861-3d69-b726-cca1ee88d8e4 | -2.4532 | -48.495998 | 2024-10-30 00:52:11 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5eb45548-6dc4-35db-810a-bb4bb5325631 | -2.4557 | -48.506802 | 2024-10-30 00:52:11 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9684b519-6eef-3609-846d-d52d49209af9 | -2.4434 | -48.498299 | 2024-10-30 00:52:11 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee76c786-2532-3698-8d0c-3b2b2f44bc86 | -2.5344 | -49.072201 | 2024-10-30 00:52:12 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85b3bd6c-99b4-3142-a699-964bf5b9a440 | -2.5367 | -49.082001 | 2024-10-30 00:52:12 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd299217-d903-3f7c-8e69-4335e23292d9 | -2.539 | -49.0919 | 2024-10-30 00:52:12 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f84b097a-6a47-350c-a106-b9c968ae4d44 | -3.2424 | -52.169701 | 2024-10-30 00:52:12 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72b94c42-6be1-3b6f-8116-6af76194b616 | -3.244 | -52.1768 | 2024-10-30 00:52:12 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6f7a46e-ba08-37d4-862f-6159ba99c4f4 | -2.5269 | -49.084202 | 2024-10-30 00:52:12 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ee7787a-c08b-3afe-b980-5a74ae2599b0 | -3.745 | -54.627399 | 2024-10-30 00:52:12 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63c9bc5c-4e37-39ce-bbda-87314ab2ceff | -3.7466 | -54.634399 | 2024-10-30 00:52:12 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac336c47-0c0e-3357-9eba-2339f2c853eb | -2.3976 | -48.924702 | 2024-10-30 00:52:13 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 197fc626-305d-3a91-9b14-57ea6250e048 | -2.4 | -48.934799 | 2024-10-30 00:52:13 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f47195d-5d4a-3db5-8e00-ada24c43a2b4 | -3.0501 | -51.7771 | 2024-10-30 00:52:13 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cd674da-7d2a-3b1a-8538-12aa6ce24b48 | -3.9475 | -55.7649 | 2024-10-30 00:52:13 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 716e3681-5ec0-377f-87e5-cf712e0fca14 | -3.9492 | -55.772598 | 2024-10-30 00:52:13 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b619e59-9a75-3da1-8c81-6415d58d4c68 | -3.9509 | -55.7803 | 2024-10-30 00:52:13 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92533698-4e33-3b40-b07a-c03e429cb005 | -3.0387 | -51.771999 | 2024-10-30 00:52:13 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1af76991-324e-3b30-8129-81e289dc5d27 | -3.0403 | -51.779301 | 2024-10-30 00:52:13 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e9f2e19-8cfb-3779-a2a7-bb212ba45255 | -3.9768 | -56.035599 | 2024-10-30 00:52:14 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 380da4a8-2734-331f-ac6a-60503edead69 | -2.8901 | -51.3004 | 2024-10-30 00:52:14 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33c81269-5707-3ae7-b0a1-56e11fdbea0d | -2.9196 | -51.4748 | 2024-10-30 00:52:14 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90a707dc-213d-3e0f-8b9b-1c27f28cfe6f | -3.9023 | -55.977798 | 2024-10-30 00:52:15 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a146bf4-f435-3b1e-a60d-17ea9710e7be | -3.743 | -55.539501 | 2024-10-30 00:52:16 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03d2a87f-6b0c-38a0-aaf8-4eccc068fe1e | -3.2186 | -53.385601 | 2024-10-30 00:52:16 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdf79078-876c-3810-9121-13995383f3ca | -3.1204 | -53.041901 | 2024-10-30 00:52:17 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c6bff25-6f18-304f-b7f1-6436f65bd901 | -3.1219 | -53.048698 | 2024-10-30 00:52:17 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04d01a1d-f75f-3b87-9595-57cd96348742 | -2.4946 | -50.470299 | 2024-10-30 00:52:17 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecf9aa3a-4511-3df0-9423-f54e366f7b02 | -2.4965 | -50.4785 | 2024-10-30 00:52:17 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e57a595d-1d57-39ea-b212-17de4376c16a | -2.8296 | -51.940201 | 2024-10-30 00:52:17 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6dbcbda9-b07e-33d4-8672-c708fc4da528 | -2.8181 | -51.9352 | 2024-10-30 00:52:18 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README16.md)
