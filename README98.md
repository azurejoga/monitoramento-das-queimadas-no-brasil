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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33e4d97f-a406-35d6-a970-c5c27012cff1 | -5.0202 | -45.48579 | 2024-10-04 04:32:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05f668f8-3d5d-34e6-b5b3-0f4ea5b51ac7 | -5.00529 | -45.49107 | 2024-10-04 04:32:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f4cf079-cf6f-3450-b8bc-dd446a24d15a | -4.9579 | -45.50737 | 2024-10-04 04:32:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4960369b-d71a-339f-a81f-ebbf0d73ca4d | -4.95446 | -45.50686 | 2024-10-04 04:32:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0bea4de1-a86a-3040-8f22-0ceb3307732c | -4.87101 | -45.77369 | 2024-10-04 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a18a524-cc34-31d1-b2d9-e9bf78ccad1b | -4.87045 | -45.77734 | 2024-10-04 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dca7a93e-11f0-3518-8f0b-7e8f5cf9ff14 | -6.33313 | -45.68361 | 2024-10-04 04:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5cf60987-6c0e-3190-9cd1-39cfff9fe09e | -6.32969 | -45.68301 | 2024-10-04 04:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31e173cb-8822-3782-b616-aa46547d71ef | -6.09271 | -45.95287 | 2024-10-04 04:32:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3538a6c9-d8a6-3bfc-ad69-f6c345751409 | -6.09223 | -45.95208 | 2024-10-04 04:32:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a53f5a30-d517-3f91-82a2-7403f43d4766 | -6.08702 | -45.94444 | 2024-10-04 04:32:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2315c167-3420-33bf-83a3-6e9e68b669a8 | -5.97447 | -45.37387 | 2024-10-04 04:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b77b7d6-59e9-387c-9eb5-df561f95e2ab | -5.97389 | -45.37771 | 2024-10-04 04:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 916cb564-c2db-3a6d-9b6e-fef52a9f71e1 | -5.97331 | -45.38155 | 2024-10-04 04:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 22665991-1256-3be5-b954-5c3e7f0c66f6 | -5.97273 | -45.38538 | 2024-10-04 04:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 04ae339a-a3e1-3e2d-82e6-5341db66bf15 | -5.97041 | -45.37716 | 2024-10-04 04:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7dc36314-d462-3ed9-a4f1-f36049b5e33d | -5.96983 | -45.381 | 2024-10-04 04:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 068ff302-e4cf-3291-984a-01f432c12063 | -5.96925 | -45.38484 | 2024-10-04 04:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bc449273-e034-35f1-b0c6-8bfac07cf245 | -5.96693 | -45.3766 | 2024-10-04 04:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c8e3d143-8fd4-363b-995c-a92d7c86cf32 | -5.96635 | -45.38045 | 2024-10-04 04:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e6224dc6-a58a-3161-a313-a323b593129b | -5.96596 | -45.37752 | 2024-10-04 04:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a13baaab-5601-3659-906b-1c03fde8a308 | -5.96577 | -45.3843 | 2024-10-04 04:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 866fd58a-d934-3bad-923d-a6c5c3f9f5de | -5.96536 | -45.38137 | 2024-10-04 04:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 89a7195b-430f-3146-9b96-095b196566fd | -5.96476 | -45.38521 | 2024-10-04 04:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 81bffa95-1444-323b-a6b8-5da61777fc5b | -5.89174 | -46.27981 | 2024-10-04 04:32:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b17354b-017c-34ad-a332-4e465fb99109 | -5.79489 | -45.08688 | 2024-10-04 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| edb47f61-a42c-3273-b466-0ac79535b729 | -5.79465 | -45.08559 | 2024-10-04 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6c86f30c-eb3d-3642-ae00-d9d1afa294bf | -5.79406 | -45.0895 | 2024-10-04 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 185185ce-45cc-3778-b26b-ad18e0867606 | -5.79136 | -45.08634 | 2024-10-04 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fe016108-02c8-35de-a268-7f69c9024f57 | -5.79113 | -45.08506 | 2024-10-04 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 223e36c4-94f2-30bb-85c1-43597842f4f3 | -5.79076 | -45.09025 | 2024-10-04 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 272ee10f-15d2-3f52-b0df-e79f75309df5 | -5.79054 | -45.08897 | 2024-10-04 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0ec1de54-2589-3b07-96b5-026155c9b6db | -5.78724 | -45.08973 | 2024-10-04 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b7212b9a-f168-3d7c-8b32-c3190fe8c71b | -5.71909 | -46.40751 | 2024-10-04 04:32:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 389d48bd-2661-30f1-bca5-aa8ed2a48a7f | -5.59909 | -46.37056 | 2024-10-04 04:32:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2a81676-e2cb-3d6f-9849-8c5c8f37b05b | -5.29514 | -45.17285 | 2024-10-04 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d06c3c3b-3dc8-3aca-a322-350104ded48d | -5.10406 | -46.14146 | 2024-10-04 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| acb471b5-8cd4-3618-bb6c-1a76a41d12c9 | -5.08935 | -46.11744 | 2024-10-04 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b478b04-1891-3123-b71f-d645a1ef64d9 | -5.08879 | -46.12101 | 2024-10-04 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c72151e2-1809-3f13-9316-185c46db5ae4 | -5.59854 | -46.37413 | 2024-10-04 04:32:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 478bb492-a837-36bd-860f-c6e697284866 | -5.59517 | -46.37362 | 2024-10-04 04:32:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d1ae113-6c55-305e-a811-a3a36c9d87dc | -5.29863 | -45.17339 | 2024-10-04 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3bc89ac-9b4c-39bb-88c7-898d4e3c018e | -5.10798 | -46.13843 | 2024-10-04 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 747c3a36-a3b9-36a2-8ad9-660a786e2ea8 | -5.10743 | -46.14199 | 2024-10-04 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4bab160-94c8-3b94-b794-472499338b52 | -5.10461 | -46.1379 | 2024-10-04 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b76ea58-dfff-31fa-85c3-5daa10788add | -7.91034 | -46.42482 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4005596-ed3a-3e23-886c-22ee85ff9d65 | -7.76738 | -46.15361 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c4ff0c15-c0b8-3857-8621-d9782e337e75 | -7.76393 | -46.15313 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 94d7273d-8d0f-3950-8a91-86efc6fad47d | -7.76336 | -46.15685 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| edacd20b-fe32-3b7f-98e1-a4a65c4a013e | -7.76049 | -46.1526 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| f6e01c7e-fec6-3f13-ab18-4790134dacbb | -7.75992 | -46.15635 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| bad34cb8-7811-37c8-a80c-c165cea5bc50 | -7.75706 | -46.15206 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ecb4d34e-1184-3d9f-831d-3d643d88a185 | -7.75648 | -46.15583 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 487a309e-b4b2-3d3a-b96b-bc326e55880c | -7.75362 | -46.15151 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e29341d0-e3ec-3851-a39a-62f5b6515e4d | -7.75019 | -46.15096 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 297623de-bdd0-32f1-a401-c49e9a1afcaf | -7.74675 | -46.15041 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 003b46e4-5541-3e41-ba7e-bc0395638213 | -7.7439 | -46.14608 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 964ce539-03f4-3304-9f4d-53f8c268e2ab | -7.74332 | -46.14988 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ee33cbe8-9acf-342d-a2dc-7944e67faedc | -7.74104 | -46.14178 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04d57ff8-42b5-3987-a918-be2a9092fd49 | -7.70783 | -46.1519 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 65ae7963-7863-3ad0-a225-32a1365c4f6b | -7.70439 | -46.15134 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34905e0f-1d12-3a39-8a0b-811b2cc2e90c | -7.70213 | -46.16624 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 050ebe07-cb94-344d-9089-0df8d95de678 | -7.70096 | -46.15079 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d57e2070-408c-3b08-9f27-19a46eb124de | -7.70039 | -46.15456 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2afbdfd1-22e0-3ea6-9d28-857f2bbf65c7 | -7.69982 | -46.15829 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd9badaa-3956-3647-a860-439152774577 | -7.69814 | -46.16942 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b2cd285-5bae-30f0-8b2b-fd1c22e32521 | -7.69757 | -46.17315 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68964a2e-87d5-3f35-9741-6fc26a74ec85 | -7.69695 | -46.15401 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7825366-9fb0-39e7-81da-99f0a3ec3bc2 | -7.69639 | -46.15775 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7540799-08f2-32e9-8ea4-d17aade03a08 | -7.6947 | -46.16889 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37bc7cbe-f225-3e63-9323-ba1ec60d8083 | -7.69414 | -46.17262 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a0fe1b85-8cfc-3cee-a98e-e3c7badff2e9 | -7.69352 | -46.15346 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2f61d5d-26ba-395b-a4d4-1bd262eb6cdc | -7.69296 | -46.1572 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1dec3a3e-7b9f-3015-bb0f-6ae676d8e129 | -7.69183 | -46.16465 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a26b1e6-a566-3986-aa2e-80460f677b4d | -7.69127 | -46.16835 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9f9b2f5-ef81-36ad-a4cc-0933aab7a999 | -7.68839 | -46.16411 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9c63233-7ef7-32ea-8c34-e8f423f25632 | -7.68552 | -46.15983 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f98b60a-cbcc-31ba-88ca-970c4312e20c | -7.68496 | -46.16356 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 337578de-89e5-39c8-bd89-1110b8187f79 | -7.68222 | -46.16314 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0744e60-2cdd-31e0-9aea-02bd6e23bfd5 | -7.68153 | -46.16301 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89ccf15e-118d-3638-8775-9bada120d21c | -7.59785 | -46.4377 | 2024-10-04 04:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 990217b1-b7fa-310b-b830-2c771fe2d91a | -7.44487 | -46.48191 | 2024-10-04 04:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b62e76f8-98c9-38ad-8a4d-14fc7aee2f5f | -7.34737 | -46.20863 | 2024-10-04 04:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9ca6811-e6f6-3952-a3ec-f63e6ff56b54 | -7.33323 | -46.70552 | 2024-10-04 04:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c1e43d5-e0ee-38ac-a0db-fdce85739a41 | -7.33268 | -46.7091 | 2024-10-04 04:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bac30b73-fb20-3ed8-b212-c679d7e1930c | -7.21414 | -46.66567 | 2024-10-04 04:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d372f7f-7b13-3d65-b31a-3af27195ca47 | -6.63771 | -45.31981 | 2024-10-04 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20d14c81-cc84-3c60-af9e-7b62c5a3e0c9 | -6.6336 | -45.32319 | 2024-10-04 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 73477e01-98e9-3baf-8f08-cfb0c254d44d | -6.53661 | -46.10186 | 2024-10-04 04:32:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0bdf24e-1602-3fe0-be8e-bb2f653fcb95 | -7.78976 | -45.46412 | 2024-10-04 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8a87b869-6090-3461-a8f4-4c383446e794 | -7.73587 | -45.41572 | 2024-10-04 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e50c895b-e507-3dc1-8760-b90a1e8b3c74 | -7.73528 | -45.41964 | 2024-10-04 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e3bc3228-c22e-3bdf-b268-5010521fdbd8 | -7.70993 | -45.41968 | 2024-10-04 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bbac8943-8b23-30e0-b2b7-ee006ab560d1 | -7.63117 | -45.53843 | 2024-10-04 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 00b79a8e-e4d9-3192-8627-79f2194e7ccf | -7.62765 | -45.53788 | 2024-10-04 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 9ce8cd6e-4ac0-3b5f-8502-082b8c407463 | -7.62705 | -45.54186 | 2024-10-04 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 1f398b42-501a-3cc3-a2b2-567a702c4e13 | -7.62644 | -45.54584 | 2024-10-04 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ab31a6e4-925b-3d69-9b35-6efcc1508314 | -7.62584 | -45.54978 | 2024-10-04 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b11aad6f-8c07-3ef1-a7ce-d673f9a80314 | -7.62414 | -45.53734 | 2024-10-04 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 35.6 |
| c8e681e0-5609-3f51-a342-bff1cb11b8e8 | -7.62353 | -45.54131 | 2024-10-04 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 35.6 |


[Clique aqui para ver as próximas entradas](README99.md)
