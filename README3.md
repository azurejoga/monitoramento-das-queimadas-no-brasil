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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6d5836d-47b1-32aa-b488-c389593a9649 | -9.81284 | -38.10331 | 2026-02-25 03:25:00 | NOAA-21 | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6a7ddf69-e041-3807-bf99-637b9be3f760 | -9.99129 | -35.99968 | 2026-02-25 03:25:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| dbcca461-e132-3e60-beeb-09add92ca8b3 | -9.7988 | -36.1213 | 2026-02-25 03:30:00 | GOES-19 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 86.9 |
| 2e26e5d6-99f2-31cf-ac9e-6255b6b2dcc8 | 1.4864 | -59.9308 | 2026-02-25 03:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 93.8 |
| d35efddb-f75b-3ed6-a346-df2784442c58 | 1.4864 | -59.9498 | 2026-02-25 03:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 135.8 |
| 0c27514f-81c7-3149-bb7f-aeaf49ff22bf | 1.5046 | -59.9497 | 2026-02-25 03:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 169.0 |
| d294b735-fa90-3136-8b6b-2973272f2fb1 | 1.5229 | -59.9495 | 2026-02-25 03:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 47e808c6-08f6-3b11-bd49-32033e79ca5f | 1.5229 | -59.9305 | 2026-02-25 03:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 48bef8f4-a42a-3683-881f-08ac143d23e0 | 1.5046 | -59.9306 | 2026-02-25 03:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 180.2 |
| ce3c7972-777c-35f9-a435-5850895f9e8b | 1.5046 | -59.9497 | 2026-02-25 03:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 197.9 |
| 00d6bf0d-151f-34f9-83de-31cfdac093d6 | 1.5046 | -59.9306 | 2026-02-25 03:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 172.5 |
| 863b80f9-4785-3779-af8f-d29600780820 | 1.5229 | -59.9305 | 2026-02-25 03:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.4 |
| d9391517-96c6-3369-969c-2181227f5bc5 | 1.5229 | -59.9495 | 2026-02-25 03:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 244c48dd-7a6f-37c0-b668-25208840d0d6 | 1.4864 | -59.9498 | 2026-02-25 03:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 155.3 |
| 1c8689fc-f23b-3fa4-b33b-f063d3eb9c84 | 1.4864 | -59.9308 | 2026-02-25 03:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 88362a63-add4-3fb1-ae7a-6d9d7713014b | 1.5229 | -59.9495 | 2026-02-25 03:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 63cc5388-3a29-3e6c-87cb-65510fd78437 | 1.5046 | -59.9306 | 2026-02-25 03:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 192.5 |
| cb4dd12d-de85-3547-843d-19f0f0d423cf | 1.5229 | -59.9305 | 2026-02-25 03:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 4aa9b9d2-2554-3fa8-8acc-fc07cca5c390 | 1.5046 | -59.9497 | 2026-02-25 03:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 209.1 |
| f6a3ff33-9dda-3ae7-8f8d-337694c2d194 | 1.4864 | -59.9498 | 2026-02-25 03:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 160.7 |
| 216ab44a-2b81-3ae1-80d3-b9330a5c1cac | 1.4864 | -59.9308 | 2026-02-25 03:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 581a269b-84f9-3181-98ad-9ffeb2c2e783 | -6.07875 | -37.30953 | 2026-02-25 03:53:00 | NPP-375D | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6d8dea42-ec25-32a0-a820-261e91bb2975 | -5.40442 | -37.33471 | 2026-02-25 03:53:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d9573ed7-1ec7-3f8a-8c4a-4d352713231d | -7.88758 | -35.23067 | 2026-02-25 03:53:00 | NPP-375D | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 767c67af-ece4-3c2d-aceb-eda98adf0fe4 | -5.41539 | -37.48046 | 2026-02-25 03:53:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 22bff586-0079-3fb7-ad21-e4db7429e756 | -6.07541 | -37.309 | 2026-02-25 03:53:00 | NPP-375D | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7c79b613-9691-3090-b0e7-43f4822964c5 | -9.98047 | -36.00162 | 2026-02-25 03:55:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 27c9f72d-99b3-3ab9-83fe-5903bdaa0e96 | -9.81025 | -38.09866 | 2026-02-25 03:55:00 | NPP-375D | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1bc2f432-0794-3ccf-aa16-b2a02bb72f33 | -9.98444 | -35.99846 | 2026-02-25 03:55:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| c80fcedb-bad2-3ceb-9e52-bd81d3b015a1 | -9.23079 | -36.31876 | 2026-02-25 03:55:00 | NPP-375D | CHÃ PRETA | ALAGOAS | Brasil | 2701902 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bd40938e-a1de-36ff-b15b-7bea6958bfd4 | -11.01375 | -45.07713 | 2026-02-25 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8e48c77-9c76-387c-b1fe-e64dc38a60bd | -9.81358 | -38.09919 | 2026-02-25 03:55:00 | NPP-375D | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| de46587a-1704-3641-8e35-4696a2d31acb | -9.62091 | -36.9687 | 2026-02-25 03:55:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4208c733-fcf0-389f-b465-0a8f30c6e599 | -9.92994 | -37.45304 | 2026-02-25 03:55:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 098164d0-db7b-360f-8449-8505041d6e48 | -9.41368 | -35.55844 | 2026-02-25 03:55:00 | NPP-375D | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 226d7326-c430-3a04-8fcf-f51931fad73f | -9.62036 | -36.97222 | 2026-02-25 03:55:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4dfde42a-aff1-3f41-81bc-1d2c682b9d6a | -9.40966 | -35.56166 | 2026-02-25 03:55:00 | NPP-375D | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| e8b6df82-b814-3539-bf66-728aaa7713ba | -9.41252 | -35.56597 | 2026-02-25 03:55:00 | NPP-375D | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3d710b45-e113-3760-951f-f383a74d055c | -9.81301 | -38.10272 | 2026-02-25 03:55:00 | NPP-375D | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 97aec01b-dabf-3517-9964-18c1d8246878 | -9.98785 | -35.99898 | 2026-02-25 03:55:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 98a6458f-14de-3ea1-92c7-8c58f7a6cb4a | -8.2422 | -38.0689 | 2026-02-25 03:55:00 | NPP-375D | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6968e674-9687-3149-8870-d40350eee58e | -9.4131 | -35.5622 | 2026-02-25 03:55:00 | NPP-375D | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 2bbfc6eb-723d-3191-b637-bc9e44242be9 | -9.99126 | -35.9995 | 2026-02-25 03:55:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| e9495baa-5a8f-3a00-99c9-9b053b164c1b | -22.6757 | -43.47858 | 2026-02-25 03:57:00 | NPP-375D | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 83c59911-e3d3-306e-9e81-de71fd6581b1 | -29.59508 | -54.20918 | 2026-02-25 04:01:00 | NPP-375D | SÃO PEDRO DO SUL | RIO GRANDE DO SUL | Brasil | 4319406 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| 05de1823-02f7-32a4-bfd0-34fe978c3cb4 | 1.4864 | -59.9498 | 2026-02-25 04:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 150.4 |
| 5271be3a-6927-3e1f-935a-93437b82a9fd | 1.4864 | -59.9308 | 2026-02-25 04:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 93.6 |
| ffd62fc5-39c5-309b-8da6-1282b35d8426 | 1.5046 | -59.9306 | 2026-02-25 04:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 170.2 |
| 2924e228-3f89-36f0-a909-113803ffddf3 | 1.5046 | -59.9497 | 2026-02-25 04:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 217.8 |
| 99bbf704-c84f-3cd1-af12-3946c997d0c6 | 1.5229 | -59.9495 | 2026-02-25 04:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 2296c6ae-c43f-3d72-92ef-391b9b16e193 | 1.5229 | -59.9305 | 2026-02-25 04:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.0 |
| b6028f9d-fe7e-34ab-9d30-df26153be6b7 | -9.98886 | -36.00133 | 2026-02-25 04:16:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 5c32cd8a-1384-306d-b2c8-7ac1cad715cf | -9.81168 | -38.10231 | 2026-02-25 04:16:00 | NOAA-20 | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| aac854da-ccbf-3203-92d1-fceda8e46370 | -5.7783 | -47.81902 | 2026-02-25 04:16:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5359935e-9bfb-348b-a313-ceebd20f1740 | -9.99069 | -35.99686 | 2026-02-25 04:16:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| 9e823037-1c30-3d8b-9721-fe72d9f6fc82 | -9.92973 | -37.45334 | 2026-02-25 04:16:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1752a055-49d7-3350-bf8b-d899e5b3cabd | -9.98964 | -35.99558 | 2026-02-25 04:16:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| bf122fe3-dee4-3d59-a549-b733a9c349f0 | -9.97895 | -36.00011 | 2026-02-25 04:16:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ce8f3c21-388a-38f2-a318-b1a185dee011 | -12.23998 | -44.22894 | 2026-02-25 04:16:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8eca063b-a226-3716-b1c7-6b61163c633f | -12.24053 | -44.22542 | 2026-02-25 04:16:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b9b4a3b-0a44-31ab-9157-794a9b1209f9 | -9.81223 | -38.09844 | 2026-02-25 04:16:00 | NOAA-20 | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f082e2be-daa4-3d2f-829b-ea3b1cf338d0 | -6.077 | -37.30848 | 2026-02-25 04:16:00 | NOAA-20 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6397fe6b-0e56-3677-bd9b-645144e36cff | 1.5046 | -59.9306 | 2026-02-25 04:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 169.6 |
| 77c4f534-2bcf-3c19-8452-b8aced88be61 | 1.4864 | -59.9498 | 2026-02-25 04:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 160.4 |
| 935f1004-d254-3b4b-b52a-b426e621a097 | 1.5229 | -59.9305 | 2026-02-25 04:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 121c591a-57a9-3a60-a4f5-5492efa7fef4 | 1.5229 | -59.9495 | 2026-02-25 04:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 03e6ac04-53f1-34eb-9a5b-acc7d8d2db24 | 1.4864 | -59.9308 | 2026-02-25 04:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 11abb578-cdaf-3754-ae53-231799fc69f3 | 1.5046 | -59.9497 | 2026-02-25 04:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 221.8 |
| f48eef01-2d9f-3e06-a608-9f14a3946b0d | -22.69905 | -43.34576 | 2026-02-25 04:21:00 | NOAA-20 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 448b6dad-db8b-3b8a-91a6-69bfbca8f8e7 | -22.69761 | -43.34813 | 2026-02-25 04:21:00 | NOAA-20 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2cec00cb-ac77-32f6-b825-3a6fe8f7d2da | -29.596 | -54.20601 | 2026-02-25 04:23:00 | NOAA-20 | SÃO PEDRO DO SUL | RIO GRANDE DO SUL | Brasil | 4319406 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| bbbc3972-51d4-3b6a-a2c7-e235c8cc650e | 1.5229 | -59.9305 | 2026-02-25 04:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.9 |
| b028bc8d-4620-37b8-ae55-15526a44f7ba | 1.4864 | -59.9498 | 2026-02-25 04:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 158.8 |
| 0f4ca447-9071-3326-93c9-66417529b974 | 1.5046 | -59.9497 | 2026-02-25 04:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 225.4 |
| 5a7ec449-0d53-325d-a96a-2b3d3d250b8e | 1.5229 | -59.9495 | 2026-02-25 04:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.5 |
| a4d6ccb0-631c-3b81-928d-a4a6f2d83907 | 1.4864 | -59.9308 | 2026-02-25 04:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 99.3 |
| e423beb4-2ef6-3352-aaec-43f9d4609936 | 1.5046 | -59.9306 | 2026-02-25 04:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 203.7 |
| 7fcdab8a-f5e7-39a6-948f-edbf11910a9d | 1.4864 | -59.9498 | 2026-02-25 04:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 157.5 |
| 4cde9129-faf1-3b78-acc3-f6b077b96d2c | 1.4864 | -59.9308 | 2026-02-25 04:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 5909479d-c531-3d7c-9280-e7a20c097aa7 | 1.5046 | -59.9497 | 2026-02-25 04:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 198.6 |
| dd10d42c-0a7a-3b9c-a89a-e1eab4cc47ca | 1.5229 | -59.9305 | 2026-02-25 04:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.2 |
| df8865e9-c150-30fc-8a4e-926c37c96a07 | 1.5046 | -59.9306 | 2026-02-25 04:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 215.6 |
| 009dbc75-9939-3804-af09-091f2f262d9d | 1.4864 | -59.9498 | 2026-02-25 04:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 148.4 |
| e8df76b4-c0e4-3dc8-97ea-1350f977d422 | 1.4864 | -59.9308 | 2026-02-25 04:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 207450fa-3a62-3575-beb2-6da2e03322de | 1.5229 | -59.9495 | 2026-02-25 04:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.1 |
| fbe25a48-399e-3bac-8240-2f9854ccadba | 1.5046 | -59.9306 | 2026-02-25 04:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 218.7 |
| 8684358d-4be3-38b4-a172-95f4f78f47b1 | 1.5046 | -59.9497 | 2026-02-25 04:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 203.0 |
| 1ab6a791-4c0d-351c-bb0f-cfc1d362a552 | 1.5229 | -59.9305 | 2026-02-25 04:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.7 |
| a8d07e2d-eb92-350e-8886-68807850114a | 1.5046 | -59.9306 | 2026-02-25 05:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 237.0 |
| 3b70b42c-27d9-3585-9316-9a9b44accd41 | 1.5229 | -59.9495 | 2026-02-25 05:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.1 |
| dadf9198-2133-38c9-bd7b-23be17ab166d | 1.5046 | -59.9497 | 2026-02-25 05:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 194.3 |
| 90ad05ad-2374-3246-8360-c73c12f6ac9d | 1.4864 | -59.9308 | 2026-02-25 05:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 143.1 |
| 8cd5130a-7a24-3795-9970-5bc0eae7c99c | 1.4864 | -59.9498 | 2026-02-25 05:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 164.1 |
| 3d4650bd-d632-3262-bb51-1b2616799d5d | 1.5229 | -59.9305 | 2026-02-25 05:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 3bee40bd-eb2b-3fe2-84ad-8a5046ad4863 | 4.77934 | -60.15626 | 2026-02-25 05:01:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e79e4f54-c50c-3db7-9552-0d1cd9681875 | 3.92875 | -60.05942 | 2026-02-25 05:01:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2bade2d6-4d2c-3cf1-b2d0-6f66b0e6f64b | 3.9243 | -60.06007 | 2026-02-25 05:01:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ed35888d-30bb-3724-9f96-2fd86295106c | 4.78202 | -60.15453 | 2026-02-25 05:01:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2512a997-f75b-33e6-a4b8-7943d7351bb1 | 4.77873 | -60.15202 | 2026-02-25 05:01:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 927ee557-e0af-3111-97de-e01b65320305 | 4.06453 | -60.18567 | 2026-02-25 05:01:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README4.md)
