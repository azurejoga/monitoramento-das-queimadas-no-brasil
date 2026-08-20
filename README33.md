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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 871e0f1d-b82f-3540-b0a8-07a36d0e63d7 | -6.34679 | -54.90602 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 04c7b2ed-e6fd-3dda-a059-db94914f7eed | -12.23652 | -43.15509 | 2026-08-20 04:19:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 04e94302-2260-3e98-b518-9b1bb74215a4 | -6.42101 | -52.76469 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 12ef8a43-eef6-3480-bb8d-b0091b4bbd63 | -8.56081 | -54.66749 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06646c65-7a4a-3ab8-9eb9-9df7f2f6cd80 | -11.81181 | -44.80631 | 2026-08-20 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| dd7c8e1a-3213-372f-8b2b-3cb43b603415 | -7.45159 | -47.17098 | 2026-08-20 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| abc07ce2-bb37-3a01-aade-569df978d694 | -11.69683 | -47.81462 | 2026-08-20 04:19:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc728c11-4ab7-3758-a130-4eaca2cd9a58 | -7.47587 | -55.31906 | 2026-08-20 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 95bbc77f-95e8-3d4d-aec6-42d8d5ebe23e | -6.33816 | -44.08233 | 2026-08-20 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f2d662f-e640-31e1-bd25-b5012181287c | -8.58922 | -54.74436 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9f10c3f7-cdac-3ef7-8b9c-42ebdeb09c8e | -8.47092 | -46.94351 | 2026-08-20 04:19:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ed90f05-f6cd-3f5f-98c5-9fbc9ad722c0 | -12.25917 | -43.15075 | 2026-08-20 04:19:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 808271ca-1e33-3223-b869-46b044871297 | -8.55573 | -54.66203 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c3ec1af-8db1-3e30-964c-db6dc55b1d88 | -7.45886 | -45.14647 | 2026-08-20 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d63e5e5-ad54-3576-a1b9-f0aaf8f644f2 | -7.11872 | -47.49436 | 2026-08-20 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 257d3637-8a4d-3012-bc05-0cd6b3472b07 | -8.66566 | -54.65108 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 4c4ffad8-5ace-32a3-ab63-b450c6b4abf4 | -10.83457 | -50.3018 | 2026-08-20 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68a3e359-2cf1-34d8-8daf-108ffd41d3aa | -7.34606 | -45.8223 | 2026-08-20 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| fe8ac508-324e-3789-b71f-c4ca94c78eb8 | -8.66485 | -54.65529 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| fd096f61-6ca1-38e9-9116-27afe6b97399 | -6.3477 | -54.9011 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e4f30389-a159-3f0a-8782-48fe19e8b688 | -6.14212 | -47.23038 | 2026-08-20 04:19:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17431a00-3eff-3867-b830-860d16e5d4e4 | -8.66646 | -54.6469 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 417aa2f2-2506-3311-bc5a-cf598808d1af | -7.97161 | -44.66218 | 2026-08-20 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2952216d-7fa9-3e68-9e5b-88c3404ff2a5 | -8.10498 | -51.66245 | 2026-08-20 04:19:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fe7ef6a3-b234-31b6-b39b-1b740a4bb3cd | -6.43592 | -52.72195 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 13e2d557-5bb2-324d-982f-30d91affb97d | -8.52142 | -54.87415 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a74daa2a-6cc9-3982-a579-59ab71105ce4 | -10.83811 | -50.30666 | 2026-08-20 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 776b7c13-98b0-364f-83c9-bbd06a3699dd | -9.12833 | -51.15207 | 2026-08-20 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6b80d0f1-e43e-3965-9203-b0908ad74a19 | -11.31893 | -45.21019 | 2026-08-20 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 59369834-0505-32f5-8cc0-1a1c82319bf1 | -6.51992 | -43.62334 | 2026-08-20 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4fe1fb08-6006-3c08-b5df-332c55c67eff | -6.43406 | -52.7323 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 059836ad-d2a8-34a2-a9cc-16afb0da5e6c | -4.90038 | -46.83047 | 2026-08-20 04:19:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c46baa44-fa5f-3edf-9208-05a9efb3f44d | -7.17964 | -42.75787 | 2026-08-20 04:19:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4f32f9d4-2045-39c4-9fe3-7ffda090c956 | -8.45872 | -46.95004 | 2026-08-20 04:19:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b25e043-792c-39ac-8f9e-be495c6e44a4 | -7.6359 | -42.72883 | 2026-08-20 04:19:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 01a3cd64-d0f7-3428-a139-2f46d56fcd9a | -12.25751 | -43.16174 | 2026-08-20 04:19:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 3341a78e-35a5-3654-8c85-05a538c03664 | -8.56793 | -54.72694 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a30ec44e-71f5-3145-88c5-8277e9ee85b7 | -7.34543 | -45.82614 | 2026-08-20 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6a4188d0-55ef-3f6c-a21d-cc3d1e66ad24 | -8.10215 | -51.66563 | 2026-08-20 04:19:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 854c6bcb-7de7-3e69-a2be-356d0b6ed0f5 | -8.65953 | -54.58763 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c9422894-e8be-34e7-b382-bc481f5bf58c | -11.81124 | -44.80982 | 2026-08-20 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8d54df08-7998-346f-9f22-3d3383351734 | 2.15634 | -50.71524 | 2026-08-20 04:19:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 536b379c-eb28-3910-8dd7-25fb3d687191 | -7.96771 | -44.66518 | 2026-08-20 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 868bc243-5216-3735-8634-e991f52200f4 | -11.80849 | -44.80576 | 2026-08-20 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b050d3e8-6a4e-3f99-a1d2-70135f1ced73 | -8.56875 | -54.72255 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f301861-5d96-3ddb-9dee-30682ef86df7 | -7.35362 | -45.81961 | 2026-08-20 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5bc7ee8f-fe4a-3cd8-a42e-9821d725d379 | -10.41678 | -48.33426 | 2026-08-20 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fcf8a2a2-9dfa-3def-91eb-2d021e658449 | -8.66832 | -54.648 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 8dbd6300-51a4-303a-ad39-05e2f61c9710 | -7.35584 | -45.82786 | 2026-08-20 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d823ce62-6123-33c4-a948-6391cb51d753 | -8.71235 | -49.62012 | 2026-08-20 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3a67933c-471e-3fd4-aba1-540aecbfd893 | -6.17365 | -39.383 | 2026-08-20 04:19:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5fd9aa71-fb52-3a38-a07f-25ad3fd46d41 | -7.96545 | -46.92049 | 2026-08-20 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 467c48ec-4502-3277-980b-3a26f9a852ff | -8.66728 | -54.64259 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d0800b97-78b9-3c54-ac55-255ca3633391 | -7.61172 | -45.15956 | 2026-08-20 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b0e0c7f2-82a6-3ea0-a09d-a64cb1cf1a3f | -8.58162 | -54.7521 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8dda02b9-40ba-323c-bff8-a4b0d506f77f | -10.75539 | -50.35032 | 2026-08-20 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 88a53d30-1b90-346f-9a3e-0cb3ccff7b8e | -10.78553 | -50.30533 | 2026-08-20 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 89ab4a88-a0c1-36d5-b130-e93436cf5346 | -8.66323 | -54.64252 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9fc0e558-d17e-32bc-958a-527dd7fa8614 | -12.2444 | -43.17126 | 2026-08-20 04:19:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 0c3c1afd-1d48-35b4-997b-a73ca168dfd5 | -8.09821 | -51.6593 | 2026-08-20 04:19:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c4e59d4d-15ee-3455-ae75-8143ef079bc9 | -6.73337 | -44.66783 | 2026-08-20 04:19:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a41a982e-2d15-3a54-b139-a16d9c4c0200 | -7.01735 | -47.97062 | 2026-08-20 04:19:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 25bee426-9b86-32b8-b8c8-381b9f83126f | -5.73991 | -43.27211 | 2026-08-20 04:19:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 381f5585-647a-34c2-90f1-ac6c2aa8c6d1 | -8.49153 | -54.86817 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a68d8d19-4296-3161-9883-8f35b9ad4a83 | -6.35542 | -54.90582 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ef26bf2-7c93-371f-8ac9-51f27f6759d4 | -8.67837 | -44.30054 | 2026-08-20 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ca82dcf-fe0b-3606-82e7-0e4a4b3c6187 | -10.82393 | -50.28727 | 2026-08-20 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93ace9af-3b8a-3217-8bcb-cd0f0941cd38 | -8.56751 | -54.66443 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b06a41ed-2661-3a96-9558-dd2ae72d2155 | -8.48978 | -54.87727 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c13c1fa-4cfd-3add-aa60-90be5090f01c | -8.34984 | -46.35652 | 2026-08-20 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b3a1d84-dbb5-3804-be76-8117895c6c6f | -7.35175 | -45.83113 | 2026-08-20 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ab1e9d7c-2e36-3e1d-bccb-a80eec3235ed | -6.42306 | -52.76228 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1924e4f8-a96a-3ac6-8e6c-ff5e0ed7e33b | -8.67317 | -54.6437 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8c55abc-08b9-391f-8778-778d78cb848b | -11.70045 | -47.81528 | 2026-08-20 04:19:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 277363cf-1786-3824-8272-a54036bf4210 | -10.48417 | -50.31592 | 2026-08-20 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2269d9fc-7853-3b5c-8d98-5347164408ad | -11.37384 | -46.37786 | 2026-08-20 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e7fd1512-7081-3b44-a5e5-be84345fef6a | -5.79808 | -55.73363 | 2026-08-20 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bc035c75-2bc4-3d49-9a7f-f939d48320c7 | -5.79365 | -55.72072 | 2026-08-20 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f45406cb-fc65-30f9-ba68-9264f8d49c77 | -6.78177 | -42.89145 | 2026-08-20 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 38d80616-94dd-3eb2-8898-29fd80f5c328 | -6.3426 | -44.07587 | 2026-08-20 04:19:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc76f1cc-9bff-3069-b52b-35f3f604ebd4 | -6.43698 | -52.74712 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1e4e95b-dda1-30a5-a4be-1e1d7a000aad | -10.25658 | -46.99331 | 2026-08-20 04:19:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 459dd462-0e31-3f31-ab69-ff59618cadb7 | -11.39326 | -47.22174 | 2026-08-20 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4329f074-2d80-3eb9-ac91-cec5fd6624c4 | -7.53181 | -55.58024 | 2026-08-20 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 608fca10-b303-367d-8471-2cb071755ca8 | -7.97274 | -44.65513 | 2026-08-20 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fdb96696-ffec-3396-8de1-c5602672cb0e | -7.01654 | -47.97554 | 2026-08-20 04:19:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ed566197-b0e9-3bee-a1fa-435df4870291 | -8.56162 | -54.66324 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 758cdc91-330c-3d40-88aa-411dd7369dfc | -10.80547 | -50.29223 | 2026-08-20 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a9e721d8-fa9d-3d7e-bef4-6e6600eec9e1 | -8.67827 | -54.64898 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fdd2db9-7707-33e9-b62b-7cf0d0892e7a | -6.42242 | -52.76584 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 45bf4b5f-5a07-30dd-9b95-05d8ddc146a6 | -6.35394 | -54.9021 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 99f18513-6b6a-360f-8fd3-023349499a27 | -7.6157 | -45.15646 | 2026-08-20 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c2ea773d-99a1-3367-9ed7-f89429785fa5 | -7.53431 | -55.5765 | 2026-08-20 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2075527-1f45-3d65-9f9a-cf081f93d3d9 | -7.95805 | -46.91644 | 2026-08-20 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d0f5eb1-4105-3411-a2a6-20c42387a85d | -7.34356 | -45.83766 | 2026-08-20 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 748764cc-0927-3c73-8f94-fc171cbab9a1 | -6.94829 | -52.80986 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 918e61af-59cd-350a-b080-41d300bfcc62 | -6.78672 | -42.88155 | 2026-08-20 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 44935327-0c9b-3ef7-a32e-bfbd7e0cf2ad | -9.92275 | -48.75518 | 2026-08-20 04:19:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d2547bf-44a8-36f5-ab94-8c928238afe2 | -9.85906 | -48.05192 | 2026-08-20 04:19:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2681461f-ec16-3b4b-9250-51cb565842d2 | -10.91088 | -50.56872 | 2026-08-20 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README34.md)
