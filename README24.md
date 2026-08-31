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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ad52011-b28f-3254-b400-a9af172bc5eb | -5.2548 | -55.8907 | 2026-08-31 04:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 3fcf1d09-2720-3a72-99dd-42cd6fd73d36 | -7.3118 | -60.5897 | 2026-08-31 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| b96e2d43-ac74-31d9-a5c3-a4dce1190c0c | 2.52175 | -50.85542 | 2026-08-31 04:10:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 658438a4-8870-367f-9f67-d276d3edec77 | 2.51565 | -50.85638 | 2026-08-31 04:10:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8919467-55a8-362e-a6a5-ad470c68ffd3 | -4.37584 | -39.55703 | 2026-08-31 04:12:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 522f39e9-69ca-3d60-bc62-7585cbeb2b0a | -3.45909 | -51.89308 | 2026-08-31 04:12:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0bda9002-6a95-340e-81d7-baf54b965a44 | -3.4015 | -43.26949 | 2026-08-31 04:12:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 78ee8e0b-7603-3993-9c9d-bbb96c3cc7aa | -1.5968 | -54.40743 | 2026-08-31 04:12:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b8dc59d-9f62-3402-872c-c341fcaf4fae | -3.23 | -46.37294 | 2026-08-31 04:12:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3712a9ba-b4ea-3ca9-8c1a-c7e024a4f5b3 | -4.74322 | -41.10723 | 2026-08-31 04:12:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0c892c3d-69c7-31eb-a9c3-70a960411034 | -1.5865 | -54.40389 | 2026-08-31 04:12:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 567701ea-81e1-3af5-a87e-fbde76e64a6e | -3.68648 | -51.99748 | 2026-08-31 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed7a4bee-9699-30f0-bd9e-83854320db31 | -1.59562 | -54.41442 | 2026-08-31 04:12:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b563692-beae-36d2-a203-df4ed5e1d175 | -3.4161 | -43.37735 | 2026-08-31 04:12:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6b5fdd1b-bbd6-3d16-9017-35eb33960e29 | -1.58536 | -54.41095 | 2026-08-31 04:12:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bfab52e0-be31-3735-aee8-dff038023acf | -3.86207 | -49.11349 | 2026-08-31 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 946d99f7-29a7-391d-92e8-d8399685c963 | -3.40434 | -43.27383 | 2026-08-31 04:12:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a8c1d05-4d9a-3b83-8651-7518f66de802 | 1.10384 | -50.97598 | 2026-08-31 04:12:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c760a913-8d90-324a-a630-48234bbe9a09 | -1.60267 | -54.41605 | 2026-08-31 04:12:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 82bbd5c4-426c-3ab8-bd4b-09d48ea958e0 | -4.12349 | -43.25365 | 2026-08-31 04:12:00 | NOAA-20 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f416d591-c097-32dc-9304-97276f92bcd4 | -5.19166 | -35.84541 | 2026-08-31 04:12:00 | NOAA-20 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e3b908b0-c64a-3d6d-823c-59feb353fd40 | -3.4046 | -50.1264 | 2026-08-31 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5afc8a30-731f-3fb8-8151-3d58020e9c57 | -4.06139 | -48.95893 | 2026-08-31 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e6eee22d-a2f3-3935-a402-19fe1fba836e | -3.53999 | -49.47285 | 2026-08-31 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e917eef4-b889-3930-a646-79ee4f2e1fc7 | -1.58857 | -54.41282 | 2026-08-31 04:12:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| ff6ebc53-b2f0-3a81-a64e-966c329be927 | -3.40915 | -43.37624 | 2026-08-31 04:12:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10786ff5-aead-3eeb-8649-176c565a01f9 | -3.41672 | -43.37352 | 2026-08-31 04:12:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3437cf49-daec-3de3-b9d1-91b9b428e289 | -3.68575 | -52.00186 | 2026-08-31 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ad32449-b1e0-39a2-bc0b-a5b0a219f60c | -3.86303 | -49.10785 | 2026-08-31 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 99ac1c3d-7560-3b65-a3bc-a270fd841609 | -2.09712 | -48.21982 | 2026-08-31 04:12:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79a66767-a153-3dc3-b456-599098c80cec | -4.0814 | -45.94138 | 2026-08-31 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1175367-77ea-3086-ab37-e358263d0656 | -3.22649 | -46.36855 | 2026-08-31 04:12:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e29eb29-445d-39f8-a6e4-016c3412efe0 | -3.53492 | -49.47196 | 2026-08-31 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3f6d0734-fdf3-3ef3-9b2c-401d073d3c78 | -5.1911 | -35.84928 | 2026-08-31 04:12:00 | NOAA-20 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 8575c5c2-b0c5-3e70-9a73-c2a5785adee1 | -2.4725 | -49.41412 | 2026-08-31 04:12:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 852c0f9d-3e3d-3085-81bb-d0d9ac6c2a57 | -4.98966 | -41.82478 | 2026-08-31 04:12:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8fa8bffd-75ff-31b5-9e46-2a945d39d219 | -4.13575 | -40.84546 | 2026-08-31 04:12:00 | NOAA-20 | SÃO BENEDITO | CEARÁ | Brasil | 2312304 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6e671427-9666-381f-b41b-4e591676e8e3 | -3.46221 | -51.89279 | 2026-08-31 04:12:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 231dd2d2-c158-349d-b9ca-c6548080cd6d | -3.46504 | -51.89414 | 2026-08-31 04:12:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87f0159c-ec7f-352c-b50a-a0e98fd183ad | -3.05842 | -40.8481 | 2026-08-31 04:12:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 52452f46-8037-3a83-8f8d-2c0db81942e0 | -3.46141 | -51.89733 | 2026-08-31 04:12:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7dba1c8f-e215-339b-821e-0f0dcb8540c8 | -3.40991 | -50.12732 | 2026-08-31 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f9c628c-a3d1-32ae-9d69-0910e679d6e0 | 1.10453 | -50.98051 | 2026-08-31 04:12:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1a1bc8cf-b1e3-35c2-8e04-022899e1f8ee | -3.39803 | -43.26894 | 2026-08-31 04:12:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2febf2df-05de-3ef9-9fc3-8b178c6dcee0 | -5.19041 | -35.84651 | 2026-08-31 04:12:00 | NOAA-20 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 1884df44-cc37-3035-9190-76b6f406c358 | -4.08536 | -45.94205 | 2026-08-31 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2061c7a-8597-3c5b-adb1-e1c4c0f35652 | -1.58974 | -54.40584 | 2026-08-31 04:12:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 81525c8c-ec4a-3b6d-a3da-5d20c3bc6f82 | -3.40088 | -43.27328 | 2026-08-31 04:12:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 134304aa-c99c-3f79-8c8e-44a6a9d0ff43 | -10.1473 | -45.76111 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7da5a359-ff17-3543-9e30-c328192d7632 | -8.15143 | -45.47891 | 2026-08-31 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0b35454c-5ab3-39c0-b85f-d8b2d308639f | -6.931 | -55.64001 | 2026-08-31 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0059edbf-b417-32f8-bed2-534ba1b99a4a | -10.05102 | -48.6933 | 2026-08-31 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd1cd7b3-87c3-388a-8ea0-b400e85c9eab | -10.15526 | -45.73517 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a4b0fbe6-ea6c-3dbd-ad60-6091d5d9dd07 | -7.13215 | -44.30877 | 2026-08-31 04:14:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b7f1638-a3cb-301e-b25c-d7a19f2ed4b6 | -11.32891 | -45.1887 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4dd9e46c-3cb1-35f8-8dd8-107b581b59c0 | -10.76346 | -50.8559 | 2026-08-31 04:14:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1ac6e3a5-7c7d-389b-8097-69ba84c71081 | -11.22393 | -45.14457 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 156b607c-5289-3b0f-9925-cdc61e6ce362 | -7.11524 | -42.1957 | 2026-08-31 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ec722934-cf5e-3f58-bf7b-8bc2f8c1ee4a | -7.09596 | -42.8481 | 2026-08-31 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1836f835-053b-3df3-aa06-f4db08c8a157 | -10.15401 | -45.7295 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 75b95a7a-69a0-331c-b59e-e8958a67c5ed | -11.37628 | -45.1723 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| afb1fddf-ce8e-39e3-ac35-eecf1365f2a4 | -11.21762 | -45.13956 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 056063d8-252b-37de-8885-efb2923813d6 | -7.26515 | -45.35413 | 2026-08-31 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96502aed-7344-3e6d-b6f3-3672874335e5 | -5.58667 | -42.32259 | 2026-08-31 04:14:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 34bc005d-b42c-318b-b0bf-7b9cf821293d | -8.61101 | -54.78341 | 2026-08-31 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 961110f6-d4a6-330c-89ac-71e54ce8bee7 | -12.10113 | -45.0363 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6def350-e97b-3cb0-8b2e-e4f8ace8abfe | -9.43641 | -45.688 | 2026-08-31 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0167bde-9502-3082-9462-fa0cf8360c71 | -6.39331 | -45.51197 | 2026-08-31 04:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2b6c4dde-f9c0-320c-9d97-435fda8a3b67 | -7.92074 | -44.25211 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 80c8b347-7b6c-3822-b896-67a2da1ad52a | -10.83673 | -45.3175 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 916c8e53-d282-37f2-bbca-dc66ea073167 | -11.6517 | -46.75525 | 2026-08-31 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b166d08-d53f-3051-9fca-bdd8f7266080 | -7.18975 | -46.56608 | 2026-08-31 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d48fd0d3-03ab-3af2-858a-73a05fd0fbe3 | -7.97267 | -44.30344 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba2d2e23-5eb0-3774-94b8-672e50fd45e1 | -7.97796 | -44.29274 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8acdd7a5-c8bc-3592-aa93-f9c7b47ce870 | -10.13222 | -45.7402 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac871a8b-971a-3131-b495-43d581f5c741 | -10.75854 | -50.85493 | 2026-08-31 04:14:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a4599f1-6265-32f9-94a0-c4f30cbe6dd4 | -7.14891 | -46.16953 | 2026-08-31 04:14:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7b48fb6-1f86-3056-855d-8903282da58e | -8.61162 | -54.77261 | 2026-08-31 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4afc9a49-9069-3842-b479-ccbf96122a90 | -11.20747 | -43.37763 | 2026-08-31 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5e0d29bf-1642-3e95-ac38-bac810cf1e6e | -10.75203 | -44.87267 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 072cfa9d-905f-3cf2-aedc-343169442961 | -10.75483 | -44.87709 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dcd30248-9885-3461-801b-dbd0a3581b81 | -8.72713 | -45.37841 | 2026-08-31 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e06ee4aa-6f84-3de0-b8f1-df4eed908252 | -8.24067 | -49.04422 | 2026-08-31 04:14:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69727d3a-a300-352e-ba6b-07b0552fcb42 | -10.14801 | -45.75684 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a3436aa9-9dc0-3b93-8ce8-00bf80983250 | -7.12101 | -42.84124 | 2026-08-31 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 61802c09-48cd-35eb-8bce-55ba3c843545 | -10.83388 | -45.31293 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8e3b09f1-0e2c-3f0a-ac59-f41054cda91d | -7.13841 | -42.75378 | 2026-08-31 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1152c978-790b-3461-9eda-64d9daeea037 | -11.21079 | -45.09451 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6fa3b86a-0284-3c11-ad17-34df9890d0f4 | -11.24704 | -45.38016 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1db9fe71-5158-3697-b4b4-bd2427a7878b | -11.68504 | -47.60459 | 2026-08-31 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8ade7a3c-9dd2-314f-9274-ffe470544eff | -7.97511 | -44.28842 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf31d2fd-8814-30a1-a894-da40df501d69 | -12.39053 | -46.45196 | 2026-08-31 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5222e89f-100f-3ec2-9bc4-ecc8ae78e968 | -6.8749 | -41.65363 | 2026-08-31 04:14:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c8bc9e6e-0e6d-3e56-9287-eaa94d89165d | -10.15689 | -45.73431 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| be1dd108-1b37-37bb-a349-bbbfede5e03e | -12.13255 | -47.23315 | 2026-08-31 04:14:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0572194a-5c6f-3089-ae23-630037639d1b | -6.39174 | -45.49801 | 2026-08-31 04:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d9f5cca2-365c-3b8f-86a6-20d85cff5d94 | -11.32862 | -45.16878 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8dd1799c-5c06-306b-b927-8ded94d87bc7 | -7.22171 | -42.76383 | 2026-08-31 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 64f2fc77-1fc0-3195-89c5-1976f52e8229 | -6.39547 | -45.49866 | 2026-08-31 04:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9e899a5f-d68f-3838-a7b6-7316bfe578d4 | -7.9242 | -44.25269 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |


[Clique aqui para ver as próximas entradas](README25.md)
