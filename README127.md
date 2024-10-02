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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25e3e22a-62aa-3b1f-b5f2-75e772d2506c | -2.60105 | -48.04068 | 2024-10-02 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7a307f2-5008-35da-9645-e9337be6692a | -2.59948 | -48.03475 | 2024-10-02 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 609c4319-ec69-36e7-88ac-c28afcda0f0a | -2.59904 | -48.03775 | 2024-10-02 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b45edd09-8ed2-37c4-bd02-5a6d45e04115 | -2.5986 | -48.04076 | 2024-10-02 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8dbe3ea4-0756-3d11-9622-724cff617e0d | -2.5964 | -48.03691 | 2024-10-02 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 497ab581-e3d0-3595-b87c-8821e4fa7ae6 | -2.59594 | -48.03993 | 2024-10-02 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36a2a661-6b49-3715-a945-1964a18dc9da | -4.57924 | -48.01085 | 2024-10-02 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5b5f52a4-05f0-39ab-9c99-76b907d4c123 | -4.57877 | -48.01408 | 2024-10-02 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ec64b17b-c905-3cbb-88b9-d15d56b8c4ee | -4.5735 | -48.01331 | 2024-10-02 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aaa9844a-b264-3a8f-8f49-a8f9d3b7096e | -4.56341 | -48.00851 | 2024-10-02 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0378e852-78b3-34ab-a3bf-1983abe12a39 | -4.55813 | -48.00772 | 2024-10-02 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c087ad07-7009-3a61-be8d-825418afc5c6 | -4.48858 | -48.11816 | 2024-10-02 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a85b679-cb17-33ce-baf3-4c40ed6ecdde | -4.48812 | -48.12131 | 2024-10-02 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6be41192-62b7-37bc-a1e6-aa4d2366cbaa | -4.28705 | -48.0722 | 2024-10-02 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8e30a585-146a-308f-b89a-4501d969ea0b | -4.28275 | -48.06514 | 2024-10-02 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48d3d645-7f66-3bf5-9a01-4c89a1c04503 | -4.28228 | -48.06832 | 2024-10-02 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b7dcc9e8-c47a-33dc-a664-9bcf0036a206 | -4.27751 | -48.06443 | 2024-10-02 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c63e7223-80a2-3fb3-a412-5ed13a80fb74 | -4.27704 | -48.06759 | 2024-10-02 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| edae0120-fdd0-3687-9d43-50344cdd6198 | -4.19441 | -48.23323 | 2024-10-02 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ced48d80-9b69-3e8f-a547-acd7719ff053 | -4.18929 | -48.23217 | 2024-10-02 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 407fc9fc-092b-3f6c-94ca-05f73717a8f5 | -4.15279 | -48.39823 | 2024-10-02 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 141f6c2f-83ae-3d0c-bea9-dab55d4ccf3d | -4.14404 | -48.40173 | 2024-10-02 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 43dfc3c3-4eac-3c02-937f-cee092e3d26a | -4.14362 | -48.40469 | 2024-10-02 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54629ccd-1352-3827-88dd-145a6332e830 | -4.14212 | -48.39981 | 2024-10-02 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 00c27fb2-902c-3a6e-80c5-21ba60a04e30 | -4.14167 | -48.40277 | 2024-10-02 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6b62e7ba-bc16-3c87-99a3-2c6a1b8cd305 | -3.30329 | -50.44814 | 2024-10-02 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37db4130-1008-39db-a579-d6c46bd49046 | -3.30266 | -50.44978 | 2024-10-02 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be05223e-a547-3d63-90e2-10970685bd7c | -3.14121 | -49.41795 | 2024-10-02 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fd0b7f8a-8568-3df2-a29e-721f62465294 | -3.14048 | -49.42289 | 2024-10-02 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e99b8e90-1784-33f9-bfe6-d63487e3c46b | -3.1399 | -49.41644 | 2024-10-02 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5c7cd8e9-2499-30b7-b46f-d1bb5298ee49 | -3.13976 | -49.42782 | 2024-10-02 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 97f90193-44ce-3667-9a25-32877ac5bdb9 | -3.13914 | -49.42139 | 2024-10-02 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b2e28476-9bfe-3ec9-bba3-f24faed7e208 | -3.13838 | -49.42629 | 2024-10-02 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 88c510b6-a5bd-3285-83ae-9b707df18436 | -3.13763 | -49.43116 | 2024-10-02 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ed4bc1f9-d012-3c13-996e-8ca37553e4f6 | -3.13725 | -49.41222 | 2024-10-02 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24f69626-db57-32a0-947e-7ae109b63866 | -3.13652 | -49.41722 | 2024-10-02 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 716fae92-306a-3149-bdec-419014c07f95 | -3.1358 | -49.42218 | 2024-10-02 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5e2b0606-e64d-3b89-81d1-fa7ffe2dfb9a | -3.13522 | -49.41571 | 2024-10-02 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 748aae01-1ff1-3b04-983b-8e5748754991 | -3.13508 | -49.4271 | 2024-10-02 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 835beff1-9559-31b3-beed-128478df37bd | -3.13446 | -49.42067 | 2024-10-02 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e3ba3b3f-633a-36b0-ae2b-45974cd387c9 | -3.1337 | -49.42559 | 2024-10-02 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 99fd235b-2691-3401-8e1c-ce8ddb581f12 | -3.13295 | -49.43047 | 2024-10-02 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c72deb4-9965-3c66-bc54-c3cfaeadf19b | -3.13184 | -49.41645 | 2024-10-02 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 49104a80-97a5-371d-a449-dcae8205a36c | -3.13111 | -49.42146 | 2024-10-02 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3793329b-30ab-35dc-82c8-6c5038e8d8ff | -3.12978 | -49.41993 | 2024-10-02 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ca5060f1-fe71-3909-98cb-f4cac1c73821 | -3.11722 | -49.40805 | 2024-10-02 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b9cb528-25aa-370d-8234-7b9b411d841e | -3.11252 | -49.40739 | 2024-10-02 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd6f91a9-daa2-398e-90ab-db5d065cfe46 | -3.11178 | -49.41229 | 2024-10-02 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79ea4966-27f7-3098-a504-def570aa7686 | -2.95911 | -49.36109 | 2024-10-02 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 720bec99-a265-3fec-9cbd-298eada5d6c4 | -2.95838 | -49.36602 | 2024-10-02 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 594a5f00-0128-309c-8e2a-464440877875 | -2.95442 | -49.36036 | 2024-10-02 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5161f799-7460-3aef-abe4-375e2489df8e | -2.87883 | -49.14881 | 2024-10-02 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 315d2e65-f74c-3495-90a5-e36057de7489 | -2.3942 | -50.32425 | 2024-10-02 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 890b99ed-9756-38e4-8eb3-a3b1ace157aa | -2.39357 | -50.32838 | 2024-10-02 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86d88370-97f5-3c42-b0de-5b4b05e189ee | -4.03862 | -50.38338 | 2024-10-02 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 094d889b-4ef5-3424-8e1f-b0058ef303e9 | 2.13647 | -50.91278 | 2024-10-02 05:08:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8e26604-3542-3be5-b263-83b60559c5de | -3.32371 | -50.78526 | 2024-10-02 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1f15a88-67a5-3cc1-b79b-279863df0c23 | -2.88406 | -51.68034 | 2024-10-02 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8c0f85d-f4df-3200-94ea-a781353a0eaa | -2.88086 | -51.67458 | 2024-10-02 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d036ad2-9af5-3bfb-9b6e-ce6ef9fcf7c4 | -2.88006 | -51.67973 | 2024-10-02 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac091708-31b2-3d64-a5f4-4ff49e90d006 | -2.87686 | -51.67398 | 2024-10-02 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01882cc9-cd56-3309-91b1-e6e5de849267 | -2.87218 | -51.65113 | 2024-10-02 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3123122c-d4fd-357e-86a7-44e660e3eaae | -2.69668 | -54.69405 | 2024-10-02 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0ecf2467-2753-353f-b2a8-4e6017a2c8bc | -1.50799 | -55.37626 | 2024-10-02 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f2add96-5079-33ec-aa58-fcf434c84df2 | 2.31085 | -61.28518 | 2024-10-02 05:08:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e056b6a4-33a5-343f-9ff5-d42f31fc982f | -9.31889 | -66.54492 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 947192fe-01db-30be-988d-289205ed6405 | -9.31833 | -66.54799 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27ce9cc8-318d-3d72-8394-e2e5ba8482f8 | -9.31211 | -66.55321 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b758eaef-7fda-311c-8c79-b5a8f8e468b4 | -9.31155 | -66.55627 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c6ac7cc-1cfd-356c-98cc-7e00eacd2f00 | -9.311 | -66.55935 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe07e651-8f65-3e6f-87eb-60d7e274f43e | -9.31044 | -66.56241 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 557a3e3e-9f45-3ce3-b10d-7b66506a58b4 | -8.88989 | -66.71673 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f65db422-e4cb-355b-aae1-8e5bcc950eb9 | -8.88945 | -66.71761 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9367e55-a459-3d66-be67-151d841b34f2 | -8.88931 | -66.71988 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d346974-e5ff-347c-b4cd-48342f5c8256 | -8.88889 | -66.72076 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4eebeb0a-ca19-3e6a-a440-a6512bb69962 | -8.76799 | -66.61642 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c00a2cb1-5acf-303f-8533-5a94e3f92c0f | -8.76743 | -66.61954 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f0d601a-1d38-34c2-a7b4-aa3b9aea2af9 | -8.76687 | -66.62268 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 006cc59e-d5cc-3484-9089-d21b63012578 | -8.76226 | -66.61853 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5fb218d6-5922-34ee-a068-f60138622906 | -8.76169 | -66.62166 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af4e04f3-73dc-34cb-9ff3-7bdc27f8a3d2 | -8.75651 | -66.62068 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b75da80-b868-3458-bde3-aad44b885db9 | -8.75595 | -66.62383 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3e30664-2ada-3256-ad18-e2adeb54d704 | -8.75134 | -66.61968 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e672afd5-05c6-38ae-9fdc-110a4199915c | -9.59207 | -66.50351 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6fa22eef-a813-3813-98ae-1ef9b5be292d | -9.59151 | -66.50655 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54bc6c5a-44c2-304a-ab3e-bb0f36890339 | -9.58644 | -66.50556 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be4dfca4-1167-350b-a9c1-1a24542b3574 | -9.58589 | -66.50858 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a9726240-4b62-3985-8913-22c24da7c859 | -9.55044 | -66.61418 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d807da25-018d-3049-8765-c3761ac9eec4 | -9.54988 | -66.61721 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a53e0e8-f53c-3aca-b74d-3e9414e3d1c2 | -9.54781 | -66.61584 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d34d7cf-5df8-313e-a010-8abba158681b | -9.54726 | -66.61888 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed7f51c7-3a73-328d-92e6-e3874bf09c14 | -9.54672 | -66.62191 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c543b9a7-440b-3853-8859-966c4b17b591 | -9.54533 | -66.61325 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93bc80e4-fee8-3793-a503-91c553a4e8c7 | -9.54477 | -66.61625 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8a7aee8-01a7-3039-83a8-b2142edcc63a | -9.54421 | -66.61926 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d73966da-1406-3496-9310-25e55abaf2ac | -9.54364 | -66.62227 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0379f1bf-4a7b-3dba-a0a3-c890ebdb678a | -9.5427 | -66.61486 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa2e2a40-2d34-33ec-a436-7c7872b7c044 | -9.54216 | -66.61786 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 062ce882-fa87-3e31-aa2f-487eb2657bbc | -9.54162 | -66.62086 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8e43c18-1192-3a74-97b6-5d1693dbad5c | -9.50091 | -67.11162 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README128.md)
