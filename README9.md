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
| dcb355d2-b1ad-3a4d-b08f-092a17f0f9ca | -7.23154 | -43.10583 | 2025-06-14 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8c2ce968-f7c2-3971-8f18-df4ff0d613c3 | -8.39633 | -46.9253 | 2025-06-14 03:49:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32ef0494-2090-35bb-ae3b-efdccfb6b9c9 | -7.45065 | -45.50916 | 2025-06-14 03:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f77fdce0-a913-3192-99d6-e305e87f78c2 | -7.45384 | -45.50417 | 2025-06-14 03:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0fc804a2-2182-3222-b07e-8a7e2f1b7453 | -6.95692 | -42.8065 | 2025-06-14 03:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 30134647-156c-38af-a224-d9e2246f117b | -5.9036 | -43.4498 | 2025-06-14 03:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 392d57d3-cc70-3a24-9e42-740b301c3d6e | -7.2254 | -43.58833 | 2025-06-14 03:49:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 94037c8f-81be-3383-b4e2-b1d1e5ac74a8 | -7.39346 | -43.39414 | 2025-06-14 03:49:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9587a2fd-ea66-3390-a485-950be8fdaf8d | -6.95309 | -42.89241 | 2025-06-14 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 31.8 |
| d8a1e57a-7f2b-361e-9002-38dc9b711229 | -4.82339 | -44.35625 | 2025-06-14 03:49:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f75743cb-79ea-3d03-a9aa-451db85afd72 | -8.42842 | -49.56339 | 2025-06-14 03:49:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1f6ff744-eb3e-3f64-ab89-fae987b22437 | -6.95167 | -42.90063 | 2025-06-14 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 35.3 |
| 7ccd742e-8f7b-31de-9092-73afff2a0fdc | -7.39787 | -43.3949 | 2025-06-14 03:49:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a7e5d0b1-8434-3142-9cae-92340186d095 | -7.68021 | -43.65326 | 2025-06-14 03:49:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49e8527e-2652-313e-b8e0-3d4b9974b752 | -7.46138 | -45.50792 | 2025-06-14 03:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 06fb8997-67cb-37f7-a654-4233dfa0e520 | -5.45182 | -44.81571 | 2025-06-14 03:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5d38ec71-562a-35be-ae3f-8f365e3b58e3 | -6.94711 | -42.89201 | 2025-06-14 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 914b6686-2368-3bd6-b766-863f73947dea | -5.77927 | -43.6268 | 2025-06-14 03:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b181e52-ef8a-3821-95db-c9d792602c68 | -6.60328 | -43.90555 | 2025-06-14 03:49:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ab7cfae2-e45c-30a4-9cfa-2688830d77d9 | -7.07235 | -43.55435 | 2025-06-14 03:49:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f5c19c0a-5dd4-3d73-86de-2b6c7d8f99dd | -5.77222 | -43.47592 | 2025-06-14 03:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00e5eddd-7b64-3d71-9665-cf515d6795c7 | -9.36591 | -40.41537 | 2025-06-14 03:49:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 569ff43e-5109-3a87-b4c0-34518af188f8 | -9.36301 | -40.41067 | 2025-06-14 03:49:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| f00d7234-9b20-32ce-a3ad-cb04b7bea8f1 | -7.6319 | -43.62877 | 2025-06-14 03:49:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 746ab3e7-dde3-3bd5-975d-1a29ff902b5f | -6.60114 | -43.8903 | 2025-06-14 03:49:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f2f09c10-e962-3029-94bb-28ab4bbff646 | -7.63761 | -43.67594 | 2025-06-14 03:49:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8ad341c-a3c6-36ea-836e-7068c9cb897a | -5.07033 | -37.71572 | 2025-06-14 03:49:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 06c4c72b-1d85-3b8c-9ed7-ceb4ad3e9345 | -7.63683 | -43.68049 | 2025-06-14 03:49:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 687f1762-1042-3adf-b79f-7d38cd25d119 | -7.23949 | -43.11148 | 2025-06-14 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 162e4417-d170-3efe-8ddf-be7587f4ce92 | -7.22103 | -43.10962 | 2025-06-14 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e723d66e-7207-3e7c-8943-95071e4297df | -6.94808 | -42.89579 | 2025-06-14 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 8e24f7b1-0992-3433-b630-edbc049ee08f | -7.22912 | -43.59358 | 2025-06-14 03:49:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3de8e441-9c78-39d9-b758-8673749525b9 | -9.36659 | -40.41127 | 2025-06-14 03:49:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 2974ef19-ba0a-3100-9cab-2cc4fdf07d06 | -6.56445 | -43.42435 | 2025-06-14 03:49:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e2899212-6ac4-32d5-abe4-879a32509d81 | -7.11093 | -43.43782 | 2025-06-14 03:49:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ca3fae2a-33cc-3421-a76d-1a71e828b380 | -5.88953 | -44.35461 | 2025-06-14 03:49:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4dda0c26-b9aa-31e8-9266-5f45e5ccc7a8 | -7.22988 | -43.58909 | 2025-06-14 03:49:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| abaabaf7-3e36-3f1a-86ee-ef2a70c80e67 | -6.67964 | -43.76341 | 2025-06-14 03:49:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 664c642b-404d-3b7f-8725-29b41e2e3dfb | -7.45893 | -45.50506 | 2025-06-14 03:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| be49f414-7431-3739-8dad-034de7919e1f | -7.22173 | -43.10546 | 2025-06-14 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a1655174-366c-3458-a9cf-183ecdfd031b | -5.9028 | -43.45441 | 2025-06-14 03:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 67d29b1d-167e-34cb-aafc-bcd917d66e7e | -7.63714 | -43.62505 | 2025-06-14 03:49:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1fa3bb7e-280e-3981-a445-dfb756407216 | -5.77203 | -43.47884 | 2025-06-14 03:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53221841-bcea-35e9-802d-b6192ea2cc86 | -8.07986 | -43.11264 | 2025-06-14 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 38.5 |
| a0fd2df6-2b21-3ea1-99d1-e689553c2a40 | -7.45173 | -45.50322 | 2025-06-14 03:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9a898ccb-f51c-3503-9057-46aa6b7b5e09 | -8.07131 | -43.11109 | 2025-06-14 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 73fb15cc-b465-39fc-934b-2678dd0a1b18 | -7.17486 | -43.53385 | 2025-06-14 03:49:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 581e23e8-b03b-314d-92cf-3fe7ce532e8c | -7.45119 | -45.50618 | 2025-06-14 03:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a6e0d7fc-d667-3888-8c7c-7d4d0c218682 | -7.2318 | -43.09865 | 2025-06-14 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 682c6433-4524-354b-b64c-afc1fc7fc691 | -6.33642 | -43.7432 | 2025-06-14 03:49:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e10da9fc-b95a-334f-96c5-21db85a258bc | -7.23111 | -43.10277 | 2025-06-14 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 39316e64-8b10-3c04-b2e8-92617429c234 | -6.21808 | -43.33183 | 2025-06-14 03:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c659a626-6f4e-3bfb-9b42-08c53c09fc80 | -6.21436 | -43.32649 | 2025-06-14 03:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 14633c9f-1b1f-3f5b-a74a-c49f4622c0c0 | -7.18518 | -39.29417 | 2025-06-14 03:49:00 | NPP-375D | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7a5db5a2-5120-3b8c-9891-92e5873c2199 | -6.9612 | -42.8072 | 2025-06-14 03:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 9a4853e2-6555-3734-8649-3c45df9e12bf | -7.07683 | -43.55516 | 2025-06-14 03:49:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb411e24-5c41-37eb-aa4a-99c87c1de3c4 | -7.4579 | -45.51099 | 2025-06-14 03:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e1184daa-b3c6-3266-8eeb-50a6d17c267e | -8.42909 | -49.56199 | 2025-06-14 03:49:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cb1df48c-8eb4-3de7-bd41-204568b518b4 | -7.45944 | -45.50212 | 2025-06-14 03:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a734de6-aca2-3f33-a9b5-03a16fc0496c | -6.60576 | -43.89116 | 2025-06-14 03:49:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| fc7b684d-82e6-3143-8c39-9096f23d3761 | -7.23731 | -43.09838 | 2025-06-14 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8bf72536-15c2-3553-8380-54de920347b9 | -6.91638 | -38.55873 | 2025-06-14 03:49:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4ffcebd5-4060-3b69-aee6-e3480c89d1c0 | -7.45842 | -45.50802 | 2025-06-14 03:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7b8e030e-172f-3dac-a370-a9c07d0080f5 | -7.2272 | -43.10509 | 2025-06-14 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c18303bb-5374-33f5-8079-ed287decc96e | -7.23298 | -43.09761 | 2025-06-14 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 07e669b6-9097-39c1-9907-bde19aa81ef2 | -6.94644 | -42.8961 | 2025-06-14 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fdc22c6a-f782-37fb-a7c3-9d86fc026250 | -7.23042 | -43.1069 | 2025-06-14 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 46a8d157-6b85-3694-965b-14d7a9d57f60 | -7.22286 | -43.10438 | 2025-06-14 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8450cb6e-fdfb-3c48-a2be-3cf88f1df7b3 | -5.91562 | -43.46144 | 2025-06-14 03:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 34b0b40d-1bfb-3c04-955f-eaf26d2efcf9 | -7.18517 | -43.554 | 2025-06-14 03:49:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b0c2d128-25cc-3422-857a-c1d7e442a15b | -7.45332 | -45.50714 | 2025-06-14 03:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fd281395-79d6-3710-a711-4e54767a917c | -6.60954 | -43.89686 | 2025-06-14 03:49:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d3504108-ab47-3574-b6b5-9a514f811fe0 | -6.59951 | -43.89977 | 2025-06-14 03:49:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8986fc52-681c-3f4b-a2fc-8d5455205791 | -3.77398 | -41.60672 | 2025-06-14 03:49:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a609f201-d61f-3c69-aebd-5d5f7f8aabe0 | -7.4318 | -45.42085 | 2025-06-14 03:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba735801-48d2-35bd-8faf-349271082a00 | -7.4528 | -45.51012 | 2025-06-14 03:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d5506360-8cfd-3358-967f-f6bb8bc8f296 | -6.95239 | -42.8965 | 2025-06-14 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 35.3 |
| 85c1bb34-bb78-3ef9-a59c-296d4fe572f0 | -6.94412 | -42.80419 | 2025-06-14 03:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2516c9e7-30e9-32c1-bd6c-4e4800a0b948 | -7.45682 | -45.50408 | 2025-06-14 03:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ccec9e85-fd1b-35c0-bf71-7c1d2fdd7c46 | -7.46084 | -45.51087 | 2025-06-14 03:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2172185-5c56-39b5-adf7-6f7c261ca430 | -8.20844 | -42.83916 | 2025-06-14 03:49:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b7b983fe-83bc-35e7-9e23-425ccf74ac13 | -6.94838 | -42.80499 | 2025-06-14 03:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9f656c37-c52f-3f12-ac42-8b4d4f629444 | -5.88472 | -44.35366 | 2025-06-14 03:49:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b04397ea-24e2-3cce-b218-3df6c5d162cb | -8.39562 | -46.92432 | 2025-06-14 03:49:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfacaebe-cfdf-3977-80d7-5e16a0e43a31 | -7.45435 | -45.50122 | 2025-06-14 03:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 74f9cab3-25b8-305c-985f-9e1eecffc851 | -3.76983 | -41.60605 | 2025-06-14 03:49:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4ad3a400-42b0-34d6-8284-e634f926a792 | -7.43232 | -45.4179 | 2025-06-14 03:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78cebc8c-900b-39b7-9c54-b56dfc81a63f | -13.9062 | -54.6084 | 2025-06-14 03:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| d7f833cd-8222-3bb4-8632-9fb78a5f769b | -6.9605 | -42.8816 | 2025-06-14 03:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.3 |
| 6ac5166b-10b3-3093-9c0a-c540a04a5b26 | -14.2121 | -57.4098 | 2025-06-14 03:50:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 9d789d39-6c01-3f61-b403-f441fd64d5b7 | -6.9602 | -42.9052 | 2025-06-14 03:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| 9cf9ab8b-3d4e-3193-bf17-93e4d6a81f32 | -13.887 | -54.6106 | 2025-06-14 03:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| ca6700de-90d5-355f-adc0-01490304769c | -10.9355 | -56.8322 | 2025-06-14 03:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| e86d6b7b-0583-32ea-a44d-ce70be7cca42 | -12.68876 | -52.40238 | 2025-06-14 03:51:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9ffd604c-4f0b-3a50-97b9-6058410b3458 | -9.40572 | -50.42251 | 2025-06-14 03:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5afa750c-8b47-3a62-8fe5-c9994719796b | -15.38206 | -47.86389 | 2025-06-14 03:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5052bd75-3657-35ac-a202-a32d92684774 | -15.39692 | -47.87013 | 2025-06-14 03:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f966e217-dfee-368e-a0b7-3dc6531649f7 | -12.11165 | -48.87669 | 2025-06-14 03:51:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a859673e-cc0f-3c30-a621-e7e76d1bffa3 | -10.97779 | -42.18103 | 2025-06-14 03:51:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| ea7ac16c-d2e6-3a56-8f8f-7ace1b65504a | -10.85625 | -46.6986 | 2025-06-14 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README10.md)
