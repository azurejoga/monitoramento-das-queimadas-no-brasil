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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 063552f0-97f6-3086-b081-a92eacccdfcd | -22.51753 | -44.61135 | 2025-09-30 04:44:00 | NOAA-21 | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| bafcc711-4533-3b21-b714-a5efc9a612fe | -22.51812 | -44.60558 | 2025-09-30 04:44:00 | NOAA-21 | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| f8c79d37-edbc-370f-b905-2f4a18d61bdd | -22.5402 | -45.3235 | 2025-09-30 04:44:00 | NOAA-21 | DELFIM MOREIRA | MINAS GERAIS | Brasil | 3121100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7b6bc6a5-4b96-3344-9cc1-07e40e2d0978 | 2.10233 | -50.8765 | 2025-09-30 05:04:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2de6f2f-7ba5-38cd-b60b-b38ca9e97811 | 4.15732 | -60.01115 | 2025-09-30 05:04:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1f87894-d607-305a-b6ba-5eaa1cda64e5 | 4.15801 | -60.01579 | 2025-09-30 05:04:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03db0b20-c692-3ef9-b654-24c80eb04191 | -6.29951 | -43.80544 | 2025-09-30 05:06:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 837e8836-bc7f-3025-b27e-7deadff876a9 | -5.339 | -43.73749 | 2025-09-30 05:06:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 33.3 |
| d18fc43e-e430-37fd-b238-8107a7a61e9f | -5.97235 | -44.12989 | 2025-09-30 05:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f7f6c6ab-0c76-39b3-bf16-ab2b2c4e2913 | -6.34962 | -44.83496 | 2025-09-30 05:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be5e13be-a18b-3fcc-992a-7fe83a7b156b | -3.8089 | -47.5683 | 2025-09-30 05:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 177ec6ce-428e-33b8-9a11-bbcb212aa978 | -5.33263 | -43.73644 | 2025-09-30 05:06:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 5f1e5369-c7bf-3543-aece-5fffaccda3e6 | -3.47593 | -51.5978 | 2025-09-30 05:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 155299fa-b030-3e58-87ce-b4c0c76bbbfe | -5.7457 | -42.68066 | 2025-09-30 05:06:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d0654e10-5c48-397d-ad2e-0648b2fcf244 | -4.86904 | -45.05548 | 2025-09-30 05:06:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 681bf13b-672f-3f10-b782-fdd65ecd3d27 | -1.39519 | -55.17973 | 2025-09-30 05:06:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07160ba7-d18d-3c14-b2f5-f403bc540934 | -4.75522 | -42.5886 | 2025-09-30 05:06:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f0096fc4-9a68-3efa-bbdd-db66244fcf15 | -5.81517 | -42.78426 | 2025-09-30 05:06:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c36bae6c-3b76-323e-a15f-992e5781248b | -5.32717 | -45.23434 | 2025-09-30 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 760d69d6-f557-3cd0-8491-3031f452ac43 | -3.55048 | -50.33119 | 2025-09-30 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 069c7668-d00c-3e5c-994c-d1c5c41a4915 | -4.68001 | -43.26013 | 2025-09-30 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9de5f9bf-8f4a-3f70-9fac-348e92652c6f | -6.29985 | -43.80819 | 2025-09-30 05:06:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b7a5d052-f8c9-349a-8483-513d2c71cc53 | -3.98587 | -47.88559 | 2025-09-30 05:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e21864e3-cf3f-34b9-bf78-c58458cc81eb | -5.25155 | -43.74403 | 2025-09-30 05:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5e5166f2-7508-33a3-a1b2-111c1d6362c5 | -1.29215 | -54.17998 | 2025-09-30 05:06:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6811e1f5-8142-338d-9620-460a6c3ec6e5 | -4.29568 | -48.26982 | 2025-09-30 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2c617d9-2201-3d50-b67e-3c7bf2ab85e6 | -4.07642 | -47.31076 | 2025-09-30 05:06:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0f07423-3815-3ba8-8d86-5770920a946e | -5.97172 | -44.13453 | 2025-09-30 05:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e2c78ff1-fc92-37ca-9fec-7cd1cb3433f9 | -5.69125 | -42.6198 | 2025-09-30 05:06:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f2093991-01d6-3b59-b165-6f42de582224 | -4.58134 | -50.68983 | 2025-09-30 05:06:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9d5341a4-7173-36e3-b0e9-aaa2fe9a8ba6 | -4.25492 | -48.55453 | 2025-09-30 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76d15977-d3f9-3a4a-b7b0-fa0d543d44f9 | -5.81597 | -42.77847 | 2025-09-30 05:06:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3041a058-4f74-3260-a633-f9a706a39bea | -1.28772 | -54.18643 | 2025-09-30 05:06:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 85ea1419-1d9d-322d-b9a3-d2e2679c67ca | -6.42699 | -43.07796 | 2025-09-30 05:06:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3b5f5c42-088d-3769-898d-37ed649ea312 | -2.69074 | -54.7703 | 2025-09-30 05:06:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bb2cab0f-aff2-31fc-ac71-951ab3c5a57a | -3.81298 | -47.5743 | 2025-09-30 05:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 18cae634-ca19-399c-82ae-c13cc91e65a2 | -6.07623 | -42.62257 | 2025-09-30 05:06:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5acd534b-a400-3a37-8f86-bc757f9d6bfa | -5.74705 | -42.87637 | 2025-09-30 05:06:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8e13c793-3b02-3dae-b193-8871438d0dee | -4.39998 | -44.08245 | 2025-09-30 05:06:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7f41e5a-4878-3f1d-9f4b-ceda0b6d9ca5 | -4.64554 | -50.68021 | 2025-09-30 05:06:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6f9ac20-d8e2-3662-8c03-be989cc85fe1 | -6.27361 | -43.65652 | 2025-09-30 05:06:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a63cc42e-3d06-369c-ae3d-5a1dc1f3bf8e | -3.22469 | -49.34542 | 2025-09-30 05:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17ed695c-db2e-3ff2-839b-7d5d566e3924 | -5.76883 | -43.8316 | 2025-09-30 05:06:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8fded993-b440-3169-bb49-72e03cb0315f | -4.89384 | -43.4732 | 2025-09-30 05:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4e6cc7b0-52ca-3e4a-8da2-862f27ad27b0 | -5.05069 | -45.31258 | 2025-09-30 05:06:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8bc1e397-0cf3-3824-a3af-22aa44fe342b | -3.85692 | -54.08195 | 2025-09-30 05:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bd08e0b0-3d0b-3149-9489-3ccb6fe9e6c7 | -5.5744 | -44.85647 | 2025-09-30 05:06:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b5a4ca05-0220-344d-80c5-03e64e9d934b | -3.28172 | -50.03193 | 2025-09-30 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 412a9556-7788-39f3-940b-4818d0739bd9 | -1.28827 | -54.18295 | 2025-09-30 05:06:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 875b1479-6e97-3171-8ce9-7b6f0c6ba761 | -3.28099 | -50.03503 | 2025-09-30 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cc10034e-c599-3c0f-994d-2e0d2456896a | -6.45745 | -44.00235 | 2025-09-30 05:06:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b38ab5cc-9c00-38bc-b868-0f360f03dddd | -4.86319 | -45.0546 | 2025-09-30 05:06:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8eb7a548-b0e1-3835-8ebd-77a7fc578698 | -4.25881 | -48.55965 | 2025-09-30 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2f9d28af-b9e4-31e5-acce-fac54fd71bdc | -4.58055 | -50.69498 | 2025-09-30 05:06:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94090297-1e8e-3ebc-9c8c-349a9d6c2d6b | -6.24861 | -43.65274 | 2025-09-30 05:06:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ebf8f8da-7d66-36a4-9c23-7b1dfdd41171 | -3.25629 | -50.11515 | 2025-09-30 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3aa924be-bf38-36bb-a7c6-3087a4855e4f | -5.73892 | -42.67979 | 2025-09-30 05:06:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| cf62ed09-eeea-3c44-b510-8d65a7670b29 | -5.82277 | -42.77959 | 2025-09-30 05:06:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cfc5080a-639a-3a3f-b5e2-a0f5150d5faa | -5.62573 | -42.83158 | 2025-09-30 05:06:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| df58effe-4ac3-37ee-b0c1-c066444b68e5 | -4.86271 | -45.05243 | 2025-09-30 05:06:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d1e58561-4393-3600-83f3-b6fd0c06175a | -5.76741 | -43.83595 | 2025-09-30 05:06:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2382d440-c29c-3f84-921a-999a804789a4 | -5.74651 | -42.67462 | 2025-09-30 05:06:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6f5802eb-8eaf-37b6-9935-ca8e8eaf37ae | -3.28506 | -50.03566 | 2025-09-30 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f9fe9e41-b7ae-325f-a256-ab2dfefa7939 | -3.05605 | -48.71022 | 2025-09-30 05:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2abdafd5-0088-3506-8804-88bc250210ed | -5.31446 | -44.78715 | 2025-09-30 05:06:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aca4a58f-59f9-32c0-bae9-ac7111d187b2 | -4.40427 | -44.39464 | 2025-09-30 05:06:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 249266a3-cae4-33a1-81fd-fff22b35147a | -5.66619 | -45.29768 | 2025-09-30 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5cf1765-030f-331f-a9fb-e2ba6f8c3c4c | -3.33546 | -50.24842 | 2025-09-30 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 606684d3-34d8-3962-9ced-111a9b76ea26 | -3.09618 | -47.01379 | 2025-09-30 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| af200b72-a155-3f31-9572-2437f48b0060 | -3.25386 | -49.12415 | 2025-09-30 05:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29aee30b-8852-356b-b8ff-b782bb6a82ad | -3.8729 | -55.40229 | 2025-09-30 05:06:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2744e3ab-ce71-360d-bf38-7e7f5b06ba82 | -5.74489 | -42.68707 | 2025-09-30 05:06:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ae0b6a4f-8caa-3ea4-98a7-5361554f7954 | -5.32775 | -45.23027 | 2025-09-30 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed6cb93b-5854-3ab3-b8ac-5ed65ffaa43b | -3.45241 | -53.83421 | 2025-09-30 05:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 603bdd48-23b2-3a2e-8cab-05479229b43e | -4.29329 | -48.27164 | 2025-09-30 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b033c54c-9a57-303f-a131-ea4bea94f2ba | -3.93828 | -51.33075 | 2025-09-30 05:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f52301cd-4bae-314b-8d9b-53e02737156f | -4.40362 | -44.39912 | 2025-09-30 05:06:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56e686c4-a4ec-3193-b86c-c203c0276416 | -6.30521 | -43.81173 | 2025-09-30 05:06:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0bb3c917-210f-3862-8839-e471892b8048 | -3.10178 | -47.01155 | 2025-09-30 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 69572bbe-62c4-35d4-b52d-448e852672ef | -6.5563 | -43.42208 | 2025-09-30 05:06:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| edc12dbd-a319-3841-8356-3cb899ea991b | -2.07007 | -56.87872 | 2025-09-30 05:06:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 60192ea1-488e-3625-b205-1923f97284f1 | -2.13288 | -46.47142 | 2025-09-30 05:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a177c10d-ccaa-3a90-a158-9c00fc723ff7 | -5.77451 | -43.83182 | 2025-09-30 05:06:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a41307fe-cf00-34ff-b769-5b5ff3042d82 | -5.23897 | -50.92531 | 2025-09-30 05:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0579cc62-2cca-369e-b318-8350935baf47 | -3.38309 | -52.71534 | 2025-09-30 05:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1b59481-4622-3bf4-a22a-402a53ed12a4 | -3.05243 | -48.71152 | 2025-09-30 05:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3747fc2e-d914-3a1b-a6d8-9457aaed050b | -2.07066 | -56.87498 | 2025-09-30 05:06:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 81cb15f7-aae6-38af-95f7-b4ef95abf611 | -3.68083 | -53.97881 | 2025-09-30 05:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af08d2b7-9eee-3d5c-8eb4-5d526368c264 | -6.47311 | -44.21753 | 2025-09-30 05:06:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7ffb919-eb03-34ca-b42e-c964252729aa | -3.09706 | -47.00812 | 2025-09-30 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 0dad843b-d0e8-3431-b62b-7ce245238936 | -5.52705 | -46.38216 | 2025-09-30 05:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e3a3b549-ce3c-3201-9f24-c4d0da91fb2b | -6.2476 | -43.65258 | 2025-09-30 05:06:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac39dc02-35b0-38b4-8052-05714ea73559 | -4.66661 | -46.46566 | 2025-09-30 05:06:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6dcb3091-afcd-3dd4-aa87-e132e2a3d024 | -3.50074 | -52.46732 | 2025-09-30 05:06:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2fe529b-6a93-3e52-90f2-a468a896cd49 | -1.8346 | -54.66419 | 2025-09-30 05:06:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8a9ab5b-c801-36cc-a817-fc90652a18c3 | -6.26774 | -43.65084 | 2025-09-30 05:06:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8780990-f6ee-3307-abe9-287da954dc9f | -3.84593 | -52.28602 | 2025-09-30 05:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83eb7e4d-a967-34a1-a0c6-b5027fcc8a0f | -3.10704 | -47.00965 | 2025-09-30 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| db63da23-9adc-3787-99b5-398922ca9080 | -5.82335 | -42.78582 | 2025-09-30 05:06:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 66a61e9b-ed7a-35f6-8c9c-fe9ee92c58a2 | -2.94887 | -48.94669 | 2025-09-30 05:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README82.md)
