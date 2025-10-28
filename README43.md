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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d80e26f7-9d70-3ebe-a37d-27a8c312208d | -10.5683 | -49.8018 | 2025-10-28 04:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 3ae31f5b-a0c1-34b7-81db-44140f1841d9 | -11.2798 | -45.5052 | 2025-10-28 04:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 8dd22fdc-6b4d-3d3b-bac2-5421d0242a45 | -3.0158 | -45.3679 | 2025-10-28 04:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 2e64bf18-d408-39d7-9057-dade93e192b5 | -8.6463 | -45.2578 | 2025-10-28 04:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 57.5 |
| c3765215-5682-3c44-abfc-7586da12cb3c | -10.5872 | -49.7998 | 2025-10-28 04:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 011e385b-77bc-304d-8170-10176b99f0df | -7.9693 | -46.7423 | 2025-10-28 04:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 564ee703-91f2-3ab5-8566-ffd0972be18e | -3.0344 | -45.3672 | 2025-10-28 04:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 0b61b8ad-eabd-32f9-b557-608b10dbcdb7 | -8.646 | -45.2806 | 2025-10-28 04:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 155.0 |
| 73f9838a-979c-362f-b0c1-4bf3585331ed | -4.4632 | -43.2386 | 2025-10-28 04:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 47.2 |
| a20dde95-071f-3053-8966-361159ca7998 | -11.2798 | -45.5052 | 2025-10-28 04:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| f3db7622-5298-37f9-ac8f-573413e532c1 | 1.20307 | -51.07504 | 2025-10-28 04:40:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5601fea8-5404-3ac2-aa68-fd448a5d6c67 | -1.00253 | -47.6539 | 2025-10-28 04:40:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa56a9fc-ee1c-31dc-ad84-5dd859a0f6f3 | 3.35775 | -51.34665 | 2025-10-28 04:40:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb48e60e-2908-3618-a700-7f7667f9891a | 0.96796 | -51.12049 | 2025-10-28 04:40:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b9a04daf-bf61-34f3-b315-3eb981252e85 | 0.23517 | -51.15367 | 2025-10-28 04:40:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55489cd0-c82e-39b2-964b-c5b6094ac6ad | 1.60935 | -55.72076 | 2025-10-28 04:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a32fff5b-1a59-37df-be5e-ecf837950aff | -1.84124 | -45.29531 | 2025-10-28 04:40:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb5eb238-d0b1-37cb-9b26-63a69ed32b1e | -1.00586 | -47.65442 | 2025-10-28 04:40:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8796f7ea-dd0d-373c-9047-522bc01fced3 | -1.48791 | -49.08213 | 2025-10-28 04:40:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2265cb06-9a6a-34dc-9337-33bac08b4520 | 1.62971 | -55.68832 | 2025-10-28 04:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ba32c27-ce14-3668-be64-ac7622c00dcf | 1.62149 | -55.70125 | 2025-10-28 04:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75c601d7-8d3b-3831-b749-f518630c1476 | 1.60827 | -55.71485 | 2025-10-28 04:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 366b58b0-72bc-3f88-b98a-69ef6845387b | 0.99594 | -51.10907 | 2025-10-28 04:40:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24013a01-9b54-37d1-bbfa-2740c3bf6745 | 1.88951 | -50.8397 | 2025-10-28 04:40:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf06b773-a182-354a-b92c-9a6a53026051 | 1.6091 | -55.72036 | 2025-10-28 04:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 038ca0b4-0d13-302b-ba55-d37eb12f3950 | 1.61737 | -55.70766 | 2025-10-28 04:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a4d2e03-6366-36b1-a57e-172cadc3a200 | 1.59534 | -55.72894 | 2025-10-28 04:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bdf758c9-99a3-35be-9850-b80bb1b23fed | -1.83761 | -45.29474 | 2025-10-28 04:40:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 182e1779-eba9-35c0-a625-2c019b696b51 | 0.23549 | -51.15628 | 2025-10-28 04:40:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38977c06-8232-3da2-ab13-34c5fc56db1e | 0.97095 | -51.11575 | 2025-10-28 04:40:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d483d05e-fdc0-3bd1-b860-17d24d915f19 | -1.59617 | -48.03023 | 2025-10-28 04:40:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c9308f21-110b-3ae9-b521-94e44d508844 | 0.98392 | -51.12673 | 2025-10-28 04:40:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 47ea486e-31b4-3ebb-aeb0-1799a61fc05e | 1.63468 | -55.68758 | 2025-10-28 04:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59d3859f-b690-37a4-a0c4-8dfb242cb21d | 1.04239 | -51.31208 | 2025-10-28 04:40:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f8228bf2-2d56-355c-93a2-3f3ba65f10d3 | 1.6003 | -55.72805 | 2025-10-28 04:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3bb9efc-9377-35eb-9075-9f40cbc0d862 | 1.60848 | -55.71525 | 2025-10-28 04:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3308fad7-4b9a-35af-99d9-13a7766390cf | -0.90683 | -47.55379 | 2025-10-28 04:40:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c35c5fce-e034-389d-9086-dd82bfcfd91f | -1.35448 | -48.27546 | 2025-10-28 04:40:00 | NPP-375D | BENEVIDES | PARÁ | Brasil | 1501501 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a80ea1d8-c16d-3735-a727-bdd6dcb9dbf8 | 1.89249 | -50.83495 | 2025-10-28 04:40:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cac10573-d9d5-3139-b48e-bfeb3580afc5 | 0.97988 | -51.10141 | 2025-10-28 04:40:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17d30db5-350c-37a4-9281-b1c342ae3e0c | 1.59213 | -55.74098 | 2025-10-28 04:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1c91929-bb6e-32ea-8369-ed356a5ddcec | 1.82693 | -50.51215 | 2025-10-28 04:40:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 24a7ff48-44db-327a-a1d1-d41f645182f8 | -0.90738 | -47.55032 | 2025-10-28 04:40:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 200c1d95-c382-3d16-925e-ce5633256dfe | 0.97624 | -51.10198 | 2025-10-28 04:40:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3645c493-0902-3383-bc01-b60f5cf3b244 | 0.99528 | -51.10485 | 2025-10-28 04:40:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b055d2e-b4d4-3320-9c46-141725012661 | 1.14307 | -51.04897 | 2025-10-28 04:40:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 886e60cb-8aaf-39d1-b9ff-1a6dfb53fa42 | 1.05265 | -50.97126 | 2025-10-28 04:40:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e9f734a7-aac7-3643-bebb-a1ce26687d92 | -1.14226 | -48.09758 | 2025-10-28 04:40:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 61fca957-f55f-3680-a82b-323a73e35a41 | 1.59125 | -55.73536 | 2025-10-28 04:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b19a83d0-d143-3e56-9dee-156e777261a3 | -7.95634 | -45.46238 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78f5d292-39c1-3c9f-ae81-9b7a270c8d0a | -4.49493 | -43.67889 | 2025-10-28 04:42:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9322c2de-2750-3bbe-8cf0-0ef78500dd82 | -7.6204 | -46.69144 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e0c6671-a231-3909-9554-19ba8b4a765a | -6.14051 | -41.83868 | 2025-10-28 04:42:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6fde6d62-16b2-35f1-8b62-aaaeff0224fc | -2.75627 | -47.7555 | 2025-10-28 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8598868-65af-3c32-ae8d-0157c12edd9b | -5.19998 | -46.14911 | 2025-10-28 04:42:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 365d07c5-f603-3c1f-8a24-4e869e7a9f5b | -6.58988 | -42.68646 | 2025-10-28 04:42:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bc9c659d-63d2-372b-a4c7-1fb3409d3576 | -7.95 | -45.50531 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8d3332d2-bdfd-3ec1-b555-8245d287286b | -5.63074 | -47.61317 | 2025-10-28 04:42:00 | NPP-375D | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5a235d07-348b-3734-9b85-38f59ad0d3d7 | -5.62986 | -43.63764 | 2025-10-28 04:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54f2bf03-f787-3466-b329-04170c5b3790 | -4.7052 | -50.46987 | 2025-10-28 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f61e7697-cca4-316d-a2cb-248be4d7274f | -1.55966 | -55.41683 | 2025-10-28 04:42:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 490233bc-c0a1-321d-8713-08d0f3eb066e | -5.65521 | -47.63577 | 2025-10-28 04:42:00 | NPP-375D | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d6e1e7db-8052-364d-b0c3-f0f97791d819 | -5.36465 | -46.96827 | 2025-10-28 04:42:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28c8b76b-629e-3fdb-a7f6-dc1c2c30e643 | -3.11428 | -51.21522 | 2025-10-28 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18556f4c-fad3-314c-8c31-7ca8d00f9ee0 | -4.90391 | -47.41685 | 2025-10-28 04:42:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c84089d-6ccb-31b5-8da2-0bd63bd7a402 | -3.02545 | -45.3744 | 2025-10-28 04:42:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 1fc6d9fa-1c4f-3d5a-9cad-b3d0bb965492 | -3.08606 | -44.45124 | 2025-10-28 04:42:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 647ab6de-7db5-3470-aa17-7cb32df68b4e | -5.65856 | -41.12015 | 2025-10-28 04:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0cf62dcd-f3fd-30d9-bd00-ed3ae8f27f82 | -7.35558 | -47.64236 | 2025-10-28 04:42:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 213caac9-012b-36a6-a4d2-95948084b6ed | -3.57771 | -43.60079 | 2025-10-28 04:42:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9458da6e-9373-3d41-ab60-75e93bbb481d | -1.49294 | -53.13131 | 2025-10-28 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39a88077-ed20-3833-b873-4ff35ddc5702 | -6.03498 | -46.56602 | 2025-10-28 04:42:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8079f65b-1c54-38ee-a8e2-07d7e35c7c0b | -5.61401 | -47.1066 | 2025-10-28 04:42:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e28af11-02bb-346b-a599-c0b8f18d2963 | -7.82779 | -46.40192 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e857b848-aa84-3caa-ad73-561dc9bbfaca | -7.95458 | -45.50112 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 030bd0df-66f2-3291-afaa-3ca67d707b90 | -7.83318 | -46.41597 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 89200d63-6ddb-3114-b063-b1e567619ca3 | -4.85317 | -50.68135 | 2025-10-28 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 20d6c6e9-e73b-3552-bad7-715dfc9ed43e | -7.07016 | -44.95227 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7b014539-8792-3f8d-bff1-30844230fe20 | -3.69096 | -43.22137 | 2025-10-28 04:42:00 | NPP-375D | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 147bfe7f-5005-379c-98a7-aa72c90ef834 | -6.08559 | -42.14865 | 2025-10-28 04:42:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8af48c07-7f25-3c38-8005-848e170cbbb0 | -5.64952 | -47.62735 | 2025-10-28 04:42:00 | NPP-375D | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e4fa8de-21b5-33f6-951a-edf1a580d763 | -3.86885 | -55.68937 | 2025-10-28 04:42:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c99c8475-4bad-3de5-9ebd-1487142b2419 | -1.50428 | -53.12473 | 2025-10-28 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c60a1d17-f81e-332c-8562-eb3bdf8f9f88 | -4.24874 | -48.37424 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9727a984-832b-3a8c-9830-098d6ef0a984 | -4.20024 | -50.09106 | 2025-10-28 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 65238761-491b-3ffe-b94c-80d03fec4a4f | -4.35664 | -50.51108 | 2025-10-28 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| de2b1bbf-652d-3206-8e6d-08bfb701ff71 | -3.07569 | -49.47808 | 2025-10-28 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c3a3d69-eebe-3596-a6a7-df99224ea8b4 | -7.39217 | -45.12413 | 2025-10-28 04:42:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f5e44d28-fa6f-379f-863f-989899f35796 | -7.78773 | -46.44397 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0516086-98d2-3b00-bfe9-4419a1d9a32c | -5.30347 | -48.70284 | 2025-10-28 04:42:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2fb6f273-11af-351c-9f88-5040be30e61e | -6.58882 | -42.69364 | 2025-10-28 04:42:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c2b9bd72-c14f-39a3-b382-046566b8a057 | -6.84676 | -50.11417 | 2025-10-28 04:42:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a8f5c66-4d49-39ef-9781-5eba98bfc204 | -5.82312 | -53.45388 | 2025-10-28 04:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1d88433-92a7-364c-b77e-4b70fca58f30 | -5.85129 | -46.44941 | 2025-10-28 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eaefda24-b311-3581-ab1f-5e7fe2c90fb9 | -6.63374 | -47.19722 | 2025-10-28 04:42:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46cd03e3-ee51-3dea-abc0-a71b572a142d | -5.64895 | -47.63105 | 2025-10-28 04:42:00 | NPP-375D | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a2fa1a5c-21e4-3d6d-8b48-6a921073a1e7 | -4.76015 | -46.42582 | 2025-10-28 04:42:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56575c06-0c0b-36e1-9bb8-52a30a3a516f | -2.97848 | -51.34352 | 2025-10-28 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa044300-f63b-313f-aad0-2251b3c9d20a | -5.48936 | -42.1677 | 2025-10-28 04:42:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 9dbb3fec-2f8a-3b53-87db-582dd8252bcb | -7.0756 | -44.94295 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |


[Clique aqui para ver as próximas entradas](README44.md)
