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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb79dfe6-99d7-3855-bc9e-af4454c216e4 | -12.92003 | -54.73059 | 2025-10-01 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 27d376fe-e39b-3951-924c-038f09f97974 | -14.05127 | -47.97183 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 2edc6e06-c0a3-3f86-ae04-f26716be8c00 | -15.33443 | -47.94015 | 2025-10-01 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b09a871e-7993-3414-9657-64b0b592d990 | -9.94406 | -55.16009 | 2025-10-01 04:51:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e51e00e6-d5a9-343c-a932-22b357b1575d | -12.78607 | -46.90987 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0cb0b1e7-2dd0-3961-b8a9-6ca8d55239be | -10.21794 | -43.04807 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 64fd017a-0f2e-387e-9b02-97bb97577b85 | -10.67637 | -48.72056 | 2025-10-01 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 36c9f8ee-cf6c-3b66-a751-29f67427d6c4 | -13.53291 | -47.25722 | 2025-10-01 04:51:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed81f143-9dcf-30a7-84d5-cc96e8453bb1 | -11.15256 | -54.12172 | 2025-10-01 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1f4c7a39-7bde-3460-83b7-f175965f0e53 | -11.47331 | -45.10577 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cab41a7c-b9d6-363d-8aef-48d46b658b30 | -10.90637 | -46.56655 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 14f05622-2312-3ef9-a895-335985ea1a28 | -14.90463 | -48.37113 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4343f447-d0da-34bc-832c-477dd1629c4d | -15.3856 | -49.1924 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0229a5df-314e-32c9-a733-49930927ee73 | -11.46424 | -44.99396 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 003cd3db-e97b-3569-a02d-75a0524c3a5f | -14.59224 | -48.29696 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3bb1fe0-e2f3-3ebb-a116-600c94a5a9ca | -15.40635 | -47.05586 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c421472-03d6-36b0-8ae0-fe786cc92fad | -14.49288 | -48.44112 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a6144554-02c9-3a58-b2fc-cbc8bd9b2717 | -13.77235 | -48.01062 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2f8efd09-2bbe-3ef2-b5b5-fe8e366a2904 | -9.80606 | -45.93824 | 2025-10-01 04:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51b9ebed-371b-3acd-9223-177471aa159e | -12.85383 | -47.0085 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2371742b-c885-3b86-a49e-f37f5e71ba26 | -11.92189 | -47.89444 | 2025-10-01 04:51:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 18e64e8f-8299-3226-b544-e82e54bcbb80 | -14.39369 | -46.21806 | 2025-10-01 04:51:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e156de2-68d2-3be4-add9-8a4a8a4856ca | -13.78804 | -51.23324 | 2025-10-01 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 079a3542-4f84-3689-aafa-ead71dd2ee70 | -15.48805 | -45.91777 | 2025-10-01 04:51:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| be4f2f3c-aef1-340c-88dd-190ed11049b5 | -14.91748 | -47.821 | 2025-10-01 04:51:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4fc95b8a-f214-38ab-baf9-686f02427b8a | -14.68108 | -48.22848 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5aaa5fd-25de-3029-9d6f-cd7348a4762a | -10.92799 | -46.50576 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 885d33a9-a9f2-30a0-a8d3-f7003a737fcf | -16.24356 | -44.05936 | 2025-10-01 04:51:00 | NPP-375D | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 60e12be2-f5f9-3909-94c5-7110c573bd36 | -15.28287 | -47.89333 | 2025-10-01 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43adc4e5-13a9-37c5-ba99-0874f6deeca4 | -10.47558 | -55.62344 | 2025-10-01 04:51:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e638bb3e-d065-32bb-84aa-02cd161d63be | -14.68038 | -48.23368 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d80e91c-8004-3ddf-84e2-1263945bf0c5 | -10.3625 | -48.78231 | 2025-10-01 04:51:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 070f805c-2575-39ae-b3dd-0f8b49228247 | -13.5859 | -48.0384 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 05364262-29e3-3d69-871b-3ca9f521dddf | -13.3682 | -47.32376 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 03184ed0-0862-3c1d-a7e8-442d250c4d3b | -11.92647 | -47.8901 | 2025-10-01 04:51:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 74bf73f5-e602-3f45-84d6-f0975711a1e8 | -12.13372 | -42.87416 | 2025-10-01 04:51:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 528285f0-c248-3c5c-bf11-3f658b56589f | -12.2411 | -47.80827 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9d6824ef-4180-3f09-8f87-95f6614072a3 | -13.79164 | -47.98822 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ce2254cd-a071-3bea-88d7-53164bbfee6f | -9.938 | -43.64627 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7a1aeeb5-4869-37b9-a82d-0c63e55b6369 | -11.83802 | -44.98529 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3340b7ad-9543-3b35-b46f-2bec1c31ad8d | -9.92338 | -43.6799 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 09099f4d-e9b2-307c-978d-6bf91a8c61ce | -16.0092 | -50.8786 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d2b0e14-e208-3097-863c-c953086437ec | -13.33211 | -47.85361 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f7a034f5-2372-3472-9ee1-2667ee5c4964 | -15.16836 | -52.80809 | 2025-10-01 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ecf165b-39c0-3bc9-8837-0fe64143b44f | -14.56183 | -48.48833 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96b9a3a0-22b8-35c2-85f8-46b602223c9f | -12.79603 | -46.89976 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b269c28c-7110-3b11-9cd0-1b49e62e4aa1 | -8.65046 | -50.20588 | 2025-10-01 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 968a00c5-4e6f-3b1f-9bcf-05d71ba73f39 | -9.92614 | -43.66163 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9f9f09cb-1e11-32cd-a63f-bfeb05bb6ed3 | -12.0021 | -46.64789 | 2025-10-01 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6610f970-3ab7-305b-bc2f-8bfdaf345fdd | -9.39827 | -54.71653 | 2025-10-01 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15dfa98d-820a-360f-8ea4-2ac32fab8d95 | -13.98657 | -44.91336 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 361d70b9-4e48-3b66-a89b-79f500f9436e | -14.70835 | -49.14355 | 2025-10-01 04:51:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 32dac8aa-8420-3c1f-8203-a7ee336dfa2e | -14.87941 | -48.32037 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 97997d42-1f4e-30fb-b961-cf9ebedcfcfe | -11.43044 | -43.49926 | 2025-10-01 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 114556fe-7ac2-363c-89b5-d3766decc1f3 | -12.8428 | -46.87027 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12a36bc8-4a9f-3bf6-b224-824b880e94bd | -10.91002 | -46.57087 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7f44ebf1-16a6-3a39-b455-476783f56bdb | -15.31425 | -46.4121 | 2025-10-01 04:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f2a7e34-9959-38d8-b137-fe7e9f022727 | -15.23248 | -48.73816 | 2025-10-01 04:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f5fe6356-678c-3521-ac8f-25546b79d202 | -14.7108 | -48.21782 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1f30d267-a839-337f-9b56-78380b77ea2c | -12.01795 | -46.62634 | 2025-10-01 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aba4217c-c802-30d9-b3d2-38ea7084b84b | -13.09482 | -47.00145 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b8a028b-50bb-3029-88fd-a551669256bc | -13.81377 | -48.03226 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2182b9d-adaa-3018-9fce-bef94c360f96 | -15.77522 | -43.68353 | 2025-10-01 04:51:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2912bce2-4e8e-3bc1-b57a-aed8fb040602 | -11.91662 | -47.90379 | 2025-10-01 04:51:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 725ffd86-d5a8-3eec-b7a0-be92bbab4d01 | -13.81453 | -48.0269 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1bd9c98-c5a4-35f2-abe3-f1e35cfd705f | -10.90748 | -46.55885 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b0411649-21fb-3dbc-bc06-f0a671f4d91c | -12.24902 | -47.80902 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d400a9b3-2486-34a2-9fab-b7eae7325aeb | -11.05517 | -47.82016 | 2025-10-01 04:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c941cc40-a059-371b-afff-9ade687f535a | -12.9276 | -54.72795 | 2025-10-01 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4da14b2-e11d-39e6-8a70-d4834bde9dae | -11.64888 | -45.32277 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 969c2b71-fd48-3c56-9d88-75cc805f2a60 | -15.26895 | -49.28499 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8ab25ac-f5ae-3314-90a4-e781d2f84714 | -11.9414 | -47.06229 | 2025-10-01 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e69cb615-aa1d-324b-82ac-c7c8b5a5fc51 | -12.22199 | -43.75621 | 2025-10-01 04:51:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b23b7e2a-8480-3ece-be05-5c25e3d437bf | -15.73956 | -49.3253 | 2025-10-01 04:51:00 | NPP-375D | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a210f7c-7e49-31ab-8c03-fd5acf35222d | -13.97597 | -44.8792 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a2e6b0a7-0c40-3a13-b481-f25daf57ca15 | -8.96725 | -50.25063 | 2025-10-01 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9cc42960-5a1a-3bd3-a13a-bc943db41c49 | -10.17651 | -44.90134 | 2025-10-01 04:51:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ebac24d-1a5d-3f3f-af1d-9c7363902e32 | -12.3726 | -50.20096 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7796893-f413-3117-add2-dac25f7f11a5 | -11.83252 | -44.9543 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75a7513c-8481-37ed-9091-9b0bbf891b92 | -10.59269 | -54.34901 | 2025-10-01 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f58fca9-5941-3fbf-aba1-fa9e3b84a956 | -10.17256 | -44.89584 | 2025-10-01 04:51:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| daa6c0b0-1501-3f37-a043-72a23ec320e7 | -12.80502 | -46.89648 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27e65d5e-2a0d-31a5-8edc-6a4619e8b4c5 | -13.33157 | -47.82783 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1441ff80-7a32-30b1-9608-74fe9d34f64c | -11.82255 | -44.99341 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 30e729e6-4f83-3ea7-840c-fa99209be580 | -14.3637 | -47.13309 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e083fd49-37bc-3322-9d93-2c7220254880 | -12.23493 | -47.82322 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b8878e6e-51d1-3ee4-b0e6-d8fab3eb6798 | -13.37845 | -47.31047 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a625b376-83fb-3a62-b7e8-04b6be4a69b8 | -10.21317 | -43.04221 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e4f4b1d2-8196-3885-9d91-a7d7738a6799 | -15.81858 | -41.88998 | 2025-10-01 04:51:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b87bd151-eb01-3319-ab43-6d6184d4b9ce | -13.71672 | -54.71764 | 2025-10-01 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d8bc716-5389-3c36-9af7-027712f76f45 | -14.75339 | -45.76354 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0da4f5ad-5f85-3a54-94b8-4c08bca6af3b | -13.56034 | -47.27284 | 2025-10-01 04:51:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1a8e9253-dd9d-3967-9eec-0edc2051cbda | -11.07626 | -47.82006 | 2025-10-01 04:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 96f9377c-8ed9-3908-a119-358d08de36e8 | -11.08401 | -47.82108 | 2025-10-01 04:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4a61a0f8-bf58-3c75-85ef-3a29193fcd52 | -13.81274 | -48.02906 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d142ae9d-0825-32c8-bf1f-e30b529d1d51 | -13.10114 | -47.02502 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b99026cb-f9be-3a1a-8481-a9a79cc2959b | -13.30409 | -47.20747 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b1343337-f48e-38e3-9efb-efc7642663e3 | -14.61205 | -48.21158 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 940d9dda-e48e-3fdb-85ad-9c1291b1d0a3 | -10.85032 | -45.41324 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| faf151d1-19ea-38cd-9140-29787a42e3ac | -14.18537 | -46.11466 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README94.md)
