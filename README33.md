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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39ddee73-9dc0-3914-9bec-e0d320aaed31 | -3.40991 | -52.66086 | 2025-10-11 04:59:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8405dc6c-66a9-39a1-bf1d-bb86ffa60408 | -5.86424 | -42.85032 | 2025-10-11 04:59:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 41.9 |
| c1b53e21-c9d0-3fe4-a8da-242da37203b5 | -3.40936 | -52.66437 | 2025-10-11 04:59:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ffc7f450-46bf-35c0-9eae-26fa580b3a65 | -5.83157 | -49.02264 | 2025-10-11 04:59:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a4c2704-224d-3139-ac24-b64b8b6e1799 | -2.37127 | -48.29267 | 2025-10-11 04:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce8637ec-8444-379e-87aa-27a419e2ee50 | -4.42558 | -43.47661 | 2025-10-11 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1fa30469-5313-34d3-8f7d-f0a9150cc215 | -2.52266 | -44.12006 | 2025-10-11 04:59:00 | NPP-375D | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fdde9884-0482-3ed0-964b-9347fb5156c6 | -5.68783 | -47.90315 | 2025-10-11 04:59:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7803ec55-9013-3a54-98f6-82c43701a612 | -3.38874 | -50.14778 | 2025-10-11 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6ae2035-3510-3a9d-a5a2-427e79382c4d | -5.84421 | -43.40228 | 2025-10-11 04:59:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d51f907-bb34-3073-b1dd-3cb8a2fa4142 | -5.63197 | -50.4017 | 2025-10-11 04:59:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b710f28f-ca0b-3535-b7c3-e3528afad1b8 | -5.24001 | -50.94224 | 2025-10-11 04:59:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d4d948a-fd39-39d6-996d-c215e1fbe7b6 | -5.84363 | -43.40651 | 2025-10-11 04:59:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5f0fcc2-ea01-336c-a951-e227fbf09e7c | -6.75866 | -42.82573 | 2025-10-11 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 0cf07947-5a9e-38e8-ab24-83bb1fcfeae9 | -5.87539 | -45.29901 | 2025-10-11 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c6f7feff-7a0e-3941-a689-56ac95e335a8 | -5.85681 | -42.85849 | 2025-10-11 04:59:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 33.1 |
| 29e2632a-a479-3ebf-bd4f-ad4a546934e0 | -4.41454 | -43.47094 | 2025-10-11 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9883d88b-314e-3cd5-ac36-22f719aabf88 | -3.83309 | -43.98555 | 2025-10-11 04:59:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 848c9b72-5e3f-390d-97c2-5783ee8267eb | -5.36622 | -48.35816 | 2025-10-11 04:59:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a33c0916-0392-35e1-8c5b-db31b3f8cbe9 | -5.84156 | -43.40462 | 2025-10-11 04:59:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a8fc0a9-7b24-3cb1-be26-993f6d89507a | -6.75245 | -42.82451 | 2025-10-11 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| e74fc44c-ec75-3b3a-b4cb-d5b979e6396d | -13.45909 | -47.71303 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3f376f12-6df6-3d0f-8a85-a6ce8c9da867 | -13.28326 | -47.13312 | 2025-10-11 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5994cfb8-b259-32a1-8ddd-b8d749d2f4ae | -7.74991 | -44.21538 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee0b2381-2620-3efa-ba4a-b028c885fe54 | -13.36219 | -47.63605 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b0a6d7d5-c96a-33b6-902d-9b89e3b77558 | -13.30695 | -47.98407 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be5e6239-43c4-35dd-9185-9f7048e36041 | -10.51708 | -47.34591 | 2025-10-11 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 987ec122-e67e-3fcb-a3b4-1f3a15bfc4f2 | -10.61506 | -47.44905 | 2025-10-11 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 20e34894-b894-3b24-a566-4e9eb4ca6c00 | -8.01256 | -44.45804 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c9865ede-0108-39aa-9318-f8c6cc42f17d | -10.51974 | -47.34505 | 2025-10-11 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9bcd71dc-d5ef-3258-8e0b-0ed7e76dedef | -7.57352 | -45.93194 | 2025-10-11 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca1e5971-aa4f-3dcf-83a4-9d8b3a06c1f3 | -13.38454 | -47.73838 | 2025-10-11 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 415d68a6-249d-3452-b982-3f5ffc05728e | -9.25361 | -56.30093 | 2025-10-11 05:01:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7733b12c-3b87-3a3a-805b-c0917bc9d211 | -13.2979 | -48.49985 | 2025-10-11 05:01:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 077d8f4a-ecad-337b-8a25-b59d57c9dfc3 | -12.89974 | -47.05054 | 2025-10-11 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dfd1b865-50fd-3947-a9b6-a3638dc8be89 | -7.40506 | -45.92025 | 2025-10-11 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5672b04f-d575-3c58-8ab9-2a9655df6d6e | -13.29579 | -47.99366 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f78c25f-c64c-3086-bffb-a612a0e283e7 | -12.14778 | -48.0148 | 2025-10-11 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 17262167-70d2-3acf-a560-50b48ae3e614 | -12.18405 | -48.81049 | 2025-10-11 05:01:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b29a72f-880e-3dd0-a7fe-3dc064f96aa5 | -10.19403 | -44.61006 | 2025-10-11 05:01:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3349ab01-5135-336d-91d6-07d4e72356b9 | -8.88869 | -66.86884 | 2025-10-11 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46fafe38-1dbd-3f32-88f2-6f2de4efcedd | -8.21089 | -43.34654 | 2025-10-11 05:01:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| de9c2ff3-5e73-3b7e-9aa0-133525920da4 | -10.51636 | -47.35142 | 2025-10-11 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4e0150b2-1fbe-3990-a7cb-78cf9ee85b5c | -12.99775 | -45.22419 | 2025-10-11 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e8fc322b-ce2c-367e-bae2-b0b7f3f11172 | -12.90046 | -47.0449 | 2025-10-11 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c284ef1-7e5e-34dc-804a-026c13dd2758 | -7.65651 | -42.58896 | 2025-10-11 05:01:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 16388238-561d-35ab-8fa3-dc137afec87a | -13.84208 | -45.79137 | 2025-10-11 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac25c512-32bb-37e3-bccb-c6e4ffbb03eb | -8.08659 | -43.90822 | 2025-10-11 05:01:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4dd141d4-92bb-3f5c-a168-adb1bd9e3d2d | -10.14902 | -44.55629 | 2025-10-11 05:01:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6a0cee5d-248c-3626-bb0e-7d971f2cdb10 | -13.52932 | -48.12455 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6f96f4a8-4152-3999-9661-583bc4ea1184 | -9.40575 | -66.75816 | 2025-10-11 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8b43b425-71f9-31ff-8f9c-2f980d1e5518 | -10.51483 | -47.34447 | 2025-10-11 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 456f1a29-3f01-3ad0-9175-e9d764f8bf44 | -12.01955 | -55.54566 | 2025-10-11 05:01:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 67eb74a3-05a5-32ef-89f0-f1b42b162c10 | -8.21025 | -43.35144 | 2025-10-11 05:01:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 677da43b-8c79-361e-8f14-015c6240e2d0 | -9.17403 | -68.1769 | 2025-10-11 05:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14a4c25a-55ef-3cfc-8ed6-d90aaed76a3d | -12.23932 | -51.13586 | 2025-10-11 05:01:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c73ed492-5f15-3ff4-8cc8-b6ff05983589 | -11.44989 | -43.47757 | 2025-10-11 05:01:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4bc18dd6-dd87-3de2-91a2-66af22680596 | -11.9127 | -44.17839 | 2025-10-11 05:01:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3e5a4813-4d31-39be-b815-ca4ba5fc3d74 | -13.31929 | -48.48259 | 2025-10-11 05:01:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2745563-79d4-3298-8a36-1450675b3acd | -12.99727 | -45.22838 | 2025-10-11 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f194817d-1e62-3cd8-aad0-fa3c835edf46 | -13.31811 | -47.12006 | 2025-10-11 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6b43968-4a12-3fa8-9a5d-4ba2d300b979 | -6.92216 | -43.583 | 2025-10-11 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e4791806-4369-3552-9ed8-8d2a1a82cc9f | -7.41022 | -45.92095 | 2025-10-11 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e032d68-da43-3dd2-adcf-83457c039bfe | -13.21654 | -42.34805 | 2025-10-11 05:01:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 25.6 |
| 19dc0c2a-8ef9-3025-91a5-a39cd624eb4d | -12.14287 | -48.01551 | 2025-10-11 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6b7b5fae-541c-3f1c-92c3-987ca625b39f | -11.77528 | -45.04114 | 2025-10-11 05:01:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b9652de-0ffd-3cf3-ae10-1026a26ce560 | -7.87073 | -44.45471 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5cb8daa5-49c2-362e-943a-3611fb39fcf0 | -8.16387 | -43.32087 | 2025-10-11 05:01:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cca5b5bf-5581-34dd-b4e0-f0ca2c707ce7 | -13.30046 | -47.12157 | 2025-10-11 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ab1ae0fd-a9ce-30e4-87c3-228a63bb4b19 | -11.76798 | -46.37551 | 2025-10-11 05:01:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2e739221-bba1-3039-a84f-590dc18790f6 | -8.20473 | -43.34556 | 2025-10-11 05:01:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| fe340af3-ab05-3edb-9c97-671c3e5bdf36 | -10.87459 | -44.19402 | 2025-10-11 05:01:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9ca46dc-d5b2-379b-8d5c-e16c3a9492e3 | -8.58486 | -48.75051 | 2025-10-11 05:01:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d19f6419-e058-3715-af7a-f20473e4c7a7 | -11.75745 | -43.3148 | 2025-10-11 05:01:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6c8295cb-03cb-36cc-a955-185acd7a069c | -13.35155 | -47.63628 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 201fc502-946f-3af6-ac08-27b167af7cb3 | -11.067 | -49.56179 | 2025-10-11 05:01:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bcaa9c20-e90a-31cd-b498-f59ae3933b70 | -7.74975 | -44.21698 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2758a1ac-c024-34e6-9a1f-a34f282736f8 | -7.85665 | -44.47279 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9cd7efc-11a7-345e-bd57-d11cda44e4be | -10.52198 | -47.34651 | 2025-10-11 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 22fb3e47-2bd5-38e5-988c-0dec4ea4df5f | -13.33479 | -48.47403 | 2025-10-11 05:01:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23eb24af-4a5b-3296-a7a2-6d6a706f7841 | -13.2103 | -42.34055 | 2025-10-11 05:01:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 28.6 |
| a83d383f-8c63-31c6-8504-9172ecc4fba1 | -7.54608 | -44.28802 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4f559046-0b7c-3b5b-9c33-c62344831613 | -7.06674 | -45.21484 | 2025-10-11 05:01:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bd7a7a24-3d3e-32ba-ad31-2004f686062b | -10.52475 | -47.36353 | 2025-10-11 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61160c2c-9e45-3bcf-bc42-5abe8e15e109 | -13.29498 | -47.12337 | 2025-10-11 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 30a2b8d0-a854-3674-ac93-cee3a5116439 | -7.52771 | -44.29375 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d287c02-e082-3882-91df-d4024e573143 | -13.36169 | -47.63634 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 321658dc-4c71-3fd1-89e8-1012c6a84a6c | -8.01164 | -44.46006 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6bbf2abd-3e93-3bc4-8ba9-3b690c6b83d4 | -13.48943 | -48.10769 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3b60fddd-ee9e-3dbb-8c11-e8f1a43087e9 | -12.14297 | -48.01434 | 2025-10-11 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 567442b7-efca-3eab-bc45-2730b54e43a7 | -13.31608 | -47.12263 | 2025-10-11 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc443b8a-6ba6-3a15-bd93-8e6c0fe7554e | -7.85721 | -44.46864 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a09e929e-0936-3851-9aaa-146a09911f48 | -7.12466 | -45.0863 | 2025-10-11 05:01:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d14522ea-433a-3381-a1a1-d95ad18e85c8 | -13.309 | -47.98535 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ced931c9-d239-3b72-9d73-af5fa356ff13 | -12.23333 | -51.06729 | 2025-10-11 05:01:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c571fe9-af83-313d-8250-cf521e29fd33 | -7.41064 | -45.91786 | 2025-10-11 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e0b49f18-402c-3759-a79c-995ceafc6944 | -13.30976 | -47.97906 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 65ccde49-607e-3244-95e9-8038e8ad4327 | -12.9001 | -47.0477 | 2025-10-11 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 23978dc7-1800-32a8-bd00-fab033709005 | -12.23965 | -51.13422 | 2025-10-11 05:01:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f03bf796-167f-34e2-964a-83c91242b1ce | -11.15988 | -49.81892 | 2025-10-11 05:01:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README34.md)
