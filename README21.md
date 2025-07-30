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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4981a720-64a3-36d9-8e6a-7f2b69c2eb9d | -6.6242 | -44.04772 | 2025-07-30 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9fc87693-dd75-34b6-b49f-736c63007e52 | -5.67458 | -43.67781 | 2025-07-30 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef5666c3-f77f-3227-82f0-849b0b8e4162 | -8.56655 | -44.32419 | 2025-07-30 04:27:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8767171-dddf-37b1-8408-0cb202262f52 | -8.02134 | -47.68513 | 2025-07-30 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 530ce23d-4272-31d8-a6ed-2bf19e297f44 | -10.62388 | -45.24421 | 2025-07-30 04:27:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b58e881a-cfec-3710-8f79-66b931e6ce85 | -6.54256 | -56.20073 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47a22fda-47c7-3085-87f0-257cd6cde03d | -3.58164 | -47.52141 | 2025-07-30 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2272cc43-7b7a-3b82-a4fc-1e1bca315e97 | -6.39291 | -53.35961 | 2025-07-30 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d9f2f20-591d-37b8-af01-579d4c165d66 | -6.67014 | -49.80462 | 2025-07-30 04:27:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40ec1f1d-3a51-3d51-bcae-fda6649b2d6c | -2.80571 | -48.66413 | 2025-07-30 04:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 310c2447-fc7a-363f-9ce4-cf937d7c747c | -8.07334 | -42.95412 | 2025-07-30 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6758a172-d7b3-3468-aa42-094be4cfb006 | -4.32395 | -48.39698 | 2025-07-30 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0b6b7b04-c8bb-39c4-96f7-dedc691b6e88 | -9.14512 | -49.84857 | 2025-07-30 04:27:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 99740c5f-ef0d-366b-ad47-10be5ef27442 | -8.02249 | -47.67802 | 2025-07-30 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2b58837-7757-3642-9efd-30fb3a6991ff | -6.89043 | -44.72796 | 2025-07-30 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf03b0f6-436a-3a77-9434-96dc7eb4f6df | -6.49627 | -56.1999 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| aaffcbac-36ea-35a2-b848-84de7848b214 | -5.76188 | -43.90561 | 2025-07-30 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02220a41-94a1-31be-806a-076966f70861 | -8.96011 | -46.74578 | 2025-07-30 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9d1cefb8-a611-3acf-9907-f685d795298d | -9.01844 | -47.97776 | 2025-07-30 04:27:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4751b80c-b599-379e-8702-1721a5cc60b0 | -9.04521 | -45.07585 | 2025-07-30 04:27:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 401e96e4-fe5e-3e5b-8dc8-11fc45f5470e | -9.26121 | -50.23339 | 2025-07-30 04:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f480720-d16a-331b-9d8a-03d69628b8df | -6.55778 | -56.19436 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 087f9b73-958a-3357-957c-54d8a3dbf393 | -7.13706 | -44.37095 | 2025-07-30 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 216614ca-22dd-373a-8d2b-ccb83bff7879 | -8.33099 | -54.75747 | 2025-07-30 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0178eda7-527c-3ec5-90c6-8a8d57761e57 | -6.56476 | -56.18788 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c418bf7-e82a-3c1c-bb2c-c0c7060aef18 | -3.49731 | -49.04901 | 2025-07-30 04:27:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6006123b-614f-3360-9001-95dfb6b7b1c5 | -6.5174 | -56.2117 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 651c7b82-7b8c-38bd-987c-8b60169d8249 | -3.18574 | -48.80573 | 2025-07-30 04:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a0eab369-e491-3c12-9ef2-fc0f6af365b4 | -8.62258 | -45.50671 | 2025-07-30 04:27:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41bb4012-e560-3309-8003-54fa08659b1f | -6.55915 | -56.18684 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dafc315d-de1d-3ac6-95cc-b192f0a24c0b | -9.86311 | -44.70969 | 2025-07-30 04:27:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bb23eaed-5d64-3633-831b-a3fced6cc45b | -8.40654 | -50.11556 | 2025-07-30 04:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 43a03c44-316c-36dc-9ae3-07550a61bf8a | -4.58493 | -48.0148 | 2025-07-30 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fb88916-6992-3c0b-90a4-d66eff71e276 | -7.63631 | -46.55612 | 2025-07-30 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 778e4ebf-095b-3a75-a232-322b4edc3262 | -6.95643 | -56.3843 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ac0a17c6-f26f-32a5-b058-aedcd073f7c4 | -6.54518 | -56.19981 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94874d1d-a0ae-35c6-b07f-b12dd560c255 | -5.39936 | -43.24501 | 2025-07-30 04:27:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 527faedd-afdb-33fa-9b94-80135c47f362 | -6.55708 | -56.19821 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8be2ad4f-dad7-3475-8479-956c7c2c8d0c | -9.74403 | -48.57539 | 2025-07-30 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c2b16fc-78a0-34a0-b83e-fde8f2a7b19b | -9.70709 | -48.21832 | 2025-07-30 04:27:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eae2e22e-fece-38c2-9860-b97dc1cac83b | -8.62595 | -45.50723 | 2025-07-30 04:27:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a53753e8-a598-3c7d-a368-1673c6b7cc03 | -8.67942 | -51.20931 | 2025-07-30 04:27:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46e1f00f-9131-36ab-a131-b108e75c80f6 | -6.23882 | -44.08823 | 2025-07-30 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d509c7a5-598a-3c60-b638-6548871515c5 | -7.10106 | -44.38126 | 2025-07-30 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be4c079a-d6d9-3493-b9f5-69d0ccb586f8 | -5.93214 | -42.56161 | 2025-07-30 04:27:00 | NPP-375D | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 599a1367-d677-3751-add3-f01b09b853d7 | -7.66336 | -46.51412 | 2025-07-30 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 541617bd-4828-3fe2-a2fd-f697049467c3 | -7.08567 | -44.50078 | 2025-07-30 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2d10248-50a5-3f54-9223-c3176fabb898 | -4.89619 | -44.95976 | 2025-07-30 04:27:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0f59782a-63e5-3ae9-9152-647d61f080f7 | -10.61073 | -45.23829 | 2025-07-30 04:27:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 01d0044d-cb1c-332d-b2ec-11d764e67804 | -8.59852 | -45.5287 | 2025-07-30 04:27:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b4f5ac54-0f8b-3495-941b-59caa618398a | -10.62102 | -45.23991 | 2025-07-30 04:27:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 20.1 |
| edd1f7b4-5af1-32da-b960-8022af0a17c7 | -6.39933 | -44.74637 | 2025-07-30 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18165349-ac5e-30cb-96fd-356d980fdc33 | -8.03076 | -46.90779 | 2025-07-30 04:27:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f74559a7-59db-3789-842f-33de9825effd | -6.50749 | -56.20208 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c51aa690-1c0d-3c2b-a0d2-f3e34c5d67c6 | -6.39877 | -44.74998 | 2025-07-30 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7fa8db08-5381-3fcf-a8c6-640fabd1d6f9 | -6.70151 | -42.04839 | 2025-07-30 04:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e83eb582-2e67-3e04-9edb-5e47d24afe2e | -6.69982 | -42.05033 | 2025-07-30 04:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 13492ab8-5a3b-3e3a-942b-f29703ec91b8 | -7.73715 | -51.09438 | 2025-07-30 04:27:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 36d29705-b17c-3ec3-8f54-51d1d450af87 | -6.88647 | -44.73112 | 2025-07-30 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 69fe2cad-a262-3d0c-a1e7-7b562c722ef2 | -9.26265 | -50.22478 | 2025-07-30 04:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 302c922d-99d3-3384-a40f-06cb5d0be681 | -5.67807 | -43.67834 | 2025-07-30 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 05a105ed-e957-32c3-a4f3-9e0d4f3b45b7 | -9.74344 | -48.57906 | 2025-07-30 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b43a984-34a9-3ee6-878e-9002d2b66b52 | -6.52438 | -56.2051 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dcfd34e0-de3d-345e-87a4-eebf43303e0b | -6.56335 | -56.18125 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b440a8fb-42ad-3567-abb9-3e52f59276ca | -8.01798 | -47.68459 | 2025-07-30 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ab123122-43cd-33f4-8d81-00178f626f76 | -10.61302 | -45.24633 | 2025-07-30 04:27:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d64aebb0-d454-38d5-b0d5-6a413f3f937b | -10.52866 | -42.55274 | 2025-07-30 04:27:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2e7297f2-4293-38f4-879c-f24f614d6c69 | -7.15483 | -44.0429 | 2025-07-30 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a597c4b5-42c1-3ef2-a339-300cc2165f5e | -9.1458 | -49.84443 | 2025-07-30 04:27:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| feea2a8f-da7c-3033-bac9-b6f1320cf577 | -7.78 | -45.00055 | 2025-07-30 04:27:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 98eea834-b526-3b66-97aa-9052add3873a | -4.03486 | -48.061 | 2025-07-30 04:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6df05edc-e408-3bca-9edf-ad0ab0474b13 | -6.45425 | -53.36532 | 2025-07-30 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 873a9bbb-ddfa-334c-a9c5-46ddc3e0a9f2 | -6.52865 | -56.21383 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aab8b278-35ee-390a-b79c-e7948cdaee16 | -6.4646 | -44.57031 | 2025-07-30 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0ce5ceff-febd-3a4e-98a8-a1b486bb397f | -9.23217 | -50.04623 | 2025-07-30 04:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bed9da0b-e397-37ed-909e-eb47060e8b67 | -6.55708 | -56.18396 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 963ee187-64cb-3f8f-a050-7000a994aec2 | -6.49355 | -56.21511 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d800734-e31e-311f-8dbd-dace240b33b4 | -5.7613 | -43.96652 | 2025-07-30 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7bf94d69-2777-3de6-8431-919f604820d8 | -5.40765 | -49.12153 | 2025-07-30 04:27:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71eb34f7-2ee5-3505-8d5a-ff57063b9704 | -10.62217 | -45.2324 | 2025-07-30 04:27:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| faa83bdc-df2e-3ea9-a5bf-40ac7ced5cd3 | -7.77222 | -45.86382 | 2025-07-30 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b49877f9-143d-3adc-9a07-37fe8e0db97a | -9.59414 | -46.32622 | 2025-07-30 04:27:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 39cf57b0-6cc3-3df9-b310-23567fb8bcc2 | -9.58159 | -44.44541 | 2025-07-30 04:27:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b357eb23-15ac-37f8-83b7-681a66f00439 | -5.24818 | -45.21546 | 2025-07-30 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10597956-df3c-3272-80f2-3cfdfb15f4ed | -4.64938 | -43.1291 | 2025-07-30 04:27:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 72e8b7a1-d712-31d4-8f83-b8ed2eb5327a | -7.94358 | -44.08637 | 2025-07-30 04:27:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a17239fb-3b9c-355f-8408-4e72c7c91242 | -7.93657 | -44.08527 | 2025-07-30 04:27:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36d1aec9-814c-3f0f-a7ad-e0632530e7e7 | -7.15053 | -44.03915 | 2025-07-30 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 751acfac-98a1-3c8e-b006-63c480a6cb37 | -6.51874 | -56.20412 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5bb1c4fc-b445-367e-9908-79fb6797ddf2 | -3.82481 | -41.56422 | 2025-07-30 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 59540f57-1251-395b-9a78-28aa1448be01 | -3.18505 | -48.80994 | 2025-07-30 04:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| df552ac1-d10c-3424-ad03-10a84225bcbb | -6.52638 | -56.19373 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c607374c-fd4f-345f-bb42-aa582984effe | -7.74106 | -51.09513 | 2025-07-30 04:27:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6f8d712a-9bac-3e57-989f-fafbedf5d674 | -5.76247 | -43.90183 | 2025-07-30 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7677a6cb-70de-33c9-bcea-e89f0e72a392 | -9.74657 | -37.00562 | 2025-07-30 04:27:00 | NPP-375D | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b88b36c1-1b8b-3602-b704-16a14312f821 | -10.61015 | -45.24204 | 2025-07-30 04:27:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| eeb29cea-7359-3d4f-ad6e-b10e1004e003 | -6.61889 | -59.98793 | 2025-07-30 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b3680b8e-150b-34be-9ed7-7ca24f731190 | -10.61416 | -45.23883 | 2025-07-30 04:27:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 060be698-0fd5-39c3-b647-54a1af2ffcd7 | -6.49919 | -56.21613 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4df5d9eb-3b53-3cae-93ea-2a3f1c3b896b | -10.51633 | -44.89191 | 2025-07-30 04:27:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README22.md)
