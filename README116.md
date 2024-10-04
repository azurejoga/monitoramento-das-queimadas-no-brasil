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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| afe54b20-caba-3d38-9a75-b65669541926 | -14.16375 | -44.64849 | 2024-10-04 04:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 66d54592-1d19-31c2-bb89-18cbda38584f | -14.16304 | -44.65379 | 2024-10-04 04:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b4875122-5782-318f-b9fb-3bd88d8f5ff5 | -14.1624 | -44.64664 | 2024-10-04 04:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2da5ede-aaf0-32b1-9ddc-6959df0d30a9 | -14.16166 | -44.65193 | 2024-10-04 04:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 342c0eb5-4a18-3f3d-9a60-423b74dbcdea | -14.13469 | -43.70193 | 2024-10-04 04:34:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 218594fe-a1cc-3895-859c-05c9203e1683 | -13.99611 | -44.02687 | 2024-10-04 04:34:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d80e02bd-ba41-3d76-b38d-e8c1a471a337 | -13.99559 | -44.03069 | 2024-10-04 04:34:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c1837843-66ee-36f4-aa08-e74d4e923359 | -13.99507 | -44.03451 | 2024-10-04 04:34:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 76c02b85-213a-343b-88ff-ce38d4fef446 | -13.99196 | -44.02628 | 2024-10-04 04:34:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e1f640d1-dc9f-35e1-9324-4f531c8b668c | -13.99145 | -44.0301 | 2024-10-04 04:34:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 4f3efceb-5b76-3280-8525-73fa12fc6946 | -13.99093 | -44.03392 | 2024-10-04 04:34:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 67531dc2-5a1a-39cd-baf2-ccf77d16ab86 | -13.89534 | -44.2777 | 2024-10-04 04:34:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41a581b4-d541-3df3-ac66-95050ccecbc3 | -13.89485 | -44.28137 | 2024-10-04 04:34:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da1939de-c8e6-371f-8ba2-e5d5b85ae6b2 | -16.1517 | -44.22855 | 2024-10-04 04:34:00 | NPP-375D | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fbc0649a-f5c6-3739-99a4-02588485a87a | -15.86211 | -45.26987 | 2024-10-04 04:34:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b81b100-44be-3173-bc19-7dc9bfd1c43d | -15.85817 | -45.26932 | 2024-10-04 04:34:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9be70ff-35ce-39ce-b92a-38319f69cfe4 | -15.64597 | -45.1623 | 2024-10-04 04:34:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a157961-4b9c-3e24-8bd5-423fb38a17b2 | -17.42085 | -44.94239 | 2024-10-04 04:34:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8a83fe8f-60dc-3003-b9f2-5ec7d14748d2 | -17.41675 | -44.94181 | 2024-10-04 04:34:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa80011b-1e53-317c-bbf7-b6c119aa1720 | -17.41265 | -44.94122 | 2024-10-04 04:34:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 556baf35-baa9-33bf-8982-42eecea45c1e | -17.40905 | -44.93688 | 2024-10-04 04:34:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6641166-7c4f-3c9f-b562-bf95eb5a9670 | -17.40856 | -44.94064 | 2024-10-04 04:34:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5c3ca56-7021-3b73-9be0-bf807968782d | -17.1034 | -44.58681 | 2024-10-04 04:34:00 | NPP-375D | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| caf608b2-6936-3879-b46a-819e5c2d3bbd | -16.97341 | -44.76639 | 2024-10-04 04:34:00 | NPP-375D | IBIAÍ | MINAS GERAIS | Brasil | 3129608 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d683b32c-9de5-351b-aa6e-21b485814dcf | -13.50807 | -48.6046 | 2024-10-04 04:34:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cac79465-a5d6-3f22-887b-4eb5f6b308ad | -13.14543 | -46.31533 | 2024-10-04 04:34:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| dac6d4fd-b588-3add-97f0-e791c2c694b3 | -11.83645 | -46.26724 | 2024-10-04 04:34:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f73bbcaa-fc40-3288-b7fb-cf89205bed09 | -11.8329 | -46.2667 | 2024-10-04 04:34:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2f4e84ac-17a4-3f24-902e-8e84b2e95e7e | -13.1599 | -46.32443 | 2024-10-04 04:34:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3fc3f0c7-569a-3dbd-9657-e8d3b9671db4 | -13.15855 | -46.32587 | 2024-10-04 04:34:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b2e1536f-b54c-3237-88ac-2252e817a10e | -13.15495 | -46.32541 | 2024-10-04 04:34:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d23a1654-7161-3996-a465-c574454f6faa | -13.15315 | -46.31273 | 2024-10-04 04:34:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 07a551c4-5e2d-3439-bf80-d26a2343af44 | -13.15255 | -46.31678 | 2024-10-04 04:34:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3845cce0-a884-3f85-9d6a-5be730068644 | -13.15196 | -46.32082 | 2024-10-04 04:34:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2109cb84-7eb4-3f75-88c9-f94cd609a2c1 | -13.15137 | -46.32483 | 2024-10-04 04:34:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 91df8340-9f36-3d84-b3e8-3910ef8e0428 | -13.14959 | -46.312 | 2024-10-04 04:34:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 07785c16-4d9f-30f0-a327-557db4fbce5d | -13.14899 | -46.31604 | 2024-10-04 04:34:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 35f3315e-ac9f-339f-ade2-db57351cb6d3 | -13.1466 | -46.30733 | 2024-10-04 04:34:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e7c8f593-e638-32f0-bbb5-1d627e6d94f9 | -13.14602 | -46.31129 | 2024-10-04 04:34:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7bb20800-0d83-3ae2-9ca0-eceb5683959e | -13.14419 | -46.29873 | 2024-10-04 04:34:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| efe3a0b8-83c9-3595-8cfe-cac6b63e979d | -13.1436 | -46.30276 | 2024-10-04 04:34:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6e453f83-5386-38c3-94eb-3581011d4f89 | -13.1406 | -46.29821 | 2024-10-04 04:34:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ad1c001e-bf3b-304b-af73-de2c725d6dd5 | -13.14001 | -46.3022 | 2024-10-04 04:34:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0594cfab-0b06-30a9-97f9-1139ae0a0e4d | -13.13641 | -46.3017 | 2024-10-04 04:34:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b083a0d6-7aba-31fb-9e2c-2f09a4201e4f | -13.13583 | -46.30571 | 2024-10-04 04:34:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| b3b5f18a-b00f-3b4d-a3df-e22e7c6ae108 | -13.13281 | -46.30127 | 2024-10-04 04:34:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8d214e47-ae41-3a9d-b58c-8904dcef844b | -13.13221 | -46.30532 | 2024-10-04 04:34:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 69bfd57c-5ba6-3124-9760-a08abd835312 | -13.1286 | -46.30492 | 2024-10-04 04:34:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 06c1fae6-fef5-3682-aa72-037015ce1f7e | -13.12801 | -46.30894 | 2024-10-04 04:34:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 715ff3e5-55aa-3da8-a013-92318c26e421 | -13.12742 | -46.31299 | 2024-10-04 04:34:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a60e8d41-b1a4-3ee4-b80b-f744d6a3208a | -13.12379 | -46.31269 | 2024-10-04 04:34:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e176e0e5-70d9-30a7-8c2f-7f34b9f36af3 | -12.2682 | -45.96293 | 2024-10-04 04:34:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53a6a4d1-0b6c-324c-aac2-b6f16a94eaca | -12.26759 | -45.96714 | 2024-10-04 04:34:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2df0ee18-344b-359e-bfaa-7bed49f864b5 | -13.16938 | -45.43555 | 2024-10-04 04:34:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2cb183d6-94ca-3a15-bf52-0673d233618b | -13.16496 | -45.43962 | 2024-10-04 04:34:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b37a9626-e0c4-30c0-953d-e46a21c15e04 | -12.89899 | -45.65852 | 2024-10-04 04:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af27afdd-fb46-3c5e-a11f-8fca317c66c1 | -12.89529 | -45.65796 | 2024-10-04 04:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 64ead9a4-f3ee-39a8-86dd-e51b2c1ebe2b | -14.04032 | -45.47753 | 2024-10-04 04:34:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 137c566f-25c3-3236-ae8a-9df77298a186 | -14.03964 | -45.48224 | 2024-10-04 04:34:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a4de66a3-99a4-3f34-94f1-70892e273b92 | -14.03931 | -45.47965 | 2024-10-04 04:34:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 958ce9bc-9dd6-331d-b079-fbbed8492546 | -14.03866 | -45.48438 | 2024-10-04 04:34:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| aeb550a5-7b55-3f57-8995-328542baadce | -14.03476 | -45.46228 | 2024-10-04 04:34:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 76e8b8d4-2323-3763-bf3b-e2f81b6e45a0 | -14.03366 | -45.46437 | 2024-10-04 04:34:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2ab87774-740a-327c-a9dc-f0ccf7c6fea9 | -14.01997 | -45.48441 | 2024-10-04 04:34:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dc87bc7a-5197-3bd1-85d3-73782c3298a4 | -14.20499 | -46.4685 | 2024-10-04 04:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 14c0881d-cd5b-3b81-b2c4-d6bfdbd085f5 | -14.20198 | -46.46384 | 2024-10-04 04:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1c10830-11d2-32f0-a1e2-d1394ab246d1 | -14.20138 | -46.46801 | 2024-10-04 04:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 42268a98-3bcc-375c-b17c-e48335aef0ed | -14.20076 | -46.47219 | 2024-10-04 04:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 017c935a-6f6d-36af-8eab-e60a8004dab3 | -14.19836 | -46.46342 | 2024-10-04 04:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 765be479-bb9f-3552-9f9a-f606e6bdb172 | -14.19715 | -46.47169 | 2024-10-04 04:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5868d3e5-d335-313c-954c-3e2e4853a643 | -14.19655 | -46.47585 | 2024-10-04 04:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7f84cf9b-6637-3796-a57c-86bc00c92756 | -14.19295 | -46.47527 | 2024-10-04 04:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0bc5dbd5-ab51-35d8-9fc6-58911b95dd62 | -14.19234 | -46.47941 | 2024-10-04 04:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23737221-6682-352c-8080-e72eb40ec6c5 | -14.18935 | -46.47468 | 2024-10-04 04:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1133824-0cb5-38f4-8b40-c83ae24b4119 | -14.18574 | -46.47417 | 2024-10-04 04:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b389d58-ee75-3526-b0eb-aee7f37f6cf6 | -14.06472 | -46.51302 | 2024-10-04 04:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0f091bd-a3e8-3e3e-8128-122f9c22f36b | -14.06113 | -46.51245 | 2024-10-04 04:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86e409a2-77c3-345e-9ea2-aaae4bfe8ee8 | -14.06053 | -46.51662 | 2024-10-04 04:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef862ef4-7c44-3833-91e0-4599a8db7e9b | -14.05887 | -46.34906 | 2024-10-04 04:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 23328afd-5a7c-3f7d-8d6f-d6b1831602b8 | -14.05464 | -46.35277 | 2024-10-04 04:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0621e85b-3efc-3994-b2c0-1b66f89e732d | -14.05404 | -46.357 | 2024-10-04 04:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e5792f3d-df64-3166-96aa-2ed5b6405028 | -13.50364 | -48.63332 | 2024-10-04 04:34:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f135fd51-9f11-3287-92d7-d4039f5f8b97 | -15.76089 | -46.16345 | 2024-10-04 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 46a5e276-5d8b-3c7a-b81e-1beaa835b85d | -17.61614 | -46.97699 | 2024-10-04 04:34:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| af1e2940-c9f7-3d77-921c-0433e1306200 | -17.61553 | -46.98144 | 2024-10-04 04:34:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 60c3d9b0-904f-3a3d-b3a7-4b1652cc3ab2 | -17.61249 | -46.97643 | 2024-10-04 04:34:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae441e51-d937-371c-8bcb-e8307fa51909 | -17.61188 | -46.9809 | 2024-10-04 04:34:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 35adb0eb-3291-3559-976e-ecb9405a2ff9 | -17.61129 | -46.98512 | 2024-10-04 04:34:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 609dbf1d-027d-37a3-ac20-1b7d97f55f85 | -17.60884 | -46.97587 | 2024-10-04 04:34:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5c4bcb02-c48e-343b-9aeb-5b02586178f3 | -17.60823 | -46.9803 | 2024-10-04 04:34:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 31c3d542-b8a3-373a-8e60-4729d8663d86 | -17.60765 | -46.9845 | 2024-10-04 04:34:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1373781e-0009-36c7-9fb6-d0355f73d02d | -17.60642 | -46.96632 | 2024-10-04 04:34:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10848bb3-cbb2-39e9-8131-e694763b0636 | -17.60518 | -46.97535 | 2024-10-04 04:34:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8f10f778-9f48-3a9e-89db-663dfef9ad7e | -17.60458 | -46.97969 | 2024-10-04 04:34:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 69e5fb14-60c0-3c8d-8aef-73b8e109bdf8 | -17.604 | -46.98389 | 2024-10-04 04:34:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0b28927f-03af-3371-adb7-82d59f8eb83b | -17.60155 | -46.97467 | 2024-10-04 04:34:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0073e20a-ff57-3bd0-a44b-53641aeccec8 | -17.60095 | -46.97897 | 2024-10-04 04:34:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 141eada9-3127-3b17-91b3-5bb90e198ec9 | -17.53429 | -46.73691 | 2024-10-04 04:34:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d47e09b9-b706-3969-853e-1c5b98a1362e | -17.53368 | -46.74143 | 2024-10-04 04:34:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5d58119d-4a65-3edf-ac62-d923a8cae865 | -17.5306 | -46.73637 | 2024-10-04 04:34:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README117.md)
