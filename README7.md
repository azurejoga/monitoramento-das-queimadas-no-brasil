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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c96fd31b-cd73-3c9d-8645-b6a1b4246e73 | -3.51462 | -48.04002 | 2026-06-22 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 93a5cb4f-27ca-3120-8b9b-64990145c536 | -4.27882 | -48.66162 | 2026-06-22 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 908fc555-3e57-3ea6-8149-15d6d27a0271 | -3.50741 | -48.03596 | 2026-06-22 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 44909107-57ee-3726-ba96-3cd8a726eb88 | -3.51419 | -48.04284 | 2026-06-22 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fb02ce9e-0697-3833-a4e8-bb663edef7cd | -6.23863 | -48.52987 | 2026-06-22 05:10:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9ea46269-6218-3b2d-a449-da915780fd07 | -8.02045 | -49.64525 | 2026-06-22 05:10:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3bfc6b37-1ded-3214-be69-e3253e0b9199 | -3.5121 | -48.03973 | 2026-06-22 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b4dd8daf-cd0d-3884-8387-7ca0738be216 | -8.61825 | -47.79428 | 2026-06-22 05:10:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 48b40617-1c99-3b95-9fde-10289ba1461c | -6.51154 | -44.69963 | 2026-06-22 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a36359c8-df5d-36d6-b00a-b6b64ddc09c9 | -3.5194 | -48.0253 | 2026-06-22 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be0943f3-49bc-3686-a7a9-b1d77d411e4f | -3.50698 | -48.03893 | 2026-06-22 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 171dc355-ed8a-33b5-bb29-497984197cd1 | -3.50949 | -48.03929 | 2026-06-22 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e05dff34-04ef-317d-a082-6d9b0d05fd34 | -6.24029 | -48.53212 | 2026-06-22 05:10:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2de2fda9-3075-35e0-8c3e-00b08eb50d02 | -6.23572 | -48.52696 | 2026-06-22 05:10:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91583256-1740-3aff-8dff-0d8c74a280e7 | -7.96551 | -47.42223 | 2026-06-22 05:10:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 41455f63-eb44-3c98-a129-fbf2734a9d5d | -7.97274 | -47.43027 | 2026-06-22 05:10:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6bc4c8d-6ea5-3a17-9065-018e4214cefa | -3.51475 | -48.02115 | 2026-06-22 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 20f3c24f-c04a-3320-98b7-3161465b3039 | -3.51505 | -48.03716 | 2026-06-22 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00fb8527-b298-32a0-b398-fcacaa90ed13 | -6.24077 | -48.52861 | 2026-06-22 05:10:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e03e7b91-e40a-370c-bbf0-6c6ea0d0686e | -2.32456 | -60.06224 | 2026-06-22 05:10:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f7b8c07-d886-3fce-91fb-657c30761b9b | -6.51222 | -44.69427 | 2026-06-22 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ba0c041-debd-3657-a3cd-b971c2477961 | -4.27787 | -48.66111 | 2026-06-22 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb22760b-d865-3032-a3be-67e0700a2a64 | -6.23982 | -48.53567 | 2026-06-22 05:10:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| baee7d91-de8f-3c14-a6fb-2ce9ea7619c6 | -3.50907 | -48.04208 | 2026-06-22 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9fe65977-737e-32e7-8072-22436a02e11e | -6.50101 | -44.69435 | 2026-06-22 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 4c206241-a0b0-37cb-b3d3-37d749ba9eaa | -2.73724 | -58.18967 | 2026-06-22 05:10:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a38ed900-179c-3998-a5f2-edc4ab1e4275 | -7.96607 | -47.418 | 2026-06-22 05:10:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 41d45d7a-9846-32c7-82f6-3f566dc777a8 | -3.51691 | -48.02478 | 2026-06-22 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe89da8e-d407-323c-8530-6cc2c90dfd2c | -6.23914 | -48.52634 | 2026-06-22 05:10:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2cd50f2c-c7b2-3a8a-aa63-df0e99d6d896 | -3.5117 | -48.04254 | 2026-06-22 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dda84489-0fe3-3690-85d1-3ec2b1d675cd | -3.51894 | -48.02852 | 2026-06-22 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ea0dab95-b938-37bd-8d0e-4a9812d7b18f | -8.87364 | -46.95609 | 2026-06-22 05:10:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8054faad-e382-32f9-8545-fba41a40f9db | -6.25627 | -48.53073 | 2026-06-22 05:10:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3297a72f-57ae-34d3-ac99-7d146c3a483c | -3.5143 | -48.02435 | 2026-06-22 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4376761-73fd-32a4-883c-07adad04ab5a | -8.8742 | -46.95171 | 2026-06-22 05:10:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 55560b36-e862-3aab-af54-14b64f86f749 | -6.25152 | -48.52696 | 2026-06-22 05:10:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ac92db0-4445-3f8b-813e-39021de35fe1 | -3.51724 | -48.04042 | 2026-06-22 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ad939f92-bbac-3d31-bdf9-7f9b778913de | -2.67119 | -55.74789 | 2026-06-22 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6dccb507-7345-31c1-841a-431776f23d9c | -12.46816 | -55.13156 | 2026-06-22 05:12:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b95acbe-1e05-33c2-bda7-6c16796d878f | -11.06073 | -52.47476 | 2026-06-22 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d38964d-081a-3fda-93b2-f1f6584098b5 | -11.05596 | -52.4781 | 2026-06-22 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2828f1db-3b2b-36e3-9988-da9734db65dc | -12.4712 | -55.1365 | 2026-06-22 05:12:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fff16a2b-78cc-3d52-acf1-7906958335e6 | -10.91207 | -46.31701 | 2026-06-22 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9145cf77-ffa6-3b84-a35c-22099eecc681 | -12.07021 | -48.42546 | 2026-06-22 05:12:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cd8e96b5-6a3f-3a86-b29b-2cc2552e459f | -11.51755 | -56.12228 | 2026-06-22 05:12:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 159b4aee-609f-316e-a219-0f602335b98c | -8.88547 | -46.93952 | 2026-06-22 05:12:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1d6bc72-f418-34d9-90e3-62eea03fad36 | -10.7713 | -54.10917 | 2026-06-22 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef5d0a22-f974-32fb-a54d-6af94d1c2ab8 | -11.10772 | -54.13626 | 2026-06-22 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ce8095d6-81f6-3c78-bfe0-51c706d3ff9f | -13.29979 | -45.2143 | 2026-06-22 05:12:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8af35405-b127-3e3b-a920-47d92678016d | -12.4305 | -58.40744 | 2026-06-22 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0730f742-e136-3923-b0c3-c654e04aa12c | -12.46613 | -49.16135 | 2026-06-22 05:12:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f2aef60-e616-32f8-bbb4-d8470a064075 | -11.05909 | -52.4866 | 2026-06-22 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4d28b6d-2535-387c-aed1-0e904cf1954e | -11.51409 | -56.12175 | 2026-06-22 05:12:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f3ed5fc-a8a6-3617-b2b6-8e05a7e5a50a | -13.51835 | -52.16389 | 2026-06-22 05:12:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6291cd5a-b40e-3962-8b5f-4059eb83802f | -12.4694 | -55.12278 | 2026-06-22 05:12:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e78a89fc-7b99-3c0b-b4d3-88edc59d4b17 | -12.42941 | -58.41446 | 2026-06-22 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3c73c6d7-de96-3219-a2a7-fc2cde0759bb | -10.90925 | -46.31693 | 2026-06-22 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b80ac009-2244-35a8-9b5d-a5048325167f | -12.42996 | -58.41095 | 2026-06-22 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| feef0b32-7949-3ed9-908f-ea6471f00bf7 | -13.30076 | -45.21132 | 2026-06-22 05:12:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a73c55c-97d7-387f-864e-87c632f8c227 | -10.17943 | -51.66433 | 2026-06-22 05:12:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d44e582c-ecc0-33e2-ab6d-c2a151b350d3 | -12.55049 | -57.2035 | 2026-06-22 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c084fe3-bf0a-3b64-b04d-ee739716e504 | -12.22569 | -57.28377 | 2026-06-22 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61f62484-713f-3908-a4b8-565a806ab6b1 | -11.10325 | -54.14045 | 2026-06-22 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b6135573-20ec-3e50-93d2-a348f961bc58 | -10.55789 | -46.24355 | 2026-06-22 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57a7265a-0565-3a42-859b-eca9445a1c7e | -12.43544 | -58.39744 | 2026-06-22 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 87e889d2-4d88-3187-8c46-837e2ce87842 | -9.18514 | -58.05693 | 2026-06-22 05:12:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3369b6f-3572-3a51-89a1-86c5936ac2cd | -10.53905 | -47.73117 | 2026-06-22 05:12:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9f9ae9bc-7bed-3a17-a228-7bf80fc3112a | -12.43489 | -58.40095 | 2026-06-22 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 482f6c02-e0ab-37bd-babc-a70edc840c2f | -11.05433 | -52.48991 | 2026-06-22 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39662d27-eb96-33ab-8309-6bc0a99b4945 | -12.42802 | -54.17804 | 2026-06-22 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da5f102f-4f84-3527-a314-e31c11ec2885 | -11.11153 | -54.1368 | 2026-06-22 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dff58d56-b468-3b3e-86c1-811a4a72cf2c | -13.83504 | -47.12287 | 2026-06-22 05:12:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21dc1094-ddbe-3a5c-b995-f5ea5d4f8049 | -13.84114 | -47.12505 | 2026-06-22 05:12:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5dc80a3a-905c-3cac-af20-ef64b39215b0 | -11.93299 | -57.04144 | 2026-06-22 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6db19bca-f6c0-35e5-a19a-70a5151be321 | -11.05066 | -52.48531 | 2026-06-22 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6166aae-4d93-3601-bbf4-7a23dab3ee0b | -11.04808 | -52.47282 | 2026-06-22 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2972bde-ff73-3799-b10e-11393d7d75ce | -10.94452 | -46.42445 | 2026-06-22 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d0e1412c-14d2-38b6-b801-ff11ad9986d5 | -10.54109 | -47.71435 | 2026-06-22 05:12:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a506a810-ad83-31f9-a30a-c87ed6271017 | -11.05229 | -52.4735 | 2026-06-22 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 67de278f-1198-32c6-a59e-45f60b8f43b3 | -9.25157 | -60.33346 | 2026-06-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b646f3e2-1cc9-3204-a030-910d44515fed | -10.5654 | -46.23421 | 2026-06-22 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6d0d767-31d0-3b30-bb9e-cf1ddf433624 | -13.52281 | -52.16451 | 2026-06-22 05:12:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5abef88f-b27d-30fd-96e3-b40ebb9a33b5 | -11.05487 | -52.48598 | 2026-06-22 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b9049c2-e9a0-39cb-a4c6-7e66e8ee26dc | -10.56927 | -46.23487 | 2026-06-22 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 176f2bf1-3c49-3470-8caa-c29154aa840f | -11.05175 | -52.47744 | 2026-06-22 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 51a8be36-de8c-34c6-8691-d90ccd00af2e | -12.2011 | -47.96795 | 2026-06-22 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8947b460-0b1b-3fae-99a8-ba31ab6435c6 | -11.05542 | -52.48205 | 2026-06-22 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0dd76b2a-0799-31f6-bb54-a7722a143c9b | -8.88192 | -46.93876 | 2026-06-22 05:12:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50518a86-89a4-338f-80e4-7e3ff771568a | -10.56172 | -46.24403 | 2026-06-22 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03df35d4-5bbc-3129-978a-316a4491e9cd | -11.06018 | -52.47873 | 2026-06-22 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 153aa07e-b065-3599-8962-4ccdaa7568cf | -12.43819 | -58.40149 | 2026-06-22 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 377754f1-1dd7-3dea-ab86-0522dce5bcc8 | -10.57178 | -46.23478 | 2026-06-22 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1eed0134-39f3-3812-8b9c-ee01064b6510 | -11.05706 | -52.47018 | 2026-06-22 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f4f5313-2dbc-3dd0-a381-3ef422bfa54e | -10.02614 | -59.3468 | 2026-06-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4bdf38da-def0-3580-9fb7-b77e10f7198e | -12.06976 | -48.42929 | 2026-06-22 05:12:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1ae3b4d0-532b-3634-9a5f-c26cc69fe764 | -11.10706 | -54.14098 | 2026-06-22 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a29491b3-de4e-3529-8fd2-75e7b080ec4c | -10.05722 | -48.09239 | 2026-06-22 05:12:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d494011c-89bc-385b-adfa-af386692f791 | -13.30543 | -45.22871 | 2026-06-22 05:12:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e1d12d8c-b1d5-3624-bc82-a71258bf71db | -10.58908 | -53.5198 | 2026-06-22 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 169d018f-1b7b-3110-8595-c16c6d0ef646 | -11.11399 | -54.14678 | 2026-06-22 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |


[Clique aqui para ver as próximas entradas](README8.md)
