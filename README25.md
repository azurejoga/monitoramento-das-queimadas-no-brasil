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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 241ecfc1-63cf-3c09-a8ad-dc79347122c0 | -13.89423 | -54.60606 | 2025-06-14 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9e5a776d-8a6c-3e9f-a8f1-74f640a72e72 | -10.2945 | -60.55274 | 2025-06-14 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 032204c2-47b4-3083-b320-d69fc486eeae | -11.1367 | -53.94543 | 2025-06-14 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f92b9a20-a2e6-31d2-b3a8-41183ba60381 | -10.29837 | -57.13874 | 2025-06-14 05:31:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 770cb586-275d-3a51-a8b9-783c623bf695 | -13.90372 | -54.61791 | 2025-06-14 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6de9b055-b920-3513-85f0-fa9af58c4cd9 | -11.56702 | -54.57397 | 2025-06-14 05:31:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e77feef-6bd8-3451-bb0a-464170436352 | -10.04721 | -64.98209 | 2025-06-14 05:31:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 89407a0b-4b4d-3f22-b973-7bf7fc2369e3 | -10.86268 | -54.30147 | 2025-06-14 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c06c2858-3ba6-3c5e-8135-86e4dbda3a7b | -10.76825 | -56.29895 | 2025-06-14 05:31:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1483ed46-2f5b-3cb8-b5ca-584c15c3f9f8 | -11.91486 | -57.47879 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f27e6271-2726-3fa5-9899-c59b6a80f3f6 | -9.46992 | -57.85081 | 2025-06-14 05:31:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e8c5dc4-7955-38ef-aec8-52eb6f3c947d | -10.91708 | -56.83344 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| afe08431-20a6-3ef2-b2a6-97ed85644ccf | -8.88464 | -64.20488 | 2025-06-14 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d3358e5-3785-3136-ae17-1fc9c46776b9 | -10.91779 | -54.7799 | 2025-06-14 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a7c7bd3c-1a78-382e-b6e6-cbfd7a2192c0 | -9.46234 | -57.84616 | 2025-06-14 05:31:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 808cf02d-6b54-3f0d-92aa-88c921759741 | -9.38996 | -57.51762 | 2025-06-14 05:31:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9b3a0d0e-b9bc-37f7-ba2c-541860bf3ebc | -12.61439 | -57.88869 | 2025-06-14 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bca13090-291b-3b7c-8b60-a36a94ab1810 | -10.85472 | -53.78471 | 2025-06-14 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1526633f-9ed3-3bff-89e1-4edfe6b29bf2 | -12.6107 | -57.88413 | 2025-06-14 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7722e92-ce73-3c07-824e-44b89aca0756 | -11.80997 | -54.50201 | 2025-06-14 05:31:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 238c0d30-902e-3e00-ade3-532afa919a28 | -10.29861 | -60.54931 | 2025-06-14 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 389b8964-74d8-33a0-8e32-705504e3d5ad | -11.81109 | -57.35211 | 2025-06-14 05:31:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3ff21414-b0ee-36c4-8959-dbd083a645a1 | -10.36189 | -57.23203 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cc6e15cd-f562-37af-b8a2-81ee573ffe87 | -10.92531 | -56.839 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e327048f-c3a7-3c8b-8eb4-576a0133efac | -12.61861 | -57.88934 | 2025-06-14 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ddd91755-1049-3519-ac1e-75f459019025 | -10.56095 | -52.0166 | 2025-06-14 05:31:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0b821f6-ac3e-3036-b27d-7ef35ebd1d83 | -10.91895 | -54.77096 | 2025-06-14 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 028b9770-aad3-334f-9177-b23795543360 | -13.8996 | -54.60671 | 2025-06-14 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 66c7d5d1-2265-3361-990c-6298910015f3 | -11.91706 | -57.46231 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da47ca95-51ef-32af-8f1c-615f0ab03f41 | -11.80656 | -57.34483 | 2025-06-14 05:31:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 788336ae-2927-39e9-b44b-75c635507f8e | -11.8833 | -54.68333 | 2025-06-14 05:31:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac32c52b-0ad5-3c0a-add8-0c2c8165ac11 | -9.92305 | -65.12233 | 2025-06-14 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 74e656b5-996a-37e0-9772-fa5cf6c38e0a | -10.87236 | -54.30938 | 2025-06-14 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 198f3797-d807-3b2c-8fb3-4c004a4b5063 | -9.87828 | -61.40088 | 2025-06-14 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0e4a72ab-a750-39b4-bff3-647d9bfee5ab | -10.67262 | -56.55848 | 2025-06-14 05:31:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 83beb383-d7b0-3b5a-806e-c2674b3b080f | -11.80597 | -57.34904 | 2025-06-14 05:31:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 46a1ed66-336c-319a-a602-feb5291dfd7c | -10.9221 | -56.82975 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8b56ed40-b584-39cb-a766-94ef6df49cb9 | -10.92248 | -54.78363 | 2025-06-14 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bd9e35f6-91bf-3d52-a7f0-3f6c32b091b0 | -10.52076 | -59.39377 | 2025-06-14 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 155df2e3-861a-311e-ad6b-681867d27c45 | -14.68056 | -53.37402 | 2025-06-14 05:33:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87ad6b4c-b5b5-3360-bad1-f7e1609ace57 | -14.6728 | -53.39046 | 2025-06-14 05:33:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f1e34c49-0683-3d74-922f-5ca86aa9a124 | -14.03903 | -55.13131 | 2025-06-14 05:33:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0085601-1bf7-392b-9e74-7a6f83d9acd7 | -14.20243 | -57.4104 | 2025-06-14 05:33:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f2f0238-03f3-32fa-b5fa-4fb513182dfe | -14.21136 | -57.41148 | 2025-06-14 05:33:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 65e1cc71-1e6e-3e09-a0eb-4389b81c461d | -17.37936 | -53.82285 | 2025-06-14 05:33:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc784246-a922-35c3-8a56-41434998b281 | -14.0346 | -55.12423 | 2025-06-14 05:33:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2790117-f71f-301d-9181-eb728923ef72 | -16.14319 | -60.08051 | 2025-06-14 05:33:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b641662a-288e-3e86-a06c-c4777e287127 | -16.14251 | -60.08543 | 2025-06-14 05:33:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f378e4d1-1af8-3cd8-901f-dccb1b12e90f | -14.20689 | -57.41096 | 2025-06-14 05:33:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| aed151f6-ca2c-3eaa-a833-b1eb4ecc0140 | -18.74057 | -54.19538 | 2025-06-14 05:33:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 54319cdc-ca89-3248-9e90-25d00083e08e | -14.22087 | -57.40812 | 2025-06-14 05:33:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 74d17aa8-befb-3b9e-a31b-e5a09de4bde0 | -14.21758 | -57.3985 | 2025-06-14 05:33:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5dc0f6ca-e232-3fae-a623-c6d62986630b | -13.72551 | -58.68122 | 2025-06-14 05:33:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74f83e0b-0751-333f-b45f-8087e2a48c45 | -13.72144 | -58.68065 | 2025-06-14 05:33:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b1f2cc0-0978-39a9-a9c3-f6bb0a886084 | -18.73476 | -54.1943 | 2025-06-14 05:33:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dbda092c-7fc1-3cac-a6a9-44418acdcfd9 | -15.99404 | -49.81769 | 2025-06-14 05:33:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a434966-bbe9-32e0-bba8-655d4f33cd32 | -14.54798 | -53.67266 | 2025-06-14 05:33:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e96c3f71-2534-3f13-9745-18db37f51e7b | -14.30976 | -59.89307 | 2025-06-14 05:33:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0742221e-a353-360c-b0de-ef4cd184ed23 | -14.68686 | -53.37082 | 2025-06-14 05:33:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| de4738aa-515b-3fd0-bc11-130720a16cdd | -14.22029 | -57.41254 | 2025-06-14 05:33:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce706267-ed4d-3704-8c7c-b31f6ca22f21 | -14.68641 | -53.37487 | 2025-06-14 05:33:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9031f588-76ec-3d2c-bc2a-e2689f3d458a | -14.67233 | -53.39474 | 2025-06-14 05:33:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 268525ab-582f-3cc2-98de-e919c3af735d | -15.99334 | -49.82542 | 2025-06-14 05:33:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1f5be8d-79b2-3099-a02e-d7f6b77a349d | -14.02941 | -55.12356 | 2025-06-14 05:33:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2bfb8253-d497-3410-a9b4-ff56612b194c | -14.67327 | -53.38614 | 2025-06-14 05:33:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6b1ead9b-678b-392b-87b0-c0b37ef328dc | -14.02894 | -55.12385 | 2025-06-14 05:33:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b7a87b8-7827-3bfa-9780-3f1131c5d3ad | -16.14704 | -60.08112 | 2025-06-14 05:33:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b961a586-4d0d-3cd7-a2be-f7f711cc823b | -14.69274 | -53.37143 | 2025-06-14 05:33:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c3af243-6787-32c8-960d-09ec7acdd27c | -14.22145 | -57.40363 | 2025-06-14 05:33:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 25e642f3-64f4-3255-80fc-380919f54dc4 | -14.2164 | -57.40761 | 2025-06-14 05:33:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d30df34c-21a3-3740-a352-0a0c4915827f | -14.21193 | -57.40706 | 2025-06-14 05:33:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8682f73d-454d-3957-ac26-b2d3f606ecf3 | -14.03827 | -55.13777 | 2025-06-14 05:33:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cbf27ecb-a682-3d65-b23a-d5e7688334fa | -14.20747 | -57.40647 | 2025-06-14 05:33:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 868b8de9-5433-3adc-b554-8edd6a7eee50 | -14.54844 | -53.6686 | 2025-06-14 05:33:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0b902fb-21ff-360f-a277-5719472fcfea | -14.20631 | -57.41544 | 2025-06-14 05:33:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 7bbf6414-f6a4-3073-960c-2db047ff3022 | -14.03789 | -55.14095 | 2025-06-14 05:33:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f07564bf-616c-38d9-8e0e-58f2ba560cfd | -14.02853 | -55.12708 | 2025-06-14 05:33:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cafba97-ad10-3504-95c3-e1b13cb2db08 | -14.21582 | -57.41201 | 2025-06-14 05:33:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 49244fe7-9722-3266-aa57-584ae8ab92b5 | -16.13935 | -60.0799 | 2025-06-14 05:33:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a9b0e92-1484-3eb4-a228-b6e26040669d | -14.2121 | -57.4098 | 2025-06-14 05:40:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 940c17e7-935b-34b6-ba1e-4eaf98cb8708 | -6.9605 | -42.8816 | 2025-06-14 05:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 63.2 |
| dd9691ce-e781-3784-a78d-46a70e154880 | -10.94203 | -56.8427 | 2025-06-14 05:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a4ee471c-aed4-3d53-a59c-f64a2a7234b2 | -10.93605 | -56.83645 | 2025-06-14 05:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 3b69f698-07af-3542-93bb-0ab9ecb3707f | -12.62058 | -57.88998 | 2025-06-14 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5e6b94fc-dd0d-3fc8-a913-3f3a5cc64e09 | -10.36674 | -57.23008 | 2025-06-14 05:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 98e2c2bc-68df-3eec-892c-fc9475893cad | -10.36038 | -57.23578 | 2025-06-14 05:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b52f1c9-b9a8-3708-9433-b0911f094f2c | -9.92351 | -59.90488 | 2025-06-14 05:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94ff6a44-3e83-3a11-b306-9c6c7d3a3c9b | -9.3932 | -57.52831 | 2025-06-14 05:53:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d04dda5-6ac2-3bdc-99af-e83528bcf468 | -9.64388 | -67.28821 | 2025-06-14 05:53:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ed7ba5aa-0f77-3b6f-a4ee-32c17a01c2ee | -9.84155 | -63.66768 | 2025-06-14 05:53:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68602d1f-8005-32b6-8953-75bb0e8986f1 | -10.93296 | -56.84419 | 2025-06-14 05:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2f71dccd-7310-3f5e-a901-f300620f272e | -12.62456 | -57.89148 | 2025-06-14 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3f4c90c1-b2c1-3a7f-9113-8d64cfc4d6d2 | -11.91526 | -57.47119 | 2025-06-14 05:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e95a0b4b-b5c9-396a-abf4-cbdf00c74d90 | -9.38849 | -57.52971 | 2025-06-14 05:53:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 16dea91d-3700-38d0-8f28-c0fea558772f | -12.6182 | -57.89079 | 2025-06-14 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 883f3fa3-8490-33b6-af3c-d65162c09669 | -9.38912 | -57.52484 | 2025-06-14 05:53:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ad73b28a-3253-317a-b478-763f74af8e1f | -9.38756 | -57.52256 | 2025-06-14 05:53:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2325ac58-aef0-3d69-8249-1a62df708447 | -10.93467 | -56.84789 | 2025-06-14 05:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 5f1ca13a-759a-302f-8560-f31a12850f98 | -9.36644 | -65.70083 | 2025-06-14 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6e659706-fda7-3152-a182-6e1b6dbd1a87 | -10.28846 | -67.42238 | 2025-06-14 05:53:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README26.md)
