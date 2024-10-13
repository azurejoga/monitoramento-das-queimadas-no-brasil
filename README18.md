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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b555f0f0-bda8-3caa-a616-0efdb17386e4 | -3.1342 | -48.98 | 2024-10-13 00:59:57 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e458b309-61ae-3aef-ac66-ba9c64740a8e | -3.4381 | -50.156898 | 2024-10-13 00:59:57 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f242579e-0ccf-36fb-b79a-7b89f3562255 | -3.4398 | -50.164101 | 2024-10-13 00:59:57 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2b84e7e-dac5-3074-bea1-ab8e69505c3d | -3.9085 | -52.2029 | 2024-10-13 00:59:57 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f631a712-84f9-3216-8187-7a317ff3ec66 | -3.9101 | -52.209801 | 2024-10-13 00:59:57 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f3c491c-4f4b-3931-be00-6934065514a1 | -3.8987 | -52.205101 | 2024-10-13 00:59:57 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| beb0c5a2-c0fb-3e67-b77a-5a4e1bbb7c90 | -3.9003 | -52.212002 | 2024-10-13 00:59:57 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f49c334d-8f48-37fc-a04a-468e53d42789 | -3.1323 | -48.972 | 2024-10-13 00:59:57 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c02b9745-339d-3d85-a090-83b7932e63dd | -3.863 | -52.1842 | 2024-10-13 00:59:57 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ba78a44-af82-382d-95f7-c613ebcef060 | -3.324 | -49.931099 | 2024-10-13 00:59:58 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76e8db50-8482-3487-8930-d134b8c746c4 | -3.8074 | -52.391602 | 2024-10-13 00:59:59 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82bee3c3-595c-3c22-992e-01961fbac2e8 | -3.8089 | -52.398499 | 2024-10-13 00:59:59 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ba9074a-dfc4-3466-a9fa-61459b9ce42d | -3.5328 | -51.2384 | 2024-10-13 00:59:59 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 300f69d7-396a-30fd-b54d-a72663f53cc8 | -3.5343 | -51.245201 | 2024-10-13 00:59:59 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b650b295-f46f-372a-8ce6-ec5afa148260 | -3.5359 | -51.252102 | 2024-10-13 00:59:59 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21d419d3-5eb2-3ca8-aeb7-c50babe4008d | -2.6177 | -47.3409 | 2024-10-13 00:59:59 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35864dda-3625-3ec3-a16c-6491177be755 | -3.5842 | -51.507301 | 2024-10-13 00:59:59 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd62a9d5-3904-3b57-bcec-1836db38beeb | -3.5858 | -51.514099 | 2024-10-13 00:59:59 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78ba3391-99b8-3591-a59b-9a1cfa76bf04 | -2.6056 | -47.333302 | 2024-10-13 01:00:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 044a8017-bb52-3bf4-891e-2dfd89c39809 | -2.6079 | -47.343201 | 2024-10-13 01:00:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7746e4c2-2763-33a4-99a1-6c86e7afe711 | -3.7544 | -52.294998 | 2024-10-13 01:00:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d344217f-3ea5-385e-8ccc-f0da8e430ff1 | -3.7559 | -52.301899 | 2024-10-13 01:00:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3bd7478-a85e-307d-b11a-b8842c8bfb4b | -3.7748 | -52.384499 | 2024-10-13 01:00:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6106cae3-fe12-3cdb-b4f3-cc0f86782923 | -3.7764 | -52.391399 | 2024-10-13 01:00:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 347c90fb-59bd-3b07-9529-e420b3dd1197 | -3.7379 | -52.313202 | 2024-10-13 01:00:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fae2c519-5a03-32ba-85a9-4aab70c24d6c | -3.7281 | -52.315399 | 2024-10-13 01:00:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe110532-cc8f-34d4-9c51-7fea4cca61be | -3.047 | -49.403301 | 2024-10-13 01:00:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b36cabc8-6a36-3e40-9437-f999b001c0a1 | -3.0488 | -49.410999 | 2024-10-13 01:00:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90aa3815-d503-372d-ab62-73fb9fe70d67 | -3.7434 | -52.427601 | 2024-10-13 01:00:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e90e7f34-998c-32a9-b019-148599bf35e7 | -2.5259 | -47.256802 | 2024-10-13 01:00:01 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56609842-be56-33cb-bf05-e6868141b9af | -2.5282 | -47.266899 | 2024-10-13 01:00:01 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51547411-c658-3a2f-ac1a-a25d11293bbd | -2.5306 | -47.276901 | 2024-10-13 01:00:01 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32ef4cec-19e1-330b-a0ae-c0aa43857ba5 | -2.7509 | -48.396301 | 2024-10-13 01:00:01 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc42703c-2db7-3e5a-a2a2-147d98c266e3 | -2.7529 | -48.4049 | 2024-10-13 01:00:01 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f37ac1d5-fb6c-3a09-b77e-642306426759 | -2.9916 | -49.520302 | 2024-10-13 01:00:02 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0761a1e4-7d96-3008-b794-1afa95cda7a3 | -2.9934 | -49.527901 | 2024-10-13 01:00:02 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7de1ab34-b5ca-3750-8262-847c0c8744ef | -2.7904 | -48.698601 | 2024-10-13 01:00:02 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3271c18-2820-37ba-9975-2609e8440dcf | -2.9818 | -49.522598 | 2024-10-13 01:00:02 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d3282a1-f2d0-33e4-8e0d-ce917f8f4a39 | -2.9836 | -49.530201 | 2024-10-13 01:00:02 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2363c7a-ff70-3710-aef4-17368128ade6 | -3.1853 | -50.446602 | 2024-10-13 01:00:02 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee72812a-e946-3aba-bcc6-af92a5840a81 | -3.1869 | -50.453701 | 2024-10-13 01:00:02 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25270444-36cf-30e7-b62a-1e9742c06ad1 | -3.1886 | -50.4608 | 2024-10-13 01:00:02 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18901951-d2f0-3af3-b9d8-e69e93294f43 | -3.1755 | -50.448799 | 2024-10-13 01:00:02 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0946217e-9298-328d-b2b5-96eb03cb670d | -3.1771 | -50.455898 | 2024-10-13 01:00:02 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fa8aec3-c555-3c92-8aec-8ca7d8bd86ed | -3.1788 | -50.463001 | 2024-10-13 01:00:02 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87083f2e-4f43-3712-ac1e-def2c8ca0663 | -3.1657 | -50.451 | 2024-10-13 01:00:02 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56e587ba-48eb-3d7d-b81e-cc72ac538ef9 | -3.1673 | -50.458099 | 2024-10-13 01:00:02 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8323a109-ba88-3adb-903e-26151ea04243 | -3.169 | -50.465199 | 2024-10-13 01:00:02 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9934d241-0fc1-342a-af76-20f885028292 | -3.1706 | -50.472198 | 2024-10-13 01:00:02 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f93fd7e-ecc0-30c5-962e-ae72489ba83f | -2.792 | -49.282001 | 2024-10-13 01:00:04 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6318d73a-c99f-3f23-951a-b020328cb162 | -2.7938 | -49.289799 | 2024-10-13 01:00:04 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43f562d1-c497-324f-a959-4cec0a1baeea | -2.7956 | -49.2976 | 2024-10-13 01:00:04 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c643312-53db-3581-ba33-834b3d070409 | -3.3022 | -51.491501 | 2024-10-13 01:00:04 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcdf743d-479d-3896-b346-f2e2d1c9ee80 | -2.784 | -49.292 | 2024-10-13 01:00:04 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e68f991b-17e3-3535-9410-e6c436597dc9 | -2.7716 | -49.327599 | 2024-10-13 01:00:04 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8225632-6e3c-30ca-8511-42411c7c1d51 | -2.7788 | -49.358601 | 2024-10-13 01:00:04 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0cd74e5-3078-346a-bb6f-7ab17d7ce24e | -2.7806 | -49.366299 | 2024-10-13 01:00:04 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c182c50e-f738-36a2-8276-f22f10b60b9e | -3.5175 | -52.7472 | 2024-10-13 01:00:05 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b86ade39-c827-359f-8fcb-61ec3028ca8d | -2.7442 | -49.520302 | 2024-10-13 01:00:06 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64dee310-e70c-358d-94e5-487d12634557 | -3.3844 | -52.435299 | 2024-10-13 01:00:06 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 488cd0c1-4ad9-33fd-afd3-4a55dccd06f4 | -3.386 | -52.4422 | 2024-10-13 01:00:06 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c92bba0e-3ef8-3f6e-b7fc-20bdd6bfe4d8 | -3.438 | -52.941002 | 2024-10-13 01:00:07 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e0212f8-06b8-3d8c-a869-8e4496fd2ee1 | -3.4396 | -52.948002 | 2024-10-13 01:00:07 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2990a932-0cfb-3366-929f-fe72a4e299fb | -3.4292 | -52.7668 | 2024-10-13 01:00:07 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61926262-2e6b-369c-8796-7ed79b105151 | -3.4308 | -52.7738 | 2024-10-13 01:00:07 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f19f3344-8a87-3cca-b75e-b43557ee4595 | -3.6148 | -54.125999 | 2024-10-13 01:00:09 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99ff38a1-27ed-324d-9e7f-36fdc2abb2b6 | -2.164 | -48.797001 | 2024-10-13 01:00:12 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d04dc82b-a436-380d-9e3b-94f51aec3093 | -2.1659 | -48.805302 | 2024-10-13 01:00:12 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 144c5410-67d4-3313-9da2-731d44931fd8 | -2.1678 | -48.813599 | 2024-10-13 01:00:12 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27ec872e-b94c-3f5e-a514-5e9856761a07 | -2.1736 | -48.8386 | 2024-10-13 01:00:12 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6eb4492e-7632-3b75-aebe-4aa874e5eff4 | -2.1755 | -48.846802 | 2024-10-13 01:00:12 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cb1e610-07fc-38c2-a907-f1fc4eefd631 | -2.1521 | -48.834801 | 2024-10-13 01:00:13 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d0e2e8c-436f-3b28-b107-fe383ecffcfd | -3.2945 | -53.849201 | 2024-10-13 01:00:13 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58613250-f28d-3320-8495-fd0e078da796 | -3.2962 | -53.856602 | 2024-10-13 01:00:13 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f313e9a-af53-3ca3-809e-8814307d19c4 | -3.0963 | -53.0243 | 2024-10-13 01:00:13 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 107886b1-ce71-3037-9597-7356a9f48984 | -3.0979 | -53.0313 | 2024-10-13 01:00:13 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f867e488-637e-312c-9163-b4d3f8da2ede | -3.0995 | -53.0383 | 2024-10-13 01:00:13 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8522e806-730c-39b3-8f9d-f5f1cfa7d4af | -3.1011 | -53.0453 | 2024-10-13 01:00:13 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d517742-0bd8-3d6e-9637-2b271d1e0d11 | -3.0865 | -53.026501 | 2024-10-13 01:00:13 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3364af9-5427-3645-94f6-7f7973b9eae4 | -3.0881 | -53.033501 | 2024-10-13 01:00:13 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bd1f2b2-381d-3bd3-96a2-c031a9d30c9b | -3.0897 | -53.040501 | 2024-10-13 01:00:13 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a74e4969-43fa-3447-a1db-3826d7cca625 | -3.0913 | -53.047501 | 2024-10-13 01:00:13 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 578e8292-216f-38cb-9b14-9959f833a18b | -3.2486 | -54.1908 | 2024-10-13 01:00:15 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db4aa1e9-2cc1-3074-ac67-ce1fbc27cbb3 | -3.2504 | -54.198399 | 2024-10-13 01:00:15 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f013e37b-92ec-3f5d-a931-233ba6318235 | -2.6492 | -51.881401 | 2024-10-13 01:00:16 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0bd2361-be1a-3157-b7df-5910180e0150 | -2.6507 | -51.888199 | 2024-10-13 01:00:16 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf7cf576-5d0a-3206-bc90-5b3b33f375e9 | -2.2539 | -50.5667 | 2024-10-13 01:00:17 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c88a628d-fcc3-301d-9a22-9e3330d7c394 | -2.6829 | -52.433201 | 2024-10-13 01:00:17 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff04c616-e1aa-3319-a495-4675a0d0b29d | -3.0819 | -54.2276 | 2024-10-13 01:00:18 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9c795f4-d9b4-31f1-b3a0-7c8573b6c98f | -3.0837 | -54.235199 | 2024-10-13 01:00:18 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8807215e-9a23-3249-b214-c01395df803c | -3.0854 | -54.242802 | 2024-10-13 01:00:18 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8ebc863-3e77-3524-b51d-7d4e9eabf4ec | -2.9988 | -53.906898 | 2024-10-13 01:00:18 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78ffe218-58db-35ab-aaa1-9e0da3157eaa | -3.0004 | -53.914299 | 2024-10-13 01:00:18 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5542a79e-21f3-3e43-85a4-8d76844253f6 | -3.0721 | -54.229801 | 2024-10-13 01:00:18 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bfd4c5a-2029-3e09-a079-7d0363ef224c | -3.0739 | -54.2374 | 2024-10-13 01:00:18 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bab86499-9cc0-3243-a848-cf7a57914b47 | -3.0756 | -54.244999 | 2024-10-13 01:00:18 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79472ee4-5521-3cb7-9694-baf6c6f93be5 | -3.0773 | -54.252701 | 2024-10-13 01:00:18 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac9efa91-e067-31c8-a36a-ca24d827dcd9 | -3.0641 | -54.239601 | 2024-10-13 01:00:18 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0d95130-022c-3a8e-b1c8-3ee17c1262c7 | -3.0658 | -54.2472 | 2024-10-13 01:00:18 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 059ec9ce-ad02-3fc2-aaa3-4d5d3d7c63fb | -3.0062 | -54.0303 | 2024-10-13 01:00:18 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README19.md)
