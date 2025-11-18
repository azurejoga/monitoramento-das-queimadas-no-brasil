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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5bc4bb5-24d7-3096-a987-d12d2c242160 | -3.35788 | -48.39943 | 2025-11-18 12:16:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 7d828f7b-0757-3609-8d62-ee3f6d29e310 | -3.60815 | -43.60651 | 2025-11-18 12:16:00 | TERRA_M-T | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| cb9bf826-f738-365c-9805-b78221e8e513 | -9.0138 | -44.82447 | 2025-11-18 12:16:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 40543019-2e32-3f81-8e96-08eceade2e5b | -3.69921 | -42.34361 | 2025-11-18 12:16:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 23.2 |
| ae59cf79-eb08-3713-ba8b-950413b30166 | -7.73912 | -44.73096 | 2025-11-18 12:16:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 93ab50ca-81bc-3dd0-a68a-df284a506162 | -2.65296 | -48.04095 | 2025-11-18 12:16:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| da920326-cd5e-367d-88e0-0f306ef68059 | -8.1566 | -47.63857 | 2025-11-18 12:16:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 9af3855f-9b4c-3ee7-92bd-523586d2dd15 | -2.51957 | -47.811 | 2025-11-18 12:16:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 15740d3d-f8f0-3c1b-9080-4a4cc23fc8d8 | -3.35107 | -43.49605 | 2025-11-18 12:16:00 | TERRA_M-T | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 844a4253-9cec-3329-9321-1240696cc47d | -5.33415 | -43.76032 | 2025-11-18 12:16:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| d6e6ae2d-11c5-34f1-99c7-ad33b215c63d | -7.75096 | -44.72024 | 2025-11-18 12:16:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 98a62555-4081-38d5-8c5f-eb8c1c9ac86b | -8.29737 | -43.99334 | 2025-11-18 12:16:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 4c3dc58e-b375-351c-bb21-0fa418074c64 | -8.20597 | -49.78781 | 2025-11-18 12:16:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 4cc1206b-0097-3bfa-a0d2-08f30362b6cd | -3.75337 | -42.27702 | 2025-11-18 12:16:00 | TERRA_M-T | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 29.4 |
| 8ccd89ef-eeda-34ff-b56b-927fb691ece1 | -3.36395 | -41.46867 | 2025-11-18 12:16:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 27.3 |
| c74dd58e-a71f-3b9e-bd42-103612a9682a | -8.0639 | -38.01533 | 2025-11-18 12:16:00 | TERRA_M-T | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 67.2 |
| c622c629-6857-3dbd-a13a-9be0e96f26d4 | -9.01215 | -44.83683 | 2025-11-18 12:16:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 41.6 |
| c24059fe-b6a1-3f52-a80f-32c1eff4163e | -7.75951 | -44.73375 | 2025-11-18 12:16:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 98.8 |
| bc0cd8cb-90a2-3944-b3d0-6c82a0cb2c05 | -5.32915 | -43.75376 | 2025-11-18 12:16:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 0309c079-5443-3ad6-8f51-437b926b9100 | -4.53118 | -45.60941 | 2025-11-18 12:16:00 | TERRA_M-T | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 8dbe0f88-e65e-3338-8309-ea5b88b3d693 | -8.41748 | -44.03023 | 2025-11-18 12:16:00 | TERRA_M-T | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 270.2 |
| 39ff58a1-775c-3734-bddb-d7746d03ec08 | -3.08544 | -50.34911 | 2025-11-18 12:16:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e5bd2116-d4c7-3182-8ac7-3fcd4aeb1b70 | -3.0254 | -44.48203 | 2025-11-18 12:16:00 | TERRA_M-T | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 14433393-9208-3d19-adb2-c20a0c453cd1 | -4.87594 | -42.53878 | 2025-11-18 12:16:00 | TERRA_M-T | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 0d8edeb4-9486-30fa-a37e-3a74adf5adff | -3.66536 | -42.4179 | 2025-11-18 12:16:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 37.2 |
| 530a86fb-2e92-3f05-8d0a-a1828d71c4d1 | -3.28317 | -41.91924 | 2025-11-18 12:16:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 30.8 |
| 1208e0ca-a0fd-3c97-8866-1b2a250eb1ca | -3.36941 | -41.45772 | 2025-11-18 12:16:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 51.0 |
| 05e4da2f-a91e-3ec0-9d0b-9256eac997b5 | -3.23818 | -50.49788 | 2025-11-18 12:16:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| cf3f0173-e073-32e8-89af-bc4ccd79caa8 | -5.34644 | -43.7488 | 2025-11-18 12:16:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 27eb0e71-81db-34a2-aa2d-3f850dc0c349 | -3.70815 | -42.17315 | 2025-11-18 12:16:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 456.2 |
| b46b1cf9-c8ef-3ba8-81e2-14437c89e334 | -4.44401 | -49.18639 | 2025-11-18 12:16:00 | TERRA_M-T | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| cf8af161-5888-3152-914f-e74506d0a85b | -3.07495 | -42.36446 | 2025-11-18 12:16:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 7fcc5499-f708-31e6-a3d5-b9e312627599 | -3.88549 | -46.46536 | 2025-11-18 12:16:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| eec8e7a5-6e29-3226-b041-de8dd22426c3 | -3.94871 | -46.14892 | 2025-11-18 12:16:00 | TERRA_M-T | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 04140f98-8703-37db-be2b-34b0af54d2a4 | -8.55258 | -46.0504 | 2025-11-18 12:16:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 8bc235e7-a84f-33cb-a41e-19cec5cf9a9a | -3.71029 | -42.15703 | 2025-11-18 12:16:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 19.3 |
| a6c3dba6-2361-33d2-b104-a6cb6971f8ea | -3.47992 | -46.07229 | 2025-11-18 12:16:00 | TERRA_M-T | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 5b9cdf55-f57d-3821-8a3f-4c8102ed3665 | -7.84459 | -48.46764 | 2025-11-18 12:16:00 | TERRA_M-T | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| f52b11f0-5423-38ac-9be4-98b999dad5af | -8.46688 | -47.98881 | 2025-11-18 12:16:00 | TERRA_M-T | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 28d9576e-0b60-3d78-9200-96993948c0fb | -8.62787 | -40.80979 | 2025-11-18 12:16:00 | TERRA_M-T | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 44.8 |
| 0123f767-ec52-3c68-b9c7-3614b84e8a2b | -7.50413 | -37.98897 | 2025-11-18 12:16:00 | TERRA_M-T | NOVA OLINDA | PARAÍBA | Brasil | 2510204 | 25 | 33 | nan | nan | nan | Caatinga | 61.2 |
| 4516220b-4414-32b4-9b53-1c901b154e5b | -3.70803 | -42.35082 | 2025-11-18 12:16:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 28.2 |
| 5a3ca80f-d17e-3520-945c-6205acc66722 | -0.98707 | -52.43866 | 2025-11-18 12:16:00 | TERRA_M-T | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| ca038f9a-f91d-3b52-a8fe-dc013704bc4b | -2.98575 | -44.19667 | 2025-11-18 12:16:00 | TERRA_M-T | ROSÁRIO | MARANHÃO | Brasil | 2109601 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 02795308-ffb3-3ef5-9abf-ac299a529176 | -1.40357 | -47.61686 | 2025-11-18 12:16:00 | TERRA_M-T | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 68333e01-c60e-35d4-ac49-6acc71202086 | -5.26716 | -40.6696 | 2025-11-18 12:16:00 | TERRA_M-T | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 28.4 |
| 9343a724-5542-3145-a87f-ef78a8e84ff1 | -4.27753 | -44.24921 | 2025-11-18 12:16:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 567b45bd-3b46-3eb9-8d75-4ec3a764b08d | -8.15787 | -47.62961 | 2025-11-18 12:16:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 96c5165b-b41f-3f4e-870e-98769b969600 | -8.47696 | -47.98117 | 2025-11-18 12:16:00 | TERRA_M-T | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 0e5deb82-415e-3655-8d0f-da0afc48fa2c | -2.87073 | -44.1344 | 2025-11-18 12:16:00 | TERRA_M-T | AXIXÁ | MARANHÃO | Brasil | 2101103 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| c0145582-a4bb-345e-892d-6ce5ad07f69c | -8.46032 | -45.14114 | 2025-11-18 12:16:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 92.9 |
| f0fbdd06-b5d9-329c-aadf-690bf7f61d2f | -7.68843 | -44.58129 | 2025-11-18 12:16:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 5587dc31-0875-3a40-abce-a0b3ccb09599 | -5.29397 | -46.74965 | 2025-11-18 12:16:00 | TERRA_M-T | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7880bdc4-c421-3a3b-8d26-77eb392b7c0a | -5.33972 | -43.75521 | 2025-11-18 12:16:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 9cec224d-236b-3a3b-9dd5-cc2b8d2b33d3 | -2.76358 | -48.42644 | 2025-11-18 12:16:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4520fd19-6037-33b8-99a6-a7e82ea564fd | -3.34266 | -48.37897 | 2025-11-18 12:16:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| feaeceb9-5383-378a-82e5-76ffa9e11461 | -4.31663 | -44.84824 | 2025-11-18 12:16:00 | TERRA_M-T | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 6cfa97be-fae9-323e-bc31-16e03ad694ce | -8.63103 | -40.78447 | 2025-11-18 12:16:00 | TERRA_M-T | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 42.8 |
| 9e6b237f-d231-3d62-9787-e4a9e2f55de7 | -0.85679 | -47.5666 | 2025-11-18 12:16:00 | TERRA_M-T | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5916d807-45a8-37db-850d-efa5a8bc2eb1 | -1.901 | -45.81778 | 2025-11-18 12:16:00 | TERRA_M-T | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 55238edd-7554-3bc2-b612-dedf75676557 | -1.11088 | -48.10478 | 2025-11-18 12:16:00 | TERRA_M-T | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| d213a68e-614d-3cdb-93fa-a04e57e16501 | -4.64151 | -47.94523 | 2025-11-18 12:16:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 31b8d113-dbd1-3f30-8df5-561f876ce4a1 | -3.70053 | -42.16628 | 2025-11-18 12:16:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 21.0 |
| 7319767e-12a2-38ef-9d85-3eef9b84d120 | -2.02478 | -47.15063 | 2025-11-18 12:16:00 | TERRA_M-T | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4ef9be42-5dac-3d98-a16d-0110d846dfbf | -8.45932 | -47.97871 | 2025-11-18 12:16:00 | TERRA_M-T | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 42.4 |
| e47aaf63-d941-3b35-98b8-1c71d065f1b0 | -5.32735 | -43.76669 | 2025-11-18 12:16:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ff2b8d77-6442-31e3-bf3a-1c5587319149 | -3.83897 | -42.14785 | 2025-11-18 12:16:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 93.0 |
| aa6958dd-853a-334f-9638-11295679fc2d | -8.21033 | -45.02483 | 2025-11-18 12:16:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 8d2ca259-d333-3a0d-a169-84de60ef1d2c | -5.2927 | -46.75869 | 2025-11-18 12:16:00 | TERRA_M-T | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 8911eec8-17d9-3f93-aa56-64e157a3d700 | -6.21572 | -46.88335 | 2025-11-18 12:16:00 | TERRA_M-T | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9e5c5819-cd18-3469-804b-66c9838efa15 | -7.30878 | -49.35428 | 2025-11-18 12:16:00 | TERRA_M-T | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| eda4b3a4-7f76-3d7a-91e8-9588ab167f0e | -3.83677 | -42.16413 | 2025-11-18 12:16:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 5d98526c-edda-3f6d-87f6-6d459b9b0c36 | -4.10428 | -41.99303 | 2025-11-18 12:16:00 | TERRA_M-T | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 30.4 |
| 09bed2c9-5915-3b4e-90e3-01eea69ccd22 | -8.14901 | -47.62836 | 2025-11-18 12:16:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0c3babb8-2156-36ad-ac7d-ccbd976e47a0 | -8.22834 | -48.30388 | 2025-11-18 12:16:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 0849e80f-5082-341f-8ea3-543c758b3e2e | -3.75121 | -42.29269 | 2025-11-18 12:16:00 | TERRA_M-T | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| e4c1a5b8-e80c-324d-9fe7-d40088b63341 | -3.46781 | -42.08994 | 2025-11-18 12:16:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 100.0 |
| 4dec3f32-af84-38c7-81f5-bf888244a1e2 | -8.46292 | -45.12349 | 2025-11-18 12:16:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 8eb90866-e9e4-3fd7-8943-5980e3a78dcc | -8.19694 | -49.78654 | 2025-11-18 12:16:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 09248f71-427f-395c-b7c7-77783245c643 | -4.1416 | -46.34673 | 2025-11-18 12:16:00 | TERRA_M-T | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 0a5bacdc-9103-3ca3-9af6-abaf4a2214e5 | -7.54889 | -41.18423 | 2025-11-18 12:16:00 | TERRA_M-T | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 22.3 |
| b3ba5314-c5c0-3e0e-ace4-fb8c75c4d1ce | -6.44095 | -43.80806 | 2025-11-18 12:16:00 | TERRA_M-T | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 2ef74456-d527-34c3-9f59-72f87b3f4884 | -3.47092 | -46.07104 | 2025-11-18 12:16:00 | TERRA_M-T | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f2d3b9c3-57ef-37b8-8b6a-542623283a1d | -5.42884 | -43.04168 | 2025-11-18 12:16:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 58c56619-4983-3fed-832c-f394ded9b432 | -5.97357 | -49.39572 | 2025-11-18 12:16:00 | TERRA_M-T | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a70c9700-eb09-3d6a-aa0e-d06396f10ad4 | -8.87677 | -43.94742 | 2025-11-18 12:16:00 | TERRA_M-T | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 44.2 |
| e9658a14-506d-3bcc-a96d-bf09c383bdcb | -2.4757 | -50.24133 | 2025-11-18 12:16:00 | TERRA_M-T | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| f95d131e-3cc6-31ad-b5e8-d924320bc26b | -4.83214 | -47.77862 | 2025-11-18 12:16:00 | TERRA_M-T | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 1886c68f-b2ae-39a1-aefe-9b33538d11f3 | -5.33587 | -43.74731 | 2025-11-18 12:16:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 45faee92-8892-36f6-a4ee-81801b799183 | -3.17329 | -46.59958 | 2025-11-18 12:16:00 | TERRA_M-T | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f77e7422-64ad-3359-9dfd-86035a39ac3f | -3.60607 | -42.42577 | 2025-11-18 12:16:00 | TERRA_M-T | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 20.5 |
| ae4d08f2-7415-32cf-97d3-023daa131327 | -4.6503 | -47.94648 | 2025-11-18 12:16:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 55e1c36b-f855-3716-be92-01f7af16db02 | -6.95998 | -38.53917 | 2025-11-18 12:16:00 | TERRA_M-T | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 41.0 |
| 70eefd3d-8c4e-3b8f-a70a-101f2d093581 | -3.48612 | -41.54934 | 2025-11-18 12:16:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 204f3c30-654e-3dbb-a600-fc5540fda382 | -3.67273 | -42.19539 | 2025-11-18 12:16:00 | TERRA_M-T | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| e82c64c4-d1ab-31d3-aabf-4194dda2cf21 | -8.46138 | -45.13522 | 2025-11-18 12:16:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 79.6 |
| be65be5d-4fef-3dc9-82f7-c837020dd3d4 | -2.40461 | -45.71813 | 2025-11-18 12:16:00 | TERRA_M-T | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 14.8 |
| b9895dce-0ae7-37f9-952f-82393a1d515f | -3.46045 | -42.0825 | 2025-11-18 12:16:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 66.4 |
| d6188c76-1c43-3ba5-8f2e-32d42ca1eef3 | -3.07704 | -42.3492 | 2025-11-18 12:16:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 0d192c0b-4bba-358a-b924-c0e34b494f78 | -7.43458 | -48.93602 | 2025-11-18 12:16:00 | TERRA_M-T | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 6.3 |


[Clique aqui para ver as próximas entradas](README56.md)
