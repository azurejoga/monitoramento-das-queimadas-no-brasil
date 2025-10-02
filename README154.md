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

## Dados Diários - Página 154

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34d25d06-6c66-36c9-ad45-025198367008 | -10.222 | -50.2662 | 2025-10-02 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 5219a1f4-7cf0-3ab3-9514-d3c08d4786a2 | -8.1513 | -44.1397 | 2025-10-02 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 4a767555-c080-32c6-8d95-8f025181364e | -9.9376 | -43.6953 | 2025-10-02 13:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 149.1 |
| a2176a27-92a9-37e4-909d-507f47dd6fc3 | -13.1743 | -47.8093 | 2025-10-02 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 176.6 |
| 417f41cb-c1f8-3024-ae9a-4807c04adf5b | -11.1941 | -47.2557 | 2025-10-02 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 298f3f51-a8ec-35cb-909d-2741f6ce9393 | -12.5001 | -50.2453 | 2025-10-02 13:20:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 97.0 |
| e008cc2d-bb47-30e0-8e62-063c534d9cfb | -15.3067 | -45.0713 | 2025-10-02 13:20:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 246.2 |
| 48b66718-91c9-3f59-9473-178a4228fb9e | -7.8879 | -47.3031 | 2025-10-02 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 112.2 |
| d3fbd0d8-d7b0-395b-bc9f-c34e9fc1bfc4 | -8.5201 | -47.8386 | 2025-10-02 13:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 058fa1b3-3aa9-335f-aa6f-8f26b0e2968e | -11.2803 | -47.8223 | 2025-10-02 13:20:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 737eb14b-ab18-3bbc-b791-ed0088f78221 | -8.6722 | -47.6924 | 2025-10-02 13:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 609551b3-aef1-3586-b014-2e45bdd25af5 | -13.1932 | -47.8288 | 2025-10-02 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| b6929d00-7840-3a84-aaf7-e5d7b2799656 | -6.679 | -42.8136 | 2025-10-02 13:20:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 91.2 |
| b7a88a25-33d7-3deb-b283-32ff7af4eda6 | -6.6976 | -42.8354 | 2025-10-02 13:20:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 108.0 |
| a9318f60-b9aa-39ef-b56d-359633f9f519 | -16.0426 | -50.8522 | 2025-10-02 13:20:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 27a01c45-c2a8-33fa-88e6-cf3474ca1714 | -8.2094 | -45.5301 | 2025-10-02 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 544f21be-be02-3fcb-8cc8-4f3d8f78d169 | -9.4083 | -47.5742 | 2025-10-02 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 162.9 |
| d37147af-2fef-30ed-bf7e-28485519c16c | -11.4796 | -44.9943 | 2025-10-02 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 341a81d6-b263-3063-8900-d2cd74cb0c21 | -14.2924 | -45.977 | 2025-10-02 13:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 98a42ce8-cdd4-373f-b368-d80d0e9a5c6d | -11.8234 | -45.0364 | 2025-10-02 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 116.6 |
| e832e55c-eefc-30e0-83f4-5a4e1859843f | -8.6534 | -47.6943 | 2025-10-02 13:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| f7fda850-41f0-38a2-8b7b-dab41a241c0c | -14.4757 | -48.4137 | 2025-10-02 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 04f9b7f7-474c-3671-a83a-667ed6333104 | -7.7752 | -42.539 | 2025-10-02 13:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 288.8 |
| 58543b2e-8e6c-3c99-9eb4-25b50a5ecd59 | -8.1702 | -44.1377 | 2025-10-02 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 207.3 |
| ed9566fb-5f94-3acd-8daf-e3bdd20fef12 | -16.0421 | -50.874 | 2025-10-02 13:20:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 79.8 |
| b18e7754-7cfd-330d-848e-c65fd965d175 | -12.902 | -46.9299 | 2025-10-02 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 140a2094-5bd4-322d-83aa-687ba5a89e74 | -6.7814 | -45.5929 | 2025-10-02 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 287a9f4f-3a33-348a-b614-eb95611e373a | -7.5472 | -42.6579 | 2025-10-02 13:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 94.9 |
| a65867ad-ad67-3781-8b4b-e425a32cd726 | -13.1739 | -47.8317 | 2025-10-02 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| ae572ef2-2de2-3f8d-8884-395a188b895a | -14.1917 | -46.1552 | 2025-10-02 13:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 126.3 |
| c09ce006-5b34-37ca-b421-c18bed296531 | -11.8238 | -45.0132 | 2025-10-02 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 1da80177-881b-3c0b-a54e-41fa3139410c | -13.7864 | -48.0524 | 2025-10-02 13:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 2c6a432f-75b3-30d2-b304-8b88f8ed59c0 | -9.4086 | -47.5521 | 2025-10-02 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 07e157c5-95db-3885-aa4d-ef670d0946bb | -11.0997 | -51.0687 | 2025-10-02 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| f82c7dee-004a-399d-b2bc-0bef0d79fd99 | -7.5746 | -46.8 | 2025-10-02 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| f369593a-e1ea-3c7b-b6b7-f80b41d77408 | -9.336 | -45.9305 | 2025-10-02 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 317.2 |
| e11c395f-2f7a-366f-8926-61bfa8173863 | -7.8882 | -47.281 | 2025-10-02 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 7a390173-9537-39b2-88e4-cc086373cd51 | -6.7816 | -45.5703 | 2025-10-02 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 8a7fba83-e72d-3092-ba8e-26be4f511055 | -14.3309 | -45.9933 | 2025-10-02 13:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 162.9 |
| 0b2235c6-4ec5-39f4-b668-0f94c45f8d6d | -11.8438 | -44.964 | 2025-10-02 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 223.0 |
| 08713b82-d0e8-3096-8a51-0ff915bbc94f | -7.7311 | -46.2289 | 2025-10-02 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| bcf887f6-b955-3a7b-bf64-d22c9a783e4b | -11.9085 | -47.8745 | 2025-10-02 13:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 6b8e66a2-d41e-3a4e-ae6f-f9c1e056a971 | -14.3114 | -45.9967 | 2025-10-02 13:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 159.7 |
| cd416963-27a0-3503-a5c5-4dd85ad78d08 | -7.7941 | -42.5369 | 2025-10-02 13:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 238.0 |
| bcd7ed6a-334c-3521-af14-b2949f69ef1a | -6.7816 | -45.5703 | 2025-10-02 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 103.6 |
| b1921efe-b585-32b5-8dbb-27402b64d17c | -14.2121 | -46.1058 | 2025-10-02 13:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 55856552-9c3f-3353-b61c-415d5ebcd8b4 | -18.1782 | -53.3024 | 2025-10-02 13:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 175.1 |
| 3d7b0985-23ca-3599-8727-3c1a2dd371a2 | -8.1702 | -44.1377 | 2025-10-02 13:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 99.3 |
| d9bea429-399a-3473-849b-662dcf4b752c | -9.4083 | -47.5742 | 2025-10-02 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 2c54c084-f456-3305-b60f-654e7c6a836f | -11.1746 | -47.2805 | 2025-10-02 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| d30b6e6c-6d7f-3670-ba43-c7cf527474e8 | -7.5661 | -42.656 | 2025-10-02 13:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 94.9 |
| b684c045-345c-37ea-aa15-b621758233ec | -13.7864 | -48.0524 | 2025-10-02 13:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 92.7 |
| b7e85e25-f185-34b7-81f1-55eb7f9d4eb5 | -9.336 | -45.9305 | 2025-10-02 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 232.4 |
| 477da5e4-81d9-3487-9799-8960797ee905 | -8.2094 | -45.5301 | 2025-10-02 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| bf6140d1-aa03-3783-b576-4166c0727779 | -14.7562 | -45.2219 | 2025-10-02 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 2c344e1a-064b-38e4-8ad2-1709651e1975 | -8.5201 | -47.8386 | 2025-10-02 13:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 86378f34-bee6-3172-8ec5-b1f80ffbe726 | -18.2375 | -53.3145 | 2025-10-02 13:30:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 129.6 |
| e6e591a5-4354-3572-97da-439f9a65989c | -7.7944 | -42.5132 | 2025-10-02 13:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 211.4 |
| fe680497-e938-36c2-b5a0-65e8782d59fe | -12.6729 | -46.851 | 2025-10-02 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 208.2 |
| 9dda3a77-3929-399d-a0bb-c7852d63b4cb | -7.8879 | -47.3031 | 2025-10-02 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 170.9 |
| c1d861de-7052-3df5-90a5-94ac549c9b5c | -7.8882 | -47.281 | 2025-10-02 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 1ad0cba6-866d-3a5a-8085-fda833570426 | -11.8238 | -45.0132 | 2025-10-02 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 07c785c3-80a8-30db-a280-7d5badc6dd21 | -8.5599 | -44.6494 | 2025-10-02 13:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 166.5 |
| d98c2f99-b746-3438-b8ae-66f771514a8d | -8.5962 | -44.7603 | 2025-10-02 13:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 87.2 |
| c31ed423-55f2-3da5-864e-0da261fb2c92 | -18.1981 | -53.2993 | 2025-10-02 13:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 8eb9aeb1-b893-36b0-ae8b-14262649bb68 | -14.4065 | -46.0953 | 2025-10-02 13:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 1456e42c-595e-3b07-8417-e87c402eb96d | -11.9276 | -47.8719 | 2025-10-02 13:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 367c1d77-b830-3cbd-9d31-eac0531e7d9f | -9.4272 | -47.5722 | 2025-10-02 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 7915e6ac-b0ab-3647-aae5-35d90f3032eb | -6.6976 | -42.8354 | 2025-10-02 13:30:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 88.1 |
| b7d4055d-7a3e-3834-8d4a-b99392e0225a | -6.7626 | -45.5944 | 2025-10-02 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 150.0 |
| f6e4d621-5a9d-3195-b1ec-753ea9ca08e5 | -7.5475 | -42.6342 | 2025-10-02 13:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 105.9 |
| 40c176d4-2c6e-3b79-8ee6-e2f5e2e10dee | -16.0421 | -50.874 | 2025-10-02 13:30:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 77618429-afa3-3662-8f28-20cfbc27dbcd | -7.7755 | -42.5152 | 2025-10-02 13:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 192.5 |
| 3a7d2902-86cb-3518-9562-1e9a701c2cdf | -10.127 | -50.3184 | 2025-10-02 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 634cbf6b-c397-32b8-852c-dc715c6f2d47 | -13.1542 | -47.8568 | 2025-10-02 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| c57a7442-672e-3b5a-ac86-f0f5681dd655 | -14.2924 | -45.977 | 2025-10-02 13:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 210.0 |
| b4ed62f1-cb8e-3183-a58c-a8148b5556bb | -7.7752 | -42.539 | 2025-10-02 13:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 357.3 |
| bef40234-e2f1-3d03-a673-8538d71f9831 | -12.7627 | -50.5567 | 2025-10-02 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 4d15203b-0b7e-388c-b8e9-614ac4bc0728 | -6.7814 | -45.5929 | 2025-10-02 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 148.3 |
| b79a5bb8-1e7c-32ab-9464-8d81a0212895 | -13.3001 | -47.2529 | 2025-10-02 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 60.9 |
| c0f10ce2-e99d-3942-bc69-9149fb0629d3 | -8.5016 | -47.8184 | 2025-10-02 13:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 8446059d-08d2-3abc-83c1-ccd61eaaeda6 | -10.937 | -46.6618 | 2025-10-02 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 1695861e-e6d7-3bd6-b475-e3361517980b | -11.5869 | -50.1612 | 2025-10-02 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| e5649f75-b09e-36a8-997f-99050ced509b | -14.7043 | -49.616 | 2025-10-02 13:30:00 | GOES-19 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 111.3 |
| a327cc19-f59c-3e48-b2a7-622722ac7934 | -14.1917 | -46.1552 | 2025-10-02 13:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 234.8 |
| 88a7b7db-ed1d-3bfa-9c0f-be1d9f96bd61 | -18.2171 | -53.3392 | 2025-10-02 13:30:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 195.1 |
| 00036ac5-e139-3dc1-8386-40bff6c33cbd | -8.5204 | -47.8167 | 2025-10-02 13:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 5440c499-983d-3a1c-ab8d-3f072f05814d | -15.2738 | -49.3073 | 2025-10-02 13:30:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 35aa50d9-4f19-3a0f-90bd-1b20769ec5e2 | -10.1459 | -50.3165 | 2025-10-02 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 41e7850a-286b-3d1e-98ec-c36e5dd7b47c | -7.7941 | -42.5369 | 2025-10-02 13:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 179.3 |
| 753b4d54-85b9-3445-ad85-fcc14d1a06dd | -16.0567 | -45.7204 | 2025-10-02 13:30:00 | GOES-19 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 9f39a29a-b22e-32ca-ae1a-97f160c54f92 | -14.4753 | -48.436 | 2025-10-02 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 88.7 |
| faf03f89-5556-3457-88d7-3dc713fc16e6 | -10.8234 | -46.6313 | 2025-10-02 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 37202fb7-855f-306a-9ca5-7b25a0a94004 | -18.1786 | -53.2809 | 2025-10-02 13:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 212.4 |
| 8204405c-728f-3675-a2ab-257d6353764c | -15.3067 | -45.0713 | 2025-10-02 13:30:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 6e14f42c-6da0-3328-a5bf-763916406dd9 | -12.5001 | -50.2453 | 2025-10-02 13:30:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 105.8 |
| f3c17b48-26a5-3159-b970-35024bbd6bd9 | -11.4792 | -45.0174 | 2025-10-02 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 0c62662b-914e-38a8-969e-e39490a19180 | -11.4796 | -44.9943 | 2025-10-02 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 149.6 |
| 2489a478-8c86-3d5a-8c97-32713b20eb4b | -10.8622 | -46.5814 | 2025-10-02 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 126.4 |
| c9249364-7711-3f3b-a8d7-3dc09d5528ec | -14.4757 | -48.4137 | 2025-10-02 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 124.4 |


[Clique aqui para ver as próximas entradas](README155.md)
