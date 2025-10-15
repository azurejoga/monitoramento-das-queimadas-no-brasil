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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7bd9b99-fad8-39db-80cb-9fe3781581ad | -7.29258 | -41.95568 | 2025-10-15 03:47:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8390d73e-2094-3913-88ee-74981f8419c0 | -5.91155 | -42.8251 | 2025-10-15 03:47:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 24bbb8a8-2039-3e5e-97fc-7c0fac9b22c5 | -6.23489 | -44.16507 | 2025-10-15 03:47:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a41c849b-18b4-3e94-9518-1f0593d97ac8 | -5.84191 | -43.95623 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be74ef10-3569-3c3e-b741-b6f017cf171d | -6.23434 | -44.16813 | 2025-10-15 03:47:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0c76713c-e28c-38de-9774-179502a4c441 | -6.05119 | -43.3905 | 2025-10-15 03:47:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c12e83c8-439f-3ff1-b7f7-07924e675f65 | -4.52435 | -48.04981 | 2025-10-15 03:47:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c03caebf-67af-3acb-887f-423b15d00d05 | -6.38383 | -41.4855 | 2025-10-15 03:47:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f1032aa1-4087-30ff-8db8-f77bfdb8ca72 | -6.14056 | -41.74903 | 2025-10-15 03:47:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c047ab44-fe18-318a-b998-436625f8c997 | -5.86224 | -43.8702 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ebb666d-154b-37d7-9383-3c884e408810 | -8.26518 | -43.36494 | 2025-10-15 03:47:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 659c5982-52a3-37a2-a524-6bf130b379a2 | -6.17752 | -42.61252 | 2025-10-15 03:47:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 172e1dc2-7f40-3de8-aa6c-266528a13926 | -8.21499 | -43.32178 | 2025-10-15 03:47:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 74dff11e-ada1-33bc-aaab-a6dfdff9ab22 | -7.00685 | -38.3603 | 2025-10-15 03:47:00 | NPP-375D | CARRAPATEIRA | PARAÍBA | Brasil | 2504108 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2d08b732-895e-315f-9e31-e96aa851821b | -5.58842 | -44.74944 | 2025-10-15 03:47:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82b76279-79ac-3e70-8966-95a4e359aaef | -7.57334 | -42.69392 | 2025-10-15 03:47:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cc8192e5-3abd-3da3-a035-f36d9d242052 | -4.64549 | -43.13462 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df06cc5f-060b-3cb7-b407-602d196833c2 | -4.66164 | -43.13136 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9dce4b7a-a77a-3292-93ee-19474c119340 | -8.20428 | -44.07757 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a873a09c-1500-313e-adb3-17ae3251510e | -5.42548 | -44.22311 | 2025-10-15 03:47:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 53f982b7-cca7-3234-a6be-39a8a4d6e19a | -6.17463 | -44.29851 | 2025-10-15 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f54855f-76b9-373d-b3d5-af8bffeeec19 | -8.24647 | -39.45747 | 2025-10-15 03:47:00 | NPP-375D | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 24135d50-d672-3e52-8d12-ec13dcb3c3d0 | -6.17624 | -42.61892 | 2025-10-15 03:47:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 4e45870d-0df6-3a09-a5f3-7a4c54ed9c29 | -5.00538 | -44.49481 | 2025-10-15 03:47:00 | NPP-375D | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44864f20-63e5-30d1-aa19-8af8b9ffbfad | -6.58108 | -42.96582 | 2025-10-15 03:47:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0147cbf3-0caf-331d-9f58-96d8e733ffde | -5.67566 | -44.25356 | 2025-10-15 03:47:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85e8004a-0126-36ab-a83b-d80db7acd192 | -5.43279 | -41.34466 | 2025-10-15 03:47:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c98865d2-1561-3df1-975a-be31fe10e264 | -5.14977 | -45.6976 | 2025-10-15 03:47:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cea1d891-8d5d-3669-9234-a795a5d2a2db | -5.58578 | -42.84182 | 2025-10-15 03:47:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d6101f7f-c951-300e-b660-04e6be4eec13 | -6.58199 | -42.96061 | 2025-10-15 03:47:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 36887728-6a78-3077-8ffb-59a8d1afbc3e | -7.55286 | -42.71257 | 2025-10-15 03:47:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 981a0631-3ad7-3e86-95e4-8d1984affd1f | -5.42139 | -40.98192 | 2025-10-15 03:47:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fec69382-bb2e-311a-bcf0-d30dcb1f7382 | -7.48442 | -42.14717 | 2025-10-15 03:47:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2072e35d-48bd-38ea-a388-2602c0d9e6d2 | -4.25641 | -45.5878 | 2025-10-15 03:47:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d82cccab-a16a-3819-9760-a5d68484482b | -6.39949 | -42.52159 | 2025-10-15 03:47:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 3b30f8a5-c925-3c74-96fe-b0e9c30038e1 | -7.54064 | -42.6882 | 2025-10-15 03:47:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e79a2c75-4c7d-393e-b8df-30baf0440262 | -5.44026 | -46.28916 | 2025-10-15 03:47:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5f6e424b-a5f1-3a39-a2d5-d7cc04f9ce2f | -5.42911 | -41.33946 | 2025-10-15 03:47:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 40c50634-a4a4-3dbe-9ee1-06bcfa5c3ea2 | -5.56648 | -41.32001 | 2025-10-15 03:47:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b7d92f22-b3d8-36d1-a001-f9f8b815fe95 | -10.0608 | -42.61552 | 2025-10-15 03:47:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 24fda956-fc8d-3b19-9685-269e81c52e5c | -8.2169 | -44.03693 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16d3d9a4-fc00-3dea-8e3e-e6522d7a9736 | -7.94387 | -44.13773 | 2025-10-15 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5cf4a0f9-c7d4-36af-a89c-8cacb6a69d49 | -7.03266 | -42.73866 | 2025-10-15 03:47:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 760ac0a5-2030-34f9-82bb-df8319b073d6 | -5.41895 | -44.22885 | 2025-10-15 03:47:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a3551519-9b8c-3c0c-aede-bccca2d9fa0d | -5.62744 | -42.68314 | 2025-10-15 03:47:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 72a46e33-67ef-3358-a91f-0087c062a38b | -6.57625 | -42.96489 | 2025-10-15 03:47:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0201da86-72ac-3069-b3ba-91bf1bafbd52 | -7.95303 | -44.14568 | 2025-10-15 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 346a348d-e952-3334-8a09-b8309c6cc758 | -5.33302 | -42.56549 | 2025-10-15 03:47:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4f3e530d-e877-3784-9440-3dd33d8d5157 | -5.42997 | -40.98355 | 2025-10-15 03:47:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 374c8332-f6e7-3fe3-96f3-dd7d5293f03a | -6.39867 | -42.52623 | 2025-10-15 03:47:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| a352cc55-a8a7-3c4b-aba7-a438e43a63d0 | -7.67453 | -42.37484 | 2025-10-15 03:47:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9a8dbf61-d255-311e-b2bd-bab9751b2279 | -5.03755 | -44.7368 | 2025-10-15 03:47:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 126339d1-9d70-3dff-ac8c-f937a665eabe | -7.16367 | -42.18172 | 2025-10-15 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8bcc3c6c-8986-3316-afd4-99d4dfc2b4a0 | -5.89462 | -43.74971 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e27c3c8c-fea3-3599-8580-8f800cab8230 | -5.73829 | -44.988 | 2025-10-15 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 11f616f8-a18f-3517-b417-e1ac57d3c9f3 | -5.9463 | -43.75838 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 77577141-b290-307c-a5fb-041cbf772d64 | -6.34145 | -42.65624 | 2025-10-15 03:47:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| c7eda59a-4edb-37bd-a6d7-6699b7b78c52 | -5.85756 | -43.86619 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 18965dad-bdad-37c1-bbf7-ed4b8dc20130 | -6.5461 | -44.72437 | 2025-10-15 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a3d7d67-da61-3e01-81a3-e4f874c439ce | -6.04984 | -43.3907 | 2025-10-15 03:47:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2f53d94a-b3f0-3494-a858-28e5f09cb090 | -5.85808 | -43.86312 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ba140f4b-f08c-3a4d-8ef6-e42f62364950 | -7.09029 | -41.95675 | 2025-10-15 03:47:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cb85f5ba-ec1c-3212-a6de-39dc3dab9c97 | -6.45668 | -41.84874 | 2025-10-15 03:47:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4f711b70-7f96-3fb1-976b-b434619c9b94 | -8.21583 | -44.04282 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a5b62256-eab8-3c9c-9069-07d46a7bbf9e | -8.22352 | -44.08706 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc0bf65a-0396-3fe7-b1be-872293649991 | -4.90617 | -43.46711 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 5999d317-2c0a-3f43-8990-613fb6566ccc | -7.57038 | -42.69553 | 2025-10-15 03:47:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0247b2f0-3029-3ee0-b817-1adc5f62fd8e | -4.65203 | -43.12672 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 16ad8e5c-f4e4-32ff-838e-758413cc267e | -5.43676 | -44.22187 | 2025-10-15 03:47:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 103409b1-375c-33a2-bb17-4e966bb536d0 | -4.77075 | -45.73774 | 2025-10-15 03:47:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 976c7575-c5d4-3d60-b4d7-1ba406a267a1 | -8.46277 | -44.18686 | 2025-10-15 03:47:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c169864c-dbbd-3e07-a1cc-7532d908ef4f | -5.56562 | -42.99789 | 2025-10-15 03:47:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| eea320be-0021-3d23-a0e1-c5b0178b7b4b | -4.52312 | -48.05671 | 2025-10-15 03:47:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff97a1be-27f7-3f13-8c92-43284191d2a4 | -7.36367 | -43.64721 | 2025-10-15 03:47:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e3dc8239-8cc4-3486-93a1-00b19b11bc63 | -8.22298 | -44.09003 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38eb7a58-c186-3f7b-bb84-de8dd1dec869 | -5.42431 | -44.22985 | 2025-10-15 03:47:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 845c1eb3-3a84-30a9-9517-ff350f5816e4 | -7.81482 | -42.10763 | 2025-10-15 03:47:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 963aa68b-7a5d-384e-8095-69995fdc146f | -5.82948 | -42.32925 | 2025-10-15 03:47:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b8a4a176-b2fa-3d8f-9700-8951e2c5fbd5 | -10.05635 | -42.61472 | 2025-10-15 03:47:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 326b616d-0d6b-3028-a3c3-b252aa60cc11 | -6.45901 | -41.83522 | 2025-10-15 03:47:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5d9346ab-4d88-3945-a0bf-feb1ced9bef9 | -5.02633 | -44.73504 | 2025-10-15 03:47:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c6293da-00f2-3949-b88f-c53204256f89 | -8.19623 | -43.9866 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c7ed6c8-cbb2-3635-9074-2ac8979c4e99 | -7.16147 | -42.49716 | 2025-10-15 03:47:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cbc7183c-3468-3a75-8146-9f244180596e | -6.226 | -44.15984 | 2025-10-15 03:47:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3a184a26-0e0d-3591-b1ec-ccb236309b7b | -4.19856 | -44.70465 | 2025-10-15 03:47:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc088f75-0e78-3c35-984f-765e1ff8fa33 | -6.90678 | -38.26539 | 2025-10-15 03:47:00 | NPP-375D | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cbb71369-f099-3211-862a-9c564e7e7c93 | -5.95473 | -43.17288 | 2025-10-15 03:47:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| cc9b42e0-bfcb-30bd-8ca1-9b5e66f8a350 | -7.56833 | -42.68003 | 2025-10-15 03:47:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0218ae00-d9d1-39da-ab55-56b10fac15ec | -15.38185 | -39.21755 | 2025-10-15 03:47:00 | NPP-375D | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5c4482fb-023d-34d2-b1d8-37dba67ff3a4 | -6.9928 | -38.44736 | 2025-10-15 03:47:00 | NPP-375D | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 62cc9a94-1d26-304e-8e06-48ed4cd9871a | -4.39644 | -43.62078 | 2025-10-15 03:47:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bcb88cfe-4990-3a81-959c-1c89b7b4896e | -6.02598 | -44.31509 | 2025-10-15 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1b8df3e-885d-30d8-a0eb-45c0b2ad7d0a | -4.82504 | -45.44365 | 2025-10-15 03:47:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 531dbffb-a37b-37ae-9402-6c59bb35e028 | -7.9549 | -44.14808 | 2025-10-15 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b7814b3-e34c-3259-9073-ab6ac4df84b9 | -11.22793 | -39.23836 | 2025-10-15 03:47:00 | NPP-375D | ARACI | BAHIA | Brasil | 2902104 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ea8310ac-a967-3901-93bf-234690813847 | -7.17117 | -42.19247 | 2025-10-15 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4efd919a-f50c-3301-ae20-c48f594bee58 | -6.88767 | -43.96824 | 2025-10-15 03:47:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98b8f15f-8c48-3012-9dc1-ad638cc4528c | -5.32071 | -42.92729 | 2025-10-15 03:47:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cb30dc30-64cd-3588-b06e-6efa4b1e386a | -8.45601 | -44.19527 | 2025-10-15 03:47:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5e9559e6-caea-38ba-af30-7d407f7d6c19 | -6.90838 | -38.26422 | 2025-10-15 03:47:00 | NPP-375D | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README17.md)
