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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75613f21-a7df-3716-b1a5-9cf6ab06dffb | -11.4965 | -43.55837 | 2025-09-23 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 958e730e-49c2-318a-93de-cd9ed0d45b82 | -5.10203 | -43.16918 | 2025-09-23 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47389723-52d3-3b7c-bd39-f51c3a1d14e4 | -5.64698 | -42.59973 | 2025-09-23 03:57:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| becd1723-3243-3ce0-9b7d-b3e44f78a712 | -11.45427 | -43.53174 | 2025-09-23 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02cf8c12-ec91-39a5-b487-d1cf436afe0f | -4.15308 | -48.60518 | 2025-09-23 03:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa742593-3b4b-3c19-b053-e6c11bb71cb0 | -11.89303 | -41.27105 | 2025-09-23 03:57:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| b8351bed-0fd2-37ac-8538-c5ba0d21a6da | -8.82336 | -44.33582 | 2025-09-23 03:57:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95f081da-2de6-30f7-96ef-aa3bba1590e1 | -7.36168 | -44.54645 | 2025-09-23 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5632f902-4f4e-39cd-bc98-2a0f9ed374da | -8.20625 | -42.20943 | 2025-09-23 03:57:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7d6ed8a7-37cd-3842-87c2-39a3b7d4fbea | -4.77916 | -47.25643 | 2025-09-23 03:57:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c520085f-49c9-3d93-b7ff-dc044bbac61c | -7.88549 | -44.02208 | 2025-09-23 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6051b082-4965-3e08-9df9-8bf3b0bcda9f | -4.9629 | -48.01402 | 2025-09-23 03:57:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f877d452-04a2-3431-af32-8effd42f42f4 | -11.52603 | -43.58573 | 2025-09-23 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ba60cde-54a2-33f6-9dba-d9691b947329 | -4.96861 | -48.01472 | 2025-09-23 03:57:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4ca2defa-518d-31ea-a1ec-a2d4869d409e | -4.76462 | -43.62339 | 2025-09-23 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8734a0e3-4bc4-3f13-bcbf-98837a359f14 | -11.4067 | -44.94846 | 2025-09-23 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da47ecde-6065-3297-8b9c-2d79ebef1236 | -11.45885 | -43.52779 | 2025-09-23 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be283ac9-1362-34e1-be8e-7d48c56d3a23 | -5.64698 | -42.59768 | 2025-09-23 03:57:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| dccc95ab-790d-3417-9076-9fd484768a09 | -4.07731 | -48.04071 | 2025-09-23 03:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e78b824-bec5-30ca-a41e-d2276fc5a202 | -4.78255 | -42.7645 | 2025-09-23 03:57:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e252703-e9b8-3307-80aa-70903167845b | -3.51442 | -49.45142 | 2025-09-23 03:57:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8a081082-83b7-3534-ac33-adc5f708bd88 | -11.22407 | -40.09171 | 2025-09-23 03:57:00 | NPP-375D | CAPIM GROSSO | BAHIA | Brasil | 2906873 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d14f4f26-460a-34a8-936e-2c1ba1cf28c9 | -6.25721 | -45.33606 | 2025-09-23 03:57:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c98c632c-978f-39cd-8099-6aeb25a22664 | -7.8896 | -44.0228 | 2025-09-23 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 095a676d-0fd2-3855-8209-269f50783cd7 | -7.03969 | -34.91058 | 2025-09-23 03:57:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 45b14a78-acc3-32c5-91af-2e56ba2ab5a3 | -4.96222 | -48.01791 | 2025-09-23 03:57:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e578bd6-fd09-394a-9dee-43a1b40c7442 | -11.43752 | -43.52195 | 2025-09-23 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 427e1b74-3284-338e-9cad-ea9a02854cf6 | -6.36217 | -43.36084 | 2025-09-23 03:57:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e24dd063-0234-35aa-8cc4-0a7c5ae58a45 | -6.61427 | -44.60692 | 2025-09-23 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 339485ee-eb4e-3a67-9a2b-0d767088dbaa | -9.18891 | -44.62175 | 2025-09-23 03:57:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84532a18-552b-34d7-b175-c265b3c87655 | -7.77273 | -44.72147 | 2025-09-23 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aab8d3d7-583c-344e-818f-032374efd2b6 | -7.03466 | -34.91875 | 2025-09-23 03:57:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| c07df512-2ccc-3101-85b5-dcbdd1427b25 | -7.3678 | -44.54559 | 2025-09-23 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45611409-aa2c-3ae5-a4e3-ddf0973328a5 | -8.80723 | -43.07461 | 2025-09-23 03:57:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| af99be7a-a5a9-3a47-87f9-aa21f05fe9cf | -4.07155 | -48.0398 | 2025-09-23 03:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 577800f3-204c-3bb8-8da5-39eeef859ef4 | -4.38388 | -43.28897 | 2025-09-23 03:57:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e19e870f-e93a-3890-9272-707c052aa930 | -7.07225 | -46.19914 | 2025-09-23 03:57:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dad0b2a1-0baf-3f52-8aed-eff7278e528f | -5.94228 | -45.39532 | 2025-09-23 03:57:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 34601fc2-aabe-3b20-9473-5ff9f826325f | -7.22744 | -45.17949 | 2025-09-23 03:57:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1d0841cc-170d-357e-ba57-a82508726077 | -11.4145 | -44.93703 | 2025-09-23 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 01890c16-751d-3763-938e-10a16cee98ac | -11.91765 | -43.42552 | 2025-09-23 03:57:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d622ed0-3f3d-38b7-8624-a2eba57716c4 | -6.25506 | -43.87887 | 2025-09-23 03:57:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 09bca50c-39f7-3dae-aec6-8e841325e6ea | -8.81922 | -44.33511 | 2025-09-23 03:57:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a7e2908-0429-36c6-82c7-712ee76cb6d9 | -10.50412 | -43.8536 | 2025-09-23 03:57:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1f68d13-4789-3d86-bde9-590012a0b469 | -5.84042 | -42.614 | 2025-09-23 03:57:00 | NPP-375D | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 50c53015-de95-36cf-b9cd-c374000ab094 | -4.12805 | -48.82311 | 2025-09-23 03:57:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9389d541-25ea-3571-bd14-c43382657043 | -11.44751 | -43.5257 | 2025-09-23 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1d74c92-f62b-33d6-9556-613184865cd2 | -12.64665 | -39.43808 | 2025-09-23 03:57:00 | NPP-375D | SANTA TEREZINHA | BAHIA | Brasil | 2928505 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cef38cd0-d184-3893-94d8-e4a3f85d97d8 | -7.85953 | -42.95361 | 2025-09-23 03:57:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 46b471a3-13ad-3673-ab2f-ddebd211306b | -4.49235 | -48.11533 | 2025-09-23 03:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 84d11ea9-50fd-3d82-9866-b65cabace034 | -7.87788 | -44.01691 | 2025-09-23 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 147118dc-27eb-3a2e-9ae2-17d255bfe6f8 | -11.53324 | -43.61831 | 2025-09-23 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ed65c749-56ba-3ee9-950c-e246d04cc703 | -6.89763 | -44.76699 | 2025-09-23 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2ba9b194-9842-3a44-866b-a73b9eeb9663 | -7.49875 | -35.24643 | 2025-09-23 03:57:00 | NPP-375D | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 2e977e20-75a7-32fe-aa6e-cbce6950af0c | -11.53167 | -43.62054 | 2025-09-23 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 320aa0c6-7c2b-3174-af14-d2dc40adfc99 | -6.60988 | -44.60626 | 2025-09-23 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4e0c4d3-c67a-3e6b-aea7-af7cf17a311f | -11.40557 | -44.93928 | 2025-09-23 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9a24fe59-4721-3a55-877c-5ed5b6792ce8 | -8.37541 | -44.70002 | 2025-09-23 03:57:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15375776-7396-390c-bd4d-82063670b782 | -6.25423 | -45.33369 | 2025-09-23 03:57:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 83871f20-09ee-3a98-918a-cf1f5393cc95 | -7.88668 | -44.02623 | 2025-09-23 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8d284d08-1757-3448-ae8d-9e9986b0f449 | -9.18826 | -44.62539 | 2025-09-23 03:57:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e1dff06-cb1e-3f99-b5dd-05bfec355160 | -4.15903 | -48.6062 | 2025-09-23 03:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 804a560a-3a25-3305-a449-22f65405362d | -5.51866 | -46.51276 | 2025-09-23 03:57:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3deb1a95-0070-3d8f-a50a-d65b9077a2c5 | -7.70166 | -44.903 | 2025-09-23 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ad17654f-b24b-3991-8216-2464745bd543 | -5.83962 | -42.61889 | 2025-09-23 03:57:00 | NPP-375D | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 897b81ad-4f64-3bcf-ac30-12c04b3dbe0f | -8.52706 | -44.9685 | 2025-09-23 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6e22f7cc-35b7-3ce6-ba48-e9518f893514 | -8.80962 | -43.07233 | 2025-09-23 03:57:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| be74d620-ef29-3812-8dcc-099c17f458c3 | -8.38574 | -37.20783 | 2025-09-23 03:57:00 | NPP-375D | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f344db0f-c5a9-3e5d-bcd4-5d96dff7e87f | -11.92469 | -40.23595 | 2025-09-23 03:57:00 | NPP-375D | BAIXA GRANDE | BAHIA | Brasil | 2902609 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 316e0f85-0904-3098-bfef-9b42a624b38c | -11.40624 | -44.93558 | 2025-09-23 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 010a99eb-6bf7-390f-a577-a630663a67a9 | -8.13439 | -44.46827 | 2025-09-23 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cffe3eeb-68ae-3cf2-afe6-20bcaa233179 | -5.69331 | -44.44092 | 2025-09-23 03:57:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f320e1e-4d6e-3f60-ac9e-827408f122c4 | -6.25342 | -45.33854 | 2025-09-23 03:57:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 995e7419-74dd-3c5e-81f3-0b742587f239 | -4.08307 | -48.04162 | 2025-09-23 03:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ab79ce4-718e-3e29-b7b3-837531d22800 | -11.41172 | -44.9525 | 2025-09-23 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 06604a0d-15b7-3834-8ac4-3093a71c2dfe | -4.48596 | -47.67741 | 2025-09-23 03:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 527d0b7a-1567-32dd-872f-284ee3741453 | -7.88076 | -44.02501 | 2025-09-23 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 99fd516b-fc3d-321c-a156-c3a07c0c63b1 | -11.41721 | -44.94562 | 2025-09-23 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 682bceca-3fb4-32ef-aa9e-30c1afd0be43 | -11.40324 | -44.94377 | 2025-09-23 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2ef5e12d-2ef9-39a6-a839-41e159a8d329 | -11.88963 | -41.27048 | 2025-09-23 03:57:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| ad730f85-3176-3259-b497-84d504f1ab5e | -7.88487 | -44.02575 | 2025-09-23 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a5ee68c8-30b8-379d-8ed9-f5cff7e178fd | -6.50297 | -41.5444 | 2025-09-23 03:57:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bab50b17-f357-3049-ab54-3f31021a7d86 | -11.51898 | -43.2466 | 2025-09-23 03:57:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| db1364d9-03e2-3257-8afd-a9ef64e7d156 | -7.7684 | -44.72076 | 2025-09-23 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cb74ffd6-dae6-306a-8f35-58a274147fa5 | -7.16663 | -44.43425 | 2025-09-23 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3014cfd7-4b6d-36bf-851b-6416f1a886fc | -4.79777 | -47.27739 | 2025-09-23 03:57:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55c959b9-1860-37dc-b42e-a1030d9a0086 | -9.50664 | -37.96498 | 2025-09-23 03:57:00 | NPP-375D | DELMIRO GOUVEIA | ALAGOAS | Brasil | 2702405 | 27 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5be7b161-642b-3a31-96d8-7065f906b1ba | -8.517 | -44.97488 | 2025-09-23 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f835fa9b-b5eb-315f-8042-7610c060c891 | -7.79163 | -46.19651 | 2025-09-23 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78894475-b0c6-3a33-82a9-10c1f0cf7b87 | -4.07759 | -48.04372 | 2025-09-23 03:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b243363-7a9e-3c63-b6eb-621ab0bfafe1 | -11.08923 | -45.35572 | 2025-09-23 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 208beeba-5790-38b1-b589-65ad9e511603 | -11.0226 | -45.88817 | 2025-09-23 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| bf6eb196-0ca0-3372-981e-6bf5d48a1d3c | -11.45129 | -43.52639 | 2025-09-23 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e60e7c0d-3245-3afb-ac60-67d3dbd020e0 | -7.94002 | -41.60897 | 2025-09-23 03:57:00 | NPP-375D | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fecc7934-9e06-3a9c-aa78-2199958bc900 | -7.89021 | -44.01914 | 2025-09-23 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6ac42119-783b-3734-9ed2-5a586a93c326 | -8.0048 | -45.73066 | 2025-09-23 03:57:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9cd16cc-e393-3e25-a870-d4c1e75d2961 | -4.07183 | -48.04277 | 2025-09-23 03:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f4296e2-411c-36cc-9b0f-cd3221909fd7 | -11.41651 | -44.94952 | 2025-09-23 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 79a4a0e3-ba8e-3c19-b6c2-1e4c46586a1b | -4.59319 | -46.59335 | 2025-09-23 03:57:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c298c124-b348-31f3-ab5a-11ce7a7600e1 | -6.89712 | -44.76484 | 2025-09-23 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README10.md)
