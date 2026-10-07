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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f910da7e-0f63-3b82-8b74-3882fde0e230 | -9.51462 | -54.73958 | 2026-10-07 07:20:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 26845e5a-2da2-33be-9f8d-1d99f4434265 | -6.4389 | -55.02028 | 2026-10-07 07:20:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| f734ed31-fddc-3390-980f-3ffee368a8f6 | -7.8894 | -72.3475 | 2026-10-07 08:58:00 | AQUA_M-M | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 2f7df5a8-231c-3ea6-a35c-8f9f3f0efd46 | -7.88241 | -72.36475 | 2026-10-07 08:58:00 | AQUA_M-M | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 285caf3c-36bc-3e02-8f91-ec5dfc177821 | -7.88578 | -72.33984 | 2026-10-07 08:58:00 | AQUA_M-M | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 89f16e89-0b9e-3a66-8cf2-3e0c9fc31920 | -7.87528 | -72.34566 | 2026-10-07 08:58:00 | AQUA_M-M | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 1bab13d2-4e0f-3bdd-9a6a-da650799103c | -17.5069 | -45.4666 | 2026-10-07 10:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 992eb82e-53a5-307c-ae51-ee26deacaf9e | -11.7335 | -43.649 | 2026-10-07 10:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 6140f612-7b24-3894-93e5-4e5b6b52ec52 | -11.7335 | -43.649 | 2026-10-07 10:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| f37d339a-6fc3-3e6e-8ff5-fe4975260568 | -17.5069 | -45.4666 | 2026-10-07 10:50:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 845a7b64-f37a-36d0-bbec-c0625a5f87c1 | -11.7335 | -43.649 | 2026-10-07 11:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 4149f82b-7f7f-36f7-9f2d-e20bb08c0513 | -11.3745 | -46.6948 | 2026-10-07 11:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 82c540e8-5a8e-3511-8012-c798fd5a6660 | -11.7755 | -46.6856 | 2026-10-07 11:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 1b07eb7a-de54-387d-bf7f-9adcf918d59e | -11.7335 | -43.649 | 2026-10-07 11:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 4b27f271-1de2-3134-9cff-52cebd44619c | -11.7335 | -43.649 | 2026-10-07 11:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| b6d44982-d2bf-3f49-b220-f55decb59633 | -11.0833 | -45.8514 | 2026-10-07 11:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 32a3d91b-388e-3ce4-92dd-0b0242a12039 | -11.3745 | -46.6948 | 2026-10-07 11:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| b1108159-3f9f-35fe-adfc-99bef35314f3 | -11.0642 | -45.854 | 2026-10-07 11:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 0193a2b2-7f7f-3246-af29-2ec468b1eb77 | -11.7943 | -46.7056 | 2026-10-07 11:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| f8eeaa0c-3aad-3f26-976e-52658af3893a | -3.18459 | -50.55799 | 2026-10-07 11:38:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| d51ca6d1-5834-35b2-99f6-fa84c39c44a4 | -3.74844 | -46.12341 | 2026-10-07 11:38:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2d21e046-5564-3d39-8bed-e3ab68345c0f | -4.28816 | -43.65228 | 2026-10-07 11:38:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8b05333a-0d8b-3711-802d-5409aebefb43 | -3.61629 | -43.08878 | 2026-10-07 11:38:00 | TERRA_M-M | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 15afe16a-9b95-3872-bcce-32eabc489133 | -3.88465 | -44.10924 | 2026-10-07 11:38:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 08907891-4ad1-3427-9650-f720296ae2ed | -2.60708 | -48.26088 | 2026-10-07 11:38:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 24b3a700-b88f-3b6d-89b2-b0256c384d64 | -4.34557 | -43.79736 | 2026-10-07 11:38:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| dafba1b3-40ef-3750-b680-70a8b589dc66 | -1.59715 | -47.0848 | 2026-10-07 11:38:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 75bf9b24-f3a4-37d5-9dc6-05a1786e2c6b | -1.49993 | -47.31194 | 2026-10-07 11:38:00 | TERRA_M-M | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 655cba4a-591f-32e4-88bd-35d8766d3bd5 | -3.61884 | -43.08432 | 2026-10-07 11:38:00 | TERRA_M-M | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 7424e60a-ff8f-3dae-ae3e-3fefa205ef68 | -5.01255 | -38.81039 | 2026-10-07 11:38:00 | TERRA_M-M | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 32.7 |
| 6ace9c9c-9b08-300d-ad43-7485f1e21c54 | -3.20338 | -42.60788 | 2026-10-07 11:38:00 | TERRA_M-M | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 89992a00-6fcf-35a8-8492-db677fe7ba7b | -3.18608 | -50.56428 | 2026-10-07 11:38:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 687db525-1dae-3b06-9bf4-602e2c06be5c | -4.28961 | -43.64172 | 2026-10-07 11:38:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 0d16d492-23ae-37ca-bbd7-9d881b788100 | -3.20173 | -42.61958 | 2026-10-07 11:38:00 | TERRA_M-M | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 10f80744-8fbf-3d34-8f79-9c116185ad11 | -1.9921 | -47.03363 | 2026-10-07 11:38:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a099b401-f2a4-39fd-ac5c-5b6b74d7fe78 | -3.88328 | -44.11904 | 2026-10-07 11:38:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 65f05f76-c85b-3d17-b4dd-13975d75a904 | 0.72404 | -51.37953 | 2026-10-07 11:38:00 | TERRA_M-M | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 24.9 |
| e2ca5f33-9c88-3972-a7e2-a3f3b91fb95f | -11.7943 | -46.7056 | 2026-10-07 11:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| c7755b8a-73ed-38fe-a7d3-19ed9522d5d0 | -11.3745 | -46.6948 | 2026-10-07 11:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 36ad7f8b-e830-310d-b28e-5f2f0e1e2515 | -11.7947 | -46.683 | 2026-10-07 11:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 125.8 |
| d727ee17-05a5-3d3f-a7e4-fbfec7bcf204 | -12.1742 | -44.7284 | 2026-10-07 11:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| b9df247d-ef3e-30eb-b794-29af66d49dad | -11.7751 | -46.7082 | 2026-10-07 11:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 4428b1f8-0694-32c5-9679-553e86cc389e | -11.0642 | -45.854 | 2026-10-07 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 885e23f8-77cd-3428-bf82-db5c4fb67a95 | -11.7755 | -46.6856 | 2026-10-07 11:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 51b06240-3dce-3a01-83ac-30eb44eaa2de | -4.3997 | -44.24657 | 2026-10-07 11:40:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3a2ff8a8-c58e-3a78-a397-f2da88021f94 | -6.80705 | -43.62505 | 2026-10-07 11:40:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d46ff842-9bae-3c46-9fdd-25c158602b3d | -4.45759 | -47.92171 | 2026-10-07 11:40:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 530bc9dc-3dd7-325a-ab79-e48bf0c983d9 | -6.29188 | -43.6464 | 2026-10-07 11:40:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 1d2da304-b11b-3ed3-9a73-46540d40036b | -7.24673 | -45.25359 | 2026-10-07 11:40:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| bb0807f0-fef6-33bb-945b-e96ebcac8b89 | -7.52735 | -45.88254 | 2026-10-07 11:40:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e12b42f0-fa2a-36b5-937b-feda2ad0df00 | -7.83537 | -44.18638 | 2026-10-07 11:40:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| bad957f7-65ec-3b4a-8c13-5a95bb1ab2ae | -8.04388 | -45.61893 | 2026-10-07 11:40:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7fd19cff-0343-331e-a5f5-be3e202560dd | -6.33914 | -43.82637 | 2026-10-07 11:40:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4cbb4a6d-447a-3ca4-a13b-7a0673c4c472 | -6.92314 | -43.66998 | 2026-10-07 11:40:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 063bee0e-ee56-384c-af7b-dbff8cd05f6c | -7.2454 | -45.26308 | 2026-10-07 11:40:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b650247e-d82c-3af8-b383-98e5502277b2 | -5.27806 | -43.36211 | 2026-10-07 11:40:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 748bb2ee-af05-3de9-b0c5-1fbea242fb9e | -7.35461 | -45.2744 | 2026-10-07 11:40:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 49e70aee-2fb7-3c54-af56-a71e923f0663 | -5.68293 | -47.93773 | 2026-10-07 11:40:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8489e891-d391-3ec4-8657-3dca9d283ed3 | -7.27662 | -45.56806 | 2026-10-07 11:40:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c30c3e87-7e31-327e-ae4c-c123f50649ea | -8.04519 | -45.60962 | 2026-10-07 11:40:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f5d0525c-c1d8-3162-a4a3-5a56668ed320 | -5.73932 | -43.28092 | 2026-10-07 11:40:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| e4ae0a18-f295-3916-8a95-551e30bf9481 | -4.79906 | -42.75093 | 2026-10-07 11:40:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f456a364-9498-3e34-95a1-817a1da6c635 | -6.02705 | -42.26097 | 2026-10-07 11:40:00 | TERRA_M-M | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 42.6 |
| a5f16613-460b-3fa0-8002-be7fc8e525a0 | -5.74932 | -43.28218 | 2026-10-07 11:40:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 63846f4b-14a2-35ce-a730-0063ccebd1e7 | -6.68977 | -44.94648 | 2026-10-07 11:40:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4f6aa7ef-ced6-3df7-a3cf-75602c4aea9f | -5.9723 | -40.92883 | 2026-10-07 11:40:00 | TERRA_M-M | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 31.1 |
| 44790dbe-e6e0-3654-aebe-f131c78eab2d | -7.52863 | -45.87346 | 2026-10-07 11:40:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 4447309f-0e30-3788-b056-d742294c5eb8 | -7.87264 | -44.20218 | 2026-10-07 11:40:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 52.3 |
| cbbd5d03-7bd9-3399-9387-f461eabed294 | -6.15101 | -51.74233 | 2026-10-07 11:40:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 714a6e8e-6809-3c12-950a-657f7763677b | -7.76397 | -43.80879 | 2026-10-07 11:40:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 23.4 |
| f4008fd5-fad8-3bd7-a260-f8302b7a1943 | -7.88084 | -44.21414 | 2026-10-07 11:40:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 0ace097b-3b73-3841-8aa4-8629e27d1ff7 | -6.94279 | -45.25124 | 2026-10-07 11:40:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| afc16ad3-fa59-3b6c-bcba-4eabff027f21 | -5.95388 | -43.66028 | 2026-10-07 11:40:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 372484ce-6985-381b-8555-2a5b0a5db960 | -5.01562 | -38.81618 | 2026-10-07 11:40:00 | TERRA_M-M | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 37.3 |
| 87858ce1-a0e9-3d8c-bb2c-e625c1133e4d | -5.55408 | -43.96299 | 2026-10-07 11:40:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 31fcdaf9-0f43-33e3-8447-d5ae8c364c91 | -7.20498 | -44.29672 | 2026-10-07 11:40:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fcb22790-a503-317d-93df-082b5c4108a0 | -7.21448 | -44.29829 | 2026-10-07 11:40:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 24.1 |
| cafdb3e8-d399-3488-8750-b0b14ed4e63c | -7.88323 | -44.22102 | 2026-10-07 11:40:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 36.0 |
| ca94b697-894f-33b0-aa12-4787ae229f1d | -7.8689 | -44.15767 | 2026-10-07 11:40:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 7adaaef1-8d93-387f-9977-e5c470905510 | -4.43996 | -46.18216 | 2026-10-07 11:40:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 07c90f03-2e1e-3862-9c8f-d959c4e1e349 | -5.74087 | -43.26945 | 2026-10-07 11:40:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 15ed951c-3184-32fa-960d-a691ddc93ce2 | -6.9247 | -43.65864 | 2026-10-07 11:40:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 41.6 |
| bf797656-6721-320e-a1da-dd7c0109a1d2 | -6.69109 | -44.93682 | 2026-10-07 11:40:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 18595461-2d44-3378-a5b7-690678abbc1f | -5.97338 | -43.51614 | 2026-10-07 11:40:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4b3f7b51-42e7-30da-908c-2db12868e98a | -7.53627 | -45.88375 | 2026-10-07 11:40:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a9150f44-2181-3712-b5dd-11d0c6511aa4 | -6.58375 | -41.59135 | 2026-10-07 11:40:00 | TERRA_M-M | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 105dcc8f-65f2-31b8-bcab-7246b1077821 | -4.35863 | -47.77687 | 2026-10-07 11:40:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 7f9837e3-9fa9-345e-8d3b-19f672fa8ae2 | -6.38045 | -45.05434 | 2026-10-07 11:40:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1bf3dd26-a1c1-3284-84be-c49364b917d2 | -6.32941 | -43.82516 | 2026-10-07 11:40:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| bcdbfeb5-21ba-3a80-8883-4190d3565fb8 | -6.3489 | -42.56821 | 2026-10-07 11:40:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 2fa19218-a045-381d-b480-1860ab9b028a | -7.83687 | -44.17525 | 2026-10-07 11:40:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 442c6b3e-b89a-3e0d-82de-edc585109f18 | -5.55266 | -43.97335 | 2026-10-07 11:40:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| fd3964e8-2292-3c67-a3f4-1be2624a3f43 | -6.29033 | -43.65748 | 2026-10-07 11:40:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 9acdfa23-bcd5-30eb-b2ba-5598bdcda81d | -5.75089 | -43.27068 | 2026-10-07 11:40:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 3c34a08c-2425-399f-ade6-547978adae16 | -7.35594 | -45.26497 | 2026-10-07 11:40:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| cdf1e2c1-7ee0-34d6-90d2-4280b81096ff | -6.37211 | -42.91483 | 2026-10-07 11:40:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 5d68c276-e2cd-3fff-8f2e-e6a6b657402f | -4.7057 | -43.21382 | 2026-10-07 11:40:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e4af34f9-af8e-306b-a144-c027c43cf5e0 | -6.65643 | -47.90996 | 2026-10-07 11:40:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a0023832-080a-3064-ba79-7bcaf5ad92cd | -6.20137 | -39.26919 | 2026-10-07 11:40:00 | TERRA_M-M | QUIXELÔ | CEARÁ | Brasil | 2311355 | 23 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 8834dfd4-748b-3893-94a2-140d2ee5956b | -7.43906 | -44.46304 | 2026-10-07 11:40:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |


[Clique aqui para ver as próximas entradas](README126.md)
