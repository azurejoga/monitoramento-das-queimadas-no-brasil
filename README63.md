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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73c119da-adb0-3404-bd05-ef0a18ed6fa9 | -6.2725 | -41.86803 | 2024-10-06 04:17:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ad5a5867-5e85-3293-80b4-414acfab8c83 | -6.272 | -41.84764 | 2024-10-06 04:17:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2ff03e1d-46ff-3dd6-a2e6-7644e3fe8ee0 | -7.35241 | -41.94699 | 2024-10-06 04:17:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 79c6b339-d4bc-3106-a1ca-fdd7fbda2190 | -7.34884 | -41.94648 | 2024-10-06 04:17:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5f914026-9d27-3a92-a861-d40c0678f83e | -6.93243 | -41.97443 | 2024-10-06 04:17:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| da52f840-daba-3841-a32a-3fb338dc89d9 | -6.8493 | -41.69028 | 2024-10-06 04:17:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ac01f7f1-2d5e-310a-bdeb-2d85304facaf | -6.84867 | -41.69436 | 2024-10-06 04:17:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bc7006d1-2f58-3c50-a593-7cc940648d18 | -6.84571 | -41.68978 | 2024-10-06 04:17:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6a047eaf-ab87-3401-a44e-c649e3e72119 | -6.84274 | -41.68515 | 2024-10-06 04:17:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c7c9a826-96cc-336d-82cd-ebb50b6c3fb9 | -6.80186 | -40.98697 | 2024-10-06 04:17:00 | NOAA-20 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4d66fbee-e13b-37fe-aa53-c9de2ea719b6 | -6.49306 | -41.38132 | 2024-10-06 04:17:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 52dd38d1-4136-3f88-b2a8-0a3b1182978a | -6.49007 | -41.37648 | 2024-10-06 04:17:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 542d6681-c8a3-311e-9b6b-5a36ab2e7e2d | -6.48945 | -41.38071 | 2024-10-06 04:17:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 29927805-cbeb-3955-b6c9-33e82d765cfa | -6.48913 | -41.3778 | 2024-10-06 04:17:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a63f61e5-6ce2-31cb-b3fa-778d75520a75 | -6.47745 | -41.94663 | 2024-10-06 04:17:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0248621b-df46-3332-b537-24599fe6fa6d | -6.47685 | -41.95059 | 2024-10-06 04:17:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a3990d42-c952-3071-8f79-983d08bc2d29 | -8.42224 | -41.94525 | 2024-10-06 04:17:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4df05263-aff5-33bf-914d-5c45af63fd57 | -8.28395 | -41.13572 | 2024-10-06 04:17:00 | NOAA-20 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5171fa37-4f4d-38b6-b356-9d56ef102719 | -7.69091 | -42.98548 | 2024-10-06 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 9d47378f-65e9-37fa-8365-8eb36b3aa829 | -2.92333 | -41.4668 | 2024-10-06 04:17:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 502d0ad3-89d9-38f1-9fc3-4e0805d7d350 | -6.07415 | -42.33908 | 2024-10-06 04:17:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c2439e72-e1c8-3eaf-a49b-9d663a0ede7f | -5.94997 | -43.38868 | 2024-10-06 04:17:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4e0defd7-b6fc-36c6-9485-f3e280fa1f12 | -5.94078 | -42.43145 | 2024-10-06 04:17:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3060150c-f371-3c88-8856-5c0bf2a94eb0 | -5.91844 | -42.80347 | 2024-10-06 04:17:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 67ec95d6-893a-3fa7-b98d-9109a1db7250 | -5.74056 | -43.05039 | 2024-10-06 04:17:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a7e8ae33-d728-3ad8-9a53-e29b1ed2e6dd | -5.68647 | -43.15566 | 2024-10-06 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 90adeab6-d979-3c1e-bfb9-44eb7302bbc4 | -5.68311 | -43.15515 | 2024-10-06 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c1b6cdcd-c66b-330d-9753-3ddbe4fbbfc2 | -5.68256 | -43.15872 | 2024-10-06 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7dc0baac-9891-327d-9bcb-4bf0a92b221d | -5.68201 | -43.16228 | 2024-10-06 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3e92b3e9-e7d6-351d-934a-1bfae7f9e3f9 | -6.13701 | -43.38492 | 2024-10-06 04:17:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3d188820-c675-347b-8664-fa4e2f086c39 | -6.44106 | -43.12315 | 2024-10-06 04:17:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 365ac898-87e1-37fb-ae32-64867c8907e0 | -5.94663 | -43.38816 | 2024-10-06 04:17:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2bfc551d-82a8-302e-98f9-e06432f88f50 | -6.23462 | -43.38904 | 2024-10-06 04:17:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 74c97c82-dba6-3198-861a-542a2afe8212 | -6.13366 | -43.3844 | 2024-10-06 04:17:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f01ff714-844a-3345-90b5-f59948e0b066 | -7.79368 | -43.11449 | 2024-10-06 04:17:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 33498ef2-6aca-3998-a484-1dc7ccfef152 | -7.772 | -43.07345 | 2024-10-06 04:17:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4f363868-dbcb-3f44-96b1-7c5ac20cdaea | -7.77145 | -43.07712 | 2024-10-06 04:17:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8a8eeba0-a4e2-31dd-bfa4-b530354a4bbd | -7.76804 | -43.07658 | 2024-10-06 04:17:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8ec3b5bd-f3c9-3a51-ba9d-0866b268332d | -7.76748 | -43.08024 | 2024-10-06 04:17:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| dea2e794-3238-32bc-a5b1-f5187d83613b | -7.76122 | -43.0755 | 2024-10-06 04:17:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 34cfadfa-a823-3442-ade7-bda21f167027 | -7.75488 | -43.04814 | 2024-10-06 04:17:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 16bb3747-8f23-3ab3-a1c6-f83c3f97a32c | -7.74784 | -43.04747 | 2024-10-06 04:17:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3f46ffe2-82c6-379b-bef9-ca93795ead2f | -7.74702 | -43.07709 | 2024-10-06 04:17:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| dcc2f354-22ec-3f47-905d-cecbce537d0b | -7.74443 | -43.04695 | 2024-10-06 04:17:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 1154330e-1bfd-3582-a47a-8e197d11e3ff | -7.74386 | -43.05066 | 2024-10-06 04:17:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 580dee4c-9e66-3b36-b6c7-baf486d470f5 | -7.74045 | -43.05013 | 2024-10-06 04:17:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| d495ca28-feae-3f5d-b416-768cb2a3bc42 | -7.73988 | -43.05383 | 2024-10-06 04:17:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 507e4201-5518-3396-9e31-84ff673758d5 | -7.73931 | -43.05753 | 2024-10-06 04:17:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b80757bf-44d4-3b06-843c-27c30b80d2e9 | -7.73874 | -43.06122 | 2024-10-06 04:17:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 583c1661-94d1-3eb2-b2b3-be335873af50 | -7.73817 | -43.06488 | 2024-10-06 04:17:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8b272930-2451-3c1f-9a9e-8076aca30eca | -7.73761 | -43.06853 | 2024-10-06 04:17:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d26fc02e-ff53-34e0-9237-2cca33ce3cb0 | -7.73646 | -43.05331 | 2024-10-06 04:17:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 707cde0a-979a-3707-9bfb-896a77026277 | -7.7359 | -43.057 | 2024-10-06 04:17:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 7ea26af5-932e-3df2-b084-9a29b0ff8cbc | -7.73533 | -43.06068 | 2024-10-06 04:17:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| d949e199-3275-3dcd-90fc-16b7bd257c0b | -7.73477 | -43.06435 | 2024-10-06 04:17:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| f3b1027f-6f44-30bc-933c-ca13b89e6e85 | -7.73421 | -43.06799 | 2024-10-06 04:17:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 295b0d8e-a3e6-37c7-84ff-f4c562700407 | -7.69945 | -42.97532 | 2024-10-06 04:17:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| a6741140-821b-3318-bb61-d34e9b25f7b3 | -7.69888 | -42.97907 | 2024-10-06 04:17:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 117e92a0-b3bc-3f54-9bb9-bbd03599940e | -7.69603 | -42.97481 | 2024-10-06 04:17:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 0fe69593-9831-3de8-863f-ae85f55bb80a | -7.69546 | -42.97856 | 2024-10-06 04:17:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 28fb85ab-9c07-3d4a-8470-5200d49a9186 | -7.69489 | -42.98228 | 2024-10-06 04:17:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 0e943909-93bb-3038-994a-996e68d461c0 | -7.69432 | -42.986 | 2024-10-06 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 5dbe9bc1-5895-3fcf-8c81-b3e5bac9e7af | -7.69147 | -42.98176 | 2024-10-06 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3118c293-ea60-35f0-894c-2a0abd101cba | -7.66008 | -42.44781 | 2024-10-06 04:17:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 49409304-9ce3-3231-b9a2-390d4fd67389 | -7.65662 | -42.42327 | 2024-10-06 04:17:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 82df31fc-1111-309c-9c03-194b7bfdfb9b | -7.65371 | -42.41882 | 2024-10-06 04:17:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 56ecaa34-144e-3109-8537-bec693d522fa | -7.65021 | -42.4183 | 2024-10-06 04:17:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3da1b08b-9294-3324-a207-ce03ea930947 | -7.64672 | -42.41778 | 2024-10-06 04:17:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d531f6db-a42d-3c41-af65-3b54af340412 | -7.64322 | -42.41726 | 2024-10-06 04:17:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2d48e1f9-3935-3270-b44c-a3965d348c2a | -7.64029 | -42.48451 | 2024-10-06 04:17:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8504d92d-f07c-36a4-8f1b-3cd9d2d4e506 | -7.63972 | -42.41674 | 2024-10-06 04:17:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f2fbc10b-0a9d-3b74-a1d1-45cdde5c0687 | -7.63971 | -42.4884 | 2024-10-06 04:17:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0246ce59-0458-306c-a743-f24009f73cca | -7.63913 | -42.49227 | 2024-10-06 04:17:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 95f000c2-5fd9-3ccb-b2bf-212ebd98b3d0 | -7.63855 | -42.49614 | 2024-10-06 04:17:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| dd6a7b0c-e426-332b-bdb7-c4e205cfae61 | -7.63797 | -42.5 | 2024-10-06 04:17:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f1daed7c-2b99-313c-9669-adf423288a24 | -7.63623 | -42.41621 | 2024-10-06 04:17:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1761d20e-06a9-3409-9a39-6d753678bb1d | -7.63449 | -42.49947 | 2024-10-06 04:17:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| af2a9271-bd20-3ca5-8f53-a569f33d0258 | -7.63215 | -42.41959 | 2024-10-06 04:17:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1d7a61c7-c9cd-36e8-b4bc-d23cc3ade507 | -7.63159 | -42.49507 | 2024-10-06 04:17:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 7a48d682-f029-37df-8d88-25d2d47916bd | -7.63157 | -42.4235 | 2024-10-06 04:17:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4450d940-e07a-37ec-b5a4-1660147ae13b | -7.63101 | -42.49894 | 2024-10-06 04:17:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| aacd0d8f-7e99-3b62-85ef-0ce99d760546 | -7.63089 | -42.42027 | 2024-10-06 04:17:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d197b7a5-edaf-35d5-bf5e-48066f281947 | -7.6281 | -42.49453 | 2024-10-06 04:17:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d8f6ad58-8b57-3f63-a784-5bf79d02fc5f | -7.6252 | -42.4901 | 2024-10-06 04:17:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1ed8109f-88b9-33c0-9310-4fb7203056e8 | -7.62462 | -42.49398 | 2024-10-06 04:17:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2c914314-7e87-3738-8ccf-8a167f60d870 | -7.61505 | -42.45365 | 2024-10-06 04:17:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c809404d-b657-39fa-9c2a-607f5a77ada0 | -6.65124 | -42.11178 | 2024-10-06 04:17:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f85db5ca-00a2-3212-85a9-a3d324208993 | -6.65064 | -42.11573 | 2024-10-06 04:17:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f7c17e10-f902-3c1b-a728-79f849344383 | -6.64652 | -42.11923 | 2024-10-06 04:17:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 35501c65-15b5-3d1f-95ef-c6bbf03ef270 | -6.64592 | -42.12319 | 2024-10-06 04:17:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b7a670ef-77de-360c-b332-05ae4674144e | -6.64241 | -42.12268 | 2024-10-06 04:17:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 670b97c5-a1f9-3849-bff2-5e3188644c71 | -6.63831 | -42.12609 | 2024-10-06 04:17:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 34dd6b89-e4a7-36a7-b21b-529e5c72dfee | -6.63772 | -42.12998 | 2024-10-06 04:17:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 07dedfc5-70b2-35d9-8959-8fee9342dff9 | -6.63481 | -42.12556 | 2024-10-06 04:17:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b1f19deb-3405-3fa1-8f5c-eb3afd4f2be1 | -6.63422 | -42.12946 | 2024-10-06 04:17:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6765f167-d1ea-3978-9f17-914d41c863e0 | -6.63309 | -42.11324 | 2024-10-06 04:17:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b6343b31-dc2b-36cd-a627-97b591ebb8f9 | -6.63071 | -42.12893 | 2024-10-06 04:17:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8ff7d3ba-58ea-3169-8630-edb3d8ee5968 | -6.63013 | -42.13281 | 2024-10-06 04:17:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0ca2ab55-df36-3b49-81f5-7028aa8e596f | -6.62721 | -42.1284 | 2024-10-06 04:17:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 58ecf533-b832-347c-bfd1-71c9ac1962e1 | -6.62662 | -42.13229 | 2024-10-06 04:17:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |


[Clique aqui para ver as próximas entradas](README64.md)
