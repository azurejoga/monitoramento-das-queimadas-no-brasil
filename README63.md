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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 550055f3-551c-3e66-b3ad-678d27693554 | -9.41978 | -60.42304 | 2026-08-20 05:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae5aa426-1516-3565-aa1b-0d312600a449 | -7.04547 | -56.60936 | 2026-08-20 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88a61388-d1bc-3c44-adcd-3d578b14a27d | -6.79994 | -59.58014 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2836ad79-7920-3bec-a07f-99afb90f700f | -9.11827 | -60.34728 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12383f35-75b5-3bd0-bdb4-314a01837105 | -8.5752 | -54.68218 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14233247-db06-3e31-8a02-57f60178fd1d | -6.7163 | -59.09486 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 247abc68-ac24-3c85-8875-de24b1282f2e | -9.4221 | -60.43145 | 2026-08-20 05:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 29784d8a-006e-3af8-98bb-e95007b6761a | -7.53197 | -55.58357 | 2026-08-20 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3b3eecef-a2f1-37d0-8a02-ecc464da3688 | -6.71073 | -59.10698 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b749150-535a-38bc-aff0-ab1ac31c65be | -6.71137 | -59.10277 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 410db276-fb91-3a69-8055-b49440c26a3b | -7.0137 | -59.59472 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 218d7e46-c5aa-316c-b50e-2ace0065bcf4 | -9.20543 | -59.77131 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aa82d68b-696c-34d9-832c-a213a9043e0e | -11.22323 | -55.05368 | 2026-08-20 05:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7137d678-99bc-3528-a13b-022d1c573d24 | -7.87078 | -63.76522 | 2026-08-20 05:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b27fdfec-29b3-387d-b2b1-8cd8cb694116 | -7.868 | -63.76111 | 2026-08-20 05:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f0bb92c-3c79-3b4c-b763-c7aa53e168b3 | -8.09298 | -51.66436 | 2026-08-20 05:42:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed3a54bc-c35a-3e63-ba03-0f6078708aba | -7.54117 | -55.58499 | 2026-08-20 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3d066a0-54d4-3d12-bc6b-295dd9de359e | -7.0987 | -59.76987 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2bb257e6-2712-38cc-8dd5-c7b2a05301fe | -8.67714 | -54.63925 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3de5abb8-efb9-339f-b287-c1f16ca2ef2c | -8.53924 | -54.78942 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c3afe847-1561-3e8b-8a0b-7cf0706a74e9 | -8.56844 | -54.72542 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c482a15b-25d6-3efc-bd1f-70dcd01739d4 | -8.57488 | -54.67986 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 338c7b98-b1e7-3d4e-9c44-c1bc427e51b6 | -9.21862 | -59.78189 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 591a3a15-2b5c-3c91-a0c3-d385c3257e06 | -11.42339 | -54.32017 | 2026-08-20 05:42:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da9770f3-3d85-396a-8312-43201618c58e | -7.6023 | -60.95007 | 2026-08-20 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42bae299-250a-305c-a8d9-2c3e586d2928 | -11.82962 | -58.83514 | 2026-08-20 05:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| d8b7b840-5d15-34eb-a45d-7d05f9a88bed | -8.67638 | -54.64498 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 06b4e75b-d24f-3f71-8f77-b723f851fec3 | -7.00304 | -59.5929 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63c9b9c0-1de8-3ab0-a381-29db7485c430 | -9.12656 | -51.15284 | 2026-08-20 05:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6b4eff42-bf7c-3c4f-922b-a99ce30acae9 | -11.19795 | -54.0121 | 2026-08-20 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b51df0ec-4879-3ded-ad06-85e5e45dd984 | -7.41445 | -59.99335 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9205c131-ae0b-3f7d-b94e-9a00b9437076 | -9.1236 | -61.6067 | 2026-08-20 05:42:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec580c24-b0b6-3252-b04d-56df7c3ec281 | -11.18535 | -54.02461 | 2026-08-20 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 519b8c0c-15d3-36b0-90f0-d99b50547194 | -9.31956 | -68.66975 | 2026-08-20 05:42:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 915a0d01-8705-3ba1-9ca3-c0c7ea5e8359 | -13.45277 | -51.42642 | 2026-08-20 05:42:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64ea3aae-7afd-36ce-a00b-d6496ec7f7cd | -11.20955 | -55.05171 | 2026-08-20 05:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 06531fd8-5f66-3420-b737-b9637ba705c4 | -6.5948 | -58.96104 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d1089ad-ac8e-308c-b99a-57215abebbbe | -8.55817 | -54.6543 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33d8beed-4817-316f-88b0-1169afb28d0a | -6.86041 | -59.02817 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c71cd52-3816-3601-9b6c-f7fefb91d304 | -8.58093 | -54.75254 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fa147a8a-0f81-3130-9b39-312d541d3039 | -13.60744 | -51.79572 | 2026-08-20 05:42:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2c330b71-3e6c-34ee-b2db-3b402b944b88 | -9.17599 | -57.00882 | 2026-08-20 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4f4523ca-86db-3bb9-8aa1-a66fe9f5d065 | -7.60513 | -60.95425 | 2026-08-20 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fee7b4aa-0f0f-3339-b3c1-b5ad6ee9381f | -11.24201 | -54.82627 | 2026-08-20 05:42:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80415021-d41e-36d6-91a1-7a1530d4d0c2 | -13.61573 | -51.79203 | 2026-08-20 05:42:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 06f52613-4a5f-3037-aed8-abb26099a012 | -8.4959 | -54.88451 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 983322e4-93fb-3f47-b629-bb67731e99ef | -7.708 | -56.72725 | 2026-08-20 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec3853f8-48d8-3912-ae7a-cabfcc34f1e0 | -6.63275 | -59.07935 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9fa44fe5-70cb-3c62-a4a0-1f4894708f29 | -7.60117 | -60.95736 | 2026-08-20 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5aae54bf-0d26-35af-ae17-c6b318b14c36 | -8.56653 | -54.66709 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| faa26d6c-34d5-3b07-8359-3a30a57245dc | -10.75438 | -50.35024 | 2026-08-20 05:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b0e8a102-c8f3-3752-8e5d-75ece6099116 | -8.57299 | -54.77402 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6960117a-a11a-305f-bcc0-57e9c8dd93a4 | -8.53168 | -54.8789 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a81e23e1-fc61-35ba-9b97-2a5ea16dd0f1 | -6.70602 | -59.08901 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dbbe0423-5ace-3dd5-89d9-7963ab240ba8 | -6.85975 | -59.03243 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 69be8f35-d667-34d3-aaf8-7638127293dc | -9.50387 | -51.68084 | 2026-08-20 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4a6bef19-dfef-304a-9e3d-2f78ad627824 | -9.22052 | -59.76934 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3d47f7dd-c19c-3e47-9edb-413da568d415 | -7.06489 | -59.96981 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb2cb070-b773-3b74-bf22-4b67d2c5d287 | -6.89073 | -56.43596 | 2026-08-20 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc186513-fcb2-30b1-9aa4-da97e088039e | -7.37722 | -59.95184 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 578fb31e-a016-32c2-8a14-4ea831012c78 | -6.79639 | -59.57961 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c638b6a6-7841-39a3-b20d-d43eb2d774be | -8.64534 | -62.82307 | 2026-08-20 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2f2a078-db5a-34cc-970e-d858743ed635 | -6.71994 | -59.0954 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7983801d-c606-3198-a0d5-a545edf9000e | -7.61306 | -60.97041 | 2026-08-20 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32123ad5-0d0e-3b93-8d8a-a57e5166670e | -6.95719 | -59.05436 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20f1c271-2a0f-3912-b07b-a0eaf038c20d | -8.71774 | -49.61202 | 2026-08-20 05:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2146b199-441b-398c-ba30-43fc6feffc5a | -11.21896 | -55.04699 | 2026-08-20 05:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 806deef7-4667-31c7-95ca-8adf22db83c6 | -8.40638 | -62.70645 | 2026-08-20 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c44d630e-6ebe-35ec-9677-406678bdd111 | -12.00275 | -53.43838 | 2026-08-20 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| af46ae2b-d200-38f1-aadd-ac799dff9552 | -8.5683 | -54.65783 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3bba0698-ccec-3a99-9597-bb1809c45a4d | -13.60806 | -51.79032 | 2026-08-20 05:42:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 88e45454-e64a-3967-bdbe-b095d9fa2a34 | -11.21181 | -54.0061 | 2026-08-20 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e14f9c0-98f1-3f8f-a29b-90ce37c1b946 | -6.8574 | -59.02338 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a9413dd-7a43-3be2-8b74-36adb543f7c7 | -13.41128 | -54.3713 | 2026-08-20 05:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41bec977-bd12-39f6-ab2f-13276d5e0d68 | -8.66328 | -54.59595 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 052ab37c-cda8-309e-8b1f-132aefe4d743 | -10.91129 | -56.36878 | 2026-08-20 05:42:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b017e9e-88b6-3c55-bcab-ddd936e2cb13 | -7.53497 | -57.65668 | 2026-08-20 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 056db2b5-771e-3e13-aecf-30767b531d35 | -13.60929 | -51.79138 | 2026-08-20 05:42:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 2a70eeb4-11d7-3788-b545-d3f0eac75ee1 | -11.18026 | -54.80522 | 2026-08-20 05:42:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06bb32d5-5875-3694-a1c6-9763327fc5cc | -7.0491 | -56.52336 | 2026-08-20 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9652aa85-b078-37bc-ac1f-7ea17036bf18 | -8.68027 | -54.65677 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85abc859-ba91-32a8-b7be-7be7f4f8decd | -8.6703 | -54.6553 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1d8fd2f0-e5cc-3cad-a684-478bfde7fe48 | -11.58547 | -50.53559 | 2026-08-20 05:42:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 085a03cf-f1f1-3010-96f0-6183d448840a | -6.70346 | -59.10588 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45a8f4e2-b119-3a5c-9084-a17eb4232c46 | -7.60338 | -60.83008 | 2026-08-20 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac4e6e42-467c-34d4-b120-08a67d74f6c2 | -7.01384 | -59.54517 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d033c968-970a-3208-a70a-1b380c14f3c2 | -9.20904 | -59.77188 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 40b9ec80-2b98-315c-a763-6b46dd15b90d | -9.13873 | -60.61649 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8bde1fa-cc72-36b7-9553-6a339d49ea93 | -10.38489 | -61.20677 | 2026-08-20 05:42:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| feecb331-3fdb-386f-9c3c-db206b22fd97 | -6.70174 | -59.09273 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 90fc3ba3-a6a6-359b-9b22-cf363ac7580a | -11.20337 | -54.01273 | 2026-08-20 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01e6297a-a0d5-3b30-8f14-a2d31606ad72 | -10.91867 | -57.18149 | 2026-08-20 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e04eb17-ac1e-35cf-87d7-42a9cd5aa3d8 | -8.58009 | -54.75012 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d6ceb3a9-a7bd-3ad5-8556-472dde574da6 | -9.21925 | -59.77772 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ed16e8c6-b1a7-3530-8c3c-2ea155d9ed5c | -6.69733 | -58.94882 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| af9a6965-14d4-3f9b-a0e6-7c79d401ac5c | -9.10583 | -60.92671 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3f6a0b0f-fa85-3edd-9f9f-6d53548c6fa6 | -6.93263 | -62.8846 | 2026-08-20 05:42:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fea31c4d-aad6-3bbf-8ad6-17cea5397105 | -7.89019 | -61.18783 | 2026-08-20 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 875b72d9-1929-3e4c-835d-a74360599278 | -6.60741 | -58.39123 | 2026-08-20 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bcbf6d53-b654-3db1-ac6d-e0734036b3e7 | -7.10224 | -59.77042 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README64.md)
