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

## Dados Diários - Página 179

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc2cf4a0-3e4d-3d3a-a663-e71337aa6961 | -9.4168 | -51.4636 | 2024-09-26 13:06:00 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 217.4 |
| 478ce71c-cbd2-305f-955b-cd9630b64fa7 | -1.57358 | -47.6757 | 2024-09-26 13:06:00 | TERRA_M-T | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| f9b434f2-abcd-3bd1-b61e-14532f77dbfc | -1.5661 | -47.68117 | 2024-09-26 13:06:00 | TERRA_M-T | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 41e32cb6-e44f-35bf-b2e5-51caf0133673 | -1.56062 | -47.53725 | 2024-09-26 13:06:00 | TERRA_M-T | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 01c4a5e7-889e-33d2-b291-f78ead41f32b | -1.55867 | -47.55084 | 2024-09-26 13:06:00 | TERRA_M-T | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| d0bbe34d-29d8-3741-a341-1fbbc6a5b88c | -1.36702 | -48.09698 | 2024-09-26 13:06:00 | TERRA_M-T | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 01f78148-382e-390f-b99e-3ee54420cbd1 | -0.99955 | -47.82408 | 2024-09-26 13:06:00 | TERRA_M-T | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| b68d51a4-a155-36af-b23a-496a3deafa66 | -0.99594 | -47.81708 | 2024-09-26 13:06:00 | TERRA_M-T | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 2397b3fa-1b44-3497-8198-e578b17a82a9 | -3.25766 | -48.46048 | 2024-09-26 13:06:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 880c97a3-9111-31c2-8e03-f9de7844189f | -3.14424 | -48.8305 | 2024-09-26 13:06:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| c14a7fdb-7e48-348e-ad23-cde1f396f3bb | -2.94462 | -48.49974 | 2024-09-26 13:06:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 3b240d60-be41-348d-8dee-571e402c06a1 | -2.53736 | -48.35041 | 2024-09-26 13:06:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 6764704e-dbea-3453-b5b0-fc9beee0b6d1 | -2.35596 | -47.60472 | 2024-09-26 13:06:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| e7ae393a-1ac1-3af0-bd20-8d359441453e | -4.86418 | -48.38009 | 2024-09-26 13:06:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| ef784012-3550-33d5-b582-4e31d7dc87bc | -4.62621 | -48.53418 | 2024-09-26 13:06:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 8c58e280-d190-3167-aac0-37f6256fd291 | -4.53138 | -48.7829 | 2024-09-26 13:06:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 47c0188a-dd73-3e60-aaa0-93b0b5c7d203 | -4.52964 | -48.79515 | 2024-09-26 13:06:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 125.1 |
| 7ca1eb08-69db-388a-bf5f-1adba646951e | -4.48988 | -48.11296 | 2024-09-26 13:06:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| e2b9e2a3-d8ee-3acf-80b6-c34087bb7533 | -4.18164 | -48.27053 | 2024-09-26 13:06:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 5e66ff27-1a35-3d5d-92fd-7bf7f7bccc90 | -4.03818 | -47.97842 | 2024-09-26 13:06:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 90b7dc05-53c6-3e57-8921-294d69cd0234 | -5.88141 | -48.08886 | 2024-09-26 13:06:00 | TERRA_M-T | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| af8a16aa-0d88-3b5f-b020-5f95b3540075 | -5.87941 | -48.10353 | 2024-09-26 13:06:00 | TERRA_M-T | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 44.1 |
| dd9ced10-8c3b-3566-af7d-c8cee580a006 | -5.26902 | -49.04956 | 2024-09-26 13:06:00 | TERRA_M-T | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 29e88f3b-bfad-3ce9-ac0b-fc1c14b54d87 | -1.2581 | -49.43702 | 2024-09-26 13:06:00 | TERRA_M-T | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 78348c55-cc60-371f-bbb1-2046b8389a6f | -1.08714 | -49.27554 | 2024-09-26 13:06:00 | TERRA_M-T | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| ef1345bd-40cf-3caf-877a-a7e1745ce41d | -1.08567 | -49.28587 | 2024-09-26 13:06:00 | TERRA_M-T | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 6a2abf0d-2dca-3fa6-98ec-6db4bfb10d3a | -2.95669 | -49.35656 | 2024-09-26 13:06:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 61922d80-6865-3dd4-9dd4-358c576ca262 | -3.31675 | -50.30609 | 2024-09-26 13:06:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| c45f728e-28dc-37fd-8988-42f39ee4b1ae | -3.31538 | -50.31581 | 2024-09-26 13:06:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 3c78136e-bc06-33ad-b3f0-7bd4f30ed37c | -3.24742 | -50.47721 | 2024-09-26 13:06:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| bb2e6da8-4839-32fb-8f57-6f138a2b3cc4 | -3.23235 | -50.31824 | 2024-09-26 13:06:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 37d9b1b2-43b8-3e6a-b62e-bf638667b493 | -3.16438 | -49.90324 | 2024-09-26 13:06:00 | TERRA_M-T | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 85fcbe88-2703-3d69-a1d4-8e7f3977f575 | -3.15663 | -50.46809 | 2024-09-26 13:06:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 2b8fa7e8-34f5-3feb-bc19-6157bd4edcba | -3.14431 | -50.28987 | 2024-09-26 13:06:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 740dba85-06e0-3f24-b476-6adc3fe80bff | -2.99717 | -49.78477 | 2024-09-26 13:06:00 | TERRA_M-T | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| aa42c305-842a-3978-9a0a-b3852534b472 | -2.88026 | -50.40158 | 2024-09-26 13:06:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| d9bceeff-7a8b-375b-8da2-162847c969e6 | -2.13349 | -50.15425 | 2024-09-26 13:06:00 | TERRA_M-T | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8fe9e219-fdb8-3335-be08-e23d16f31dd1 | -2.12426 | -50.15298 | 2024-09-26 13:06:00 | TERRA_M-T | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 715d6235-b412-3c0b-a059-700adbdd2393 | -3.56712 | -50.37316 | 2024-09-26 13:06:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 9f8d93b1-e930-3646-81a7-1a11c38b1983 | -3.56572 | -50.38285 | 2024-09-26 13:06:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| d4f54f8f-e8cd-3a24-8798-fa8d91f73f15 | -3.55786 | -50.37182 | 2024-09-26 13:06:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 9ffd23e0-a658-3f75-b6a5-d83d144f8445 | -3.55646 | -50.38157 | 2024-09-26 13:06:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 067d445b-a48c-3639-817c-090fea764951 | -2.18069 | -50.65313 | 2024-09-26 13:06:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 66f7fde0-1e07-3623-8b64-c9e3d1238fc3 | -2.17937 | -50.66236 | 2024-09-26 13:06:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| bc87406d-9a8d-362d-bac8-51d59bdefe53 | -3.30344 | -50.66487 | 2024-09-26 13:06:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 7cab6a0d-6f94-39bd-ad1e-9edad060af54 | -3.19879 | -51.13972 | 2024-09-26 13:06:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 887c253b-e003-3432-bab2-7a0c0d299196 | -3.1975 | -51.1488 | 2024-09-26 13:06:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 776c5783-0a44-384f-a135-1f3ff4899248 | -3.09495 | -51.2852 | 2024-09-26 13:06:00 | TERRA_M-T | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 9ae046df-5e20-30c0-9976-ee55730d34e6 | -3.02489 | -51.1309 | 2024-09-26 13:06:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ba2b7d9e-c85c-331f-a29f-7e757a09aa90 | -3.01238 | -51.08617 | 2024-09-26 13:06:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 4bd43038-aaf5-3e29-827a-aa88f9ec4aa4 | -3.00733 | -51.05768 | 2024-09-26 13:06:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| fe53a0e6-3202-35f5-8a1a-e06789752677 | -3.00339 | -51.08489 | 2024-09-26 13:06:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| bbfdb95b-a187-3446-8e5f-f1188e99604e | -2.89002 | -51.68071 | 2024-09-26 13:06:00 | TERRA_M-T | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 9f43aaec-fa44-3c88-9728-d7c0d635fcfc | -2.88875 | -51.68956 | 2024-09-26 13:06:00 | TERRA_M-T | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 4464876e-f471-3247-8ef1-57382ab3c984 | -2.88465 | -50.56642 | 2024-09-26 13:06:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 63551c33-30ad-3931-9c43-eeeab913977d | -2.87482 | -51.66053 | 2024-09-26 13:06:00 | TERRA_M-T | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 6ebbb160-2104-356a-a466-bf12f7560d3c | -2.87354 | -51.66938 | 2024-09-26 13:06:00 | TERRA_M-T | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 38d9fb1a-e7ae-315e-9d6d-360f2f08e1bc | -2.86594 | -51.65929 | 2024-09-26 13:06:00 | TERRA_M-T | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 93f39dc9-b4a1-3531-b4ea-f2ddab5d28a0 | -2.86466 | -51.66814 | 2024-09-26 13:06:00 | TERRA_M-T | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 2ddb8144-0169-384d-8c9d-dd42ab229f1a | -2.78045 | -51.48699 | 2024-09-26 13:06:00 | TERRA_M-T | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4f26342a-8b1d-3979-9c85-7e0b4353d4e5 | -2.74185 | -51.36655 | 2024-09-26 13:06:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| d99d8806-c03a-3653-abaa-e45595b692fe | -2.74057 | -51.37548 | 2024-09-26 13:06:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| ebdd53f0-71d6-3ab3-8586-33d786feff27 | -2.73165 | -51.37424 | 2024-09-26 13:06:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 97f62150-4237-3936-9c80-3c0722c8b341 | -2.59618 | -51.22435 | 2024-09-26 13:06:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| bb60bb9f-2b3f-31bb-96de-4ad2f9b778e6 | 1.21294 | -51.23218 | 2024-09-26 13:06:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 78700b7b-1ff2-39d3-9c5e-0b4a5e8fa269 | -3.39641 | -53.71688 | 2024-09-26 13:06:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 21d3ee15-d85c-35d0-8ba6-3c1ae45ca424 | -3.39504 | -53.72619 | 2024-09-26 13:06:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f457a1a9-9eda-35ef-b303-9514b257a3d0 | -3.33134 | -53.21565 | 2024-09-26 13:06:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f668e5e0-6e4f-3b79-b0da-2f26d64ffbeb | -3.33002 | -53.22472 | 2024-09-26 13:06:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| cc447858-aa15-390f-93e6-ee7d9fbfa16e | -3.32236 | -53.2144 | 2024-09-26 13:06:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 97834b98-1014-33ec-9d45-f5793248f18a | -3.32104 | -53.22348 | 2024-09-26 13:06:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| d8ab910d-6ca0-363b-a84f-0c7264195f98 | -3.3015 | -52.98177 | 2024-09-26 13:06:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e6ac20b7-1cb5-3cc7-88dd-fc627a76dd2f | -2.92287 | -52.91558 | 2024-09-26 13:06:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f2459f07-26ff-397d-8a0e-ce411cb0ce0c | -3.0192 | -52.18783 | 2024-09-26 13:06:00 | TERRA_M-T | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 4a29bc64-358e-3d08-afd5-bbc9f6dc0d34 | -3.01034 | -52.18659 | 2024-09-26 13:06:00 | TERRA_M-T | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 7fde28d3-36f9-3340-9a4b-695397ac77c2 | -2.61697 | -52.04379 | 2024-09-26 13:06:00 | TERRA_M-T | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1a6be753-eb8a-3fde-947e-c9f75062684c | -2.56274 | -52.28121 | 2024-09-26 13:06:00 | TERRA_M-T | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| cb7e8a18-e8ec-3e4c-b10d-26f1c6a6dd63 | -1.88956 | -54.8957 | 2024-09-26 13:06:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 225769ff-84ab-3a15-bd1a-30a10c9951f7 | -1.88563 | -54.71617 | 2024-09-26 13:06:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 4fd977ba-0c00-3ac9-a3ea-2ee39d68d8a6 | -1.88404 | -54.72702 | 2024-09-26 13:06:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 582fa024-6807-39b8-9b35-fc75f0657a91 | -1.87587 | -54.7148 | 2024-09-26 13:06:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| ce483189-e957-3168-bfe9-92e5fff50fd2 | -1.0513 | -53.35802 | 2024-09-26 13:06:00 | TERRA_M-T | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| efe40826-3ce8-342a-be2a-61c17ab886af | -3.35983 | -53.78243 | 2024-09-26 13:06:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 2a97d717-c9d1-39f9-8b41-c97a8a45b612 | -3.35068 | -53.78114 | 2024-09-26 13:06:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 79050440-0ca0-39af-9f40-46647bef796e | -3.30129 | -54.82576 | 2024-09-26 13:06:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 2807c211-356f-3f1d-9223-d62168d3612d | -3.27492 | -54.47373 | 2024-09-26 13:06:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5e991f08-d248-3f4e-9e23-44848503bc73 | -3.11854 | -54.67976 | 2024-09-26 13:06:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 154a5f07-0b79-3e97-a613-0c698d6ee516 | -2.9902 | -53.72422 | 2024-09-26 13:06:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7fc9b44b-02c7-3162-8161-bcc3a8af1f0b | -2.87276 | -53.96447 | 2024-09-26 13:06:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 858cce4b-3070-3127-8bf8-91d872e54904 | -4.50524 | -54.94623 | 2024-09-26 13:06:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 75c86554-294b-3144-ba29-dee88240b817 | -4.50369 | -54.95657 | 2024-09-26 13:06:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 83b3412b-55d9-3266-a396-b189118e2662 | -4.02441 | -56.19022 | 2024-09-26 13:06:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| e91b18e4-20c8-3106-bd0d-c9e7da8bc192 | -2.72574 | -57.50208 | 2024-09-26 13:06:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 74752d8d-5338-336c-b0ca-e2aa53ac6aa1 | -2.72321 | -57.51862 | 2024-09-26 13:06:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 41.1 |
| b7320148-9b1c-3d56-94fd-62f8e2ffef2c | -2.71755 | -57.51086 | 2024-09-26 13:06:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 3b27b832-e8b7-3625-baf0-e38e40804cef | -2.70324 | -57.52576 | 2024-09-26 13:06:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 6a4f99a8-20f8-30d5-9dcc-c63a7f77b2d3 | -2.66506 | -57.53723 | 2024-09-26 13:06:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 134.7 |
| d0b499ff-5321-38ea-a623-b927b98d7e0a | -2.66256 | -57.55394 | 2024-09-26 13:06:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 114.6 |
| e65097c6-7b1e-3309-b409-7b32d64908a0 | -3.01734 | -42.29852 | 2024-09-26 13:06:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 7f8dfab9-b67d-338f-ab3f-a3381544f830 | -3.0137 | -42.29117 | 2024-09-26 13:06:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |


[Clique aqui para ver as próximas entradas](README180.md)
