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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c39ca1af-031a-3f05-b91b-98c432de8167 | -11.2106 | -51.2688 | 2026-08-30 16:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 7f637eb7-0ae2-3d15-8d61-1848503ca427 | -7.9419 | -44.3001 | 2026-08-30 16:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 242.9 |
| d906dc96-5544-3c9e-8ad8-4e60dbcf40be | -3.6399 | -60.5466 | 2026-08-30 16:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 110.8 |
| ef876b56-7fe6-32af-9d12-37b7ff8a62b4 | -9.7028 | -48.1366 | 2026-08-30 16:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| f2eb5bce-1ba7-3236-ab2a-b39969307d1c | -12.2287 | -50.5148 | 2026-08-30 16:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 74539b20-9e96-34f9-ac95-73c63889ffd5 | -5.9636 | -57.6704 | 2026-08-30 16:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 8e5bdc7b-a408-32f9-9cdb-6620cd169957 | -5.982 | -57.6697 | 2026-08-30 16:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| f753e097-47c5-3a4e-8d7f-0bd1edecce86 | -6.7699 | -55.6644 | 2026-08-30 16:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 1aa54b27-299c-34fe-93be-e6087f6e79ed | -10.899 | -50.5159 | 2026-08-30 16:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| b4743a00-c513-36f3-aa35-d7fdd8cd34fc | -10.8804 | -50.4965 | 2026-08-30 16:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| f6bf7f38-b956-308e-8761-462b9cc1ff7b | -3.4979 | -59.0409 | 2026-08-30 16:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 5c59e772-6de3-3e11-89c2-19b4ad70eeac | -9.1525 | -59.619 | 2026-08-30 16:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 1b579f67-b9e9-321c-b47b-6e818689fabc | -9.6839 | -48.1386 | 2026-08-30 16:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| d065aa49-0500-3377-97c3-d13ecb5baace | -11.1634 | -50.5727 | 2026-08-30 16:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 6d4f2d81-00c1-3d2d-bbd8-3ec1b7d9db25 | -10.8801 | -50.5179 | 2026-08-30 16:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 5a059279-1bc5-3b8c-926d-ce0b59f355e9 | -7.9611 | -44.275 | 2026-08-30 16:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 183.6 |
| f5d87f21-eeb9-3690-b9dc-754b3a05d811 | -12.3618 | -50.5417 | 2026-08-30 16:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 149.7 |
| e9370a46-0960-3b91-8de2-8658b408f36b | -10.8993 | -50.4945 | 2026-08-30 16:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| c3b1982a-cd74-3103-8d2c-91e6b53d7ecd | -9.1523 | -59.6384 | 2026-08-30 16:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| f713e74d-6009-3cb7-b066-d6c412bbc4ef | -10.7428 | -50.8727 | 2026-08-30 16:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 913e70fc-284c-3446-8ea7-a997fb157e85 | -8.5975 | -54.715 | 2026-08-30 16:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 1de30486-594f-3472-a88a-69ab8ccce8da | -3.4185 | -61.3273 | 2026-08-30 16:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| fbb9c519-d1e5-35e3-ba6e-f7a1762bcb29 | -3.1266 | -61.2 | 2026-08-30 17:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| f0ec8b35-b0b3-3951-a87c-c9cf3d3095f7 | -11.1723 | -51.294 | 2026-08-30 17:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 5d21779a-d792-3047-913c-a10936a7d750 | -7.9419 | -44.3001 | 2026-08-30 17:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 152.7 |
| 2d67c9d4-ad17-31f9-85d1-bcaa7ade851e | -3.4002 | -61.3276 | 2026-08-30 17:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 2e83ffad-8965-303c-9902-0924286be150 | -12.3229 | -50.5892 | 2026-08-30 17:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| c05de239-de0b-30ce-9c8b-3fae3a68b0d0 | -10.3296 | -45.3799 | 2026-08-30 17:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 6953adee-2dd9-3c30-87a8-2ae44c9013e0 | -8.5925 | -66.9564 | 2026-08-30 17:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 120.5 |
| 21a8bc4d-7f16-3b5f-88d9-f4033e5c6fa1 | -6.0743 | -57.6465 | 2026-08-30 17:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 4ca9e2e3-1a6b-36f4-840e-0839f5ca8bca | -7.546 | -44.3395 | 2026-08-30 17:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 392cb4e9-c727-3724-baed-635acdc49574 | -5.982 | -57.6697 | 2026-08-30 17:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 81010314-350c-3d79-bf3f-8330f271b456 | -9.8617 | -65.0334 | 2026-08-30 17:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 24b24562-2cc0-3257-be80-d17244e07653 | -7.9611 | -44.275 | 2026-08-30 17:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 138.7 |
| ee20f3e9-0cd2-3c10-a1d8-286fb55e94e2 | -12.3618 | -50.5417 | 2026-08-30 17:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 1288ea05-a289-3004-92a8-229f62e62d22 | -19.0744 | -57.3876 | 2026-08-30 17:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.8 |
| d85e7915-7425-336a-b790-5d63789df1a0 | -5.9636 | -57.6704 | 2026-08-30 17:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| f2137150-9a80-38d9-8600-f72386cc16b6 | -8.6673 | -62.8369 | 2026-08-30 17:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 5bc1cca5-5de2-3a27-b74f-b8125bfad72a | -3.4185 | -61.3273 | 2026-08-30 17:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 2261f4ee-b29c-341f-9b88-00a37284133b | -12.3232 | -50.5678 | 2026-08-30 17:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 4a2af427-b156-3bf2-ba09-e92670c75b0c | -6.7114 | -59.0958 | 2026-08-30 17:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| d568b820-7329-35b1-b431-cae892330cd8 | -11.1542 | -51.2324 | 2026-08-30 17:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| db34c061-acf4-3271-bf3c-da175ce458f9 | -3.6216 | -60.547 | 2026-08-30 17:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 231.4 |
| 726d587b-550b-3ed0-8ca1-d4a5716d8884 | -11.0057 | -49.6677 | 2026-08-30 17:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 7c1b3333-22a2-3ee5-a9ed-ea3328470fc9 | -10.8249 | -45.3382 | 2026-08-30 17:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 988.6 |
| cb8c2eb5-473a-3e95-8c8c-b3909c071137 | -9.1523 | -59.6384 | 2026-08-30 17:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| f4a8cf0f-daaa-3924-8934-8e453160a497 | -11.3622 | -45.1494 | 2026-08-30 17:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| c1cb8cac-2a35-3375-9848-7d26724dac1f | -10.7434 | -50.8302 | 2026-08-30 17:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| d72084cc-7b5f-371f-b19e-8d291f4f0306 | -10.9405 | -50.255 | 2026-08-30 17:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| ddb05069-24a3-3700-b883-e3d53f982444 | -9.1525 | -59.619 | 2026-08-30 17:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 5b0e58c3-ee66-3f5e-b50c-63df8e5bd9a9 | -8.739 | -45.3844 | 2026-08-30 17:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 120.4 |
| b063b7e1-92a2-3148-bc67-8cbeab15240f | -12.3809 | -50.5393 | 2026-08-30 17:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 2939929a-e8e2-3146-93d4-1bbeb20845fa | -12.3427 | -50.544 | 2026-08-30 17:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| c1aa8b50-bf1d-3566-8fa8-cf0f1c77b9ea | -8.574 | -66.9569 | 2026-08-30 17:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 4b4372e8-061e-326b-a605-b44ad5ef8e42 | -7.1121 | -42.7963 | 2026-08-30 17:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 142.9 |
| caf898ed-9863-308b-8e12-331c4df0b515 | -3.1267 | -61.1811 | 2026-08-30 17:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| f9d4e1e2-8094-3762-b4e9-e362fe8c785c | -11.1634 | -50.5727 | 2026-08-30 17:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 1d59e89a-a09a-3f73-b0fb-e24be01610ab | -6.7884 | -55.6635 | 2026-08-30 17:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| b4b7c36c-62c6-3bf3-bee5-a91402a0f5fd | -12.3424 | -50.5655 | 2026-08-30 17:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 5d301731-ab5c-3b36-a629-74af09ec2bb0 | -8.948 | -62.3894 | 2026-08-30 17:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 75.7 |
| cc133222-20bc-38a6-a0ad-6e392db9fce4 | -7.9425 | -44.2538 | 2026-08-30 17:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 171739f3-0a1b-348c-a4d3-77545770ee63 | -7.9422 | -44.277 | 2026-08-30 17:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 173.4 |
| aa27dec1-d08b-3386-a8c8-aab9474d4cfd | -6.0 | -45.0889 | 2026-08-30 17:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 156.7 |
| 92ea51d4-1ea8-305a-a10a-fed0c694f3a7 | -8.7969 | -62.8506 | 2026-08-30 17:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 57.1 |
| ab829f8a-359a-3b2b-9ce6-0eface6b4536 | -11.3622 | -45.1494 | 2026-08-30 17:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 148.1 |
| 89f28b4d-6560-3ba0-bcc2-03a178cac8a6 | -7.9419 | -44.3001 | 2026-08-30 17:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 252.6 |
| eb63e3ae-1fa6-3713-816b-1687ff596b0c | -11.172 | -51.3151 | 2026-08-30 17:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 124b5665-6634-3ceb-ad6a-585e613a94d6 | -5.982 | -57.6697 | 2026-08-30 17:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 4dc305e4-5bc9-3ecb-8336-e41554049dde | -12.1902 | -50.5409 | 2026-08-30 17:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| a38a61c9-216f-3a02-a15c-1cdf2dc7fc10 | -12.3424 | -50.5655 | 2026-08-30 17:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 65b99972-7faf-3eb8-a7ee-330d3b168320 | -7.9422 | -44.277 | 2026-08-30 17:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 204.8 |
| a8f3adb2-e909-318f-8038-da5e4534fb42 | -8.574 | -66.9569 | 2026-08-30 17:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 5ff2d1a2-aae5-3d84-a84b-c0c2223d62af | -10.5782 | -50.4643 | 2026-08-30 17:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 57c8918c-45fa-30e6-9d6d-3556b760ed7f | -11.1723 | -51.294 | 2026-08-30 17:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 4d132793-9871-338e-a87e-63361a2ae45e | -6.0743 | -57.6465 | 2026-08-30 17:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 61271b57-3db6-33b1-b40b-0e2bccfd7640 | -6.8019 | -59.4008 | 2026-08-30 17:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| f55676b8-c486-340b-898d-e1bc11d24b78 | -7.2746 | -60.6294 | 2026-08-30 17:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 20cce48c-fc74-3838-bdf8-155592fcf6a3 | -7.9611 | -44.275 | 2026-08-30 17:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 150.4 |
| 8ba4eae5-617d-3fea-9197-ba84bebfacf2 | -11.2443 | -45.3497 | 2026-08-30 17:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 66b7fbfe-9058-3d16-8c68-50eadbf2217f | -6.0 | -45.0889 | 2026-08-30 17:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 12f743f1-61ab-31bb-b1c3-8c4ca41a3cdb | -8.3717 | -62.716 | 2026-08-30 17:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 0b2d9fb7-f7f0-3b9e-aa00-522f36c44613 | -7.1121 | -42.7963 | 2026-08-30 17:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 221.0 |
| 7b6712b3-8921-3df9-8d4e-c65a83700918 | -5.9636 | -57.6704 | 2026-08-30 17:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 1316455f-b88a-3553-9e35-94cf7e9d1f15 | -11.0057 | -49.6677 | 2026-08-30 17:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 3dd3af95-7f9d-3c4b-a27a-e4170636b0fd | -3.1266 | -61.2 | 2026-08-30 17:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| e6352246-1bb9-3348-ac84-fe5f6cc4293a | -11.245 | -45.3037 | 2026-08-30 17:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.2 |
| ea118c4d-5712-3556-887f-721bb318987e | -3.6033 | -60.5474 | 2026-08-30 17:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 37ac8888-637a-386a-b60d-3871edf29536 | -11.0054 | -49.6893 | 2026-08-30 17:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 640bddcb-5058-38c7-a705-4e9087762f94 | -11.1939 | -53.9993 | 2026-08-30 17:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 4ca9d101-0cc6-3922-8196-d27b556e6e3a | -3.1267 | -61.1811 | 2026-08-30 17:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| f108dd8b-07e6-37ff-976a-312daa66bcf2 | -12.3618 | -50.5417 | 2026-08-30 17:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| a6ce0e9a-483f-37a4-8d1e-04f29ae13163 | -3.6399 | -60.5466 | 2026-08-30 17:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 116.5 |
| fab6300f-b0e7-3323-b066-7d031fe541c2 | -12.3427 | -50.544 | 2026-08-30 17:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.5 |
| bfdfbea0-50b9-393a-8a0d-d83de75ee6dc | -11.04 | -51.5 | 2026-08-30 17:15:00 | MSG-03 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c9c2b99d-18a3-3ed0-b250-e93e789995bb | -14.61 | -53.55 | 2026-08-30 17:15:00 | MSG-03 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dae18171-5657-3005-93fe-72017fb02161 | -11.03 | -51.44 | 2026-08-30 17:15:00 | MSG-03 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a4fff3b9-8865-3b86-9a96-e17ecdf99d35 | -12.11 | -47.23 | 2026-08-30 17:15:00 | MSG-03 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 27de2abc-444a-3b65-860a-c07edd1af367 | -14.64 | -53.62 | 2026-08-30 17:15:00 | MSG-03 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b49cf574-05d7-3485-b4aa-94667e93edcc | -10.74 | -54.03 | 2026-08-30 17:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| edc559f7-733b-399f-8586-414140bc0b25 | -15.36 | -53.78 | 2026-08-30 17:15:00 | MSG-03 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README100.md)
