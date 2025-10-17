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
| 59c1c1b4-d36d-3359-b9f4-9be271757d7f | -6.19961 | -41.74879 | 2025-10-17 00:13:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 272bf412-754a-31d5-85a4-1e1d84871551 | -4.9515 | -45.06667 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7a32d463-0ceb-321d-b34c-a86e62b12943 | -7.46501 | -42.15598 | 2025-10-17 00:13:00 | TERRA_M-M | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| cfea0cd6-3851-31d1-b5a0-2aea537613f7 | -8.49906 | -48.50563 | 2025-10-17 00:13:00 | TERRA_M-M | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0a55065f-2754-3dc2-a4de-2b12bc7d4a74 | -8.23641 | -43.44123 | 2025-10-17 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 5b36b5e2-fb58-3e2b-87c5-a546d8822570 | -5.93467 | -43.79366 | 2025-10-17 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e89b5f51-b153-333d-8d34-dd44969b8b7e | -6.25695 | -43.91648 | 2025-10-17 00:13:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c7e2f3b0-2d2c-3c3d-8be1-4dce432bb057 | -6.7584 | -42.37191 | 2025-10-17 00:13:00 | TERRA_M-M | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 10dd1dc0-1eab-3a73-8447-c1f81c9c3b0d | -7.84337 | -45.46043 | 2025-10-17 00:13:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4b6d3fe3-c5cc-3bb7-b919-5929d4903d90 | -7.02865 | -41.81735 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| d1c519c0-b53e-3f71-882d-c521b2712c04 | -8.19927 | -43.30749 | 2025-10-17 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 4e08cb81-c291-32dc-863d-6dfa186ab5e7 | -9.23234 | -48.58386 | 2025-10-17 00:13:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4f0dda94-cf6a-3eee-aa15-cb60b46380a4 | -8.39777 | -46.2215 | 2025-10-17 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| dbc6a81a-6365-3b97-b886-a494f064c8ce | -5.92573 | -43.79492 | 2025-10-17 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 881280d0-0c16-3bd4-ba79-b2bf6ae76dfe | -9.89944 | -47.67988 | 2025-10-17 00:13:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4c456ce4-44ac-39ba-8f10-b0def9b85007 | -7.12939 | -46.44205 | 2025-10-17 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 06f4fea0-0dec-3fe7-8619-765dc6b2692a | -6.16573 | -44.32372 | 2025-10-17 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| beca745d-892f-3e41-b2ef-c2349975ab55 | -10.66154 | -44.85655 | 2025-10-17 00:13:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1a82b503-1de8-334c-8b61-63b87d14968c | -8.2275 | -43.4425 | 2025-10-17 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 79e6fba1-d6d5-3fbf-9e03-d64d99b36299 | -5.88747 | -43.9114 | 2025-10-17 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9d5c65cc-94cc-3098-b314-2e5fef2f8254 | -7.00211 | -47.00125 | 2025-10-17 00:13:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 01ac4a94-6731-30d2-a5f9-cb59508a0713 | -9.07917 | -48.02802 | 2025-10-17 00:13:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 11a5eab9-a54e-3661-bd13-9e63a583dc37 | -4.40651 | -43.40967 | 2025-10-17 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 622e4971-8871-353e-9861-d91d022a50f4 | -6.5211 | -46.51368 | 2025-10-17 00:13:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 3d75f976-4d83-3ee2-b146-bfa1ca9f759b | -6.06894 | -41.89766 | 2025-10-17 00:13:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| e461e103-d4d9-359c-a955-d156f48bfdb8 | -6.89269 | -43.98955 | 2025-10-17 00:13:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a31a6997-c813-3e01-ba35-501f5aae299c | -4.66535 | -44.80238 | 2025-10-17 00:13:00 | TERRA_M-M | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3163d396-9ce3-36d0-a5d6-d1fb6f9be005 | -5.84509 | -43.8772 | 2025-10-17 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| b085e542-137c-3c88-a662-588ccfede43b | -5.49265 | -42.16924 | 2025-10-17 00:13:00 | TERRA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| efcf8950-1090-3566-a768-66ec32c5a7f4 | -10.50161 | -43.43224 | 2025-10-17 00:13:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 97dab7eb-858d-30c7-922a-c817ad72a641 | -4.71758 | -46.45206 | 2025-10-17 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 26.9 |
| c1ad0fe1-63aa-384d-8931-dfbd18e74f1a | -6.35101 | -41.51884 | 2025-10-17 00:13:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 0f9eabbc-cc5b-33cf-a87b-86b968d1fb8b | -5.88491 | -43.8933 | 2025-10-17 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 4b8da8f3-df17-31c8-8d76-55eae83026df | -10.26581 | -44.04879 | 2025-10-17 00:13:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 32.9 |
| d7554024-e762-3ad5-beba-cf2d6a6ec2dd | -10.05228 | -43.83756 | 2025-10-17 00:13:00 | TERRA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0e5c1bc0-3ea9-309a-978b-b10b47e90271 | -6.2343 | -44.15388 | 2025-10-17 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 331a9c14-3b3a-3b2b-816a-939779373f96 | -6.35607 | -41.48287 | 2025-10-17 00:13:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| e78b065d-f8b8-3457-9a66-444cc7f8ea59 | -5.86921 | -43.91981 | 2025-10-17 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 5de3b23d-cfb4-307e-9fd4-4f8d454327e0 | -5.51141 | -43.7954 | 2025-10-17 00:13:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4c0fd660-1863-3549-b40a-5db74efd82d6 | -8.39119 | -46.24236 | 2025-10-17 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 8baf9f61-1f37-3ad4-ab5b-1920fd7ea6b3 | -5.91932 | -45.33699 | 2025-10-17 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 67139ec6-de38-34a8-81d8-54f5feb6c030 | -10.53902 | -44.49948 | 2025-10-17 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| af2cafdf-58b4-3d19-975b-b786984ac225 | -10.51142 | -45.04031 | 2025-10-17 00:13:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| ef1efd86-8c84-3d67-bcfa-c81fe7fd8c22 | -6.13091 | -41.75983 | 2025-10-17 00:13:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| fee9f9de-f391-3b93-8de4-8951d75dbdcf | -11.1784 | -49.80396 | 2025-10-17 00:13:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 71e20b22-9113-3be9-9d9f-316ad1ce0c91 | -5.74811 | -49.02602 | 2025-10-17 00:13:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 10168235-39cd-3e72-8ff8-634faff71441 | -6.12927 | -41.74869 | 2025-10-17 00:13:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| b959129b-5481-362a-aefd-c630868f34b9 | -6.13305 | -44.2832 | 2025-10-17 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4c7565ab-d44a-3318-8e57-c28b523b498c | -8.27968 | -43.36084 | 2025-10-17 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 53c2382a-7a67-349c-8de0-afc01846bd95 | -4.39602 | -43.40147 | 2025-10-17 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| a947712f-a137-3a03-a120-0105909c3138 | -7.1844 | -42.19514 | 2025-10-17 00:13:00 | TERRA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 5027d3fc-eaa3-33a0-a6ae-500850c549a4 | -10.28098 | -44.02843 | 2025-10-17 00:13:00 | TERRA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 107.4 |
| c29076bb-d5ed-35c2-bfd5-85245bd72da2 | -9.10257 | -46.6692 | 2025-10-17 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| eaa68d3a-13a4-35f1-9194-4ab6629f5e73 | -9.62352 | -49.14149 | 2025-10-17 00:13:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| e9e105ef-3893-3bbd-b64c-84be73c81ec2 | -9.88212 | -47.68802 | 2025-10-17 00:13:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 37.6 |
| a57f02cb-217b-3050-a6ff-ccb64b61766e | -7.17286 | -42.51518 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| e098c712-05bc-3205-ac28-2628c99c27c7 | -5.83839 | -40.81282 | 2025-10-17 00:13:00 | TERRA_M-M | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 0810f27d-15b3-3e2e-b21b-7a3bcf966629 | -4.38551 | -43.39324 | 2025-10-17 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 2ab37afb-d55c-3f88-8b67-3325f41867a1 | -6.2928 | -45.50512 | 2025-10-17 00:13:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 08b149a3-2306-3266-ad7e-b4d92153a389 | -7.2912 | -42.29765 | 2025-10-17 00:13:00 | TERRA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 254f5524-207b-37f7-bdc9-09848fdbed84 | -5.83765 | -45.54473 | 2025-10-17 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| a93c1396-4f43-3876-9add-85eded3c7962 | -10.94887 | -49.75689 | 2025-10-17 00:13:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 7dfe8106-2617-3935-aba8-97f1d8b8d0e7 | -5.22582 | -46.19448 | 2025-10-17 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 8838ede7-76ca-3dcb-ab57-a78ca81ea02a | -10.49537 | -43.38761 | 2025-10-17 00:13:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 7e26159d-80e9-3ee4-afcd-a06acd5bb855 | -10.56434 | -43.60838 | 2025-10-17 00:13:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 59a2602f-eabe-3f1b-9f4c-c39252d2262f | -8.33448 | -46.2408 | 2025-10-17 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 7375011a-d2af-3b3f-b9a4-f07d0c3afe33 | -7.95226 | -44.10881 | 2025-10-17 00:13:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 35d35505-2503-3e6a-8ccc-e35bda25bb4a | -7.18347 | -41.68103 | 2025-10-17 00:13:00 | TERRA_M-M | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 9ccbd074-ea7b-3567-855c-9cb6c242d3dd | -9.15061 | -41.05665 | 2025-10-17 00:13:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 32.8 |
| cda5c2ce-5b74-37da-98dd-f6d4d6d72f0d | -10.0611 | -43.83628 | 2025-10-17 00:13:00 | TERRA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a838d40a-37ca-3c38-a062-87fa00a81dd9 | -6.25569 | -43.9075 | 2025-10-17 00:13:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| b334606c-0bf4-3343-b8ad-1831439e4afc | -5.85401 | -43.87596 | 2025-10-17 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 0a680bde-53b4-320d-ba29-da7fee873435 | -9.96399 | -43.86576 | 2025-10-17 00:13:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6ad24d2d-9357-34c8-91b8-337af13d1f67 | -8.82253 | -47.31247 | 2025-10-17 00:13:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 3ec3eeae-64d6-3881-95f2-b70c6a693057 | -10.48074 | -43.79971 | 2025-10-17 00:13:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 35aada20-6281-3cda-a12a-42075beb921c | -8.33318 | -46.23101 | 2025-10-17 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 37.0 |
| f82060ae-cb56-3ac3-8a63-05d41cfdfeb1 | -5.2453 | -49.22551 | 2025-10-17 00:13:00 | TERRA_M-M | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 9faf5218-d7f6-3949-8a75-ce9c66cbd788 | -8.23887 | -43.32963 | 2025-10-17 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| a67c65b3-5de5-3c71-96dc-e6e6812ecb09 | -6.20945 | -41.74735 | 2025-10-17 00:13:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| a9b86032-241d-37a5-a2b0-3ac1da483725 | -11.51957 | -49.13667 | 2025-10-17 00:13:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 629120f9-0ee2-358c-af4d-1b5dfc85c656 | -6.17334 | -42.61732 | 2025-10-17 00:13:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| b0da4165-8ac1-338b-8264-cb89c34673dc | -7.54413 | -42.06482 | 2025-10-17 00:13:00 | TERRA_M-M | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 9ed77dd5-133b-3c53-b316-b8b834de629e | -9.24795 | -44.359 | 2025-10-17 00:13:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 7c000e19-7968-36c0-b257-635631e6faf3 | -9.88047 | -47.67555 | 2025-10-17 00:13:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 09062939-ce92-3426-a31a-fee5a918f2b1 | -10.51479 | -44.19181 | 2025-10-17 00:13:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 66229c49-3479-365b-a566-7f1430c784a0 | -6.25594 | -44.50308 | 2025-10-17 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3f9ef7e9-ece9-3e72-bb9b-471a3e28781b | -8.38336 | -46.32414 | 2025-10-17 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a713f955-976a-3472-8384-19de178dfcbd | -8.25801 | -43.33611 | 2025-10-17 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 22359dd1-6f72-39ac-8403-f34d0b8c7117 | -6.28963 | -42.97028 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 80a7e314-a6b4-3709-bac6-ffdb2d8bfb25 | -4.43186 | -43.39962 | 2025-10-17 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0a71542f-4a31-369c-9955-7642dfe11e1d | -8.23543 | -44.82447 | 2025-10-17 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 55.7 |
| b0d59a97-804d-3e39-b66b-43119d5418eb | -6.39894 | -41.49393 | 2025-10-17 00:13:00 | TERRA_M-M | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| d1da283c-b300-39e4-bcde-3928992f5117 | -10.62037 | -42.30944 | 2025-10-17 00:13:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 23.7 |
| a6b1c15d-4bc6-37da-8925-2e9c251d2f6e | -6.1827 | -42.61602 | 2025-10-17 00:13:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 22.7 |
| 801224f6-ef89-3459-b332-1235c53c691d | -6.29788 | -42.9731 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 826d51e6-62a9-3615-9f79-0a02e805811c | -5.87856 | -43.91267 | 2025-10-17 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 74e1db0b-d058-3d71-bc68-44582459254e | -7.05197 | -46.68948 | 2025-10-17 00:13:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 37c18f42-639d-3b6e-81bf-d487750d5620 | -6.6031 | -42.06379 | 2025-10-17 00:13:00 | TERRA_M-M | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| fee20283-78ef-3ff5-816f-17cc80a48207 | -10.11641 | -44.56578 | 2025-10-17 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d08603ac-0916-37f4-a39f-d540992f99d1 | -4.47584 | -42.92904 | 2025-10-17 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 123.6 |


[Clique aqui para ver as próximas entradas](README10.md)
