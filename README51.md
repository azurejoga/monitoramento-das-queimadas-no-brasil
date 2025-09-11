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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42e7398a-89ff-3e26-8813-1380517d7760 | -7.65588 | -49.5013 | 2025-09-11 04:21:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38378f85-22ce-3ac6-95a6-85cec9c86492 | -6.91078 | -44.55401 | 2025-09-11 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1f17dea6-d9df-3f08-9c17-f20f9a84bf1f | -6.7267 | -51.95727 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5c30ea00-f22a-3ace-88c1-de2a2f70bd95 | -5.94281 | -45.71896 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8e97617-8e7d-3477-b30c-1c7ca76968ae | -5.87617 | -45.66093 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f021bf78-0d1c-3e66-b19d-d8a66f8d9ce5 | -6.56107 | -42.92175 | 2025-09-11 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25521dfc-fc4b-3d69-a5e5-425b8700fb7b | -7.70279 | -45.15052 | 2025-09-11 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ab6f3eec-2782-32fc-967b-1337d4a87ac7 | -5.52771 | -44.34298 | 2025-09-11 04:21:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cde91925-0dfc-3f3e-85c2-990ae36b820f | -8.6628 | -45.7377 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1047173-bb6f-3c7d-a494-879657508d46 | -5.73451 | -45.27718 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a999aa89-1399-34d6-b21d-c8b36edb4437 | -8.03764 | -49.04928 | 2025-09-11 04:21:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2e5d0e14-7853-3203-b23b-2473086b1fbc | -8.73533 | -47.09265 | 2025-09-11 04:21:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e391cb1c-a65f-3ac8-ad21-6921f0ecd6c0 | -6.42825 | -44.49137 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07b9f5a6-5d2f-3534-a7b6-04eb2395b16e | -6.64911 | -42.96211 | 2025-09-11 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb0cbe50-0e77-3e97-8755-5fc2618444ce | -7.22184 | -45.30992 | 2025-09-11 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8932b5e9-6901-304e-82b6-8e162160a5ec | -7.70722 | -45.14408 | 2025-09-11 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e7d0a946-7b32-3484-9b69-596631824b87 | -5.72948 | -45.28719 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99781eca-8114-3ea5-872f-08f0dedb3df9 | -8.42954 | -47.26876 | 2025-09-11 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d3c184b9-2350-3014-80f4-9e47c743dc02 | -7.46386 | -45.29091 | 2025-09-11 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84a45e60-bce7-3387-ad4b-5913033cf9ab | -7.91916 | -44.8778 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1a08b45-38df-37e8-acf7-31aefedae3ce | -6.54513 | -42.43943 | 2025-09-11 04:21:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c7c5d6d5-128e-3f14-9120-2e99088ae2e6 | -8.52264 | -45.70014 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 676bd2f2-582e-3973-a7d6-3ffbe546f594 | -6.30897 | -44.58213 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c9c85a5-6e89-304b-a417-f16360310d3b | -8.04523 | -49.05061 | 2025-09-11 04:21:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c0a1ead4-ece7-38b4-8cc9-774110eb30c1 | -4.21997 | -46.36113 | 2025-09-11 04:21:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| afd28116-f607-3372-bada-f4b0c4e8dc0f | -4.83806 | -45.35586 | 2025-09-11 04:21:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ee0b4e2-ba30-30db-9fda-4926ae25801f | -8.65781 | -45.72604 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41fb6212-9b05-3b82-810f-692f75dafd05 | -4.45063 | -43.92093 | 2025-09-11 04:21:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14a26d93-c263-3aa1-87ea-043f4572534c | -5.76443 | -45.52035 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9fd04f36-33b5-3f7e-b005-f4ee383d3393 | -5.86181 | -44.2209 | 2025-09-11 04:21:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 96e9c21a-3a76-3bc3-96f1-ec199ffc8d84 | -8.34974 | -45.06013 | 2025-09-11 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e073dfef-0c72-3cbd-ad45-4bb8c667e6fd | -5.72655 | -45.41291 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d3042449-468a-3244-92a2-2796736e7c8c | -8.4434 | -47.27108 | 2025-09-11 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 336e78a2-de22-36cf-8a40-4a7c1040d017 | -5.77859 | -43.12922 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dcef13cb-9561-3fd9-aeed-403c7e73e511 | -7.50495 | -48.24307 | 2025-09-11 04:21:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e58a427-51bc-32ff-aa85-b11944a125ec | -7.7859 | -50.76507 | 2025-09-11 04:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 8dfc142f-3cb8-3aac-b667-fdba05daf495 | -7.88177 | -46.04334 | 2025-09-11 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 885c6d9a-3c1a-3a9e-8d1b-af468d8a7078 | -5.42816 | -45.87758 | 2025-09-11 04:21:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 87f24f33-c4a5-3ec1-85a1-ad135c0c1d01 | -4.55922 | -43.74652 | 2025-09-11 04:21:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec293a63-ccf5-33a4-a93c-c950b269fd54 | -5.86291 | -44.21394 | 2025-09-11 04:21:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4813d0c-c423-3c51-ad01-fd87a54f83e7 | -6.38667 | -43.50763 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ab59b17-2022-3893-a1df-4375e7a10f90 | -6.49206 | -49.1794 | 2025-09-11 04:21:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 363ee4d7-0fbe-324a-bc76-b95d4309e60d | -5.89819 | -45.80355 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e8b3999-9454-3d9a-8cc7-c41cd99e19d4 | -6.1969 | -42.65965 | 2025-09-11 04:21:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c1453c66-e50e-3b34-a1ff-b058670c7020 | -8.74888 | -47.11792 | 2025-09-11 04:21:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 059dbdcd-db5d-3f81-98b3-9abccd048f0f | -3.24084 | -50.7975 | 2025-09-11 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c463619e-4d1e-3610-823c-b46c057ef7b2 | -8.17032 | -46.06792 | 2025-09-11 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4852883d-5e7e-3f6f-9b71-d9c0e0eac5ee | -6.52831 | -44.60655 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 014804e8-bd6b-32c2-8f03-2da4beb6aa02 | -3.31888 | -54.91142 | 2025-09-11 04:21:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab61966d-f703-3542-b277-b9c0a07524bf | -7.1035 | -50.758 | 2025-09-11 04:21:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c3e083ea-58a7-3910-8647-91377eab5015 | -8.03278 | -44.49479 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13167cde-47a1-385f-aba0-2533b9cefaa7 | -7.87899 | -46.72718 | 2025-09-11 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60755169-1b07-371f-8dee-85722a9f1999 | -6.24673 | -44.80345 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 712cc690-714b-3ad8-b159-0d8862f29e26 | -6.30989 | -45.65699 | 2025-09-11 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7882543e-e588-3ac4-8c04-f04ddce22c7d | -7.20104 | -44.94594 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7b360f91-63a4-39cb-861c-913fc60cb1bf | -7.85243 | -45.50698 | 2025-09-11 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3c92c7bf-764f-3ebc-ad39-e22ffb9efebc | -7.55955 | -48.20845 | 2025-09-11 04:21:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67698aaa-0478-3b27-b7d9-7796237d4691 | -8.44063 | -49.113 | 2025-09-11 04:21:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2cc59b16-9d79-3b74-aac8-4d4d89ef9cb8 | -8.74221 | -47.09378 | 2025-09-11 04:21:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b7faf863-f5d0-3c5b-bc1e-5991ce6385f9 | -5.93816 | -45.94968 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7fdb4fda-ffd7-3152-a0e2-ae32f46826f3 | -9.0497 | -45.72771 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ea25aec-9c0b-3214-9bb7-e943ff5c915d | -6.27949 | -43.38874 | 2025-09-11 04:21:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16f13726-a316-3787-a522-c576477093be | -3.89409 | -42.54998 | 2025-09-11 04:21:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cbaf1b8f-1c31-3274-9559-30e04e5bcf86 | -5.3579 | -43.40442 | 2025-09-11 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49e25642-3302-33d4-817f-265f935fdb10 | -6.67175 | -44.12263 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14235e28-90fe-3dbc-b414-7d0e1b544556 | -5.74391 | -45.36869 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8d069d7-a88f-3e20-baec-11097c448f5e | -6.24728 | -44.79999 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dadbe3ce-cdf2-3b28-a064-8e2e82ceb087 | -6.3732 | -45.16287 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 7b53079d-4e4d-31b0-8f17-4add5900af40 | -6.89781 | -47.91825 | 2025-09-11 04:21:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f47ceaa1-e48e-3ab6-9dfc-8e9a884f5e39 | -6.41309 | -44.39286 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0b1d847-d8ce-30a0-8348-4252655414ef | -7.42257 | -45.87181 | 2025-09-11 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ea197a69-195d-32dc-ae3d-6ec095ff11a0 | -8.7507 | -47.10666 | 2025-09-11 04:21:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e0f9d83c-1716-3d99-90ab-028f11da01d7 | -5.8164 | -45.68127 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8b27609-7ff0-3643-9f49-dd50ffbca487 | -8.077 | -50.18036 | 2025-09-11 04:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5c85f8dc-aec6-3a79-b69f-e9bde15504cd | -8.5271 | -45.69362 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f0b768f-ed6a-3a48-a968-830c6da8ea35 | -8.48027 | -47.28511 | 2025-09-11 04:21:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3cf65d14-b4cf-358a-9fe7-a8a0ccac7ba1 | -7.72947 | -50.7376 | 2025-09-11 04:21:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bfd10428-6e14-3ebf-aab6-6b9b3e94268c | -8.74827 | -47.12168 | 2025-09-11 04:21:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e5b0e5c5-aaf1-3630-9d23-355e4de9a3a6 | -5.48121 | -44.11894 | 2025-09-11 04:21:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00e564b8-126c-3873-aab0-42ceb5f97698 | -6.67897 | -44.12016 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f792484-d745-3558-b43f-9f59d464c6a2 | -6.4017 | -47.32761 | 2025-09-11 04:21:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb43285e-1f76-3687-b763-eee4b211bec5 | -5.23018 | -43.69415 | 2025-09-11 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac2494df-b597-32a8-be30-86482c0740e4 | -4.96169 | -43.22302 | 2025-09-11 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9068e39a-e4a1-3007-95ec-2db97300deb7 | -6.5532 | -43.97889 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd9dbae3-4bf9-3695-b293-aa05778b8f9e | -6.9611 | -44.81841 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b5ef8ef-cc95-384d-979a-025728d42a25 | -5.69246 | -43.34007 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d51836ec-4501-3914-b874-8916d41165ff | -7.42593 | -45.87236 | 2025-09-11 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f2a54604-44bd-33d5-8cdc-38253ba58842 | -3.79759 | -51.16211 | 2025-09-11 04:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3c602af7-d014-3c45-b816-1ec0b40474ea | -8.5232 | -45.69662 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7139d2c-cabd-359e-aa74-97442ee690d2 | -8.02339 | -48.65028 | 2025-09-11 04:21:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a1bcda54-3ded-362f-bcd1-11ea3c4369d9 | -3.08323 | -48.82091 | 2025-09-11 04:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83375e1b-dd73-31c6-ad80-1877682f8630 | -8.19715 | -50.10952 | 2025-09-11 04:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2be2b898-ff16-3d0c-af79-49cd6377dc41 | -5.82997 | -45.27404 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7392d4a3-f1bc-3834-80f8-0b70ac6e065c | -4.93333 | -55.77895 | 2025-09-11 04:21:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 355d108f-7d24-3ad1-acdf-ef40e80b080f | -5.73283 | -45.28772 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4dc0d43-bb28-380e-be84-981b3b0592bb | -7.15557 | -39.41479 | 2025-09-11 04:21:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 716eb713-8834-3077-be4d-4335e52096e0 | -2.56704 | -48.95672 | 2025-09-11 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b54d2fa6-761f-3897-b85d-2b04cac039c1 | -5.92122 | -53.83354 | 2025-09-11 04:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57e5600e-2c5c-34ca-b1b5-7938ee346913 | -9.07138 | -45.6988 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 879ba558-a2a1-3618-834e-284fe71cc1fc | -7.32424 | -44.3803 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README52.md)
