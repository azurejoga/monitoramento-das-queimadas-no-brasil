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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c921961-4124-338d-a9b2-a2d8a609243c | -2.6333 | -49.26337 | 2024-10-17 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f123fb5-e7f9-33bc-a6a5-324f9f5bf1f8 | -2.63275 | -49.26981 | 2024-10-17 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5db63a97-43ba-3546-a258-c8d8a5ab7143 | -2.6325 | -49.26863 | 2024-10-17 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3598fdef-a115-3fb6-b40b-41126ab8c729 | -2.62899 | -49.07279 | 2024-10-17 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5a7404e2-d07a-3e2d-8acb-8f0b9b5f3336 | -2.61248 | -49.4858 | 2024-10-17 05:27:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6ed9ae9d-69d8-3ba2-8f69-536d168b4c9c | -2.60786 | -49.48645 | 2024-10-17 05:27:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 7a85b6dd-b859-305a-b5fc-0a8b070fe69d | -2.60615 | -49.48485 | 2024-10-17 05:27:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 97e95b7d-83f3-3ae4-be3d-46235790904e | -2.60539 | -49.48989 | 2024-10-17 05:27:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 43b91cac-a7ce-3cbb-aa12-687ef7016099 | -3.22237 | -50.35922 | 2024-10-17 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 941de7cf-85d0-3567-829e-dc58edaeef55 | -3.21837 | -50.35563 | 2024-10-17 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e1588342-97b9-3149-9716-ff9e61d704df | -3.21775 | -50.35997 | 2024-10-17 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ce1af4ce-6c94-3c1e-8b3b-9bf46938dc1c | -3.21699 | -50.35392 | 2024-10-17 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 171fba1f-3963-3fd6-a23c-433ae9640a9f | -3.21633 | -50.35829 | 2024-10-17 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d6fd57f-9ee3-3751-bb8d-9b4f060ba37d | -3.18335 | -50.2042 | 2024-10-17 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9c92d49e-d822-39ae-822f-86d7f056dbeb | -3.07764 | -50.37216 | 2024-10-17 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a3cfaff7-0659-3e6a-90d2-4523ee8d74f8 | -3.07228 | -50.36678 | 2024-10-17 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a422c70f-1227-3cfb-a2dc-4151f7539804 | -3.07161 | -50.37126 | 2024-10-17 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f06cdcff-8d78-34f3-b4fa-a0cf1ac84421 | -3.07096 | -50.3757 | 2024-10-17 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e168bfed-cc34-3b2d-b18d-1bdca7a5cc91 | -3.06653 | -50.48787 | 2024-10-17 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90c69b9b-bccc-3b06-8576-f4c4ec573535 | -3.06626 | -50.36582 | 2024-10-17 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a0d6d5be-6bb1-3eac-b50f-19132b54eeba | -3.06588 | -50.49223 | 2024-10-17 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 76f3cc87-de62-3d99-b957-76788d84450c | -4.09579 | -50.75751 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 506907a7-1817-393d-8df9-8825870b5a35 | -4.09515 | -50.76194 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f24ae382-ecae-393d-8c46-3c1e632a87b9 | -3.65301 | -50.19685 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61ac6abe-fdec-32f1-8feb-ea1b4e842087 | -3.6523 | -50.20168 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60fc1e01-5077-3a9c-96b3-c54561776b90 | -3.64688 | -50.1959 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 947c1c45-3b8e-3fa4-9b01-be5d7158c71b | -3.58459 | -50.57607 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30d969d8-206b-367d-a354-51db7aa4f072 | -3.58056 | -50.56186 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96059ccb-535e-3d82-a682-0f946ac89ad2 | -3.57991 | -50.56632 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4bd45b4f-adec-3edb-a445-fb29682b68bb | -3.57926 | -50.57074 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2dc98db-07b2-311f-b479-4e55945688bd | -3.5786 | -50.57521 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b8efa67-c761-3a51-ba26-7937868bd1d4 | -3.57455 | -50.56105 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ef3f854-4da6-3874-8f0c-cb6d30543388 | -3.57324 | -50.57003 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 085c6750-f672-3023-8099-663c78e1ea67 | -3.67231 | -51.02075 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 603b8496-0f4c-3524-a102-8c2cd8587269 | -3.67172 | -51.02483 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30da52ce-bbd8-3fbf-90f2-b38bfaaba39a | -3.59778 | -51.00914 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86e22b73-803c-3dc7-8f16-af6ae40bcdc4 | -3.54489 | -51.29158 | 2024-10-17 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8cd53491-73e5-3c58-8202-8af727197221 | -3.53915 | -51.29087 | 2024-10-17 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a81101c6-473a-3946-b754-5674b4761981 | -3.51156 | -51.10998 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1f7a90c6-5af4-3392-a248-8154ad0837fe | -3.50635 | -51.10524 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5b28a9a0-df9c-3e20-bc93-16994f424083 | -3.50577 | -51.10918 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c7b46c34-2783-328f-a26a-06c065355381 | -3.50116 | -51.10036 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f15c3d09-d1fe-338b-96a0-cde0f98dc85b | -3.50057 | -51.10433 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8760d337-b9bc-3b69-8b55-684b541d3961 | -3.50032 | -51.67594 | 2024-10-17 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3dbb8372-6654-3424-b701-aec4aadeda85 | -3.49998 | -51.10832 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 025af58b-a3a9-3cba-9ca3-8e878595a603 | -3.49529 | -51.67141 | 2024-10-17 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3705b136-f6d1-3762-b95b-d78be95c9006 | -3.49476 | -51.67506 | 2024-10-17 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 26549b47-b75c-34d5-b4c7-a817ab82c10c | -3.49423 | -51.6787 | 2024-10-17 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 33b75b8d-6e7e-37c9-b820-88f207ef34f1 | -3.27114 | -50.66364 | 2024-10-17 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d2c6bb0-8aa1-3972-9ca8-f60bb5792032 | -3.15954 | -51.05285 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 24562898-9ea9-3089-8750-8299bbcc8024 | -3.08789 | -51.20981 | 2024-10-17 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d88222f5-a636-36c5-996d-b473cfe6673e | -3.08729 | -51.21378 | 2024-10-17 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec56adf1-459d-390d-9cf7-a62b0cba3734 | -3.08157 | -51.21302 | 2024-10-17 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b20b8a8a-b7f6-3870-8c10-fec8b3c9098e | -3.06501 | -51.04903 | 2024-10-17 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 019e2ecd-5b04-3a0a-b880-b2b2977bfd0c | -3.05984 | -51.04417 | 2024-10-17 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e530dcd-2d04-3811-b109-b00f1c6382d7 | -3.03312 | -51.22515 | 2024-10-17 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aca4b2ca-ba62-35fe-aa95-6e5b49daffdf | -3.03255 | -51.22902 | 2024-10-17 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12251800-4dde-330c-9426-52ccff635e47 | -3.02742 | -51.22432 | 2024-10-17 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 529a9766-85fb-33fb-b0dd-9934079bca6b | -3.02685 | -51.22816 | 2024-10-17 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7bb57f7-1817-37e4-a2a4-d0d036865113 | -2.99473 | -51.00739 | 2024-10-17 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 600f9cbd-ef55-356f-aba1-019a1cb70637 | -2.98895 | -51.00652 | 2024-10-17 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9d1d7ac5-a148-30e2-82f4-748f103b71dd | -2.98834 | -51.01056 | 2024-10-17 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f37dfa83-4d22-367c-9c21-a13635da4ffd | -2.89311 | -51.68223 | 2024-10-17 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d6336388-ad23-35fb-a0f3-300ee8904036 | -2.89256 | -51.68584 | 2024-10-17 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 01273d05-6520-3ee4-85e6-b51a6f99c29e | -2.89203 | -51.68939 | 2024-10-17 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7577119e-2498-367b-a752-5117f30c2223 | -2.88705 | -51.68498 | 2024-10-17 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6b50a940-3beb-34da-8e87-9cfeefbd341e | -2.88651 | -51.68859 | 2024-10-17 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4b62ede7-8cd4-3ff8-bc42-f53f3c1c8114 | -2.88209 | -51.68052 | 2024-10-17 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a06218ed-69f6-3122-942c-e744f9f3d07b | -2.88154 | -51.68411 | 2024-10-17 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa68d4f3-ad92-3ee9-910a-d3c0c0668792 | -2.88101 | -51.68769 | 2024-10-17 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4479baf3-32f7-3a13-b816-4b756c5807fd | -2.82098 | -51.33696 | 2024-10-17 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50e20ed5-8dd7-38d3-a24b-a26a94d7c770 | -2.82041 | -51.34075 | 2024-10-17 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4fa86c6-37a8-3e6f-9a95-c4dbb85f0ede | -2.81984 | -51.34455 | 2024-10-17 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| add2f125-bc1a-3686-a5c8-7cd2d24f2913 | -2.7021 | -51.72019 | 2024-10-17 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2ee19ed-6d27-3db8-8f3d-f7215dc1a97f | -2.70156 | -51.72372 | 2024-10-17 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9af1b3d-ba3f-38e4-b11b-56edd1565705 | -4.07128 | -51.11894 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9cb0e4d8-101b-38c4-bda2-7273bb731ed0 | -4.0707 | -51.12307 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6af2aac3-623d-38dd-b099-93fc1f73b35a | -3.88364 | -51.15329 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72582afd-1e1d-3241-ad05-52f5e20eef3d | -3.88311 | -51.15702 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c05256d-0a6e-305f-9fba-43a4e462992d | -3.88114 | -51.83193 | 2024-10-17 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e22d1517-bca1-3103-bbec-7b42ace78094 | -3.81301 | -51.15462 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e171643a-2bf3-3490-a501-ce73d0690f2e | -3.8094 | -51.29888 | 2024-10-17 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b9745cb-19d8-3658-87e2-9fb0a9b5533c | -3.80883 | -51.30272 | 2024-10-17 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33d309e7-e341-3c54-8288-ecb43f2fa396 | -3.80826 | -51.30659 | 2024-10-17 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7457c1e4-79f5-3292-8b6a-833947e33f45 | -3.80371 | -51.29769 | 2024-10-17 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 753d90b0-768e-339f-bdad-f301cf7023ee | -3.80314 | -51.30159 | 2024-10-17 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7882cdff-6c9f-3d48-8360-1947e371c177 | -3.80119 | -51.39352 | 2024-10-17 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e017ee9-bfc2-34d8-a44c-9b84ad5b22d3 | -3.79499 | -51.60835 | 2024-10-17 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 68dd16e8-d153-329e-82ec-95d7073bb673 | -3.79445 | -51.61217 | 2024-10-17 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35eb5086-a2de-3e31-979b-acefd953c80b | -3.78739 | -51.1273 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b8b22d3-50af-3c3f-8c93-1f5ae958a818 | -3.7868 | -51.13142 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9859573-4ddb-32d9-a559-2f64df76b9f6 | -3.77842 | -51.35028 | 2024-10-17 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e935d16a-3dac-38c0-812e-8ec93358a36e | -3.77784 | -51.35427 | 2024-10-17 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7ae7b53-9758-38be-85ce-df78b937c0f3 | -3.75381 | -51.93483 | 2024-10-17 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4baa5791-19da-388f-a900-bf34f9e7db21 | -3.74834 | -51.93382 | 2024-10-17 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 513a08be-c9ae-368b-a957-227f80e58731 | -3.70317 | -51.05423 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd9743a9-b1cc-30a2-a2ac-af1be65eccc1 | -3.70256 | -51.05837 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a9a4b1a-1217-3861-a908-e5545f906c81 | -3.70196 | -51.0625 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad8ed8e4-fd4c-3e01-bb96-6ed42094634b | -2.00605 | -52.10791 | 2024-10-17 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2011f982-3607-3595-a3ce-322aceff4a0c | -2.00504 | -52.10401 | 2024-10-17 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README51.md)
