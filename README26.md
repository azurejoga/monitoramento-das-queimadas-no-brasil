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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6d0644c-aea5-30b5-93e5-0a8a8ee6af7c | -9.43112 | -44.16283 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7f24ee65-b95c-30e3-9bd2-50a7cc32d59f | -10.6772 | -44.3275 | 2024-10-15 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c99ccaa7-5efb-3308-80eb-44096a6ae786 | -10.25942 | -43.97327 | 2024-10-15 04:02:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 93a87bf6-f49e-38b8-88f9-72a5fe8f3d6d | -10.12071 | -43.95157 | 2024-10-15 04:02:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ef87c46-afe6-3894-81cb-f3c84e248e51 | -10.09218 | -44.23145 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d8a2f2ba-5fd5-36a6-a726-34dac3696f16 | -10.09 | -44.22214 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 612e936a-eac0-3a11-982a-b8a82f8d03e2 | -10.08927 | -44.22649 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de1be1f2-e4df-3584-8446-cbf2dcffc0f8 | -10.08855 | -44.20848 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a42a059d-18f5-3383-b67d-fa85a3a4ee66 | -10.08853 | -44.23083 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f523c32-0c6b-3917-92cc-a27392a02b99 | -10.08782 | -44.21283 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 51005d40-cd65-3681-a267-a9068212ded6 | -10.0878 | -44.23518 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8463ddcc-e444-37e3-8f3d-065f3853f252 | -10.08635 | -44.22152 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 639b6dec-04f4-3c58-82e1-07b75c0762be | -10.08564 | -44.20354 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b7106967-1c50-31e5-9a7c-6fa62ac84a2a | -10.08562 | -44.22587 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c30c1cf5-b868-39bd-918b-73cefd7f94db | -10.08491 | -44.20787 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2d66009d-0899-3a02-ab65-67cf7405e67c | -10.08489 | -44.23021 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7cbb7650-e198-3c6b-8c6a-f66eafb45581 | -10.08415 | -44.23456 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5119e8d7-7924-364f-b751-8b1a914c2429 | -10.08344 | -44.21656 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4c24dfb-d8d0-33ce-bba4-8b322a42831a | -10.08272 | -44.19865 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c41efd61-936b-38c2-840e-8972297047bb | -10.082 | -44.20293 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90ec8ef3-aa6e-3e16-bd13-f4f509e2b1ee | -10.08197 | -44.22525 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82a67b87-a84a-3806-8672-45e30f5caeb0 | -10.08124 | -44.22959 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f948975-6441-3155-8880-c513ddabec26 | -10.0798 | -44.19374 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e6fc3e7f-a46b-33ac-bf55-a24b551ba812 | -10.07908 | -44.19803 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 018fee08-8541-3cdf-9a76-d0bdc5d110aa | -10.07686 | -44.23331 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8b82b39-cadb-3e35-99a6-bd7eb357d5b8 | -10.07616 | -44.19313 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 87e04411-8905-367f-90f2-91560da66502 | -10.06445 | -44.24001 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c4094d66-c1a3-3ede-834e-e41a52773546 | -10.06081 | -44.23933 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 29a79a08-bc9c-3b44-bcfe-a2715d95dd1e | -10.0603 | -44.17422 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95ed3d81-62a1-3b2b-84cf-01fc3369b498 | -10.05785 | -44.25673 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9e914404-0bcc-35a8-b4af-18eded808193 | -10.05724 | -44.17228 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9fbcd960-c61e-3ad3-93b5-3f0f30a51796 | -10.05711 | -44.2611 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0386c2f1-fd08-3a46-9649-16dcd3bcc965 | -10.05665 | -44.17365 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2614e41-010b-3e9a-868b-82a9067bab2b | -10.0565 | -44.17658 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47610603-4e40-3851-a6d9-1180e357432d | -10.05562 | -44.26984 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8162aa75-8b24-3173-89aa-8c3dc4919e18 | -10.04653 | -44.18964 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 15581a6d-3cc7-309a-894c-299f3749d426 | -10.04289 | -44.18902 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b24c17e8-c689-3b63-a84a-08169e8b59fa | -10.04218 | -44.19332 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1a723c2d-62bf-3bbf-8d54-58d9844ea3a4 | -10.04147 | -44.19761 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7eb7b650-c50d-3f4e-8df7-52a27aa3c616 | -10.04076 | -44.2019 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3fdb03d9-629e-3b63-b091-791b118d6edc | -10.04004 | -44.20623 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b3adf02f-d270-3c99-8222-d11906ffcd50 | -10.03712 | -44.20124 | 2024-10-15 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6be04ba5-f9f1-3f22-a72b-709085cad8ce | -11.06337 | -43.30404 | 2024-10-15 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd92b36a-a7be-300f-9fd0-7f978b44313b | -10.94547 | -43.75838 | 2024-10-15 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ea805ac-c735-30b1-bbdf-b9ff87a38fad | -11.05991 | -43.30346 | 2024-10-15 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 90b4b616-08ed-3afc-98f5-4a2f53f49e59 | -11.0693 | -43.88774 | 2024-10-15 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab204514-a791-3a86-a84b-3dfc75a8cdc8 | -4.0227 | -43.23953 | 2024-10-15 04:02:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26a04c76-0506-3dba-b444-3eaff2e4b218 | -6.50068 | -44.1459 | 2024-10-15 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f9d9e64b-9e3e-3055-8c57-d6a429155230 | -6.45194 | -44.2579 | 2024-10-15 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1a0796be-786a-3ac7-b147-a3fafef439fd | -6.45087 | -44.25509 | 2024-10-15 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 17896cf5-3a73-31c8-9f2e-1840267f9d27 | -6.41139 | -44.36105 | 2024-10-15 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e8aaba42-c54d-3baf-afd1-8ee400e17381 | -6.40752 | -44.3604 | 2024-10-15 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 29f5a271-2871-3dac-9cbc-4146a342b382 | -6.40034 | -44.74428 | 2024-10-15 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b649aefd-513d-3891-98cc-b71f94721fed | -6.37794 | -44.06824 | 2024-10-15 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3524eba9-411f-3476-9bf6-83e35753246f | -6.26608 | -44.96846 | 2024-10-15 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5dfb6992-c609-3794-be51-d227c4140bda | -6.26207 | -44.96772 | 2024-10-15 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1ff0449f-5d9d-33bb-9811-0448b81dadb1 | -6.14151 | -44.91568 | 2024-10-15 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 49e81dd2-475e-3513-bf08-b2fb00f7db78 | -5.85512 | -43.74647 | 2024-10-15 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2bde413f-adc8-3ebc-8e05-97658c08aeb4 | -5.85136 | -43.74588 | 2024-10-15 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 15d7249b-68ae-3217-849c-3333c42fc56e | -5.32234 | -43.37328 | 2024-10-15 04:02:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f527ec0d-abef-3387-b7fa-e484c4adae2a | -5.59288 | -44.89345 | 2024-10-15 04:02:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7ad09f65-1efc-3bfc-89dd-6f3362b682f0 | -5.58205 | -44.88032 | 2024-10-15 04:02:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 272b01fa-152f-3e33-9b5b-a039baaaed7c | -7.94916 | -44.52689 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b08b1643-e1cb-397f-a060-c7bf72ffea42 | -7.94838 | -44.53151 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36283f9e-12b7-3a54-814a-be1c4382ef9f | -7.94759 | -44.53614 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 323d28d0-3d49-3ff1-a36e-c31cfa09a84f | -7.93768 | -44.52513 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 11913e69-0a34-37db-8d31-22f1af52455e | -7.93687 | -44.52985 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f0f2c57d-5d07-3779-a970-15e739937ed5 | -7.93448 | -44.52714 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ef6f3dd4-4f78-3cab-a659-fc09ddc6c73b | -7.88931 | -44.53892 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fe92561e-b57c-38d1-8e68-1215a4ef0c88 | -7.88857 | -44.54337 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 38966eff-056d-3e4e-b304-8f1000301b38 | -7.87705 | -44.54166 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 23782e2a-af65-3a62-8cea-bfde7e30e881 | -7.87321 | -44.54113 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4ff18645-064c-35a7-91ea-007fc486155d | -7.843 | -45.24493 | 2024-10-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3cd14870-7447-3273-a488-7b95d4198108 | -7.76864 | -44.53966 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| deb8ebe9-bf06-3c59-a4e7-525cf7d4d63d | -7.7618 | -44.53344 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c3108b95-2729-3ed8-a798-5f3db060b524 | -7.76099 | -44.53828 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79f3b5b2-92bb-3e68-9601-4bed62e24a82 | -7.75758 | -44.89398 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6f99f191-7407-3de2-a4b4-316415da8a74 | -7.75728 | -44.89594 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8faa3a3b-0531-39aa-8f5f-0be196af91c8 | -7.75717 | -44.53759 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ca73dec1-311e-33da-9de5-3e452c16e241 | -7.75635 | -44.54244 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc1d43d9-cf83-329f-89c4-41652825a3dd | -7.75253 | -44.54172 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2fffa918-7275-31d7-83d9-f66d4aa8779d | -7.75172 | -44.54654 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e57d0e6c-db48-3b01-b0af-fd644ae2b8a7 | -7.7509 | -44.55143 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e5e6921d-1d5a-3b49-a9ad-5e57c3d2a468 | -7.65353 | -44.67207 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6329d2a-bf0b-3036-84c7-cf90d0bdaadd | -7.64967 | -44.67141 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 711db9a8-de2f-3c35-9666-f7c7dea5312f | -7.62867 | -44.67798 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 947f92ab-6185-324a-bc14-f35f65f266f3 | -7.61838 | -44.69178 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 46e24fab-d7ee-3604-acb3-c950c45b34bc | -7.58909 | -44.64472 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1c754e5a-46d5-3956-b2e2-c3694390fa35 | -7.56269 | -44.78143 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6904afb5-cee7-3ecf-9037-6dacaef483d6 | -7.40049 | -45.19096 | 2024-10-15 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7caa9a74-4dfc-332d-8bdf-c3c503fd20b9 | -7.39587 | -45.19382 | 2024-10-15 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c917c4b5-c6cb-3534-84f1-fee9ba116005 | -7.28461 | -44.97693 | 2024-10-15 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 06dca109-3a0b-3e65-baa8-671503a507a0 | -6.90297 | -43.96929 | 2024-10-15 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ee6b6c2-0337-36bc-8c66-b41588b20f20 | -6.89996 | -43.96413 | 2024-10-15 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4badb0ab-3232-3a0c-ace4-4dbf6d9bccb6 | -6.89922 | -43.96867 | 2024-10-15 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 887d5b6f-1139-3a35-bd13-f586fbf4fb20 | -6.84938 | -43.79588 | 2024-10-15 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5b7d64c7-b35f-37fe-83db-1239a11055ff | -6.98097 | -44.7183 | 2024-10-15 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a051e677-d78f-3986-b6c7-13a49c560466 | -6.94976 | -45.20771 | 2024-10-15 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3e67ce45-adaf-3943-97cf-4162e07b3a7e | -6.94917 | -45.21117 | 2024-10-15 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f02f7247-1932-3f7d-a877-0629cacc6609 | -6.94912 | -45.2075 | 2024-10-15 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README27.md)
