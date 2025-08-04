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
| 808700ca-98f7-359f-aba3-1d393d11db28 | -6.65138 | -59.11582 | 2025-08-04 04:34:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a6d2798-3341-3af1-b86b-7d681756ece9 | -7.6452 | -45.29907 | 2025-08-04 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83bc32e3-b8d9-32cf-bf4c-ee9638e9bfd0 | -7.53194 | -44.87666 | 2025-08-04 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99e846c0-bfac-3ecd-9942-7f5390ce1ba2 | -8.00765 | -43.19246 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 171d41a8-9767-377d-94b9-1c8ac29f0e0d | -5.88432 | -43.72987 | 2025-08-04 04:34:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63b6e6f5-e224-38d2-9381-2e172a0a469b | -8.38284 | -46.94031 | 2025-08-04 04:34:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b6f65b7c-13b2-3194-aa4c-9937e4d5a632 | -5.88363 | -43.73445 | 2025-08-04 04:34:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c8c15a6-ffeb-375e-918c-45a98ae05030 | -4.74518 | -44.4459 | 2025-08-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46237445-8e04-3954-b2fc-8b05b757f311 | -8.55613 | -47.46325 | 2025-08-04 04:34:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 353e88bc-68b6-3f01-b090-e791724fd177 | -8.0361 | -43.11037 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| b900b35a-c474-3b7b-9c6b-7e102592784d | -7.40935 | -45.28582 | 2025-08-04 04:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b320d0e3-fad4-3605-b0a9-5368b4143dde | -9.62148 | -43.85674 | 2025-08-04 04:34:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4ee5f741-1f8c-3fcc-b428-2b451abad012 | -8.03154 | -43.1133 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 827754b7-0a07-31a3-8fed-a2ab3071f938 | -6.61125 | -44.04746 | 2025-08-04 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e125a5bd-c558-372d-abc1-8453211280f1 | -7.02013 | -59.8281 | 2025-08-04 04:34:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4772205d-a64e-3de2-8a70-b33a01c09a84 | -8.04928 | -43.10505 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 8d42a105-91a8-303b-a3e9-abd2e25d5b66 | -8.38566 | -46.94442 | 2025-08-04 04:34:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| ca00ce57-0a5b-3c9f-958f-de5cb01ecd01 | -5.99005 | -45.02625 | 2025-08-04 04:34:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9b7fa07-1f2a-3171-9856-32d4f056f5a4 | -3.28072 | -48.81532 | 2025-08-04 04:34:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40903228-4034-34d2-811d-532a0aded71b | -7.55427 | -44.87591 | 2025-08-04 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9aeaf5c2-5764-37da-a4d1-b5e8218ad13d | -8.0203 | -43.16212 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 7bd9170f-8816-3490-96bc-d8223adfa6c4 | -6.61517 | -59.95637 | 2025-08-04 04:34:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ca06ffd-07be-3baf-b541-7af3dec4ea26 | -4.13303 | -47.64298 | 2025-08-04 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f376c1a4-c950-37f8-b5ee-256a4beab9b1 | -8.38676 | -46.93725 | 2025-08-04 04:34:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1dda52dc-870c-340c-881c-4a02ed3c3cd3 | -7.02432 | -59.83356 | 2025-08-04 04:34:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b876c5e-4ee8-372c-ae3e-c81f9604e575 | -8.0127 | -43.18604 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| faa164a8-3391-3de7-89c4-5efd6891738e | -8.36165 | -46.91526 | 2025-08-04 04:34:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6989b2d-623c-3bd7-b91b-7b7eaa4b9553 | -6.55761 | -43.91608 | 2025-08-04 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 978140c1-71d2-3516-bf7f-9d26d390d9db | -7.99559 | -43.21899 | 2025-08-04 04:34:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 7e7326e6-4e00-3463-811a-0ff9b9938eec | -4.12916 | -47.64592 | 2025-08-04 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d1328e1f-fbc4-31b3-a5b2-456ef341fa5a | -6.43953 | -44.19122 | 2025-08-04 04:34:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d80dfc82-d143-308e-a38d-c886b764a79c | -7.65107 | -49.8408 | 2025-08-04 04:34:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 138fdfa8-99b3-342b-98ab-a5a948d080ad | -7.44544 | -48.94521 | 2025-08-04 04:34:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4655348-90cd-3a29-a4db-79d0d9397504 | -7.21528 | -41.85618 | 2025-08-04 04:34:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 85cc66a0-4834-3f84-8ba1-6dfe3337132d | -8.3167 | -47.52279 | 2025-08-04 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d737790-1c83-3cda-b3bb-df4199e4a541 | -8.4223 | -47.45327 | 2025-08-04 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6f0b0d8-712b-36ac-b366-1cac4d28b3e2 | -6.67385 | -44.36987 | 2025-08-04 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aae7dc37-06b3-30ee-8518-07869ad8af18 | -6.1995 | -43.76186 | 2025-08-04 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7e622603-5fd4-3228-8bd6-9267a7703c79 | -7.6293 | -45.06794 | 2025-08-04 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94e20987-6af8-3aef-adfd-19b5b0a66814 | -6.64667 | -45.88831 | 2025-08-04 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5833ded2-e0ab-3cf1-8b74-7840a6446783 | -7.03409 | -59.85207 | 2025-08-04 04:34:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b49b5955-426d-3ab3-a9ce-04639f619da2 | -7.03516 | -59.85293 | 2025-08-04 04:34:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32747d2e-fe6a-3b57-ba7d-ad5de2ae0c4c | -7.99361 | -43.17588 | 2025-08-04 04:34:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 673e1b1d-5f62-3f80-991b-7b68709415d7 | -6.06909 | -44.67452 | 2025-08-04 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e9f9b112-647e-3e85-b579-b19ddec596a0 | -7.01703 | -59.83751 | 2025-08-04 04:34:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe84e183-cf47-3ad1-94d3-605408bcb035 | -6.62063 | -59.96286 | 2025-08-04 04:34:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0cd8752b-559a-35c5-aa41-10ccb9013202 | -8.0001 | -43.21616 | 2025-08-04 04:34:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 31350470-c8e5-31af-a9fd-8a36c06483c9 | -7.95403 | -43.90757 | 2025-08-04 04:34:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f6ec9211-6cf1-36da-a224-d28dae15e622 | -8.73789 | -46.39871 | 2025-08-04 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74d25335-6f3c-3f7c-9cae-7dc0fee93f3f | -6.61863 | -59.97364 | 2025-08-04 04:34:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8529fda0-bd7f-3d5f-9528-31ff88a817a5 | -5.87917 | -43.73842 | 2025-08-04 04:34:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca3ecf7d-d5f1-3c9e-9a6f-d723277c4c1e | -8.73503 | -46.41741 | 2025-08-04 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0b797b52-45a0-3ad2-bf37-987886fa2873 | -6.06549 | -44.67398 | 2025-08-04 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8207af67-8607-378f-bdb0-cc21a5746208 | -6.67082 | -44.36505 | 2025-08-04 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b9a2dc9-efca-33be-bc17-5ec60abb33bc | -5.54538 | -45.2017 | 2025-08-04 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 61fa99ac-7886-3a0d-9ed2-7d76c3922999 | -8.03092 | -43.14579 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 08cf3660-8d82-3595-bd1e-a4bb20383480 | -6.96664 | -44.50227 | 2025-08-04 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba78e9df-7efb-37ea-b63a-e92654731350 | -7.56325 | -44.89007 | 2025-08-04 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c61b7988-722f-33e0-b77a-b49da5e690a9 | -8.00266 | -43.17021 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 334c2a44-1065-31a6-bdc8-d0f19c019aeb | -6.70035 | -44.24525 | 2025-08-04 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82493c19-f064-3126-8cb7-8879a23510d1 | -7.4837 | -45.05151 | 2025-08-04 04:34:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9189ff6-d3e7-3146-97e1-f3558ca0707a | -7.01593 | -44.61717 | 2025-08-04 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e064e475-c99c-3fe1-af2b-e34c2a6d6b54 | -7.19594 | -44.48829 | 2025-08-04 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6937282d-aac6-30f1-accd-9264ec425a37 | -9.39595 | -45.50346 | 2025-08-04 04:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f4f4be16-d05b-3465-abff-23f39260a721 | -8.3067 | -47.52123 | 2025-08-04 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5ac24ee-7550-3ee1-af06-c9450687f21b | -6.24883 | -44.42219 | 2025-08-04 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 574f4447-2bc4-376b-8d59-cbf9169f808a | -7.99609 | -43.21555 | 2025-08-04 04:34:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 70505190-3689-3d7f-9c7f-f1636c1222e3 | -7.77042 | -45.22536 | 2025-08-04 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 54870c21-5184-3b26-ab17-8537161ad92b | -7.99866 | -43.14091 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 066530c4-9066-38fc-a9fb-ba1bfca7c75d | -6.61616 | -59.95107 | 2025-08-04 04:34:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0540557-cea4-39ac-9b62-78781bd311ea | -8.04419 | -43.11157 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 385c8cae-ce7f-3314-bab2-5b8e59514c1f | -8.00115 | -43.15215 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 45531019-9285-3277-8d26-3efd0dfe221f | -8.73217 | -46.41315 | 2025-08-04 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19d0561f-dd42-34fd-927b-37c4cb4efd37 | -7.08282 | -44.3708 | 2025-08-04 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19771463-8c92-32b6-92f5-6deb86619774 | -6.57071 | -47.03131 | 2025-08-04 04:34:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db2fcdfa-ee71-3563-a6ab-e2ccb50e4c39 | -4.12584 | -47.64539 | 2025-08-04 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| faca972c-ad25-3201-842a-ee63e4474c52 | -6.43939 | -45.15178 | 2025-08-04 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 20830d13-b277-3e99-8743-3d1e9d7a9741 | -7.99311 | -43.17939 | 2025-08-04 04:34:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 81f540ac-c841-3c17-b874-7cc77f5de203 | -4.12862 | -47.64938 | 2025-08-04 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 758206f8-05b1-357c-a803-3eb951e0bb33 | -6.70403 | -44.09526 | 2025-08-04 04:34:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60a6dc91-419b-3b3b-b9f3-e932aee36988 | -8.01877 | -43.17254 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a9acf604-8f35-3837-8ff3-7b9ea569adb0 | -8.36111 | -46.94093 | 2025-08-04 04:34:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2fc98438-43e8-3455-b178-e3019c8a7806 | -7.9502 | -43.90694 | 2025-08-04 04:34:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0f1d844c-c79c-354f-9a94-cdb9c2c4ffd5 | -6.43583 | -44.19061 | 2025-08-04 04:34:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8b657d59-2add-3c56-8dfd-07ad06098439 | -5.98488 | -45.52502 | 2025-08-04 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 428575f2-38e0-3737-bf51-b5e425a62fad | -7.99814 | -43.14447 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 106bb8ef-0ce6-3fd3-83f9-3ebbaa825b87 | -4.10864 | -49.2693 | 2025-08-04 04:34:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ab203648-1d0d-3932-82d0-0c15da3a8c15 | -7.77163 | -45.21721 | 2025-08-04 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d13df806-4f77-369c-971e-164c849784a1 | -6.20019 | -43.75724 | 2025-08-04 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b0150676-6bed-3921-9087-b99d91b5fb5c | -6.84513 | -44.28914 | 2025-08-04 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c91da680-6f6e-3f97-99bd-e761fd8810fb | -6.84883 | -44.28976 | 2025-08-04 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ff36e22d-df6c-3dc9-b3d7-2ae4822f32bd | -4.12807 | -47.65285 | 2025-08-04 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0430b11e-8de3-3597-8537-058ac1ed5303 | -7.69204 | -45.12653 | 2025-08-04 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cf03c49-d404-3c77-b78e-0af3f7064248 | -8.3845 | -46.92952 | 2025-08-04 04:34:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a61d126-fafa-3316-b992-ef569f54961c | -8.36929 | -46.91607 | 2025-08-04 04:34:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e85c3d36-0fdd-3d83-9a57-e45ff9d9741b | -8.73331 | -46.40567 | 2025-08-04 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 062bb807-98b5-3b7d-a4fe-895b20477733 | -7.38363 | -48.07938 | 2025-08-04 04:34:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d53c33db-8ada-332f-98ae-604467d45fb3 | -8.01423 | -43.1755 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| dcd5c79a-9e7d-3060-af9b-561a673603b6 | -7.38308 | -48.08286 | 2025-08-04 04:34:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1763e050-450c-3de0-894f-9fd818abfa7a | -4.73496 | -44.42898 | 2025-08-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README16.md)
