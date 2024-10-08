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
| 0c7e487c-c9c2-39bd-8096-1e6bd301b52b | -3.61751 | -42.75673 | 2024-10-08 03:40:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f623aeb5-f2db-305b-aaff-c74d9bb51c3c | -5.81785 | -43.23951 | 2024-10-08 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc0b8ad5-4d43-39be-a84a-bd43876abb82 | -5.79625 | -43.27503 | 2024-10-08 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0ac5f0c5-5ef6-3c30-a986-b138325ecb46 | -5.13818 | -42.88202 | 2024-10-08 03:40:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b36bd1b-3d43-3c03-92d0-06b2b1e3cb0a | -4.04321 | -43.24314 | 2024-10-08 03:40:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c49fe72-2243-37c6-aaab-aaf07c8fd704 | -4.03805 | -43.24224 | 2024-10-08 03:40:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d5c70dca-7101-38a2-84d0-05b343268615 | -4.01569 | -43.23951 | 2024-10-08 03:40:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab1b9ca3-fec6-3827-b5d7-a717c141efea | -6.15844 | -43.52719 | 2024-10-08 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf98c6c1-8bf7-38e5-972e-3ccab77f6ea8 | -5.77378 | -43.99655 | 2024-10-08 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38853757-68af-34b6-b7a1-7a826a367c64 | -5.76849 | -43.99571 | 2024-10-08 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ff4b0c0-4cf3-31df-98b5-6653e5700a09 | -4.65906 | -43.77268 | 2024-10-08 03:40:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| efdfc24f-cefd-3c51-92f7-b034f32f5b82 | -4.65376 | -43.77184 | 2024-10-08 03:40:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e4eabd2-6ab2-3a3c-83ae-fdb0362a1576 | -5.38917 | -43.57318 | 2024-10-08 03:40:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 694d45ce-1fd9-3ee5-b756-890552d876ad | -5.32342 | -43.73127 | 2024-10-08 03:40:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 119f05f4-68f8-37b1-a9ae-41fbbcdffc0c | -5.32287 | -43.73449 | 2024-10-08 03:40:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a2cda64-537e-322e-a5eb-95ed513e5997 | -6.48402 | -43.88165 | 2024-10-08 03:40:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9cf70907-b070-3f32-ba50-783030925711 | -6.47886 | -43.88072 | 2024-10-08 03:40:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54070b52-509d-3772-bf4e-e30792257599 | -6.69748 | -43.95682 | 2024-10-08 03:40:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89850322-6ea3-3508-aad9-a8b5bb083f45 | -6.69694 | -43.95997 | 2024-10-08 03:40:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8f27148-8295-3354-bfc0-06bb96b7ffeb | -6.69232 | -43.95581 | 2024-10-08 03:40:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8747340a-3add-3f7b-963a-4eef6fae0b16 | -7.84713 | -45.35787 | 2024-10-08 03:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d4988f68-e31b-3ee5-b967-5bd6fb797255 | -7.85892 | -45.35623 | 2024-10-08 03:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1cfd2663-a3c3-39cc-ad3c-4a2e16002650 | -7.85825 | -45.35999 | 2024-10-08 03:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0e77bf9e-8b86-39d9-a0f9-8ce9eb484f98 | -7.85759 | -45.35615 | 2024-10-08 03:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 75164584-cc59-30a6-97a0-a7cca0915c69 | -7.85757 | -45.3638 | 2024-10-08 03:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3c782af5-0990-373b-96ac-8375374e5432 | -7.85689 | -45.35991 | 2024-10-08 03:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3192ac79-a42b-34e2-a305-f0723386acc6 | -7.85618 | -45.3637 | 2024-10-08 03:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f7d012a1-3200-30ac-8006-93ce2e8e4daf | -5.915 | -35.32327 | 2024-10-08 03:40:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d95d8a03-3fc3-3918-a366-e4015b445b41 | -6.1635 | -43.52814 | 2024-10-08 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34bfe076-99ee-3048-9ee9-bdce4ff760b3 | -7.85269 | -45.35894 | 2024-10-08 03:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 41eb98a3-1096-3885-b401-f86249181fc7 | -7.85201 | -45.36272 | 2024-10-08 03:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7e7138d0-cddb-3d7f-9de5-d86791dd1f5a | -7.85133 | -45.35886 | 2024-10-08 03:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| cd5970b9-cf9e-34df-b4a4-c9c342a4643b | -7.85063 | -45.36264 | 2024-10-08 03:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 922c7207-8f4d-3071-b39c-7f5523fa7e69 | -5.90524 | -35.42808 | 2024-10-08 03:40:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 66a33915-f88c-33a7-87db-1e2f8206b4f9 | -5.9047 | -35.43154 | 2024-10-08 03:40:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 003e3db9-698b-35fc-84fa-a2fc56d1a9c5 | -7.03704 | -35.51175 | 2024-10-08 03:40:00 | NOAA-20 | ALAGOA GRANDE | PARAÍBA | Brasil | 2500304 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a8010189-21cd-3ff2-9f08-678e1d2d4d47 | -7.03649 | -35.51521 | 2024-10-08 03:40:00 | NOAA-20 | ALAGOA GRANDE | PARAÍBA | Brasil | 2500304 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b52cd87e-fdf5-3190-bae3-0a7136a252a1 | -6.60283 | -35.24823 | 2024-10-08 03:40:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 5b8f382d-9b5f-3f8d-8c3e-c5d377e5a8cf | -7.85284 | -35.37897 | 2024-10-08 03:40:00 | NOAA-20 | LAGOA DO CARRO | PERNAMBUCO | Brasil | 2608453 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9e6dfc67-4d71-334c-b6dc-b06d59cdd9b1 | -7.84953 | -35.37845 | 2024-10-08 03:40:00 | NOAA-20 | LAGOA DO CARRO | PERNAMBUCO | Brasil | 2608453 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 333890f0-4b52-39a5-99c7-3c072e7ab35e | -7.47474 | -34.8432 | 2024-10-08 03:40:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cfae2b35-ec60-3138-a6fd-69f0f220caaf | -7.19732 | -34.9875 | 2024-10-08 03:40:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 29c49aed-0c7b-39ce-891b-01093c52a0d8 | -7.19401 | -34.98697 | 2024-10-08 03:40:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4216c9c4-89ff-3a71-aa64-a15cb13981fb | -6.99666 | -34.94554 | 2024-10-08 03:40:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 23.4 |
| ef77f0e3-874a-3278-85a7-7b31496275b8 | -6.99612 | -34.94901 | 2024-10-08 03:40:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 89e95a17-38d8-331d-b03a-7576e4d37e9e | -6.99336 | -34.94503 | 2024-10-08 03:40:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 23.4 |
| 149820db-a87f-35dd-bb44-ae02b56a95c1 | -6.99281 | -34.94849 | 2024-10-08 03:40:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| ef85e7f9-b7bf-3f50-b65e-dccfaa341275 | -6.74484 | -35.12186 | 2024-10-08 03:40:00 | NOAA-20 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 453fa057-b8c5-35f9-86e0-7da6d5d54974 | -6.60338 | -35.24477 | 2024-10-08 03:40:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| d65c93e0-6d28-3396-8430-6b44cbd177ba | -8.15051 | -35.38679 | 2024-10-08 03:40:00 | NOAA-20 | POMBOS | PERNAMBUCO | Brasil | 2611309 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c7138c9f-c1b7-3df8-b1fb-4d38408fda0e | -10.08973 | -36.20992 | 2024-10-08 03:40:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 57cdb7c5-d783-33f1-9f42-3d2761021e99 | -10.08642 | -36.20938 | 2024-10-08 03:40:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e6a6b8e5-b552-3fde-a204-76608d700582 | -9.49161 | -36.08199 | 2024-10-08 03:40:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f8a8bf68-65b0-3326-b8ee-b5f66ca3329c | -6.66986 | -37.47145 | 2024-10-08 03:40:00 | NOAA-20 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 05513cb7-db6a-35f0-8ea7-59c3b7a48455 | -6.6664 | -37.47087 | 2024-10-08 03:40:00 | NOAA-20 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4ee50f01-8f23-3616-a98b-816270fbd9cb | -6.43727 | -38.83108 | 2024-10-08 03:40:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4a44f029-77d2-39c0-a56d-6cfc65601779 | -6.43654 | -38.8355 | 2024-10-08 03:40:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c3965cab-29be-3678-b7ef-56224e77d291 | -6.43579 | -38.84006 | 2024-10-08 03:40:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2cc47f72-9d76-3deb-85d4-4297e3c255cf | -6.43355 | -38.83054 | 2024-10-08 03:40:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 0c0dc147-e31f-3d6a-a088-6f6c3c52f2d9 | -6.4328 | -38.83504 | 2024-10-08 03:40:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 6bc8f3b7-3ba8-382d-ac06-010bfda7b607 | -6.43205 | -38.8396 | 2024-10-08 03:40:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 60b8a566-d354-3f3b-a032-44d13da95a23 | -6.42982 | -38.82998 | 2024-10-08 03:40:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| bc025c6b-bbe2-3f69-90b5-d16177b2f49c | -6.42907 | -38.83456 | 2024-10-08 03:40:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 336f1580-6e44-3592-8544-ce9dbb7f0278 | -6.42832 | -38.83912 | 2024-10-08 03:40:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| f4fc9708-06ba-33b4-bc06-24e03a60b683 | -6.42684 | -38.84809 | 2024-10-08 03:40:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 018aac85-2e09-3c4b-a426-a5db26e516f1 | -6.4261 | -38.82946 | 2024-10-08 03:40:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4a83d705-a39f-3ef4-9262-e6aec0529bc6 | -7.25296 | -39.85607 | 2024-10-08 03:40:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 378b1566-8925-313a-bb83-0c162263291a | -7.97683 | -40.02715 | 2024-10-08 03:40:00 | NOAA-20 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5ff239e8-dbae-33f0-b3fe-a6952c2cad42 | -5.04051 | -40.87003 | 2024-10-08 03:40:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b289b85a-3abe-3cf4-bbed-98122187257a | -3.79714 | -40.4455 | 2024-10-08 03:40:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 76d84d69-60c0-3032-a29f-2de4b6be568e | -6.05939 | -41.09912 | 2024-10-08 03:40:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2661132b-39f1-34b7-9d25-824e348bd57a | -5.18228 | -41.29525 | 2024-10-08 03:40:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 21f2c200-ddc9-3253-bd32-3f0bb8e673f4 | -5.18081 | -41.30413 | 2024-10-08 03:40:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| b65f466f-0311-3166-b5e3-be4d54be2183 | -7.59869 | -41.7159 | 2024-10-08 03:40:00 | NOAA-20 | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3dfb73fe-8df8-3778-b90d-a70ce6b5f109 | -6.82582 | -41.79987 | 2024-10-08 03:40:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f37746b4-5e9e-3805-a3e1-e079da3b6e95 | -6.8409 | -41.68426 | 2024-10-08 03:40:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6a8869b8-237f-37ee-ba9b-ef859f13ced3 | -6.48432 | -41.95184 | 2024-10-08 03:40:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| bb6d3fe4-2d73-34f0-89ee-3fe189e456d1 | -6.48504 | -41.94757 | 2024-10-08 03:40:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 45c0146f-e01f-36ef-81b0-4d9bb65a7baf | -7.59797 | -41.7201 | 2024-10-08 03:40:00 | NOAA-20 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e3298fa4-ca22-3ee4-9bca-9d0d303dc8ab | -7.97207 | -41.61739 | 2024-10-08 03:40:00 | NOAA-20 | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3f3e9409-be70-313e-a24b-b6b605c35f65 | -4.25117 | -41.92511 | 2024-10-08 03:40:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 191d6af9-429a-3324-bfa9-6d83b4a3d566 | -4.24902 | -41.92008 | 2024-10-08 03:40:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cd5c67e2-8050-3946-a52b-2de8d4e32407 | -4.24817 | -41.92508 | 2024-10-08 03:40:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8cc52c88-7789-31f1-9ae7-fdfc5eddf729 | -5.8399 | -42.65235 | 2024-10-08 03:40:00 | NOAA-20 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| d3db15cc-0321-3530-9fe0-7b4dc58c905a | -7.65644 | -42.50269 | 2024-10-08 03:40:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 92683ccb-fcce-32f7-8e8d-a7cb8b49fb69 | -7.64757 | -42.52618 | 2024-10-08 03:40:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c5571125-3497-37d0-ae55-1b34e9523bdf | -7.62391 | -42.4213 | 2024-10-08 03:40:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b2caf8ee-14f8-3e98-8ea8-520e07f2919f | -7.62384 | -42.41852 | 2024-10-08 03:40:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6630cceb-c8ea-3693-9d34-f5cd1e39e435 | -7.623 | -42.42321 | 2024-10-08 03:40:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fcd4da8d-1737-3e1f-9918-49d6e40f3f23 | -7.61607 | -42.43957 | 2024-10-08 03:40:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 28c1e2a4-5b41-3c0e-8ee2-3f72892de99f | -7.30525 | -42.24603 | 2024-10-08 03:40:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d5e6f392-2338-3588-b847-c05d396ff3e5 | -6.83083 | -42.80638 | 2024-10-08 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 995cc5c7-4d3c-3e7a-8f3f-b47f15b52043 | -7.78508 | -43.08866 | 2024-10-08 03:40:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| c41814bd-eeb9-3597-aafe-8a3cf16838c6 | -7.77366 | -43.0974 | 2024-10-08 03:40:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8e0f8836-d513-3006-a42d-8cdfea912eb3 | -7.65475 | -42.51238 | 2024-10-08 03:40:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c9e75c37-24e6-3de7-bf1f-136008ad1075 | -7.63471 | -42.41332 | 2024-10-08 03:40:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ad050fc2-557b-36ff-984d-16817f655a42 | -7.63011 | -42.41259 | 2024-10-08 03:40:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| fb5159d4-4d50-37c1-ae97-b8da0d6d3ea4 | -7.6185 | -42.42528 | 2024-10-08 03:40:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e4c3e33b-349d-3574-960d-2937a947994e | -7.34863 | -43.66792 | 2024-10-08 03:40:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e04dc725-bae8-3286-a813-9a3f7a75789b | -7.30901 | -42.25155 | 2024-10-08 03:40:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |


[Clique aqui para ver as próximas entradas](README34.md)
