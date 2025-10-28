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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 604359bb-686b-3897-b528-cb37f782f1ed | -4.96287 | -47.58878 | 2025-10-28 05:01:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 078bf2b9-2eb5-3668-a324-f7c8f7ebee36 | -3.05025 | -53.01714 | 2025-10-28 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19c2aeae-ffce-3014-968f-68891f451553 | -6.68567 | -42.05243 | 2025-10-28 05:01:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 7d89c2c6-6f40-3031-a93a-47fa3cebcdaa | -1.50122 | -53.12344 | 2025-10-28 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c6d40e2-ecdb-3dad-bda3-9a478d2b4ddc | 0.99038 | -51.29147 | 2025-10-28 05:01:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6b290ae3-f4a6-39d1-b81a-4fedae9a1294 | -3.23366 | -50.05228 | 2025-10-28 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75320c33-9154-3428-9df7-0717985c49e4 | -4.45464 | -43.64154 | 2025-10-28 05:01:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 036d1476-0ddc-3872-92f1-ef8710c22964 | -2.7634 | -48.57829 | 2025-10-28 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 540b47f8-cdcb-38eb-a8a5-fb7a0fa6c4da | -6.4793 | -42.23046 | 2025-10-28 05:01:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| cbc6094b-bd74-3804-993e-18a53bc37736 | -2.76396 | -48.57733 | 2025-10-28 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1de7bc7c-905d-301a-af0e-8344c13b6800 | -1.49728 | -53.1265 | 2025-10-28 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac18a5a3-66b6-3400-8f41-cba8a0579ead | -3.33785 | -52.83454 | 2025-10-28 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72de6c7c-23ed-3847-8c78-eb97913bc033 | -2.7521 | -45.41404 | 2025-10-28 05:01:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49ef5880-eeb0-34c8-b098-48cc9c2d602f | -5.70156 | -49.20002 | 2025-10-28 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3af80dbd-9a3d-3f73-bd73-9de042eece8c | -3.14572 | -53.14452 | 2025-10-28 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b48952a-b236-3dad-b4ec-b9aa41d00b82 | -2.97555 | -51.03176 | 2025-10-28 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38fadb0b-98e9-3071-86ea-62d1c9920964 | -1.51129 | -53.14695 | 2025-10-28 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09788ae6-2812-3d65-b8c7-ec1d80770753 | -3.02947 | -45.37148 | 2025-10-28 05:01:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 4d13a2a6-03f4-388b-975d-9633f72f225f | -2.6388 | -47.30192 | 2025-10-28 05:01:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b203211-b0fd-3165-a60a-91351fa0ef9f | -4.7219 | -46.81359 | 2025-10-28 05:01:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17b171fe-7960-32be-bd5f-78d9b6b0d4af | -1.69878 | -53.6993 | 2025-10-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5f8c822-1634-31c9-9cd0-f8eb26ae3386 | -3.70296 | -47.64789 | 2025-10-28 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 63117149-6ec8-309b-bb23-1eada7af914c | -6.09785 | -44.68594 | 2025-10-28 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 30006f66-c189-3b3b-bb4a-c531783619c2 | -2.95033 | -49.3505 | 2025-10-28 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1804dfc8-37ae-3a1f-93c1-647661d26077 | 1.62867 | -55.69415 | 2025-10-28 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02272ea3-9644-39ec-afef-294b5175476b | -3.10986 | -51.21084 | 2025-10-28 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1a95090-edac-324b-90e1-df4ccbb01ceb | -3.52797 | -51.57361 | 2025-10-28 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9aacee07-3a16-3b0d-a03c-ce1ebbf8248d | 1.20224 | -51.07188 | 2025-10-28 05:01:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4a68690-ee4c-3f31-97af-dd2e5ffd44f0 | -3.14707 | -53.14029 | 2025-10-28 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b12ce13-ec7e-3aae-bb6d-82cdb53c7375 | -3.93175 | -56.06327 | 2025-10-28 05:01:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 168d1a54-f9d6-38ee-8f0c-8bfee7b57181 | -4.41923 | -55.38835 | 2025-10-28 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5bbf5347-52dc-3a11-8ac7-b16767b0f5a2 | -3.69731 | -49.56628 | 2025-10-28 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb3009ac-f075-3d65-86fc-84ca13312ac0 | -5.83919 | -47.56281 | 2025-10-28 05:01:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5f27f300-51e0-38d7-bcc0-46c995d7d8b9 | -3.53332 | -53.31121 | 2025-10-28 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d11062b6-4f32-3e57-b189-c3547877685c | -4.20088 | -48.36204 | 2025-10-28 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6512ca9c-3a37-3111-95f9-96f0a477f070 | -3.22498 | -48.77013 | 2025-10-28 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ee3d43e-d9f8-31aa-a478-737c0be6af89 | -1.69988 | -53.69232 | 2025-10-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b57b2f8-0f05-303e-9e2a-de163feb8611 | -6.16856 | -46.09778 | 2025-10-28 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8029f72c-5566-3c6b-9549-7dc11d61252e | -2.75368 | -45.40351 | 2025-10-28 05:01:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b65c99be-fd70-300d-81f7-9dd364b84bdf | -5.61388 | -47.10932 | 2025-10-28 05:01:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b95b4f3-1f9a-3b6c-ab25-3f5d92442dc3 | 1.59013 | -55.74148 | 2025-10-28 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ba2f799-51eb-3424-b0dd-c4b52aa77d21 | -3.02844 | -45.37438 | 2025-10-28 05:01:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 57888844-730b-3902-95ce-d707cf1423a5 | -3.02351 | -45.36993 | 2025-10-28 05:01:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 25.6 |
| c4e09fe3-0353-38ab-a030-cf3351f976e4 | -4.75778 | -46.42418 | 2025-10-28 05:01:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed85affe-80e8-3749-879e-552e0fa2d465 | -3.06291 | -53.16169 | 2025-10-28 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3fd0693-7777-3063-bdda-1e819bdc595c | -5.36464 | -50.56858 | 2025-10-28 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2900614-1d9d-3f92-b1de-728f6e3bd143 | -2.75997 | -47.75652 | 2025-10-28 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ca3d780-3fae-3ff9-998b-2fe063138e53 | -3.1465 | -53.14399 | 2025-10-28 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4954541-9ce6-37b7-b0cb-99cd376e47fe | -5.46927 | -47.26129 | 2025-10-28 05:01:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4169219f-d59c-30fb-a451-fb118f75d7e6 | 1.59238 | -55.7336 | 2025-10-28 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f255ba1-378f-3892-a607-6908ca131670 | -1.70376 | -53.68935 | 2025-10-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0bf6d3a2-50bb-36f2-b937-126bed38e91a | 1.71019 | -54.99463 | 2025-10-28 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2bba5931-a629-3806-aa6f-bab3288ff1f7 | -3.57073 | -49.01972 | 2025-10-28 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c664a3f-d8c8-3a5b-aebe-adcc8a4195d5 | -3.58166 | -43.63302 | 2025-10-28 05:01:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dbc0b7d5-dce5-3470-a9ea-0b703048028d | -5.84758 | -46.4481 | 2025-10-28 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e6b4ca2-b89e-37f9-9512-9a9fda9c0255 | -3.42879 | -54.53795 | 2025-10-28 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6adcd74f-7a3b-3edb-a452-2c5ffcbf54b8 | -5.63346 | -47.61578 | 2025-10-28 05:01:00 | NOAA-20 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 08bd01a6-b824-3129-83d5-2306da7cd0a8 | 3.13791 | -61.01021 | 2025-10-28 05:01:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4bde600-c2ea-3a40-9477-81ecec70f701 | -5.56583 | -51.01414 | 2025-10-28 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2adb6349-03b1-30e9-9672-212d6ac73d86 | -3.95981 | -53.70517 | 2025-10-28 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 01c70003-e75b-38ad-8cfa-910cb2ffa357 | -1.55349 | -55.41802 | 2025-10-28 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e698bf6-9258-30a2-ad30-0cfa40527fb1 | -3.08587 | -44.44975 | 2025-10-28 05:01:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b150477f-0de4-3e26-b7b4-17a3a93daa2e | -3.707 | -47.6534 | 2025-10-28 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6935bfd0-6792-33d0-b07f-6f9350933fa0 | -3.12632 | -50.15225 | 2025-10-28 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0c19fa6-de12-3f12-8683-e231b5770b6a | -2.58303 | -48.40344 | 2025-10-28 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3412f9c-c665-342e-854d-6bd64711bd40 | -1.75636 | -54.77843 | 2025-10-28 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49cc4739-0a31-33c5-89a4-6e1169b9c82c | -4.26601 | -48.70037 | 2025-10-28 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa8f4102-4f7e-3610-9424-a7f1d5da8e22 | -2.58344 | -48.40464 | 2025-10-28 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c2950e8-bc83-39e0-a709-bd73f21bcf19 | -3.52731 | -51.57791 | 2025-10-28 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b710ea5-3659-3c09-a0c8-66b9ba757fc5 | -1.50459 | -53.12394 | 2025-10-28 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 924725e8-a325-369d-8ecb-3dfc7cacfbfd | -4.5179 | -44.03836 | 2025-10-28 05:01:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 98312d41-891f-392d-86e9-4104492ac74c | -2.793 | -54.86422 | 2025-10-28 05:01:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 791cecfb-58dc-30e1-ba33-a22c44c2477f | -5.65069 | -47.63515 | 2025-10-28 05:01:00 | NOAA-20 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0ff8403b-9294-3604-84b2-9ccc18d8434a | -3.15063 | -50.33381 | 2025-10-28 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5100e528-6ede-3333-968c-84efad0660e4 | -3.57974 | -43.6031 | 2025-10-28 05:01:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b3581e5-3c7e-3ab0-8828-4d4ec8485ffd | -2.72031 | -49.16042 | 2025-10-28 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4122d6c3-aee6-30d3-a1e2-ada8dc0dc697 | -3.44171 | -41.85129 | 2025-10-28 05:01:00 | NOAA-20 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 45c17b65-cde0-36f9-91c9-ccc6fae6b62c | -1.78186 | -55.54334 | 2025-10-28 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9dc69967-a7ca-3811-9590-7be0aa0da2aa | -1.49335 | -53.12955 | 2025-10-28 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7705afc9-700f-3ea6-86e3-ebce97b7fee9 | -4.18545 | -46.23047 | 2025-10-28 05:01:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35fc922e-e4af-360e-b096-9348b92a9f67 | -6.10449 | -44.68223 | 2025-10-28 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3bb77097-888b-3731-b20a-d05f60d5e094 | -3.59077 | -43.61429 | 2025-10-28 05:01:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa14b521-39da-3995-9522-4feb25ba37c1 | -4.75255 | -46.42329 | 2025-10-28 05:01:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8238898c-c993-34b6-b161-647cc1ecbd02 | -3.09695 | -57.22849 | 2025-10-28 05:01:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af1dae99-194d-38c8-81d1-512e74c6fef3 | -5.43966 | -47.39775 | 2025-10-28 05:01:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ed8099da-2f93-35cc-b6ad-3235a0fe0302 | -1.67221 | -51.99693 | 2025-10-28 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e2cc4a47-5955-3acf-bae4-4330929e3eb2 | -3.59148 | -43.60949 | 2025-10-28 05:01:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71785d58-ed78-381c-8b04-97e6ba820db5 | -2.41978 | -48.44334 | 2025-10-28 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8906eac0-92f7-3379-9b71-fc629a505695 | -1.41494 | -52.67167 | 2025-10-28 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fa9c206-5216-3abe-bfae-53cec8e067a0 | -2.82342 | -57.14445 | 2025-10-28 05:01:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f35dd7b-282e-3219-af55-c4afe3de9d43 | -4.87283 | -47.54947 | 2025-10-28 05:01:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a860cba9-f168-36a6-b81d-7cbac9fb7f26 | -3.57257 | -51.33076 | 2025-10-28 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14ca54f3-5091-3b01-83a3-4d6f2f5f92ed | 1.6315 | -55.68995 | 2025-10-28 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 765d2d1b-3c87-30f6-906a-3dac2adfe96d | -2.14424 | -56.71647 | 2025-10-28 05:01:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 744a9a74-9748-3b67-bb25-8c1995f04b2f | -4.96409 | -47.59299 | 2025-10-28 05:01:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a77c0665-4620-3ec8-89e6-ab50829f6338 | -2.74666 | -45.41317 | 2025-10-28 05:01:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d9fb3d5d-92ec-33aa-8ff0-da3c12dd36f8 | -3.53099 | -52.96725 | 2025-10-28 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6991acfb-537f-35e4-8f77-6e41a3a2d3b3 | -6.13847 | -44.58482 | 2025-10-28 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 361751b2-1403-3f89-8699-bfc19620d3e1 | -4.90516 | -47.41671 | 2025-10-28 05:01:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62fd7176-557b-3e5e-a7df-cd2cb9684b0c | -3.08648 | -44.44559 | 2025-10-28 05:01:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README74.md)
