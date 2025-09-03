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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6b736e3-d3f9-3736-b92d-b03f5a437633 | -7.7182 | -48.72377 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 19ffe183-2645-302c-808d-fbe23d28043c | -5.91531 | -57.73381 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 9ca1a371-bd1f-3671-8f18-4666e4820d62 | -5.85811 | -57.77117 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 65d99cd3-8ca5-30f3-ad1b-1373dabd6502 | -6.32829 | -58.17295 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9a9e77f-7528-3cac-bc1b-e80fa1293ad9 | -6.35079 | -55.55772 | 2025-09-03 05:12:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8f1eeaf6-4676-32a9-a169-451e575b7594 | -7.91583 | -46.4338 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 23eaeb2f-7345-30af-8519-efeee96eafce | -5.91253 | -57.7298 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 4b0be8ac-7e08-3938-a26d-d87ab314bd35 | -6.22378 | -43.38061 | 2025-09-03 05:12:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a21f0879-2827-3768-9904-67655ba26004 | -5.91697 | -57.72334 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cf57bf4b-5796-3061-8cbc-6034c33b747c | -8.01695 | -44.11589 | 2025-09-03 05:12:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aeb8d9b1-456b-3c8f-ba52-8be5e340d7f4 | -7.90003 | -46.45991 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 877c38e2-f295-3043-b38e-eaf1e9141a9c | -7.01371 | -44.36433 | 2025-09-03 05:12:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60664278-e6ca-361a-8e95-c8b2a62c1514 | -5.90754 | -57.7397 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 8e364dec-aff2-3a4a-8a3d-8d22594f6a56 | -5.55642 | -43.75429 | 2025-09-03 05:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f2c73240-b1d7-3c98-80fb-6c6a73f2af19 | -6.41448 | -43.76458 | 2025-09-03 05:12:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fbdf2f7b-707b-3083-8e80-0b6ec82a0795 | -6.83102 | -52.83875 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 33b94c85-6b38-3680-a2cd-8a6eecd91ed8 | -6.3389 | -58.17102 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2b62f64-c687-3b1e-b0df-2976d92ec058 | -7.01399 | -44.36567 | 2025-09-03 05:12:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2828b75d-5065-3d99-9feb-5bef39807405 | -6.46994 | -45.41428 | 2025-09-03 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fa825a57-1b85-39d5-acb9-7204d5d6230a | -6.34253 | -58.32022 | 2025-09-03 05:12:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7454e9c8-cd4d-315a-b97f-dad068fd17fb | -6.46501 | -45.40269 | 2025-09-03 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 369b7f99-4b1f-3b93-9eb4-e628401ff1c2 | -7.69363 | -48.74598 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 3779b3f8-5db4-372a-a2a0-2b2cdc7d9f69 | -2.5578 | -47.712 | 2025-09-03 05:12:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94f81d19-15bf-3c8b-be78-48ee25491390 | -6.77967 | -52.80917 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41964d67-dc96-37e3-9824-c17a301fc517 | -6.19795 | -43.35445 | 2025-09-03 05:12:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| dd07fd03-807c-3b9c-8a10-5eccbe549ad6 | -6.79147 | -52.81093 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ff0b038a-667c-3375-b117-7b4e7da2758e | -4.992 | -56.25369 | 2025-09-03 05:12:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b65ff04f-5ff4-3efe-bffa-2c1d7a0e235c | -7.70194 | -48.72489 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a7d64317-6896-3abb-b324-0ac6fa94ced3 | -6.53841 | -56.19738 | 2025-09-03 05:12:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90597d4a-f43d-3fef-8c2a-8404fb83bf5e | -5.87366 | -57.75938 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc777116-ecab-33a0-8251-2a2631ea078b | -6.47734 | -45.41162 | 2025-09-03 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5436cde-798e-3875-b110-3f275ca3b8bb | -3.8754 | -54.22868 | 2025-09-03 05:12:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3fe527b6-1afa-3318-8bc6-f7f98bfcb161 | -5.87033 | -57.75886 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| f6cc9cec-c287-3148-9d67-acd5de106158 | -6.19896 | -43.34692 | 2025-09-03 05:12:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 82126413-53a2-3e87-a93c-d22dbde18b2e | -7.62763 | -46.54198 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1f9e085-4ecb-3599-b6f6-cd0f8f7890de | -2.1458 | -53.64828 | 2025-09-03 05:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5f83b58c-285a-3132-9ce8-b34259e6f3e3 | -3.48294 | -48.44153 | 2025-09-03 05:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a3245a3-2843-3fec-8a88-112454682e3d | -5.90143 | -57.73516 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 91b824b5-1c8e-3316-8c70-24cea0db5817 | -5.91141 | -57.71532 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6d13aeb6-3f07-31b7-80cc-352182c231dc | -4.47986 | -48.11906 | 2025-09-03 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec0fc097-f60b-33bf-a445-57fd7bcbbf54 | -4.15172 | -46.78821 | 2025-09-03 05:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 22249396-66c1-3b41-acd9-c085533ac21b | -7.91011 | -46.47653 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 24d995b1-24eb-38ac-bb47-2b1a1399f624 | -6.47628 | -45.41573 | 2025-09-03 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 09c7bcba-67bb-38d9-ac23-58c813cb99b6 | -6.25777 | -57.89568 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f926cbf-d86c-3888-93e8-9b406500c786 | -7.90098 | -46.45169 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dd2d4fd5-e0e9-3bbd-97e0-5eff39efe552 | -5.80667 | -43.23736 | 2025-09-03 05:14:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| e925e110-f380-3bf5-8716-b13047953346 | -6.41049 | -43.75269 | 2025-09-03 05:14:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 7963c12a-9633-308e-9f06-66ace26756b5 | -8.88547 | -45.79765 | 2025-09-03 05:14:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 0453f96a-a807-34d4-8db5-1fe7ad52a274 | -6.17428 | -43.30553 | 2025-09-03 05:14:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 34.5 |
| dec41b92-ef3a-348b-90ba-02cd2cf26e86 | -4.89106 | -43.21206 | 2025-09-03 05:14:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 09350d07-3a4a-33a8-b6aa-4cdfb6efbcc8 | -6.17457 | -43.32285 | 2025-09-03 05:14:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| b9bd4e9e-dd12-3e4b-9723-3ae24222666a | -8.05908 | -45.36502 | 2025-09-03 05:14:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 564b7d15-1994-3cc4-a416-4c412ab0c28d | -5.53031 | -36.84482 | 2025-09-03 05:14:00 | AQUA_M-M | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 83901dbc-91d8-386f-aa8d-f5172ffc863c | -5.81974 | -43.22261 | 2025-09-03 05:14:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 463dc941-c010-3548-a951-d903d81d4682 | -7.93566 | -46.54219 | 2025-09-03 05:14:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 6ac1dc68-77d3-3828-8750-08c8c679f23f | -11.87987 | -40.94872 | 2025-09-03 05:14:00 | AQUA_M-M | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 475b6758-5eb3-3186-8fc3-91906561d96a | -6.17807 | -43.30114 | 2025-09-03 05:14:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 70e43456-6bce-36c5-b078-f8313a8fca7c | -7.47865 | -44.81636 | 2025-09-03 05:14:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 1b86d379-072e-3563-b0b5-4e1e82a2340b | -7.48001 | -44.80902 | 2025-09-03 05:14:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 93a7fe82-10f4-3c6e-b8b8-ab7d7cd76cf8 | -8.88866 | -45.79307 | 2025-09-03 05:14:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 29.9 |
| b957c59e-c339-355f-ba98-83eee4d647f4 | -5.81013 | -43.21589 | 2025-09-03 05:14:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 198dc77b-32fd-3b30-a181-9665e6f0c1b3 | -8.05755 | -45.36985 | 2025-09-03 05:14:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 34d117db-3296-3e69-bee0-075d19c7f24c | -6.1938 | -43.35329 | 2025-09-03 05:14:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 32c189b6-78d5-32d6-96e2-d16c4cd1c318 | -4.8993 | -43.21851 | 2025-09-03 05:14:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 4c2ac102-c33b-3db8-acb0-c24fca94e76b | -7.00252 | -43.24803 | 2025-09-03 05:14:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 910c117a-77f7-3a31-91a8-48eb8001c027 | -4.90312 | -43.19566 | 2025-09-03 05:14:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 96f7d72a-9a4d-3523-ae07-d7992d0272fa | -11.60834 | -52.07333 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0cea9cf2-9af6-3810-b7f1-f0f91222d134 | -11.03659 | -45.06862 | 2025-09-03 05:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3dc3e1b2-6bc4-39b2-ad3f-b595bd4380bc | -8.3706 | -48.30903 | 2025-09-03 05:14:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df6dea2f-c495-33c7-a3d8-3a4b247efabe | -9.63164 | -47.06096 | 2025-09-03 05:14:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2259f241-637e-3e50-9aed-e0b74c6bc41a | -11.86478 | -52.42225 | 2025-09-03 05:14:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6aa8b67-fbee-3843-a22c-354597dd8078 | -13.0126 | -48.10188 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| db42d422-f210-385a-82c3-6c632e1e18ed | -11.63226 | -52.06354 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3214090c-e90c-32b9-a435-e42708bc7548 | -9.63527 | -47.04016 | 2025-09-03 05:14:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f666ccc6-6a1d-3195-a6ab-06440f4769be | -12.84247 | -48.05863 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7b6c8c0-c985-36a0-973c-f3eed5fe8fd4 | -13.00304 | -48.09621 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 49ca456d-cb97-33db-9c4f-10e17f04332c | -10.13907 | -46.25089 | 2025-09-03 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa2fe8b5-483c-37c9-a8f3-a97f59151066 | -11.65738 | -57.35949 | 2025-09-03 05:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 787aa7a2-6578-3e7d-ab5c-9e066b121f36 | -10.55108 | -50.43686 | 2025-09-03 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7af82cb0-3786-3095-a211-c346e1c6efe8 | -11.81971 | -51.44317 | 2025-09-03 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95ccee78-6b3e-33e5-9960-aa34901b44c2 | -11.44786 | -47.30308 | 2025-09-03 05:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48c87a92-00d9-3da9-a0ef-9bd38015ca56 | -11.65102 | -52.05046 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77cfa94d-55d7-381c-8323-4c591b32c97c | -10.87464 | -60.73258 | 2025-09-03 05:14:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b38c6c7-66e3-3b9b-917e-0cf482fd52bc | -14.57574 | -48.04387 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7cbaaa79-9b30-3b26-88e2-2acaff7ec01c | -14.9797 | -50.19558 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f9ea431-c1a2-3816-af75-a90bd102fa59 | -11.86422 | -52.42637 | 2025-09-03 05:14:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b89974ad-e005-3d87-a700-4059401b3661 | -12.9009 | -48.10049 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd49dc29-7166-37d7-ae29-d1da4fed3f50 | -9.62789 | -47.04251 | 2025-09-03 05:14:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bd2f3189-b352-3f77-a8bb-0a9812de628a | -14.31132 | -53.08873 | 2025-09-03 05:14:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da696aaf-f44f-3c0b-a546-f0c5a8bec229 | -6.75506 | -56.39425 | 2025-09-03 05:14:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdbcb7ee-8fd0-34c7-bf41-ed15f6c9b113 | -13.72588 | -46.93712 | 2025-09-03 05:14:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3bcb484c-bff7-37ce-a5b1-23ab6d1c97a1 | -8.37106 | -48.30563 | 2025-09-03 05:14:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 879b7c61-ea6e-3fd8-9a65-ff2718740492 | -11.20917 | -55.07218 | 2025-09-03 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 682700f9-41c4-3147-949d-317011be34c1 | -14.78605 | -48.16099 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffad1601-9354-3183-8fc6-5bba860cc7c9 | -9.78983 | -49.98007 | 2025-09-03 05:14:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4562c960-8f10-345b-82af-a301f29b3c8f | -13.45239 | -46.92405 | 2025-09-03 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a28dffd-c4aa-3a29-9b1d-42b71a3d3218 | -8.81371 | -47.80772 | 2025-09-03 05:14:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 72295688-6421-3bd3-ab75-fd42f49afcc7 | -9.62867 | -47.04398 | 2025-09-03 05:14:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f5947212-7682-32a6-9378-65df2072674c | -9.63185 | -47.86672 | 2025-09-03 05:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6b51c474-3ceb-349e-a081-49c4b678ffa0 | -8.88049 | -45.83296 | 2025-09-03 05:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README87.md)
