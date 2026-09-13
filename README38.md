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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f5b6238-b017-3f7a-8ff2-66d56d2927df | -6.59666 | -58.84302 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0dfb3564-519f-34a0-81ee-c739c844f14c | -8.11709 | -54.79148 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ffac167-c48f-3b38-a2f8-670cc570d167 | -13.60772 | -47.87952 | 2026-09-13 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 774001c9-2322-3d41-b610-6a93e3052b8e | -7.8577 | -54.69832 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 673e5fe7-e9e1-30d9-8d33-aa8078a459ed | -13.44774 | -48.49399 | 2026-09-13 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 259cec80-554d-308a-849a-4a84c1f8f5f3 | -9.38709 | -50.12463 | 2026-09-13 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 92d50fa3-5bd9-3a23-825f-fad0edff52a0 | -8.11872 | -54.80612 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad486a1c-33e2-388d-a534-556fd7615c30 | -8.01427 | -54.856 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e524b9ab-83ef-3be2-92fa-0399f9adf5d7 | -9.75382 | -47.08785 | 2026-09-13 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc55a84c-dab2-3a93-91a5-6e9b1171a800 | -9.38376 | -50.1241 | 2026-09-13 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d0fa559e-b665-3a26-9a57-f2a97861ec2b | -10.89894 | -47.80864 | 2026-09-13 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 59df2d42-8b82-3e2f-aedc-a5591e75a611 | -10.58264 | -51.3513 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be21bfc2-ef05-3bce-8302-48e4dd46f238 | -14.10646 | -46.35748 | 2026-09-13 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 3e7b492a-2e43-34c5-9d08-e11f508110c9 | -6.06902 | -57.86496 | 2026-09-13 04:51:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3ec2bb2-457f-3e22-b6f9-2a8d8e45d20a | -11.81846 | -46.37679 | 2026-09-13 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e0c49006-de8c-3a05-9ae2-ef91ba04eac4 | -7.63873 | -47.18641 | 2026-09-13 04:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2732c5a6-78cf-34ee-8d20-765d9cc47ef2 | -10.25264 | -57.7028 | 2026-09-13 04:51:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 885355ad-41fd-360b-94d4-9f821889434a | -12.47418 | -57.65208 | 2026-09-13 04:51:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1162f99f-8fb5-3b45-a76b-ab98aa910a91 | -13.36983 | -51.71232 | 2026-09-13 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1c8d92f-4f7e-3c23-8d4c-530c09c7a095 | -9.38431 | -50.1206 | 2026-09-13 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 98c723e9-22f9-3471-8434-061a28ef220a | -8.05275 | -54.85268 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1931fac5-0c87-318b-9a20-260e1b8d0c04 | -6.95478 | -59.75177 | 2026-09-13 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2a7cfbf-c69b-33ec-a2c9-c95b9c4d4eb9 | -7.85455 | -54.69255 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd718e52-3cb1-3f97-86c1-8a49033c3266 | -8.32024 | -49.68895 | 2026-09-13 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d267033-4036-35cf-b38c-b31935298cdc | -7.86326 | -54.71437 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d2172e5-310d-3b2c-8620-b56afcf67edd | -13.61559 | -47.87646 | 2026-09-13 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 118a6ebb-bc4e-3a66-964b-01b7663b03d8 | -10.46214 | -48.64087 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 083a3ec3-2c13-382a-a519-dae0f58fc8c4 | -10.50134 | -51.30119 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b604bf2-8030-3e9a-b988-1fd7f487f915 | -9.36878 | -50.09623 | 2026-09-13 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99f1af11-cc99-3dab-897c-78c81a5300cd | -6.71987 | -50.95878 | 2026-09-13 04:51:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad5d197f-463c-3099-a380-4ca0d247b96d | -6.59128 | -58.84199 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e0bbd4c6-6f51-3a70-b473-4c4f0c7a8c61 | -13.37948 | -48.02053 | 2026-09-13 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b1a9f2b-d44d-35fd-9a29-4541fbd5f4a9 | -9.39928 | -50.13377 | 2026-09-13 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a6864a57-258d-363a-acee-160941376bdb | -13.3665 | -51.71176 | 2026-09-13 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32784e9a-d090-3be9-a1a8-2b3cb465f2f7 | -10.6799 | -54.16305 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 539f8287-8dda-371e-99ea-9b11767d96e7 | -13.31804 | -51.72215 | 2026-09-13 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b9d1a985-a7f5-3d35-b4cd-ee762eaa7610 | -11.24661 | -54.15267 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd6831fc-cbfc-3cb9-971e-7ad0cc0c37b0 | -10.92438 | -48.35359 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b75e0ab1-f20c-3e29-9e8e-862a7b49bee8 | -9.71403 | -54.3594 | 2026-09-13 04:51:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee18613a-d805-3166-8933-8b0aff76affa | -13.14999 | -48.58434 | 2026-09-13 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ba7ff2c-f820-3e19-9c11-6b24fbb63976 | -9.89581 | -47.58648 | 2026-09-13 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e92344ac-124c-3972-8301-bfa89fea29c0 | -13.3147 | -51.72159 | 2026-09-13 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e1ec243d-bd8f-3abe-831a-490b5347c6f0 | -8.81334 | -46.90808 | 2026-09-13 04:51:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3835912e-b661-3abc-9904-b02422988479 | -11.24585 | -54.15709 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3742499c-1d28-3e8d-bdd5-69c72d248ede | -9.69576 | -54.3515 | 2026-09-13 04:51:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8dacd6e1-13f1-33ee-bf1f-76f46f401319 | -6.72293 | -50.46871 | 2026-09-13 04:51:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 14b4d02a-a8cf-317a-885d-41777f95aaa5 | -11.25776 | -54.1319 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 792f564e-bc29-3c93-80df-bd2b182aa288 | -8.02755 | -54.85103 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 270de73b-93a0-396f-aa1e-ecc725924e91 | -9.57703 | -55.159 | 2026-09-13 04:51:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c1bbe10-a5fb-3cd5-8ba8-92ce78c52084 | -10.68285 | -54.16816 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| bb066e2c-5df6-3223-8805-b1f8eef9d102 | -8.86611 | -62.5298 | 2026-09-13 04:51:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b1a0c08e-f80e-3434-8db1-fdb9ff0e3c47 | -7.86846 | -54.69136 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b6087fb-45c8-316b-9a0f-1f11f8c493de | -6.11429 | -57.66559 | 2026-09-13 04:51:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 4734b818-d799-394c-9d89-cd7af1008530 | -5.9792 | -57.76208 | 2026-09-13 04:51:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee968854-0976-3743-8a9b-be36f0aaa143 | -10.92496 | -48.34976 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41643319-3910-3165-954b-21d495bdba83 | -7.0771 | -50.35234 | 2026-09-13 04:51:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ceee16a7-7a8b-3db4-a429-7a382e80579e | -8.81736 | -61.41132 | 2026-09-13 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5303a7b-9e75-3a47-b2d5-ab89790ae549 | -13.75638 | -42.6001 | 2026-09-13 04:51:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 988d01d5-abb1-3372-ba8d-297867f13038 | -6.07976 | -57.86361 | 2026-09-13 04:51:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8b346c06-6097-31e6-8679-62cc479ba39d | -12.67585 | -54.66454 | 2026-09-13 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e3f88fcb-a478-3ad4-8dfb-9cf54f82aa90 | -6.3807 | -58.29252 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b851292-4a01-38ba-83c7-9100fb09aea7 | -10.28381 | -45.32986 | 2026-09-13 04:51:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0792aa6f-a464-3bb4-a242-cb7300ec009d | -6.75701 | -58.96139 | 2026-09-13 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1b242c2-203f-3a5a-94ee-fa85eeb7505c | -8.03158 | -54.85174 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b6506ca-59fd-3cf2-a2a3-e1f777d34360 | -6.06603 | -57.73335 | 2026-09-13 04:51:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 02ed463a-4871-3216-a7e1-80d7875430a7 | -6.36503 | -57.86686 | 2026-09-13 04:51:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9dca1c97-3084-37dc-8977-c0ea1b2bb26f | -8.12614 | -54.81107 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0ab12b4-5b2a-3112-922c-31ee76cd8f26 | -11.04621 | -47.17253 | 2026-09-13 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02174db7-49f8-3c1d-8bde-210c16537a69 | -6.66328 | -58.88327 | 2026-09-13 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 235b2c65-cf6d-3abb-b689-ea6d25138967 | -10.46273 | -48.63708 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e76373e4-81fc-3dd1-9ca4-0b8c014e0fad | -12.6594 | -54.67083 | 2026-09-13 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8afd0557-5ccf-3793-a8c8-94b02526a20c | -11.9867 | -48.64409 | 2026-09-13 04:51:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b115aaec-15f4-3424-8372-e1005316cb5a | -10.93073 | -48.35854 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3e9e5d5-b9d6-3cf5-9b51-0821bc7759b5 | -6.67667 | -58.71443 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97e07e93-43a7-3594-8df4-5b4e325974bd | -7.85556 | -54.69452 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b48f579-6bd2-3feb-8316-6c1be4191a95 | -6.68071 | -58.87926 | 2026-09-13 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7811db21-e284-3409-86a9-e6ab4e7227b8 | -10.58207 | -51.35486 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fec3114b-be26-3a7f-a4af-6e87fdccf1ab | -6.36451 | -57.86974 | 2026-09-13 04:51:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 61fb872a-7c58-3d6d-a8c0-fa264b2b6f15 | -7.37453 | -46.03752 | 2026-09-13 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d12b0c68-f85a-3162-a013-0ae3852a0e1a | -10.54867 | -51.32733 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 38ae35ba-136f-3d47-9822-ba21407405ac | -6.38184 | -58.28683 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58e81e0e-cfa7-38e0-9917-b2ccaa943676 | -8.05575 | -54.85593 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a69d6da-cd12-3701-bdf4-4d7f64821175 | -8.04426 | -54.85028 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6bea800e-401a-335a-a3f1-cdefff7bc919 | -8.1207 | -47.13689 | 2026-09-13 04:51:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c0f83f2-329e-3028-a086-0725193c32c6 | -13.29674 | -51.64153 | 2026-09-13 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d272d1c2-6d0a-3083-8065-e281828016f0 | -11.98613 | -48.64794 | 2026-09-13 04:51:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7779aa5b-0f40-3415-85da-2e6a43418fc1 | -8.0189 | -54.85314 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbb9f8d3-f03e-3def-9df9-e52cc9f51a77 | -10.58034 | -51.36565 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02886ebd-5b62-3543-8df8-4fcfe639b736 | -9.8529 | -48.51759 | 2026-09-13 04:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 639ca8c0-8178-3649-b513-72df46976873 | -6.34742 | -52.74709 | 2026-09-13 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e73cd2e-957d-3c0a-a122-5aa7b8f42694 | -10.94704 | -57.18055 | 2026-09-13 04:51:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bee4519e-b1f7-3073-b1c6-afc8430039c0 | -13.7461 | -42.59917 | 2026-09-13 04:51:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 1d4a9065-e54b-3532-9124-90c75c9fd02d | -13.45302 | -48.50715 | 2026-09-13 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dec8d333-2e46-3851-9888-be4f838ac4fd | -6.27928 | -59.93623 | 2026-09-13 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 38674442-f246-3858-aa97-779310bb4cc1 | -10.53539 | -51.30318 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc48c8d7-6d58-3b5d-9fa3-37c9e9728940 | -12.66762 | -54.66768 | 2026-09-13 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 40f08fe6-7e21-3d3a-a210-6a550980c2ce | -10.57594 | -51.35015 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b9fe99d3-0e28-3d25-af26-9412bab750c1 | -10.55537 | -51.32845 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 41d9485f-efbd-3a2a-aeaf-a9b76768a7e0 | -13.6144 | -47.88478 | 2026-09-13 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d612ebc4-85a6-3efc-9f8c-642567136518 | -13.61195 | -47.87592 | 2026-09-13 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README39.md)
