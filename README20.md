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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 909209ed-42db-3d8a-8c83-0ca5415a97c0 | -13.87183 | -53.82782 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 392ecbe4-2be2-300b-9208-6876711cc8f5 | -11.98174 | -46.38649 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ce8f4152-2732-3d16-a18f-d2b85fcbc991 | -10.37 | -46.38341 | 2026-08-12 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cde33c63-41af-3f32-a254-b983363d7ed0 | -9.34731 | -47.49862 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 73dc530e-f207-32d6-bf2f-9b081fb07146 | -8.89714 | -60.56131 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8f287d5b-8dda-35cd-9249-d5eb82d1ef8d | -10.09948 | -46.2119 | 2026-08-12 04:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d25761c-a14d-37ef-9d4d-b10e71360a87 | -10.36862 | -46.39277 | 2026-08-12 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 67e265f5-c0a8-3836-bb96-a4c7c63deee9 | -9.34854 | -47.49057 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61168311-2b6e-385e-99fa-108c2dad58ac | -8.9437 | -60.50611 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 587db991-dd30-3623-8382-c04e2cc8ecbd | -11.78219 | -51.86368 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 40785691-4cbe-3aeb-b59f-ab2a189e0640 | -13.6576 | -46.23971 | 2026-08-12 04:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3447279-f953-3a2e-b542-351cfd7d6876 | -13.89014 | -53.7848 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 793ab5ee-028c-34ed-add0-ca0800372e0e | -11.82483 | -51.83394 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 72aba367-40a9-3feb-ba79-aaeeb094a6e2 | -14.49691 | -49.3041 | 2026-08-12 04:51:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a012d838-f8d1-3abf-b504-a92e17314a8b | -11.97255 | -46.39507 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c5408b7-9b88-3a0e-aee1-77d21cf8bf03 | -11.46386 | -46.61029 | 2026-08-12 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20f8295b-f816-3ded-af9a-ec46ef2d5b72 | -11.94771 | -46.34585 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 92247dc6-ddf5-37fa-be32-7f5bfb8d088a | -14.28378 | -45.28112 | 2026-08-12 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68e40e68-25ff-3cff-abd3-06051736b7b1 | -14.51168 | -49.28952 | 2026-08-12 04:51:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9bc65e2c-8685-3851-a37f-b81b630515d5 | -13.88367 | -53.82162 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 43a9dd73-104e-3843-8937-3a08b5515bf4 | -11.49304 | -54.60294 | 2026-08-12 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2ce8d2b7-ca69-3fd9-8543-ec1b39408f7e | -11.82744 | -51.84872 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c7838e68-fa99-3f11-828d-699c54046b6d | -11.4616 | -44.55225 | 2026-08-12 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e3a77ab2-b339-3b80-92c0-aa9605b5ee28 | -7.41447 | -60.00222 | 2026-08-12 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2da31ab6-cc08-3518-8483-fea2fabbe34d | -10.71639 | -47.91864 | 2026-08-12 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d4fd833-5a36-3cf3-bfc9-d2632db12994 | -11.94967 | -46.33196 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ec52f37c-9765-3cc2-892f-2097c790e75a | -15.02592 | -46.593 | 2026-08-12 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88a3cdf6-b175-3edc-b4ad-c91daf5b5b2d | -12.14012 | -48.26984 | 2026-08-12 04:51:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0b4ec7ef-0c7f-3832-8b1a-fa7c4fd616cd | -11.98104 | -46.39136 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b616f70d-445b-36c6-95cc-cbfa8eb4c21a | -11.22881 | -54.85179 | 2026-08-12 04:51:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 960fe903-9dfa-34f3-b34a-f1fc2d910508 | -11.97325 | -46.39016 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fda98f27-7a90-3079-bc0d-3565874c2559 | -13.56392 | -47.63649 | 2026-08-12 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 05f244b0-84c0-3fcc-bde9-4cdbec1bf684 | -11.96237 | -47.31072 | 2026-08-12 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2eaf5853-fbd0-3f32-82f7-7b2e82e33b06 | -9.37729 | -47.44532 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d7bc49a-fca6-362b-8a47-8a34df4385bf | -11.78728 | -51.85348 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07e66521-ba33-3b27-981d-d11ce0915292 | -14.35631 | -54.87249 | 2026-08-12 04:51:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 743a5f08-a590-3b45-a051-e203a5b05aec | -13.30371 | -49.69788 | 2026-08-12 04:51:00 | NPP-375D | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 44f786ca-f398-32f3-a171-c2a12e26e206 | -11.80371 | -51.81568 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6532234d-c7b8-3336-885d-fb6725f8e5b4 | -13.88685 | -53.82512 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 597a3581-a285-3f2b-b046-e7338d5347c5 | -7.40449 | -59.99253 | 2026-08-12 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6a73900-840d-3103-a95f-4ff430c4ca65 | -10.47034 | -46.61754 | 2026-08-12 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6ae5b251-72fe-3b11-b43e-48b548fc930c | -10.90654 | -50.286 | 2026-08-12 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| abc05782-05c0-3e9a-b55a-3d6f2b20a9e3 | -14.29815 | -51.98476 | 2026-08-12 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7efbae63-6b52-39d1-a188-6a4c166f7114 | -14.52094 | -49.29873 | 2026-08-12 04:51:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 28e2c84e-6efa-3384-b9af-32ed9fd63120 | -13.89943 | -53.83589 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 663ab276-f131-3da7-8dd1-8332be509bba | -13.90558 | -53.79983 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 960ec14e-169e-3517-9cab-64ec2d1b0f57 | -13.25587 | -50.37872 | 2026-08-12 04:51:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 493b9873-637e-39a5-8357-606f31f7a6ed | -8.96087 | -60.5094 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f9047e1a-d8c1-3004-ad44-3df2bcfb0239 | -11.4901 | -54.59771 | 2026-08-12 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 615cb096-6420-3464-b6e6-a1e7aaa4bd8e | -9.06935 | -60.40807 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1795eedf-9a46-371f-b224-6edafb915a90 | -9.34009 | -47.52222 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99565d31-0975-3679-b9c9-b4d12b87dd56 | -15.29572 | -48.87401 | 2026-08-12 04:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 10194f44-9d60-3466-8c95-3623007f6a48 | -13.53484 | -46.28386 | 2026-08-12 04:51:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3e7991a-46b4-3c19-aa8f-71bfaebe4b49 | -12.17785 | -50.16253 | 2026-08-12 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e9f7f21-200b-39d6-97ce-8010d9eff90b | -9.34499 | -47.49002 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f2d5441-6a1f-3d60-ae40-8290f9655174 | -9.3341 | -47.53777 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d786d75a-a524-38ed-ae8d-39cb29b38a29 | -10.09877 | -46.21668 | 2026-08-12 04:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72dd0bf4-daa2-3894-9bf8-1bb14eb142c6 | -9.76108 | -60.76218 | 2026-08-12 04:51:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2520de2-779c-38fc-8506-f8705e8dfcd9 | -12.4769 | -44.50237 | 2026-08-12 04:51:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d1fbb51-30c0-36d1-ae80-f7e45c2cd94f | -14.35915 | -53.64194 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46f3c336-90b1-3ec6-b034-bf3e7b7334c8 | -13.5759 | -46.25976 | 2026-08-12 04:51:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e6e9c5e2-c26c-3514-8cca-248d51a0f21a | -14.36141 | -53.23665 | 2026-08-12 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 607b3fec-df3e-3ae9-9484-43dfab1e880d | -14.98982 | -46.58798 | 2026-08-12 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d8bc4ec-0901-3eef-9729-51e808c071e9 | -11.3181 | -45.22176 | 2026-08-12 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98f6863c-3e62-31a1-881a-eb85387a772a | -9.47686 | -47.8296 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be9ef988-ecb5-390f-9b11-d0b2143d1e34 | -13.8415 | -53.79375 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4833f493-33ba-316d-91a6-18f99b71796c | -11.65409 | -50.14112 | 2026-08-12 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4dae6f5-191d-3e23-b161-6371fad6cafa | -13.30258 | -49.70528 | 2026-08-12 04:51:00 | NPP-375D | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 73ea6721-b846-3b51-afaf-53be8cf13e1d | -9.32763 | -47.53262 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 25a0b11d-b159-348c-8257-a2780d693f2a | -13.83399 | -53.81697 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 224d52f5-d76c-3270-ad09-fda324c46a04 | -11.95342 | -46.36181 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7630b8b2-574c-354d-8991-85da0547a75e | -8.95063 | -60.53232 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fd61b4dc-da73-312c-8a3c-7f3a0a5010a3 | -8.95516 | -60.50825 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6d6e2103-f063-3ab5-bfd2-7e5a53c24aea | -12.09935 | -47.19252 | 2026-08-12 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f5b1abd9-79c9-3a10-b0d6-28fec2a058da | -8.95187 | -60.55743 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0fee252-144d-39e7-aa1e-e193af125e10 | -9.46514 | -60.52652 | 2026-08-12 04:51:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48ad1dab-d1b8-329e-956d-06ad07a6c6cf | -13.5396 | -46.27918 | 2026-08-12 04:51:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 813c1242-1991-3842-8f22-3fab4df15684 | -10.23046 | -45.91906 | 2026-08-12 04:51:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 076f5c0c-d9fc-3d75-bf36-c1227751e5a9 | -14.9741 | -46.60653 | 2026-08-12 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 55eeb51b-e891-37e8-96e7-49c10e71b8b9 | -9.62729 | -48.33154 | 2026-08-12 04:51:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ba66de3-e5cb-3781-bd6c-5de2eb071077 | -16.2584 | -49.41967 | 2026-08-12 04:51:00 | NPP-375D | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1bfe229a-878c-308d-84c8-3eb019215fa7 | -12.03187 | -47.80146 | 2026-08-12 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7ce7ea9-6ef7-339c-b87c-13fc1c29eb7d | -14.98759 | -46.59762 | 2026-08-12 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 977a8e70-3fa2-3b61-bef1-2d1e890b1238 | -11.60549 | -54.66752 | 2026-08-12 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 438940c8-c705-316c-986c-0f7b092f2ab8 | -9.75534 | -60.76106 | 2026-08-12 04:51:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc4f6a0c-8fbd-37e4-86b2-b97c967febd5 | -11.46044 | -44.5607 | 2026-08-12 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15da64fe-76d2-3caf-b21a-0690a4be59a4 | -10.84231 | -50.35132 | 2026-08-12 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 401a5f80-57db-32d8-acc0-2d03faf68361 | -15.02528 | -46.59775 | 2026-08-12 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a60a877e-31b3-32ce-b066-e346fe3f7c66 | -8.89972 | -60.58115 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41c8ae9e-193f-308b-aa47-79b7ff3375a4 | -8.94942 | -60.50718 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d007b087-c84e-3678-b6b3-df87e3c61373 | -13.2867 | -49.627 | 2026-08-12 04:51:00 | NPP-375D | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 935f9c75-08e6-3c51-8b6a-9d947865245b | -14.97882 | -46.60196 | 2026-08-12 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30489533-8c40-35c6-a42c-25fd05d4dddd | -15.01252 | -46.60147 | 2026-08-12 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2806eba1-ffab-3f58-a1bd-b0e36d446f0d | -14.3807 | -52.02449 | 2026-08-12 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 44ad88cc-9d14-3ca3-8e60-57e29c072c5e | -8.89551 | -60.57198 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8c5fa6b-7778-3dfd-8328-2c5f5ea7ac89 | -8.8942 | -60.57732 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2eb68fe7-a240-37be-9076-4ecb071d36b2 | -9.37791 | -47.44128 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53680616-9c1e-37ec-830e-73e3aad7b9fc | -13.89723 | -53.80655 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05243368-bbec-3ecc-b3e6-9086f51cc64a | -9.37372 | -47.4448 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf9ec053-b9dc-3347-811e-5ead60328dce | -11.46844 | -46.68718 | 2026-08-12 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README21.md)
